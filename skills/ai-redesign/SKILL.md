---
name: ai-redesign
description: AI-first workflow redesign roadmap for a vertical market software (VMS) company's product — decomposes its workflows, designs an AI-first alternative for the ones worth redesigning, and rolls them into a prioritized, tiered roadmap. Use when scoping an AI transformation engagement or answering "what should this product's AI roadmap look like."
---

# VMS AI Redesign

Produce an AI-first transformation roadmap for a VMS company's product: which workflows it
already owns are worth rebuilding with AI as the primary actor, what each redesign would
concretely look like, and in what order to build them.

This skill is fully standalone: it runs its own research pass every time, with no shared cache
and no dependency on any other skill or report. If the user has run other research skills in this plugin on the
same company, do not read their output — research this one fresh.

Adapted from VMS-Analyzer's `transformation/transformation-decompose-agent.md` +
`transformation-design-agent.md` + `transformation-synthesize-agent.md` +
`transformation-framework-definition-spec.md`. In the source pipeline these were three chained
agents, each reading the previous one's output file from a shared run folder (decompose →
fan out one design agent per qualifying workflow → synthesize). There is no orchestrator and no
file handoff here, so run all three as **sequential phases inside this one conversation**:
decompose first, then design each qualifying workflow, then synthesize — carrying findings
forward in context rather than reading them back from disk.

## Inputs

Ask the user (if not already given) for:
- **Company name** and, ideally, its website/domain.
- **Product to scope to**, if the company has multiple products/lines — otherwise scope to the
  company's primary product.
- **Optional focus**: a specific workflow, team, or job function to prioritize in the research
  (e.g. "focus on dispatch and scheduling," "focus on the back-office/billing side"). If given,
  bias the workflow inventory toward that area but don't refuse to note other high-scoring
  workflows you encounter along the way.

## Phase 0: Research

Full framework detail — workflow schema, TPS rubric, transformation types, design schema,
priority scoring, roadmap tiers: `references/ai-redesign-spec.md` — read it in full before
decomposing anything.

There is no cache to fall back on, so this phase does the work the source pipeline's shared
`pass2_product_market_map` cache used to do. Run your own WebSearch/WebFetch pass — budget
roughly 12-18 searches/fetches here, enough to answer:

- **What the product does:** core modules/features, the vertical it serves, the buyer/user
  roles, and its documented workflows (product site, docs/help center, demo videos, G2/Capterra
  category listing).
- **What data and integrations already exist:** integrations/marketplace page, API docs, any
  published data model or module list — this feeds Data Availability scoring later.
- **Current AI posture:** anything already shipped or announced (product blog, changelog, press)
  — workflows already AI-touched score differently and inform `ai_readiness_signals`.
- **Competitive landscape:** named 1-2 direct competitors and what they've shipped in AI (for
  later competitor-precedent search in Phase 2 — you don't need full designs yet, just who to
  check).
- **Manual-volume evidence:** job postings for roles at this company or the vertical broadly
  (titles like "operations coordinator," "claims processor" — whatever fits the vertical),
  G2/Capterra/TrustRadius reviews mentioning manual work, workarounds, or time-consuming steps.

Log roughly how many searches you ran and what they covered — this goes in the report's Run
Statistics section.

## Phase 1: Decompose Workflows

Rubric and schema: `references/ai-redesign-spec.md` §2-§3.

1. From your research, build a workflow inventory — typically 6-12 workflows depending on
   product scope. Apply the granularity rule (§2.1): a discrete job one person does, trigger to
   completion. Split multi-actor/multi-phase workflows into separate records where warranted.
2. For each workflow, write the full current-state record (actor, trigger, data in/out, manual
   steps, decision points, failure modes, known friction).
3. Score TPS on all four dimensions (manual_volume, ai_tractability, failure_cost,
   data_availability) per §3.1-§3.4. Manual volume should be evidence-based from Phase 0
   research; if you have no direct signal for a specific workflow, one additional targeted
   WebSearch is fine — the other three dimensions are reasoning-only, no search.
4. Compute `tps_composite` and mark `qualifies_for_design` (TPS ≥ 3.5).
5. Apply the qualification floor (§3.5): if fewer than 3 workflows qualify, pull the
   highest-scoring Borderline (3.0-3.4) workflows up to a floor of 3, flagged
   `borderline_qualification`. Note this explicitly later in Run Statistics.

