# Warp Pilot — Checkpoint

## MISSION HIERARCHY (Rakshit, 2026-11-21 02:10 PT — pinned)
"Goal is to find something new — new physics. And finally FTL or
practical, btw, [at the] speed of light."
1. PRIMARY: find something genuinely NEW — new physics (a verified
   configuration, mechanism, or exclusion not in the literature).
2. TERMINAL OUTCOMES, in order: (a) FTL — a superluminal candidate
   surviving the full gate protocol; or (b) PRACTICAL AT/NEAR LIGHT
   SPEED — the lightest verified design at the highest reachable
   fraction of c (the Track L/P frontier pushed as far as it goes).
3. Everything else (ledgers, exclusion maps, patterns) serves 1-2.
Interim reports state which rung each result serves. Standards,
gates and the sequencing lock are unchanged.

## Rules in force
- Python/NumPy only, no MATLAB. float64 everywhere (JAX x64 confirmed ON by
  default in warpax's jax 0.12.1; verified 2026-11-20).
- Replication/audit/ledger = calibration & tooling. Goal = NOVEL result or a
  bounded verified exclusion map.
- Direction update (Rakshit, 2026-11-20, "Get a Nobel — try it, why not"):
  superluminal lens is DEDICATED and equal-effort, outside SSV scope only,
  velocities 0.5/0.9/1.0/1.1/2.0, extraordinary bar, candidate must name its
  SSV escape route, search volume logged here.

## FAILURE PROTOCOL (Rakshit, 2026-11-21 05:26 PT — STANDING RULE,
## binding on every track incl. running ones)
"Don't give up if something fails — try to see why, and try more
experiments."
- F1 DIAGNOSE BEFORE CLOSING. No row closes on "it failed" alone:
  every failure gets an anatomy — WHERE it fails (site/structure),
  WHAT binds (condition/term/mechanism), HOW it scales (mass,
  velocity, size, coupling, resolution). The Patterns section is
  the model: every closed row adds a pattern or cites one.
- F2 EVERY DIAGNOSIS GENERATES EXPERIMENTS. Each anatomy proposes
  >= 1 follow-up the mechanism itself suggests. Run the ones
  computable within the track's engine; log the rest with what
  they would need.
- F3 STOP ONLY ON STRUCTURE, NOT ON SCORES. Closure requires the
  diagnosis to show the failure is STRUCTURAL (adversarial
  saturation; monotone anti-alignment across the full coupling
  range; a wall located from both sides) AND the closing entry
  must state the structural evidence AND what would reopen it.
- F4 RETRO-APPLY LIGHTLY. Closed rows whose pattern citations
  (P5/P7/P8/P9) already carry mechanism + saturation satisfy
  F1-F3; where a closed row lacks a reopening condition, add one
  line when next touched. Do not rerun closed work for bookkeeping.
- F5 Report failures WITH anatomy + generated follow-ups, at the
  same prominence as passes (rung-1 progress).

## QUEUE REORDER (Rakshit, 2026-11-21 05:23-05:24 PT)
N3 REVERSE-ENGINEERED GEOMETRY is promoted to HEADLINE (conditions
first, shape second — see Track N section) and runs immediately
after the X2 scan, ahead of X4/X5/S6/N1/N2/N4. TRACK B (free-form
3D blob, no imposed symmetry) is added as the second un-caged
track, queued after N3's first static results. X1 phi-extension
follows them. Interim reports flag N3/Track B results explicitly
as conditions-first / symmetry-free.

## Environment
- Python 3.12.3, numpy 1.26.4, scipy 1.11.4, sympy 1.12 (system).
- venv: einsteinpy 0.5.0, warpax 1.6.1 (pip install succeeded, one command).
  warpax exports certify / energy_conditions (Hawking-Ellis classification,
  frame-free certification) / geometry (ADM, autodiff Einstein tensor).
  JAX devices: CPU only. x64: enabled by default, float64 confirmed.

## Phase 0 — status
- [x] verify_metric.py: NumPy FD Einstein tensor (WarpFactory logic),
      Eulerian tetrad, Hawking-Ellis eigenvalue margins (all observers).
      Minkowski smoke test: max|T| = 2.2e-17, Type I everywhere, margins 0.
- [x] symbolic_alcubierre.py: SymPy exact Eulerian density for Alcubierre =
      -v^2 (y^2+z^2) (f')^2 / (32 pi r^2); difference from Alcubierre 1994 /
      Pfenning-Ford Eq. (8) simplifies to EXACTLY 0; numeric check 0.0.
- [x] Fuchs baseline extracted from primary paper (see TARGETS.md):
      R1=10 m, R2=20 m, M=4.49e27 kg CONFIRMED (§3); beta_warp=0.02 (§4.1)
      CORRECTS the report's ~0.04c (that is Table 1's comparison speed).
- [x] Pfenning-Ford anchors from primary paper: Eq. (26)/(28)
      E = -(v^2/12) int r^2 (f')^2 dr; ~1/4 M_sun at R=100 m, Delta=1 m;
      ~-3e20 galaxy masses at QI wall (Eq. 31).
- [x] calibration.py COMPLETE (results/calibration.json). PHASE 0 = PASS:
  * Judge unit tests 5/5 (perfect fluid passes; Eulerian-positive-but-NEC-
    violating tensor rejected; large-flux Type-IV tensor flagged, sampled
    NEC -1.98; dust passes; negative density fails WEC).
  * Alcubierre FD vs analytic rho: median rel err 28.5% (h=0.375) -> 10.8%
    (0.25) -> 4.0% (0.1875) -> 0.90% (0.125); min NEC stable at -0.065 ->
    -0.069 -> -0.070 -> -0.070 (sampled Type-IV scale, sign rigorous);
    NEC violations 97.6-98.2% inside the wall at full-audit resolutions.
  * KEY PHYSICS FINDING: the exact Alcubierre tensor is Hawking-Ellis
    Type IV at generic wall points (complex eigenvalues, SymPy-confirmed);
    Type I only at symmetry points (equator NEC exact -0.00964; point
    auditor at h=0.05 gives -0.00960, That00 exact to 5 decimals).
    => Judge rule: PASS requires Type I + eigenvalue margins > error;
    non-Type-I = fail (sign from sampled contractions).
  * Eigen vs sampled NEC sign agreement: 14/14 clear Type-I points.
    Magnitudes differ by null-normalisation (eigenframe vs Eulerian k0=1);
    brute-force sphere optimisation matched sampled values. Documented in
    calibration.json.
  * Van den Broeck: violations reproduced (min NEC -0.261 in wall),
    matching WarpFactory's published qualitative result.
  * Fuchs base shell (exact 1D, constant profile, our Gaussian smoothing
    s_rho=1.5, s_P=0.87): PASSES all ECs in shell, min margin +2.9e-6 (SEC),
    rho_peak 1.131e-4 (analytic 1.137e-4), max |p_t|/rho = 0.557.
    Unsmoothed constant shell FAILS DEC (headroom -23) — Fuchs's stated
    edge/hoop-stress problem, reproduced.
  * float64 audit: grep over all pilot .py — no float32/16 anywhere.
  * warpax notes: certify() as configured was under-resolved (eigenvalues
    ~1e-27 = vacuum noise) — inconclusive, not used as evidence.
    warpax WarpShellPhysical is a potential-based construction with rho~0
    at mid-shell — NOT a faithful Fuchs S3 shell; not used as a Fuchs
    cross-check. warpax will be used at finalist stage via a custom
    MetricSpecification of OUR metric (autodiff = independent path).

## Phase 1 — QI ledger COMPLETE (results/qi_ledger.json)
- PF anchor 1: R=100 m, Delta=1 m, v=1: piecewise -0.564 M_sun; tanh
  (Delta_eff=1.5 m) -0.376 M_sun; PF claim "order of a quarter solar mass"
  -> reproduced within a factor ~2.
- PF anchor 2: QI wall Delta=100 v L_P: -3.47e20 galaxy masses vs PF
  Eq. (31) -3e20 -> reproduced within 16%.
- Scaling exponents fitted: v^2.000, R^1.97, Delta^-0.96 (theory: 2, 2, -1).
- VdB: v5 abstract "few solar masses" total negative (E_II,-=-1.4e30 kg,
  E_IV=-6.3e29 kg quoted from his Eqs. 9/15); v4's "grams" was corrected.
- Casimir: rho(1 um) = -4.3e-4 J/m^3; warp scale (c^4/8piG)/R^2 at R=1 m
  = 4.8e42 J/m^3; gap ~46 orders of magnitude (research report's ~1e35 /
  ~38 orders is arithmetically inconsistent with its own formula; even
  its smaller figure leaves >= 38 orders).

## Search volume log
- Stage A (exact 1D base-shell screen): 330 shells (5 masses x 11 profile
  kinds x 6 smoothing pairs), R1=10, R2=20. All smoothed profiles pass the
  base-shell ECs; headroom best at low M (weak field) — Stage A ranks
  construction quality only; shift tolerance is decided in Stage B.
- Stage B (shell + beta_w=0.02, N=41 grid screening): 42 configs. Grid FD
  error at h=1.5 is ~2e-5 — LARGER than the margins at play; Stage B's
  near-zero negatives were grid artefacts. Point auditor is the arbiter.
- Stage C (point-auditor optimisation, fixed + extended samples):
  * Fuchs-replica family (constant/smoothbox, Fuchs shift): passes at
    Fuchs mass (worst +2.0e-5, h-stable), fails at M=3.0 / beta=0.03.
  * Edge-peaked density + Fuchs shift: passes at M=2.7 (+1.6e-5 core).
  * RETRACTED: tanh-shift "passes" at M<=2.4 (Stage C5-C7 first pass) —
    the extended radial sample (r from 4) found NEC~-4e-6 violations and
    non-Type-I pockets in the INTERIOR from the tanh tail's shift
    gradient. Lesson recorded: audit the whole volume, always.
  * Cosine shift (compact support on [10,20], max slope 0.157/m < Fuchs
    0.2/m, zero slope at edges, exactly flat inside/outside): passes at
    M=2.0 (beta=0.02) and M=2.4 (beta=0.03); M=1.6/1.7 pass (tail-limited
    +1.7e-7), M=1.5 fails (SEC -9.3e-6 @ r=10.5); beta=0.04 fails at M=2.4
    and beta=0.05 fails at Fuchs mass. Failure site is consistently the
    inner shell edge r~10.5.
  * Margin subtlety: Gaussian smoothing leaks the shell inward (m(9)=0.02);
    far-tail margins -> 0+ with fraction ~1 (dust-like tail). Verdicts use
    margins paired with per-point FD-error estimates, not absolutes alone.
- Superluminal lens SL-1 (generalised lapse/conformal/shift bubbles,
  R~1.5 m): 5 velocities (0.5, 0.9, 1.0, 1.1, 2.0) x (24 random + 1
  Natario control) at N=33. ALL fail at order-unity margins (~-1.0),
  best no better than controls. Bounded exclusion, no near-misses.
- Superluminal lens SL-2 (finalist shell family, cos shift): beta in
  {0.1..1.5} x M in {2.0, 5.0, 8.0} (compactness up to 0.8): ALL fail,
  NEC -1.4e-4..-3.3e-3, Type-I fraction ~0.4, worst at r=10.5. Shell
  family velocity ceiling beta ~ 0.03-0.04. Bounded exclusion.

## Finalists (full verification in results/finalist_*.json)
- A: M=2.0 m geom = 2.69e27 kg (1.42 M_jup), beta=0.02, edge-peaked
  density (wd=3, floor=0.2), Gaussian smoothing (2.0, 1.16), cosine shift.
  => 40% below Fuchs mass at the same radius and velocity. VERIFIED:
  dense audit (2210 pts) core margins +1.20e-5..+1.28e-5, Type I 100%,
  h=0.3/0.15 agree <1%; grids N=81/121 Type I 1.000; warpax autodiff
  cross-check NEC +2.12139e-5 vs FD +2.12140e-5; photon asymmetry
  5.31 ns; ADM fit 2.00000021 vs 2.0; QI negative energy ~0 (FD noise).
- B: M=2.4 m geom = 3.23e27 kg, beta=0.03, same family. **CORRECTION
  (supersedes earlier listing): B FAILED its dense audit** — coarse
  screen and warpax spot-check passed, but the 2210-point audit finds a
  genuine violation pocket at r=10.25, direction (-0.13,0.97,-0.19):
  core NEC -2.1e-6 (h=0.3) worsening to -5.6e-6 (h=0.15), SEC -4.9e-5.
  B is NOT a verified candidate. Lesson: coarse samples miss pockets;
  dense whole-volume audit is the arbiter.
- B2: M=2.7 m geom = 3.64e27 kg (1.92 M_jup), beta=0.03, same family.
  VERIFIED with the full protocol: dense core margins +1.20e-5..+1.28e-5,
  Type I 100%, h-agreement <0.02%; grids Type I 1.000; warpax NEC
  +2.86446e-5 vs FD +2.86448e-5; photon asymmetry 8.97 ns; ADM
  2.70000029; QI negative ~0. => 19% below Fuchs mass AND 50% higher
  velocity than the Fuchs shell.
- B3: M=2.4, beta=0.025 passed the dense audit only (core +1.1e-5);
  dominated by A (mass) and B2 (velocity); not fully verified.

## Track L — mass-velocity frontier (named families; results/trackL_b*.json)
Edge-peaked density + cosine shift on [R1,R2] unless noted. Min confirmed
mass = passes dense audit at h and h/2, Type I 1.000.
- beta=0.02: M_min = 2.0 geom at (10,20) [Finalist A]. beta=0.03: 2.7
  [B2]. beta=0.025 at M=2.4 passes (dense audit).
- beta=0.05 (141 evals): PASSES. Min compactness M/R1 = 0.383 at every
  W=R1 geometry: (5,10) M=1.91 geom = 2.58e27 kg (1.36 M_jup), worst
  +5.9e-7; (10,20) M=3.84 = 5.17e27 kg, worst +1.5e-7; (20,40) M=7.65,
  worst +3.7e-8; (30,60) M=11.48, worst +1.6e-8. Margins scale as 1/R^2
  (exact GR scale covariance — smaller shells are lighter in kg AND
  have larger margins; the invariant frontier is compactness vs beta).
  Also: (10,30) with wide window ws=[5,35] confirmed at M=4.5 (+2.4e-8);
  two (10,30) ws=[10,30] candidates FAILED h/2 confirmation (flipped
  negative) — pipeline anti-artefact behaviour working as designed.
  Shift windows extending outside the shell matter fail catastrophically
  (DEC -1.0 where the gradient sits in vacuum).
- beta=0.1 (124 evals): EMPTY for named families. Closest: (10,30)
  thick shell, M=10 (compactness 1.0), edge-peaked/cos: worst -2.06e-7
  (NEC @ r=18.8 mid-shell), Type I 0.996. All other geometries <= -7e-5.
  Free-form (Track P): also empty under verified standards, boundary
  located to 1e-9 at M/R1 = 1.0 — see Track P section.
- beta=0.2 / 0.35 / 0.5 / 0.7 / 0.9 (124 evals EACH, named families):
  ALL EMPTY. Every row fails; the best NEC margin in each rung sits
  at the largest geometry (30,60), M=21, and degrades smoothly with
  beta: -1.18e-5 (0.2), -2.07e-5 (0.35), -3.56e-5 (0.5), -5.42e-5
  (0.7), -6.34e-5 (0.9). Worst margins saturate the -1.0 sampled
  floor (DEC at exterior window points and non-Type-I pockets —
  at these speeds the failure is not marginal anywhere in the
  design space). FRONTIER SUMMARY (named families + free-form):
  the positive-energy shell frontier TERMINATES between beta=0.05
  (passes at compactness 0.383) and beta=0.1 (boundary at
  compactness ~1.0, no verified interior point). Higher rungs are
  excluded by wide margins, not near-misses. Serves hierarchy
  rung 2(b): the lightest verified design at the highest verified
  speed is the beta=0.05 frontier (2.58e27 kg at (5,10)); the
  practical near-c frontier of this family is mapped end to end.

## Track F / MG-1 — f(R) = R + alpha R^2 (results/mg1_stage1.json,
## mg1_stage2.json, mg1_fd_check.json, mg1_controls.py, mg1_symbolic_check.py)
Engine: JAX autodiff (x64) on the generalised ADM ansatz (Gaussian
lapse/conformal bumps, Rodal irrotational shift + vorticity admixture
eta). T_matter from Lobo arXiv:1112.6333 Eqs. (2)-(5) (verified against
primary text; algebraically identical to the brief's formula).
Validations: Minkowski exact 0; Alcubierre limit reproduces SymPy
That00=-0.00492, NEC=-0.00964 exactly; AD vs FD Einstein on a random
metric 2.7e-10; SymPy-vs-JAX symbolic slice check (static spherical,
alpha=0.7) agrees to 6 decimals at 5 radii; alpha=0 identity vs FD
auditor (NEC -5.9158 vs -5.8902); Fuchs-shell known-yes control through
the f(R) chain at alpha=0: NEC +2.121389e-5 vs verified +2.12140e-5.
METHODS FINDING: sample points must exclude the exact origin — a
Gaussian bump's exponentially small nonzero slope at r=0 makes bump(|x|)
only C0 at the centre and 4th-order AD amplifies the cusp into a fake
R~1e7 spike. First scan run was polluted by this; discarded and rerun
with innermost sample radius 0.1R (cusp contribution <1e-3 of wall
scales there). All numbers below are from the clean rerun.
SCAN VOLUME: Stage 1: 7 amp pairs x 6 velocities (0.3..3.0) x
alpha-hat in {0, 1e-3, 1e-2, 1e-1, 1, 10} + negative-alpha diagnostics
= 260 evals (R=1, Delta/R=0.25, eta=0). Stage 2: 256 evals (Delta/R in
{0.1, 0.5}, eta in {0.1, 0.2}, extreme amps +-0.5, R=3, finer alpha-hat
{0.03, 0.3, 3}, v in {0.5, 1.2}). TOTAL 516 evals, ~101 sample points
each. RESULT: ZERO passes. No config has worst matter margin > 0.
Margins are alpha-insensitive for alpha-hat <= 1e-2 (smooth-perturbation
consistency) and degrade monotonically for alpha-hat >= 0.1 at every
velocity and amplitude; best normalised margin J = worst/|T_eff| =
-0.85 (thin wall Delta/R=0.1, alpha-hat=0.03) — still an order-unity
relative violation. F>0 side-gate: F_min >= 0.94 in all non-diagnostic
rows (gate not the binding constraint). Negative-alpha diagnostics also
fail (and hit F<0 at alpha-hat=-1, as expected for the unstable branch).
G1 second engine (nested FD + Richardson, mg1_fd_check.py): at 4 wall
points in 2 moving alpha!=0 configs, FD NEC agrees with AD to <2% at
3 points (-0.965/-0.965, -0.642/-0.634, -0.324/-0.305) and in sign at
the sharpest wall point (-5.41 AD vs -1.31 FD; FD is the cruder engine
there; both deeply negative). Verdict confirmed by two engines.
G6 note: no candidate exists, so no Einstein-frame cross-examination
was triggered; the exclusion makes it moot for this family. G5/G7:
alpha->0 controls reproduce the GR failures (J=-1.14 plateau) and the
Fuchs shell reproduces as known-yes (above).
MG-1 CONCLUSION: bounded exclusion — the f(R) analogue of the GR shell
ceiling. Within this ansatz, the R^2 term moves matter margins the
WRONG way once alpha-hat >= 0.1; the pre-registered expectation
(flipping needs alpha-hat~1 with F varying O(1)) is confirmed in
direction but the flip never arrives — margins at alpha-hat=1..10 are
the worst in the grid. The seam (classical modified gravity supplying
the convergence violation while matter obeys all ECs) is NOT realised
by metric f(R)=R+alpha R^2 on this ansatz family.

## Track F / MG-2 — f(Q) = Q + beta Q^2, symmetric teleparallel
## (results/mg2_scan.json; mg2_fq.py, mg2_scan.py) — CLOSED
DEFINITION CHOICE (De & How vs Mandal et al. dispute): the two camps'
Friedmann equations for the actual matter (rho, p) agree; they differ
only in which extra terms are booked into "effective" density/
pressure. This lens therefore audits T_m obtained by SOLVING Zhao's
covariant field equation (Mandal et al., arXiv:2208.13636, Eq. (2))
for the matter tensor — the object both camps agree on — with the
(Q, P) pair in Mandal's sign convention (Q_FLRW = +6H^2, their
Eq. (8)); the JHK pair is the overall sign flip and gives the same
T_m. Effective margin = the GR judge's NEC on G/8pi (must be negative
somewhere or the geometry does no warp work).
VALIDATIONS: V1 FLRW anchor Q = +2.939995 (expect 6H^2 = 2.94 at
H=0.7). V2 beta=0 identity: max|T_m - G/8pi| = 0.0 EXACTLY. Zhao vs
Mandal divergence form at beta=0.05: agree to 2% at interior points,
22% at the sharpest wall point (nested-FD error in the divergence
form; Zhao is primary). V4 shell known-yes: Finalist A metric through
T_m at beta=0 gives NEC min +2.1214023e-5 vs verified +2.12140e-5.
c_T gate (D2): f(Q) STEGR propagates tensors at c identically —
inside the GW170817 window by construction.
SCAN (60 evals): same generalised ansatz as MG-1 (NumPy twin),
amps {(0,0), (0.3,0), (0,0.3), (0.3,-0.3)} x v in {0.9, 1.5, 2.0} x
beta-hat in {0, 0.01, 0.1, 1, 10} (beta = beta-hat/Q*, Q* = GR row's
Q_absmax), R=1, Delta=0.25, eta=0, ~120 pts/config. ZERO passes.
Best row: (0.3, 0) v=0.9 beta-hat=0.1, worst_m = -12.94 (WEC-bound;
NEC -1.33). T_eff does warp work (eff_nec_min < 0 in 45/60 rows) but
matter never obeys. beta-hat response mirrors MG-1: flat/slightly
improving to beta-hat=0.1 (-13.45 -> -12.94), then strongly worse
(-20.9 at 1, -160.5 at 10; at (0,0) v=2.0 monotone -374 -> -4330).
Wart (honest): eff_nec_min is NaN in 15/60 rows (the (0,0)-amps
groups — a sampled-fallback NaN in the effective-margin diagnostic);
all matter margins are finite, and at beta-hat=0 T_eff = T_m by
construction, so no verdict depends on the NaN rows.
MG-2 CONCLUSION: bounded exclusion. The seam is NOT realised by
f(Q) = Q + beta Q^2 on this ansatz family either. Combined with
MG-1: in BOTH quadratic-curvature/nonmetricity extensions, the extra
classical terms anti-align with the wall's NEC deficit once their
strength reaches the scale that would matter (Pattern P7). Serves
hierarchy rung 1 (verified exclusions not in the literature).

## Data bindings (Rakshit directive 2026-11-21 01:53 PT, clarified 01:55 PT)

PROVENANCE RULE: no gate number without a source. THREE-CASE RULE
(clarification, verbatim spirit): (1) CONTRADICTED BY DATA — where open
data / published measurements cover a claim and conflict with it, the
claim dies. (2) COVERED AND CONSISTENT — gates use the real measured
numbers below. (3) NO DATA COVERAGE — a mathematically established
result in a regime no experiment probes is a VALID finding, reported
labelled exactly: "mathematically established; experimentally untested
regime." Data informs (patterns, bounds, parameter values); it does not
veto case (3). The core warp audits (energy conditions on computed
metrics) are case (3) by nature — pure mathematics — and were never
data-gated.

- D1 COSMOLOGY (Lens E, X2, E3) — CASE 2. Planck 2018 legacy
  (Planck Collaboration, A&A 641, A6 (2020), arXiv:1807.06209):
  H0 = 67.4 ± 0.5 km/s/Mpc; Omega_m = 0.315 ± 0.007; Omega_Lambda =
  0.685 (flat). Dark-energy equation of state, Planck+BAO+SNe:
  w0 = -1.03 ± 0.03. E3 PHANTOM WINDOW (data-consistent): w in
  [-1.06, -1.00] (1-sigma lower edge); a phantom source with w below
  -1.06 is case (1) — contradicted at >1 sigma by this combination.
- D2 GRAVITATIONAL WAVES (MG-2, N2, any modified-gravity claim) —
  CASE 2. GW170817 / GRB 170817A (Abbott et al., ApJL 848, L13
  (2017)): -3e-15 <= c_T/c - 1 <= +7e-16. Any theory lens with
  c_T != c must fit inside this window or it is case (1), dead.
  (f(Q) STEGR has c_T = c identically — theory property, literature
  value; f(R) metric also propagates tensors at c.)
- D3 FIFTH FORCE / PPN / EQUIVALENCE PRINCIPLE (N1 gates, X4 moduli)
  — CASE 2. Eot-Wash torsion balance (Lee et al., PRL 124, 101101
  (2020)): inverse-square law verified down to 52 um separations;
  gravitational-strength Yukawa range lambda < 38.6 um (95% CL);
  largest-extra-dimension radius < 30 um. N1 GATE: compactification
  radius must be < 30 um (case 1 above that). Cassini: gamma - 1 =
  (2.1 ± 2.3)e-5 (Bertotti, Iess & Tortora, Nature 425, 374 (2003)).
  MICROSCOPE final (Touboul et al., PRL 129, 121102 (2022)):
  eta(Ti,Pt) = [-1.5 ± 2.3(stat) ± 1.5(syst)]e-15 — WEP holds at the
  ~1e-15 level; an unstabilised massless modulus coupling at
  gravitational strength is case (1). LLR Nordtvedt parameter
  |eta_N| <~ 4.4e-4 (literature value, not re-derived).
- D4 COLLIDER (N1 KK gates) — CASE 2. ATLAS 13 TeV combination
  (36 fb^-1, PRD 98, 052008 (2018)): bulk Randall-Sundrum KK graviton
  excluded below 2.3 TeV. ATLAS 7 TeV diphoton (PLB 710 (2012) 519):
  RS lightest graviton > 1.85 TeV at k/M_Pl = 0.1; ADD fundamental
  scale M_S > 2.27-3.53 TeV (n-dependent). N1 GATE FLOOR used:
  m_KK >= 2.3 TeV (conservative published floor; 139 fb^-1 searches
  are stronger — literature value, not re-derived).
- D5 LORENTZ VIOLATION / DISPERSION (any Track N LV proposal) —
  CASE 2. Fermi-LAT GRB 090510 (Abdo et al., Nature 462, 331 (2009)):
  E_QG > 1.2 E_Planck for linear (n=1) photon dispersion,
  E_Planck = 1.22e19 GeV. Linear Planck-scale dispersion is case (1).
- CASE 3 (explicit): all Phase 0-2 / Track L / Track P energy-
  condition audits; MG-1/MG-2 matter-vs-effective audits at wall
  curvature scales no experiment probes; Track N constructions in
  unprobed regimes. Label in reports: "mathematically established;
  experimentally untested regime."

## EXHAUSTION LEDGER (sequencing lock, Rakshit 2026-11-21 01:26 PT)
Final REPORT.md may be written only when every row is CLOSED (or Rakshit
calls a stop). No external contact of any kind during the pilot.
- Phase 0 verifier/calibration: CLOSED (passed, caveats logged).
- Phase 1 QI ledger: CLOSED.
- GR subluminal search Stages A-C + finalists A/B2: CLOSED (verified;
  B failed honestly, replaced by B2).
- SL-1/SL-2 superluminal GR lenses: CLOSED (bounded exclusion).
- Track L rungs: ALL CLOSED. beta=0.05 pass (frontier table);
  beta=0.1 empty (named + free-form, boundary located to 1e-9);
  beta=0.2/0.35/0.5/0.7/0.9 empty (124 evals each, best NEC
  -1.2e-5..-6.3e-5, no near-misses).
- Track P: beta=0.05 M=3.5 run 1 CLOSED (screen-artefact, arbiter
  caught it — logged); run 2 CLOSED (angular-pocket artefact, arbiter
  failed it — logged as negative); adversarial-training run CLOSED
  (NEGATIVE: objective never positive on 893 training pts, final
  fresh-seed verdicts -1.9e-4..-4.2e-4 — named floor 0.383 stands);
  beta=0.1 (10,30) free-form CLOSED (3-round split verdict; 5-round
  extension converged to the boundary — AD margins +1.3e-9 at M=10,
  uncertifiable; mass sweep M=11/12 DEC-fails; rung EMPTY with the
  boundary located to 1e-9 at M/R1 = 1.0 — see Track P section);
  X1 toroidal profiles OPEN; MG-1 profile space CLOSED by decision
  (P did not earn a verified pass at 0.05 or 0.1; its boundary
  location at 0.1 is the deliverable — no further MG-1 profile
  spend justified).
- MG-1 f(R): CLOSED (516 evals, bounded exclusion, two engines).
- MG-2 f(Q): CLOSED (60 evals, bounded exclusion; engine validated —
  FLRW anchor, exact beta=0 identity, Zhao/Mandal cross-check, shell
  known-yes; beta-hat response mirrors MG-1, Pattern P7).
- Red team R1/R2/R3 for A, B2, frontier_b005: R1 CLOSED, R3 CLOSED,
  R2 CLOSED (see below). R4 appendix: CLOSED (in REPORT.md,
  written at ledger completion, continuation session 3).
  R5: STANDING RULE for all future finalists.
  R2 RESULTS (redteam_sym3.py — SymPy derivation in spherical
  coordinates with the polar axis on the shift axis, genuinely
  axisymmetric form; Gamma and dGamma derived symbolically,
  lambdified, Ricci contracted numerically; 21 sample points per
  config at 3 orientations x 7 radii): symbolic vs FD margins agree
  at every point. Min NEC: A sym +1.891e-7 vs FD +1.877e-7; B2 sym
  +2.404e-7 vs FD +2.384e-7; frontier_b005 sym +1.496e-6 vs FD
  +1.481e-6. Max tensor diff 1.2e-6 (A), 2.0e-6 (B2), 1.4e-5 (b005,
  sharper scale) — ~1% relative. All margins positive on the third,
  independent path. (Two earlier R2 attempts are part of the record:
  the full-Cartesian simplify path was computationally infeasible,
  and the first spherical version had a profile-feed bug — the cos
  window's S'' evaluated outside its support — caught BECAUSE the
  shell points agreed to 1e-9 while flat-region points did not;
  fixed and rerun.)
  R1 RESULTS (JAX autodiff hunt, 192 restarts x 500 Adam steps each,
  NEC + WEC contractions over position x observer direction/boost,
  restarts seeded at audit-worst points; JAX path pre-validated vs FD
  auditor: NEC margins agree to ~6 figures at test points): the red
  team could NOT push any margin below zero — frac_negative = 0.0 in
  all 6 hunts. Worst found: A NEC +7.31e-6 / WEC +7.43e-6 (r=22.4,
  exterior tail); B2 NEC +8.59e-6 / WEC +8.82e-6 (r=22.5); frontier
  beta=0.05 NEC +1.04e-4 / WEC +2.29e-4 (r=7.57). Scope note: R1 hunts
  NEC and WEC (single contractions); SEC/DEC rest on the eigenvalue
  audits + R3 — stated as a limitation for the R4 appendix.
  R3 RESULTS (150 random points x 300 random observers per config,
  FD tensors): NEC and WEC sign agreement between eigenvalue margins
  and brute observer sampling = 1.000 for A, B2 and frontier_b005
  (143 significant points each); median sampled/eigen NEC ratio
  0.69-0.80 (sampling + normalisation effect; sign is the content).
- X1 toroidal shell: CLOSED (continuation session, 2026-11-21) —
  BOUNDED EXCLUSION for tube-symmetric (s-only) toroidal profiles.
  FULL RESULT: prescribed spherical profiles fail (worst SEC -1.67e-3,
  window-dominated; genuine inner-equator deficit -2.5e-5..-3.7e-5).
  Free-form DE (x1_de.py; 5,134 evals at EACH of Rmaj = 30/45/60,
  aspects 2/3/4; 17-gene a(s), b(s) splines, equator-emphasised
  screens): best static bases saturate at worst margin -1.59e-4
  (aspect 2), -2.12e-5 (aspect 3), -3.48e-5 (aspect 4) — Type I
  1.000, h-stable (arbiters at h=0.3/0.15 agree), i.e. NO legal
  static toroidal shell exists in this ansatz at any aspect tried;
  the residual deficit sits at the inner equator at exactly the
  analytically estimated scale (Pattern P9). ADVERSARIAL ROUND
  (x1_de2.py: DE retrained on the union of all three arbiter point
  sets, 1,020 pts, seeded at the winning genes): training objective
  saturates at -1.78e-5; fresh-seed finals -1.76e-5..-3.96e-5,
  Type I 1.000 — the deficit survives adversarial training, it is
  structural, not a sampling gap. VELOCITY LADDER (x1_ladder.py;
  best base x 3 aspects x v in {0.02, 0.05, 0.1} + S1 grid
  {0.5, 0.9, 1.0, 1.1, 1.5, 2.0, 3.0} = 30 rows): ALL FAIL. Any
  shift collapses Type I (1.000 at beta=0 -> 0.79 at v=0.02 ->
  ~0.47 at v>=0.5); NEC degrades monotonically with v at every
  aspect (-4.5e-5 @ v=0.02 to -4.6e-3 @ v=3.0, Rmaj=45). S1
  SUPERLUMINAL SUB-ROW: COMPLETE — toroidal superluminal fails at
  NEC -2.4e-3..-4.6e-3, Type I ~0.47-0.49, no near-misses.
  Named UNSEARCHED extension (honest scoping): cross-section-
  asymmetric (phi-dependent) profiles — the deficit lives at one
  phi and s-only profiles cannot answer it there; not attempted.
  EXTENSION IN PROGRESS (continuation session 3, x1_phi.py):
  a,b gain W(s)[a1(s) cos phi + a2(s) cos 2phi] corrections (28
  extra genes on the de2 winner's 17; window pins corrections to
  zero for s<=5 and s>=45 so cavity/exterior stay exact). Zero-
  correction control reproduces the s-only winner bit-for-bit
  (-1.777e-5). DE at Rmaj=45 running; arbiters + ladder (incl.
  v = 1.1/1.5/2.0) follow. Queue position: after N3 + Track B
  per the 05:23-05:24 reorder (run already in flight, not
  restarted).
  EXTENSION RESULT — CLOSED (continuation session 3;
  results/x1_phi_Rmaj45.json + x1_phi_ladder.json): bounded
  exclusion EXTENDED to phi-dependent profiles. Volume: 9,990
  (stage-1 DE) + 5,040 (stage-2 adversarial DE) evals + ladder
  (5 velocities x 2 seeds x 2 resolutions x 2,400 pts). Stage 1
  improved the s-only winner's screen worst -1.78e-5 ->
  -1.39e-5; stage-2 adversarial training saturated at -1.59e-5
  (finals: -1.60e-5/-1.92e-5 seed 555001, -1.59e-5/-1.92e-5
  seed 777001 at h=0.3/0.15, Type I 1.000) — cross-section
  asymmetry buys ~10%, then hits the same wall: the inner-
  equator deficit is NOT a phi-localised shortage the
  corrections can fill; it is the divergence-mismatch scale
  itself (P9 stands, strengthened). VELOCITY LADDER on the
  phi-base: v=0 reproduces the finals (-1.63e-5); v=0.02
  already collapses to the -1.0 floor with Type I 0.748 (the
  phi-optimised base is MORE brittle under motion than the
  s-only base — it spent its margin headroom on the static
  deficit); v in {1.1, 1.5, 2.0} (S1 extension): floor,
  Type I ~0.46. F3 closure: saturation under adversarial
  retraining in BOTH symmetry classes + ladder collapse.
  REOPENING: a genuinely toroidal equilibrium construction
  (profiles solved in the torus's own divergence from the
  start — the N3 conditions-first method ported to toroidal
  topology; not computable in this session's engine set).
  Serves hierarchy rung 1 (verified exclusion + a located
  structural mechanism, not in the literature as an audit result).
  IN PROGRESS (continuation session, 2026-11-21).
  ENGINE (x1_torus.py): prescribed-profile construction — the verified
  spherical family's 1D profiles a(.), b(.) (edge-peaked, s_rho=2.0,
  s_P=1.16) reinterpreted as functions of the torus distance
  s = dist(x, ring circle, Rmaj); gamma = delta + (e^{2b(s)}-1) shat shat,
  shat = grad s; cosine shift along the torus AXIS (g_tz = -S beta);
  profiles windowed to exact flatness outside the tube. Controls:
  flat profiles + beta=0 give max|That| = 0.0 EXACTLY (engine sound);
  flat profiles + beta=1.5 shift give max|That| = 1.5e-3 — NOT noise:
  a bare shift field on Minkowski is genuinely curved (the Natario-form
  stress-energy), a useful reminder that the shift alone is the exotic
  part. DIAGNOSTICS (x1_diag.py, structured s x phi points): the
  prescribed spherical profiles FAIL on the torus, worst SEC -1.67e-3
  (M=2, Rmaj=45, beta=0), with a clean failure anatomy: (i) the outer
  WINDOW layer [R2, R2+Delta] dominates at small Delta (violation
  ~ amplitude x 5.77/Delta^2 / 8pi: -1.7e-3 @ Delta=5, -3.9e-4 @ 10,
  -8.6e-5 @ 20 — an artefact of hand-windowing, fixable by shaping);
  (ii) the GENUINE toroidal effect: at the INNER equator (phi=pi, the
  face toward the ring hole) margins are -2.5e-5..-3.7e-5 at ALL s
  (shell interior and dilute tail alike, rho_Eulerian ~ -1e-5 there),
  while the outer equator (phi=0) passes at +2.3e-5 — the ring's
  curvature breaks the spherical shell's balance on its inner face by
  roughly the whole margin budget. Nearly Rmaj-independent between 45
  and 90 (the mismatch is the tube-vs-sphere divergence structure, not
  the ring size). (iii) Axis points must sit in the exactly-flat
  region (Rmaj > R2+Delta): on-axis with unwindowed profiles the
  discontinuous shat fabricates rho ~ +2.8e-2 — guarded by design.
  RESPONSE: free-form profile search (x1_de.py, Track P protocol):
  DE over a(s), b(s) CubicSpline knots on s in [0,45] (17 genes;
  cavity-flat and exterior-flat pinned), seeded from windowed
  spherical profiles at M in {2,3} x Delta in {10,15,20} x amplitude
  {0.8,1,1.25}; screen 260 pts (random + equator/pole emphasis),
  arbiter = fresh seeds 999/31337 at h=0.3 AND h=0.15. Rmaj=45
  (aspect 3) running first; Rmaj=30 (aspect 2) after. The S1 velocity
  grid is audited on the best base found, pass or fail.
  SUPERLUMINAL SUB-ROW (S1, Rakshit
  2026-11-21 02:09): v in {0.5, 0.9, 1.0, 1.1, 1.5, 2.0, 3.0} x aspect
  ratio x compactness, Fuchs ingredients, full all-observer audit.
  Named SSV escape route (logged per standing rule): the toroidal
  shell has non-spherical topology, non-unit lapse and non-flat
  spatial slices — outside every Natario-class assumption (unit
  lapse, flat slices, spherical/topologically trivial flow).
  Topology posited as initial data (Geroch), never "formed".
- X2 background curvature: ENGINE VALIDATED (x2_bg.py, continuation
  session): superposition g_tt = g_tt^bg x e^{2a_sh}, g_ti = g_ti^bg -
  S beta x-hat, gamma = gamma_bg + (e^{2b_sh}-1) nn, backgrounds in
  PG form (Schwarzschild, de Sitter river) + static AdS. Controls:
  flat bg reproduces Finalist A EXACTLY (min NEC +1.851e-7 over the
  sample = the R2-recorded +1.877e-7 point set minimum, Type I 1.0);
  dS H=0.05 bg-only: rho = 2.984e-4 vs 3H^2/8pi = 2.98e-4, NEC
  saturated at -4e-16, SEC = -2rho (background's own SEC violation,
  E2 framing; Type-I fraction is meaningless on the degenerate
  Lambda tensor — margins are the content); AdS L=30 bg-only:
  rho = -1.326e-4 = Lambda/8pi exactly, NEC saturated, WEC violated
  by the background itself. Schwarzschild PG bg-only: spurious
  |T| up to 6.9e-5 confined to r in [3,5) (INSIDE the horizon,
  FD truncation on the steep PG shift; falls as r^-steep to 8e-11
  at r>=20 and shrinks 16x from h=0.3 to h=0.15 = clean h^4
  scaling) — verdict region for schw rows is r>=5 (noise <=1.7e-6
  at h=0.3), r<5 reported as noise-dominated interior. Scan next.
  SUPERLUMINAL SUB-ROW (S2): local
  beta superluminal on the same v grid, Schwarzschild + (A)dS
  backgrounds; report direction and size of the background's effect
  on superluminal margins vs flat control.
  SCAN RESULT (x2_scan.py + x2_fix3.py; results/x2_scan.json,
  results/x2_schw_fix3.json) — X2 CLOSED: background curvature does
  NOT assist anywhere in this superposition ansatz; it degrades the
  shell monotonically with background strength, at every velocity.
  * Schwarzschild (verdict domain: alpha^2>0, stencil-guarded,
    r >= max(5, 2Mbg+1)): even the STATIC shell (beta=0) fails on
    the superposed background — total worst -9.9e-5 (Mbg=1),
    -5.7e-5 (Mbg=2), -1.2e-5 (Mbg=4, tightest mask), vs exactly 0
    for the same profiles in flat space. At the design beta=0.02:
    -1.37e-4 (Mbg=1), NEC -1.23e-3 (Mbg=2), NEC -4.13e-4 (Mbg=4),
    vs flat +1.85e-7. Superluminal rows (S2) all fail; the worst
    degradation sits near beta~1 (NEC -2.0e-2 at Mbg=2, -1.3e-2 at
    Mbg=4 — ~8x worse than the flat control's -2.7e-3), i.e. where
    the shell shift resonates with the PG inflow profile.
    DECOMPOSITION (F2 follow-up, x2_fix3 beta=0 rows): most of the
    beta=0.02 degradation is already present at beta=0 — it is the
    MATTER-IN-BACKGROUND interaction of the ad-hoc superposition
    (multiplicative lapse x additive shift is not a solution-
    generating map; its interaction stress-energy is of order the
    shell's own margins even for Mbg=1), NOT shift x inflow
    coupling. CAVEAT (binding on interpretation): X2 excludes THIS
    superposition, not a shell re-solved in the field. REOPENING
    CONDITION (F3): a construction that re-equilibrates the shell
    profiles in the background lapse (background-TOV) — needs a
    new solver, logged under F2-not-computable-here.
    AUDIT-DOMAIN FINDING (methodological, for R4): the first scan's
    NaN/overflow rows traced to (i) alpha^2<0 points inside the
    horizon (slices not spacelike; no Eulerian tetrad) whose
    |That|~1e297 poisoned the significance threshold (threshold
    computed over ALL points -> empty verdict set -> NaN print).
    Fixed by domain-restricted thresholds + overflow guard +
    stencil guard (x2_fix3.py); all 27 schw rows finite and the
    previously-finite rows reproduce exactly. Fourth artefact
    class for the record: THRESHOLD POISONING by out-of-domain
    points.
  * AdS (L=30/60): the background's own rho<0 violates WEC in the
    TOTAL tensor (background property, reported as such). The
    shell's DIFF tensor at beta=0.02 PASSES (+5.4e-6 worst at
    L=30, +5.0e-6 at L=60) — AdS is ~neutral for the shell itself.
    Superluminal diff rows fail exactly as flat. No assistance.
  Serves rung 1 (bounded exclusion + mechanism: superposition
  interaction scale) — background assistance is not a free lunch;
  curvature strong enough to matter is strong enough to break the
  shell's balance first, in every background tried.
- X3 SNEC + volume-integral diagnostics: CLOSED (see X3 section).
- X4 non-minimal scalar: CLOSED (continuation session 3,
  x4_scalar.py; results/x4_scalar.json) — NEGATIVE in BOTH frames,
  all profiles. 22 configs: shell (10,20) M=2 at beta in {0.05,
  1.1, 1.5} + M=8 at 1.5 (S4 superluminal points included), xi in
  {1/6, 0.25} (Fewster-Osterbrink interval), phi0 in {0.1, 0.3},
  F_min 0.44-0.96 > 0 throughout. JORDAN frame: the scalar's own
  T^(min) NEC is negative in EVERY row — the coupling terms do not
  legalise the matter; for a localised bump phi they OVERSHOOT
  (worst NEC -1.4e-2 at phi0=0.3, ~9x worse at phi0=0.3 than 0.1 =
  xi phi0^2 scaling; the bump's F'' changes sign across the wall,
  helping one face and hurting the other — the binding face loses).
  F2 FOLLOW-UP RUN (mechanism-suggested): monotone tail profile
  phi ~ 1/(1+(r/15)^2), one-signed F'' through the wall: Jordan
  NEC at beta=0.05 improves 40x (-2.4e-4 vs -9.2e-3) — anatomy
  confirmed — but still negative, and at superluminal beta the
  tail's Jordan NEC (-2.6e-3 @ 1.1, -3.2e-3 @ 1.5) is no better
  than the raw GR deficit: the coupling supplies no net NEC at
  the binding site. EINSTEIN FRAME (g_tilde = F g): NEC negative
  in all 22 rows (-5.6e-4..-5.8e-2) — no frame rescue, consistent
  with Fliss et al.'s effective-ANEC restoration. DSNEC gate moot
  (no Jordan pass to bound); recorded as scaling context only.
  CLOSED per F3: structural (two profile classes, both frames,
  xi across the QEI interval, superluminal included). REOPENING:
  an interacting-field construction (no QEI theorem exists —
  absence, not a construction) or a phi profile solving the
  coupled system rather than prescribed (full scalar-tensor
  solve; new engine).
- X5 Casimir threading: CLOSED (continuation session 3,
  x5_casimir.py; results/x5_casimir.json) — prescribed-source
  magnitude exclusion; NO superluminal shortcut shown (S5).
  Superluminal shell deficits (SL-2 configs (10,20), M in
  {2,5,8}, beta in {1.1,1.5,2.0}): D_max = 2.8e-3..4.2e-3 at the
  inner edge / mid-wall; ~57% of significant points in deficit.
  Covering D_max with a Casimir NEC supply 4 C_C N_eff / L^4
  (C_C = pi^2/720, axis generously aligned per-point) requires
  cycle size L <= 2.0 m (N_eff=1), 3.7 m (10), 6.6 m (100) — a
  BUBBLE-SIZED "compact" cycle, not a hidden dimension; threaded
  density rho_C ~ D/4 ~ 1e-3 geom over the wall volume is a
  negative-energy budget ~10x the shell's own mass; QI pulse
  ratio 65-585x over the Ford-Roman scale at tau = wall/beta
  (static-threading caveat stated in the file: a ground-state
  threading is not literally a pulse — the ratio is the ledger
  comparison, and even read generously the L scale alone closes
  it). MMP honesty honoured: their construction is long and
  causality-clean; nothing here shows a shortcut — the Casimir
  part would have to do exactly the NEC work SL-2 measured, at
  metre-scale cycles. REOPENING: a cycle geometry whose mode sum
  beats the plates coefficient by orders (none known; Kenneth-
  Klich opposites-attract closes the repulsive-Casimir variant).
- LENS E (expansion assistance, extension of X2; Rakshit 2026-11-21):
  E1 shell on FLRW/de Sitter backgrounds, H scanned from H0-scaled to
  inflation-scale; CLOSED (scan results appended below — shared
  machinery). E2 FRAMING (binding for all reporting): cosmic
  expansion's "FTL" is recession (v = H x distance), not local motion —
  nothing overtakes a local light beam; inflation's driver violates
  the SEC (rho+3p<0, legal for a canonical scalar: rho+p = phidot^2
  >= 0) but NOT the NEC; superluminal warp needs NEC violation and
  expansion never supplies it. Alcubierre's metric is itself the
  inflation trick localised (expand behind, contract ahead) — the
  pilot's shells are the right objects to embed. E3 PHANTOM CAVEAT:
  w<-1 phantom sources violate NEC but a phantom scalar is a ghost
  (negative kinetic term, quantum instability) — any phantom use in
  N4/X4 must carry that label + stability note.
- LENS E SUPERLUMINAL SUB-ROW (S3): superluminal LOCAL beta on
  FLRW/de Sitter backgrounds with Planck-bound parameters (D1);
  total-transport accounting stays honest (recession labelled as
  recession, never as local FTL).
  SCAN RESULT (x2_scan.py, ds rows) — LENS E CLOSED:
  * H0 ANCHOR (H = 7.3e-27 /m, Planck D1): rows IDENTICAL to flat
    to all printed digits (bg max|T| 3e-42). Today's expansion
    does nothing at shell scale — the honest baseline.
  * H RESPONSE at design beta=0.02 (frozen-H river snapshot; Hdot
    terms outside the audit, logged limitation): the TOTAL worst
    margin is the background's own SEC (-2 rho_bg, E2 framing —
    expansion violates SEC, not NEC, and it shows up exactly
    there): -2.4e-7 (H=1e-3) -> -6.0e-4 (H=5e-2). The shell's own
    DIFF tensor: passes at H=1e-3 (+1.3e-7), then its NEC deficit
    grows ~ -rho_bg/3 (rho_bg = 3H^2/8pi): -3.6e-7 (H=3e-3),
    -4.1e-6 (1e-2), -1.5e-5 (2e-2), -2.3e-4 (5e-2). CROSSOVER:
    background density reaches the shell's margin scale (2e-5)
    at H* ~ 1.3e-2 /m — above that, the background dominates the
    audit. Direction: expansion HURTS the shell in this
    superposition, roughly linearly in rho_bg.
  * SUPERLUMINAL (S3): beta in {0.5..3.0} at H=1e-2 and 5e-2 —
    ALL FAIL, margins within ~10-30% of the flat controls (never
    better beyond noise). NO superluminal rescue from expansion.
  * E2 MADE NUMERICAL: at H=5e-2 the recession across the shell
    (v_rec = H*r at r=R2=20) reaches 1.0c — and the shell's local
    audit is at its WORST there, not rescued. Recession is not
    transport; expansion supplies SEC violation, warp needs NEC,
    and the shell's NEC only degrades. CLOSED per F3: structural
    within the superposition class (monotone in rho_bg, both
    sub- and superluminal, H0 anchor exact); REOPENING CONDITION:
    same as X2 — a shell re-solved on the expanding background
    (comoving construction), not a superposition.
- Track P SUPERLUMINAL SUB-ROW (S6): after the beta=0.1 rung
  resolves, free-form ladder extends to v in {1.1, 1.5, 2.0} on the
  best-performing geometry so far, same re-randomised arbiter
  protocol.
  S6 RESULT — CLOSED (continuation session 3, s6_driver.py;
  results/trackP_b{1.1,1.5,2.0}_M10.0_S6.json): all three
  superluminal points on the (10,30) free-form geometry fail at
  the -1.0 margin floor with Type I fractions 0.31-0.38 on
  fresh arbiters (beta=1.1: 2 adversarial rounds, 2,496 evals,
  arbiter worst -1.000, 780 bad points in round 0 alone;
  beta=1.5: 1,248 evals; beta=2.0: 1,248 evals). No near-miss
  structure: at superluminal shift the free-form landscape is
  Type-IV-dominated everywhere the adversarial trainer looks,
  consistent with SL-2's dense named-family audits. REOPENING:
  none within free-form spherical splines — the geometry class
  is saturated at these velocities by two independent
  protocols (dense audit + adversarial training).
- Track N (N1 KK/braneworld, N2 non-Riemannian, N3 reverse-engineered
  + formation snapshots, N4 multi-component sources): CLOSED
  (all four implemented; results appended to each proposal
  below; proposals to be logged even if
  they die at the ansatz stage). SUPERLUMINAL SUB-ROW (S7): every
  N1-N4 proposal must include at least one superluminal test point
  in its first scan; a proposal tested only subluminally is
  INCOMPLETE in this ledger.
  PROPOSALS LOGGED 2026-11-21 (ansatz / named assumption / binding
  constraint / superluminal point each; implementation queued after
  the X-lenses):
  N1 KK LIFT OF THE VERIFIED SHELL: ds5^2 = g4(shell) +
  exp(2 sigma(r)) dy^2, y on S^1 of radius L_y; derive the 4D
  effective T_ab from the 5D Einstein equations and audit BOTH the
  4D effective tensor and a prescribed ordinary 5D anisotropic
  fluid source's own ECs. Assumption: sigma stabilised (a minimum
  of an unspecified potential — stated, not derived). Gates (D3/D4,
  case 2): L_y < 30 um (Eot-Wash), no unstabilised massless modulus
  (MICROSCOPE/Cassini); the 2.3 TeV ATLAS floor binds the RS-warped
  variant, the flat-S^1 variant is bound by fifth-force/EP data
  (KK tower from ~meV at 30 um). Superluminal point: beta=1.5 lift.
  If the 4D NEC relief traces to a 5D source that violates its own
  ECs, it is logged as disguised exotic matter = FAIL.
  N1 RESULT (continuation session 3, n1_kk.py; results/
  n1_kk.json) — CLOSED, bounded exclusion. Exact warped-product
  reduction (validated: sigma=0 controls reproduce the 4D source
  in 5D exactly — sampled NEC +6.9e-7 at beta=0.02, -3.36e-3 at
  beta=1.5 = the known deficit; Einstein frame = Jordan at
  sigma=0). sigma(r) wall bump, sigma0 in {0.1, 0.3}: the 5D
  SOURCE's all-observer NEC (sampled over 5D null directions —
  the eigenvalue min silently restricts to Type-I points and is
  NOT the verdict; both recorded) is NEGATIVE in every nonzero-
  sigma row: beta=0.02: -1.7e-3 (sig0=0.1), -5.3e-3 (0.3) — the
  lift of the VERIFIED shell already needs an NEC-violating 5D
  source, and it worsens with sigma0; beta=1.5: -4.4e-3 / -1.4e-2
  (vs -3.4e-3 trivial lift). Mechanism: the reduction terms
  -Hess(sigma) - dsigma dsigma enter R5 with the same anti-
  aligned sign structure as P7 — sigma's gradients are themselves
  exotic in 5D. Einstein frame: worst margin at the -1.0 floor
  in all nonzero-sigma rows (the conformal rescaling is a
  different, harder configuration). By the proposal's own rule:
  disguised exotic matter = FAIL. REOPENING: a stabilisation
  sector whose own stress-energy is audited ordinary AND cancels
  the sigma-gradient terms (a coupled sigma-potential solve —
  new engine), or a warped (RS-type) lift, which then carries
  the D4 2.3 TeV floor as its binding gate.
  N2 EINSTEIN-CARTAN TORSION: Weyssenhoff spin fluid in the shell;
  the spin-squared contact term contributes a computable effective
  stress-energy (Hehl-Datta form) on top of the fluid's own.
  Audit: fluid ECs (ordinary), effective ECs, and the torsion
  sector's algebraic consistency. Assumption: torsion couples only
  to intrinsic spin (standard EC). Constraint: spin-density
  required vs torsion bounds from spin-precession/Hughes-Drever
  class experiments (literature values, case 2 where they cover,
  case 3 labelling otherwise). Superluminal point: beta=1.5.
  N2 RESULT (continuation session 3, n2_ec.py; results/
  n2_ec.json) — CLOSED, bounded exclusion BY MAGNITUDE. Sign
  audit: the Weyssenhoff spin-spin contact term is the one
  classical term with the HELPING sign (NEC supply 2 delta along
  the spin axis, saturating transverse). Magnitude ledger:
  supplying the beta=1.5 deficit D = 3.36e-3 needs delta =
  1.68e-3, and since delta/T_fluid ~ T_fluid/T_Cartan with
  T_Cartan ~ 7.4e26 geom (rho_Cartan ~ 1e54 kg/m^3, literature
  scale, labelled), the required spin-polarised fluid density
  is T_f = sqrt(delta*T_Cartan) = 1.5e39 kg/m^3 — 21.2 orders
  of magnitude above nuclear density, before polarisation
  fractions. Structural (F3): the coupling is fixed by GR
  constants; no parameter to tune. REOPENING: non-minimal
  torsion-matter coupling >> EC standard (a different theory,
  gated by D2/D3 spin-precession bounds).
  N3 REVERSE-ENGINEERED + FORMATION SNAPSHOTS: (a) prescribe
  Type-I eigenvalue profiles with all margins positive and a target
  shift, integrate the Einstein ODEs for a(r), b(r) — the shell
  construction generalised to l=2 non-axisymmetric perturbations
  audited mode by mode; (b) quasi-static formation sequence:
  snapshots at beta(t) = 0 -> 0.05 in 6 steps with profiles
  re-solved at each step, every snapshot audited (a legal instant
  path is necessary, not sufficient, for formation — labelled).
  Assumption: quasi-static approximation. Constraint: none
  experimental (case 3). Superluminal point: one snapshot sequence
  member at beta=1.1 (expected to fail; included per S7).
  N3 PROMOTED (Rakshit, 2026-11-21 05:23 PT) to the full
  conditions-first spec: PRESCRIBE Hawking-Ellis Type I eigenvalue
  fields (rho, p_i) satisfying all ECs with margin BY CONSTRUCTION
  (compact support, smooth falloff, finite mass, no shape family
  assumed), then INTEGRATE BACK to a metric in a stated gauge
  (gauge + boundary conditions logged) whose Einstein tensor
  reproduces the prescribed eigenvalues to a stated tolerance; the
  recovered shift defines the bubble velocity — targets beta in
  {0.05, 0.1, 0.5} + superluminal {1.1, 1.5, 2.0}. The recovered
  metric is then judged by the STANDARD auditor (two resolutions +
  fresh-point arbiters), with the anti-smuggling checks: (a) full
  recovered T_ab Type I, not just prescribed eigenvalues
  (eigenvector misalignment / hidden fluxes); (b) no
  distributional artefacts at the support boundary; (c) asymptotic
  flatness + ADM mass from the RECOVERED metric; (d) horizons /
  trapped surfaces inside the bubble region reported if present;
  (e) implied matter flow subluminal (DEC, confirmed explicitly).
  Time-dependent morph snapshots (formation probe) follow the
  static results. Inversion failure modes (non-convergence, gauge
  breakdown, tolerance floors) are logged as results; a bounded
  "cannot produce X within tolerance Y" closes the row (F3).
  N3 RESULTS (continuation session 3, n3_invert.py + n3_de.py;
  results/n3_*.json) — CONDITIONS-FIRST, flagged as such.
  Inverter: prescribe rho*(r) >= 0 and p_t*(r) = tau(r) rho*(r)
  freely (spline knots, compact support [0, R2+14]); p_r follows
  from the conservation/Bianchi identity integrated OUTWARD
  (inward is unstable, mode ~r^-2) with p_r(RMAX)=0 by secant
  shooting on p_c = p_r(0) = p_t(0); m from rho*, b = -1/2
  ln(1-2m/r), a from the TOV-like a' with asymptotic matching;
  gauge = the pilot ADM ansatz, cosine shift on [R1, R2] added
  after; ADM mass = m(RMAX) from the recovered metric. CONTROL:
  inverting the forward construction's realised (rho, p_t)
  (Finalist A config) returns its metric to max|da| = 3.3e-7,
  max|db| = 6.8e-7 — the inverter is exact where the answer is
  known. Solve cost ~0.05 s.
  RUN 1 (beta=0.1, M=10, (10,30); realisability-penalised
  objective): DE winner audits -2.1e-6..-3.1e-6 on fresh
  arbiters — WORSE than the forward seed (-5.8e-7). DIAGNOSIS
  (F1): the penalty priced the seed out of the population (the
  forward profiles are not exact conservation solutions, so
  their shooting residual is large even though their margin is
  the best known) — an objective-design artefact, not physics.
  RUN 2 (penalty removed, F2 follow-up): screen +2.44e-7;
  fresh-seed finals +6.64e-7/+6.64e-7/+6.32e-7/+6.33e-7
  (seeds 555001/777001 x h=0.3/0.15), Type I 1.000, shooting
  F = 1.1e-8, realisation residuals ~1e-5 relative, ADM
  10.000005, u_min = 0.470 (no trapped surface). An APPARENT
  PASS at beta=0.1 — treated as candidate under attack.
  ATTACK (n3_attack.py): dense audits (3,000 pts x 3 seeds x 2
  resolutions) CONFIRM the interior: all margins positive, min
  DEC +2.56e-7, Type I 1.0000; cavity positive (+1.79e-7).
  The first tail audit (r in [29, 44.5]) FAILED at -1e-3 —
  and the failure itself then failed scrutiny, in two layers.
  LAYER 1 (artefact): the audit sampled past the recovered
  metric's solved domain (rmax=44), where prof_gfunc CLAMPED
  e^{2a}, e^{2b} at their r=44 values — a kink whose FD tensor
  is ~1e-3 and grows like 1/h (the adversarial hunt's argmin
  sat at r = 44.0, the seam). Fixed by an exact Schwarzschild
  continuation in prof_gfunc (support ends at 38, so [38, 44]
  is vacuum by construction; far-field tensor then ~1e-12,
  h^2-clean). RUN 3 (knots/screens extended in response to
  the layer-1 reading) is thereby VOID as tail evidence — it
  optimised against the seam artefact; noted, not used.
  LAYER 2 (the real disease, measured with the seam moved to
  r=60): the recovered matter's tail beyond the prescription
  window (rho* = 0 past r=38) carries the conservation law's
  p_r tail, p_r ~ +1.8e-6 decaying slowly — a rho=0, p_r != 0
  tail violates DEC by |p_r|: DEC -1.8e-6 on [39, 52],
  resolution-independent to 3 digits; NEC ~ 0 (-5e-9 worst).
  Anti-smuggling check (b) fails in whisper form: not a thin
  shell, a pressure tail that outlives its density.
  VERDICT on run 2: NOT a verified pass — legal on the
  interior [0, 38] at +2.6e-7, DEC-illegal in its own tail
  at -1.8e-6. The interior result stands as a measurement:
  conditions-first freedom (independent p_t) DOES move the
  beta=0.1 interior margin from the forward wall (+1e-9 AD /
  -2.06e-7 named) to +6.4e-7 sustained — the wall was partly
  a family artefact (p_t slaving) in the interior. RUN 4
  (the F2 follow-up the anatomy dictates): replace the hard
  prescription window with a soft exponential tail (decay
  length a gene), so rho* decays WITH p_r instead of dying
  before it; solve domain 60, screens to 58.
  RUN 4 RESULT — SPLIT VERDICT = NEGATIVE under protocol
  (3,565 evals): screen (seed 4242) +2.85e-9; finals seed
  555001 +2.12e-9 (both resolutions, Type I 1.000); finals
  seed 777001 -1.24e-5 (both resolutions, Type I 1.000 — a
  smooth margin pocket, not a type collapse). With the tail
  honestly priced, the conditions-first DE saturates AT the
  wall: it holds the boundary to +3e-9 on its own screen but
  a fresh arbiter finds -1.24e-5. The warpax AD tiebreak was
  not needed (FD arbiters already split; AD is reserved for
  FD-positive candidates).
  N3 CLOSURE (F3, structural): the beta=0.1 wall is now
  located from BOTH SIDES by TWO INDEPENDENT CONSTRUCTIONS —
  forward families (best +1.3e-9 AD, uncertifiable; M=11/12
  fail) and conditions-first prescriptions with unrelated
  DOF (interior freedom demonstrably real: +6.4e-7 interior
  in run 2; full-configuration attempts saturate at the same
  ~1e-9 boundary in run 4, with the binding constraint
  migrated to the support tail — P2's migration completed:
  inner edge -> mid-shell -> tail). No fully-legal beta=0.1
  configuration exists in anything this programme can build;
  beta=0.05 remains the fastest verified rung (forward), with
  conditions-first boundary contact at the below-floor point
  from the other side (-7.8e-9). Superluminal members of
  every N3 run: floor, Type I ~0.43-0.72 (S7 complete).
  REOPENING (precise): (i) a run-4-design rerun at the
  beta=0.05 below-floor point (10,20) M=3.5 — the one N3
  measurement whose tail is still unaudited; (ii) a
  prescription basis with an explicit boundary-layer family
  at the support edge (the tail is where the constraint now
  lives); (iii) the meridional PDE inversion (logged above).
  BELOW-FLOOR RUN (beta=0.05, M=3.5, (10,20), run-2 objective):
  DE converged to screen -7.68e-9, finals -7.83e-9 (both
  seeds, both resolutions, Type I 1.000) — from the forward
  free-form floor of -2e-4, the conditions-first search lands
  within 8e-9 of zero at the below-floor point: boundary
  contact from a second, independent construction (the floor
  is real), but NOT below it (no positive margin; this run's
  screens carried the same tail hole — interior verdict,
  tail unaudited; a run-3-style rerun is the logged follow-up
  if run 3 shows tails can be made legal).
  SNAPSHOTS (run-1 winner prescription; interior audits):
  static beta=0: -2.87e-8; formation morph beta 0 -> 0.05 in
  6 steps: worst ~ -3.1e-8 at EVERY step (Type I 1.000) — a
  quasi-static instant path exists at boundary-hugging
  margin for this prescription family (necessary, not
  sufficient, for formation — labelled); beta=1.1 snapshot:
  floor, Type I 0.43 (S7 superluminal member fails, as
  everywhere). Sweeps of both DE winners at beta in
  {0.5, 1.1, 1.5, 2.0}: floor, Type I ~0.43-0.45.
  AXISYMMETRIC STEP: closed by argument, logged honestly —
  deforming a known solution by a diffeomorphism preserves
  every pointwise EC verdict exactly (pullback), so a
  prolate "conditions-first" metric built that way is
  vacuous; a non-vacuous axisymmetric inversion is a coupled
  PDE solve (Picard on the meridional grid), NOT computable
  in this engine set — logged as the follow-up with its
  requirements (elliptic solver + constraint damping). The
  genuinely non-vacuous angular-freedom test of this
  programme is Track B (metric-side), which resolved
  negative on dense audit.
  N4 TWO-COMPONENT ORDINARY SOURCES: canonical scalar (all ECs by
  construction) + k-essence-type fluid, each audited separately AND
  as a sum, at the beta=0.05 frontier point: can a mixture beat the
  single-fluid compactness floor 0.383 while every component stays
  ordinary? Assumption: components interact only gravitationally
  (stated). Constraint: none experimental for canonical parts
  (case 3); any phantom-flavoured variant only inside the D1
  window w in [-1.06, -1.00] and carrying the E3 ghost-instability
  label. Superluminal point: beta=1.1 mixture audit.
  N4 RESULT (continuation session 3, n4_mix.py; results/
  n4_mix.json) — CLOSED, theorem-grade exclusion with numeric
  confirmation. LP feasibility (components granted co-diagonal,
  flux-free, relaxed-scalar treatment — the most favourable
  case) at the 40 worst audited points of each config: beta=0.05
  (10,20) M=3.5 below-floor config: 0/40 admit an ordinary
  split; beta=1.1 (10,30) M=10 (S7 point): 0/40. LP controls
  behave (legal tensors split trivially; violating ones do
  not). The core is arithmetic, not search: NEC is linear in T,
  so NEC(T1+T2) = NEC(T1)+NEC(T2) >= 0 whenever every component
  obeys NEC — a violating total cannot be assembled from
  non-violating parts in any frame, with any interaction
  (interactions move energy-momentum between components; the
  pointwise sum is untouched). The same linearity closes DEC/
  SEC mixture hopes wherever the binding condition is NEC.
  The ONLY exit is a component that itself violates NEC — a
  ghost (k-essence F_X<0 / phantom), which is exotic matter
  under the E3 label, not an ordinary source. REOPENING: none
  within "sum of ordinary components" — the row closes on a
  proof, the strongest closure in the ledger (F3).
