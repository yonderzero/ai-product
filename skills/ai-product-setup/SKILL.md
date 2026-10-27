---
name: ai-product-setup
description: Start here. Set up the team's product - asks for the product name, company, website and customers, creates a folder for the product with a documents/ folder for anything the team wants Claude to use, and checks that web research works. Run once before any other ai-product skill.
---

# Set up your product

Run once. Every other ai-product skill reads and writes in the folder this creates.

## Steps

1. **Already set up?** If the current folder, or one folder below it, has a `product.md`, show it and ask whether to update it or start a new product. Don't overwrite without a yes.

2. **The product.** Ask the team, in one message:
   - the product's name;
   - the company that makes it;
   - the product's website (URL);
   - the product line, if the company has several;
   - who is on the team, and their roles;
   - the 3–5 types of customer the product serves.

   Anything they don't know yet can be left blank and filled in later.

3. **The folder.** Create a folder named after the product (lowercase, hyphens, e.g. `acme-scheduler/`) in the current folder, with `documents/`, `panel/` and `handoff/` inside. Write the answers to `product.md` in it:

   ```markdown
   # [product name]
   - company: …
   - website: …
   - product line: …
   - team: name (role), …
   - customer types: …
   ```

4. **Documents.** Tell the team, plainly:

   > Put anything you want me to use in `[folder]/documents/`: customer interviews, support tickets, sales and churn notes, usage exports, specs, decks. Any format. You can add more at any time; every skill reads it.

   If they've added files, list them. Then scan them for personal data (people's names, email addresses, phone numbers). If you find any, list the files and ask the team to remove or redact it before personas are built. Don't change their files yourself.

5. **Smoke test.** Run one web search for the product and report one sourced fact about it. If web search doesn't work, say so plainly: the research skills need it.

6. **Done.** Show the folder tree and say: "Ready. Next: `/ai-product:01-know-your-product`."

## Done when

`product.md` exists, the team knows where `documents/` is, and the smoke test returned a sourced fact.
