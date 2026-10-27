# Company Brief — CELCAT

**Vertical:** Education technology — timetabling / academic scheduling software for Higher and Further Education
**Geography:** Headquartered in the UK, with customers in 30+ countries
**Brief generated:** 2026-07-27

---

## General

| Field | Detail |
|---|---|
| Legal name | CELCAT (registered as CELCAT Ltd; England & Wales company number 1448722; VAT GB418696219) [1] |
| Founded | Disputed — see note below |
| HQ | Coleshill Manor Office Campus, Coleshill, Warwickshire, UK (near Birmingham/Coventry) [1][8] |
| Additional offices | France (Celcat France), Australasia (via CDS Australasia Pty Ltd), South Africa (via Adapt IT partnership) [1][2] |
| Domain | celcat.com |
| Ownership | Strategic portfolio company — owned by **Kinetic**, a business unit of **Volaris Group**, which is an operating group of the publicly traded **Constellation Software Inc.** (TSX: CSU). Acquired by Kinetic/Volaris in **2023** [11][12][21] |
| Headcount | ~41 employees (LinkedIn/Tracxn, as of mid-2026); LinkedIn size band "11–50 employees" [8][9] — **Medium confidence**, single data-provider source |

**Founding-year note:** Public sources disagree. Tracxn and LinkedIn both list **1979** as the founding year [8][9], but Celcat's own marketing consistently refers to "30+ years" of timetabling experience [1][5], and Volaris' acquisition write-up refers to "over 40 years" in the sector [11] — these would imply a founding date anywhere from the mid-1980s to mid-1990s. One plausible reconciliation (not confirmed by any source): the 1979 date may reflect the original legal-entity registration (company number 1448722), while the CELCAT timetabling product/brand launched later. Flagged as a genuine divergence rather than picked — **Low confidence** on an exact founding year.

**Notable news, trailing 12 months:**
1. **Celcat AI unveiled** at the Celcat Conference, Manchester, 11–12 November 2025 — described internally as "the most significant shift in timetabling in 30 years," a ground-up agentic, graph-database-backed rebuild of the platform [5][7]. Matters because it's a full architecture bet, not an incremental feature.
2. **CEO David Wilkes featured at Volaris Group's "Quadrants 2026"** conference (Copenhagen, 26–30 April 2026), discussing the decision to retire the legacy platform and reskill (not replace) staff, and framing "deep domain knowledge" as the company's durable moat against AI disruption [13]. Matters as a public signal of the company's AI strategy and change-management approach.
3. **Post-acquisition performance disclosed by Volaris**: "double-digit growth," professional-services utilization tripled, and R&D productivity reportedly up 4x since joining Kinetic/Volaris in 2023 [11]. No specific date attached to the figures; treat as a standing claim rather than a single news event.

---

## Financials

- **Revenue:** Not publicly disclosed. No independent revenue estimate was found in press, Crunchbase (page blocked), or Tracxn (funding/revenue masked) [9].
  - **Headcount-triangulated estimate (inferred, not a finding):** using ~41–50 FTEs [8][9] at the $150–250K revenue/FTE range for B2B VMS companies → **roughly $6–12.5M USD/year**. **Low confidence**, explicitly an estimate, not a sourced figure.
- **Pricing model:** Subscription/license, tailored per institution. Third-party aggregators describe pricing as calculated on EFT (equivalent full-time) student numbers, with vendor contact required for a quote — no public price list [source: SoftwareAdvice/GetApp/Capterra vendor-profile pages, aggregated in search results]. **Medium confidence** — consistent across multiple secondary sources, no primary pricing page found.
- **Customer count:** "200+ universities and colleges," "over 1 million students" as daily end-users, across 30+ countries [1]. **Medium confidence** — vendor-stated claim, not independently corroborated with a customer list or filing.
- **Growth signals:** 2023 acquisition by Kinetic/Volaris; post-acquisition "double-digit growth" and utilization/R&D productivity gains reported by the parent [11]. No independent financial filings exist (private, non-reporting UK subsidiary of a larger public parent) — Constellation Software's own consolidated filings do not break out CELCAT individually.

---

## Products

