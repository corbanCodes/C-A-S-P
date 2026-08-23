# -*- coding: utf-8 -*-
"""Business facts, service definitions and geography for Inspector Group California.

Everything the pages say about the client lives here. Legal specifics carry a
citation in the copy itself so the client can check them against the code.
"""

# 60 Minute Sites HQ form endpoint — leads land straight in the 60MS CRM.
# The route accepts JSON or form-encoded, honours the `_gotcha` honeypot, sends
# LEAD_FIELDS (name/phone/email/business/business_type) to real CRM columns and
# files every other field into a "Form extras" note. CORS is open, so the JSON
# fetch posts work cross-origin. HTTPS is required: http:// 301-redirects, and
# a browser blocks mixed-content POSTs from the HTTPS site.
FORM_ACTION = "https://60minutesites.com/form/general-contact-form-a935"
CHECKOUT_ACTION = FORM_ACTION
CALENDLY = "https://calendly.com/robert-inspectorgroupcalifornia/30min"  # Robert's own 30-min booking

BIZ = {
    "name": "Inspector Group California",
    "legal": "Inspector Group California",  # no entity suffix — LLC not yet formed
    "short": "IGC",
    "principal": "Robert Lehman",
    "phone": "408-600-7165",
    "email": "rob@inspectorgroupcalifornia.com",
    "base": "https://inspectorgroupcalifornia.com",
    "tagline": "Two California mandates. One inspector.",
    "blurb": ("CASp accessibility inspections and SB 721 / SB 326 balcony inspections, "
              "statewide across all 58 California counties."),
}

# ---------------------------------------------------------------- service lines

