---
tags: [protocols, agents, anthropic, integrations]
---

# Model Context Protocol (MCP)

An open protocol introduced by [Anthropic](anthropic.md) for connecting AI agents to external tools, data sources, and services. MCP has become a foundational primitive of the [Agentic AI](agentic-ai.md) stack — the standard way agents reach beyond their context window into the world.

## What MCP Is

MCP is a standardized interface between an AI agent (the client) and a tool provider (the server). An MCP server exposes capabilities — file access, database queries, API calls, custom workflows — that any MCP-compatible agent can call. The protocol abstracts the wiring between models and tools so each side can evolve independently.

## Where MCP Shows Up in the Wiki

- **[Claude Code](claude-code.md)** — MCP servers are one of the four main customization levers (alongside CLAUDE.md, slash commands, and tool allowlists). They let Claude Code reach databases, APIs, browsers, and custom systems.
- **[Agentic AI](agentic-ai.md)** — MCP is one of the integration mechanisms used by enterprise "agent deployers" to connect agents to internal systems, alongside APIs and CLIs.
- **[Prompt Engineering](prompt-engineering.md)** — MCP connectors are part of the "apps and tools" customization lever for escaping default model behavior.

## Why It Matters

Foundation models without tools are limited to what fits in their context. MCP turns the agent into a router that can pull in fresh data, take actions, and chain operations across systems. This is what makes long-running agentic workflows (insurance claims, sales sequences, SRE investigations) possible — the agent has stable, governed access to the data and actions it needs.

The "harness is everything" thesis applies: model capability is largely a commodity now; the moat is in tool design, state management, and constraint enforcement. MCP is the protocol layer of that harness. See [Agentic AI](agentic-ai.md) for the harness argument.

## Related

- [Claude Code](claude-code.md)
- [Anthropic](anthropic.md)
- [Agentic AI](agentic-ai.md)
- [Agentic Coding](agentic-coding.md)
- [Prompt Engineering](prompt-engineering.md)
