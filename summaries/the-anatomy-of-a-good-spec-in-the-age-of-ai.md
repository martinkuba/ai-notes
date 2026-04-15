---
id: "01kjngfsqsnyzpr0yesqwmj750"
title: "The Anatomy of a Good Spec in the Age of AI"
author: "Kinde"
source_url: "https://kinde.com/learn/ai-for-software-engineering/best-practice/the-anatomy-of-a-good-spec-in-the-age-of-ai/"
category: "article"
tags: [ai, work]
saved_at: "2026-03-01T20:12:27.770000+00:00"
summarized_at: "2026-04-15T19:53:49Z"
---

# The Anatomy of a Good Spec in the Age of AI

**Original source:** [The Anatomy of a Good Spec in the Age of AI](https://kinde.com/learn/ai-for-software-engineering/best-practice/the-anatomy-of-a-good-spec-in-the-age-of-ai/)
**Author:** Kinde

## Summary

This article argues that software specifications must evolve to serve a hybrid audience of human engineers and AI development tools. While the core purpose of a spec remains creating shared understanding of what needs to be built, the rise of AI code generators, automated testing, and AI assistants means the spec is no longer just a guide -- it's becoming a direct input for machine processes. The fundamental principle is that AI tools cannot infer intent, so specs must be ruthlessly literal and unambiguous.

The article outlines key elements of an AI-ready spec: precise quantified language instead of subjective terms (e.g., "under 200ms for 99% of requests" rather than "fast"), defined glossaries for domain-specific terms, formal notations like Gherkin for complex logic, and consistent hierarchical structure (overview, user stories, functional requirements, non-functional requirements, acceptance criteria). Edge cases deserve particular attention since AI struggles without explicit guidance -- the spec should enumerate unusual scenarios like oversized files, unsupported types, or dropped connections. Acceptance criteria should be binary, testable, and focused, serving as direct inputs for AI-generated test suites. The article challenges the misconception that AI can "figure out" vague specs, emphasizing that output quality is directly proportional to input quality. It recommends treating specs like code: stored in version control and requiring reviews for changes.

## Main Ideas

- Software specs must now serve both human engineers and AI tools as a direct machine-readable input
- AI cannot infer intent, so specs must use precise, quantified language and avoid subjective terms
- A well-structured spec follows a consistent hierarchy: overview, user stories, functional/non-functional requirements, acceptance criteria
- Edge cases must be explicitly enumerated since AI struggles with unstated unusual scenarios
- Acceptance criteria should be binary, testable, and focused -- they directly generate AI-powered test suites
- "Garbage in, garbage out" still applies: AI output quality is proportional to spec quality
- Specs should be version-controlled and reviewed like code to maintain accuracy as products evolve
