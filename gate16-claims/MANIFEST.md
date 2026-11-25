# Gate-16 claims bundle - MANIFEST (release v1.16.0, revised 2026-11-23)

Every file in this folder, its size in bytes, and where it came
from. Copies are byte-for-byte copies of the named source
(md5-verified; every copy also cmp-verified against its source
at revision: 48/48 identical). This manifest lists every file in
the bundle except itself.

**Revision (2026-11-23, pre-publication):** this bundle was
originally assembled with two Gate-16 claims. Gate-19 then
re-judged both claims under a corrected instrument tensor:
G16-1 SURVIVES IN RESTATED WORDING and is the bundle's only
claim; G16-2 FAILS and was withdrawn before publication. The
full revision record is `REVISION_2026-11-23.md`. Rows marked
† are new or refreshed at the revision; rows marked ‡ are
Gate-16's original records, retained as history — their
legality coordinates are superseded by Gate-19's corrected
re-read (see the fencing note after the table).

| file | bytes | source / traceability |
|---|---|---|
| GATE16.md | 17877 | gate16/GATE16.md (gate record, verbatim copy — † refreshed at revision: the source now ends with Gate-19's dated correction note; the originally bundled copy is a strict byte-prefix of this file) md5 90eb0ad95628265f42570434242592c4 |
| GATE19.md † | 19336 | gate19/GATE19.md (the re-judgement of record: defect proof, fix, corpus re-audit, verdicts, verbatim copy) md5 85755fb4a3b03380be05643b5bb81f1d |
| RESULTS.md | 5497 | written for this bundle, rewritten at revision (the single claim G16-1 in its Gate-19-restated wording, verbatim, plus the G16-2 withdrawal note) |
| RELEASE_v1.16.0.md | 5648 | written for this bundle, rewritten at revision (release draft with the dated Gate-19 revision note; version DOI TBD — minted at release) |
| README_WHATSNEW_v1160.md | 3268 | written for this bundle, rewritten at revision (prepared README update; applied at upload) |
| REVISION_2026-11-23.md † | 6132 | written for this bundle at revision (the revision record: what changed and the verification results) |
| code/g16_audit.py | 11828 | gate16/work_a/g16_audit.py (gate auditor code, verbatim copy; byte-identical to the copy Gate-19 re-ran) md5 c799c02e665ead1b3c564a79eebb8234 |
| code/g16_run.py | 6174 | gate16/work_a/g16_run.py (gate driver code, verbatim copy; Gate-19's copy differs only in the output path) md5 fa15395728803932ba7ecea46008a800 |
| code/g16_check.py | 9394 | gate16/g16_check.py (gate checker code, verbatim copy) md5 f3afac74595e0576000817f97ecd9a08 |
| code/g19_repro.py † | 5429 | gate19/work/g19_repro.py (Gate-19's independent defect-reproduction code, verbatim copy) md5 516df0667e7ae5f86967500ba1ceb654 |
| results/g19_g16_results.json † | 23003 | gate19/results/g19_g16_results.json (Gate-19's corrected re-read on Gate-16's own machinery — the bundle's source of truth for every deciding number, verbatim copy) md5 b6bb512dc027441e3c923b1feeca1d99 |
| results/g19_repro_pre.json † | 537 | gate19/results/g19_repro_pre.json (defect reproduction, pre-fix output, verbatim copy) md5 99de4b74250a731957e72aa6a28f799b |
| results/g19_repro_post.json † | 541 | gate19/results/g19_repro_post.json (defect reproduction, post-fix regression output, verbatim copy) md5 7b56258186ff38b6966b7c6d0ec2991d |
| results/wa_results.json ‡ | 23026 | gate16/results/wa_results.json (Gate-16's original run output, verbatim copy — historical: its legality coordinates are superseded by results/g19_g16_results.json; its EoM coordinates are bit-identical and stand) md5 b2f24c1f3fdb6180763447d00f69ca19 |
| results/g16_check_output.json ‡ | 6268 | gate16/results/g16_check_output.json (Gate-16's checker output against its original wordings, verbatim copy — historical record) md5 80962e4261c3efd0c821ef9a0bafb6c7 |
| results/g16_search_log.md | 3480 | gate16/results/g16_search_log.md (novelty search log, verbatim copy) md5 4a82cfb9d01dd3006fd03656c02dcbcf |
| sources/CHECKPOINT128.md | 55417 | phase128/CHECKPOINT128.md (phase record (P128-1/P128-2), verbatim copy — † refreshed at revision: the source now ends with Gate-19's dated correction note; the originally bundled copy is a strict byte-prefix of this file) md5 2974fb8db25ba1139ac11ace1d9f48c0 |
| sources/CHECKPOINT119.md | 56406 | phase119/CHECKPOINT119.md (phase record (the two escapes characterised, P119-4), verbatim copy) md5 fdbe25353d5db7a5f3bbcbe9da73e524 |
| sources/CHECKPOINT108.md | 39408 | phase108/CHECKPOINT108.md (phase record (the front’s definitions and the alignment-set law, P108-3), verbatim copy) md5 40b01987ba86a527e5b0a8b579484a63 |
| sources/CHECKPOINT101.md | 43304 | phase101/CHECKPOINT101.md (lineage phase record (the hinge theory, P101-5), verbatim copy) md5 40a06ec5901ba988e5debde3cac1a407 |
| sources/p1281_memo.md | 11760 | phase128/results/p1281_memo.md (phase worker memo, verbatim copy) md5 5df1317d95084084d678239c455c0716 |
| sources/p1281_results.json | 105680 | phase128/results/p1281_results.json (phase results (the gate’s comparison target for G16-1), verbatim copy — ‡ its stored legality read is superseded on that coordinate by Gate-19's corrected re-read; its EoM reads stand) md5 1aa12d7c437776606dc4ab81b3c06fa9 |
| sources/p1281_run_record.md | 11433 | phase128/results/p1281_run_record.md (phase run record, verbatim copy) md5 ded0f763db014bad4421ea5fe187f691 |
| sources/p1281_gate.py | 3127 | phase128/work/p1281_gate.py (phase gate code, verbatim copy) md5 8df2423877b094f00d9125ea4dfcf8fe |
| sources/p1281_search.py | 10638 | phase128/work/p1281_search.py (phase search code, verbatim copy) md5 bd0f838a3fbb203acec2be239107b016 |
| sources/p1281_assemble.py | 4939 | phase128/work/p1281_assemble.py (phase assembly code, verbatim copy) md5 5c7df5e6bc316b1325a331399a8fea4f |
| sources/p1281_checker.py | 12299 | phase128/work/p1281_checker.py (phase checker code, verbatim copy) md5 100eb070fdf7865492bc4872d25a651c |
| sources/p1281_checker_output.json | 29186 | phase128/work/p1281_checker_output.json (phase checker output, verbatim copy) md5 ef30d8cffdc40da7f9151f804272c2ed |
| sources/p1194_memo.md | 10584 | phase119/results/p1194_memo.md (phase worker memo, verbatim copy) md5 e76c96626fa3f36f05bba9ee5ee28dc0 |
| sources/p1194_results.json | 34545 | phase119/results/p1194_results.json (phase results (the two escapes, both halves), verbatim copy) md5 05976d947a6910e960936bd7e0b309b7 |
| sources/p1194_run_record.md | 7740 | phase119/results/p1194_run_record.md (phase run record, verbatim copy) md5 f4aae7a208191aa26ac7c3fd8d0a14c7 |
| sources/p1194_lib.py | 8063 | phase119/work/p1194_lib.py (phase library code, verbatim copy) md5 a69c1eec67c873175d5ac4d8992752d9 |
| sources/p1194_gate.py | 2515 | phase119/work/p1194_gate.py (phase gate code, verbatim copy) md5 d35aae1792a3a3af678a3b336722d539 |
| sources/p1194_gate.json | 1644 | phase119/work/p1194_gate.json (phase gate record, verbatim copy) md5 05b179f99eb612e8bf87c2e46616bd64 |
| sources/p1194_halfA.py | 4419 | phase119/work/p1194_halfA.py (phase code (escape half A: the non-flat profile), verbatim copy) md5 65ede0dfb7bf7741ef6a86e9f9f373a1 |
| sources/p1194_halfB.py | 6458 | phase119/work/p1194_halfB.py (phase code (escape half B: H_,φ(π0) = 0), verbatim copy) md5 c89633cec33027eb33243409a6f98696 |
| sources/p1194_assemble.py | 4335 | phase119/work/p1194_assemble.py (phase assembly code, verbatim copy) md5 a6157b4a9ce78b5b9c702d1b227df0bd |
| sources/p1194_checker.py | 12260 | phase119/work/p1194_checker.py (phase checker code, verbatim copy) md5 9734792730d1b5de6aadebdb5209bd68 |
| sources/p1194_checker_output.json | 28174 | phase119/work/p1194_checker_output.json (phase checker output, verbatim copy) md5 f65aa7f5cad12ebe2151f943baabd243 |
| sources/p1194_patch_ties.py | 1433 | phase119/work/p1194_patch_ties.py (phase code, verbatim copy) md5 0219ba68073b1981e007306d1982df06 |
| sources/p1083_memo.md | 6412 | phase108/results/p1083_memo.md (phase worker memo, verbatim copy) md5 53fe0b96dc25f0aee8c10d4136a74b10 |
| sources/p1083_results.json | 29370 | phase108/results/p1083_results.json (phase results (the alignment-set law), verbatim copy) md5 af5a8996f3a1bd17311ac560640c0829 |
| sources/p1083_run_record.md | 8181 | phase108/results/p1083_run_record.md (phase run record, verbatim copy) md5 485148ac374e67258018230c3131fbe3 |
| sources/p1083_main.py | 8897 | phase108/work/p1083_main.py (phase code, verbatim copy) md5 d2834df884c952894b714af2dbe9fd9b |
| sources/p1083_checker.py | 5831 | phase108/work/p1083_checker.py (phase checker code, verbatim copy) md5 f30f03b3aeae4aa8c4d7f2b18391617a |
| sources/p1015_partB_raw.json | 13524 | phase101/results/p1015_partB_raw.json (phase results (the machinery-gate corpus; the hinge best is P101-5 Part B family B — a direct input of the gate’s run), verbatim copy) md5 94b375b68b50e6dc9698afc928e14459 |
| sources/p1015_memo.md | 17979 | phase101/results/p1015_memo.md (phase worker memo, verbatim copy) md5 9e5e5b61f6db89e436d4ce684f3abe66 |
| sources/p1015_results.json | 18535 | phase101/results/p1015_results.json (phase results, verbatim copy) md5 587160688559c6c29302e239e1f5e348 |
| sources/p761_lib.py | 16103 | phase76/p761_lib.py (datum machinery (the bed definition: Wall, H(φ), fluid stress-energy, margins) imported by the gate’s auditor, verbatim copy — † SUBSTITUTED at revision: the copy bundled at original assembly was the pre-fix library (14164 bytes, md5 2b43084dc5f2e96d02265d31c58d5385); this copy is the current source, carrying Gate-19’s `fluid_T` fix (Aᵀ·That·A) and its dated note, so the bundled machinery matches the corrected numbers) md5 4dc71194a14265f88a2dfcd123b2b7b6 |
| sources/p182_engine.py | 12098 | phase18/p182_engine.py (datum machinery (Lagrangian basis engine) imported by the gate’s auditor, verbatim copy) md5 d7526e4df1f76202f65bea75415adfe0 |
| sources/p182_basis.py | 13458 | phase18/p182_basis.py (datum machinery (profile splines, stencil) imported by the gate’s auditor, verbatim copy) md5 30a2c1b5068784d876541bce1493be0a |
| sources/p761_B_1.1.json | 34873 | phase76/results/p761_B_1.1.json (bed data at β = 1.1 read by the gate’s auditor, verbatim copy) md5 0151131d2e6732e61f6b67bb60041acc |

**Fencing note (superseded numbers in retained records).** The
verbatim records in this bundle were written before Gate-19 and
some carry the pre-correction legality figures (hinge
0.5892857142857143; P128-1 best 0.9285714285714286 /
0.9464285714285714; P128-2 best 0.7857142857142857). Those
figures are superseded as a class: every legality number
computed from E_total with a fluid posed encodes the defective
tensor (GATE19.md §6). `GATE16.md` and
`sources/CHECKPOINT128.md` carry Gate-19's own appended
correction notes on their faces; `results/wa_results.json`,
`results/g16_check_output.json`, `sources/p1281_results.json`
and the remaining phase records are fenced by this note and by
`REVISION_2026-11-23.md`. Their EoM coordinates are unaffected
and stand. The bundle's deciding numbers are Gate-19's
corrected re-reads, in `results/g19_g16_results.json`.

## Numbers check (every deciding number in the restated G16-1 wording, plus the figures the G16-2 withdrawal rests on, re-derived from the bundled corrected results)

Source of truth for this section: `results/g19_g16_results.json`
in this bundle (Gate-19's corrected re-read; byte-identical to
`gate19/results/g19_g16_results.json`, md5 above). Values below
were re-derived from that bundled file at revision — packaging
copies, hashes, and transcribes only; no bundled code was
executed.

- **Machinery gate (unchanged by the correction):** all 7
  stored corpus configurations reproduced (every row `pass_`
  true in the bundled `machinery_gate` record); worst error
  8.54938342342848e-12, inside the 1e-6 bar; hinge S_F = 1.0
  exactly; hinge alignment set {44}.
- **Hinge best, corrected (both sides of the comparison are
  Gate-19's re-reads on Gate-16's machinery):** subset_legal
  0.75 (fast) and 0.75 (full margins) — 42/56 points; EoM rel
  max 0.9999999999784565; median 0.22437629566157347; cr2_max
  1.000848801768969 → the wording's health fence (cr2 clause);
  alignment set {44}; worst point 44; t_kin at point 44 =
  1.9977096830799565e-58 → 2.0×10⁻⁵⁸ (the dead □φ channel);
  health False; Frontier A 0.0. (Stored pre-correction hinge
  legality 0.5892857142857143 is superseded — see the fencing
  note.)
- **G16-1 (P128-1 best), corrected:** subset_legal
  0.8928571428571429 (fast) and 0.8928571428571429 (full
  margins) — 50/56 points, i.e. both margin forms agree, as
  the restated wording carries them; Δlegal vs the corrected
  hinge = +0.1428571428571429; EoM rel max 0.999981215379503,
  i.e. Δ = −1.8784598953436316e-05 against the hinge → the
  wording's 1.9×10⁻⁵ move; median 0.47963896879690177
  (WORSENED, as the wording's fence states); cr2_max
  1.0009867195074533 → 1.00099; H_,φ(π₀) = 0.0 exactly
  (`Hphi_at_pi0` in the bundled record); t_FA at point 44 =
  2.3124581666039688e-06 → +2.31×10⁻⁶ (the posed zero holds);
  t_FB share at point 44 = 0.8818823902228511 → 0.882;
  alignment set empty; worst point 44; health False;
  Frontier A 0.0; both registered Pareto clauses TRUE
  (`comparisons/p1281_vs_hinge` in the bundled record).
- **G16-2 withdrawal basis (P128-2 best), corrected:**
  subset_legal 0.6071428571428571 (both margin forms) vs the
  corrected hinge 0.75 — Δlegal = −0.1428571428571429, and
  both registered Pareto clauses FALSE
  (`comparisons/p1282_vs_hinge`); the targeted candidate's
  corrected subset_legal is 0.42857142857142855. These are
  the figures RESULTS.md's withdrawal note and the release
  note carry; no G16-2 wording is carried anywhere in this
  bundle.
- **Defect proof (Gate-19's reproduction, bundled):**
  pre-fix synthetic max miss 0.7368628163383721 vs the
  correct form's 3.3306690738754696e-16; degenerate-plane
  rotation move 0.13975220335342817 (coded) vs
  1.1102230246251565e-16 (correct); P128-2 bed max diff
  0.11439922600789168 pre-fix → 5.551115123125783e-17
  post-fix (`results/g19_repro_pre.json` /
  `results/g19_repro_post.json`).

**Total: 35 deciding numbers re-derived from the bundled
corrected results, 0 unmatched.** (The only non-numeric string
carried without a numbers check is the concept DOI
10.5281/zenodo.24425078, whitelisted as in v1.15.0. The arXiv
identifiers in GATE16.md §6 are literature citations in the
novelty audit, not claim numbers.)

## Assembly notes

- **Selection, stated:** from phase128/, the P128-1 records
  and their deciding machinery (plus CHECKPOINT128.md); the
  search/checker logs and the run checkpoint files
  (p1281_ckpt.jsonl) were not copied — the claim rests on
  P128-1. From phase119/, only the P119-4 records (plus
  CHECKPOINT119.md); p1194_coord_rerun.log (a coordination
  log) and p1194_writefile.pl (a file-writing utility) were
  not copied, and neither were the P119-1/2/3/5 records — the
  claim rests on P119-4's two escapes. From phase108/, only
  the P108-3 records (plus CHECKPOINT108.md) — the front's
  definitions and the alignment-set law. From phase101/, the
  P101-5 Part B raw corpus with its memo and results (plus
  CHECKPOINT101.md): GATE16.md §§1/3 name
  `phase101/results/p1015_partB_raw.json` as a direct input
  of the gate's run (the machinery-gate corpus; the hinge
  best is P101-5 Part B family B), so it is bundled; Part A,
  the anatomy and checkpoint files were not copied.
  `__pycache__` is excluded everywhere, including
  gate16/work_a/__pycache__.
- **Removed at revision (G16-2's bundled evidence):** the
  twelve P128-2 source files bundled at original assembly —
  sources/p1282_memo.md, p1282_results.json,
  p1282_run_record.md, p1282_lib.py, p1282_gate.py,
  p1282_gate.json, p1282_search.py, p1282_assemble.py,
  p1282_checker.py, p1282_checker_output.json,
  p1282_seeds.py, p1282_seeds.json — were removed. The
  withdrawn claim's anatomy is preserved in the phase
  record (phase128/ in the programme tree) and in
  Gate-19's bundled re-read
  (`results/g19_g16_results.json`, which retains the
  P128-2 configurations' corrected reads), not in this
  release's claim files.
- **Datum scope, stated exactly:** the gate's auditor
  imports exactly three programme datum modules —
  phase76/p761_lib.py, phase18/p182_engine.py and
  phase18/p182_basis.py — and those three are bundled in
  `sources/`, together with the bed data file the
  auditor reads (phase76/results/p761_B_1.1.json).
  p761_lib.py itself references further pre-claim datum
  modules (p152_lib, p481_lib, verify_metric, p182_run);
  they are NOT bundled — the gate's deciding machinery
  is implemented in-file in `code/g16_audit.py`, and the
  three bundled modules are exactly the datum layer
  GATE16.md §1 names. Gate-19's re-read ran copies of
  `code/g16_audit.py` (byte-identical) and `code/g16_run.py`
  (output path redirected to gate19/results/) against the
  fixed p761_lib.py bundled here.
- No source file was edited; no bundled .py was executed
  and nothing was unpickled at any point in packaging or
  revision.
