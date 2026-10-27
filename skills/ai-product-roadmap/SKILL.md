---
name: ai-product-roadmap
description: Seventh step, after ai-product-flows. Ideation, prioritisation, ROI and pricing - turns the right flows into feature ideas, prioritises them on value, pay, confidence and effort, works out the ROI for customers and for the product (from the double-cost economics), chooses how to charge for agents, and lays out the roadmap (Now / Next / Later) with the clear features in this product update and the build-day slice for developers. Writes roadmap/ (features.md, roi.md, roadmap.md).
---

# ai-product-roadmap

What goes into this product update, what's it worth, and how do we charge for it? Generate feature ideas from the right flows, prioritise them, work out the ROI and the price, and lay out the roadmap from this update to the BHAG.

## How to talk

Conversational, short messages, one question at a time. Never send a list of questions. Don't explain what you're about to do; just do it. While subagents run, keep talking with the product manager.

## Save as you go

Write each file as soon as its step has content, and update it as you go. Mark any section you haven't reached `Not done yet`. After every step that saves something, update `index.html`, the product's deck (follow `references/deck.md` in the ai-product-start skill's folder), so the deck always shows the latest. If the product manager says they're out of time or wants to move on, stop cleanly: save what's there, say which steps are left, and that they can run this skill again to continue, or edit the files themselves. Moving on is fine as long as something is saved.

## Before you start

Work in the product folder: the current folder, or the folder below it that has `product.md`. This skill's files go in `roadmap/` inside it: `features.md`, `roi.md` and `roadmap.md` mean `roadmap/<name>`. The other skills' files are in `vision/`, `discovery/`, `problem/`, `research/` and `flows/`. `product.md` and `documents/` stay at the top. Create `roadmap/` if it doesn't exist.

- No `product.md`, or it's empty: say in one line that the product profile comes first, ask them to run `/ai-product-start`, and stop.
- No `flows/flows.md`: say in one line that the roadmap builds on the right flows, ask them to run `/ai-product-flows`, and stop. Anything saved there is enough to go on.

Read `product.md`, `problem/problem.md`, `flows/` (above all the flows taken forward), `research/experiences.md` (the double cost and the new economics), `research/personas/`, `discovery/value.md` and `discovery/discovery.md`, `vision/vision.md` and `vision/opportunities.md` where they exist, and anything new in `documents/`.

If files from an earlier run exist, say which steps are done and which aren't (look for `Not done yet`), and ask whether to continue, redo a step, or start again.

## Steps

1. **What this is.** Say which product and which flows you're working on, then explain in two or three sentences, your own words:

   > Now we decide what goes into this product update. We generate feature ideas from your right flows, prioritise them, work out what they're worth to your customers and to you, choose how to charge for the agents, and lay out the roadmap from this update to your BHAG.

   Then ask: "Shall we start?" Wait for a yes.

2. **Ideation.** For each flow taken forward, go moment by moment and generate feature ideas: what the agent needs to be able to do, what the person sees and controls (summary of the agent's work, approvals, exceptions, "why the agent did this", undo, guardrails), and the data it needs. Add ideas from the opportunities, the Imagine section, what real customers and the panel asked for in `flows/panel-tests.md`, and the product manager. Ask: "What else would make this flow great for [persona]?" and "What could we leave out and still show the whole flow?" Merge duplicates. Fill the ideas table in `templates/features.md` into `features.md`.

3. **Prioritise.** For each feature, fill value (hours given back and how much customers want it, real customers first, then the panel), pay, confidence (the evidence grade) and effort (agree it with the product manager: "How hard is this to build, on data you hold today?"). Compute the priority with the formula in the template and show the working. Sort, and propose the horizon for each: Now for this product update, Next, Later. Show the ranked list and ask: "Does this order feel right? What would you move?"

4. **ROI.** Fill `templates/roi.md` into `roi.md`:
   - **for a typical customer:** today against with this update, using the double cost and the new economics in `research/experiences.md`, updated for the features in Now: licence, agents, people's time; what they save; their return on what they pay for agents;
   - **for us:** new agent revenue per customer and across the customers who'd buy (base × share, measured or labelled), against the cost to build and run the update. Ask the product manager for the cost: "Roughly what would this update cost to build and run?" Label what's assumed.

   Follow the sizing rules in the ai-product-vision skill's `references/opportunities.md`: at least one measured number, at most two labelled assumptions per figure, the working shown.

5. **Pricing.** Walk through the ways to charge for agents (per outcome, per agent, usage, a tier) with the fit and the risk of each for this product. Run a price vote with the personas: each in its own subagent, sceptic first, answers the four Van Westendorp questions for the update as described (see the ai-product-research skill), marked **synthetic vote**. Add what real customers said. Check the price against the labour it saves (a price well below the saving is easy to defend). Ask: "How do you want to charge, and at what price?" Record the choice and what would change it.

6. **The roadmap.** Fill `templates/roadmap.md` into `roadmap.md`, in three horizons, Now, Next and Later, without dates:
   - **Now** is this product update: the clear features, the flow they make real, the outcome for customers, the hours given back, the price, the new revenue, and how we'll know it worked;
   - **Next** and **Later** climb the AI levels toward the vision (`vision/vision.md`) and the BHAG (`problem/problem.md`), with the other flows and features;
   - for each horizon, what we must learn first.

   Walk through it one horizon at a time and ask what to change. Add what's not on the roadmap, and why.

7. **This product update.** Finish `features.md`: the clear list of features in Now, and **the build-day slice**: the smallest end-to-end slice of the update that developers can build first to make the flow real and testable, with what's in, what's out for now, and when it's done. Ask: "Is this the update you want to put in front of your developers?"

8. **Update the profile.** In `product.md`, under `## The idea we have in mind`, add one line: this product update in a few words, its price, and the build-day slice, pointing to `roadmap/roadmap.md`.

9. **The deck.** Update `index.html`, the product's deck: follow `references/deck.md` in the ai-product-start skill's folder (next to this skill's folder).

10. **Done.** Show the files you wrote and sum up in three lines: what's in this product update, what it's worth to a typical customer and to you, and the build-day slice.

## Done when

- `features.md` has the ideas, the features prioritised with the working shown, the features in this product update, and the build-day slice;
- `roi.md` has the ROI for a typical customer and for us, with the working, and the pricing choice with the panel's vote and what real customers said;
- `roadmap.md` has Now (this update), Next and Later, toward the vision and the BHAG, without dates.
