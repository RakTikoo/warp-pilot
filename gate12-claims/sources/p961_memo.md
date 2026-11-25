# P96-1(b)+(c) — THE HARD FRAME-CONSTRAINED SOLVE + THE BAND ANATOMY — MEMO

**Item:** P96-1(b) (FU-P881-1) and P96-1(c) (FU-P881-3), Phase 96.
**Date:** 2026-11-22. **Registration:** `phase96/CHECKPOINT96.md`
§P96-1(b), §P96-1(c) (binding, not edited by this worker).
**Category (exact):** subluminal ACCELERATING shell,
Bobrick–Martire class (Le, arXiv:2606.22531). Nothing in this memo
is an FTL claim, in any wording. INTERNAL only; nothing uploaded;
nobody contacted. Phase 88/80 records read-only throughout.

## ★ MILESTONE — (x, λ) = (0.7, 0.09): CONFIRMED AT OUR BARS

A hard frame-constrained solve (timelikeness imposed as a
constraint of the solve, δ = 1×10⁻³, exact autodiff Jacobians of
residual AND constraints) produced an L = 6 coefficient set at
(0.7, 0.09) that meets the inherited closure bar under BOTH
evaluations and passes the full Phase-80-pattern audit:

- solver's own (JAX) residual, dense61: max|[h]| = **1.9893×10⁻³**
  (bar 2.0×10⁻³; recomputed by the checker from the stored set);
- Phase 80 independent FD audit: max|[h]| = **1.9891×10⁻³**;
- **finiteness: 0 non-finite rows of 221** (its own clause);
- Type-I at every grid point; worst-observer DEC margin
  **+1.3460×10⁻²** at θ = 2.4775; eigenvalue margin +1.3460×10⁻²;
  min discriminant +1.307×10⁻³; poles +3.788×10⁻² (rear, Type-I)
  and +2.975×10⁻² (front);
- frame margin: JAX fm_min on the registered constraint grid
  **+4.288×10⁻³** ≥ δ, FD audit fm_min +4.288×10⁻³ — the shared
  frame is timelike at every audit angle;
- sampled-observer cross-check at the binding angle +1.087×10⁻²;
  h-ladder at the binding angle 0.013239 / 0.013460 / 0.013515 /
  0.013533 (spread 2.9×10⁻⁴, converged, sign-stable).

