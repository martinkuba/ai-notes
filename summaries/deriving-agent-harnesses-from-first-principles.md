---
id: "01kr9dpd6t5akntxcdhmxwyphj"
title: "Deriving Agent Harnesses from First Principles"
author: "Viv"
source_url: "https://x.com/vtrivedy10/status/2031408954517971368/?s=12&t=lja9AMD11WXSlUvoMkbJMw&rw_tt_thread=True"
category: "tweet"
tags: [ai]
saved_at: "2026-05-10T17:06:56.346000+00:00"
summarized_at: "2026-05-12T00:22:20Z"
---

# Deriving Agent Harnesses from First Principles

**Original source:** [Deriving Agent Harnesses from First Principles](https://x.com/vtrivedy10/status/2031408954517971368/?s=12&t=lja9AMD11WXSlUvoMkbJMw&rw_tt_thread=True)
**Author:** Viv

## Summary

An agent is fundamentally the composition of a language model and a "harness"—all code, configuration, and execution logic beyond the model itself. The harness provides essential capabilities that models lack natively: durable state maintenance, code execution, real-time knowledge access, and environment setup. By working backward from desired agent behaviors, the author derives core harness primitives and explains why each is necessary for practical autonomous work.

The foundational harness components include filesystems for storage and multi-agent collaboration, bash/code execution as a general-purpose tool for autonomous problem-solving, and sandboxes that provide safe execution environments with appropriate tooling. To enable long-horizon work, harnesses must manage context efficiency through compaction and progressive tool disclosure, while maintaining state through git versioning and planning. The harness and model training co-evolve in a feedback loop—useful primitives discovered in harnesses get incorporated into model training—but harness optimization for specific tasks remains valuable regardless of base model capability.

## Main Ideas

- **Agent formula**: Agent = Model (intelligence) + Harness (system that makes intelligence useful)
- **Core model limitations**: Models cannot maintain durable state, execute code, access real-time knowledge, or set up environments without harness support
- **Filesystem as foundational primitive**: Enables durable storage, context offloading, incremental work, and natural multi-agent collaboration surfaces
- **Bash/code execution as general-purpose tool**: Lets agents design and execute their own solutions autonomously rather than being constrained to pre-configured tools
- **Sandboxes for safe execution**: Isolated environments with configurable defaults, security controls, and rich tooling (runtimes, git, browsers, test runners) for verification
- **Context management as core concern**: Harnesses address context rot through compaction, tool output offloading, and progressive disclosure of tools via "skills"
- **Long-horizon work composition**: Requires filesystem tracking, git versioning, explicit planning, and self-verification loops to maintain coherence across multiple context windows
- **Model-harness co-evolution**: Training models with harnesses creates feedback loops that improve capability but can cause overfitting to the training harness
- **Harness engineering persists**: Like prompt engineering, harness optimization will remain valuable even as models improve, enabling better systems around any base intelligence

## Key Quotes

- "If you're not the model, you're the harness."
- "The model contains the intelligence and the harness is the system that makes that intelligence useful."
- "Harnesses today are largely delivery mechanisms for good context engineering."
