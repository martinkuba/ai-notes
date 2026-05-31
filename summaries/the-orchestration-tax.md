---
id: "01kst4q6n4rd313svfszkptqae"
title: "The Orchestration Tax"
author: "Addy Osmani"
source_url: "https://x.com/addyosmani/status/2059844244907696186/?rw_tt_thread=True"
category: "tweet"
tags: [ai]
saved_at: "2026-05-29T15:12:52.388000+00:00"
summarized_at: "2026-05-31T23:38:43Z"
---

# The Orchestration Tax

**Original source:** [The Orchestration Tax](https://x.com/addyosmani/status/2059844244907696186/?rw_tt_thread=True)
**Author:** Addy Osmani

## Summary

The "orchestration tax" describes the hidden cost of scaling AI agent usage: while spawning agents is trivially easy, the work of reviewing, verifying, and merging their output remains fundamentally serial and bottlenecked by human judgment. Osmani argues this creates a structural asymmetry—there exists exactly one person to close every loop an agent opens. As you add more agents, you don't multiply your output; you create a growing queue of work waiting for human review, generating cognitive overhead through context switching and decision fatigue.

This is not a willpower or discipline problem but an architecture problem, best understood through the lens of concurrent systems. Just as Python's Global Interpreter Lock makes the human the serialization point, Amdahl's Law makes it clear that the speedup from parallelizing agent work is capped by the serial fraction—the judgment required. Osmani illustrates the distinction between "feeling productive" (dashboard full, many agents running) and "being productive" (shipping good code). The former masks the latter: you can run 20 agents and feel busy while barely moving the needle, accumulating both technical and cognitive debt as you merge work you didn't fully review.

The solution is treating attention as a scarce architectural resource: scale your agent fleet to your review rate (typically low single digits), sort work by whether it requires human judgment, batch reviews to minimize context switching, restrict human involvement to decisions machines cannot verify, and protect your best cognitive hours for the serial work that genuinely matters. This reframes orchestration not as management but as system design.

## Main Ideas

- Starting agents is cheap; closing the loop (reviewing and merging) is expensive and strictly serial, creating an asymmetry that doesn't scale
- Human attention is the bottleneck—the single-threaded resource that controls all agent output, analogous to Python's GIL
- Amdahl's Law applies directly: speedup is capped by the serial fraction (judgment), meaning more agents don't increase throughput, only the queue depth
- Context switching carries severe cognitive costs; jumping between agents requires expensive context reloads that compound with scale
- Scale agent count to review capacity, not UI capability; sort work by whether judgment is central or peripheral; batch reviews to reduce switching costs
- Reserve human judgment only for decisions machines cannot verify; let agents write tests and generate proofs for the routine 80%
- Feeling busy is decoupled from productivity; running 20 agents can feel productive while delivering little shipped code and accumulating hidden cognitive debt

## Key Quotes

> "Running multiple agents does not mean there is more of you. Your cognitive bandwidth doesn't parallelize."

> "You are the GIL of your AI agents. They all can run at once. But when any of their work needs genuine understanding of the architecture or resolving merge conflicts, that work has to acquire the lock. There is one lock. You hold it."

> "The real skill is designing the system around the one serial resource that cannot be cloned or parallelized. That resource is your attention. Architect it the way you architect anything else you depend on in production."
