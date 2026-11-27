# PHASE 400 — THE INCUMBENT-CENTRED STATIC SEARCH

**VERDICT: STATIC FLOOR RAISES AGAIN — AND THE
CONFIRMED STATIC LEVEL IS ≥ 0: +1.397719×10⁻⁶
(SET-244, band [10, 20]). Centred on Phase 398's
incumbent, with 341's roughness penalty rescaled
to the 10⁻⁷ level scale (LAM400 = 1.0×10⁻⁵,
registered in SS4 before searching) and the dip
family widened, the penalised walks themselves —
not probe screens — walked the static floor from
the anchor's −2.599171×10⁻⁷ through zero to a
confirmed joint of +1.3977194851281464×10⁻⁶
(NEC = DEC = WEC at the argmin, Type-I fraction
1.0000, exact worst-null at the SET NEC argmin
identical to the joint, adversary-polished
in-region depth +1.376183×10⁻⁶, S identically
zero on the winner's own assembly). The margin
over the anchor is +1.657637×10⁻⁶; over 397's
endpoint, +2.056427×10⁻⁶. Per registration SS6
the ≥ 0 clauses FIRE: GATE REFERRAL, and the
small-shift re-introduction read is the named
immediate successor. THE STAKES, ON THE FACE:
the static margin m = +1.397719×10⁻⁶ buys back
the shift, under 397's carried law fitted on the
endpoints' UNCORRECTED bases, only to a
break-even μ_S* = 0.271 (Trace-A law) / 0.282
(Trace-B) — BELOW the SS7 warp criterion
(μ_S* ≥ 0.5); the shortfall to the required
margin m_req is 3.821957×10⁻⁶ (A) /
3.405489×10⁻⁶ (B). No member is claimed: the
object is static (S ≡ 0), the level is the
lineage's joint min(NEC, DEC) (SEC, outside the
joint, remains −2.050292×10⁻⁴), the pose is the
band [10, 20] with 356's caveats, and the member
question belongs to the re-introduction
successor, which will MEASURE the break-even on
this corrected base rather than estimate it from
the fitted law.**

Charged at ledger entry 1030. Registration filed
before any computation:
`phase400/work/p400_registration.md` (SS0–SS7).
Frame of record: the VM (the laptop admission
control was run and followed — §2).

## 1. The act

398's search, re-centred. The assembly is 398's
verbatim (p398_lib.profiles_at398: H2's totals,
S sector absent, N/M = a base's scaled totals
plus 341's additive correction splines in
(vN, vM) only — no vS exists in the machinery).
The seed is 398's confirmed winner (the ANCHOR:
base (μ_N, μ_M) = (2.386698313835416,
11.968911464156438), K = 9, vN knot 6 (r = 17.5)
at −0.02, vM = 0, level −2.599171×10⁻⁷). The two
registered changes: (1) the objective's
roughness penalty is PEN400, LAM400 = 1.0×10⁻⁵
= LAM_REG × 10⁻³ exactly — under it the
incumbent's own dip costs 2.4×10⁻⁸ (0.092 ×
|L_ANCHOR|) instead of 341's 2.400000×10⁻⁵
(92 × |L_ANCHOR|); the incumbent semantics are
379's (pure min(nec, dec) among C1-feasible
screens), as in 398. (2) The dip family widened
(Stage B) and dM retested under the rescaled
penalty (Stage D). Five stages, one centre:
A — K = 9 CD sweeps (steps 0.02, 0.008, 0.003)
+ NM from the incumbent vector; B — the
registered dip screens; C — K = 17 refinement
warm-started from Stage A's end vector (the
registered seed rule picked it by pure joint
over the anchor and Stage B's best); D — the
dM retest (vM-only NM, vM single-knot probes,
a joint CD pass); E — a (μ_N, μ_M) scaling
micro-polish with the best vector frozen.
981 stored screens (A 328, B 22, C 432, D 182,
E 17; cap 1100 not binding), ZERO rejected,
every screen C1-feasible and floor-feasible,
every candidate read at S ≡ 0 by construction.

## 2. Controls (VM: ALL PASS) and admission

Record: `phase400/results/p400_controls.json`
(76.5 s).

- CTL-400-A / CTL-400-B: the endpoints read on
  the lineage scaling machinery reproduce 397's
  stored values at diff 0.0 (all five minima),
  and their exact worst-nulls reproduce
  −6.587071568730905×10⁻⁷ (A) /
  −7.229718758606569×10⁻⁷ (B) at diff 0.0.
