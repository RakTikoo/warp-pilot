# Gate-52 claims bundle - MANIFEST (release v1.43.0)

Every file in this folder, its size in bytes, and where it came from.
Copies are byte-for-byte copies of the named source (md5-verified at
assembly; every copy also cmp-verified against its source at assembly).
This manifest lists every file in the bundle except itself.

| file | bytes | source / traceability |
|---|---|---|
| GATE52.md | 13888 | gate52/GATE52.md (gate record, verbatim copy) md5 78e395c8a7681170b9e5a7e91ab6191e |
| GATE52_CHECKPOINT.md | 6512 | gate52/GATE52_CHECKPOINT.md (gate checkpoint, verbatim copy) md5 38a0b70738641d9c9be87af9290508fd |
| README_WHATSNEW_v1430.md | 7348 | written for this bundle (prepared README update; applied at upload) |
| RELEASE_v1.43.0.md | 15632 | written for this bundle (release draft; the GATE52.md §0 fence and §1 claim set with riders G52-R1…R4 embedded verbatim as a blockquote, round-trip-verified at assembly; version DOI TBD — minted at release) |
| RESULTS.md | 10307 | written for this bundle (the claim set: the GATE52.md §0 standing fence and §1 quotable claim set (G52-A…G52-D, riders G52-R1…R4) verbatim — the only quotable form of the Phase 412 claim set — diff-verified character-for-character at assembly) |
| code/g52_admit.py | 1488 | gate52/work/g52_admit.py (Gate-52's laptop-admission driver — the gate machinery re-run on the pool laptop (GATE52.md §6), verbatim copy) md5 d413d24350a947f0ec98c7266a21da93 |
| code/g52_arith.py | 6237 | gate52/work/g52_arith.py (Gate-52's arithmetic driver — the G52-C spends/exponents/fit recomputation and the G52-D gap arithmetic, verbatim copy) md5 0c2e20a2a37f3ede86ddd7252707952c |
| code/g52_calibrate.py | 9170 | gate52/work/g52_calibrate.py (Gate-52's calibration driver — CAL-1…CAL-10, verbatim copy) md5 be19e635fe8a0b6b9bbd46bfa98c5f36 |
| code/g52_extract.py | 3990 | gate52/work/g52_extract.py (Gate-52's extraction driver — the stored inputs taken from the primary artefacts with md5s, verbatim copy) md5 cd9035cab27104a3d9629a6633536abc |
| code/g52_lib.py | 32214 | gate52/work/g52_lib.py (Gate-52's machinery — Cartan structure equations in an orthonormal tetrad, forward-mode second-order Taylor-jet derivative engine, certified worst-null (KKT/PSD certificate), verbatim copy) md5 f600e2d7695f075626f849a93d9b636e |
| code/g52_mp.py | 17639 | gate52/work/g52_mp.py (Gate-52's 50-digit mpmath named-point verification path, verbatim copy) md5 cbe5d3c0e537940e1be90c9da5db849e |
| code/g52_polish.py | 5449 | gate52/work/g52_polish.py (Gate-52's adversary-polish driver, verbatim copy) md5 c891072be056c0bae0ef7dda4615b00f |
| code/g52_run.py | 6495 | gate52/work/g52_run.py (Gate-52's deciding-reads driver — the SET-244 band reads of the base, criterion and ladder winners, verbatim copy) md5 ecf75918aa89132d53cb73ffb5d093f7 |
| code/make_g52_figure.py | 5687 | written for this bundle (the figure generator — reads only the bundled records in sources/ (p412_fit.json, g52_arith.json) and writes figures/g52_ladder.png) |
| code/p412_admission.py | 878 | phase412/work/p412_admission.py (Phase 412's laptop-admission control, verbatim copy) md5 fa8e41cf389e374b38ebb817c88e9a73 |
| code/p412_controls.py | 2861 | phase412/work/p412_controls.py (Phase 412's controls driver (CTL-412-WIN / CTL-412-CRIT), verbatim copy) md5 1013d4df276db38acb8bc46c2da01f99 |
| code/p412_fit.py | 2066 | phase412/work/p412_fit.py (Phase 412's cost-law fit driver, verbatim copy) md5 60019b733cb723d7480f672ce64cd3f2 |
| code/p412_lib.py | 3281 | phase412/work/p412_lib.py (Phase 412's machinery — the ladder's profile stack and SET-244 reads, verbatim copy) md5 3683430b968561210077c5c658e36ba9 |
| code/p412_search.py | 14338 | phase412/work/p412_search.py (Phase 412's ladder search driver — the registered per-rung boxes and screens, verbatim copy) md5 e80f0e98b8411ed561a65a4ba5f87cce |
| figures/g52_ladder.png | 385628 | generated at assembly by code/make_g52_figure.py from the bundled records (the ladder's three rungs — criterion joint +1.227385×10⁻⁶, 2× joint +6.699289×10⁻⁷, 5× best-found joint −6.506282×10⁻⁵ — and the spend curve 1.703343×10⁻⁷ → 7.277906×10⁻⁷ → 6.646054×10⁻⁵ with the 3-point fit (A = 2.414947×10⁻⁶, p = 3.771023, implied crossing 0.865014 below the measured-legal rung), local exponents 2.095 / 4.927, the §0 fence, riders G52-R1/R2/R3/R4 and the SEC value −2.917201×10⁻⁴ on the figure's face) |
| sources/CHECKPOINT412.md | 15360 | phase412/CHECKPOINT412.md (Phase 412's phase record — registration summary, controls, verdict, anatomy, verbatim copy) md5 d4c368cb5751278e00c0db2b5dd5b628 |
| sources/g52_admission_laptop.json | 793 | gate52/results/g52_admission_laptop.json (Gate-52's laptop-admission record — ADMITTED at roundoff, all diffs ≤ 6.5×10⁻¹⁹, verbatim copy) md5 f94607e41f6089e176d2506941091154 |
| sources/g52_arith.json | 3054 | gate52/results/g52_arith.json (Gate-52's arithmetic record — spends recomputed at diff 0.0, local exponents 2.095 / 4.927, the refit (A, p, crossing) and the million-c gap figures (22.86 / 29.54 / 12.39 orders), verbatim copy) md5 31b2db669649d5bdd57882c2cce77cb8 |
| sources/g52_calibration.json | 1474 | gate52/results/g52_calibration.json (Gate-52's calibration record — CAL-1…CAL-10 ALL PASS, verbatim copy) md5 9def71bc5673eddfbc518e06a3c13ab5 |
| sources/g52_mp.json | 2491 | gate52/results/g52_mp.json (Gate-52's 50-digit mpmath named-point record — three named points, basis-invariant quantities agreeing at ≤ 9.3×10⁻¹⁹, verbatim copy) md5 162c52d91390e2b4e8c112cae9f70768 |
| sources/g52_numbers.json | 21776 | gate52/results/g52_numbers.json (Gate-52's deciding numbers — the G52-A/G52-B reads and controls, verbatim copy) md5 6990e0152dd4547f35533dad173ba001 |
| sources/g52_polish.json | 7846 | gate52/results/g52_polish.json (Gate-52's adversary-polish record, verbatim copy) md5 6ff2af990a1b357e37e6f56b79d3efd4 |
| sources/g52_stored_inputs.json | 939869 | gate52/results/g52_stored_inputs.json (Gate-52's stored-inputs record — the primary artefacts and their md5s, verbatim copy) md5 61186777dd0c1675a39534062c332e51 |
| sources/p412_controls.json | 1586 | phase412/results/p412_controls.json (Phase 412's controls record (VM), verbatim copy) md5 f63f9aebd1f588c4ea9d9a073737ef0a |
| sources/p412_controls_laptop.json | 1074 | phase412/results/p412_controls_laptop.json (Phase 412's controls record (laptop admission), verbatim copy) md5 dea2b31212af9e4dbabe105767f4e114 |
| sources/p412_fit.json | 1185 | phase412/results/p412_fit.json (Phase 412's fit record — the three rungs' peaks/joints/spends, the 3-point fit and the bracket outcome, verbatim copy) md5 ab6971c10f94f2cc5ba0c7c2edb57b55 |
| sources/p412_memo.md | 5646 | phase412/results/p412_memo.md (Phase 412's memo, verbatim copy) md5 9f020572c4072116d3dfef3a4d82d038 |
| sources/p412_registration.md | 10714 | phase412/work/p412_registration.md (Phase 412's registration — the rungs, the per-rung boxes B(P) = max(1, 2P/β), the caps and the verdict forms, verbatim copy) md5 aa34b3f2b4cfae88a2d16679f3a95592 |
| sources/p412_rungs.json | 4190 | phase412/results/p412_rungs.json (Phase 412's rungs record — the winners, knot vectors and confirmations at m = 2 and m = 5, verbatim copy) md5 d57b7c02e13413f56f6a09845c59073b |
| sources/p412_screens.jsonl | 827664 | phase412/results/p412_screens.jsonl (Phase 412's screen record — 760 stored screens, zero rejected, verbatim copy) md5 b544a1a17b53f42d0833f98e6c02396d |
| sources/p412_search.log | 473 | phase412/results/p412_search.log (Phase 412's search log — including the two runtime-restart resumes, verbatim copy) md5 49d28bcce67a95f5fc7f8aecb0c62f63 |
| sources/p412_state.json | 6184 | phase412/results/p412_state.json (Phase 412's search state record, verbatim copy) md5 dcdc9db9314f631be1c1eb21377121f1 |
