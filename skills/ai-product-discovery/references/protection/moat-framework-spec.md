# MOAT Framework Spec (standalone)

Condensed from VMS-Analyzer's `moat/moat-framework-definition-spec.md` v1 for a standalone,
single-pass skill. Source of truth for all lever rubrics, exposure tags, composite math, mode
logic, and report structure. If anything in SKILL.md conflicts with this file, this file wins.

## 1. Purpose

A MOAT analysis answers one question: **what does this company have that a well-funded
competitor with modern AI tools cannot easily replicate or erode?** The framework decomposes
competitive defensibility into four pillars and 24 levers, each scored 1–5 and tagged by its
AI-exposure status. Written for the company's own leadership — honest, specific, actionable.
Not a vendor pitch.

## 2. Framework Overview

| Pillar | ID | Levers | AI-Safe | Partial | AI-Exposed |
|--------|----|--------|---------|---------|------------|
| Switching Costs | SC | 6 | 2 | 1 | 3 |
| Domain Knowledge | DK | 6 | 2 | 4 | 0 |
| Development Speed & Cost | DS | 5 | 1 | 3 | 1 |
| Distribution Channel | DC | 7 | 7 | 0 | 0 |

The further a moat component is from human relationship and institutional trust, the more
AI-exposed it is. Distribution is structurally human-relational and AI-safe across all levers.
Switching Costs are the most directly AI-attacked pillar. Domain Knowledge and Development
Speed sit in the middle.

## 3. Full-Range Anchoring Rule

Every lever must use the full 1–5 range where the evidence supports it. Compressing everything
into the 2–3 band hides the strategic signal (a pillar of all-3s reads "moderate everywhere"
when the truth might be "strong distribution, weak switching costs"). For every lever: match
the evidence to the closest anchor text and cite it; if the evidence genuinely matches a 1, 4,
or 5 anchor, score it — extremes are information, not risk. Before finalizing a pillar, compare
against `references/calibration-index.json`: if every lever in a pillar lands on 2–3, re-check
each against the 1 and 4/5 anchors and either re-anchor or note explicitly why the middle band
is genuinely correct for this company.

## 4. Pillar Definitions and Lever Rubrics

### Pillar SC: Switching Costs

What it takes — in time, money, and disruption — for a customer to leave. AI attacks three SC
levers directly (data migration, retraining, process reconfiguration). Integration depth,
customization volume, and contractual lock-in remain structurally defensible because they
require engineering effort, organizational time, or legal resolution regardless of AI capability.

**SC1: Data Migration Complexity** — `ai_exposed` (AI simplifies data cleaning/transformation/migration tooling)
| Score | Anchor |
|-|-|
| 1 | All data exportable as standard CSV/JSON; any competitor can import in hours |
| 2 | Structured export exists but requires light transformation; migration takes days |
| 3 | Custom fields or relational data; migration requires a specialist and takes weeks |
| 4 | Complex relational data with custom schemas, workflow history, attachments; months of effort |
| 5 | Deeply nested multi-year data with no standard migration path; parallel operation required 6+ months |

**SC2: User Retraining Burden** — `ai_exposed` (AI-assisted onboarding reduces retraining time for competitors)
| Score | Anchor |
|-|-|
| 1 | Generic UI patterns; users transfer skills immediately |
| 2 | Product-specific terminology but intuitive; days of retraining |
| 3 | Workflow-specific training required; weeks for proficiency |
| 4 | Deep workflow/configuration knowledge required; 1–3 months for power users |
| 5 | Specialized certification/accreditation required; product defines how the team operates |

**SC3: Process Reconfiguration Effort** — `ai_exposed` (AI tooling reduces cost of process re-mapping for a switcher)
| Score | Anchor |
|-|-|
| 1 | Product adapts to any process; no reconfiguration needed on switch |
| 2 | Minor process adjustments on switch; completed in days |
| 3 | Processes built around product conventions; weeks of reconfiguration |
| 4 | Organizational processes deeply aligned to product capabilities; 1–3 months |
| 5 | Product defines the organization's operating model; reconfiguration touches every team |

