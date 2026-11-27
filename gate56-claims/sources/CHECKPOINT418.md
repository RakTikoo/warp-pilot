# PHASE 418 CHECKPOINT — THE CARRYING-AWARE
# HUNT

Status: COMPLETE. Verdict: **A BETTER CARRYING
BASE EXISTS** (the criterion bar beaten;
GATE REFERRAL). Not cost-bounded: 1,884
screens against the registered 2,200 total
cap. Memo: results/p418_memo.md.
Registration: work/p418_registration.md
(filed before any computation).

## The result in one paragraph

The joint hunt over (base scalings × base
corrections × shift shape), objective the
carried joint at the SS7 criterion peak
directly under PEN418, found base B418 —
(μ_N, μ_M) = (2.0473858121439443,
5.606036969201072), K_B = 17, full vectors in
results/p418_confirmation.json — carrying the
criterion shift at CONFIRMED joint
+3.6518621144739354×10⁻⁶ (score-incumbent,
screen 1320) / +3.6526207343841256×10⁻⁶
(pure-joint maximum, screen 1347), 2.98× the
bar J1_400 = +1.2273852081052888×10⁻⁶, both
confirmations at diff 0.0, worst-nulls
+3.512×10⁻⁶ and adversary polishes
+3.62×10⁻⁶ / +3.62×10⁻⁶ positive (frame-
invariant legality), SEC −5.49×10⁻⁴ /
−5.29×10⁻⁴ on the face. B418's criterion
spend against its own static joint
(+3.654×10⁻⁶) is 2.14×10⁻⁹ / 1.25×10⁻⁹ — the
hunt's spend floor. The SECOND READ does not
beat its bar: at 2× the criterion on B418 the
confirmed joint is −3.05568504581619×10⁻⁵
(worst-null −3.206×10⁻⁵, NEC-bound at
r ≈ 12.07) — B418 is a criterion specialist
and 412's P* on 400's base remains the 2×
carrier of record.

## What was run

- Controls (work/p418_controls.py →
  results/p418_controls.json): all SS3
  controls passed — 405's winner, 412's P*,
  B1's T1 non-carrier read, both statics, the
  penalty identity — at diff 0.0 / diff-0.0
  class; REP-418-K9 recorded (400's base at
  K_B = 9: static +1.182534×10⁻⁶, carried
  +9.722871×10⁻⁷ — a shadow, never a bar).
- Admission (work/p418_admission.py on the
  pool mirror → results/
  p418_controls_laptop.json): ADMITTED,
  diffs ≤ 5.5×10⁻¹⁹, argmin radii identical;
  deciding reads all VM regardless (SS2).
- Search (work/p418_search.py →
  results/p418_screens.jsonl,
  results/p418_state.json,
  results/p418_confirmation.json): Stage S
  seeds 6 (incl. the supplementary S-F, the
  H2 seed on B1); Stage T transect 228
  (6 bases × static + 37-screen shape CD);
  Stage A (K_B = 9 joint hunt) 800 — cap
  bound; Stage B (K_B = 17, from Stage A's
  winner resampled) 350 — cap bound, the
  winner found here by base CD; CONF1 →
  Stage G not triggered (confirmed joint
  > J1_400, the registered condition);
  Stage R (2× on B418) 300 — cap bound.
- Supplement (work/p418_r17.py →
  results/p418_r17.log): the K_S = 17 gate
  at 2× (stage R17, 200 screens — cap-squeezed
  inside Stage R, run disclosed as a
  supplement; phase total stays under the
  2,200 cap) and the SS6 confirmation of the
  pure-joint maximum (screen 1347, diff 0.0).

## Bookkeeping disclosures (also in the memo)

- 414 attribution correction: 414's
  −5.503912×10⁻⁵ B1 seed read is its H2-seed
  screen (p414_screens2.jsonl id 1), not the
  G50-shape seed (id 0, −1.999057×10⁻⁴). Both
  reproduced at diff 0.0 (S-F, S-C). 414's
  verdict substance unaffected. Flagged for
  the parent; no ledger edit made here.
- Pattern execution: caps bound in A/B/R/R17
  while CD blocks still improved; the joint
  NM read no screens in A or B, B's shape
  block and R/R17's shape NM likewise (one
  120-eval shape NM ran in A). The squeezed
  polishes are a named residual — a
  resumption can run them against the stored
  incumbents (results/p418_state.json) with
  work/p418_search.py's blocks; the verdict
  does not rest on them.
- Rejects 0; penalised evals 0; all 1,884
  screens C1-feasible. Wall time ≈ 2.34 h
  (main driver) + ≈ 0.55 h (supplement).

## Files

- work/p418_registration.md — the charge as
  registered (SS0–SS8).
- work/p418_lib.py — machinery (414's reads
  verbatim; PEN418; seed bases/shapes; bars).
- work/p418_controls.py, work/p418_admission.py,
  work/p418_search.py, work/p418_r17.py.
- results/p418_controls.json,
  results/p418_controls_laptop.json,
  results/p418_screens.jsonl (1,884 screens,
  full configurations),
  results/p418_state.json (incumbents,
  transect table, tallies),
  results/p418_confirmation.json
  (criterion_best, criterion_best_joint,
  twice_best — full SS6 records),
  results/p418_memo.md — the deliverable memo.
- results/p418_search.log, results/p418_r17.log
  — run logs.

## Fences observed

Band [10, 20] on every figure; SEC on the
face of every winner; no member, no EC pass —
the carried point is a GATE REFERRAL; the
peak quoted AT the criterion with the scaling
construction disclosed; deciding values
frame-invariant (C-10 naming: sampled minima
are SAMPLER-M). No ledger append, no
successor launch, no user contact.
