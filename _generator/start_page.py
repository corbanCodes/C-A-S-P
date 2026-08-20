# -*- coding: utf-8 -*-
"""/start.html — paid-traffic landing page.

Mirrors the 60minutesites start funnel: a short quiz, answers accumulated in JS,
one JSON POST to Formspree on the contact step so the lead lands in the CRM with
the same payload shape as every other 60MS funnel. Meta pixel calls are guarded
so they no-op until a pixel is actually added.
"""
from data import BIZ, FORM_ACTION
from chrome import head, svg, demo_bar, TEL, PH, EM
from blocks import img

STEP1 = [
    ("CASp accessibility inspection", "shield"),
    ("SB 721 balcony inspection (apartments)", "building"),
    ("SB 326 balcony inspection (condo / HOA)", "hoa"),
    ("I have been served with a claim", "alert"),
    ("Both accessibility and structural", "scale"),
    ("I am not sure which I need", "search"),
]
STEP2 = [
    ("Retail or restaurant", "storefront"),
    ("Office or medical", "doc"),
    ("Apartment building (3+ units)", "building"),
    ("Condominium or HOA", "hoa"),
    ("Hotel or hospitality", "bed"),
    ("Something else", "geo"),
]
STEP3 = [
    ("Urgent — I have been served or I am past a deadline", "alert"),
    ("Soon — within the next month", "clock"),
    ("Planning ahead", "calendar"),
    ("Just getting a price", "check"),
]


def opts(items, q):
    return "".join(
        '<button type="button" class="qopt" data-q="%s" data-a="%s">%s<span>%s</span></button>'
        % (q, a.replace("&", "and"), svg(ic), a) for a, ic in items)


