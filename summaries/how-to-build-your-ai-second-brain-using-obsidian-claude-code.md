---
id: "01kjjrvyk7mk1ndg9s6xbtxnve"
title: "How to Build Your AI Second Brain Using Obsidian + Claude Code"
author: "Noah Vincent"
source_url: "https://x.com/noahvnct/status/2027435582461259997/?rw_tt_thread=True"
category: "tweet"
tags: [ai]
saved_at: "2026-02-28T18:41:11.271000+00:00"
summarized_at: "2026-04-15T19:46:34Z"
---

# How to Build Your AI Second Brain Using Obsidian + Claude Code

**Original source:** [How to Build Your AI Second Brain Using Obsidian + Claude Code](https://x.com/noahvnct/status/2027435582461259997/?rw_tt_thread=True)
**Author:** Noah Vincent

## Summary

Noah Vincent provides a detailed, step-by-step guide to building an "AI second brain" by combining Obsidian (a free, local-first markdown note-taking app) with Claude Code (Anthropic's terminal-based AI agent). The core argument is that the persistent context problem -- where every AI conversation starts from zero -- is the real bottleneck in AI productivity, not prompt quality. Built-in memory features in Claude and ChatGPT are structurally broken because they save arbitrary snippets without user control or organization. The solution is to put the AI inside your knowledge system rather than going to the AI externally.

The setup revolves around two critical files: `CLAUDE.md` (read automatically at every session startup) stores identity, projects, folder architecture, writing rules, and preferences -- functioning as "the brain of the brain." Over five sessions, Claude learns your voice, standards, and projects better than most human collaborators. `memory.md` serves as a session log where Claude records key decisions, patterns, and progress, providing continuity across conversations. Vincent describes a compounding effect: the more you use the system, the more context accumulates, and the smarter the AI becomes. He emphasizes meta-optimization -- asking Claude how to restructure its own context files for maximum efficiency.

For practical use cases, Vincent describes knowledge management across a 491-note Zettelkasten system (bulk tag updates, finding unlinked notes, synthesizing permanent notes from literature notes), content creation with full vault context (sub-agents scan related notes before writing), and "skills" -- repeatable slash commands created by asking Claude to write SOPs after productive sessions. He also covers MCP (Model Context Protocol) integration with external tools like Things3 (task management) and Tana (capture/voice notes), enabling workflows like `/voicenotetoletter` that converts a French voice note into a complete newsletter in one command. The entire setup costs approximately 20 euros per month, and Vincent argues it provides dramatically better value than API-based alternatives or proprietary tools like Notion.

## Main Ideas

- The real AI productivity bottleneck is not prompts but persistent context: every conversation starting from zero produces generic output regardless of prompt quality.
- `CLAUDE.md` (auto-read at startup) and `memory.md` (session log) create a compounding context system where Claude gets smarter with every session, learning your voice, projects, and preferences.
- Obsidian's local-first, plain-markdown architecture is ideal because Claude can read files directly with no API calls, no proprietary formats, and no vendor lock-in.
- The terminal is essential: the visual Claude.ai interface is structurally weaker because it does not give Claude full file system access -- the power lives in Claude Code.
- Skills (repeatable slash commands) are created by asking Claude to write SOPs after productive sessions, turning every workflow into a permanent, callable command.
- MCP (Model Context Protocol) extends Claude Code to external tools (Things3, Tana, etc.), enabling integrated workflows across tasks, capture, and content creation from a single interface.
- Meta-optimization -- asking Claude how to restructure its own context files and what information it still needs -- accelerates the compounding effect.

## Key Quotes

- "Context is everything when it comes to getting good AI output. Generic context produces generic results."
- "Use Claude Code once and it knows your folder structure. Use it five times and it knows your projects, your current focus, and your voice. Use it twenty times and it becomes your personalized operating system."
- "Every workflow becomes a permanent, callable command. The system grows in capability the more you use it."
