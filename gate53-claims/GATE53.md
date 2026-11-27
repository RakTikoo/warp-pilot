# GATE-53 — INDEPENDENT RE-JUDGEMENT OF THE PHASE 408 CLAIM SET

**Charge:** ledger entry 1086 (FU-P408-1). **Frame:** VM frame of
record; deciding reads on the VM. The laptop was run as an
admission control (§1) and is admitted as a corroborating
instrument for the deciding eigenvalue reads only. **Machinery:**
fresh gate machinery only — `gate53/work/g53_lib.py`, written for
this gate in the gate-lineage builder pattern of Gates 42/44/51
(the graded-family builder generalised to grading bases of
n_c ∈ {8, 12, 16}), with the box-4 stages 2–4 evaluated by the
spline-antiderivative scheme (a different numerical organisation
from the phase's cumulative-trapezoid + Hermite scheme; the phase
scheme is carried alongside as an internal cross-check). Tensor
instruments gate6/wa_auditor.py and phase50/p503_lib.audit4, the
registered pair. Nothing was imported from phase408/work,
phase392/work, phase391/work or phase386/work. Stored bytes
verified by hash before any audit. float64 everywhere.

**The registered bars, applied as written** (CHECKPOINT386 §2,
inherited verbatim by CHECKPOINT391/392/408): on the primary wa
audit at BOTH spacings (h = 0.0375, 0.01875), registered set
pts_1020_control (1,430 rows) — Type-I fraction = 1.000 over
significant points; worst NEC/WEC/SEC/DEC margins > 0,
sign-stable, worst ≥ 3× the measured FD floor; shell
sampled-null NEC min > 0 — **and audit4 agreement on the sign of
every deciding margin** (the four eigenvalue EC minima). Per
Gate-44 §1 C-1, audit4's own Type-I fraction and
direction-sampled diagnostics are recorded as diagnostics, not
bars.

**The gate's own additions** (charged at entry 1086, first
question): the deciding reads on A-6 were additionally taken on
a spacing ladder finer than the registered pair (h = 0.009375,
0.0046875) with the FD floor proxy measured at every rung and a
Richardson h → 0 extrapolation of the deciding margin; and a
dense radial sampling (radii 2.6–10.6, step 0.05, the registered
26 directions, h = 0.009375) was run on A-6 and, for context, on
the lineage controls RW-5, E2-1, y_his and on B-2.

## Verdict summary

| Claim | Ruling |
|---|---|
| (a) A-6 legal at β = 0.193359375; failure bracket [0.193359375, 0.195859375] | **SURVIVES AS FENCED** (riders G53-R1 thin margin, G53-R2 registered-set scope — §2) |
| (b) Arm B control: the clipped seed home-verifies at exactly RW-5's ceiling 0.192578125 with RW-5's bracket — the embedding is lossless | **SURVIVES** (in the registered-bars sense the phase claimed; §3) |
| (c) Amendment A-408-1's handling keeps the Arm B record quotable | **SURVIVES AS FENCED** (quotable only in the amended form, rider G53-R3 — §4) |
| (d) The ladder statement: time spent; modes paid once finished; 12-mode widening spent; combination unproven, not refuted; increments +0.0008/+0.0008, ceiling margin thinned ~17× | **SURVIVES RESTATED** (two precision restatements — §5) |
| Controls: y_his at 0.1363 (legal) and 0.1364 (fails); E2-1 legal at 0.191796875; RW-5 legal at 0.192578125, failing at 0.195078125 | **SURVIVE with calibration note C-1** (the 0.1364 half is a screening-rating statement, not a pointwise failure on either instrument — §1, §6) |

The quotable set is §7 (G53-A…G53-E). The fence is carried
verbatim in G53-B: **graded-category wording only — this set
never contests the step-profile category (Procaccia's 0.1363
stands there; the programme's verified best there remains
0.10).**

## §1 Machinery and calibrations

**C-0 · Stored bytes (hash gate).** Every audited vector was
re-hashed (sha256 of the float64 tobytes) against its stored
record before auditing: A-6 `6461827f…c00039` ✓, B-2 / clipped
seed `d228c82e…5d69f` ✓, unclipped embedding `a0201be1…0d374`
✓, RW-5 `44719b50…35c2` ✓, E2-1 `61679383…73066` ✓. B-2's
stored subject vector is byte-identical to the amendment
record's clipped vector. Full hashes in
`gate53/results/g53_records.json`.

