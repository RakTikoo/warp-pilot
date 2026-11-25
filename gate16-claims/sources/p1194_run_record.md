# P119-4 run record — FU-P1083-1 + FU-P1083-2 (the alignment set's two named escapes)

Written BEFORE any deciding number of this item was computed
(machinery-gate numbers are validation only). Registration:
`../CHECKPOINT119.md` §P119-4, fixed there. This file does not
edit the checkpoint.

## 0. Grounding (stated on the face, per the evidence rule)

Phase 108's P108-3 verdict: on the coupling-force front
(Phase 48 bed, β = 1.1, 56-point subset, hinge theory of
P101-5 Part B), the corpus profiles are flat (φ ≡ pi0) over
the inner shells, so □φ ≈ 0 plateau-wide, the EoM there is a
pure force balance, and the force terms align wherever
μ·H_,φ(pi0)·R_bed < 0. Point 44 is the alignment set {44}
at the hinge best and carries the worst residual (1.000000)
in 4 of 5 live-channel corpus configurations. The two
registered escapes run here as halves (a) and (b).

Theory (fixed by the P101-5B action): H(φ) = 1 − ξφ² +
β_cφ/2 − β₂φ²/2, H_,φ(φ) = −(2ξ+β₂)φ + β_c/2
(`phase76/p761_lib.py`: `H_of`, `dH_of`). Canonical EoM
(`phase101/work/p1015_lib.py`: `canonical_terms`):
t_kin = □φ, t_pxx, t_FA = (½·H_,φ·R_bed)/P_X,
t_FB = (−μφ)/P_X, D_can = Σ|terms|, non-degenerate iff
D_can ≥ 1e-9. z = (ξ, β_c, β₂, pi0, shape, p₁, p₂, μ).

Registered comparison — the P101-5B hinge best (family B,
start 6): z = (2.756667559450937, −1.498683175695639,
0.7811507949670238, 0.3385988091052908, 0.870145941019083,
1.222294121969537, 0.0639057960421364, −0.15512773896022752),
ρ₀ = 0.046611949162594764, family-B fluid w from the stored
Phase-76 B best; subset_legal = 0.5892857142857143;
EoM rel max (nondeg) = 0.9999999999784565; median =
0.22437629566157347; n_nondeg = 56, n_deg = 0;
health_ok = False; Frontier A = 0.000; alignment set {44}
under the registered definition (both force terms live at
≥ 1e-6 × max|term| at the point, same strict sign,
S_F = (|t_FA|+|t_FB|)/D_can ≥ 0.90, |t_kin|/D_can ≤ 1e-6).

## 1. Machinery gate (runs first; failure stops the item)

Via `p1015_lib.canonical_terms` on
`phase101/results/p1015_partB_raw.json`: reproduce all
seven unique corpus configurations' stored EoM rel
max/medians within 1e-6 (the seven: direct B76_mu0,
direct A76_mu0, runs_B[0..2], runs_A[0..1]; best_A/best_B
duplicate runs entries), and the hinge best's alignment
set = {44} under the registered definition above.
Fluid for family-B rows: (w_B, ρ₀) with w_B from the
stored Phase-76 B joint best, as in `p1015_partB.py`.

## 2. Half (a) — non-flat profile (FU-P1083-1), pose fixed here

Same theory, same bed, same 56-point subset. The scalar
profile is replaced by the following stated closed-form
blend (envelope option 2 of the registration):

  φ(r) = φ_ww(r; pi0, shape)
         + A · W(r) · sin(2π (r − 10)/λ),

where φ_ww is the stored 'wallwide' profile
(`p182_engine.pi_splines`), and W is the smootherstep
window of the Phase-79 counterweight pattern
(`p791_lib._window`): W = S((r−10)/1.25) ·
(1 − S((r−18.75)/1.25)), S = smootherstep — W = 0 below
r = 10, 1 on [11.25, 18.75], 0 above r = 20, so the blend
lives inside the wallwide support and the exterior data
are unchanged.

Profile parameters (searched, bounds fixed here):
A ∈ [−0.35, 0.35], λ ∈ [2.0, 6.0]. The hinge plateau
value is pi0 ≈ 0.34, so |A| up to ≈ pi0 is in-envelope;
λ spans roughly 2–7 blend oscillations across the shell.

Jets: by the PhiProfile pattern — φ is built as a
CubicSpline on the same 4001-point grid on [0, 60] as
`pi_splines`, d1/d2 are the spline derivatives, and the
jet formulas are `PhiProfile.pi_jets` verbatim. Before
any read, d1 and d2 are FD-verified against the spline
itself (central FD of cs for d1, of d1 for d2) at the 56
subset radii: required max relative agreement < 1e-6
(relative to the max |derivative| over the subset).