def build(write):
    body = """
<div class="start">
 <div class="start-bg">{bg}</div>

 <div class="start-nav">
  <div class="wrap start-nav-in">
   <a class="brand" href="/index.html">
    <span class="brand-mark" aria-hidden="true">IGC</span>
    <span class="brand-txt"><b>Inspector Group California</b><i>CASp &amp; SB 721 / SB 326</i></span>
   </a>
   <a class="btn btn-line" href="tel:{tel}">{ic_p} <span class="hide-sm">{ph}</span></a>
  </div>
 </div>

 <div class="wrap start-in">
  <div class="start-copy" id="start-copy">
   <span class="eyebrow">{ic_g} All 58 California counties</span>
   <h1>Find out what your inspection costs</h1>
   <p>Three quick questions and we come back with a flat price &mdash; CASp accessibility,
    SB&nbsp;721 / SB&nbsp;326 balcony inspections, or both. Takes about thirty seconds.</p>
   <ul class="start-ticks">
    <li>{ck}<span>Flat price quoted before anything is scheduled</span></li>
    <li>{ck}<span>We inspect and report &mdash; we never sell you the repairs</span></li>
    <li>{ck}<span>Reports written for a lawyer, a board or a code official</span></li>
    <li>{ck}<span>Statewide, same business day reply</span></li>
   </ul>
  </div>

  <div class="quiz" id="quiz">
   <div class="qbar" aria-hidden="true">
    <i class="on" data-dot="1"></i><i data-dot="2"></i><i data-dot="3"></i><i data-dot="4"></i>
   </div>

   <div class="qstep on" data-step="1">
    <p class="qnum">Question 1 of 4</p>
    <h2>What do you need?</h2>
    <div class="qopts">{s1}</div>
   </div>

   <div class="qstep" data-step="2">
    <p class="qnum">Question 2 of 4</p>
    <h2>What kind of property?</h2>
    <div class="qopts">{s2}</div>
    <button type="button" class="qback" data-back="1">&larr; Back</button>
   </div>

   <div class="qstep" data-step="3">
    <p class="qnum">Question 3 of 4</p>
    <h2>How soon?</h2>
    <div class="qopts">{s3}</div>
    <button type="button" class="qback" data-back="2">&larr; Back</button>
   </div>

   <div class="qstep" data-step="4">
    <p class="qnum">Last step</p>
    <h2>Where do we send the price?</h2>
    <div class="field"><label for="l-name">Name <span class="req">*</span></label>
     <input id="l-name" type="text" autocomplete="name"></div>
    <div class="field"><label for="l-phone">Phone <span class="req">*</span></label>
     <input id="l-phone" type="tel" autocomplete="tel"></div>
    <div class="field"><label for="l-email">Email <span class="req">*</span></label>
     <input id="l-email" type="email" autocomplete="email"></div>
    <div class="field"><label for="l-addr">Property address or city <span class="req">*</span></label>
     <input id="l-addr" type="text" autocomplete="street-address"></div>
    <input class="hp" type="text" id="l-gotcha" tabindex="-1" autocomplete="off" aria-hidden="true">
    <p class="qerr" id="qerr" role="alert">Please add your name, a valid phone number, an email and the property location.</p>
    <button type="button" class="btn btn-solid btn-lg btn-full" id="qsend">Get my flat price {ic_a}</button>
    <button type="button" class="qback" data-back="3">&larr; Back</button>
    <p class="form-note">No obligation. We do not share your details, and we do not sell the
     repairs we recommend.</p>
   </div>

   <div class="qdone" id="qdone">
    <div class="qtick">{ck_big}</div>
    <h2>Got it &mdash; that reached us</h2>
    <p>We reply the same business day with a flat price. If it is urgent, call
     <a href="tel:{tel}">{ph}</a> and we will move you up the schedule.</p>
    <a class="btn btn-line" href="/index.html">Browse the site</a>
   </div>
  </div>
 </div>

 <div class="start-foot">
  <div class="wrap start-foot-in">
   <div><b>Voluntary</b><span>CASp protects you from a claim you can see coming</span></div>
   <div><b>Mandatory</b><span>SB 721 &amp; SB 326 deadlines have already passed</span></div>
   <div><b>Statewide</b><span>All 58 California counties, one report format</span></div>
  </div>
 </div>
</div>

<script>
(function () {{
  var t0 = Date.now(), answers = {{}};
  function utm(k) {{ return new URLSearchParams(location.search).get(k) || ''; }}

  function show(n) {{
    document.querySelectorAll('.qstep').forEach(function (s) {{
      s.classList.toggle('on', Number(s.getAttribute('data-step')) === n);
    }});
    document.querySelectorAll('.qbar i').forEach(function (d) {{
      d.classList.toggle('on', Number(d.getAttribute('data-dot')) <= n);
    }});
    if (window.innerWidth < 900) document.getElementById('quiz').scrollIntoView({{ behavior: 'smooth', block: 'start' }});
  }}

  document.querySelectorAll('.qopt').forEach(function (b) {{
    b.addEventListener('click', function () {{
      answers[b.getAttribute('data-q')] = b.getAttribute('data-a');
      var step = Number(b.closest('.qstep').getAttribute('data-step'));
      show(step + 1);
      if (window.fbq) fbq('trackCustom', 'QuizStep', {{ step: step }});
    }});
  }});
  document.querySelectorAll('.qback').forEach(function (b) {{
    b.addEventListener('click', function () {{ show(Number(b.getAttribute('data-back'))); }});
  }});

  document.getElementById('qsend').addEventListener('click', function () {{
    var name = document.getElementById('l-name').value.trim(),
        phone = document.getElementById('l-phone').value.trim(),
        email = document.getElementById('l-email').value.trim(),
        addr = document.getElementById('l-addr').value.trim(),
        err = document.getElementById('qerr');

    if (!name || phone.replace(/\\D/g, '').length < 7 || !/^\\S+@\\S+\\.\\S+$/.test(email) || !addr) {{
      err.classList.add('on');
      return;
    }}
    err.classList.remove('on');

    var payload = {{
      name: name, phone: phone, email: email, _replyto: email,
      property_address: addr,
      service_needed: answers.service_needed || '',
      property_type: answers.property_type || '',
      timeline: answers.timeline || '',
      fill_seconds: Math.round((Date.now() - t0) / 1000),
      traffic_source: utm('utm_source') || document.referrer || 'direct',
      utm_campaign: utm('utm_campaign'),
      utm_content: utm('utm_content'),
      landing_page: '/start.html',
      _gotcha: document.getElementById('l-gotcha').value,
      _subject: 'New quote request — Inspector Group California ad funnel (start.html)'
    }};

    fetch('{form}', {{
      method: 'POST',
      headers: {{ 'Content-Type': 'application/json', Accept: 'application/json' }},
      body: JSON.stringify(payload)
    }}).catch(function () {{}});

    if (window.fbq) fbq('track', 'Lead', {{
      content_name: 'inspection_quiz',
      content_category: answers.service_needed || '',
      status: answers.timeline || ''
    }});

    document.querySelectorAll('.qstep').forEach(function (s) {{ s.classList.remove('on'); }});
    document.querySelector('.qbar').style.display = 'none';
    document.getElementById('qdone').classList.add('on');
    if (window.innerWidth < 900) document.getElementById('quiz').scrollIntoView({{ behavior: 'smooth', block: 'center' }});
  }});
}})();
</script>
""".format(
        bg=img("plaza-ramp", "", loading="eager"),
        tel=TEL, ph=PH, form=FORM_ACTION,
        ic_p=svg("phone"), ic_a=svg("arrow"), ic_g=svg("geo"), ck=svg("check"),
        ck_big='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" '
               'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20 6L9 17l-5-5"/></svg>',
        s1=opts(STEP1, "service_needed"), s2=opts(STEP2, "property_type"),
        s3=opts(STEP3, "timeline"),
    )

    html = head(
        "Get a flat price on your California inspection | Inspector Group California",
        "Three questions and we come back with a flat price for a CASp accessibility or "
        "SB 721 / SB 326 balcony inspection anywhere in California.",
        "/start.html",
        extra_css='<link rel="stylesheet" href="/assets/css/start.css">',
        body_class="start-page")

    # the funnel deliberately drops the site nav — strip it back out,
    # but keep the demo bar so the disclaimer travels with paid traffic too
    html = html.split('<a class="skip"')[0] + \
        '<a class="skip" href="#main">Skip to content</a>\n' + demo_bar() + '\n<main id="main">\n'

    write("start.html", html + body + """
</main>
<footer class="start-legal">
 <div class="wrap">
  <p><b>Not legal advice.</b> Inspector Group California performs inspections and writes
   reports. We are not a law firm and nothing here creates an attorney&ndash;client
   relationship. Retain California counsel for advice on your own situation.</p>
  <p>&copy; 2026 Inspector Group California &middot;
   <a href="/index.html">Main site</a> &middot;
   <a href="tel:%s">%s</a> &middot;
   Site by <a href="https://60minutesites.com" rel="noopener">60 Minute Sites</a></p>
 </div>
</footer>
</body>
</html>
""" % (TEL, PH))
