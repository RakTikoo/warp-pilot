# PHASE 394 — SCALING SEARCH SEEDED AT THE RAY POINT

**VERDICT: STATIONARY LEVEL IMPROVES AGAIN. The best
stationary band level on the A2 lineage is now
−6.812653×10⁻⁵ (SET-244, band [10, 20]) at the new
centre (μ_S, μ_N, μ_M) = (0.8015689430763502,
1.3179449338854314, 3.574968377899082) on H2's total
profiles — +5.601066×10⁻⁵ over the seed (393's ray
point, −1.241372×10⁻⁴), +1.075808×10⁻⁴ over 389's
mixed centre, +1.260980×10⁻⁴ over L_stat(H2). The
improvement is confirmed at pointwise grade
(worst-null −7.173153×10⁻⁵, +5.304123×10⁻⁵ over the
seed's) and survives the end-clamp re-read inside
this charge (clamped level −6.968823×10⁻⁵, clamp
cost 1.562×10⁻⁶). The level remains NEGATIVE — no
energy-condition pass, no member. GATE REFERRAL.**

Charged at ledger entry 1009. Registration filed
before any computation:
`phase394/work/p394_registration.md` (SS0–SS7).
Frame of record: the VM (laptop NOT admitted — §2).

## 1. The act

389's search pattern (grid, axes, refinement,
polish) over the full per-profile scaling space of
H2's totals, seeded at 393's ray point R_M(2.0) =
(0.9323593026620368, 1.1444417317708335,
2.289013671875), in the registered box μ_S ∈
[0.80, 1.10], μ_N ∈ [0.95, 1.35], μ_M ∈ [1.60, 3.60].
349 stored SET-244 reads (RAY 8, G1 41, G2 9,
G3 26, G5 127, G4 138; cap 400 not binding), EVERY
read C1-feasible and floor-feasible, and not one
DEC-saturated read in the box (worst DEC over all
reads −5.392×10⁻⁵).

## 2. Controls (VM: ALL PASS)

Record: `phase394/results/p394_controls.json`.

- CTL-394-H2S: (1, 1, 1) reproduces L_stat(H2) at
  diff 0.0 (all five minima + polished depth).
- CTL-394-MIX: the mixed centre reproduces 393's
  anchor at diff 0.0 (all minima + depth).
- CTL-394-SEED: the seed reproduces 393's stored
  ray read at diff 0.0 on all five minima, and its
  exact worst-null at the SET NEC argmin reproduces
  at pointwise grade: −1.2477276305772507×10⁻⁴,
  diff 0.0.
- CTL-394-CLAMP: the SS5 end-clamp construction at
  (1, 1, 1) reproduces 379's stored end-clamp read
  at diff 0.0 (NEC/DEC/ρ); at the mixed centre the
  lineage clamped joint agrees with Gate-43's
  independent AD-machinery value
  −1.7669632754376664×10⁻⁴ at 2.17×10⁻¹⁹.
- Floors hold at the seed and the centre.

**Frame admission: LAPTOP NOT ADMITTED**
(fourteenth occurrence). Laptop seed read (mirror
p390root): NEC diff 2.744×10⁻⁷, WEC 1.602×10⁻⁵,
SEC 4.229×10⁻⁶; DEC 6.8×10⁻²⁰ and ρ 1.2×10⁻¹⁸ at
roundoff — the lineage pattern. Record:
`p394_controls_laptop.json`. All deciding reads
are VM reads.

## 3. The confirmed new centre

Confirmation (`p394_confirmation.json`): the full
re-read reproduces the stored screen minima at
diff 0.0.

| quantity | seed (393) | new centre |
|---|---|---|
| joint (SET-244) | −1.241372×10⁻⁴ | **−6.812653×10⁻⁵** |
| NEC | −1.241372×10⁻⁴ @ 12.317 | −6.812653×10⁻⁵ @ 15.488 |
| DEC | −3.435086×10⁻⁵ @ 19.634 | −4.611098×10⁻⁶ @ 18.171 |
| ρ_min | +9.469617×10⁻⁵ | +9.678145×10⁻⁵ |
| worst-null @ NEC argmin | −1.247728×10⁻⁴ | −7.173153×10⁻⁵ |
| polished depth | −3.679047×10⁻⁵ | −4.730182×10⁻⁶ |
| end-clamped joint | −1.247663×10⁻⁴ | **−6.968823×10⁻⁵** |

NEC-bound, by a wide margin now (DEC sits at
−4.6×10⁻⁶). Both argmins moved inward/off their
seed sites (NEC 12.317 → 15.488; DEC 19.634 →
18.171). The clamp cost at the new centre is
1.562×10⁻⁶ — the gain is again carried by the
scaling direction, not the correction vectors'
end knots (the Gate-43 pattern); the clamped
level still beats the seed's UNclamped level by
+5.445×10⁻⁵ and the mixed centre by +1.060×10⁻⁴.
The rider 393 owed is measured, inside this
charge.

## 4. Anatomy (`p394_anatomy.json`)

