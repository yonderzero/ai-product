---
name: ai-product-research
description: Fifth step, after ai-product-problem. Goes deep on how each type of customer experiences the chosen problem - in their own words, what they do today, the options they have - from the product manager's own documents (customer data, interviews, meeting transcripts, emails, tickets) and public research, then defines the ideal customer and builds synthetic personas (buyer, user, sceptic, adjacent segment) with every field sourced, reality-checked and calibrated, uncovers agentic customer experiences by interviewing the product manager on how people use the product today, agentifying those workflows, and showing the new economics (licence + agents + far less labour: the customer saves, the product earns more), and lets the product manager talk to the personas (interview, score, argue, react, vote on price, calibrate) to pressure-test the problem, the experiences and later ideas; rerun it any time to talk to them again. Writes research/ (market.md, evidence.md, icp.md, personas/, experiences.md, panel.md).
---

# ai-product-research

How does each type of customer really experience the problem? What do they do today, and what options do they have? Then: personas built from that evidence, which the product manager can talk to and use to pressure-test ideas.

**Say it every time the personas are used:** synthetic personas generate hypotheses. A real customer's yes is evidence; a persona's yes is not.

## How to talk

Conversational, short messages, one question at a time. Never send a list of questions. Don't explain what you're about to check; just do it. While research runs, keep talking with the product manager.

## Save as you go

Write each file as soon as its step has content, and update it as you go. Mark any section you haven't reached `Not done yet`. If the product manager says they're out of time or wants to move on, stop cleanly: save what's there, say which steps are left, and that they can run this skill again to continue, or edit the files themselves. Update `index.html` before you stop. Moving on is fine as long as something is saved.

## Before you start

Work in the product folder: the current folder, or the folder below it that has `product.md`. This skill's files go in `research/` inside it: `market.md`, `evidence.md`, `icp.md`, `experiences.md`, `panel.md` and `personas/` mean `research/<name>`. The other skills' files are in `vision/`, `discovery/` and `problem/`. `product.md` and `documents/` stay at the top. Create `research/` if it doesn't exist.

- No `product.md`, or it's empty: say in one line that the product profile comes first, ask them to run `/ai-product-start`, and stop.
- Nothing in `problem/`: say in one line that research looks at the problem they chose, ask them to run `/ai-product-problem` first, and stop. Anything saved there is enough to go on.

Read `product.md`, `problem/` (above all `problem.md` and its riskiest assumptions), and `vision/` and `discovery/` where they exist. Read `references/persona-schema.md`.

If files from an earlier run exist, say which steps are done and which aren't (look for `Not done yet`), and ask whether to continue, redo a step, or start again. If the personas already exist in `research/personas/`, also offer: "Or do you want to talk to your personas?" If they do, show the roster in one short table and go straight to step 10 (Talk to them). Read the files as they are now: the product manager may have edited them.

## Ground rules for personas

- **Evidence first.** No persona before the evidence map.
- **Every field is sourced:** `[documents/<file>]`, `[source: <url>]`, `[PM]` or `[assumed]`. Fewer than a third `[assumed]`; if you can't get there, say which gap causes it.
- **No personal data.** A persona may be modelled on a customer organisation, never named after a real person.
- **No flattery.** Real B2B customers are busy, sceptical and protective of budget. Each persona starts from "no" and needs a reason, from its own record, to say yes. A persona never calls an idea great without saying what it would replace and what it would cost them.
- **One persona, one agent.** When several personas answer the same thing, run each in its own subagent with only its own file and the material being judged, so they can't copy each other. Start the sceptic first. Without subagents, answer one persona at a time without showing later ones the earlier answers.
- **Stay specific:** numbers, systems, days of the week. No marketing voice.

## Steps

1. **What this is.** Say which product and which problem you're working on, then explain in two or three sentences, your own words:

   > Now we go deep on the people with this problem: how each of them experiences it, what they do today, and what options they have. Then we turn that into personas you can talk to, built from evidence, and uncover the agentic customer experiences that could solve the problem, in and around your product, so you can pressure-test them before taking real customers' time.

   Then ask: "Shall we start?" Wait for a yes.

2. **Your documents.** This is where the product manager's own material matters most. List what's already in `documents/`, then ask:

   > The more real material you give me, the more real your personas will be. Do you have any of these? Drag and drop them here, or put them in `[full path]/documents/`:
   > - interview notes or recordings' transcripts
   > - meeting and call transcripts (sales, onboarding, account reviews, QBRs)
   > - customer emails and support threads
   > - support tickets or a helpdesk export
   > - CRM exports: deals won and lost, with reasons
   > - survey or NPS answers, reviews you've collected
   > - churn notes and cancellation reasons
   > - usage data or analytics exports
   >
   > Any format works. Transcripts and emails usually contain names: I can make anonymised copies for you.

   Save anything dropped into the chat into `documents/`. Then check every file for personal data: people's names, email addresses, phone numbers. If you find any, list the files and offer two choices: they remove it themselves, or you write anonymised copies into `documents/anonymised/`, with each person replaced by their role ("the fleet manager", "the account's CFO"), and use only those. Never use or quote the originals. Ask them to delete the originals once the copies are made. If they have nothing, carry on: the personas will lean more on public research and their answers, and more fields will be `[assumed]`.

