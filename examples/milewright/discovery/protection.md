# Milewright · What protects the product

> Fictional example. Milewright, its documents and numbers are invented; inside-view answers are tagged `[PM, illustrative]`. Market facts are real and cite pages retrieved on 27 Oct 2026. Scores computed by `compute_moat_score.py`.

## 1. Summary

```
Company:          Milewright (fictional)
MOAT Composite:   2.7 / 5.0
Mode:             Mode T — Transitional
Exposure Ratio:   0.35 (Moderate)
Strongest Pillar: Domain knowledge (3.0)
Most Exposed:     Switching costs (0.58)
```

## 2. Verdict

Milewright's protection is real but uneven: fifteen years of edge cases across many kinds of fleet, deep parts and DOT records, and a latent store of repair history no newcomer has. What protects it least is the cost of leaving and the size of its feature set, because Motive and Fleetio have shown they can build a full maintenance product with AI in one release, and AI makes moving records and retraining cheaper. The most important investment is to turn the repair history into something customers use every day, so staying gives them answers they can't get from a bundle.

## 3. Pillar summary

| Pillar | Score | Exposure Ratio | Mode Signal |
|---|---|---|---|
| Switching costs (SC) | 2.8 | 0.58 | Eroding — AI targets 3 of 6 levers, all at 3 |
| Domain knowledge (DK) | 3.0 | 0.33 | Holding — edge cases strong, history latent |
| Speed and cost of building (DS) | 2.4 | 0.50 | Weak — rivals reach parity fast |
| Distribution (DC) | 2.6 | 0.00 | Safe from AI, but thin |

## 4. Pillar analysis

### Switching costs (2.8/5.0 | Exposure: 0.58)

| Lever | Score | AI Exposure | Evidence Basis |
|---|---|---|---|
| Data migration complexity | 3 | AI-exposed | Direct, Medium |
| User retraining burden | 3 | AI-exposed | Direct, Medium |
| Process reconfiguration effort | 3 | AI-exposed | Inference, Low |
| Integration dependency depth | 3 | Structural | Direct, Medium |
| Customisation volume | 3 | Partial | Inference, Low |
| Contractual lock-in | 2 | Structural | Direct, Medium |

Leaving Milewright takes some work, and more for larger fleets: churn above 150 vehicles is 4%, against 10.8% overall [documents/churn-note-2026.md]. Records are relational and VMRS-coded, and PM programs and parts setups are built per vehicle class. But nothing here is deep. Rivals onboard fast ("They were live in a week") [documents/lost-deals-h1-2026.md], contracts are annual with no exit fees, and the telematics links are ones every rival also has. Integration depth is the most solid lever because it doesn't depend on AI; the contract is the weakest. A credible rival would use AI to import the history, map PM schedules and train technicians, then make the offer at renewal, as Motive's reps already do [documents/interview-fleet-ops-director-distribution.md].

**AI acceleration risk:** this pillar's AI-exposed levers are both weak and directly targeted by modern AI tooling. Competitor advantage in AI product development would accelerate decay here.

### Domain knowledge (3.0/5.0 | Exposure: 0.33)

| Lever | Score | AI Exposure | Evidence Basis |
|---|---|---|---|
| Regulatory and compliance logic | 3 | Partial | Direct, High |
| Industry-specific process encoding | 3 | Partial | Direct, Medium |
| Edge case handling | 4 | Partial | Direct, Medium |
| Data models | 3 | Partial | Inference, Medium |
| Terminology and taxonomy | 2 | Structural | Direct, Medium |
| Historical benchmarks | 3 | Structural | Direct, Medium (latent asset) |

