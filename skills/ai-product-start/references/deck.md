# index.html: the product's deck

`index.html` sits at the top of the product folder, next to `product.md`. It's the main file to open: a slide deck that grows with each skill: the product, the customers, the six levels, the opportunities, Imagine, the vision, where to take the product, the four pillars, the move, where value flows, and readiness. Every slide links to the files it comes from. Slides a skill hasn't reached yet say "Not done yet" and name the skill to run.

The files are the source of truth. The deck only shows them.

## When to update it

At the end of every ai-product skill, and whenever a skill stops early because the product manager is out of time.

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
  "move": "Build on it",
  "move_why": "one or two lines",
  "direction": { "protect": "", "grow": ["one to three bets"], "build_first": "", "dont": "", "signals": ["two or three"] },
  "value_flows": [ { "flow": "Who gets value", "today": "", "tomorrow": "" } ],
  "value_shift": "most of the value goes to … today → … tomorrow",
  "readiness": [ { "area": "Data", "gap": "", "must_be_true": "" } ]
}
```

- `pillars`: the composites from the scripts, as numbers.
- `move`: exactly one of Build on it, Move first, Optimise, Defend.
- `value_flows`: the rows of the value-flow table in `discovery.md`.
- `complete`: true only when `discovery.md` is agreed.
