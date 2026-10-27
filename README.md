# ai-product

A Claude Code plugin.

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

Claude asks about your product and creates a folder for it. Put any documents you want Claude to use in its `documents/` folder.

## Update

To get updates automatically, run `/plugin`, open **Marketplaces**, select `ai-product` and choose **Enable auto-update**.

To update by hand, run this in your terminal and restart Claude Code:

```
claude plugin marketplace update ai-product
claude plugin update ai-product@ai-product
```

## Credits

See `THIRD-PARTY-NOTICES.md`.
