# P80-3 — RUN RECORD

**Item:** P80-3, source-modulated composition (payload transport).
**Verdict:** BEATS 0.0799 AT FULL LEGALITY — deciding row
(o0.06_i0.06), held payload 0.08745c. Checker 17/17 PASS.
**Python:** ~/workspace/warp-pilot/venv/bin/python, float64
everywhere. INTERNAL only. CHECKPOINT80.md not edited.

## Machinery route (recorded as required)

**REUSE of Phase 73's P73-1 build**, generalised — not a fresh
build from the p501 specification alone. `phase80/p803_lib.py`
takes the chain algebra from `phase73/p731_lib.py` (which is the
registered adaptation of `phase50/p501_recon.py` lines 100–140)
and parameterises it by shell profile: per-shell span
[R1−0.3W, R2+0.3W] (P73-1's extended-domain rule, adopted because
P73-1's primary domain failed its endpoint read), knots
[lo×3, linspace(lo,hi,10), hi×3], dr = 2.5e-4 chain grid, switch
w = 0.05, λ-balance, F-reset, S = 1 − k∫F/r². Composition,
re-equilibration and audit patterns are Phase 41/46/52's
(p413 `build_composed`; p523 gate-standard summarise pattern;
wa_auditor primary). p501_recon.py itself was read in full and
governs the source form's fidelity (14-number vector: 12 aᵢ, q,
r_m).

## Protocol as run

1. **Anchors:** Minkowski max|G| = 0 exactly (gate-standard
   auditor). Finalist-A β=0 control on the seed-11 audit set:
   worst −2.11e-08, Type-I 1.000 (stored p731 read on its own set:
   +2.141e-07 — the difference is point-set, magnitude is
   floor-level either way; recorded, not hidden).
2. **Alone shells** (`p803_alone.py`, `p803_inner.py`): zero-start
   (aᵢ=0, q=1.47837873, r_m=span midpoint) + L-BFGS-B polish on
   the clone-algebra core objective (points r∈[R1−0.75, R2],
   h=0.3, two-number instrument; SCREENING ONLY), continuation in
   β_alone ∈ {0.05, 0.06, 0.07, 0.08}; full gate-standard audits
   at h ∈ {0.3, 0.15, 0.075} on the full audit set with regions.
3. **Economics** (`p803_compose.py`, first action): held-W
   anatomy + payload sums for all 6 assemblable pairs frozen to
   `p803_economics.json` BEFORE any composed legality read.
   Calibration inside the same step: (0.05,0.05) payload 0.07292
   = P52-3's F-dual row; cosine control of the P46-2 0.0799 row
   read gate-standard (cavity −1.109e-04 artefact read
   reproduced).
4. **Composed audits:** gate-standard h=0.3/0.15, regions
   (payload/inner wall/cavity/outer wall/exterior), conservation
   (gate-standard divergence read, 28 wall points).
5. **Verification** (`p803_verify.py`) on both beating rows:
   4th-order auditor + Phase-1 judge at h=0.15, DEC ladder
   (focused + stencil-clear × h∈{0.15,0.075,0.0375}).
6. **Checker** (`p803_check.py`) over the frozen JSONs + library
   recompute of held-W anatomy and chain balance: 17/17 PASS.

## Economics-before-legality table (from p803_economics.json)

| row | β_o^comp | β_i^comp | W_o held | W_i held | W sum | payload relat |
|---|---|---|---|---|---|---|
| o0.05_i0.05 | 0.04076 | 0.03225 | 0.06638 | 0.06638 | 0.13276 | 0.07292 |
| o0.05_i0.06 | 0.04076 | 0.03870 | 0.06638 | 0.07966 | 0.14604 | 0.07934 |
| o0.06_i0.05 | 0.04891 | 0.03225 | 0.07966 | 0.06638 | 0.14604 | 0.08104 |
| o0.06_i0.06 | 0.04891 | 0.03870 | 0.07966 | 0.07966 | 0.15931 | 0.08745 |
| o0.07_i0.05 | 0.05707 | 0.03225 | 0.09293 | 0.06638 | 0.16503 | 0.08915 |
| o0.07_i0.06 | 0.05707 | 0.03870 | 0.09293 | 0.07966 | 0.17834 | 0.09556 |

(β^comp and W values for the deciding row checker-recomputed;
full anatomy per row in the economics JSON. Lapse factors:
inner exp(Δa)=0.6451, outer 0.8152.)

## Alone-legality criterion (stated in full, as applied)

