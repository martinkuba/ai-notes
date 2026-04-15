---
id: "01ke68ttba7fd2c3cr7ep1frw6"
title: "o1 isn't a chat model (and that's the point)"
author: "Ben Hylak"
source_url: "https://www.latent.space/p/o1-skill-issue"
category: "article"
tags: [ai]
saved_at: "2025-01-20T00:28:48+00:00"
summarized_at: "2026-04-15T19:50:48Z"
---

# o1 isn't a chat model (and that's the point)

**Original source:** [o1 isn't a chat model (and that's the point)](https://www.latent.space/p/o1-skill-issue)
**Author:** Ben Hylak

## Summary

Ben Hylak, writing as a guest on the Latent Space newsletter, recounts his journey from being an outspoken skeptic of OpenAI's o1 model to becoming an enthusiastic daily user. His initial experience was deeply frustrating — long wait times followed by walls of self-contradicting text with unrequested architecture diagrams. The key realization was that he had been using o1 like a conventional chat model, but o1 is fundamentally a different kind of tool: a "report generator" that requires a completely different interaction paradigm.

Hylak outlines three core principles for effective o1 usage. First, instead of writing short prompts and iterating through conversation, users should write comprehensive "briefs" — pushing as much context as possible into the model, including database schemas, company context, everything tried so far, and detailed definitions. Where chat models pull context from users through back-and-forth, o1 takes prompts at face value. Second, users should focus on describing exactly what output they want (the "what") rather than instructing the model on how to think (the "how"), allowing o1's autonomous reasoning to plan its own approach. Third, users should understand o1's strengths and weaknesses: it excels at one-shotting entire files, generating accurate code for niche query languages, explaining difficult concepts, and evaluating outputs (LLM-as-Judge), but struggles with writing in specific voices/styles and building entire applications.

The article also discusses UI design implications of reasoning models. Because o1 responses have high latency (5+ minutes), the chat interface is a poor fit — it functions more like email than instant messaging. Hylak suggests UX improvements including mini tables of contents, navigable response hierarchies, and better context management interfaces. He expresses excitement about o1 enabling new categories of products that leverage high-latency, long-running background intelligence.

## Main Ideas

- o1 is not a chat model — it is a "report generator" that requires a fundamentally different interaction paradigm: push large amounts of context in rather than pulling it out through back-and-forth conversation.
- Write "briefs" not prompts: include database schemas, company context, prior failed attempts, and detailed definitions — treat o1 like a new hire who needs full context.
- Focus on describing what you want as output, not how the model should think — let o1's autonomous reasoning plan its own approach.
- o1 excels at one-shotting entire files of code, handling niche query languages accurately, explaining complex concepts, and serving as an LLM-as-Judge evaluator.
- o1 struggles with writing in specific voices/styles (defaulting to academic/corporate report tone) and cannot build entire applications, though it can one-shot individual features.
- The high latency of reasoning models demands new UI paradigms — chat interfaces are a poor fit, and products should explore designs suited to asynchronous, report-style outputs.
- The perception gap between o1's actual capability and initial user impressions represents a "skill issue" — learning to use the model correctly can completely change the experience.

## Key Quotes

- "I was using o1 like a chat model — but o1 is not a chat model."
- "Spend 100x more in prompting if you expect 100x more in output quality."
- "To justify the $200/mo price tag, it just has to provide 1-2 Engineer hours a month."
