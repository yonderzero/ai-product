# ai-product-vision

```
/ai-product-vision
```

The second skill, after [`ai-product-start`](ai-product-start.md). Software is moving from recording the work to doing it. Claude maps your market on six levels of AI, shows where your product is today and where the opportunities are, then works with you on a vision for where you could take your product.

**Who runs it:** the product manager, ideally with the team.
**How long:** about 30–45 minutes. The research runs in the background while you talk.
**Run it:** in the folder where `ai-product-start` created your product's folder.

## What you need

- Your product folder from `ai-product-start`, with `product.md`.
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

3. **Research.** Claude researches every company's AI features in the background, and scans for anyone already attacking your product, for example by unbundling a module, rebuilding it for small customers, or sitting on top of it.

4. **Where are you today?** While the research runs, Claude asks where you think your product sits on the six levels, and why.

5. **The map.** Claude places every company, and your product, with sources. If the evidence puts your product lower than you did, it says so and shows why. It names the openings: levels where nobody credible is yet. You get a table and a picture of the market to open in your browser.

6. **The vision interview.** One question at a time:
   - Which level do you want to reach, and by when?
   - Which workflow should AI take over first, end to end?
   - For which customer persona, and what changes in their day?
   - What do you have that others on the map don't?
   - If an agent sat on top of your data tomorrow, what would customers stop paying you for, and what would they pay for instead?
   - Who on the map worries you most, and how does your vision answer them?
   - What's the smallest thing you could build or test next?

7. **The vision.** Claude writes your vision and asks: "Is this right?" It revises until you say yes.

8. **Done.** Claude adds today's level and your target level to `product.md`, and sums up where you are, where you're going, and the first step.

## What you get

```
acme-scheduler/
  product.md          now with today's level and your target level
  market-map.md       every company on the six levels, with sources, and the openings
  market-map.html     the market as a picture: open it in a browser
  threats.md          who is attacking or could attack your product, and how
  vision.md           your product's AI vision
```

`vision.md` holds:

| Section | What's in it |
|---|---|
| Today / where we're going | Today's level and the target level, with a date |
| The vision | Two or three sentences in your words |
| For whom | Each persona, the problem it removes, what changes in their day |
| What AI takes over | Each workflow, today and tomorrow |
| Why us | The data, knowledge, customers or reach others don't have |
| The opening | The gap on the map |
| Who could get there first | The attackers, and how the vision answers them |
| What customers would pay for | What they'd stop paying for, and what they'd pay for instead |
| First step | The smallest thing to build or test next |
| Open questions | What you still need to find out |

## Tips

- Be honest about where your product is today. A flattering placement makes a weak vision.
- Add the competitors you meet in deals, not only the famous ones.
- Placements are a snapshot from public sources on the day you run it. Check the ones you act on.
- Add files to `documents/` at any time, such as lost-deal notes that name competitors; Claude reads them.
