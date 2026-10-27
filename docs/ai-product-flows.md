# ai-product-flows

```
/ai-product-flows
```

The sixth skill, after [`ai-product-research`](ai-product-research.md). Claude takes your agentic customer experiences and maps each one as a **flow**: what the agent does, what people see and decide, and what happens when it goes wrong. It makes the flows clickable, then helps you find the **right flows** by testing them with **real customers and your synthetic panel, side by side**.

Flows, not features yet: features come in the next skill.

**Real customers outweigh the panel.** The panel covers the people you can't reach yet, and stress-tests reactions before you take customers' time. A flow real customers reject drops, whatever the panel said.

**Who runs it:** the product manager, with anyone who can line up customer conversations.
**Run it:** in the folder that holds your product's folder. Run it again after each real interview.
**You leave with:** your agentic experiences mapped as flows, clickable mockups of each, an interview kit for real customers, and the flows to take forward, ranked on value, trust and what customers would pay for.

## Before you begin

- **Your research.** Run [`/ai-product-research`](ai-product-research.md) first: this skill needs its agentic experiences and personas. They don't have to be finished.
- **A screenshot of your product** (optional), or its colours and logo, so the mockups feel like yours.
- **Real customers to talk to**, today or this week. Real interviews are the strongest evidence for which flows matter.

## What happens

Claude asks one question at a time, like a conversation.

1. **What this is.** Claude explains the session and asks: "Shall we start?"

2. **The flows.** Starting with the experience you chose to explore first, Claude walks through each experience with you, one moment at a time, and maps:
   - **the main path:** at each moment, what the agent does, what the person does (nothing, reviews, approves, decides), and what they see;
   - **when it goes wrong:** missing data, low confidence, a complaint, a rule broken, and what the agent and the person do then;
   - **what the agent does alone, what the person always approves, and what the agent never does;**
   - **the data it needs.**

   At each moment Claude asks what the persona would need to see to trust it.

3. **The mockups.** One clickable mockup per flow, walking through its key moments in order: the trigger, what the agent did, the moment the person approves, an exception being handled. They use realistic data and open in the preview. They're mockups for testing flows, not the product.

4. **The interview kit.** A script for real customers: questions about their past first (the Mom Test), then each flow one moment at a time, then a real next step. Claude asks who you can talk to.

5. **Interview the panel.** Each persona walks through each flow as themselves, sceptic first, each in its own agent: what they'd do first, where they'd get stuck, what they'd let the agent do alone, what never, what's missing. Each scores every flow 1 to 5 on:
   - **value:** does it give their time back?
   - **trust:** would they let the agent do it?
   - **pay:** would their organisation pay for it?

6. **Iterate.** Claude proposes the three changes that would win over the most personas, updates the flows and mockups with the ones you choose, and runs a second round.

7. **Real customers.** Add interview transcripts or notes to `documents/`, or paste them in. Claude summarises each, without names, and shows where real customers agree or disagree with the panel.

8. **The right flows.** Claude ranks the flows on value, trust, pay and hours given back, with real customers outweighing the panel. You decide which flows to take forward, which later and which not, and the thinnest version of each that still shows the whole experience end to end.

9. **The deck.** Claude adds the flows, the mockups and the feedback to `index.html`.

10. **Done.** Claude sums up the flow customers valued most, the flows to take forward, and the next real interview to do.

## What you get

```
acme-scheduler/
  flows/
    flows.md         each flow mapped and ranked; the flows to take forward and their thinnest versions
    mockups/         one clickable mockup per flow
    panel-tests.md   each round with the panel, and every real interview, side by side
    script.md        the interview kit for real customers
```

## Troubleshooting

- **Claude asks you to run another skill first.** This skill needs the research step's experiences and personas.
- **You can't reach a real customer today.** Carry on with the panel, and keep `script.md` for this week. The ranking says plainly that it rests on the panel until real interviews come in.
- **A real customer disagrees with the panel.** Good: that's what real interviews are for. The real customer wins, and Claude notes the difference.
- **The mockups don't look like your product.** Share a screenshot, and Claude restyles them.
- **You ran out of time.** Say so. Claude saves what's done and marks the rest "Not done yet". Run `/ai-product-flows` again later, for example after your next real interview.

## Tips

- Show one moment at a time, and don't explain it first: watch what they do.
- Ask what they'd *never* let an agent do. The answer tells you where the approvals and guardrails go.
- Ask for a real next step (a trial on one real case, a colleague to show it to), not "would you buy it?".

## Next

[`/ai-product-roadmap`](ai-product-roadmap.md): ideation, prioritisation, ROI and pricing, turning the right flows into the features for this product update and the roadmap.
