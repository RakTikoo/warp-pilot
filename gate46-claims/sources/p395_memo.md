# PHASE 395 MEMO — WIDEN THE BOX

**VERDICT: STATIONARY LEVEL IMPROVES AGAIN (gate
referral).** In the extended box registered before
searching (μ_S ∈ [0.60, 1.10], μ_N ∈ [0.95, 1.60],
μ_M ∈ [1.60, 5.00]), the scaling search seeded at
Phase 394's centre finds a new centre at
(μ_S, μ_N, μ_M) = (0.601180962300002,
1.5934531363763935, 4.887238651223381) on H2's total
profiles with SET-244 band level
**−2.980985×10⁻⁵** (band [10, 20]) —
+3.831668×10⁻⁵ over the anchor (394's centre,
−6.812653×10⁻⁵), +9.432734×10⁻⁵ over 393's ray
point, +1.458975×10⁻⁴ over 389's mixed centre,
+1.644147×10⁻⁴ over L_stat(H2). The improvement is
confirmed at pointwise grade (exact worst-null
−3.089621×10⁻⁵, +4.083532×10⁻⁵ over the anchor's)
and survives the end-clamp re-read inside this
charge (clamped level −3.018921×10⁻⁵, clamp cost
3.794×10⁻⁷). The level remains NEGATIVE — no
energy-condition pass, no member.

**BOX-EDGE DISCLOSURE (on the face of the claim):**
the new centre PRESSES the extended box's μ_S
lower edge (μ_S = 0.60118, 0.00118 above the edge
0.60 — the same margin by which 394's centre
pressed its box) and NEARS the μ_N upper edge
(1.59345, 0.00655 below 1.60); μ_M = 4.88724 sits
inside its edge (0.11276 below 5.00). The centre
is a local optimum of the searched box at polish
resolution (a tight cluster of five reads within
1.7×10⁻⁷), NOT a certified interior optimum of
the scaling surface: whether the level keeps
rising for μ_S < 0.60 or μ_N > 1.60 is UNMEASURED.

Quotable wording (gate-referral form): "On the A2
lineage's per-profile scaling surface, in the
registered extended box μ_S ∈ [0.60, 1.10],
μ_N ∈ [0.95, 1.60], μ_M ∈ [1.60, 5.00], the best
stationary band level (SET-244, SAMPLER-M, band
[10, 20]) is −2.980985×10⁻⁵ at (0.601181, 1.593453,
4.887239), NEC-bound, confirmed at pointwise grade
(worst-null −3.089621×10⁻⁵) and under the
end-clamp re-read (−3.018921×10⁻⁵); the centre
presses the box's μ_S edge and nears its μ_N edge,
so the figure is the best level IN THE REGISTERED
BOX, with the surface beyond those edges
unmeasured. The level is negative: no
energy-condition pass is claimed."

## The numbers

| quantity | anchor (394) | new centre |
|---|---|---|
| joint (SET-244) | −6.812653×10⁻⁵ | **−2.980985×10⁻⁵** |
| NEC | −6.812653×10⁻⁵ @ 15.488 | −2.980985×10⁻⁵ @ 15.732 |
| DEC | −4.611098×10⁻⁶ @ 18.171 | −1.776685×10⁻⁶ @ 18.659 |
| ρ_min | +9.678145×10⁻⁵ | +9.780858×10⁻⁵ |
| worst-null @ NEC argmin | −7.173153×10⁻⁵ | −3.089621×10⁻⁵ |
| polished depth | −4.730182×10⁻⁶ | −1.844219×10⁻⁶ |
| end-clamped joint | −6.968823×10⁻⁵ | **−3.018921×10⁻⁵** |

220 stored SET-244 reads, EVERY read C1-feasible
and floor-feasible, 212 of them beating the
anchor. Not one DEC-saturated read in the box —
the worst DEC over all 220 reads is −6.553×10⁻⁶,
and at the centre DEC (−1.78×10⁻⁶) sits a factor
~17 above NEC: the joint is purely NEC-bound in
this region, further outside 387's past-branch
regime than 394's box was.

## Anatomy in brief

- THE GAIN IS STILL DIAGONAL. The pure μ_M ray
  from the anchor first DIPS (−6.912×10⁻⁵ at
  μ_M = 3.75) and then rises monotonically to the
  box edge (−6.334×10⁻⁵ at 5.00) with no turn —
  the whole ray accounts for +4.79×10⁻⁶ of the
  phase's +3.83×10⁻⁵. The registered diagonal
  (μ_S down, μ_N up, μ_M up) rises at every step
  (+5.08, +5.50, +4.65, +4.72 ×10⁻⁶) with no turn
  inside the box either.
- TWO POLISHES, TWO ANSWERS, ONE TEXTURE: the G4
  polish from the G1/G3 corner incumbent
  (0.625, 1.60, 5.00) returned exactly its start
  point (−3.189372×10⁻⁵) — that corner is a local
  optimum of the box at polish resolution. The G5
  polish from the diagonal's end walked past it
  to the centre above. The ascent direction is
  unchanged from 394's; this box simply gives it
  more room, and it uses the room.
- THE CENTRE PRESSES AN EDGE AGAIN (see the
  disclosure): the pattern of 394 repeats one box
  further out — each widening has moved the centre
  and the centre has arrived at or near the new
  μ_S edge both times. The surface's peak, if it
  has one in this direction, is not yet in view;
  what is measured is a sustained diagonal ascent
  with undiminished step gains (the diagonal's
  increments do not decay across the box).

## Fences

Band pose [10, 20] only; 356's full-extent
caveats travel (lineage full-extent levels
≈ −1.44×10⁻³ over [10, 60] stand untouched; no
full-extent read of the new centre is claimed).
No EC pass, no member, no sustainment, front or
transport content. Sampled minima name their
frame convention (SAMPLER-M, the lineage's
eulerian_that association, Gate-43 C-10); the
deciding values are the diff-0.0 reproductions
and the frame-invariant worst-nulls. Controls:
ALL PASS at diff 0.0 (H2, mixed centre, seed,
anchor incl. worst-null and depth; clamp
construction at diff 0.0 on the H2 and anchor
legs, 2.17×10⁻¹⁹ on the Gate-43 mixed leg).
Laptop NOT ADMITTED (fifteenth consecutive
occurrence); all deciding reads are VM reads.

DESK: NO DATA CONTACT.
