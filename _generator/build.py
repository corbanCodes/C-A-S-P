# -*- coding: utf-8 -*-
"""Build every page. Run:  python3 _generator/build.py

Shared chrome lives in chrome.py, reusable sections in blocks.py, the SVG
diagrams in diagrams.py and all business content in data.py. Editing a
generated .html directly works for a one-off tweak but the next run overwrites it.
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, ".."))
sys.path.insert(0, HERE)

from data import (BIZ, SERVICES, ACCESS_SERVICES, STRUCT_SERVICES, SERVICE_BY_SLUG,
                  PATH_OF_TRAVEL, EEE_CHECKS, PROCESS, REGIONS, COUNTIES, AUDIENCES,
                  FAQ, STATS, REVIEWS)
from chrome import head, foot, cta, svg, demo_btn, TEL, PH, EM
from blocks import (img, phead, service_cards, service_mini, faq_block, faq_schema,
                    quote_form, process_steps, stat_row, review_cards, review_feature,
                    review_pull)
import diagrams as dg
import commerce
import report_docs

PAGES = []


def write(path, html):
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(html)
    PAGES.append(path)


# ============================================================ home

def build_home():
    body = """
<section class="hero-lite">
 <div class="wrap hero-lite-in">
  <span class="eyebrow">{ic_geo} Statewide &middot; all 58 California counties</span>
  <h1>Two California mandates.<br><em>One inspector.</em></h1>
  <p class="hero-lede">
   CASp accessibility inspections that make you a qualified defendant before anyone files,
   and the SB&nbsp;721 / SB&nbsp;326 balcony inspections the state already requires.
   Priced up front, booked online, reported in days.
  </p>
  <div class="hero-btns">
   <a class="btn btn-solid btn-lg" href="/book.html">Book an inspection {ic_a}</a>
   {demo_hero}
  </div>
  <div class="hero-chips">
   <span class="chip">{ic_ck} DSA Certified Access Specialist program</span>
   <span class="chip">{ic_ck} Civil Code &sect;55.54 qualified defendant</span>
   <span class="chip">{ic_ck} SB 721 &middot; H&amp;S &sect;17973</span>
   <span class="chip">{ic_ck} SB 326 &middot; Civ. &sect;5551</span>
   <span class="chip">{ic_ck} Flat pricing, published</span>
  </div>

  <div class="hero-stage">
  <div class="hero-photo" aria-hidden="true">{im_hero}</div>
  <div class="rv" role="img" aria-label="Preview of an inspection report and its compliance summary">
   <div class="rv-chrome">
    <div class="rv-dots" aria-hidden="true"><i></i><i></i><i></i></div>
    <span>CASp Inspection Report &mdash; 1420 Alisal Street, Salinas</span>
   </div>
   <div class="rv-body">
    <div class="rv-main">
     <h3>Itemised findings</h3>
     <p class="rv-sub">34 findings &middot; measured against CBC Chapter 11B &amp; 2010 ADA Standards</p>
     <div class="rv-row">{ic_geo2}<b>Parking &mdash; access aisle slope 4.1% (max 2.08%)</b><span class="rv-sev rv-sev-hi">Priority</span></div>
     <div class="rv-row">{ic_doc2}<b>Entrance &mdash; door opening force 11 lbf (max 5 lbf)</b><span class="rv-sev rv-sev-md">Correct</span></div>
     <div class="rv-row">{ic_ruler2}<b>Restroom &mdash; grab bar at 30&Prime; (required 33&ndash;36&Prime;)</b><span class="rv-sev rv-sev-md">Correct</span></div>
     <div class="rv-row">{ic_ck2}<b>Service counter &mdash; 34&Prime; section provided</b><span class="rv-sev rv-sev-ok">Compliant</span></div>
    </div>
    <div class="rv-side">
     <div class="rv-badge">{ic_sh2}<div><b>Qualified defendant</b><span>Report &amp; schedule on file &middot; &sect;55.54</span></div></div>
     <div class="rv-stat"><span>Exposure per offence</span><b>$4,000 &rarr; <i class="up" style="font-style:normal">$1,000</i></b></div>
     <div class="rv-stat"><span>Schedule of completion</span><b>12 items &middot; 60 days</b></div>
     <div class="rv-stat"><span>Next inspection cycle</span><b>April 2029</b></div>
    </div>
   </div>
  </div>
  </div>
 </div>
</section>

<section class="tight">
 <div class="wrap">
  <div class="mandates">
   <a class="mandate mandate-a" href="/casp.html">
    <span class="mandate-tag">{ic_s} Voluntary &mdash; the shield you choose</span>
    <h2 class="mh">CASp accessibility inspections</h2>
    <p>A Certified Access Specialist report is the only thing that makes you a
       <b>qualified defendant</b> if someone files an accessibility claim against your
       business. Nobody makes you get one. That is rather the point.</p>
    <span class="mandate-go">What CASp actually is {ic_a}</span>
   </a>
   <a class="mandate mandate-s" href="/balcony-inspections.html">
    <span class="mandate-tag">{ic_al} Mandatory &mdash; and already late</span>
    <h2 class="mh">SB 721 &amp; SB 326 balcony inspections</h2>
    <p>Every apartment, condo and HOA building in California with elevated wood-framed
       balconies, walkways or stairs had a <b>hard deadline</b>. Both have now passed.
       If yours has not been inspected, you are out of compliance today.</p>
    <span class="mandate-go">Check whether you are in scope {ic_a}</span>
   </a>
  </div>
  <div class="stat-row" style="margin-top:1.1rem">{stats}</div>
 </div>
</section>

<section>
 <div class="wrap">
  <div class="sec-head">
   <span class="eyebrow eyebrow-a">{ic_s} Accessibility</span>
   <h2>Why anyone pays for an inspection the law does not require</h2>
   <p class="lede">Because the alternative gets priced by somebody else. California's Unruh
    Civil Rights Act carries minimum statutory damages of <b>$4,000 per offence</b> plus the
    plaintiff's attorney fees &mdash; and a single visit can generate several alleged offences.</p>
  </div>

  <figure class="dgw">
   {d_timeline}
   <figcaption>What changes the day a complaint is served, with and without a CASp report on
    file. Qualified defendant protections under Civil Code &sect;55.54 require the inspection,
    report and correction schedule to pre-date the filing.</figcaption>
  </figure>

  <div class="note note-warn" style="margin-top:1.6rem">
   <b>The timing is the whole trick.</b>
   You cannot buy the shield after the arrow lands. An inspection commissioned the week you
   are served does not make you a qualified defendant &mdash; the report has to already exist.
  </div>

  <div style="margin-top:2.6rem">{acc_cards}</div>
 </div>
</section>

<section class="sec-paper">
 <div class="wrap">
  <div class="sec-head">
   <span class="eyebrow eyebrow-s">{ic_al} Structural</span>
   <h2>The balcony laws are not optional, and both deadlines have passed</h2>
   <p class="lede">After the 2015 Berkeley balcony collapse killed six people, California made
    inspection of exterior elevated elements mandatory. Which statute you fall under depends
    on one thing: whether you rent the units or an association maintains them.</p>
  </div>

  <figure class="dgw">
   {d_which}
   <figcaption>SB 721 covers multifamily rentals under Health &amp; Safety Code &sect;17973.
    SB 326 covers condominiums and common interest developments under Civil Code &sect;5551.
    AB 2579 extended the SB 721 deadline by one year; it did not touch SB 326.</figcaption>
  </figure>

  <div style="margin-top:2.6rem">{st_cards}</div>
 </div>
</section>

<section>
 <div class="wrap">
  <div class="split">
   <div class="split-media">{im_wood}</div>
   <div>
    <h2>What we are actually looking for</h2>
    <p>An exterior elevated element fails from the inside out. By the time a balcony looks
     wrong from the ground, the ledger has usually been wet for years. The inspection goes
     after the parts you cannot see from the courtyard.</p>
    <ul class="checks checks-s">{eee_checks}</ul>
   </div>
  </div>
 </div>
