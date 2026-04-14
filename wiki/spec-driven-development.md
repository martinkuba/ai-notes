---
tags: [coding, methodology, agents, prompt-engineering]
---

# Spec-Driven Development

An emerging methodology where detailed specifications are written *before* engaging AI coding agents. The spec becomes the primary artifact — more important than the code itself, which can be regenerated cheaply.

## Why Specs Matter for Agents

AI agents need clear, unambiguous instructions to produce good output. Without specs, [[agentic-coding]] degrades into "vibe coding" chaos — superficially working code that accumulates hidden defects. The spec bridges human intent and agent execution.

## Vibe Specs

A practical technique: have the AI write the spec first, then implement from it. This creates a feedback loop where the human validates the *plan* before the *execution*, catching misunderstandings early.

See source: [[sources/vibe-specs-vibe-coding-that-actually-works]]

## Anatomy of a Good Spec

Key elements identified across sources:
- **Context** — Why does this exist? What problem does it solve?
- **Requirements** — What must it do? Explicit acceptance criteria.
- **Constraints** — What must it *not* do? Boundaries and limitations.
- **Examples** — Concrete input/output pairs.
- **Edge cases** — What happens at the boundaries?

See sources: [[sources/how-to-write-a-good-spec-for-ai-agents]], [[sources/the-anatomy-of-a-good-spec-in-the-age-of-ai]]

## Spec-Only Libraries

A radical extension: software libraries distributed as specs + tests with *no implementation code*. The consuming agent generates the implementation in whatever language is needed. Raises questions about when specifications become more valuable than code.

See source: [[sources/a-software-library-with-no-code]]

## Related

- [[agentic-coding]]
- [[prompt-engineering]]
