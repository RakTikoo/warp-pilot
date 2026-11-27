# PHASE 412 REGISTRATION — THE SPEED LADDER:
# HOW MUCH PEAK CAN THE FAMILY CARRY?

Filed before any computation. Charge: ledger
entry 1072 (Rakshit's direction: "let's speed
it up 1000000 time c").

## SS0. The act

On Phase 400's corrected static base (N/M at
400's winner verbatim), the shift re-introduced
as a FREE SPLINE SHAPE (p341's family, K = 9;
K = 17 gated, SS5) — the Phase 405 assembly
verbatim. In this family the design's speed
variable IS the peak |β·S| (β = 1.1 pose). The
Gate-50 winner meets the SS7 warp criterion
(peak = CRIT = 0.4426742490267404) at joint
+1.227385×10⁻⁶. This phase climbs a LADDER of
peak targets above the criterion and at each
rung maximises the joint (SET-244, band
[10, 20], the lineage's joint min(NEC, DEC))
subject to peak |β·S| = the rung target (hard
equality, by scaling — S is exactly linear in
the knot vector), until the joint's zero
crossing is bracketed or the registered
ceiling is reached. A million c is a peak of
10⁶ ≈ 2.26×10⁶ × CRIT; the ladder measures
how far the family actually carries, with its
own fitted cost law — the extrapolation is a
prior (SS1), never the result.

## SS1. Stored bars and the prior

- THE BASE (400's confirmed winner, Gate-48):
  (μ_N, μ_M) = (2.330448313835416,
  11.343911464156438), K = 17 vN/vM verbatim.
  Joint at S ≡ 0: +1.3977194851281464×10⁻⁶
  (the static margin M0). SEC min
  −2.0502915986749415×10⁻⁴; ρ_min
  9.943380734109653×10⁻⁵.
- THE GATE-50 WINNER (405's best shape,
  Gate-50 quotable set): K = 9 knots
  (0.40243113547885484, 0.23237610808870765,
  0.10110504581235646, 0.030274386301308052,
  0.021559512630984955, 0.01297222477301449,
  0.007865452045132022, 0.0035285750792539276,
  −0.00043513901545560714) at peak = CRIT,
  attained at r = 10 (G50-R5: quoted AT THE
  CRITERION, edge attainment on its face).
  Joint +1.2273852081052888×10⁻⁶ (405 stored;
  Gate-50 read +1.2273852081036624×10⁻⁶);
  worst-null +7.282191×10⁻⁷; adversary polish
  +1.214724×10⁻⁶; SEC −2.213557×10⁻⁴.
  Spend at the criterion: M0 − joint =
  1.703×10⁻⁷.
- THE FIXED SHAPE ON THIS BASE (404): break-
  even peak 0.1522; cost at the criterion
  1.058382×10⁻⁵. Context only.
- THE PRIOR (Gate-50 claim (c), RESTATED):
  on this base both shapes' spends are
  ~quadratic in peak; the free shape's
  coefficient is 8.69×10⁻⁷ per peak²
  (exponent ≈ 2.10). Extrapolated naively it
  prices the margin out at peak ≈ 1.27
  (≈ 2.9 × CRIT) and peak 10⁶ ~12 orders
  short. STATUS: A PRIOR TO BE TESTED. The
  coefficient was base- and shape-dependent
  at every prior test (397/401/405); the
  ladder re-optimises the shape at every
  rung, and its own fitted exponent and
  coefficient — from its own rungs — are the
  deliverable's numbers.

## SS2. Frame

VM is the frame of record. The laptop
admission control (the lineage endpoint read,
p389 form, as in 398/400/401/405) is run and
followed: if ADMITTED, deciding reads are
nevertheless all VM reads (the ladder compares
levels at 10⁻⁷–10⁻⁹ increment scale; one frame
carries every rung). If the pool is
unreachable, the admission is recorded NOT
RUN with the reason and the phase proceeds
VM-only.

## SS3. Controls (before any rung is believed)

- CTL-412-WIN: p412's assembly (p405's,
  verbatim) at vS = 0 reproduces the 400
  winner: the five minima (nec, dec, wec,
  sec, rho), the joint and the exact
  worst-null at the SET NEC argmin at diff
  0.0 vs SS1.
- CTL-412-CRIT (the criterion rung): the
  Gate-50 winner's stored knot vector, scaled
  to peak = CRIT through this phase's screen
  path, reproduces the stored confirmation:
  joint +1.2273852081052888×10⁻⁶, the five
  minima, nec_argmin_r 17.926829268292682,
  peak 0.44267424902674035 attained at
  r = 10.0 — diff 0.0 class (float64
  roundoff; Gate-50's own read differed from
  the stored value by −1.6×10⁻¹⁸).
- CTL-412-ADM: the laptop admission read
  (SS2), compared against the VM endpoint
  record (phase405/results/
  p405_controls_laptop.json).

## SS4. The assembly and the reads

Identical to Phase 405 SS4, verbatim:
profiles_at405 / set_read405 / phys_row405 /
worst_null_at405 / adversary_polish405 from
p405_lib (N/M = 400's winner through
p398_lib.profiles_at398; S = not-a-knot C2
cubic through K knot values uniform on
[10, 20] on a base S ≡ 0; T via
p316_lib.T_from_SNM at BETA = 1.1). Peak
|β·S|: the phys-row form (FINE_R x-axis).
Amplitude is set by scaling (scale_to_peak);
the scaled shape's peak is the target up to
float rounding, verified per screen by the
read's phys row, and the peak's attainment
radius (FINE_R argmax) is recorded per rung
winner. Feasibility of a screen: C1 — the
SET read's ρ_min > 0 (the N/M floors are
frozen at the winner; no S floor exists in
the lineage). Sampled minima name their
frame convention (SAMPLER-M, Gate-43 C-10);
deciding values are diff-0.0 reproductions,
frame-invariant worst-nulls and adversary
polishes. SEC is read at every screen and
printed in every rung record (it is NOT in
the joint).

## SS5. The ladder

RUNGS. Multiples m of CRIT, targets
P(m) = m × CRIT:
  m = 2 → 0.8853484980534808 (= H2's peak)
  m = 5 → 2.213371245133702
  m = 10 → 4.426742490267404
  m = 25 → 11.06685622566851
  m = 100 → 44.26742490267404
then ADAPTIVE continuation ×3 in m
(300, 900, 2700, 8100, 24300, 72900, 218700,
656100, 1968300, …) until (a) a rung's best
joint < 0 at both K (the crossing is
bracketed between the last legal rung and
this one), or (b) the next target would
exceed the registered CEILING peak = 10⁶
(the last adaptive target ≤ 10⁶ is
m = 1968300, P ≈ 8.71×10⁵). The criterion
rung (m = 1) is the control CTL-412-CRIT,
not a searched rung.

AMPLITUDE BOX PER RUNG (stated before
searching, per the charge). The walks
operate on the SCALED knot vector (405 form:
CD perturbs the scaled incumbent; each
screen renormalises to the target). The 405
box |vS| ≤ 1 cannot contain scaled vectors
at these peaks (the criterion winner's own
largest knot is 0.402; at m = 100 the same
direction has knots ~40). The registered
box at target P is
  B(P) = max(1.0, 2.0 × P / BETA)
on every scaled knot component:
  m=2: 1.610 · m=5: 4.024 · m=10: 8.049 ·
  m=25: 20.12 · m=100: 80.49 ·
  adaptive: B = 2P/1.1 by the same formula.
CD step sizes scale with the rung:
steps = (0.05, 0.02, 0.008) × max(1, P/CRIT);
NM polish xatol likewise × max(1, P/CRIT).

OBJECTIVE at fixed P: score(vS) =
joint(SET read at the scaled vS) −
PEN400(vS_scaled), PEN400 = LAM400 ×
rough(v), LAM400 = 1.0×10⁻⁵ (Phase 400's
rescaled penalty, as in 405). Incumbent
semantics (379/398/400/405): best score
among C1-feasible screens at the rung; the
pure joint is recorded for every screen,
and each rung record carries BOTH the
score-incumbent's joint and the maximum
pure joint among the rung's feasible
screens. DISCLOSED PROPERTY of the
registered pricing: PEN400 on a fixed
direction grows ~quadratically with
amplitude, so at high rungs the score
increasingly prices smoothness; the
pure-joint maxima are on the record so a
gate can re-judge. RUNG LEGALITY is by
the score-incumbent's joint (≥ 0 legal),
with the pure-joint maximum stated
alongside wherever the two disagree in
sign.

SEARCH PATTERN PER RUNG (K = 9). Seeds:
(i) the previous rung's score-incumbent
shape (for m = 2: the Gate-50 winner);
(ii) the Gate-50 winner shape; (iii) the
H2 seed (h2_seed). Seed screens first; CD
sweeps from the best seed; NM polish
(maxfev 120) on the incumbent; CD again
from the polished incumbent (405's stage
pattern). Per-rung cap: 280 screens (K = 9).

K = 17 GATE. At the first rung where the
K = 9 incumbent joint < 0, a K = 17 arm
runs at that same rung BEFORE the rung is
declared illegal: warm start = the K = 9
incumbent's spline sampled at the 17
knots, plus the Gate-50 winner interpolated
to 17 knots; same pattern; arm cap 200
screens. If the K = 17 incumbent is ≥ 0
the rung is legal (K = 17) and the ladder
continues (at each later rung K = 9 runs
first; the K = 17 arm runs iff K = 9 is
< 0 there). If both K are < 0 the rung is
illegal and the ladder stops: the crossing
is bracketed.

CONFIRMATION per rung winner (the score
incumbent, at its frozen scaled vector):
full SET re-read reproducing the stored
screen at diff 0.0; exact worst-null at
the SET NEC argmin; the peak and its
FINE_R attainment radius; the shape's
locals at the joint's argmin radius (S,
S′, S′′ — the fragile-site anatomy);
SEC min on the face. The adversary polish
runs for every LEGAL rung winner and for
the first illegal rung's incumbent.

CAPS. Per-rung K = 9 cap 280; per-arm
K = 17 cap 200; TOTAL CAP 2400 stored
screens. If the total cap binds before
the crossing is bracketed or the ceiling
reached, the verdict is COST-BOUNDED with
the bracket state as it stands.

THE LADDER'S OWN COST LAW (a deliverable):
spend(P) = M0 − joint_incumbent(P) at the
criterion (control) and every searched
rung; fit spend = A × P^p over the rungs
with spend > 0 (log-log least squares,
the fit's points named); report A, p, the
fit's implied zero-crossing peak, and the
measured bracket side by side. The prior
(SS1) is reported as a prior, tested
against the fit.

## SS6. Verdict mapping

- CARRIES TO P* = ⟨value⟩: at least one
  rung above the criterion is legal and
  confirmed; P* is the highest legal
  rung's peak. The P* winner is stored as
  a candidate at that speed. GATE
  REFERRAL of the ladder's claim set.
- THE CRITERION IS NEAR THE CEILING: the
  crossing is bracketed (last legal rung
  and first illegal rung stated, at both
  K where the gate ran); the joint-vs-peak
  curve is the anatomy; the gap from P*
  to 10⁶ is stated in orders of magnitude
  WITH THE LADDER'S MEASURED EXPONENT
  (SS5), not the extrapolated prior.
- COST-BOUNDED: the total cap binds first;
  the bracket state reported honestly.

## SS7. Fences

Every rung is a band [10, 20] read at the
home pose (β = 1.1); 356's full-extent
caveats travel (no full-extent read of any
ladder configuration is claimed). The level
is the lineage's joint min(NEC, DEC); SEC
— outside that joint at every point of
this line — is read at every rung and
printed, never hidden. No EC pass and no
member by verdict name: a legal rung is a
CANDIDATE at its peak, referred to a gate.
The peak is the design's coordinate-speed
parameter — a rung's peak is a property of
a stored configuration's shift profile;
nothing physical moves, and no transport,
sustainment or front content is claimed.
Sampled minima name SAMPLER-M (C-10).
Three-goal accounting and the DESK line
go in the memo.