</section>

<section class="sec-paper">
 <div class="wrap">
  <div class="sec-head center">
   <h2>Who calls us</h2>
   <p>If the public can walk in, accessibility applies. If it has a balcony over six feet,
    so does the structural side.</p>
  </div>
  <div class="grid g4">{aud}</div>
 </div>
</section>

<section>
 <div class="wrap">
  <div class="sec-head"><h2>How it works</h2>
   <p class="lede">Six steps, one flat price, and a report you can hand to a lawyer, a board,
    a lender or a code official.</p></div>
  {steps}
  <div class="note note-ok" style="margin-top:2rem">
   <b>We do not do the repairs.</b>
   An inspector who sells the repair he recommends has an obvious reason to find more of them.
   We inspect and report; you use your own contractors. It is the reason our findings are
   worth reading.
  </div>
 </div>
</section>

<section class="sec-ink">
 <div class="wrap">
  <div class="split">
   <div>
    <span class="eyebrow eyebrow-a">{ic_geo} Statewide</span>
    <h2>All 58 counties, one inspector</h2>
    <p>California Inspector Group works the entire state. Robert Lehman spent a career as a
     municipal building inspector for California cities before founding the firm &mdash;
     the same code, read from the other side of the counter.</p>
    <p>Portfolios with buildings in several regions get one inspector, one report format and
     one calendar, instead of a different vendor and a different template in every market.</p>
    <p style="margin-top:1.6rem">
     <a class="btn btn-solid" href="/coverage.html">See coverage {ic_a}</a>
     <a class="btn btn-line" href="/about.html">About the firm</a>
    </p>
   </div>
   <div class="split-media">{im_street}</div>
  </div>
 </div>
</section>

<section class="sec-paper">
 <div class="wrap">
  <div class="split">
   <div>
    <span class="eyebrow eyebrow-a">{ic_tag} Pricing</span>
    <h2>Our prices are on the board</h2>
    <p class="lede">Most inspection firms make you call to find out whether you can afford
     them. If your building fits a standard occupancy and footprint, the price is published
     &mdash; and you can book the whole thing online in about four minutes.</p>
    <ul class="checks">
     <li>{ck}<span>Flat price by occupancy type and floor area, travel included</span></li>
     <li>{ck}<span>Balcony inspections priced per building on unit count</span></li>
     <li>{ck}<span>20% deposit holds your date &mdash; the balance is due on completion</span></li>
     <li>{ck}<span>Portfolios, franchises and multi-building campuses priced as a package</span></li>
    </ul>
    <p style="margin-top:1.6rem">
     <a class="btn btn-solid btn-lg" href="/pricing.html">See the rate card {ic_a}</a>
     <a class="btn btn-line btn-lg" href="/book.html">Book online</a>
    </p>
   </div>
   <div class="split-media">{im_park}</div>
  </div>
 </div>
</section>

<section>
 <div class="wrap">
  <div class="sec-head center"><h2>See the report before you buy it</h2>
   <p class="lede">The report is the product, so look at one first. Two worked samples &mdash;
    fictional property, real format &mdash; showing exactly what lands on your desk.</p></div>
  <div class="grid g2">
   <a class="card svc" href="/samples/casp-report.html">
    <div class="doc-card-img">{th_casp}</div>
    <div class="svc-body"><span class="svc-tag">Accessibility</span>
     <h3>Sample CASp inspection report</h3>
     <p>Built to Civil Code &sect;55.53: every finding stated as a measurement against the
      code section it fails, a schedule of completion, and the certificate &mdash; the
      document that makes you a qualified defendant.</p>
     <span class="card-more">Read the sample {ic_a}</span></div>
   </a>
   <a class="card svc svc-s" href="/samples/sb721-report.html">
    <div class="doc-card-img">{th_721}</div>
    <div class="svc-body"><span class="svc-tag">Structural</span>
     <h3>Sample SB 721 balcony report</h3>
     <p>Built to Health &amp; Safety Code &sect;17973: current condition and projected
      service life per element, the photographic baseline your next cycle is measured
      against, and the immediate-threat advisory done properly.</p>
     <span class="card-more">Read the sample {ic_a}</span></div>
   </a>
  </div>
 </div>
</section>

<section class="sec-tint">
 <div class="wrap">
  <div class="sec-head center"><h2>Owners and boards on working with us</h2></div>
  {rev_feat}
  {revs}
  <p class="center" style="margin-top:2rem"><a class="btn btn-line" href="/reviews.html">Read all reviews {ic_a}</a></p>
 </div>
</section>

<section>
 <div class="wrap narrow">
  <div class="sec-head center"><h2>Common questions</h2></div>
  {faq}
  <p class="center" style="margin-top:2rem"><a class="btn btn-line" href="/faq.html">All questions {ic_a}</a></p>
 </div>
</section>

{cta}
""".format(
        tel=TEL, ph=PH, ic_a=svg("arrow"), ic_p=svg("phone"), ic_s=svg("shield"),
        ic_al=svg("alert"), ic_geo=svg("geo"),
        demo_hero=demo_btn(cls="btn btn-line btn-lg"),
        im_hero=img("plaza-ramp", "", loading="eager"),
        ic_ck=svg("check"), ic_ck2=svg("check"), ic_geo2=svg("geo"), ic_doc2=svg("doc"),
        ic_ruler2=svg("ruler"), ic_sh2=svg("shield"),
        stats="".join('<div class="stat"><b>%s</b><span>%s</span></div>' % s for s in STATS),
        d_timeline=dg.lawsuit_timeline(), d_which=dg.which_law(),
        acc_cards=service_cards(ACCESS_SERVICES[:3], tagged=False),
        st_cards=service_mini(STRUCT_SERVICES),
        im_wood=img("weathered-wood", "Weathered, checked timber of the kind found in exterior elevated framing"),
        im_street=img("commercial-street", "A California main-street commercial building"),
        eee_checks="".join('<li>%s<span><b>%s.</b> %s</span></li>' % (svg("check"), t, d)
                           for t, d in EEE_CHECKS),
        aud="".join('<div class="card"><div class="card-ic">%s</div><h3>%s</h3><p>%s</p></div>'
                    % (svg(ic), t, d) for t, ic, d in AUDIENCES[:8]),
        steps=process_steps(),
        th_casp=img("report-casp-thumb", "First page of the sample CASp inspection report"),
        th_721=img("report-sb721-thumb", "First page of the sample SB 721 inspection report"),
        rev_feat=review_feature(next(r for r in REVIEWS if r.get("feat"))),
        revs=review_cards([r for r in REVIEWS if not r.get("feat")][:6]),
        ic_tag=svg("tag"), ck=svg("check"),
        im_park=img("parking-stalls", "Marked accessible parking stalls in a commercial car park"),
        faq=faq_block([f for f in FAQ if f[1] in (
            "Is a CASp inspection required by law?",
            "So why would I pay for something optional?",
            "Are these optional too?",
            "What is the deadline?",
            "Do you do the repairs as well?",
            "How much does it cost?")]),
        cta=cta(),
    )
    write("index.html", head(
        "CASp &amp; SB 721 / SB 326 Inspections Statewide | California Inspector Group",
        "CASp accessibility inspections and SB 721 / SB 326 balcony inspections across all 58 "
        "California counties. Flat-price quotes, reports you can hand to a lawyer or a board.",
        "/") + body + foot())


# ============================================================ what is CASp

def build_casp():
    body = phead(
        "What a CASp inspection actually is",
        "Certified Access Specialist &mdash; a California certification, a specific kind of "
        "report, and the only route to qualified defendant status. Here is the whole thing "
        "in plain English.",
        [("Home", "/index.html"), ("What is CASp?", None)]) + """
