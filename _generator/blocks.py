# -*- coding: utf-8 -*-
"""Reusable page sections shared across the site."""
from data import BIZ, FORM_ACTION, SERVICES, ACCESS_SERVICES, STRUCT_SERVICES, FAQ, PROCESS
from chrome import svg, TEL, PH, EM


def img(name, alt, cls="", loading="lazy", sizes=""):
    """<picture> with a webp first and the jpg as the fallback."""
    return ('<picture><source srcset="/assets/img/%s.webp" type="image/webp">'
            '<img src="/assets/img/%s.jpg" alt="%s" class="%s" loading="%s" decoding="async"%s>'
            '</picture>' % (name, name, alt, cls, loading, sizes))


def phead(title, sub, crumbs=None, amber=False):
    cr = ""
    if crumbs:
        parts = " / ".join('<a href="%s">%s</a>' % (h, t) if h else t for t, h in crumbs)
        cr = '<p class="crumb">%s</p>' % parts
    return ('<section class="phead%s"><div class="wrap phead-in">%s<h1>%s</h1><p>%s</p>'
            '</div></section>' % (" amber" if amber else "", cr, title, sub))


# ------------------------------------------------------------- service grids

def service_cards(services, tagged=True):
    out = []
    for s in services:
        s_cls = " svc-s" if s["line"] == "structural" else ""
        tag = "Accessibility" if s["line"] == "access" else "Structural"
        out.append(
            '<a class="card svc%s" href="/services/%s.html">'
            '<div class="svc-img">%s</div>'
            '<div class="svc-body">%s<h3>%s</h3><p>%s</p>'
            '<span class="card-more">Read more %s</span></div></a>'
            % (s_cls, s["slug"], img(s["img"], ""),
               ('<span class="svc-tag">%s</span>' % tag) if tagged else "",
               s["name"], s["teaser"], svg("arrow")))
    return '<div class="grid g3">%s</div>' % "".join(out)


def service_mini(services):
    out = []
    for s in services:
        cls = " card-s" if s["line"] == "structural" else ""
        out.append('<a class="card%s" href="/services/%s.html">'
                   '<div class="card-ic">%s</div><h3>%s</h3><p>%s</p>'
                   '<span class="card-more">Read more %s</span></a>'
                   % (cls, s["slug"], svg(s["icon"]), s["name"], s["teaser"], svg("arrow")))
    return '<div class="grid g2">%s</div>' % "".join(out)


# --------------------------------------------------------------------- faq

def faq_block(items, with_filter=False):
    pills = ""
    if with_filter:
        pills = ('<div class="pills" role="group" aria-label="Filter questions">'
                 '<button class="pill" type="button" data-filter="all" aria-pressed="true">All questions</button>'
                 '<button class="pill" type="button" data-filter="access" aria-pressed="false">Accessibility &mdash; CASp</button>'
                 '<button class="pill" type="button" data-filter="structural" aria-pressed="false">Structural &mdash; SB 721 / 326</button>'
                 '<button class="pill" type="button" data-filter="general" aria-pressed="false">Working with us</button>'
                 '</div>')
    rows = []
    for i, (cat, q, a) in enumerate(items):
        rows.append(
            '<div class="faq-item" data-cat="%s" data-open="0">'
            '<button type="button" class="faq-q" aria-expanded="false" aria-controls="fa%d">%s</button>'
            '<div class="faq-a" id="fa%d"><p>%s</p></div></div>' % (cat, i, q, i, a))
    return pills + '<div class="faq-list">%s</div>' % "".join(rows)


def faq_schema(items):
    """FAQPage JSON-LD. Harmless on a noindex demo, correct the day it goes live."""
    import json
    ents = [{"@type": "Question", "name": _strip(q),
             "acceptedAnswer": {"@type": "Answer", "text": _strip(a)}}
            for _, q, a in items]
    return ('<script type="application/ld+json">%s</script>'
            % json.dumps({"@context": "https://schema.org", "@type": "FAQPage",
                          "mainEntity": ents}))


