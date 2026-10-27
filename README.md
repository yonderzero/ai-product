# Product Track

One skill per session. In each workshop, type that session's skill in Claude Code and Claude walks your team through the mission, writing one file at a time. By Wednesday at Align you have a `handoff/` folder your developers can build from.

## Install

In Claude Code:

```
/plugin marketplace add yonderzero/ai-product
/plugin install product-track@ai-product
```

Then open your team's folder and run `/product-track:00-setup`.

## The sessions

### Day 1 · Tuesday 27 Oct · Learn: your product, its problems, its customers

| Session | Type this | You leave with |
|---|---|---|
| Before 01 | `/product-track:00-setup` | `my-product/` with `inputs/`, `panel/`, `handoff/` |
| 01 Introduction & Roundtable | `/product-track:01-know-your-product` | `01-brief.md`, `inputs/idea.md` |
| 02 SoR to SoU | `/product-track:02-whos-eating-our-lunch` | `02-ai-market-map.md` + `.html`: your market on the six AI levels |
| 03 Assessing Intelligence Maturity | `/product-track:03-read-the-domain` | `handoff/domain-read.md` |
| 04 Problem Definition & Opportunity Framing | `/product-track:04-harvest` | `04-long-list.md` |
| 05 AI-Assisted Market & User Research | `/product-track:05-build-your-customers` | `panel/`: evidence map, ideal customer, personas |
| 06 Customer Interviews | `/product-track:06-interview` | `06-interviews.md` |
| 07 Wrap Up & Reflections | `/product-track:07-day-one` | `07-day-one.md` |

### Day 2 · Wednesday 28 Oct · Decide, hand over, challenge

| Session | Type this | You leave with |
|---|---|---|
| 08 Ideation, Prioritisation, ROI & Pricing | `/product-track:08-make-the-case` | `handoff/problem.md`, `proposal.md`, `prototype/` |
| Align (with your developers) | `/product-track:align-product-spec` | `handoff/product-spec.md` |
| 09 Challenge the Shortlist | `/product-track:09-try-to-kill-it` | `09-challenge.md`, updated spec and prototype |
| 10 Group Discussion & Debrief | `/product-track:10-demo-story` | `10-demo-story.md`, `handoff/README.md` |

## The toolbox

The session skills call these. You can also use them on their own.

| Skill | What it does |
|---|---|
| `company-brief` | A sourced factual brief of a company or product |
| `ai-level-map` | Your market on six AI levels, from system of record to system of understanding: who is doing what, with evidence |
| `moat-scan` | 24 levers in four pillars: what protects the product |
| `threat-scan` | Five ways someone attacks it with AI, with named evidence |
| `maturity-score` | 12 dimensions: business quality, customer strength, AI opportunity |
| `risk-score` | 11 dimensions of risk, 1 safest to 5 most exposed |
| `product-gaps` | What the product is missing, from reviews, competitors and the market |
| `ai-redesign` | AI-first redesigns of the product's workflows |
| `synthetic-customers` | An evidence map, your ideal customer profile and personas from your own data, then interview, score, argue, react, calibrate, and Van Westendorp pricing |
| `interview-script` | A Mom Test interview script with JTBD probes |
| `summarize-interview` | A structured summary of a real interview transcript |

## Your folder

```
my-product/
  product.md       the product, the team, the customer types
  inputs/          what you brought: interviews, tickets, sales and support notes, usage data, idea.md
  01-brief.md …    one file per session
  panel/           your synthetic customers
  handoff/         what the developers get
```

Take personal data out of `inputs/` before session 05: no names, emails or phone numbers.

## Credits

See `THIRD-PARTY-NOTICES.md`.
