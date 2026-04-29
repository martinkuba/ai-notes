---
tags: [rag, retrieval, knowledge, tools]
---

# RAG and Knowledge Systems

Retrieval-Augmented Generation (RAG) and related approaches for grounding AI in external knowledge sources.

## RAG Architecture

### Indexing
The core technical challenge: building the "brain" behind knowledge-augmented AI. Key components:
- **Chunking strategies** — How to split documents for retrieval (fixed-size, semantic, recursive)
- **Embedding models** — Converting text to vector representations
- **Vector databases** — Storing and searching embeddings efficiently
- **Query-time retrieval** — Matching questions to relevant chunks

See source: [Indexing In RAG Systems Building The Brain](../summaries/indexing-in-rag-systems-building-the-brain-behind-knowledge.md)

## AI-Native Reading

Kairos maps Mortimer Adler's reading levels to AI-assisted interaction:
- **Elementary** — AI explains concepts simply
- **Inspectional** — AI provides summaries and structure
- **Analytical** — AI enables deep questioning
- **Syntopical** — AI connects themes across multiple texts

See source: [A New Way To Read](../summaries/a-new-way-to-read.md)

## LLM Knowledge Bases

[Andrej Karpathy](andrej-karpathy.md)'s system for personal knowledge bases: a `raw/` folder for ingestion, a `wiki/` folder compiled by AI, and Obsidian as the IDE. The LLM handles summarizing, cross-referencing, Q&A, linting, and synthetic data generation.

See source: [LLM Knowledge Bases](../summaries/llm-knowledge-bases.md)

## AI + Obsidian

Integration of Claude with Obsidian for enhanced knowledge management — combining AI capabilities with networked note-taking. The key insight: Obsidian CLI gives Claude Code access not just to files but to the *inter-relationships* between them, enabling the agent to surface latent patterns across your vault that you wouldn't notice yourself. The better the context you feed (via files, not re-explanation), the more complex the delegation.

See sources: [Claude Obsidian Got A Level Up](../summaries/claude-obsidian-got-a-level-up.md), [How To Build Your AI Second Brain Using Obsidian Claude Code](../summaries/how-to-build-your-ai-second-brain-using-obsidian-claude-code.md), [How To Build Your Second Brain](../summaries/how-to-build-your-second-brain.md), [Obsidian Claude Code 101](../summaries/obsidian-claude-code-101.md), [How I Use Obsidian + Claude Code To Run My Life](../summaries/how-i-use-obsidian-claude-code-to-run-my-life.md)

## Research vs. Creation Workflows

Google's two notebook-style AI tools demonstrate a useful general principle: separate the research phase from the creation phase. **NotebookLM** excels at grounded research — upload multiple sources, ask questions with citation-backed answers, generate Audio Overviews and study guides. **Gemini Notebooks** is optimized for creation — transforming research into polished outputs like blog posts, presentations, and marketing materials, with access to live web information.

The key insight: using both sequentially (NotebookLM for understanding → Gemini Notebooks for creation) is more effective than forcing one tool to handle both stages. NotebookLM's source grounding prevents AI drift; Gemini Notebooks' broader tooling enables polished output.

See source: [I Finally Figured Out When To Use Gemini Notebooks vs NotebookLM](../summaries/i-finally-figured-out-when-to-use-gemini-notebooks-vs.md)

## This Wiki

This wiki itself follows the "LLM Wiki" pattern: a three-layer architecture (raw sources → LLM-maintained wiki → schema) that uses AI to maintain cross-references and build knowledge over time. The LLM handles the bookkeeping humans find tedious.

## Evaluating AI Systems

A critical but often overlooked discipline. Key techniques and dimensions:

- **LLM-as-a-judge** — Use a language model to evaluate outputs; requires careful implementation and awareness of its limitations (self-preference, sycophancy)
- **Evaluation-driven development** — Design and evaluation criteria are specified before implementation, analogous to TDD
- **Six core eval types for RAG systems** — Evaluation needs can be systematized around retrieval quality, generation quality, groundedness, etc.
- **Binary vs. Likert scale** — Different methodological choices with distinct tradeoffs for consistency vs. nuance
- **Error analysis** — Fundamental to iterating and improving AI systems; generic metrics are often misleading

See source: [Every Day 100+ People Ask Me How Can I Learn AI Evals](../summaries/every-day-100-people-ask-me-how-can-i-learn.md)

## Related

- [Deep Research](deep-research.md)
- [How LLMS Work](how-llms-work.md)
- [Prompt Engineering](prompt-engineering.md)
