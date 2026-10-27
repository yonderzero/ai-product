# Salesforce Sales Cloud and Service Cloud · The right flows

> Illustrative. Built from public sources; not affiliated with or endorsed by Salesforce. The personas are synthetic and the product manager's answers are invented, tagged `[PM, illustrative]`.

The flows of the five agentic customer experiences in `../research/experiences.md`, tested with the synthetic panel in two rounds (`panel-tests.md`). There are no real customer interviews in this public example, so the ranking rests on the panel and the earlier evidence. Built on 27 Oct 2026. Flows to take forward, not features or a build plan yet.

## The flows, ranked

| # | Flow | Experience | Persona | Level today → with agents | Hours back per customer | Value | Trust | Pay | Real customers | Take forward? |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | The rep confirms the deal | 1. The deal record that keeps itself | Marcus, account executive | 2 → 4 | 1,725 a year | 3.75 | 3.0 | 2.5 | not yet | yes |
| 2 | The forecast brief without the chase | 2. The forecast call without the chase (explore first) | Priya, VP of sales | 2 → 4 | 1,552 a year (690 managers, 862 reps) | 3.25 | 3.25 | 2.25 | not yet | yes |
| 3 | Hygiene without the bulk reset | 4. Pipeline hygiene without the bulk reset | Elena, revenue operations | 1 → 4 | 552 a year | 3.0 | 3.5 | 3.25 | not yet | later |
| 4 | Step in before a deal slips | 3. Step in before a deal slips | Sales manager, with the rep | 1 → 4 | few; moves time to coaching | 2.25 | 2.25 | 2.25 | not yet | later |
| 5 | Service signals reach the deal | 5. Service signals reach the deal | Service manager and account executive | 2 → 4 | few | 2.25 | 3.5 | 1.75 | not yet | no |

Value, trust and pay are the panel's averages (1 to 5) from `panel-tests.md`: flows 1 and 2 from round 2, after the changes; flows 3 to 5 from round 1. Hours come from `../research/experiences.md`. Without the adjacent persona, who has no forecast, flow 2 averages 4.0 for value, 3.33 for trust and 2.67 for pay. *Synthetic panel: hypotheses, not evidence.*

**Why this order.** Flows 1 and 2 give back the most hours (3,277 a year for a typical customer together) and are the chosen problem in the buyer's own terms: Priya scored flow 2 at 5 for value and 4 for pay. Flow 3, hygiene, scores higher on trust and pay, but it's revenue operations' win, the buyer won't fund it on its own, and it builds on the same change log as flows 1 and 2, so it comes next. Flow 4 needs data we don't hold (job changes) and every persona doubted its flags. Flow 5 only works when support runs on Service Cloud, and nobody would pay for it from a sales budget.

## 1. The rep confirms the deal

From experience 1, the deal record that keeps itself. Mockup: [`mockups/rep-confirm.html`](mockups/rep-confirm.html).

**Persona:** Marcus, account executive (`../research/personas/p2-marcus.md`) · **Trigger:** a call, meeting or email thread with a buyer ends · **Outcome:** the deal shows what was said and agreed, the rep confirmed it without typing it, and a standard report says "agent-proposed, rep-confirmed".

### The main path

| # | Moment | The agent | The person | What they see |
|---|---|---|---|---|
| 1 | Capture | reads the call summary, the emails and the calendar for this deal; logs the activity and links known contacts | nothing | "Capture is on" |
| 2 | Propose | proposes changes to stage, close date, next step and forecast category, each with the sentence or email behind it | nothing | a notification: "3 changes proposed for Halden Freight. Nothing changes, and nobody else sees it, until you do" |
| 3 | Review | shows one list, the evidence beside each change, no "accept all" | accepts, edits or rejects each change | the review list; changes that move the forecast are marked |
| 4 | You see it first | shows the rep a private preview of how the deal will look in the manager's brief | adds a note for the manager, marks it seen | "Only you can see this preview" |
| 5 | Done | writes the confirmed changes to the deal; adds a row per change to a standard report | nothing | the deal with who confirmed what, and undo |

