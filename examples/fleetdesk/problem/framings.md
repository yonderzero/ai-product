# FleetDesk · Framing the problem

> Fictional example. FleetDesk, its documents and the product manager's answers are invented, tagged `[PM, illustrative]`. Market sources are real, retrieved on 27 Oct 2026; "search result" means seen in search results but not opened.

Built from `../product.md`, `../vision/`, `../discovery/`, `evidence.md` and the product manager's answers on 27 Oct 2026.

## The job

**When** the trucks have reported overnight and the shop opens, **I want to** know which trucks need work today and have that work ready to start, **so I can** keep every truck safe and on the road when dispatch needs it.

- **The struggling moment:** 5:30 am, before coffee: 40 driver write-ups and a few hundred fault codes, "Two of them will be the truck that breaks down on I-70 tonight, and I can't tell which two." [documents/interview-maintenance-manager-regional-carrier.md]
- **Functional:** find the trucks that need work, open the work, get it into the shop before it fails.
- **Emotional:** not to be the one who missed the code before a breakdown; to start the day in control rather than behind.
- **Social:** to be seen by operations and the CFO as the person who keeps the fleet running, not the cost centre that explains road calls.

Asking "why?" behind the task: "read the fault codes" → "find the trucks that will fail" → "keep trucks ready when dispatch needs them". `[PM, illustrative]`

## Pressure test

| Question | Answer | Evidence |
|---|---|---|
| Is it real? | Yes, at every customer with a telematics feed: about 310 of 812. Daily, in the customers' own words, and visible in tickets and churn | `evidence.md`; [documents/fault-code-assist-beta-feedback.md] |
| Does it hurt enough? | An hour a day of a scarce technician at one carrier; a truck down costs more in a day than a year of FleetDesk for that truck. The buyer pays for downtime, and says he'd pay more for less of it | [documents/interview-maintenance-manager-regional-carrier.md] [documents/interview-fleet-ops-director-distribution.md] |
| What do they do today? | Read codes by hand, ignore the "watch" ones, rank trucks with homemade reports, or switch to a telematics bundle | `evidence.md` |
| Why us? | The shop's work order, parts, PM history and 15 years of repairs sit with us; we see codes from Samsara, Motive and Geotab in one place | `../vision/vision.md`, "Why us" |
| Why now? | Motive turns codes into work orders and its agents act on their own; 37 customers face a bundled offer at renewal | https://www.truckinginfo.com/news/motive-adds-ai-agents-for-fleet-operations; [documents/churn-note-2026.md] |

### The four forces

| Force | What we found | Source |
|---|---|---|
| Push | Hundreds of codes a day, most noise; technicians are scarce; road calls are what managers are measured on | [documents/interview-maintenance-manager-regional-carrier.md]; https://fleetmaintenance.com/shop-operations/employees-and-training/article/55261439/techforce-foundation-increases-projected-technician-demand-by-20 |
| Pull | Rivals show work orders created from codes in demos; beta users ask for it | [documents/lost-deals-h1-2026.md] [documents/fault-code-assist-beta-feedback.md] |
| Anxiety | Missing the one code that matters; a machine opening jobs the shop doesn't trust; too many alerts again ("Too many 'watch' codes") | [documents/fault-code-assist-beta-feedback.md] |
| Habit | The morning routine and the whiteboard; the lead tech's experience is trusted more than any list | [documents/interview-maintenance-manager-regional-carrier.md] |

**Switching verdict:** push and pull beat anxiety and habit for fleets with a telematics feed and a busy shop, as the churn to bundles shows. Anxiety is the force to lower: managers need to see why a truck was chosen, and that nothing important was dropped.

### The case against it

Fault-code triage is the part of the job the telematics vendors do best, because the codes are theirs. Solving it puts us in a race on their ground, using their data, and they've already shipped it. The pain we own is what happens after the code: the shop, the parts, the technicians, the outside repairs.

**Our answer:** fair, and it's why we widen the problem. The fault code is only the moment the job starts; what managers want is the truck ready, which runs through our parts room and bays. We start learning at the fault code because that's where the struggle is sharpest, but we frame the problem around the whole job, from first signal to truck back on the road. `[PM, illustrative]`

## Thinking bigger

### The BHAG

**By 2031, every truck in a FleetDesk fleet is ready when dispatch needs it: road calls halved against 2026, and no one at a FleetDesk fleet reads a fault code by hand.** `[PM, illustrative]`

Options we considered:
- "By 2031, no FleetDesk fleet has a breakdown on the road from a failure its own data warned about."
- "By 2030, a maintenance manager's morning takes ten minutes of approvals." Dropped: about the manager's time, not the truck.

The chosen one goes beyond `../vision/vision.md`, which targets level 4 by 2028. Road calls halved needs prediction across fleets, level 5 and above; the vision can be updated later.

### The job map

