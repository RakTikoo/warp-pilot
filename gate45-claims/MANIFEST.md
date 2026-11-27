# Gate-45 claims bundle - MANIFEST (release v1.36.0)

Every file in this folder, its size in bytes, and where it came from.
Copies are byte-for-byte copies of the named source (md5-verified at
assembly; every copy also cmp-verified against its source at assembly).
This manifest lists every file in the bundle except itself.

| file | bytes | source / traceability |
|---|---|---|
| GATE45.md | 16663 | gate45/GATE45.md (gate record, verbatim copy) md5 aebe3da522659159e87150e6be9e41d0 |
| README_WHATSNEW_v1360.md | 4593 | written for this bundle (prepared README update; applied at upload) |
| RELEASE_v1.36.0.md | 7458 | written for this bundle (release draft; the GATE45.md §5 claim set embedded verbatim, diff-verified against GATE45.md §5 at assembly; the disclosure paragraph in gate38-claims/RELEASE_v1.29.0.md's exact form; version DOI TBD — minted at release) |
| RESULTS.md | 9454 | written for this bundle (the claim set: the GATE45.md §5 block verbatim — the only quotable form of the Phase 394 claim set; the §5 block in RESULTS.md was diff-verified character-for-character against GATE45.md §5 at assembly) |
| code/g45_lib.py | 24070 | gate45/work/g45_lib.py (Gate-45's machinery — AD jets of the metric with whole-array einsum Christoffel/Ricci contractions, own profile assembly, Eulerian frame, SAMPLER-M margins, worst-null, verbatim copy) md5 dcd9c27c4740c9dbaff502c1f4424bdd |
| code/make_g45_figure.py | 4698 | written for this bundle (the figure generator — reads only the bundled records in sources/ and writes figures/g45_level_progression.png) |
| figures/g45_level_progression.png | 244088 | generated at assembly by code/make_g45_figure.py from the bundled records (the lineage progression −1.942246×10⁻⁴ → −1.757074×10⁻⁴ → −1.241372×10⁻⁴ → −6.812653×10⁻⁵, the end-clamped level −6.968823×10⁻⁵ marked as a ring on the centre point, rider G45-E and the §5 fence on the figure's face) |
| sources/CHECKPOINT394.md | 9726 | phase394/CHECKPOINT394.md (Phase 394's phase record — registration, controls, verdict, anatomy, verbatim copy) md5 815bdbf1a498ee6abfad8970047c93ea |
| sources/g45_clamp_margins.json | 210 | gate45/results/g45_clamp_margins.json (Gate-45's clamp-margin record — the clamped centre and both surviving margins, verbatim copy) md5 7562b529c815ae83e3d218841b65cb95 |
| sources/g45_numbers.json | 15144 | gate45/results/g45_numbers.json (Gate-45's §2 deciding reads — the centre, its clamp, and the three controls, verbatim copy) md5 7844f00ee47a2832dab74e9e7d7739d2 |
| sources/g45_ray_box.json | 2785 | gate45/results/g45_ray_box.json (Gate-45's §3 records — the μ_M ray re-reads at all eight registered radii, the worst-DEC re-read, the mixed-centre stored-point read, the FD cross-check, verbatim copy) md5 86439f50e0a7cda2efbdffb75ac969d6 |
| sources/g45_summary.json | 2601 | gate45/results/g45_summary.json (Gate-45's summary — rulings, deciding diffs, the box recount, calibrations, the md5 registry of the gate's inputs, verbatim copy) md5 800ef23e02e090854bfa2c1264086d76 |
| sources/p394_anatomy.json | 2665 | phase394/results/p394_anatomy.json (Phase 394's anatomy record — the ray trace, the diagonal gain, the box-edge disclosure, verbatim copy) md5 81312726c1206879f3a236559e04b434 |
| sources/p394_clamp.json | 1239 | phase394/results/p394_clamp.json (Phase 394's end-clamp record — clamped reads for the centre and the seed, verbatim copy) md5 7e04481ec112da6ad34cdaaa59c52e6f |
| sources/p394_confirmation.json | 1329 | phase394/results/p394_confirmation.json (Phase 394's confirmation record — the centre's full re-read at diff 0.0, its worst-null and margins, verbatim copy) md5 611424f0c0ac49ead895e2ed2b3a9172 |
| sources/p394_controls.json | 2886 | phase394/results/p394_controls.json (Phase 394's VM controls — all diff 0.0, verbatim copy) md5 8549ffaed25f5a102a91cbccbfae40d2 |
| sources/p394_memo.md | 5428 | phase394/results/p394_memo.md (Phase 394's worker memo — the claim set as filed, verbatim copy) md5 7b9da9e7e1cff62f062020ba8f660065 |
| sources/p394_screens.jsonl | 151439 | phase394/results/p394_screens.jsonl (Phase 394's stored screen record — all 349 reads of the registered box, the record Gate-45 recounted for claim (d), verbatim copy) md5 2810edf151add1905c351b5277bb95a2 |
| sources/p394_search_summary.json | 7433 | phase394/results/p394_search_summary.json (Phase 394's search summary — the 349-read box accounting, verbatim copy) md5 b4a9017d092b74a9ea450b7b785071be |

## Numbers check (every deciding number in the final set, transcribed from the bundled records)

Sources of truth for this section: the bundled gate record
`GATE45.md` (§§1–6), the bundled Phase 394 records in
`sources/` (`CHECKPOINT394.md`, `p394_memo.md`,
`p394_confirmation.json`, `p394_clamp.json`,
`p394_controls.json`) and Gate-45's bundled result records in
`sources/` (`g45_numbers.json`, `g45_ray_box.json`,
`g45_clamp_margins.json`, `g45_summary.json`). Values below were
transcribed from those files during packaging — packaging copies,
hashes, and transcribes only; no bundled code was executed except
the figure generator (which reads the bundled records and writes
only the figure). Spot-checks performed against the bundled JSON
records at assembly: 36 checks covering every deciding value
below — the centre's joint/DEC/ρ minima and argmin radii, its
Type-I count, its worst-null and both margins, all three
controls, the clamped centre and both clamped margins, the box
recount, the ray edge and the worst-DEC re-read — 0 unmatched.

- **The centre (G45-A)** — (μ_S, μ_N, μ_M) =
  (0.8015689430763502, 1.3179449338854314, 3.574968377899082) on
  H2's total profiles. Gate batch SET-244 joint
  **−6.812652656191745×10⁻⁵** vs stored
  −6.812652656191736×10⁻⁵ (diff −8.1×10⁻²⁰), NEC-carried at
  r = 15.487804878048781; DEC min gate
  −4.611098054059921×10⁻⁶ / stored −4.611098054060287×10⁻⁶ at
  r = 18.170731707317074, Type-I; ρ min gate
  +9.678145350055485×10⁻⁵ / stored +9.678145350055573×10⁻⁵;
  Type-I count **3311** exact. Margins on the stored values:
  **+5.601066×10⁻⁵** over the seed (−1.241372×10⁻⁴),
  +1.075808×10⁻⁴ over the mixed centre (−1.757074×10⁻⁴),
  +1.260980×10⁻⁴ over L_stat(H2) (−1.942246×10⁻⁴) —
  `GATE45.md` §2, §5; `sources/g45_numbers.json` (`CENTRE`),
  `sources/p394_confirmation.json` (`best`).
- **Pointwise grade (G45-B)** — the exact worst-null at the
  centre's SET NEC argmin: gate −7.17315328450248×10⁻⁵ vs
  stored **−7.173153284502476×10⁻⁵** (diff −4.1×10⁻²⁰); the
  seed's worst-null −1.2477276305772507×10⁻⁴; the margin
  **+5.304123×10⁻⁵** — `GATE45.md` §2, §5;
  `sources/p394_confirmation.json` (`best`, `seed_worst_null`).
- **The end-clamp rider (G45-C)** — clamped centre: gate
  **−6.968822658140869×10⁻⁵** / stored −6.968822658140883×10⁻⁵
  (diff +1.4×10⁻¹⁹); clamp cost **1.561700×10⁻⁶**; the clamped
  level remains above the seed's unclamped level by
  **+5.4449×10⁻⁵** and above L_stat(H2) by **+1.2454×10⁻⁴** —
  both margins survive clamping. The gate's clamp construction
  is cross-validated in C-3: at the mixed centre it reproduces
  Gate-43's clamped joint identically (diff 0.0) and at (1,1,1)
  Gate-41/43's at −5.4×10⁻²⁰ — `GATE45.md` §§1–2, §5;
  `sources/g45_clamp_margins.json`, `sources/p394_clamp.json`.
- **Controls** — (1,1,1): gate shell NEC at the stored argmin
  shell r = 16.21951219512195 is −1.9422459891767224×10⁻⁴ (diff
  +2.7×10⁻²⁰ vs L_stat(H2)); Type-I count **3262** exact. Mixed
  centre: Type-I count **3359** exact; at Gate-43's stored
  argmin point the gate's NEC differs by ~+1×10⁻¹⁹ and its
  exact worst-null by 0.0. Seed: named-point sampled NEC diff
  +3.8×10⁻¹⁹, exact worst-null diff +3.5×10⁻¹⁹; its raw batch
  sampled minimum differs by 7.7×10⁻⁸, inside the C-10 band —
  `GATE45.md` §§1–2; `sources/g45_numbers.json` (`H2S`, `MIX`,
  `SEED`), `sources/p394_controls.json`.
- **The registered box (G45-D)** — recount of the stored
  record: **349** reads, all feasible; **318** beating the
  seed; worst DEC **−5.3917400712468285×10⁻⁵** (the G2 read at
  (0.9323593026620368, 1.1444417317708335, 1.9890136718749998)),
  independently re-read on gate machinery at diff −2.6×10⁻¹⁸
  (Type-I at r = 19.634146341463413); **zero** DEC-saturated
  reads under either threshold (−0.5, −0.9999). The pure μ_M
  ray, independently re-read at all eight registered radii:
  strictly increasing, no turn inside the box, edge joint gate
  −1.0390174144950061×10⁻⁴ / stored −1.0390174144950094×10⁻⁴
  at μ_M = 3.6 — `GATE45.md` §3, §5;
  `sources/g45_summary.json` (`box_recount`),
  `sources/g45_ray_box.json`, `sources/p394_screens.jsonl`.
- **The box-edge rider (G45-E)** — the centre's μ_S =
  0.8015689430763502 sits 0.00157 above the registered box's
  lower edge 0.80, in the disclosed flat cluster (four further
  stored reads within 3.1×10⁻⁷ of its joint, at μ_S ≤ 0.81);
  the phase's fresh polish from the incumbent returned exactly
  its start point; μ_N = 1.3179 (edge 1.35) and μ_M = 3.5750
  (edge 3.60) sit inside their edges, and the ray was still
  rising at the μ_M edge. The centre is quotable only as the
  optimum of the registered box — `GATE45.md` §4, §5;
  `sources/p394_anatomy.json`, `sources/CHECKPOINT394.md`.

Checked: every deciding number in the final set — 0 unmatched.

## Assembly notes

- **Selection, stated:** the gate record entire (`GATE45.md` —
  its §5 is the only quotable form of the set). From gate45/,
  the gate's machinery (`code/g45_lib.py` — Gate-45 ran its own
  computation, so this bundle carries the gate's code) and its
  deciding result records (in `sources/`: the numbers, ray/box,
  clamp-margin and summary JSONs). From phase394/, the
  checkpoint and the worker memo — the phase's verdict records,
  carrying the claim set as filed — and the phase's key records
  the gate judged against (confirmation, clamp, anatomy,
  controls, search summary, and the stored screens the gate
  recounted for claim (d)). The figure
  (`figures/g45_level_progression.png`) was generated at
  assembly by the bundled `code/make_g45_figure.py` from the
  bundled records, per the standing diagrams rule; its values
  were read back from the generator's own output at assembly
  (H2 −1.942245989176723×10⁻⁴; mixed centre
  −1.757073553794524×10⁻⁴; seed −1.241371898379008×10⁻⁴; centre
  −6.812652656191745×10⁻⁵ — the gate read; clamped
  −6.968822658140869×10⁻⁵) and the rendered figure was
  inspected before packaging. **Not bundled:** Phase 394's own
  machinery (`phase394/work/` — the gate judged Phase 394's
  records; its deciding values are carried in the bundled gate
  records and the bundled phase records); Phase 394's laptop
  control record (p394_controls_laptop.json — the laptop was
  NOT ADMITTED as a frame, fourteenth occurrence; the
  checkpoint carries the admission outcome) and its search
  logs (console transcripts of the bundled records' drivers);
  Gate-45's run logs and the `__pycache__` .pyc files under the
  gate work directory (compiled artefacts); the stored profile
  vectors the gate's code reads (identified on the bundled
  code's face and in GATE45.md §6, with their md5s in the
  bundled `g45_summary.json`).
- The verbatim block embedded in the written files was
  diff-verified character-for-character at assembly: the
  GATE45.md §5 claim set in RESULTS.md and in
  RELEASE_v1.36.0.md — both checks exact. The disclosure
  paragraph in RELEASE_v1.36.0.md is in
  gate38-claims/RELEASE_v1.29.0.md's exact form.
- No source file was edited; no bundled .py was executed at
  packaging except the figure generator, and nothing was
  unpickled.
