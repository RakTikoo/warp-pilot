# Gate-49 claims bundle - MANIFEST (release v1.40.0)

Every file in this folder, its size in bytes, and where it came from.
Copies are byte-for-byte copies of the named source (md5-verified at
assembly; every copy also cmp-verified against its source at assembly).
This manifest lists every file in the bundle except itself.

| file | bytes | source / traceability |
|---|---|---|
| GATE49.md | 26257 | gate49/GATE49.md (gate record, verbatim copy) md5 1ce7eb90ccaff21c7bc9afd267d66a8c |
| README_WHATSNEW_v1400.md | 6425 | written for this bundle (prepared README update; applied at upload) |
| RELEASE_v1.40.0.md | 11846 | written for this bundle (release draft; the GATE49.md §8 claim set embedded verbatim, diff-verified at assembly; version DOI TBD — minted at release) |
| RESULTS.md | 12547 | written for this bundle (the claim set: the GATE49.md §8 block verbatim — the only quotable form of the Phase 403 claim set; the §8 block in RESULTS.md was diff-verified character-for-character at assembly) |
| code/g49_calibrate.py | 3272 | gate49/work/g49_calibrate.py (Gate-49's calibration driver — C-0/C-0b/C-1/C-2, verbatim copy) md5 21583422cbb5908b0489a7986b255d14 |
| code/g49_lib.py | 20659 | gate49/work/g49_lib.py (Gate-49's machinery — brute-force Cartesian FD Einstein tensor from stored profile values only, Richardson extrapolation, Eulerian frame, margins, exact secular-equation worst-null, SET read, verbatim copy) md5 bf60c18cb82947bb271bc338c1b48099 |
| code/g49_polish.py | 4787 | gate49/work/g49_polish.py (Gate-49's adversary-polish driver — the Type-I depth re-derivation and h-refinement for claim (b), verbatim copy) md5 a3cb813aad71cc0fad7bf1382cc4c7d5 |
| code/g49_recount.py | 5117 | gate49/work/g49_recount.py (Gate-49's recount driver — the 334-screen recount, decomposition, box edges and worst-DEC re-read for claims (c) and (d), verbatim copy) md5 7a97bd7d7c4ccac6e6f88a0b2802d315 |
| code/g49_run.py | 8705 | gate49/work/g49_run.py (Gate-49's main driver — controls, the width curve, the winner, the clamp and the SS7 peaks for claims (a), (b) and (e), verbatim copy) md5 5ab8cab05a009c9f5a7bf9a77ae90bf8 |
| code/make_g49_figure.py | 6724 | written for this bundle (the figure generator — reads only the bundled records in sources/ and writes figures/g49_width_curve.png) |
| figures/g49_width_curve.png | 347558 | generated at assembly by code/make_g49_figure.py from the bundled records (the width curve W10 −2.980985×10⁻⁵ → W28 transported −9.384899×10⁻⁶ → re-optimised centre −3.676112×10⁻⁶, the gain decomposition — transport +2.042495×10⁻⁵, re-optimisation +5.708787×10⁻⁶ — and riders G49-E and G49-F on the figure's face) |
| sources/CHECKPOINT403.md | 7476 | phase403/CHECKPOINT403.md (Phase 403's phase record — registration, controls, verdict, anatomy, verbatim copy) md5 a776f5e9915ed8ed33757a3804ddb5e4 |
| sources/g49_calibration.json | 3004 | gate49/results/g49_calibration.json (Gate-49's calibration record — C-0/C-0b/C-1/C-2, verbatim copy) md5 8a19386c44f33fcef537170795cdf844 |
| sources/g49_numbers.json | 11738 | gate49/results/g49_numbers.json (Gate-49's deciding reads — controls, the width curve, the winner and the SS7 peaks, verbatim copy) md5 c8be9b9a7943e7c3fc441fdd3e38d8ff |
| sources/g49_polish.json | 4531 | gate49/results/g49_polish.json (Gate-49's adversary-polish record — the Type-I depth re-derivation at the winner, verbatim copy) md5 fe2a14b5a87fe49fdb786ff4045f7b3b |
| sources/g49_recount.json | 3528 | gate49/results/g49_recount.json (Gate-49's recount record — 334 screens, the decomposition, the box edges, the worst-DEC re-read, verbatim copy) md5 b0c5e97e909e14dd2836cb87045a2260 |
| sources/g49_winner_set.npz | 367754 | gate49/results/g49_winner_set.npz (Gate-49's winner SET record — the full point-set read at the W28 centre, verbatim copy) md5 4a9136636893075975cad3124a6a97f2 |
| sources/p402_memo.md | 10598 | phase402/results/p402_memo.md (Phase 402's memo — the pose drift map and the registered transport the width curve rides on, verbatim copy) md5 6f73c108da21f220b54748e5691a8c00 |
| sources/p403_anatomy.json | 4933 | phase403/results/p403_anatomy.json (Phase 403's anatomy record at the winner, verbatim copy) md5 a04e1ff6eac7ba35828328045966d746 |
| sources/p403_clamp.json | 1087 | phase403/results/p403_clamp.json (Phase 403's end-clamp record at the winner, verbatim copy) md5 51b3b04a5fdf52b58e570f06c19d1673 |
| sources/p403_confirmation.json | 4246 | phase403/results/p403_confirmation.json (Phase 403's confirmation record — the winner's full re-read at diff 0.0, verbatim copy) md5 c39a358bfa6e8ad4ac3881ddbaf04ad6 |
| sources/p403_controls.json | 2825 | phase403/results/p403_controls.json (Phase 403's VM controls record, verbatim copy) md5 9b82f0b6307fbf2a4a1d30b4243edfb2 |
| sources/p403_controls_laptop.json | 1460 | phase403/results/p403_controls_laptop.json (Phase 403's laptop admission record — NOT ADMITTED, the C-10 signature, verbatim copy) md5 f900802320f68a5b1f8fdf60bca785d5 |
| sources/p403_memo.md | 12897 | phase403/results/p403_memo.md (Phase 403's memo, verbatim copy) md5 839a084f7ea4e967af443eea0892b37d |
| sources/p403_screens.jsonl | 179806 | phase403/results/p403_screens.jsonl (Phase 403's 334-read screens record — the file Gate-49 recounted for claims (c) and (d), verbatim copy) md5 40767ad5b159240a0e77d0a90c70d68b |
| sources/p403_search_summary.json | 10040 | phase403/results/p403_search_summary.json (Phase 403's search summary record, verbatim copy) md5 d20c40c375c031f6af2c92a30ec415b2 |
| sources/p403_step1.json | 9370 | phase403/results/p403_step1.json (Phase 403's Step-1 record — the width curve W10…W28, verbatim copy) md5 f08f1c8a3de468960c17d672d9c38d83 |
