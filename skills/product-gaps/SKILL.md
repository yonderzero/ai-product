---
name: product-gaps
description: Product gap shortlist for a vertical market software (VMS) company — where the product is missing features the vertical needs, what competitors and AI-native entrants already ship, and what a well-funded challenger would build first. Use when you need a ranked, evidence-backed list of what to build or pitch next.
---

# VMS Product Gaps

Mine public signal — reviews, competitor feature pages, job postings, funded-startup activity,
regulatory change, technology shifts — to produce a ranked shortlist of product gaps for a
vertical market software company: features it's missing relative to what the vertical needs or
what an AI-native competitor could ship. Written for a founder/CPO deciding what to build next,
or for a pre-sales conversation about what a company is missing.

This skill is fully standalone: it runs its own research pass every time, with no shared cache
and no dependency on any other skill or report having run first. There is no pre-built product
map to check gaps against — Phase 0 below has you build a lightweight one yourself, from public
sources, before mining for gaps. If the user has run other research skills in this plugin on the same company, do
not read their output — research this one fresh.

Adapted from VMS-Analyzer's `ideation/ideation-agent.md` + `ideation/ideation-framework-definition-spec.md`.

## Inputs

Ask the user (if not already given) for:
- **Company name** and, ideally, its website/domain — disambiguates from similarly-named companies.
- **Product to scope to**, if the company has multiple products/lines — otherwise scan the
  flagship or most prominent product.

## Phase 0: Build the Product Baseline

Full detail: `references/product-gaps-spec.md` §2. Before you can call anything a "gap" you need
to know what the product already does. Spend a handful of searches/fetches on the product's own
website (features/product pages), docs or help center, pricing page, and its G2/Capterra listing
(the features tab there is often a fuller inventory than the vendor's marketing pages). Capture,
as a short working list — not a polished artifact:

- workflows the product covers today
- named modules/features it ships
- integrations it already lists
- AI capabilities actually shipped vs. merely announced/roadmapped

Any later candidate that turns out to already be covered by this baseline is not a gap — drop it.

## Phase 1: Research

Full rubric — research angles, candidate schema, confidence rules, category tags, overlap logic,
structural wedge detection: `references/product-gaps-spec.md` §3–§7. Read it in full before
mining candidates.

Run your own WebSearch/WebFetch pass. There is no cache to fall back on, so budget generously —
roughly 20–30 searches/fetches across the baseline and all four angle groups combined. Suggested
angles per group (not a rigid checklist — follow the evidence):

- **Internal/workflow-adjacency:** what logically precedes or follows the product's covered
  workflows that it doesn't touch; forum/community workaround threads ("we use a spreadsheet
  for X"); integration marketplace/Zapier/Make listings for things users repeatedly wire up
  manually.
- **Customer & market voice:** G2/Capterra/Trustpilot complaint patterns for the product and its
  direct competitors; competitor reviews praising a feature this product lacks; customer job
  postings (LinkedIn, Indeed, sector boards) describing manual work adjacent to the product's
  workflows; "alternatives to X" pages and any public win-loss/renewal-friction commentary.
- **Competitive & adjacent intelligence:** direct competitors' feature/pricing pages and release
  notes; recently funded startups (~last 24 months) and AI-native entrants targeting this
  vertical or an adjacent one — what unmet need is their funding thesis betting on; a similar
  product in an adjacent vertical with capabilities not yet brought to this market.
- **Environmental signals:** regulatory/compliance changes (~last 18 months) in the product's
  vertical and geography that create a reporting/data-capture gap; technology capability shifts
  (~last 12–24 months) that 2+ competitors have already shipped against.

Log roughly how many searches went to each group — this goes in the Run Statistics section.

## Phase 2: Identify and Rank Candidates

Per `references/product-gaps-spec.md` §4–§8: build each candidate against the schema (summary,
detail, category tag, confidence, evidence snippets, gap confirmation against the Phase 0
baseline, overlap tracking, structural wedge flag if applicable). Apply the confidence
upgrade/downgrade rules and the zero-review fallback where relevant. Detect overlaps across
research angles and apply the escalation/override rules before final ranking — full ranking
logic in §8.

Don't force every candidate into a research-angle bucket that doesn't fit; the four groups
organize the research, they don't gate what counts as evidence.

## Phase 3: Write the Report

Structure, voice, and the structural-wedge alert block format: `references/product-gaps-spec.md`
§9. Sections in order: Top 5 Product Opportunities (each with category, confidence, detail,
pitch angle, evidence — plus the wedge alert block for any `structural_wedge: true` entry),
Flagged for Review, All Candidates table, Evidence Quality table, Run Statistics.

Never use internal shorthand (research-angle labels, category codes, or candidate IDs like
`c_007`) in narrative prose — name the concept in plain English. Codes belong only in the All
Candidates table, Evidence Quality table, and Run Statistics.

Deliver the report as the final message content (plain markdown), not as a file, unless the user
asks for a file.
