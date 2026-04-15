---
id: "01kjngddgbaxzvb1v2erxmn051"
title: "How to Write a Good Spec for AI Agents"
author: "Addy Osmani"
source_url: "https://www.oreilly.com/radar/how-to-write-a-good-spec-for-ai-agents/"
category: "article"
tags: [ai, work]
saved_at: "2026-03-01T20:11:09.707000+00:00"
summarized_at: "2026-04-15T19:46:34Z"
---

# How to Write a Good Spec for AI Agents

**Original source:** [How to Write a Good Spec for AI Agents](https://www.oreilly.com/radar/how-to-write-a-good-spec-for-ai-agents/)
**Author:** Addy Osmani

## Summary

Osmani presents a comprehensive framework for writing specifications that guide AI coding agents effectively. The core insight is that simply throwing a massive spec at an agent does not work due to context window limits and the model's finite attention budget. Instead, developers need to write "smart specs" that guide the agent clearly, stay within practical context sizes, and evolve with the project. The article distills five principles drawn from experience with tools like Claude Code and Gemini CLI.

The five principles are: (1) Start with a high-level vision and let the AI draft the details, using plan mode to enforce a planning-first workflow. (2) Structure the spec like a professional PRD or SRS covering six core areas identified by GitHub's analysis of 2,500+ agent configuration files: commands, testing, project structure, code style, git workflow, and boundaries. (3) Break tasks into modular prompts rather than one monolithic prompt, using techniques like hierarchical summaries, subagents, and parallel orchestration to manage large specs. (4) Build in self-checks, constraints, and human expertise through three-tier boundaries (always do, ask first, never do), self-verification prompts, and conformance testing. (5) Test, iterate, and evolve the spec continuously using automated tests, version control, and context management tools.

The article also identifies key antipatterns: vague prompts, overlong contexts without summarization, skipping human review, conflating vibe coding with production engineering, and ignoring the "lethal trifecta" of speed, nondeterminism, and cost. Osmani emphasizes that the spec is a living document and a management tool for an iterative cycle of instructing, verifying, and refining, drawing on Simon Willison's comparison of AI agents to "a very weird form of management."

## Main Ideas

- Write smart specs that guide the AI clearly and stay within practical context sizes, rather than dumping everything into one massive prompt.
- Use a planning-first workflow: draft a high-level vision, let the AI expand it, review and refine before any code generation.
- Structure specs around six core areas: commands, testing, project structure, code style, git workflow, and boundaries.
- Use three-tier boundaries (always/ask first/never) rather than flat lists of rules to give agents clearer guidance.
- Break work into modular prompts with focused context; use spec summaries and subagents for large projects.
- The "curse of instructions" means more directives in a single prompt leads to worse adherence to each one.
- Treat the spec as a living, version-controlled document that evolves through continuous testing and iteration.

## Key Quotes

- "Most agent files fail because they're too vague."
- "Never commit secrets" was the single most common helpful constraint found in GitHub's study of 2,500+ agent configuration files.
- "Getting good results out of a coding agent feels uncomfortably close to managing a human intern." -- Simon Willison
