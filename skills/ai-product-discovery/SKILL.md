---
name: ai-product-discovery
description: Third step, after ai-product-vision. A deeper check of whether the product is ready to go where the vision says. Scores four pillars with evidence (protection, strength, AI opportunity, exposure), adds the product manager's inside view, lets them overturn scores with evidence, checks what has to be true for the vision (data, tech, team, customers, pricing), and places the product on AI opportunity against AI risk to choose its move. Writes protection.md, strength.md, exposure.md and discovery.md.
---

# ai-product-discovery

Is your product ready to go where the vision says? What protects it, how strong it is, how big the AI opportunity is, what could go wrong, what has to be true, and which move follows.

## How to talk

Conversational, short messages, one question at a time. Never send a list of questions. Don't explain what you're about to check; just do it. While research runs, keep talking with the product manager instead of going quiet. Name scores in plain English; never use codes like SC1 or A4 in what you say.

## Before you start

Work in the product folder: the current folder, or the folder below it that has `product.md`.

- No `product.md`: say in one line that the product profile isn't done yet, ask them to run `/ai-product-start` first, and stop.
- No `vision.md`: say in one line that discovery checks the product against its vision, ask them to run `/ai-product-vision` first, and stop.

Read `product.md`, `ai-levels.md`, `market-map.md`, `market-moves.md`, `opportunities.md`, `vision.md` and anything in `documents/` you haven't read yet.

If files from an earlier run exist (`protection.md`, `strength.md`, `exposure.md`, `discovery.md`), say which steps are done and ask whether to continue from where they stopped or start again.

## Steps

1. **What this is.** Say which product you're working on, then explain in two or three sentences, your own words:

   > Your vision says where the product could go. Now we check whether it's ready: what protects it, how strong it is, how big the AI opportunity is, and what could go wrong. Then we look at what has to be true to reach the vision, and choose your move.

   Then ask: "Shall we start?" Wait for a yes.

2. **Research, in the background.** Start three subagents in parallel, and tell the product manager in one line that research is running. Pass each the full path of its folder, the product, company, website and industry from `product.md`, and the scope (which product, if the company has several). Each follows `instructions.md` in its folder, works in a scratch folder, and writes its report into the product folder:
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

4. **The scores.** When all three are back, show the four pillars in one short table: score, and one line on what it means. Protection is the moat composite; strength is the business quality and customer strength sections; AI opportunity is the AI opportunity section; exposure is the risk composite. Then, one at a time, show the two or three most important findings from each report.

5. **Overturn a score.** Ask: "Which score do you disagree with most?" Show its anchor from the rubric and the evidence it was based on. Ask for their evidence. If the evidence meets a different anchor, change the score, rerun the script, and record the change and why, tagged `[PM]`. If it doesn't, say so plainly and keep the score. Then ask: "Any other?" Continue until they say no.

6. **Ready for the vision?** Take the vision's target level and the opportunities it starts with (`vision.md`, `opportunities.md`). Go through five areas, one at a time. For each, say what the reports and the inside view show, then ask what's missing:
   - **Data:** do we have the data the vision needs, and the rights to use it?
   - **Tech:** can the product's stack support it?
   - **Team:** do we have the skills and the capacity?
   - **Customers:** will they trust AI with this job, and change how they work?
   - **Pricing:** can we charge for the outcome, not just the seat?

   For each, write what we have, the gap, what must be true, and how we'll check it. Then name the strengths the vision builds on, and the risks that could stop it.

7. **Our move.** Place the product on AI opportunity (the AI opportunity section score) against AI risk (the exposure composite). 3.0 is the line on both; if a score is within 0.2 of it, say it's borderline and ask the product manager which side it's on.
   - **Build on it:** higher opportunity, lower risk. Invest from strength.
   - **Move first:** higher opportunity, higher risk. Move before someone else does.
   - **Optimise:** lower opportunity, lower risk. Make the most of what's there.
   - **Defend:** lower opportunity, higher risk. Protect the core first.

   Propose the quadrant with one or two lines of reasoning, and ask: "Is that where you'd put it?" They confirm or move it; record why.

8. **One page.** Fill `templates/discovery.md` into `discovery.md` in the product folder. Plain language, every claim with its source (a report, a link, `documents/`, or `[PM]`). End with three next steps that follow from the move and the gaps. Show the "In short" and the move, and ask: "Is this right?"

9. **Update the profile.** In `product.md`, under `## AI today`, add one line: the move, pointing to `discovery.md`.

10. **Done.** Show the files you wrote and sum up in three lines: the move, the biggest gap to the vision, and the first next step.

## Done when

- `protection.md`, `strength.md` and `exposure.md` are written, each score with a source and computed by its script;
- the product manager's inside view is in the scores, tagged `[PM]`;
- at least one score was challenged, and changed or kept with the reason;
- `discovery.md` has the four pillars, the readiness check for the vision with what must be true and how to check it, the move the product manager confirmed, and three next steps.
