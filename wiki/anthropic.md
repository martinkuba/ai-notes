---
tags: [companies, anthropic, claude, safety]
---

# Anthropic

AI safety company. Creator of Claude. Founded by [Dario Amodei](dario-amodei.md) and Daniela Amodei (former OpenAI researchers). Positions itself as safety-focused but navigates tensions between commercial pressure and safety commitments.

## Products

- **Claude** — Foundation model family (Opus, Sonnet, Haiku)
- **[Claude Code](claude-code.md)** — Agentic coding tool
- **Claude Artifacts** — No-code app creation. See source: [Create AI Powered Apps With Claude Artifacts No Coding](../summaries/create-ai-powered-apps-with-claude-artifacts-no-coding.md)

## Safety Stance

A complex and evolving picture:
- Drew red lines against mass surveillance and autonomous weapons in Pentagon negotiations, even under threat of blacklisting. See source: [Anthropic Says Pentagon S Final Offer Is Unacceptable](../summaries/anthropic-says-pentagon-s-final-offer-is-unacceptable.md)
- Reportedly departed from earlier flagship safety pledges. See source: [Exclusive Anthropic Drops Flagship Safety Pledge](../summaries/exclusive-anthropic-drops-flagship-safety-pledge.md)
- Researchers question whether they fully understand Claude's capabilities. See source: [Do The People Building The AI Chatbot Claude Understand](../summaries/do-the-people-building-the-ai-chatbot-claude-understand.md)

## Technical Capabilities

- Claude Opus 4.6 uncovered 500+ zero-day vulnerabilities in open-source code. See source: [Anthropic S Claude Opus 4 6 Uncovers 500 Zero Day Flaws In Open Source Code](../summaries/anthropic-s-claude-opus-4-6-uncovers-500-zero-day-flaws-in.md)
- Extended thinking for complex reasoning. See source: [Claude S Extended Thinking](../summaries/claude-s-extended-thinking.md)
- Long context window prompting. See source: [Prompt Engineering For Claude S Long Context Window](../summaries/prompt-engineering-for-claude-s-long-context-window.md)

## Model Evolution

Simon Willison's analysis of system prompt changes between Claude Opus 4.6 (Feb 2026) and 4.7 (Apr 2026) reveals how model behavior evolves: Claude 4.7 is less pushy, more concise, better at autonomous tool use. Notable changes include strengthened child safety guardrails, a new `tool_search` mechanism to reduce false negatives about capabilities, new safeguards against "screenshot attacks" forcing yes/no answers, and guidance against excessive disclaimers. Behavioral directives that were removed indicate the newer model no longer exhibits those specific problems. The platform was also rebranded from "developer platform" to "Claude Platform" with new integrations (PowerPoint, Chrome, Excel).

See source: [Changes In The System Prompt Between Claude Opus 4.6 And 4.7](../summaries/changes-in-the-system-prompt-between-claude-opus-4-6-and-4-7.md)

## Related

- [Dario Amodei](dario-amodei.md)
- [Claude Code](claude-code.md)
- [AI Safety](ai-safety.md)
