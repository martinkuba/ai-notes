---
id: "01kj9daeze305hebqdxy89fxan"
title: "I'm using claude --worktree for everything now"
author: "Matt Pocock"
source_url: "https://www.youtube.com/watch?v=yv8VZpov8bk&list=WL&index=5"
category: "video"
tags: [ai]
saved_at: "2026-02-25T03:26:13.998000+00:00"
summarized_at: "2026-04-15T19:50:48Z"
---

# I'm using claude --worktree for everything now

**Original source:** [I'm using claude --worktree for everything now](https://www.youtube.com/watch?v=yv8VZpov8bk&list=WL&index=5)
**Author:** Matt Pocock

## Summary

Matt Pocock walks through his first experience using Claude Code's built-in git worktree support, which allows multiple AI agents to run in parallel without interfering with each other. He starts by explaining the basics of git worktrees -- how they create separate folders with independent git state, each on its own branch -- and demonstrates creating and managing worktrees manually via the terminal and VS Code's source control panel. He then moves on to testing `claude --worktree`, which automates the process by creating a worktree with a randomly generated name and letting the agent work within it.

During his experimentation, Pocock encounters a notable gotcha: by default, the worktree's branch tracks the parent branch (e.g., main), so if you push without specifying the worktree's branch name explicitly, commits can accidentally land on main rather than a separate feature branch. He discovers that the agent needs to push with `git push origin <worktree-branch-name>` to correctly create a new remote branch. He flags this as an important caveat, especially for repos where main is unprotected.

Despite this rough edge, Pocock is enthusiastic about the workflow. He sees Claude-managed worktrees as a natural fit for parallelizing AI-driven development -- each worktree maps to a single agent's lifecycle, enabling developers to spin up multiple independent tasks simultaneously and merge them back via PRs. He also highlights that sub-agents now support worktrees, enabling orchestrated parallel workflows. He connects this to broader themes from his upcoming Claude Code course, arguing that effective AI coding requires reintroducing software engineering fundamentals like TDD, planning, and parallelization into the AI-assisted workflow.

## Main Ideas

- Claude Code now has built-in git worktree support (`claude --worktree` or `claude -w`), enabling each agent to work in an isolated branch without conflicting with others.
- Git worktrees create separate folders with independent branch state, and VS Code's source control panel picks them up automatically.
- A key gotcha: the worktree branch tracks the parent branch by default, so you must explicitly push to the worktree's branch name to avoid accidentally committing to main.
- Worktrees tie the lifecycle of each work tree to a single agent's task, making parallelization of AI-driven development much more natural.
- Sub-agents also support worktrees, enabling orchestrated multi-agent workflows where each sub-agent creates its own PR.
- Pocock argues that AI coding still requires traditional software engineering fundamentals (TDD, planning, fast feedback loops) adapted for the AI era.
