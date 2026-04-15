---
id: "01kfbpnyajdqj8hc2cmfrr4dtm"
title: "Claude Code creator Boris shares his setup with 13 detailed steps,full details below"
author: "BuildwithVignesh"
source_url: "https://www.reddit.com/r/ClaudeAI/comments/1q2c0ne/claude_code_creator_boris_shares_his_setup_with/"
category: "article"
tags: [ai]
saved_at: "2026-01-19T18:01:10.737000+00:00"
summarized_at: "2026-04-15T19:39:03Z"
---

# Claude Code creator Boris shares his setup with 13 detailed steps

**Original source:** [Claude Code creator Boris shares his setup with 13 detailed steps,full details below](https://www.reddit.com/r/ClaudeAI/comments/1q2c0ne/claude_code_creator_boris_shares_his_setup_with/)
**Author:** BuildwithVignesh

## Summary

Boris Cherny, creator of Claude Code, shared his personal workflow on X, which was compiled into a Reddit thread with extensive community discussion. His setup is "surprisingly vanilla"—he emphasizes that Claude Code works great out of the box. He runs 5 Claude instances in parallel locally and 5-10 more on claude.ai/code, each in separate git checkouts to avoid conflicts. He uses Opus 4.5 with thinking for everything, finding that despite being bigger and slower than Sonnet, it requires less steering and ultimately works faster.

Key practices include: sharing a single CLAUDE.md per repo (just 2.5k tokens) that the whole team contributes to; starting most sessions in Plan Mode until the plan looks good, then switching to auto-accept; using slash commands for frequently repeated workflows; employing subagents for code simplification and verification; using PostToolUse hooks for formatting; and pre-allowing safe bash commands instead of skipping permissions entirely. He uses MCP for Slack, BigQuery, Sentry, and other tools. For long-running tasks, he uses verification loops, Stop hooks, or the "ralph-wiggum" plugin.

The community reaction was mixed—many were impressed by the simplicity but noted the setup depends on unlimited API tokens unavailable to regular users. Boris completes 50-100 PRs per week and abandons about 10-20% of sessions. The thread contains 30+ Q&A responses from Boris covering topics like managing parallel features, compaction strategies, verification loops, and more. A recurring community theme is that simpler setups often outperform over-engineered ones with dozens of specialized subagents.

## Main Ideas

- Boris runs 10-15 Claude instances in parallel (5 local + 5-10 web), each in separate git checkouts
- His CLAUDE.md is only 2.5k tokens—the team contributes corrections as they encounter mistakes
- Plan Mode is the starting point for most sessions; he iterates on the plan before switching to auto-accept
- The most important tip: give Claude a way to verify its work (tests, browser, simulator) for 2-3x quality improvement
- Slash commands automate repeated workflows like commit-push-PR, used dozens of times daily
- Boris completes 50-100 PRs per week, abandoning 10-20% of sessions
- Community consensus: simpler, vanilla setups often beat over-engineered configurations with many subagents
