# PHASE 389 MEMO — PER-PROFILE STATIONARY SCALING AT H2

Charge: ledger entry 984 (Phase 383's named reopening,
memo SS7). Registration: work/p389_registration.md
(SS0–SS7), filed before any computation. Frame of
record: the VM (laptop NOT admitted — SS2).

## SS0. VERDICT

**STATIONARY LEVEL IMPROVES AT A MIXED CENTRE.**

The per-profile scaling search around Phase 379's H2
centre finds a mixed centre,

  (mu_S, mu_N, mu_M) =
  (0.9323593026620368, 1.1444417317708335,
   1.1445068359375)

applied to H2's total profiles (S -> mu_S*S,
N -> mu_N*N, M -> 1 + mu_M*(M - 1)), whose CONFIRMED
stationary joint level is

  **-1.757074x10^-4** (SET-244, band [10, 20]),

beating the bar L_stat(H2) = -1.942246x10^-4 by
**+1.851724x10^-5** (9.5%). The level remains
NEGATIVE — no energy-condition pass, no member; the
SS4 EC-pass rider does not fire. GATE REFERRAL: the
mixed centre is a new harvest candidate (SS7).

Consequence for the classification: Phase 381's
dwell -> harvest fixed point was a fixed point of
that ITERATION, not a local optimum of the
stationary level surface. The direction neither
lever searched — scaling the three profiles
independently at a fixed centre — pays. The A2
lineage's best stationary band level is now
-1.757074x10^-4 at the mixed centre.

## SS1. The act

