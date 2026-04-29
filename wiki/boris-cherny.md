---
tags: [people, anthropic, coding, claude-code]
---

# Boris Cherny

Creator and head of [Claude Code](claude-code.md) at [Anthropic](anthropic.md). The wiki's primary source of strong-form claims that "coding is largely solved." His numbers anchor several pages on AI's impact on software engineering.

## Headline Claims

- **100% AI-authored code since November**: Cherny reports writing none of his own code since that point.
- **200% productivity gains** at Anthropic following Claude Code adoption.
- **10-30 PRs per day** shipped personally, running 5 parallel agents in worktree sessions.
- **4% of all GitHub commits** authored by Claude Code (Semi Analysis), projected to reach 20% by year-end. Likely higher in private repos.
- **The title "software engineer" will be replaced by "builder."**

See sources: [Head Of Claude Code What Happens After Coding Is Solved](../summaries/head-of-claude-code-what-happens-after-coding-is-solved.md), [AI Writes The Code Now Whats Left For Software Engineers](../summaries/ai-writes-the-code-now-whats-left-for-software-engineers.md), [Claude Code And What Comes Next](../summaries/claude-code-and-what-comes-next.md).

## Setup and Working Style

Cherny's recommended Claude Code setup: 5 parallel worktree sessions, Plan Mode, custom skills, and a curated set of hooks and MCP servers. Treats CLAUDE.md files as project-scoped system prompts. See sources: [Claude Code Creator Boris Shares His Setup With 13 Detailed Steps](../summaries/claude-code-creator-boris-shares-his-setup-with-13-detailed.md), [I'm Boris And I Created Claude Code](../summaries/i-m-boris-and-i-created-claude-code.md).

## Design Lessons

Key lesson from building Claude Code: tool design matters as much as model capability. Structured tools (e.g., `AskUserQuestion`) elicit better agent behavior than prompts alone. See source: [Lessons From Building Claude Code Seeing Like An Agent](../summaries/lessons-from-building-claude-code-seeing-like-an-agent.md).

## Tension With Other Evidence

Cherny's claims sit in direct tension with several findings catalogued elsewhere in the wiki:
- The METR study found AI **slowed experienced developers by 19%** in early 2025.
- Thousands of CEOs reported **no measurable productivity impact**.
- 95% of enterprise AI pilots fail.

See [AI Critical Perspectives](ai-critical-perspectives.md), [AI Impact On Software Engineering](ai-impact-on-software-engineering.md). Cherny's numbers are reported from inside Anthropic, working with the most capable agentic-coding harness in production — not necessarily generalizable.

## Related

- [Claude Code](claude-code.md)
- [Anthropic](anthropic.md)
- [Agentic Coding](agentic-coding.md)
- [AI And Software Engineering Jobs](ai-and-software-engineering-jobs.md)
- [AI Impact On Software Engineering](ai-impact-on-software-engineering.md)
