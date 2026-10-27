---
name: 03-read-the-domain
description: Product Track session 03 workshop (Assessing Intelligence Maturity). Score the product's moat, maturity and risk in parallel, have the team overturn one score with evidence, and merge sessions 01–03 into a one-page domain read for the developers. Writes 03a-maturity.md, 03b-risk.md, 03c-moat.md and handoff/domain-read.md.
---

# 03 · Read the domain

**Goal.** One page the developers can read in two minutes: where the product is strong, where it's exposed, and where the AI opportunity sits. It is the first file in the handoff.

Work in the team's product folder: the current folder, or the folder below it that has `product.md`. If there is none, run `/ai-product:ai-product-setup` first. Remind the team they can add files to `documents/` at any time, and read any new ones. Read `product.md`, `01-brief.md`, `02-ai-market-map.md` and `02b-threats.md`.

## Steps

1. **Run all three at once.** Launch three subagents in parallel:
   - one uses the `maturity-score` skill on the product and saves `03a-maturity.md`;
   - one uses the `risk-score` skill on the product and saves `03b-risk.md`;
   - one uses the `moat-scan` skill on the product and saves `03c-moat.md`.

   If subagents aren't available, run them one after the other, maturity first. Split the team across the three, each reading against the anchors.

2. **Overturn one score.** Ask the team which score they disagree with most. Show its anchor and the evidence it was based on. Ask for their evidence, change the score, and add one line on why, tagged `[human]`.

3. **One page.** Fill `templates/domain-read.md` into `handoff/domain-read.md` from `01-brief.md`, `02-ai-market-map.md`, `02b-threats.md`, `03a-maturity.md`, `03b-risk.md` and `03c-moat.md`. Include where the product sits on the six AI levels. Plain language, every claim with its source, one screen long.

4. **Place the product.** Propose where it sits on AI opportunity against AI risk, with one line of reasoning. The team confirms or moves it.

## Done when

- [ ] one score overturned with evidence, tagged `[human]`
- [ ] `handoff/domain-read.md` fits on one screen
- [ ] the product's place on the grid, confirmed by the team

Finish with the checklist and: "Next session: `/ai-product:04-harvest`."
