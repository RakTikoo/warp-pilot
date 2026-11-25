# GATE-36 — WORKER B MEMO: CONTROLS (SPINOR SIDE) + ITEM 2

Independent builder `g36_spinor.py` (Dirac superposition from the field
definition, m = 1; direct + pairwise paths; own Segre classifier; own
FD Jacobian), driver `g36_item2.py`, recovery `g36_item2_recover.py`.
No phase/gate spinor code imported for computation; stored artefacts
read as data only. Seeds: ladder base 3601, perturbation stream 3602.
Full numbers: `g36_item2_results.json`; all N = 6 solutions at the bar:
`g36_item2_solutions.json` (3 solutions, full θ).

## CONTROLS — ALL PASS (run before any fit read)

**CTRL-S3 (builder self-consistency).** Direct vs pairwise paths:
on 8 random mode sets max abs component diff 1.42×10⁻¹³ at max
relative diff 9.56×10⁻¹⁶ (round-off class for O(10–100) tensor
entries); on the stored Phase 320 winner max diff 2.79×10⁻¹⁷; on the
stored Phase 313 winner 2.47×10⁻¹⁶. The pairwise path was used in
fits only after this passed. The builder also reproduces the stored
winner's spinors U from (p, a) at diff 0.0.

**CTRL-S1 (Phase 320's stored winner under this builder).** Direct-path
per-site residuals 7.0115436303192264×10⁻¹⁵ / 7.801776409152642×10⁻¹⁴ /
8.230813708013984×10⁻¹⁴ / 1.2959098518061706×10⁻¹⁵ — **diff 0.0 on every
site** vs the stored values; densities likewise diff 0.0 on every site.
FD Jacobian at the stored winner (central FD, h_j = 10⁻⁶·max(1,|θ_j|)):
**σ_min = 3.994300×10⁻⁴** (stored 3.994×10⁻⁴), **σ_max = 3.909267×10³**
(stored 3.909×10³), **rank 40** at 10⁻¹⁰ relative (stored: full row
rank 40). Singular-value tail: …, 0.21990, 0.042944, 0.011693,
0.0083539, 0.00039943 — the smallest value is isolated, ~21× below the
next. (This is Item 3's E3(i) input.)

**CTRL-S2 (Phase 313's stored winner under this builder).** Direct-path
max R = 3.253339860306391×10⁻¹³ — the stored 3.253×10⁻¹³ exactly.
Jacobian at that solution under this recipe: **σ_min = 0.034753**,
σ_max = 6.389650×10³, rank 40. (No stored gate value exists for this
exact quantity; Gate-34's 0.0272 was at Gate-34's own solution on the
same targets — same class.)

## ITEM 2 — THE LADDER ON THE POINTWISE TARGETS (own starts)

Bar: max R ≤ 1×10⁻⁹ (direct path; ladder screened on the pairwise
path, verified direct). Per-start outcomes all persisted in the
results file.

| N | starts | best max R (pairwise) | at bar |
|---|---|---|---|
| 4 | 6 random | 5.523×10⁻⁴ | 0/6 |
| 5 | 6 random | 5.806×10⁻⁵ | 0/6 |
| 6 | 1 warm + 8 random | **1.128×10⁻¹³** | **3/9** |
| 8 | 1 warm + 3 random | 4.054×10⁻¹² | 4/4 |

The transition sits at the counting threshold 7N − 1 ≥ 40 exactly as
in Phase 320 (its ladder: N = 4 best 7.317×10⁻⁴ 0/6; N = 5 best
6.215×10⁻⁵ 0/6; N = 6 best 8.231×10⁻¹⁴ 4/9; N = 8 best 8.878×10⁻¹²
9/9). My three N = 6 solutions at the bar (direct max R): warm0
1.128×10⁻¹³, rand2 2.654×10⁻¹³, rand0 2.117×10⁻¹² — all θ persisted
for Item 3's census.

## BEST N = 6 SOLUTION (warm0 lineage) — DIAGNOSTICS

- Direct-path per-site residuals: 9.373×10⁻¹⁵ / 1.069×10⁻¹³ /
  1.128×10⁻¹³ / 1.501×10⁻¹⁵ (max 1.128×10⁻¹³, ~8,900× inside the bar).
- Density at the match vs target ρ per site: fit 6.263182190010×10⁻⁴ /
  6.818808066128×10⁻⁴ / 6.257630013852×10⁻⁴ / 1.172277511696×10⁻⁴ vs
  target 6.263182190002×10⁻⁴ / 6.818808066078×10⁻⁴ /
  6.257630013908×10⁻⁴ / 1.172277511698×10⁻⁴ — the target's own,
  **positive at all four sites** (diffs ≤ 5.6×10⁻¹⁵).
- Segre types: fit I / IV / I / IV = target I / IV / I / IV (own
  classifier, η·T eigenvalues).
- Dirac residuals of the modes: max 1.91×10⁻¹⁷ (on shell).
- Global scale |a|² = 0.01020438976676859 (Phase 320's winner:
  0.010204382146024456 — same warm lineage, agreement to 7.5×10⁻⁷
  relative).
- **D-a (per-site amplitude refits, p and spin directions frozen):**
  every site returns the joint solution — per-site R after refit
  equals the joint direct residual at that site, α = 1, and the
  α-route implied per-site scale Σ_j|a_j|²|α_j|² equals |a|² to
  1.7×10⁻¹⁸ at all four sites. One field, one global scale.
- **Leg-3 (kstar form — both forms run; kstar is present in the
  p320 targets file):** per-site implied s² = |tkk_target|/|tkk_unit|
  agrees with |a|² to ≤ 7.3×10⁻¹⁴ absolute (S1 4.0×10⁻¹⁴, S2
  7.3×10⁻¹⁴, S3 2.6×10⁻¹⁴, S4 2.3×10⁻¹⁵) — the same class as Phase
  320's ≤ 5.1×10⁻¹⁴.

## JACOBIAN AT MY BEST N = 6 SOLUTION

40 × 42, central FD, h_j = 10⁻⁶·max(1,|θ_j|): **full row rank 40**
(10⁻¹⁰ relative), σ_max = 3.909271×10³, **σ_min = 3.994302×10⁻⁴**.
Full singular-value list in the results file; tail: …, 0.42680,
0.21990, 0.042944, 0.011693, 0.0083539, 0.00039943 — same isolated
thin direction as at the stored winner, whose tail under this recipe
is numerically the same (σ_min 3.994300×10⁻⁴). Recipe stability:
σ_min = 3.994303×10⁻⁴ at h = 10⁻⁵, 3.994302×10⁻⁴ at h = 10⁻⁶,
3.994300×10⁻⁴ at h = 10⁻⁷ — stable to ~5×10⁻⁷ relative across two
decades of h. **The thin σ_min of C-320-3 reproduces at an
independently-fit solution under an independent builder and recipe,
and is not an FD artefact.**

## PERTURBATION LADDER AT MY BEST N = 6 SOLUTION (seed 3602)

Componentwise symmetric noise ε·|That_s|_F, 2 draws per rung, warm +
1 fresh start per draw, best direct max R against the perturbed
targets:

| ε | draw 0 | draw 1 | Phase 320 stored |
|---|---|---|---|
| 1×10⁻¹² | 1.122×10⁻¹³ | 1.125×10⁻¹³ | 8.3×10⁻¹⁴ |
| 1×10⁻⁹ | 7.311×10⁻¹⁴ | 7.333×10⁻¹³ | 1.0×10⁻¹² |
| 1×10⁻⁶ | 3.913×10⁻¹³ | 1.029×10⁻¹³ | 2.0×10⁻¹³ |
| 1×10⁻⁴ | 2.089×10⁻¹³ | 2.340×10⁻¹⁴ | 8.1×10⁻¹⁴ |

**The bar is re-achieved at every rung and every draw.** Fitted
densities track the perturbed targets' densities throughout and stay
positive (minimum fitted ρ ≈ +1.172×10⁻⁴ at every rung).

## PROCESS NOTE — RESTART AND RECOVERY (disclosed)

The VM restarted mid-run, killing the driver during the perturbation
ladder, after all controls, all four ladder arms, the best-solution
diagnostics and the Jacobian had completed and persisted per-arm.
The ladder tail was completed by `g36_item2_recover.py` — the
driver's perturbation block verbatim (identical seeds/stream), gated
on the persisted checkpoint: its ε = 10⁻¹² draw 0 reproduces the
executed run's logged best max R 1.122×10⁻¹³ exactly. No completed
arm was re-run. The main driver's wall time was lost with the
restart; the recovery segment's wall time (2413 s) is recorded in
the results file.

## BOTTOM LINE FOR THE PARENT

C-320-1, C-320-2 and the σ_min / perturbation content of C-320-3 all
reproduce under a fully independent builder, optimiser starts and
Jacobian recipe: the stored match reads at diff 0.0, the ladder
transition sits at the same counting threshold, my own fits close at
1.128×10⁻¹³ with the target's positive densities and Segre types,
D-a and Leg-3 both return one global scale, σ_min = 3.994×10⁻⁴ is
confirmed at both the stored winner and my solution with h-stable
FD, and the perturbation ladder re-closes at every rung. The three
persisted N = 6 solutions (one warm-lineage, two random) are on disk
for Item 3's census.
