# Risk Framework Spec (standalone)

Condensed from VMS-Analyzer's `assessment/framework-definition-spec.md` (the Risk half only —
Sections I–III, R1–R12) for a standalone, single-pass skill. Source of truth for all dimension
rubrics, evidence rules, composite math, and report structure. If anything in SKILL.md conflicts
with this file, this file wins.

## 1. Purpose

A Risk assessment answers one question: **what could go wrong for this VMS vendor, and how
exposed are they to it?** The framework decomposes commercial and competitive risk into 11
active dimensions across three sections, each scored 1–5 with **higher always meaning greater
risk/exposure** — the reverse convention from a maturity or moat scan, where higher means
stronger. Written to be read alongside a diligence or account-planning process — honest,
specific, evidence-anchored.

**R7 (AI Labor Displacement Risk) is retired as of framework v2.0.** Across every prior company
scored, R7 never diverged from the maturity dimension it mirrors (C4) — both measured the same
automatable-labor surface from opposite directions, so R7 carried no independent signal. It is
dropped from scoring and from the composite; this skill scores only R1–R6 and R8–R12 (11
dimensions). Never score R7. Never mention it in a report as if it were active.

## 2. Framework Overview

Risk has 12 dimension IDs total (R1–R12), 11 of them active — 3 sections, no section weighting
(unlike Maturity, Risk uses a flat average across all 11 active dimensions):

| Section | ID | Dimensions |
|---|---|---|
| I — End Market Environment | R1–R4 | AI Disruption, Market Growth, Regulatory & Market Shift Risk, Partner & Ecosystem Dependency |
| II — Product Defensibility | R5, R6, R8 | Integration & Lock-in Depth, Substitution & Data Portability Risk, Timing of Disruption (R7 retired, skipped) |
| III — Business Health | R9–R12 | Price-Value Pressure, Audit/SoD/Approvals Embeddedness, Brand & Trust Strength, Tech Stack Obsolescence |

**Score direction, locked:** for every dimension in this framework, **1 = safest/most protected,
5 = most exposed/highest risk**. This is the opposite convention from a maturity or capability
scan — do not default to "higher is better" muscle memory from those frameworks.

## 3. Scoring Discipline

- Scores are integers 1–5, **rubric-led, not average-led**: match the evidence to the rubric
  level that fits best: do not blend levels numerically or default to the middle band out of
  caution. Use the full 1–5 range — an extreme score, well-evidenced, is more useful than a
  hedged 3.
- Score each dimension independently against its own rubric, before computing anything
  aggregate. Composites are computed deterministically by the bundled script — never by hand.
- Every score carries a `rationale` (2–5 sentences citing the rubric anchor and the evidence),
  `key_supporting_evidence` (named source + what it showed), `evidence_confidence`
  (`High`|`Medium`|`Low`), `score_basis` (`direct_evidence`|`mixed`|`inference_heavy`), and
  `flags` (see §6).

**Evidence confidence model** — reflects strength of evidence, not conviction:
- **High** — multiple directly relevant sources, limited contradiction, rubric fit well-supported.
- **Medium** — some direct evidence, some indirect or modest conflict; supportable but not
  deeply anchored.
- **Low** — weak base, heavy reliance on inference, unresolved conflicts materially affect
  interpretation.

**Confidence caps (mandatory):**
- All cited sources of the same type (e.g. all review-site quotes, all job postings) → cap at
  Medium, flag `single_class_evidence`.
- Majority of sources older than 24 months → cap at Medium, flag `stale_majority`; any single
  source over 24 months old → flag `stale_evidence_present`.

**Score basis model:** `direct_evidence` (score primarily follows strong direct evidence),
`mixed` (both direct evidence and meaningful inference), `inference_heavy` (largely inferential —
sparse, indirect, or conflicting evidence base). Expected pairings: High+direct_evidence,
Medium+mixed, Low+inference_heavy — other combinations are possible but should be rare and
explainable.

**Never refuse to score a dimension for lack of evidence.** An inference-based score, flagged
`inference_heavy` with `Low` confidence, is always better than an unscored dimension.

