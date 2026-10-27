# index.html: the product's deck

`index.html` sits at the top of the product folder, next to `product.md`. It's the main file to open: a slide deck that grows with each skill: the product, the customers, the six levels, the opportunities, Imagine, the vision, where to take the product, the four pillars, the move, where value flows, readiness, the BHAG, the right problem, three framings, and what to learn first. A sidebar lists every section, grouped into Start, Vision, Discovery, Problem, Research, Flows and Roadmap, with a dot for done or not done, so the product manager can jump anywhere. Every section links to the files it comes from. Slides a skill hasn't reached yet say "Not done yet" and name the skill to run.

The files are the source of truth. The deck only shows them.

## When to update it

Continuously. After **every step** of every ai-product skill that saves or changes a file the deck shows, update the matching part of the JSON, so the deck always shows the latest. Do it quietly, without stopping the conversation; mention it in one line only when a new slide fills in for the first time. Always update it before a skill stops, including when the product manager is out of time, and at the end of every skill.

If `index.html` was made from an older template (it lacks a slide this JSON has data for), copy the current `templates/index.html` and move the JSON block across, so every slide shows.

## How

1. If `index.html` doesn't exist in the product folder, copy `templates/index.html` from the ai-product-start skill's folder into the product folder.
2. Replace only the JSON inside `<script type="application/json" id="data">`. Don't change anything else in the file.
3. Fill the JSON only from the product folder's files. Keep every text short: one or two sentences, in plain language. Leave out what isn't in the files yet.
4. Show it:
   - in Claude Desktop, open `index.html` in the preview so the product manager sees it next to the chat;
   - otherwise, tell them to open `index.html` in a browser.
   Say in one line what's new on it.
5. If they want a link to share and you can publish Artifacts, publish `index.html` as an Artifact, private until they share it, and save the link in `product.md` as `- overview: <link>`. Next time, update that same Artifact instead of making a new one. The links to local files won't open from a shared link; say so.

## The data

```json
{
  "updated": "27 Oct 2026",
  "product": {
    "name": "", "company": "", "industry": "", "website": "",
    "what": "two sentences from product.md: what it does and for whom",
    "personas": [
      { "name": "Head of Scheduling", "who": "role, organisation, buyer or user", "problems": ["up to three problems the product solves for them"] }
    ]
  },
  "vision": null,
  "discovery": null
}
```

After `/ai-product-vision`, set `vision` (from `vision/`). Fill what exists; leave out the rest:

```json
{
  "complete": false,
  "level_today": 2, "level_target": 4, "target_when": "2028",
  "market": [ { "name": "Our product", "level": 2, "us": true }, { "name": "Competitor", "level": 3 } ],
  "opportunities": [ { "title": "", "kind": "Grow the base", "level": 4, "priority": 3.95, "band": "Do first" } ],
  "imagine": [ { "level": 5, "sketch": "three or four lines: our product at this level", "already_there": "Harvey, OpenEvidence" } ],
  "day": "the day with our System of Understanding, five or six sentences",
  "statement": "the vision, two or three sentences",
  "first_step": ""
}
```

- `complete`: true only when `vision.md` is agreed.
- `market`: every placed company, with the product as `"us": true`.
- `opportunities`: the top six, in rank order.

After `/ai-product-discovery`, set `discovery` (from `discovery/`):

```json
{
  "complete": false,
  "in_short": "the In short from discovery.md",
  "pillars": { "protection": 3.1, "strength": 3.4, "ai_opportunity": 3.6, "exposure": 2.7 },
  "urgency": "high: competitors ship AI in the same workflows this year",
  "move": "Build on it",
  "move_why": "one or two lines",
  "direction": { "protect": "", "grow": ["one to three bets"], "start_with": "the first customer problem to go after", "dont": "", "signals": ["two or three"] },
  "value_flows": [ { "flow": "Who gets value", "today": "", "tomorrow": "" } ],
  "value_shift": "most of the value goes to … today → … tomorrow",
  "readiness": [ { "area": "Data", "gap": "", "must_be_true": "" } ]
}
```

- `pillars`: the four numbers from `compute_pillars.py`, as numbers.
- `urgency`: the AI urgency from `compute_pillars.py` in plain words, with one line on why.
- `move`: exactly one of Build on it, Move first, Optimise, Defend.
- `value_flows`: the rows of the value-flow table in `discovery.md`.
- `complete`: true only when `discovery.md` is agreed.

After `/ai-product-problem`, set `problem` (from `problem/`):

