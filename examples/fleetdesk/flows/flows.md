# FleetDesk · The right flows

> Fictional example. FleetDesk, its documents, customers and the product manager's answers are invented, tagged `[PM, illustrative]`. The personas are synthetic: what they say is a hypothesis, not evidence.

The flows of the agentic customer experiences in `../research/experiences.md`, tested with real customers and the synthetic panel. Built on 27 Oct 2026. Flows to take forward, not features or a build plan yet.

## The flows, ranked

| # | Flow | Experience | Persona | Level today → with agents | Hours back per customer | Value | Trust | Pay | Real customers | Take forward? |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | The morning shortlist | 1 | Rosa, with Dwayne | 2 → 4 | 300 h a year | 3.5 | 3.0 | 2.75 | agree: both want it; they disagree on when the lead tech strikes | yes, first |
| 2 | Say it, sign it | 4 | Dwayne and the technicians | 1 → 3 | 1,120 h a year | 3.75 | 3.75 | 2.5 | agree, with two changes: the technician confirms his own time; the recording stays with the truck | yes, next |
| 3 | Parts on the bench before the truck | 2 | Parts manager, Glen | 1 → 4 | 350 h a year | 3.0 | 2.75 | 3.0 | agree it's where trucks wait; neither would let it order until counts are right | later |
| 4 | A slot that survives dispatch | 3 | Rosa | 1 → 3 | 175 h a year | 2.75 | 2.0 | 2.0 | disagree: not a problem at a fixed-route hauler; "dispatch won't answer a computer" | later |
| 5 | Overflow to a trusted shop | 5 | Tess, Rosa | 1 → 4 | not counted | 3.25 | 3.25 | 3.0 | disagree: their outside shops won't use a new tool | no, for now |

Value, trust and pay are the panel's averages (1 to 5) across all four personas from `panel-tests.md`: round 2 for flows 1 and 2, round 1 for the others. Tess pulls every fleet-side average down; the three fleet personas alone give the shortlist 4.3 value and 3.3 trust. Hours back are from `../research/experiences.md`. Real customers outweigh the panel: two interviews on 27 Oct 2026 (`../documents/interview-maintenance-manager-waste-hauler-flows.md`, `../documents/interview-shop-supervisor-beverage-distributor-flows.md`). *Synthetic panel: hypotheses, not evidence.*

## 1. The morning shortlist

**Persona:** Rosa, maintenance manager, with Dwayne, lead technician · **Trigger:** the overnight fault codes, driver write-ups and PMs coming due, gathered before the shop opens · **Outcome:** Rosa has the few trucks to pull in today, each with a work order she approved and the reason, Dwayne had his say, and nothing else was dropped out of sight.

### The main path

| # | Moment | The agent | The person | What they see |
|---|---|---|---|---|
| 1 | Overnight read | reads every fault code, driver write-up and PM coming due; groups them by truck; drops exact repeats and codes the fleet marked as noise | nothing | a morning message: "214 fault codes, 31 write-ups, 9 PMs due, from 46 trucks. 4 to pull in today." |
| 2 | Rank | ranks trucks by risk: the code and its severity, how often it repeats, a linked write-up, a PM due, the truck's last repairs, and what similar codes led to before | nothing | nothing yet |
| 3 | The lead tech's say | shows the picks to the lead tech first, on the shop desktop | Dwayne keeps or strikes a pick in one tap, with a preset reason; no typing | the picks with "Keep" and one-tap reasons: "Known sensor glitch on this model", "Already fixed", "Not today" |
| 4 | The shortlist | sends one page before the shop opens: "Pull in today" (three to five trucks), "Plan this week" and "Watching", each truck with one line of why; the feed's status at the top | Rosa opens it; she doesn't wait for Dwayne if he hasn't looked | "Truck 2217: coolant temperature code three nights running, and a driver wrote 'temp gauge high on hills'. PM due in 1,200 miles: do both." |
| 5 | Why this truck | drafts each work order: complaint, likely cause, VMRS code, the parts it expects, whether they're on the shelf, and the evidence behind it | Rosa reviews | the draft beside "Why this truck": the raw codes with times, the write-up, the last three repairs, and the past cases behind the ranking |
| 6 | Approve | opens the approved work orders in FleetDesk with Rosa's name on them, and logs every decision; a job waits for the lead tech's look before it gets a bay | Rosa approves, edits or rejects with a one-line reason | "WO-58114 opened for truck 2217 by Rosa. Parts: 1 thermostat, 1 gasket, on the shelf in the north shop." |
| 7 | Watching | keeps every truck not chosen visible in "Watching", with its reason and its days there, and brings it back to the top if a code repeats or gets worse | Rosa handles what comes back | "Back on your list: truck 1840. Same aftertreatment code, third night." |

