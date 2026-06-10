---
tags: [software-engineering, cognitive-debt, ai-risks, teams]
---

# Cognitive Debt

The concept of **cognitive debt**, introduced by Margaret-Anne Storey, describes the erosion of shared understanding among developers about what a system does, how it works, and how to modify it. Unlike [technical debt](ai-impact-on-software-engineering.md), which lives in code, cognitive debt lives in people — in the mental models (or "theories") that developers collectively hold about a system.

> "Technical debt lives in the code. Cognitive debt lives in people." — Margaret Storey

Peter Naur's notion of a "program theory" is central: a program exists not just as source code but as a theory in the minds of its developers capturing what it does, how intentions were implemented, and how it can be changed. When that shared theory fragments, the system becomes unmaintainable regardless of code quality.

## How AI Amplifies Cognitive Debt

Generative and agentic AI accelerate development velocity, but velocity can outpace understanding. Teams ship faster with AI assistance, yet developers report:

- Losing confidence in making changes
- Heavier review burdens that don't keep pace with output
- Debugging friction and slower onboarding
- Systems that feel like black boxes — even clean, test-passing ones

Cognitive debt doesn't announce itself through failing builds or subtle bugs. It shows up as a **silent loss of shared theory**: no one can articulate the reasoning behind key design decisions or explain how components interconnect.

## Distinction from Comprehension Debt

[Comprehension debt](ai-impact-on-software-engineering.md#comprehension-debt) (Addy Osmani) and cognitive debt are closely related but operate at different levels:

| Concept | Level | Where it lives |
|---|---|---|
| Comprehension debt | Individual | Gap between code volume and what any one developer understands |
| Cognitive debt | Team | Gap between the system's evolving structure and the team's *shared* mental model |

Both are invisible to standard metrics (velocity, DORA, coverage). Both accelerate under AI-assisted development. Cognitive debt is the team-level manifestation: even if each individual understands their own piece, no one holds a coherent theory of the whole.

## Warning Signs

- Developers hesitate before making changes ("I don't want to touch that")
- Critical knowledge concentrates in a few individuals (tribal knowledge)
- System is perceived as a black box
- Review burden grows even as output grows
- Debugging takes disproportionately long
- Onboarding new developers slows

## Mitigation Strategies

**Slowing down to build understanding:**
- Require at least one human to fully understand each AI-generated change before merging
- Document the *reasoning* behind decisions, not just what changed
- Treat prototypes as disposable; rebuild understanding when graduating to production

**Rebuilding shared mental models:**
- Pair programming and code reviews as knowledge distribution, not just quality gates
- Tests that capture *intent*, not just behavior
- Continuously updated design documents that evolve with the architecture
- Using AI to make cognitive work *more* visible, not less

**Practices with proven track records:**
- Test-driven development (forces articulation of intent before implementation)
- Refactoring — Kent Beck's "make the hard change easy" as a sustainable velocity approach
- Retrospectives focused on shared understanding, not just process

## Community Response

After Storey published the initial article, the developer community confirmed the pattern from their own practice: teams that ship faster with AI often find that velocity outpaces understanding. The emerging consensus is that **shared understanding may become the bottleneck on performance** as AI removes most other bottlenecks.

Repaying cognitive debt requires maintaining a distributed theory of the system across multiple channels: people, documentation, tests, conversations, tooling, and AI agents. The challenge intensifies as AI lowers the cost of producing new code, making it easier for architecture to evolve faster than understanding can stabilize.

> "As AI reduces technical friction, shared understanding may become the bottleneck on performance." — Margaret Storey

## Sources

- [How Generative and Agentic AI Shift Concern from Technical Debt to Cognitive Debt](../summaries/how-generative-and-agentic-ai-shift-concern-from-technical.md) — Storey's introduction of the concept; the student team example; mitigation framework
- [What I'm Hearing About Cognitive Debt (So Far)](../summaries/what-im-hearing-about-cognitive-debt-so-far.md) — Community response; shared understanding as performance bottleneck; distributed theory of the system

## Related

- [AI Impact On Software Engineering](ai-impact-on-software-engineering.md) — Broader context; comprehension debt; agentic coding risks
- [Vibe Coding](vibe-coding.md) — Coding style that most aggressively trades understanding for velocity
- [Spec Driven Development](spec-driven-development.md) — Specs as one mechanism to externalize intent and slow accumulation of cognitive debt
- [Agentic Coding](agentic-coding.md) — The coding workflow in which cognitive debt accumulates fastest
