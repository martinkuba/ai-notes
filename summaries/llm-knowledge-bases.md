---
id: "01knhs49r10xx60rr7hxkh99p9"
title: "LLM Knowledge Bases"
author: "Andrej Karpathy"
source_url: "https://x.com/karpathy/status/2039805659525644595/?rw_tt_thread=True"
category: "tweet"
tags: [ai]
saved_at: "2026-04-06T16:13:35.873000+00:00"
summarized_at: "2026-04-15T19:50:48Z"
---

# LLM Knowledge Bases

**Original source:** [LLM Knowledge Bases](https://x.com/karpathy/status/2039805659525644595/?rw_tt_thread=True)
**Author:** Andrej Karpathy

## Summary

Andrej Karpathy describes a pattern he has found increasingly useful: using LLMs to build and maintain personal knowledge bases for research topics. The workflow involves indexing source documents (articles, papers, repos, datasets, images) into a raw directory, then using an LLM to incrementally "compile" a wiki -- a collection of markdown files with summaries, backlinks, categorized concepts, articles, and cross-links. He uses the Obsidian Web Clipper to convert web articles to markdown and downloads related images locally for LLM reference. Obsidian serves as the IDE frontend for viewing raw data, the compiled wiki, and derived visualizations.

A key insight is that once the wiki reaches sufficient scale (Karpathy's example is around 100 articles and 400K words), you can ask the LLM agent complex questions against it, and it will research and synthesize answers. He initially expected to need fancy RAG, but found that having the LLM auto-maintain index files and brief summaries was sufficient at this scale for effective retrieval. Rather than receiving answers in a terminal, he has the LLM render outputs as markdown files, slide shows (Marp format), or matplotlib images, all viewable in Obsidian. Crucially, outputs from queries are often "filed" back into the wiki, so explorations compound the knowledge base over time.

Karpathy also describes running LLM "health checks" (linting) over the wiki to find inconsistencies, impute missing data using web search, discover interesting connections, and suggest new article candidates. He has built additional tools like a naive search engine over the wiki, usable both via a web UI and as a CLI tool for the LLM. Looking forward, he sees natural extensions into synthetic data generation and fine-tuning to embed knowledge into model weights rather than relying solely on context windows. He notes that this workflow -- raw data collection, LLM-compiled wiki, LLM-operated Q&A with incremental enhancement, all viewable in Obsidian -- represents an opportunity for a dedicated product rather than a collection of scripts.

## Main Ideas

- LLMs can effectively build and maintain personal knowledge bases by "compiling" raw source documents into structured markdown wikis with summaries, backlinks, and concept pages.
- Obsidian serves as an effective IDE for viewing and navigating LLM-maintained wikis, with the human rarely editing the wiki directly.
- At moderate scale (~100 articles, ~400K words), LLM-maintained index files and summaries can substitute for formal RAG pipelines.
- Query outputs should be filed back into the wiki so that explorations compound the knowledge base over time.
- LLM "linting" or health checks can find inconsistencies, impute missing data, and suggest new research directions.
- Additional tools (search engines, CLI utilities) can be vibe-coded to enhance both human and LLM interaction with the knowledge base.
- Future directions include synthetic data generation and fine-tuning to embed wiki knowledge directly into model weights.

## Key Quotes

- "I thought I had to reach for fancy RAG, but the LLM has been pretty good about auto-maintaining index files and brief summaries of all the documents and it reads all the important related data fairly easily at this ~small scale."
- "Often, I end up 'filing' the outputs back into the wiki to enhance it for further queries. So my own explorations and queries always 'add up' in the knowledge base."
- "I think there is room here for an incredible new product instead of a hacky collection of scripts."