**C-0b · The gate builder reproduces the constructions.**
Chain reads on gate machinery vs the stored records: RW-5
ρ_max 3.240335264325754×10⁻⁴ class, λ 0.8999655940391417 class,
k 0.02367465973823105 class — all reproduced at relative
differences ≤ 1.1×10⁻¹¹ (the residual is the box-4 stage
scheme's, measured directly: the gate's two internal schemes
differ by ≤ 7.6×10⁻¹² absolute in λ, ≤ 2.5×10⁻¹³ in k); A-6,
B-2, E2-1 chain reads reproduce at the same level (M to
≤ 1.5×10⁻¹⁵ relative). The c = 0 member's density profile
matches the closed-form box-4 step response to 2.05×10⁻¹¹
(max, max-normalised). Construction grid 1,200,707 points.

**C-1 · Calibration note — the y_his 0.1364 control (read
before §6).** The charged control pair "(0.1363 legal, 0.1364
fails)" is, in the Gate-42 record this gate calibrates
against, a statement of two different instruments: the verdict
audit at 0.1363 (the calibration digit) and the FD screen's
β_crit rating. On this gate's machinery the verdict audit
finds y_his **still legal at 0.1364** (worst SEC
+3.3866486242770997×10⁻⁷ @ r = 5.0, 109.0× floor, Type-I
1.000 at both spacings, second path agreeing — Gate-51's
pointwise digit +3.386648×10⁻⁷ reproduced to eight
significant figures). "Fails at 0.1364" survives **only** in
the rating sense of Gate-51 §1 C-1 (β_crit(y_his) =
0.136328125 on the screen, so 0.1364 lies on the bracket's
failing side). No claim (a)–(d) turns on 0.1364; the
calibration digit at 0.1363 is reproduced (gate
+3.4041777787759174×10⁻⁷ vs stored +3.404177799426875×10⁻⁷).

**C-2 · Direction-sampled diagnostics are subordinate.**
A-6's shell sampled-NEC minimum at its legal rung reads
+1.334×10⁻⁷ (phase), +1.414×10⁻⁷ (this gate, VM), +2.268×10⁻⁷
(this gate, laptop) — all positive, the bar met on every
instrument, the value itself moving at the first-digit level
between samplings. q_max likewise (0.9934 gate / 0.9938 phase
for A-6; 0.9898–0.9934 across subjects). This is the Gate-44
§1 / Gate-51 §1 C-2 pattern: direction-sampled quantities are
C-10 (Gate-43) sampling-convention territory; no ruling in
this gate turns on one. Every deciding (eigenvalue) margin
agrees across instruments to ≤ 1.4×10⁻¹².

**Laptop admission control.** The gate's builder + wa
instrument were run on the laptop pool (venv numpy 2.5.5 /
scipy 1.18.1, the frame of record) as a corroborating read of
A-6 at its legal rung, h = 0.0375: deciding SEC margin
+3.612965823764544×10⁻⁸ vs the VM's +3.6129700650270704×10⁻⁸
(agreement 4.2×10⁻¹⁴), chain reads agreeing to ≤ 2×10⁻¹⁵,
floor proxy identical class (5.2958×10⁻⁹). **The laptop is
admitted as a corroborating instrument for the deciding
eigenvalue reads of this gate; all deciding reads reported
below are the VM's.** (Direction-sampled diagnostics do not
agree across machines — C-2 — and are not admitted.)

**Machinery note (disclosed).** The builder's exterior-branch
line emits a benign RuntimeWarning (log of a negative argument
inside a `np.where` branch whose values are discarded by that
same where) — inherited from the gate-lineage pattern; all
chain reads reproduce stored digits (C-0b), so it touches no
read. The gate's first Richardson pass (in `g53_thin.py`)
used the wrong-direction extrapolation formula; its printed
values were discarded, and the corrected limits were
recomputed from the stored ladder in `g53_dense.py` (§2). No
audit read was affected.

## §2 Claim (a) — A-6's legality and the thin margin: SURVIVES AS FENCED

A-6 (16-mode lineage, Arm A original box, sha256 `6461827f…`),
full registered bars on gate machinery, registered set, both
spacings:

