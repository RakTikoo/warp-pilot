# PHASE 405 — W15: CHEAP-SHIFT SHAPES ON THE
STATIC WINNER'S BASE

**VERDICT: SHAPE PAYS — GATE REFERRAL of the
re-introduced claim set. On Phase 400's
corrected static base (N/M verbatim, joint
+1.397719×10⁻⁶ at S ≡ 0), the shift re-introduced
as a FREE SPLINE SHAPE (p341's family, K = 9)
carries the FULL SS7 warp criterion — peak
|β·S| = 0.4426742490267404, half of H2's peak,
at the β = 1.1 pose — at a confirmed joint of
+1.227385×10⁻⁶ (SET-244, band [10, 20], Type-I
fraction 1.0000, exact worst-null at the argmin
+7.282191×10⁻⁷, adversary-polished in-region
NEC +1.214724×10⁻⁶). The free shape spends
1.703×10⁻⁷ of the base's static margin where
Phase 404's fixed shape (H2's S scaled) spends
a measured 1.058×10⁻⁵ at the same amplitude on
the same base — A FACTOR OF ~62 CHEAPER — and
its cost curve is nearly amplitude-flat,
not the fixed shape's ~amplitude^2.16 law.
The fixed shape's break-even on this base was
μ_S* = 0.171875 (peak 0.1522); the free shape's
break-even peak is at or beyond the criterion
(the registered curve tops out there, all
non-negative). NO MEMBER IS CLAIMED: the
configuration is a warp-grade CANDIDATE,
referred to a gate of the re-introduced set
itself; SEC, outside the lineage's joint,
remains −2.213557×10⁻⁴ at the best point; the
pose is the band [10, 20] with 356's caveats.
Gate-48, pending at charge time, has since
ruled the BASE claim set SURVIVES in full
((e) as rider G48-E) — the base fence is
discharged; the gate this verdict refers is
of the re-introduced set.**

Charged at ledger entry 1043 (Rakshit's
direction: "let's get this one moving at ftl
then let's see"). Registration filed before
any computation:
`phase405/work/p405_registration.md` (SS0–SS7).
Frame of record: the VM (the laptop admission
control was run and followed — §2).

## 1. The act

404's question, freed. The assembly is 404's
base with the S slot opened: N/M =
p398_lib.profiles_at398 at 400's winner
verbatim (base (μ_N, μ_M) = (2.330448313835416,
11.343911464156438), K = 17 vN/vM as stored);
S = p341's correction spline (not-a-knot C2
cubic through K knot values uniform on
[10, 20]) on a base S ≡ 0 — the slot 398's
machinery zeroed. The search maximises the
peak |β·S| subject to the joint ≥ 0,
equivalently minimises the NEC cost per unit
peak shift. At each stage's fixed target peak
the walks maximise score = joint − PEN400
(PEN400 = LAM400 × rough(vS), LAM400 =
1.0×10⁻⁵ — 400's rescaled penalty), incumbent
semantics 379's (best score among C1-feasible
screens; the pure joint recorded for every
screen). Five stages: A — the H2-shape
reference curve (the fixed shape spline-
embedded, 8 peaks); B — walks at the
criterion peak (CD sweeps + NM polish);
C — walks at mid peak 0.25; D — cost curves
and break-even bisection for the two stage
shapes; E — K = 17, GATED on the criterion
not being reached at K = 9 (it was reached;
E did not run). 726 stored screens, ZERO
rejected (every screen C1-feasible), of the
1100 cap.

## 2. Controls (VM: ALL PASS) and admission

Record: `phase405/results/p405_controls.json`
(≈ 65 s across two runs).

- CTL-405-WIN: this phase's own assembly at
  vS = 0 (K = 9 and K = 17) reproduces the
  winner at diff 0.0 (five minima, joint,
  worst-null); max |S|, |S′|, |S′′| over the
  SET grid = 0.0 exactly; the frozen base's
  positivity floors hold (positivity_ok398
  at the winner).
