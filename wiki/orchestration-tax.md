---
tags: [agents, cognitive-limits, orchestration, productivity]
---

# Orchestration Tax

A concept coined by [Addy Osmani](addy-osmani.md) to describe the hidden cost of scaling AI agent usage. Spawning agents is trivially easy; closing the loop — reviewing, verifying, and merging their output — is strictly serial and bottlenecked by human judgment.

See source: [The Orchestration Tax](../summaries/the-orchestration-tax.md)

## The Core Argument

The human is the GIL (Global Interpreter Lock) of their AI agents. Agents can all run in parallel, but any work requiring genuine architectural understanding, conflict resolution, or quality judgment must acquire the lock — and there is exactly one lock. [Amdahl's Law](https://en.wikipedia.org/wiki/Amdahl%27s_law) applies directly: the speedup from parallelizing agent work is capped by the serial fraction, which is human judgment. More agents don't increase throughput — they deepen the review queue.

> "Running multiple agents does not mean there is more of you. Your cognitive bandwidth doesn't parallelize."

This is not a willpower problem. It's an architecture problem, best understood through the lens of concurrent systems.

## Consequences

- **Feeling productive ≠ being productive.** A dashboard full of running agents generates the sensation of output while the actual bottleneck — review — stalls.
- **Cognitive debt compounds.** Merged work that wasn't fully understood accumulates silently. The debt isn't in the code; it's in the engineer's head.
- **Context switching multiplies the cost.** Jumping between agent threads requires expensive mental context reloads that compound with agent count. See [Your Parallel Agent Limit](../summaries/your-parallel-agent-limit.md) — the typical ceiling is 3-4 threads before review quality degrades.

## The Solution: Attention as an Architectural Resource

Rather than maximizing agent count to match UI capability, scale the fleet to your *review rate* (typically low single digits). Practical implications:

- Sort work by whether human judgment is central or peripheral to it
- Batch reviews to minimize context switching
- Reserve human involvement for decisions machines cannot verify — let agents write tests and generate proofs for the routine 80%
- Treat attention the way you treat any scarce production resource: budget it, protect it, route work through it efficiently

## Relationship to Long-Running Agents

The orchestration tax and [long-running agents](agentic-ai.md) are complementary — but they address different components of the cost.

**Review volume is conserved.** A long-running agent that works for 10 hours produces the same output whether you review it in one batch at the end or at 10 checkpoints along the way. Total review work doesn't shrink. Long-running agents don't solve that part of the tax.

**What they do address is thread count and context-switching cadence** — the other half of the tax:

| | Short agents, many parallel | Long-running agents, fewer parallel |
|---|---|---|
| **Simultaneous thread count** | High | Low |
| **Context switching cost** | High — unpredictable completions | Low — checkpoints at designed times |
| **Ambient anxiety tax** | High — many things unmonitored | Lower — fewer threads to track |
| **Total review volume** | Same | Same |

Running 3 long-running agents instead of 10 short ones means 3 mental models to maintain, not 10. The "ambient anxiety tax" — background worry about what unmonitored threads might be getting wrong — scales with thread count, not review volume. And because checkpoints are designed rather than reactive, you can batch reviews instead of context-switching every time an agent finishes.

The **Delegated Approval** pattern makes this concrete: the agent pauses at a defined gate with full state intact; you review with complete context; the agent resumes. You control *when* lock acquisitions happen rather than reacting to unpredictable agent completions.

## What to Learn and Practice

1. **Scale fleet to review rate, not UI capability.** Your throughput ceiling is how fast you can review, not how many agents the platform supports.
2. **Design pause points explicitly.** Use the Delegated Approval pattern — build natural checkpoints where the agent hands off complete, reviewable state.
3. **Batch reviews to reduce context switching.** Treat agent review like code review: block time, don't interrupt.
4. **Know your cognitive ceiling.** Osmani's typical ceiling is 3-4 threads; [Addy Osmani](addy-osmani.md) and Simon Willison both report exhaustion-by-11am at higher counts.
5. **Shift toward depth to reduce thread count, not review volume.** Fewer long-running agents means fewer simultaneous contexts to hold — which directly reduces context switching cost and ambient anxiety. Total review work stays the same; the shape of when and how you do it improves. See [Agentic AI](agentic-ai.md).

## Related

- [Agentic AI](agentic-ai.md) — Long-running agent architectures, production patterns, memory systems
- [Agent Harness](agent-harness.md) — Scaffolding that determines review quality and agent reliability
- [Agentic Coding](agentic-coding.md) — Practical application to software development
- [Addy Osmani](addy-osmani.md) — Coined the concept; also coined "comprehension debt" and "ambient anxiety tax"
