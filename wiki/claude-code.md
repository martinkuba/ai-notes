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

Engineers love the customizability: hooks, plugins, LSPs, MCPs, skills — every engineer's setup is different.

See sources: [Claude Code Creator Boris Shares His Setup With 13 Detailed Steps](../sources/claude-code-creator-boris-shares-his-setup-with-13-detailed-steps.md), [Reflecting On What Engineers Love About Claude Code](../sources/reflecting-on-what-engineers-love-about-claude-code.md), [I Wanted To Share A Bunch Of My Favorite Hidden Features](../sources/i-wanted-to-share-a-bunch-of-my-favorite-hidden-features.md)

## Advanced Features

Hidden and advanced capabilities: mobile app, teleport between devices, `/loop`, `/schedule`, hooks, remote control. Boris recommends running 5 parallel worktree sessions with Plan Mode and custom skills.

See sources: [I Wanted To Share A Bunch Of My Favorite Hidden Features](../sources/i-wanted-to-share-a-bunch-of-my-favorite-hidden-features.md), [I'm Boris And I Created Claude Code](../sources/i-m-boris-and-i-created-claude-code.md)

## Design Philosophy

Key lesson from building Claude Code: tool design matters as much as model capability. Structured tools like `AskUserQuestion` elicit better agent behavior than prompts alone.

See source: [Lessons From Building Claude Code Seeing Like An Agent](../sources/lessons-from-building-claude-code-seeing-like-an-agent.md)

## Obsidian Integration

Claude Code integrates with Obsidian vaults for AI-assisted knowledge management — markdown files as thinking tools, vault indexes as context.

See sources: [How To Build Your AI Second Brain Using Obsidian Claude Code](../sources/how-to-build-your-ai-second-brain-using-obsidian-claude-code.md), [Obsidian Claude Code 101](../sources/obsidian-claude-code-101.md)

## Impact

Described as a turning point in how software is built. Ethan Mollick frames it as evidence that AI is moving from "tool" to "colleague" in software engineering. The "Claude Christmas" event (late 2024) marked a step change in coding agent capability.

See sources: [Claude Code And What Comes Next](../sources/claude-code-and-what-comes-next.md), [AI Writes The Code Now Whats Left For Software Engineers](../sources/ai-writes-the-code-now-whats-left-for-software-engineers.md), [A Very Special Guest On This Episode Of The Lightcone](../sources/a-very-special-guest-on-this-episode-of-the-lightcone.md)

## Security Capabilities

Claude Opus 4.6 demonstrated the ability to uncover 500+ zero-day vulnerabilities in open-source code, showing capability beyond code generation into security research.

See source: [Anthropic S Claude Opus 4 6 Uncovers 500 Zero Day Flaws In Open Source Code](../sources/anthropic-s-claude-opus-4-6-uncovers-500-zero-day-flaws-in-open-source-code.md)

## Related

- [Agentic Coding](agentic-coding.md)
- [Anthropic](anthropic.md)
- [Spec Driven Development](spec-driven-development.md)
