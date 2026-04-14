---
tags: [coding, agents, tools, productivity]
---

# Agentic Coding

The shift from manually writing code to directing AI agents that write code on your behalf. By late 2025, practitioners like [Andrej Karpathy](andrej-karpathy.md) report spending ~80% of coding time in agent-driven mode vs ~20% manual.

## Key Tools

- **[Claude Code](claude-code.md)** — Anthropic's terminal-based agentic coding tool. Follows an explore-plan-code-commit workflow. Customizable via CLAUDE.md files, MCP servers, and slash commands.
- **Cursor** — IDE with built-in agent mode, Plan Mode for structured planning, and rules/skills for extending agent behavior. See source: [Best Practices For Coding With Agents](../sources/best-practices-for-coding-with-agents.md)
- **GitHub Copilot** — Context-aware code completion using a prompt engineering pipeline (snippet extraction, context dressing, prioritization). See source: [A Developer S Guide To Prompt Engineering And LLMS](../sources/a-developer-s-guide-to-prompt-engineering-and-llms.md)

## Paradigm Shifts

### Vibe Coding
An intuitive, conversational style of coding with AI — describing what you want rather than specifying how. Works best when combined with [Spec Driven Development](spec-driven-development.md) to prevent chaos. See sources: [How I Learned To Stop Worrying And Love Vibe Coding](../sources/how-i-learned-to-stop-worrying-and-love-vibe-coding.md), [Vibe Specs Vibe Coding That Actually Works](../sources/vibe-specs-vibe-coding-that-actually-works.md)

### Code as Clay
In the agentic era, code becomes malleable material — easily reshaped, regenerated, and restructured. The cost of writing code drops to near zero, shifting value to judgment about *what* to build. See source: [Code Is Clay](../sources/code-is-clay.md)

### Reading vs Writing
A growing tension: AI makes writing code trivially easy but reading AI-generated code remains hard. Code review burden increases as the ratio of generated-to-handwritten code grows. See source: [It S Harder To Read Code Than To Write It](../sources/it-s-harder-to-read-code-than-to-write-it.md)

## Productivity Evidence

- [Andrej Karpathy](andrej-karpathy.md): Reports 10x productivity gains but warns of "slopacolypse" — a flood of low-quality AI-generated code. See source: [A Few Random Notes From Claude Coding Quite A Bit](../sources/a-few-random-notes-from-claude-coding-quite-a-bit.md)
- METR study (early 2025): Measured actual productivity impact on experienced open-source developers — results more nuanced than hype suggests. See source: [Measuring The Impact Of Early 2025 AI On Experienced Open Source Developers](../sources/measuring-the-impact-of-early-2025-ai-on-experienced-open-source-developers.md)
- The "outship 10x" claim: Small teams leveraging AI agents can match output of much larger teams. See source: [How To Outship Teams 10x Your Size](../sources/how-to-outship-teams-10x-your-size.md)

## Best Practices

Key patterns emerging across tools:
1. **Spec first** — Write clear specifications before engaging the agent ([Spec Driven Development](spec-driven-development.md))
2. **Context management** — Curate what the agent sees via project files (CLAUDE.md, .cursorrules)
3. **Iterative refinement** — Start broad, then narrow; use plan-then-execute workflows
4. **Human review** — Treat AI output as draft code requiring careful review

See sources: [Claude Code Best Practices For Agentic Coding](../sources/claude-code-best-practices-for-agentic-coding.md), [Best Practices For Coding With Agents](../sources/best-practices-for-coding-with-agents.md)

## Related

- [Spec Driven Development](spec-driven-development.md)
- [AI And Software Engineering Jobs](ai-and-software-engineering-jobs.md)
- [Prompt Engineering](prompt-engineering.md)
- [Claude Code](claude-code.md)
