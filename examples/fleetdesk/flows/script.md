# FleetDesk · Customer interview kit

> Fictional example. FleetDesk and its customers are invented. The questions are the kind to use with real customers.

For interviewing real customers about getting every truck that needs work from the first signal back on the road, and about the flows, using the mockups. About their life and the past first, the mockups second. Built on 27 Oct 2026.

**Who to talk to:** maintenance managers at fleets of 150 to 500 vehicles with their own shop and a telematics feed (three or more, like Rosa); lead technicians or shop supervisors at the same fleets (two or more, like Dwayne); one director of fleet operations (like Glen). Start with the 46 Fault Code Assist beta customers. · **Bring:** the mockups in `mockups/`: `morning-shortlist.html` and `say-it-sign-it.html`.

## Before you start

- Ask permission to take notes or record. Don't keep names or contact details in the notes you share.
- You're there to learn, not to sell. Talk less than they do.
- Don't show a mockup until Part 2.

## Part 1 · Their world (no mockups yet)

The riskiest assumptions from `../problem/problem.md`, as questions about the past:

1. "Walk me through yesterday morning. What was waiting for you, and who read it?"
2. "How many codes did you see yesterday, and how many became work?"
3. "Tell me about the last time a code you didn't act on turned into a breakdown. What happened? What did it cost?"
4. "What did you check before you opened the last work order from a code?"
5. "Who has to agree before a work order is opened from a code? Who gets blamed when the call is wrong?"
6. "Walk me through the last work order you closed. What did you write, and why that?" (technicians)
7. "When did a warranty claim last get rejected? What was missing?"
8. "Think of the last truck that sat in the yard waiting. What was it waiting for?"
9. "How did you work out what the last truck that didn't roll cost you? Who saw that number?" (directors)
10. "On a morning the beta saved your lead tech time, what did he do with it?" (beta customers)

## Part 2 · The flows

Show each flow's mockup one moment at a time, with "Next". Don't explain it first.

**The morning shortlist** (`mockups/morning-shortlist.html`), seven moments: overnight, the lead tech's say, the shortlist, why this truck, approve, when the feed stops, Watching.

**Say it, sign it** (`mockups/say-it-sign-it.html`), six moments: open the job, say it, the draft, when it isn't sure, sign it, what's left.

At each moment:

1. "What do you think this is?"
2. "What would you do first here?"
3. "What would you let this do on its own? What would you always want to check?"
4. "What's missing for you to rely on it?"
5. "What would this replace in your week?"

Then, once per flow:

- "When would you stop using it?"
- (Shortlist) "Who should be able to strike a pick: you, the lead tech, both? Before or after it's opened?"
- (Notes) "Where in the shop would you actually talk to it? Who should be able to hear the recording?"

Describe the other three flows from `flows.md` in one or two lines each (parts, the dispatch slot, overflow) and ask: "Is this a problem at your fleet? When did it last happen?"

## Part 3 · Commitment

Not "would you buy it?", but a real next step:

- "Could we run the shortlist on your own recent codes, write-ups and PMs, and you mark which trucks you'd have pulled?"
- "Could two of your technicians try the notes on real jobs?"
- "Who else should see this?"
- "Who would need to agree to pay for something like this, and from which budget?"

## After the interview

Write notes the same day, in their words, and put them in `../documents/`. Then run `/ai-product-flows` again to compare them with the panel.

So far: two interviews on 27 Oct 2026, a maintenance manager at a waste hauler and a shop supervisor at a beverage distributor (`../documents/interview-maintenance-manager-waste-hauler-flows.md`, `../documents/interview-shop-supervisor-beverage-distributor-flows.md`). **Next real interview:** a director of fleet operations, to test whether the buyer will pay for the shortlist alone.
