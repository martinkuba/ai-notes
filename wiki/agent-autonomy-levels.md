---
tags: [agents, autonomy, orchestration, verification]
---

# Agent Autonomy Levels

A two-axis framework by [Addy Osmani](addy-osmani.md) for reasoning about how much independence to grant AI agents. It reframes Steve Yegge's single-axis autonomy scale, which conflates two separate questions: how independently *one* agent can operate (**agency**) and how well an organization can coordinate *many* agents at once (**orchestration**). Systems like [Claude Code](claude-code.md) and Codex require managing both dimensions separately.

See source: [Agentic Autonomy Levels](../summaries/agentic-autonomy-levels.md)

## Six Levels of Organizational Maturity

0. **Assist** — agent makes suggestions; human executes
1. **Supervised execution** — agent executes, human watches closely
2. **Scoped delegation** — bounded tasks delegated with monitoring
3. **Goal-driven** — agent pursues a measurable goal autonomously
4. **Parallel agents** — multiple agents coordinated on isolated work
5. **Managed-by-exception** — a manager agent dispatches work across hundreds or thousands of workers; humans intervene only on exceptions

## What Actually Determines the Right Level

The appropriate autonomy level depends not on the task's name but on three questions:

- **How quickly can errors be detected?**
- **How easily can changes be undone?**
- **What evidence can independently verify success?**

These three factors — detection speed, reversibility, and verifiability — are the real inputs to a defensible autonomy decision, not the task category.

## Contracts Precede Execution

Every agent run should be preceded by a formal contract specifying:

- Goal and scope (including non-goals)
- Allowed tools
- Stopping conditions
- Success evidence
- Escalation policy
- Resource budget

This shifts teams away from approval-gate fatigue (checking every step) toward evidence-based trust (checking the right things). It parallels the harness-level discipline described in [Agent Harness](agent-harness.md), but operates one level up — as a policy for *when* and *how far* to let an agent run, rather than the scaffolding it runs inside.

## Metrics for Calibration

- Mean time between interventions
- Approval rates
- Defect escape rates
- Token cost per change

Tracking these lets teams detect drift — whether the actual risk of a workflow has outpaced the autonomy level assigned to it.

## Four Anti-Patterns

- **Autonomy-as-status** — granting higher autonomy levels as a reward or signal of trust rather than as a response to reversibility and verifiability
- **Permission laundering** — nominally requiring approval while the approval step is rubber-stamped, so real autonomy is higher than the stated level
- **Summary substitution** — reviewing an agent's self-generated summary of its work instead of the work itself
- **Fleet cosplay** — running many agents in parallel without the orchestration maturity (Level 4-5 tooling) to actually manage them, producing the appearance of scale without its benefits

Each requires a structural fix (boundaries, sandboxes, actual review, better orchestration tooling), not simply "more trust."

## Core Insight: Verification Is the Bottleneck

High autonomy does not mean removing humans from the loop. It means moving them from executing every step to deciding direction, supported by defensible evidence. This is the same conclusion reached from a different angle in [Orchestration Tax](orchestration-tax.md): the constraint on scaling agent usage is never agent capability, it's how fast and how well humans (or independent evidence) can verify outcomes.

> "Verification will always be the bottleneck."

## Related

- [Addy Osmani](addy-osmani.md) — author of this framework
- [Orchestration Tax](orchestration-tax.md) — the review-capacity bottleneck this framework formalizes into levels
- [Agent Harness](agent-harness.md) — the scaffolding that contracts are layered on top of
- [Agentic AI](agentic-ai.md) — Delegated Approval and Fleet Orchestration patterns map onto Levels 2-5
- [Agentic Coding](agentic-coding.md) — practical multi-agent management this framework generalizes