<section>
 <div class="wrap">
  <div class="split">
   <div>
    <h2>Start with the name, because it is confusing on purpose</h2>
    <p><b>CASp</b> stands for <b>Certified Access Specialist</b>. The programme is run by the
     California Division of the State Architect (DSA), part of the Department of General
     Services, and it certifies individuals to inspect buildings and sites against California
     and federal construction-related accessibility standards.</p>
    <div class="note note-warn">
     <b>Searching for it will mislead you.</b>
     <b>CASP</b> in capitals is also an unrelated cybersecurity credential, and it dominates
     the search results. If what you are reading mentions penetration testing, you have the
     wrong CASp. The one that matters to a California business owner is about ramps, door
     widths and restroom clearances.
    </div>
    <p>Certification is not a weekend course. Candidates qualify on education and experience
     &mdash; time in a code enforcement agency, or with a licensed architect or engineer, or
     as a licensed general contractor &mdash; then pass both an open-book and a closed-book
     state examination, and maintain the certification with continuing education.</p>
   </div>
   <div class="split-media">{im_sign}</div>
  </div>
 </div>
</section>

<section class="sec-paper">
 <div class="wrap">
  <div class="sec-head">
   <h2>What the inspector actually walks</h2>
   <p class="lede">An accessibility inspection follows a path, not a checklist of rooms. It
    starts at the property line and ends wherever your customer has to reach.</p>
  </div>
  <figure class="dgw">
   {d_path}
   <figcaption>The sequence a CASp inspection follows through a commercial site. Every
    segment carries its own dimensional requirements &mdash; a compliant restroom at the end
    of a non-compliant route is still a finding.</figcaption>
  </figure>
  <div class="rows" style="margin-top:2.6rem">{rows}</div>

  <div class="photoband">
   <figure>{im_curb}<figcaption>Curb ramps: running slope, cross-slope, flare and landing.</figcaption></figure>
   <figure>{im_dome}<figcaption>Detectable warnings: dome size, spacing and placement.</figcaption></figure>
   <figure>{im_walk}<figcaption>The route itself: width, level changes and where it actually goes.</figcaption></figure>
  </div>
  <p class="form-note center">Findings are recorded as measurements against the required
   dimension, not as opinions. A number can be checked; an impression can only be argued with.</p>
 </div>
</section>

<section>
 <div class="wrap">
  <div class="sec-head">
   <h2>Why a voluntary inspection is worth paying for</h2>
   <p class="lede">Nothing in California law requires a CASp inspection. What it does is
    change your position the moment somebody files.</p>
  </div>

  <p>California's Unruh Civil Rights Act treats a construction-related accessibility violation
   as a civil rights violation and attaches <b>minimum statutory damages of $4,000 per
   offence</b>, plus the plaintiff's attorney fees. A single visit to your business can
   generate more than one alleged offence. There is an established practice of plaintiffs
   who visit many businesses looking for exactly this, and the economics work in their favour
   because the fee award does not depend on the damages being large.</p>

  <p>The Construction-Related Accessibility Standards Compliance Act gives owners a way to
   change that arithmetic. A site that has been CASp-inspected before a claim is filed can
   move into a different procedural category.</p>

  <figure class="dgw" style="margin:2rem 0">
   {d_damages}
   <figcaption>Minimum statutory damages per offence under Civil Code &sect;55.56. The
    reductions depend on correction within the stated window and, for the $1,000 tier, on the
    site having been CASp-inspected or permitted after 1 January 2008.</figcaption>
  </figure>

  <h3>Qualified defendant status</h3>
  <p>If your site has been CASp-inspected and you are sued over construction-related
   accessibility, you may apply to the court for a <b>90-day stay of proceedings</b> and an
   <b>early evaluation conference</b> under Civil Code &sect;55.54. The case pauses. A judge
   gets both parties in a room early, before fees compound and before the matter develops the
   momentum that makes nuisance settlements attractive.</p>

  <div class="note note-a">
   <b>The report has to come first.</b>
   Qualified defendant protections apply only where the inspection, the report and the
   schedule of completion pre-date the filing. This is the single most common and most
   expensive misunderstanding about the programme.
  </div>

  <h3>Small business grace period</h3>
  <p>A business with 50 or fewer employees over the previous three years may opt for a
   <b>120-day grace period</b> after a CASp inspection, during which it is not liable for
   minimum statutory damages on the violations identified in the report, provided those
   violations are corrected within that window and the CASp notifies DSA of the inspection.</p>
 </div>
</section>

<section class="sec-paper">
 <div class="wrap">
  <div class="split flip">
   <div class="split-media">{im_restroom}</div>
   <div>
    <h2>What you receive</h2>
    <p>Civil Code &sect;55.53 sets out what a CASp report has to contain, and it differs
     depending on what the inspection found.</p>
    <h3 style="margin-top:1.6rem">If the site meets applicable standards</h3>
    <ul class="checks">
     <li>{ck}<span>A description of the structures and areas inspected</span></li>
     <li>{ck}<span>A signed statement that the site meets applicable standards</span></li>
     <li>{ck}<span>A note on whether readily achievable barrier removal was assessed</span></li>
    </ul>
    <h3 style="margin-top:1.6rem">If it does not &mdash; which is usual</h3>
    <ul class="checks">
     <li>{ck}<span>A description of the structures and areas inspected, and the date</span></li>
     <li>{ck}<span>A signed statement identifying the corrections needed</span></li>
     <li>{ck}<span>An itemised list of every required correction</span></li>
     <li>{ck}<span>A schedule of completion for each correction</span></li>
    </ul>
    <p style="margin:1.4rem 0"><a class="btn btn-soft" href="/samples/casp-report.html">Read a sample report {ic_a2}</a></p>
    <div class="note">
     <b>The certificate is not a compliance certificate.</b>
     A Disability Access Inspection Certificate records that an inspection happened. DSA is
     explicit that it is not a certificate of compliance. Keep it available; do not treat it
     as a clean bill of health.
    </div>
   </div>
  </div>
 </div>
</section>

<section>
 <div class="wrap narrow">
  <h2>Questions people ask before booking</h2>
  {faq}
 </div>
</section>

{cta}
""".format(
        im_sign=img("parking-sign", "An accessible parking sign against a clear sky"),
        im_restroom=img("restroom", "A restroom fitted with grab bars at a water closet"),
        d_path=dg.path_of_travel(), d_damages=dg.damages_chart(),
        ic_a2=svg("arrow"),
        rows="".join('<div class="row"><h3>%s</h3><p>%s</p></div>' % (t, d)
                     for t, d in PATH_OF_TRAVEL),
        im_curb=img("curb-ramp", "A concrete curb ramp meeting a road at a marked crossing"),
        im_dome=img("tactile-pad", "A yellow detectable warning surface set into a pavement"),
        im_walk=img("sidewalk-ramp", "A long, gently graded pavement ramp running to a crossing"),
        ck=svg("check"),
        faq=faq_block([f for f in FAQ if f[0] == "access"]),
        cta=cta("Get the report before you need it",
                "A CASp inspection is a known, one-time cost. A claim is not. Call for a flat "
                "price on your property."),
    )
    write("casp.html", head(
        "What Is a CASp Inspection? California Access Compliance Explained",
        "CASp means Certified Access Specialist — a California Division of the State Architect "
        "certification. What the inspection covers, what the report must contain, and how "
        "qualified defendant status works under Civil Code §55.54.",
        "/casp.html") + body + faq_schema([f for f in FAQ if f[0] == "access"]) + foot())


# ============================================================ balcony law

def build_balcony():
    body = phead(
        "California's balcony inspection laws",
        "SB 721 and SB 326 made inspection of exterior elevated elements mandatory. Both first "
        "deadlines have now passed. Here is who is in scope, what gets inspected and what "
        "happens next.",
        [("Home", "/index.html"), ("Balcony law", None)], amber=True) + """
