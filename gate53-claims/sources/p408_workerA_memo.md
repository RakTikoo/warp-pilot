# Phase 408 — Worker A memo (home/VM controls + specs)

**VERDICT (Worker A scope): MACHINERY FAILURE — C-408-5 (home part).**
C-408-1, C-408-2 and C-408-3 all PASS with exact reproduction of the
standing records. C-408-5's embedding was computed exactly as registered,
and the embedded RW-5 vector lies **outside the Arm B box** at one
coordinate, failing C-408-5's registered containment bar. Per the failure
protocol the run stopped there: **no arm spec files were written** (the
spec stage comes after the controls in the registered order, and Arm B's
spec would carry the out-of-box vector as its `y_ref`/seed). No fix was
improvised. Full records: `results/p408_controls.json`; code:
`work/p408_workerA.py`; log: `results/p408_workerA.log`.

Frame: programme venv (`~/workspace/warp-pilot/venv/bin/python`, float64
everywhere); verdict audits via `p2513_lib.audit_chunked` (Gate-6
`wa_auditor`) + `phase50/p503_lib` `audit4` second path on
`p2513_lib.pts_1020_control` (1,430 pts) at h = 0.0375 AND h = 0.01875,
legality via `p2513_lib.legality_1020` — the 392 pattern
(`p386_rejudge_stage1.audit_beta`).

Task 1 (library copy): `work/p408_lib16.py` written — verbatim copy of
`phase392/work/p392_lib16.py` except a header note stating it is the
Phase 408 copy (numerics identical; verified: the file differs only in
the header lines, and C-408-1's chain reads match 392's C-392-4a 16-mode
record at rel diff 0.0).

## C-408-1 — PASS (c = 0 reproduces Gate-42, through p408_lib16)

- Subject: y_his as (0₁₆, y_his a/q/r_m) through
  `p408_lib16.GradedProcaccia16`, β = 0.1363. Source y_his22 sha256
  `d4eb224779778f58308abbb28c4832562dcad02d40e90b2b8055ce29990eddd7`
  verified.
- **LEGAL** under the common bars at both spacings.
- h = 0.0375 worst margin **+3.404177799426875×10⁻⁷, SEC @ r = 5.0** —
  ratio **0.99999994** to Gate-42's +3.404178×10⁻⁷ (bar: within factor 3).
  Type-I fraction 1.000; floor multiple 109.51×; shell sampled-NEC min
  +8.662×10⁻⁸; audit4 worst +3.395770×10⁻⁷; q_max 0.99473 @ 16.6.
  h = 0.01875 worst +3.397877×10⁻⁷ (SEC @ 5.0).