A shell is alone-legal at its β_alone iff, on the full audit set:
(i) payload + wall regions: Type-I fraction 1.000, all four EC
margins > 0, sampled-null > 0, at h=0.3 AND h=0.15; (ii) exterior
region: clean at h=0.15, OR the demonstrated artefact signature —
failures confined to the exterior with the h=0.075 ladder rung
clean (Type-I 1.000, worst > 0), or worst-magnitude strictly
shrinking across h=0.3/0.15/0.075 with the 0.075 worst within
3e-5 of zero (positive Richardson limit; the deciding composed
row's own ladder then carries the site). Outcomes: outer legal
at 0.05, 0.06; NOT legal at 0.07 (payload-region Type-I 0.46 —
fails clause (i) outright, no artefact reading available);
inner legal at 0.05, 0.06 (fringe site r≈4.6 under clause (ii)'s
shrinking-magnitude branch: −9.22e-04/−2.03e-04/−1.40e-05,
Richardson ≈ +4e-05).

## Deviations and process events (all recorded, none hidden)

1. **Optimiser, first attempt:** L-BFGS-B with scipy's default
   finite-difference step (1.5e-8) stalled at the start score
   (gradient below the FD auditor's noise; polish nfev=30, no
   movement). Fixed by the clone-algebra objective + explicit
   forward-difference Jacobian at step 2e-3. No verdict number
   ever rested on a screening score.
2. **Objective point set, first attempt:** a widened union set's
   minimum sat at r=11.53 in the smoothed exterior tail —
   design-insensitive, h=0.3 artefact (flips +5.3e-07 at
   h=0.075; wall read +1.5e-04). Replaced by the P73-1 core mask
   [R1−0.75, R2]; the episode is why the alone criterion carries
   its exterior clause in the artefact form above.
3. **Outer β_alone=0.08 abandoned** (polish killed mid-run after
   the 0.07 anatomy showed the alone ceiling at 0.06; its state
   record carries start data only, no design vector, and no
   economics row uses it). **Inner β_alone=0.07/0.08 not run:**
   the inner scan was stopped after 0.05/0.06 when the deciding
   pairs were in hand and the 0.06 polish had converged to the
   0.05 design's fringe read; pairs requiring inner 0.07/0.08
   were not assemblable in this run and are not claimed. This
   bounds the scan: the space's best legal row FOUND is
   0.08745c; rows above it in the economics table fail on the
   OUTER shell's alone legality, which was measured, not on the
   unrun inner rows.
4. **Compute / Kaggle flag assessment:** optimiser state was
   checkpointed to `p803_alone_state.json` after every polish
   (each ≤ ~18 min of wall time under heavy multi-worker VM
   contention). Total item compute ≈ 2 h wall, but no single
   uncheckpointed run exceeded ~20 min and every stage is
   resumable from disk; the ~2 h continuous-grind condition for
   the Kaggle flag was therefore not met. Two operator errors
   (pkill patterns matching the operator's own shell) killed
   the operator's shell twice; no data was lost (all state on
   disk), and the affected launches were re-issued.
5. **VM contention:** wall times throughout are inflated by
   parallel Phase-80/73/82/83 workers on the same VM; audit
   wall times ranged 2–60 s for identical work. No number
   depends on wall time.

## Deciding numbers (for the coordinator's spot-check)

- Deciding row o0.06_i0.06: payload_relat **0.0874508116004831**,
  W sum 0.15931, β_o^comp 0.04891, β_i^comp 0.03870, W rel errs
  1.7e-16. Primary h=0.15: Type-I 1.000; regions payload
  +3.853e-06, inner wall +1.188e-03, cavity −1.107e-04
  (artefact, §3 of memo), outer wall +3.202e-05, exterior
  +1.038e-06; min sampled NEC (all sig) +8.55e-07; conservation
  rel_med 0.0115.
- Ladder (deciding row): focused DEC −1.807e-04 → +5.04e-07 →
  +1.213e-05; stencil-clear −1.496e-04 → +9.334e-05 → +1.609e-04;
  Type-I 1.000 all rungs.
- Second paths h=0.15: 4th-order worst −5.93e-07 (cavity site
  only), Phase-1 worst −1.18e-06 (same site); both Type-I 1.000.
- Second row o0.06_i0.05: payload 0.08104, same pattern
  (4th −5.94e-07; Phase-1 −1.18e-06; ladder +9.34e-05/+1.61e-04).
- Outer alone ceiling: 0.07 audit h=0.15 Type-I 0.646, sampled
  NEC −5.04e-04 (payload region Type-I 0.46, wall +1.49e-04).

## Files

Scripts: `phase80/p803_lib.py`, `p803_alone.py`, `p803_inner.py`,
`p803_compose.py`, `p803_verify.py`, `p803_check.py`.
Results: `p803_results.json` (frozen bundle), `p803_economics.json`,
`p803_alone.json`, `p803_alone_state.json`, `p803_composed.json`,
`p803_verify_o0.06_i0.06.json`, `p803_verify_o0.06_i0.05.json`,
`p803_check.json`, `p803_memo.md`, this record, run logs
(`p803_alone.log`, `p803_inner.log`, `p803_compose.log`).
