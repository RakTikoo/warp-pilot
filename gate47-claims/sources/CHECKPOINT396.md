# PHASE 396 — THE THIRD WIDENING

**VERDICT: STATIONARY LEVEL IMPROVES AGAIN — WITH
A DEGENERACY NOTE ON ITS FACE (SS7). The best
stationary band level on the A2 lineage is now
−7.431892×10⁻⁶ (SET-244, band [10, 20]) at the new
centre (μ_S, μ_N, μ_M) = (0.4003528067864536,
1.9863455070489624, 6.715383396291902) on H2's
total profiles — +2.237796×10⁻⁵ over the anchor
(395's centre, −2.980985×10⁻⁵), +6.067464×10⁻⁵
over 394's centre, +1.682755×10⁻⁴ over 389's mixed
centre, +1.867927×10⁻⁴ over L_stat(H2). The
standing level is now 3.83% of its H2 magnitude.
The improvement is confirmed at pointwise grade
(worst-null −8.706719×10⁻⁶, +2.218949×10⁻⁵ over
the anchor's) and survives the end-clamp re-read
inside this charge (clamped level −7.644644×10⁻⁶,
clamp cost 2.128×10⁻⁷). DEGENERACY NOTE (SS7,
pre-registered): the centre's peak physical shift
over the band is |β·S| = 0.354, 40.0% of H2's peak
0.885 — below the registered half-of-H2 flag — so
by the charge's own criterion the level gain is
substantially purchased by shift removal (with
the lapse doubled and the M-deformation grown
~6×, §4): the point is a SCALING-FAMILY ARTEFACT
CANDIDATE, not a design improvement, until a gate
rules otherwise. BOX-EDGE DISCLOSURE: the centre
presses the extended box's μ_S lower edge
(0.00035 above 0.40) and nears its μ_N upper edge
(0.01365 below 2.00); it is a local optimum of
the searched box at polish resolution, not a
certified interior optimum of the surface. The
level remains NEGATIVE — no energy-condition
pass, no member. GATE REFERRAL, with the
degeneracy note as a charged item.**

Charged at ledger entry 1018. Registration filed
before any computation:
`phase396/work/p396_registration.md` (SS0–SS8).
Frame of record: the VM (laptop NOT admitted —
§2).

## 1. The act

389/394/395's search pattern (traces, grid, axes,
refinement, two polishes) over the full
per-profile scaling space of H2's totals, seeded
at 395's centre (the ANCHOR), in the registered
extended box μ_S ∈ [0.40, 1.10], μ_N ∈ [0.95,
2.00], μ_M ∈ [1.60, 7.00] — extended past every
edge the 395 centre presses (μ_S 0.60) or nears
(μ_N 1.60, μ_M 5.00), with the anchor strictly
inside. 336 stored SET-244 reads (RAY3 7, DIAG 8,
G1 24, G2 12, G3 26, G4 128, G5 131 — new reads
stored per stage, deduplicated against the store;
cap 400 not binding), EVERY read C1-feasible and
floor-feasible, 326 of them beating the anchor,
and not one DEC-saturated read in the box (worst
DEC over all reads −2.025×10⁻⁶).

## 2. Controls (VM: ALL PASS)

Record: `phase396/results/p396_controls.json`.

- CTL-396-H2S: (1, 1, 1) reproduces L_stat(H2) at
  diff 0.0 (all five minima + polished depth).
- CTL-396-MIX: the mixed centre reproduces 393's
  anchor at diff 0.0 (all minima + depth).
- CTL-396-SEED: the seed reproduces 393's stored
  ray read at diff 0.0 on all five minima, and its
  exact worst-null at the SET NEC argmin
  reproduces at pointwise grade:
  −1.2477276305772507×10⁻⁴, diff 0.0.
- CTL-396-C394: 394's centre reproduces 395 SS1's
  stored values at diff 0.0 (all five minima +
  polished depth), and its exact worst-null at
  the SET NEC argmin reproduces at pointwise
  grade: −7.173153284502476×10⁻⁵, diff 0.0.
- CTL-396-ANCHOR: the anchor reproduces SS1's
  stored values at diff 0.0 (all five minima +
  polished depth), and its exact worst-null at
  the SET NEC argmin reproduces at pointwise
  grade: −3.0896210095678075×10⁻⁵, diff 0.0.
- CTL-396-CLAMP: the SS5 end-clamp construction
  at (1, 1, 1) reproduces 379's stored end-clamp
  read at diff 0.0 (NEC/DEC/ρ); at the mixed
  centre the lineage clamped joint agrees with
  Gate-43's independent AD-machinery value
  −1.7669632754376664×10⁻⁴ at 2.17×10⁻¹⁹; at C394
  the clamped joint reproduces 395's stored
  −6.968822658140883×10⁻⁵ at diff 0.0; at the
  ANCHOR the clamped joint reproduces 395's
  stored −3.0189206094012074×10⁻⁵ at diff 0.0.
- Floors hold at the seed, the centre, C394 and
  the anchor.

**Frame admission: LAPTOP NOT ADMITTED**
(sixteenth occurrence). Laptop anchor read
(mirror p390root): NEC diff 1.612×10⁻⁷, WEC
1.766×10⁻⁶ (the laptop's NEC argmin lands on the
neighbouring radial node, r = 15.488 vs the VM's
15.732); DEC 2.2×10⁻¹⁹, SEC 3.1×10⁻¹⁸ and ρ 0.0
at roundoff — the lineage pattern. Record:
`p396_controls_laptop.json`. All deciding reads
are VM reads.

## 3. The confirmed new centre

Confirmation (`p396_confirmation.json`): the full
re-read reproduces the stored screen minima at
diff 0.0 (NEC/DEC/ρ).

| quantity | anchor (395) | new centre |
|---|---|---|
| joint (SET-244) | −2.980985×10⁻⁵ | **−7.431892×10⁻⁶** |
| NEC | −2.980985×10⁻⁵ @ 15.732 | −7.431892×10⁻⁶ @ 16.463 |
| DEC | −1.776685×10⁻⁶ @ 18.659 | −1.097932×10⁻⁶ @ 18.902 |
| ρ_min | +9.780858×10⁻⁵ | +9.858014×10⁻⁵ |
| worst-null @ NEC argmin | −3.089621×10⁻⁵ | −8.706719×10⁻⁶ |
| polished depth | −1.844219×10⁻⁶ | −1.132046×10⁻⁶ |
| end-clamped joint | −3.018921×10⁻⁵ | **−7.644644×10⁻⁶** |

NEC-bound, purely: DEC sits a factor ~6.8 above
NEC at the centre, the Type-I fraction rose to
0.716 (395's centre: 0.612), and ρ_min did not
fall — it rose slightly. The clamp cost at the
new centre is 2.128×10⁻⁷ — the gain is again
carried by the scaling direction, not the
correction vectors' end knots (the Gate-43
pattern). The clamped level still beats the
anchor's UNclamped level by +2.216520×10⁻⁵ and
the mixed centre's unclamped level by
+1.680309×10⁻⁴. The rider is measured, inside
this charge.

## 4. Anatomy (`p396_anatomy.json`,
`p396_physicality.json`)