- TRACK B — FREE-FORM 3D BLOB (Rakshit, 2026-11-21 05:24 PT):
  CLOSED NEGATIVE (result appended below; it was queued after
  N3's first static results — the two un-caged tracks are the
  headline pair). Parametrisation: metric-side
  fields (lapse, conformal factor, shift components, density
  weight) as 3D B-spline/trilinear control lattices (start 4^3-5^3
  per field) over a box containing the bubble; NO spherical or
  axial symmetry; boundary pinned to Minkowski by a window; DE as
  in Track P, objective = worst all-observer margin on dense
  space-filling RANDOM 3D screens (no radial/angular grids);
  arbiters re-randomised at h and h/2; autodiff tiebreak before
  any candidate is called anything. TARGETS in order: (a) beta=0.1
  FIRST (spherical wall located at ~1e-9 there, Pattern P8 —
  margin > 1e-6 sustained across arbiters = real progress; ~1e-9
  again = the wall is symmetry-independent, itself a strong
  result); (b) beta=0.05 below compactness 0.383; (c) superluminal
  beta in {1.1, 1.5} (S6/S7 for this geometry). COST DISCIPLINE:
  log evals + wall-times; saturation like the torus adversarial
  round closes it as a bounded negative; ONE refinement step
  (5^3 -> 6^3) authorised if the coarse run ends within 10x of
  the spherical boundary at beta=0.1.
  TRACK B RESULT (continuation session 3, blob.py +
  blob_attack.py; results/blob_b0.1_NL5.json) — target (a)
  RESOLVED NEGATIVE; the row's first apparent pass was BROKEN
  by its own attack protocol, and the break is the result.
  Implementation as run: Gaussian-RBF lattice (trilinear
  rejected: stencil artefacts; B-spline basis replaced after a
  knot mismatch — normalised RBF, partition of unity exact),
  NL=5 (625 genes), boundary planes pinned, C2 taper to exact
  Minkowski at |x_i|=38. Seed = spherical (10,30) M=10 wall
  sampled on the lattice: -1.88e-5. DE (5,625 evals, 2,905 s):
  screen worst +8.86e-6; fresh 500-pt finals +2.78e-6 /
  +3.58e-6 (two seeds x h=0.35/0.175, Type I 1.000) — an
  APPARENT PASS, treated as candidate under attack. ATTACK:
  (i) anatomy — interior ADM shift mean +0.036 (the DE had
  diluted the seed's 0.1 motion; velocity not pinned by the
  objective — a design flaw, logged); grid mass 46.9 vs the
  spherical 10 (fat smooth configuration, node spacing 20 m).
  (ii) DENSE audits (6,000 pts x 3 fresh seeds x 2 resolutions):
  worst -1.87e-5 / -1.21e-5 / -1.64e-5, Type I 0.9993-0.9998 —
  the 500-pt finals were a 3D SAMPLING HOLE (artefact class
  (i)/(ii) in 3D form, exactly the failure the track spec
  warned about); the dense scale matches the seed's -1.88e-5:
  angular freedom at this lattice resolution bought NOTHING
  against the beta=0.1 wall. Verdict: NOT a candidate; the
  wall survives the first symmetry-free attack at ~1e-5, four
  orders below the spherical boundary measurement — the blob
  is a weaker instrument than the spherical family here, not
  a stronger one. Targets (b)/(c) NOT run: (a)'s dense-audit
  collapse removes the premise (a coarse lattice that cannot
  hold its own screen at 0.1 has no standing at 0.05-below-
  floor or superluminal points, where every other instrument
  fails by orders more); the 5^3->6^3 refinement is NOT
  triggered (the run did not end within 10x of the spherical
  boundary — it ended 4 orders below it on dense audit).
  REOPENING: a lattice/basis whose seed reproduces the
  spherical wall at ~1e-7 or better (resolution first), plus
  velocity pinned in the objective (interior shift plateau
  constrained, not seeded-and-free). FOLLOW-UP LOGGED (F2,
  not run): NL=5 with 3,000-pt screens + dense-audit-in-the-
  loop finals — cost ~4x this run; expected value low after
  the dense collapse.
