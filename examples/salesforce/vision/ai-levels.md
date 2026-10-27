# Salesforce Sales Cloud and Service Cloud · value at each AI level

> Illustrative example built from public sources on 27 Oct 2026. In a real run the product manager confirms each row; here, rows tagged `[PM, illustrative]` are invented.

**Level today:** 4, AI Delegated: the highest level with value that is shipped and used. Agentforce service agents resolve customer conversations end to end, with people handling the rest, and named customers report the results.
**Planned or in beta:** none verified at level 5 or 6. Headless 360 (agents outside Salesforce calling its actions) is shipped but is plumbing, not a higher level.

## Summary

| Level | Value today? | Main features | For whom | How they pay |
|---|---|---|---|---|
| 1 System of Record | Yes | Accounts, contacts, leads, deals, forecasts, cases, knowledge, workflows, reports | All four personas | Per seat, by edition ($25–$550 per user per month) |
| 2 AI Assisted | Yes | Einstein lead and opportunity scoring, forecasting, call and record summaries, reply suggestions | Account executives, sales managers, service reps | Some included; most in Einstein for Sales or higher editions |
| 3 AI Directed | Yes | Close plans and emails on request, Agentforce Coworker, Agentforce Sales in ChatGPT | Account executives, service reps | Agentforce add-on ($125 per user per month), Max edition, or $50 Coworker licence |
| 4 AI Delegated | Yes | Agentforce service agents resolving conversations; Agentforce Engagement working leads; Fin | Service managers and their customers; sales managers | Per conversation ($2), per resolution, or Flex Credits (about $0.10 per action) |
| 5 AI Domain Intelligence | No | none | | |
| 6 System of Understanding | No | none | | |

## Level 1 · System of Record

People do the work; the product stores and runs it.

| Feature | For whom | The value they get | How they pay | Status | Source |
|---|---|---|---|---|---|
| Accounts, contacts, deals and pipeline in one place, with automatic capture of calls, emails and meetings | Account executive, user | One view of each customer and deal | Per seat, by edition | Shipped and used | https://www.salesforce.com/sales/ |
| Forecasting, quotas and commissions | Sales manager, buyer and user | A forecast built from deal data; quota tracking | Per seat, by edition | Shipped and used | https://www.salesforce.com/sales/ |
| Cases, knowledge, assets, contact center and field service | Service rep and manager | Every customer issue tracked from first contact to close | Per seat: Starter $25 to Max $550 | Shipped and used | https://www.salesforce.com/service/ · https://www.salesforce.com/service/pricing/ |
| Configuration, permissions, flows and reports | Admin or revenue operations | The system fits how the company sells and serves | Included; complexity drives partner and admin costs | Shipped and used | https://g2.com/products/salesforce-crm/reviews |

## Level 2 · AI Assisted

People do the work; AI suggests.

| Feature | For whom | The value they get | How they pay | Status | Source |
|---|---|---|---|---|---|
| Einstein Lead Scoring and Opportunity Scoring | Account executive | Knows which leads and deals to work first | Sales Cloud Einstein licence; opportunity scoring also with a standard licence | Shipped | https://help.salesforce.com/s/articleView?id=sales.sales_core_artificial_intelligence.htm&language=en_US&type=5 |
| Einstein Forecasting | Sales manager | A predicted forecast next to the team's call | Sales Cloud Einstein licence | Shipped | same as above |
| Call summaries and conversation insights | Account executive, sales manager | No notes to write after a call; managers see what was said | Einstein Conversation Insights plus Einstein for Sales add-on | Shipped | same as above |
| AI-generated reply suggestions for service | Service rep | Faster, personalised replies; Wonolo reports 20% shorter handle times | Included in higher editions or add-on (exact packaging not verified) | Shipped and used | https://www.salesforce.com/sales/ |

## Level 3 · AI Directed

A person asks; AI does one task; the person checks each result.

