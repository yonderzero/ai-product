# ai-product

The AI era gives you, as a product manager, a chance to re-imagine your product and grow the business.

ai-product is a plugin for Claude that helps you do just that. It helps you re-imagine your product for the AI era and innovate in and around it: bringing new value to your existing customers, winning new ones, and growing organically.

Claude works alongside you, step by step. It gets to know your product, your customers and the problems you solve for them; maps your market; helps you set your product's AI vision; and turns it into requirements your developers can build from.

## Install

In the Claude desktop app:

1. Open **Customize** and go to **Plugins**.
2. Click **Add**, choose **Add marketplace**, then **Add from a repository**.
3. Enter `yonderzero/ai-product` and add it.
4. Find **ai-product** in the list and click **Install**.

Plugins need a paid Claude plan (Pro, Max, Team or Enterprise).

## Get started

1. Start a new conversation and choose a folder on your computer with **Project or folder**, under the message box. Claude will create your product's folder inside it.
2. Type `/ai-product-start` and send.

<details>
<summary>Using Claude Code in the terminal instead</summary>

```
/plugin marketplace add yonderzero/ai-product
/plugin install ai-product@ai-product
```

Restart Claude Code in the folder you want to work in, then run `/ai-product-start`.

</details>

## How it works

You run the skills in order, in one folder:

1. **`/ai-product-start`**: set up your product's folder, build its profile, describe your customers.
2. **`/ai-product-vision`**: place your product and your market on six levels of AI, rank the opportunities, imagine the future, and agree a vision.
3. **`/ai-product-discovery`**: check whether your product is ready for that vision: what protects it, how strong it is, the AI opportunity, what could go wrong, what has to be true, where value flows, and where to take the product.
4. **`/ai-product-problem`**: make sure you're solving the right problem: say it as a customer job, test the evidence, set a BHAG, think bigger, and choose the framing that captures the most value.

Each skill is a conversation. Claude asks one question at a time, researches the web in the background, and writes what you build together into files in your product's folder. Each skill reads what the earlier ones wrote, so run them in the same place.

After each skill, Claude updates **`index.html`**: a slide deck of everything so far, from the product and its customers to the vision and your move. In Claude Desktop it opens in the preview next to the chat. A sidebar lets you jump to any section, every section links to the files it comes from, and slides you haven't reached yet say which skill fills them.

You don't have to finish a skill before moving on. Claude saves as you go and marks what's not done yet. As long as something is saved, you can go on to the next skill, and come back to any skill later to finish it, redo a step or update it. You can also edit the files yourself; the next skill reads your edits.

```
acme-scheduler/          named after your product
  index.html             a slide deck of everything so far, updated by every skill
  product.md             your product's profile, from /ai-product-start
  documents/             your files: Claude reads everything here
  vision/                from /ai-product-vision
    ai-levels.md
    market-map.md
    market-map.html
    market-moves.md
    opportunities.md
    vision.md
  discovery/             from /ai-product-discovery
    protection.md
    strength.md
    exposure.md
    value.md
    discovery.md
  problem/               from /ai-product-problem
    evidence.md
    framings.md
    problem.md
```

Every fact in the files says where it came from: a link for anything found on the web, `[documents/<file>]` for anything from your files, and `[PM]` for anything you said. Claude leaves a gap rather than guess, and lists what's still unknown.

## Skills

**[`/ai-product-start`](docs/ai-product-start.md)**\
Sets up a folder for your product, builds a first profile from its website and your documents, and interviews you about the product and each type of customer.

You get:
- **`product.md`**: your product's profile: what it does, your customers as personas and the problems you solve for each, workflows, pricing, competitors, data and tech, and AI today. *([example](examples/salesforce/product.md))*
- **`documents/`**: a folder for your files, such as customer interviews, tickets, sales notes and specs. Every skill reads it.

**[`/ai-product-vision`](docs/ai-product-vision.md)**\
Maps your market on six levels of AI, from System of Record to System of Understanding, finds the opportunities, and creates a vision for where you could take your product.

You get:
- **`ai-levels.md`**: the value your product gives customers at each level: features, for whom, and how they pay. *([example](examples/salesforce/vision/ai-levels.md))*
- **`market-map.md`** and **`market-map.html`**: your market on the six levels, with sources, and the openings. Open the `.html` in a browser to see it as a picture. *([example](examples/salesforce/vision/market-map.md))*
- **`market-moves.md`**: who's moving in your market, and what it opens up for you. *([example](examples/salesforce/vision/market-moves.md))*
- **`opportunities.md`**: your customers' work step by step, and the opportunities in and around your product, rated and ranked. *([example](examples/salesforce/vision/opportunities.md))*
- **`vision.md`**: your product's AI vision: your product imagined at each higher level, a day with your System of Understanding, the vision you agreed, and the first step. *([example](examples/salesforce/vision/vision.md))*

