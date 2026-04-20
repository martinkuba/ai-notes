---
id: "01kpkdeg6pdf5fszsskfmqtdze"
title: "Changes in the system prompt between Claude Opus 4.6 and 4.7"
author: "Simon Willison"
source_url: "https://simonwillison.net/2026/Apr/18/opus-system-prompt/"
category: "article"
tags: [ai]
saved_at: "2026-04-19T17:43:37.856000+00:00"
summarized_at: 2026-04-20T00:21:39Z
---

# Changes in the system prompt between Claude Opus 4.6 and 4.7

**Original source:** [Changes in the system prompt between Claude Opus 4.6 and 4.7](https://simonwillison.net/2026/Apr/18/opus-system-prompt/)
**Author:** Simon Willison

## Summary

Anthropic's publication of system prompts for Claude models provides valuable insight into how AI systems evolve. Between Claude Opus 4.6 (February 2026) and 4.7 (April 2026), the system prompt underwent significant refinements reflecting improvements in model behavior and expanded capabilities. The changes reveal a pattern of making Claude less pushy, more concise, and better at using tools autonomously. Notable updates include expanded child safety guardrails with a critical new instruction that subsequent requests following a child safety refusal must be approached with extreme caution. The prompt now includes mechanisms for Claude to search for available tools before claiming a capability doesn't exist, reducing false negatives about what the system can do. New guidance encourages Claude to be more proactive in disambiguating user requests using available tools rather than asking clarifying questions. Several behavioral directives from the 4.6 prompt were removed, indicating the newer model no longer exhibits those problematic behaviors, such as excessive use of emotes or certain verbal hedges.

## Main Ideas

- The platform rebranding from "developer platform" to "Claude Platform" and new tool integrations (Claude in PowerPoint, Claude in Chrome, Claude in Excel) are now explicitly mentioned in system prompts
- Child safety instructions have been significantly strengthened with new critical tags and a requirement for extreme caution in subsequent requests after safety refusals
- Claude is now encouraged to use `tool_search` to verify available capabilities before claiming limitations, reducing false negatives about system abilities
- The system prompt now instructs Claude to be more concise and focused, avoiding unnecessarily verbose responses with extensive disclaimers
- New safeguards against "screenshot attacks" that force yes/no answers to complex questions, encouraging nuanced responses instead
- Claude 4.6's explicit statement about Trump being president has been removed, reflecting the model's updated knowledge cutoff to January 2026
- A new section on disordered eating guidance prevents specific nutrition/diet/exercise recommendations when users show concerning signs

## Key Quotes

> "When a request leaves minor details unspecified, the person typically wants Claude to make a reasonable attempt now, not to be interviewed first. Claude only asks upfront when the request is genuinely unanswerable without the missing information."

> "Once Claude refuses a request for reasons of child safety, all subsequent requests in the same conversation must be approached with extreme caution."

> "Claude keeps its responses focused and concise so as to avoid potentially overwhelming the user with overly-long responses."