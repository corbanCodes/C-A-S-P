# -*- coding: utf-8 -*-
"""Shared page chrome: demo bar, <head>, nav, footer, CTA band and the icon set.

Every page on the site is wrapped by head() and foot(). The demo carries
noindex on every page, a blanket robots.txt disallow, and a persistent demo
bar so nobody mistakes the wiring for live: forms post to the 60MS Formspree
endpoints (real), payments and e-signature are staged hand-offs (not yet).

"Book a demo" opens Corban's 60MS Calendly in a popup (lazy-loaded); any
element with data-calendly gets the behaviour, and the plain href works as a
new-tab fallback without JS.
"""
from data import BIZ, CALENDLY, ACCESS_SERVICES, STRUCT_SERVICES

TEL = BIZ["phone"].replace("-", "")
PH = BIZ["phone"]
EM = BIZ["email"]
CAL = CALENDLY

# ------------------------------------------------------------------ icon set

ICONS = {
    "shield": '<path d="M12 3l7 3v6c0 4.4-3 8.2-7 9-4-.8-7-4.6-7-9V6l7-3z"/>',
    "check": '<path d="M20 6L9 17l-5-5"/>',
    "alert": '<path d="M12 9v4m0 4h.01M10.3 3.9L2.4 17.3A2 2 0 004.1 20.3h15.8a2 2 0 001.7-3L13.7 3.9a2 2 0 00-3.4 0z"/>',
    "phone": '<path d="M22 16.9v3a2 2 0 01-2.2 2 19.8 19.8 0 01-8.6-3.1 19.5 19.5 0 01-6-6A19.8 19.8 0 012.1 4.2 2 2 0 014.1 2h3a2 2 0 012 1.7c.1 1 .4 1.9.7 2.8a2 2 0 01-.5 2.1L8.1 9.9a16 16 0 006 6l1.3-1.3a2 2 0 012.1-.4c.9.3 1.8.6 2.8.7a2 2 0 011.7 2z"/>',
    "mail": '<path d="M4 4h16v16H4z"/><path d="M4 6l8 6 8-6"/>',
    "geo": '<path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0118 0z"/><circle cx="12" cy="10" r="3"/>',
    "clock": '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
    "doc": '<path d="M14 2H6a2 2 0 00-2 2v16a2 2 0 002 2h12a2 2 0 002-2V8z"/><path d="M14 2v6h6"/><path d="M8 13h8M8 17h6"/>',
    "plans": '<path d="M3 5h18v14H3z"/><path d="M3 10h18M9 5v14"/>',
    "building": '<path d="M4 21V5a1 1 0 011-1h9a1 1 0 011 1v16"/><path d="M15 9h4a1 1 0 011 1v11"/><path d="M8 8h3M8 12h3M8 16h3M2 21h20"/>',
    "hoa": '<path d="M3 21V10l6-4 6 4v11"/><path d="M15 21V13l6-3v11"/><path d="M2 21h20M7 21v-5h4v5"/>',
    "storefront": '<path d="M3 9l1.5-5h15L21 9"/><path d="M4 9v11a1 1 0 001 1h14a1 1 0 001-1V9"/><path d="M3 9a3 3 0 006 0 3 3 0 006 0 3 3 0 006 0"/><path d="M9 21v-6h6v6"/>',
    "bed": '<path d="M2 20v-9h20v9"/><path d="M2 13V6M22 13h-9a3 3 0 00-3-3H6"/>',
    "keys": '<circle cx="8" cy="14" r="4"/><path d="M11 11l9-9 2 2-2 2 2 2-3 3-2-2-2 2"/>',
    "arrow": '<path d="M5 12h14M13 6l6 6-6 6"/>',
    "ruler": '<path d="M2 15l13-13 7 7-13 13z"/><path d="M7 10l2 2M10 7l2 2M4 13l2 2"/>',
    "scale": '<path d="M12 3v18M7 21h10"/><path d="M4 8h16M6 8l-3 6h6zM18 8l-3 6h6z"/>',
    "calendar": '<path d="M4 5h16v16H4z"/><path d="M4 10h16M8 3v4M16 3v4"/>',
    "search": '<circle cx="11" cy="11" r="7"/><path d="M20 20l-4-4"/>',
    "star": '<path d="M12 3l2.7 5.6 6.3.9-4.5 4.4 1 6.1-5.5-2.9L6.5 20l1-6.1L3 9.5l6.3-.9z"/>',
    "card": '<rect x="2" y="5" width="20" height="14" rx="2.5"/><path d="M2 10h20M6 15h4"/>',
    "bank": '<path d="M3 10h18M12 3l9 5H3zM5 10v8M10 10v8M14 10v8M19 10v8M3 21h18"/>',
    "wire": '<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c2.5 2.7 3.8 5.7 3.8 9s-1.3 6.3-3.8 9c-2.5-2.7-3.8-5.7-3.8-9S9.5 5.7 12 3z"/>',
    "lock": '<rect x="4" y="10" width="16" height="11" rx="2.5"/><path d="M8 10V7a4 4 0 018 0v3"/>',
    "unlock": '<rect x="4" y="10" width="16" height="11" rx="2.5"/><path d="M8 10V7a4 4 0 017.5-2"/>',
    "sign": '<path d="M3 20c3.5 0 3.5-14 7-14s3.5 11 7 11c1.6 0 2.4-1 3-2"/><path d="M3 20h18"/>',
    "tag": '<path d="M20.6 13.4L12 22l-9-9V3h10l7.6 7.6a2 2 0 010 2.8z"/><circle cx="7.5" cy="7.5" r="1.4"/>',
    "spark": '<path d="M12 2l1.9 6.1L20 10l-6.1 1.9L12 18l-1.9-6.1L4 10l6.1-1.9z"/>',
}


