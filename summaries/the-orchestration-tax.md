---
id: "01kst4q6n4rd313svfszkptqae"
title: "The Orchestration Tax"
author: "Addy Osmani"
source_url: "https://x.com/addyosmani/status/2059844244907696186/?rw_tt_thread=True"
category: "tweet"
tags: [ai]
saved_at: "2026-05-29T15:12:52.388000+00:00"
summarized_at: "2026-06-09T00:00:04Z"
---

# The Orchestration Tax

**Original source:** [The Orchestration Tax](https://x.com/addyosmani/status/2059844244907696186/?rw_tt_thread=True)
**Author:** Addy Osmani

## Summary

The core insight is about the fundamental asymmetry in agentic workflows: starting agents is cheap (just a keystroke or prompt), but reviewing and integrating their output is expensive because only one person can do it serially. Osmani argues that the human becomes the single-threaded bottleneck in what should be a concurrent system—analogous to Python's Global Interpreter Lock (GIL). This creates structural limits governed by Amdahl's Law: speedup from parallelization is capped by the fraction of work that remains serial. Adding more agents doesn't increase productivity; it just deepens the queue of work awaiting human review, which remains the true constraint.

The "orchestration tax" manifests through multiple cognitive costs: context-switching between agent reviews (each cold reload takes minutes and is never perfect), tracking which agent needs attention next, and the temptation to perform shallow reviews or accept agent work without genuine judgment just to keep pace. The feeling of "maximal busyness" (busy dashboard, many running agents) can coexist with barely shipping good code. This is not a discipline problem but an architecture problem—grinding harder doesn't overcome structural limits; it just shifts the failure mode to cognitive debt, shallow code reviews, or acceptance of work you didn't actually understand.

The practical solution is to architect human attention as a scarce serial resource. Key strategies include: scaling agent count to match actual review capacity (typically low single digits), separating isolated, delegable work from complex judgment-heavy problems (and never trying to parallelize the latter), batching reviews to minimize context-switching costs, automating verification through tests and screenshots so humans only review the irreducible 20%, and protecting uninterrupted deep-thinking time. The critical skill is not running more agents but designing the system to respect human cognitive throughput.

## Main Ideas

- Human attention is the system bottleneck in agentic workflows; it acts like Python's GIL—all agents can run, but only one serial processor (human judgment) can execute, especially for architectural understanding and merge conflicts
- The orchestration tax is structural, not a discipline issue—governed by Amdahl's Law and cognitive limits that cannot be overcome by effort alone
- Context-switching between agent reviews is cognitively expensive; busy feeling decouples from shipped work quality, creating invisible failure modes (technical debt, stale mental models, poor code reviews)
- Scale agent parallelization to human review capacity, not UI limits; for most people this is low single digits, not 20
- Separate isolated/delegable work (safe to parallelize) from complex judgment-heavy work (never parallelize); the mistake is trying to scale the latter
- Practical tactics: batch reviews, use backpressure (let agents wait), have agents self-verify with tests/screenshots, protect uninterrupted thinking time for hard problems
- The core skill is architecting the system around the one non-parallelizable resource—human attention—not simply spawning more agents

## Key Quotes

- "Starting an agent is very cheap. It is just a keystroke or a sentence prompt. But closing the loop on the agent is not cheap at all. Someone has to check if what came back is correct and reconcile it with whatever the other agents touched. That someone is you. And there is exactly one of you."
- "You are the GIL of your AI agents. They all can run at once. But when any of their work needs genuine understanding of the architecture or resolving merge conflicts, that work has to acquire the lock. There is one lock. You hold it."
- "The real skill is designing the system around the one serial resource that cannot be cloned or parallelized. That resource is your attention. Architect it the way you architect anything else you depend on in production."
