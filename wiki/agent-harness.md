---
tags: [agents, architecture, infrastructure, systems]
---

# Agent Harness

The scaffolding that surrounds a language model and makes it useful for autonomous work. An agent equals a model plus a harness — everything beyond the model itself: prompts, tools, context policies, hooks, sandboxes, memory files, and feedback loops.

> "If you're not the model, you're the harness."

See sources: [Agent Harness Engineering](../summaries/agent-harness-engineering.md), [Deriving Agent Harnesses from First Principles](../summaries/deriving-agent-harnesses-from-first-principles.md), [The Harness Is Everything](../summaries/the-harness-is-everything-what-cursor-claude-code-and.md)

## The Core Insight

A decent model with an excellent harness consistently outperforms a great model with poor scaffolding. The gap between what today's models can theoretically do and what you actually see them doing is largely a harness gap.

Interface design alone produced a 64% performance improvement in the SWE-agent research — with identical underlying models. The execution layer (foundation model generating functional code) is a commodity; the real moat is orchestration, state management, and constraint enforcement.

## Core Model Limitations Without a Harness

Models cannot natively:
- Maintain durable state across sessions
- Execute code or run shell commands
- Access real-time or external knowledge
- Set up their own execution environments

The harness provides all of these.

## Harness Components

### Durable State
**Filesystem** — the foundational primitive. Enables persistent storage, context offloading, incremental work, and natural multi-agent collaboration surfaces (agents read/write shared files). **Git** provides versioning, rollback, and a history the agent can reason about.

### Execution
**Bash / code execution** — a general-purpose tool. Rather than being constrained to pre-configured tools, agents with bash access can design and execute their own solutions autonomously.

### Safety
**Sandboxes** — isolated environments with configurable defaults, security controls, and rich tooling (runtimes, browsers, test runners). Allow safe exploration without permanent side effects.

### Knowledge
**Memory files** (CLAUDE.md, AGENTS.md) — inject persistent knowledge into the context window. Durable lessons from past failures become encoded constraints. See [Claude Code](claude-code.md) for CLAUDE.md conventions.

### Context Management
Context rot is the gradual degradation of model reasoning as the context window fills with irrelevant, stale, or redundant content. Harnesses fight this through:
- **Compaction** — summarizing earlier context
- **Tool output offloading** — writing large outputs to files rather than returning them inline
- **Progressive disclosure** — surfacing only the tools and instructions relevant to the current step

### Long-Horizon Execution
Multi-step tasks that span context windows need:
- Explicit planning files tracking current state
- Git checkpoints after logical work batches
- Self-verification loops (run tests, check outputs)
- Planner/executor splits for complex workflows

### Enforcement
**Hooks** — shell commands that fire on agent events (before/after tool calls, on session end). Used to block destructive commands, enforce conventions, and log activity.

## The Ratchet Principle

Treat each agent failure as a permanent signal, not a one-off. Every mistake should trigger lasting harness improvements:
- If the agent ignored a convention → add it to AGENTS.md
- If it ran a destructive command → write a hook to block it
- If it got lost in a 40-step task → split into planner + executor

This creates a ratchet effect: the harness becomes progressively more refined, and the same mistake never recurs.

## Behavior-Driven Design

Each harness component should directly serve a specific desired behavior. If you can't name the behavior a component delivers, remove it. Harnesses built by adding components without a clear behavioral purpose become bloated and fragile.

## Harnesses Evolve, Not Shrink

As models improve, harnesses don't become obsolete — they shift to address new failure modes and enable previously unreachable capabilities. The model-harness relationship is co-evolutionary: useful primitives discovered in harnesses get incorporated into model training, which changes the failure modes the next harness must address.

## Industry Convergence

Tools like Cursor, Claude Code, and GitHub Copilot have converged on similar harness patterns: git worktrees for isolation, task-based interfaces replacing file tabs, async background agents, and CI/CD integration. These patterns are becoming fundamental conventions.

## Related

- [Agentic AI](agentic-ai.md)
- [Agentic Coding](agentic-coding.md)
- [Claude Code](claude-code.md)
- [Addy Osmani](addy-osmani.md)
