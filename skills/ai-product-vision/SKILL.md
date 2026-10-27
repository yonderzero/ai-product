---
name: ai-product-vision
description: Second step, after ai-product-start. Interviews the product manager about the value the product gives customers at each of six levels of AI, from System of Record to System of Understanding, maps the market on the same levels, sees who's moving in the market, maps the work around the product and ranks the opportunities in and around it, then interviews the product manager one question at a time to write the product's AI vision. Writes ai-levels.md, market-map.md, market-map.html, market-moves.md, opportunities.md and vision.md in the product folder.
---

# ai-product-vision

What value does your product give customers at each level, from System of Record to System of Understanding, where is your market, where are the opportunities, and where do you want to take your product?

## How to talk

Conversational, short messages, one question at a time. Never send a list of questions. Don't explain what you're about to check; just do it. While research runs, keep talking with the product manager instead of going quiet.

## Save as you go

Write each file as soon as its step has content, and update it as you go. Mark any section you haven't reached `Not done yet`. If the product manager says they're out of time or wants to move on, stop cleanly: save what's there, say which steps are left, and that they can run this skill again to continue, or edit the files themselves. Moving on is fine as long as something is saved.

## Before you start

Work in the product folder: the current folder, or the folder below it that has `product.md`. If there is none, or it's empty, say in one line that the product profile comes first, ask them to run `/ai-product-start`, and stop. A partly filled `product.md` is enough to go on.

Read `product.md` and anything in `documents/` you haven't read yet. If files from an earlier run exist (`ai-levels.md`, `market-map.md`, `market-moves.md`, `opportunities.md`, `vision.md`), say which steps are done and which aren't (look for `Not done yet`), and ask whether to continue, redo a step, or start again. When continuing, skip the steps that are done, unless they ask to redo one. Read the files as they are now: the product manager may have edited them. Read `references/levels.md`: the six levels, the evidence each needs, and the placement rules. Apply them strictly.

## Steps

1. **What this is.** Say which product you're working on, then explain in two or three sentences, your own words:

   > Software is moving from recording the work to doing it. We'll go through six levels, from System of Record to System of Understanding, and look at what value your product gives customers at each one today. Then we'll map your market on the same levels, find the opportunities in and around your product, and create a vision for where you could take it.

   Then ask: "Shall we start?" Wait for a yes.

2. **The market.** From `product.md` and a quick search, propose 10–15 companies in three groups:
   - **incumbents**: established vendors in the same vertical, including direct competitors;
   - **AI-native challengers**: funded startups building the vertical's workflows with AI;
   - **horizontal players**: general platforms (ERP, CRM, productivity suites, AI assistants) that reach into the vertical.

   Show the list, short, and ask one question: "Who's missing?" Add their names.

3. **Research, in the background.** Start these as parallel subagents, and tell the product manager in one line that research is running:
   - **Level map:** split the companies into batches of 3–5, one subagent per batch. For each company: find its AI features from product pages, docs, release notes, pricing pages, case studies and credible press from the last 18 months; place each feature at a level with the source URL, shipped / beta / announced, and confidence; place the company at the highest level it has shipped with evidence of use; add one line on where it's heading (announcements count here, labelled as such). Skip a company rather than guess. Pass each subagent the full path of `references/levels.md`.
   - **Market moves:** one subagent that researches the five ways others move into a market, following the research and evidence rules in `references/threat-scan.md` and `references/threat-framework-spec.md` (phases 1 and 2 only: research, then seen / early signs / not seen, never inventing a name). It fills `templates/market-moves.md` into `market-moves.md` in the product folder, in plain, constructive language: what others are doing and what it opens up for the product. No score and no hypothetical scenarios. Pass it the full paths of the three files, and the product, company, website and industry from `product.md`, so it doesn't need to ask.

   - **The work around the product:** one subagent that researches the customers' work step by step, following section 1 of `references/opportunities.md` (pass its full path): job postings for the personas' roles, reviews and complaints (G2, Capterra, app stores, forums), the customers' own words, and rules or deadlines that create new work. It returns findings with sources, especially manual work, for step 6.

   If subagents aren't available, do the same work yourself, one batch at a time, between questions.

4. **Your product, level by level.** While research runs, go up the levels with the product manager, from 1. For each level, say in two lines what it means and its main characteristics (from `references/level-examples.md`), then ask one question at a time:
   - Does the product give customers value at this level? Which features or functionality?
   - For whom: which persona from `product.md`, buyer or user?
   - What value does it give them: what do they get done, save or avoid?
   - How do they pay for it: included in the base price, an add-on, per seat, per use, per outcome?
   - Is it shipped and used? By how many customers, roughly, and is there an example?

   Start from what `product.md`, the website and `documents/` already say: confirm it rather than ask from scratch. Level 1 always applies to some degree; get the core records and workflows the product owns and what customers pay for them.

   When the answer at a level is "nothing", ask once whether anything is in beta or planned, note it as such, and ask whether to look at the next level or stop. Tag their answers `[PM]`.

   Fill `templates/ai-levels.md` into `ai-levels.md` in the product folder as you go. The product's level today is the highest level with value that is shipped and used; beta and planned don't count. Show the summary and ask: "Is this right?"

