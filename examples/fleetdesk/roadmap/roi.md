# FleetDesk · ROI and pricing

> Fictional example. FleetDesk, its documents, prices and the product manager's answers are invented, tagged `[PM, illustrative]`. Assumptions are tagged `[assumed]`. The personas are synthetic: their price vote is a hypothesis, not evidence.

What this product update, the morning shortlist, is worth, to customers and to us, and how we charge for it. Built from `../research/experiences.md` (the double cost and the new economics), `../discovery/value.md`, `features.md` and the product manager's answers on 27 Oct 2026. Every number shows its working; assumptions are labelled.

## For a typical customer

The ideal customer in `../research/icp.md`: about 200 powered vehicles on Pro, one or two shops, a telematics feed. Today's figures are the double cost in `../research/experiences.md`.

| | Today | With this update |
|---|---|---|
| Licence | $31,200 | $31,200 |
| Agents | – | $7,200 |
| People's time using the product | $132,800 | $115,700 |
| **Total a year** | **$164,000** | **$154,100** |

- **They save:** $9,900 a year (6%); their people get about 300 hours back: the lead tech's morning code list drops from 250 hours to about 25, and the manager's review from 125 to about 50.
- **Their return:** every $1 they pay for agents saves them $2.40 of labour ($17,100 ÷ $7,200).
- **Not counted:** road calls avoided. One missed code at Rosa's carrier meant a tow, a rental tractor and a late load (`../research/panel.md`); at the waste hauler, a tow of about $1,400 and two late routes [documents/interview-maintenance-manager-waste-hauler-flows.md]. That's what the buyer pays for ("I'd pay more if it cut downtime", [documents/interview-fleet-ops-director-distribution.md]), but we have no measured rate of road calls avoided yet. The pilot measures it.

**Working.** Labour saved: lead tech 225 h × $52 = $11,700, plus manager 75 h × $72 = $5,400, total $17,100, as in experience 1 of `../research/experiences.md`. People's time with the update: $132,800 − $17,100 = $115,700. Agents: $3 × 200 vehicles × 12 months = $7,200. The 200 vehicles is the ideal customer's typical size `[PM, illustrative]`; hourly costs and hours are measured or labelled in `../research/experiences.md`.

**As the agents grow** (from `../research/experiences.md`, "The new economics"): with the notes added (Next), labour saved rises to $75,300 ($17,100 + $58,200) against $14,400 for agents at $6. With all four in-shop experiences live (Later), the customer saves $82,700 a year (50%), paying $19,200 for agents at $8.

## For us

| | Per customer a year | Across 93 customers who'd buy |
|---|---|---|
| New agent revenue | $7,200 | $669,600 |
| Cost to run | $1,100 | $102,300 |
| Cost to build (once) | $4,090 | $380,000 |
| **Net, first year** | **$2,010** | **$187,300** |
| **Net, each year after** | **$6,100** | **$567,300** |

