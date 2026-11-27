# Warp Pilot v1.49.0 — Gate-59: Phase 431's persistent-mating claim set survives independent re-judgement — persistent spinor matings exist for both standing supply targets (the ladder arm mates T_req at 1.3730×10⁻¹⁶ for 0.48× the drifting fit's price; the single-energy arm mates the corrected target T_corr at 9.9696×10⁻¹⁵, stationary by construction; the ladder mates T_corr at 1.2311×10⁻¹⁵ for 0.59×) — and the one negative is structural: no single-energy supply can express T_req (floor ≈ 1.27×10⁻³, isotropic spatial-diagonal shortfall, full-rank Jacobian, per-site relaxation floors at the same residuals) — Phase 428's supply leg is satisfiable in principle; its geometry leg (GAP-3) still gates every sustainment claim

This release publishes Phase 431's claim set as
re-judged by Gate-59 (ledger entry 1151). Phase
430 had shown that both standing supply fits —
Phase 410's Fit A for the 405 winner's required
stress T_req, and Phase 420's composite C-A for
the SEC-corrected target T_corr — drift: their
cancellation is fine (cross-term weights ~4.1×10²
× the target norm) and their stored floats cross
Phase 428's persistence bar (R ≤ 1×10⁻⁹) at
t* ≈ 2.42×10⁻¹⁷ s. Phase 431 answered with
DEGENERATE MATINGS — supplies whose mode energies
are exactly degenerate (one shell: the supplied
tensor is constant in time by construction) or
exactly commensurate (an integer ladder: the
supplied tensor is exactly periodic). Its four
verdicts: the ladder arm mates T_req; the
single-energy arm mates T_corr (stationary) and
the ladder mates it too (periodic); and the
single-energy arm does NOT mate T_req — its best
fits stall at maxR ≈ 1.27×10⁻³ with the residual
carried almost isotropically by the spatial
diagonals, a candidate expressiveness wall of the
single-shell family.

