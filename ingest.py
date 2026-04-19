#!/usr/bin/env python3
"""
Sync sources from Readwise, generate summaries via Claude API,
ingest into wiki, and open a PR.

Usage:
    python3 ingest.py              # sync + summarize + ingest + PR
    python3 ingest.py --skip-sync  # skip Readwise sync
"""

import argparse
import asyncio
import hashlib
import json
import os
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

import anthropic

BASE_DIR = Path(__file__).parent
SOURCES_DIR = BASE_DIR / "sources"
SUMMARIES_DIR = BASE_DIR / "summaries"
SUMMARY_STATE_PATH = SUMMARIES_DIR / ".summary-state.json"
ENV_PATH = BASE_DIR / ".env"

SUMMARIZE_MODEL = "claude-haiku-4-5"
MAX_CONCURRENT = 5

# Static system prompt — kept stable so it caches across all files in the batch.
# The summarized_at value is passed in the user message, not here.
SYSTEM_PROMPT = """\
You are generating summary documents for an AI research wiki.

The user message starts with a metadata line:
  summarized_at: <ISO 8601 UTC datetime>
followed by the raw source document content (markdown with YAML frontmatter).

Produce a summary document with this EXACT format:

---
id: <from raw frontmatter>
title: <from raw frontmatter>
author: <from raw frontmatter>
source_url: <from raw frontmatter>
category: <from raw frontmatter>
tags: <from raw frontmatter>
saved_at: <from raw frontmatter>
summarized_at: <from the summarized_at metadata line above>
---

# <Title>

**Original source:** [<Title>](<source_url>)
**Author:** <Author>

## Summary

<2-3 paragraph summary of the full document>

## Main Ideas

<Bulleted list of 3-7 key ideas, findings, or arguments>

## Key Quotes

<1-3 notable quotes from the source. Omit this section entirely if there are no notable quotes.>

Rules:
- Summarize concisely but substantively (200-400 words for the Summary section).
- If source_url is empty, omit the "Original source" line.
- If author is empty, omit the "Author" line.
- Output ONLY the document content — no preamble, no explanation.
"""

WIKI_INGEST_PROMPT = """\
You are maintaining an AI research wiki. Your job is to ingest source summaries into the wiki.

1. Find all summary files in summaries/*.md that are NOT yet referenced by any wiki page in wiki/*.md
   (search for their filename pattern like ../summaries/filename.md across all wiki pages)

2. For each unreferenced summary:
   - Read it to understand the content
   - Add a reference to the most relevant existing wiki page(s), or create a new page if no good fit exists
   - Use standard markdown links: [Display Title](../summaries/filename.md) for sources, [Page Title](page-name.md) for wiki pages

3. Update wiki/index.md if you created any new pages

4. Prepend an entry to wiki/log.md (newest first) summarizing what was ingested

Follow the conventions in CLAUDE.md. Do not modify summary files.
"""


def get_anthropic_key() -> str:
    key = os.environ.get("ANTHROPIC_API_KEY")
    if key:
        return key.strip()
    if ENV_PATH.exists():
        for line in ENV_PATH.read_text().splitlines():
            line = line.strip()
            if line.startswith("#") or "=" not in line:
                continue
            k, _, v = line.partition("=")
            if k.strip() == "ANTHROPIC_API_KEY":
                return v.strip().strip("'\"")
    print("Error: ANTHROPIC_API_KEY not found. Set it as env var or in .env", file=sys.stderr)
    sys.exit(1)


def find_new_sources() -> list[str]:
    """Return filenames in sources/ whose content hash is new or changed."""
    state = json.loads(SUMMARY_STATE_PATH.read_text()) if SUMMARY_STATE_PATH.exists() else {}
    new_files = []
    for f in sorted(SOURCES_DIR.glob("*.md")):
        content_hash = hashlib.sha256(f.read_bytes()).hexdigest()[:16]
        if f.name not in state or state[f.name] != content_hash:
            new_files.append(f.name)
    return new_files


def update_summary_state(filenames: list[str]) -> None:
    state = json.loads(SUMMARY_STATE_PATH.read_text()) if SUMMARY_STATE_PATH.exists() else {}
    for name in filenames:
        src = SOURCES_DIR / name
        if src.exists() and (SUMMARIES_DIR / name).exists():
            state[name] = hashlib.sha256(src.read_bytes()).hexdigest()[:16]
    SUMMARY_STATE_PATH.write_text(json.dumps(state, indent=2, sort_keys=True) + "\n")


