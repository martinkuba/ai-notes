---
id: "01knyvnzmfx56z2cn5ah7rmv4p"
title: "GitHub - forrestchang/andrej-karpathy-skills"
author: "https://github.com/forrestchang/"
source_url: "https://github.com/forrestchang/andrej-karpathy-skills"
category: "article"
tags: [ai, work]
saved_at: "2026-04-11T18:08:20.111000+00:00"
summarized_at: "2026-04-15T19:46:34Z"
---

# Karpathy-Inspired Claude Code Guidelines

**Original source:** [GitHub - forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills)

## Summary

This GitHub repository provides a single CLAUDE.md file designed to improve Claude Code's behavior when writing and editing code. The guidelines are derived from Andrej Karpathy's observations about common LLM coding pitfalls, specifically that models make wrong assumptions without checking, overcomplicate code and APIs, bloat abstractions, and sometimes modify comments or code they do not understand as side effects of unrelated tasks.

The solution is organized around four principles. "Think Before Coding" addresses the tendency to silently assume rather than surface confusion, tradeoffs, or ambiguity. "Simplicity First" combats overengineering by enforcing minimum viable code with no speculative features, unnecessary abstractions, or error handling for impossible scenarios. "Surgical Changes" ensures the model only touches what is necessary, matching existing style and not performing drive-by refactoring. "Goal-Driven Execution" transforms imperative tasks into verifiable goals with success criteria, leveraging LLMs' strength at looping until specific conditions are met.

The repository includes installation instructions for adding the guidelines to a CLAUDE.md file or a skills directory. It notes that these guidelines intentionally bias toward caution over speed, and are designed for non-trivial work rather than simple one-liner changes. Success indicators include fewer unnecessary changes in diffs, simpler first-pass code, clarifying questions before implementation, and clean minimal PRs.

## Main Ideas

- LLMs commonly make silent assumptions, overcomplicate code, bloat abstractions, and make unintended side-effect changes when coding.
- Four principles address these pitfalls: Think Before Coding, Simplicity First, Surgical Changes, and Goal-Driven Execution.
- The "Goal-Driven Execution" principle leverages a key LLM strength: they are exceptionally good at looping until they meet specific, declarative success criteria.
- Every changed line should trace directly to the user's request; drive-by improvements and refactoring of unrelated code should be avoided.
- The guidelines bias toward caution over speed and are meant for non-trivial work, not simple fixes.
- These principles are designed to be merged with project-specific CLAUDE.md instructions.

## Key Quotes

- "The models make wrong assumptions on your behalf and just run along with them without checking. They don't manage their confusion, don't seek clarifications, don't surface inconsistencies, don't present tradeoffs, don't push back when they should." -- Andrej Karpathy
- "LLMs are exceptionally good at looping until they meet specific goals... Don't tell it what to do, give it success criteria and watch it go." -- Andrej Karpathy
