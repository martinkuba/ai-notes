---
tags: [agents, systems, automation, futures]
---

# Agentic AI

AI systems that can autonomously plan, execute, and iterate on tasks — moving beyond single-turn chat interactions to multi-step workflows. Positioned as the "third wave" of AI after expert systems and neural networks.

See source: [The Third Wave Of AI Is Here](../summaries/the-third-wave-of-ai-is-here-why-agentic-ai-will-transform.md)

## Vision

Bill Gates described AI agents as personal assistants that replace app-based interfaces with natural language task execution — transforming healthcare, education, productivity, and commerce.

See source: [AI Is About To Completely Change How You Use Computers](../summaries/ai-is-about-to-completely-change-how-you-use-computers.md)

## Current Implementations

- **[Claude Code](claude-code.md)** — Agentic coding in the terminal
- **OpenAI Swarm** — Multi-agent coordination framework for getting AI to do things on your behalf. See source: [Openai Reveals Swarm A Breakthrough New Method](../summaries/openai-reveals-swarm-a-breakthrough-new-method-for-getting.md)
- **Google AI Co-Scientist** — Research-focused agent for scientific discovery. See source: [Google Unveils AI Co Scientist To Supercharge Research](../summaries/google-unveils-ai-co-scientist-to-supercharge-research.md)
- **Salesforce Agentforce** — Enterprise platform for building custom digital agents. See source: [Salesforce S New AI Platform](../summaries/salesforce-s-new-ai-platform-lets-companies-build-their-own.md)
- **Deep Research tools** — Agents that conduct multi-step research autonomously ([Deep Research](deep-research.md))
- **OpenClaw** — An autonomous agent architecture running an entire company: Jarvis (router), Atlas (research), Scribe (copywriter), Trendy (trend scout) for ~$400/month. See source: [This Army Of Openclaw Agents Runs An Entire Company](../summaries/this-army-of-openclaw-agents-runs-an-entire-company-for.md)
- **AI SRE** — A specialized Site Reliability Engineer agent built in 60 minutes using Claude and Grafana's gcx CLI. Narrow scope (one service domain) + skill-based architecture (alert playbooks, runbooks, past incidents) proved highly effective; false positive rate dropped below 10% after 4-5 investigations. Persistent, file-based knowledge bases that grow with each incident and integrate into PR workflows. Broad implication: this basic AI SRE capability will become a standard platform feature for every observability vendor. See source: [I Built An AI SRE In 60mins, You Should Too](../summaries/i-built-an-ai-sre-in-60mins-you-should-too.md)
- **AutoResearch** — [Andrej Karpathy](andrej-karpathy.md)'s concept of fully autonomous agent-driven research loops: agents optimize model hyperparameters and experiment setups without human intervention, discovering improvements missed by decades of manual tuning. Extends to "Program MDs" — entire research organizations abstracted as markdown documents that AI can optimize at the meta level. See source: [Skill Issue: Andrej Karpathy on Code Agents, AutoResearch, and the Loopy Era of AI](../summaries/skill-issue-andrej-karpathy-on-code-agents-autoresearch-and.md)

## Production Design Patterns

Most agent architectures fail in production because they're stateless and optimized for single-turn interactions. Real-world workflows — insurance claims, week-long sales sequences, financial reconciliation — require agents that maintain state and reasoning continuity over days. Google's Gemini Enterprise Agent Platform identifies five composable patterns for long-running agents:

- **Checkpoint-and-Resume** — Persist execution state to disk after logical work batches; treat agents like server processes, not request handlers
- **Delegated Approval (Human-in-the-Loop)** — Agents pause at approval gates with full context intact; zero compute consumed during pauses with sub-second cold starts
- **Memory-Layered Context** — Working memory (Memory Profiles) for low-latency access + long-term memory (Memory Bank) for cross-session knowledge; governed by Agent Identity, Registry, and Gateway
- **Ambient Processing** — Event-driven agents connected to data streams; policies externalized through Agent Gateway so updates propagate to entire fleets instantly
- **Fleet Orchestration** — Coordinator agent manages specialist agents, each with independent identity and versioning; enables updates without cascading failures