Milewright knows how fleet shops work. It encodes the FMCSA rules on inspection reports, annual inspections and record retention (https://www.law.cornell.edu/cfr/text/49/396.11, https://www.law.cornell.edu/cfr/text/49/396.17, https://www.law.cornell.edu/cfr/text/49/396.3), but those rules are public and every rival handles them. Edge cases are the strongest lever: fifteen years across carriers, distributors, waste haulers, utilities and last-mile fleets, including reefer units and trailers [documents/product-one-pager.md]. Terminology is the weakest: VMRS codes are the industry's, not ours (https://www.samsara.com/ca/blog/sobeys-fleet-maintenance-ai). Historical benchmarks are a latent asset: about 2 million work orders a year across 800 fleets `[PM, illustrative]`, and buyers already ask "How do we compare to fleets like us?" [documents/lost-deals-h1-2026.md]. This is a named investment opportunity, not a weakness.

### Speed and cost of building (2.4/5.0 | Exposure: 0.50)

| Lever | Score | AI Exposure | Evidence Basis |
|---|---|---|---|
| Codebase maturity | 3 | Partial | Inference, Medium |
| QA infrastructure | 2 | Partial | Direct, Medium |
| Developer domain familiarity | 3 | Partial | Inference, Low |
| Feature parity as barrier | 2 | AI-exposed | Direct, High |
| Regulatory approval navigated | 2 | Structural | Direct, Medium |

A fifteen-year codebase is hardened across many fleets, but it is not a barrier others can't cross. Motive launched maintenance with AI fault codes, automatic work orders, invoice reading, parts and warranty in one release (https://gomotive.com/motive-launches-ai-powered-maintenance-to-help-operations-teams-prevent-breakdowns-increase-uptime-and-lower-repair-costs/), and Fullbay launched an "AI-native" platform (https://fullbay.com/blog/fullbay-next-heavy-duty-repair-shop-software/). Feature parity is the most exposed lever. Testing is thin: most regression testing is manual `[PM, illustrative]`, and meter-sync problems are 18% of tickets [documents/support-tickets-q3-2026.csv]. No regulatory approval is needed to sell in this market.

### Distribution (2.6/5.0 | Exposure: 0.00)

| Lever | Score | AI Exposure | Evidence Basis |
|---|---|---|---|
| Direct buyer relationships | 3 | Structural | Direct, Medium |
| Niche brand recognition | 2 | Structural | Inference, Low |
| Conference and community presence | 3 | Structural | Direct, Low |
| Referral and partner networks | 2 | Structural | Direct, Medium |
| Sales team domain expertise | 3 | Structural | Direct, Medium |
| Customer success depth | 3 | Structural | Direct, Medium |
| Geographic and language coverage | 2 | Structural | Direct, Medium |

Distribution is safe from AI but thin. The strongest levers are people: implementation specialists who ran fleet shops, and business reviews with the top 50 accounts [documents/lost-deals-h1-2026.md] [documents/churn-note-2026.md]. Brand is the weakest: Samsara, Motive and Fleetio dominate the trade press (`../vision/market-map.md`), and the telematics vendors reach the CFO directly. There is no partner channel; the telematics marketplaces Milewright is listed in belong to its biggest rivals `[PM, illustrative]`.

## 5. Exposure map

**AI-exposed levers**
- Data migration complexity (switching costs, 3): AI makes importing 15 years of records cheaper for a rival. Urgency: high, as bundles target renewals now.
- User retraining burden (switching costs, 3): AI onboarding and simpler apps cut retraining; rivals already win on ease of use. Urgency: high.
- Process reconfiguration effort (switching costs, 3): PM templates and AI setup reduce re-mapping. Urgency: medium.
- Feature parity as barrier (speed and cost of building, 2): one release from Motive matched most of the feature set. Urgency: high.

**Structural levers**
- Integration dependency depth (switching costs, 3): real engineering to redirect accounting and fuel-card links; but the telematics links belong to rivals.
- Contractual lock-in (switching costs, 2): annual contracts; safe from AI, but weak.
- Terminology (domain knowledge, 2) and historical benchmarks (domain knowledge, 3): history can't be copied without time in market.
- Regulatory approval (speed and cost of building, 2): no approval needed.
- All seven distribution levers (2–3): human and safe from AI.

## 6. Strategic implications

**Defend now**
- *Historical benchmarks.* Package the repair history as answers customers use: which codes led to breakdowns, cost per mile against similar fleets. Start by confirming contract rights [documents/fault-code-assist-beta-feedback.md].
- *Edge case handling.* Keep the multi-shop parts and mixed-fleet depth that wins fleets of 150 to 500 vehicles [documents/lost-deals-h1-2026.md].
- *Customer success.* Extend business reviews beyond the top 50 to the 37 customers facing a bundled offer [documents/churn-note-2026.md].

**Act on**
- *Data migration and retraining.* Make Milewright the easiest to use for technicians: voice notes and fewer clicks (`../vision/opportunities.md` #3), so the reason to leave disappears.
- *Feature parity.* Stop competing feature for feature; compete on doing the shop's work, from fault code to ready work order (`../vision/opportunities.md` #1).

**Watch**
- Regulatory logic, process encoding and data models: safe while rules are stable, but AI makes them easier to copy each year.

## 7. Evidence provenance

- **Switching costs:** churn and lost-deal notes, the one-pager, Fleetio's PM templates; process reconfiguration and customisation volume scored mainly by inference.
- **Domain knowledge:** the FMCSA rules on Cornell's legal information site, the one-pager and sales notes, a Samsara customer story on VMRS coding.
- **Speed and cost of building:** Motive's and Fullbay's launch pages, the support tickets and the product manager's answers; developer domain familiarity scored by inference.
- **Distribution:** churn and sales notes, TMC's fleet survey page, the product manager's answers; brand recognition scored by inference, as a fictional company has no public reviews.

## 8. Evidence quality

| Lever ID | Pillar | Score | Evidence Source | Evidence Confidence | Flags |
|---|---|---|---|---|---|
| SC1 | SC | 3 | documents/product-one-pager.md, documents/lost-deals-h1-2026.md | Medium | |
| SC2 | SC | 3 | documents/churn-note-2026.md | Medium | |
| SC3 | SC | 3 | `[PM, illustrative]`, fleetio.com PM template | Low | inference_heavy |
| SC4 | SC | 3 | documents/product-one-pager.md, documents/fault-code-assist-beta-feedback.md | Medium | |
| SC5 | SC | 3 | `[PM, illustrative]`, documents/churn-note-2026.md | Low | |
| SC6 | SC | 2 | documents/product-one-pager.md, `[PM, illustrative]` | Medium | |
| DK1 | DK | 3 | law.cornell.edu (49 CFR 396.3, 396.11, 396.17) | High | |
| DK2 | DK | 3 | documents/product-one-pager.md, documents/lost-deals-h1-2026.md | Medium | |
| DK3 | DK | 4 | documents/product-one-pager.md, documents/interview-fleet-ops-director-distribution.md | Medium | |
| DK4 | DK | 3 | documents/product-one-pager.md | Medium | |
| DK5 | DK | 2 | samsara.com Sobeys story | Medium | |
| DK6 | DK | 3 | `[PM, illustrative]`, documents/lost-deals-h1-2026.md | Medium | latent_asset |
| DS1 | DS | 3 | `[PM, illustrative]` | Medium | |
| DS2 | DS | 2 | `[PM, illustrative]`, documents/support-tickets-q3-2026.csv | Medium | |
| DS3 | DS | 3 | inference | Low | inference_heavy |
| DS4 | DS | 2 | gomotive.com, fullbay.com | High | |
| DS5 | DS | 2 | `[PM, illustrative]` | Medium | |
| DC1 | DC | 3 | documents/churn-note-2026.md, `[PM, illustrative]` | Medium | |
| DC2 | DC | 2 | vision/market-map.md | Low | inference_heavy |
| DC3 | DC | 3 | `[PM, illustrative]`, tmc.trucking.org | Low | |
| DC4 | DC | 2 | `[PM, illustrative]` | Medium | |
| DC5 | DC | 3 | documents/lost-deals-h1-2026.md | Medium | |
| DC6 | DC | 3 | documents/churn-note-2026.md | Medium | |
| DC7 | DC | 2 | `[PM, illustrative]` | Medium | |
