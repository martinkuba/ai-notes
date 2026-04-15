---
id: "01kp6zz80th59zbapbc67hm2dx"
title: "Agentic Engineering"
author: "Addy Osmani"
source_url: "https://addyosmani.com/blog/agentic-engineering/"
category: "article"
tags: [ai, work]
saved_at: "2026-04-14T21:57:13.369000+00:00"
summarized_at: "2026-04-15T20:22:19Z"
---

# Agentic Engineering

**Original source:** [Agentic Engineering](https://addyosmani.com/blog/agentic-engineering/)
**Author:** Addy Osmani

## Summary

Addy Osmani argues that the term "vibe coding" — coined by Andrej Karpathy to describe prompt-and-accept AI programming without code review — has become a "suitcase term" conflating reckless prototyping with disciplined, AI-assisted professional workflows. While vibe coding is genuinely useful for MVPs, personal scripts, learning, and creative brainstorming, its failure modes are well-documented: code that demos well but can't be modified, scaled, or secured because nobody understands it.

Osmani endorses the term "agentic engineering," also suggested by Karpathy, as the professional alternative. The term describes a workflow where engineers orchestrate AI agents that handle implementation while the human acts as architect, reviewer, and decision-maker. Unlike "vibe engineering" (proposed by Simon Willison), "agentic engineering" avoids the casual connotations of "vibe" and is professionally legible — suitable for job descriptions, team practices, and executive conversations.

In practice, agentic engineering requires starting with a plan or spec before prompting, reviewing every diff with the same rigor as a human PR, testing relentlessly (the single biggest differentiator from vibe coding), and maintaining ownership of the codebase through documentation, version control, and CI. Osmani highlights an uncomfortable truth: this approach disproportionately benefits senior engineers who already have deep fundamentals, while juniors risk skill atrophy by producing code they can't debug or reason about. The path forward requires honest terminology, better evaluation frameworks for AI-assisted workflows, and continued investment in engineering fundamentals.

## Main Ideas

- "Vibe coding" has become an overloaded term that conflates reckless prototyping with disciplined AI-assisted engineering, causing confusion and damage.
- "Agentic engineering" is proposed as the preferred term for professional AI-assisted development where agents implement under human oversight.
- The workflow requires upfront planning, rigorous code review, comprehensive testing, and full codebase ownership — AI accelerates the work but doesn't replace engineering discipline.
- AI-assisted development actually rewards good engineering practices more than traditional coding: better specs yield better output, more tests enable more confident delegation.
- Senior engineers benefit disproportionately because they can efficiently review and correct AI output, while juniors risk skill atrophy from producing code without understanding it.
- The industry needs honest terminology, better evaluation frameworks, and increased investment in fundamentals as AI handles more implementation.

## Key Quotes

- "Vibe coding means going with the vibes and not reviewing the code. That's the defining characteristic."
- "AI-assisted development actually rewards good engineering practices more than traditional coding does. The better your specs, the better the AI's output."
- "Agentic engineering isn't easier than traditional engineering — it's a different kind of hard. You're trading typing time for review time, implementation effort for orchestration skill, writing code for reading and evaluating code."
