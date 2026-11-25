# Gate-20 claims bundle - MANIFEST (release v1.20.0)

Every file in this folder, its size in bytes, and where it came from.
Copies are byte-for-byte copies of the named source (md5-verified at
assembly; every copy also cmp-verified against its source at assembly).
This manifest lists every file in the bundle except itself.

| file | bytes | source / traceability |
|---|---|---|
| GATE20.md | 12442 | gate20/GATE20.md (gate record, verbatim copy) md5 a36e83f716a92d8678444da421d49901 |
| RESULTS.md | 2192 | written for this bundle (G20-1 in Gate-20's exact quotable form, verbatim) |
| RELEASE_v1.20.0.md | 2410 | written for this bundle (release draft; version DOI TBD — minted at release) |
| README_WHATSNEW_v1200.md | 1133 | written for this bundle (prepared README update; applied at upload) |
| code/g20_verify.py | 8520 | gate20/work/g20_verify.py (gate verifier code, verbatim copy) md5 324e12942a9df92e6842073f8d1ca429 |
| results/g20_verify_out.json | 3968 | gate20/work/g20_verify_out.json (gate verifier output, verbatim copy) md5 f7b696a298ae674db2b55eec9a6ec76b |
| sources/CHECKPOINT178.md | 25676 | phase178/CHECKPOINT178.md (phase record, verbatim copy) md5 1a36b9be6cbdbf80854fa0ffcdaf7816 |
| sources/p1781_checker_output.txt | 1255 | phase178/results/p1781_checker_output.txt (phase checker output, verbatim copy) md5 2fee438917f1ba6365a966d10a43ddb5 |
| sources/p1781_memo.md | 6876 | phase178/results/p1781_memo.md (phase worker memo, verbatim copy) md5 5df75b6d17963b745f0167e3f7e8354e |
| sources/p1781_results.json | 6759 | phase178/results/p1781_results.json (phase numbers, verbatim copy) md5 897544a84dc89f2803069c5720317f99 |
| sources/p1781_run_record.md | 4319 | phase178/results/p1781_run_record.md (phase run record, verbatim copy) md5 d0a899d7332f1ff28e98285a22779f85 |
| sources/p1781_state.npz | 3316 | phase178/work/p1781_state.npz (the exhibited witness field (bit-identical state), verbatim copy) md5 ca8fd295d3e5d1bfda96943cebe9aabf |
| sources/t9_check.json | 4044 | phase97/results/t9_check.json (phase checker output, verbatim copy) md5 4e3f51177e441894d75a4811794083f3 |
| sources/t9_memo.md | 15996 | phase97/results/t9_memo.md (phase memo, verbatim copy) md5 a98b70c4c7e73c660d19e10a41b93983 |
| sources/t9_results.json | 40975 | phase97/results/t9_results.json (digit-identical cross-check record, verbatim copy) md5 40562ec2fabbf6de709073d008a024fa |

## Numbers check (every deciding number in Gate-20's quotable form, re-derived from the bundled results)

Source of truth for this section: `results/g20_verify_out.json` in this
bundle (the gate's own verifier output; byte-identical to
`gate20/work/g20_verify_out.json`, md5 above) together with
`sources/p1781_results.json`. Values below were transcribed from those
files during packaging — packaging copies, hashes, and transcribes
only; no bundled code was executed.

- **Coupled closure 0.6232117059867903** — present verbatim in
  `results/g20_verify_out.json` and in `sources/p1781_results.json`
  (the phase value the gate re-passed at reldiff 0.0).
- **Δq first component −4.992×10⁻⁶** — stored in
  `results/g20_verify_out.json` / `sources/p1781_results.json` in
  float form (−4.992…e-06); **Δq second component −1.321×10⁻⁴** —
  stored in `sources/p1781_checker_output.txt` (−1.321…e-04 class).
- **Subset count 52; Type-I [False, False]** — recorded in
  `results/g20_verify_out.json`.
- **Witness norm ‖d‖₂ = 0.18088** — as printed in GATE20.md; the
  witness state itself is bundled (`sources/p1781_state.npz`,
  bit-identical) and is digit-identical to Phase 97's record
  (`sources/t9_results.json`).

Checked: every deciding number in the quotable form — 0 unmatched.

## Assembly notes

- **Selection, stated:** from gate20/, the gate record and its
  verifier with output. From phase178/, CHECKPOINT178.md and the
  P178-1 records the claim rests on (memo, results, run record,
  checker output) plus the exhibited witness state
  (`work/p1781_state.npz`). From phase97/, the t9 record set the
  gate used as its digit-identical cross-check (results, memo,
  checker output). The P178-2 records are not bundled — no claim
  in this release rests on them.
- No source file was edited; no bundled .py was executed and
  nothing was unpickled at any point in packaging.
