---
id: "01kj6a6sam8natr0jdb5ne1we1"
title: "How I Learned to Stop Worrying and Love Vibe Coding"
author: "SANS Cloud Security"
source_url: "https://www.youtube.com/watch?v=XaosRsgGSX8&t=3s"
category: "video"
tags: [ai, work]
saved_at: "2026-02-23T22:34:04.500000+00:00"
summarized_at: "2026-04-15T19:46:34Z"
---

# How I Learned to Stop Worrying and Love Vibe Coding

**Original source:** [How I Learned to Stop Worrying and Love Vibe Coding](https://www.youtube.com/watch?v=XaosRsgGSX8&t=3s)
**Author:** SANS Cloud Security

## Summary

John Zola, founder of Zenible and CNCF ambassador, presents a practical framework for adopting AI coding tools safely in production environments. He begins by acknowledging the risks of "vibe coding" -- the practice of letting AI generate code without closely reading it, coined by Andrej Karpathy -- and uses humorous AI training videos (walking robots, bowling, table tennis) to illustrate how AI tools optimize for results in unexpected ways that may look correct on the surface but break under changing conditions.

Zola's core argument is that vibe coding can work reliably if you build proper foundations and guardrails. He outlines a maturity model: first, build a baseline (repository structure, file conventions, testing tools, CI/CD pipelines, security scans) so the AI has patterns to follow rather than starting from an empty folder. He demos an open-source project called "AI Native Python" that scaffolds this entire foundation automatically by answering 11 questions, producing starter code, linters, credential checks, GitHub Actions, automatic dependency updates, and 100% test coverage templates. Second, adopt specification-driven development -- a three-step process where you have the AI do research first, then build specifications (using formats like Gherkin or EARS), and only then implement code. Each step involves human review. Third, implement deterministic guardrails using policy-as-code tools (Conftest, Goss, InSpec) that run automatically on every commit, ensuring AI-generated code never ships with hardcoded credentials, vulnerable configurations, or policy violations.

The talk emphasizes the distinction between non-deterministic guardrails (AI peer review, context engineering) and deterministic guardrails (policy-as-code checks that produce the same result every time). Zola argues the right approach combines both, and credits the shift from "prompt engineering" to "context engineering" as a key conceptual advance for working with AI tools effectively.

## Main Ideas

- Vibe coding (generating code via AI without reading it line-by-line) is risky if done without guardrails, but can be made reliable with proper foundations.
- Always build a baseline first: repository structure, testing frameworks, CI/CD pipelines, security scans, and instruction files give AI patterns to follow rather than inventing from scratch.
- Specification-driven development (research, then specifications, then implementation) with human review at each step dramatically improves AI code quality.
- Gherkin and EARS are structured formats for writing specifications that force AI to think more critically and include all required information.
- Deterministic guardrails (policy-as-code via Conftest, Goss, InSpec) should run on every commit to catch issues like hardcoded credentials, vulnerable configurations, and compliance violations.
- The shift from "prompt engineering" to "context engineering" -- feeding AI comprehensive information about what is and is not allowed -- is key to getting reliable outputs.
- The process of writing specifications for AI also benefits human collaboration by documenting institutional knowledge that was previously only in people's heads.
