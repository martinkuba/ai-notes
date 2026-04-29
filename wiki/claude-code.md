---
tags: [tools, coding, anthropic, agents]
---

# Claude Code

Anthropic's terminal-based [Agentic Coding](agentic-coding.md) tool. Created by [Boris Cherny](boris-cherny.md). Operates in a terminal rather than an IDE, following a deliberate design philosophy around directness and composability.

## Workflow

The recommended workflow is **explore → plan → code → commit**:
1. Explore the codebase to understand context
2. Plan the approach (can use Plan Mode)
3. Execute the code changes
4. Review and commit

See source: [Claude Code Best Practices For Agentic Coding](../summaries/claude-code-best-practices-for-agentic-coding.md)

## Official Best Practices

The central constraint is **context window management** — performance degrades as context fills, making this the most important resource to manage. The highest-leverage practice is providing **self-verification criteria** (tests, screenshots, expected outputs) so Claude can check its own work. Other key practices: use Plan Mode to separate exploration from execution, write precise prompts referencing specific files and patterns, and keep CLAUDE.md files concise. For scaling, use non-interactive mode (`claude -p`) for CI, parallel sessions via the desktop app, the writer/reviewer pattern across separate sessions, and fan-out for batch operations. Common anti-patterns: "kitchen sink" sessions mixing unrelated tasks, bloated CLAUDE.md, skipping verification, and unbounded exploration.

See source: [Best Practices For Claude Code](../summaries/best-practices-for-claude-code.md)

## Customization

- **CLAUDE.md** — Project-level instructions that shape agent behavior. Functions like a persistent system prompt scoped to the repo.
- **[MCP](mcp.md) servers** — Extend Claude Code with external tool access (databases, APIs, etc.)
- **Custom slash commands** — User-defined workflows invoked via `/command`
- **Tool allowlists** — Control which bash commands the agent can run without confirmation
- **Claude Skills** — Reusable, scoped instruction sets (SKILL.md files) that Claude loads on demand via progressive disclosure. Unlike Projects (persistent context), Skills are executable workflows with clear inputs/outputs. Use cases include brand guidelines, lead scoring, report generation, and decision frameworks.

Engineers love the customizability: hooks, plugins, LSPs, MCPs, skills — every engineer's setup is different.

See sources: [Claude Code Creator Boris Shares His Setup With 13 Detailed Steps](../summaries/claude-code-creator-boris-shares-his-setup-with-13-detailed.md), [Reflecting On What Engineers Love About Claude Code](../summaries/reflecting-on-what-engineers-love-about-claude-code-one.md), [I Wanted To Share A Bunch Of My Favorite Hidden Features](../summaries/i-wanted-to-share-a-bunch-of-my-favorite-hidden.md), [5 Mind-Blowing Use Cases Of Claude Skills](../summaries/5-mind-blowing-use-cases-of-claude-skills.md)

## Advanced Features

Hidden and advanced capabilities: mobile app, teleport between devices, `/loop`, `/schedule`, hooks, remote control. Boris recommends running 5 parallel worktree sessions with Plan Mode and custom skills.

**Git Worktrees** — Built-in `claude --worktree` support lets agents run in parallel without interfering with each other. Each agent gets its own worktree branch, enabling free parallelization of tasks. Sub-agents also support worktrees for orchestrated multi-branch workflows.

See sources: [I Wanted To Share A Bunch Of My Favorite Hidden Features](../summaries/i-wanted-to-share-a-bunch-of-my-favorite-hidden.md), [I'm Boris And I Created Claude Code](../summaries/i-m-boris-and-i-created-claude-code.md), [I'm Using Claude Worktree For Everything Now](../summaries/i-m-using-claude-worktree-for-everything-now.md)

## Design Philosophy

Key lesson from building Claude Code: tool design matters as much as model capability. Structured tools like `AskUserQuestion` elicit better agent behavior than prompts alone.

See source: [Lessons From Building Claude Code Seeing Like An Agent](../summaries/lessons-from-building-claude-code-seeing-like-an-agent.md)

## Obsidian Integration

Claude Code integrates with Obsidian vaults for AI-assisted knowledge management — markdown files as thinking tools, vault indexes as context. With Obsidian CLI, Claude Code can access not just files but the inter-relationships between them, surfacing latent patterns and connections across your vault that you might not notice yourself.

See sources: [How To Build Your AI Second Brain Using Obsidian Claude Code](../summaries/how-to-build-your-ai-second-brain-using-obsidian-claude-code.md), [Obsidian Claude Code 101](../summaries/obsidian-claude-code-101.md), [How I Use Obsidian + Claude Code To Run My Life](../summaries/how-i-use-obsidian-claude-code-to-run-my-life.md)

## Impact

Described as a turning point in how software is built. Ethan Mollick frames it as evidence that AI is moving from "tool" to "colleague" in software engineering. The "Claude Christmas" event (late 2024) marked a step change in coding agent capability.

[Boris Cherny](boris-cherny.md) (head of Claude Code) reports 100% AI-authored code since November, shipping 10-30 PRs daily with 5 parallel agents. Semi Analysis found 4% of all GitHub commits authored by Claude Code (likely higher in private repos), projecting 20% by year-end. Boris predicts "coding is largely solved" and the title "software engineer" will be replaced by "builder." Productivity per engineer up 200% at Anthropic.

See sources: [Claude Code And What Comes Next](../summaries/claude-code-and-what-comes-next.md), [AI Writes The Code Now Whats Left For Software Engineers](../summaries/ai-writes-the-code-now-whats-left-for-software-engineers.md), [A Very Special Guest On This Episode Of The Lightcone](../summaries/a-very-special-guest-on-this-episode-of-the-lightcone.md), [Head Of Claude Code What Happens After Coding Is Solved](../summaries/head-of-claude-code-what-happens-after-coding-is-solved.md)

## Security Capabilities

Claude Opus 4.6 demonstrated the ability to uncover 500+ zero-day vulnerabilities in open-source code, showing capability beyond code generation into security research.

See source: [Anthropic S Claude Opus 4 6 Uncovers 500 Zero Day Flaws In Open Source Code](../summaries/anthropic-s-claude-opus-4-6-uncovers-500-zero-day-flaws-in.md)

## Related

- [Agentic Coding](agentic-coding.md)
- [Anthropic](anthropic.md)
- [Spec Driven Development](spec-driven-development.md)
