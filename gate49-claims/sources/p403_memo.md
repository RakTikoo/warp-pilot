# PHASE 403 MEMO — THE POSE SEARCH

**VERDICT: POSE SEARCH RAISES — GATE REFERRAL.**
Step 1: the width trend does NOT turn — C395's
transported joint rises monotonically through
every charged width to the registered cap
W28 [1, 29] (−9.384899×10⁻⁶, +2.042495×10⁻⁵ over
home), with the per-unit-width increments
decaying steadily (2.54 → 0.48 ×10⁻⁶ per unit)
but still positive at the cap. Step 2: the
scaling re-optimisation at W28 pays a further
+5.708787×10⁻⁶ beyond the C-10 band. The new
centre — pose [1, 29], triple (μ_S, μ_N, μ_M) =
(0.5000090643041506, 1.8999807308424006,
4.892092241322827) — reads joint
**−3.676112×10⁻⁶** (SET-244, band pose [1, 29]
under transport), exact worst-null
−5.242074×10⁻⁶ at its NEC argmin, end-clamped
−3.811020×10⁻⁶. It beats C395's home level by
+2.613374×10⁻⁵, with the worst-null improving
alongside (+2.565414×10⁻⁵, no disagreement
flag). THREE RIDERS RIDE ON ITS FACE: (1) it
presses the registered box's μ_S edge (9.1×10⁻⁶
above 0.50) and μ_N edge (1.9×10⁻⁵ below 1.90)
— it is the optimum OF THE REGISTERED BOX at
the widened pose, not a certified interior
optimum; (2) its SS7 physicality peak
|β·S| = 0.442682 CLEARS the half-of-H2 bar
(0.442674) by only 8.0×10⁻⁶ — the search used
essentially all the non-degenerate room the
criterion allows, and whether "at the bar" is
substance is the gate's question, not this
phase's; (3) it is a BAND read at its pose
under transport — no full-extent audit at W28
has run, and it is quotable only as such until
one does. The level remains negative: no
energy-condition pass, no member.

