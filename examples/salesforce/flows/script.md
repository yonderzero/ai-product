# Salesforce Sales Cloud and Service Cloud · Customer interview kit

> Illustrative. Not affiliated with or endorsed by Salesforce. The product manager's plans are invented, tagged `[PM, illustrative]`.

For interviewing real customers about where every deal really stands without chasing reps, and about the two flows taken forward, using the mockups. About their life and the past first, the mockups second. Built on 27 Oct 2026.

**Who to talk to:** VPs of sales or sales managers at mid-market B2B companies on Sales Cloud (five), account executives on their teams (five), and revenue operations leads or admins (three) `[PM, illustrative]` · **Bring:** `mockups/rep-confirm.html` and `mockups/forecast-brief.html`

## Before you start

- Ask permission to take notes or record. Don't keep names or contact details in the notes you share.
- You're there to learn, not to sell. Talk less than they do.
- Talk to the rep and the manager separately. Reps won't say what they hide in front of their manager.

## Part 1 · Their world (no mockups yet)

The riskiest assumptions from `../problem/problem.md`, as questions about the past:

1. **Reps hold back bad news, or just lack time?** "Tell me about the last deal that slipped without warning. When did the rep know?" · "What was in the record the week before? Why?" · To a rep: "When you kept a deal in commit you had doubts about, what would have made you pull it earlier?"
2. **Will they trust a record they didn't type?** "Tell me about the last time you found a wrong number in the pipeline. How did you find it?" · "When a tool logged activity for you, what did you still check by hand?" · "What did you do after you found the mistake?"
3. **Is the spreadsheet there because the CRM is behind?** "Walk me through last week's forecast. Where did each number come from?" · "What did you change in the spreadsheet that wasn't in Salesforce?"
4. **Would they pay us instead of, or on top of, a tool on top?** "What do you pay today for call recording or forecasting? Who signed it?" · "At the last renewal, what nearly made you drop it?"
5. "Who else gets involved when the forecast goes wrong?"

## Part 2 · The flows

Show each mockup one moment at a time. Don't explain it first. Reps see `rep-confirm.html`; managers see `forecast-brief.html`, then the rep's one; revenue operations sees both.

1. "What do you think this is?"
2. "What would you do first here?"
3. "What would you let this do on its own? What would you always want to check?"
4. "What's missing for you to rely on it?"
5. "What would this replace in your week?"

Moment by moment, also ask:

- **Rep, the review list:** "Last time you updated a deal after a call, what did you change? Would these three have been right?"
- **Rep, the private preview:** "If your manager saw this before you did, what would you do?"
- **Manager, what changed:** "Could you repeat this to your CEO as it stands?"
- **Manager, the number:** "Last quarter, how far off were you? What would have told you sooner?"
- **Manager, the override:** "When did you last overrule a rep's deal? What was the reason?"
- **Revenue operations, the log:** "Where would you check this? What would make you switch it off?"

## Part 3 · Commitment

Not "would you buy it?", but a real next step:

- "Could we run this with one of your teams on last quarter's deals, and compare the brief with what really closed?"
- "Who else should see this?"
- "Who would need to agree to pay for something like this, and from which budget?"

## After the interview

Write notes the same day, in their words, and put them in `documents/` (create it in a real run). Then run `/ai-product-flows` again to compare them with the panel.