### When it goes wrong

| What happens | What the agent does | What the person does |
|---|---|---|
| Capture stops (a mailbox disconnects after a password change) | stops proposing from email and says so at once, in the product and as a notification | reconnects |
| The rep accepts forecast-moving changes in a few seconds | asks the rep to look again at the one with the most impact | confirms or changes it |
| An email comes from someone it can't match to a contact | flags it as "couldn't place"; doesn't guess | links it or ignores it |
| A date or owner is vague ("early next year", "you or your colleague") | leaves the field blank and asks one question | answers or skips |

- **What the agent does alone:** reads activity, logs it, links known contacts, drafts proposals.
- **What the person always approves:** any change to stage, amount, close date, next step or forecast category.
- **What the agent never does:** changes a deal without the rep; shows the manager anything about a deal before the rep has seen it; guesses who a contact or a follow-up belongs to.
- **Data it needs:** call summaries or transcripts, email and calendar from activity capture, the deal and its field history; validation rules still apply to every write.
- **What real customers said:** no real interviews in this public example. See `panel-tests.md` for what public first-hand sources say about similar flows.
- **What the panel said:** the rep-first preview is the reason Marcus would try it; Elena and Priya want the speed-accept rate by rep and an admin-side alert when capture stops; Sam, the adjacent advisor, wants the same gate on tasks and notes. *Hypotheses, not evidence.*

## 2. The forecast brief without the chase

From experience 2, the forecast call without the chase: the experience to explore first. Mockup: [`mockups/forecast-brief.html`](mockups/forecast-brief.html).

**Persona:** Priya, VP of sales (`../research/personas/p1-priya.md`) · **Trigger:** the weekly forecast call is coming · **Outcome:** the manager walks in knowing what changed and why, which three deals need them, and a commit with a range that matches the Forecasts tab, without having messaged a single rep.

### The main path

| # | Moment | The agent | The person | What they see |
|---|---|---|---|---|
| 1 | Check | checks every open deal against what happened since last week, using only changes reps have confirmed (flow 1) | nothing | nothing yet |
| 2 | Ask | puts a question about each gap it can't fill into the rep's own review list | the rep answers | one question per gap, in the rep's list |
| 3 | What changed | drafts the week-over-week change in commit and best case, with a reason and who confirmed it for every move | reviews | "Commit down $84K, for one reason" |
| 4 | Deals that need you | picks the three deals that need the manager, with the evidence | reviews | three cards |
| 5 | The number | drafts the commit, best case and likely range; checks the commit against the Forecasts tab; states how the range is worked out and what it said last quarter | reviews | "Matches the Forecasts tab ✓" and the deals behind it |
| 6 | Override | records the override and its reason, and updates the commit; the rep sees the change and the reason | overrides any deal and says why | an override box; the new commit |
| 7 | The call | nothing | runs a shorter call on the three deals, and submits the forecast | the same brief |

### When it goes wrong

| What happens | What the agent does | What the person does |
|---|---|---|
| The brief and the Forecasts tab stop matching (someone edits a deal after the brief) | stops, shows what changed and who changed it, keeps the last brief clearly marked out of date | refreshes, or asks the rep |
| A rep hasn't reviewed a proposed change | leaves it out of the brief and says so; the manager can't see the draft | asks the rep in the call |
| A rep doesn't answer a question | marks the deal "no update" with the last evidence, visible to the manager only; doesn't guess | decides |

- **What the agent does alone:** checks deals, asks reps about gaps, flags deals, drafts the brief.
- **What the person always approves:** the commit; every override; anything sent to the CEO or the board.
- **What the agent never does:** changes a rep's deal; edits the Forecasts tab; submits the forecast; shows a draft the rep hasn't seen.
- **Data it needs:** opportunities and their history, the rep-confirmed changes from flow 1, Forecasts totals and categories, the team's past forecasts against what closed.
- **What real customers said:** no real interviews yet.
- **What the panel said:** Priya can repeat "what changed, and why" to the CEO, and would pay from her tools budget if she can drop her spreadsheet; she wants a fallback brief marked stale rather than none. Elena notes that matching the Forecasts tab proves agreement, not truth. Marcus fears the per-rep table becoming a scorecard. *Hypotheses, not evidence.*

