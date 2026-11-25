# P178-1 — Run record (SPECULATIVE)

Item: P178-1 (FU-P1763-1), THE THIRD GATE ATTEMPT,
witness-first, DESIGNATED SPECULATIVE.
Frame of record: ~/workspace/warp-pilot/venv/bin/python
(numpy 2.5.5 / scipy 1.18.1) + Phase 166 pin; float64.
Registration: phase178/CHECKPOINT178.md §P178-1, executing
phase176/results/p1763_memo.md's successor registration.
Coupled E-a Jacobian REUSED from phase176/work/
p1763_state.npz + p1763_J_coupled_Ea.npz (not rebuilt).

## Stages

1. CONTROLS — work/p1781_stage1_controls.py (18.5 s).
   PASS, all values exact: coupled LS floor
   0.6197514399668285 (diff 0.0); floor witness exact
   coupled closure 0.6196571998307678 (diff 0.0), Δq
   +0.019929411948893305 / +0.020785147728896503, Type-I
   [F,F], count 52; d=0 reads reproduce stored q
   [1.0032717740717199, 1.1029635664194024] and count 52;
   state-vs-file Jacobian max diff 0.0. D0 min |D_r| =
   1.0432897799616071e-08 (later identified: point 44).

2. GRADIENTS — work/p1781_stage2_grad.py (1728.6 s,
   background, checkpointed per batch of 6 coefficients
   to work/p1781_grad_partial.npz; final
   work/p1781_grad.npz). Central FD, H = 1e-3 (P171-1
   Stage-B form), q41/q44/D_r(56) wrt 72 enriched
   coefficients around d=0 via p1711_common.reads on
   make_gf_enriched fields. Checkpoint log (cumulative
   gradient norms): 6 coeffs [218 s] ‖g41‖ 0.069;
   12 [381 s] 0.69/6.52; 18 [548 s] 0.92/8.84; 24 [700 s];
   30 [911 s] 0.95/8.84; 36 [1019 s] 1.39/12.5; 42
   [1128 s] 1.70/17.3; 48 [1258 s]; 54 [1388 s] 1.74/17.3;
   60 [1504 s] 51.1/159.1 (b-field block enters);
   66 [1611 s] 63.7/178.8; 72 [1729 s] done.
   Final: ‖g41‖₂ = 63.65699006371403, ‖g44‖₂ =
   178.76254728000893, ‖GD‖_F = 0.0041033995332816955,
   D0 argmin = 44.

3. CONSTRAINED OPTIMUM — work/p1781_stage3_opt.py
   (SLSQP portion seconds; whole stage 55 s incl. exact
   reads). Minimise linearised coupled closure subject to
   |g41·d| ≤ 5e-4, |g44·d| ≤ 5e-4, linearised
   count-preserving sign constraints (56). Multi-start:
   - from_ls: SLSQP success=False ("Positive directional
     derivative for linesearch"), lin closure
     0.622555262651198, lin Δq (−4.9986e-4, +5.00002e-4)
     — Δq44 a hair outside tol; NOT selected.
   - from_eqLS: SLSQP success=True, lin closure
     0.6227068127601647, lin Δq (2.4e-16, 9.3e-18),
     count-preserving (min margin 1.0402933644018856e-08)
     — SELECTED (the a-priori rule's converged optimum;
     below the targeted 0.625 margin).
   - from_zero: success=False, lin closure 0.754 — not
     feasible-converged.
   Min-max-|Δq| cross-check (SLSQP success=False on all
   three, corroborating only): t ≈ −1.4e-15 at cap 0.63,
   t ≈ −1.4e-16 at cap 0.625, t = 0.014602945472997375
   at cap 0.62 (cap 0.62 unreachable under the q/count
   constraints, consistent with constrained min closure
   0.6227).

4. EXACT VERIFICATION — same script, iteration log:
   - iteration 0 (the selected optimum, exact-read):
     closure 0.6232117059867903, q41 1.0032667816897762,
     q44 1.1028314523056981, Δq (−4.992381943624835e-06,
     −0.00013211411370428472), Type-I [False, False],
     count 52 — ALL clauses hold. Iteration count: 1
     (no correction iteration needed). Witness saved as
     d_final in work/p1781_state.npz.

5. GATE — work/p1781_stage5_gate.py (~5 s). Clause (a)
   replicated in p1631_solver.py gate-stage form
   (That_counter_fixed / rich2; solver pipeline not
   executed): c2 reldiff 0.0 / 0.0, survival reldiff
   0.0 / 0.0 vs stored 0.013652955217293665 /
   0.14058890317097553 — PASS. Clause (c) sizes:
   ‖d‖₂ 0.18087836878121485, max |coeff|
   0.14320434982453112, max field value
   0.0013184603821767068 (cap 0.25), fraction of ‖d‖²
   below σ_cut = 23.491427444171965: 0.9971746120746057.

6. ASSEMBLY + CHECKER — work/p1781_assemble.py writes
   results/p1781_results.json; results/p1781_checker.py
   (independent, imports no stage script) re-derives all
   deciding numbers from saved state: **15/15 PASS**
   (results/p1781_checker_output.txt, 38 s).

## Verdict

GATE PASSES (SPECULATIVE) — see p1781_memo.md.

INTERNAL only; nothing uploaded; nobody contacted; no
Kaggle launch; nothing appended to the ledger; no other
phase's files edited. SPECULATIVE.
