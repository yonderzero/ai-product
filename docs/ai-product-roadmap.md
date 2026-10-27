# ai-product-roadmap

```
/ai-product-roadmap
```

The seventh skill, after [`ai-product-flows`](ai-product-flows.md): ideation, prioritisation, ROI and pricing. Claude turns your right flows into feature ideas, prioritises them, works out what this product update is worth to your customers and to you, helps you choose how to charge for the agents, and lays out the roadmap from this update to your BHAG.

**Who runs it:** the product manager, ideally with someone who can judge effort, and someone who knows pricing.
**Run it:** in the folder that holds your product's folder.
**You leave with:** the clear features in this product update, its ROI for a typical customer and for you, how you'll charge for the agents, a Now / Next / Later roadmap, and the build-day slice your developers can build first.

## Before you begin

- **Your right flows.** Run [`/ai-product-flows`](ai-product-flows.md) first. It doesn't have to be finished: this skill needs `flows/flows.md`.
- **Rough numbers:** what the update might cost to build and run, and how you price today. Rough is fine.

## What happens

Claude asks one question at a time, like a conversation.

1. **What this is.** Claude explains the session and asks: "Shall we start?"

2. **Ideation.** For each flow you're taking forward, moment by moment, Claude generates feature ideas:
   - what the agent needs to be able to do;
   - what people see and control: a summary of the agent's work, approvals, exceptions, "why the agent did this", undo, guardrails;
   - the data it needs.

   It adds ideas from your opportunities, the Imagine section, and what real customers and the panel asked for, then asks what else would make the flow great and what could be left out.

3. **Prioritise.** Each feature gets:
   - **value:** hours given back and how much customers want it (real customers first, then the panel);
   - **pay:** how likely customers pay for it;
   - **confidence:** how strong the evidence is;
   - **effort:** agreed with you.

   **Priority = (value + pay) × confidence ÷ (effort + 1)**, with the working shown. Claude proposes Now, Next or Later for each, and asks what you'd move.

4. **ROI.**
   - **For a typical customer:** today against with this update, from the double cost (licence plus people's time) worked out in research: what they save, and their return on what they pay for agents.
   - **For you:** new agent revenue per customer and across the customers who'd buy, against what the update costs to build and run.

   Every number shows its working, and assumptions are labelled.

5. **Pricing.** The ways to charge for agents (per outcome, per agent, usage, a tier), with the fit and risk of each. The personas vote on price (Van Westendorp), and Claude adds what real customers said and checks the price against the labour it saves. You choose how to charge, and at what price.

6. **The roadmap.** Three horizons, without dates:
   - **Now:** this product update: the clear features, the flow they make real, the outcome, the price, the new revenue, how you'll know it worked;
   - **Next** and **Later:** climbing the AI levels toward your vision and your BHAG.

7. **This product update.** The clear list of features in Now, and **the build-day slice**: the smallest end-to-end slice your developers can build first to make the flow real and testable, with what's in, what's out for now, and when it's done. It points your developers to `flows/DESIGN.md` and the mockups, so what they build looks like what customers tested.

8. **The deck.** Claude adds this update, ROI and pricing, and the roadmap to `index.html`.

9. **Done.** Claude sums up what's in this update, what it's worth to a typical customer and to you, and the build-day slice.

## What you get

```
acme-scheduler/
  roadmap/
    features.md     the ideas, the features prioritised, this product update, and the build-day slice
    roi.md          what the update is worth to a typical customer and to you, and how you'll charge
    roadmap.md      Now (this update), Next and Later, toward your vision and BHAG
```

## Troubleshooting

- **Claude asks you to run another skill first.** The roadmap needs `flows/flows.md`.
- **You don't know the cost to build.** Give a rough range, or say so. Claude labels it as an assumption, and the ROI shows what would have to be true.
- **The panel won't pay.** Treat it as a signal to test with real customers, and look at what would change their mind.
- **You ran out of time.** Say so. Claude saves what's done and marks the rest "Not done yet". Run `/ai-product-roadmap` again later to finish.

## Tips

- Keep Now small. A thin update that makes one flow real beats a long list that makes none.
- Price agents well below the labour they save: the customer should win clearly.
- Keep the build-day slice end to end: a thin version of the whole flow beats a polished half.
