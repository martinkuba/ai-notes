---
id: "01kj0ngj703bf27p9875an8pyf"
title: "I'm Boris and I created Claude Code"
author: "Boris Cherny"
source_url: "https://x.com/bcherny/status/2017742741636321619/?rw_tt_thread=True"
category: "tweet"
tags: [ai]
saved_at: "2026-02-21T17:56:12.640000+00:00"
summarized_at: "2026-04-15T19:46:34Z"
---

# I'm Boris and I created Claude Code

**Original source:** [I'm Boris and I created Claude Code](https://x.com/bcherny/status/2017742741636321619/?rw_tt_thread=True)
**Author:** Boris Cherny

## Summary

Boris Cherny, creator of Claude Code, shares ten practical tips for using Claude Code effectively, sourced directly from the Claude Code team at Anthropic. He emphasizes that there is no single right way to use the tool and encourages experimentation. The tips range from workflow strategies to specific technical setups.

The single biggest productivity unlock, according to the team, is working in parallel by spinning up 3-5 git worktrees, each running its own Claude session simultaneously. Other key workflow tips include starting every complex task in plan mode (with one team member even using a second Claude instance to review the plan as a "staff engineer"), investing heavily in CLAUDE.md files by having Claude write its own rules after every correction, and creating reusable custom skills committed to git. For debugging, the team recommends enabling the Slack MCP to paste bug threads directly into Claude, or simply telling Claude to "go fix the failing CI tests" without micromanaging.

Prompting strategies include challenging Claude by asking it to "grill me on these changes" before making a PR, and after a mediocre fix, asking it to "scrap this and implement the elegant solution." The team recommends terminal setups using Ghostty with customized status bars, voice dictation for faster prompting, and subagents to offload individual tasks while keeping the main context window clean. Claude Code is also used extensively for data and analytics work via BigQuery CLI, with one team member not having written SQL manually in over six months.

## Main Ideas

- Parallel worktrees (3-5 simultaneous Claude sessions) are the team's top productivity recommendation.
- Start every complex task in plan mode; invest energy in the plan so Claude can one-shot the implementation.
- Continuously invest in CLAUDE.md by having Claude update its own rules after every correction.
- Create reusable custom skills and slash commands for repetitive tasks.
- Use subagents to offload tasks and keep the main context window focused.
- Claude can fix most bugs autonomously when given sufficient context (Slack threads, CI logs, Docker logs).
- Use Claude Code for data and analytics work through CLI tools like BigQuery, eliminating the need to write SQL manually.

## Key Quotes

- "There is no one right way to use Claude Code -- everyone's setup is different. You should experiment to see what works for you!"
- "After every correction, end with: 'Update your CLAUDE.md so you don't make that mistake again.' Claude is eerily good at writing rules for itself."
