# ai-product-start

```
/ai-product-start
```

The first skill to run. Claude checks where it's working, explains what ai-product is for, sets up a folder for your product, builds a first profile of the product from the web and your documents, and interviews you about your product and your customers.

**Who runs it:** the product manager, or whoever knows the product best.
**How long:** about 20–30 minutes, most of it conversation.
**Run it:** once per product, in the folder where you want the product's folder to be created.

## What you need

- The product's name, the company's name, and the industry it's in.
- Links about the product: the website, and if you have them, the pricing page, help docs, app store listing, review pages (G2, Capterra) and recent announcements.
- Any documents about the product and its customers (optional, but the more the better). See [Documents](#documents).

## What happens

Claude asks one question at a time, like a conversation.

1. **Where we are.** Claude tells you which folder it's working in and checks that's where you want your product's folder. If it's not working in a folder on your computer, it tells you how to pick one. If a product is already set up there, it asks whether to continue with it or start a new one; it never overwrites without asking.

2. **What this is.** Claude explains in a few sentences that ai-product helps you re-imagine your product for the AI era, and asks: "Shall we start?"

3. **The basics.** One question at a time:
   - What's your product called?
   - What's its website?
   - What's the company called? Is it the same as the product? If not, what's its website?
   - Any other links to read: pricing, help docs, app store listing, G2 or Capterra reviews, recent news?
   - What industry is it in, and which niche?
   - What does it do, and who is it for?
   - Who are your customers?

   Once it has the product's name, Claude creates the product's folder.

4. **Documents.** Claude asks whether you have files about the product or your customers. Drag and drop them into the chat, or put them straight into the `documents/` folder. See [Documents](#documents).

5. **The initial profile.** Claude reads every link you gave, searches the web for the product and the company, and reads anything already in `documents/`. It writes a first `product.md`, with the source of every fact, and shows you what's missing. This step also checks that web research works, which later skills depend on.

6. **The customers.** Claude asks you to describe each type of customer as a person, one customer type and one question at a time, starting with the most important:
   - who they are: role, type and size of organisation, and whether they buy, use, or both;
   - a typical day or week, and what they're measured on;
   - the problems your product solves for them, with a real example;
   - how they managed before your product, or would without it;
   - what still frustrates them.

   Claude follows up until each persona is concrete, writes it into `product.md`, and checks it with you. These personas are your view of the customer; later skills test them against real data.

7. **The interview.** Claude asks about whatever the profile doesn't answer yet, one question at a time: the main workflows, what customers love and complain about, pricing and sales, competitors and alternatives, data and tech, AI in the product today, any idea your team already has, and who is on the team. It updates `product.md` as you talk and shows you the final version. Say "enough" at any point to stop.

8. **Documents check.** Claude lists what's in `documents/` and checks it for personal data (people's names, email addresses, phone numbers). If it finds any, it tells you which files to clean up. It never edits your files.

9. **Done.** Claude shows the folder and sums up the product, its personas, and what's still unknown. Next: [`/ai-product-vision`](ai-product-vision.md).

## What you get

```
acme-scheduler/          named after your product
  product.md             the product profile
  documents/             your material: Claude reads everything here
  panel/                 used later for synthetic customers
  handoff/               used later for what your developers get
```

`product.md` holds:

| Section | What's in it |
|---|---|
| Header | Company, industry, links, team |
| What it does | The product in a few sentences |
| Customers | One persona per customer type: who they are, what they're trying to get done, the problems the product solves for them, how they managed before, what still frustrates them |
| Main workflows | What users do in the product, and where they spend time |
| What customers love / complain about | |
| Pricing and market | How it's priced and sold, roughly how many customers |
| Competitors and alternatives | Including spreadsheets and doing nothing |
| Data and tech | What data the product holds, how it's built |
| AI today | AI in the product, and what competitors do with AI |
| The idea we have in mind | Any direction the team already has |
| Still unknown | Open questions to fill later |

Every fact is tagged with where it came from: a URL, a file in `documents/`, or `[PM]` for what you said.

## Documents

Drag and drop files into the chat, or put them straight into `documents/`, in any format:

- customer interviews, call notes or transcripts
- support tickets and the most common complaints
- sales notes, lost deals and churn reasons
- usage data or analytics exports
- product specs, roadmap, pricing, sales decks
- notes on competitors

You can add more at any time; every skill reads this folder. Remove people's names, email addresses and phone numbers first.

## Tips

- Give Claude as many links as you can: the profile is only as good as what it can read.
- Answer the customer questions with real examples ("last week a scheduler at…"), not general statements.
- If you don't know something, say so. It goes under "Still unknown" instead of being guessed.
- To change the profile later, edit `product.md` yourself or run `/ai-product-start` again and choose to update.
