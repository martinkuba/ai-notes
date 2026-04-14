#!/usr/bin/env python3
"""Sync AI-tagged documents from Readwise Reader to local markdown sources."""

import html.parser
import json
import os
import re
import sys
import time
import unicodedata
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

BASE_DIR = Path(__file__).parent
SOURCES_DIR = BASE_DIR / "sources"
SYNC_STATE_PATH = SOURCES_DIR / ".sync-state.json"
ENV_PATH = BASE_DIR / ".env"
API_URL = "https://readwise.io/api/v3/list/"
REQUEST_DELAY = 3  # seconds between API requests
MAX_RETRIES = 3


# --- HTML to Markdown ---

class HTMLToMarkdown(html.parser.HTMLParser):
    """Converts simple HTML to markdown. Handles common tags; strips the rest."""

    BLOCK_TAGS = {"p", "div", "article", "section", "main", "header", "footer"}
    HEADING_TAGS = {"h1", "h2", "h3", "h4", "h5", "h6"}
    LIST_TAGS = {"ul", "ol"}

    def __init__(self):
        super().__init__()
        self.output = []
        self.current_link = None
        self.link_text = []
        self.in_pre = False
        self.in_code = False
        self.list_stack = []  # stack of "ul" or "ol"
        self.ol_counters = []  # counters for nested ol
        self.in_blockquote = False

    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)
        if tag in self.HEADING_TAGS:
            level = int(tag[1])
            self.output.append(f"\n\n{'#' * level} ")
        elif tag in self.BLOCK_TAGS:
            self.output.append("\n\n")
        elif tag == "br":
            self.output.append("\n")
        elif tag == "a":
            self.current_link = attrs_dict.get("href", "")
            self.link_text = []
        elif tag in ("strong", "b"):
            self.output.append("**")
        elif tag in ("em", "i"):
            self.output.append("*")
        elif tag == "pre":
            self.in_pre = True
            self.output.append("\n\n```\n")
        elif tag == "code" and not self.in_pre:
            self.in_code = True
            self.output.append("`")
        elif tag in self.LIST_TAGS:
            self.list_stack.append(tag)
            if tag == "ol":
                self.ol_counters.append(0)
            self.output.append("\n")
        elif tag == "li":
            indent = "  " * (len(self.list_stack) - 1)
            if self.list_stack and self.list_stack[-1] == "ol":
                self.ol_counters[-1] += 1
                self.output.append(f"{indent}{self.ol_counters[-1]}. ")
            else:
                self.output.append(f"{indent}- ")
        elif tag == "blockquote":
            self.in_blockquote = True
            self.output.append("\n\n> ")
        elif tag == "img":
            alt = attrs_dict.get("alt", "")
            src = attrs_dict.get("src", "")
            if src:
                self.output.append(f"![{alt}]({src})")

    def handle_endtag(self, tag):
        if tag in self.HEADING_TAGS:
            self.output.append("\n")
        elif tag in self.BLOCK_TAGS:
            self.output.append("\n")
        elif tag == "a":
            text = "".join(self.link_text)
            if self.current_link:
                self.output.append(f"[{text}]({self.current_link})")
            else:
                self.output.append(text)
            self.current_link = None
            self.link_text = []
        elif tag in ("strong", "b"):
            self.output.append("**")
        elif tag in ("em", "i"):
            self.output.append("*")
        elif tag == "pre":
            self.in_pre = False
            self.output.append("\n```\n")
        elif tag == "code" and not self.in_pre:
            self.in_code = False
            self.output.append("`")
        elif tag in self.LIST_TAGS:
            if self.list_stack:
                popped = self.list_stack.pop()
                if popped == "ol" and self.ol_counters:
                    self.ol_counters.pop()
            self.output.append("\n")
        elif tag == "li":
            self.output.append("\n")
        elif tag == "blockquote":
            self.in_blockquote = False
            self.output.append("\n")

    def handle_data(self, data):
        if self.current_link is not None:
            self.link_text.append(data)
        else:
            if self.in_blockquote and "\n" in data:
                data = data.replace("\n", "\n> ")
            self.output.append(data)

    def get_markdown(self):
        text = "".join(self.output)
        # Collapse 3+ newlines into 2
        text = re.sub(r"\n{3,}", "\n\n", text)
        return text.strip()


