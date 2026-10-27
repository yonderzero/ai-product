---
name: ai-product-discovery
description: Third step, after ai-product-vision. A deeper check of whether the product is ready to go where the vision says. Scores four pillars with evidence (protection, strength, AI opportunity, exposure), adds the product manager's inside view, lets them overturn scores with evidence, checks what has to be true for the vision (data, tech, team, customers, pricing), places the product on AI opportunity against AI risk to choose its move, maps where value flows today and tomorrow, and sets a clear direction: what to protect, where to grow, which problem to start with. Writes protection.md, strength.md, exposure.md, value.md and discovery.md.
---

# ai-product-discovery

Is your product ready to go where the vision says? What protects it, how strong it is, how big the AI opportunity is, what could go wrong, what has to be true, and which move follows.

## How to talk

Conversational, short messages, one question at a time. Never send a list of questions. Don't explain what you're about to check; just do it. While research runs, keep talking with the product manager instead of going quiet. Name scores in plain English; never use codes like SC1 or A4 in what you say.

## Save as you go

Write each file as soon as its step has content, and update it as you go. Mark any section you haven't reached `Not done yet`. After every step that saves something, update `index.html`, the product's deck (follow `references/deck.md` in the ai-product-start skill's folder), so the deck always shows the latest. If the product manager says they're out of time or wants to move on, stop cleanly: save what's there, say which steps are left, and that they can run this skill again to continue, or edit the files themselves. Update `index.html` before you stop. Moving on is fine as long as something is saved.

## Before you start

Work in the product folder: the current folder, or the folder below it that has `product.md`. This skill's files go in `discovery/` inside it: `protection.md`, `strength.md`, `exposure.md`, `value.md` and `discovery.md` mean `discovery/<name>`. The vision skill's files are in `vision/`. `product.md` and `documents/` stay at the top. Create `discovery/` if it doesn't exist.

- No `product.md`, or it's empty: say in one line that the product profile comes first, ask them to run `/ai-product-start`, and stop.
- None of the vision files (`ai-levels.md`, `market-map.md`, `market-moves.md`, `opportunities.md`, `vision.md`): say in one line that discovery builds on the vision, ask them to run `/ai-product-vision` first, and stop. Any one of them is enough to go on.

Read `product.md`, `ai-levels.md`, `market-map.md`, `market-moves.md`, `opportunities.md`, `vision.md` and anything in `documents/` you haven't read yet.

If files from an earlier run exist (`protection.md`, `strength.md`, `exposure.md`, `value.md`, `discovery.md`), say which steps are done and which aren't (look for `Not done yet`), and ask whether to continue, redo a step, or start again. Read the files as they are now: the product manager may have edited them.

## Steps

1. **What this is.** Say which product you're working on, then explain in two or three sentences, your own words:

   > Your vision says where the product could go. Now we check whether it's ready: what protects it, how strong it is, how big the AI opportunity is, and what could go wrong. Then we look at what has to be true to reach the vision, and choose your move.

   Then ask: "Shall we start?" Wait for a yes.

2. **Research, in the background.** Start three subagents in parallel, and tell the product manager in one line that research is running. Pass each the full path of its folder, the product, company, website and industry from `product.md`, and the scope (which product, if the company has several). Each follows `instructions.md` in its folder, works in a scratch folder, and writes its report into `discovery/`:
   - **Protection:** `references/protection/` → `protection.md`. What protects the product: 24 levers in four groups (switching costs, domain knowledge, speed and cost of building, distribution).
   - **Strength and AI opportunity:** `references/strength/` → `strength.md`. Business quality, customer strength, and the AI opportunity.
   - **Exposure:** `references/exposure/` → `exposure.md`. 11 risks: the market, defensibility, and business health. 1 is safest, 5 most exposed.

   If subagents aren't available, run them one after the other, strength first, between questions.

3. **The inside view.** While research runs, ask the product manager what public sources can't show. One question at a time, skipping anything `product.md` or `documents/` already answers:
   1. How many customers do you keep each year? Why do the ones who leave, leave?
   2. How long does a new customer take to set up, and what makes it hard to switch away?
   3. Which other systems is the product connected to at your customers?
   4. What data do you hold about your customers' work, and do your contracts let you use it for AI, including across customers?
   5. How big is the team that builds the product, and how fast do you ship?
   6. What is the product built on, and what in it is old or hard to change?
   7. Who do you depend on: cloud, marketplaces, partners, resellers?
   8. Are customers pushing back on price, or asking for more for the same?
   9. Who decides on AI at your company, and how much appetite is there?

   Tag their answers `[PM]`. As each subagent finishes, send it the answers that bear on its scores (or rescore yourself with its rubric) so the inside view counts as evidence, and rerun its script.

4. **The scores.** When all three are back, compute the four pillars and the move with `references/compute_pillars.py` (`python3 compute_pillars.py --protection <protection composites.json> --strength <strength composites.json> --exposure <exposure composite.json> --output <scratch>/pillars.json`). Use its numbers; don't compute them by hand. It gives:
   - **Protection:** the moat composite.
   - **Strength:** the average of business quality and customer strength.
   - **AI opportunity:** the average of AI in the product today, revenue AI could earn, and work AI could take off customers. Urgency is left out because its scale is inverted (1 means immediate urgency) and would make a product under heavy AI pressure look like a smaller opportunity.
   - **AI urgency:** reported on its own, as how fast the product needs to move.
   - **Exposure:** the risk composite, which already counts AI disruption and its timing.

   Show the four pillars in one short table, with one line each on what it means, and say the urgency in plain words. Then, one at a time, show the two or three most important findings from each report.

5. **Overturn a score.** Ask: "Which score do you disagree with most?" Show its anchor from the rubric and the evidence it was based on. Ask for their evidence. If the evidence meets a different anchor, change the score, rerun its script and `compute_pillars.py`, and record the change and why, tagged `[PM]`. If it doesn't, say so plainly and keep the score. Then ask: "Any other?" Continue until they say no.

6. **Ready for the vision?** Take the furthest the vision got: the target level and starting opportunities in `vision.md`; if that isn't written yet, the top opportunities in `opportunities.md`; if not those, the next level up from `ai-levels.md`. Say which one you're using. Go through five areas, one at a time. For each, say what the reports and the inside view show, then ask what's missing:
   - **Data:** do we have the data the vision needs, and the rights to use it?
   - **Tech:** can the product's stack support it?
   - **Team:** do we have the skills and the capacity?
   - **Customers:** will they trust AI with this job, and change how they work?
   - **Pricing:** can we charge for the outcome, not just the seat?

   For each, write what we have, the gap, what must be true, and how we'll check it. Then name the strengths the vision builds on, and the risks that could stop it.

7. **Our move.** Take the move from `compute_pillars.py`: AI opportunity against exposure, with 3.0 as the line on both. If it marks a score as borderline (within 0.2 of the line), say so and ask the product manager which side it's on. Use the urgency to set the pace: with high or immediate urgency, say the move has to start now.
   - **Build on it:** higher opportunity, lower risk. Invest from strength.
   - **Move first:** higher opportunity, higher risk. Move before someone else does.
   - **Optimise:** lower opportunity, lower risk. Make the most of what's there.
   - **Defend:** lower opportunity, higher risk. Protect the core first.

   Propose the quadrant with one or two lines of reasoning, and ask: "Is that where you'd put it?" They confirm or move it; record why.

8. **Where value flows.** Draft it first from `product.md`, `vision/ai-levels.md`, `vision/opportunities.md`, `vision/market-moves.md` and the reports, then check it with the product manager one question at a time.
   - **Today:** for each persona, the value they get and who pays for it, for what (seat, module, add-on, usage) and roughly how much. Then where value leaks: work customers still do by hand or in spreadsheets around the product, value partners or other tools capture, and value the product creates but doesn't charge for.
   - **At the vision's target level:** the job AI does, who gets the value, what customers would pay for (the outcome, not the seat), and who else could capture that value: a general AI assistant, a challenger, a partner, the customer's own build. What keeps it with us: data, workflow, trust, distribution.

   Ask: "Where does most of the value go today, and where should it go tomorrow?" Fill `templates/value.md` into `value.md`, with the shift as one from → to line at the top, and how you'd charge today and tomorrow.

9. **Where to take the product.** Turn everything into one direction. Propose it, then ask the product manager to confirm or change each part, one at a time:
   - **Protect:** the core to defend, from protection and exposure.
   - **Grow:** one to three bets in and around the product, from the top opportunities and the vision, each with where its value comes from.
   - **Start with:** the first customer problem to go after, and what we need to learn about it before building anything. A problem, not a solution: if the product manager names a feature, ask which customer problem it solves and write that.
   - **Don't:** what not to spend on now, and why.
   - **How we'll know:** two or three signals that it's working, such as adoption, usage, retention or willingness to pay.

   The direction must fit the move: Build on it invests from strength, Move first goes fast on the bet, Optimise makes the most of the core, Defend protects the core before betting.

10. **One page.** Fill `templates/discovery.md` into `discovery.md`. Plain language, every claim with its source (a report, a link, `documents/`, or `[PM]`). Show the "In short", the move and the direction, and ask: "Is this right?"

11. **Update the profile.** In `product.md`, under `## AI today`, add one line: the move and the direction in a few words, pointing to `discovery.md`.

12. **The deck.** Update `index.html`, the product's deck: follow `references/deck.md` in the ai-product-start skill's folder (next to this skill's folder).

13. **Done.** Show the files you wrote and sum up in three lines: the move, where to take the product, and which problem to start with. Say the next step is `/ai-product-problem`.

## Done when

- `protection.md`, `strength.md` and `exposure.md` are written, each score with a source and computed by its script;
- the product manager's inside view is in the scores, tagged `[PM]`;
- at least one score was challenged, and changed or kept with the reason;
- `value.md` shows where value flows today, where it leaks, where it would flow at the vision's target level, who else could capture it, and how we'd charge;
- `discovery.md` has the four pillars, the readiness check for the vision, the move, where value flows today and tomorrow, and a direction the product manager confirmed: protect, grow, start with, don't, and how we'll know.
