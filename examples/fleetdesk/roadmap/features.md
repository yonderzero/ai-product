# FleetDesk · Features, prioritised

> Fictional example. FleetDesk, its customers and the product manager's answers are invented, tagged `[PM, illustrative]`. The personas are synthetic: what they say is a hypothesis, not evidence.

Features for the flows taken forward in `../flows/flows.md` (the morning shortlist first, then say it, sign it), plus the best ideas from ideation, prioritised. Built on 27 Oct 2026.

## Ideas

Where the features came from: the flows, the opportunities, the Imagine section, what customers and the panel asked for, and ideation with the product manager.

| Idea | From | Flow it serves | Keep? |
|---|---|---|---|
| Read every overnight code, write-up and PM due, and group by truck | flow (shortlist, moment 1) | The morning shortlist | yes |
| Rank trucks by risk with one line of why and the evidence behind it | flow (moments 2, 5); real customers ("the actual codes, not a summary") | The morning shortlist | yes |
| Draft the work order: complaint, likely cause, VMRS code, expected parts | flow (moment 5); `../vision/opportunities.md` #1 | The morning shortlist | yes |
| Approve, edit or reject with a one-line reason; the work order opens with the approver's name | flow (moment 6); panel ("a named person on every action", `../research/panel.md`) | The morning shortlist | yes |
| The lead tech's one-tap strike with preset reasons, that truck only | panel round 1 and 2; real customer (shop supervisor) | The morning shortlist | yes |
| "Watching": nothing hidden, days there, trucks come back when a code repeats | flow (moment 7); panel; real customer (maintenance manager) | The morning shortlist | yes |
| A feed warning when codes or meters stop | flow (when it goes wrong); 18% of tickets are meter sync [documents/support-tickets-q3-2026.csv] | The morning shortlist | yes |
| Parts on the shelf, read only, on each draft | `../research/panel.md` (for the buyer); panel round 2 (Glen) | The morning shortlist | yes |
| A log of every decision, and whether the draft matched what the technician found | flow; `../discovery/discovery.md` ("how we'll know") | Both | yes |
| A noise rule per model, approved by the manager, in a list she can review | panel round 2 (Rosa, Glen, Dwayne); both real customers | The morning shortlist | yes |
| The buyer's weekly card: trucks pulled in, "Watching" trucks that broke down, trucks down at 5 am | panel (Glen, rounds 1 and 2); [documents/interview-fleet-ops-director-distribution.md] ("prove it to the CFO") | The morning shortlist | yes |
| A morning text or email with the shortlist | ideation | The morning shortlist | merge into the shortlist page's morning message |
| Hold to talk: the technician's words to complaint, cause and correction | flow (say it, sign it, moments 2–3); `../vision/opportunities.md` #3 | Say it, sign it | yes |
| The technician confirms his time and signs; the recording stays with the truck; the promise in the customer agreement | flow; real customers (union, "who listens to it?"); panel round 2 | Say it, sign it | yes |
| Suggest the VMRS code from the note | flow (moment 3) | Say it, sign it | yes |
| End-of-shift list of notes the agent couldn't complete | flow (moment 5); panel (Rosa) | Say it, sign it | merge into "hold to talk" |
| Flag parts still under warranty | `../research/experiences.md` #4; `../vision/opportunities.md` #5 | Say it, sign it | yes, later |
| Reserve stock and draft purchase orders within limits | flow 3 (parts, later) | Parts on the bench | yes, later |
| Rebook a missed PM | flow 4 (dispatch slot, later) | A slot that survives dispatch | yes, later |
| Tune the ranking from rejections on its own | ideation | The morning shortlist | yes, later |
| PTO hours for refuse trucks in the ranking | real customer (maintenance manager) | The morning shortlist | yes, later |
| Freeze-frame data in "Why this truck" | real customer (shop supervisor) | The morning shortlist | yes, later |
| The signed note as a page that travels with the truck to an outside shop | panel round 2 (Tess) | Say it, sign it | yes, later |
| Small known jobs approved by rule, without a person | `../vision/vision.md` (level 4) | The morning shortlist | drop for now: no persona or customer would let a work order open without a named person |
| Send overflow jobs to outside shops | flow 5 | Overflow | drop: real customers' outside shops won't use a new tool |
| Message dispatch to ask when a truck is back | flow 4 | A slot that survives dispatch | drop: "they'll never answer a message from a computer" |

## The features, prioritised

