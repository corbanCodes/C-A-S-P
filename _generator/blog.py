# -*- coding: utf-8 -*-
"""The blog — "Field notes".

Six articles drafted from Robert's own talking points, written to be read in
five minutes by a worried owner: the civil-rights framing, the two big myths
(the grandfathered old building and the freshly-approved new one), a
self-assessment walk, who actually files these suits, and the CRASCA bargain.
Statutory claims carry their citation inline, same standard as the rest of
the site. Robert should review every piece before launch — see DEMO-NOTES.
"""
from chrome import head, foot, cta, svg, demo_btn, TEL, PH
from blocks import phead, img

# ------------------------------------------------------------------ articles

ARTICLES = [
    {
        "slug": "denying-access-is-a-civil-rights-violation",
        "title": "Denying access to your store is a civil rights violation. Literally.",
        "teaser": "Not a code infraction. Not a permitting problem. In California, a barrier "
                  "at your front door is treated the same way the law treats discrimination — "
                  "because that is what the statute says it is.",
        "cat": "access", "cat_label": "Accessibility",
        "date": "August 14, 2026", "read": "5 min",
        "img": "entrance-ramp",
        "body": """
<p>Most owners think of accessibility as a building-code issue &mdash; the same family of
rules as smoke detectors and exit signs. That mental model is the first mistake, and it is
the one lawsuits are built on.</p>

<p>California's Unruh Civil Rights Act (Civil Code &sect;51) guarantees every person
&ldquo;full and equal accommodations, advantages, facilities, privileges, or services in all
business establishments.&rdquo; And since 1992, the Act has said in as many words that
<b>any violation of the federal Americans with Disabilities Act is automatically a violation
of the Unruh Act</b> (&sect;51(f)). The consequence sits in &sect;52: minimum statutory
damages of <b>$4,000 per occasion</b>, plus the plaintiff's attorney fees.</p>

<h2>What that means at your front door</h2>
<p>A door that takes eleven pounds of force to open. A counter with no lowered section. A
restroom grab bar mounted three inches too low. A parking stall with a faded access aisle.
None of these feel like &ldquo;discrimination&rdquo; to the owner &mdash; the owner didn't
<i>intend</i> anything. But intent is not an element. If a barrier prevents a person with a
disability from the full and equal access everyone else gets, the violation exists the moment
they encounter it, and it repeats on every visit.</p>

<p>That &ldquo;per occasion&rdquo; framing matters more than it looks. A single visit can
involve the parking lot, the route, the door and the restroom &mdash; and a plaintiff who
comes back has a new occasion. The arithmetic compounds quickly, and the attorney-fee
provision means the case is economical for the plaintiff's counsel even when the damages
are small.</p>

<h2>People are sharp, and they are looking</h2>
<p>This is the part owners have trouble believing until they see the numbers: in 2025,
<b>3,252 federal ADA lawsuits were filed in California</b> &mdash; more than any other
state, roughly nine every day, before counting state-court actions and demand letters. A
single plaintiff group filed 2,598 suits in 2024. These are people who can read a parking
lot from the street &mdash; sometimes from a satellite photo &mdash; and who know exactly
what a missing van stall or a steep ramp is worth. <a href="/casp.html#numbers">The sourced
figures are here.</a></p>

<h2>The good news is structural</h2>
<p>California built an off-ramp into the same body of law. The Construction-Related
Accessibility Standards Compliance Act &mdash; <a href="/casp.html">CRASCA, the 2008 statute
behind the CASp program</a> &mdash; exists precisely because the legislature wanted owners
to fix barriers with expert help rather than discover them in litigation. A CASp inspection
before anyone files puts you in a different procedural category: proceedings can pause for
90 days, a judge looks early, and minimum damages can drop from $4,000 toward $1,000 while
you work a written correction schedule.</p>

<p>The law treats access as a civil right. The practical response is not anxiety &mdash;
it is a measured inspection, an itemised list, and dates on a calendar.</p>
""",
    },
    {
        "slug": "the-1955-building-myth",
        "title": "The 1955 building myth: there is no grandfather clause",
        "teaser": "Your building was approved decades before accessibility was law, so you're "
                  "exempt &mdash; right? No. That certificate from back in the day excuses "
                  "exactly nothing, and here is why.",
        "cat": "access", "cat_label": "Accessibility",
        "date": "August 7, 2026", "read": "6 min",
        "img": "commercial-street",
        "body": """
<p>It is the most common sentence we hear on a first call: <i>&ldquo;The building went up in
1955 &mdash; it's grandfathered.&rdquo;</i> The owner is picturing a rule that says buildings
only have to meet the law that existed when they were built. For structural matters, that
intuition is roughly how it works. For accessibility, <b>the grandfather clause does not
exist.</b></p>

<h2>Where the myth comes from</h2>
<p>Your 1955 building was designed, permitted and approved with no thought to accessibility
at all, because there was nothing to think about &mdash; the federal ADA arrived in 1990 and
California's modern access codes evolved alongside it. The original certificate of occupancy
was perfectly valid. It still is, for what it certifies. The mistake is believing it
certifies anything about today's obligations.</p>

<h2>What the law actually says about existing buildings</h2>
<p>Title III of the ADA imposes a continuing duty on public accommodations to remove
architectural barriers in <b>existing</b> facilities where removal is &ldquo;readily
achievable&rdquo; &mdash; easily accomplishable without much difficulty or expense
(42 U.S.C. &sect;12182(b)(2)(A)(iv)). That duty attached in 1992 and never expires. A ramp
at a raised entrance, re-striping the parking lot, lowering a section of counter, grab bars
in the restroom &mdash; for most small commercial buildings these are exactly the sort of
measures the statute contemplates.</p>

<p>And the moment you remodel, California adds a second layer: alterations trigger
<b>path-of-travel</b> obligations under the California Building Code (11B-202.4) &mdash;
the area you improve must be served by an accessible route, restrooms, and signage, with a
disproportionality cap of roughly 20% of the project cost when full compliance would
overwhelm the job. Every tenant improvement quietly re-opens the accessibility question.</p>

<h2>The uncomfortable middle</h2>
<p>So the 1955 building sits in the worst spot: built with zero accessibility, never
&ldquo;forced&rdquo; to renovate, but carrying a live legal duty the whole time &mdash; and
presenting, to a practised eye, the richest set of barriers on the block. The plaintiff who
walks in is not confused about any of this. The owner usually is.</p>

<h2>What a CASp inspection does for an old building</h2>
<p>This is the exact situation the CASp program was designed for. The inspector determines
<b>which standards actually apply to your building given its age and permit history</b>
&mdash; that determination is itself part of the certification &mdash; then hands you the
statement the statute requires: you are in violation of this, this and this; here is the
itemised list; here is the schedule to fix it (Civil Code &sect;55.53). Work the schedule
and the law treats you as the owner who is fixing things &mdash; qualified-defendant status,
a possible 90-day stay, reduced damages tiers &mdash; instead of the owner who never
looked. <a href="/samples/casp-report.html">Here is what that report looks like.</a></p>
""",
    },
    {
        "slug": "certificate-of-occupancy-is-not-a-defense",
        "title": "Brand-new building, signed off last month? You can still be in violation",
        "teaser": "The building department approved it, the certificate of occupancy is on the "
                  "wall, and the store is already out of compliance. It happens constantly, "
                  "and no &mdash; you cannot sue the building department.",
        "cat": "access", "cat_label": "Accessibility",
        "date": "July 30, 2026", "read": "6 min",
        "img": "plaza-ramp",
        "body": """
<p>Owners of older buildings at least suspect they have a problem. Owners of brand-new
buildings are frequently the most exposed people in the room, because they are certain they
don't.</p>

<h2>How a new building opens in violation</h2>
<p>The list of accessibility obligations in the California Building Code's Chapter 11B is
enormous &mdash; hundreds of dimensional requirements across parking, routes, doors,
plumbing fixtures, counters, signage and reach ranges. A municipal building inspector
checking your project is working the whole code at once: structural, electrical, mechanical,
fire, energy <i>and</i> access, on a schedule, across every active project in the
jurisdiction. They are conscientious people. They still do not catch everything, and the
final walk was never a promise that they had.</p>

<p>So the certificate of occupancy gets signed, the store opens, and it is sitting there
with an entry door adjusted to twice the allowed opening force, a threshold a quarter-inch
too proud, a mirror an inch too high, a point-of-sale counter with no 36-inch section. Real
examples, all of them &mdash; from buildings months old.</p>

<h2>Why you cannot pass the blame</h2>
<p>Two hard truths. First, <b>the certificate of occupancy is not a compliance defense.</b>
The duty to provide access belongs to the business and the property owner, not to the
inspector who signed the final. A plaintiff sues you, not the city, and your permit file is
not an answer to a tape measure.</p>

<p>Second, <b>you cannot sue the building department for missing it.</b> California
Government Code &sect;818.6 gives public entities immunity for failures to inspect and for
inadequate or negligent inspections. That immunity is absolute and it is old law. The
inspector's signature transferred nothing to the city; the exposure stayed with you the
whole time.</p>

<h2>The one real advantage a new building has</h2>
<p>Here is what the new-building owner <i>does</i> get: facilities built under permits
issued on or after 1 January 2008 can qualify for the reduced $1,000 statutory-damages tier
when violations are corrected within 60 days of a complaint (Civil Code &sect;55.56) &mdash;
the law assumes newer construction was trying. Pair that with a CASp inspection done before
anyone files and you hold close to the strongest legal position an owner can have.</p>

<h2>The takeaway</h2>
<p>New or old, the pattern is identical: the only inspection that changes your legal
position is the one done by a Certified Access Specialist, on your initiative, before a
claim exists. A CASp walks your months-old building the way a plaintiff's expert would
&mdash; and hands the findings to you instead. <a href="/pricing.html">The price is
published.</a></p>
""",
    },
    {
        "slug": "ten-minute-vulnerability-walk",
        "title": "The ten-minute walk that tells you how vulnerable you are",
        "teaser": "You cannot self-certify compliance &mdash; but you can absolutely spot the "
                  "barriers a serial plaintiff would spot. Take this walk before they do.",
        "cat": "access", "cat_label": "Accessibility",
        "date": "July 22, 2026", "read": "7 min",
        "img": "parking-stalls",
        "body": """
<p>This walk will not make you compliant and it is not an inspection &mdash; the real
dimensional rules run to hundreds of entries and turn on your building's age and permit
history. What it will do is tell you, in ten minutes, whether your property has the kind of
visible-from-the-street barriers that get businesses picked. Walk it like a stranger in a
wheelchair. Better: walk it like someone paid to find problems, because those people exist
and <a href="/casp.html#numbers">they are busy</a>.</p>

<h2>1. Start across the street</h2>
<p>Can you see an accessible parking stall with an access aisle whose paint is actually
visible? Is there a van stall with the wider aisle? Is the signage up &mdash; including the
$250-fine placard California requires? Faded striping is one of the most common findings in
the state and it is visible from a car window, which is exactly how many claims begin.</p>

<h2>2. Park in the accessible stall</h2>
<p>Set a level app on the stall if you like: anything much over a 2% slope in any direction
is a finding. Now roll an imaginary chair from the stall to your front door. Every step, every
abrupt level change over half an inch, every stretch of route pinched below three feet by a
sign or a display is a barrier.</p>

<h2>3. The front door</h2>
<p>Thresholds over half an inch. Door hardware that requires a twisting grip. And the one
nobody checks: <b>opening force</b> &mdash; an interior door should open with about five
pounds of pressure, and a badly adjusted closer routinely doubles or triples that. A $10
door-pressure gauge is the cheapest pre-inspection you will ever run.</p>

<h2>4. Inside</h2>
<p>Aisles: a wheelchair needs 36 inches, continuously &mdash; watch for the merchandising
that crept into the route. Sales counter: there should be a lowered section around 34 inches
with clear floor space in front of it. If a customer in a chair would pay at armpit height,
that is a finding with your name on it.</p>

<h2>5. The restroom</h2>
<p>If the public can use it, it is in scope. Grab bars present, at the right heights (side
bar 33&ndash;36 inches). Clear space to actually turn a chair. Pipes under the lavatory
wrapped. Mirror and dispensers low enough to use. Restrooms produce more findings per square
foot than any other space in a commercial building.</p>

<h2>What to do with what you find</h2>
<p>If this walk turned up nothing, good &mdash; you are ahead of most, and an inspection
will likely be short. If it turned up three or four items, understand what that means: the
things you could see in ten minutes are the things anyone can see. The correct next step is
not quiet panic and not a weekend of guesswork &mdash; it is a <a href="/casp.html">CASp
inspection</a> that determines which standards apply to your building, measures everything,
and puts the fixes on a schedule the courts recognise. That schedule is the difference
between an owner with a plan and a defendant with a problem.</p>
""",
    },
    {
        "slug": "who-actually-files-these-lawsuits",
        "title": "Who actually files these lawsuits (the numbers will annoy you)",
        "teaser": "It is not a wave of aggrieved customers. It is a small, professional, "
                  "extremely productive group of plaintiffs and firms &mdash; and the state "
                  "publishes the receipts.",
        "cat": "access", "cat_label": "Accessibility",
        "date": "July 15, 2026", "read": "5 min",
        "img": "tactile-pad",
        "body": """
<p>When owners imagine an accessibility lawsuit, they imagine a wronged customer. The data
describes something else: a compact industry. Knowing how it actually works is the difference
between vague worry and a rational plan.</p>

<h2>The concentration is the story</h2>
<p>In 2025, plaintiffs filed <b>3,252 federal ADA Title III lawsuits in California</b> &mdash;
the most of any state, around 271 a month. In 2024, a single plaintiff organisation filed
<b>2,598</b> of that year's suits by itself. And of all the demand letters and complaints
reported to the California Commission on Disability Access in 2024, <b>95.8% came from just
ten law firms</b> &mdash; one firm alone accounted for roughly 41%. These are not our
estimates; attorneys are required by Civil Code &sect;55.32 to send copies of demand letters
to the Commission, which tabulates them quarterly. <a href="/casp.html#numbers">Sources
here.</a></p>

<h2>How the targeting works</h2>
<p>Parking lots are legible from the street and, increasingly, from satellite and street-view
imagery: stall counts, striping, van aisles, ramps and slopes photograph well. Entrances and
counters take one short visit. A practised filer does not need to find a sympathetic
disaster; they need to find one measurable barrier, because statutory damages are set by
statute &mdash; $4,000 minimum per occasion &mdash; and the attorney-fee award makes modest
cases worth running at volume.</p>

<h2>Two wrong conclusions to avoid</h2>
<p>First: <i>&ldquo;these suits are frivolous.&rdquo;</i> Usually not, and that is the
problem &mdash; the barrier named in the complaint is typically real and measurable. The
industry is opportunistic; the violations are genuine. Judges know the difference, which is
why the defence of &ldquo;but everyone does it&rdquo; goes nowhere.</p>

<p>Second: <i>&ldquo;I'm small, they won't bother.&rdquo;</i> The volume numbers say
otherwise. Small retail, restaurants and strip-mall tenants are the core of the docket
precisely because they are plentiful, visibly imperfect, and motivated to settle fast.</p>

<h2>The rational response</h2>
<p>You cannot control who drives past your parking lot. You can control which procedural
category you are in when they do. A CASp inspection done <b>before</b> any claim exists is
what California's own CRASCA statute offers as the escape: qualified-defendant status, the
possibility of a 90-day stay and an early evaluation conference, reduced damages tiers, and
&mdash; more practically &mdash; a property that stops being an easy pick, because the easy
findings got fixed on your schedule instead of theirs.</p>
""",
    },
    {
        "slug": "crasca-the-deal-california-is-offering",
        "title": "CRASCA: the deal California is offering every business owner",
        "teaser": "In 2008 the state looked at the lawsuit machine and built an off-ramp. "
                  "Eighteen years later, most owners still have never heard its name.",
        "cat": "access", "cat_label": "Accessibility",
        "date": "July 8, 2026", "read": "5 min",
        "img": "handrail",
        "body": """
<p>Google &ldquo;CRASCA&rdquo; and you will find the Construction-Related Accessibility
Standards Compliance Act &mdash; SB 1608, passed in 2008, now living at Civil Code
&sect;&sect;55.51&ndash;55.545. It is the least famous law that should matter most to a
California business owner, because it is the state saying, in statute: <b>we would rather
help you comply than watch you get sued.</b></p>

<h2>The bargain, in one paragraph</h2>
<p>The state certifies a class of specialists &mdash; Certified Access Specialists, CASp
&mdash; trained and examined on exactly one question: does this property meet the
construction-related accessibility standards that apply to it? Hire one <b>before anyone
files</b>, receive the report and its schedule of corrections, and the courts treat you as a
<b>qualified defendant</b>: you may apply for a 90-day stay of proceedings and an early
evaluation conference (&sect;55.54), and minimum statutory damages can fall from $4,000
toward $1,000 per occasion when corrections land within the statutory windows
(&sect;55.56). Small businesses get further protection still &mdash; a qualifying business
of 50 or fewer employees can take a 120-day grace period on the violations a CASp report
identifies.</p>

<h2>&ldquo;Get out of jail free&rdquo; &mdash; almost</h2>
<p>Owners like to call the CASp report a get-out-of-jail-free card. The honest version:
it is a <b>stay-out-of-the-worst-of-it</b> card, and the fine print is friendly but firm.
The protections attach only when the inspection, the report and the schedule <b>pre-date
the claim</b> &mdash; you cannot buy the shield after the arrow lands. And the shield
assumes you actually work the schedule; a report filed in a drawer protects the drawer.</p>

<h2>Why the state built this</h2>
<p>By the mid-2000s California had the nation's most generous disability damages statute and
its most productive filing industry, and small businesses were settling cases they could
have fixed for less than the settlement. CRASCA's design is candid about all of it: keep the
civil right fully intact, keep the damages for owners who ignore it, and give the owner who
engages an expert and fixes things a visibly better path. The legislature has reinforced the
same idea since &mdash; the reduced-damages tiers, the small-business provisions, the
demand-letter reporting that lets the state watch the filing industry it is trying to
outgrow.</p>

<h2>Eighteen years on</h2>
<p>The program works exactly as designed for the owners who know it exists. That is the
catch: most don't, and the filing statistics are the measure of the gap. Reading this puts
you in the smaller, better-informed group. The next step is the one the statute was built
around: <a href="/book.html">an inspection on your initiative</a>, a written schedule, and
the state's bargain working for you instead of around you.</p>
""",
    },
]


