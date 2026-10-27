# FleetDesk · Design direction

Source: a style like IBM (Carbon), from getdesign.md (MIT), not its brand. No screenshots of FleetDesk were shared, so this is route 2 in the flows skill's `references/design.md`. The tokens come from `design-md/ibm/DESIGN.md` in https://github.com/VoltAgent/awesome-design-md, fetched 27 Oct 2026; the light status tints are worked out from those colours. No IBM logo, name or assets appear in the mockups. FleetDesk's own name stays.

- **Offered:** IBM Carbon (structured, square, high contrast), Linear (calm, one accent, dense) and Notion (soft, readable).
- **Chosen:** IBM Carbon. Rosa reads the shortlist at a shop desktop early in the morning and Dwayne uses a tablet at the bench in a bright, noisy shop, so the product manager wanted the most contrast and the biggest, plainest controls. Linear felt too dark and fine-grained for a shop floor, Notion too soft for safety items. [PM, illustrative]

## Colours

| Token | Value | Use |
|---|---|---|
| background | `#ffffff` | the page |
| surface | `#f4f4f4` | panels, the selected nav item, input fields, quoted speech |
| surface-2 | `#e0e0e0` | neutral tags, disabled controls |
| inverse | `#161616` | the top bar and the Back / Next bar |
| text | `#161616` | everything that matters |
| text-muted | `#525252` | labels, meta, "who did it" lines |
| text-subtle | `#8c8c8c` | helper text only, never for data |
| border | `#e0e0e0` | 1px lines on cards, rows and inputs |
| border-strong | `#161616` | focus underline |
| accent | `#0f62fe` | primary actions, links, focus, the agent's work |
| accent-hover / pressed | `#0050e6` / `#002d9c` | button states |
| accent-tint | `#edf5ff` | the agent's banners and tags |
| success | `#24a148` (tint `#defbe6`, text `#0e6027`) | opened, approved, parts on the shelf, feed OK |
| warning | `#f1c21b` (tint `#fcf4d6`, text `#161616`) | not sure, waiting, feed incomplete, plan this week |
| danger | `#da1e28` (tint `#fff1f1`, text `#a2191f`) | pull in today, safety items, struck |

## Type

- Families: IBM Plex Sans (Google Fonts), then Helvetica Neue, Arial, sans-serif. IBM Plex Mono for truck numbers, fault codes and VMRS codes.
- Scale: page title 28px weight 400; section 20px weight 600; body 16px weight 400, line height 1.5, letter spacing 0.16px; small 14px; caption 12px.
- Weights: 300 only for big numbers; 400 for text; 600 for truck numbers, section heads and the moment name.
- Sentence case everywhere. No all-caps labels.

## Spacing and shape

- Base unit 4px. Steps: 4, 8, 12, 16, 24, 32, 48.
- Cards: 24px padding, 16px apart.
- Radius 0 on everything: cards, buttons, inputs, banners, tags. The only round thing is the talk button on the tablet.
- Borders, not shadows: 1px `border` lines and a change of surface carry the structure.
- Buttons are 48px tall on the shop desktop and tablet, so they work with gloves on.

## Components

- **Buttons:** primary is accent with white text, square, 48px tall. Secondary is charcoal `#161616` with white text. Tertiary is white with a 1px accent border and accent text. Danger is `#da1e28` with white text.
- **Cards and tables:** white, 1px border, square, 24px padding. Rows split by 1px lines. Truck numbers in Plex Mono 20px weight 600, the reason in body text, the status tag on the right.
- **Status tags:** square, 24px tall, 12px text, tint background with dark text. Opened / approved: success. Waiting / not sure / plan this week: warning. Pull in today / safety / struck: danger. Watching: neutral `surface-2`.
- **Navigation:** charcoal top bar 48px tall with "FleetDesk" in white. Side nav white; the selected item on `surface` with a 3px accent bar on the left.
- **The agent's work:**
  - a suggestion or draft: an accent-tint banner with a 3px accent bar on the left, and a "Drafted by the agent" tag in accent-tint with accent text; nothing it drafts looks like it is already done;
  - an approval: a primary button that names who signs ("Approve", "Sign and close as Dwayne"); afterwards a success tag and a "who, when" line under the row;
  - an exception: a warning banner (tint, 3px `#f1c21b` bar on the left, dark text) that says what is missing and what the agent did not do; safety items always carry a red "Safety" tag.
- **The Back / Next bar:** inverse charcoal at the bottom; the moment name in white weight 600, its line in `#c6c6c6`; progress as small squares, the current one in accent.
- **"Mockup for testing":** a small warning-tint tag, fixed at the top right.
- **Light and dark:** light only for now. The charcoal top and bottom bars are the only dark surfaces.

## Do / don't

- Do keep contrast high: data in `#161616` on white; muted grey only for labels.
- Do use one accent colour. Blue means "act here" or "the agent did this", nothing else.
- Do show raw codes in Plex Mono so a technician can check them.
- Don't round corners or add shadows.
- Don't put meaning in colour alone: every status tag has words.
- Don't use IBM's logo, name, imagery or the 8-bar mark.