### When it goes wrong

| What happens | What the agent does | What the person does |
|---|---|---|
| The telematics feed or meter sync stopped overnight | flags it at the top of the page ("No codes from Samsara since 1:12 am: this list is incomplete") and doesn't guess | Rosa checks the feed or calls the lead tech |
| The agent isn't sure about a truck | puts it in "Plan this week" with "Not sure: check", never in "Watching" | Rosa or Dwayne decides |
| A driver reports a safety defect (brakes, steering, tyres, lights) | always puts it in "Pull in today"; never drops it or moves it to "Watching" | Rosa approves or moves it herself, with her name on it |
| Dwayne strikes a pick that Rosa already approved | holds the job off the bay board and shows both names and reasons | Rosa decides |
| A strike suggests a rule for the whole fleet ("this code is noise on this model") | applies it to that truck only, and sends the rule to Rosa | Rosa approves or declines the rule |
| A truck in "Watching" breaks down | flags it, shows the history it had, and asks for a review of why it was ranked low | Rosa and Dwayne review; the reason tunes the ranking |

- **What the agent does alone:** reads, groups, drops exact repeats, ranks, drafts, keeps "Watching" and brings trucks back.
- **What the person always approves:** opening a work order; striking a pick; moving a safety defect; any new noise rule for the fleet.
- **What the agent never does:** opens a work order without a named person; hides or closes a code or write-up; puts a safety defect in "Watching"; turns one strike into a fleet-wide rule on its own; orders parts; takes a truck off a route.
- **Data it needs:** fault codes and meter readings (about 310 customers stream them from Samsara, Motive or Geotab); driver write-ups from the Driver app; PM schedules and repair history; Fault Code Assist's code library; parts stock, read only [documents/fault-code-assist-beta-feedback.md].
-

## 2. Parts on the bench before the truck

**Persona:** the parts manager, with Glen as buyer and Rosa when a job has to move · **Trigger:** a work order is approved, or a PM comes due within the planning window · **Outcome:** the parts are on the bench when the truck arrives, or the job moves to a day when they will be.

### The main path

| # | Moment | The agent | The person | What they see |
|---|---|---|---|---|
| 1 | What the jobs need | lists the parts each approved job and each PM coming due needs, from the PM kit and the drafted work order | nothing | nothing yet |
| 2 | Check the shelf | checks stock across shops and flags counts that look wrong, such as a receipt with no change in the count | the parts manager handles a flagged count | "North shop shows 4 oil filters; 12 were received yesterday. Count?" |
| 3 | Reserve and move | reserves stock for each job and moves it between shops | nothing | the job shows "Parts reserved" |
| 4 | Order | drafts purchase orders to the usual vendor at the usual price | the parts manager approves orders above the limit he set | "PO-7731 to the usual vendor: 2 brake chambers, $214. Under your $500 limit: sent." |
| 5 | Delivery | tracks the delivery date and warns Rosa if a part won't arrive in time | Rosa moves the job or keeps it | "Turbo actuator for truck 3302 arrives Thursday, after its Tuesday slot. Move the job?" |

### When it goes wrong

| What happens | What the agent does | What the person does |
|---|---|---|
| The count looks wrong | stops ordering that part and asks for a count | the parts manager counts |
| The vendor gives no delivery date | flags the order as unconfirmed | the parts manager calls the vendor |
| The price is up on the vendor's last price | stops and asks | the parts manager approves or picks another usual vendor |
| The same part is ordered twice | blocks the second order against the daily cap | the parts manager checks |