**Conflict handling:** acknowledge every evidence conflict relevant to a dimension in its
rationale. A conflict may support the lower reading, the higher reading, or remain unresolved —
note which, and if unresolved, reduce confidence rather than silently picking a side.

## 4. Dimension Rubrics

### Section I — End Market Environment

**R1: AI Disruption** — *How exposed is the company to AI-native competitive disruption?*
Measures exposure to AI-native or AI-enabled competitors in the relevant vertical. Does not
measure current market position, AI opportunity upside, or internal AI readiness — those are
separate lenses.

| Score | Definition |
|-|-|
| 1 | Little visible AI-native threat in the relevant market |
| 2 | Emerging threat exists, but limited real traction is visible |
| 3 | Meaningful AI-native competitive activity is visible and should be taken seriously |
| 4 | Strong AI-native threat is emerging and likely affecting decision-making |
| 5 | AI-native disruption is a major active threat to the company's position |

*Common traps:* over-scoring hype without real vertical relevance; treating healthy retention
metrics (NRR, churn, renewals) as evidence disruption risk is low — those are lagging
indicators reflecting decisions made 12–24 months ago. Anchor instead to forward-looking
signals: what AI-native entrants have recently shipped, their funding, and whether
category-defining platforms have begun competing in this vertical.

*Complementary assets note:* before finalizing R1, explicitly enumerate the complementary
assets this company owns that an AI-native entrant would need real time to replicate —
installed-base depth, multi-year contracts, compliance certifications embedded in the product,
deep ERP/government integrations, a trained implementation-partner network, proprietary
historical data, brand trust with slow-moving buyers. The more time-expensive these assets are
to replicate, the lower the effective disruption risk even in a market with active AI-native
competition — a strong complementary-asset base warrants capping R1 at 3 unless there's
evidence AI-native entrants are actively replicating those specific assets. Document the asset
inventory in the rationale.

**R2: Market Growth** — *How supportive or constraining is the underlying market growth
profile?* Measures structural growth or contraction of the company's underlying market. Does
not measure company share gains, pricing power, or AI disruption directly.

| Score | Definition |
|-|-|
| 1 | Strong market growth tailwinds; the market structure is supportive |
| 2 | Healthy market growth with generally favorable conditions |
| 3 | Stable or modest-growth market; neither strongly favorable nor adverse |
| 4 | Low-growth, stagnant, or structurally pressured market |
| 5 | Market contraction or serious structural weakness creates material growth risk |

*Common traps:* substituting company performance for market structure; using broad sector
growth figures instead of the actual relevant category.

**R3: Regulatory & Market Shift Risk** — *How likely are external regulatory or market shifts
to destabilize the company?* Measures the risk that regulation, policy, or market-structure
shifts redefine the operating environment in ways that materially matter. Does not measure
operational mission-criticality, audit embeddedness, or partner dependency.

| Score | Definition |
|-|-|
| 1 | Regulatory and market context is stable and predictable |
| 2 | Some change exists, but manageable and foreseeable |
| 3 | Moderate external change pressure exists and requires active adaptation |
| 4 | Frequent or materially significant shifts create meaningful exposure |
| 5 | Rapid or destabilizing changes create major strategic and product risk |

*Dual-role regulation:* some regulatory regimes both drive demand (compliance obligation
creates buyers) and carry adaptation risk (scope could shift, requirements could change,
addressable market could shrink). Score R3 on **net risk exposure**: a regulation that is
stable, well-defined, and actively driving demand should score low (1–2) even though the
product is "regulatory-dependent" — that dependency is protective, not risky. A rapidly
shifting regime creates genuine adaptation risk even where current demand is strong. Document
both readings in the rationale.

*Common traps:* confusing "heavily regulated" with automatically high risk; over-weighting a
regime that is actually stable and protective.

**R4: Partner & Ecosystem Dependency** — *How exposed is the company to external platforms,
partners, or ecosystem dependencies?* Measures risk from dependence on partners, external
platforms, cloud providers, marketplaces, or other third-party ecosystem layers. Does not
measure customer workflow embeddedness, direct substitution risk, or internal stack quality.

| Score | Definition |
|-|-|
| 1 | Dependencies are limited, diversified, or well-controlled |
| 2 | Some meaningful dependencies exist, but exposure is manageable |
| 3 | Dependence is moderate and creates real but not dominant risk |
| 4 | Heavy dependence on important external layers creates significant exposure |
| 5 | Extreme dependency on one or a few external ecosystems creates major structural risk |

