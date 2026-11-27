# GATE-47 — Independent re-judgement of the Phase 396 claim set, with the degeneracy note as a charged item

Charged at ledger entry 1020 (2026-11-26). Phase 396 claimed
that a third widening of the per-profile scaling box, seeded at
Phase 395's centre, climbed the diagonal ridge to a new centre
at (μ_S, μ_N, μ_M) = (0.4003528067864536, 1.9863455070489624,
6.715383396291902) on H2's total profiles, with band level
−7.431892×10⁻⁶ — and it carried, on its own face, a
pre-registered DEGENERACY NOTE: the centre's peak physical
shift is 40.0% of H2's, below the registered half-of-H2 flag,
so the gain is substantially purchased by shift removal and
the point is a scaling-family artefact candidate, not a
design improvement, until a gate rules otherwise. This gate
re-judges that claim set with fresh machinery only, every
deciding value reproduced independently on the VM frame of
record, and rules on the degeneracy note as a charged item
(claim (f)) on its own measurements.

## Verdict

- **(a) The new centre and its level −7.431892×10⁻⁶:
  SURVIVES** — as a scaling-surface level, with riders G47-E
  and G47-F attached wherever it is quoted. The gate's batch
  SET-244 read reproduces the stored joint at
  −7.431892169092337×10⁻⁶ (diff +1.6×10⁻¹⁹), the DEC minimum
  at diff −1.8×10⁻¹⁹, ρ_min at diff +2.4×10⁻¹⁸, and the
  Type-I count exactly (4756 of 6642). All five lineage
  controls reproduce at roundoff (§2).
- **(b) Pointwise survival: SURVIVES.** The exact worst-null
  at the centre's SET NEC argmin point reproduces at
  −8.706718841221368×10⁻⁶ (diff +1.9×10⁻¹⁹ vs stored).
  Riders G47-E and G47-F attach.
- **(c) The end-clamp rider: SURVIVES.** The clamped level
  reproduces at diff 0.0 (−7.644643599300465×10⁻⁶); clamp
  cost 2.127514×10⁻⁷ (gate, = stored to the digits shown);
  the clamped level remains above the anchor's unclamped
  level by +2.216521×10⁻⁵ and above L_stat(H2) by
  +1.865800×10⁻⁴ — both clamped margins survive. Riders
  G47-E and G47-F attach.
- **(d) The box claims: SURVIVE.** The stored record
  recounts exactly (336 reads, all feasible; 326 beating the
  anchor; worst DEC −2.0253148251802704×10⁻⁶; zero
  DEC-saturated reads under either saturation threshold);
  the worst-DEC read is independently re-read on gate
  machinery at diff −1.5×10⁻¹⁹ (Type-I); the diagonal trace
  re-reads strictly monotone at roundoff, its increments
  decaying mildly with last/first = 0.617 (§3).
- **(e) The box-edge disclosure: SURVIVES — and is issued
  as rider G47-E**, attached on the face of G47-A, G47-B
  and G47-C wherever the centre's level is quoted: the
  centre presses the registered μ_S lower edge
  (0.4003528067864536 vs 0.40, by 0.00035) and nears the
  μ_N upper edge (by 0.01365) — the third widening in a row
  whose centre arrived at the new μ_S edge. The centre is
  quotable only as the optimum of the registered box (§3).