**SC4: Integration Dependency Depth** — `structural` (requires engineering work regardless of AI)
| Score | Anchor |
|-|-|
| 1 | Standalone product; no integration dependencies |
| 2 | 1–2 lightweight integrations; easily redirected |
| 3 | Several integrations including critical business systems; redirection takes weeks |
| 4 | Deep bidirectional integrations with ERP/payroll/compliance systems; months to re-integrate |
| 5 | Integrations are the product; switching requires re-engineering the surrounding data ecosystem |

**SC5: Customization Volume** — `partial` (AI replicates patterns, but volume + institutional "why" is hard to transfer)
| Score | Anchor |
|-|-|
| 1 | Off-the-shelf configuration only; no meaningful customization |
| 2 | Minor workflow configuration; days to recreate |
| 3 | Several custom workflows and fields; weeks of reconfiguration effort |
| 4 | Extensive custom workflows/forms/automations/reports built over years; months to recreate |
| 5 | Years of bespoke configuration layers; institutional knowledge exists only in customer's team |

**SC6: Contractual Lock-in** — `structural` (legal/contractual commitments are human-institutional)
| Score | Anchor |
|-|-|
| 1 | Monthly rolling contract; exit any time at no cost |
| 2 | Annual contract; standard notice period |
| 3 | Multi-year with moderate exit terms |
| 4 | Multi-year with significant exit fees or data retention penalties |
| 5 | Multi-year with exit penalty + data portability restrictions + compliance entanglement |

*Public sector note:* when the buyer base is predominantly public sector (government agencies,
public universities, NHS, local authorities, utilities), factor in procurement cycle duration
and formal re-tender processes (often 2–4 years) as effective lock-in even without formal exit
penalties — this may justify +0.5 above what contract terms alone suggest; document the rationale.

*SMB SaaS inference default:* when contract terms aren't publicly disclosed (no pricing-page
language, no press on exit clauses, no review-site mentions of lock-in) for an SMB-targeted
product, default SC6 to 2 with `inference_heavy` flag — SMB SaaS rarely carries multi-year
commitments or exit penalties unless positioned as an enterprise platform. Don't infer above 2
purely from monthly-vs-annual pricing options (a standard SMB pricing pattern, not lock-in).

*Compliance-dependency exception:* for operationally critical compliance SaaS (e.g. certificate
management, regulatory filing) where losing access creates immediate regulatory/commercial
exposure, compliance entanglement substitutes for contract evidence — score above the SMB
default toward the compliance-entanglement anchors, with `score_basis: mixed`, when structural
dependency is evidenced but contract terms are not. Review language like "non-negotiable" or
"we couldn't operate without it" is high-confidence substitute evidence.

### Pillar DK: Domain Knowledge

The encoded understanding of how the vertical actually operates — regulations, processes, edge
cases, data models, terminology, historical patterns. None of the DK levers are fully AI-exposed.
DK1–DK4 are `partial`: AI can capture/replicate the knowledge, but building buyer trust in it and
encoding real edge cases from years of exposure takes time. DK5–DK6 are `structural`: proprietary
vocabulary and time-locked data assets a competitor cannot reconstruct without time in market.

**DK1: Regulatory/Compliance Logic** — `partial`
| Score | Anchor |
|-|-|
| 1 | No vertical regulation; generic compliance (GDPR, ISO 27001) replicable by any vendor |
| 2 | Standard compliance requirements; widely documented and replicable |
| 3 | Vertical-specific regulatory logic that is documented; a competitor could encode it in 12–18 months |
| 4 | Deeply encoded vertical regulations with grey areas, edge cases, jurisdiction-specific handling |
| 5 | Regulatory logic is the product; company is the de facto compliance reference for its vertical |

