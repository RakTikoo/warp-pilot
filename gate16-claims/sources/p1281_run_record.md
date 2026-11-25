# P128-1 run record — FU-P1194-1: compose the two escapes

Written BEFORE any deciding number of this item was computed
(machinery-gate numbers and seed projections are validation /
pose-fixing only). Registration: `../CHECKPOINT128.md` §P128-1,
fixed there. This file does not edit the checkpoint.

## 0. Grounding (stated on the face, per the evidence rule)

Phase 119's two halves (CHECKPOINT119 §P119-4;
`../../phase119/results/p1194_memo.md`): half (a)'s non-flat
profile emptied the alignment set but re-pinned as the
**all-sign pin** — at its best candidate's worst point (51;
tie set 44/50/52) all four canonical terms share one strict
sign, the revived □φ joining the pin instead of opposing it;
half (b)'s H_,φ(pi0) = 0 constraint emptied the alignment set
but re-pinned as the **single-channel pin** — with t_FA dead
and □φ ≡ 0 on the plateau, the EoM there is t_FB alone,
rel = 1 across the whole plateau. The memo's mechanism:
"Half (b) shows t_FB needs an opposing live channel at
plateau points; half (a) shows □φ can be that channel but
joined the pin at the searched candidates. The composed pose
is the direct test of whether a live □φ of the *opposing*
sign is attainable at the pin points." This item is that
test — a new pose (the composition), not a re-run of either
half.

Theory (fixed by the P101-5B action): H(φ) = 1 − ξφ² +
β_cφ/2 − β₂φ²/2, H_,φ(φ) = −(2ξ+β₂)φ + β_c/2. Canonical EoM
(`phase101/work/p1015_lib.py`: `canonical_terms`):
t_kin = □φ, t_pxx, t_FA = (½·H_,φ·R_bed)/P_X,
t_FB = (−μφ)/P_X, D_can = Σ|terms|, non-degenerate iff
D_can ≥ 1e-9. z = (ξ, β_c, β₂, pi0, shape, p₁, p₂, μ).
Front: Phase 48 bed, β = 1.1, 56-point subset, family B
(w_B from the stored Phase-76 B joint best), hinge theory of
P101-5 Part B.

Registered comparison — the P101-5B hinge best (family B,
start 6): z = (2.756667559450937, −1.498683175695639,
0.7811507949670238, 0.3385988091052908, 0.870145941019083,
1.222294121969537, 0.0639057960421364, −0.15512773896022752),
ρ₀ = 0.046611949162594764; subset_legal =
0.5892857142857143; EoM rel max (nondeg) =
0.9999999999784565; median = 0.22437629566157347;
n_nondeg = 56, n_deg = 0; health_ok = False; Frontier A =
0.000; alignment set {44} under the registered definition
(both force terms live at ≥ 1e-6 × max|term| at the point,
same strict sign, S_F = (|t_FA|+|t_FB|)/D_can ≥ 0.90,
|t_kin|/D_can ≤ 1e-6).

## 1. Machinery gate (runs first; failure stops the item)

Via `p1015_lib.canonical_terms` on
`phase101/results/p1015_partB_raw.json`: reproduce all
seven unique corpus configurations' stored EoM rel
max/medians within 1e-6, and the hinge best's alignment
set = {44} under the registered definition. Fluid for
family-B rows as in `p1015_partB.py` (the gate reads EoM
terms only, which are fluid-independent).

**Gate result (validation, recorded here before the
search): PASS.** Worst error 8.54938342342848×10⁻¹²
(tolerance 1e-6; runs_A[1] median, all other errors 0.0);
hinge alignment set = {44}, S_F = 1.0. Machinery:
`work/p1281_gate.py`, record in the results JSON.

## 2. Pose (fixed here, before numbers)

Same theory, bed, and 56-point subset. The scalar profile
is half (a)'s registered blend, verbatim in form:

  φ(r) = φ_ww(r; pi0, shape)
         + A · W(r) · sin(2π (r − 10)/λ),

φ_ww the stored 'wallwide' profile (`p182_engine.pi_splines`),
W the smootherstep window of `p1194_lib.py` (W = 0 below
r = 10, 1 on [11.25, 18.75], 0 above r = 20);
A ∈ [−0.35, 0.35], λ ∈ [2.0, 6.0]; jets by the PhiProfile
pattern (CubicSpline on the 4001-point grid), FD-verified
at rel agreement < 1e-6 before any read. FD verification
(h = 10⁻⁶, at pi0 = 0.34, shape = 0.87, A = 0.15, λ = 3.0,
as in half (a)): d1 rel 7.241610582640341×10⁻¹⁰, d2 rel
4.740598367972746×10⁻⁷ — both < 1e-6, PASS (recorded with
the gate; validation only).