- SUPERLUMINAL REPORTING RULE (S-directive, binding): the final
  report's superluminal exclusion map is PER-GEOMETRY (spherical
  shell / toroidal / background-assisted / expansion-assisted /
  free-form / each theory lens), never one global claim. Any
  apparent superluminal pass goes through R1-R3 + the full finalist
  protocol and is reported as "candidate under attack", never as a
  discovery, until it survives. For modified-gravity variants T_eff
  must still violate somewhere, else it is not a warp candidate.

## Track P — free-form machine search (trackP.py)
Parametrisation: density weight and shift profile as PCHIP splines
through free knots (8 density log-knots + 6 shift interior knots on
[R1,R2], endpoints pinned S=1->0; s_rho, s_P free) = 16 genes.
Optimiser: differential evolution (popsize 8, mutation (0.3,1.2),
recomb 0.8), objective = worst all-observer margin on a screening
sample; arbiter = re-randomised dense samples (seeds 999/31337,
~1000 pts) at h and h/2 that the optimiser never saw.
- beta=0.05 named-config re-audit (pre-P calibration): the (10,20) M=4
  edge-peaked pass SURVIVES re-randomised dense audits (worst
  +3.5e-8..+6.2e-8, both seeds, both h; NEC +1.0e-7..+1.4e-7, Type I
  1.000); the M=6 wd=3 variant fails at the exterior tail (SEC -1.4e-7
  @ r=24.4) — heavier is not monotonically better; tail shaping matters.
