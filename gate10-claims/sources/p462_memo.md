# P46-2 — LAPSE-RE-EQUILIBRATED NESTED SHELLS: MEMO

Pre-registration: `../CHECKPOINT46.md` §P46-2 (bars, verdict forms,
target and the P22-3 trigger fixed there before any number).
Source record: Phase 41 P41-3 (`../../phase41/CHECKPOINT41.md`,
`../../phase41/results/p413_memo.md`, `p413_results.json`,
`p413_follow.json`). Scripts: `../p462_audit.py`,
`../p462_follow.py`, `../p462_cavity.py`, `../p462_check.py`
(checker over result files — ALL CHECKS PASS). Numbers:
`p462_results.json`, `p462_follow.json`, `p462_cavity.json`,
`p462_check.json`. Judge: Phase-1 `verify_metric.einstein_at_points`,
float64, full-volume all-directions NEC/WEC/SEC/DEC + Hawking–Ellis
Type at h ∈ {0.3, 0.15} (h = 0.075 focused follow-ups at deciding
sites), conservation (divergence) read, flat-space FD-floor control
(max|T| = 0.0 at both h).

## Construction (P41-3 pattern, ONE changed ingredient)

The composed metric is P41-3's, unchanged: m_comp = m_i + m_o
(disjoint supports); b_comp from m_comp; P_comp = P_i (standalone —
its enclosed mass and edge pressure are unchanged by nesting) +
P_o* (outer TOV re-integrated against m_comp — the joint re-solve
is retained); a_comp integrated inward from the composed pressure;
staircase shift V(r) = β_o·S_o(r) + β_i·S_i(r).

The single changed ingredient is the **re-equilibration of the
inner shell for the composed lapse**, P41-3's registered reopening
verbatim: the inner shell is solved inside the composed lapse from
the start. Because a_comp is shift-independent, the construction
order is: (1) joint re-solve → a_comp; (2) choose the inner
coordinate β_i so the inner shell's characteristic orthonormal
shift — the P41-3 follow-up E4 quantity,

  W_i = β_i · e^(−a(r_mid,i)),  r_mid,i = inner mid-wall —

