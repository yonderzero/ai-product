# CELCAT — AI-First Workflow Redesign Roadmap

**Vertical:** Higher & further education timetabling and scheduling software (HE, FE/TVET)
**Product scoped:** Celcat Timetabler (marketed as "Celcat AI"), including its Room Booking, Attendance Monitoring, Exam Scheduling, and Automated Premium extensions
**Generated:** 2026-07-27

## Executive Summary

- Celcat has already shipped an unusually mature AI layer — a graph-database-backed, agentic engine ("Celcat AI") that generates term timetables, exam schedules, and multi-channel publishing largely on its own. The single biggest, most obvious transformation opportunity in this product category — automated schedule generation — is not a roadmap item here because it is already in production.
- That leaves a real, evidence-grounded roadmap of four workflows still worth rebuilding, of which two land in the top tier: turning ad-hoc room and space booking into a fully autonomous approval loop, and replacing the email-driven timetable helpdesk with a conversational assistant embedded in the product's existing student and staff portals.
- The single most important feasibility fact: all four Tier 1 and Tier 2 candidates can be built almost entirely on data Celcat's own graph database already holds — timetable occupancy, enrollment, room attributes, and policy rules — so none require a net-new integration to get started; the constraints that hold two candidates back are trust and institution-specific HR data, not missing product data.
- After the top tier ships, a timetabling officer stops manually checking every ad-hoc room request against capacity and policy, and a registry helpdesk stops answering the same "where's my next class" email hundreds of times a term — both jobs shrink to reviewing genuine exceptions.
- Two further candidates — automatically rebalancing groups and rooms after enrollment shifts, and an agent that chases and structures staff teaching preferences — are real opportunities but each has a named blocking constraint that keeps it a near-term rather than immediate build.

## Product Baseline

Celcat Timetabler is timetabling and resource-scheduling software built for universities, colleges, and further-education/TVET providers, used by hundreds of institutions across more than 30 countries. Its core modules cover interactive timetable creation, room booking, attendance monitoring, exam scheduling, and publishing — importing programme structures, modules, and confirmed registrations from a student information system (SIS) and pushing personalised timetables back out to students, staff, and invigilators across calendars, portals, and its "Celcat Now" mobile experience. It competes most directly with Scientia's Syllabus Plus (now part of TechnologyOne) among larger, centralised institutions, and is particularly strong with further-education institutions and smaller or decentralised universities; Coursedog and Ad Astra are the closest comparable players in the North American academic-operations-platform segment.

Celcat's current AI posture is not a bolt-on — it is the company's current core narrative. "Celcat AI" is described as an agentic platform built on a graph database that models relationships between staff, rooms, modules, and students, with a named "cohort of timetabling agents" that build and continuously refine conflict-free term timetables, an exam-scheduling extension that produces student and invigilator schedules "in minutes," scenario-modelling tools for testing policy changes before committing them, and automated multi-channel publishing that keeps every stakeholder's calendar current in real time. Attendance monitoring already includes automated non-attendance alerts to welfare and employer contacts. This means the transformation starting point for this roadmap is unusual: the product's central, highest-volume workflow (building the master timetable) is already transformed, so the genuine opportunity lives in the workflows that sit around that engine rather than in the engine itself. Ten workflows were decomposed in total; three of those — batch timetable generation, batch exam-and-invigilator scheduling, and real-time multi-channel publishing — are excluded from design here not because they scored poorly, but because Celcat has already shipped production redesigns of them. Of the remaining seven, four qualified for design and three were recorded as borderline and excluded.

## Transformation Landscape

| Category | Count |
|---|---|
| Total workflows decomposed | 10 |
| Already transformed by vendor (excluded from design) | 3 |
| Qualified and designed (TPS ≥ 3.5) | 4 |
| Borderline, excluded (TPS 3.0–3.4) | 3 |

| Transformation type (designed candidates only) | Count |
|---|---|
| Autonomous | 3 |
| Conversational | 1 |
| Augmented / Ambient / Predictive | 0 (each present only as a secondary type) |

| Tier (designed candidates only) | Count |
|---|---|
| Tier 1 — Transform Now | 2 |
| Tier 2 — Build Toward | 2 |
| Tier 3 — Watch | 0 |
| Tier 4 — Deprioritize | 0 |

Three of the four designed candidates take the shape of handing a full execution loop to AI rather than adding a decision-support layer — a direct consequence of Celcat's own product having already automated the judgment-heavy parts of scheduling itself, leaving mostly rule-bound, high-volume execution work (approvals, chasing, rebalancing) as the remaining manual layer worth closing out.

## Tier 1 Candidates

### 1. Ad-Hoc Room & Space Booking

Transformation type: Autonomous · Priority score: 4.2 · Evidence confidence: Strong