<section>
 <div class="wrap">
  <div class="deadline">
   {ic_al}
   <div>
    <b>Both first-round deadlines are behind us</b>
    <p>SB 326 was due <b>1 January 2025</b>. SB 721 was due <b>1 January 2026</b> after the
     one-year extension in AB 2579. A building in scope without a completed inspection is out
     of compliance today, not at some future date.</p>
   </div>
   <a class="btn btn-amber" href="/contact.html">Get scheduled {ic_a}</a>
  </div>

  <div class="split">
   <div>
    <h2>Why these laws exist</h2>
    <p>In June 2015 a fifth-floor apartment balcony in Berkeley collapsed during a birthday
     party. Six people were killed and seven more were seriously injured. The cantilevered
     joists had been rotted by water that got past the waterproofing and stayed in the framing.
     From the outside, the balcony had looked ordinary.</p>
    <p>California's response was to stop relying on anyone noticing. SB 721 in 2018 and SB 326
     in 2019 put exterior elevated elements on a mandatory inspection cycle &mdash; a
     recurring, documented look at the parts that fail silently.</p>
    <p>This is the difference that matters when people ask us which service they need.
     A CASp inspection is a shield you can choose to pick up. <b>These inspections are not
     optional and they are not waivable.</b></p>
   </div>
   <div class="split-media">{im_eee}</div>
  </div>

  <div class="split flip" style="margin-top:clamp(2.4rem,5vw,4rem)">
   <div class="split-media">{im_frame}</div>
   <div>
    <h2>Wood is the whole reason these statutes exist</h2>
    <p>California builds multifamily housing in wood, and wood is fine until water reaches it
     and stays. Every element these laws reach has the same weakness: framing that was
     designed dry, protected by a membrane and a piece of flashing that were installed once
     and never looked at again.</p>
    <p>Concrete and steel balconies are largely outside these statutes for exactly that
     reason. If your building went up as a wood-framed structure &mdash; and in California
     most three-to-five storey residential buildings did &mdash; assume you are in scope
     until someone competent says otherwise.</p>
   </div>
  </div>
 </div>
</section>

<section class="sec-paper">
 <div class="wrap">
  <div class="sec-head"><h2>Which law applies to your building</h2>
   <p class="lede">One question decides it: do you rent the units out, or does an association
    maintain them?</p></div>
  <figure class="dgw">
   {d_which}
   <figcaption>AB 2579 extended the SB 721 first-inspection deadline from 1 January 2025 to
    1 January 2026. It did not extend SB 326, whose deadline remained 1 January 2025.</figcaption>
  </figure>
 </div>
</section>

<section>
 <div class="wrap">
  <div class="sec-head"><h2>What counts as an exterior elevated element</h2>
   <p class="lede">Four tests, and an element has to meet all of them to be in scope.</p></div>

  <div class="grid g4" style="margin-bottom:2.6rem">
   <div class="card card-s"><div class="card-ic">{ic_b}</div><h3>It projects out</h3>
    <p>Balconies, decks, porches, stairways, walkways and elevated entry structures that
     extend beyond the exterior walls of the building.</p></div>
   <div class="card card-s"><div class="card-ic">{ic_r}</div><h3>More than 6 feet up</h3>
    <p>The walking surface sits more than six feet above the ground below. A ground-floor
     patio is out; a second-storey walkway is in.</p></div>
   <div class="card card-s"><div class="card-ic">{ic_h}</div><h3>Made for people</h3>
    <p>Designed for human occupancy or use &mdash; not a decorative ledge or a piece of
     mechanical screening.</p></div>
   <div class="card card-s"><div class="card-ic">{ic_pl}</div><h3>Supported by wood</h3>
    <p>Supported substantially by wood or wood-based products. A concrete topping over wood
     framing still counts, which catches a lot of owners out.</p></div>
  </div>

  <figure class="dgw">
   {d_eee}
   <figcaption>Where these elements fail. The ledger connection at the building wall is the
    usual culprit: once flashing or membrane lets water behind it, decay works on the framing
    for years before anything is visible from below.</figcaption>
  </figure>
 </div>
</section>

<section class="sec-paper">
 <div class="wrap">
  <div class="sec-head"><h2>SB 721 and SB 326 side by side</h2></div>
  <div class="tw">
   <table>
    <caption class="hp">Comparison of SB 721 and SB 326 requirements</caption>
    <thead><tr><th>&nbsp;</th><th class="th-s">SB 721</th><th class="th-a">SB 326</th></tr></thead>
    <tbody>
     <tr><td><b>Applies to</b></td><td>Apartment and multifamily rental buildings with three
      or more dwelling units</td><td>Condominiums and common interest developments of three
      or more units</td></tr>
     <tr><td><b>Statute</b></td><td>Health &amp; Safety Code &sect;17973</td>
      <td>Civil Code &sect;5551</td></tr>
     <tr><td><b>Duty sits with</b></td><td>The building owner</td>
      <td>The association &mdash; a board responsibility</td></tr>
     <tr><td><b>First inspection due</b></td><td><b>1 January 2026</b><br><small>extended from
      2025 by AB 2579</small></td><td><b>1 January 2025</b><br><small>not extended</small></td></tr>
     <tr><td><b>Repeat cycle</b></td><td>At least every <b>6 years</b></td>
      <td>At least every <b>9 years</b></td></tr>
     <tr><td><b>Who may inspect</b></td><td>Licensed architect; licensed civil or structural
      engineer; A, B or C-5 contractor with 5+ years relevant experience; certified building
      inspector or official</td><td>Licensed structural engineer or architect only</td></tr>
     <tr><td><b>Sampling</b></td><td>A statistically significant sample &mdash; at least 15%
      of each type of element</td><td>A statistically significant sample of the elements the
      association maintains</td></tr>
     <tr><td><b>Where the report goes</b></td><td>Retained by the owner for two inspection
      cycles; provided to the local enforcement agency on request</td><td>To the board, and
      incorporated into the reserve study under Civil Code &sect;5550</td></tr>
     <tr><td><b>If an element is unsafe</b></td><td colspan="2">Local code enforcement is
      notified within 15 days and the element is taken out of service until repaired. This is
      not discretionary under either statute.</td></tr>
    </tbody>
   </table>
  </div>

  <p style="margin-top:1.8rem"><a class="btn btn-amber" href="/samples/sb721-report.html">Read a sample report {ic_a}</a></p>
  <div class="note note-s" style="margin-top:1.4rem">
   <b>HOA boards: the report is a funding document too.</b>
   Because an SB 326 report feeds the reserve study, a deferred balcony repair stops being a
   maintenance opinion and becomes a number the board has to fund. That is uncomfortable, and
   it is exactly what the statute intends.
  </div>
 </div>
</section>

<section>
 <div class="wrap">
  <div class="sec-head"><h2>What the inspection looks at</h2>
   <p class="lede">Load path and water. Almost every failure is one of those two, and usually
    it is both.</p></div>
  <div class="grid g3">{eee}</div>
 </div>
</section>

<section class="sec-paper">
 <div class="wrap">
  <div class="grid g2">
   {cards}
  </div>
 </div>
</section>

<section>
 <div class="wrap narrow">
  <h2>Questions boards and owners ask</h2>
  {faq}
 </div>
</section>