def html_to_markdown(html_content):
    """Convert HTML string to markdown."""
    if not html_content:
        return ""
    parser = HTMLToMarkdown()
    parser.feed(html_content)
    return parser.get_markdown()


# --- Slug generation ---

def slugify(title, max_len=60):
    """Convert a title to a lowercase hyphen-separated slug."""
    if not title:
        return "untitled"
    # Unicode normalize and strip to ASCII
    text = unicodedata.normalize("NFKD", title)
    text = text.encode("ascii", "ignore").decode("ascii")
    text = text.lower()
    # Replace non-alphanumeric with hyphens
    text = re.sub(r"[^a-z0-9]+", "-", text)
    text = text.strip("-")
    # Truncate on a hyphen boundary
    if len(text) > max_len:
        text = text[:max_len].rsplit("-", 1)[0]
    return text or "untitled"


# --- Sync state ---

def load_sync_state():
    if SYNC_STATE_PATH.exists():
        return json.loads(SYNC_STATE_PATH.read_text())
    return {"last_updated_after": None, "synced_ids": {}}


def save_sync_state(state):
    SOURCES_DIR.mkdir(parents=True, exist_ok=True)
    SYNC_STATE_PATH.write_text(json.dumps(state, indent=2) + "\n")


# --- Token ---

def get_token():
    """Read Readwise API token from env var or .env file."""
    token = os.environ.get("READWISE_TOKEN")
    if token:
        return token.strip()
    if ENV_PATH.exists():
        for line in ENV_PATH.read_text().splitlines():
            line = line.strip()
            if line.startswith("#") or "=" not in line:
                continue
            key, _, value = line.partition("=")
            if key.strip() == "READWISE_TOKEN":
                return value.strip().strip("'\"")
    print("Error: READWISE_TOKEN not found. Set it as an env var or in .env", file=sys.stderr)
    sys.exit(1)


# --- API ---

def api_request(token, params):
    """Make a GET request to the Readwise Reader API with retries."""
    url = API_URL + "?" + urllib.parse.urlencode({k: v for k, v in params.items() if v is not None})
    req = urllib.request.Request(url, headers={"Authorization": f"Token {token}"})

    for attempt in range(MAX_RETRIES):
        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                return json.loads(resp.read().decode())
        except urllib.error.HTTPError as e:
            if e.code == 429:
                retry_after = int(e.headers.get("Retry-After", 10))
                print(f"  Rate limited. Waiting {retry_after}s...")
                time.sleep(retry_after)
            elif e.code >= 500:
                wait = 2 ** (attempt + 1)
                print(f"  Server error {e.code}. Retrying in {wait}s...")
                time.sleep(wait)
            else:
                print(f"Error: API returned {e.code}: {e.read().decode()}", file=sys.stderr)
                sys.exit(1)
        except urllib.error.URLError as e:
            wait = 2 ** (attempt + 1)
            print(f"  Network error: {e.reason}. Retrying in {wait}s...")
            time.sleep(wait)

    print("Error: Max retries exceeded.", file=sys.stderr)
    sys.exit(1)


def fetch_documents(token, updated_after=None):
    """Fetch all AI-tagged documents, handling pagination."""
    documents = []
    params = {"tag": "ai", "withHtmlContent": "true"}
    if updated_after:
        params["updatedAfter"] = updated_after

    page = 1
    while True:
        print(f"  Fetching page {page}...")
        data = api_request(token, params)
        results = data.get("results", [])
        documents.extend(results)

        next_cursor = data.get("nextPageCursor")
        if not next_cursor:
            break

        params["pageCursor"] = next_cursor
        page += 1
        time.sleep(REQUEST_DELAY)

    return documents


# --- Markdown generation ---

def yaml_str(value):
    """Format a value for YAML frontmatter."""
    if value is None:
        return '""'
    s = str(value)
    if any(c in s for c in ":#[]{}|>&*!%@`,"):
        return f'"{s}"'
    return f'"{s}"'


