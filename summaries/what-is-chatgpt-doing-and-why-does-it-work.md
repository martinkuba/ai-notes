---
id: "01ke68vkhhwws31383m0j1gthk"
title: "What Is ChatGPT Doing … and Why Does It Work?"
author: "stephenwolfram.com"
source_url: "https://writings.stephenwolfram.com/2023/02/what-is-chatgpt-doing-and-why-does-it-work/"
category: "article"
tags: [ai]
saved_at: "2024-01-14T03:17:15+00:00"
summarized_at: "2026-04-15T20:00:38Z"
---

# What Is ChatGPT Doing … and Why Does It Work?

**Original source:** [What Is ChatGPT Doing … and Why Does It Work?](https://writings.stephenwolfram.com/2023/02/what-is-chatgpt-doing-and-why-does-it-work/)
**Author:** stephenwolfram.com

## Summary

Stephen Wolfram provides a comprehensive technical explanation of how ChatGPT works, starting from the fundamental insight that it is a next-word prediction system. At each step, the model takes all preceding text and produces a probability distribution over possible next tokens. A "temperature" parameter controls randomness — always choosing the top-ranked word produces flat, repetitive text, while introducing controlled randomness (temperature ~0.8) yields more creative output. Wolfram uses actual Wolfram Language code with the GPT-2 model to demonstrate these concepts interactively.

The article builds up from first principles: from letter-frequency analysis to n-gram models to the realization that there aren't enough texts in existence to estimate probabilities for all possible word sequences, necessitating a model that can generalize. This is where neural networks enter — Wolfram explains perceptrons, layers, activation functions, training via loss minimization, and backpropagation. He then covers the key innovations that make modern LLMs work: embeddings (representing words as points in high-dimensional "meaning space"), attention mechanisms (allowing the model to attend to relevant earlier parts of the text), and the transformer architecture.

A particularly insightful section addresses computational irreducibility — Wolfram's signature concept. He argues that there's a fundamental tension between trainability and computational capability: neural networks are trainable precisely because they operate in a "computationally shallow" regime, but this means they can't perform computationally irreducible tasks (like formal mathematics). The surprising conclusion is that tasks like essay writing, which we assumed were "fundamentally hard," are actually computationally shallower than we thought — which is why neural networks can do them. The article suggests that the success of LLMs reveals something deep about the nature of human language: it may have a more regular, learnable structure than we previously appreciated.

## Main Ideas

- ChatGPT is fundamentally a next-word prediction system using probability distributions over tokens
- Temperature controls the tradeoff between predictability and creativity in output
- Neural networks generalize beyond training data by learning compressed statistical patterns of language
- Embeddings represent words as points in high-dimensional "meaning space" where similar words cluster together
- The transformer architecture with attention mechanisms enabled the breakthrough in language modeling
- Computational irreducibility creates a fundamental limit: neural nets can't do everything, only computationally "shallow" tasks
- Essay writing being achievable by LLMs reveals it's computationally shallower than we assumed
- The success of LLMs suggests human language has more regular, learnable structure than previously thought
