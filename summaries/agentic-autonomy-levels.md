---
id: "01kwm69m8pbp53gd4az2nt5xvv"
title: "Agentic Autonomy Levels"
author: "Addy Osmani from Elevate"
source_url: "mailto:reader-forwarded-email/6ff9e18886702dcd2594ac95372c869f"
category: "email"
tags: [ai]
saved_at: "2026-07-03T14:32:03.606000+00:00"
summarized_at: "2026-07-08T00:00:05Z"
---

# Agentic Autonomy Levels

**Author:** Addy Osmani from Elevate

## Summary

This piece proposes a six-level framework for understanding AI agent autonomy, moving beyond single-axis models to capture both individual agent agency and multi-agent orchestration. The levels progress from Level 0 (Assist—suggestions requiring human approval) through Level 5 (Managed-by-exception orchestration—manager agents dispatching workers autonomously). The key insight is that autonomy decisions should be guided by risk and reversibility: how quickly you'll know something is wrong, how cleanly you can undo it, and what evidence proves it worked. High autonomy doesn't remove humans from decision-making; it shifts them from executing every step to deciding direction. The author emphasizes that verification is the bottleneck and proposes concrete contracts for each agent run that define goals, scope, constraints, stopping conditions, evidence, and escalation paths.

## Main Ideas

- **Two separate dimensions**: Agency (how far the agent goes) and orchestration (coordinating many agents) should be measured separately rather than collapsed onto a single ladder
- **Six autonomy levels**: Range from assisted suggestions to full orchestration with hundreds of agents, each with distinct failure modes and verification requirements
- **Risk-driven autonomy**: Set autonomy levels based on reversibility, error cost, and measurable stopping conditions—not task type alone
- **Humans stay in the loop**: Even high autonomy systems require humans for ~30% of planning decisions; the shift is from doing every step to steering direction
- **Contracts define safety**: Each agent run needs a documented contract specifying goals, scope, non-goals, tools, stopping conditions, evidence metrics, escalation rules, and budgets
- **Verification is the constraint**: Three questions determine whether high autonomy is defensible—how quickly will we know we're wrong, how cleanly can we undo it, what proves we're right
- **Four anti-patterns to avoid**: Autonomy as status, permission laundering, summary substitution (skipping real review), and fleet cosplay (manual orchestration of parallel agents)
- **Calibrated autonomy**: The mature approach is choosing the correct level for each task and building evidence patterns that support that choice

## Key Quotes

> "High autonomy is not about leaving people out of the loop, but moving from having them do every step to having them decide which direction to go next."

> "If we want to determine whether a large AI system is operating with high autonomy, the three questions we should be asking are: How quickly will we know we're wrong about what it's doing? How cleanly can we undo what it's doing? What would prove we're right about what it's doing?"

> "Every run of an agent should be preceded by a contract that defines what it's trying to do."
