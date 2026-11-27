# Gate-56 registration — independent verification of the Phase 418 claim set

Charged at ledger entry 1112 (parent: FTL — Warp Research chat).
Object: ledger entry 1111 (Phase 418: A BETTER CARRYING BASE
EXISTS), `phase418/CHECKPOINT418.md`, `phase418/results/`
(p418_memo.md, p418_confirmation.json, p418_state.json,
p418_screens.jsonl [1,884 lines], p418_controls.json,
p418_controls_laptop.json), `phase418/work/p418_registration.md`.

Written BEFORE any gate computation. Deciding reads on the VM
(programme venv, float64); laptop admission control run and
reported (SS6). No ledger append, no publication, no user
contact: the verdict returns to the parent agent.

## SS0 — Standing fences (inherited, not under test)

Band [10, 20] on every figure. NO member, NO EC pass: SEC
fails at the carried point and prints on its face. B418 is a
CRITERION SPECIALIST: its 2x failure rides alongside the
carried point whenever the ladder is discussed. Lineage
wording per G50-R6 / G52-R4. Sampler named SAMPLER-M on every
sampled statistic (Gate-43 C-10); deciding values are
frame-invariant quantities (Type-I eigenvalue margins at
named points; the secular worst-null).

## SS1 — Claims under test (stored values = the phase's record)

