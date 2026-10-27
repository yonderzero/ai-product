---
name: align-product-spec
description: Product Track, Align session (Wednesday, with the developers). Turn the proposal and prototype into the product half of the developers' spec - overview, goals, non-goals, users, user stories with acceptance criteria, main flow, data, agent permissions, metrics, risks - leaving the technical design to the developers. Writes handoff/product-spec.md.
---

# Align · The product spec

**Goal.** The product half of the spec the developers build from, written with them in the room. The technical design is theirs.

Work in the team's product folder. Read `handoff/proposal.md`, `handoff/problem.md` and `handoff/prototype/`.

## Steps

1. Fill `templates/product-spec.md` into `handoff/product-spec.md`:
   - the overview, goals and non-goals from the proposal;
   - users from `panel/` and the proposal's stakeholders;
   - user stories with acceptance criteria, one per step of the prototype's main flow;
   - the main flow, marking where the agent acts and where the user approves;
   - data: what the feature reads and writes, where it lives today, and what sample data the demo can use;
   - what the agent may do, must ask first, and must never do;
   - the outcome number as the success metric;
   - risks with mitigations.
2. Leave the **Technical design** section for the developers. Don't fill it in.
3. Walk the developers through it. Write every question they ask that the spec doesn't answer under a new **Open questions** heading, with who answers it.

If the developers use their own spec template, match their headings instead and keep the same content.

## Done when

- [ ] every step of the prototype's main flow has a user story with acceptance criteria
- [ ] data, agent permissions and the success metric are written down
- [ ] a developer has said "I could start from this"

Finish with the checklist and: "Next session: `/ai-product:09-try-to-kill-it`."
