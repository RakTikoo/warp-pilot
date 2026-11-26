# PHASE 389 — PER-PROFILE STATIONARY SCALING AT H2

**VERDICT: STATIONARY LEVEL IMPROVES AT A MIXED
CENTRE. The best stationary band level on the A2
lineage is now −1.757074×10⁻⁴ (SET-244, band
[10, 20]) at the mixed centre (μ_S, μ_N, μ_M) =
(0.9323593026620368, 1.1444417317708335,
1.1445068359375) on Phase 379's H2 centre —
+1.851724×10⁻⁵ over L_stat(H2) = −1.942246×10⁻⁴.
The level remains NEGATIVE — no energy-condition
pass, no member. GATE REFERRAL (a new harvest
candidate).**

Charged at ledger entry 984. Registration filed
before any computation:
`phase389/work/p389_registration.md` (SS0–SS7).
Frame of record: the VM (laptop NOT admitted —
below).

## 1. The act

The stationary search had only ever scaled H2's
profiles uniformly (379's μ; 381's bottoms). This
phase searched the per-profile scaling space
(S → μ_S·S, N → μ_N·N, M → 1 + μ_M·(M − 1)) of the
H2 centre's total profiles — 383's one accidental
point (1.225, 1.30, 1.30) was the only off-diagonal
point on record. Protocol: G1 grid 125 reads
(μ ∈ {0.90…1.10}³), G2 axis extension 6, G3
refinement 26, G4 Nelder-Mead polish 182 stored —
339 SET-244 reads total, cap 600 not binding,
every read C1-feasible and floor-feasible.

## 2. Controls (VM: ALL PASS, diff 0.0)

Record: `phase389/results/p389_controls.json`.

- CTL-389-V: H2 vectors from the two stored
  artefacts agree, max diff 0.0.
- CTL-389-A: (1, 1, 1) reproduces 379's confirmed
  H2 record exactly (NEC −1.9422459891767227×10⁻⁴,
  DEC −1.8982585080461558×10⁻⁴, WEC
  −1.7768467393179327×10⁻³, SEC
  −2.0943799294291577×10⁻³, ρ 8.789653555683182×10⁻⁵,
  depth −1.4402430840320638×10⁻⁴ — all diff 0.0).
- CTL-389-M: (1.225, 1.30, 1.30) reproduces 383's
  stationary verification exactly (NEC
  −1.9954038171026746×10⁻⁴, DEC
  −1.287489042939161×10⁻⁴ — diff 0.0).
- CTL-389-F: floors hold at the centre (N min
  1.150001, M min 1.124784 on FINE_R).

**Frame admission: LAPTOP NOT ADMITTED**
(eleventh occurrence). Laptop CTL-389-A: NEC diff
6.386751250093265×10⁻⁷, WEC 6.315941396222054×10⁻⁶
— digit-for-digit 383's CTL-383-H2S diffs on the
same centre; DEC/ρ/depth at roundoff
(≤ 1.1×10⁻¹⁹); CTL-389-M NEC diff 5.257×10⁻⁸.
Record: `p389_controls_laptop.json`. All deciding
reads are VM reads.

## 3. The confirmed mixed centre

Confirmation (`p389_confirmation.json`): full
re-reads reproduce the stored screen minima at
diff 0.0 for the best point and the centre.

| quantity | H2 centre | mixed centre |
|---|---|---|
| joint (SET-244) | −1.942246×10⁻⁴ | **−1.757074×10⁻⁴** |
| NEC | −1.942246×10⁻⁴ @ 16.220 | −1.757074×10⁻⁴ @ 12.561 |
| DEC | −1.898259×10⁻⁴ @ 19.634 | −1.567069×10⁻⁴ @ 19.634 |
| ρ_min | +8.789654×10⁻⁵ | +8.936713×10⁻⁵ |
| depth (polished) | −1.440243×10⁻⁴ | −9.660225×10⁻⁵ |
| worst-null @ NEC argmin | −1.943288×10⁻⁴ | −1.770370×10⁻⁴ |

