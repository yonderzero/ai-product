---
name: ai-product-flows
description: Sixth step, after ai-product-research. Uncovers the right flows for the agentic customer experiences - step by step, what the agent does and what the person sees, approves or never lets go - by interviewing real customers (with an interview kit, and their transcripts or notes) and the synthetic panel side by side, with clickable mockups of the flows, ranking flows on value, trust, pay and hours given back, and choosing the flows to take forward. Writes flows/ (flows.md, mockups/, panel-tests.md, script.md).
---

# ai-product-flows

Which flows are the right ones? Take the agentic customer experiences from research, map each as a flow (what the agent does, what the person sees and decides, what happens when it goes wrong), make them clickable, and test them with real customers and the synthetic panel until the right flows are clear. Flows, not features yet: features come in the next skill.

**Real customers outweigh the panel.** The panel covers who you can't reach yet and stress-tests reactions before you take customers' time. Every panel result is marked: *"Synthetic panel: hypotheses, not evidence. Confirm with a real customer."*

## How to talk

Conversational, short messages, one question at a time. Never send a list of questions. Don't explain what you're about to do; just do it. While subagents run, keep talking with the product manager.

## Save as you go

Write each file as soon as its step has content, and update it as you go. Mark any section you haven't reached `Not done yet`. After every step that saves something, update `index.html`, the product's deck (follow `references/deck.md` in the ai-product-start skill's folder), so the deck always shows the latest. If the product manager says they're out of time or wants to move on, stop cleanly: save what's there, say which steps are left, and that they can run this skill again to continue, or edit the files themselves. Update `index.html` before you stop. Moving on is fine as long as something is saved.

## Before you start

Work in the product folder: the current folder, or the folder below it that has `product.md`. This skill's files go in `flows/` inside it: `flows.md`, `panel-tests.md`, `script.md` and `mockups/` mean `flows/<name>`. The other skills' files are in `vision/`, `discovery/`, `problem/` and `research/`. `product.md` and `documents/` stay at the top. Create `flows/` if it doesn't exist.

- No `product.md`, or it's empty: say in one line that the product profile comes first, ask them to run `/ai-product-start`, and stop.
- No `research/experiences.md` and no personas in `research/personas/`: say in one line that this builds on the research step, ask them to run `/ai-product-research`, and stop. Anything saved there is enough to go on.

Read `product.md`, `problem/problem.md`, everything in `research/` (above all `experiences.md`), and `vision/vision.md` where it exists, and anything in `documents/` you haven't read yet. Follow the ground rules for personas in the ai-product-research skill's `SKILL.md` (next to this skill's folder): one persona per agent, sceptic first, no flattery, stay specific.

If files from an earlier run exist, say which steps are done and which aren't (look for `Not done yet`), and ask whether to continue, redo a step, or start again. If new interview notes or transcripts are in `documents/` since last time, offer to go straight to step 7.

## Steps

1. **What this is.** Say which product you're working on, then explain in two or three sentences, your own words:

   > Now we find the right flows. We take your agentic customer experiences and map each as a flow: what the agent does, what people see and decide, and what happens when it goes wrong. Then we make them clickable and test them with real customers and your synthetic panel, so you know which flows to take forward.

   Then ask: "Shall we start?" Wait for a yes.

2. **The flows.** Take the experiences in `research/experiences.md`, starting with the one to explore first. For each, walk the product manager through it one moment at a time and map the flow:
   - **the main path:** each moment, what the agent does, what the person does (nothing, reviews, approves, decides), and what they see (the screen, the message, the notification);
   - **when it goes wrong:** missing data, low confidence, a customer complaint, a rule broken; what the agent does (stops and asks, flags, retries) and what the person does;
   - **what the agent does alone, what the person always approves, and what the agent never does;**
   - **the data it needs.**

   Ask at each moment: "What would [persona] need to see here to trust it?" Fill `templates/flows.md` into `flows.md`, leaving the scores for later.

3. **The mockups.** Ask once whether they can share a screenshot of the product, or its colours and logo, so the mockups feel like theirs. Then build one clickable HTML mockup per flow in `mockups/`, walking through its key moments in order: the trigger, what the agent did, the moment the person reviews or approves, and an exception being handled. Each is one self-contained HTML file (inline CSS and JavaScript, no external services) with realistic data from the personas and the product, "Next" and "Back" between moments, and a small "Mockup for testing" label. Open the first one in the preview. These are mockups to test flows, not the product.

4. **The interview kit.** Fill `templates/script.md` into `script.md`: questions about the past from the riskiest assumptions in `problem/problem.md` (Mom Test, see the ai-product-problem skill's `references/methods.md`), then each flow's mockup one moment at a time, then a real commitment. Ask: "Which real customers can you talk to today or this week?" Encourage it: real interviews are the strongest evidence for which flows matter.

5. **Interview the panel.** Each persona, in its own subagent, sceptic first, walks through each flow's mockup as themselves and says: the first thing they'd do, where they'd get stuck, what they'd let the agent do alone, what they'd never let it do, what's missing for their job, and the moment they'd stop. Each scores every flow 1 to 5 on **value** (does it give their time back?), **trust** (would they let the agent do it?) and **pay** (would their organisation pay for it, and through which budget?). Record the round in `panel-tests.md` from `templates/panel-tests.md`, with the average, the spread, where they disagree, and the three changes that would win over the most personas.

6. **Iterate.** Show the three changes and ask which to make. Update the flows and the mockups, then run a second round with the panel on what changed. Log what changed and why in `flows.md`.

7. **Real customers.** When the product manager has real interviews, as transcripts or notes in `documents/` or pasted into the chat (check for personal data first, as in the research skill), summarise each: who (role, no names), what they said about the problem in the past, their reaction to each flow, what they'd let an agent do, what's missing, and any commitment. Add them to the real-customers table in `panel-tests.md`, and say where real customers agree or disagree with the panel. If there are none yet, say plainly that the ranking rests on the panel and the earlier evidence, and keep `script.md` ready.

8. **The right flows.** Rank the flows in `flows.md` on value, trust, pay and hours given back, with real-customer evidence outweighing the panel: a flow real customers rejected drops, whatever the panel said. Mark which flows to take forward, which later, and which not, and the thinnest version of each flow taken forward that still shows the whole experience end to end. Show the ranking and ask: "Are these the right flows to take forward?"

9. **The deck.** Update `index.html`, the product's deck: follow `references/deck.md` in the ai-product-start skill's folder (next to this skill's folder).

10. **Done.** Show the files you wrote and sum up in three lines: the flow customers valued most, the flows to take forward, and the next real interview to do. Say the next step is `/ai-product-roadmap`.

## Done when

- `flows.md` maps each experience's flow (main path, when it goes wrong, what the agent never does), ranked on value, trust, pay and hours given back, with the flows to take forward and their thinnest versions;
- one clickable mockup per flow in `mockups/`, revised at least once after the panel;
- `panel-tests.md` has at least one panel round, and any real interviews, with where they agree and disagree;
- `script.md` is ready for real customers;
- nothing here is a feature list or a build plan yet.
