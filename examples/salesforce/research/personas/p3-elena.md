# p3 · Elena, revenue operations lead

> Illustrative synthetic persona. Not a real person. Built from public sources and invented product-manager input, tagged `[PM, illustrative]`.

modelled_on: the revenue operations lead at the ideal customer in `../icp.md`, who is also the Salesforce admin [PM, illustrative]
panel_role: sceptic

## Background
- organisation: B2B software, about 300 employees, North America [PM, illustrative]
- group position: one of two revenue operations people; reports to the VP of sales, works closely with finance [PM, illustrative]
- role and tenure: revenue operations lead, four years; certified Salesforce admin [PM, illustrative]
- runs on: Sales Cloud Setup, reports and flows, validation rules, Gong admin, spreadsheets for reconciliation [source: https://revengine.substack.com/p/automatically-nudging-reps-to-update]

## Business
- who signs: she doesn't sign, but she can block anything that touches the data model [PM, illustrative]
- budget route: renewal; she owns the Salesforce renewal paperwork [PM, illustrative]
- what they are measured on: Salesforce data accuracy and completeness; forecast accuracy [source: https://builtin.com/job/manager-revenue-operations-analytics/7780783] [source: https://jobs.workable.com/jobs/732e5b77-61c5-404f-9e4f-538f937b6ef6.md]
- renewal or contract moment: February [PM, illustrative]

## Psychology
- attitude to change: cautious [PM, illustrative]
- trust in AI: low until she can audit it; trust ranks above cost as admins' biggest barrier [source: https://www.salesforceben.com/5-reasons-salesforce-professionals-distrust-ai/]
- burned by: Activity Capture, whose captured email couldn't be used in reports, so she rebuilt activity reporting [source: https://revenuegrid.com/blog/einstein-activity-capture-limitations/] (competitor's account)
- will not tolerate: anything writing to opportunity fields without a log of who confirmed it and why [PM, illustrative]
- would pay for: no more bulk resets of close dates and no more "why doesn't this match?" tickets [source: https://www.revopscoop.com/post/salesforce-forecasting]

## Capability
- tech comfort: high [PM, illustrative]
- data they hold: the whole org: opportunities, field history, validation rules, forecast settings; she knows which fields are junk [source: https://revengine.substack.com/p/automatically-nudging-reps-to-update]
- time they can give a new tool: whatever the setup takes, but she has none to spare; admins manage more users than ever [source: https://www.appsruntheworld.com/survey-finds-agentforce-enriching-salesforce-admins-with-a-catch/]

## The problem, through their eyes
- the problem in their words: "The data is junk, so the forecast is junk, and I'm the one who gets asked why." [source: https://revengine.substack.com/p/automatically-nudging-reps-to-update] (paraphrased)
- how often it hits them, and what it costs them: weekly clean-ups and a reset each quarter; about 8 hours a week [PM, illustrative]
- what they do about it today: validation rules, nudging flows that loop in the manager after three reminders, scheduled resets [source: https://revengine.substack.com/p/automatically-nudging-reps-to-update]
- options they've tried or considered: Activity Capture; tested Agentforce in Setup and found it slower than doing it herself [source: https://www.getclientell.com/salesforce-blogs/what-salesforce-admins-are-saying-about-agentforce-2026] (vendor blog quoting admins)
- what would make them switch: a log of every change, rules she controls, and fewer tickets within a quarter [PM, illustrative]
- what worries them about a new way: errors she can't trace; another add-on with unclear credits; being the one who owns it when it breaks [source: https://oliv.ai/blog/agentforce-sales-coach] (unclear pricing per reviews quoted by a competitor)

## Behaviour
- a normal day: tickets from reps and managers in the morning, report fixes and a flow change in the afternoon, a reconciliation with finance before the forecast call [PM, illustrative]
- workarounds: exports to spreadsheets to reconcile the forecast; a scheduled job for past-due dates [source: https://www.revopscoop.com/post/salesforce-forecasting]
- last time it went wrong: a rule requiring a reason for a pushed close date broke on the second push, and reps learned to type anything [source: https://trailhead.salesforce.com/trailblazer-community/feed/0D54S00000A8Jy9SAF] (seen in search results only)
- how they buy: reads Salesforce Ben and the Trailblazer Community, asks peers, tests in a sandbox before anyone signs [PM, illustrative]

## Voice
- sounds like: "Show me the log. If I can't see who changed it and why, it doesn't go near the forecast." [PM, illustrative]

## Evidence log
| Kind | Evidence | Source |
|---|---|---|
| workaround | A flow nudges owners about past-due dates and adds the manager after three reminders | https://revengine.substack.com/p/automatically-nudging-reps-to-update |
| workaround | Scheduled reset of past-due close dates | https://www.revopscoop.com/post/salesforce-forecasting |
| objection | Trust is admins' top AI barrier (29.3% against 16.1% for cost) | https://www.salesforceben.com/5-reasons-salesforce-professionals-distrust-ai/ |
| pain | Admins manage more users than in 2020; a solo admin is drowning | https://www.appsruntheworld.com/survey-finds-agentforce-enriching-salesforce-admins-with-a-catch/ |
| objection | Admins found Agentforce in Setup slower than doing it themselves | https://www.getclientell.com/salesforce-blogs/what-salesforce-admins-are-saying-about-agentforce-2026 |
| pain | Activity Capture email outside reports and flows (competitor) | https://revenuegrid.com/blog/einstein-activity-capture-limitations/ |
| budget signal | Revenue operations postings measure data accuracy and forecast accuracy | https://builtin.com/job/manager-revenue-operations-analytics/7780783 |

**Grounding:** 28 tagged fields: 13 sourced, 15 `[PM, illustrative]`, 0 `[assumed]`.
