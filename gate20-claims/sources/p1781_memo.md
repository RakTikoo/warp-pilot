# P178-1 (FU-P1763-1) — THE THIRD GATE ATTEMPT, witness-first

**DESIGNATED SPECULATIVE** — this label applies to the whole
item, every number in it, and the verdict line below. It is
carried on every form, never softened.

## Verdict

**GATE PASSES (SPECULATIVE)** — a single enriched field is
exhibited whose EXACT coupled reads satisfy every witness
clause simultaneously, and with that witness exhibited the
gate's clauses (a), (b), (c), unmodified from CHECKPOINT163
§P163-1, all hold with the numbers below. Milestone-adjacent
for the P123-3 line, flagged plainly: this goes to a Gate.
P123-3's milestone stands exactly as scoped regardless; a
pass here removes its "awaits the full pose" cap at
instrument scope, nothing more.

## Controls (all exact)

The enriched E-a instrument, reused from P176-3's saved state
(Jacobian not rebuilt; the state copy and the standalone
`p1763_J_coupled_Ea.npz` agree with max diff 0.0), reproduces
P176-3's deciding reads bit-for-bit in value:

- coupled LS floor **0.6197514399668285** (registered
  0.6197514399668285, diff 0.0);
- floor witness exact coupled closure **0.6196571998307678**
  (diff 0.0), Δq = (+0.019929411948893305,
  +0.020785147728896503), Type-I [False, False], count 52;
- reads at d = 0 reproduce the stored q
  [1.0032717740717199, 1.1029635664194024] exactly and
  count 52.

## Gradients

Central FD in P171-1 Stage-B form, **h = 1×10⁻³**, of q41,
q44 and D_r (all 56 subset points) wrt the 72 enriched
coefficients around d = 0, via `p1711_common.reads` on
`make_gf_enriched` fields; checkpointed per batch of 6 to
`work/p1781_grad_partial.npz` (1728.6 s total).
‖g41‖₂ = 63.657, ‖g44‖₂ = 178.763 (dominated by the
b-field block, coefficients 54–71); ‖GD‖_F = 0.004103.
One structural fact worth naming: the smallest |D_r| at
d = 0 is 1.0432897799616071×10⁻⁸, at subset point **44
itself** — site 44 sits essentially on the Type-I boundary,
so the count-preserving constraint is binding there by
construction (its linearised margin at the witness is
1.04×10⁻⁸); the exact count nevertheless holds (below).

## The witness (a-priori selection rule)

Selection rule, as registered: the minimum-closure field
subject to the linearised q_r and count-preserving
constraints, priced against the COUPLED Jacobian. Solved as:
minimise the linearised coupled closure ‖res0 + J·d‖ (J =
saved coupled E-a Jacobian) subject to linearised
|g41·d| ≤ 5×10⁻⁴, |g44·d| ≤ 5×10⁻⁴ (aimed at the stored
values, Δq ≈ 0), linearised count-preserving
sign(D0 + GD·d) = sign(D0) at all 56 points. Method: scipy
SLSQP with analytic Jacobians, multi-start (LS field /
equality-constrained LS field / zero). Targeted closure
margin: the constrained minimum itself — it lands at
0.622707 linearised, below the 0.625 margin target and the
0.63 cap. The converged solve (SLSQP success) is the
equality-LS start: linearised closure **0.6227068127601647**,
linearised Δq = (2.4×10⁻¹⁶, 9.3×10⁻¹⁸), count-preserving
with min margin 1.04×10⁻⁸. (The LS start reached a
marginally lower linearised closure, 0.622555, but SLSQP
stopped on a linesearch condition with linearised Δq44 =
5.00002×10⁻⁴ — a hair outside tolerance — so it was not
selected; the zero start did not converge to feasibility.
A min-max-|Δq| cross-check returns t ≈ 0 at caps 0.63 and
0.625 and t = 0.0146 at cap 0.62: the q/count-constrained
set does not reach 0.62, consistent with the constrained
minimum closure 0.6227.)

