# Product Gap Analysis — CELCAT

**Vertical:** Higher & Further Education (Timetabling / Academic Scheduling Software) | **Product:** Celcat AI / Celcat Timetabler (flagship platform; Pay Claim and Celcat Now extensions scoped out) | **Generated:** 2026-07-27

## Top 5 Product Opportunities

### 1. The compliance and engagement layer UK sponsors now need is being built on top of Celcat's own data — by a third party, not by Celcat
**Category:** AI gap (competitor AI shipping) | **Confidence:** Strong

Celcat's Attendance Monitoring module states it supports "automated compliance reporting... for UKVI and other regulatory requirements," but that claim is self-reported marketing copy, and by its own description it stops at attendance capture, audit trails, and generic "historical analytics" for at-risk students — it does not describe case management or multi-stage intervention workflows. Since April 2026, the Home Office has raised the bar for UK student-visa sponsors: a simple attendance register is no longer sufficient evidence of "substantive engagement" — sponsors must now show academic participation, welfare touchpoints, and progression milestones, with a full audit trail. SEAtS Software (SEAtS ONE) is built specifically to close that exact gap, and it does so by consuming Celcat's own output: SEAtS documentation states it "plugs directly into... CELCAT timetabling solution with no parallel data pipeline," pulling Celcat's timetable and attendance feed into its own AI risk-flagging, case-management, and one-click UKVI reporting layer. SEAtS goes further and markets its own AI "Schedule" module as a direct replacement, stating it "replaces manual processes in tools like Scientia and CELCAT." This is not a hypothetical future risk — it is a live, named, shipped competitive product sitting on top of Celcat's data today.

**Pitch angle:** Every UK institution running Celcat now has a regulatory reason to bring in a third party that ingests Celcat's own data and is actively marketing itself as Celcat's replacement — the retention risk compounds every intake cycle SEAtS is the one producing the compliance evidence, not Celcat.

