# -*- coding: utf-8 -*-
"""Pricing, booking, agreement and client-portal pages.

The booking flow is a real front end: the price calculator computes from the
published rate card, and the details post to Formspree like every other form on
the site. The three steps that need a vendor — e-signature, payment and the
gated report — are staged as clearly-labelled hand-offs rather than fake
implementations. In particular the deposit step never renders a card field:
real card capture belongs on the processor's own hosted page, which is both the
correct integration and the reason there is nothing here to phish.
See DEMO-NOTES.md for what has to be wired before this takes money.
"""
import json

from data import (BIZ, SQFT_BANDS, CASP_RATES, EEE_RATES, PRICE_INCLUDES, PRICE_EXCLUDES,
                  CUSTOM_QUOTE, BOOK_STEPS, AGREEMENT_TERMS, PAY_METHODS, FORM_ACTION,
                  CHECKOUT_ACTION)
from chrome import head, foot, cta, svg, demo_btn, TEL, PH, EM
from blocks import img, phead, quote_form, review_pull
from data import REVIEWS


# --------------------------------------------------------------- rate table

def _rate_table():
    head_cells = "".join("<th>%s sq ft</th>" % b for b in SQFT_BANDS)
    rows = []
    for name, icon, blurb, prices in CASP_RATES:
        cells = "".join(
            '<td class="%s">%s</td>' % ("q" if p == "Quote" else "p", p) for p in prices)
        rows.append('<tr><th scope="row"><b>%s</b><small>%s</small></th>%s</tr>'
                    % (name, blurb, cells))
    return """
<div class="tw">
 <table class="rate">
  <caption class="hp">CASp inspection prices by occupancy type and floor area</caption>
  <thead><tr><th scope="col">Occupancy</th>%s</tr></thead>
  <tbody>%s</tbody>
 </table>
</div>""" % (head_cells, "".join(rows))


def _eee_table():
    rows = "".join('<tr><th scope="row">%s</th><td class="%s">%s</td></tr>'
                   % (band, "q" if price == "Quote" else "p", price)
                   for band, price in EEE_RATES)
    return """
<div class="tw">
 <table class="rate">
  <caption class="hp">SB 721 and SB 326 inspection prices by unit count</caption>
  <thead><tr><th scope="col">Building size</th><th scope="col">Price per building</th></tr></thead>
  <tbody>%s</tbody>
 </table>
</div>""" % rows


# ------------------------------------------------------------------ pricing

