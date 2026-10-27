# Salesforce Sales Cloud and Service Cloud · Opportunities

Built from `product.md`, `ai-levels.md`, `market-map.md` and `market-moves.md` on 27 Oct 2026. No `documents/` in this example, so the evidence is public: Salesforce's own surveys, job postings, reviews and trade press. Some surveys are from 2024; their dates are given.

## The work around the product

| # | Step | What happens | Who | Software | Still manual | Coverage | Who's moving here | Our AI level |
|---|---|---|---|---|---|---|---|---|
| 1 | Lead capture and qualification | Leads come in or are found; someone contacts and qualifies them | SDR, account executive | Salesforce, HubSpot, Zoho | Reps log notes, stages and outcomes by hand in the CRM [https://www.myjobmag.co.ke/job/sales-development-representative-sdr-pavago] | partial | Microsoft Dynamics 365, HubSpot, Clay | 4 (Agentforce Engagement) |
| 2 | Prospect research and outreach | Research target accounts, build lists, send sequences, call | SDR, account executive | LinkedIn Sales Navigator, Apollo, Salesforce | Reps research and build lists by hand, then track every activity in Salesforce [https://www.workingnomads.com/jobs/sales-development-representative-hackerrank] | partial | Clay, Attio | 3 (research on request) |
| 3 | Meetings and activity logging | Calls, emails and meetings get recorded on the deal | Account executive | Salesforce, Gong, many other apps | Non-selling work took 70% of reps' time in 2024 [https://www.salesforce.com/news/?p=79781]; manual data entry is about 11% of the week [https://www.apollo.io/magazine/the-toggle-tax-what-1200-daily-app-switches-are-costing-sales-teams] | partial | Day.ai, Microsoft 365 Copilot, Gong, Coffee | 2 (activity capture, call summaries) |
| 4 | Opportunity management and forecasting | Reps update stage, amount and close date; managers review pipeline and roll up a commit | Account executive, sales manager, revenue operations | Salesforce Forecasts, Clari, spreadsheets | Weekly forecast roll-ups in spreadsheets take about an hour and go stale fast [https://zapier.com/templates/details/weekly-forecast-rollup]; only 45% of sales leaders had high confidence in their forecast (Gartner, 2020) [https://www.gartner.com/en/newsroom/press-releases/2020-02-12-gartner-says-less-than-50--of-sales-leaders-and-selle] | partial | Clari | 2 (Einstein Forecasting) |
| 5 | Quoting and close | Configure, price, approve, sign | Account executive, deal desk | Salesforce CPQ and Revenue Cloud | A reviewer reports many workarounds in CPQ [https://trustradius.com/reviews/salesforce-cpq-formerly-steelbrick-2018-10-24-18-03-16] | unknown | Oracle Fusion CX | not covered in `ai-levels.md` |
| 6 | Handoff to customer success | Deal context passes to onboarding | Account executive, customer success manager | Salesforce, Slack | Handoffs run on scattered notes and Slack messages (vendor blog) [https://www.rocketlane.com/blogs/sales-to-customer-success-handoff] | partial | none on the map | not covered |
| 7 | Case intake and routing | Cases arrive by phone, email, chat or web and get classified and assigned | Service rep, service manager | Service Cloud | No specific evidence found | unknown | SAP, Microsoft Dynamics 365 | 4 (Agentforce service agents) |
| 8 | Case resolution and knowledge | Resolve the case, write notes, update knowledge | Service rep | Service Cloud | Service agents spent only 39% of their time serving customers in 2024; the rest went to admin, meetings and logging case notes by hand [https://www.cxtoday.com/workforce-engagement-management/salesforce-contact-center-agents-spend-just-39-of-their-time-servicing-customers/] | partial | Sierra, Decagon, HubSpot, ServiceNow | 4 |
| 9 | Reporting, admin and data hygiene | Build reports, import and dedupe data, fix records, answer user requests | Salesforce admin, revenue operations | Salesforce, spreadsheets, Cloudingo, Validity | Admin postings list cleanup, deduplication, reconciliation and a ticket queue of data fixes [https://jobs.workable.com/jobs/83139990-02aa-447b-9f68-5d26b90d22f1.md] [https://www.vaneck.com/globalassets/home/us/our-firm/careers/salesforce-administrator_2025-002.pdf] | partial | none on the map | 1 |

## Opportunities, ranked

| # | Opportunity | Kind | Level | Impact | Effort | Urgency | Evidence | Priority | Band |
|---|---|---|---|---|---|---|---|---|---|
| 1 | The deal record that keeps itself | Grow the base | 4 | 5 | 3 | 4 | Strong | 4.35 | Do first |
| 2 | Outcome-priced service for the fast-setup customer | New revenue | 4 | 4 | 3 | 5 | Strong | 4.25 | Do first |
| 3 | An admin agent for data hygiene and the request queue | Grow the base | 4 | 3 | 2 | 3 | Strong | 3.60 | Strong option |
| 4 | The forecast without the spreadsheet | Grow the base | 4 | 4 | 3 | 3 | Good | 3.55 | Strong option |
| 5 | Case wrap-up done for the rep | Grow the base | 4 | 3 | 2 | 3 | Good | 3.40 | Strong option |
| 6 | "Deals like yours": opt-in benchmarks across customers | New revenue | 5 | 5 | 5 | 2 | Thin | 2.85 | Worth watching |

## 1. The deal record that keeps itself

- **The job today:** after every call, email and meeting, account executives and SDRs type notes, next steps, stage and close date into Salesforce. Postings ask reps to "meticulously track all activities". [https://www.workingnomads.com/jobs/sales-development-representative-hackerrank] Non-selling work took 70% of reps' time in 2024 [https://www.salesforce.com/news/?p=79781], with manual data entry about 11% of the week [https://www.apollo.io/magazine/the-toggle-tax-what-1200-daily-app-switches-are-costing-sales-teams].
- **What the product would do:** an agent listens to calls, reads email and calendar, and updates the deal: contacts, next step, stage, close date, risks. The rep sees a short list of changes and approves or edits them. Fields with high confidence update on their own.
- **For whom:** account executive (user); sales manager (buyer, who gets a pipeline that reflects reality).
- **Kind and level:** grow the base; level 4.
- **Who else is going after it:** Day.ai (agents read email, calendar and meetings), Gong (fills CRM fields from calls), Coffee (says it replaces data entry), Microsoft 365 Copilot (logs to the CRM from Outlook). See `market-map.md`, `market-moves.md`.
- **Ratings:** impact 5 because it defends the core seat and removes the main reason to buy tools on top; effort 3 because Einstein Activity Capture and call summaries exist but reliable field updates across email, calendar and calls are new; urgency 4 because Day.ai and Gong have shipped versions of this; evidence Strong because there are four findings across surveys, job postings and third-party analysis, with a quote from a non-Salesforce source.
- **Priority:** 0.35 × 5 + 0.25 × 4 + 0.20 × 5 + 0.20 × (6 − 3) = 1.75 + 1.00 + 1.00 + 0.60 = 4.35 → Do first
- **Size:** not sized, because there's no public count of Sales Cloud customers or seats to multiply from.
- **First question:** "If the CRM updated your deals for you, what would you need to see before you trusted it?"

## 2. Outcome-priced service for the fast-setup customer

- **The job today:** smaller service teams want an agent that answers customers within days, not a consulting project. Reviewers say Service Cloud setup depends on consultants. [https://capterra.com/p/136189/Salesforce/reviews/] Sierra, Decagon and HubSpot sell agents that resolve conversations and charge per outcome. [https://sierra.ai/customers] [https://decagon.ai/] [https://www.cxtoday.com/contact-center/hubspot-customer-agent-resolution-rate/]
- **What the product would do:** one package of Fin and the Agentforce Help Agent for small and commercial Service Cloud customers: live in a day, connected to their Service Cloud cases and knowledge, paid only per resolved conversation.
- **For whom:** service manager at a small or mid-size company (buyer).
- **Kind and level:** new revenue; level 4.
- **Who else is going after it:** Sierra, Decagon, HubSpot; Attio and Lightfield on the small-CRM side.
- **Ratings:** impact 4 because outcome pricing is a product customers will pay extra for, and Salesforce paid about $3.6B for Fin to win this segment [https://www.salesforce.com/news/press-releases/2026/06/15/salesforce-signs-definitive-agreement-to-acquire-fin]; effort 3 because Fin and Service Cloud must share cases, knowledge and billing; urgency 5 because others already take this job from Salesforce's customers; evidence Strong because there are five findings across reviews, vendor sites and trade press, with third-party quotes.
- **Priority:** 0.35 × 4 + 0.25 × 5 + 0.20 × 5 + 0.20 × (6 − 3) = 1.40 + 1.25 + 1.00 + 0.60 = 4.25 → Do first
- **Size:** 30,000 Fin customers (measured [https://www.salesforce.com/news/press-releases/2026/09/10/salesforce-completes-acquisition-of-fin/]) × 5–15% who also adopt Service Cloud (assumption) × $10,000–$30,000 extra a year each (assumption) = $15M–$135M a year in new Service Cloud revenue. Wide, because both of the last two factors are assumptions.
- **First question:** "Would you move your support desk to Service Cloud if the agent were live in a day and you paid only for resolved conversations?"

## 3. An admin agent for data hygiene and the request queue

- **The job today:** admins run cleanup, deduplication and reconciliation by hand, work a queue of data-fix and field-change requests, and lean on spreadsheets and tools like Cloudingo and Validity. [https://jobs.workable.com/jobs/83139990-02aa-447b-9f68-5d26b90d22f1.md] [https://www.wearedevelopers.com/jobs/ext/6751643/salesforce-administrator-remote] [https://www.vaneck.com/globalassets/home/us/our-firm/careers/salesforce-administrator_2025-002.pdf] Reviewers call advanced automation, reporting and permissions hard. [https://g2.com/products/salesforce-crm/reviews]
- **What the product would do:** an agent that finds duplicates and broken records, proposes merges and fixes, and works simple requests from users (a new field, a report, a permission), with the admin approving each batch.
- **For whom:** Salesforce admin or revenue operations lead (influences the renewal).
- **Kind and level:** grow the base; level 4.
- **Who else is going after it:** no one on the map; Cloudingo and Validity cover deduplication.
- **Ratings:** impact 3 because admins shape renewals and complexity is the top complaint; effort 2 because the data and metadata are already in the platform; urgency 3 because the complexity complaint is visible in every review site; evidence Strong because there are three postings plus review summaries, two kinds of source, with quotes from employers.
- **Priority:** 0.35 × 3 + 0.25 × 3 + 0.20 × 5 + 0.20 × (6 − 2) = 1.05 + 0.75 + 1.00 + 0.80 = 3.60 → Strong option
- **Size:** not sized: no public count of Salesforce admins or of time spent on data fixes.
- **First question:** "What share of your week goes to fixing data and small requests, and which would you hand off first?"

## 4. The forecast without the spreadsheet

- **The job today:** managers export pipeline, roll it up in spreadsheets each week and chase reps for updates. [https://zapier.com/templates/details/weekly-forecast-rollup] Users call forecast exports cumbersome. [https://community.salesloft.com/product-q-a-11/need-enhanced-forecasting-reporting-1921] Confidence in forecasts was low in Gartner's 2020 survey. [https://www.gartner.com/en/newsroom/press-releases/2020-02-12-gartner-says-less-than-50--of-sales-leaders-and-selle]
- **What the product would do:** an agent inspects every deal each week, flags slipped dates and missing steps, asks reps only about what changed, and drafts the commit with reasons. The manager edits and submits.
- **For whom:** sales manager or VP of sales.
- **Kind and level:** grow the base; level 4.
- **Who else is going after it:** Clari.
- **Ratings:** impact 4 because forecasting is something leaders pay extra for, as Clari shows; effort 3 because it needs opportunity 1's clean records to work well; urgency 3 because the gap is noticed and Clari sells into it; evidence Good because there are three findings, mostly from search snippets and one dated survey.
- **Priority:** 0.35 × 4 + 0.25 × 3 + 0.20 × 4 + 0.20 × (6 − 3) = 1.40 + 0.75 + 0.80 + 0.60 = 3.55 → Strong option
- **Size:** not sized: no public figure for how many Sales Cloud customers forecast in Salesforce.
- **First question:** "Walk me through last week's forecast call: what did you do in a spreadsheet, and why?"

## 5. Case wrap-up done for the rep

- **The job today:** when a rep handles a case, they write notes and a summary by hand; service agents spent only 39% of their time with customers in 2024. [https://www.cxtoday.com/workforce-engagement-management/salesforce-contact-center-agents-spend-just-39-of-their-time-servicing-customers/] Salesforce's own training says forms and case data pull agents away from customers. [https://trailhead.salesforce.com/content/learn/modules/einstein-work-summaries-service/get-to-know-future-of-service-and-generative-ai]
- **What the product would do:** at the end of every human-handled case, the agent writes the notes, sets the fields, drafts a knowledge article if the answer was new, and closes the case once the rep approves.
- **For whom:** service rep (user), service manager (buyer).
- **Kind and level:** grow the base; level 4.
- **Who else is going after it:** ServiceNow, Microsoft Dynamics 365 (case agents).
- **Ratings:** impact 3 because it's a clear time saving for every rep; effort 2 because work summaries already exist; urgency 3 because Microsoft's case agent already updates and closes cases; evidence Good because there are two findings, both from Salesforce's own research.
- **Priority:** 0.35 × 3 + 0.25 × 3 + 0.20 × 4 + 0.20 × (6 − 2) = 1.05 + 0.75 + 0.80 + 0.80 = 3.40 → Strong option
- **Size:** not sized: no public count of Service Cloud reps.
- **First question:** "How long does wrap-up take after a typical case, and what do you skip when you're busy?"

## 6. "Deals like yours": opt-in benchmarks across customers

- **The job today:** sales managers judge whether a deal is healthy from their own team's history. Einstein scoring learns from each customer's own data only. [https://help.salesforce.com/s/articleView?id=sales.sales_core_artificial_intelligence.htm&language=en_US&type=5] Nobody on the map offers benchmarks from many companies' deals (`market-map.md`).
- **What the product would do:** customers who opt in share anonymised deal patterns. In return each team sees how deals like theirs, in their industry and size, tend to move: typical cycle length, the steps that predict a win, where similar deals stall.
- **For whom:** sales manager or VP of sales; revenue operations.
- **Kind and level:** new revenue; level 5.
- **Who else is going after it:** Clay says its agents share what they learn across sales plays (stated direction). [https://www.clay.com/]
- **Ratings:** impact 5 because it would open a new paid data product; effort 5 because Salesforce would need customers' permission to learn across their data, which it doesn't have today; urgency 2 because no one has shipped it; evidence Thin because the only finding is the gap on the map, plus the product manager's belief.
- **Priority:** 0.35 × 5 + 0.25 × 2 + 0.20 × 2 + 0.20 × (6 − 5) = 1.75 + 0.50 + 0.40 + 0.20 = 2.85 → Worth watching
- **Size:** not sized: no measured factor.
- **First question:** "Would you share anonymised deal data with other companies if you got their benchmarks back? What would you need to be sure of first?"

## Open questions

- Sales-to-customer-success handoff: evidence so far is vendor blogs only. Worth asking customers whether it hurts.
- Quoting: one reviewer reports workarounds; not enough to call it an opportunity yet.
- Case routing: no evidence of manual work found.
- First-hand review quotes from G2, Capterra and TrustRadius couldn't be read in full for this example. A real run should add them, or the product manager's own customer notes in `documents/`.
