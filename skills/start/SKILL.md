---
name: start
description: Start here. Explains what ai-product does, asks the product manager for the product, company, industry and relevant URLs, creates a folder for the product with a documents/ folder for customer interviews and other material, builds an initial product profile from the URLs and the web, then interviews the product manager to fill the gaps in product.md. Run once before any other ai-product skill.
---

# Start

Run once. Every other ai-product skill reads and writes in the folder this creates.

## Steps

1. **What this is.** Open by telling the team, in your own words and briefly:

   > ai-product takes your product in an AI-native direction. I'll set up a folder for it on your machine, and from there we work step by step: research your product and its market, find the problems worth solving, build synthetic customers from your own data, and shape something new, cool and AI-native. You end with requirements and a prototype your developers can build from.

2. **Already set up?** If the current folder, or one folder below it, has a `product.md`, show it and ask whether to update it or start a new product. Don't overwrite without a yes.

3. **The basics.** Ask, in one message:
   - the product's name;
   - the company's name;
   - the URLs that are relevant: the product's website, and any others worth reading (pricing page, docs or help centre, app store listing, review pages such as G2 or Capterra, recent announcements);
   - the industry (and the niche within it, if there is one);
   - a few sentences about the product: what it does and who it's for.

4. **The folder.** Create a folder named after the product (lowercase, hyphens, e.g. `acme-scheduler/`) in the current folder, with `documents/`, `panel/` and `handoff/` inside. Then ask for documents straight away, so they can copy files while you work:

   > While I build the first profile, put anything you have about the product in `[full path]/documents/`. The most useful:
   > - customer interviews, call notes or transcripts
   > - support tickets and the most common complaints
   > - sales notes, lost deals and churn reasons
   > - usage data or analytics exports
   > - product specs, roadmap, pricing, sales decks
   > - notes on competitors
   >
   > Any format works. You can add more at any time; every skill reads this folder.

5. **The initial profile.** Read every URL they gave, run a few web searches on the product and the company, and read anything already in `documents/`. Write a first `product.md` in the folder from that and what they told you. Mark where each fact came from: `[url]`, `[documents/<file>]` or `[PM]`. Leave a section empty rather than guess.

   ```markdown
   # [product name]
   - company: …
   - industry: …
   - links: …
   - team: name (role), …

   ## What it does
   ## Who buys it, who uses it
   - customer types: …
   ## Main workflows
   ## What customers love / complain about
   ## Pricing and market
   ## Competitors and alternatives
   ## Data and tech
   ## AI today
   ## The idea we have in mind
   ## Still unknown
   ```

   Show the profile, short, and say what's missing. If web search or fetching doesn't work, say so plainly: the research skills need it.

6. **The interview.** Interview the product manager to correct the profile and fill its gaps. Ask one or two questions at a time, follow up on vague or interesting answers, and ask for examples ("when did that last happen?"). Only ask what the profile doesn't already answer, from:
   - the job customers hire the product for;
   - who buys it and who uses it day to day (often different people), and the 3–5 customer types;
   - the main workflows users go through, and where they spend the most time;
   - what customers love, and what they complain about most;
   - how it's priced and sold, and roughly how many customers;
   - the main competitors and alternatives, including spreadsheets and doing nothing;
   - the data the product holds, and how it's built (stack, integrations);
   - any AI in the product today, and what competitors are doing with AI;
   - the idea or direction the team already has in mind, if any;
   - who is on the team, and their roles.

   Aim for 10–15 minutes. If they say "enough", stop. Update `product.md` as you go, in their words where you can, and show the final version for a last check.

7. **Documents check.** If `documents/` is still empty, remind them once more what to add. If it has files, list them. Then scan them for personal data (people's names, email addresses, phone numbers). If you find any, list the files and ask them to remove or redact it before personas are built. Don't change their files yourself.

8. **Done.** Show the folder tree and say: "Ready. Next: `/ai-product:01-know-your-product`."

## Done when

`product.md` holds a sourced profile the product manager has checked, they know where `documents/` is, and web research works.
