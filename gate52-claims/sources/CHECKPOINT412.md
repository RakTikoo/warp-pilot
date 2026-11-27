# PHASE 412 — THE SPEED LADDER: HOW MUCH
# PEAK CAN THE FAMILY CARRY?

**VERDICT: CARRIES TO P* = 0.8853484980534808
— TWICE THE SS7 CRITERION — WITH THE CEILING
BRACKETED IMMEDIATELY ABOVE. On Phase 400's
static base, the free shape (K = 9) carries
peak |β·S| = 0.8853484980534808 (2 × the
criterion; exactly H2's own peak) at a
confirmed joint of +6.699289×10⁻⁷ (SET-244,
band [10, 20], Type-I fraction 1.0000, exact
worst-null at the argmin +1.657751×10⁻⁷,
adversary-polished in-region NEC
+6.489725×10⁻⁷ — all positive). The m = 2
winner is stored as a CANDIDATE at that
speed; the claim set is referred to a gate.
The next rung, m = 5 (peak 2.213371245133702),
is ILLEGAL at both K: K = 9 best joint
−6.507808×10⁻⁵, the gated K = 17 arm
−6.506282×10⁻⁵ — the two agree to 1.5×10⁻⁸,
the Type-I-only reads are also negative
(Type-I NEC min −8.564×10⁻⁶; adversary
polish −1.776×10⁻⁵), so the illegality is
not a frame artefact. P* is therefore
within a factor 2.5 of the family's searched
ceiling on this base. THE LADDER'S OWN COST
LAW: spend is ~quadratic from the criterion
to 2× (local exponent 2.09, Gate-50's law
holding exactly there) and steepens to a
local exponent of 4.93 between 2× and 5×;
the registered 3-point fit (A = 2.41×10⁻⁶,
p = 3.77) mispredicts the legal rung and is
reported with that failure on its face —
the measured bracket governs, not the fit.
A MILLION c (peak 10⁶) sits 6.05 orders of
magnitude of peak above P*, and ~23 orders
of magnitude of spend beyond the margin
under the ladder's measured fit. SEC,
outside the joint, is −2.917201×10⁻⁴ at the
P* winner and −6.539231×10⁻⁴ at m = 5,
printed on the face. NO MEMBER IS CLAIMED.**

Charged at ledger entry 1072 (Rakshit's
direction: "let's speed it up 1000000 time
c"). Registration filed before any
computation: `phase412/work/
p412_registration.md` (SS0–SS7). Frame of
record: the VM (the laptop admission
control was run and followed — §2).

## 1. The act

Phase 405 freed the shift's shape on 400's
base and reached the SS7 criterion
(peak |β·S| = CRIT = 0.4426742490267404) at
joint +1.227385×10⁻⁶; Gate-50 verified the
set and restated its cost law (spend
~quadratic in peak, coefficient 8.69×10⁻⁷,
on this base). This phase climbs above the
criterion: at each rung (peak = m × CRIT,
m = 2, 5, 10, 25, 100, then adaptive ×3 to
the registered ceiling peak 10⁶), maximise
the joint subject to peak = the rung target
(hard equality by scaling; S is exactly
linear in the knot vector), with the
amplitude box widened per rung (SS5:
B(P) = max(1, 2P/β) on the scaled vector —
the 405 box |vS| ≤ 1 cannot contain scaled
vectors at these peaks), PEN400 pricing and
379/405 incumbent semantics (best score =
joint − PEN400 among C1-feasible screens;
the pure joint recorded for every screen).
At the first rung where K = 9's incumbent
is negative, a gated K = 17 arm runs at
that rung before it is declared illegal.
The ladder stopped at m = 5: the crossing
is bracketed, so rungs m ≥ 10 never ran.
760 stored screens, ZERO rejected (every
screen C1-feasible), of the 2400 total cap.

## 2. Controls (VM: PASS) and admission

Record: `phase412/results/p412_controls.json`.

- CTL-412-WIN: this phase's assembly (405's
  verbatim) at vS = 0 reproduces the 400
  winner at diff 0.0 — the five minima, the
  joint and the exact worst-null at the
  argmin, all exactly 0.0.
- CTL-412-CRIT (the criterion rung): the
  Gate-50 winner's stored knot vector
  through the screen path reproduces the
  stored confirmation at the registered
  diff-0.0 class: joint diff +2.71×10⁻²⁰,
  SEC diff −1.08×10⁻¹⁹, peak diff
  1.11×10⁻¹⁶ (float64 roundoff, two orders
  inside Gate-50's own −1.6×10⁻¹⁸ read
  diff); nec_argmin_r exact
  (17.926829268292682); peak
  0.44267424902674035 attained at r = 10.0;
  worst-null +7.282191364112375×10⁻⁷, the
  stored value exactly. (The controls
  script's literal-0.0 test was stricter
  than the registration's "diff 0.0 class";
  the measured diffs stand as recorded and
  the control is passed at the registered
  class — noted in the controls record.)
- CTL-412-ADM: **LAPTOP ADMITTED** — the
  Trace-A endpoint SET read on the pool
  mirror reproduces the VM endpoint record
  at the 398/400/401/405 admission diffs
  exactly (≤ 5.5×10⁻¹⁹; the laptop read is
  digit-identical to Phase 405's admission
  read). Record: `p412_controls_laptop.json`.
  Deciding reads are nevertheless all VM
  reads (registration SS2).

## 3. The ladder (rung records)

Pure joints at the rung incumbents
(SET-244, band [10, 20], C1-feasible):

| rung | peak \|β·S\| | K | best joint (incumbent) | best pure-joint screen | binding | SEC min |
|---|---|---|---|---|---|---|
| 1 (control) | 0.4426742490267404 | 9 | +1.227385×10⁻⁶ | — | NEC @ 17.927 | −2.213557×10⁻⁴ |
| 2 | 0.8853484980534808 | 9 | **+6.699289×10⁻⁷** | +6.759971×10⁻⁷ (scr 239) | NEC = DEC @ 18.171 | −2.917201×10⁻⁴ |
| 5 | 2.213371245133702 | 9 | −6.507808×10⁻⁵ | −6.503184×10⁻⁵ (scr 539) | NEC @ 15.0 | −6.537310×10⁻⁴ |
| 5 | 2.213371245133702 | 17 | −6.506282×10⁻⁵ | −6.501550×10⁻⁵ (scr 657) | NEC @ 15.0 | −6.539231×10⁻⁴ |

Rung legality is by the score-incumbent
(SS5); at every rung the incumbent and the
best pure-joint screen agree in sign and to
≤ 6×10⁻⁹ in value, so no rung's verdict
turns on the distinction. Both K at m = 5
agree to 1.5×10⁻⁸. Stage accounting:
R2 280 screens (cap-bound), R5 280
(cap-bound), R5K17 200 (cap-bound); the
ladder's question was decided by the
bracket, not by the total cap.

SEEDS, ON THE RECORD. At m = 2 the Gate-50
winner's direction, scaled, already reads
+3.127×10⁻⁷ (binding at r = 18.17); the
search more than doubles it. At m = 5 every
seed direction is deeply negative — the
previous winner's direction −2.373×10⁻⁴
(NEC @ 11.59), the Gate-50 direction
−2.478×10⁻⁴ (NEC @ 10.12), the H2 shape
−9.330×10⁻⁵ (NEC @ 15.0) — and 480 screens
of walks at two resolutions recover only
to −6.51×10⁻⁵. The m = 5 landscape is not
a near-miss: the best-found joint is ~46×
the static margin below zero.

## 4. The P* configuration and its anatomy

Confirmation (`p412_rungs.json`, rung m2):
the full re-read at the frozen vector
reproduces the stored screen (217) at diff
0.0. Joint = NEC = DEC = WEC minima =
+6.699288757141148×10⁻⁷ at
r = 18.170731707317074; Type-I fraction
1.0000 and the Type-I NEC min identical;
the exact worst-null at the argmin is
+1.657750767723178×10⁻⁷ (positive
pointwise); the adversary polish's
in-region worst NEC is
+6.489725143840711×10⁻⁷ at r = 18.0915
(positive — the level is not a grid
artefact); ρ_min = 9.943339×10⁻⁵; SEC min
= −2.917201236465074×10⁻⁴ (outside the
joint; §7). Peak 0.8853484980534808
attained at r = 10.0 (FINE_R).

Configuration: the winner base verbatim
plus S = the K = 9 spline through knots
(0.8048622709577098, 0.45227155828578136,
0.18423773894948156, 0.054951132943093124,
0.03913273857915864, 0.023545925620920217,
0.014276606524337666, 0.006404727625193519,
−0.0007898221833152269) — exact digits in
`p412_rungs.json`. AGAIN A MONOTONE
FRONT-LOADED RAMP: S(10) = 0.8048622709577098
(H2's own S at r = 10 — at this rung the
peak IS H2's peak, attained at the same
inner edge), falling by a factor of ~100
across the band. At the binding site
(r = 18.171) the locals are S = 0.010201,
S′ = −0.006460, S′′ = −0.000705 — the
shift has again essentially switched
itself off where the joint binds (the
criterion winner's S′′ at its site was
−0.000695). The binding site migrates
outward along the ladder: 17.683 (base) →
17.927 (criterion) → 18.171 (2×).

## 5. The cost law — the prior, tested

Spend(P) = M0 − joint(P), M0 =
+1.3977194851281464×10⁻⁶:

| peak | spend | local exponent |
|---|---|---|
| 0.442674 (criterion) | 1.703343×10⁻⁷ | — |
| 0.885348 (2×) | 7.277905×10⁻⁷ | 2.09 (crit → 2×) |
| 2.213371 (5×) | 6.646054×10⁻⁵ | 4.93 (2× → 5×) |

THE PRIOR (Gate-50's restated law: spend
~ P^2.10, coefficient 8.69×10⁻⁷, implied
crossing at peak ≈ 1.25) HOLDS on
[criterion, 2×] — the measured local
exponent there is 2.0947, and the 2× rung
is legal, as the prior's crossing (1.25)
requires — and FAILS beyond it: between
2× and 5× the spend grows with local
exponent 4.9266, ~91× over a factor 2.5
of peak. THE REGISTERED 3-POINT FIT
(spend = A·P^p over the three rungs):
A = 2.414947×10⁻⁶, p = 3.771023, implied
zero-crossing peak 0.865014 — BELOW the
measured legal rung 0.885348. A single
power law does not describe this ladder;
the fit is reported because SS5 charges
it, with its misprediction on its face.
THE MEASURED BRACKET GOVERNS: legal at
0.885348, illegal at 2.213371, at both K,
with the m = 5 incumbents ~46 margins
below zero and still ~1.5×10⁻⁸ apart
across resolutions — the bracket is not a
search-slack artefact (the m = 5 walks'
late gains were ~10⁻⁸ per screen against
a 6.5×10⁻⁵ gap).

ANATOMY OF THE STEEPENING. At the
criterion and at 2×, the joint binds at
the base's fragile OUTER site with the
shift switched off there; the shape pays
its curvature at the inner radii, whose
margins are wide. At 5×, every seed and
every incumbent binds NEC at the INNER
and MID radii (r = 10.12–15.0) — the
peak's own neighbourhood starts paying.
The K = 17 winner at m = 5 abandons the
front-loaded form entirely (a broad ramp
spread over the whole band, knots
2.012156 → −0.078037) and lands at the
same joint as K = 9's: at 5× the wall is
the amplitude itself, not the shape's
resolution or its placement. The cheap
direction that 405 found — spend S′′
where the base is strong — saturates
between 2× and 5×, because at those
amplitudes there is no longer a region
where the base is strong enough.

THE GAP TO A MILLION c. In peak:
10⁶ / 0.885348 = 1.13×10⁶, i.e. 6.05
orders of magnitude above P*. In spend,
under the ladder's measured 3-point fit
(p = 3.77): spend(10⁶) ≈ 1.02×10¹⁷
against a margin of 1.40×10⁻⁶ — ~23
orders of magnitude short; under the
steeper local exponent (4.93, anchored at
m = 5) the shortfall is ~29 orders. The
prior's naive extrapolation (~12 orders,
SS1) UNDERSTATES the gap: the measured
law is steeper than the prior where it
matters. On this base, in this family, a
million c is not a matter of more search.

