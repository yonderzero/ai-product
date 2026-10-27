# Threat Framework Spec (standalone)

Condensed from VMS-Analyzer's `threat/threat-framework-definition-spec.md` v1 (plus
`threat/threat-scan-agent.md` and `threat/attack-simulation-agent.md`) for a standalone,
single-pass skill. Source of truth for vector definitions, evidence bars, the fabrication gate,
TES math, combination patterns, and report structure. If anything in SKILL.md conflicts with
this file, this file wins.

## 1. Purpose

This scan answers one question in two strictly separated registers, inside a single report:
**who is already attacking this VMS company, and how could it plausibly be attacked next?**

- **Evidence section** — sourced only. Every claim names an entity and a source, or the vector
  is marked "None found." No hypotheticals, ever.
- **Hypothetical section** — speculative only, clearly banner-walled, built only for vectors
  that did NOT come back Confirmed. Every scenario is a red-team construction from this
  company's own researched weaknesses, never presented as something happening today.

The wall between the two registers is this framework's core integrity property. Evidence and
hypothesis never mix in the same block of output. **A false "Confirmed" is worse than an honest
"None found."**

In the source pipeline this was two chained agents (threat-scan, then attack-simulation, fed by
a MOAT agent's structured handoff and a shared research cache). None of that machinery survives
here: this skill runs its own research pass every time, derives its own read on the company's
weak points directly from what it finds during that pass, and drops all lever-ID grounding
("Moat under attack: SC1...") in favor of describing the weakness in plain English — there is no
MOAT report to cite from inside a standalone skill.

## 2. The Five Attack Vectors

Vector IDs are fixed and never renumbered.

### V1 — Point-Solution Unbundling

A competitor peels off one module — typically the incumbent's weakest — with a sharper, often
AI-native, single-purpose product, and wins users the incumbent still bills but no longer
delights.

**Search angles:** `"{company}" alternative {weak_module}` · `{weak_module} software for
{vertical}` · `site:g2.com OR site:capterra.com "{company}" {weak_module}` — plus a generic pass
over review sites for the company's own name to first identify which module draws the most
complaints/workaround mentions (there is no cache to hand you this — find it here).

**Evidence bars:**
- **Confirmed** — a named competitor actively marketed at the same vertical for that module, OR
  3+ independent reviews complaining about that specific module *and* naming an alternative.
- **Likely** — 3+ independent complaints about the module with no named alternative yet, or a
  named horizontal point solution with visible traction in the vertical but no explicit
  targeting of it.
- **None found** — searches ran; nothing met either bar.

### V2 — SMB Full Rebuild

A funded startup rebuilds the whole category for the segment the incumbent deprioritizes —
usually SMB, self-serve, at a lower ACV tier — and grows upmarket from under it.

**Search angles:** `{vertical} software small business self-serve pricing` · `{vertical} SaaS
startup funding {current_year}` · `"{company}" competitor SMB`.

**Evidence bars:**
- **Confirmed** — a named, funded company with self-serve/PLG pricing targeting the same
  vertical at a lower ACV tier than the company's core segment.
- **Likely** — a named, funded company in the vertical whose segment targeting or pricing motion
  is not yet public, or credible funding activity in the category without a confirmed vertical
  match.
- **None found** — searches ran; nothing met either bar.

### V3 — Integration / Interoperability Layer

An iPaaS or integration platform becomes the connective tissue across the incumbent and its
competitors, commoditizing the incumbent into an interchangeable back-end.

**Search angles:** `"{company}" site:zapier.com` · `site:make.com OR site:workato.com
"{company}"` · `{vertical} integration platform connector`.

**Evidence bars:**
- **Confirmed** — a named platform advertising a native connector to the company AND at least 2
  of its direct competitors.
- **Likely** — a named platform with a connector to the company OR broad connector coverage of
  the vertical, but not both yet.
- **None found** — searches ran; nothing met either bar.

### V4 — Distribution Bypass

A platform with existing distribution in an adjacent category — embedded payments, a
marketplace, a hyperscaler vertical cloud — bundles software into the vertical and reaches the
incumbent's buyers through a channel the incumbent doesn't control.

**Search angles:** thinnest-evidence vector of the five; give it the largest share of the search
budget (see SKILL.md Phase 2). `{vertical} embedded payments software` · `{vertical} embedded
software platform` · `{vertical} marketplace software bundle` · `AWS OR Microsoft OR Google
{vertical} industry cloud`.

**Evidence bars:**
- **Confirmed** — a named platform with existing distribution in an adjacent category publicly
  expanding into this vertical's software workflows.
- **Likely** — a named adjacent-category platform present in the vertical (e.g. payments only)
  without announced software expansion, or credible analyst/press signals of category entry.
- **None found** — searches ran; nothing met either bar.

### V5 — On-Top / API Wrapper

A third party builds on the incumbent's own API or ecosystem, owns an increasing share of the
user's day, and evolves from complement to substitute — or generalizes across multiple VMS
back-ends.

**Search angles:** `"built on {company}" OR "{company} API" app` · `"{company}" marketplace OR
app directory partner` · `{vertical} AI copilot works with existing software`.

**Evidence bars:**
- **Confirmed** — a named third-party app in the company's own ecosystem with substitutive
  scope, or an explicit API-dependent competitor.
- **Likely** — named on-top products in the vertical positioned across incumbents generally
  ("works with your ITSM/ERP/etc."), not yet naming the company specifically.
- **None found** — searches ran; nothing met either bar.

## 3. Status and Confidence Definitions

### Status (per vector, mandatory, exactly one of)

- **Confirmed** — a named, verifiable entity actively shipping or marketing against this
  company's segment, meeting the vector's Confirmed bar, with at least one independent source
  (company site, funding database, marketplace listing, review platform).
- **Likely** — pattern evidence meeting the vector's Likely bar: a named adjacent actor with
  credible motion, or 2+ independent indirect signals. A Likely without a named entity is
  permitted only when the status derives from strong indirect evidence — then `flags` must
  contain `no_named_entity`.
- **None found** — the searches ran and nothing met the bar. **None found is a valid, expected,
  reportable outcome — never force a finding to avoid it.** The "What We Did Not Find" section
  makes it auditable.

### evidence_confidence (per vector, mandatory)

- **High** — 2+ independent sources of different types (e.g. funding database + vendor site).
- **Medium** — 1 direct source.
- **Low** — a single source, or evidence that is thin/indirect/older (no cache exists here, so
  "stale" means: the only signal you found is from a fast-moving vector — funding, AI-native
  entrants — and is more than ~6 months old; run one refresh query before accepting it).

### flags vocabulary

`single_source` · `stale_evidence` · `no_named_entity` · `conflict_present`

## 4. The Fabrication Gate (non-negotiable)

**A vector marked Confirmed must have at least one named entity AND at least one source.** This
is the single most important rule in the framework — reproduced here as an explicit checklist
because this skill does not bundle a validation script the way the three scoring skills do:

- Before writing "Confirmed" for any vector, check: is there a real, named company/product in
  `named_entities`? Is there at least one source (URL, or a clearly described publication/listing)
  in `sources`?
- If either is missing, the status cannot be Confirmed — downgrade to Likely (if the Likely bar
  is met) or None found.
- **Never invent a company name to fill a gap.** Only names that appear in something you actually
  retrieved during this run. A false "Confirmed" is worse than an honest "None found."
- Apply this same self-check to every vector before moving to Phase 4 (TES) — there is no script
  to catch a violation after the fact in this skill, so the check has to happen while scoring.

## 5. Threat Exposure Score (TES)

```
TES = 2 × (count of Confirmed vectors) + 1 × (count of Likely vectors)      → integer 0–10
```

| TES | Band |
|-----|------|
| 0 | Quiet |
| 1–3 | Emerging |
| 4–6 | Contested |
| 7–10 | Under Attack |

This is simple, fully specified arithmetic across exactly 5 vectors — do it by hand, showing the
substituted numbers in the report's Methodology Note (e.g. "2 Confirmed × 2 + 1 Likely × 1 = 5 →
Contested"). No script, no calibration index — there is nothing to calibrate against for a
5-vector count-based score, unlike the 1–5 lever/dimension scores in the other three skills.

## 6. Combination Patterns (hypothetical section only)

Attack vectors chain. The hypothetical section may cite **only these three patterns by name**
(or "none apparent"):

1. **wedge-then-expand** — a point-solution attacker (V1) becomes a full rebuild (V2) once it
   owns a daily workflow. Tell-tale preconditions: the wedge module generates or holds the
   customer's operational data; the attacker's segment overlaps the incumbent's core, not just
   its deprioritized tier.
2. **integration-plus-distribution** — an interoperability layer (V3) acquires channel power
   (V4): once it connects the category, it can steer buyers. Tell-tale preconditions: the
   platform has connector coverage across the incumbent and competitors, plus an existing
   commercial relationship with the buyer (billing, marketplace, payments).
3. **on-top-evolving-to-integration** — a wrapper (V5) generalizes across multiple VMS back-ends
   and becomes an integration layer (V3), reducing each incumbent to a data store. Tell-tale
   preconditions: the wrapper's value prop is workflow-level rather than product-level; it
   advertises multi-backend support.

## 7. Report Structure

One report, two walled sections, in this order. Section headers below are canonical — do not
reorder or rename them.

```markdown
# Threat Exposure Scan — {Company Name}
*Generated: {date} | Own-research pass, no shared cache | Evidence section is sourced only —
hypothetical scenarios are clearly walled below and speculative*

## Threat Summary
**Threat Exposure Score: {N}/10 — {Band}**

| Vector | Status | Named entities | Confidence |
[5 rows, V1–V5. Vector IDs allowed in tables, never in prose.]

## Evidence: Vector Analysis

### V1 — Point-Solution Unbundling — {Status}
- **Status:** Confirmed | Likely | None found
- **Named entities:** {names, comma-separated, or "None"}
- **Evidence summary:** {1–2 sentences, paraphrased}
- **Confidence:** High | Medium | Low
- **Sources:** {url or named source} (as of {YYYY-MM if known}) — one per line

### V2 — SMB Full Rebuild — {Status}
### V3 — Integration / Interoperability Layer — {Status}
### V4 — Distribution Bypass — {Status}
### V5 — On-Top / API Wrapper — {Status}
[same field block each]

## What We Did Not Find
[Explicit negative results: which searches ran and returned nothing meeting the bar, per
None-found vector. Makes every "None found" auditable.]

---

## Hypothetical Attack Scenarios

> ⚠️ HYPOTHETICAL — NO EVIDENCE OF ACTIVE ATTACKER. Red-team scenario for planning purposes only.

[2–3 sentence framing: everything below this line is a constructed red-team scenario, not a
finding. Attackers are described as archetypes ("a Series-A AI-native entrant with a
conversational-first product"), not invented company names. Confirmed vectors above are never
simulated here — they get a one-line pointer instead.]

**Confirmed threats (not simulated):** {one line per Confirmed vector pointing back to the
Evidence section above, or "None — no vector was Confirmed."}

### Scenario: {archetype title} — {Vector name} (scan status: {Likely|None found})
> ⚠️ HYPOTHETICAL — NO EVIDENCE OF ACTIVE ATTACKER. Red-team scenario for planning purposes only.

- **Entry point:** {how the attacker gets initial access, via this company's specific
  researched weakness — named in plain English, no MOAT lever codes}
- **Wedge mechanic:** {the initial value prop that gets the foot in the door — tied to a
  specific complaint, gap, or workaround found during research}
- **Expansion path (12–36 months):** {staged path from wedge to real threat}
- **Weak point exploited:** {plain-English description of the underlying weakness this
  scenario leans on — e.g. "thin onboarding documentation and a fragmented partner program,"
  never a lever ID like "SC1"}
- **Combination risk:** wedge-then-expand | integration-plus-distribution |
  on-top-evolving-to-integration | none apparent
- **Time to threat:** 12mo | 24mo | 36mo+

[…one `## Scenario:` block per vector that scored Likely or None found. Zero scenarios is valid
output if all five vectors were Confirmed.]

