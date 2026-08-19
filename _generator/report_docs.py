# -*- coding: utf-8 -*-
"""Sample report documents.

Two document-styled pages showing exactly what the client receives — one CASp
accessibility report built to Civil Code §55.53, one SB 721 exterior elevated
element report built to Health & Safety Code §17973. Both are watermarked
SAMPLE, use the same fictional engagement as the portal/checkout demo, and
carry print CSS so File → Save as PDF approximates the real deliverable.
"""
from chrome import head, foot, cta, svg, TEL, PH, EM
from blocks import img, phead

RCSS = '<link rel="stylesheet" href="/assets/css/report.css">'

NOTE = ('<div class="demo-flag doc-note">%s<div><b>Sample document</b>'
        '<p>The property, findings and measurements below are illustrative — a worked '
        'example of the format, structure and level of detail, using a fictional '
        'engagement. Your report covers your property.</p></div></div>' % svg("alert"))


def _bar(pdf_label, other_href, other_label):
    return ('<div class="doc-bar">'
            '<div style="display:flex;gap:.6rem;flex-wrap:wrap">'
            '<button class="btn btn-solid" type="button" onclick="window.print()">%s Save as PDF</button>'
            '<a class="btn btn-line" href="%s">%s %s</a></div>'
            '<a class="btn btn-ghost" href="/book.html">Book yours &rarr;</a></div>'
            % (svg("doc"), other_href, svg("arrow"), other_label))


def _letterhead(doc_type, report_no, date):
    return """
<div class="doc-ribbon">Sample</div>
<div class="doc-head">
 <a class="brand" href="/index.html" style="pointer-events:none">
  <span class="brand-mark" aria-hidden="true">CIG</span>
  <span class="brand-txt"><b>California Inspector Group</b><i>LLC &middot; statewide California</i></span>
 </a>
 <div class="doc-head-meta">
  <b>%s</b>
  Report no. %s &middot; issued %s<br>
  %s &middot; %s
 </div>
</div>""" % (doc_type, report_no, date, PH, EM)


# ================================================================ CASp sample

