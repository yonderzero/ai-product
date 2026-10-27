<!-- Instructions for the strength subagent run by ai-product-discovery. Files referred to as 'next to this file' are in this folder. Work in a scratch folder for scores.json. -->

# VMS Maturity Score

Score a vertical market software company's business maturity across 12 dimensions in three
sections — Business Quality (A1–A6), Customer Strength (B1, B3), AI Opportunity (C1–C4) — and
produce a grounded maturity report: what's structurally strong, what's weak, where the AI
opportunity actually sits.

Run your own research pass. The caller gives you the product's profile and the product manager's answers: use them to scope the product and as evidence tagged `[PM]`, but find public evidence of your own for every score. This skill produces the
**Maturity composite only** — there is no Risk composite and no Mode quadrant (A/B/C/D). That
classification only existed in the source pipeline because Maturity and Risk composites were
combined by a shared script after both agents finished; there is no shared step here, so it's
dropped rather than left as a manual "go run risk-score and combine these yourself" footer.

Adapted from VMS-Analyzer's `assessment/maturity-agent.md` +
`assessment/framework-definition-spec.md` (Maturity half only — dims A1–A6, B1, B3, C1–C4). B2
(Customer Engagement) is retired as of framework v2.0 and is never scored — see
`maturity-framework-spec.md` (next to this file) §2.

## Inputs

Ask the user (if not already given) for:
- **Company name** and, ideally, its website/domain — disambiguates from similarly-named companies.
- **Product to scope to**, if the company has multiple products/lines — otherwise assess the
  company as a whole. If scoping to a module within a larger platform, note that explicitly (it
  affects how A4, B1, and B3 should be read — see the framework spec §4/§5).

## Phase 1: Research

Full rubric, all anchors, evidence rules, and report structure:
`maturity-framework-spec.md` (next to this file) — read it in full before scoring anything.

Run your own WebSearch/WebFetch pass. There is no cache to fall back on, so budget generously —
roughly 15–20 searches/fetches, enough to cover all three sections with real evidence rather than
inference. Suggested angles per section (not a rigid checklist — follow the evidence):

- **Section A (business quality — A1–A6):** what layer of the customer's operations the product
  occupies (system of record vs. workflow tool vs. front-end — company site, product docs,
  integration/API pages); how vertical-specific vs. horizontal the product is (case studies,
  industry-specific terminology, vertical certifications); what happens operationally if the
  product goes down (uptime SLAs, customer testimonials on criticality, incident history);
  competitive standing in the specific sub-segment (G2/Capterra category rankings, analyst
  reports, "vs {competitor}" pages); leadership bios, founder statements, ownership structure (PE/
  strategic portfolio vs. independent — LinkedIn, Crunchbase, press releases on funding/
  acquisition); tech stack signals (engineering job postings, engineering blog, page performance/
  framework fingerprinting, any published architecture content).
- **Section B (customer strength — B1, B3):** reviews on G2/Capterra/TrustRadius searching for
  "switching", "migration", "hard to leave", "embedded in our workflow"; case studies describing
  depth of usage or years-long customer relationships; churn/retention figures if publicly
  disclosed (earnings calls, press, case studies); integration depth signals (marketplace/
  integrations page, partner ecosystem) as a structural-signal proxy when direct behavioral
  evidence is thin.
- **Section C (AI opportunity — C1–C4):** company's own AI feature announcements/roadmap page/
  changelog; press coverage of AI launches; competitor AI shipping activity in the same workflow
  area (to calibrate urgency); pricing page for AI add-on tiers or usage-based AI pricing (revenue
  opportunity signal); the volume and nature of manual/repetitive customer work the product
  currently only partially automates (to size labor automation upside); any public statements
  on data rights/training data sourcing if AI monetization depends on third-party-processed data.

Log roughly how many searches you ran per section — this goes in §9 Evidence Provenance.

## Phase 2: Score All 12 Dimensions

Score section by section, per the rubric and evidence rules in
`maturity-framework-spec.md` (next to this file) §4–§6 and §9. For each of the 12 active dimensions (never
B2): match evidence to the closest rubric anchor (use the full 1–5 range — don't default to the
2–3 band), write a 2–5 sentence rationale citing the evidence, tag `evidence_confidence`
(`High`|`Medium`|`Low`) and `score_basis` (`direct_evidence`|`mixed`|`inference_heavy`), and any
`flags`.

Before finalizing each section, sanity-check against `calibration-index.json` (next to this file) (frozen
snapshot of 16 prior maturity scans — not live data, just an anchor-calibration reference): if
every dimension in a section lands 2–3, re-check against the 1 and 4/5 anchors before accepting a
flat "moderate everywhere" section.

Write a `scores.json` in your working directory:
```json
{
  "company_name": "",
  "framework_version": "2.0",
  "scored_at": "",
  "dimensions": {
    "A1": {"score": 0, "rationale": "", "evidence_confidence": "High|Medium|Low", "score_basis": "direct_evidence|mixed|inference_heavy", "flags": []},
    "...": "... all 12 active dimension IDs: A1-A6, B1, B3, C1-C4 (no B2 — retired v2.0) ..."
  }
}
```

## Phase 3: Compute Composites

Run the bundled script — do not compute section scores, the Maturity composite, or the borderline
flag by hand:

```
python3 <this folder>/compute_maturity_score.py --scores scores.json --output composites.json
```

This gives you section scores (A/B/C), the Maturity composite, the borderline flag (composite
within 0.1 of 3.0), and lists of low-confidence and inference-heavy dimensions. Use its values
verbatim in the report. There is no Mode quadrant to compute — see
`maturity-framework-spec.md` (next to this file) §8 for why that's out of scope here.

## Phase 4: Write the Report

Structure and voice rules: `maturity-framework-spec.md` (next to this file) §10. Sections in order: §1
Maturity Summary block, §2 Verdict (exactly 3 sentences), §3 Dimension Score Table, §4 Section
Analysis (A/B/C), §5 AI Picture, §6 Strategic Priorities, §7 Watch-outs, §8 Evidence Quality
table, §9 Evidence Provenance.

Never use dimension codes (A1, B3, C4, etc.) in narrative prose — name the concept in plain
English. Codes belong only in the summary block, the three tables (§3, §8), and structured
metadata.

Write the report to the file the caller names, in plain markdown, and return the composite scores and a five-line summary.
