---
id: "01kg2sf9j1ex2v009kmare3d92"
title: "Vibe Specs: Vibe Coding That Actually Works"
author: "Luke Bechtel"
source_url: "https://lukebechtel.com/blog/vibe-speccing"
category: "article"
tags: [ai, work]
saved_at: "2026-01-28T17:12:30.529000+00:00"
summarized_at: "2026-04-15T20:00:38Z"
---

# Vibe Specs: Vibe Coding That Actually Works

**Original source:** [Vibe Specs: Vibe Coding That Actually Works](https://lukebechtel.com/blog/vibe-speccing)
**Author:** Luke Bechtel

## Summary

Luke Bechtel proposes "Vibe Specs" — a simple but powerful pattern for AI-assisted development where you have the LLM write a specification document before writing any code. The core insight is that the real reason AI-generated software often disappoints isn't bad prompts or weak models, but that the AI doesn't understand the problem context. Rather than investing in elaborate prompting techniques, the fix is to have the LLM interview you, challenge your assumptions, and produce a structured spec that captures objectives, success criteria, constraints, scope boundaries, and completion criteria.

The workflow is straightforward: add a cursor rule that's always attached, and the AI will automatically guide you through spec creation before generating code. The spec becomes a stable, git-trackable document that persists beyond ephemeral chat sessions, can be handed to colleagues or fresh context windows, and prevents the common problems of chat drift, feature creep, solo coding silos, lost context, and token waste. Bechtel draws on the concept of "context engineering" (coined by Shopify's Tobi Lütke and endorsed by Andrej Karpathy) — the art of providing exactly the right information for the LLM to perform well, neither too little nor too much.

Bechtel reports dramatic personal results: spending 5 minutes on a spec during a coding interview let him finish 20 minutes early with a perfect implementation, and he estimates a 60% reduction in feature development time overall. He argues that the pattern works because it mirrors how we delegate work to humans — through clear requirements documents — and aligns with how OpenAI's own Deep Research product works (asking clarifying questions before proceeding). The article concludes that in the age of AI-assisted development, every developer becomes their own product manager, and the hardest part is no longer writing code but knowing what code to write.

## Main Ideas

- Have the LLM write a specification before code — this is the single most impactful pattern for AI-assisted development
- The real problem with AI-generated code is inadequate context, not bad prompting
- "Context engineering" (providing the right information) matters more than "prompt engineering"
- Specs are stable, git-trackable documents that solve chat drift, feature creep, and lost context
- The LLM interviews you and writes the spec; your job is to critique and clarify
- The author reports ~60% reduction in feature development time with spec-first approach
- In AI-assisted development, every developer becomes their own product manager

## Key Quotes

- "It doesn't matter how quickly you can create something if it's useless."
- "Give the AI a crisp spec, and you get crisp, consistent output; give it a vibe, and you get a vibe back."
- "The magic isn't in avoiding the LLM until you have requirements. The magic is in using the LLM to help you discover what your requirements actually are."
