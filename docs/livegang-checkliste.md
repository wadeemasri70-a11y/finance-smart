# Go-live checklist

## 1. Google Maps (embedded map)

An artifact preview cannot embed other sites, so the page currently shows a
location card that links out to Google Maps. On the real domain, replace the
`<a class="loc-card">` block in `site/index.html` with this iframe:

```html
<iframe
  class="loc-card"
  title="Standort Smart Finance Consulting, Mainstraße 26–30, 41469 Neuss"
  src="https://www.google.com/maps?q=51.1582644,6.7364462&hl=de&z=17&output=embed"
  loading="lazy" referrerpolicy="no-referrer-when-downgrade"
  style="border:0" allowfullscreen></iframe>
```

Note for the privacy policy: the iframe contacts Google as soon as the page
loads. Either load it only after cookie consent, or keep the current
click-out card, which sends nothing to Google until the visitor clicks.

- Place: Smart Finance Consulting, Mainstraße 26–30, 41469 Neuss
- Coordinates: 51.1582644, 6.7364462
- Short link: https://maps.app.goo.gl/UEfZgx9Jsora8MZEA

## 2. Still to be supplied

| Item | Status |
|------|--------|
| Logo file (SVG or PNG) | **missing** – neither PDF contains one, so the site uses an "SF" mark built from the coin motif |
| Instagram / Facebook / LinkedIn URLs | **missing** – the footer icons currently point at `#` |
| Photos (owner, office) | **missing** – do not take these from the Google Maps listing unless you own them |
| Owner's name | placeholder in the texts |
| Name + website of the partner tax firm | placeholder in the texts |
| Impressum, Datenschutzerklärung | not written yet (legally required) |
| Contact form backend | the form validates but sends nothing yet |

## 3. WhatsApp

The header icon links to `https://wa.me/491629631605` (the mobile number from
the business card). Check that this number is actually on WhatsApp.

## 4. Fonts

Beatrix Antiqua and Garet from the business card are not free web fonts.
The site uses Cormorant Garamond (headings) and Outfit (body) from Google
Fonts. To keep the exact card fonts, a web licence has to be bought and the
files self-hosted.
