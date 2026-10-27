# FleetDesk · The right problem

> Fictional example. FleetDesk, its documents and the product manager's choices are invented, tagged `[PM, illustrative]`. Market sources are real, retrieved on 27 Oct 2026.

Built from `evidence.md`, `framings.md` and the product manager's choices on 27 Oct 2026.

## The BHAG

**By 2029, every truck in a FleetDesk fleet is ready when dispatch needs it: road calls halved against 2026, and no one at a FleetDesk fleet reads a fault code by hand.** `[PM, illustrative]`

## The problem we'll solve

**When** a truck signals it needs work, through a fault code, a driver's defect or a PM coming due, **the maintenance manager wants to** know which trucks need work today and have each job ready to start, with the parts and a slot that fits dispatch, **so they can** keep every truck safe and on the road when dispatch needs it. Today they read hundreds of codes by hand, plan on a whiteboard, chase parts and retype the plan when dispatch changes it. At one carrier, that's the lead technician's first hour every day, and trucks still wait for parts the PM predicted [documents/interview-maintenance-manager-regional-carrier.md] [documents/interview-fleet-ops-director-distribution.md].

- **Framing chosen:** the bigger job, because what customers most want is trucks ready, not codes read, and that job runs through the parts room and bays we already hold. The fault-code moment is where we start learning, because that's where the struggle is sharpest. `[PM, illustrative]`
- **Level:** from 1 today to 4.
- **How it moves us toward the BHAG:** it covers define to conclude for the in-house shop, and capturing what technicians actually found builds the record that prediction, and halving road calls, would need.
- **Evidence:** Good. It's strong on the fault-code struggle, trucks waiting for parts and missed PMs, with past events and workarounds from customers, churn and an outside carrier. It's thin on bay planning and dispatch (`evidence.md`).

## The opportunity

| | |
|---|---|
| **More value for existing customers** | Fleets with their own shops and a telematics feed: fewer road calls, no hand triage, no waiting for parts. They'd pay for trucks ready, as a per-vehicle shop agent, and stay rather than move to a bundle |
| **New customers** | Independent heavy-duty repair shops that serve our fleets, where technician time is what they sell and over half are understaffed (https://www.freightwaves.com/?p=571607, search result). Not sized |
| **Size a year** | $524,000–$1,047,000 new revenue = 812 customers (measured) × about $12,900 a year each (measured, `[PM, illustrative]`) × 20–40% who'd buy (assumption) × 25% price uplift (assumption). Plus $143,000–$286,000 kept from the 37 customers with a bundled offer (`framings.md`) |

## What success looks like

- No one at a pilot fleet reads fault codes by hand each morning, and managers say they trust what was chosen.
- Fewer trucks waiting for parts, and fewer missed PMs, at the same fleets.
- Road calls per million miles going down at those fleets.
- The 37 customers with a bundled offer renew.

## What we need to learn before building

The riskiest assumptions, most dangerous first, each with the questions to ask customers (Mom Test: their life, the past, specifics).

| Assumption | Why it's risky | Questions to ask |
|---|---|---|
| Managers will let something else decide which trucks need work | If they re-check everything, nothing is saved; the beta's users already hide "watch" codes | "Tell me about the last time a code you didn't act on turned into a breakdown. What happened?" · "Walk me through yesterday morning: which codes did you open, and how did you decide?" · "What did you check before you opened the last work order from a code?" |
| What technicians find can be captured on every job | Without it we can't tell good choices from bad, claim warranty or learn | "Walk me through the last work order you closed. What did you write, and why that?" · "When did a warranty claim last get rejected? What was missing?" |
| The real cost is downtime, and the buyer can see it | If downtime isn't counted, a better morning isn't worth paying for | "How did you work out what the last truck that didn't roll cost you? Who saw that number?" · "What did you last spend money on to cut downtime? How did you justify it?" |
| Parts and bays, not just codes, are where trucks wait | If the wait is elsewhere, the bigger framing is wrong | "Think of the last truck that sat in the yard waiting. What was it waiting for, and for how long?" · "When did dispatch last keep a truck out past its PM? What happened next?" |
| The problem is as sharp at fleets of 150–500 vehicles beyond our two interviews | We have two interviews and one segment's tickets | "How many codes did you see yesterday, and how many became work?" · "Who reads them, and what else would they be doing?" |

## Not now

- **The moonshot.** Halving road calls needs prediction across fleets: data rights aren't confirmed and technicians' notes are too thin to learn from (`../discovery/strength.md`). We park it until the notes and rights are in place.
- **Smaller fleets and government fleets.** Smaller fleets buy bundles on price; government fleets are a different sale. Neither now.
- **Outside invoices and warranty** as problems on their own: they stay in the discovery "Grow" bets (`../discovery/discovery.md`) and connect to this job at "conclude".