5. **The map.** When the research is back:
   - place the product with the same rules as everyone else, using `ai-levels.md` and the public evidence. Don't round up. If the public evidence puts it lower than `ai-levels.md` does, say so plainly and show why; write both;
   - add any companies named in `market-moves.md` to the map if they're missing;
   - name the openings: the empty or thin levels, and the challengers moving up fastest;
   - fill `templates/market-map.md` into `market-map.md` in the product folder;
   - copy `templates/market-map.html` to `market-map.html` in the product folder and replace only the JSON inside `<script id="data">` with the companies, their levels and groups, and the product (`"us": true`). Don't change the rest of the file.

   Show the result in a few lines: where the product is, who is a level above it, who's moving fastest, and the openings. Tell them to open `market-map.html` in a browser.

6. **The work around your product.** Read `references/opportunities.md`. Draft the customer's work as 6–10 steps, from what the research, `product.md` and `documents/` show, and walk the product manager through it one step at a time, asking only what you can't fill:
   - Is this step right? What's missing?
   - Who does it, and what's still done by hand, in email or in spreadsheets?
   - Which software runs it today: yours, someone else's, nothing?

7. **The opportunities.** Find up to 8 opportunities in and around the product, following `references/opportunities.md`: grow the base and new revenue, each specific, on evidence, at a level, rated, ranked and sized where the numbers allow. Fill `templates/opportunities.md` into `opportunities.md` in the product folder. Show the ranked table, short, and ask one question at a time:
   - Which of these excite you most?
   - Is anything missing that you've heard from customers?
   - Is any rating wrong?

   Update the file with their answers, tagged `[PM]`.

8. **Imagine.** Now help the product manager picture the future, beyond what the evidence shows today. This is the creative part: be concrete and vivid, and specific to their product, personas and data. Read `references/level-examples.md`.

   For each level above the product's level today, up to 6, one message per level:
   - name the level, give its main characteristics in two lines, and show two real products already there, one line each;
   - sketch **their product at this level** in three or four lines: what it does, for which persona, what changes in their day, and how customers would pay;
   - ask one question: "What would you add or change?"

   Then the System of Understanding. Write a short day in the life of their main persona, five years from now, with the product at level 6: what it knows that nobody knows today, what it does before anyone asks, what the persona never does again, and what they spend their time on instead. Then ask, one at a time:
   - What excites you in this? What feels wrong?
   - What would it need to know that it doesn't know today?
   - What data would that take, and who has it?
   - If this were real, what would customers pay for?

   Note what they say, tagged `[PM]`. Ideas that come up here can become new opportunities: add them to `opportunities.md` with evidence "Assumption".

9. **The vision interview.** One question at a time, following up on vague answers and asking for examples. Skip what's already answered.
   1. Which of the top opportunities should the vision start with, on the way to the future you just pictured?
   2. Looking at the map, which level do you want the product to reach, and by when?
   3. For which persona? What changes in their day? (Offer the personas from `product.md`.)
   4. What do you have that others on the map don't: data, domain knowledge, customers, distribution?
   5. If an agent sat on top of your data tomorrow, what would customers stop paying you for? What would they pay for instead?
   6. Who on the map is moving closest to this vision, and what makes yours different?
   7. What's the smallest thing you could build or test next to see if this is right?

10. **The vision.** Fill `templates/vision.md` into `vision.md` in the product folder, in their words where you can. Every claim about the market cites `market-map.md`, `market-moves.md` or `opportunities.md`; every claim about the product cites `ai-levels.md`, `product.md`, a file in `documents/`, or `[PM]`. Show the vision paragraph and ask: "Is this right?" Revise until they say yes.

11. **Update the profile.** In `product.md`, under `## AI today`, add one line: today's level and the target level, pointing to `ai-levels.md` and `vision.md`.

12. **Done.** Show the files you wrote and sum up in four lines: where the product is today, the top opportunity, where it's going, and the first step. Say the next step is `/ai-product-discovery`. End with: "Placements are a snapshot from public sources on [date]. Check the ones you act on."

## Done when

- at least ten companies placed, each with a source, or listed as not placed with the reason;
- `ai-levels.md` has the product's value at each level (features, for whom, value, how they pay), checked by the product manager;
- the product placed on the market map with the same rules as everyone else;
- `market-moves.md` covers the five ways in, each seen, early signs or not seen, with sources;
- at least one opening named;
- `opportunities.md` maps the work around the product and ranks the opportunities, each on evidence, with a first question;
- `vision.md` has the pictures of the product at higher levels and a System of Understanding day in the life, and a vision the product manager said yes to, built on named opportunities, with a target level, the persona, and a first step.
