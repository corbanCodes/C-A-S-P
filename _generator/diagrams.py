# -*- coding: utf-8 -*-
"""Authored SVG diagrams.

These carry most of the explanatory weight on the site. Each one is inline SVG
so it inherits the CSS custom properties in main.css, scales without a second
request, and stays sharp on any display. Every diagram is role="img" with a
<title> and <desc> so it is not a black hole for a screen reader — which, on a
site about accessibility, is rather the point.
"""


def _wrap(view, title, desc, body, cls="dg"):
    return ('<svg class="%s" viewBox="%s" role="img" aria-labelledby="%s %s" '
            'xmlns="http://www.w3.org/2000/svg">'
            '<title id="%s">%s</title><desc id="%s">%s</desc>%s</svg>'
            % (cls, view, title[0], desc[0], title[0], title[1], desc[0], desc[1], body))


# ------------------------------------------------------------ lawsuit timeline

def lawsuit_timeline():
    """Two tracks from the day a complaint is served: with and without a report.

    Laid out on a strict row grid — lane A (rows y=84..200), lane B
    (y=260..324), outcome row (y=356..420) — so nothing can overlap.
    """
    body = """
<defs>
 <marker id="ar" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto">
  <path d="M0 0L10 5L0 10z" fill="var(--red)" fill-opacity=".75"/>
 </marker>
 <marker id="ag" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto">
  <path d="M0 0L10 5L0 10z" fill="var(--green)"/>
 </marker>
</defs>

<!-- day 0 rule -->
<line x1="210" y1="40" x2="210" y2="420" stroke="var(--ink)" stroke-width="2" stroke-dasharray="5 4" opacity=".35"/>
<text x="210" y="26" text-anchor="middle" class="dg-cap dg-strong">Day 0 &mdash; complaint served</text>

<!-- ============ lane A : no report ============ -->
<text x="24" y="72" class="dg-lane">Without a CASp report</text>
<rect x="24" y="84" width="168" height="64" rx="12" fill="var(--paper)" stroke="var(--line)"/>
<text x="42" y="110" class="dg-cap">You are an</text>
<text x="42" y="130" class="dg-cap dg-strong">ordinary defendant</text>

<rect x="210" y="84" width="666" height="64" rx="12" fill="var(--red-wash)" stroke="var(--red)" stroke-opacity=".3"/>
<text x="234" y="110" class="dg-cap dg-strong" fill="var(--red)">The case simply proceeds</text>
<text x="234" y="132" class="dg-cap">$4,000 minimum per offence under the Unruh Act, plus the plaintiff&#8217;s attorney fees.</text>

<line x1="234" y1="176" x2="846" y2="176" stroke="var(--red)" stroke-width="2" opacity=".6" marker-end="url(#ar)"/>
<text x="234" y="198" class="dg-cap dg-mute">day 1</text>
<text x="846" y="198" text-anchor="end" class="dg-cap dg-mute">fees compound the longer it runs</text>

<!-- ============ lane B : report on file ============ -->
<text x="24" y="248" class="dg-lane">With a CASp report on file</text>
<rect x="24" y="260" width="168" height="64" rx="12" fill="var(--blue-wash)" stroke="var(--blue)" stroke-opacity=".35"/>
<text x="42" y="286" class="dg-cap">You are a</text>
<text x="42" y="306" class="dg-cap dg-strong" fill="var(--blue-ink)">qualified defendant</text>

<rect x="210" y="260" width="330" height="64" rx="12" fill="var(--blue)" fill-opacity=".13" stroke="var(--blue)" stroke-opacity=".6"/>
<text x="234" y="286" class="dg-cap dg-strong" fill="var(--blue-ink)">90-day stay of proceedings</text>
<text x="234" y="308" class="dg-cap">The case pauses. Civil Code &#167;55.54.</text>

<circle cx="540" cy="292" r="7" fill="var(--gold)"/>
<line x1="549" y1="292" x2="566" y2="292" stroke="var(--gold)" stroke-width="1.5" opacity=".7"/>
<text x="574" y="286" class="dg-cap dg-strong">Early evaluation conference</text>
<text x="574" y="306" class="dg-cap">A judge and both parties, before fees compound.</text>

<!-- outcome row -->
<line x1="375" y1="326" x2="375" y2="352" stroke="var(--green)" stroke-width="2" marker-end="url(#ag)"/>
<rect x="210" y="356" width="666" height="64" rx="12" fill="var(--green-wash)" stroke="var(--green)" stroke-opacity=".35"/>
<text x="234" y="382" class="dg-cap dg-strong" fill="var(--green-ink)">Minimum statutory damages may fall to $1,000 per offence</text>
<text x="234" y="404" class="dg-cap">where the site was CASp-inspected and violations are corrected within 60 days of service. &#167;55.56.</text>
"""
    return _wrap("0 0 900 436",
                 ("lt-t", "What changes on the day you are served"),
                 ("lt-d", "A comparison of two tracks after a construction-related accessibility "
                          "complaint is served. Without a CASp report the case proceeds immediately "
                          "with minimum damages of $4,000 per offence plus plaintiff attorney fees. "
                          "With a CASp report on file the defendant may apply for a 90-day stay of "
                          "proceedings and an early evaluation conference under Civil Code section "
                          "55.54, and minimum statutory damages may fall to $1,000 per offence where "
                          "violations are corrected within 60 days under section 55.56."),
                 body)


