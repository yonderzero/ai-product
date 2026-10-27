---
name: ai-product-problem
description: Fourth step, after ai-product-discovery. Takes the problem the team chose, says it sharply as a customer job (Jobs to be Done), grades the evidence (Mom Test), pressure-tests it (including the four forces of switching), then thinks bigger - a BHAG, the job map, what customers most want fixed, adjacent segments where it hurts now - and lays out three framings (as stated, the bigger job, the moonshot), each sized, so the product manager picks the right problem and the opportunity it captures. Writes problem/evidence.md, problem/framings.md and problem/problem.md.
---

# ai-product-problem

Is this the right problem? Is it real, does it hurt enough, and is it ambitious enough? The skill sharpens the problem the team picked, tests it, and then pushes it bigger, toward a higher AI level and a bigger opportunity, until the product manager chooses the right problem to solve. Think first: no building and no features here.

## How to talk

Conversational, short messages, one question at a time. Never send a list of questions. Don't explain what you're about to check; just do it. While research runs, keep talking with the product manager. Use the methods in `references/methods.md` as tools, in plain language; name a method only when it helps.

## Save as you go

Write each file as soon as its step has content, and update it as you go. Mark any section you haven't reached `Not done yet`. If the product manager says they're out of time or wants to move on, stop cleanly: save what's there, say which steps are left, and that they can run this skill again to continue, or edit the files themselves. Update `index.html` before you stop. Moving on is fine as long as something is saved.

## Before you start

Work in the product folder: the current folder, or the folder below it that has `product.md`. This skill's files go in `problem/` inside it: `evidence.md`, `framings.md` and `problem.md` mean `problem/<name>`. The other skills' files are in `vision/` and `discovery/`. `product.md` and `documents/` stay at the top. Create `problem/` if it doesn't exist.

- No `product.md`, or it's empty: say in one line that the product profile comes first, ask them to run `/ai-product-start`, and stop.
- Nothing in `vision/` or `discovery/`: say in one line that this skill builds on them, ask them to run `/ai-product-vision` or `/ai-product-discovery` first, and stop. Anything saved there is enough to go on.

Read `product.md`, everything in `vision/` and `discovery/`, and anything in `documents/` you haven't read yet. Read `references/methods.md`.

If files from an earlier run exist, say which steps are done and which aren't (look for `Not done yet`), and ask whether to continue, redo a step, or start again. Read the files as they are now: the product manager may have edited them.

## Steps

1. **What this is.** Say which product you're working on, then explain in two or three sentences, your own words:

   > You've picked a problem to go after. Now we make sure it's the right one: we say it sharply, check the evidence, and test it. Then we think bigger, so that solving it captures as much value as possible and moves your product up the levels.

   Then ask: "Shall we start?" Wait for a yes.

2. **The problem.** Offer the likely starting points, short: "Start with" and the "Grow" bets in `discovery/discovery.md`, and the top opportunities in `vision/opportunities.md`. Ask: "Which problem are you going after?" If they name a feature or a solution, ask which customer problem it solves, and use that.

3. **Say it as a job.** Draft the job statement (*When [situation], I want to [motivation], so I can [outcome]*), the struggling moment, and its functional, emotional and social sides, from the files. Ask, one at a time, only what you can't fill:
   - Who has this problem most? Which persona?
   - When does it hit them? Tell me about the last time.
   - What are they really trying to get done? (Ask "why?" until you reach the job behind the task.)

   Start `framings.md` from `templates/framings.md`.

4. **The evidence.** In the background, research the problem: reviews, forums, job postings, the customers' own words, and the market. At the same time, go through `documents/` and the earlier files for everything that backs it. Grade it with the Mom Test (`references/methods.md`): past events, workarounds and money already spent are strong; opinions, compliments and "we'd use that" are weak. Fill `templates/evidence.md` into `evidence.md`. Tell the product manager the overall grade in one line, and what's missing.

5. **Pressure test.** One question at a time, filling the pressure-test section of `framings.md`:
   - Is it real? How many customers, how often, in whose words?
   - Does it hurt enough? What does it cost them, who pays, and would they pay to make it go away?
   - What do they do about it today?
   - Why us? What do we have that makes us the ones to solve it?
   - Why now?
   - The four forces: what pushes them to change, what would pull them to something new, what would worry them (for AI: trust, errors, losing control), and what habit keeps them where they are? Give a switching verdict.
   - Then argue the strongest case that this is the wrong problem, and ask: "How would you answer that?"

6. **Think bigger.** One part at a time:
   - **The BHAG.** Ask: "If you solved this completely, for every customer, what would be true?" Draft two or three bold, measurable, dated options from the job, the vision's day with the System of Understanding, and the opportunities. The product manager picks one and makes it theirs. If it goes beyond `vision/vision.md`, say so; they can update the vision later.
   - **The job map.** Map the job onto the eight steps in `references/methods.md`, mark which ones the product covers today and at which AI level. Show the uncovered steps: "This is where a bigger version of the problem sits."
   - **What customers most want fixed.** From `documents/`, the research and the product manager: beyond this problem, what's the biggest thing current customers want fixed? Ask: "If your customers could fix one thing about their work, what would it be?" If it's bigger than the problem they picked, say so.
   - **Adjacent segments.** Research where else this problem is very painful now: other customer sizes, neighbouring verticals with the same job, the partners before and after your customers, other countries. For each, why it hurts there now, how big it is, and the evidence. Ask: "Which of these could you reach?"

7. **Three framings.** Lay out the problem three ways, in the table in `framings.md`:
   - **as stated:** the problem as the team brought it;
   - **the bigger job:** the problem widened along the job map, toward what customers most want fixed, one or two levels up;
   - **the moonshot:** the BHAG.

   For each: the problem, for whom, the level, the value from existing customers, new customers or revenue (including adjacent segments), the evidence grade, and how it moves toward the BHAG. Size each with the sizing rules in the ai-product-vision skill's `references/opportunities.md` (at least one measured number, at most two labelled assumptions, the working shown; otherwise "not sized"). Show the three side by side, short.

8. **The right problem.** Ask: "Which one will you go after?" Usually it's the most ambitious one they can start on now. Then fill `templates/problem.md` into `problem.md`:
   - the BHAG, and the problem as a job statement, with today's workaround and what it costs;
   - which framing and why, the level from today to target, and how it moves toward the BHAG;
   - the opportunity: more value for existing customers, new customers, and the size;
   - what success looks like;
   - **what we need to learn before building:** the riskiest assumptions, most dangerous first, each with two or three Mom Test questions about their life, the past and specifics. These feed the research and interview skills;
   - what we're parking, and why.

   Show the problem and the opportunity, and ask: "Is this right?"

9. **Update the profile.** In `product.md`, add one line under `## The idea we have in mind`: the right problem in a few words and the BHAG, pointing to `problem/problem.md`.

10. **The deck.** Update `index.html`, the product's deck: follow `references/deck.md` in the ai-product-start skill's folder (next to this skill's folder).

11. **Done.** Show the files you wrote and sum up in three lines: the BHAG, the right problem, and the riskiest assumption to test first. Say the next step is `/ai-product-research`.

## Done when

- `evidence.md` grades the evidence with the Mom Test, with sources;
- `framings.md` has the job, the pressure test with the four forces and the case against, the BHAG, the job map, what customers most want fixed, adjacent segments, and three sized framings;
- `problem.md` has the right problem the product manager confirmed, the opportunity, what success looks like, and the riskiest assumptions as Mom Test questions;
- nothing in the files proposes building a solution yet.
