# Salesforce Sales Cloud and Service Cloud · What could go wrong

> Illustrative example built from public sources on 27 Oct 2026. Not affiliated with or endorsed by Salesforce. Anything tagged `[PM, illustrative]` is invented to show what a product manager would add. Scores computed by `compute_risk_score.py`. 1 is safest, 5 most exposed.

## 1. Risk summary

```
Company:         Salesforce (Sales Cloud and Service Cloud)
Risk Composite:  2.64 / 5.0   (lower = safer, higher = more exposed)
Highest Risk:    AI disruption (4) and timing of disruption (4)
Lowest Risk:     Market growth (2), with five others at 2
```

The composite was 2.55 from public sources. The product manager raised AI disruption from 3 to 4 with their own win/loss evidence (see `discovery.md`, "What we corrected"), and the script was rerun. `[PM, illustrative]`

## 2. Top risks

**AI disruption: 4.** AI-native service agents are well funded and winning service decisions.
- Sierra raised $950M at a valuation above $15B. It says it serves more than 40% of the Fortune 50 and is moving into sales [https://www.vktr.com/customer-experience/sierra-raises-950m-at-15b-valuation-eyes-transformation-beyond-customer-support/].
- Decagon raised $250M in January 2026 [https://www.vktr.com/contact-center/decagon-triples-valuation-to-45b-with-250m-series-d/]. HubSpot's customer agent resolves about 70% of conversations for 9,000+ customers [https://www.cxtoday.com/contact-center/hubspot-customer-agent-resolution-rate/].
- `[PM, illustrative]` In win/loss notes, AI-native agents now appear in most mid-market service evaluations Salesforce loses.

Salesforce's complementary assets slow this down: installed base, integrations, partners and years of history. They would normally cap this risk at 3. The product manager's evidence shows buyers choosing the agent first, which meets the higher anchor. Urgency: near-term.

**Timing of disruption: 4.** The market is pricing the risk now, even though customers aren't leaving yet.
- The stock was down about 33% in 2026 by late May, amid fears that agents shrink seat-based software. Bank of America rated it Underperform for that reason [https://www.tikr.com/blog/salesforce-beat-q1-earnings-by-0-76-a-share-heres-why-the-stock-is-still-down-33-in-2026].
- Revenue attrition is still about 8% [https://transcripts.platformaeronaut.com/summaries/CRM-4Q26-AI-Summary]. That is a lagging signal, so it doesn't lower this score.

Urgency: near-term.

**Price-value pressure: 3.** Prices still hold, but the pricing model is in motion.
- A 6% list increase on Enterprise and Unlimited editions of Sales Cloud and Service Cloud took effect in August 2025 [https://tech.co/news/lock-in-deal-salesforce-price-rise-august].
- Salesforce moved its agents from per-conversation and consumption pricing back towards seat-based agreements because customers wanted predictability. Analysts warn buyers may pay for seats they barely use [https://www.theregister.com/2025/12/12/ai_agents_salesforce_pricing/].
- Reviewers point to cost and add-ons (`../product.md`).

Urgency: medium-term.

## 3. Risk landscape

**End market environment.** The market is growing: global CRM is forecast to grow about 10.9% a year from 2025 to 2030 [https://www.researchandmarkets.com/r/z4gnmz]. AI disruption is the one risk that is accelerating. Regulation is manageable. In May 2026 the EU agreed to push back its high-risk AI deadlines, while the duty to tell people they are talking to AI stays on 2 August 2026 [https://www.gibsondunn.com/eu-ai-act-omnibus-agreement-postponed-high-risk-deadlines-and-other-key-changes/]. Dependence on partners is spread out. Agentforce runs models from OpenAI, Anthropic and Google [https://www.constellationr.com/insights/news/salesforce-expands-openai-anthropic-partnerships-eyes-agentforce-everywhere], and Hyperforce runs on several public clouds [https://www.infoworld.com/article/3599854/salesforce-targets-public-clouds-with-hyperforce.html].

**Product defensibility.** Integration depth is strong: 91% of customers run AppExchange apps [https://smartbridge.com/salesforce-appexchange-apps-top-20-for-2026/]. Substitution is realistic but takes effort. Data exports as CSV every week [https://trailhead.salesforce.com/content/learn/modules/lex_implementation_data_management/lex_implementation_data_export], and migration firms plan weeks to months [https://insidea.com/blog/hubspot/salesforce-to-hubspot-migration-timeline]. Timing is the risk to watch: it is accelerating.

**Business health.** The brand is strong but has taken knocks. In August 2025 a threat group used stolen tokens from the Salesloft Drift app to export data from many companies' Salesforce orgs; Google found no flaw in the Salesforce platform itself [https://cloud.google.com/blog/topics/threat-intelligence/data-theft-salesforce-instances-via-salesloft-drift]. A default-on data-sharing setting [https://www.salesforceben.com/salesforces-new-ai-data-setting-sparks-debate-over-what-customers-agreed-to/] and the Slack API restrictions [https://www.cxtoday.com/crm/salesforce-blocks-competitors-from-using-slack-data-so-what/] drew criticism. The stack is mostly modern, with Classic remnants in older orgs [https://www.salesforceben.com/salesforce-lightning-transition-apps-retired-amid-98-1-adoption/]. CRM plays some part in approvals but is not the core financial control layer. All three are stable.

| Dimension | Score | Section |
|---|---|---|
| R1 AI disruption | 4 | End market environment |
| R2 Market growth | 2 | End market environment |
| R3 Regulatory and market shift | 2 | End market environment |
| R4 Partner and ecosystem dependency | 2 | End market environment |
| R5 Integration and lock-in depth | 2 | Product defensibility |
| R6 Substitution and data portability | 3 | Product defensibility |
| R8 Timing of disruption | 4 | Product defensibility |
| R9 Price-value pressure | 3 | Business health |
| R10 Audit, segregation of duties and approvals | 3 | Business health |
| R11 Brand and trust strength | 2 | Business health |
| R12 Tech stack obsolescence | 2 | Business health |

## 4. Watch-outs

- Customers stay (about 8% attrition), but exposure to AI-native rivals is high. Is today's retention hiding decisions being made now?
- Pricing has moved from seats to consumption and back. Will customers keep paying per seat if agents do more of the work?
- Trust is a strength, but the data-setting debate touches exactly what level 5 needs: permission to learn across customers.
- Rivals connect to Salesforce rather than replace it. Does that keep the record safe, or slowly move the value elsewhere?

## 5. Open questions for interview

| Dimension | Question | If the answer is unfavourable |
|---|---|---|
| Audit and approvals embeddedness | How many customers run approvals, discounts or controls that auditors rely on inside Sales Cloud? | Rises to 4 |
| Substitution and data portability | In the last year, how many lost customers moved fully off, and how long did it take them? | Rises to 4 |
| Price-value pressure | What share of renewals ended with fewer seats? | Rises to 4 |
| Timing of disruption | Are lost service deals rising quarter on quarter? | Rises to 5 |

## 6. Methodology note

About 12 searches and fetches went into this report: funding coverage, analyst and trade press, Salesforce's own pages, a Google security advisory and a market forecast. Gartner's CRM forecasts couldn't be opened, so a ResearchAndMarkets forecast is used for market growth, which caps that score at Medium confidence. The retired labour-displacement dimension is not scored.

## 7. Evidence quality

| Dimension | Name | Score | Evidence Confidence | Score Basis | Flags |
|---|---|---|---|---|---|
| R1 | AI disruption | 4 | Medium | mixed | conflict_present; changed by `[PM, illustrative]` |
| R2 | Market growth | 2 | Medium | direct_evidence | single_class_evidence |
| R3 | Regulatory and market shift | 2 | Medium | mixed | |
| R4 | Partner and ecosystem dependency | 2 | Medium | direct_evidence | |
| R5 | Integration and lock-in depth | 2 | High | direct_evidence | |
| R6 | Substitution and data portability | 3 | Medium | mixed | |
| R8 | Timing of disruption | 4 | Medium | mixed | conflict_present |
| R9 | Price-value pressure | 3 | Medium | mixed | |
| R10 | Audit, segregation of duties and approvals | 3 | Low | inference_heavy | inference_heavy |
| R11 | Brand and trust strength | 2 | Medium | mixed | conflict_present |
| R12 | Tech stack obsolescence | 2 | Medium | mixed | |
