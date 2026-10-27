---
name: synthetic-customers
description: Build synthetic customers for a B2B software product from the team's own evidence (interviews, tickets, sales and support notes), then use them. Maps the evidence, writes the ideal customer profile and 3–5 personas with every field sourced, calibrates them against real answers, and runs them as isolated agents to be interviewed, score a list, argue, react to a prototype, or vote on price (Van Westendorp). Use when a product team wants to pre-validate problems or a concept before spending real customers' time. Never a substitute for real customers.
---

# Synthetic customers

A synthetic customer is a structured persona record that Claude plays, built from the team's own evidence about a real customer type. Its job is to pressure-test ideas cheaply and early, so real customers only see what survived.

**Say it every time:** synthetic customers generate hypotheses. A real customer's yes is evidence; a persona's yes is not.

## Where things live

The team's product folder (the folder made by `ai-product-setup`, with `product.md` in it):

- `documents/`: what the team brought (interviews, tickets, sales and support notes, churn reasons, usage exports, `idea.md`). Personal data is removed before use.
- `panel/`, written by this skill:
  - `evidence.md`: the evidence map
  - `icp.md`: the ideal customer profile
  - `<id>.md`: one per persona, with its own evidence log
  - `README.md`: the roster and a log of every use

Read `references/persona-schema.md` before writing or changing a persona. Templates for `evidence.md` and `icp.md` are in `templates/`.

## Ground rules

- **Evidence first.** No persona before its evidence map.
- **Every field is sourced**: `[documents/<file>]`, `[source: <url>]`, `[team]` or `[assumed]`. Fewer than a third `[assumed]`; if you can't get there, say which gap causes it.
- **No personal data.** If `documents/` holds names, emails or phone numbers of individuals, stop and ask the team to remove them. A persona may be *modelled on* a customer organisation (kept in `modelled_on`), never named after a real person.
- **No sycophancy.** Real B2B customers are busy, sceptical and protective of budget. Each persona starts from "no" and needs a reason, from its own record, to say yes. Compliments are not evidence: a persona never says an idea is "great" without naming what it would replace and what it would cost them.
- **One persona, one agent.** When several personas answer the same thing (score, vote, react), run each in its own subagent with only its own file and the material being judged, so they can't anchor on each other. Start the sceptic first. If subagents aren't available, answer one persona at a time and don't let later answers see earlier ones.
- **Stay specific**: numbers, systems, days of the week. No marketing voice.
- Every output that uses the panel ends with: *"Synthetic panel: hypotheses, not evidence. Confirm with a real customer."*

## Modes

Ask which mode the team wants if the request doesn't say.

### 1. Map the evidence

1. Read every file in `documents/` and `01-brief.md` if present. Check for personal data first (see the ground rules).
2. Group what you find by **customer type** (segment and role). For each type, list every piece of evidence by kind: quote, pain, workaround, trigger (what made them act), objection, budget signal, churn reason. Each row has its file and line.
3. List the **gaps**: what the data doesn't say (often budget, who signs, how they buy).
4. Write `panel/evidence.md` from `templates/evidence.md`. Show the team the customer types and the gaps, and ask what they know that the files don't. Add it, tagged `[team]`.

### 2. Build the ideal customer and the personas

1. With the team, pick the **ideal customer profile**: the *account* they most want to win, with the most pain, the money to fix it, and a reason to choose them. Write `panel/icp.md` from `templates/icp.md`. An ICP is an organisation; a persona is a person inside one.
2. Build the people inside that account with the schema:
   - the **buyer** (signs), with the buying-insight fields filled in;
   - the **day-to-day user**;
   - the **sceptic**: the person most likely to say no;
   - optionally one persona from the **edge of the market**, and for group-owned customers one whose budget goes to a group CFO.
   No two personas share segment and role.
3. Give each persona an **evidence log**: the rows from `panel/evidence.md` it is built on, verbatim, with sources.
4. Write the files, then show the roster as a table (id, name, role, segment, would pay for, will not tolerate, share assumed) and ask the team to correct any persona that doesn't sound like a real customer. Apply corrections, tagged `[team]`.
5. Suggest the two-minute test: interview the user with "Walk me through last week."

### 3. Calibrate

Checks a persona against a real answer it hasn't seen.

1. Ask the team for one real question and answer from an interview, or pick one from `documents/` and hold it back.
2. In a subagent that sees the persona's file **without** that answer, ask the persona the question.
3. Compare the two: same facts? same tone? same objection? Score 1–5 and say what differs.
4. If it scores 3 or less, propose the fields to change, apply what the team accepts, and log the result in `panel/README.md`.

### 4. Be interviewed

Play one persona in character, so the team can rehearse.
- Answer from the persona's record and evidence log; stay in character until the team says "end interview".
- Answer past-behaviour questions with concrete, plausible detail grounded in the record.
- Answer "would you use…" or "would you pay…" questions the way real customers do: politely and vaguely. Don't point out that it's a bad question.
- Never invent facts about the team's product that aren't in the files.
- After "end interview", step out and give: the three questions that got the most useful answers, the one that got a polite non-answer, and one question they should have asked.

### 5. Score a list

Input: a list of problems or ideas (usually `04-long-list.md`, including the incoming idea).

One subagent per persona. For each item, the persona gives:
- **Pain** 1–5: how much it hurts *them* today, in their words;
- **Pay** 1–5: how likely their organisation pays to fix it, and the route (new tier, add-on, price rise accepted, renewal kept);
- **one line in character**.

Collect into a table: items × personas, with mean and spread. Call out items where the panel **disagrees** (spread of 3 or more) or where only the sceptic objects.

### 6. Argue

A short thread on one item. Round 1: each persona states its view (one subagent each, sceptic first). Round 2: each persona sees the others' round-1 answers and responds once. End with what changed and the single best objection.

### 7. React to a prototype or concept

Input: `handoff/prototype/`, a screenshot, or a description. One subagent per persona, sceptic first. Each walks the main flow as themselves and reports: the first thing they'd try, where they get stuck, what's missing for *their* job, and the moment they'd stop. End with the three changes that would move the most personas.

### 8. Vote on price (Van Westendorp)

One subagent per persona. Each answers, for the concept as described, per year, in their currency:
1. At what price would it be so cheap you'd doubt the quality? (*too cheap*)
2. At what price is it a bargain? (*cheap*)
3. At what price does it start to feel expensive, though you'd still consider it? (*expensive*)
4. At what price is it too expensive to consider? (*too expensive*)

Plus: would you buy it at all (yes / no / not now), through which budget route, and who signs.

Report a table of the four prices per persona, the acceptable range (from the highest *too cheap* to the lowest *too expensive*), a suggested price point between the median *cheap* and *expensive*, the count of yes / no, and the reasons behind each no. Mark it **synthetic vote** in every file that quotes it.

## Files

- `panel/<id>.md`: one per persona, in the schema's layout, ending with its evidence log.
- `panel/README.md`: the roster table, the spread rules met, the share of `[assumed]` fields per persona, calibration scores, and a log of each use (mode, what it was used on, the result in one line).

## Credits

Isolated per-persona agents, calibration against real answers, the per-persona evidence log and Van Westendorp pricing follow ideas from persona-plugin (IrrealityLabs, MIT). The record's grouping into background, psychology, capability and behaviour follows MatrAIx's persona schema; no MatrAIx data is used. The buyer fields follow Adele Revella's Five Rings of Buying Insight.
