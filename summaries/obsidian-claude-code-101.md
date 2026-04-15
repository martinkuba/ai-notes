---
id: "01kfcw96xs5w5hgnrj46hqqwm4"
title: "obsidian + claude code 101"
author: "Heinrich"
source_url: "https://x.com/arscontexta/status/2013045749580259680/?s=12&rw_tt_thread=True"
category: "tweet"
tags: [ai]
saved_at: "2026-01-20T04:58:19.449000+00:00"
summarized_at: "2026-04-15T19:50:48Z"
---

# obsidian + claude code 101

**Original source:** [obsidian + claude code 101](https://x.com/arscontexta/status/2013045749580259680/?s=12&rw_tt_thread=True)
**Author:** Heinrich

## Summary

Heinrich describes a system he has built over the past year that uses Claude Code to operate Obsidian vaults as an "operating system for thinking with AI." The core insight is that knowledge bases and codebases have a lot in common — they are both folders of text files with relationships between them, conventions and patterns, and both benefit from agents that can navigate and operate them. Just as "vibe coding" changed software development by letting AI handle implementation while humans focus on direction, the same shift applies to knowledge work: you don't take notes anymore, you operate a system that takes notes.

The system works through several layers. A vault is a structured folder of interconnected markdown files using wiki-style links. A CLAUDE.md file teaches the AI agent the vault's specific philosophy, conventions, and operating instructions — Heinrich's own is around 2,000 lines. The agent orients itself at session start by viewing the folder structure via hooks, scanning an index file with one-sentence descriptions of each note, and reading topic pages (Maps of Content) that link to related notes. Topic pages also contain breadcrumbs the agent leaves for itself about what it learned while traversing the graph, enabling cross-session learning.

Heinrich emphasizes that every vault needs its own philosophy based on its purpose — a work vault, research vault, and creative vault would all have different rules despite sharing the same underlying pattern of markdown files, links, and AI operation. For his personal thinking vault, key principles include composability (each note should stand alone), naming notes as claims rather than topics (e.g., "quality is the hard part" instead of "thoughts on AI slop"), and valuing network relationships over individual notes. The human role evolves from writer to editor, from creator to curator — providing judgment about what matters while the AI system handles navigation, connection-finding, and structured output.

## Main Ideas

- Knowledge bases and codebases share deep structural similarities — both are folders of text files with relationships, conventions, and patterns that benefit from agent navigation.
- "Vibe note-taking" mirrors vibe coding: the human provides direction and judgment while the AI agent handles implementation, connection-finding, and structuring.
- CLAUDE.md is the critical teaching document that encodes your vault's philosophy, conventions, and operating instructions for the AI agent.
- Agent orientation happens in layers: folder structure (via hooks), index file scanning, then topic page (MOC) reading — allowing quick navigation without reading every file.
- Topic pages serve as cross-session memory, with the agent leaving breadcrumbs about what it learned while traversing the knowledge graph.
- Notes should be composable (standalone) and named as claims rather than topics, so linking them into sentences reads naturally and forces deeper understanding.
- The network of relationships between notes is more valuable than any individual note — link density creates reading paths and emergent knowledge.

## Key Quotes

- "You don't take notes anymore. You operate a system that takes notes."
- "Knowledge bases and codebases have a lot in common — they're both folders of text files with relationships between them."
- "The human role evolves from writer to editor and from creator to curator."