| Feature | For whom | The value they get | How they pay | Status | Source |
|---|---|---|---|---|---|
| Einstein for Sales: summarise a record, draft sales emails, create a close plan | Account executive | Drafts on request, reviewed before sending | Einstein for Sales add-on | Shipped | https://help.salesforce.com/s/articleView?id=sales.sales_core_artificial_intelligence.htm&language=en_US&type=5 |
| Account research by an agent on request | Account executive | Carnegie Learning cut rep research from up to an hour to 5–10 minutes | Agentforce for Sales add-on, from $125 per user per month | Shipped and used | https://www.salesforce.com/news/stories/agentforce-customer-success-stories/ · https://www.salesforce.com/sales/pricing/ |
| Agentforce Sales app in ChatGPT: ask for leads, update deals, build an account plan saved back to Salesforce | Account executive | Works the CRM from where they already are | Not stated | Shipped (December 2025) | https://www.salesforceben.com/salesforce-brings-agentforce-sales-to-chatgpt/ |
| Agentforce Coworker: one place to ask questions across CRM, documents and Slack, and hand tasks to agents | All employees | Answers and actions without hunting across tools | $50 per user per month, unmetered in Max | Shipped; general availability timing not verified | https://www.salesforce.com/agentforce/pricing/ |

## Level 4 · AI Delegated

AI does the job end to end; people handle exceptions.

| Feature | For whom | The value they get | How they pay | Status | Source |
|---|---|---|---|---|---|
| Agentforce service agents resolving customer conversations and acting in systems | Service manager (buyer); their customers | Engine: 50% of chat cases resolved automatically, 15% less handle time, 16% higher chat satisfaction. 1-800Accountant: 70% of chats resolved in tax week 2025 | $2 per conversation, or Flex Credits | Shipped and used | https://www.salesforce.com/customer-stories/engine/agentic-service/ · https://www.salesforce.com/news/stories/agentforce-customer-success-stories/ · https://www.salesforce.com/agentforce/pricing/ |
| Agentforce on Salesforce's own help site | Salesforce's customers | More than five million conversations; over 63% resolved instantly | Internal use | Shipped and used | https://www.salesforce.com/agentforce/case-study/customer-zero |
| Agentforce Help Agent, ready-made service agent | Service manager | Pays only when the agent resolves an issue; no charge if the customer asks for a human | Per resolution ($2 per trade press) | Shipped (June 2026); usage not yet reported | https://www.cxnetwork.com/cx-experience/news/salesforce-launches-pay-per-resolution-agent/amp |
| Agentforce Engagement (formerly the SDR agent): emails new leads, answers replies, books meetings, hands qualified leads to reps | Sales manager; account executives get meetings | Salesforce's own use (Jul–Oct 2025): 68,000 leads re-engaged, 800 meetings booked autonomously | Einstein for Sales or Agentforce add-on | Shipped and used | https://help.salesforce.com/s/articleView?id=sales.sales_agent_sdr_parent.htm&language=en_US&type=5 · https://www.salesforce.com/ap/blog/ai-for-lead-qualification/?bc=OTH |
| Fin, the customer agent from the former Intercom | Service teams, especially smaller ones | 76% average resolution rate claimed; more than 30,000 customer companies | Fin's own pricing (outcome-based) | Shipped and used; part of Salesforce since 10 Sep 2026 | https://www.salesforce.com/news/press-releases/2026/09/10/salesforce-completes-acquisition-of-fin/ |

## Level 5 · AI Domain Intelligence

AI brings expertise learned from data across many customers.

none. Einstein scoring and forecasting learn from each customer's own history, which is level 2. No public evidence of Sales Cloud or Service Cloud giving benchmarks or recommendations drawn from many customers' data. [https://help.salesforce.com/s/articleView?id=sales.sales_core_artificial_intelligence.htm&language=en_US&type=5]

Planned: the product manager's target, see `vision.md` `[PM, illustrative]`.

## Level 6 · System of Understanding

The product understands how the domain works, anticipates and acts.

none.