- CTL-405-H2S: (1, 1, 1) → L_stat(H2) at
  diff 0.0 (five minima).
- CTL-405-C395: C395 → its stored TG (five
  minima) and worst-null at diff 0.0.
- CTL-405-FIX: the fixed-shape control on
  this base — p404_lib's assembly read in
  this session at μ_S = 0.171875 and 0.5
  reproduces p404_ladder.json's stored rows
  (joint, five minima, peak |β·S|) at diff
  0.0. The fixed shape's achievable peak at
  joint ≥ 0: P_fix = 0.152169273102942.
- CTL-405-ADM: **LAPTOP ADMITTED** — the
  Trace-A endpoint SET read on the pool
  mirror reproduces the VM record at
  roundoff (diffs ≤ 5.5×10⁻¹⁹, argmin radii
  identical — the 398/400/401 admission
  values exactly). Record:
  `p405_controls_laptop.json`. Deciding
  reads are nevertheless all VM reads
  (registration SS2).

## 3. The search (screens; stage bests)

Pure joint levels at each stage's target peak
(SET-244, band [10, 20], C1-feasible screens
only):

| stage | target peak | best joint | note |
|---|---|---|---|
| A seed (H2 shape embedded) | 0.4427 | −9.151429×10⁻⁶ | tracks 404's ladder (≤ 3.5×10⁻⁸) |
| B: walks at the criterion | 0.4427 | +9.733734×10⁻⁹ | crosses zero inside the CD walks; lands on the DEC plateau |
| C: walks at mid peak | 0.2500 | +1.346254×10⁻⁶ | 96% of the static margin retained |
| D: curves | — | see §4 | both shapes all-nonneg to the criterion |

- Stage A's reference curve reproduces 404's
  fixed-shape prices through the spline
  interpolant (at P_fix: +1.435517×10⁻⁸ vs
  404's +1.435278×10⁻⁸; at the criterion:
  −9.151429×10⁻⁶ vs −9.186098×10⁻⁶) — the
  machinery and the comparison are sound
  before any free-shape read is believed.
- Stage B crossed zero at the criterion peak
  inside its CD walks (incumbent
  +9.088×10⁻⁹ by screen 238, +9.734×10⁻⁹
  final, screen 375) — but its shape spends
  the margin doing it (§4).
- Stage C, optimising where a single NEC
  site binds, found the cheap direction:
  at peak 0.25 the joint is +1.346254×10⁻⁶,
  within 5.15×10⁻⁸ of the base's zero-shift
  level.
- Stage D read both shapes' cost curves at
  9 amplitudes each (18 screens, no
  bisection needed — no negative point on
  either curve): P* = the criterion for
  both; the best shape is C by the joint at
  the criterion (+1.227385×10⁻⁶ vs
  +9.734×10⁻⁹).
- Stage E (K = 17) did not run: the
  registered gate (K = 9 best P* < criterion)
  was false.

## 4. The confirmed best shape and its anatomy

Confirmation (`p405_confirmation.json`): the
full re-read at the criterion amplitude
reproduces the stored Stage D screen at diff
0.0. Joint = NEC = DEC min
+1.2273852081052888×10⁻⁶ at
r = 17.926829268292682 (NEC and DEC argmins
coincide); Type-I fraction 1.0000, the Type-I
NEC min identical to the joint; the exact
worst-null at the SET NEC argmin is
+7.282191364112375×10⁻⁷ (positive pointwise);
the adversary polish's in-region worst NEC
is +1.214723699102956×10⁻⁶ at r = 17.792
(positive — the level is not a grid
artefact); ρ_min > 0 throughout (all screens
C1-feasible); SEC min = −2.213556504990559×10⁻⁴
(outside the joint; §7). The stage-amplitude
confirmation (peak 0.25) likewise reproduces
at diff 0.0: joint +1.346253628681937×10⁻⁶,
worst-null +1.0199343192615842×10⁻⁶, polish
+1.327026604141981×10⁻⁶.