**Today.** When a staff member or student group requests a room or space outside the standard published timetable — a society meeting, a one-off event, an exam resit — a room-booking coordinator checks the request against room capacity, existing occupancy, and institutional policy before approving or rejecting it. Celcat's own room-booking module already checks availability automatically, but a verified user of the product still flags a live gap: no automatic warning when a booking's registered headcount exceeds venue capacity, meaning capacity mismatches still surface only when someone notices them manually.

**The AI-First Version.** A booking request triggers the agent immediately: it checks the request against real-time occupancy, room capacity, equipment, and the institution's configured priority policy (for example, no non-academic bookings during exam periods), and auto-approves or auto-rejects anything unambiguous — including the capacity-overflow check the current system lacks. The room-booking coordinator's job becomes reviewing a short queue of genuine exceptions: competing high-priority requests for the same space, unusual equipment needs, or policy edge cases (VIP or external-hire bookings) that the agent flags rather than guesses at.

**What changes for users:** requesters get an instant answer instead of waiting on manual review; the coordinator stops checking routine requests entirely.
**Time saved:** the bulk of day-to-day booking triage — the routine majority of requests — moves from a multi-step manual check to zero-touch approval.
**Outcomes changed:** eliminates the specific capacity-overflow failure mode a user has already reported, alongside double-booking risk.

**Evidence:** Competitor precedent — Ad Astra markets "conflict-free calendars with double-booking validation" and Coursedog offers customizable, automated approval workflows for event and space requests, both in the same room-scheduling category Celcat competes in. User signal — a verified Capterra reviewer (ICT Manager, education management) states Celcat "needs more automation, validation and checks to warn if registration quotas are over venue capacity." Job posting signal — UK timetabling-officer job descriptions consistently list "processing room bookings" as a discrete, recurring responsibility.

**What it takes to build:** Data required — room capacity and features (accessible), timetable occupancy (accessible), booking policy rules (accessible, already configurable via the existing Automated Premium rule engine), requester identity/role (accessible via existing SIS/directory integration). AI capability required: structured workflow agent. Integration complexity: Low — everything needed already lives inside the product's existing graph database. Build complexity: Low. Dependencies: none external and unconfirmed; this extends an existing module rather than introducing a new one.

### 2. Student & Staff Timetable Query Assistant

Transformation type: Conversational · Priority score: 3.9 · Evidence confidence: Moderate

**Today.** Students and staff email or ticket their registry or department administration team with routine timetable questions — where a next class is, why a timetable changed, whether a seminar-group swap is allowed, why a clash appeared — each taking only a few minutes to answer individually, but arriving in volumes that, by outside accounts of the same administrative burden across higher education, "bury even the most efficient teams," especially during enrollment and add/drop weeks.

**The AI-First Version.** A student or staff member asks a question in natural language, inside Celcat's own student/staff portal or the Celcat Now mobile experience, rather than emailing a person. The assistant looks up the asker's live timetable and enrollment record, answers direct lookups immediately, and checks configured policy for anything actionable (for example, whether a requested group swap is within the rules) before executing it or explaining why it can't. Anything genuinely ambiguous — a disputed clash, an unusual circumstance — routes to a human registry officer with the question and the assistant's partial findings already attached, rather than starting cold.

**What changes for users:** most timetable questions get an instant, always-available answer instead of waiting on a staffed inbox during business hours.
**Time saved:** the routine majority of registry timetable-query volume, concentrated in the peak weeks that currently strain teams most.
**Outcomes changed:** faster, more consistent answers regardless of which staff member (or none) is available; registry escalations arrive pre-triaged instead of cold.

