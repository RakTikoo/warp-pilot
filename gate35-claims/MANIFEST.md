# Gate-35 claims bundle - MANIFEST (release v1.26.0)

Every file in this folder, its size in bytes, and where it came from.
Copies are byte-for-byte copies of the named source (md5-verified at
assembly; every copy also cmp-verified against its source at assembly).
This manifest lists every file in the bundle except itself.

| file | bytes | source / traceability |
|---|---|---|
| GATE35.md | 13075 | gate35/GATE35.md (gate record, verbatim copy) md5 ba013a381b9092cae7eb0516244909c2 |
| CHECKPOINT_GATE35.md | 4233 | gate35/CHECKPOINT_GATE35.md (gate checkpoint, verbatim copy) md5 3c405bbc0886e28c28fbecb7dfbacd3a |
| RESULTS.md | 4362 | written for this bundle (G35-A, G35-B restated-continuum, G35-C, in Gate-35 §5's wording, verbatim, EC fence carried) |
| RELEASE_v1.26.0.md | 4397 | written for this bundle (release draft; version DOI TBD — minted at release) |
| README_WHATSNEW_v1260.md | 1983 | written for this bundle (prepared README update; applied at upload) |
| code/g35_item1.py | 13703 | gate35/work/g35_item1.py (gate Item 1 code (the adversary search), verbatim copy) md5 205ca418af5e3ae10d04530a56e1edf1 |
| code/g35_item2.py | 7721 | gate35/work/g35_item2.py (gate Item 2 code (independent re-read), verbatim copy) md5 6d12f75cdf46c01e3d14404ef6f0b7c4 |
| code/g35_lib.py | 17421 | gate35/work/g35_lib.py (gate library, verbatim copy) md5 526d32819b5de220c8de3097a51704de |
| code/g35_rho.py | 5776 | gate35/work/g35_rho.py (gate density evaluator, verbatim copy) md5 c24c321c1c5b4f9afb05419ad7ab9865 |
| results/g35_item1_results.json | 8761 | gate35/work/g35_item1_results.json (gate Item 1 numbers, verbatim copy) md5 3d6cb47faeea26552011b7bdb4d499ab |
| results/g35_item2.log | 0 | gate35/work/g35_item2.log (gate Item 2 run log, verbatim copy) md5 d41d8cd98f00b204e9800998ecf8427e |
| results/g35_item2_results.json | 13595 | gate35/work/g35_item2_results.json (gate Item 2 numbers, verbatim copy) md5 980577c5f44e9db7a5404f1f5c1e1332 |
| results/g35_item2_run.log | 2248 | gate35/work/g35_item2_run.log (gate Item 2 run log (replacement run), verbatim copy) md5 b66b459d657196b3710245f7e73ccff0 |
| sources/CHECKPOINT314.md | 3479 | phase314/CHECKPOINT314.md (phase record, verbatim copy) md5 646064021c19b27c6250092fa8155523 |
| sources/g35_item1_memo.md | 5013 | gate35/work/g35_item1_memo.md (gate Item 1 worker memo, verbatim copy) md5 09f6989b1e80955ee41b303ccd4d8ce4 |
| sources/g35_item2_memo.md | 6591 | gate35/work/g35_item2_memo.md (gate Item 2 worker memo, verbatim copy) md5 bce0b606b9534647fed8fdf300b9dae0 |
| sources/g35_registration.md | 7451 | gate35/work/g35_registration.md (gate registration, verbatim copy) md5 3dfce91d931f8113bf59ac19a8b2e6cf |
| sources/p312_memo.md | 18479 | phase312/results/p312_memo.md (phase worker memo (the member's background provenance), verbatim copy) md5 6436cf29d891017ce40f9a770c9a03f7 |
| sources/p314_confirmed.json | 48075 | phase314/results/p314_confirmed.json (the confirmed pointwise members, verbatim copy) md5 2af568d14030528f7c7b3b9378115224 |
| sources/p314_controls.json | 41093 | phase314/results/p314_controls.json (phase control output, verbatim copy) md5 98b90d8c735fedfa2b8c1197804cc943 |
| sources/p314_memo.md | 12168 | phase314/results/p314_memo.md (phase worker memo, verbatim copy) md5 20d91b2666b5a9440429e99b83be7e57 |
| sources/p314_opt_log.json | 3744 | phase314/results/p314_opt_log.json (phase optimisation log, verbatim copy) md5 e9b36662108231fbfeafd5f98cc8bac3 |
| sources/p314_results.json | 131266 | phase314/results/p314_results.json (phase numbers, verbatim copy) md5 2d51d61b1c6c408921f5adf1aac36a49 |
| sources/p314_screens.json | 49073 | phase314/results/p314_screens.json (phase screen record, verbatim copy) md5 bba3ab60bb64325966b2f85682428aa6 |

## Numbers check (every deciding number in Gate-35 §5's claim set, re-derived from the bundled results)

Source of truth for this section: the gate's own result files in
`results/` (byte-identical to `gate35/work/` originals, md5s
above) together with the bundled phase records in `sources/`.
Values below were transcribed from those files during packaging
— packaging copies, hashes, and transcribes only; no bundled
code was executed.

- **Continuum minimum +8.100317×10⁻⁵ at r = 20** — present in
  `results/g35_item1_results.json`.
- **Certified regional lower bounds +2.547705×10⁻⁴ /
  +1.167761×10⁻⁴ / +8.081922×10⁻⁵** — stored in
  `results/g35_item1_results.json` in float form
  (0.0002547705…, 0.00011677608503257706, 8.081922…e-05; the
  claim's prints are their roundings).
- **SET-244 ρ min +8.272455×10⁻⁵; 0/6642 negative** — present in
  `results/g35_item1_results.json`, `results/g35_item2_results.json`
  and `sources/p314_results.json`.
- **Depth −5.327659×10⁻⁴ (gate re-read −5.327658635240827×10⁻⁴)**
  — stored in `results/g35_item2_results.json` as
  0.0005327658635240827 in magnitude.
- **Type-I count 2615/6642** — recorded in
  `results/g35_item2_results.json`.
- **EC fence values (NEC min −1.170007×10⁻³, WEC min
  −1.044069×10⁻², DEC min −1.000003, SAMPLER-M)** — Phase 314's
  stored reads in `sources/p314_results.json`, carried into the
  claim set's fence by GATE35.md §5.

Checked: every deciding number in the §5 set — 0 unmatched.

## Assembly notes

- **Selection, stated:** from gate35/, the gate record and
  checkpoint, the four deciding code files, both items' result
  files and logs (filed under `results/`), and both item memos
  plus the registration (filed under `sources/`). From
  phase314/, the checkpoint and the full results set. From
  phase312/, the memo only (the member's background provenance;
  Phase 312's full record is bundled with the Gate-34 release,
  v1.25.0). The other four Phase 314 pointwise members were not
  attacked by this gate and no claim here covers them.
- No source file was edited; no bundled .py was executed and
  nothing was unpickled at any point in packaging.
