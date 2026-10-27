# ai-product-vision

```
/ai-product-vision
```

The second skill, after [`ai-product-start`](ai-product-start.md). Software is moving from recording the work to doing it. Claude goes through six levels of AI with you and maps the value your product gives customers at each one today. Then it maps your market on the same levels, maps your customers' work around the product, ranks the opportunities in and around it, and works with you on a vision for where you could take your product.

**Who runs it:** the product manager, ideally with the team.
**How long:** about 45–60 minutes. The research runs in the background while you talk.
**Run it:** in the folder where `ai-product-start` created your product's folder.

## What you need

- Your product profile from [`ai-product-start`](ai-product-start.md). If it isn't done yet, Claude asks you to run `/ai-product-start` first.
- An idea of your competitors. Claude proposes the market; you add who's missing.

## The six levels

| # | Level | Who does the work |
|---|---|---|
| 1 | System of Record | People do the work; the software stores it |
| 2 | AI Assisted | People do the work; AI suggests |
| 3 | AI Directed | A person asks; AI does one task; the person checks each result |
| 4 | AI Delegated | AI does the job end to end; people handle exceptions |
| 5 | AI Domain Intelligence | AI brings expertise learned from data across many customers |
| 6 | System of Understanding | The product understands how the domain works, anticipates and acts |

A company sits at the highest level it has **shipped and customers use**, with a source. Announcements don't count, and your own product gets the same rules as everyone else.

## What happens

Claude asks one question at a time, like a conversation.

1. **What this is.** Claude names your product, explains the idea in a few sentences, and asks: "Shall we start?"

2. **The market.** Claude proposes 10–15 companies in three groups: incumbents in your vertical, AI-native challengers, and horizontal players such as big platforms and AI assistants. It asks who's missing.

3. **Research.** Claude researches every company's AI features in the background, and looks at how others are moving into your market: focused tools for one part of your product, simpler products for smaller customers, add-on layers, new channels, and AI products built on top.

4. **Your product, level by level.** While the research runs, Claude goes up the levels with you, starting at 1. At each level it asks, one question at a time:
   - Does your product give customers value at this level? Which features?
   - For whom: which persona, buyer or user?
   - What value do they get?
   - How do they pay for it: included, an add-on, per seat, per use, per outcome?
   - Is it shipped and used, and is there an example?

   It starts from what it already knows from your profile and website, and asks you to confirm. When a level has nothing yet, it asks whether anything is in beta or planned. Your product's level today is the highest level with value that is shipped and used.

5. **The map.** Claude places every company, and your product, with sources. If the public evidence puts your product lower than your own answers did, it says so and shows why. It names the openings: levels where nobody credible is yet. You get a table and a picture of the market to open in your browser.

6. **The work around your product.** Claude drafts your customers' work as 6–10 steps, from the research and what you've told it, and walks you through it one step at a time: what happens, who does it, which software runs it, and what's still done by hand, in email or in spreadsheets.

7. **The opportunities.** Claude finds up to 8 opportunities in and around your product, in two kinds: more value for your existing customers, and new revenue (new products, modules, data or services, or new customers). Each one is specific, based on evidence, placed at a level, and rated:
   - **Impact**, **effort** and **urgency**, from 1 to 5, each with a reason;
   - **Evidence**: Strong, Good, Thin or Assumption;
   - **Priority**: Do first, Strong option or Worth watching;
   - **Size**: what it could be worth a year, only when real numbers allow, with the working shown;
   - **First question**: the one question to ask customers that would confirm or kill it.

   Claude shows the ranked list and asks which excite you, what's missing, and whether any rating is wrong.

8. **Imagine.** The creative part. For each level above where your product is today, Claude shows two real products already there and sketches what *your* product could look like at that level: what it does, for whom, what changes in their day, and how customers would pay. You add to it. Then Claude writes a day in the life of your main persona five years from now, with your product as a System of Understanding, and asks what excites you, what feels wrong, and what it would need to know. See [real products at each level](../skills/ai-product-vision/references/level-examples.md).

9. **The vision interview.** One question at a time:
   - Which of the top opportunities should the vision start with, on the way to that future?
   - Which level do you want to reach, and by when?
   - For which customer persona, and what changes in their day?
   - What do you have that others on the map don't?
   - If an agent sat on top of your data tomorrow, what would customers stop paying you for, and what would they pay for instead?
   - Who on the map is moving closest to your vision, and what makes yours different?
   - What's the smallest thing you could build or test next?

10. **The vision.** Claude writes your vision and asks: "Is this right?" It revises until you say yes.

11. **Done.** Claude adds today's level and your target level to `product.md`, and sums up where you are, where you're going, and the first step.

## What you get

```
acme-scheduler/
  product.md          now with today's level and your target level
  ai-levels.md        the value your product gives at each level: features, for whom, how they pay
  market-map.md       every company on the six levels, with sources, and the openings
  market-map.html     the market as a picture: open it in a browser
  market-moves.md     who's moving in your market, and what it opens up for you
  opportunities.md    your customers' work, and the opportunities in and around your product, ranked
  vision.md           your product's AI vision
```

`vision.md` holds:

| Section | What's in it |
|---|---|
| Today / where we're going | Today's level and the target level, with a date |
| Imagine | Your product at each higher level, and a day with your System of Understanding |
| The vision | Two or three sentences in your words |
| Built on | The opportunities the vision is built around |
| For whom | Each persona, the problem it removes, what changes in their day |
| What AI takes over | Each workflow, today and tomorrow |
| Why us | The data, knowledge, customers or reach others don't have |
| The opening | The gap on the map |
| Others moving this way | Who, at which level, and what makes your vision different |
| What customers would pay for | What they'd stop paying for, and what they'd pay for instead |
| First step | The smallest thing to build or test next |
| Open questions | What you still need to find out |

## Tips

- Be honest about where your product is today. A flattering placement makes a weak vision.
- Add the competitors you meet in deals, not only the famous ones.
- Placements are a snapshot from public sources on the day you run it. Check the ones you act on.
- Add files to `documents/` at any time, such as lost-deal notes that name competitors; Claude reads them.
