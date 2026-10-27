# Finding and rating opportunities

Adapted from the Opportunity Scanner's process map, opportunity and ranking rules.

## 1. The work around the product

Map the customer's work as 6–10 steps, in order, from the first thing that happens to the last. Cover the steps the product runs and the ones around it. For each step:

- **What happens:** one or two plain sentences.
- **Who does it:** the roles, using the personas in `product.md` where they fit.
- **Software:** each system seen at this step: ours, a competitor's, a spreadsheet, nothing. Only what's evidenced.
- **The record:** what record the step produces, and whether the product holds it.
- **Still manual:** what's still done by hand, phone, email, paper, spreadsheet or re-keying. This must come from evidence (the product manager, `documents/`, reviews, job postings, the customer's own words), never from a general belief about the industry.
- **Coverage:** software (software runs it), partial (software exists but manual work is evidenced), manual, or unknown.
- **Who's moving here:** companies from `market-map.md` and `market-moves.md` going after this step.
- **AI level today:** from `ai-levels.md`, the product's level at this step, or "not covered".

## 2. Opportunities

An opportunity is a specific job that AI could do or change, usually on a record the product already holds, that brings new value to customers. Two kinds:

- **Grow the base:** more value for existing customers, so they stay, use more and pay more.
- **New revenue:** a new paid product, module, data product or service, or the product reaching customers it doesn't serve today.

Rules:

- **On evidence.** Each opportunity cites what shows the job exists today: the manual work, the complaint, the competitor's move, the rule. No evidence, no opportunity.
- **Specific.** Name the step, who does the job today, and what the product would do instead. "Schedulers rebuild the timetable by hand when a lecturer is off sick" not "automate scheduling".
- **Its level.** Say which AI level the opportunity sits at, from `references/levels.md`.
- **Few and strong.** Up to 8. With thin evidence, three solid ones and a list of open questions beat eight padded ones. Don't repeat one idea in different words or split one idea into several.
- **Who else.** Name the companies already going after this job.
- **First question.** The one question to ask customers that would confirm or kill it.

## 3. Ratings

Integers 1–5, with a one-sentence reason each that points at evidence.

**Impact** (for the business):
1 marginal · 2 helps one customer team · 3 a clear sales story, or noticeable money · 4 a product customers will pay extra for · 5 changes the business: defends the core or opens a revenue line comparable to an existing one.

**Effort:**
1 days to weeks, on data the product already holds · 2 a few weeks and one integration · 3 a quarter, several integrations or new data capture · 4 several quarters, or waits on a migration · 5 needs data or rights the company doesn't have.

**Urgency:**
1 no clock · 2 worth doing within the year · 3 a competitor announced it, or a gap customers notice · 4 a competitor shipped it, or a dated rule lands within 18 months · 5 someone is already taking this job from the product's customers, or a deadline within 6 months.

**Evidence grade:**
- **Strong** (5 points): three or more findings, two or more kinds of source, and a quote from someone other than the company itself.
- **Good** (4): two or more findings, or a quote.
- **Thin** (2): one finding.
- **Assumption** (1): nothing beyond the product manager's belief.

The company describing its own customers' pain is one voice, however many of its pages say it. The product manager's interview counts as one source.

## 4. Priority

```
priority = 0.35 × impact + 0.25 × urgency + 0.20 × evidence points + 0.20 × (6 − effort)
```

Bands: **Do first** from 3.8 · **Strong option** from 3.3 · **Worth watching** below. Show the arithmetic.

## 5. Size, when you can

Express the yearly value as a product of factors, each with a low and high value, a unit and its source:

- **Grow the base:** customers × current price per customer a year × share who would buy × price uplift.
- **Retention:** customers at risk × revenue per customer a year × share of churn avoided.
- **New revenue:** customers or sites that could buy × price per customer a year × share who would buy.

At least one factor must be measured (a number from a source or the product manager). At most two can be assumptions; label them. Show the working. If you can't meet that, write "not sized" and why. A figure without its working is worse than none.
