# Salesforce Sales Cloud and Service Cloud · Interviews about the flows

> Illustrative. Built from public sources; not affiliated with or endorsed by Salesforce. The personas are synthetic; the product manager's choices are invented, tagged `[PM, illustrative]`.

Each round, the personas walk through each flow as themselves, each in its own agent that sees only its own persona file and the material being judged, the sceptic first. Real interviews would sit at the bottom and outweigh the panel. Built on 27 Oct 2026.

## Round 1 · 27 Oct 2026 · the five flows as mapped in `flows.md`

### Elena, revenue operations lead (sceptic)

- **First thing she'd do:** open a sandbox and check whether "agent-proposed, rep-confirmed" is a real field she can report on; for the brief, reconcile its commit deal by deal against the Forecasts tab.
- **Where she'd get stuck:** where the evidence lives (Activity Capture burned her before); how the range is worked out; whether the hygiene rules sit in Setup or in a black box.
- **What she'd let the agent do alone:** log activity and link existing contacts; find broken records and ask owners once.
- **What she'd never let the agent do:** write stage, amount, close date or forecast category without a named rep's click; offer "accept all"; touch the Forecasts tab.
- **What's missing for her job:** a log of who confirmed each change and why, a pause per field, reconciliation to Forecasts, fire counts and a dry run for rules.
- **The moment she'd stop:** reps tap through three cards in two seconds, and the history becomes rubber-stamped noise.
- **In her words:** "Accepted isn't confirmed. If reps tap through in two seconds, your audit trail is just noise."

### Priya, VP of sales (buyer)

- **First thing she'd do:** open the brief the night before and compare its three deals and commit with her spreadsheet.
- **Where she'd get stuck:** reps who don't answer become "no update", which is what her managers chase today; she can't yet repeat how the range is worked out.
- **What she'd let the agent do alone:** check deals, ask reps, flag deals, draft the brief.
- **What she'd never let the agent do:** change a rep's deal, submit the forecast, or send anything to the CEO or board without her.
- **What's missing for her job:** a week-over-week diff with a reason per move; a test against her last missed quarters; acceptance and edit rates by rep.
- **The moment she'd stop:** the commit moves for a reason she can't repeat to the CEO.
- **In her words:** "Tell me which three deals need me and why. If I can't defend the number to the board, it's noise."

### Marcus, account executive (user)

- **First thing he'd do:** open the "3 changes proposed" notification and check the close date; then look at what the brief says about his deals.
- **Where he'd get stuck:** a new review step after every call; a question per deal in chat feels like the chase, automated.
- **What he'd let the agent do alone:** log activity, link contacts, draft proposals.
- **What he'd never let the agent do:** change stage, date or category without him, or show his manager a change first.
- **What's missing for his job:** a preview of his deals as his manager will see them; a loud warning when capture stops.
- **The moment he'd stop:** capture drops out silently and his manager asks why a deal has no activity.
- **In his words:** "If my manager reads my deals before I do, I'm out. Show me the brief first."

### Sam, financial advisor (adjacent)

- **First thing he'd do:** check every proposed task against the transcript line, above all who it's assigned to.
- **Where he'd get stuck:** sales words (stage, commit) don't fit households and meetings; the forecast brief doesn't apply to him.
- **What he'd let the agent do alone:** read the notetaker summary, log the meeting, link known household members.
- **What he'd never let the agent do:** create a books-and-records entry before he's read it; assign a follow-up to a household member by guess.
- **What's missing for his job:** a compliance-ready meeting note, consent status, a task for every promise made.
- **The moment he'd stop:** a follow-up attributed to the wrong person.
- **In his words:** "Show me the sentence behind every task, or I'm retyping it myself. I'm the one liable."

### Scores

Each cell is value / trust / pay.

| Flow | Elena (sceptic) | Priya (buyer) | Marcus (user) | Sam (adjacent) | Average | Spread |
|---|---|---|---|---|---|---|
| 1. The rep confirms the deal | 3 / 2 / 2 | 3 / 3 / 2 | 4 / 3 / 2 | 4 / 3 / 3 | 3.5 / 2.75 / 2.25 | value 3–4, trust 2–3, pay 2–3 |
| 2. The forecast brief without the chase | 3 / 2 / 3 | 5 / 3 / 5 | 3 / 2 / 4 | 1 / 3 / 1 | 3.0 / 2.5 / 3.25 | value 1–5, pay 1–5 |
| 3. Hygiene without the bulk reset | 5 / 3 / 4 | 3 / 4 / 2 | 1 / 3 / 4 | 3 / 4 / 3 | 3.0 / 3.5 / 3.25 | value 1–5 |
| 4. Step in before a deal slips | 2 / 2 / 2 | 3 / 3 / 2 | 2 / 2 / 3 | 2 / 2 / 2 | 2.25 / 2.25 / 2.25 | narrow |
| 5. Service signals reach the deal | 2 / 3 / 2 | 2 / 4 / 1 | 3 / 4 / 3 | 2 / 3 / 1 | 2.25 / 3.5 / 1.75 | narrow |

