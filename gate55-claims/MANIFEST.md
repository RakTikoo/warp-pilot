# Gate-55 claims bundle - MANIFEST (release v1.46.0)

Every file in this folder, its size in bytes, and where it came from.
Copies are byte-for-byte copies of the named source (md5-verified at
assembly; every copy also cmp-verified against its source at assembly).
This manifest lists every file in the bundle except itself.

| file | bytes | source / traceability |
|---|---|---|
| GATE55.md | 20682 | gate55/GATE55.md (gate record, verbatim copy) md5 89a4fbbae61d27e1b52f4666f265adc8 |
| GATE55_CHECKPOINT.md | 6205 | gate55/GATE55_CHECKPOINT.md (gate checkpoint, verbatim copy) md5 fb32272dbec6d5752611f1cf5b0215cc |
| README_WHATSNEW_v1460.md | 8228 | written for this bundle (prepared README update; applied at upload) |
| RELEASE_v1.46.0.md | 15666 | written for this bundle (release draft; the GATE55.md §1 quotable claim set (G55-A…G55-D, riders G55-R1…R3) embedded verbatim as a blockquote, round-trip-verified at assembly; version DOI TBD — minted at release) |
| RESULTS.md | 10505 | written for this bundle (the claim set: the GATE55.md §1 quotable claim set (G55-A…G55-D, riders G55-R1…R3) verbatim — the only quotable form of the Phase 420 claim set — verified character-for-character at assembly) |
| code/g55_laptop.py | 2563 | gate55/work/g55_laptop.py (Gate-55's laptop-admission driver — the gate machinery re-run on the pool laptop as corroboration for claims (a), (b) and (c), verbatim copy) md5 11a24f91f0c047bfccc748dab1a0b426 |
| code/g55_lib.py | 13037 | gate55/work/g55_lib.py (Gate-55's machinery — gamma matrices by Kronecker products, the composite as an explicit field function with per-mode masses and analytic derivatives, own Hawking–Ellis classifier and eigen-channel decomposition, own delta construction, own FD Jacobians, verbatim copy) md5 781e9385b1187e865eae84000378de52 |
| code/g55_run.py | 15452 | gate55/work/g55_run.py (Gate-55's driver — controls C1–C3 and claims (a)–(d), verbatim copy) md5 602ea78d3ebf50047affaff1fa9905ae |
| code/make_g55_figure.py | 3897 | written for this bundle (the figure generator — reads only the bundled record in sources/ (g55_results.json) and writes figures/g55_correction.png) |
| code/p420_admission.py | 2860 | phase420/work/p420_admission.py (Phase 420's laptop-admission driver, verbatim copy) md5 30b9ed156020edda9514695a8dc51767 |
| code/p420_check.py | 9664 | phase420/work/p420_check.py (Phase 420's independent checker — ALL PASS, verbatim copy) md5 ff1cba735b7ca6bc9eb747b610e1f810 |
| code/p420_ladder_fix.py | 5055 | phase420/work/p420_ladder_fix.py (Phase 420's ladder-completion script — Amendment 3: the completed perturbation ladder at tightened tolerances, bar unchanged, verbatim copy) md5 0531beb387bb008af3ab98cbb01cb1b7 |
| code/p420_machinery.py | 16658 | phase420/work/p420_machinery.py (Phase 420's machinery — Phase 410's mating block verbatim plus the per-mode-mass generalisation and the disclosed u_spinor guard of Amendment 2, verbatim copy) md5 5ac836958a07e61bbe85aeb8a2572685 |
| code/p420_run.py | 31627 | phase420/work/p420_run.py (Phase 420's driver — the composite mating fits C-A/C-B/C-S and the controls, verbatim copy) md5 5e64b1a9054cc46b62ea926ada21c1d3 |
| figures/g55_correction.png | 213005 | generated for this bundle by code/make_g55_figure.py from the bundled records only (the corrected target's channel margins at the A sites before/after delta — SEC_trace zeroed at A2/A3, joint_min rising — and the supplied total's densities under both definitions (Eulerian T[0,0] and eigenvalue rho, rider G55-R2), the standing fences on its face) |
| sources/CHECKPOINT420.md | 10226 | phase420/CHECKPOINT420.md (Phase 420's checkpoint — verdict, corrected target, controls, fits, accounting, amendments and incidents, verbatim copy) md5 d7b4aacb0aa4e2bd3e5e22de56040e74 |
| sources/g55_admission.json | 931 | gate55/results/g55_admission.json (Gate-55's laptop admission record, verbatim copy) md5 688c0550c65e14b62f925673b5ffa26c |
| sources/g55_laptop_results.json | 850 | gate55/results/g55_laptop_results.json (Gate-55's laptop corroboration reads for claims (a), (b) and (c), verbatim copy) md5 a00ca42e0e867a3047dc00f0f8489d5f |
| sources/g55_registration.md | 6735 | gate55/work/g55_registration.md (Gate-55's registration — ruling bars fixed in advance, verbatim copy) md5 58476f0f7b5c4a0d947c94448084ce11 |
| sources/g55_results.json | 11651 | gate55/results/g55_results.json (Gate-55's deciding record — controls C1–C3, claims (a)–(d) and the amendment audits, verbatim copy) md5 b32461864fa24ba380b74debd3290917 |
| sources/p420_admission.json | 1607 | phase420/results/p420_admission.json (Phase 420's laptop admission record, verbatim copy) md5 e04ebc32e1b758bf6a4fe83d03b951f4 |
| sources/p420_cands_fitCA_N3_3.jsonl | 10076 | phase420/work/p420_cands_fitCA_N3_3.jsonl (Phase 420's Fit C-A (3,3) counting-arm candidate record, verbatim copy) md5 520b1906c1f79422df90aad1e639bc3b |
| sources/p420_cands_fitCA_N6_6.jsonl | 17734 | phase420/work/p420_cands_fitCA_N6_6.jsonl (Phase 420's Fit C-A (6,6) candidate record, verbatim copy) md5 ca58c0cf73ecddba744188c2aebc7347 |
| sources/p420_cands_fitCB_N6_6.jsonl | 14042 | phase420/work/p420_cands_fitCB_N6_6.jsonl (Phase 420's Fit C-B tracking candidate record, verbatim copy) md5 e164b165d220ad4ad917a3755da8d0ab |
| sources/p420_cands_fitCS_N12.jsonl | 11067 | phase420/work/p420_cands_fitCS_N12.jsonl (Phase 420's Fit C-S single-family N = 12 candidate record — the G55-D context arm, verbatim copy) md5 babe19a716128818ab440d4459082d96 |
| sources/p420_cands_fitCS_N6.jsonl | 5051 | phase420/work/p420_cands_fitCS_N6.jsonl (Phase 420's Fit C-S single-family N = 6 candidate record — the stored C-S warm-A solution of G55-D, verbatim copy) md5 f85315d9b50bfb54c9fc98288d97939e |
| sources/p420_check_results.json | 3778 | phase420/results/p420_check_results.json (Phase 420's checker results — ALL PASS, verbatim copy) md5 bf3d1cb638acc39457739d265806f1a1 |
| sources/p420_fitCA_primary.json | 2917 | phase420/work/p420_fitCA_primary.json (Phase 420's Fit C-A primary solution — the stored composite primary of G55-B, verbatim copy) md5 3ef305bc7419d7e783f5561432b33e51 |
| sources/p420_fitCB_primary.json | 2995 | phase420/work/p420_fitCB_primary.json (Phase 420's Fit C-B tracking primary solution, verbatim copy) md5 a397b17ab0c3cdf1111527bdb652a8fa |
| sources/p420_ladder_completed.json | 1016 | phase420/results/p420_ladder_completed.json (Phase 420's completed perturbation ladder — Amendment 3, bar unchanged, verbatim copy) md5 e6d41dbe369f98ad665ecd1c0987a2e3 |
| sources/p420_ladder_fix.log | 403 | phase420/work/p420_ladder_fix.log (the ladder-completion run log, verbatim copy) md5 b8a4b2f3d6044b7bcb525d0048d85a53 |
| sources/p420_memo.md | 2911 | phase420/results/p420_memo.md (Phase 420's memo, verbatim copy) md5 8adcd8c75472b394b7e58b6a6f66578f |
| sources/p420_registration.md | 16036 | phase420/work/p420_registration.md (Phase 420's registration SS0–SS9 plus Amendments 1–3, verbatim copy) md5 77e54f0030306874528fcee997c287b5 |
| sources/p420_results.json | 55986 | phase420/results/p420_results.json (Phase 420's deciding record — controls, fits, accounting, verdict, and the preserved as-first-computed verdict string, verbatim copy) md5 07baaf504ecb9b60379da54142b908b1 |
| sources/p420_run.log | 5223 | phase420/work/p420_run.log (Phase 420's driver run log, verbatim copy) md5 d55b433a7b1f5b24e7c1b1a024d7d8f1 |
| sources/p420_targets.json | 9074 | phase420/work/p420_targets.json (Phase 420's stored target tensors — T_req and the constructed T_corr at the eight site reads, verbatim copy) md5 dda98bca496694cbbb254ed15107cbd3 |
