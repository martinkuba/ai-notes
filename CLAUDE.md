# AI Research Wiki — Schema

This is an LLM-maintained knowledge base for AI research, following the "LLM Wiki" pattern. Obsidian is the IDE; the LLM is the programmer; the wiki is the codebase.

## Structure

```
sources/      — Raw, immutable source documents downloaded from Readwise.
                 Gitignored. LLM reads during summary generation only.
summaries/    — LLM-generated summary documents (one per source).
                 Committed. Contains source URL, summary, and main ideas.
wiki/         — LLM-generated knowledge pages (summaries, entity pages, concept pages,
                 comparisons, syntheses). LLM owns this entirely.
wiki/index.md — Content catalog of every page with a one-line summary, grouped by
                 category. Updated on every ingest.
wiki/log.md   — Append-only chronological activity log.
CLAUDE.md     — This file. Schema and conventions. Co-evolved by human and LLM.
```

## Conventions

- **Links**: Use standard markdown links for compatibility with both Obsidian and GitHub. Link liberally.
  - Wiki-to-wiki: `[Page Title](page-name.md)`
  - Wiki-to-source: `[Source Title](../summaries/filename.md)`
- **File names**: Lowercase, hyphen-separated (e.g., `transformer-architecture.md`).
- **Headings**: Each wiki page starts with an H1 title matching its topic.
- **Tags**: Use YAML frontmatter tags where helpful (e.g., `tags: [llm, architecture, attention]`).

## Sources Pipeline

### 1. Sync raw sources

Sources are synced from Readwise Reader using `sync-readwise.py`. Only items tagged both "AI" and "kb" in Readwise are pulled.

```bash
python3 sync-readwise.py
```

- Requires `READWISE_TOKEN` in `.env` or as an env var (get it at readwise.io/access_token)
- Fetches incrementally — only new/updated items since last sync
- Writes one markdown file per document into `sources/` with YAML frontmatter
- Tracks sync state in `sources/.sync-state.json`

### 2. Generate summaries

After syncing, run `generate-summaries.sh` to create summary documents in `summaries/`.

```bash
bash generate-summaries.sh
```

- Reads raw source files from `sources/`, generates concise summaries in `summaries/`
- Each summary contains: link to original URL, summary paragraphs, main ideas list
- Uses content hashing for incremental processing — only new/changed sources are summarized
- Tracks state in `summaries/.summary-state.json`

### 3. Ingest into wiki

Run an Ingest operation on new summaries to integrate them into the wiki. The full pipeline is automated by `ingest.sh`.

## Operations

### Ingest
When new summaries are available in `summaries/`:
1. Read the summary documents.
2. Discuss findings with the user.
3. Create or update related wiki pages — entity pages, concept pages, comparisons.
   Aim for 10-15 page touches per ingest to build cross-references.
4. Use `[Source Title](../summaries/filename.md)` when linking to source summaries.
5. Update `wiki/index.md` with new/changed pages.
6. Prepend an entry to `wiki/log.md` (reverse-chronological — newest first).

### Query
When the user asks a question:
1. Search relevant wiki pages and synthesize an answer with `[[citations]]`.
2. If the answer produces a worthwhile standalone insight, offer to file it as a new wiki page.
3. Good explorations compound into the knowledge base.

### Lint
Periodically (or on request), audit the wiki for:
- Contradictions between pages
- Stale claims that need revisiting
- Orphaned pages (not linked from anywhere)
- Missing cross-references
- Gaps that suggest new research directions