### CELCAT Timetabler (primary / installed-base product)
- **Category:** System of Record / System of Action for academic scheduling.
- **Core workflows:** timetable creation and clash-free scheduling; room/resource booking; attendance monitoring; exam scheduling; academic staff pay-claim management; timetable publishing to students/staff [1][4].
- **Key modules:** Timetabler (core engine), Attendance Monitoring, Exam Scheduling, Automated Premium Scheduling, Pay Claim, "Now" (student/parent self-service portal) [1].
- **Key integrations:** Tribal SITS, Tribal EBS, Unit-e, Ellucian Banner, Unit4, StudentOne, iTrent, StarRez, SEAtS, Adapt IT ITS Integrator, Microsoft 365 (AD/Exchange/Outlook), Google Workspace [4]. **Medium confidence** — sourced to Celcat's own migration/integration page, not independently verified per-integration.
- **Reference customers/sectors:** University of Suffolk, University of East London, Walsall College, University of Johannesburg, JTL (apprenticeships, 8,000 apprentices/3,800 employers), University of the Arts London, Keele University, University of Greater Manchester [3]. University of Suffolk case study cites a specific outcome: improved space utilisation of "52%" [3] (exact baseline/methodology not disclosed).
- **Review-site presence:** G2 — **absent** (no product page found in repeated searches). Capterra — **present**, 1 published review, 5.0/5.0 rating as of this research [10].

### Celcat AI (next-generation platform, launched Nov 2025)
- **Category:** Emerging platform layer, positioned to eventually replace/absorb Timetabler.
- **Architecture claim:** built on a proprietary graph database for "real-time relational insight across rooms, staff, cohorts, and constraints," with a multi-agent ("Cohort of Timetabling Agents") design — specialist agents for data analysis, risk detection, recommendation, and continuous learning [4][6].
- **Named capabilities:** agentic room-booking automation, parallel scenario modeling ("what-if" planning without touching the live timetable), continuous monitoring of utilization/workload/policy compliance with real-time recommendations [6].
- **Migration path:** vendor states "full migration or phased rollout" options, with a "typical deployment" of one academic term and a zero-downtime/data-loss claim [4].