**DK2: Industry-Specific Process Encoding** — `partial`
| Score | Anchor |
|-|-|
| 1 | Generic business processes; no vertical encoding; replicable in months |
| 2 | Common vertical workflows documented and replicable within 12 months |
| 3 | Mid-complexity vertical workflows with some unique logic; replication takes 2–3 years |
| 4 | Complex multi-party workflows unique to the vertical, not documented in any public standard |
| 5 | Process encoding is the core IP; product is the canonical definition of how the vertical operates |

**DK3: Edge Case Handling** — `partial`
| Score | Anchor |
|-|-|
| 1 | No meaningful edge case library; standard error handling only |
| 2 | Common edge cases handled based on product maturity |
| 3 | Moderate edge case library from several years of customer exposure |
| 4 | Extensive edge case handling from 10+ years across diverse customer scenarios |
| 5 | Edge case library is a competitive moat; customers choose the product because it handles what others don't |

**DK4: Data Models** — `partial`
| Score | Anchor |
|-|-|
| 1 | Generic data model; replicable in months by any competent team |
| 2 | Vertical-aligned model based on documented industry standards; replicable in 12 months |
| 3 | Custom data model reflecting vertical operations; would take 2 years to replicate |
| 4 | Complex data model with vertical-specific relationships/constraints, built from diverse customer input |
| 5 | Data model is the vertical's canonical schema; 15+ years of refinement, impossible to reconstruct without that history |

**DK5: Terminology/Taxonomy** — `structural` (proprietary vocabulary is a social/organizational moat, not technical)
| Score | Anchor |
|-|-|
| 1 | Generic business terminology; no proprietary vocabulary |
| 2 | Standard vertical terminology from industry bodies; any vendor uses the same terms |
| 3 | Some proprietary terminology embedded in UI/reports; not yet adopted as industry standard |
| 4 | Proprietary vocabulary deeply embedded in product and customer operations; users think in the product's terms |
| 5 | Product defines the vocabulary of the vertical; switching means relearning what concepts mean |

**DK6: Historical Benchmarks** — `structural` (time-locked asset; only strengthens with time)
| Score | Anchor |
|-|-|
| 1 | No benchmark data; no historical record of value to customers |
| 2 | Basic operational data; limited comparative value to customers |
| 3 | Several years of benchmarks covering key metrics; useful for internal reporting |
| 4 | 10+ years of benchmarks; customers use them for board reporting and peer comparison |
| 5 | Benchmark database is the vertical's industry standard; customers publish research citing it |

*Latent asset clarification:* when a company demonstrably holds multi-year cross-customer
benchmark data but hasn't packaged it as a customer-facing product, score 3 with a `latent_asset`
note — this reflects existing internal-intelligence value while acknowledging it isn't yet an
active lever. Frame this as a positive finding and a named investment opportunity, not a weakness.

### Pillar DS: Development Speed & Cost

How hard it is for a new entrant or existing competitor to replicate what's been built. Feature
parity as a barrier is nearly destroyed by AI coding tools — a well-resourced competitor can
close feature surface in months rather than years. Codebase maturity, QA infrastructure, and
developer domain familiarity are partially degraded by AI, but domain expertise and production
hardening remain meaningful. Regulatory approval is fully structural: time-locked, jurisdiction-
specific, not accelerated by AI.

**DS1: Codebase Maturity** — `partial`
| Score | Anchor |
|-|-|
| 1 | Codebase is fragile or immature; a competitor could build a comparable system in 12 months |
| 2 | Functional codebase with moderate technical debt; replicable in 18–24 months |
| 3 | Mature codebase with significant investment; replication would take 2–3 years |
| 4 | Deeply mature codebase with complex domain logic and production hardening across diverse scenarios |
| 5 | Codebase embodies irreplicable institutional knowledge; greenfield rebuild would take 5+ years to reach equivalent reliability |

