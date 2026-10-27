# How ai-product works

ai-product helps you, as a product manager, re-imagine your product for the AI era. You run its skills in order, in one folder. Each skill is a conversation: Claude asks one question at a time, researches in the background, and writes what you build together into files you keep.

## The skills, in order

| Step | Skill | What you do | Time | What you get |
|---|---|---|---|---|
| 1 | [`/ai-product-start`](ai-product-start.md) | Set up your product's folder, build its profile, describe your customers | 20–30 min | `product.md`, `documents/` |
| 2 | [`/ai-product-vision`](ai-product-vision.md) | Place your product and your market on six levels of AI, rank the opportunities, imagine the future, agree a vision | 45–60 min | `ai-levels.md`, `market-map.md` and `.html`, `market-moves.md`, `opportunities.md`, `vision.md` |

## Your product's folder

Everything lives in one folder, named after your product. Each skill reads what the earlier ones wrote, so run them in the same place.

```
acme-scheduler/
  product.md          the profile: what it does, customers and personas, workflows, pricing, competitors     (start)
  documents/          your files: interviews, tickets, sales notes, specs. Claude reads everything here       (start)
  ai-levels.md        the value your product gives at each level of AI                                        (vision)
  market-map.md       your market on the six levels, with sources                                             (vision)
  market-map.html     the same map as a picture: open it in a browser                                         (vision)
  market-moves.md     who's moving in your market, and what it opens up                                       (vision)
  opportunities.md    your customers' work, and the opportunities in and around your product, ranked          (vision)
  vision.md           your product's AI vision                                                                (vision)
```

All files are plain text. You can open, edit and share them; the next skill reads your edits.

## Where facts come from

Every fact in the files says where it came from:

- a link, for anything found on the web;
- `[documents/<file>]`, for anything from your files;
- `[PM]`, for anything you said.

Claude leaves a gap rather than guess, and lists what's still unknown.

## Example

The [Salesforce example](../examples/salesforce/) shows every file, filled in. It's illustrative, built from public sources, and not affiliated with Salesforce.