**Evidence:** User signal — independent commentary on higher-education administrative load describes timetable and scheduling enquiries as a volume problem that "creates a wave of admin" for registry teams generally, and UK timetabling-officer job descriptions describe sustained liaison and enquiry-handling as core to the role. Adjacent-vertical precedent — Canvas's "Course Bot" already answers students' routine questions about class schedules, locations, and logistics inside a learning-management-system context, and general higher-ed chatbot adoption for registration and scheduling questions is well documented. No competitor precedent was found of a scheduling-software vendor (Celcat's direct category) shipping this specific assistant — this is a real gap in the evidence, not an oversight.

**What it takes to build:** Data required — student/staff timetable and enrollment data (accessible), group-swap and clash policy rules (accessible, but currently configured for internal use — exposing them for conversational consumption requires new work, so annotated (requires access layer)), historical query/escalation patterns to route ambiguous cases (requires access layer, not currently modelled as queryable data). AI capability required: NL interface combined with a structured workflow agent for the actionable subset of queries. Integration complexity: Low — delivered inside Celcat's own existing portal and mobile channels rather than a new surface like Microsoft Teams (a Teams-specific integration was checked and not confirmed, so the design deliberately avoids depending on it). Build complexity: Medium, driven by the access-layer work, not by missing data.

## Tier 2 Summary

| Workflow | Type | Priority Score | Blocking Constraint |
|---|---|---|---|
| Post-Enrollment Group & Room Rebalancing | Autonomous | 3.3 | No institution will hand a live, already-published timetable to an unsupervised re-solve on day one — needs a human-approval rollout phase before full autonomy, and the underlying engine has to be re-architected to re-solve incrementally rather than as a full batch run |
| Staff Teaching-Load & Preference Collection | Autonomous (secondary: Augmented) | 3.2 | Structured staff availability data mostly lives in each institution's own HR system (e.g., iTrent) — the integration exists, but a per-institution access layer to expose it to a collection agent has to be built before this runs autonomously |

## Transformation Roadmap

| Rank | Workflow | Type | Tier | Priority Score |
|---|---|---|---|---|
| 1 | Ad-Hoc Room & Space Booking | Autonomous | 1 | 4.2 |
| 2 | Student & Staff Timetable Query Assistant | Conversational | 1 | 3.9 |
| 3 | Post-Enrollment Group & Room Rebalancing | Autonomous | 2 | 3.3 |
| 4 | Staff Teaching-Load & Preference Collection | Autonomous | 2 | 3.2 |

Room booking ranks first because it is the cleanest build on the list: every data point it needs already sits inside the product, the fix targets a gap a real user has already named, and it can ship without touching anything outside the room-booking module. The timetable query assistant follows closely and can be built in parallel rather than in sequence — the two candidates don't share a build prerequisite, so there's no reason to interleave or delay one for the other. The two Tier 2 candidates are held back by trust and data-access constraints rather than by weak opportunity; staff preference collection in particular is worth watching closely because a competitor (Coursedog) already runs it in production, and because the structured availability data it would produce could, in a future round, make Celcat's already-shipped automated timetable-generation engine work from cleaner inputs — a second-order benefit outside this roadmap's scope but worth institutions' attention when prioritizing. Taken together, the Tier 1 portfolio converts two of the highest-volume manual interactions institutions have with the product — approving space requests and answering timetable questions — into exception-only human work, without requiring any new external integration to get there.

## What This Product Looks Like After Transformation

Once both Tier 1 candidates ship, the two roles that touch Celcat most often on a daily basis change in a concrete, observable way. A room-booking coordinator who used to open a queue of pending requests each morning and manually cross-check each one against capacity and policy now opens a much shorter list — only the ones the system genuinely couldn't resolve on its own, with its reasoning already attached. A registry timetabling officer who used to spend a meaningful share of the day answering the same handful of question types by email now spends that time on the smaller set of disputes and edge cases the assistant couldn't close out itself, arriving with context instead of a blank inbox.

For students and staff, the visible change is smaller but real: a room request gets an answer in seconds instead of a wait, and a timetable question gets answered the moment it's asked, inside the same portal and mobile app they already use, at any hour rather than only during registry office hours.

Celcat's identity after this round is not "the vendor that generates timetables with AI" — that positioning already exists today. It becomes the vendor whose AI runs the whole operational perimeter around the timetable, not just its initial construction: the requests, questions, and exceptions that keep arriving after the schedule is published. Competitively, that matters because Celcat's rivals in this category have so far shown AI precedent in adjacent pieces of this same perimeter — Ad Astra in real-time enrollment-driven room adjustment, Coursedog in automated faculty-preference collection — but not, on current public evidence, in autonomous ad-hoc booking approval or a conversational timetable assistant embedded in the product itself. Shipping both would put Celcat ahead on two fronts where no direct competitor has yet published evidence of shipping.

## Evidence Quality

| Rank | Workflow | Type | Tier | Evidence Confidence | Flags |
|---|---|---|---|---|---|
| 1 | Ad-Hoc Room & Space Booking | Autonomous | 1 | Strong | None |
| 2 | Student & Staff Timetable Query Assistant | Conversational | 1 | Moderate | No competitor precedent found within the scheduling-software category specifically; evidence rests on adjacent-vertical precedent and general user-burden signal |
| 3 | Post-Enrollment Group & Room Rebalancing | Autonomous | 2 | Weak | Single evidence source (competitor precedent only); no direct Celcat-specific user or job-posting signal found |
| 4 | Staff Teaching-Load & Preference Collection | Autonomous | 2 | Moderate | Strong competitor precedent but no direct user-complaint evidence; HR-integration dependency varies by institution |

## Run Statistics

- **Workflows decomposed:** 10 total — 3 already transformed in production by the vendor (excluded from design as a deliberate scoping decision, documented in Product Baseline, not a scoring exclusion), 4 qualifying for design (TPS ≥ 3.5), 3 recorded as borderline (TPS 3.0–3.4) and excluded.
- **Qualification floor:** not invoked — 4 workflows cleared the 3.5 threshold on their own merits, above the 3-candidate floor.
- **Designs completed:** 4.
- **Tier counts:** Tier 1 — 2; Tier 2 — 2; Tier 3 — 0; Tier 4 — 0.
- **Total research calls:** 26 (19 web searches, 7 page fetches) across product research, competitor precedent, and evidence verification.
- **Generated:** 2026-07-27.