- THE DIAGONAL DOES NOT TURN (the charge's
  headline item): the registered direction
  (−0.025, +0.025, +0.25) from the anchor, traced
  k = 1..8 to the box's corner region at
  (0.40118, 1.79345, 6.88724), rises at EVERY
  step: −2.693110×10⁻⁵, −2.397925×10⁻⁵,
  −2.130771×10⁻⁵, −1.853953×10⁻⁵, −1.621570×10⁻⁵,
  −1.384676×10⁻⁵, −1.172000×10⁻⁵, −9.943226×10⁻⁶.
  Increments (from the anchor): +2.879, +2.952,
  +2.672, +2.768, +2.324, +2.369, +2.127, +1.777
  ×10⁻⁶ — a MILD decay (the last is 62% of the
  first) but no sign change, no collapse: the
  trace ends because it reaches the μ_S edge
  region of the registered box, not because the
  surface turns. The ridge is still rising at
  the corner.
- THE POLISH GOES PAST THE DIAGONAL'S END: the
  G4 polish, started from the G3 incumbent
  (0.40, 1.81845, 6.78724; −9.524129×10⁻⁶),
  walked to the centre of §3 — it trades the
  diagonal's remaining μ_M for μ_N (1.986 vs the
  diagonal end's 1.793) at the μ_S edge and gains
  +2.511×10⁻⁶ for it. The G5 polish, started
  independently from the diagonal's end point,
  converged to the same corner basin
  (0.40101, 1.98306, 6.94061) at −7.471375×10⁻⁶:
  two polishes, one basin, pressed against the
  same two edges.