Registered operational non-flatness: at the posed
configurations, |t_kin|/D_can > 1e-6 at a MAJORITY of the
former plateau points (subset indices 0–43). A profile
failing this at its own best candidate has not posed the
escape and the half reports exactly that.

Search: joint least-squares on the P101-5 Part B pattern
(residual in `p791_main`'s form, as coded in
`p1015_partB.residuals`: EoM rel array with degenerate
points zeroed, 50 × EC hinge residuals against the
GR-reference scales, 50 × health-violation vector) over
(z, A, λ, ρ₀ ∈ [0, 0.05]) for family B; bounds for z are
the P101-5B LO8/HI8. ≥ 12 starts, including the hinge
best re-posed on the non-flat profile (several (A, λ)
seedings). max_nfev = 150 per start (P101-5B pattern),
checkpointed to `work/p1194_halfA_ckpt.json`. Family A
also read at the best candidate (same z, no fluid).

## 3. Half (b) — H_,φ(pi0) = 0 (FU-P1083-2), pose fixed here

Stored 'wallwide' profile family. The constraint
H_,φ(pi0) = −(2ξ+β₂)·pi0 + β_c/2 = 0 is imposed by
parametrisation: pi0 is eliminated,
pi0 = β_c / (2(2ξ+β₂)). Free variables:
(ξ, β_c, β₂, shape, p₁, p₂, μ, ρ₀). Guards (stated here):
a large penalty residual fires if |2ξ+β₂| < 0.2 or if the
eliminated pi0 leaves [0.02, 2.9]; deciding candidates
must satisfy both strictly. Because least_squares needs
one box, the search runs in two β_c branches,
β_c ∈ [−4, −0.05] and β_c ∈ [0.05, 4] (other bounds:
P101-5B LO8/HI8 with pi0's slot removed), ≥ 12 starts in
total including the hinge best projected onto the
constraint set (projection computed by bounded
least-squares minimisation of the scaled distance to the
hinge z subject to the constraint and the fence; the
projected point is recorded in the results file).

HARD BOUNDARY (Phase 118 owns β_c = 0): |β_c| ≥ 0.05 at
any deciding candidate. If the best candidate presses
the fence, the half reports PRESSING THE PHASE-118
BOUNDARY and stops at the fence.

Trap gate verbatim from P101-5B (`p1015_lib.read`):
trap_fires iff max over subset of |F_A + F_B| < 1e-9 or
the trap subspace (|β_c| < 1e-12, |2ξ+β₂| < 1e-12,
|μ| < 1e-12) holds at the deciding candidate =
KILLED BY THE TRAP.

## 4. Reads and bars (both halves; registered in the checkpoint)

At each half's best candidate and at the hinge-seeded
start: full `p1015_lib.read` (subset_legal, EoM rel
max/median on the non-degenerate set, n_nondeg/n_deg,
health_ok, Frontier A), the alignment set under the
registered definition with members' terms and shares,
whether the maximum-residual point is in the set, and
the term decomposition at the maximum-residual point.
Best candidate selection key (P101-5B pattern, extended):
(Frontier A, subset_legal, −eom_rel_max_nondeg,
−eom_rel_med_nondeg), family B. Every read states its
content set (56 subset points; non-degenerate count
stated).

- JOINT PASS: Frontier A > 0 (subset_legal > 0 AND
  eom_rel_max_nondeg ≤ 0.02 AND health_ok) AND
  n_nondeg ≥ 28 AND trap not firing; second-pathed by
  full-margins recomputation (fast=False,
  `p1015_checker.py` pattern).
- JOINT IMPROVEMENT: Pareto-dominance over the hinge
  best: subset_legal ≥ 0.5892857142857143 AND
  eom_rel_max_nondeg < 0.9999999999784565, OR
  subset_legal > 0.5892857142857143 AND
  eom_rel_max_nondeg ≤ 0.9999999999784565; second-pathed.
- ESCAPE WORKS MECHANICALLY, FRONT STANDS: alignment set
  empty or max-residual point exited it, neither bar met
  — new binding form named.
- ESCAPE FAILS: alignment set still carries the
  max-residual point — re-forming mechanism named.

A joint pass or improvement is a MILESTONE and is said
so in the first line of the memo/report.

C12: pre-existing walls at β = 1.1; no transport claim;
a moved front is not a legal wall. float64 throughout.
INTERNAL only; nothing uploaded, nobody contacted.
