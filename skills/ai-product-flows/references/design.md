# The design direction

Before the mockups, settle how they should look, and write it to `flows/DESIGN.md`. Every mockup follows it, and the roadmap skill hands it to the developers with the build-day slice, so what they build looks like what customers tested.

## Two ways in

1. **The product's own look (preferred).** Ask the product manager for two or three screenshots of the product (drag and drop, or files in `documents/`). Read them and describe what you see.
2. **A style from getdesign.md.** If they have no screenshots, or want the new experience to look fresher, offer three styles that fit the product and its customers from getdesign.md, a public collection of design descriptions (MIT licence, https://github.com/VoltAgent/awesome-design-md, browse at https://getdesign.md). Each one is a `DESIGN.md` describing colours, type, spacing and components. Good fits for B2B software are often Linear (calm, precise, one accent), Stripe (polished), IBM Carbon (structured), Notion (soft, readable), Cal.com (neutral) or Mintlify (clean, readable). Describe each in one line and ask which feels right. Fetch the chosen `DESIGN.md` from `https://raw.githubusercontent.com/VoltAgent/awesome-design-md/main/design-md/<site>/DESIGN.md` (for example `linear.app`); if that path doesn't work, find it on getdesign.md.

   Use it as **a style like** that site, never as its brand: no logos, product names or brand assets in the mockups, and say "inspired by the Linear style" in `DESIGN.md`. The product's own name and logo, if shared, stay.

## What goes in `flows/DESIGN.md`

Keep it short and concrete, so a developer or another agent can apply it:

```markdown
# [Product] · Design direction

Source: the product's screenshots / a style like [site] from getdesign.md (MIT).

## Colours
| Token | Value | Use |
|---|---|---|
| background | | |
| surface | | cards, panels |
| text | | |
| text-muted | | |
| border | | |
| accent | | primary actions, focus |
| success / warning / danger | | statuses |

## Type
- Families: … (with fallbacks)
- Scale: page title …px, section …px, body …px, small …px; weights …

## Spacing and shape
- Base unit …px; card padding …; radius …; borders or shadows …

## Components
- Buttons: primary, secondary
- Cards and tables
- Status pills (approved, waiting, exception)
- The agent's work: how a suggestion, an approval and an exception look
- Light and dark, if both

## Do / don't
- …
```

Show the product manager the colours and one sample component, and ask: "Does this feel like your product?" Adjust until they say yes.
