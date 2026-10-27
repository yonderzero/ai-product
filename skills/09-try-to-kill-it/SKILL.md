---
name: 09-try-to-kill-it
description: Product Track session 09 workshop (Challenge the Shortlist). The synthetic panel walks the prototype and votes on price, the team runs a pre-mortem, the most important change goes into the spec and prototype for the developers already building, and the team makes its roadmap call. Writes 09-challenge.md and updates handoff/.
---

# 09 · Try to kill it

**Goal.** Find what breaks before Friday does. Every change goes to the developers straight away; they're already building.

Work in the team's product folder: the current folder, or the folder below it that has `product.md`. If there is none, run `/ai-product:start` first. Remind the team they can add files to `documents/` at any time, and read any new ones. Read `handoff/` and `panel/`.

## Steps

1. **React.** Run `synthetic-customers` mode 7 (react) on `handoff/prototype/`, one subagent per persona, sceptic first. If the team booked a real customer, ask them to show the prototype now and write down what the customer says, word for word, in the "Real customer" row.

2. **Vote.** Run mode 8 (Van Westendorp) on `handoff/proposal.md`. Mark it as a synthetic vote.

3. **Pre-mortem.** Ask the team: "It's six months later and this failed. Why?" Collect three reasons and one change for each. Offer these if they're stuck: we solved the wrong problem; customers wouldn't pay; it was badly scoped; it couldn't compete with what's already out there; the data was wrong and nobody noticed.

4. **Change it.** With the team, pick the one change that matters most. Make it in `handoff/product-spec.md` and `handoff/prototype/`, and list what changed under **Changes** at the top of the spec. Tell the team to walk over and tell their developers, not just edit the file.

5. **The roadmap call.** Fill `templates/09-challenge.md` into `09-challenge.md`, ending with the team's call: we're in (a sponsor, a budget, a date), we're in, if (one condition, an owner, a deadline), or not now (with the reason).

## Done when

- [ ] reactions and the vote recorded, marked synthetic (plus a real customer if there was one)
- [ ] a pre-mortem with three reasons
- [ ] one change made in the spec and prototype and told to the developers
- [ ] the roadmap call

Finish with the checklist and: "Next session: `/ai-product:10-demo-story`."
