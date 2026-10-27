# Product Gaps Framework Spec (standalone)

Condensed from VMS-Analyzer's `ideation/ideation-agent.md` + `ideation/ideation-framework-definition-spec.md`
for a standalone, single-pass skill. Source of truth for the research angles, candidate schema,
confidence rules, category tags, overlap logic, structural wedge detection, ranking, and report
structure. If anything in SKILL.md conflicts with this file, this file wins.

## 1. Purpose

A product gap analysis answers one question, per candidate: **what is being done manually,
outside the product, or by a competitor — that this product should be doing but isn't?**
Written for a founder/CPO audience evaluating where to invest next, or for a pre-sales
conversation about what a company is missing. Every candidate must be anchored to the specific
product and vertical — no generic "add AI" ideas.

There is no pre-built product map or research cache in this skill (unlike VMS-Analyzer's
pipeline, which anchors every candidate against a `pass2_product_market_map.json` produced by an
earlier pass). Standalone, you build a lightweight equivalent yourself in Phase 0 before mining
gaps — see §2.

## 2. Phase 0: Build the Product Baseline (replaces the product-map dependency)

Before any gap can be confirmed, you need to know what the product already does. Spend the first
few searches building a short baseline inventory from public sources: the product's own website
(features/product pages), docs or help center, pricing page (which often lists feature tiers),
and its listing on G2/Capterra (the "features" tab there is usually a fuller inventory than the
vendor's own marketing pages). Capture:

- **`workflows_covered`** — the end-to-end processes the product handles today (plain language,
  e.g. "invoice creation and sending", "subcontractor onboarding").
- **`modules_shipped`** — discrete features/modules by name.
- **`integrations_listed`** — third-party systems the product already connects to (marketplace
  page, Zapier/Make listing, docs).
- **`ai_shipped` vs `ai_announced`** — AI capabilities the product has actually shipped (in
  product today) vs. merely announced/roadmapped (press release, "coming soon" page). This
  distinction matters: a candidate cannot claim a gap the product has already shipped, and an
  announced-but-unshipped feature gets a confidence downgrade if it's used as the sole
  "this is absent" reason (see §5.2).

Keep this baseline short (a working list, not a polished artifact) — it exists so that every
later candidate can be checked against it before being called a genuine gap. If a candidate
turns out to already be covered by `modules_shipped` or `integrations_listed`, it is not a gap;
drop it, don't shortlist it.

## 3. Research Angles (replaces the 12-signal-source model)

VMS-Analyzer's ideation framework defines 12 active signal sources (I1–IV3) mined against a
shared cache. Standalone, there is no cache — every angle below is a fresh WebSearch/WebFetch
pass. The four groupings are preserved because they organize the research well and map cleanly
to category tags, but treat them as suggested angles, not a rigid checklist — follow the
evidence and don't force a search into a bucket it doesn't fit.

**I — Internal / workflow-adjacency signals** (→ mostly `gap`)
- What logically precedes or follows the workflows in `workflows_covered` that the product
  doesn't touch? (e.g. product handles invoicing but not payment reconciliation)
- Forum/community threads, review mentions of workarounds — "we use a spreadsheet for X",
  "we export to Excel because reporting doesn't do Y".
- Integration marketplace / Zapier / Make listings — what are users repeatedly wiring up that
  isn't a native integration?

**II — Customer & market voice** (→ `friction`, `parity`, `gap`)
- G2/Capterra/Trustpilot complaint patterns for the product and its direct competitors — a
  pattern (3+ independent reviewers) is a candidate; a single complaint is noise.
- Competitor reviews that praise a feature absent from this product (parity signal) — if the
  product has fewer than 3 own reviews with specifics across all three sites, this becomes the
  primary source; see the zero-review fallback in §5.3.
- Customer job postings (LinkedIn, Indeed, sector boards) for roles that describe manual work
  adjacent to the product's workflows — a role pattern repeated across 3+ companies in the
  vertical is a stronger signal than one posting.
- "Alternatives to X" / comparison pages and any public win-loss or renewal-friction commentary —
  features cited as a reason to switch or almost switch.

**III — Competitive & adjacent intelligence** (→ `parity`, `ai_gap`, `adjacency`)
- Direct competitors' feature/pricing pages and release notes — what do 2+ competitors ship that
  this product doesn't?
- AI-native entrants and recently funded startups (last ~24 months) targeting this vertical or an
  adjacent one — what unmet need is their funding thesis betting on? This is also where
  structural-wedge candidates get flagged (§6).
- A similar product in an adjacent vertical (same buyer archetype, similar workflow shape,
  different industry) — capabilities proven there but not yet brought to this market.

**IV — Environmental signals** (→ `regulatory`, `ai_gap`)
- Regulatory/compliance changes in the product's vertical and geography (last ~18 months) that
  create a reporting or data-capture requirement the product doesn't yet meet.
- Technology capability shifts (new AI models/APIs/platform capabilities, last ~12–24 months)
  that make a feature class newly viable, checked against whether 2+ competitors have already
  shipped something built on the shift.

Budget generously — roughly 20–30 searches/fetches across the baseline (Phase 0) and all four
angle groups combined, enough to ground candidates in real evidence rather than inference. Log
roughly how many searches went to each group; this feeds the Run Statistics section.

## 4. Candidate Schema

Every candidate carries:

```json
{
  "candidate_id": "c_001",
  "idea_summary": "One sentence, specific enough a PM immediately understands the proposal",
  "idea_detail": "2-4 sentences: the signal, where found, the gap, why it matters here",
  "category_tag": "gap | ai_gap | parity | adjacency | friction | regulatory",
  "confidence": "Weak | Moderate | Strong",
  "evidence_snippets": [{"url": "", "snippet": "", "source_class": ""}],
  "gap_confirmed": true,
  "gap_confirmation_note": "why confirmed absent from workflows_covered/modules_shipped/integrations_listed, or what's uncertain",
  "overlap_ids": [],
  "overlap_note": "",
  "structural_wedge": false,
  "structural_wedge_urgency_months": null,
  "flags": []
}
```

`idea_summary` — bad: "Add AI features." Good: "Automate subcontractor compliance certificate
chasing, currently done manually via email by operations staff."

`flags` — any of: `low_evidence`, `inference_heavy`, `borderline`, `conflict_present`,
`single_source`, `needs_validation`, `marketing_only_source`, `announced_not_shipped`.

## 5. Confidence Levels

| Level | Definition |
|---|---|
| **Weak** | Single signal from one source. Plausible but thinly supported. Needs human validation before use in a pitch. |
| **Moderate** | 2–3 signals from one source or class, or light corroboration from a second source type. Credible. |
| **Strong** | Independent signals from 2+ distinct research angles pointing at the same gap, or 4+ independent signals within one angle all pointing the same way. Ready to use without further validation. |

### 5.1 Overlap Upgrade Rule

When the same underlying gap is surfaced by more than one research angle (§3), that's an
overlap — see detection method in §7. Apply:

- 1 overlap from a **different** angle group → upgrade one level (Weak→Moderate, Moderate→Strong).
- 2+ overlaps from different angle groups → upgrade directly to Strong.
- Overlaps within the *same* angle group don't upgrade (they often mine the same evidence pool).
- **Independent confirmation requirement:** the upgrade only applies if the overlapping
  candidates cite at least one distinct evidence URL each. If both cite only the same underlying
  source (e.g. the same review-site page surfaced twice under different searches), that's not
  independent confirmation — don't upgrade; note "Same-source overlap: no upgrade applied" in
  `overlap_note`.

### 5.2 Downgrade Rule

Downgrade one level if:
- The only evidence is the target company's own marketing material (self-reported gaps are
  unreliable) — flag `marketing_only_source`.