# line: "access" (CASp — voluntary shield) or "structural" (EEE — mandatory)
SERVICES = [
    {
        "slug": "casp-inspection",
        "line": "access",
        "name": "CASp property inspection",
        "short": "CASp inspection",
        "icon": "shield",
        "img": "plaza-ramp",
        "teaser": ("A full walk of your property against California and federal accessibility "
                   "standards, ending in the report that makes you a qualified defendant."),
        "lede": ("The core service. A Certified Access Specialist walks the property, measures "
                 "what actually matters, and writes the report that changes your legal position "
                 "the day it lands in your hands."),
        "points": [
            ("What we walk",
             "Parking and passenger loading, the path of travel from the property line and "
             "from parking to the entrance, entrances and doors, interior circulation, "
             "restrooms, service counters, seating, signage, drinking fountains, telephones "
             "and any element your public actually touches."),
            ("What we measure",
             "Slopes and cross-slopes, clear widths, door opening force and hardware height, "
             "strike-side clearance, ramp rise and landings, counter heights, grab bar "
             "placement, turning space, reach ranges and mounting heights — the dimensions "
             "that decide the case, not a general impression."),
            ("What you get",
             "A CASp report written to Civil Code &sect;55.53: a description of the areas "
             "inspected, the inspection date, a signed statement, an itemised list of each "
             "correction needed and a schedule of completion for each one."),
            ("Why it is the only inspection that counts",
             "An architect or an engineer can tell you the same things are wrong. Only a "
             "CASp report earns qualified defendant status under the Construction-Related "
             "Accessibility Standards Compliance Act. The certification is the point."),
        ],
    },
    {
        "slug": "casp-plan-review",
        "line": "access",
        "name": "Pre-construction CASp plan review",
        "short": "Plan review",
        "icon": "plans",
        "img": "commercial-street",
        "teaser": ("Catch the non-compliant detail while it is still a line on a drawing, "
                   "not a demolished restroom wall."),
        "lede": ("The cheapest accessibility correction in the world is the one made in "
                 "CAD. We review drawings before they are built and again before they "
                 "are signed off."),
        "points": [
            ("Design-phase review",
             "We mark up the drawings against the current California Building Code Chapter "
             "11B and the 2010 ADA Standards — parking counts and location, accessible route "
             "slopes, door clearances, restroom layouts, counter and reach ranges."),
            ("Tenant improvements",
             "A remodel can drag path-of-travel obligations into scope. We tell you what "
             "the permit is about to trigger before you commit the budget."),
            ("Post-construction verification",
             "A drawing that complied does not prove a building that complies. We verify "
             "the built condition and issue the CASp report on the finished work."),
            ("New construction advantage",
             "Facilities built or improved under permits issued on or after 1 January 2008 "
             "can already qualify for reduced statutory damages. We confirm whether yours "
             "does and document it."),
        ],
    },
    {
        "slug": "casp-lawsuit-response",
        "line": "access",
        "name": "Served with a claim",
        "short": "Lawsuit response",
        "icon": "alert",
        "img": "entrance-ramp",
        "teaser": ("A demand letter or a complaint arrived. What you do in the next few "
                   "weeks decides what this costs."),
        "lede": ("If you already hold a CASp report, you have moves available that most "
                 "defendants do not. If you do not, there is still a correction clock "
                 "worth beating. Either way, speed matters."),
        "points": [
            ("If you already had the inspection",
             "You may apply to the court for a 90-day stay and an early evaluation "
             "conference as a qualified defendant under Civil Code &sect;55.54. Protections "
             "apply only where the inspection, report and correction schedule pre-date the "
             "filing — which is exactly why the inspection is worth doing early."),
            ("If you did not",
             "Correction timing still moves the number. Under Civil Code &sect;55.56 minimum "
             "statutory damages can drop to $1,000 per offence where the violations are "
             "corrected within 60 days of service and the site was CASp-inspected or built "
             "under a post-2008 permit; a qualifying small business that corrects within "
             "30 days may see $2,000 instead of $4,000."),
            ("Documentation your counsel can use",
             "We inspect, we itemise, we date everything and we produce the schedule of "
             "completion. Your attorney argues the law; we supply the record."),
            ("Re-inspection and sign-off",
             "Once the corrections are made we come back, verify them and document the "
             "corrected condition so the fix is provable rather than asserted."),
        ],
        "note": ("We are inspectors, not attorneys. Nothing here is legal advice and we do "
                 "not represent anyone in litigation. Retain California counsel on any "
                 "active claim."),
    },
    {
        "slug": "casp-lease-disclosure",
        "line": "access",
        "name": "Commercial lease disclosure",
        "short": "Lease disclosure",
        "icon": "doc",
        "img": "handrail",
        "teaser": ("Civil Code &sect;1938 makes every commercial lease say whether the space "
                   "has been CASp-inspected. Most say no."),
        "lede": ("Landlords and property managers have a disclosure obligation on every "
                 "commercial lease. Answering it with a real inspection is a leasing "
                 "advantage; answering it with the statutory boilerplate is a question "
                 "your prospect will ask about."),
        "points": [
            ("The obligation",
             "Every commercial lease or rental agreement must state whether the premises "
             "have been inspected by a CASp and, if so, whether the property meets "
             "applicable construction-related accessibility standards."),
            ("The tenant's rights",
             "Where a report exists, the prospective tenant must have the chance to review "
             "it before signing. If it is not provided at least 48 hours before execution, "
             "the tenant may rescind for 72 hours after signing."),
            ("Where no certificate exists",
             "The lease must carry statutory language telling the tenant a CASp may inspect "
             "the premises and that the landlord may not prohibit an inspection the tenant "
             "requests. Whoever pays for repairs is then a negotiation."),
            ("Portfolio disclosure packages",
             "For owners with several buildings we inspect on a schedule and hand back one "
             "consistent disclosure package per property rather than a scramble per lease."),
        ],
    },
    {
        "slug": "sb-721-inspection",
        "line": "structural",
        "name": "SB 721 balcony inspection",
        "short": "SB 721 — apartments",
        "icon": "building",
        "img": "residential-eee",
        "teaser": ("Apartment buildings with three or more units. The first deadline has "
                   "already passed."),
        "lede": ("Health and Safety Code &sect;17973 — added by SB 721 and extended once by "
                 "AB 2579 — requires the owner of a multifamily rental building with three "
                 "or more dwelling units to have every exterior elevated element inspected."),
        "points": [
            ("Who it covers",
             "Buildings with three or more multifamily dwelling units. Condominiums and "
             "common interest developments fall under SB 326 instead."),
            ("What counts as an exterior elevated element",
             "Balconies, decks, porches, stairways, walkways and elevated entry structures "
             "that extend beyond the exterior walls, carry a walking surface more than six "
             "feet above ground level, are designed for human occupancy or use, and are "
             "supported substantially by wood or wood-based products."),
            ("The deadline",
             "The first inspection was due 1 January 2025, extended to 1 January 2026 by "
             "AB 2579. That date has passed. Inspections then repeat at least every six "
             "years, aligned to the building's inspection cycle."),
            ("What the inspection covers",
             "A statistically significant sample — at least 15% of each type of element — "
             "examined for the load-bearing components and the waterproofing that protects "
             "them. Reports are retained by the owner for two inspection cycles."),
            ("When something is unsafe",
             "An element that poses an immediate threat to safety means the local code "
             "enforcement agency is notified within 15 days and the element comes out of "
             "service until it is repaired. Non-emergency repairs run on a permit clock."),
            ("Who may perform it",
             "A licensed architect, a licensed civil or structural engineer, a contractor "
             "holding an A, B or C-5 licence with at least five years of relevant "
             "experience, or a certified building inspector or building official."),
        ],
    },
    {
        "slug": "sb-326-inspection",
        "line": "structural",
        "name": "SB 326 balcony inspection",
        "short": "SB 326 — condos &amp; HOAs",
        "icon": "hoa",
        "img": "condo-lake",
        "teaser": ("Condominiums and common interest developments. A board duty, on a "
                   "nine-year cycle, tied to the reserve study."),
        "lede": ("Civil Code &sect;5551 — added by SB 326 — puts the inspection duty on the "
                 "association rather than an individual owner, and ties the result to the "
                 "money the association is supposed to be setting aside."),
        "points": [
            ("Who it covers",
             "Condominium projects and common interest developments of three or more "
             "dwelling units where the association carries maintenance responsibility for "
             "the elements."),
            ("The deadline",
             "The first inspection was due 1 January 2025 and was not extended by AB 2579 — "
             "that extension moved SB 721 only. Inspections repeat at least every nine "
             "years thereafter."),
            ("Who may perform it",
             "A licensed structural engineer or architect. The qualification bar is "
             "narrower than SB 721's, and we staff these inspections accordingly."),
            ("What the board receives",
             "A report on the physical condition and remaining useful life of the elements, "
             "delivered to the board and incorporated into the reserve study under Civil "
             "Code &sect;5550 — which is where a deferred repair becomes a funding decision."),
            ("When something is unsafe",
             "Where an element poses an immediate threat, local code enforcement is notified "
             "within 15 days and the association takes the element out of service until it "
             "is repaired."),
            ("Why boards get caught",
             "The duty sits with the association, the cost hits the reserve, and the "
             "cycle is long enough that nobody on the current board remembers the last one. "
             "We put it on a calendar."),
        ],
    },
]

