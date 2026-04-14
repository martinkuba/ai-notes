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

See sources: [O1 Isnt A Chat Model](../sources/o1-isnt-a-chat-model-and-thats-the-point.md), [Something New On Openai S Strawberry And Reasoning](../sources/something-new-on-openai-s-strawberry-and-reasoning.md)

### Extended Thinking
Claude's extended thinking capability allows the model to "think" through complex problems step-by-step before responding, producing more accurate and nuanced answers for difficult tasks.

See source: [Claude S Extended Thinking](../sources/claude-s-extended-thinking.md)

## Early Practical Tests

In 2023, Brian X. Chen tested ChatGPT and Google Bard as executive assistants across four tasks: meeting preparation, summarizing meetings, planning business trips, and calendar management. ChatGPT significantly outperformed Bard, but both succeeded at most tasks even if imperfectly — early evidence that LLMs could eventually automate administrative white-collar roles.

See source: [How ChatGPT And Bard Performed As My Executive Assistants](../sources/how-chatgpt-and-bard-performed-as-my-executive-assistants.md)

## Limitations

### Hallucinations and Plausibility
LLMs can produce confident, plausible-sounding output that is factually wrong. Simon Willison demonstrated this by showing ChatGPT will write "thinly disguised horoscopes" — unfounded but authoritative-sounding analysis.

See source: [Chatgpt Will Happily Write You A Thinly Disguised Horoscope](../sources/chatgpt-will-happily-write-you-a-thinly-disguised-horoscope.md)

### The Comprehension Gap
Models that generate code may not "understand" it the way humans do, creating challenges for verification and debugging.

## The "Lossy Zip File" Mental Model

[Andrej Karpathy](andrej-karpathy.md) describes LLMs as "lossy, probabilistic zip files" of the internet. Pre-training compresses all of the internet into ~1 trillion parameters, creating vague but broad knowledge. Post-training attaches a "smiley face" (assistant persona) via human-labeled conversations. The user and model collaborate by building a shared one-dimensional token stream (the context window). Knowledge cutoff is an inherent limitation since pre-training is too expensive to run frequently.

See source: [How I Use LLMs](../sources/how-i-use-llms.md)

## Model Landscape

A guide to current frontier models and their comparative strengths:
- Claude Opus 4.6 — Strong reasoning, extended thinking, agentic coding
- GPT-5.2 Thinking — Reasoning-focused
- Gemini 3 Pro — Multimodal, large context

[Ethan Mollick](ethan-mollick.md) analyzes the diverging strategies: frontier model companies (OpenAI, Anthropic, Google) pursue general intelligence while Apple bets on small on-device models with cloud fallback, optimizing for narrow, reliable use cases (Siri) over open-ended capability. The tension between "a machine that can do anything" (frontier) vs "a machine that just works" (Apple) reflects fundamentally different bets on the future.

See sources: [A Guide To Which AI To Use In The Agentic Era](../sources/a-guide-to-which-ai-to-use-in-the-agentic-era.md), [What Apple's AI Tells Us: Experimental Models](../sources/what-apple-s-ai-tells-us-experimental-models4.md)

### Early Tools (2023)

The 2023 AI tool landscape was dominated by ChatGPT (14.6B visits), Character.ai (3.8B), and Quillbot (1.1B), reflecting early consumer adoption heavily concentrated in chatbots and writing tools.

See source: [Top 10 Most Popular AI Tools Of 2023](../sources/these-are-the-top-10-most-popular-ai-tools-of-2023-and-how.md)

## Related

- [Prompt Engineering](prompt-engineering.md)
- [Scaling And Compute](scaling-and-compute.md)
- [Reasoning Models](reasoning-models.md)
- [AGI Timelines](agi-timelines.md)
