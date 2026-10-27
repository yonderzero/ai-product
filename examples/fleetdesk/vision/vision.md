# FleetDesk · AI vision

> Fictional example. FleetDesk and the product manager's answers are invented, tagged `[PM, illustrative]`. Market facts cite the other files in this folder; the real products named under Imagine cite their own pages.

**Today:** level 1, System of Record. Nothing AI is shipped and used; Fault Code Assist is a level 2 beta. Ten of the fifteen placed companies are already at level 3 or above, including Samsara, Motive and Fleetio (`market-map.md`, `ai-levels.md`).
**Where we're going:** level 4, AI Delegated, by the end of 2028. `[PM, illustrative]`

## The vision

By the end of 2028, FleetDesk does the paperwork of the shop. Every fault code, driver defect and outside invoice becomes ready work: a drafted work order with the likely cause, the parts reserved and a slot booked around the truck's route. The maintenance manager approves instead of types, and spends the morning on the three trucks that need a person's judgement. `[PM, illustrative]`

## Imagine

*Illustrative sketches, not plans. They show what each level could mean for FleetDesk.*

### Our product at each level

| Level | Already there | Our product at this level |
|---|---|---|
| 2 AI Assisted | **Grammarly**: suggests clearer, correct writing as you type [https://www.grammarly.com/]. **Gmail Smart Compose**: suggests the rest of the sentence [https://workspaceupdates.googleblog.com/2018/09/gmail-smart-compose-gsuite.html] | Fault Code Assist, shipped: every code explained, rated and given a suggested repair code. Work orders suggest the VMRS code and parts from the truck's history as the technician types. The manager still decides and clicks everything. Included in Pro, to win the "What does your AI do?" question in demos. |
| 3 AI Directed | **Microsoft 365 Copilot**: drafts documents from your files when asked [https://learn.microsoft.com/en-us/office365/servicedescriptions/office-365-platform-service-description/microsoft-365-copilot]. **Shopify Sidekick**: does a merchant's task and shows the change for approval [https://help.shopify.com/en/manual/shopify-admin/productivity-tools/sidekick] | The technician says "Replaced the left steer tire, cut sidewall, 4/32 tread on the right" and FleetDesk writes the complaint, cause and correction, codes it and fills the time. The manager asks "Which trucks are due a PM and an annual inspection next week?" and gets the plan, ready to send to dispatch. Paid as a per-vehicle add-on. |
| 4 AI Delegated | **Intercom Fin**: answers support conversations end to end, paid per outcome [https://fin.ai/pricing]. **Abridge**: writes the clinical note from the doctor's visit; the doctor signs it [https://www.abridge.com/] | FleetDesk triages every fault code overnight, drafts the work orders that matter with parts reserved and a bay booked, reads and checks every outside invoice, and files warranty claims. The maintenance manager approves a short list each morning; small known jobs go through by rule. Paid per vehicle for the shop agent, plus a share of warranty money recovered. |
| 5 AI Domain Intelligence | **Harvey**: legal research and drafting that law firms trust [https://www.harvey.ai/]. **OpenEvidence**: answers clinicians' questions from the medical literature [https://siliconangle.com/2025/10/20/medical-search-engine-startup-openevidence-closes-200m-investment-led-gv/] | FleetDesk knows how trucks fail across 800 fleets and 15 years of repairs. "Tractors like yours, on routes like yours, lose this turbo actuator at 410,000 miles. Four of yours are past 390,000." The director sees cost per mile against fleets like theirs, and which vendors charge more for the same job. Sold as a yearly benchmark and prediction subscription. |
| 6 System of Understanding | **Waymo**: drives riders with no one at the wheel [https://waymo.com/]. **Tempus**: combines clinical and molecular data to guide cancer care [https://www.tempus.com/oncology/] | FleetDesk understands how each truck, route and shop behaves. It plans the shop around dispatch's week, orders parts before they're needed, pulls a truck in before it breaks down, and tells the director when to replace a truck rather than repair it. Fleets pay for uptime: trucks ready when dispatch needs them. |

### A day with our System of Understanding

Rosa runs maintenance for a 240-tractor regional carrier with two shops, in 2029.

At 5:30 she opens FleetDesk on her phone. Overnight it read 1,900 fault codes from the trucks. It dropped the noise, and found two that matter. Truck 418's coolant temperature pattern matches 37 trucks across other fleets that lost a water pump within a week. Nobody told it to look; it knows what that pattern led to before. It has already moved 418's PM forward to this morning, reserved the pump in the north shop, and asked dispatch to swap the load to truck 422. Dispatch said yes at 4 am.

She never reads a fault-code list again. She never types an outside invoice, and never rebuilds the cost-per-mile report: the CFO gets it on the first of the month, with the reasons it moved.

At 9 she gets one question she has to answer herself. A dealer quoted $4,800 for an aftertreatment job that costs $3,100 at the shop down the road, but the dealer can do it today and the road shop can't until Thursday. FleetDesk shows the cost of two days off the road. She chooses the dealer.

The technicians talk to the tablets as they work. Their notes are complete, so warranty claims go out the same day, and FleetDesk files them.

Rosa spends the afternoon with her two newest technicians, on the jobs the system flagged as ones new techs most often get wrong. Road calls are down by half since 2027. Her job is the people, the vendors and the judgement calls.

**What excites us:** the morning fault-code list disappears, and the shop works on the right trucks before they break down. `[PM, illustrative]`
**What it would need to know, and the data that takes:** what each fault code actually led to, which needs technicians' findings captured on every job (opportunity #3), and repair outcomes across fleets, which needs customers' permission. It would also need dispatch's plan, which sits in the fleet's dispatch system, not in FleetDesk. `[PM, illustrative]`

## Built on

- **From fault code to a ready work order:** Do first, 4.60 (`opportunities.md` #1). The heart of the vision.
- **Outside invoices read and checked for you:** Do first, 4.20 (`opportunities.md` #2).
- **Technician notes from the technician's voice:** Do first, 3.85 (`opportunities.md` #3). The foundation: good notes make the work orders, warranty claims and, later, the level 5 predictions possible.
- **"Fleets like us": cost-per-mile benchmarks:** Strong option, 3.30 (`opportunities.md` #6). The step after the vision, once contracts and data allow it.

## For whom

| Persona | The problem it removes | What changes in their day |
|---|---|---|
| Fleet maintenance manager | Reading hundreds of fault codes and typing work orders (`opportunities.md` step 2) | Approves a short list of drafted work orders each morning; spends time on the trucks that need judgement `[PM, illustrative]` |
| Shop technician | 20–30 minutes of typing per job [documents/interview-maintenance-manager-regional-carrier.md] | Talks while working; checks and signs the note |
| Director of fleet operations | Typing and checking outside invoices; cost per mile in Excel [documents/interview-fleet-ops-director-distribution.md] | Sees which vendors charge more, and fewer trucks down at 5 am |

## What AI takes over

| Workflow | Today | Tomorrow |
|---|---|---|
| Fault code to work order | A person reads every code, looks it up and types a work order (`opportunities.md` step 2) | FleetDesk triages every code and drafts the work order with parts and a slot. The manager approves; small known jobs go through by rule `[PM, illustrative]` |
| Outside repairs | Office staff type invoices line by line; nobody compares vendors (`opportunities.md` step 7) | FleetDesk reads, codes and checks every invoice; a person sees only the ones that don't match `[PM, illustrative]` |
| Repair notes | Technicians type, or don't (`opportunities.md` step 4) | Technicians speak; FleetDesk writes, technicians sign `[PM, illustrative]` |

## Why us

- 15 years of work orders, repairs, parts and outside invoices for about 800 fleets, roughly 2 million work orders a year (`../product.md`).
- The shop's own work: multi-shop parts, purchasing and DOT records, where we win half our deals with fleets of 150 to 500 vehicles [documents/lost-deals-h1-2026.md].
- Telematics data from all three big providers in one place for about 310 customers [documents/fault-code-assist-beta-feedback.md]. A telematics vendor's bundle sees only its own trucks' data.
- Implementation specialists who ran fleet shops themselves [documents/lost-deals-h1-2026.md].

## The opening

Level 4 has two players and neither runs the fleet's own shop end to end: Fleetio approves repairs and ServiceUp coordinates outside repairs. Level 5 has one low-confidence player selling mostly to large fleets and OEMs, and level 6 is empty (`market-map.md`). The in-house shop of the mid-size fleet, from fault code to parts to bay to warranty, is open.

## Others moving this way

| Who | At which level | What makes our vision different |
|---|---|---|
| Motive | 3; its agents can already open work orders (`market-map.md`, `market-moves.md`) | Motive starts from its own trucks' data and the CFO's bill; we start from the shop, its parts and its technicians, and work with every telematics provider |
| Samsara | 3, heading to 4 with purchase orders and warranty claims (`market-map.md`) | Same as Motive; strong agents platform, lighter shop and parts depth |
| Fleetio | 4 (`market-map.md`) | Approves repairs within limits, strongest with smaller fleets and outside repairs; we plan the in-house shop's work around parts and bays |
| Uptake (Bosch) | 5, low confidence (`market-map.md`) | Predicts failures for large fleets and OEMs; we could take its kind of prediction straight into the work order and the parts room |

## What customers would pay for

If an agent sat on top of our data tomorrow, customers would stop paying us just to store work orders and print the DOT file; a telematics bundle or a general assistant could do that. They would pay instead for trucks back on the road sooner and money they get back: a per-vehicle shop agent that turns codes and defects into ready work, and a share of warranty money recovered. Later, a yearly subscription for benchmarks. `[PM, illustrative]`

## First step

Pilot "from fault code to a ready work order" with 10 of the 46 Fault Code Assist beta customers. For each drafted work order, record whether the manager approved it unchanged, edited or rejected it, and what the technician actually found. In the same calls, test two prices: included in Pro, or $3 per vehicle per month as an add-on. `[PM, illustrative]`

## Open questions

- How accurate must drafted work orders be before managers approve without checking?
- Do we partner with Samsara and Motive, or compete with their maintenance bundles?
- Will customers allow their repair outcomes to train models across fleets, and on what terms?
- Can we get dispatch's plan, or do we schedule around it without it?
