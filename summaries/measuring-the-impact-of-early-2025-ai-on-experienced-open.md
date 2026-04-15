---
id: "01ke68th2djyx245kr4h49effy"
title: "Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity"
author: "METR"
source_url: "https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/"
category: "article"
tags: [ai]
saved_at: "2025-07-14T16:38:55+00:00"
summarized_at: "2026-04-15T19:50:48Z"
---

# Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity

**Original source:** [Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/)
**Author:** METR

## Summary

METR conducted a randomized controlled trial (RCT) to measure how early-2025 AI tools affect the productivity of experienced open-source developers working on their own repositories. The study recruited 16 developers from large open-source projects (averaging 22k+ stars and 1M+ lines of code) who completed 246 real issues — bug fixes, features, and refactors — randomly assigned to either allow or disallow AI tool usage. When AI was allowed, developers primarily used Cursor Pro with Claude 3.5/3.7 Sonnet.

The headline finding was surprising and counterintuitive: developers using AI tools took 19% longer to complete tasks, not faster. This directly contradicts developer self-perceptions — participants expected AI to speed them up by 24%, and even after experiencing the measured slowdown, they still believed AI had made them 20% faster. The study investigated 20 potential factors contributing to the slowdown and found evidence that 5 likely play a role. Importantly, the researchers ruled out many experimental artifacts: developers used frontier models, complied with treatment assignments, didn't selectively drop harder tasks, and submitted similar-quality PRs in both conditions.

The paper carefully avoids overgeneralization, noting this is a snapshot of one specific setting — experienced developers on familiar codebases using early-2025 tools. The researchers present three hypotheses for reconciling their findings with impressive AI benchmark scores and widespread anecdotal reports of AI helpfulness: (1) the RCT may underestimate capabilities due to methodological limitations, (2) benchmarks and anecdotes may overestimate capabilities, or (3) different methodologies may validly measure different subsets of the task distribution. METR plans to continue running similar studies to track how AI's impact on developer productivity evolves over time, particularly given implications for AI R&D acceleration and associated risks.

## Main Ideas

- Experienced open-source developers took 19% longer to complete real coding tasks when using AI tools compared to working without them — a statistically significant slowdown.
- There is a striking perception gap: developers believed AI sped them up by ~20% even when it actually slowed them down by 19%, providing strong evidence that self-reported AI productivity gains can be highly inaccurate.
- The slowdown persisted across different outcome measures, estimator methodologies, and data subsets, ruling out many potential experimental artifacts.
- Benchmark scores (like SWE-Bench) and real-world RCT results give partially contradictory evidence about AI capabilities, possibly because they measure different aspects of the task distribution under different conditions.
- The results apply specifically to experienced developers working on familiar, high-quality codebases with high standards — AI may be more helpful for less experienced developers or those in unfamiliar codebases.
- This methodology may be more resistant to gaming than benchmarks, making it valuable for tracking real-world AI capability trends over time.
- Understanding AI's impact on software development is important for estimating AI's potential to accelerate AI R&D itself, which carries significant safety implications.

## Key Quotes

- "When developers are allowed to use AI tools, they take 19% longer to complete issues — a significant slowdown that goes against developer beliefs and expert forecasts."
- "Developers expected AI to speed them up by 24%, and even after experiencing the slowdown, they still believed AI had sped them up by 20%."
- "We now have strong evidence that anecdotal reports/estimates of speed-up can be very inaccurate."
