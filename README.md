# ai-product

A Claude Code plugin that takes your product in an AI-native direction: from knowing your product and your customers to requirements your developers can build from.

## Install

In Claude Code, run:

```
/plugin marketplace add yonderzero/ai-product
/plugin install ai-product@ai-product
```

Then restart Claude Code, open the folder you want to work in, and run:

```
/ai-product:start
```

## Skills

| Skill | What it does |
|---|---|
| [`/ai-product:start`](docs/start.md) | Sets up a folder for your product, builds a first profile from its website and your documents, and interviews you about the product and each type of customer. |

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
