# P119-3 Memo — Separable-minimum price reference for the Xun–Ren Hamiltonian (FU-P1085-3)

**Verdict: REFERENCE COMPLETED — PRICE LINE STANDS**

C12: bookkeeping completion only. R_net is not re-read here; no claim
about the Phase 108 reopening moves. INTERNAL only.

## Control (passed before any registered row was believed)

The minimisation machinery at N = 2 reproduces P72-2's stored
E_prep^(sep) (`phase72/results/p722_results.json`) **exactly**
(abs err 0.0 at all three r, bar ≤ 1e-9):

| r | E_sep (this work) | P72-2 stored |
|---|---|---|
| 0.5 | 0.2360679774997898 | 0.2360679774997898 |
| 1.0 | 0.3284271247461903 | 0.3284271247461903 |
| 2.0 | 0.2221359549995796 | 0.2221359549995796 |

At r = 0.5 the corner and the interior critical point coincide
(cos θ = h/2k = 1); at r = 1 (θ* = 1.0471975512) and r = 2
(θ* = 1.3181160717) the symmetric interior critical point carries the
minimum — the control exercises both branches of the analytic
reduction. Multi-start optimisation agreed with the analytic value at
every control point; 110000 random product states found none lower.

Machinery grounding: the derived product expectation
⟨H⟩ = h Σzᵢ + 2k Πxᵢ + D was checked against a dense Kronecker
construction of H at (N,k) = (2,0.5), (3,1), (5,0.5): max error
3.6e-15 over 200 random product states each; dense ground eigenvalue
0 to ≤ 1.6e-15, as the printed constants require.

## The separable minimum (both certificates, every row)

Analytic reduction (run record §3): any minimiser has yᵢ = 0,
zᵢ = −√(1−xᵢ²), Πxᵢ ≤ 0; no θⱼ = π/2 and no partial-zero pattern can
be optimal; any interior optimum is symmetric with
h = 2k sin^{N−2}θ cos θ. At **every registered row that equation has
no root in (0, π/2)** (max of 2k sin^{N−2}θ cos θ < h = 1), so the
global minimum is the corner θ = 0 — the product state |1⟩^{⊗N} —
with the closed form

    E_sep = E_prep^(sep) = D − N = √(N² + 4k²) − N = 4k²/(D + N)   (h = 1).

Numerical certificate (per row): 220-start L-BFGS-B over the full
Bloch product manifold reproduced E_sep to all printed digits
(|multistart − analytic| = 0.0 at the stored precision on every row),
and 110000 random product states found none lower (random minima
0.81–3.35, far above). No row rests on a single certificate.
The independent checker (`work/p1193_checker.py`, dense-H tensor
expectations, its own sampling and optimisation) re-derived every
minimum and every ratio: ALL PASS (control, each row, final
threshold run).

## Registered rows (E_in, E_out: Phase 108 stored, `phase108/results/p1085_results.json`)

| (N,m,r) | E_sep = E_prep^(sep) | E_prep^(marg) | E_in | E_out | Π_sep | Π_marg | Π_marg/Π_sep | deciding Π (min ref) |
|---|---|---|---|---|---|---|---|---|
| (5,1,0.5) | 0.099019513593 | 0.196116135138 | 3.9223227028 | 0.2375167515 | 16.930773 | 17.339572 | 1.024145 | 16.930773 (sep) |
| (6,1,0.5) | 0.082762530298 | 0.164398987305 | 4.9319696192 | 0.2634206512 | 19.036974 | 19.346883 | 1.016279 | 19.036974 (sep) |
| (6,1,1) | 0.324555320337 | 0.632455532034 | 4.7434164903 | 0.6549291474 | 7.738199 | 8.208326 | 1.060754 | 7.738199 (sep) |
| (8,1,0.5) | 0.062257748299 | 0.124034734589 | 6.9459451370 | 0.2979009511 | 23.525279 | 23.732653 | 1.008815 | 23.525279 (sep) |
| (8,1,1) | 0.246211251235 | 0.485071250073 | 6.7909975010 | 0.7808542273 | 9.012193 | 9.318088 | 1.033942 | 9.012193 (sep) |
| (10,1,0.5) | 0.049875621121 | 0.099503719021 | 8.9553347119 | 0.3196726531 | 28.170099 | 28.325346 | 1.005511 | 28.170099 (sep) |
| (10,1,1) | 0.198039027186 | 0.392232270276 | 8.8252260812 | 0.8632550315 | 10.452606 | 10.677561 | 1.021521 | 10.452606 (sep) |
| (10,1,2) | 0.770329614269 | 1.485562705416 | 8.3562902180 | 1.7090662293 | 5.340121 | 5.758614 | 1.078368 | 5.340121 (sep) |

Π_marg recomputed from the stored E_in/E_out matches Phase 108's
stored `price_per_unit_marg` exactly (cross-check 0.00e+00 every row).

## Why the price line stands

The separable floor is lower than the marginal reference at every
row (roughly half of it — see scaling), so P72-2's deciding total
does switch reference to (R-sep). But the price is
injection-dominated: E_in exceeds E_prep by one to two orders of
magnitude, so the switch moves the total by only 0.55%–7.84%.
Deciding-total price per unit at the eight rows: **5.340121 –
28.170099**, all > 1; the largest ratio Π_marg/Π_sep is 1.078368
(at (10,1,2)), far below the registered ≥ 2 move threshold. Neither
move condition is met.

**Completed price caveat (restated):** with both of P72-2's
preparation references now evaluated for the Xun–Ren Hamiltonian,
the total counted price per unit delivered at the E_net,B < 0 rows
is 5.34–28.17 with the resource priced at the smaller (separable)
reference — still ≫ 1, still injection-dominated, still a lower
bound (classical leg ≥ 0 omitted, as inherited).

## N-scaling statement (m = 1, registered N)

E_prep^(sep) = 4k²/(D + N) exactly, vs E_prep^(marg) = 4k²/D, so

    E_prep^(sep) / E_prep^(marg) = D/(D + N) → 1/2  as N → ∞.

| r | N | E_prep^(sep) | E_prep^(marg) | sep/marg |
|---|---|---|---|---|
| 0.5 | 5 | 0.099019513593 | 0.196116135138 | 0.504902 |
| 0.5 | 6 | 0.082762530298 | 0.164398987305 | 0.503425 |
| 0.5 | 8 | 0.062257748299 | 0.124034734589 | 0.501938 |
| 0.5 | 10 | 0.049875621121 | 0.099503719021 | 0.501244 |
| 1 | 6 | 0.324555320337 | 0.632455532034 | 0.513167 |
| 1 | 8 | 0.246211251235 | 0.485071250073 | 0.507577 |
| 1 | 10 | 0.198039027186 | 0.392232270276 | 0.504902 |

**The separable floor DOES dilute like the marginal reference** —
both are Θ(1/N): E_prep^(marg) ~ 4k²/N and E_prep^(sep) ~ 2k²/N.
The separable reference is the same dilution with exactly half the
leading coefficient, not a non-diluting floor. (This is a statement
about the two preparation references only; it does not re-read
E_net,B or R_net, which Phase 108 defined on the marginal reference
and which are out of this item's scope.)

## Files

- `results/p1193_run_record.md` — definitions, derivation, reduction proof, certificates.
- `results/p1193_results.json` — control, per-row numbers, scaling, verdict basis.
- `work/p1193_eval.py` — evaluation (unit-split for this contended VM; `merge` combines).
- `work/p1193_checker.py` — independent checker; ALL PASS.