```json
{
  "complete": false,
  "bhag": "one bold, measurable, dated goal",
  "bhag_why": "one line",
  "statement": "When …, [persona] wants to …, so they can …",
  "framing": "The bigger job",
  "levels": "1 → 4",
  "evidence": "Good",
  "switching": "one line from the four forces",
  "framings": [ { "name": "As stated", "level": 2, "problem": "", "size": "", "chosen": false } ],
  "opportunity": "two or three lines: existing customers, new customers, size",
  "learn": [ { "assumption": "", "ask": "Tell me about the last time…" } ]
}
```

- `framings`: as stated, the bigger job, the moonshot, with `chosen` true on the one picked.
- `learn`: the riskiest assumptions, most dangerous first.
- `complete`: true only when `problem.md` is agreed.

After `/ai-product-research`, set `research` (from `research/`); talking to the personas again updates `panel` and `objection`:

```json
{
  "complete": false,
  "icp": "one line: the account we most want to win",
  "personas": [ { "name": "Dana", "role": "Buyer", "sees": "the problem in their words", "today": "what they do now", "wont": "won't tolerate" } ],
  "options": [ { "option": "Spreadsheets", "who": "", "good": "", "bad": "" } ],
  "gap": "what no option does well today",
  "economics": { "currency": "$", "today": { "licence": 10000, "labour": 100000 }, "agents": { "licence": 10000, "agents": 10000, "labour": 20000 }, "labour_x": 5, "revenue_x": 2, "note": "for a typical customer; working in experiences.md" },
  "experiences": [ { "name": "", "persona": "", "levels": "1 → 4", "today": "one line", "agent": "one line", "hours": "120 h a year per person", "first": false,
      "today_steps": ["three to six short steps a person does today"],
      "agent_steps": [ { "text": "short step", "by": "agent" }, { "text": "approves", "by": "check" } ] } ],
  "panel": "two or three lines: what the panel said about the problem",
  "objection": "the single best objection"
}
```

- `economics`: the new economics for a typical customer from `experiences.md`, as numbers per year.
- `experiences`: the agentic customer experiences, with `first` true on the one to explore first. `today_steps` and `agent_steps` draw the today-against-with-agents strips; `by` is agent, person, or check (a person approves). Keep each step to a few words.
- `complete`: true when the personas are checked and the panel has run once.

After `/ai-product-flows`, set `flows` (from `flows/`):

```json
{
  "complete": false,
  "flows": [ { "name": "", "persona": "", "value": 4.2, "trust": 3.5, "pay": 3.8, "hours": "120 h/yr", "forward": "yes",
      "trigger": "a new fault code arrives", "outcome": "the truck is booked in with parts ready",
      "steps": [ { "moment": "Detect", "agent": "reads the fault code", "person": "" }, { "moment": "Approve", "agent": "", "person": "approves the work order" } ],
      "wrong": "one line", "never": "one line" } ],
  "thinnest": "one line: the thinnest version of the flow to take forward",
  "mockups": [ { "name": "Morning review", "file": "flows/mockups/morning-review.html", "what": "one line" } ],
  "customers": "two or three lines from real interviews, or empty",
  "panel": "two or three lines from the panel",
  "never": "what the agent never does"
}
```

- `flows`: ranked, real customers outweighing the panel; `forward` is yes, later or no. Flows with `steps` get their own flow-map slide: one column per moment, an agent lane and a person lane, a few words per cell; set `exception` true on a step that shows what happens when it goes wrong.
- `complete`: true when the flows to take forward are agreed.

After `/ai-product-roadmap`, set `roadmap` (from `roadmap/`):

```json
{
  "complete": false,
  "summary": "this product update in one or two lines",
  "update": [ { "name": "", "flow": "", "priority": 6.4 } ],
  "slice": "the build-day slice in two lines: the flow, what's in, when it's done",
  "customer_saves": "$82K (50%)",
  "customer_return": "every $1 on agents saves $4",
  "revenue_per_customer": "+$19K a year",
  "revenue_total": "$2.7M a year",
  "price": "per vehicle per month for agents, $X",
  "price_why": "one line",
  "horizons": {
    "now": { "outcome": "", "items": ["features in this update"], "level": 2, "revenue": "" },
    "next": { "outcome": "", "items": [], "level": 3, "revenue": "" },
    "later": { "outcome": "", "items": [], "level": 4, "revenue": "" }
  }
}
```

- `update`: the features in Now, in priority order.
- `complete`: true when the roadmap and this product update are agreed.
