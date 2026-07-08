# AI Research Wiki

An LLM-maintained knowledge base for AI research, following the [LLM Wiki pattern](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f). Obsidian is the IDE; the LLM is the programmer; the wiki is the codebase.

**[Browse the wiki](wiki/index.md)**

## Structure

```
sources/          Raw source documents synced from Readwise Reader (gitignored)
summaries/        LLM-generated summaries of each source (committed)
                  Contains original URL, summary, and main ideas
wiki/             LLM-generated knowledge pages (summaries, entities, concepts,
                  comparisons, syntheses). LLM owns this entirely.
  index.md        Content catalog of every page, grouped by category
  log.md          Reverse-chronological activity log
CLAUDE.md         Schema defining structure, conventions, and workflows
sync-readwise.py  Pulls content tagged "AI" and "kb" from Readwise Reader into sources/
ingest.py         Full pipeline: sync → summarize → ingest → PR
.env              API tokens (not committed)
```

## Setup

1. Add your Readwise token to `.env`:
   ```
   READWISE_TOKEN=rw_xxxxxxxxxxxxx
   ```
   - Readwise token: https://readwise.io/access_token
2. Ensure `claude` (Claude Code CLI) is on your PATH — summarization and wiki ingest both run through it. A Claude Code subscription is required.

## Running the Pipeline

```bash
python3 ingest.py              # sync + summarize + ingest + open PR
python3 ingest.py --skip-sync  # skip Readwise sync (sources already up to date)
```

`ingest.py` runs the full pipeline:

1. **Sync** — pulls documents tagged both "AI" and "kb" from Readwise Reader into `sources/` (incremental, stdlib only, tracks state in `sources/.sync-state.json`)
2. **Summarize** — generates summary docs in `summaries/` via the Claude CLI (`claude-haiku-4-5-20251001`), parallelized up to 5 concurrent requests; skips sources whose content hasn't changed
3. **Ingest** — runs Claude Code to read summaries and create/update wiki pages, cross-references, index, and log
4. **PR** — commits changes and opens a pull request

Early exit (no branch created) if nothing is new after sync.

### Recovery

If a run fails partway through — after summarize but before ingest or PR — you can resume from the ingest step without re-syncing or re-summarizing:

```bash
git checkout <the ingest branch>   # branch created during the failed run
python3 ingest.py --resume
```

`--resume` skips steps 1–2, runs the wiki ingest against the existing summaries, then commits, pushes, and creates or updates the PR. Use it when you see summaries in `summaries/` but no (or an incomplete) PR.

## Using the Wiki

Open this folder as an Obsidian vault. All pages use standard markdown links for cross-references, which work on both GitHub and Obsidian. The graph view shows how everything connects.

### Operations

All operations are performed by asking the LLM (Claude) in conversation:

- **Ingest** — Run `python3 ingest.py` for the full automated pipeline, or ask Claude directly to ingest summaries. Claude reads the summaries, creates/updates wiki pages, and maintains cross-references, the index, and the log.
- **Query** — Ask questions about the content. Claude synthesizes answers from wiki pages with citations. Good answers can be filed as new wiki pages.
- **Lint** — Ask Claude to audit the wiki for contradictions, stale claims, orphaned pages, or gaps.

### Conventions

- File names: lowercase, hyphen-separated (e.g., `transformer-architecture.md`)
- Each page starts with an H1 title
- Standard markdown links (work on both GitHub and Obsidian):
  - Wiki-to-wiki: `[Page Title](page-name.md)`
  - Wiki-to-source: `[Source Title](../summaries/filename.md)`
- YAML frontmatter tags where helpful (e.g., `tags: [llm, architecture]`)
- Log entries are reverse-chronological (newest first)