def build_casp_sample(write):
    findings = [
        ("F-01", "Parking", "Accessible stall access aisle slopes 4.1% at midpoint",
         "Max 2.083% in any direction", "11B-502.4", "a", "30 days"),
        ("F-02", "Parking", "No van-accessible stall; 14 stalls total provided",
         "1 van stall required per 6 accessible", "11B-208.2.4", "a", "30 days"),
        ("F-03", "Exterior route", "Cross-slope on walk from public way measures 3.4%",
         "Max 2.083% cross-slope", "11B-403.3", "b", "60 days"),
        ("F-04", "Entrance", "Door opening force measures 11 lbf",
         "Max 5 lbf, interior hinged door", "11B-404.2.9", "b", "60 days"),
        ("F-05", "Entrance", "Threshold height 3/4&Prime; without bevel",
         "Max 1/2&Prime;, beveled above 1/4&Prime;", "11B-404.2.5", "b", "60 days"),
        ("F-06", "Sales counter", "Counter height 38&Prime; with no lowered section",
         "34&Prime; max section, 36&Prime; min length", "11B-904.4.1", "a", "30 days"),
        ("F-07", "Restroom", "Side grab bar mounted at 30&Prime; above finished floor",
         "33&Prime;&ndash;36&Prime; to top of gripping surface", "11B-604.5.1", "b", "60 days"),
        ("F-08", "Restroom", "Lavatory pipes not insulated or protected",
         "Protect against contact", "11B-606.5", "c", "90 days"),
        ("F-09", "Signage", "No ISA at accessible entrance; restroom signage lacks braille",
         "Braille + raised characters required", "11B-703.2", "c", "90 days"),
        ("F-10", "Interior route", "Display fixture narrows aisle to 32&Prime; for 30&Prime; run",
         "36&Prime; min continuous clear width", "11B-403.5.1", "b", "60 days"),
    ]
    rows = "".join(
        '<tr><td><b>%s</b></td><td>%s</td><td>%s</td><td>%s <span class="code">%s</span></td>'
        '<td><span class="sev sev-%s">%s</span></td><td>%s</td></tr>'
        % (fid, loc, obs, req, code, sev,
           {"a": "Priority", "b": "Correct", "c": "Plan"}[sev], sched)
        for fid, loc, obs, req, code, sev, sched in findings)

    body = phead(
        "Sample CASp inspection report",
        "A worked example of the deliverable — built to Civil Code &sect;55.53, the way a "
        "court, a lender or a contractor will actually read it.",
        [("Home", "/index.html"), ("Sample reports", None)]) + """
<div class="doc-stage">
 {note}
 {bar}
 <article class="doc">
  {letterhead}
  <p class="doc-title">CASp Property Inspection Report</p>
  <p class="doc-sub">Construction-related accessibility &middot; Civil Code &sect;&sect;55.51&ndash;55.545</p>

  <div class="doc-meta">
   <div><span>Property</span><b>1420 Alisal Street, Salinas, CA 93905</b></div>
   <div><span>Client</span><b>Alisal Mercantile LLC</b></div>
   <div><span>Engagement</span><b>CIG-2026-0418</b></div>
   <div><span>Occupancy</span><b>Retail &mdash; M, 2,180 sq ft</b></div>
   <div><span>Inspection date</span><b>28 April 2026</b></div>
   <div><span>Standards applied</span><b>2022 CBC Ch. 11B &middot; 2010 ADAS</b></div>
  </div>

  <h2><span class="no">1</span>Statement pursuant to Civil Code &sect;55.53</h2>
  <div class="doc-statute">
   <b>This site was inspected by a Certified Access Specialist and does not meet applicable
   construction-related accessibility standards.</b> This report describes the structures and
   areas inspected, states the date of inspection, identifies the corrections needed, sets an
   itemised schedule of completion for each, and is signed by the certifying CASp. Upon
   issue, a Disability Access Inspection Certificate was provided &mdash; a record of
   inspection, not a certificate of compliance.
  </div>

  <h2><span class="no">2</span>Structures and areas inspected</h2>
  <p>The single-storey retail building and site, comprising: off-street parking (14 stalls)
   and passenger loading; the exterior accessible route from the public way and from parking
   to the principal entrance; the principal entrance and secondary exit; interior circulation
   and sales floor; the sales counter; the single-user restroom; and interior and exterior
   signage. Storage mezzanine excluded (not open to the public).</p>

  <h2><span class="no">3</span>Summary of findings</h2>
  <p>Thirty-four findings were recorded; <b>six are priority items</b> on the accessible
   route, parking and sales counter. The ten shown below illustrate the format &mdash; every
   finding is stated as a measurement against the applicable standard, so any disputed item
   can be re-measured rather than argued.</p>

  <div class="tw"><table>
   <thead><tr><th>Ref</th><th>Location</th><th>Condition observed</th>
   <th>Requirement</th><th>Class</th><th>Schedule</th></tr></thead>
   <tbody>{rows}</tbody>
  </table></div>
  <p style="font-size:.78rem;color:var(--mute)">Sample shows 10 of 34 findings.
   Classes: <span class="sev sev-a">Priority</span> barrier on a primary function &middot;
   <span class="sev sev-b">Correct</span> within schedule &middot;
   <span class="sev sev-c">Plan</span> with next capital works.</p>

  <h2><span class="no">4</span>Representative photographs</h2>
  <div class="doc-photos">
   <figure>{ph1}<figcaption><b>F-01</b> &middot; Access aisle, digital level reading at midpoint</figcaption></figure>
   <figure>{ph2}<figcaption><b>F-03</b> &middot; Exterior route, cross-slope measurement stations</figcaption></figure>
   <figure>{ph3}<figcaption><b>F-07</b> &middot; Restroom side wall, grab bar mounting height</figcaption></figure>
  </div>
  <p style="font-size:.78rem;color:var(--mute)">The full report carries 118 located and
   captioned photographs; three are reproduced here.</p>

  <h2><span class="no">5</span>Schedule of completion</h2>
  <p>Priority items within <b>30 days</b>; corrective items within <b>60 days</b>; planning
   items within <b>90 days</b> or the next tenant improvement, whichever is sooner. On written
   notice of completion, California Inspector Group will re-inspect the corrected items and
   issue a supplement documenting the corrected condition.</p>

  <div class="doc-statute">
   <b>Why the schedule matters.</b> Qualified defendant protections under Civil Code
   &sect;55.54 attach where the inspection, this report and its schedule of completion
   pre-date any claim &mdash; and minimum statutory damages may be reduced under &sect;55.56
   where corrections meet the statutory windows. Working this schedule is what those
   protections assume.
  </div>

  <h2><span class="no">6</span>Certification</h2>
  <div class="doc-sign">
   <div><p class="doc-sig">Robert Lehman</p><b>Robert Lehman</b>
    Certified Access Specialist &middot; CASp No. [&bull;&bull;&bull;]<br>
    California Inspector Group LLC</div>
   <div style="display:flex;align-items:flex-end"><span>Disability Access Inspection
    Certificate No. [&bull;&bull;&bull;] issued to the client with this report.</span></div>
  </div>

  <div class="doc-foot">
   <span>CASp Inspection Report &middot; CIG-2026-0418 &middot; page 1 of 42 (sample extract)</span>
   <span>SAMPLE &mdash; illustrative property and findings</span>
  </div>
 </article>
</div>
{cta}
""".format(note=NOTE,
           bar=_bar("", "/samples/sb721-report.html", "See the SB 721 sample"),
           letterhead=_letterhead("CASp Inspection Report", "CIG-2026-0418", "5 May 2026"),
           rows=rows,
           ph1=img("parking-stalls", "Accessible parking stalls with painted markings"),
           ph2=img("sidewalk-ramp", "Exterior accessible route with gradual ramp"),
           ph3=img("restroom", "Restroom grab bars at the water closet"),
           cta=cta("This is what you are buying",
                   "A document written to be handed to somebody else — a judge, a lender, "
                   "a board, a contractor. Book yours online in about four minutes."))
    write("samples/casp-report.html", head(
        "Sample CASp Inspection Report | California Inspector Group",
        "A worked example of a CASp report built to Civil Code §55.53: areas inspected, "
        "itemised findings with measurements and code sections, schedule of completion, "
        "certification and the Disability Access Inspection Certificate.",
        "/samples/casp-report.html", extra_css=RCSS) + body + foot())