Charged at ledger entry 1039 (Phase 402's named
successor). Registration filed before any
computation: `phase403/work/p403_registration.md`
(SS0–SS9; SS5 records the polish-method note —
the charge's "Powell polish" resolves to the
394/395 registered Nelder-Mead pattern, stated
on the registration's face).

## Controls (registration SS3 — all pass)

VM: CTL-403-C395-HOME (the lineage read at C395
reproduces all five stored minima and the
worst-null −3.0896210095678075×10⁻⁵ at diff 0.0;
Type-I count 4067), CTL-403-POSE-HOME (this
phase's machinery at [10, 20] reproduces that
read at diff 0.0 on every field), CTL-403-W12
and CTL-403-W14 (402's transported rows
reproduced at diff 0.0: joints
−2.4728052267161693×10⁻⁵ / −2.050976956715771×10⁻⁵,
worst-nulls, DEC, ρ, Type-I counts 4093 / 4097),
CTL-403-H2 ((1,1,1) → L_stat(H2) at diff 0.0).
Record: `p403_controls.json` (32 s).

LAPTOP ADMISSION (CTL-403-ADM): NOT ADMITTED —
the Gate-43 C-10 signature, the same pattern as
402's: frame-invariant fields at roundoff (dec
diff 2.2×10⁻¹⁹, ρ diff 0.0), Type-I count exact,
but the sampled NEC/WEC minima drift by
1.61×10⁻⁷ / 1.77×10⁻⁶ with the laptop's NEC
argmin on the sibling shell (r = 15.488 vs the
VM's 15.732). All deciding reads are VM reads.
Record: `p403_controls_laptop.json`.

## Step 1 — the width response curve

Transported C395 (its own triple; SET-244 joint
= min(nec, dec); SAMPLER-M / eulerian_that,
Gate-43 C-10; worst-null exact at the SET NEC
argmin). W10/W12/W14 are 402's rows, reproduced
under SS3:

| W | pose | λ | joint | Δ vs prev | worst-null | DEC min | ρ_min | NEC @ r |
|---|---|---|---|---|---|---|---|---|
| 10 | [10, 20] | 1.000 | −2.980985×10⁻⁵ | — | −3.089621×10⁻⁵ | −1.777×10⁻⁶ | +9.781×10⁻⁵ | 15.732 |
| 12 | [9, 21] | 0.833 | −2.472805×10⁻⁵ | +5.082×10⁻⁶ | −2.660769×10⁻⁵ | −1.314×10⁻⁶ | +8.887×10⁻⁵ | 15.585 |
| 14 | [8, 22] | 0.714 | −2.050977×10⁻⁵ | +4.218×10⁻⁶ | −2.268065×10⁻⁵ | −1.050×10⁻⁶ | +8.110×10⁻⁵ | 15.683 |
| 16 | [7, 23] | 0.625 | −1.792647×10⁻⁵ | +2.583×10⁻⁶ | −1.970635×10⁻⁵ | −8.669×10⁻⁷ | +7.431×10⁻⁵ | 15.780 |
| 18 | [6, 24] | 0.556 | −1.571427×10⁻⁵ | +2.212×10⁻⁶ | −1.702465×10⁻⁵ | −7.329×10⁻⁷ | +6.834×10⁻⁵ | 15.878 |
| 20 | [5, 25] | 0.500 | −1.393772×10⁻⁵ | +1.777×10⁻⁶ | −1.522698×10⁻⁵ | −6.306×10⁻⁷ | +6.306×10⁻⁵ | 15.976 |
| 24 | [3, 27] | 0.417 | −1.128452×10⁻⁵ | +2.653×10⁻⁶ | −1.253404×10⁻⁵ | −4.854×10⁻⁷ | +5.418×10⁻⁵ | 16.171 |
| 28 | [1, 29] | 0.357 | **−9.384899×10⁻⁶** | +1.900×10⁻⁶ | −1.054503×10⁻⁵ | −3.879×10⁻⁷ | +4.705×10⁻⁵ | 16.366 |

- NO TURN, NO INFEASIBILITY: every width is
  C1-feasible and floor-feasible; the stop is
  the registered CAP (SS4(c)) — the trend is
  unturned at W28, the box-edge disclosure
  pattern of 394/395 transposed to the pose.
  The best width in the registered set is 28.
- THE INCREMENTS DECAY: per unit width the gain
  falls 2.54 → 2.11 → 1.29 → 1.11 → 0.89 → 0.66
  → 0.48 (×10⁻⁶). The curve is still rising at
  the cap but flattening toward the band scale;
  ρ_min falls steadily alongside (9.78 → 4.71
  ×10⁻⁵) — widening spends density margin to
  buy pressure level.
- The worst-null improves at every width in the
  same direction as the joint (no disagreement
  flag anywhere on the curve); the joint stays
  purely NEC-bound (DEC recedes from
  −1.78×10⁻⁶ to −3.88×10⁻⁷ across the curve).
  The transported object's SS7 peak is
  0.532255 at every width (transport rescales
  no profile value), ratio 0.6012 to H2's.

## Step 2 — the re-optimisation at W28 [1, 29]

Registered box μ_S ∈ [0.50, 1.10], μ_N ∈
[0.95, 1.90], μ_M ∈ [1.60, 6.50] (SS5: past
every edge C395 presses or nears at home; the
μ_S lower edge is the SS7 boundary itself).
Anchor = C395's triple, its read at the pose
being Step 1's W28 row. 334 stored reads, ALL
feasible, ZERO DEC-saturated (the worst DEC
over all reads is −4.327×10⁻⁷ — DEC is nowhere
near binding anywhere in this search), 334
beat C395's home level, 329 beat the
transported seed.

- RAY (pure μ_M from the anchor): rises gently
  to −8.998×10⁻⁶ at μ_M = 5.75, then wiggles at
  the 10⁻⁸ scale (−9.012, −9.040, −8.987 ×10⁻⁶
  at 6.0 / 6.25 / 6.5) — the ray alone buys
  only ≈ +3.9×10⁻⁷ over the seed. As at home:
  the gain is not on the axis.
- DIAG (the (−0.025, +0.025, +0.25) diagonal):
  rises at every step with GROWING increments
  (−8.149, −7.185, −6.192, −5.221 ×10⁻⁶) — the
  road to the corner, as in 394/395.
- G1 found the (μ_S ↓, μ_N ↑) slope at fixed
  μ_M (best grid point (0.525, 1.875, A_M));
  G3's cube walked it to the corner (0.50,
  1.90, A_M) at −3.787147×10⁻⁶; G4's polish
  settled a hair inside it; G5, polished from
  the DIAG endpoint, converged to the same
  basin (−3.861226×10⁻⁶) and did not beat G4.

