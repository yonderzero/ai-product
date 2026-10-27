# Salesforce Sales Cloud and Service Cloud · What protects the product

> Illustrative example built from public sources on 27 Oct 2026. Not affiliated with or endorsed by Salesforce. Anything tagged `[PM, illustrative]` is invented to show what a product manager would add. Scores computed by `compute_moat_score.py`.

## 1. Summary

```
Company:          Salesforce (Sales Cloud and Service Cloud)
MOAT Composite:   3.67 / 5.0
Mode:             Mode F — Fortress
Exposure Ratio:   0.35 (Moderate)
Strongest Pillar: Distribution (4.3)
Most Exposed:     Switching costs (0.58)
```

Boundary note from the script: exposure 0.35 is within 0.03 of the Fortress/Resilient boundary (0.35). Read this as Fortress, close to Resilient.

## 2. Verdict

Salesforce has a broad moat: the best-known brand in CRM, the largest partner and certified-expert network around any CRM, and years of customisation inside each customer's org. The part AI can wear down is the cost of leaving: data export is standard, and AI tools make moving records, retraining people and re-mapping processes cheaper for a rival. The most valuable thing to invest in is turning years of cross-customer history into something customers use every day, so that staying gives them something they can't get elsewhere.

## 3. Pillar summary

| Pillar | Score | Exposure Ratio | Mode Signal |
|---|---|---|---|
| Switching costs (SC) | 3.7 | 0.58 | Holding, but AI targets 3 of 6 levers |
| Domain knowledge (DK) | 3.3 | 0.33 | Solid; history is a latent asset |
| Speed and cost of building (DS) | 3.4 | 0.50 | Wide surface; talent is easy to find |
| Distribution (DC) | 4.3 | 0.00 | Strong, relational and safe from AI |

## 4. Pillar analysis

### Switching costs (3.7/5.0 | Exposure: 0.58)

| Lever | Score | AI Exposure | Evidence Basis |
|---|---|---|---|
| Data migration complexity | 3 | AI-exposed | Direct, Medium |
| User retraining burden | 4 | AI-exposed | Direct, Medium |
| Process reconfiguration effort | 4 | AI-exposed | Direct, Medium |
| Integration dependency depth | 4 | Structural | Direct, High |
| Customisation volume | 4 | Partial | Direct, Medium |
| Contractual lock-in | 3 | Structural | Direct, Medium |

