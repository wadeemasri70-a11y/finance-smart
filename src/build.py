#!/usr/bin/env python3
"""Assemble every page from one set of shared parts, so the styles,
header, footer and translations exist in exactly one place."""
import io, re, os, json, glob

# GitHub Pages can only serve a branch root or /docs, so the finished pages go
# to the repository root and only the parts they are assembled from live here.
SRC  = os.path.dirname(os.path.abspath(__file__))
OUT  = os.path.dirname(SRC)
R = lambda f: io.open(os.path.join(SRC, f), encoding="utf-8").read()
W = lambda f, t: io.open(os.path.join(OUT, f), "w", encoding="utf-8").write(t)
# the artifact preview form is a build input for claude.ai, never a served page
WS = lambda f, t: io.open(os.path.join(SRC, f), "w", encoding="utf-8").write(t)

src   = R("body.html")
i18n  = R("i18n.json").strip()
# split at the LAST </style> before the symbol block, not the first: the page
# now has a font-face <style> ahead of the main stylesheet
MARK = '</style>\n\n<svg width="0"'
if MARK in src:
    i = src.index(MARK) + len('</style>')
else:
    i = src.index("</style>") + len("</style>")
head, rest = src[:i], src[i:]
symbol = re.search(r'<svg width="0".*?</svg>', rest, re.S).group(0)
header = re.search(r'<header class="top">.*?</header>', rest, re.S).group(0)
home   = re.search(r'<main id="start">.*?</main>', rest, re.S).group(0)
tail   = rest[rest.index('<div class="foot-rule"'):].replace("__I18N_DICT__", i18n)

DOC = ('<!doctype html>\n<html lang="de">\n<head>\n<meta charset="utf-8">\n'
       '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
       '<meta name="description" content="{desc}">\n{head}\n</head>\n<body>\n'
       '{symbol}\n{header}\n{main}\n{tail}\n</body>\n</html>\n')

def page(main, desc, sub):
    h = header
    if sub:                       # anchors on a subpage have to point back home
        h = re.sub(r'href="#(?!sfmark")([a-z-]+)"', r'href="index.html#\1"', h)
    t = tail
    if sub:
        t = re.sub(r'href="#(?!sfmark")([a-z-]+)"', r'href="index.html#\1"', t)
    return DOC.format(desc=desc, head=head, symbol=symbol, header=h, main=main, tail=t)

HOME_DESC = ("Buchhaltung, Lohnabrechnung, Controlling und Digitalisierung "
             "für kleine und mittelständische Unternehmen in Neuss.")
W("index.html", page(home, HOME_DESC, False))
# the artifact preview publishes a page WITHOUT its own doctype/head, so emit
# that form too - with the dictionary substituted, which body.html itself lacks
WS("artifact-page.html", head + "\n\n" + symbol + "\n" + header + "\n" + home + "\n" + tail)
built = ["index.html"]
for f in sorted(glob.glob(os.path.join(SRC, "pages", "*.html"))):
    body = R(os.path.join("pages", os.path.basename(f)))
    d = re.search(r'<!--\s*desc:\s*(.*?)\s*-->', body)
    desc = d.group(1) if d else ""
    main = re.search(r'<main.*?</main>', body, re.S).group(0)
    out = os.path.basename(f)
    W(out, page(main, desc, True))
    built.append(out)
for base, name in [(OUT, f) for f in built] + [(SRC, "artifact-page.html")]:
    if "__I18N_DICT__" in io.open(os.path.join(base, name), encoding="utf-8").read():
        raise SystemExit("BUILD FAILED: %s still contains the dictionary placeholder" % name)
print("built into %s: %s" % (OUT, ", ".join(built)))
