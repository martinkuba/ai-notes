---
id: "01kst4q6n4rd313svfszkptqae"
title: "The Orchestration Tax"
author: "Addy Osmani"
source_url: "https://x.com/addyosmani/status/2059844244907696186/?rw_tt_thread=True"
category: "tweet"
tags: [ai]
saved_at: "2026-05-29T15:12:52.388000+00:00"
summarized_at: "2026-06-11T00:00:04Z"
---

# The Orchestration Tax

**Original source:** [The Orchestration Tax](https://x.com/addyosmani/status/2059844244907696186/?rw_tt_thread=True)
**Author:** Addy Osmani

## Summary

The orchestration tax is the hidden cognitive and management overhead of running multiple AI agents in parallel. While spawning agents is cheap—just a keystroke—closing the loop on them is expensive: someone must verify correctness, reconcile conflicts, and merge changes. That someone is the human user, and there is exactly one of them. This creates a fundamental asymmetry: the user becomes the single-threaded bottleneck in an otherwise parallel system, similar to Python's Global Interpreter Lock. Amdahl's Law makes this precise—the speedup from parallelization is capped by the fraction of work that remains serial. In agent workflows, that serial fraction is human judgment, making the throughput of the entire system equal to the throughput of the review step alone.

The failure mode is insidious because feeling busy is decoupled from actual productivity. Running twenty agents creates the illusion of massive output while potentially shipping shallow code reviews, stale mental models of the codebase, and accumulated technical and cognitive debt. Grinding harder cannot overcome structural limits; attempting to do so results in either cognitive surrender (accepting agent output without genuine review) or burnout from constant context-switching and reload costs.

The solution is to architect attention as the scarce serial resource it is: scale agent fleet to review capacity (usually low single digits), sort work into parallelizable vs. judgment-intensive tasks, batch reviews to reduce context-switching costs, only spend judgment on what machines cannot verify, and protect serial time for deep thinking. The real skill is not spawning agents—anyone can do that. The real skill is designing systems that respect the one non-parallelizable resource: human attention.

## Main Ideas

- **The production-review asymmetry**: Starting agents is cheap, but reviewing them is expensive and creates a bottleneck at the human
- **The human as bottleneck**: The user is the single-threaded component in a concurrent system, analogous to Python's GIL
- **Structural limits apply**: Amdahl's Law shows that system throughput is limited by the serial review step, not agent parallelism
- **Busy ≠ productive**: Multiple agents create the illusion of productivity while potentially degrading code quality and understanding
- **Cognitive debt compounds**: Skipping proper reviews accumulates technical debt, stale mental models, and cognitive debt simultaneously
- **Attention architecture matters**: Effective orchestration requires treating attention as a scarce resource through backpressure, sorting, batching, and protecting serial time
- **Judgment is the work**: The highest leverage is focusing human attention only on decisions machines cannot verify

## Key Quotes

- "Running multiple agents does not mean there is more of you."
- "You are the GIL of your AI agents. They all can run at once. But when any of their work needs genuine understanding of the architecture or resolving merge conflicts, that work has to acquire the lock."
- "The orchestration tax is the structural gap between agent production and what you can actually merge. It's what happens when you put a single-threaded resource in charge of a concurrent one."
- "The real skill is designing the system around the one serial resource that cannot be cloned or parallelized. That resource is your attention."
- "You can be maximally busy and barely produce anything. From the inside it feels identical."
