# Gate-46 claims bundle - MANIFEST (release v1.38.0)

Every file in this folder, its size in bytes, and where it came from.
Copies are byte-for-byte copies of the named source (md5-verified at
assembly; every copy also cmp-verified against its source at assembly).
This manifest lists every file in the bundle except itself.

| file | bytes | source / traceability |
|---|---|---|
| GATE46.md | 20688 | gate46/GATE46.md (gate record, verbatim copy) md5 af79279d9590b06bf1405b0cd48ad5dd |
| README_WHATSNEW_v1380.md | 5481 | written for this bundle (prepared README update; applied at upload) |
| RELEASE_v1.38.0.md | 8992 | written for this bundle (release draft; the GATE46.md §5 claim set embedded verbatim, diff-verified against GATE46.md §5 at assembly; the disclosure paragraph in gate38-claims/RELEASE_v1.29.0.md's exact form; version DOI TBD — minted at release) |
| RESULTS.md | 12837 | written for this bundle (the claim set: the GATE46.md §5 block verbatim — the only quotable form of the Phase 395 claim set; the §5 block in RESULTS.md was diff-verified character-for-character against GATE46.md §5 at assembly) |
| code/g46_derive.py | 6209 | gate46/work/g46_derive.py (Gate-46's sympy derivation driver — its docstring records why the shipped form uses an analytic Schur-complement inverse with time-boxed simplify/factor: the first, fully-simplifying attempt did not finish and was terminated, verbatim copy) md5 d3789b5a88eec940a84e0fb0f889bf27 |
| code/g46_diag.py | 1536 | gate46/work/g46_diag.py (Gate-46 diagnostic driver, verbatim copy) md5 be10294bc9c5a895ad92c71e1bbff3f6 |
| code/g46_diag2.py | 1329 | gate46/work/g46_diag2.py (Gate-46's C-10 diagnostic — the batch-vs-single evaluation at the seed's batch argmin point recorded in GATE46.md §1, verbatim copy) md5 543e55a3e7b8aa6f09a8abb977f48182 |
| code/g46_exprs.py | 2191895 | gate46/work/g46_exprs.py (the derived Einstein-tensor expressions — the sympy derivation's output, consumed by g46_lib.py, verbatim copy) md5 be7e91b4dbbf8a36e3a9d427d068d181 |
| code/g46_lib.py | 14127 | gate46/work/g46_lib.py (Gate-46's machinery — spherical-coordinate sympy-derived Einstein tensor, lambdified and transformed to Cartesian point by point, own profile assembly, Eulerian frame, SAMPLER-M margins, worst-null, verbatim copy) md5 7424554bd3ccd43dba5a309709bcceeb |
| code/g46_profiles.py | 6718 | gate46/work/g46_profiles.py (Gate-46's own profile assembly — A2 base + K = 33 corrections; H2 = centre(1.15) + K = 17 corrections, verbatim copy) md5 2f3ca0cff24ece4a3f4edc21cac50099 |
| code/g46_recount.py | 1687 | gate46/work/g46_recount.py (Gate-46's recount driver for claim (d), verbatim copy) md5 949b4fc3821d1e23f9a6b641582a71c8 |
| code/g46_run.py | 9643 | gate46/work/g46_run.py (Gate-46's main driver — the run that produced the bundled deciding records; its first launch was lost to a service restart before any output was written and was relaunched in full, verbatim copy) md5 7ad03d8c863399bf5bfe639b14acccf9 |
| code/g46_shellpoints.py | 2623 | gate46/work/g46_shellpoints.py (Gate-46's shell-point driver, verbatim copy) md5 71b35345c4ef55695775ed65a940ce17 |
| code/g46_smoke.py | 1566 | gate46/work/g46_smoke.py (Gate-46's smoke-test driver, verbatim copy) md5 b11edef7b075c96aab7330d01b29c425 |
| code/g46_summary.py | 3521 | gate46/work/g46_summary.py (Gate-46's summary driver — produced sources/g46_summary.json, verbatim copy) md5 52960d3fbfaa17117fa1a29b6e5dcc70 |
| code/make_g46_figure.py | 5619 | written for this bundle (the figure generator — reads only the bundled records in sources/ and writes figures/g46_level_progression.png) |
| figures/g46_level_progression.png | 319226 | generated at assembly by code/make_g46_figure.py from the bundled records (the lineage progression −1.942246×10⁻⁴ → −1.757074×10⁻⁴ → −1.241372×10⁻⁴ → −6.812653×10⁻⁵ → −2.980985×10⁻⁵, the end-clamped level −3.018921×10⁻⁵ marked as a ring on the centre point, rider G46-E and the §5 fence on the figure's face; the progression stops at Phase 395's centre, as charged) |
| sources/CHECKPOINT395.md | 11625 | phase395/CHECKPOINT395.md (Phase 395's phase record — registration summary, controls, verdict, anatomy, box-edge disclosure, verbatim copy) md5 0c30b160559366962ff3c6cd3d454713 |
| sources/g46_clamp_margins.json | 5695 | gate46/results/g46_clamp_margins.json (Gate-46's clamp record — the clamped reads for H2S, the mixed centre, the anchor and the centre, with the clamp cost and both surviving margins, verbatim copy) md5 e6c622984ecffde8f888f54ee905dcbe |
| sources/g46_numbers.json | 11406 | gate46/results/g46_numbers.json (Gate-46's §2 deciding reads — the centre, the four lineage controls, the named points and worst-nulls, verbatim copy) md5 4ce396bc1a42a54896a2deccd099635a |
| sources/g46_ray_box.json | 4367 | gate46/results/g46_ray_box.json (Gate-46's §3 records — the worst-DEC re-read, the diagonal and μ_M-ray re-reads, the FD cross-check, verbatim copy) md5 9ad9f5e395a82ecd0c7f51867989adda |
| sources/g46_recount.json | 711 | gate46/results/g46_recount.json (Gate-46's recount of the 220 stored reads for claim (d), verbatim copy) md5 0bd7e72e8f2704049e3eddfae61bb087 |
| sources/g46_shellpoints.json | 2040 | gate46/results/g46_shellpoints.json (Gate-46's shell-point records, verbatim copy) md5 38b0912999c6d9d957425fca48565f5f |
| sources/g46_summary.json | 3588 | gate46/results/g46_summary.json (Gate-46's summary — rulings, deciding diffs, the C-10 band observations and the md5 registry of the gate's inputs, verbatim copy) md5 76e3d5bc850fd6d202da99aba80ea180 |
| sources/p395_anatomy.json | 3101 | phase395/results/p395_anatomy.json (Phase 395's anatomy record — the ray and diagonal traces, the box-edge disclosure, verbatim copy) md5 1632c1d11b6242ff4593e64d6cd94691 |
| sources/p395_clamp.json | 1349 | phase395/results/p395_clamp.json (Phase 395's end-clamp record — clamped reads for the centre and the lineage legs, verbatim copy) md5 2eb334e7a12e55753fc894d1793f8df6 |
| sources/p395_confirmation.json | 1340 | phase395/results/p395_confirmation.json (Phase 395's confirmation record — the centre's full re-read at diff 0.0, its worst-null and margins, verbatim copy) md5 6d3e2c209ffbcd36ff2f59bdee09a0bb |
| sources/p395_controls.json | 3804 | phase395/results/p395_controls.json (Phase 395's VM controls — all diff 0.0, verbatim copy) md5 c351a47304f5186a1884e8db2dcbdc7c |
| sources/p395_memo.md | 5287 | phase395/results/p395_memo.md (Phase 395's worker memo — the claim set as filed, verbatim copy) md5 15af837dcac189fec01751ad2ee66979 |
| sources/p395_screens.jsonl | 95355 | phase395/results/p395_screens.jsonl (Phase 395's stored screen record — all 220 reads of the registered extended box, the record Gate-46 recounted for claim (d), verbatim copy) md5 918d28be3c00c7d978ce318ed1580bd0 |
| sources/p395_search_summary.json | 8236 | phase395/results/p395_search_summary.json (Phase 395's search summary — the 220-read box accounting, verbatim copy) md5 62993b28d0ea5f6dbb000fef530053ff |

## Numbers check (every deciding number in the final set, transcribed from the bundled records)

Sources of truth for this section: the bundled gate record
`GATE46.md` (§§1–6), the bundled Phase 395 records in
`sources/` (`CHECKPOINT395.md`, `p395_memo.md`,
`p395_confirmation.json`, `p395_clamp.json`,
`p395_controls.json`) and Gate-46's bundled result records in
`sources/` (`g46_numbers.json`, `g46_clamp_margins.json`,
`g46_ray_box.json`, `g46_recount.json`, `g46_summary.json`).
Values below were transcribed from those files during packaging — packaging copies,
hashes, and transcribes only; no bundled code was executed except
the figure generator (which reads the bundled records and writes
only the figure). Spot-checks performed against the bundled JSON
records at assembly: 67 checks covering every deciding value
below — the centre's joint/NEC/DEC/ρ minima and argmin radii,
its Type-I count, its worst-null and both margins, all four
controls, the clamped centre, its cost and both clamped margins,
the box recount, the diagonal and ray re-reads and the worst-DEC
re-read — 0 unmatched.

- **The centre (G46-A)** — (μ_S, μ_N, μ_M) =
  (0.601180962300002, 1.5934531363763935, 4.887238651223381) on
  H2's total profiles. Gate batch SET-244 joint
  **−2.9809850277749195×10⁻⁵** vs stored
  −2.9809850277749006×10⁻⁵ (diff −1.9×10⁻¹⁹), NEC-carried at
  r = 15.73170731707317; DEC min stored
  −1.7766846142506707×10⁻⁶ (gate diff −6.8×10⁻²⁰) at
  r = 18.65853658536585, Type-I; ρ min stored
  +9.780857711542179×10⁻⁵ (gate diff −6.9×10⁻¹⁸); Type-I count
  **4067** of 6642 exact. Margins on the stored values:
  **+3.831668×10⁻⁵** over Phase 394's centre (−6.812653×10⁻⁵),
  +9.432734×10⁻⁵ over the ray point (−1.241372×10⁻⁴),
  +1.458975×10⁻⁴ over the mixed centre (−1.757074×10⁻⁴),
  +1.644147×10⁻⁴ over L_stat(H2) (−1.942246×10⁻⁴) —
  `GATE46.md` §2, §5; `sources/g46_numbers.json` (`configs.CENTRE`),
  `sources/p395_confirmation.json` (`best`).
- **Pointwise grade (G46-B)** — the exact worst-null at the
  centre's SET NEC argmin: gate −3.089621009567827×10⁻⁵ vs
  stored **−3.0896210095678075×10⁻⁵** (diff −2.0×10⁻¹⁹); the
  anchor's worst-null −7.173153284502476×10⁻⁵; the margin
  **+4.083532×10⁻⁵** — `GATE46.md` §2, §5;
  `sources/g46_numbers.json` (`configs.CENTRE.named_point`),
  `sources/p395_confirmation.json` (`best`).
- **The end-clamp rider (G46-C)** — clamped centre: gate
  **−3.0189206094012128×10⁻⁵** / stored
  −3.0189206094012074×10⁻⁵ (diff −5.4×10⁻²⁰); clamp cost
  stored **3.7935581626306804×10⁻⁷** (gate magnitude agrees at
  1.4×10⁻¹⁹); the clamped level remains above the anchor's
  unclamped level by **+3.793732×10⁻⁵** and above L_stat(H2)
  by **+1.640354×10⁻⁴** — both margins survive clamping, each
  by more than an order of magnitude over the C-10 band. The
  gate's clamp construction is cross-validated on three
  further legs (C-3): the clamped mixed centre against
  Gate-43's independent value at diff −2.7×10⁻¹⁹
  (−1.7669632754376664×10⁻⁴), the clamped (1,1,1) against
  Gate-41/43/45's value at diff +2.7×10⁻¹⁹
  (−2.0872993097613136×10⁻⁴), and the clamped anchor against
  Phase 395's stored value at diff −1.2×10⁻¹⁹
  (−6.968822658140883×10⁻⁵) — `GATE46.md` §2, §5;
  `sources/g46_clamp_margins.json`, `sources/p395_clamp.json`.
- **Controls** — (1,1,1): DEC diff −5.7×10⁻¹⁹, ρ diff
  +5.4×10⁻²⁰, Type-I count **3262** exact; at the stored NEC
  argmin shell the shell NEC minimum reproduces L_stat(H2) at
  diff −5.1×10⁻¹⁹ (the batch minimum's sibling-shell excursion
  is the C-10 effect). Mixed centre: DEC diff +1.0×10⁻¹⁸, ρ
  diff +1.4×10⁻¹⁹, Type-I count **3359** exact, worst-null
  diff −2.4×10⁻¹⁹. Seed: DEC diff −1.1×10⁻¹⁹, ρ diff
  −9.5×10⁻¹⁹, Type-I count **3148** exact, named-point NEC
  diff 0.0, worst-null diff −2.7×10⁻²⁰. Anchor (Phase 394's
  centre): joint diff −2.7×10⁻²⁰, Type-I count **3311**
  exact, worst-null diff +1.4×10⁻²⁰. C-10 note: the batch
  WEC/SEC minima at (1,1,1) differ from stored by
  −7.10×10⁻⁶ / −4.09×10⁻⁶ — differences of two extreme order
  statistics over ~2.6×10³ non-Type-I points; no claim in this
  set rests on a WEC or SEC value — `GATE46.md` §§1–2;
  `sources/g46_numbers.json` (`configs`),
  `sources/p395_controls.json`.
- **The registered extended box (G46-D)** — recount of the
  stored record: **220** reads, **220** feasible; **212** with
  joint above the anchor's −6.812652656191736×10⁻⁵; worst DEC
  **−6.5529696405777245×10⁻⁶** (the G2 read at
  (0.8015689430763502, 1.3179449338854314,
  3.074968377899082)), independently re-read on gate
  machinery at diff +1.6×10⁻¹⁹ (its DEC argmin Type-I at
  r = 18.170731707317074); **zero** DEC-saturated reads under
  either threshold (−0.5, −0.9999). The registered diagonal,
  re-read at all five points at roundoff (diffs ≤ 2.2×10⁻¹⁹):
  −6.812653×10⁻⁵ → −6.304991×10⁻⁵ → −5.754609×10⁻⁵ →
  −5.289900×10⁻⁵ → −4.818018×10⁻⁵, increments +5.076619,
  +5.503820, +4.647083, +4.718826 ×10⁻⁶ — undiminished, no
  turn. The pure μ_M ray, re-read at all seven registered
  radii: dips at μ_M = 3.75 (−6.912171×10⁻⁵) then rises
  monotonically to the 5.00 edge (gate −6.323066×10⁻⁵;
  stored −6.333735×10⁻⁵; the edge joint differs by
  +1.07×10⁻⁷, inside the C-10 band) with no turn —
  `GATE46.md` §3, §5; `sources/g46_ray_box.json`,
  `sources/g46_recount.json`, `sources/p395_screens.jsonl`,
  `sources/p395_anatomy.json`.
- **The box-edge rider (G46-E)** — the centre's μ_S =
  0.601180962300002 sits 0.00118 above the extended box's
  lower edge 0.60 and its μ_N = 1.5934531363763935 sits
  0.00655 below the upper edge 1.60; μ_M = 4.887238651223381
  sits inside its edge (5.00), 0.113 below it. The centre is
  quotable only as the optimum of the registered extended
  box — `GATE46.md` §4, §5; `sources/p395_anatomy.json`,
  `sources/CHECKPOINT395.md`.

Checked: every deciding number in the final set — 0 unmatched.

## Assembly notes

- **Selection, stated:** the gate record entire (`GATE46.md` —
  its §5 is the only quotable form of the set). From gate46/,
  the gate's machinery (all of `gate46/work/*.py` — the
  derivation driver and its derived expressions, the machinery
  and profile assembly, the run/recount/shell-point/summary
  drivers and the diagnostic and smoke drivers — Gate-46 ran
  its own computation, so this bundle carries the gate's code)
  and its deciding result records (in `sources/`: the numbers,
  clamp-margin, ray/box, recount, shell-point and summary
  JSONs). From phase395/, the checkpoint and the worker memo —
  the phase's verdict records, carrying the claim set as
  filed — and the phase's key records the gate judged against
  (confirmation, clamp, anatomy, controls, search summary, and
  the stored screens the gate recounted for claim (d)). The
  figure (`figures/g46_level_progression.png`) was generated
  at assembly by the bundled `code/make_g46_figure.py` from
  the bundled records, per the standing diagrams rule; its
  values were read back from the generator's own output at
  assembly (H2 −1.942245989176723×10⁻⁴; mixed centre
  −1.757073553794524×10⁻⁴; seed −1.241371898379008×10⁻⁴; C394
  −6.812652656191736×10⁻⁵; C395 −2.980985027774901×10⁻⁵ — the
  stored levels quoted in GATE46.md §5; clamped
  −3.018920609401207×10⁻⁵) and the rendered figure was
  inspected before packaging. **Not bundled:** Phase 395's own
  machinery (`phase395/work/` — the gate judged Phase 395's
  records; its deciding values are carried in the bundled gate
  records and the bundled phase records); Phase 395's laptop
  control record (p395_controls_laptop.json — the laptop is
  not a gate instrument; the checkpoint carries the admission
  outcome) and its console logs (p395_controls.log,
  p395_search.log — transcripts of the bundled records'
  drivers) and the per-stage screen parts under
  `phase395/results/parts/` (the combined `p395_screens.jsonl`
  bundled here is the record Gate-46 recounted); Gate-46's
  run logs (g46_derive.log, g46_diag.log, g46_diag2.log,
  g46_run.log, g46_shellpoints.log) and the `__pycache__` .pyc
  files under the gate work directory (compiled artefacts);
  the stored profile vectors the gate's code reads (identified
  on the bundled code's face and in GATE46.md §6, with their
  md5s in the bundled `g46_summary.json`).
- The verbatim block embedded in the written files was
  diff-verified character-for-character at assembly: the
  GATE46.md §5 claim set in RESULTS.md and in
  RELEASE_v1.38.0.md — both checks exact. The disclosure
  paragraph in RELEASE_v1.38.0.md is in
  gate38-claims/RELEASE_v1.29.0.md's exact form.
- No source file was edited; no bundled .py was executed at
  packaging except the figure generator, and nothing was
  unpickled.