- **(f) The degeneracy note: SURVIVES RESTATED — issued as
  G47-F.** The note's quotable consequence is UPHELD on the
  gate's own measurements: the centre is not quotable as a
  design improvement (peak shift 40.0% of H2's, below the
  pre-registered bar; shift removal alone buys 77% of the
  anchor→centre gain in the gate's one-factor attribution).
  Its mechanism is RESTATED: the purchase is approximately
  LINEAR in μ_S at the binding site, not the quadratic
  S′′-scaling the note's rationale implied — and the
  shift-free limit is not a trivial pass either, since the
  μ_S = 0 configuration at the centre's (μ_N, μ_M) still
  violates at −1.049934×10⁻⁶ in the (N, M) sector. The
  last centre on this line clearing the registered
  half-of-H2 peak-shift bar is Phase 395's centre. The
  asymptote question is referred, with its criterion
  stated, to Phase 397's degeneracy probe (§4).

Every level in this set remains negative. No EC pass, no
member, no drive or transport implication arises from
anything in this gate. Fence in §5.

## §1 Machinery and calibrations

Fresh gate machinery (`gate47/work/g47_lib.py`), written for
this gate alone; no phase code and no earlier gate code is
imported or reused for any deciding read. The registered
definitions are re-implemented from the records:

  * profiles: beta-profile shift, plateau lapse bump,
    ramped M, plus not-a-knot correction splines with
    constant extension outside [10, 20]; H2 = centre(1.15)
    of the A2 totals + K = 17 corrections; per-profile
    scaling S -> muS*S, N -> muN*N, M -> 1 + muM*(M - 1);
    the end-clamp zeroes the first/last knots of H2's
    three correction vectors before scaling.
  * tensor: the metric's first and second spatial
    derivatives derived SYMBOLICALLY with sympy in
    Cartesian coordinates (S, N, M as functions of
    r = √(x²+y²+z²); the radial-derivative nodes
    substituted by plain symbols and lambdified with
    cse), with the Christoffel and Ricci contractions
    carried out by the gate's own vectorised numpy
    assembly — a different organisation from the lineage's
    hand-derived radial formulas, Gate-43's loop
    contractions, and Gate-45's forward-mode AD jets.
    T = G / (8 pi), stationary.
  * gamma's value is assembled in the definition's
    association, delta_ij + ((M-1) n_i) n_j (the Gate-41
    C-8 / Gate-43 C-10 lesson).
  * frames/margins: Eulerian ADM frame (eigh triad);
    Hawking-Ellis eigenvalue margins at Type-I points,
    SAMPLER-M sampled margins (162 Fibonacci directions x
    velocities linspace(0, 0.95, 6)) at non-Type-I points;
    rho = Eulerian T_00.
  * SET-244 = 41 radial midpoint nodes on [10, 20]
    x 162 Fibonacci directions (6642 points).

float64 throughout. VM only. Scoping: the adversary-polish
depth was not re-run; controls are judged on the five
minima and the worst-nulls.

Calibrations:

  * Trivial limit (N ≡ 1, S ≡ 0, M ≡ 1): max|T| = 0.0
    exactly at the sample points.
  * FD cross-path (from-scratch 4th-order centred-FD
    Einstein tensor from the metric function alone,
    profile values only): at the centre's NEC argmin
    point, max|ΔT| over h = 0.1, 0.05, 0.025, 0.0125 runs
    2.12×10⁻⁶ → 2.03×10⁻⁷ → 1.52×10⁻¹¹ → 3.87×10⁻¹²
    (ΔThat 1.03×10⁻¹³ at the finest h); at the H2 NEC
    argmin control point, 1.58×10⁻⁶ → 9.82×10⁻⁷ →
    4.00×10⁻⁷ → 1.12×10⁻⁸ (ΔThat 3.46×10⁻⁹). Both trends
    decrease monotonically to agreement with the symbolic
    tensor; neither is a clean h⁴ line across the whole
    range, and the endpoint agreement is the deciding
    fact.
  * Stored bytes: the A2 K = 33 vectors agree between
    Phase 344's confirmation artefact and its state file
    at max|Δ| = 0.0, and the H2 K = 17 vectors agree
    between Phase 379's confirmation artefact and its
    state file at max|Δ| = 0.0 (all six vectors; C-0).
    Md5 registry in §6.

## §2 The centre, the controls, the pointwise read, the clamp — claims (a), (b), (c)

The gate's SET-244 batch reads (diffs vs stored):

| read | NEC | DEC | WEC | SEC | ρ |
|---|---|---|---|---|---|
| H2 (1,1,1) | −1.1×10⁻¹⁹ | −6.0×10⁻¹⁹ | +1.7×10⁻¹⁸ | +8.7×10⁻¹⁸ | −5.4×10⁻²⁰ |
| mixed centre | +4.9×10⁻¹⁹ | +1.0×10⁻¹⁸ | −3.3×10⁻¹⁸ | −6.5×10⁻¹⁸ | +1.4×10⁻¹⁹ |
| 393 seed | 0.0 | −9.6×10⁻¹⁹ | −4.4×10⁻¹⁸ | −4.3×10⁻¹⁹ | +3.9×10⁻¹⁹ |
| C394 | −4.1×10⁻¹⁹ | +2.4×10⁻¹⁹ | +1.6×10⁻¹⁹ | −7.8×10⁻¹⁸ | +1.3×10⁻¹⁸ |
| anchor (395) | −2.4×10⁻¹⁹ | −6.8×10⁻²⁰ | −1.7×10⁻¹⁸ | +1.0×10⁻¹⁸ | +3.7×10⁻¹⁹ |
| centre (396) | +1.6×10⁻¹⁹ | −1.8×10⁻¹⁹ | (= DEC, as stored) | −7.0×10⁻¹⁹ | +2.4×10⁻¹⁸ |

The largest |diff| anywhere in the table is 8.7×10⁻¹⁸
(H2 SEC). The centre's own values: NEC min
−7.431892169092337×10⁻⁶ at r = 16.46341463414634; DEC min
−1.097932392391424×10⁻⁶ at r = 18.902439024390244;
SEC min −3.391058851844148×10⁻⁴; ρ min
+9.858014400881535×10⁻⁵; Type-I count 4756 of 6642,
fraction diff 0.0. All argmin radii match the stored
radii exactly.

C-10 note: on the gate's machinery the NEC argmin point
is non-Type-I at all six main reads (so those NEC minima
are SAMPLER-M sampled values), while every DEC argmin
point is Type-I. Despite that, no sampled minimum in
reads 1–5 differs from its stored value by more than
~10⁻¹⁸: the C-10 frame-convention band (±3×10⁻⁶) is not
engaged by any deciding value in this gate. The one
C-10-bar comparison in the set — the clamped mixed
centre against Gate-43's independent value — sits at
9.2×10⁻¹⁹, far inside the band.

Pointwise (claim (b)): exact worst-nulls — centre
−8.706718841221368×10⁻⁶ (diff +1.9×10⁻¹⁹ vs stored
−8.706718841221561×10⁻⁶); anchor
−3.089621009567838×10⁻⁵ (diff −3.0×10⁻¹⁹); seed
−1.2477276305772507×10⁻⁴ (diff 0.0).

Clamp (claim (c)): the clamped centre reads joint =
NEC = −7.644643599300465×10⁻⁶ at diff 0.0, DEC
−1.0999871338544456×10⁻⁶ (diff +6.8×10⁻²⁰), ρ at diff
+5.4×10⁻¹⁹; clamp cost 2.127514302081271×10⁻⁷ vs stored
2.1275143020796448×10⁻⁷ (diff 1.6×10⁻¹⁹). The clamped
anchor reproduces at diff +5.4×10⁻²⁰
(−3.018920609401202×10⁻⁵); the clamped (1,1,1) read
reproduces Phase 379's stored end-clamp set (NEC diff
+2.7×10⁻¹⁹, DEC diff +6.0×10⁻¹⁹, ρ diff −1.9×10⁻¹⁹;
joint −2.087299309761305×10⁻⁴, DEC-carried); the clamped
mixed centre reproduces Gate-43's value at diff
+9.2×10⁻¹⁹. Clamped margins: over the anchor's
unclamped level +2.2165206678448785×10⁻⁵; over
L_stat(H2) +1.865799553183718×10⁻⁴. Both survive.

