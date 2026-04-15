---
id: "01kg0dkzpzb4qys7vhkkenfeer"
title: "A Software Library with No Code"
author: "Drew Breunig"
source_url: "https://www.dbreunig.com/2026/01/08/a-software-library-with-no-code.html"
category: "article"
tags: [ai, work]
saved_at: "2026-01-27T19:06:52.511000+00:00"
summarized_at: "2026-04-15T19:35:33Z"
---

# A Software Library with No Code

**Original source:** [A Software Library with No Code](https://www.dbreunig.com/2026/01/08/a-software-library-with-no-code.html)
**Author:** Drew Breunig

## Summary

Drew Breunig introduces "whenwords," an experimental software library that contains no actual code -- only a specification (SPEC.md), a set of language-agnostic test cases (tests.yaml), and installation instructions that amount to a prompt for an AI coding agent. The library provides five functions for converting between timestamps and human-readable strings (e.g., "3 hours ago"). Users paste a simple prompt into Claude, Codex, or Cursor, specify their language and location, and the AI implements the library from the spec. It works across Ruby, Python, Rust, Elixir, Swift, PHP, Bash, and even Excel formulas.

The experiment serves as a tangible thought experiment about what software engineering looks like when coding is effectively free. Breunig notes that recent advances in coding agents -- particularly Opus 4.5 with Claude Code -- have crossed a threshold where tightly specified code can be implemented reliably in one shot across any language. This raises the question of whether simple utility libraries still need language-specific implementations, or whether a single well-defined spec could replace them all.

However, Breunig identifies five key areas where traditional code libraries remain essential: when performance matters and needs careful optimization; when testing becomes complicated across many languages and AI agents; when bug support requires reproducible issues against a consistent codebase; when ongoing updates and security patches are needed; and when community and interoperability are important. He concludes that spec-only libraries may work for simple, implement-and-forget utilities, but for foundational software that people build on, the community, maintenance, and crystallized knowledge embodied in actual code remain irreplaceable.

## Main Ideas

- A "spec-only" library with no code -- just specifications and tests -- can be implemented by AI coding agents in any language on demand.
- Modern coding agents (particularly Claude Code with Opus 4.5) can reliably implement tightly specified code in one shot across multiple languages.
- Spec-only approaches may work for simple utility libraries but break down when performance optimization, complex testing, bug reproduction, ongoing updates, or community support are needed.
- The experiment raises fundamental questions about what software engineering looks like when the cost of writing code approaches zero.
- Open-source community value goes beyond code -- it includes bug discovery, maintenance, security updates, and the culture that sustains reliable foundations.

## Key Quotes

- "The code we rely on is not just an instantiation of a spec, but the product of people and culture that crystallize around a goal. It's the magic of open source; why it works and why I love it."
- "Models and their harnesses crossed a threshold in Q4, and everyone I know using Opus 4.5 has felt it."