**DS2: QA Infrastructure** — `partial`
| Score | Anchor |
|-|-|
| 1 | Manual testing only; no automated test suite |
| 2 | Basic automated testing; core flows covered |
| 3 | Solid test coverage of main workflows; regression testing in place |
| 4 | Comprehensive test suite including edge cases, compliance scenarios, load testing |
| 5 | QA infrastructure is cited as a product differentiator in enterprise procurement; publicly demonstrated |

**DS3: Developer Domain Familiarity** — `partial`
| Score | Anchor |
|-|-|
| 1 | Generic software domain; any competent dev team can build without vertical background |
| 2 | Some domain knowledge needed; available in the talent market |
| 3 | Specialized domain knowledge required; available but scarce |
| 4 | Deep vertical expertise required; few developers have it; most come from the incumbent ecosystem |
| 5 | Domain expertise is a recruitment barrier; talent pool is small and concentrated in existing vendors |

**DS4: Feature Parity as Barrier** — `ai_exposed` (AI coding tools let well-resourced competitors close feature surface far faster than "years of roadmap" suggests)
| Score | Anchor |
|-|-|
| 1 | Feature surface is small; a competitor could reach parity in 6 months with AI tooling |
| 2 | Moderate feature surface; parity achievable in 12–18 months |
| 3 | Significant feature depth; parity would take 2–3 years of focused investment |
| 4 | Very large feature surface accumulated over years; parity requires 3–5 years |
| 5 | Feature surface so large and interconnected that parity is functionally impossible without acquisition |

**DS5: Regulatory Approval Navigated** — `structural`
| Score | Anchor |
|-|-|
| 1 | No regulatory approval required to compete in this market |
| 2 | Standard certifications (ISO 27001, SOC 2); achievable by a new entrant in months |
| 3 | One significant vertical certification; takes 12–18 months for a new entrant |
| 4 | Multiple vertical certifications across geographies; 2–3 years for a new entrant to replicate |
| 5 | Regulatory approval is a years-long process with ongoing compliance obligations; effectively a market entry barrier |

### Pillar DC: Distribution Channel

How the company reaches, wins, and retains customers. Every DC lever is structural — none are
AI-exposed. Direct relationships, brand recognition, community presence, referral networks,
sales expertise, customer success depth, and geographic coverage are human, relational, and
institutional. A well-funded AI-native competitor still has to earn these, and they do not
scale with compute. Typically the most defensible pillar for established VMS companies.

**DC1: Direct Buyer Relationships** — `structural`
| Score | Anchor |
|-|-|
| 1 | Transactional; no meaningful relationship beyond the contract |
| 2 | Account management in place; professional but not deep |
| 3 | Executive relationships at some accounts; renewal is partly relationship-driven |
| 4 | Executive sponsorship at most accounts; company leadership knows buyer leadership personally |
| 5 | Relationships are the product; company is a strategic partner, not a vendor |

**DC2: Niche Brand Recognition** — `structural`
| Score | Anchor |
|-|-|
| 1 | Unknown outside existing customers |
| 2 | Known to buyers who actively search; no unaided recognition |
| 3 | Named in vertical RFPs without prompting; moderate brand recognition |
| 4 | Strong brand recognition; automatically short-listed in the vertical |
| 5 | Synonymous with the vertical; the brand defines the category |

**DC3: Conference/Community Presence** — `structural`
| Score | Anchor |
|-|-|
| 1 | No presence at vertical events |
| 2 | Occasional attendance; no visible role |
| 3 | Regular exhibitor or speaker presence |
| 4 | Major sponsor or session organizer; high visibility |
| 5 | Organizes or co-organizes the vertical's primary events; sets the community agenda |