AND half (b)'s constraint imposed by parametrisation,
verbatim: H_,φ(pi0) = −(2ξ+β₂)·pi0 + β_c/2 = 0, i.e. pi0
eliminated, pi0 = β_c / (2(2ξ+β₂)). Free vector
y = (ξ, β_c, β₂, shape, p₁, p₂, μ, A, λ, ρ₀); z is
reconstructed with pi0 in slot 3. Guards verbatim from
`p1194_run_record.md` §3: a large penalty residual fires
if |2ξ+β₂| < 0.2 or if the eliminated pi0 leaves
[0.02, 2.9]; deciding candidates must satisfy both
strictly. Two β_c branches, β_c ∈ [−4, −0.05] and
[0.05, 4] (the Phase-118 fence |β_c| ≥ 0.05 is a HARD
boundary of this pose). Bounds for the remaining free
variables: the P101-5B LO8/HI8 with pi0's slot removed
(ξ ∈ [0, 5], β₂ ∈ [−2, 2], shape ∈ [0.85, 1.15],
p₁, p₂, μ ∈ [−3, 3]), A ∈ [−0.35, 0.35], λ ∈ [2, 6],
ρ₀ ∈ [0, 0.05].

**Registered operational non-flatness (inherited):** at
the posed configurations, |t_kin|/D_can > 1e-6 at a
MAJORITY of the former plateau points (subset indices
0–43). A candidate failing this has not posed the
composition and the item reports exactly that.

**Projection pattern (§3 of the P119-4 run record, reused
verbatim):** closed-form scaled projection — keep
(ξ, pi0, shape, p₁, p₂, μ); solve (β_c, β₂) minimising
(β_c−β_c,h)² + (β₂−β₂,h)² subject to
β_c = 2(2ξ+β₂)·pi0 (1-D quadratic, solved exactly).
Projections computed at pose-fixing time (validation
only):

- Hinge best projected: z = (2.756667559450937,
  2.4512053601027106, −1.8937043136728997,
  0.3385988091052908, 0.870145941019083, 1.222294121969537,
  0.0639057960421364, −0.15512773896022752); H_,φ(pi0) = 0.0
  exactly; |2ξ+β₂| = 3.6196; positive branch. (Identical to
  half (b)'s recorded projection.)
- Half (a)'s best projected: z = (1.09396088842477,
  0.12677495730118515, −2.042212343664698,
  0.43502659549969874, 0.8501116945716124,
  0.08238464503952589, −2.1859449891197795,
  −0.026844566778504827); H_,φ(pi0) = 0.0 exactly;
  **|2ξ+β₂| = 0.14570943318484186 < 0.2** — the registered
  projection of half (a)'s best lands INSIDE the guard's
  penalty zone. It is used as a seed exactly as registered
  (a seed is not a deciding candidate); the penalty
  residual is active at that seed and any deciding
  candidate must satisfy the guard strictly. This is
  recorded here, before numbers, so it cannot be mistaken
  for a post-hoc excuse.
- Half (b)'s best already satisfies the constraint
  (projection = itself): z = (0.6364774799490114,
  −0.550546095484792, −1.6603977857177497,
  0.7104868883815072, 0.87329906344317, 1.7677186914997867,
  0.016255180150389955, −0.20395940295879322);
  |2ξ+β₂| = 0.3874428258197269; negative branch.

## 3. Search (fixed here, before numbers)

Joint least-squares on the P101-5 Part B pattern (residual
in `p791_main`'s form, as coded in
`p1015_partB.residuals` and reused by the p1194 drivers:
EoM rel array with degenerate points zeroed, 50 × EC hinge
residuals against the GR-reference scales, 50 ×
health-violation vector, via `p1194_lib.residuals_gen` on
the WallNF wall) over y above, family B;
max_nfev = 150 per start, checkpointed to
`work/p1281_ckpt.json` (driver appends one JSON record per
completed start). Best-candidate selection key (P101-5B
pattern, as in both halves): (Frontier A, subset_legal,
−eom_rel_max_nondeg, −eom_rel_med_nondeg), family B.

16 starts (≥ 12 registered), y = (ξ, β_c, β₂, shape, p₁,
p₂, μ, A, λ, ρ₀):

- Start 0 (registered (i)): half (a)'s best projected
  (§2), its (A, λ) carried: A = −0.033678153095735734,
  λ = 4.640050126789908, ρ₀ = 0.04996138256328585. Pos.
