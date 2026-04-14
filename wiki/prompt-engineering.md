---
tags: [prompting, techniques, practical]
---

# Prompt Engineering

The practice of crafting inputs to AI systems to get better outputs. Ranges from simple conversational techniques to structured methodologies for complex tasks.

## Getting Started: Good Enough Prompting

Ethan Mollick argues against over-engineering prompts. For most tasks, a clear, natural language description works well. The key insight: just start using AI and iterate — perfection is the enemy of adoption.

See source: [[sources/getting-started-with-ai-good-enough-prompting]]

## When to Use AI (and When Not)

Mollick's framework:
- **Use AI for**: idea generation, drafting, summarization, specialized domain work, brainstorming, formatting
- **Avoid AI for**: tasks where learning matters, high-accuracy requirements, tasks where effort itself is the point

See source: [[sources/15-times-to-use-ai-and-5-not-to]]

## Thinking Like an AI

Framing problems the way AI systems process them improves results. Understanding token prediction, context windows, and model tendencies helps craft better prompts.

See source: [[sources/thinking-like-an-ai]]

## Long Context Prompting

Specific techniques for leveraging Claude's extended context window: document placement, structured queries, XML tags for organization.

See source: [[sources/prompt-engineering-for-claude-s-long-context-window]]

## Technical: How Prompts Are Processed

GitHub Copilot's pipeline reveals prompt engineering at scale: snippet extraction from open files, context dressing (wrapping code in natural language cues), priority scoring to fit context windows.

See source: [[sources/a-developer-s-guide-to-prompt-engineering-and-llms]]

## The Wait Calculation Trap

Mollick warns against the "lazy tyranny of the wait calculation" — procrastinating AI adoption because something better is always around the corner. The opportunity cost of waiting exceeds the cost of using imperfect tools now.

See source: [[sources/the-lazy-tyranny-of-the-wait-calculation]]

## Related

- [[spec-driven-development]]
- [[agentic-coding]]
- [[how-llms-work]]
