---
tags: [technical, llm, architecture, reasoning]
---

# How LLMs Work

Technical foundations of large language models — from token prediction to emergent reasoning capabilities.

## Core Mechanism: Token Prediction

Stephen Wolfram's detailed explanation: LLMs predict the next token in a sequence based on probability distributions learned from training data. This deceptively simple mechanism, scaled to billions of parameters, produces apparently intelligent behavior.

Key insight: the model doesn't "understand" in a human sense — it builds a compressed statistical model of language that captures structure, facts, and reasoning patterns.

See source: [What Is Chatgpt Doing And Why Does It Work](../sources/what-is-chatgpt-doing-and-why-does-it-work.md)

## Reasoning Models

A fundamental shift from pure token prediction to structured reasoning:

### OpenAI o1 / Strawberry
Not a chat model — a reasoning model designed for complex problem-solving. Represents a qualitative change in what LLMs can do, moving beyond fluency to actual logical deduction.

See sources: [O1 Isnt A Chat Model](../sources/o1-isnt-a-chat-model.md), [Something New On Openai S Strawberry And Reasoning](../sources/something-new-on-openai-s-strawberry-and-reasoning.md)

### Extended Thinking
Claude's extended thinking capability allows the model to "think" through complex problems step-by-step before responding, producing more accurate and nuanced answers for difficult tasks.

See source: [Claude S Extended Thinking](../sources/claude-s-extended-thinking.md)

## Limitations

### Hallucinations and Plausibility
LLMs can produce confident, plausible-sounding output that is factually wrong. Simon Willison demonstrated this by showing ChatGPT will write "thinly disguised horoscopes" — unfounded but authoritative-sounding analysis.

See source: [Chatgpt Will Happily Write You A Thinly Disguised Horoscope](../sources/chatgpt-will-happily-write-you-a-thinly-disguised-horoscope.md)

### The Comprehension Gap
Models that generate code may not "understand" it the way humans do, creating challenges for verification and debugging.

## Model Landscape

A guide to current frontier models and their comparative strengths:
- Claude Opus 4.6 — Strong reasoning, extended thinking, agentic coding
- GPT-5.2 Thinking — Reasoning-focused
- Gemini 3 Pro — Multimodal, large context

See source: [A Guide To Which AI To Use In The Agentic Era](../sources/a-guide-to-which-ai-to-use-in-the-agentic-era.md)

## Related

- [Prompt Engineering](prompt-engineering.md)
- [Scaling And Compute](scaling-and-compute.md)
- [Reasoning Models](reasoning-models.md)
- [AGI Timelines](agi-timelines.md)
