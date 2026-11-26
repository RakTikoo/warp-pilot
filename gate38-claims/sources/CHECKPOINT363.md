# CHECKPOINT 363 — THE RE-EXAMINATION: WHERE REST_print CAME FROM

**Charged:** ledger entry 915. **Scope:** Phase 361's scoped R1–R3.
**Work:** `phase363/work/`. **Machine-readable results:**
`phase363/results/p363_results.json`.

## Verdict: ORIGIN IN R2

The (0, 8/105, 0) was manufactured by the programme's own Phase 241
driver. Its monomial function **m39** (MONO position 38, group c3,
ξ⁰ coefficient 2/315) computes the (3.15) monomial
**N40 = R^{pqrs} R_{pqt a} R_{rs}{}^t{}_{b}** with the third factor's
index raised from the **wrong slot**: it forms R^t{}_{rsb} (slot 0
raised) and contracts it where the monomial requires
R_{rs}{}^t{}_{b} (slot 2 raised). At the Ellis throat the
miscontraction reads mixed diag (0, **+4**, 0) against the verbatim
monomial's (0, **−8**, 0) — a raw T^r_r error of +12, worth exactly
210·(2/315)·12 = **+16 bracket** in the stored ξ⁰ T^r_r total. That
single defective cell is the whole discrepancy: the Stage-4 back-out
converted the corrupted total into REST_print, and the corrupted
REST was misread downstream as an implied print H{2,0}(3) of
(80, 80/3, 112). **There is no misprint in DF anywhere in the tested
chain.** R1 and R3 are cleared in full (below).

## Control (passed before anything was quoted)

The Stage-4 back-out chain, re-run in exact Fractions from the stored
Phase 241 totals and sector values (`work/p363_control.py`),
reproduces REST_print = (44/135, 4/27, 100/189) exactly and
REST_print − REST_derived = (0, 8/105, 0). Internal cross-check: the
chain's H(6,3)(2) input (52, 12, 60) reproduces Stage 3's
independently recorded backed-out H(6,3)(5) = (20, −36, 84) exactly.

## R1 — the back-out algebra: CLEARED

The algebra is exact and **every value it consumed is verified**:
each print §2 form was evaluated at the Ellis throat from Phase 361's
independent double transcription with the VAL-0-certified library
(`work/p363_r1_evals.py`), and each agrees **exactly** with the value
the back-out used. Side/forced audit:

