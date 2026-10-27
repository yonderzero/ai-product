# AI Redesign Framework Spec (standalone)

Condensed from VMS-Analyzer's `transformation/transformation-framework-definition-spec.md` v1
(plus the decompose, design, and synthesize agent instructions it fed) for a standalone,
single-pass skill. Source of truth for workflow schema, TPS scoring, transformation types, the
design candidate schema, priority scoring, and roadmap tier logic. If anything in SKILL.md
conflicts with this file, this file wins.

## 1. Purpose

For every workflow a VMS product already owns, this framework answers one question:

> **If we rebuilt this workflow from scratch today, with AI as the primary actor — not an
> assistant, not an add-on, but the engine — what would it do, how would it behave, and what
> would it unlock for the user?**

This is not a gap finder (that's `product-gaps`) and not a maturity or risk assessment
(`maturity-score`, `risk-score`). It produces a concrete, evidence-grounded transformation
design for workflows the product already has, then rolls those designs into a prioritized
roadmap.

In VMS-Analyzer this ran as three chained agents (decompose → design ×N → synthesize), each
reading the prior one's output file from a shared run folder. Standalone, there is no
orchestrator and no file handoff — one skill run does all three phases in sequence, in the same
context, carrying findings forward from phase to phase rather than reading them back from disk.

## 2. Workflow Record Schema (Phase 1: Decompose)

Every workflow identified in research is expanded into a current-state record:

```json
{
  "workflow_id": "W01",
  "workflow_name": "Short job-level name (the task a person does)",
  "workflow_description": "One sentence describing the workflow from trigger to completion",
  "current_state": {
    "actor": "The human role that performs this workflow (e.g. operations coordinator)",
    "trigger": "What initiates this workflow (event, schedule, threshold, manual decision)",
    "data_in": ["2-5 data inputs the actor needs to start"],
    "data_out": ["2-4 data outputs or actions produced when the workflow completes"],
    "manual_steps": ["3-8 discrete manual steps the actor takes"],
    "decision_points": ["2-5 judgment calls or choices the actor makes during execution"],
    "failure_modes": ["2-4 things that go wrong when this workflow is done poorly or not at all"],
    "known_friction": "One sentence summarizing the dominant pain or cost"
  },
  "ai_readiness_signals": ["Any observed signals that AI transformation is already happening here"],
  "manual_volume_evidence": [
    {"source": "URL or named source", "snippet": "paraphrase", "signal_type": "job_posting | user_complaint | workaround_description | analyst_mention"}
  ],
  "tps_scores": { "...see §3..." },
  "tps_composite": 0.0,
  "qualifies_for_design": true,
  "primary_transformation_type_hypothesis": "T1|T2|T3|T4|T5"
}
```

### 2.1 Workflow Granularity Rule

Decompose to the level of a **discrete job a specific person does, from trigger to completion**.
Not product features, not individual UI steps, not broad capability areas.

- Too coarse: "Manage subcontractors"
- Correct: "Track and renew subcontractor compliance certificates"
- Too fine: "Open the certificates screen"

The right level: if this workflow were automated, one human job (or a significant fraction of
one) would change.

**Split multi-actor / multi-phase workflows.** When a candidate workflow spans multiple distinct
actors (e.g., service advisor write-up AND technician inspection) or two phases separated by
time with a distinct trigger and output, split it into two workflow records if each phase
independently qualifies as a discrete job. Note the split in `workflow_description` (e.g., "Split
from the intake workflow — advisor write-up separated from technician inspection because each is
a distinct job with a different actor"). Absorbing a multi-phase workflow into one record risks
missing a standalone AI opportunity — two targeted designs ship faster than one composite design.

## 3. Transformation Potential Score (TPS) — Phase 1

A 1-5 composite that determines which workflows qualify for Phase 2 design.

```
TPS = (manual_volume × 0.30) + (ai_tractability × 0.30) + (failure_cost × 0.20) + (data_availability × 0.20)
```

All four dimensions 1-5, TPS rounded to 1 decimal.

| TPS Range | Qualification |
|---|---|
| 4.0-5.0 | **Prime** — proceed to design |
| 3.5-3.9 | **Strong** — proceed to design |
| 3.0-3.4 | **Borderline** — recorded, excluded from design unless needed to reach the 3-candidate floor (§3.5) |
| 2.0-2.9 | **Conditional** — excluded; note the blocking constraint |
| 1.0-1.9 | **Low** — excluded |

### 3.1 Manual Volume — *evidence-based*

How much human time and attention this workflow consumes today. Ground this in your research
(job postings, review-site complaints, help-doc language implying manual effort) rather than
guessing from product complexity.

| Score | Definition |
|-|-|
| 1 | Trivial — minutes per week in total across all users |
| 2 | Minor — a small but regular portion of someone's time |
| 3 | Moderate — a meaningful recurring responsibility for one or more people |
| 4 | High — consumes a substantial share of someone's working time, or is a common hire reason |
| 5 | Very high — a primary job function; multiple FTEs or high-frequency repetition evident |

### 3.2 AI Tractability — *reasoning-only*

How suited the workflow is to AI execution, given its decision logic. Assess from the
`current_state` record — no search needed.

| Score | Definition |
|-|-|
| 1 | Highly judgment-dependent — open-ended expertise or legal/ethical judgment at every step |
| 2 | Mostly judgment-dependent — some rule-bound steps, but core decisions need human expertise |
| 3 | Mixed — roughly half rule-bound/pattern-recognizable, half judgment |
| 4 | Mostly tractable — largely rule-bound with a small number of exceptional cases |
| 5 | Highly tractable — fully rule-bound or pattern-driven; AI can execute the full loop |

Trap: don't treat any human-review requirement as low tractability — an Autonomous design can
still route exceptions to a human. Don't confuse data complexity with decision complexity.

### 3.3 Failure Cost — *reasoning-only*

What it costs when this workflow is done poorly, inconsistently, or not at all. Assess from
`failure_modes` and vertical context.

| Score | Definition |
|-|-|
| 1 | Negligible — no meaningful operational or commercial consequence |
| 2 | Minor — inconvenience or minor rework, no lasting damage |
| 3 | Moderate — noticeable operational problems, customer dissatisfaction, or reportable errors |
| 4 | Significant — compliance exposure, financial loss, customer churn, or reputational damage |
| 5 | Severe — major operational breakdown, regulatory penalties, loss of licence, material harm |

Trap: don't import the severity of the whole product ("this is mission-critical software,
therefore everything is a 5") — score the specific workflow's failure.

### 3.4 Data Availability — *reasoning-only*

Whether the data an AI would need to run this workflow is already inside the product or easily
connectable. Assess from what your research turned up about the product's modules/features and
integrations, plus the workflow's `data_in`/`data_out`.

| Score | Definition |
|-|-|
| 1 | Largely external — significant new data capture, integrations, or infrastructure needed first |
| 2 | Partially available — some data is in the product, but important inputs are missing |
| 3 | Mostly available — primary data is in scope, one or two gaps remain |
| 4 | Well-covered — most required inputs already in the product's documented scope; minor gaps |
| 5 | Fully available — all required inputs already captured; AI can start with no new infrastructure |

**Data accessibility annotation (carried into Phase 2 design):** a score of 4-5 here means the
data *exists* — it does not mean an AI agent can query it today. Annotate each data item in the
design's `feasibility.data_required` as **(accessible)** — queryable via the product's existing
service architecture — or **(requires access layer)** — exists in the database/module scope but
the product lacks an agent API/service layer, so building that layer is a prerequisite. A design
where every item scores 5 on data availability but several require an access layer should note:
"All data in-product; agent service layer required as build prerequisite — adds complexity
regardless of data availability."

### 3.5 Qualification floor for a standalone run

The source pipeline hard-stops if fewer than 3 workflows qualify (TPS ≥ 3.5) and asks the
orchestrator to re-run decomposition. There is no orchestrator here, so instead: if fewer than 3
workflows clear 3.5, pull the highest-scoring Borderline workflows (3.0-3.4) up to a floor of 3
total candidates, flag each pulled-up candidate `borderline_qualification` in its record, and say
so plainly in the report's Run Statistics section. Never silently invent a fourth workflow to hit
the floor — if genuinely fewer than 3 workflows exist worth designing (e.g., a very narrow
product), report fewer and say why.

## 4. Transformation Types (Phase 2: Design)

Every design candidate gets a primary transformation type, optionally a secondary. The type
defines the shape of the AI-first redesign.

### T1 — Autonomous

AI takes over the end-to-end execution loop: receives the trigger, executes all steps, decides
within defined policy bounds, closes the loop. Humans see only exceptions — out-of-policy
actions, failure states, items needing explicit approval.

- **Ready when:** clear trigger; rule-bound or pattern-recognizable decision logic; predictable,
  recoverable failure modes; data already in or easily connectable to the product.
- **Design principle:** eliminate the human from the execution loop. Their job shifts from
  executor to policy-setter + exception-handler. The surface becomes an exception queue.
- **Human role after:** policy-setter + exception-handler.
- **Typical UX:** exception queue / approval inbox.
- **Traps:** proposing automation for steps that are actually judgment-dependent (should be
  Augmented); ignoring the exception-handling UX; calling "AI does 80% automatically, human
  handles 20%" Autonomous — true Autonomous means AI owns the full loop with exceptions surfaced.

### T2 — Augmented

The human stays the decision-maker; AI changes the quality and speed of the decision by
surfacing better data, context, risk signals, predictions, and a recommended action before the
human acts.

- **Ready when:** judgment calls where humans work with incomplete/scattered information today;
  better context would predictably change the outcome, not just validate what they'd have done
  anyway.
- **Design principle:** make the human dramatically more accurate, fast, and confident — without
  removing them. Value is in the richness of pre-decision context, not automating the act itself.
- **Human role after:** decision-maker, with a recommendation and risk signal in hand.
- **Typical UX:** pre-decision briefing — AI-assembled context plus a one-click action to confirm.
- **Traps:** confusing Augmented with "more data on a dashboard" (needs synthesis + a
  recommendation); proposing Augmented for a decision that's actually rule-bound (should be
  Autonomous).

### T3 — Ambient

AI watches the product's data continuously and speaks up unprompted — no workflow trigger, no
user request. The user doesn't ask; the AI decides something is worth surfacing.

- **Ready when:** a pattern is detectable before it's visible through normal operations; early
  detection has real value; the signal can be monitored continuously and cheaply.
- **Design principle:** add a persistent watcher layer. Experience shifts from checking
  dashboards to receiving signals. The product speaks first.
- **Human role after:** recipient of proactive signals.
- **Typical UX:** notification / alert / insight card in the product feed, not behind navigation.
- **Traps:** too noisy (false positives destroy trust — ambient must be high-signal); confusing a
  scheduled report with ambient intelligence (a report on a timer isn't ambient — the AI must
  decide *when* something is worth surfacing).

### T4 — Conversational

Replaces a form, menu, search filter, or static report with natural language. The user describes
what they want; AI executes or retrieves; the product answers in natural language.

- **Ready when:** users have to know where to look/navigate today; the underlying data is
  well-structured (the barrier is access/expression, not data); the need is variable and
  contextual, not a fixed-schedule operation.
- **Design principle:** remove the navigation layer. Complex queries that needed multiple reports
  and manual synthesis become one natural-language question.
- **Human role after:** asker.
- **Typical UX:** chat or command bar embedded in product context, no navigation required.
- **Traps:** proposing Conversational for a frequent, predictable action (a one-click action
  shouldn't become a conversation); ignoring that messy/inconsistent underlying data produces
  unreliable conversational answers.

### T5 — Predictive

AI models future states from current data and acts on, or surfaces, predictions before the human
would otherwise have noticed the problem.

- **Ready when:** leading-indicator data correlates with an outcome the user cares about and is
  available in the product; acting earlier produces materially better outcomes; prediction
  accuracy is good enough that false positives are tolerable.
- **Design principle:** convert the product from reactive to proactive. Experience shifts from
  managing current problems to preventing future ones.
- **Human role after:** early-mover — acts on predicted risk/opportunity while there's still time.
- **Typical UX:** ahead-of-time alert, e.g. "Job 4472 is likely to miss SLA — reallocate now?"
  rather than "Job 4472 has missed SLA."
- **Traps:** the signal must genuinely lead the outcome in time, not just correlate; must handle
  false positives gracefully (easy dismiss, no alarm fatigue); don't confuse with Ambient — Ambient
  surfaces current-state patterns, Predictive models a future state.

## 5. Design Candidate Schema (Phase 2)

One record per qualifying workflow:

```json
{
  "design_id": "W01_D",
  "workflow_id": "W01",
  "workflow_name": "",
  "transformation_type_primary": "T1|T2|T3|T4|T5",
  "transformation_type_secondary": "T1|T2|T3|T4|T5|null",
  "current_state_summary": "One sentence: who does this, how, dominant pain",
  "ai_first_vision": {
    "headline": "One sentence: what the AI-first version does differently",
    "description": "3-5 sentences: trigger, AI execution, human role, exception path",
    "ai_actor": "Name/description of the AI agent or capability owning the loop",
    "human_role": "What the human does in the AI-first version",
    "new_data_created": ["New artefacts/signals the AI-first version generates"],
    "new_ux_mode": "How the product surface looks different"
  },
  "value_to_end_user": {
    "time_saved": "Estimate of human time eliminated or freed per period",
    "outcomes_changed": ["Specific outcome improvements"],
    "experience_change": "One sentence: what changes about the job of the person who owned this"
  },
  "feasibility": {
    "data_required": ["Each item annotated (accessible) or (requires access layer)"],
    "ai_capability_required": "structured workflow agent | document parsing | prediction model | LLM reasoning | NL interface",
    "integration_complexity": "Low|Medium|High",
    "build_complexity": "Low|Medium|High",
    "dependencies": ["What must exist first — name shared prerequisites across candidates"]
  },
  "evidence": {
    "competitor_precedent": "Description + source, or null",
    "user_signal": "Description + source, or null",
    "job_posting_signal": "Description + source, or null",
    "adjacent_vertical_precedent": "Description + source, or null"
  },
  "confidence": "Strong|Moderate|Weak",
  "confidence_rationale": ""
}
```

### 5.1 Confidence Assignment (mechanical)

Count evidence sources present in the `evidence` block (each worth 1 point): competitor
precedent, user signal, job posting signal, adjacent-vertical precedent.

- **Strong** — ≥2 sources present, AND both competitor_precedent and user_signal are present
- **Moderate** — ≥2 sources present, but not both competitor + user
- **Weak** — <2 sources present

Document the reasoning in `confidence_rationale`, e.g. "Strong: competitor precedent (X shipped
automated renewal reminders) + user signal (job posting evidence of manual chasing). Two sources,
cross-referenced."

### 5.2 Dependency verification (non-negotiable)

If a design requires an external API/integration not already confirmed in your research, verify
it with a targeted search ("{dependency} API documentation {vertical} integration"). If not
confirmed after one search: set `build_complexity: "High"` and add the note "External dependency
not confirmed — vendor verification required before build." Never assign Low or Medium
complexity to an unconfirmed external dependency. Major platforms with established developer
programs (Salesforce, SAP, big ERPs) — confirming the docs URL exists is sufficient. Government
regulatory tools — assume no programmatic access unless proven.

### 5.3 Voice rule for designs

Describe what the AI specifically does — trigger, execution, exception path — never "AI-powered"
or "leverages ML." Specificity is the proof of quality: "monitors certificate expiry dates, sends
structured renewal requests, validates receipt against a document schema, flags non-responsive
subcontractors for review" — not "uses AI to manage compliance."

## 6. Priority Scoring (Phase 3: Synthesize)

Deterministic — no new searches in this phase, score from the design records already built.

```
Priority Score = (impact × 0.36) + (feasibility × 0.32) + (time_to_value × 0.22) + (market_gap_urgency × 0.10)
```

All four dimensions 1-5, rounded to 1 decimal.

**Impact** — how transformative for end users / the product's value proposition:
1 marginal, 2 meaningful, 3 significant, 4 major, 5 transformative (would be featured in sales/marketing)

**Feasibility** — how buildable given current product state and AI capability:
1 requires data/infra that doesn't exist, 2 significant dependencies, 3 buildable with meaningful
effort and a clear resolution path, 4 buildable with moderate effort, most data/infra exists,
5 highly buildable — all data in scope, AI capability proven, low integration complexity

**Time-to-value** — how quickly the AI-first version delivers visible value after shipping:
1 long gestation (data accumulation / learning period first), 2 medium horizon (months of
production use), 3 medium-short (weeks), 4 short (day one / first use), 5 immediate

**Market gap urgency** — whether a competitor has already shipped this, from your Phase 2
competitor-precedent research:
| Score | Definition |
|-|-|
| 5 | A direct competitor has already shipped this into production for the same segment |
| 3 | A competitor has announced, previewed, or piloted this |
| 1 | No competitor precedent found, no adjacent-market precedent either |

Rationale for the small 0.10 weight: two candidates equal on the other three dimensions
shouldn't score identically if one has a live competitor precedent — it doesn't override the
structural opportunity dimensions, but it breaks ties and captures urgency they don't encode.

## 7. Roadmap Tiers

| Tier | Score Range | Label | Meaning |
|---|---|---|---|
| 1 | 3.5-5.0 | Transform Now | High confidence, high impact, buildable — the centerpiece of the roadmap |
| 2 | 2.5-3.4 | Build Toward | Worth building with a plan; a dependency or medium-horizon value constrains it now |
| 3 | 1.5-2.4 | Watch | Low near-term priority; revisit when the limiting factor changes |
| 4 | <1.5 | Deprioritize | Do not pursue now |

Tier 2 and Tier 3 candidates **must** name a `blocking_constraint` — the single most important
reason this isn't Tier 1 yet. Sort within and across tiers by priority score descending;
tiebreak by transformation type rank T1 > T2 > T3 > T5 > T4.

### 7.1 Sprint-1 sub-tier (only when Tier 1 has >5 candidates)

If more than 5 candidates land in Tier 1, a team can't realistically build all of them at once.
Name the top 3 by priority score as Sprint 1 candidates. Two Tier 1 candidates may be grouped
into Sprint 1 together even out of strict rank order if they share a core build prerequisite
(same agent service layer, same data layer, same integration pipeline) — document the shared
infrastructure explicitly. If Tier 1 has ≤5 candidates, skip this sub-tier entirely.

### 7.2 Shared-infrastructure sequencing (any Tier 1 size)

When two or more Tier 1 candidates share a build prerequisite, the first one built accelerates
the others. In the roadmap narrative, name the shared prerequisite and which candidates depend
on it; recommend building them consecutively (or in parallel) rather than interleaved with
unrelated candidates, so the prerequisite isn't built twice. Reference the shared prerequisite by
name in each affected candidate's `dependencies` field.

## 8. Report Voice Guidelines

1. **Use the vertical's vocabulary**, drawn from your own research — a field service company's
   report says "work orders," "dispatching," "SLA compliance," not "task management."
2. **Vision and feasibility are complementary, not contradictory.** The AI-first vision describes
   what the product could be; the feasibility section describes the path to it. If feasibility
   truly undercuts the vision, the candidate belongs in Tier 2/3 — don't write it up as a
   contradicted Tier 1.
3. **Describe what the AI does, never that it "uses AI."** No "AI-powered," no "leverages machine
   learning." Say the specific behavior.
4. **Name the human role change for every Tier 1 candidate** — "the operations coordinator shifts
   from chasing subcontractors by email to reviewing a short exception queue each morning."
5. **Report length:** 1,500-3,000 words excluding tables. Every sentence earns its place.
6. **No framework codes in narrative prose** — never write "T1" or "W03" or "TPS" in a sentence
   meant for a human reader. Codes belong only in tables (Transformation Landscape, Roadmap,
   Evidence Quality).
