#!/usr/bin/env bash
#
# Sync sources from Readwise, ingest into wiki, and open a PR.
#
# Usage:
#   ./ingest.sh              # sync + ingest + PR
#   ./ingest.sh --skip-sync  # ingest only (sources already updated)
#
set -euo pipefail
cd "$(dirname "$0")"

SKIP_SYNC=false
if [[ "${1:-}" == "--skip-sync" ]]; then
    SKIP_SYNC=true
fi

# 1. Sync sources from Readwise
if [[ "$SKIP_SYNC" == false ]]; then
    echo "==> Syncing sources from Readwise..."
    python3 sync-readwise.py
fi

# 2. Create a branch for the ingest
BRANCH="ingest/$(date +%Y-%m-%d-%H%M%S)"
echo "==> Creating branch: $BRANCH"
git checkout -b "$BRANCH"

# 3. Generate summaries for new/changed sources
echo "==> Generating summaries for new sources..."
bash generate-summaries.sh

# 4. Run Claude to ingest new/unreferenced summaries into wiki
echo "==> Running Claude to ingest summaries into wiki..."
claude -p --permission-mode auto --allowedTools "Read Edit Write Glob Grep Bash" << 'PROMPT'
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
PROMPT

# 4. Check if there are changes to commit
if git diff --quiet && git diff --cached --quiet; then
    echo "==> No wiki changes. Cleaning up branch."
    git checkout main
    git branch -d "$BRANCH"
    exit 0
fi

# 5. Commit and push
echo "==> Committing changes..."
git add wiki/ summaries/
git commit -m "Ingest new sources into wiki ($(date +%Y-%m-%d))"

echo "==> Pushing branch..."
git push -u origin "$BRANCH"

# 6. Create PR
echo "==> Creating pull request..."
PR_URL=$(gh pr create \
    --title "Wiki ingest $(date +%Y-%m-%d)" \
    --body "$(cat <<'EOF'
## Summary

Automated ingest of new/unreferenced source documents into the wiki.

Review the diff to see exactly what changed in each wiki page.

See `wiki/log.md` for a summary of what was ingested.
EOF
)" 2>&1)

echo "==> Done! PR created:"
echo "$PR_URL"
