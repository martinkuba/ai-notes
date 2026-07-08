---
id: "01khm04v4wrg81bw9xxq3yx83q"
title: "My AI Adoption Journey"
author: "Mitchell Hashimoto"
source_url: "https://mitchellh.com/writing/my-ai-adoption-journey/"
category: "article"
tags: [ai, work]
saved_at: "2026-02-16T19:51:55.290000+00:00"
summarized_at: "2026-06-09T00:00:04Z"
---

# My AI Adoption Journey

**Original source:** [My AI Adoption Journey](https://mitchellh.com/writing/my-ai-adoption-journey/)
**Author:** Mitchell Hashimoto

## Summary

Mitchell Hashimoto documents his practical journey learning to work effectively with AI agents, moving through six sequential phases of adoption. He begins by abandoning chat interfaces entirely in favor of agent-based tools with autonomous capabilities (file reading, program execution, HTTP requests), realizing that interactive chatbots are fundamentally inefficient for coding tasks. He then forces himself through a painful period of "reproducing his own work" — executing tasks twice, manually and then through agents — to develop expertise and understand what agents excel and fail at.

As his confidence grows, Hashimoto shifts to running agents asynchronously during off-hours and off-peak time, focusing on high-confidence "slam dunk" tasks where he's near-certain agents will succeed. He emphasizes turning off notifications to avoid context-switching costs. The turning point comes through "harness engineering" — actively preventing agent mistakes by documenting requirements (AGENTS.md) and building better tools. By step 6, his goal is maintaining continuous background agent work on low-confidence, high-value tasks, allowing him to focus deeply on work he enjoys while remaining productive overall.

Throughout, Hashimoto stresses that true efficiency gains come not from doing everything faster, but from understanding what agents shouldn't be used for and deliberately delegating tasks at the edges of agent capability. His measured, empirically-grounded approach avoids hype while capturing real workflow improvements.

## Main Ideas

- **Agents, not chatbots:** Interactive chat interfaces are inherently inefficient for coding; only agents that can read files, execute programs, and make requests provide meaningful value.
- **Expertise through duplication:** Force yourself to reproduce manual work through agents to develop deep, grounded understanding of what they're good and bad at.
- **Asynchronous leverage:** Use agent work during low-personal-productivity times (end-of-day, off-hours) to create a "warm start" for the next day, trading deep thinking for parallel progress.
- **High-confidence delegation:** Build confidence through iteration, then systematically delegate only the tasks where you're near-certain agents will succeed with minimal touch-ups.
- **Harness engineering:** Prevention beats correction — document requirements and build tools that help agents avoid mistakes rather than fixing them repeatedly.
- **Context switching tax:** Turn off agent notifications; interruptions destroy focus and efficiency. Check on agents during natural breaks, not the reverse.
- **Workflow, not replacement:** The goal isn't faster work overall, but redirecting effort from tasks you don't enjoy toward tasks where you form skills and stay engaged.

## Key Quotes

- "To find value, you *must* use an **agent**. An agent is the industry-adopted term for an LLM that can chat and invoke external behavior in a loop."
- "I'd do the work manually, and then I'd fight an agent to produce identical results in terms of quality and function (without it being able to see my manual solution, of course)."
- "Very important at this stage: turn off agent desktop notifications. Context switching is very expensive."
- "This is where I'm at today. I'm making an earnest effort whenever I see an agent do a Bad Thing to prevent it from ever doing that bad thing again."
