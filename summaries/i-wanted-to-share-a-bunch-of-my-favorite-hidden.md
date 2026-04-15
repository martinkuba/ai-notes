---
id: "01kn06r9a56mnp97ser454kgc5"
title: "I wanted to share a bunch of my favorite hidden..."
author: "Boris Cherny"
source_url: "https://x.com/bcherny/status/2038454336355999749/?rw_tt_thread=True"
category: "tweet"
tags: [ai]
saved_at: "2026-03-30T20:25:22.501000+00:00"
summarized_at: "2026-04-15T19:50:48Z"
---

# I wanted to share a bunch of my favorite hidden...

**Original source:** [I wanted to share a bunch of my favorite hidden...](https://x.com/bcherny/status/2038454336355999749/?rw_tt_thread=True)
**Author:** Boris Cherny

## Summary

Boris Cherny, the creator of Claude Code, shares a thread of 15 hidden and under-utilized features of Claude Code. The tips span across mobile usage, session management, automation, hooks, multi-repo workflows, and more. He reveals that Claude Code has a mobile app (accessible via the Claude iOS/Android app's Code tab) that allows coding without a laptop, and that sessions can be moved back and forth between mobile, web, desktop, and terminal using `--teleport` and `/remote-control` commands.

Among the most powerful features highlighted are `/loop` and `/schedule`, which allow Claude to run automatically at set intervals for up to a week, and hooks that deterministically inject logic into the agent lifecycle (e.g., dynamically loading context at session start, logging bash commands, or routing permission prompts to WhatsApp). He also covers Cowork Dispatch for remotely controlling the Claude Desktop app, the Chrome extension for frontend verification, and the Desktop app's ability to automatically start and test web servers in a built-in browser.

Additional tips include session forking (`/branch` or `--fork-session`), the `/btw` command for side queries while the agent works, git worktrees for parallel development (`claude -w`), `/batch` for fanning out massive changesets across dozens or hundreds of worktree agents, `--bare` for 10x faster SDK startup, `--add-dir` for multi-repo access, `--agent` for custom system prompts and tools, and `/voice` for voice-driven coding. Cherny notes that he personally does most of his coding by speaking to Claude rather than typing.

## Main Ideas

- Claude Code has a mobile app for coding on the go, with session teleportation between mobile, web, desktop, and terminal.
- `/loop` and `/schedule` enable automated recurring Claude tasks for up to a week at a time.
- Hooks provide deterministic agent lifecycle control (session start, pre-tool-use, etc.) for context loading, logging, and permission routing.
- `/batch` fans out work to dozens, hundreds, or even thousands of parallel worktree agents for large-scale code migrations.
- `--bare` speeds up SDK startup by up to 10x for non-interactive usage by skipping automatic context discovery.
- `--add-dir` and `--agent` enable multi-repo access and custom agent configurations respectively.
- `/voice` enables voice-driven coding, which Cherny uses as his primary input method.
