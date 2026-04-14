---
tags: [tools, coding, anthropic, agents]
---

# Claude Code

Anthropic's terminal-based [[agentic-coding]] tool. Created by Boris Cherny. Operates in a terminal rather than an IDE, following a deliberate design philosophy around directness and composability.

## Workflow

The recommended workflow is **explore → plan → code → commit**:
1. Explore the codebase to understand context
2. Plan the approach (can use Plan Mode)
3. Execute the code changes
4. Review and commit

See source: [[sources/claude-code-best-practices-for-agentic-coding]]

## Customization

- **CLAUDE.md** — Project-level instructions that shape agent behavior. Functions like a persistent system prompt scoped to the repo.
- **MCP servers** — Extend Claude Code with external tool access (databases, APIs, etc.)
- **Custom slash commands** — User-defined workflows invoked via `/command`
- **Tool allowlists** — Control which bash commands the agent can run without confirmation

See source: [[sources/claude-code-creator-boris-shares-his-setup]]

## Impact

Described as a turning point in how software is built. Ethan Mollick frames it as evidence that AI is moving from "tool" to "colleague" in software engineering. The "Claude Christmas" event (late 2024) marked a step change in coding agent capability.

See sources: [[sources/claude-code-and-what-comes-next]], [[sources/ai-writes-the-code-now-whats-left-for-software-engineers]]

## Security Capabilities

Claude Opus 4.6 demonstrated the ability to uncover 500+ zero-day vulnerabilities in open-source code, showing capability beyond code generation into security research.

See source: [[sources/anthropic-s-claude-opus-4-6-uncovers-500-zero-day-flaws-in-open-source-code]]

## Related

- [[agentic-coding]]
- [[anthropic]]
- [[spec-driven-development]]