def svg(name, cls="ic"):
    return ('<svg class="%s" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
            'stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" '
            'aria-hidden="true">%s</svg>' % (cls, ICONS.get(name, ICONS["check"])))


def demo_btn(label="Book a demo", cls="btn btn-soft"):
    """Calendly popup trigger; plain link fallback without JS."""
    return ('<a class="%s" href="%s" target="_blank" rel="noopener" data-calendly>%s</a>'
            % (cls, CAL, label))


def demo_bar():
    return ("""
<div class="demo-bar" id="demo-bar" role="note">
 <p><span class="demo-dot" aria-hidden="true"></span><b>Demo preview</b><span class="demo-sep"></span>
  <span class="demo-long">forms post to a test inbox &mdash; payments &amp; e-signature are not
  connected.</span><span class="demo-short">payments not connected.</span>
  Built by <a href="https://60minutesites.com" rel="noopener" target="_blank">60 Minute Sites</a></p>
 <a class="demo-bar-cta" href="%s" target="_blank" rel="noopener" data-calendly>Book a demo %s</a>
</div>""" % (CAL, svg("arrow", "ic ic-sm")))


# ------------------------------------------------------------------ head / nav

def head(title, desc, path="/", extra_css="", body_class=""):
    canonical = BIZ["base"].rstrip("/") + path
    return """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="robots" content="noindex,nofollow">
<link rel="canonical" href="{canonical}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="website">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{base}/assets/img/plaza-ramp.jpg">
<meta name="theme-color" content="#0B1B2B">
<link rel="icon" href="/assets/img/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Archivo:wght@500;600;700;800&family=Fraunces:ital,opsz,wght@0,9..144,500..700;1,9..144,500..700&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/css/main.css">
{extra_css}
</head>
<body class="{body_class}">
<a class="skip" href="#main">Skip to content</a>
{bar}
{nav}
<main id="main">
""".format(title=title, desc=desc, canonical=canonical, base=BIZ["base"],
           extra_css=extra_css, body_class=body_class, bar=demo_bar(), nav=nav())


