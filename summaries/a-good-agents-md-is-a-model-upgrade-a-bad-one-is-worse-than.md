---
id: "01krkyh0c02kqctyg7d9p6r2pz"
title: "A good AGENTS.md is a model upgrade. A bad one is worse than no docs at all."
author: "Slava Zhenylenko"
source_url: "https://www.augmentcode.com/blog/how-to-write-good-agents-dot-md-files"
category: "article"
tags: [ai]
saved_at: "2026-05-14T19:13:29.472000+00:00"
summarized_at: "2026-05-14T19:32:05Z"
---

# A good AGENTS.md is a model upgrade. A bad one is worse than no docs at all.

**Original source:** [A good AGENTS.md is a model upgrade. A bad one is worse than no docs at all.](https://www.augmentcode.com/blog/how-to-write-good-agents-dot-md-files)
**Author:** Slava Zhenylenko

## Summary

AugmentCode conducted an empirical study measuring the impact of `AGENTS.md` documentation files on AI agent code generation quality. They evaluated hundreds of PRs using AuggieBench and found that well-designed `AGENTS.md` files can deliver quality improvements equivalent to upgrading from a weaker to stronger model (e.g., Haiku to Opus), while poorly-designed ones actively degrade output quality compared to having no documentation. The same file can simultaneously improve performance on one task by 25% while degrading another by 30%, showing that documentation effectiveness is task-dependent.

The study identified specific patterns that reliably improve agent performance: progressive disclosure (100–150 line main files with focused references), procedural multi-step workflows, decision tables for resolving ambiguity, real code examples from the actual codebase, domain-specific rules, and pairing prohibitions ("don'ts") with concrete alternatives ("dos"). In contrast, common failure modes include the "overexploration trap"—where comprehensive architecture documentation pulls the agent into reading dozens of unnecessary files—excessive warning lists without corresponding guidance, and documentation that describes outdated patterns conflicting with new architectural directions.

A critical finding concerns documentation discovery: `AGENTS.md` files are automatically discovered in 100% of cases, making them the only reliably discoverable documentation location. The research also revealed that the module environment matters as much as the file itself—a focused `AGENTS.md` sitting atop 500K of surrounding specs doesn't prevent the agent from finding and reading that sprawl, undermining the intended focus.

## Main Ideas

- **Same documentation, opposite effects**: A single `AGENTS.md` can improve task performance by 25% on one type of work while degrading it by 30% on another, depending on task scope and reference relevance
- **Progressive disclosure pattern wins**: 100–150 line main files with focused reference documents on-demand outperformed both minimal and comprehensive documentation approaches
- **Procedural workflows eliminate ambiguity**: Multi-step numbered workflows reduced missing components (40% → 10%), increased correctness (+25%), and completeness (+20%)
- **Decision tables enforce conventions**: Choice matrices for selecting between similar approaches (e.g., React Query vs Zustand) improved best_practices adherence by 25%
- **Overexploration trap**: Comprehensive architecture overviews and excessive warning lists cause agents to read dozens of unnecessary documentation files, wasting context and degrading output quality
- **Documentation discovery is lopsided**: AGENTS.md is the only reliably discovered documentation location (100% of cases); nested READMEs reach 40% discovery; orphan docs in `_docs/` folders reach under 10%
- **Fix the environment, not just the entry point**: Surrounding documentation sprawl undermines even good `AGENTS.md` files; fixing the module's overall documentation structure is as important as perfecting the single file

## Key Quotes

> "The best ones gave our coding agent a quality jump equivalent to upgrading from Haiku to Opus. The worst ones made the output worse than having no `AGENTS.md` at all."

> "Progressive disclosure beats comprehensive coverage. Treat your `AGENTS.md` like a skill. Cover the common cases and workflows at a high level, then push details into reference files the agent can load on demand."

> "`AGENTS.md` is the only documentation location with reliable discovery. If something needs to be seen, it either lives there or is directly referenced from there."
