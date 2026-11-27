# Phase 408 — Worker A2 memo (Amendment A-408-1 clipped seed + arm specs)

Scope: Worker A2 tasks under Amendment A-408-1 only. No pool work, no
audits, no ledger append. `CHECKPOINT408.md` and `p408_controls.json`
were not edited. Code: `work/p408_workerA2.py` (programme venv, float64).
All results below were re-verified in a second, independent read-back
pass over the written files.

## Task 1 — The clipped seed (Amendment A-408-1) — PASS

Record: `results/p408_amendment_A408_1.json`.

- (a) Unclipped RW-5 embedding taken from `p408_controls.json`
  (`C-408-5.RW-5_to_16mode.embedded_y30`); its sha256 (float64 tobytes)
  recomputed from the stored values =
  **`a0201be16477e244d82b14e421f8de5d6fff1a2917b6cfe40441a4a03dd2d374`** —
  matches the registered hash exactly.
- Clipped vector = unclipped with c idx 13 set to exactly −2.25.
  (b) It differs from the unclipped vector in **exactly one coordinate**
  (index 13; verified by elementwise comparison).
  Clip record: index 13 (c13), unclipped −2.3199648239179234,
  clipped −2.25, excess **0.06996482391792336**.
- Clipped vector sha256 (float64 tobytes) =
  **`d228c82e18396fe5d6a7ccc85881c558355d8d096bc8923e856ea7fc3615d69f`**.
- (c) Containment: full 30-row table in the amendment record
  (c idx 0 and idx 11 against [−3.375, 3.375]; other c against
  [−2.25, 2.25]; a idx 16–26 against [−8, 8]; a idx 27 (a12) against
  [−12, 12]; q against [0.25, 3.0]; r_m against [11, 23]).
  **Verdict: all 30 coordinates inside the Arm B box** (the clipped
  c13 sits exactly on its −2.25 bound, inside). The Arm B box used was
  cross-checked two ways: it equals the box stored in
  `p408_controls.json` (`armB_box_lo`/`armB_box_hi`) and an independent
  reconstruction from the CHECKPOINT408-as-amended text.
- Downstream name of record: "RW-5 embedded, box-clipped at c13".

## Task 2 — Arm A DE spec (`work/p408_spec_a_de.json`) — PASS

Format/keys mirror `p392_spec_r16_de.json` exactly (same keys, same
order: tag, lib, lo, hi, cap_min, pop, y_ref, seed_ys, seed_names).

- tag `a408`, lib `p392_16`, cap_min 120, pop 64.
- lo/hi copied from `p392_spec_r16_de.json` (the R-16 box); verified
  **identical to the staged state's stored `box_lo`/`box_hi`** in
  `phase392/results/p392_pool_r16_de_state.json`.
- `y_ref` = the 392 R-16 spec's `y_ref` verbatim (E2-1 embedding;
  r_m = 16.187589217631558, verified).
- `seed_ys` = **all 64 members** of the staged state's `pop`, in stored
  order — verified elementwise identical to the stored `pop`
  (64 seeds × 30 dims); **every seed inside lo/hi** coordinate-by-coordinate.
- `seed_names` = `["staged_population_64_in_stored_order"]` (per tasking).

## Task 3 — Arm B DE spec (`work/p408_spec_b_de.json`) — PASS

Same format/keys as the 392 DE spec.

- tag `b408`, lib `p392_16`, cap_min 120, pop 64.
- lo/hi = the Arm B box (c idx 0 and idx 11 at ±3.375, other c ±2.25,
  a/q/r_m as R-16) — same box as Task 1's containment check.
- `y_ref` = the **clipped** embedding (Task 1); its sha256 recomputed
  from the spec file = `d228c82e…d69f` (above); **r_m =
  16.17148847124908**, verified.
- `seed_ys` = [`y_his_equivalent`, clipped embedding]:
  - `y_his_equivalent` built from RW-5's full 26-vector in
    `phase392/results/p392_verdicts.json` (`subjects/RW-5/y`, sha256
    re-verified `44719b50…c2`): c 0..15 = 0, a (30-vec idx 16..27) =
    RW-5's a-block (26-vec idx 12..23), q (idx 28) = RW-5 idx 24,
    r_m (idx 29) = RW-5 idx 25. Cross-check: identical to Worker A's
    stored `y_his_equivalent_armB` in `p408_controls.json`, sha256
    `c8cb0ed4b7d25281ba289b73a1f3fe251c2f60c983d609906af2e21da886c44a`.
  - seed names: `["y_his_equivalent", "RW-5_embedded_ls_16mode_boxclipped_c13"]`.
- **Both seeds verified inside the Arm B box** coordinate-by-coordinate.

## Task 4 — Powell + harvest spec templates — written

- `work/p408_spec_a_powell_starts.json`, `work/p408_spec_b_powell_starts.json`:
  mirror `p392_spec_r16_powell_starts.json`'s fields
  (picked_idx / picked_fit / picked_brackets / picked_hashes), with the
  arm's tag/lib/lo/hi and maxfev 1500 filled in, and
  `de_state_path` = `~/work/p408/state/a408_de_state.json` /
  `~/work/p408/state/b408_de_state.json`. The picked-* fields are
  clearly-marked string placeholders for Worker B to complete at runtime.
- `work/p408_spec_a_harvest.json`, `work/p408_spec_b_harvest.json`:
  mirror `p392_spec_r16_harvest.json` (tag/lib/candidates/y_ref/top_k/
  distinct_min), `candidates` empty by design, y_ref = the arm's DE-spec
  y_ref (verified), top_k 6, distinct_min 0.05, plus `de_state_path`.
  Each file carries a `_template_note` stating exactly what Worker B
  fills in and by what pattern.

### Deviations from the 392 spec pattern (with reasons)

1. **Powell templates reference the DE state file instead of embedding
   member vectors.** In 392, `p392_spec_r16_powell_starts.json` was
   written *after* the DE finished (by `p392_make_followups.py`) and
   embeds the actual picked indices/fits/brackets/hashes, and the
   individual `p392_spec_r16_powell_de0/1/2.json` files embed the actual
   `start_y` vectors. Here the DEs have not run, so per tasking the
   DE-state-dependent fields are placeholders keyed to the state-file
   path; Worker B completes the starts file and writes the per-start
   Powell specs at runtime in the 392 shape. This difference is also
   noted inside each template file itself.
2. **Seed-name wording differs from Worker A's (unexecuted) spec-stage
   draft** in `work/p408_workerA.py`: Arm A's seed name is
   `staged_population_64_in_stored_order` and Arm B's second seed is
   `RW-5_embedded_ls_16mode_boxclipped_c13`, per the A2 tasking (the
   draft's `staged_population_64` / `RW-5_embedded_ls_16mode` predated
   the amendment and the stored-order clarification).
3. Arm B's `y_ref`/seed is the **clipped** embedding, not the unclipped
   LS embedding the original C-408-5 registration specified — that is
   Amendment A-408-1 itself, not a Worker A2 choice.

## Files written

- `results/p408_amendment_A408_1.json` (both vectors, both hashes, clip
  record, 30-row containment table)
- `work/p408_spec_a_de.json`, `work/p408_spec_b_de.json`
- `work/p408_spec_a_powell_starts.json`, `work/p408_spec_b_powell_starts.json`
- `work/p408_spec_a_harvest.json`, `work/p408_spec_b_harvest.json`
- `work/p408_workerA2.py` (generating/verifying script)
- this memo

DESK: NO DATA CONTACT (programme's own records only).