## §3 The registered box and the diagonal — claims (d), (e)

Recount of the stored screens file
(`phase396/results/p396_screens.jsonl`, md5 in §6), no
tensor reads: 336 reads, 336 feasible, 326 with joint
above the anchor's −2.9809850277749006×10⁻⁵, worst
dec_min −2.0253148251802704×10⁻⁶, zero reads with
dec_min ≤ −0.5 and zero with dec_min ≤ −0.9999 — the
stored anatomy's counts on every line. The worst-DEC
read (a G2 read at (0.601180962300002,
1.5934531363763935, 4.387238651223381)) re-read on gate
machinery: DEC min −2.0253148251804195×10⁻⁶ (diff
−1.5×10⁻¹⁹), argmin at r = 18.65853658536585, Type-I;
its joint is −3.0654469143335814×10⁻⁵.

The diagonal trace (the registered direction
(−0.025, +0.025, +0.25) from the anchor, k = 1..8 to the
corner region (0.40118096230000194, 1.7934531363763935,
6.887238651223381)): all nine joints (anchor + 8)
reproduce with max |diff| 2.4×10⁻¹⁹ and the sequence is
strictly monotone on the gate's reads, ending at
−9.943225903497104×10⁻⁶, still rising. Increments from
the anchor (gate): +2.8787467063572775×10⁻⁶,
+2.9518552812045622×10⁻⁶, +2.671537624396406×10⁻⁶,
+2.768176070933303×10⁻⁶, +2.3238345462523466×10⁻⁶,
+2.368937799387586×10⁻⁶, +2.1267632453844014×10⁻⁶,
+1.7767731003361271×10⁻⁶ — a mild decay, no sign change;
last/first = 0.6172036936811398 (stored-exact
0.6172036936811021), the claimed ≈ 62%. The RAY3
endpoint (0.601180962300002, 1.5934531363763935, 7.0)
re-reads at diff −8.1×10⁻²⁰ (−2.8521103406139005×10⁻⁵).

