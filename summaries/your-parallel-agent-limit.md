---
id: "01kp6zyeabd3zw2paw0hm4e0cb"
title: "Your parallel Agent limit"
author: "Addy Osmani"
source_url: "https://addyosmani.com/blog/cognitive-parallel-agents/"
category: "article"
tags: [ai, work]
saved_at: "2026-04-14T21:56:47.050000+00:00"
summarized_at: "2026-04-15T20:22:19Z"
---

# Your parallel Agent limit

**Original source:** [Your parallel Agent limit](https://addyosmani.com/blog/cognitive-parallel-agents/)
**Author:** Addy Osmani

## Summary

Addy Osmani examines the personal cognitive cost of running multiple AI coding agents in parallel — a dimension largely absent from the throughput-focused discourse around agentic engineering. Building on Simon Willison's observation that running four parallel agents can leave you exhausted by 11am, Osmani identifies three sources of hidden cognitive load: context switching (reloading mental models between threads, with recovery time that never fully completes), continuous judgment calls (architectural decisions and trust assessments that can't be batched or deferred), and trust calibration overhead (maintaining separate, dynamic assessments of each agent's reliability that degrade when unmonitored).

The central insight is that agent parallelism doesn't scale linearly for the human. Agents parallelize code generation, but evaluation, judgment, trust, and integration remain single-threaded on the human side. Supervision scales; understanding does not. The gap between the two is where comprehension debt accumulates. Osmani introduces the concept of "ambient anxiety tax" — the background vigilance of not knowing what's happening in threads you haven't checked, which draws from the same cognitive reservoir as active work.

Rather than maximizing agent count, Osmani advocates finding your personal ceiling through intentional calibration. His concrete practices include time-boxing sessions with scope sized to fit, accepting that three well-reviewed threads outperform six half-supervised ones, and reducing scope per thread before reducing thread count. He offers calibration heuristics: start one thread below what feels right, watch review quality rather than agent count, notice the anxiety signal when you've lost track of multiple threads, and try tighter task scoping before reducing parallelism.

## Main Ideas

- Running parallel agents imposes a new kind of cognitive labor — context switching, continuous judgment calls, and trust calibration — that the throughput narrative largely ignores.
- "Ambient anxiety tax" describes the background vigilance of not knowing what unmonitored agent threads might be getting wrong, drawing from the same cognitive reservoir as active work.
- Agent parallelism doesn't scale linearly for humans: supervision scales but understanding doesn't, and the gap is where comprehension debt compounds.
- Your personal ceiling isn't a fixed number — it shifts with task complexity, brief quality, session duration, and your own energy level on a given day.
- Three focused, well-reviewed threads produce more mergeable output than six half-supervised ones; the author's typical ceiling is 3-4 threads.
- Time-boxing sessions with scope sized to fit converts indefinite vigilance into bounded vigilance, reducing cumulative cognitive drain.
- Calibration heuristics: start one thread below what feels right, watch review quality (not agent count), notice multi-thread anxiety as a capacity signal, and try scope reduction before count reduction.

## Key Quotes

- "More agents running doesn't mean more of you available."
- "What scales is your throughput of supervision, not your throughput of understanding. You can supervise more agents than you can deeply understand."
- "The engineers who get the most from parallel agents in the long run won't be the ones running the most simultaneously — they'll be the ones who know the difference between throughput and understanding."