- Run 1 (beta=0.05, M=3.5, 3328 evals): screen worst +2.76e-6 but
  arbiter FAILED (DEC -1.0 @ r=10.12, Type I 0.87): the screen had a
  radial hole at r in (6,13) and the optimiser hid a spike in it.
- Run 2 (fixed dense screen, 3328 evals): screen worst +5.72e-7 but
  arbiter FAILED again (SEC -8.0e-4, NEC -8.3e-5 @ r=16.8, Type I
  0.94-0.96, both seeds/h): this pocket is ANGULAR — the screen's 12
  directions never sampled it; the arbiter's 26 rotated directions did.
  Per anti-artefact rule (iv) both runs are logged as Track P NEGATIVE
  results for naive fixed-sample optimisation: optimiser gains
  evaporate under re-randomised sampling. Standing fix: adversarial
  training (arbiter pockets are fed back into the objective sample;
  run in progress at M=3.5). The named-family compactness floor
  M/R1=0.383 at beta=0.05 stands until a machine candidate survives
  the full arbiter protocol.
- ADVERSARIAL RUN (beta=0.05, M=3.5, (10,20), 4608 evals, 2221 s):
  NEGATIVE — no machine pass below the named floor. Adversarial
  training worked as designed on each round's fresh arbiter (worst:
  -1.0 -> -1.4e-3 -> -4.3e-5; harvested bad points 158 -> 177 -> 60),
  but the DE objective on the growing training set (558 -> 716 -> 893
  pts) NEVER reached positive (-1.57e-4 -> -1.50e-4 -> -2.09e-4), and
  the FINAL verdicts on two never-used seeds failed: seed 555001
  worst -1.86e-4 (h=0.3) / -3.68e-4 (h=0.15); seed 777001 -2.79e-4 /
  -4.20e-4; Type I 0.96-0.98. Interpretation: at compactness 0.35
  (below the named floor 0.383) the free-form landscape has a hard
  margin floor around -2e-4 — violating pockets keep appearing
  wherever fresh points are sampled, and the optimiser cannot satisfy
  even the points it has seen. Serves hierarchy rung 1 (a machine-
  scale exclusion datapoint) and confirms rung 2(b)'s floor: the
  named M/R1 = 0.383 at beta=0.05 STANDS against 11,264 free-form
  evaluations across three protocols. Next: beta=0.1 adversarial at
  the named near-miss (10,30) M=10.