- CTL-400-ZERO-A/B: 398's assembly at zero
  corrections reproduces both endpoint reads at
  diff 0.0, and its S output is identically zero
  (max |S|, |S′|, |S′′| over the SET grid = 0.0
  exactly, both endpoints).
- CTL-400-ANCHOR: the anchor reproduces 398's
  confirmation at diff 0.0 (all five minima),
  its exact worst-null reproduces
  −2.5991706000781927×10⁻⁷ at diff 0.0, and the
  S ≡ 0 assertion holds on its assembly
  (max |S|, |S′|, |S′′| = 0.0 exactly).
- CTL-400-PEN: the penalty arithmetic on the
  incumbent's stored vector: 341's penalty2 =
  2.4000000000000004×10⁻⁵ (diff 3.4×10⁻²¹ from
  the 2.400000×10⁻⁵ identity); PEN400 =
  2.4000000000000003×10⁻⁸ (diff 3.3×10⁻²⁴);
  rough(vN_inc) = 0.0024 (diff 4.3×10⁻¹⁹);
  LAM400 = LAM_REG × 10⁻³ holds exactly.
- CTL-400-H2S: (1, 1, 1) → L_stat(H2) at diff
  0.0 (five minima + polished depth).
- CTL-400-C395: C395 → its stored values at
  diff 0.0 (five minima, depth, worst-null).
- Floors hold at both endpoints and at the
  anchor.

