---
id: "01kjftepsxf9qmsy6jzeeye65h"
title: "90% of AI Users Are Getting Mediocre Output. Don't Be One of Them (Stop Prompting, Do THIS Instead)"
author: "AI News & Strategy Daily | Nate B Jones"
source_url: "https://youtube.com/watch?v=KX0GurmgAoo&si=sJHzhg6E-BneFncc"
category: "video"
tags: [ai]
saved_at: "2026-02-27T15:11:11.166000+00:00"
summarized_at: "2026-04-15T19:35:33Z"
---

# 90% of AI Users Are Getting Mediocre Output. Don't Be One of Them (Stop Prompting, Do THIS Instead)

**Original source:** [90% of AI Users Are Getting Mediocre Output. Don't Be One of Them (Stop Prompting, Do THIS Instead)](https://youtube.com/watch?v=KX0GurmgAoo&si=sJHzhg6E-BneFncc)
**Author:** AI News & Strategy Daily | Nate B Jones

## Summary

Nate B Jones argues that default AI output is inherently mediocre because LLMs are trained via reinforcement learning from human feedback (RLHF) to satisfy the broadest possible audience -- the statistical median user. Just as a chain pizza restaurant optimizes for inoffensiveness rather than delight, AI models learn to produce responses that a pool of human raters (not individual users) would score highest. The result is output that is technically competent but never truly personalized. Jones explains that this is not speculation but a well-documented consequence of the RLHF training process, published openly by both Anthropic and OpenAI.

The core thesis is that users must go beyond prompting and use four "levers" to escape the averaging effect. Lever 1, Memory, involves getting the AI to retain personal context across conversations -- ChatGPT uses saved memories and conversation history, Claude uses project-scoped memory with RAG-style retrieval, and Gemini connects to the Google ecosystem. Lever 2, Instructions, covers persistent behavioral guidance: custom instructions, project-specific instructions, and notably Claude's CLAUDE.md files for developers. Lever 3, Apps and Tools, addresses which external capabilities (web search, code execution, MCP servers) the AI can access, noting that tool configuration fundamentally shapes output character. Lever 4, Style and Tone Control, includes ChatGPT's personality presets and Claude's custom style profiles built from writing samples.

Jones emphasizes that vague instructions ("be concise") do not steer the model meaningfully; specificity is required. He cites Boris Chernny's practice of running multiple Claude instances and updating CLAUDE.md rules whenever Claude makes a mistake, shipping roughly 100 PRs per week. The compounding effect of encoding corrections into the system is what separates power users from those who find AI perpetually mediocre.

## Main Ideas

- Default AI output is optimized for the median user due to RLHF training, making it competent but impersonal.
- Four levers beyond prompting can customize AI: memory, instructions, apps/tools, and style controls.
- Memory implementations differ significantly across ChatGPT, Claude, and Gemini, with Claude emphasizing project-scoped isolation.
- CLAUDE.md files serve as living instruction documents for Claude Code that entire teams can maintain and evolve.
- Vague steering instructions are ineffective; specificity about context, constraints, and desired behavior is essential.
- The compounding effect of encoding corrections back into the AI system over time is what produces 10x results.
- Steering fixes personalization but does not fix hallucination or the creative ceiling of training-data-centered output.

## Key Quotes

- "Every time you use default settings, you're getting an answer optimized for a hypothetical typical person. The training literally encodes 'what would most people want here' as the target."
- "The people getting 10x results... capture the corrections and when they notice a pattern, they encode it back into the AI and add it to their instructions."
