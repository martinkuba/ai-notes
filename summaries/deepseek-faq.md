---
id: "01ke68tt0x0n91sv4k5xbf9j1j"
title: "DeepSeek FAQ"
author: "Ben Thompson"
source_url: "https://stratechery.com/2025/deepseek-faq/"
category: "article"
tags: [ai, will]
saved_at: "2025-01-27T17:10:26+00:00"
summarized_at: "2026-04-15T19:39:03Z"
---

# DeepSeek FAQ

**Original source:** [DeepSeek FAQ](https://stratechery.com/2025/deepseek-faq/)
**Author:** Ben Thompson

## Summary

Ben Thompson provides an in-depth technical and strategic analysis of DeepSeek's AI models in FAQ format, written during the January 2025 market shock when DeepSeek's R1 model briefly crashed Nvidia's stock price. The technical story centers on DeepSeek-V3, which introduced innovations in mixture-of-experts (DeepSeekMoE) and multi-head latent attention (DeepSeekMLA) that dramatically reduced training costs and memory requirements. V3 was trained for just $5.576 million (final run only), a plausible figure given the architecture—671 billion parameters with only 37 billion active per token. Critically, all design decisions make sense only if you're constrained to H800 GPUs (legal under the chip ban), not H100s. DeepSeek's engineers even dropped to PTX assembly language to reprogram GPU processing units for cross-chip communications—an "insane level of optimization."

R1, the reasoning model, matched OpenAI's o1 in performance. But R1-Zero is the bigger scientific deal: it developed chain-of-thought reasoning through pure reinforcement learning without human feedback, a powerful affirmation of the "Bitter Lesson" that compute and data can teach AI to reason without explicit instruction. Thompson argues the market panic was largely driven by people's pre-existing assumptions being shattered—that China couldn't compete in AI software, that training costs would stay high, that OpenAI had special sauce. The reality is more nuanced: DeepSeek leads in efficiency but not overall capability (OpenAI has demonstrated the more powerful o3), and their open-weights approach aligns with CEO Liang Wenfeng's belief that moats come from team culture and cost structure, not closed models.

Thompson's strategic analysis is sharp: model commoditization helps Big Tech (cheaper inference benefits Microsoft, Amazon, Apple, Meta) but hurts pure-play AI labs, especially Anthropic, which lacks consumer traction and faces commoditization of its API business. The chip ban inadvertently drove DeepSeek's innovations, and Thompson argues the U.S. should respond by competing through innovation rather than denial.

## Main Ideas

- DeepSeek-V3 innovations (MoE, MLA, FP8 precision, PTX-level GPU optimization) dramatically reduced training costs to $5.576M for the final run
- R1-Zero developed chain-of-thought reasoning through pure reinforcement learning without human feedback—a major affirmation of the Bitter Lesson
- All DeepSeek optimizations make sense only under H800 constraints from the chip ban, which inadvertently drove innovation
- Model commoditization benefits Big Tech (cheaper inference) but threatens pure-play AI labs, especially Anthropic
- DeepSeek's open-weights strategy reflects a belief that long-term differentiation comes from superior cost structure, not closed models
- The U.S. should compete through innovation rather than defensive measures like expanding chip bans
- Distillation from leading models (likely including OpenAI and Anthropic) is assumed to be widespread and undermines the economics of frontier model training

## Key Quotes

- "The arrogance in this statement [OpenAI's 2019 GPT-2 release] is only surpassed by the futility: here we are six years later, and the entire world has access to the weights of a dramatically superior model."
- "If we choose to compete we can still win, and, if we do, we will have a Chinese company to thank."