{cta}
""".format(
        ic_al=svg("alert"), ic_a=svg("arrow"), ic_b=svg("building"), ic_r=svg("ruler"),
        ic_h=svg("hoa"), ic_pl=svg("plans"),
        im_eee=img("residential-eee", "A multi-storey residential building with exterior wood balconies and porches"),
        im_frame=img("condo-construction", "A wood-framed multifamily building under construction"),
        d_which=dg.which_law(), d_eee=dg.eee_section(),
        eee="".join('<div class="card card-s"><h3>%s</h3><p>%s</p></div>' % (t, d)
                    for t, d in EEE_CHECKS),
        cards=service_mini(STRUCT_SERVICES),
        faq=faq_block([f for f in FAQ if f[0] == "structural"]),
        cta=cta("Your deadline has already passed",
                "Getting inspected now is materially better than getting inspected after "
                "something happens. Call for a flat price on your building.",
                variant="amber"),
    )
    write("balcony-inspections.html", head(
        "SB 721 &amp; SB 326 Balcony Inspections in California | Deadlines &amp; Scope",
        "California's mandatory balcony inspection laws explained: who SB 721 and SB 326 cover, "
        "what an exterior elevated element is, the passed deadlines, inspection cycles and who "
        "is qualified to sign the report.",
        "/balcony-inspections.html") + body
        + faq_schema([f for f in FAQ if f[0] == "structural"]) + foot())


# ============================================================ services

def build_services():
    body = phead(
        "Services",
        "Two lines of work, one firm. Accessibility inspections that protect you from a claim, "
        "and structural inspections California requires you to have.",
        [("Home", "/index.html"), ("Services", None)]) + """
<section>
 <div class="wrap">
  <div class="sec-head">
   <span class="eyebrow eyebrow-a">{ic_s} Accessibility &mdash; voluntary</span>
   <h2>CASp services</h2>
   <p>Nothing here is required by law. All of it changes what a claim costs you.</p>
  </div>
  {acc}
 </div>
</section>

<section class="sec-paper">
 <div class="wrap">
  <div class="sec-head">
   <span class="eyebrow eyebrow-s">{ic_al} Structural &mdash; mandatory</span>
   <h2>Balcony &amp; exterior elevated element inspections</h2>
   <p>Required by statute, on a repeating cycle, with deadlines that have already passed.</p>
  </div>
  {st}
 </div>
</section>

<section>
 <div class="wrap">
  <div class="split">
   <div>
    <h2>Not sure which one you need?</h2>
    <p>That is the most common call we get, and it is a short one. Tell us the property type
     and the number of units and we can usually tell you inside five minutes which mandate
     applies, whether both do, and roughly what it costs.</p>
    <p>Mixed-use properties frequently need both &mdash; ground-floor retail with apartments
     above is the classic case &mdash; and combining them into one mobilisation saves money.</p>
    <p style="margin-top:1.6rem">
     <a class="btn btn-solid btn-lg" href="tel:{tel}">{ic_p} {ph}</a>
     <a class="btn btn-line btn-lg" href="/contact.html">Send the details</a>
    </p>
   </div>
   <div>{form}</div>
  </div>
 </div>
</section>

{cta}
""".format(ic_s=svg("shield"), ic_al=svg("alert"), ic_p=svg("phone"), ic_a=svg("arrow"),
           tel=TEL, ph=PH,
           acc=service_cards(ACCESS_SERVICES, tagged=False),
           st=service_cards(STRUCT_SERVICES, tagged=False),
           form=quote_form("services", "Get a flat price",
                           "One form, both service lines. We reply the same business day."),
           cta=cta())
    write("services.html", head(
        "Inspection Services | CASp &amp; SB 721 / SB 326 | California Inspector Group",
        "CASp inspections, plan review, lawsuit response, §1938 lease disclosure, SB 721 "
        "apartment and SB 326 HOA balcony inspections — statewide in California.",
        "/services.html") + body + foot())


def build_service_pages():
    for s in SERVICES:
        amber = s["line"] == "structural"
        line_name = "Structural" if amber else "Accessibility"
        others = [o for o in SERVICES if o["slug"] != s["slug"] and o["line"] == s["line"]]

        extra = ""
        if s["slug"] == "casp-lawsuit-response":
            extra = ('<figure class="dgw" style="margin:2.4rem 0">%s<figcaption>The two tracks '
                     'after service. Which one you are on was decided before the complaint '
                     'arrived.</figcaption></figure>' % dg.lawsuit_timeline())
        elif s["slug"] == "casp-inspection":
            extra = ('<figure class="dgw" style="margin:2.4rem 0">%s<figcaption>The path an '
                     'inspection follows through the site.</figcaption></figure>'
                     % dg.path_of_travel())
        elif s["slug"] in ("sb-721-inspection", "sb-326-inspection"):
            extra = ('<figure class="dgw" style="margin:2.4rem 0">%s<figcaption>Where exterior '
                     'elevated elements fail, and the six-foot test that puts them in '
                     'scope.</figcaption></figure>' % dg.eee_section())

        note = ""
        if s.get("note"):
            note = '<div class="note note-warn"><b>To be clear.</b>%s</div>' % s["note"]

        deadline = ""
        if amber:
            due = "1 January 2026" if s["slug"] == "sb-721-inspection" else "1 January 2025"
            cyc = "six years" if s["slug"] == "sb-721-inspection" else "nine years"
            deadline = ('<div class="deadline">%s<div><b>First inspection was due %s</b>'
                        '<p>That date has passed. Inspections then repeat at least every %s. '
                        'If your building has not been inspected, it is out of compliance now.</p>'
                        '</div><a class="btn btn-amber" href="/contact.html">Get scheduled %s</a>'
                        '</div>' % (svg("alert"), due, cyc, svg("arrow")))

        body = phead(s["name"], s["teaser"],
                     [("Home", "/index.html"), ("Services", "/services.html"), (s["name"], None)],
                     amber=amber) + """
<section>
 <div class="wrap">
  {deadline}
  <div class="split">
   <div>
    <span class="eyebrow eyebrow-{k}">{ic} {line}</span>
    <p class="lede">{lede}</p>
   </div>
   <div class="split-media">{im}</div>
  </div>
  {extra}
  <div class="rows" style="margin-top:2.6rem">{rows}</div>
  {note}
 </div>
</section>

<section class="sec-paper">
 <div class="wrap">
  <div class="split">
   <div>
    <h2>How this one runs</h2>
    {steps}
    {review}
   </div>
   <div>{form}</div>
  </div>
 </div>
</section>

<section>
 <div class="wrap">
  <div class="sec-head"><h2>Related services</h2></div>
  {others}
 </div>
</section>

{cta}
""".format(
            deadline=deadline, k="s" if amber else "a",
            ic=svg("alert") if amber else svg("shield"), line=line_name,
            lede=s["lede"], im=img(s["img"], s["name"], loading="eager"),
            extra=extra, note=note,
            rows="".join('<div class="row"><h3>%s</h3><p>%s</p></div>' % (t, d)
                         for t, d in s["points"]),
            steps=process_steps(PROCESS[:4]),
            review=review_pull([r for r in REVIEWS if r["line"] == s["line"]]
                               [hash(s["slug"]) % len([r for r in REVIEWS if r["line"] == s["line"]])]),
            form=quote_form(s["slug"], "Quote this service",
                            "Send the property details and we&rsquo;ll come back with a flat price."),
            others=service_mini(others),
            cta=cta(variant="amber" if amber else ""),
        )
        write("services/%s.html" % s["slug"], head(
            "%s | California Inspector Group" % s["name"].replace("&amp;", "&"),
            s["teaser"].replace("&sect;", "§").replace("&mdash;", "—"),
            "/services/%s.html" % s["slug"]) + body + foot())


# ============================================================ process / about

def build_process():
    body = phead(
        "How an inspection works",
        "From the first call to the report on your desk, and the calendar entry that stops the "
        "next cycle sneaking up on you.",
        [("Home", "/index.html"), ("How it works", None)]) + """
