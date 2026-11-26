# Phase 365 memo — THE m39 REPAIR AND THE 259 RESIDUAL RESTATEMENT

**Verdict: RESTATEMENT COMPLETE.** All four registered controls
pass; the repaired driver is what Phase 363 certified; every
print-side ξ⁰ residual in the Phase 259 record is restated below
with its old value, corrected value, and the m39 contribution at
that background. Full record: `phase365/CHECKPOINT365.md`;
machine-readable restatement: `phase365/results/
p365_restatement.json`; controls output: `phase365/work/
p365_controls_out.json`. All values bracket units (210 × DF sum)
unless stated.

## The repair artefact

`phase365/work/p2411_driver_v2.py` — a full copy of the Phase 241
driver with exactly one functional change, in `m39`: the third
factor of N40 = R^{pqrs} R_{pqt a} R_{rs}{}^t{}_{b} is now formed by
raising Riemann slot 2 (`raise_idx(G['Riem'], 2, G['ginv'])`, keyed
(r, s, t, b) = R_{rs}{}^t{}_{b}) instead of slot 0 (keyed
(t, r, s, b) = R^t{}_{rsb}), and contracted under the keying
('r','s','t','b'). The verbatim diff against the stored driver —
one function, saved as `phase365/work/p365_m39_diff.txt` — is part
of the artefact. The stored driver was not edited.

## Controls (all passed before any re-run value was quoted)

- **C-m39:** at the Ellis throat, the stored m39 reads raw mixed
  (0.0, +4.0, 0.0); the repaired m39 reads (0.0, −8.0, 0.0) — 363's
  certified verbatim value, float-exact.
- **C-total:** `eval_df` throat totals reproduce the stored
  (8641/9, 1075/9, 10261/9) ξ⁰ and, repaired, give ξ⁰ T^r_r =
  931/9 (max deviation from the certified fractions 1.14×10⁻¹³ on
  both sides). The stored-minus-repaired difference at ξ⁰ is
  exactly (0, 16, 0); at ξ¹/ξ²/ξ³ it is exactly 0.0 (m39's
  coefficient is the constant 2/315 — ξ⁰ only).
- **C-REST — the (0, 8/105, 0), cell by cell:** 363's exact-Fraction
  back-out chain re-run with the single corrected input
  tdf[0] T^r_r = (931/9)/210 gives REST = (44/135, 68/945, 100/189)
  = REST_derived **exactly, in all three cells**. The shift from
  REST_print (44/135, 4/27, 100/189) is exactly (0, −8/105, 0), and
  it is m39's throat contribution in DF-sum units, (0, 16, 0)/210:
  the T^t_t cell is untouched because m39's raw T^t_t difference at
  the throat is 0; the T^r_r cell carries the whole 8/105 because
  the raw difference is +12 under the weight 210·(2/315)·12 = 16
  bracket; the T^θ_θ cell is untouched because the raw difference
  is 0. (The chain is exactly linear in tdf[0] with coefficient 1;
  its other solved inputs come from tdf[3], tdf[2], tdf[1], which
  m39 does not touch — the H5p assert (20, −36, 84) holds on the
  corrected chain unchanged.)
