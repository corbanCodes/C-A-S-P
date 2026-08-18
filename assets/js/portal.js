/* /portal.html — demo client portal.

   The pay button here demonstrates the gate: settling the balance is what
   unlocks the report. On the live site the button opens the payment
   provider's hosted checkout and the unlock happens server-side on the
   webhook — never in the browser, because anything the browser can unlock a
   visitor can unlock too. See DEMO-NOTES.md. */
(function () {
  'use strict';

  var pay = document.getElementById('ppay'),
      lock = document.getElementById('plock'),
      files = document.getElementById('pfiles'),
      report = document.getElementById('preport');
  if (!pay) return;

  pay.addEventListener('click', function () {
    lock.classList.add('unlocked');
    report.classList.add('is-open');
    files.hidden = false;

    lock.querySelector('.plock-ic').innerHTML =
      '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" ' +
      'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">' +
      '<path d="M20 6L9 17l-5-5"/></svg>';
    document.getElementById('plock-sub').textContent =
      'Released 12 May 2026 · balance settled in full';
    pay.outerHTML = '<span class="pstat pstat-ok">Paid in full</span>';

    var track = document.querySelector('.ptrack');
    if (track) {
      var items = track.querySelectorAll('li');
      items.forEach(function (li) { li.classList.remove('now'); li.classList.add('done'); });
    }
    var badge = document.querySelector('.pstat-wait');
    if (badge) {
      badge.textContent = 'Complete';
      badge.className = 'pstat pstat-ok';
    }
  });

  /* Demo files are not real downloads — say so rather than 404 into a dead link. */
  document.querySelectorAll('[data-demo]').forEach(function (a) {
    a.addEventListener('click', function (e) {
      e.preventDefault();
      var note = document.getElementById('pdemo-note');
      if (note) { note.hidden = false; note.scrollIntoView({ block: 'center' }); }
    });
  });
}());