- ADVERSARIAL RUN beta=0.1, (10,30), M=10 (4608 evals, 3 rounds):
  SPLIT VERDICT = NEGATIVE under the protocol, but the closest
  approach of the whole pilot. Training objective went POSITIVE in
  rounds 1-2 (+2.76e-7 on 694 pts, +1.69e-7 on 847 pts — unlike
  beta=0.05, the optimiser CAN satisfy seen points here); arbiter
  pockets shrank (118 -> 153 -> 82 bad pts, worst -1.5e-4 -> -7.3e-5
  -> -9.9e-5). FINAL verdicts: seed 777001 PASSES COMPLETELY
  (worst +3.334e-7 at h=0.3, +3.336e-7 at h=0.15, Type I 1.000);
  seed 555001 FAILS genuinely (-1.633e-5 at both h, Type I 0.993 —
  consistent under refinement, a real pocket). One failing fresh
  seed kills the candidate (anti-artefact rule iii): NO machine pass
  is claimed at beta=0.1. But the rung is balanced on a knife edge:
  a free-form shape exists that passes an entire 1000-point random
  audit at beta=0.1 / compactness 1.0. A 5-round extension (2 more
  adversarial rounds harvesting the 555001 pockets) is RUNNING; if
  both final seeds pass there, the shape goes to full finalist
  treatment + R1-R3 (rule R5) before being reported as anything.
  Winning-shape genes (round 2, for the record): theta_d =
  [-0.95, 0.85, -0.41, -2.09, -2.50, -0.93, -0.11, -0.82], svals =
  [0.935, 0.765, 0.552, 0.349, 0.153, 0.022], s_rho=3.80, s_P=1.78 —
  note the shift knots are nearly the cosine values; the machine's
  freedom went into the DENSITY shape (deep mid-shell trough,
  theta_d ~ -2.5) and much heavier smoothing.