**[`/ai-product-discovery`](docs/ai-product-discovery.md)**\
Checks whether your product is ready for its vision and sets a clear direction. Scores four pillars with evidence and your inside knowledge, tests what has to be true for the vision, maps where value flows, and ends with where to take the product: what to protect, where to grow, which problem to start with.

You get:
- **`protection.md`**: what protects your product: switching costs, domain knowledge, speed and cost of building, and distribution, scored with sources. *([example](examples/salesforce/discovery/protection.md))*
- **`strength.md`**: how strong the product and its customers are, and how big the AI opportunity is, scored with sources. *([example](examples/salesforce/discovery/strength.md))*
- **`exposure.md`**: 11 risks, from AI disruption to ageing tech, scored with sources. *([example](examples/salesforce/discovery/exposure.md))*
- **`value.md`**: where value flows today, where it leaks, where it would flow at your vision's target level, who else could capture it, and how you'd charge. *([example](examples/salesforce/discovery/value.md))*
- **`discovery.md`**: the one page: where to take the product, the four pillars, whether you're ready for the vision (data, tech, team, customers, pricing), your move, and where value flows. *([example](examples/salesforce/discovery/discovery.md))*

Each skill's files go in a folder named after it inside your product's folder (`vision/`, `discovery/`, `problem/`), as plain text you can open, edit and share.

**[`/ai-product-problem`](docs/ai-product-problem.md)**\
Makes sure you're solving the right problem, and that it's big enough. Says it as a customer job, grades the evidence with the Mom Test, pressure-tests it, sets a BHAG, looks at what customers most want fixed and at adjacent segments, and lays out three framings so you pick the one that captures the most value.

You get:
- **`evidence.md`**: everything that backs the problem, graded by what customers did, not what they said.
- **`framings.md`**: the job, the pressure test, the BHAG, the job map, the biggest pains, adjacent segments, and three framings, each sized.
- **`problem.md`**: the right problem, the opportunity it captures, what success looks like, and what you need to learn from customers before building.

## Example

See what you get, using Salesforce as the product: [the Salesforce example](examples/salesforce/). It's illustrative, built from public sources, and not affiliated with Salesforce.

## The six levels of AI

Software is moving from recording the work to doing it. ai-product looks at your product, your market and your future on six levels.

**1 · System of Record**: people do the work; the software stores it.\
The record is the value: data, forms, workflows and reports for one customer. Paid per seat, licence or module. *Examples: Epic, SAP, Procore.*

**2 · AI Assisted**: people do the work; AI suggests.\
Suggestions, summaries and autocomplete inside the existing screens; the workflow doesn't change. Usually included, or a small add-on. *Examples: Gmail Smart Compose, Grammarly.*

**3 · AI Directed**: a person asks, AI does one task, the person checks the result.\
A copilot or chat that drafts, builds or fills in on request, across the customer's data. Paid as a per-seat add-on, or by usage. *Examples: Microsoft 365 Copilot, Shopify Sidekick.*

**4 · AI Delegated**: AI does the job end to end; people handle exceptions.\
Owns a whole job and is measured on outcomes; needs guardrails, audit trails and approvals. Paid per outcome or per use, not per seat. *Examples: Intercom Fin, Abridge.*

**5 · AI Domain Intelligence**: AI brings expertise.\
Learns from data across many customers to benchmark, recommend and give answers experts trust. Paid as a premium for expertise. *Examples: Harvey, OpenEvidence.*

**6 · System of Understanding**: the product runs the day-to-day; people set goals.\
Understands how the domain behaves, and anticipates and acts before anyone asks. Paid for results. *Examples: Waymo, Tempus.*

More on each level, with more examples: [the six levels](skills/ai-product-vision/references/level-examples.md).

## Update

In the Claude desktop app, open **Customize**, go to **Plugins**, select the **ai-product** marketplace and click **Check for updates**. Then start a new conversation.

<details>
<summary>In Claude Code</summary>

Run `/plugin`, open **Marketplaces**, select `ai-product` and choose **Enable auto-update**. Or, in your terminal:

```
claude plugin marketplace update ai-product
claude plugin update ai-product@ai-product
```

Then restart Claude Code.

</details>

## License

[MIT](LICENSE) © Yonder SRL ([tss-yonder.com](https://tss-yonder.com/)). Free for anyone to use, change and share.
