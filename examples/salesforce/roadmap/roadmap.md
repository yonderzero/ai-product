# Salesforce Sales Cloud and Service Cloud · Roadmap

> Illustrative. Built from public sources; not affiliated with or endorsed by Salesforce. The product manager's answers are invented, tagged `[PM, illustrative]`.

From the thinnest version to the BHAG, in three horizons. Outcomes first, features second. Built from `features.md`, `roi.md`, `../flows/flows.md`, `../research/experiences.md`, `../vision/vision.md` and `../problem/problem.md` on 27 Oct 2026.

**The BHAG:** by 2029, sellers spend 70% of their week selling, up from 40%, and no sales manager has to ask a rep where a deal stands (`../problem/problem.md`).
**The vision:** level 5, AI Domain Intelligence, by the end of 2028: Sales Cloud keeps every deal up to date on its own and tells each sales team what is working in deals like theirs (`../vision/vision.md`).

| | Now | Next | Later |
|---|---|---|---|
| **The outcome for customers** | Managers walk into the forecast call knowing what changed and which deals need them, without chasing reps; reps confirm instead of typing | Records stay clean at the source; managers and reps get the brief where they already work | Each team sees what works in deals like theirs; the forecast comes with a range from many companies |
| **Agentic experiences** | The forecast call without the chase, with the rep's confirm step (flows 1 and 2), thinnest version first | Pipeline hygiene without the bulk reset (flow 3); step in before a deal slips (flow 4) | "Deals like yours" benchmarks; a household version for financial advisors |
| **Key features** | Review list, override with a reason, change log, proposed updates with evidence, the brief, commit reconciled to Forecasts, private preview (`features.md`) | Hygiene rules with a dry run; the brief and questions in Slack; calls from other recorders; slipping-deal flags to the rep first | Opt-in benchmarks across customers; household records and compliance-ready notes |
| **AI level** | 4, AI Delegated, in the forecast workflow | 4, across more of the sales workflow | 5, AI Domain Intelligence |
| **Hours given back per customer** | 3,277 a year | 3,829 a year (adds 552 for revenue operations) | more of the non-selling week, toward the BHAG; not sized yet |
| **What customers pay for** | Agents for the sales team, $45 a user a month, a fixed line at renewal | The same line; hygiene included, to protect the renewal | A benchmark subscription per sales team, priced on pipeline managed `[PM, illustrative]` |
| **New agent revenue per customer** | $17,280 a year | $17,280 a year; the renewal is what grows | not priced yet |
| **What we must learn first** | Do reps hold back bad news, or lack time? Will managers believe a record reps confirmed but didn't type? | Do reps answer hygiene questions, or mute them? Do flags show a real hit rate on the customer's own deals? | Will sales leaders opt in to sharing anonymised deal data, and on what terms? |
| **How we'll know it worked** | Managers stop messaging reps before the call; share of proposed changes accepted without edits; more teams within 5% of their forecast | Past-due close dates on open deals; tickets about numbers that don't match | Share of leaders who opt in; benchmark subscriptions sold |

## Now

This product update: the rep confirms the deal, and the manager's brief is built only from what reps confirmed (`features.md`, This product update). It comes first because it is the chosen problem in the buyer's own terms, it gives back the most hours (3,277 a year for a typical customer, a $239,400 saving, `roi.md`), and it tests the riskiest assumption head on: whether managers believe a record their reps confirmed but didn't type, and whether a rep-first flow makes reps share bad news sooner.

Developers start with the build-day slice in `features.md`: one team's sample data, end to end, from a call to an override. Then the full update runs as a pilot with one sales team at each of 10 customers, as the first step in `../vision/vision.md` says, with the interview kit in `../flows/script.md`.

## Next

Once Now works, the same change log carries hygiene: revenue operations sets the rules, the agent asks the person who knows the deal, and the bulk reset goes away (flow 3). The brief and the questions move into Slack, and the agent reads calls from recorders customers already pay for, which answers the buyer's "why pay twice?" objection in `../research/panel.md`. Slipping-deal flags go to the rep first, and only once they can show their hit rate on the customer's own past deals. All of this stays at level 4 and widens it; the hours reach the full 3,829 in `../research/experiences.md`.

## Later

The step to level 5 and toward the BHAG. With clean, rep-confirmed records across many customers, and only with their opt-in, Sales Cloud can show "deals like yours" and give the forecast a range drawn from thousands of companies (`../vision/vision.md`, Imagine). That needs the readiness gaps in `../discovery/discovery.md` closed first: explicit consent, and data scientists and privacy engineers on the team. The adjacent segment comes here too: a household version for financial advisors, who already pay for the same job after every meeting (`../problem/framings.md`). Beyond that, the rest of the non-selling week, the bigger half of the BHAG.

## Not on the roadmap

- **Service signals reach the deal (flow 5):** it only works where support runs on Service Cloud, and no persona would pay for it from a sales budget (`../flows/panel-tests.md`).
- **"Accept all":** the sceptic and the buyer both said a rubber-stamped log is worse than none.
- **Showing managers unconfirmed drafts:** it would break the rep-first promise every rep persona asked for.
- **Repricing seats across the board:** not until outcome pricing is proven (`../discovery/discovery.md`, Don't).
- **Quoting and sales-to-success handoff agents:** the evidence is still thin (`../vision/opportunities.md`).
