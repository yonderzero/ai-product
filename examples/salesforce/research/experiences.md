# Salesforce Sales Cloud and Service Cloud · Agentic customer experiences

> Illustrative. Built from public sources; not affiliated with or endorsed by Salesforce. The product manager's answers are invented to show how `/ai-product-research` works, tagged `[PM, illustrative]`.

The main customer experiences for solving `../problem/problem.md`, reimagined with agents in and around the product: agents that do the customer's work end to end, with the person setting goals, approving and handling exceptions. Exploration, not a build plan yet: these are the experiences to test with the personas and then with real customers. Built on 27 Oct 2026.

**The problem:** when the quarter is on the line and the forecast call is coming, a sales manager wants to know where every deal really stands and which ones need them, without chasing reps, so they can call the number with confidence and spend their time coaching.
**Where the AI sits:** both. Agents inside today's Sales Cloud workflows (the opportunity, Forecasts, the console), and around it in Slack and the inbox, where reps and managers already answer each other.

## How people use the product today

The work a typical customer's employees do in and around the product, for the ideal customer in `icp.md`: a mid-market B2B software company with 25 account executives, 5 sales managers (4 front-line managers and a VP) and 2 revenue operations people on Sales Cloud. `[PM, illustrative]`

| Persona | What they do, step by step | How often | How long each time | People per customer | Outside the product | Source |
|---|---|---|---|---|---|---|
| Account executive | After a call or email, opens the opportunity, logs the activity, updates stage, amount, close date and next step; checks that activity capture picked up the email | After every customer touch | About 2 hours a week of manual data entry (Gen Z sellers, the only figure broken out) | 25 | Notes app or shadow spreadsheet, then batch updates before the forecast call | https://www.salesforce.com/news/stories/state-of-sales-report-announcement-2026/ · https://www.scratchpad.com/blog/salesforce-issues |
| Account executive | Answers the manager's "where is this deal?" messages and gets records right before the forecast call | Weekly, peaking at quarter end | About 1 hour a week `[PM, illustrative]` | 25 | Slack, email, the call itself | `[PM, illustrative]`; the chase is described at https://www.revopscoop.com/post/salesforce-forecasting |
| Sales manager or VP of sales | Opens the pipeline, spots past-due dates and stale next steps, messages reps one by one, copies the numbers into their own forecast sheet, adjusts by judgement, runs the forecast call | Weekly | About 4 hours a week: about an hour for the roll-up itself, the rest chasing and checking `[PM, illustrative]` | 5 | A personal forecast spreadsheet that moves with them from job to job | https://zapier.com/templates/details/weekly-forecast-rollup · https://www.revopscoop.com/post/salesforce-forecasting |
| Revenue operations or Salesforce admin | Builds and fixes forecast reports, runs clean-ups of past-due close dates, chases missing fields, answers "why doesn't this number match?" | Weekly, plus a clean-up each quarter | About 8 hours a week each `[PM, illustrative]` | 2 | Exports to spreadsheets, data-quality tools, a ticket queue | https://www.revopscoop.com/post/salesforce-forecasting · https://jobs.workable.com/jobs/83139990-02aa-447b-9f68-5d26b90d22f1.md |
| Service rep and service manager | Resolve cases and write notes; when a big customer has a run of escalations, the service manager tells the account team by message, if they think of it | Every case; escalations ad hoc | Service agents spent 39% of their time serving customers in 2024, the rest on admin, meetings and notes | Not counted in the sales numbers below | Slack, email | https://www.cxtoday.com/workforce-engagement-management/salesforce-contact-center-agents-spend-just-39-of-their-time-servicing-customers/ |

## The double cost today

A typical customer pays for the product twice: the licence, and the time their people spend using it. Only the sales workflows tied to the problem are counted.

