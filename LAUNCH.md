# Go-live runbook — California Inspector Group

Two builds exist:

```bash
python3 _generator/build.py          # demo (default): demo bar, noindex, robots disallow
python3 _generator/build.py --live   # launch: no demo bar, index,follow, robots allow
```

**Never push a `--live` build until every gate below passes.** The demo build is always safe.

---

## Gates before `--live` (content that is currently placeholder)

1. **Reviews are invented.** Remove or replace `REVIEWS` in `_generator/data.py` with real,
   permissioned quotes. Publishing them as genuine is an FTC violation. If Robert has no
   reviews yet, ship without the sections (delete the blocks) — an empty review page is
   worse than none.
2. **Pricing is invented.** Robert sets the real numbers in `CASP_RATES` / `EEE_RATES`.
3. **Credentials.** CASp certification number on /about + sample reports; resolve the SB 326
   signer question (licensed SE/architect) or pull that service page.
4. **Blog byline.** Robert reads and approves all six Field Notes articles — they speak as him.
5. **Contract.** The real inspection agreement exists (attorney-drafted).
6. **Domain in data.py.** Set `BIZ["base"]` to the real domain so canonicals/OG are right.
7. Swap `CALENDLY` to Robert's own calendar; decide Formspree endpoints vs 60MS CRM.

---

## GoDaddy domain → Netlify (the meeting script)

Do it with Robert on a screen-share; it is a 10-minute job. Two access options — prefer A:

- **A. Delegate access (professional, no passwords):** Robert: GoDaddy → Account Settings →
  **Delegate Access** → invite corbandamukaitis@gmail.com with "Products & Domains" access.
  You then manage his DNS from your own login, forever, without his password.
- B. He shares his screen and you dictate. Fine for a one-off.

Then, either path below. **Path 1 is recommended** — fewer moving parts, and if he ever has
email on this domain it can't break:

### Path 1 — keep GoDaddy DNS, point records at Netlify (recommended)
1. Netlify → the site → **Domain management → Add a domain you already own** → enter the
   domain. Netlify will show it as "awaiting external DNS".
2. GoDaddy → the domain → **DNS → Manage records**:
   - `A` record: Name `@` → Value `75.2.60.5` (Netlify's load balancer)
   - `CNAME`: Name `www` → Value `<sitename>.netlify.app`
   - Delete any old parked `A @` / `CNAME www` GoDaddy put there (the "Parked" A record).
3. Back in Netlify: wait for the checks to go green, then **Provision certificate**
   (Let's Encrypt, automatic). Set the primary domain (usually `www` or apex — pick one,
   Netlify redirects the other).
4. Propagation: usually minutes, occasionally up to an hour. `dig +short <domain>` to check.

### Path 2 — move DNS to Netlify (only if you want Netlify managing everything)
Netlify → Domain management → **Set up Netlify DNS** → it gives 4 nameservers
(`dns1–4.p0X.nsone.net`) → GoDaddy → domain → **Nameservers → Change → Custom** → paste.
⚠️ This moves ALL DNS. If the domain has email (MX records) or anything else, recreate those
records in Netlify DNS **before** switching nameservers — same lesson as the 60MS hyphenated
domain's email records.

### Don't forget
- The Netlify site name is currently `california-inspector-group.netlify.app` — it keeps
  working as a secondary URL after the custom domain attaches.
- If tomorrow is "domain only" (content still placeholder): attach the domain but **keep the
  demo build** (bar + noindex) until the gates pass. The domain resolving ≠ launched.

---

## Stripe (the promise is fine — here's the shape)

The site was built for exactly this: no card fields anywhere, checkout hands off to a hosted
page. Two phases:

### Phase 1 — live payments in ~1 hour, zero backend
1. **Robert creates the Stripe account** (his business, his EIN + bank — takes him ~15 min
   in Stripe onboarding). Never run client money through a 60MS Stripe account.
2. Robert invites you as a **team member (Developer role)** — you never need his password,
   and you never need to handle his API keys for this phase at all.
3. Create **Payment Links** in his dashboard:
   - "Inspection deposit" — customer-enters-amount (they type the deposit from their quote)
   - "Balance payment" — customer-enters-amount
   - Optionally fixed-price links per rate-card tier later.
4. Paste those URLs into the site: the checkout page's "Continue to secure payment" button
   and the booking flow. Money lands in Robert's bank. Done.

### Phase 2 — proper integration (when worth it)
Netlify Function creates a Checkout Session for the exact quoted amount; Stripe webhook
marks the engagement paid; that webhook is what should eventually drive the report gate
(server-side, never in the browser). Needs his **secret key in Netlify env vars only**
(Site settings → Environment variables) — never in the repo. ~a day of work when he's
generating real volume.

Card + ACH both work through either phase (enable ACH debit in his Stripe settings).
Wire stays invoice-based, as the site already says.
