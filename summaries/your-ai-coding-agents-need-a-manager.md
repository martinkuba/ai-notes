---
id: "01kp700b2bx1w05nknmychw3g2"
title: "Your AI coding agents need a manager"
author: "Addy Osmani"
source_url: "https://addyosmani.com/blog/coding-agents-manager/"
category: "article"
tags: [ai, work]
saved_at: "2026-04-14T21:57:49.259000+00:00"
summarized_at: "2026-04-15T20:22:19Z"
---

# Your AI coding agents need a manager

**Original source:** [Your AI coding agents need a manager](https://addyosmani.com/blog/coding-agents-manager/)
**Author:** Addy Osmani

## Summary

Addy Osmani argues that as developers move from pairing with a single AI agent to orchestrating multiple parallel agents, the bottleneck shifts from "can the agent write code?" to management skills: clarity, delegation, verification loops, and async communication. He envisions the highest-leverage developers operating as async-first managers running small fleets of parallel agents, splitting work into high-touch local sessions (for architecture, tricky refactors, and product nuance) and async background sessions (for bounded tasks like migrations, test generation, and docs updates).

Four management skills transfer directly to agent orchestration. First, clear task scoping — writing agent briefs with outcomes, constraints, non-goals, acceptance criteria, and verification plans rather than vague prompts. Second, delegation judgment — knowing what to fully hand off (mechanical implementations), what to delegate with checkpoints (shared interfaces, data migrations), and what to keep (architecture, security, product decisions). Third, verification loops — requiring agents to run tests, pass linting, and produce structured PR packets, or using a two-agent writer/reviewer pattern. Fourth, async check-ins — treating agents like remote reports with predictable status formats and defined escalation criteria.

The hard parts are genuine management problems too: merge conflicts multiply when parallel agents touch adjacent code (solved with git worktrees and intentional task boundaries), and cheap building creates feature bloat unless you apply WIP limits and kill criteria. Osmani's personal workflow runs 4-5 background agents on bounded work while staying human-in-the-loop across 3-5 local sessions, emphasizing that the sweet spot depends on honest self-assessment of context-switching capacity.

## Main Ideas

- Running multiple AI coding agents in parallel is fundamentally a management problem, not a prompting problem — the skills of tech leads and engineering managers transfer directly.
- Work splits naturally into high-touch local sessions (architecture, product nuance) and async background sessions (bounded tasks like migrations and test generation).
- Four key management skills apply: clear task scoping with briefs, delegation judgment (hand off vs. checkpoint vs. own), verification loops (tests, lint, two-agent review), and async check-ins with structured status updates.
- Merge conflicts are a boundary failure, not a tooling failure — solve with git worktrees, one-agent-one-PR rules, and human-led interface PRs before agent work.
- When building becomes cheap, judgment and prioritization ("should we build this?") become the real bottleneck — apply WIP limits and kill criteria.
- A practical operating loop: plan like a manager, spawn with explicit boundaries, monitor async, verify aggressively, integrate carefully, and retro to improve the process.

## Key Quotes

- "AI coding at scale stops being a prompting problem and becomes a management problem."
- "The bottleneck is no longer 'can the agent write code?' It's 'should we build this?' and 'can I manage multiple agents doing so effectively?'"
- "Throughput looks better with six. Code I'm willing to actually merge without a second pass looks better with three."