| | Per year | How we got it |
|---|---|---|
| Licence | $74,880 | 32 Sales Cloud seats (25 reps, 5 managers, 2 revenue operations) `[PM, illustrative]` × $195 a user a month for Core, billed annually (https://www.salesforce.com/sales/pricing/, via `../product.md`) × 12 |
| Labour: reps keeping records and answering the chase | $248,400 | 25 reps × 3 hours a week (2 measured for data entry, 1 `[PM, illustrative]` for the chase) × 46 working weeks `[assumed]` × $72 an hour loaded |
| Labour: managers chasing and rebuilding the forecast | $93,840 | 5 managers × 4 hours a week `[PM, illustrative]` × 46 weeks × $102 an hour loaded |
| Labour: revenue operations on hygiene and reports | $53,728 | 2 people × 8 hours a week `[PM, illustrative]` × 46 weeks × $73 an hour loaded |
| **Total** | **$470,848** | The labour ($395,968) is a bit over five times the licence |

**Loaded hourly cost.** Median pay, May 2025: sales representatives for technical and scientific products $104,920 a year (https://www.bls.gov/ooh/sales/wholesale-and-manufacturing-sales-representatives.htm), sales managers $71.28 an hour (https://www.bls.gov/ooh/management/sales-managers.htm), and computer systems analysts, used as a stand-in for revenue operations and admins, $50.89 an hour (https://www.bls.gov/ooh/computer-and-information-technology/computer-systems-analysts.htm). Wages are 70% of what private employers pay per employee hour, benefits the other 30% (June 2026, https://www.bls.gov/news.release/ecec.nr0.htm), so each wage is divided by 0.70: $104,920 ÷ 2,080 hours ÷ 0.70 = $72; $71.28 ÷ 0.70 = $102; $50.89 ÷ 0.70 = $73. Reps' pay here leaves out commission, so the true cost of their hours is likely higher.

## The experiences at a glance

| # | Experience | Persona | Trigger | Level today → with agents | In or around the product | Why it matters |
|---|---|---|---|---|---|---|
| 1 | The deal record that keeps itself | Account executive | A call, meeting or email with a buyer ends | 2 → 4 | In: the opportunity, with approvals in Slack | Removes the typing and the reason records go stale |
| 2 | The forecast call without the chase | Sales manager or VP of sales | The forecast call is coming | 2 → 4 | In: Forecasts and the pipeline, with a brief in Slack | The job itself: know where every deal stands without asking |
| 3 | Step in before a deal slips | Sales manager, with the rep | A deal starts to look like ones that slip | 1 → 4 | In: the opportunity and the manager's calendar | Covers Modify, the step nothing covers today |
| 4 | Pipeline hygiene without the bulk reset | Revenue operations or admin | Data that breaks the forecast appears | 1 → 4 | In: the platform's rules and reports | Fixes records at the source instead of resetting dates in bulk |
| 5 | Service signals reach the deal | Service manager and account executive | A customer's cases spike or an escalation opens | 2 → 4 | Around: from Service Cloud into the sales deal | The forecast misses what support already knows |

## 1. The deal record that keeps itself

**Persona:** the account executive (`personas/p2-marcus.md`) · **Trigger:** a call, meeting or email thread with a buyer ends · **Outcome:** the opportunity reflects what was said and agreed, and the rep confirmed it without typing it.

| Step | Today | With the agent | The person's part |
|---|---|---|---|
| 1 | Rep finishes a call and moves on; notes sit in a notebook or a recorder | The agent reads the transcript, emails and calendar for that deal | nothing |
| 2 | Later, rep opens the opportunity and logs the activity | The agent logs the activity and links it to the right contacts | nothing |
| 3 | Rep updates stage, amount, close date and next step from memory, often in a batch | The agent proposes changes, each with the sentence or email that justifies it | approves, edits or rejects each change in one tap |
| 4 | Rep checks whether activity capture picked up the email | The agent shows what it couldn't place, such as an email to an unknown contact | handles the exception |
| 5 | Manager finds out about changes at the next forecast call | Approved changes appear in the pipeline straight away, marked as agent-proposed and rep-confirmed | nothing |

- **Data it needs:** call transcripts, email and calendar, the opportunity and its history. We hold the record and captured activity (Einstein Activity Capture, call summaries); transcripts may sit in Gong or another recorder the customer pays for.
- **What the agent decides alone, and what it hands to a person:** alone: logging activity and linking contacts. Handed to the rep: any change to stage, amount, close date or forecast category.
- **What could go wrong, and how the person stays in control:** a wrong close date lands in the commit; the rep stops reading and accepts everything. The rep sees the evidence for each change, nothing reaches the forecast without the rep, and a change history shows who confirmed what.
- **Hours it gives back:** about 1.5 of the 2 hours a week of data entry per rep (half an hour stays for reviewing): 69 hours a year per rep, 1,725 for a typical customer.
- **How we'd know it works:** the share of proposed changes reps accept without editing; past-due close dates on open deals.
- **What the panel said:** the rep and the advisor back this one first. The sceptic wants field history to show "agent-proposed, rep-confirmed" and would stop when reps accept everything in one tap; the rep would stop the first time it silently stops capturing (`panel.md`). *Synthetic panel: hypotheses, not evidence.*

## 2. The forecast call without the chase

**Persona:** the sales manager or VP of sales (`personas/p1-priya.md`) · **Trigger:** the weekly forecast call is coming · **Outcome:** the manager walks in knowing what changed, which deals need them, and a commit with a range and the reasons, without having messaged a single rep.

| Step | Today | With the agent | The person's part |
|---|---|---|---|
| 1 | Manager opens the pipeline and spots past-due dates and old next steps | The agent checks every open deal against what actually happened since last week | nothing |
| 2 | Manager messages reps one by one; reps stop selling to reply | The agent asks the rep only about the gaps it can't fill, in Slack, one question per deal | the rep answers the exceptions |
| 3 | Manager copies numbers into their own forecast sheet | The agent drafts the commit, best case and a range, with the deals that move the number | reviews |
| 4 | Manager adjusts by judgement, privately | The manager overrides any deal and says why; the agent keeps the reason | approves or overrides |
| 5 | Forecast call is a round of updates | The brief lists what changed, the three deals that need the manager, and why | runs a shorter call on the deals that matter |

- **Data it needs:** opportunities and their history, captured activity, the rep-confirmed changes from experience 1, last quarters' forecasts against what closed. All in Sales Cloud today; past forecast accuracy is there if the customer uses Forecasts.
- **What the agent decides alone, and what it hands to a person:** alone: what changed and which deals to flag. Handed to the manager: the commit itself, every override, anything said to the VP or board.
- **What could go wrong, and how the person stays in control:** the brief misses a deal the manager knows is at risk; reps feel watched. The manager can override and the reason is kept; the brief shows its evidence; reps see the same view of their own deals that the manager sees.
- **Hours it gives back:** managers from about 4 hours a week to 1: 138 hours a year each, 690 for a typical customer. Reps from about 1 hour a week answering the chase to a quarter of an hour: 862 hours a year for a typical customer.
- **How we'd know it works:** managers stop messaging reps for updates before the call; the share of teams landing within 5% of their forecast.
- **What the panel said:** the buyer backs this one first, with the rep's confirm step, but would keep her spreadsheet beside it until the brief proves itself and pay only by cutting a tool on top. The sceptic would stop the first week the brief and the Forecasts tab disagree; the rep never wants his manager to see a draft of his deal before he does (`panel.md`). *Synthetic panel: hypotheses, not evidence.*

## 3. Step in before a deal slips

**Persona:** the sales manager, with the rep (`personas/p1-priya.md`, `personas/p2-marcus.md`) · **Trigger:** a deal starts to look like the ones that usually slip: the buyer's champion goes quiet or leaves, security review hasn't started, the next step keeps moving · **Outcome:** the manager and rep agree what to do while there's still time, instead of finding out at quarter end.

| Step | Today | With the agent | The person's part |
|---|---|---|---|
| 1 | Manager notices, if at all, from memory or the forecast call | The agent spots the pattern and the reason, from activity and the team's past deals | nothing |
| 2 | Manager asks the rep in a one-to-one | The agent sends both a short note: what it sees, and two possible plays | the rep reviews |
| 3 | Rep and manager decide what to do | The agent books time if both want it, and drafts the email to a new contact | approves, sends |
| 4 | Nobody checks whether it worked | The agent records the play and whether the deal moved | nothing |

- **Data it needs:** activity, opportunity history, the team's won and lost deals; job changes from outside the CRM, which we don't hold for most customers.
- **What the agent decides alone, and what it hands to a person:** alone: which deals to flag. Handed to people: every play, every email, every meeting.
- **What could go wrong, and how the person stays in control:** too many flags and the manager ignores them; a rep feels second-guessed. Flags are capped per week and the rep sees them first.
- **Hours it gives back:** few. It moves the manager's time from chasing to coaching rather than saving it, so it isn't counted in the economics.
- **How we'd know it works:** deals flagged early that still close in the quarter; managers' time in one-to-ones spent on flagged deals.
- **What the panel said:** the buyer calls it "the deal I lost"; the rep's hard line is that no flag reaches his manager before him; the sceptic notes we don't hold job-change data (`panel.md`). *Synthetic panel: hypotheses, not evidence.*

## 4. Pipeline hygiene without the bulk reset

**Persona:** revenue operations or the Salesforce admin (`personas/p3-elena.md`) · **Trigger:** data that will break the forecast appears: a past-due close date, a deal with no next step, a duplicate opportunity · **Outcome:** each record is fixed by the person who knows the deal, and revenue operations sets the rules instead of doing the clean-up.

| Step | Today | With the agent | The person's part |
|---|---|---|---|
| 1 | Admin runs a report of bad records each week or quarter | The agent watches for the rules revenue operations set | sets the rules |
| 2 | A scheduled job moves every past-due date to the start of the month | The agent asks the owner for the real date, with what it knows from activity | the rep answers |
| 3 | Admin chases owners by email | The agent follows up once and escalates to the manager if needed | handles the exception |
| 4 | Admin explains why the report doesn't match the forecast | The agent keeps a log of what changed, by whom and why | reviews |

- **Data it needs:** the records, validation rules, field history. All in Sales Cloud.
- **What the agent decides alone, and what it hands to a person:** alone: finding problems and asking owners. Handed to people: any change to a deal's value or date; the rules themselves.
- **What could go wrong, and how the person stays in control:** reps get nagged and ignore it; the agent changes records nobody asked it to. It never edits values on its own, and revenue operations can switch any rule off.
- **Hours it gives back:** revenue operations from about 8 hours a week to 2: 276 hours a year each, 552 for a typical customer.
- **How we'd know it works:** past-due close dates on open deals; tickets about forecast numbers that don't match.
- **What the panel said:** the sceptic backs this one first: it replaces her scheduled reset and nudge flow. The buyer sees it as revenue operations' win, not hers to fund; the rep would mute it after the third nag in a week (`panel.md`). *Synthetic panel: hypotheses, not evidence.*

## 5. Service signals reach the deal

**Persona:** the service manager and the account executive · **Trigger:** a customer's cases spike, or an escalation opens on an account with an open deal or a renewal · **Outcome:** the account team and the forecast know what support knows.

| Step | Today | With the agent | The person's part |
|---|---|---|---|
| 1 | Service manager sees a spike in cases, if they look | The agent watches case volume and escalations per account | nothing |
| 2 | Service manager messages the account team, if they think of it | The agent attaches a short summary to the open deal or renewal and tells the owner | the rep reviews |
| 3 | The deal stays in commit until it slips | The agent suggests a change to the deal's risk, with the cases behind it | the rep approves or rejects |

- **Data it needs:** cases in Service Cloud and deals in Sales Cloud for the same account. We hold both when the customer runs both clouds; many run service elsewhere.
- **What the agent decides alone, and what it hands to a person:** alone: the summary and who to tell. Handed to people: any change to the deal.
- **What could go wrong, and how the person stays in control:** a noisy week of cases scares a deal that was fine. The rep decides; the summary shows the cases.
- **Hours it gives back:** few; its value is a forecast that doesn't miss what support knows. Not counted in the economics.
- **How we'd know it works:** deals at accounts with escalations that slip without warning.
- **What the panel said:** everyone said it only matters if support runs on Service Cloud, and nobody would let it change a deal's risk from a case count (`panel.md`). *Synthetic panel: hypotheses, not evidence.*

## The new economics

For a typical customer, today against with agents. Agents are priced as a share of the labour they save, so the customer clearly wins.

| | Today | With agents |
|---|---|---|
| Licence | $74,880 | $74,880 |
| Agents (new) | – | $48,000 |
| Labour using the product | $395,968 | $98,992 |
| **Total for the customer** | **$470,848** | **$221,872** |

- **Labour:** 4 times lower; 3,829 hours a year back across the reps, managers and revenue operations, for selling and coaching.
- **The customer saves:** $248,976 a year, 53%.
- **Our revenue per customer:** from $74,880 to $122,880, 1.6 times.
- **Working:** remaining labour: reps 25 × 0.75 hours a week (half an hour reviewing proposed changes, a quarter of an hour on the agent's questions) × 46 × $72 = $62,100; managers 5 × 1 hour × 46 × $102 = $23,460; revenue operations 2 × 2 hours × 46 × $73 = $13,432. Labour saved: $395,968 − $98,992 = $296,976. Agents priced at 32 users × $125 a user a month × 12 = $48,000, the list price of the Agentforce for Sales add-on today (https://www.salesforce.com/agentforce/pricing/, via `../product.md`), which is about 16% of the labour saved. That list price is a placeholder for the full set of experiences 1, 2 and 4; the price for this product update (experiences 1 and 2) is chosen in `../roadmap/roi.md`: $45 a user a month, a fixed line at renewal. The hours a week left after agents are assumptions `[PM, illustrative]`; the people counts are `[PM, illustrative]`; prices and wages are measured. Experiences 3 and 5 aren't counted.
- **What this leaves out:** what the customer pays Gong, Clari or others today. If the agents replace part of that, the customer saves more; if they don't, the saving stands as above.

`[PM, illustrative]` Would customers pay for agents at that price, for that saving? We think yes for teams that already feel the chase, but only once the acceptance rate in experience 1 is proven. The synthetic buyer said "not now": the hours saved aren't cash unless they replace a tool or a hire, so the agents have to replace what's spent on tools on top (`panel.md`).

## The experience to explore first

**The forecast call without the chase (2), with the rep's confirm step from experience 1 built in**, because it is the chosen problem in the manager's own terms, the manager is the buyer, and the switching verdict in `../problem/framings.md` says anxiety decides it: reps must see and correct every change. Testing the two together tests whether managers believe a record their reps confirmed but didn't type.

It's small enough to prototype end to end: one sales team's sample data (five reps, about fifteen open deals, a few call transcripts and email threads as text, in a Salesforce developer org or plain files). The agent reads each deal and its activity and proposes the current stage, close date and next step, each with its evidence. A rep screen accepts, edits or rejects each change. The manager gets a one-page brief: what changed since last week, the three deals that need them and why, and a commit with a range. The manager overrides one deal with a reason, and the brief updates. No live integrations, no Slack, no learning across customers. Build in what the panel asked for: the rep sees and confirms each change before the manager's brief shows it, every change carries who confirmed it and why, and the brief's commit adds up to the same total as the deals behind it.

**Open questions for real customers:**
- When a deal slipped without warning, did the rep know earlier? (The riskiest assumption in `../problem/problem.md`; the synthetic rep said yes.) Would seeing a flag before their manager make them share bad news sooner?
- What share of agent-proposed changes would a rep accept without editing, and what would make a manager trust them?
- Would the manager drop their own forecast sheet, or keep it beside the brief?
- Would the agents be paid from the sales budget, or from what's spent on Gong or Clari today?