def _strip(s):
    import re
    s = re.sub(r"<[^>]+>", "", s)
    for a, b in (("&sect;", "§"), ("&mdash;", "—"), ("&lsquo;", "‘"), ("&rsquo;", "’"),
                 ("&amp;", "&"), ("&hellip;", "…"), ("&ndash;", "–")):
        s = s.replace(a, b)
    return s


# -------------------------------------------------------------------- form

SUBJECTS = [
    ("", "What do you need? — select one"),
    ("CASp inspection", "CASp accessibility inspection"),
    ("CASp plan review", "Pre-construction plan review"),
    ("Served with a claim", "I have been served with a claim or demand letter"),
    ("Lease disclosure", "Commercial lease / §1938 disclosure"),
    ("SB 721 inspection", "SB 721 balcony inspection (apartments)"),
    ("SB 326 inspection", "SB 326 balcony inspection (condo / HOA)"),
    ("Both", "Both accessibility and structural"),
    ("Not sure", "I am not sure which one I need"),
]

PROPERTY_TYPES = [
    ("", "Property type — select one"),
    ("Retail or restaurant", "Retail or restaurant"),
    ("Office or medical", "Office or medical"),
    ("Apartment building", "Apartment building (3+ units)"),
    ("Condo or HOA", "Condominium or HOA"),
    ("Hotel or hospitality", "Hotel or hospitality"),
    ("Industrial or warehouse", "Industrial or warehouse"),
    ("Public agency", "Public agency facility"),
    ("Other", "Something else"),
]


def _opts(pairs, name=""):
    return "".join('<option value="%s"%s>%s</option>'
                   % (v, ' selected' if v == "" else "", t) for v, t in pairs)


def quote_form(source="page", heading="Request a quote",
               sub="Tell us the property and we&rsquo;ll come back with a flat price. "
                   "No hourly surprises."):
    return """
<div class="form-card">
 <h2>{heading}</h2>
 <p>{sub}</p>
 <form action="{action}" method="POST" class="quote-form" enctype="multipart/form-data" data-source="{source}">
  <div class="fgrid">
   <div class="field"><label for="q-name-{source}">Name <span class="req">*</span></label>
    <input id="q-name-{source}" name="name" type="text" autocomplete="name" required></div>
   <div class="field"><label for="q-phone-{source}">Phone <span class="req">*</span></label>
    <input id="q-phone-{source}" name="phone" type="tel" autocomplete="tel" required></div>
   <div class="field"><label for="q-email-{source}">Email <span class="req">*</span></label>
    <input id="q-email-{source}" name="email" type="email" autocomplete="email" required></div>
   <div class="field"><label for="q-company-{source}">Company or association</label>
    <input id="q-company-{source}" name="business" type="text" autocomplete="organization"></div>
   <div class="field full"><label for="q-addr-{source}">Property address <span class="req">*</span></label>
    <input id="q-addr-{source}" name="property_address" type="text" autocomplete="street-address" required
           placeholder="Street, city, county"></div>
   <div class="field"><label for="q-svc-{source}">Service needed <span class="req">*</span></label>
    <select id="q-svc-{source}" name="service_needed" required>{svc}</select></div>
   <div class="field"><label for="q-type-{source}">Property type</label>
    <select id="q-type-{source}" name="business_type">{ptype}</select></div>
   <div class="field full"><label for="q-msg-{source}">Anything we should know?</label>
    <textarea id="q-msg-{source}" name="message"
      placeholder="Square footage, number of units, how many balconies or walkways, whether you have been served, deadlines you are working to."></textarea></div>
   <div class="field full">
    <label for="q-photos-{source}">Photos of the property <span style="font-weight:400;color:var(--mute)">&mdash; optional</span></label>
    <label class="upl" for="q-photos-{source}">
     <input id="q-photos-{source}" name="upload" type="file" accept="image/*" multiple>
     {cam}<span><b>Add photos</b> &mdash; they help us hold the quote. Material discrepancies
      found on site are re-quoted before we proceed.</span>
    </label>
    <div class="upl-list" hidden></div>
   </div>
  </div>
  <input type="hidden" name="source" value="IGC site &mdash; {source}">
  <input type="hidden" name="_next" value="">
  <input type="hidden" name="landing_page" value="{source}">
  <input type="hidden" name="fill_seconds" value="">
  <input type="hidden" name="traffic_source" value="">
  <input type="hidden" name="utm_campaign" value="">
  <input type="hidden" name="utm_content" value="">
  <input class="hp" type="text" name="_gotcha" tabindex="-1" autocomplete="off" aria-hidden="true">
  <button class="btn btn-solid btn-lg btn-full" type="submit">Request a quote {arrow}</button>
  <p class="form-note">We reply the same business day. We do not sell or share your details,
   and we do not sell the repairs we recommend.</p>
 </form>
</div>
""".format(heading=heading, sub=sub, action=FORM_ACTION, source=source,
           svc=_opts(SUBJECTS), ptype=_opts(PROPERTY_TYPES), arrow=svg("arrow"),
           cam=svg("camera"))