SERVICE_BY_SLUG = {s["slug"]: s for s in SERVICES}
ACCESS_SERVICES = [s for s in SERVICES if s["line"] == "access"]
STRUCT_SERVICES = [s for s in SERVICES if s["line"] == "structural"]

# ---------------------------------------------------------------- what we check

PATH_OF_TRAVEL = [
    ("Parking", "Count, location, stall and access aisle dimensions, slope, signage, van spaces."),
    ("Route", "The accessible path from the property line and from parking, its width, running "
              "slope, cross-slope, changes in level and obstructions."),
    ("Entrance", "Door clear width, opening force, hardware type and height, strike-side "
                 "clearance, thresholds, landings."),
    ("Interior", "Circulation width, protruding objects, seating, aisles, elevator access "
                 "where present."),
    ("Restrooms", "Turning space, stall dimensions, grab bar placement, lavatory knee clearance, "
                  "pipe protection, dispenser reach ranges, mirror and signage heights."),
    ("Counters", "Service and transaction counter heights, queue routing, point-of-sale reach."),
]

EEE_CHECKS = [
    ("Load-bearing components", "Ledgers, joists, beams, posts, cantilevers and their "
                                "connections — the elements that carry the load to the building."),
    ("Connections and fasteners", "Corrosion, loosening and displacement at the hardware "
                                  "that ties the element to the structure."),
    ("Waterproofing", "Membranes, coatings, deck surfaces and their terminations — the "
                      "system that keeps water off the wood."),
    ("Flashing and drainage", "Ledger flashing, counterflashing, weep paths, slope to drain "
                              "and where water actually goes in a storm."),
    ("Dry rot and decay", "Fungal decay in concealed framing, most often where a failed "
                          "membrane has been quietly wetting a ledger for years."),
    ("Guardrails and handrails", "Height, infill spacing, and whether the assembly is still "
                                 "attached to something sound."),
]

# ---------------------------------------------------------------- process

PROCESS = [
    ("Call or send the form",
     "Tell us the property type, the address and which mandate you are dealing with. If you "
     "are not sure which one applies to you, that is a normal question and the call is free."),
    ("Scope and quote",
     "We confirm square footage, unit counts, how many exterior elevated elements exist and "
     "what standards apply based on the building's age and permit history. You get a flat "
     "price before anyone schedules anything."),
    ("The inspection",
     "We walk the property with instruments, not impressions. Most single-tenant commercial "
     "sites take a few hours; multifamily EEE inspections scale with unit count."),
    ("The report",
     "A written report you can hand to a lawyer, a board, a lender or a code official. "
     "Itemised findings, photographs, the applicable standard for each item and a schedule "
     "of completion."),
    ("Corrections",
     "You fix what the report lists, using your own contractors. We do not sell the repairs "
     "we recommend, which is the entire reason our findings are worth reading."),
    ("Re-inspection and the calendar",
     "We verify the corrections, document the corrected condition, and put your next cycle "
     "date on a calendar so the six or nine year clock does not run out unnoticed."),
]

# ---------------------------------------------------------------- geography