equals its verified ALONE value; (3) β_o carries the remainder of
the payload (β_o = payload_coord − β_i). Hence
β_i^new = β_i^alone · exp(a_comp(r_mid,i) − a_i^alone(r_mid,i)).
No exotic matter is introduced anywhere: both shells are the
verified Fuchs-class profiles of P41-3, read off one composed
metric (smuggling rule: nothing to catch — the matter is the
record's own).

## Gate — Finalist-A calibration class at payload 0.04: PASS

Re-equilibrated Finalist-A row (β_o = 0.0231, β_i = 0.02 → 0.01695;
composed lapse at inner mid-wall a = −0.2975 vs −0.1320 alone,
e^a ratio 0.847; W held at 0.02282 exactly): composed worst margin
**+5.479e-07 (h = 0.3) / +5.496e-07 (h = 0.15)**, Type I 1.000,
conservation rel. median 7.7e-04 — reproducing P41-3's
preserves-legality control (+5.48e-07 / +5.50e-07, Type I 1.000,
cons. 7.8e-04) to its digits. The gate passes before any frontier
number is trusted, as registered.

## Frontier rows — margins by region

Frontier class: outer (5,10), M = 1.9125 geom, compactness 0.383;
inner (2,4), M = 0.765 (×0.4 scale copy). Re-equilibration (same
for all frontier rows — a_comp is payload-independent):
a_comp(inner mid-wall) = **−0.7218** vs a_alone = −0.2834
(e^a ratio **0.6451** — P41-3's −0.722 / −0.283 / 0.645 exactly);
β_i: 0.05 → **0.03225**; characteristic orthonormal shift held at
**W_i = 0.06638 = the verified alone value** (checker-verified to
<1e-9); the inner shell's own local orthonormal shift at mid-wall,
β_i·S_i·e^(−a), is 0.03319 composed vs 0.03319 alone — held, not
relabelled. Conservation rel. median 4.5–4.6e-03 (P41-3 frontier:
4.7e-03).

Worst margin per region (h = 0.15; h = 0.3 in brackets where it
differs in character):

| Region | payload 0.0599 (β_o=0.0277) | payload 0.0799 (β_o=0.0477) | payload 0.0998 (β_o=0.0677) |
|---|---|---|---|
| payload | +1.10e-04 [+0.3: −2.12e-04 artefact, flips +] | +1.09e-04 [same artefact] | +1.08e-04 |
| **inner wall** | **+9.74e-04** | **+9.79e-04** | **+9.86e-04** |
| cavity | −4.7e-07 (artefact, see below) | −1.5e-06 (artefact) | −4.7e-06 (artefact) |
| **outer wall** | +4.36e-05 | +4.05e-05 | **−2.73e-04 (SEC, r≈7.28)** |
| exterior | +2.09e-06 | +2.09e-06 | +2.09e-06 |

Type I fraction 1.000 at h = 0.15 for the 0.06/0.08 rows (0.993
for 0.0998, the loss sitting in the outer wall).

**The inner wall passes at every payload.** Against P41-3's frozen
composition at payload 0.0998 (inner-wall SEC −1.43e-02,
h-converged), the re-equilibrated inner wall reads **+9.86e-04** —
the lapse-deepening kill of the inner shell is removed, by the
registered mechanism: the coordinate β_i was lowered by exactly
the lapse factor (×0.645) so the orthonormal shift never rose.

**The cavity DEC dip is a stencil artefact, demonstrated, not
asserted** (`p462_cavity.py`): the dip sits only at r ≈ 4.8–4.87,
whose FD stencil crosses the outer wall's inner edge (R1o = 5);
cavity points whose stencil stays clear of the wall (r ≤ 4.6)
read **+1.13e-04 (h = 0.15) / +1.15e-04 (h = 0.075)**, Type I 1.0,
at both frontier payloads tested; the near-edge value itself is
floor-level (−1.4e-06…−5.8e-06), sign-unstable across point sets
at h = 0.15 (+5.1e-06 on the focused set, −4.7e-07 on the main
bed). This is the identical site/kind P41-3's integrated verdict
already classed as FD-rate, not deciding. The h = 0.3 payload SEC
dip (−2.1e-04, r ≈ 1.43) is likewise the P41-3 h = 0.3 stencil
artefact: it flips to +1.1e-04 at h = 0.15 and +1.0e-05…+1.2e-05
on focused h = 0.15/0.075 points.

## The 0.0998 row — failure anatomy (Failure Protocol)

The stretch row FAILS, and what binds now is named: **the outer
wall** (SEC −2.69e-04 at h = 0.3, −2.73e-04 at h = 0.15, focused
−2.42e-04 / −2.43e-04 at h = 0.15 / 0.075, worst at r ≈ 7.28 —
h-converged, real). Mechanism: the payload remainder pushed
β_o to 0.0677, past the outer shell's verified 0.05, and the
outer shell's own characteristic orthonormal shift at its
mid-wall rose to **0.1103** vs its alone value 0.06638 — the
*same* lapse-amplification anatomy, one shell out: the composed
lapse at the outer mid-wall is −0.4877 vs −0.2834 alone (the
inner mass deepens it), so an over-driven outer coordinate shift
is amplified exactly as the inner one was in P41-3. The failure
migrated outward and shrank ~50× (−1.43e-02 → −2.7e-04).

Follow-up experiments (run, `p462_follow.json`):
- **Dual re-equilibration** (anatomy experiment, not a registered
  row): β_o ALSO held at its alone characteristic value
  (β_o = 0.0408) with β_i re-equilibrated → payload 0.0729, outer
  wall +4.25e-05, inner +9.77e-04 at h = 0.15 — both walls clean.
  The 0.0998 failure is outer overdrive, not a new term.
- **β_o capped at the verified 0.05**, β_i re-equilibrated:
  payload **0.0821** — inner +9.79e-04, outer +3.96e-05, payload
  +1.09e-04 at h = 0.15 (cavity artefact only). A follow-up datum
  above the ladder's 0.08 row, reported as such; the verdict
  below rests on the registered ladder row.

## P22-3 extension rows — NOT TRIGGERED

The registered trigger is a full-bar pass at payload ≥ 0.0998.
The 0.0998 row fails at the outer wall, so **no superluminal
extension rows were run** and there are no extension-row verdicts
to report. Had one fired, its language would have been "scan
signal under attack", never FTL.

## C12 accounting (mandatory)

Both shells' setup is ≤ c pre-arrangement: the composed object is
a stationary, pre-arranged configuration; nothing in its
construction propagates faster than c. All payloads here are
subluminal (≤ 0.0998c); payload transit is ordinary subluminal
transport, and the construction-inclusive earliest arrival over
any baseline D is ≥ D/c. No superluminal row exists in this item,
so no EFFECTIVE ONLY line is needed beyond this statement; no
transport claim beyond subluminal motion is made or implied.

## Verdict (registered fixed form)

**COMPOSITION BEATS FRONTIER** — the re-equilibrated frontier-class
row at payload **β = 0.0799 relativistic (0.08 coordinate;
β_o = 0.0477, β_i = 0.03225)** passes full bars at h ∈ {0.3, 0.15}
(worst wall margins: inner wall +9.79e-04, outer wall +4.05e-05,
Type I 1.000, conservation clean), and the 0.06 row passes
likewise (payload 0.0599). The single-shell frontier is 0.05:
**the payload beat the 0.05 single-shell frontier** — the first
composed configuration in the programme to do so at full bars.
The stretch payload 0.0998 does NOT pass: re-equilibration
removes the inner-wall lapse kill entirely (inner wall
+9.86e-04 where the frozen composition read −1.43e-02), and the
binding term relocates to the outer shell's own over-driven
shift (outer-wall SEC −2.7e-04, h-converged), with the dual
re-equilibration follow-up (payload 0.0729, walls clean) and the
β_o-capped follow-up (payload 0.0821, walls clean) naming the
ceiling's mechanism. Reopening/continuation condition, stated
for the record: a composition that re-equilibrates BOTH shells'
orthonormal shifts (or carries the payload remainder on a third
element) is the object the 0.0998 anatomy now points at; it is
not excluded by anything here. Rung lines: 2b YES (payload
0.0799 at full legality, frontier beaten); 2a NO (nothing
superluminal tested; P22-3 dormant); 1 YES (the lapse tax is
payable — re-equilibration works as registered, and the wall's
cost relocates predictably to whichever shell is over-driven).
