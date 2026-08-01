#!/usr/bin/env python3
"""
Kayak Photography Sim — store text check page updater.

Usage:
    python3 update-texts.py <localization.md> [--label v2.6]

Reads the localization markdown, checks it, and writes the texts into
index.html. Nothing else in the page is touched. Old index.html is kept
as index.html.bak.

The markdown must keep this shape per language (this is the format the
existing files already use):

    # Language Name — `steamcode`
    ...anything...
    ```
    short description
    ```
    ...anything...
    ```
    [p]full description in BBCode[/p]
    ```
"""

import json
import re
import sys
import pathlib

HERE = pathlib.Path(__file__).parent
PAGE = HERE / "index.html"
ASSETS = HERE / "assets"
SHORT_CAP = 300


def die(msg):
    print("\n  STOPPED: " + msg + "\n  index.html was not changed.\n")
    sys.exit(1)


def parse(md_text):
    langs = []
    for part in re.split(r"\n# ", md_text)[1:]:
        head, body = part.split("\n", 1)
        head = head.strip()
        m = re.match(r"^(.*?)\s+—\s+`([a-z]+)`$", head)
        if m:
            name, code = m.group(1).strip(), m.group(2)
        elif head.startswith("English"):
            name, code = "English (source)", "english"
        else:
            continue  # document title / prose headings
        blocks = re.findall(r"```\n(.*?)\n```", body, re.S)
        if len(blocks) < 2:
            die("'%s' has %d code blocks, expected 2 (short, then full)." % (head, len(blocks)))
        langs.append({"code": code, "name": name,
                      "short": blocks[0].strip(), "full": blocks[1].strip()})
    return langs


def structure(full):
    return re.findall(r"\[p\][\s\S]*?\[/p\]|\[h2\][\s\S]*?\[/h2\]|\[list\][\s\S]*?\[/list\]", full)


def main():
    args = [a for a in sys.argv[1:]]
    label = None
    if "--label" in args:
        i = args.index("--label")
        label = args[i + 1]
        del args[i:i + 2]
    if not args:
        die("give me the markdown file: python3 update-texts.py <file.md> [--label v2.6]")

    md_path = pathlib.Path(args[0])
    if not md_path.exists():
        die("no such file: %s" % md_path)
    if not PAGE.exists():
        die("index.html not found next to this script.")

    langs = parse(md_path.read_text(encoding="utf-8"))
    if not langs:
        die("found no language sections. Check the heading format: # Name — `code`")

    print("\n  %s\n" % md_path.name)

    # 1. short descriptions must fit Steam's field
    over = [l for l in langs if len(l["short"]) > SHORT_CAP]
    if over:
        die("short description too long: " +
            ", ".join("%s (%d chars)" % (l["code"], len(l["short"])) for l in over))

    # 2. every language must share the English block structure, or compare
    #    mode and the paragraph numbers in reviewers' notes stop lining up
    ref = structure(langs[0]["full"])
    for l in langs:
        n = len(structure(l["full"]))
        if n != len(ref):
            die("%s has %d paragraphs, %s has %d — they must match."
                % (l["code"], n, langs[0]["code"], len(ref)))

    # 3. referenced media must actually be in assets/
    missing = set()
    for l in langs:
        for name in re.findall(r"extras/([a-z0-9_]+)", l["full"], re.I):
            if not (ASSETS / (name.lower() + ".mp4")).exists():
                missing.add(name.lower())
    if missing:
        die("these clips are referenced but not in assets/: " + ", ".join(sorted(missing)) +
            "\n  add <name>.mp4 and <name>.jpg (poster frame) there first.")

    # 4. unknown BBCode would render as literal brackets on the page
    known = re.compile(r"\[/?(?:p|h2|list|\*|b|i|u|img[^\]]*)\]")
    for l in langs:
        odd = re.findall(r"\[[^\]]{0,30}\]", known.sub("", l["full"]))
        if odd:
            print("  ! %s uses tags the page does not render: %s" % (l["code"], ", ".join(sorted(set(odd)))))

    for l in langs:
        print("  %-11s short %3d/%d   paragraphs %d" %
              (l["code"], len(l["short"]), SHORT_CAP, len(structure(l["full"]))))

    # write
    page = PAGE.read_text(encoding="utf-8")
    (HERE / "index.html.bak").write_text(page, encoding="utf-8")

    data = json.dumps(langs, ensure_ascii=False)
    page, n = re.subn(r"const LANGS = .*?;\n", lambda m: "const LANGS = " + data + ";\n",
                      page, count=1, flags=re.S)
    if n != 1:
        die("could not find the 'const LANGS = ...' line in index.html.")

    if label:
        page, n = re.subn(r'const TEXT_VERSION = ".*?";',
                          lambda m: 'const TEXT_VERSION = "%s";' % label, page, count=1)
        if n != 1:
            print("  ! could not update the version label")

    PAGE.write_text(page, encoding="utf-8")
    print("\n  index.html updated — %d languages%s" % (len(langs), (", labelled " + label) if label else ""))
    print("  previous version saved as index.html.bak")
    print("  open index.html in a browser to check, then push.\n")


if __name__ == "__main__":
    main()
