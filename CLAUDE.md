# AI Research Wiki — Schema

This is an LLM-maintained knowledge base for AI research, following the "LLM Wiki" pattern. Obsidian is the IDE; the LLM is the programmer; the wiki is the codebase.

## Structure

```
sources/    — Raw, immutable source documents (articles, papers, images, data).
               LLM reads but NEVER modifies files here.
wiki/       — LLM-generated markdown pages (summaries, entity pages, concept pages,
               comparisons, syntheses). LLM owns this entirely.
wiki/index.md — Content catalog of every page with a one-line summary, grouped by
               category. Updated on every ingest.
wiki/log.md   — Append-only chronological activity log.
CLAUDE.md     — This file. Schema and conventions. Co-evolved by human and LLM.
```

## Conventions

- **Links**: Use standard markdown links for compatibility with both Obsidian and GitHub. Link liberally.
  - Wiki-to-wiki: `[Page Title](page-name.md)`
  - Wiki-to-source: `[Source Title](../sources/filename.md)`
- **File names**: Lowercase, hyphen-separated (e.g., `transformer-architecture.md`).
- **Headings**: Each wiki page starts with an H1 title matching its topic.
- **Tags**: Use YAML frontmatter tags where helpful (e.g., `tags: [llm, architecture, attention]`).

## Sources Pipeline

Sources are synced from Readwise Reader using `sync-readwise.py`. Only items tagged "AI" in Readwise are pulled.

```bash
python3 sync-readwise.py
```

- Requires `READWISE_TOKEN` in `.env` or as an env var (get it at readwise.io/access_token)
- Fetches incrementally — only new/updated items since last sync
- Writes one markdown file per document into `sources/` with YAML frontmatter
- Tracks sync state in `sources/.sync-state.json`

After syncing, run an Ingest operation on new sources to integrate them into the wiki.

## Operations

### Ingest
When the user drops a new source into `sources/` or provides a URL/content to ingest:
1. Read the source material.
2. Discuss findings with the user.
3. Create a summary page in `wiki/` (under the Sources category in index).
4. Create or update related wiki pages — entity pages, concept pages, comparisons.
   Aim for 10-15 page touches per ingest to build cross-references.
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
