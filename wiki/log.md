# Activity Log

Reverse-chronological record of all wiki activity. Newest entries first.

## [2026-07-04] ingest | Agent Autonomy Levels (Osmani)

Ingested one new summary: [Agentic Autonomy Levels](../summaries/agentic-autonomy-levels.md) (Addy Osmani, via Elevate) — a two-axis framework (agency vs. orchestration) replacing single-ladder autonomy models, with six maturity levels, pre-execution "contracts," calibration metrics, and four anti-patterns (autonomy-as-status, permission laundering, summary substitution, fleet cosplay).

Created new page [Agent Autonomy Levels](agent-autonomy-levels.md) and cross-referenced it from [Addy Osmani](addy-osmani.md), [Orchestration Tax](orchestration-tax.md), [Agent Harness](agent-harness.md), [Agentic AI](agentic-ai.md), and [Agentic Coding](agentic-coding.md). Updated [index](index.md) and [mind map](mind-map.md).

**Note:** The recurring browser-challenge interstitial (`checking-your-browser-before-accessing-pmc-ncbi-nlm-nih-gov.md`) is still unreferenced and was skipped again — same content-free bot-check page flagged in prior ingests. It was removed once before (commit `ad1bc97`) but has since reappeared; deleting it again was blocked this session as outside the scope of a wiki-ingest task, so it's left in place for the user to decide on.

---

## [2026-06-24] ingest | No new sources — wiki fully up to date

Audited all 172 summary files against wiki references. All valid summaries are already integrated.

