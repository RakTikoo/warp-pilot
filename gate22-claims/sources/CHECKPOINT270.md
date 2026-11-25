# CHECKPOINT 270 — THE c_trim UNCERTAINTY ESTIMATE:
# THE GAP BITES — DEFENSIBLE REFITS MOVE c_trim BY
# −22% / +8.4%, AN ORDER OF MAGNITUDE PAST GATE-27'S
# ±~2% STABILITY BAND

Phase 270, 2026-11-24. The priced gap in Gate-27's G27-A
fence (i), executed under `phase270/work/
p270_registration.md` (controls, legs, grids,
interpretation and combination rules, verdict forms —
all fixed before computation). Item memo:
`results/p2701_memo.md`; driver `work/p270_run.py`,
results `results/p270_results.json`; independent checker
`work/p270_check.py` → `results/p270_verify.json`,
**PASS 39/39** (full independent recomputation of all 60
refits at max diff 0.0; zero discrepancies). Stored-row
arithmetic only; no march re-run, no engine imported;
source files md5-identical before/after. Frame of
record: Phase 166 pin, Gate-19-corrected tensor, venv
python, float64.

## FTL VERDICT (leading): NO

No grouped joint pass anywhere; Frontier A unchanged;
drive step 1 remains unachieved. The phase's yield is on
the wormhole goal's record hygiene: the one unpriced
parameter dependence of the programme's lead sustainment
claim (G27-A) is now priced — and it is large.

## VERDICT (form 2): THE GAP BITES

Gate-27 priced the certified bracket (0.675, 0.68125] as
stable to δc_trim ∈ [−0.11264, +0.10352] (≈ ±2% of
c_trim = +5.253378225339471) and left the fit's own
parameter uncertainty unpriced. Measured here, the total
defensible uncertainty is

  **δc_trim ∈ [−1.158404, +0.440454]**
  (c_trim ∈ [4.094974, 5.693832]),

exiting the band on both sides (lo by 1.045764, hi by
0.336934). Only 5 of 60 defensible refits land inside the
band, all in the maximal-window corner: the stored
coefficient is the product of the single most aggressive
window choice in the defensible set.

**Legs.** (1) Residual SE: SE(q₂) = 0.224899 (3.71%),
SE(c_trim) = 0.194872 — but the residuals are SYSTEMATIC
under the pre-registered rule (4 sign runs, Durbin–
Watson 0.348; a smooth deterministic arch, not noise:
the trajectory is a bit-exact deterministic march
output), so the SE is a misfit-scale diagnostic only and
stays out of the total; the verdict does not hinge on
the exclusion (the ±1 SE band alone also exits the
stability band on both sides). (2) Variation spread —
THE exiting leg: 60 defensible refits (15 lattice
windows in the holding interval × full/half subsetting
× OLS/Huber) give c_trim ∈ [4.116961, 5.654858], median
4.799039. The window END drives it (end 0.475 → 0.375
moves the baseline −18.6%; even a one-instant trim to
0.45 gives −5.53%); dropping the posed t = 0 point
drives the hi side (+7.64% at start 0.05); subsetting
and weighting are minor. Diagnostics outside the
distribution, priced: cubic c₂ = −0.922518 (outside the
registered fit class); forced-t² c₂ implies c_trim
4.145130 (a different parameter). (3) Divisor: Tier-1
summaries (mean / median / trapezoid) give δ ∈
[−0.028056, +0.036207] — inside the band alone; the
constituents are FD-exact (≤1.85×10⁻¹⁰) and the
finite-amplitude delivery agrees to 3.78×10⁻¹² relative,
so the divisor carries no numerical spread; its
provenance is era-bound (the slope drifts −0.431536 per
unit t; bracket-era reads ≈ 1.0 would imply c_trim
≈ 6.03 — a different design era, priced as Tier 3, not
counted).

**Bracket consequences (linearised, Gate-27's slope,
locality caveat on the memo's face):** the crossing
ranges over **[0.644750, 0.690957]** under the full
defensible uncertainty. The lead change over the WOUND
bracket (0.55625, 0.5625] **survives the full range**
(min crossing clears it by 0.082250). The ordering past
the CLAMPED bracket (0.65625, 0.6625] **does not
survive** — the crossing range straddles it. Phase 266's
certificate is untouched: it certifies the pose as posed
with the stored coefficient; what changes is only that
G27-A's fence (i) must carry the fit uncertainty as a
live caveat (rewording stated in the memo §5) instead of
an unpriced gap.

**Named successor:** a Gate registration rewording
G27-A's fence (i) per memo §5 (the parent's step, as
Gate-27's publication consequence was). No other
successor is registered by this phase.

## Fences

Stored-row arithmetic only; no new bracket computed or
certified (the robust interval is Gate-27's linearised
response applied to the measured uncertainty, locality
caveat carried). The uncertainty priced is the
counterfactual spread of Phase 248's FIXED procedure
under its own defensible variations — the coefficient
was fixed in advance and never tuned against any
bracket (Gate-26 §4(3b)); this is a robustness price,
not a tuning finding. Defensible set and exclusions as
registered, reasons on the memo's face. Jet scope;
datum ≠ construction; programme-level sustainment
wording remains gated by p1592 regardless. No ledger
append (parent's step); no launches; no contact.
