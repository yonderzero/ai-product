# Threat Exposure Scan — CELCAT
*Generated: 2026-07-27 | Own-research pass, no shared cache | Evidence section is sourced only — hypothetical scenarios are clearly walled below and speculative*

## Threat Summary

**Threat Exposure Score: 5/10 — Contested**

| Vector | Status | Named entities | Confidence |
|---|---|---|---|
| V1 — Point-Solution Unbundling | Likely | Skedda | Low |
| V2 — SMB Full Rebuild | None found | None | Medium |
| V3 — Integration / Interoperability Layer | Confirmed | Edusign, TimeEdit, ADE | Medium |
| V4 — Distribution Bypass | Confirmed | Ellucian, TimeEdit | Medium |
| V5 — On-Top / API Wrapper | None found | None | Medium |

## Evidence: Vector Analysis

### V1 — Point-Solution Unbundling — Likely
- **Status:** Likely
- **Named entities:** Skedda (horizontal room/space-booking product with documented higher-ed traction, e.g. Northwestern University)
- **Evidence summary:** A single verified reviewer (education-sector customer, 501–1000 employees, 2+ years' daily use) described CELCAT Timetabler as lacking advance validation between registration numbers and venue capacity, surfacing over-enrolled classes and scheduling clashes only after the fact rather than warning during setup. Separately, horizontal room/space-booking point solutions such as Skedda have established traction in higher education without yet marketing explicitly against CELCAT's venue-booking module specifically.
- **Confidence:** Low
- **Sources:**
  - GetApp CELCAT Timetabler review page (as of 2022-10) — https://www.getapp.com.au/software/2074278/celcat-timetabler
  - Software Advice CELCAT Timetabler profile, same review syndicated (as of 2022-10) — https://www.softwareadvice.com/scheduling/celcat-profile/
  - Skedda higher-ed customer/solutions page (as of 2026-07) — https://www.skedda.com/solutions/university-scheduling-software

### V2 — SMB Full Rebuild — None found
- **Status:** None found
- **Named entities:** None
- **Evidence summary:** Searches for a funded, self-serve/PLG entrant targeting a lower-ACV tier of the academic-timetabling market than CELCAT's core segment returned no qualifying match. The one well-funded, vertical-matched company found — Coursedog ($113M raised across 5 rounds, including a $90M growth round from JMI Equity and a $17M Series A led by Coatue) — targets large, centralized institutions (CUNY, Columbia, BYU), the opposite direction of an SMB rebuild.
- **Confidence:** Medium
- **Sources:**
  - Coursedog funding coverage (as of 2026-07) — https://www.coursedog.com/articles/coursedog-raises-17m-to-break-down-barriers-in-higher-education
  - Coursedog company profile/funding aggregation — https://www.clay.com/dossier/coursedog-funding

### V3 — Integration / Interoperability Layer — Confirmed
- **Status:** Confirmed
- **Named entities:** Edusign (education attendance/e-signature platform), CELCAT, TimeEdit, ADE
- **Evidence summary:** Edusign's own integrations page advertises a live connector to ADE (schedules feed Edusign automatically for attendance) alongside two "coming soon" connectors under active development: one to CELCAT (pilot scheduled with Université Panthéon-Assas) and one to TimeEdit (rollout planned at Kedge Business School, September 2026). This meets the bar for a named platform advertising native connectors to CELCAT and at least two of its direct timetabling competitors.
- **Confidence:** Medium
- **Sources:**
  - Edusign integrations page (as of 2026-07) — https://edusign.com/integration

### V4 — Distribution Bypass — Confirmed
- **Status:** Confirmed
- **Named entities:** Ellucian, TimeEdit
- **Evidence summary:** Ellucian — an established Student Information System vendor (Banner/Ellucian Student) with existing enterprise distribution across higher education, an adjacent category to standalone timetabling — announced a partnership embedding TimeEdit's curriculum-planning and scheduling functionality directly inside Ellucian Student, positioning it as native SIS functionality rather than a separate system institutions must procure independently.
- **Confidence:** Medium
- **Sources:**
  - Ellucian newsroom press release, published 2025-07-08 — https://www.ellucian.com/newsroom/ellucian-partners-timeedit-transform-higher-education-curriculum-planning-and-scheduling

### V5 — On-Top / API Wrapper — None found
- **Status:** None found
- **Named entities:** None
- **Evidence summary:** No commercial third-party product was found building a substitutive layer on top of CELCAT's API or ecosystem. Searches did surface individual-developer, non-commercial projects on GitHub that reverse-engineer or consume CELCAT's timetable feed for personal calendar export (Google Calendar/Outlook/iCal), but these are hobbyist utilities with no business behind them, no substitutive scope, and no evidence of monetization or growth — they do not meet the vector's bar.
- **Confidence:** Medium
- **Sources:**
  - Searches ran; no qualifying commercial entity retrieved this run (see What We Did Not Find)

## What We Did Not Find

- Three independent searches for an AI-native or conversational-first timetabling entrant marketing directly against CELCAT returned only CELCAT's own AI product announcements ("Celcat AI") — no competing entrant was named.
- Searches for a funded SMB/self-serve academic-scheduling rebuild returned only low-cost/free general tools (e.g. FET — free/open-source school timetabling; Schedula — ~$29/month subscription timetabling for schools) and one enterprise-upmarket competitor (Coursedog). None of these is a funded company explicitly targeting a lower-ACV tier of CELCAT's own vertical, so V2 stays "None found" rather than being stretched to fit.
- Two searches for CELCAT connectors on Zapier, Make, or Workato returned no listing on any of the three platforms.
- Two searches for a commercial AI copilot or on-top wrapper product naming CELCAT specifically, or generalizing across multiple VMS timetabling back-ends, returned no named commercial entity — only the individual-developer GitHub projects noted under V5 above.
- The one review-based complaint used as V1 evidence is a single reviewer from October 2022 (~3.75 years old); a refresh check of CELCAT's Info-Tech/SoftwareReviews listing found zero published reviews there, and no newer independent review surfaced to corroborate or update it.

---

## Hypothetical Attack Scenarios

> ⚠️ HYPOTHETICAL — NO EVIDENCE OF ACTIVE ATTACKER. Red-team scenario for planning purposes only.

Everything below this line is a constructed red-team scenario built from CELCAT's own researched weak points, not a finding. Attackers are described as archetypes, never as invented company names — any real name appearing here is a precedent citation traceable back to the Evidence section above.

**Confirmed threats (not simulated):** Ellucian's embedding of TimeEdit inside Banner/Ellucian Student (distribution bypass) and Edusign's live/in-preparation connectors spanning CELCAT, TimeEdit, and ADE (integration layer) are both already real and documented above — see V4 and V3 in Evidence: Vector Analysis. Neither is simulated here.

### Scenario: The precision point-solution — Point-Solution Unbundling (scan status: Likely)
> ⚠️ HYPOTHETICAL — NO EVIDENCE OF ACTIVE ATTACKER. Red-team scenario for planning purposes only.

- **Entry point:** A horizontal, AI-native room/space-booking product (in the mold of the traction Skedda already has in higher ed) targets the exact seam CELCAT's own customer feedback flagged — venue capacity and registration numbers that aren't cross-validated at scheduling time, only discovered as clashes after the fact.
- **Wedge mechanic:** The entrant sells one thing extremely well: real-time capacity and clash validation the moment a class is scheduled, not after publication. It's pitched as a companion to CELCAT, not a replacement, which lowers the barrier for a timetabling office to adopt it.
- **Expansion path (12–36 months):** Months 0–12: the entrant owns the room-utilization and capacity-conflict dataset for early-adopter departments. Months 12–24: it adds registration-number validation and light scheduling suggestions, becoming the system staff check first each morning. Months 24–36: with the operational data and daily habit already captured, it pitches a full timetabling module to the same institutions, positioning CELCAT as the legacy system being worked around.
- **Weak point exploited:** capacity and registration-number validation gaps that let over-enrolled or clashing classes surface only after scheduling is complete, rather than being flagged in advance.
- **Combination risk:** wedge-then-expand
- **Time to threat:** 24mo

### Scenario: The budget rebuild from below — SMB Full Rebuild (scan status: None found)
> ⚠️ HYPOTHETICAL — NO EVIDENCE OF ACTIVE ATTACKER. Red-team scenario for planning purposes only.

- **Entry point:** A low-cost, self-serve scheduling product targets further education colleges, vocational/TVET providers, and small multi-campus training operators — the segment CELCAT's enterprise-oriented pricing and implementation complexity underserve (the market already has free/low-cost general tools circling this tier, per What We Did Not Find, though none yet is a funded, vertical-focused rebuild).
- **Wedge mechanic:** Dramatically simpler self-serve signup and setup at a fraction of CELCAT's price, appealing to resource-constrained institutions currently priced out or overwhelmed by a comprehensive enterprise product they only use a fraction of.
- **Expansion path (12–36 months):** Months 0–12: wins standalone FE/vocational customers on price and simplicity. Months 12–24: adds multi-campus and exam-scheduling features to match CELCAT's feature depth. Months 24–36+: with venture funding, moves upmarket toward smaller, non-centralized universities — CELCAT's own stated stronghold segment.
- **Weak point exploited:** enterprise-oriented pricing and a comprehensive-but-complex product that underserves smaller, resource-constrained institutions relative to a simpler, cheaper alternative.
- **Combination risk:** none apparent
- **Time to threat:** 36mo+

### Scenario: The convenience layer that keeps climbing — On-Top / API Wrapper (scan status: None found)
> ⚠️ HYPOTHETICAL — NO EVIDENCE OF ACTIVE ATTACKER. Red-team scenario for planning purposes only.

- **Entry point:** CELCAT openly markets its own API and integration framework for connecting to SIS, HR, finance, space, and learning systems — and independent developers have already demonstrated, in public GitHub projects, that CELCAT's timetable feed can be pulled and reused without any official partnership.
- **Wedge mechanic:** A conversational scheduling assistant reads a student's or staff member's timetable via that same open/reverse-engineered feed and offers a nicer daily interface — natural-language "what's my next class," proactive clash and room-change notifications — sitting visually on top of CELCAT with no cooperation required from CELCAT itself.
- **Expansion path (12–36 months):** Months 0–12: read-only convenience layer (calendar sync, notifications) builds a daily-use habit. Months 12–24: adds write-back actions — room-swap requests, absence reporting — becoming the surface people actually interact with instead of CELCAT's own UI. Months 24–36: generalizes across multiple VMS back-ends (CELCAT, TimeEdit, ADE alike), marketing itself as "the layer that works with whatever your institution already runs," reducing each underlying vendor to an interchangeable data store.
- **Weak point exploited:** an openly documented, actively marketed integration API, already shown by independent developers to be reusable without a commercial partnership in place.
- **Combination risk:** on-top-evolving-to-integration
- **Time to threat:** 24mo

## Defensive Priorities

1. **Close the capacity/registration validation gap.** The one concrete, if dated, customer complaint found in this scan — clashes and over-enrollment surfacing only after scheduling, rather than being flagged in advance — is exactly the kind of narrow, well-defined pain a point-solution entrant would target first (see the Point-Solution Unbundling scenario). Shipping proactive, pre-publish capacity/registration validation closes the most concrete wedge this scan identified.
2. **Move from reverse-engineered access to an official integration/partner story.** Edusign is already building toward CELCAT connectivity without an announced CELCAT partnership, and independent developers already pull CELCAT's feed unofficially. Establishing an official partner/certification program for attendance, e-signature, and LMS platforms — rather than leaving this to unofficial and third-party-initiated integration — keeps CELCAT positioned as the system of record instead of an interchangeable back-end.
3. **Sharpen the case against SIS-embedded scheduling for CELCAT's core segment.** Ellucian's embedding of TimeEdit directly inside Banner raises the bar for what "good enough, bundled" scheduling looks like to Banner-using institutions. CELCAT's known strength with further-education and smaller/non-centralized institutions is exactly where a simpler, more flexible, non-bundled offering can still win — worth reinforcing explicitly in positioning and pricing rather than competing head-on with bundled convenience.

## Methodology Note

- **Searches fired:** 22 WebSearch queries + 4 WebFetch verification pulls (26 total against a 15–20 guidance budget — the extra fetches were used to verify two search-engine summaries against primary sources before finalizing status, see below).
- **Allocation:** V4 (5 searches, largest share per guidance) → Confirmed via the Ellucian/TimeEdit press release. V1 (4 searches + 2 verification fetches) → the initial search summary implied broader review sentiment; fetching the actual GetApp and Software Advice pages directly revealed it was one reviewer (Oct 2022) syndicated across affiliated Gartner Digital Markets properties, not independent corroboration — downgraded accordingly to Likely with `single_source` and `stale_evidence` flags. V2 (4 searches) → None found. V3 (3 searches + 1 fetch) → Confirmed via Edusign's own integrations page. V5 (4 searches) → None found; only non-commercial hobbyist tooling surfaced.
- **TES arithmetic:** 2 Confirmed vectors (V3, V4) × 2 = 4, plus 1 Likely vector (V1) × 1 = 1. Total = 5 → **Contested**.
- **Staleness refresh:** V1's sole evidentiary review (Oct 2022) triggered a refresh check; CELCAT's Info-Tech/SoftwareReviews listing was fetched directly and showed zero published reviews, so no newer corroboration was available — status and confidence reflect this.
- **`no_named_entity` flag:** not used — the one Likely vector (V1) has a named entity (Skedda).
- **Fabrication gate:** applied to all five vectors before status assignment; no vector was upgraded to Confirmed without both a named entity and a retrieved source. V2 and V5 were kept at "None found" rather than stretched to Likely on thin/tangential evidence (Coursedog's opposite-direction segment targeting for V2; hobbyist non-commercial GitHub tooling for V5).