See source: [5 Agent Design Patterns For Long-Running AI Agents](../summaries/5-agent-design-patterns-for-long-running-ai-agents.md)

## Human Cognitive Limits

Managing multiple agents creates cognitive load — context and anxiety accumulate. Finding your personal ceiling for parallel agent sessions requires deliberate time-boxing and deep focus.

See source: [Tip Figure Out Your Personal Ceiling For Running Multiple Agents](../summaries/tip-figure-out-your-personal-ceiling-for-running-multiple.md)

## Fully Automated Firms

Dwarkesh Patel speculates on future organizations run entirely by AI agents — no human employees. Raises questions about ownership, accountability, and economic structure.

See source: [What Fully Automated Firms Will Look Like](../summaries/what-fully-automated-firms-will-look-like.md)

## Enterprise Roles: The Agent Deployer

As enterprises adopt AI agents, a new critical role is emerging: the **agent deployer and manager**. This person is a technical-business hybrid who identifies high-leverage workflows where agents can deliver 100x improvements in speed or scale (e.g., lead qualification, contract review, knowledge base creation). Key responsibilities include workflow design, data mapping, system integration (using [MCP](mcp.md), APIs, CLIs), human-in-the-loop interface design, and ongoing performance monitoring. The role will likely be distributed across teams rather than centralized, and represents a strong career opportunity for technically-minded engineers repositioning for the AI era.

See source: [The More Enterprises I Talk To About AI Agent Transformation](../summaries/the-more-enterprises-i-talk-to-about-ai-agent-transformation.md)

## Getting Started

Practical guidance for adopting agentic AI responsibly: start small, maintain human oversight, iterate on prompts, measure outcomes.

See source: [How To Get Started With AI Agents And Do It Right](../summaries/how-to-get-started-with-ai-agents-and-do-it-right.md)

## Economic Impact

Jack Clark (Anthropic co-founder) and Ezra Klein discuss the transition from AI "talkers" (2023-2024) to AI "doers" (2026-2027). The S&P 500 Software Industry index fell 20% as markets price in agent disruption. Sequoia frames it as: agents can now work together, oversee each other, and run in swarms — making it possible to have a "team of incredibly fast, somewhat peculiar software engineers" at your disposal.

See source: [How Fast Will A.I. Agents Rip Through The Economy](../summaries/how-fast-will-a-i-agents-rip-through-the-economy-the-ezra.md)

## Environment and Harness Design

The limiting factor in agent performance is not model capability but the "harness" — the complete designed environment in which the model operates. The SWE-agent research demonstrated 64% performance improvements through interface design alone, with identical underlying models. Key principles:

- **The interface is cognitive architecture**: Everything in the context window determines what the model can reason about. Format is not decoration.
- **Context window management**: Functions as working memory, not storage. Unbounded search results, stale state, and irrelevant data degrade reasoning.
- **Multi-session architecture**: Long-running projects need explicit scaffolding — persistent state files, progress logs, two-agent patterns (initializer + coder).
- **Feedback loops drive quality**: Immediate syntax checking, integrated linters, browser automation for end-to-end testing all improve output over delayed external feedback.
- **The execution layer is a commodity**: Foundation models generate functional code reliably. The real moat is orchestration, state management, and constraint enforcement.

See source: [The Harness Is Everything: What Cursor, Claude Code, and Perplexity Actually Built](../summaries/the-harness-is-everything-what-cursor-claude-code-and.md)

## Related

- [Agentic Coding](agentic-coding.md)
- [AI And Jobs](ai-and-jobs.md)
- [Deep Research](deep-research.md)
- [AGI Timelines](agi-timelines.md)
