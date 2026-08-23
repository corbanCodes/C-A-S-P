/* Floating Call / Email contact dock.
   Self-contained: injects its own styles and markup, no backend, no dependencies.
   The real 60MS chat product drops in here at launch once a tenant slug exists. */
(function () {
  'use strict';
  if (document.body.classList.contains('start-page')) return;   // funnel stays clean

  var PHONE = '4086007165',
      PHONE_TXT = '408-600-7165',
      EMAIL = 'rob@inspectorgroupcalifornia.com',
      FORM = 'https://60minutesites.com/form/general-contact-form-a935';

  var css = [
    '.cw{position:fixed;left:20px;bottom:20px;z-index:120;font-family:Inter,sans-serif}',
    '.cw-pill{display:flex;align-items:center;gap:.5rem;background:#0B1B2B;color:#fff;',
    'border:0;border-radius:100px;padding:.72rem 1.15rem;cursor:pointer;font-family:Archivo,sans-serif;',
    'font-weight:700;font-size:.9rem;box-shadow:0 8px 24px rgba(11,27,43,.28)}',
    '.cw-pill:hover{background:#12324F}',
    '.cw-pill svg{width:18px;height:18px}',
    '.cw-panel{display:none;width:310px;max-width:calc(100vw - 40px);background:#fff;',
    'border:1px solid #DCE3EC;border-radius:18px;box-shadow:0 20px 50px rgba(11,27,43,.22);',
    'overflow:hidden;margin-bottom:.6rem}',
    '.cw.open .cw-panel{display:block}',
    '.cw-head{background:#0B1B2B;color:#fff;padding:1rem 1.1rem}',
    '.cw-head b{display:block;font-family:Archivo,sans-serif;font-size:.98rem}',
    '.cw-head span{font-size:.8rem;color:#9FB2C4}',
    '.cw-body{padding:.9rem}',
    '.cw-opt{display:flex;align-items:center;gap:.7rem;width:100%;background:#F6F8FB;border:1px solid #DCE3EC;',
    'border-radius:12px;padding:.75rem .85rem;margin-bottom:.5rem;cursor:pointer;text-align:left;',
    'text-decoration:none;color:#0B1B2B;font-size:.9rem;font-weight:600}',
    '.cw-opt:hover{background:#EAF2FB;border-color:#1263B8}',
    '.cw-opt svg{width:19px;height:19px;color:#1263B8;flex:none}',
    '.cw-opt small{display:block;font-weight:400;color:#64748B;font-size:.76rem}',
    '.cw-form{display:none;padding:.9rem}',
    '.cw-form.on{display:block}.cw-body.off{display:none}',
    '.cw-form input,.cw-form textarea{width:100%;font-family:inherit;font-size:.9rem;padding:.55rem .7rem;',
    'border:1.5px solid #DCE3EC;border-radius:9px;margin-bottom:.5rem;box-sizing:border-box}',
    '.cw-form textarea{min-height:74px;resize:vertical}',
    '.cw-form button{width:100%;background:#1263B8;color:#fff;border:0;border-radius:9px;padding:.65rem;',
    'font-family:Archivo,sans-serif;font-weight:700;font-size:.9rem;cursor:pointer}',
    '.cw-back{background:none;border:0;color:#64748B;font-size:.8rem;cursor:pointer;padding:.3rem 0}',
    '.cw-ok{padding:1.4rem 1.1rem;text-align:center;display:none}.cw-ok.on{display:block}',
    '.cw-ok b{display:block;font-family:Archivo,sans-serif;color:#0B1B2B;margin-bottom:.3rem}',
    '.cw-ok p{font-size:.86rem;color:#64748B;margin:0}',
    '@media(max-width:600px){.cw{left:12px;right:12px;bottom:12px}',
    '.cw-pill{width:100%;justify-content:center}.cw-panel{width:100%}}'
  ].join('');

  var ic = {
    chat: '<path d="M21 11.5a8.4 8.4 0 01-9 8.4 8.4 8.4 0 01-3.8-.9L3 20.5l1.5-4.6A8.4 8.4 0 013.6 12a8.4 8.4 0 018.4-8.4h.5A8.4 8.4 0 0121 11.5z"/>',
    phone: '<path d="M22 16.9v3a2 2 0 01-2.2 2 19.8 19.8 0 01-8.6-3.1 19.5 19.5 0 01-6-6A19.8 19.8 0 012.1 4.2 2 2 0 014.1 2h3a2 2 0 012 1.7c.1 1 .4 1.9.7 2.8a2 2 0 01-.5 2.1L8.1 9.9a16 16 0 006 6l1.3-1.3a2 2 0 012.1-.4c.9.3 1.8.6 2.8.7a2 2 0 011.7 2z"/>',
    mail: '<path d="M4 4h16v16H4z"/><path d="M4 6l8 6 8-6"/>',
    close: '<path d="M18 6L6 18M6 6l12 12"/>'
  };

  function svg(k) {
    return '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" ' +
      'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">' + ic[k] + '</svg>';
  }

  var style = document.createElement('style');
  style.textContent = css;
  document.head.appendChild(style);

  var el = document.createElement('div');
  el.className = 'cw';
  el.innerHTML =
    '<div class="cw-panel" role="dialog" aria-label="Contact Inspector Group California">' +
      '<div class="cw-head"><b>Talk to an inspector</b><span>Same business day reply</span></div>' +
      '<div class="cw-body" id="cw-body">' +
        '<a class="cw-opt" href="tel:' + PHONE + '">' + svg('phone') +
          '<span>Call ' + PHONE_TXT + '<small>Fastest &mdash; ask for Robert</small></span></a>' +
        '<a class="cw-opt" href="sms:' + PHONE + '">' + svg('chat') +
          '<span>Send a text<small>Good for photos of the property</small></span></a>' +
        '<button class="cw-opt" type="button" id="cw-open-form">' + svg('mail') +
          '<span>Email us<small>Send the details and get a price</small></span></button>' +
      '</div>' +
      '<form class="cw-form" id="cw-form">' +
        '<input type="text" name="name" placeholder="Your name" autocomplete="name" required>' +
        '<input type="tel" name="phone" placeholder="Phone" autocomplete="tel" required>' +
        '<input type="email" name="email" placeholder="Email" autocomplete="email" required>' +
        '<textarea name="message" placeholder="Property address and what you need"></textarea>' +
        '<input type="hidden" name="landing_page" value="">' +
        '<button type="submit">Send</button>' +
        '<button class="cw-back" type="button" id="cw-back">&larr; Back</button>' +
      '</form>' +
      '<div class="cw-ok" id="cw-ok"><b>Thanks &mdash; that reached us</b>' +
        '<p>We reply the same business day.</p></div>' +
    '</div>' +
    '<button class="cw-pill" id="cw-toggle" aria-expanded="false">' + svg('chat') +
      '<span>Talk to an inspector</span></button>';
  document.body.appendChild(el);

  var toggle = el.querySelector('#cw-toggle'),
      body = el.querySelector('#cw-body'),
      form = el.querySelector('#cw-form'),
      ok = el.querySelector('#cw-ok');

  toggle.addEventListener('click', function () {
    var open = el.classList.toggle('open');
    toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
    toggle.innerHTML = (open ? svg('close') : svg('chat')) +
      '<span>' + (open ? 'Close' : 'Talk to an inspector') + '</span>';
  });

  el.querySelector('#cw-open-form').addEventListener('click', function () {
    body.classList.add('off');
    form.classList.add('on');
  });
  el.querySelector('#cw-back').addEventListener('click', function () {
    body.classList.remove('off');
    form.classList.remove('on');
  });

  form.addEventListener('submit', function (e) {
    e.preventDefault();
    fetch(FORM, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json', Accept: 'application/json' },
      body: JSON.stringify({
        name: form.name.value.trim(),
        phone: form.phone.value.trim(),
        email: form.email.value.trim(),
        message: form.message.value.trim(),
        source: 'IGC site widget',
        landing_page: window.location.pathname
      })
    }).catch(function () {});
    form.classList.remove('on');
    ok.classList.add('on');
  });

  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape' && el.classList.contains('open')) toggle.click();
  });
}());
