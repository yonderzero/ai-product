# Salesforce Sales Cloud and Service Cloud · The panel

> Illustrative. Built from public sources; not affiliated with or endorsed by Salesforce. The personas are synthetic and the product manager's choices are invented, tagged `[PM, illustrative]`.

Synthetic personas generate hypotheses. A real customer's yes is evidence; a persona's yes is not. Each persona answered in its own subagent, seeing only its own file and the material being judged, the sceptic first. Run on 27 Oct 2026.

## The roster

| Persona | Role | Segment | How they see the problem | Would pay for | Won't tolerate | Share `[assumed]` |
|---|---|---|---|---|---|---|
| [Priya](personas/p1-priya.md) | VP of sales (buyer) | Mid-market B2B software | "I can't believe the pipeline unless I've chased every rep myself" | Knowing what changed and which deals need her, without asking | A forecast that changes without a reason she can repeat | 6% |
| [Marcus](personas/p2-marcus.md) | Account executive (user) | Mid-market B2B software | "Updating Salesforce is something I do for my manager" | Never typing a stage or date again | His manager hearing about his deal before he does | 0% |
| [Elena](personas/p3-elena.md) | Revenue operations lead (sceptic) | Mid-market B2B software | "Junk data, junk forecast, and I get asked why" | No more bulk resets or "why doesn't this match?" tickets | Changes to opportunity fields without a log | 0% |
| [Sam](personas/p4-sam.md) | Financial advisor (adjacent) | Mid-size RIA | "Every meeting creates follow-up, and I'm liable if it's wrong" | Notes, tasks and the CRM done right after each meeting | A compliance record he hasn't reviewed | 11% |

Across the panel, 117 tagged fields: 47 sourced, 65 `[PM, illustrative]`, 5 `[assumed]` (4%). There are no customer documents in this example, so the product manager's input carries much of each persona; a real run would replace it with interview notes.

## Interview: Marcus, account executive

The product manager asked the Mom Test questions from `../problem/problem.md`. Marcus answered in character, from his record; specific details such as the deal name are invented to fit it.

**Tell me about the last deal that slipped without warning. When did you know?**
"It wasn't without warning, not for me. The logistics deal: the buyer told me on a call their budget was frozen, and I kept it in commit hoping it would thaw. My manager found out at the forecast call at quarter end. I'd known for weeks."

**What was in the record the week before? Why?**
"Commit, the quarter-end close date, and a next step about a month old. My manager asks what closes this quarter, so that's the date I put in. Pulling it meant a conversation I didn't want to have yet."

**What happened to you after it slipped?**
"My manager asked in Slack why the record didn't show it. I got pulled into a deal review, and for a few weeks I got 'where is this deal?' messages on everything I had."

**Tell me about the last time you found a wrong number in the pipeline. How did you find it?**
"It wasn't a wrong number, it was nothing at all. Activity Capture stopped logging after a password reset and nobody told me. I found out when my manager asked why my deal had no activity."

**When a tool logged activity for you, what did you still check by hand?**
"Whether the emails landed on the right deal, and whether it was still connected. Stage, close date and next step I always typed myself. The note-taker pushed summaries, never stages or dates."

**What did you do after you found the mistake?**
"Reconnected it, then pasted the important threads in by hand that evening. Now I glance at the activity timeline before every forecast call. One more thing to check, which was the whole point of not having to."

**Walk me through last week's forecast. Where did your numbers come from?**
"Late Thursday I batch-updated from my notes app and my memory of the calls. Gong had the recordings, but I didn't rewatch any. The close dates are mine, and they're optimistic. My manager messaged me about three deals anyway."

**Would you use something that updated your deals for you?**
"Sure, maybe, if it really saves me clicks. Depends how it works. I'd have to see it."

### Stepping out: feedback on the interview

- **The three questions that got the most useful answers:**
  1. "When did you know?" It surfaced that the rep knew weeks earlier and chose to keep the deal in commit: the riskiest assumption in `../problem/problem.md`, answered against us.
  2. "What was in the record the week before? Why?" It showed why the date was wrong: the manager's question sets the date, not the buyer.
  3. "When a tool logged activity for you, what did you still check by hand?" It showed the trust cost of silent failures: one outage, and he now checks every time.
- **The polite non-answer:** "Would you use something that updated your deals for you?" A future, hypothetical question got "sure, maybe". Drop it from the real interviews.
- **The one you should have asked:** "When you kept that deal in commit, what would have made you pull it earlier?" It tests whether the problem is time or motivation, and what an agent could change about it.

*Synthetic panel: hypotheses, not evidence. Confirm with a real customer.*

## Scoring the three framings

Each persona rated pain (how much it hurts them today) and pay (how likely their organisation pays to fix it), 1 to 5, sceptic first.

| Framing | Elena (sceptic) | Priya (buyer) | Marcus (user) | Sam (adjacent) | Average pain | Average pay | Spread |
|---|---|---|---|---|---|---|---|
| As stated | 3 / 2 | 3 / 2 | 4 / 1 | 2 / 1 | 3.0 | 1.5 | pain 2–4, pay 1–2 |
| **The bigger job** (chosen) | 4 / 3 | 5 / 4 | 2 / 2 | 1 / 1 | 3.0 | 2.5 | pain 1–5, pay 1–4 |
| The moonshot | 2 / 1 | 2 / 1 | 3 / 1 | 3 / 2 | 2.5 | 1.25 | pain 2–3, pay 1–2 |

