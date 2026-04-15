---
id: "01ke68v70syjamsqttmmasxg94"
title: "Thinking Like an AI"
author: "Ethan Mollick"
source_url: "https://www.oneusefulthing.org/p/thinking-like-an-ai?r=dwxxh&utm_medium=ios&triedRedirect=true"
category: "article"
tags: [ai]
saved_at: "2024-11-25T16:55:27+00:00"
summarized_at: "2026-04-15T20:00:38Z"
---

# Thinking Like an AI

**Original source:** [Thinking Like an AI](https://www.oneusefulthing.org/p/thinking-like-an-ai?r=dwxxh&utm_medium=ios&triedRedirect=true)
**Author:** Ethan Mollick

## Summary

In this 100th post on his One Useful Thing Substack, Ethan Mollick provides an accessible explanation of three core LLM concepts — next-token prediction, training data, and context windows — and explains how intuitive understanding of these mechanisms can help users get better results from AI. He uses actual GPT-3.5 probability distributions to demonstrate how LLMs work, showing that even tiny changes in prompts (capitalization, word choice, extra spaces) can dramatically alter the probability distribution for the next token, producing wildly different outputs.

Mollick explains that LLMs are sophisticated autocomplete systems that chain token predictions together, creating a "butterfly effect" where early token choices cascade into entirely different outputs. This helps explain hallucinations (the model guesses plausible-sounding continuations rather than retrieving facts), stubbornness (once committed to a direction, the model must justify it going forward), and why different users get different answers to the same question. He demonstrates how training data composition affects model performance, contrasting the model's near-perfect recall of Alice in Wonderland with its inability to reproduce obscure works by Cordwainer Smith.

On practical implications, Mollick notes that understanding training data helps users push models toward more original outputs by prompting for less common styles or topics. He explains that context windows function as short-term memory, resetting with each new conversation, and warns against expecting deep personal insights from models that don't actually remember you. Ultimately, Mollick argues that while these technical intuitions are helpful, the best way to understand AI is simply to use it extensively — about 10 hours of hands-on experimentation for work or fun.

## Main Ideas

- LLMs work through next-token prediction, where tiny prompt changes can produce dramatically different outputs
- Token predictions chain together in a "butterfly effect" — early choices cascade into completely different responses
- Hallucinations arise because models predict plausible words, not retrieve verified facts
- Training data composition determines what models are good at; common material is reproduced more accurately
- Pushing prompts toward less common territory in training data yields more original outputs
- Context windows are short-term memory that resets between conversations; AI doesn't learn about you persistently
- The best way to understand AI is 10 hours of hands-on experimentation

## Key Quotes

- "Saying 'AI is just next-token prediction' is a bit of a joke online, because it doesn't really help us understand why AI can produce such seemingly creative, novel, and interesting results."