def nav():
    acc = "".join(
        '<a href="/services/%s.html"><b>%s</b><span>%s</span></a>' % (s["slug"], s["name"], s["teaser"][:78] + "&hellip;")
        for s in ACCESS_SERVICES)
    st = "".join(
        '<a href="/services/%s.html"><b>%s</b><span>%s</span></a>' % (s["slug"], s["name"], s["teaser"][:78] + "&hellip;")
        for s in STRUCT_SERVICES)
    return """
<header class="nav" id="nav">
 <div class="nav-in">
  <a class="brand" href="/index.html">
   <span class="brand-mark" aria-hidden="true">CIG</span>
   <span class="brand-txt"><b>California Inspector Group</b><i>CASp &amp; SB 721 / SB 326</i></span>
  </a>

  <nav class="nav-links" aria-label="Main">
   <div class="has-menu">
    <button type="button" class="nav-top" aria-expanded="false">Services {caret}</button>
    <div class="menu">
     <div class="menu-col">
      <p class="menu-head"><i class="dot dot-a"></i>Accessibility &mdash; CASp</p>
      {acc}
     </div>
     <div class="menu-col">
      <p class="menu-head"><i class="dot dot-s"></i>Structural &mdash; SB 721 / SB 326</p>
      {st}
     </div>
    </div>
   </div>
   <a href="/pricing.html">Pricing</a>
   <div class="has-menu">
    <button type="button" class="nav-top" aria-expanded="false">Learn {caret}</button>
    <div class="menu menu-1">
     <div class="menu-col">
      <a href="/casp.html"><b>What is CASp?</b><span>The certification, the report, qualified defendant status</span></a>
      <a href="/balcony-inspections.html"><b>The balcony laws</b><span>SB 721 and SB 326 scope, deadlines and cycles</span></a>
      <a href="/process.html"><b>How it works</b><span>From first call to report on your desk</span></a>
      <a href="/agreement.html"><b>The inspection agreement</b><span>What you are signing, section by section</span></a>
      <a href="/portal.html"><b>Client portal</b><span>Where the engagement and the report live</span></a>
      <a href="/faq.html"><b>FAQ</b><span>Everything people ask on the first call</span></a>
     </div>
    </div>
   </div>
   <a href="/coverage.html">Coverage</a>
   <a href="/about.html">About</a>
  </nav>

  <div class="nav-cta">
   <a class="btn btn-ghost nav-tel" href="tel:{tel}" aria-label="Call {ph}">{ic_p}<span>{ph}</span></a>
   {demo}
   <a class="btn btn-solid" href="/book.html">Book an inspection</a>
  </div>

  <button type="button" class="burger" id="burger" aria-label="Menu" aria-expanded="false">
   <span></span><span></span><span></span>
  </button>
 </div>

 <div class="mobile" id="mobile">
  <div class="m-cta m-cta-top">
   <a class="btn btn-solid btn-full" href="/book.html">Book an inspection</a>
   {demo_full}
  </div>
  <a href="/pricing.html">Pricing</a>
  <a href="/services.html">All services</a>
  <p class="m-head">Accessibility &mdash; CASp</p>
  {m_acc}
  <p class="m-head">Structural &mdash; SB 721 / SB 326</p>
  {m_st}
  <p class="m-head">Learn</p>
  <a href="/casp.html">What is CASp?</a>
  <a href="/balcony-inspections.html">Balcony inspection law</a>
  <a href="/process.html">How it works</a>
  <a href="/agreement.html">The inspection agreement</a>
  <a href="/coverage.html">Where we work</a>
  <a href="/about.html">About</a>
  <a href="/faq.html">FAQ</a>
  <a href="/portal.html">Client portal</a>
  <div class="m-cta">
   <a class="btn btn-line btn-full" href="tel:{tel}">{ic_p} {ph}</a>
  </div>
 </div>
</header>
""".format(acc=acc, st=st, tel=TEL, ph=PH, ic_p=svg("phone"),
           demo=demo_btn(),
           demo_full=demo_btn(cls="btn btn-soft btn-full"),
           caret='<svg class="cv" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M6 9l6 6 6-6"/></svg>',
           m_acc="".join('<a href="/services/%s.html">%s</a>' % (s["slug"], s["name"]) for s in ACCESS_SERVICES),
           m_st="".join('<a href="/services/%s.html">%s</a>' % (s["slug"], s["name"]) for s in STRUCT_SERVICES))


# ------------------------------------------------------------------ cta / foot

