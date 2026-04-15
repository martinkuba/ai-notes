---
id: "01kndwjgxc9bq7zav08s0fyr2h"
title: "How to Build Your Second Brain"
author: "Nick Spisak"
source_url: "https://x.com/nickspisak_/status/2040448463540830705/?s=10&rw_tt_thread=True"
category: "tweet"
tags: [ai]
saved_at: "2026-04-05T03:56:49.964000+00:00"
summarized_at: "2026-04-15T19:46:34Z"
---

# How to Build Your Second Brain

**Original source:** [How to Build Your Second Brain](https://x.com/nickspisak_/status/2040448463540830705/?s=10&rw_tt_thread=True)
**Author:** Nick Spisak

## Summary

Nick Spisak provides a concise, practitioner-oriented guide to building a personal AI-maintained knowledge base, inspired by Andrej Karpathy's approach of using plain folders and text files rather than specialized software. The system requires just three folders (`raw/` for unprocessed source material, `wiki/` for AI-organized content, and `outputs/` for generated reports and answers) plus a schema file (`CLAUDE.md` or equivalent) that tells the AI the rules for organizing the knowledge base. Spisak emphasizes that the simplicity is the point -- no apps to install, no accounts to create, no databases.

The guide walks through eight steps: creating the folder structure, filling the raw folder with everything you have (articles, notes, screenshots, meeting docs) without organizing it, optionally automating source collection using Vercel's agent-browser CLI tool (which uses 82% fewer tokens than Playwright MCP for web scraping), writing a schema file with wiki rules and topic focus areas, telling the AI to compile raw sources into an organized wiki with an index and cross-linked topic files, asking questions against the wiki and saving answers back into the knowledge base, running monthly health checks to catch contradictions and compounding errors, and choosing tools pragmatically. Spisak explicitly pushes back against over-tooling, noting that Karpathy himself uses "just a nested directory of .md files" and that "Obsidian with 47 plugins is the Notion trap all over again." The key insight is that the AI maintains the wiki entirely -- you do not edit it by hand -- and every question you ask makes the next answer better through a compounding loop. However, Spisak also warns (citing community feedback) that errors compound too when outputs get filed back, making periodic health checks essential.

## Main Ideas

- A personal AI knowledge base needs only three folders (`raw/`, `wiki/`, `outputs/`) and one schema file -- no special software or databases required.
- The schema file (`CLAUDE.md`) is the critical piece: it tells the AI the rules for organizing, linking, and maintaining the wiki, serving as the system's instruction manual.
- The raw folder should be filled with everything without organization; organizing is the AI's job, not yours.
- Agent-browser (Vercel Labs) automates web scraping into the raw folder, handling JavaScript-heavy sites and dynamic content with 82% fewer tokens than Playwright MCP.
- The compounding loop -- ask questions, save answers back, AI updates wiki -- makes the system smarter over time, but errors also compound, requiring periodic health checks.
- Over-tooling is a trap: flat files and a good schema outperform complex tool stacks 90% of the time; the tool does not matter as long as you have the folder structure and schema.
- Monthly health checks (flagging contradictions, unsupported claims, missing topics) are essential to prevent error accumulation in the AI-maintained wiki.
