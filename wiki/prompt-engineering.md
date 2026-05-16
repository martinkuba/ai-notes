---
tags: [prompting, techniques, practical]
---

# Prompt Engineering

The practice of crafting inputs to AI systems to get better outputs. Ranges from simple conversational techniques to structured methodologies for complex tasks.

## Getting Started: Good Enough Prompting

Ethan Mollick argues against over-engineering prompts. For most tasks, a clear, natural language description works well. The key insight: just start using AI and iterate — perfection is the enemy of adoption.

See source: [Getting Started With AI Good Enough Prompting](../summaries/getting-started-with-ai-good-enough-prompting.md)

## When to Use AI (and When Not)

Mollick's framework:
- **Use AI for**: idea generation, drafting, summarization, specialized domain work, brainstorming, formatting
- **Avoid AI for**: tasks where learning matters, high-accuracy requirements, tasks where effort itself is the point

See source: [15 Times To Use AI And 5 Not To](../summaries/15-times-to-use-ai-and-5-not-to.md)

## Thinking Like an AI

Framing problems the way AI systems process them improves results. Understanding token prediction, context windows, and model tendencies helps craft better prompts.

See source: [Thinking Like An AI](../summaries/thinking-like-an-ai.md)

## Long Context Prompting

Specific techniques for leveraging Claude's extended context window: document placement, structured queries, XML tags for organization.

See source: [Prompt Engineering For Claude S Long Context Window](../summaries/prompt-engineering-for-claude-s-long-context-window.md)

## Technical: How Prompts Are Processed

GitHub Copilot's pipeline reveals prompt engineering at scale: snippet extraction from open files, context dressing (wrapping code in natural language cues), priority scoring to fit context windows.

See source: [A Developer S Guide To Prompt Engineering And LLMS](../summaries/a-developer-s-guide-to-prompt-engineering-and-llms.md)

## The Wait Calculation Trap

Mollick warns against the "lazy tyranny of the wait calculation" — procrastinating AI adoption because something better is always around the corner. The opportunity cost of waiting exceeds the cost of using imperfect tools now.

See source: [The Lazy Tyranny Of The Wait Calculation](../summaries/the-lazy-tyranny-of-the-wait-calculation.md)

## Context Engineering

The real leverage is not in wordsmithing prompts but in designing the information environment surrounding them. A three-layer model explains why most people get generic outputs: they only use layer one.

1. **Immediate context** — the prompt itself
2. **Session context** — conversation history and uploaded files
3. **Persistent context** — knowledge that carries across sessions (memory files, foundational docs)

The practical framework: four reusable context files (identity, audience, standards, project), dynamic loading rules matched to task type rather than loading everything, and persistent memory systems that compound over time (Markdown → structured knowledge bases → RAG). At scale, MCP tools let context-rich systems act rather than merely advise.

> "Prompt engineering is the syntax. Context engineering is the infrastructure. And infrastructure beats syntax every single time."

See source: [How to Master Context Engineering & Build AI Systems That Actually Understand You](../summaries/how-to-master-context-engineering-build-ai-systems-that.md)

## Role-Based Prompt Templates

Prompt architecture matters more than model capability. Transformative outputs come from role definition, explicit context, structure rules, and format specification — not clever wording. Common patterns:

- **Specialized role framing** ("senior research analyst", "brutal editor", "Socratic teacher") unlocks very different thinking patterns from the same model
- **Multi-source synthesis** (consensus/conflicts/gaps across documents) delivers more value than sequential summarization
- **Structured output templates** with explicit sections make output immediately actionable
- **Explicit constraints** ("do not do X", "quote the source", "end with one sentence") produce more usable outputs than open-ended requests
- **Learning through dialogue** — Socratic and Feynman techniques force active reasoning rather than passive consumption

See source: [20 Claude Prompts That Turn a $20 Subscription into a Personal Assistant, Editor, Coach, and Analyst](../summaries/20-claude-prompts-that-turn-a-20-subscription-into-a.md)

## Beyond Prompting: Customization Levers

Prompting is just one of four levers for escaping the "averaged out" default AI experience. By default, models optimize for the median user via RLHF training. The full customization stack:
1. **Memory** — Persistent facts across conversations (platform-specific: ChatGPT conversation history, Claude project-scoped memory, Gemini Google app integration)
2. **Instructions** — Persistent behavioral guidance (custom instructions, project instructions, CLAUDE.md files, style profiles)
3. **Style controls** — Uploading writing samples for tone matching (Claude's style feature is particularly underused)
4. **Apps and tools** — [MCP](mcp.md) connectors, web search, code execution, file access

See source: [90% Of AI Users Are Getting Mediocre Output](../summaries/90-of-ai-users-are-getting-mediocre-output-don-t-be-one-of.md)

## Related

- [Spec Driven Development](spec-driven-development.md)
- [Agentic Coding](agentic-coding.md)
- [How LLMS Work](how-llms-work.md)