# ------------------------------------------------------------------ helpers

def _card(a, big=False):
    return ('<a class="card svc post-card" href="/blog/%s.html">'
            '<div class="svc-img">%s</div>'
            '<div class="svc-body"><span class="svc-tag">%s</span>'
            '<h3>%s</h3><p>%s</p>'
            '<span class="post-meta">%s &middot; %s read</span></div></a>'
            % (a["slug"], img(a["img"], ""), a["cat_label"], a["title"], a["teaser"],
               a["date"], a["read"]))


# ------------------------------------------------------------------- builds

def build_index(write):
    cards = "".join(_card(a) for a in ARTICLES)
    body = phead(
        "Field notes",
        "Plain-English reading on California accessibility and balcony law, written by the "
        "inspector &mdash; the things owners usually learn from a demand letter, offered "
        "earlier and cheaper.",
        [("Home", "/index.html"), ("Field notes", None)]) + """
<section>
 <div class="wrap">
  <div class="grid g3">{cards}</div>
  <div class="note note-a" style="margin-top:2.4rem">
   <b>The theme running through all of it.</b>
   It is good that you are here reading rather than opening a demand letter. While you are:
   full and equal access is a civil right in California, barriers are violations whether or
   not anyone intended them, people are actively looking for them &mdash; and the state
   built a program (CRASCA) whose entire purpose is helping owners fix things with an
   expert before that happens.
  </div>
 </div>
</section>
{cta}
""".format(cards=cards,
           cta=cta("Read enough to be worried?",
                   "Good — that is the useful kind. A fifteen-minute call tells you whether "
                   "the worry is warranted, and the inspection price is published."))
    write("blog.html", head(
        "Field Notes | Accessibility &amp; Balcony Law | Inspector Group California",
        "Plain-English articles on California accessibility law: the civil-rights framing, "
        "the grandfathering myth, why a certificate of occupancy is no defense, who files "
        "the lawsuits, and the CRASCA bargain.",
        "/blog.html") + body + foot())


