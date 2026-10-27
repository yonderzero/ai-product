# ai-product-discovery

```
/ai-product-discovery
```

The third skill, after [`ai-product-vision`](ai-product-vision.md). Your vision says where your product could go. Discovery checks whether it's ready: what protects it, how strong it is, how big the AI opportunity is, and what could go wrong. Then it looks at what has to be true to reach the vision, maps where value flows today and tomorrow, and ends with a clear direction: what to protect, where to grow, which problem to start with, and what not to do.

It goes deeper than the vision in two ways: it adds your inside knowledge, which public research can't see, and it tests the vision against what it would take.

**Who runs it:** the product manager, ideally with someone who knows the numbers and the tech.
**Run it:** in the folder that holds your product's folder.
**You leave with:** your product scored on four pillars, a readiness check for your vision, your move, where value flows, and where to take the product.

## Before you begin

- **Your product profile and some of your vision.** Run [`/ai-product-start`](ai-product-start.md) and [`/ai-product-vision`](ai-product-vision.md) first. Neither has to be finished: discovery needs a `product.md` and at least one file from the vision skill. The readiness check uses the furthest your vision got: `vision.md`, else your top opportunities, else your AI levels.
- **The same folder.** In the Claude desktop app, pick the folder that holds your product's folder with **Project or folder**. In Claude Code, start Claude there.
- **Web search.** The scores are researched on the web.
- **Some numbers, if you have them:** retention, implementation time, team size. Rough figures are fine.

## The four pillars

Each pillar is scored 1–5 against a fixed rubric, with a source for every score. Scripts do the arithmetic, including the four pillars and your move.

| Pillar | The question | What's scored |
|---|---|---|
| **Protection** | What protects your product? | 24 levers in four groups: switching costs, domain knowledge, speed and cost of building, and distribution. It also shows which are eroding fastest because of AI. |
| **Strength** | How strong is the product and its customer base? | Business quality: where it sits in your customers' operations, how vertical and how critical it is, its competitive standing, leadership, and tech stack. Customer strength: how embedded it is, and how loyal customers are. |
| **AI opportunity** | How big is the AI prize? | AI in the product today, revenue AI could earn, and work AI could take off customers. **How urgent it is** is shown separately, as how fast you need to move. |
| **Exposure** | What could go wrong? | 11 risks in three groups: the market (AI disruption, growth, regulation), defensibility (dependence on partners, lock-in, substitution, timing), and business health (price pressure, trust, ageing tech). 1 is safest, 5 most exposed. |

## Your move

Your product is placed on AI opportunity against AI risk:

| | Lower risk | Higher risk |
|---|---|---|
| **Higher AI opportunity** | **Build on it**: invest from strength | **Move first**: move before someone else does |
| **Lower AI opportunity** | **Optimise**: make the most of what's there | **Defend**: protect the core first |

3.0 is the line on both scores. If your product is close to the line, Claude asks you which side it's on.

## What happens

Claude asks one question at a time, like a conversation.

1. **What this is.** Claude names your product, explains discovery in a few sentences, and asks: "Shall we start?"

2. **Research.** Claude scores protection, strength and AI opportunity, and exposure in the background, with sources.

3. **The inside view.** While the research runs, Claude asks what only you know, one question at a time:
   - how many customers you keep each year, and why the ones who leave, leave;
   - how long setup takes, and what makes it hard to switch away;
   - which other systems the product is connected to;
   - what data you hold, and whether your contracts let you use it for AI;
   - how big the team is, and how fast you ship;
   - what the product is built on, and what's old or hard to change;
   - who you depend on: cloud, marketplaces, partners;
   - whether customers push back on price;
   - who decides on AI at your company, and how much appetite there is.

   Your answers count as evidence in the scores, tagged `[PM]`.

4. **The scores.** Claude shows the four pillars, then the most important findings from each.

5. **Overturn a score.** Claude asks which score you disagree with most, shows what it was based on, and asks for your evidence. If your evidence meets a different level of the rubric, the score changes and the reason is written down. If not, Claude says so and keeps it. You can challenge as many as you like.