| Step | What the customer does | Covered by us today? | Our AI level there |
|---|---|---|---|
| Define | Decide which trucks need work today | no | 2 in beta (Fault Code Assist) |
| Locate | Gather codes, defects, PM due dates, the truck's history, its route | partly: defects and PM, not the route | 1 |
| Prepare | Get parts, a bay and a technician ready; agree the slot with dispatch | partly: parts, no bay or dispatch planning | 1 |
| Confirm | Check the truck is in, parts are here, the job is right | no | none |
| Execute | Do the repair | partly: the work order | 1 |
| Monitor | Track jobs in progress and outside repairs | partly | 1 |
| Modify | Reschedule when a truck doesn't come in, a part is missing, or a job grows | no | none |
| Conclude | Record cause and correction, close, claim warranty, learn | partly: records, thin notes, warranty little used | 1 |

FleetDesk covers execute and conclude, as a level 1 product does. Define, prepare, confirm and modify are where the bigger version of the problem sits.

### What customers most want fixed

The biggest pains of current customers, beyond the problem we started with.

| Pain | Who | How big | Evidence |
|---|---|---|---|
| Trucks not ready at 5 am | Director of fleet operations | "A truck down for a day costs me more than FleetDesk costs me for a year for that truck" | [documents/interview-fleet-ops-director-distribution.md] |
| Trucks waiting for parts the PM predicted | Director, parts manager | Recurring at a 180-vehicle distributor | [documents/interview-fleet-ops-director-distribution.md] |
| PMs missed when dispatch keeps a truck out, with nothing rescheduling | Maintenance manager | Meter and PM issues are 18% of tickets | [documents/interview-maintenance-manager-regional-carrier.md] [documents/support-tickets-q3-2026.csv] |
| Outside vendor invoices and overcharges | Director | Half one distributor's repair spend | [documents/interview-fleet-ops-director-distribution.md] |

The biggest is bigger than the problem we picked: customers want trucks ready, not just codes read. `[PM, illustrative]` "I don't need AI that talks to me. I need trucks ready at 5 am." [documents/interview-fleet-ops-director-distribution.md]

### Adjacent segments

Where else this problem is very painful now.

| Segment | Why it hurts there now | How big | Evidence |
|---|---|---|---|
| Independent heavy-duty repair shops serving fleets | Technician time is what they sell; labor runs about $149 an hour and over half are understaffed, so triage and paperwork cost them directly | Fullbay alone serves 5,000+ shops handling $6.5B of service a year | https://www.freightwaves.com/?p=571607 (search result); https://www.motor.com/2026/03/fullbay-acquires-pitstop-to-advance-ai-predictive-maintenance/ |
| Government and municipal fleets | Mixed fleets, small shops, the same technician shortage; vendors serving them shipped AI assistants this year | Not sized; RTA and Collective Data lean to this market | https://worktruckonline.com/news/rta-introduces-ron360-ai-assistant-for-fleet360-users-at-government-fleet-expo-2026 |
| Smaller fleets, under 50 vehicles | Same codes, no lead tech to read them; but they're buying bundles | 99.3% of US carriers run fewer than 100 power units | https://www.truckersnews.com/news/article/15754113/briefly-atas-american-trucking-trends-report-now-available (search result); [documents/churn-note-2026.md] |
| Canadian private fleets | The same work-order and invoice pain; Motive launched maintenance for the US and Canada | Not sized | https://www.samsara.com/ca/blog/sobeys-fleet-maintenance-ai; https://gomotive.com/motive-launches-ai-powered-maintenance-to-help-operations-teams-prevent-breakdowns-increase-uptime-and-lower-repair-costs/ |

`[PM, illustrative]` We could reach independent repair shops that already work on our customers' trucks; the others aren't for now.

## Three framings

| | As stated | The bigger job | The moonshot |
|---|---|---|---|
| **The problem** | Managers read hundreds of fault codes by hand each morning to find the trucks that need work, then type the work orders | Getting every truck that needs work from the first signal (code, defect, PM due) back on the road: chosen, parted, slotted around dispatch, repaired, recorded | The BHAG: every truck ready when dispatch needs it, road calls halved, nobody reads a fault code by hand |
| **For whom** | Maintenance manager, lead technician | Maintenance manager, parts manager, technician; the director as buyer | The director of fleet operations and every shop |
| **Level** | 2 → 4 | 1 → 4 | 1 → 6 |
| **Value from existing customers** | Keeps the customers telematics bundles target | Keeps them, and a paid shop agent across fleets with their own shops | Paid for uptime, not vehicles |
| **New customers or revenue** | Little | Independent repair shops that serve our fleets | Every fleet with a shop, in any segment |
| **Size a year** | $143,000–$286,000 kept = 37 customers with a bundled offer (measured, [documents/churn-note-2026.md]) × about $12,900 a year each (measured, `[PM, illustrative]`) × 30–60% of that churn avoided (assumption) | $524,000–$1,047,000 new = 812 customers (measured) × about $12,900 a year each (measured) × 20–40% who'd buy (assumption) × 25% price uplift (assumption) | Not sized: no measured number links road calls to price |
| **Evidence** | Strong | Good: strong on codes, the parts wait and missed PMs; thin on bays and dispatch | Assumption |
| **Moves us toward the BHAG** | Removes the hand-reading of codes | Covers define to conclude for the in-house shop, the base for prediction | Is the BHAG |
