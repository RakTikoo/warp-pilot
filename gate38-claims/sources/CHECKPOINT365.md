# CHECKPOINT 365 — THE m39 REPAIR AND THE 259 RESIDUAL RESTATEMENT

**Charged:** ledger entry 920. **Registration:**
`work/p365_registration.md` (filed before computation).
**Work:** `phase365/work/`. **Machine-readable results:**
`phase365/results/p365_restatement.json`; controls output
`phase365/work/p365_controls_out.json`.

## Verdict: RESTATEMENT COMPLETE

All four registered controls pass. The Phase 241 driver's m39
defect (Phase 363: N40's third factor raised from Riemann slot 0
instead of slot 2) is repaired in a versioned copy, and every
print-side ξ⁰ residual in the Phase 259 record is restated on
corrected totals, per background, with the m39 contribution Δ
stated at each.

## The repair artefact

`work/p2411_driver_v2.py`: full copy of the stored driver, one
functional change in `m39` — `raise_idx(G['Riem'], 2, G['ginv'])`
keyed (r,s,t,b) = R_{rs}{}^t{}_{b}, contracted under
('r','s','t','b'), replacing slot-0 raise keyed (t,r,s,b).
Verbatim diff: `work/p365_m39_diff.txt` (one hunk). The stored
driver was not edited.

## Controls (passed before any re-run value was quoted)

- **C-m39:** stored m39 raw (0.0, +4.0, 0.0); repaired
  (0.0, −8.0, 0.0) = 363's certified verbatim value, float-exact.
- **C-total:** throat ξ⁰ totals: stored side reproduces
  (8641/9, 1075/9, 10261/9); repaired side gives T^r_r = 931/9
  (max dev from certified fractions 1.14×10⁻¹³ both sides).
  Difference at ξ⁰ exactly (0, 16, 0); at ξ¹/ξ²/ξ³ exactly 0.0.
- **C-REST:** 363's exact-Fraction chain with the single corrected
  input tdf[0] T^r_r = (931/9)/210 returns REST =
  (44/135, 68/945, 100/189) = REST_derived **exactly in all three
  cells**; the shift from REST_print is exactly (0, −8/105, 0) =
  −(0, 16, 0)/210, accounted cell by cell (T^t_t: raw Δ = 0;
  T^r_r: 210·(2/315)·12 = 16 bracket = 8/105 DF-sum; T^θ_θ: raw
  Δ = 0). H5p assert (20, −36, 84) holds unchanged.
- **C-58:** all 58 monomials agree with 363's certified exact
  library in all three components (every rationalised bracket
  difference exactly 0; max float dev 5.3×10⁻¹⁵).

## Re-run (24 backgrounds, the harness's `build_backgrounds()` set)

Guard: the stored driver's totals reproduce `p2411_results.json`
bit-exactly (DF and residuals, max dev 0.0) and the 259 print
cells to 5.7×10⁻¹⁴; corrected-via-Δ print cells match the repaired
driver's direct residuals to 5.7×10⁻¹⁴; Δ at ξ¹/ξ²/ξ³ = 0.0
everywhere. Δ (ξ⁰, bracket) per background — full table in the
memo and JSON. Headline values: throat (0, 16, 0); A_throat
(0, 2, −7); C:1/2 (0, 250, 117); D family Δ T^θ_θ ∈ [−8.00,
−7.27]; E:1/10 (64, 66, −7) — the only family with Δ T^t_t ≠ 0 is
E (Φ′ ≠ 0).

## Restatement headlines (bracket; per-cell detail in the JSON)

- **Print:** throat ξ⁰ (−72.888889, −67.555556, −72.888889) →
  (−72.888889, **−83.555556**, −72.888889) = (−656/9, −752/9,
  −656/9), 363's figure. Core ξ⁰ max 72.888889 → 83.555556.
  Wider maxima: A_fullr 2.537739 → 1.952107; C 892.888889 →
  989.555556; D 17.899347 → 20.578764; E 155.444444 → 170.444444.
  7 sign changes (all T^θ_θ).
- **FULL:** throat +16 → 5.7×10⁻¹⁴ (closes); A throat (0, +2, −7)
  → ~10⁻¹⁴ (closes). Decay-profile point maxima at R=1.5/2/3
  (0.291404 / 0.052979 / 0.002896) **stand** — T^θ_θ cells,
  Δ T^θ_θ = 0 on the Ellis family; their T^r_r cells move
  (R=1.5: +0.021386 → −0.101932, sign change). Core ξ⁰ max
  16.0 → **0.291404** (Ellis R=1.5 T^θ_θ). Wider maxima:
  A_fullr 4.116167 → 0.267252; C 250.0 → 4.5×10⁻¹² (the 250.0
  was Δ at C:1/2 exactly); D 7.996625 → 6.0×10⁻¹⁴;
  E 108.044444 → 42.044444 (E:1/10 T^r_r, survives).
  Gate readout restated: P(ξ) [203, …] → [187.00000000000006,
  −1806, 5460, −4200] (ξ⁰ dev +16 → 6×10⁻¹⁴); P root dev
  0.008958 → 7.0×10⁻¹²; NEC max dev 0.007904 → 4.9×10⁻¹²;
  Δp_r 1.71996×10⁻⁴ → 9.158220×10⁻⁵ = target; Δp_r(m·r₀=2)
  4.29990×10⁻⁵ → 2.289555×10⁻⁵ = target; Δρ, Δp_t unchanged.
  28 cells close to zero, 5 sign changes, none open from zero.
- **only5/6/8:** core ξ⁰ maxima 7.111111 → 8.888889 (throat
  T^r_r sign change +7.111111 → −8.888889); 71.555556 →
  80.888889; 76.0 → 77.333333. Wider maxima and all cells in the
  JSON. Sign changes: 32 / 6 / 11.
- **Total flags: 89 cells** (sign changes + closes-to-zero),
  enumerated per cell in the JSON.
- **Survivors (FULL ξ⁰, not m39):** zero at throat, A throat,
  all C, all D, E:1/2. Nonzero: Ellis T^θ_θ decay cells
  (≤ 0.291404), A_fullr (≤ 0.267252), E:7/20 (≤ 0.300672),
  E:1/5 (≤ 3.825), E:1/10 (21.511111, 42.044444, 21.511111) —
  the widest-set survivor. At E:1/5 and E:7/20 the corrected
  FULL T^t_t = T^θ_θ exactly (degeneracy restored).

## Fences

The derived-side record is untouched: REST cancels in every
arbitrated difference, so this phase changes no closure, no gate
figure, and no identification substance — the Phase 318/323 exact
core closures, Gate-37's figures, and the derived assembly stand
exactly as judged. Restated here: only the Phase 259 record's own
print-side ξ⁰ residuals and its internal Stage-4 readout (a Phase
259 internal record against Phase 219 targets, not a Gate-37
figure); claim wording on the restated numbers is Gate-38's.
Phase 241's H(6,3)(5),(6),(8) indictment stands distinct, neither
re-derived nor re-judged. Stored records unedited. Nothing posted
anywhere. No ledger append; no successor launched.

**DESK:** literature and exact computation only; no observational
data; nothing for the Publishing Desk.
