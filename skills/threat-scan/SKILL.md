---
name: threat-scan
description: Evidence-based scan of 5 competitive/AI-driven attack vectors against a vertical market software (VMS) company, scored Confirmed/Likely/None found with a fabrication gate, plus a clearly walled hypothetical-scenarios section for vectors not yet Confirmed. Use when you need to know who is already attacking a VMS vendor and how a credible attacker could exploit its specific weak points next.
---

# VMS Threat Scan

Scan five attack vectors — point-solution unbundling, SMB full rebuild, integration/
interoperability layers, distribution bypass, and on-top/API wrappers — for named, sourced
evidence that someone is already attacking this specific VMS company. Score each vector
Confirmed / Likely / None found, compute a Threat Exposure Score (TES), then — in a clearly
banner-walled section, only for vectors that did NOT come back Confirmed — construct grounded
hypothetical attack scenarios built from this company's own researched weak points.

This skill is fully standalone: it runs its own research pass every time, with no shared cache
and no dependency on any other skill or report (including `moat-scan` — do not read its
output even if you have it from an earlier run). If the user has run other research skills in this plugin on the
same company, research this one fresh.

Adapted from VMS-Analyzer's `threat/threat-scan-agent.md` + `threat/attack-simulation-agent.md`
(merged — see `references/threat-framework-spec.md` §1 for why) +
`threat/threat-framework-definition-spec.md`.

Full rubric — vector definitions, evidence bars, the fabrication gate, TES math, combination
patterns, and the exact report skeleton with verbatim banner text: read
`references/threat-framework-spec.md` in full before scoring anything. This file (SKILL.md) is
the phase-by-phase operating sequence; the spec file is the source of truth if the two disagree.

**This is not a scoring skill in the bundled-script sense.** Unlike `maturity-score`,
`risk-score`, and `moat-scan`, there is no Python script here and no calibration-index
snapshot. The Threat Exposure Score is a simple count-based formula across exactly 5 vectors —
do the arithmetic yourself, inline, per Phase 4 below, and show your work in the report.

## Inputs

Ask the user (if not already given) for:
- **Company name** and, ideally, its website/domain — disambiguates from similarly-named
  companies and anchors the "built on {company}'s API" style searches.
- **Vertical / market** the company serves, if not obvious from the name — sharpens every query
  template below.
- **Product to scope to**, if the company has multiple products/lines — otherwise scan the
  company as a whole.

## Phase 1: Research (own WebSearch/WebFetch pass, budget 15–20)

There is no cache and no MOAT-agent handoff to pre-populate vectors, so all five start from
zero — this budget is higher than the source pipeline's post-cache top-up budget (which only
had to close gaps). Fire searches in parallel batches, not one at a time.

Allocation guidance (not rigid — follow the evidence, but don't spend the budget evenly out of
symmetry):
- **V4 (Distribution Bypass)** gets the largest share, 4–5 queries — it's the thinnest,
  hardest-to-source vector of the five.
- **V1 (Point-Solution Unbundling)** needs an initial review-site pass (G2, Capterra,
  TrustRadius, Reddit) to first *find* which module draws the most complaints/workarounds before
  you can search for a named alternative against it — there's no cache to hand you the weak
  module for free.
- **V2, V3, V5** typically need 2–4 queries each once you have the vertical and company name.

Query templates per vector (fill `{company}`, `{vertical}`, `{weak_module}`, `{current_year}`):
full templates and evidence bars are in `references/threat-framework-spec.md` §2. As you research
V1 in particular, hold onto the specific weak points you find (a module with clustered
complaints, thin docs, a missing integration, a fragmented partner program, slow onboarding,
etc.) — these feed the plain-English "weak point exploited" field in Phase 5, not any MOAT lever
code.

Copyright discipline: at most one quote per source, under 15 words; paraphrase everything else
in your evidence summaries.

## Phase 2: Status Assignment

Apply the evidence bars in spec §2, per vector: Confirmed | Likely | None found, with
`evidence_confidence` (High/Medium/Low) and `flags` (`single_source`, `stale_evidence`,
`no_named_entity`, `conflict_present`).

**Apply the fabrication gate (spec §4) before finalizing any status:**
- A vector cannot be Confirmed unless it has at least one named entity AND at least one source
  you actually retrieved this run.
- If either is missing, downgrade — to Likely if its bar is met, otherwise None found.
- Never invent a company name to fill a gap. "None found" is a valid, expected, reportable
  outcome — record what you searched so the negative result is auditable in "What We Did Not
  Find."