# ------------------------------------------------------------- damages compare

def damages_chart():
    """$4,000 / $2,000 / $1,000 minimum statutory damages per offence."""
    # Left gutter is 330px: enough for the longest label pair without clipping.
    bars = [
        (4000, "$4,000", "The default", "No CASp report, no correction credit.", "var(--red)", 460),
        (2000, "$2,000", "Small business",
         "Corrected within 30 days of service.", "var(--gold)", 230),
        (1000, "$1,000", "CASp-inspected site",
         "Corrected within 60 days of service.", "var(--green)", 115),
    ]
    out = []
    y = 40
    for _, amt, label, sub, col, w in bars:
        out.append(f'<rect x="340" y="{y}" width="{w}" height="46" rx="6" fill="{col}" fill-opacity=".16" stroke="{col}" stroke-opacity=".5"/>')
        out.append(f'<rect x="340" y="{y}" width="5" height="46" rx="2.5" fill="{col}"/>')
        out.append(f'<text x="362" y="{y+29}" class="dg-num" fill="{col}">{amt}</text>')
        out.append(f'<text x="326" y="{y+20}" text-anchor="end" class="dg-cap dg-strong">{label}</text>')
        out.append(f'<text x="326" y="{y+38}" text-anchor="end" class="dg-cap dg-mute">{sub}</text>')
        y += 74
    out.append('<line x1="340" y1="26" x2="340" y2="256" stroke="var(--line)" stroke-width="1.5"/>')
    out.append('<text x="340" y="18" class="dg-cap dg-mute">minimum statutory damages, per offence</text>')
    return _wrap("0 0 830 272",
                 ("dc-t", "Minimum statutory damages per offence"),
                 ("dc-d", "Bar comparison of minimum statutory damages per offence: $4,000 by "
                          "default; $2,000 for a qualifying small business correcting within 30 "
                          "days of service; $1,000 for a CASp-inspected site or one permitted after "
                          "2008 that corrects within 60 days of service."),
                 "".join(out))


# --------------------------------------------------------------- path of travel