- 5-ROUND EXTENSION (7680 evals): rounds 3-4 CONVERGED at the
  training resolution — training objective +3.74e-7 (929 pts) ->
  +4.21e-7 (981 pts); fresh arbiter worst POSITIVE twice in a row
  (+5.37e-7, +6.15e-7). BUT the FINAL verdicts split BY RESOLUTION:
  both seeds PASS at h=0.3 (+6.60e-7, +6.75e-7, Type I 1.000) and
  FAIL at h=0.15 (-1.02e-4 seed 555001, -1.34e-5 seed 777001,
  Type I 0.986-0.995). VERDICT: NOT A PASS — margins must hold under
  refinement. This is a THIRD artefact class for the record:
  stencil-scale exploitation (the optimiser shaped features at the
  h=0.3 stencil scale that the finer stencil resolves as
  violations; rounds 3-4 arbiters were all audited at h=0.3 only).
  Standing fix, now mandatory for Track P: arbiter audits at BOTH
  h and h/2 in every round, not only at finals. DECISIVE TIEBREAK
  QUEUED: audit the round-4 genes with the warpax AUTODIFF path
  (no stencil exists in AD) at the final-seed point sets — if AD
  margins are positive, the h=0.15 FD failure is itself the
  artefact (FD on knot-scale features) and the candidate proceeds
  to full finalist treatment with the AD path as primary; if AD
  agrees negative, the shape is dead and beta=0.1 free-form closes
  as a near-miss negative. Round-4 genes: theta_d = [-1.07, 1.30,
  -0.33, -2.14, -2.70, -1.07, -0.17, -0.82], svals = [0.930, 0.752,
  0.520, 0.333, 0.176, 0.047], s_rho=3.97, s_P=1.44.
