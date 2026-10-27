# Salesforce Sales Cloud and Service Cloud · ROI and pricing

> Illustrative. Built from public sources; not affiliated with or endorsed by Salesforce. The product manager's answers are invented, tagged `[PM, illustrative]`.

What this product update is worth, to customers and to us, and how we charge for it. Built from `../research/experiences.md` (the double cost and the new economics), `../discovery/value.md`, `features.md`, `../flows/panel-tests.md` and the product manager's answers on 27 Oct 2026. Every number shows its working; assumptions are labelled.

## For a typical customer

The ideal customer in `../research/icp.md`: 25 account executives, 5 sales managers and 2 revenue operations people on Sales Cloud Core `[PM, illustrative]`. This update covers flows 1 and 2 (experiences 1 and 2), not hygiene, so revenue operations' time doesn't change yet.

| | Today | With this update |
|---|---|---|
| Licence | $74,880 | $74,880 |
| Agents | – | $17,280 |
| People's time using the product | $395,968 | $139,288 |
| **Total a year** | **$470,848** | **$231,448** |

- **They save:** $239,400 a year (51%); their people get 3,277 hours back: 1,725 for reps keeping deals current, 862 for reps answering the chase, 690 for managers.
- **Their return:** every $1 they pay for agents gives back $14.85 of people's time.
- **Working:** licence: 32 seats × $195 a user a month (Core list, https://www.salesforce.com/sales/pricing/) × 12 = $74,880. Agents: 32 × $45 × 12 = $17,280. People's time with the update: reps 25 × 0.75 hours a week × 46 weeks × $72 = $62,100; managers 5 × 1 hour × 46 × $102 = $23,460; revenue operations unchanged at $53,728; total $139,288. Labour saved $395,968 − $139,288 = $256,680; $256,680 ÷ $17,280 = 14.85. Hours, rates and people counts as in `../research/experiences.md`: wages measured (BLS), hours a week `[PM, illustrative]`.
- **Against the research economics:** `../research/experiences.md` counted experiences 1, 2 and 4 with agents at the $125 list price of the Agentforce for Sales add-on as a placeholder: $221,872 a year, a $248,976 saving. This update leaves out hygiene (experience 4, Next) and uses the price chosen below. When hygiene follows in Next, at no extra price, revenue operations' time falls to $13,432, the hours reach 3,829 as in research, and the customer's total falls to $191,152, a $279,696 saving (59%).

## For us

| | Per customer a year | Across about 12,060 customers who'd buy |
|---|---|---|
| New agent revenue | $17,280 | $208M |
| Cost to run the agents | $3,456 | $42M |
| Cost to build the update (one-off) | – | $4M |
| **Net** | **$13,824** | **about $163M** |

- **Customers who'd buy:** about 12,060 typical-customer equivalents = $903M ÷ $74,880, where $903M is 10% (assumption: the low end of the share used in `../problem/framings.md`) of $9.03B Sales revenue in fiscal 2026 (measured, https://www.sec.gov/Archives/edgar/data/1108524/000110852426000056/crm-q4fy26xexhibit991.htm). Salesforce doesn't report customer counts, so this counts revenue, not companies.
- **New revenue across them:** $903M × ($45 ÷ $195) = $208M. That's a 23% uplift on a Core seat, inside the 15–30% uplift `../problem/problem.md` assumed, and $208M sits inside its $135M–$542M opportunity.
- **Cost to run:** 20% of the price (assumption: model and compute for reading each deal's activity and drafting the brief). **Cost to build:** $4M `[PM, illustrative]`, from the product manager.
- **Per customer:** revenue rises from $74,880 to $92,160, 1.23 times.

## How we charge

Salesforce's public Agentforce prices today, for context (https://www.salesforce.com/agentforce/pricing/, checked 27 Oct 2026): the Agentforce add-on for Sales or Service at $125 a user a month, with unmetered use by employees; Flex Credits at $500 per 100,000; $2 per conversation for customer-facing agents; the Max edition from $550 a user a month with the add-on and 2.75M Flex Credits included. Trade press reports the Help Agent at $2 per resolution (https://www.cxnetwork.com/cx-experience/news/salesforce-launches-pay-per-resolution-agent/amp).

| Option | How it works | Fits when | Risk |
|---|---|---|---|
| Per outcome | per confirmed deal update, or per forecast brief | value is easy to count | revenue swings with how many calls reps have; reps may feel counted |
| Per agent | a fixed price per user a month, like a seat, billed at renewal | buyers want predictable bills; the panel asked for a flat line | harder to tie to value; reps who only review a list feel overpriced (Priya) |
| Usage | Flex Credits per action | usage varies a lot | Elena: "unclear credits already burn me"; bills feel unpredictable |
| Tier | included in the $125 Agentforce for Sales add-on or in Max | simple to sell to customers already on it | gives the value away to those customers and doesn't reach the rest |

**Our choice:** per agent, at **$45 a user a month** for every Sales Cloud user on the team, a fixed line billed annually at renewal. Customers already on the Agentforce for Sales add-on or Max get it included. `[PM, illustrative]` Because the buyer and the sceptic both asked for one flat line with no credit surprises, and $45 sits at the buyer's "getting expensive" mark: high enough to be taken seriously, low enough to sit well under a tool on top.

- **Value-based check:** the price is 6.7% of the labour it saves ($17,280 ÷ $256,680), so the customer clearly wins; for the 32-seat customer it's $17,280 a year, against Gong's median deal of about $55,000 (https://vendr.com/marketplace/gong).
- **Panel price vote:** medians: too cheap $6.50, a bargain $17.50, getting expensive $42.50, too expensive $77.50; the buyer's own line is $45 (`../flows/panel-tests.md`). The panel priced well below the value; we sit at the top of its acceptable range rather than the bottom. *Synthetic vote: hypotheses, not evidence.*
- **Real customers said:** nothing yet; no real interviews in this public example. Ask the budget question in `../flows/script.md`, Part 3.
- **What would change our mind:** real buyers accepting a higher price once a one-team pilot shows managers stop chasing; reps resenting a seat price for a review list (then a lower rep rate and a higher manager rate, as Priya suggested); or too many customers already on the add-on, so little new revenue comes in.
