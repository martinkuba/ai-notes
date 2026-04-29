---
tags: [technical, llm, reasoning, architecture]
---

# Reasoning Models

A class of LLMs that perform structured, multi-step reasoning before producing a final answer — a qualitative shift from the pure next-token prediction described in [How LLMs Work](how-llms-work.md). Reasoning models trade latency for capability on hard problems: math, code, logic, science.

## The Shift

Standard chat models predict the next token directly. Reasoning models generate an internal chain of thought first — exploring, backtracking, verifying — and then produce a response. The chain may be hidden (o1) or surfaced as visible "thinking" (Claude Extended Thinking). The result: better accuracy on problems where fluency alone fails.

## Examples

### OpenAI o1 / Strawberry
[OpenAI](openai.md)'s first reasoning model. Explicitly framed as *not a chat model* — designed for complex problem-solving rather than conversation. Marked the field's clearest pivot from token prediction to structured reasoning.

See sources: [O1 Isnt A Chat Model](../summaries/o1-isnt-a-chat-model-and-thats-the-point.md), [Something New On Openai S Strawberry And Reasoning](../summaries/something-new-on-openai-s-strawberry-and-reasoning.md).

### Claude Extended Thinking
[Anthropic](anthropic.md)'s reasoning capability, built into Claude Opus 4.x. Lets the model think through problems step-by-step before responding. Surfaced in [Claude Code](claude-code.md) for harder coding tasks.

See source: [Claude S Extended Thinking](../summaries/claude-s-extended-thinking.md).

### GPT-5.2 Thinking
Reasoning-focused variant in the GPT-5.x family. See [How LLMs Work](how-llms-work.md) for the model landscape.

## Why It Matters

Reasoning models are the technical substrate for several wiki narratives:

- **AGI claims** — The OpenAI employee who claimed "we have already achieved AGI" cited o1 specifically. See [AGI Timelines](agi-timelines.md).
- **Agentic coding capability** — Many of the gains [Boris Cherny](boris-cherny.md) and [Andrej Karpathy](andrej-karpathy.md) report come from agents using reasoning models for planning and verification, not just generation.
- **Scaffolding vs. scaling** — The ARC-AGI-3 results suggest the next leap may come from rethinking scaffolding around reasoning models rather than from larger weights. See [AGI Timelines](agi-timelines.md).

## Limitations

Reasoning is computationally expensive and slow. Not every task warrants it. Reasoning models can also hallucinate confidently in their chain of thought, producing plausible-looking derivations that arrive at wrong answers. The same comprehension/verification challenges from [How LLMs Work](how-llms-work.md) apply.

## Related

- [How LLMs Work](how-llms-work.md)
- [OpenAI](openai.md)
- [Anthropic](anthropic.md)
- [Claude Code](claude-code.md)
- [AGI Timelines](agi-timelines.md)