| # | Feature | Kind | Flow | Value | Pay | Confidence | Effort | Priority | Horizon |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Read and group overnight signals by truck | agent capability | Shortlist | 4 | 3 | Strong | 1 | 17.5 | Now |
| 2 | Approve, edit or reject with a reason; opens with the approver's name | control | Shortlist | 4 | 3 | Strong | 1 | 17.5 | Now |
| 3 | Feed warning when codes or meters stop | visibility | Shortlist | 3 | 2 | Strong | 1 | 12.5 | Now |
| 4 | Rank trucks with one line of why and the evidence | agent capability | Shortlist | 5 | 4 | Good | 2 | 12.0 | Now |
| 5 | Drafted work order | agent capability | Shortlist | 5 | 4 | Good | 2 | 12.0 | Now |
| 6 | "Watching", with days there and trucks coming back | visibility | Shortlist | 4 | 2 | Good | 1 | 12.0 | Now |
| 7 | Parts on the shelf, read only | visibility | Shortlist | 3 | 3 | Good | 1 | 12.0 | Now |
| 8 | Lead tech's one-tap strike, that truck only | control | Shortlist | 4 | 2 | Good | 1 | 12.0 | Now |
| 9 | Decision log, and whether the draft matched what was found | data | Both | 3 | 2 | Good | 1 | 10.0 | Now |
| 10 | VMRS code from the note | agent capability | Say it, sign it | 3 | 2 | Good | 1 | 10.0 | Next |
| 11 | Hold to talk: words to complaint, cause and correction | agent capability | Say it, sign it | 5 | 3 | Good | 3 | 8.0 | Next |
| 12 | Technician confirms time and signs; recording with the truck; promise in the agreement | control | Say it, sign it | 4 | 2 | Good | 2 | 8.0 | Next |
| 13 | The buyer's weekly card | visibility | Shortlist | 3 | 4 | Good | 3 | 7.0 | Next |
| 14 | Noise rules per model, approved by the manager | control | Shortlist | 3 | 2 | Good | 2 | 6.7 | Next |
| 15 | Flag parts still under warranty | agent capability | Say it, sign it | 4 | 4 | Thin | 3 | 4.0 | Later |
| 16 | Reserve stock and draft purchase orders within limits | agent capability | Parts on the bench | 4 | 4 | Thin | 3 | 4.0 | Later |
| 17 | PTO hours in the ranking | data | Shortlist | 3 | 2 | Thin | 2 | 3.3 | Later |
| 18 | Rebook a missed PM | agent capability | Dispatch slot | 4 | 3 | Thin | 4 | 2.8 | Later |
| 19 | Freeze-frame data in "Why this truck" | data | Shortlist | 3 | 2 | Thin | 3 | 2.5 | Later |
| 20 | Tune the ranking from rejections on its own | agent capability | Shortlist | 4 | 2 | Assumption | 3 | 1.5 | Later |
| 21 | The signed note as a page for outside shops | visibility | Say it, sign it | 2 | 1 | Assumption | 1 | 1.5 | Later |

- **Value:** the hours it gives back and how much customers want it (real customers, then the panel).
- **Pay:** how likely customers pay for it.
- **Confidence:** the evidence grade (Strong 5, Good 4, Thin 2, Assumption 1).
- **Effort:** 1 small, on data we already hold … 5 needs data or rights we don't have. Agreed with the product manager and the engineering lead `[PM, illustrative]`.
- **Priority** = (value + pay) × confidence points ÷ (effort + 1).

**The working:**

- 1: (4 + 3) × 5 ÷ 2 = 17.5. 2: (4 + 3) × 5 ÷ 2 = 17.5. 3: (3 + 2) × 5 ÷ 2 = 12.5.
- 4 and 5: (5 + 4) × 4 ÷ 3 = 12.0. 6: (4 + 2) × 4 ÷ 2 = 12.0. 7: (3 + 3) × 4 ÷ 2 = 12.0. 8: (4 + 2) × 4 ÷ 2 = 12.0.
- 9 and 10: (3 + 2) × 4 ÷ 2 = 10.0. 11: (5 + 3) × 4 ÷ 4 = 8.0. 12: (4 + 2) × 4 ÷ 3 = 8.0. 13: (3 + 4) × 4 ÷ 4 = 7.0. 14: (3 + 2) × 4 ÷ 3 = 6.7.
- 15 and 16: (4 + 4) × 2 ÷ 4 = 4.0. 17: (3 + 2) × 2 ÷ 3 = 3.3. 18: (4 + 3) × 2 ÷ 5 = 2.8. 19: (3 + 2) × 2 ÷ 4 = 2.5. 20: (4 + 2) × 1 ÷ 4 = 1.5. 21: (2 + 1) × 1 ÷ 2 = 1.5.

**Why the horizons don't follow the order exactly:** the VMRS code from the note (10.0) scores above two Now features but needs the note first, so it moves with "Say it, sign it" into Next. The buyer's weekly card is Next because it needs the shortlist's own log to count anything, and trucks down at 5 am aren't recorded today.

**Confidence, explained:** Strong where the evidence is past behaviour across several sources (the morning code list, meter-sync tickets, the named-person rule). Good where it rests on our interviews, the two new real interviews and the beta. Thin where only one source or the panel backs it. Assumption where nothing does.

## This product update

The morning shortlist: the features in Now, the thinnest version in `../flows/flows.md`.

1. Read and group overnight signals by truck.
2. Approve, edit or reject with a one-line reason; the work order opens with the approver's name.
3. A feed warning when codes or meters stop.
4. Rank trucks with one line of why and the evidence.
5. The drafted work order.
6. "Watching", with days there and trucks coming back.
7. Parts on the shelf, read only.
8. The lead tech's one-tap strike, for that truck only.
9. A log of every decision, and whether the draft matched what the technician found.

Priced at $3 per powered vehicle a month as an add-on (`roi.md`).

### The build-day slice

The smallest end-to-end slice of this update that developers can start with, to make the flow real and testable:

- **The flow:** the morning shortlist, from the overnight signals to an approved work order.
- **In:** one pilot fleet's last day of fault codes, driver write-ups and PMs due, read through the public API; grouped by truck; ranked with simple rules (severity from Fault Code Assist's library, repeats, a linked write-up, a PM due); one page with "Pull in today" (three to five trucks, each with one line of why and its raw codes) and "Watching" (everything else); a drafted work order for each pick; "Approve" opens it through the API with the approver's name; "Reject" saves a one-line reason; every decision written to a log.
- **Out (for now):** the lead tech's strike, the parts line, the feed warning, days in "Watching" and trucks coming back, "Plan this week", the morning message, any learning from rejections, more than one fleet.
- **Done when:** on the pilot fleet's real data in a test copy of its FleetDesk account, the page shows three to five trucks with reasons, approving one creates a real work order with the approver's name, rejecting one saves the reason, and the log holds every decision, so the waste hauler's maintenance manager can mark it against the trucks she would have pulled.
- **Design:** follow `../flows/DESIGN.md`; it should look like `../flows/mockups/`.