Margin over the bar +1.851724×10⁻⁵ (9.5%); the
improvement survives at pointwise grade
(worst-null beats L_H2 by +1.721×10⁻⁵). NEC-bound;
the NEC argmin moved 16.220 → 12.561; the DEC
argmin unmoved (19.634). Depth far above the C2
bar (−0.0034).

## 4. Anatomy (SS6; `p389_anatomy.json`)

- GRADIENT AT THE CENTRE (fit over the
  non-saturated cube): (−1.096, +1.115, +0.821)
  ×10⁻⁴ per unit μ — S wants to shrink, N and M
  to grow. The centre was never stationary in
  this space. The μ_M gain is cooperative (the
  μ_M axis alone dips both ways; the S–N cross
  term is the size of the diagonal terms).
- BOWL, NOT RIDGE: fit Hessian eigenvalues all
  negative (−3.33×10⁻³, −8.38×10⁻⁴, −6.1×10⁻⁵) —
  concave surface, centre on the flank, peak at
  the polished point (μ_N ≈ μ_M ≈ 1.1445, agree
  to 6.5×10⁻⁵). The second polish run (120 evals
  from the point) found no improving step.
- μ_M NEAR-IDENTITY (observation): J(1, 1, μ) =
  J(μ, μ, μ) to ≤ 3.4×10⁻¹⁹ at μ ∈ {0.95, 1.05,
  1.10}, NEC/DEC minima and argmin radii agreeing
  — the binding margins there are functions of
  μ_M alone at roundoff (M-carried sites). This
  explains 381's uniform readings.
- DEC-SATURATED CORNER: 9 grid points (μ_N, μ_M
  ≤ 0.95, μ_S ≥ 1.0) are DEC-pinned at ~ −1
  (387's past branch; DEC argmin r = 17.683) —
  C1-feasible but level-meaningless; excluded
  from the fit; the optimum goes the other way.
- DIAGONAL: falls both ways from μ = 1 (381's
  uniform verdict reproduced in-grid) — the one
  direction where the three gradients cancel.
- BAND EDGES: the scaling's edge values are
  inherited from H2 (379 SS6); no end-clamp
  re-read was registered. FLAGGED FOR THE GATE:
  at H2 the clamp cost 1.45×10⁻⁵ (Gate-41 rider),
  the same order as this gain — the margin's
  survival under clamping at the new centre is
  unmeasured here.

## 5. Classification consequence

381's fixed point was the ITERATION's fixed
point, not a local optimum of the stationary
level surface. The family's best stationary band
level restates to −1.757074×10⁻⁴ at the mixed
centre. Named follow-ups (not run): the
spline-correction harvest re-centred at the
mixed centre; a dwelling pose around it;
scaling iterated with the harvest.

## 6. Incidents

- The first G4 polish run was killed by a
  runtime restart after 63 stored reads; every
  read is flushed per evaluation (no loss), and
  the relaunched polish completed at nfev = 120,
  returning exactly its start point.
- The laptop mirror initially lacked the
  root-level modules (verify_metric, shell); two
  admission attempts aborted on import before the
  deciding run.
- A cos(φ)/cos(θ) transcription slip in the
  first draft of the polish objective was caught
  against p379_lib before any run (controls'
  depth at diff 0.0 confirms the fixed form).

## 7. Fences and accounting

Band-posed [10, 20] SET-244 levels; 356's
full-extent caveats travel (lineage full-extent
≈ −1.44×10⁻³ over [10, 60]); no EC pass claimed;
no sustainment, front or transport content. The
verdicts of 379/381/383 stand as stated.

Goal 1 (FTL drive): the stationary pressure
level improves again (−1.942246×10⁻⁴ →
−1.757074×10⁻⁴, band) — the wall moved, it did
not break. Goal 2 (wormhole): untouched. Goal 3
(subluminal record): untouched.

DESK: NO DATA CONTACT.

Artefacts: `phase389/work/p389_registration.md`,
`p389_lib.py`, `p389_controls.py`,
`p389_search.py`, `p389_confirm.py`,
`p389_anatomy.py`; `phase389/results/
p389_controls.json`, `p389_controls_laptop.json`,
`p389_screens.jsonl` (+ `parts/`),
`p389_search_summary.json`,
`p389_confirmation.json`, `p389_anatomy.json`,
`p389_memo.md`, search/polish logs.
