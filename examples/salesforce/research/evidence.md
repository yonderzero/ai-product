# Evidence map · Salesforce Sales Cloud and Service Cloud

> Illustrative. Built from public sources; not affiliated with or endorsed by Salesforce. Anything tagged `[PM, illustrative]` is invented to show what a product manager would add.

What we know about customers before any persona is written. One row per piece of evidence. No real names. Built on 27 Oct 2026.

**There are no customer documents in this example.** This is a public example, so there is no `documents/` folder: no interview notes, call transcripts, tickets or CRM exports. A real run would start from the team's own material. Instead, this map uses public first-hand sources: forum posts, practitioner newsletters, job postings and reviews, grouped by customer type. Reddit, G2, Capterra and TrustRadius pages couldn't be opened for this example, so review text is thin; rows marked *(search result only)* were seen in search results but the page itself wasn't opened.

## Customer types we see

| Type | How many sources | Example source |
|---|---|---|
| Account executives and other reps | 6 | https://news.ycombinator.com/item?id=33132951 |
| Sales managers and sales leaders | 6 | https://news.ycombinator.com/item?id=33135245 |
| Revenue operations and Salesforce admins | 8 | https://revengine.substack.com/p/automatically-nudging-reps-to-update |
| Service leads (Service Cloud) | 5 | https://aws.amazon.com/marketplace/reviews/reviews-list/prodview-xdmwnsnyxbqou |
| Financial advisors (adjacent segment) | 5 | https://www.kitces.com/blog/artificial-intelligence-ai-meeting-notetakers-note-tools-client-communication-accuracy-domentation/ |

## Evidence

### Account executives and other reps

| Kind | What they said or did | Source |
|---|---|---|
| pain | A seller in cloud sales says points about poor Salesforce upkeep "hit especially hard" for them (2022) | https://news.ycombinator.com/item?id=33132951 |
| objection | A person in B2B sales and customer success says call recordings at past employers were stored but almost never looked at again (2022) | https://news.ycombinator.com/item?id=33132951 |
| pain | A sales leader writing in the first person says reps spend up to an hour a day updating Salesforce, mainly to keep managers happy (2024) | https://beyondsnakeoil.substack.com/p/just-let-ai-help-you-sell-more |
| workaround | A sales team on Zoho CRM built a voice-note tool because per-call updates took 15–20 minutes | https://help.zoho.com/portal/en/community/topic/how-we-cut-crm-updates-from-20-minutes-down-to-2-our-real-workflow?page=10 |
| pain | Gen Z sellers lose about two hours a week to manual data entry; sellers overall spend 40% of their time selling (survey of 4,050) | https://www.salesforce.com/news/stories/state-of-sales-report-announcement-2026/ |
| pain | A reviewer says creating opportunities is too time-consuming *(search result only)* | https://www.gartner.com/reviews/market/sales-force-automation-platforms/compare/product/salesforce-sales-cloud-vs-sap-sales-cloud |

### Sales managers and sales leaders

| Kind | What they said or did | Source |
|---|---|---|
| quote | A manager of a top-producing team at a large cybersecurity company: "Our reps have atrocious CRM hygiene" (2022) | https://news.ycombinator.com/item?id=33135245 |
| pain | The same manager spends a lot of time chasing reps for the bare minimum; forecast category is the one field they insist on, because other teams plan from it | https://news.ycombinator.com/item?id=33135245 |
| objection | The same manager: upkeep only gets checked when a rep misses quota, and good records don't predict good selling | https://news.ycombinator.com/item?id=33135245 |
| workaround | A former CMO turned revenue chief emails the forecast dashboard the night before a weekly call with the CEO and finance; slow deals repeat last week's update (2024) | https://cmo2cro.substack.com/p/efficient-effective-forecast-calls |
| workaround | Managers forecast from their own spreadsheet, carried from job to job; the forecast call becomes a round of hopes | https://www.revopscoop.com/post/salesforce-forecasting |
| pain | A sales author: reps set quarter-end close dates to answer the manager's question, not because the buyer will act then (2014) | https://www.thesalesblog.com/blog/lies-mistruths-and-fabrications-in-your-sales-forecast |
| pain | A consultant: close dates drift outward; suggests a reason for every change and counting how often a date moved (2016) | https://customerthink.com/where-did-that-close-date-come-from-and-where-is-it-going-to/ |
| budget signal | Only 24% of sales leaders trust their reps' commits (survey of 928, 2022) | https://www.gong.io/press/as-economic-headwinds-grow-stronger-only-24-of-sales-leaders-are-confident-in-their-teams-revenue-forecast |

### Revenue operations and Salesforce admins