- **C-58:** the per-monomial confrontation (363's R2 protocol)
  re-run with the repaired monomials: **all 58 monomials agree with
  the certified exact library in all three mixed components** —
  every per-component bracket difference is exactly 0 under 363's
  rationalisation (max float deviation 5.3×10⁻¹⁵), N40 included.

## Re-run guard (the old side against the stored record)

The stored driver's re-run totals reproduce the Phase 241 record
**bit-exactly** (max deviation 0.0 against both the stored DF
values and the stored residuals in `p2411_results.json`) and the
Phase 259 print cells to 5.7×10⁻¹⁴. The corrected print cells
computed by subtracting Δ agree with the repaired driver's direct
residuals to 5.7×10⁻¹⁴. Δ at ξ¹/ξ²/ξ³ is exactly 0.0 at every one
of the 24 backgrounds. The re-run machinery is the 259 machinery.

## The m39 contribution Δ (ξ⁰, bracket; stored total − repaired total)

| background | Δ T^t_t | Δ T^r_r | Δ T^θ_θ |
|---|---|---|---|
| Ellis R=1.0 | 0 | 16 | 0 |
| Ellis R=1.5 | 0 | 0.123317546 | 0 |
| Ellis R=2.0 | 0 | 0.00390625 | 0 |
| Ellis R=3.0 | 0 | 3.01068×10⁻⁵ | 0 |
| A_throat | 0 | 2 | −7 |
| A_fullr l=0.5 | 0 | 1.17126427 | −4.09942496 |
| A_fullr l=1.0 | 0 | 0.305263833 | −1.06842342 |
| A_fullr l=2.0 | 0 | 0.0102426203 | −0.035849171 |
| C:1/2 | 0 | 250 | 117 |
| C:1 | 0 | 54 | 19 |
| C:2 | 0 | 16 | 0 |
| C:3 | 0 | 9.25925926 | −3.37037037 |
| C:5 | 0 | 5.488 | −5.256 |
| C:8 | 0 | 3.90625 | −6.046875 |
| D:3/20 | 0 | 0.00675 | −7.996625 |
| D:3/10 | 0 | 0.054 | −7.973 |
| D:9/20 | 0 | 0.18225 | −7.908875 |
| D:3/5 | 0 | 0.432 | −7.784 |
| D:3/4 | 0 | 0.84375 | −7.578125 |
| D:9/10 | 0 | 1.458 | −7.271 |
| E:1/10 | 64 | 66 | −7 |
| E:1/5 | 3.375 | 5.375 | −7 |
| E:7/20 | 0.0787172012 | 2.0787172 | −7 |
| E:1/2 | 0 | 2 | −7 |

Recorded pattern (stated, not interpreted): Δ T^θ_θ = −7 at every
A and E point and between −8.00 and −7.27 on the D family;
Δ T^t_t = 0 except on the E family, the only family with Φ′ ≠ 0.

## Restated residuals — print assembly

Throat ξ⁰ (T^t_t, T^r_r, T^θ_θ): (−72.888889, −67.555556,
−72.888889) → **(−72.888889, −83.555556, −72.888889)** =
(−656/9, −752/9, −656/9), exactly 363's corrected print residual.
Core ξ⁰ max: 72.888889 → **83.555556**. Wider ξ⁰ maxima:
A_fullr 2.537739 → 1.952107; C 892.888889 → 989.555556;
D 17.899347 → 20.578764; E 155.444444 → 170.444444. Seven cells
change sign (all T^θ_θ: A_throat, A_fullr l=0.5/1.0/2.0, D:9/10,
E:7/20, E:1/2) — flagged in the machine record.

## Restated residuals — FULL assembly (the recorded comparisons)

- **Throat:** ξ⁰ cells (2.3×10⁻¹³, +16, 2.3×10⁻¹³) →
  (2.3×10⁻¹³, 5.7×10⁻¹⁴, 2.3×10⁻¹³). The +16 closes to zero.
- **A throat:** (0, +2, −7) → (0, 2.1×10⁻¹⁴, −1.1×10⁻¹⁴). Both
  nonzero cells close to zero (the recorded "A throat 7.0" was the
  T^θ_θ cell).
- **Decay profile (point maxima over components):** R=1: 16.0 →
  2.3×10⁻¹³. At R=1.5 / 2 / 3 the recorded maxima 0.291404 /
  0.052979 / 0.002896 **stand as recorded** — they are T^θ_θ cells,
  and Δ T^θ_θ = 0 on the whole Ellis family. Their T^r_r cells do
  move: R=1.5: +0.021386 → −0.101932 (sign change); R=2:
  0.004639 → 0.000732; R=3: 0.000546 → 0.000516.
- **Core ξ⁰ max:** 16.0 → **0.291404**, attained at Ellis R=1.5
  T^θ_θ — an m39-free cell that was in the record all along,
  masked by the throat's 16.
- **Wider ξ⁰ maxima:** A_fullr 4.116167 → **0.267252** (attained
  at l=1.0, T^r_r = −0.267252); C 250.0 → **4.5×10⁻¹²** (the
  recorded 250.0 at C:1/2 T^r_r was Δ itself, exactly);
  D 7.996625 → **6.0×10⁻¹⁴**; E 108.044444 → **42.044444**
  (E:1/10 T^r_r — survives correction; see below).
- **Gate readout (FULL, throat; Phase 259's Stage-4 readout
  against the Phase 219 targets):** P(ξ) coefficients
  [203, −1806, 5460, −4200] → **[187.00000000000006, −1806, 5460,
  −4200]** — the ξ⁰ deviation from target goes from +16.0 to
  6×10⁻¹⁴. P root deviation 0.008958 → 7.0×10⁻¹². NEC-roots max
  deviation 0.007904 → 4.9×10⁻¹². Stage B Δp_r: 1.71996×10⁻⁴ →
  **9.158220×10⁻⁵** (target 9.158220×10⁻⁵); Δp_r at m·r₀=2:
  4.29990×10⁻⁵ → **2.289555×10⁻⁵** (target 2.289555×10⁻⁵).
  Δρ (4.244053×10⁻⁵) and Δp_t (5.338572×10⁻⁴) are unchanged —
  Δ T^t_t = Δ T^θ_θ = 0 at the throat.
- **Flags:** 28 stored FULL ξ⁰ cells close to zero (throat T^r_r;
  A_throat T^r_r and T^θ_θ; every C-family T^r_r and T^θ_θ cell;
  every D-family T^r_r and T^θ_θ cell; E:1/2 T^r_r and T^θ_θ) and
  5 change sign (Ellis R=1.5 T^r_r; A_fullr l=0.5 and l=1.0 T^r_r;
  E:1/5 and E:7/20 T^θ_θ). No cell opens from zero.

## Restated residuals — only5 / only6 / only8 (summary; full cells in the machine record)

Core ξ⁰ maxima: only5 7.111111 → **8.888889** (throat T^r_r
+7.111111 → −8.888889, a sign change); only6 71.555556 →
**80.888889**; only8 76.0 → **77.333333**. Wider ξ⁰ maxima —
only5: A_fullr 2.537739 → 1.952107, C 175.111111 → 74.888889,
D 5.753778 → 2.979444, E 44.888889 → 21.111111. only6:
A_fullr 2.733033 → 1.735353, C 876.555556 → 961.138889,
D 17.571920 → 19.916410, E 168.577778 → 180.827778. only8:
A_fullr 3.920873 → 0.471912, C 931.0 → 943.083333,
D 18.663344 → 18.998271, E 121.688889 → 117.355556. Sign changes:
only5 32 cells, only6 6, only8 11 — all flagged per cell in the
machine record. Total flags across all assemblies: 89 cells.

## What survives correction (FULL ξ⁰ residuals that are not m39)

After correction the FULL assembly's ξ⁰ residual is zero (float
noise ≤ 6×10⁻¹⁴) at the Ellis throat, the A throat, every C point,
every D point, and E:1/2. The nonzero survivors: the Ellis T^θ_θ
decay cells (max 0.291404 at R=1.5); A_fullr (max 0.267252);
E:7/20 (0.011386, 0.300672, 0.011386); E:1/5 (0.675, 3.825,
0.675); and one substantial survivor, **E:1/10: (21.511111,
42.044444, 21.511111)** — the widest-set FULL ξ⁰ residual after
correction sits there, not at C:1/2. One internal-consistency
observation: at E:1/5 and E:7/20 the corrected FULL T^t_t and
T^θ_θ cells are exactly equal (0.675/0.675; 0.011386/0.011386) —
the degeneracy the miscontraction had broken is restored. These
survivors are stated as arithmetic facts of the corrected record;
what they mean for the 259 verdict's wording is Gate-38's, not
this phase's.

## Fences

The derived-side record is untouched: REST cancels in every
arbitrated difference (it enters the FULL residual with sign +
and the substitution delta with sign −, Phase 363 consequence 2),
so this phase changes **no closure, no gate figure, and no
identification substance**. The Phase 318/323 exact core closures,
Gate-37's figures, and the derived assembly's record stand exactly
as judged. What is restated here is the Phase 259 record's own
print-side ξ⁰ residuals and the internal Stage-4 readout computed
from the corrupted totals — including its gate-style readout
against the Phase 219 targets, which is a Phase 259 internal
record, not a Gate-37 figure. Phase 241's H(6,3)(5),(6),(8)
indictment stands distinct and was neither re-derived nor
re-judged. The stored Phase 241 driver and the stored 259 records
were not edited; the repair is a new artefact. Nothing posted
anywhere.

## DESK

Literature and exact computation only; no observational data;
nothing for the Publishing Desk.