# ================================================================ SB721 sample

def build_sb721_sample(write):
    elements = [
        ("B-201", "Balcony, Bldg A", "Ledger flashing staining; moisture 22% at ledger; "
         "fasteners sound", "fair", "3&ndash;5 yrs", "Replace membrane &amp; flashing; re-read in 12 mo"),
        ("B-104", "Balcony, Bldg A", "Surface coating worn; framing dry (11%); connections tight",
         "good", "8&ndash;10 yrs", "Recoat walking surface within 24 mo"),
        ("B-107", "Balcony, Bldg A", "Fungal decay in two joists at ledger; deflection under load",
         "threat", "&mdash;", "Access prevented, shoring installed; see &sect;6"),
        ("W-02", "Walkway, Bldg B", "Fastener corrosion at three hangers; localised soft decking",
         "poor", "1&ndash;2 yrs", "Replace hangers; open soffit for framing verification"),
        ("W-05", "Walkway, Bldg B", "Drainage ponding at east end; membrane intact",
         "fair", "4&ndash;6 yrs", "Correct slope to drain at next resurfacing"),
        ("S-01", "Exterior stair, Bldg C", "Guardrail post movement at top landing; infill compliant",
         "poor", "1&ndash;2 yrs", "Re-anchor posts; torque-check all landings"),
        ("S-03", "Exterior stair, Bldg C", "Stringers, treads and rails sound; coating intact",
         "good", "9+ yrs", "Routine maintenance only"),
        ("L-02", "Landing, Bldg C", "Hairline surface checking; no moisture ingress (9%)",
         "good", "7&ndash;9 yrs", "Monitor at next cycle"),
    ]
    cond_label = {"good": "Good", "fair": "Fair", "poor": "Poor", "threat": "Immediate threat"}
    rows = "".join(
        '<tr><td><b>%s</b></td><td>%s</td><td>%s</td>'
        '<td><span class="cond cond-%s">%s</span></td><td>%s</td><td>%s</td></tr>'
        % (eid, loc, obs, c, cond_label[c], life, rec)
        for eid, loc, obs, c, life, rec in elements)

    body = phead(
        "Sample SB 721 inspection report",
        "A worked example of the exterior elevated element report &mdash; built to Health "
        "&amp; Safety Code &sect;17973, including the baseline your next inspection is "
        "compared against.",
        [("Home", "/index.html"), ("Sample reports", None)], amber=True) + """
<div class="doc-stage">
 {note}
 {bar}
 <article class="doc">
  {letterhead}
  <p class="doc-title">Exterior Elevated Element Inspection Report</p>
  <p class="doc-sub">SB 721 &middot; Health &amp; Safety Code &sect;17973 &middot; multifamily, 3+ units</p>

  <div class="doc-meta">
   <div><span>Property</span><b>Casa Robles Apartments, 2847 Fulton Grove, Sacramento, CA</b></div>
   <div><span>Client</span><b>Fulton Grove Holdings LP</b></div>
   <div><span>Engagement</span><b>CIG-2026-0533</b></div>
   <div><span>Buildings / units</span><b>3 buildings &middot; 24 units</b></div>
   <div><span>Inspection dates</span><b>11&ndash;12 June 2026</b></div>
   <div><span>Next inspection due</span><b>By 1 January 2032 (6-year cycle)</b></div>
  </div>

  <h2><span class="no">1</span>Scope and sampling</h2>
  <p>The property carries <b>46 exterior elevated elements</b> supported substantially by
   wood: 24 balconies, 12 elevated walkway segments, 6 exterior stairs and 4 landings. A
   statistically significant sample of <b>no less than 15% of each element type</b> was
   inspected as &sect;17973 requires &mdash; 8 elements in this engagement, selected across
   buildings, exposures and construction eras. Methods: visual examination, moisture-meter
   readings at ledgers and posts, fastener torque checks, and borescope examination through
   existing soffit vents. No destructive openings were made; &sect;5 recommends one.</p>

  <h2><span class="no">2</span>Condition, projected service life and recommendations</h2>
  <div class="tw"><table>
   <thead><tr><th>Element</th><th>Location</th><th>Current physical condition</th>
   <th>Rating</th><th>Projected service life</th><th>Recommendation</th></tr></thead>
   <tbody>{rows}</tbody>
  </table></div>

  <h2><span class="no">3</span>Representative photographs</h2>
  <div class="doc-photos">
   <figure>{ph1}<figcaption><b>B-201</b> &middot; Ledger line staining below balcony, Bldg A north elevation</figcaption></figure>
   <figure>{ph2}<figcaption><b>B-107</b> &middot; Joist decay at ledger, borescope frame through soffit vent</figcaption></figure>
   <figure>{ph3}<figcaption><b>W-02</b> &middot; Hanger corrosion, walkway W-02 mid-span</figcaption></figure>
  </div>

  <h2><span class="no">4</span>Baseline for future comparison</h2>
  <p>Photographs, moisture readings and the narrative above establish the baseline
   &sect;17973 requires, against which the next inspection &mdash; due no later than
   <b>1 January 2032</b> &mdash; can measure deterioration rather than guess at it. All
   readings are logged by element ID and elevation in Appendix B.</p>

  <h2><span class="no">5</span>Further inspection recommended</h2>
  <p>Walkway W-02: open the soffit at the two soft-decking locations to verify framing
   condition before hanger replacement is scoped. This is the only destructive verification
   recommended; it should be performed with, not before, the repair mobilisation.</p>

  <h2><span class="no">6</span>Immediate threat advisory &mdash; element B-107</h2>
  <div class="doc-threat">
   <b>Immediate threat to occupant safety</b>
   Balcony B-107 exhibits fungal decay in two joists at the ledger with measurable deflection
   under load. Occupant access was prevented on the day of inspection (unit door placarded,
   balcony access secured) and temporary shoring was installed. As &sect;17973 requires, the
   local enforcement agency was notified in writing within 15 days of completion of the
   inspection, and emergency repairs have been recommended to the owner. This element is
   excluded from the service-life table pending repair and re-inspection.
  </div>

  <h2><span class="no">7</span>Certification and delivery</h2>
  <p>This report was delivered to the owner&rsquo;s designated agent within <b>45 days</b> of
   completion of the inspection, as &sect;17973 requires, and is to be retained with the
   building records for no fewer than <b>two inspection cycles</b>.</p>
  <div class="doc-sign">
   <div><p class="doc-sig">Robert Lehman</p><b>Robert Lehman</b>
    Certified building inspector &middot; Licence [&bull;&bull;&bull;]<br>
    California Inspector Group LLC</div>
   <div style="display:flex;align-items:flex-end"><span>Stamped and signed per
    &sect;17973(d). SB 326 engagements are signed by a licensed structural engineer or
    architect as Civil Code &sect;5551 requires.</span></div>
  </div>

  <div class="doc-foot">
   <span>EEE Inspection Report &middot; CIG-2026-0533 &middot; page 1 of 28 (sample extract)</span>
   <span>SAMPLE &mdash; illustrative property and findings</span>
  </div>
 </article>
</div>
{cta}
""".format(note=NOTE,
           bar=_bar("", "/samples/casp-report.html", "See the CASp sample"),
           letterhead=_letterhead("EEE Inspection Report", "CIG-2026-0533", "3 July 2026"),
           rows=rows,
           ph1=img("residential-eee", "Multi-storey residential building with wood balconies"),
           ph2=img("weathered-wood", "Close view of checked, weathered structural timber"),
           ph3=img("condo-construction", "Wood-framed multifamily construction"),
           cta=cta("Your building's baseline starts here",
                   "Both deadlines have passed. Book the inspection online, or start with "
                   "a fifteen-minute call.", variant="amber"))
    write("samples/sb721-report.html", head(
        "Sample SB 721 Balcony Inspection Report | California Inspector Group",
        "A worked example of an exterior elevated element report built to Health & Safety "
        "Code §17973: sampling, current condition, projected service life, recommendations, "
        "baseline photographs and the immediate-threat advisory.",
        "/samples/sb721-report.html", extra_css=RCSS) + body + foot())


def build(write):
    build_casp_sample(write)
    build_sb721_sample(write)
