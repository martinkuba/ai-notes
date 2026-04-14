---
tags: [tools, coding, anthropic, agents]
---

# Claude Code

Anthropic's terminal-based [Agentic Coding](agentic-coding.md) tool. Created by Boris Cherny. Operates in a terminal rather than an IDE, following a deliberate design philosophy around directness and composability.

## Workflow

The recommended workflow is **explore → plan → code → commit**:
1. Explore the codebase to understand context
2. Plan the approach (can use Plan Mode)
3. Execute the code changes
4. Review and commit

See source: [Claude Code Best Practices For Agentic Coding](../sources/claude-code-best-practices-for-agentic-coding.md)

## Customization

- **CLAUDE.md** — Project-level instructions that shape agent behavior. Functions like a persistent system prompt scoped to the repo.
- **MCP servers** — Extend Claude Code with external tool access (databases, APIs, etc.)
- **Custom slash commands** — User-defined workflows invoked via `/command`
- **Tool allowlists** — Control which bash commands the agent can run without confirmation

See source: [Claude Code Creator Boris Shares His Setup](../sources/claude-code-creator-boris-shares-his-setup.md)

## Impact

Described as a turning point in how software is built. Ethan Mollick frames it as evidence that AI is moving from "tool" to "colleague" in software engineering. The "Claude Christmas" event (late 2024) marked a step change in coding agent capability.

See sources: [Claude Code And What Comes Next](../sources/claude-code-and-what-comes-next.md), [AI Writes The Code Now Whats Left For Software Engineers](../sources/ai-writes-the-code-now-whats-left-for-software-engineers.md)

## Security Capabilities

Claude Opus 4.6 demonstrated the ability to uncover 500+ zero-day vulnerabilities in open-source code, showing capability beyond code generation into security research.

See source: [Anthropic S Claude Opus 4 6 Uncovers 500 Zero Day Flaws In Open Source Code](../sources/anthropic-s-claude-opus-4-6-uncovers-500-zero-day-flaws-in-open-source-code.md)

## Related

- [Agentic Coding](agentic-coding.md)
- [Anthropic](anthropic.md)
- [Spec Driven Development](spec-driven-development.md)
