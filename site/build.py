#!/usr/bin/env python3
"""Assemble every page from one set of shared parts, so the styles,
header, footer and translations exist in exactly one place."""
import io, re, os, json, glob

HERE = os.path.dirname(os.path.abspath(__file__))
R = lambda f: io.open(os.path.join(HERE, f), encoding="utf-8").read()
W = lambda f, t: io.open(os.path.join(HERE, f), "w", encoding="utf-8").write(t)

src   = R("body.html")
i18n  = R("i18n.json").strip()
head, rest = src.split("</style>", 1)
head += "</style>"
symbol = re.search(r'<svg width="0".*?</svg>', rest, re.S).group(0)
header = re.search(r'<header class="top">.*?</header>', rest, re.S).group(0)
home   = re.search(r'<main id="start">.*?</main>', rest, re.S).group(0)
tail   = rest[rest.index('<div class="nrw"'):].replace("__I18N_DICT__", i18n)

DOC = ('<!doctype html>\n<html lang="de">\n<head>\n<meta charset="utf-8">\n'
       '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
       '<meta name="description" content="{desc}">\n{head}\n</head>\n<body>\n'
       '{symbol}\n{header}\n{main}\n{tail}\n</body>\n</html>\n')

def page(main, desc, sub):
    h = header
    if sub:                       # anchors on a subpage have to point back home
        h = re.sub(r'href="#([a-z-]+)"', r'href="index.html#\1"', h)
    t = tail
    if sub:
        t = re.sub(r'href="#([a-z-]+)"', r'href="index.html#\1"', t)
    return DOC.format(desc=desc, head=head, symbol=symbol, header=h, main=main, tail=t)

HOME_DESC = ("Buchhaltung, Lohnabrechnung, Controlling und Digitalisierung "
             "für kleine und mittelständische Unternehmen in Neuss.")
W("index.html", page(home, HOME_DESC, False))
# the artifact preview publishes a page WITHOUT its own doctype/head, so emit
# that form too - with the dictionary substituted, which body.html itself lacks
W("artifact-page.html", head + "\n\n" + symbol + "\n" + header + "\n" + home + "\n" + tail)
built = ["index.html", "artifact-page.html"]
for f in sorted(glob.glob(os.path.join(HERE, "pages", "*.html"))):
    body = R(os.path.join("pages", os.path.basename(f)))
    d = re.search(r'<!--\s*desc:\s*(.*?)\s*-->', body)
    desc = d.group(1) if d else ""
    main = re.search(r'<main.*?</main>', body, re.S).group(0)
    out = os.path.basename(f)
    W(out, page(main, desc, True))
    built.append(out)
for f in built:
    if "__I18N_DICT__" in R(f):
        raise SystemExit("BUILD FAILED: %s still contains the dictionary placeholder" % f)
print("built:", ", ".join(built))
