# ai-product

In the AI era, product managers have an opportunity to re-imagine their products and grow the business: to rethink what the product does, who it serves and how, now that AI can do work that used to need people.

ai-product is a Claude Code plugin that helps product managers do just that: re-imagine their product for the AI era. Claude works alongside you, step by step. It gets to know your product, your customers and the problems you solve for them; researches your market; finds the opportunities worth pursuing; and turns them into requirements your developers can build from, so your product moves in an AI-native direction.

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