| subtraction | w(ξ⁰) | side used | forced or assumed | this phase's check |
|---|---|---|---|---|
| H{2,0}(1) (224, 32, 224) | +1/56 | print, by construction (solved from totals' ξ²) | forced given totals + weights (sole ξ² carriers: H{2,0}(1), H(6,3)(1) at 1/2, 1/2) | print (2.22) at throat = (224, 32, 224) exactly |
| H(6,3)(1) (92, 20, 92) | +1/216 | print, by construction (solved from totals' ξ³) | forced given totals + weights (sole ξ³ carrier, weight −1) | print (2.24) = (92, 20, 92) exactly |
| H(6,3)(2) (52, 12, 60) | −1/180 | **derived** | **assumed** in 259 (Stage 1c, from preserved contents) — but doubly safe: (i) any side error Δ in H(6,3)(2) shifts the backed-out H(6,3)(5) by exactly +Δ, and the two subtractions carry weights −1/180 and +1/180, so the error **cancels in REST identically** (proved in the memo); (ii) print (2.25) at throat = (52, 12, 60) exactly — the assumption was also factually right |
| H(6,3)(5) (20, −36, 84) | +1/180 | print, by construction (mode-3 back-out from totals' ξ¹) | forced given totals, weights, and the rows above | print (2.28) = (20, −36, 84) exactly (not merely up to Stage 3's pure-trace freedom) |
| H(6,3)(6) (4, −4, 52) | +1/1260 | print §2 transcription (Stage 3, t3-swap) | assumed — carried a recorded S-residue caveat | independent transcription evaluates to (4, −4, 52) exactly; the sole-origin-required (4, 92, 52) is **refuted** |
| H(6,3)(7) (−4, 20, 92) | +17/7560 | derived candidate A | assumed, backed by Stage 3's direct calibration (1.1×10⁻¹² over 26 points) | print (2.30) = (−4, 20, 92) exactly |
| H(6,3)(8) (−1, 5, −25) | −1/270 | print §2 transcription (Stage 3) | assumed — same caveat family as (6) | print (2.31) = (−1, 5, −25) exactly; sole-origin-required (−1, −109/7, −25) **refuted** |

Netting structure: the three solved subtractions (H{2,0}(1),
H(6,3)(1), H(6,3)(5)) are **conduits of the totals** — they transmit
a totals error but originate none. Given the totals, REST is forced.
The back-out originates nothing.

*Bookkeeping note (fence): the H(6,3)(5) row re-derives only the
subtraction's arithmetic and its throat value. It does not re-open,
use, or disturb Phase 241's H(6,3)(5),(6),(8) indictment, which
concerns those print tensors' behaviour in the full assembly's core
arbitration and stands exactly as recorded.*

## R2 — the harness's throat evaluation of (3.15): ORIGIN FOUND

Independent path: Phase 361's resolved (3.15) transcription evaluated
with the certified library on the exact SSS throat jet (one addition:
∇∇Riem built by applying the engine's covariant-derivative op twice,
needed for monomial N15; that addition is itself cross-validated —
the driver's N15 value agrees with it exactly). Result against the
stored harness totals (Phase 241 `DF_throat_cubics`): **11 of 12
entries exact** (ξ¹, ξ², ξ³ all components; ξ⁰ T^t_t, T^θ_θ). The
single deviation: **ξ⁰ T^r_r — independent 931/9, stored 1075/9,
difference exactly −16 bracket**.

Localisation (per-monomial, driver functions vs exact library, all
58 entries, programme order per Phase 361 Arm B): the driver's group
sums split as d20 −920 / c3 238/3 / t20 976 / tc3 −143/9 against the
exact −920 / 190/3 / 976 / −143/9 — the entire +16 sits in group
**c3**, and inside c3 exactly one monomial differs: **N40**
(driver raw (0, +4, 0) vs exact (0, −8, 0); all other 57 monomials
agree in all three components). From-scratch verification with
explicit index gymnastics (no library monomial function): the
verbatim R^{pqrs}R_{pqt a}R_{rs}{}^t{}_{b} gives (0, −8, 0); the
driver's variant (slot-0 raise, R^t{}_{rsb}) gives (0, +4, 0);
weighted difference 210·(2/315)·12 = 16 exactly.

The defect, in the driver's own code (`phase241/work/p2411_driver.py`,
function m39, registered with coefficient (2/315) for the monomial at
position 38): `R1 = raise_idx(G['Riem'], 0, G['ginv'])  # R^t_{rsb}`,
then contracted under the keying ('t','r','s','b') against
R^{pqrs} and R_{pqt a} — i.e. the raised index is placed in the third
slot of the contraction while having been raised from the first. The
correct factor is R_{rs}{}^t{}_{b} = g^{tu}R_{rs u b}.

Why it survived every earlier check: Phase 241's controls audited
coefficients and reproduced totals *through the same driver*; Phase
361's Arm B audited the (3.15) **coefficients** (specs) against print,
not the monomial functions' values; and every downstream read that
mattered was a difference in which the corrupted REST cancels (next
section). This phase's R2 is the first value-level confrontation of
the stored totals against an independent evaluation.

## R3 — the THA target side: CLEARED

The harness `tha_ellis` at R = 1 returns, per ξ-power: Tt (1033,
−11242, 33180, −19320), Tr (**187**, −1806, 5460, −4200), Tθ (1213,
−11634, 33180, −19320). The ξ⁰ targets (1033, 187, 1213) equal the
stored totals minus Phase 259's stored print residuals exactly; the
Tr polynomial is the registered [187, −1806, 5460, −4200]. The
differencing (assembled − target, bracket = 210 × DF-sum, per power)
is as recorded. No target-side or differencing defect. Consistency
spot values: DF − THA at ξ¹ = (+448, +448, +448) (the recorded print
ξ¹ residual, carried by the genuine H(6,3)(5) pure-trace difference);
at ξ² and ξ³ the totals equal the targets exactly.

## Consequences (arithmetic facts; claim wording is Gate-38's)

1. **The +16 was never a property of any assembly.** With the
   corrected ξ⁰ total (931/9), the print assembly's ξ⁰ throat
   residual is (−656/9, −752/9, −656/9), and Phase 259's substitution
   moves (Tr: +224/3, +8/3, +56/9 = +752/9) close the T^r_r cell to
   exactly 0. Phase 259's "FULL fails ξ⁰ by +16" headline and the
   decay/wider-set ξ⁰ residuals were computed through the corrupted
   totals/REST and carry the local m39 error at each point (size
   varies by point; only the throat's is computed here: exactly 16,
   T^r_r only).
2. **The arbitrated closures are untouched.** Every 318/323/Gate-37
   arbitrated read replaces REST wholesale by the derived aggregate;
   REST enters the FULL residual with sign + and the substitution
   delta with sign −, so the corrupted value cancels identically.
   The derived assembly's exact core closures, G37-B, and the
   identification's substance (G37-C) stand exactly as judged — on
   per-tensor evaluations, none of which is the corrupted cell. What
   falls is only the attribution (G37-A's location clause, already
   fallen per 355/361): there is no DF misprint behind the residual
   at all; the "implied print (80, 80/3, 112)" was the driver's
   defect, laundered through the back-out. The A-throat implied
   tensor (9/4, 25/12, 7/12) is an artefact of the same mechanism
   (the A totals came from the same driver; the A defect's size is
   not computed here) — while G37-B's closure there is again a
   differenced read and stands.
3. **Priced follow-up (named, not run):** repair m39 (raise slot 2)
   and re-run the Phase 241 driver's totals on the Phase 237/259
   background set; restate every print-assembly ξ⁰ residual in the
   259 record (throat decay profile, A throat, wider-set maxima C
   250 / E 108 / D 7.997) on corrected totals. Mechanical, one
   function changed, all other monomials already verified against
   the exact library at the throat. Until it runs, stored print-side
   ξ⁰ residuals in the 259 record should be read as carrying an
   unquantified per-point m39 contribution.

## Fences

Nothing posted anywhere. v1.27.0's wording not altered (Gate-38 owns
claim wording; this phase supplies it the mechanism). Phase 241's
indictment kept distinct throughout (see the R1 bookkeeping note).
No ledger append; no successor launched.

**DESK:** literature and exact computation only; no observational
data; nothing for the Publishing Desk.
