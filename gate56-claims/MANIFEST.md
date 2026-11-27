# Gate-56 claims bundle - MANIFEST (release v1.47.0)

Every file in this folder, its size in bytes, and where it came from.
Copies are byte-for-byte copies of the named source (md5-verified at
assembly; every copy also cmp-verified against its source at assembly).
This manifest lists every file in the bundle except itself.

| file | bytes | source / traceability |
|---|---|---|
| GATE56.md | 15688 | gate56/GATE56.md (gate record, verbatim copy) md5 d0d4d811b8f309c9621d50452476407e |
| GATE56_CHECKPOINT.md | 11848 | gate56/GATE56_CHECKPOINT.md (gate checkpoint, verbatim copy) md5 631d787e4439be5c40577a60fc9910f6 |
| README_WHATSNEW_v1470.md | 8145 | written for this bundle (prepared README update; applied at upload) |
| RELEASE_v1.47.0.md | 17132 | written for this bundle (release draft; the GATE56.md §1 quotable claim set (G56-A…G56-D, riders G56-R1…R5) embedded verbatim as a blockquote, round-trip-verified at assembly; version DOI TBD — minted at release) |
| RESULTS.md | 10246 | written for this bundle (the claim set: the GATE56.md §1 quotable claim set (G56-A…G56-D, riders G56-R1…R5) verbatim — the only quotable form of the Phase 418 claim set — verified character-for-character at assembly) |
| code/g56_admission.py | 1316 | gate56/work/g56_admission.py (Gate-56's laptop-admission driver — the gate endpoint read re-run on the pool laptop, verbatim copy) md5 94e002887b2762cab7af25d8c18eb494 |
| code/g56_build_tensor.py | 8417 | gate56/work/g56_build_tensor.py (Gate-56's tensor builder — derives all metric derivatives symbolically with sympy and generates g56_tensor.py, verbatim copy) md5 454d277f16a1a926c561bcd7c4cb7dfa |
| code/g56_controls.py | 13012 | gate56/work/g56_controls.py (Gate-56's calibrations CAL-1…CAL-5 and controls driver, verbatim copy) md5 c20e268072205c85dc282134b6ce6648 |
| code/g56_lib.py | 24176 | gate56/work/g56_lib.py (Gate-56's machinery — analytic base profiles and the stored assembly arithmetic, own ADM tetrad, Hawking–Ellis margins, exact secular-equation worst-null, adversary polish, verbatim copy) md5 942dba64742f202e5c1c8eb1d567cfb0 |
| code/g56_reads.py | 7851 | gate56/work/g56_reads.py (Gate-56's claim-reads driver, verbatim copy) md5 45b958938f86aee6f00ed0bf22e60f4d |
| code/g56_reads2.py | 8441 | gate56/work/g56_reads2.py (Gate-56's claim-reads driver, second part — transect, binning recount and disclosure audits, verbatim copy) md5 2ea8301ff3262593d45d9374c3f72992 |
| code/g56_splines.py | 5238 | gate56/work/g56_splines.py (Gate-56's own not-a-knot cubic spline solver, float64 + mpmath variants, verbatim copy) md5 d5fe93452100da7906addf5d8dd784b8 |
| code/g56_spot.py | 11841 | gate56/work/g56_spot.py (Gate-56's 50-digit mpmath spot check of the full chain at the carried point's binding site, verbatim copy) md5 d0018ceb5b8e5dd6f7d79b32a6ba3c6d |
| code/g56_tensor.py | 17027 | gate56/work/g56_tensor.py (Gate-56's generated tensor module — sympy-derived Einstein tensor, readable CSE source, numpy + mpmath evaluators, verbatim copy) md5 53297b2c70aed236e714364d68e6e5b3 |
| code/make_g56_figure.py | 3679 | written for this bundle (the figure generator — reads only the bundled record in sources/ (g56_reads.json) and writes figures/g56_spend_landscape.png) |
| code/p418_admission.py | 993 | phase418/work/p418_admission.py (Phase 418's laptop-admission driver, verbatim copy) md5 6143a18382cbaeece1549bd3307c5d51 |
| code/p418_controls.py | 6155 | phase418/work/p418_controls.py (Phase 418's controls driver, verbatim copy) md5 41f2db4802cfd4d25713b3244d8db492 |
| code/p418_lib.py | 7075 | phase418/work/p418_lib.py (Phase 418's machinery — the carrying-aware hunt's evaluation library, verbatim copy) md5 9b35a5abd9761544a1bd91c9cfc07082 |
| code/p418_r17.py | 3114 | phase418/work/p418_r17.py (Phase 418's R17 supplement driver — the disclosed 200-screen K_S = 17 supplement, verbatim copy) md5 19474aa2428738b9e3404c7091c19ee9 |
| code/p418_search.py | 28187 | phase418/work/p418_search.py (Phase 418's search driver — the joint optimisation over base scalings, base corrections and shift shape, verbatim copy) md5 d1c20d892617db204ace5c444569c7a2 |
| figures/g56_spend_landscape.png | 225222 | generated for this bundle by code/make_g56_figure.py from the bundled records only (the three-base criterion spend comparison at matched peaks (G56-B) and the 400-base→B1 transect landscape (G56-D), the standing fences on its face) |
| sources/CHECKPOINT418.md | 4884 | phase418/CHECKPOINT418.md (Phase 418's checkpoint — verdict, the carried point, the landscape, disclosures and accounting, verbatim copy) md5 cd93ceee6e49b00b42b1a9e52c9e1038 |
| sources/g56_admission_laptop.json | 485 | gate56/results/g56_admission_laptop.json (Gate-56's laptop admission record, laptop side, verbatim copy) md5 f44e4460f954491b8b18b4f530fd9b80 |
| sources/g56_admission_vm.json | 394 | gate56/results/g56_admission_vm.json (Gate-56's laptop admission record, VM side, verbatim copy) md5 1d89a6182407fc7aa03904ffce4eca0b |
| sources/g56_build_tensor.log | 107 | gate56/work/g56_build_tensor.log (Gate-56's tensor-build log, verbatim copy) md5 9d578317eb37ea2250cd4fa6adb3e97a |
| sources/g56_controls.json | 6643 | gate56/results/g56_controls.json (Gate-56's calibrations and controls record, verbatim copy) md5 a446655f9b0adf558eac78e11f6e6f6f |
| sources/g56_reads.json | 15111 | gate56/results/g56_reads.json (Gate-56's deciding record — claims (a)–(d) and the disclosure audits, verbatim copy) md5 38ecd8f380005b2b4de081b70ff38504 |
| sources/g56_registration.md | 11493 | gate56/work/g56_registration.md (Gate-56's registration — charges, bars and machinery fixed in advance, verbatim copy) md5 47989c3291c48a3474160e7188737677 |
| sources/g56_spot.json | 988 | gate56/results/g56_spot.json (Gate-56's 50-digit spot-check record, verbatim copy) md5 59bf31e824b71a241009dfc9676f262d |
| sources/p418_confirmation.json | 7412 | phase418/results/p418_confirmation.json (Phase 418's confirmation reads of the referred points, verbatim copy) md5 2d4b8f47e32991d99f84f164d5226bcb |
| sources/p418_controls.json | 4101 | phase418/results/p418_controls.json (Phase 418's controls record, VM side, verbatim copy) md5 f98ddef2f67922035f79c0aa630b8428 |
| sources/p418_controls_laptop.json | 1222 | phase418/results/p418_controls_laptop.json (Phase 418's controls record, laptop side, verbatim copy) md5 2c96976799c365a1ffc76771e1dd5d9d |
| sources/p418_memo.md | 11063 | phase418/results/p418_memo.md (Phase 418's memo, verbatim copy) md5 5dd30bbd575067c061f6e20c7baa4d73 |
| sources/p418_r17.log | 398 | phase418/results/p418_r17.log (Phase 418's R17 supplement run log, verbatim copy) md5 fc4d1bc7e7ffa6d24fd3a59a807dcada |
| sources/p418_registration.md | 16947 | phase418/work/p418_registration.md (Phase 418's registration — filed before computation, verbatim copy) md5 bd139a0a336a0f97a416f590bf536daf |
| sources/p418_screens.jsonl | 2749554 | phase418/results/p418_screens.jsonl (Phase 418's full screen record — 1,884 screens; the recount source of claim (d), verbatim copy) md5 f4e4fb2955d2a6a87e2dcdda9b619180 |
| sources/p418_search.log | 159 | phase418/results/p418_search.log (Phase 418's search run log, verbatim copy) md5 40b046d9aaa7bdbd573c3ed541474277 |
| sources/p418_state.json | 13918 | phase418/results/p418_state.json (Phase 418's search state — stage counts exact; its total_screens field counts the main driver only, the cosmetic note of Gate-56's audit (ii), verbatim copy) md5 0f8a1d752e120a236f32748b1debf0f9 |
