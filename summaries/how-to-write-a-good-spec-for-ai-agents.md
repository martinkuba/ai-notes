---
id: "01kjnjf1z6d29fpay4j9dhdthe"
title: "How to write a good spec for AI agents"
author: "Addy Osmani"
source_url: "https://addyosmani.com/blog/good-spec/#:~:text=January%2013%2C%202026,and%20the%20model%20breaks%20down.%E2%80%9D"
category: "article"
tags: [ai, work]
saved_at: "2026-03-01T20:47:00.583000+00:00"
summarized_at: "2026-04-15T19:46:34Z"
---

# How to write a good spec for AI agents

**Original source:** [How to write a good spec for AI agents](https://addyosmani.com/blog/good-spec/#:~:text=January%2013%2C%202026,and%20the%20model%20breaks%20down.%E2%80%9D)
**Author:** Addy Osmani

## Summary

This is the original blog post version of Osmani's guide to writing effective specifications for AI coding agents, published on his personal site (the O'Reilly Radar version is a republication). The content covers the same five principles for spec-writing, presented with slightly different formatting and images. The core argument is that developers must write "smart specs" that balance clarity and conciseness rather than overwhelming AI agents with massive, monolithic prompts.

The five principles are: (1) Start with a high-level vision and use plan mode to enforce planning before execution, letting the AI expand a concise brief into a detailed spec. (2) Structure the spec like a professional PRD covering six areas GitHub identified as critical -- commands, testing, project structure, code style, git workflow, and boundaries. Integrate specs into your toolchain using a four-phase gated workflow: specify, plan, tasks, implement. (3) Break work into modular prompts, tackling one piece at a time; use extended TOC summaries, subagents, and parallel agents for large projects, being mindful of the "curse of instructions" where too many directives degrade model adherence. (4) Build in self-checks and constraints using three-tier boundaries (always/ask first/never), LLM-as-a-Judge for subjective quality checks, and conformance testing. (5) Test, iterate, and evolve the spec continuously, treating it as version-controlled code.

The article concludes with antipatterns to avoid: vague prompts, overlong contexts without summarization, skipping human review, conflating vibe coding with production engineering, ignoring the "lethal trifecta" of speed/nondeterminism/cost, and missing coverage of the six core spec areas. Osmani positions spec-writing as a management skill for AI agents, drawing on comparisons from Simon Willison about managing digital interns.

## Main Ideas

- AI agents need smart specs that balance detail with focus, not massive RFC-style documents that exceed the model's attention budget.
- The six core areas every spec should cover: commands, testing, project structure, code style, git workflow, and boundaries.
- A four-phase gated workflow (specify, plan, tasks, implement) prevents fragile "house of cards code."
- Three-tier boundaries (always do / ask first / never do) provide more nuanced guidance than flat rule lists.
- Modular prompts outperform monolithic ones; the "curse of instructions" causes models to ignore rules when given too many simultaneously.
- Subagents and parallel agent workflows can boost throughput but require clear task scoping and coordination.
- The spec is a living document that must evolve through continuous testing, feedback, and refinement.