6. **Ready for the vision?** For your vision's target level and the opportunities it starts with (or, if your vision isn't finished, your top opportunities), Claude goes through five areas one at a time: **data** (do you have it, and the rights?), **tech**, **team**, **customers** (will they trust AI with the job?) and **pricing** (can you charge for outcomes?). For each: what you have, the gap, what must be true, and how you'll check it.

7. **Your move.** Claude places your product on the grid, explains why, and asks if that's where you'd put it.

8. **Where value flows.** Claude drafts it from everything so far, then checks it with you, one question at a time:
   - **today:** for each persona, the value they get, who pays, for what and roughly how much, and where value leaks: manual work and spreadsheets around the product, partners, other tools, or value you don't charge for;
   - **at your vision's target level:** the job AI does, who gets the value, what customers would pay for (the outcome, not the seat), who else could capture it, and what keeps it with you.

   It asks: "Where does most of the value go today, and where should it go tomorrow?", and writes `value.md`, including how you'd charge today and tomorrow.

9. **Where to take the product.** Claude turns everything into one direction, and you confirm or change each part:
   - **Protect:** the core to defend.
   - **Grow:** one to three bets in and around the product, each with where its value comes from.
   - **Start with:** the first customer problem to go after, and what you need to learn about it before building anything. Think first, then build.
   - **Don't:** what not to spend on now, and why.
   - **How we'll know:** two or three signals that it's working.

   The direction fits your move: Build on it invests from strength, Move first goes fast on the bet, Optimise makes the most of the core, Defend protects the core before betting.

10. **One page.** Claude writes `discovery.md` and asks: "Is this right?"

11. **The deck.** Claude adds the direction, the four pillars, your move, where value flows and the readiness check to `index.html`, and opens it in the preview.

12. **Done.** Claude adds your move and direction to `product.md` and sums up: the move, where to take the product, and which problem to start with. Next: [`/ai-product-problem`](ai-product-problem.md).

## What you get

See finished ones in [the Salesforce example](../examples/salesforce/discovery/): [`discovery.md`](../examples/salesforce/discovery/discovery.md), [`value.md`](../examples/salesforce/discovery/value.md), [`protection.md`](../examples/salesforce/discovery/protection.md), [`strength.md`](../examples/salesforce/discovery/strength.md) and [`exposure.md`](../examples/salesforce/discovery/exposure.md), and the whole deck in [`index.html`](../examples/salesforce/index.html). It's illustrative, built from public sources.

```
acme-scheduler/
  product.md       now with your move
  discovery/
    protection.md    what protects your product: 24 levers, scored, with sources
    strength.md      business quality, customer strength and the AI opportunity, scored, with sources
    exposure.md      11 risks, scored, with sources
    value.md         where value flows today, where it leaks, where it would flow tomorrow, and how you'd charge
    discovery.md     the one page: where to take the product, four pillars, your move, readiness for the vision
```

`discovery.md` holds:

| Section | What's in it |
|---|---|
| In short | Where you're strong, where you're exposed, the move, and where to take the product |
| Where to take the product | Protect, grow, start with, don't, and how you'll know |
| The four pillars | Each score and what it means |
| Where we're strong / exposed | The findings that matter most, with sources |
| The AI opportunity | Your level today, where AI could earn money and take work off customers |
| Our move | Your quadrant, why, and what it means |
| Ready for the vision? | Data, tech, team, customers and pricing: what you have, the gap, what must be true, how to check |
| Where value flows | The summary of `value.md`: today, tomorrow, and the shift |
| What we corrected | Every score you challenged, and why it changed or didn't |

## Troubleshooting

- **Claude asks you to run another skill first.** Discovery needs `product.md` and at least one file from the vision skill. Check you picked the right folder.
- **You don't know a number.** Say so, or give a rough range. Claude marks it, and the score relies on public evidence instead.
- **A score feels wrong.** Challenge it in step 5, with evidence: a customer example, a number, a link.
- **You ran out of time.** Say so. Claude saves what's done and marks the rest "Not done yet". Move on, and run `/ai-product-discovery` again later to finish.

## Tips

- Bring someone who knows retention, the stack and the contracts. The inside view is what makes this deeper than public research.
- Challenge at least one score. The point isn't the number; it's the evidence behind it.
- Be honest about the gaps. A vision with its gaps named is one your developers and leadership can plan for.