- THE RAY (charge-required report): along the
  pure μ_M ray from the seed at (μ_S⁰, μ_N⁰), the
  level rises MONOTONICALLY to the box edge —
  −1.241372×10⁻⁴ (2.289) → −1.154605×10⁻⁴ (2.5)
  → −1.117751×10⁻⁴ (2.75) → −1.096222×10⁻⁴ (3.0)
  → −1.069928×10⁻⁴ (3.25) → −1.041328×10⁻⁴ (3.5)
  → −1.039017×10⁻⁴ (3.6) — with decaying
  increments (last step +2.31×10⁻⁷ over 0.1). NO
  TURN INSIDE THE BOX on the ray: the ray's peak
  is at or beyond the registered μ_M edge, and
  the ray alone accounts for only +2.02×10⁻⁵ of
  the phase's +5.60×10⁻⁵.
- THE GAIN IS DIAGONAL: at the seed the pure-axis
  slopes are small and sign-mixed (μ_S: +1.04×10⁻⁵
  per unit downward at the 0.05 step, −1.33×10⁻⁵
  upward; μ_N: −1.15×10⁻⁵ downward, −0.88×10⁻⁵
  upward; μ_M downward −0.30 step: the level falls
  at 7.35×10⁻⁵ per unit). The ascent runs along
  the joint direction (μ_S down, μ_N up, μ_M up):
  G1's corner (0.85, 1.25, 3.5) already read
  −8.136279×10⁻⁵, and the G5 polish (started from
  the ray's edge point) walked it to the centre
  of §3. 389's cooperativity (cross terms the
  size of the diagonal terms) is the same texture
  one neighbourhood further out.
- THE CENTRE PRESSES THE μ_S EDGE: the incumbent
  sits at μ_S = 0.80157, 0.0016 above the
  registered box's lower edge, in a tight flat
  cluster (four further reads within 3.1×10⁻⁷).
  The G4 polish — a fresh Nelder-Mead simplex
  from the incumbent, 150 evaluations — returned
  exactly its start point: the centre is a local
  optimum of the searched box at polish
  resolution. Whether the level keeps rising for
  μ_S < 0.80 is UNMEASURED (named follow-up, §7);
  μ_N = 1.318 and μ_M = 3.575 sit inside their
  edges (1.35, 3.60).
- NO SATURATION ANYWHERE IN THE BOX: all 349
  reads feasible, worst DEC −5.392×10⁻⁵ — this
  neighbourhood is entirely outside 387's
  past-branch regime (contrast 389's saturated
  corner at low μ_N/μ_M).
- RECONCILIATION WITH 389: 389's concavity was a
  fit over the cube μ ∈ [0.90, 1.10]³ around H2 —
  a local statement about that neighbourhood, and
  it stands. The seed region (μ_M ≈ 2.3–3.6,
  μ_S ≈ 0.80, μ_N ≈ 1.32) is a different
  neighbourhood of the same surface, separated
  from H2's by 393's dip along the ray; the two
  readings describe different neighbourhoods and
  neither revises the other. The surface has at
  least two ascent regions, and the second is
  higher.

## 5. Incidents (disclosed)

- The first G4 polish invocation no-opped: a
  dropped load_done() in this phase's driver made
  its start-up read an empty store and report "no
  feasible point yet" (its own log line). Caught
  from the log, fixed, and rerun in full (138
  stored reads). No read was lost; every stage's
  part file is intact, and the confirmation's
  diff-0.0 reproduction covers the best point.
- Stage execution order: G5 (the ray-start polish)
  ran before the repaired G4 (the incumbent-start
  polish). The registration's pattern — two
  polishes from two distinct starts — is intact
  in substance; the order swap is recorded here.

## 6. Verdict mapping (registration SS6)

- STATIONARY LEVEL IMPROVES AGAIN: FIRES. SET
  gain over the seed +5.601066×10⁻⁵ > the
  registered 1×10⁻⁶ bar, AND the confirmed
  worst-null beats the seed's by +5.304123×10⁻⁵.
  New centre, SET level, pointwise level and
  clamped level all stated (§3). Gate referral.
- THE RAY POINT IS A RIDGE: does not fire — the
  polish did not slide back; it climbed across
  the ray to a distinct, higher centre.
- COST-BOUNDED: does not fire (349 of 400 reads;
  all stages complete).

## 7. Named follow-ups (not run)

- A scaling search in a box extended below
  μ_S = 0.80 (and, on the ray's evidence, beyond
  μ_M = 3.60): the centre presses one registered
  edge and the ray was still rising, slowly, at
  the other. Any centre found there owes its own
  end-clamp read before quotation, as this one
  carried.
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
level improves again — the lineage progression
is now −1.942246×10⁻⁴ (379, H2) → −1.757074×10⁻⁴
(389, mixed) → −1.241372×10⁻⁴ (393, ray point)
→ −6.812653×10⁻⁵ (394). The wall moved again;
it did not break. Goal 2 (wormhole): untouched.
Goal 3 (subluminal record): untouched.

DESK: NO DATA CONTACT.

Artefacts: `phase394/work/p394_registration.md`,
`p394_lib.py`, `p394_controls.py`,
`p394_admission.py`, `p394_search.py`,
`p394_confirm.py`, `p394_clamp.py`;
`phase394/results/p394_controls.json`,
`p394_controls_laptop.json`,
`p394_screens.jsonl` (+ `parts/`),
`p394_search_summary.json`, `p394_anatomy.json`,
`p394_confirmation.json`, `p394_clamp.json`,
`p394_memo.md`, search logs.

Spend: VM wall ≈ 21 min total (controls ≈ 1 min,
search ≈ 20 min across both driver runs,
confirmation + clamp ≈ 1 min, anatomy
negligible); laptop: the admission read only.
