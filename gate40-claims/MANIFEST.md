# Gate-40 claims bundle - MANIFEST (release v1.31.0)

Every file in this folder, its size in bytes, and where it came from.
Copies are byte-for-byte copies of the named source (md5-verified at
assembly; every copy also cmp-verified against its source at assembly).
This manifest lists every file in the bundle except itself.

| file | bytes | source / traceability |
|---|---|---|
| GATE40.md | 19629 | gate40/GATE40.md (gate record, verbatim copy) md5 41046c28961f03ca23c846914ad78670 |
| RESULTS.md | 9052 | written for this bundle (the claim set: the GATE40.md §5 block verbatim — the only quotable form of the Phase 374 claim set; the §5 block in RESULTS.md was diff-verified character-for-character against GATE40.md §5 at assembly) |
| RELEASE_v1.31.0.md | 10193 | written for this bundle (release draft; the GATE40.md §5 claim set embedded verbatim, diff-verified against GATE40.md §5 at assembly; the disclosure paragraph in gate38-claims/RELEASE_v1.29.0.md's exact form; version DOI TBD — minted at release) |
| README_WHATSNEW_v1310.md | 3319 | written for this bundle (prepared README update; applied at upload) |
| code/g40_lib.py | 25180 | gate40/work/g40_lib.py (Gate-40's library — centre assembly, dwelling-waveform layer, time-dependent Einstein tensor from the metric, Eulerian-frame / Hawking–Ellis margins / SET-244 read path, adversary polish and worst-null, verbatim copy) md5 da4264f0c426a2247dece913b85dead1 |
| code/g40_members.py | 1777 | gate40/work/g40_members.py (Gate-40's registered member definitions, verbatim copy) md5 784a46411153344dda4cbefd1c9f8a8a |
| code/g40_calibrate.py | 5463 | gate40/work/g40_calibrate.py (Gate-40's calibration driver — C-1…C-8, run before any audit read, verbatim copy) md5 0cd304f4d5c2cfc2dbecd79234284922 |
| code/g40_audit.py | 4478 | gate40/work/g40_audit.py (Gate-40's audit driver — J = 32/64/128 audits and stationary scaled reads, verbatim copy) md5 0fed9b663786daa9cf8101ae442ea9ee |
| code/g40_confirm.py | 3300 | gate40/work/g40_confirm.py (Gate-40's confirmation driver — adversary polish and worst-null at the candidate worst instants, verbatim copy) md5 6fa5e4b5ae9a47eb00c830945419b1da |
| sources/CHECKPOINT374.md | 3767 | phase374/CHECKPOINT374.md (Phase 374's phase record — verdict, anatomy, verification state, verbatim copy) md5 22211ccfb6bd40cdd90216485c178c62 |
| sources/p374_memo.md | 16969 | phase374/results/p374_memo.md (Phase 374's worker memo — the claim set as filed, verbatim copy) md5 8254e61411916761aabeaf1ea5065754 |
| sources/g40_calibration.json | 3274 | gate40/results/g40_calibration.json (Gate-40's calibration record C-1…C-8, verbatim copy) md5 5c7268e83507423bb088e2ac0f8068ad |
| sources/g40_calibration_c7_full.json | 717 | gate40/results/g40_calibration_c7_full.json (Gate-40's full-precision C-7 record — the four Gate-39-verified Phase 364 champions against their full-precision stored values, verbatim copy) md5 b97a4ac188144a11f71e7ed0b4e0b450 |
| sources/g40_frame_admission.json | 504 | gate40/results/g40_frame_admission.json (Gate-40's frame-admission record — the laptop did not reproduce the anchor and was not admitted, verbatim copy) md5 b85ed199a54021f215e3d12f324104f3 |
| sources/g40_audit_summary_all.json | 9227 | gate40/results/g40_audit_summary_all.json (Gate-40's consolidated audit summary — all 17 members at J = 32 and J = 128, the two acceptance members at J = 64, verbatim copy) md5 b3e1e75b6ef5f582977cb1cd2cbf2fdb |
| sources/g40_numbers.json | 7290 | gate40/results/g40_numbers.json (Gate-40's numbers record — the bars, the J = 128 table, champion margins, acceptance statistics, period-lever steps, verbatim copy) md5 958fab5431ba791d5e93ac66da00aa99 |
| sources/g40_confirm.json | 11213 | gate40/results/g40_confirm.json (Gate-40's confirmation record — C2 polishes, per-instant worst-nulls, stationary scaled reads, the champion at φ = π, verbatim copy) md5 2dded0ff670c5ff96d3c0358e201b8a4 |

## Numbers check (every deciding number in the final set, transcribed from the bundled records)

Sources of truth for this section: the bundled gate record
`GATE40.md` (§§1–3, §5), the bundled Phase 374 records in
`sources/` (`CHECKPOINT374.md`, `p374_memo.md`), and Gate-40's
bundled result records in `sources/` (`g40_calibration.json`,
`g40_calibration_c7_full.json`, `g40_frame_admission.json`,
`g40_audit_summary_all.json`, `g40_numbers.json`,
`g40_confirm.json`). Values below were transcribed from those
files during packaging — packaging copies, hashes, and transcribes
only; no bundled code was executed and nothing was unpickled.
Spot-checks performed against the bundled JSON records at
assembly: the champion's deciding values and margins, the
corrected worst-null, the C1 global minimum and the restated
period-lever steps match `sources/g40_numbers.json` /
`sources/g40_confirm.json` digit-for-digit at the precision
printed there, and the stationary NEC anchor matches
`sources/g40_calibration.json`.

- **Stationary anchor (the bars)** — Phase 344's A2 centre reads,
  on the gate's machinery: NEC_stat = **−2.319453×10⁻⁴** (gate
  read −2.3194531327529972×10⁻⁴, diff −1.08×10⁻¹⁹, argmin
  r = 16.2195), DEC_stat = **−2.233693×10⁻⁴** (gate read
  −2.2336932044559813×10⁻⁴, diff +5.42×10⁻²⁰, argmin
  r = 19.3902) — `GATE40.md` §1 (C-3);
  `sources/g40_calibration.json`.
- **Champion (G40-A)** — SNM_a0.15_T640_D0.750_m0.88 at
  J = 128: NEC_worst = joint L_worst = **−2.099385×10⁻⁴** at
  φ = π (full precision −2.0993850795917056×10⁻⁴ in the gate's
  J = 128 table), DEC_worst = **−1.941081×10⁻⁴** at φ = π
  (−1.941081222390093×10⁻⁴). Margins: NEC over Phase 364's
  gate-verified level **+6.966286×10⁻⁶** (full precision
  +6.966285691067145×10⁻⁶); NEC over L_stat
  **+2.200681×10⁻⁵** (+2.2006805316129055×10⁻⁵) — the wall has
  moved 9.49% from stationary; DEC against Phase 364's DEC
  champion **−8.638217×10⁻⁶** (a REGRESSION, full precision
  −8.638216544706314×10⁻⁶), DEC over DEC_stat
  **+2.926120×10⁻⁵** (+2.926119820658888×10⁻⁵); C2 adversary
  polish passes at the worst instant (polished depth
  −1.693611×10⁻⁴, past the −0.0034 bar) — `GATE40.md` §2, §5;
  `sources/g40_numbers.json`, `sources/g40_confirm.json`.
- **The corrected worst-null (the gate's one correction to a
  deciding-adjacent figure)** — Phase 374's stored worst-null
  equality FAILS as stated: the SET NEC argmin is non-Type-I at
  all 24 candidate worst instants, and the true pointwise
  worst-nulls lie **2.69×10⁻⁹ … 1.36×10⁻⁶ BELOW** the stored
  values; champion, worst instant: SET value
  **−2.099385×10⁻⁴**, true worst-null **−2.099412×10⁻⁴**
  (−2.0994120250120935×10⁻⁴; the SET value less
  2.6945420387948418×10⁻⁹), itself beating Phase 364's level by
  **6.94×10⁻⁶** > tol = 1.0×10⁻⁶ — verdict relevance none —
  `GATE40.md` §2, §5; `sources/g40_confirm.json` (per-instant
  values).
- **Both-coordinates champion (G40-B)** —
  SNM_a0.30_T640_D0.750_m0.88 at J = 128: joint L_worst
  **−2.143888×10⁻⁴** (+2.516020×10⁻⁶ over Phase 364's level;
  full precision +2.5160195901779102×10⁻⁶), DEC_worst
  **−1.696387×10⁻⁴** (+1.583120×10⁻⁵ over Phase 364's DEC
  champion; full precision +1.5831197669564695×10⁻⁵); C2 passes
  at both worst instants — `GATE40.md` §2, §5;
  `sources/g40_numbers.json`.
- **Candidate set and C1 (G40-C)** — the gate's own J = 128
  audits yield exactly **12 of 16** candidates (the four
  a = 0.15 / m = 0.88, four a = 0.30 / m = 0.75 and four
  a = 0.30 / m = 0.88 members; the four non-candidates are
  exactly the a = 0.15 / m = 0.75 members, all still above
  L_stat); global min ρ = **+8.638077678074048×10⁻⁵** (the
  anchor's), ρ ≥ 0 at every audited instant, zero
  floor-infeasible instants across **2848 instant-reads** —
  `GATE40.md` §3, §5; `sources/g40_numbers.json`,
  `sources/g40_confirm.json` (`n_candidates_gate` = 12).
- **Acceptance** — side (i) |ΔL_worst| = **0.0** PASS;
  side (ii) |ΔL_best| = **1.753266×10⁻⁶** > 1.0×10⁻⁶ FAIL
  (full precision 1.753266081739929×10⁻⁶); the claim set stands
  on the registered consequence, re-executed in substance by
  the gate — `GATE40.md` §4; `sources/g40_numbers.json`.
- **Anatomy (G40-D, restated)** — the saturation identities are
  exact on gate machinery: the champion's worst instant is a
  bottom-dwell instant (μ = 1.1125, μ_dot = μ_ddot = 0.0) with
  L_worst = L_stat(1.1125) at diff **0.0**; DEC_worst =
  DEC_stat(bottom μ) for every member at max |diff| **0.0**, all
  DEC-worst instants at φ = π. Period lever, RESTATED (Phase
  374's §SS4.2 prose is ten times the true steps; its §SS3
  table is correct): T160→T320 **+3.160267×10⁻⁶**
  (+3.1602669967937776×10⁻⁶), T320→T640 **+1.752888×10⁻⁷**;
  the champion's T320→T640 gain **+7.905661×10⁻⁷**
  (+7.905661442960191×10⁻⁷); the a = 0.15 lift step (m 0.75 →
  0.875) **+7.278147×10⁻⁶** (+7.2781472376289025×10⁻⁶) —
  `GATE40.md` §3, §5; `sources/g40_numbers.json`,
  `sources/g40_confirm.json` (`champion_at_pi`).
- **Calibrations** — C-1 vectors max diff **0.0**; C-4 flat
  limit exactly **0.0**; C-5 μ ≡ 1 reduction ≤ **8.67×10⁻¹⁹**
  at all 32 instants; C-6 from-scratch FD path: relative
  agreement **2.505×10⁻⁶** (bar 1.0×10⁻³), agreeing with Phase
  374's own CTL-T2 figure to three digits; C-7: all four
  Gate-39-verified Phase 364 champions reproduce at
  ≤ **1.1×10⁻¹⁹**; frame admission: the laptop did NOT
  reproduce the anchor (max diff **8.31×10⁻⁶**, WEC — the
  pattern a sixth time) — every deciding read is a VM read.
  Max |gate − stored| over all compared audits and fields:
  **5.42×10⁻¹⁹** — `GATE40.md` §1;
  `sources/g40_calibration.json`,
  `sources/g40_frame_admission.json`,
  `sources/g40_numbers.json`.

Checked: every deciding number in the final set — 0 unmatched.

## Assembly notes

- **Selection, stated:** the gate record entire (`GATE40.md` —
  its §5 is the only quotable form of the set). From gate40/, the
  gate's machinery entire (five files in `code/` — Gate-40 ran
  its own computation, so this bundle carries the gate's code)
  and its deciding result records (in `sources/`: the
  calibration, C-7 full calibration, frame admission, audit
  summary, numbers and confirmation JSONs). From phase374/, the
  checkpoint and the worker memo — the phase's verdict records,
  carrying the claim set as filed. **Not bundled:** the 36
  per-audit checkpoint parts (`gate40/results/parts/` — resume
  checkpoints whose contents are consolidated in the bundled
  `g40_audit_summary_all.json`); Gate-40's run logs
  (`gate40/results/audit_run.log`, `confirm_run.log`); the
  `__pycache__` .pyc files under the gate work directory
  (compiled artefacts); Phase 374's own machinery,
  control/scan/refine/confirm/anchor JSONs and run logs (the
  gate judged Phase 374's records; its deciding values are
  carried in the bundled gate records); the stored Phase 344 A2
  centre files the gate's assembly reads (identified on the
  bundled code's face).
- The verbatim block embedded in the written files was
  diff-verified character-for-character at assembly: the
  GATE40.md §5 claim set in RESULTS.md and in
  RELEASE_v1.31.0.md — both checks exact. The disclosure
  paragraph in RELEASE_v1.31.0.md is in
  gate38-claims/RELEASE_v1.29.0.md's exact form.
- No source file was edited; no bundled .py was executed and
  nothing was unpickled at any point in packaging.