- **What the agent does alone:** reserves stock, moves it between the fleet's own shops, drafts orders under the limit.
- **What the person always approves:** any order above the limit, any price change, any vendor change.
- **What the agent never does:** orders from a new vendor; goes over the daily cap; orders against a count it flagged.
- **Data it needs:** PM kits, inventory across shops, vendor price history and purchase orders (ours); vendors' delivery dates (by email today; not held).
- **What real customers said:** the supervisor wants it most ("It's always parts") and the manager stages PM kits already; both said counts are wrong after every delivery and wouldn't let it order until they're right. [documents/interview-shop-supervisor-beverage-distributor-flows.md] [documents/interview-maintenance-manager-waste-hauler-flows.md]
- **What the panel said:** Glen's top flow on value and pay (5 and 5): "Why am I waiting on filters?" Rosa and Dwayne both stuck on wrong counts: "Shelf says four. Shelf lies." Everyone would let it reserve and move stock; nobody would let it order from a guessed cause. *Hypotheses, not evidence.*

## 3. A slot that survives dispatch

**Persona:** Rosa · **Trigger:** dispatch keeps a truck on a route past its slot, a part is late, or a job grows · **Outcome:** the shop's plan stays true all day, and a missed PM is rebooked the moment it's missed.

### The main path

| # | Moment | The agent | The person | What they see |
|---|---|---|---|---|
| 1 | The day's plan | proposes the plan: trucks, bays, technicians, parts ready | Rosa approves | the shop day as a board, in place of the whiteboard |
| 2 | The truck isn't back | sees the truck isn't where the plan expected and asks dispatch, by message, when it will be | dispatch answers | "Truck 2390 is still 140 miles out. Back by 2 pm?" |
| 3 | Rebook | rebooks the PM at the next slot that fits and fills the gap with the next ready job | Rosa reviews the change | "PM for 2390 moved to Wednesday 7 am. Bay 3 now: truck 2217." |
| 4 | Replan | replans and shows only what changed | Rosa handles conflicts | three changes since 9 am, each with its reason |

### When it goes wrong

| What happens | What the agent does | What the person does |
|---|---|---|
| No dispatch data and no answer | asks again, then leaves the slot open and tells Rosa; never assumes | Rosa calls dispatch |
| An overdue safety item | never pushes it past due; puts it in front of Rosa | Rosa decides |
| Two jobs want the same bay | shows the conflict and both options | Rosa picks |

- **What the agent does alone:** fills an empty slot with the next ready job.
- **What the person always approves:** any change to a truck's route; any overdue safety item; locking a slot.
- **What the agent never does:** takes a truck off a route; moves a safety item past its due date.
- **Data it needs:** the shop plan and PM due dates (ours); live location (we hold meter readings, not live location, today); dispatch's plan (in the dispatch system; not held).
- **What real customers said:** the hauler's routes run on fixed days, so missed PMs aren't her problem; the supervisor says dispatch "will never answer a message from a computer". [documents/interview-maintenance-manager-waste-hauler-flows.md] [documents/interview-shop-supervisor-beverage-distributor-flows.md]
- **What the panel said:** Rosa would value it most (5) if it worked, but nobody trusts it without dispatch's plan and live location, which FleetDesk doesn't hold (trust 2 from all four). *Hypotheses, not evidence.*

## 4. Say it, sign it

**Persona:** Dwayne and the technicians · **Trigger:** a technician finishes a job · **Outcome:** every work order closes with complaint, cause and correction, parts and time, in the technician's words, signed by him.

### The main path

| # | Moment | The agent | The person | What they see |
|---|---|---|---|---|
| 1 | Open the job | shows the job with the complaint already filled from the work order | nothing | the work order on the tablet, complaint filled |
| 2 | Say it | listens while the technician holds the button and says what he found and did | the technician speaks | a big "Hold to talk" button, and his words appearing |
| 3 | The draft | writes cause and correction in his words, matches the parts charged out, shows the time clocked for him to confirm, suggests the VMRS code | nothing yet | complaint, cause, correction, parts and code, each editable; "Clocked on this job: 1.6 h. Confirm?" |
| 4 | Sign it | marks any word it wasn't sure of | the technician reads, fixes, confirms his time and signs | "Sign and close as Dwayne", with the promise: notes and recordings stay with the truck's record, never timesheets or grading |
| 5 | What's left | shows Rosa only the work orders it couldn't complete | Rosa handles them | "2 work orders need you: no cause given." |