- THE RAY: along the pure μ_M ray from the
  anchor, the level first DIPS — −2.985616×10⁻⁵
  at μ_M = 5.5, 4.6×10⁻⁸ below the anchor — then
  rises monotonically to the box edge:
  −2.932960×10⁻⁵ (5.75) → −2.931584×10⁻⁵ (6.0)
  → −2.888320×10⁻⁵ (6.5) → −2.852110×10⁻⁵ (7.0).
  NO TURN INSIDE THE BOX on the ray, and the ray
  alone accounts for only +1.289×10⁻⁶ of the
  phase's +2.238×10⁻⁵.
- THE CENTRE PRESSES TWO EDGES (the box-edge
  disclosure, on the verdict's face): the
  incumbent sits at μ_S = 0.40035, 0.00035 above
  the extended box's lower edge — the third
  widening in a row whose centre has arrived at
  the new μ_S edge (394: 0.0016 above 0.80; 395:
  0.00118 above 0.60) — and nears the μ_N upper
  edge (0.01365 below 2.00); μ_M = 6.715 sits
  inside its edge (0.285 below 7.00). Whether
  the level keeps rising for μ_S < 0.40 or
  μ_N > 2.00 is UNMEASURED (§7).
- NO SATURATION ANYWHERE IN THE BOX: all 336
  reads feasible, worst DEC −2.025×10⁻⁶ — DEC
  has effectively left the stage in this region;
  the binding constraint is NEC alone, as in
  395's box, only more so.
- PHYSICALITY (SS7, on the verdict's face;
  `p396_physicality.json`): the scaled profiles
  over the band, H2 → anchor → centre:

  | | peak \|β·S\| | S range | N range | M range |
  |---|---|---|---|---|
  | H2 | 0.885 | [−0.0079, 0.8049] | [1.150, 1.237] | [1.125, 7.900] |
  | C394 | 0.710 | [−0.0063, 0.6452] | [1.516, 1.631] | [1.446, 25.667] |
  | anchor (395) | 0.532 | [−0.0047, 0.4839] | [1.832, 1.972] | [1.610, 34.722] |
  | centre (396) | **0.354** | [−0.0032, 0.3222] | [2.284, 2.458] | [1.838, 47.337] |

  At the centre's binding NEC site (r = 16.463)
  the local scaled values are S = 0.0774,
  S′ = −0.0515, S′′ = +0.0162; N = 2.4548,
  N′ = +0.0028, N′′ = −0.0361; M = 39.311,
  M′ = +5.484, M′′ = −1.582 — against H2's own
  totals at the same radius (S = 0.1934,
  N = 1.2358, M = 6.7049). The winning object is
  NOT H2's object gently rescaled: its shift is
  40% of H2's (in band peak and at the site
  alike), its lapse is doubled, and its spatial
  deformation at the binding site is ~5.9× H2's
  value there (band max 47.3 vs 7.9). The ridge's
  direction, measured across three boxes, is
  exactly (less shift, more lapse, more spatial
  deformation); the NEC terms the shift carries
  (316's anatomy: S′′ carries NEC/WEC/DEC)
  shrink mechanically as μ_S falls. It is not a
  pure vanishing-shift corner — a shift of peak
  |β·S| = 0.354 remains, and ρ_min rose rather
  than collapsing — but the pre-registered SS7
  flag fires (0.354 < 0.5 × 0.885), and the
  DEGENERACY NOTE stands on the verdict: the
  gain is substantially purchased by shift
  removal and N/M growth, and the centre is an
  artefact candidate until a gate rules.
- RECONCILIATION ACROSS THE ASCENT REGIONS:
  389's concavity was a fit over the cube
  μ ∈ [0.90, 1.10]³ around H2 — a local
  statement, and it stands. The second ascent
  region is a sustained diagonal ridge, now
  measured across three boxes (394, 395, 396),
  whose pure-axis sections are flat or dipping
  (the μ_M ray dips before it rises in both 395
  and 396) and whose diagonal increments decay
  only mildly. Its measured direction is the
  degenerate one of SS7: the ridge has no
  measured peak, and its continuation points
  toward the shift-free limit of the family,
  where what remains is a static N/M
  configuration — a different object from the
  shift-carrying configurations the lineage set
  out to design. The lineage progression is now
  −1.942246×10⁻⁴ (379, H2) → −1.757074×10⁻⁴
  (389, mixed) → −1.241372×10⁻⁴ (393, ray point)
  → −6.812653×10⁻⁵ (394) → −2.980985×10⁻⁵ (395)
  → −7.431892×10⁻⁶ (396): the standing level is
  3.83% of its H2 magnitude.

## 5. Incidents (disclosed)

- The traces+grids driver chain's first
  background completion notice reported exit 0
  with a log tail (G2/G3 lines and joint values)
  that DID NOT MATCH THE DISK: the parts files
  then held only RAY3/DIAG and a partial G1, and
  the grid1 process was in fact still running.
  The coordinator trusted the disk over the
  notice, confirmed the live process, and waited
  for the chain's real completion (77 reads:
  RAY3 7, DIAG 8, G1 24, G2 12, G3 26) before
  launching the polishes. No read was lost or
  double-counted — the driver's flush-per-read,
  deduplicated store made the on-disk state the
  true state throughout, and the confirmation's
  diff-0.0 reproduction covers the best point.
  The notice's phantom values appear nowhere in
  the stored record.

