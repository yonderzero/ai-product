# FleetDesk · Interviews about the flows

> Fictional example. FleetDesk, its customers and documents are invented. The personas are synthetic and not real people: what they say is a hypothesis to test with real customers, never evidence.

Each round: the personas walk through each flow as themselves, each in its own agent with only its own persona file and the material being judged, the sceptic first. Real interviews are at the bottom, and outweigh the panel. Built on 27 Oct 2026.

## Round 1 · 27 Oct 2026 · the five flow maps in `flows.md`

All five flows, read moment by moment from the "What they see" column and "When it goes wrong". No mockups yet.

### Dwayne, lead technician (sceptic)

- **First thing he'd do:** test the shortlist on trucks he already knows, then check what it left out.
- **Where he'd get stuck:** "a code three nights running can mean a bad sensor, not a thermostat"; a strike that needs typing; shop noise for the notes; shelf counts for parts.
- **What he'd let the agent do alone:** read, group, drop exact repeats; draft notes and match parts; reserve and move parts between the two shops.
- **What he'd never let it do:** open jobs that tie up a bay for nothing with his name on them; order from a guessed cause; close a note without his signature; use his words to judge or time him.
- **What's missing for his job:** "a way to say no without typing"; a record of when it was wrong; a written promise that recordings never go to timesheets.
- **The moment he'd stop:** "the first time a 'Watching' truck breaks down and nobody asks me why"; a recording used against a tech.
- **In his words:** "Show me it was right on 2217 last week, then talk to me." · "I'll talk for two minutes. Just don't make me type."

### Glen, director of fleet operations (buyer)

- **First thing he'd do:** check the shortlist against which trucks didn't roll at 5 am; look at the filter case in the parts flow.
- **Where he'd get stuck:** the shortlist goes to Rosa, and he gets no number; vendor delivery dates and reefer parts sit outside FleetDesk; dispatch is another system.
- **What he'd let the agent do alone:** read, group, rank, draft; reserve stock and order under a limit he sets; package outside jobs.
- **What he'd never let it do:** open a work order without a named person; buy from a new vendor or go over the cap; touch a route.
- **What's missing for his job:** "a count of trucks down at 5 am, before and after", as a weekly page for the CFO with no new login.
- **The moment he'd stop:** a truck in "Watching" misses the morning "and the only fix is 'tune the ranking'"; the first double order.
- **In his words:** "Don't send me a list. Send me fewer trucks down." · "Nice for Dwayne. I won't pay extra for it."

### Rosa, maintenance manager (user)

- **First thing she'd do:** open the shortlist before coffee, check the feed line, read the "Pull in today" reasons.
- **Where she'd get stuck:** the "Watching" pile: "too many watch codes" is what made her hide them in the beta; wrong counts for parts; a dispatch system she can't see.
- **What she'd let the agent do alone:** read, group, rank, draft, bring trucks back; reserve and move parts between her shops; draft notes.
- **What she'd never let it do:** open a work order without her name; hide or drop a code; put a safety defect in "Watching"; order parts; invent a cause.
- **What's missing for her job:** "Dwayne's say before I see the list, not after"; the "needs you" notes list at the end of the shift.
- **The moment she'd stop:** the meter sync breaks again and the list doesn't say so. "Once."
- **In her words:** "Three trucks, and why. If the why is vague, it's just another dashboard."

### Tess, owner of an independent repair shop (adjacent)

- **First thing she'd do:** for overflow, read the job: codes, history, limit, then accept and set the time. The other four: "not my world".
- **Where she'd get stuck:** jobs arriving by link instead of in her own shop software; how a shop gets on a "preferred" list; a supplement over the limit while the truck sits in her bay.
- **What she'd let the agent do alone:** package the job and approve her estimate under the limit.
- **What she'd never let it do:** set her price or time; show the fleet her margins; touch her vendors; move her schedule.
- **What's missing for her job:** being paid fast, not just approved fast.
- **The moment she'd stop:** a half-empty job, or an approval slower than a phone call.
- **In her words:** "Send me the codes, the history and how much I can spend. I'll have it out today."

### Scores

Value / trust / pay, 1 to 5.