Box edges (claim (e)): the registered box is μ_S ∈
[0.40, 1.10], μ_N ∈ [0.95, 2.00], μ_M ∈ [1.60, 7.00].
The centre sits 0.0003528067864536 above the μ_S lower
edge and 0.0136544929510376 below the μ_N upper edge;
μ_M = 6.715383396291902 sits inside its edge. Two
independent polishes converged to the same corner basin
in the phase's record; the gate's re-reads confirm the
centre as the box's best read. The disclosure stands
exactly as the phase stated it, and is issued as rider
G47-E.

## §4 The degeneracy ruling — claim (f)

The phase's pre-registered flag (registration SS7): if
the best point's peak |β·S| over the band is < 0.5 ×
H2's peak — equivalently μ_S < 0.5, the scaling being
linear in S — the gain is substantially purchased by
shift removal and the point is an artefact candidate,
not a design improvement, until a gate rules. The gate
measured the following, all on its own machinery.

(i) The physicality table reproduces EXACTLY. Every
entry of Phase 396's physicality record — the S/N/M
band ranges, the peaks, all nine local profile values
and all nine unscaled-H2 values at each configuration's
own NEC argmin radius, for H2, C394, the anchor and the
centre — reproduces at max diff 0.0. Peaks |β·S|:
H2 0.8853484980534808; C394 0.7096678598389627; anchor
0.532254662030653; centre 0.35445175617988206. The peak
ratios to H2 equal μ_S exactly in every row. At the
centre: band N range [2.2842995923862865,
2.458052773695781] against H2's [1.1500011374053365,
1.237474933224289]; band M range [1.8379746215992199,
47.336550068823556] against H2's [1.1247843305658367,
7.90006025484854]; at its binding site
(r = 16.46341463414634) the scaled locals are
S = 0.07743322636564062, S′′ = 0.016179742866951445,
N = 2.4547830252740606, M = 39.31075989942729, against
H2's totals at the same radius S = 0.19341247283160218,
S′′ = 0.040413711588093475, N = 1.2358288205967942,
M = 6.704925190210542. The drift the note describes is
real, digit for digit.

(ii) Gain attribution. One-factor moves from the anchor
(gate SET joints; the full anchor→centre gain is
+2.2377958108656912×10⁻⁵ on the gate's reads, stored
+2.2377958108656506×10⁻⁵): μ_S alone (to
0.4003528067864536) reads −1.2541136241732198×10⁻⁵, a
gain of +1.726871403601705×10⁻⁵ — 77% of the full gain;
μ_N alone (to 1.9863455070489624) reads
−1.95375089438119×10⁻⁵, +1.0272341333937351×10⁻⁵ —
46%; μ_M alone (to 6.715383396291902) reads
−2.8774926941038865×10⁻⁵, +1.0349233367103845×10⁻⁶ —
5%. The single-factor gains sum to more than the full
gain (interaction ≈ −6.2×10⁻⁶), but the ordering is
unambiguous: shift removal is the dominant single
purchaser of the centre's gain, exactly as the note
charged.

