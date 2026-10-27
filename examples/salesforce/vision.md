# Salesforce Sales Cloud and Service Cloud · AI vision

> Illustrative. The product manager's answers in this file are invented to show how `/ai-product-vision` works, tagged `[PM, illustrative]`. Market and product facts cite the other files in this folder.

**Today:** level 4, AI Delegated. Agentforce agents resolve service conversations and work leads end to end, with named customers reporting results (`market-map.md`, `ai-levels.md`).
**Where we're going:** level 5, AI Domain Intelligence, by the end of 2028. `[PM, illustrative]`

## The vision

By the end of 2028, Sales Cloud keeps every deal up to date on its own and tells each sales team what is working in deals like theirs. Sales managers stop chasing updates and building forecasts in spreadsheets. They spend that time coaching on the deals that matter. `[PM, illustrative]`

## Imagine

*Illustrative sketches, not plans. They show what each level could mean for this product.*

### Our product at each level

| Level | Already there | Our product at this level |
|---|---|---|
| 5 AI Domain Intelligence | **Harvey**: legal research and drafting for law firms [https://www.harvey.ai/]. **OpenEvidence**: answers doctors' questions from the medical literature, with citations [https://www.kleinerperkins.com/perspectives/openevidence-expanding-the-worlds-collective-medical-knowledge/] | Sales Cloud knows how deals move across thousands of companies that opt in. A sales manager opens a deal and sees: "Deals like this, at companies your size, close in 74 days when security review starts before the pricing call. Yours hasn't started." Forecasts come with a range and the reasons behind it. Customers pay a yearly subscription for benchmarks, on top of their seats. |
| 6 System of Understanding | **Waymo**: an autonomous ride-hailing service, no one at the wheel [https://waymo.com/]. **Tempus**: combines clinical and molecular data to guide cancer care [https://d3.harvard.edu/platform-digit/submission/tempus-ai-data-driven-precision-medicine/] | Sales Cloud understands how a company's revenue is made: which accounts are ready to buy, which customers are drifting, what each team can deliver this quarter. It plans the quarter, routes the work to agents and people, and adjusts as deals move. The VP of sales sets the goals and makes the calls only people can make. Customers pay for revenue outcomes, such as pipeline created and deals closed, not seats. |

### A day with our System of Understanding

Priya runs a 25-person sales team at a mid-size software company, in 2031.

At 7:40 she opens Slack. Overnight, Sales Cloud has read every email, call and contract change. It moved three deals forward, and pulled one back because the buyer's champion changed jobs last week. Nobody told it; it noticed the email bounce and the new LinkedIn title. It has already found the new contact and drafted an introduction for the rep to send.

Her forecast is done. It doesn't ask her for a number. It shows the range it expects, based on her team's deals and thousands like them, and the two deals that decide the quarter. Priya disagrees on one; she knows the CFO personally. She overrides it and says why. It remembers.

She never chases a rep for an update again, and never exports pipeline to a spreadsheet. The Monday pipeline call is gone. In its place: one hour with the two reps whose deals look like ones that usually slip in week 10, working out what to do differently.

At 4 pm it flags that a large customer's support cases tripled this month and their renewal is in 90 days. It has already booked time with the account team. Priya spends her day on the people and the judgement calls. The record keeps itself.

**What excites us:** the forecast call disappears, and managers coach instead of chase. `[PM, illustrative]`
**What it would need to know, and the data that takes:** how deals actually move across many companies, which takes customers' permission to learn from their anonymised data. It would also need signals from outside the CRM, such as job changes and support volume, joined to the deal. `[PM, illustrative]`

## Built on

- **The deal record that keeps itself:** Do first, 4.35 (`opportunities.md` #1). The foundation: benchmarks are only as good as the records.
- **The forecast without the spreadsheet:** Strong option, 3.55 (`opportunities.md` #4).
- **"Deals like yours": opt-in benchmarks:** Worth watching, 2.85 (`opportunities.md` #6). This is the level 5 step; it's rated low today because Salesforce doesn't yet have permission to learn across customers. The first step tests exactly that.

## For whom

| Persona | The problem it removes | What changes in their day |
|---|---|---|
| Sales manager or VP of sales | Forecasts built from what reps remember to type in, rolled up in spreadsheets (`opportunities.md` steps 3–4) | No weekly roll-up; time goes to coaching on the deals most likely to slip `[PM, illustrative]` |
| Account executive | Most of the week spent on non-selling work, including data entry (`opportunities.md` #1) | Approves a short list of record changes instead of typing them `[PM, illustrative]` |

## What AI takes over

| Workflow | Today | Tomorrow |
|---|---|---|
| Opportunity to close: keeping deals current and forecasting | Reps log activities and update stages by hand; managers chase updates and roll up the forecast in spreadsheets (`opportunities.md` steps 3–4) | Agents capture every activity and update deals; the forecast drafts itself with reasons and benchmarks. People decide the commit, the strategy and anything the agent flags as unsure `[PM, illustrative]` |

## Why us

- Years of pipeline, activity and case history across Salesforce's customers (`product.md`).
- Agents already working at level 4 in both sales and service, with customer results (`ai-levels.md`).
- Data 360 to join outside signals to the deal, and Headless 360, Slack and the ChatGPT app to show up where sellers work (`product.md`, `market-moves.md`).
- Distribution: sellers and managers already live in Sales Cloud. `[PM, illustrative]`

## The opening

Level 5 is empty for everyone on the map, and level 4 is thin on the sales side: Salesforce's own lead agent, Microsoft's lead qualification agent and Clay's research agents (`market-map.md`).

## Others moving this way

| Who | At which level | What makes our vision different |
|---|---|---|
| Clari | Not placed; a forecasting tool on top of the CRM (`market-moves.md`) | We own the record it forecasts from; when the record keeps itself, the forecast lives where the deal does |
| Day.ai | 3 (`market-map.md`) | Captures activity well for new teams; we bring years of history and benchmarks across many companies |
| Microsoft Dynamics 365 and 365 Copilot | 4 and 3 (`market-map.md`) | Strong in Outlook and Teams; we aim at the forecast and benchmarks, not just the inbox |
| Clay | 4 (`market-map.md`) | Strong at research before the deal; we cover the deal from first meeting to close |

## What customers would pay for

If an agent sat on top of our data tomorrow, customers would stop paying for seats that exist mainly to type into the CRM, and for separate tools that capture activity or roll up the forecast (`market-moves.md`). They would pay instead for a forecast they trust and for benchmarks they can't get anywhere else: a yearly subscription per sales team, priced on pipeline managed, not seats. `[PM, illustrative]`

## First step

Run a one-quarter pilot of "the deal record that keeps itself" with 10 Sales Cloud customers. Measure the share of agent-proposed updates reps accept without editing, and the hours saved per rep. In the same interviews, ask 20 sales leaders the opt-in question: would they share anonymised deal data to get benchmarks back, and on what terms? `[PM, illustrative]`

## Open questions

- Will customers give permission to learn across their data, and under what guarantees?
- How accurate do automatic updates need to be before reps stop checking them?
- How does this sit next to Clari and Gong, which many customers already pay for?
- Does pricing on pipeline managed undercut seat revenue faster than it grows new revenue?
