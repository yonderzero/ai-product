# ai-product-discovery

```
/ai-product-discovery
```

The third skill, after [`ai-product-vision`](ai-product-vision.md). Your vision says where your product could go. Discovery checks whether it's ready: what protects it, how strong it is, how big the AI opportunity is, and what could go wrong. Then it looks at what has to be true to reach the vision, and helps you choose your move.

It goes deeper than the vision in two ways: it adds your inside knowledge, which public research can't see, and it tests the vision against what it would take.

**Who runs it:** the product manager, ideally with someone who knows the numbers and the tech.
**Run it:** in the folder that holds your product's folder.
**You leave with:** your product scored on four pillars, a readiness check for your vision, your move, and three next steps.

## Before you begin

- **Your product profile and some of your vision.** Run [`/ai-product-start`](ai-product-start.md) and [`/ai-product-vision`](ai-product-vision.md) first. Neither has to be finished: discovery needs a `product.md` and at least one file from the vision skill. The readiness check uses the furthest your vision got: `vision.md`, else your top opportunities, else your AI levels.
- **The same folder.** In the Claude desktop app, pick the folder that holds your product's folder with **Project or folder**. In Claude Code, start Claude there.
- **Web search.** The scores are researched on the web.
- **Some numbers, if you have them:** retention, implementation time, team size. Rough figures are fine.

## The four pillars

Each pillar is scored 1–5 against a fixed rubric, with a source for every score. A script does the arithmetic.

| Pillar | The question | What's scored |
|---|---|---|
| **Protection** | What protects your product? | 24 levers in four groups: switching costs, domain knowledge, speed and cost of building, and distribution. It also shows which are eroding fastest because of AI. |
| **Strength** | How strong is the product and its customer base? | Business quality: where it sits in your customers' operations, how vertical and how critical it is, its competitive standing, leadership, and tech stack. Customer strength: how embedded it is, and how loyal customers are. |
| **AI opportunity** | How big is the AI prize? | AI in the product today, how urgent it is, revenue AI could earn, and work AI could take off customers. |
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

8. **One page.** Claude writes `discovery.md` and asks: "Is this right?"

9. **Done.** Claude adds your move to `product.md` and sums up: the move, the biggest gap to the vision, and the first next step.

## What you get

```
acme-scheduler/
  product.md       now with your move
  3-discovery/
    protection.md    what protects your product: 24 levers, scored, with sources
    strength.md      business quality, customer strength and the AI opportunity, scored, with sources
    exposure.md      11 risks, scored, with sources
    discovery.md     the one page: four pillars, readiness for the vision, your move, next steps
```

`discovery.md` holds:

| Section | What's in it |
|---|---|
| In short | Where you're strong, where you're exposed, and the move |
| The four pillars | Each score and what it means |
| Where we're strong / exposed | The findings that matter most, with sources |
| The AI opportunity | Your level today, where AI could earn money and take work off customers |
| Our move | Your quadrant, why, and what it means |
| Ready for the vision? | Data, tech, team, customers and pricing: what you have, the gap, what must be true, how to check |
| What we corrected | Every score you challenged, and why it changed or didn't |
| Next steps | Three steps that follow from the move and the gaps |

## Troubleshooting

- **Claude asks you to run another skill first.** Discovery needs `product.md` and at least one file from the vision skill. Check you picked the right folder.
- **You don't know a number.** Say so, or give a rough range. Claude marks it, and the score relies on public evidence instead.
- **A score feels wrong.** Challenge it in step 5, with evidence: a customer example, a number, a link.
- **You ran out of time.** Say so. Claude saves what's done and marks the rest "Not done yet". Move on, and run `/ai-product-discovery` again later to finish.

## Tips

- Bring someone who knows retention, the stack and the contracts. The inside view is what makes this deeper than public research.
- Challenge at least one score. The point isn't the number; it's the evidence behind it.
- Be honest about the gaps. A vision with its gaps named is one your developers and leadership can plan for.
