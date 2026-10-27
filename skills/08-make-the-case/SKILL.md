---
name: 08-make-the-case
description: Product Track session 08 workshop (Ideation, Prioritisation, ROI & Pricing). Five parts - shortlist the long list with the synthetic panel and interview evidence, ideate AI-first solutions, score and pick one, write the problem and nine-section proposal, and build a first clickable prototype for the developers. Writes 08-shortlist.md, 08a-ideas.md, 08-scorecard.md and handoff/problem.md, proposal.md, prototype/.
---

# 08 · Pick one and make the case

**Goal.** One idea, the case for it, and a first clickable prototype, ready for the developers at Align.

Work in the team's product folder: the current folder, or the folder below it that has `product.md`. If there is none, run `/ai-product:start` first. Remind the team they can add files to `documents/` at any time, and read any new ones. Read `04-long-list.md`, `06-interviews.md`, `panel/` and `handoff/domain-read.md`.

Five parts. Keep the team moving: if they are still on part B at the halfway point, push them to pick.

## Part A · Shortlist

1. Run `synthetic-customers` mode 5 (score) on `04-long-list.md`, one subagent per persona.
2. Fill `templates/08-shortlist.md` into `08-shortlist.md`, with the real evidence from `06-interviews.md` next to the panel scores. When they disagree, the real evidence wins.
3. With the team, apply the three tests and keep three problems. Every cut gets a reason. The incoming idea competes like any other.
   - **Pain worth paying for:** high pain and pay, a clear route to budget, and the interviews don't contradict it.
   - **Hard to copy:** it runs on domain knowledge or data a newcomer doesn't have.
   - **A number:** the outcome can be counted (hours, cost, churn, revenue, price).

## Part B · Ideate

Use the `ai-redesign` skill on the workflows behind the three shortlisted problems. At least two solution ideas per problem, with an agent as the primary actor, not a chatbot on the side. Save `08a-ideas.md`. Ask the team for their own ideas and add them; aim for six or more.

Apply the **agentic check** to each idea: if every step is deterministic, it's automation. Where does the agent decide, plan or act?

## Part C · Score and pick

1. Fill `templates/08-scorecard.md` into `08-scorecard.md` for every idea. Gates first: a dashboard, a chatbot, or anything nobody pays for is out.
2. The team picks **one** idea and one in reserve. Write down why, in their words.

## Part D · Write the case

1. Fill `templates/problem.md` into `handoff/problem.md` for the chosen idea, from `08-shortlist.md`, `06-interviews.md` and `panel/`.
2. Fill `templates/proposal.md` into `handoff/proposal.md` from all the files. Use rough numbers with a clear source, and show the working.
3. Leave two lines for the team to write themselves: **the outcome number** (section 5) and **the price** (section 9). If they want a starting point for the price, offer `synthetic-customers` mode 8 (Van Westendorp), marked as a synthetic vote.

## Part E · First prototype

Build `handoff/prototype/index.html`: one self-contained HTML file, realistic fake data, no backend, no login, no external requests. Show the main flow of the proposal, and make two moments obvious: where the agent does the work, and where the user approves it. Ask the team to open it in a browser and click through once.

## Done when

- [ ] three problems shortlisted, every cut with a reason
- [ ] one idea picked, one in reserve, with the reason
- [ ] `handoff/problem.md` and `handoff/proposal.md`, with the outcome number and the price written by the team
- [ ] `handoff/prototype/index.html` clicks through the main flow

Finish with the checklist and: "At Align, with your developers: `/ai-product:align-product-spec`."