<section>
 <div class="wrap narrow">
  {steps}
  <div class="note note-ok">
   <b>We do not sell the repairs we recommend.</b>
   An inspector with a repair crew has a reason to lengthen the list. We inspect and we
   report; the corrections are yours to bid competitively. It costs us upsell revenue and it
   is why a lender, a board or a court can take the report at face value.
  </div>
 </div>
</section>

<section class="sec-paper">
 <div class="wrap">
  <div class="sec-head"><h2>What lands on your desk</h2>
   <p class="lede">A report written to be used by somebody else &mdash; your attorney, your
    board, your lender, your contractor or a code official.</p></div>
  <p style="margin:-.8rem 0 1.6rem"><a class="btn btn-soft" href="/samples/casp-report.html">Sample CASp report {ic_c2}</a>
   <a class="btn btn-soft" href="/samples/sb721-report.html">Sample SB 721 report {ic_c2}</a></p>
  <div class="grid g3">
   <div class="card"><div class="card-ic">{ic_d}</div><h3>Itemised findings</h3>
    <p>Every item listed separately with the applicable standard or code section beside it,
     not a narrative you have to interpret.</p></div>
   <div class="card"><div class="card-ic">{ic_se}</div><h3>Photographs</h3>
    <p>Located and captioned, so a contractor bidding the work knows exactly what and where
     without a second site visit.</p></div>
   <div class="card"><div class="card-ic">{ic_c}</div><h3>Schedule of completion</h3>
    <p>A date against each correction. Required by Civil Code &sect;55.53 on the CASp side,
     and simply good practice on the structural side.</p></div>
   <div class="card"><div class="card-ic">{ic_r}</div><h3>Measurements</h3>
    <p>Actual dimensions recorded against the required ones, so a disputed item can be
     checked rather than argued.</p></div>
   <div class="card"><div class="card-ic">{ic_sh}</div><h3>Certification</h3>
    <p>Signed by the certified or licensed individual the relevant statute requires &mdash;
     which is the part that gives the document its legal weight.</p></div>
   <div class="card"><div class="card-ic">{ic_cal}</div><h3>Your next date</h3>
    <p>Six years for SB 721, nine for SB 326, and a sensible re-look interval on the
     accessibility side. Diarised before we leave.</p></div>
  </div>
 </div>
</section>

<section>
 <div class="wrap">
  <div class="split">
   <div>
    <h2>What we need from you</h2>
    <ul class="checks">
     <li>{ck}<span>The property address and, for multifamily, the unit count</span></li>
     <li>{ck}<span>Roughly when it was built, and whether it has been remodelled</span></li>
     <li>{ck}<span>Any permit history or prior reports you already hold</span></li>
     <li>{ck}<span>Access &mdash; keys, codes, and a contact who can open locked areas</span></li>
     <li>{ck}<span>For HOAs, whoever on the board is authorised to receive the report</span></li>
     <li>{ck}<span>If you have been served, the date of service. It starts a clock.</span></li>
    </ul>
   </div>
   <div>{form}</div>
  </div>
 </div>
</section>

{cta}
""".format(steps=process_steps(), form=quote_form("process"), ck=svg("check"), ic_c2=svg("arrow"),
           ic_d=svg("doc"), ic_se=svg("search"), ic_c=svg("check"), ic_r=svg("ruler"),
           ic_sh=svg("shield"), ic_cal=svg("calendar"), cta=cta())
    write("process.html", head(
        "How an Inspection Works | California Inspector Group",
        "From first call to final report: scoping, flat-price quote, the inspection itself, "
        "what the report contains, corrections and re-inspection.",
        "/process.html") + body + foot())


def build_about():
    body = phead(
        "About California Inspector Group",
        "A building inspector&rsquo;s firm. Founded by someone who spent a career on the "
        "enforcement side of the counter reading the same code.",
        [("Home", "/index.html"), ("About", None)]) + """
<section>
 <div class="wrap">
  <div class="split">
   <div>
    <h2>Robert Lehman</h2>
    <p class="lede">Founder, California Inspector Group LLC.</p>
    <p>Robert spent his career as a building inspector for California cities &mdash; reading
     plans, walking sites and signing off work under the same code the state now asks private
     inspectors to apply. That is an unusual background for this work and a useful one: the
     questions a code official will ask about your building are the questions he spent years
     asking about other people's.</p>
    <p>He founded California Inspector Group to do two things properly. The first is
     accessibility &mdash; a field where most owners have no idea they are exposed until a
     letter arrives. The second is the balcony inspection work that California made mandatory
     after Berkeley, where the deadlines have now passed and a great many buildings are
     quietly non-compliant.</p>
    <p>The firm works statewide, across all 58 counties, and staffs each inspection with
     someone who holds the certification or licence that the particular statute requires.</p>
   </div>
   <div class="split-media">{im}</div>
  </div>
 </div>
</section>

<section class="sec-paper">
 <div class="wrap">
  <div class="sec-head"><h2>How we work</h2></div>
  <div class="grid g3">
   <div class="card"><div class="card-ic">{ic_sc}</div><h3>Inspection only</h3>
    <p>We do not sell repairs. No estimate at the end of the walk, no crew in the van. The
     findings are the product, and they are worth more for being disinterested.</p></div>
   <div class="card"><div class="card-ic">{ic_d}</div><h3>Flat pricing</h3>
    <p>Quoted before we schedule, from square footage, unit count and element count. Travel is
     in the number, not discovered afterwards.</p></div>
   <div class="card"><div class="card-ic">{ic_r}</div><h3>Measured, not eyeballed</h3>
    <p>Slopes, clearances, widths and heights recorded as numbers. A finding you can check is
     a finding that survives a challenge.</p></div>
   <div class="card"><div class="card-ic">{ic_g}</div><h3>Statewide, one standard</h3>
    <p>Portfolio owners get one report format across every market rather than a different
     vendor's template in each county.</p></div>
   <div class="card"><div class="card-ic">{ic_cal}</div><h3>We track your cycle</h3>
    <p>Six years, nine years, or whenever your risk profile changes. We diarise it so the next
     deadline is not a surprise.</p></div>
   <div class="card"><div class="card-ic">{ic_sh}</div><h3>Right credential, right job</h3>
    <p>SB 326 requires a licensed structural engineer or architect. SB 721 and CASp have their
     own bars. We staff to the statute, not to convenience.</p></div>
  </div>
 </div>
</section>

<section>
 <div class="wrap narrow">
  <blockquote class="quote">
   Most owners are not careless. They simply have no idea a walkway they have walked on for
   twenty years is now a statutory obligation with a date attached, or that a customer's
   single visit can cost them four thousand dollars per item.
   <cite>&mdash; Robert Lehman</cite>
  </blockquote>
 </div>
</section>

<section class="sec-ink">
 <div class="wrap"><div class="stat-row">{stats}</div></div>
</section>

{cta}
""".format(im=img("handrail", "A wall-mounted handrail along an accessible route"),
           ic_sc=svg("scale"), ic_d=svg("doc"), ic_r=svg("ruler"), ic_g=svg("geo"),
           ic_cal=svg("calendar"), ic_sh=svg("shield"),
           stats="".join('<div class="stat"><b>%s</b><span>%s</span></div>' % s for s in STATS),
           cta=cta())
    write("about.html", head(
        "About | California Inspector Group",
        "Founded by Robert Lehman, a career California municipal building inspector. CASp "
        "accessibility and SB 721 / SB 326 structural inspections, statewide.",
        "/about.html") + body + foot())


# ============================================================ coverage

def build_coverage():
    cards = "".join(
        '<a class="card" href="/areas/%s.html"><div class="card-ic">%s</div><h3>%s</h3>'
        '<p>%s</p><span class="card-more">Coverage detail %s</span></a>'
        % (slug, svg("geo"), name, blurb, svg("arrow"))
        for slug, name, counties, blurb in REGIONS)

    body = phead(
        "Where we work",
        "All 58 California counties. One inspector, one report format, one calendar &mdash; "
        "whether your buildings are in one city or nine.",
        [("Home", "/index.html"), ("Coverage", None)]) + """
