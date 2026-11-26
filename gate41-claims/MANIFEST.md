# Gate-41 claims bundle - MANIFEST (release v1.32.0)

Every file in this folder, its size in bytes, and where it came from.
Copies are byte-for-byte copies of the named source (md5-verified at
assembly; every copy also cmp-verified against its source at assembly).
This manifest lists every file in the bundle except itself.

| file | bytes | source / traceability |
|---|---|---|
| GATE41.md | 19444 | gate41/GATE41.md (gate record, verbatim copy) md5 737620c6919157101c1fc502100d5845 |
| RESULTS.md | 9208 | written for this bundle (the claim set: the GATE41.md §5 block verbatim — the only quotable form of the Phase 379 claim set; the §5 block in RESULTS.md was diff-verified character-for-character against GATE41.md §5 at assembly) |
| RELEASE_v1.32.0.md | 10205 | written for this bundle (release draft; the GATE41.md §5 claim set embedded verbatim, diff-verified against GATE41.md §5 at assembly; the disclosure paragraph in gate38-claims/RELEASE_v1.29.0.md's exact form; version DOI TBD — minted at release) |
| README_WHATSNEW_v1320.md | 2870 | written for this bundle (prepared README update; applied at upload) |
| code/g41_lib.py | 29914 | gate41/work/g41_lib.py (Gate-41's library — centre assembly from A2's stored profile vectors, jet-algebra Einstein tensor, Eulerian-frame / Hawking–Ellis margins / SET-244 read path, adversary polish and worst-null, verbatim copy) md5 19196fad7679983c0e1f68fef1560dc8 |
| code/g41_calibrate.py | 5011 | gate41/work/g41_calibrate.py (Gate-41's calibration driver — C-0…C-8, run before any audit read, verbatim copy) md5 17239720e460dd46f61b38ec96897318 |
| code/g41_audit.py | 5452 | gate41/work/g41_audit.py (Gate-41's audit driver — the centre, incumbent and end-clamp SET-244 reads, verbatim copy) md5 d22af760ae64621bd643cb18ed9582d8 |
| code/g41_anchor_only.py | 650 | gate41/work/g41_anchor_only.py (Gate-41's anchor-only runner — the frame-admission read executed on the laptop pool, verbatim copy) md5 a6ad74521bf0d714cd635c436bd1fecf |
| sources/CHECKPOINT379.md | 7873 | phase379/CHECKPOINT379.md (Phase 379's phase record — verdict, anatomy, verification state, verbatim copy) md5 53739baf89c8b8f687a711b23faa05fa |
| sources/p379_memo.md | 4308 | phase379/results/p379_memo.md (Phase 379's worker memo — the claim set as filed, verbatim copy) md5 dda5e554fa19674e798404093ef76c6c |
| sources/g41_calibration.json | 1692 | gate41/results/g41_calibration.json (Gate-41's calibration record C-0…C-8, verbatim copy) md5 3573d880de8e4183830d88a929405226 |
| sources/g41_calibration_fd.json | 473 | gate41/results/g41_calibration_fd.json (Gate-41's FD-path calibration record — the from-scratch centred-FD Einstein tensor against the gate's analytic tensor, verbatim copy) md5 9c1c2106aba45eb11f0fae8a19697a70 |
| sources/g41_frame_admission.json | 1057 | gate41/results/g41_frame_admission.json (Gate-41's frame-admission record — the laptop did not reproduce the anchor and was not admitted, verbatim copy) md5 9ce4da25db93ff5abc3de50cc37bc1fb |
| sources/g41_numbers.json | 4197 | gate41/results/g41_numbers.json (Gate-41's numbers record — the centre reads, the incumbent reads with margins, the end-clamp re-read, verbatim copy) md5 6a17e48c4a1cf0d3da2ea4d48112cac1 |

## Numbers check (every deciding number in the final set, transcribed from the bundled records)

Sources of truth for this section: the bundled gate record
`GATE41.md` (§§1–4, §5), the bundled Phase 379 records in
`sources/` (`CHECKPOINT379.md`, `p379_memo.md`), and Gate-41's
bundled result records in `sources/` (`g41_calibration.json`,
`g41_calibration_fd.json`, `g41_frame_admission.json`,
`g41_numbers.json`). Values below were transcribed from those
files during packaging — packaging copies, hashes, and transcribes
only; no bundled code was executed and nothing was unpickled.
Spot-checks performed against the bundled JSON records at
assembly: both incumbents' deciding values and margins, both
centres' zero-displacement reads and floor minima, and the
end-clamp values match `sources/g41_numbers.json` digit-for-digit
at the precision printed there, and the stationary NEC anchor
matches `sources/g41_calibration.json`.

- **Stationary anchor (the bar at the A2 centre)** — Phase 344's
  A2 centre reads, on the gate's machinery (C-4): NEC min
  **−2.319453×10⁻⁴** (gate read −2.319453132752996×10⁻⁴, diff
  −1.36×10⁻¹⁹, argmin r = 16.2195), DEC min **−2.233693×10⁻⁴**
  (gate read −2.233693204455982×10⁻⁴, diff +8.13×10⁻²⁰, argmin
  r = 19.3902), ρ min 8.638077678074035×10⁻⁵ (diff +2.17×10⁻¹⁹),
  Type-I count 3535 exact — `GATE41.md` §1 (C-4);
  `sources/g41_calibration.json`.
- **H2 incumbent (G41-A)** — μ = 1.15 centre, K = 17: NEC min
  **−1.942246×10⁻⁴** (gate read −1.9422459891767262×10⁻⁴ at
  r = 16.2195, diff −3.52×10⁻¹⁹), DEC min **−1.898259×10⁻⁴**
  (−1.8982585080461542×10⁻⁴, diff +1.63×10⁻¹⁹), ρ min
  **+8.789654×10⁻⁵** (+8.789653555683191×10⁻⁵, diff
  +9.49×10⁻²⁰), Type-I count 3262 exact. Margins: over its centre
  bar **+8.957×10⁻⁶** (gate +8.956535×10⁻⁶; stored
  +8.956534894425722×10⁻⁶), over the Gate-40-verified dwelling
  ceiling **+1.571×10⁻⁵** (gate +1.571391×10⁻⁵; stored
  +1.5713909041498343×10⁻⁵); polished depth
  −1.4402430840320605×10⁻⁴ (diff +3.25×10⁻¹⁹; past the −0.0034
  C2 bar by a factor of 24); exact pointwise worst-null at the
  SET NEC argmin −1.9432881962794707×10⁻⁴ (diff −3.25×10⁻¹⁹),
  itself above the ceiling by +1.561×10⁻⁵ — `GATE41.md` §2, §5;
  `sources/g41_numbers.json` (`B_incumbent_H2`).
- **H1 incumbent (G41-B)** — μ = 1.1125 centre, K = 17: NEC min
  **−2.014605×10⁻⁴** (gate read −2.014605242909165×10⁻⁴ at
  r = 17.6829, diff −3.52×10⁻¹⁹), DEC min **−1.964171×10⁻⁴**
  (−1.9641708622922396×10⁻⁴, diff −4.34×10⁻¹⁹), ρ min
  **+8.750851×10⁻⁵** (+8.750850886168864×10⁻⁵, diff
  +4.07×10⁻²⁰), Type-I count 3310 exact. Margin over its centre
  bar (= the dwelling ceiling) **+8.478×10⁻⁶** (gate
  +8.477984×10⁻⁶; stored +8.47798366825447×10⁻⁶); polished depth
  −1.6697787772751145×10⁻⁴ (diff −8.67×10⁻¹⁹); exact worst-null
  −2.0234192402649137×10⁻⁴ (diff −3.52×10⁻¹⁹), itself above the
  centre bar by +7.597×10⁻⁶ — `GATE41.md` §2, §5;
  `sources/g41_numbers.json` (`B_incumbent_H1`).
- **The centres (G41-C)** — gate-built μ-scalings of A2's totals,
  zero-displacement reads reproducing Phase 374's bottom
  identities at roundoff: H1 (μ = 1.1125): NEC
  −2.0993850795917053×10⁻⁴, DEC −1.941081222390092×10⁻⁴,
  ρ min 8.764071936093984×10⁻⁵, max |diff| vs identity
  3.25×10⁻¹⁹; H2 (μ = 1.15): NEC −2.0318113381209823×10⁻⁴, DEC
  −1.854699056943026×10⁻⁴, ρ min 8.801281960223575×10⁻⁵, max
  |diff| 3.79×10⁻¹⁹. Floor minima on FINE_R reproduce Phase
  379's CTL-379-F at exactly 0.0 — H1: N 1.1125340342235222,
  M 1.1206906539640158; H2: N 1.1500351814445395,
  M 1.1247588782549376 — `GATE41.md` §3, §5;
  `sources/g41_numbers.json` (`A_centre_H1`, `A_centre_H2`).
- **The end-clamp rider (G41-E)** — H2's stored end-knot values
  read from the vectors: S −8.141616667879931×10⁻⁵ (r = 10),
  **−7.926584743685476×10⁻³** (r = 20); N
  −3.404403920298938×10⁻⁵, +7.01931505368771×10⁻⁶; M
  +2.5452310899203476×10⁻⁵, +2.529041046983001×10⁻⁵. The gate's
  end-clamp re-read: NEC min −1.956241449779669×10⁻⁴ (diff
  +8.13×10⁻²⁰), DEC min −2.087299309761317×10⁻⁴ (diff
  −5.96×10⁻¹⁹), ρ min 8.793529206482109×10⁻⁵ — joint
  (DEC-carried) **−2.087299×10⁻⁴**, clamp cost
  **1.450533×10⁻⁵**; the clamped level falls below L_stat(1.15)
  by **−5.549×10⁻⁶** (−5.548797164033699×10⁻⁶ in the record) —
  the margin over the centre bar does not survive clamping —
  and remains above the dwelling ceiling by **+1.208577×10⁻⁶**
  (+1.2085769830389218×10⁻⁶) — the classification margin
  survives in reduced form — `GATE41.md` §4, §5;
  `sources/g41_numbers.json` (`C_endclamp_H2`).
- **Calibrations** — C-0 vectors max diff **0.0**; C-1 trivial
  limit exactly **0.0**; C-2 FD path: max |ΔT| falls
  **4.30×10⁻⁵ → 5.36×10⁻⁸** over h = 0.1 → 0.0125; C-3
  density-split identity max diff **1.52×10⁻¹⁸** at all 6642 SET
  points of the anchor; C-5 μ ≡ 1 reduction max diff **0.0**;
  C-6 anchor depth reproduced at diff −3.25×10⁻¹⁹; C-7 frame
  admission: the laptop did NOT reproduce the anchor (NEC
  −1.05×10⁻⁶, WEC **−8.31×10⁻⁶**, SEC −5.74×10⁻⁷; DEC and ρ at
  roundoff — the pattern a seventh time) — every deciding read
  is a VM read; C-8 the disclosed frame-association calibration
  incident (first anchor run missed the NEC/WEC/SEC minima by up
  to 4.95×10⁻⁶; root cause the γ association, ~4×10⁻¹⁶; with γ
  assembled in the definition's association every anchor field
  collapsed to roundoff). Max |gate − stored| over all deciding
  fields: **3.9×10⁻¹⁸** (the H1 WEC minimum); every
  NEC/DEC/ρ/depth/worst-null diff ≤ **8.7×10⁻¹⁹**. Audit
  programme: 5 SET-244 reads, 33,210 point reads, all on the
  VM — `GATE41.md` §1; `sources/g41_calibration.json`,
  `sources/g41_calibration_fd.json`,
  `sources/g41_frame_admission.json`,
  `sources/g41_numbers.json`.

Checked: every deciding number in the final set — 0 unmatched.

## Assembly notes

- **Selection, stated:** the gate record entire (`GATE41.md` —
  its §5 is the only quotable form of the set). From gate41/, the
  gate's machinery entire (four files in `code/` — Gate-41 ran
  its own computation, so this bundle carries the gate's code)
  and its deciding result records (in `sources/`: the
  calibration, calibration-FD, frame admission and numbers
  JSONs). From phase379/, the checkpoint and the worker memo —
  the phase's verdict records, carrying the claim set as filed.
  **Not bundled:** Phase 379's own machinery and its
  control/confirmation/state JSONs, screen JSONLs and search
  logs (the gate judged Phase 379's records; its deciding values
  are carried in the bundled gate records); the `__pycache__`
  .pyc files under the gate work directory (compiled artefacts);
  the stored Phase 344 A2 centre files the gate's assembly reads
  (identified on the bundled code's face).
- The verbatim block embedded in the written files was
  diff-verified character-for-character at assembly: the
  GATE41.md §5 claim set in RESULTS.md and in
  RELEASE_v1.32.0.md — both checks exact. The disclosure
  paragraph in RELEASE_v1.32.0.md is in
  gate38-claims/RELEASE_v1.29.0.md's exact form.
- No source file was edited; no bundled .py was executed and
  nothing was unpickled at any point in packaging.
