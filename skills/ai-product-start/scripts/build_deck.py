#!/usr/bin/env python3
"""Embed a product folder's markdown files into its index.html deck.

Usage:
    python3 build_deck.py <product folder> [--template <templates/index.html>]

- Reads <product folder>/index.html (or the template if there's none yet).
- With --template, rebuilds the deck from the current template and keeps its data block,
  so an older deck gets every new slide.
- Embeds every .md file in the folder (except documents/, which can hold customer material)
  into the <script id="files"> block, and lists the HTML files (mockups, the market map) as assets.
"""
import argparse
import json
import os
import re

DATA = re.compile(r'(<script type="application/json" id="data">)(.*?)(</script>)', re.S)
FILES = re.compile(r'(<script type="application/json" id="files">)(.*?)(</script>)', re.S)
SKIP_DIRS = {"documents", ".git", "node_modules"}


def collect(folder):
    files, assets = {}, []
    for root, dirs, names in os.walk(folder):
        dirs[:] = sorted(d for d in dirs if d not in SKIP_DIRS and not d.startswith("."))
        for name in sorted(names):
            path = os.path.join(root, name)
            rel = os.path.relpath(path, folder).replace(os.sep, "/")
            if name.endswith(".md"):
                with open(path, encoding="utf-8") as f:
                    files[rel] = f.read()
            elif name.endswith(".html") and rel != "index.html":
                assets.append(rel)
    return files, assets


def safe_json(obj):
    # Keep "</script>" inside the content from closing the script tag.
    return json.dumps(obj, ensure_ascii=False).replace("</", "<\\/")


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("folder", help="the product folder (the one with product.md)")
    ap.add_argument("--template", help="the deck template, to rebuild an older deck")
    a = ap.parse_args()

    deck_path = os.path.join(a.folder, "index.html")
    current = open(deck_path, encoding="utf-8").read() if os.path.exists(deck_path) else None
    if a.template:
        html = open(a.template, encoding="utf-8").read()
        if current and DATA.search(current):
            data = DATA.search(current).group(2)
            m = DATA.search(html)
            html = html[: m.start(2)] + data + html[m.end(2):]
    elif current:
        html = current
    else:
        raise SystemExit("No index.html in the folder: pass --template to create it.")

    files, assets = collect(a.folder)
    block = safe_json({"files": files, "assets": assets})
    m = FILES.search(html)
    if not m:
        raise SystemExit("This deck has no files block: rerun with --template to update it.")
    html = html[: m.start(2)] + block + html[m.end(2):]

    with open(deck_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Embedded {len(files)} markdown files and {len(assets)} HTML files into {deck_path}")


if __name__ == "__main__":
    main()