- **β = 0.193359375: LEGAL.** wa worst margin SEC
  **+3.612970×10⁻⁸ @ r = 5.0** (phase stored +3.612960×10⁻⁸;
  agreement 1.0×10⁻¹²), **6.82× FD floor**, Type-I 1.000 at
  both spacings (fine spacing worst +2.909530×10⁻⁸); per-EC
  minima NEC/WEC/DEC +6.817×10⁻⁷ @ 3.75, SEC +3.613×10⁻⁸;
  shell sampled-NEC +1.414×10⁻⁷ > 0 (C-2); audit4 worst
  **+2.674508×10⁻⁸** (h = 0.0375) / +2.674595×10⁻⁸
  (h = 0.01875), all four deciding margins positive at both
  spacings — sign agreement met. Sole bound-sitter verified
  from the stored vector: c idx 0 = +2.25, every other
  coordinate strictly inside the Arm A box. q_max 0.9934
  @ r = 23.0 (< 1; diagnostic, C-2).
- **β = 0.195859375: FAILS — SEC-set, as charged.** wa worst
  SEC **−1.256969×10⁻⁵ @ r = 9.75** (stored −1.256969×10⁻⁵),
  Type-I fraction 0.98499, audit4 SEC −1.258116×10⁻⁵ — a
  plain SEC wall, not Type-I-only. The bracket
  [0.193359375, 0.195859375] is confirmed.

**The FD-floor question (the charge's first question).**
The gate's spacing ladder at the legal rung (registered set,
wa): SEC minimum +3.612970×10⁻⁸ (h = 0.0375) →
+2.909530×10⁻⁸ (0.01875) → +2.733434×10⁻⁸ (0.009375) →
+2.689501×10⁻⁸ (0.0046875), at r = 5.0 at every rung,
Type-I 1.000 throughout. The floor proxy is ~5.0–5.3×10⁻⁹
at every spacing (it is spline-representation noise at
non-significant points, not FD truncation, and does not
fall with h). Richardson extrapolation of the margin
(2nd-order instrument, M(h) = M₀ + Ch²) from the three
successive pairs gives M₀ = +2.675049×10⁻⁸, +2.674735×10⁻⁸,
+2.674856×10⁻⁸ — three limits agreeing to 3.2×10⁻¹¹ — and
the 4th-order second path reads +2.6745×10⁻⁸ independently.
**The deciding margin is a converged property of the
configuration, +2.675×10⁻⁸ in the h → 0 limit — 5.4× the
gate's floor at the finest spacing, above the registered
3× bar at every spacing (6.82× / 5.71× / 5.44× / 5.38×) —
not an FD artefact.** It is, as charged, the thinnest
deciding margin of the lineage's raises (RW-5: 106.5×;
E2-1: 13.4×), and its thinness is carried onto the quotable
set as rider G53-R1.

