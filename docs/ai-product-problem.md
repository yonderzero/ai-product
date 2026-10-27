# ai-product-problem

```
/ai-product-problem
```

The fourth skill, after [`ai-product-discovery`](ai-product-discovery.md). You've picked a problem to go after. This skill makes sure it's the right one: it says the problem sharply, checks the evidence and tests it. Then it pushes you to think bigger, so that solving the problem captures as much value as possible and moves your product up the levels.

Think first, then build: nothing here proposes a feature or a solution. You leave with the right problem, the opportunity it captures, and what you need to learn from customers before building anything.

**Who runs it:** the product manager, ideally with the team.
**Run it:** in the folder that holds your product's folder.
**You leave with:** a BHAG, the right problem as a customer job, the opportunity it captures, and the riskiest assumptions written as questions for customers.

## Before you begin

- **Your profile and some of the earlier skills.** Run [`/ai-product-start`](ai-product-start.md), then [`/ai-product-vision`](ai-product-vision.md) and [`/ai-product-discovery`](ai-product-discovery.md). They don't have to be finished: this skill needs `product.md` and anything saved by the vision or discovery skills.
- **The same folder.** In the Claude desktop app, pick the folder that holds your product's folder with **Project or folder**. In Claude Code, start Claude there.
- **Your documents.** Customer interviews, tickets and sales notes in `documents/` make the evidence much stronger.

## The methods

Claude uses these as tools, in plain language.

| Method | What it's for | From |
|---|---|---|
| **Jobs to be Done** | Saying the problem as the job the customer is trying to get done: *When [situation], I want to [motivation], so I can [outcome].* Asking "why?" until you reach the job behind the task. | Clayton Christensen, Bob Moesta |
| **The job map** | Eight steps every job runs through: define, locate, prepare, confirm, execute, monitor, modify, conclude. The steps your product doesn't cover show where a bigger problem sits. | Tony Ulwick |
| **The Mom Test** | Judging evidence by what customers did, not what they say they'd do. Past events, workarounds and money already spent count; compliments and "we'd use that" don't. Also how to ask good questions. | Rob Fitzpatrick |
| **The four forces** | Whether customers would really switch: the **push** of today's pain and the **pull** of something new, against **anxiety** about the new (for AI: trust, errors, losing control) and the **habit** of the old. | Bob Moesta |
| **BHAG** | A Big Hairy Audacious Goal: one bold, measurable, dated goal for what would be true if the problem were solved completely. | Jim Collins and Jerry Porras |

## What happens

Claude asks one question at a time, like a conversation.

1. **What this is.** Claude explains the session in a few sentences, and asks: "Shall we start?"

2. **The problem.** Claude offers the likely starting points from your discovery ("Start with" and the "Grow" bets) and your top opportunities, and asks which problem you're going after. If you name a feature, it asks which customer problem the feature solves.

3. **Say it as a job.** Claude writes the problem as a job statement, with the struggling moment and its functional, emotional and social sides. It asks who has the problem most, when it last hit them, and what they're really trying to get done.

4. **The evidence.** Claude researches the problem in the background and goes through your documents and earlier files. It grades the evidence with the Mom Test: Strong, Good, Thin or Assumption.

5. **Pressure test.** One question at a time: is it real, does it hurt enough, what do customers do about it today, why us, why now, and the four forces. Then Claude argues the strongest case that this is the wrong problem, and asks how you'd answer it.

6. **Think bigger.**
   - **The BHAG:** "If you solved this completely, for every customer, what would be true?" Claude drafts options; you pick one and make it yours.
   - **The job map:** the eight steps of the job, which ones your product covers today, and at which level.
   - **What customers most want fixed:** beyond this problem, the biggest thing your current customers want fixed.
   - **Adjacent segments:** where else this problem is very painful now, such as other customer sizes, neighbouring verticals, partners or countries, each with evidence.

7. **Three framings.** The problem three ways, side by side: **as stated**, **the bigger job** (widened along the job map, one or two levels up) and **the moonshot** (the BHAG). Each shows who it's for, the level, the value from existing customers, new customers or revenue, the evidence, and a size built from real numbers.

8. **The right problem.** You choose, usually the most ambitious framing you can start on now. Claude writes the problem, the opportunity, what success looks like, and **what you need to learn before building**: the riskiest assumptions, each with Mom Test questions to ask customers.

9. **The deck.** Claude adds the BHAG, the right problem, the three framings and what to learn first to `index.html`, and opens it in the preview.

10. **Done.** Claude adds the right problem and the BHAG to `product.md`, and sums up: the BHAG, the right problem, and the riskiest assumption to test first. Next: [`/ai-product-research`](ai-product-research.md).

## What you get

```
acme-scheduler/
  problem/
    evidence.md     everything that backs the problem, graded with the Mom Test
    framings.md     the job, the pressure test, the BHAG, the job map, the biggest pains, adjacent segments, three framings
    problem.md      the right problem: the BHAG, the problem, the opportunity, success, what to learn before building
```

`problem.md` holds:

| Section | What's in it |
|---|---|
| The BHAG | One bold, measurable, dated goal |
| The problem we'll solve | The job statement, today's workaround and what it costs; the framing chosen and why; the level; how it moves toward the BHAG; the evidence grade |
| The opportunity | More value for existing customers, new customers, and the size a year |
| What success looks like | How you'd know the problem is solved |
| What we need to learn before building | The riskiest assumptions, each with questions to ask customers |
| Not now | What you're parking, and why |

## Troubleshooting

- **Claude asks you to run another skill first.** This skill needs `product.md` and something from the vision or discovery skills. Check you picked the right folder.
- **The evidence comes out Thin or Assumption.** That's useful: it tells you what to ask customers. Add interview notes or tickets to `documents/`, or carry the questions into your customer interviews.
- **The BHAG feels too big.** It's meant to. It should feel slightly uncomfortable, but stay measurable and about the customer's job.
- **You ran out of time.** Say so. Claude saves what's done and marks the rest "Not done yet". Run `/ai-product-problem` again later to finish.

## Tips

- Bring real stories: "Last Tuesday, two carers called in sick and…" beats "scheduling is hard".
- Don't fall in love with the first framing. The point of the bigger job and the moonshot is to see how much more value is on the table.
- If you catch yourself describing a feature, stop and ask which customer problem it solves.
