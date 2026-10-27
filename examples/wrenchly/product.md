# Wrenchly

> Fictional example. Wrenchly, its company, customers, documents and numbers are invented. Facts about Wrenchly cite the invented files in `documents/` or are tagged `[PM, illustrative]`. Facts about the market, competitors and regulation are real and cite public sources retrieved on 27 Oct 2026.

- company: Wrenchly Software, Columbus, Ohio. Founded 2011; part of Halvard Software Group, a group of vertical software companies, since 2019. About 120 employees. `[PM, illustrative]`
- industry: transportation software. Niche: fleet maintenance software for US trucking and delivery fleets that run their own shops, mostly 50 to 500 vehicles. [documents/product-one-pager.md]
- links: website, pricing and help centre (fictional, not linked). Sales one-pager: [documents/product-one-pager.md]
- team: a product manager for the core product, working with an engineering lead, a designer and the head of customer success `[PM, illustrative]`

## What it does

Wrenchly runs the maintenance side of a fleet. It plans preventive maintenance (PM) by miles, engine hours or days, with meter readings synced from telematics. It takes a defect from a driver's inspection or a fault code to a closed work order, with labor, parts, VMRS repair codes and the technician's sign-off. It manages parts across shops, purchase orders and outside vendor repairs, and keeps the inspection and repair records US fleets must hold for DOT audits. [documents/product-one-pager.md]

About 800 fleets manage more than 115,000 trucks, tractors, vans and trailers with it. [documents/product-one-pager.md] [documents/churn-note-2026.md]

## Customers

- customer types: regional and LTL carriers, foodservice and beverage distributors, waste haulers, utilities' private fleets and last-mile delivery fleets, mostly with 50 to 500 vehicles and at least one in-house shop. [documents/product-one-pager.md]
- 812 customers at the end of September 2026; the average new customer runs about 120 vehicles. [documents/churn-note-2026.md] [documents/lost-deals-h1-2026.md]

### Fleet maintenance manager

- who they are: runs one or more shops at a fleet of 100 to 500 vehicles, with 5 to 20 technicians and a parts manager. The main daily user; strongly influences the purchase and the renewal. [documents/interview-maintenance-manager-regional-carrier.md]
- what they're trying to get done: keep trucks safe and on the road. Measured on road calls (breakdowns on the road) per million miles, PM compliance, out-of-service rate at roadside inspections, and cost per mile. [documents/interview-maintenance-manager-regional-carrier.md]
- the problems this product solves for them: PM schedules that follow real miles and engine hours; every work order and inspection in one place; DOT audit records printed in minutes, not a week. [documents/interview-maintenance-manager-regional-carrier.md]
- how they handled it before: a wall calendar, paper work orders and binders. "Before Wrenchly we did PMs off a wall calendar and missed a third of them." [documents/interview-maintenance-manager-regional-carrier.md]
- what still frustrates them: hundreds of fault codes a day, most of them noise, read one by one; technicians' notes too thin for warranty claims; PM slots missed when dispatch keeps a truck on the road, with nothing rescheduling it. [documents/interview-maintenance-manager-regional-carrier.md] [documents/support-tickets-q3-2026.csv]

### Shop technician

- who they are: a diesel technician in the fleet's shop, on a tablet or shared desktop. A user, not a buyer. `[PM, illustrative]`
- what they're trying to get done: fix the truck right the first time and move to the next job. Measured on hours billed to work orders and comebacks (repeat repairs). `[PM, illustrative]`
- the problems this product solves for them: the job, the vehicle's history and the parts in one work order. [documents/product-one-pager.md]
- how they handled it before: paper work orders and asking the parts counter. `[PM, illustrative]`
- what still frustrates them: typing. Techs spend an estimated 20 to 30 minutes per job on notes, time entry and finding part numbers, and often close with "replaced" or "fixed". "Too many clicks to close a work order" came up in churn interviews. [documents/interview-maintenance-manager-regional-carrier.md] [documents/churn-note-2026.md] [documents/support-tickets-q3-2026.csv]

### Parts manager

- who they are: runs the parts room for one or more shops: stock, receiving, purchase orders, vendors and warranty returns. A user. [documents/interview-maintenance-manager-regional-carrier.md]
- what they're trying to get done: the right part on the shelf before the truck comes in, without tying up cash in stock. `[PM, illustrative]`
- the problems this product solves for them: inventory across shops, reorder points, purchase orders and vendor price history. Customers using parts in two or more shops churn least (3%). [documents/product-one-pager.md] [documents/churn-note-2026.md]
- how they handled it before: spreadsheets and the parts vendor's website. `[PM, illustrative]`
- what still frustrates them: counts that don't match the shelf after receiving; trucks waiting for parts the PM schedule could have predicted; no time to check warranty on a failed part. [documents/support-tickets-q3-2026.csv] [documents/interview-fleet-ops-director-distribution.md] [documents/fault-code-assist-beta-feedback.md]

### Director of fleet operations

- who they are: owns the fleet and the maintenance budget at a fleet of 100 to 500 vehicles; reports to the CFO or COO. The buyer, who signs the contract. [documents/interview-fleet-ops-director-distribution.md]
- what they're trying to get done: trucks ready at 5 am, on-time delivery, maintenance cost per mile under control, and clean DOT audits. [documents/interview-fleet-ops-director-distribution.md]
- the problems this product solves for them: one record of every repair, including outside vendors; driver inspections that reach the shop. [documents/interview-fleet-ops-director-distribution.md]
- how they handled it before: the shop's paper files and the accounting system. `[PM, illustrative]`
- what still frustrates them: rebuilding the cost-per-mile report in Excel every month ("two days a month, every month"); no idea which outside vendor overcharges; too many logins. Telematics vendors offer maintenance in the same bill. [documents/interview-fleet-ops-director-distribution.md] [documents/lost-deals-h1-2026.md]

