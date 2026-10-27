# Wrenchly · Where value flows

> Fictional example. Wrenchly, its documents, prices and numbers are invented; the product manager's answers are tagged `[PM, illustrative]`. Market facts are real and sourced.

Built from `../product.md`, `../vision/ai-levels.md`, `../vision/opportunities.md`, `../vision/market-moves.md`, the discovery reports and the product manager's answers on 27 Oct 2026.

**The shift:** most of the value goes to the fleet as a well-kept record, paid per vehicle, while the work around it is done by hand or captured by telematics bundles today → to the maintenance manager and the buyer as ready work and money recovered, paid per vehicle for the shop agent plus a share of warranty recovered, at level 4.

## Today

| Persona | The value they get | Who pays | For what | Roughly how much | Source |
|---|---|---|---|---|---|
| Director of fleet operations | One record of every repair, including outside vendors; clean DOT audits | Buyer | Per vehicle per month, Core or Pro | $8–$13 per vehicle per month, $3 per trailer; about $12,900 per customer a year on average | [documents/product-one-pager.md] `[PM, illustrative]` |
| Fleet maintenance manager | PM schedules that follow real miles; the audit file in ten minutes | Buyer pays; user | Included in the per-vehicle price | Part of the above | [documents/interview-maintenance-manager-regional-carrier.md] |
| Shop technician | The job, history and parts in one work order | Buyer pays; user | Included | Part of the above | [documents/product-one-pager.md] |
| Parts manager | Inventory and purchasing across shops | Buyer pays; user | Pro plan, $5 more per vehicle than Core | Pro customers using two or more shops churn 3% | [documents/product-one-pager.md] [documents/churn-note-2026.md] |

## Where value leaks today

Value the product creates or could create, but that goes somewhere else.

| The leak | Where it goes instead | How big | Source |
|---|---|---|---|
| Reading fault codes and typing work orders | The customer's own manual work: the lead tech's first hour each morning | An hour a day at a 240-tractor carrier | [documents/interview-maintenance-manager-regional-carrier.md] |
| Technician notes, time and part numbers | The customer's own manual work, and thin records | An estimated 20–30 minutes per job | [documents/interview-maintenance-manager-regional-carrier.md] |
| Outside invoices typed in and never compared | The customer's own manual work; vendors' overcharges go unnoticed | Half of one distributor's repair spend goes outside | [documents/interview-fleet-ops-director-distribution.md] |
| Warranty not claimed | Not recovered at all | "Maybe a third" recovered, by one customer's estimate | [documents/interview-maintenance-manager-regional-carrier.md] |
| Cost per mile for the CFO | A spreadsheet, two days a month | Every month, at every buyer who reports it | [documents/interview-fleet-ops-director-distribution.md] |
| Fault-code insight and the "one bill" | Telematics vendors, who now sell maintenance in their bundle | 31 customers lost to bundles in a year | [documents/churn-note-2026.md] |
| Fault Code Assist | Not charged for during the beta | 46 customers | [documents/fault-code-assist-beta-feedback.md] |
| Repair history across 800 fleets | Not used; buyers ask for benchmarks we don't offer | About 2 million work orders a year | [documents/lost-deals-h1-2026.md] `[PM, illustrative]` |

## At the vision's target level

Level 4, AI Delegated, by the end of 2028 (`../vision/vision.md`).

| Persona | The job AI does | The value they get | What they'd pay for | Source |
|---|---|---|---|---|
| Fleet maintenance manager | Triages every fault code and defect; drafts work orders with cause, parts and a slot | Approves a short list instead of typing; fewer road calls | Trucks back on the road sooner: a per-vehicle shop agent | `../vision/opportunities.md` #1 |
| Shop technician | Writes the note from the technician's voice | Wrenching instead of typing | Included in the shop agent | `../vision/opportunities.md` #3 |
| Parts manager | Reserves parts and drafts purchase orders from the plan; tags and claims warranty | No truck waiting on parts; money back | A share of warranty money recovered | `../vision/opportunities.md` #4, #5 |
| Director of fleet operations | Reads and checks every outside invoice; reports cost per mile | Overcharges caught; the CFO report done | Money saved on outside repairs, within the shop agent | `../vision/opportunities.md` #2 |

## Who else could capture it

| Who | How they'd capture the value | What keeps it with us |
|---|---|---|
| Telematics vendors: Motive, Samsara, Geotab | Already turn fault codes into work orders and sell one bill to the CFO (https://gomotive.com/motive-launches-ai-powered-maintenance-to-help-operations-teams-prevent-breakdowns-increase-uptime-and-lower-repair-costs/) | Workflow: the shop's parts, bays and technicians; data across all three providers' trucks |
| Fleetio | Approves low-risk repairs on its own at a lower price (https://itbrief.co.uk/story/fleetio-opens-ai-service-advisor-after-maintenance-beta, https://www.fleetio.com/pricing) | Workflow and data: deeper multi-shop parts and fleets with their own shops |
| A general AI assistant | Reads fleet data through connectors and answers or schedules (https://truckinginfo.com/news/what-geotabs-new-ai-connector-means-for-fleets) | Trust: the DOT record and the approved work order live with us |
| ServiceUp and repair networks | Coordinate outside repairs end to end (https://www.serviceup.com/blog/serviceup-launches-the-agentic-repair-platform-for-modern-fleets) | Distribution: our customers do most repairs in their own shops |

## How we'd charge

- **Today:** per vehicle per month: Core $8, Pro $13, trailers $3, on annual contracts, plus implementation [documents/product-one-pager.md].
- **Tomorrow:** the per-vehicle base stays for the record. On top: a per-vehicle shop agent, and a share of warranty money recovered. Later, a yearly subscription for benchmarks. `[PM, illustrative]`
- **What has to be true:** managers approve drafted work orders without rework most of the time; we can show the buyer road calls and downtime falling, and money recovered, in numbers the CFO accepts. "I'd pay more if it cut downtime and I could prove it to the CFO." [documents/interview-fleet-ops-director-distribution.md]

## Open questions

- Is the shop agent a Pro feature, to defend against bundles, or a paid add-on?
- How do we measure downtime saved in a way buyers trust?
- What share of warranty recovered is fair, and who verifies the amount?
- Should we partner with a telematics vendor rather than compete for the "one bill"?