| Kind | What they said or did | Source |
|---|---|---|
| workaround | A revenue operations writer built a flow that messages the owner about past-due close dates and adds the manager after three reminders (2022) | https://revengine.substack.com/p/automatically-nudging-reps-to-update |
| workaround | A scheduled job moves every past-due close date to the start of the month | https://www.revopscoop.com/post/salesforce-forecasting |
| budget signal | A data-storage company hires a full-time specialist whose job is to chase reps by call, Slack and email until required deal fields are filled (posted 4 Sep 2026) | https://careers.greenfield-growth.com/companies/vast-data/jobs/92220906-sales-data-management-specialist |
| trigger | Revenue operations postings make Salesforce data accuracy and forecast accuracy part of the job | https://builtin.com/job/manager-revenue-operations-analytics/7780783 · https://jobs.workable.com/jobs/732e5b77-61c5-404f-9e4f-538f937b6ef6.md |
| objection | Trust is admins' top barrier to AI (29.3%, against 16.1% for cost); 15.3% don't use AI at all (Salesforce Ben surveys, Aug 2026) | https://www.salesforceben.com/5-reasons-salesforce-professionals-distrust-ai/ |
| pain | Admins in an analyst survey of 234 manage more users than in 2020; a solo admin at a 300-person agency says they are drowning | https://www.appsruntheworld.com/survey-finds-agentforce-enriching-salesforce-admins-with-a-catch/ |
| objection | Admins testing Agentforce in Setup said it was slower than doing the work themselves (vendor blog quoting admins, 2026) | https://www.getclientell.com/salesforce-blogs/what-salesforce-admins-are-saying-about-agentforce-2026 |
| pain | Email captured by Einstein Activity Capture sat outside reports and flows; a newer sync option writes email as records but backfills only 180 days (competitor's blog, 2026) | https://revenuegrid.com/blog/einstein-activity-capture-limitations/ · https://www.avoma.com/blog/einstein-activity-capture |

### Service leads (Service Cloud)

| Kind | What they said or did | Source |
|---|---|---|
| objection | A G2 reviewer of Service Cloud and Agentforce Service: AI misleads when knowledge is out of date, and cleaning data first takes months (Oct 2026) | https://aws.amazon.com/marketplace/reviews/reviews-list/prodview-xdmwnsnyxbqou |
| budget signal | A capital-markets reviewer lists high cost and unpredictable pricing as a dislike (Oct 2026) | https://aws.amazon.com/marketplace/reviews/reviews-list/prodview-xdmwnsnyxbqou |
| pain | Escalations reach account owners in a weekly report, sometimes after the renewal call (integration vendor, Sep 2026) | https://tray.ai/blog/support-history-in-crm/ |
| pain | Support quality rarely shows in customer success tools, so a customer with heavy tickets can look healthy in the CRM (helpdesk vendor, Jul 2026) | https://www.kustomer.com/resources/blog/cx-b2b-renewal-decisions/ |
| churn reason | A team saw high bot deflection, but customers who hit the bot on billing churned faster: deflection measured silence, not resolution (May 2026) | https://tianpan.co/blog/2026/05/27/the-deflection-metric-that-lied |

### Financial advisors (adjacent segment)

| Kind | What they said or did | Source |
|---|---|---|
| pain | Writing notes in a meeting pulls attention from the client; notes written afterwards miss follow-ups. Action-item accuracy in one test ranged 62–87% (Aug 2025) | https://www.kitces.com/blog/artificial-intelligence-ai-meeting-notetakers-note-tools-client-communication-accuracy-domentation/ |
| objection | The advisor stays liable for any errors in the software's notes | https://www.kitces.com/blog/artificial-intelligence-ai-meeting-notetakers-note-tools-client-communication-accuracy-domentation/ |
| budget signal | An RIA president reports advisors saving about 2–10 hours a week with notetakers; CRM integration was a key buying question; the firm built consent notices and an AI policy first (May 2025) | https://www.investmentnews.com/fintech/as-ai-notetaking-booms-at-rias-what-guardrails-are-being-put-in-place/260616 |
| churn reason | An independent advisor switched notetakers because of price | https://advisor.ca/practice/technology/what-advisors-need-to-know-about-ai-notetaking-apps/ |
| trigger | In a survey of about 3,000 advisors, AI notetakers went from one product to fourteen in a year; CRM is still the most valued software (Mar 2026) | https://www.familywealthreport.com/printarticle.php?id=207153 |

## What the product manager knows that the files don't

| Customer type | What | Tag |
|---|---|---|
| Sales managers | In our win-loss calls, managers who bought Clari said they did it because they'd stopped believing the Sales Cloud pipeline | `[PM, illustrative]` |
| Account executives | Reps at our mid-market customers turn on Activity Capture and then stop checking whether it worked | `[PM, illustrative]` |
| Revenue operations | Most mid-market customers have one or two revenue operations people who also own the Salesforce admin work | `[PM, illustrative]` |
| Service leads | Customers that run both clouds rarely connect case escalations to open deals | `[PM, illustrative]` |

## Gaps

What we couldn't find, so any persona that needs it marks it `[assumed]` or `[PM, illustrative]`:

- Sales Cloud customers in their own words on Reddit, G2, Capterra and TrustRadius: the pages couldn't be opened.
- A rep saying whether they'd trust a record they didn't type. Nothing either way.
- A first-hand admission that reps hide bad news on purpose. What exists points to optimism, pressure and lack of time, not deliberate hiding.
- Hours managers spend chasing reps and rebuilding the forecast: no measured figure; the economics in `experiences.md` use the product manager's estimate.
- Service manager job postings and what service leads are measured on.
- Budgets and renewal moments for any of these roles.
