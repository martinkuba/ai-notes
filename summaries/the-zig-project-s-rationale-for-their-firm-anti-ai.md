---
id: "01ktsnjspgvq7t43zvvkn4rnp6"
title: "The Zig project's rationale for their firm anti-AI contribution policy"
author: "Simon Willison"
source_url: "https://simonwillison.net/2026/Apr/30/zig-anti-ai/"
category: "article"
tags: [ai]
saved_at: "2026-06-10T21:04:01.231000+00:00"
summarized_at: 2026-06-11T00:00:04Z
---

# The Zig project's rationale for their firm anti-AI contribution policy

**Original source:** [The Zig project's rationale for their firm anti-AI contribution policy](https://simonwillison.net/2026/Apr/30/zig-anti-ai/)
**Author:** Simon Willison

## Summary

The Zig programming language project maintains one of the strictest anti-LLM policies in open source, explicitly prohibiting LLM-generated contributions at all stages—issues, pull requests, and comments. This contrasts sharply with Bun, a Zig-based JavaScript runtime acquired by Anthropic in December 2025, which actively uses AI assistance and maintains its own fork of Zig specifically to deploy optimizations (achieving 4x compilation speedups) that the main Zig project would not accept due to the LLM contribution ban.

Zig Software Foundation VP Loris Cro articulates the reasoning as "contributor poker"—the insight that successful open source projects must invest in *developing contributors* as people, not just acquiring code. When maintainers review and accept LLM-assisted PRs, they invest review effort that does nothing to help grow confident, trustworthy long-term contributors. This philosophy values sustained team building over short-term code velocity, betting on contributors rather than the contents of individual pull requests.

The policy reflects a fundamental premise: LLM assistance breaks the contributor development loop. If a PR is primarily LLM-authored, maintainers reasonably ask why they should review it rather than generating their own solution with an LLM. This creates a coordination problem where AI-assisted contributions paradoxically become *less* valuable to a project oriented toward human contributor growth.

## Main Ideas

- **Contributor poker**: Open source success depends on growing a stable of trusted, prolific contributors over time—the primary goal of code review is developing people, not landing features.
- **LLM contributions break contributor development**: AI-assisted submissions provide no signal about the submitter's competence, judgment, or learning, so maintainer review effort yields no relationship-building ROI.
- **Strategic fork divergence**: Bun's acquisition by Anthropic allows it to maintain a Zig fork that includes AI-assisted optimizations the upstream project rejects, creating a performance gap but respecting Zig's values.
- **Coordination problem**: If LLM-assisted PRs become normalized, maintainers face a rational choice to generate solutions themselves rather than review third-party AI code.
- **Long-term vs. short-term trade-offs**: Zig explicitly trades code velocity for the compound returns of investing in human contributor relationships.

## Key Quotes

> "We try our best to help new contributors to get their work in, even if they need some help getting there. We don't do this just because it's the 'right' thing to do, but also because it's the smart thing to do."

> "The reason I call it 'contributor poker' is because, just like people say about the actual card game, 'you play the person, not the cards'. In contributor poker, you bet on the contributor, not on the contents of their first PR."

> "If a PR was mostly written by an LLM, why should a project maintainer spend time reviewing and discussing that PR as opposed to firing up their own LLM to solve the same problem?"
