# Activity Log

Reverse-chronological record of all wiki activity. Newest entries first.

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
