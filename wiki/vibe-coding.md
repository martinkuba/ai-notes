---
tags: [coding, agents, methodology, culture]
---

# Vibe Coding

Term coined by [Andrej Karpathy](andrej-karpathy.md) for prompt-and-accept AI programming — generating code by describing intent to an agent and accepting the output without rigorous review. Has become both a pop-culture handle for AI-assisted coding generally and a slur for sloppy versions of it.

## Origin and Meaning

Karpathy's framing: "I just see the stuff, say the stuff, run the stuff, and copy-paste the stuff, and it mostly works." A loose, fast, conversational mode. The term captured something real about how the practice felt — flow-state coding without traditional review discipline.

See source: [How I Learned To Stop Worrying And Love Vibe Coding](../summaries/how-i-learned-to-stop-worrying-and-love-vibe-coding.md).

## The Overloaded Term

[Addy Osmani](addy-osmani.md) argues "vibe coding" has become overloaded: it now conflates reckless prototyping with disciplined AI-assisted work, papering over an important distinction. The casual usage flattens what should be two different practices.

## Vibe Coding vs. Agentic Engineering

The professional alternative is **agentic engineering** (term endorsed by both Karpathy and Osmani):

| Vibe Coding | Agentic Engineering |
|---|---|
| Prompt-and-accept | Spec-driven, plan-then-execute |
| No code review | Rigorous review of every diff |
| Disposable prototypes | Full codebase ownership |
| Skill-flat (anyone can do it) | Disproportionately rewards seniors |

See [Agentic Coding](agentic-coding.md), source: [Agentic Engineering](../summaries/agentic-engineering.md).

## The Vibe Specs Corrective

A practical fix that keeps the speed but adds discipline: have the AI write the spec first, then implement from it. The human validates the *plan* before the *execution*, catching misunderstandings early. See [Spec Driven Development](spec-driven-development.md), source: [Vibe Specs Vibe Coding That Actually Works](../summaries/vibe-specs-vibe-coding-that-actually-works.md).

## Risks

- **Slopacolypse** — Karpathy's term for the coming flood of low-quality AI-generated code that vibe coding produces at scale. See [Andrej Karpathy](andrej-karpathy.md), [AI Impact On Software Engineering](ai-impact-on-software-engineering.md).
- **Comprehension debt** — Code generated faster than humans can evaluate it; the codebase looks clean but no one understands the design decisions. See [Addy Osmani](addy-osmani.md).
- **Cognitive surrender** — The psychological mechanism behind prompt-and-accept: the engineer's judgment is replaced by the AI's output without the engineer noticing. Surface signals (green tests, clean diffs) generate borrowed confidence. Each unexamined merge is a small cognitive debt payment. See [Addy Osmani](addy-osmani.md), source: [Cognitive Surrender](../summaries/cognitive-surrender.md).
- **Skill atrophy** — Junior engineers who only vibe-code never develop the review and judgment skills that distinguish seniors.

## Related

- [Andrej Karpathy](andrej-karpathy.md)
- [Addy Osmani](addy-osmani.md)
- [Agentic Coding](agentic-coding.md)
- [Spec Driven Development](spec-driven-development.md)
- [AI Impact On Software Engineering](ai-impact-on-software-engineering.md)
