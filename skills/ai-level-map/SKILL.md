---
name: ai-level-map
description: Map a vertical software market onto six levels of AI maturity (System of Record, AI Assisted, AI Directed, AI Delegated, AI Domain Intelligence, System of Understanding). Researches incumbents, AI-native startups and horizontal players in the product's vertical, places each company's AI features at a level with sourced evidence, places the team's own product with the same rules, and draws the market on the curve. Use to see who is doing what at which level, and where the openings are.
---

# AI level map

Who in this market is doing what with AI, and at which level? The output is a table, a picture of the market on the curve, and the openings: levels where nobody credible is yet.

Read `references/levels.md` first. It defines the six levels, the evidence each needs, and the placement rules. Use them strictly.

## Inputs

The product, its website and its vertical (from `product.md` if it exists, otherwise ask). If `01-brief.md` exists, read its competitors and alternatives.

## Steps

1. **Scope the market.** Name the vertical and the workflow the product owns, in one line. List who to research, about 10–15 companies, in three groups:
   - **incumbents**: established vendors in the same vertical, including the team's direct competitors;
   - **AI-native challengers**: funded startups attacking the vertical's workflows with AI;
   - **horizontal players**: general platforms (ERP, CRM, productivity suites, AI assistants) that reach into the vertical.

   Show the list to the team and ask what's missing. Add their names.

2. **Research in parallel.** Split the list into batches of 3–5 and run one subagent per batch. Each subagent, for each company:
   - finds its AI features from product pages, docs, release notes, pricing pages, case studies and credible press, within the last 18 months;
   - places each feature at a level, with the source URL, shipped / beta / announced, and confidence;
   - places the company at the highest level it has shipped with evidence of use;
   - notes one line on where it's heading (announcements count here, labelled as such).

   If subagents aren't available, research one batch at a time. Skip a company rather than guess.

3. **Place the team's product.** Apply the same rules, using the brief and anything the team tells you. Tag the team's input `[team]`. Don't round up.

4. **Find the openings.** For each level, who's there with high confidence? Name the empty or thin levels, the challengers moving up fastest, and the level where the team could lead.

5. **Write it up.**
   - Fill `templates/ai-market-map.md` into the output file (default `02-ai-market-map.md`).
   - Copy `templates/ai-market-map.html` to the same name with `.html`, and replace only the JSON inside `<script id="data">` with the companies, their levels and groups, and the team's product (`"us": true`). Don't change the rest of the file. Tell the team to open it in a browser.

## Done when

- every company placed has a source for its level, or is listed as "not placed" with the reason;
- the team's product is placed with the same rules;
- at least one opening is named.

End with: "Placements are a snapshot from public sources on [date]. Check the ones you act on."
