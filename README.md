# AI Research Wiki

An LLM-maintained knowledge base for AI research, following the [LLM Wiki pattern](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f). Obsidian is the IDE; the LLM is the programmer; the wiki is the codebase.

**[Browse the wiki](wiki/index.md)**

## Structure

```
sources/              Raw source documents synced from Readwise Reader (gitignored)
summaries/            LLM-generated summaries of each source (committed)
                      Contains original URL, summary, and main ideas
wiki/                 LLM-generated knowledge pages (summaries, entities, concepts,
                      comparisons, syntheses). LLM owns this entirely.
  index.md            Content catalog of every page, grouped by category
  log.md              Reverse-chronological activity log
CLAUDE.md             Schema defining structure, conventions, and workflows
sync-readwise.py      Script to pull AI-tagged content from Readwise Reader
generate-summaries.sh Script to generate summary docs from raw sources
ingest.sh             Full pipeline: sync → summarize → ingest → PR
.env                  Readwise API token (not committed)
```

## Setup

1. Get a Readwise API token at https://readwise.io/access_token
2. Add it to `.env`:
   ```
   READWISE_TOKEN=rw_xxxxxxxxxxxxx
   ```
3. Sync sources:
   ```bash
   python3 sync-readwise.py
   ```

## Syncing Sources

`sync-readwise.py` pulls documents tagged "AI" from Readwise Reader into `sources/` as markdown files with YAML frontmatter.

- Uses only Python 3 stdlib (no dependencies)
- Incremental sync — only fetches new/updated items since last run
- Tracks state in `sources/.sync-state.json`
- Each document gets a slugified filename (e.g., `attention-is-all-you-need.md`)

After syncing, run `generate-summaries.sh` to create committed summary documents in `summaries/`. Each summary contains the original URL, a concise summary, and main ideas. Wiki pages link to these summaries.

## Using the Wiki

Open this folder as an Obsidian vault. All pages use standard markdown links for cross-references, which work on both GitHub and Obsidian. The graph view shows how everything connects.

### Operations

All operations are performed by asking the LLM (Claude) in conversation:

- **Ingest** — After syncing and summarizing sources, ask Claude to ingest them. It will read the summaries, create/update wiki pages, and maintain cross-references, the index, and the log. Or run `./ingest.sh` for the full automated pipeline.
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
