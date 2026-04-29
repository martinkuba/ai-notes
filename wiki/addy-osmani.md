---
tags: [people, coding, agents, productivity]
---

# Addy Osmani

Engineer and writer; the wiki's most-cited contemporary voice on the practical discipline of [Agentic Coding](agentic-coding.md). Where [Andrej Karpathy](andrej-karpathy.md) named the cultural moment ("vibe coding," "slopacolypse"), Osmani has named its failure modes — and offered the working frame for what to do about them.

## Coined Concepts

- **Comprehension debt** — The gap between how much code exists in a system and how much any human genuinely understands. Unlike technical debt, it breeds false confidence: tests pass, the codebase looks clean, and no one can explain the design decisions. See [AI Impact On Software Engineering](ai-impact-on-software-engineering.md).
- **Ambient anxiety tax** — The background vigilance cost of running parallel agents: continuous worry about what unmonitored threads might be getting wrong. A hidden cognitive ceiling on agent parallelism.
- **Agentic engineering** — The professional alternative to [vibe coding](vibe-coding.md). Engineers orchestrate AI agents that handle implementation while the human acts as architect, reviewer, and decision-maker. Requires upfront planning, rigorous review, comprehensive testing, and full codebase ownership. See source: [Agentic Engineering](../summaries/agentic-engineering.md).

## Core Arguments

### Agent management is a skill
The bottleneck isn't "can the agent write code?" — it's clarity, delegation, verification, and async communication. Four management skills transfer directly: scoping with briefs, delegation judgment (hand off vs. checkpoint vs. own), verification loops (tests, lint, writer/reviewer), and structured async check-ins. See source: [Your AI Coding Agents Need A Manager](../summaries/your-ai-coding-agents-need-a-manager.md).

### The parallel agent ceiling is ~3-4 threads
Supervision scales but understanding doesn't, and the gap is where comprehension debt compounds. Three focused threads produce more mergeable output than six half-supervised ones. See source: [Your Parallel Agent Limit](../summaries/your-parallel-agent-limit.md).

### The IDE is being de-centered
The unit of work shifts from the file to the agent. Development moves from "open files → edit → build → debug" to "specify intent → delegate → observe → review diffs → merge." The IDE becomes a subordinate instrument; orchestration migrates to dashboards and cloud control planes. See source: [Is The IDE Dead](../summaries/is-the-ide-dead.md).

### Specs over code
Code is regenerable; intent is not. The spec becomes the durable artifact. See [Spec Driven Development](spec-driven-development.md), source: [How To Write A Good Spec For AI Agents (Osmani)](../summaries/how-to-write-a-good-spec-for-ai-agents-01kjng.md).

### Senior engineers benefit disproportionately
Agentic engineering rewards engineers who can efficiently review and correct AI output. Juniors risk skill atrophy. See [AI And Software Engineering Jobs](ai-and-software-engineering-jobs.md).

## Related

- [Agentic Coding](agentic-coding.md)
- [Vibe Coding](vibe-coding.md)
- [AI Impact On Software Engineering](ai-impact-on-software-engineering.md)
- [Spec Driven Development](spec-driven-development.md)
- [Andrej Karpathy](andrej-karpathy.md)
