# Company Brief Spec (standalone)

Condensed from VMS-Analyzer's `intel/intel-agent.md` for a standalone, single-pass skill. Source
of truth for the 7 facet definitions, evidence/sourcing rules, and report structure. If anything
in SKILL.md conflicts with this file, this file wins.

## 1. Purpose

A company brief answers one question: **what is publicly, factually true about this VMS vendor
right now?** Seven facets — General, Financials, Products, Tech, Personas, People, Competitive
Landscape. This is an **observational** report, not an analytical one: no scoring, no rubric, no
dimension codes, no verdict, no recommendation. Analysis belongs in the other research skills in this plugin
(maturity, risk, MOAT, threat) — this one just gets the facts straight and sourced, so someone
prepping for a call or a diligence pass has a reliable snapshot in one read.

There is no research cache, no `viewpoint.txt`, and no prior-agent handoff in this standalone
version — every fact comes from this run's own WebSearch/WebFetch pass, cited to a source.

## 2. Facet Definitions

### General

Legal name, founding year, HQ location, additional offices, domain, ownership structure (Public |
PE-backed | VC-backed | Founder-owned | Strategic portfolio | Unknown), headcount estimate (with
scope — full company vs. a specific business unit — and as-of date), and 2–3 of the most
significant news items from the trailing 12 months, each with a one-sentence note on why it
matters (funding, leadership change, acquisition, major product launch, layoffs, etc.).

### Financials

Revenue estimate(s) with currency, as-of year, and confidence (High/Medium/Low), each tagged to
its source domain. If estimates diverge by more than 2x, list all and flag the divergence rather
than picking one. If no public revenue data exists, fall back to a headcount-triangulated estimate
using **$150–250K revenue per FTE** as the range for B2B VMS companies, tagged Low confidence and
labeled explicitly as an estimate, not a finding. Also cover: pricing model (subscription | license
| transaction | usage-based | mixed) with a one-sentence description of how customers actually
pay, customer-count signals (exact claims, ranges, or "not publicly disclosed"), and growth
signals (funding rounds, expansion announcements, headcount trajectory, pricing changes).

### Products

One block per product, primary product first if there are several. Cover: category (System of
Record / System of Action / System of Engagement / platform / module), 3–5 core workflows the
product handles, named key modules or feature areas, key integrations (ERP, payroll, other
third-party platforms), AI features with each one's lifecycle stage (GA | Beta | Limited |
Roadmap | None), an overall AI-maturity tag (user-facing GenAI | embedded ML | operational
delivery only | mixed | none), 2–3 notable reference customers or sectors if public, and review-
site presence (G2 present/absent/blocked, Capterra present/absent/blocked).

### Tech

A stack table (language(s), frameworks, cloud/infra, database, AI/ML layer) built from job
postings and product docs — expect gaps, note them as "not publicly determinable" rather than
guessing. AI infrastructure provider if identifiable (AWS Bedrock | Azure OpenAI | GCP Vertex |
self-hosted | unknown) with source. An architecture verdict (Legacy monolith | Modern cloud-native
| Dual-track [legacy + modern rebuild in parallel] | Unknown) — if dual-track, name both products
and note migration pace (fast/gradual/stalled) if there's evidence of it. Hiring velocity
(active/slowing/flat) based on open-role count and posting recency.

### Personas

2–4 key end-user roles. For each: seniority (IC | Manager | Director | Executive), buying role
(User | Influencer | Economic buyer | Gatekeeper), 2–3 jobs-to-be-done, 2–3 daily pains or
friction points, and 1–2 capabilities they'd pay more for. Also note the vertical's industry
associations/trade bodies and key events or conferences the company or its buyers show up at.

### People

Table of known executives (CEO/GM/MD first, then key product and technology leads): name, title,
LinkedIn URL (or "not found"), confidence tag. Add 1–2 sentences on tenure, background, or
substantive public statements only where there's something worth noting — don't pad every row.

### Competitive Landscape

Table of top competitors: name, AI posture relative to this company (ahead/parity/behind), their
most relevant AI feature (or "none public"), and its stage (GA/Beta/Roadmap/None). Close with 1–2
sentences on market position — leader, challenger, niche player, under pressure — relative to
those competitors.

## 3. Evidence and Sourcing Rules (standalone)

There is no cache and no confirmed/probable confidence scale carried over from a shared pipeline
— everything in this report comes from this run's fresh WebSearch/WebFetch pass. For every
non-trivial claim (anything beyond the company's own name and domain), cite a source: a specific
URL or clearly named source ("G2 reviews page", "2025 Series B press release", "LinkedIn profile",
"job posting on greenhouse.io"). Tag each fact's confidence:

- **High** — corroborated by 2+ independent sources, or a single authoritative primary source
  (company's own site, SEC/Companies House filing, an official press release).
- **Medium** — a single credible secondary source (news article, review site, LinkedIn) with no
  corroboration found.
- **Low** — inferred or triangulated (e.g. the headcount-based revenue estimate), or a single
  weak/indirect source.

**Never fabricate a fact to fill a gap.** If something isn't findable after a reasonable search
effort, write "not publicly disclosed" or "not publicly determinable" rather than guessing, and
don't tag a guess with a confidence level — an absence is not a Low-confidence finding, it's a
gap. Where a fact is genuinely inferred (the revenue-per-FTE fallback, an architecture verdict
guessed from job postings alone), say so explicitly in the text, not just via a confidence tag.

## 4. Report Structure

Voice: plain, factual, no sales spin, no scoring language, no framework codes. This is a briefing
a salesperson or delivery lead reads in five minutes before a call — short declarative sentences,
tables over prose wherever the source data is a table, prose only for the 1–2 sentence synthesis
lines each facet calls for (market position, architecture verdict discussion, etc.).

Header: `# Company Brief — {company_name}` followed by vertical, geography (if known), and the
date the brief was generated.

Sections, in order, one `##` header each: **General**, **Financials**, **Products**, **Tech**,
**Personas**, **People**, **Competitive Landscape** — using the fields and format described in
§2 for each. Close with a short **Sources** list: every distinct source used, numbered, so a
reader can verify anything in the brief without re-running the research.

Do not add a summary, verdict, or recommendation section — that's out of scope for this skill by
design (see §1). If a whole facet turns up essentially nothing after a real search effort, keep
the header and state plainly what's missing rather than omitting the section.
