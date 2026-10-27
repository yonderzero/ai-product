---
name: moat-scan
description: 4-pillar, 24-lever defensibility scan for a vertical market software (VMS) company — switching costs, domain knowledge, development speed/cost, distribution channel. Use when you need a direct read on how eroded a VMS vendor's moat is and where AI is accelerating that erosion.
---

# VMS MOAT Scan

Score a vertical market software company's competitive defensibility across 24 levers in four
pillars — Switching Costs (SC), Domain Knowledge (DK), Development Speed & Cost (DS),
Distribution Channel (DC) — and produce a strategic-mirror report for that company's own
leadership (CTO, CPO, CEO): what they actually have, what's eroding, where to invest to defend.

This skill is fully standalone: it runs its own research pass every time, with no shared cache
and no dependency on any other skill or report. If the user has run other research skills in this plugin on the
same company, do not read their output — research this one fresh.

Adapted from VMS-Analyzer's `moat/moat-agent.md` + `moat/moat-framework-definition-spec.md`.

## Inputs

Ask the user (if not already given) for:
- **Company name** and, ideally, its website/domain — disambiguates from similarly-named companies.
- **Product to scope to**, if the company has multiple products/lines — otherwise scan the company as a whole.

## Phase 1: Research

Full rubric, all anchors, exposure tags, and evidence rules: `references/moat-framework-spec.md`
— read it in full before scoring anything.

Run your own WebSearch/WebFetch pass. There is no cache to fall back on, so budget generously —
roughly 15–25 searches/fetches, enough to cover all four pillars with real evidence rather than
inference. Suggested angles per pillar (not a rigid checklist — follow the evidence):

- **SC (switching costs):** the product's integrations/marketplace page, user reviews on
  G2/Capterra/TrustRadius (search for "migration", "switching", "onboarding", "implementation
  time"), pricing/contract terms page, case studies mentioning implementation length.
- **DK (domain knowledge):** the vertical's regulatory bodies and how long the product has
  served this vertical, product docs/help center for terminology, company blog/case studies for
  edge-case handling and years in market, any published benchmark reports.
- **DS (development speed/cost):** company age and funding history, engineering job postings
  (tech stack, team size), G2/Capterra reviews mentioning bugs/reliability, competitor feature
  comparison pages, any security/compliance certifications (SOC 2, ISO 27001, vertical-specific).
- **DC (distribution channel):** leadership bios and how long they've been in the vertical,
  conference sponsorships/speaker slots, partner/referral program pages, customer testimonials
  naming account teams, geographic footprint (offices, language support, local case studies).

Log roughly how many searches you ran per pillar — this goes in §7 Evidence Provenance.

## Phase 2: Score All 24 Levers

Score pillar by pillar, per the rubric and evidence rules in `references/moat-framework-spec.md`
§4 and §7. For each of the 24 levers: match evidence to the closest anchor (use the full 1–5
range — don't default to the 2–3 band), write a 2–3 sentence rationale citing the evidence,
tag `evidence` (`direct`|`inference`) and `evidence_confidence` (`High`|`Medium`|`Low`), and any
`flags`.

Before finalizing each pillar, sanity-check against `references/calibration-index.json` (frozen
snapshot of 16 prior scans — not live data, just an anchor-calibration reference): if every
lever in a pillar lands 2–3, re-check against the 1 and 4/5 anchors before accepting a flat
"moderate everywhere" pillar.

Write a `scores.json` in your working directory:
```json
{
  "company_name": "",
  "framework_version": "1.0",
  "scored_at": "",
  "levers": {
    "SC1": {"score": 0, "rationale": "", "evidence": "direct|inference", "evidence_confidence": "High|Medium|Low", "flags": []},
    "...": "... all 24 lever IDs: SC1-SC6, DK1-DK6, DS1-DS5, DC1-DC7 ..."
  }
}
```

## Phase 3: Compute Composites

Run the bundled script — do not compute pillar scores, exposure ratios, the composite, or the
mode by hand:

```
python3 scripts/compute_moat_score.py --scores scores.json --output composites.json
```

This gives you pillar scores, pillar exposure ratios, the MOAT composite, overall exposure
ratio, mode letter, and the `distribution_only` trigger. Use its values verbatim in the report.
Apply the judgment-based `ai_acceleration_risk` note yourself per §6 of the spec — the script
doesn't compute it.

## Phase 4: Write the Report

Structure and voice rules: `references/moat-framework-spec.md` §8. Sections in order: §1 Summary
block, §2 Verdict (exactly 3 sentences), §3 Pillar Summary Table, §4 Pillar Analysis (SC/DK/DS/
DC), §5 Exposure Map, §6 Strategic Implications (Defend now / Act on / Watch), §7 Evidence
Provenance, §8 Evidence Quality table.

Never use lever codes (SC1, DK3, etc.) in narrative prose — name the lever in plain English.
Codes belong only in the three tables (§3, §7 references, §8).

Deliver the report as the final message content (plain markdown), not as a file, unless the
user asks for a file.