Drivers also use the Wrenchly Driver app for pre- and post-trip inspections, but don't choose the product. [documents/product-one-pager.md]

## Main workflows

- Driver inspection to defect: pre- and post-trip inspections in the Driver app; defects go to the shop queue. [documents/product-one-pager.md]
- Fault code to work order: telematics codes arrive in Wrenchly; a person reads each one and decides whether to open a work order. The lead tech at one customer spends "the first hour of his day as a fault-code clerk". [documents/interview-maintenance-manager-regional-carrier.md]
- PM planning: schedules by miles, hours or days; the shop plans the day on a whiteboard, then types it in. [documents/interview-maintenance-manager-regional-carrier.md]
- Work order to close: labor, parts, VMRS codes, notes and sign-off. Where technicians spend the most time typing. [documents/support-tickets-q3-2026.csv]
- Parts and purchasing, outside vendor invoices, and DOT records and reports. [documents/product-one-pager.md]

## What customers love / complain about

- love: PM schedules that follow real miles; DOT audit-ready records; multi-shop parts inventory deeper than simpler tools; implementation specialists who ran fleet shops. [documents/interview-maintenance-manager-regional-carrier.md] [documents/lost-deals-h1-2026.md]
- complain: PM schedules wrong when meter readings stop syncing (18% of support tickets in Q3 2026); parts counts (15%); closing work orders on the tablet (13%); fault-code overload (12%); a slow mobile app; reports the CFO wants that don't exist. [documents/support-tickets-q3-2026.csv] [documents/churn-note-2026.md] [documents/interview-fleet-ops-director-distribution.md]

## Pricing and market

- Core $8 per vehicle per month; Pro $13; trailers and equipment $3 per unit. Annual contracts; implementation from $2,500. [documents/product-one-pager.md]
- Core went from $7.50 to $8 in 2026; 12 customers left over price. [documents/churn-note-2026.md]
- About $10.5M in annual recurring revenue. Gross revenue retention 90%, net 101%, logo churn 10.8%; churn is 4% above 150 vehicles. `[PM, illustrative]` [documents/churn-note-2026.md]
- Win rate 43% in the first half of 2026; 51% for fleets of 150–500 vehicles, 34% under 75. [documents/lost-deals-h1-2026.md]
- The market: see `vision/market-map.md` and `discovery/exposure.md` for size, growth and rules.

## Competitors and alternatives

- Lost deals in the first half of 2026: Fleetio (29), Samsara with maintenance bundled into telematics (21), Whip Around (9), Motive (8), spreadsheets or no decision (11). [documents/lost-deals-h1-2026.md]
- Churn to telematics bundles: 31 of 88 customers who left. [documents/churn-note-2026.md]
- The full market, with AI-native challengers and horizontal players: `vision/market-map.md` and `vision/market-moves.md`.

## Data and tech

- Holds 15 years of work orders, repairs, parts, PM history, inspections and outside vendor invoices for each fleet: about 2 million work orders a year across customers. `[PM, illustrative]`
- About 310 customers stream telematics fault codes and meter readings from Samsara, Motive or Geotab. [documents/fault-code-assist-beta-feedback.md]
- Built on a C# and .NET Framework monolith with SQL Server, moved to Azure in 2020; newer services on .NET 8; a React Native app for technicians and drivers; a public REST API since 2023. `[PM, illustrative]`
- Integrates with QuickBooks and Sage Intacct, and imports fuel card files. [documents/product-one-pager.md]
- Contracts since 2021 allow de-identified, aggregated data for product improvement and benchmarks; about 70% of customers are on them. Whether that covers training AI models isn't confirmed. [documents/fault-code-assist-beta-feedback.md]

## AI today

- No AI in the shipped product. Fault Code Assist, in beta since May 2026 with 46 customers, explains fault codes in plain English, rates urgency and suggests a repair code. 61% of rated answers got a thumbs-up. No charge in the beta. [documents/fault-code-assist-beta-feedback.md]
- Prospects ask "What does your AI do?" in every second demo. [documents/lost-deals-h1-2026.md]
- **Level today: 1, System of Record (level 2 in beta). Target: 4, AI Delegated, by the end of 2028.** See `vision/ai-levels.md` and `vision/vision.md`.
- **Our move: Move first** (AI opportunity 3.67, risk 3.0, borderline). Direction: protect the shop's work for fleets of 150–500 vehicles; turn fault codes, invoices and notes into ready work; start with how managers triage fault codes today. See `discovery/discovery.md`.

## The idea we have in mind

Our customers drown in fault codes and paperwork. We want Wrenchly to turn a fault code into a ready work order, with the parts pulled and the slot booked, so the maintenance manager approves instead of types. `[PM, illustrative]`

- **The right problem:** getting every truck that needs work from the first signal back on the road, starting where managers read fault codes by hand. BHAG: by 2031, every truck ready when dispatch needs it, road calls halved, and no one reads a fault code by hand. See `problem/problem.md`. `[PM, illustrative]`

## Still unknown

- How accurate Fault Code Assist's suggestions are against what technicians actually found. [documents/fault-code-assist-beta-feedback.md]
- Whether our contracts let us train models on repair outcomes across customers.
- How much warranty money customers miss: one customer guesses they recover a third. [documents/interview-maintenance-manager-regional-carrier.md]
- How many customers would pay for AI as an add-on, and at what price.
