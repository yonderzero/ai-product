# FleetDesk · The panel

> Fictional example. FleetDesk, its documents and the product manager's answers are invented, tagged `[PM, illustrative]`. The personas are synthetic and not real people. What they say is a hypothesis to test with real customers, never evidence.

Every conversation with the personas, newest at the bottom. Built on 27 Oct 2026. Each persona answered in its own agent, with only its own file and the material being judged; the sceptic went first.

## The roster

| Name | Role | Segment | How they see the problem | Would pay for | Won't tolerate | Share `[assumed]` |
|---|---|---|---|---|---|---|
| [Glen](personas/p1-glen.md) | Director of fleet operations · buyer | Foodservice distributor, 180 vehicles | Trucks not ready at 5 am; waiting on parts everyone knew were needed | Fewer trucks down, with a number for the CFO | Another login or dashboard | 6% |
| [Rosa](personas/p2-rosa.md) | Maintenance manager · user | Regional LTL carrier, 240 tractors | A pile of signals with two real problems hidden in it | A work order written from the code that the tech only checks | Another dashboard | 4% |
| [Dwayne](personas/p3-dwayne.md) | Lead technician · sceptic | Same carrier, north shop | Reading codes isn't the job; fixing trucks is | (not his money) staying on the floor | A machine's call with his name on it | 4% |
| [Tess](personas/p4-tess.md) | Owner, independent heavy-duty shop · adjacent | Independent shop, 5 technicians | Fleet jobs arrive thin and wait on approval | Complete, pre-approved jobs, paid faster | A fleet's system setting her prices | 14% |

Across the panel: 117 fields, 8 `[assumed]` (7%), under the one-third limit. The thinnest is Dwayne: no technician speaks in our documents, so he leans on `[PM, illustrative]`.

### Reality check

The product manager read each persona and said what they'd never say or do. Fixes applied, tagged `[PM, illustrative]`:

- Glen would never buy without a reference call from another distributor: "how they buy" updated.
- Dwayne would never type in the bay with gloves on; he types at the shared desktop at the end of the shift: "workarounds" updated.
- Rosa and Tess: no changes.

No calibration yet: `documents/` has two interview summaries but no verbatim question-and-answer to hold back. The next real interview transcript should be used to calibrate Rosa.

## 1. Interview: Rosa, maintenance manager

The product manager asked the Mom Test questions from `../problem/problem.md`. Rosa answered in character from her record.

**PM:** Walk me through yesterday morning. Which codes did you open, and how did you decide?
**Rosa:** I got in before six. The overnight list had a few hundred codes and about forty write-ups. My lead tech took the codes, like every day. I took the write-ups. He flagged maybe a dozen trucks. We looked at three properly: a coolant temperature code that had come back three nights running, an aftertreatment code on a truck due a PM anyway, and an air pressure write-up from a driver. Everything else we left.

**PM:** Tell me about the last time a code you didn't act on turned into a breakdown. What happened?
**Rosa:** Back in the summer. A tractor threw a low-severity code a few times over a week. Nobody pulled it in, because it looked like the usual noise. It derated on the interstate on a Thursday night. Tow, a rental tractor, a late load. I had to explain the road call on Monday. When we looked back, the code had been telling us.

**PM:** What did you check before you opened the last work order from a code?
**Rosa:** Whether it repeated. The truck's last few work orders. Whether it had a PM coming up, so we could do both at once. And my lead tech's gut. Honestly, his gut is most of it.

**PM:** Think of the last truck that sat in the yard waiting. What was it waiting for, and for how long?
**Rosa:** A turbo actuator, last month. We knew it needed one. The part wasn't in either shop, and the vendor took until the next afternoon. Before that it was a set of filters for a PM. That one shouldn't happen.

**PM:** When did dispatch last keep a truck out past its PM? What happened next?
**Rosa:** Two weeks ago. It was on the whiteboard for Tuesday. Dispatch kept it on a run. Nobody moved the PM. We found it overdue on Friday, in the overdue list.

**PM:** How many codes did you see yesterday, and how many became work?
**Rosa:** A few hundred codes. Three or four work orders came out of them. I couldn't tell you the exact number. Nobody counts.