## 3. Hygiene without the bulk reset

From experience 4. No mockup yet: it isn't taken forward in this round.

**Persona:** Elena, revenue operations lead (`../research/personas/p3-elena.md`) · **Trigger:** a record breaks a rule she set: a past-due close date, no next step, a likely duplicate · **Outcome:** the person who knows the deal fixes it, and revenue operations sets rules instead of cleaning up.

### The main path

| # | Moment | The agent | The person | What they see |
|---|---|---|---|---|
| 1 | Rules | nothing | revenue operations sets the rules, with a dry run | a rules page in Setup, with how often each rule would fire |
| 2 | Watch | finds records that break a rule | nothing | nothing yet |
| 3 | Ask | adds a question to the owner's review list, with what it knows from activity | the rep answers | one question per record |
| 4 | Follow up | follows up once, then adds it to a short list for the manager | the manager handles it | a short list |
| 5 | Log | logs what changed, by whom and why, in the same report as flow 1 | revenue operations reviews | a standard report |

### When it goes wrong

| What happens | What the agent does | What the person does |
|---|---|---|
| A rule would fire on hundreds of records at once | stops and asks before sending | revenue operations narrows the rule |
| A rep ignores the question | one follow-up, then the manager's list | the manager decides |
| A likely duplicate isn't clear | flags it to revenue operations | merges or keeps |

- **What the agent does alone:** finds problems, asks owners, follows up once.
- **What the person always approves:** any change to a deal's value or date; the rules themselves.
- **What the agent never does:** edits values or dates on its own; merges records; changes a rule.
- **Data it needs:** the records, validation rules, field history. All in Sales Cloud.
- **What the panel said:** Elena's own flow (value 5, pay 4); Marcus calls it "Elena's cleanup, paid for with my afternoon"; Priya would hand it to revenue operations. *Hypotheses, not evidence.*

## 4. Step in before a deal slips

From experience 3. No mockup yet.

**Persona:** the sales manager, with the rep (`../research/personas/p1-priya.md`, `../research/personas/p2-marcus.md`) · **Trigger:** a deal starts to look like ones that usually slip: the champion goes quiet, security review hasn't started, the next step keeps moving · **Outcome:** the rep and manager agree what to do while there's still time.

### The main path

| # | Moment | The agent | The person | What they see |
|---|---|---|---|---|
| 1 | Spot | spots the pattern and the reason, from activity and the team's past deals | nothing | nothing yet |
| 2 | Tell the rep | sends the rep a short note: what it sees, and two possible plays | the rep reviews, adds context, or says "I know, I'm on it" | a flag on the deal, rep only |
| 3 | Tell the manager | passes the flag and the rep's context to the manager | the manager and rep decide | the flag with the rep's view |
| 4 | Act | drafts an email to a new contact; books time if both want it | approve and send | a draft email; a meeting invite |
| 5 | Learn | records the play and whether the deal moved | nothing | the play on the deal's history |

### When it goes wrong

| What happens | What the agent does | What the person does |
|---|---|---|
| Too many flags | caps them per manager and shows how often past flags were right | ignores the rest |
| It needs a job change it can't see | says so | checks |

- **What the agent does alone:** spots and flags deals to the rep.
- **What the person always approves:** every play, every email, every meeting.
- **What the agent never does:** emails or books time with a buyer on its own; flags a deal to the manager before the rep; writes a risk score into a deal field.
- **Data it needs:** activity, deal history, the team's won and lost deals; job changes from outside the CRM, which we don't hold for most customers.
- **What the panel said:** Priya: "My last slip wasn't a pattern. The rep knew." Elena wants the hit rate on their own deals before it flags anyone. *Hypotheses, not evidence.*

