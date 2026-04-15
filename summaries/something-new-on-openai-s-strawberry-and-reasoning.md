---
id: "01ke68twbg0c7qns9mfp3mfep0"
title: "Something New: On OpenAI's \"Strawberry\" and Reasoning"
author: "Ethan Mollick"
source_url: "https://www.oneusefulthing.org/p/something-new-on-openais-strawberry"
category: "article"
tags: [ai, newsletter]
saved_at: "2026-02-08T20:35:28.109000+00:00"
summarized_at: "2026-04-15T19:53:49Z"
---

# Something New: On OpenAI's "Strawberry" and Reasoning

**Original source:** [Something New: On OpenAI's "Strawberry" and Reasoning](https://www.oneusefulthing.org/p/something-new-on-openais-strawberry)
**Author:** Ethan Mollick

## Summary

Ethan Mollick provides an early hands-on assessment of OpenAI's o1-preview model (codenamed "Strawberry"), which introduces a reasoning/planning step before generating answers. The model "thinks through" problems before solving them, enabling it to tackle complex tasks requiring iteration and planning -- such as novel math and science questions -- that previous LLMs struggled with. Notably, o1-preview can beat human PhD experts on extremely hard physics problems.

Mollick demonstrates the model's capabilities and limitations using a crossword puzzle, which is particularly challenging for LLMs because it requires iterative solving where answers affect each other. While Claude (without planning) commits to an early wrong answer and gets stuck, o1-preview spends 108 seconds "thinking," trying and rejecting multiple approaches. The model gets impressively close but still fails on a tricky cultural reference (Samsung Galaxy "APPS" vs. astronomical galaxy clusters). When given a single hint, it solves the entire puzzle correctly. Mollick also shows o1-preview generating complete code for a teaching simulator from a research paper with minimal prompting. However, he notes the model isn't universally better -- Claude remains superior for writing style. The deeper implication is a paradigm shift: as AI gains planning capabilities and moves toward autonomous agency, the human role as collaborative partner feels diminished, raising questions about how humans stay meaningfully in the loop.

## Main Ideas

- o1-preview introduces a "think before answering" step that enables iterative reasoning and planning
- The model excels at complex problems requiring multi-step iteration (math, science, planning) but isn't a better writer
- Crossword puzzles illustrate both the breakthrough (iterative solving) and limitations (cultural knowledge gaps, hallucinations)
- Planning represents a form of agency where AI arrives at conclusions independently, diminishing the human's role as a co-pilot
- As AI systems gain autonomous capabilities, the key challenge becomes: how do humans evolve their collaboration with AI?
- The model is still built on GPT-4o's underlying capabilities, meaning it inherits that model's knowledge limitations

## Key Quotes

- "Using o1-preview means confronting a paradigm change in AI. Planning is a form of agency, where the AI arrives at conclusions about how to solve a problem on its own, without our help."
- "How do we evolve our collaboration with AI as it evolves? That is a problem that o1-preview can not yet solve."