The confirming set is the SLSQP-from-zeros run's best feasible
iterate, stored independently in `results/p961_solve.json` under
`x0.7_L6_fromZeros`. Checker: **23/23 PASS**
(`results/p961_check.json`). This is the first auditable closure
of a Le high-x pin in the programme: Phase 80's confirmations at
x ∈ {0.1, 0.2, 0.3} are untouched, and the paper's own margin at
this pin (21×10⁻³, for the paper's unpublished set) is a different
set's number — our set's worst margin is +13.5×10⁻³.

## VERDICTS (registered forms, per pin) — P96-1(b)

- **(0.7, 0.09): CONFIRMED AT OUR BARS** (above).
- **(0.5, 0.14): STILL UNCLOSEABLE** at our bars — a METHODS
  result about our solvers, not a physics result about the
  paper. The constrained floor is quantified (below) and the
  obstruction is named one level deeper than Phase 88's.

Neither pin is REFUTED: at x = 0.5 no auditable set meets the bar
(the refutation form requires one), and at x = 0.7 the pin
confirms.

## 1. The instrument (differs in kind from Phase 88's failed routes)

scipy **SLSQP** with **exact autodiff Jacobians of both** the
residual objective (½‖[h]‖² on the author's 21-point grid) and
all 92–148 inequality constraints −h_ττ(θ) ≥ δ = 1×10⁻³, built
from the same JAX geometry kernel as the residual of record
(`phase88/work/p881_jax.py`, reused unmodified). Constraint grid:
author 21-pt ∪ rear band θ∈[2.0,π] (spacing 0.05; one polish run
at 0.02, a strengthening within the registered "≤ 0.05") ∪ both
pole endpoints. NOT a penalty (Phase 88 D4) and NOT unconstrained
+ selection (Phase 88 D–G): infeasible starts are feasibility-
restored by the solver itself. **Re-gate: PASS** (fresh, this
item: dipole poles −2.009572×10⁻⁴ / −1.226338×10⁻⁴ vs targets
−2.0096×10⁻⁴ / −1.2263×10⁻⁴; confirmed-pin poles +1.728328×10⁻³ /
+9.102104×10⁻³; all diffs ≤ 2.8×10⁻⁸). **Constraint cross-check:
PASS** — JAX kernel vs Phase 88's stored FD spot reads of h_ττ:
max |diff| 5.0×10⁻⁵ (x = 0.5) / 4.8×10⁻⁵ (x = 0.7), the FD
h = 0.01 truncation scale; fm finite at both poles.

## 2. P96-1(b) per-strategy quantification

x = 0.7, λ = 0.09, L = 6 (bar 2.0×10⁻³):

| Strategy (start) | Outcome |
|---|---|
| SLSQP from strategy-A set | converged (nit 115, success): dense61 7.80×10⁻⁴, fm_min = δ — **but audit: 1 non-finite row** at θ = 2.7202 (FD fm −5.7×10⁻⁵, an inter-node dip between constraint nodes) → not auditable, NOT the confirming set |
| SLSQP from zeros | **CONFIRMING SET** (best feasible iterate, dense61 1.9893×10⁻³; final iterate 2.171×10⁻³ also feasible) — full audit passes (above) |
| SLSQP polish at rear spacing 0.02, from A-lineage set | diverged into a NaN geometry region (nit 13); set not auditable; recorded as a failed strategy |
| SLSQP L = 8 from A set (pad) | success, feasible, dense61 9.90×10⁻⁴ (best feasible iterate 7.78×10⁻⁴) — audit: same single non-finite row (θ ≈ 2.72) as its L = 6 parent → not auditable |

x = 0.5, λ = 0.14 — the CONSTRAINED FLOOR (best achievable
max|[h]| under fm ≥ δ; every run's optimum sits ON the
constraint, fm_min = δ to ~10⁻⁶):

| Strategy | L | Best strictly-feasible dense61 | Final dense61 |
|---|---|---|---|
| from A set | 6 | — (no strictly-feasible iterate; final at fm = δ−9×10⁻⁷) | 3.248×10⁻² |
| from zeros | 6 | 1.757×10⁻² | 1.536×10⁻² (fm = δ−2×10⁻⁷) |
| λ-continuation under constraint (λ = 0.08 step) | 6 | 2.059×10⁻² at λ = 0.08 | 2.059×10⁻² |
| λ-continuation under constraint (λ = 0.14) | 6 | 1.864×10⁻² | 1.735×10⁻² |
| from zeros-best (pad) | 8 | **1.606×10⁻²** | 2.390×10⁻² |

**Constrained floor at x = 0.5: ≈ 1.6×10⁻² (L = 8) / 1.76×10⁻²
(L = 6) — about 8× the bar, at both L.** Obstruction, one level
deeper than Phase 88's "every path trades fm for [h]": under the
hard constraint the floor is set by the constraint itself — in
every strategy the optimum is constraint-active in the rear
band, and even at λ = 0.08 (half-way to the pin) the constrained
floor (2.06×10⁻²) is already 10× the bar while the unconstrained
closure there is 5.6×10⁻³. L = 8 was run at both pins per the
registered rule (x = 0.5: L = 6 returned a quantified floor;
x = 0.7: L = 6 closed healthy) — reasons recorded here and in
the run record.

## 3. P96-1(c) — BAND ANATOMY verdict

**Verdict (strongest form the scores support, MIXED):** the
frame degeneracy is **not a truncation artefact** — hypothesis
(ii) is excluded as the whole story. On every closed set found
it is a property of the set's shell geometry in the rear band:
the shell's tangent space there is driven **within ~1×10⁻⁶ of
admitting no timelike direction** from the whole constructible
seed class (iii, in this weakened, class-scoped form), and the
shared τ-seed's meridional tilt is what carries it from null to
spacelike (i, as amplifier, not as sole cause). It is **not** a
property of the pin itself: at (0.7, 0.09) the constrained solve
exhibits a closed set at the same pin whose frame margin is
+4.3×10⁻³ everywhere — the degeneracy belongs to the
unconstrained-optimum basin, escapable at x = 0.7 by constrained
optimisation, and at x = 0.5 not escapable by any strategy tried
(floor §2).

Scores — one line per hypothesis per probe:

**Probe 1 (λ/L anatomy; fm_min on DENSE61, x = 0.5 chains;
closure level stated per row in the run record):**
- (i) ansatz: CONSISTENT but not separated by this probe — the
  loss occurs in the shared frame at every L ≥ 2.
- (ii) truncation: AGAINST — larger L loses fm *earlier* in λ
  and deeper: L = 2 loses rear fm in λ ∈ (0.08, 0.14]
  (fm +0.290 → −0.016, band [2.54, 3.02], depth 0.016); L = 4 and
  L = 6 lose it in λ ∈ (0.04, 0.08] (L = 6: +0.159 at λ = 0.04 →
  −0.198 at 0.08 → −0.367 at 0.11 → −0.549/−0.600 at the pin);
  the L = 1 (dipole) truncation never loses it in range
  (+0.325 at the pin, at its own poor closure 8.1×10⁻²).
- (iii) shell: CONSISTENT — every L ≥ 2 family at x = 0.5 loses
  rear-band fm before the pin; at x = 0.7 the same pattern is
  L-gated (L = 2: +0.139 at pin; L = 4: +0.0148, near-closed at
  2.36×10⁻³; L = 6: loss in λ ∈ (0.03, 0.06], A set −0.198).
- Single carrying mode: **NO** — leave-one-mode-out at the pin
  (L = 6 chain set: fm_min −0.14…−0.53 with any one mode zeroed;
  L = 8 A-lineage: −0.73…−1.10) never restores fm > 0, so no
  mode-restricted healthy closure was triggered under (b)'s
  forms.

**Probe 2 (frame dependence — the discriminator; alternative
seeds stated in the run record BEFORE reading; constructible
class = seeds A ∂t + B·merid with (A,B) ∈ {shared (F0),
pure-time (F1), flipped-tilt (F2), swapped-side (F3), unit-time
(F4)} × both sides, same projection construction):**
- (i) ansatz: PARTIAL — depth is strongly seed-dependent: every
  tilt-carrying seed degenerates in the same band (F0 −0.549 /
  −0.198; F2 −0.547 / −0.194; F3 −0.556 / −0.242; F4 −0.242 /
  −0.093 at x = 0.5 / 0.7), while the pure-time seed F1 removes
  the spacelike sign. But the registered strong form is NOT
  earned: F1's exact (JAX) margin is **+6.6×10⁻⁷ (x = 0.5) /
  +3.9×10⁻⁷ (x = 0.7)** — null within 1×10⁻⁵, not a robust
  timelike survival (the FD read, +2.5×10⁻⁵ / +1.0×10⁻³, is at
  FD truncation scale and does not decide the sign; the JAX
  read does).
- (ii) truncation: NEUTRAL — the pattern is identical at both
  pins at fixed L = 6; no L-interaction read by this probe.
- (iii) shell: SUPPORTED in weakened form — no seed in the
  constructible class is robustly timelike through the band on
  the degenerate sets, while on healthy sets (λ = 0.04 point;
  the (b) confirming set) all five frames are comfortably
  timelike (margins +4×10⁻⁴…+0.42, no band): the near-nullity
  is in the degenerate sets' geometry, not in the machinery.

**Probe 3 (L-scaling at fixed pin, x = 0.5):**
- (i) ansatz: NEUTRAL.
- (ii) truncation: EXCLUDED as the whole story — from L = 6 to
  L = 8 the band persists (width 0.78 → ~0.82) and *deepens*
  (depth 0.549 → 1.100) while the closure improves by an order
  of magnitude (dense61 1.36×10⁻³ → 1.23×10⁻⁴): the opposite of
  convergent shrinkage.
- (iii) shell: SUPPORTED (same scoping as Probe 2).

## 4. C12 accounting

What was computed: reconstructions of a *published*
configuration (Le's multipole shell) from its published
specification, now including one independently stored,
constraint-satisfying, fully audited coefficient set at
(0.7, 0.09), and solver/anatomy measurements about those
reconstructions. The configuration is pre-existing (the
paper's), not a programme construction; no formation claim is
made or audited. Category-exact language: subluminal
accelerating shell, Bobrick–Martire class — not FTL, not a
payload-transport row, not a programme shell. Phase 80's
x ≤ 0.3 confirmations and the category's other standing marks
are untouched. The x = 0.5 verdict is a methods result; the
paper's x = 0.5 margin (18×10⁻³) remains untested, not
impeached.

## 5. Failure Protocol — follow-ups (≥1, mechanism-suggested)

- **FU-P961-1 (x = 0.5 floor attack):** the constrained floor
  binds at fm = δ in the rear band at both L; attack the floor
  with (a) L = 10 constrained solves, and (b) a two-stage solve
  (constrained floor point → residual re-optimisation on the
  constraint's active-set manifold). Mechanism: the floor fell
  only 1.76→1.61×10⁻² from L = 6 to L = 8; whether it is a
  truncation-slow floor or a hard wall is decidable at L = 10.
- **FU-P961-2 (inter-node dip):** both A-lineage x = 0.7 sets
  fail finiteness at exactly one audit angle (θ ≈ 2.7202)
  between constraint nodes; a constraint grid refined *at the
  audit's own angles* (spacing ≤ 0.02 in [2.6, 2.85]) decides
  whether that basin also contains a fully auditable set (the
  from-zeros basin already provides one, so this is basin
  anatomy, not a verdict gap).
- **FU-P961-3 (harvest):** the registered Kaggle harvest
  FU-P961-2h (P96-1(a)) — any author-path set it returns is
  re-judged on this item's audit unchanged; a healthy
  author-path set at x = 0.5 would reopen that pin.

## 6. Deliverables

`results/p961_memo.md` (this memo), `results/p961_run_record.md`,
`results/p961_solve.json` (all constrained sets + finals),
`results/p961_ckpt_*.json` (per-solve histories incl. floors),
`results/p961_audit.json` (full audits: fromZeros, fromA,
polish002, L8-fromA), `results/p961_anatomy.json`,
`results/p961_probe2.json` + `p961_probe2_jax.json`,
`results/p961_fmdense_A.json`, `results/p961_regate.json`,
`results/p961_xcheck.json`, `results/p961_summary.json`,
`results/p961_check.py` → `results/p961_check.json` (**23/23
PASS**). Scripts in `work/p961_*.py`. float64 throughout
(JAX x64 on).
