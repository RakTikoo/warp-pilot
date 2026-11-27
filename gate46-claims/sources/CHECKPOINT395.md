# PHASE 395 — WIDEN THE BOX

**VERDICT: STATIONARY LEVEL IMPROVES AGAIN. The
best stationary band level on the A2 lineage is
now −2.980985×10⁻⁵ (SET-244, band [10, 20]) at
the new centre (μ_S, μ_N, μ_M) =
(0.601180962300002, 1.5934531363763935,
4.887238651223381) on H2's total profiles —
+3.831668×10⁻⁵ over the anchor (394's centre,
−6.812653×10⁻⁵), +9.432734×10⁻⁵ over 393's ray
point, +1.458975×10⁻⁴ over 389's mixed centre,
+1.644147×10⁻⁴ over L_stat(H2). The improvement
is confirmed at pointwise grade (worst-null
−3.089621×10⁻⁵, +4.083532×10⁻⁵ over the anchor's)
and survives the end-clamp re-read inside this
charge (clamped level −3.018921×10⁻⁵, clamp cost
3.794×10⁻⁷). BOX-EDGE DISCLOSURE: the centre
presses the extended box's μ_S lower edge
(0.00118 above 0.60) and nears its μ_N upper edge
(0.00655 below 1.60); it is a local optimum of
the searched box at polish resolution, not a
certified interior optimum of the surface. The
level remains NEGATIVE — no energy-condition
pass, no member. GATE REFERRAL.**

Charged at ledger entry 1012. Registration filed
before any computation:
`phase395/work/p395_registration.md` (SS0–SS7).
Frame of record: the VM (laptop NOT admitted —
§2).

## 1. The act

389/394's search pattern (traces, grid, axes,
refinement, two polishes) over the full
per-profile scaling space of H2's totals, seeded
at 394's centre (the ANCHOR), in the registered
extended box μ_S ∈ [0.60, 1.10], μ_N ∈ [0.95,
1.60], μ_M ∈ [1.60, 5.00] — extended past every
edge the 394 centre presses (μ_S 0.80) or nears
(μ_N 1.35, and the μ_M ray still rising at 3.60),
with the anchor strictly inside. 220 stored
SET-244 reads (RAY2 7, DIAG 4, G1 24, G2 12,
G3 17, G4 29, G5 127 — new reads stored per
stage, deduplicated against the store; cap 400
not binding), EVERY read
C1-feasible and floor-feasible, 212 of them
beating the anchor, and not one DEC-saturated
read in the box (worst DEC over all reads
−6.553×10⁻⁶).

## 2. Controls (VM: ALL PASS)

Record: `phase395/results/p395_controls.json`.

- CTL-395-H2S: (1, 1, 1) reproduces L_stat(H2) at
  diff 0.0 (all five minima + polished depth).
- CTL-395-MIX: the mixed centre reproduces 393's
  anchor at diff 0.0 (all minima + depth).
- CTL-395-SEED: the seed reproduces 393's stored
  ray read at diff 0.0 on all five minima, and its
  exact worst-null at the SET NEC argmin
  reproduces at pointwise grade:
  −1.2477276305772507×10⁻⁴, diff 0.0.
- CTL-395-ANCHOR: 394's centre reproduces at diff
  0.0 on all five minima and the polished depth,
  and its exact worst-null at the SET NEC argmin
  reproduces at pointwise grade:
  −7.173153284502476×10⁻⁵, diff 0.0.
- CTL-395-CLAMP: the SS5 end-clamp construction
  at (1, 1, 1) reproduces 379's stored end-clamp
  read at diff 0.0 (NEC/DEC/ρ); at the mixed
  centre the lineage clamped joint agrees with
  Gate-43's independent AD-machinery value
  −1.7669632754376664×10⁻⁴ at 2.17×10⁻¹⁹; at the
  ANCHOR the clamped joint reproduces 394's
  stored −6.968822658140883×10⁻⁵ at diff 0.0.
- Floors hold at the seed, the centre and the
  anchor.

**Frame admission: LAPTOP NOT ADMITTED**
(fifteenth occurrence). Laptop anchor read
(mirror p390root): NEC diff 1.590×10⁻⁶, WEC
1.320×10⁻⁵, SEC 5.75×10⁻⁸; DEC 1.3×10⁻²⁰ and ρ
0.0 at roundoff — the lineage pattern. Record:
`p395_controls_laptop.json`. All deciding reads
are VM reads.

## 3. The confirmed new centre

Confirmation (`p395_confirmation.json`): the full
re-read reproduces the stored screen minima at
diff 0.0 (NEC/DEC/ρ).

