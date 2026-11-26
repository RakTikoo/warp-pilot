# Phase 363 memo — THE RE-EXAMINATION: WHERE REST_print CAME FROM

**Verdict: ORIGIN IN R2.** The (0, 8/105, 0) difference was
manufactured inside the programme, by one monomial function of the
Phase 241 driver. There is no misprint in Décanini–Folacci anywhere
in the tested chain. Full record: `phase363/CHECKPOINT363.md`;
machine-readable results: `phase363/results/p363_results.json`.

## The defect

The stored printed totals at the Ellis throat (Phase 241
`DF_throat_cubics`) are wrong in exactly one cell: ξ⁰ T^r_r reads
1075/9 where faithful evaluation of printed Eq. (3.15) gives 931/9 —
**stored exceeds true by exactly 16** (bracket units). An independent
exact evaluation (Phase 361's resolved (3.15) transcription, certified
library, exact SSS jet) reproduces the other eleven cells (4 powers ×
3 components) exactly.

Per-monomial localisation (all 58 (3.15) monomials, driver functions
against the exact library): the whole +16 sits in the driver's **c3**
group, and inside it in exactly one monomial — **N40 =
R^{pqrs} R_{pqt a} R_{rs}{}^t{}_{b}**, ξ⁰ coefficient 2/315. Driver
raw value (0, +4, 0); true value (0, −8, 0); weighted difference
210·(2/315)·(4 − (−8)) = 16. The driver function (m39 in
`phase241/work/p2411_driver.py`) raises the third factor's index
from Riemann slot 0 — forming R^t{}_{rsb} — and contracts it in the
slot-2 position, where the monomial requires R_{rs}{}^t{}_{b}
(g^{tu}R_{rs u b}). Verified from scratch with explicit index
gymnastics, independent of both implementations: verbatim (0, −8, 0),
driver variant (0, +4, 0).

## R1 — the back-out: cleared, with the audit the charge asked for

The control passed by the original route (exact Fractions; REST_print
= (44/135, 4/27, 100/189); difference (0, 8/105, 0)). The algebra is
exact, and every consumed value was confronted with an independent
exact evaluation of the corresponding printed §2 form at the throat:
(2.22) → (224, 32, 224), (2.24) → (92, 20, 92), (2.25) → (52, 12, 60),
(2.28) → (20, −36, 84), (2.29) → (4, −4, 52), (2.30) → (−4, 20, 92),
(2.31) → (−1, 5, −25) — **all exactly the values the back-out used**.
The sole-origin hypotheses for the transcription-carrying
subtractions are refuted (H(6,3)(6) would have needed (4, 92, 52);
H(6,3)(8) would have needed (−1, −109/7, −25)).

Side/forced findings, in brief (full table in the checkpoint): the
H{2,0}(1), H(6,3)(1) and H(6,3)(5) subtractions are solved from the
totals themselves — conduits, forced given totals and weights,
originating nothing. The H(6,3)(7) subtraction used the derived
tensor under a direct Stage-3 calibration (re-verified here). The
one genuinely **assumed** side choice, H(6,3)(2) = derived, is
provably immaterial to REST: if the used H(6,3)(2) differs from
print by Δ, the mode-3 back-out of H(6,3)(5) shifts by exactly +Δ
(its ξ¹ weight is +1/30 against H(6,3)(5)'s −1/30), and the two
ξ⁰ subtractions carry weights −1/180 (H(6,3)(2)) and +1/180
(H(6,3)(5)), so the induced REST error is Δ/180 − Δ/180 = 0,
identically. It was also factually right: print (2.25) evaluates to
the derived value used. Given the totals, REST was forced — and the
totals' ξ⁰ T^r_r cell was the single corrupted input.

*Bookkeeping note (fence): the H(6,3)(5) work above re-derives only
that subtraction's arithmetic and throat value. Phase 241's
H(6,3)(5),(6),(8) indictment is a separate matter — those print
tensors' behaviour in the full assembly's core arbitration — and is
neither re-opened, used, nor disturbed here.*

## R3 — the target side: cleared

`tha_ellis`(R = 1) returns Tt (1033, −11242, 33180, −19320),
Tr (187, −1806, 5460, −4200), Tθ (1213, −11634, 33180, −19320) per
ξ-power; the ξ⁰ row equals stored totals minus Phase 259's stored
print residuals exactly, and the Tr polynomial is the registered
target. The differencing is sound. (Spot consistency: totals − targets
at ξ¹ = (+448, +448, +448), the recorded print ξ¹ residual; at ξ², ξ³
the totals equal the targets exactly.)

## What this does to the record (arithmetic; wording is Gate-38's)

- The Phase 259 ξ⁰ throat residual (+16) was never a property of any
  assembly: on corrected totals the print ξ⁰ throat residual is
  (−656/9, −752/9, −656/9) and the (5)/(6)/(8) substitution moves
  close T^r_r to exactly 0. All print-side ξ⁰ residuals in the 259
  record (decay profile, A throat, wider-set maxima) carry the local
  m39 error, unquantified per point except at the throat.
- The arbitrated closures (Phases 318/323, Gate-37) are **not**
  affected: REST cancels identically in every arbitrated difference
  (it enters the FULL residual and the substitution delta with
  opposite signs), so the derived assembly's exact closures, the
  A-throat evaluation, and the identification's substance stand on
  per-tensor evaluations alone. What falls is solely the attribution
  clause: the "implied print H{2,0}(3) = (80, 80/3, 112)" was the
  driver's defect read through the back-out. The correct statement is
  that print H{2,0}(3), evaluated directly (Phase 355), is (80, 16,
  112) — the derived value — and no DF misprint stands behind the
  residual.
- Named, priced, **not run**: repair m39 (raise slot 2 instead of
  slot 0) and re-run the driver's totals over the 237/259 background
  set to restate the 259 print-side ξ⁰ residuals on corrected totals.
  One function changes; the other 57 monomials are already verified
  against the exact library at the throat.

## DESK

Literature and exact computation only; no observational data; nothing
for the Publishing Desk.
