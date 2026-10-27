---
name: ai-product-start
description: Start here. Confirms the folder, explains what ai-product does, then asks the product manager one question at a time for the product, company, URLs, industry and customers, collects their documents, builds an initial product profile from the URLs and the web, then interviews the product manager about each customer persona and the problems the product solves for them, and fills the gaps in product.md. Run once before any other ai-product skill.
---

# ai-product-start

Run once. Every other ai-product skill reads and writes in the folder this creates.

## How to talk

Conversational, short messages, one question at a time. Never send a list of questions. Don't explain what you didn't find or what you're about to check; just do it.

## Steps

1. **Where we are.** Say which folder you're working in, by its full path, and ask if that's the right place for the product's folder. If you have no folder on the user's computer, say so in one line and tell them how to pick one (in Claude Desktop: the folder picker next to the message box), then wait.

   If this folder, or one folder below it, already has a `product.md`, say which product it is and ask whether to continue with it or start a new one. Don't overwrite without a yes.

2. **What this is.** In two or three sentences, your own words:

   > ai-product helps you re-imagine your product for the AI era. We'll set up a folder for your product, build a profile of it and its customers together, and from there work towards requirements and a prototype your developers can build from.

   Then ask: "Shall we start?" Wait for a yes.

3. **The basics, one question at a time.** Ask each in its own message and wait for the answer. Skip any question an earlier answer already covers.
   1. What's your product called?
   2. What's its website?
   3. What's the company called? Is it the same as the product?
   4. If different: what's the company's website?
   5. Any other links you'd like me to read? For example the pricing page, help docs, an app store listing, reviews on G2 or Capterra, recent news.
   6. What industry is it in, and which niche?
   7. In a few sentences, what does it do and who is it for?
   8. Who are your customers: what types of company or person buy it and use it?

   As soon as you have the product's name, create a folder named after it (lowercase, hyphens, e.g. `acme-scheduler/`) with `documents/` inside. Don't stop to talk about it.

4. **Documents.** Ask:

   > Do you have files about the product or your customers? For example customer interviews or call notes, support tickets, sales or churn notes, usage data, specs, roadmap, pricing, sales decks, notes on competitors. Any format.
   >
   > Drag and drop them here, or put them straight into `[full path]/documents/`. You can add more at any time.

   Save any files they drop into the chat into `documents/`. If they have none yet, carry on.

5. **The initial profile.** Read every URL they gave, run a few web searches on the product and the company, and read anything already in `documents/`. Write a first `product.md` in the folder from that and what they told you. Mark where each fact came from: `[url]`, `[documents/<file>]` or `[PM]`. Leave a section empty rather than guess.

   ```markdown
   # [product name]
   - company: …
   - industry: …
   - links: …
   - team: name (role), …

   ## What it does
   ## Customers
   - customer types: …

   ### [persona name, e.g. "Head of Scheduling at a mid-size university"]
   - who they are: role, type and size of organisation, buyer or user
   - what they're trying to get done
   - the problems this product solves for them
   - how they handled it before, or would without the product
   - what still frustrates them

   ## Main workflows
   ## What customers love / complain about
   ## Pricing and market
   ## Competitors and alternatives
   ## Data and tech
   ## AI today
   ## The idea we have in mind
   ## Still unknown
   ```

   Fill a persona section for each customer type you can see from the URLs and documents, and leave the rest for the next step. Show the profile, short, and say what's missing. If web search or fetching doesn't work, say so plainly: the research skills need it.

6. **The customers.** Ask the product manager to describe each customer type as a person, one at a time, starting with the most important. For each, ask one question at a time about:
   - who they are: role, type and size of organisation, and whether they buy, use, or both;
   - a typical day or week, and what they're measured on;
   - the problem or problems this product solves for them, with a real example;
   - how they handled it before the product, or would without it;
   - what still frustrates them, with or without the product.

   Follow up until each persona feels like someone you could picture, then write it into the `## Customers` section of `product.md` and confirm it with them. Say these are the product manager's view; later skills test them against real data.

7. **The interview.** Interview the product manager to correct the profile and fill its gaps. Ask one question at a time, follow up on vague or interesting answers, and ask for examples ("when did that last happen?"). Only ask what the profile doesn't already answer, from:
   - the job customers hire the product for;
   - the main workflows users go through, and where they spend the most time;
   - what customers love, and what they complain about most;
   - how it's priced and sold, and roughly how many customers;
   - the main competitors and alternatives, including spreadsheets and doing nothing;
   - the data the product holds, and how it's built (stack, integrations);
   - any AI in the product today, and what competitors are doing with AI;
   - the idea or direction the team already has in mind, if any;
   - who is on the team, and their roles.

   Keep it focused. If they say "enough", stop. Update `product.md` as you go, in their words where you can, and show the final version for a last check.

8. **Documents check.** If `documents/` is still empty, remind them once more what to add. If it has files, list them. Then scan them for personal data (people's names, email addresses, phone numbers). If you find any, list the files and ask them to remove or redact it before personas are built. Don't change their files yourself.

9. **Done.** Show the folder tree and sum up in three lines: the product, its customer personas, and what's still unknown. Say they can keep adding files to `documents/`, and that the next step is `/ai-product-vision`.

## Done when

`product.md` holds a sourced profile with a persona and its problems for each customer type, checked by the product manager; they know where `documents/` is, and web research works.
