# FleetDesk · Opportunities

> Fictional example. FleetDesk, its documents and numbers are invented; market facts are real and sourced. The product manager's answers are tagged `[PM, illustrative]`. Sources marked "vendor" are companies selling software for that step: the rules count them as one voice.

Built from `../product.md`, `ai-levels.md`, `market-map.md`, `market-moves.md` and `documents/` on 27 Oct 2026.

## The work around the product

| # | Step | What happens | Who | Software | Still manual | Coverage | Who's moving here | Our AI level |
|---|---|---|---|---|---|---|---|---|
| 1 | Driver inspection and defects | Drivers do pre- and post-trip inspections; defects go to the shop | Driver, maintenance manager | FleetDesk Driver app, Whip Around, Fleetpal, telematics apps | Paper inspections at some fleets; drivers "pencil-whip" forms (search result: https://www.ccjdigital.com/business/article/14937883/how-electronic-dvirs-help-to-ensure-proper-truck-inspections); defects retyped into work orders where systems aren't joined (vendor: https://www.samsara.com/products/telematics/fleet-maintenance) | software | Fleetpal (free), Whip Around (AI photo checks), Motive | 1 |
| 2 | Fault codes and triage | Telematics sends fault codes; someone decides which matter and opens a work order | Maintenance manager, lead technician | Samsara, Motive, Geotab, OEM portals, FleetDesk | Each code read and looked up by hand: "My lead tech spends the first hour of his day as a fault-code clerk" [documents/interview-maintenance-manager-regional-carrier.md]; 12% of our tickets [documents/support-tickets-q3-2026.csv]. Diagnostics ranked third in TMC fleet members' concerns, Fall 2025 (https://tmc.trucking.org/blog/tmc-fleet-members-top-maintenance-concerns-shift-considerably-fall-2025-spring-2026) | partial | Motive, Samsara, Fleetio, Uptake | 2 in beta (Fault Code Assist) |
| 3 | PM and DOT inspection planning | Schedule PMs and annual inspections; plan the shop's day | Maintenance manager | FleetDesk, spreadsheets, whiteboards | Day planned on a whiteboard, then typed in; PMs missed when dispatch keeps a truck out, with nothing rescheduling it [documents/interview-maintenance-manager-regional-carrier.md]; meter sync is 18% of tickets [documents/support-tickets-q3-2026.csv]. Job postings ask fleet managers for Excel to coordinate 3/6/12-month DOT inspections (https://jobs.khoslaventures.com/companies/cloudtrucks/jobs/39004423-fleet-manager) | partial | Samsara (Shop Planner) | 1 |
| 4 | Repair and work-order notes | Technician repairs, records complaint, cause and correction, labor, parts and VMRS code; manager reviews | Technician, maintenance manager | FleetDesk tablet and desktop | Techs spend an estimated 20–30 minutes per job typing and close with "replaced" [documents/interview-maintenance-manager-regional-carrier.md]; "too many clicks to close a work order" [documents/churn-note-2026.md]; postings require "documentation that backs up the complaint, cause, and correction" (search result: https://www.interviewpal.com/jobs/2119855443) | partial | Fullbay (AI note clean-up), Fleetio | 1 |
| 5 | Parts and purchasing | Look up, stock, order and receive parts; return cores and warranty parts | Parts manager | FleetDesk Pro, vendor websites, spreadsheets | Trucks wait for parts the PM schedule predicted [documents/interview-fleet-ops-director-distribution.md]; counts off after receiving, 15% of tickets [documents/support-tickets-q3-2026.csv]; postings list cycle counts, POs and invoice checks by hand (search result: https://www.arjoblink.arkansas.gov/jobs/4462165) | partial | Samsara (automatic POs, early access) | 1 |
| 6 | Warranty recovery | Check if a failed part is under warranty, tag it, file the claim | Parts manager, technician, maintenance manager | FleetDesk Pro (little used), OEM portals | "Maybe a third" recovered [documents/interview-maintenance-manager-regional-carrier.md]; "coverage isn't visible at the moment of repair" (vendor-sponsored: https://www.fleetowner.com/resources/white-papers/whitepaper/55409832/the-money-youre-already-owed-a-warranty-recovery-playbook) | manual | Samsara (warranty claim agent, early access), Fleetio | 1 |
| 7 | Outside repairs and invoices | Send trucks to dealers and vendors; enter and check their invoices | Director of fleet operations, office staff | FleetDesk, email, accounting | Invoices arrive as PDFs and faxes and are typed in line by line [documents/interview-fleet-ops-director-distribution.md] [documents/interview-maintenance-manager-regional-carrier.md]; a five-page invoice "could take an administrator 30 to 45 minutes to key in" (Sobeys, quoted by vendor: https://www.samsara.com/ca/blog/sobeys-fleet-maintenance-ai) | partial | Motive, Samsara, Collective Data, RTA, Trimble TMT, ServiceUp, Fleetio | 1 |
| 8 | DOT records and audits | Keep inspection, repair and annual inspection records; answer audits and roadside inspections | Maintenance manager | FleetDesk | Mostly covered: an audit file "in ten minutes" [documents/interview-maintenance-manager-regional-carrier.md]. Rules: maintenance records 1 year plus 6 months after a vehicle leaves (https://www.law.cornell.edu/cfr/text/49/396.3); periodic inspection every 12 months (https://www.law.cornell.edu/cfr/text/49/396.17) | software | Fleetio, Whip Around | 1 |
| 9 | Cost per mile and downtime reporting | Report maintenance cost, downtime and availability to the CFO | Director of fleet operations | FleetDesk exports, Excel, fuel card portal | "Two days a month, every month" in Excel [documents/interview-fleet-ops-director-distribution.md]; 9% of tickets [documents/support-tickets-q3-2026.csv]. Repair and maintenance cost per mile rose 8.6% in 2025 (https://truckingresearch.org/2026/07/new-atri-report-details-accelerating-costs-and-low-profitability-despite-cuts/) | partial | Motive (cost per mile, heading), RTA, Geotab | 1 |

## Opportunities, ranked

| # | Opportunity | Kind | Level | Impact | Effort | Urgency | Evidence | Priority | Band |
|---|---|---|---|---|---|---|---|---|---|
| 1 | From fault code to a ready work order | Grow the base | 4 | 5 | 3 | 5 | Strong | 4.60 | Do first |
| 2 | Outside invoices read and checked for you | Grow the base | 4 | 4 | 2 | 4 | Strong | 4.20 | Do first |
| 3 | Technician notes from the technician's voice | Grow the base | 3 | 3 | 2 | 4 | Strong | 3.85 | Do first |
| 4 | Parts ready before the truck arrives | Grow the base | 4 | 4 | 3 | 3 | Good | 3.55 | Strong option |
| 5 | Warranty money found and claimed | New revenue | 4 | 4 | 3 | 3 | Good | 3.55 | Strong option |
| 6 | "Fleets like us": cost-per-mile benchmarks | New revenue | 5 | 4 | 4 | 2 | Strong | 3.30 | Strong option |

## 1. From fault code to a ready work order

- **The job today:** every morning the maintenance manager or lead technician reads a list of fault codes, "a few hundred" at a 240-tractor carrier, looks each one up, decides if it matters and types a work order [documents/interview-maintenance-manager-regional-carrier.md]. Fault codes are 12% of support tickets [documents/support-tickets-q3-2026.csv]. Fault Code Assist explains codes, but beta users ask "why can't it start the work order and pull the parts?" [documents/fault-code-assist-beta-feedback.md]
- **What the product would do:** an agent reads every code with the truck's repair history, groups repeats, drops noise, and for the ones that matter drafts the work order: likely cause, VMRS code, parts in stock or to order, and a proposed shop slot around the truck's route. The manager approves, edits or rejects; small, known jobs can be approved by rule.
- **For whom:** maintenance manager (user, influences the buy); director of fleet operations (buyer), who gets fewer road calls.
- **Kind and level:** grow the base; level 4.
- **Who else is going after it:** Motive turns defects and fault codes into work orders automatically, and Motive Agents can open one on their own (https://www.truckinginfo.com/news/motive-adds-ai-agents-for-fleet-operations); Samsara's maintenance agents; Fleetio's AI Service Advisor drafts work orders (`market-map.md`).
- **Ratings:** impact 5 because it defends the core against telematics bundles, which took 31 of the 88 customers we lost [documents/churn-note-2026.md]; effort 3 because the beta, the codes and the repair history exist, but parts and scheduling must join in and outcomes must be captured to check accuracy; urgency 5 because Motive already does this job for fleets that used to be our customers; evidence Strong because there are five findings across interviews, tickets, beta data and competitors, with customer quotes.
- **Priority:** 0.35 × 5 + 0.25 × 5 + 0.20 × 5 + 0.20 × (6 − 3) = 1.75 + 1.25 + 1.00 + 0.60 = 4.60 → Do first
- **Size (retention):** 37 customers with a bundled offer at renewal (measured [documents/churn-note-2026.md]) × about $12,900 revenue per customer a year ($10.5M across 812 customers, measured `[PM, illustrative]`) × 30–60% of that churn avoided (assumption) = about $143,000–$286,000 a year kept. An add-on price would come on top; not sized, because no customer has been asked a price yet.
- **First question:** "If FleetDesk drafted the work order from the fault code, with parts and a slot, what would you need to see before you approved it without checking?"

## 2. Outside invoices read and checked for you

- **The job today:** dealer, roadside and vendor invoices arrive as PDFs, email and fax; office staff type them in line by line [documents/interview-fleet-ops-director-distribution.md] [documents/interview-maintenance-manager-regional-carrier.md]. 7% of tickets ask how to enter them faster [documents/support-tickets-q3-2026.csv]. At Sobeys, a long invoice took "30 to 45 minutes to key in" and parts were miscoded (quoted by Samsara: https://www.samsara.com/ca/blog/sobeys-fleet-maintenance-ai). "I have no idea if the dealer in Joliet charges me twice what the one in Gary does." [documents/interview-fleet-ops-director-distribution.md]
- **What the product would do:** read every invoice, code it to the vehicle and VMRS, post it, and compare each line with the fleet's own history and the same job at other vendors. Only invoices that don't match, or look high, go to a person.
- **For whom:** director of fleet operations (buyer); office and parts staff.
- **Kind and level:** grow the base; level 4.
- **Who else is going after it:** Motive, Samsara, Collective Data, RTA and Trimble TMT all read invoices with AI; ServiceUp and Fleetio check repair costs (`market-map.md`).
- **Ratings:** impact 4 because the buyer says checking vendors "would pay for itself in a quarter", a feature customers will pay extra for; effort 2 because reading invoices is now common technology and we already hold vendor price history; urgency 4 because several competitors shipped invoice reading in 2026; evidence Strong because there are five findings across interviews, tickets and a third-party fleet's quote.
- **Priority:** 0.35 × 4 + 0.25 × 4 + 0.20 × 5 + 0.20 × (6 − 2) = 1.40 + 1.00 + 1.00 + 0.80 = 4.20 → Do first
- **Size:** not sized: we don't know how many customers send half their repairs outside, as this distributor does.
- **First question:** "If we flagged every outside invoice that's higher than your history, how much would that be worth to you a year?"

## 3. Technician notes from the technician's voice

- **The job today:** technicians type notes, time and part numbers on a tablet, an estimated 20–30 minutes per job, and often close with "replaced" or "fixed", so warranty claims fail and repeat repairs hide [documents/interview-maintenance-manager-regional-carrier.md]. 13% of tickets are about closing work orders [documents/support-tickets-q3-2026.csv]; 14 churned customers named the mobile app and too many clicks [documents/churn-note-2026.md].
- **What the product would do:** the technician says what they found and did; FleetDesk writes complaint, cause and correction, picks the VMRS code and parts used, and fills the time. The technician checks and signs.
- **For whom:** technician (user); maintenance manager, who reviews every work order.
- **Kind and level:** grow the base; level 3.
- **Who else is going after it:** Fullbay turns shorthand and dictated notes into clean repair records (https://www.worktruckonline.com/news/fullbay-debuts-ai-tool-and-key-platform-upgrades).
- **Ratings:** impact 3 because it's a clear sales and retention story but not a paid product on its own; effort 2 because speech-to-text and general models do most of it, on our own work-order data; urgency 4 because Fullbay shipped it; evidence Strong because there are four findings across interviews, tickets, churn notes and job postings, with a customer quote.
- **Priority:** 0.35 × 3 + 0.25 × 4 + 0.20 × 5 + 0.20 × (6 − 2) = 1.05 + 1.00 + 1.00 + 0.80 = 3.85 → Do first
- **Size:** not sized: the value is time and better records, not new revenue.
- **First question:** "Would your technicians talk to the tablet in the bay, and would you trust what it wrote?"

## 4. Parts ready before the truck arrives

- **The job today:** "We know the PM is due. We know which filters it takes. Why am I waiting on filters?" [documents/interview-fleet-ops-director-distribution.md] Parts counts and receiving are 15% of tickets [documents/support-tickets-q3-2026.csv].
- **What the product would do:** from the PM schedule and drafted work orders, reserve parts in the right shop and draft purchase orders for what's missing, for the parts manager to approve.
- **For whom:** parts manager (user); maintenance manager.
- **Kind and level:** grow the base; level 4.
- **Who else is going after it:** Samsara generates purchase orders automatically (early access) (https://www.samsara.com/blog/samsaras-new-innovations-increase-efficiency); Fullbay plans parts forecasting (announced).
- **Ratings:** impact 4 because parts across shops is our stickiest feature (churn 3%) and sits in the Pro plan [documents/churn-note-2026.md]; effort 3 because it needs reliable meter sync, which causes 18% of tickets today; urgency 3 because a competitor has it in early access; evidence Good because there are two kinds of finding, with a customer quote.
- **Priority:** 0.35 × 4 + 0.25 × 3 + 0.20 × 4 + 0.20 × (6 − 3) = 1.40 + 0.75 + 0.80 + 0.60 = 3.55 → Strong option
- **Size:** not sized: no measure yet of how much downtime is spent waiting for parts.
- **First question:** "How many hours did trucks wait for parts last month, and which parts?"

## 5. Warranty money found and claimed

- **The job today:** nobody checks if a failed part is still under warranty; one customer thinks they recover "maybe a third" [documents/interview-maintenance-manager-regional-carrier.md]. Our warranty tracking is little used: 4% of tickets [documents/support-tickets-q3-2026.csv]. Unclaimed warranty "shows up as repair spend that looks normal" (vendor-sponsored: https://www.fleetowner.com/resources/white-papers/whitepaper/55409832/the-money-youre-already-owed-a-warranty-recovery-playbook).
- **What the product would do:** check every closed work order against warranty terms, tag the part for return, and draft the claim with the technician's notes; the parts manager sends it.
- **For whom:** parts manager, maintenance manager; the director sees money recovered.
- **Kind and level:** new revenue, priced as a share of money recovered; level 4.
- **Who else is going after it:** Samsara's warranty claim agent (early access); Fleetio checks warranty during repairs (`market-map.md`).
- **Ratings:** impact 4 because a share of recovered money is a new revenue line customers can see; effort 3 because warranty terms by part and OEM aren't in FleetDesk today, and it depends on good technician notes (#3); urgency 3 because Samsara has it in early access; evidence Good because there are two findings and a customer's estimate, but no independent study of money missed.
- **Priority:** 0.35 × 4 + 0.25 × 3 + 0.20 × 4 + 0.20 × (6 − 3) = 1.40 + 0.75 + 0.80 + 0.60 = 3.55 → Strong option
- **Size:** not sized: no measured figure for warranty money missed, and public figures are vendor claims without a study.
- **First question:** "How much did you claim in warranty last year, and how much do you think you missed?"

## 6. "Fleets like us": cost-per-mile benchmarks

- **The job today:** the buyer rebuilds cost per mile in Excel "two days a month" [documents/interview-fleet-ops-director-distribution.md]; buyers above 150 vehicles ask "How do we compare to fleets like us?" [documents/lost-deals-h1-2026.md]; a customer asked the same [documents/interview-maintenance-manager-regional-carrier.md]. Repair and maintenance cost per mile rose 8.6% in 2025, the second-largest increase of any cost (https://truckingresearch.org/2026/07/new-atri-report-details-accelerating-costs-and-low-profitability-despite-cuts/).
- **What the product would do:** cost per mile, downtime and failure rates by vehicle type, age and duty, compared with similar fleets that opt in, with the reasons behind the gaps.
- **For whom:** director of fleet operations (buyer).
- **Kind and level:** new revenue, a yearly subscription; level 5.
- **Who else is going after it:** Motive is heading to cost per mile and total cost of ownership (announced); Fleetio talks of 14 years of maintenance data; Uptake learns across fleets (`market-map.md`).
- **Ratings:** impact 4 because benchmarks are a product buyers ask for and would pay extra for; effort 4 because the data exists but 30% of customers aren't on contracts that allow aggregated use, and the coding must be cleaned [documents/fault-code-assist-beta-feedback.md]; urgency 2 because nobody in our segment ships it yet; evidence Strong because there are four findings across sales notes, two interviews and ATRI research, with customer quotes.
- **Priority:** 0.35 × 4 + 0.25 × 2 + 0.20 × 5 + 0.20 × (6 − 4) = 1.40 + 0.50 + 1.00 + 0.40 = 3.30 → Strong option
- **Size:** not sized: there is no price test yet, and the share of customers who would opt in is unknown.
- **First question:** "Would you share your de-identified repair costs to see how you compare with fleets like yours?"

## From Imagine

- **A shop that plans itself around the routes** (level 6, evidence: Assumption): the product books every PM, repair and part around dispatch's plan, so no truck misses a PM because it was on the road. Came up in `vision.md`. Beyond the product manager's belief, there's one interview [documents/interview-maintenance-manager-regional-carrier.md], and it needs dispatch data we don't hold, so it isn't rated yet. `[PM, illustrative]`

## Open questions

- How accurate are Fault Code Assist's suggestions against what technicians found? Nobody has checked [documents/fault-code-assist-beta-feedback.md].
- Do our 2021 contracts cover training models on repair outcomes across customers?
- Would customers pay for AI as an add-on per vehicle, or only for outcomes such as money recovered?
- Do we partner with telematics vendors or compete with their maintenance bundles?
- Rescheduling missed PMs around dispatch (step 3) has good evidence, but needs dispatch data we don't hold; worth asking about.
