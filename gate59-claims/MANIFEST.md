# Gate-59 claims bundle - MANIFEST (release v1.49.0)

Every file in this folder, its size in bytes, and where it came from.
Copies are byte-for-byte copies of the named source (md5-verified at
assembly; every copy also cmp-verified against its source at assembly).
This manifest lists every file in the bundle except itself.

| file | bytes | source / traceability |
|---|---|---|
| GATE59.md | 23163 | gate59/GATE59_REPORT.md (gate record, verbatim copy of gate59/GATE59_REPORT.md) md5 ece768d455866da633f05d79c79a6a13 |
| GATE59_CHECKPOINT.md | 4486 | gate59/GATE59_CHECKPOINT.md (gate checkpoint, verbatim copy) md5 56d6e2041f139547371e2ad95ec1d2a4 |
| README_WHATSNEW_v1490.md | 5845 | written for this bundle (prepared README update; applied at upload) |
| RELEASE_v1.49.0.md | 8139 | written for this bundle (release draft; the quotable claim set (G59-A…G59-D) embedded as a blockquote; version DOI TBD — minted at release) |
| RESULTS.md | 9102 | written for this bundle (the claim set: G59-A…G59-D and riders G59-R1/R2/R4/R5 verbatim — the only quotable form of the Phase 431 claim set; G59-D is rider G59-R3 verbatim) |
| code/g59_armA.py | 9527 | gate59/work/g59_armA.py (Gate-59's Arm A driver — anatomy, constrained Jacobians, independent search, first-pass relaxation; its run died in a service restart before writing its JSON — see GATE59.md §10(ii); verbatim copy) md5 5fed8175f8ea8889e58555d3594ec8d2 |
| code/g59_armA_recovery.py | 7091 | gate59/work/g59_armA_recovery.py (the recovery run — recomputed anatomy, Jacobians and the N = 12 warm re-convergence after the restart; verbatim copy) md5 b601a0b95c2e0383db298dad5c09ce42 |
| code/g59_audit.py | 9495 | gate59/work/g59_audit.py (Gate-59's audit driver — hashes, controls CTL-431-0/1/3, the four matings at t = 0 on both paths, spectra, prices, densities; verbatim copy) md5 d18fed84482c663041975a4e744593ea |
| code/g59_b2.py | 6954 | gate59/work/g59_b2.py (Gate-59's B-2 persistence reads — registered grids, window spots in both evaluable forms, ladder periods/worst instants/returns; verbatim copy) md5 25031207d19b76a691946c040139df51 |
| code/g59_crossing.py | 3765 | gate59/work/g59_crossing.py (Gate-59's crossing diagnostic — the per-mode-form reproduction of the phase's stored spots and the two faithful-form crossings of §6(a); verbatim copy) md5 a754218811a3ac2defe03795a851ee40 |
| code/g59_laptop.py | 1222 | gate59/work/g59_laptop.py (Gate-59's laptop-admission driver (corroboration); verbatim copy) md5 d0f5c60e9805e4c82c02e3d08468ae30 |
| code/g59_lib.py | 9006 | gate59/work/g59_lib.py (Gate-59's independent implementation — the stress tensor from the field bilinear, the derived pair kernel, B-2 reads; no phase code; verbatim copy) md5 1a3f5233d41b6c9560542af7e023d957 |
| code/g59_relax2.py | 6208 | gate59/work/g59_relax2.py (Gate-59's converged per-site dictionary relaxation — Adam + analytic-Jacobian Gauss–Newton polish; the §5 decisive read; verbatim copy) md5 7c05bcfa0dc2a33ee2f1e11f5b9759ab |
| code/make_g59_figure.py | 2644 | gate59/work/make_g59_figure.py (written for this bundle (the figure generator — reads only the bundled sources/g59_relax2.json and writes figures/g59_relaxation.png)) md5 b11d35dee8e6d728d27ad557f76792c1 |
| code/p431_check.py | 7094 | phase431/work/p431_check.py (Phase 431's coordinator checker — re-run at the gate ALL PASS, output identical to the stored record; verbatim copy) md5 ceb97bf891fd018f96c62a85f96cfa57 |
| figures/g59_relaxation.png | 103649 | generated at assembly by code/make_g59_figure.py from the bundled records (left: the per-site relaxation floor at the peak site A3 vs shell energy E — minimised at the mating's own E = 1.005853, rising monotonically to 1.9139×10⁻³ at E = 4.3 — against the joint fit's A3 residual and the 428 F1 bar; right: per-site joint residuals vs relaxation floors at the three sites) |
| sources/CHECKPOINT428.md | 6008 | phase428/CHECKPOINT428.md (Phase 428's phase record — the persistence functional F1–F3 this gate's verdicts are stated against, verbatim copy) md5 8c4e990ddced62e69ca0fd3c02121f1c |
| sources/CHECKPOINT430.md | 9184 | phase430/CHECKPOINT430.md (Phase 430's phase record — the B-2 instrument and the drift verdict that charged Phase 431, verbatim copy) md5 341cf971dafa331cadeab495ad27256f |
| sources/CHECKPOINT431.md | 5500 | phase431/CHECKPOINT431.md (Phase 431's phase record — registration, amendments A1/A2, incidents, verdicts, verbatim copy) md5 89c2ff0b3ceee0b33122a82ee4b1398f |
| sources/g59_armA.json | 5266 | gate59/results/g59_armA.json (Gate-59's Arm A record — anatomy, Jacobians, warm re-convergence (recovery run), per-start search values transcribed from sources/g59_armA.log, first-pass relaxation marked undertrained; verbatim copy) md5 272864bc4a5814165b495f1a11489544 |
| sources/g59_armA.log | 921 | gate59/work/g59_armA.log (the original Arm A run's log — the surviving record of its per-start search values and Jacobian σ_min lines, transcribed into sources/g59_armA.json after the service restart; verbatim copy) md5 50639763704b08bd86ec063e3867a061 |
| sources/g59_audit.json | 9371 | gate59/results/g59_audit.json (Gate-59's audit record — sha256 of every audited object, controls, the four matings on both paths, spectra, prices, supplier densities; verbatim copy) md5 579f7ad2ac7ba1c685496a652f990304 |
| sources/g59_b2.json | 5135 | gate59/results/g59_b2.json (Gate-59's B-2 record — registered grids, window spots, ladder periods, worst instants, ladder returns in pair and direct forms; verbatim copy) md5 a7bf5bf73b83c98d95f8f84396b1c73f |
| sources/g59_crossing.json | 1218 | gate59/results/g59_crossing.json (Gate-59's crossing record — the per-mode-form spot reproductions and the faithful-form crossings t* = 67210312.02 (Acoef) / 67187297.34 (longdouble per-mode) units; verbatim copy) md5 5cdaba7e7def06c1abe40682c5260f57 |
| sources/g59_laptop_out.json | 1124 | gate59/results/g59_laptop_out.json (Gate-59's laptop-admission record — admitted as corroboration (Fit A t = 0 pair read 2.9659850903775113×10⁻¹², diff 6.8×10⁻¹⁹ vs the VM read); verbatim copy) md5 30427dce9dcf16854827935f335e5840 |
| sources/g59_relax2.json | 2866 | gate59/results/g59_relax2.json (Gate-59's converged relaxation record — A3 energy scan, best-fit anatomy, other-site floors, the joint residuals they are compared against; verbatim copy) md5 9866e39040bca38e5ad06654a23ff17b |
| sources/p410_targets.json | 8994 | phase410/work/p410_targets.json (the target record — T_req's and T_corr's tensors at the three sites both arms mate; verbatim copy) md5 91e43f2ffc164005edf84e394c1b93a8 |
| sources/p431_admission.json | 1224 | phase431/results/p431_admission.json (Phase 431's laptop-admission record, verbatim copy) md5 6dceb8e02f2b359fe913710e62d4f031 |
| sources/p431_best_A_t1_N12.json | 2766 | phase431/work/p431_best_A_t1_N12.json (the confirmed Arm A / T_req mating of record (N = 12), verbatim copy) md5 a081f3c591285ad68226c36af27f2623 |
| sources/p431_best_A_t2_6_6.json | 2772 | phase431/work/p431_best_A_t2_6_6.json (the Arm A / T_corr mating of record ((6,6), one shell), verbatim copy) md5 67b0eaa230f5f62b411e007c1d2960d1 |
| sources/p431_best_B_t1_N6_L3.json | 1481 | phase431/work/p431_best_B_t1_N6_L3.json (the Arm B / T_req ladder mating of record (N = 6, L3), verbatim copy) md5 81cecbffac8082f130636b67976d9ff8 |
| sources/p431_best_B_t2_6_6_L3.json | 2777 | phase431/work/p431_best_B_t2_6_6_L3.json (the Arm B / T_corr ladder mating of record ((6,6), L3), verbatim copy) md5 7f23c5b8c2f577cdc491f136b763dacd |
| sources/p431_check_results.json | 3312 | phase431/results/p431_check_results.json (the stored checker record — the gate's re-run reproduced it identically, verbatim copy) md5 92610b6491413172b04567f02a5a8bf8 |
| sources/p431_memo.md | 9598 | phase431/results/p431_memo.md (Phase 431's memo — the phase's quotable wording pending its gate, verbatim copy) md5 4ec9589318cd4d8eddb0fb98871f524f |
| sources/p431_results.json | 36688 | phase431/results/p431_results.json (Phase 431's driver record — searches, confirmations, anatomies, Jacobians, B-2 reads, verbatim copy) md5 5ef7b0830b50fe662274a1b6b23feccd |
| sources/p431_supplement.json | 1205 | phase431/results/p431_supplement.json (Phase 431's window-spot supersession record — confirmed by the gate in both evaluable forms, verbatim copy) md5 c41784a96373c1d1bc88a5c2af7c06c9 |
