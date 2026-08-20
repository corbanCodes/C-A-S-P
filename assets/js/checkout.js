/* /checkout.html — example checkout.

   Demonstration only: the method toggle is real UI, the billing contact posts
   to the 60MS checkout Formspree endpoint, and the "continue to secure
   payment" step deliberately stops at a success pane. No card or bank field
   exists on this page by design — capture belongs on the processor's hosted
   checkout, which keeps the site out of PCI scope and leaves nothing here to
   clone into a phishing form. */
(function () {
  'use strict';
  var CFG = window.CIG_CHECKOUT || {};

  /* method segmented control */
  var seg = document.querySelectorAll('.seg [data-method]');
  seg.forEach(function (btn) {
    btn.addEventListener('click', function () {
      seg.forEach(function (b) { b.setAttribute('aria-pressed', b === btn ? 'true' : 'false'); });
      var want = btn.getAttribute('data-method');
      document.querySelectorAll('.co-method').forEach(function (pane) {
        pane.classList.toggle('on', pane.getAttribute('data-pane') === want);
      });
    });
  });

  /* billing contact -> demo inbox, then show the hand-off pane */
  var form = document.getElementById('co-form'),
      ok = document.getElementById('co-ok'),
      err = document.getElementById('co-err');
  if (!form) return;

  form.addEventListener('submit', function (e) {
    e.preventDefault();
    var name = document.getElementById('co-name').value.trim(),
        email = document.getElementById('co-email').value.trim();
    if (!name || !/^\S+@\S+\.\S+$/.test(email)) {
      err.classList.add('on');
      return;
    }
    err.classList.remove('on');

    var method = 'card';
    seg.forEach(function (b) {
      if (b.getAttribute('aria-pressed') === 'true') method = b.getAttribute('data-method');
    });

    if (CFG.form) {
      fetch(CFG.form, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json', Accept: 'application/json' },
        body: JSON.stringify({
          name: name,
          email: email,
          _replyto: email,
          company: document.getElementById('co-company').value.trim(),
          phone: document.getElementById('co-phone').value.trim(),
          billing_address: document.getElementById('co-addr').value.trim(),
          payment_method: method,
          order: 'IGC-2026-0418 — CASp inspection deposit',
          amount: '$230.00',
          landing_page: '/checkout.html',
          _subject: 'CHECKOUT (demo) — Inspector Group California deposit'
        })
      }).catch(function () {});
    }

    form.hidden = true;
    ok.hidden = false;
    ok.scrollIntoView({ behavior: 'smooth', block: 'center' });
  });
}());