**DC4: Referral/Partner Networks** — `structural`
| Score | Anchor |
|-|-|
| 1 | No referral or partner network |
| 2 | A few informal referral relationships |
| 3 | Structured partner program with active referrals |
| 4 | Dominant referral channel in the vertical; most new business comes through partners |
| 5 | Partner ecosystem is a barrier to entry; competitors cannot access the referral channel without displacing the incumbent |

**DC5: Sales Team Domain Expertise** — `structural`
| Score | Anchor |
|-|-|
| 1 | Generalist sales team; no vertical expertise |
| 2 | Some sales team members with vertical background |
| 3 | Majority of sales team has meaningful vertical experience |
| 4 | Sales team is respected in the vertical; buyers consult them as advisors |
| 5 | Sales team expertise is a product differentiator; buyers buy access to the team's knowledge |

**DC6: Customer Success Depth** — `structural`
| Score | Anchor |
|-|-|
| 1 | Reactive support only; no proactive engagement |
| 2 | Periodic check-ins; basic health monitoring |
| 3 | Proactive QBRs; success team drives adoption and expansion |
| 4 | Success team is embedded in customer operations; considered part of the customer's team |
| 5 | Customer success is the primary retention mechanism; customers stay for the success team, not just the product |

**DC7: Geographic/Language Coverage** — `structural`
| Score | Anchor |
|-|-|
| 1 | Single geography, single language; fully vulnerable to a local competitor |
| 2 | Single geography but strong local presence and first-mover advantage |
| 3 | Primary geography dominant; some adjacent coverage |
| 4 | Multi-geography with localized teams and language support |
| 5 | Geographic coverage is a barrier to entry; the vertical is fragmented enough that local presence in each market is a prerequisite for competition |

## 5. Composite Formula

```
Pillar_score = average of all lever scores in the pillar (round to 1 decimal)

Pillar_exposure_ratio = (
  (count of ai_exposed levers × 1.0) +
  (count of partial levers × 0.5)
) / total levers in pillar
Round to 2 decimal places. Range: 0.00 – 1.00.

MOAT_composite = average of SC, DK, DS, DC pillar scores (equal weights), round to 2 decimals
Overall_exposure_ratio = average of the four pillar exposure ratios, round to 2 decimals
```

All four pillars carry equal weight. Each is independently load-bearing: a company with a
perfect Distribution score (5.0) and a collapsed Switching Cost score (1.0) has a Distribution
moat, not a MOAT. This math is computed by `scripts/compute_moat_score.py` — never eyeball it.

## 6. MOAT Mode Logic

Determined by two axes: composite strength and AI exposure.

| Mode | Name | Composite | Exposure ratio | Description |
|------|------|-----------|---------------|-------------|
| F | Fortress | ≥ 3.5 | ≤ 0.35 | Durable, broad, AI-safe competitive advantage |
| R | Resilient | ≥ 3.5 | 0.36–0.60 | Strong moat but specific components are AI-exposed — act on those levers |
| T | Transitional | 2.5–3.4 | any | Moat is real but uneven; exposed levers are degrading while structural ones hold |
| V | Vulnerable | < 2.5, OR exposure_ratio > 0.65 | — | Moat is thin or fast-eroding; competitive displacement risk is elevated |

**Distribution-only flag:** if DC pillar score ≥ 3.5 AND the average of SC/DK/DS < 2.5, this is
a `distribution_only` company (the script computes the trigger). Note explicitly: "This
company's moat is primarily relational. The product itself does not generate meaningful
switching cost or domain knowledge defensibility. Distribution is structurally safe but
insufficient alone if a better-resourced competitor targets this vertical with AI-first product
capabilities."

**AI acceleration note:** if any pillar contains 2+ ai_exposed levers AND that pillar score <
3.0, add: "AI acceleration risk — this pillar's ai_exposed levers are both weak and directly
targeted by modern AI tooling. Competitor advantage in AI product development would accelerate
decay here." (Judgment call — the script doesn't compute this one; check pillar-by-pillar.)