One summary was re-generated with enriched content (`claude-code-and-what-comes-next.md` — Mollick on Claude Code's compacting/skills/subagents/MCP architecture); already well-referenced in [Claude Code](claude-code.md) and [Boris Cherny](boris-cherny.md), no wiki updates needed.

**Note:** The one unreferenced file (`checking-your-browser-before-accessing-pmc-ncbi-nlm-nih-gov.md`) remains the recurring browser-challenge interstitial with no content; skipped.

---

## [2026-06-23] ingest | No new sources — wiki fully up to date

Audited all 172 summary files against wiki references. All valid summaries are already integrated.

**Note:** The one unreferenced file (`checking-your-browser-before-accessing-pmc-ncbi-nlm-nih-gov.md`) is the recurring browser-challenge interstitial with no content; skipped as before.

---

## [2026-06-16] ingest | Expand 2 pages with updated source

**Sources updated (1):**

- **SBSQ #17: How Should You Prepare for an AI Future?** (Nate Silver) — Re-summarized with richer detail on the G×S×P multiplicative production framework (general intelligence × specialized knowledge × personal skills), winner-take-all dynamics created by AI performing at 8.7/10, and resilience/resourcefulness as the highest-leverage personal development traits.

**Note:** One source ("Checking your browser before accessing pmc.ncbi.nlm.nih.gov") was again an empty browser-challenge page with no content; skipped.

**Pages updated (2):**
- **ai-futures.md** — Expanded "Personal Preparation" section with Silver's G×S×P framework, winner-take-all analysis, and key quote.
- **ai-and-jobs.md** — Added new "Knowledge Worker Strategy: The G×S×P Framework" section linking the framework to the broader job displacement/adaptation discussion.

---

## [2026-06-10] ingest | Integrate 1 new source across 2 pages

**New sources integrated (1):**

- **The Zig Project's Rationale for Their Firm Anti-AI Contribution Policy** (Simon Willison, Apr 2026) — Zig's total ban on LLM contributions framed around "contributor poker": maintainer code review exists to *develop contributors as people*, not land features. LLM-authored PRs provide no signal about the submitter, breaking the contributor development loop. Creates a coordination problem where accepting AI PRs is irrational. Bun's Anthropic acquisition allows a divergent Zig fork with AI-assisted optimizations (4x speedup) the upstream project would never accept.

**Note:** One source ("Checking your browser before accessing pmc.ncbi.nlm.nih.gov") was a browser-challenge page with no content; skipped (same pattern as ad1bc97).

**Pages updated (2):**
- **ai-critical-perspectives.md** — Added "Open Source Resistance: The Zig Case" section with contributor poker framing and the Bun fork divergence.
- **agentic-coding.md** — Added note under "Reading vs Writing" linking Zig's policy to the open source contributor pipeline concern.

---

## [2026-06-09] ingest | Integrate 2 new sources across 2 pages (1 new)

**New sources integrated (2):**

- **How Generative and Agentic AI Shift Concern from Technical Debt to Cognitive Debt** (Margaret-Anne Storey, Feb 2026) — Introduces "cognitive debt" as the team-level erosion of shared understanding (Peter Naur's "program theory") as AI accelerates development velocity. Distinct from comprehension debt (individual-level) — cognitive debt lives in people, not code. Mitigation: require humans to understand AI changes, document reasoning, use TDD and pair programming to rebuild shared mental models.
- **What I'm Hearing About Cognitive Debt (So Far)** (Margaret-Anne Storey, Feb 2026) — Community follow-up confirming the pattern: velocity outpaces understanding, manifesting as review burden, debugging friction, and onboarding slowdowns. Core insight: as AI removes other bottlenecks, shared understanding may become the primary performance bottleneck. Mitigation requires maintaining a "distributed theory" across people, documentation, tests, tooling, and AI agents.

**Note:** One source ("Checking your browser before accessing pmc.ncbi.nlm.nih.gov") was again an empty browser-challenge page; skipped.

**New page (1):**
- **cognitive-debt.md** — Defines and distinguishes cognitive debt from comprehension debt; covers Storey's warning signs, mitigation framework, and community response; cross-references agentic coding and spec-driven development.

**Pages updated (1):**
- **ai-impact-on-software-engineering.md** — Extended the Comprehension Debt section with a paragraph linking to cognitive debt as the team-level complement, citing both Storey sources.

---

## [2026-06-08] ingest | Integrate 1 new source across 2 pages (0 new)

**New sources integrated (1):**

- **My AI Adoption Journey** (Mitchell Hashimoto, mitchellh.com, Feb 2026) — Practitioner's six-phase journey from chat → agents → async delegation → harness engineering. Key insight: efficiency gains come from understanding what agents *shouldn't* do and systematically delegating at the capability edge. Notable emphasis on async timing (off-hours "warm starts"), high-confidence delegation, and treating every Bad Thing as a permanent harness fix.

**Note:** One source ("Checking your browser before accessing pmc.ncbi.nlm.nih.gov") was an empty browser-challenge page; skipped.

**Pages updated (2):**
- **agentic-coding.md** — Added "Adoption Phases" section documenting Hashimoto's six-phase framework (switch to agents → reproduce work → async timing → high-confidence delegation → harness engineering → continuous background work).
- **agent-harness.md** — Extended the Ratchet Principle section with Hashimoto's corroborating account of phase-5 harness engineering as permanent-prevention practice.

---

## [2026-06-01] ingest | Integrate 2 new sources across 3 pages (0 new)

**New sources integrated (2):**

- **One of the New, Buzzy Jobs in Silicon Valley Is...** (Andrew Ng, Twitter/X, June 2026) — Analyzes the AI Forward Deployed Engineer (FDE) role vs. the larger and more scalable AI Engineer role. FDEs (embedded engineers who build and tune agentic workflows for clients) are resurgent, but AI Engineers will vastly outnumber them: companies prefer vendor-neutral engineers who preserve optionality as the AI landscape evolves. Ng predicts AI Engineering will fragment into specializations (LLMOps, Evals, Harness, Data Engineers) mirroring how software engineering split in prior decades.
- **Making AI Work: Leadership, Lab, and Crowd** (Ethan Mollick, One Useful Thing, June 2026) — Names and diagnoses the enterprise AI paradox: individual gains (2–3×, confirmed by experiments) are real; organizational gains are not materializing. Root cause: an organizational innovation deficit, not a technology gap. Proposes a Leadership/Lab/Crowd feedback loop. Identifies "Secret Cyborgs" (40%+ of workers privately using AI while only ~20% use official tools) as the key behavioral signal. Frames AI as a bottleneck-shifter: when research takes minutes, the constraint becomes knowing what to research.

**Note:** A third synced source ("Checking your browser before accessing pmc.ncbi.nlm.nih.gov") was an empty browser-challenge page with no recoverable content; skipped.

**Pages updated (3):**
- **ai-and-software-engineering-jobs.md** — Added "New AI Engineering Specializations" section (FDE vs. AI Engineer, vendor optionality, specialization trajectory per Andrew Ng).
- **ethan-mollick.md** — Added "Organizational AI Transformation: Leadership, Lab, and Crowd" section (Secret Cyborgs, three-part framework, bottleneck-shift thesis).
- **ai-and-jobs.md** — Extended the Productivity Paradox section with Mollick's structural explanation (organizational innovation deficit, Secret Cyborg dynamic, Leadership/Lab/Crowd framework).

---

## [2026-05-31] query | Orchestration tax × long-running agents synthesis (1 new page)

**Exploration:**
User asked whether long-running agents contradict the orchestration tax. Research across summaries and wiki revealed these are complementary concepts addressing different axes: breadth (orchestration tax — how many agents?) vs. depth (long-running agents — how long per agent?). Shifting from breadth to depth directly reduces review frequency and context-switching cost, which are the mechanisms behind the tax.

**New page:**
- **orchestration-tax.md** — Dedicated concept page: Amdahl's Law framing, the GIL analogy, relationship to long-running agents, the Delegated Approval pattern as the key intersection, and practical guidance on what to learn.

**Sources used:**
- [The Orchestration Tax](../summaries/the-orchestration-tax.md) (Osmani)
- [Long-running Agents](../summaries/long-running-agents.md) (Osmani)
- [5 Agent Design Patterns For Long-Running AI Agents](../summaries/5-agent-design-patterns-for-long-running-ai-agents.md) (Google Cloud Tech)
- [Your Parallel Agent Limit](../summaries/your-parallel-agent-limit.md) (Osmani)
- [Your AI Coding Agents Need A Manager](../summaries/your-ai-coding-agents-need-a-manager.md) (Osmani)
- [Agentic Memory: A Detailed Breakdown](../summaries/agentic-memory-a-detailed-breakdown.md)
- [What to Learn, Build, and Skip in AI Agents (2026)](../summaries/what-to-learn-build-and-skip-in-ai-agents-2026.md)

---

## [2026-05-31] ingest | Integrate 3 new sources across 3 pages (0 new)

**New sources integrated (3):**

- **Long-running Agents** (Addy Osmani, Substack, May 2026) — Architecture for agents that maintain progress over days/weeks across multiple context windows. Three core problems: context rot, statelessness between sessions, and self-grading bias. Solution: decouple brain/hands/session log; state lives outside the context window; structured handoffs enable recovery. The Ralph loop is the practitioner starting point. Unlocks dramatically more work — owning entire features, completing multi-quarter migrations, overnight research sweeps.
- **The Orchestration Tax** (Addy Osmani, Twitter/X, May 2026) — The hidden cost of scaling agent usage: starting agents is cheap but reviewing output is strictly serial. Human attention is the GIL of your AI agents; Amdahl's Law caps speedup at the serial fraction (judgment). Scale fleet to review rate, batch reviews, reserve human judgment only for decisions machines cannot verify.
- **Ad Infinitum** (Matthias Ott, May 2026) — Google's 2026 I/O: generative search absorbs web content into synthesized answers without linking back, breaking the 25-year web contract. Token auctions and prominence allocation embed ads directly into LLM output, indistinguishable from organic answers. Spark's demand for personal data powers hyper-targeted placement; advertisers lose keyword and creative control.

**Pages updated (3):**
- **addy-osmani.md** — Added "The Orchestration Tax" to Coined Concepts and "Long-Running Agents Require External State" to Core Arguments.
- **agentic-ai.md** — Extended Production Design Patterns with Osmani's brain/hands/session architecture for long-running agents.
- **ai-governance.md** — Added AI Search and Monetization section (Google token auctions, web contract collapse, surveillance dependency).

---

## [2026-05-17] ingest | Integrate 2 new sources across 1 page (0 new)

**New sources integrated (2):**

- **Agentic Memory: A Detailed Breakdown** (ramakrushna, Twitter/X, May 2026) — Four-type memory architecture (in-context, external, episodic, semantic/parametric) for building stateful agents. Key insight: retrieval quality is 80% of the problem — stored memories become inaccessible without effective retrieval. Vector embeddings enable semantic search over personal episode history. Active curation (decay, importance scoring, consolidation) prevents memory systems from degrading over time.
- **What to Learn, Build, and Skip in AI Agents (2026)** (Rohit, Twitter/X, May 2026) — Five-test filter for evaluating new AI launches. Durable primitives: context engineering, tool design, orchestrator-subagent pattern, eval discipline, harness mindset. Anti-patterns to skip: AutoGen/CrewAI/Semantic Kernel, autonomous agent pitches, naive multi-agent systems. Boring execution playbook: one outcome, tracing+evals first, single-agent start. Career implication: artifact-driven careers compound better than credential-based ones in a quarterly-changing field.

**Pages updated (1):**
- **agentic-ai.md** — Added Memory Architecture section (four types, retrieval bottleneck, vector search, active curation) and What to Build vs. Skip (2026) section (five-test filter, durable primitives, anti-patterns, execution playbook).

---

## [2026-05-14] ingest | Integrate 6 new sources across 4 pages (0 new)

**New sources integrated (6):**

- **How to Master Context Engineering** (Khairallah AL-Awady, Twitter/X, May 2026) — Argues context engineering (the information environment) beats prompt engineering (the wording). Three-layer context model: immediate/session/persistent. Four foundational context files; dynamic loading; memory systems from Markdown to RAG.
- **20 Claude Prompts That Turn a $20 Subscription Into a Personal Assistant** (Anatoli Kopadze, Twitter/X, May 2026) — Prompt architecture patterns: role framing, structured output templates, multi-source synthesis, explicit constraints. Most users tap ~10% of Claude's capability.
- **A Good AGENTS.md Is a Model Upgrade** (Slava Zhenylenko / AugmentCode, May 2026) — Empirical study: good AGENTS.md = Haiku-to-Opus quality jump; bad AGENTS.md degrades below no docs. Progressive disclosure (100–150 lines), procedural workflows, decision tables, and pairing prohibitions with alternatives all reliably improve agent output. Overexploration trap is the main failure mode.
- **There Will Be No AI Jobpocalypse** (Andrew Ng, Twitter/X, May 2026) — Multiple incentive structures (labs, pricing, corporate PR) sustain the jobpocalypse narrative despite weak evidence. Healthy hiring and unemployment contradict it. Ng predicts an "AI jobapalooza."
- **AI Is Killing the Career Ladder** (EO / Bharat Chandar, YouTube, May 2026) — Stanford research: 16% slower employment growth for early-career workers in AI-exposed roles; experienced workers unaffected. Career lattice model: AI lowers cost of learning adjacent skills, enabling profession switching.
- **If Anyone Builds It, Everyone Thrives** (Séb Krier, Twitter/X, May 2026) — Introduces "Positive Alignment" research: beyond harm avoidance to actively enabling human flourishing. Key challenge: avoiding technocratic paternalism while supporting human agency.

**Pages updated (4):**
- **prompt-engineering.md** — Added Context Engineering section (three-layer model, infrastructure-beats-syntax thesis) and Role-Based Prompt Templates section (structured role framing, synthesis patterns).
- **agent-harness.md** — Expanded Knowledge section with AGENTS.md Design: progressive disclosure, decision tables, overexploration trap, discovery statistics.
- **ai-and-jobs.md** — Added The Jobpocalypse Narrative and Its Incentives section (Andrew Ng) and Early-Career Impact and the Career Lattice section (Bharat Chandar / Stanford).
- **ai-safety.md** — Added Positive Alignment section (beyond harm avoidance to human flourishing).

---

## [2026-05-11] ingest | Integrate 6 new sources across 8 pages (1 new)

**New sources integrated (6):**

- **Agent Harness Engineering** (Addy Osmani, Twitter/X, May 2026) — Frames harness design as the emerging competitive discipline. Agent = Model + Harness. The Ratchet Principle: treat each failure as a permanent signal generating lasting harness improvements. A decent harness beats a great model.
- **Deriving Agent Harnesses from First Principles** (Viv, Twitter/X, May 2026) — Works backward from desired agent behaviors to derive core harness primitives: filesystem (durable state), bash (general-purpose tool), sandboxes (safe execution), context management, long-horizon composition. Model and harness co-evolve.
- **A Critical Question in Agent Design** (Ethan Mollick, Twitter/X, May 2026) — Argues agentic workflows should preserve meaningful human decision points. When all companies use the same models, the model is a commodity; the durable moat is process architecture that integrates human judgment at high-variance moments.
- **The Era of Easy AI Progress Is Ending — Ilya Sutskever** (Dwarkesh Patel, YouTube, May 2026) — Three-era framework: research discovery (2012–2020), scaling execution (2020–2025), return to research (post-2025). Pre-training data is finite; 100x scaling won't transform capability; new training paradigms needed.
- **Karpathy's 4 CLAUDE.md Rules Cut Claude Mistakes From 41% to 11%** (Mnimiy, Twitter/X, May 2026) — Karpathy's 4 foundational rules extended with 8 more targeting multi-step agent failures (token budgets, checkpointing, visible failures, test intent). CLAUDE.md over 200 lines causes sharp compliance drops.
- **Using Claude Code: The Unreasonable Effectiveness of HTML** (Thariq, Twitter/X, May 2026) — HTML outperforms Markdown for AI-generated documents: higher information density, better readability at scale, easy sharing, interactive feedback loops. Key psychological benefit: keeps users in the loop with Claude's decisions.

**New pages created (1):**
- **agent-harness.md** — Comprehensive synthesis of harness engineering: components (filesystem, bash, sandboxes, memory, context management, hooks), the Ratchet Principle, behavior-driven design, and co-evolution with model training.

**Pages updated (7):**
- **addy-osmani.md** — Added Agent Harness Engineering section with Ratchet Principle and harness components.
- **ethan-mollick.md** — Added Competitive Advantage in the Agentic Era section on model commoditization and process architecture as moat.
- **agentic-ai.md** — Expanded Environment and Harness Design section with new sources and Ratchet Principle; added Human-AI Competitive Advantage section.
- **scaling-and-compute.md** — Added The End of the Scaling Era section with Sutskever's three-era framework.
- **claude-code.md** — Added CLAUDE.md Rules Engineering section (12-rule framework) and Output Format: HTML over Markdown section.
- **andrej-karpathy.md** — Added CLAUDE.md Rules section linking to the 4-rule origin story.
- **index.md** — Added agent-harness.md to Applications.

---

## [2026-05-07] ingest | Integrate 1 new source across 3 wiki pages

**New source integrated (1):**

- **Cognitive Surrender** (Addy Osmani, Twitter/X, May 2026) — Distinguishes cognitive offloading (valid: delegate execution, retain judgment) from cognitive surrender (invalid: accept AI output wholesale without forming independent views). Research: 73% of participants accepted incorrect AI answers with confidence paradoxically increasing despite deliberate errors. Software engineers are uniquely vulnerable due to surface correctness signals. Antidotes span personal (form expectations before reviewing, devil's advocate prompts) and structural (verification exit criteria, anti-rationalization tables, smaller PRs).

**Pages updated (3):**
- **addy-osmani.md** — Added "cognitive surrender" to Coined Concepts alongside comprehension debt and ambient anxiety tax.
- **vibe-coding.md** — Added cognitive surrender to Risks as the psychological mechanism behind prompt-and-accept.
- **ai-impact-on-software-engineering.md** — Extended Comprehension Debt section to explain cognitive surrender as the mechanism that drives it.

---

## [2026-05-05] ingest | Integrate 3 new sources across 3 wiki pages (2 new)

**New sources integrated (3):**

- **How To Build A Team Of AI Agents That Replace Your First 3 Hires** (Khairallah AL-Awady, Twitter/X, May 2026) — Framework for solo founders building three specialized Claude agents (research, content, operations) connected via MCP servers to business tools. Shared knowledge base + quality gates turn independent tools into a coordinated team. Handles 70–80% of what three FTEs would do for subscription cost vs. $180K+/year.
- **AI And The Quantity And Quality Of Creative Products: Have LLMs Boosted Creation Of Valuable Books?** (Reimers & Waldfogel, NBER working paper, 2025) — Rigorous empirical study of AI's effect on book publishing 2022–2025. Supply tripled; average quality fell (AI books get 61% fewer ratings); but consumer surplus rose 7.23% by 2025. Author selection (low-quality authors adopting AI) explains ~65% of quality gap. No displacement of incumbent authors.
- **The Effects Of GenAI On Learning Performance: A Meta-Analysis Study** (Gökçül & Erdoğan, 2025) — 31 studies, 2,646 participants. Medium positive effect on learning (g=.689). K-12 benefits most; flipped classrooms and 1–3 month interventions are optimal; AI-integrated systems far outperform chatbots alone.

**Pages updated (1):**
- **agentic-ai.md** — Added Three-Agent Team for Solo Founders to Current Implementations.

**New pages created (2):**
- **ai-and-creative-work.md** — AI's effect on creative industries using books as the first large-scale empirical case; long tail expands, quality frontier unchanged; author selection dominates the quality gap.
- **ai-and-education.md** — GenAI's effect on learning performance; meta-analysis evidence, contrasting cognitive cost literature, and design principles for effective AI-augmented learning.

---

## [2026-05-03] ingest | Integrate 1 new source across 2 wiki pages

**New source integrated (1):**

- **The AI Economy Is About to Change** (The PrimeTime, YouTube, May 2026) — Covers the structural economic strain on AI companies: Anthropic's "painted door" pricing test ($20→$100/mo for Claude Code), Microsoft's GitHub Copilot shift from action-based to token-based pricing, OpenAI's $5–7B/month burn rate, and Google's structural advantage as a profitable AI investor. Argues that while free-tier contraction is inevitable, AI's genuine utility in specific applications survives the hype correction.

**Pages updated (2):**
- **ai-futures.md** — New "AI Industry Economics" section covering burn rates, pricing tests, Google's competitive advantage, and the token contraction ahead.
- **anthropic.md** — New "Pricing and Economics" section noting Anthropic's painted-door test and linking to the broader industry economics picture.

---

## [2026-05-02] ingest | Integrate 1 new source across 2 wiki pages

**New source integrated (1):**

- **The More Young People Use AI, The More They Hate It** (The Verge, Janus Rose, Apr 2026) — Gen Z's AI optimism has collapsed: only 18% express hopefulness (down from 27%), nearly 50% believe risks outweigh benefits. Young people face a contradictory mandate — warned AI will eliminate jobs while told they must adopt it to remain competitive. Universities are integrating AI without clear pedagogical justification. Neuroscience research shows cognitive offloading reduces brain activity and critical thinking. AI use has become culturally stigmatized among Gen Z despite 74% monthly usage.

**Pages updated (2):**
- **ai-critical-perspectives.md** — New "Gen Z Backlash" section covering declining optimism statistics, contradictory job-market pressures, cognitive offloading concerns, cultural stigma, and systemic harms.
- **ai-and-jobs.md** — Extended "The AI Fluency Divide" section with Gen Z context: the contradictory mandate and the gap between mandated use and genuine buy-in.

---

## [2026-04-29] ingest | Integrate 1 new source across 2 wiki pages

**New source integrated (1):**

- **Skill Issue: Andrej Karpathy on Code Agents, AutoResearch, and the Loopy Era of AI** (No Priors podcast, Apr 2026) — Karpathy describes the step-change beginning Dec 2024: delegating 80-90% of coding to agents, "manifesting will" through natural language. Introduces **AutoResearch** — autonomous agent loops discovering hyperparameter improvements humans missed in decades of manual tuning. Discusses "Program MDs" (research orgs described as markdown, optimizable by AI), the jagged intelligence landscape (superhuman on verifiable tasks, novice on subjective), and untrusted distributed worker pools for research.

**Pages updated (2):**
- **andrej-karpathy.md** — New section "The Loopy Era: AutoResearch and 80–90% Delegation" covering AutoResearch, Program MDs, jagged intelligence, and agent-as-content-router for education.
- **agentic-ai.md** — Added AutoResearch to Current Implementations with link back to the Karpathy page.

## [2026-04-29] lint | Close gap and orphan findings from audit

Acted on the highest-leverage findings from the wiki lint audit.

**6 new pages created** to close gap candidates flagged in the audit:
- **openai.md** — Organization page for OpenAI; collects products (GPT, o-series, Deep Research, Swarm), AGI claims, Pentagon red lines, copyright lawsuits, and the Anthropic-vs-OpenAI messaging tension.
- **addy-osmani.md** — Person page for Osmani; consolidates "comprehension debt," "ambient anxiety tax," "agentic engineering," parallel agent ceiling, and the IDE de-centering thesis.
- **boris-cherny.md** — Person page for the Claude Code creator; centralizes the "coding is largely solved" claims (100%/200%/4%/20%) and explicitly notes the tension with METR/CEO survey evidence.
- **vibe-coding.md** — Concept page for Karpathy's term; contrasts vibe coding vs. agentic engineering and links to the vibe specs corrective.
- **mcp.md** — Concept page for Model Context Protocol; positions MCP as the protocol layer of the agent harness.
- **reasoning-models.md** — Concept page for o1/Extended Thinking/GPT-5.2 Thinking; previously a broken link in `how-llms-work.md`.

**Orphan fix**: Converted three plain-text "Geoffrey Hinton" mentions into wiki links in `ai-safety.md`, `ai-critical-perspectives.md`, and `ai-futures.md`. The page now has inbound links.

**Inline cross-references added** so the new pages aren't themselves orphans: `agentic-coding.md` now links to `vibe-coding.md`, `addy-osmani.md`, and `mcp.md`; `claude-code.md` now links to `boris-cherny.md` and `mcp.md`; `ai-impact-on-software-engineering.md` and `ai-and-software-engineering-jobs.md` link to `boris-cherny.md` and `addy-osmani.md`; `agi-timelines.md` and `deep-research.md` link to `openai.md`; `anthropic.md`, `agentic-ai.md`, `prompt-engineering.md`, `andrej-karpathy.md`, and `spec-driven-development.md` updated with the relevant new-page links.

**Index updated**: Added Osmani and Cherny under People, OpenAI under Organizations, Reasoning Models and MCP under Technical, and Vibe Coding under Coding.

Remaining audit findings not addressed in this pass: contradictions (Karpathy 80/20 dating, Aschenbrenner timeline phrasing), stale-claim date anchoring (Amodei AGI by 2026, "year-end" ambiguity, METR "early 2025"), and several smaller gaps (Aaron Levie, DeepSeek cross-link, Apple/Obsidian duplication, Gary Marcus, MIT/CEO stat duplication, Tegmark cross-link).

## [2026-04-28] ingest | Integrate 4 new sources across 4 wiki pages

**New sources integrated (4):**

- **GitHub COO: Why Now Is the BEST Time to Be a Developer** (Kyle Daigle / Sajjaad Khader) — GitHub COO argues agentic AI mirrors historical tech shifts that created more developers, not fewer; human judgment on *what* to build remains irreplaceable; hiring now prioritizes problem-solving mindset over syntax knowledge.
- **I Built an AI SRE in 60mins, You Should Too** (Goutham City) — Narrow-scope AI SRE using Claude + Grafana gcx: skill-based architecture with curated runbooks and incident write-ups, false positive rate under 10% after 4-5 investigations, persistent file-based knowledge base that improves with each incident.
- **It Is Finally Happening** (Kyle Cook / Web Dev Simplified) — AI companies beginning "enshittification": VC subsidies ending, GitHub Copilot and Anthropic implementing drastic plan changes (suspended signups, per-token billing), enterprises that depend on AI for core functions may have no viable exit.
- **MIT Explains the 12 Possible Endings for AI** (Species / Documenting AGI) — Tegmark's *Life 3.0* framework: 12 scenarios from extinction to post-scarcity utopia; mainstream researchers estimate 1-in-6 odds of AI-caused extinction; Zoo scenario (humans as captive subjects) identified as potentially worse than extinction.

Pages updated:
- **ai-and-software-engineering-jobs** — Added "GitHub COO's Optimistic View" section: historical analogy to prior language abstraction shifts, interns doing months of work in weeks, hiring shifting to why/how reasoning over syntax.
- **agentic-ai** — Added AI SRE to "Current Implementations": narrow domain + curated knowledge base + iterative learning = highly effective operational agent.
- **ai-critical-perspectives** — Added "AI Pricing: Enshittification Begins" section: lock-in dynamics, per-token billing transition, enterprise exposure.
- **ai-futures** — Added "Tegmark's 12 Endings" subsection under Scenario Planning: Conqueror, Benevolent Dictator, Zoo, Gatekeeper, post-scarcity utopias, technological regression.
- **ai-safety** — Added Tegmark/MIT reference under "Expert Warnings" with extinction probability estimates from Hinton and Amodei.

0 new pages created — all sources fit existing categories.

## [2026-04-28] ingest | Integrate 3 new sources across 3 wiki pages

**New sources integrated (3):**

- **5 Agent Design Patterns For Long-Running AI Agents** (Google Cloud Tech) — Checkpoint-resume, delegated approval, memory-layered context, ambient processing, and fleet orchestration for production agents that run for days.
- **Every Day 100+ People Ask Me How Can I Learn AI Evals** (Paul Iusztin) — Curated resources on AI evaluation: LLM-as-a-judge, evaluation-driven development, RAG-specific evals, error analysis, and binary vs. Likert scale tradeoffs.
- **Fraud And The False Optimism Of AI For Science** (Jessica Hullman) — Critical examination of AI in scientific research: misattribution of AI-generated ideas as human contributions, the fraud spectrum, and why much pro-AI optimism is actually technological determinism.

Pages updated:
- **agentic-ai** — Added "Production Design Patterns" section covering Google's five composable patterns for stateful long-running agents (checkpoint-resume, human-in-loop, memory layers, ambient processing, fleet orchestration).
- **rag-and-knowledge-systems** — Added "Evaluating AI Systems" section on eval methodologies: LLM-as-judge, evaluation-driven development, RAG eval types, error analysis, and measurement tradeoffs.
- **ai-critical-perspectives** — Added "AI in Scientific Research" section on fraud spectrum, misattribution risks, and the argument that pro-AI science narratives mask pessimism about human agency.

0 new pages created — all sources fit existing categories.

## [2026-04-20] ingest | Integrate 5 new sources across 3 wiki pages

**New sources integrated (5):** Alex Imas's structural reallocation theory (tweet + Fortune article), the "harness is everything" agent design analysis, NotebookLM vs Gemini Notebooks workflow guide, and a MarketWatch AI job displacement article.

Pages updated:
- **ai-and-jobs** — Added new "Structural Reallocation: The Relational Sector" section covering economist Alex Imas's framework: labor migrates to high-income-elasticity "relational sector" jobs (nursing, teaching, therapy) as AI commoditizes routine work; mimetic desire and exclusivity premiums explain human provenance value; transition speed determines whether reallocation or demand collapse occurs. Also added MarketWatch 18-month displacement article to Displacement Predictions.
- **agentic-ai** — Added new "Environment and Harness Design" section: the harness (interface design, context management, feedback loops, multi-session scaffolding) determines agent performance more than model capability; SWE-agent showed 64% gains from interface changes alone.
- **rag-and-knowledge-systems** — Added new "Research vs. Creation Workflows" section: Google NotebookLM (grounded research, source citations) vs. Gemini Notebooks (creation, live web access) as complementary sequential tools.

0 new pages created — all sources fit existing categories.

## [2026-04-19] ingest | Integrate 5 new sources across 4 wiki pages

**New sources integrated (5):**

- **Changes in Claude system prompt between Opus 4.6 and 4.7** (Simon Willison) — Analysis of behavioral refinements: more concise, less pushy, better tool search, stronger child safety guardrails, screenshot attack safeguards.
- **Is the IDE dead?** (Addy Osmani) — The IDE is being de-centered as agent orchestration replaces line-by-line editing; new convergent UI patterns emerging.
- **The best AI coding content isn't on your feed** (John Crickett) — Curated conference talks on agents, context management, prompt engineering, and spec-driven development.
- **When people think software engineers, they tend to think jobs** (Aaron Levie) — AI agents will spread engineering demand to every sector (biopharma, finance, manufacturing), shifting work toward automation and process redesign.
- **Why will AI create more jobs in plenty of industries?** (Aaron Levie) — AI creates downstream bottlenecks that require human labor; competitive pressure sustains demand across value chains.

Pages updated:
- **anthropic** — Added "Model Evolution" section on system prompt changes between Opus 4.6 and 4.7
- **agentic-coding** — Added "The IDE Is Being De-Centered" section and "Resources" section with curated conference talks
- **ai-and-jobs** — Added "Job Creation Through Cascading Bottlenecks" section on Aaron Levie's downstream bottleneck thesis
- **ai-and-software-engineering-jobs** — Added "Industry-Wide Expansion" section on engineering demand spreading beyond tech

## [2026-04-19] ingest | Integrate 2 new sources into existing wiki pages

**New sources integrated (2):**

- **Aaron Levie tweet on the agent deployer role** — New organizational role emerging in enterprises as AI agents proliferate: a technical-business hybrid who identifies high-leverage workflows, designs agent context, and manages ongoing operations.
- **MarketWatch survival guide framing** — Popular media framing AI job displacement as imminent (18 months), offering practical worker preparation advice.

Pages updated:
- **agentic-ai** — Added new "Enterprise Roles: The Agent Deployer" section covering the emerging agent deployer/manager role: responsibilities, required skills (MCP, APIs, workflow design), and organizational placement
- **ai-and-jobs** — Added new "Survival Guides for Workers" section covering mainstream media framing of AI job displacement timelines

## [2026-04-19] ingest | Integrate 1 new source into ai-critical-perspectives

**New sources integrated (1):** Victor Tangermann's report on the growing AI backlash movement.

Pages updated:
- **ai-critical-perspectives** — Added new "Public Backlash" section covering escalation from online criticism to direct action (arson, gunfire), rural organizing against data centers, political victories against city councils approving data center deals, and the AI industry's narrative credibility problem (OpenAI's utopian messaging vs. Anthropic's existential risk warnings).

## [2026-04-15] ingest | Integrate 5 new sources across 3 wiki pages

**New sources integrated (5):** Addy Osmani's agentic engineering trilogy (agentic engineering terminology, multi-agent management, parallel agent cognitive limits), Anthropic's official Claude Code best practices guide, and Osmani's comprehension debt concept.

Pages updated:
- **agentic-coding** — Expanded "Vibe Coding" section into "Vibe Coding vs Agentic Engineering" with Osmani's terminology argument; added new "Multi-Agent Management" section covering agent fleet orchestration and "The Parallel Agent Ceiling" subsection on cognitive costs of parallelism
- **claude-code** — Added "Official Best Practices" section covering context window management, self-verification, Plan Mode, and scaling patterns
- **ai-impact-on-software-engineering** — Added "Comprehension Debt" subsection under Quality Risks covering the gap between code volume and human understanding, speed asymmetry, and metric blindness

1 source skipped (untitled-01ke68th.md — empty/no content).

## [2026-04-14] ingest + fix | Integrate 15 new sources, fix 29 broken links

**Link fixes:** Fixed 29 broken source links across all wiki pages caused by filename truncation mismatch (Readwise sync generates longer filenames than the wiki was referencing).

**New sources integrated (15):** Added references for 15 previously unreferenced sources across 12 wiki pages. No new pages created — all sources fit existing categories.

Pages updated:
- **claude-code** — Added Claude Skills (5 use cases), worktree support, Obsidian CLI inter-relationships, Boris Cherny impact interview (4% GitHub commits, "coding is largely solved")
- **prompt-engineering** — Added "Beyond Prompting" section (4 customization levers: memory, instructions, style, tools)
- **andrej-karpathy** — Added "How I Use LLMs" tutorial (lossy zip file model, token streams, tool use)
- **how-llms-work** — Added Karpathy's zip file mental model, Apple vs frontier model strategies (Mollick), 2023 tool landscape, early ChatGPT/Bard assistant tests
- **agentic-ai** — Added Ezra Klein/Jack Clark on agents ripping through the economy (talkers → doers transition)
- **ai-and-jobs** — Added Ezra Klein economic speed discussion, Krugman/Ritholtz historical perspective
- **ai-critical-perspectives** — Added Krugman/Ritholtz historical tech disruption analysis
- **ai-and-software-engineering-jobs** — Added early 2023 predictions, Boris "coding is solved" claims
- **ai-impact-on-software-engineering** — Added Boris Cherny "coding is solved" section
- **ai-governance** — Added NYT newsroom AI adoption, March 2026 governance snapshot (AI Data Center Moratorium Act, Anthropic injunction)
- **ethan-mollick** — Added Apple AI model strategy analysis
- **agi-timelines** — Added ARC-AGI-3 benchmark results (Symbolica 36% vs frontier models < 1%)
- **ai-futures** — Added AI business model viability analysis
- **rag-and-knowledge-systems** — Added Obsidian CLI inter-relationship access

1 source skipped (untitled-01ke68th.md — empty/no content).

## [2026-04-14] ingest | Incorporate 14 new sources + 45 previously unreferenced sources

Updated 8 wiki pages with references to newly synced and previously unreferenced source documents:
- **claude-code** — Added 8 new sources: Boris tips, hidden features, design philosophy, Obsidian integration
- **agentic-coding** — Added three eras of AI development (Cursor CEO)
- **agentic-ai** — Added OpenClaw multi-agent company, cognitive load limits
- **rag-and-knowledge-systems** — Added Karpathy's LLM knowledge base system, Obsidian integrations
- **ai-and-jobs** — Added Stanford employment study, 2024 workforce trends
- **ai-critical-perspectives** — Added discourse gap, realistic risk scenarios
- **spec-driven-development** — Added PM role evolution, Osmani spec guide
- **ai-impact-on-software-engineering** — Updated METR study (19% slowdown), industrial software

## [2026-04-14] query → synthesis | AI impact on software engineering

Created [AI Impact On Software Engineering](ai-impact-on-software-engineering.md) from a query about AI's effects on the profession. Synthesizes evidence across agentic coding, job market data, productivity research, and professional identity shifts. Includes open questions for future research.

## [2026-04-14] ingest | Bulk ingest of 96 Readwise sources into wiki

Created 20 wiki pages from 96 source documents synced from Readwise (AI tag).

**Entity pages (6):**
- andrej-karpathy.md
- dario-amodei.md
- ethan-mollick.md
- geoffrey-hinton.md
- leopold-aschenbrenner.md
- anthropic.md

**Concept pages (10):**
- agentic-coding.md
- claude-code.md
- spec-driven-development.md
- agentic-ai.md
- deep-research.md
- how-llms-work.md
- prompt-engineering.md
- rag-and-knowledge-systems.md
- ai-and-jobs.md
- ai-and-software-engineering-jobs.md
- ai-safety.md
- ai-governance.md
- ai-geopolitics.md
- scaling-and-compute.md

**Synthesis pages (4):**
- agi-timelines.md
- situational-awareness.md
- ai-futures.md
- ai-critical-perspectives.md

All 96 sources referenced across wiki pages. Index updated.

## [2026-04-14] init | Wiki initialized with index, log, and schema