Gate-59 re-judged the set on machinery
independent of the phase's evaluator — the gate's
own implementation of the spinor stress tensor
from the field bilinear directly (the phase's
driver works through a pairwise pair-kernel; the
gate's pair kernel was derived in its own file
and validated against its field path at
3.2×10⁻¹⁶), with every audited object
sha256-verified against its stored record before
auditing, all deciding reads on the VM (frame of
record), and the laptop admitted as corroboration
only (the admission read agreeing to 6.8×10⁻¹⁹;
the pool's priority run undisturbed). The
controls were re-derived first: Fit A and C-A
reproduce digit-for-digit, prices exact; the B-2
instrument's self-checks reproduce at roundoff.
The phase's coordinator checker re-ran at the
gate: ALL PASS, output identical to the stored
record. The three ADMITS confirm at t = 0 on both
of the gate's evaluation paths (pair values
digit-for-digit the stored values) and under the
gate's own B-2 reads — the single-energy T_corr
mating is stationary over the full 3.860 yr
window (registered-energy deviation exactly 0.0;
window spots confirmed in both evaluable forms),
and the ladder matings are periodic with worst
instants 0.20791 (T_req) and 0.65688 (T_corr)
reproduced digit-for-digit and ladder returns
≤ ~10⁻¹³ at 2¹⁰ cycles, seven orders inside the
per-cycle bar. Prices recompute exactly:
0.4771× Fit A, 0.8251× and 0.5887× C-A — persistent
supplies are CHEAPER than the drifting fits they
replace. For the negative, the gate went beyond
re-running the search: its own search (a second
implementation) re-converges to the same basin
(polished floor 1.2716×10⁻³, a hair below the
phase's best) with 19 fresh random starts across
N = 6–16 finding nothing lower; its constrained
Jacobian at the mating reproduces σ_min =
5.41×10⁻⁴ at full rank 30/30 — a genuine shallow
strict local minimum; and its per-site dictionary
relaxation — amplitudes freed per site over 192
modes, a feasible set strictly containing the
joint problem's per-site behaviour — floors at
the joint fit's per-site residuals at every site
(peak site 1.285×10⁻³ vs 1.2754×10⁻³), with the
same anatomy and an energy scan minimised at the
mating's own shell. The gate accordingly rules
the negative STRUCTURAL at its registered scope
(rider G59-R3): a single-energy supply cannot
express T_req's principal pressures. Three
corrections to the phase's printed record touch
no verdict: the verbatim representation bound for
the stationary mating is 0.224 s, not 0.119 s
(the printed value is an artefact of the
per-mode-phase evaluation form — the same form
the record itself superseded for its window
spots; the faithful forms agree to 0.03%); the
comparison to the drifting fits is ~16 orders of
magnitude, not 24; and the anatomy's off-diagonal
bound is ≤ 1.11×10⁻⁶, not ≤ 3.1×10⁻⁷. The fence
stands on the whole set: Phase 428's geometry leg
(GAP-3) still gates every sustainment claim,
T_corr is a construction rather than a geometry,
and the ACTIVE SUPPLY — the road named in case no
persistent mating existed — has its premise
falsified for both standing targets.

The quotable claim set (Gate-59; the only
quotable form of the Phase 431 claim set):

> **G59-A (Arm B / T_req ADMITS, periodic).** *The
> commensurate-ladder arm mates T_req at the bar:
> a six-mode mating whose energies sit exactly on
> the integer ladder (1,1,2,2,3,3) of
> E₀ = 1.019134 fits all three sites at
> maxR = 1.3730×10⁻¹⁶ (the 428 F1 bar is
> 1×10⁻⁹), at price |a|² = 0.013963 = 0.4771× the
> unconstrained Fit A. The mating is persistent in
> the PERIODIC (Form P) form: common period
> T_c = 6.165222 units (2.06×10⁻⁸ s), 5.923×10¹⁵
> cycles in the 3.860 yr window, ladder returns
> ≤ ~10⁻¹³ at 2¹⁰ cycles against the 1×10⁻⁶
> per-cycle bar (rider G59-R2).*
>
> **G59-B (Arm A / T_corr ADMITS, stationary).**
> *The single-energy arm mates T_corr: two
> families of six modes on one shell
> (E = 2.189896, spectrum scatter 4.44×10⁻¹⁶) fit
> all three sites at maxR = 9.9696×10⁻¹⁵, at
> total price |a|² = 0.024071 = 0.8251× the
> composite C-A. The mating is persistent in the
> STATIONARY form: the supplied tensor is
> constant by construction, confirmed at the
> registered energy over the full window
> (deviation exactly 0.0 on the grid read; window
> spots confirmed in both evaluable forms). Its
> verbatim float representation bound is
> t* = 6.72×10⁷ units = 0.224 s (rider G59-R4).*
>
> **G59-C (Arm B / T_corr ADMITS, periodic).**
> *The commensurate-ladder arm mates T_corr: two
> families of six modes on the integer ladder
> (1,1,2,2,3,3) of E₀ = 1.178657 fit all three
> sites at maxR = 1.2311×10⁻¹⁵, at price
> |a|² = 0.017173 = 0.5887× C-A. The mating is
> persistent in the PERIODIC (Form P) form:
> common period T_c = 5.330801 units
> (1.78×10⁻⁸ s), 6.850×10¹⁵ cycles in the window,
> ladder returns ≤ ~10⁻¹³ at 2¹⁰ cycles (rider
> G59-R2).*
>
> **G59-D (Arm A / T_req DOES NOT ADMIT — the
> negative, rider G59-R3 verbatim).** *Arm A /
> T_req DOES NOT ADMIT — structural at the
> registered scope: in the record's mating
> machinery at Phase 410's sites, no single-energy
> (single-shell, m = 1) supply mates T_req at the
> 1×10⁻⁹ bar. The best fits stall at
> maxR ≈ 1.27×10⁻³ with the residual carried
> almost isotropically by the spatial diagonals
> (peak site 7.40/7.36/7.34×10⁻⁴; T00
> ≤ 4.12×10⁻⁶; off-diagonals ≤ 1.11×10⁻⁶); the
> constrained Jacobian at the optimum is
> full-rank (σ_min 5.41×10⁻⁴); and a per-site
> relaxation with free amplitudes over a dense
> direction dictionary floors at the same
> per-site residuals (peak site 1.285×10⁻³) — a
> single-energy supply cannot express T_req's
> principal pressures. Scope: joint searches to
> N = 12 (16 probed) by two independent
> implementations; relaxation dictionary 96
> directions per site; no analytic impossibility
> proof is claimed, and an exhibited single-energy
> mating at the bar reopens the arm.*

Riders G59-R1…R5 (GATE59.md §7) bind every
quotation of this set. DOI: [version DOI minted
at release — fill in at upload].
