# Gate-50 claims bundle - MANIFEST (release v1.42.0)

Every file in this folder, its size in bytes, and where it came from.
Copies are byte-for-byte copies of the named source (md5-verified at
assembly; every copy also cmp-verified against its source at assembly).
This manifest lists every file in the bundle except itself.

| file | bytes | source / traceability |
|---|---|---|
| GATE50.md | 22858 | gate50/GATE50.md (gate record, verbatim copy) md5 5cce26fa1f601c1b65c984ef317d131c |
| README_WHATSNEW_v1420.md | 7419 | written for this bundle (prepared README update; applied at upload) |
| RELEASE_v1.42.0.md | 11944 | written for this bundle (release draft; the GATE50.md §0 fence and §1 claim set embedded verbatim, diff-verified at assembly; version DOI TBD — minted at release) |
| RESULTS.md | 14688 | written for this bundle (the claim set: the GATE50.md §0 fence and §1 block verbatim — the only quotable form of the Phase 405 claim set — diff-verified character-for-character at assembly) |
| code/g50_admission.py | 1442 | gate50/work/g50_admission.py (Gate-50's laptop-admission runner — the gate's own SET-244 reads on the pool frame, verbatim copy) md5 5c26efbe6f7b1714228f4d8342e9774f |
| code/g50_calibrate.py | 9329 | gate50/work/g50_calibrate.py (Gate-50's calibration driver — CAL-1…CAL-7, run before any deciding read, verbatim copy) md5 0defc0df9d4af5473caaf0d71037b3c3 |
| code/g50_lib.py | 33952 | gate50/work/g50_lib.py (Gate-50's machinery — the (r, n) operator algebra, Γ/Ricci assembly, Hawking–Ellis margins and secular-equation worst-null solver; imports no phase/gate evaluation code, verbatim copy) md5 f9ba20bd01b526747e9e6bd530f608f9 |
| code/g50_mp.py | 14775 | gate50/work/g50_mp.py (Gate-50's 50-digit mpmath verification at the named points, verbatim copy) md5 30d2905f2e91eb3df6f080feb253a2c9 |
| code/g50_polish.py | 2933 | gate50/work/g50_polish.py (Gate-50's adversary-polish driver (SAMPLER-M protocol) and the C395 diagnostic, verbatim copy) md5 caad218e510976c76bc068412ae6d12a |
| code/g50_run.py | 9885 | gate50/work/g50_run.py (Gate-50's deciding-reads driver — controls CTL-A/CTL-C, claims (a)–(e), verbatim copy) md5 1f9218188506db63999a7ac46ddcca00 |
| code/make_g50_figure.py | 8661 | written for this bundle (the figure generator — reads only the bundled records in sources/ and writes figures/g50_shape_and_cost.png) |
| figures/g50_shape_and_cost.png | 448654 | generated at assembly by code/make_g50_figure.py from the bundled records (the winning shape at the criterion with the fixed shape's stored local reads, the two shapes' joint-vs-peak cost reads, the winner's confirmations — joint +1.227385×10⁻⁶, worst-null +7.282×10⁻⁷, polish +1.214724×10⁻⁶ — the criterion spends 1.703×10⁻⁷ vs 1.058×10⁻⁵ with ratio 62.10, and riders G50-R2/G50-R5 plus the SEC value −2.213557×10⁻⁴ on the figure's face) |
| sources/CHECKPOINT405.md | 14138 | phase405/CHECKPOINT405.md (Phase 405's phase record — registration summary, controls, verdict, verbatim copy) md5 ffd2fb1781d5c785670884ce4c207884 |
| sources/g50_admission_laptop.json | 606 | gate50/results/g50_admission_laptop.json (Gate-50's laptop-admission record — the winner's joint bit-exact on the pool frame, verbatim copy) md5 5cd61916778ce99a650baa275d17eb9b |
| sources/g50_calibration.json | 2650 | gate50/results/g50_calibration.json (Gate-50's calibration record, verbatim copy) md5 4e1bcdf084323a7583d1f03eb607e500 |
| sources/g50_ctl_b_resolution.json | 2036 | gate50/results/g50_ctl_b_resolution.json (Gate-50's CTL-B resolution record — the H2 anchor identified as a SAMPLER-M sampled statistic, verbatim copy) md5 03181128a506dd45bc62942108be9c12 |
| sources/g50_mp.json | 2611 | gate50/results/g50_mp.json (Gate-50's mpmath record — named-point margins, exact peak arithmetic, shape derivative scan, verbatim copy) md5 5f1a9460795f7940555c669bdb724018 |
| sources/g50_numbers.json | 21588 | gate50/results/g50_numbers.json (Gate-50's deciding record — all deciding reads and stored comparisons, verbatim copy) md5 755ffb868f959c390420c18f4d479e29 |
| sources/g50_polish.json | 11348 | gate50/results/g50_polish.json (Gate-50's polish record — SAMPLER-M adversary polishes of the base, the winner and the peak-0.25 read, verbatim copy) md5 0493543f05b3e5088b9959979ce3273c |
| sources/g50_stored_inputs.json | 20099 | gate50/results/g50_stored_inputs.json (Gate-50's stored inputs with source md5s — profile knot vectors, the Phase 400 winner, Phase 404's ladder, Phase 405's confirmation, verbatim copy) md5 6d825e17dbf3409e981b753b2c5200bb |
| sources/p404_memo.md | 8911 | phase404/results/p404_memo.md (Phase 404's memo — the fixed-shape re-introduction read: break-even μ_S* = 0.171875, the criterion cost 1.058×10⁻⁵, verbatim copy) md5 0181945f43bfa8707f30dc4a7095de25 |
| sources/p405_confirmation.json | 10544 | phase405/results/p405_confirmation.json (Phase 405's confirmation record — the winning shape's criterion knot vector and the criterion re-read at diff 0.0, verbatim copy) md5 9b6a30cf3e17343288e69a7103a7f66d |
| sources/p405_controls.json | 2379 | phase405/results/p405_controls.json (Phase 405's VM controls record, verbatim copy) md5 c951d493ba7d0e3b995b1e9552f9cae1 |
| sources/p405_controls_laptop.json | 813 | phase405/results/p405_controls_laptop.json (Phase 405's laptop-admission record, verbatim copy) md5 d15733be155328b7cbc779ad223e9ffb |
| sources/p405_memo.md | 9035 | phase405/results/p405_memo.md (Phase 405's memo — the quotable phase wording, the cost curve and the anatomy, verbatim copy) md5 1c0240d21160922bc701cbdd943e0f4a |
| sources/p405_registration.md | 9498 | phase405/work/p405_registration.md (Phase 405's registration SS0–SS7, filed before any computation, verbatim copy) md5 da617acbc91bfbce458a7804fe27c60e |
| sources/p405_screens.jsonl | 758838 | phase405/results/p405_screens.jsonl (Phase 405's screens record — 726 stored screens, zero rejected, verbatim copy) md5 665fd5bd593df5750d69929c57db77c9 |
| sources/p405_state.json | 56099 | phase405/results/p405_state.json (Phase 405's search state record, verbatim copy) md5 dc4f44984885041dc52a359fcb7de553 |