| quantity | anchor (394) | new centre |
|---|---|---|
| joint (SET-244) | −6.812653×10⁻⁵ | **−2.980985×10⁻⁵** |
| NEC | −6.812653×10⁻⁵ @ 15.488 | −2.980985×10⁻⁵ @ 15.732 |
| DEC | −4.611098×10⁻⁶ @ 18.171 | −1.776685×10⁻⁶ @ 18.659 |
| ρ_min | +9.678145×10⁻⁵ | +9.780858×10⁻⁵ |
| worst-null @ NEC argmin | −7.173153×10⁻⁵ | −3.089621×10⁻⁵ |
| polished depth | −4.730182×10⁻⁶ | −1.844219×10⁻⁶ |
| end-clamped joint | −6.968823×10⁻⁵ | **−3.018921×10⁻⁵** |

NEC-bound, purely: DEC sits a factor ~17 above
NEC at the centre, and the Type-I fraction rose
to 0.612 (394's centre: 0.498). The clamp cost at
the new centre is 3.794×10⁻⁷ — an order below
394's already-small 1.562×10⁻⁶; the gain is again
carried by the scaling direction, not the
correction vectors' end knots (the Gate-43
pattern). The clamped level still beats the
anchor's UNclamped level by +3.793732×10⁻⁵ and
the mixed centre's unclamped level by
+1.455181×10⁻⁴. The rider is measured, inside
this charge.

## 4. Anatomy (`p395_anatomy.json`)

- THE RAY (charge-required trace): along the pure
  μ_M ray from the anchor at (A_S, A_N), the level
  first DIPS — −6.812653×10⁻⁵ (3.575) →
  −6.912171×10⁻⁵ (3.75) — then rises
  monotonically to the box edge: −6.730269×10⁻⁵
  (4.0) → −6.626716×10⁻⁵ (4.25) → −6.572789×10⁻⁵
  (4.5) → −6.477082×10⁻⁵ (4.75) → −6.333735×10⁻⁵
  (5.0). NO TURN INSIDE THE BOX on the ray (its
  peak is at the edge), and the ray alone accounts
  for only +4.789×10⁻⁶ of the phase's +3.832×10⁻⁵.
- THE DIAGONAL (charge-required trace): the
  registered direction (−0.025, +0.025, +0.25)
  from the anchor rises at EVERY step with
  undiminished increments: −6.304991×10⁻⁵ (k = 1),
  −5.754609×10⁻⁵ (k = 2), −5.289900×10⁻⁵ (k = 3),
  −4.818018×10⁻⁵ (k = 4); step gains +5.077,
  +5.504, +4.647, +4.719 ×10⁻⁶ (the first from the
  anchor). No turn inside the box.
- THE GAIN IS DIAGONAL, AGAIN: G1's corner
  (0.65, 1.575, 5.0) already read −3.491957×10⁻⁵;
  the G3 refinement around it produced the corner
  incumbent (0.625, 1.60, 5.0) at −3.189372×10⁻⁵,
  and the G4 polish from that incumbent returned
  exactly its start point (150 evaluations): the
  (μ_N, μ_M) corner is a local optimum of the box
  at polish resolution. The G5 polish, started
  from the diagonal's end point, walked past the
  corner to the centre of §3 — the centre is NOT
  the corner: it trades a little μ_M (4.887 vs
  5.00) and μ_N (1.593 vs 1.60) for a lot of μ_S
  (0.601 vs 0.625), and gains +2.084×10⁻⁶ for it.
- THE CENTRE PRESSES THE μ_S EDGE (the box-edge
  disclosure, on the verdict's face): the
  incumbent sits at μ_S = 0.60118, 0.00118 above
  the extended box's lower edge — the same margin
  by which 394's centre pressed its box (0.0016
  above 0.80) — in a tight flat cluster (five
  reads within 1.7×10⁻⁷). It also nears the μ_N
  upper edge (0.00655 below 1.60); μ_M = 4.887
  sits inside its edge (0.113 below 5.00).
  Whether the level keeps rising for μ_S < 0.60
  or μ_N > 1.60 is UNMEASURED (named follow-up,
  §7). Two widenings in a row have moved the
  centre to the new μ_S edge; the ascent along
  the diagonal shows no decay in its step gains,
  so the surface's peak in this direction — if it
  has one — is not yet in view.
- NO SATURATION ANYWHERE IN THE BOX: all 220
  reads feasible, worst DEC −6.553×10⁻⁶ — this
  neighbourhood is entirely outside 387's
  past-branch regime, further out than 394's box
  (worst DEC there −5.392×10⁻⁵). DEC has nearly
  left the stage: the binding constraint in this
  region is NEC alone.