Each cell is pain / pay. Without the adjacent persona, the bigger job averages 3.7 for pain and 3.0 for pay.

In their words:

- **Elena, the bigger job (4 / 3):** "This is the 'why doesn't this match?' ticket. I'd fund it from the renewal or from what we pay for tools on top. But the VP signs, and I can still block it."
- **Priya, the bigger job (5 / 4):** "This is my week. It would come from my sales tools budget at the February renewal, but only if I can cut a tool on top."
- **Marcus, the bigger job (2 / 2):** "That's my manager's pain, not mine. If it's a manager dashboard built on my deals, I'll quietly undermine it."
- **Sam, the bigger job (1 / 1):** "Nobody chases me for deal updates. My clients chase me when a follow-up never happened."
- **Marcus, as stated (4 / 1):** "Two hours a week of typing for my manager. But I don't sign anything."
- **Priya, the moonshot (2 / 1):** "Nobody on my board is asking about 2031. There's no budget line for selling time."

**Where they disagree:** the bigger job has the widest spread. The buyer and the sceptic feel it most and would pay; the rep, whose typing it depends on, feels it least and says he'd undermine a manager's view of his deals. "As stated" hurts the rep most, but nobody would pay for it. The adjacent persona doesn't recognise the bigger job at all: for advisors the problem is liability for notes, not a forecast.

*Synthetic panel: hypotheses, not evidence. Confirm with a real customer.*

## Reacting to the experiences

Each persona walked through the five experiences in `experiences.md`, sceptic first.

| Experience | Elena (sceptic) | Priya (buyer) | Marcus (user) | Sam (adjacent) |
|---|---|---|---|---|
| 1. The deal record that keeps itself | Helps if field history shows "agent-proposed, rep-confirmed". Stops when reps accept everything in one tap | Helps: no more "scrub before the call". Asks whose agent reads the calls already in Gong | **Backs it first.** Stops the first time it silently stops logging | **Backs it first**, as "the household record that keeps itself". Never links people on its own |
| 2. The forecast call without the chase | Stops the first week the brief and the Forecasts tab show different totals | **Backs it first**, with experience 1's confirm step. Keeps her spreadsheet beside it until the brief proves itself | Never shows his manager a draft of his deal he hasn't seen | Doesn't apply |
| 3. Step in before a deal slips | Needs job-change data we don't hold; won't let it email new contacts | "It's the deal I lost." Never emails or books time with a buyer | Hard line: no flag reaches his manager before him | Barely applies: overdue follow-ups only |
| 4. Pipeline hygiene without the bulk reset | **Backs it first**: it replaces her scheduled reset and nudge flow. Never edits values or her rules | Revenue operations' win, not hers to fund | Fine, until the third nag in a week | Mostly doesn't apply |
| 5. Service signals reach the deal | Only if they run Service Cloud; never changes risk from a case count | Does nothing if support isn't on Service Cloud | Wants to know before his buyer brings it up | Doesn't apply |

**Would the buyer pay about $48,000 a year for the agents?** Priya: not now. The labour saved isn't cash, because she isn't cutting people, and the agents sit on top of Salesforce and a call-recording tool. She'd pay from her sales tools budget at the February renewal if a pilot with one team showed managers stop chasing and the forecast landing within 5%, and only by cutting the call tool at its renewal. (The price for this product update is chosen in `../roadmap/roi.md`.)

**The three changes that would win over the most personas:**

1. **The rep sees and confirms everything first.** No change, flag or summary about a deal reaches the manager before the rep has seen it, and the tool says loudly when it stops capturing (Marcus, Sam, Priya).
2. **One audit log in standard Salesforce reports, and one number.** Every agent action, with who confirmed it and why, reportable in ordinary reports and flows, not a separate store; the brief's totals always match the Forecasts tab (Elena, Priya).
3. **Replace a tool, don't add one.** Read the calls customers already record, and price it as a fixed line at renewal, not unpredictable credits, so it can replace a tool on top rather than add a bill (Priya, Elena, Sam).

These are noted against each experience in `experiences.md`.

*Synthetic panel: hypotheses, not evidence. Confirm with a real customer.*

## What changed, and the best objection

**What changed:** the panel backs the chosen problem from the buyer's and the sceptic's side, but the rep's interview answered the riskiest assumption against us: he knew the deal had slipped and kept it in commit. If real reps say the same, the problem is partly motivation, not typing, and the experiences must make it safe for the rep to share bad news early (rep first, manager second) rather than simply read more of what the rep says.

**The single best objection (Marcus):** "My deals aren't stale because I can't type. Read my calls and show my manager first, and you've built surveillance: reps will stop putting the truth where your agent can see it."

The buyer's objection runs close behind: the truth about her lost deal was on a call recorded in Gong, not in Sales Cloud, so why pay twice to read the same conversation?

`[PM, illustrative]` We'll offer to add a line to `../problem/problem.md` under what to learn before building: test with real reps whether a rep-first flow changes when they share bad news.

*Synthetic panel: hypotheses, not evidence. Confirm with a real customer.*