def build_pricing(write):
    body = phead(
        "Published pricing",
        "Most inspections fit a standard occupancy and footprint, so the price is on the "
        "board rather than behind a phone call. Anything larger or stranger gets a quote.",
        [("Home", "/index.html"), ("Pricing", None)]) + """
<section>
 <div class="wrap">
  <div class="note note-a">
   <b>Why we publish prices at all.</b>
   Most inspection firms will not. It makes budgeting impossible and it wastes a call
   working out whether you are in the same ballpark. If your building fits one of the
   categories below, that is the price.
  </div>

  <div class="sec-head" style="margin-top:2.6rem">
   <span class="eyebrow eyebrow-a">{ic_s} Accessibility</span>
   <h2>CASp inspection &mdash; by occupancy and floor area</h2>
   <p>One building, one tenant space, inspected and reported. Travel anywhere in California
    is included in these figures.</p>
  </div>
  {rate}

  <div class="sec-head" style="margin-top:3.4rem">
   <span class="eyebrow eyebrow-s">{ic_al} Structural</span>
   <h2>SB 721 &amp; SB 326 balcony inspection &mdash; by unit count</h2>
   <p>Priced per building on the number of dwelling units, because that is what drives the
    number of exterior elevated elements in the sample.</p>
  </div>
  {eee}
  <p class="form-note" style="margin-top:.9rem">SB 326 inspections are performed by a licensed
   structural engineer or architect as the statute requires; that is reflected in the pricing
   above rather than added later.</p>
 </div>
</section>

<section class="sec-paper">
 <div class="wrap">
  <div class="sec-head"><h2>Work out your price</h2>
   <p class="lede">Pick what you have. The calculator reads straight off the rate card above.</p></div>

  <div class="calc" id="calc">
   <div class="calc-in">
    <div class="field">
     <label for="c-line">What do you need?</label>
     <select id="c-line">
      <option value="casp">CASp accessibility inspection</option>
      <option value="eee">SB 721 / SB 326 balcony inspection</option>
     </select>
    </div>
    <div class="field" id="c-occ-field">
     <label for="c-occ">Occupancy type</label>
     <select id="c-occ">{occ_opts}</select>
    </div>
    <div class="field" id="c-sqft-field">
     <label for="c-sqft">Approximate floor area</label>
     <select id="c-sqft">{sqft_opts}</select>
    </div>
    <div class="field" id="c-units-field" hidden>
     <label for="c-units">Dwelling units in the building</label>
     <select id="c-units">{unit_opts}</select>
    </div>
   </div>

   <div class="calc-out" id="calc-out" aria-live="polite">
    <p class="calc-label">Your inspection</p>
    <p class="calc-price" id="calc-price">$895</p>
    <p class="calc-sub" id="calc-sub">Retail &amp; storefront, up to 1,500 sq ft</p>
    <hr>
    <p class="calc-dep">Deposit to book <b id="calc-dep">$179</b> <span>20% &mdash; balance due on completion</span></p>
    <a class="btn btn-solid btn-full" href="/book.html" id="calc-go">Book this inspection {ic_a}</a>
   </div>
  </div>
  {rev}
 </div>
</section>

<section>
 <div class="wrap">
  <div class="split top">
   <div>
    <h2>What the price includes</h2>
    <ul class="checks">{inc}</ul>
   </div>
   <div>
    <h2>What it does not</h2>
    <div class="rows">{exc}</div>
   </div>
  </div>
 </div>
</section>

<section class="sec-paper">
 <div class="wrap">
  <div class="sec-head"><h2>When it goes to a quote instead</h2>
   <p class="lede">California being California, a great many jobs are not one building. Those
    are priced as a package, and the package is nearly always cheaper than the sum of its
    parts.</p></div>
  <div class="grid g4">{custom}</div>
  <div class="note note-s" style="margin-top:2rem">
   <b>One owner, many buildings, one inspector.</b>
   A franchise operator with sites across the state, or a management company with a portfolio,
   should not be buying inspections one at a time from a different vendor in every county.
   Tell us the whole list and we will price the whole list.
  </div>
  <p style="margin-top:1.6rem"><a class="btn btn-solid btn-lg" href="/contact.html">Get a portfolio quote {ic_a}</a></p>
 </div>
</section>

<section>
 <div class="wrap">
  <div class="sec-head"><h2>How payment works</h2>
   <p class="lede">Twenty per cent on signing confirms the booking &mdash; and funds the
    mobilisation, which is how one inspector covers all 58 counties. The balance falls due
    when the report is complete, and paying it releases the signed PDF on the spot.</p></div>
  <div class="grid g3">{pay}</div>
  <div class="note note-a" style="margin-top:1.8rem">
   <b>Our terms are the terms.</b>
   No net-30, no net-anything, and no retention &mdash; whatever your accounts-payable
   process usually asks of vendors. We are told how developers operate; we decline. The
   deposit gets us to your property, the report is finished work, and finished work is paid
   for on delivery. If that does not fit your organisation, we are genuinely not the right
   fit &mdash; no hard feelings.
  </div>
  <p style="margin:1.6rem 0 0"><a class="btn btn-soft" href="/checkout.html">See the example checkout {ic_a}</a></p>
  <div class="note note-warn" style="margin-top:1.6rem">
   <b>We will never email you changed bank details.</b>
   Wire fraud in construction and property services works by sending a convincing message
   saying the account has changed. If you ever receive one that appears to be from us, do not
   act on it &mdash; call {ph} and confirm.
  </div>
 </div>
</section>

{cta}
""".format(
        ic_s=svg("shield"), ic_al=svg("alert"), ic_a=svg("arrow"), ph=PH,
        rate=_rate_table(), eee=_eee_table(),
        rev=review_pull(next(r for r in REVIEWS if "price was the price" in r["q"])),
        occ_opts="".join('<option value="%d">%s</option>' % (i, n.replace("&amp;", "&"))
                         for i, (n, _, _, _) in enumerate(CASP_RATES)),
        sqft_opts="".join('<option value="%d">%s sq ft</option>' % (i, b)
                          for i, b in enumerate(SQFT_BANDS)),
        unit_opts="".join('<option value="%d">%s</option>' % (i, b)
                          for i, (b, _) in enumerate(EEE_RATES)),
        inc="".join('<li>%s<span>%s</span></li>' % (svg("check"), t) for t in PRICE_INCLUDES),
        exc="".join('<div class="row"><h3>%s</h3><p>%s</p></div>' % (t, d)
                    for t, d in PRICE_EXCLUDES),
        custom="".join('<div class="card"><div class="card-ic">%s</div><h3>%s</h3><p>%s</p></div>'
                       % (svg("tag"), t, d) for t, d in CUSTOM_QUOTE),
        pay="".join('<div class="card"><div class="card-ic">%s</div><h3>%s</h3><p>%s</p></div>'
                    % (svg(ic), t, d) for t, ic, d in PAY_METHODS),
        cta=cta("Ready to put it on the calendar?",
                "Book online in about four minutes: pick your price, sign the agreement, pay "
                "the deposit and choose your date."),
    )

    rates = {
        "casp": [[p for p in prices] for _, _, _, prices in CASP_RATES],
        "caspNames": [n.replace("&amp;", "&") for n, _, _, _ in CASP_RATES],
        "bands": SQFT_BANDS,
        "eee": [p for _, p in EEE_RATES],
        "eeeNames": [b for b, _ in EEE_RATES],
    }
    script = ('<script>window.CIG_RATES=%s;</script>'
              '<script src="/assets/js/calculator.js" defer></script>' % json.dumps(rates))

    write("pricing.html", head(
        "Pricing | CASp &amp; SB 721 / SB 326 Inspections | California Inspector Group",
        "Published prices for CASp accessibility inspections by occupancy and floor area, and "
        "SB 721 / SB 326 balcony inspections by unit count. 20% deposit to book.",
        "/pricing.html") + body + script + foot())


