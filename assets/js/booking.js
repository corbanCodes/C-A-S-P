/* /book.html — the four-step booking wizard.

   Steps 1–3 are fully working front end: the price computes off the published
   rate card and the details POST to Formspree with the same payload shape as
   every other 60MS form, so the booking lands in the CRM.

   Step 4 is deliberately a hand-off, not a simulation. It never renders a card
   field. Real payment belongs on the processor's hosted page and real signature
   on the e-sign vendor's — see DEMO-NOTES.md for the wiring. */
(function () {
  'use strict';
  var R = window.CIG_RATES;
  if (!R) return;

  var t0 = Date.now(), quoted = null, quoteLabel = '';

  var line = document.getElementById('w-line'),
      occ = document.getElementById('w-occ'),
      sqft = document.getElementById('w-sqft'),
      units = document.getElementById('w-units'),
      occF = document.getElementById('w-occ-field'),
      sqftF = document.getElementById('w-sqft-field'),
      unitF = document.getElementById('w-units-field'),
      priceEl = document.getElementById('w-price'),
      depEl = document.getElementById('w-dep'),
      noteEl = document.getElementById('w-price-note');

  function money(n) { return '$' + n.toLocaleString('en-US'); }
  function toNumber(p) {
    var n = parseInt(String(p).replace(/[^0-9]/g, ''), 10);
    return isNaN(n) ? null : n;
  }
  function param(k) { return new URLSearchParams(location.search).get(k) || ''; }

  /* --------------------------------------------------------------- price */
  function updatePrice() {
    var v = line.value, price, label;

    occF.hidden = (v !== 'casp');
    sqftF.hidden = (v !== 'casp');
    unitF.hidden = (v !== 'eee');

    if (v === 'casp') {
      price = R.casp[occ.value][sqft.value];
      label = R.caspNames[occ.value] + ', ' + R.bands[sqft.value].toLowerCase() + ' sq ft';
    } else if (v === 'eee') {
      price = R.eee[units.value];
      label = 'Balcony inspection, ' + R.eeeNames[units.value].toLowerCase();
    } else {
      price = 'Quote';
      label = (v === 'both')
        ? 'Mixed-use property — both mandates'
        : 'Multiple buildings or a portfolio';
    }

    quoteLabel = label;
    quoted = toNumber(price);

    if (quoted === null) {
      priceEl.textContent = 'Custom quote';
      depEl.textContent = '—';
      noteEl.textContent = 'We price these as a package. Send the details and we come back ' +
        'the same business day with a fixed number.';
    } else {
      priceEl.textContent = money(quoted);
      depEl.textContent = money(Math.round(quoted * 0.2));
      noteEl.textContent = 'Balance due on completion. The report is released when it clears.';
    }
  }

  [line, occ, sqft, units].forEach(function (el) {
    if (el) el.addEventListener('change', updatePrice);
  });
  updatePrice();

  /* ---------------------------------------------------------------- steps */
  function show(n) {
    document.querySelectorAll('.wstep').forEach(function (s) {
      s.classList.toggle('on', Number(s.getAttribute('data-step')) === n);
    });
    document.querySelectorAll('.wiz-rail i').forEach(function (d) {
      d.classList.toggle('on', Number(d.getAttribute('data-w')) <= n);
    });
    var wiz = document.getElementById('wiz');
    if (wiz) wiz.scrollIntoView({ behavior: 'smooth', block: 'start' });
  }

  document.querySelectorAll('.qback').forEach(function (b) {
    b.addEventListener('click', function () { show(Number(b.getAttribute('data-back'))); });
  });

  function validDetails() {
    var name = document.getElementById('w-name').value.trim(),
        phone = document.getElementById('w-phone').value.trim(),
        email = document.getElementById('w-email').value.trim(),
        addr = document.getElementById('w-addr').value.trim();
    return name && phone.replace(/\D/g, '').length >= 7 &&
      /^\S+@\S+\.\S+$/.test(email) && addr;
  }

  function submitBooking() {
    var email = document.getElementById('w-email').value.trim();
    var payload = {
      name: document.getElementById('w-name').value.trim(),
      company: document.getElementById('w-company').value.trim(),
      email: email,
      _replyto: email,
      phone: document.getElementById('w-phone').value.trim(),
      property_address: document.getElementById('w-addr').value.trim(),
      message: document.getElementById('w-notes').value.trim(),
      service_needed: line.options[line.selectedIndex].text,
      property_type: quoteLabel,
      quoted_fee: quoted === null ? 'Custom quote' : money(quoted),
      deposit_due: quoted === null ? 'TBC' : money(Math.round(quoted * 0.2)),
      esign_consent: document.getElementById('w-esign').checked ? 'yes' : 'no',
      hazard_ack: document.getElementById('w-ack').checked ? 'yes' : 'no',
      fill_seconds: Math.round((Date.now() - t0) / 1000),
      traffic_source: param('utm_source') || document.referrer || 'direct',
      utm_campaign: param('utm_campaign'),
      utm_content: param('utm_content'),
      landing_page: '/book.html',
      _subject: 'BOOKING — California Inspector Group (agreement requested)'
    };

    fetch(R.form, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json', Accept: 'application/json' },
      body: JSON.stringify(payload)
    }).catch(function () {});

    if (window.fbq) window.fbq('track', 'Schedule', {
      content_name: 'inspection_booking',
      value: quoted || 0,
      currency: 'USD'
    });

    var echo = document.getElementById('w-echo');
    if (echo) echo.textContent = email;
    var dep2 = document.getElementById('w-dep2');
    if (dep2) dep2.textContent = quoted === null ? 'the' : money(Math.round(quoted * 0.2));
  }

  document.querySelectorAll('.wnext').forEach(function (btn) {
    btn.addEventListener('click', function () {
      var next = Number(btn.getAttribute('data-next'));

      if (next === 3) {
        var err = document.getElementById('w-err');
        if (!validDetails()) { err.classList.add('on'); return; }
        err.classList.remove('on');
      }

      if (next === 4) {
        var err2 = document.getElementById('w-err2');
        if (!document.getElementById('w-esign').checked ||
            !document.getElementById('w-ack').checked) {
          err2.classList.add('on');
          return;
        }
        err2.classList.remove('on');
        submitBooking();
      }

      show(next);
    });
  });
}());