3. **Research, in the background.** Start these as parallel subagents, and tell the product manager in one line that research is running:
   - **In their words:** how each type of customer talks about the problem, from reviews (G2, Capterra, app stores), forums and communities (Reddit, LinkedIn, industry groups), trade press, and job postings for their roles (what they're responsible for and measured on).
   - **The options they have today:** doing nothing, spreadsheets and manual work, building their own, the product today, competitors' features, point tools, AI-native tools, outsourcing. For each: what it is, who uses it, what it costs, what it's good and bad at, with sources. Use `vision/market-map.md` and `vision/market-moves.md` as a start.
   - **The segments:** how many organisations are in the core segment and in the adjacent segments from `problem/framings.md`, who buys, and why it hurts there now.
   - **Your own evidence:** read every file in `documents/` (the anonymised copies where they exist) and group what you find by customer type: quotes, pains, workarounds, triggers (what made them act), objections, budget signals, churn reasons, each with its file and line. Fill `templates/evidence.md` into `evidence.md`.

   Without subagents, do them one at a time between questions.

4. **The product manager's view.** While research runs, go persona type by persona type (buyer, user, the person most likely to say no, and anyone in an adjacent segment). One question at a time:
   - How would they describe this problem, in their own words?
   - What do they do about it today? Tell me about the last time.
   - What have they tried, and why did they stop?
   - Who else is involved when it goes wrong?
   - What would worry them about a new way of doing it?

   Tag answers `[PM]`.

5. **The problem in the market.** When research is back, fill `templates/market.md` into `market.md`: each persona type in their own words, the problem through each persona's eyes (how they see it, how often, what it costs, what they do now, what they've tried, what would make them switch, what worries them), the options they have today and what no option does well, and the segments. Show the most surprising finding and the options table, short, and ask: "What's missing?"

6. **The ideal customer.** Ask: "Which account do you most want to win: the one with the most pain, the money to fix it, and a reason to choose you?" Fill `templates/icp.md` into `icp.md`. An ideal customer is an organisation; a persona is a person inside one.

7. **The personas.** Build the people inside that account with `references/persona-schema.md`, one file each in `personas/`:
   - the **buyer** (signs), with the buying-insight fields;
   - the **day-to-day user**;
   - the **sceptic**, the person most likely to say no;
   - one persona from an **adjacent segment** in `problem/framings.md`, if there is one worth winning.

   Every persona fills "the problem, through their eyes" from `market.md`, and ends with its evidence log: the rows from `evidence.md` and `market.md` it's built on, with sources. Show the roster as a table (name, role, segment, how they see the problem, would pay for, won't tolerate, share `[assumed]`).

8. **Reality check.** One persona at a time, ask the product manager: "Read [name]. What would they never say or do?" Apply the fixes, tagged `[PM]`. If `documents/` has a real interview or transcript, calibrate one persona: hold back one real question and answer, ask the persona the question in a subagent that can't see the answer, and compare facts, tone and objections. Score it 1 to 5 and fix the fields that differ.