def path_of_travel():
    """Plan view of the route a CASp inspection actually follows."""
    body = """
<defs>
 <marker id="pt" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto">
  <path d="M0 0L10 5L0 10z" fill="var(--blue)"/>
 </marker>
</defs>

<!-- street -->
<rect x="0" y="330" width="820" height="46" fill="var(--ink)" fill-opacity=".06"/>
<line x1="0" y1="353" x2="820" y2="353" stroke="var(--ink)" stroke-width="2" stroke-dasharray="16 12" opacity=".3"/>
<text x="14" y="368" class="dg-cap dg-mute">public way</text>

<!-- parking -->
<rect x="30" y="200" width="230" height="118" rx="6" fill="var(--paper)" stroke="var(--line)"/>
<text x="34" y="192" class="dg-cap dg-strong">1 &middot; Parking</text>
<g stroke="var(--line)" stroke-width="1.5">
 <line x1="74" y1="200" x2="74" y2="318"/><line x1="118" y1="200" x2="118" y2="318"/>
 <line x1="214" y1="200" x2="214" y2="318"/>
</g>
<!-- accessible stall + aisle -->
<rect x="118" y="200" width="48" height="118" fill="var(--blue)" fill-opacity=".16"/>
<rect x="166" y="200" width="48" height="118" fill="var(--blue)" fill-opacity=".07"/>
<g stroke="var(--blue)" stroke-width="1.2" opacity=".65">
 <line x1="166" y1="200" x2="214" y2="318"/><line x1="214" y1="200" x2="166" y2="318"/>
</g>
<circle cx="142" cy="248" r="13" fill="none" stroke="var(--blue)" stroke-width="2"/>
<text x="142" y="253" text-anchor="middle" class="dg-isa" fill="var(--blue)">&#9855;</text>
<text x="190" y="336" text-anchor="middle" class="dg-cap dg-mute">access aisle</text>

<!-- route -->
<path d="M190 200 C190 168 250 160 300 160 L392 160" fill="none" stroke="var(--blue)"
      stroke-width="3.5" stroke-linecap="round" stroke-dasharray="9 7" marker-end="url(#pt)"/>
<text x="248" y="146" class="dg-cap dg-strong">2 &middot; Accessible route</text>
<text x="248" y="182" class="dg-cap dg-mute">slope, cross-slope, width, level changes</text>

<!-- building -->
<rect x="400" y="40" width="392" height="278" rx="10" fill="var(--paper)" stroke="var(--ink)" stroke-opacity=".35" stroke-width="2"/>
<text x="416" y="30" class="dg-cap dg-strong">The building</text>

<!-- entrance -->
<rect x="392" y="140" width="16" height="52" fill="var(--blue)" fill-opacity=".3" stroke="var(--blue)"/>
<path d="M408 192 a52 52 0 0 0 52 -52" fill="none" stroke="var(--blue)" stroke-width="1.4" stroke-dasharray="4 4" opacity=".8"/>
<text x="422" y="212" class="dg-cap dg-strong">3 &middot; Entrance</text>
<text x="422" y="230" class="dg-cap dg-mute">clear width, opening force, hardware</text>

<!-- interior route -->
<path d="M420 166 L560 166 L560 96" fill="none" stroke="var(--blue)" stroke-width="3.5"
      stroke-linecap="round" stroke-dasharray="9 7" marker-end="url(#pt)"/>
<path d="M560 166 L700 166 L700 240" fill="none" stroke="var(--blue)" stroke-width="3.5"
      stroke-linecap="round" stroke-dasharray="9 7" marker-end="url(#pt)"/>
<text x="470" y="120" class="dg-cap dg-strong">4 &middot; Circulation</text>

<!-- restroom -->
<rect x="500" y="56" width="120" height="44" rx="5" fill="var(--blue)" fill-opacity=".12" stroke="var(--blue)" stroke-opacity=".5"/>
<text x="560" y="76" text-anchor="middle" class="dg-cap dg-strong">5 &middot; Restrooms</text>
<text x="560" y="92" text-anchor="middle" class="dg-cap dg-mute">turning space, grab bars</text>

<!-- counter -->
<rect x="640" y="244" width="120" height="44" rx="5" fill="var(--blue)" fill-opacity=".12" stroke="var(--blue)" stroke-opacity=".5"/>
<text x="700" y="264" text-anchor="middle" class="dg-cap dg-strong">6 &middot; Counters</text>
<text x="700" y="280" text-anchor="middle" class="dg-cap dg-mute">height, reach range</text>
"""
    return _wrap("0 0 820 384",
                 ("pt-t", "The path of travel an inspection follows"),
                 ("pt-d", "A plan view of a commercial site showing the sequence an accessibility "
                          "inspection follows: parking including the accessible stall and access "
                          "aisle, the accessible route from parking to the building, the entrance, "
                          "interior circulation, restrooms, and service counters."),
                 body)