### When it goes wrong

| What happens | What the agent does | What the person does |
|---|---|---|
| Shop noise or a word it isn't sure of | highlights the word and asks; never fills it in | the technician fixes it in one tap |
| A part was charged out but not mentioned, or the other way round | asks which is right | the technician answers |
| The technician says nothing about the cause | leaves cause empty and marks the job incomplete; never invents a cause | Rosa follows up |
| The technician's finding differs from the drafted cause | records his finding, not the draft | nothing: this is how the shortlist learns |

- **What the agent does alone:** writes the draft note, matches parts, suggests the code.
- **What the person always approves:** the technician signs every note and confirms his own time.
- **What the agent never does:** closes a work order without his signature; invents a finding; fills time on its own; uses notes or recordings for timesheets or to judge a technician; deletes the recording.
- **Data it needs:** the work order, parts charged out, clock times (ours); the technician's voice (new); warranty terms (ours, little used).
- **What real customers said:** "Notes. The part nobody does." Both want it. The manager: never fill time from the clock ("The union steward would be in my office the same day"); techs would talk at the bench or in the cab, not in the bay. The supervisor: "If my manager can play it back to grade me, the guys won't touch it." Commitment: two technicians will try it once there is a pilot. [documents/interview-maintenance-manager-waste-hauler-flows.md] [documents/interview-shop-supervisor-beverage-distributor-flows.md]
- **What the panel said:** Dwayne's first choice (value 5): "I'll talk for two minutes. Just don't make me type." Trust rose to 3.75 once the promise was on the sign screen and the technician confirms his own time, but Rosa, Glen and Dwayne all said a promise on a screen isn't a policy: it belongs in the customer agreement. Glen wouldn't pay for it alone. *Hypotheses, not evidence.*

## 5. Overflow to a trusted shop

**Persona:** Tess, owner of an independent shop, and Rosa on the fleet's side · **Trigger:** an approved job has no bay or technician in the fleet's shop, or the truck is near another depot · **Outcome:** the job reaches a trusted outside shop complete and pre-approved, and comes back as a proper record.

### The main path

| # | Moment | The agent | The person | What they see |
|---|---|---|---|---|
| 1 | Offer the job | offers it to the fleet's preferred shops with codes, history and an approval limit | Rosa picks or approves the shop | three preferred shops near the truck, with their last jobs for the fleet |
| 2 | The shop gets it | sends the job to Tess by link or into her own shop software | Tess accepts and sets the time | the job, ready to start: codes, history, limit |
| 3 | Estimate | approves an estimate within the limit; asks Rosa above it | Rosa approves above the limit | "Estimate $1,180, limit $1,500: approved." |
| 4 | Invoice | reads the invoice into the work order and checks it against the estimate | the office handles mismatches | "Invoice $1,420 against estimate $1,180: check." |

### When it goes wrong

| What happens | What the agent does | What the person does |
|---|---|---|
| No preferred shop can take it | tells Rosa; never tries a new shop | Rosa phones |
| The estimate is over the limit | stops and asks | Rosa approves or declines |
| The invoice doesn't match the estimate | holds it for the office | the office checks |

- **What the agent does alone:** packages the job and approves within the limit.
- **What the person always approves:** a new shop; anything above the limit.
- **What the agent never does:** sends a job to a shop the fleet hasn't chosen; shows the fleet the shop's margins.
- **Data it needs:** the work order and history (ours); preferred shops and limits (new, set by the fleet); the shop's estimate and invoice (from the shop).
- **What real customers said:** neither would use it as drawn: "The dealer won't log into anything of ours"; "Our mobile mechanic texts photos. He won't use an app." [documents/interview-maintenance-manager-waste-hauler-flows.md] [documents/interview-shop-supervisor-beverage-distributor-flows.md]
- **What the panel said:** Tess's first choice (value 5) if jobs land in her own shop software and the fleet never sees her margins; she'd pay per job she wins, never per seat. Glen likes it for his two smaller depots. Rosa: "Handy on a bad week. Not why I'd renew." *Hypotheses, not evidence.*