9. **Agentic customer experiences.** Customers pay for the product twice: the licence, and the time their employees spend using it (entering data, checking, chasing, fixing, reporting). The second cost is usually far bigger and invisible, because it sits in payroll. Agentic experiences give employees that time back: agents do the work, sold as a separate line. The customer pays three things but less in total, and the product earns more. Work through it in four parts, one at a time:

   1. **How people use the product today.** Interview the product manager, persona by persona, one question at a time: "What does [persona] actually do in the product, step by step?", "How often, and how long does it take?", "How many people at a typical customer do this?", "What do they do outside the product to finish the job (spreadsheets, email, phone)?" Use `documents/`, `market.md` and the job map in `problem/framings.md` to prompt and check. List the human workflows: who, what, how often, how long, how many people.
   2. **The double cost.** For a typical customer (the ideal customer in `icp.md`), estimate the yearly licence and the yearly labour cost of using the product: people × hours a year on these workflows × loaded hourly cost. Use measured numbers where you can (prices, the product manager's figures, job-posting wage bands) and label assumptions, following the sizing rules in the ai-product-vision skill's `references/opportunities.md`. Show the working.
   3. **Agentify the workflows.** Draft three to five agentic customer experiences that take over the biggest human workflows, either agents inside today's workflows or a companion product next to it, from those workflows, `problem/framings.md` (the uncovered steps of the job), `market.md` (what no option does well), `vision/vision.md` (Imagine) and the personas. For each: the persona, the trigger, the outcome, each step today against each step with the agent, with the person's part (approves, reviews, handles the exception, or nothing); the data it needs and whether we hold it; what the agent decides alone and what it hands to a person; what could go wrong and how the person stays in control; the level today and with agents; the hours it gives back; and how we'd know it works. Walk the product manager through them one at a time and ask: "Is this how it should feel for [persona]? What's missing?"
   4. **The new economics.** For the typical customer, today against with agents: licence, agents (the new line, priced as a share of the labour saved, so the customer clearly wins), and the labour that remains. Show the customer's total today and with agents, their saving in money and percent, how many times lower the labour gets, and how our revenue per customer changes. For example: today 10K licence + 100K labour = 110K; with agents 10K licence + 10K agents + 20K labour = 40K, so labour falls 5x, the customer saves 70K (64%), and our revenue doubles. Ask: "Would your customers pay for agents at that price, for that saving?"

   Then ask which experience to explore first, and its thinnest version that still shows the whole experience end to end, small enough for developers to prototype. Fill `templates/experiences.md` into `experiences.md`. These are experiences to test, not features to build yet.

10. **Talk to them.** Now the personas pressure-test the problem. Offer these, and run what the product manager picks, one at a time:
   - **Interview a persona.** The product manager asks the Mom Test questions from `problem/problem.md`, and the persona answers in character from its record. Answer questions about the past with concrete detail; answer "would you use" or "would you pay" questions the way real customers do, politely and vaguely. After "end interview", step out and give the three questions that got the most useful answers, the one that got a polite non-answer, and one they should have asked. This rehearses the real interviews.
   - **Score the three framings.** Each persona, in its own subagent, rates the three framings in `problem/framings.md` on pain (1 to 5: how much it hurts them today, in their words) and pay (1 to 5: how likely their organisation pays to fix it, and through which budget), with one line in character. Show a table with the average and the spread, and call out where they disagree or where only the sceptic objects.
   - **React to the experiences.** Each persona, in its own subagent, sceptic first, walks through the experiences in `experiences.md` as themselves: where it helps, where they'd get stuck, what they'd never let an agent do, and the moment they'd stop. End with the three changes that would win over the most personas, and note what each persona said in `experiences.md`.
   - **Argue.** On the chosen problem or the experience to explore first: each persona states its view (sceptic first), then each answers the others once. End with what changed and the single best objection.

   - **Score a list.** Any list of problems or ideas (from `vision/opportunities.md`, or what they paste): each persona, in its own subagent, gives pain and pay 1 to 5 and one line in character, as for the framings.
   - **Vote on price.** For a concept as described, each persona, in its own subagent, answers the four Van Westendorp questions per year in their currency: too cheap to trust, a bargain, getting expensive but still possible, too expensive to consider; plus whether they'd buy at all (yes, no, not now), through which budget, and who signs. Show the four prices per persona, the acceptable range (highest "too cheap" to lowest "too expensive"), a suggested price between the median "bargain" and "getting expensive", the yes and no count, and the reason behind each no. Mark it **synthetic vote**.
   - **Calibrate a persona.** With a real question and answer from `documents/` the persona hasn't seen: ask it in a subagent that can't see the answer, compare facts, tone and objections, score 1 to 5, and propose the fields to fix.

   The product manager can run as many as they like, now or later.

   Write every conversation and result into `panel.md`, with the roster at the top. End every result with: *"Synthetic panel: hypotheses, not evidence. Confirm with a real customer."* If the panel changes the picture, offer to add a line to `problem/problem.md` under what to learn before building.

11. **Update the profile.** In `product.md`, under `## Customers`, add one line: the ideal customer and the personas, pointing to `research/`.

12. **The deck.** Update `index.html`, the product's deck: follow `references/deck.md` in the ai-product-start skill's folder (next to this skill's folder).

13. **Done.** Show the files you wrote and sum up in four lines: what surprised you about how customers see the problem, the option they use most today, the agentic experience to explore first, and what the panel said. Say they can talk to the personas any time by running `/ai-product-research` again.

## Done when

- the documents were asked for, and any personal data was removed or anonymised before use;
- `market.md` shows the problem in each persona's words, what they do today, and the options they have, with sources;
- `icp.md` and at least a buyer, a user and a sceptic in `personas/`, each with an evidence log, fewer than a third `[assumed]` or the gap named, and each read and corrected by the product manager;
- `experiences.md` has three to five agentic customer experiences, today against with agents, and the one to explore first;
- the panel has pressure-tested the problem or the experiences at least once, logged in `panel.md` as hypotheses, not evidence.

## Credits

Isolated per-persona agents, calibration against real answers, the per-persona evidence log and the panel modes follow ideas from persona-plugin (IrrealityLabs, MIT). Van Westendorp's price sensitivity meter is from Peter van Westendorp (1976). The persona record's grouping (background, psychology, capability, behaviour) follows MatrAIx's persona schema; no MatrAIx data is used. The buyer fields follow Adele Revella's Five Rings of Buying Insight.
