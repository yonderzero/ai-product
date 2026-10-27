# Maturity Framework Spec (standalone)

Condensed from VMS-Analyzer's `assessment/framework-definition-spec.md` (the Maturity half —
Sections A/B/C only) for a standalone, single-pass skill. Source of truth for all dimension
rubrics, section weights, composite math, and report structure. If anything in SKILL.md conflicts
with this file, this file wins.

## 1. Purpose

A Maturity assessment answers one question: **how strong, defensible, and forward-ready is this
vertical market software (VMS) business today?** The framework decomposes that question into 12
dimensions across 3 sections, each scored 1–5. Written to give a buyer, operator, or acquirer a
grounded, evidence-based read — not a sales pitch, not a guess.

This skill scores Maturity only. There is no Risk composite and no combined Mode quadrant here —
those require a Risk score from a companion pass that this standalone skill does not run. See §6.

## 2. Framework Overview

| Section | ID | Dimensions | Weight |
|---|---|---|---|
| Business Quality | A | A1–A6 (6) | 0.40 |
| Customer Strength | B | B1, B3 (2 — B2 retired v2.0) | 0.35 |
| AI Opportunity | C | C1–C4 (4) | 0.25 |

**B2 (Customer Engagement) is retired as of framework v2.0.** It scored exactly 3 for every
company analyzed under v1.x — zero cross-company variance, chronically inference-heavy from
public sources (engagement depth is not observable from outside a company). Its observable
fragments live on in B1 (behavioral switching propensity) and B3 (embeddedness). Never score B2.

## 3. Scoring Direction

Maturity uses `1 = weakest/least mature`, `5 = strongest/most mature`. Higher is always better.

## 4. Section A — Business Quality (weight 0.40)

### A1: Type of System — `Auto`

Core question: what operational layer does this product occupy for the customer? Does not
measure customer loyalty, compliance embeddedness, or technical quality — that's A3, B3, R10.

| Score | Anchor |
|-|-|
| 1 | System of Engagement. Front-end interaction layer only; not a source of truth, not central to core workflows. |
| 2 | System of Action. Coordinates/automates work but relies on another system as the main source of truth. |
| 3 | System of Record in a simpler domain. Trusted source of truth, but for a less complex or regulated area. |
| 4 | System of Record in a moderately complex domain. Core operational system in a meaningful business area. |
| 5 | System of Record in a highly regulated, high-volume, or highly complex domain. Foundational to the customer's operation. |

Common traps: treating all workflow software as System of Record; over-scoring customer-facing
experience layers that don't hold real data of record.

### A2: Vertical Market Software — `Auto`

Core question: how specifically built is the product for its vertical? Does not measure market
share, retention, or product quality.

| Score | Anchor |
|-|-|
| 1 | Generic horizontal product with minimal vertical specificity. |
| 2 | Some vertical relevance, but primarily horizontal. |
| 3 | Mixed — vertical modules exist, but substantial horizontal overlap remains. |
| 4 | Predominantly vertical-specific; vertical workflows, local rules, and domain data are meaningfully embedded. |
| 5 | Built specifically for the vertical; most of the product is vertical-native and supports core business processes deeply. |

Common traps: scoring from marketing language instead of workflow specificity; confusing niche
branding with genuine vertical depth.

### A3: Mission Criticalness — `Inferrable`