(iii) The μ_S² test — the note's mechanism does not
survive as stated. At the centre's own binding site
(the gate's NEC argmin point [16.158003891492058,
−3.020989248027475, 0.9146341463414641],
r = 16.46341463414634), with (μ_N, μ_M) held at the
centre's, the pointwise violation was scanned over
μ_S ∈ {0, 0.05, 0.1, 0.2, 0.3, 0.4003528067864536, 0.5,
0.601180962300002, 0.8, 1.0}. The shift-free floor at
that site is POSITIVE: NEC(0) = worst-null(0) =
+8.716515065031833×10⁻⁶ (Type-I; both margin forms
agree) — the site is NEC-satisfied with no shift at
all, and the violation grows monotonically as μ_S
increases (worst-null: +6.54×10⁻⁶ at 0.05,
+4.37×10⁻⁶ at 0.1, +1.4×10⁻⁸ at 0.2, −4.34×10⁻⁶ at
0.3, −8.706718841221368×10⁻⁶ at the centre,
−3.479×10⁻⁵ at 1.0). But the growth is approximately
LINEAR in μ_S, not quadratic: the log–log slope of
|worst-null(μ_S) − worst-null(0)| against μ_S is
1.00005, and least-squares fits against μ_S² fail —
slope −3.9689×10⁻⁵ with intercept −7.84×10⁻⁶ and max
|residual| 5.77×10⁻⁶ for the worst-null (−4.0577×10⁻⁵,
−6.19×10⁻⁶, 6.02×10⁻⁶ for the NEC margin): residuals
the size of the effect itself. The rationale implied
by 316's anatomy — S′′ carries NEC and S′′ scales
with μ_S, suggesting a μ_S² purchase — is refuted as
the mechanism at this site; the shift's first-order
presence, not its square, is what the site charges.

(iv) The shift-free limit is not a trivial pass. The
full SET-244 read at (0, 1.9863455070489624,
6.715383396291902) — the centre's (μ_N, μ_M) with the
shift removed entirely — reads joint = NEC = DEC =
WEC = −1.0499339416511982×10⁻⁶ (SEC
−3.367547400792578×10⁻⁴, ρ +9.858094353742352×10⁻⁵):
a residual (N, M)-sector violation survives with no
shift at all, at some other site. So the family's
level does not reach zero by shift removal at fixed
(N, M); equally, the centre at μ_S = 0.40 sits BELOW
that floor (−7.431892×10⁻⁶ < −1.049934×10⁻⁶), because
the binding constraint has moved. And the (N, M)
dependence is real in both directions: at H2's
(μ_N, μ_M) = (1, 1), removing the shift makes the
joint WORSE (−2.928040843203875×10⁻⁴ against
L_stat(H2) = −1.942246×10⁻⁴). Along the ridge, joint/
μ_S² is not constant (H2 −1.9422459891767238×10⁻⁴;
C394 −1.0603139686767782×10⁻⁴; anchor
−8.248013369707106×10⁻⁵; centre
−4.6367496148491085×10⁻⁵), and every centre beats the
pure μ_S²-scaling prediction from H2 — C394 by
+5.667×10⁻⁵, the anchor by +4.039×10⁻⁵, the centre by
+2.370×10⁻⁵: the (μ_N, μ_M) co-movement contributes
improvement beyond shift removal, in declining
measure as the ridge descends.

RULING. The degeneracy note is upheld in its quotable
consequence and restated in its mechanism. Upheld: by
the pre-registered criterion the centre fails the
design-improvement bar, and the gate's attribution
confirms the failure is substantive, not formal —
shift removal is the largest single purchaser of the
gain (77%). The centre is quotable only as a
scaling-surface level with G47-F attached, never as a
design improvement. Restated: the purchase is
approximately linear in μ_S at the binding site above
a positive shift-free floor, not quadratic; and the
strong trivial-limit reading — the level approaches
zero because the shift does — is refuted at the
centre's (μ_N, μ_M), where the shift-free configuration
itself violates at −1.049934×10⁻⁶. What the gate's
measurements do NOT decide is the ridge's asymptote:
whether continued travel along the ridge (which
co-moves (μ_N, μ_M)) reaches a legal level only in the
shift-free limit. That question, and the (N, M)-sector
floor along the ridge, belong to Phase 397's
degeneracy probe, which is the measuring instrument
named for it; the criterion it applies is the one
stated in G47-F. The last centre on this line whose
gain is not so purchased — the deepest centre clearing
the registered half-of-H2 peak-shift bar — is Phase
395's centre (μ_S = 0.601180962300002, peak ratio
0.6012, level −2.980985×10⁻⁵; Gate-46's set).

## §5 The quotable set (G47-*), with the fence

**FENCE (verbatim, travels with every quotation):** band pose
[10, 20] only; Phase 356's full-extent caveats travel with
every level in this set; every level is negative; no EC pass,
no member, no drive or transport implication.

