# Persona schema

One persona per file, `research/personas/<id>.md`. The layout follows MatrAIx's four groups (background, psychology, capability, behaviour) with the business fields a B2B software buyer needs. Every field ends with its grounding tag: `[documents/<file>]`, `[source: <url>]`, `[PM]` or `[assumed]`.

```markdown
# <id> · <first name>, <role>

modelled_on: <real customer organisation or type, kept for the product manager> [PM]
panel_role: buyer | user | sceptic | influencer

## Background
- organisation: <segment, size, sites, region> [...]
- group position: independent | part of a group, budget goes to <who> [...]
- role and tenure: <title, years in role, reports to> [...]
- runs on: <our product version/modules, plus other systems and spreadsheets> [...]

## Business
- who signs: <role> above <amount> [...]
- budget route: new tier | add-on | price rise | renewal | not budgeted [...]
- what they are measured on: <1–3 KPIs> [...]
- renewal or contract moment: <when, if known> [...]

## Psychology
- attitude to change: early adopter | pragmatist | cautious | resistant [...]
- trust in AI: <one line, with why> [...]
- burned by: <a past rollout, vendor or project that went wrong> [...]
- will not tolerate: <the one thing that makes them quit> [...]
- would pay for: <the outcome they would buy> [...]

## Capability
- tech comfort: low | medium | high [...]
- data they hold: <what, where, how clean> [...]
- time they can give a new tool: <per week> [...]

## The problem, through their eyes
- the problem in their words: "<how they'd describe the problem from `problem/problem.md`>" [...]
- how often it hits them, and what it costs them: <…> [...]
- what they do about it today: <workaround, tool, person, or nothing> [...]
- options they've tried or considered: <and why they stopped or didn't start> [...]
- what would make them switch: <…> [...]
- what worries them about a new way: <for AI: trust, errors, losing control, their job> [...]

## Behaviour
- a normal day: <three sentences: when they open the product, what they do, where they leave it> [...]
- workarounds: <spreadsheets, exports, phone calls, double entry> [...]
- last time it went wrong: <a concrete incident> [...]
- how they buy: <trial, reference call, procurement, RFP> [...]

## Buying insight (buyer persona; optional for others)
- priority initiative: <what makes them invest now, and what happens if they don't> [...]
- success factors: <what result they expect to see> [...]
- perceived barriers: <what makes them doubt this or us> [...]
- decision criteria: <what they compare, and against whom> [...]
- buyer's journey: <who is involved, the steps, how long> [...]

## Voice
- sounds like: "<one sentence in their words>" [...]

## Evidence log
| Kind | Evidence, verbatim | Source |
|---|---|---|
| quote | "…" | documents/<file>, line … |
| pain | … | … |
```

The buying-insight fields follow Adele Revella's Five Rings of Buying Insight. The evidence log lists the rows from `panel/evidence.md` the persona is built on; when someone asks "where did that come from?", the answer is here.

## Spread rules for a panel of 3–5

- At least one buyer and one day-to-day user.
- At least one sceptic.
- For group-owned customers, one persona whose budget goes to a group CFO.
- No two personas share segment and role.
- Fewer than a third of fields `[assumed]`; report the share in `research/panel.md`.

## Illustrative persona (timetabling software)

```markdown
# p3 · Martine, timetabling manager

modelled_on: a mid-size university, three campuses [PM]
panel_role: user

## Background
- organisation: public university, 18,000 students, 3 campuses [assumed]
- group position: independent; budget through the faculty IT committee [assumed]
- role and tenure: timetabling manager, 9 years, reports to the registrar [PM]
- runs on: the timetabling product, plus a room-booking spreadsheet and the student record system [documents/interview-02.md]

## Business
- who signs: registrar above €20,000 [assumed]
- budget route: renewal [PM]
- what they are measured on: clash-free timetables published on time; room utilisation [documents/interview-02.md]
- renewal or contract moment: August, before term planning [assumed]

## Psychology
- attitude to change: pragmatist [documents/interview-02.md]
- trust in AI: will use suggestions, won't let it publish without her [documents/interview-02.md]
- burned by: a 2023 room-booking integration that double-booked lecture halls [documents/interview-02.md]
- will not tolerate: anything that changes a published timetable without telling her [PM]
- would pay for: getting the two-week clash-resolution crunch down to two days [documents/interview-02.md]

## Capability
- tech comfort: high [PM]
- data they hold: rooms, staff availability, course structures; staff availability is out of date [documents/tickets.csv]
- time they can give a new tool: two hours a week outside term planning [assumed]

## Behaviour
- a normal day: opens the product at 08:00 to check overnight changes, spends the morning on staff change requests, ends with an export to the room spreadsheet [documents/interview-02.md]
- workarounds: a shared spreadsheet of room exceptions; phone calls to departments [documents/interview-02.md]
- last time it went wrong: a staff absence in week 1 cascaded into 40 manual moves [documents/interview-02.md]
- how they buy: reference call with another university, then procurement [assumed]

## Voice
- sounds like: "I don't need it to be clever. I need it to stop me moving forty lectures by hand in week one." [documents/interview-02.md]
```
