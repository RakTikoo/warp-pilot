# Figures pass — inventory (staging, 2026-11-24)

Scope of this pass: staging only. Nothing here is uploaded, no repo files are
edited, no ledger entry is appended. Every figure is drawn by code
(matplotlib, `~/workspace/warp-pilot/venv/bin/python`) from stored result
files; no plotted number is typed into a script by hand. Where a curve is
shown, it is either stored table points or the programme's own stored
closed form / stored evaluator code, evaluated by the script.

## First set — produced (see FIGURES.md for captions)

| # | Claim | Figure | Stored data drawn from |
|---|-------|--------|------------------------|
| 1 | Gate-35 / Phase 314: the pointwise member's required density is positive throughout the volume (continuum minimum +8.100317×10⁻⁵); its pressures still fail (NEC depth −5.33×10⁻⁴) | `fig_gate35_density.png` | `phase314/results/p314_results.json`; `gate35-claims/results/g35_item1_results.json`; stored evaluator `gate35/work/g35_rho.py` (the script's re-evaluation of ρ* at the stored argmin reproduces the stored global minimum 8.100316627374×10⁻⁵ exactly) |
| 2 | Gate-13 / Phase 116: composed nested shells hold a payload at 0.09758c | `fig_gate13_schematic.png` | `gate13-claims/code/wa_profiles.py` (shell supports + region cuts, regex-extracted); `gate13-claims/sources/p1161_alone.json` (outer span); `gate13-claims/sources/p1161_composed.json` (row anatomy) |
| 3 | Gate-14: multipartite QET delivers net negative energy at a total price of 5.34–28.17 per unit — not an energy source | `fig_gate14_qet.png` | `gate14-claims/results/g14_numbers.json` (rows, `sep_certificate`, stored `price_deciding_range_sep`) |
| 4 | Gate-33: spin-1 channel flat curve (HT 1.87×10⁻⁵ / NS–BH 1.70×10⁻² at c_V = 1, 2, 10) + Corner B | `fig_gate33_flat.png` | `gate33-claims/GATE33.md` §5 (G33-E/F) — see gap note G-1 |
| 5 | Phases 327/328/331: K_pair sech² separation profile; (1 − 4ξ) sign chart; QI price line R_exc = max(0, 12h − 1) | `fig_kpair.png` | `phase327/work/p327_results.json`; `phase328/work/p328_results_b.json`; `phase331/results/p331_results.json` (stored formula strings evaluated by the script; stored h values "1/12", "5/24" are fraction strings, parsed exactly) |
| 6 | Phase 309: the design-space map, 84 cells by state | `fig_phase309_map.png` | `phase309/results/DESIGN_SPACE_MAP.md` §(i), parsed by the script (84/84 cells; counts DECIDED 27 · PRICED 3 · CLOSED 7 · OPEN 8 · UNREACHED 39, matching the compile record) |
| 7 | 3D: Phase 314 bubble wall, density-coloured renders + exportable shell mesh | `model_bubble_wall_view1.png`, `model_bubble_wall_view2.png`, `model_bubble_wall_shell.png`, `bubble_wall_shell.obj`, `bubble_wall_shell.stl` | stored evaluator `gate35/work/g35_rho.py`; band [10, 20] from `gate35-claims/results/g35_item1_results.json` region ranges; member profile from `phase314/results/p314_results.json`. Mesh: 24,832 vertices / 49,152 faces; ρ on mesh ∈ [+8.1003×10⁻⁵, +2.6225×10⁻⁴] |
| 8 | 3D: Gate-13 nested payload shells, renders + mesh | `model_payload_shells_view1.png`, `model_payload_shells_view2.png`, `payload_shells.obj`, `payload_shells.stl` | `gate13-claims/code/wa_profiles.py` (radii); `gate13-claims/sources/p1161_composed.json` (row anatomy). Mesh: 35,040 vertices / 69,120 faces, five surfaces (payload r = 2; inner shell r = 2, 4; outer shell r = 5, 10) |

## Gap notes (recorded, not worked around)

- **G-1 (Gate-33):** no stored results JSON exists for the flat curve —
  `gate33-claims/results/` holds only the Fig. 7 extraction
  (`g33_fig7_data.json`). The quotable values live in the stored gate prose
  (GATE33.md §5). The figure script extracts them from that stored document
  by pattern (mantissa × 10^superscript, incl. the Corner B coordinate
  c₁₄* = 6.4227×10⁻⁹ at c_V = 3593.4 and its HT ratio 2.0607×10⁻¹⁸); it
  fails loudly if a pattern is absent. Nothing was hand-typed.
- **G-2 (Gate-13):** the inner shell's source span is not stored in the
  composition results (only the outer span [4.5, 10.5] is, in
  `p1161_alone.json`). The schematic and the 3D model draw the inner shell
  at its stored support [2, 4] from `wa_profiles.py`; no inner span is shown.
- **G-3 (Phase 314 profiles):** the member's (S, N, M) profiles are not
  stored as numeric arrays anywhere. They exist as the programme's stored
  evaluator code (`gate35/work/g35_rho.py`, on top of `phase258/work` and
  `phase274/work` libraries) plus the stored profile parameters
  (ramp m₀ = +4.00, rise [9, 20.5]) in `phase314/results/p314_results.json`.
  The figures evaluate that stored code — the same code Gate-35 used — so
  no profile was reconstructed by hand; but a reader should know the
  "stored data" for this member is code + parameters, not a data table.

## Inventoried, no figure in the first set (stored data exists)

- **Gate-12** — Le multipole shell confirmed at (0.7, 0.09); endowed shell
  spectrum gate-verified with correction. Stored: `gate12-claims/results/`
  (`g12_le_numbers.json`, `g12_endowed_numbers.json`, `g12_c_rescale.json`,
  `g12_check.json`). Candidate figure: pin/spectrum diagram.
- **Gate-34** — Phase 312 positive-density winner + Phase 313 six-mode Dirac
  supplier at its sites (σ_min = 0.0272). Stored: `gate34-claims/results/`
  (`g34_item1.json`, `g34_item2.json`, `g34_item2_scan.npz`, `g34_item3a/b/c.json`,
  `g34_c2_richardson.json`, `g34_controls.json`). Candidate figure:
  supplier site/singular-value diagram. (The member line itself is
  visualised via the Gate-35 figure and the 3D wall model.)
- **Gate-37** — the Décanini–Folacci identification (Phases 318 + 323): one
  printed number wrong at the Ellis throat (print 80/3 vs derived 16);
  A-throat evaluation (9/4, 3/4, 21/4) exact. Stored:
  `gate37-claims/results/g37_arithmetic.json`, `g37_results.json`;
  `gate37-claims/sources/` (`p318_derived_H633.json`, `p318_derived_H634.json`,
  `p323_exact_jets.json`, `p318_final_read.json`). Candidate figure:
  residual-collapse (203 → 187 → 0) diagram.
