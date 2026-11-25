# Gate-36 claims bundle - MANIFEST (release v1.28.0)

Every file in this folder, its size in bytes, and where it came from.
Copies are byte-for-byte copies of the named source (md5-verified at
assembly; every copy also cmp-verified against its source at assembly).
This manifest lists every file in the bundle except itself.

| file | bytes | source / traceability |
|---|---|---|
| GATE36.md | 17332 | gate36/GATE36.md (gate record, verbatim copy) md5 f8d7935a53cbe26a5778ed21f374aae4 |
| CHECKPOINT_GATE36.md | 5917 | gate36/CHECKPOINT_GATE36.md (gate checkpoint, verbatim copy) md5 2d991afdc88d9de4f012a77f7f94c49e |
| RESULTS.md | 6538 | written for this bundle (G36-A/B/C, in Gate-36 §5's wording, verbatim — the only quotable form of the mating claims; the §5 claim quotes and fences in RESULTS.md were verified character-for-character in substance against GATE36.md §5 at assembly) |
| RELEASE_v1.28.0.md | 7237 | written for this bundle (release draft; version DOI TBD — minted at release) |
| README_WHATSNEW_v1280.md | 3500 | written for this bundle (prepared README update; applied at upload) |
| code/g36_lib.py | 15862 | gate36/work/g36_lib.py (gate target-assembly library (own symbolic-jet Einstein tensor, ADM tetrad, worst-null/Segre machinery), verbatim copy) md5 8dbc1605d0019cf9e5e5755a22caab36 |
| code/g36_item1.py | 5816 | gate36/work/g36_item1.py (gate Item 1 driver (targets and controls CTRL-T1/T2), verbatim copy) md5 a999f9598ac755788c710840ad1e903e |
| code/g36_spinor.py | 9332 | gate36/work/g36_spinor.py (gate spinor builder (direct definitional path + pairwise fast path), verbatim copy) md5 97ac46bb3d4074283893d29613538523 |
| code/g36_item2.py | 13720 | gate36/work/g36_item2.py (gate Item 2 driver (independent ladder, Jacobians, perturbation ladder), verbatim copy) md5 ea543b470f75e61672c1ad3c7fe43d2a |
| code/g36_item2_recover.py | 3070 | gate36/work/g36_item2_recover.py (gate Item 2 recovery script (checkpoint-gated tail completion after the VM restart), verbatim copy) md5 a166d48255d05e4aa0ed2059436df933 |
| code/g36_item3.py | 11788 | gate36/work/g36_item3.py (gate Item 3 driver (σ_min censuses, optimiser/recipe variation, scale probe), verbatim copy) md5 a6f443790c467e138412957260223130 |
| results/g36_item1_results.json | 20386 | gate36/work/g36_item1_results.json (the gate's Item 1 deciding record (target reads, CTRL-T1/T2), verbatim copy) md5 6bb2014c7e06b6040f274913368aff25 |
| results/g36_item2_results.json | 24653 | gate36/work/g36_item2_results.json (the gate's Item 2 deciding record (controls CTRL-S1/S2/S3, ladder, best solution, perturbation ladder, recovery disclosure), verbatim copy) md5 49b470da344fe068eb7945e7f777a2fd |
| results/g36_item2_solutions.json | 3922 | gate36/work/g36_item2_solutions.json (the gate's Item 2 solution record, verbatim copy) md5 a2ef363b9223d8864e42e885c0a16b6f |
| results/g36_item2_run.log | 1876 | gate36/work/g36_item2_run.log (gate Item 2 run log (the executed run, killed by the VM restart mid-ladder), verbatim copy) md5 cdeff975035b752b2656d5597b62dffa |
| results/g36_item2_recover.log | 472 | gate36/work/g36_item2_recover.log (gate Item 2 recovery log, verbatim copy) md5 ce2cbdb89e3355d1922abff07a88e6b8 |
| results/g36_item3_results.json | 25506 | gate36/work/g36_item3_results.json (the gate's Item 3 deciding record (both censuses, E3/E4/E5 experiments, attribution), verbatim copy) md5 a9e36bf5d74227541158186b9517306e |
| results/g36_item3_solutions.json | 12638 | gate36/work/g36_item3_solutions.json (the gate's Item 3 census solution record, verbatim copy) md5 a9b6f149069f7df87ab7cea688962548 |
| results/g36_item3_run.log | 2242 | gate36/work/g36_item3_run.log (gate Item 3 run log, verbatim copy) md5 1245a4675eac1ef7021d95a114741659 |
| sources/g36_registration.md | 9490 | gate36/work/g36_registration.md (gate registration, written before computation, incl. Item 3's attribution decision tree, verbatim copy) md5 f8147de68c50eb91ba9d626bb9b02868 |
| sources/g36_item1_memo.md | 4818 | gate36/work/g36_item1_memo.md (gate Item 1 worker memo, verbatim copy) md5 01bf57357cac145724cfe057d1cf1053 |
| sources/g36_item2_memo.md | 7502 | gate36/work/g36_item2_memo.md (gate Item 2 worker memo, verbatim copy) md5 ce53f84d65a6419e53cbc4c283dbd06c |
| sources/g36_item3_memo.md | 9993 | gate36/work/g36_item3_memo.md (gate Item 3 worker memo, verbatim copy) md5 e69c2c26f530a108624a0535b2b62d2f |
| sources/CHECKPOINT320.md | 9502 | phase320/CHECKPOINT320.md (phase record, verbatim copy) md5 bf73b374415386fc530cfdbace73b8d6 |
| sources/p320_memo.md | 13876 | phase320/results/p320_memo.md (phase worker memo (the match at positive density), verbatim copy) md5 5de0b4d8d7959de5d7b235a1edb00967 |
| sources/p320_results.json | 34012 | phase320/results/p320_results.json (Phase 320's deciding results record (ladder, winning fit, residuals), verbatim copy) md5 8ca0c98fc9ba2cef9259fd6a29f93824 |
| sources/p320_check_results.json | 1273 | phase320/results/p320_check_results.json (Phase 320's independent checker record (all deciding numbers reproduced at diff 0.0), verbatim copy) md5 1b0345fdd02609141e0bd6bd40ea2b71 |
| sources/p320_registration.md | 16047 | phase320/work/p320_registration.md (phase registration (verdict forms fixed before computation), verbatim copy) md5 1da67dfb7ace5fdec7758476e014fb7f |
| sources/p320_targets.json | 6491 | phase320/work/p320_targets.json (the stored target tensors at the four binding sites — the data CTRL-S1 fits against; carries the stored transverse eigh gauge of Gate-36 §2's record note, verbatim copy) md5 a51f12ce1bbea790232a970d6762bab1 |
| sources/p320_joint_bestfit.json | 4083 | phase320/work/p320_joint_bestfit.json (Phase 320's winning configuration (the reported solution, σ_min = 3.994×10⁻⁴), verbatim copy) md5 b4c9ed75b7d6a0c69acf8256c74bd05a |
| sources/p320_best_N4.json | 1176 | phase320/work/p320_best_N4.json (Phase 320's best N = 4 fit record, verbatim copy) md5 6d8a85d27b36350d5d9c00818cf71442 |
| sources/p320_best_N5.json | 1385 | phase320/work/p320_best_N5.json (Phase 320's best N = 5 fit record, verbatim copy) md5 7699eed4481e477be1a32686bc2e1712 |
| sources/p320_best_N6.json | 1610 | phase320/work/p320_best_N6.json (Phase 320's best N = 6 fit record, verbatim copy) md5 706d592c413e5456280f6ae8ca51ff6a |
| sources/p320_best_N8.json | 2035 | phase320/work/p320_best_N8.json (Phase 320's best N = 8 fit record, verbatim copy) md5 7959d889af9f315b51d0e3aac5d84472 |
| sources/p320_best_N12.json | 2896 | phase320/work/p320_best_N12.json (Phase 320's best N = 12 fit record, verbatim copy) md5 17c0f5e899cf7b4fbc25e70edc6b2728 |

## Numbers check (every deciding number in Gate-36 §5's claim set, re-derived from the bundled records)

Sources of truth for this section: `results/g36_item1_results.json`,
`results/g36_item2_results.json` and `results/g36_item3_results.json`
(the gate's own deciding records), cross-read against the bundled
phase record in `sources/` (`p320_results.json`,
`p320_check_results.json`). Values below were transcribed from those
files during packaging — packaging copies, hashes, and transcribes
only; no bundled code was executed and nothing was unpickled.

- **Phase 320's fit: residuals ≤ 8.231×10⁻¹⁴ against the 1×10⁻⁹
  bar** — `sources/p320_results.json` (max residual stored as
  8.231e-14); the same value is carried in
  `sources/p320_check_results.json`'s reproduction at diff 0.0.
- **Gate-36's independent fits: best N = 6 max R =
  1.1280204516520184×10⁻¹³** — `results/g36_item2_results.json`;
  the N = 4 / N = 5 rungs stall (5.523×10⁻⁴ / 5.806×10⁻⁵, 0 at bar)
  and N = 8 closes (4.054×10⁻¹², 4/4) in the same record — the
  counting-threshold transition of G36-A.
- **Densities at the match (G36-B): +6.263182×10⁻⁴ /
  +6.818808×10⁻⁴ / +6.257630×10⁻⁴ / +1.172278×10⁻⁴ at S1/S2/S3/S4**
  — stored in `results/g36_item1_results.json` as 0.0006263182… /
  0.0006818808… / 0.0006257630… / 0.00011722775…; the gate's
  re-derivation of the target densities sits at ≤ 1.27×10⁻¹⁵
  relative (the S2 entry) in the same record (CTRL-T1).
- **σ_min at Phase 320's reported solution = 3.994300×10⁻⁴** —
  `results/g36_item2_results.json` (stored 0.00039943001…, with
  σ_max = 3.909267×10³ class and rank 40 in the same record,
  CTRL-S1) and confirmed again in `results/g36_item3_results.json`
  (0.0003994299965922211 at the warm solution).
- **Census (G36-C): pointwise target — 5 solutions, σ_min =
  3.994×10⁻⁴ … 4.941×10⁻², median 6.879×10⁻³** —
  `results/g36_item3_results.json` carries the census entries
  0.0003994062616228799 (the ×4-scaled warm probe, 3.994063×10⁻⁴),
  0.003813788924756437 (3.813789×10⁻³), 0.006878744…
  (median 6.879×10⁻³), 0.046175974… (4.617597×10⁻²) and
  0.049405916… (4.940592×10⁻²); the weaker winner's census spans
  1.43×10⁻³ … 2.85×10⁻² (median 1.26×10⁻²) in the same record.
- **Perturbation ladder (G36-C): bar re-achieved at every rung,
  best max R ≤ 7.3×10⁻¹³ at ε = 1×10⁻⁴** —
  `results/g36_item2_results.json` (rung values stored, max
  7.332624766361005×10⁻¹³ at the ε = 1×10⁻⁹ rung; the ε = 1×10⁻⁴
  rung reads 2.089×10⁻¹³ / 2.340×10⁻¹⁴ as GATE36.md §3 states).

Checked: every deciding number in the §5 set — 0 unmatched.

## Assembly notes

- **Selection, stated:** from gate36/, the gate record and the gate
  checkpoint entire, and the gate's own machinery entire (target
  library, both item drivers, the spinor builder, the Item 2
  recovery script, and the Item 3 driver), its deciding records
  (Item 1/2/3 results and solutions JSONs and the Item 2/3 run
  logs, including the recovery log), and its registration and item
  memos. From phase320/, the checkpoint, the memo, the
  registration, the deciding results and checker records, the
  stored targets, the winning configuration, and the per-N best-fit
  records (N = 4, 5, 6, 8, 12) the ladder claims rest on.
  **Not bundled:** Gate-36's per-arm Item 2 checkpoint JSONs
  (`g36_item2_arm_*.json`, 16 files — intermediate per-arm
  checkpoints whose content is consolidated in
  `results/g36_item2_results.json` and
  `results/g36_item2_solutions.json`, both bundled); Phase 320's
  engine/run code and run/recovery logs (the gate judged the
  phase's records and results; the deciding re-derivation
  machinery is the gate's own, bundled in `code/`) and its
  executed-run backup JSON (`p320_results_executed_run_backup.json`
  — a backup of the bundled `p320_results.json` record); the
  `__pycache__` .pyc files under gate36/work/ and phase320/work/
  (compiled artefacts; their sources are bundled).
- No source file was edited; no bundled .py was executed and
  nothing was unpickled at any point in packaging.
