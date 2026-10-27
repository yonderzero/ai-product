# Customer interview: maintenance manager, waste hauler (flows and mockups)

*Fictional. Transcript of a customer call by the FleetDesk product team, 27 Oct 2026, lightly edited. Names, emails and phone numbers removed; people are named by role only.*

**Who:** maintenance manager at a regional waste hauler. 160 refuse trucks (rear-loaders, side-loaders and roll-offs) and 40 support vehicles, one shop with 9 technicians and a shop lead. FleetDesk Pro since 2020. Geotab telematics streaming codes and meters into FleetDesk. In the Fault Code Assist beta since May 2026. Influences the purchase; the general manager signs.

**Interviewers:** product manager, designer. **Shown:** `flows/mockups/morning-shortlist.html` and `flows/mockups/say-it-sign-it.html`, one moment at a time; the parts, dispatch and overflow flows described from the flow map.

## Part 1 · Their world

**PM:** Walk me through yesterday morning. What was waiting for you?
**Manager:** About 180 codes from Geotab and maybe 25 driver write-ups. I take the write-ups. My shop lead and I go through the codes together before the trucks roll out. Most of an hour, between the two of us.

**PM:** How many of those codes became work?
**Manager:** Two work orders. Two. And one of them was a write-up first, the code just backed it up.

**PM:** Tell me about the last time a code you didn't act on turned into a breakdown.
**Manager:** August. A rear-loader threw an aftertreatment code three days running. We had it in the beta as "plan in". It derated on route with a full body. We sent another truck to take the load and towed it. The tow alone was fourteen hundred, and two routes ran late.

**PM:** What did you check before you opened the last work order from a code?
**Manager:** Did it repeat. Did a driver write anything up on that truck. When was the last PM. And for the packers, the PTO hours, because the hydraulics wear on hours, not miles. FleetDesk doesn't really use the PTO hours.

**PM:** You told us in the beta you hide the "watch" codes. Why?
**Manager:** Because there were forty of them a day and none of them meant anything. So I hid them. Which is how I missed the one in August.

**PM:** Think of the last truck that sat waiting. What was it waiting for?
**Manager:** A cylinder seal kit for a packer. Nobody could have predicted that one. PM parts we're fine on. We stage the kits the day before.

## Part 2 · The flows

*Mockup: the morning shortlist.*

**PM:** What do you think this is?
**Manager:** My morning. Done before I get in.

**PM:** What would you do first here?
**Manager:** Tap "Why this truck". I want to see the codes behind it. The actual codes, not a summary. Every time, until I trust it.

**PM:** What would you let this do on its own? What would you always want to check?
**Manager:** Sort them, group them, rank them, write the draft. Fine. Opening the work order, that's me. And it can't hide a driver write-up. Ever. The driver signed that.

**PM:** *(moment 5, the shop lead's strike)* What about this?
**Manager:** My shop lead should see it, yes. But I'm not waiting on him to open the day. If I approve and he strikes it, it's a conversation. Show me both and I'll decide.

**PM:** *(moment 7, "Watching")* And this list?
**Manager:** This is the one that matters to me. If a truck's in here, tell me how many days it's been in here. If it's back for the third time, it should shout.

**PM:** What's missing for you to rely on it?
**Manager:** The PTO hours on the packers. And a way to mark a code as noise for one model only. One model of ours throws a sensor code every cold morning.

*Mockup: say it, sign it.*

**PM:** What do you think this is?
**Manager:** Notes without typing. My techs would love that.

**PM:** What would you let this do on its own?
**Manager:** Write the cause and correction from what he says. Match the parts. Yes. The time, no. Don't fill the time from the clock. Time is touchy here. The union steward would be in my office the same day. Let the tech put his own time, or confirm it.

**PM:** Where would they use it?
**Manager:** Not in the bay. They're in ear protection. At the bench, or in the cab.

**PM:** What would this replace in your week?
**Manager:** Me chasing cause and correction. Our hydraulics vendor bounces warranty claims with no cause on them.

*Described from the flow map: parts, the dispatch slot, overflow.*

**Manager:** Parts: our counts are wrong after every delivery. I wouldn't let it order anything until that's fixed. The dispatch one isn't our problem. Our routes run on fixed days, so PMs land where we put them. Outside shops: we use the dealer for warranty work. The dealer won't log into anything of ours.

## Part 3 · Commitment

**PM:** Could we try this with your team on one real case?
**Manager:** Run the shortlist on our codes from the last two weeks. I'll mark which trucks I'd have pulled. If it matches, we turn it on for real at the north yard.

**PM:** Who would need to agree to pay for something like this?
**Manager:** If it's a few dollars a truck, it's my budget. If it's another Pro plan on top, it's the general manager, and he'll ask what it replaces.

## Follow-ups

- Product team to run the shortlist on two weeks of the hauler's codes, write-ups and PMs, and send it for marking.
- Look at PTO hours from Geotab for refuse trucks.
