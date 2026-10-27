---
name: 00-setup
description: Set up a product team's folder for the Product Track (run once, before session 01). Creates my-product/ with inputs/, panel/ and handoff/, records the product, checks that web research works, and checks the inputs for personal data.
---

# 00 · Set up

Run once, in the folder the team will work in all week. Every other Product Track skill reads and writes here.

## Steps

1. **Where.** If the current directory is not already a product folder (no `product.md`), propose creating `my-product/` here and moving into it. Create `inputs/`, `panel/` and `handoff/`.

2. **The product.** Ask the team, in one message:
   - the product's name and website;
   - the product line, if the company has several;
   - who is on the team, and their roles;
   - the 3–5 types of customer the product serves.

   Write the answers to `product.md`:

   ```markdown
   # [product name]
   - website: …
   - product line: …
   - team: name (role), …
   - customer types: …
   ```

3. **Inputs.** Ask the team to copy what they brought into `inputs/`: customer interviews, support tickets, sales and churn notes, usage exports. List what's there. Then scan the files for personal data (people's names, email addresses, phone numbers). If you find any, list the files and ask the team to remove or redact it before session 05. Don't change their files yourself.

4. **Smoke test.** Run one web search for the product name and report one sourced fact about it. If web search doesn't work, say so plainly: missions 01–04 need it.

5. **Done.** Show the folder tree and say: "Ready. In session 01, run `/product-track:01-know-your-product`."

## Done when

`product.md` exists, `inputs/` has the team's material (or the team has said it has none), and the smoke test returned a sourced fact.
