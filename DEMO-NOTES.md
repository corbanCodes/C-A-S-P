# Demo notes — read before this goes live

Everything below is either test wiring, a placeholder, or a question only Robert can answer.
Ordered by what blocks launch soonest.

---

## 1. Blocking — things that are wrong until Robert confirms them

### Pricing is invented
The entire rate card in `_generator/data.py` (`CASP_RATES`, `EEE_RATES`) is **placeholder
numbers chosen to establish the structure**, not real prices. They are plausible for the
California market and internally consistent, but Robert has never seen them.

He described exactly the structure he wanted — sliding scale by square footage, broken down by
occupancy type (hotel / restaurant / retail), custom quote above that — so the shape should be
right. He sets the numbers. Change them in one place and both the table and the live calculator
update together.

The **20% deposit** is his stated figure and is used throughout.

### Credentials are not stated anywhere, deliberately
The site never claims a CASp certification number, a contractor licence number, or an engineer's
stamp, because we do not have them. Before launch, add:

- Robert's CASp certification number and its expiry (DSA certifies for three-year terms)
- Any contractor or building-inspector certification relied on for **SB 721** work
- **SB 326 is the one to watch.** That statute permits only a *licensed structural engineer or
  architect* — a certified building inspector does **not** qualify, unlike under SB 721.
  The site currently says "we staff these inspections accordingly" and the pricing page says the
  cost reflects it. If Robert does not have an SE or architect on the team, either name the
  partner firm or **pull the SB 326 service page**. Selling an inspection you cannot legally
  sign is the single largest risk on this site.

### Insurance limits
`/agreement.html` says the agreement states the general liability and professional liability
(E&O) cover carried. Get the real limits and the carrier, and put the numbers in the contract.

### The contract itself does not exist
Robert said he can get one quickly. `/agreement.html` is a **plain-English summary of twelve
sections we think it should contain** — it is not a contract and it is not legal advice.
A California attorney needs to draft the real one. Points worth briefing them on:

- The mandatory hazard-reporting term (section 7). Where an exterior elevated element is an
  immediate threat, the statutes require notice to the local enforcement agency within 15 days.
  Clients must acknowledge this up front; it cannot be contracted away.
- Third-party reliance. These reports get handed to courts, lenders, boards and buyers.
- Payment terms need to actually support the business model below — deposit non-refundable
  after scheduling, report released on cleared balance.

### Legal copy review
The site states statutes, damages figures, deadlines and cycles throughout. Everything was
researched against DSA, the California codes and current practitioner sources in **August 2026**,
and key claims carry their citation inline so they can be checked. Specifically verified:

- CASp / DSA programme, Civil Code §§55.51–55.54, §55.56, §55.53, §1938
- Unruh Act $4,000 minimum; $2,000 and $1,000 reductions; 120-day small-business grace period
- **SB 721** — Health & Safety Code §17973, first inspection **1 Jan 2026** (extended from 2025
  by **AB 2579**), then every 6 years, 15% sample
- **SB 326** — Civil Code §5551, first inspection **1 Jan 2025** (*not* extended by AB 2579),
  then every 9 years, licensed SE/architect only

**Both deadlines have now passed**, which the site uses as its main urgency hook. That is
factually true as of August 2026 and should be re-checked if this sits unlaunched for long.
Have counsel read it anyway — we are inspectors' marketing, not lawyers.

---

## 2. Integrations the commerce flow needs

The front end is complete; none of it is connected. Current behaviour is a single Formspree
POST with everything captured, which lands the lead in the CRM.

| Step | Now | Needs |
|---|---|---|
| Price | Live calculator, real maths | nothing |
| Book a demo | 60MS Calendly (`corban-leadsprinter/new-meeting`) popup | swap to Robert's own Calendly when he has one |
| Details | Validated, posts to Formspree `xojeqvng` | point at the 60MS HQ CRM endpoint |
| Checkout | `/checkout.html` example — method choice + billing contact to Formspree `mvzalyrw` | Stripe Checkout for card + ACH; wire stays invoice-based |
| E-signature | Consent checkboxes; confirmation screen says the agreement is on its way | DocuSign or Dropbox Sign; send template on submit, webhook on completion |
| Deposit | Explains methods; **renders no card fields** | Stripe Checkout / Payment Links (card + ACH). Never build card fields into this site |
| Scheduling | Confirmation says a calendar link follows | Cal.com or Calendly embed, ideally gated until the deposit clears |
| Report gate | `portal.js` unlocks client-side for the demo | Real auth + server-side gate. See the warning below |