Registration SS1's family: the centre is 379's
confirmed H2 incumbent (A2's total profiles at
mu = 1.15 plus its confirmed K = 17 corrections,
assembled verbatim by p381_lib.centre_profiles381);
the search variable is the scaling triple alone —
no spline corrections admitted. Protocol (SS3):
G1 coarse grid (mu in {0.90, ..., 1.10} per axis,
125 reads), G2 axis extension (+/- 0.15, 6 reads),
G3 refinement (3x3x3 at 0.025 around the grid best,
26 reads), G4 Nelder-Mead polish in the box
[0.80, 1.25]^3 (182 stored reads across two runs —
SS5's incident). Total 339 stored SET-244 reads;
the 600 cap did not bind. EVERY read is C1-feasible
(rho_min >= 0) and floor-feasible; rho_min stays in
[8.60, 8.94]x10^-5 across the whole search.

## SS2. Controls and frame admission

Record: results/p389_controls.json (VM),
results/p389_controls_laptop.json (laptop mirror).

VM — ALL PASS at diff 0.0:
- CTL-389-V: the two stored H2 vector artefacts
  agree, max diff 0.0.
- CTL-389-A: (1, 1, 1) reproduces 379's confirmed
  H2 record exactly (NEC -1.9422459891767227x10^-4,
  DEC -1.8982585080461558x10^-4, WEC
  -1.7768467393179327x10^-3, SEC
  -2.0943799294291577x10^-3, rho
  8.789653555683182x10^-5, polished depth
  -1.4402430840320638x10^-4 — all diff 0.0).
- CTL-389-M: (1.225, 1.30, 1.30) reproduces 383
  memo SS6 (c)'s stationary verification exactly
  (NEC -1.9954038171026746x10^-4, DEC
  -1.287489042939161x10^-4 — diff 0.0).
- CTL-389-F: floors hold at the centre (N min
  1.150001, M min 1.124784 on FINE_R).

**FRAME ADMISSION: LAPTOP NOT ADMITTED** —
eleventh occurrence of the lineage pattern.
CTL-389-A on the laptop: NEC diff
6.386751250093265x10^-7, WEC diff
6.315941396222054x10^-6, SEC diff 4.231x10^-6 —
the NEC/WEC diffs are DIGIT-FOR-DIGIT 383's
CTL-383-H2S values on the same centre — while
DEC, rho and the polished depth agree at roundoff
(<= 1.1x10^-19). CTL-389-M: NEC diff 5.257x10^-8.
SET statistics differ; pointwise values agree.
All deciding reads are VM reads.

## SS3. The confirmed mixed centre (SS5 protocol)

Confirmation record: results/p389_confirmation.json.
The full set_read389 of the best point reproduces
its stored screen minima at diff 0.0 (NEC, DEC,
rho); the centre's own confirmation likewise.

| quantity | H2 centre (1,1,1) | mixed centre |
|---|---|---|
| joint level (SET-244) | -1.942246x10^-4 | **-1.757074x10^-4** |
| NEC min | -1.942246x10^-4 @ r 16.220 | -1.757074x10^-4 @ r 12.561 |
| DEC min | -1.898259x10^-4 @ r 19.634 | -1.567069x10^-4 @ r 19.634 |
| rho min | +8.789654x10^-5 | +8.936713x10^-5 |
| WEC min | -1.776847x10^-3 | -1.176749x10^-3 |
| SEC min | -2.094380x10^-3 | -2.149650x10^-3 |
| polished depth | -1.440243x10^-4 | -9.660225x10^-5 |
| worst-null at NEC argmin | -1.943288x10^-4 | -1.770370x10^-4 |

The improvement survives at pointwise grade: the
exact worst-null at the mixed centre's SET NEC
argmin (-1.770370x10^-4) still beats L_H2 by
+1.721x10^-5. The depth improves by +4.742x10^-5
and sits far above the C2 material bar (-0.0034).
The binding coordinate remains NEC; its argmin
MOVED, from r = 16.220 at the centre to r = 12.561
at the mixed centre. The DEC argmin did not move
(r = 19.634, the centre's own site).

## SS4. Anatomy (SS6; record: p389_anatomy.json)

(a) GRADIENT AT THE CENTRE. The quadratic fit over
the non-saturated G1 cube (116 points, max resid
2.09x10^-5 — the min(NEC, DEC) kink limits
quadratic fidelity, stated) gives the centre
gradient per unit mu:

  dJ/dmu_S = -1.096x10^-4,  dJ/dmu_N = +1.115x10^-4,
  dJ/dmu_M = +0.821x10^-4.

S wants to SHRINK, N and M want to GROW — the
centre is not stationary in the scaling space at
all. Axis finite differences agree in sign for S
(-1.49x10^-4 at h = 0.05) and N (+1.54x10^-4). The
mu_M axis alone is deceptive: both +/- 0.05 steps
from the centre LOSE ~1.5-1.8x10^-5 (the axis dips
both ways); the M gain is cooperative, realised
only with N grown and S shrunk (the fit's S-N
cross term, +3.84x10^-4, is the size of the
diagonal terms).

(b) BOWL, NOT RIDGE. The fit's Hessian eigenvalues
at the centre are all negative (-3.33x10^-3,
-8.38x10^-4, -6.1x10^-5): the smooth surface is
concave there, with no rising curvature direction.
Combined with the nonzero gradient, the centre
sits on the FLANK of an inverted bowl whose peak
the polish located at (0.932, 1.144, 1.145). At
the peak mu_N and mu_M agree to 6.5x10^-5 — the
optimum is near-diagonal in (N, M) with S
off-diagonal below 1. What stops the climb: the
NEC margin at the new site r = 12.561; the second
polish run (120 evaluations from the point) found
no improving step — the simplex collapsed onto
the point, final neighbourhood levels within
~10^-8.

(c) THE mu_M NEAR-IDENTITY (observation). Along
the mu_M axis and the uniform diagonal the joint
levels agree to roundoff: J(1, 1, mu) =
J(mu, mu, mu) to <= 3.4x10^-19 at mu in
{0.95, 1.05, 1.10}, with NEC and DEC minima and
both argmin radii also agreeing (NEC @ r 12.317
for mu > 1, @ 17.683 for mu = 0.95; DEC @ 19.634).
At those points the binding margins are, to
roundoff, functions of mu_M alone — the binding
sites are M-carried. This is also why 381's
uniform bottoms and a pure-M move read alike.

(d) THE SATURATED CORNER. Nine G1 points — mu_N,
mu_M in {0.90, 0.95} (one at mu_M = 1.0) with
mu_S >= 1.0 — are DEC-SATURATED: dec_min pinned at
~ -1.0000005 (DEC argmin r = 17.683), Phase 387's
past-branch pinning appearing in the scaling
space. They are C1-feasible, but their joint is a
branch flag, not a level; they rank last, are
excluded from the fit, and no axis pair through
the centre touches them. The optimum goes the
opposite way (N, M up).

(e) BINDING-COORDINATE SWITCHES. Along -mu_S and
+mu_N from the centre the joint becomes DEC-bound
(the DEC margin at r = 19.634 takes over); the
centre and the optimum are NEC-bound. Along the
diagonal the level falls both ways from mu = 1
(0.95: -2.084363x10^-4; 1.05: -2.119274x10^-4;
1.10: -2.137551x10^-4) — 381's uniform verdict
reproduced inside the grid, and now explained:
the diagonal is the ONE direction in which the
three gradients cancel.

(f) BAND EDGES (SS6 (d)). Scaling acts on the
whole profiles; the scaled totals at the band
edges, centre -> mixed centre: r = 10: S 0.804862
-> 0.750421, N 1.150001 -> 1.316109, M 1.124784 ->
1.142817; r = 20: S -7.891419x10^-3 ->
-7.357637x10^-3, N 1.202541 -> 1.376238, M
7.900060 -> 8.897166. The band-edge freedom is
INHERITED from H2 (379 SS6), not added by scaling;
no end-clamp re-read was registered in this phase.
The gate's obvious first check is the end-clamp
at the new centre: at H2 the clamp cost 1.45x10^-5
(Gate-41's rider), the same order as this gain
(+1.852x10^-5) — the margin's survival under
clamping is UNMEASURED here and is stated as the
referral's caveat, not assumed either way.

## SS5. Incidents

- The first G4 polish run was killed by a runtime
  restart after 63 stored reads (the 379
  precedent). Every evaluation is flushed to disk
  per read, so no computed read was lost; the
  polish was relaunched from the stored best
  point and completed at nfev = 120, returning
  EXACTLY its start point as the optimum. The two
  runs' reads are one stored set (G4: 182).
- The laptop admission mirror initially lacked
  the root-level programme modules (verify_metric,
  shell); two admission attempts aborted on import
  before the mirror was completed. The deciding
  (third) run is the recorded one (SS2).
- The first draft of p389_lib carried the
  cos(phi)/cos(theta) transcription slip in the
  polish objective (379's disclosed defect class);
  caught against p379_lib BEFORE any run — the
  controls' depth reproduction at diff 0.0
  confirms the corrected form.

## SS6. Classification consequence

The composed ceiling of the A2-lineage family
restates: the best stationary band level is
-1.757074x10^-4 at the mixed centre (0.932, 1.144,
1.145) on H2. Phase 381's convergence verdict
stands as stated — the dwell -> harvest ITERATION
converged — but its object was the iteration's
fixed point, and the fixed point is not a local
optimum of the level surface: the gradient at H2
in the scaling space was never zero. Named
follow-ups (not run): (i) 379's spline-correction
harvest re-centred at the mixed centre; (ii) a
dwelling pose around the mixed centre (the cycle
re-posed at the new centre, per the charge's gate
referral note); (iii) per-profile scaling iterated
with (i). Each starts from a centre 1.852x10^-5
above the old fixed point.

## SS7. Fences and accounting

All levels are BAND-POSED [10, 20] SET-244
SAMPLER-M figures on the A2 lineage, beta = 1.1.
Phase 356's full-extent caveats travel (the
lineage's stationary full-extent levels restate
to ~ -1.44x10^-3 over [10, 60]); nothing here is
a full-extent read and no level is a member in
the energy-condition sense. No EC-pass wording:
the confirmed level is negative. The verdicts of
379, 381 and 383 stand as stated; this phase
tests the one direction 383 named. No spinor
match; no sustainment, front/joint, transport or
drive claim.

Three-goal accounting. Goal 1 (FTL drive): the
extended-class stationary pressure level improves
again, -1.942246x10^-4 -> -1.757074x10^-4 in the
band — the wall moved 9.5%, it did not break; no
EC pass, no member, no transport content. Goal 2
(wormhole): untouched. Goal 3 (subluminal record):
untouched.

DESK: NO DATA CONTACT.

Artefacts: work/p389_registration.md, p389_lib.py,
p389_controls.py, p389_search.py, p389_confirm.py,
p389_anatomy.py; results/p389_controls.json,
p389_controls_laptop.json, p389_screens.jsonl
(+ parts/), p389_search_summary.json,
p389_confirmation.json, p389_anatomy.json, search
and polish logs.