Configuration: the winner base verbatim (§1)
plus S = the K = 9 spline through, at the
criterion amplitude, knots (r: value) =
10: 0.402431, 11.25: 0.232376, 12.5: 0.101105,
13.75: 0.030274, 15: 0.021560, 16.25: 0.012972,
17.5: 0.007865, 18.75: 0.003529, 20: −0.000435
(exact digits in p405_confirmation.json).
A MONOTONE FRONT-LOADED RAMP: peak |β·S| at
r = 10.0 (the inner band edge, S = 0.402431),
falling by a factor of ~60 across the band.

COST CURVE of the best shape (Stage D;
confirmed at 0.25 and 0.4427): joint
+1.3960×10⁻⁶ (peak 0.05) → +1.3793×10⁻⁶
(0.1522) → +1.3463×10⁻⁶ (0.25) →
+1.3226×10⁻⁶ (0.30) → +1.2605×10⁻⁶ (0.40) →
+1.2274×10⁻⁶ (0.4427), NEC-bound at
r = 17.93 at every amplitude ≥ 0.10. THE
COST IS NEARLY AMPLITUDE-FLAT: 1.703×10⁻⁷
spent across the whole range to the
criterion, against the fixed shape's
1.058×10⁻⁵ at the criterion alone (404,
measured) — and against 397's law, under
which this base's margin bought μ_S* ≈
0.27–0.28 of the FIXED shape.

ANATOMY: at the binding site (r = 17.927,
the base's fragile region) the shape's
locals are S = 0.006480, S′ = −0.003428,
S′′ = −0.000695 — the shift has essentially
switched itself off where the base is
fragile, and paid its curvature budget at
small radii where the base's margins are
wide (316's anatomy: S′′ carries the NEC
cost of a shift; this shape spends S′′
where it is cheap). The Stage B shape
shows the counterfactual: optimised at the
criterion, it holds shift out to the outer
radii, its DEC argmin migrates to
r = 19.88, and it lands on the same DEC
plateau 404's ladder showed (+1.44×10⁻⁸ at
μ_S ∈ [0.10, 0.172]) — spending the entire
margin to stand at +9.7×10⁻⁹. WHERE YOU
OPTIMISE DECIDES WHAT YOU FIND: the mid-peak
search, under a single clean NEC gradient,
found the direction the criterion-peak
search, fighting two constraints at once,
did not.

## 5. The stakes (registration SS6 bars)

- The SS7 warp criterion: peak |β·S| ≥
  0.4426742490267404 at joint ≥ 0 — MET by
  the confirmed read (peak
  0.44267424902674035, joint
  +1.227385×10⁻⁶).
- The fixed shape's price on this base
  (404, measured): break-even peak 0.1522;
  cost at the criterion 1.058×10⁻⁵. The
  free shape beats the fixed shape's
  achievable peak by a factor of 2.9 and
  its criterion-amplitude cost by a factor
  of ~62.
- 401's prior (a free shape must beat
  A_c ≈ 3.66×10⁻⁵ at binding weights):
  beaten by ~two orders of magnitude — the
  free shape's measured cost at the
  criterion is 1.703×10⁻⁷ total, an
  effective quadratic coefficient of
  8.7×10⁻⁷ per unit peak² against the fixed
  shape's 5.4×10⁻⁵ on this base.
- What the margin buys now: at the
  criterion amplitude the configuration
  still holds +1.227×10⁻⁶ of joint — the
  re-introduction is not a break-even
  scrape but a standing positive level.
  No amplitude beyond the criterion was
  read (the registered curve tops out
  there); the curve's slope at the top
  (−7×10⁻⁷ per unit peak, from the stored
  reads) is recorded as arithmetic on
  stored reads, not as a measurement
  beyond the grid.

## 6. Verdict mapping (registration SS6)

