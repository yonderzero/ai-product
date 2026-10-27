# AI level map · US fleet maintenance software

> Fictional example: FleetDesk is invented. Every other company here is real, and placed from public sources retrieved on 27 Oct 2026.

FleetDesk owns preventive maintenance, work orders, parts and DOT records for US trucking and delivery fleets of 50 to 500 vehicles that run their own shops (`../product.md`). Snapshot from public sources on 27 Oct 2026. Most metrics below are the vendors' own claims.

## The market on the curve

| Level | Incumbents | AI-native challengers | Horizontal players |
|---|---|---|---|
| 6 System of Understanding | | | |
| 5 AI Domain Intelligence | | Uptake (low confidence) | |
| 4 AI Delegated | Fleetio | ServiceUp | |
| 3 AI Directed | RTA Fleet, Collective Data, Trimble TMT (low confidence) | | Samsara, Motive, Geotab, MaintainX |
| 2 AI Assisted | Fullbay, Whip Around | | |
| 1 System of Record | **FleetDesk (us)**, Cetaris, Chevin FleetWave, Decisiv | | |

**Us:** level 1, because nothing AI is shipped and used. Fault Code Assist, in beta with 46 customers, would be level 2 once shipped; under the placement rules a beta counts as half a level at most, so we don't round up (`ai-levels.md`, `../documents/fault-code-assist-beta-feedback.md`). There is no public evidence for FleetDesk to check this against: it's the product manager's own reading, with the same rules applied. `[PM, illustrative]`

## Company by company