- AD TIEBREAK RESULT (trackP_ad_audit.py; results/
  trackP_b01_ad_audit.json): the AUTODIFF margins of the round-4
  shape are POSITIVE on both final-seed point sets — worst
  +1.34e-9 (seed 555001, NEC +3.69e-9) and +1.61e-9 (seed 777001,
  NEC +4.22e-9), Type I 1.000 — but ~4 orders of magnitude BELOW
  the FD noise floor at these knot-scale features (FD h=0.3 says
  +6.6e-7, FD h=0.15 says -1.0e-4; they bracket the AD value and
  agree only that the shape is within ~1e-4 of the boundary).
  VERDICT: NOT A VERIFIED PASS (the novel-candidate rule requires
  margins ABOVE numerical error; 1e-9 is not above 1e-5 FD error,
  and no second path can certify a 1e-9 margin). The correct
  statement: the machine search CONVERGED TO THE FEASIBLE/
  INFEASIBLE BOUNDARY at beta=0.1, (10,30), M/R1 = 1.0 — the
  boundary passes through this shape to within 1e-9 in exact
  derivatives. Follow-up running: same genes at M=11 and M=12
  (AD audit) — if the boundary shape moves genuinely inside with
  modest extra mass, the beta=0.1 rung minimum lies just above
  M=10 and a verifiable candidate exists there; if AD margins stay
  ~1e-9, the boundary is a wall, not a slope.
