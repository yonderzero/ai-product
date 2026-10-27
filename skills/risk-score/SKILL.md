---
name: risk-score
description: 11-dimension risk assessment for a vertical market software (VMS) company — AI disruption exposure, market growth, regulatory shift risk, partner dependency, integration lock-in, substitution risk, disruption timing, price-value pressure, audit embeddedness, brand/trust strength, and tech stack obsolescence. Use when you need a direct read on what could go wrong for a VMS vendor and how exposed they are to it.
---

# VMS Risk Score

Score a vertical market software company's commercial and competitive risk across 11 active
dimensions in three sections — End Market Environment, Product Defensibility, Business Health —
and produce a risk report. Every dimension follows the same convention: **1 = safest/most
protected, 5 = most exposed/highest risk.**

This skill is fully standalone: it runs its own research pass every time, with no shared cache
and no dependency on any other skill or report. If the user has run other research skills in this plugin on the
same company, do not read their output — research this one fresh. This skill reports the Risk
composite only — there is no Maturity composite and no combined Mode quadrant here (that
required both composites plus a shared downstream step that doesn't exist in a standalone
skill); do not invite the user to "combine this with a maturity score" anywhere in the report.

Adapted from VMS-Analyzer's `assessment/risks-agent.md` + the Risk half of
`assessment/framework-definition-spec.md`.

## Inputs

Ask the user (if not already given) for:
- **Company name** and, ideally, its website/domain — disambiguates from similarly-named
  companies.
- **Product to scope to**, if the company has multiple products/lines — otherwise score the
  company as a whole.

## Phase 1: Research

Full rubric, all anchors, evidence rules, and report structure: `references/risk-framework-spec.md`
— read it in full before scoring anything.

Run your own WebSearch/WebFetch pass. There is no cache to fall back on, so budget generously —
roughly 15–25 searches/fetches, enough to cover all three sections with real evidence rather
than inference. Suggested angles per dimension (not a rigid checklist — follow the evidence):

- **R1 (AI disruption):** AI-native startups targeting this vertical, their funding
  announcements and product launches, category-defining platforms (Microsoft, Salesforce, etc.)
  entering the space, job postings or press mentioning "AI-native" competitors by name.
- **R2 (market growth):** industry analyst reports and market-size forecasts for the specific
  vertical (not the broad software sector), trade-press coverage of consolidation or
  contraction, funding activity in the category over the last 2–3 years.
- **R3 (regulatory/market shift):** the vertical's regulatory bodies and any pending rule
  changes, trade-press coverage of policy shifts affecting the sector, whether the company's
  product exists because of a compliance mandate (and whether that mandate looks stable).
- **R4 (partner/ecosystem dependency):** the product's reliance on specific cloud providers,
  marketplaces (App Store, Salesforce AppExchange, etc.), payment processors, or distribution
  partners; how concentrated that dependency is.
- **R5 (integration/lock-in depth):** integrations/marketplace page, API documentation depth,
  case studies describing ERP/payroll/compliance-system connections.
- **R6 (substitution/data portability):** G2/Capterra/TrustRadius reviews mentioning
  "migration", "switching", "export"; competitor comparison pages; whether the product is
  described as mission-critical or compliance-mandatory (review language like "non-negotiable").
- **R8 (timing of disruption):** the pace of competitor AI shipping (recent release notes,
  changelogs, product-hunt launches), funding velocity of AI-native entrants, whether
  category-leading platforms have shipped AI features in this exact workflow yet.
- **R9 (price-value pressure):** pricing page (or its absence — check historical snapshots),
  review-site complaints about cost, competitor price comparisons, analyst commentary on price
  positioning.
- **R10 (audit/SoD/approvals embeddedness):** product documentation or case studies mentioning
  approval workflows, segregation-of-duties controls, audit trails, or compliance certifications
  tied to financial or regulatory controls.
- **R11 (brand & trust strength):** G2/Capterra/Trustpilot review volume and sentiment, press
  mentions, analyst recognition, social proof on the company's own site (logos, testimonials).
- **R12 (tech stack obsolescence):** engineering job postings (tech stack, hiring for legacy vs.
  modern skills), engineering blog posts about modernization or migration efforts, review-site
  complaints about performance/reliability/UI datedness.

Log roughly how many searches you ran per section — this goes in the Methodology Note.

## Phase 2: Score All 11 Risk Dimensions

Score section by section, per the rubric and evidence rules in `references/risk-framework-spec.md`
§4 and §6. **R7 is retired (framework v2.0) — never score it, never mention it as if active.**

For each of the 11 active dimensions (R1–R6, R8–R12): match evidence to the closest anchor (use
the full 1–5 range — don't default to the 2–3 band), write a 2–5 sentence rationale citing the
rubric level and the evidence, tag `evidence_confidence` (`High`|`Medium`|`Low`), `score_basis`
(`direct_evidence`|`mixed`|`inference_heavy`), and any `flags`. Remember the locked direction:
**higher score always means higher risk**, even where that reads counter-intuitively (R5, R10,
R11 all score higher when the underlying thing that would normally read as "strong" — deep
integration, control embeddedness, brand trust — is instead weak or absent).

Before finalizing scores, sanity-check against `references/calibration-index.json` (frozen
snapshot of 16 prior scans — not live data, just an anchor-calibration reference): if every
dimension lands 2–3, re-check against the 1 and 4/5 anchors before accepting a flat
"moderate everywhere" read.

Write a `scores.json` in your working directory:
```json
{
  "company_name": "",
  "framework_version": "2.0",
  "scored_at": "",
  "dimensions": {
    "R1": {"score": 0, "rationale": "", "evidence_confidence": "High|Medium|Low", "score_basis": "direct_evidence|mixed|inference_heavy", "flags": []},
    "...": "... all 11 active dimension IDs: R1-R6, R8-R12 (no R7) ..."
  }
}
```

## Phase 3: Compute the Composite

Run the bundled script — do not compute the composite by hand:

```
python3 scripts/compute_risk_score.py --scores scores.json --output composite.json
```

This gives you the Risk composite (simple average of the 11 dimensions, 2 decimal places) and a
borderline flag if the composite lands within 0.1 of 3.0. Use its values verbatim in the report.
The script computes the composite only — no Maturity composite, no Mode quadrant, because there
is no shared step here to combine them into. Do not compute or reference a Mode quadrant
anywhere in this skill.

## Phase 4: Write the Report

Structure and voice rules: `references/risk-framework-spec.md` §7. Sections in order: §1 Risk
Summary block, §2 Top Risks, §3 Risk Landscape, §4 Watch-outs, §5 Open Questions for Interview,
§6 Methodology Note, §7 Evidence Quality table.

Never use dimension codes (R1, R9, etc.) in narrative prose — name the dimension in plain
English. Codes belong only in the Risk Landscape table and the Evidence Quality table. Do not
add a footer suggesting the user "combine this with a maturity score" or compute a quadrant
themselves — that combination is out of scope for this standalone skill.

Deliver the report as the final message content (plain markdown), not as a file, unless the
user asks for a file.