**Where they disagree:** flow 2 splits the panel most. The buyer scores it 5 for value and pay; the adjacent advisor has no forecast and scores it 1. Hygiene splits by role: Elena's best flow, Marcus's worst ("Elena's cleanup, paid for with my afternoon"). On flow 1, Marcus wants one tap to accept the boring changes; Elena wants no "accept all" at all.

**The three changes that would win over the most personas:**

1. **The rep sees everything first, visibly.** A private preview of how each deal will look in the brief; nothing reaches the manager until the rep has seen it; questions go into the rep's own review list, not a chat (Marcus, Sam, Priya).
2. **One auditable record, and one number.** A report row per change with who confirmed it, when and the evidence; a pause per field; the brief reconciled to the Forecasts tab, with a diff and a reason for every move and the range's method stated (Elena, Priya).
3. **Accepted isn't confirmed, and loud when blind.** The evidence beside each change, no "accept all", a check on fast accepts, and a notice the moment capture stops (Elena, Marcus, Priya).

`[PM, illustrative]` We made all three, in the flows and both mockups.

*Synthetic panel: hypotheses, not evidence. Confirm with a real customer.*

## Round 2 · 27 Oct 2026 · mockups: `mockups/rep-confirm.html`, `mockups/forecast-brief.html`

Flows 1 and 2 only, the ones that changed.

### Elena, revenue operations lead (sceptic)

- **First thing she'd do:** check that the report row's fields (old and new value, evidence, who, when, edited) can be filtered, then try to break the reconciliation by editing the Forecasts tab.
- **Where she'd get stuck:** whether accepting writes straight to the deal and still runs validation rules; reps will learn to beat a fixed "look again" threshold by waiting; one past quarter isn't proof the range is right.
- **The moment she'd stop:** the brief and the Forecasts tab differ while a manager still uses the old brief; or no admin-side alert when capture stops.
- **In her words:** "Matching the Forecasts tab is table stakes. If the tab is junk, you've reconciled junk to junk."

### Priya, VP of sales (buyer)

- **First thing she'd do:** "What changed since last week", then the Forecasts match: "I can repeat that to the CEO."
- **Where she'd get stuck:** a rep who never opens the list leaves a stale deal in commit; she'd like unreviewed drafts visible to her, labelled unconfirmed.
- **The moment she'd stop:** the brief halts the day before the call and leaves her with no number; she wants a fallback brief marked stale.
- **In her words:** "Show me the three deals and the reason for every move. That's the whole job."

### Marcus, account executive (user)

- **First thing he'd do:** open the list, read the close-date row, check the preview before anything reaches Priya.
- **Where he'd get stuck:** still three decisions after every call; the per-rep table ranks his review habits next to his peers'.
- **The moment he'd stop:** his accept rate becomes a scorecard in one-to-ones; or the capture notice doesn't reach his phone.
- **In his words:** "Preview first is the only reason I'd try it. Show me before Priya, and I'll accept most of it."

### Sam, financial advisor (adjacent)

- **First thing he'd do:** the evidence line on each task, and who it's assigned to.
- **Where he'd get stuck:** consent and record-keeping rules aren't shown; the brief doesn't apply to him.
- **The moment he'd stop:** capture quietly drops during a client week and a promise never becomes a task.
- **In his words:** "The audit row with who confirmed and when is what my compliance officer actually wants."

### Scores

| Flow | Elena (sceptic) | Priya (buyer) | Marcus (user) | Sam (adjacent) | Average | Spread |
|---|---|---|---|---|---|---|
| 1. The rep confirms the deal | 3 / 3 / 3 | 4 / 3 / 3 | 4 / 3 / 1 | 4 / 3 / 3 | 3.75 / 3.0 / 2.5 | pay 1–3 |
| 2. The forecast brief without the chase | 4 / 3 / 3 | 5 / 4 / 4 | 3 / 3 / 1 | 1 / 3 / 1 | 3.25 / 3.25 / 2.25 | value 1–5, pay 1–4 |