# ------------------------------------------------------------------ booking

def build_book(write):
    steps = "".join(
        '<div class="bstep"><div class="bstep-n">%d</div><div class="bstep-ic">%s</div>'
        '<h3>%s</h3><p>%s</p></div>' % (i + 1, svg(ic), t, d)
        for i, (t, d, ic) in enumerate(BOOK_STEPS))

    body = phead(
        "Book an inspection",
        "Price, agreement, deposit and date &mdash; the whole booking runs here. It takes "
        "about four minutes and you do not need to speak to anybody unless you want to.",
        [("Home", "/index.html"), ("Book", None)]) + """
<section class="tight">
 <div class="wrap">
  <div class="bsteps">{steps}</div>
 </div>
</section>

<section class="sec-paper">
 <div class="wrap">
  <div class="wiz-grid">
  <div class="wiz" id="wiz">
   <div class="wiz-rail" aria-hidden="true">
    <i class="on" data-w="1"></i><i data-w="2"></i><i data-w="3"></i><i data-w="4"></i>
   </div>

   <!-- 1. price -->
   <div class="wstep on" data-step="1">
    <p class="qnum">Step 1 of 4</p>
    <h2>What are we inspecting?</h2>
    <div class="fgrid">
     <div class="field full">
      <label for="w-line">Inspection type</label>
      <select id="w-line">
       <option value="casp">CASp accessibility inspection</option>
       <option value="eee">SB 721 / SB 326 balcony inspection</option>
       <option value="both">Both &mdash; mixed-use property</option>
       <option value="quote">Multiple buildings or a portfolio</option>
      </select>
     </div>
     <div class="field" id="w-occ-field">
      <label for="w-occ">Occupancy type</label>
      <select id="w-occ">{occ_opts}</select>
     </div>
     <div class="field" id="w-sqft-field">
      <label for="w-sqft">Approximate floor area</label>
      <select id="w-sqft">{sqft_opts}</select>
     </div>
     <div class="field" id="w-units-field" hidden>
      <label for="w-units">Dwelling units</label>
      <select id="w-units">{unit_opts}</select>
     </div>
    </div>

    <div class="wiz-price" id="w-price-box" aria-live="polite">
     <div><span>Estimated fee</span><b id="w-price">$895</b></div>
     <div><span>Deposit to book (20%)</span><b id="w-dep">$179</b></div>
     <p id="w-price-note">Rate-card estimate. Robert reviews your photos and description and
      confirms the final fee with the agreement.</p>
    </div>

    <button type="button" class="btn btn-solid btn-lg btn-full wnext" data-next="2">
     Continue {ic_a}</button>
   </div>

   <!-- 2. details -->
   <div class="wstep" data-step="2">
    <p class="qnum">Step 2 of 4</p>
    <h2>The project, in your words and your photos</h2>
    <p style="font-size:.93rem">For every job, we ask for photos and your best description of
     the property. Robert reviews both and confirms your estimate &mdash; usually the same
     business day, before anything is signed or paid.</p>
    <div class="fgrid">
     <div class="field"><label for="w-name">Your name <span class="req">*</span></label>
      <input id="w-name" type="text" autocomplete="name"></div>
     <div class="field"><label for="w-company">Company or association</label>
      <input id="w-company" type="text" autocomplete="organization"></div>
     <div class="field"><label for="w-email">Email <span class="req">*</span></label>
      <input id="w-email" type="email" autocomplete="email"></div>
     <div class="field"><label for="w-phone">Phone <span class="req">*</span></label>
      <input id="w-phone" type="tel" autocomplete="tel"></div>
     <div class="field full"><label for="w-addr">Property address <span class="req">*</span></label>
      <input id="w-addr" type="text" autocomplete="street-address" placeholder="Street, city, county"></div>
     <div class="field full"><label for="w-notes">Describe the project <span class="req">*</span></label>
      <textarea id="w-notes" placeholder="Best description you can give: what the property is, roughly when it was built, how many balconies / walkways / stairs, access arrangements, deadlines, whether you have been served."></textarea></div>
     <div class="field full">
      <label for="w-photos">Photos of the property <span style="font-weight:400;color:var(--mute)">&mdash; please add for every job</span></label>
      <label class="upl" for="w-photos">
       <input id="w-photos" type="file" accept="image/*" multiple>
       {ic_cam}<span><b>Add photos</b> &mdash; balconies, walkways, entrances, parking; whatever
        we should see before we quote.</span>
      </label>
      <div class="upl-list" id="w-photo-list" hidden></div>
      <p class="form-note">Robert looks at your photos before confirming the number, so the
       estimate you get is a real one. If the property differs materially from what is
       described or shown, the fee is re-quoted on site before the inspection proceeds.</p>
     </div>
    </div>
    <p class="qerr" id="w-err" role="alert">Please add your name, a valid phone number, an
     email, the property address and a short description of the project.</p>
    <button type="button" class="btn btn-solid btn-lg btn-full wnext" data-next="3">Continue {ic_a}</button>
    <button type="button" class="qback" data-back="1">&larr; Back</button>
   </div>

   <!-- 3. agreement -->
   <div class="wstep" data-step="3">
    <p class="qnum">Step 3 of 4</p>
    <h2>The inspection agreement</h2>
    <p>We send this for electronic signature the moment you submit. It covers scope,
     exclusions, insurance, liability, confidentiality and payment terms &mdash;
     <a href="/agreement.html">read what is in it</a> before you sign, not after.</p>

    <div class="wiz-doc">
     <div class="wiz-doc-ic">{ic_doc}</div>
     <div>
      <b>Inspection Services Agreement</b>
      <span>California Inspector Group LLC &mdash; 12 sections, about 4 pages</span>
     </div>
     <a class="btn btn-line" href="/agreement.html">Preview</a>
    </div>

    <label class="wcheck"><input type="checkbox" id="w-esign">
     <span>I consent to sign and receive documents electronically under the federal ESIGN Act
      and the California Uniform Electronic Transactions Act.</span></label>
    <label class="wcheck"><input type="checkbox" id="w-ack">
     <span>I understand that where an exterior elevated element poses an immediate threat to
      safety, California Inspector Group is required by statute to notify the local
      enforcement agency within 15 days.</span></label>

    <p class="qerr" id="w-err2" role="alert">Please tick both boxes to continue.</p>
    <button type="button" class="btn btn-solid btn-lg btn-full wnext" data-next="4">
     Send me the agreement {ic_a}</button>
    <button type="button" class="qback" data-back="2">&larr; Back</button>
   </div>

   <!-- 4. deposit + schedule -->
   <div class="wstep" data-step="4">
    <div class="wiz-done">
     <div class="qtick">{ic_ck}</div>
     <h2>Sent &mdash; check your email</h2>
     <p>The agreement is on its way to <b id="w-echo">you</b>. Here is what happens next.</p>
    </div>

    <ol class="wnext-list">
     <li><b>We confirm your fee.</b> Robert reviews the photos and description you just sent
      and the agreement arrives with the confirmed number &mdash; usually the same business
      day.</li>
     <li><b>Sign the agreement.</b> Two minutes on a phone. Nothing is charged at this point.</li>
     <li><b>Pay the <span id="w-dep2">the deposit</span> deposit.</b> Signing releases a secure
      payment link &mdash; card, ACH or wire. This is what holds your date.
      <a href="/checkout.html">See the example checkout &rarr;</a></li>
     <li><b>Pick your date.</b> The confirmation email carries a live calendar of our
      availability in your region.</li>
     <li><b>We inspect, then you settle the balance</b> and the signed PDF report unlocks in
      your <a href="/portal.html">client portal</a>.</li>
    </ol>

    <div class="wiz-pay">
     <p class="calc-label">Payment methods</p>
     <div class="paylist">{pays}</div>
     <p class="form-note">Card and bank details are only ever entered on our payment
      provider&rsquo;s own secure page. We never take card numbers by phone, by email, or on
      this site &mdash; and nobody legitimate ever will.</p>
    </div>

    <p style="margin-top:1.6rem">
     <a class="btn btn-line btn-lg" href="/index.html">Back to the site</a>
     <a class="btn btn-ghost btn-lg" href="tel:{tel}">{ic_p} {ph}</a>
    </p>
   </div>
  </div>

  <aside class="wiz-side">
   <div class="pcard">
    <h3>Not sure yet? Book a demo</h3>
    <p>Fifteen minutes on a call. We will tell you which mandate applies to your property,
     what it costs, and whether you need an inspection at all.</p>
    {demo_side}
   </div>
   {side_rev}
   <div class="pcard">
    <h3>Rather just talk to someone?</h3>
    <p>Portfolios, franchise rollouts and anything where you have already been served are
     better handled on a call.</p>
    <a class="btn btn-line btn-full" href="tel:{tel}">{ic_p} {ph}</a>
    <a class="btn btn-ghost btn-full" href="/contact.html" style="margin-top:.4rem">Send the details instead</a>
   </div>
  </aside>
  </div>
 </div>
</section>

{cta}
""".format(
        steps=steps, ic_a=svg("arrow"), ic_p=svg("phone"), ic_doc=svg("doc"),
        demo_side=demo_btn(cls="btn btn-solid btn-full"),
        ic_cam=svg("camera"),
        side_rev=review_pull(next(r for r in REVIEWS if "binder" in r["q"])),
        ic_ck='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" '
              'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20 6L9 17l-5-5"/></svg>',
        tel=TEL, ph=PH,
        occ_opts="".join('<option value="%d">%s</option>' % (i, n.replace("&amp;", "&"))
                         for i, (n, _, _, _) in enumerate(CASP_RATES)),
        sqft_opts="".join('<option value="%d">%s sq ft</option>' % (i, b)
                          for i, b in enumerate(SQFT_BANDS)),
        unit_opts="".join('<option value="%d">%s</option>' % (i, b)
                          for i, (b, _) in enumerate(EEE_RATES)),
        pays="".join('<div class="payitem">%s<div><b>%s</b><span>%s</span></div></div>'
                     % (svg(ic), t, d) for t, ic, d in PAY_METHODS),
        cta=cta(),
    )

    rates = {
        "casp": [[p for p in prices] for _, _, _, prices in CASP_RATES],
        "caspNames": [n.replace("&amp;", "&") for n, _, _, _ in CASP_RATES],
        "bands": SQFT_BANDS,
        "eee": [p for _, p in EEE_RATES],
        "eeeNames": [b for b, _ in EEE_RATES],
        "form": FORM_ACTION,
    }
    script = ('<script>window.CIG_RATES=%s;</script>'
              '<script src="/assets/js/booking.js" defer></script>' % json.dumps(rates))

    write("book.html", head(
        "Book an Inspection | California Inspector Group",
        "Book a CASp or SB 721 / SB 326 inspection online: get your price, sign the agreement "
        "electronically, pay a 20% deposit and pick your date.",
        "/book.html") + body + script + foot())