def build_articles(write):
    for i, a in enumerate(ARTICLES):
        others = [x for j, x in enumerate(ARTICLES) if j != i][:3]
        related = "".join(_card(x) for x in others)
        body = phead(
            a["title"], a["teaser"],
            [("Home", "/index.html"), ("Field notes", "/blog.html"), ("Article", None)]) + """
<section>
 <div class="wrap narrow">
  <div class="post-byline">
   {avatar}
   <div><b>Robert Lehman</b><span>Founder, Inspector Group California &middot; {date} &middot; {read} read</span></div>
  </div>
  <article class="post-body">
  {content}
  </article>
  <div class="note" style="margin-top:2.4rem">
   <b>This is orientation, not legal advice.</b>
   Statutes are summarised and cited so you can check them; how they apply to your property
   depends on facts we have not seen. For an answer about your building,
   <a href="/book.html">book the inspection</a> or <a href="/contact.html">start with a
   call</a> &mdash; and for anything in active litigation, retain California counsel.
  </div>
 </div>
</section>

<section class="sec-paper">
 <div class="wrap">
  <div class="sec-head"><h2>Keep reading</h2></div>
  <div class="grid g3">{related}</div>
 </div>
</section>
{cta}
""".format(avatar=img("robert-lehman", "Robert Lehman", cls="post-avatar"),
           date=a["date"], read=a["read"], content=a["body"], related=related,
           cta=cta())
        write("blog/%s.html" % a["slug"], head(
            "%s | Field Notes | Inspector Group California" % a["title"].replace("&mdash;", "—"),
            a["teaser"].replace("&mdash;", "—").replace("&ldquo;", '"').replace("&rdquo;", '"'),
            "/blog/%s.html" % a["slug"]) + body + foot())


def build(write):
    build_index(write)
    build_articles(write)
