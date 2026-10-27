# ai-product

The AI era gives you, as a product manager, a chance to re-imagine your product and grow the business.

ai-product is a plugin for Claude that helps you do just that. It helps you re-imagine your product for the AI era and innovate in and around it: bringing new value to your existing customers, winning new ones, and growing organically.

Claude works alongside you, step by step. It gets to know your product, your customers and the problems you solve for them; maps your market; helps you set your product's AI vision; and turns it into requirements your developers can build from.

## Install

In the Claude desktop app:

1. Open **Customize** and go to **Plugins**.
2. Click **Add**, choose **Add marketplace**, then **Add from a repository**.
3. Enter `yonderzero/ai-product` and add it.
4. Find **ai-product** in the list and click **Install**.

Plugins need a paid Claude plan (Pro, Max, Team or Enterprise).

## Get started

1. Start a new conversation and choose a folder on your computer with **Project or folder**, under the message box. Claude will create your product's folder inside it.
2. Type `/ai-product-start` and send.

<details>
<summary>Using Claude Code in the terminal instead</summary>

```
/plugin marketplace add yonderzero/ai-product
/plugin install ai-product@ai-product
```

Restart Claude Code in the folder you want to work in, then run `/ai-product-start`.

</details>

## Skills

| Skill | What it does |
|---|---|
| [`/ai-product-start`](docs/ai-product-start.md) | Sets up a folder for your product, builds a first profile from its website and your documents, and interviews you about the product and each type of customer. |
| [`/ai-product-vision`](docs/ai-product-vision.md) | Maps your market on six levels of AI, from System of Record to System of Understanding, places your product, finds who could overtake it, and writes your product's AI vision with you. |

More skills are coming.

## Update

In the Claude desktop app, open **Customize**, go to **Plugins**, select the **ai-product** marketplace and click **Check for updates**. Then start a new conversation.

<details>
<summary>In Claude Code</summary>

Run `/plugin`, open **Marketplaces**, select `ai-product` and choose **Enable auto-update**. Or, in your terminal:

```
claude plugin marketplace update ai-product
claude plugin update ai-product@ai-product
```

Then restart Claude Code.

</details>

## License

[MIT](LICENSE) © Yonder SRL ([tss-yonder.com](https://tss-yonder.com/)). Free for anyone to use, change and share.
