---
name: ai-product-vision
description: Second step, after ai-product-start. Maps the product's market onto six levels of AI, from System of Record to System of Understanding, places the product honestly, finds who could overtake it, then interviews the product manager one question at a time to write the product's AI vision. Writes market-map.md, market-map.html, threats.md and vision.md in the product folder.
---

# ai-product-vision

Where is your market on the road from System of Record to System of Understanding, where is your product, who could overtake it, and where do you want to take it?

## How to talk

Conversational, short messages, one question at a time. Never send a list of questions. Don't explain what you're about to check; just do it. While research runs, keep talking with the product manager instead of going quiet.

## Before you start

Work in the product folder: the current folder, or the folder below it that has `product.md`. If there is none, say so in one line and ask them to run `/ai-product:ai-product-start` first.

Read `product.md` and anything in `documents/` you haven't read yet. Read `references/levels.md`: the six levels, the evidence each needs, and the placement rules. Apply them strictly.

## Steps

1. **What this is.** Say which product you're working on, then explain in two or three sentences, your own words:

   > Software is moving from recording the work to doing it. We'll map your market on six levels, from System of Record to System of Understanding, see where your product really is and who could overtake you, and then write where you want to take it: your product's AI vision.

   Then ask: "Shall we start?" Wait for a yes.

2. **The market.** From `product.md` and a quick search, propose 10–15 companies in three groups:
   - **incumbents**: established vendors in the same vertical, including direct competitors;
   - **AI-native challengers**: funded startups attacking the vertical's workflows with AI;
   - **horizontal players**: general platforms (ERP, CRM, productivity suites, AI assistants) that reach into the vertical.

   Show the list, short, and ask one question: "Who's missing?" Add their names.

3. **Research, in the background.** Start these as parallel subagents, and tell the product manager in one line that research is running:
   - **Level map:** split the companies into batches of 3–5, one subagent per batch. For each company: find its AI features from product pages, docs, release notes, pricing pages, case studies and credible press from the last 18 months; place each feature at a level with the source URL, shipped / beta / announced, and confidence; place the company at the highest level it has shipped with evidence of use; add one line on where it's heading (announcements count here, labelled as such). Skip a company rather than guess. Pass each subagent the full path of `references/levels.md`.
   - **Threats:** one subagent that follows `references/threat-scan.md` and `references/threat-framework-spec.md` (pass both full paths) and writes `threats.md` in the product folder. Give it the product, company, website and industry from `product.md`, so it doesn't need to ask.

   If subagents aren't available, do the same work yourself, one batch at a time, between questions.

4. **Where are you today?** While research runs, show the six levels in one short line each, and ask: "Where do you think your product sits today?" Then ask why, with an example of a customer using the AI feature that puts it there. Note their answer as `[PM]`.

5. **The map.** When the research is back:
   - place the product with the same rules as everyone else. Don't round up. If the evidence puts it lower than the product manager did, say so plainly and show why; write both;
   - add any named attackers from `threats.md` to the map if they're missing, and mark which level they attack from;
   - name the openings: the empty or thin levels, and the challengers moving up fastest;
   - fill `templates/market-map.md` into `market-map.md` in the product folder;
   - copy `templates/market-map.html` to `market-map.html` in the product folder and replace only the JSON inside `<script id="data">` with the companies, their levels and groups, and the product (`"us": true`). Don't change the rest of the file.

   Show the result in a few lines: where the product is, who is a level above it, the most credible attacker, and the openings. Tell them to open `market-map.html` in a browser.

6. **The vision interview.** One question at a time, following up on vague answers and asking for examples. Skip what's already answered.
   1. Looking at the map, which level do you want the product to reach, and by when?
   2. Which workflow should AI take over first, end to end? (Offer the main workflows from `product.md`.)
   3. For which persona? What changes in their day? (Offer the personas from `product.md`.)
   4. What do you have that others on the map don't: data, domain knowledge, customers, distribution?
   5. If an agent sat on top of your data tomorrow, what would customers stop paying you for? What would they pay for instead?
   6. Who on the map worries you most, and how does this vision answer them?
   7. What's the smallest thing you could build or test next to see if this is right?

7. **The vision.** Fill `templates/vision.md` into `vision.md` in the product folder, in their words where you can. Every claim about the market cites `market-map.md` or `threats.md`; every claim about the product cites `product.md`, a file in `documents/`, or `[PM]`. Show the vision paragraph and ask: "Is this right?" Revise until they say yes.

8. **Update the profile.** In `product.md`, under `## AI today`, add one line: today's level and the target level, pointing to `vision.md`.

9. **Done.** Show the files you wrote and sum up in three lines: where the product is today, where it's going, and the first step. End with: "Placements are a snapshot from public sources on [date]. Check the ones you act on."

## Done when

- at least ten companies placed, each with a source, or listed as not placed with the reason;
- the product placed with the same rules, and the product manager's own view written beside it;
- `threats.md` names the most credible attacker, or says plainly that none was found;
- at least one opening named;
- `vision.md` has a vision the product manager said yes to, a target level, the persona, the workflow, and a first step.
