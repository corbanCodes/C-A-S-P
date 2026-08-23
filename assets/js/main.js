/* Inspector Group California — site behaviour.
   No dependencies. Everything degrades to working HTML if this never loads. */
(function () {
  'use strict';

  /* ---------------------------------------------------------- desktop menu */
  document.querySelectorAll('.has-menu').forEach(function (wrap) {
    var btn = wrap.querySelector('.nav-top');
    if (!btn) return;

    function open(state) {
      wrap.setAttribute('data-open', state ? '1' : '0');
      btn.setAttribute('aria-expanded', state ? 'true' : 'false');
    }
    btn.addEventListener('click', function (e) {
      e.stopPropagation();
      open(wrap.getAttribute('data-open') !== '1');
    });
    wrap.addEventListener('mouseenter', function () { open(true); });
    wrap.addEventListener('mouseleave', function () { open(false); });
    wrap.addEventListener('focusout', function (e) {
      if (!wrap.contains(e.relatedTarget)) open(false);
    });
    document.addEventListener('click', function (e) {
      if (!wrap.contains(e.target)) open(false);
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape') { open(false); btn.focus(); }
    });
  });

  /* -------------------------------------------------------------- burger */
  var burger = document.getElementById('burger'),
      mobile = document.getElementById('mobile');
  if (burger && mobile) {
    burger.addEventListener('click', function () {
      var open = mobile.classList.toggle('open');
      burger.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
  }

  /* ----------------------------------------------------------------- faq */
  document.querySelectorAll('.faq-q').forEach(function (btn) {
    btn.addEventListener('click', function () {
      var item = btn.closest('.faq-item'),
          open = item.getAttribute('data-open') === '1';
      item.setAttribute('data-open', open ? '0' : '1');
      btn.setAttribute('aria-expanded', open ? 'false' : 'true');
    });
  });

  /* --------------------------------------------------------- faq filters */
  var pills = document.querySelectorAll('.pill[data-filter]');
  if (pills.length) {
    pills.forEach(function (pill) {
      pill.addEventListener('click', function () {
        var want = pill.getAttribute('data-filter');
        pills.forEach(function (p) {
          p.setAttribute('aria-pressed', p === pill ? 'true' : 'false');
        });
        document.querySelectorAll('.faq-item').forEach(function (item) {
          var show = want === 'all' || item.getAttribute('data-cat') === want;
          item.style.display = show ? '' : 'none';
        });
      });
    });
  }

  /* ------------------------------------------------- form context fields */
  var t0 = Date.now();
  function param(k) {
    return new URLSearchParams(window.location.search).get(k) || '';
  }
  document.querySelectorAll('form.quote-form').forEach(function (form) {
    function set(name, value) {
      var el = form.querySelector('[name="' + name + '"]');
      if (el) el.value = value;
    }
    set('traffic_source', param('utm_source') || document.referrer || 'direct');
    set('utm_campaign', param('utm_campaign'));
    set('utm_content', param('utm_content'));
    set('landing_page', window.location.pathname);
    // HQ redirects here after a non-JSON post. Absolute, and built from the
    // current origin so it works on the preview domain and the live one alike.
    set('_next', window.location.origin + '/thank-you.html');

    form.addEventListener('submit', function () {
      set('fill_seconds', Math.round((Date.now() - t0) / 1000));
    });
  });
}());

/* ------------------------------------------------------- Calendly popups */
/* Any [data-calendly] element opens the 60MS Calendly in a popup; assets
   load on first click, and the plain href still works without JS. */
(function () {
  'use strict';
  var loaded = false, loading = false, queue = [];

  function openPopup(url) {
    if (window.Calendly) {
      window.Calendly.initPopupWidget({ url: url });
      return;
    }
    queue.push(url);
    if (loading) return;
    loading = true;
    var css = document.createElement('link');
    css.rel = 'stylesheet';
    css.href = 'https://assets.calendly.com/assets/external/widget.css';
    document.head.appendChild(css);
    var js = document.createElement('script');
    js.src = 'https://assets.calendly.com/assets/external/widget.js';
    js.onload = function () {
      loaded = true;
      queue.splice(0).forEach(function (u) {
        window.Calendly.initPopupWidget({ url: u });
      });
    };
    js.onerror = function () { loading = false; queue.length = 0; };
    document.head.appendChild(js);
  }

  document.addEventListener('click', function (e) {
    var a = e.target.closest && e.target.closest('[data-calendly]');
    if (!a) return;
    e.preventDefault();
    openPopup(a.getAttribute('href'));
  });
}());

/* ------------------------------------------------------- photo previews */
/* Any .upl file input gets thumbnail previews in its sibling .upl-list. */
(function () {
  'use strict';
  var MAX = 8;
  document.querySelectorAll('.upl input[type="file"]').forEach(function (input) {
    input.addEventListener('change', function () {
      var wrap = input.closest('.field') || input.closest('form') || document;
      var list = wrap.querySelector('.upl-list');
      if (!list) return;
      list.innerHTML = '';
      var files = Array.prototype.slice.call(input.files || []);
      files.slice(0, MAX).forEach(function (f) {
        if (!/^image\//.test(f.type)) return;
        var img = document.createElement('img');
        img.alt = '';
        img.src = URL.createObjectURL(f);
        img.onload = function () { URL.revokeObjectURL(img.src); };
        list.appendChild(img);
      });
      if (files.length > MAX) {
        var more = document.createElement('span');
        more.className = 'upl-more';
        more.textContent = '+' + (files.length - MAX);
        list.appendChild(more);
      }
      list.hidden = files.length === 0;
    });
  });
}());
