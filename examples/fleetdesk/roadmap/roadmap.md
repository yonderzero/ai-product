# FleetDesk · Roadmap

> Fictional example. FleetDesk, its documents, prices and the product manager's answers are invented, tagged `[PM, illustrative]`. Assumptions are tagged `[assumed]`.

From the thinnest version to the BHAG, in three horizons. Outcomes first, features second. Built from `features.md`, `roi.md`, `../flows/flows.md`, `../research/experiences.md`, `../vision/vision.md` and `../problem/problem.md` on 27 Oct 2026.

**The BHAG:** by 2031, every truck in a FleetDesk fleet is ready when dispatch needs it: road calls halved against 2026, and no one at a FleetDesk fleet reads a fault code by hand (`../problem/problem.md`).
**The vision:** level 4, AI Delegated, by the end of 2028 (`../vision/vision.md`).

| | Now | Next | Later |
|---|---|---|---|
| **The outcome for customers** | No one reads the overnight code list by hand; the manager approves a short list of trucks, with the reasons | Every work order closes with cause and correction, in the technician's words | Parts on the bench before the truck, and a plan that survives dispatch |
| **Agentic experiences** | The morning shortlist, thinnest version | Say it, sign it, thinnest version | Parts on the bench; a slot that survives dispatch |
| **Key features** | Read and group; rank with why; drafted work order; approve with a name; the lead tech's strike; "Watching"; feed warning; parts line, read only; decision log | Hold to talk; the technician confirms and signs; VMRS from the note; noise rules approved by the manager; the buyer's weekly card | Warranty flag; reserve stock and draft orders within limits; rebook a missed PM; PTO hours and freeze-frame data in the ranking |
| **AI level** | 3 | 3 | 4 |
| **Hours given back per customer** | About 300 a year | About 1,420 a year | About 1,945 a year |
| **What customers pay for** | Trucks chosen and work orders drafted: $3 per powered vehicle a month | The shortlist and the notes: $6 | The full shop agent: $8 |
| **New agent revenue per customer** | $7,200 a year | $14,400 a year | $19,200 a year |
| **What we must learn first** | Will managers approve drafts without re-reading the codes? Who strikes, and when? Does the lead tech's hour really come back? | Will technicians talk to it in a loud shop? Can we write the notes promise into the agreement? Does the note match what the draft predicted? | Are counts after receiving right? Can we see dispatch's plan? Do our contracts allow learning across fleets? |
| **How we'll know it worked** | Share of drafts approved unchanged; "Watching" trucks that later broke down; minutes the lead tech spends on codes; pilot fleets that pay $3 after the pilot | Work orders closed with cause and correction; warranty claims rejected for missing information; drafts whose likely cause matched the finding | Trucks waiting for parts each month; PMs found overdue rather than rebooked; road calls per million miles |

Hours and revenue per customer are for the ideal customer of about 200 powered vehicles (`roi.md`, `../research/experiences.md`). Across the 93 customers we assume would buy (`roi.md`): about $670,000 a year Now, $1.3M Next and $1.8M Later. The Next and Later prices are the plan, to be set from what the pilots show. `[PM, illustrative]`

## Now

**This product update: the morning shortlist.** One page before the shop opens: three to five trucks to pull in, each with one line of why, the evidence and a drafted work order; the lead tech strikes in one tap; the manager approves with her name; everything else stays in "Watching" and comes back if it gets worse. No parts ordering, bays or dispatch.

It comes first because it tests the riskiest assumption in `../problem/problem.md`, whether managers will let something else decide which trucks need work, and every later flow starts from a job it picks. It proves trust, not money: it gives back about 300 hours and saves a typical customer $9,900 a year after the $7,200 it costs (`roi.md`).

**Start with** the build-day slice in `features.md`: one pilot fleet's real day of codes, write-ups and PMs, ranked onto one page, where "Approve" opens a real work order and every decision is logged. Then the waste hauler replays its own recent codes through the shortlist and marks it against the trucks it would have pulled [documents/interview-maintenance-manager-waste-hauler-flows.md], and the rest of the update fills in around what the pilot shows. The pilot is free; the price starts after it.

## Next

**The notes, and the number for the buyer.** "Say it, sign it" on the work orders the shortlist opened: the technician says what he found, the agent writes cause and correction, he confirms his time and signs. It gives back the most hours (about 1,120 a year) and records what the technician actually found, which tells us whether the shortlist picked the right trucks.

Before it ships, the promise goes into the customer agreement: notes and recordings stay with the truck's record, never timesheets or grading (`../flows/panel-tests.md`). With the notes and the shortlist's log, the buyer's weekly card becomes possible: trucks pulled in, "Watching" trucks that broke down, and trucks down at 5 am, for the CFO. That's what Glen needs before his renewal, with a bundled offer on the table [documents/interview-fleet-ops-director-distribution.md].

## Later

**The bench and the bays, toward level 4.** Parts on the bench before the truck, once counts after receiving can be trusted, so the agent reserves stock and drafts orders within limits the buyer sets. A slot that survives dispatch, once there's a way to see dispatch's plan. Warranty flags from complete notes, the first step toward a share of warranty money recovered (`../discovery/value.md`). Together these are the four in-shop experiences priced at $8 in `../research/experiences.md`, where a typical customer saves $82,700 a year.

**Toward the BHAG.** Halving road calls needs ranking that learns from what codes led to across fleets: level 5. That waits on two things this roadmap builds and one it doesn't: the notes (Next) and the decision log (Now) make the record; legal must confirm that contracts allow learning across customers (`../discovery/discovery.md`, "Don't").

## Not on the roadmap

- **Overflow to a trusted shop.** Real customers' outside shops won't use a new tool. If it comes back, it lands in the shop's own software and is charged per job (`../flows/panel-tests.md`).
- **Messaging dispatch from FleetDesk.** "They'll never answer a message from a computer." The dispatch slot waits for dispatch's data instead.
- **Small known jobs approved by rule, without a person.** No persona or customer would let a work order open without a named person yet.
- **Outside invoices read and checked**, and **cost-per-mile benchmarks.** Still bets in `../discovery/discovery.md` and `../vision/opportunities.md`, but they solve a different problem from this one.
- **Fleets under 75 vehicles and fleets without a telematics feed.** The shortlist needs the codes, and smaller fleets buy bundles on price (`../research/icp.md`).
