# P259-1 Stage 4 — Gate readout: assembly + deciding checks (FU-P228-2c)

Assembly: Eq. (3.14) weights print-exact (H(5) −(1/30)(ξ−1/6),
H(6) 1/1260, H(8) −1/270; prefactor ratio 210); the other seven
H-tensors stay print. FULL = derived H(5), H(6), H(8-B) substituted;
only5/only6/only8 = single substitutions. No coefficient adjustments
anywhere. Mode 2 (direct) primary, mode 1 (Δ) cross-check, mode 3
(back-out, §2 print H6/H8) third check. Machine record:
`p2591_assembled.json`; runner `work/p2591_run_stage4.py`.

**Headline: the FULL assembly fails the deciding checks — at ξ⁰
only, and at the throat in exactly one cell (Tʳ_r, +16). Every ξ¹,
ξ², ξ³ check passes; per-power conservation passes. This is the
K3 pattern (corrected tensors, assembly still fails), with the
failure priced below.**

## 1. Consistent core (bar: ≤2.2×10⁻⁸ all powers; ξ²/ξ³ ≤1×10⁻¹⁰)

Max residuals per ξ-power (Ellis R = 1, 1.5, 2, 3 + A throat):

| assembly | ξ⁰ | ξ¹ | ξ² | ξ³ |
|---|---|---|---|---|
| print | 72.889 | 448.0 | 6.8×10⁻¹³ | 2.8×10⁻¹³ |
| **FULL** | **16.0 ✗** | **3.4×10⁻¹³ ✓** | 6.8×10⁻¹³ ✓ | 2.8×10⁻¹³ ✓ |
| only5 | 7.111 ✗ | 3.4×10⁻¹³ ✓ | 6.8×10⁻¹³ | 2.8×10⁻¹³ |
| only6 | 71.556 ✗ | 448.0 ✗ | 6.8×10⁻¹³ | 2.8×10⁻¹³ |
| only8 | 76.0 ✗ | 448.0 ✗ | 6.8×10⁻¹³ | 2.8×10⁻¹³ |

ξ²/ξ³ are bit-identical to the print assembly (no degradation ✓).
FULL ξ⁰ residuals by point: Ellis R=1: **16.0**; A throat: 7.0;
Ellis R=1.5: 0.291; R=2: 0.0530; R=3: 0.00290. At Ellis R=1 the
FULL ξ⁰ failure is a single cell: Tt and Tth residuals are 0.0,
**Tr residual = +16.0 exactly** (print: Tt −72.889, Tr −67.556,
Tth −72.889; ξ¹ print +448 in all three, FULL 0.0 in all three).

## 2. Per-power assembled conservation, Ellis ℓ=1 (bar ≤1×10⁻¹², DF-sum units)

FULL, route (ii) (linearity: harness jet S of printed total +
certified derived S + back-out S(H5p) = 6.0 in-runner + Phase 241
recorded S(H6p) = 0.4375, S(H8p) = 0.84375 — the decomposition
consistent with the printed total, 6/180 + 0.4375/1260 −
0.84375/270 = 0.030556 exactly):

| ξ⁰ | ξ¹ | ξ² | ξ³ |
|---|---|---|---|
| −8.1×10⁻¹⁶ ✓ | +2.0×10⁻¹⁵ ✓ | −6.5×10⁻¹⁵ ✓ | 0.0 ✓ |

Route (i) (jet route on assembled total jets, §2-transcribed print
H6/H8 jets): ξ¹/ξ²/ξ³ identical passes; ξ⁰ = **−4.464×10⁻⁴** —
exactly the §2 transcription residue, labelled: it equals
(1/1260)(0.4375 − 0.671875) − (1/270)(0.84375 − 0.773438), the
recorded §2-vs-Phase-241 S deviations of H(6)/H(8). Attribution
(route ii): only5 leaves ξ⁰ S = −0.002778 (the H6+H8 print
remainder); only6 ξ⁰ 0.0302, only8 ξ⁰ 0.0337, both keep ξ¹ = −0.2.

## 3. Ellis gate (FULL; Phase 219 targets)

| sub-check | target | FULL | verdict |
|---|---|---|---|
| forced deficit | −0.07957747155 | −1/(4π) exact | **PASS** |
| P(ξ) coefficients | 187, −1806, 5460, −4200 | **203**, −1806, 5460, −4200 | FAIL: ξ⁰ coef dev **+16.0** (bar 1×10⁻⁸); ξ¹–ξ³ exact |
| P root | 0.86035766893 | 0.869316 | FAIL (dev 0.00896, driven by the +16) |
| NEC roots | 0.15155109082 / 0.25959968220 / 1.42218256030 | 0.144365 / 0.267503 / 1.421465 | FAIL: max dev **0.007904** (bar 1×10⁻⁸) |
| Stage B Δρ (m·r₀=1) | 4.244053×10⁻⁵ | 4.244053×10⁻⁵ (rel dev 2.5×10⁻⁸) | **PASS** |
| Stage B Δp_t | 5.338572×10⁻⁴ | 5.338572×10⁻⁴ (rel dev 1.2×10⁻⁸) | **PASS** |
| Stage B Δp_r (m·r₀=1) | 9.158220×10⁻⁵ | 1.71996×10⁻⁴ (rel dev 0.878) | FAIL |
| Stage B Δp_r (m·r₀=2) | 2.289555×10⁻⁵ | 4.2999×10⁻⁵ (rel dev 0.878) | FAIL |

