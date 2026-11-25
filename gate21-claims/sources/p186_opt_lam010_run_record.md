# P186 Stage 4 — registered selection + exact reads at λ = 0.10 — RUN RECORD (SPECULATIVE)

SPECULATIVE throughout. Final Stage-4 step at λ_mid = 0.10 (frontier
pricing after the λ = 0.1452 read failed at d = 0 level on clauses
(iii)/(iv), onset bracket (0.10, 0.12]).

## Method

`phase186/work/p186_opt_lam010.py` mirrors
`phase178/work/p1781_stage3_opt.py` exactly, with the two registered
substitutions: spin threaded at LAM = 0.10 everywhere
(`pose_E_coupledIa(gf, C.coeff0, 0.10)`, `P186.reads_lam(gf, 0.10)`),
and Δq taken against the same-λ reference
QREF = q(0; 0.10) = [0.9923385740704013, 0.9223100532072909],
recomputed via `reads_lam` and asserted equal (≤1e-12) to the Stage-1
values — actual max diff 0.0; D0 from the gradient file asserted equal
(≤1e-12) to `reads_lam` D_r at d = 0 — actual max diff 0.0.
Inputs: `p186_J_coupled_lam010.npz` (J, res0, scales; LS floor
0.6200617243030124 ≤ 0.63), `p186_grad_lam010.npz` (g41, g44, GD, D0).
CAP = 0.63, TOL = 5e-4, σ_cut = 23.491427444171965. Runtime 62.8 s,
project venv, cwd ~/workspace/warp-pilot.

## Linearised selection

All three SLSQP multi-starts terminated with "Positive directional
derivative for linesearch" (success=False) at essentially the same
point (lin_closure ≈ 0.622981):

| start | lin_closure | lin Δq41 | lin Δq44 | count_ok |
|---|---|---|---|---|
| from_ls | 0.6229815888296493 | −4.999986026002634e-4 | +5.000039214448932e-4 | True |
| from_eqLS | 0.6229816306285766 | −4.99587163859053e-4 | +5.011732771109259e-4 | True |
| from_zero | 0.6229814438458013 | −4.964936878768976e-4 | +5.098284246062831e-4 | True |

Under the original's feasibility filter (|lin Δq| ≤ TOL+1e-9 and
lin_count_ok), the feasible set is EMPTY — every candidate's lin Δq44
exceeds 5e-4 (by 3.9e-9, 1.17e-6, 9.83e-6 respectively) — so
linearised_best = None and, per the original's fallback, the exact-read
loop started from the min_t candidate at cap 0.63.

min-max-|Δq| cross-check (all success=False, same linesearch message):
cap 0.63 → t = 7.70e-16 (lin_closure 0.6300000000004269);
cap 0.625 → t = 4.16e-16 (lin_closure 0.6249999999999968);
cap 0.62 → t = 0.0032640051433232144 (lin_closure 0.6244431116106041,
i.e. the 0.62 cap is not reachable: best lin_closure at that solve is
0.62444 > 0.62).

## Exact-read correction loop (≤13 iterations, as registered)

| iter | closure | Δq41 | Δq44 | Type-I 41/44 | count | all_ok |
|---|---|---|---|---|---|---|
| 0 | 0.6302835602173782 | +1.314824882421295e-4 | −9.162958377479935e-4 | F/F | 52 | False (closure, Δq) |
| 1 | 0.6264191966232877 | −3.8851759893565596e-4 | −1.8352163796261367e-3 | F/F | 52 | False (Δq) |
| 2 | 0.6233418793559693 | +2.8923707575456703e-5 | +2.3035807094939909e-4 | F/F | 52 | **True** |

Correction step norms: iter 0→1 |δ| = 5.795610942227238;
iter 1→2 |δ| = 0.31150971371123504. Loop stopped at iteration 2 with
all clauses holding on exact reads.

## Verdict for this step: WITNESS FOUND at λ = 0.10

Witness (d_final) exact reads: closure 0.6233418793559693 ≤ 0.63 (i);
|Δq41| = 2.89e-5, |Δq44| = 2.30e-4 ≤ 5e-4 (ii); Type-I [False, False]
(iii); count 52 (iv). Sizes (v): ‖d‖₂ = 4.407427402148757,
max |coeff| = 3.547358374106746, max field value =
0.042537246320521915 ≤ 0.25 trust cap, fraction of ‖d‖² below σ_cut =
0.9997605765139753.

Note (for the record, not a clause): the witness's linearised-around-
d=0 diagnostics read lin_closure 0.6252383846938673, lin Δq44
0.002751512217372438, lin_count_ok False (min margin −8.77e-8) — the
linearisation at d = 0 does not track this field; the registered
deciding reads are the exact ones above, which all hold.

## Outputs

- Script: `phase186/work/p186_opt_lam010.py`
- State: `phase186/work/p186_opt_lam010_state.npz` (d_final, d_lin_best
  [= min_t@0.63 fallback, since linearised_best is None], d_mint_063,
  d_ls)
- Iteration log: `phase186/work/p186_opt_lam010_iters.json`
- Results: `phase186/results/p186_opt_lam010.json`