def document_to_markdown(doc):
    """Convert a Readwise document dict to a markdown string with frontmatter."""
    tags = sorted(doc.get("tags", {}).keys()) if isinstance(doc.get("tags"), dict) else []
    tags_yaml = "[" + ", ".join(tags) + "]" if tags else "[]"

    frontmatter_lines = [
        "---",
        f"id: {yaml_str(doc.get('id', ''))}",
        f"title: {yaml_str(doc.get('title', 'Untitled'))}",
        f"author: {yaml_str(doc.get('author', ''))}",
        f"source_url: {yaml_str(doc.get('source_url') or doc.get('url', ''))}",
        f"category: {yaml_str(doc.get('category', ''))}",
        f"tags: {tags_yaml}",
        f"saved_at: {yaml_str(doc.get('saved_at', ''))}",
        f"synced_at: {yaml_str(datetime.now(timezone.utc).isoformat())}",
        "---",
    ]

    title = doc.get("title") or "Untitled"
    body_parts = ["\n".join(frontmatter_lines), f"\n# {title}\n"]

    # Content: prefer html_content, fall back to summary
    html_content = doc.get("html_content") or doc.get("content")
    if html_content:
        md = html_to_markdown(html_content)
        if md:
            body_parts.append(md)
    elif doc.get("summary"):
        body_parts.append(doc["summary"])

    # User notes
    notes = doc.get("notes")
    if notes:
        body_parts.append(f"\n## Notes\n\n{notes}")

    return "\n".join(body_parts) + "\n"


# --- Sync ---

def resolve_slug(doc, state):
    """Get the slug for a document, reusing existing or generating new."""
    doc_id = doc["id"]
    synced_ids = state.get("synced_ids", {})

    # Reuse existing slug
    if doc_id in synced_ids:
        return synced_ids[doc_id]["slug"]

    # Generate new slug
    title = doc.get("title") or ""
    slug = slugify(title)
    if not slug or slug == "untitled":
        slug = f"untitled-{doc_id[:8]}"

    # Check for collisions with existing slugs
    existing_slugs = {info["slug"] for info in synced_ids.values()}
    if slug in existing_slugs:
        slug = f"{slug}-{doc_id[:6]}"

    return slug


def sync_document(doc, state):
    """Write a document to sources/ and update state. Returns (slug, is_new)."""
    doc_id = doc["id"]
    synced_ids = state.setdefault("synced_ids", {})
    is_new = doc_id not in synced_ids

    # Check if update is needed
    if not is_new:
        prev_updated = synced_ids[doc_id].get("updated_at", "")
        curr_updated = doc.get("updated_at", "")
        if curr_updated and prev_updated and curr_updated <= prev_updated:
            return synced_ids[doc_id]["slug"], None  # no change

    slug = resolve_slug(doc, state)
    md = document_to_markdown(doc)

    SOURCES_DIR.mkdir(parents=True, exist_ok=True)
    filepath = SOURCES_DIR / f"{slug}.md"
    filepath.write_text(md)

    synced_ids[doc_id] = {
        "slug": slug,
        "updated_at": doc.get("updated_at", ""),
    }

    return slug, is_new


def main():
    token = get_token()
    state = load_sync_state()
    updated_after = state.get("last_updated_after")

    if updated_after:
        print(f"Fetching documents updated after {updated_after}...")
    else:
        print("First sync — fetching all AI-tagged documents...")

    documents = fetch_documents(token, updated_after)

    # Filter out child documents (highlights)
    documents = [d for d in documents if not d.get("parent_id")]

    if not documents:
        print("No new or updated documents found.")
        return

    new_count = 0
    updated_count = 0
    skipped_count = 0
    results = []

    for doc in documents:
        slug, is_new = sync_document(doc, state)
        if is_new is None:
            skipped_count += 1
        elif is_new:
            new_count += 1
            results.append(f"  [NEW] {slug}.md — {doc.get('title', 'Untitled')}")
        else:
            updated_count += 1
            results.append(f"  [UPD] {slug}.md — {doc.get('title', 'Untitled')}")

    # Update last_updated_after to max updated_at seen
    timestamps = [d.get("updated_at", "") for d in documents if d.get("updated_at")]
    if timestamps:
        state["last_updated_after"] = max(timestamps)

    save_sync_state(state)

    print(f"\nSynced {new_count} new, {updated_count} updated ({skipped_count} unchanged).")
    for line in results:
        print(line)


if __name__ == "__main__":
    main()