<section>
 <div class="wrap">
  <div class="sec-head"><h2>By region</h2>
   <p class="lede">Grouped the way scheduling actually works. Travel outside the immediate
    region is quoted up front, never added later.</p></div>
  <div class="grid g3">{cards}</div>
 </div>
</section>

<section class="sec-paper">
 <div class="wrap">
  <div class="sec-head"><h2>Every county in California</h2>
   <p>Statewide means statewide. If it is in California, we will quote it.</p></div>
  <ul class="county-list">{counties}</ul>
 </div>
</section>

<section>
 <div class="wrap">
  <div class="split">
   <div>
    <h2>Multi-property portfolios</h2>
    <p>If you hold buildings across several regions, the usual problem is not the inspection
     &mdash; it is ending up with six different vendors, six report formats and six renewal
     dates that nobody is tracking.</p>
    <p>We inspect the whole portfolio on one schedule, deliver one format, and hand back a
     single register of what was found and when each property comes round again. For
     management companies that is the difference between a compliance programme and a
     recurring fire drill.</p>
    <p style="margin-top:1.6rem"><a class="btn btn-solid btn-lg" href="/contact.html">Talk about a portfolio {ic_a}</a></p>
   </div>
   <div>{form}</div>
  </div>
 </div>
</section>

{cta}
""".format(cards=cards, ic_a=svg("arrow"),
           counties="".join("<li>%s County</li>" % c for c in COUNTIES),
           form=quote_form("coverage"), cta=cta())
    write("coverage.html", head(
        "Service Area | All 58 California Counties | California Inspector Group",
        "CASp and SB 721 / SB 326 inspections across every California county, grouped by "
        "region, with portfolio scheduling for multi-property owners.",
        "/coverage.html") + body + foot())


def build_area_pages():
    for slug, name, counties, blurb in REGIONS:
        plain = name.replace("&amp;", "&")
        others = [(s, n) for s, n, _, _ in REGIONS if s != slug]
        body = phead(
            "%s" % name,
            blurb,
            [("Home", "/index.html"), ("Coverage", "/coverage.html"), (name, None)]) + """
<section>
 <div class="wrap">
  <div class="split">
   <div>
    <h2>Counties we cover here</h2>
    <div class="tags" style="margin-bottom:1.6rem">{tags}</div>
    <p>{blurb}</p>
    <p>Both service lines are available throughout the region: CASp accessibility inspections
     for any building open to the public, and SB&nbsp;721 or SB&nbsp;326 balcony inspections
     for multifamily and association-maintained properties.</p>
    <p>Scheduling in this region is usually within two weeks. If you are working to a
     deadline or responding to a claim, say so when you call and we will work around it.</p>
    <p style="margin-top:1.6rem">
     <a class="btn btn-solid btn-lg" href="tel:{tel}">{ic_p} {ph}</a>
     <a class="btn btn-line btn-lg" href="/contact.html">Request a quote</a>
    </p>
   </div>
   <div>{form}</div>
  </div>
 </div>
</section>

<section class="sec-paper">
 <div class="wrap">
  <div class="sec-head"><h2>What we are usually called for in {plain}</h2></div>
  {cards}
 </div>
</section>

<section>
 <div class="wrap">
  <div class="sec-head"><h2>Other regions</h2></div>
  <div class="tags">{others}</div>
 </div>
</section>

{cta}
""".format(tags="".join('<span class="tag">%s County</span>' % c for c in counties),
           blurb=blurb, plain=plain, tel=TEL, ph=PH, ic_p=svg("phone"),
           form=quote_form("area-" + slug, "Get a quote in %s" % plain,
                           "Send the property details and we&rsquo;ll come back with a flat price."),
           cards=service_mini(SERVICES[:4]),
           others="".join('<a class="tag" href="/areas/%s.html">%s</a>' % (s, n) for s, n in others),
           cta=cta())
        write("areas/%s.html" % slug, head(
            "%s | CASp &amp; Balcony Inspections | California Inspector Group" % name,
            "CASp accessibility inspections and SB 721 / SB 326 balcony inspections across "
            "%s." % plain,
            "/areas/%s.html" % slug) + body + foot())


# ============================================================ reviews

def build_reviews():
    body = phead(
        "Reviews",
        "What owners, boards and managers say about working with California Inspector Group.",
        [("Home", "/index.html"), ("Reviews", None)]) + """
<section>
 <div class="wrap">
  {feat}
  {revs}
  <div class="note" style="margin-top:2.4rem">
   <b>Every engagement ends with an ask.</b>
   We request a short review after the report is delivered &mdash; and we publish what
   clients actually say, not a curated highlight reel. If we inspected your property and
   you have feedback, good or bad, <a href="/contact.html">we want it</a>.
  </div>
 </div>
</section>
{cta}
""".format(feat=review_feature(next(r for r in REVIEWS if r.get("feat"))),
           revs=review_cards([r for r in REVIEWS if not r.get("feat")]),
           cta=cta("Join the list",
                   "Book the inspection online in about four minutes, or start with a "
                   "fifteen-minute call."))
    write("reviews.html", head(
        "Reviews | California Inspector Group",
        "Reviews from California owners, HOA boards and property managers on CASp and "
        "SB 721 / SB 326 inspections.",
        "/reviews.html") + body + foot())


# ============================================================ faq / contact

def build_faq():
    body = phead(
        "Questions",
        "The things people ask on the first call, answered at the length they deserve.",
        [("Home", "/index.html"), ("FAQ", None)]) + """
<section>
 <div class="wrap narrow">
  {faq}
  <div class="note" style="margin-top:2.4rem">
   <b>Still not sure?</b>
   Call. Working out which mandate applies to a property takes about five minutes and we do
   not charge for the conversation.
  </div>
 </div>
</section>
{cta}
""".format(faq=faq_block(FAQ, with_filter=True), cta=cta())
    write("faq.html", head(
        "FAQ | CASp &amp; SB 721 / SB 326 Inspections | California Inspector Group",
        "Answers on CASp certification, qualified defendant status, Unruh Act damages, SB 721 "
        "and SB 326 scope, deadlines, sampling and who may sign the reports.",
        "/faq.html") + body + faq_schema(FAQ) + foot())


def build_contact():
    body = phead(
        "Contact",
        "Tell us the property and what you are dealing with. We reply the same business day, "
        "and the first conversation is free.",
        [("Home", "/index.html"), ("Contact", None)]) + """
<section>
 <div class="wrap">
  <div class="split">
   <div>
    <h2>Talk to an inspector</h2>
    <p class="lede">Not a call centre and not a form that disappears. You get Robert or
     someone who has walked the kind of building you are calling about.</p>

    <div class="grid" style="gap:.9rem;margin:2rem 0">
     <a class="card" href="tel:{tel}" style="display:flex;gap:1rem;align-items:center">
      <div class="card-ic" style="margin:0">{ic_p}</div>
      <div><h3 style="margin:0">{ph}</h3><p>Call or text &mdash; fastest route</p></div></a>
     <a class="card" href="mailto:{em}" style="display:flex;gap:1rem;align-items:center">
      <div class="card-ic" style="margin:0">{ic_m}</div>
      <div><h3 style="margin:0;word-break:break-all">{em}</h3><p>Send plans, photos or a prior report</p></div></a>
     <div class="card" style="display:flex;gap:1rem;align-items:center">
      <div class="card-ic" style="margin:0">{ic_g}</div>
      <div><h3 style="margin:0">All 58 counties</h3><p>Statewide California &mdash; travel quoted up front</p></div></div>
     <div class="card" style="display:flex;gap:1rem;align-items:center;flex-wrap:wrap">
      <div class="card-ic" style="margin:0">{ic_cal}</div>
      <div style="flex:1;min-width:200px"><h3 style="margin:0">Prefer to pick a time?</h3><p>Fifteen minutes, no obligation</p></div>
      {demo_card}</div>
    </div>

    <h3>What to have ready</h3>
    <ul class="checks">
     <li>{ck}<span>Property address and, for multifamily, the unit count</span></li>
     <li>{ck}<span>Approximate year built, and any major remodels</span></li>
     <li>{ck}<span>How many balconies, walkways or exterior stairs, if any</span></li>
     <li>{ck}<span>Whether you have been served with anything &mdash; and when</span></li>
    </ul>

    <div class="note note-warn">
     <b>If you have been served with a claim, say so first.</b>
     Correction windows run from the date of service and they are short. Call rather than
     email so we can get you on the schedule the same week.
    </div>
   </div>
   <div>{form}</div>
  </div>
 </div>
