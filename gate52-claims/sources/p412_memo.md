# PHASE 412 MEMO — THE SPEED LADDER: HOW
# MUCH PEAK CAN THE FAMILY CARRY?

VERDICT: CARRIES TO P* = 0.8853484980534808
(2 × the SS7 criterion), GATE REFERRAL —
with the ceiling bracketed immediately
above at 5×.

Phase 405 carried the SS7 warp criterion
(peak |β·S| = 0.4426742490267404) on Phase
400's static base at joint +1.227385×10⁻⁶,
and Gate-50 verified the set, restating
its cost law: spend ~quadratic in peak
(coefficient 8.69×10⁻⁷ per peak²) on this
base. Rakshit's direction — "speed it up
1000000 time c" — asks how far the peak,
this family's speed variable, actually
goes. This phase climbed the ladder:
rungs at peak = {2, 5, 10, 25, 100} × the
criterion with adaptive continuation to a
registered ceiling of peak 10⁶, the joint
maximised at each rung subject to peak =
the rung target, the amplitude box widened
per rung, a gated K = 17 arm at the first
negative rung. The ladder stopped at the
second rung: the crossing is bracketed.

| rung | peak \|β·S\| | best joint | verdict |
|---|---|---|---|
| 1× (control) | 0.442674 | +1.227385×10⁻⁶ | legal (Gate-50) |
| 2× | 0.885348 | +6.699289×10⁻⁷ | **LEGAL — P\*** |
| 5× | 2.213371 | −6.506282×10⁻⁵ | illegal (K = 9 and K = 17) |

THE P* CONFIGURATION (rung m = 2 winner,
screen 217; confirmation at diff 0.0):
joint = NEC = DEC = WEC = +6.699289×10⁻⁷
at r = 18.171, Type-I fraction 1.0000,
exact worst-null +1.657751×10⁻⁷, adversary
polish +6.489725×10⁻⁷ — all positive. Its
shape is the criterion winner's anatomy
again: a monotone front-loaded ramp,
S(10) = 0.804862 (H2's own value there —
at this rung the peak IS H2's peak,
attained at the same inner edge r = 10),
falling ~100× across the band, with
S′′ = −0.000705 at the binding site — the
shift switched off where the joint binds.
SEC at the winner is −2.917201×10⁻⁴, on
the face (SEC is outside the lineage's
joint). The configuration is a CANDIDATE
at peak 0.885348, referred to a gate; no
member is claimed.

THE COST LAW, MEASURED (the prior,
tested). Spend = margin − joint:
1.703×10⁻⁷ at the criterion, 7.278×10⁻⁷
at 2×, 6.646×10⁻⁵ at 5×. Gate-50's
quadratic law holds exactly from the
criterion to 2× (local exponent 2.09 vs
the law's 2.10) and fails beyond: the
local exponent from 2× to 5× is 4.93.
The registered 3-point fit (A =
2.41×10⁻⁶, p = 3.77) implies a crossing
at peak 0.865 — below the rung measured
legal at 0.885 — so a single power law
does not describe this ladder; the
measured bracket governs. The anatomy of
the steepening: at the criterion and 2×
the joint binds at the fragile outer site
with the shift off there, the curvature
paid at the wide-margin inner radii; at
5× every seed and incumbent binds at the
inner/mid radii (r = 10.1–15.0) — the
peak's own neighbourhood starts paying,
and the K = 17 winner abandons the
front-loaded form entirely (a broad
full-band ramp) yet lands at the same
joint as K = 9 (agreement 1.5×10⁻⁸). At
5× the wall is the amplitude itself.

A MILLION c, PRICED WITH THE MEASURED
LAW: peak 10⁶ is 6.05 orders of magnitude
above P*; the spend it would require
under the ladder's fitted law is
~1.0×10¹⁷ against the base's margin of
1.40×10⁻⁶ — ~23 orders of magnitude short
(~29 under the steeper local exponent).
The naive extrapolation of Gate-50's law
(~12 orders) understates the gap. On
this base, in this family, a million c
is not a matter of more search.

CONTROLS: the 400 winner reproduced at
diff 0.0 exactly (five minima, joint,
worst-null); the criterion rung
reproduces the Gate-50 winner at the
diff-0.0 class (joint diff +2.7×10⁻²⁰;
argmin and peak radius exact; worst-null
the stored value exactly). Laptop
ADMITTED at roundoff (the 398/400/401/405
diffs); deciding reads all VM. 760 stored
screens, zero rejected. TWO INCIDENTS,
DISCLOSED: runtime restarts killed the
search process at 142 and at 696 screens;
each time the ladder resumed from the
state-file incumbent under the Phase
398/405 precedent, stage counts restored
from the append-only record; no screen
was lost and the incumbent semantics
never changed.

FENCES: band [10, 20] reads at the home
pose (β = 1.1); 356's full-extent caveats
travel. The level is the joint
min(NEC, DEC); SEC is read at every rung
and printed (−2.917201×10⁻⁴ at P*,
−6.539231×10⁻⁴ at 5×), never hidden. The
m = 5 NEC minimum is a SAMPLER-M sampled
minimum at a non-Type-I point; its
Type-I companions (Type-I NEC min
−8.564×10⁻⁶, adversary polish
−1.776×10⁻⁵) are also negative, so the
bracket does not rest on it. The peak is
the design's coordinate-speed parameter;
nothing physical moves. No sustainment,
front or transport content. Three-goal
accounting: Goal 1 — the amplitude link
of the drive chain is now a measured
bracket (legal at 2× the criterion,
illegal at 5×, both resolutions) instead
of an extrapolation; the gate of this
set, the SEC fence, the full-extent
audit, sustainment and transport remain
the named unrun links. Goals 2 and 3
untouched.

DESK: NO DATA CONTACT — the programme's
own stored configurations, re-shaped and
re-read on its own instruments; no
external data of any kind.

Files: work/p412_registration.md,
work/p412_lib.py, work/p412_controls.py,
work/p412_admission.py, work/p412_search.py,
work/p412_fit.py; results/p412_controls.json,
results/p412_controls_laptop.json,
results/p412_screens.jsonl,
results/p412_state.json,
results/p412_rungs.json, results/p412_fit.json,
results/p412_search.log.
Spend: ≈ 3 h VM wall across three
processes; laptop: the admission read only.
