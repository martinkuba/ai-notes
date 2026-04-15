---
id: "01kp705mbh5k6mjcxpjqdf0d0h"
title: "Best Practices for Claude Code"
author: "Claude Code Docs"
source_url: "https://code.claude.com/docs/en/best-practices"
category: "article"
tags: [ai, work]
saved_at: "2026-04-14T22:00:42.609000+00:00"
summarized_at: "2026-04-15T20:22:19Z"
---

# Best Practices for Claude Code

**Original source:** [Best Practices for Claude Code](https://code.claude.com/docs/en/best-practices)
**Author:** Claude Code Docs

## Summary

This official guide from Anthropic covers effective patterns for working with Claude Code, an agentic coding environment that autonomously reads files, runs commands, and implements changes. The central constraint is context window management — Claude's performance degrades as context fills with conversation, file reads, and command output, making this the most important resource to manage.

The highest-leverage practice is providing self-verification criteria: tests, screenshots, or expected outputs that let Claude check its own work rather than relying on the human as the sole feedback loop. The guide recommends using Plan Mode to separate exploration from execution on complex tasks, writing precise instructions that reference specific files and patterns, and setting up persistent project context via CLAUDE.md files (kept concise and prunable). Additional setup includes configuring permission modes (auto mode, allowlists, sandboxing) to reduce approval interruptions, leveraging CLI tools like `gh` for context-efficient external service interaction, using MCP servers for integrations, hooks for deterministic automation, and skills/subagents for domain-specific workflows.

For scaling beyond a single session, the guide covers non-interactive mode (`claude -p`) for CI and scripts, parallel sessions using the desktop app or agent teams, the writer/reviewer pattern across separate sessions, and fan-out patterns for batch operations. Common anti-patterns include "kitchen sink" sessions mixing unrelated tasks, over-correcting without clearing context, bloated CLAUDE.md files, skipping verification, and unbounded exploration that fills context. The guide emphasizes that these are starting points — developers should observe what works and develop personal intuition.

## Main Ideas

- Context window management is the fundamental constraint: performance degrades as context fills, so use `/clear` between tasks, subagents for exploration, and `/compact` for targeted summarization.
- Self-verification (tests, screenshots, expected outputs) is the single highest-leverage practice — it lets Claude check its own work instead of relying on human review for every iteration.
- CLAUDE.md files provide persistent project context but must be kept concise; bloated files cause Claude to ignore instructions.
- Precise prompts with specific files, constraints, and example patterns dramatically reduce course corrections compared to vague instructions.
- Subagents are a key tool for managing context — they explore codebases in separate context windows and report back summaries without cluttering the main conversation.
- Parallel sessions, the writer/reviewer pattern, and fan-out batch operations enable horizontal scaling of Claude Code beyond a single conversation.
- Common anti-patterns: mixing unrelated tasks in one session, repeated corrections without clearing context, and unbounded exploration that fills the context window.
