---
id: "01ke68trcyrytyynpndcqt6xex"
title: "Claude's extended thinking"
author: "anthropic.com"
source_url: "https://www.anthropic.com/research/visible-extended-thinking"
category: "article"
tags: [ai]
saved_at: "2025-02-28T23:31:16+00:00"
summarized_at: "2026-04-15T19:39:03Z"
---

# Claude's extended thinking

**Original source:** [Claude's extended thinking](https://www.anthropic.com/research/visible-extended-thinking)
**Author:** anthropic.com

## Summary

Anthropic introduced extended thinking mode with Claude 3.7 Sonnet, allowing the model to allocate more cognitive effort to harder problems—analogous to how humans apply more mental stamina to complex tasks versus simple ones. This isn't a switch to a different model; it's the same model giving itself more time and effort. Developers can set a "thinking budget" to control how long Claude spends on a problem, and the thought process is made visible in raw form as a research preview.

Making the thought process visible has benefits (trust, alignment research, and fascination—researchers note how similar Claude's reasoning is to human problem-solving) but also significant concerns. The thinking content is less polished and more detached than normal output since character training wasn't applied to it. "Faithfulness" is an open question—the visible thoughts may not truly represent the model's internal processes, meaning monitoring thoughts can't be relied upon for safety arguments. There's also risk that malicious actors could use visible thinking to craft better jailbreaks, or that models might learn to hide certain thoughts if they know they're being observed.

The article details impressive benchmark results. Claude 3.7 Sonnet's "action scaling" enables sustained agentic work—it progressed much further in Pokémon Red than prior versions, defeating three Gym Leaders. Serial test-time compute (extended thinking) improves math performance logarithmically with thinking tokens. Parallel test-time compute—sampling multiple independent thought processes and selecting the best—achieved 84.8% on GPQA (96.5% on physics) using 256 independent samples. Safety evaluations confirmed ASL-2 remains appropriate, though some CBRN "uplift" was observed with critical failures still preventing success. New defenses against prompt injection in computer use now prevent attacks 88% of the time, up from 74%.

## Main Ideas

- Extended thinking lets Claude apply variable cognitive effort—not a different model, but the same one thinking longer
- Visible thought process aids trust and alignment research but raises faithfulness and security concerns
- Claude 3.7 Sonnet's agentic capabilities showed dramatic improvement in sustained tasks like playing Pokémon Red
- Serial test-time compute improves accuracy logarithmically with thinking tokens on math problems
- Parallel test-time compute (256 samples with scoring model) achieved 84.8% on GPQA, including 96.5% on physics
- Prompt injection defenses for computer use improved from 74% to 88% prevention rate
- Character training was deliberately not applied to the thought process to give Claude maximum reasoning freedom
