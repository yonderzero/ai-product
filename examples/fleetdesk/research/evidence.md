# Evidence map · FleetDesk

> Fictional example. FleetDesk, its documents and the product manager's answers are invented, tagged `[PM, illustrative]`. Line numbers point to the files in `../documents/`.

What our own data says about our customers, before any persona is written. One row per piece of evidence. No real names: the documents already had names removed, so no anonymised copies were needed. Built on 27 Oct 2026.

**The problem we're researching:** getting every truck that needs work from the first signal (fault code, driver defect, PM coming due) back on the road (`../problem/problem.md`).

## Customer types we see

| Type | How many in our data | Example source |
|---|---|---|
| Regional and LTL carriers with their own shops (maintenance manager, lead tech, technicians) | 1 interview, 1 beta quote, ticket themes | documents/interview-maintenance-manager-regional-carrier.md |
| Foodservice and beverage distributors (director of fleet operations, parts manager) | 1 interview, 1 beta quote | documents/interview-fleet-ops-director-distribution.md |
| Waste haulers and other mid-size private fleets (maintenance manager, shop supervisor) | 2 beta quotes | documents/fault-code-assist-beta-feedback.md |
| Smaller fleets, under 75 vehicles (buyer in finance or operations) | 61 of 88 churned; lost-deal themes | documents/churn-note-2026.md, documents/lost-deals-h1-2026.md |
| All customers (support) | 1,940 tickets in Q3 2026 | documents/support-tickets-q3-2026.csv |

## Evidence

