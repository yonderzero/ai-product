---
name: 06-interview
description: Product Track session 06 workshop (Customer Interviews). Write a past-behaviour interview guide for the top five problems, rehearse it on the team's synthetic user and sceptic, then test the problems against the real interview notes the team brought. Writes 06-interviews.md.
---

# 06 · Interview

**Goal.** Put the top five problems in front of customers: a real interview guide, a rehearsal with the personas from session 05, and the evidence from the interviews the team brought. Session 08 shortlists with this evidence in hand.

Work in the team's product folder: the current folder, or the folder below it that has `product.md`. If there is none, run `/ai-product:ai-product-setup` first. Remind the team they can add files to `documents/` at any time, and read any new ones. Read `04-long-list.md` (the top five in shape), `panel/` and `documents/`.

## Steps

1. **The guide.** Use the `interview-script` skill for an interview with the day-to-day user in `panel/`, about the top five problems. Then cut the core exploration to **seven questions about past behaviour**: strike every "would you", keep "walk me through the last time". Put the guide in `06-interviews.md`, using `templates/06-interviews.md`.

2. **Rehearse.** Run `synthetic-customers` mode 4 (be interviewed) twice: first the user, then the sceptic, about eight minutes each. One person asks, the others take notes. When the team types "end interview", give the feedback and add the rehearsal notes to `06-interviews.md`, marked synthetic.

3. **The real evidence.** For each interview file in `documents/`, use the `summarize-interview` skill. Then, for each of the top five problems, list what confirms it, what contradicts it, and the best real quote, with file and line. Add it to `06-interviews.md`. If the team has no interview notes, say so and ask for second-hand evidence from support or sales, tagged `[team]`.

4. **Calibrate one persona (if time).** Pick one real answer from step 3 that the user persona hasn't seen and run `synthetic-customers` mode 3 (calibrate). Log the score.

5. **Book a real customer.** Ask who the team can show a prototype to for fifteen minutes on Wednesday afternoon, and note it at the end of the file.

## Done when

- [ ] a seven-question guide with no "would you"
- [ ] rehearsal notes for the user and the sceptic
- [ ] for each of the top five: real evidence for or against, or a note that there is none

Finish with the checklist and: "Next: `/ai-product:07-day-one`."