REGIONS = [
    ("bay-area", "San Francisco Bay Area",
     ["San Francisco", "San Mateo", "Santa Clara", "Alameda", "Contra Costa", "Marin",
      "Sonoma", "Napa", "Solano"],
     "Dense commercial frontage, a long tail of pre-1990 storefronts on tight lots, and "
     "one of the highest concentrations of construction-related accessibility filings in "
     "the state."),
    ("sacramento", "Sacramento &amp; the Capital Region",
     ["Sacramento", "Placer", "El Dorado", "Yolo", "Sutter", "Yuba", "Nevada"],
     "State offices, a wide band of garden-style apartment stock from the 1970s and 80s, "
     "and the wood-framed walkways that come with it."),
    ("central-valley", "Central Valley",
     ["San Joaquin", "Stanislaus", "Merced", "Fresno", "Madera", "Kings", "Tulare", "Kern"],
     "Fast-growing multifamily construction alongside older main-street retail that has "
     "never been formally assessed."),
    ("los-angeles", "Los Angeles County",
     ["Los Angeles"],
     "The largest concentration of apartment buildings in California and the deepest pool "
     "of accessibility litigation. SB 721 exposure here is measured in tens of thousands "
     "of buildings."),
    ("orange-county", "Orange County",
     ["Orange"],
     "Heavy condominium and common interest development stock, which puts SB 326 board "
     "duties near the top of the agenda."),
    ("inland-empire", "Inland Empire",
     ["Riverside", "San Bernardino"],
     "Rapid multifamily growth, large HOA communities and long distances between "
     "inspectors — scheduling matters more here than almost anywhere."),
    ("san-diego", "San Diego County",
     ["San Diego", "Imperial"],
     "Coastal exposure accelerates waterproofing failure on exterior elevated elements, "
     "and the tourist-facing retail base draws accessibility claims."),
    ("central-coast", "Central Coast",
     ["Santa Barbara", "Ventura", "San Luis Obispo", "Monterey", "Santa Cruz", "San Benito"],
     "Historic downtowns where accessible routes were retrofitted piecemeal, plus salt air "
     "working on balcony connections."),
    ("north-coast", "North Coast &amp; Far North",
     ["Humboldt", "Mendocino", "Lake", "Del Norte", "Trinity", "Siskiyou", "Shasta",
      "Tehama", "Glenn", "Colusa", "Butte", "Plumas", "Lassen", "Modoc"],
     "Small commercial districts, wet winters and wood-framed decks that take the weather "
     "harder than anything on the coast."),
    ("eastern-sierra", "Eastern Sierra, Gold Country &amp; Desert",
     ["Mono", "Inyo", "Alpine", "Amador", "Calaveras", "Tuolumne", "Mariposa", "Sierra"],
     "Freeze-thaw cycles and snow load on exterior stairs and walkways, plus resort "
     "properties with heavy public access."),
]

COUNTIES = [
    "Alameda", "Alpine", "Amador", "Butte", "Calaveras", "Colusa", "Contra Costa",
    "Del Norte", "El Dorado", "Fresno", "Glenn", "Humboldt", "Imperial", "Inyo", "Kern",
    "Kings", "Lake", "Lassen", "Los Angeles", "Madera", "Marin", "Mariposa", "Mendocino",
    "Merced", "Modoc", "Mono", "Monterey", "Napa", "Nevada", "Orange", "Placer", "Plumas",
    "Riverside", "Sacramento", "San Benito", "San Bernardino", "San Diego", "San Francisco",
    "San Joaquin", "San Luis Obispo", "San Mateo", "Santa Barbara", "Santa Clara",
    "Santa Cruz", "Shasta", "Sierra", "Siskiyou", "Solano", "Sonoma", "Stanislaus",
    "Sutter", "Tehama", "Trinity", "Tulare", "Tuolumne", "Ventura", "Yolo", "Yuba",
]

# ---------------------------------------------------------------- who needs this

AUDIENCES = [
    ("Retail &amp; restaurants", "storefront",
     "Anything the public walks into. The highest-frequency target for construction-related "
     "accessibility claims in California."),
    ("Apartment owners", "building",
     "Three or more units means SB 721 applies to every balcony, walkway and exterior "
     "stairway over six feet."),
    ("HOA &amp; condo boards", "hoa",
     "SB 326 puts the duty on the association and the cost in the reserve study."),
    ("Medical &amp; professional offices", "doc",
     "Public accommodation obligations apply the moment a patient or client can walk in."),
    ("Hotels &amp; hospitality", "bed",
     "Guest rooms, common areas, pools and the exterior walkways connecting them."),
    ("Property managers", "keys",
     "One inspector, one report format, every property in the portfolio on one calendar."),
    ("Commercial landlords", "doc",
     "Civil Code &sect;1938 disclosure on every lease you sign."),
    ("Public agencies", "shield",
     "Facilities open to the public, held to the same standards and audited more often."),
]

# ---------------------------------------------------------------- faq

