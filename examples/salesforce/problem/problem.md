# Salesforce Sales Cloud and Service Cloud · The right problem

> Illustrative. Built from public sources; not affiliated with or endorsed by Salesforce. The product manager's choices are invented to show how `/ai-product-problem` works, tagged `[PM, illustrative]`.

Built from `evidence.md`, `framings.md` and the product manager's choices on 27 Oct 2026.

## The BHAG

**By 2031, sellers spend 70% of their week selling, up from 40%, and no sales manager has to ask a rep where a deal stands.**

Sellers say they spend 40% of their time selling today (https://www.salesforce.com/news/stories/state-of-sales-report-announcement-2026/). `[PM, illustrative]` We chose this one because both people feel it: the rep gets the week back, and the manager stops chasing.

## The problem we'll solve

**When** the quarter is on the line and the forecast call is coming, **a sales manager wants to** know where every deal really stands and which ones need them, without chasing reps, **so they can** call the number with confidence and spend their time coaching. Today they message reps one by one, rebuild the forecast in their own spreadsheet, and reset past-due close dates in bulk (https://www.revopscoop.com/post/salesforce-forecasting). Reps pay with selling time: some block out an hour a day for updates (https://beyondsnakeoil.substack.com/p/just-let-ai-help-you-sell-more). Leaders still don't believe the result: only 24% trust their reps' commits (https://www.gong.io/press/as-economic-headwinds-grow-stronger-only-24-of-sales-leaders-are-confident-in-their-teams-revenue-forecast).

- **Framing chosen:** the bigger job, because the evidence is good, customers already pay for it (Gong passed $500M a year, https://en.globes.co.il/en/article-1001542789), and it covers the steps where managers lose the most: Monitor, Modify and Conclude. "As stated" fixes the typing but leaves the manager still guessing. The moonshot is the right direction but too thin on evidence to start with. `[PM, illustrative]`
- **Level:** from 2 today to 4 (`../vision/ai-levels.md`).
- **How it moves us toward the BHAG:** it removes the chase, the second half of the BHAG, and gives back the selling time that goes into updates and forecast prep. The rest of the non-selling week comes later.
- **Evidence:** Good, because the forecast findings come from surveys, practitioners and spend on tools on top, but nothing yet from Sales Cloud managers in their own words (`evidence.md`).

## The opportunity

| | |
|---|---|
| **More value for existing customers** | Sales managers and VPs of sales get a forecast they believe and time to coach; reps get selling time back. They'd pay for it as part of what they now spend on tools on top. `[PM, illustrative]` |
| **New customers** | Financial advisors already pay $100–$120 a month each for the same job after client meetings, and more than 27,000 use one tool (https://finovate.com/category/jump/, https://www.wealthmanagement.com/technology/ai-startup-advisors-jump-announces-46m-funding). Not counted in the size. |
| **Size a year** | $135M–$542M = $9.03B Sales revenue in fiscal 2026 (measured, https://www.sec.gov/Archives/edgar/data/1108524/000110852426000056/crm-q4fy26xexhibit991.htm) × 10–20% of it from customers who'd pay (assumption) × 15–30% price uplift (assumption). Working in `framings.md`. |

## What success looks like

- Sales managers stop messaging reps for updates before the forecast call. `[PM, illustrative]`
- Records are current when the forecast is called: close dates not in the past, next steps booked. `[PM, illustrative]`
- More teams land within 5% of their forecast. `[PM, illustrative]`
- Reps report more of their week selling, measured the same way as the State of Sales. `[PM, illustrative]`

## What we need to learn before building

The riskiest assumptions, most dangerous first, each with the questions to ask customers (Mom Test: their life, the past, specifics).

| Assumption | Why it's risky | Questions to ask |
|---|---|---|
| Records are stale because updating takes time, not because reps hold back bad news | If reps hide deals on purpose, a current record of activity won't make the forecast honest (`evidence.md`) | "Tell me about the last deal that slipped without warning. When did the rep know?" · "What was in the record the week before? Why?" · "What happened to the rep after it slipped?" |
| Managers and reps will trust a deal record they didn't type | Salesforce's own activity capture fell short before; one wrong update in a commit can break trust (`framings.md`, four forces) | "Tell me about the last time you found a wrong number in the pipeline. How did you find it?" · "When a tool logged activity for you, what did you still check by hand?" · "What did you do after you found the mistake?" |
| Managers rebuild the forecast in spreadsheets because the CRM is behind, not for other reasons such as splits or their own judgement | If the spreadsheet stays for other reasons, the chase moves but doesn't end (https://www.revopscoop.com/post/salesforce-forecasting) | "Walk me through last week's forecast. Where did each number come from?" · "What did you change in the spreadsheet that wasn't in Salesforce?" |
| Customers would pay us for this instead of, or on top of, what they pay Gong or Clari | They may be happy with the tool on top and see no reason to move (`framings.md`, habit) | "What do you pay today for call recording or forecasting? Who signed it?" · "At the last renewal, what nearly made you drop it?" · "What did you try before it?" |

## Not now

- **The moonshot: the whole non-selling week.** Research, internal meetings and admin are bigger than this problem, but the evidence that customers would pay for outcomes instead of seats is thin. The BHAG keeps it in sight.
- **"Deals like yours" benchmarks.** They need clean records and customers' opt-in first (`../discovery/discovery.md`, Don't).
- **Adjacent segments.** Financial advisors are promising and already pay. We'll come back once the problem is proven with Sales Cloud managers. Dealerships and recruiters are further from us.
- **Coaching on real conversations.** Real for newer reps, but one finding so far (`framings.md`).
