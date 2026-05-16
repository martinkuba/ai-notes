---
id: "01krcabadzehspmr07ds647phs"
title: "Karpathy's 4 CLAUDE.md rules cut Claude mistakes from 41% to 11%. After 30 codebases, I added 8 more"
author: "Mnimiy"
source_url: "https://x.com/mnilax/status/2053116311132155938/?s=12&t=lja9AMD11WXSlUvoMkbJMw&rw_tt_thread=True"
category: "tweet"
tags: [ai]
saved_at: "2026-05-11T20:06:10.623000+00:00"
summarized_at: 2026-05-12T00:22:20Z
---

# Karpathy's 4 CLAUDE.md rules cut Claude mistakes from 41% to 11%. After 30 codebases, I added 8 more

**Original source:** [Karpathy's 4 CLAUDE.md rules cut Claude mistakes from 41% to 11%. After 30 codebases, I added 8 more](https://x.com/mnilax/status/2053116311132155938/?s=12&t=lja9AMD11WXSlUvoMkbJMw&rw_tt_thread=True)
**Author:** Mnimiy

## Summary

Andrej Karpathy's January 2026 complaint about Claude's coding behavior was crystallized by Forrest Chang into 4 CLAUDE.md rules that became the fastest-growing single-file repo of 2026. After testing these rules across 30 codebases over 6 weeks, Mnimiy found they successfully reduced coding mistakes from ~41% to under 3% on aligned tasks, but identified gaps specific to May 2026's multi-step agent workflows. The original 4 rules addressed silent assumptions, over-engineering, orthogonal damage, and weak success criteria, but missed failure modes in long-running operations, multi-codebase consistency, test quality, and agent orchestration. Mnimiy added 8 complementary rules targeting these gaps: using the model only for judgment calls (not routing/retries), hard token budgets, surfacing conflicts instead of averaging patterns, reading before writing, verifying test intent over behavior, checkpointing multi-step workflows, matching codebase conventions, and failing visibly. Testing showed the combined 12-rule framework reduced error rates to 3% while maintaining 76% compliance (down only slightly from 78% with 4 rules), demonstrating that additional rules address non-overlapping failure modes rather than competing for attention.

## Main Ideas

- **Karpathy's 4-rule foundation** addresses specific January 2026 coding problems but remains incomplete for May 2026's multi-step agent workflows and orchestration patterns
- **Rule 5–12 target new failure modes**: agent token budgets, multi-step checkpoints, pattern conflicts, test meaningfulness, silent failures, and codebase convention drift
- **Token budgets and checkpoints** are critical for multi-step tasks; Rule 6 and Rule 10 prevent both context bloat and undetected errors mid-workflow
- **Test quality distinction**: tests must encode *why* behavior matters (business logic verification), not just confirm function execution
- **Compliance mechanics**: CLAUDE.md files over 200 lines show sharp compliance drops; 12 carefully-chosen rules outperform larger rulesets
- **Conflict resolution principle**: when codebase patterns contradict, picking one consciously is better than averaging or silently forking patterns
- **Visible failure beats silent success**: surfacing uncertainty about task completion (migrations, tests, features) prevents weeks of undetected production issues

## Key Quotes

> "Claude Code's CLAUDE.md is the most under-leveraged file in the entire AI coding stack. Most developers either treat it as a dump for every preference they've ever had, bloated to 4,000+ tokens, compliance drops to 30%"

> "The most expensive Claude failures are the ones that look like success. A function 'works' but returns wrong data. A migration 'completes' but skipped 30 records."

> "A 6-rule CLAUDE.md tuned to your real failure modes beats a 12-rule one with 6 rules you'll never need."
