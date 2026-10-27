# Salesforce Sales Cloud and Service Cloud · Where value flows

> Illustrative example built from public sources on 27 Oct 2026. Not affiliated with or endorsed by Salesforce. Anything tagged `[PM, illustrative]` is invented to show what a product manager would add.

Built from `../product.md`, `../vision/ai-levels.md`, `../vision/opportunities.md`, `../vision/market-moves.md`, the discovery reports and the product manager's answers on 27 Oct 2026.

**The shift:** today most of the value Salesforce charges for comes from seats for people who type deals and cases into the CRM, while reps' time, tools on top and partners take the work around it → at level 5, sales teams pay for a forecast they trust and benchmarks they can't get elsewhere, and service teams pay per resolved conversation.

## Today

| Persona | The value they get | Who pays | For what | Roughly how much | Source |
|---|---|---|---|---|---|
| Account executive | One view of each account and deal; activity capture; on the AI editions, research and drafts on request | Buyer (the company) | Seat, by edition; Agentforce add-on | $25–$550 per user per month by edition; Agentforce for Sales add-on $125 per user per month | [https://www.salesforce.com/sales/pricing/] [https://www.salesforce.com/agentforce/pricing/] |
| Sales manager or VP of sales | Forecasts from live deal data, quotas, coaching data | Buyer, often with revenue operations | Same seat; more AI in Core and above | Included in the seat; Max at $550 bundles the full AI suite | [https://www.salesforce.com/sales/pricing/] |
| Salesforce admin or revenue operations | One configurable platform for data, flows and reports | Buyer | Included in seats; partner and admin costs on top | Partner work not priced publicly; the consulting ecosystem earns nearly six times Salesforce's revenue | [https://www.forrester.com/blogs/the-salesforce-consulting-landscape-shows-no-sign-of-slowdown/] |
| Service rep and service manager | Cases, knowledge and channels in one console; agents that resolve routine questions | Buyer (head of service) | Seat; plus usage or outcome for agents | $25–$550 per user per month; agents $2 per conversation, or Flex Credits at about $0.10 per action; Help Agent $2 per resolution | [https://www.salesforce.com/service/pricing/] [https://www.salesforce.com/agentforce/pricing/] |

`[PM, illustrative]` Most of our sales revenue comes from Enterprise-level seats for reps and managers. AI is still a small share of a typical account's bill.

## Where value leaks today

Value the product creates or could create, but that goes somewhere else.

| The leak | Where it goes instead | How big | Source |
|---|---|---|---|
| Reps type notes, stages and next steps by hand | The customer's own manual work | Non-selling work took 70% of reps' time in 2024; data entry about 11% of the week | `../vision/opportunities.md` |
| Weekly forecast roll-ups | A spreadsheet | Done by hand and stale fast; only 45% of sales leaders trusted their forecast (Gartner, 2020) | `../vision/opportunities.md` |
| Call capture, CRM field updates and forecasting | Other tools on top: Gong, Clari, Coffee | Not verified: their prices aren't public | `../vision/market-moves.md` |
| Setup, configuration and data fixes | Partners, admins and apps like Cloudingo and Validity | Consulting around Salesforce is nearly six times its revenue; 91% of customers run an AppExchange app | [https://www.forrester.com/blogs/the-salesforce-consulting-landscape-shows-no-sign-of-slowdown/] [https://smartbridge.com/salesforce-appexchange-apps-top-20-for-2026/] |
| Service conversations resolved by AI-native agents | Another tool: Sierra, Decagon, HubSpot | Not measured. `[PM, illustrative]` AI-native agents show up in most mid-market service deals we lose | `exposure.md` |
| Years of pipeline and case history across customers | Not charged for: not packaged as benchmarks | Unknown | `../vision/ai-levels.md`, `protection.md` |
| Employee use of agents on the per-user add-on | Not charged for: usage is unmetered | Unknown | [https://www.salesforce.com/agentforce/pricing/] |

## At the vision's target level

Level 5, AI Domain Intelligence, by the end of 2028 (`../vision/vision.md`).

| Persona | The job AI does | The value they get | What they'd pay for | Source |
|---|---|---|---|---|
| Sales manager or VP of sales | Keeps every deal current, drafts the forecast with a range and reasons, and compares deals with similar ones at other companies | A forecast they trust; time spent coaching instead of chasing | A yearly benchmark subscription per sales team, priced on pipeline managed `[PM, illustrative]` | `../vision/vision.md` |
| Account executive | Captures every call, email and meeting and proposes record updates | Approves a short list instead of typing; more selling time | Paid by the buyer as part of the outcome, not as a seat to type into `[PM, illustrative]` | `../vision/vision.md` |
| Service manager | Resolves routine conversations end to end; writes up the rest | Lower cost per case; faster answers | Per resolved conversation, as the Help Agent already charges | [https://www.salesforce.com/agentforce/pricing/] |
| Revenue operations | Keeps data clean and handles simple requests, with approval | Fewer fixes and tickets | Included, to protect the renewal `[PM, illustrative]` | `../vision/opportunities.md` #3 |

## Who else could capture it

| Who | How they'd capture the value | What keeps it with us |
|---|---|---|
| A general AI assistant: Microsoft 365 Copilot, ChatGPT | Logs activity and drafts updates from Outlook, Teams or ChatGPT. Headless 360 already lets outside agents call Salesforce actions, so the assistant could become where reps work [https://www.destinationcrm.com/Articles/CRM-News/CRM-Across-the-Wire/Salesforce-Expands-Headless-360-Across-Its-Portfolio-176206.aspx] | Data and trust: the record, permissions and history stay in Salesforce; benchmarks need data across many customers |
| A challenger: Sierra, Decagon, Day.ai, Clari, Gong | Sell the outcome on top of the CRM: resolved conversations, captured activity, forecasts [https://www.vktr.com/customer-experience/sierra-raises-950m-at-15b-valuation-eyes-transformation-beyond-customer-support/] | Workflow: if the record keeps itself, the gap they fill shrinks; Fin gives a fast-setup answer in service |
| A partner | Consultancies and AppExchange apps build agents and data fixes for customers | Distribution: bring partners in as builders on Agentforce rather than around it (`protection.md`) |
| The customer's own build | Large customers wire their own models to Salesforce data through APIs and MCP | Trust and distribution: governed access, the trust layer, and agents that already work in the product |

## How we'd charge

- **Today:** per seat by edition ($25–$550 per user per month), plus the Agentforce add-on ($125 per user per month), Flex Credits, $2 per conversation, or $2 per Help Agent resolution [https://www.salesforce.com/sales/pricing/] [https://www.salesforce.com/agentforce/pricing/]. Large customers increasingly buy seat-based agentic licence agreements [https://www.theregister.com/2025/12/12/ai_agents_salesforce_pricing/].
- **This product update:** agents for the sales team's forecast flow at $45 a user a month, a fixed line at renewal, about 6.7% of the labour it saves a typical customer (`../roadmap/roi.md`). `[PM, illustrative]`
- **Tomorrow:** per resolution in service; in sales, a benchmark subscription per sales team priced on pipeline managed, on top of fewer, cheaper seats. `[PM, illustrative]`
- **What has to be true:**
  - Customers believe the forecast and benchmarks are accurate, and opt in to sharing anonymised deal data.
  - We measure accepted updates, forecast accuracy and resolutions in a way customers can audit.
  - Outcome revenue grows faster than seat revenue shrinks.

## Open questions

- How much of a typical account's spend sits on seats that exist mainly to type into the CRM? `[PM, illustrative]` Not known yet.
- What do customers pay Gong, Clari or Day.ai alongside Salesforce? Not verified.
- Would sales leaders pay for benchmarks on top of seats, and at what price?
- If outside assistants call Salesforce through Headless 360, how do we charge for that use?
