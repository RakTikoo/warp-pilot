# Gate-57 claims bundle - MANIFEST (release v1.48.0)

Every file in this folder, its size in bytes, and where it came from.
Copies are byte-for-byte copies of the named source (md5-verified at
assembly; every copy also cmp-verified against its source at assembly).
This manifest lists every file in the bundle except itself.

| file | bytes | source / traceability |
|---|---|---|
| GATE57.md | 15841 | gate57/GATE57_REPORT.md (gate record, verbatim copy of gate57/GATE57_REPORT.md) md5 e325c7efa01b6ac0ce7198ec71fedd42 |
| GATE57_CHECKPOINT.md | 2347 | gate57/GATE57_CHECKPOINT.md (gate checkpoint, verbatim copy) md5 a7a8e119e5366dbb3b02d86ce413dbe5 |
| README_WHATSNEW_v1480.md | 5511 | written for this bundle (prepared README update; applied at upload) |
| RELEASE_v1.48.0.md | 4951 | written for this bundle (release draft; the GATE57.md §8 quotable claim set (G57-A…G57-D, riders G57-R1…R4) embedded as a blockquote; version DOI TBD — minted at release) |
| RESULTS.md | 5760 | written for this bundle (the claim set: the GATE57.md §8 quotable claim set (G57-A…G57-D) and riders G57-R1…R4 verbatim — the only quotable form of the Phase 416 claim set) |
| code/g57_audit.py | 6567 | gate57/work/g57_audit.py (Gate-57's audit driver — the machinery control, the independent registered audits of B-4/B-3/B-5, the bracket reads, the q reads; verbatim copy) md5 888ff79429ba250fd4fe265857d092c3 |
| code/g57_dense.py | 6792 | gate57/work/g57_dense.py (Gate-57's dense-read driver — Phase 417's form applied to B-4; verbatim copy) md5 974fdc23aed50b1560c3b83cf9a21dc7 |
| code/g57_laptop.py | 1973 | gate57/work/g57_laptop.py (Gate-57's laptop-admission driver (corroboration); verbatim copy) md5 158b6f442a0b8337ff178d68292ae896 |
| code/g57_qdiag.py | 2666 | gate57/work/g57_qdiag.py (Gate-57's q diagnostic (the §3 anatomy; diagnostic only, no deciding read); verbatim copy) md5 e268eca2a147dc14a6276cce89405345 |
| code/g57_repro.py | 3345 | gate57/work/g57_repro.py (Gate-57's recomputation of claims (ii)–(iv) from the stored records; verbatim copy) md5 8733f84e3ac82ed548df53d7e94e5f49 |
| code/make_g57_figure.py | 3364 | gate57/work/make_g57_figure.py (written for this bundle (the figure generator — reads only the bundled records in sources/ plus the dose–response sequence as stated in rider G57-R4, and writes figures/g57_ladder.png)) md5 55c2b1b1b89edcf70edaba0c7086b4a2 |
| code/p416_check.py | 10358 | phase416/work/p416_check.py (Phase 416's checker — the coordinator-run home checker, re-run at the gate 31/31 PASS, verbatim copy) md5 c5a3ddf7ef1ce19ea77bacc8a1feab97 |
| code/p417_dense.py | 9233 | phase417/work/p417_dense.py (Phase 417's dense-read driver — the form Gate-57's dense read follows; verbatim copy) md5 81712f8c406fd96ac31c12dff49514b2 |
| code/p417_lib.py | 24155 | phase417/work/p417_lib.py (Phase 417's machinery — the panel-Lagrange graded-family builder and the registered summary/legality code; Gate-57's deciding-path geometry, verbatim copy) md5 d9ec74a14b3d910cfe3f353d55ee222e |
| figures/g57_ladder.png | 160402 | generated at assembly by code/make_g57_figure.py from the bundled records (the ladder's dose–response 0.1363 → 0.18671875 → 0.18984375 → 0.191796875 → 0.192578125 → 0.193359375 → 0.194140625 with increments; registered vs dense refined SEC margins for y_his, S1, E2-1, RW-5, A-6 (Phase 417) and B-4 (Gate-57: registered +5.804×10⁻⁷, dense +2.450×10⁻⁷, CONTINUUM-LEGAL); E2-1 and A-6 shown dipping below zero on densification) |
| sources/CHECKPOINT416.md | 38651 | phase416/CHECKPOINT416.md (Phase 416's phase record — registration, D-416-1 and the integrated closure, verbatim copy) md5 1b1d3745cff194a7e43ccb61eb966f8e |
| sources/CHECKPOINT417.md | 11538 | phase417/CHECKPOINT417.md (Phase 417's phase record — the dense-read form and the scope table B-4's row extends, verbatim copy) md5 41f92678cca46c077728ad13e2f6cc74 |
| sources/g57_audit.json | 12997 | gate57/results/g57_audit.json (Gate-57's independent registered audits — the A-6 machinery control, B-4/B-3/B-5 at 0.194140625 with q reads, the bracket reads at 0.196640625 and 0.195390625, verbatim copy) md5 8f115173f106a10d2f6bc6738f5c36b1 |
| sources/g57_chain.json | 484 | gate57/results/g57_chain.json (Gate-57's chain calibration for B-4 (gate vs phase-stored; max rel diff 4.6×10⁻¹¹), verbatim copy) md5 98a623cd734cb02e79b791b5f869a965 |
| sources/g57_dense.json | 23121 | gate57/results/g57_dense.json (Gate-57's dense read on B-4 — CONTINUUM-LEGAL, refined SEC +2.450385×10⁻⁷ @ 3.52, Richardson +2.450087×10⁻⁷, verbatim copy) md5 3c972bfaef64a6cf913bb817509c2f6c |
| sources/g57_laptop_out.json | 1922 | gate57/results/g57_laptop_out.json (Gate-57's laptop-admission record — admitted as corroboration (chain reads bit-identical; registered worst SEC agreeing to 1.1×10⁻²²), verbatim copy) md5 bd0eee4ed9bb11e9493df2cb8afd79ff |
| sources/g57_qdiag.json | 29765 | gate57/results/g57_qdiag.json (Gate-57's q diagnostic record (GATE57.md §3), verbatim copy) md5 e742051aad533fa42bf57cc9c90034a5 |
| sources/g57_repro.json | 1596 | gate57/results/g57_repro.json (Gate-57's recomputation of claims (ii)–(iv), verbatim copy) md5 731eae218a5685f675894d0c08223b72 |
| sources/p416_controls.json | 67892 | phase416/results/p416_controls.json (Phase 416's home controls record (incl. the C-416-3 FD floor 5.295791×10⁻⁹), verbatim copy) md5 7898c171f896b8c8c90b3a68ebccff33 |
| sources/p416_memo.md | 5901 | phase416/results/p416_memo.md (Phase 416's memo — the phase's quotable wording pending its gate, verbatim copy) md5 0fabba8ca2535a53578eb38361d65b51 |
| sources/p416_search.json | 57667 | phase416/results/p416_search.json (Phase 416's search record (both arms; the budget-overrun disclosure on its face), verbatim copy) md5 25efa0964b5a59c5a274d96cc021aa0f |
| sources/p416_verdicts.json | 1097630 | phase416/results/p416_verdicts.json (Phase 416's verdicts record — all 13 subjects' vectors, audits, ceilings and anatomy, verbatim copy) md5 3995eb3deca6dafb50e664e777cffadf |
| sources/p417_controls.json | 58515 | phase417/results/p417_controls.json (Phase 417's controls record — the stored record Gate-57's machinery control reproduces at abs diff 0.0, verbatim copy) md5 8fbeb1612f70ed0154d30ae25716ae8d |
| sources/p417_dense.json | 145203 | phase417/results/p417_dense.json (Phase 417's dense record — the scope table (v2, significance-filtered), verbatim copy) md5 e2c697389e61c5ebbef7dccffa733915 |
