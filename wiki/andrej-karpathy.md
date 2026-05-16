---
tags: [people, coding, ai-research]
---

# Andrej Karpathy

AI researcher. Former Director of AI at Tesla, former OpenAI researcher. Influential voice on practical AI use and coding with AI agents.

## On Agentic Coding

Reports spending ~80% of coding time in agent-driven mode. Key observations:
- AI makes conceptual errors and tends toward over-complexity
- Coined "[vibe coding](vibe-coding.md)" for prompt-and-accept AI programming
- The "slopacolypse" — expects a flood of low-quality AI-generated code in 2026
- Despite risks, productivity gains are real (estimates ~10x for certain tasks)
- The transition requires vigilance in code review

See source: [A Few Random Notes From Claude Coding Quite A Bit](../summaries/a-few-random-notes-from-claude-coding-quite-a-bit.md)

## The Loopy Era: AutoResearch and 80–90% Delegation

In a 2026 interview, Karpathy describes a step-change beginning December 2024 — delegating 80-90% of coding to agents and entering what he calls "AI psychosis": perpetual exploration of what's newly possible. The work mode shifts from writing code to "manifesting will" through natural language across multiple coordinated agents.

**AutoResearch** is Karpathy's term for fully autonomous agent-driven research loops: agents optimize model hyperparameters and experimental setups without human intervention, discovering improvements he hadn't found in two decades of manual tuning. The implication is that humans are bottlenecks to scaling intelligence. He envisions extending this to entire research organizations described as markdown documents ("Program MDs") that can themselves be optimized by models — meta-level automation of institutional workflows.

**The jagged intelligence landscape**: current AI systems are superhuman on verifiable, reward-optimized tasks (code generation, hyperparameter search) but novice-level on subjective, context-dependent tasks (humor, nuance, clarification). This jaggedness reflects reinforcement-learning optimization paths rather than generalized intelligence gains.

Additional ideas:
- Agents should be the target audience for technical documentation, acting as content routers that then explain things to humans in customized ways
- AutoResearch could use distributed, untrusted worker pools (à la SETI@home) where result verification is cheap but generation is expensive
- Open-source models are 6-8 months behind frontier and converging, creating a healthy Linux-like ecosystem

See source: [Skill Issue: Andrej Karpathy on Code Agents, AutoResearch, and the Loopy Era of AI](../summaries/skill-issue-andrej-karpathy-on-code-agents-autoresearch-and.md)

## CLAUDE.md Rules

Karpathy's January 2026 complaints about Claude coding behavior — silent assumptions, over-engineering, orthogonal damage, weak success criteria — were crystallized by Forrest Chang into 4 CLAUDE.md rules that became the fastest-growing single-file repo of 2026. Independent testing showed these 4 rules reduced coding mistakes from ~41% to under 11% on aligned tasks. See [Claude Code](claude-code.md) for the extended 12-rule framework built on this foundation.

See source: [Karpathy's 4 CLAUDE.md Rules Cut Claude Mistakes From 41% to 11%](../summaries/karpathy-s-4-claude-md-rules-cut-claude-mistakes-from-41-to.md)

## Skills Profile

A curated list of Karpathy's technical skills and knowledge areas — useful as a reference for AI research competencies.

See source: [Github Forrestchang Andrej Karpathy Skills](../summaries/github-forrestchang-andrej-karpathy-skills.md)

## How I Use LLMs

Comprehensive tutorial on practical LLM use. Key explanations:
- LLMs as "lossy zip files" of internet knowledge — pre-training compresses the internet into ~1T parameters
- Post-training adds assistant persona via human-labeled conversations
- The context window as a shared token stream built collaboratively between user and model
- Knowledge cutoff as a fundamental limitation of the pre-training paradigm
- Tool use as the escape hatch for accessing current information

See source: [How I Use LLMs](../summaries/how-i-use-llms.md)

## Related

- [Agentic Coding](agentic-coding.md)
- [AI And Software Engineering Jobs](ai-and-software-engineering-jobs.md)
- [How LLMS Work](how-llms-work.md)
