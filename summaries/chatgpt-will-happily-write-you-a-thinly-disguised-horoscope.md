---
id: "01ke68txrj39vq1p12pxqcmwb3"
title: "ChatGPT will happily write you a thinly disguised horoscope"
author: "Simon Willison"
source_url: "https://simonwillison.net/2024/Oct/15/chatgpt-horoscopes/"
category: "article"
tags: [ai]
saved_at: "2024-11-25T16:52:40+00:00"
summarized_at: "2026-04-15T19:39:03Z"
---

# ChatGPT will happily write you a thinly disguised horoscope

**Original source:** [ChatGPT will happily write you a thinly disguised horoscope](https://simonwillison.net/2024/Oct/15/chatgpt-horoscopes/)
**Author:** Simon Willison

## Summary

Simon Willison debunks a viral meme where users ask ChatGPT "From all of our interactions what is one thing that you can tell me about myself that I may not know about myself" and receive seemingly profound personality insights. He demonstrates this is essentially the Barnum effect—a psychological phenomenon where people give high accuracy ratings to vague, flattering personality descriptions that could apply to anyone. ChatGPT's "memory" feature is just a simple tool that stores a handful of brief notes, not a deep ongoing analysis of the user's personality.

Willison reverse-engineers the memory system by prompting ChatGPT to reveal its system prompt, showing that the "bio" tool simply persists small text snippets across conversations. His own memory contained only a few sparse notes about open-source projects and being a Python programmer—yet ChatGPT produced glowing assessments about his "natural ability to create tools that are both technically robust and unexpectedly resourceful." The flattery is generated from minimal data and could apply to virtually any developer.

The deeper concern is that this meme reinforces a common misconception about how ChatGPT works—that it has been learning about your personality through ongoing conversations and can refer back to them later. In reality, ChatGPT's context consists of only the current conversation, stored memory notes, and custom instructions. Understanding this is crucial for using LLMs effectively, as effective use is entirely about controlling context. Willison notes this also serves as a reminder of how susceptible humans are to psychological tricks, and that LLMs—being extremely effective at human language—are particularly good at exploiting these biases.

## Main Ideas

- ChatGPT's "personality insights" meme is a modern manifestation of the Barnum effect—vague flattery that feels personalized
- ChatGPT's memory is just a handful of brief text notes, not a deep analysis of user behavior over time
- The meme reinforces the dangerous misconception that ChatGPT learns from and remembers all past conversations
- Effective LLM use depends on understanding and controlling context—knowing exactly what information the model has access to
- LLMs are particularly good at exploiting psychological biases because of their facility with human language
- Even horoscope-like tools can prompt useful self-reflection, regardless of their actual accuracy
