# Milewright · Problem evidence

> Fictional example. Milewright, its documents and the product manager's answers are invented, tagged `[PM, illustrative]`. Market sources are real, retrieved on 27 Oct 2026; "search result" means seen in search results but not opened.

What backs the problem, graded with the Mom Test. Built on 27 Oct 2026.

**The problem as we started:** every morning, maintenance managers and lead technicians read hundreds of fault codes one by one to find the few trucks that need work, then type the work orders themselves (`../discovery/discovery.md`, "Start with").
**Overall grade:** Strong, because there are more than three findings from customers, our own usage data, churn and an outside fleet, including past behaviour and time already spent on workarounds. What's missing: how many codes become work, and what that triage costs at fleets outside our two interviews.

## Past behaviour and spend (strong)

| What happened | Who | How often / how much | Source |
|---|---|---|---|
| The lead tech spends the first hour of each day reading fault codes, looking them up and opening work orders | Lead technician at a 240-tractor carrier | Every morning; "a few hundred" codes and 40 driver write-ups waiting | [documents/interview-maintenance-manager-regional-carrier.md] |
| Customers raised 233 support tickets about fault codes and the telematics feed in one quarter, typically "how do we filter the ones that matter?" | Maintenance managers | 12% of all tickets, Q3 2026 | [documents/support-tickets-q3-2026.csv] |
| Beta users had 5,800 fault codes explained; 18% of "act now" codes became a work order within 24 hours | Maintenance managers and lead techs at 46 fleets | Since May 2026 | [documents/fault-code-assist-beta-feedback.md] |
| Customers left for telematics vendors whose maintenance turns codes into work orders | Buyers at 31 fleets | 31 of 88 customers lost in a year | [documents/churn-note-2026.md] |
| A carrier's VP of maintenance built reports in ServiceNow to rank trucks by alert count and send the worst to the shop, plus a monthly alert review | A real carrier, Genox Transportation, at a TMC panel | Ongoing (2021) | https://www.fleetowner.com/technology/article/21162229/navigating-telematics-complexities-to-boost-fleet-uptime |
| Diagnostics ranked third among fleet maintenance concerns | 400+ TMC fleet members | Fall 2025 survey | https://tmc.trucking.org/blog/tmc-fleet-members-top-maintenance-concerns-shift-considerably-fall-2025-spring-2026 |

## Workarounds today

| Workaround | Who | What it costs them | Source |
|---|---|---|---|
| A person reads every code and looks it up | Lead technician | An hour a day of a technician's time, at a time when technicians are scarce: 46,695 diesel jobs went unfilled in 2022–23 | [documents/interview-maintenance-manager-regional-carrier.md], https://fleetmaintenance.com/shop-operations/employees-and-training/article/55261439/techforce-foundation-increases-projected-technician-demand-by-20 |
| The shop day planned on a whiteboard, then typed in | Maintenance manager | Retyping; plans out of date by noon when dispatch changes them | [documents/interview-maintenance-manager-regional-carrier.md] |
| Custom reports ranking trucks by alert count | VP of maintenance at a real carrier | Building and reviewing reports outside the maintenance system | https://www.fleetowner.com/technology/article/21162229/navigating-telematics-complexities-to-boost-fleet-uptime |
| Hiding or ignoring "watch" codes | Maintenance managers in the beta | Codes ignored that might matter; nobody knows which | [documents/fault-code-assist-beta-feedback.md] |
| Switching to a telematics bundle | Buyers at smaller fleets | Leaving their maintenance system and its history | [documents/churn-note-2026.md] |

## What people say (weak on its own)

| Said | Who | Source |
|---|---|---|
| "If it wrote the work order from the fault code and the tech just checked it, I'd pay for that." | Maintenance manager, 240-tractor carrier | [documents/interview-maintenance-manager-regional-carrier.md] |
| "Don't give me another dashboard. Give me the three trucks I need to pull in today, and why." | Same | [documents/interview-maintenance-manager-regional-carrier.md] |
| "If it already knows what the code is, why can't it start the work order and pull the parts?" | Parts manager, beverage distributor | [documents/fault-code-assist-beta-feedback.md] |
| "I don't need AI that talks to me. I need trucks ready at 5 am." | Director of fleet operations, foodservice distributor | [documents/interview-fleet-ops-director-distribution.md] |
| Prospects ask "What does your AI do?" in every second demo | Prospects, via sales | [documents/lost-deals-h1-2026.md] |
| 57% of repaired trucks went back out with undiagnosed fault codes | A diagnostics vendor's own study, about 2012 | https://www.fleetowner.com/perspectives/trucks-at-work/article/21697920/all-in-one-diagnostics (search result) |

## What we looked for and didn't find

- An independent study of how much time fleets spend triaging fault codes. All figures found were from vendors.
- How many of the codes a person reads lead to a repair, at any fleet. Our own beta can't tell false alarms from codes that were ignored [documents/fault-code-assist-beta-feedback.md].
- Evidence from fleets of 150 to 500 vehicles beyond our two interviews: no third interview yet. `[PM, illustrative]`
- A published cost of a missed fault code that became a breakdown, from a source that doesn't sell software.
