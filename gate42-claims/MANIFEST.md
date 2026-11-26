# Gate-42 claims bundle - MANIFEST (release v1.33.0)

Every file in this folder, its size in bytes, and where it came from.
Copies are byte-for-byte copies of the named source (md5-verified at
assembly; every copy also cmp-verified against its source at assembly).
This manifest lists every file in the bundle except itself.

| file | bytes | source / traceability |
|---|---|---|
| GATE42.md | 18593 | gate42/GATE42.md (gate record, verbatim copy) md5 e8415fc89a05732ff41a774ac2475360 |
| RESULTS.md | 9323 | written for this bundle (the claim set: the GATE42.md §5 block verbatim — the only quotable form of the Phase 386 claim set; the §5 block in RESULTS.md was diff-verified character-for-character against GATE42.md §5 at assembly) |
| RELEASE_v1.33.0.md | 10450 | written for this bundle (release draft; the GATE42.md §5 claim set embedded verbatim, diff-verified against GATE42.md §5 at assembly; the disclosure paragraph in gate38-claims/RELEASE_v1.29.0.md's exact form; version DOI TBD — minted at release) |
| README_WHATSNEW_v1330.md | 3634 | written for this bundle (prepared README update; applied at upload) |
| code/g42_lib.py | 21688 | gate42/work/g42_lib.py (Gate-42's library — the gate's own graded builder, summary, legality, q-read and exact-min-null code, written from the construction registered in CHECKPOINT386, verbatim copy) md5 15853c3d008f098fc8c1565b9ecda543 |
| code/g42_controls.py | 5397 | gate42/work/g42_controls.py (Gate-42's controls driver — the hash gate, the builder reproduction against the stored chain reads, the anchors, verbatim copy) md5 b9550f3887a7800858ddd8dcb39a688a |
| code/g42_audits.py | 3709 | gate42/work/g42_audits.py (Gate-42's audit driver — the verdict-set audits of every claim subject at its legal rung and its failure bracket, verbatim copy) md5 270a61cdecb69090a337759752f41702 |
| code/g42_cg3.py | 1573 | gate42/work/g42_cg3.py (Gate-42's C-G3 cross-check driver — the exact-min-null ladder at the (0, 16.635, 0) point, verbatim copy) md5 5b5da50579b2331238f1e38e0a305191 |
| code/g42_screen.py | 4560 | gate42/work/g42_screen.py (Gate-42's screening driver — the recalibration on the gate's own FD screening instrument under both masks, verbatim copy) md5 7b74cf38348715a43d1b3c5a8a9ec408 |
| sources/CHECKPOINT386.md | 21865 | phase386/CHECKPOINT386.md (Phase 386's phase record — registration, verdict, anatomy, verification state, verbatim copy) md5 75d78122cdd22b6d68316984aba84ffb |
| sources/p386_memo.md | 10608 | phase386/results/p386_memo.md (Phase 386's worker memo — the claim set as filed, verbatim copy) md5 87362b457772356585bd1bacf556eb5a |
| sources/g42_controls.json | 6585 | gate42/results/g42_controls.json (Gate-42's controls record — the hash gate, the chain reads and their differences against the stored reads, the anchors, verbatim copy) md5 da49691f749a0317ddeecdf7b941398c |
| sources/g42_audits.json | 107417 | gate42/results/g42_audits.json (Gate-42's audits record — the full deciding audits of every subject, the chain reads, the vector hashes, the exclusion and distinctness checks, verbatim copy) md5 5d788e1bfef510ee0598b1c3524bb9e1 |
| sources/g42_cg3.json | 3703 | gate42/results/g42_cg3.json (Gate-42's C-G3 record — the twelve-row exact-min-null ladder at the cross-check point, verbatim copy) md5 762a9a20ca4b7b4089b04fedadd9848b |
| sources/g42_screen.json | 1382 | gate42/results/g42_screen.json (Gate-42's screening record — the registered-set recalibration under both masks, verbatim copy) md5 f784e2803100b7551d811ad3dcb748fa |
| sources/g42_screen_dense_variant.json | 1393 | gate42/results/g42_screen_dense_variant.json (Gate-42's screening density cross-check — the 209-radii variant returning the same four β_crit values, verbatim copy) md5 495a6f11c088c1451c0f35cf395c70d3 |

## Numbers check (every deciding number in the final set, transcribed from the bundled records)

Sources of truth for this section: the bundled gate record
`GATE42.md` (§§1–5), the bundled Phase 386 records in
`sources/` (`CHECKPOINT386.md`, `p386_memo.md`), and Gate-42's
bundled result records in `sources/` (`g42_controls.json`,
`g42_audits.json`, `g42_cg3.json`, `g42_screen.json`,
`g42_screen_dense_variant.json`). Values below were transcribed
from those files during packaging — packaging copies, hashes, and
transcribes only; no bundled code was executed and nothing was
unpickled. Spot-checks performed against the bundled JSON records
at assembly: every subject's deciding audit values at its legal
rung and its failure bracket, the full twelve-row C-G3 ladder, the
screening β_crit values under both masks (registered and dense
sets), and every vector hash match `sources/g42_audits.json`,
`sources/g42_cg3.json` and `sources/g42_screen.json`
digit-for-digit at the precision printed there.

- **Hash gate (C-1)** — all three stored copies of Procaccia's
  design vector hash to the published figshare SHA-256
  `a8814dfb…d74a` (record:
  a8814dfb6273956da9656379a8dd887218ecc28cbafb03fc87f980c07510d74a),
  `all_match = True`. Claim-subject vector hashes: S1
  `84c9043e…2068`, S2 `29af1376…27cf`, S3 `87df3cfe…996`,
  Rank-1 `d1efd424…5418` — gate-computed and stored values
  identical (`all_stored_match = True`); the Stage-1 champion
  `2c14cbca…dbed` matches none of them
  (`champion_in_claim_set = False`); the claim set's audited
  subjects are exactly {S1, S2, S3} plus the separately filed
  Rank-1; S1 and Rank-1 are distinct (max |Δy|∞ =
  0.4741898849746842) — `GATE42.md` §1 (C-1);
  `sources/g42_controls.json`, `sources/g42_audits.json`.
- **Construction reproduction (C-2)** — the gate builder's c = 0
  chain reads reproduce the phase builder's stored graded reads
  at float64 roundoff (relative differences: M 2.91×10⁻¹⁶,
  ρ_max 6.71×10⁻¹⁶, λ 1.40×10⁻¹⁵, k 4.58×10⁻¹⁶, ∫F/r²
  4.30×10⁻¹⁶, a(R_in) 5.70×10⁻¹⁶ — all ≤ 1.4×10⁻¹⁵) and the step
  builder's stored reads at ρ_max **3.99×10⁻¹²**, λ
  **2.07×10⁻¹¹**, k **8.70×10⁻¹²** — the phase's own C-G1
  figures; against the paper's §3 enclosures ≤ 2.7×10⁻⁸;
  construction grid count 1,200,671 exact — `GATE42.md` §1
  (C-2); `sources/g42_controls.json`.
- **The step member at β = 0.1363 (G42-A)** — through the graded
  factory, fully legal under the common bars at h = 0.0375:
  worst margin SEC **+3.404178×10⁻⁷** at r = 5.0 (record
  3.404177926256379×10⁻⁷), **109.5× the FD floor**, Type-I
  fraction 1.000 over 988 significant points, sampled-NEC min
  +8.585×10⁻⁸, NEC/WEC minima +5.007667×10⁻⁷, DEC min
  +4.290249×10⁻⁷; second path (audit4) worst +3.396×10⁻⁷;
  h = 0.01875 concurs (+3.397875×10⁻⁷); ratio **1.000** to
  Gate-7's stored read — `GATE42.md` §2;
  `sources/g42_audits.json` (`subjects.y_his`).
- **The C-G3 cross-check ladder (G42-A's disclosure)** — exact
  min-null at (0, 16.635, 0), SLSQP and the Lagrange secular
  solve agreeing to ~10⁻¹⁵ on every row: at β = 0.1364, wa
  **+7.4645×10⁻⁸ Type-I** at h = 0.0375 (the disclosed flip,
  reproduced exactly), −8.1794×10⁻⁸ at h = 0.01875,
  −1.1821×10⁻⁷ at h = 0.009375; audit4 −2.0027×10⁻⁷ /
  −1.3394×10⁻⁷ / **−1.3035×10⁻⁷** (0.17% from Procaccia's
  stored −1.30135×10⁻⁷). At β = 0.1363, wa +2.5651×10⁻⁷ /
  +1.0020×10⁻⁷ / +6.3809×10⁻⁸; audit4 **−1.8183×10⁻⁸** at
  h = 0.0375 (the gate's symmetric marginal), +4.8094×10⁻⁸ /
  +5.1680×10⁻⁸ (the finest matching Gate-7's stored
  +5.3×10⁻⁸) — `GATE42.md` §1 (C-5);
  `sources/g42_cg3.json` (all twelve rows).
- **S1 (G42-B)** — at β = 0.18671875, h = 0.0375: FULLY LEGAL —
  worst SEC **+3.971325×10⁻⁷** at r = 3.75 (record
  3.971324866805713×10⁻⁷), **123.0× the FD floor**, Type-I
  1.000 (1,066 significant), NEC/WEC/DEC minima
  +4.724565×10⁻⁷, shell sampled-NEC min +1.784×10⁻⁷ (gate
  sampling; phase stored +1.671×10⁻⁷ — the C-6 convention
  note), audit4 worst +3.967×10⁻⁷, q_max 0.9945 at r = 16.4
  (phase stored 0.9974 — C-6); h = 0.01875 concurs
  (+3.968024×10⁻⁷, 129.3× floor). At β = 0.19171875 it FAILS:
  SEC **−2.673018×10⁻⁵** at r = 9.75, Type-I 0.9559 —
  `GATE42.md` §3; `sources/g42_audits.json` (`subjects.S1`).
- **Rank-1 (G42-B)** — at β = 0.18671875, h = 0.0375: FULLY
  LEGAL — worst SEC **+2.252869×10⁻⁷** at r = 7.0 (record
  2.252869307890705×10⁻⁷), **64.9× the FD floor**, Type-I
  1.000, NEC/WEC/DEC +4.907537×10⁻⁷, audit4 worst
  +2.037367×10⁻⁷, q_max 0.9956 at r = 21.0; h = 0.01875
  concurs (+2.091261×10⁻⁷). At β = 0.1875 it FAILS: SEC
  **−3.630506×10⁻⁶** at r = 9.75, Type-I 0.9981 —
  `GATE42.md` §3; `sources/g42_audits.json`
  (`subjects.rank1`).
- **The ladder (G42-C)** — S3 (grading alone) legal at
  0.1515625: worst DEC **+4.649873×10⁻⁷**, Type-I 1.000;
  fails at 0.1565625 (SEC −1.337570×10⁻⁵, Type-I 0.9939). S2
  (joint Powell) legal at 0.16640625: worst SEC
  **+1.650946×10⁻⁷**, Type-I 1.000; fails at 0.17140625
  (SEC −1.124156×10⁻⁵, Type-I 0.9837). S1 and Rank-1 legal at
  0.18671875 (above); the step member at 0.1363 (above) —
  `GATE42.md` §4 (e); `sources/g42_audits.json`
  (`subjects.S3`, `subjects.S2`).
- **The artefact (G42-D)** — the Stage-1 champion illegal at
  β = 0.1363 on gate machinery: worst SEC
  **−7.042941×10⁻⁶** at r = 7.0 (record
  −7.042941002760425×10⁻⁶), Type-I fraction **0.9644**, both
  spacings, audit4 concurring (−7.097×10⁻⁶); illegal at
  0.17422 (SEC −6.342114×10⁻⁵ at r = 9.0, Type-I 0.8912);
  all binding sites at r ≤ 9.0, below the old core mask's
  9.25 floor. Recalibration on the gate's own FD screening
  instrument (98 radii, 2,470 points inside the extended
  mask, matching the phase's stored set size exactly):
  β_crit(y_his) = **0.136328125** under BOTH masks; the
  champion reads **0.174609375** under the old mask
  [9.25, 27.27] and **0.120703125** under the extended mask
  [R_in − 0.5, R_out], brackets identical to the stored
  recalibration; the denser 209-radii variant returns the
  same four β_crit values — `GATE42.md` §4 (d);
  `sources/g42_audits.json` (`subjects.champion`),
  `sources/g42_screen.json`,
  `sources/g42_screen_dense_variant.json`.
- **Diagnostic conventions (C-6, disclosed, non-deciding)** —
  shell sampled-NEC minima: gate S1 +1.784×10⁻⁷, Rank-1
  +2.369×10⁻⁷; phase +1.671×10⁻⁷, +2.790×10⁻⁷; S1 q_max gate
  0.9945 vs phase 0.9974, same site r = 16.4; three
  162-direction samplings of the gate's tensor at the
  flat-valley fringe point (r = 23.0) give 1.72 / 1.78 /
  2.16×10⁻⁷, a dense sampling 1.226×10⁻⁷, the exact min-null
  +1.218×10⁻⁷ — the phase's value sits inside the sampling
  spread; every eigenvalue margin agrees with the stored
  reads to ~10⁻¹³; all bars involving these diagnostics
  (sampled-NEC > 0, q_max < 1) pass under every sampling —
  `GATE42.md` §1 (C-6).

Checked: every deciding number in the final set — 0 unmatched.

## Assembly notes

- **Selection, stated:** the gate record entire (`GATE42.md` —
  its §5 is the only quotable form of the set). From gate42/, the
  gate's machinery entire (five files in `code/` — Gate-42 ran
  its own computation, so this bundle carries the gate's code)
  and its deciding result records (in `sources/`: the controls,
  audits, C-G3 cross-check and both screening JSONs). From
  phase386/, the checkpoint and the worker memo — the phase's
  verdict records, carrying the claim set as filed.
  **Not bundled:** Phase 386's own machinery and its
  control/search/verdict JSONs, pool state files and logs (the
  gate judged Phase 386's records; its deciding values are
  carried in the bundled gate records); the `__pycache__`
  .pyc files under the gate work directory (compiled artefacts);
  the stored design vectors and the registered tensor
  instruments the gate's code reads (identified on the bundled
  code's face).
- The verbatim block embedded in the written files was
  diff-verified character-for-character at assembly: the
  GATE42.md §5 claim set in RESULTS.md and in
  RELEASE_v1.33.0.md — both checks exact. The disclosure
  paragraph in RELEASE_v1.33.0.md is in
  gate38-claims/RELEASE_v1.29.0.md's exact form.
- No source file was edited; no bundled .py was executed and
  nothing was unpickled at any point in packaging.
