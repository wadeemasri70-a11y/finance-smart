# Smart Finance Consulting: analysis of the website materials

Sources: `Smart_Finance_Consulting_Website_Texte_Agenda.pdf` (7 pages, as of 27.09.2026) and `Smart_Finance_3.pdf` (business card).

## 1. Existing content (texts PDF)

| # | Page | Headline | Content |
|---|-------|-------------|--------|
| 1 | Startseite (home) | „Ihre Zahlen. Ihre Systeme. Intelligent verbunden.“ | Services: Buchhaltung · Lohnabrechnung · Unternehmensberatung · Controlling · Digitalisierung. Sections: bookkeeping support + tax partner, service teasers, „Persönlich. Unternehmerisch. Digital.“ CTAs: „Erstgespräch vereinbaren“, „Unsere Leistungen kennenlernen“ |
| 2 | Leistungen: Buchhaltung & Lohn | „Verlässlich im kaufmännischen Alltag.“ | 5 points each for Buchhaltung and Lohnabrechnung, plus a box „Digitale Zusammenarbeit mit Agenda“ and a legal note |
| 3 | Leistungen: Beratung, Controlling, Digitalisierung | „Aus Zahlen werden Entscheidungen.“ | 5 points for Unternehmensberatung, 4 for Digitalisierung, 5 for Controlling |
| 4 | Digital arbeiten: Agenda | „Moderne Buchhaltung mit Agenda.“ | Belege digital, Bank/PayPal, Automatisierung, E-Rechnungen (XRechnung/ZUGFeRD), Archiv (InvoiceHub), Auswertungen Online |
| 5 | Datenaustausch & Sicherheit | „Gut verbunden. Sorgfältig organisiert.“ | Interfaces (GetMyInvoices, CSV import), bank/PayPal, security (data centre in Germany) |
| 6 | Über uns / Steuerpartner / Kontakt | „Persönlich beraten. Fachlich vernetzt.“ | Owner profile (diploma in economics), partner firm with 6 tax services, contact section |
| 7 | Editorial appendix | – | **Not for publication.** Sources [1]–[8] and to-dos |

## 2. Business card

- Phone: +49 2131 539 850 1 · Mobile: +49 162 963 160 5 (grouping as on the card; check against the original)
- E-mail: info@smartfinance-nrw.de · Domain: smartfinance-nrw.de
- Address: Mainstraße 26–30, 41469 Neuss
- Colors: navy `#132A3B`, gold `#CCAA67`, white
- Fonts: Beatrix Antiqua (serif, headings) + Garet (sans, body)
- (Values decoded by machine from the PDF; check against the original)

The texts PDF uses slightly different colors: `#123043` (navy), `#087C80` (petrol/teal), `#273E49`, `#627682`.

## 3. Still missing before go-live

1. Fill the placeholders: [Name des Inhabers], [Adresse], [Telefon], [E-Mail], [Name der Steuerberatungsgesellschaft] mbH, partner website.
2. **Impressum + Datenschutzerklärung** (required by law; not included yet).
3. Check the exact diploma title against the certificate.
4. Legal review under StBerG §§ 3, 6: Steuerberatung (tax advice) must be offered by the partner firm only.
5. Only promise Agenda functions that are actually set up. Agenda logo or partner badge only with permission.
6. Real photos (owner, office in Neuss).
7. Cookie banner and a GDPR-compliant contact form / appointment booking.

## 4. Proposed sitemap

- Startseite
- Leistungen
  - Buchhaltung & Lohn
  - Beratung & Controlling
  - Digitalisierung
- Digital arbeiten (Agenda, Datenaustausch & Sicherheit)
- Über uns (incl. Steuerberatung durch Partnergesellschaft)
- Kontakt / Erstgespräch
- Footer: Impressum · Datenschutz · Kontaktdaten · Öffnungszeiten

## 5. Design direction (proposal)

- Primary: navy `#132A3B`; accent: gold `#CCAA67` (matches the business card); optional secondary: teal `#087C80` for digital topics.
- Serif headings (Beatrix Antiqua or a web alternative such as Cormorant/Playfair) + a sans-serif body font.
- A regional touch for NRW/Neuss, e.g. through photography or a small green/white/red detail. **Do not use the official NRW coat of arms**: its use is legally restricted, and the site must not look like an authority (Finanzamt).

## 6. Analysis of the reference sites (28.09.2026)

**Competitors:** kalkuel, hksteuerberatung, skalar, axcon, limetax, integral
- Typical homepage order: Hero (promise + CTA „Kostenloses Erstgespräch“ + microcopy) → key figures/promises → services (5–6 cards, title + 1 sentence + 3 checkmarks) → collaboration model → 3-step process → Why us → team/founder → testimonials → tools/integrations → FAQ (6–9) → location + contact form.
- axcon and limetax: an explicit note that tax advice is provided only by the partner firm. This is exactly our model.
- Skalar: concrete promises and microcopy under the CTA. H&K: FAQ on the homepage. Kalkül: sticky mobile bar with „Anrufen / Erstgespräch“.

**Design references**
- Finanzamt Neuss: clear contact/hours block, info boxes, accessibility. Primary colour #233755.
- NRW coat of arms: a Hoheitszeichen whose use is not allowed for private companies (law of 10.03.1953). We use only a thin green/white/red line (#3F983E / #C1001F).
- Agenda: alternating text/image rows, checkmark lists, a recurring lead box. Colours #CF112D, font Milo.

## 7. Design tokens (draft `site/index.html`)
- Navy #132A3B · Gold #CCAA67 · Teal #087C80 · Surface #F3F5F7
- Headings: Cormorant Garamond (web alternative to Beatrix Antiqua) · Body: Outfit (alternative to Garet)
- Radius 4–6px, section spacing 64–112px, container 1180px
