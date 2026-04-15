#!/usr/bin/env bash
#
# Generate summary documents from raw source files.
#
# Reads sources/*.md, generates concise summaries in summaries/.
# Uses content hashing for incremental processing — only new/changed sources.
#
# Usage:
#   bash generate-summaries.sh
#
set -euo pipefail
cd "$(dirname "$0")"

SOURCES_DIR="sources"
SUMMARIES_DIR="summaries"
STATE_FILE="$SUMMARIES_DIR/.summary-state.json"

# Check that sources directory exists and has files
if [ ! -d "$SOURCES_DIR" ]; then
    echo "==> Error: sources/ directory not found. Run sync-readwise.py first."
    exit 1
fi

SOURCE_COUNT=$(find "$SOURCES_DIR" -maxdepth 1 -name '*.md' | wc -l | tr -d ' ')
if [ "$SOURCE_COUNT" -eq 0 ]; then
    echo "==> No source files found in sources/. Run sync-readwise.py first."
    exit 1
fi

# Ensure summaries dir exists
mkdir -p "$SUMMARIES_DIR"

# Find source files that need summarization
NEW_FILES=$(python3 -c "
import json, hashlib
from pathlib import Path

sources_dir = Path('$SOURCES_DIR')
summaries_dir = Path('$SUMMARIES_DIR')
state_path = Path('$STATE_FILE')

state = json.loads(state_path.read_text()) if state_path.exists() else {}

new_files = []
for f in sorted(sources_dir.glob('*.md')):
    content_hash = hashlib.sha256(f.read_bytes()).hexdigest()[:16]
    if f.name not in state or state[f.name] != content_hash:
        new_files.append(f.name)

print('\n'.join(new_files))
")

if [ -z "$NEW_FILES" ]; then
    echo "==> All source files already have up-to-date summaries."
    exit 0
fi

FILE_COUNT=$(echo "$NEW_FILES" | wc -l | tr -d ' ')
echo "==> Generating summaries for $FILE_COUNT source files..."

# Process in batches of 20 to stay within context limits
BATCH_SIZE=20
BATCH_NUM=0
BATCH_LIST=""
BATCH_COUNT=0

while IFS= read -r file; do
    BATCH_LIST="${BATCH_LIST}${file}"$'\n'
    BATCH_COUNT=$((BATCH_COUNT + 1))

    if [ "$BATCH_COUNT" -ge "$BATCH_SIZE" ]; then
        BATCH_NUM=$((BATCH_NUM + 1))
        BATCH_LIST="${BATCH_LIST%$'\n'}"  # trim trailing newline
        echo "==> Processing batch $BATCH_NUM ($BATCH_COUNT files)..."

        claude -p --permission-mode auto --allowedTools "Read Write Glob Grep Bash" << PROMPT
You are generating summary documents for an AI research wiki.

For each of the following raw source files, create a summary document in summaries/ with the SAME filename.

Files to summarize:
$BATCH_LIST

For each file:
1. Read sources/<filename>
2. Extract the frontmatter metadata (especially source_url, title, author, tags)
3. Write summaries/<filename> with this exact format:

---
id: <from raw frontmatter>
title: <from raw frontmatter>
author: <from raw frontmatter>
source_url: <from raw frontmatter>
category: <from raw frontmatter>
tags: <from raw frontmatter>
saved_at: <from raw frontmatter>
summarized_at: "$(date -u +%Y-%m-%dT%H:%M:%SZ)"
---

# <Title>

**Original source:** [<Title>](<source_url>)
**Author:** <Author>

## Summary

<2-3 paragraph summary of the full document>

## Main Ideas

<Bulleted list of 3-7 key ideas, findings, or arguments>

## Key Quotes

<1-3 notable quotes from the source, if any. Omit this section entirely if there are no notable quotes.>

IMPORTANT:
- Do NOT copy the full raw content. Summarize it concisely but substantively (200-400 words for the summary section).
- Preserve the exact same filename from sources/ to summaries/.
- If the source_url is empty, omit the "Original source" link line.
- If the author is empty, omit the "Author" line.
PROMPT
        BATCH_LIST=""
        BATCH_COUNT=0
    fi
done <<< "$NEW_FILES"

# Process remaining files in the last partial batch
if [ "$BATCH_COUNT" -gt 0 ]; then
    BATCH_NUM=$((BATCH_NUM + 1))
    BATCH_LIST="${BATCH_LIST%$'\n'}"
    echo "==> Processing batch $BATCH_NUM ($BATCH_COUNT files)..."

    claude -p --permission-mode auto --allowedTools "Read Write Glob Grep Bash" << PROMPT
You are generating summary documents for an AI research wiki.

For each of the following raw source files, create a summary document in summaries/ with the SAME filename.

Files to summarize:
$BATCH_LIST

For each file:
1. Read sources/<filename>
2. Extract the frontmatter metadata (especially source_url, title, author, tags)
3. Write summaries/<filename> with this exact format:

---
id: <from raw frontmatter>
title: <from raw frontmatter>
author: <from raw frontmatter>
source_url: <from raw frontmatter>
category: <from raw frontmatter>
tags: <from raw frontmatter>
saved_at: <from raw frontmatter>
summarized_at: "$(date -u +%Y-%m-%dT%H:%M:%SZ)"
---

# <Title>

**Original source:** [<Title>](<source_url>)
**Author:** <Author>

## Summary

<2-3 paragraph summary of the full document>

## Main Ideas

<Bulleted list of 3-7 key ideas, findings, or arguments>

## Key Quotes

<1-3 notable quotes from the source, if any. Omit this section entirely if there are no notable quotes.>

IMPORTANT:
- Do NOT copy the full raw content. Summarize it concisely but substantively (200-400 words for the summary section).
- Preserve the exact same filename from sources/ to summaries/.
- If the source_url is empty, omit the "Original source" link line.
- If the author is empty, omit the "Author" line.
PROMPT
fi

# Update summary state with content hashes
python3 -c "
import json, hashlib
from pathlib import Path

sources_dir = Path('$SOURCES_DIR')
summaries_dir = Path('$SUMMARIES_DIR')
state_path = Path('$STATE_FILE')

state = json.loads(state_path.read_text()) if state_path.exists() else {}

for f in sources_dir.glob('*.md'):
    if (summaries_dir / f.name).exists():
        content_hash = hashlib.sha256(f.read_bytes()).hexdigest()[:16]
        state[f.name] = content_hash

state_path.write_text(json.dumps(state, indent=2, sort_keys=True) + '\n')
"

echo "==> Summary generation complete."