**Evidence:**
- [SEAtS ONE — UKVI Visa Compliance](https://seatsone.ai/higher-education/home-office-ukvi-visa-compliance/) — "From April 2026, the Home Office requires sponsors to evidence substantive student engagement... a simple class register is no longer sufficient."
- SEAtS integration documentation — "SEAtS plugs directly into SITS Student Management System and CELCAT timetabling solution with no parallel data pipeline."
- [SEAtS ONE — Academic Scheduling & Smart Space Utilisation](https://seatsone.ai/academic-scheduling-and-smart-space-utilization/) — SEAtS's Schedule module "replaces manual processes in tools like Scientia and CELCAT."
- [Celcat — Attendance Monitoring](https://celcat.com/timetabler/extensions/attendance-monitoring/) — self-reported: "Automated compliance reporting supports UKVI and other regulatory requirements," no mention of case management or intervention workflows.
- SEAtS company data (Getlatka/Crunchbase) — ~$5.5M revenue, ~50 employees, no disclosed institutional funding round, but documented adoption at 100+ institutions and inclusion in three Gartner Market Guides (Student Success, Timetabling, Smart Campus), with a named case study at Aston University.

> **STRUCTURAL WEDGE ALERT — Urgency: 6 months**
>
> SEAtS Software (SEAtS ONE platform) is the tool doing this. It has no disclosed VC funding but shows documented adoption at scale — 100+ institutions, three Gartner Market Guide listings, a named Aston University case study, and ~$5.5M revenue. SEAtS's own integration documentation confirms it consumes Celcat's structured timetable and attendance output directly ("no parallel data pipeline") and builds its AI engagement-scoring, early-alert, and UKVI case-management/reporting layer on top of that feed. Build window estimated at **6 months** — SEAtS has already shipped a native AI scheduling module and explicitly markets it, by name, as a replacement for CELCAT, so this isn't a future threat still being built; it's already in market and already naming the target.

---

### 2. Celcat's space reporting is retrospective; three-plus competitors have already shipped live occupancy analytics
**Category:** Parity | **Confidence:** Strong

Celcat's Reporting feature — confirmed directly from its own product page — generates "predictive modeling and historical analysis," "resource allocation recommendations," and utilisation dashboards, but all of it is derived from *scheduled/booked* data, not physical occupancy. There is no mention anywhere in Celcat's own materials of IoT, Wi-Fi-based, or sensor-driven live occupancy tracking. Meanwhile, at least four named competitors in the timetabling/campus-operations space have shipped exactly that: SEAtS ONE's SmartSpace module builds AI schedules "informed by live SmartSpace occupancy data," Ad Astra markets AI-driven space-utilization optimization, Accruent EMS offers AI-powered mobile booking with real occupancy detection, and Siemens/Occuspace-class vendors use Wi-Fi/sensor data to report up to 40% "ghost booking" space recovery. The gap is structural: Celcat can tell an institution what was *booked*; it can't tell them what was actually *used*.

**Pitch angle:** Every one of Celcat's institutional customers is sitting on a room-utilisation story that's one sensor integration away from being told by someone else — and that someone else is already selling "40% space recovery" as a headline number competitors don't have to invent.

**Evidence:**
- [Celcat — Reporting](https://celcat.com/timetabler/features/reporting/) — utilisation dashboards are built from "historical timetabling and booking records," not live occupancy.
- [SEAtS ONE — SmartSpace](https://seatsone.ai/seats-one-smartspace-smart-campus-space-utilization/) — AI schedule building "informed by live SmartSpace occupancy data."
- [Ad Astra](https://www.aais.com/) — AI-driven space-utilization optimization marketed as a core differentiator.
- [Accruent EMS — Space Utilization Optimization](https://www.accruent.com/products/ems/analytics-space-utilization-optimization-software) — AI-powered mobile booking and live space analytics.
- Siemens / Occuspace reporting on Wi-Fi/sensor-based occupancy tracking and up to 40% space recovery from eliminating "ghost bookings."

---

### 3. Curriculum and catalog approval happens entirely outside Celcat, in a market where a well-funded competitor has made that the whole platform
**Category:** Gap | **Confidence:** Moderate

Celcat's own baseline — website, docs, and integrations page — covers timetabling, room booking, attendance, exam scheduling, and reporting, but nothing upstream of that: there is no module for curriculum proposal workflows, course catalog authoring/publishing, or program-approval tracking. That's the workflow that logically precedes timetabling (you can't schedule a course that hasn't been approved and cataloged), and it's exactly where Coursedog — a well-funded academic-operations platform ($113M raised across five rounds, including a $90M JMI Equity growth investment) — has built its business, explicitly positioning itself as more than "just a catalog" and integrating curriculum, catalog, and scheduling into one governed system. Coursedog customers describe cutting curriculum-approval time from a multi-year paper process down to 6–9 months. Celcat customers doing that work today are doing it in separate systems (or paper/committee workflows) with no data connection back into the timetable until the course is already approved.

**Pitch angle:** The workflow immediately upstream of Celcat's core product is being consolidated into a single funded platform by a direct competitor — institutions currently stitch curriculum approval and timetabling together by hand, and that stitching is Coursedog's entire pitch.

**Evidence:**
- [Coursedog — Curriculum & Catalog Management](https://www.coursedog.com/products/curriculum-catalog-management) — positions curriculum/catalog management as integrated with scheduling, not a bolt-on.
- [Coursedog raises $90M from JMI Equity](https://www.businesswire.com/news/home/20230329005403/en/Coursedog-Receives-$90-Million-Strategic-Growth-Investment-from-JMI-Equity-to-Accelerate-Product-Development-and-Customer-Success) — $113M total raised, signaling investor conviction in the combined curriculum + scheduling thesis.
- Celcat's own integrations/migration page — lists SIS, HR, space-management, and calendar integrations, with no curriculum/catalog-management module or integration named.

*Flag: single named competitor cited for this signal — treat as directional rather than confirmed market consensus without further validation.*

---

### 4. Customers report the product doesn't catch over-capacity bookings in real time
**Category:** Friction | **Confidence:** Weak

Celcat has almost no public review footprint (one specific review found across Capterra/G2/Trustpilot combined — see Evidence Quality note below), so this rests on a single but specific data point: a verified Capterra reviewer (ICT Manager, Education Management, October 2022) praised Celcat's ease of setup but explicitly flagged "insufficient automation and validation checks" and the absence of "real-time alerts when class enrollment exceeds venue capacity," naming "realtime checks and balances" as a capability they wanted and found lacking relative to alternatives they'd considered.

**Pitch angle:** The recurring complaint is narrow and concrete — real-time overflow/capacity alerting — which makes it an easy, bounded feature to prototype and pitch even though it currently rests on one data point.

**Evidence:**
- CELCAT Timetabler review (Capterra, Juanita F., ICT Manager, Education Management, Oct 2022) — "Lacks real-time alerts when class enrollment exceeds venue capacity limits... insufficient automation and validation checks."

*Flag: single source — needs validation before use in a pitch without further corroboration.*

---

### 5. Individual exam accommodations (extra time, separate rooms) aren't in Celcat's Exam Scheduling module
**Category:** Gap | **Confidence:** Weak

Celcat's Exam Scheduling extension page describes bulk optimisation only — "over 70 constraint types" for room/invigilator allocation — with no mention of individual student accessibility accommodations (extended time, rest breaks, separate distraction-reduced rooms). Cross-referencing how UK universities (Reading, Goldsmiths, Dundee, Birmingham, Nottingham, Edinburgh) actually describe this process shows it running through separate disability-support-service workflows layered on top of, not inside, the timetabling/exam system — adjustments like limiting exams per day or assigning quiet rooms are coordinated by disability teams and communicated back to timetabling manually. This is inferred from the absence of the capability plus general sector practice, not a named complaint about Celcat specifically, so it's held to Weak pending validation.

**Pitch angle:** Exam accommodation coordination is a workflow every UK/EU institution running Celcat already has to do by hand, right next to the exam-scheduling module that doesn't touch it — a natural, low-controversy feature to validate directly with a disability-services office.

**Evidence:**
- [Celcat — Exam Scheduling](https://celcat.com/timetabler/extensions/exam-scheduling/) — describes only bulk room/invigilator optimisation across "70+ constraint types"; no accommodation-specific capability mentioned.
- University disability-service pages (Reading, Goldsmiths, Dundee, Birmingham, Nottingham, Edinburgh) describing reasonable-adjustment coordination (extra time, quiet rooms, exams-per-day limits) as a distinct, manually-coordinated process.

*Flags: inference_heavy, needs_validation — no direct complaint or workaround thread naming Celcat found; this is a structural absence inferred from the feature page plus sector practice.*

## Flagged for Review

**Whether Celcat's own AI claims are shipped or still marketing.** An initial signal — SEAtS positioning itself against "legacy" timetabling tools — suggested Celcat might lack any AI-driven optimisation at all. That doesn't hold up: Celcat's own site describes a shipped "Celcat AI" system (graph-database-backed "Cohort of Timetabling Agents," parallel scenario modeling, continuous optimisation), so a blanket "no AI" gap is not confirmed and isn't shortlisted. What remains genuinely uncertain: every description of Celcat AI's mechanics — the agentic cohort, the graph database, the "five superpowers" — comes exclusively from Celcat's own marketing pages (`marketing_only_source`), published across late 2025–2026. No independent case study, customer reference, or third-party benchmark of the system in production was found in this research pass. Worth pressing on directly in any pitch or diligence conversation rather than taking at face value — the gap may be real if the capability turns out to be more roadmap than shipped product.

## All Candidates

| Rank | Idea | Category | Confidence | Gap Confirmed |
|---|---|---|---|---|
| 1 | Third party (SEAtS) ingests Celcat's data to deliver the AI compliance/engagement layer UK sponsors now require | ai_gap | Strong | Yes |
| 2 | No live/sensor-based occupancy analytics vs. 4 competitors shipping it | parity | Strong | Yes |
| 3 | No curriculum/catalog-approval workflow upstream of timetabling | gap | Moderate | Yes |
| 4 | No real-time over-capacity/enrollment-vs-venue alerting | friction | Weak | Yes |
| 5 | No individual exam-accommodation automation in Exam Scheduling | gap | Weak | Yes |
| 6 | No native no-code integration marketplace (Zapier/Make) alongside the named-system integration list | gap | Weak | Yes |
| 7 | Home Office "substantive engagement" mandate creates a UKVI compliance gap (overlapped by candidate 1) | regulatory | Moderate (pre-merge) | Yes |

## Evidence Quality

| Rank | Idea | Confidence | Evidence Basis | Flags |
|---|---|---|---|---|
| 1 | SEAtS structural wedge / UKVI compliance gap | Strong | 2 distinct research angles (competitive intelligence + regulatory), 4+ distinct URLs, independent confirmation | overlap upgrade applied |
| 2 | Live occupancy analytics parity gap | Strong | 4+ independent named competitors within one angle (SEAtS, Ad Astra, Accruent, Siemens/Occuspace) | — |
| 3 | Curriculum/catalog adjacency gap | Moderate | Single named competitor (Coursedog), well-documented funding + product scope | single_source |
| 4 | Over-capacity real-time alert gap | Weak | Single Capterra reviewer; Celcat has near-zero public review footprint | single_source, low_evidence, needs_validation |
| 5 | Exam accommodation automation gap | Weak | Absence confirmed on product page; sector-practice inference, no named Celcat complaint | inference_heavy, needs_validation |
| 6 | No-code integration marketplace gap | Weak | Absence of Zapier/Make from Celcat's own 20+-system integration list | inference_heavy |
| 7 | UKVI regulatory mandate gap | Moderate (pre-merge) | gov.uk guidance + SEAtS framing; merged into candidate 1 | overlapped_by c_001 |

## Run Statistics

- Candidates generated: 7 (pre-consolidation, including the regulatory candidate later merged)
- After consolidation: 6 shortlist-eligible entries (1 overlap merge: regulatory candidate folded into the SEAtS structural-wedge candidate, upgraded Moderate → Strong)
- Overlap clusters found: 1 (competitive-intelligence + regulatory angles, both pointing at the same UKVI/engagement-compliance gap)
- Confidence distribution: Strong — 2 · Moderate — 1 · Weak — 3 (excluding the overlapped-out regulatory candidate)
- Structural wedge candidates: 1 (SEAtS Software, urgency estimated at 6 months)
- Searches/fetches run: 32 total — approximately 11 on Phase 0 baseline (Celcat's own site, docs, pricing, Capterra listing), 7 on customer/market voice (reviews, review-site coverage, job postings), 10 on competitive & adjacent intelligence (competitors, funded entrants, SEAtS specifically), 2 on environmental/regulatory signals (UKVI mandate change), with some searches spanning more than one angle
- Notable research constraint: Celcat has almost no independent public review footprint — no G2 listing found, a single Capterra review, and no Trustpilot presence — which caps several candidates at Weak confidence regardless of how specific the underlying signal is, and materially limits what the "customer & market voice" angle could contribute versus a product with a fuller review base
- Generated: 2026-07-27
