# FleetDesk · value at each AI level

> Fictional example. FleetDesk and its features, customers and numbers are invented. The product manager's answers are tagged `[PM, illustrative]`.

**Level today:** 1, System of Record: the highest level with value that is shipped and used. FleetDesk stores and runs the maintenance work; people do all of it.
**Planned or in beta:** level 2, Fault Code Assist, in beta with 46 customers since May 2026 [documents/fault-code-assist-beta-feedback.md]. Beta doesn't count towards the level today.

## Summary

| Level | Value today? | Main features | For whom | How they pay |
|---|---|---|---|---|
| 1 System of Record | Yes, shipped and used by about 800 fleets | PM schedules, work orders, DVIR, parts, outside repairs, DOT records, reports | Maintenance manager, technician, parts manager, director of fleet operations | Per vehicle per month: Core $8, Pro $13, trailers $3 |
| 2 AI Assisted | Beta only | Fault Code Assist: explains codes, rates urgency, suggests a repair code | Maintenance manager, lead technician | Free in beta; price undecided |
| 3 AI Directed | No | none | | |
| 4 AI Delegated | No | none | | |
| 5 AI Domain Intelligence | No | none; 15 years of repair history is unused for this | | |
| 6 System of Understanding | No | none | | |

## Level 1 · System of Record

People do the work; the product stores and runs it.

| Feature | For whom | The value they get | How they pay | Status | Source |
|---|---|---|---|---|---|
| Preventive maintenance schedules by miles, engine hours or days, meters synced from Samsara, Motive and Geotab | Maintenance manager (user, influences the buy) | PMs done on time instead of "off a wall calendar"; fewer road calls | Included in Core | shipped and used | [documents/product-one-pager.md] [documents/interview-maintenance-manager-regional-carrier.md] |
| Work orders with labor, parts, VMRS codes and sign-off, on desktop or tablet | Technician (user), maintenance manager | One record of every repair per vehicle | Included in Core | shipped and used | [documents/product-one-pager.md] |
| Driver inspections (DVIR) in the Driver app, defects routed to the shop | Drivers, maintenance manager | Defects reach the shop the same day, with photos | Included in Core | shipped and used | [documents/interview-fleet-ops-director-distribution.md] |
| Parts inventory and purchasing across shops, vendor price history | Parts manager (user) | Stock in the right shop; purchase orders tracked. The stickiest feature: churn 3% where used in two or more shops | Pro, $13 per vehicle per month | shipped and used | [documents/product-one-pager.md] [documents/churn-note-2026.md] |
| Outside vendor repairs and invoices | Director of fleet operations, office staff | Every repair on one record, including dealers and roadside | Included in Core; invoices typed in by hand | shipped and used | [documents/interview-fleet-ops-director-distribution.md] |
| DOT annual inspection records and audit reports | Maintenance manager, director of fleet operations | An audit file in ten minutes instead of a week | Included in Core | shipped and used | [documents/interview-maintenance-manager-regional-carrier.md] |
| Warranty tracking | Parts manager, maintenance manager | Sees warranty dates on parts, if someone checks | Pro | shipped, little used (4% of tickets) | [documents/support-tickets-q3-2026.csv] `[PM, illustrative]` |
| Reports: cost per vehicle, PM compliance, technician productivity | Director of fleet operations | Monthly numbers, though cost per mile is still rebuilt in Excel | Included in Core | shipped and used | [documents/interview-fleet-ops-director-distribution.md] |

## Level 2 · AI Assisted

People do the work; AI suggests.

| Feature | For whom | The value they get | How they pay | Status | Source |
|---|---|---|---|---|---|
| Fault Code Assist: explains a fault code in plain English, rates it act now / plan in / watch, suggests a VMRS repair code | Maintenance manager, lead technician | "Saves my lead tech an hour a morning on the bad days"; the person still opens and types the work order | Free during beta; add-on or Pro undecided | beta, 46 customers, 31 active in the last 30 days | [documents/fault-code-assist-beta-feedback.md] |

## Level 3 · AI Directed

A person asks; AI does one task; the person checks each result.

none. `[PM, illustrative]` Nothing planned yet. The beta's users already ask for it: "If it already knows what the code is, why can't it start the work order and pull the parts?" [documents/fault-code-assist-beta-feedback.md]

## Level 4 · AI Delegated

AI does the job end to end; people handle exceptions.

none.

## Level 5 · AI Domain Intelligence

AI brings expertise learned from data across many customers.

none. `[PM, illustrative]` FleetDesk holds about 2 million work orders a year across 800 fleets, and buyers ask "How do we compare to fleets like us?", but nothing uses this data across customers yet. [documents/lost-deals-h1-2026.md]

## Level 6 · System of Understanding

The product understands how the domain works, anticipates and acts.

none.