Bars: J1_400 = +1.2273852081052888e-6 (405 winner, Gate-50);
J2_400 = +6.699288757141148e-7 (412 P*, Gate-52);
M0_400 = +1.3977194851281464e-6; SPEND_400(CRIT) =
1.703342770228576e-7. CRIT = 0.4426742490267404 (SS7: half of
H2's peak 0.8853484980534808). 400's base: (muN, muM) =
(2.330448313835416, 11.343911464156438), K_B = 17. B1 (414):
(2.161841908570932, 3.0347910919347685), K_B = 9; static
+6.257021665543401e-6; SPEND_B1(CRIT) = 1.0861605997805081e-5.

(a) THE CARRIED POINT. Base B418 = (2.0473858121439443,
5.606036969201072), K_B = 17, from the stored vectors of
phase418/results/p418_confirmation.json:
 - pure-joint max (screen 1347, criterion_best_joint):
   joint +3.6526207343841256e-6 (NEC = DEC = WEC argmin at
   r = 18.170731707317074), SEC -5.294468643886768e-4,
   worst-null +3.5127967556114907e-6, adversary polish
   +3.616014548066894e-6 at r = 18.8126818196957 (Type-I),
   Type-I fraction 1.0, peak 0.4426742490267404 at r = 10.
 - score-incumbent (screen 1320, criterion_best): joint
   +3.6518621144739354e-6, SEC -5.489496097910961e-4,
   worst-null +3.512020893143546e-6, polish
   +3.626875336510207e-6, peak 0.4426742490267404 at r = 10.
 PEAK RULING REQUIRED: the peak equals the SS7 criterion
 exactly at r = 10, SET BY SCALING. Rule the quotable form
 under G49-F / G50-R5 / G52-R1: the equality is definitional;
 the gate's content is the stored vector's achieved peak
 (dense scan + SET-grid read) and the positive joint.
(b) THE SPEND FLOOR. criterion_best_joint's own static joint
 +3.653874736289154e-6, hence criterion spend
 1.2540019050282306e-9. Three-base comparison at matched
 peaks recomputed from gate reads: B1 1.0861605997805081e-5 /
 400's base 1.703342770228576e-7 / B418 1.2540019050282306e-9.
(c) THE 2x NEGATIVE (search-scoped, G52-R2 discipline).
 Stored 2x winner (screen 1648, K_S = 9): joint
 -3.05568504581619e-5, NEC-bound at r = 12.073170731707318,
 worst-null at the argmin -3.206208318096399e-5, SEC
 -5.578679240331959e-4, Type-I fraction 0.5326708822643782.
 The R17 supplement's K_S = 17 winner: -3.055685517891921e-5
 (the rungs agree). 412's P* on 400's base remains the 2x
 carrier of record; this claim is never a non-existence
 proof.
(d) THE LANDSCAPE CLAIM. Transect 400-base -> B1 (K_B = 9
 representation; stored table in p418_state.json): static
 joint rises monotonically +1.1825342241416796e-6 (t = 0) to
 +6.257021665543401e-6 (t = 1) while the carried joint peaks
 in the interior and collapses at the B1 end. Screen cloud:
 1,378 feasible criterion screens (Stage S + Stage T carried
 + A + B; the 6 Stage-T statics excluded), 859 with joint >
 0, 760 above J1_400; per-mu_M-bin maxima as in p418_memo
 SS3. Re-derive the 6 static + 6 carried transect reads from
 the stored screen configurations; audit the binning by
 full recount of p418_screens.jsonl.

Disclosure audits:
(i) 414 seed attribution. phase414/results/
 p414_screens2.jsonl id 0 joint -1.9990569533851312e-4 and
 id 1 joint -5.503911941753001e-5 (stored). 418's correction:
 id 0 is the G50-shape seed, id 1 the H2-shape seed (414's
 memo/registration swapped them); both reproduced at 418
 (S-C = B1 + G50 shape; supplementary S-F = B1 + H2 seed).
 Audit: shape identity from the stored vectors + gate
 re-reads of both seed configurations; S-C / S-F records in
 p418_screens.jsonl.
(ii) Pattern execution. Stage counts {S 6, T 228, A 800,
 B 350, R 300, R17 200} = 1,884 = the jsonl line count;
 caps A 800 / B 350 / R 300 bound as registered; total
 1,884 <= 2,200; Stage G not triggered; rejects 0,
 penalised 0. NOTE for the record: p418_state.json's
 total_screens field reads 1,684 (the main driver only;
 the R17 supplement's 200 are counted in stage_counts and
 in the jsonl). Confirm the referred points (screens 1320,
 1347: Stage B, base-CD-found; 1648: Stage R) rest on none
 of the squeezed NM/shape blocks: the verdict's points are
 CD-found and SS6-confirmed configurations, re-derived
 here from the stored vectors.

## SS2 — Gate machinery (fresh organisation, not used by 418)

Phase 418 read through the lineage's hand-coded Cartesian
algebra (p316_lib.T_from_SNM) + verify_metric.eulerian_that
+ p2352_run.margins_chunked. Gate-56 does NOT import any of
them for deciding reads (they appear only as calibration
comparators in SS3, never in a deciding path).

- PROFILES: the object definition is the stored assembly
  (A2 base spec/prof; A2 K = 33 vectors from
  phase344/results/p344_confirmation.json; centre scaling
  mu = 1.15; H2 K = 17 vectors from
  phase379/results/p379_confirmation.json; the 398/414
  assembly arithmetic). Every spline in the chain is
  evaluated by the gate's OWN not-a-knot cubic solver
  (second-derivative form, dense linear solve, constant
  extension outside [10, 20] per the registered _eval_corr
  semantics), implemented in gate56/work/g56_splines.py
  (float64 and mpmath variants). The analytic base profiles
  (S_ab via the regularised incomplete beta; plateau bump
  _H; M ramp via the quintic smootherstep) are implemented
  from their registered formulas in g56_lib.py.
- TENSOR: the metric is g_tt = -N(r)^2, g_tx = -beta*S(r)
  (beta = 1.1), gamma_ij = delta_ij + (M(r)-1) n_i n_j,
  r = |x|. ALL first and second metric derivatives are
  derived SYMBOLICALLY from this metric with sympy
  (Cartesian coordinates; r = sqrt(x^2+y^2+z^2); profiles
  as functions of r), lambdified to numpy and to mpmath
  (g56_build_tensor.py generates g56_tensor.py). The
  Christoffel -> Ricci -> Einstein contraction is the
  gate's own einsum assembly in g56_lib.py. This is the
  layer where the lineage's hand-derived content lives
  (its ddv / dd-gamma formulas); the gate derives it.
- TETRAD: the gate's own ADM construction of the Eulerian
  orthonormal frame from its metric (lapse from g^tt,
  shift from g_ti, triad from the spatial metric).
- MARGINS: the gate's own implementation of the
  Hawking-Ellis eigenvalue margins (mixed-tensor
  eigenvalues; Type-I test by eigenvector eta-norm) and,
  for non-Type-I points only, of the registered sampled
  fallback (162 Fibonacci dirs, velocities linspace(0,
  0.95, 6)) — the SAMPLER-M definitions, independently
  coded.
- WORST-NULL: the gate's EXACT solver for the
  quadratic-on-the-sphere problem min_|n|=1 k^T That k,
  k = (1, n): the secular equation ||n(lam)|| = 1,
  n(lam) = -(A - lam I)^{-1} f, lam <= lambda_min(A), with
  the KKT certificate (A - lam I positive semidefinite,
  stationarity residual, unit-norm residual). Corroborated
  by the registered fib(642) scan + Nelder-Mead polish,
  both re-implemented. The secular value is the gate's
  deciding worst-null.
- SET READ: SET-244 as registered (41 radial midpoint
  nodes x 162 Fibonacci dirs; the gate's own fib_dirs from
  the registered formula), joint = min(NEC min, DEC min).
- ADVERSARY POLISH: the registered protocol (Nelder-Mead
  in (r, theta, phi) from the read's 5 lowest Type-I SET
  points, maxiter 300, xatol 1e-4, fatol 1e-7, objective =
  point NEC if Type-I else NEC + 1) on gate machinery.
- PEAK: dense scan, 20,001 radii on [10, 20], of |beta*S|
  from the gate's spline, plus the FINE_R (401-point) read.
- SPOT CHECK: the screen-1347 NEC argmin point re-evaluated
  end-to-end in 50-digit mpmath (profiles, derivatives,
  tensor, tetrad, eigenvalue NEC margin, secular
  worst-null).

## SS3 — Calibrations and controls (run BEFORE claim reads)

CAL-1 spline solver vs scipy CubicSpline(not-a-knot) on the
stored A2/H2/B418 vectors: value/1st/2nd derivative max
diffs on a dense grid (expect <= 1e-11).
CAL-2 gate assembled profiles vs the lineage's
profiles_at414 at scattered points for the control
configurations (expect <= 1e-12 abs).
CAL-3 gate tensor vs verify_metric.einstein_at_points (FD)
at scattered points of a control configuration (agreement
at FD accuracy), and vs the lineage T_from_SNM on the
control SET points (expect <= 1e-11 abs).
CAL-4 gate tetrad + That vs verify_metric.eulerian_that on
the control SET points (expect <= 1e-13 abs).
CAL-5 gate margins vs margins_chunked on Type-I and
non-Type-I control points (expect <= 1e-12 on Type-I;
sampled-fallback agreement reported as found).
Controls (gate machinery, VM; stored targets):
CTL-405WIN 400 base + G50 knots: joint
+1.2273852081052888e-6, NEC argmin r 17.926829268292682,
worst-null +7.282191364112375e-7, polish
+1.214723699102956e-6, SEC -2.213557e-4 (record value).
CTL-PSTAR 412 P*: joint +6.699288757141148e-7, worst-null
+1.657750767723178e-7, SEC -2.917201236465074e-4.
CTL-B1T1 B1 + its T1 winner (K_S = 17): joint
-4.60458433226168e-6, worst-null -4.666009738694515e-6.
CTL-400STAT static 400 base: +1.3977194851281464e-6.
CTL-B1STAT static B1: +6.257021665543401e-6, SEC
-7.149443971550401e-4.
CTL-H2 static H2 centre (muN = muM = 1, zero corrections):
joint = NEC_H2 = -1.9422459891767227e-4 (p381_lib record).

## SS4 — Verdict bars

A claim SURVIVES if the gate's deciding read reproduces the
stored value to <= 1e-9 absolute on joints/margins at the
1e-6 scale (the C-10 / admission class of this lineage:
Gates 50/52/54/55 reproduced at diff 0.0 to 5.5e-19 on
their deciding reads; any diff > 1e-9 is reported as found
and ruled on). The peak ruling follows G52-R1's form. The
2x negative is ruled search-scoped per G52-R2 regardless of
read agreement. The transect/binning audit is a recount:
the stored table must reproduce exactly from the jsonl,
and the gate's re-reads of the 12 stored configurations
must meet the same bar.

## SS5 — Deliverables

gate56/GATE56.md (quotable claim set SS1 with riders),
gate56/GATE56_CHECKPOINT.md (machinery, calibrations,
controls, reads, admission, incidents), gate56/results/
(g56_controls.json, g56_reads.json, g56_spot.json,
g56_admission_*.json). No ledger append, no publication.

## SS6 — Admission control

The gate's endpoint read (the screen-1347 SET read) is run
on the laptop pool from a minimal mirror (gate lib + the
three stored-vector artefacts + the generated tensor
module); VM deciding values compared against the laptop's.
Route: SSH per the standing pool instructions; work dir
/home/spark/work/gate56. If the pool is unreachable the
admission is reported NOT RUN with the observed reason;
deciding reads remain the VM's.
