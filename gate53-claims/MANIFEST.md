# Gate-53 claims bundle - MANIFEST (release v1.44.0)

Every file in this folder, its size in bytes, and where it came from.
Copies are byte-for-byte copies of the named source (md5-verified at
assembly; every copy also cmp-verified against its source at assembly).
This manifest lists every file in the bundle except itself.

| file | bytes | source / traceability |
|---|---|---|
| GATE53.md | 24090 | gate53/GATE53.md (gate record, verbatim copy) md5 a453065b3d61ca27b2a840d76dd5b828 |
| GATE53_CHECKPOINT.md | 12035 | gate53/GATE53_CHECKPOINT.md (gate checkpoint, verbatim copy) md5 d4c4f03894d13a008a0ce2a99d646938 |
| README_WHATSNEW_v1440.md | 7731 | written for this bundle (prepared README update; applied at upload) |
| RELEASE_v1.44.0.md | 18026 | written for this bundle (release draft; the GATE53.md §7 quotable claim set (G53-A…G53-E, riders G53-R1…R3) embedded verbatim as a blockquote, round-trip-verified at assembly; version DOI TBD — minted at release) |
| RESULTS.md | 7151 | written for this bundle (the claim set: the GATE53.md §7 quotable claim set (G53-A…G53-E, the fence G53-B, riders G53-R1…R3) verbatim — the only quotable form of the Phase 408 claim set — verified character-for-character at assembly) |
| code/g53_audits.py | 2553 | gate53/work/g53_audits.py (Gate-53's audits driver — the controls and B-2 full registered audits, verbatim copy) md5 c978d17b2f14da3dc80fc212112a47a2 |
| code/g53_dense.py | 5525 | gate53/work/g53_dense.py (Gate-53's dense driver — the dip confirmation, A-6's radial profile, the dense scans of the controls, the corrected Richardson limits, verbatim copy) md5 ef85ebd71791d21dfe38025672839312 |
| code/g53_laptop.py | 1845 | gate53/work/g53_laptop.py (Gate-53's laptop-admission driver — the gate machinery re-run on the pool laptop as corroboration for the deciding eigenvalue reads, verbatim copy) md5 9ed93bea659db43e379b5c5843215f2c |
| code/g53_lib.py | 21469 | gate53/work/g53_lib.py (Gate-53's machinery — the graded-family builder generalised to n_c ∈ {8, 12, 16}, box-4 stages 2–4 by the spline-antiderivative scheme, the registered set and the gate's legality/q reads, verbatim copy) md5 5bb842d1d0b3f73e01e714ef33fb2531 |
| code/g53_records.py | 6853 | gate53/work/g53_records.py (Gate-53's records driver — stored-byte hashes, the independent embedding recomputation, chain calibration, verbatim copy) md5 bf1973ab06d6acdd854b28fb0c89a995 |
| code/g53_thin.py | 5570 | gate53/work/g53_thin.py (Gate-53's thin-margin driver — A-6's registered audits, the spacing ladder, the first dense scan; contains the discarded wrong-direction Richardson pass disclosed in GATE53.md §1, verbatim copy) md5 4c51a19968960ac8a18c116715c93ac1 |
| code/make_g53_figure.py | 6403 | written for this bundle (the figure generator — reads only the bundled records in sources/ (g53_audits_*.json, g53_thin.json, g53_dense.json) plus the dose–response sequence as stated in GATE53.md §5, and writes figures/g53_ladder.png) |
| code/p408_check.py | 8257 | phase408/work/p408_check.py (Phase 408's checker — the coordinator-run home checker, 31/31 PASS, verbatim copy) md5 72f0a37d3df82d6d6c3117290b99e170 |
| code/p408_lib16.py | 12686 | phase408/work/p408_lib16.py (Phase 408's 16-mode library, verbatim copy) md5 d29403552c09c87703daeaa58e4c4c1b |
| code/p408_make_followups.py | 2854 | phase408/work/p408_make_followups.py (Phase 408's follow-up generator, verbatim copy) md5 36c0ce867fe89f7eba982b6e273b4c03 |
| code/p408_pool_p408_de.py | 9233 | phase408/work/p408_pool_p408_de.py (Phase 408's pool DE driver, verbatim copy) md5 53d682b3e9bda0584b4b1d5fb2dcec52 |
| code/p408_pool_p408_gen0check.py | 7253 | phase408/work/p408_pool_p408_gen0check.py (Phase 408's pool generation-0 check driver, verbatim copy) md5 4dbef96abcd61bceaae403a9262b9982 |
| code/p408_pool_p408_harvest.py | 3537 | phase408/work/p408_pool_p408_harvest.py (Phase 408's pool harvest driver, verbatim copy) md5 7d020ff0220f057f98166736102e2139 |
| code/p408_pool_p408_lib16.py | 12906 | phase408/work/p408_pool_p408_lib16.py (Phase 408's pool 16-mode library, verbatim copy) md5 fec9868cb9a872f33e3ea648bf6e6a2d |
| code/p408_pool_p408_powell.py | 4206 | phase408/work/p408_pool_p408_powell.py (Phase 408's pool Powell polish driver, verbatim copy) md5 e4766a0e402eeca4bede1da2dd64a2e9 |
| code/p408_pool_p408_recalib.py | 10331 | phase408/work/p408_pool_p408_recalib.py (Phase 408's pool recalibration driver, verbatim copy) md5 8ab56dd735458799659fa89c78459665 |
| code/p408_pool_p408_screen16.py | 4814 | phase408/work/p408_pool_p408_screen16.py (Phase 408's pool 16-mode screen driver, verbatim copy) md5 36098431d7b0d9fba68a99610163d080 |
| code/p408_pool_p408_validate.py | 7409 | phase408/work/p408_pool_p408_validate.py (Phase 408's pool validation driver, verbatim copy) md5 db8625856a409044c3e567b1449cfcd8 |
| code/p408_verdicts.py | 31321 | phase408/work/p408_verdicts.py (Phase 408's verdicts driver, verbatim copy) md5 528a048d34a3b0af7c22f1f9912c9982 |
| code/p408_watchdog.sh | 1264 | phase408/work/p408_watchdog.sh (Phase 408's pool watchdog script, verbatim copy) md5 13a6898e547d147d3fa328fc1cb0051e |
| code/p408_workerA.py | 27125 | phase408/work/p408_workerA.py (Phase 408 Worker A driver, verbatim copy) md5 45b893d8f8af6f9c2df176ecdd649ce2 |
| code/p408_workerA2.py | 9658 | phase408/work/p408_workerA2.py (Phase 408 Worker A2 driver, verbatim copy) md5 e41fc448865d139c7818bc31ee0b7cb6 |
| figures/g53_ladder.png | 332690 | generated at assembly by code/make_g53_figure.py from the bundled records (the ladder's dose–response 0.1363 → 0.18671875 → 0.18984375 → 0.191796875 → 0.192578125 → 0.193359375 with increments; the registered deciding SEC margins with floor multiples — y_his +3.404×10⁻⁷ (109.5×), E2-1 +7.075×10⁻⁸ (13.4×), RW-5 +6.056×10⁻⁷ (106.5×), A-6 +3.613×10⁻⁸ (6.82×), A-6 converged +2.675×10⁻⁸ — set against the dense radial (step 0.05) SEC minima: y_his +5.449×10⁻⁸ @ 4.0, RW-5 +2.975×10⁻⁷ @ 3.55, E2-1 −1.162×10⁻⁶ @ 9.95, A-6 −1.257×10⁻⁶ @ 5.42; the G53-B fence, rider G53-R2 and the G53-R3 seed name on the figure's face) |
| sources/CHECKPOINT408.md | 36126 | phase408/CHECKPOINT408.md (Phase 408's phase record — registration, Amendment A-408-1 and the integrated closure, verbatim copy) md5 f93aec567e450e07fc567e85c01aea47 |
| sources/g53_audits_B-2.json | 18781 | gate53/results/g53_audits_B-2.json (Gate-53's full registered audits of B-2 — 'RW-5 embedded, box-clipped at c13' — at 0.192578125 and 0.195078125, verbatim copy) md5 144c2fe696280e678d83071f2f846d8b |
| sources/g53_audits_E2-1.json | 9895 | gate53/results/g53_audits_E2-1.json (Gate-53's full registered audits of E2-1 at 0.191796875, verbatim copy) md5 3c73fcef3c66aea208ac3c35c8e2ed20 |
| sources/g53_audits_RW-5.json | 18657 | gate53/results/g53_audits_RW-5.json (Gate-53's full registered audits of RW-5 at 0.192578125 and 0.195078125, verbatim copy) md5 85c35eea15ccac64b8a8bde9f6cd9328 |
| sources/g53_audits_y_his.json | 18593 | gate53/results/g53_audits_y_his.json (Gate-53's full registered audits of y_his at 0.1363 and 0.1364, verbatim copy) md5 046e2a08fa6219984736fa851c24ab44 |
| sources/g53_dense.json | 11745 | gate53/results/g53_dense.json (Gate-53's dense record — the corrected Richardson limits, the dip-point confirmation, A-6's radial profile and the dense scans of RW-5, E2-1, y_his and B-2, verbatim copy) md5 7522bd526475c7b4b4be114bfe244ff7 |
| sources/g53_laptop_out.json | 2429 | gate53/results/g53_laptop_out.json (Gate-53's laptop-admission record — admitted as corroboration for the deciding eigenvalue reads, A-6's deciding SEC agreeing to 4.2×10⁻¹⁴, verbatim copy) md5 5fe37b384ed7ff379fa35bf5be2b39a9 |
| sources/g53_records.json | 5489 | gate53/results/g53_records.json (Gate-53's records — the six vectors' sha256 verification and the independent embedding recomputation (max diff 0.0), verbatim copy) md5 99a225bfc0dbfdb2c00e657db32aaf0a |
| sources/g53_thin.json | 22327 | gate53/results/g53_thin.json (Gate-53's A-6 record — chain reads, the registered audits at 0.193359375 and 0.195859375, the spacing ladder and the deciding point, verbatim copy) md5 4c3a12f7a1edc9c798f8d309e0100458 |
| sources/p408_amendment_A408_1.json | 7436 | phase408/results/p408_amendment_A408_1.json (Amendment A-408-1's record — both vector hashes, the c13 clip and the losslessness gate, verbatim copy) md5 ef16a5dd5b3879e324561a52ffe3a1cf |
| sources/p408_controls.json | 64712 | phase408/results/p408_controls.json (Phase 408's home controls record, verbatim copy) md5 95bb996e96f42cfc67f4066c2ace2d4e |
| sources/p408_memo.md | 11796 | phase408/results/p408_memo.md (Phase 408's memo — the quotable wording of the phase record, verbatim copy) md5 5aaa822c58b66135844bd3b16d48c1e9 |
| sources/p408_pool_a408_de_pop.npz | 16370 | phase408/results/p408_pool_a408_de_pop.npz (Phase 408's pool staged DE population, Arm A, verbatim copy) md5 c879c162403ac1f5ca1357004313906f |
| sources/p408_pool_a408_de_state.json | 64322 | phase408/results/p408_pool_a408_de_state.json (Phase 408's pool DE state record, Arm A, verbatim copy) md5 58c6a22b8cc72a216ddf059d0e8399e3 |
| sources/p408_pool_a408_de_yref.json | 172 | phase408/results/p408_pool_a408_de_yref.json (Phase 408's pool DE reference record, Arm A, verbatim copy) md5 d56a11bb7e5248459b17eb9a4219c1aa |
| sources/p408_pool_a408_harvest.json | 25566 | phase408/results/p408_pool_a408_harvest.json (Phase 408's pool harvest record, Arm A, verbatim copy) md5 7127547c999b41cb25ee299a89ab6465 |
| sources/p408_pool_a408_powell_de0.json | 2478 | phase408/results/p408_pool_a408_powell_de0.json (Phase 408's pool Powell polish record, Arm A, verbatim copy) md5 71357dd8ce32afb98bd0820366cd5ea0 |
| sources/p408_pool_a408_powell_de0_inc.json | 2478 | phase408/results/p408_pool_a408_powell_de0_inc.json (Phase 408's pool Powell polish record, Arm A, verbatim copy) md5 71357dd8ce32afb98bd0820366cd5ea0 |
| sources/p408_pool_a408_powell_de1.json | 2538 | phase408/results/p408_pool_a408_powell_de1.json (Phase 408's pool Powell polish record, Arm A, verbatim copy) md5 f0501c2f8a6822283026fa17da251f28 |
| sources/p408_pool_a408_powell_de1_inc.json | 2538 | phase408/results/p408_pool_a408_powell_de1_inc.json (Phase 408's pool Powell polish record, Arm A, verbatim copy) md5 f0501c2f8a6822283026fa17da251f28 |
| sources/p408_pool_a408_powell_de2.json | 2504 | phase408/results/p408_pool_a408_powell_de2.json (Phase 408's pool Powell polish record, Arm A, verbatim copy) md5 36c191a91d3c11146a3064b8936f70c9 |
| sources/p408_pool_a408_powell_de2_inc.json | 2504 | phase408/results/p408_pool_a408_powell_de2_inc.json (Phase 408's pool Powell polish record, Arm A, verbatim copy) md5 36c191a91d3c11146a3064b8936f70c9 |
| sources/p408_pool_b408_de_pop.npz | 16370 | phase408/results/p408_pool_b408_de_pop.npz (Phase 408's pool staged DE population, Arm B, verbatim copy) md5 1994dc738b26e79a5abee6f099d55f9d |
| sources/p408_pool_b408_de_state.json | 70687 | phase408/results/p408_pool_b408_de_state.json (Phase 408's pool DE state record, Arm B, verbatim copy) md5 b163a3a19f145f5dcad746ff9cef4829 |
| sources/p408_pool_b408_de_yref.json | 189 | phase408/results/p408_pool_b408_de_yref.json (Phase 408's pool DE reference record, Arm B, verbatim copy) md5 8282639b93405ab0f25b80e1caafed9d |
| sources/p408_pool_b408_harvest.json | 24737 | phase408/results/p408_pool_b408_harvest.json (Phase 408's pool harvest record, Arm B, verbatim copy) md5 9802e8ddf2240e1715b9e21b9b75f736 |
| sources/p408_pool_b408_powell_de0.json | 2546 | phase408/results/p408_pool_b408_powell_de0.json (Phase 408's pool Powell polish record, Arm B, verbatim copy) md5 4b16bc3638c3deba68f14c471d1d5e87 |
| sources/p408_pool_b408_powell_de0_inc.json | 2546 | phase408/results/p408_pool_b408_powell_de0_inc.json (Phase 408's pool Powell polish record, Arm B, verbatim copy) md5 4b16bc3638c3deba68f14c471d1d5e87 |
| sources/p408_pool_b408_powell_de1.json | 2559 | phase408/results/p408_pool_b408_powell_de1.json (Phase 408's pool Powell polish record, Arm B, verbatim copy) md5 9ad6e8ab9dd0caa93d4bfb3f37f8d985 |
| sources/p408_pool_b408_powell_de1_inc.json | 2559 | phase408/results/p408_pool_b408_powell_de1_inc.json (Phase 408's pool Powell polish record, Arm B, verbatim copy) md5 9ad6e8ab9dd0caa93d4bfb3f37f8d985 |
| sources/p408_pool_b408_powell_de2.json | 2615 | phase408/results/p408_pool_b408_powell_de2.json (Phase 408's pool Powell polish record, Arm B, verbatim copy) md5 e12027283b63b081ea0d26ac0b770fac |
| sources/p408_pool_b408_powell_de2_inc.json | 2615 | phase408/results/p408_pool_b408_powell_de2_inc.json (Phase 408's pool Powell polish record, Arm B, verbatim copy) md5 e12027283b63b081ea0d26ac0b770fac |
| sources/p408_pool_p408_gen0check_a.json | 19360 | phase408/results/p408_pool_p408_gen0check_a.json (Phase 408's pool home-verification record, verbatim copy) md5 20db2c7ffa6917df0b687301e87d2b14 |
| sources/p408_pool_p408_recalib_a.json | 2503 | phase408/results/p408_pool_p408_recalib_a.json (Phase 408's pool home-verification record, verbatim copy) md5 e20c1a1edf662d7cc0a73a98ef78b35b |
| sources/p408_pool_p408_recalib_b.json | 4423 | phase408/results/p408_pool_p408_recalib_b.json (Phase 408's pool home-verification record, verbatim copy) md5 9020ea86ea1f45b8363fd000fd7b02fa |
| sources/p408_pool_p408_validate_a.json | 3900 | phase408/results/p408_pool_p408_validate_a.json (Phase 408's pool home-verification record, verbatim copy) md5 e079493ce133bbaf676de7a2cfae9d61 |
| sources/p408_pool_p408_validate_b.json | 7584 | phase408/results/p408_pool_p408_validate_b.json (Phase 408's pool home-verification record, verbatim copy) md5 299a807711786bb6fb2dfa0e08d63720 |
| sources/p408_pool_vectors.json | 6810 | phase408/work/p408_pool_vectors.json (Phase 408's pool subject-vectors record, verbatim copy) md5 1cde1f38cf39728af29cecf312e9f9d2 |
| sources/p408_search.json | 43688 | phase408/results/p408_search.json (Phase 408's search record, verbatim copy) md5 ea14a2608151ec70e6b320108dbb2d58 |
| sources/p408_spec_a_de.json | 45327 | phase408/work/p408_spec_a_de.json (Phase 408's arm specification — the registered search record, verbatim copy) md5 286baeaeb0ed36640abfc390ab022478 |
| sources/p408_spec_a_harvest.json | 14295 | phase408/work/p408_spec_a_harvest.json (Phase 408's arm specification — the registered search record, verbatim copy) md5 ed460629aaf3ddd59d46f2d219a79a49 |
| sources/p408_spec_a_powell_de0.json | 1225 | phase408/work/p408_spec_a_powell_de0.json (Phase 408's arm specification — the registered search record, verbatim copy) md5 542623d41ff477c688fc0eb54523759c |
| sources/p408_spec_a_powell_de1.json | 1245 | phase408/work/p408_spec_a_powell_de1.json (Phase 408's arm specification — the registered search record, verbatim copy) md5 70a61d04ac94ffe8a85936b36cea2744 |
| sources/p408_spec_a_powell_de2.json | 1234 | phase408/work/p408_spec_a_powell_de2.json (Phase 408's arm specification — the registered search record, verbatim copy) md5 88bd4b24efdda4c5746bdfdb995fa54e |
| sources/p408_spec_a_powell_starts.json | 493 | phase408/work/p408_spec_a_powell_starts.json (Phase 408's arm specification — the registered search record, verbatim copy) md5 b903d290ce9c1b8bc9426b2ae238ec85 |
| sources/p408_spec_b_de.json | 2490 | phase408/work/p408_spec_b_de.json (Phase 408's arm specification — the registered search record, verbatim copy) md5 c53dffd5f8811911ac5b4f11e7352714 |
| sources/p408_spec_b_harvest.json | 13590 | phase408/work/p408_spec_b_harvest.json (Phase 408's arm specification — the registered search record, verbatim copy) md5 4018d78f68517768657a04489ed7b6ba |
| sources/p408_spec_b_powell_de0.json | 1251 | phase408/work/p408_spec_b_powell_de0.json (Phase 408's arm specification — the registered search record, verbatim copy) md5 ddfab96c692f00abcba65999b356a9e6 |
| sources/p408_spec_b_powell_de1.json | 1244 | phase408/work/p408_spec_b_powell_de1.json (Phase 408's arm specification — the registered search record, verbatim copy) md5 c1046c29a99a88ba9f5097c8cf1db6ce |
| sources/p408_spec_b_powell_de2.json | 1264 | phase408/work/p408_spec_b_powell_de2.json (Phase 408's arm specification — the registered search record, verbatim copy) md5 8e3375a71d2e6298121b789ba5143320 |
| sources/p408_spec_b_powell_starts.json | 506 | phase408/work/p408_spec_b_powell_starts.json (Phase 408's arm specification — the registered search record, verbatim copy) md5 7171bbd6157f98fcd9da4d3676b092c3 |
| sources/p408_verdicts.json | 961076 | phase408/results/p408_verdicts.json (Phase 408's verdicts record — the home re-judgement of every subject, verbatim copy) md5 7d750418268a484b6685e62297e01aa6 |
| sources/p408_workerA2_memo.md | 6501 | phase408/results/p408_workerA2_memo.md (Phase 408 Worker A2 memo, verbatim copy) md5 3030e6b1ff3abd8cd63e5c772da26c16 |
| sources/p408_workerA_memo.md | 8523 | phase408/results/p408_workerA_memo.md (Phase 408 Worker A memo, verbatim copy) md5 f633760e16ad026707ba16085c755764 |
| sources/p408_workerB_memo.md | 12688 | phase408/results/p408_workerB_memo.md (Phase 408 Worker B memo, verbatim copy) md5 752df445552b43f0d42671506203933b |
| sources/p408_workerC_memo.md | 12989 | phase408/results/p408_workerC_memo.md (Phase 408 Worker C memo, verbatim copy) md5 54188422e367ef38700d9a855b9993c9 |
