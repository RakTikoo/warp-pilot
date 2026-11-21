# Warp Pilot — Targets and Baselines

## Standing rules
- Licence-free Python only. No MATLAB. Core numerics NumPy, float64 everywhere.
- Replication / audit / QI ledger = calibration and tooling only.
- End goal: a NOVEL, REAL result (definition in Phase 2 below), or a verified
  exclusion map of the searched region. An honest negative counts.
- Never report a candidate from a single code path, a single grid, or an
  Eulerian-only check (the 2021 failure mode).

## Fuchs et al. 2024 baseline — FROM THE PRIMARY PAPER
Source: arXiv:2405.02709v1, "Constant Velocity Physical Warp Drive Solution",
Class. Quantum Grav. 41, 095013. Read in full 2026-11-20 via arXiv HTML.

| Quantity | Value | Where in the paper |
|---|---|---|
| Inner shell radius R1 | 10 m | §3, text after Eq. (25) / Fig. 4 discussion |
| Outer shell radius R2 | 20 m | §3, same passage |
| Total (ADM) mass M | 4.49×10^27 kg = 2.365 Jupiter masses | §3, same passage + footnote 8; repeated Table 1 |
| Constant trial density rho' | 3M / (4π (R2^3 − R1^3)) = 1.53×10^23 kg/m^3 | Eq. (19) + numbers above |
| Shift added inside shell, beta_warp | **0.02** (dimensionless, g_01 shift covector amplitude) | §4.1, text after Eq. (28) |
| Warp-shell light-ray asymmetry delta_t | ≈ 7.6 ns (matter shell: 0 ns) | §5.1, Table 1 |
| Smoothing span ratio s_rho / s_P | ≈ 1.72 (moving average ×4 passes) | §3, footnote 7 passage |
| Stress-energy scale / error floor | T ~ 10^39 J/m^3; meaningful above ~10^34 J/m^3 | §3.2, Appendix A |

**Correction to the research report:** the report's "~0.04c" velocity comes from
Table 1's heading, which states the comparison speed (v_warp = 0.04c) used for the
*reference* metrics (Alcubierre, Van den Broeck, Modified Time). The warp shell's
own added shift is beta_warp = 0.02 (§4.1), and by the paper's Eq. (8)
(dx^i/dt = −gamma^ij beta_j, gamma ≈ delta inside) the passenger transport speed
of the Fuchs warp shell itself is ≈ 0.02c. The secondary mass figure
(2.365 Jupiter masses) is CONFIRMED by the primary text.

**Why this baseline is beatable in principle (paper's own words):**
- §5.2: the shift used is "very conservative"; profiles can be optimised to place
  energy density where momentum flux is highest.
- §6: "The metric construction process of smoothing can be replaced by a direct
  1D optimization of the radial profiles for density, pressure, and shift vector,
  possibly reducing required mass by orders of magnitude."
Fuchs used a *constant* trial density and MATLAB moving-average smoothing.
Our search varies profile shapes and shift/density matching directly.

## Phase 0 calibration targets
- Alcubierre analytic Eulerian density (Alcubierre 1994 / Pfenning–Ford Eq. 8):
  rho_E = −(v^2 / 32π) · ((y^2+z^2)/r^2) · (df/dr)^2  [G=c=1]
  Negative wherever non-zero; zero on the x-axis and wherever f'=0.
- WarpFactory (Helmerich et al. 2024) published results: Alcubierre and
  Van den Broeck both show energy-condition violations localised in the bubble
  wall. Our pipeline must reproduce violation *locations and signs*.
- Rejection: Natário-class metrics (unit lapse, flat spatial slices) must be
  flagged as WEC/DEC-violating for all observers (Santiago–Schuster–Visser,
  PRD 105, 064038 (2022): violations at any speed in this class).

## Phase 1 QI-ledger anchors (Pfenning & Ford 1997, primary, arXiv:gr-qc/9702026)
- Eq. (26)/(28): E = −(v_b^2/12) ∫ r^2 (f')^2 dr
  = −(v_b^2/12)(R^2/Δ + Δ/12) for piecewise-linear f (Planck units).
- R = 100 m, Δ = 1 m, v_b ~ 1: |E| ≈ 0.25–0.6 M_sun ("order of a quarter of a
  solar mass", §4 text after Eq. 31).
- R = 100 m, Δ = QI wall (few hundred Planck lengths): E ≈ −3×10^20 galaxy
  masses × v_b (Eq. 31).
- Scaling: |E| ∝ v^2 R^2 / Δ (thin-wall limit).
- Van den Broeck anchor: total negative energy of order a few solar masses for
  his published pocket parameters (VdB 1999) — to be checked against our own
  numerical integration for the same parameters, not assumed.
- Casimir scale: rho_Casimir(1 µm) ≈ −π^2 ħc/(720 a^4) ≈ −1.3×10^-3 J/m^3.

## Phase 2 novel-search space (outside Santiago–Schuster–Visser scope)
SSV covers Natário class only (unit lapse, flat spatial slices). Search:
- Fuchs-type spherical shells built from *non-constant*, matched radial
  profiles (density / pressure / shift), non-unit lapse a(r), non-flat spatial
  metric b(r) — varied profile family, edge widths, span ratio, shift
  amplitude beta_w, shift transition placement and shape, R1, R2, M.
- Van den Broeck-type conformal spatial factor as a free function (secondary).
- Subluminal first. Bounded superluminal stretch on the shell family only,
  labelled as stretch, adversarially re-checked.

A candidate is NOVEL AND REAL only if ALL hold:
1. Not a published configuration; difference documented.
2. NEC/WEC/SEC/DEC pass for ALL observers (Hawking–Ellis eigenvalue margins),
   margins > numerical error from the convergence study, on ≥2 refinements.
3. Two independent code paths agree.
4. Beats the Fuchs baseline above on ADM mass / peak density at comparable
   R1, R2, beta_w — OR is a new geometry-class member passing where published
   members fail.
5. QI-ledger cost computed and reported alongside.
Fallback deliverable: verified exclusion map of the searched region.
