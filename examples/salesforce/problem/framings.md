# Salesforce Sales Cloud and Service Cloud · Framing the problem

> Illustrative. Built from public sources; not affiliated with or endorsed by Salesforce. The product manager's answers are invented to show how `/ai-product-problem` works, tagged `[PM, illustrative]`.

Built from `../product.md`, `../vision/`, `../discovery/`, `evidence.md` and the product manager's answers on 27 Oct 2026.

## The job

The problem hits two people. The rep does the typing; the sales manager feels the cost. We asked "why?" until we reached the job behind the task: "update the opportunity" → "give my manager a number they can believe" → "call the quarter and spend my time on the deals that need help". `[PM, illustrative]`

**When** the quarter is on the line and the forecast call is coming, **I want to** know where every deal really stands, without chasing my reps for updates, **so I can** call the number with confidence and coach the deals that need it.

- **The struggling moment:** the day before the forecast call. The manager opens the pipeline, sees close dates in the past and next steps from last month, and starts messaging reps one by one. The reps stop selling to update records, or answer from memory. `[PM, illustrative]` Practitioners describe the same moment: managers forecast from their own spreadsheet because the CRM is behind (https://www.revopscoop.com/post/salesforce-forecasting).
- **Functional:** a current record of every deal, and a forecast built on it. · **Emotional:** for the manager, not being surprised at quarter end; for the rep, not feeling like a typist. · **Social:** for the manager, being the leader whose number holds in front of the VP and the board; for the rep, being seen as on top of their deals.

**Who has it most:** the sales manager or VP of sales at a mid-market B2B company with 8–40 sellers (the buyer). The account executive pays the time. `[PM, illustrative]`

## Pressure test

| Question | Answer | Evidence |
|---|---|---|
| Is it real? | Yes. Sellers say they spend about 40% of their time selling, and only about a third fully trust their data. Practitioners on Salesforce, Zoho and dealership CRMs describe the same chase in their own words | `evidence.md`; https://www.salesforce.com/news/stories/state-of-sales-report-announcement-2026/ · https://www.salesforce.com/news/?p=79781 |
| Does it hurt enough? | Yes. It costs reps selling time and costs leaders a forecast they can believe. Companies already pay to make it go away: Gong passed $500M in annual recurring revenue, and some teams hire assistants to update close dates | https://en.globes.co.il/en/article-1001542789 · https://stealthagents.com/virtual-assistant-salesforce-support |
| What do they do today? | Shadow spreadsheets, a manager's own forecast sheet, scheduled resets of past-due close dates, blocking an hour a day for updates, tools on top, and rules that tie new leads to logging | `evidence.md`, workarounds |
| Why us? | We hold the record every other tool reads from, years of deal history, and the activity already captured from email, calendar and calls. Reps and managers already work in Sales Cloud | `../product.md`, `../discovery/protection.md` |
| Why now? | Day.ai, Gong, Coffee and Microsoft 365 Copilot already fill CRM fields from calls and email (`../vision/market-map.md`). If they keep the record current, the value of the record moves to them (`../discovery/value.md`). Investors are already pricing the risk to seat revenue (`../discovery/discovery.md`) | `../vision/market-moves.md`, `../discovery/exposure.md` |

### The four forces

| Force | What we found | Source |
|---|---|---|
| Push | Sellers say they sell only 40% of the time. Leaders don't trust reps' commits: 24% do. Managers chase reps before every forecast call | https://www.salesforce.com/news/stories/state-of-sales-report-announcement-2026/ · https://www.gong.io/press/as-economic-headwinds-grow-stronger-only-24-of-sales-leaders-are-confident-in-their-teams-revenue-forecast |
| Pull | Others already show it can work: a dealership manager calls automatic call logging the most efficient method they've seen; 27,000+ financial advisors use an assistant that writes their notes and CRM updates; leaders using what was said with customers forecast closer to the actual | https://forum.dealerrefresh.com/threads/how-often-do-your-sales-reps-actually-update-the-crm-after-customer-calls.13520/ · https://finovate.com/category/jump/ |
| Anxiety | Wrong updates landing in the forecast; reps feeling watched; losing control of what the manager sees. Salesforce's own activity capture left some email outside reports, so customers have been let down before. A default-on data setting dented trust in how Salesforce uses customer data | https://salesforcebreak.com/2026/03/04/einstein-activity-capture-guide/ · https://www.salesforceben.com/salesforces-new-ai-data-setting-sparks-debate-over-what-customers-agreed-to/ |
| Habit | The manager's spreadsheet travels with them from job to job; the weekly forecast call is a ritual; many customers already pay for Gong or Clari and have built their process around them | https://www.revopscoop.com/post/salesforce-forecasting · `../vision/market-moves.md` |

**Switching verdict:** push and pull beat habit. Anxiety decides it. Customers will switch only if they can see why each update was made, correct it easily, and trust that it's right more often than a rep's memory. `[PM, illustrative]`

### The case against it

This might be the wrong problem. Records may be stale because reps choose not to share bad news, not because typing takes too long: one vendor says reps change values and dates to avoid scrutiny (https://www.scratchpad.com/blog/salesforce-issues). If so, removing the typing doesn't fix the forecast. And customers who care most already pay Gong and Clari for this, so we'd be arriving late to a job others do well.

**Our answer:** that's why we widen it. A record built from what actually happened in calls and email doesn't depend on what a rep chooses to report, and Gong's own survey suggests forecasts built that way land closer. Tools on top read from our record; if we leave it stale, we hand them the job. We'll test the "hiding deals" question first, because if it's true the problem is trust, not time. `[PM, illustrative]`

## Thinking bigger

### The BHAG

**By 2031, sellers spend 70% of their week selling, up from 40%, and no sales manager has to ask a rep where a deal stands.**

It's measurable (Salesforce's State of Sales already tracks selling time, https://www.salesforce.com/news/stories/state-of-sales-report-announcement-2026/), dated, about the customer's job, and uncomfortable: it flips the 70% of time that went to non-selling work in 2024 (https://www.salesforce.com/news/?p=79781). It goes beyond `../vision/vision.md`, which targets level 5 by the end of 2028; the vision's day with the System of Understanding is set in 2031, so the BHAG matches it. The vision can be updated later. `[PM, illustrative]`

Options we considered `[PM, illustrative]`:
- "By 2030, nine in ten sales teams on Sales Cloud land within 5% of their forecast." Bold, but forecast accuracy also depends on the market, not only on the job.
- "By 2029, no rep types a deal update by hand." Clear, but it describes a feature, not what the customer gets.
- The chosen one: about the time sellers get back and the chase that disappears, which is what both the rep and the manager feel.

### The job map

The manager's job of calling the quarter, with the reps' inputs. Levels from `../vision/ai-levels.md`.

| Step | What the customer does | Covered by us today? | Our AI level there |
|---|---|---|---|
| Define | Set the quarter's target and the pipeline coverage needed | yes: quotas and forecast categories | 1 |
| Locate | Gather what happened in each deal: calls, emails, meetings | partly: activity capture and call summaries, but some captured email isn't usable in reports | 2 |
| Prepare | Get every record current before the forecast call: stage, amount, close date, next step | partly: reps type it; managers chase | 1 |
| Confirm | Check each deal is real: buyer engaged, next step booked, date believable | partly: opportunity scoring | 2 |
| Execute | Roll up the commit and run the forecast call | partly: Forecasts and Einstein Forecasting; many managers still use a spreadsheet | 2 |
| Monitor | Watch deals move during the quarter and catch slippage | partly: deal tracking flags risk | 2 |
| Modify | Step in: coach the rep, change the plan, bring in help | no: done by people, from memory | none |
| Conclude | Submit the commit, then learn why deals were won or lost | partly: forecast submission; little learning across deals | 1 |

**Where a bigger version of the problem sits:** Locate, Prepare and Confirm are the problem as stated. Monitor, Modify and Conclude are where managers lose the most, and nothing covers Modify today.

### What customers most want fixed

The biggest pains of current customers, beyond the problem we started with.

| Pain | Who | How big | Evidence |
|---|---|---|---|
| More time selling. Data entry is one slice; research, internal meetings and admin are the rest | Account executives, SDRs | 40% of time spent selling; 48% lack bandwidth for outreach | Strong: https://www.salesforce.com/news/stories/state-of-sales-report-announcement-2026/ · https://www.saastr.com/the-40-problem-do-your-sales-reps-really-cover-all-their-accounts-and-is-ai-the-answer-with-yamini-rangan-ceo-hubspot · `evidence.md` |
| A forecast they can believe | Sales managers, VPs of sales | 24–45% confident, depending on the survey | Good: https://www.gong.io/press/as-economic-headwinds-grow-stronger-only-24-of-sales-leaders-are-confident-in-their-teams-revenue-forecast · https://www.gartner.com/en/newsroom/press-releases/2020-02-12-gartner-says-less-than-50--of-sales-leaders-and-selle |
| A simpler, cheaper Salesforce | Admins, buyers | The top complaints on G2 and Capterra | Good: `../product.md` |
| Coaching on real conversations | Newer reps | 46% of Gen Z reps rarely get feedback on their calls | Thin: https://www.salesforce.com/news/stories/state-of-sales-report-announcement-2026/ |

**Bigger than the problem we picked:** selling time. Stale records are one cause of lost selling time, and the BHAG is written around it. `[PM, illustrative]`

### Adjacent segments

Where else this problem is very painful now.

| Segment | Why it hurts there now | How big | Evidence |
|---|---|---|---|
| Financial advisors (RIAs, broker-dealers) | Every client meeting needs notes, tasks, CRM updates and compliance records. Advisors already pay to have it done | 27,000+ advisors on one tool alone, at $100–$120 each a month (2024 prices): about $32M–$39M a year already spent | Good: https://finovate.com/category/jump/ · https://www.wealthmanagement.com/technology/ai-startup-advisors-jump-announces-46m-funding |
| Car dealership sales | Managers enforce logging by tying leads to it and inspect records daily; some dealer tools now log calls automatically | not measured | Thin: https://forum.dealerrefresh.com/threads/how-often-do-your-sales-reps-actually-update-the-crm-after-customer-calls.13520/ |
| Recruiters and staffing firms | Same job, different record: notes after every interview, kept current for the hiring manager | 17.7 hours of manual admin per vacancy, 3.0 of them on post-interview notes (Totaljobs survey of 748 HR leaders, 2025) | Thin: https://recruiterflow.com/blog/recruiter-time/ |

`[PM, illustrative]` We could reach financial advisors through the customers we already have in financial services. Dealerships and recruiters are further from us.

## Three framings

| | As stated | The bigger job | The moonshot |
|---|---|---|---|
| **The problem** | Reps' deal records are never current, so managers don't trust the forecast and reps lose selling time to data entry | Sales managers can't see where every deal really stands, or which ones need them, without chasing reps and rebuilding the forecast by hand. Widened from Locate–Prepare to Monitor, Modify and Conclude | The BHAG: by 2031, sellers spend 70% of their week selling, up from 40%, and no manager has to ask where a deal stands |
| **For whom** | Account executive (user), sales manager | Sales manager or VP of sales (buyer), account executive, revenue operations | Every seller and sales leader on Sales Cloud, plus adjacent segments such as financial advisors |
| **Level** | 2 → 4 | 2 → 4, with a first step toward 5 | 2 → 6 |
| **Value from existing customers** | Selling time back for reps; records current for managers | A forecast managers believe, and time moved from chasing to coaching; less need for tools on top | Most of the non-selling week removed, not just data entry |
| **New customers or revenue** | Little; mostly defends the seat | Some of the spend now going to tools on top (Gong alone passed $500M a year) | Adjacent segments that already pay for the same job, such as financial advisors |
| **Size a year** | $45M–$181M = $9.03B Sales revenue in fiscal 2026 (measured) × 5–10% of it from customers who'd pay for this (assumption) × 10–20% price uplift (assumption) | $135M–$542M = $9.03B Sales revenue in fiscal 2026 (measured) × 10–20% of it from customers who'd pay (assumption) × 15–30% price uplift (assumption) | Not sized: it changes how customers pay, from seats to outcomes, so today's seat revenue isn't a fair base, and nothing measured prices an outcome yet |
| **Evidence** | Strong | Good | Thin |
| **Moves us toward the BHAG** | Removes one slice of non-selling work | Removes the chase: the second half of the BHAG | Is the BHAG |

**Working and sources for the sizes.** Sales revenue (Agentforce Sales) was $9,028M in fiscal 2026, to January 2026 (https://www.sec.gov/Archives/edgar/data/1108524/000110852426000056/crm-q4fy26xexhibit991.htm). As stated: $9,028M × 5% × 10% = $45M; $9,028M × 10% × 20% = $181M. The bigger job: $9,028M × 10% × 15% = $135M; $9,028M × 20% × 30% = $542M. The bigger job assumes more customers and a higher uplift because it reaches the buyer of forecasting tools. For reference, the Agentforce for Sales add-on lists at $125 a user a month next to a $195 Core seat (`../product.md`). Both ranges are wide because two of the three factors are assumptions. Per-seat revenue isn't split by edition, so the shares are of revenue, not of customers.

**Evidence grades.** As stated: Strong (the whole of `evidence.md`). The bigger job: Good, because the forecast findings are surveys and practitioners' accounts, plus Gong's revenue; nothing yet from Sales Cloud managers directly. The moonshot: Thin, because selling time is measured, but nothing shows customers would pay for outcomes instead of seats.