- **G47-A (the third-widening centre).** At the per-profile
  stationary scaling (μ_S, μ_N, μ_M) =
  (0.4003528067864536, 1.9863455070489624,
  6.715383396291902) of the harvested centre H2's total
  profiles, the stationary joint level (SET-244, SAMPLER-M,
  band [10, 20]) is **−7.431892×10⁻⁶** (NEC min
  −7.4318921690925×10⁻⁶ at r = 16.46341463414634; DEC min
  −1.0979323923912478×10⁻⁶, Type-I, at
  r = 18.902439024390244; ρ min +9.858014400881535×10⁻⁵),
  above Phase 395's centre (−2.980985×10⁻⁵) by
  +2.237796×10⁻⁵, above Phase 394's centre
  (−6.812653×10⁻⁵) by +6.067464×10⁻⁵, above Phase 389's
  mixed centre (−1.757074×10⁻⁴) by +1.682755×10⁻⁴, and
  above L_stat(H2) = −1.942246×10⁻⁴ by +1.867927×10⁻⁴.
  **G47-E and G47-F are part of this claim wherever its
  level is quoted.**
- **G47-B (pointwise grade).** The exact worst-null at
  G47-A's NEC argmin is −8.706719×10⁻⁶, above Phase 395's
  centre's worst-null (−3.0896210095678075×10⁻⁵) by
  +2.218949×10⁻⁵: the improvement survives at pointwise
  grade. **G47-E and G47-F are part of this claim wherever
  its level is quoted.**
- **G47-C (the end-clamp rider — part of G47-A wherever
  its margin is quoted).** End-clamping H2's correction
  splines (all first/last knots zeroed) and applying the
  G47-A scaling to the clamped totals reads a joint level
  of −7.644644×10⁻⁶ (NEC-carried), a clamp cost of
  2.128×10⁻⁷: the clamped level remains above Phase 395's
  centre's unclamped level by +2.216521×10⁻⁵ — the margin
  over the anchor survives clamping — and remains above
  L_stat(H2) by +1.865800×10⁻⁴ — the margin over the
  centre bar survives clamping with it. **G47-E and G47-F
  are part of this claim wherever its level is quoted.**
- **G47-D (the registered box).** In Phase 396's
  registered box (μ_S ∈ [0.40, 1.10], μ_N ∈ [0.95, 2.00],
  μ_M ∈ [1.60, 7.00]), all 336 stored reads are feasible
  and none is DEC-saturated (worst DEC
  −2.0253148251802704×10⁻⁶, a Type-I read at
  r = 18.65853658536585); 326 of the 336 reads beat Phase
  395's centre's level; and the registered diagonal from
  that centre rises at every one of its eight steps to
  −9.943226×10⁻⁶ at the box's corner region, its
  increments decaying only mildly (last/first = 0.617)
  with no turn inside the box.
- **G47-E (the box-edge rider — part of G47-A, G47-B and
  G47-C wherever their levels are quoted).** The G47-A
  centre presses the registered box's μ_S lower edge
  (μ_S = 0.4003528067864536 against the edge 0.40) and
  nears its μ_N upper edge (1.9863455070489624 against
  2.00) — the third widening in a row whose centre has
  arrived at the new μ_S edge: the centre is the optimum
  **of the registered box**, and whether the level keeps
  rising outside the box — below μ_S = 0.40, or above
  μ_N = 2.00 — is unmeasured in this claim set.
