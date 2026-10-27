# Milewright · How strong the product is, and the AI opportunity

> Fictional example. Milewright, its documents and numbers are invented; inside-view answers are tagged `[PM, illustrative]`. Market facts are real and cite pages retrieved on 27 Oct 2026. Scores computed by `compute_maturity_score.py`; the AI opportunity pillar by `compute_pillars.py`.

## 1. Maturity summary

```
Company:            Milewright (fictional)
Maturity Composite:  3.44 / 5.0
  Section A (Business Quality):   3.67
  Section B (Customer Strength):  3.5
  Section C (AI Opportunity):     3.0
```

The AI opportunity pillar used in discovery is **3.67**: the mean of AI today, AI revenue and the work AI could take off customers. Urgency is left out of it and reported on its own: **immediate** (1 out of 5, where 1 means the most urgent).

Market position was overturned from 2 to 3 by the product manager, with evidence; before that, business quality was 3.5 and the composite 3.38. See `discovery.md`.

## 2. Verdict

Milewright is a solid, deeply vertical system of record that larger fleets with their own shops depend on every day. Its strongest asset is how deeply it sits in the shop's daily work: work orders, parts across shops and DOT records, where customers using parts in two or more shops almost never leave. Its biggest gap is AI: nothing is shipped, while the category leaders shipped AI in exactly this workflow in the last few months.

## 3. Dimension scores

| Dimension | Score | Evidence Confidence | Score Basis |
|---|---|---|---|
| A1 Type of system | 4 | Medium | mixed |
| A2 Vertical market software | 5 | High | direct_evidence |
| A3 Mission criticalness | 4 | Medium | mixed |
| A4 Market position | 3 (overturned from 2) | Medium | mixed |
| A5 Leadership mindset | 3 | Low | inference_heavy |
| A6 Technology modernity | 3 | Medium | mixed |
| B1 Customer switching propensity | 3 | High | direct_evidence |
| B3 Customer dependency and embeddedness | 4 | Medium | direct_evidence |
| C1 Current AI features | 4 | High | direct_evidence |
| C2 AI initiative urgency | 1 | High | direct_evidence |
| C3 AI revenue opportunity | 3 | Medium | mixed |
| C4 AI labour automation upside | 4 | Medium | mixed |

## 4. Section analysis

### Section A (Business Quality) — 3.67/5.0