- RECONCILIATION ACROSS THE ASCENT REGIONS: 389's
  concavity was a fit over the cube μ ∈ [0.90,
  1.10]³ around H2 — a local statement, and it
  stands. 393's ray crossed a dip (at ray-μ 1.05)
  into the second ascent region, which 394
  searched to its box edge and 395 has now
  searched one box further: the region's measured
  shape is a sustained diagonal ridge, rising
  toward (μ_S down, μ_N up, μ_M up), with its
  pure-axis sections flat or dipping (the μ_M ray
  dips before it rises; 394's axis slopes at the
  seed were small and sign-mixed). The three
  readings describe three neighbourhoods of one
  surface; none revises another. The lineage
  progression is now −1.942246×10⁻⁴ (379, H2) →
  −1.757074×10⁻⁴ (389, mixed) → −1.241372×10⁻⁴
  (393, ray point) → −6.812653×10⁻⁵ (394) →
  −2.980985×10⁻⁵ (395): the standing level is
  15.3% of its H2 magnitude.

## 5. Incidents

None. The search chain ran clean in one pass
(all seven stages, no driver defect, no lost
read; the confirmation's diff-0.0 reproduction
covers the best point). One stage-order note,
for the record: G5's 127 stored reads include
its full Nelder-Mead exploration of the corner
basin before the walk to the centre; the G4
polish's return of its start point is a result
(the corner's local optimality), not a no-op —
its 150 evaluations are stored and counted.

## 6. Verdict mapping (registration SS6)

- STATIONARY LEVEL IMPROVES AGAIN: FIRES. SET
  gain over the anchor +3.831668×10⁻⁵ > the
  registered 1×10⁻⁶ bar, AND the confirmed
  worst-null beats the anchor's by
  +4.083532×10⁻⁵. New centre, SET level,
  pointwise level, clamped level and box-edge
  distances all stated (§3, §4). Gate referral.
- THE SURFACE TURNS: does not fire — neither
  trace turns inside the box, and the polish
  climbed to a distinct, higher centre.
- COST-BOUNDED: does not fire (220 of 400 reads;
  all stages complete).

## 7. Named follow-ups (not run)

- A scaling search in a box extended below
  μ_S = 0.60 and above μ_N = 1.60 (and, on the
  ray's evidence, beyond μ_M = 5.00): the centre
  presses one registered edge and nears another,
  and neither trace turns. Any centre found there
  owes its own end-clamp read before quotation,
  as this one carried. (This is the third
  widening in the line; the anti-loop discipline
  notes that each widening so far has been
  charged by the previous phase's measured
  edge-pressing, not by repetition of a failed
  mechanism — the mechanism, diagonal ascent,
  keeps paying.)
- The dwell→harvest cycle at the new centre
  (390's pattern, owed at each new centre by the
  line's own discipline), and scaling iterated
  with that harvest.
- A Gate for this claim set before any
  publication (the standing route).

## 8. Fences and accounting

Band-posed [10, 20] SET-244 / SAMPLER-M levels;
356's full-extent caveats travel (the lineage's
full-extent levels ≈ −1.44×10⁻³ over [10, 60]
stand untouched; no full-extent read of the new
centre is claimed here). No EC pass (the level
is negative); no member; no sustainment, front
or transport content. Sampled minima name their
frame convention (SAMPLER-M, the lineage's
eulerian_that association, Gate-43 C-10); the
deciding values are the diff-0.0 reproductions
and the frame-invariant worst-nulls.

Goal 1 (FTL drive): the stationary pressure
level improves again — progression in §4. The
wall moved again; it did not break. Goal 2
(wormhole): untouched. Goal 3 (subluminal
record): untouched.

DESK: NO DATA CONTACT.

Artefacts: `phase395/work/p395_registration.md`,
`p395_lib.py`, `p395_controls.py`,
`p395_admission.py`, `p395_search.py`,
`p395_confirm.py`, `p395_clamp.py`,
`p395_anatomy.py`;
`phase395/results/p395_controls.json`,
`p395_controls_laptop.json`,
`p395_screens.jsonl` (+ `parts/`),
`p395_search_summary.json`, `p395_anatomy.json`,
`p395_confirmation.json`, `p395_clamp.json`,
`p395_memo.md`, control and search logs.

Spend: VM wall ≈ 17 min total (controls 104.9 s,
search ≈ 13 min, confirmation + clamp + anatomy
≈ 1.5 min); laptop: the admission read only.