| Customer type | Kind | What they said or did | Source (file, line) |
|---|---|---|---|
| Carrier, maintenance manager | quote | "Two of them will be the truck that breaks down on I-70 tonight, and I can't tell which two." | documents/interview-maintenance-manager-regional-carrier.md, line 11 |
| Carrier, maintenance manager | pain | 40 driver write-ups and a few hundred fault codes waiting each morning; most codes are noise | documents/interview-maintenance-manager-regional-carrier.md, line 11 |
| Carrier, lead technician | workaround | The lead tech reads, looks up and decides on each code, then opens work orders: "a fault-code clerk" | documents/interview-maintenance-manager-regional-carrier.md, line 23 |
| Carrier, maintenance manager | workaround | Plans the shop day on a whiteboard, then types it into FleetDesk; dispatch changes it twice before noon | documents/interview-maintenance-manager-regional-carrier.md, line 12 |
| Carrier, maintenance manager | pain | When dispatch keeps a truck on a route past its PM slot, nothing reschedules it; the planner finds out when it's overdue | documents/interview-maintenance-manager-regional-carrier.md, line 26 |
| Carrier, technicians | pain | Techs close with "replaced" or "fixed"; cause and correction missing, so warranty claims get rejected | documents/interview-maintenance-manager-regional-carrier.md, line 24 |
| Carrier, technicians | quote | "Half my techs would rather turn a wrench for two hours than type for ten minutes." | documents/interview-maintenance-manager-regional-carrier.md, line 24 |
| Carrier, maintenance manager | budget signal | "If it wrote the work order from the fault code and the tech just checked it, I'd pay for that." | documents/interview-maintenance-manager-regional-carrier.md, line 32 |
| Carrier, maintenance manager | quote | "Don't give me another dashboard. Give me the three trucks I need to pull in today, and why." | documents/interview-maintenance-manager-regional-carrier.md, line 31 |
| Carrier, maintenance manager | objection | Samsara's maintenance is "a checklist", but the CFO sees one bill instead of two | documents/interview-maintenance-manager-regional-carrier.md, line 33 |
| Carrier, maintenance manager | pain | Warranty: recovers "maybe a third" of what they could | documents/interview-maintenance-manager-regional-carrier.md, line 25 |
| Carrier, maintenance manager | trigger | Measured on road calls per million miles, PM compliance, out-of-service rate, cost per mile | documents/interview-maintenance-manager-regional-carrier.md, line 13 |
| Distributor, director | quote | "I don't need AI that talks to me. I need trucks ready at 5 am." | documents/interview-fleet-ops-director-distribution.md, line 30 |
| Distributor, director | pain | Trucks wait for parts nobody ordered ahead of the PM: "Why am I waiting on filters?" | documents/interview-fleet-ops-director-distribution.md, line 23 |
| Distributor, director | budget signal | "A truck down for a day costs me more than FleetDesk costs me for a year for that truck." | documents/interview-fleet-ops-director-distribution.md, line 11 |
| Distributor, director | budget signal | Would pay more per truck if it cut downtime and he could prove it to the CFO | documents/interview-fleet-ops-director-distribution.md, line 32 |
| Distributor, director | workaround | Rebuilds the cost-per-mile report in Excel from three sources, "two days a month, every month" | documents/interview-fleet-ops-director-distribution.md, line 12 |
| Distributor, director | objection | Too many logins; Motive offers maintenance in one login: "I haven't said no." | documents/interview-fleet-ops-director-distribution.md, line 25 |
| Distributor, director | trigger | Renewal in March 2027 with a Motive bundling offer on the table | documents/interview-fleet-ops-director-distribution.md, line 37 |
| Distributor, director | workaround | Two smaller depots use outside vendors and a mobile repair service; half the repair spend goes outside | documents/interview-fleet-ops-director-distribution.md, lines 5, 22 |
| Distributor, parts manager | quote | "If it already knows what the code is, why can't it start the work order and pull the parts?" | documents/fault-code-assist-beta-feedback.md, line 21 |
| Waste hauler, maintenance manager | objection | "Too many 'watch' codes. Hide them unless they repeat." | documents/fault-code-assist-beta-feedback.md, line 20 |
| Mid-size fleet, shop supervisor | pain | "Tells me what the code means. I still have to do everything else." | documents/fault-code-assist-beta-feedback.md, line 19 |
| Beta fleets | workaround | 18% of "act now" codes became a work order within 24 hours; no one knows if the rest were false alarms or ignored | documents/fault-code-assist-beta-feedback.md, line 14 |
| Beta fleets | budget signal | 31 of 46 beta customers used it in the last 30 days; 61% thumbs-up | documents/fault-code-assist-beta-feedback.md, lines 12–13 |
| All customers | pain | Telematics and fault codes: 233 tickets (12%), "how do we filter the ones that matter?" | documents/support-tickets-q3-2026.csv, line 5 |
| All customers | pain | PM wrong or overdue when meter readings stop syncing: 349 tickets (18%) | documents/support-tickets-q3-2026.csv, line 2 |
| All customers | pain | Parts counts and receiving: 291 tickets (15%) | documents/support-tickets-q3-2026.csv, line 3 |
| All customers | workaround | Techs pick "Other" as the cause code to close a work order on the tablet: 252 tickets (13%) | documents/support-tickets-q3-2026.csv, line 4 |
| Smaller fleets, buyer | churn reason | 31 of 88 left for a telematics bundle, decided by finance or operations; most under 100 vehicles | documents/churn-note-2026.md, line 15 |
| All customers | churn reason | 14 left over the app: "too many clicks to close a work order" | documents/churn-note-2026.md, line 17 |
| Larger fleets | budget signal | Churn above 150 vehicles was 4%; 3% where parts run in two or more shops | documents/churn-note-2026.md, lines 24–25 |
| Top customers | trigger | 37 customers face a bundled offer at renewal; 9 of the top 50 asked about AI, none has an AI budget line | documents/churn-note-2026.md, lines 30–31 |
| Prospects | trigger | "What does your AI do?" in every second demo; prospects ask why it doesn't open the work order itself | documents/lost-deals-h1-2026.md, line 29 |
| Prospects | objection | Lost 29 deals to Fleetio ("live in a week") and 29 to telematics bundles | documents/lost-deals-h1-2026.md, lines 13–16 |
| Prospects | churn reason | 11 stayed on spreadsheets or made no decision: "our Excel works" | documents/lost-deals-h1-2026.md, line 17 |

## What the product manager knows that the files don't

| Customer type | What | Tag |
|---|---|---|
| Carriers and distributors, 150–500 vehicles | About 140 of the 310 customers with a telematics feed have 150 to 500 vehicles and at least one shop | [PM, illustrative] |
| Lead technicians | They trust their own read of a code more than any list, and resent being pulled off the floor to do it | [PM, illustrative] |
| Directors | The maintenance budget is set once a year with the CFO; new spend outside renewal needs a payback story | [PM, illustrative] |
| Dispatch | Dispatch plans in a separate system; at most customers the shop hears about changes by phone or radio | [PM, illustrative] |
| Independent repair shops | Several customers send overflow work to the same local independent shops, which re-enter the job by hand | [PM, illustrative] |

## Gaps

What we couldn't find in our data, so any persona that needs it marks it `[assumed]`:

- A third interview at a fleet of 150–500 vehicles; we have two.
- Anything from a technician in their own words: every technician fact comes through the manager.
- How dispatch and the shop agree a slot, and what it costs when they don't.
- What an independent repair shop experiences when it takes work from our fleets.
- Who signs above which amount, and what the approval path for a new AI add-on looks like.
