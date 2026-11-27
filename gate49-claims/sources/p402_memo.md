# PHASE 402 MEMO — W19: POSE DRIFT MAP

**VERDICT: POSE PAYS.** Carried to neighbouring
band poses by the registered argument transport,
C395 (the certified design centre) improves
beyond the C-10 band at both widened poses:
[9, 21] by +5.081798×10⁻⁶ on the joint
(worst-null +4.288518×10⁻⁶, same direction) and
[8, 22] by +9.300081×10⁻⁶ (worst-null
+8.215565×10⁻⁶) — the improvement is monotone in
band width over the registered set and has not
turned at the widest registered pose. The static
winner is pose-flat at this grain (every
neighbouring price within 8.9×10⁻⁸ of home, two
orders inside the band). The named successor is
a pose search. Both objects' levels remain
negative at every pose: no energy-condition
pass, no member.

Charged at ledger entry 1037 (W19 of the
W14–W19 intake, entry 1034). Registration filed
before any pose read:
`phase402/work/p402_registration.md` (SS0–SS7,
with Amendment 1 — the JOINT definition
correction, filed after the home controls and
before any neighbouring-pose read).

## The transport (registration SS3)

For pose [a′, b′], W′ = b′ − a′, the affine
argument map φ(r) = 10 + (r − a′)·(10/W′),
λ = 10/W′, carries each stored profile total by
P_pose(r) = P_home(φ(r)), P′_pose = λ·P′_home(φ(r)),
P′′_pose = λ²·P′′_home(φ(r)); β = 1.1 unchanged,
profile values unrescaled. The winner's dN
correction rides inside its N total. Poses:
HOME [10, 20]; translations T−2 [8, 18],
T−1 [9, 19], T+1 [11, 21], T+2 [12, 22];
narrowed N8 [11, 19]; widened W12 [9, 21],
W14 [8, 22]. Read set per (object, pose):
SET-244 (41 midpoints × 162 dirs over the pose)
joint = min(nec, dec), pointwise worst-null at
the SET NEC argmin, DEC, ρ_min, binding sites,
C1 floor (ρ_min > 0 plus the transported totals'
N/M floors on a fine band grid).

## Controls (registration SS2 — all pass)

VM: CTL-402-C395-ORIG (the lineage read at C395
reproduces all five stored minima and the
worst-null −3.0896210095678075×10⁻⁵ at diff 0.0;
Type-I count 4067), CTL-402-C395-POSE (the pose
machinery at home reproduces that read at diff
0.0 on every field), CTL-402-WIN-ORIG (the
winner reproduces −2.5991706000781927×10⁻⁷ at
diff 0.0 on nec/dec/wec, worst-null equal to the
joint, max |S|, |S′|, |S′′| on its assembly
exactly 0.0), CTL-402-WIN-POSE (diff 0.0),
CTL-402-H2 ((1,1,1) → L_stat(H2) at diff 0.0).
Record: `p402_controls.json`.

