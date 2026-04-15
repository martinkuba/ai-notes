---
id: "01kjjgmfx8ve0bxmspb0be7bqm"
title: "The third era of AI software development"
author: "Michael Truell"
source_url: "https://x.com/mntruell/status/2026736314272591924/?rw_tt_thread=True"
category: "tweet"
tags: [ai]
saved_at: "2026-02-28T16:17:18.248000+00:00"
summarized_at: "2026-04-15T19:53:49Z"
---

# The third era of AI software development

**Original source:** [The third era of AI software development](https://x.com/mntruell/status/2026736314272591924/?rw_tt_thread=True)
**Author:** Michael Truell

## Summary

Michael Truell, co-founder of Cursor, describes three eras of AI-assisted software development. The first era was Tab autocomplete, which excelled at automating low-entropy, repetitive work and dominated for nearly two years. The second era brought synchronous agents, where developers directed AI through prompt-and-response loops -- this shift was so complete that many Cursor users stopped using Tab entirely, with agent users now outnumbering Tab users 2:1 (flipped from 2.5:1 the other way in March 2025). The third era, now arriving, features agents that tackle larger tasks independently over longer timescales with less human direction.

In this third era, Cursor is no longer primarily about writing code -- it's about helping developers build the "factory that creates their software," composed of fleets of agents they interact with as teammates. Cloud agents run on their own virtual machines, work through tasks over hours, iterate and test autonomously, and return reviewable artifacts (logs, video recordings, live previews) rather than just diffs. This makes parallel agent execution practical. At Cursor itself, 35% of merged PRs are now created by agents operating autonomously in cloud VMs. Developers adopting this model share three traits: agents write nearly 100% of their code, they spend time breaking down problems and reviewing artifacts rather than writing code, and they spin up multiple agents simultaneously. The main challenges remaining are infrastructure reliability (a flaky test becomes a failure interrupting every agent run) and ensuring agents have full access to needed tools and context.

## Main Ideas

- Three eras of AI coding: Tab autocomplete, synchronous agents, and now autonomous cloud agents working independently over longer timescales
- Agent users now outnumber Tab users 2:1 in Cursor, a complete reversal from March 2025
- 35% of PRs merged at Cursor are created by autonomous agents running in cloud VMs
- The developer role is shifting from writing code to building the "factory" -- defining problems, reviewing artifacts, and managing fleets of agents
- Cloud agents return reviewable artifacts (logs, videos, live previews) rather than just code diffs, enabling practical parallel execution
- Infrastructure reliability is the key challenge: flaky tests and broken environments interrupt every parallel agent run

## Key Quotes

- "Cursor is no longer primarily about writing code. It is about helping developers build the factory that creates their software."
- "A year from now, we think the vast majority of development work will be done by these kinds of agents."