# ------------------------------------------------------------ balcony section

def eee_section():
    """Cross-section of a wood-framed balcony with the inspection points called out."""
    body = """
<!-- ground -->
<rect x="-80" y="392" width="1020" height="40" fill="var(--ink)" fill-opacity=".07"/>
<line x1="-80" y1="392" x2="940" y2="392" stroke="var(--ink)" stroke-width="2" opacity=".35"/>
<text x="-66" y="416" class="dg-cap dg-mute">ground level</text>

<!-- building wall -->
<rect x="150" y="40" width="112" height="352" fill="var(--ink)" fill-opacity=".1" stroke="var(--ink)" stroke-opacity=".35" stroke-width="2"/>
<g stroke="var(--ink)" stroke-opacity=".18" stroke-width="1">
 <line x1="150" y1="96" x2="262" y2="96"/><line x1="150" y1="152" x2="262" y2="152"/>
 <line x1="150" y1="208" x2="262" y2="208"/><line x1="150" y1="264" x2="262" y2="264"/>
 <line x1="150" y1="320" x2="262" y2="320"/>
</g>
<text x="206" y="34" text-anchor="middle" class="dg-cap dg-strong">building</text>

<!-- joists -->
<rect x="262" y="196" width="268" height="26" fill="var(--gold)" fill-opacity=".22" stroke="var(--gold)" stroke-opacity=".7"/>
<g stroke="var(--gold)" stroke-opacity=".45" stroke-width="1">
 <line x1="300" y1="196" x2="300" y2="222"/><line x1="340" y1="196" x2="340" y2="222"/>
 <line x1="380" y1="196" x2="380" y2="222"/><line x1="420" y1="196" x2="420" y2="222"/>
 <line x1="460" y1="196" x2="460" y2="222"/><line x1="500" y1="196" x2="500" y2="222"/>
</g>

<!-- ledger -->
<rect x="250" y="192" width="18" height="34" fill="var(--red)" fill-opacity=".28" stroke="var(--red)" stroke-opacity=".8"/>

<!-- walking surface + membrane -->
<rect x="262" y="182" width="268" height="8" fill="var(--blue)" fill-opacity=".45"/>
<rect x="262" y="174" width="268" height="8" fill="var(--ink)" fill-opacity=".22"/>

<!-- guardrail -->
<line x1="524" y1="174" x2="524" y2="86" stroke="var(--ink)" stroke-width="4" stroke-opacity=".55" stroke-linecap="round"/>
<line x1="266" y1="90" x2="528" y2="90" stroke="var(--ink)" stroke-width="5" stroke-opacity=".55" stroke-linecap="round"/>
<g stroke="var(--ink)" stroke-opacity=".3" stroke-width="2.5">
 <line x1="320" y1="96" x2="320" y2="174"/><line x1="368" y1="96" x2="368" y2="174"/>
 <line x1="416" y1="96" x2="416" y2="174"/><line x1="464" y1="96" x2="464" y2="174"/>
</g>

<!-- 6 ft dimension -->
<line x1="600" y1="186" x2="600" y2="392" stroke="var(--green)" stroke-width="2"/>
<line x1="590" y1="186" x2="610" y2="186" stroke="var(--green)" stroke-width="2"/>
<line x1="590" y1="392" x2="610" y2="392" stroke="var(--green)" stroke-width="2"/>
<rect x="614" y="272" width="150" height="44" rx="6" fill="var(--green-wash)" stroke="var(--green)" stroke-opacity=".5"/>
<text x="626" y="292" class="dg-cap dg-strong" fill="var(--green-ink)">More than 6 feet</text>
<text x="626" y="308" class="dg-cap">puts it in scope</text>

<!-- callouts -->
<g class="dg-call">
 <circle cx="259" cy="209" r="12" fill="var(--red)"/><text x="259" y="214" text-anchor="middle" class="dg-badge">1</text>
 <line x1="247" y1="209" x2="120" y2="209" stroke="var(--red)" stroke-width="1.5" opacity=".6"/>
 <text x="112" y="205" text-anchor="end" class="dg-cap dg-strong">Ledger &amp; flashing</text>
 <text x="112" y="221" text-anchor="end" class="dg-cap dg-mute">where most failures start</text>

 <circle cx="396" cy="209" r="12" fill="var(--gold)"/><text x="396" y="214" text-anchor="middle" class="dg-badge">2</text>
 <line x1="396" y1="221" x2="396" y2="300" stroke="var(--gold)" stroke-width="1.5" opacity=".6"/>
 <text x="396" y="318" text-anchor="middle" class="dg-cap dg-strong">Joists &amp; connections</text>
 <text x="396" y="334" text-anchor="middle" class="dg-cap dg-mute">decay, corrosion, fasteners</text>

 <circle cx="330" cy="178" r="12" fill="var(--blue)"/><text x="330" y="183" text-anchor="middle" class="dg-badge">3</text>
 <line x1="330" y1="166" x2="330" y2="126" stroke="var(--blue)" stroke-width="1.5" opacity=".6"/>
 <text x="322" y="120" text-anchor="end" class="dg-cap dg-strong">Waterproofing</text>
 <text x="322" y="136" text-anchor="end" class="dg-cap dg-mute">membrane &amp; surface</text>

 <circle cx="524" cy="90" r="12" fill="var(--ink)"/><text x="524" y="95" text-anchor="middle" class="dg-badge">4</text>
 <line x1="536" y1="90" x2="640" y2="90" stroke="var(--ink)" stroke-width="1.5" opacity=".5"/>
 <text x="648" y="86" class="dg-cap dg-strong">Guardrail</text>
 <text x="648" y="102" class="dg-cap dg-mute">height, infill, attachment</text>
</g>
"""
    return _wrap("-80 0 1020 432",
                 ("ee-t", "Anatomy of an exterior elevated element"),
                 ("ee-d", "A cross-section of a wood-framed balcony attached to a building wall. "
                          "Four inspection points are called out: the ledger and its flashing where "
                          "the balcony meets the wall, the joists and their connections, the "
                          "waterproofing membrane under the walking surface, and the guardrail. A "
                          "dimension line shows that a walking surface more than six feet above "
                          "ground level brings the element into scope."),
                 body)


