---
id: "01kr9dcjx1hyjaeqspfckrphzm"
title: "Agent Harness Engineering"
author: "Addy Osmani"
source_url: "https://x.com/addyosmani/status/2053231239721885918/?s=12&t=lja9AMD11WXSlUvoMkbJMw&rw_tt_thread=True"
category: "tweet"
tags: [ai]
saved_at: "2026-05-10T17:01:34.495000+00:00"
summarized_at: "2026-05-12T00:22:20Z"
---

# Agent Harness Engineering

**Original source:** [Agent Harness Engineering](https://x.com/addyosmani/status/2053231239721885918/?s=12&t=lja9AMD11WXSlUvoMkbJMw&rw_tt_thread=True)

**Author:** Addy Osmani

## Summary

The essay argues that an AI agent consists of two equally important components: the model itself and the harness—the entire scaffolding of prompts, tools, infrastructure, hooks, and feedback loops built around it. While the industry has focused heavily on model selection and capability, harness engineering emphasizes that a decent model with excellent harness design consistently outperforms a great model with poor scaffolding. This represents a fundamental shift in how to evaluate agent performance, suggesting that the real competitive advantage lies not in selecting the smartest model but in engineering superior supporting infrastructure.

The core principle of harness engineering is treating agent failures as permanent signals rather than one-off flukes. Each mistake should trigger lasting improvements—updated documentation, new hooks, architectural changes—ensuring the agent never makes that exact mistake again. This creates a ratchet effect where the harness becomes progressively more refined over time. The harness encompasses multiple critical domains: durable state management (filesystem, git), general-purpose tooling (bash, code execution), isolated execution environments (sandboxes), knowledge injection (memory files), context management strategies, long-horizon execution patterns, and enforcement mechanisms (hooks).

The essay concludes that harness engineering represents the emerging discipline where real competitive advantage lies. As models improve, the harness doesn't become obsolete—it evolves to address new failure modes and enable previously unreachable tasks. The industry is already converging on similar harness patterns across different agent platforms, suggesting these principles are becoming fundamental conventions. Future developments involve more sophisticated multi-agent orchestration, agents analyzing their own traces for self-improvement, and harnesses functioning more like adaptive compilers than static configuration files.

## Main Ideas

- **Agent = Model + Harness**: The model is only one input into a running agent; the harness (prompts, tools, context policies, hooks, sandboxes) is equally critical and often determines whether an agent succeeds or fails.
- **The Ratchet Principle**: Treat each agent failure as a permanent signal that generates lasting improvements to the harness so the same mistake never recurs.
- **A Decent Harness Beats a Great Model**: An excellent harness with a mediocre model consistently outperforms a cutting-edge model with poor scaffolding.
- **Key Harness Components**: Effective harnesses combine filesystem/git state, general-purpose tools (bash), safe sandboxes, memory for knowledge injection, context management strategies, long-horizon execution patterns, and hooks for enforcement.
- **Behavior-Driven Design**: Each component should directly serve a specific desired behavior; if you can't name the behavior a component delivers, remove it.
- **Context Rot Management**: Harnesses battle degrading model reasoning through compaction, tool-call offloading, and progressive disclosure of instructions and tools.
- **Harnesses Evolve, Not Shrink**: As models improve, harnesses don't become obsolete—they shift to address new failure modes and enable previously unreachable capabilities.

## Key Quotes

- "A decent model with a great harness consistently beats a great model with a bad harness."
- "If the agent ignored a convention, add it to [AGENTS.md](http://AGENTS.md). If it ran a destructive command, write a hook to block it. If it got lost in a 40-step task, split the architecture into a planner and an executor."
- "The gap between what today's models can theoretically do and what you actually see them doing is largely a harness gap."