FAQ = [
    ("access", "What does CASp actually stand for?",
     "Certified Access Specialist. The programme is run by the California Division of the "
     "State Architect, part of the Department of General Services, and it certifies "
     "individuals to inspect buildings against state and federal construction-related "
     "accessibility standards. Be careful searching for it — <b>CASP</b> is also the name "
     "of an unrelated cybersecurity credential, and most of the search results you will "
     "find are for that one."),
    ("access", "Is a CASp inspection required by law?",
     "No. It is voluntary. Nothing in California law compels a business to get one. What it "
     "does is change your legal position if you are sued, which is why owners choose it."),
    ("access", "So why would I pay for something optional?",
     "Because the alternative is priced by somebody else. California's Unruh Civil Rights Act "
     "carries minimum statutory damages of $4,000 per offence plus the plaintiff's attorney "
     "fees, and a single visit can generate multiple alleged offences. In 2025 alone, 3,252 "
     "federal ADA lawsuits were filed in California &mdash; more than any other state, about "
     "271 a month &mdash; and a handful of firms and serial plaintiffs file most of them. A "
     "CASp inspection is a known, one-time cost. A claim is not."),
    ("access", "What is CRASCA?",
     "The <b>Construction-Related Accessibility Standards Compliance Act</b> &mdash; SB 1608, "
     "passed in 2008, now Civil Code &sect;&sect;55.51&ndash;55.545. It created the CASp "
     "program and everything this site describes: the state certifies access specialists, and "
     "owners who hire one and work the report's schedule get treated differently by the "
     "courts &mdash; the stay of proceedings, the early evaluation conference, the reduced "
     "damages tiers. California's stated intent is compliance with help, not litigation. "
     "Google CRASCA; the statute says what we say."),
    ("access", "What is &lsquo;qualified defendant&rsquo; status?",
     "If your site has been CASp-inspected and you are sued over construction-related "
     "accessibility, you may apply to the court for a stay of proceedings and an early "
     "evaluation conference under Civil Code &sect;55.54. It pauses the case for 90 days and "
     "puts a judge in front of both parties early, before fees compound."),
    ("access", "Does the report have to come before the lawsuit?",
     "Yes, and this is the part people get wrong. The inspection, the report and the schedule "
     "of completion have to pre-date the filing for qualified defendant protections to apply. "
     "You cannot buy the shield after the arrow lands."),
    ("access", "Does a CASp report mean I cannot be sued?",
     "No. Anyone can file. It means that when someone does, you are in a different procedural "
     "category with a different damages exposure and a documented record of what you knew and "
     "when you planned to fix it."),
    ("access", "What if the report finds violations?",
     "It usually does — that is the point of looking. The report lists each item with a "
     "schedule of completion. Working that schedule is what protects you; a report you file "
     "in a drawer and ignore is worth much less."),
    ("access", "Is the Disability Access Inspection Certificate proof I am compliant?",
     "No. DSA is explicit that the certificate is a record that an inspection happened, not a "
     "certificate of compliance. Keep it available; do not treat it as a clean bill of health."),
    ("structural", "What are SB 721 and SB 326?",
     "Two California laws requiring inspection of exterior elevated elements — balconies, "
     "decks, stairways, walkways and similar structures more than six feet above the ground "
     "and supported substantially by wood. SB 721 covers apartment buildings with three or "
     "more units. SB 326 covers condominiums and common interest developments."),
    ("structural", "Are these optional too?",
     "No. These are mandatory. CASp is the shield you choose; this is the law you cannot "
     "skip. If your building is in scope, the inspection is required and the deadline has "
     "already passed."),
    ("structural", "What is the deadline?",
     "SB 326's first inspection was due 1 January 2025. SB 721's was due 1 January 2025 and "
     "was extended one year to 1 January 2026 by AB 2579. Both dates are behind us. After the "
     "first inspection, SB 721 repeats at least every six years and SB 326 at least every nine."),
    ("structural", "My building has balconies but they are concrete. Am I in scope?",
     "Probably not for these statutes, which reach elements supported substantially by wood or "
     "wood-based products. That said, &lsquo;concrete balcony&rsquo; often means a concrete "
     "topping over wood framing. It is worth twenty minutes of somebody competent looking "
     "rather than an assumption."),
    ("structural", "What is the six-foot rule exactly?",
     "The walking surface has to be more than six feet above the ground below. A ground-floor "
     "patio is out. A second-storey walkway is in. Mixed properties usually have both, which "
     "is why the sampling is done by element type."),
    ("structural", "Do you inspect every single balcony?",
     "Not necessarily. SB 721 calls for a statistically significant sample — at least 15% of "
     "each type of element. If the sample turns up problems, the sample widens. SB 326 works "
     "to a similar sampling logic under the association's report."),
    ("structural", "What happens if you find something dangerous?",
     "If an element poses an immediate threat to safety, the local code enforcement agency is "
     "notified within 15 days and the element comes out of service until it is repaired. That "
     "is not our discretion; it is what the statutes require."),
    ("structural", "Who is allowed to sign these reports?",
     "SB 721 accepts a licensed architect, a licensed civil or structural engineer, a "
     "contractor holding an A, B or C-5 licence with five or more years of relevant "
     "experience, or a certified building inspector. SB 326 is narrower — a licensed "
     "structural engineer or architect."),
    ("general", "Do you do the repairs as well?",
     "No, deliberately. We inspect and we report. An inspector who sells the repair he "
     "recommends has an obvious reason to find more of them, and a report written that way is "
     "worth less to a court, a board and a lender. Use your own contractors."),
    ("general", "Do you offer net-30 or other payment terms?",
     "No &mdash; and this is a firm policy, not an opening position. The deposit is 20% on "
     "signing; it confirms the booking and it is what puts an inspector on the road, "
     "anywhere in the state, hotels included. The balance falls due when the report is "
     "complete, and paying it is what releases the report. No net-30, no net-anything, and "
     "no retention or retainage &mdash; however large the organisation or its AP process. "
     "Our founder spent years consulting on large development projects under net-30 terms "
     "with 10% retention holdbacks, in effect financing other people's projects. This firm "
     "does not do that, and clients benefit from it: nobody's unpaid invoices are priced "
     "into your inspection."),
    ("general", "How do I actually receive the report?",
     "As a signed PDF, the moment the balance clears &mdash; it unlocks in your client "
     "portal and is emailed to you, along with the photograph set and the schedule of "
     "completion. If an element poses an immediate safety threat we tell you (and the "
     "enforcement agency) right away, paid or not; the gate applies to the report, never "
     "to a hazard."),
    ("general", "How much does it cost?",
     "It depends on square footage, unit count and how many exterior elevated elements are on "
     "the property. We quote a flat price after a short call. No hourly surprises. Sending "
     "photos with your request helps us hold that price &mdash; if the property turns out to "
     "differ materially from what was described or shown, the fee is re-quoted on site "
     "before the inspection proceeds, not invoiced as a surprise afterwards."),
    ("general", "How far do you travel?",
     "All 58 counties. We are a statewide practice; travel outside the immediate region is "
     "quoted up front so it is never a line item you find later."),
    ("general", "Can you do both inspections in one visit?",
     "Frequently, yes — a multifamily property with retail on the ground floor can need both, "
     "and combining them saves a mobilisation. Ask when you call."),
]