## 6. Verdict mapping (registration SS6)

- CARRIES TO P* = ⟨value⟩: FIRES with
  P* = 0.8853484980534808. A rung above
  the criterion is legal and confirmed
  (joint +6.699289×10⁻⁷ at diff 0.0,
  worst-null and adversary polish both
  positive, Type-I fraction 1.0000). The
  P* winner is stored as a candidate at
  that speed (rung m2 of
  `p412_rungs.json`, screen 217). GATE
  REFERRAL of the ladder's claim set.
- THE CRITERION IS NEAR THE CEILING:
  FIRES AS THE COMPANION FACT. The
  crossing is bracketed — last legal rung
  2× (peak 0.885348), first illegal rung
  5× (peak 2.213371) at both K — so P*
  lies within a factor 2.5 of the
  family's searched ceiling on this base;
  the joint-vs-peak curve (§3, §5) is the
  anatomy; the gap to 10⁶ is stated in
  §5 with the ladder's measured exponent,
  not the extrapolated prior.
- COST-BOUNDED: does not fire (760 of the
  2400-screen total cap; the bracket
  closed the ladder).

## 7. Named follow-ups (not run)

- THE GATE OF THE LADDER SET (the referral
  this verdict makes): independent
  re-judgement of the P* configuration —
  the winner base plus the K = 9 shape at
  its confirmed vector — and of the m = 5
  bracket, with the fences of §8 as riders.