*Common traps:* confusing a rich partner ecosystem with a safe ecosystem position — breadth of
partners is not the same as low dependency risk.

### Section II — Product Defensibility

**R5: Integration & Lock-in Depth** — *How much technical and workflow lock-in exists through
integrations?* Measures the depth of integrations and the re-integration effort required to
replace the product. Does not measure behavioral switching reluctance, broad operational
embeddedness, or data portability alone (those belong to R6/B-type dimensions).

**Score direction note:** counter-intuitively, higher R5 means *weaker* lock-in (easier
technical replacement), because the locked Risk-framework convention requires higher scores to
always mean higher risk.

| Score | Definition |
|-|-|
| 1 | Deep, mission-critical integrations make replacement highly difficult |
| 2 | Strong integration depth creates meaningful replacement friction |
| 3 | Moderate integration depth creates some defensibility but not extreme lock-in |
| 4 | Limited integration depth means replacement is fairly manageable |
| 5 | Minimal integration depth; technical replacement is relatively easy |

*Common traps:* treating any API presence as deep lock-in; conflating this with broader
workflow-embeddedness reasoning (a different, non-technical lens).

**R6: Substitution & Data Portability Risk** — *How structurally easy is it for a customer to
leave?* Measures ease of replacing the product, combining alternative availability with data
portability and migration practicality. Does not measure customer conservatism alone,
relationship depth, or integration depth alone.

| Score | Definition |
|-|-|
| 1 | Leaving is structurally difficult; alternatives are weak and migration is highly painful |
| 2 | Replacement is possible but structurally hard for most customers |
| 3 | Replacement is possible with meaningful effort and tradeoffs |
| 4 | Viable alternatives and data portability make leaving fairly realistic |
| 5 | Alternatives are credible and migration is practically achievable; structural substitution risk is high |

*Contract lock-in evidence note:* contract terms (length, exit clauses, exit penalties) are
rarely discoverable from public sources for privately-held VMS companies, so inference-based
scoring is the norm here. Exception: for operationally critical compliance SaaS (e.g. pesticide
compliance platforms, certificate management systems) where non-renewal creates immediate
regulatory or supply-chain exposure for the customer, the substitution barrier is structurally
high regardless of contract term length — score toward 1–2 even without direct contract
evidence, with `score_basis: mixed`, documenting the compliance-driven lock-in reasoning
explicitly. Review-site language like "non-negotiable" or "we couldn't operate without it" is a
high-confidence substitute for direct contract data.

*Common traps:* mistaking customer loyalty (a behavioral signal) for hard-to-exit product
structure (a technical/contractual one); ignoring data portability and migration-history
complexity.

**R8: Timing of Disruption** — *How soon is disruption likely to matter materially?* Measures
the likely time horizon over which disruption or erosion becomes commercially meaningful. Does
not measure absolute severity of the risk, AI opportunity size, or current product quality.

| Score | Definition |
|-|-|
| 1 | Risk is long-dated and unlikely to materialize materially in the near term |
| 2 | Risk is visible but likely several years away |
| 3 | Risk may materialize on a medium-term horizon |
| 4 | Risk is likely to matter in the near term |
| 5 | Disruption is immediate or already materially affecting outcomes |

*Common traps:* confusing long-term significance with short-term immediacy; over-relying on
lagging business-health metrics (current NRR, churn, renewals) as evidence disruption timing is
distant. Revenue erosion from prior disruption waves typically lags disruption onset by 2–4
years — a company can look fully healthy while displacement is already underway. Anchor to
leading indicators: competitor AI shipment pace, AI-native funding activity in the vertical,
category-defining platform-level AI releases by market leaders.

### Section III — Business Health

**R9: Price-Value Pressure** — *How much pressure exists on pricing power relative to
delivered value?* Measures pressure on pricing power from cheaper alternatives, customer price
sensitivity, or weak value differentiation. Does not measure market growth, pure customer
engagement, or direct AI disruption.