# ---------------------------------------------------------------- trust signals

STATS = [
    ("58", "California counties served"),
    ("$4,000", "Minimum Unruh damages per offence"),
    ("90", "Day stay for a qualified defendant"),
    ("6 ft", "Height that puts a balcony in scope"),
]

# ============================================================ pricing

# Published rate card. Off-the-shelf pricing for buildings that fit a standard
# occupancy and footprint; everything larger or stranger goes to a quote.
# NOTE FOR THE CLIENT: these figures are placeholders that establish the
# structure. Robert sets the real numbers — see DEMO-NOTES.md.

SQFT_BANDS = ["Up to 1,500", "1,501 – 2,500", "2,501 – 5,000", "5,001 – 10,000", "Over 10,000"]

CASP_RATES = [
    ("Retail &amp; storefront", "storefront",
     "Shops, salons, showrooms, single-tenant retail.",
     ["$895", "$1,150", "$1,550", "$2,250", "Quote"]),
    ("Restaurant, bar &amp; cafe", "bed",
     "Dining rooms, counters, bars, patios and restrooms.",
     ["$1,050", "$1,350", "$1,750", "$2,500", "Quote"]),
    ("Office &amp; medical", "doc",
     "Professional suites, clinics, dental and urgent care.",
     ["$950", "$1,200", "$1,600", "$2,300", "Quote"]),
    ("Hotel &amp; lodging", "keys",
     "Guest rooms, lobbies, pools, meeting space and the routes between them.",
     ["$1,450", "$1,850", "$2,400", "$3,200", "Quote"]),
]

EEE_RATES = [
    ("Up to 12 units", "$1,250"),
    ("13 – 30 units", "$1,950"),
    ("31 – 60 units", "$2,950"),
    ("61 – 120 units", "$4,500"),
    ("Over 120 units", "Quote"),
]

PRICE_INCLUDES = [
    "The on-site inspection itself, by the certified or licensed inspector the statute requires",
    "All measurements, photographs and field notes",
    "The written report, itemised, with the applicable code section against each finding",
    "A schedule of completion for every correction",
    "Travel anywhere in California &mdash; quoted in the price, never added afterwards",
    "A follow-up call to walk you or your board through the findings",
]

PRICE_EXCLUDES = [
    ("Destructive or invasive testing",
     "Opening up framing, removing finishes or coring a deck. Quoted separately if the "
     "visual inspection says it is needed."),
    ("Repairs and remediation",
     "We do not perform the work we recommend, and we do not take a referral fee from "
     "anyone who does."),
    ("Re-inspection after corrections",
     "Priced at a reduced rate against the original inspection &mdash; ask when you book."),
    ("Expert witness or litigation support",
     "Billed hourly and engaged separately from the inspection agreement."),
]

