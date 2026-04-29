---
id: "01kqabzk85mesdg4621sw8qc5m"
title: "I built an AI SRE in 60mins, you should too"
author: "Goutham City"
source_url: "https://www.gouthamve.dev/i-built-an-ai-sre-in-60mins-you-should-too/"
category: "article"
tags: [ai, work]
saved_at: "2026-04-28T15:40:32.901000+00:00"
summarized_at: 2026-04-29T00:00:04Z
---

# I built an AI SRE in 60mins, you should too

**Original source:** [I built an AI SRE in 60mins, you should too](https://www.gouthamve.dev/i-built-an-ai-sre-in-60mins-you-should-too/)
**Author:** Goutham City

## Summary

The author describes building a specialized AI Site Reliability Engineer (SRE) in under 60 minutes using Claude and Grafana's gcx CLI tool. Rather than attempting to build a general-purpose incident investigation system, the author focused on a narrow scope covering only the services they were directly on-call for—the Faro frontend observability product backend. The system uses a skill-based architecture with structured knowledge bases including alert playbooks, cluster topology, runbooks, and a growing repository of past incident write-ups.

The AI SRE works by accessing observability data through gcx queries and applying curated operational knowledge to investigate alerts and identify root causes. After the initial 4-5 investigations where the author manually guided Claude, the system became highly effective at pattern matching and automatically updating knowledge bases and runbooks as it encounters new incidents. The false positive rate dropped below 10%, and the tool has been adopted across the team for troubleshooting instead of manual Grafana UI exploration.

The author notes that this approach works exceptionally well for typical backend services with limited failure modes (stateless components, simple dependencies), which represents approximately 95% of services in most organizations. The system's effectiveness stems from combining access to codebases, curated runbooks, and a persistent memory system that learns from each incident resolution.

## Main Ideas

- **Narrow scope is powerful**: Building an AI SRE specialized to a specific service domain is far more effective than attempting a general-purpose solution, and most services have only a handful of failure modes
- **Skill-based architecture**: Using a structured skill definition with reference materials and a knowledge base allows Claude to leverage observability tools (gcx) systematically while learning from incidents
- **Learning from incidents**: The system improves iteratively by updating playbooks, adding incident write-ups, and discovering new patterns after each investigation
- **Code and observability context**: Providing access to the codebase allows the AI to build dependency graphs and make intelligent connections between error types and relevant metrics
- **Persistent, reviewable knowledge**: Using file-based knowledge bases that integrate with PR workflows enables governance and crowdsourcing improvements across teams
- **Practical limitations to understand**: The system currently lacks good change/deployment visibility, cross-service investigation capabilities, and automatic triggering
- **Broad market opportunity**: The simplicity of building functional AI SREs suggests many observability vendors will incorporate this as a standard platform feature

## Key Quotes

> "Claude is excellent at leveraging it, and honestly, **my visits to the Grafana UI decreased significantly**!"

> "After it had 4-5 investigations under its belt, it got extremely effective and was usually spot on."

> "I think it's not that difficult to build a system that can connect to your GitHub and then build this context for each service. And it'll even help you keep your runbooks up to date... This basic but *decent* AI SRE capability will become a platform feature for every observability vendor."