## Defensive Priorities
[2–3 ranked moves, each tied to a specific weak point named above in plain English.]

## Methodology Note
[Searches fired (N of budget) and how allocated across vectors; TES arithmetic shown with
substituted numbers; any staleness refresh performed; any vector where Likely was assigned
without a named entity (`no_named_entity` flag) called out explicitly.]
```

## 8. Guardrails

1. **Never fabricate a company name.** Evidence section: only names that appear in something
   retrieved during this run. Hypothetical section: no invented real-company names ever —
   attacker archetypes only; a real name may appear solely as a precedent citation traceable to
   the evidence section above it.
2. **Search budget.** 15–20 WebSearch/WebFetch calls total, weighted toward V4 (thinnest,
   hardest-to-find evidence) — see SKILL.md Phase 2 for allocation guidance. There is no cache
   here to pre-populate vectors for free, so the budget is higher than the source pipeline's
   post-cache top-up budget.
3. **Copyright discipline.** At most one quote per source, under 15 words; `evidence_summary` is
   always paraphrased. Never reproduce review text verbatim.
4. **The wall.** No hypothetical content above the `---` divider; no unsourced "Confirmed"-
   register language below it. The two registers never share a paragraph.
5. **Confirmed vectors are never simulated.** A real threat is already scarier than a
   hypothetical one; the hypothetical section references it with a one-line pointer, nothing
   more.
6. **Plain language.** Vector IDs (V1–V5) belong in tables and section headings only, never in
   narrative prose — name the vector in plain English. No MOAT lever codes anywhere in this
   skill's output — there is no MOAT report to cite from a standalone run; describe weaknesses in
   plain English instead.
7. **Independence.** This skill does not read another skill's output, a shared cache, or a
   MOAT report. Every run derives its own view of the company's weak points from its own
   research pass, every time.