| Flow | Dwayne | Glen | Rosa | Tess | Average | Spread |
|---|---|---|---|---|---|---|
| 1. The morning shortlist | 4 / 2 / 2 | 4 / 4 / 4 | 5 / 3 / 4 | 1 / 2 / 1 | 3.5 / 2.75 / 2.75 | 1–5 / 2–4 / 1–4 |
| 2. Parts on the bench | 3 / 3 / 3 | 5 / 3 / 5 | 3 / 3 / 3 | 1 / 2 / 1 | 3.0 / 2.75 / 3.0 | 1–5 / 2–3 / 1–5 |
| 3. A slot that survives dispatch | 2 / 2 / 3 | 2 / 2 / 2 | 5 / 2 / 2 | 2 / 2 / 1 | 2.75 / 2.0 / 2.0 | 2–5 / 2 / 1–3 |
| 4. Say it, sign it | 5 / 3 / 3 | 3 / 4 / 2 | 4 / 4 / 4 | 1 / 3 / 1 | 3.25 / 3.5 / 2.5 | 1–5 / 3–4 / 1–4 |
| 5. Overflow to a trusted shop | 2 / 3 / 2 | 4 / 3 / 4 | 2 / 3 / 2 | 5 / 4 / 4 | 3.25 / 3.25 / 3.0 | 2–5 / 3–4 / 2–4 |

**Where they disagree:**

- **Each persona's top flow removes their own chore:** Rosa the shortlist, Glen the parts, Dwayne the notes, Tess the overflow, as in `../research/panel.md`.
- **Trust in the shortlist splits user and sceptic:** Rosa 3, Dwayne 2. He trusts it only if he can say no in one tap, before anything opens.
- **The buyer won't pay for the notes** (pay 2) that the sceptic values most (value 5). Its money case has to be warranty and clean records, not Glen's downtime.
- **Nobody trusts the dispatch slot** (trust 2 from all four): FleetDesk doesn't hold dispatch's plan or live location.

**The three changes that would win over the most personas:**

1. **The lead tech goes first, with a one-tap "no".** Preset reasons, no typing, before Rosa reads the list, and nothing opens until she approves. Wins Dwayne and Rosa.
2. **Make "Watching" short and honest.** Days in "Watching", trucks come back when a code repeats, the feed's status at the top, the long piles collapsed. Wins Rosa, Dwayne and Glen.
3. **Put the promise on the notes.** Notes and recordings stay with the truck's record, never timesheets or grading; the technician confirms his own time. Wins Dwayne, Rosa and Glen.

All three made. Mockups built for the two flows that led round 1, the shortlist and the notes: `mockups/morning-shortlist.html` and `mockups/say-it-sign-it.html`.

*Synthetic panel: hypotheses, not evidence. Confirm with a real customer.*

## Round 2 · 27 Oct 2026 · mockups: `morning-shortlist.html`, `say-it-sign-it.html`

The same four agents, on what changed.

### Dwayne, lead technician (sceptic)

- **Better:** sees the picks before Rosa; one tap with a preset reason; a job waits for him before it gets a bay; "the feed warning is honest".
- **Still bothers him:** one strike turning a code into noise for every truck of that model ("If I'm wrong on a bad day, a real DEF fault gets buried and it's my name on it"); "7 out of 9 is a small sample. Show the nine"; parts "on the shelf" is the system's count, not the shelf; a big button for gloved hands.
- **The moment he'd stop:** the noise rule hides a real fault, or a strike is used to judge him; the recording or his clocked time shows up in a pay or review conversation.
- **In his words:** "A promise on a screen is not a policy. I want it in writing."

### Glen, director of fleet operations (buyer)

- **Better:** Dwayne strikes first; days in "Watching"; the feed warning; "parts on the shelf" and "sensor on order, due Wed" is "exactly the filter problem I told you about".
- **Still bothers him:** still no count of trucks that rolled at 5 am: "I can't prove a thing to my CFO from a shortlist." A fleet-wide noise rule from one tap; he wants a rule list he can review.
- **The moment he'd stop:** a truck in "Watching" dies on the road and the answer is "the ranking will be tuned".
- **In his words:** "Add it as a weekly card, not a new screen." Pay rises from 3 to 4 with the CFO card.

### Rosa, maintenance manager (user)

- **Better:** "Dwayne checks first, so I'm not reading a list he'd gut"; the feed warning names the trucks; safety items stay in "Pull in today" even with the feed down; the end-of-shift "needs you" list catches "the two things I chase today".
- **Still bothers her:** "One tech's tap quietly rewrites the rules for 240 tractors. That is how I miss the one code that matters." She wants the rule to need her OK. 37 trucks in "Watching" is still a lot. The notes promise belongs in the contract.
- **The moment she'd stop:** a struck truck breaks down on I-70 and the answer is "known glitch".
- **In her words:** "Charge per tractor, not per trailer."

### Tess, owner of an independent repair shop (adjacent)