- SHAPE PAYS: FIRES. The confirmed best
  shape has an amplitude (the criterion
  amplitude itself) with peak |β·S| =
  0.44267424902674035 ≥ 0.4426742490267404
  at joint +1.227385×10⁻⁶ ≥ 0, the
  confirmation reproducing the stored
  screen at diff 0.0 with the worst-null
  and the adversary polish both positive.
  GATE REFERRAL of the re-introduced claim
  set (the base's own gate, Gate-48, has
  ruled the base SURVIVES; a gate of the
  re-introduced set is the owed next act).
- SHAPE HELPS BUT SHORT: does not fire —
  the criterion is reached.
- COST-BOUNDED: does not fire (726 of the
  1100-screen cap; the stage pattern
  completed, E gated off by its registered
  condition).

## 7. Named follow-ups (not run)

- THE GATE OF THE RE-INTRODUCED SET (the
  referral this verdict makes): independent
  re-judgement of the criterion-amplitude
  configuration — the winner base plus the
  K = 9 shape at its confirmed vector —
  with the fences of §8 as riders.
- The dwell→harvest cycle at C395 and the
  scaling line's other standing follow-ups
  are unaffected.
- Amplitudes beyond the criterion, a
  K = 17 refinement of the winning shape,
  and any full-extent audit of the
  re-introduced configuration are named
  here as unregistered, unrun directions —
  none is charged by this phase.

## 8. Fences and accounting

Band-posed [10, 20] SET-244 / SAMPLER-M
levels at β = 1.1; 356's full-extent
caveats travel (no full-extent read of the
re-introduced configuration is claimed).
The level is the lineage's joint
min(NEC, DEC); SEC — not part of this
line's level at any point — remains
negative at the best point
(−2.213557×10⁻⁴), and NO EC pass is
claimed by verdict name: a criterion-
amplitude configuration at a positive band
joint is reported as a CANDIDATE with a
gate referral, never presumed a member.
Sampled minima name their frame convention
(SAMPLER-M, the lineage's eulerian_that
association, Gate-43 C-10); the deciding
values are the diff-0.0 control and
confirmation reproductions, the
frame-invariant worst-null and the
adversary polish. Gate-48's ruling on the
base (SURVIVES, rider G48-E) is recorded
in the verdict block; member language
waits for the gate of the re-introduced
set itself.

Goal 1 (FTL drive): the re-introduction
road is walked to its criterion: on the
gate-confirmed static base, a free-shaped
shift at the SS7 warp amplitude stands at
a positive band joint — the first
re-introduced configuration in the
programme to clear the criterion amplitude
at a non-negative joint. The wall did not
break; its price, on this base, turned out
to be a shape question, and the shape is
62× cheaper than the inherited one. What
remains before any drive language:
the gate of this set, the SEC fence, the
full-extent audit, sustainment, transport —
each a named, unrun act. Goal 2
(wormhole): untouched. Goal 3 (subluminal
record): untouched.

DESK: NO DATA CONTACT.

Artefacts: `phase405/work/p405_registration.md`,
`p405_lib.py`, `p405_controls.py`,
`p405_admission.py`, `p405_search.py`,
`p405_search_B_resume.py`, `p405_confirm.py`;
`phase405/results/p405_controls.json`,
`p405_controls_laptop.json`,
`p405_screens.jsonl`, `p405_state.json`,
`p405_search_B.log`, `p405_search_Bresume.log`,
`p405_search_C.log`, `p405_confirmation.json`,
`p405_memo.md`.

INCIDENTS: one, disclosed — a runtime
restart killed Stage B's first process at
308 of its 400 stage screens. The stage was
resumed from the state-file incumbent
(screen 238, joint +9.088×10⁻⁹) under the
stage count restored from the append-only
screens record (the Phase 398 resume
precedent), via p405_search_B_resume.py,
and completed the registered pattern at
exactly 400 stage screens. No screen was
lost, duplicated or re-read out of order;
the incumbent semantics never changed.

Spend: VM wall ≈ 90 min total (controls
≈ 1 min, Stage A ≈ 1 min, Stage B ≈ 50 min
across both processes, Stage C ≈ 28 min,
Stage D ≈ 1.5 min, confirmation ≈ 2 min);
laptop: the admission read only.
