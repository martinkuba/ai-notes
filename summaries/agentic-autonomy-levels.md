---
id: "01kwm69m8pbp53gd4az2nt5xvv"
title: "Agentic Autonomy Levels"
author: "Addy Osmani from Elevate"
source_url: "mailto:reader-forwarded-email/6ff9e18886702dcd2594ac95372c869f"
category: "email"
tags: [ai]
saved_at: "2026-07-03T14:32:03.606000+00:00"
summarized_at: "2026-07-05T00:00:02Z"
---

# Agentic Autonomy Levels

**Author:** Addy Osmani from Elevate

## Summary

This framework reimagines AI agent autonomy as a two-dimensional problem rather than a single ladder. The author argues that Steve Yegge's single-axis autonomy scale conflates two separate questions: how independently a single agent can operate (agency) and how well an organization can coordinate multiple agents (orchestration). Real-world agentic systems—including Claude Code and Codex—require both dimensions to be managed separately, yet most autonomy debates treat them as one.

The piece defines six autonomy levels (0–5) reflecting how organizations typically mature in their use of AI agents. These range from Level 0 (agent as assistant making suggestions) through Level 2 (delegating bounded tasks with monitoring), Level 3 (pursuing measurable goals autonomously), and Level 4 (coordinating parallel agents on isolated work) to Level 5 (managed-by-exception orchestration, where a manager agent dispatches work across hundreds or thousands of workers). However, the appropriate level for any task depends not on the task name but on three factors: how quickly errors can be detected, how easily changes can be undone, and what evidence can independently verify success.

The author proposes that every agent execution should be preceded by a formal "contract" specifying the goal, scope, allowed tools, stopping conditions, success evidence, escalation policies, and resource budgets. Supporting this contract are metrics—mean time between interventions, approval rates, defect escape rates—that let teams calibrate autonomy safely. The essay also identifies four systemic anti-patterns (autonomy-as-status, permission laundering, summary substitution, fleet cosplay) that undermine these systems if unchecked. The core insight: verification is the bottleneck, not capability; high autonomy means moving humans from executing every step to deciding direction based on defensible evidence.

## Main Ideas

- **Two-axis model replaces single ladder**: Separate agency (how independently agents act) from orchestration (coordinating multiple agents); most autonomy debates incorrectly treat these as one dimension.

- **Six-level progression matches organizational maturity**: Level 0 (assist), Level 1 (supervised execution), Level 2 (scoped delegation), Level 3 (goal-driven), Level 4 (parallel agents), Level 5 (managed-by-exception)—teams naturally progress through these phases.

- **Risk and reversibility determine appropriate autonomy, not task type**: Three key questions define defensible autonomy: How quickly will we know we're wrong? How cleanly can we undo it? What independent evidence proves success?

- **Contracts precede execution**: Every agent run needs a formal specification of goal, scope, non-goals, permitted tools, stopping condition, success evidence, escalation policies, and resource budget; this shifts from approval-gate fatigue to evidence-based trust.

- **Four anti-patterns systematically fail**: Autonomy-as-status, permission laundering, summary substitution, and fleet cosplay each require specific design fixes (boundaries, sandboxes, actual review, better orchestration) rather than harder trust.

- **Metrics enable safe calibration**: Track mean time between interventions, auto-approval rates, token costs per change, and defect escape rates to detect whether autonomy level matches actual risk and to catch drift over time.

- **Verification, not capability, is the bottleneck**: High autonomy is not removing humans from the loop; it's moving them from executing every step to deciding direction, supported by testable evidence and independent reviewers.

## Key Quotes

- "How far away from yourself are we letting this single agent go, and what is our skill at coordinating many agents?"

- "High autonomy is not about leaving people out of the loop, but moving from having them do every step to having them decide which direction to go next."

- "Every run of an agent should be preceded by a contract that defines what it's trying to do."

- "Verification will always be the bottleneck."
