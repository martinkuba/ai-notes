---
tags: [coding, agents, tools, productivity]
---

# Agentic Coding

The shift from manually writing code to directing AI agents that write code on your behalf. By late 2025, practitioners like [[andrej-karpathy]] report spending ~80% of coding time in agent-driven mode vs ~20% manual.

## Key Tools

- **[[claude-code]]** — Anthropic's terminal-based agentic coding tool. Follows an explore-plan-code-commit workflow. Customizable via CLAUDE.md files, MCP servers, and slash commands.
- **Cursor** — IDE with built-in agent mode, Plan Mode for structured planning, and rules/skills for extending agent behavior. See source: [[sources/best-practices-for-coding-with-agents]]
- **GitHub Copilot** — Context-aware code completion using a prompt engineering pipeline (snippet extraction, context dressing, prioritization). See source: [[sources/a-developer-s-guide-to-prompt-engineering-and-llms]]

## Paradigm Shifts

### Vibe Coding
An intuitive, conversational style of coding with AI — describing what you want rather than specifying how. Works best when combined with [[spec-driven-development]] to prevent chaos. See sources: [[sources/how-i-learned-to-stop-worrying-and-love-vibe-coding]], [[sources/vibe-specs-vibe-coding-that-actually-works]]

### Code as Clay
In the agentic era, code becomes malleable material — easily reshaped, regenerated, and restructured. The cost of writing code drops to near zero, shifting value to judgment about *what* to build. See source: [[sources/code-is-clay]]

### Reading vs Writing
A growing tension: AI makes writing code trivially easy but reading AI-generated code remains hard. Code review burden increases as the ratio of generated-to-handwritten code grows. See source: [[sources/it-s-harder-to-read-code-than-to-write-it]]

## Productivity Evidence

- [[andrej-karpathy]]: Reports 10x productivity gains but warns of "slopacolypse" — a flood of low-quality AI-generated code. See source: [[sources/a-few-random-notes-from-claude-coding-quite-a-bit]]
- METR study (early 2025): Measured actual productivity impact on experienced open-source developers — results more nuanced than hype suggests. See source: [[sources/measuring-the-impact-of-early-2025-ai-on-experienced-open-source-developers]]
- The "outship 10x" claim: Small teams leveraging AI agents can match output of much larger teams. See source: [[sources/how-to-outship-teams-10x-your-size]]

## Best Practices

Key patterns emerging across tools:
1. **Spec first** — Write clear specifications before engaging the agent ([[spec-driven-development]])
2. **Context management** — Curate what the agent sees via project files (CLAUDE.md, .cursorrules)
3. **Iterative refinement** — Start broad, then narrow; use plan-then-execute workflows
4. **Human review** — Treat AI output as draft code requiring careful review

See sources: [[sources/claude-code-best-practices-for-agentic-coding]], [[sources/best-practices-for-coding-with-agents]]

## Related

- [[spec-driven-development]]
- [[ai-and-software-engineering-jobs]]
- [[prompt-engineering]]
- [[claude-code]]
