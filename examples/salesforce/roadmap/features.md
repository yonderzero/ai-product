# Salesforce Sales Cloud and Service Cloud · Features, prioritised

> Illustrative. Built from public sources; not affiliated with or endorsed by Salesforce. The product manager's answers are invented, tagged `[PM, illustrative]`.

Features for the flows taken forward in `../flows/flows.md` (flow 1, the rep confirms the deal, and flow 2, the forecast brief without the chase), plus the best ideas from ideation, prioritised. Built on 27 Oct 2026.

## Ideas

Where the features came from: the flows moment by moment, the opportunities and the Imagine section in `../vision/`, what the panel asked for in `../flows/panel-tests.md`, and ideation with the product manager. There are no real customer interviews in this example.

| Idea | From | Flow it serves | Keep? |
|---|---|---|---|
| Propose stage, close date, next step and forecast category from calls and email, each with its evidence | flow 1, moments 1–2; `../vision/opportunities.md` #1 | 1 | yes |
| One review list: accept, edit or reject each change; no "accept all" | flow 1, moment 3; panel round 1 | 1 | yes |
| A private preview of the rep's deal as the manager will see it | panel round 1 (Marcus, Sam) | 1, 2 | yes |
| A report row per change: old and new value, evidence, who confirmed, when, edited or not; pause per field | panel round 1 (Elena) | 1, 2 | yes |
| Undo any confirmed change | ideation `[PM, illustrative]` | 1 | yes |
| A loud notice the moment capture stops, to the rep and to the admin | panel rounds 1 and 2 (Marcus, Elena) | 1 | yes |
| "Look again" when a rep accepts forecast-moving changes fast | panel round 1 (Elena) | 1 | yes |
| One-tap "accept all" for small changes | panel round 1 (Marcus) | 1 | drop, because the sceptic and the buyer said a rubber-stamped log is worse than none |
| Questions about gaps, in the rep's own review list | flow 2, moment 2; panel round 1 | 2 | yes |
| The brief: what changed since last week with a reason per move, and the three deals that need the manager | flow 2, moments 3–4 | 2 | yes |
| Commit, best case and a range with its method stated, reconciled to the Forecasts tab; stop on a mismatch | flow 2, moment 5; panel round 1 (Elena, Priya) | 2 | yes |
| Override any deal with a reason, visible to the rep | flow 2, moment 6 | 2 | yes |
| Accept, edit and reject counts per rep, for the manager | panel round 1 (Priya) | 2 | yes, with a rule on who sees them (panel round 2, Marcus) |
| A fallback brief marked stale when the totals disagree | panel round 2 (Priya) | 2 | yes |
| Unconfirmed drafts visible to the manager, labelled | panel round 2 (Priya) | 2 | drop, because it breaks the rep-first promise every rep persona asked for |
| Test the range against the team's past quarters | panel round 1 (Priya) | 2 | merge into the range feature |
| Read calls from recorders customers already pay for | `../research/panel.md`, change 3 | 1 | yes, later |
| The brief and the questions in Slack | `../research/experiences.md` #2 | 2 | yes, later |
| Hygiene rules with a dry run and owner questions | flow 3 (`../research/experiences.md` #4) | 3 | yes, next |
| Slipping-deal flags to the rep first, with their hit rate | flow 4 | 4 | yes, later |
| Service notes on the deal | flow 5 | 5 | drop for now, because the flow isn't taken forward |
| "Deals like yours": opt-in benchmarks | `../vision/vision.md`, Imagine; `../vision/opportunities.md` #6 | 2 | yes, later |
| A household version for financial advisors | `../problem/framings.md`, adjacent segments; Sam | 1 | yes, later |

## The features, prioritised

| # | Feature | Kind | Flow | Value | Pay | Confidence | Effort | Priority | Horizon |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Review list: accept, edit or reject each change, no "accept all" | control | 1 | 4 | 3 | Good | 1 | 14.0 | Now |
| 2 | Override any deal with a reason, visible to the rep | control | 2 | 4 | 3 | Good | 1 | 14.0 | Now |
| 3 | Change log in a standard report, with a pause per field | visibility | 1, 2 | 4 | 4 | Good | 2 | 10.67 | Now |
| 4 | Proposed deal updates with evidence | agent capability | 1 | 5 | 3 | Strong | 3 | 10.0 | Now |
| 5 | Undo any confirmed change | control | 1 | 3 | 2 | Good | 1 | 10.0 | Now |
| 6 | Hygiene rules with a dry run and owner questions | agent capability | 3 | 3 | 3 | Strong | 2 | 10.0 | Next |
| 7 | Questions about gaps, in the rep's review list | agent capability | 2 | 4 | 3 | Good | 2 | 9.33 | Now |
| 8 | The brief: what changed and why, and the three deals that need you | visibility | 2 | 5 | 4 | Good | 3 | 9.0 | Now |
| 9 | Commit, best case and range, reconciled to the Forecasts tab | agent capability | 2 | 4 | 4 | Good | 3 | 8.0 | Now |
| 10 | Private preview for the rep | control | 1, 2 | 4 | 3 | Thin | 1 | 7.0 | Now |
| 11 | Accept, edit and reject counts per rep | visibility | 2 | 3 | 3 | Thin | 1 | 6.0 | Now |
| 12 | Fallback brief marked stale | control | 2 | 3 | 3 | Thin | 1 | 6.0 | Now |
| 13 | Capture notice, to the rep and the admin | visibility | 1 | 3 | 2 | Thin | 1 | 5.0 | Now |
| 14 | "Look again" on fast accepts | control | 1 | 3 | 2 | Thin | 1 | 5.0 | Now |
| 15 | The brief and the questions in Slack | visibility | 2 | 3 | 2 | Thin | 2 | 3.33 | Next |
| 16 | Read calls from other recorders | data | 1 | 4 | 4 | Thin | 4 | 3.2 | Next |
| 17 | A household version for financial advisors | agent capability | 1 | 4 | 3 | Thin | 4 | 2.8 | Later |
| 18 | Slipping-deal flags to the rep first, with their hit rate | agent capability | 4 | 3 | 2 | Thin | 4 | 2.0 | Next |
| 19 | "Deals like yours": opt-in benchmarks | data | 2 | 4 | 4 | Assumption | 5 | 1.33 | Later |

- **Value:** the hours it gives back and how much customers want it (no real customers yet, so the panel and `../research/experiences.md`): 5 for the features that carry the 1,725 hours of flow 1 or the 1,552 of flow 2.
- **Pay:** how likely customers pay for it, from the panel's pay scores.
- **Confidence:** the evidence grade (Strong 5, Good 4, Thin 2, Assumption 1). Strong where `../problem/evidence.md` and `../research/evidence.md` show past behaviour or spend; Thin where only the panel asked for it.
- **Effort:** 1 small, on data we already hold … 5 needs data or rights we don't have. Agreed with the product manager `[PM, illustrative]`; developers haven't scored it yet.
- **Priority** = (value + pay) × confidence points ÷ (effort + 1).

**Working:** 1: (4 + 3) × 4 ÷ 2 = 14.0 · 2: (4 + 3) × 4 ÷ 2 = 14.0 · 3: (4 + 4) × 4 ÷ 3 = 10.67 · 4: (5 + 3) × 5 ÷ 4 = 10.0 · 5: (3 + 2) × 4 ÷ 2 = 10.0 · 6: (3 + 3) × 5 ÷ 3 = 10.0 · 7: (4 + 3) × 4 ÷ 3 = 9.33 · 8: (5 + 4) × 4 ÷ 4 = 9.0 · 9: (4 + 4) × 4 ÷ 4 = 8.0 · 10: (4 + 3) × 2 ÷ 2 = 7.0 · 11: (3 + 3) × 2 ÷ 2 = 6.0 · 12: (3 + 3) × 2 ÷ 2 = 6.0 · 13: (3 + 2) × 2 ÷ 2 = 5.0 · 14: (3 + 2) × 2 ÷ 2 = 5.0 · 15: (3 + 2) × 2 ÷ 3 = 3.33 · 16: (4 + 4) × 2 ÷ 5 = 3.2 · 17: (4 + 3) × 2 ÷ 5 = 2.8 · 18: (3 + 2) × 2 ÷ 5 = 2.0 · 19: (4 + 4) × 1 ÷ 6 = 1.33.

**Why hygiene (6) is Next despite its score:** it serves flow 3, which isn't taken forward in this update, and it builds on the change log (3). It's the first thing in Next. `[PM, illustrative]`

## This product update

The features in Now, in priority order: the rep confirms the deal, and the manager's forecast brief is built only from what reps confirmed.

1. Review list: accept, edit or reject each change, no "accept all"
2. Override any deal with a reason, visible to the rep
3. Change log in a standard report, with a pause per field
4. Proposed deal updates with evidence
5. Undo any confirmed change
6. Questions about gaps, in the rep's review list
7. The brief: what changed and why, and the three deals that need you
8. Commit, best case and range, reconciled to the Forecasts tab
9. Private preview for the rep
10. Accept, edit and reject counts per rep, with a rule on who sees them
11. Fallback brief marked stale
12. Capture notice, to the rep and the admin
13. "Look again" on fast accepts

### The build-day slice

The smallest end-to-end slice of this update that developers start with, small enough to build in about a day, to make the flow real and testable:

- **The flow:** a call ends → the agent proposes changes with evidence → the rep accepts, edits or rejects each one → the manager's brief shows only what the rep confirmed, what changed, the three deals that need them and the commit → the manager overrides one deal with a reason.
- **In:** sample data for one team (five reps, fifteen open deals, a few call summaries and email threads as text, in a developer org or plain files); proposed updates with evidence (4); the review list (1); a simple change log (3); the brief with what changed, three deals and a commit that adds up to the deals behind it (7, 8); override with a reason (2).
- **Out (for now):** live email, calendar and call capture; other recorders; Slack; the private preview screen (the brief simply leaves out anything unconfirmed); the range and its test against past quarters; reconciliation to the real Forecasts tab; undo; per-rep counts; the capture notice; "look again"; the fallback brief; anything across customers.
- **Done when:** someone playing a rep accepts two proposed changes and rejects one on a deal; the manager's brief shows only the two, with who confirmed them and the evidence; the commit equals the sum of the commit deals; and an override changes the commit and appears in the log with its reason.