**Exact verification (deciding), iteration 1 of 1** — the
linearised optimum's exact reads satisfy every clause, so
no correction iteration was needed:

- exact coupled closure (direct evaluation,
  `pose_E_coupledIa` + `residual_frame`):
  **0.6232117059867903 ≤ 0.63** ✓ (margin 0.006788);
- exact q (gate path `reads()`): q41 = 1.0032667816897762,
  q44 = 1.1028314523056981; Δq = (**−4.992×10⁻⁶,
  −1.321×10⁻⁴**), both |Δq| ≤ 5×10⁻⁴ ✓;
- Type-I at sites 41/44: **[False, False]** ✓;
- subset count: **52** exact ✓.

## The gate

- **(a) FIXED-PATH part — PASS.** Re-run in
  `p1631_solver.py`'s gate-stage form (`That_counter_fixed`
  / `rich2` replicated in this item's own script; the solver
  module's pipeline was not executed): c₂ reproduced =
  0.0009028647947471692 (site 41) and −0.0011544294511897568
  (site 44), reldiff **0.0** at both sites; survival
  fractions reproduced = **0.013652955217293665** (41) /
  **0.14058890317097553** (44), reldiff **0.0** (tolerance
  1×10⁻⁶).
- **(b) FULL-POSE DIRECT READ — PASS.** The witness's exact
  reads above ARE the full-pose direct read at
  λ_val = 0.019992372183091776: the diagonal response is the
  witness field, the profile sector at coeff0 and the
  dragging sector as in the anatomy's pose (drag = None in
  this instrument; drift 0.0 on the record since P163-1),
  relief NOT active. Type-I [False, False] exact, count 52
  exact, q_r within 5×10⁻⁴ of stored at both sites, and the
  coupled closure 0.623212 ≤ 0.63 read in the same pose.
- **(c) RESPONSE SIZES — exhibited.** ‖d‖₂ =
  **0.18087836878121485**; max |coeff| = **0.14320434982453112**;
  max field value at the subset points =
  **0.0013184603821767068**, far inside the solver's
  trust-region cap 0.25; fraction of ‖d‖² below
  σ_cut = 23.4914 (at η_J = 1.00168500225718):
  **0.9971746120746057**.

## Verification

Independent checker `results/p1781_checker.py`:
**15/15 PASS** (`results/p1781_checker_output.txt`) — it
re-derives the coupled floor from the saved Jacobian,
re-runs the d = 0 control, re-checks the witness's
linearised stats from the saved gradients, re-evaluates the
witness's exact coupled closure and exact gate reads itself,
replicates gate (a) independently (reldiffs 0.0), recomputes
the clause-(c) sizes, and checks verdict consistency.

## Files

- `results/p1781_results.json` — controls, gradients,
  linearised optimum, witness, gate clauses, verdict.
- `results/p1781_run_record.md` — stages, timings,
  iteration log.
- `results/p1781_checker.py`,
  `results/p1781_checker_output.txt` — 15/15 PASS.
- `work/p1781_stage1_controls.py`, `work/p1781_stage2_grad.py`,
  `work/p1781_stage3_opt.py`, `work/p1781_stage5_gate.py`,
  `work/p1781_assemble.py`; state: `work/p1781_controls.npz`,
  `work/p1781_grad_partial.npz`, `work/p1781_grad.npz`,
  `work/p1781_iter_partial.npz`, `work/p1781_state.npz`
  (witness field d_final), plus stage logs and JSONs.

Execution form: local-short staged computation with
checkpointing after every batch (the FD gradient sweep was
the long stage, 1728.6 s checkpointed, Phase 171/176
precedent); float64 throughout; the phase176 coupled
Jacobian was reused, not rebuilt. INTERNAL only; nothing
uploaded, nobody contacted, nothing appended to the ledger.
SPECULATIVE.