Leaving Salesforce takes real work. Nearly 6,000 apps sit on AppExchange and 91% of customers use at least one [https://smartbridge.com/salesforce-appexchange-apps-top-20-for-2026/]. Salesforce's own engineers found that most customer orgs are highly customised, each with its own objects and business logic [https://engineering.salesforce.com/how-agentforce-delivers-trusted-extensible-ai-agents-for-enterprise-orchestration/]. Integrations are the strongest lever, and they don't depend on AI. Data migration is the weakest. Enterprise editions can export all data as CSV files every week [https://trailhead.salesforce.com/content/learn/modules/lex_implementation_data_management/lex_implementation_data_export], and migration firms plan 6 to 12 weeks to move a customised org to HubSpot, plus a read-only period [https://insidea.com/blog/hubspot/salesforce-to-hubspot-migration-timeline]. Contracts can't be cancelled or reduced mid-term, but most renew yearly [https://www.nutshell.com/blog/salesforce-contracts-explained]. A credible rival would use AI to map objects, rebuild flows and train users, then time the switch to a renewal.

### Domain knowledge (3.3/5.0 | Exposure: 0.33)

| Lever | Score | AI Exposure | Evidence Basis |
|---|---|---|---|
| Regulatory and compliance logic | 2 | Partial | Direct, Medium |
| Industry-specific process encoding | 3 | Partial | Inference, Low |
| Edge case handling | 4 | Partial | Inference, Medium |
| Data models | 4 | Partial | Direct, Medium |
| Terminology | 4 | Structural | Direct, Medium |
| Historical benchmarks | 3 | Structural | Direct, Medium (latent asset) |

Sales and service are horizontal work, so there is little regulatory logic to protect. Salesforce has been first in CRM for 13 years in a row, with a 20.0% share in 2025 [https://www.digitaltoday.co.kr/en/view/74831/salesforce-tops-idc-global-crm-market-share-for-13th-straight-year], and that breadth has built a deep library of edge cases. The data model of accounts, contacts, opportunities and cases is widely copied: migration firms recreate custom objects one for one [https://insidea.com/blog/hubspot/salesforce-to-hubspot-migration-timeline]. Its vocabulary has stuck: job postings ask for a "Salesforce administrator" (`../vision/opportunities.md`). The most promising lever is historical benchmarks. Salesforce holds years of pipeline and case history across customers but doesn't package it (`../vision/ai-levels.md`). Since Spring '26, a default-on setting lets customer data train global predictive models [https://www.salesforceben.com/salesforces-new-ai-data-setting-sparks-debate-over-what-customers-agreed-to/]. This is a latent asset and a named opportunity.

### Speed and cost of building (3.4/5.0 | Exposure: 0.50)

| Lever | Score | AI Exposure | Evidence Basis |
|---|---|---|---|
| Codebase maturity | 4 | Partial | Direct, Medium |
| QA infrastructure | 3 | Partial | Direct, Medium |
| Developer domain familiarity | 2 | Partial | Direct, Medium |
| Feature parity as barrier | 4 | AI-exposed | Direct, Medium |
| Regulatory approval navigated | 4 | Structural | Direct, Medium |

The platform is mature and moved to public clouds through Hyperforce [https://www.infoworld.com/article/3599854/salesforce-targets-public-clouds-with-hyperforce.html]. 98.1% of orgs are on Lightning, with Classic still around [https://www.salesforceben.com/salesforce-lightning-transition-apps-retired-amid-98-1-adoption/]. The reasoning engine ships every other day with staged rollouts [https://engineering.salesforce.com/how-agentforce-delivers-trusted-extensible-ai-agents-for-enterprise-orchestration/]. Government Cloud Plus has held a FedRAMP High provisional authorisation since May 2020 [https://compliance.salesforce.com/en/categories/fedramp-high]. The feature surface is wide, which is the strongest lever here. The weakest is talent: more than 170,000 certified experts work in the ecosystem [https://www.forrester.com/blogs/the-salesforce-consulting-landscape-shows-no-sign-of-slowdown/], so CRM skills are easy to hire. Rivals don't try to match every feature. They take one slice, such as service agents, and connect to the CRM (`../vision/market-moves.md`).

### Distribution (4.3/5.0 | Exposure: 0.00)

| Lever | Score | AI Exposure | Evidence Basis |
|---|---|---|---|
| Direct buyer relationships | 4 | Structural | Inference, Medium |
| Brand recognition | 5 | Structural | Direct, High |
| Conference and community presence | 5 | Structural | Direct, Medium |
| Referral and partner networks | 5 | Structural | Direct, High |
| Sales team expertise | 3 | Structural | Inference, Low |
| Customer success depth | 4 | Structural | Direct, Medium |
| Geographic coverage | 4 | Structural | Direct, Medium |

This is the strongest pillar. Salesforce is a Leader in Gartner's 2025 sales force automation report [https://www.cxtoday.com/crm/gartner-magic-quadrant-for-sales-force-automation-platforms-sfa-2025-the-rundown/]. It runs Dreamforce, which drew more than 40,000 people in person in 2025 [https://www.salesforceben.com/dreamforce/]. More than 3,800 consulting firms work on Salesforce, and Forrester puts their combined revenue at nearly six times Salesforce's own [https://www.forrester.com/blogs/the-salesforce-consulting-landscape-shows-no-sign-of-slowdown/]. The paid Signature plan adds a named customer success manager and round-the-clock monitoring [https://www.salesforce.com/services/success-plans/overview/signature-success/]. The sales team's expertise is the least evidenced lever. A well-funded rival would have to earn all of this over many years.

## 5. Exposure map

**AI-exposed levers**
- Data migration complexity (switching costs, 3): standard CSV export plus AI mapping tools make moving records cheaper. Urgency: high.
- User retraining burden (switching costs, 4): AI onboarding and agents that work in Slack or ChatGPT shrink what users need to learn. Urgency: medium.
- Process reconfiguration effort (switching costs, 4): AI can rebuild flows and rules from configuration. Urgency: medium.
- Feature parity as a barrier (speed and cost, 4): AI-native rivals build one slice fast and sit on top of the CRM. Urgency: medium.

**Structural levers**
- Integration dependency depth (switching costs, 4): re-integrating ERP, data and apps still takes engineering time.
- Contractual lock-in (switching costs, 3): non-cancellable terms; multi-year agentic licence agreements [https://www.theregister.com/2025/12/12/ai_agents_salesforce_pricing/].
- Terminology (domain knowledge, 4) and historical benchmarks (domain knowledge, 3): only time builds these.
- Regulatory approval (speed and cost, 4): FedRAMP High takes years for a newcomer.
- All seven distribution levers (4.3 average): relationships, brand, Dreamforce and partners.

## 6. Strategic implications

**Defend now**
- **Partners.** The consulting ecosystem is the biggest barrier to entry. Give partners agent-building work to sell, so they keep bringing customers in.
- **Integrations.** Keep AppExchange and Headless 360 open and well documented, so builders build on Salesforce rather than around it. The 2025 Slack API change drew lock-in criticism [https://www.cxtoday.com/crm/salesforce-blocks-competitors-from-using-slack-data-so-what/].

**Act on**
- **Make leaving cost the customer something they value.** Export will stay easy. Instead, give each customer benchmarks and agent learnings built from many customers' history, which a new CRM can't offer on day one.
- **Make the agent the place people work.** If agents update the record and do the follow-up, retraining matters less, and so does a rival's AI onboarding.

**Watch**
- Edge-case depth and the data model: AI can learn both from public docs and migrations.
- QA and release speed: AI-native rivals ship fast; staged rollouts are a strength to keep.

## 7. Evidence provenance

About 30 searches and fetches were shared across the three reports, with about 10 for this one.
- Switching costs: Trailhead, contract analysis, migration vendor timelines, AppExchange statistics, the engineering blog.
- Domain knowledge: IDC rankings, product files in this folder, trade press on the data setting. Industry process encoding (DK2) and edge-case handling (DK3) were scored mainly by inference.
- Speed and cost: InfoWorld, SalesforceBen, the engineering blog, the compliance portal and Forrester.
- Distribution: CX Today, SalesforceBen, Forrester and Salesforce's success-plan page. Direct buyer relationships (DC1) and sales team expertise (DC5) were scored by inference.

## 8. Evidence quality

| Lever ID | Pillar | Score | Evidence Source | Evidence Confidence | Flags |
|---|---|---|---|---|---|
| SC1 | Switching costs | 3 | Trailhead; INSIDEA | Medium | borderline |
| SC2 | Switching costs | 4 | Forrester; review summaries in `../product.md` | Medium | |
| SC3 | Switching costs | 4 | Salesforce engineering blog; `[PM, illustrative]` | Medium | |
| SC4 | Switching costs | 4 | Smartbridge; INSIDEA | High | |
| SC5 | Switching costs | 4 | Engineering blog; Signature page | Medium | |
| SC6 | Switching costs | 3 | Nutshell (MSA quotes); The Register | Medium | |
| DK1 | Domain knowledge | 2 | Compliance portal; Gibson Dunn | Medium | |
| DK2 | Domain knowledge | 3 | Inference | Low | inference_heavy |
| DK3 | Domain knowledge | 4 | Digital Today (IDC) | Medium | |
| DK4 | Domain knowledge | 4 | INSIDEA | Medium | |
| DK5 | Domain knowledge | 4 | Job postings in `../vision/opportunities.md` | Medium | |
| DK6 | Domain knowledge | 3 | `../vision/ai-levels.md`; SalesforceBen | Medium | latent_asset |
| DS1 | Speed and cost | 4 | InfoWorld; SalesforceBen | Medium | |
| DS2 | Speed and cost | 3 | Engineering blog; Signature page | Medium | |
| DS3 | Speed and cost | 2 | Forrester | Medium | |
| DS4 | Speed and cost | 4 | `../product.md`; `../vision/market-moves.md` | Medium | |
| DS5 | Speed and cost | 4 | Compliance portal; InfoWorld | Medium | |
| DC1 | Distribution | 4 | Signature page; `[PM, illustrative]` | Medium | |
| DC2 | Distribution | 5 | Digital Today (IDC); CX Today | High | |
| DC3 | Distribution | 5 | SalesforceBen | Medium | single_source |
| DC4 | Distribution | 5 | Forrester | High | |
| DC5 | Distribution | 3 | Inference | Low | inference_heavy |
| DC6 | Distribution | 4 | Signature page | Medium | |
| DC7 | Distribution | 4 | InfoWorld | Medium | |