Core question: how operationally painful is it for the customer if this product fails? This is
about operational continuity, not audit/regulatory exposure (that's R10) or brand trust.

| Score | Anchor |
|-|-|
| 1 | Non-essential. Customers could operate normally without it. |
| 2 | Helpful but not central. Failure is inconvenient rather than serious. |
| 3 | Moderately important. Failure impairs operations but the organization continues to function. |
| 4 | Crucial to core operations. Failure causes major disruption and costly workarounds. |
| 5 | Essential to core operations. Failure materially stops or severely damages the customer's ability to operate. |

Common traps: over-scoring products with important data but low operational dependence; importing
compliance-criticality logic that belongs to a different lens entirely.

### A4: Market Position — `Auto`

Core question: how strong is the company's current competitive position in its market? A
present-day measure, not a future-disruption measure.

| Score | Anchor |
|-|-|
| 1 | Small player, unclear player, or weak competitive standing. |
| 2 | Meaningful participant but clearly behind the category leader. |
| 3 | Shared leadership or a strong second player with defensible relevance. |
| 4 | Clear market leader in the relevant segment or geography. |
| 5 | Dominant player with very strong share or near-default status in the relevant market. |

**Niche sub-segment rule:** for a specialist VMS vendor whose real market is a defined sub-segment
(e.g. agricultural CTRM vs. all-commodity CTRM/ETRM, or dental practice management vs. all
healthcare software), score relative to that competitive sub-segment, not the broad category —
and document which segment was used. **Module-within-platform rule:** if scoping to a module
within a larger platform, score against the module's own functional competitive set, not the
platform's overall position, and document that choice.

Common traps: mistaking recognition for dominance; scoring against the broad category when the
company competes in a well-defined niche (under-scores niche leaders, over-scores thin
generalists).

### A5: Leadership Mindset — `Inferrable`

Core question: how much ownership and entrepreneurial drive does leadership show? Does not
measure roadmap quality, technical modernity, or customer intimacy.

| Score | Anchor |
|-|-|
| 1 | Reactive leadership. Responsibility is externalized; change is not self-driven. |
| 2 | Some responsibility is taken, but leadership remains mostly reactive. |
| 3 | Developing ownership. Leadership shows initiative but not consistently. |
| 4 | Entrepreneurial leadership. Proactive, forward-looking, and accountable. |
| 5 | Strong ownership mentality. Leadership behaves like owners and sets a high standard for the organization. |

**Portfolio ownership note:** when the company is owned by a PE firm or strategic portfolio owner
(e.g. Constellation Software, Volaris Group, Vista Equity, TA Associates, Thoma Bravo, Francisco
Partners), separate the leadership mindset score (how proactive the team is within its
constraints) from the investment authorization pathway (what AI R&D capital is actually
available). For permanent-hold, decentralized-capital owners (Constellation/Volaris model), score
per-operating-company evidence and default to a note of "discretionary budget for incremental
work" rather than penalizing the absence of a portfolio-wide AI mandate — that's the expected norm
for that ownership model, not a negative signal. For finite-fund PE ownership, a portfolio-level
AI investment mandate is a positive signal worth naming explicitly. Note both readings in the
rationale if they diverge — do not let investment-authorization constraints drag down a genuinely
entrepreneurial team's score.

**Complementary note (not score-changing):** where evidence supports it, note the size and years
of collective vertical domain expertise held in the implementation/support/product organization,
and whether it's concentrated in a few key people or distributed and actively retained. This is a
defensibility annotation, not part of the A5 score itself.

Common traps: equating polished messaging with genuine ownership; over-weighting founder status
alone.

### A6: Technology Modernity — `Auto`

Core question: how much is the technology stack a positive capability asset? This is the positive
capability lens — not the liability lens, not customer lock-in, not current AI product revenue.

| Score | Anchor |
|-|-|
| 1 | Severely legacy stack that materially constrains product velocity and modern capability development. |
| 2 | Aging stack with meaningful limitations and weak modern capability headroom. |
| 3 | Mixed modern/legacy environment. Some modern capability exists, but technical debt is still material. |
| 4 | Mostly modern stack. Good current capability, manageable debt, practical AI readiness. |
| 5 | Modern, well-supported, AI-ready stack that acts as a genuine product capability advantage. |

Common traps: scoring aspirations instead of current capability; treating "cloud migration
underway" as equivalent to modernity already achieved.

## 5. Section B — Customer Strength (weight 0.35)

### B1: Customer Switching Propensity — `Inferrable`

Core question: how behaviorally unlikely are customers to switch? This is behavioral inertia, not
structural lock-in, data portability, or integration depth.

| Score | Anchor |
|-|-|
| 1 | Customers readily change systems when a better option appears. |
| 2 | Customers may switch with clear ROI or a compelling alternative. |
| 3 | Customers are selective and slower-moving, but switching is still realistic. |
| 4 | Customers prefer to keep incumbent platforms and add around them. |
| 5 | Customers are deeply conservative and highly resistant to switching. |

Evidence hierarchy (behavioral dimension — applies to B1 and B3 alike): demonstrated behavior
(churn data, documented switching events, win/loss analysis) > structural signals (switching
costs, integration depth, contractual lock-in) > preference signals (testimonials, review
sentiment, NPS) > inference. **Do not score above 3 on a behavioral dimension with only
preference-signal evidence** — reserve 4–5 for scores backed by structural lock-in or demonstrated
switching/churn patterns.

Common traps: confusing customer conservatism with a technical inability to leave.

### B3: Customer Dependency & Embeddedness — `Inferrable`

Core question: how deeply is the product embedded in customer workflows? Does not measure purely
technical integration depth, compliance embeddedness, or customer conservatism alone.

| Score | Anchor |
|-|-|
| 1 | Peripheral product. Removal would be manageable with limited disruption. |
| 2 | Supports some meaningful workflows but is not deeply embedded. |
| 3 | Embedded in important workflows, with noticeable removal friction. |
| 4 | Deeply integrated into day-to-day operations. Removal would require significant redesign and retraining. |
| 5 | Operationally inseparable in the short to medium term. Removal would mean major operational redesign. |

Same evidence hierarchy and same "no 4/5 on preference-signal evidence alone" rule as B1.

Common traps: collapsing this into pure integration-surface counting; scoring based only on
contract length or tenure rather than actual workflow embeddedness.

**Module-within-platform note:** if scoping to a module inside a larger platform, B1 and B3 should
reflect the module's own switching/embeddedness reality, not the platform's — a customer can have
very high platform-level inertia while a specific module has real, independent alternatives. Note
the divergence explicitly if it's significant. Platform-level customer counts/retention/NPS are
legitimate supporting evidence when module-specific data is absent, but apply one confidence-level
reduction and label them as inherited platform signals.

## 6. Section C — AI Opportunity (weight 0.25)

### C1: Current AI Features — `Auto`

Core question: what customer-facing AI capability has the company actually shipped? Does not
measure AI urgency, AI revenue potential, or internal-only AI tooling maturity.

| Score | Anchor |
|-|-|
| 1 | No visible AI initiative or public AI signal. |
| 2 | AI is mentioned but with no meaningful evidence of active product capability. |
| 3 | AI roadmap or active development is visible, but customer-facing capability is not yet truly shipped. |
| 4 | AI features are in beta, pilot, or late-stage release preparation. |
| 5 | Customer-facing AI features are shipped and visibly part of the product story. |

**AI maturity stage calibration** (Houlihan Lokey Q1 2026 VMS market report, 2025 distribution):
Stagnating (14% of market, no AI action) → anchor 1. Emerging (46%, foundational capabilities,
struggling to scale) → anchor 2. Scaling (35%, defined strategy, generating value) → anchor 3–4.
Future-Built (5%, cutting-edge, substantial value) → anchor 5. A C1 of 5 implies top-5%-of-market
characteristics — requires strong evidence (agentic systems, continuous learning loops, documented
customer outcomes), not just a long feature list. Where attach-rate evidence exists (industry AI
feature attach rate reached ~80% in 2025, up from 42% in 2024), use sub-30% attach as a signal the
company sits at Stagnating/Emerging regardless of raw feature count.

Common traps: over-scoring AI messaging; counting internal engineering-productivity AI as
customer-facing product AI.

### C2: AI Initiative Urgency — `Inferrable`

Core question: how urgently does the business need to move on AI? Does not measure whether AI
features already exist, absolute AI revenue size, or risk score direction. **Higher score = less
urgency / more available time** (this direction is intentionally inverted from the intuitive
reading — a 5 means the category is not yet under strong AI pressure, which is a comfortable
position).

| Score | Anchor |
|-|-|
| 1 | Immediate urgency. Delay materially threatens competitiveness. |
| 2 | High urgency. Action needed soon to avoid meaningful disadvantage. |
| 3 | Moderate urgency. Time exists, but the window is not open-ended. |
| 4 | Low urgency. AI matters, but immediate competitive damage is limited. |
| 5 | Minimal near-term urgency. The category is not yet under strong AI pressure. |

**Competitive pace anchor:** score against what the competitive set has actually *shipped* in the
last 12 months, not merely whether AI competition exists in the abstract. Score 1–2 if a
category-defining competitor has shipped production AI capability in this company's core workflow
area within the last 12 months. Score 3 if AI-native competitors exist and are shipping but not
yet in direct competition with this company's core workflow. Score 4–5 only if the competitive set
shows limited active AI *shipment*, not merely limited AI ambition.

Common traps: confusing AI ambition with urgency; importing generic competitor fear without
category-specific shipping evidence.

### C3: AI Revenue Opportunity — `Inferrable`

Core question: how much realistic revenue upside could AI create? Does not measure whether AI has
already shipped, operational risk from AI disruption, or technical feasibility alone.

| Score | Anchor |
|-|-|
| 1 | Little to no visible AI monetization opportunity. |
| 2 | Theoretical opportunity exists, but commercial shape is weak or unclear. |
| 3 | Clear AI monetization potential is visible, but not yet proven. |
| 4 | AI commercial model is defined or in active pilot form. |
| 5 | AI is already creating revenue or very near-term paid expansion. |

**AI monetization stage anchors** (Houlihan Lokey Q1 2026): Stage 1 — Establish System of Record
(subscription/seat-based ARR, AI not a distinct line item) → 1–2. Stage 2 — Deepen Workflow and
Intelligence (ARPU expansion via premium AI tiers/add-ons, AI separately priced) → 3–4. Stage 3 —
Orchestrate the Ecosystem (transaction fees, take rates, outcome-based pricing; AI is the primary
commercial engine) → 5. A **data feedback flywheel** (daily workflow usage generates proprietary
data that continuously improves the model, reinforcing more usage) supports a higher score within
its stage band — note its presence or absence explicitly.

**Data rights downward adjustment:** if the AI monetization opportunity depends on training/
fine-tuning on data currently processed by a third-party provider (OCR vendor, document-processing
API, external enrichment service) and confirmed data rights for training are unresolved, lower the
score by one level from what the structural opportunity alone would support, or apply an
`inference_heavy`-style caveat noting the score assumes those rights get resolved. Never score
Stage 2+ purely on structural opportunity if a known data-rights prerequisite is unresolved.

Common traps: over-scoring generic "AI can help everyone" claims; confusing internal cost savings
with customer-facing revenue opportunity.

### C4: AI Labor Automation Upside — `Inferrable`

Core question: how much customer labor could this company automate and monetize? Does not measure
whether competitors might automate that work first, current AI feature maturity, or structural
market risk — this is the opportunity lens only.

| Score | Anchor |
|-|-|
| 1 | Little manual work remains. AI upside is limited. |
| 2 | Some manual work remains, but upside is narrow. |
| 3 | Meaningful manual workflows remain, but the opportunity is not yet clearly defined. |
| 4 | Significant automation upside is visible and well suited to productization. |
| 5 | Major customer labor automation upside exists and is highly monetizable if executed well. |

**Dual reading note:** the same automatable-labor pool that represents this company's upside is
also, in principle, a displacement surface a faster competitor could attack first. This skill
scores C4 once, as upside only — it does not separately score a threat-side reading (that
required a companion Risk pass this standalone skill doesn't run). If your own research surfaces
strong evidence that a competitor is already shipping AI automation into the same workflow
surface, say so plainly in the AI Picture section of the report as context, without inventing a
second score for it.

**Agentic AI frontier note:** identify which automation layer the opportunity sits in — the
ML/predictive layer (forecasting, risk scoring, anomaly detection; meaningful opportunity but
typically replicable over time) or the agentic layer (autonomous multi-step task execution,
cross-system orchestration, closed-loop scheduling/dispatching/compliance checks; higher ceiling,
harder to commoditize once embedded). Projected agentic share of AI-driven software value: ~29% by
2028, up from ~17% today. Companies whose manual-work surface suits the agentic layer should score
higher than companies whose only automation upside is at the ML layer — name the dominant layer in
the rationale.

Common traps: treating all manual work as equally monetizable; confusing customer pain with
actual productizable opportunity.

## 7. Composite Formula

```
Section A avg = (A1 + A2 + A3 + A4 + A5 + A6) / 6, round to 2 decimals
Section B avg = (B1 + B3) / 2, round to 2 decimals              # B2 retired v2.0 — never scored
Section C avg = (C1 + C2 + C3 + C4) / 4, round to 2 decimals

Maturity Composite = (A × 0.40) + (B × 0.35) + (C × 0.25), round to 2 decimals
```

This math is computed by `scripts/compute_maturity_score.py` — never eyeball it. The script also
flags a composite within 0.1 of the 3.0 reference point as borderline (see §8) — no Mode letter,
no Risk combination, just the flag and a note in the report.

## 8. No Mode Quadrant — Scope Boundary

VMS-Analyzer's pipeline combines a Maturity composite and a separately-run Risk composite into a
four-quadrant Mode (A/B/C/D) after both finish. This skill produces the Maturity composite only —
there is no Risk pass running alongside it, no shared script combining the two, and no partial
"go run risk-score and combine these yourself" instruction. If the composite lands within 0.1
of 3.0 (the reference threshold that used to gate Mode classification), name it as a borderline
read in the report and note which dimension(s) would need to move, and by how much, to clear that
threshold clearly in either direction — but do not invent or gesture at a Mode letter.

## 9. Evidence Rules (standalone)

There is no research cache in this skill — every dimension is scored from your own WebSearch/
WebFetch pass, done fresh each run. The assessor scores every dimension even when evidence is
weak, but must make the strength of that evidence visible — inference is allowed, silent certainty
is not.

Required per-dimension fields: `score` (1–5 int, rubric-led — anchor to the rubric level that best
fits the evidence, don't blend levels numerically), `rationale` (2–5 sentences citing the anchor
and evidence), `evidence_confidence` (`High`|`Medium`|`Low`), `score_basis`
(`direct_evidence`|`mixed`|`inference_heavy`), `flags` (any of: `low_evidence`,
`inference_heavy`, `conflict_present`, `boundary_risk`, `single_class_evidence`,
`stale_evidence_present`, `stale_majority`, `product_stage_early`, `inherited_evidence_base`).

**Confidence caps (mandatory):**
- All sources for a dimension from the same source class (`company_material`,
  `analyst_or_research`, `industry_press`, `customer_case_study`, `job_posting`, `competitor`,
  `forum`) → cap at Medium, flag `single_class_evidence`.
- Majority of sources older than 24 months → cap at Medium, flag `stale_majority`; any source
  older than 24 months → flag `stale_evidence_present`.

**Product lifecycle flags:**
- `product_stage_early` — product is under 18 months old. Applies to B1, B3 (both behavioral
  dimensions require an established customer base to observe true switching/embeddedness). Cap
  confidence at Medium; cap the score itself at 3 unless direct behavioral evidence exists (scores
  of 4–5 require demonstrated outcomes, not just designed structural intent).
- `inherited_evidence_base` — the product is a rebuild/successor of a legacy product, and most
  behavioral evidence (churn, switching, embeddedness) is documented for the *predecessor's*
  installed base rather than this product's own confirmed deployments — regardless of this
  product's own age. Applies to B1, B3. Same confidence cap and same "4–5 requires direct new-
  product evidence" rule as `product_stage_early`.

**Conflict handling:** every evidence conflict relevant to a dimension must be acknowledged in the
rationale — it may support the lower reading, the higher reading, or remain unresolved (either
non-score-changing or confidence-reducing). Interpret the conflict; never pretend it doesn't
exist.

**Boundary pairs** (dimensions easy to conflate — flag `boundary_risk` if two share >50% of the
same evidence or near-identical rationale): A3 (operational criticality) is adjacent to but
distinct from compliance criticality; A6 (positive tech capability) is the mirror of a liability
lens this skill doesn't score; B1 (behavioral inertia) is adjacent to but distinct from structural
lock-in; B3 (workflow embeddedness) is adjacent to but distinct from pure technical integration
depth. Keep each dimension's rationale grounded in what it — and only it — is defined to measure
(see each dimension's "does not measure" line above).

**Suspicious combinations worth a note in the report:** high B1 + low structural lock-in evidence
(loyal customers, thin structural moat); high C4 + low current AI shipping (upside without any
visible movement toward it yet); low A6 + claims of active modernization (stated intent without
demonstrated capability).

## 10. Report Structure

Voice: direct, specific (name dimensions in plain English, cite real evidence), honest (state weak
dimensions plainly, flag inferences). Written for someone with 15 minutes who needs a grounded
read, not a pitch. **Plain language: never use dimension codes (A1, B3, C4, etc.) in narrative
prose** — name the concept ("switching inertia is high," not "B1 scores 4/5"). Codes belong only
in the composite block, the dimension score table, and the Evidence Quality table.

**§1 Maturity Summary** — single block:
```
Company:            {company_name}
Maturity Composite:  {composite} / 5.0
  Section A (Business Quality):   {score}
  Section B (Customer Strength):  {score}
  Section C (AI Opportunity):     {score}
```
Include the borderline note verbatim if `compute_maturity_score.py` flagged one. No Mode letter —
see §8.

**§2 Verdict** — exactly three sentences: (1) what the business's maturity position actually is,
(2) its single strongest structural asset, (3) its single biggest maturity gap.

**§3 Dimension Score Table** — `| Dimension | Score | Evidence Confidence | Score Basis |`, one
row per active dimension (all 12 — never a B2 row).

**§4 Section Analysis** — one section per A/B/C. Sub-header `## Section {X} ({name}) — {score}/5.0`.
One paragraph (4–6 sentences) per section: what this section looks like in practice, the strongest
dimension and why, the weakest dimension and why, and what evidence anchors that read.

**§5 AI Picture** — the four Section C scores read together: is this company on-curve, behind, or
ahead of the market calibration anchors in §6 (C1)/§6 (C3)? Name the C4 automation-layer reading
(ML vs. agentic) explicitly. If research surfaced strong evidence of a competitor already shipping
AI automation into the same workflow surface C4 identifies as upside, name that context plainly —
without inventing a second score.

**§6 Strategic Priorities** — 3 actionable items grounded in the dimension scores: title, why now,
what a good outcome looks like in 12 months, and who inside the company would own it.

**§7 Watch-outs** — 3–4 questions raised by low-confidence dimensions or suspicious combinations
(§9).

**§8 Evidence Quality Table** — one row per dimension: `| Dimension | Score | Evidence
Confidence | Score Basis | Flags |`.

**§9 Evidence Provenance** — one or two sentences per section noting the research basis (roughly
how many searches, which source types). Name explicitly any dimension scored primarily by
inference.
