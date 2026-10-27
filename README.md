# ai-product

The AI era gives you, as a product manager, a chance to re-imagine your product and grow the business.

ai-product is a Claude Code plugin that helps you do just that. It helps you re-imagine your product for the AI era and innovate in and around it: bringing new value to your existing customers, winning new ones, and growing organically.

Claude works alongside you, step by step. It gets to know your product, your customers and the problems you solve for them; maps your market; helps you set your product's AI vision; and turns it into requirements your developers can build from.

## Install

In Claude Code, run:

```
/plugin marketplace add yonderzero/ai-product
/plugin install ai-product@ai-product
```

Then restart Claude Code, open the folder you want to work in, and run:

```
/ai-product:ai-product-start
```

## Skills

| Skill | What it does |
|---|---|
| [`/ai-product:ai-product-start`](docs/ai-product-start.md) | Sets up a folder for your product, builds a first profile from its website and your documents, and interviews you about the product and each type of customer. |
| [`/ai-product:ai-product-vision`](docs/ai-product-vision.md) | Maps your market on six levels of AI, from System of Record to System of Understanding, places your product, finds who could overtake it, and writes your product's AI vision with you. |

More skills are coming.

## Update

To get updates automatically, run `/plugin`, open **Marketplaces**, select `ai-product` and choose **Enable auto-update**.

To update by hand, run this in your terminal and restart Claude Code:

```
claude plugin marketplace update ai-product
claude plugin update ai-product@ai-product
```

## License

[MIT](LICENSE) © Yonder SRL ([tss-yonder.com](https://tss-yonder.com/)). Free for anyone to use, change and share.