- **G47-F (the degeneracy rider — part of G47-A, G47-B
  and G47-C wherever their levels are quoted; the gate's
  ruling on Phase 396's pre-registered degeneracy
  note).** The G47-A centre is quotable only as a
  scaling-surface level, **not as a design
  improvement**: its peak physical shift over the band
  is |β·S| = 0.35445175617988206, 40.0% of H2's peak
  0.8853484980534808 — below the half-of-H2 bar
  pre-registered in Phase 396's SS7 — with the lapse
  doubled (band N max 2.458052773695781 against H2's
  1.237474933224289) and the spatial deformation grown
  ~6× (band M max 47.336550068823556 against 7.90006025484854).
  On the gate's own one-factor attribution from Phase
  395's centre, shift removal alone buys
  +1.726871×10⁻⁵ of the +2.237796×10⁻⁵ gain (77%;
  μ_N alone 46%, μ_M alone 5%). The mechanism, as
  measured by the gate, is restated: at the centre's
  binding site the NEC violation grows approximately
  linearly in μ_S (log–log slope 1.00005) above a
  positive shift-free floor (worst-null at μ_S = 0:
  +8.716515×10⁻⁶, Type-I) — not as μ_S², whose fits
  leave residuals the size of the effect — and the
  shift-free configuration at the centre's (μ_N, μ_M)
  itself violates, at joint −1.049934×10⁻⁶ in the
  (N, M) sector, so the level's approach is not a pure
  trivial limit either. The last centre on this line
  clearing the registered half-of-H2 peak-shift bar is
  Phase 395's centre (μ_S = 0.601180962300002, peak
  ratio 0.6012, level −2.980985×10⁻⁵). Criterion: a
  centre on this scaling line is quotable as a design
  improvement only while its peak |β·S| is at least
  half of H2's peak; whether the ridge's continuation
  reaches a legal level only in the shift-free limit
  is referred to Phase 397's degeneracy probe, the
  measuring instrument named for that question, and
  until it reports, centres below the bar carry this
  rider.

## §6 Provenance and artefacts

- Stored bytes verified (md5): CHECKPOINT396.md
  447b42f2fdea53f6653210190cb31098 · p396_memo.md
  2d6aef13d18ce6274f10691eaf948adb ·
  p396_confirmation.json 0da43dc00af7cd0a4194b9e1235f66c9 ·
  p396_clamp.json c3bc4d30448abf28785635c4d36a3f75 ·
  p396_controls.json 3eac238d67e681fc2821cc99f8a53179 ·
  p396_anatomy.json 7507dfa0b8ee3c228b69daa09151c749 ·
  p396_physicality.json 651b4900f1d3cfa1a95dbf3dbaa16695 ·
  p396_search_summary.json e609508c4c03c85c7749e44104b98dd9 ·
  p396_screens.jsonl d3a71a0d225726d7d989406191f126ff ·
  p395_confirmation.json 6d3e2c209ffbcd36ff2f59bdee09a0bb ·
  p395_clamp.json 2eb334e7a12e55753fc894d1793f8df6 ·
  p395_search_summary.json 62993b28d0ea5f6dbb000fef530053ff ·
  p394_confirmation.json 611424f0c0ac49ead895e2ed2b3a9172 ·
  p379_confirmation.json 1bcb8b3900026cc78e6aacb33654ad72 ·
  p379_state_H2.json 66adf3797e6e105c71f89ca8fe5be4fe ·
  p344_confirmation.json bca93c039daf9c8baf68f4e567abe873 ·
  p344_state_A2.json eec813ee4d1c94de6ac21829304d5ebd.
  The gate's profile assembly consumes the stored vectors
  from the confirmation artefacts; the state files agree
  at 0.0 (C-0).
- Gate artefacts: `gate47/work/g47_lib.py` (machinery),
  `gate47/work/g47_run.py`, `gate47/work/g47_run2.py`
  (drivers); `gate47/results/g47_numbers.json` (the §2
  deciding reads), `g47_box_diag.json` (the §3 recount,
  worst-DEC re-read, diagonal and RAY3 re-reads),
  `g47_clamp_margins.json` (the §2 clamp reads and
  margins), `g47_degeneracy.json` (the §4 physicality
  table, binding-site μ_S scan and fits, shift-free
  reads, gain attribution, ridge table),
  `g47_summary.json` (calibrations, md5 registry).
- Bookkeeping remark: the first diagonal increment is
  +2.8787467063572775×10⁻⁶ on both the stored anatomy
  file and the gate's re-read. A figure of
  ≈2.874796×10⁻⁶ appeared in this gate's own charge
  text; that was a transcription slip in the charge,
  not in the phase record (whose checkpoint rounds the
  increment +2.879×10⁻⁶, agreeing with the file). No
  phase number is affected.
- Process note: the worker's first driver run crashed
  on a driver-side array-size bug in the trivial-limit
  calibration call; it was fixed and rerun in full
  (`g47_run2.py`), the trivial limit then reading
  exactly 0.0. No machinery changed and no deciding
  read was affected.
- Publication: none by this gate. The parent publishes
  the G47-* set only in the wording of §5 — in
  particular, G47-A may not be quoted without G47-E and
  G47-F attached.
