# Gate-21 claims bundle - MANIFEST (release v1.21.0)

Every file in this folder, its size in bytes, and where it came from.
Copies are byte-for-byte copies of the named source (md5-verified at
assembly; every copy also cmp-verified against its source at assembly).
This manifest lists every file in the bundle except itself.

| file | bytes | source / traceability |
|---|---|---|
| GATE21.md | 17481 | gate21/GATE21.md (gate record, verbatim copy) md5 c5c186745a7e62d1ec1512b11b8d4d87 |
| RESULTS.md | 3653 | written for this bundle (G21-1 restated and G21-2 intact, in Gate-21's exact quotable forms, verbatim) |
| RELEASE_v1.21.0.md | 3730 | written for this bundle (release draft; version DOI TBD — minted at release) |
| README_WHATSNEW_v1210.md | 1377 | written for this bundle (prepared README update; applied at upload) |
| code/g21_verify.py | 5799 | gate21/work/g21_verify.py (gate verifier code, verbatim copy) md5 6c70475c8c8246448c197ab479a6a450 |
| code/g21_verify2.py | 2943 | gate21/work/g21_verify2.py (gate verifier code (second pass), verbatim copy) md5 79daf0c25585cb0729fecb4157939a26 |
| results/g21_verify2_out.json | 2497 | gate21/work/g21_verify2_out.json (gate verifier output (second pass), verbatim copy) md5 05ae7f66e3e535c23ebeaa4d8a10dda0 |
| results/g21_verify_out.json | 8215 | gate21/work/g21_verify_out.json (gate verifier output, verbatim copy) md5 46cdc184da4cd34e9f537ac5df8cacb6 |
| sources/CHECKPOINT178.md | 25676 | phase178/CHECKPOINT178.md (phase record, verbatim copy) md5 1a36b9be6cbdbf80854fa0ffcdaf7816 |
| sources/CHECKPOINT186.md | 23118 | phase186/CHECKPOINT186.md (phase record, verbatim copy) md5 bc12a45438dcb99976a2877aba242edf |
| sources/p1781_results.json | 6759 | phase178/results/p1781_results.json (the lambda_val witness record, verbatim copy) md5 897544a84dc89f2803069c5720317f99 |
| sources/p1781_stage3_opt.py | 9262 | phase178/work/p1781_stage3_opt.py (the registered script the witness search ran (provenance-diffed by the gate), verbatim copy) md5 3b09c015df7e092fdee2a77eaf793011 |
| sources/p186_J_lam010.json | 2158 | phase186/results/p186_J_lam010.json (coupled Jacobian record at lambda = 0.10, verbatim copy) md5 382a11ec7555fc02cd9b972e1754aca9 |
| sources/p186_checker_output.json | 1077 | phase186/results/p186_checker_output.json (phase checker output, verbatim copy) md5 9a8b3308af2f785ad298527368ab9472 |
| sources/p186_grad_lam010.json | 358 | phase186/results/p186_grad_lam010.json (gradient record at lambda = 0.10, verbatim copy) md5 3e31ad4996de06e90d0d1df1b4896a3c |
| sources/p186_opt_lam010.json | 6382 | phase186/results/p186_opt_lam010.json (the lambda = 0.10 optimisation record, verbatim copy) md5 194000161b3d865fca71655fe42ae813 |
| sources/p186_opt_lam010_run_record.md | 4027 | phase186/results/p186_opt_lam010_run_record.md (phase run record, verbatim copy) md5 9a1fddab176a9d3ac54e643f98bd1c70 |
| sources/p186_opt_lam010_state.npz | 3316 | phase186/work/p186_opt_lam010_state.npz (the lambda = 0.10 witness field (stored state), verbatim copy) md5 7dc4fa8a5e33522ccdb2163462d1c010 |
| sources/p186_stage01.json | 4592 | phase186/results/p186_stage01.json (phase stage record, verbatim copy) md5 aabc7c7c08d050fa29ae95dfcdd7ee21 |

## Numbers check (every deciding number in Gate-21's quotable forms, re-derived from the bundled results)

Source of truth for this section: `results/g21_verify_out.json` and
`results/g21_verify2_out.json` in this bundle (the gate's own
verifier outputs; byte-identical to the gate21/work
originals, md5s above) together with
`sources/p186_opt_lam010.json`. Values below were transcribed from
those files during packaging — packaging copies, hashes, and
transcribes only; no bundled code was executed.

- **Coupled closure 0.6233418793559693** — present verbatim in
  `results/g21_verify_out.json` and `sources/p186_opt_lam010.json`.
- **Δq = (+2.892×10⁻⁵, +2.304×10⁻⁴)** — stored in float form in
  `results/g21_verify_out.json`: 2.892…e-05 and
  0.00023035807094939909 (the claim's rounded print).
- **‖d‖₂ = 4.407427; max field value 0.042537; subset count 52;
  Type-I [False, False]** — present in `results/g21_verify_out.json`
  and `sources/p186_opt_lam010.json`.
- **The λ = 0.1452 failure reads (Type-I [False, True] at site 44;
  count 53 ≠ 52 at d = 0) and the tightened onset (0.10, 0.11]** —
  recorded in `results/g21_verify2_out.json`.

Checked: every deciding number in the quotable forms — 0 unmatched.

## Assembly notes

- **Selection, stated:** from gate21/, the gate record and both
  verifier passes with outputs. From phase186/, CHECKPOINT186.md,
  the λ = 0.10 optimisation record set (optimum, run record,
  checker output, stage record, Jacobian and gradient records)
  and the witness state (`work/p186_opt_lam010_state.npz`). From
  phase178/, CHECKPOINT178.md, the λ_val witness record and the
  registered script the gate provenance-diffed
  (`work/p1781_stage3_opt.py`). Other Phase 186 λ rows are not
  bundled — no claim in this release rests on them.
- No source file was edited; no bundled .py was executed and
  nothing was unpickled at any point in packaging.