The Δp_r failure is exactly the throat Tr ξ⁰ error: Δp_r is read
from Tr at ξ = 1/6, and 16/(20160π²) = 8.04×10⁻⁵ is precisely the
excess over target. Attribution (throat ξ⁰, Tt/Tr/Tth moves vs
print): only5 moves all three by +74.667 (leaves Tr +7.111, P dev
7.111, NEC dev unchanged 0.002745, Stage B unchanged — Δρ/Δp_t are
ξ=1/6 reads where only5's ξ¹ fix and ξ⁰ move cancel); only6 moves
Tt/Tth +1.333, Tr +2.667; only8 moves Tt/Tth −3.111, Tr +6.222.
The three moves sum exactly to the FULL result at every throat
cell (Tr: −67.556 + 74.667 + 2.667 + 6.222 = +16.0).

## 4. Wider set, FULL (max residuals per family per ξ-power)

| family | ξ⁰ | ξ¹ | ξ² | ξ³ |
|---|---|---|---|---|
| A full-r | 4.116 ✗ | 7.7×10⁻¹³ | 1.9×10⁻¹² | 1.4×10⁻²⁸ |
| C | 250.0 ✗ | 2.5×10⁻¹² | 7.3×10⁻¹² | 2.7×10⁻¹² |
| D | 7.997 ✗ | 4.7×10⁻¹³ | 1.3×10⁻¹² | **1680.0** (THA charge kept ✓) |
| E | 108.0 ✗ | 2.9×10⁻¹¹ | 5.8×10⁻¹¹ | 9.1×10⁻¹² |

ξ¹ is fixed on the whole set (print: 5488 / 110 / 896 / ~0 →
≤2.9×10⁻¹¹); every remaining wider failure is ξ⁰-only. Family-D
ξ³ keeps the 1680-unit charge on THA Eq. (26) ✓.

## Cross-checks and caveats

- Mode 1 vs mode 2: max dev **2.91×10⁻¹¹** absolute — above the
  1×10⁻¹² headline bar, reported as required. Characterisation
  (recomputed from the checkpoint cache): on all core points
  (max |total| ≤ 600) the dev is ≤4.6×10⁻¹⁴; the 10⁻¹¹-level devs
  sit only on the largest C-family totals (|T| up to 8.6×10⁵) and
  are float-accumulation differences between the driver's
  eval_df totals and the sum of individually evaluated H values.
  The assembly algebra itself is exact-Fraction: mode 3 vs mode 2
  (FULL) agree to 2.27×10⁻¹³, and mode 3's solved print H5 matches
  the back-out. No verdict is within three orders of magnitude of
  this noise (passes ≤3.4×10⁻¹³, failures ≥7).
- Validation vs Stage 3: all derived/print pattern values used
  here reproduce `p2591_arbitration.json` exactly (max dev 0.0;
  back-out H5 1.9×10⁻¹²; derived-A vs print H7 1.1×10⁻¹²).
- Print H(6)/H(8) values enter through the §2 transcription
  (Stage 3 residue caveat). The ξ⁰ failures above (16.0 etc.) are
  ~10⁵ times larger than any plausible §2 value residue on this
  set and are exact rational-looking numbers (16, 7, 2, +74.667
  moves); the S route-(i) ξ⁰ number is the one place the residue
  is the whole signal, and it is labelled as such.
- Print-sector inputs H{2,0}(3)/H(3)/H(4) enter only through
  their ξ⁰ weighted aggregate, backed out of the printed totals
  exactly (their weights are ξ⁰-only constants); H(1)/H{2,0}(1)
  likewise by exact back-out; H(2) = derived (Stage 1c), H(7) =
  derived A (Stage 3 calibration).

## Bottom line for the coordinator

FULL passes: ξ¹/ξ²/ξ³ core (≤3.4×10⁻¹³), no-degradation, per-power
conservation (route ii, ≤6.5×10⁻¹⁵), forced deficit, Stage B Δρ
and Δp_t, family-D ξ³ charge. FULL fails: core ξ⁰ (16.0 at the
throat Tr cell, 7.0 at A throat Tth), gate P (ξ⁰ coefficient
+16), gate NEC (0.007904), gate Stage B Δp_r (rel 0.878 — the
same +16 read at ξ = 1/6). All failures trace to one ξ⁰ sector
that no single substitution fixes: H(5) removes most of it
(throat Tr +74.667 of the needed +83.556), H(6) and H(8-B) add
+2.667 and +6.222, and +16.0 remains. Iteration 2 was not run;
Stage 5 discriminators were not touched.
