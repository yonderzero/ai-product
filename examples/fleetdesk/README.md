# Worked example: FleetDesk, fleet maintenance software

> **Fictional example. FleetDesk and everything about it, its customers, documents and numbers are invented to show how the skills work. The competitors and market facts are real and sourced as of 27 Oct 2026.**

This folder shows what a product manager has after running all seven skills, `/ai-product-start`, `/ai-product-vision`, `/ai-product-discovery`, `/ai-product-problem`, `/ai-product-research`, `/ai-product-flows` and `/ai-product-roadmap`, for a typical vertical software product.

FleetDesk is a mid-size, 15-year-old company in a software group. It sells fleet maintenance software to about 800 US trucking and delivery fleets, priced per vehicle per month. Its AI is at level 1 today, with one level 2 feature in beta. The product manager brought seven files, in `documents/`, which are the evidence for many facts, and added two real-customer interview transcripts during the flows step.

- **Start:** builds a profile of the product and four personas from those files.
- **Vision:** maps the real market on six AI levels, finds and ranks the opportunities, imagines FleetDesk at each higher level, and agrees a vision.
- **Discovery:** scores protection, strength, AI opportunity and exposure; one score is overturned. It checks readiness, maps where value flows, chooses the move and sets where to take the product.
- **Problem:** sharpens the problem to start with, grades its evidence, thinks bigger and picks the right problem.
- **Research:** looks at how each type of customer lives the problem and what options they have, defines the ideal customer, builds four synthetic personas, drafts five agentic customer experiences with their economics, and lets the personas pressure-test the problem.
- **Flows:** maps each experience as a flow, makes the two leading ones clickable, tests them in two panel rounds and two real interviews, and takes forward the morning shortlist, then the notes.
- **Roadmap:** turns the flows into prioritised features, works out the ROI and the price ($3 per powered vehicle a month for the shortlist), lays out Now, Next and Later, and defines the build-day slice.

Facts about FleetDesk cite `[documents/<file>]` or are tagged `[PM, illustrative]`. Facts about the market cite the public page they came from. The personas are synthetic: what they say is a hypothesis, not evidence.

## Files

- [`index.html`](index.html): **open this first.** The deck covers every step, from the product and the vision to the flows, this product update, ROI and the roadmap, with links to every file.
- [`product.md`](product.md): the product profile: company, four personas and their problems, workflows, pricing, competitors, data and tech, AI today.
- [`documents/`](documents/): the invented files the product manager brought:
  - two customer interviews: a maintenance manager and a director of fleet operations;
  - a support tickets export;
  - won and lost deal notes;
  - a churn note;
  - the sales one-pager;
  - notes from the AI beta;
  - two transcripts from the flows step, with roles only: a waste hauler's maintenance manager and a beverage distributor's shop supervisor.

From `/ai-product-vision`, in [`vision/`](vision/):

- [`vision/ai-levels.md`](vision/ai-levels.md): the value FleetDesk gives at each level. Level today is 1, System of Record, with Fault Code Assist in beta at level 2.
- [`vision/market-map.md`](vision/market-map.md): 15 real companies placed on the six levels, each with source, status and confidence. Fleetio and ServiceUp are at level 4.
- [`vision/market-map.html`](vision/market-map.html): the same map as a page; open it in a browser.
- [`vision/market-moves.md`](vision/market-moves.md): who is moving into the market across five ways in. Telematics vendors bundling maintenance is the strongest.
- [`vision/opportunities.md`](vision/opportunities.md): the fleet's maintenance work as nine steps, then six opportunities, rated and ranked. First is "From fault code to a ready work order", at 4.60.
- [`vision/vision.md`](vision/vision.md): FleetDesk imagined at levels 2 to 6, a day with its System of Understanding, and the vision: level 4 by the end of 2028.

From `/ai-product-discovery`, in [`discovery/`](discovery/):