Milewright is the system of record for maintenance, repairs, parts and the DOT inspection records fleets must keep (https://www.law.cornell.edu/cfr/text/49/396.3). It is built only for fleet maintenance, with VMRS codes, driver inspections, annual inspections and multi-shop parts [documents/product-one-pager.md], which makes vertical depth the strongest dimension. It is mission-critical: a truck down for a day "costs me more than Milewright costs me for a year for that truck" [documents/interview-fleet-ops-director-distribution.md]. Market position is a strong second in its own segment, fleets of 150 to 500 vehicles with their own shops, where it wins 51% of deals [documents/lost-deals-h1-2026.md]; overall, Fleetio's 8,500+ fleets and the telematics bundles lead (https://itbrief.co.uk/story/fleetio-opens-ai-service-advisor-after-maintenance-beta). The weakest dimensions are leadership mindset and technology: an AI beta without a budget line, and a .NET Framework monolith with newer services around it `[PM, illustrative]`.

### Section B (Customer Strength) — 3.5/5.0

Customers behave in two groups. Fleets under 75 vehicles switch readily: 61 of the 88 who left in the last year were small, and 31 went to a telematics bundle [documents/churn-note-2026.md]. Larger fleets stay: churn above 150 vehicles is 4%, and 3% where parts run in two or more shops. Embeddedness is the stronger dimension, backed by that demonstrated behaviour and by work orders, parts and DOT records running through the product daily. Switching propensity stays at 3 because the overall pattern is "selective, but switching is realistic".

### Section C (AI Opportunity) — 3.0/5.0

The opportunity is large and the clock is short. Fault Code Assist is in beta with 46 customers, 31 active, and 61% of rated answers got a thumbs-up [documents/fault-code-assist-beta-feedback.md]. The work AI could take off customers is the strongest dimension: fault-code triage, work orders, outside invoices, technician notes, parts and warranty (`../vision/opportunities.md`). The section average is pulled down by urgency, scored 1 because Motive, Fleetio and Samsara shipped AI in this exact workflow in 2026 (https://gomotive.com/motive-launches-ai-powered-maintenance-to-help-operations-teams-prevent-breakdowns-increase-uptime-and-lower-repair-costs/). Revenue opportunity is clear but unproven: no price has been tested.

## 5. AI picture

Read together, Milewright is behind the market. It sits with the "Emerging" companies in the Houlihan Lokey calibration the rubric uses: an AI beta, no shipped feature, no AI line in revenue. Its competitors are "Scaling": Fleetio's AI Service Advisor approves repairs on its own, Motive's agents open work orders (https://www.truckinginfo.com/news/motive-adds-ai-agents-for-fleet-operations).

The automation upside sits in the **agentic layer**: closed-loop triage, drafting work orders, reserving parts, booking bays and filing warranty claims. That has a higher ceiling and is harder to copy once it runs inside a shop than prediction alone.

The same work is already being automated by others. Motive turns defects and fault codes into work orders automatically, and Samsara has warranty claim and purchase-order agents in early access (https://www.samsara.com/blog/samsaras-new-innovations-increase-efficiency). The upside is real, but it is not waiting.

The data flywheel is possible but not running: technicians' notes are too thin to learn from today [documents/interview-maintenance-manager-regional-carrier.md], and rights to learn across customers aren't confirmed [documents/fault-code-assist-beta-feedback.md].

## 6. Strategic priorities

1. **Ship one AI job that does work, not just explains it.**
   - Why now: prospects ask "What does your AI do?" in every second demo, and rivals show automatic work orders [documents/lost-deals-h1-2026.md].
   - A good outcome: drafted work orders from fault codes, approved unchanged most of the time by the beta customers.
   - Owner: the product manager for the core product.
2. **Capture what technicians actually found.**
   - Why now: without it, there's no accuracy check, no warranty claims and no flywheel.
   - A good outcome: complaint, cause and correction filled on most closed work orders.
   - Owner: product and design, with customer success.
3. **Settle the data rights.**
   - Why now: level 5 and benchmarks depend on it, and 30% of customers are on older contracts.
   - A good outcome: legal confirms what the 2021 contract allows, and an opt-in for the rest.
   - Owner: the general manager, with legal.

## 7. Watch-outs

- High upside, low shipping: a large automation surface with nothing shipped yet. How quickly can the team turn the beta into a product?
- Loyal large customers, thin structural lock-in: churn above 150 vehicles is 4%, but contracts are annual and exports are standard. Would they stay if a bundle matched the parts depth?
- Leadership appetite is inferred, not evidenced: will the group fund AI beyond the discretionary budget?
- The modern services around the legacy core are a stated direction; how much of the AI work can run outside the monolith?

## 8. Evidence quality

| Dimension | Score | Evidence Confidence | Score Basis | Flags |
|---|---|---|---|---|
| A1 | 4 | Medium | mixed | |
| A2 | 5 | High | direct_evidence | |
| A3 | 4 | Medium | mixed | |
| A4 | 3 | Medium | mixed | boundary_risk |
| A5 | 3 | Low | inference_heavy | inference_heavy |
| A6 | 3 | Medium | mixed | |
| B1 | 3 | High | direct_evidence | |
| B3 | 4 | Medium | direct_evidence | |
| C1 | 4 | High | direct_evidence | |
| C2 | 1 | High | direct_evidence | |
| C3 | 3 | Medium | mixed | |
| C4 | 4 | Medium | mixed | |

## 9. Evidence provenance

- **Business quality:** the invented one-pager, sales and churn notes and interviews, plus the FMCSA rules, Fleetio's customer count in trade press and the product manager's answers on stack and leadership. Leadership mindset is scored mainly by inference.
- **Customer strength:** the churn note's demonstrated switching by fleet size and plan.
- **AI opportunity:** the beta feedback note, the opportunities file, and Motive's, Fleetio's and Samsara's 2026 launch pages and trade coverage.
