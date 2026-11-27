# Gate-53 CHECKPOINT (working record)

**Charge:** ledger entry 1086 (FU-P408-1) — independent
verification of the Phase 408 claim set under fresh machinery:
(a) A-6's legality at β = 0.193359375, first question the thin
margin (worst SEC +3.613×10⁻⁸ @ r = 5.0, 6.8× the phase's FD
floor); (b) the Arm B control (clipped seed at exactly RW-5's
ceiling with RW-5's bracket); (c) Amendment A-408-1's handling;
(d) the ladder statement. **Deliverables:** `GATE53.md`
(quotable set §7, G53-A…G53-E, riders G53-R1…R3) + this
checkpoint. No ledger append, no publication, no user contact.
**Verdicts:** (a) SURVIVES AS FENCED · (b) SURVIVES ·
(c) SURVIVES AS FENCED · (d) SURVIVES RESTATED · controls
SURVIVE with calibration note C-1.

## Machinery (fresh, gate53/work/)

- `g53_lib.py` — the gate's own graded-family builder
  (n_c ∈ {8, 12, 16}) written for this gate in the
  gate-lineage builder pattern (Gates 42/44/51), from the
  construction registered in CHECKPOINT386 §2 and the shared
  (10,20)-class definitions. Box-4 stages 2–4 by the
  **spline-antiderivative scheme** (primary) — a different
  numerical organisation from the phase's
  cumulative-trapezoid + Hermite scheme, which is carried as
  `stage_scheme="trapH"` for internal cross-check.
  Instruments: gate6/wa_auditor.py + phase50/p503_lib.audit4
  (the registered pair, imported; nothing imported from any
  phase work dir). The gate's own summary / legality /
  q-read / point-set code. Registered set pts_1020_control
  (1,430 rows) regenerated from the shared definition.
- Scripts: `g53_records.py` (hashes, embedding recomputation,
  chain calibration), `g53_audits.py` (controls + B-2 full
  audits), `g53_thin.py` (A-6 registered audits, spacing
  ladder, first dense scan, deciding-point check),
  `g53_dense.py` (dip confirmation, radial profile, dense
  scans of the controls, corrected Richardson), `g53_laptop.py`
  (laptop admission control; ran on the pool at ~/work/g53/
  with a stub p503_lib — audit4 not run on the laptop).
- Frame: VM for all deciding reads; programme venv
  (numpy 2.5.5 / scipy 1.18.1) everywhere; laptop venv
  identical versions.

## Execution log

1. **Records (g53_records.json).** All six vectors
   hash-verified against their stored records (A-6
   6461827f…, B-2/clipped d228c82e…, unclipped a0201be1…,
   RW-5 44719b50…, E2-1 61679383…). B-2's subject vector is
   byte-identical to the amendment's clipped vector. The
   clip differs from the unclipped embedding at exactly one
   index (13: −2.3199648239179234 → −2.25; excess
   0.06996482391792336).
   **Embedding recomputed independently** (log φ of RW-5 on
   linspace(R1,R2,20001), lstsq onto the 16-mode basis,
   a/q/r_m carried): reproduces the stored unclipped vector
   at **max diff 0.0**, hash match, residual RMS
   9.207430281480095×10⁻³ / max 3.673295654339093×10⁻² —
   identical to the phase's stored record.
   **Builder calibration:** chain reads vs stored —
   RW-5 rel diffs: M 1.45×10⁻¹⁵, ρ_max 2.86×10⁻¹¹,
   λ 5.59×10⁻¹², k 1.02×10⁻¹¹; E2-1 ≤ 3.1×10⁻¹¹;
   A-6 ≤ 2.84×10⁻¹¹ (ρ_max), λ 4.8×10⁻¹²; B-2 ≤ 2.83×10⁻¹¹.
   Internal scheme cross-check (spline vs trapH): λ abs diff
   ≤ 7.6×10⁻¹², k ≤ 2.5×10⁻¹³, ρ_max ≤ 9.4×10⁻¹⁵. c = 0
   profile vs closed-form step response: max normalised diff
   2.05×10⁻¹¹. Construction grid 1,200,707 points.
2. **Controls + Arm B audits (g53_audits_*.json)** — full
   registered audits (wa + audit4, both spacings):
   - y_his @ 0.1363 LEGAL: SEC +3.4041777787759174×10⁻⁷
     @ 5.0, 109.5× floor, Type-I 1.000, audit4 +3.395770×10⁻⁷.
     @ 0.1364 LEGAL pointwise: SEC +3.3866486242770997×10⁻⁷
     (Gate-51's C-1 digit reproduced; "fails" = rating sense
     only).
   - E2-1 @ 0.191796875 LEGAL: SEC +7.075488945987914×10⁻⁸
     @ 6.0, 13.4× floor, audit4 +5.407160×10⁻⁸.
   - RW-5 @ 0.192578125 LEGAL: SEC +6.055585116608624×10⁻⁷
     @ 3.75, 106.5× floor, audit4 +6.050012×10⁻⁷ (class);
     @ 0.195078125 FAILS compound: SEC
     −1.031585673360951×10⁻⁵ @ 9.75, Type-I 0.98499,
     sampled-NEC −8.16×10⁻⁷, audit4 −1.032461×10⁻⁵.
   - B-2 @ 0.192578125 LEGAL: SEC +6.042169269330512×10⁻⁷
     @ 3.75, 106.0× floor, Type-I 1.000 both spacings,
     audit4 +6.036612×10⁻⁷; @ 0.195078125 FAILS: SEC
     −1.274694525376475×10⁻⁵ @ 9.75, Type-I 0.98593,
     audit4 −1.275580×10⁻⁵. Phase stored digits reproduced
     to ≤ 7.9×10⁻¹³.
3. **A-6 registered audits (g53_thin.json).**
   @ 0.193359375 LEGAL: SEC +3.6129700650270704×10⁻⁸ @ 5.0
   (phase +3.612959826980664×10⁻⁸), 6.82× floor, Type-I
   1.000, per-EC NEC/WEC/DEC +6.817165×10⁻⁷ @ 3.75,
   sampled-NEC +1.414×10⁻⁷, audit4 +2.674508×10⁻⁸ /
   +2.674595×10⁻⁸, q_max 0.99341 @ 23.0.
   @ 0.195859375 FAILS: SEC −1.2569692615417962×10⁻⁵
   @ 9.75, Type-I 0.98499, audit4 −1.258116×10⁻⁵.
4. **Spacing ladder (g53_thin.json)** — A-6 @ 0.193359375,
   registered set, wa: SEC +3.612970×10⁻⁸ (h 0.0375) /
   +2.909530×10⁻⁸ (0.01875) / +2.733434×10⁻⁸ (0.009375) /
   +2.689501×10⁻⁸ (0.0046875), all @ r = 5.0, Type-I 1.000;
   floors 5.2958 / 5.0981 / 5.0206 / 5.0028 ×10⁻⁹; ratios
   6.82 / 5.71 / 5.44 / 5.38. Sampled-NEC 1.414 / 1.404 /
   1.401 / 1.401 ×10⁻⁷.
   **Corrected Richardson limits** (g53_dense.py, from the
   stored ladder): +2.675049×10⁻⁸, +2.674735×10⁻⁸,
   +2.674856×10⁻⁸ — spread 3.2×10⁻¹¹; audit4's +2.6745×10⁻⁸
   concurs. The margin's h → 0 limit is +2.675×10⁻⁸.
   Deciding-point check (the stored r = 5.0 point,
   h = 0.009375): margins NEC/WEC/DEC +4.189347×10⁻⁶,
   SEC +2.733434×10⁻⁸, Type-I true; sampled-NEC 162-dir
   +1.281×10⁻⁶, 642-dir +1.197×10⁻⁶ (both positive).
5. **Dense radial sampling (g53_thin.json + g53_dense.json)**
   — radii 2.6–10.6 step 0.05 × DIRS26, h = 0.009375, wa:
   - A-6 @ 0.193359375: SEC min **−1.252873×10⁻⁶ @ r = 5.4**
     (point [−0.21601601, −4.67154547, −2.7]).
     Confirmation at that point: wa SEC −1.237779×10⁻⁶
     (h 0.0375) → −1.249850×10⁻⁶ → −1.252873×10⁻⁶ →
     −1.253628×10⁻⁶ (h 0.0046875); audit4 −1.253881×10⁻⁶ /
     −1.253882×10⁻⁶; NEC/WEC/DEC +6.076×10⁻⁶, Type-I true,
     sampled-NEC +1.570×10⁻⁶. Radial profile (step 0.02,
     direction-min SEC): +9.042×10⁻⁷ @ 4.8, +2.733×10⁻⁸
     @ 5.0, negative on [5.02, 5.84], min −1.257492×10⁻⁶
     @ 5.42, +2.127×10⁻⁶ @ 6.2.
   - RW-5 @ 0.192578125: SEC min **+2.975032×10⁻⁷ @ 3.55**
     (positive; registered +6.056×10⁻⁷).
   - E2-1 @ 0.191796875: SEC min **−1.161957×10⁻⁶ @ 9.95**
     (dips; registered +7.075×10⁻⁸).
   - y_his @ 0.1363: SEC min **+5.448910×10⁻⁸ @ 4.0**
     (positive; registered +3.404×10⁻⁷).
   - B-2 @ 0.192578125: SEC min **−8.610895×10⁻⁷ @ 9.95**
     (dips; registered +6.042×10⁻⁷).
   Dense-scan floor proxies: 3.8×10⁻⁹ – 1.03×10⁻⁸.
6. **Laptop admission control (g53_laptop_out.json)** —
   gate builder + wa on the pool (numpy 2.5.5 / scipy
   1.18.1): A-6 chain reads agree with the VM's to
   ≤ 2×10⁻¹⁵ (ρ_max 3.286516818707203×10⁻⁴ vs VM
   …201×10⁻⁴); wa @ 0.193359375, h = 0.0375: SEC
   +3.612965823764544×10⁻⁸ @ 5.0 vs VM
   +3.6129700650270704×10⁻⁸ (**abs diff 4.2×10⁻¹⁴**),
   Type-I 1.0, floor 5.295817×10⁻⁹. Sampled-NEC differs
   (2.268×10⁻⁷ laptop vs 1.414×10⁻⁷ VM vs 1.334×10⁻⁷
   phase) — C-2 diagnostic class, positive everywhere.
   **Admitted as corroboration for deciding eigenvalue
   reads; deciding reads are the VM's.**
7. **Ladder-statement record checks (claim d)** — from
   p408_search.json / p408_verdicts.json / the checkpoints:
   Arm A DE 107 gens / 6,912 evals, done, best 0.193359375,
   final mean 0.19277; resumption cross-check 64/64 exact,
   best exactly 0.191015625; staged control (A-CONTROL)
   home ceiling 0.191015625 = its screening level. Arm B DE
   140 gens / 9,024 evals, done, best_y = the clipped seed
   itself (sha d228c82e…, `best_y_is_clipped_seed: true`),
   best flat 0.192578125 at every recorded generation, mean
   0.10145 → 0.19034 (still rising at cap). C-408-5 pool
   gate record: clipped seed screens at exactly
   0.19257812500000002 on both instruments, PASSED. A-6's
   bound-sitters from the stored vector: c idx 0 = +2.25
   only (all other coordinates strictly inside the Arm A
   box; a-block ≤ 8.341 < 12; q = 1.7532; r_m = 16.2385).
   Dose–response increments recomputed: +0.05041875,
   +0.003125, +0.001953125, +0.00078125, +0.00078125.
   Margin thinning: 6.055585×10⁻⁷ / 3.612970×10⁻⁸ = 16.76
   (absolute); 106.5 / 6.82 = 15.6 (floor multiples,
   gate reads; phase figures 106.5 / 6.8 = 15.7).

## Incidents and disclosures

1. The benign `RuntimeWarning: invalid value encountered in
   log` from the builder's exterior branch (values discarded
   by the enclosing `np.where`) — inherited gate-lineage
   pattern; chain reads reproduce stored digits, no read
   touched.