Trust rose on both flows (flow 1 from 2.75 to 3.0, flow 2 from 2.5 to 3.25), with the biggest gains from the sceptic and the buyer. Pay fell for Marcus and Sam, who both now say plainly it isn't their budget; the buyer's pay stayed high (4) and the sceptic's rose to 3.

**Where they disagree:** the per-rep accept, edit and reject counts. Priya and Elena want them; Marcus fears a scorecard.

**The three changes for the next round:** a fallback brief marked stale when totals disagree (Priya); an admin-side alert when capture stops, and the speed-accept rate by rep in the report (Elena); a clear rule on who sees per-rep counts and for what (Marcus).

### The price vote

The four Van Westendorp questions for this product update (flows 1 and 2, a fixed line per user per month at renewal), each persona in its own agent. Sam answered for flow 1 as it would apply to him, per advisor.

| | Too cheap to trust | A bargain | Getting expensive | Too expensive |
|---|---|---|---|---|
| Elena (sceptic) | $4 | $12 | $30 | $55 |
| Priya (buyer) | $8 | $20 | $45 | $80 |
| Marcus (user) | $5 | $15 | $40 | $75 |
| Sam (adjacent) | $8 | $25 | $55 | $95 |
| Median | $6.50 | $17.50 | $42.50 | $77.50 |

Why, in short: Priya compares the bill with Gong (median about $55,000 a year, https://vendr.com/marketplace/gong) and the Agentforce add-ons; at $45 for 32 users it's "about $17K a year". Elena wants a flat line with no credit surprises. Marcus thinks past $40 his VP would ask what it does that Gong and activity capture don't. Sam compares it with his own notetaker. The choice is in `../roadmap/roi.md`.

*Synthetic vote: hypotheses, not evidence.*

*Synthetic panel: hypotheses, not evidence. Confirm with a real customer.*

## Real customers

**There are no real customer interviews in this public example.** The ranking in `flows.md` rests on the panel and on the evidence gathered earlier. `script.md` is ready for the first real interviews; a real run would add each one here and let it outweigh the panel.

What public first-hand sources say about flows like these (the same sources as `../research/evidence.md`):

| Source | Who | What they say about a similar flow | Same as the panel? |
|---|---|---|---|
| https://help.zoho.com/portal/en/community/topic/how-we-cut-crm-updates-from-20-minutes-down-to-2-our-real-workflow?page=10 | A sales team on Zoho CRM | Built their own voice-note tool that fills CRM fields after each call, cutting per-call updates from 15–20 minutes to about 2 | yes: capture-then-confirm saves real time (flow 1) |
| https://forum.dealerrefresh.com/threads/how-often-do-your-sales-reps-actually-update-the-crm-after-customer-calls.13520/ | Car dealership sales managers | Tie new leads to logging and inspect records daily; one calls automatic call logging the most efficient method they've seen | yes: managers want capture without asking (flows 1 and 2) |
| https://www.kitces.com/blog/artificial-intelligence-ai-meeting-notetakers-note-tools-client-communication-accuracy-domentation/ | Financial advisors | Action items from AI notetakers were 62–87% accurate in one test; the advisor stays liable, so every item is checked | yes: Sam's "show me the sentence behind every task" (flow 1) |
| https://revengine.substack.com/p/automatically-nudging-reps-to-update | A revenue operations writer | A flow that nudges owners about past-due close dates and adds the manager after three reminders | yes: Elena's hygiene flow, and Marcus's dislike of escalation (flow 3) |
| https://customerthink.com/where-did-that-close-date-come-from-and-where-is-it-going-to/ | A sales consultant | Close dates drift outward; suggests a reason for every change and counting how often a date moved | yes: a reason per move in the brief (flow 2) |
| https://cmo2cro.substack.com/p/efficient-effective-forecast-calls | A revenue leader | Emails the forecast dashboard the night before the call; slow deals repeat last week's update | yes: a brief before the call (flow 2) |
| https://news.ycombinator.com/item?id=33135245 | A sales manager at a cybersecurity company | Spends a lot of time chasing reps for the minimum; insists on forecast category because others plan from it | yes: the chase the brief removes (flow 2) |
| https://ideas.salesforce.com/s/idea/a0B8W00000GdVXoUAN/einstein-activity-capture-notification-of-disconnected-account | Salesforce users (search result only) | Ask to be notified when activity capture disconnects | yes: the loud capture notice (flow 1) |

None of these is an interview about our flows. They show the same needs the panel raised, from people who lived them.