# ---------------------------------------------------------------- agreement

def build_agreement(write):
    rows = "".join('<div class="row"><h3>%d. %s</h3><p>%s</p></div>' % (i + 1, t, d)
                   for i, (t, d) in enumerate(AGREEMENT_TERMS))
    body = phead(
        "The inspection agreement",
        "What you are signing, section by section, before you sign it rather than after. "
        "It runs to about four pages.",
        [("Home", "/index.html"), ("The agreement", None)]) + """
<section>
 <div class="wrap">
  <div class="split">
   <div>
    <h2>Why there is a contract at all</h2>
    <p>An inspection report gets used by people who were not in the room &mdash; a court, a
     lender, an insurer, a board, a buyer. The agreement is what makes it clear who the report
     was written for, what it covers, what it deliberately does not cover, and who carries
     which risk.</p>
    <p>It also protects you. It fixes the price, states the insurance we carry, sets out when
     the deposit is refundable, and commits us to a scope you can hold us to.</p>
    <div class="note note-a">
     <b>Read section 7 in particular.</b>
     Where an exterior elevated element poses an immediate threat to safety, we are required
     by statute to notify the local enforcement agency within 15 days. That is not a term we
     can negotiate away, and anybody offering to is telling you something useful about how
     they work.
    </div>
   </div>
   <div class="split-media">{im}</div>
  </div>
 </div>
</section>

<section class="sec-paper">
 <div class="wrap">
  <div class="sec-head"><h2>What is in it</h2>
   <p class="lede">Twelve sections. None of them are surprising, which is rather the
    point.</p></div>
  <div class="rows">{rows}</div>
 </div>
</section>

<section>
 <div class="wrap">
  <div class="grid g3">
   <div class="card"><div class="card-ic">{ic_sign}</div><h3>Signed electronically</h3>
    <p>Sent to your email, signed on a phone in about two minutes. Valid under the federal
     ESIGN Act and California&rsquo;s Uniform Electronic Transactions Act.</p></div>
   <div class="card"><div class="card-ic">{ic_sc}</div><h3>Nothing charged to sign</h3>
    <p>Signing costs nothing. The deposit link comes afterwards, and the booking is not held
     until it is paid.</p></div>
   <div class="card"><div class="card-ic">{ic_lock}</div><h3>Your copy, kept</h3>
    <p>A countersigned PDF lands in your inbox and stays in your client portal alongside the
     report.</p></div>
  </div>
  <div class="note" style="margin-top:2rem">
   <b>This page is a plain-English summary.</b>
   The agreement itself is the operative document, and where the two differ the agreement
   governs. Nothing here is legal advice &mdash; if the terms matter to you, and on a
   commercial engagement they should, have your own counsel read it.
  </div>
 </div>
</section>

{cta}
""".format(im=img("commercial-street", "A California main-street commercial building"),
           rows=rows, ic_sign=svg("sign"), ic_sc=svg("scale"), ic_lock=svg("lock"),
           cta=cta("Start the booking",
                   "Pick your price, get the agreement sent over, and hold a date."))
    write("agreement.html", head(
        "The Inspection Agreement | California Inspector Group",
        "A plain-English summary of the inspection services agreement: scope, exclusions, "
        "standard of care, insurance, liability, mandatory hazard reporting and payment terms.",
        "/agreement.html") + body + foot())