CUSTOM_QUOTE = [
    ("Multi-building campuses", "A single owner with several structures on one site — one "
                                "mobilisation, one report, one price."),
    ("Statewide franchise portfolios", "Big-box and chain operators inspecting every "
                                       "California facility to one standard and one format."),
    ("Mixed-use properties", "Ground-floor retail under apartments needs both mandates. "
                             "Combined, it costs less than two separate visits."),
    ("Property management portfolios", "Every building on one calendar, invoiced together, "
                                       "with a register of what is due when."),
]

# ============================================================ booking flow

BOOK_STEPS = [
    ("Get your estimate",
     "Pick your occupancy and footprint off the rate card, then send photos and your best "
     "description of the project &mdash; every job, no exceptions. Robert reviews both and "
     "confirms the number.",
     "camera"),
    ("Sign the inspection agreement",
     "The agreement arrives with your confirmed fee. It sets out scope, exclusions, "
     "insurance, liability, confidentiality and payment terms. Signing takes a couple of "
     "minutes on a phone.",
     "doc"),
    ("Pay the 20% deposit",
     "A 20% deposit confirms the booking and holds your date. Card, ACH bank transfer or "
     "wire. The balance is not due until the work is done.",
     "scale"),
    ("Schedule the inspection",
     "Pick a date from the calendar. For occupied buildings we coordinate notice to "
     "residents; for retail we work around your trading hours.",
     "calendar"),
    ("We inspect and report",
     "We walk the property, measure everything and write it up. Turnaround is usually five "
     "to seven business days from the site visit.",
     "shield"),
    ("Pay the balance, get the report",
     "Settling the balance releases the signed PDF instantly &mdash; unlocked in your "
     "portal and emailed to you. No net terms, no retention.",
     "check"),
]

AGREEMENT_TERMS = [
    ("Scope of work",
     "Exactly which buildings, areas and elements are covered, which standard they are being "
     "measured against, and the date the inspection is scheduled for."),
    ("What is expressly excluded",
     "A visual and dimensional inspection is not destructive testing. Concealed conditions, "
     "anything behind a finish and anything not reasonably accessible on the day are outside "
     "scope unless separately engaged."),
    ("Standard of care",
     "The inspection is performed to the standard of a reasonably prudent certified inspector. "
     "A report is a professional opinion on observed conditions &mdash; it is not a warranty, "
     "a guarantee, or an insurance policy against future failure."),
    ("Insurance",
     "The commercial general liability and professional liability (errors and omissions) "
     "cover carried by the firm, with limits stated, and certificates available on request."),
    ("Client obligations",
     "Safe access to the property, keys and codes, a contact who can open locked areas, "
     "disclosure of known hazards, and any prior reports or permit history you already hold."),
    ("Limitation of liability &amp; indemnity",
     "The cap on liability, how claims are handled, and the indemnity each party gives the "
     "other. Read this section properly &mdash; it is the one your insurer will ask about."),
    ("Mandatory hazard reporting",
     "You acknowledge that where an exterior elevated element poses an immediate threat to "
     "safety, we are required by statute to notify the local enforcement agency within 15 "
     "days. That obligation is not waivable and is not ours to negotiate."),
    ("Confidentiality &amp; third-party reliance",
     "The report is prepared for you. Who else may rely on it &mdash; a lender, a buyer, a "
     "board, opposing counsel &mdash; and on what terms."),
    ("Fees &amp; payment terms",
     "The quoted fee, the 20% deposit due on signing, and the balance due on completion of "
     "the report. Paying the balance releases the signed PDF immediately. There are no net "
     "terms and no retention &mdash; the agreement says so in as many words, so nobody's "
     "accounts-payable process is surprised later. The fee relies on the property "
     "information and photographs the client provides; where the site differs materially "
     "from what was described or shown, the fee is re-quoted on site before the inspection "
     "proceeds."),
    ("Scheduling, cancellation &amp; rescheduling",
     "Notice periods, what happens if the site is not accessible on the day, and the "
     "circumstances in which the deposit is refundable."),
    ("Governing law &amp; disputes",
     "California law, the venue for any dispute, and the dispute resolution steps that come "
     "before anyone files anything."),
    ("Electronic signature consent",
     "Your consent to sign and receive documents electronically under the federal ESIGN Act "
     "and the California Uniform Electronic Transactions Act."),
]

PAY_METHODS = [
    ("Credit or debit card", "card", "Visa, Mastercard, American Express and Discover, "
                                     "processed on our payment provider&rsquo;s secure page."),
    ("ACH bank transfer", "bank", "Direct debit from a US business checking account. Lowest "
                                  "fees, usual choice for associations and management companies."),
    ("Wire transfer", "wire", "For larger portfolio engagements. Wiring instructions are "
                              "issued with the balance statement &mdash; and we will never "
                              "email you changed bank details."),
]

