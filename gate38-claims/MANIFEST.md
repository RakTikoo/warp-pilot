# Gate-38 claims bundle - MANIFEST (release v1.29.0)

Every file in this folder, its size in bytes, and where it came from.
Copies are byte-for-byte copies of the named source (md5-verified at
assembly; every copy also cmp-verified against its source at assembly).
This manifest lists every file in the bundle except itself.

| file | bytes | source / traceability |
|---|---|---|
| GATE38.md | 21060 | gate38/GATE38.md (gate record, verbatim copy) md5 7ebb8e8a83ce2c1044decb4ce0a66728 |
| GATE38_ADDENDUM.md | 22484 | gate38/GATE38_ADDENDUM.md (gate addendum record — the governing text wherever it differs from GATE38.md, verbatim copy) md5 6dd8fb86bccedbf6a5197a41a42cd295 |
| RESULTS.md | 7409 | written for this bundle (the final claim set: the Gate-38 Addendum §2 block verbatim — the only quotable form of the identification claims; the §2 block in RESULTS.md was diff-verified character-for-character against GATE38_ADDENDUM.md §2 at assembly) |
| RELEASE_v1.29.0.md | 10666 | written for this bundle (release draft; the Addendum §3 correction note and the §2 claim set embedded verbatim, both diff-verified against GATE38_ADDENDUM.md at assembly; the disclosure paragraph in gate37-claims/RELEASE_v1.27.0.md's exact form, diff-verified at assembly; version DOI TBD — minted at release) |
| README_WHATSNEW_v1290.md | 2533 | written for this bundle (prepared README update; applied at upload) |
| code/p2411_driver_v2.py | 51823 | phase365/work/p2411_driver_v2.py (Phase 365's repaired Phase 241 driver — a full copy of the stored driver with exactly one functional change, the m39 slot fix; the stored original was never edited, verbatim copy) md5 4b0b1e71b0c88f7624e463a167dadb78 |
| code/p363_r2_c3.py | 3148 | phase363/work/p363_r2_c3.py (Phase 363's per-monomial confrontation script — driver monomial functions vs the certified exact library, group c3, in Phase 361 Arm B's programme order; the script that isolated m39/N40, verbatim copy) md5 ef58cb97640bedbf3496ba3754929d05 |
| code/p363_r2_c3_out.json | 11573 | phase363/work/p363_r2_c3_out.json (the confrontation script's output record — per-monomial driver vs exact values, verbatim copy) md5 fc3db6bc9f3018a02c1a03ae5b882159 |
| sources/CHECKPOINT355.md | 11698 | phase355/CHECKPOINT355.md (phase record (the verbatim Eq. (2.23) evaluation; control R2 failure), verbatim copy) md5 ece96bef25efe3d4a51e153143f4e61e |
| sources/p355_memo.md | 10268 | phase355/results/p355_memo.md (phase worker memo (no famous consumer; the identity result), verbatim copy) md5 98d920b4815adff5a8f4a1245519c5f7 |
| sources/CHECKPOINT361.md | 8213 | phase361/CHECKPOINT361.md (phase record (the localisation: NEITHER), verbatim copy) md5 826a249ce62e5d3f3805a3766fe14b39 |
| sources/p361_memo.md | 3012 | phase361/results/p361_memo.md (phase worker memo (Arms A and B), verbatim copy) md5 da742c5f0dc96efc264aacdbdf2ccbd8 |
| sources/CHECKPOINT363.md | 9982 | phase363/CHECKPOINT363.md (phase record (ORIGIN IN R2: the m39 localisation), verbatim copy) md5 6761c3d5112b2b6568f5380472c57ec1 |
| sources/p363_memo.md | 5678 | phase363/results/p363_memo.md (phase worker memo (R1/R2/R3 and consequences), verbatim copy) md5 3ca6776f04fbd6a4516f994312bac34d |
| sources/p363_results.json | 3528 | phase363/results/p363_results.json (Phase 363's results record — named on the Addendum's face as part of the record it verified, verbatim copy) md5 6586b56e2e50eb799c86ccca522dc518 |
| sources/CHECKPOINT365.md | 5707 | phase365/CHECKPOINT365.md (phase record (the repair and restatement), verbatim copy) md5 7dbc37a47fd5b054e9cef33ddc576a71 |
| sources/p365_memo.md | 10318 | phase365/results/p365_memo.md (phase worker memo (controls, corrected REST, restated residuals), verbatim copy) md5 2a9d52e1eb4664f8ba023faec87aa8aa |
| sources/p365_restatement.json | 70037 | phase365/results/p365_restatement.json (Phase 365's full restatement record — the 89 flagged cells, verbatim copy) md5 15c710e9eda5037802b187c02e672ed0 |
| sources/p365_m39_diff.txt | 1319 | phase365/work/p365_m39_diff.txt (the one-hunk diff between the stored Phase 241 driver and the repaired copy in code/ — m39 raises slot 2, verbatim copy) md5 fd1d069b70b0ed8ccde9dda44a318b46 |

## Numbers check (every deciding number in the final set, transcribed from the bundled records)

Sources of truth for this section: the bundled phase records in
`sources/` (`CHECKPOINT355.md`, `CHECKPOINT361.md`,
`CHECKPOINT363.md`, `CHECKPOINT365.md`, `p365_memo.md`,
`p365_restatement.json`). Values below were transcribed from those
files during packaging — packaging copies, hashes, and transcribes
only; no bundled code was executed and nothing was unpickled.

- **Print Eq. (2.23) is the derived tensor** — both arms read
  (80, 16, 112) at the Ellis throat; the registered control
  ΔH(throat) = (0, 0, 0), not (0, 32/3, 0); Δ = 0 on nine jets —
  `sources/CHECKPOINT355.md`, `sources/p355_memo.md` (Phase 355,
  control R2; re-confirmed Phase 361, CTL-1, in
  `sources/CHECKPOINT361.md`).
- **Print H(6,3)(3) is the derived tensor** — (32, 8, 44) at the
  throat; the registered single-carrier prediction (32, −1, 44)
  refuted; ΔH(6,3)(3) vanishes identically on six generic jets;
  DF's (3.14)→(3.15) expansion reproduces printed (3.15) exactly,
  term by term (59 monomials) — `sources/CHECKPOINT361.md`
  (Phase 361, Arms A and B).
- **The defective cell** — the Phase 241 driver's monomial
  function m39 (MONO position 38, group c3, ξ⁰ coefficient 2/315)
  reads the (3.15) monomial N40 at the Ellis throat as
  **(0, +4, 0)** where the verbatim monomial gives
  **(0, −8, 0)** (third factor's index raised from Riemann slot 0
  instead of slot 2); weighted, 210·(2/315)·12 = exactly +16 —
  `sources/CHECKPOINT363.md` (R2 localisation; from-scratch
  re-verification with explicit index gymnastics), and the
  per-monomial record in `code/p363_r2_c3_out.json`.
- **Stored vs true throat total** — stored ξ⁰ T^r_r total
  **1075/9**, faithful evaluation **931/9**; the other eleven
  cells (4 powers × 3 components) reproduce exactly —
  `sources/CHECKPOINT363.md`; re-derived by the repaired driver
  in `sources/p365_memo.md` (stored (8641/9, 1075/9, 10261/9) ξ⁰;
  repaired T^r_r = 931/9).
- **Corrected REST** — with the repaired total, REST =
  **(44/135, 68/945, 100/189) = REST_derived exactly in all three
  cells**; the shift from REST_print (44/135, 4/27, 100/189) is
  exactly **(0, −8/105, 0)**, the whole of it the m39 cell's
  throat contribution — `sources/CHECKPOINT365.md`,
  `sources/p365_memo.md` (control C-REST).
- **Gate coefficient** — under the derived assembly the Ellis
  gate polynomial's ξ⁰ coefficient is **187** exactly, the target
  value; Phase 365's restated readout lands on target:
  **187.00000000000006** (deviation 6×10⁻¹⁴, from a stored
  deviation of +16); the stored print-side coefficient 203 is
  withdrawn as a comparator (203 − 187 = exactly the corrupted
  +16) — `sources/p365_memo.md`.
- **FULL throat residual** — the stored +16.0 closes to
  **5.7×10⁻¹⁴** ((2.3×10⁻¹³, 5.7×10⁻¹⁴, 2.3×10⁻¹³)) under the
  corrected totals — `sources/p365_memo.md`,
  `sources/p365_restatement.json`.
- **A-throat residual** — (0, +2, −7) restates to
  (0, 2.1×10⁻¹⁴, −1.1×10⁻¹⁴), ~10⁻¹⁴ — `sources/p365_memo.md`.
- **Survivor, stated as such** — **E:1/10 (21.511111, 42.044444,
  21.511111)** is the widest-set FULL ξ⁰ maximum after the
  restatement. It is **NOT attributable to m39** (it survives the
  repair) and is **unattributed** — Phase 365 adjudicated no
  attribution for the survivors; they stand as the corrected
  record's residuals, in the territory of Phase 241's separate
  H(6,3)(5),(6),(8) result and the D2 generic-θ gap —
  `sources/p365_memo.md`, `sources/CHECKPOINT365.md`,
  `sources/p365_restatement.json` (Tt 21.511111111105492,
  Tr 42.04444444444175).

Checked: every deciding number in the final set — 0 unmatched.

## Assembly notes

- **Selection, stated:** the gate record and its addendum entire
  (the addendum governs wherever the two differ: its §2 is the
  final quotable set, superseding Gate-38 §5, and its §3 is the
  final correction note, replacing Gate-38 §6's draft in full —
  both bundled gate files are included so the supersession is
  auditable from the bundle). Gate-38 ran no computation and has
  no `work/` directory, so there are no gate code/results
  artefacts and this bundle has no `results/` folder: the
  deciding records are the phases'. From phase355/ and
  phase361/, the checkpoint and the memo each (the phases'
  verdict records). From phase363/, the checkpoint, the memo, and
  the results JSON the Addendum names on its face; plus, in
  `code/`, the phase's per-monomial confrontation script and its
  output — the single identifiable deciding artefacts that
  isolated m39. From phase365/, the checkpoint, the memo, the
  full restatement JSON, the one-hunk m39 diff (in `sources/`),
  and the repaired driver (in `code/`). **Not bundled:** the
  certified exact library Phase 363's confrontation ran against —
  it is a multi-file artefact (Phase 361's `p361_eval.py` over
  Phase 355's `p355_print_eval.py` machinery and the Phase 259
  engine), not a single file, and is identified by the imports on
  the bundled script's face; the phases' remaining work files,
  run logs and engine code (the gate judged the phases' records
  and results); the stored Phase 241 driver itself (never edited;
  its repair is fully specified by the bundled one-hunk diff and
  the bundled repaired copy); the `__pycache__` .pyc files under
  the phase work directories (compiled artefacts).
- The verbatim blocks embedded in the written files were
  diff-verified character-for-character at assembly: the
  Addendum §2 claim set in RESULTS.md and in
  RELEASE_v1.29.0.md, the Addendum §3 correction note in
  RELEASE_v1.29.0.md, and the disclosure paragraph against
  gate37-claims/RELEASE_v1.27.0.md — all four checks exact.
- No source file was edited; no bundled .py was executed and
  nothing was unpickled at any point in packaging.
