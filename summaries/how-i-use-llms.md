---
id: "01kk86cbbym7tsm04nj5z6xkyp"
title: "How I use LLMs"
author: "Andrej Karpathy"
source_url: "https://www.youtube.com/watch?v=EWvNQjAaOHw"
category: "video"
tags: [ai]
saved_at: "2026-03-09T02:21:23.198000+00:00"
summarized_at: "2026-04-15T19:46:34Z"
---

# How I use LLMs

**Original source:** [How I use LLMs](https://www.youtube.com/watch?v=EWvNQjAaOHw)
**Author:** Andrej Karpathy

## Summary

Andrej Karpathy delivers a comprehensive, practical guide to using large language models effectively across everyday life and professional work. He begins with a foundational mental model: LLMs are "zip files" of the internet -- lossy, probabilistic compressions of web knowledge with a knowledge cutoff from pre-training, plus an assistant persona from post-training. He stresses that understanding this architecture is key to knowing what questions are safe to ask (common, non-recent knowledge) versus what requires tool use (recent or niche information).

Karpathy walks through the major capabilities and tools available across LLM providers (ChatGPT, Claude, Gemini, Grok, Perplexity, DeepSeek). He covers thinking/reasoning models trained via reinforcement learning, which excel at hard math and code problems by developing internal problem-solving strategies. He demonstrates internet search integration (where models visit web pages and stuff results into the context window), Deep Research (extended thinking + search that produces custom research reports over 10+ minutes), file uploads for reading papers and books alongside an LLM, Python interpreter use for data analysis and visualization, Claude's artifacts feature for generating interactive apps, and Cursor/Composer for professional vibe coding. He also explores multimodal capabilities: speech-to-text input, advanced voice mode (native audio tokens), image input for analyzing nutrition labels and blood tests, image generation via DALL-E, video input via mobile camera, and podcast generation via NotebookLM.

Throughout, Karpathy emphasizes practical wisdom: start new chats when switching topics to keep the context window clean, verify model outputs against primary sources, be aware of which model and pricing tier you are using, transcribe images to text first before asking questions to verify accuracy, and treat all AI outputs as "first drafts" that need human verification. He uses his personal workflow of consulting an "LLM council" -- asking the same question across multiple providers -- and demonstrates custom GPTs for Korean language learning as examples of few-shot prompting to create personalized tools.

## Main Ideas

- LLMs should be understood as lossy, probabilistic "zip files" of the internet with a knowledge cutoff; this mental model guides what you can and cannot trust them to know.
- Thinking/reasoning models (trained via reinforcement learning) provide significantly higher accuracy on hard math and code problems but are overkill for simple queries.
- Internet search tools allow models to access fresh information beyond their training cutoff by visiting web pages and loading content into the context window.
- Deep Research combines extended thinking with internet search to produce custom research reports, but all outputs should be treated as first drafts with potential hallucinations.
- File uploads enable reading papers and books alongside an LLM, dramatically increasing comprehension and accessibility of unfamiliar material.
- Professional coding with tools like Cursor/Composer (vibe coding) is where Karpathy spends most of his time, using AI as an autonomous agent on the codebase.
- Multimodal capabilities (voice, image, video) are rapidly maturing, with native audio handling being qualitatively different from speech-to-text wrappers.
- Consulting an "LLM council" -- asking the same question across multiple providers -- is a practical strategy for getting diverse perspectives and catching errors.

## Key Quotes

- "Hi, I'm ChatGPT. I am a one-terabyte zip file. My knowledge comes from the internet, which I read in its entirety about six months ago, and I only remember vaguely."
- "Don't read books alone."
- "Treat this as your first draft, treat this as papers to look at, but don't take this as definitely true."