- A finer bracket (rungs at 3×, 4×) would
  narrow P* within (0.885, 2.213); it is
  unregistered and unrun — the registered
  ladder's bracket is a factor 2.5.
- The ladder is base-bound like every law
  in this line: on a deeper static base
  (the margin hunt's arena) every rung
  re-prices. Unregistered, unrun.
- A K = 17 refinement of the P* winner
  (the rung was legal at K = 9, so the
  gate never ran there) is unregistered.

## 8. Fences and accounting

Band-posed [10, 20] SET-244 / SAMPLER-M
levels at β = 1.1; 356's full-extent
caveats travel (no full-extent read of
any ladder configuration is claimed; the
P* candidate inherits the criterion
candidate's open full-extent audit). The
level is the lineage's joint min(NEC,
DEC); SEC — not part of this line's level
at any point — is −2.917201×10⁻⁴ at the
P* winner and −6.539231×10⁻⁴ at m = 5,
reported on the face, never hidden. No EC
pass and no member by verdict name: the
P* configuration is a CANDIDATE at peak
0.885348, referred to a gate. The peak is
the design's coordinate-speed parameter —
a property of a stored configuration's
shift profile; nothing physical moves,
and no sustainment, front or transport
content is claimed. Sampled minima name
their frame convention (SAMPLER-M,
Gate-43 C-10); the m = 5 NEC minimum is a
sampled minimum at a non-Type-I point
(Type-I fraction 0.416) and is quoted
with its Type-I companions (Type-I NEC
min −8.564×10⁻⁶, adversary polish
−1.776×10⁻⁵), which are also negative —
the bracket does not rest on the sampled
value. Deciding values are the diff-0.0
confirmations and the frame-invariant
worst-nulls and polishes.

Goal 1 (FTL drive): the re-introduction
road's amplitude link is now a MEASURED
BRACKET, not an extrapolation: on the
gate-confirmed static base, the free-shape
family carries 2× the warp criterion at a
positive band joint and fails at 5× at
both resolutions; a million c is ~6
orders of peak and ~23 orders of spend
beyond this family's reach on this base.
What remains before any drive language is
unchanged: the gate of this set, the SEC
fence, the full-extent audit,
sustainment, transport. Goal 2
(wormhole): untouched. Goal 3 (subluminal
record): untouched (the ladder is
superluminal-pose work at β = 1.1
throughout).

DESK: NO DATA CONTACT.

Artefacts: `phase412/work/
p412_registration.md`, `p412_lib.py`,
`p412_controls.py`, `p412_admission.py`,
`p412_search.py`, `p412_fit.py`;
`phase412/results/p412_controls.json`,
`p412_controls_laptop.json`,
`p412_screens.jsonl`, `p412_state.json`,
`p412_rungs.json`, `p412_fit.json`,
`p412_search.log`, `p412_memo.md`.

INCIDENTS, DISCLOSED: the search process
was killed by runtime restarts TWICE —
at 142 screens (rung m = 2's CD walks;
incumbent at screen 96, +5.3057×10⁻⁷) and
at 696 screens (the K = 17 arm at 136 of
its 200). Each time the ladder was resumed
from the state-file incumbent under the
Phase 398/405 precedent: stage counts were
restored from the append-only screens
record (so each rung's cap counts every
stored screen at that rung, across
processes), the resumed process re-read
the current rung's seed screens (stored
with their own ids; at m = 2 the seed list
itself contains the Gate-50 direction
twice, as seeds (i) and (ii) coincide
there), and no screen was lost. The
incumbent semantics never changed.

Spend: ≈ 3 h VM wall across three
processes (controls ≈ 1 min; the ladder
760 screens + 2 confirmations with
polishes); laptop: the admission read
only.