## 6. Verdict mapping (registration SS6)

- STATIONARY LEVEL IMPROVES AGAIN: FIRES, with
  the SS7 DEGENERACY NOTE and the box-edge
  disclosure on its face. SET gain over the
  anchor +2.237796×10⁻⁵ > the registered 1×10⁻⁶
  bar, AND the confirmed worst-null beats the
  anchor's by +2.218949×10⁻⁵. New centre, SET
  level, pointwise level, clamped level,
  box-edge distances and the physicality table
  all stated (§3, §4). Gate referral — the gate
  is asked to rule on the degeneracy note as
  part of the claim set.
- THE RIDGE TURNS: does not fire — neither trace
  turns inside the box, the diagonal reaches the
  corner region still rising, and both polishes
  climb past its end to a distinct, higher
  centre.
- COST-BOUNDED: does not fire (336 of 400 reads;
  all stages complete).

## 7. Named follow-ups (not run)

- A Gate for this claim set before any
  publication (the standing route), with the
  SS7 degeneracy note as a charged item: the
  gate should rule whether the centre is
  quotable as a design improvement, or only as
  a scaling-surface level with the degeneracy
  note attached.
- The dwell→harvest cycle at the new centre
  (390's pattern, owed at each new centre by the
  line's own discipline) — with the caveat on
  its face that the centre's profiles have
  drifted far from H2's harvested shape (§4), so
  the harvest's meaning there needs its own
  registration care.
- A fourth widening is NOT named as a plain
  repeat: the ridge has no measured turn and its
  direction is the degenerate one (shift removal
  + N/M growth), so another improvement search
  in a wider box would mostly re-measure the
  drift. If the direction is probed again, the
  honest form is a DEGENERACY PROBE, registered
  as such: the level's behaviour as μ_S → 0
  along the ridge's ratios (does the level
  asymptote to the static N/M configuration's
  level?), with the N/M growth priced against
  the lineage's floors and a full-extent read —
  not another centre hunt.

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
level improves again — progression in §4 — but
under the SS7 degeneracy note: the improvement
is substantially the scaling family walking
toward its shift-free limit, and the drive
content of the winning configuration (peak shift
0.354, against H2's 0.885) has thinned as the
level improved. The wall moved again; it did
not break. Goal 2 (wormhole): untouched. Goal 3
(subluminal record): untouched.

DESK: NO DATA CONTACT.

Artefacts: `phase396/work/p396_registration.md`,
`p396_lib.py`, `p396_controls.py`,
`p396_admission.py`, `p396_search.py`,
`p396_confirm.py`, `p396_clamp.py`,
`p396_anatomy.py`, `p396_physicality.py`;
`phase396/results/p396_controls.json`,
`p396_controls_laptop.json`,
`p396_screens.jsonl` (+ `parts/`),
`p396_search_summary.json`, `p396_anatomy.json`,
`p396_confirmation.json`, `p396_clamp.json`,
`p396_physicality.json`, `p396_memo.md`, control,
search and post-search logs.

Spend: VM wall ≈ 28 min total (controls ≈ 3 min,
search ≈ 24 min across the stage chains,
confirmation + clamp + anatomy + physicality
≈ 1 min); laptop: the admission read only.