# ------------------------------------------------------------------- portal

def build_portal(write):
    body = phead(
        "Client portal",
        "Where your engagement lives: the signed agreement, the status of the inspection, "
        "your invoices and &mdash; once the balance is settled &mdash; the report.",
        [("Home", "/index.html"), ("Client portal", None)]) + """
<section>
 <div class="wrap">
  <div class="demo-flag">
   {ic_al}
   <div><b>Demonstration view</b>
    <p>This is a sample engagement showing how the portal behaves. On the live site it sits
     behind a login and shows your own properties.</p></div>
  </div>

  <div class="portal">
   <div class="portal-main">
    <div class="pcard">
     <div class="pcard-head">
      <div>
       <p class="calc-label">Engagement CIG-2026-0418</p>
       <h2>1420 Alisal Street, Salinas &mdash; Monterey County</h2>
       <p class="pmeta">Retail &amp; storefront &middot; 2,180 sq ft &middot; CASp property inspection</p>
      </div>
      <span class="pstat pstat-wait">Balance due</span>
     </div>

     <ol class="ptrack">
      <li class="done"><b>Agreement signed</b><span>14 April 2026</span></li>
      <li class="done"><b>Deposit paid &mdash; $230.00</b><span>14 April 2026 &middot; Visa &bull;&bull;&bull;&bull; 4242</span></li>
      <li class="done"><b>Inspection completed</b><span>28 April 2026 &middot; R. Lehman</span></li>
      <li class="done"><b>Report written</b><span>5 May 2026 &middot; 34 findings, 6 priority</span></li>
      <li class="now"><b>Balance due &mdash; $920.00</b><span>Settle to release the report</span></li>
      <li><b>Report released</b><span>Available immediately on payment</span></li>
     </ol>
    </div>

    <div class="pcard preport" id="preport">
     <div class="plock" id="plock">
      <div class="plock-ic">{ic_lock}</div>
      <div class="plock-txt">
       <b>CASp Inspection Report &mdash; 1420 Alisal Street</b>
       <span id="plock-sub">Locked &middot; PDF, 42 pages, 118 photographs</span>
      </div>
      <button type="button" class="btn btn-solid" id="ppay">Pay balance $920.00</button>
     </div>
     <div class="pfiles" id="pfiles" hidden>
      <a class="pfile" href="#" data-demo>{ic_doc}<div><b>CASp Inspection Report.pdf</b><span>42 pages &middot; 4.1 MB</span></div></a>
      <a class="pfile" href="#" data-demo>{ic_doc}<div><b>Schedule of Completion.pdf</b><span>3 pages &middot; 240 KB</span></div></a>
      <a class="pfile" href="#" data-demo>{ic_doc}<div><b>Photograph set.zip</b><span>118 images &middot; 96 MB</span></div></a>
      <a class="pfile" href="#" data-demo>{ic_doc}<div><b>Disability Access Inspection Certificate.pdf</b><span>1 page &middot; 88 KB</span></div></a>
     </div>
    </div>

    <div class="pcard">
     <h3>Documents</h3>
     <div class="pfiles">
      <a class="pfile" href="/agreement.html">{ic_doc}<div><b>Inspection Services Agreement (signed)</b><span>Countersigned 14 April 2026</span></div></a>
      <a class="pfile" href="#" data-demo>{ic_doc}<div><b>Invoice CIG-2026-0418-A &mdash; deposit</b><span>Paid 14 April 2026</span></div></a>
      <a class="pfile" href="#" data-demo>{ic_doc}<div><b>Invoice CIG-2026-0418-B &mdash; balance</b><span>Outstanding &middot; $920.00</span></div></a>
     </div>
     <p class="note" id="pdemo-note" hidden style="margin-top:1.2rem">
      These are sample documents on a demonstration page, so there is nothing behind the link.
      On the live portal each one is a real file served only to the signed-in client.</p>
    </div>
   </div>

   <aside class="portal-side">
    <div class="pcard">
     <h3>Next inspection due</h3>
     <p class="pdue">April 2029</p>
     <p class="form-note">We diarise your cycle and write to you ninety days before it falls
      due, so the date never arrives as a surprise.</p>
    </div>
    <div class="pcard">
     <h3>Your inspector</h3>
     <p><b>Robert Lehman</b><br><span class="pmeta">California Inspector Group LLC</span></p>
     <a class="btn btn-line btn-full" href="tel:{tel}">{ic_p} {ph}</a>
    </div>
    <div class="pcard">
     <h3>Add a property</h3>
     <p>Running more than one building? Add them here and they go on one calendar and one
      invoice.</p>
     <a class="btn btn-solid btn-full" href="/book.html">Book another {ic_a}</a>
    </div>
   </aside>
  </div>
 </div>
</section>

<section class="sec-paper">
 <div class="wrap">
  <div class="sec-head center"><h2>Why the report is gated</h2></div>
  <div class="narrow center">
   <p>It is not leverage. An inspection report is the entire deliverable &mdash; once it is
    handed over there is nothing left to withhold, and chasing a balance afterwards means
    either writing it off or sending a client to collections over work that was done properly.
    A 20% deposit and a settled balance on release keeps that conversation from ever
    happening.</p>
   <p>Payment releases the report the moment it clears &mdash; the signed PDF unlocks here
    and lands in your inbox. We do not offer net-30 or retention terms to anyone, which is
    precisely why the price never has anyone else's unpaid invoices built into it.</p>
   <p>If a genuine emergency finding turns up, that does not wait for an invoice. Where an
    element is an immediate threat to safety we tell you, and the enforcement agency, straight
    away &mdash; paid or not.</p>
  </div>
 </div>
</section>

{cta}
""".format(ic_al=svg("alert"), ic_lock=svg("lock"), ic_doc=svg("doc"), ic_p=svg("phone"),
           ic_a=svg("arrow"), tel=TEL, ph=PH,
           cta=cta("Not a client yet?",
                   "Book an inspection and this is where your engagement will live."))
    script = '<script src="/assets/js/portal.js" defer></script>'
    write("portal.html", head(
        "Client Portal | California Inspector Group",
        "Track your inspection, view the signed agreement and invoices, settle the balance "
        "and download your CASp or SB 721 / SB 326 report.",
        "/portal.html") + body + script + foot())


