---
id: "01ke7q08kjajnkafs3hj7yehzt"
title: "Claude Code: Best practices for agentic coding"
author: "anthropic.com"
source_url: "https://www.anthropic.com/engineering/claude-code-best-practices"
category: "article"
tags: [ai, work]
saved_at: "2026-01-05T18:34:09.393000+00:00"
summarized_at: "2026-04-15T19:39:03Z"
---

# Claude Code: Best practices for agentic coding

**Original source:** [Claude Code: Best practices for agentic coding](https://www.anthropic.com/engineering/claude-code-best-practices)
**Author:** anthropic.com

## Summary

Anthropic's official guide to Claude Code best practices covers setup, tooling, workflows, and optimization techniques drawn from both internal teams and the broader user community. Claude Code is intentionally low-level and unopinionated, providing close to raw model access. The foundation of effective use is customization: creating CLAUDE.md files to document commands, code style, and project conventions; tuning tool allowlists; and integrating with GitHub CLI. CLAUDE.md files can be placed at repo root, in parent directories, child directories, or the home folder, and should be iteratively refined like any frequently used prompt.

The guide outlines several proven workflows. "Explore, plan, code, commit" is the most versatile: have Claude research relevant files (using subagents for complex problems), make a plan using extended thinking mode ("think" through "ultrathink"), implement the solution, then commit and create a PR. Test-driven development works especially well—write tests first, confirm they fail, then have Claude iterate on implementation until all tests pass. Visual workflows involve giving Claude screenshots and design mocks to implement and iterate against. For complex tasks, using Markdown checklists as scratchpads helps Claude track progress.

Multi-Claude workflows offer additional power: one Claude writes code while another reviews it, or multiple checkouts of the same repo allow parallel work on different tasks. Git worktrees provide a lighter-weight alternative for this. Headless mode enables CI integrations like automated issue triage and subjective code reviews. The key optimization insight is specificity—Claude's success rate improves significantly with detailed instructions, explicit file references, and clear iteration targets.

## Main Ideas

- CLAUDE.md files are the primary customization mechanism—place them at multiple directory levels and refine them iteratively
- The "explore, plan, code, commit" workflow with extended thinking produces the best results for complex problems
- Test-driven development is especially powerful with agentic coding—Claude iterates until all tests pass
- Use triggers like "think," "think hard," "think harder," and "ultrathink" for progressively deeper reasoning
- Multi-Claude workflows (separate reviewer, parallel git checkouts, git worktrees) improve quality and throughput
- Headless mode (`claude -p`) enables CI/CD integrations for issue triage, code review, and automated migrations
- Specificity in prompts dramatically improves outcomes—compare "add tests" vs detailed instructions with patterns and constraints
