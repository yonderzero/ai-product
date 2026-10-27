---
name: 04-harvest
description: Product Track session 04 workshop (Problem Definition & Opportunity Framing). Mine the team's own data and the market for problems, build a tagged long list of ten or more including the idea they came in with, and rewrite the best five in save or earn shape. Writes 04a-from-our-data.md, 04b-gaps.md and 04-long-list.md.
---

# 04 · Harvest

**Goal.** A long list of at least ten problems worth money, from the team's own data first and the market second, with the best five written so an outsider understands them and could count them.

Work in the team's product folder. Read `product.md`, `inputs/` (including `idea.md`) and `handoff/domain-read.md`.

## Steps

1. **Mine both sources at once.** Launch two subagents in parallel:
   - one reads every file in `inputs/` and lists every problem customers mention: who has it, how often, what it costs them, and where it was found (file and line), grouping duplicates. It saves `04a-from-our-data.md`.
   - one uses the `product-gaps` skill on the product and saves `04b-gaps.md`.

   If `inputs/` is thin, say so, and ask the team what support, sales and implementation hear most often; tag it `[team]`.

2. **The long list.** Fill `templates/04-long-list.md` into `04-long-list.md` from both files and `handoff/domain-read.md`. At least ten rows. The incoming idea from `inputs/idea.md` is one row. Tag each row with who has it, how often, what it costs today, save or earn, and its source. Then ask the team what's missing and add it.

3. **Shape the top five.** With the team, pick the five strongest and rewrite each in one of the two shapes:
   - *Save:* [Who] spends [time or money] on [what], because [why]. If it were solved, [what would change].
   - *Earn:* [Who] would pay [how much] for [what], because [why]. Today we can't offer it, because [what is missing].

   If a bracket can't be filled, leave it visible and say what the team would need to find out. Don't invent the number.

## Done when

- [ ] ten or more tagged problems, each with a source
- [ ] the incoming idea on the list
- [ ] five in shape

Finish with the checklist and: "Next session: `/product-track:05-build-your-customers`."