- Start 1 (registered (ii)): half (b)'s best on the blend
  at (A, λ) = (0.15, 3.0), ρ₀ = 0.04999986064344583. Neg.
- Start 2 (registered (ii)): half (b)'s best at half
  (a)'s best (A, λ) = (−0.033678153095735734,
  4.640050126789908), ρ₀ = 0.04999986064344583. Neg.
- Start 3: half (b)'s best at (−0.15, 3.0), same ρ₀. Neg.
- Start 4: half (b)'s best at (0.25, 4.5), same ρ₀. Neg.
- Start 5 (registered (iii)): hinge best projected (§2),
  blended at (0.15, 3.0), ρ₀ = 0.046611949162594764. Pos.
- Start 6: hinge projected at (−0.15, 3.0), same ρ₀. Pos.
- Start 7: hinge projected at (0.25, 5.0), same ρ₀. Pos.
- Start 8: half (a)'s best projected at (0.15, 3.0),
  ρ₀ = 0.04996138256328585. Pos.
- Starts 9–15: random feasible seeds, rng =
  `np.random.default_rng(12811)`: ξ ∈ [0, 2],
  β₂ ∈ [−2, 2] redrawn until |2ξ+β₂| ≥ 0.3;
  β_c = ±U[0.1, 3.5] with sign = sign(2ξ+β₂), redrawn
  until pi0 ∈ [0.05, 2.8]; shape ∈ [0.85, 1.15];
  p₁, p₂, μ ∈ [−3, 3]; A ∈ [−0.35, 0.35];
  λ ∈ [2, 6]; ρ₀ ∈ [0, 0.05]. Branch by sign of β_c.
  The drawn vectors are stored verbatim in the results
  JSON (`seed_starts`).

## 4. Reads and bars (registered in the checkpoint)

At the best candidate and at each seeded start (initial
configuration and optimised candidate): full
`p1015_lib.read` (subset_legal, EoM rel max AND median on
the non-degenerate set, n_nondeg/n_deg, health_ok,
Frontier A); the alignment set under the registered
definition with members' terms and shares; whether the
maximum-residual point is in the set; the term
decomposition at the maximum-residual point. PLUS the
composition's deciding anatomy at the best candidate:
the signed term decomposition at its maximum-residual
point, stating explicitly whether t_kin opposes t_FB
there and whether t_FA is at its posed zero; the
non-flatness test of §2; the guard values
(|2ξ+β₂|, pi0, |β_c|) at every candidate. Family A also
read at the best candidate (same z and (A, λ), no fluid).
Every read states its content set (56 subset points;
non-degenerate count stated).

- **JOINT PASS** (the programme's first on this front):
  Frontier A > 0 in `p1015_lib.read`'s exact sense
  (subset_legal > 0 AND eom_rel_max_nondeg ≤ 0.02 AND
  health_ok) AND n_nondeg ≥ 28 AND trap not firing
  (max over subset of |F_A + F_B| < 1e-9, or the trap
  subspace, at the deciding candidate = KILLED BY THE
  TRAP); second-pathed by full-margins recomputation
  (fast=False, `p1015_checker.py` pattern) BEFORE the
  memo calls it.
- **JOINT IMPROVEMENT** (milestone): Pareto-dominance
  over the hinge best: subset_legal ≥ 0.5892857142857143
  AND eom_rel_max_nondeg < 0.9999999999784565, OR
  subset_legal > 0.5892857142857143 AND
  eom_rel_max_nondeg ≤ 0.9999999999784565; second-pathed
  the same way.
- **COMPOSITION WORKS MECHANICALLY, FRONT STANDS:** the
  composed pose is posed as registered (non-flatness
  test passed; t_FA at its posed zero at plateau
  points) and neither bar is met — the composition's
  own binding form is NAMED with its deciding term and
  the max-residual point's full decomposition.
- **ESCAPE FAILS (composition form):** the composed pose
  cannot be posed as registered, or an alignment set in
  the registered sense re-forms carrying the
  maximum-residual point — the re-forming mechanism
  named (including any P_X → 0 blow-up re-formation).

A joint pass or improvement is a MILESTONE, reported
immediately on landing. If a search trajectory presses
|β_c| → 0.05, the item reports PRESSING THE PHASE-118
BOUNDARY and stops at the fence; the β_c = 0 slice is
never entered.

C12: pre-existing walls at β = 1.1; no transport claim; a
moved front is not a legal wall. float64 throughout.
INTERNAL only; nothing uploaded, nobody contacted.
