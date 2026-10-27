---
name: company-brief
description: 7-facet factual snapshot of a vertical market software (VMS) company — identity, financials, products, tech stack, personas, people, competitive landscape. Use when you need a quick factual read on a company before a call, account review, or diligence pass. No scoring or judgment — facts only, each with a source.
---

# VMS Company Brief

Produce a factual, sourced snapshot of a vertical market software company across seven facets:
General, Financials, Products, Tech, Personas, People, Competitive Landscape. This is an
**observational** report — no scoring, no rubric, no verdict, no recommendation. It exists so
someone can walk into a call or a diligence review with the facts straight, each one traceable
to a source.

This skill is fully standalone: it runs its own research pass every time, with no shared cache
and no dependency on any other skill or report. If the user has run other research skills in this plugin on the
same company, do not read their output — research this one fresh.

Adapted from VMS-Analyzer's `intel/intel-agent.md`.

## Inputs

Ask the user (if not already given) for:
- **Company name** and, ideally, its **domain/website** — disambiguates from similarly-named
  companies and anchors the research.
- **Product to scope to**, if the company has multiple distinct products/lines — otherwise brief
  the company as a whole, covering its primary product first.

## Phase 1: Research

Full facet definitions, evidence/sourcing rules, and report structure: `references/company-brief-
spec.md` — read it in full before writing anything.

Run your own WebSearch/WebFetch pass. There is no cache to fall back on, so budget generously —
roughly 12–20 searches/fetches, enough to cover all seven facets with real sourced facts rather
than inference. Suggested angles per facet (not a rigid checklist — follow the evidence and stop
early on a facet once it's well covered):

- **General:** company's own "About"/"Company" page, Crunchbase/PitchBook-style profile pages,
  press releases and news search for the company name over the trailing 12 months, LinkedIn
  company page (headcount, founding year).
- **Financials:** funding announcements and press coverage, pricing page (subscription vs.
  license vs. usage-based cues), G2/Capterra pages for customer-count claims, any "customers"
  or "trusted by" page, review-site or news mentions of growth/expansion.
- **Products:** product/features pages, docs or help-center site, G2/Capterra/TrustRadius listing
  pages (category, review presence), integrations/marketplace page, case studies for reference
  customers, changelog or release-notes pages for AI feature lifecycle (GA/Beta/Roadmap).
- **Tech:** engineering job postings (stack keywords), engineering blog, status page or trust
  page (infra hints), any conference talks or case studies mentioning architecture.
- **Personas:** G2/Capterra review text (search for role titles alongside the company name),
  the vertical's trade-body or association sites, conference speaker/sponsor pages, product
  marketing pages that name target roles.
- **People:** company's own leadership/about page, LinkedIn profiles for CEO and key product/tech
  leads, press coverage quoting executives, conference speaker bios.
- **Competitive Landscape:** G2/Capterra "compare" or "alternatives" pages, review-site category
  pages listing competitors, competitor product pages for their AI feature claims, analyst or
  press coverage naming market leaders in the vertical.

Cite a specific source for every non-trivial claim as you go — you'll need it for the Sources
list and the confidence tags in Phase 2. Do not fabricate a fact to fill a gap: if something
isn't findable after a reasonable effort, that facet states "not publicly disclosed" or "not
publicly determinable" rather than a guess (see spec §3).

## Phase 2: Write the Report

Structure, section order, and voice rules: `references/company-brief-spec.md` §4. Sections in
order: **General**, **Financials**, **Products**, **Tech**, **Personas**, **People**,
**Competitive Landscape**, then a numbered **Sources** list.

Tag each non-trivial fact's confidence (High/Medium/Low) per spec §3, and say explicitly in the
text when a figure is inferred rather than sourced (e.g. the headcount-triangulated revenue
estimate). Plain language throughout — no framework codes, no scoring language, no verdict or
recommendation section: this skill stops at the facts.

Deliver the report as the final message content (plain markdown), not as a file, unless the user
asks for a file.