LAPTOP ADMISSION (CTL-402-ADM): NOT ADMITTED for
the sampled minima — the lineage pattern (cf.
Phase 395's non-admission at NEC diff
1.590×10⁻⁶). The frame-invariant fields agree at
roundoff (dec diff 2.2×10⁻¹⁹, ρ diff 0.0, sec
diff 3.1×10⁻¹⁸) and the Type-I count is exact,
but the sampled NEC/WEC minima drift by
1.61×10⁻⁶ / 1.77×10⁻⁶ with the laptop's NEC
argmin on the sibling shell (r = 15.488 vs the
VM's 15.732) — the Gate-43 C-10 signature, inside
the ±3×10⁻⁶ band. All deciding reads are VM
reads, per the registration. Record:
`p402_controls_laptop.json`.

AMENDMENT 1 (on the record): the home controls
caught SS4's first statement of the JOINT as
min(nec, dec, wec); the lineage's joint is the
pure min(nec, dec) (379's semantics, quoted in
398's checkpoint §1). At C395 all stored minima
reproduce at diff 0.0 and the stored joint
equals the NEC minimum while the WEC minimum
lies below it, which is what decided the
correction. Filed before any pose read; the map
is unaffected.

## The pose-price map

OBJ-C395 — home joint −2.980985×10⁻⁵, home
worst-null −3.089621×10⁻⁵ (band [10, 20],
SET-244 / SAMPLER-M):

| pose | [a′, b′] | λ | joint | Δjoint | worst-null | Δwn | NEC @ r | DEC @ r | ρ_min | C1 |
|---|---|---|---|---|---|---|---|---|---|---|
| HOME | [10, 20] | 1.000 | −2.980985×10⁻⁵ | — | −3.089621×10⁻⁵ | — | −2.981×10⁻⁵ @ 15.732 | −1.777×10⁻⁶ @ 18.659 | +9.781×10⁻⁵ | ok |
| T−2 | [8, 18] | 1.000 | −3.437367×10⁻⁵ | −4.564×10⁻⁶ | −3.689555×10⁻⁵ | −6.000×10⁻⁶ | −3.437×10⁻⁵ @ 13.488 | −1.854×10⁻⁶ @ 16.659 | +1.209×10⁻⁴ | ok |
| T−1 | [9, 19] | 1.000 | −3.193361×10⁻⁵ | −2.124×10⁻⁶ | −3.435047×10⁻⁵ | −3.454×10⁻⁶ | −3.193×10⁻⁵ @ 14.488 | −1.810×10⁻⁶ @ 17.659 | +1.084×10⁻⁴ | ok |
| T+1 | [11, 21] | 1.000 | −2.844843×10⁻⁵ | +1.361×10⁻⁶ | −3.018658×10⁻⁵ | +7.096×10⁻⁷ | −2.845×10⁻⁵ @ 16.488 | −1.753×10⁻⁶ @ 19.659 | +8.866×10⁻⁵ | ok |
| T+2 | [12, 22] | 1.000 | −3.014423×10⁻⁵ | −3.344×10⁻⁷ | −3.022358×10⁻⁵ | +6.726×10⁻⁷ | −3.014×10⁻⁵ @ 14.317 | −1.737×10⁻⁶ @ 20.659 | +8.074×10⁻⁵ | ok |
| N8 | [11, 19] | 1.250 | −9.109264×10⁻⁵ | −6.128×10⁻⁵ | −9.124870×10⁻⁵ | −6.035×10⁻⁵ | −9.109×10⁻⁵ @ 12.854 | −2.698×10⁻⁶ @ 17.927 | +1.082×10⁻⁴ | ok |
| W12 | [9, 21] | 0.833 | **−2.472805×10⁻⁵** | **+5.082×10⁻⁶** | −2.660769×10⁻⁵ | **+4.289×10⁻⁶** | −2.473×10⁻⁵ @ 15.585 | −1.314×10⁻⁶ @ 19.683 | +8.887×10⁻⁵ | ok |
| W14 | [8, 22] | 0.714 | **−2.050977×10⁻⁵** | **+9.300×10⁻⁶** | −2.268065×10⁻⁵ | **+8.216×10⁻⁶** | −2.051×10⁻⁵ @ 15.683 | −1.050×10⁻⁶ @ 20.463 | +8.110×10⁻⁵ | ok |

OBJ-WIN (398's static winner, S ≡ 0) — home
joint −2.599171×10⁻⁷, worst-null identical at
every pose (Type-I fraction 1.000 throughout):

| pose | [a′, b′] | λ | joint | Δjoint | NEC = DEC @ r | ρ_min | C1 |
|---|---|---|---|---|---|---|---|
| HOME | [10, 20] | 1.000 | −2.599171×10⁻⁷ | — | @ 18.902 | +9.950×10⁻⁵ | ok |
| T−2 | [8, 18] | 1.000 | −2.906720×10⁻⁷ | −3.075×10⁻⁸ | @ 16.902 | +1.230×10⁻⁴ | ok |
| T−1 | [9, 19] | 1.000 | −2.744356×10⁻⁷ | −1.452×10⁻⁸ | @ 17.902 | +1.103×10⁻⁴ | ok |
| T+1 | [11, 21] | 1.000 | −2.468575×10⁻⁷ | +1.306×10⁻⁸ | @ 19.902 | +9.020×10⁻⁵ | ok |
| T+2 | [12, 22] | 1.000 | −2.350475×10⁻⁷ | +2.487×10⁻⁸ | @ 20.902 | +8.214×10⁻⁵ | ok |
| N8 | [11, 19] | 1.250 | −3.388892×10⁻⁷ | −7.897×10⁻⁸ | @ 18.122 | +1.100×10⁻⁴ | ok |
| W12 | [9, 21] | 0.833 | −2.080088×10⁻⁷ | +5.191×10⁻⁸ | @ 19.683 | +9.041×10⁻⁵ | ok |
| W14 | [8, 22] | 0.714 | −1.714930×10⁻⁷ | +8.842×10⁻⁸ | @ 20.463 | +8.250×10⁻⁵ | ok |

## Anatomy of the map

- THE LEVER IS WIDTH, NOT POSITION. At fixed
  width 10, translations move C395's joint by
  at most +1.361×10⁻⁶ (inside the band) in the
  improving direction and worsen it beyond the
  band only at T−2. At fixed centre 15, the
  width sequence 8 → 10 → 12 → 14 reads
  −9.109×10⁻⁵ → −2.981×10⁻⁵ → −2.473×10⁻⁵ →
  −2.051×10⁻⁵: narrowing is heavily punished,
  widening pays monotonically, and the trend
  has NOT turned at the widest registered pose
  — the map's edge is still rising, the same
  disclosure pattern as the scaling line's box
  edges (394/395).
- THE IMPROVEMENT IS CONFIRMED AT POINTWISE
  GRADE: at both paying poses the exact
  worst-null at the argmin improves in the same
  direction (+4.289×10⁻⁶ / +8.216×10⁻⁶), inside
  no disagreement flag; the joint remains
  purely NEC-bound (DEC sits at −1.314×10⁻⁶ /
  −1.050×10⁻⁶ at W12/W14, an order above NEC).
- THE WINNER'S SITE TRACKS THE TRANSPORT
  EXACTLY: its binding radius at every pose is
  φ⁻¹(18.902) to the printed digit (16.902,
  17.902, 19.902, 20.902 under translation;
  18.122, 19.683, 20.463 under rescaling) — the
  static residual is carried rigidly by the
  argument map, and its price moves only at the
  10⁻⁸ scale. The same width-monotone direction
  exists for the winner (W14 its best row) but
  two orders below the band: at the static
  floor's magnitude the pose is not a lever.
- FLOORS: every row of both objects is
  C1-feasible (ρ_min > 0) and floor-feasible;
  the transported totals' N/M band minima are
  pose-independent (C395: N 1.832, M 1.610; WIN:
  N 2.745, M 2.494), as they must be — the
  transport rescales no profile value, so the
  band extrema of the values are the home
  extrema. An internal consistency signal, on
  the record.

## Verdict mapping (registration SS5)

- POSE PAYS: FIRES. W12 and W14 improve C395's
  joint by +5.081798×10⁻⁶ and +9.300081×10⁻⁶,
  both more than the +3×10⁻⁶ band, both with
  the worst-null improving alongside (no
  disagreement flag). NAMED SUCCESSOR: a pose
  search — an optimisation over the pose (the
  width direction first, since the registered
  trend is monotone and unturned at W14, with
  the scaling re-optimised at the new pose) —
  charged separately; not run here.
- POSE FLAT: does not fire for C395 (it is the
  correct description of OBJ-WIN's map, whose
  every price is within the band).
- COST-BOUNDED: does not fire (the full
  8-pose × 2-object map is complete).

## Fences

Every row is a BAND read over its pose under
SS3's transport — not a full-extent
re-derivation (Phase 356): no transported
object has been re-closed over [10, 60], the
home objects' full-extent restatements stand
untouched, and no row may be quoted as a
full-extent level. A pose search that finds a
new centre will owe its own full-extent audit
and end-clamp read before quotation, as every
centre in the line has. Sampled minima name
their frame convention (SAMPLER-M, the
lineage's eulerian_that association, Gate-43
C-10); the deciding values are the diff-0.0
control reproductions and the frame-invariant
worst-nulls at named points. No EC pass (every
level negative); no member; no sustainment,
front or transport content.

Goal 1 (FTL drive): the pressure wall's price
is pose-dependent in the width direction —
widening the band pose from 10 to 14 buys
+9.3×10⁻⁶ at C395 with the trend unturned, a
new lever the scaling line never priced. The
wall did not break; its cheapest known
direction now includes the pose. Goal 2
(wormhole): untouched. Goal 3 (subluminal
record): untouched.

DESK: NO DATA CONTACT.

Artefacts: `phase402/work/p402_registration.md`
(+ Amendment 1), `p402_lib.py`,
`p402_controls.py`, `p402_admission.py`,
`p402_map.py`; `phase402/results/
p402_controls.json`, `p402_controls_laptop.json`,
`p402_map.json`, `p402_map.log`, `p402_memo.md`.

Spend: VM wall ≈ 2.5 min total (controls 44 s,
map 96 s); laptop: the admission read only
(plus the mirror sync of phase394/396/397/398/
402 work dirs it required).
