# FleetDesk · Agentic customer experiences

> Fictional example. FleetDesk, its documents, prices and the product manager's answers are invented, tagged `[PM, illustrative]`. Market sources are real, retrieved on 27 Oct 2026; "search result" means seen in search results but not opened.

The main customer experiences for solving `../problem/problem.md`, reimagined with agents in and around the product: agents that do the customer's work end to end, with the person setting goals, approving and handling exceptions. Exploration, not a build plan yet: these are the experiences to test with the personas and then with real customers. Built on 27 Oct 2026.

**The problem:** when a truck signals it needs work, through a fault code, a driver's defect or a PM coming due, the maintenance manager wants to know which trucks need work today and have each job ready to start, with the parts and a slot that fits dispatch, so they can keep every truck safe and on the road when dispatch needs it.
**Where the AI sits:** both. Four experiences are agents inside today's FleetDesk workflows; one is a companion that reaches the independent shops our fleets already use.

## How people use the product today

The work a typical customer's employees do in and around FleetDesk for this job, at the ideal customer in `icp.md`: about 200 vehicles, one or two shops.

| Persona | What they do, step by step | How often | How long each time | People per customer | Outside the product | Source |
|---|---|---|---|---|---|---|
| Lead technician | Opens the overnight code list, reads each code, looks it up, decides if it matters, opens a work order | Every working day | About an hour | 1 | OEM lookup sites, memory | `documents/interview-maintenance-manager-regional-carrier.md` (line 23) |
| Maintenance manager | Reads driver write-ups and the codes the lead tech flags; decides which trucks come in | Every working day | About half an hour `[PM, illustrative]` | 1 | — | `documents/interview-maintenance-manager-regional-carrier.md` (line 11) |
| Maintenance manager | Plans the shop day on a whiteboard, types it into FleetDesk, replans when dispatch moves trucks, finds missed PMs when they're overdue | Every working day, replanned twice before noon | About an hour across the day `[PM, illustrative]` | 1 | Whiteboard, phone and radio with dispatch | `documents/interview-maintenance-manager-regional-carrier.md` (lines 12, 26) |
| Parts manager | Checks parts for the day's jobs and the PMs coming due, orders, chases vendors, receives and fixes counts | Every working day | About two hours `[PM, illustrative]` | 1 | Vendor websites, phone, spreadsheets | `documents/interview-fleet-ops-director-distribution.md` (line 23); `documents/support-tickets-q3-2026.csv` (line 3) |
| Technicians | Type notes, time and part numbers; pick a cause code; close the work order on the tablet | Every job: about 3,400 a year | 20–30 minutes | About 12 | Paper notes, the parts counter | `documents/interview-maintenance-manager-regional-carrier.md` (line 24); `documents/support-tickets-q3-2026.csv` (line 4) |

Not counted here, because they sit outside this problem: the office manager typing outside invoices line by line, and the director's cost-per-mile report in Excel, two days a month (`documents/interview-maintenance-manager-regional-carrier.md`, line 27; `documents/interview-fleet-ops-director-distribution.md`, line 12).

## The double cost today

A typical customer pays for the product twice: the licence, and the time their people spend using it.

| | Per year | How we got it |
|---|---|---|
| Licence | $31,200 | 200 vehicles × $13 (Pro) × 12 months. Price measured [documents/product-one-pager.md]; 200 vehicles is the ideal customer's typical size `[PM, illustrative]` |
| Labour using the product | $132,800 | 2,525 hours a year × the loaded hourly cost of whoever does the work (below) |
| **Total** | **$164,000** | |