- **Customers who'd buy:** 93 = 310 customers with a telematics feed (measured, [documents/fault-code-assist-beta-feedback.md]) × 30% who'd buy (assumption) `[assumed]`. The shortlist needs the codes, so the base is the 310, not all 812.
- **Revenue per customer:** $3 × 200 vehicles (assumption: the ideal customer's typical size; the 310's real average isn't known) × 12 = $7,200.
- **Cost to build and run:** $380,000 to build: the agent as a service beside the monolith, the shortlist page, and an owner for AI quality and evaluation, the gap named in `../discovery/discovery.md` `[PM, illustrative]`. $1,100 per customer a year to run: model calls on a few hundred codes a night, plus hosting `[assumed]`.
- **Fits the earlier sizing:** $669,600 sits inside the $524,000–$1,047,000 a year the problem's bigger job was sized at (`../problem/problem.md`). Not counted: revenue kept from the 37 customers with a bundled offer at renewal, $143,000–$286,000 a year (`../problem/framings.md`).

## How we charge

| Option | How it works | Fits when | Risk |
|---|---|---|---|
| Per outcome | per work order the manager approves from the shortlist | value is easy to count | rewards opening work orders, the opposite of what Dwayne wants; revenue swings with the season |
| Per agent | a fixed price per agent, like a seat | buyers want predictable bills | one agent at a 200-vehicle fleet and at a 500-vehicle fleet does very different work |
| Usage | per code read or per shortlist | usage varies a lot | hundreds of codes a night: bills feel unpredictable and punish noisy trucks |
| Tier | the shortlist included in Pro | simple to sell; answers "What does your AI do?" | gives away the first agent before we know what it's worth; the vision proposed testing it (`../vision/vision.md`) |
| **Per vehicle add-on** | a monthly price per powered vehicle, on top of the plan | customers already buy per vehicle [documents/product-one-pager.md]; scales with fleet size | a price rise last year cost 12 customers [documents/churn-note-2026.md] |

**Our choice:** a per-vehicle add-on, at **$3 per powered vehicle a month**, trailers not counted, on Pro, where the telematics feed lives. After a free pilot on the customer's own trucks. `[PM, illustrative]`

Because:

- customers already buy per vehicle, and both the manager and the buyer think in trucks; Rosa: "Charge per tractor, not per trailer";
- $3 is a bargain for the user and the buyer personas, and well under where they'd find it expensive ($5–$7);
- a real maintenance manager said "a few dollars a truck" is in her own budget; "another Pro plan on top" needs her general manager [documents/interview-maintenance-manager-waste-hauler-flows.md];
- the panel asked to prove it on their own trucks before the price (`../research/panel.md`), so the pilot is free.

- **Value-based check:** the price is 42% of the labour it saves ($7,200 of $17,100), before a single road call avoided. That's a larger share than the rule in `../research/experiences.md` (agents at about a fifth of the labour saved), because the shortlist's value is mostly trust and road calls, not hours. It falls back to about a fifth as the notes join ($14,400 of $75,300, 19%).
- **Panel price vote** (Van Westendorp, $ per powered vehicle a month, for the shortlist only). *Synthetic vote: hypotheses, not evidence.*

  | Persona | Too cheap to trust | A bargain | Getting expensive | Too expensive |
  |---|---|---|---|---|
  | Dwayne (sceptic) | $0.50 | $2 | $5 | $9 |
  | Glen (buyer) | $1 | $3 | $7 | $12 |
  | Rosa (user) | $1 | $3 | $7 | $14 |

  An acceptable range of about $2 to $7, with $3 at the bargain point for two of three. Dwayne: "Not my money. This is a guess at what Rosa could defend." Glen: "It has to show fewer trucks down to be worth more than $3." Tess voted per overflow job, not per vehicle ($3 / $15 / $40 / $90): useful if overflow comes back, not for this update.
- **Real customers said:** "If it's a few dollars a truck, it's my budget. If it's another Pro plan on top, it's the general manager, and he'll ask what it replaces." (maintenance manager, waste hauler). The shop supervisor: "Not my call. My manager would ask what it replaces." No buyer has been asked yet.
- **What would change our mind:** a director of fleet operations who won't pay without a downtime number (then the buyer's weekly card moves into Now); pilot fleets approving few drafts unchanged (then it's not worth $3 yet); many Core customers with a feed outside FleetDesk, like Glen's fleet, who'd need Pro first (then offer the add-on on Core).

## One pricing story

Earlier files floated different numbers. Here is how they fit, and the one story we're keeping:

- **$3 per powered vehicle a month for the morning shortlist, now.** It's the add-on the vision proposed to test (`../vision/vision.md`), and about 23% of Pro's $13, in line with the 25% uplift in the problem's sizing (`../problem/problem.md`). We chose the add-on over "included in Pro" because buyers will pay "a few dollars a truck" and we need to learn what the agent is worth.
- **$6 when the notes join, in Next.** About a fifth of the labour the two flows save.
- **$8 for the full shop agent, Later,** when the four in-shop experiences are live. That's the price in the new economics of `../research/experiences.md`; it was never the price for the shortlist alone, and no persona would pay it before a pilot.
- **A share of warranty money recovered, later still,** as in `../discovery/value.md`, once notes make warranty claims possible.