## The flows to take forward

**1. The morning shortlist, first.** It tests the riskiest assumption in `../problem/problem.md` (will managers let something else decide which trucks need work?), every other flow starts from a job it picks, both real customers recognised it at once, and one offered a pilot. It gives back fewer hours than the notes, so it has to prove trust, not carry the money.

*The thinnest version that still shows the whole experience:* one pilot fleet's overnight codes, write-ups and PMs due, read through the public API. The agent groups them by truck and ranks them with Fault Code Assist's code library, repeats and the truck's last repairs. The lead tech can strike a pick in one tap. Rosa gets one page before the shop opens: three to five trucks to pull in, each with one line of why, the evidence, a drafted work order and whether its parts are on the shelf (read only). "Approve" opens the work order with her name on it; "Reject" asks for one line of reason. Everything else sits in "Watching" with its days there, and comes back if it repeats. A feed warning sits at the top when codes stop. Every decision is logged. No parts ordering, bays or dispatch.

**2. Say it, sign it, next.** It gives back the most hours (1,120 a year), it's Dwayne's and the supervisor's first choice, and it records what the technician actually found, which is how we'll know whether the shortlist was right.

*The thinnest version:* on work orders opened from the shortlist, the technician holds a button at the bench and says what he found and did. The agent drafts cause and correction in his words, matches the parts charged out and suggests the VMRS code; it asks about any word it isn't sure of; he confirms his own time and signs. The recording stays with the truck's record only. Rosa sees the ones it couldn't complete at the end of the shift. No warranty claims yet.

**Later:** parts on the bench, once counts after receiving can be trusted (the shortlist's read-only parts line comes first); a slot that survives dispatch, once there's a way to see dispatch's plan. **Not for now:** overflow to a trusted shop, because real customers say their outside shops won't use a new tool; if it comes back, it has to land in the shop's own software.

## What changed after the interviews

| Round | Change | Why | Who said so |
|---|---|---|---|
| 1 | The lead tech sees the picks before Rosa and strikes in one tap, with preset reasons, no typing | "Make no a one-tap, no-typing, no-penalty action"; Rosa wanted his say before she reads the list | Dwayne, Rosa (personas) |
| 1 | "Watching" shows each truck's days there and brings it back when a code repeats; "Plan this week" and "Watching" start collapsed; a feed warning at the top | Rosa stops reading a long watch list; Dwayne and Glen stop the first time a "Watching" truck breaks down | Rosa, Dwayne, Glen (personas) |
| 1 | A written promise on the sign screen: notes and recordings stay with the truck's record, never timesheets or grading; the technician confirms his own time | Every fleet persona said "never judge a tech" | Dwayne, Rosa, Glen (personas) |
| 1 | Mockups built for the two flows that led round 1; the others stay as flow maps | Overflow, parts and the dispatch slot scored lower on trust | panel |
| 2 | A strike applies to that truck only; a fleet-wide noise rule needs Rosa's approval | "One tech's tap quietly rewrites the rules for 240 tractors" | Rosa, Glen, Dwayne (personas) |
| 2 | "Why this truck" shows the past cases behind the ranking ("See the 9 trucks") | "7 out of 9 is a small sample. Show the nine." | Dwayne (persona) |
| Real | Rosa doesn't wait for the lead tech; a job she approved waits for his look before it gets a bay | The manager won't wait to open the day; the supervisor won't have a bay tied up | real customers (maintenance manager; shop supervisor) |
| Real | Time is never filled from the clock: the technician confirms it | "The union steward would be in my office the same day" | real customer (maintenance manager) |
| Real | Notes promise to go in the customer agreement, not just on the screen | "If my manager can play it back to grade me, the guys won't touch it"; the panel said the same | real customer (shop supervisor); Rosa, Glen, Dwayne (personas) |
| Real | Overflow to a trusted shop dropped for now | Neither fleet's outside shops would use a new tool | real customers (both) |

Not changed, and why: Glen's weekly "trucks down at 5 am, before and after" for his CFO. It matters for the sale, but it's a report on top of the flows, not part of them; it goes to the roadmap.