**AI features and lifecycle stage** (all per vendor's own marketing pages; no independent/customer-side confirmation of production use was found):
| Feature | Stage |
|---|---|
| Multi-agent ("Cohort") timetabling engine | Limited / early rollout — publicly launched Nov 2025, but no independently verified live-customer deployment found |
| Graph-database real-time relational model | Limited / early rollout |
| Scenario modeling / "what-if" planning | Limited / early rollout |
| Agentic automated room booking | Limited / early rollout |
| Continuous utilization/compliance monitoring | Limited / early rollout |

**Overall AI-maturity tag: mixed.** The installed-base Timetabler product is largely rule-based operational automation (constraint-solving, not generative). Celcat AI is a genuine agentic/GenAI-adjacent layer, but it is newly announced (Nov 2025) and, as of this research, its claims come entirely from Celcat's own marketing — no case study, review, or press coverage was found describing it running in production at a named institution.

---

## Tech

| Layer | Detail | Confidence |
|---|---|---|
| Language(s) | C#, VB.NET | Low — sourced only to a third-party technology-profiling aggregator (RocketReach), not a primary source or job posting directly reviewed [14] |
| Frameworks | ASP.NET, jQuery, HTML/JavaScript | Low [14] |
| Cloud/infra | AWS (S3, Route53); Plesk hosting automation | Low [14] |
| Database | Microsoft SQL Server, MySQL (legacy); proprietary graph database (Celcat AI, name/vendor not disclosed) | Low (legacy DBs) / Not publicly determinable (graph DB provider) [14][4] |
| AI/ML layer | Proprietary agentic framework marketed as "Celcat AI"; underlying model/LLM provider not named anywhere in public material | Not publicly determinable |

**AI infrastructure provider:** Not publicly determinable — no mention of AWS Bedrock, Azure OpenAI, GCP Vertex, or a named self-hosted model stack in any Celcat AI page reviewed.

**Architecture verdict: Dual-track.** CELCAT Timetabler (legacy: ASP.NET/C#/VB.NET, SQL Server/MySQL, Windows-era design per the stack signals above) continues to run the existing 200+ institution installed base, in parallel with **Celcat AI**, a newly built cloud-native, graph-database/agentic platform launched November 2025. **Migration pace: gradual** — Celcat's own materials describe a phased, per-institution rollout paced at roughly one academic term per migration, rather than a fast forced cutover [4].

**Hiring velocity:** Not publicly determinable. The company's own careers page lists no open roles (applicants are told to email in) [2], and no active CELCAT job postings were found on LinkedIn or Reed.co.uk at the time of this research. Combined with a small (~41–50 person) total headcount and Volaris' reported "4x" R&D productivity gain since 2023 [11], this is consistent with either a lean, efficiency-driven team or simply low external hiring signal — cannot distinguish between the two from public data.

---

## Personas

| Persona | Seniority | Buying role | Jobs-to-be-done | Daily pains | Would pay more for |
|---|---|---|---|---|---|
| Timetabling Manager / Academic Scheduling Administrator | Manager | User + Influencer | Build clash-free term timetables; process mid-term change requests; allocate rooms/resources | Manual conflict-checking when enrolment exceeds venue capacity (noted directly in a published review) [10]; last-minute room/staff reshuffles | Automated conflict validation; agentic scenario simulation for "what-if" replanning |
| Academic Registrar / Director of Academic Operations | Director | Economic buyer | Institution-wide policy/accreditation compliance; optimize space utilization; report up to leadership | Disconnected SIS/room-booking/payroll systems requiring manual reconciliation; limited real-time utilization visibility | Cross-system real-time analytics; strategic scenario modeling (e.g., compressed teaching weeks) |
| Faculty / Tutors | IC | User | View/manage personal teaching schedule; submit pay claims; request room changes | Rigid schedules; slow room-change approval; manual pay-claim submission | Self-service instant room booking; automated pay-claim reconciliation |
| Students (via "Now" portal) | N/A (end user) | User (indirect) | View live timetable, attendance, and assignment info | Delayed/out-of-date schedule information | Not applicable — not a purchasing persona |

**Industry associations/events:** UCISA (Universities and Colleges Information Systems Association, UK) — Celcat's own annual **Celcat Conference** has featured UCISA-delivered sessions (e.g., cybersecurity) [7]; the company's user base is concentrated in UK/Ireland further-education colleges and small-to-mid, non-centralised higher-education institutions rather than the largest research universities [16].

---

## People

| Name | Title | LinkedIn | Confidence |
|---|---|---|---|
| David Wilkes | CEO, CELCAT (within Kinetic's Timetabling Group, Volaris/Constellation Software) | Not found (profile URL not located) | Medium — corroborated by two independent sources (RocketReach profile [14/15] and Volaris Group's own Quadrants 2026 write-up [13]), but no primary LinkedIn or company "leadership" page confirms the title directly |
| Patrick Ashe | Sales Manager | Not found | Low — single source (RocketReach) [15] |
| Tremaine Gooden | Senior Marketing Executive | Not found | Low — single source (RocketReach) [15] |
| David Sweeney | Attributed as "founder" in a Celcat blog post specifically about the Celcat AI platform launch [5] | Not found | Low — his company-wide role and how this reconciles with David Wilkes' CEO title is not clear from public sources; may reflect a product-level "founder" framing for the AI initiative rather than a company-founder claim |

Wilkes' public commentary (at Volaris' Quadrants 2026) centers on a deliberate decision to retire CELCAT's legacy platform rather than patch it, paired with reskilling existing staff instead of layoffs/rehiring, and a stated view that deep domain expertise — not the software itself — is the company's durable competitive moat [13].

---

## Competitive Landscape

| Competitor | AI posture vs. CELCAT | Most relevant AI feature | Stage |
|---|---|---|---|
| TechnologyOne (Syllabus Plus, formerly Scientia) | Parity | "Cohort Planning Pathways" — enrolment-data-driven pathway/gap analysis in the 2026A release | GA [17] |
| OneAdvanced (CMIS / CMISGo) | Behind (for the timetabling product specifically) | None public tied directly to CMIS scheduling; OneAdvanced markets a broader "OneAdvanced AI" layer across its education portfolio, but CMIS itself is reported to be in support-only mode, not active further development | None public (CMIS-specific) [19] |
| TimeEdit | Ahead | Embedded inside Ellucian's "AI-driven" Student SIS (Banner) via a July 2025 partnership, covering curriculum planning through daily scheduling | GA [18] |
| Coursedog | Ahead (by resourcing/marketing) | Positions itself broadly as an "AI-powered" academic-operations platform (curriculum, catalog, scheduling); well-capitalized ($117M+ raised) | GA per vendor marketing — feature specifics not independently verified [20] |

**Market position:** CELCAT is a **niche/challenger** player, historically strongest with UK/Ireland further-education colleges and smaller, non-centralised higher-education institutions, rather than the largest research universities — where the market has historically been dominated by a Syllabus Plus/CMIS duopoly (roughly 50%/24% UK HE share as of 2020, per one industry source) [16]. Its November 2025 pivot to an agentic, graph-database-native platform is a genuine differentiation attempt relative to competitors who are largely layering AI features onto existing SIS/scheduling engines rather than rebuilding — but as of this research, that bet is unproven in public production evidence.

---

## Sources

1. [Celcat — Timetabling Software (homepage)](https://celcat.com/)
2. [Celcat — Careers](https://celcat.com/careers/)
3. [Celcat — Client Stories](https://celcat.com/client-stories/)
4. [Celcat — Celcat AI: Migration & Integration](https://celcat.com/celcat-ai-migration-integration/)
5. [Celcat — "30 Years of Timetabling Progress… So, What's Next?"](https://celcat.com/30-years-of-timetabling-progress-so-whats-next/)
6. [Celcat — "The Five Superpowers of Celcat AI"](https://celcat.com/timetabler/features/the-five-superpowers-of-celcat-ai/) / [Celcat AI: The Power of a Cohort of Timetabling Agents](https://celcat.com/celcat-ai-the-power-of-a-cohort-of-timetabling-agents/)
7. [Celcat — Agenda for the Celcat Conference 2025](https://celcat.com/agenda-for-the-celcat-conference-2025/)
8. [CELCAT | LinkedIn company page](https://www.linkedin.com/company/celcat)
9. [Celcat — 2025 Company Profile, Funding & Competitors — Tracxn](https://tracxn.com/d/companies/celcat/__bhJlE_T4mpNv4OrCf3l1hEQ7j7z-m40yM9ZrH2iGz_U)
10. [CELCAT Timetabler Software Pricing, Alternatives & More — Capterra](https://www.capterra.com/p/252097/CELCAT/)
11. [CELCAT Acquisition Story — Volaris Group](https://fm.volarisgroup.com/sell-software-business/celcat-acquisition-story/)
12. [Kinetic Acquisition of CELCAT is a Win for Higher Education Customers — Volaris Group](https://www.volarisgroup.com/press-room/kinetic-acquisition-of-celcat-is-a-win-for-higher-education-customers/)
13. [Quadrants 2026: Equipping Leaders to Tackle Challenges & Opportunities Ahead — Volaris Group](https://www.volarisgroup.com/acquired-knowledge/quadrants-2026-equipping-leaders-to-tackle-challenges-ahead/)
14. [CELCAT Technology Stack — RocketReach](https://rocketreach.co/celcat-technology-stack_b5cc420bf42e0ab0)
15. [CELCAT Management Team | Org Chart — RocketReach](https://rocketreach.co/celcat-management_b5cc420bf42e0ab0)
16. [Stick or twist? Is it time to change your Timetabling System? — SUMS](https://sums.ac.uk/info-hub/university-timetabling-is-it-time-to-change-your-system/)
17. [New Software Release: 2026A — TechnologyOne](https://www.technology1.com/saas-plus/software-releases/2026a)
18. [Ellucian Partners with TimeEdit to Transform Higher Education Curriculum Planning and Scheduling Operations — PR Newswire](https://www.prnewswire.com/news-releases/ellucian-partners-with-timeedit-to-transform-higher-education-curriculum-planning-and-scheduling-operations-302500197.html)
19. [CMIS and CMISGo — OneAdvanced](https://www.oneadvanced.com/solutions/cmis-and-cmisgo/) / [AI in a Day's Work — OneAdvanced](https://www.oneadvanced.com/resources/ai-in-a-days-work/)
20. [Coursedog — Company Profile — CB Insights](https://www.cbinsights.com/company/coursedog)
21. [About — Volaris Group](https://www.volarisgroup.com/about/)
