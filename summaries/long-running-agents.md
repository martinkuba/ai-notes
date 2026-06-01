---
id: "01kst5bc30tn4c2mpke7nwtyw1"
title: "Long-running Agents"
author: "Addy Osmani"
source_url: "https://addyo.substack.com/p/long-running-agents"
category: "article"
tags: [ai]
saved_at: "2026-05-29T15:23:53.312000+00:00"
summarized_at: "2026-05-31T23:38:43Z"
---

# Long-running Agents

**Original source:** [Long-running Agents](https://addyo.substack.com/p/long-running-agents)
**Author:** Addy Osmani

## Summary

Traditional AI agents operate in a single session, working within a limited context window and typically completing within minutes or hours. Long-running agents represent a fundamental shift: systems that maintain progress over days or weeks across multiple context windows, sandboxes, and execution sessions while leaving structured artifacts that enable recovery and continuation. This architecture unlocks dramatically more work—where a 10-minute agent answers questions or fixes small bugs, a 10-hour agent can own entire features, complete multi-quarter migrations, or conduct comprehensive research sweeps. Anthropic's internal testing showed 30+ hours of autonomous coding, including one run producing an 11,000-line Slack-style application.

The engineering challenges center on three walls: finite context windows that fill and degrade (context rot), no persistent state between sessions, and models that grade their own work too optimistically. The major labs—Anthropic, Google, and Cursor—have converged on similar architectural solutions: decoupling the model loop (brain) from the execution environment (hands) from the durable session log, separating planning from generation from evaluation, and baking in checkpointing and structured handoffs. Implementations vary (Anthropic's harness-based approach, Cursor's planner/worker/judge pipeline, Google's Agent Platform with Memory Bank), but all share a core principle: **state lives outside the model's context window**, and structured handoffs between sessions allow agents to wake up and continue.

For developers, the practical starting point is using existing tools like Claude Code with the Ralph loop pattern: maintain a task list and progress file outside context, checkpoint after meaningful work, and run skeptical verification when completion is claimed. For production systems, the choice is between managed platforms (Google Agent Platform, Claude Managed Agents) that handle persistence and observability, or self-hosted solutions using ADK or Claude Agent SDK with custom infrastructure.

## Main Ideas

- **Three dimensions of "long-running"**: Long-horizon reasoning (model coherence over many steps), long-running execution (process runs for days with thousands of model invocations), and persistent agency (agent identity that accumulates memory across time)
- **Three core problems**: Finite context that fills and degrades, loss of state between sessions without explicit persistence, and models grading their own work too generously without external verification
- **Brain/hands/session architecture**: Decoupling model loop, execution environment, and durable event log enables failure recovery, fast cold starts, and auditability while keeping state external to context window
- **Five production patterns**: Checkpoint-and-resume for multi-day work, delegated approval (human-in-the-loop with full state intact), memory-layered context (long-term curated memory with governance), ambient processing (event-driven unsupervised agents), fleet orchestration (coordinator/specialist agents)
- **Separation of concerns**: Split planning from generation from evaluation to prevent agents from redefining "done" mid-run and suppress the self-grading bias
- **The Ralph loop**: Simple practitioner pattern—bash script, JSON task list, progress file—keeps state on filesystem, enabling amnesiac agents to continue across sessions by reading disk state
- **Real limitations**: Cost control requires explicit budgets, larger attack surface demands credential isolation, alignment drift requires memory governance, and verification remains a human-time problem

## Key Quotes

> "An agent that runs for ten minutes can answer a question, summarize a doc, fix a small bug. An agent that runs for ten hours can own an entire feature, finish a migration that was on the backlog for six quarters, or do the kind of overnight research sweep that used to require a junior analyst."

> "The session-as-event-log idea is the part most teams underappreciate. It is what makes a long-running agent recoverable. Without it, a container failure is a session failure and you're debugging into a stale snapshot. With it, the agent's memory is a queryable artifact that lives outside whatever process happens to be running at the moment."

> "The model is still load-bearing. But the gap between a chat window and an agent you can leave running overnight is mostly in the state, sessions, and structured handoffs wrapped around it."
