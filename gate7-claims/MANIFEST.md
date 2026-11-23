# Gate-7 claims bundle - MANIFEST (release v1.10.0)

Every file in this folder, its size in bytes, and where it came from.
Copies are byte-for-byte copies of the named source (verified by the
assembly size check against the gate6-claims pattern). Figures are
generated from the bundle's own stored result files only.

| file | bytes | source / traceability |
|---|---|---|
| GATE7.md | 38182 | gate7/GATE7.md (verbatim copy of the gate record) |
| RESULTS.md | 12627 | written for this bundle; claim wordings extracted verbatim from GATE7.md (G7-1) and results/wB_g7_2.md S4 / results/wC_g7_3.md final section (G7-2/G7-3) |
| code/wa_anatomy.py | 5529 | gate7/wa_anatomy.py (gate verifier code, verbatim copy) |
| code/wa_check.py | 3222 | gate7/wa_check.py (gate verifier code, verbatim copy) |
| code/wa_eval.py | 9437 | gate7/wa_eval.py (gate verifier code, verbatim copy) |
| code/wa_run_g7.py | 7187 | gate7/wa_run_g7.py (gate verifier code, verbatim copy) |
| code/wa_symbolic.py | 9365 | gate7/wa_symbolic.py (gate verifier code, verbatim copy) |
| code/wa_tiebreak.py | 2490 | gate7/wa_tiebreak.py (gate verifier code, verbatim copy) |
| code/wb_auditor.py | 14167 | gate7/wb_auditor.py (gate verifier code, verbatim copy) |
| code/wb_symbolic.py | 5003 | gate7/wb_symbolic.py (gate verifier code, verbatim copy) |
| code/wc_auditor.py | 8752 | gate7/wc_auditor.py (gate verifier code, verbatim copy) |
| code/wc_check.py | 2738 | gate7/wc_check.py (gate verifier code, verbatim copy) |
| code/wc_crosscheck.py | 5557 | gate7/wc_crosscheck.py (gate verifier code, verbatim copy) |
| code/wc_recon.py | 7076 | gate7/wc_recon.py (gate verifier code, verbatim copy) |
| code/wc_run.py | 8020 | gate7/wc_run.py (gate verifier code, verbatim copy) |
| figures/fig_g71_margin_ledger.png | 109568 | data: results/wa_g71_numbers.json (deciding_b0.09/deciding_b0.1 all_sig margins) + results/wa_anatomy.json (r10_b*_Spp-inside/outside dec_min); script: figures/make_figures.py |
| figures/fig_g72_spline_finalists.png | 50100 | data: results/wb_g72_numbers.json (deciding_primary_b0.10_b0.10, deciding_second_b0.1363_b0.10); script: figures/make_figures.py |
| figures/fig_g73_procaccia_confirmation.png | 103408 | data: results/wc_g73_numbers.json (verdict_h0.0375, verdict_h0.01875, secondpath_order4_h0.0375, step3_crosscheck, step3_crosscheck_exact_minnull); script: figures/make_figures.py |
| figures/make_figures.py | 4434 | figure generator (programme venv python; reads only ../results/*.json) |
| results/wA_g7_1.md | 13878 | gate7/results/wA_g7_1.md (gate worker output, verbatim copy) |
| results/wB_g7_2.md | 15348 | gate7/results/wB_g7_2.md (gate worker output, verbatim copy) |
| results/wC_g7_3.md | 13758 | gate7/results/wC_g7_3.md (gate worker output, verbatim copy) |
| results/wa_anatomy.json | 6262 | gate7/results/wa_anatomy.json (gate worker output, verbatim copy) |
| results/wa_check.json | 2342 | gate7/results/wa_check.json (gate worker output, verbatim copy) |
| results/wa_g71_numbers.json | 20012 | gate7/results/wa_g71_numbers.json (gate worker output, verbatim copy) |
| results/wa_search_log.md | 5645 | gate7/wa_search_log.md (gate novelty search log, verbatim copy) |
| results/wa_tiebreak.json | 3753 | gate7/results/wa_tiebreak.json (gate worker output, verbatim copy) |
| results/wb_g72_numbers.json | 17244 | gate7/results/wb_g72_numbers.json (gate worker output, verbatim copy) |
| results/wb_search_log.md | 3206 | gate7/wb_search_log.md (gate novelty search log, verbatim copy) |
| results/wc_g73_numbers.json | 19831 | gate7/results/wc_g73_numbers.json (gate worker output, verbatim copy) |
| results/wc_search_log.md | 3514 | gate7/results/wc_search_log.md (gate worker output, verbatim copy) |
| sources/p501_memo.md | 16053 | phase50/results/p501_memo.md (Phase-50 source record the gate audited, verbatim copy) |
| sources/p502_memo.md | 13637 | phase50/results/p502_memo.md (Phase-50 source record the gate audited, verbatim copy) |
| sources/p502_verify10.json | 18512 | phase50/results/p502_verify10.json (Phase-50 source record the gate audited, verbatim copy) |
| sources/p502_verify10b.json | 4328 | phase50/results/p502_verify10b.json (Phase-50 source record the gate audited, verbatim copy) |
| sources/p503_ledger.json | 19664 | phase50/results/p503_ledger.json (Phase-50 source record the gate audited, verbatim copy) |
| sources/p503_memo.md | 19824 | phase50/results/p503_memo.md (Phase-50 source record the gate audited, verbatim copy) |
| sources/p503_pol_B_b0.10_K5.json | 1234 | phase50/results/p503_pol_B_b0.10_K5.json (Phase-50 source record the gate audited, verbatim copy) |
| sources/p503_pol_B_b0.1363_K5.json | 1258 | phase50/results/p503_pol_B_b0.1363_K5.json (Phase-50 source record the gate audited, verbatim copy) |
| sources/p504_closure.md | 1718 | phase50/results/p504_closure.md (Phase-50 source record the gate audited, verbatim copy) |

Not copied (deliberately): gate7/*.pkl (symbolic-expression caches,
machinery scratch), gate7/*.log (run logs), gate7/__pycache__/ - the
bundle carries the code, the numbers and the reports, not caches.

Figure verification: each PNG was regenerated from the listed JSON
files by figures/make_figures.py at assembly time and read back
visually; every plotted value traces to the listed data file.
