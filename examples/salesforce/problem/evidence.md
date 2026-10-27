# Salesforce Sales Cloud and Service Cloud · Problem evidence

> Illustrative. Built from public sources; not affiliated with or endorsed by Salesforce. Anything tagged `[PM, illustrative]` is invented to show what a product manager would add.

What backs the problem, graded with the Mom Test. Built on 27 Oct 2026. There is no `documents/` folder in this example, so all the evidence is public. A real run would add the team's own customer notes, win/loss notes and usage data.

**The problem as we started:** reps' deal records are never current, so managers don't trust the forecast and reps lose selling time to data entry (`../discovery/discovery.md`).
**Overall grade:** Strong, because there are more than three findings from four kinds of source (spend, practitioners' own accounts, forums and surveys), and several show past behaviour and money spent by people other than Salesforce. The weak spot: almost nothing is in Sales Cloud customers' own words. Most first-hand accounts come from other CRMs or from sales teams in general.

## Past behaviour and spend (strong)

| What happened | Who | How often / how much | Source |
|---|---|---|---|
| Companies pay for a tool on top of the CRM that records calls and helps forecast. Gong's annual recurring revenue passed $500M at the end of April 2026, up 55% in a year | Sales leaders and revenue operations, as buyers | More than $500M a year, across many customers. Not all of it is spent on this problem | https://en.globes.co.il/en/article-1001542789 |
| Gong had more than 4,500 customers, and named forecasting among its fastest-growing products | Sales teams | 4,500+ companies (March 2025) | https://www.gong.io/press/gong-surpasses-300m-arr-amid-increased-demand-for-ai-powered-revenue-solutions |
| A sales team on Zoho CRM found per-call updates took 15–20 minutes, so they built their own voice-note tool that fills the CRM fields | A sales team, writing in the first person | Every call; down to about 2 minutes after the change | https://help.zoho.com/portal/en/community/topic/how-we-cut-crm-updates-from-20-minutes-down-to-2-our-real-workflow?page=10 |
| A writer on sales technology describes reps blocking out an hour a day to update Salesforce, before AI tools, and says they did it to keep managers happy | Account executives | An hour a day (2024) | https://beyondsnakeoil.substack.com/p/just-let-ai-help-you-sell-more |
| Car dealership managers made logging a condition for getting new leads, and inspect records with no next action every day. One manager's rule: "log notes or it did not happen" | Sales managers at dealerships | Every customer conversation; daily inspection (thread from August 2026) | https://forum.dealerrefresh.com/threads/how-often-do-your-sales-reps-actually-update-the-crm-after-customer-calls.13520/ |
| Financial advisors pay for an assistant that turns client meetings into notes, tasks, CRM updates and compliance records | Financial advisors (adjacent segment) | More than 27,000 advisors (Feb 2026); most paid $100–$120 a month each in 2024 | https://finovate.com/category/jump/ · https://www.wealthmanagement.com/technology/ai-startup-advisors-jump-announces-46m-funding |

## Workarounds today

| Workaround | Who | What it costs them | Source |
|---|---|---|---|
| Managers forecast from their own spreadsheet, carried from company to company; the forecast call is a verbal round of hopes | Sales managers | A second system beside the CRM, which then "rarely reflects reality" | https://www.revopscoop.com/post/salesforce-forecasting |
| A scheduled clean-up moves every past-due close date to the start of the current month, so stale deals don't linger | Revenue operations | Admin time each quarter, and dates that are guesses | https://www.revopscoop.com/post/salesforce-forecasting |
| Reps keep shadow spreadsheets because they are faster to edit, and update Salesforce in batches, often at quarter end (vendor view) | Account executives | Leaders see old data when decisions are made | https://www.scratchpad.com/blog/salesforce-issues |
| Virtual assistants hired to update close dates, chase reps for notes and fill gaps from calendars and call recordings (a staffing firm's offer) | Sales teams | From about $10–$15 an hour, per the firm's page | https://stealthagents.com/virtual-assistant-salesforce-support |
| Salesforce's own Einstein Activity Capture logs emails and meetings, but some captured email isn't reliably available to reports or automation, and history is kept for a limited time. What customers tried, and where it fell short | Account executives, admins | Activity that exists but can't be used for the forecast | https://salesforcebreak.com/2026/03/04/einstein-activity-capture-guide/ |
| Job postings ask reps to track every activity in Salesforce by hand | SDRs, account executives | Part of every rep's job description | `../vision/opportunities.md` (step 3) |

## What people say (weak on its own)

Surveys report what people say, not what they did. Several are run by vendors who sell a fix, Salesforce included, so each counts as one voice.

| Said | Who | Source |
|---|---|---|
| The average seller spends 40% of their time selling; Gen Z reps 35%, losing about two hours a week to manual data entry. 74% say they're focusing on data cleansing | 4,050 sales professionals, 22 countries, surveyed Aug–Sep 2025 (Salesforce, State of Sales 2026) | https://www.salesforce.com/news/stories/state-of-sales-report-announcement-2026/ |
| Reps spend about 70% of their time on non-selling work; only 35% completely trust their organisation's data accuracy | 5,500 sales professionals, 27 countries, surveyed 2024 (Salesforce) | https://www.salesforce.com/news/?p=79781 |
| Only 24% of sales leaders are confident in their team's forecast, and 24% trust their reps' commits. Leaders using what was said with customers were twice as likely to land within 5% as those relying on seller-entered data (22% vs 11%) | 928 sales and revenue professionals (Gong, 2022) | https://www.gong.io/press/as-economic-headwinds-grow-stronger-only-24-of-sales-leaders-are-confident-in-their-teams-revenue-forecast |
| Only 45% of sales leaders and sellers have high confidence in their forecast accuracy | Gartner survey of sales operations, 2020 | https://www.gartner.com/en/newsroom/press-releases/2020-02-12-gartner-says-less-than-50--of-sales-leaders-and-selle |
| 76% say less than half of their CRM data is accurate and complete; 37% say they lost revenue because of poor data | 602 CRM users and stakeholders (Validity, which sells data-quality tools, 2025) | https://www.validity.com/resource-center/the-state-of-crm-data-management-in-2025/ |
| Reps spend 25–35% of their time with customers, and give real coverage to about 40% of their accounts; the cause is admin, including CRM hygiene | HubSpot's CEO, speaking at SaaStr 2025 (no study cited) | https://www.saastr.com/the-40-problem-do-your-sales-reps-really-cover-all-their-accounts-and-is-ai-the-answer-with-yamini-rangan-ceo-hubspot |
| Managers say a forecast is only as good as what reps type in | `[PM, illustrative]` | `../product.md` |

## What we looked for and didn't find

- **Sales Cloud customers in their own words.** Reddit threads and full G2, Capterra and TrustRadius reviews couldn't be read for this example. A real run should add them, or the team's own interview notes in `documents/`.
- **Hours spent updating Salesforce specifically.** The time figures are for sales work in general or for other CRMs.
- **A direct link from stale records to missed forecasts.** The surveys show low trust and low data quality, but not how much of a forecast miss comes from records that weren't updated, rather than from optimism or hidden deals.
- **Whether reps hide deals on purpose.** One vendor says reps change values or dates to avoid scrutiny (https://www.scratchpad.com/blog/salesforce-issues). If that's common, the problem is partly motivation, not data entry.
- **Evidence that reps would trust records they didn't type.** Nothing found either way.
- **A count of Sales Cloud customers or seats.** Not reported; only revenue is (`../product.md`).
