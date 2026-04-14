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

See source: [Indexing In RAG Systems Building The Brain](../sources/indexing-in-rag-systems-building-the-brain.md)

## AI-Native Reading

Kairos maps Mortimer Adler's reading levels to AI-assisted interaction:
- **Elementary** — AI explains concepts simply
- **Inspectional** — AI provides summaries and structure
- **Analytical** — AI enables deep questioning
- **Syntopical** — AI connects themes across multiple texts

See source: [A New Way To Read](../sources/a-new-way-to-read.md)

## AI + Obsidian

Integration of Claude with Obsidian for enhanced knowledge management — combining AI capabilities with networked note-taking.

See source: [Claude Obsidian Got A Level Up](../sources/claude-obsidian-got-a-level-up.md)

## This Wiki

This wiki itself follows the "LLM Wiki" pattern: a three-layer architecture (raw sources → LLM-maintained wiki → schema) that uses AI to maintain cross-references and build knowledge over time. The LLM handles the bookkeeping humans find tedious.

## Related

- [Deep Research](deep-research.md)
- [How LLMS Work](how-llms-work.md)
- [Prompt Engineering](prompt-engineering.md)