- Chain reads vs Gate-42 digits (392's C-392-1 record): rel diffs
  M 1.02×10⁻¹⁵, rho_max 1.74×10⁻¹⁵, lambda 1.79×10⁻¹⁵, k 2.29×10⁻¹⁶
  (bar ≲ 1×10⁻¹⁰); vs 392's C-392-4a 16-mode record: rel diff 0.0 on all
  four.

## C-408-2 — PASS (E2-1 reproduces, 12-mode machinery)

- sha256 verified before audit:
  `6167938325934832baac896f7e177be6e0bed594fe43865c9bafcfe8a2573066`
  (matches `p391_verdicts.json`).
- β = 0.191796875: **LEGAL**; deciding digits reproduce the 391/392 home
  record at **rel diff 0.0**: worst SEC **+7.075485239309395×10⁻⁸ @
  r = 6.0** (13.36× FD floor), audit4 **+5.407152092244097×10⁻⁸**,
  q_max **0.9932762939270345 @ 19.75**; Type-I 1.000; shell sampled-NEC
  min +2.611×10⁻⁷. h = 0.01875 worst +5.824590×10⁻⁸ (SEC @ 6.0).

## C-408-3 — PASS (RW-5 reproduces, both rungs, 12-mode machinery)

- sha256 verified before audit:
  `44719b508ba733bb257281f994f90340b1ac25b33684bbe8ac9c4da5f10535c2`
  (matches `p392_verdicts.json` subjects/RW-5 and the registered hash).
- β = 0.192578125: **LEGAL**; rel diff 0.0 vs 392's home record on every
  deciding digit: worst SEC **+6.055585252705956×10⁻⁷ @ r = 3.75**
  (106.53× FD floor), audit4 **+6.050011956571471×10⁻⁷**, q_max
  **0.9933621063959674 @ 19.75**; Type-I 1.000; shell sampled-NEC min
  +2.007×10⁻⁷.
- β = 0.195078125: **FAILS as required** — worst SEC
  **−1.0315856835997687×10⁻⁵ @ r = 9.75** (rel diff 0.0 vs 392),
  audit4 −1.032461×10⁻⁵, Type-I 0.98499, q_max 1.00575 @ 19.75.

## C-408-5 (home part) — FAIL (box containment) → MACHINERY FAILURE

Method (registered 391 e2gate pattern): log φ of RW-5 (12-mode) on
linspace(R₁,R₂,20001), `np.linalg.lstsq` of the 16-mode BSpline basis,
residual = Bᵀc − log φ on the same grid; a/q/r_m carried unchanged
(q = 1.6681638067393412, r_m = 16.17148847124908 — both match
CHECKPOINT408's registered values).

- **Residual: RMS 9.207430281480095×10⁻³, max abs 3.673295654339093×10⁻²**
  (larger than 392's E2-1→16-mode embedding: RMS 6.326×10⁻³, max
  2.571×10⁻²).
- Embedded 30-vector sha256:
  **`a0201be16477e244d82b14e421f8de5d6fff1a2917b6cfe40441a4a03dd2d374`**
- Embedded c₁₆: [2.4881984560738917, 1.161664107623004,
  −0.2714675118499194, −1.3949354945482046, −2.0726437815067107,
  −2.1239315825403633, −1.708244228076615, −1.0967622998971354,
  −0.6313586240986713, −0.9389439670379169, −1.568930091686234,
  −2.1134365124109813, −2.1599591180228574, **−2.3199648239179234**,
  −1.2119557567871244, 1.0604781946957984]; a/q/r_m = RW-5's, unchanged.
  (Full vector + per-coordinate box table in `p408_controls.json`.)

### Anatomy of the failure

- **Binding clause:** CHECKPOINT408 C-408-5 — "the embedded vector must
  lie inside the Arm B box (every coordinate reported against its
  bounds)".
- **Site:** exactly **1 of 30** coordinates outside: **y index 13 =
  c idx 13** (0-based; 14th grading coefficient) =
  **−2.3199648239179234** vs its bound [−2.25, 2.25] — outside by
  **0.06996482391792336**. All other 29 coordinates are inside,
  including both widened coordinates: c idx 0 = +2.4881984560738917
  (inside ±3.375) and c idx 11 = −2.1134365124109813 (inside even the
  unwidened ±2.25).
- **Mode geometry:** c idx 13's B-spline has Greville abscissa
  19.23056616510756 and support [17.692141169803087, 19.999778662759798]
  — an outer mode spanning the switch-to-R₂ region. It is not one of
  the coordinates the registration widened.
- **Not a numerical accident:** the embedding was recomputed in an
  independent recheck (fresh `lstsq` call) — c₁₆ identical, max diff
  0.0. In the same run, the artefact embedding (below) reproduces 392's
  stored embedded vector exactly (max diff 0.0), so the embedding
  machinery is the registered one; the out-of-box value is a property
  of RW-5's log φ shape at the finer basis, not of the instrument.
- **Consequence:** Arm B cannot start as registered — its `y_ref`/seed
  (this embedding) lies outside its own box. The screening-losslessness
  gate (pool part of C-408-5) and C-408-4/C-408-6 were not reached by
  Worker A (pool scope / Worker B in any case).

### Artefact embedding for Worker B's C-408-4 (computed, stored in controls)

Recomputed fresh by the same LS pattern (not merely copied), and it
**matches the stored 392 vector exactly**: residual RMS
2.345856×10⁻³, max abs 6.449422×10⁻³; embedded 30-vector sha256
`8501b2006993d29d8a9887878491749faf9d205cec620d083c12c5144cabf954`
(= `p392_pool_vectors.json` `artefact_emb16` and 392's C-392-4b record;
max abs diff vs stored 0.0). Recorded under
`C-408-5.artefact_to_16mode_for_C-408-4` in `p408_controls.json`.

### Follow-ups (logged, NOT executed — a decision above Worker A)

1. Clip c idx 13 to −2.25 and re-price (new residual/hash, screening
   gate re-read) — changes the registered seed; needs a dated post-hoc
   amendment on the face of CHECKPOINT408.
2. Widen c idx 13 in the Arm B box — a new widening, which changes the
   priced question (FU-P392-3 prices basis resolution at the widened
   box, not another widening); needs re-registration.
3. Waive containment for `y_ref` only — 392 precedent exists (the E2-1
   embedding `y_ref` in `p392_spec_r16_de.json` has c idx 0 =
   2.2569788046198447, outside its ±2.25 box by 0.00698, and was used as
   `y_ref`/seed), but 408's C-408-5 wording is explicit and the excess
   here (0.06996) is 10× that precedent's — only via a dated amendment.

## Spec files (Task 6) — NOT WRITTEN

The run stopped at the C-408-5 failure before the spec stage, per the
tasking ("If any control FAILS its bar, stop, record the failure with
anatomy in the memo, and report it as MACHINERY FAILURE"). Neither
`p408_spec_a_de.json` / `p408_spec_b_de.json` nor the Powell/harvest
templates exist. The inputs for them are all verified and on record
(Arm A: staged pop-64 + original R-16 `y_ref`/box, cross-checked in the
worker script against the staged state's `box_lo`/`box_hi`; Arm B:
box, `y_his_equivalent` seed and the embedding above), so the specs can
be written immediately once the coordinator rules on the C-408-5
amendment — the worker script's spec stage is intact and will run
unchanged after the embedding gate.

DESK: NO DATA CONTACT (Worker A scope: programme's own records only).
