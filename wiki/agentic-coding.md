---
tags: [coding, agents, tools, productivity]
---

# Agentic Coding

The shift from manually writing code to directing AI agents that write code on your behalf. By late 2025, practitioners like [Andrej Karpathy](andrej-karpathy.md) report spending ~80% of coding time in agent-driven mode vs ~20% manual.

## Key Tools

- **[Claude Code](claude-code.md)** — Anthropic's terminal-based agentic coding tool. Follows an explore-plan-code-commit workflow. Customizable via CLAUDE.md files, MCP servers, and slash commands.
- **Cursor** — IDE with built-in agent mode, Plan Mode for structured planning, and rules/skills for extending agent behavior. See source: [Best Practices For Coding With Agents](../sources/best-practices-for-coding-with-agents.md)
- **GitHub Copilot** — Context-aware code completion using a prompt engineering pipeline (snippet extraction, context dressing, prioritization). See source: [A Developer S Guide To Prompt Engineering And LLMS](../sources/a-developer-s-guide-to-prompt-engineering-and-llms.md)

## Three Eras

Michael Truell (Cursor CEO) identifies three eras of AI-assisted development: tab completion → agents → cloud agents. In the latest era, developers manage fleets of autonomous agents running on cloud VMs. 35% of Cursor PRs already come from autonomous agents.

See source: [The Third Era Of AI Software Development](../sources/the-third-era-of-ai-software-development.md)

## Paradigm Shifts

### Vibe Coding
An intuitive, conversational style of coding with AI — describing what you want rather than specifying how. Works best when combined with [Spec Driven Development](spec-driven-development.md) to prevent chaos. See sources: [How I Learned To Stop Worrying And Love Vibe Coding](../sources/how-i-learned-to-stop-worrying-and-love-vibe-coding.md), [Vibe Specs Vibe Coding That Actually Works](../sources/vibe-specs-vibe-coding-that-actually-works.md)

### Code as Clay
In the agentic era, code becomes malleable material — easily reshaped, regenerated, and restructured. The cost of writing code drops to near zero, shifting value to judgment about *what* to build. See source: [Code Is Clay](../sources/code-is-clay.md)

### Reading vs Writing
A growing tension: AI makes writing code trivially easy but reading AI-generated code remains hard. Code review burden increases as the ratio of generated-to-handwritten code grows. See source: [It S Harder To Read Code Than To Write It](../sources/it-s-harder-to-read-code-than-to-write-it-especially-when.md)

### Agentic Engineering
Andrej Karpathy coined "vibe coding" for the reckless, unreviewed prototype style. For disciplined, agent-assisted development with human oversight, Karpathy proposed "agentic engineering" as the proper term. The distinction: vibe coding = YOLO; agentic engineering = AI does implementation, human owns architecture and correctness. Key practices: write a spec first, review every diff, test relentlessly, maintain a mental model of the codebase. Importantly, agentic engineering rewards senior engineers more than juniors — deep fundamentals become *more* valuable, not less.

See source: [Agentic Engineering](../sources/agentic-engineering.md)

### Comprehension Debt
The growing gap between how much code exists in a system and how much any human genuinely understands. Unlike technical debt, comprehension debt breeds false confidence — the codebase looks clean, tests are green, but the reckoning arrives quietly. AI generates code far faster than humans can evaluate it, breaking the traditional review feedback loop. An Anthropic study found engineers who used AI for code generation scored 17% lower on comprehension tests vs. controls. Tests help but can't substitute for understanding.

See source: [Comprehension Debt The Hidden Cost Of AI Generated Code](../sources/comprehension-debt-the-hidden-cost-of-ai-generated-code.md)

## Productivity Evidence

- [Andrej Karpathy](andrej-karpathy.md): Reports 10x productivity gains but warns of "slopacolypse" — a flood of low-quality AI-generated code. See source: [A Few Random Notes From Claude Coding Quite A Bit](../sources/a-few-random-notes-from-claude-coding-quite-a-bit.md)
- METR study (early 2025): Measured actual productivity impact on experienced open-source developers — results more nuanced than hype suggests. See source: [Measuring The Impact Of Early 2025 AI On Experienced Open Source Developers](../sources/measuring-the-impact-of-early-2025-ai-on-experienced-open.md)
- The "outship 10x" claim: Small teams leveraging AI agents can match output of much larger teams. See source: [How To Outship Teams 10x Your Size](../sources/how-to-outship-teams-10x-your-size.md)

## Best Practices

Key patterns emerging across tools:
1. **Spec first** — Write clear specifications before engaging the agent ([Spec Driven Development](spec-driven-development.md))
2. **Context management** — Curate what the agent sees via project files (CLAUDE.md, .cursorrules)
3. **Iterative refinement** — Start broad, then narrow; use plan-then-execute workflows
4. **Human review** — Treat AI output as draft code requiring careful review

See sources: [Claude Code Best Practices For Agentic Coding](../sources/claude-code-best-practices-for-agentic-coding.md), [Best Practices For Coding With Agents](../sources/best-practices-for-coding-with-agents.md)

## Orchestrating Multiple Agents

As tooling matures, the highest-leverage developers operate as **async-first managers** running fleets of parallel agents. Key insight: the bottleneck is no longer "can the agent write code?" — it's "can I manage multiple agents effectively?" This requires the same skills as tech lead or engineering manager: clear task scoping, delegation, verification loops, and async check-ins.

### Management Skills That Transfer
- **Clear task scoping** — Write a brief with outcome, context, constraints, non-goals, and acceptance criteria before prompting
- **Delegation** — Fully delegate mechanical tasks; stay in loop for architecture and product judgment; never delegate "should we build this?"
- **Verification loops** — Require agents to run tests and report results; use two-agent "writer + reviewer" patterns
- **Async check-ins** — Define structured status formats; set check-in cadences to prevent drift

See source: [Your AI Coding Agents Need A Manager](../sources/your-ai-coding-agents-need-a-manager.md)

### Cognitive Limits of Parallel Agents
Running multiple agents doesn't scale linearly for humans. Each parallel thread adds: context-switching costs (recovery time is the expensive part), continuous judgment calls that can't be batched, and "ambient anxiety tax" — background vigilance about threads you haven't checked. The cognitive ceiling shifts with thread complexity and session length. Practical ceiling for most developers: 3-4 well-scoped threads. The fix is usually tighter task scoping per thread, not fewer agents.

See sources: [Your Parallel Agent Limit](../sources/your-parallel-agent-limit.md), [Your AI Coding Agents Need A Manager](../sources/your-ai-coding-agents-need-a-manager.md)

## Related

- [Spec Driven Development](spec-driven-development.md)
- [AI And Software Engineering Jobs](ai-and-software-engineering-jobs.md)
- [Prompt Engineering](prompt-engineering.md)
- [Claude Code](claude-code.md)