2. **The gate's own Richardson slip:** `g53_thin.py`'s first
   extrapolation used M(h) + (M(h) − M(h/2))/3 (the
   wrong-direction formula), printing limits
   [3.85×10⁻⁸, 2.97×10⁻⁸, 2.75×10⁻⁸]. Caught on review
   against audit4's read; the corrected limits were
   recomputed from the stored ladder in `g53_dense.py`
   ([2.675049, 2.674735, 2.674856]×10⁻⁸) and are the ones
   quoted. No audit read was affected — the ladder values
   themselves were always stored correctly.
3. The first laptop staging attempt failed on shell quoting
   of the SSH ProxyCommand (no state changed on either
   machine); staging was redone via a script file and the
   control ran clean.
4. Direction-sampled diagnostics (sampled-NEC minima,
   q_max) differ between instruments/machines at the
   first-digit level while remaining positive / < 1 as the
   case requires — recorded as C-2 in GATE53.md; no ruling
   turns on one.

## Verdict derivation (summary)

- (a) The registered claim reproduces exactly on fresh
  machinery at both spacings with the second path agreeing;
  the bracket reproduces. On the charged FD-floor question,
  the deciding margin has a stable h → 0 limit
  (+2.675×10⁻⁸, three Richardson pairs + audit4 concurring)
  at 5.4× the gate's floor at the finest spacing — a genuine
  margin, the lineage's thinnest → SURVIVES with rider
  G53-R1. The gate's denser radial sampling finds the
  continuum SEC dip (−1.257×10⁻⁶ @ r ≈ 5.42) → the
  registered-set scope is made binding as rider G53-R2,
  with the lineage context (RW-5/y_his positive, E2-1/B-2
  dipping) recorded so the scope is not misread as A-6's
  private defect.
- (b) Ceiling, bracket and deciding margins reproduce on
  gate machinery side-by-side with RW-5 (0.22% margin
  difference, no rung bought or lost); the embedding
  itself recomputes exactly → SURVIVES, with "lossless"
  scoped to the registered bars (the sense claimed).
- (c) The amendment's factual basis was re-derived by the
  gate (embedding exact; the failure real; the clip one
  coordinate; both losslessness gates passed, the home
  gate by this gate's §3 reads) and its disclosure is
  complete and stricter than the lineage precedent →
  SURVIVES AS FENCED (G53-R3 amended-form wording).
- (d) Every clause confirmed against the stored records;
  two precisions required (bests-vs-mean for "time spent";
  absolute-vs-floor-multiple for "~17×") → SURVIVES
  RESTATED, restatements carried into G53-E.
- Controls survive; the 0.1364 shorthand is corrected on
  the face (C-1), per the Gate-51 discipline.

**DESK: NO DATA CONTACT** (prescribed configurations from
the programme's own record; no real-world dataset
consulted).