**Frame admission: LAPTOP ADMITTED — the third
admission in the lineage.** The Trace-A endpoint
SET read on the pool mirror reproduces the VM's
stored read at roundoff (max diff 5.5×10⁻¹⁹,
both argmin radii identical — the diffs are
398's admission diffs exactly). Record:
`p400_controls_laptop.json`. Per registration
SS2 and the 397/398 precedent, the deciding
reads are nevertheless all VM reads — the search
compares levels at 10⁻⁷–10⁻⁹ increment scale,
where one frame must carry every point. No
deciding read depends on the laptop.

## 3. The search (screens; stage bests)

Pure joint levels (SET-244, band [10, 20],
C1-feasible screens only), best per stage:

| stage | best pure joint | note |
|---|---|---|
| anchor (start) | −2.599171×10⁻⁷ | 398's winner, re-screened at diff 0.0 |
| A: K = 9 centred walks | **+1.230765×10⁻⁶** | zero crossed inside CD step 0.003 |
| B: dip family | +1.123691×10⁻⁷ | single knot-6 dip at −0.05, nothing else |
| C: K = 17 refinement | +1.308679×10⁻⁶ | seeded from A's end vector |
| D: dM retest | +1.311540×10⁻⁶ | +2.86×10⁻⁹ over C (the joint CD pass) |
| E: scaling micro-polish | **+1.397719×10⁻⁶** | base moved: (μ_N, μ_M) → (2.330448, 11.343911) |

- THE CROSSING HAPPENED IN THE WALKS: by screen
  200 of Stage A's CD (step 0.003), the
  incumbent already stood at +9.219393×10⁻⁷ —
  the CD had deepened the dip (knot 6:
  −0.02 → −0.062) and shaped its neighbours
  (knots 3–5 positive, knot 8 at +0.062). Under
  341's pricing every one of those screens
  would have ranked ~10⁻⁵ BELOW the walks'
  start; under PEN400 the walks followed the
  mechanism up. Stage A's NM end:
  +1.230765×10⁻⁶.
- THE DIP RESPONSE (Stage B, the single knot-6
  dip alone on the anchor base) is a clean
  single-peaked curve: −0.01 → −4.248977×10⁻⁷;
  −0.02 (the anchor) → −2.599171×10⁻⁷; −0.03 →
  −9.511134×10⁻⁸; −0.04 → +6.951970×10⁻⁸;
  −0.05 → +1.123691×10⁻⁷ (the peak); −0.06 →
  −9.910×10⁻⁸; −0.08 → −5.212×10⁻⁷; −0.10 →
  −9.423×10⁻⁷; −0.14 → −1.781×10⁻⁶; −0.18 →
  −2.616×10⁻⁶. The single dip crosses zero
  between −0.03 and −0.04, peaks at −0.05, and
  the binding site migrates outward
  (r = 18.902 → 19.878) past −0.04: deepening
  the dip past its peak exports the binding
  site to the dip's outer flank. The shaped
  multi-knot correction reaches 12× the
  single-dip peak — the dip is the mechanism,
  but its exploitation is a shaped N′′
  reduction across r ≈ 16–19, not a deeper
  single spike.
- STAGE D (the dM retest under PEN400): the
  vM-only NM (80 fev) and the 34 vM single-knot
  probes bought nothing on their own; the
  stage's +2.86×10⁻⁹ came from the final joint
  CD pass. The ablations (§4) settle the
  retest: 398's dM-inertness is CONFIRMED under
  the rescaled pricing, at a positive level.
- STAGE E moved the base scalings jointly with
  the frozen K = 17 correction: μ_N
  2.386698 → 2.330448, μ_M 11.968911 →
  11.343911, for +8.618×10⁻⁸ — the anchor base
  was not a static optimum in the scalings once
  the correction was shaped (398's Stage 0 had
  polished the scalings only at zero
  corrections, from the endpoint).

## 4. The confirmed winner and its anatomy

Confirmation (`p400_confirmation.json`): the
full re-read reproduces the stored screen minima
at diff 0.0 (all five). Joint = NEC = DEC =
WEC = +1.3977194851281464×10⁻⁶ at
r = 17.682926829268293, Type-I fraction 1.0000;
the exact worst-null at the SET NEC argmin is
+1.3977194851281464×10⁻⁶ — identical to the
joint, as at the endpoints and the anchor; the
adversary polish's depth is
+1.3761826591108812×10⁻⁶ (the in-region
pointwise floor at the site region is also
positive — the level is not a grid artefact).
The S ≡ 0 assertion is verified on the winner's
own assembly: max |S|, |S′|, |S′′| over the SET
grid = 0.0 exactly. ρ_min = +9.943381×10⁻⁵.
SEC min = −2.050292×10⁻⁴ (outside the joint;
see the verdict's fence).

Configuration: base (μ_N, μ_M) =
(2.330448313835416, 11.343911464156438), K = 17,
vN = (0.001381, 0.000812, −0.000691, −0.001566,
−0.000288, 0.000715, 0.007948, 0.016847,
0.028143, 0.027377, −0.002470, −0.041671,
−0.070700, −0.058496, −0.000867, 0.062507,
0.096563), vM = (−0.000084, −0.000030, −0.000078,
−0.000127, −0.000024, 0.000188, 0.000047,
−0.000734, −0.001339, −0.000685, −0.050028,
0.000012, −0.000391, −0.002331, −0.000595,
−0.000191, 0.000658). The K = 17 dip sits at
knots 11–13 (radii ≈ 16.8–18.2) — the refinement
of the anchor's K = 9 knot-6 dip at r = 17.5.

ANATOMY (`p400_anatomy.json`): the binding site
MOVED inward, r = 18.902 → 17.682926829268293 —
onto the dip's own support. There the Eulerian
tensor is Type-I with eigenvalues
(−1.262622×10⁻⁴, +1.101974×10⁻⁵, +1.101974×10⁻⁵,
+1.276599×10⁻⁴) and ρ = +1.276599×10⁻⁴: the
ρ + p_r gap that was −2.599171×10⁻⁷ at the
anchor is +1.397719×10⁻⁶ here — the radial
pressure now sits CLOSER to zero than the
density sits above it (p_r = −1.262622×10⁻⁴
against ρ = +1.276599×10⁻⁴), and the tangential
pair is degenerate and positive. Locals at the
site: N = 2.794857, N′ = −0.033311,
N′′ = +0.064049; M = 74.653304, M′ = +5.241431,
M′′ = −3.736971. ABLATIONS at the winner's
base: dN only → +1.397250×10⁻⁶ (99.97% of the
level; the gain is the N correction, as in
398); dM only → −6.222083×10⁻⁷; zero
corrections → −6.224934×10⁻⁷ (the winner's
base's own static level). dM's whole
contribution in context is the cooperative
remainder, +4.69×10⁻¹⁰. The static floor is an
N′′-sector quantity at one site — 316's anatomy
holding at the ridge's residue — and its
remedy, within this machinery, is the shaped
local N′′ reduction the walks built once the
penalty stopped forbidding it.

## 5. The stakes (registration SS5)

`p400_stakes.json`. The confirmed static level
L_new = +1.397719×10⁻⁶ is POSITIVE, so a
break-even shift exists under 397's carried law
|L(μ_S) − L_static| = A_c·μ_S^p: μ_S* =
(m / A_c)^(1/p) with m = L_new gives
μ_S* = 0.271335 (Trace-A coefficients) /
0.282108 (Trace-B). The SS7 warp criterion
requires μ_S* ≥ 0.5: NOT CLEARED under either
law. The margin a warp-grade re-introduction
would require, m_req = A_c·0.5^p, is
5.219677×10⁻⁶ (A) / 4.803209×10⁻⁶ (B); the
shortfall to m_req is 3.821957×10⁻⁶ /
3.405489×10⁻⁶ — the floor stands above zero by
about a quarter of the required margin. The
caveat of SS5 stands, and matters more now: the
carried law was fitted along the ridge on the
endpoints' uncorrected bases; on this corrected
base the coefficient may differ, so the
break-even is the law's estimate, not a
measurement. The direct measurement is the
small-shift re-introduction read named as the
immediate successor (SS6).

## 6. Verdict mapping (registration SS6)

- STATIC FLOOR RAISES AGAIN: FIRES. The
  confirmed joint +1.3977194851281464×10⁻⁶
  exceeds the anchor bar L_ANCHOR =
  −2.5991706000781927×10⁻⁷ by +1.657637×10⁻⁶ >
  the registered 1×10⁻⁹, and the confirmation's
  worst-null (+1.3977194851281464×10⁻⁶) likewise
  exceeds the anchor's worst-null. The level is
  ≥ 0, so the registered clauses trigger: GATE
  REFERRAL, and the small-shift re-introduction
  read is the named immediate successor (not
  run here).
- STATIC FLOOR STUCK: does not fire — the floor
  moved through zero in the walks themselves.
- COST-BOUNDED: does not fire (the full pattern
  completed at 981 of the 1100-screen cap).

## 7. Named follow-ups (not run)

- THE SMALL-SHIFT RE-INTRODUCTION READ (the
  immediate successor, named by SS6 at ≥ 0):
  on the winner's corrected base, re-introduce
  the shift at small μ_S and MEASURE the
  level's carried cost directly — replacing
  397's fitted-law break-even (μ_S* ≈ 0.27–0.28
  on the uncorrected bases' law) with a
  measurement on this base, and reading the
  configuration against the SS7 warp criterion
  (peak |β·S| ≥ ½ H2's) as μ_S grows.
- The dwell→harvest cycle at C395 (390's
  pattern) remains the scaling line's standing
  follow-up, unaffected by this phase.
- Whether the raised (now positive) static
  floor is quotable is the referred gate's
  question; this phase makes the referral and
  no quotation of its own beyond the memo's
  fenced wording.

## 8. Fences and accounting

S ≡ 0 throughout, by construction (no vS exists
in the machinery) and asserted on the winner
(§4). Band-posed [10, 20] SET-244 / SAMPLER-M
levels; 356's full-extent caveats travel (no
full-extent read of any static candidate is
claimed; floors are the lineage's FINE_R
floors, held at all 981 screens). The level is
the lineage's joint min(NEC, DEC); SEC — not
part of this line's level at any point (the
endpoints' SEC was −2.2×10⁻⁴) — remains
negative at the winner (−2.050292×10⁻⁴), and NO
EC pass is claimed by verdict name: a static
level ≥ 0 is reported as a level, with the
stakes computation, never presumed a member —
the object at S = 0 has no drive content
whatever its level, and the member question
belongs to the re-introduction successor.
Sampled minima name their frame convention
(SAMPLER-M, the lineage's eulerian_that
association, Gate-43 C-10); the deciding values
are the diff-0.0 control and confirmation
reproductions and the frame-invariant
worst-null.

Goal 1 (FTL drive): the static residue of the
scaling family is closed — its floor, attacked
at zero shift with the penalty priced at the
level's own scale, stands POSITIVE at
+1.398×10⁻⁶, and the road it guards is priced
end-to-end: under the fitted carried law the
margin pays for a shift only to μ_S* ≈
0.27–0.28, short of the 0.5 warp criterion, with
the direct measurement named as the successor.
The wall did not break; its last residue changed
sign, and what remains is a measured question
about the shift's price on a corrected base.
Goal 2 (wormhole): untouched. Goal 3
(subluminal record): untouched.

DESK: NO DATA CONTACT.

Artefacts: `phase400/work/p400_registration.md`,
`p400_lib.py`, `p400_controls.py`,
`p400_admission.py`, `p400_search.py`,
`p400_confirm.py`; `phase400/results/
p400_controls.json`, `p400_controls_laptop.json`,
`p400_screens.jsonl`, `p400_state.json`,
`p400_search.log`, `p400_confirmation.json`,
`p400_anatomy.json`, `p400_stakes.json`,
`p400_memo.md`.

INCIDENTS: none in the computation. (The
launching shell's output stream timed out on
drain — a harness artefact; the detached search
process ran clean in one pass, all five stages,
no restart, no lost or duplicated screen: 981
stored screens, zero rejected.)

Spend: VM wall ≈ 85 min total (controls ≈
1.5 min, search ≈ 82 min of which ≈ 55 min is
screen read time, confirmation + anatomy +
stakes ≈ 1 min); laptop: the admission read
only.