- [`discovery/protection.md`](discovery/protection.md): what protects the product, 24 levers in four groups. 2.7 out of 5, Transitional; switching costs are eroding.
- [`discovery/strength.md`](discovery/strength.md): business quality and customer strength. Strength is 3.58, AI opportunity 3.67, and AI urgency is immediate.
- [`discovery/exposure.md`](discovery/exposure.md): 11 risks, 1 safest to 5 most exposed. 3.0 overall, borderline; highest on AI disruption, its timing, and dependence on rivals' data.
- [`discovery/value.md`](discovery/value.md): where value flows today, where it leaks, where it would flow at level 4, who else could capture it, and how to charge.
- [`discovery/discovery.md`](discovery/discovery.md): the one page: where to take the product, the four pillars, the move (Move first), readiness, value flows and the overturned score.

From `/ai-product-problem`, in [`problem/`](problem/):

- [`problem/evidence.md`](problem/evidence.md): the evidence for the problem, graded with the Mom Test.
- [`problem/framings.md`](problem/framings.md): the job, the pressure test with the four forces, the BHAG, the job map, adjacent segments and three sized framings.
- [`problem/problem.md`](problem/problem.md): the right problem: getting every truck that needs work from the first signal back on the road. It also covers the opportunity and what to learn from customers before building anything.

From `/ai-product-research`, in [`research/`](research/):

- [`research/evidence.md`](research/evidence.md): what the seven documents say, grouped by customer type, each row with its file and line.
- [`research/market.md`](research/market.md): the problem in each persona's words, through their eyes, the options fleets have today (from doing nothing to Fleetio, Samsara, Motive, Whip Around, Fullbay and outsourcing) and the segments, with sources.
- [`research/icp.md`](research/icp.md): the ideal customer: a regional carrier or distributor with 150–500 vehicles, its own shop and a telematics feed.
- [`research/personas/`](research/personas/): four synthetic personas, every field sourced: Glen, director of fleet operations (buyer); Rosa, maintenance manager (user); Dwayne, lead technician (sceptic); Tess, owner of an independent repair shop (adjacent segment).
- [`research/experiences.md`](research/experiences.md): how people use the product today, what that time costs a typical customer, five agentic customer experiences, the new economics, and the one to explore first: the morning shortlist.
- [`research/panel.md`](research/panel.md): the personas at work: an interview with Rosa, the three framings scored, and reactions to the experiences. Hypotheses, not evidence.

From `/ai-product-flows`, in [`flows/`](flows/):

- [`flows/flows.md`](flows/flows.md): the five experiences mapped as flows, moment by moment, ranked on value, trust, pay and hours back. The morning shortlist goes forward first, say it, sign it next; parts and the dispatch slot later; overflow not for now.
- [`flows/DESIGN.md`](flows/DESIGN.md): the design direction the mockups follow: a style like IBM Carbon, from getdesign.md, chosen for contrast in a bright shop. The developers build the slice to match it.
- [`flows/mockups/morning-shortlist.html`](flows/mockups/morning-shortlist.html) and [`flows/mockups/say-it-sign-it.html`](flows/mockups/say-it-sign-it.html): clickable mockups of the two flows taken forward. Open them in a browser.
- [`flows/panel-tests.md`](flows/panel-tests.md): two panel rounds, the sceptic first, and the two real interviews, with where they agree and disagree.
- [`flows/script.md`](flows/script.md): the interview kit for real customers.

From `/ai-product-roadmap`, in [`roadmap/`](roadmap/):

- [`roadmap/features.md`](roadmap/features.md): ideas, the features prioritised with the working, this product update (the morning shortlist) and the build-day slice.
- [`roadmap/roi.md`](roadmap/roi.md): what the update is worth to a typical customer and to FleetDesk, the ways to charge, the panel's price vote, the choice of $3 per powered vehicle a month, and one pricing story across the earlier files.
- [`roadmap/roadmap.md`](roadmap/roadmap.md): Now, Next and Later, without dates, toward the vision and the BHAG.

Placements are a snapshot from public sources on 27 Oct 2026. Check the ones you act on.