- MASS-SWEEP RESOLUTION (AD + FD, seed 777001 points): the boundary
  is a WALL for this shape. M=11: NEC/WEC +3.92e-9, SEC +3.7e-10,
  but DEC = -3.05e-5 (AD; FD -3.4e-5/-3.0e-5, Type I 1.000 — all
  three paths agree). M=12: AD worst -1.36e-4 (DEC; FD -1.40e-4/
  -1.36e-4), NEC still +3.27e-9. Increasing mass at fixed shape
  leaves NEC pinned at ~1e-9 and drives a DEC violation in the
  low-density tail (pressure tail outliving density — Patterns P2/
  P4 in a new register). FINAL beta=0.1 FREE-FORM VERDICT: rung
  EMPTY under verified standards (named 124 evals + free-form
  12,288 evals + AD audits), with the feasible/infeasible boundary
  LOCATED to 1e-9 at (10,30), M/R1 = 1.0 for the best machine
  shape — the strongest near-miss of the pilot, reported as a
  boundary measurement, not a candidate. Serves hierarchy rung 1
  (a machine-precision boundary location is new information) and
  closes the beta=0.05 + beta=0.1 interim handoff: beta=0.05 PASSES
  (named, compactness 0.383, lightest 2.58e27 kg at (5,10));
  beta=0.1 is empty with its boundary mapped.

## X3 — SNEC + volume-integral diagnostics (x3_diag.py;
## results/x3_diag.json) — CLOSED
For the three frozen findings (A, B2, frontier_b005):
- I_V^- (all-observer volume integral of min(NEC margin, 0)):
  A -4.35e-3, B2 -6.20e-3, b005 -2.10e-3 (geometric metres; b005 at
  N=121/L=15, h=0.25 — the first b005 value, -1.11 on an N=81/L=30
  grid, was a 500x resolution artefact and is superseded). All
  three are FD-grid-noise level, consistent with ZERO negative
  volume, and cross-check the QI ledger's grid-integrated negative
  energies (-1.5e-3 m for A). Pareto picture: the findings carry
  NO volume-integrated NEC negativity to trade against mass —
  I_V^- ~ 0 is the expected signature of a pointwise-passing
  configuration, and it is what the integrals show.
- SNEC functional (Freivogel-Krommydas, conjectured bound) along
  the axis null geodesic, Gaussian smearing tau in {0.5, 1, 2, 5}
  centred on the wall and on the centre: smeared integrals
  I(tau) = int g^2 T_kk dlam are POSITIVE everywhere (wall-centred:
  A 2.0e-5..2.8e-4, B2 2.3e-5..3.3e-4, b005 3.6e-5..1.0e-3 across
  tau), so the implied B_min is negative at every width — SNEC is
  satisfied for any B >= 0, as it must be when pointwise NEC holds.
  Axis T_kk minimum: ~0 (-6e-15, -8e-15) for A/B2; -5.5e-6 for
  b005 at the diagnostic's coarse h=0.15 (its verified point audits
  at h=0.075 are positive; the dip is the FD error at its sharper
  wall, noted for honesty). Diagnostic normalisation: k^t = 1.

## Patterns (fitted from accumulated audit data; sample sizes stated)
- P1 SCALE COVARIANCE (n=4 geometries, beta=0.05): min passing
  compactness M/R1 = 0.383 +- 0.001 independent of R1 in {5,10,20,30}
  (W=R1, same relative design); worst margins scale as R^-2 within
  10%. GR is scale-free; the frontier is a compactness-beta curve.
- P2 FAILURE-SITE MIGRATION (n~40 failing configs): at beta<=0.05 the
  binding failure sits at the INNER shell edge (r ~= R1 + 0.05W); the
  beta=0.1 thick-shell near-miss binds MID-shell (r=18.8 of (10,30),
  NEC); tail (r > 1.2 R2) SEC binds only for near-passing configs —
  i.e. as the shell interior is fixed, the binding constraint moves
  outward to the smoothing tail.
- P3 WINDOW PLACEMENT (n=32, Track L Phase A/B): shift transitions
  extending outside the matter support fail at DEC ~ -1.0 regardless of
  mass (gradient in vacuum = bare Alcubierre violation); transitions
  must live inside the shell.
- P4 MONOTONICITY FAILURE (n=6, beta=0.05 (10,20) edge-peaked): worst
  margin vs M is non-monotone (M=4 passes, M=6 fails at the tail,
  M=9 fails DEC at the inner edge) — profile/smoothing interplay, not
  a simple mass threshold. Bisect-with-confirmation, never assume.
- P5 MG-1 ALPHA RESPONSE (n=516): matter margins flat for
  alpha-hat <= 1e-2, then monotonically WORSE with alpha-hat at all
  (v, amps, Delta, eta) — no ridge toward zero anywhere in the grid;
  the R^2 correction's tensor structure anti-aligns with the wall's
  NEC deficit in this ansatz.
- P8 BOUNDARY-WALL / DEC-TAIL BINDING (n=3 mass points, Track P
  beta=0.1 shape, AD-measured): at the feasible boundary the NEC/
  SEC margins pin at ~1e-9 independent of mass (M=10, 11, 12), while
  DEC in the low-density tail degrades monotonically with mass
  (+4.2e-9 -> -3.0e-5 -> -1.4e-4). The boundary is set by two
  different mechanisms on its two sides: NEC/SEC from the wall
  interior, DEC from the smoothing tail's pressure-to-density
  ratio. Mass is not a universal solvent: past the boundary shape,
  adding mass only buys tail DEC trouble.
- P7 QUADRATIC-CORRECTION ANTI-ALIGNMENT (n=576, MG-1 + MG-2):
  in both f(R)=R+alpha R^2 and f(Q)=Q+beta Q^2 on the generalised
  bubble ansatz, the matter worst-margin is flat or marginally
  improving for coupling-hat <= 0.1 and then degrades monotonically
  (steeply) with coupling — the extra classical DOF's stress tensor
  anti-aligns with the wall NEC deficit at the strength where it
  would have to supply the violation. Two independent theories, same
  signature: the seam, if it exists, is not in the quadratic
  single-function extensions of this ansatz.
- P9 TOROIDAL INNER-EQUATOR DEFICIT (X1: 15,402 DE evals + 1,564
  adversarial evals + structured diagnostics, aspects 2/3/4): a
  tube-symmetric toroidal shell built from spherical-family profiles
  carries an NEC-class deficit of ~-2e-5 concentrated at the INNER
  equator (the tube face toward the ring hole), at all radii in the
  tube and its tail, while the outer equator passes at +2.3e-5.
  Origin: the tube's distance-function divergence (1/s + ring term)
  differs from the spherical 2/r the profiles were equilibrated
  against; the mismatch is O(the shell's whole margin budget) and
  nearly aspect-independent for aspect >= 3. Free-form re-shaping
  of a(s), b(s) recovers two orders of magnitude over hand-windowed
  profiles but saturates at the same -2e-5 scale, and adversarial
  retraining on the caught pockets does not move it — within
  s-only profiles the deficit is structural. Any toroidal warp
  claim needs cross-section-asymmetric matter or a genuinely
  toroidal equilibrium construction; a spherical shell's profiles
  cannot be bent into a donut for free.
- P10 MODIFICATION ROBUSTNESS + AUDIT ARTEFACTS (session 3):
  (a) Every perturbative modification of the theory or setting
  tried around the shell — f(R) and f(Q) quadratics (P7),
  non-minimal scalar (X4: coupling overshoots on one wall face,
  supplies no net NEC at the binding site even with a
  one-signed-curvature profile), KK sigma gradients (N1: the
  reduction terms are themselves NEC-negative in 5D, worsening
  with sigma0), background superposition (X2: interaction terms
  enter at the shell's own margin scale already at beta=0),
  expansion (Lens E: shell-diff NEC deficit ~ -rho_bg/3,
  crossover at H* ~ 1.3e-2/m where rho_bg reaches the margin
  scale) — degrades or leaves unchanged the binding margin.
  The wall's deficit is robust to modifications AROUND the
  shell; the only levers that ever moved margins were
  compactness (P1) and in-shell profile freedom, and those
  saturate at the P8 boundary. (b) FOURTH AUDIT ARTEFACT CLASS:
  THRESHOLD POISONING — a single out-of-domain point with
  |That| ~ 1e297 inflates the significance threshold
  (1e-3 * rho_peak over ALL points) and silently empties the
  verdict set (NaN rows in the first X2 scan). Defence:
  domain-restricted thresholds + overflow guards + domain
  masks stated per audit. (c) EIGENVALUE-ONLY NEC TRAP (N1):
  eigenvalue margins silently restrict to Type-I points; a
  sampled-null cross-check is mandatory whenever a tensor's
  type is not already established (at beta=1.5 the eigenvalue
  NEC read +2.8e-7 while the sampled all-observer NEC was
  -3.36e-3).
- P6 FREE-FORM MARGIN FLOOR (n=11,264 evals, Track P at beta=0.05,
  (10,20)): at compactness M/R1 = 0.35 the best worst-margin found by
  any protocol is ~-2e-4 (adversarial DE objective on 893 pts), while
  named families pass at 0.383 — the free-form landscape does not
  undercut the named floor; if anything the floor is a property of
  the geometry (compactness vs beta), not of human shape-guessing.
  Adversarial training reduces fresh-sample violations by ~30x per
  round but the training-set objective saturates negative — pockets
  are dense in the design's neighbourhood, not isolated.