def cta(title="Find out where you actually stand",
        sub="Book the inspection online in about four minutes, or grab fifteen minutes on a "
            "call first &mdash; it is usually enough to tell you which mandate applies and "
            "what it costs.",
        variant=""):
    return """
<section class="cta {variant}">
 <div class="wrap cta-in">
  <div>
   <h2>{title}</h2>
   <p>{sub}</p>
  </div>
  <div class="cta-btns">
   <a class="btn btn-solid btn-lg" href="/book.html">Book an inspection {ic_a}</a>
   {demo}
   <a class="btn btn-ghost btn-lg cta-tel" href="tel:{tel}">{ic_p} {ph}</a>
  </div>
 </div>
</section>
""".format(title=title, sub=sub, variant=variant, tel=TEL, ph=PH,
           demo=demo_btn(cls="btn btn-line btn-lg"),
           ic_p=svg("phone"), ic_a=svg("arrow"))


def foot():
    acc = "".join('<li><a href="/services/%s.html">%s</a></li>' % (s["slug"], s["name"])
                  for s in ACCESS_SERVICES)
    st = "".join('<li><a href="/services/%s.html">%s</a></li>' % (s["slug"], s["name"])
                 for s in STRUCT_SERVICES)
    return """
</main>
<footer class="foot">
 <div class="wrap">
  <div class="foot-grid">
   <div class="foot-brand">
    <a class="brand" href="/index.html">
     <span class="brand-mark" aria-hidden="true">CIG</span>
     <span class="brand-txt"><b>California Inspector Group</b><i>LLC</i></span>
    </a>
    <p>{blurb}</p>
    <p class="foot-contact">
     <a href="tel:{tel}">{ic_p} {ph}</a>
     <a href="mailto:{em}">{ic_m} {em}</a>
     <a href="{cal}" target="_blank" rel="noopener" data-calendly>{ic_c} Book a demo</a>
    </p>
   </div>
   <div>
    <h3>Accessibility</h3>
    <ul>{acc}<li><a href="/casp.html">What is CASp?</a></li></ul>
   </div>
   <div>
    <h3>Structural</h3>
    <ul>{st}<li><a href="/balcony-inspections.html">The balcony laws</a></li></ul>
   </div>
   <div>
    <h3>Book &amp; pay</h3>
    <ul>
     <li><a href="/book.html">Book an inspection</a></li>
     <li><a href="/pricing.html">Pricing</a></li>
     <li><a href="/checkout.html">Example checkout</a></li>
     <li><a href="/agreement.html">The agreement</a></li>
     <li><a href="/portal.html">Client portal</a></li>
    </ul>
    <h3 style="margin-top:1.4rem">Company</h3>
    <ul>
     <li><a href="/about.html">About</a></li>
     <li><a href="/process.html">How it works</a></li>
     <li><a href="/coverage.html">Where we work</a></li>
     <li><a href="/faq.html">FAQ</a></li>
     <li><a href="/contact.html">Contact</a></li>
     <li><a href="/sitemap.html">Sitemap</a></li>
    </ul>
   </div>
  </div>

  <p class="disclaimer">
   <b>Not legal advice.</b> California Inspector Group performs inspections and writes
   reports. We are not a law firm, we do not provide legal representation, and nothing on
   this site creates an attorney&ndash;client relationship. Statutes are summarised for
   orientation and are current as described; retain California counsel for advice on your
   own situation and verify any citation against the code before you rely on it.
  </p>

  <div class="foot-base">
   <p>&copy; 2026 {legal}. All rights reserved.</p>
   <p>Demo preview &mdash; payments &amp; e-signature not connected &middot;
      Site by <a href="https://60minutesites.com" rel="noopener">60 Minute Sites</a></p>
  </div>
 </div>
</footer>
<script src="/assets/js/main.js" defer></script>
<script src="/assets/js/contact-widget.js" defer></script>
</body>
</html>
""".format(blurb=BIZ["blurb"], tel=TEL, ph=PH, em=EM, cal=CAL, legal=BIZ["legal"],
           acc=acc, st=st, ic_p=svg("phone"), ic_m=svg("mail"), ic_c=svg("calendar"))