## 5. Service signals reach the deal

From experience 5. No mockup.

**Persona:** the service manager and the account executive · **Trigger:** a customer's cases spike, or an escalation opens on an account with an open deal or renewal · **Outcome:** the account team knows what support knows.

### The main path

| # | Moment | The agent | The person | What they see |
|---|---|---|---|---|
| 1 | Watch | watches case volume and escalations per account | nothing | nothing yet |
| 2 | Summarise | attaches a short note to the open deal and tells the owner | the rep reviews | a note on the deal |
| 3 | Suggest | suggests a change to the deal's risk, with the cases behind it | the rep approves or rejects | the suggestion and the cases |

### When it goes wrong

| What happens | What the agent does | What the person does |
|---|---|---|
| A noisy week of cases | shows the trend against normal | decides |
| Support isn't on Service Cloud | does nothing, and says why | nothing |

- **What the agent does alone:** the note and who to tell.
- **What the person always approves:** any change to the deal.
- **What the agent never does:** changes risk from a case count; contacts the customer.
- **Data it needs:** cases in Service Cloud and deals in Sales Cloud for the same account.
- **What the panel said:** "Case count isn't churn risk" (Elena); "I'm not buying Service Cloud to get one summary on a deal" (Priya). *Hypotheses, not evidence.*

## The flows to take forward

**Flows 1 and 2, together, as one experience:** the rep confirms the deal, and the manager's brief is built only from what reps confirmed. This is the experience to explore first in `../research/experiences.md` (the forecast call without the chase, with the rep's confirm step built in). Together they give back about 3,277 hours a year for a typical customer, they're the chosen problem in the buyer's own terms, and they test the riskiest assumption in `../problem/problem.md`: whether managers believe a record their reps confirmed but didn't type.

**The thinnest version that still shows the whole experience end to end:** one sales team (five reps, fifteen open deals, a few call summaries and email threads as text). The agent proposes stage, close date, next step and forecast category for each deal with its evidence; each rep reviews one list and sees a private preview; the manager's brief shows only confirmed changes, what changed and why, the three deals that need them, and a commit that adds up to the deals behind it; the manager overrides one deal with a reason. No Slack, no live integrations, no calls from other recorders, no learning across customers.

**Later:** hygiene (flow 3), once the change log exists; slipping deals (flow 4), once flags can show a hit rate on the customer's own deals. **Not now:** service signals (flow 5).

## What changed after the interviews

| Round | Change | Why | Who said so |
|---|---|---|---|
| 1 → 2 | The rep sees everything first: a private preview of their deal as the manager will see it; nothing reaches the brief until they have; questions go into the rep's own review list instead of a chat | "If my manager reads my deals before I do, I'm out"; the one-question-per-deal chat felt like the chase, automated | Marcus, Sam, Priya (personas) |
| 1 → 2 | One auditable record: a report row per change (old and new value, evidence, who confirmed it, when, edited or not), a pause per field, accept, edit and reject counts per rep, a week-over-week diff with a reason per move, the range's method and last quarter's result, and a stop when the brief and the Forecasts tab disagree | "If I can't reproduce the commit from the underlying deals, I'm not defending it"; Priya must repeat every move to the CEO | Elena, Priya (personas) |
| 1 → 2 | Accepted isn't confirmed: one list with the evidence beside each change, no "accept all", a "look again" check on fast accepts of forecast-moving changes, and a loud notice the moment capture stops | "Accepted isn't confirmed"; Marcus was burned by capture stopping silently | Elena, Marcus (personas) |
| After 2 | Open for the next round: a fallback brief marked stale instead of none when the totals disagree; an admin-side alert when capture stops; who sees the per-rep counts, and for what | Raised in round 2 | Priya, Elena, Marcus (personas) |

`[PM, illustrative]` We kept "no accept all" against Marcus's wish for one tap: the sceptic and the buyer both said a rubber-stamped log is worse than none.
