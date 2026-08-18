/* Pricing-page calculator. Reads window.CIG_RATES, which is generated straight
   from the same rate card the table above it renders — so the two can never
   drift apart. */
(function () {
  'use strict';
  var R = window.CIG_RATES;
  if (!R) return;

  var line = document.getElementById('c-line'),
      occ = document.getElementById('c-occ'),
      sqft = document.getElementById('c-sqft'),
      units = document.getElementById('c-units'),
      occF = document.getElementById('c-occ-field'),
      sqftF = document.getElementById('c-sqft-field'),
      unitF = document.getElementById('c-units-field'),
      outPrice = document.getElementById('calc-price'),
      outSub = document.getElementById('calc-sub'),
      outDep = document.getElementById('calc-dep'),
      go = document.getElementById('calc-go');
  if (!line || !outPrice) return;

  function money(n) {
    return '$' + n.toLocaleString('en-US');
  }
  function toNumber(price) {
    var n = parseInt(String(price).replace(/[^0-9]/g, ''), 10);
    return isNaN(n) ? null : n;
  }

  function update() {
    var isEEE = line.value === 'eee', price, label;

    occF.hidden = isEEE;
    sqftF.hidden = isEEE;
    unitF.hidden = !isEEE;

    if (isEEE) {
      price = R.eee[units.value];
      label = 'SB 721 / SB 326 balcony inspection, ' + R.eeeNames[units.value].toLowerCase();
    } else {
      price = R.casp[occ.value][sqft.value];
      label = R.caspNames[occ.value] + ', ' + R.bands[sqft.value].toLowerCase() + ' sq ft';
    }

    var n = toNumber(price);
    if (n === null) {
      outPrice.textContent = 'Custom quote';
      outPrice.classList.add('is-quote');
      outSub.textContent = label + ' — priced as a package';
      outDep.textContent = '—';
      go.textContent = 'Request a quote';
      go.setAttribute('href', '/contact.html');
    } else {
      outPrice.textContent = money(n);
      outPrice.classList.remove('is-quote');
      outSub.textContent = label;
      outDep.textContent = money(Math.round(n * 0.2));
      go.textContent = 'Book this inspection';
      go.setAttribute('href', '/book.html');
    }
  }

  [line, occ, sqft, units].forEach(function (el) {
    if (el) el.addEventListener('change', update);
  });
  update();
}());