async def summarize_file(
    client: anthropic.AsyncAnthropic,
    filename: str,
    semaphore: asyncio.Semaphore,
) -> bool:
    src_path = SOURCES_DIR / filename
    dst_path = SUMMARIES_DIR / filename

    content = src_path.read_text()
    summarized_at = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    user_content = f"summarized_at: {summarized_at}\n\n{content}"

    async with semaphore:
        try:
            response = await client.messages.create(
                model=SUMMARIZE_MODEL,
                max_tokens=2048,
                system=[{
                    "type": "text",
                    "text": SYSTEM_PROMPT,
                    "cache_control": {"type": "ephemeral"},
                }],
                messages=[{"role": "user", "content": user_content}],
            )
            dst_path.write_text(response.content[0].text)
            print(f"  Summarized: {filename}")
            return True
        except Exception as e:
            print(f"  Error summarizing {filename}: {e}", file=sys.stderr)
            return False


async def summarize_all(filenames: list[str]) -> list[str]:
    """Summarize files in parallel. Returns list of successfully summarized filenames."""
    api_key = get_anthropic_key()
    client = anthropic.AsyncAnthropic(api_key=api_key)
    semaphore = asyncio.Semaphore(MAX_CONCURRENT)
    tasks = [summarize_file(client, f, semaphore) for f in filenames]
    results = await asyncio.gather(*tasks)
    return [f for f, ok in zip(filenames, results) if ok]


def run(cmd: list[str], **kwargs) -> subprocess.CompletedProcess:
    return subprocess.run(cmd, check=True, **kwargs)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--skip-sync", action="store_true", help="Skip Readwise sync")
    args = parser.parse_args()

    os.chdir(BASE_DIR)

    # 1. Sync from Readwise
    if not args.skip_sync:
        print("==> Syncing sources from Readwise...")
        run(["python3", "sync-readwise.py"])

    # 2. Find new source files — early exit if nothing changed
    print("==> Checking for new source files...")
    new_files = find_new_sources()
    if not new_files:
        print("==> Nothing to ingest. Exiting.")
        sys.exit(0)
    print(f"==> Found {len(new_files)} new/updated source(s) to summarize.")

    # 3. Summarize via Claude API (parallel)
    SUMMARIES_DIR.mkdir(exist_ok=True)
    print("==> Generating summaries via Claude API...")
    summarized = asyncio.run(summarize_all(new_files))
    update_summary_state(summarized)

    if not summarized:
        print("==> No summaries generated. Exiting.", file=sys.stderr)
        sys.exit(1)

    # 4. Create git branch
    branch = f"ingest/{datetime.now().strftime('%Y-%m-%d-%H%M%S')}"
    print(f"==> Creating branch: {branch}")
    run(["git", "checkout", "-b", branch])

    # 5. Wiki ingest via claude CLI (agentic — needs tool use across wiki pages)
    print("==> Running Claude to ingest summaries into wiki...")
    run(
        ["claude", "-p", "--permission-mode", "auto",
         "--allowedTools", "Read Edit Write Glob Grep Bash"],
        input=WIKI_INGEST_PROMPT,
        text=True,
    )

    # 6. Check for changes — clean up and exit if wiki was not modified
    no_changes = (
        subprocess.run(["git", "diff", "--quiet"]).returncode == 0
        and subprocess.run(["git", "diff", "--cached", "--quiet"]).returncode == 0
    )
    if no_changes:
        print("==> No wiki changes. Cleaning up branch.")
        run(["git", "checkout", "main"])
        run(["git", "branch", "-d", branch])
        sys.exit(0)

    # 7. Commit, push, open PR
    print("==> Committing changes...")
    run(["git", "add", "wiki/", "summaries/"])
    run(["git", "commit", "-m",
         f"Ingest new sources into wiki ({datetime.now().strftime('%Y-%m-%d')})"])

    print("==> Pushing branch...")
    run(["git", "push", "-u", "origin", branch])

    print("==> Creating pull request...")
    pr_body = (
        "## Summary\n\n"
        "Automated ingest of new/unreferenced source documents into the wiki.\n\n"
        "Review the diff to see exactly what changed in each wiki page.\n\n"
        "See `wiki/log.md` for a summary of what was ingested.\n"
    )
    result = subprocess.run(
        ["gh", "pr", "create",
         "--title", f"Wiki ingest {datetime.now().strftime('%Y-%m-%d')}",
         "--body", pr_body],
        capture_output=True, text=True, check=True,
    )
    print("==> Done! PR created:")
    print(result.stdout.strip())


if __name__ == "__main__":
    main()
