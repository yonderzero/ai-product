# FleetDesk · What could go wrong

> Fictional example. FleetDesk, its documents and numbers are invented; inside-view answers are tagged `[PM, illustrative]`. Market facts are real and cite pages retrieved on 27 Oct 2026. Scores computed by `compute_risk_score.py`. 1 is safest, 5 most exposed.

## 1. Risk summary

```
Company:         FleetDesk (fictional)
Risk Composite:  3.0 / 5.0   (lower = safer, higher = more exposed)
Highest Risk:    AI disruption (4), partner and ecosystem dependency (4), timing of disruption (4)
Lowest Risk:     Market growth (2), regulatory shift (2), audit embeddedness (2)
```

**Borderline:** the composite of 3.00 sits right on the 3.0 line. One point on any single risk moves it by about 0.09. If AI disruption fell to 3, for example by a partnership that made the telematics vendors' data work for FleetDesk rather than against it, the composite would be 2.91, just on the safer side. If price pressure rose to 4, it would be 3.09. That matters: it is the difference between "exposed, move now" and "moderately safe, build steadily", and it is close enough that the product manager should decide.

## 2. Top risks

**AI disruption (4).** The telematics vendors and Fleetio now do maintenance with AI, and they are winning our customers.
- Motive Maintenance (18 Aug 2026) turns defects and fault codes into work orders automatically, reads invoices, and covers parts and warranty (https://gomotive.com/motive-launches-ai-powered-maintenance-to-help-operations-teams-prevent-breakdowns-increase-uptime-and-lower-repair-costs/).
- Fleetio's AI Service Advisor approves low-risk repairs on its own, generally available since 25 Sep 2026 (https://itbrief.co.uk/story/fleetio-opens-ai-service-advisor-after-maintenance-beta).
- 31 of the 88 customers we lost moved to a telematics vendor's bundled maintenance [documents/churn-note-2026.md].
- Urgency: near-term.

**Dependence on rivals' data (4).** The data our AI vision needs flows from the companies competing with us.
- About 310 customers stream fault codes and meter readings from Samsara, Motive or Geotab [documents/fault-code-assist-beta-feedback.md].
- Those same vendors sell maintenance bundles (`../vision/market-moves.md`).
- Meter sync problems are already the top support category, at 18% [documents/support-tickets-q3-2026.csv].
- Urgency: structural.

**Timing of disruption (4).** This is happening now, not in some later wave.
- Motive Agents can open a work order and mark a truck out of service, since 20 Oct 2026 (https://www.truckinginfo.com/news/motive-adds-ai-agents-for-fleet-operations).
- Samsara's maintenance agents arrived in June 2026 (https://www.samsara.com/blog/samsaras-new-innovations-increase-efficiency).
- 37 customers face a bundled offer at renewal [documents/churn-note-2026.md].
- Urgency: near-term.

## 3. Risk landscape

**End market environment.** The market itself is supportive. Fleet management is forecast to grow about 17% a year to 2035, and the US about 15% (https://www.gminsights.com/industry-analysis/fleet-management-market). The rules that create demand are stable: inspection reports, annual inspections and record keeping (https://www.law.cornell.edu/cfr/text/49/396.11). FMCSA's 2026 deregulation changed small items, not these duties (https://jjkellercompliancenetwork.com/news/fmcsa-finalizes-12-deregulatory-changes). The freight downturn is a drag on small carriers: 19 customers closed or merged [documents/churn-note-2026.md]. The risks here are AI disruption and dependence on the telematics vendors, and both are accelerating.

**Product defensibility.** Integrations are real but standard, and alternatives are credible and fast to set up (https://www.fleetio.com/pricing). Leaving is real work for larger fleets with years of records and parts setups, and easy for small ones. Timing is the accelerating risk in this section; integration depth and substitution are stable.

**Business health.** Price pressure is mixed. FleetDesk charges $8–$13 per vehicle [documents/product-one-pager.md] against Fleetio's $4–$10 (https://www.fleetio.com/pricing) and free inspection apps (https://www.worktruckonline.com/news/fleetpal-makes-its-driver-inspection-app-free-for-qualified-fleets). 12 customers left over the 2026 increase, yet net retention is 101% [documents/churn-note-2026.md]. The product is meaningfully embedded in DOT audits, which lowers risk. Brand is adequate and the stack is mixed, with legacy parts and mobile problems visible in churn.

| Dimension | Score | Section |
|---|---|---|
| R1 AI disruption | 4 | End market environment |
| R2 Market growth | 2 | End market environment |
| R3 Regulatory and market shift | 2 | End market environment |
| R4 Partner and ecosystem dependency | 4 | End market environment |
| R5 Integration and lock-in depth | 3 | Product defensibility |
| R6 Substitution and data portability | 3 | Product defensibility |
| R8 Timing of disruption | 4 | Product defensibility |
| R9 Price-value pressure | 3 | Business health |
| R10 Audit and approvals embeddedness | 2 | Business health |
| R11 Brand and trust strength | 3 | Business health |
| R12 Tech stack obsolescence | 3 | Business health |

## 4. Watch-outs

- Strong retention in larger fleets, high AI disruption: churn above 150 vehicles is 4% today, but retention is a lagging signal. Are bundles starting to win larger fleets too?
- Dependence on rivals' data, and the AI vision built on it: what happens if a telematics vendor limits or prices its data feed?
- Price pressure next to a thin brand: if Fleetio or a bundle matches the parts depth at half the price, what holds the price?
- Brand and trust is scored on inference: no public reviews exist for this fictional company.

## 5. Open questions for interview

| Dimension | Question | Likely change if the answer is unfavourable |
|---|---|---|
| Brand and trust | How often are we on the shortlist without being asked, in fleets of 150–500 vehicles? | 3 → 4 |
| Partner and ecosystem dependency | Do our data agreements with Samsara, Motive and Geotab let us use their feeds for AI features that compete with theirs? | 4 → 5 |
| AI disruption | Have bundles won any fleet above 150 vehicles in the last year? | 4 → 5 |
| Price-value pressure | How many renewals this year asked for a discount, citing Fleetio's price? | 3 → 4 |

`[PM, illustrative]` On the first question: sales says FleetDesk is shortlisted unprompted in about half of 150–500-vehicle deals, which supports keeping brand and trust at 3.

## 6. Methodology note

Market, competitor and regulatory evidence comes from pages retrieved on 27 Oct 2026: competitor launch pages and trade press, Cornell's copy of the FMCSA rules, J. J. Keller on deregulation, and a Global Market Insights forecast. Everything about FleetDesk comes from the invented `documents/` and the product manager's answers. A fictional company has no reviews on G2, Capterra or Trustpilot, so brand and trust is capped at Low confidence.

## 7. Evidence quality

| Dimension | Name | Score | Evidence Confidence | Score Basis | Flags |
|---|---|---|---|---|---|
| R1 | AI disruption | 4 | High | direct_evidence | |
| R2 | Market growth | 2 | Medium | mixed | conflict_present |
| R3 | Regulatory and market shift | 2 | Medium | mixed | |
| R4 | Partner and ecosystem dependency | 4 | Medium | mixed | |
| R5 | Integration and lock-in depth | 3 | Medium | mixed | |
| R6 | Substitution and data portability | 3 | Medium | mixed | |
| R8 | Timing of disruption | 4 | High | direct_evidence | |
| R9 | Price-value pressure | 3 | Medium | mixed | conflict_present |
| R10 | Audit and approvals embeddedness | 2 | Medium | mixed | |
| R11 | Brand and trust strength | 3 | Low | inference_heavy | single_class_evidence, interview_candidate |
| R12 | Tech stack obsolescence | 3 | Medium | mixed | |
