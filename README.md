# California Inspector Group — demo site

Demo / pitch site for **California Inspector Group LLC** (Robert Lehman, statewide California),
built by [60 Minute Sites](https://60minutesites.com).

Static HTML. No build step required to deploy — serve the repo root.

> **This is a demo.** Every page carries `noindex,nofollow` and `robots.txt` disallows
> everything, so it cannot outrank the client's real site. The booking flow does not yet take
> money or signatures. Read `DEMO-NOTES.md` before this goes anywhere near a customer.

## The business, in one line

Two California inspection mandates, one firm:

| | Accessibility | Structural |
|---|---|---|
| Service | CASp — Certified Access Specialist inspections | SB 721 / SB 326 balcony inspections |
| Status | **Voluntary** — the shield you choose | **Mandatory** — the law you cannot skip |
| Why anyone buys | Unruh Act minimum damages are $4,000 per offence; a CASp report makes you a *qualified defendant* | Both first-round deadlines have already passed |
| Colour on site | blue | amber |

That split is the organising idea of the whole design — the two service lines are colour-coded
consistently through nav, cards, buttons, diagrams and CTAs.

## What's here

| | |
|---|---|
| Pages | 35 |
| Services | 6 detail pages + index |
| Service areas | 10 regional pages + a 58-county coverage page |
| Education | `/casp.html`, `/balcony-inspections.html` — the long-form pages that do the selling |
| Commerce | `/pricing.html`, `/book.html`, `/agreement.html`, `/portal.html` |
| Ad funnel | `/start.html` — 4-step quiz landing page for paid traffic |
| Other | home, about, process, FAQ, contact, thank-you, 404, sitemap |

## The commerce flow

The client wants customers to sign up, sign a contract, pay a deposit, schedule, and then
unlock the report on final payment. The front end for all of that is built:

1. **`/pricing.html`** — a published rate card. CASp priced by occupancy × floor area,
   SB 721 / SB 326 priced by unit count, plus a live calculator that reads from the same
   data as the printed table so the two cannot drift.
2. **`/book.html`** — a four-step wizard. Price → property and contact details →
   agreement consent → confirmation. Validated at each step; posts one JSON payload to the
   same Formspree endpoint as every other 60MS funnel.
3. **`/agreement.html`** — a plain-English walk through the twelve sections of the
   inspection agreement, so the client reads it before signing rather than after.
4. **`/portal.html`** — a demo client portal: engagement status timeline, invoices, and the
   report locked behind the outstanding balance. Click *Pay balance* to see it unlock.

**Nothing here takes real money or real signatures yet**, and the deposit step deliberately
renders no card fields at all — card capture belongs on the processor's hosted page. See
`DEMO-NOTES.md` for the integrations required.

## Design brief

There was no existing site and no logo, so the look was built from the subject matter:

- **Authority over friendliness.** This is a compliance purchase made under legal pressure.
  Deep navy `#0B1B2B`, accessibility blue `#1263B8`, structural amber `#B4661E`.
- **Diagram-led, not stock-led.** Most of the explanatory weight is carried by five authored
  inline SVG diagrams — the lawsuit timeline, the damages comparison, the path of travel, the
  balcony cross-section and the which-law decision tree. They out-perform stock photography
  for this subject, cost no extra requests, and stay sharp at any size.
- **The site practises what it sells.** Skip link, single `h1` per page, semantic landmarks,
  visible focus rings, `prefers-reduced-motion` honoured, AA-or-better contrast throughout,
  and every diagram carries a `<title>` and a full `<desc>`. A site about accessibility that
  fails an audit is an own goal.

Type is Archivo 800/900 over Inter.

## Local preview

```bash
python3 -m http.server 5083
```

Then open <http://localhost:5083>. (A `.claude/launch.json` entry named
`california-inspector-group` does the same thing.)

## Regenerating the pages

Every page shares one header and footer, so the HTML is generated rather than hand-edited:

```bash
python3 _generator/build.py
```

- `_generator/data.py` — business details, services, pricing, regions, FAQ, agreement terms
- `_generator/chrome.py` — `<head>`, nav, footer, CTA band, icon set
- `_generator/diagrams.py` — the five authored SVG diagrams
- `_generator/blocks.py` — reusable sections (cards, forms, FAQ, steps)
- `_generator/build.py` — one function per page
- `_generator/commerce.py` — pricing, booking, agreement and portal pages
- `_generator/start_page.py` — the paid-traffic funnel

Editing a generated `.html` directly works for a one-off tweak, but the next `build.py` run
overwrites it.

### Images

`_generator/fetch_images.py` and `fetch_categories.py` pull commercial-use candidates from
Wikimedia Commons into `_generator/raw/` (gitignored). `process_images.py` crops, colour-corrects
and compresses the shortlist into `assets/img/`. Credits are in `ATTRIBUTION.md`.

## Verification

The interactive pieces are covered by a 25-assertion harness run against headless Chrome —
calculator maths and deposit percentages, wizard step gating and validation, the absence of any
card or password field, and the portal's report gate. All passing at time of writing. There is
no horizontal overflow at 390px on any page, and no broken internal links across 2,170 refs.
