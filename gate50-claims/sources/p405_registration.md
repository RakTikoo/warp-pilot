# PHASE 405 REGISTRATION — W15: CHEAP-SHIFT SHAPES
# ON THE STATIC WINNER'S BASE

Filed before any computation. Charge: ledger
entry 1043 (Rakshit's direction: "let's get this
one moving at ftl then let's see").

## SS0. The act

Phase 400's corrected static base (S ≡ 0, joint
+1.397719×10⁻⁶, Gate-48 re-judgement running
concurrently) at the β = 1.1 pose. N/M held at
400's winner verbatim. The S sector — the slot
398's machinery zeroed and 400 inherited — is
opened as a FREE SPLINE SHAPE (p341's correction
spline family: not-a-knot C2 cubic through K knot
values uniform on [10, 20], K = 9; K = 17 gated,
SS5-E). The shape is searched to MAXIMISE the
peak |β·S| subject to the joint (SET-244, band
[10, 20], the lineage's joint min(NEC, DEC))
remaining ≥ 0 — equivalently, to minimise the
NEC cost per unit peak shift. Phase 404 measures
the FIXED shape's price on this same base
concurrently (its ladder is stored:
phase404/results/p404_ladder.json); this phase
does not duplicate that ladder — it cross-checks
one ladder point as a control (SS3 CTL-405-FIX)
and uses the ladder as the same-base fixed-shape
comparison (SS1).

## SS1. Stored bars and priors

- THE BASE (400's confirmed winner, stored in
  phase400/results/p400_confirmation.json):
  base (μ_N, μ_M) = (2.330448313835416,
  11.343911464156438), K = 17, vN/vM as stored
  (verbatim copies in p405_lib). Joint =
  +1.3977194851281464×10⁻⁶ at
  r = 17.682926829268293; worst-null at the
  argmin identical; SEC min =
  −2.0502915986749415×10⁻⁴; ρ_min =
  9.943380734109653×10⁻⁵; Type-I fraction 1.0000.
- L_stat(H2): the (1, 1, 1) read (p394_lib
  H2_TG; NEC = −1.942246×10⁻⁴ class value,
  reproduced exactly by CTL-405-H2S).
- C395 = (0.601180962300002, 1.5934531363763935,
  4.887238651223381); stored TG in p398_lib
  (NEC −2.9809850277749006×10⁻⁵; worst-null
  −3.0896210095678075×10⁻⁵).
- THE FIXED SHAPE ON THIS BASE (404's stored
  ladder, p404_ladder.json): break-even
  μ_S* = 0.171875, bracket [0.171875, 0.175];
  joint(0.171875) = +1.4352780045877611×10⁻⁸;
  joint(0.5) = −9.1860984150769×10⁻⁶ at peak
  0.4427 (the criterion amplitude); measured
  cost at μ_S = 0.5: 1.0583817900205046×10⁻⁵;
  shortfall to warp-grade 9.1860984150769×10⁻⁶.
  The fixed shape's achievable peak at joint
  ≥ 0 is its peak at μ_S* (read exactly in
  CTL-405-FIX; ≈ 0.1522).
- THE WARP CRITERION (SS7): peak |β·S| ≥
  0.4426742490267404 (= 0.5 × H2's peak
  0.8853484980534808) at joint ≥ 0.
- PRIORS (context, not bars): 397's carried law
  on the ridge base, A_c = 2.3255901039892218×10⁻⁵,
  p = 2.15556441798475; 401's implied A_c ≈
  3.66×10⁻⁵ for C395's shape on 398's base —
  the fixed shape's price is base-dependent;
  a free shape counts as paying only per SS6.

## SS2. Frame

VM is the frame of record. The laptop admission
control (the lineage endpoint read, p389 form,
as in 398/400/401) is run and followed: if
ADMITTED, deciding reads are nevertheless all
VM reads (the search compares levels at
10⁻⁷–10⁻⁹ increment scale; one frame carries
every point — the 397/398/400 precedent).

## SS3. Controls (all diff 0.0 before any search
read is believed)

- CTL-405-WIN: p405's own assembly at vS = 0
  (K = 9 and K = 17 zero vectors) reproduces
  the winner: the five minima (nec, dec, wec,
  sec, rho) and the exact worst-null at the
  SET NEC argmin at diff 0.0 vs SS1; max |S|,
  |S′|, |S′′| over the SET grid = 0.0 exactly.
- CTL-405-H2S: (1, 1, 1) → L_stat(H2) via the
  lineage machinery (p398_lib constants /
  p394_lib read), five minima at diff 0.0.
- CTL-405-C395: the C395 triple → its stored
  TG (five minima) and worst-null at diff 0.0.
- CTL-405-FIX: the fixed-shape control on this
  base — p404_lib.profiles_at404 read through
  p405's SET read at μ_S = 0.5 and
  μ_S = 0.171875, compared against
  p404_ladder.json's stored rows (joint, nec,
  dec, wec, sec, rho, peak |β·S|) at diff 0.0.
- CTL-405-ADM: the laptop admission read
  (SS2), compared against the VM endpoint
  record.
- The frozen base's inherited floors: the
  winner's N/M positivity floors (p398_lib
  positivity_ok398 at the winner) verified
  once in CTL-405-WIN; N/M never move in this
  phase, so the floors cannot move.

## SS4. The assembly and the reads