**Working.** 250 working days a year `[assumed]`. Loaded cost = wage ÷ 0.70, because wages are 70% of total pay in US private industry (https://www.bls.gov/news.release/ecec.nr0.htm).

| Workflow | Hours a year | Loaded cost an hour | Per year |
|---|---|---|---|
| Lead tech reading codes | 1 h × 250 = 250 | $52: a median $36.50 wage (https://www.freightwaves.com/?p=571607); postings pay up to $42 (https://recruiting.paylocity.com/Recruiting/Jobs/Details/3695081) | $13,000 |
| Manager deciding which trucks come in | 0.5 h × 250 = 125 | $72: $105,000 a year `[PM, illustrative]`; no manager wage source could be opened | $9,000 |
| Manager planning and replanning the day | 1 h × 250 = 250 | $72 | $18,000 |
| Parts manager getting parts in | 2 h × 250 = 500 | $40: a $28 wage `[assumed]` | $20,000 |
| Technicians' notes, time and part numbers | 3,400 jobs × 25 min = 1,400 | $52 | $72,800 |
| **Total** | **2,525** | | **$132,800** |

3,400 jobs a year = about 17 work orders per vehicle a year, from 2 million work orders across 115,000 vehicles [documents/product-one-pager.md] `[PM, illustrative]`, × 200 vehicles. 25 minutes is the middle of the customer's own estimate [documents/interview-maintenance-manager-regional-carrier.md].

The surprise: the labour cost is four times the licence, and most of it sits with the technicians' typing, not the morning code list.

## The experiences at a glance

| # | Experience | Persona | Trigger | Level today → with agents | In or around the product | Why it matters |
|---|---|---|---|---|---|---|
| 1 | The morning shortlist | Rosa, maintenance manager | Overnight codes, write-ups and PMs due | 2 → 4 | In | The sharpest struggle; the riskiest assumption (will she let something else choose?) |
| 2 | Parts on the bench before the truck | Parts manager; Glen as buyer | A job is approved or a PM comes due | 1 → 4 | In | Trucks wait for parts everyone knew were needed |
| 3 | A slot that survives dispatch | Rosa | Dispatch keeps a truck out, or a part or bay falls through | 1 → 3 | In | Missed PMs and a plan out of date by noon |
| 4 | Say it, sign it | Dwayne and the technicians | A technician finishes a job | 1 → 3 | In | The biggest labour cost, and the record that makes every other agent learn |
| 5 | Overflow to a trusted shop | Tess, independent shop owner; Rosa | The fleet's shop has no bay or technician for an approved job | 1 → 4 | Around: a companion for outside shops | Reaches the adjacent segment and gets trucks out when the bays are full |

## 1. The morning shortlist

**Persona:** Rosa, maintenance manager · **Trigger:** overnight fault codes, driver write-ups and PMs coming due · **Outcome:** before the shop opens, Rosa has the few trucks that need work today, each with a drafted work order and the reason, and nothing important was dropped.

| Step | Today | With the agent | The person's part |
|---|---|---|---|
| 1 | Codes and write-ups pile up overnight in FleetDesk | The agent reads every code, defect and PM due, groups them by truck, and drops repeats and known noise | Nothing |
| 2 | The lead tech reads each code and looks it up | The agent ranks trucks by risk, using the code, how often it repeats, linked defects, the truck's history and what similar codes led to | Nothing |
| 3 | Rosa and the lead tech decide which trucks come in | The agent shows a shortlist: "pull in today", "plan this week", "watching", each with one line of why | Rosa reviews |
| 4 | The lead tech types each work order | The agent drafts each work order: complaint, likely cause, VMRS code, parts it expects | Rosa approves, edits or rejects with one tap |
| 5 | Nobody records what wasn't acted on | Everything not chosen stays visible in "watching", and comes back if it repeats or worsens | Rosa handles the exception |

- **Data it needs:** fault codes and meters (we hold them for about 310 customers, from Samsara, Motive and Geotab); defects from the Driver app; PM schedules and repair history (ours); Fault Code Assist's code library (ours) [documents/fault-code-assist-beta-feedback.md].
- **What the agent decides alone, and what it hands to a person:** alone: grouping, dropping duplicates and ranking. To a person: every work order is opened only on Rosa's approval; nothing is closed or ignored without being visible.
- **What could go wrong, and how the person stays in control:** it ranks a dangerous code low. Rosa sees "watching" with the reason for each, can sort it her own way, and every rejection asks for a one-line reason that tunes the ranking. Repeats and rising severity always come back to the top.
- **Hours it gives back:** about 300 a year at a typical customer: the lead tech's 250 drop to about 25 for exceptions; Rosa's 125 drop to about 50 for review. Worth about $17,100.
- **How we'd know it works:** the share of drafted work orders Rosa approves unchanged; how often a truck in "watching" later broke down.
- **What the panel said:** Rosa's first choice; she stops the first time a truck in "watching" breaks down. Dwayne would accept it only with a quick veto, and gives up after two bad calls in a week. Glen: it helps the shop, but the code list isn't why trucks miss 5 am. Tess: not her world (`panel.md`). *Synthetic panel: hypotheses, not evidence.*

## 2. Parts on the bench before the truck

**Persona:** the parts manager, with Glen as buyer · **Trigger:** a work order is approved, or a PM is coming due · **Outcome:** the parts are on the bench when the truck arrives, or the job moves to a day when they will be.

| Step | Today | With the agent | The person's part |
|---|---|---|---|
| 1 | The parts manager checks the day's jobs and PMs coming due by hand | The agent lists the parts each approved job and each PM coming due needs, from the PM kit and the drafted work order | Nothing |
| 2 | He checks the shelf, often wrong after receiving | The agent checks stock across shops and flags counts that look wrong | Parts manager handles the exception |
| 3 | He orders on the vendor's website or by phone | The agent reserves stock, moves it between shops, and drafts purchase orders to the usual vendor at the usual price | Parts manager approves orders above a limit he sets |
| 4 | The truck arrives; the part doesn't | The agent tracks delivery and warns Rosa if a part won't arrive in time, so the job can move | Rosa decides |

- **Data it needs:** PM kits, parts inventory across shops, vendor price history and purchase orders (ours); vendors' delivery dates (by email today; not held).
- **What the agent decides alone, and what it hands to a person:** alone: reserving stock and transfers between shops. To a person: any purchase order above the limit; any vendor or price change.
- **What could go wrong, and how the person stays in control:** it orders against a wrong count, or doubles an order. Limits per order and per day; every order is listed for the parts manager; nothing goes to a new vendor.
- **Hours it gives back:** about 350 a year: the parts manager's 500 drop to about 150 for counts, exceptions and vendors. Worth about $14,000.
- **How we'd know it works:** jobs started on time with all parts; trucks waiting for parts each month.
- **What the panel said:** Glen's first choice: "this is my pain", with a cap per order and per day. Rosa and Dwayne both fear ordering against wrong counts; one phantom part or double order and they stop (`panel.md`). *Synthetic panel: hypotheses, not evidence.*

## 3. A slot that survives dispatch

**Persona:** Rosa · **Trigger:** dispatch keeps a truck on a route past its slot, a part is late, or a job grows · **Outcome:** the shop's plan stays true all day, and a missed PM is rebooked the moment it's missed.

| Step | Today | With the agent | The person's part |
|---|---|---|---|
| 1 | Rosa builds the day on the whiteboard and types it in | The agent proposes the day's plan: trucks, bays, technicians, parts ready | Rosa approves |
| 2 | Dispatch moves a truck; the shop hears by phone | The agent sees the truck isn't where the plan expected (from telematics) and asks dispatch, by message, when it will be back | Dispatch answers |
| 3 | Nobody reschedules the missed PM; it shows up overdue | The agent rebooks the PM at the next slot that fits the truck's route and fills the gap with the next job | Rosa reviews the change |
| 4 | Rosa replans twice before noon | The agent replans and shows only what changed | Rosa handles conflicts |

- **Data it needs:** the shop plan and PM due dates (ours); truck location from telematics (we hold meters, not live location, today); dispatch's plan (in the dispatch system; not held).
- **What the agent decides alone, and what it hands to a person:** alone: filling an empty slot with the next ready job. To a person: any change that takes a truck off a route; any overdue safety item.
- **What could go wrong, and how the person stays in control:** it plans around a route it can't see. Without dispatch data it asks rather than assumes; Rosa sees every move and can lock a slot.
- **Hours it gives back:** about 175 a year: Rosa's 250 drop to about 75. Worth about $12,600.
- **How we'd know it works:** PM compliance; PMs found overdue rather than rebooked.
- **What the panel said:** everyone wants the missed PM rebooked, and nobody believes it without dispatch's plan and live location; Dwayne says dispatch won't answer a machine. The evidence is thin here too (`../problem/evidence.md`, `panel.md`). *Synthetic panel: hypotheses, not evidence.*

## 4. Say it, sign it

**Persona:** Dwayne and the technicians · **Trigger:** a technician finishes a job · **Outcome:** every work order closes with complaint, cause and correction, time and parts, in the technician's words, and warranty-ready.

| Step | Today | With the agent | The person's part |
|---|---|---|---|
| 1 | The technician types notes on the tablet, or writes "replaced" | The technician says what he found and did, while working | Speaks |
| 2 | He looks up part numbers and enters time | The agent writes complaint, cause and correction, matches parts to what was charged out, and fills time from clock-in | Nothing |
| 3 | He picks "Other" as the cause code to close | The agent suggests the VMRS code from what was said | Technician reviews |
| 4 | Warranty isn't checked | The agent flags parts still under warranty and what the claim needs | Parts manager or Rosa handles it |
| 5 | The manager closes thin work orders | The technician signs; the manager sees only the ones the agent couldn't complete | Technician approves |

- **Data it needs:** the work order, parts charged out, clock times, warranty terms (ours, warranty little used); the technician's voice (new).
- **What the agent decides alone, and what it hands to a person:** alone: writing the note and filling codes. To a person: the technician signs every note; nothing is filed as a claim without a person.
- **What could go wrong, and how the person stays in control:** it writes something he didn't say, or the note is used to judge him. He reads and signs; the original recording is kept with the note; notes are for the truck's record, not timesheets `[PM, illustrative]`.
- **Hours it gives back:** about 1,120 a year: from 25 minutes a job to about 5 for review and signing `[assumed]`, across 3,400 jobs. Worth about $58,200.
- **How we'd know it works:** work orders closed with cause and correction; warranty claims rejected for missing information.
- **What the panel said:** Dwayne's first choice, because it fixes "replaced" and "Other"; he stops the day one note is used against a technician. Rosa and Glen worry about shop noise and techs feeling watched. Tess already has AI notes in her shop software (`panel.md`). *Synthetic panel: hypotheses, not evidence.*

## 5. Overflow to a trusted shop

**Persona:** Tess, owner of an independent shop; Rosa on the fleet side · **Trigger:** an approved job has no bay or technician in the fleet's shop, or the truck is near another depot · **Outcome:** the job reaches a trusted outside shop complete and pre-approved, and comes back as a proper record.

| Step | Today | With the agent | The person's part |
|---|---|---|---|
| 1 | Rosa phones local shops for a bay | The agent offers the job to the fleet's preferred shops with codes, history and an approval limit | Rosa picks or approves the shop |
| 2 | Tess re-enters the job and calls for approval | Tess gets the job in her own software or by link, ready to start | Tess accepts and sets the time |
| 3 | Approval by phone, while the truck sits | Estimates within the limit are approved; above it, Rosa gets one question | Rosa approves above the limit |
| 4 | The invoice comes by email and is typed in | The agent reads the invoice into the work order and checks it against the estimate | Office handles mismatches |

- **Data it needs:** the work order and history (ours); preferred shops and limits (new, set by the fleet); the shop's estimate and invoice (from the shop).
- **What the agent decides alone, and what it hands to a person:** alone: packaging the job and approving within the limit. To a person: choosing a new shop; anything above the limit.
- **What could go wrong, and how the person stays in control:** it sends a job to a shop that can't take it, or approves padding. Limits per job, preferred shops only, and every outside invoice checked against the estimate.
- **Hours it gives back:** not counted in the economics below: we have no measure of time spent arranging outside repairs.
- **How we'd know it works:** how soon outside jobs come back after approval; how many shops accept the jobs.
- **What the panel said:** Tess's first choice, if jobs drop into her own software and never show her margins; she'd pay little, after a trial. Glen likes it for his two smaller depots but doubts his outside shops will take a new tool (`panel.md`). *Synthetic panel: hypotheses, not evidence.*

## The new economics

For a typical customer, today against with agents (experiences 1 to 4). Agents are priced as a share of the labour they save, so the customer clearly wins.

| | Today | With agents |
|---|---|---|
| Licence | $31,200 | $31,200 |
| Agents (new) | – | $19,200 |
| Labour using the product | $132,800 | $30,900 |
| **Total for the customer** | **$164,000** | **$81,300** |

- **Labour:** about 4.3 times lower; people get about 1,945 hours a year back, mostly technicians' typing and the lead tech's morning, for fixing trucks and training new technicians.
- **The customer saves:** $82,700 a year, 50%.
- **Our revenue per customer:** from $31,200 to $50,400, about 1.6 times.
- **Working:** remaining labour = lead tech 25 h ($1,300) + Rosa's review 50 h ($3,600) + planning 75 h ($5,400) + parts 150 h ($6,000) + technicians 280 h ($14,600) = 580 h, $30,900. Labour saved = $101,900. Agents at $8 per vehicle a month × 200 vehicles × 12 = $19,200, about 19% of the labour saved `[PM, illustrative]`. Hourly costs and job counts as in "The double cost today"; the remaining hours are assumptions `[assumed]`.

The $8 is the price of the full shop agent, once all four in-shop experiences are live. It was never the price for one experience on its own. The pricing story is settled in `../roadmap/roi.md`: the morning shortlist starts alone at $3 per powered vehicle a month (the add-on the vision proposed to test, and close to the 25% uplift in `../problem/problem.md`), rising to $6 when the notes join and $8 for the full shop agent.

## The experience to explore first

**The morning shortlist**, mapped and tested as a flow in `../flows/flows.md`, because it's where the struggle is sharpest, it tests the riskiest assumption in `../problem/problem.md` (will managers let something else decide which trucks need work?), and every other experience starts from a job it picks. It gives back fewer hours than "Say it, sign it", which carries most of the money; that one should follow, because it also produces the record that tells us whether the shortlist was right.

It's small enough to prototype end to end: one pilot fleet's last day of fault codes, write-ups and PMs due, pulled through the public API. The agent groups them by truck and ranks them with Fault Code Assist's library and the truck's last repairs. It sends Rosa a single page before the shop opens: three to five trucks to pull in, each with one line of why, a drafted work order, and whether its parts are on the shelf (read only, the panel's suggestion for the buyer). "Approve" opens the work order through the API, and "Reject" asks for one line of reason. Everything else sits in "watching". Every decision is logged. No parts, bays or dispatch yet.

**What the panel changed:** a quick veto for the lead tech on every pick, and the parts line on each draft (`panel.md`). No persona said yes to $8 a vehicle before a pilot on their own trucks; for the shortlist alone they put the bargain at $2–$3 (`../roadmap/roi.md`).

**Open questions for real customers:**
- Would you approve a drafted work order without re-reading the codes? What would you need to see?
- When did a code you didn't act on last turn into a breakdown?
- Who would you let veto a job the agent picked: you, the lead tech, both?
- Would you pay for this per vehicle, or only if it comes with the parts and notes?
