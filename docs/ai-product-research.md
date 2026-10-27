# ai-product-research

```
/ai-product-research
```

The fifth skill, after [`ai-product-problem`](ai-product-problem.md). Claude goes deep on the people who have your problem: how each type of customer experiences it, in their own words, what they do about it today, and what options they have. Then it turns that evidence into synthetic personas you can talk to, and uncovers the **agentic customer experiences** that could solve the problem: agents that do the customer's work end to end, in and around your product. The personas pressure-test the problem and the experiences before you take real customers' time.

**This is where your own documents matter most.** Interview notes, meeting transcripts, customer emails, tickets and CRM exports make the personas real. Without them, the personas lean on public research and your answers.

**Who runs it:** the product manager, ideally with people who talk to customers: support, sales, customer success.
**Run it:** in the folder that holds your product's folder.
**You leave with:** how each persona sees the problem and what they do today, the options customers have, your ideal customer, a panel of personas you can talk to, and three to five agentic customer experiences, with the one to explore first.

## Before you begin

- **Your problem.** Run [`/ai-product-problem`](ai-product-problem.md) first. It doesn't have to be finished: this skill needs `product.md` and anything saved in `problem/`.
- **The same folder.** In the Claude desktop app, pick the folder that holds your product's folder with **Project or folder**. In Claude Code, start Claude there.
- **Your documents.** Gather what you have. See [Documents](#documents).

## Documents

Claude asks for these early. Drag and drop them into the chat, or put them in your product's `documents/` folder. Any format works.

- interview notes, or transcripts of recorded interviews
- meeting and call transcripts: sales calls, onboarding, account reviews
- customer emails and support threads
- support tickets, or a helpdesk export
- CRM exports: deals won and lost, with reasons
- survey or NPS answers, and reviews you've collected
- churn notes and cancellation reasons
- usage data or analytics exports

**Names and contact details.** Transcripts and emails usually contain people's names, email addresses and phone numbers. Claude checks every file. If it finds any, you can remove them yourself, or Claude makes anonymised copies in `documents/anonymised/`, with each person replaced by their role ("the fleet manager"), and uses only those. Delete the originals once the copies are made.

## What happens

Claude asks one question at a time, like a conversation.

1. **What this is.** Claude names your product and problem, explains the session in a few sentences, and asks: "Shall we start?"

2. **Your documents.** Claude lists what's already in `documents/`, asks for more, and checks everything for personal data.

3. **Research.** In the background, Claude researches:
   - **in their words:** how each type of customer talks about the problem, from reviews, forums, communities, trade press and job postings;
   - **the options they have today:** doing nothing, spreadsheets, building their own, your product, competitors, point tools, AI-native tools, outsourcing, with what each costs and is good and bad at;
   - **the segments:** how many organisations, who buys, and why it hurts now, including the adjacent segments from the problem skill;
   - **your own evidence:** quotes, workarounds, triggers, objections, budget signals and churn reasons from your documents, by customer type.

4. **Your view.** While research runs, Claude asks you about each type of customer: how they'd describe the problem, what they did the last time it hit, what they've tried, who else is involved, and what would worry them about a new way.

5. **The problem in the market.** Claude shows the problem through each persona's eyes and the options they have today, including what no option does well, and asks what's missing.

6. **The ideal customer.** The account you most want to win: the most pain, the money to fix it, and a reason to choose you.

7. **The personas.** The **buyer**, the **day-to-day user**, the **sceptic** (the person most likely to say no), and one from an **adjacent segment** if it's worth winning. Every field says where it came from, each persona has an evidence log, and no more than a third is assumed.

8. **Reality check.** You read each persona and say what they'd never say or do; Claude fixes it. If you have a real interview, Claude **calibrates** one persona: it asks the persona a real question it hasn't seen and compares the answer with the real one.

9. **Agentic customer experiences.** Your customers pay for your product twice: the licence, and the time their people spend *using* it (entering data, checking, chasing, fixing, reporting). That second cost is usually far bigger, and invisible because it sits in payroll. Agentic experiences give people that time back: agents do the work, and you sell them as a separate line. Claude works through it with you, one part at a time:
   - **How people use your product today:** Claude interviews you, persona by persona: what they do in the product step by step, how often, how long, how many people, and what they do outside it to finish the job.
   - **The double cost:** for a typical customer, the yearly licence and the yearly cost of people's time using the product, with the working shown.
   - **Agentify the work:** three to five experiences where agents take over the biggest workflows, inside the product or in a companion product next to it. Each shows the steps today against the steps with the agent, what the person still does (approves, reviews, handles exceptions), the data it needs, how the person stays in control, the AI level, and the hours it gives back.
   - **The new economics:** today against with agents, for a typical customer. Agents are priced as a share of the labour they save, so the customer clearly wins.

   | | Today | With agents |
   |---|---|---|
   | Licence | 10K | 10K |
   | Agents (new) | – | 10K |
   | People's time using the product | 100K | 20K |
   | **Total for the customer** | **110K** | **40K** |

   In this example, labour falls 5x, the customer saves 70K a year (64%), and your revenue per customer doubles. Claude builds the same picture from your product's real numbers.

   You pick the experience to explore first, and its thinnest version that still shows the whole experience end to end. These are experiences to test, not features to build yet.

10. **Talk to them.** The personas pressure-test your problem and the experiences. Pick one or more:
   - **interview a persona** with the questions from the problem skill, as a rehearsal for real interviews;
   - **score the three framings** of your problem on pain and willingness to pay, each persona on its own;
   - **react to the experiences:** each persona walks through them as themselves: where it helps, where they'd get stuck, what they'd never let an agent do;
   - **argue** the problem or the experience to explore first, sceptic first, to find the single best objection.

11. **The deck.** Claude adds your personas, the options customers have today, the agentic experiences, the new economics and the panel's verdict to `index.html`.

12. **Done.** Claude adds the ideal customer and the personas to `product.md`, and sums up what surprised you, the option customers use most today, the experience to explore first, and what the panel said.

**Synthetic personas generate hypotheses, not evidence.** A real customer's yes is evidence; a persona's yes is not. Everything the panel says is marked that way.

## What you get

```
acme-scheduler/
  documents/
    anonymised/      anonymised copies of files with names in them, if you asked for them
  research/
    market.md        how each persona sees the problem, and the options they have today
    evidence.md      your own evidence, by customer type
    icp.md           the account you most want to win
    personas/        one file per persona, with its evidence log
    experiences.md   how people use the product today, the double cost, agentic experiences, the new economics, and the one to explore first
    panel.md         every conversation with the panel, and what it said
```

Each persona file holds:

| Section | What's in it |
|---|---|
| Background | Organisation, role, what they run on |
| Business | Who signs, budget route, what they're measured on |
| The problem, through their eyes | The problem in their words, how often it hits, what they do today, what they've tried, what would make them switch, what worries them |
| Psychology | Attitude to change, trust in AI, what burned them before, what they won't tolerate, what they'd pay for |
| Capability | Tech comfort, the data they hold, the time they can give a new tool |
| Behaviour | A normal day, workarounds, the last time it went wrong, how they buy |
| Buying insight | For the buyer: why they'd invest now, what success looks like, barriers, how they decide |
| Voice | How they sound, in one sentence |
| Evidence log | The evidence the persona is built on, with sources |

## Talking to your personas later

Run `/ai-product-research` again any time. If your personas exist, Claude asks whether you want to continue the research or talk to your personas, and you can use any of these:

| Mode | What happens | Good for |
|---|---|---|
| **Interview one persona** | You ask questions; the persona answers in character from its record, until you say "end interview". Then Claude steps out and tells you which questions worked, which got a polite non-answer, and one you should have asked. | Rehearsing customer interviews |
| **Score a list** | Each persona rates every problem or idea on **pain** (1–5) and **pay** (1–5, and through which budget), with one line in character. You get the average, the spread, and where they disagree. | Choosing between problems or ideas |
| **Argue** | Each persona states its view, the sceptic first, then answers the others once. You get what changed and the single best objection. | Finding the weak spot |
| **React to a concept or prototype** | Each persona walks through it as themselves: the first thing they'd try, where they'd get stuck, what's missing for their job, the moment they'd stop. You get the three changes that would win over the most personas. | Testing a concept before building it |
| **Vote on price** | Each persona answers the four Van Westendorp questions (too cheap to trust, a bargain, getting expensive, too expensive), plus whether they'd buy and who signs. You get the acceptable range and a suggested price. | A first view on pricing |
| **Calibrate a persona** | Claude asks a persona a real question from one of your interviews that it hasn't seen, and compares the answer with the real one. | Checking a persona is realistic |

Each persona answers in its own separate agent, so they can't copy each other. Every conversation is added to `research/panel.md`, marked as hypotheses, not evidence.

## Troubleshooting

- **Claude asks you to run another skill first.** Research needs `product.md` and something from the problem skill.
- **You have no documents.** Carry on. The personas will lean on public research and your answers, more fields will be marked assumed, and Claude will tell you which gaps to fill.
- **A persona doesn't sound real.** Say what's wrong ("she'd never call it that"). Claude fixes it and marks the change.
- **The panel agrees with everything.** It shouldn't: personas start from "no". Ask the sceptic directly, or run "argue".
- **You ran out of time.** Say so. Claude saves what's done and marks the rest "Not done yet". Run `/ai-product-research` again later to finish.

## Credits

The persona panel follows ideas from persona-plugin (IrrealityLabs, MIT licence): one agent per persona, calibration against real answers, an evidence log per persona, and the panel modes. The price vote is Peter van Westendorp's price sensitivity meter (1976). The persona record's grouping follows MatrAIx's persona schema; the buyer fields follow Adele Revella's Five Rings of Buying Insight.
