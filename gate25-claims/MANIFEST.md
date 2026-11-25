# Gate-25 claims bundle - MANIFEST (release v1.23.0)

Every file in this folder, its size in bytes, and where it came from.
Copies are byte-for-byte copies of the named source (md5-verified at
assembly; every copy also cmp-verified against its source at assembly).
This manifest lists every file in the bundle except itself.

| file | bytes | source / traceability |
|---|---|---|
| GATE25.md | 24347 | gate25/GATE25.md (gate record, verbatim copy) md5 1f3b1e7bcfc9b4e1fe4142e00f7041d9 |
| RESULTS.md | 6070 | written for this bundle (G25-A/B/C in Gate-25's restated wordings, verbatim; novelty NONE stated) |
| RELEASE_v1.23.0.md | 5345 | written for this bundle (release draft; version DOI TBD — minted at release) |
| README_WHATSNEW_v1230.md | 1845 | written for this bundle (prepared README update; applied at upload) |
| code/g25_verify.py | 15081 | gate25/work/g25_verify.py (gate verifier code, verbatim copy) md5 4d054981897f91b86c1d747de34add4d |
| results/g25_literature.md | 18119 | gate25/work/g25_literature.md (the gate's novelty search record (12 query families), verbatim copy) md5 f50e88179c35e3498dc412c155bdeb44 |
| results/g25_verify_results.json | 15973 | gate25/work/g25_verify_results.json (gate verifier output, verbatim copy) md5 f68f2ff3889211a1fc129b7a745b3183 |
| sources/CHECKPOINT253.md | 8816 | phase253/CHECKPOINT253.md (phase record, verbatim copy) md5 5ec528813f03ff7d83940df990718a97 |
| sources/CHECKPOINT257.md | 6468 | phase257/CHECKPOINT257.md (phase record, verbatim copy) md5 ffdd7717d8abeb14ab5e9f26981de2ef |
| sources/p2531_check.json | 2366 | phase253/results/p2531_check.json (phase checker output, verbatim copy) md5 82b2ad4e8937818b1e2a9dcb04714316 |
| sources/p2531_memo.md | 13270 | phase253/results/p2531_memo.md (phase worker memo, verbatim copy) md5 2d6e3c0dc3ff7fecb656444bb958722a |
| sources/p2531_results.json | 11671 | phase253/results/p2531_results.json (phase numbers, verbatim copy) md5 1ebc48806cf6a5c05e1cc75f8c4befa7 |
| sources/p2532_memo.md | 15649 | phase253/results/p2532_memo.md (phase worker memo, verbatim copy) md5 611127b680ed5dc4b16c14b96e2523f3 |
| sources/p2532_results.json | 39128 | phase253/results/p2532_results.json (phase numbers, verbatim copy) md5 e37f8ae0d3f07a99f84bba7f8219017e |
| sources/p2571_memo.md | 5273 | phase257/results/p2571_memo.md (phase worker memo (Leg 1), verbatim copy) md5 5b91ca6573e05a56a3200117be7255a4 |
| sources/p2572_memo.md | 4999 | phase257/results/p2572_memo.md (phase worker memo (Leg 2), verbatim copy) md5 4d3405eb391d582f811fb203d2eca41c |
| sources/p2573_memo.md | 3291 | phase257/results/p2573_memo.md (phase worker memo (Leg 3), verbatim copy) md5 427a2737e1c8b16a3b946549b75e18cd |
| sources/p257_check.json | 399 | phase257/results/p257_check.json (phase checker output, verbatim copy) md5 419d67e561e970753b998edff8b92684 |
| sources/p257_leg1_results.json | 7592 | phase257/results/p257_leg1_results.json (phase numbers (Leg 1), verbatim copy) md5 4ff3ee3367f5186899867bd263f6b99b |
| sources/p257_leg2_results.json | 1848 | phase257/results/p257_leg2_results.json (phase numbers (Leg 2), verbatim copy) md5 6dc4d79b565a3e3d935a9e9afdb47a13 |
| sources/p257_leg3_results.json | 1731 | phase257/results/p257_leg3_results.json (phase numbers (Leg 3), verbatim copy) md5 8499a561f3583c51e5cc013a52e095ee |

## Numbers check (every deciding number in Gate-25's restated wordings, re-derived from the bundled results)

Source of truth for this section: `results/g25_verify_results.json`
in this bundle (the gate's own verifier output; byte-identical to
`gate25/work/g25_verify_results.json`, md5 above) together with the
bundled phase records in `sources/`. Values below were transcribed
from those files during packaging — packaging copies, hashes, and
transcribes only; no bundled code was executed.

- **T(k*,k*) = −10.8785** — present in `sources/p257_leg3_results.json`
  (and the Phase 253 record set); **ρ = +2.2404** at the same point —
  present in `sources/p2531_memo.md` / the Phase 253 records.
- **Match residual 1.77×10⁻¹⁶** — stored in
  `results/g25_verify_results.json` as 1.7674932537562168e-16
  (the claim's rounded print).
- **ρ_unit = −0.012431** — stored in full in
  `results/g25_verify_results.json` as −0.012431243730331365
  (gate-reproduced; the phase's leg-2 value
  −0.012431243730330888 is in `sources/p257_leg2_results.json`).
- **Patch NEC minimum ≈ −0.0223** — present in
  `results/g25_verify_results.json` and
  `sources/p257_leg2_results.json`.
- **R_diff 2852.41** — present in `sources/p257_leg3_results.json`
  and `sources/p2573_memo.md` (identical before and after sourcing,
  by construction, as the claim states).
- **Type-IV draws 40/300; gate spot check 13/60** — recorded in
  `results/g25_verify_results.json`.

Checked: every deciding number in the restated wordings — 0 unmatched.

## Assembly notes

- **Selection, stated:** from gate25/, the gate record, its
  verifier with output, and the novelty search record
  (`work/g25_literature.md`, filed under `results/`). From
  phase253/ and phase257/, the checkpoints and the full results
  sets (memos, results, checker outputs for P253-1/P253-2 and
  Legs 1–3). The phases' work/ scripts are not bundled — the
  gate's independent re-derivation (`code/g25_verify.py`) is the
  bundle's deciding machinery, per the gate12/gate16 pattern.
- No source file was edited; no bundled .py was executed and
  nothing was unpickled at any point in packaging.