# ----------------------------------------------------------------- which law

def which_law():
    """Decision tree: which statute applies to this building."""
    body = """
<defs>
 <marker id="wl" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto">
  <path d="M0 0L10 5L0 10z" fill="var(--ink)" fill-opacity=".5"/>
 </marker>
</defs>

<rect x="298" y="16" width="264" height="58" rx="10" fill="var(--paper)" stroke="var(--ink)" stroke-opacity=".35" stroke-width="2"/>
<text x="430" y="40" text-anchor="middle" class="dg-cap dg-strong">Three or more dwelling units,</text>
<text x="430" y="60" text-anchor="middle" class="dg-cap dg-strong">with elevated wood-framed elements?</text>

<path d="M430 74 v22 M220 96 h420 M220 96 v18" fill="none"
      stroke="var(--ink)" stroke-opacity=".45" stroke-width="2"/>
<path d="M640 96 v18" fill="none" stroke="var(--ink)" stroke-opacity=".45" stroke-width="2"/>
<path d="M220 132 v14" stroke="var(--ink)" stroke-opacity=".45" stroke-width="2" marker-end="url(#wl)"/>
<path d="M640 132 v14" stroke="var(--ink)" stroke-opacity=".45" stroke-width="2" marker-end="url(#wl)"/>

<!-- branch labels sit in a gap in the connector rather than on top of it -->
<rect x="132" y="116" width="176" height="20" fill="#fff" opacity=".92"/>
<rect x="546" y="116" width="196" height="20" fill="#fff" opacity=".92"/>
<text x="220" y="131" text-anchor="middle" class="dg-cap dg-mute">owner rents the units</text>
<text x="640" y="131" text-anchor="middle" class="dg-cap dg-mute">association maintains them</text>

<!-- apartments -->
<rect x="30" y="154" width="380" height="206" rx="12" fill="var(--gold-wash)" stroke="var(--gold)" stroke-opacity=".55" stroke-width="2"/>
<text x="54" y="188" class="dg-h" fill="var(--gold-ink)">SB 721</text>
<text x="54" y="210" class="dg-cap dg-strong">Apartment &amp; multifamily rentals</text>
<text x="54" y="234" class="dg-cap">Health &amp; Safety Code &#167;17973</text>
<line x1="54" y1="248" x2="386" y2="248" stroke="var(--gold)" stroke-opacity=".4"/>
<text x="54" y="270" class="dg-cap">First inspection due <tspan class="dg-strong">1 Jan 2026</tspan></text>
<text x="54" y="290" class="dg-cap dg-mute">(extended from 2025 by AB 2579)</text>
<text x="54" y="314" class="dg-cap">Then at least every <tspan class="dg-strong">6 years</tspan></text>
<text x="54" y="334" class="dg-cap dg-mute">Architect, engineer, A/B/C-5 contractor</text>
<text x="54" y="350" class="dg-cap dg-mute">or certified building inspector</text>

<!-- condos -->
<rect x="450" y="154" width="380" height="206" rx="12" fill="var(--blue-wash)" stroke="var(--blue)" stroke-opacity=".55" stroke-width="2"/>
<text x="474" y="188" class="dg-h" fill="var(--blue-ink)">SB 326</text>
<text x="474" y="210" class="dg-cap dg-strong">Condominiums &amp; HOAs</text>
<text x="474" y="234" class="dg-cap">Civil Code &#167;5551</text>
<line x1="474" y1="248" x2="806" y2="248" stroke="var(--blue)" stroke-opacity=".4"/>
<text x="474" y="270" class="dg-cap">First inspection due <tspan class="dg-strong">1 Jan 2025</tspan></text>
<text x="474" y="290" class="dg-cap dg-mute">(not extended by AB 2579)</text>
<text x="474" y="314" class="dg-cap">Then at least every <tspan class="dg-strong">9 years</tspan></text>
<text x="474" y="334" class="dg-cap dg-mute">Licensed structural engineer</text>
<text x="474" y="350" class="dg-cap dg-mute">or architect only</text>
"""
    return _wrap("0 0 860 376",
                 ("wl-t", "Which balcony inspection law applies"),
                 ("wl-d", "A decision diagram. Buildings with three or more dwelling units and "
                          "elevated wood-framed elements split two ways. Rented apartment and "
                          "multifamily buildings fall under SB 721, Health and Safety Code section "
                          "17973, first inspection due 1 January 2026 after the AB 2579 extension "
                          "and then every six years. Condominiums and homeowner associations fall "
                          "under SB 326, Civil Code section 5551, first inspection due 1 January "
                          "2025 and then every nine years, performed only by a licensed structural "
                          "engineer or architect."),
                 body)
