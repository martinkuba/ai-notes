---
tags: [coding, agents, tools, productivity]
---

# Agentic Coding

The shift from manually writing code to directing AI agents that write code on your behalf. By late 2025, practitioners like [Andrej Karpathy](andrej-karpathy.md) report spending ~80% of coding time in agent-driven mode vs ~20% manual.

## Key Tools

- **[Claude Code](claude-code.md)** — Anthropic's terminal-based agentic coding tool. Follows an explore-plan-code-commit workflow. Customizable via CLAUDE.md files, MCP servers, and slash commands.
- **Cursor** — IDE with built-in agent mode, Plan Mode for structured planning, and rules/skills for extending agent behavior. See source: [Best Practices For Coding With Agents](../summaries/best-practices-for-coding-with-agents.md)
- **GitHub Copilot** — Context-aware code completion using a prompt engineering pipeline (snippet extraction, context dressing, prioritization). See source: [A Developer S Guide To Prompt Engineering And LLMS](../summaries/a-developer-s-guide-to-prompt-engineering-and-llms.md)

## Three Eras

Michael Truell (Cursor CEO) identifies three eras of AI-assisted development: tab completion → agents → cloud agents. In the latest era, developers manage fleets of autonomous agents running on cloud VMs. 35% of Cursor PRs already come from autonomous agents.

See source: [The Third Era Of AI Software Development](../summaries/the-third-era-of-ai-software-development.md)

## Paradigm Shifts

### Vibe Coding vs Agentic Engineering
[Andrej Karpathy](andrej-karpathy.md) coined "vibe coding" to describe prompt-and-accept AI programming without code review. Addy Osmani argues the term has become overloaded, conflating reckless prototyping with disciplined AI-assisted work. He endorses "agentic engineering" — also suggested by Karpathy — as the professional alternative: engineers orchestrate AI agents that handle implementation while the human acts as architect, reviewer, and decision-maker. Unlike vibe coding, agentic engineering requires upfront planning, rigorous code review, comprehensive testing, and full codebase ownership. Crucially, this approach disproportionately benefits senior engineers who can efficiently review and correct AI output, while juniors risk skill atrophy. See sources: [Agentic Engineering](../summaries/agentic-engineering.md), [How I Learned To Stop Worrying And Love Vibe Coding](../summaries/how-i-learned-to-stop-worrying-and-love-vibe-coding.md), [Vibe Specs Vibe Coding That Actually Works](../summaries/vibe-specs-vibe-coding-that-actually-works.md)

### Code as Clay
In the agentic era, code becomes malleable material — easily reshaped, regenerated, and restructured. The cost of writing code drops to near zero, shifting value to judgment about *what* to build. See source: [Code Is Clay](../summaries/code-is-clay.md)

### Reading vs Writing
A growing tension: AI makes writing code trivially easy but reading AI-generated code remains hard. Code review burden increases as the ratio of generated-to-handwritten code grows. See source: [It S Harder To Read Code Than To Write It](../summaries/it-s-harder-to-read-code-than-to-write-it-especially-when.md)

## Productivity Evidence

- [Andrej Karpathy](andrej-karpathy.md): Reports 10x productivity gains but warns of "slopacolypse" — a flood of low-quality AI-generated code. See source: [A Few Random Notes From Claude Coding Quite A Bit](../summaries/a-few-random-notes-from-claude-coding-quite-a-bit.md)
- METR study (early 2025): Measured actual productivity impact on experienced open-source developers — results more nuanced than hype suggests. See source: [Measuring The Impact Of Early 2025 AI On Experienced Open Source Developers](../summaries/measuring-the-impact-of-early-2025-ai-on-experienced-open.md)
- The "outship 10x" claim: Small teams leveraging AI agents can match output of much larger teams. See source: [How To Outship Teams 10x Your Size](../summaries/how-to-outship-teams-10x-your-size.md)

## Best Practices

Key patterns emerging across tools:
1. **Spec first** — Write clear specifications before engaging the agent ([Spec Driven Development](spec-driven-development.md))
2. **Context management** — Curate what the agent sees via project files (CLAUDE.md, .cursorrules)
3. **Iterative refinement** — Start broad, then narrow; use plan-then-execute workflows
4. **Human review** — Treat AI output as draft code requiring careful review

See sources: [Claude Code Best Practices For Agentic Coding](../summaries/claude-code-best-practices-for-agentic-coding.md), [Best Practices For Coding With Agents](../summaries/best-practices-for-coding-with-agents.md)

## Multi-Agent Management

As developers move from pairing with a single agent to orchestrating parallel fleets, the bottleneck shifts from "can the agent write code?" to management: clarity, delegation, verification, and async communication. Osmani describes the highest-leverage developers as async-first managers running small fleets, splitting work into high-touch local sessions (architecture, product nuance) and async background sessions (migrations, test generation, docs).

Four management skills transfer directly: clear task scoping with briefs, delegation judgment (hand off vs. checkpoint vs. own), verification loops (tests, lint, writer/reviewer pattern), and async check-ins with structured status updates. Merge conflicts are a boundary failure — solve with git worktrees and one-agent-one-PR rules. See source: [Your AI Coding Agents Need A Manager](../summaries/your-ai-coding-agents-need-a-manager.md)

### The Parallel Agent Ceiling

Running parallel agents imposes hidden cognitive costs: context switching between threads, continuous judgment calls that can't be batched, and trust calibration overhead for each agent. Osmani identifies an "ambient anxiety tax" — background vigilance about what unmonitored threads might be getting wrong. Agent parallelism doesn't scale linearly for humans: supervision scales but understanding doesn't, and the gap is where [comprehension debt](ai-impact-on-software-engineering.md) compounds. The practical ceiling is 3-4 well-reviewed threads; three focused threads produce more mergeable output than six half-supervised ones. See source: [Your Parallel Agent Limit](../summaries/your-parallel-agent-limit.md)

## The IDE Is Being De-Centered

The traditional IDE is not disappearing but losing its role as the primary workspace. Addy Osmani argues the center of developer work is shifting from line-by-line editing toward supervising autonomous agents that plan, rewrite files, run tests, and propose diffs for review. The "unit of work" becomes the agent rather than the file; the development loop shifts from "open files → edit → build → debug" to "specify intent → delegate → observe → review diffs → merge."

Convergent patterns across tools (Cursor Glass, Claude Code Web, GitHub Copilot Agents): git worktrees for isolation, task-based UI replacing file tabs, async background agents, and CI/CD integration. New challenges include review fatigue, expanded security surfaces, and governance overhead. The IDE becomes a subordinate instrument for targeted inspection and final edits; orchestration migrates to dashboards and cloud control planes.

See source: [Is The IDE Dead](../summaries/is-the-ide-dead.md)

## Resources

A curated collection of high-signal conference talks on AI-assisted coding (agents, context management, prompt engineering, spec-driven development, measuring ROI) — chosen over viral social media content for depth. Covers "12-Factor Agents," context platform engineering, anthropomorphization risks, and tool-specific guidance for Claude, Copilot, and Amp Code.

See source: [The Best AI Coding Content Isn't On Your Feed](../summaries/the-best-ai-coding-content-isn-t-on-your-feed.md)

## Related

- [Spec Driven Development](spec-driven-development.md)
- [AI And Software Engineering Jobs](ai-and-software-engineering-jobs.md)
- [Prompt Engineering](prompt-engineering.md)
- [Claude Code](claude-code.md)
- [AI Impact On Software Engineering](ai-impact-on-software-engineering.md)
