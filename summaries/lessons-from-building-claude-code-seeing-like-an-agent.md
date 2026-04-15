---
id: "01kjjggfw476g2r6gpba4krhkf"
title: "Lessons from Building Claude Code: Seeing like an Agent"
author: "Thariq"
source_url: "https://x.com/trq212/status/2027463795355095314/?rw_tt_thread=True"
category: "tweet"
tags: [ai]
saved_at: "2026-02-28T16:15:07.139000+00:00"
summarized_at: "2026-04-15T19:50:48Z"
---

# Lessons from Building Claude Code: Seeing like an Agent

**Original source:** [Lessons from Building Claude Code: Seeing like an Agent](https://x.com/trq212/status/2027463795355095314/?rw_tt_thread=True)
**Author:** Thariq

## Summary

This thread from Thariq, a builder of Claude Code at Anthropic, shares practical lessons about designing the tool and action space for an AI coding agent. The central insight is that designing tools for an agent is as much an art as a science -- you must "see like an agent" by reading its outputs, experimenting with different tool designs, and understanding what the model can and cannot do well. The thread walks through several concrete examples from Claude Code's development that illustrate this philosophy.

The first case study covers the evolution of the AskUserQuestion tool, which went through three iterations: adding question parameters to an existing ExitPlanTool (which confused the model), modifying Claude's output format to include structured questions (which was unreliable), and finally creating a dedicated tool that Claude calls to present structured questions to the user. The key lesson is that even well-designed tools fail if the model doesn't understand how to call them. The second example tracks the transition from TodoWrite (a simple checklist to keep the model on track) to the Task Tool, which supports dependencies, subagent coordination, and dynamic modification -- reflecting how improving model capabilities can make previously helpful tools into constraints.

The thread also describes the evolution of Claude Code's search capabilities, from a RAG vector database (fragile, required setup, and gave context to Claude rather than letting it find context itself) to giving Claude a Grep tool for self-directed codebase search. This led to the concept of "progressive disclosure" -- letting agents incrementally discover relevant context through exploration, such as reading skill files that reference other files recursively. Progressive disclosure was later used to add Claude Code self-knowledge through a Guide subagent rather than bloating the system prompt. Claude Code currently has approximately 20 tools, and the bar for adding new ones is high because each additional tool adds cognitive load for the model.

## Main Ideas

- Designing an agent's action space requires empathy with the model -- you must "see like an agent" and iterate based on what the model actually does with the tools.
- Tool design went through multiple iterations for features like elicitation (AskUserQuestion), showing that the best tool is one the model naturally understands how to call.
- As model capabilities improve, tools that once helped may become constraining -- the shift from TodoWrite to the Task Tool reflects this evolution.
- Claude Code moved from RAG-based context injection to letting the model build its own context through search tools (Grep), which improved as models got smarter.
- "Progressive disclosure" is a key pattern: letting agents incrementally discover context through exploration rather than front-loading everything in the system prompt.
- The bar for adding new tools is high (~20 tools currently) because each tool adds one more option for the model to consider, increasing cognitive load.
- Tool design depends heavily on the specific model, the agent's goal, and the operating environment -- there are no rigid universal rules.

## Key Quotes

- "You want to give it tools that are shaped to its own abilities. But how do you know what those abilities are? You pay attention, read its outputs, experiment. You learn to see like an agent."
- "Even the best designed tool doesn't work if Claude doesn't understand how to call it."
- "As model capabilities increase, the tools that your models once needed might now be constraining them."