# ============================================================ reviews

# SAMPLE testimonials — placeholders that establish the layout and the voice.
# Robert must replace these with real, permissioned client quotes before
# launch; publishing invented reviews as genuine violates FTC endorsement
# rules. See DEMO-NOTES.md.

REVIEWS = [
    {
        "feat": True, "line": "access",
        "q": "We got the letter every California business owner dreads. Because the property "
             "had been CASp-inspected eight months earlier, our attorney applied for the stay "
             "the same week and the matter settled for a fraction of the demand. That report "
             "paid for itself many times over.",
        "name": "Maria G.", "role": "Restaurant owner", "where": "Fresno County",
    },
    {
        "line": "structural",
        "q": "Our board had been trying to price the balcony inspection for two years and "
             "getting numbers that made no sense. CIG quoted flat off the unit count, arrived "
             "when they said they would, and the report slotted straight into our reserve "
             "study. Our management company actually thanked us.",
        "name": "Susan T.", "role": "HOA board president", "where": "Orange County",
    },
    {
        "line": "structural",
        "q": "Sixty-one units across four buildings, one mobilisation. The two walkways they "
             "took out of service had dry rot you could not see from below. I did not enjoy "
             "writing that cheque, and I am very glad I did.",
        "name": "Daniel K.", "role": "Apartment owner", "where": "Santa Clara County",
    },
    {
        "line": "access",
        "q": "They marked up our tenant-improvement drawings before permit and caught a "
             "restroom layout that would have cost five figures to demolish and rebuild. "
             "The cheapest correction we ever made was the one on paper.",
        "name": "Rob V.", "role": "General contractor", "where": "Los Angeles County",
    },
    {
        "line": "general",
        "q": "We manage forty-odd properties across six counties. One inspector, one report "
             "format, one calendar. My compliance binder finally makes sense.",
        "name": "Alicia M.", "role": "Portfolio property manager", "where": "Inland Empire",
    },
    {
        "line": "access",
        "q": "Every lease we sign now answers the &sect;1938 question with a real inspection "
             "instead of the statutory boilerplate. Two tenants have told us directly that it "
             "is part of why they signed with us.",
        "name": "James H.", "role": "Commercial landlord", "where": "San Diego County",
    },
    {
        "line": "general",
        "q": "Quoted on Tuesday, inspected on Friday, report the following Thursday. Nobody "
             "else in this trade moves like that, and the price was the price.",
        "name": "Priya N.", "role": "Hotel general manager", "where": "Monterey County",
    },
    {
        "line": "structural",
        "q": "They do not sell repairs, which is exactly why I trust their list of repairs.",
        "name": "Frank D.", "role": "Condominium board treasurer", "where": "Los Angeles County",
    },
    {
        "line": "access",
        "q": "Robert measured things I did not know had rules &mdash; door pressure, counter "
             "height, the slope of my parking lot. The report reads like it was written to be "
             "handed to a judge. As I understand it, that is the point.",
        "name": "Denise O.", "role": "Boutique owner", "where": "Sacramento County",
    },
]

# ============================================================ lawsuit data

# Sourced figures for the "lawsuit reality" sections. Verified Aug 2026.
# Federal filings: Seyfarth Shaw's ADA Title III tracker (adatitleiii.com).
# Demand letters / law-firm concentration: California Commission on
# Disability Access (CCDA) reporting, to which attorneys must submit copies
# of demand letters and complaints under Civil Code §55.32.

LAWSUIT_STATS = [
    ("3,252", "Federal ADA lawsuits filed in California in 2025",
     "More than any other state — roughly 271 every month, in federal court alone."),
    ("~9 a day", "New federal accessibility filings in California",
     "Before counting state-court Unruh actions and demand letters."),
    ("2,598", "Suits filed by a single plaintiff group in 2024",
     "One organisation. Serial filers are not a rumour; they are the business model."),
    ("95.8%", "Of 2024 demand letters came from just 10 law firms",
     "Per filings reported to the state's own Commission on Disability Access."),
]

LAWSUIT_SOURCES = [
    ("Seyfarth Shaw ADA Title III tracker — 2025 filings",
     "https://www.adatitleiii.com/2026/02/ada-title-iii-federal-lawsuit-filings-fall-slightly-to-8667-in-2025/"),
    ("Seyfarth Shaw — 2024 recap (California retakes top spot)",
     "https://www.adatitleiii.com/2025/01/our-2024-ada-title-iii-recap-and-predictions-for-2025/"),
    ("California Commission on Disability Access — complaint & demand-letter reporting",
     "https://www.dgs.ca.gov/CCDA/Resources"),
]