**PM:** Would you use something that picked the trucks for you?
**Rosa:** Maybe. It depends what it picks. If it shows me why, I'd look at it. The beta's fine on the bad days.

**PM:** How did you work out what the last truck that didn't roll cost you? Who saw that number?
**Rosa:** I didn't, really. The tow bill and the rental went to accounts. Operations knew the load was late. Nobody put it together in one number. The CFO sees cost per mile once a month.

*End interview.*

**Stepping out: feedback on the interview**

- **The three questions that got the most useful answers:**
  1. "Tell me about the last time a code you didn't act on turned into a breakdown": a real incident, a repeat code nobody acted on, and its cost (tow, rental, a late load).
  2. "Think of the last truck that sat in the yard waiting": parts, twice, and one the PM predicted. This supports the bigger job.
  3. "What did you check before you opened the last work order?": the real decision rule: repeats, history, PM due, the lead tech's gut. That's the shortlist's ranking.
- **The polite non-answer:** "Would you use something that picked the trucks for you?" got "maybe, it depends". It's a future question, so it got a future answer. Drop it.
- **The one you should have asked:** "On a morning the beta saved your lead tech time, what did he do with it?" If the time goes back to the floor, the hours in `experiences.md` are real. If it disappears, they're not. Also worth asking: "Who has to agree before a work order is opened from a code?" Dwayne's veto came up in every other answer.
- **Also learned:** nobody adds up the cost of a truck that didn't roll. That weakens "the buyer can see downtime", the third riskiest assumption in `../problem/problem.md`.

*Synthetic panel: hypotheses, not evidence. Confirm with a real customer.*

## 2. Score the three framings

Each persona rated the three framings in `../problem/framings.md`: pain (1 to 5: how much it hurts them today) and pay (1 to 5: how likely their organisation pays to fix it, and through which budget). Sceptic first.

| Persona | As stated: pain | pay | The bigger job: pain | pay | The moonshot: pain | pay |
|---|---|---|---|---|---|---|
| Dwayne (sceptic) | 4 | 2 | 3 | 2 | 1 | 1 |
| Glen (buyer) | 2 | 2 | 5 | 4 | 4 | 2 |
| Rosa (user) | 4 | 3 | 4 | 2 | 3 | 1 |
| Tess (adjacent) | 1 | 1 | 3 | 2 | 1 | 1 |
| **Average** | **2.75** | **2.0** | **3.75** | **2.5** | **2.25** | **1.25** |
| **Spread** | 1–4 | 1–3 | 3–5 | 2–4 | 1–4 | 1–2 |
| Average, the three fleet personas | 3.3 | 2.3 | 4.0 | 2.7 | 2.7 | 1.3 |

In their own words:

- **Dwayne, as stated:** "That's my first hour every morning. Fine. But don't make me approve a list I already know by heart." Budget: the shop line, "if Rosa fights for it".
- **Dwayne, the bigger job:** "Parts and bays aren't my fight. Get me parts on the bench and leave me the call on the truck."
- **Dwayne, the moonshot:** "Nobody reads a code by hand? I've heard that one."
- **Glen, as stated:** "That's my shop's chore. Not why trucks miss 5 am." No budget of his.
- **Glen, the bigger job:** "Waiting on filters for a PM we knew was due. That's the whole problem." Budget: an add-on to the maintenance budget at the March 2027 renewal; he signs up to $50,000.
- **Glen, the moonshot:** "Show me fewer trucks down at 5 am first. Then talk about charging for uptime."
- **Rosa, as stated:** "That's my lead tech's first hour every day. But I already have Fault Code Assist for the bad days." Budget: an add-on at renewal, through the director and the CFO.
- **Rosa, the bigger job:** "That's my whole week. But it's five tools at once. Show me one that works first."
- **Rosa, the moonshot:** "Paid for uptime" isn't a line at her carrier.
- **Tess:** only her slice of the bigger job matters to her: "I won't pay for their uptime. I bill hours."

**Where they agree and disagree:**

