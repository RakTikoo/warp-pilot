# Gate-43 claims bundle - MANIFEST (release v1.34.0)

Every file in this folder, its size in bytes, and where it came from.
Copies are byte-for-byte copies of the named source (md5-verified at
assembly; every copy also cmp-verified against its source at assembly).
This manifest lists every file in the bundle except itself.

| file | bytes | source / traceability |
|---|---|---|
| GATE43.md | 18949 | gate43/GATE43.md (gate record, verbatim copy) md5 1fc62511f4b33d47de96771164ff3739 |
| RESULTS.md | 9612 | written for this bundle (the claim set: the GATE43.md §5 block verbatim — the only quotable form of the Phase 389 claim set; the §5 block in RESULTS.md was diff-verified character-for-character against GATE43.md §5 at assembly) |
| RELEASE_v1.34.0.md | 11825 | written for this bundle (release draft; the GATE43.md §5 claim set embedded verbatim, diff-verified against GATE43.md §5 at assembly; the disclosure paragraph in gate38-claims/RELEASE_v1.29.0.md's exact form; version DOI TBD — minted at release) |
| README_WHATSNEW_v1340.md | 4424 | written for this bundle (prepared README update; applied at upload) |
| code/g43_lib.py | 31253 | gate43/work/g43_lib.py (Gate-43's library — forward-mode second-order AD jets of the metric in Cartesian coordinates, own profile assembly, Eulerian frame, SAMPLER-M margins, worst-null and adversary polish, verbatim copy) md5 7d49598e3d047e7c445026dada68fcfb |
| code/g43_calibrate.py | 4476 | gate43/work/g43_calibrate.py (Gate-43's calibration driver — the C-0…C-9 calibrations and the FD cross-path, verbatim copy) md5 ee2a9d511d4051170f43ed61ff1254a2 |
| code/g43_audit.py | 4822 | gate43/work/g43_audit.py (Gate-43's audit driver — the deciding SET-244 reads at the centre, the controls and the clamped totals, verbatim copy) md5 816b6c3119c03bf83ee8ca6fe97c075c |
| code/g43_diag.py | 4165 | gate43/work/g43_diag.py (Gate-43's diagnostic driver — the named-point reads at the stored argmins and the lineage comparison, verbatim copy) md5 f1f97c2dab05c8a5ea4d8c2b9502f372 |
| code/g43_cube.py | 5602 | gate43/work/g43_cube.py (Gate-43's cube driver — the 125-point scaling cube, the quadratic fit, the corner and identity reads, verbatim copy) md5 db98a726df2807f9dcaa8d2078ec9f63 |
| sources/CHECKPOINT389.md | 6802 | phase389/CHECKPOINT389.md (Phase 389's phase record — registration, verdict, anatomy, verification state, verbatim copy) md5 153982d0d0094107fed8b74ddf984fe7 |
| sources/p389_memo.md | 11013 | phase389/results/p389_memo.md (Phase 389's worker memo — the claim set as filed, verbatim copy) md5 fa30ca36662cca0464742e28d56ad4a7 |
| sources/g43_numbers.json | 8850 | gate43/results/g43_numbers.json (Gate-43's deciding reads — the centre, both controls and the clamped centre, full SET-244 records with diffs against the stored reads, verbatim copy) md5 bb294ce8bc620cc41edc3e25d6af4f4b |
| sources/g43_diag.json | 2695 | gate43/results/g43_diag.json (Gate-43's named-point record — the gate reads at the stored argmin points with their roundoff diffs, and the lineage comparison, verbatim copy) md5 fa8547df8a94c2ba77c8446cb30fa805 |
| sources/g43_calibration.json | 1210 | gate43/results/g43_calibration.json (Gate-43's calibration record — C-0…C-9, verbatim copy) md5 265541d425331550908cbc0f2da256ec |
| sources/g43_calibration_fd.json | 409 | gate43/results/g43_calibration_fd.json (Gate-43's FD cross-path record — the centred-difference convergence at both test points, verbatim copy) md5 dbaa753654f949eaca2ff83752c019bc |
| sources/g43_frame_check.json | 197 | gate43/results/g43_frame_check.json (Gate-43's C-10 frame-check record — the coordinate-tensor, eigenvalue and That component differences between the two evaluation paths, verbatim copy) md5 f35618aec49d78eb0017b9bd68ecc19b |
| sources/g43_fit.json | 2417 | gate43/results/g43_fit.json (Gate-43's surface record — the quadratic fit, the axis finite differences, the μ_M identity and the DEC-saturated corner, verbatim copy) md5 b240dda7cfcbae5e1da2b6b738d20386 |
| sources/g43_cube.jsonl | 32571 | gate43/results/g43_cube.jsonl (Gate-43's cube record — the 125 SET-244 reads of the gate's own G1 cube, verbatim copy) md5 0d706d92151d8973a923f2afa74fcb1c |

## Numbers check (every deciding number in the final set, transcribed from the bundled records)

Sources of truth for this section: the bundled gate record
`GATE43.md` (§§1–6), the bundled Phase 389 records in
`sources/` (`CHECKPOINT389.md`, `p389_memo.md`), and Gate-43's
bundled result records in `sources/` (`g43_numbers.json`,
`g43_diag.json`, `g43_calibration.json`,
`g43_calibration_fd.json`, `g43_frame_check.json`,
`g43_fit.json`, `g43_cube.jsonl`). Values below were transcribed
from those files during packaging — packaging copies, hashes, and
transcribes only; no bundled code was executed and nothing was
unpickled. Spot-checks performed against the bundled JSON records
at assembly: 44 checks covering every deciding value below —
the mixed centre's deciding reads and their diffs, the clamped
centre's full record, both controls, the calibrations, the FD
cross-path residuals, the frame-check differences, the fit, the
corner and the identity, and the derived margins recomputed from
the bundled values — 0 unmatched.

- **Calibrations (C-0…C-9)** — the gate's A2 and H2 correction
  vectors agree with both stored artefacts each at max diff
  **0.0** (C-0); the trivial limit is exactly 0.0 (C-1);
  centre(1.0) ≡ A2 totals at max diff 0.0 (C-5); the A2 anchor
  SET-244 read (C-4): NEC min **−2.3194531327529964×10⁻⁴**,
  diffs NEC −2.7×10⁻²⁰, DEC +1.4×10⁻¹⁹, ρ +1.2×10⁻¹⁹, Type-I
  count **3535** exact, argmin radii exact; the density-split
  identity (C-3) holds at max diff **1.4094628242311558×10⁻¹⁸**
  over all 6642 A2 SET points; the FD cross-path (C-2) converges
  to the gate's AD tensor — at the NEC argmin, residuals
  1.1214808286777412×10⁻⁶ (h = 0.1) → **2.2315282217563737×10⁻¹²**
  (h = 0.0125); at the generic point 3.7790023415188573×10⁻⁷ →
  **3.000094747282467×10⁻¹³**; the clamp construction at (1,1,1)
  against Gate-41 §4 (C-9): clamped DEC diff **+3.8×10⁻¹⁹**,
  ρ diff −1.6×10⁻¹⁹, clamped joint −2.087299309761313×10⁻⁴ vs
  Gate-41's −2.087299309761317×10⁻⁴; the clamped NEC minimum
  differs (gate −1.952837×10⁻⁴, Gate-41 −1.956241×10⁻⁴) — the
  C-10 band, below — `GATE43.md` §1;
  `sources/g43_calibration.json`,
  `sources/g43_calibration_fd.json`.
- **The frame-convention band (C-10)** — two evaluation paths
  inside the gate's own library: coordinate-basis tensor max
  diff **3.3610267347050637×10⁻¹⁸**, mixed-tensor eigenvalue max
  diff **8.538092108323347×10⁻¹⁹**, That component max diff
  **2.0935446501358453×10⁻⁴** at individual non-Type-I points;
  at (1,1,1) the two paths read NEC minima −1.942242×10⁻⁴ and
  −1.949532×10⁻⁴ around the stored −1.942246×10⁻⁴, above the
  exact worst-null floor −1.951198×10⁻⁴ (the gate's batch
  worst-null at the centre, −0.00019511981961721186) —
  `GATE43.md` §1 (C-10); `sources/g43_frame_check.json`,
  `sources/g43_numbers.json` (`centre_111`).
- **The mixed centre (G43-A)** — at the stored NEC argmin point
  (r = 12.560975609756097), the gate's named-point NEC is
  **−0.00017570735537945236**, diff **+5.421010862427522×10⁻²⁰**
  against the stored −1.7570735537945242×10⁻⁴; the gate's batch
  record: DEC min **−0.00015670690855768764** (Type-I at
  r = 19.634146341463413; diff vs stored −8.131516293641283×10⁻¹⁹),
  ρ min **8.936712674433252×10⁻⁵** (stored
  8.936712674433238×10⁻⁵; diff +1.4×10⁻¹⁹), Type-I count
  **3359** exact (fraction 0.5057211683227943), adversary-polish
  depth **−9.660225437141889×10⁻⁵** (diff +6.505213034913027×10⁻¹⁹);
  the joint level is min(NEC, DEC) = **−1.757074×10⁻⁴**,
  +1.851724×10⁻⁵ above L_stat(H2) (recomputed from the bundled
  values at assembly) — `GATE43.md` §2;
  `sources/g43_diag.json` (`mixed.at_stored_argmin`),
  `sources/g43_numbers.json` (`mixed`).
- **Pointwise grade (G43-B)** — the gate's exact worst-null at
  the stored argmin is **−0.00017703703917379299**, diff
  **+8.131516293641283×10⁻²⁰** against the stored
  −1.7703703917379307×10⁻⁴; the margin over the bar recomputed
  from the stored numbers at assembly:
  1.9422459891767227×10⁻⁴ − 1.7703703917379307×10⁻⁴ =
  **+1.7188×10⁻⁵** (the restated figure; the phase prose's
  +1.721×10⁻⁵ does not reproduce) — `GATE43.md` §2;
  `sources/g43_diag.json`.
- **Controls** — (1,1,1): Type-I count **3262** exact; the
  named-point diffs at the stored argmin (NEC −8.1×10⁻²⁰,
  DEC −2.2×10⁻¹⁹, ρ −2.7×10⁻²⁰, depth +5.4×10⁻¹⁹, worst-null
  +2.7×10⁻¹⁹) return L_stat(H2) = −1.942246×10⁻⁴. Phase 383's
  mixed point (1.225, 1.30, 1.30): DEC min
  **−0.0001287489042939162** (diff −1.1×10⁻¹⁹ against the stored
  −1.287489042939161×10⁻⁴); NEC minimum sampled-carried, gate
  **−0.00019971527734957792** vs stored −1.995404×10⁻⁴, inside
  the C-10 band; the point's deciding content unchanged —
  `GATE43.md` §2; `sources/g43_numbers.json` (`centre_111`,
  `mix_383pt`), `sources/g43_diag.json`.
- **The end-clamp re-read (G43-E)** — the clamped centre's full
  record: joint (NEC min) **−0.00017669632754376664** at
  r = 12.560975609756097 (the quotable −1.766963×10⁻⁴), DEC min
  **−0.00016608234692851046** (Type-I, r = 19.634146341463413),
  ρ min **8.938934839487046×10⁻⁵**, Type-I count **3442**,
  adversary depth **−9.659258092343788×10⁻⁵**. Clamp cost on
  the gate's consistent statistic: 1.03×10⁻⁶ (recomputed at
  assembly from the bundled batch joints, −1.756688×10⁻⁴ →
  −1.766963×10⁻⁴); against the stored unclamped level 9.9×10⁻⁷.
  Margins recomputed at assembly: over L_stat(H2)
  **+1.7528×10⁻⁵**; over the dwelling ceiling (−2.099385×10⁻⁴)
  **+3.3242×10⁻⁵** — both survive — `GATE43.md` §4;
  `sources/g43_numbers.json` (`mixed_clamped`).
- **The surface (G43-C)** — the gate's fit over its own **116**
  non-saturated cube points: gradient at the centre
  (**−0.0001088784230723916**, **+0.00011075392187163483**,
  **+8.29538295022671×10⁻⁵**) per unit μ, against the stored
  (−0.00010955057573860948, +0.00011146963771141866,
  +8.211005563920505×10⁻⁵); max fit residual
  **2.0955764001968127×10⁻⁵** (stored 2.092730871046218×10⁻⁵);
  Hessian eigenvalues gate (−5.389794713493514×10⁻⁵,
  −8.341682471950254×10⁻⁴, **−3.2800976863871572×10⁻³**),
  stored (−3.3301983243515187×10⁻³, −8.377994225485973×10⁻⁴,
  −6.0639495375965976×10⁻⁵) — all negative in both fits. Axis
  finite differences (h = 0.05): μ_S gate
  **−0.00014938242913410102** vs stored
  −0.0001493824291340853 (diff 1.6×10⁻¹⁷); μ_N gate
  +0.00015377712656999804 vs stored +0.00015377712657000672;
  μ_M gate −3.597852462225903×10⁻⁵ vs stored
  −3.491179995458802×10⁻⁵ — `GATE43.md` §3;
  `sources/g43_fit.json`, `sources/g43_cube.jsonl`.
- **Side findings (G43-D)** — the μ_M near-identity from the
  gate's own cube rows: joint diffs 3.5236570605778894×10⁻¹⁹
  (μ = 0.95), **5.421010862427522×10⁻¹⁹** (1.05),
  4.336808689942018×10⁻¹⁹ (1.10), argmin radii identical for
  both members of each pair — gate bound ≤ 5.4×10⁻¹⁹. The
  DEC-saturated corner: the gate's criterion selects exactly
  the stored **9** triples (`matches_stored_9 = True`), DEC
  minima in **[−1.000000597050228, −1.0000003278917804]**
  (the pinned −1.0000003…−1.0000006), argmin radii
  (17.195121951219512, 17.682926829268293) — `GATE43.md` §3;
  `sources/g43_fit.json` (`identity`, `corner`).

Checked: every deciding number in the final set — 0 unmatched.

## Assembly notes

- **Selection, stated:** the gate record entire (`GATE43.md` —
  its §5 is the only quotable form of the set). From gate43/, the
  gate's machinery entire (five files in `code/` — Gate-43 ran
  its own computation, so this bundle carries the gate's code)
  and its deciding result records (in `sources/`: the numbers,
  diagnostic, calibration, FD-calibration, frame-check and fit
  JSONs and the cube JSONL). From phase389/, the checkpoint and
  the worker memo — the phase's verdict records, carrying the
  claim set as filed.
  **Not bundled:** Phase 389's own machinery and its
  control/search/screen JSONs and logs (the gate judged Phase
  389's records; its deciding values are carried in the bundled
  gate records); Gate-43's run logs (g43_audit.log,
  g43_calibrate.log, g43_cube.log, g43_diag.log — console
  transcripts of the bundled drivers); the `__pycache__`
  .pyc files under the gate work directory (compiled artefacts);
  the stored design vectors and state files the gate's code
  reads (identified on the bundled code's face and in
  GATE43.md §6, with their md5s).
- The verbatim block embedded in the written files was
  diff-verified character-for-character at assembly: the
  GATE43.md §5 claim set in RESULTS.md and in
  RELEASE_v1.34.0.md — both checks exact. The disclosure
  paragraph in RELEASE_v1.34.0.md is in
  gate38-claims/RELEASE_v1.29.0.md's exact form.
- No source file was edited; no bundled .py was executed and
  nothing was unpickled at any point in packaging.
