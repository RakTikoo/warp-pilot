# Gate-47 claims bundle - MANIFEST (release v1.37.0)

Every file in this folder, its size in bytes, and where it came from.
Copies are byte-for-byte copies of the named source (md5-verified at
assembly; every copy also cmp-verified against its source at assembly).
This manifest lists every file in the bundle except itself.

| file | bytes | source / traceability |
|---|---|---|
| GATE47.md | 26279 | gate47/GATE47.md (gate record, verbatim copy) md5 2c4ae17abde8b42a641f1e630ab9737d |
| README_WHATSNEW_v1370.md | 6739 | written for this bundle (prepared README update; applied at upload) |
| RELEASE_v1.37.0.md | 12704 | written for this bundle (release draft; the GATE47.md §5 claim set embedded verbatim, diff-verified against GATE47.md §5 at assembly; the disclosure paragraph in gate38-claims/RELEASE_v1.29.0.md's exact form; version DOI TBD — minted at release) |
| RESULTS.md | 18660 | written for this bundle (the claim set: the GATE47.md §5 block verbatim — the only quotable form of the Phase 396 claim set; the §5 block in RESULTS.md was diff-verified character-for-character against GATE47.md §5 at assembly) |
| code/g47_lib.py | 26930 | gate47/work/g47_lib.py (Gate-47's machinery — sympy symbolic first/second spatial derivatives of the registered metric in Cartesian coordinates, lambdified with cse, own vectorised Christoffel/Ricci assembly, own profile assembly, Eulerian frame, SAMPLER-M margins, worst-null, verbatim copy) md5 81839ad4bc0a0a650809b420a83c1b05 |
| code/g47_run.py | 19632 | gate47/work/g47_run.py (Gate-47's first driver — its trivial-limit calibration call crashed on a driver-side array-size bug; fixed and rerun in full as g47_run2.py; no machinery changed and no deciding read affected, verbatim copy) md5 8f63928aaae7c90ab5a86e77d9f0734f |
| code/g47_run2.py | 9148 | gate47/work/g47_run2.py (Gate-47's driver, full rerun — the run that produced the bundled deciding records, verbatim copy) md5 507605f6ff13ede84faabd688b73a17e |
| code/make_g47_figure.py | 6696 | written for this bundle (the figure generator — reads only the bundled records in sources/ and writes figures/g47_level_progression.png) |
| figures/g47_level_progression.png | 394213 | generated at assembly by code/make_g47_figure.py from the bundled records (the lineage progression −1.942246×10⁻⁴ → −1.757074×10⁻⁴ → −1.241372×10⁻⁴ → −6.812653×10⁻⁵ → −2.980985×10⁻⁵ → −7.431892×10⁻⁶, the end-clamped level −7.644644×10⁻⁶ marked as a ring on the centre point, the G47-F certified/flagged boundary between Phase 395's and Phase 396's centres, the one-factor attribution (μ_S 77% · μ_N 46% · μ_M 5%), riders G47-E and G47-F and the §5 fence on the figure's face) |
| sources/CHECKPOINT396.md | 15570 | phase396/CHECKPOINT396.md (Phase 396's phase record — registration, controls, verdict, anatomy, the SS7 physicality watch and the degeneracy note, verbatim copy) md5 447b42f2fdea53f6653210190cb31098 |
| sources/g47_box_diag.json | 5180 | gate47/results/g47_box_diag.json (Gate-47's §3 records — the 336-read box recount, the worst-DEC re-read, the diagonal and RAY3 re-reads, verbatim copy) md5 e5c5d1e149ec27984686ec082005d4b6 |
| sources/g47_clamp_margins.json | 391 | gate47/results/g47_clamp_margins.json (Gate-47's clamp-margin record — the clamped centre and both surviving margins, verbatim copy) md5 a135c296edf05f8d317a4698c4a51399 |
| sources/g47_degeneracy.json | 11652 | gate47/results/g47_degeneracy.json (Gate-47's §4 records — the physicality table, the binding-site μ_S scan and fits, the shift-free reads, the gain attribution, the ridge table, verbatim copy) md5 12ff6c40dcedfb9d858046747e17b0cb |
| sources/g47_numbers.json | 16549 | gate47/results/g47_numbers.json (Gate-47's §2 deciding reads — the centre, its clamp, the five lineage controls and the worst-nulls, verbatim copy) md5 6fda9f74258d2e2f8855fea7d1fd6920 |
| sources/g47_summary.json | 3811 | gate47/results/g47_summary.json (Gate-47's summary — calibrations, the md5 registry of the gate's inputs, verbatim copy) md5 411d506ec96572ff03a51c48bee43f10 |
| sources/p396_anatomy.json | 5276 | phase396/results/p396_anatomy.json (Phase 396's anatomy record — the ray and diagonal traces, the box-edge disclosure, verbatim copy) md5 7507dfa0b8ee3c228b69daa09151c749 |
| sources/p396_clamp.json | 1416 | phase396/results/p396_clamp.json (Phase 396's end-clamp record — clamped reads for the centre and the lineage legs, verbatim copy) md5 c3bc4d30448abf28785635c4d36a3f75 |
| sources/p396_confirmation.json | 1340 | phase396/results/p396_confirmation.json (Phase 396's confirmation record — the centre's full re-read at diff 0.0, its worst-null and margins, verbatim copy) md5 0da43dc00af7cd0a4194b9e1235f66c9 |
| sources/p396_controls.json | 4881 | phase396/results/p396_controls.json (Phase 396's VM controls — all diff 0.0, verbatim copy) md5 3eac238d67e681fc2821cc99f8a53179 |
| sources/p396_memo.md | 7744 | phase396/results/p396_memo.md (Phase 396's worker memo — the claim set as filed, with the degeneracy note on its face, verbatim copy) md5 2d6aef13d18ce6274f10691eaf948adb |
| sources/p396_physicality.json | 4761 | phase396/results/p396_physicality.json (Phase 396's SS7 physicality record — the peak |β·S| table and the fired degeneracy flag the gate ruled on, verbatim copy) md5 651b4900f1d3cfa1a95dbf3dbaa16695 |
| sources/p396_screens.jsonl | 147614 | phase396/results/p396_screens.jsonl (Phase 396's stored screen record — all 336 reads of the registered box, the record Gate-47 recounted for claim (d), verbatim copy) md5 d3a71a0d225726d7d989406191f126ff |
| sources/p396_search_summary.json | 9177 | phase396/results/p396_search_summary.json (Phase 396's search summary — the 336-read box accounting, verbatim copy) md5 e609508c4c03c85c7749e44104b98dd9 |

## Numbers check (every deciding number in the final set, transcribed from the bundled records)

Sources of truth for this section: the bundled gate record
`GATE47.md` (§§1–6), the bundled Phase 396 records in
`sources/` (`CHECKPOINT396.md`, `p396_memo.md`,
`p396_confirmation.json`, `p396_clamp.json`,
`p396_controls.json`, `p396_physicality.json`) and Gate-47's
bundled result records in `sources/` (`g47_numbers.json`,
`g47_box_diag.json`, `g47_clamp_margins.json`,
`g47_degeneracy.json`, `g47_summary.json`). Values below were
transcribed from those files during packaging — packaging copies,
hashes, and transcribes only; no bundled code was executed except
the figure generator (which reads the bundled records and writes
only the figure). Spot-checks performed against the bundled JSON
records at assembly: 65 checks covering every deciding value
below — the centre's joint/NEC/DEC/SEC/ρ minima and argmin radii,
its Type-I count, its worst-null and both margins, all five
controls, the clamped centre, its cost and both clamped margins,
the box recount, the diagonal and the worst-DEC re-read, the
physicality peaks and the gain attribution, the shift-free reads
and the binding-site floor — 0 unmatched.

- **The centre (G47-A)** — (μ_S, μ_N, μ_M) =
  (0.4003528067864536, 1.9863455070489624, 6.715383396291902) on
  H2's total profiles. Gate batch SET-244 joint
  **−7.431892169092337×10⁻⁶** vs stored
  −7.4318921690925×10⁻⁶ (diff +1.6×10⁻¹⁹), NEC-carried at
  r = 16.46341463414634; DEC min gate
  −1.097932392391424×10⁻⁶ / stored −1.0979323923912478×10⁻⁶ at
  r = 18.902439024390244, Type-I; ρ min gate
  +9.858014400881774×10⁻⁵ / stored +9.858014400881535×10⁻⁵;
  SEC min −3.391058851844148×10⁻⁴; Type-I count **4756** of
  6642 exact. Margins on the stored values:
  **+2.237796×10⁻⁵** over Phase 395's centre (−2.980985×10⁻⁵),
  +6.067464×10⁻⁵ over Phase 394's centre (−6.812653×10⁻⁵),
  +1.682755×10⁻⁴ over the mixed centre (−1.757074×10⁻⁴),
  +1.867927×10⁻⁴ over L_stat(H2) (−1.942246×10⁻⁴) —
  `GATE47.md` §2, §5; `sources/g47_numbers.json` (`CENTRE`),
  `sources/p396_confirmation.json` (`best`).
- **Pointwise grade (G47-B)** — the exact worst-null at the
  centre's SET NEC argmin: gate −8.706718841221368×10⁻⁶ vs
  stored **−8.706718841221561×10⁻⁶** (diff +1.9×10⁻¹⁹); the
  anchor's worst-null −3.0896210095678075×10⁻⁵ (gate diff
  −3.0×10⁻¹⁹); the seed's −1.2477276305772507×10⁻⁴ (diff 0.0);
  the margin **+2.218949×10⁻⁵** — `GATE47.md` §2, §5;
  `sources/g47_numbers.json` (`worst_nulls`),
  `sources/p396_confirmation.json` (`best`).
- **The end-clamp rider (G47-C)** — clamped centre: gate
  **−7.644643599300465×10⁻⁶** at diff 0.0 vs stored; clamp cost
  gate **2.127514302081271×10⁻⁷** / stored
  2.1275143020796448×10⁻⁷; the clamped level remains above the
  anchor's unclamped level by **+2.2165206678448785×10⁻⁵** and
  above L_stat(H2) by **+1.865799553183718×10⁻⁴** — both
  margins survive clamping. The gate's clamp construction is
  cross-validated on three further legs: the clamped anchor at
  diff +5.4×10⁻²⁰ (−3.018920609401202×10⁻⁵), the clamped
  (1,1,1) against Phase 379's stored end-clamp set at
  ≤6.0×10⁻¹⁹ (joint −2.087299309761305×10⁻⁴), and the clamped
  mixed centre against Gate-43's independent value at
  +9.2×10⁻¹⁹, far inside the C-10 band — `GATE47.md` §2, §5;
  `sources/g47_clamp_margins.json`, `sources/g47_numbers.json`
  (`clamps`), `sources/p396_clamp.json`.
- **Controls** — (1,1,1): gate joint −1.9422459891767238×10⁻⁴
  (= L_stat(H2)); Type-I count **3262** exact. Mixed centre:
  joint −1.7570735537945193×10⁻⁴; Type-I count **3359** exact.
  Seed: joint −1.2413718983790085×10⁻⁴; NEC diff 0.0, worst-null
  diff 0.0. C394: joint −6.812652656191777×10⁻⁵; Type-I count
  **3311** exact. Anchor (Phase 395's centre): joint
  −2.980985027774925×10⁻⁵; Type-I count **4067** exact. The
  largest |diff| anywhere in the control table is 8.7×10⁻¹⁸
  (H2 SEC). C-10 note: the NEC argmin point is non-Type-I at
  all six reads and every DEC argmin point is Type-I, yet no
  sampled minimum deviates beyond ~10⁻¹⁸ — the C-10 band is
  engaged by no deciding value — `GATE47.md` §§1–2;
  `sources/g47_numbers.json` (`reads`),
  `sources/p396_controls.json`.
- **The registered box (G47-D)** — recount of the stored
  record: **336** reads, **336** feasible; **326** with joint
  above the anchor's −2.9809850277749006×10⁻⁵; worst DEC
  **−2.0253148251802704×10⁻⁶**, independently re-read on gate
  machinery at diff −1.5×10⁻¹⁹ (Type-I at
  r = 18.65853658536585; its joint −3.0654469143335814×10⁻⁵);
  **zero** DEC-saturated reads under either threshold (−0.5,
  −0.9999). The registered diagonal, re-read at all nine
  points (anchor + k = 1..8): strictly monotone, max |diff|
  2.4×10⁻¹⁹, ending at −9.943225903497104×10⁻⁶, still rising,
  increments mildly decaying with last/first =
  0.6172036936811398. The RAY3 endpoint
  (0.601180962300002, 1.5934531363763935, 7.0) re-reads at diff
  −8.1×10⁻²⁰ (−2.8521103406139005×10⁻⁵) — `GATE47.md` §3, §5;
  `sources/g47_box_diag.json`, `sources/p396_screens.jsonl`,
  `sources/p396_anatomy.json`.
- **The box-edge rider (G47-E)** — the centre's μ_S =
  0.4003528067864536 sits 0.0003528067864536 above the
  registered box's lower edge 0.40 and its μ_N =
  1.9863455070489624 sits 0.0136544929510376 below the upper
  edge 2.00; μ_M = 6.715383396291902 sits inside its edge
  (7.00) — the third widening in a row whose centre arrived at
  the new μ_S edge. The centre is quotable only as the optimum
  of the registered box — `GATE47.md` §3, §5;
  `sources/p396_anatomy.json`, `sources/CHECKPOINT396.md`.
- **The degeneracy rider (G47-F)** — the gate's physicality
  table reproduces Phase 396's record at max diff exactly 0.0
  (every per-field diff in `sources/g47_degeneracy.json` is
  0.0): peaks |β·S| H2 **0.8853484980534808** → C394
  0.7096678598389627 → anchor 0.532254662030653 → centre
  **0.35445175617988206** (ratios to H2 equal μ_S exactly);
  the centre's binding-site locals (r = 16.46341463414634)
  S = 0.07743322636564062, S′′ = 0.016179742866951445,
  N = 2.4547830252740606, M = 39.31075989942729 against H2's
  S = 0.19341247283160218, S′′ = 0.040413711588093475,
  N = 1.2358288205967942, M = 6.704925190210542. One-factor
  attribution from the anchor (full gain, gate
  +2.2377958108656912×10⁻⁵): μ_S alone **+1.726871403601705×10⁻⁵
  (77%)**, μ_N alone +1.0272341333937351×10⁻⁵ (46%), μ_M alone
  +1.0349233367103845×10⁻⁶ (5%), interaction ≈ −6.2×10⁻⁶.
  The mechanism, restated: at the binding site the shift-free
  floor is positive — worst-null(0) = **+8.716515065031833×10⁻⁶**
  (Type-I) — and the violation grows ~linearly in μ_S
  (log–log slope **1.00005**); μ_S² fits fail (worst-null fit
  slope −3.9689×10⁻⁵, intercept −7.84×10⁻⁶, max |residual|
  5.77×10⁻⁶). The shift-free configuration at the centre's
  (μ_N, μ_M) still violates at joint
  **−1.0499339416511982×10⁻⁶** in the (N, M) sector, and at
  H2's (1, 1) shift removal makes the joint worse
  (−2.928040843203875×10⁻⁴). Named, as charged: the last
  centre clearing the registered half-of-H2 peak-shift bar is
  Phase 395's centre (peak ratio 0.6012, level
  −2.980985×10⁻⁵); the ridge-asymptote residue is referred to
  Phase 397's degeneracy probe — `GATE47.md` §4, §5;
  `sources/g47_degeneracy.json`, `sources/p396_physicality.json`.

Checked: every deciding number in the final set — 0 unmatched.

## Assembly notes

- **Selection, stated:** the gate record entire (`GATE47.md` —
  its §5 is the only quotable form of the set). From gate47/,
  the gate's machinery (`code/g47_lib.py`, `code/g47_run.py`,
  `code/g47_run2.py` — Gate-47 ran its own computation, so this
  bundle carries the gate's code) and its deciding result
  records (in `sources/`: the numbers, box/diagonal,
  clamp-margin, degeneracy and summary JSONs). From phase396/,
  the checkpoint and the worker memo — the phase's verdict
  records, carrying the claim set as filed with the degeneracy
  note on its face — and the phase's key records the gate
  judged against (confirmation, clamp, anatomy, controls, the
  SS7 physicality record, search summary, and the stored
  screens the gate recounted for claim (d)). The figure
  (`figures/g47_level_progression.png`) was generated at
  assembly by the bundled `code/make_g47_figure.py` from the
  bundled records, per the standing diagrams rule; its values
  were read back from the generator's own output at assembly
  (H2 −1.942245989176724×10⁻⁴; mixed centre
  −1.757073553794519×10⁻⁴; seed −1.241371898379008×10⁻⁴; C394
  −6.812652656191777×10⁻⁵; anchor −2.980985027774925×10⁻⁵;
  centre −7.431892169092337×10⁻⁶ — the gate reads; clamped
  −7.644643599300465×10⁻⁶; peaks |β·S| 0.885348498053481 /
  0.709667859838963 / 0.532254662030653 / 0.354451756179882,
  half-of-H2 0.442674249026740) and the rendered figure was
  inspected before packaging (two layout passes were needed
  and redone). **Not bundled:** Phase 396's own machinery
  (`phase396/work/` — the gate judged Phase 396's records; its
  deciding values are carried in the bundled gate records and
  the bundled phase records); Phase 396's laptop control
  record (p396_controls_laptop.json — the laptop is not a gate
  instrument and was not admitted as a frame for the phase's
  deciding reads; the checkpoint carries the admission
  outcome) and its console logs (p396_controls.log,
  p396_search.log, p396_postsearch.log — transcripts of the
  bundled records' drivers) and the per-stage screen parts
  under `phase396/results/parts/` (the combined
  `p396_screens.jsonl` bundled here is the record Gate-47
  recounted); Gate-47's run log (g47_run.log) and the
  `__pycache__` .pyc files under the gate work directory
  (compiled artefacts); the stored profile vectors the gate's
  code reads (identified on the bundled code's face and in
  GATE47.md §6, with their md5s in the bundled
  `g47_summary.json`).
- The verbatim block embedded in the written files was
  diff-verified character-for-character at assembly: the
  GATE47.md §5 claim set in RESULTS.md and in
  RELEASE_v1.37.0.md — both checks exact. The disclosure
  paragraph in RELEASE_v1.37.0.md is in
  gate38-claims/RELEASE_v1.29.0.md's exact form.
- No source file was edited; no bundled .py was executed at
  packaging except the figure generator, and nothing was
  unpickled.