There is no script here to catch a fabrication after the fact (unlike the three scoring skills)
— this check has to happen while you're assigning statuses, not after.

Keep working notes per vector (status, named entities, sources with as-of dates if known,
evidence summary, confidence, flags) — you'll need all of this verbatim for both the Evidence
section and the TES arithmetic in Phase 4.

## Phase 3: Confirm the Wall Before Writing

Before drafting the report, decide which vectors are eligible for a hypothetical scenario:
**exactly the vectors that scored Likely or None found.** Any vector that scored Confirmed gets
a one-line pointer in the hypothetical section, never a scenario. Zero scenarios is valid output
if all five vectors came back Confirmed.

## Phase 4: Compute the Threat Exposure Score

Simple, fully specified arithmetic — do it by hand and show it:

```
TES = 2 × (count of Confirmed vectors) + 1 × (count of Likely vectors)
```

Bands (spec §5):

| TES | Band |
|-----|------|
| 0 | Quiet |
| 1–3 | Emerging |
| 4–6 | Contested |
| 7–10 | Under Attack |

Example: 2 Confirmed vectors and 1 Likely vector → `2×2 + 1×1 = 5` → **Contested**. Put the
substituted arithmetic in the report's Methodology Note so the number is auditable, not asserted.

## Phase 5: Construct Hypothetical Scenarios (walled section, non-Confirmed vectors only)

For each vector eligible per Phase 3, build one scenario grounded in what you actually found
about this company during Phase 1 — not a generic vertical-software scenario. Ask of every
scenario: *could this paragraph be pasted into another company's report unchanged?* If yes,
rewrite it using a more specific weak point from your own research.

Every scenario opens with this banner as a blockquote — **copy it verbatim, byte-for-byte:**

```
⚠️ HYPOTHETICAL — NO EVIDENCE OF ACTIVE ATTACKER. Red-team scenario for planning purposes only.
```

Required fields, exact labels, per spec §7:
- **Entry point** — how the attacker gets initial access, via a specific weakness you found for
  this company.
- **Wedge mechanic** — the initial value prop that gets the foot in the door, tied to a named
  complaint, gap, or workaround from your research.
- **Expansion path (12–36 months)** — staged path from wedge to real threat.
- **Weak point exploited** — plain-English description of the underlying weakness (e.g. "thin
  self-serve onboarding and no public API docs," "a single-region deployment with no local
  language support"). **Never a MOAT lever code (SC1, DK3, etc.) — there is no MOAT report to
  cite in a standalone run.** If you also ran `moat-scan` for this company separately, do not
  reference or reuse its lever IDs here; describe the weakness fresh, in your own words.
- **Combination risk** — exactly one of `wedge-then-expand` | `integration-plus-distribution` |
  `on-top-evolving-to-integration` | `none apparent` (spec §6 — check the tell-tale
  preconditions before claiming a pattern; default to "none apparent" rather than force-fitting
  one).
- **Time to threat** — exactly one of `12mo` | `24mo` | `36mo+`, anchored to how exposed the
  weak point is, not gut feel.

Attackers are archetypes ("a Series-A AI-native entrant with a conversational-first product"),
never invented company names. A real name may appear only as a precedent citation that traces
back to something in your Evidence section.

Voice inside a scenario block: war-game register, vivid about mechanism, never about evidence
that doesn't exist — present tense is fine ("the entrant ships…") because the banner frames it as
hypothetical throughout.

## Phase 6: Write the Report

Full skeleton, section order, and the exact divider between the two registers: spec §7. In
order: Threat Summary (TES + band + 5-row vector table) → Evidence: Vector Analysis (V1–V5, one
field block each) → What We Did Not Find → `---` divider → Hypothetical Attack Scenarios
(banner + framing + Confirmed-not-simulated pointer + one scenario block per eligible vector) →
Defensive Priorities (2–3 ranked moves tied to weak points named above) → Methodology Note (TES
arithmetic shown, search count/allocation, any staleness refresh).

Voice, Evidence section: evidence-report register. Every positive claim names its entity and
source; every negative result is stated plainly ("Three searches for embedded-payments expansion
in the vertical returned no named actor"). No speculation about what an attacker *could* do — that
lives only below the divider.

**Plain language throughout:** vector IDs (V1–V5) belong in tables and section headings only,
never in narrative prose — name the vector in plain English. No MOAT lever codes anywhere in
this report.

Deliver the report as the final message content (plain markdown), not as a file, unless the user
asks for a file.
