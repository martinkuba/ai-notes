---
id: "01ke68tgxw440td8149f93angq"
title: "Prompt engineering for Claude's long context window"
author: "anthropic.com"
source_url: "https://www.anthropic.com/news/prompting-long-context"
category: "article"
tags: [ai]
saved_at: "2025-07-21T17:44:20+00:00"
summarized_at: "2026-04-15T19:50:48Z"
---

# Prompt engineering for Claude's long context window

**Original source:** [Prompt engineering for Claude's long context window](https://www.anthropic.com/news/prompting-long-context)
**Author:** anthropic.com

## Summary

Anthropic presents a quantitative case study on two prompt engineering techniques that improve Claude's ability to recall information from long documents (up to 100,000 tokens). The two techniques are: (1) instructing Claude to extract relevant quotes into a scratchpad before answering, and (2) supplementing the prompt with examples of correctly answered questions drawn from the same document. The study uses a "randomized collage" methodology where sections of a government document are split up, used to generate multiple-choice questions, and then reassembled into long documents of 70K-95K tokens.

The experiments were primarily conducted on Claude Instant 1.2 (chosen because it benefits more visibly from prompting improvements than Claude 2, which already performs well on long-context recall). Four prompting strategies were tested: a baseline, generic non-contextual examples, two contextual examples, and five contextual examples — each with and without a scratchpad for quote extraction. Results showed that using five contextual examples combined with a scratchpad produced the best performance. For Claude 2, the improvement from 93.9% to 96.1% represented a 36% reduction in errors.

The study also revealed important positional effects: while scratchpad and examples substantially improved recall for information at the beginning and middle of documents, they sometimes degraded performance for content at the very end, likely because the added examples increased the distance between the final content and the question. This finding reinforces Anthropic's recommendation to place instructions at the end of prompts. The evaluation methodology itself is noteworthy — using Claude to generate test questions, then carefully filtering out questions Claude gets wrong in short-context settings to isolate the long-context recall variable.

## Main Ideas

- Two techniques improve long-context recall: extracting relevant quotes into a scratchpad before answering, and providing contextual few-shot examples of correctly answered questions from the same document.
- Contextual examples from the document are effective, while generic/external knowledge examples provide no measurable benefit.
- Combining five contextual examples with a scratchpad yields the best performance across both 70K and 95K token documents.
- Information position matters: recall is generally better for content near the end of the document (closest to the question), with a roughly inverse relationship between distance and performance for Claude Instant.
- Adding scratchpad instructions and examples can slightly degrade recall for content at the very end of the document, reinforcing the importance of placing instructions after the document.
- The "randomized collage" evaluation method — splitting documents, generating QA pairs with Claude, then reassembling into long contexts — provides a scalable approach for testing long-context recall.
- For Claude 2, the prompting improvement from 93.9% to 96.1% accuracy represents a 36% reduction in errors, showing these techniques help even already-strong models.