- **Better:** a signed complaint, cause and correction helps her, if it travels with the truck as a page her shop software can take: "I skip the diagnosis and the phone call."
- **Still bothers her:** the shortlist never sends a truck to her; she'd re-check the fleet's cause before quoting.
- **In her words:** "It is jobs landing in software we already have."

### Scores

| Flow | Dwayne | Glen | Rosa | Tess | Average | Spread |
|---|---|---|---|---|---|---|
| 1. The morning shortlist | 4 / 3 / 3 | 4 / 4 / 3 | 5 / 3 / 4 | 1 / 2 / 1 | 3.5 / 3.0 / 2.75 | 1–5 / 2–4 / 1–4 |
| 4. Say it, sign it | 5 / 4 / 3 | 3 / 4 / 2 | 4 / 4 / 3 | 3 / 3 / 2 | 3.75 / 3.75 / 2.5 | 3–5 / 3–4 / 2–3 |

The three fleet personas alone: the shortlist 4.3 / 3.3 / 3.3; the notes 4.0 / 4.0 / 2.7.

**Where they disagree:** Glen's pay for the shortlist depends on a number for his CFO, which the flow doesn't give; Rosa's and Dwayne's depend on trust. The notes win trust from everyone, but only Rosa would put real budget behind them.

**The three changes that would win over the most personas:**

1. **A strike applies to that truck only; a fleet-wide noise rule needs Rosa's approval.** Rosa, Glen and Dwayne. Made in the mockup.
2. **Show the past cases behind the ranking.** Dwayne. Made: "See the 9 trucks".
3. **Put the notes promise in the customer agreement, not just on the screen.** Rosa, Glen and Dwayne. Taken to the roadmap.

Glen's weekly card of trucks down at 5 am is not in the flows; it goes to the roadmap.

*Synthetic panel: hypotheses, not evidence. Confirm with a real customer.*

## Real customers

| Date | Who (role, no names) | What they said about each flow | Same as the panel? | Source |
|---|---|---|---|---|
| 27 Oct 2026 | Maintenance manager, waste hauler, 160 refuse trucks, Geotab, beta user | **Shortlist:** "My morning. Done before I get in." Would tap "Why this truck" every time until she trusts it; it must never hide a driver's write-up; she won't wait for her shop lead to approve. Wants days in "Watching", noise marked per model, and PTO hours for the packers. **Notes:** wants them; never fill time from the clock (union); techs would talk at the bench or in the cab. **Parts:** not until counts are right; PM kits already staged. **Dispatch slot:** not her problem, fixed routes. **Overflow:** "The dealer won't log into anything of ours." **Commitment:** mark a shortlist replayed from her own recent codes; pilot at the north yard if it matches. "A few dollars a truck" is her budget. | **Yes** on the shortlist, "Watching" and noise per model. **No** on the strike: she won't wait for the lead tech, where the panel's Rosa wanted his say first. **No** on overflow, where Tess was keen. **New:** the union and the time field. | `../documents/interview-maintenance-manager-waste-hauler-flows.md` |
| 27 Oct 2026 | Shop supervisor (lead technician), beverage distributor, 290 vehicles, Samsara | **Shortlist:** "The list I make in my head every morning." Strike before it's opened, "or a bay's tied up". Wants freeze-frame data and the fleet's known noise; stops the first time it pulls in a known sensor glitch. **Notes:** "The part nobody does." Hold-to-talk at the bench, not in the bay; recording kept with the truck only. **Parts:** "It's always parts", but counts are wrong after every delivery. **Dispatch slot:** "They'll never answer a message from a computer." **Overflow:** the mobile mechanic "won't use an app". **Commitment:** two technicians will try the notes. | **Yes**, closely matching Dwayne: strike before opening, no grading, parts as the real wait. **No** with the panel's Glen on the notes: the supervisor values them most, the buyer persona least. | `../documents/interview-shop-supervisor-beverage-distributor-flows.md` |

**Where real customers agree with the panel:** the shortlist and the notes are the two flows to take forward; the agent never opens a work order without a named person; notes must never be used to judge a technician; counts must be right before parts ordering; the dispatch slot can't work without dispatch's data.

**Where they disagree, and what we did:** the panel's Tess and Glen liked overflow; both real customers say their outside shops won't use a new tool, so overflow drops. The panel's Rosa wanted the lead tech's say first; the real manager won't wait, and the real supervisor won't have a bay tied up. Both are met: the lead tech sees the picks first, Rosa doesn't wait, and a job she approved waits for his look before it gets a bay. Neither the panel nor the earlier evidence raised the union and the time field; now the technician always confirms his own time.

**Still not tested with a real customer:** whether a buyer pays for the shortlist on its own. Next real interview: a director of fleet operations (`script.md`).
