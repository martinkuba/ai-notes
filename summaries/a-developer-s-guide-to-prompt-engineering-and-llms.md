---
id: "01ke68twhzzf5ft95vsd206ssm"
title: "A developer's guide to prompt engineering and LLMs"
author: "John Berryman"
source_url: "https://github.blog/ai-and-ml/generative-ai/prompt-engineering-guide-generative-ai-llms/"
category: "article"
tags: [ai]
saved_at: "2024-12-04T19:24:27+00:00"
summarized_at: "2026-04-15T19:35:33Z"
---

# A developer's guide to prompt engineering and LLMs

**Original source:** [A developer's guide to prompt engineering and LLMs](https://github.blog/ai-and-ml/generative-ai/prompt-engineering-guide-generative-ai-llms/)
**Author:** John Berryman

## Summary

This article from the GitHub engineering blog explains both the fundamentals of LLMs and the specific prompt engineering techniques GitHub developed for Copilot. At the conceptual level, LLMs are framed as document completion engines -- sophisticated versions of phone autocomplete that predict the next token based on massive training data. The key insight for building applications is that every LLM app maps between a "user domain" (the actual problem) and a "document domain" (the textual context the model completes). The article illustrates this with a detailed example of an ISP support chatbot where a pseudo-transcript is constructed so that the model naturally completes it as a helpful IT expert, including injected documentation from a search engine to ground responses.

The second half details GitHub Copilot's six-step prompt engineering pipeline. Step 1 (Gathering Context) collects metadata like filename, language, and content from open editor tabs, with strict latency constraints -- every additional 10ms reduces the chance a suggestion arrives in time by 1%. Step 2 (Snippeting) cuts related files into overlapping 60-line snippets scored by Jaccard similarity to select the most relevant code. Step 3 (Dressing Up) injects this context naturally into the prompt using comment syntax, filepath headers, and shebang lines -- essentially disguising external context as normal code annotations. Step 4 (Prioritization) treats each context element as a "wish" with a priority score, iteratively dropping the lowest-priority wishes until the remaining content fits the context window. Step 5 (AI Completion) navigates the speed-vs-quality tradeoff, noting that GitHub found developers got more value from faster models. Step 6 (Post-processing) handles stop criteria and multi-line completion logic, detecting when the developer is starting a semantic block and extending suggestions to fill it.

The article provides a practical template for how to think about prompt engineering for any LLM application: construct the right document context, select and prioritize relevant information, and present it naturally to the model.

## Main Ideas

- LLMs are fundamentally document completion engines; every LLM application maps between a user domain and a document domain.
- Prompt engineering is the art of constructing the right pseudo-document so the model's completion solves the user's actual problem.
- Retrieval-augmented generation (injecting searched documentation into the prompt) can ground LLM responses in domain-specific knowledge.
- GitHub Copilot's pipeline involves six steps: gathering context, snippeting, dressing up context in natural code comments, prioritizing wishes, AI completion, and post-processing stop criteria.
- Latency is critical for interactive tools -- every 10ms of delay reduces the chance a Copilot suggestion arrives in time by 1%.
- Jaccard similarity scoring on 60-line overlapping snippets is used to select the most relevant context from open editor tabs.
- Faster models outperformed more capable but slower models in practice because suggestion timeliness matters more than raw quality.

## Key Quotes

- "The secret is any application that uses an LLM is actually mapping between two domains: the user domain and the document domain."
- "For every additional 10 milliseconds we take to come up with a suggestion, the chance it'll arrive in time decreases by one percent."
