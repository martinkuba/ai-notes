---
id: "01kst4q6n4rd313svfszkptqae"
title: "The Orchestration Tax"
author: "Addy Osmani"
source_url: "https://x.com/addyosmani/status/2059844244907696186/?rw_tt_thread=True"
category: "tweet"
tags: [ai]
saved_at: "2026-05-29T15:12:52.388000+00:00"
summarized_at: 2026-06-12T00:00:04Z
---

# The Orchestration Tax

**Original source:** [The Orchestration Tax](https://x.com/addyosmani/status/2059844244907696186/?rw_tt_thread=True)

**Author:** Addy Osmani

## Summary

Osmani argues that while spawning multiple AI agents is easy, managing them creates a hidden "orchestration tax"—the cognitive burden of reviewing, merging, and orchestrating their outputs. The core insight is an asymmetry: starting an agent is cheap (a keystroke), but closing the loop is expensive and cannot be parallelized—it bottlenecks on the human's serial cognitive capacity. Just as Amdahl's Law limits parallelization gains in concurrent systems, the human becomes the serial bottleneck in agentic workflows. You are, metaphorically, the Global Interpreter Lock (GIL) of your AI agents.

The tiredness developers feel isn't a discipline problem—it's architectural. Running a serial processor (your attention) at 100% capacity creates constant context-switching costs, cognitive fatigue, and the risk of cognitive surrender (accepting agent outputs without genuine review). The throughput of an agentic system equals exactly the throughput of the human review step, not the number of agents spawned. Optimizing agent production without addressing review bottlenecks only grows the pile of unfinished work.

Osmani proposes treating attention as a scarce resource worthy of architectural respect: scale agent count to your actual review rate (typically single digits), sort work by complexity to avoid parallelizing deep judgment tasks, batch reviews to minimize context-switching, and protect your best hours for serial work that requires genuine understanding. Feeling busy is not the same as being productive—invisible accumulation of technical and cognitive debt may accompany the appearance of high throughput.

## Main Ideas

- **Asymmetry in agentic workflows**: Starting agents is cheap; closing the loop (review, merge, reconciliation) is expensive and serial
- **The human is the GIL**: You are the serialization bottleneck; all meaningful agent work eventually requires your judgment
- **Amdahl's Law applies**: Speedup from parallelizing agents is capped by the serial fraction (your judgment throughput); spawning more agents doesn't speed up your review
- **Orchestration tax is structural, not a discipline problem**: Context-switching between agent reviews costs minutes per switch; grinding harder won't overcome architectural limits
- **Backpressure and queuing**: Scale agent fleet to review rate, not to UI capability; let work pile up and batch-process reviews
- **Distinguish isolated vs. judgment-intensive work**: Background agents can handle async isolated tasks; complex architectural/debugging work should not be parallelized
- **Busy ≠ productive**: High agent activity and cognitive debt accumulation can coexist; focus on throughput of merged code, not agent activity

## Key Quotes

- "Starting an agent is very cheap. It is just a keystroke or a sentence prompt. But closing the loop on the agent is not cheap at all."
- "You are the GIL of your AI agents. They all can run at once. But when any of their work needs genuine understanding of the architecture or resolving merge conflicts, that work has to acquire the lock."
- "The real skill is designing the system around the one serial resource that cannot be cloned or parallelized. That resource is your attention."