</section>
""".format(tel=TEL, ph=PH, em=EM, ic_p=svg("phone"), ic_m=svg("mail"), ic_g=svg("geo"),
           ic_cal=svg("calendar"), demo_card=demo_btn(),
           ck=svg("check"),
           form=quote_form("contact", "Request a quote",
                           "Flat price, same business day reply. The more detail you give us, "
                           "the tighter the number."))
    write("contact.html", head(
        "Contact | California Inspector Group",
        "Call 408-600-7165 or send the property details for a flat-price quote on a CASp or "
        "SB 721 / SB 326 inspection anywhere in California.",
        "/contact.html") + body + foot())


# ============================================================ utility pages

def build_thanks():
    body = """
<section style="padding:clamp(4rem,10vw,7rem) 0">
 <div class="wrap narrow center">
  <div class="card-ic" style="margin:0 auto 1.6rem;width:64px;height:64px;background:var(--green-wash);color:var(--green)">
   <svg class="ic" style="width:32px;height:32px" viewBox="0 0 24 24" fill="none" stroke="currentColor"
        stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20 6L9 17l-5-5"/></svg>
  </div>
  <h1>Thank you &mdash; that reached us</h1>
  <p class="lede">We reply the same business day. If your matter is time-sensitive &mdash; a
   claim you have been served with, or a deadline you are already past &mdash; call and we
   will move you up the schedule.</p>
  <p style="margin-top:2rem">
   <a class="btn btn-solid btn-lg" href="tel:{tel}">{ic_p} {ph}</a>
   <a class="btn btn-line btn-lg" href="/index.html">Back to the site</a>
  </p>
  <hr>
  <h2 style="font-size:1.3rem">While you wait</h2>
  <div class="grid g2" style="margin-top:1.4rem;text-align:left">
   <a class="card" href="/casp.html"><h3>What a CASp inspection is</h3>
    <p>The certification, the report, and how qualified defendant status actually works.</p></a>
   <a class="card card-s" href="/balcony-inspections.html"><h3>The balcony laws</h3>
    <p>SB 721 and SB 326: who is in scope, the deadlines that have passed, and what gets inspected.</p></a>
  </div>
 </div>
</section>
""".format(tel=TEL, ph=PH, ic_p=svg("phone"))
    write("thank-you.html", head(
        "Thank you | California Inspector Group",
        "Your request reached us. We reply the same business day.",
        "/thank-you.html") + body + foot())


def build_404():
    body = """
<section style="padding:clamp(4rem,10vw,7rem) 0">
 <div class="wrap narrow center">
  <p class="eyebrow eyebrow-a">Error 404</p>
  <h1>That page is not here</h1>
  <p class="lede">The link may be old, or we may have moved it. Everything on the site is one
   click away below.</p>
  <p style="margin:2rem 0">
   <a class="btn btn-solid btn-lg" href="/index.html">Go to the homepage</a>
   <a class="btn btn-line btn-lg" href="/contact.html">Contact us</a>
  </p>
  <div class="grid g2" style="text-align:left">
   <a class="card" href="/casp.html"><h3>What is CASp?</h3><p>Accessibility inspections explained.</p></a>
   <a class="card card-s" href="/balcony-inspections.html"><h3>Balcony law</h3><p>SB 721 and SB 326 explained.</p></a>
   <a class="card" href="/services.html"><h3>Services</h3><p>Everything we do.</p></a>
   <a class="card" href="/coverage.html"><h3>Coverage</h3><p>All 58 California counties.</p></a>
  </div>
 </div>
</section>
"""
    write("404.html", head("Page not found | California Inspector Group",
                          "That page could not be found.", "/404.html") + body + foot())


def build_sitemap():
    groups = [
        ("Main", [("Home", "/index.html"), ("Services", "/services.html"),
                  ("How it works", "/process.html"), ("About", "/about.html"),
                  ("Reviews", "/reviews.html"),
                  ("Coverage", "/coverage.html"), ("FAQ", "/faq.html"),
                  ("Contact", "/contact.html")]),
        ("Book &amp; pay", [("Book an inspection", "/book.html"), ("Pricing", "/pricing.html"),
                            ("Example checkout", "/checkout.html"),
                            ("The inspection agreement", "/agreement.html"),
                            ("Client portal", "/portal.html")]),
        ("Learn", [("What is CASp?", "/casp.html"),
                   ("SB 721 &amp; SB 326 balcony law", "/balcony-inspections.html"),
                   ("Sample CASp report", "/samples/casp-report.html"),
                   ("Sample SB 721 report", "/samples/sb721-report.html")]),
        ("Accessibility services", [(s["name"], "/services/%s.html" % s["slug"]) for s in ACCESS_SERVICES]),
        ("Structural services", [(s["name"], "/services/%s.html" % s["slug"]) for s in STRUCT_SERVICES]),
        ("Regions", [(n, "/areas/%s.html" % s) for s, n, _, _ in REGIONS]),
    ]
    cols = "".join(
        '<div><h3>%s</h3><ul>%s</ul></div>'
        % (title, "".join('<li><a href="%s">%s</a></li>' % (h, t) for t, h in links))
        for title, links in groups)
    body = phead("Sitemap", "Every page on the site.",
                 [("Home", "/index.html"), ("Sitemap", None)]) + """
<section><div class="wrap"><div class="grid g3">{cols}</div></div></section>
""".format(cols=cols)
    write("sitemap.html", head("Sitemap | California Inspector Group",
                              "Every page on the California Inspector Group site.",
                              "/sitemap.html") + body + foot())


def build_static():
    # Demo: block every crawler so this can never outrank the client's real site.
    write("robots.txt", "User-agent: *\nDisallow: /\n")

    write("assets/img/favicon.svg", """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">
<rect width="64" height="64" rx="13" fill="#0B1B2B"/>
<path d="M32 12l16 6.6v13.6c0 10.2-6.8 18.6-16 21-9.2-2.4-16-10.8-16-21V18.6z"
      fill="none" stroke="#1263B8" stroke-width="4" stroke-linejoin="round"/>
<path d="M23 33.5l6.5 6.5L42 27.5" fill="none" stroke="#fff" stroke-width="5"
      stroke-linecap="round" stroke-linejoin="round"/>
</svg>
""")


# ============================================================ main

def main():
    build_home()
    build_casp()
    build_balcony()
    build_services()
    build_service_pages()
    build_process()
    build_about()
    build_coverage()
    build_area_pages()
    build_reviews()
    build_faq()
    build_contact()
    build_thanks()
    build_404()
    build_sitemap()
    build_static()

    commerce.build_pricing(write)
    commerce.build_book(write)
    commerce.build_agreement(write)
    commerce.build_portal(write)
    commerce.build_checkout(write)
    report_docs.build(write)

    import start_page
    start_page.build(write)

    print("built %d files" % len(PAGES))
    for p in sorted(PAGES):
        print("  ", p)


if __name__ == "__main__":
    main()