### Two things to get right

**The report gate must be server-side.** `portal.js` flips the lock in the browser because it is
a demo. Anything the browser can unlock, a visitor can unlock. On the live site the PDF must be
served from behind authentication, released by the payment provider's webhook — never by a
client-side flag or a "secret" URL.

**Never accept card details on this site.** The deposit step hands off to the processor's hosted
page. That is the correct integration, it keeps the site out of PCI scope, and it means there is
no card form here for anyone to clone into a phishing page. The pricing page carries a matching
warning to clients that we will never email changed bank details — worth keeping, because wire
fraud against property-services firms is common and specifically targets this workflow.

### Business-model check for Robert
"Pay in full to unlock the report" is a real policy with a real edge case: if an inspection turns
up an immediate hazard, the statutory 15-day notification does **not** wait for an invoice.
`/portal.html` says so explicitly. Make sure the signed contract says it too.

---

## 3. Test wiring to swap out

- **Demo bar** — every page (funnel included) carries the top banner saying forms post to a
  test inbox and payments/e-signature are not connected. Remove it at launch (it is emitted
  by `demo_bar()` in `_generator/chrome.py` — delete the call in `head()` and rebuild).
- **Book a demo** — all `[data-calendly]` elements open Corban's 60MS Calendly. This is a
  placeholder calendar: replace `CALENDLY` in `_generator/data.py` with the client's own.
- **Forms** — every form and the funnel post to the 60MS Formspree endpoint `xojeqvng`;
  the example checkout posts to the 60MS checkout endpoint `mvzalyrw`.
  Page forms redirect to `/thank-you.html`; the funnel and booking wizard send JSON.
  Payload shape matches the other 60MS funnels so leads land in the CRM identically.
- **Contact widget** (`assets/js/contact-widget.js`) — self-contained Call / Text / Email dock.
  The real 60MS chat product drops in here once a tenant slug exists.
- **Meta pixel** — all `fbq` calls are `window.fbq`-guarded and no-op until a pixel is added.
  Events fire on quiz steps, `Lead`, and `Schedule` (with the quoted value) on booking.
- **`robots.txt` disallows everything** and every page carries `noindex,nofollow`.
  Remove both at launch or the site will never rank.
- **Domain** — canonical URLs assume `californiainspectorgroup.com`. Not registered as far as we
  know. Confirm with Robert, then update `BIZ["base"]` in `_generator/data.py`.
- **Phone and email** are Robert's real ones from the CRM (408-600-7165 /
  Roblehman72@gmail.com). A Gmail address on a compliance site undersells him — recommend a
  domain mailbox before launch.

---

## 4. Content still to get from the client

- **Photography.** All current images are CC-licensed Commons placeholders (see
  `ATTRIBUTION.md`). What this site actually needs is Robert on site with a level and a tape,
  real California storefronts, real balcony and walkway conditions, and a photo of him for the
  About page. For this business the photography is evidence of competence, not decoration.
- **Logo.** There isn't one. The current mark is a typographic "CIG" tile. It works, but a real
  logo would be better and the favicon is a placeholder shield.
- **Robert's biography.** `/about.html` says he spent a career as a municipal building inspector
  for California cities, which is what he told us — but no years, no city names, no specifics,
  because we have none. Get: how long, which jurisdictions, what he inspected. That paragraph is
  the single most persuasive thing on the site and it is currently the vaguest.
- **Proof.** No testimonials, no case studies, no client names, no report sample. A redacted
  sample report would be an excellent lead magnet for exactly this audience.
- **Turnaround time.** The site says five to seven business days. Confirm.
- **Scheduling lead time.** Area pages say "usually within two weeks". Confirm.
- **Consultation offer.** `/book.html` offers a free 15-minute consultation. Confirm he wants it.

---

## 5. Known small stuff

- Regional pages are thin by design — they exist for coverage and local search, not to be read.
  If Robert wants to compete on local SEO, they need genuine per-region content.
- No analytics installed.
- The 58-county list is complete and correct; the ten regional groupings are our invention for
  scheduling convenience, not an official taxonomy.
- FAQ JSON-LD is emitted on `/faq.html`, `/casp.html` and `/balcony-inspections.html`. Harmless
  while noindexed, correct the day it launches.
- `_generator/raw/` (≈190 candidate images, ~200 MB) is gitignored. Only the 14 processed images
  are committed.
