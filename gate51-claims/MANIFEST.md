# Gate-51 claims bundle - MANIFEST (release v1.41.0)

Every file in this folder, its size in bytes, and where it came from.
Copies are byte-for-byte copies of the named source (md5-verified at
assembly; every copy also cmp-verified against its source at assembly).
This manifest lists every file in the bundle except itself.

| file | bytes | source / traceability |
|---|---|---|
| GATE51.md | 20338 | gate51/GATE51.md (gate record, verbatim copy) md5 f096670df474a2ac89771779ec00e030 |
| README_WHATSNEW_v1410.md | 6962 | written for this bundle (prepared README update; applied at upload) |
| RELEASE_v1.41.0.md | 12687 | written for this bundle (release draft; the GATE51.md §7 claim set and §1 calibration note C-1 embedded verbatim, diff-verified at assembly; version DOI TBD — minted at release) |
| RESULTS.md | 13427 | written for this bundle (the claim set: the GATE51.md §7 block verbatim — the only quotable form of the Phase 392 claim set — and calibration note C-1 verbatim; both diff-verified character-for-character at assembly) |
| code/g51_audits.py | 2612 | gate51/work/g51_audits.py (Gate-51's audit driver — the registered-bar verdict audits of the four subjects (claims (a) and controls), verbatim copy) md5 0cc8653aa58505c0212caa9f7301f8e6 |
| code/g51_lib.py | 23298 | gate51/work/g51_lib.py (Gate-51's machinery — the gate-lineage graded-family builder (n_c ∈ {8, 12}) and audit drivers' library, verbatim copy) md5 74389bad188438d7e168a9e1f8d90f09 |
| code/g51_records.py | 5414 | gate51/work/g51_records.py (Gate-51's records driver — the hash gate, RW-5 interiority, and the Arm T / Arm R-16 record re-judgements (claims (b), (c), (d)), verbatim copy) md5 a6107ab6a8dc9c96a5123157d1859693 |
| code/g51_screen.py | 4665 | gate51/work/g51_screen.py (Gate-51's screen driver — the FD screen's β_crit ratings and the artefact conviction (C-1, §6), verbatim copy) md5 78b7505deab46ac2a1222e90c2e511aa |
| code/g51_summary.py | 2236 | gate51/work/g51_summary.py (Gate-51's summary driver — the registered-bar verdict table assembly, verbatim copy) md5 94d9de9541f2d038b64614c0d0e7608d |
| code/make_g51_figure.py | 4877 | written for this bundle (the figure generator — reads only the bundled records in sources/ and writes figures/g51_dose_response.png) |
| figures/g51_dose_response.png | 364289 | generated at assembly by code/make_g51_figure.py from the bundled records (the graded dose–response 0.1363 → 0.18671875 → 0.18984375 → 0.191796875 → 0.192578125, RW-5's margin anatomy — worst SEC +6.055586×10⁻⁷ @ r = 3.75, 106.5× the FD floor — the failure bracket 0.195078125, and the category fence plus the G51-D rider on the figure's face) |
| sources/CHECKPOINT392.md | 22881 | phase392/CHECKPOINT392.md (Phase 392's phase record — registration, controls, verdict, anatomy, verbatim copy) md5 2b58e9346fc93a46116cefb4770ee8df |
| sources/g51_audits.log | 832 | gate51/results/g51_audits.log (Gate-51's audits log, verbatim copy) md5 a303b73b8313b77f25e55193abdf865f |
| sources/g51_audits_E2-1.json | 9419 | gate51/results/g51_audits_E2-1.json (Gate-51's audit record for E2-1 (control: legal at 0.191796875), verbatim copy) md5 50a5ca82907473490424e92792bab04d |
| sources/g51_audits_RW-1.json | 9585 | gate51/results/g51_audits_RW-1.json (Gate-51's audit record for RW-1 (the tie subject: legal at 0.192578125), verbatim copy) md5 537138891c66cbca98f614af899d1b4b |
| sources/g51_audits_RW-5.json | 17778 | gate51/results/g51_audits_RW-5.json (Gate-51's audit record for RW-5 (claim (a): legal at 0.192578125; compound failure at 0.195078125), verbatim copy) md5 dd04dbfda60ceb9e5b8437d55511a34e |
| sources/g51_audits_y_his.json | 17700 | gate51/results/g51_audits_y_his.json (Gate-51's audit record for y_his (controls at 0.1363 / 0.1364, calibration note C-1), verbatim copy) md5 7b5bce12b1c5dce7c23bb37b24206555 |
| sources/g51_records.json | 9307 | gate51/results/g51_records.json (Gate-51's records — hash gate, RW-5 interiority, Arm T and Arm R-16 record re-judgements, verbatim copy) md5 badcb433b7c358a8ee9c7f25ab38057b |
| sources/g51_screen.json | 1389 | gate51/results/g51_screen.json (Gate-51's screen record — β_crit ratings under both masks and the Phase-386 artefact conviction, verbatim copy) md5 91ffa498cf84e1e85de5ffcde13871b2 |
| sources/g51_summary.json | 18777 | gate51/results/g51_summary.json (Gate-51's summary record — the registered-bar verdict table, verbatim copy) md5 869167066e1db5d15e2bf616538da0a4 |
| sources/p392_controls.json | 34914 | phase392/results/p392_controls.json (Phase 392's controls record (C-392-1…C-392-4), verbatim copy) md5 a57a8f2e47bd2709a6c6286a3e449fe1 |
| sources/p392_memo.md | 9583 | phase392/results/p392_memo.md (Phase 392's memo — the quotable new-category wording and the dose–response, verbatim copy) md5 f1036ad9fd4e82b61c7e937d4d05b849 |
| sources/p392_pool_r16_de_state.json | 63941 | phase392/results/p392_pool_r16_de_state.json (Phase 392's Arm R-16 staged DE state — the record Gate-51 re-judged claim (d) from (gen 106, done = False, staged population), verbatim copy) md5 f5d312167cf4957fac4d85f44f224dc0 |
| sources/p392_pool_t_de_state.json | 58542 | phase392/results/p392_pool_t_de_state.json (Phase 392's Arm T staged DE state — the record Gate-51 re-judged claim (c) from (118 gens, flat best-history, done = True), verbatim copy) md5 b5456c31591dd5af5adbed5a754c192c |
| sources/p392_search.json | 65856 | phase392/results/p392_search.json (Phase 392's search record — the three arms' lineages, verbatim copy) md5 f9659c44258e8bae525b3dcd23cf30a7 |
| sources/p392_verdicts.json | 888209 | phase392/results/p392_verdicts.json (Phase 392's verdicts record — the home re-judgements of the arms' subjects, verbatim copy) md5 b01422a9032c25cf95e87ca22d1e3a41 |