# ------------------------------------------------------------------ checkout

def build_checkout(write):
    """Example checkout. Deliberately renders no card fields — card and bank
    capture belong on the processor's hosted page; this page demonstrates the
    order summary, method choice and billing hand-off, and posts the billing
    contact to the 60MS checkout Formspree endpoint."""
    body = phead(
        "Checkout",
        "The deposit that confirms your booking. Card and bank details are only ever "
        "entered on our payment provider&rsquo;s secure page &mdash; never on this site.",
        [("Home", "/index.html"), ("Book", "/book.html"), ("Checkout", None)]) + """
<section>
 <div class="wrap">
  <div class="demo-flag">
   {ic_al}
   <div><b>Example checkout &mdash; payments are not connected on this demo</b>
    <p>This page shows the flow a client will follow. On the live site the buttons below open
     the payment provider&rsquo;s hosted checkout; nothing here charges a card today.</p></div>
  </div>

  <div class="co">
   <div>
    <div class="pcard">
     <h2 style="font-size:1.3rem">Pay the booking deposit</h2>
     <p style="font-size:.94rem">Engagement <b>CIG-2026-0418</b> &middot; agreement signed.
      Paying the 20% deposit confirms the booking and holds your inspection date.</p>

     <h3 style="margin-top:1.4rem">How would you like to pay?</h3>
     <div class="seg" role="group" aria-label="Payment method">
      <button type="button" data-method="card" aria-pressed="true">{ic_card} Card</button>
      <button type="button" data-method="ach" aria-pressed="false">{ic_bank} ACH transfer</button>
      <button type="button" data-method="wire" aria-pressed="false">{ic_wire} Wire</button>
     </div>

     <div class="co-method on" data-pane="card">
      <div class="co-hand">
       {ic_lock}
       <div>
        <b>Card details are taken on Stripe&rsquo;s secure page, not here</b>
        <p>You will be redirected to our payment provider&rsquo;s hosted checkout to enter
         your card. We never see or store card numbers &mdash; and no legitimate inspector
         will ever ask for them by phone or email.</p>
       </div>
      </div>
     </div>
     <div class="co-method" data-pane="ach">
      <div class="co-hand">
       {ic_bank2}
       <div>
        <b>Bank debit connects on the provider&rsquo;s secure page</b>
        <p>ACH direct debit from a US business checking account &mdash; the lowest-fee
         option, and the usual choice for associations and management companies.</p>
       </div>
      </div>
     </div>
     <div class="co-method" data-pane="wire">
      <div class="co-hand">
       {ic_wire2}
       <div>
        <b>Wiring instructions are issued on the invoice</b>
        <p>For larger portfolio engagements. We will never email you changed bank details
         &mdash; if you ever receive a message saying our account has changed, call
         {ph} before acting on it.</p>
       </div>
      </div>
     </div>

     <form id="co-form">
      <h3>Billing contact</h3>
      <div class="fgrid">
       <div class="field"><label for="co-name">Name <span class="req">*</span></label>
        <input id="co-name" name="name" type="text" autocomplete="name" required></div>
       <div class="field"><label for="co-company">Company or association</label>
        <input id="co-company" name="company" type="text" autocomplete="organization"></div>
       <div class="field"><label for="co-email">Email for the receipt <span class="req">*</span></label>
        <input id="co-email" name="email" type="email" autocomplete="email" required></div>
       <div class="field"><label for="co-phone">Phone</label>
        <input id="co-phone" name="phone" type="tel" autocomplete="tel"></div>
       <div class="field full"><label for="co-addr">Billing address</label>
        <input id="co-addr" name="billing_address" type="text" autocomplete="street-address"></div>
      </div>
      <input class="hp" type="text" name="_gotcha" tabindex="-1" autocomplete="off" aria-hidden="true">
      <p class="qerr" id="co-err" role="alert">Please add your name and a valid email.</p>
      <button class="btn btn-solid btn-lg btn-full" type="submit" id="co-pay">
       {ic_lock2} Continue to secure payment &mdash; $230.00</button>
      <p class="form-note">Demo: this submits the billing contact to the 60MS test inbox and
       stops there. On the live site this button opens the hosted payment page.</p>
     </form>

     <div class="co-ok" id="co-ok" hidden>
      <div class="qtick">{ic_ck}</div>
      <h2 style="font-size:1.3rem">This is where Stripe takes over</h2>
      <p>On the live site you would now be on the payment provider&rsquo;s secure page.
       Your billing contact has been recorded in the demo inbox.</p>
      <a class="btn btn-soft" href="/portal.html">See what happens after payment {ic_a}</a>
     </div>
    </div>
   </div>

   <aside class="co-side">
    <div class="co-sum">
     <h2>Order summary</h2>
     <div class="co-line"><span>CASp property inspection</span><b>$1,150.00</b></div>
     <div class="co-line"><span>Retail &amp; storefront &middot; 2,180 sq ft</span><b></b></div>
     <div class="co-line"><span>1420 Alisal Street, Salinas</span><b></b></div>
     <div class="co-line"><span>Travel &mdash; Monterey County</span><b>Included</b></div>
     <div class="co-line co-total"><span>Deposit due today (20%)</span><b>$230.00</b></div>
     <div class="co-line"><span>Balance on completion</span><b>$920.00</b></div>
     <p class="co-muted">The balance falls due when the report is complete; paying it
      releases the signed PDF instantly &mdash; in your portal and by email. No net terms,
      no retention. The deposit is refundable per the cancellation terms in the inspection
      agreement.</p>
    </div>
   </aside>
  </div>
 </div>
</section>

{cta}
""".format(ic_al=svg("alert"), ic_card=svg("card"), ic_bank=svg("bank"), ic_wire=svg("wire"),
           ic_bank2=svg("bank"), ic_wire2=svg("wire"), ic_lock=svg("lock"), ic_lock2=svg("lock"),
           ic_ck='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" '
                 'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20 6L9 17l-5-5"/></svg>',
           ic_a=svg("arrow"), ph=PH,
           cta=cta("Questions before you pay?",
                   "Fifteen minutes on a call answers most of them, and the deposit is not "
                   "due until the agreement is signed."))
    script = ('<script>window.CIG_CHECKOUT={"form":"%s"};</script>'
              '<script src="/assets/js/checkout.js" defer></script>' % CHECKOUT_ACTION)
    write("checkout.html", head(
        "Checkout | California Inspector Group",
        "Pay the 20% booking deposit by card, ACH or wire. Card details are only ever "
        "entered on the payment provider's secure page.",
        "/checkout.html") + body + script + foot())