| Score | Definition |
|-|-|
| 1 | Pricing power is strong and clearly defensible |
| 2 | Some pressure exists, but value remains relatively well defended |
| 3 | Mixed pricing picture; some pressure is visible |
| 4 | Significant price pressure is evident |
| 5 | Severe price-value pressure materially threatens defensibility or growth quality |

*Pre-revenue / early-revenue products (no public pricing data):* default to 2–3 with Low
confidence, flag `low_evidence`, anchor rationale to structural pricing-power indicators only
(compliance-grade value, switching costs, competitor pricing norms). Don't score above 3
without direct pressure evidence.

*Established products with undisclosed pricing:* absence of public pricing for a product
≥2 years old with a sustained base usually signals enterprise-sales opacity, not weak pricing
power. Default to 2–3 with Low confidence, flag `low_evidence`, and anchor to structural
indicators: value differentiation vs. named competitors, retention signals, competitive pricing
norms, indirect pricing comparisons. **Don't conflate pricing opacity with pricing weakness** —
a mission-critical system of record with intentional quote-based sales and low churn is not the
same as a struggling product unable to defend its price; such a product should score 1–2, not
3–4.

*Common traps:* over-relying on anecdotal review complaints; confusing premium price with
pricing power; scoring above Low confidence when there's no public pricing data.

**R10: Audit / SoD / Approvals Embeddedness** — *How much compliance or financial-control
exposure is tied to this product?* Measures how deeply the product is embedded in approvals,
segregation of duties, audit workflows, or regulated control processes. Does not measure
operational mission-criticality, general system centrality, or market trust.

**Score direction note:** higher R10 means *weaker* control embeddedness (higher risk) —
counter-intuitive relative to a "how embedded" framing.

| Score | Definition |
|-|-|
| 1 | Deeply embedded in control, approval, or audit processes; replacement would create major compliance disruption |
| 2 | Meaningfully embedded in approvals or audit-sensitive workflows |
| 3 | Some compliance relevance exists, but not as a central control layer |
| 4 | Limited role in approval or audit-sensitive workflows |
| 5 | Little or no meaningful embeddedness in controls, approvals, or audit-sensitive workflows |

*Common traps:* copying operational-criticality reasoning directly (a different lens); assuming
all back-office software is automatically deeply control-embedded.

**R11: Brand & Trust Strength** — *How much does brand and trust reduce commercial risk?*
Measures the strength of the company's reputation and market trust, both within the installed
base and in the broader market. Does not measure one-to-one relationship depth, workflow
embeddedness, or market share directly.

**Score direction note:** higher R11 means *weaker* brand/trust protection (higher risk).

| Score | Definition |
|-|-|
| 1 | Strong trust and reputation materially reduce commercial risk |
| 2 | Good brand and trust provide meaningful support |
| 3 | Brand/trust is adequate but not a strong moat |
| 4 | Brand/trust is weak or narrow, creating commercial vulnerability |
| 5 | Brand and trust strength are materially weak, increasing risk significantly |

*Zero-review-platform companies:* if no reviews or user-voice signals exist on G2, Capterra, or
Trustpilot, pre-flag R11 `single_class_evidence` and cap confidence at Medium unless a targeted
search locates direct behavioral signals. Don't burn search budget re-confirming an absence
already established — note it once in the Methodology section instead: "No public reviews
found on G2, Capterra, or Trustpilot. Behavioral scores are anchored to structural design
characteristics and preference signals rather than demonstrated behavioral outcomes."

*Common traps:* confusing installed-base satisfaction with broad market trust; over-weighting
analyst mentions alone.

