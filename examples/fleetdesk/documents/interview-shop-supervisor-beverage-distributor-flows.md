# Customer interview: shop supervisor, beverage distributor (flows and mockups)

*Fictional. Transcript of a customer call by the FleetDesk product team, 27 Oct 2026, lightly edited. Names, emails and phone numbers removed; people are named by role only.*

**Who:** shop supervisor (the lead technician) at a regional beverage distributor. 290 vehicles: tractors and bay trucks across two depots, two shops, 11 technicians, one parts manager. FleetDesk Pro since 2019. Samsara telematics streaming codes into FleetDesk. Their parts manager gave feedback in the Fault Code Assist beta. Doesn't buy; the maintenance manager and the director of fleet operations do.

**Interviewers:** product manager, designer. **Shown:** `flows/mockups/morning-shortlist.html` and `flows/mockups/say-it-sign-it.html`, one moment at a time; the parts, dispatch and overflow flows described from the flow map.

## Part 1 · Their world

**PM:** Walk me through the last work order you closed. What did you write?
**Supervisor:** Brake job on a bay truck. I wrote "replaced front pads and rotors". That's what I did.

**PM:** When did a warranty claim last get rejected? What was missing?
**Supervisor:** A starter, in the spring. It came back. No cause, no mileage at failure. The tech wrote "replaced starter". So did I, to be honest, half the time.

**PM:** Walk me through your morning yesterday.
**Supervisor:** I read the Samsara list at the desk around six. Forty minutes. On a Monday, more than an hour. Most of the codes I know by heart. Then I hand out the jobs.

**PM:** Who has to agree before a work order is opened from a code?
**Supervisor:** Me. My manager signs off anything over a thousand dollars.

**PM:** Think of the last truck that sat waiting. What was it waiting for?
**Supervisor:** Parts. It's always parts. A DEF pump on backorder, last month. And our counts are wrong after every delivery, so the system says we have it and we don't.

## Part 2 · The flows

*Mockup: the morning shortlist.*

**PM:** What do you think this is?
**Supervisor:** The list I make in my head every morning.

**PM:** What would you let this do on its own?
**Supervisor:** Rank them and write the draft. Fine.

**PM:** *(moment 5, the strike button)* And this?
**Supervisor:** Good. But I want to strike it before it's opened, not after. Once it's opened, it's on the board, a bay's tied up and someone's pulling parts.

**PM:** What's missing for you to rely on it?
**Supervisor:** Show me the freeze-frame data, not just the code. And know our noise. We have a model year that throws a sensor code every cold start. If it pulls one of those in, I'm done with it.

*Mockup: say it, sign it.*

**PM:** What do you think this is?
**Supervisor:** Notes. The part nobody does.

**PM:** Where would you use it?
**Supervisor:** Not in the bay with an impact gun going. Walking back to the bench, sure. Hold the button, say it, done.

**PM:** What would you let it do on its own?
**Supervisor:** Write it up. Match the parts. Fill the time, if I can fix it before I sign.

**PM:** *(moment 4, the recording kept with the note)* What about this?
**Supervisor:** Who listens to it? If my manager can play it back to grade me, the guys won't touch it. Keep it with the truck. For warranty. That's it.

**PM:** What would this replace in your week?
**Supervisor:** Going back through the day's work orders at the end of the shift and fixing the ones that say "replaced".

*Described from the flow map: parts, the dispatch slot, overflow.*

**Supervisor:** The parts one is the one I want most. But not until the counts are right. Dispatch: they move trucks all day, but they'll never answer a message from a computer. They'll answer me on the radio. Outside: our mobile mechanic texts photos. He won't use an app.

## Part 3 · Commitment

**PM:** Could we try this with your team on one real case?
**Supervisor:** Put the notes on two of my guys' tablets. The younger ones. If they like it, the rest will follow.

**PM:** Who else should see this?
**Supervisor:** The parts manager. And my manager, because she pays.

## Follow-ups

- Offer "Say it, sign it" to two technicians once a pilot exists.
- Ask Samsara integration team whether freeze-frame data comes through with the codes.