profiles_at405(vS, K, pts): the N/M sectors are
p398_lib.profiles_at398 at the winner's stored
configuration, verbatim; the S sector is
_eval_corr(CubicSpline(knots(K), vS,
bc_type='not-a-knot'), r) — p341's correction
spline in the slot 398 zeroed, on a base S ≡ 0.
T via p316_lib.T_from_SNM at BETA = 1.1.
set_read405 / nec_at405 / adversary_polish405 /
worst_null_at405: p398_lib's read forms verbatim,
assembly swapped (the p404_lib construction).
Peak |β·S|: the phys-row form (FINE_R x-axis,
401/404 form). Feasibility of a screen: C1 —
the SET read's ρ_min > 0. (No S floor exists in
the lineage; the N/M floors are frozen per SS3.)
Sampled minima name their frame convention
(SAMPLER-M, the lineage's eulerian_that
association, Gate-43 C-10); deciding values are
diff-0.0 reproductions, frame-invariant
worst-nulls, and bracket joints at registered
amplitudes.

## SS5. The search

PARAMETRISATION. Shape = knot vector vS ∈ R^K,
box |vS_i| ≤ 1.0. S is exactly linear in vS
(spline of scaled knots = scaled spline), so a
shape's amplitude is set by scaling: for target
peak P_t, vS is scaled by P_t / P(vS), where
P(vS) = max over FINE_R of |β·S| (x-axis spline
evaluation); the scaled shape's peak is P_t up
to float rounding, verified per screen by the
read's phys row.

OBJECTIVE at fixed P_t: score(vS) =
joint(SET read at the scaled vS) − PEN400(vS_scaled),
PEN400(v) = LAM400 × rough(v), LAM400 = 1.0×10⁻⁵
(= LAM_REG × 10⁻³, Phase 400's rescaled penalty;
rough = Σ(second differences)², the S sector of
p341_lib.penalty3 / LAM_REG). Incumbent
semantics (379/398/400): best score among
C1-feasible screens; the pure joint is recorded
for every screen.

STAGES.
- A (reference curve, K = 9): the seed shape
  vS^H2, H2's total S sampled at the 9 knots
  (the fixed shape embedded in the spline
  family — an interpolant, labelled as such,
  NOT a diff-0.0 object), read at peaks
  {0.10, P_fix (404's exact peak at μ_S*),
  0.20, 0.25, 0.30, 0.35, 0.40,
  0.4426742490267404}. 8 screens.
- B (walks at the criterion, K = 9): at
  P_t = 0.4426742490267404, coordinate-descent
  sweeps on the unscaled shape (per-knot steps
  0.05, 0.02, 0.008, both signs, renormalised
  per screen) + Nelder-Mead polish on the
  score, seeded from vS^H2 and restarted from
  the stage incumbent. Stage cap 400 screens.
- C (walks at mid peak, K = 9): at P_t = 0.25,
  the same pattern, seeded from vS^H2 and from
  Stage B's incumbent shape. Stage cap 300
  screens.
- D (cost curve + break-even): the best two
  shapes by stage score (one per distinct
  stage lineage) are each read at ≥ 5
  amplitudes spanning [0.05, the largest stage
  peak]; the break-even peak P* (the joint's
  zero crossing) is bisected to a tolerance
  of 0.005 in peak where the measured curve
  is monotone. The phase's BEST SHAPE is the
  one with the larger P*. Cap 80 screens.
- E (K = 17, GATED): runs iff the K = 9 best
  P* < 0.4426742490267404. Warm start: the
  K = 9 best shape's spline interpolated onto
  17 knots; walks at P_t = the criterion (cap
  250 screens), then Stage D repeated for the
  K = 17 incumbent (cap 80). 

TOTAL CAP: 1100 stored screens (400's cap).
Every screen is stored (jsonl) with its stage,
its scaled and unscaled vectors, its peak
(phys-row), joint, five minima, binding sites,
penalty and score; C1-infeasible screens are
stored as rejected with the reason. No hidden
reads.

CONFIRMATION of the best shape: at its
break-even amplitude (scaled vector frozen),
and — if the criterion is reached — at the
criterion amplitude: full SET re-read
reproducing the stored screen at diff 0.0;
adversary polish; exact worst-null at the SET
NEC argmin; SEC minimum on the face; Type-I
fraction; binding sites and the locals at the
argmin.

## SS6. Verdict mapping

- SHAPE PAYS: the confirmed best shape has an
  amplitude with peak |β·S| ≥ 0.4426742490267404
  at joint ≥ 0. GATE REFERRAL of the
  re-introduced claim set, noting Gate-48's
  pending verdict on the base.
- SHAPE HELPS BUT SHORT: best P* <
  0.4426742490267404. P* stated with its
  bracket; the gap stated in peak terms and in
  level terms on this base's own curve (the
  confirmed joint at the criterion amplitude
  of the best shape). Whether P* beats the
  fixed shape's achievable peak (SS1) stated
  on the face.
- COST-BOUNDED: the 1100-screen cap binds
  before the stage pattern completes; the
  state of the search reported as it stands.

## SS7. Fences

Band pose [10, 20] only; 356's full-extent
caveats travel (no full-extent read of any
re-introduced configuration is claimed).
Gate-48's verdict on the base governs: any
positive result here is a candidate until the
base is gate-confirmed, and member language
waits for a gate of the re-introduced set
itself. The level is the lineage's joint
min(NEC, DEC); SEC — outside that joint at
every point of this line (the base's own SEC
is −2.050292×10⁻⁴) — is reported at the best
point and along the cost curve, on the face,
never hidden. No EC pass and no member by
verdict name. No sustainment, front or
transport content. DESK line in the memo.