- **The bigger job hurts most** for everyone (3.75 average, 4.0 for the fleets), and it's the only framing the buyer would pay for (4). That supports the product manager's choice.
- **The user and the buyer split on where the pain is.** Rosa and Dwayne feel the code list (4); Glen gives it a 2: "not why trucks miss 5 am". The fault code is the users' pain, the parts wait is the buyer's.
- **Pay is low across the board except the buyer.** Only Glen goes above 3, and only for the bigger job. Rosa feels it but doesn't hold the budget.
- **The moonshot is a slogan to all four.** Nobody has a budget line for uptime.

*Synthetic panel: hypotheses, not evidence. Confirm with a real customer.*

## 3. React to the experiences

Each persona walked through the five experiences in `experiences.md`, sceptic first: where it helps, where they'd get stuck, what they'd never let an agent do, and the moment they'd stop.

| Experience | Dwayne (sceptic) | Glen (buyer) | Rosa (user) | Tess (adjacent) |
|---|---|---|---|---|
| 1. The morning shortlist | Takes his first hour; stops after "two bad calls in a week". Never: a job that ties up a bay with his name on it | Helps the shop, not his 5 am; stops if a "watching" truck breaks down or it's another screen | Her first choice; stops the first time a "watching" truck breaks down on I-70 | Not her world |
| 2. Parts on the bench | Wants it; stops the second time a part is a phantom | His first choice: "this is my pain". Never: spend without a cap per order and per day | Stuck on wrong counts after receiving; stops at the first double order | Not her world; never order from her vendors |
| 3. A slot that survives dispatch | Only a little; dispatch "won't answer a machine" | Needs dispatch data FleetDesk doesn't hold; won't add a login | Wants the rebooked PM; doubts it without dispatch and live location | Never let a fleet's system bump a job in her bay |
| 4. Say it, sign it | His first choice: fixes "replaced" and "Other". Stops the day one note is used against a tech | Helps the audits; techs may feel watched | 14 techs stop typing "replaced"; stops if techs just tap through | Partly hers; doesn't want a second tool beside her shop software |
| 5. Overflow to a trusted shop | Helps when both bays are full; a comeback from outside lands on his shop | Fits his two smaller depots; his outside shops won't install a new tool | Saves phoning around; stops at one bad invoice that slips through | Her first choice, if it drops into her software and never shows her margins |

**What each would want first:** Rosa the shortlist, Glen the parts, Dwayne the notes, Tess the overflow. Every persona picked the one that removes their own chore.

**What none of them would let an agent do:** spend money, move a truck off a route, or file a claim without a named person seeing it.

**Price, agents at $8 per vehicle a month:** no yes. Glen: not now, he'd pilot the parts experience first and sign it himself at renewal, under his $50,000 limit. Rosa: not now, she'd back a pilot of the shortlist; the director and the CFO sign. Dwayne: not now, "show me it on a truck I know". Tess: not her bill; she might pay a small monthly add-on to her own software for experience 5, after a trial. (The price for the shortlist alone was later voted on and set at $3 per powered vehicle a month: `../roadmap/roi.md`.)

**The three changes that would win over the most personas:**

1. **A person's name on every action, and a quick veto.** Nothing is opened, ordered, moved or filed without a named person seeing it, and the lead tech can strike a job in one tap. It answers Dwayne, Rosa and Glen.
2. **Prove it on their own trucks before the price.** A pilot that counts hours given back and trucks down at their fleet, then the price. It answers Glen, Rosa and Dwayne.
3. **Show the parts on every drafted job.** Put a "parts on the shelf: yes / no" line on each draft in the shortlist, so the buyer's pain shows up in the users' first experience. It answers Glen and Dwayne.

Added to `experiences.md` under "What the panel said" for each experience.

*Synthetic panel: hypotheses, not evidence. Confirm with a real customer.*

## The best objection

"You're asking me to trust a machine that picks my jobs and writes my notes, and when it's wrong, I'm the one who gets blamed." (Dwayne; Rosa said the same in her own words.)

Glen's is the commercial one: he'll pay only if it proves fewer trucks down with one fewer login, next to Motive's one-bill offer, with last year's price rise still fresh.

**Worth adding to `../problem/problem.md`, under what to learn before building:** "Who gets blamed when the agent's pick is wrong, and who must be able to veto it?" Not added yet; the product manager decides.

*Synthetic panel: hypotheses, not evidence. Confirm with a real customer.*
