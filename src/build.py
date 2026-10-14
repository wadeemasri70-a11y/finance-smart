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

SITE = "https://www.smartfinance-nrw.de/"

DOC = ('<!doctype html>\n<html lang="de">\n<head>\n<meta charset="utf-8">\n'
       '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
       '<title>{title}</title>\n'
       '<meta name="description" content="{desc}">\n'
       '<link rel="canonical" href="{url}">\n'
       '<meta property="og:type" content="website">\n'
       '<meta property="og:locale" content="de_DE">\n'
       '<meta property="og:site_name" content="Smart Finance Consulting">\n'
       '<meta property="og:title" content="{title}">\n'
       '<meta property="og:description" content="{desc}">\n'
       '<meta property="og:url" content="{url}">\n'
       '<meta property="og:image" content="' + SITE + 'img/office-1000.jpg">\n'
       '<link rel="icon" href="favicon.svg" type="image/svg+xml">\n'
       '<link rel="icon" href="favicon.ico" sizes="any">\n'
       '<link rel="apple-touch-icon" href="img/icon-180.png">\n'
       '<link rel="manifest" href="site.webmanifest">\n'
       '<meta name="theme-color" content="#0E2235">\n{ld}{head}\n</head>\n<body>\n'
       '{symbol}\n{header}\n{main}\n{tail}\n</body>\n</html>\n')

# Google reads the business card from this block: name, address, phone and
# position match the Impressum and the Google Business Profile, so keep them
# in step when one of them changes.
LD = ('<script type="application/ld+json">' + json.dumps({
    "@context": "https://schema.org",
    "@type": "AccountingService",
    "@id": SITE + "#firma",
    "name": "Smart Finance Consulting",
    "url": SITE,
    "logo": SITE + "img/icon-512.png",
    "image": SITE + "img/office-1000.jpg",
    "description": "Buchhaltung, Lohnabrechnung, Controlling und Digitalisierung "
                   "für kleine und mittelständische Unternehmen in Neuss.",
    "telephone": "+49 2131 5398501",
    "email": "info@smartfinance-nrw.de",
    "address": {"@type": "PostalAddress", "streetAddress": "Mainstraße 26–30",
                "postalCode": "41469", "addressLocality": "Neuss",
                "addressRegion": "Nordrhein-Westfalen", "addressCountry": "DE"},
    "geo": {"@type": "GeoCoordinates", "latitude": 51.158264, "longitude": 6.736446},
    "hasMap": "https://maps.app.goo.gl/UEfZgx9Jsora8MZEA",
    "areaServed": ["Neuss", "Rhein-Kreis Neuss", "Düsseldorf"],
    "knowsLanguage": ["de", "en", "ar"],
}, ensure_ascii=False) + '</script>\n')

def page(main, desc, sub, title, name):
    h = header
    if sub:                       # anchors on a subpage have to point back home
        h = re.sub(r'href="#(?!sfmark")([a-z-]+)"', r'href="index.html#\1"', h)
    t = tail
    if sub:
        t = re.sub(r'href="#(?!sfmark")([a-z-]+)"', r'href="index.html#\1"', t)
    url = SITE if name == "index.html" else SITE + name
    hd = re.sub(r'<title>.*?</title>\n?', '', head, count=1)
    return DOC.format(desc=desc, title=title, url=url, ld="" if sub else LD,
                      head=hd, symbol=symbol, header=h, main=main, tail=t)

HOME_DESC = ("Buchhaltung, Lohnabrechnung, Controlling und Digitalisierung "
             "für kleine und mittelständische Unternehmen in Neuss.")
HOME_TITLE = "Buchhaltung, Lohn &amp; Controlling in Neuss | Smart Finance Consulting"
W("index.html", page(home, HOME_DESC, False, HOME_TITLE, "index.html"))
# the artifact preview publishes a page WITHOUT its own doctype/head, so emit
# that form too - with the dictionary substituted, which body.html itself lacks
WS("artifact-page.html", head + "\n\n" + symbol + "\n" + header + "\n" + home + "\n" + tail)
built = ["index.html"]
for f in sorted(glob.glob(os.path.join(SRC, "pages", "*.html"))):
    body = R(os.path.join("pages", os.path.basename(f)))
    d = re.search(r'<!--\s*desc:\s*(.*?)\s*-->', body)
    desc = d.group(1) if d else ""
    tt = re.search(r'<!--\s*title:\s*(.*?)\s*-->', body)
    title = tt.group(1) if tt else "Smart Finance Consulting"
    main = re.search(r'<main.*?</main>', body, re.S).group(0)
    out = os.path.basename(f)
    W(out, page(main, desc, True, title, out))
    built.append(out)
# robots.txt and sitemap.xml tell Google which pages exist; both are rebuilt
# with the pages so a new page can never be left out of the sitemap
W("robots.txt", "User-agent: *\nAllow: /\n\nSitemap: %ssitemap.xml\n" % SITE)
W("sitemap.xml", '<?xml version="1.0" encoding="UTF-8"?>\n'
  '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' +
  "".join("  <url><loc>%s</loc></url>\n" % (SITE if f == "index.html" else SITE + f)
          for f in built) + "</urlset>\n")
for base, name in [(OUT, f) for f in built] + [(SRC, "artifact-page.html")]:
    if "__I18N_DICT__" in io.open(os.path.join(base, name), encoding="utf-8").read():
        raise SystemExit("BUILD FAILED: %s still contains the dictionary placeholder" % name)
print("built into %s: %s" % (OUT, ", ".join(built)))