## 7. Evidence Rules (standalone)

There is no research cache in this skill — every lever is scored from your own WebSearch/
WebFetch pass, done fresh each run. Per lever: cite the specific finding (named source: review
site quote, pricing page, press release, job posting, LinkedIn, G2/Capterra, etc.) that anchors
the score. Strong evidence = 2+ independent signals from different source types →
`evidence_confidence: High`. One direct signal or two same-type signals → `Medium`. No direct
evidence → score by informed inference from company profile, vertical, and ownership type,
`evidence: inference`, `evidence_confidence: Low`. **Do not refuse to score a lever for lack of
evidence — an inference score, flagged as such, is always better than no score.**

Required per-lever fields: `score` (1–5 int), `rationale` (2–3 sentences citing the anchor and
evidence), `evidence` (`direct` | `inference`), `evidence_confidence` (`High`|`Medium`|`Low`),
`flags` (any of: `low_evidence`, `inference_heavy`, `borderline`, `conflict_present`,
`single_source`, `early_stage_product`, `latent_asset`).

**Early-stage annotation:** product <3 years old or <5 confirmed live customers → flag the
time-accrual levers (SC5, DK3, DK6, DS1) `early_stage_product` and note the expected trajectory
rather than penalizing a young company for not yet having a moat that only accrues with time.

## 8. Report Structure

Voice: direct ("Your switching cost moat is eroding", not "may be experiencing erosion"),
specific (name levers, scores, competitors), honest (weak pillars stated plainly, inferences
noted), written for a CPO/CEO with 15 minutes. **Plain language: never use lever codes (SC1,
DK3, etc.) in narrative prose** — name the lever in plain English ("low data portability" not
"SC3"). Codes belong only in the Pillar Summary Table, Evidence Provenance, and the Evidence
Quality table.

**§1 MOAT Summary** — single block:
```
Company:          {company_name}
MOAT Composite:   {composite} / 5.0
Mode:             Mode {letter} — {name}
Exposure Ratio:   {overall_exposure_ratio} ({Low|Moderate|High})
Strongest Pillar: {pillar name} ({score})
Most Exposed:     {pillar name} ({exposure_ratio})
```

**§2 Verdict** — exactly three sentences: (1) what the company actually has, (2) what is
eroding and why, (3) the single most important investment to defend the moat.

**§3 Pillar Summary Table** — `| Pillar | Score | Exposure Ratio | Mode Signal |`, one row per
pillar. Mode signal = short phrase, e.g. "Intact — structural anchors hold", "Eroding — AI
attacking 2 of 6 levers", "Strong — fully relational and AI-safe".

**§4 Pillar Analysis** — one section per pillar. Sub-header `## {Pillar Name} ({score}/5.0 |
Exposure: {ratio})`. Lever table `| Lever | Score | AI Exposure | Evidence Basis |`. Then one
paragraph (4–6 sentences): what this pillar looks like in practice, strongest lever and why,
most exposed lever and why, what a credible competitor attack on this pillar looks like.

**§5 Exposure Map** — two lists: AI-exposed levers (name + pillar + score + one-sentence why +
urgency) and Structural levers (name + pillar + score + one-sentence note on what makes it safe).

**§6 Strategic Implications** — three named sub-sections: **Defend now** (2–3 highest-value
structural levers to actively invest in — working, don't let them atrophy); **Act on** (2–3 most
dangerous ai_exposed levers with specific, company-situation-specific actions, not generic
"invest in AI"); **Watch** (partial levers safe for now but worth monitoring as AI tooling matures).

**§7 Evidence Provenance** — one sentence per pillar noting the research basis (which searches,
which source types). If any lever had no direct evidence and was scored by inference, name the
lever ID explicitly.

**§8 Evidence Quality table** — one row per lever: `| Lever ID | Pillar | Score | Evidence
Source | Evidence Confidence | Flags |`.