**The radial-sampling scope (the gate's own finding).**
The registered set's inner-ramp shells sit at radii
3, 4, 5, 6, … — and A-6's SEC profile is tangent to zero
almost exactly at the r = 5.0 shell (direction-minimum
+9.04×10⁻⁷ @ 4.8, +2.73×10⁻⁸ @ 5.0). On the gate's denser
radial sampling (step 0.05, same 26 directions,
h = 0.009375) the profile continues down: **SEC minimum
−1.257492×10⁻⁶ @ r = 5.42**, negative over r ∈ [5.02, 5.84],
recovering to +2.13×10⁻⁶ @ 6.2. The dip point is Type-I
with NEC/WEC/DEC +6.08×10⁻⁶ and sampled-NEC +1.57×10⁻⁶;
its SEC value converges across both instruments and all
spacings (wa −1.2378×10⁻⁶ → −1.2536×10⁻⁶ over the ladder;
audit4 −1.253882×10⁻⁶ at both spacings) — a genuine
continuum SEC dip between the registered shells, ≈47×
deeper than the converged registered margin is high. **A-6 is not
SEC-legal in the radial continuum at β = 0.193359375; its
legality is a statement on the registered set under the
Gate-42 bars — as, this gate records, is every verdict in
this lineage.** The scope is not A-6's alone: under the
identical densification, RW-5 stays SEC-positive
(+2.975×10⁻⁷ @ r = 3.55, vs its registered +6.056×10⁻⁷),
y_his stays positive (+5.449×10⁻⁸ @ r = 4.0, vs
+3.404×10⁻⁷), while **E2-1 dips to −1.162×10⁻⁶ @ r = 9.95**
and B-2 to −8.611×10⁻⁷ @ r = 9.95 — the registered set's
radial resolution, not any one subject, is what these
ceilings are relative to. This is carried onto the
quotable set as rider G53-R2, binding every quotation of
the raised β.

## §3 Claim (b) — the Arm B control: SURVIVES

B-2, the clipped seed of record (sha256 `d228c82e…`),
full registered bars on gate machinery:

- **β = 0.192578125: LEGAL.** wa worst margin SEC
  **+6.042169×10⁻⁷ @ r = 3.75**, **106.0× FD floor**,
  Type-I 1.000 at both spacings (fine spacing
  +6.038002×10⁻⁷); audit4 worst +6.036612×10⁻⁷, sign
  agreement met; shell sampled-NEC +2.127×10⁻⁷ (C-2).
  Phase stored digits reproduced (SEC +6.042168×10⁻⁷,
  agreement 7.9×10⁻¹³).
- **β = 0.195078125: FAILS identically.** SEC
  −1.274695×10⁻⁵ @ r = 9.75 (stored −1.274695×10⁻⁵),
  Type-I 0.98593 — RW-5's own bracket rung.
- **Side-by-side with RW-5 on identical gate machinery:**
  ceilings identical (0.192578125), failure brackets
  identical ([0.192578125, 0.195078125]), deciding
  margins SEC +6.042169×10⁻⁷ (B-2) vs +6.055585×10⁻⁷
  (RW-5) — a difference of 1.34×10⁻⁹, 0.22% of the
  margin, buying and costing no rung. The gate's
  independent recomputation of the embedding itself is
  exact (§4): the LS embedding of RW-5 onto the 16-mode
  basis is what the record says it is, and its clip is
  one coordinate.
- **Recorded scope of "lossless":** the claim as charged
  and as made by the phase is a registered-bars statement
  (ceiling, bracket, deciding margins at home), and in
  that sense it is exact. Under the gate's denser radial
  sampling the two vectors do differ (§2: RW-5 stays
  SEC-positive, the clipped seed dips at r ≈ 9.95, as
  does E2-1) — so "lossless" may not be quoted in any
  continuum sense. In the registered-bars sense, the
  control licenses the combination's "unproven, not
  refuted" wording: Arm B's seed carried the standing
  best into the finer basis at full strength, and the
  arm's no-yield is a statement about the search, not
  about a weakened seed.

## §4 Claim (c) — Amendment A-408-1: SURVIVES AS FENCED

The gate verified the amendment's factual basis on its own
machinery, not on the phase's say-so:

- The registered LS embedding of RW-5 onto the 16-mode
  basis (log φ on linspace(R₁,R₂,20001), `np.linalg.lstsq`,
  a/q/r_m carried unchanged) was **recomputed by the gate
  and reproduces the stored unclipped vector at max diff
  0.0** (sha256 `a0201be1…` ✓; residual RMS
  9.207430281480095×10⁻³, max 3.673295654339093×10⁻²,
  identical to the stored record). The containment
  failure was real: exactly one coordinate, c idx 13 =
  **−2.3199648239179234**, lies outside the Arm B box
  (by 0.06996482391792336); both widened coordinates are
  inside. Not a numerical accident — the gate's fresh
  lstsq lands on the same value.
- The clip changes **exactly one coordinate** (idx 13 →
  −2.25); the clipped vector's sha256 is `d228c82e…`; it
  is byte-identical to Arm B's subject B-2; its
  containment was verified coordinate-by-coordinate
  against the Arm B box (all 30 inside).
- The losslessness gate the amendment imposed was applied
  to **the clipped vector** and passed in both places the
  registration required: at screening, exactly
  0.192578125 on both pool instruments (stored record);
  at home, §3 of this gate — ceiling and bracket
  identical to RW-5's, margins within 0.22%.

**Ruling.** The disclosure is complete (the amendment is
appended to the checkpoint, dated, marked post-hoc; both
hashes are on record; the failure it answers is recorded
with its anatomy), and the substitute seed was gated on
exact losslessness before the arm's search was believed —
a stricter handling than the lineage's own precedent
(392's R-16 seed sat 0.00698 outside its box with its
continuity read taken on the unclipped vector). The Arm B
record is therefore quotable, **only in the amended form**
(rider G53-R3): the seed is named "RW-5 embedded,
box-clipped at c13" in every quotation; Arm B's no-yield
is a statement about the arm as amended; the unclipped
vector was never a member of the Arm B box and supports
no claim as a seed; and the amendment itself is part of
the quotable record — a reader must be able to see that
the seed of record was changed by amendment, and why.

## §5 Claim (d) — the ladder statement: SURVIVES RESTATED

Each clause was checked against the stored records (the
phases' checkpoints and search records, and Gate-51's
rulings where the clause reaches back):

- **Time: SPENT** — confirmed for bests. 392's Arm T:
  Gate-51's restated ruling stands (best-history exactly
  0.191796875 at all 119 recorded generations; the cap was
  not binding). 408: Arm A's Powell bought nothing; Arm
  A's DE best was found mid-run (screening 0.193359375
  at resumed gen 74 of 107; final mean 0.19277); Arm B's
  DE best never moved. **Precision (restatement 1):**
  "time spent" is a statement about bests — Arm B's
  population *mean* was still rising at its cap (0.102 →
  0.19034 over 140 gens), with its best the seed itself
  at every generation. That is exactly why the
  combination is "unproven, not refuted" and why
  FU-P408-3 (resumption) exists; quoted without the
  precision, "time spent" would overstate Arm B.
