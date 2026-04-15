---
id: "01kj0hekvcd3c7wx8x1yfrx9q8"
title: "Reflecting on what engineers love about Claude Code, one thing..."
author: "Boris Cherny"
source_url: "https://x.com/bcherny/status/2021699851499798911/?rw_tt_thread=True"
category: "tweet"
tags: [ai]
saved_at: "2026-02-21T16:45:14.476000+00:00"
summarized_at: "2026-04-15T19:53:49Z"
---

# Reflecting on what engineers love about Claude Code, one thing...

**Original source:** [Reflecting on what engineers love about Claude Code, one thing...](https://x.com/bcherny/status/2021699851499798911/?rw_tt_thread=True)
**Author:** Boris Cherny

## Summary

Boris Cherny, reflecting on what makes Claude Code popular among engineers, highlights customizability as a key differentiator. He argues that because every engineer uses their tools differently, Claude Code was built from the ground up not just with great defaults but with deep customization options. This philosophy of respecting individual workflow preferences is presented as a core reason for the product's accelerating growth.

Cherny walks through five specific customization areas. First, terminal configuration including themes, notifications, newline handling for different terminal emulators, and vim mode. Second, adjustable effort levels (low, medium, high) that let users trade off between speed and intelligence. Third, a plugin ecosystem supporting LSPs for every major language, MCPs, skills, agents, and custom hooks, installable from an official Anthropic marketplace or custom company marketplaces. Fourth, custom agents defined via markdown files with configurable names, colors, tool sets, permissions, and models. Fifth, a sophisticated permission system with prompt injection detection, static analysis, sandboxing, and human oversight, where users can pre-approve common commands using wildcard syntax and share these configurations across teams via settings.json.

## Main Ideas

- Claude Code's growth is driven by its deep customizability, not just its AI capabilities
- Engineers can configure terminal settings, effort levels, plugins/MCPs/skills, custom agents, and granular permissions
- Custom agents are defined as simple markdown files in `.claude/agents` with configurable properties
- The permission system combines automated security (prompt injection detection, static analysis, sandboxing) with human oversight
- Team-level configurations can be checked into version control via `settings.json` for consistent setup across organizations
- A plugin marketplace model allows both official Anthropic plugins and company-specific private marketplaces
