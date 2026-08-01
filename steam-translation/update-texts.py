#!/usr/bin/env python3
"""
Kayak Photography Sim — store text check page updater.

Usage:
    python3 update-texts.py <localization.md> [--label v2.6]

Reads the localization markdown, checks it, and writes it out twice:

  texts.md    the page fetches this at load time  <- this is what visitors see
  index.html  a baked-in copy, used only if texts.md cannot be fetched

Nothing else in the page is touched. Old index.html is kept as index.html.bak.

If you only replace texts.md by hand, the live page updates too. Running this
script keeps the fallback in sync and checks the file before you push.

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

    # 2. a language with a different paragraph count still works, but its
    #    compare view falls back to whole-text side by side
    ref = len(structure(langs[0]["full"]))
    odd_shape = [(l["code"], len(structure(l["full"]))) for l in langs
                 if len(structure(l["full"])) != ref]
    for code, n in odd_shape:
        print("  ! %s has %d paragraphs, %s has %d — compare mode will show it"
              "\n    side by side rather than paragraph by paragraph." % (code, n, langs[0]["code"], ref))

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

    if odd_shape:
        print("")
    for l in langs:
        n = len(l["short"])
        flag = "  <- close to the cap" if n > SHORT_CAP - 15 else ""
        print("  %-11s short %3d/%d   paragraphs %d%s" %
              (l["code"], n, SHORT_CAP, len(structure(l["full"])), flag))

    # write
    page = PAGE.read_text(encoding="utf-8")
    (HERE / "index.html.bak").write_text(page, encoding="utf-8")

    data = json.dumps(langs, ensure_ascii=False)
    page, n = re.subn(r"const LANGS_BAKED = .*?;\n", lambda m: "const LANGS_BAKED = " + data + ";\n",
                      page, count=1, flags=re.S)
    if n != 1:
        die("could not find the 'const LANGS_BAKED = ...' line in index.html.")

    if label:
        page, n = re.subn(r'(?:let|const) TEXT_VERSION = ".*?";',
                          lambda m: 'let TEXT_VERSION = "%s";' % label, page, count=1)
        if n != 1:
            print("  ! could not update the version label")

    PAGE.write_text(page, encoding="utf-8")
    source = md_path.read_text(encoding="utf-8")
    source = re.sub(r"^<!--\s*label:[^>]*-->\n*", "", source)
    if label:
        source = "<!-- label: %s -->\n\n%s" % (label, source)
    (HERE / "texts.md").write_text(source, encoding="utf-8")
    print("\n  updated — %d languages%s" % (len(langs), (", labelled " + label) if label else ""))
    print("    texts.md    what the live page reads")
    print("    index.html  fallback copy, used if texts.md cannot be fetched")
    print("  previous index.html saved as index.html.bak")
    print("  open index.html in a browser to check, then push.\n")


if __name__ == "__main__":
    main()
