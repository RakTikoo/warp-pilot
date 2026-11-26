# GATE-41 — Re-judgement of the Phase 379 claim set
# (the harvested centres' stationary improvement)

Charged at ledger entry 964 (2026-11-26). The gate
re-judged Phase 379's claim set with machinery built
for the gate alone: its own centre assembly from the
stored A2 profile vectors, its own stationary
Einstein-tensor read path (a jet value/gradient/
Hessian algebra over the spatial coordinates, in
gate41/work/g41_lib.py), its own Eulerian-frame /
Hawking–Ellis / SET-244 read path, adversary polish
and worst-null. NO Phase 344/359/374/379 code — and
no code of the 316/338/341 lineage — was reused for
any deciding read; those records were read for the
claims, the definitions and the stored parameters
only. Execution on the VM, the frame of record
(frame admission at §1).

## Verdict

Phase 379's headline claim SURVIVES re-judgement:
the stationary level improves at both harvested
centres — the gate's independent reads reproduce
every deciding value of the phase at float64
roundoff (max |gate − stored| over all deciding
fields 3.9×10⁻¹⁸; every NEC/DEC/ρ/depth/worst-null
diff ≤ 8.7×10⁻¹⁹). Per claim: **(a) SURVIVES**
(H2's joint level −1.942246×10⁻⁴ and both margins);
**(b) SURVIVES** (H1's joint level −2.014605×10⁻⁴);
**(c) SURVIVES** (the centre constructions — the
zero-displacement reads reproduce Phase 374's
bottom identities at roundoff, the floor minima
exactly); **(d) SURVIVES** (the classification
consequence — it is arithmetic on (a) and (c) in
the same pose and instrument); **(e) SURVIVES
RESTATED** (the end-clamping anatomy reproduces at
roundoff, and the quotable form is ruled at §4:
the margin over the centre bar does not survive
end-clamping, the margin over the dwelling ceiling
does, reduced). §5 is the only quotable form of
the set. The standing fence binds every surviving
form: this is a stationary LEVEL IMPROVEMENT on the
A2 lineage in the band pose — every level remains
negative; there is NO EC pass, NO member in the
energy-condition sense, and no drive or transport
implication.

## §1 The gate's machinery and calibrations

Machinery (gate41/work/g41_lib.py; drivers
g41_calibrate.py, g41_audit.py). Centre: Phase
344's A2 incumbent — winner spec {plat, a=2, b=2,
A=0.07439108177516472, c=15, W=5, e=3.0}, lamS 0.70,
M ramp (m0 6.0, r1 8.5, r2 20.0), K = 33 not-a-knot
spline corrections (vS, vN, vM) additive, from
p344_confirmation.json (entry point A2). Centres
built by the registered scaling of A2's totals
(S→μS, N→μN, M→1+μ(M−1), derivatives by μ), μ from
374's dwell-bottom expression (μ = 1.1125, 1.15).
The tensor is assembled from metric jets: each
metric component carries its value, spatial
gradient and spatial Hessian, built by the chain
rule from radial-function and direction jets; the
Christoffel→Ricci contraction is the textbook one.
Stationary throughout (the pose is stationary).

- **C-0 (vectors):** A2's (vS, vN, vM) from
  p344_confirmation.json vs p344_state_A2.json
  final_incumbent: max diff 0.0. (The H1/H2
  incumbent vectors in p379_confirmation.json vs
  the p379_state files likewise agree at 0.0.)
- **C-1 (trivial limit):** zero profiles
  (S=0, N=1, M=1) give max |T| = 0.0 exactly.
- **C-2 (FD path):** a from-scratch 4-D centred-FD
  Einstein tensor built from the metric function
  alone (profile values only, no derivative
  formulas) converges to the gate's analytic
  tensor as h → 0: at the anchor's stored NEC
  argmin point and a generic point, max |ΔT| falls
  4.30×10⁻⁵ → 9.24×10⁻⁶ → 1.05×10⁻⁷ → 5.36×10⁻⁸
  over h = 0.1, 0.05, 0.025, 0.0125 (median |ΔT|
  3.07×10⁻⁷ → 2.09×10⁻⁹). The residual at fixed h
  is FD truncation on a C² metric (spline third
  derivatives jump at knots); the trend, not any
  single h, is the check. (Record:
  g41_calibration_fd.json; the six-point survey is
  in g41_calibration.json.)
- **C-3 (density-split identity):** the gate's
  Eulerian ρ vs the recorded closed-form split
  (R + Q_K)/(16π) at all 6642 SET points of the
  anchor: max |diff| 1.52×10⁻¹⁸.
- **C-4 (stationary anchor):** the gate's SET-244
  read of A2 through the centre path at μ = 1
  reproduces the stored confirmation at roundoff
  on every field: NEC min −2.319453132752996×10⁻⁴
  (diff −1.36×10⁻¹⁹, argmin r = 16.2195), DEC min
  −2.233693204455982×10⁻⁴ (diff +8.13×10⁻²⁰,
  argmin r = 19.3902), WEC min (diff +4.34×10⁻¹⁹),
  SEC min (diff −4.34×10⁻¹⁹), ρ min
  8.638077678074035×10⁻⁵ (diff +2.17×10⁻¹⁹),
  Type-I count 3535 exact.
- **C-5 (μ ≡ 1 reduction):** centre_profiles(1.0)
  vs A2's total profiles on r ∈ [9, 21]: max diff
  0.0 — the centre construction reduces to A2
  identically at μ = 1.
- **C-6 (anchor depth):** the gate's adversary
  polish at A2 reproduces the stored polished
  depth −2.2644422911711972×10⁻⁴ at diff
  −3.25×10⁻¹⁹, from the same polished point.
- **C-7 (frame admission):** the laptop pool ran
  the gate's anchor read and did NOT reproduce it
  at diff 0.0 (NEC −1.05×10⁻⁶, WEC −8.31×10⁻⁶,
  SEC −5.74×10⁻⁷; DEC and ρ at roundoff; Type-I
  count exact — the lineage pattern a seventh
  time). **Not admitted; every deciding read is a
  VM read.** The drift is confined to the
  sampled-margin statistics, exactly as in C-8.
  (Record: g41_frame_admission.json.)
- **C-8 (the frame-association calibration
  incident, disclosed):** the gate's first C-4 run
  reproduced DEC and ρ at roundoff but missed the
  NEC/WEC/SEC minima by up to 4.95×10⁻⁶. Localised
  (diagnostic comparison only): the covariant
  tensor and all nine profile arrays agreed
  exactly, and the stored NEC argmin point's own
  margin reproduced at 1×10⁻¹⁹; the misses came
  from isolated non-Type-I points where the
  sampled margin is taken in the Eulerian frame —
  whose triad inside γ's degenerate tangential
  eigenspace (eigenvalues 1, 1, M) is fixed by
  eigh(γ) acting on γ's exact floating-point
  entries. The gate's jet-product assembly
  ((M−1)·(n_i·n_j)) put γ ~4×10⁻¹⁶ away from the
  definition's association (((M−1)·n_i)·n_j), and
  at isolated points that ulp difference rotates
  the triad and moves the sampled margins by
  ~10⁻⁶. With γ's value assembled in the
  definition's association, C-4 passes on every
  field (above). The deciding reads below use the
  corrected assembly. This is the same instrument
  sensitivity Gates 39/40 corrected from the other
  side (SET margins at non-Type-I points are
  sampled bounds, frame-convention dependent at
  the ~10⁻⁶ level); it touches no deciding value
  here beyond what C-4/C-7 record, because every
  deciding minimum of this claim set is either a
  Type-I eigenvalue margin or reproduces at
  roundoff under the corrected assembly.

All calibrations passed before any audit read.
Audit programme: the two centre zero-displacement
reads, the two incumbent reads (SET-244 +
adversary polish + exact worst-null at each SET
NEC argmin), and the H2 end-clamp re-read —
5 SET-244 reads, 33,210 point reads, on the VM.

## §2 Adjudication of (a) and (b) — the levels

**(a) H2 (μ = 1.15) — SURVIVES.** Re-read at the
stored K = 17 incumbent vectors on the gate's
machinery: NEC min = **−1.9422459891767262×10⁻⁴**
at r = 16.2195 (diff vs stored −3.52×10⁻¹⁹),
DEC min = −1.8982585080461542×10⁻⁴ (diff
+1.63×10⁻¹⁹), ρ min = +8.789653555683191×10⁻⁵
(diff +9.49×10⁻²⁰), WEC/SEC minima at diffs
0.0 / +3.04×10⁻¹⁸, Type-I count 3262 exact, DEC
argmin Type-I. The joint level is NEC-carried:
**−1.942246×10⁻⁴**, above its centre bar
(L_stat(1.15), §3) by **+8.956535×10⁻⁶** and above
the Gate-40-verified dwelling ceiling
(−2.099385079591706×10⁻⁴) by **+1.571391×10⁻⁵** —
both margins reproduce (stored: +8.956534894425722
×10⁻⁶, +1.5713909041498343×10⁻⁵). Confirmation
quantities reproduce likewise: polished depth
−1.4402430840320605×10⁻⁴ (diff +3.25×10⁻¹⁹; past
the −0.0034 C2 bar by a factor of 24), exact
pointwise worst-null at the SET NEC argmin
−1.9432881962794707×10⁻⁴ (diff −3.25×10⁻¹⁹) —
itself above L_ceil by +1.561×10⁻⁵, so the
margin over the dwelling ceiling is not an
artefact of the sampled SET read.

**(b) H1 (μ = 1.1125) — SURVIVES.** NEC min =
**−2.014605242909165×10⁻⁴** at r = 17.6829 (diff
−3.52×10⁻¹⁹), DEC min = −1.9641708622922396×10⁻⁴
(diff −4.34×10⁻¹⁹), ρ min = +8.750850886168864×10⁻⁵
(diff +4.07×10⁻²⁰), Type-I count 3310 exact. Joint
level **−2.014605×10⁻⁴**, above its centre bar —
which is L_stat(1.1125) = L_ceil itself — by
**+8.477984×10⁻⁶** (stored +8.47798366825447×10⁻⁶).
Polished depth −1.6697787772751145×10⁻⁴ (diff
−8.67×10⁻¹⁹), exact worst-null at the SET NEC
argmin −2.0234192402649137×10⁻⁴ (diff
−3.52×10⁻¹⁹), itself above the centre bar by
+7.597×10⁻⁶.

Both incumbents are NEC-bound and C1-feasible
(ρ min > 0), as stored. No incumbent reaches
≥ 0 on either coordinate: no EC pass, no gate
referral under the phase's ≥ 0 rider — correctly
not claimed by the phase.

## §3 Adjudication of (c) and (d) — the centres
## and the classification consequence

**(c) The centre constructions — SURVIVES.** The
gate built both centres itself, from A2's stored
profile vectors (C-0: the two stored artefacts
agree at 0.0), by the registered μ-scaling, with
μ taken from 374's dwell-bottom expression. The
zero-displacement reads reproduce Phase 374's
bottom identities at roundoff:

| centre | NEC (gate) | DEC (gate) | ρ min (gate) | max |diff| vs identity |
|---|---|---|---|---|
| H1, μ = 1.1125 | −2.0993850795917053×10⁻⁴ | −1.941081222390092×10⁻⁴ | 8.764071936093984×10⁻⁵ | 3.25×10⁻¹⁹ |
| H2, μ = 1.15 | −2.0318113381209823×10⁻⁴ | −1.854699056943026×10⁻⁴ | 8.801281960223575×10⁻⁵ | 3.79×10⁻¹⁹ |

The centres are floor-feasible at zero
displacement, as claimed: the centre profiles'
minima on FINE_R reproduce Phase 379's CTL-379-F
record EXACTLY (diff 0.0) — H1: N 1.1125340342235222,
M 1.1206906539640158; H2: N 1.1500351814445395,
M 1.1247588782549376. Together with C-5 (the
μ ≡ 1 reduction is the identity, exactly), the
centre construction is verified end to end: the
harvested configurations are the configurations
Phase 374's dwell bottoms were measured to be.

**(d) The classification consequence — SURVIVES.**
The consequence is arithmetic on (a) and (c) in
the same pose (β = 1.1, band [10, 20]) and the
same instrument (SET-244, SAMPLER-M): the
dwelling ceiling −2.099385×10⁻⁴ was the A2
centre's own stationary profile value
L_stat(1.1125) (Gate-40 §3, re-derived here as
centre H1's zero-displacement read), and the
stationary search re-centred on the harvested
bottoms finds stationary levels above it —
H2's by +1.571×10⁻⁵, H1's by +8.478×10⁻⁶ — with
H2's margin surviving at pointwise grade
(worst-null +1.561×10⁻⁵, §2). The dwelling
ceiling was therefore the A2 centre's ceiling,
not the family's; the two levers compose in the
stated sense: the dwelling pose found the μ
direction, and the stationary search at the
harvested centres converts it into a better
stationary level. (What the composition does
NOT establish — and the claim does not assert —
is anything about a further iteration, the
full extent, or any configuration at ≥ 0.)

## §4 Ruling on (e) — the end-clamping anatomy
## and the quotable form

The anatomy reproduces at roundoff. H2's stored
incumbent boundary (end-knot) values, read from
the vectors: S: −8.141616667879931×10⁻⁵ (r = 10),
**−7.926584743685476×10⁻³** (r = 20); N:
−3.404403920298938×10⁻⁵, +7.01931505368771×10⁻⁶;
M: +2.5452310899203476×10⁻⁵, +2.529041046983001×10⁻⁵
— the outer-edge freedom is, as stored, chiefly
the S correction's r = 20 knot. The gate's
end-clamp re-read (first/last knots of all three
correction vectors zeroed) gives: NEC min
−1.956241449779669×10⁻⁴ (diff +8.13×10⁻²⁰),
DEC min −2.087299309761317×10⁻⁴ (diff
−5.96×10⁻¹⁹), ρ min 8.793529206482109×10⁻⁵
(diff +1.63×10⁻¹⁹) — joint (now DEC-carried)
**−2.087299×10⁻⁴**, a clamp cost of
**1.450533×10⁻⁵** against the unclamped joint
level (stored: cost 1.45×10⁻⁵, clamped
−2.087299309761311×10⁻⁴).

**Ruling — the quotable form.** The two margins
of G41-A behave differently under the clamp, and
the claim set is quotable only with that split
carried on its face:

1. The margin over H2's own centre bar
   (+8.957×10⁻⁶) does NOT survive end-clamping:
   the clamped level −2.087299×10⁻⁴ sits BELOW
   L_stat(1.15) by −5.549×10⁻⁶. The
   improvement-over-centre is therefore partly
   carried by the S correction's outer-edge knot,
   and any quotation of that margin must carry
   the end-clamp figure with it.
2. The margin over the dwelling ceiling
   (+1.571×10⁻⁵) DOES survive end-clamping,
   reduced to **+1.208577×10⁻⁶**: even with every
   end knot zeroed, the harvested centre's
   stationary level beats the best dwelling
   worst-instant level. The classification
   consequence (d) therefore stands in clamped
   form as well, at the reduced margin.

Two framing facts, verified on the record, bound
the ruling. First, the comparison is like-for-like
in the sense Phase 379 stated: the registered
reads of this family have never end-clamped their
corrections — A2's own K = 33 S-correction end
values are nonzero (−4.897×10⁻⁵ / +3.058×10⁻⁵,
Phase 344's anatomy), and Phase 344's own
end-clamp re-read of A2 collapses its level to
−4.336×10⁻³; band-edge freedom is a standing
feature of the family's corrections, not a
device of this phase. Second, the clamped level
is DEC-carried while the unclamped level is
NEC-carried — the clamp moves which condition
binds, which is the precise sense in which the
band pose's caveat "bites" here. The registered
(unclamped) level of G41-A stands as the claim;
the clamped figures are its mandatory rider, not
a replacement read.

## §5 The claim set as re-judged — the only quotable form

> **G41-A (the H2 level).** At the harvested
> centre μ = 1.15 on the A2 lineage (β = 1.1,
> posed shell [10, 20]), the confirmed K = 17
> incumbent reads, on SET-244 SAMPLER-M: NEC min
> = −1.942246×10⁻⁴ (at r = 16.220), DEC min =
> −1.898259×10⁻⁴, ρ min = +8.789654×10⁻⁵ — a
> joint stationary level of **−1.942246×10⁻⁴**,
> above the centre's zero-displacement level
> L_stat(1.15) = −2.031811×10⁻⁴ by +8.957×10⁻⁶
> and above Phase 374's Gate-40-verified
> dwelling ceiling −2.099385×10⁻⁴ by
> +1.571×10⁻⁵. Polished depth −1.440243×10⁻⁴
> (past the −0.0034 material bar); exact
> pointwise worst-null at the SET NEC argmin
> −1.943288×10⁻⁴. This claim carries the
> G41-E rider.
>
> **G41-B (the H1 level).** At the harvested
> centre μ = 1.1125, the confirmed K = 17
> incumbent reads: NEC min = −2.014605×10⁻⁴
> (at r = 17.683), DEC min = −1.964171×10⁻⁴,
> ρ min = +8.750851×10⁻⁵ — a joint stationary
> level of **−2.014605×10⁻⁴**, above its centre
> bar L_stat(1.1125) = −2.099385×10⁻⁴ by
> +8.478×10⁻⁶. Polished depth −1.669779×10⁻⁴;
> exact pointwise worst-null at the SET NEC
> argmin −2.023419×10⁻⁴.
>
> **G41-C (the centres).** The harvested centres
> are the μ-scalings of A2's total profiles
> (S→μS, N→μN, M→1+μ(M−1)) at μ = 1.1125 and
> μ = 1.15; their zero-displacement SET-244
> reads reproduce Phase 374's bottom identities
> (μ = 1.1125: NEC −2.099385×10⁻⁴, DEC
> −1.941081×10⁻⁴; μ = 1.15: NEC −2.031811×10⁻⁴,
> DEC −1.854699×10⁻⁴), and both centres are
> floor-feasible at zero displacement (FINE_R
> minima — H1: N 1.112534, M 1.120691; H2:
> N 1.150035, M 1.124759).
>
> **G41-D (the classification consequence).**
> The dwelling pose's ceiling was the A2
> centre's ceiling, not the family's: the best
> stationary level on the A2 lineage is now the
> harvested centre H2's −1.942246×10⁻⁴ (band),
> which exceeds the best dwelling worst-instant
> level (−2.099385×10⁻⁴) like-for-like in pose
> and instrument. The levers compose: dwelling
> found the μ direction; the stationary search
> at the harvested centres converts it.
>
> **G41-E (the end-clamp rider — part of G41-A
> and G41-D wherever their margins are quoted).**
> End-clamping H2's correction splines (all
> first/last knots zeroed) reads a joint level
> of −2.087299×10⁻⁴ (DEC-carried), a cost of
> 1.450533×10⁻⁵: the clamped level falls below
> L_stat(1.15) by −5.549×10⁻⁶ — the margin over
> the centre bar does not survive clamping —
> and remains above the dwelling ceiling by
> +1.208577×10⁻⁶ — the G41-D margin survives
> clamping in reduced form. The gain's
> band-edge component is chiefly the S
> correction's r = 20 knot (−7.926585×10⁻³).
>
> **Fences (part of every claim above).** These
> are stationary LEVEL IMPROVEMENTS on the A2
> lineage in the band pose only (β = 1.1, posed
> shell r ∈ [10, 20], K = 17 spline corrections
> about the two harvested centres). Every level
> remains NEGATIVE: every configuration still
> violates NEC and DEC at its binding site.
> There is NO EC pass, NO member in the
> energy-condition sense, and no sustainment,
> front/joint, transport or drive implication.
> All levels are band-posed reads; Phase 356's
> full-extent caveats travel with them (the A2
> lineage's stationary full-extent levels
> restate to ≈ −1.44×10⁻³ over [10, 60]; neither
> Phase 379 nor this gate ran an extent audit).
> Phase 344's incumbent remains the best
> stationary level AT THE A2 CENTRE and is
> untouched as such; Gate-40's set stands for
> its pose. "Centre bar" and "dwelling ceiling"
> in G41-A–E are the quantities defined in
> G41-C and Gate-40 §5 respectively, and no
> other.

## §6 Provenance and artefacts

Gate machinery and records: gate41/work/
(g41_lib.py, g41_calibrate.py, g41_audit.py,
g41_anchor_only.py), gate41/results/
g41_calibration.json, g41_calibration_fd.json,
g41_frame_admission.json, g41_numbers.json.
All deciding diffs vs Phase 379's stored record
are ≤ 3.9×10⁻¹⁸ (the H1 WEC minimum); the
calibration incident of C-8 and the laptop
non-admission of C-7 are the gate's only
non-roundoff events, both recorded with their
anatomy. Phase 379's disclosed items stand as
the phase recorded them and touch no deciding
read here: its polish transcription bug was in
its own pre-search control path (the gate's
independent polish reproduces all three depths —
A2's and both incumbents' — at roundoff), and
its restart duplicates are screen-log audit
trail, not reads. Three-goal accounting:
(1) FTL — the extended-class stationary pressure
level improvement survives gate re-judgement
(−2.319453×10⁻⁴ at the A2 centre → −1.942246×10⁻⁴
at the harvested H2 centre, band pose); the wall
is moved, not broken; no drive. (2) Wormhole —
untouched by this gate. (3) Subluminal record —
untouched; Procaccia 0.1363 and the programme's
verified 0.10 stand. **DESK: NO DATA CONTACT.**