- **Modes: PAID, once finished** — confirmed. Arm A's
  home yield over RW-5 is +0.00078125, carried by one
  member of six (the other five ceiling at 0.190859375);
  the resumption cross-check reproduced the staged
  population's fitnesses 64/64 exact; the staged control
  home-verifies at its screening level (0.191015625), so
  the yield is the finished run's, not the resumption's
  artefact.
- **12-mode widening: SPENT** — confirmed (Gate-51 claim
  (b): RW-5 strictly interior on all 26 coordinates of
  its box, nearest edge 0.0427; the price list was
  empty, and nothing in 408 reopens it at 12-mode).
- **The combination: UNPROVEN, NOT REFUTED** — confirmed
  and licensed by §3/§4 (the seed was lossless; the DE
  did not converge from 2 seeds in 140 gens; its one
  Powell screening rung at 0.193359375 does not survive
  home — B-1 ceilings at 0.190859375 on gate-confirmed
  phase records).
- **Dose–response** — confirmed from the stored ceilings:
  0.1363 → 0.18671875 (+0.05041875) → 0.18984375
  (+0.003125) → 0.191796875 (+0.001953125) → 0.192578125
  (+0.00078125) → 0.193359375 (**+0.00078125**). The last
  two increments are equal — the increments have stopped
  shrinking. **Precision (restatement 2):** "the ceiling
  margin thinned ~17×" is exact as an *absolute-margin*
  ratio — the deciding SEC margin went 6.056×10⁻⁷ →
  3.613×10⁻⁸, a factor 16.8 — while as a *floor-multiple*
  ratio it is 106.5× → 6.8×, a factor 15.7. Quotations
  should say which ratio is meant; both are on the face
  of G53-A/G53-E. The bracket above the new best fails
  hard (−1.257×10⁻⁵ SEC, §2), and what remains is the
  two named coordinates of the phase record (16-mode
  c idx 0, saturated by every Arm A subject and A-6's
  sole bound-sitter — verified from the stored vector;
  c idx 13, on/near its bound for every Arm B subject).

## §6 Controls

- **y_his @ 0.1363: LEGAL** on gate machinery — worst SEC
  +3.4041777787759174×10⁻⁷ @ r = 5.0 (stored
  +3.404177799426875×10⁻⁷; ratio 0.99999994 to Gate-42),
  109.5× floor, Type-I 1.000 at both spacings, audit4
  +3.395770×10⁻⁷ agreeing. **@ 0.1364: still legal
  pointwise** — see C-1; the "fails" half of the charged
  control survives only as the screen's rating statement.
- **E2-1 @ 0.191796875: LEGAL** — worst SEC
  +7.075488945987914×10⁻⁸ @ r = 6.0 (stored +7.075×10⁻⁸),
  13.4× floor, Type-I 1.000, audit4 +5.407160×10⁻⁸.
- **RW-5 @ 0.192578125: LEGAL** — worst SEC
  +6.055585116608624×10⁻⁷ @ r = 3.75 (Gate-51 gate read
  +6.055586×10⁻⁷; phase stored +6.055585252705956×10⁻⁷),
  106.5× floor, Type-I 1.000, audit4 +6.050012×10⁻⁷.
  **@ 0.195078125: FAILS, compound** — SEC
  −1.031585673360951×10⁻⁵ @ r = 9.75, Type-I 0.98499,
  sampled-NEC −8.16×10⁻⁷, audit4 −1.032461×10⁻⁵.

## §7 The quotable set

