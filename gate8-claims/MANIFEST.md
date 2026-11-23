# Gate-8 claims bundle - MANIFEST (release v1.10.0)

Every file in this folder, its size in bytes, and where it came from.
Copies are byte-for-byte copies of the named source. Figures are
generated from the bundle's own stored result files only.

| file | bytes | source / traceability |
|---|---|---|
| GATE8.md | 19316 | gate8/GATE8.md (verbatim copy of the gate record) |
| GATE8_AMENDMENT.md | 8304 | gate8/GATE8_AMENDMENT.md (verbatim copy of the gate amendment, 2026-11-22) |
| RESULTS.md | 11647 | written for this bundle; claim wordings extracted verbatim from results/wB_g8_2.md S7 (G8-2) and results/wA_g8_1.md S6 (G8-1, as amended by GATE8_AMENDMENT.md - see RESULTS.md S1) |
| code/wa_lib.py | 7340 | gate8/wa_lib.py (gate verifier code, verbatim copy) |
| code/wa_run1.py | 4284 | gate8/wa_run1.py (gate verifier code, verbatim copy) |
| code/wa_run2.py | 6025 | gate8/wa_run2.py (gate verifier code, verbatim copy) |
| code/wa_run3.py | 3391 | gate8/wa_run3.py (gate verifier code, verbatim copy) |
| code/wa_run4.py | 2760 | gate8/wa_run4.py (gate verifier code, verbatim copy) |
| code/wb_g82_israel.py | 6322 | gate8/wb_g82_israel.py (gate verifier code, verbatim copy) |
| code/wb_g82_solver.py | 11077 | gate8/wb_g82_solver.py (gate verifier code, verbatim copy) |
| code/wb_g82_spotcheck.py | 5719 | gate8/wb_g82_spotcheck.py (gate verifier code, verbatim copy) |
| code/wb_g82_spotcheck2.py | 8853 | gate8/wb_g82_spotcheck2.py (gate verifier code, verbatim copy) |
| figures/fig_g81_composed_payload.png | 108181 | data: results/wa_g8_1_numbers.json (wa_run1.verdict_h0.15_o4.regions; wa_run2.richardson_o4.dec_series); script: figures/make_figures.py |
| figures/fig_g82_attained_completion.png | 129429 | data: results/wb_g82_numbers.json (mirror_rows gains; uncompleted_cap0455_za1) + results/wb_g82_israel.json (kretschmann.bounds); script: figures/make_figures.py |
| figures/make_figures.py | 3274 | figure generator (programme venv python; reads only ../results/*.json) |
| results/wA_g8_1.md | 11980 | gate8/results/wA_g8_1.md (gate worker output, verbatim copy) |
| results/wB_g8_2.md | 18970 | gate8/results/wB_g8_2.md (gate worker output, verbatim copy) |
| results/wa_g8_1_numbers.json | 18961 | gate8/results/wa_g8_1_numbers.json (gate worker output, verbatim copy) |
| results/wa_run1.json | 8065 | gate8/results/wa_run1.json (gate worker output, verbatim copy) |
| results/wa_run2.json | 3896 | gate8/results/wa_run2.json (gate worker output, verbatim copy) |
| results/wa_run3.json | 3632 | gate8/results/wa_run3.json (gate worker output, verbatim copy) |
| results/wa_run4.json | 1757 | gate8/results/wa_run4.json (gate worker output, verbatim copy) |
| results/wa_run5.json | 654 | gate8/results/wa_run5.json (gate worker output, verbatim copy) |
| results/wa_run6.json | 79 | gate8/results/wa_run6.json (gate worker output, verbatim copy) |
| results/wa_search_log.md | 4949 | gate8/results/wa_search_log.md (gate worker output, verbatim copy) |
| results/wb_g82_israel.json | 5878 | gate8/results/wb_g82_israel.json (gate worker output, verbatim copy) |
| results/wb_g82_numbers.json | 17409 | gate8/results/wb_g82_numbers.json (gate worker output, verbatim copy) |
| results/wb_g82_search_log.md | 5856 | gate8/results/wb_g82_search_log.md (gate worker output, verbatim copy) |
| results/wb_g82_spotcheck2.json | 585 | gate8/results/wb_g82_spotcheck2.json (gate worker output, verbatim copy) |
| sources/p462_follow.json | 17818 | phase46/results/p462_follow.json (Phase-46 source record the gate audited, verbatim copy) |
| sources/p462_memo.md | 9278 | phase46/results/p462_memo.md (Phase-46 source record the gate audited, verbatim copy) |
| sources/p462_results.json | 22268 | phase46/results/p462_results.json (Phase-46 source record the gate audited, verbatim copy) |
| sources/p463_memo.md | 11379 | phase46/results/p463_memo.md (Phase-46 source record the gate audited, verbatim copy) |
| sources/p463_results.json | 17616 | phase46/results/p463_results.json (Phase-46 source record the gate audited, verbatim copy) |

Not copied (deliberately): gate8/*.log run logs, gate8/__pycache__/ ,
results/wb_g82_spotcheck.json + wb_spotcheck*.log (the v1 spot check,
kept non-deciding in the gate record and superseded by
wb_g82_spotcheck2.json, which is included), gate8/results/wa_run*.json
ARE included (they are the run-level numbers behind
wa_g8_1_numbers.json).

Figure verification: each PNG was regenerated from the listed JSON
files by figures/make_figures.py at assembly time and read back
visually; every plotted value traces to the listed data file.

AMENDMENT (2026-11-22): claim G8-1's v1.10.0 hold is LIFTED by
GATE8_AMENDMENT.md (copied in this bundle; original in gate8/) -
its restated wording carries one corrected figure (the cavity DEC
floor band, 4×10⁻⁵ → 2.3×10⁻⁴). The claim is upload-ready after
restatement as amended and is released in v1.10.0.