CONFIRMED WINNER (full re-read at diff 0.0
against its screen on all five minima;
adversary-polished at the pose; exact
worst-null at the argmin):

  pose [1, 29] (W28, centre 15, λ = 5/14)
  (μ_S, μ_N, μ_M) = (0.5000090643041506,
                     1.8999807308424006,
                     4.892092241322827)
  joint (SET-244)      −3.676112×10⁻⁶
  worst-null @ argmin  −5.242074×10⁻⁶ (frame-invariant)
  adversary depth      −3.928911×10⁻⁷ (Type-I-restricted)
  DEC min              −3.809243×10⁻⁷ @ r = 25.927
  ρ_min                +4.705527×10⁻⁵
  Type-I count         4603 (fraction 0.693)
  end-clamped joint    −3.811020×10⁻⁶ (cost 1.349×10⁻⁷)

## Anatomy of the winner

- THE JOINT IS NEC-BOUND AT A NON-TYPE-I POINT;
  THE TYPE-I SECTOR IS NEARLY LEGAL. The SET
  NEC argmin sits at r = 17.049 (= φ⁻¹ of
  C395's home argmin 15.732 — the site tracks
  the transport) and is not Type-I; the exact
  worst-null there is −5.242074×10⁻⁶. Over
  Type-I points the configuration is far
  shallower: the adversary polish's depth is
  −3.928911×10⁻⁷ (its starts were the SET's
  Type-I NEC samples at ≈ −3.81×10⁻⁷, the DEC
  minimum's own scale). Both statistics are
  reported; the verdict rests on the joint, the
  lineage's deciding statistic, with the
  frame-invariant worst-null confirming the
  direction.
- AT THE BINDING SITE the transported scaled
  locals are S = 0.14855, S′ = −0.02721,
  S′′ = +0.00136, N = 2.33544, N′ = +0.00961,
  N′′ = −0.00069, M = 25.679, M′ = +1.71308,
  M′′ = −0.11723 — against transported H2 at
  the same radius (S = 0.29710, N = 1.22919,
  M = 6.04464): the winner halves the shift,
  doubles the lapse factor, and carries M ≈ 25.7
  at the site (band M range [1.610, 34.756]).
- PHYSICALITY ROW (SS7): band peak |β·S| =
  0.44268227409480604; H2's peak
  0.8853484980534808; ratio 0.500009 — the peak
  ratio equals μ_S, as Gate-47 measured. The
  winner CLEARS the half-of-H2 bar
  (0.4426742490267404) by 8.03×10⁻⁶. It is
  therefore NOT an artefact candidate under
  the registered criterion — but the margin is
  the polish's hair, and the box's μ_S edge was
  placed at the boundary by construction: the
  criterion and the search boundary coincide
  here, and the gate referral carries that
  fact on its face.
- BOX EDGES: μ_S 9.064×10⁻⁶ above the lower
  edge; μ_N 1.927×10⁻⁵ below the upper edge;
  μ_M interior (3.292 above the lower edge,
  1.608 below the upper). The centre presses
  TWO edges — quotable only as the optimum of
  the registered box at this pose (the
  G45-E/G46-E/G47-E rider pattern).
- END-CLAMP: the winner clamps to
  −3.811020×10⁻⁶ (cost 1.349×10⁻⁷, the
  lineage's usual small tax); the transported
  seed at the same pose clamps to
  −9.384854×10⁻⁶ (cost −4.5×10⁻¹¹, nil).
- GAIN DECOMPOSITION: transport alone
  +2.042495×10⁻⁵ (68% of the total gain);
  re-optimisation at the pose a further
  +5.708787×10⁻⁶ (beyond the band — the scaling
  genuinely pays at the new pose too, it is
  not pose-only); total +2.613374×10⁻⁵ over
  C395's home level. The winner's level is
  1.9% of L_stat(H2)'s magnitude, and it is
  twice C396's flagged level (−7.432×10⁻⁶)
  while clearing the physicality bar C396
  failed — the comparison is stated for the
  record, with C396's rider (G47-F) untouched.

## Verdict mapping (registration SS7)

- POSE SEARCH RAISES: FIRES. The confirmed
  best joint beats C395's home joint by
  +2.613374×10⁻⁵ > the +3×10⁻⁶ band, and the
  worst-null improves alongside
  (+2.565414×10⁻⁵) — no disagreement flag, so
  the verdict does not fall back to the
  worst-null. GATE REFERRAL, carrying the
  three riders of the verdict paragraph (box
  edges, the at-the-bar physicality margin,
  band-read-at-pose status).
- WIDTH TURNS WITHOUT PAYING: does not fire
  (no turn; the re-optimisation pays).
- COST-BOUNDED: does not fire (334 of the 400
  registered reads used; the full pattern
  completed).

## Fences

Every read is a BAND read over its pose under
SS1's transport — not a full-extent
re-derivation (Phase 356): the winner is
quotable only as a band read at pose [1, 29]
until a full-extent audit at that pose runs;
the home objects' full-extent restatements
stand untouched. Sampled minima name their
frame convention (SAMPLER-M, the lineage's
eulerian_that association, Gate-43 C-10); the
deciding values are the diff-0.0 control
reproductions and the frame-invariant
worst-null at the named argmin point. No EC
pass (the level is negative); no member; no
sustainment, front or transport content.

Goal 1 (FTL drive): the pressure wall's price
is pose-dependent in the width direction, and
the pose is now a priced, searched lever: the
certified design centre's level improves from
−2.98×10⁻⁵ to −3.68×10⁻⁶ by widening the band
pose to [1, 29] and re-optimising there — an
8.1× reduction of the standing level, with the
width trend still unturned at the registered
cap and the winner pressed against the
physicality boundary. The wall did not break;
its cheapest known direction is now the pose
itself, and the next questions (wider poses
past the cap's geometric fence, the
full-extent audit at W28, the gate's ruling on
the at-the-bar margin) are named for the
parent. Goal 2 (wormhole): untouched. Goal 3
(subluminal record): untouched.

DESK: NO DATA CONTACT.

Artefacts: `phase403/work/p403_registration.md`,
`p403_lib.py`, `p403_controls.py`,
`p403_admission.py`, `p403_step1.py`,
`p403_search.py`, `p403_confirm.py`;
`phase403/results/p403_controls.json`,
`p403_controls_laptop.json`, `p403_step1.json`,
`p403_screens.jsonl` (+ `parts/`),
`p403_search_summary.json`,
`p403_confirmation.json`, `p403_clamp.json`,
`p403_anatomy.json`, `p403_memo.md`.

Spend: VM wall ≈ 35 min total (controls 32 s,
Step 1 32 s, search ≈ 31 min over 334 reads,
confirmation 87 s); laptop: the admission read
only (plus the phase403 mirror sync it
required).
