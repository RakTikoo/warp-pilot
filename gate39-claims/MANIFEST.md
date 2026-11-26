# Gate-39 claims bundle - MANIFEST (release v1.30.0)

Every file in this folder, its size in bytes, and where it came from.
Copies are byte-for-byte copies of the named source (md5-verified at
assembly; every copy also cmp-verified against its source at assembly).
This manifest lists every file in the bundle except itself.

| file | bytes | source / traceability |
|---|---|---|
| GATE39.md | 16208 | gate39/GATE39.md (gate record, verbatim copy) md5 52d960a20133a90baf4afa0226be9b18 |
| RESULTS.md | 7172 | written for this bundle (the claim set: the GATE39.md §5 block verbatim — the only quotable form of the Phase 364 claim set; the §5 block in RESULTS.md was diff-verified character-for-character against GATE39.md §5 at assembly) |
| RELEASE_v1.30.0.md | 7867 | written for this bundle (release draft; the GATE39.md §5 claim set embedded verbatim, diff-verified against GATE39.md §5 at assembly; the disclosure paragraph in gate38-claims/RELEASE_v1.29.0.md's exact form; version DOI TBD — minted at release) |
| README_WHATSNEW_v1300.md | 2503 | written for this bundle (prepared README update; applied at upload) |
| code/g39_lib.py | 30453 | gate39/work/g39_lib.py (Gate-39's library — centre assembly, dwelling-waveform layer, time-dependent Einstein tensor from the metric, Eulerian-frame / Hawking–Ellis margins / SET-244 read path, adversary polish and worst-null, verbatim copy) md5 9b235a7ba0db8037010b1aab1206f575 |
| code/g39_members.py | 3231 | gate39/work/g39_members.py (Gate-39's registered member definitions, verbatim copy) md5 0100568a5f5125fd20f52480f6e1911c |
| code/g39_calibrate.py | 11269 | gate39/work/g39_calibrate.py (Gate-39's calibration driver — C-1…C-8, run before any audit read, verbatim copy) md5 53b569fadd9838225a78b7036dcf569f |
| code/g39_scan.py | 1674 | gate39/work/g39_scan.py (Gate-39's J = 32 scan driver, verbatim copy) md5 02f7cd0911209509cbb21d1d5254e62c |
| code/g39_refine.py | 1721 | gate39/work/g39_refine.py (Gate-39's J = 64/128 refinement driver, verbatim copy) md5 952847a325ca5c10538ca84fc5425c38 |
| code/g39_confirm.py | 4565 | gate39/work/g39_confirm.py (Gate-39's confirmation driver — adversary polish and worst-null at the worst instants, verbatim copy) md5 bba72c59517fecc8553c5eb5979e6253 |
| sources/CHECKPOINT364.md | 4309 | phase364/CHECKPOINT364.md (Phase 364's phase record — verdict, anatomy, verification state, verbatim copy) md5 69433c288618ee6538a13b9d7d17f24c |
| sources/p364_memo.md | 15078 | phase364/results/p364_memo.md (Phase 364's worker memo — the claim set as filed, with Amendments 1–2 disclosed on its face, verbatim copy) md5 2d467ac5e19235af6387ffb2a5847962 |
| sources/g39_calibration.json | 9171 | gate39/results/g39_calibration.json (Gate-39's calibration record C-1…C-8, verbatim copy) md5 276ffe0dfd92a9ecba00dcad877457dc |
| sources/g39_scan.json | 691040 | gate39/results/g39_scan.json (Gate-39's full 37-member J = 32 scan record, verbatim copy) md5 f507e68ac7739331d3a658b89aace74e |
| sources/g39_refine.json | 568955 | gate39/results/g39_refine.json (Gate-39's J = 64/128 refinement record for the five registered members, verbatim copy) md5 0621a27fc14b7c996f58abed1b9b7985 |
| sources/g39_confirm.json | 46094 | gate39/results/g39_confirm.json (Gate-39's confirmation record — C2 polishes and the per-instant worst-null diffs of GATE39.md §2, verbatim copy) md5 dce6ac244d62d3fb2f5e20c876c79395 |
| sources/g39_worker_memo.md | 15050 | gate39/results/g39_worker_memo.md (Gate-39 worker's full numbers memo, including the complete diffs table vs Phase 364's stored record, verbatim copy) md5 e380ef852b96c6e0c7e655ecaeee55e8 |

## Numbers check (every deciding number in the final set, transcribed from the bundled records)

Sources of truth for this section: the bundled gate record
`GATE39.md` (§§1–3, §5), the bundled Phase 364 records in
`sources/` (`CHECKPOINT364.md`, `p364_memo.md`), and Gate-39's
bundled result records in `sources/` (`g39_calibration.json`,
`g39_scan.json`, `g39_refine.json`, `g39_confirm.json`,
`g39_worker_memo.md`). Values below were transcribed from those
files during packaging — packaging copies, hashes, and transcribes
only; no bundled code was executed and nothing was unpickled.
Spot-checks performed against the bundled JSON records at
assembly: the corrected worst-null and the C1 global minimum match
`sources/g39_confirm.json` / `sources/g39_scan.json` digit-for-digit
at the precision printed there, and the stationary NEC anchor
matches `sources/g39_calibration.json`.

- **Stationary anchor (the bars)** — Phase 344's A2 centre reads,
  on the gate's machinery: NEC_stat = **−2.319453×10⁻⁴** (gate
  read −2.319453132752996×10⁻⁴, diff −1.08×10⁻¹⁹, argmin
  r = 16.2195), DEC_stat = **−2.233693×10⁻⁴** (gate read
  −2.2336932044559818×10⁻⁴, diff +5.42×10⁻²⁰, argmin
  r = 19.3902); polished depth −2.2644422911711972×10⁻⁴ at
  r = 12.2330 (diff +4.34×10⁻¹⁹) — `GATE39.md` §1 (C-3);
  `sources/g39_calibration.json`.
- **Best member (G39-A)** — SNM_a0.30_T160_D0.750_m0.75 at
  J = 128: NEC_worst = **−2.169048×10⁻⁴** at φ = 2.9943 (margin
  over NEC_stat **+1.504×10⁻⁵**; full precision
  +1.5040519625061802×10⁻⁵; diff vs stored −1.08×10⁻¹⁹),
  DEC_worst = **−1.854699×10⁻⁴** at φ = π (margin over DEC_stat
  **+3.790×10⁻⁵**; full precision +3.789941475129525×10⁻⁵; diff
  +5.42×10⁻²⁰); C2 adversary polish passes at both worst
  instants (polished depths inside −1.496774×10⁻⁴ …
  −1.935726×10⁻⁴, agreeing with the stored C2 depths to
  ≤ 1.2×10⁻¹⁸, all past the −0.0034 bar) — `GATE39.md` §2, §5.
- **The corrected worst-null (the gate's one correction to a
  deciding-adjacent figure)** — Phase 364's stored worst-null
  equality FAILS as stated: the true pointwise worst-nulls lie
  **2.82×10⁻⁹ … 4.15×10⁻⁷ BELOW** the stored values at all eight
  instants; best member, NEC-worst instant: SET value
  **−2.169047936502378×10⁻⁴**, true worst-null
  **−2.1700111452323573×10⁻⁴** (the SET value less 9.63×10⁻⁸),
  itself beating NEC_stat by **1.494×10⁻⁵** > tol = 1.0×10⁻⁶ —
  verdict relevance none — `GATE39.md` §2, §5;
  `sources/g39_confirm.json` (per-instant diffs).
- **Four-member set (G39-B)** — all at T = 160, D = 0.75,
  m = 0.75, J = 128, every deciding value at roundoff of the
  stored record (diffs ≤ 8.1×10⁻²⁰): SNM_a0.30 NEC_worst
  −2.169048×10⁻⁴ (+1.504×10⁻⁵) / DEC_worst −1.854699×10⁻⁴
  (+3.790×10⁻⁵); M_a0.30 NEC_worst −2.224589×10⁻⁴
  (+9.486×10⁻⁶) / DEC_worst −1.854699×10⁻⁴ (+3.790×10⁻⁵);
  SNM_a0.15 NEC_worst −2.256428×10⁻⁴ (+6.303×10⁻⁶) /
  DEC_worst −2.032703×10⁻⁴ (+2.010×10⁻⁵); M_a0.15 NEC_worst
  −2.272118×10⁻⁴ (+4.734×10⁻⁶) / DEC_worst −2.032703×10⁻⁴
  (+2.010×10⁻⁵); every member's DEC-worst instant at φ = π;
  min ρ over all audited instants ≥ **+8.7246×10⁻⁵**; zero
  floor-infeasible instants; C2 passes at all eight worst
  instants; the smallest margin (M_a0.15 NEC, +4.734×10⁻⁶)
  exceeds tol = 1.0×10⁻⁶ by 4.7× — `GATE39.md` §2, §5.
- **C1 (G39-C)** — global min ρ = **+5.94490273097585×10⁻⁵** at
  SNM_a0.30_T40_D0.875_m0.00 (diff −1.5×10⁻¹⁹ vs the stored
  full-precision value), ρ ≥ 0 at every audited instant, zero
  floor-infeasible instants across **2144 instant-reads**
  (37 members × J = 32, five refinement members at J = 64/128,
  eight confirmation polishes) — `GATE39.md` §§1, 3, 5;
  `sources/g39_scan.json`.
- **Refinement acceptance** — |L_worst(128) − L_worst(64)| =
  **8.943221597361255×10⁻⁷** ≤ 1.0×10⁻⁶ for the best member;
  |L_best(128) − L_best(64)| = 0.0 — PASSED; the full-scan
  J = 128 consequence is not triggered — `GATE39.md` §1;
  `sources/g39_refine.json`.
- **Anatomy (G39-D, restated)** — Arm 1 (pure dwell, symmetric
  range m = 0, 24 members): every member's worst instant is
  DEC-saturated, DEC_worst in **−1.000001 … −1.000214**, DEC
  carrying L_worst. The winners' DEC-worst instant is the
  quasi-stationary bottom φ = π (all four, J = 128), and the
  bottom-point identity is exact: each winner's DEC_worst
  equals the stationary DEC minimum of the centre scaled by the
  constant bottom μ (**1.15** at a = 0.30, **1.075** at
  a = 0.15), both subsets, to ≤ 1×10⁻¹⁹. Period tax, RESTATED:
  the four T = 40 m = 0.75 members fall short of L_stat by
  **1.68×10⁻⁴ … 3.88×10⁻⁴** (SNM_a0.15 1.678×10⁻⁴; M_a0.15
  1.924×10⁻⁴; SNM_a0.30 2.646×10⁻⁴; M_a0.30 3.875×10⁻⁴) —
  Phase 364's "2–4×10⁻⁴" is the right scale but not the exact
  range — `GATE39.md` §3, §5.
- **Calibrations** — sympy generic-algebra check of the gate's
  tensor: max abs diff **3.47×10⁻¹⁸**; from-scratch FD path:
  relative agreement **1.21×10⁻⁷** (bar 1.0×10⁻³); flat limit
  exactly **0.0**; μ ≡ 1 reduction ≤ **8.67×10⁻¹⁹** at all 32
  instants; sinusoidal cross-check vs Phase 349's stored values
  ≤ **1.1×10⁻¹⁹**; frame admission: the laptop did NOT reproduce
  the anchor (max diff **8.31×10⁻⁶**) — every deciding read is a
  VM read — `GATE39.md` §1; `sources/g39_calibration.json`.

Checked: every deciding number in the final set — 0 unmatched.

## Assembly notes

- **Selection, stated:** the gate record entire (`GATE39.md` —
  its §5 is the only quotable form of the set). From gate39/, the
  gate's machinery entire (six files in `code/` — Gate-39 ran its
  own computation, unlike Gate-38, so this bundle carries the
  gate's code) and its deciding result records (in `sources/`:
  the calibration, scan, refinement and confirmation JSONs and
  the worker's numbers memo). From phase364/, the checkpoint and
  the worker memo — the phase's verdict records, carrying the
  claim set as filed and Amendments 1–2 disclosed on the memo's
  face. **Not bundled:** the per-member checkpoint parts
  (`g39_scan_part0/1.json`, `g39_refine_part0/1.json` — resume
  checkpoints whose contents are consolidated in the bundled
  `g39_scan.json` / `g39_refine.json`); Gate-39's run logs
  (`gate39/work/logs/`); the `__pycache__` .pyc files under the
  gate work directory (compiled artefacts); Phase 364's own
  machinery, control/scan/refine/confirm JSONs and run logs (the
  gate judged Phase 364's records; its deciding values are
  carried in the bundled gate records and the worker memo's diffs
  table); the stored Phase 344 A2 centre files the gate's
  assembly reads (identified on the bundled code's face).
- The verbatim block embedded in the written files was
  diff-verified character-for-character at assembly: the
  GATE39.md §5 claim set in RESULTS.md and in
  RELEASE_v1.30.0.md — both checks exact. The disclosure
  paragraph in RELEASE_v1.30.0.md is in
  gate38-claims/RELEASE_v1.29.0.md's exact form.
- No source file was edited; no bundled .py was executed and
  nothing was unpickled at any point in packaging.
