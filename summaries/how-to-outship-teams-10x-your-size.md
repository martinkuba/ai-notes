---
id: "01khrrhzkq9dyptw9byf83ssce"
title: "How to Outship Teams 10x Your Size"
author: "James Summerfield"
source_url: "https://www.linkedin.com/pulse/how-outship-teams-10x-your-size-james-summerfield-fyfae/"
category: "article"
tags: [ai, work]
saved_at: "2026-02-18T16:15:29.399000+00:00"
summarized_at: "2026-04-15T19:46:34Z"
---

# How to Outship Teams 10x Your Size

**Original source:** [How to Outship Teams 10x Your Size](https://www.linkedin.com/pulse/how-outship-teams-10x-your-size-james-summerfield-fyfae/)
**Author:** James Summerfield

## Summary

Summerfield argues that the bottleneck in software engineering has shifted from writing code to specifying intent and verifying results. Drawing an analogy to Sakichi Toyoda's self-stopping loom and the Toyota Production System's principle of jidoka (autonomation with a human touch), he describes how coding agents like Claude Code and Cursor have turned the act of writing code into "production work" while the highest-leverage activities have moved upstream (specification) and downstream (verification). The engineer who can run five agent sessions in parallel, specifying tasks clearly and reviewing output critically, will outproduce the one who writes beautiful code one function at a time.

His team has restructured around business domains rather than technical layers. Each engineer owns a domain end-to-end, writing specs, running agents, reviewing output, and shipping. The boundaries between domains are enforced through strict API contracts, with no cross-domain imports or database access. Platform engineers serve as force multipliers, building isolated environments, fast CI, and automated guardrails rather than shipping features directly. The poka-yoke principle applies: if a standard is not enforced in CI, it effectively does not exist.

Code review has also been reimagined. Instead of line-by-line human review of every diff, the team reviews intent (the spec) before work starts and verifies behavior after work completes, while agent reviewers and CI handle the mechanical middle. Summerfield acknowledges this feels uncomfortable but argues the guardrails have not been removed, only moved from manual processes to automated systems. He frames the current moment as roughly stage four or five of Shigeo Shingo's twenty-three stages between manual work and full automation, noting that the next unsolved problem is automating the incident management loop to match the throughput of automated production.

## Main Ideas

- The bottleneck in software engineering has moved from typing code to specifying what to build and verifying whether it works.
- Teams should organize around business domains rather than technical layers, with each engineer owning a domain end-to-end.
- Platform engineers are force multipliers whose job is to build guardrails, tooling, and CI that enforce quality standards agents alone would never set.
- Code review should be split: humans review intent and outcomes, while agents and CI handle the mechanical diff review.
- Running multiple agent sessions in parallel is the key skill that separates a team of ten from a team of a hundred.
- Strict architectural boundaries (API contracts, no cross-domain imports) are what enable speed, not restrict it.
- The next frontier is automating incident management to keep pace with the increased throughput from agent-driven production.

## Key Quotes

- "The bottleneck in software engineering is no longer the typing. It's the intent: knowing what to build, specifying it precisely enough that an agent can execute it, and verifying that the result actually works."
- "If a standard isn't enforced in CI, it does not exist."
- "That is how you outship a team ten times your size. Not by typing faster. By recognising that the typing was never the bottleneck."