Carry the full workflow inventory (qualifying and non-qualifying) forward in context — the
report needs both the qualifying set (for design) and the full set (for the Transformation
Landscape section's type/tier distribution context).

## Phase 2: Design an AI-First Alternative — one per qualifying workflow

Schema, transformation types, confidence rubric: `references/ai-redesign-spec.md` §4-§5.

For each qualifying workflow, in turn:

1. **Competitor precedent search** — check what you already learned in Phase 0 about the top
   1-2 competitors first; search only for what that didn't answer. Query shape:
   `"{competitor}" {workflow term} AI automated feature`. Budget ≤2 searches per workflow for
   this and the next step combined.
2. **User signal verification** — check Phase 0 review/complaint findings first; if nothing
   workflow-specific turned up, one more targeted search:
   `"{company}" {workflow term} review complaint workaround manual`.
3. **Dependency verification (non-negotiable, §5.2)** — if the design needs an external
   API/integration not already confirmed, verify it with one search or mark `build_complexity:
   High` and note it as unconfirmed. Never assign Low/Medium complexity to an unconfirmed
   external dependency.
4. **Design the AI-first replacement.** Select the transformation type (T1-T5, §4) — confirm or
   revise your Phase 1 hypothesis, noting why if revised. Annotate every `data_required` item
   `(accessible)` or `(requires access layer)` per §3.4. Follow the voice rule (§5.3): describe
   what the AI specifically does, never "AI-powered."
5. **Assign confidence** (Strong/Moderate/Weak) mechanically per §5.1, from evidence sources
   actually gathered across Phases 0-2.

Total design-phase search budget scales with the number of qualifying workflows — typically
3-6 workflows × ~2 searches = 6-12 additional searches on top of Phase 0.

## Phase 3: Synthesize into a Prioritized Roadmap

Formula and tiers: `references/ai-redesign-spec.md` §6-§7.2. No new searches in this phase —
score deterministically from the design records already built.

1. Score priority for every design: `(impact × 0.36) + (feasibility × 0.32) + (time_to_value × 0.22) + (market_gap_urgency × 0.10)`.
   `market_gap_urgency` comes directly from the competitor-precedent evidence gathered in Phase 2.
2. Assign roadmap tiers (§7). Name a `blocking_constraint` for every Tier 2/3 candidate.
3. Sort by priority score descending, tiebreak by transformation type rank (T1 > T2 > T3 > T5 > T4).
4. If Tier 1 has more than 5 candidates, name the top 3 as Sprint 1 (§7.1), applying the
   shared-infrastructure grouping override where it applies.
5. Apply shared-infrastructure sequencing notes (§7.2) wherever two or more Tier 1 candidates
   depend on the same build prerequisite, regardless of Tier 1 size.

## Phase 4: Write the Report

Voice rules: `references/ai-redesign-spec.md` §8. Sections in order:

1. **Header** — company name, vertical, product scoped to, generated date.
2. **Executive Summary** — 3-5 bullets: headline Tier 1 opportunity, count of Tier 1 candidates
   and transformation types present, the single most important feasibility fact, what the
   product looks like after Tier 1 ships. A 60-second read.
3. **Product Baseline** — 2-3 paragraphs: what the product does (real vertical vocabulary, never
   "comprehensive software solution"), current AI posture (shipped/announced/none found), and
   the transformation starting point (workflows decomposed / qualifying).
4. **Transformation Landscape** — one table: transformation-type distribution + tier
   distribution across all designed candidates, then one sentence on the dominant type and what
   it reveals about the product's character.
5. **Tier 1 Candidates** — one subsection per Tier 1 candidate, rank order:
   `### {rank}. {workflow_name}` — transformation type, priority score, evidence confidence, then
   **Today** (2-3 sentences), **The AI-First Version** (3-5 sentences: trigger, AI execution,
   human role, exception path), **What changes for users** / **Time saved** / **Outcomes
   changed**, **Evidence** (competitor precedent / user signal / job posting signal — "None found
   in public sources" rather than fabricating), **What it takes to build** (data, AI capability,
   build complexity, dependencies).
6. **Tier 2 Summary** — table only: Workflow | Type | Priority Score | Blocking Constraint. Omit
   if no Tier 2 candidates.
7. **Transformation Roadmap** — full ranked table of every designed candidate with tier, then a
   3-5 sentence sequencing narrative: why the top candidate goes first, which candidates share
   infrastructure and should sequence together, what the Tier 1 portfolio delivers as a whole.
8. **What This Product Looks Like After Transformation** — 3-5 paragraphs on how the product
   behaves differently, what a user's working day looks like, the product's AI-first identity in
   one sentence, the competitive implication. May be slightly visionary, but every claim must
   trace back to a specific Tier 1 candidate already named in Section 5 — no new capabilities
   introduced here.
9. **Evidence Quality** — table, one row per designed candidate, all tiers: Rank | Workflow |
   Type | Tier | Evidence Confidence | Flags.
10. **Run Statistics** — workflows decomposed / qualifying (and how many were pulled up via the
    qualification floor, if any), designs completed, tier counts, total searches run, generated
    timestamp.

Never use framework codes (T1, W03, TPS) in narrative prose — name the transformation type and
the workflow in plain English. Codes belong only in tables (§4, §7, §9).

Deliver the report as the final message content (plain markdown), not as a file, unless the user
asks for a file.