**G53-A.** In the continuously graded category, subject
A-6 (Phase 408 Arm A; 16-mode grading basis at the
original box; sha256
`6461827fac113c49f8f28aea04115df524446dbd44530b86f5e408e5d3c00039`)
is fully legal under the Gate-42 common bars on the
registered set at **β = 0.193359375**, with failure
bracket [0.193359375, 0.195859375] (the bracket rung
fails on SEC −1.257×10⁻⁵ @ r = 9.75). The deciding
margin is SEC at r = 5.0: +3.613×10⁻⁸ at the registered
spacing h = 0.0375, converging under refinement to
**+2.675×10⁻⁸** (h → 0; audit4 +2.6745×10⁻⁸). A-6's sole
box bound-sitter is c idx 0. *(Riders G53-R1 and G53-R2
bind every quotation of this claim.)*

**G53-B (the fence, verbatim).** Graded-category wording
only: this set never contests the step-profile category —
Procaccia's β = 0.1363 stands there, and the programme's
verified best there remains β = 0.10. Speeds are
comparable only within a stated category.

**G53-C.** The Arm B seed of record — RW-5 embedded by
least squares onto the 16-mode basis and box-clipped at
c idx 13 (sha256
`d228c82e18396fe5d6a7ccc85881c558355d8d096bc8923e856ea7fc3615d69f`)
— home-verifies at exactly RW-5's ceiling
β = 0.192578125 with RW-5's identical failure bracket
[0.192578125, 0.195078125] and deciding SEC margins
within 0.22% (+6.042×10⁻⁷ vs +6.056×10⁻⁷): the embedding
plus clip is lossless at the registered bars, and the
combination's no-yield is quotable as "unproven, not
refuted".

**G53-D.** Amendment A-408-1 stands as the quotable
handling of the C-408-5 containment failure: the seed of
record was changed post-hoc, by dated amendment with
both vector hashes on record, from the least-squares
embedding (whose c idx 13 = −2.3199648239179234 lies
0.06996 outside the Arm B box) to its box-clipped form,
gated on exact losslessness at screening and at home —
both gates passed. *(Rider G53-R3 binds.)*

**G53-E.** The graded family's enrichment ladder, as
restated by this gate: more time is spent (a statement
about bests; Arm B's population mean was still rising
at its cap); the finer 16-mode basis paid once its
truncated run was finished (+0.00078125, exactly the
increment the 12-mode widening bought); the 12-mode
widening is spent; the combination of basis and widened
box is unproven, not refuted. The dose–response
increments end +0.00078125, +0.00078125 — no longer
shrinking — while the deciding margin thinned from
+6.056×10⁻⁷ to +3.613×10⁻⁸ (16.8× in absolute margin;
106.5× → 6.8× in floor multiples) and the bracket above
the new best fails hard: the remaining headroom reads
as a thin shell measured from a higher floor, with two
named coordinates (16-mode c idx 0 and c idx 13) left
priced.

**G53-R1 (thin margin — binding rider to G53-A).** Any
quotation of β = 0.193359375 states the deciding margin
with it: SEC +3.613×10⁻⁸ at the registered spacing
(6.8× the FD floor — the thinnest deciding margin of
the lineage's raises), +2.675×10⁻⁸ in the h → 0 limit.
The margin is a converged, instrument-confirmed
positive quantity, not an FD artefact; it is also
~17× thinner than the previous best's.

**G53-R2 (registered-set scope — binding rider to
G53-A).** "Fully legal" in G53-A means fully legal
under the Gate-42 common bars on the registered set
pts_1020_control, the instrument of every verdict in
this lineage. On a denser radial sampling (step 0.05,
the registered directions), A-6's SEC profile dips to
−1.257×10⁻⁶ at r ≈ 5.42, between the registered
shells: A-6 is not SEC-legal in the radial continuum
at this β, and no quotation of G53-A may drop the
registered-set scope. (The same densification leaves
RW-5 and y_his SEC-positive at reduced margins and
finds E2-1 also dipping; the scope is the registered
set's, not A-6's alone.)

**G53-R3 (amended-seed wording — binding rider to
G53-C/G53-D).** The Arm B seed is named "RW-5 embedded,
box-clipped at c13" in every quotation. Arm B's
no-yield is a statement about the arm as amended. The
unclipped embedding was never a member of the Arm B
box and supports no claim as a seed.

*Gate-53 records: `gate53/results/` (g53_records.json,
g53_audits_{y_his,E2-1,RW-5,B-2}.json, g53_thin.json,
g53_dense.json, g53_laptop_out.json); machinery
`gate53/work/` (g53_lib.py, g53_records.py,
g53_audits.py, g53_thin.py, g53_dense.py, g53_laptop.py).
Working record: `gate53/GATE53_CHECKPOINT.md`.*