- The signal is >24 months old with no corroboration.
- The "gap" is actually in `ai_announced` from the Phase 0 baseline (announced ≠ shipped, but
  also ≠ absent) — flag `announced_not_shipped` and reframe the candidate around the risk that
  the announcement stalls, rather than claiming the capability doesn't exist at all.

### 5.3 Zero-Review Fallback

Niche B2B VMS products frequently have zero or near-zero public reviews. If fewer than 3
own-product reviews with specifics turn up across G2/Capterra/Trustpilot and product-specific
community searches: fall back to competitor-praise-as-parity — features reviewers praise in
direct competitors that are absent from this product's baseline. Tag these `parity`, note
"derived from competitor praise (own-product reviews unavailable)" in `gap_confirmation_note`,
and apply a one-level confidence downgrade versus what the signal would otherwise earn (a
would-be-Strong candidate caps at Moderate; a would-be-Moderate caps at Weak).

## 6. Structural Wedge Flag

A structural wedge is a sharper risk than a standard feature gap: a funded third-party tool is
actively consuming the target product's structured data output and building an AI/analytics
layer on top of it as its primary value proposition — not just filling a feature hole. The
defining risk: every customer using the workaround generates training/usage signal for a tool
that could become a full-stack replacement.

Flag `structural_wedge: true` when all three hold:
1. A third-party tool explicitly ingests data the target product generates (e.g. its OCR output,
   invoice data, attendance records).
2. That tool's primary value proposition is an AI/analytics layer built on top of that ingested
   data.
3. The third party has raised funding (any stage) or shows documented adoption at scale.

Estimate `structural_wedge_urgency_months` from funding stage and integration density:

| Third-party stage | Integration density | Urgency |
|---|---|---|
| Seed (pre-Series A) | <50 integrations, no named competitor integrations | 24–36 months |
| Series A | Active competitor integrations, growing customer base | 12–18 months |
| Series B+ | >200 integrations, or actively marketing against the target | 6–12 months |
| — | Competitor has shipped a native equivalent and markets against the gap | <6 months |