# ------------------------------------------------------------------ process

def process_steps(items=None):
    items = items or PROCESS
    return '<div class="steps">%s</div>' % "".join(
        '<div class="step"><h3>%s</h3><p>%s</p></div>' % (t, d) for t, d in items)


def stat_row(stats, dark=False):
    return '<div class="stat-row">%s</div>' % "".join(
        '<div class="stat"><b>%s</b><span>%s</span></div>' % (n, l) for n, l in stats)


# ----------------------------------------------------------------- reviews

def stars():
    s = ('<svg viewBox="0 0 24 24" fill="currentColor" stroke="none" aria-hidden="true">'
         '<path d="M12 3l2.7 5.6 6.3.9-4.5 4.4 1 6.1-5.5-2.9L6.5 20l1-6.1L3 9.5l6.3-.9z"/></svg>')
    return '<span class="rev-stars" role="img" aria-label="Five out of five stars">%s</span>' % (s * 5)


def _initials(name):
    parts = name.replace(".", "").split()
    return "".join(p[0] for p in parts[:2]).upper()


def review_cards(items):
    out = []
    for r in items:
        amber = ' rev-s' if r["line"] == "structural" else ''
        out.append(
            '<figure class="rev%s">%s<blockquote><p>&ldquo;%s&rdquo;</p></blockquote>'
            '<figcaption class="rev-who"><span class="rev-av" aria-hidden="true">%s</span>'
            '<span><b>%s</b><i>%s &middot; %s</i></span></figcaption></figure>'
            % (amber, stars(), r["q"], _initials(r["name"]),
               r["name"], r["role"], r["where"]))
    return '<div class="revs">%s</div>' % "".join(out)


def review_feature(r):
    return ('<figure class="rev-feat">%s<blockquote><p>&ldquo;%s&rdquo;</p></blockquote>'
            '<figcaption>%s &middot; %s, %s</figcaption></figure>'
            % (stars(), r["q"], r["name"], r["role"], r["where"]))


def review_pull(r):
    """Compact single review for service pages and sidebars."""
    amber = ' rev-s' if r["line"] == "structural" else ''
    return ('<figure class="rev rev-solo%s">%s<blockquote><p>&ldquo;%s&rdquo;</p></blockquote>'
            '<figcaption class="rev-who"><span class="rev-av" aria-hidden="true">%s</span>'
            '<span><b>%s</b><i>%s &middot; %s</i></span></figcaption></figure>'
            % (amber, stars(), r["q"], _initials(r["name"]), r["name"], r["role"], r["where"]))