**R12: Tech Stack Obsolescence** — *How much is the technology stack a liability?* Measures how
much the stack creates risk through obsolescence, talent scarcity, modernization cost, and weak
AI readiness. Does not measure the positive capability side of the stack, customer engagement,
or market positioning — this is the liability lens, not the capability lens (a different
dimension elsewhere would score the positive side; don't blend the two readings here).

| Score | Definition |
|-|-|
| 1 | Little meaningful stack obsolescence risk |
| 2 | Some debt exists, but obsolescence risk is manageable |
| 3 | Mixed estate with meaningful obsolescence exposure |
| 4 | Significant obsolescence risk is present |
| 5 | Severe stack obsolescence meaningfully constrains competitiveness and modernization |

*Common traps:* conflating active modernization efforts with already-resolved risk; treating
one modern subsystem as proof the overall stack isn't obsolete.

## 5. Composite Formula

```
Risk Composite = (R1 + R2 + R3 + R4 + R5 + R6 + R8 + R9 + R10 + R11 + R12) / 11
Round to 2 decimal places.
```

R7 is retired and excluded. Interpretation: **lower composite = safer/more protected, higher
composite = more exposed.** This is computed by `scripts/compute_risk_score.py` — never eyeball
it. There is no Mode quadrant in this skill: the quadrant in the source framework only existed
because Maturity and Risk composites were combined by a shared downstream step, and there is no
such shared step here. Report the Risk composite on its own.

**Borderline note:** if the composite lands within 0.1 of 3.0 (the [2.9, 3.1] range), say so
explicitly in the report and name which dimension(s), moved by roughly one point, would shift
the composite meaningfully — a 3.00 and a 2.85 carry the same rough reading but different
strategic weight, and that distinction is worth a sentence.

## 6. Evidence Rules (standalone)

There is no research cache in this skill — every dimension is scored from your own WebSearch/
WebFetch pass, done fresh each run. Cite the specific finding (named source: review-site quote,
pricing page, press release, job posting, regulatory filing, competitor announcement, etc.)
behind each score.

Required per-dimension fields: `score` (1–5 int), `rationale` (2–5 sentences citing the rubric
anchor and evidence), `evidence_confidence` (`High`|`Medium`|`Low`), `score_basis`
(`direct_evidence`|`mixed`|`inference_heavy`), `flags` (any of: `low_evidence`,
`inference_heavy`, `conflict_present`, `single_class_evidence`, `stale_evidence_present`,
`stale_majority`, `interview_candidate`).

**Boundary-pair awareness (informational only, no cross-skill dependency):** in the source
framework, R5/R6/R10/R12 each sit in a boundary or dual-lens pair with a maturity dimension
(technical lock-in vs. behavioral switching, control embeddedness vs. operational
criticality, stack liability vs. stack capability). This skill has no maturity report to check
against, so there's nothing to reconcile — but keep the distinct lens for each R dimension
sharp in your own rationale (e.g. don't let R5's technical-integration read blur into a
behavioral-loyalty read that belongs to a different framework entirely).

## 7. Report Structure

Voice: direct, specific (name dimensions, scores, evidence), honest (weak dimensions stated
plainly, inferences flagged). **Plain language: never use dimension codes (R1, R9, etc.) in
narrative prose** — name the dimension in plain English ("weak pricing power" not "R9"). Codes
belong only in the Risk Landscape table, Evidence Quality table, and structured metadata.

**§1 Risk Summary** — single block:
```
Company:         {company_name}
Risk Composite:  {composite} / 5.0   (lower = safer, higher = more exposed)
Highest Risk:    {dimension name} ({score})
Lowest Risk:     {dimension name} ({score})
```
Include the borderline note here if the script flagged one.

**§2 Top Risks** — the 3 highest-scoring, most actionable dimensions: name, score, one-sentence
headline, 2–3 evidence points, urgency (Near-term / Medium-term / Structural).

**§3 Risk Landscape** — one paragraph per section (End Market Environment, Product
Defensibility, Business Health) summarizing key findings across its dimensions; note which
risks are accelerating vs. stable. Include a table: `| Dimension | Score | Section |`.

**§4 Watch-outs** — 3–4 questions surfaced by suspicious combinations or low-confidence
dimensions (e.g. strong current retention but high AI-disruption exposure; weak brand signal
paired with heavy price pressure).

**§5 Open Questions for Interview** — 3–5: dimension affected, specific question to ask, likely
score change if the answer is unfavorable. Prioritize dimensions flagged `interview_candidate`
or `inference_heavy`.

**§6 Methodology Note** — 2–3 sentences: research basis, any confidence-capping flags applied
(e.g. zero-review-platform, no public pricing), and the retired-R7 note if worth restating.

**§7 Evidence Quality** — table, all 11 dimensions: `| Dimension | Name | Score | Evidence
Confidence | Score Basis | Flags |`.