**Geography adjustment:** if the target product serves a geographically segmented market
(e.g. Africa, APAC, LATAM, CEE, MENA, or anywhere with import-substitution or local regulatory
requirements) and the wedge tool has no documented local/regional presence, add 12–18 months to
the table estimate and note why (local compliance and institutional-trust dynamics extend the
build window). If the wedge tool already has confirmed regional customers or localization
investment, use the table as-is.

Any `structural_wedge: true` candidate with urgency ≤ 18 months is escalated to the top of its
confidence tier for ranking (§8) and must appear in the shortlist if `gap_confirmed = true`.

## 7. Overlap Detection

Two candidates overlap if they describe the same missing capability and came from different
research angles. Exact wording match isn't required — apply, in order, until one settles it:

1. **Keyword overlap:** 3+ shared nouns/verbs (same root, ignoring tense/plurality) between the
   two `idea_summary` fields.
2. **Conceptual mapping:** same core workflow, same customer pain point, or same role/department
   affected, even with different wording.
3. **Manual read:** if 1–2 are inconclusive, read both `idea_detail` fields in full and judge.

Record which criterion triggered it in `overlap_note` (e.g. "Keyword overlap (4 shared:
ticket, categorization, automation, AI). Different angles (II vs III).").

When overlap is detected: keep the higher-base-confidence candidate as primary, set its
`overlap_ids` to the secondary candidate(s), apply §5.1, and mark secondaries
`overlapped_by: <primary_id>` — they stay in the evidence pack (visible in All Candidates) but
don't get their own shortlist slot.

## 8. Ranking

1. Confidence (Strong, then Moderate, then Weak).
2. Overlap count within the tier (more independent overlaps ranks higher).
3. Category priority within a tier: `gap` and `ai_gap` rank above `parity`, `adjacency`,
   `friction`, `regulatory`.
4. **Structural wedge escalation:** any `structural_wedge: true` candidate with urgency ≤ 18
   months jumps to the top of its confidence tier (displacing the lowest-ranked candidate if the
   shortlist is already full at 5).
5. **Regulatory override:** a `regulatory` candidate whose mandate is active or takes effect
   within 12 months, and is non-optional for the buyer type, ranks above all same-confidence
   `gap`/`ai_gap` candidates. Document the deadline and applicability explicitly.

## 9. Report Structure

Shortlist = top 5 ranked candidates where `gap_confirmed = true` AND confidence ≥ Moderate. If
fewer than 5 qualify, fill with the strongest Weak candidates, flagged `needs_validation`.
High-ranking candidates that failed gap confirmation go to Flagged for Review instead of the
shortlist.

Pitch angle by category: `gap` → the workflow happening outside the product · `ai_gap` →
competitor AI shipping and the retention risk it creates · `parity` → the feature competitors
ship that this product lacks · `adjacency` → the proven pattern in an adjacent vertical ·
`friction` → the recurring complaint and workaround burden · `regulatory` → the mandate and what
the product would need to capture or output.

**Plain language:** never use internal shorthand (angle group labels like "II", category codes,
or candidate IDs like `c_007`) in narrative prose. Name the concept in plain English — "a gap in
scheduling automation," not "c_007"; "competitor AI shipping," not "the ai_gap category." Codes
belong only in the All Candidates table, Evidence Quality table, and Run Statistics.

Report sections, in order:

```markdown
# Product Gap Analysis — {company_name}

**Vertical:** … | **Product:** … | **Generated:** {date}

## Top 5 Product Opportunities
### 1. {idea_summary}
**Category:** … | **Confidence:** …
{idea_detail — 3-5 sentences}
**Pitch angle:** …
**Evidence:** {bullets with URLs}
[if structural_wedge: true — insert the wedge alert block below the evidence bullets]
[ranks 2-5]

## Flagged for Review
[high-ranking, gap_confirmed = false candidates, with the specific uncertainty named]

## All Candidates
| Rank | Idea | Category | Confidence | Gap Confirmed |

## Evidence Quality
| Rank | Idea | Confidence | Evidence Basis | Flags |

## Run Statistics
[candidates generated / after consolidation, overlap clusters found, Strong/Moderate/Weak
counts, wedge count, searches run, generated timestamp]
```

**Structural wedge alert block** (required immediately under the evidence bullets for every
`structural_wedge: true` entry in the Top 5, regardless of its category tag):

```markdown
> **STRUCTURAL WEDGE ALERT — Urgency: {structural_wedge_urgency_months} months**
>
> {Name the third-party tool consuming the target product's structured data output.} {Its
> funding stage and integration/customer count.} {The specific data flow being monetized, e.g.
> "This tool consumes [product]'s structured [data type] output and builds [capability] on top
> of it."} Build window estimated at **{urgency} months** — {the specific velocity signal behind
> the estimate}.
```

Voice: direct, specific (name the competitor, the review, the job posting — not "some
reviewers"), honest about confidence and evidence gaps. Written for a founder/CPO with 15
minutes, not a research report for its own sake.