| Company | Group | Level | Its highest AI feature | Shipped / beta / announced | Confidence | Source | Heading towards |
|---|---|---|---|---|---|---|---|
| Fleetio | Incumbent | 4 | AI Service Advisor: prioritises issues, drafts work orders and approves low-risk repairs within limits the fleet sets; bigger repairs go to a person. The vendor reports over 2,000 issues a month resolved automatically and a named customer, Ramos Oil, saving about 1.5 hours a day | Shipped (generally available 25 Sep 2026, after a beta from March) | High | https://itbrief.co.uk/story/fleetio-opens-ai-service-advisor-after-maintenance-beta | Higher auto-approval limits: one customer raised its limit from $250 to $2,000 (search result: https://www.fleetio.com/resources/press/first-half-of-2026) |
| ServiceUp | AI-native challenger | 4 | Agentic repair platform: intake, shop routing, estimate, approval and fraud agents; "Autopilot" runs outsourced repairs end to end against the fleet's policy | Shipped (launched 21 Jul 2026) | Medium | https://www.serviceup.com/blog/serviceup-launches-the-agentic-repair-platform-for-modern-fleets | Full autonomy for repairs done outside the fleet's shop; sits next to the fleet's maintenance system |
| Uptake | AI-native challenger | 5 | Predictive failure models built on data from many fleets, each prediction tied to severity and cost; completed repairs feed back into the models | Shipped (long-standing); Bosch announced it is acquiring Uptake in March 2026 | Low: customer results are old and undated; a stricter reading would put it at 2 | https://www.fleetmaintenance.com/shop-operations/ai-and-software/article/55365401/robert-bosch-llc-bosch-acquires-uptake-to-strengthen-vehicle-health-predictive-maintenance-tools | Combined with Bosch's connectivity and fleet tools for fault-to-repair vehicle health (announced) |
| Samsara | Horizontal | 3 | Agent Studio: no-code agents with maintenance templates, such as a daily maintenance and DVIR digest. June 2026 also brought a warranty claim agent, Shop Planner and automatic purchase orders | Agent Studio shipped (generally available 13 Oct 2026, per a search result: https://futurumgroup.com/?p=96840); the status of each maintenance feature isn't stated | Medium | https://www.samsara.com/company/news/press-releases/samsara-launches-new-agentic-capabilities-to-automate-tedious-operational-tasks · https://www.fleetmaintenance.com/shop-operations/ai-and-software/article/55386202/samsara-samsara-unleashes-agentic-ai-to-free-maintenance-teams-from-monotony | Level 4 in maintenance: purchase orders and warranty claims done by agents |
| Motive | Horizontal | 3 | Motive Maintenance: AI reads repair invoices into records, explains fault codes with a severity rank, and turns defects and fault codes into work orders | Shipped 18 Aug 2026 | Medium | https://gomotive.com/motive-launches-ai-powered-maintenance-to-help-operations-teams-prevent-breakdowns-increase-uptime-and-lower-repair-costs/ · https://www.freightwaves.com/news/fleet-repair-costs-ai-maintenance | Cost per mile and total cost of ownership, joining maintenance, telematics and fuel-card spend |
| Geotab | Horizontal | 3 | Geotab Ace: an assistant that answers questions over fleet data, including maintenance trends, included in MyGeotab | Shipped; voice agent and predictive maintenance announced (Feb 2026) | Medium | https://fleetinsights.emkay.com/insights/geotab-connect-2026-ai-safety-and-the-future-of-fleet-management | Predictive maintenance (announced) |
| MaintainX | Horizontal | 3 | CoPilot: answers from OEM manuals and work-order history, writes procedures; reporting AI | Shipped | Medium; fleet is a secondary market for it | https://www.nasdaq.com/articles/ai-effect-maintainx-sees-valuation-jump-25b-150m-series-d-raise (search result) | Agents for frontline teams (seen in a job posting only) |
| RTA Fleet | Incumbent | 3 | Ron360: an assistant that answers questions on maintenance, cost and compliance data with charts and saves them to dashboards; it reports but doesn't act | Shipped Jun 2026, in all plans | High | https://worktruckonline.com/news/rta-introduces-ron360-ai-assistant-for-fleet360-users-at-government-fleet-expo-2026 | Spotting trends and recommending actions (announced) |
| Collective Data | Incumbent | 3 | Document Intelligence: turns uploaded repair invoices into work orders with VMRS codes; "Ask Anything" over fleet data | Shipped (launched Apr 2026) | Medium | https://www.fleetmaintenance.com/shop-operations/data-and-telematics/article/55370589/collective-data-collective-data-ai-assistant | More document types (announced) |
| Trimble TMT Fleet Maintenance | Incumbent | 3 | AI invoice scanning in release 2026.1 | Shipped, per a release webinar only | Low | https://transportation.trimble.com/en/asset-fleet-maintenance/videos/tmt-2026-latest-in-asset-maintenance | Not found |
| Fullbay | Incumbent | 2 | Fullbay AI turns technicians' typed or dictated notes into clean repair records | Shipped May 2025; "AI-native" Fullbay Next rolling out from Aug 2026 | Medium | https://www.worktruckonline.com/news/fullbay-debuts-ai-tool-and-key-platform-upgrades | Predictive maintenance and parts forecasting from 5,000+ shops, after buying Pitstop in March 2026 (announced): https://www.motor.com/2026/03/fullbay-acquires-pitstop-to-advance-ai-predictive-maintenance/ |
| Whip Around | Incumbent | 2 | AI Inspections Pro: checks inspection photos and flags defects the driver missed; paid add-on | Shipped | Medium | https://whiparound.com/inspect | Not found |
| Cetaris | Incumbent | 1 | No AI feature described | n/a | Low | https://cetaris.com/events-blog/5-maintenance-management-takeaways-from-cetaris-summit-2025 (search result) | Clean data first, AI later |
| Chevin FleetWave | Incumbent | 1 | None found; 2026 launches are a dashboard and apps | n/a | Medium | https://transportoperator.co.uk/2026/03/09/cv-show-2026-chevin-fleetwave-dashboard-preview/ (search result) | Dashboards and configuration |
| Decisiv | Incumbent | 1 | None found; service cases open from fault codes by fixed rules | n/a | Low; sources from 2022–23 | https://www.forconstructionpros.com/construction-technology/product/21002995/decisiv-service-relationship-management-srm-system (search result) | Not found |

## Not placed

| Company | Why |
|---|---|
| Pitstop | Acquired by Fullbay in March 2026; its predictive maintenance is now part of Fullbay's plans (https://www.motor.com/2026/03/fullbay-acquires-pitstop-to-advance-ai-predictive-maintenance/) |
| Platform Science | Bought Trimble's telematics units, not TMT; its maintenance AI comes through partners |
| AssetWorks | No AI announcement found |
| Fleetpal | Named in `market-moves.md`: free inspection app with AI repair coding on top; the AI coding wasn't checked closely enough to place it |
| Penske Catalyst AI | Named in `market-moves.md`: a leasing company's fleet intelligence tool, sold as part of leasing, not maintenance software |
| Microsoft Copilot, ChatGPT and other general assistants | No evidence they reach fleet maintenance work directly yet; see `market-moves.md` |
| Newly funded AI-native fleet maintenance startups | Searches found no verifiable 2024–2026 funding round in this niche |

## Openings

- **Empty or thin levels:** nobody is at level 6, and level 5 has one low-confidence player that sells mostly to large fleets and OEMs. Level 4 has two, and neither runs the in-house shop end to end: Fleetio approves repairs, ServiceUp coordinates outside repairs. Turning a fault code into a planned, parted and scheduled job in the fleet's own shop is open.
- **Moving up fastest:** Fleetio, from a beta in March to delegated approvals in September 2026; Samsara and Motive, which shipped maintenance AI in June and August 2026 and sell it with telematics.
- **Where we could lead:** the mid-size fleet with its own shops and parts rooms, where FleetDesk already wins half its deals (`../documents/lost-deals-h1-2026.md`). Fifteen years of repair outcomes could support level 5 benchmarks and predictions for that segment, if contracts allow it.

*Placements are a snapshot from public sources. Check the ones you act on.*
