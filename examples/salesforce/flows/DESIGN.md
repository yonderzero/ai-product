# Salesforce Sales Cloud and Service Cloud · Design direction

> Illustrative. Not affiliated with or endorsed by Salesforce. The product manager's answers are invented, tagged `[PM, illustrative]`. This direction deliberately does not imitate Salesforce's look: no Salesforce blue, cloud, logo, Salesforce Sans or Lightning components.

Source: a style like Cal.com, from getdesign.md (MIT), not its brand. No product screenshots were used, so this is route 2 in the flows skill's `references/design.md`. The tokens come from `design-md/cal/DESIGN.md` in https://github.com/VoltAgent/awesome-design-md, fetched 27 Oct 2026; the darker text shades on the status tints are worked out from its success, warning and error colours so the text is readable. No Cal.com logo, name or assets appear in the mockups. The customer in the mockups, Lumen Ridge Software, is invented.

- **Offered:** Cal.com (neutral, black and white, soft cards), Stripe (polished, indigo, gradients) and Linear (calm, dark, one accent).
- **Chosen:** Cal.com. The mockups had to feel like a calm, neutral SaaS screen that a rep and a sales manager would trust, without looking like Salesforce or any other vendor. Its near-black and white palette has no brand colour to clash with, so the only colours on screen are the statuses and the agent's work. Stripe's indigo and gradients drew the eye away from the evidence; Linear's dark theme read as a developer tool to the sales personas. [PM, illustrative]

## Colours

| Token | Value | Use |
|---|---|---|
| background | `#f8f9fa` | the page |
| surface | `#ffffff` | cards, the top bar, the Back / Next bar |
| surface-soft | `#f5f5f5` | evidence boxes, neutral pills, hover |
| text | `#111111` | headings, values, the new value in a change |
| text-body | `#374151` | running text |
| text-muted | `#6b7280` | labels, table heads, the moment name |
| text-subtle | `#898989` | the old value in a change, the footnote |
| border | `#e5e7eb` | 1px lines on cards, tables and inputs |
| accent | `#111111` | primary buttons, the chosen step |
| link / focus | `#3b82f6` | links and focus rings only |
| agent | `#8b5cf6` (tint `#f5f3ff`, text `#6d28d9`) | what the agent proposed or wrote |
| success | `#10b981` (tint `#ecfdf5`, text `#047857`) | confirmed, accepted, up to date |
| warning | `#f59e0b` (tint `#fffbeb`, text `#b45309`) | waiting, moves the forecast, needs the rep |
| danger | `#ef4444` (tint `#fef2f2`, text `#b91c1c`) | rejected, overridden, at risk |

## Type

- Families: Inter (Google Fonts), then -apple-system, Segoe UI, Roboto, sans-serif. Cal.com's own display face is not used; Inter 600 with tight letter spacing stands in, as its DESIGN.md suggests.
- Scale: page title 28px weight 600, letter spacing -0.5px; section 18px weight 600; body 15px weight 400, line height 1.5; small 13px weight 500 for pills, captions and table heads.
- Numbers in tables use tabular figures, so amounts line up.

## Spacing and shape

- Base unit 4px. Steps: 4, 8, 12, 16, 24, 32, 48.
- Cards: 24px padding, 16px apart, 1px border, a faint shadow `0 1px 2px rgba(0,0,0,.05)`.
- Radius: 12px for cards and banners, 8px for buttons, inputs and evidence boxes, full round for pills and the step switcher's items.
- Content width 880px, centred.

## Components

- **Buttons:** primary is near-black `#111111` with white text, 8px radius, 36px tall, weight 600. Secondary is white with a 1px border and dark text. A chosen decision fills: accept in success tint, reject in danger tint, edit in near-black.
- **Cards and tables:** white cards with a hairline border and faint shadow. Tables have no outer border, 1px row lines, muted 13px heads, tabular numbers.
- **Status pills:** full round, 13px weight 500, tint background, darker text and a small dot in the same colour. Confirmed / accepted: success. Waiting / moves the forecast: warning. Rejected / at risk: danger. Neutral: surface-soft.
- **A proposed change:** the field name in weight 600, the old value struck through in subtle grey, an arrow, the new value in weight 600, and the evidence underneath in a soft grey box with the source and a quote.
- **The agent's work:**
  - a suggestion: a card with a 3px violet bar on the left and a violet dot, or a violet "proposed" pill; nothing the agent proposes changes the deal until the rep accepts it;
  - an approval: "Accept", "Edit" and "Reject" on every change, with no "accept all"; afterwards a success pill and who confirmed it;
  - an exception: a warning banner (amber tint, amber border) saying what the agent could not do and what it left alone.
- **The Back / Next bar:** white with a top border; Back is secondary, Next is primary; the moments sit in a soft grey switcher, the current one raised on white.
- **"Mockup for testing":** a small amber pill at the top right. Every screen ends with "Illustrative, not affiliated with Salesforce. Companies, people and numbers are invented."
- **Light and dark:** light only for now.

## Do / don't

- Do keep the screen near-monochrome, so colour always means a status or the agent's work.
- Do show the evidence next to every change the agent proposes.
- Don't use blue for buttons or headers; keep it for links and focus.
- Don't imitate Salesforce: no Salesforce blue, cloud shapes, Salesforce Sans, Lightning components or product names in the mockups.
- Don't use Cal.com's logo, name or Cal Sans wordmark.
