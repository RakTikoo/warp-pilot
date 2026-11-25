# FTL Programme — Phase 108 CHECKPOINT (ground record)

**Status:** CLOSED (2026-11-23, coordinator) — all five
items resolved against their pre-registered criteria
(checkers: P108-1 102/102, P108-2 63/63, P108-3 127/127,
P108-4 99/99, P108-5 281/281, all re-run by the
coordinator). One milestone fired: P108-5 met the QET
line's registered reopening bar (R_net > 1,
resource-counted, second-pathed). No joint (i)+(ii)
improvement at any superluminal cell. Verdict sections
and final synthesis at the end of this file. Workers
did not edit this file.

**Mission / sequencing.** Phase 108 executes Phase 106's follow-up
queue in its order: (1) the two-centre band family, (2) the
gentler-flank control, (3) the force-alignment set, and (4) Phase
83's long-carried thickness-preserving breathing item. The
conditional multipartite-QET search inherited from FU-P106-3a is
handled as P108-5, strictly under its search-first condition.
**FU-P106-4a (the ℬ-guided search) is NOT run and is not promised
in this phase.**

**Parent record.** `../phase106/CHECKPOINT106.md` in full;
Phase 106's P106-1/P106-2 result JSONs and machinery; Phase 83's
P83-2 registration and verdict for the breathing bed;
`~/workspace/compute_allocation.md` for the free-compute rule.

## Standing orders (binding)

- FAILURE PROTOCOL: anatomy plus at least one mechanism-suggested
  follow-up for every negative; closure only on structural
  evidence with a reopening condition.
- ANTI-LOOP RULE: no third revisit of a closed theory class
  without a NEW mechanism. P108-2's verdict is the item that
  supplies or denies such a mechanism for aimed deformations.
- SUPERLUMINAL AMENDMENT: β = 1.1 is scanned directly in the
  wall items; born-superluminal framing only — crossing is never
  modelled or relied on. β = 1.5 is not an item in this phase
  except where a registration explicitly says otherwise (none
  does).
- float64 everywhere; programme venv
  `~/workspace/warp-pilot/venv/bin/python`.
- Published forms only, never gate-fitted; candidates enter at
  the action where a theory is posed.
- FULL-EC bars for wall audits: NEC/WEC/SEC/DEC
  (Hawking–Ellis margins), Type-I fraction, sampled-null NEC
  (≥162 Fibonacci directions), full volume. Margins alone never
  decide. Conservation: prescribed-geometry audits use the
  Einstein tensor as required source; conservation is automatic
  by Bianchi and is stated, not re-derived.
- Time-dependent walls are audited at the WORST instant, never
  on a time average.
- Bars are pre-registered here; amendments are appended, dated,
  marked post-hoc, and never silently broaden a pass.
- ADVERSARIAL PROTOCOL: any positive gets an independent second
  path before integration.
- EVIDENCE RULE + grounding bar, stated on each item's face.
- OPTIMIZATION DIRECTIVE + RIDER + FREE-COMPUTE RULE: approved
  pools only per `~/workspace/compute_allocation.md`; any run
  expected over ~2 h continuous is checkpointed and routed, not
  left uncheckpointed on this VM.
- UNIQUENESS PROTOCOL; C12 accounting (every superluminal row
  is EFFECTIVE ONLY or worse until a joint (i) legality +
  (ii) solution-grade pass).
- LANGUAGE: any pass is a “scan signal under attack” until a
  later Gate verifies it.
- INTERNAL ONLY: nothing uploaded, nobody contacted.

---

## P108-1 (FU-P106-1a) — THE TWO-CENTRE BAND FAMILY AT β = 1.1

**Grounding.** Phase 106 found that the registered band
B₀ = {significant points: r ∈ [20, 27], θ ∈ [π/3, 2π/3]}
contains two distinct binding structures: (a) a q-collapse
corner at (20.0, π/3), where band `q_values` = +∞ in every
single-centre row at both spacings; and (b) a DEC site at
(23–25, π/2). Its reopening condition is inherited verbatim:
**a finite band q_values at BOTH grid spacings.**

**Construction.** Phase 106's deformed-radius construction and
champion (10,30), M = 8.0 profile, unchanged except that the
localised factor becomes a sum of two Gaussian centres:

  F(r,θ) = 1 + A_c·exp(−((r−20)/w_r)² − ((θ−π/3)/w_θ)²)
             + A_s·exp(−((r−24)/w_r)² − ((θ−π/2)/w_θ)²),

with ρ = r·F, all profiles and the shift evaluated at ρ, and
the radial direction m = ∇ρ/|∇ρ| derived analytically and
FD-verified before any deformed number (Phase 106 G3 pattern).
Primary widths (w_r, w_θ) = (3.0, 0.50).

**Registered rows (primary widths).** Control (A_c, A_s) =
(0,0); single-centre corner rows (−0.12, 0) and (+0.12, 0);
joint rows (−0.12, −0.12), (−0.06, −0.12), (−0.12, −0.06),
(+0.12, −0.12), (−0.12, +0.12). The A_s = −0.12 column carries
Phase 106's one genuine gain (its best row's sign and size);
the corner sign is unknown, so both corner signs are run.
**Conditional refinement:** if any primary row gives a finite
band q_values at h = 0.3, or improves the control's band
worst-direction q by ≥10%, run that row's sign pair at widths
(2.0, 0.35) and (5.0, 0.80), and at amplitudes halved and
doubled componentwise within |A| ≤ 0.16. The refinement's
disposition is stated either way.

**Machinery gates (before any deformed number).** G1:
(A_c, A_s) = (0,0) reproduces the spherical factory's metric
to ≤1e-12 relative. G2: the spherical control at β = 1.1
fails in kind (failure present; worst-margin site in
r ∈ [22,27]; sampled NEC negative at that site). G3: analytic
∇ρ FD-verified. G4: φ-redundancy at fixed (r,θ).

**Audit.** Gate-standard auditor at h = 0.3 and h = 0.15 on
Phase 106's exact point set. Primary band B₀ as above
(comparability with Phase 106 and its reopening condition);
a wider reporting band B₊ = {r ∈ [18,29], θ ∈ [π/4, 3π/4]}
is also read for every row. Per row: band max-q in BOTH
Phase-63 reads (`q_values` and `q_at_worst_dir`) with sites,
band Type-I fraction, full-volume legality fraction, Type-I
fraction, worst margin + site, global max-q + site,
sampled-NEC minimum + site. Second path (`audit4`) on any
row that is band-feasible, finite in band q_values, or
improving on the control's band worst-direction read.

**Verdicts (only these).**
- **BAND-LOCAL FEASIBLE POINT EXISTS** (row named): band
  max-q ≤ 0.99 on both reads at both h in B₀, second-path
  confirmed, full-volume price stated in the same breath.
- **FINITE BAND q — REOPENING CONDITION MET, NOT FEASIBLE**:
  band q_values finite at both h in some row but > 0.99 on
  at least one deciding read; numbers and price stated.
  (This outcome is milestone-reported on landing.)
- **NO FINITE BAND q IN THE TWO-CENTRE FAMILY**: band
  q_values = +∞ in every row at both h; the band-local
  route then CLOSES with that as its reason, the two-
  structure anatomy restated, and the best row's priced
  trade reported.
- **MACHINERY FAILURE** (gate named).
C12: prescribed-geometry wall legality at β = 1.1 — not
transport; a band-feasible row is not a legal wall.

**Deliverables:** `results/p1081_run_record.md`,
`results/p1081_memo.md`, `results/p1081_results.json`;
scripts + independent checker in `work/` (checker
recomputes every verdict-carrying number from the results
file).

---

## P108-2 (FU-P106-1b) — THE GENTLER-FLANK CONTROL

**Grounding.** Phase 106's best single-centre row
(A = −0.12 at (w_r, w_θ) = (3.0, 0.50), centre (23, π/2))
improved the band worst-direction q from 110.4 to 32.74
(−70%) and band Type-I ×6.2, while full-volume legality
FELL 0.2099 → 0.2029, the worst margin worsened ×2.9 and
the sampled-NEC minimum ×5.7. Phase 106's anatomy blamed
the bump's flanks. This control decides whether that tax
is a slope effect (reducible by gentler flanks) or the
local form of Phase 83's legality conservation
(structural). **This verdict is what would supply or deny
a NEW mechanism for any third aimed-deformation
registration (anti-loop rule).**

**Construction.** Phase 106's single-centre family,
centre (23, π/2) fixed. Gentler widths: (w_r, w_θ) =
(5.0, 0.80) and (8.0, 1.20). Amplitude ladder at each
width, h = 0.3 first: A ∈ {−0.04, −0.06, −0.08, −0.10,
−0.12, −0.16, −0.20, −0.24} (negative first — the sign
that gained); if no negative amplitude reaches the match
window, the positive ladder {+0.08, +0.16, +0.24} is run
and its failure to match is reported.

**Match definition (fixed in advance).** The target is
Phase 106's best row's band worst-direction q at
h = 0.3: 32.74. A gentler row MATCHES iff its band
worst-direction q at h = 0.3 lies within ±10% of 32.74.
Per width, the matched row is the ladder row closest to
32.74 inside the window (if two, the smaller |A|). Each
matched row is then audited at h = 0.15 in full, and
Phase 106's best row and the spherical control are
carried from `../phase106/results/p1061_results.json`
(their stored reads are the comparison; the control's
legality 0.2099 and the best row's 0.2029 at h = 0.3 fix
the tax Δlegality = −0.0070).

**Tax comparison (fixed in advance).** For each matched
gentler row vs Phase 106's best row, at both h: Δlegality
vs the control; worst margin; sampled-NEC minimum; global
max-q; band Type-I fraction.
- **FLANK TAX IS A SLOPE EFFECT (REDUCIBLE)**: some
  matched gentler row pays strictly less tax than Phase
  106's best row — |Δlegality| < 0.0070 at h = 0.3 AND
  its worst margin and sampled-NEC minimum are no worse
  than the best row's by more than the row's FD floor —
  with the h = 0.15 reads not reversing the comparison.
- **FLANK TAX IS STRUCTURAL (LEGIBILITY CONSERVED
  LOCALLY)**: every matched gentler row pays ≥ Phase
  106's tax on legality, or worse margins/NEC at matched
  target, at the deciding spacings.
- **MATCH NOT REACHED**: no ladder row at either gentler
  width lands in the match window; the closest rows and
  their target reads are reported (this outcome itself
  prices what widening does to the gain).
- **MACHINERY FAILURE** (gate named; the Phase 106 gates
  G1–G4 pattern applies, rerun for the wider widths).
C12 as P108-1.

**Deliverables:** `results/p1082_run_record.md`,
`results/p1082_memo.md`, `results/p1082_results.json`;
scripts + checker in `work/`.

---

## P108-3 (FU-P106-2a) — THE FORCE-ALIGNMENT SET

**Grounding.** Phase 106 priced the coupling-force front's
pin to one exact point: at the P101-5B hinge best, subset
point 44 is the front's ONLY same-sign point, and there
the two force contributions align (combined force share
0.926 of D_can) exactly where □φ ≈ 0 (t_kin ≈ 2×10⁻⁵⁸).
The registered question: is that point an isolated
accident of one optimisation, or a structural feature of
the family — a set the front cannot be posed without?

**Corpus (fixed).** Every unique stored configuration in
`../phase101/results/p1015_partB_raw.json`: the two direct
P76-1 rows (A76_mu0, B76_mu0), runs_A[0..1], runs_B[0..2]
(best_A and best_B duplicate runs entries and are read
once, identified as such). Seven unique configurations,
each on the 56-point β = 1.1 subset, canonical terms from
`../phase101/work/p1015_lib.py` (`canonical_terms`:
t_kin = □φ, t_pxx, t_FA, t_FB; D_can = Σ|terms|; a point
is non-degenerate iff D_can ≥ 1e-9).

**Alignment set (defined before computing).** At a
non-degenerate point of a configuration, the point is in
the ALIGNMENT SET iff all of: (i) both force terms are
live, |t_FA|, |t_FB| ≥ 1e-6 × max_k|term_k| (the P106
live floor); (ii) the force terms have the same strict
sign; (iii) the combined force share
S_F = (|t_FA| + |t_FB|)/D_can ≥ 0.90; (iv) the kinetic
term is vanishing in relative form, |t_kin|/D_can ≤ 1e-6
(absolute □φ also reported). Sensitivity reads at
S_F ∈ {0.80, 0.95} and |t_kin|/D_can ∈ {1e-8, 1e-4} are
reported so the verdict does not ride on one threshold.
For every configuration: the set's members (subset
indices), each member's terms, shares, residual, and
whether the configuration's maximum-residual point is in
the set. Algebraic signature, derived and stated in the
run record BEFORE computing: with t_FA = F_A/P_X and
t_FB = F_B/P_X, sign(t_FA·t_FB) = sign(F_A·F_B) wherever
P_X ≠ 0, with F_A = ½·H_,φ(φ)·R_bed and F_B = −μφ; and
□φ depends on the configuration only through its profile
parameters (pi0, shape) and the bed — the run record
states what that implies for which configurations can
share kinetic-vanishing points.

**Verdicts (only these).**
- **STRUCTURAL FEATURE**: the alignment set is nonempty
  for every corpus configuration in which both force
  channels are live (μ ≠ 0 with the H-force not
  identically zero), and its members carry the
  configurations' worst residuals in the stated pattern;
  the front's obstruction is then stated in alignment-
  set form.
- **ISOLATED ACCIDENT**: the set is empty for all
  configurations except the hinge best (or empty
  everywhere under the primary thresholds), with the
  sensitivity reads shown; the search guidance that
  follows is stated (what a future registration should
  aim away from or at).
- **MIXED / SET EXISTS BUT DOES NOT CARRY THE PIN**:
  the set is nonempty somewhere but the worst-residual
  pattern does not follow it; the exact distribution is
  the result.
- **MACHINERY FAILURE** (a stored configuration's stored
  EoM max/median cannot be reproduced within 1e-6 —
  discrepancy named, per Phase 106's recovery pattern).
No new optimisation is registered in this item. C12:
pre-existing walls; no transport claim; this item moves
no front — it characterises the obstruction.

**Deliverables:** `results/p1083_run_record.md`,
`results/p1083_memo.md`, `results/p1083_results.json`;
scripts + checker in `work/`.

---

## P108-4 (FU-P832-2) — THICKNESS-PRESERVING BREATHING AT THE SUPERLUMINAL WALL

**Grounding.** Phase 83's pulsed wall (thickness-changing
breathing: R1 = 10 − δ·sin, R2 = 20 + δ·sin, so thickness
10 + 2δ·sin) failed at EVERY audited instant at β_p ∈
{1.1, 1.5} by the non-Type-I route, worst at peak
compression (t = 30). Its registered follow-up F2 =
FU-P832-2: a breathing mode that holds wall thickness
fixed — peak compression is the binding instant, and
thickness is what compression spends. The variant has
never been run.

**Pose (registered).** Phase 16/83 bed, unchanged:
Finalist-A family (R1₀ = 10, R2₀ = 20, M_geom = 2.0,
edge-peaked wd = 3.0 / floor = 0.2, s_rho = 2.0,
s_P = 1.16, cos shift), period T = 40, pattern speed
β_p constant. Thickness-preserving mode: the wall
translates bodily —

  R1(t) = 10 + a·sin(2πt/T),   R2(t) = 20 + a·sin(2πt/T),

so R2(t) − R1(t) = 10 exactly at every instant and the
wall centre moves 15 ± a. Amplitudes a ∈ {1.0, 2.0}.
Rows: β_p = 1.1 × a ∈ {1.0, 2.0}; controls: β_p = 0.1 ×
a ∈ {1.0, 2.0}; static twins (a = 0) at β_p ∈ {0.1, 1.1}.
Born-superluminal framing for the 1.1 rows: β_p is
prescribed; no crossing or formation is modelled.

**Machinery gates (before any superluminal number).**
(T1) thickness invariant: param_fn returns
R2(t) − R1(t) = 10 to float64 exactness at all sampled
times. (T2) a = 0 through the dynamic machinery
reproduces the static factory's core worst margin at
β = 0.02 to Phase 83 G1's standard (the stored Phase-16
value +1.1949248907449214×10⁻⁵, ≤25%). (T3) the static
twin at β_p = 1.1 FAILS (Phase 83 G3 pattern; if it
passes, that is reported first and the item re-registers
its question with the coordinator before proceeding).
The β_p = 0.1 control's outcome is reported, not gated:
it is a control, whatever it reads.

**Audit.** Phase-7 non-stationary auditor
(`../phase7/p74_auditor.py`), Phase 83 P83-2 pattern:
12 instants over one period, h = 0.3, with h = 0.15
re-reads at each row's worst instant. Point set: the
Phase-16 sample pattern widened to cover the translated
wall — 26 Fibonacci directions × radii {2, 4, 6} ∪
{step 0.5 over [6, 24]}; q reads (Phase-63 form, 162
directions) over the union shell sample (radii [6, 24]).
Per instant: core/sig worst margins (NEC/WEC/SEC/DEC),
Type-I fraction, max q + its radius, sampled-NEC minimum,
Eulerian E_-. **Instant classes:** the four phase
quadrants of the cycle — Q1 displacement > 0, wall
moving outward (t ∈ (0,10)); Q2 displacement > 0,
moving inward (t ∈ (10,20)); Q3 displacement < 0,
moving inward (t ∈ (20,30)); Q4 displacement < 0,
moving outward (t ∈ (30,40)) — with the worst instant
reported per quadrant as well as overall. The WORST
INSTANT decides; cycle averages are reported, never
deciding. Pulse price at the worst instant under the
Phase-83 registered scaling (τ = Δ/c with Δ = 10, and
τ = T), as in P83-2.

**Verdicts (per β_p = 1.1 row, only these).**
- **LEGAL AT EVERY INSTANT** (a named): worst-instant
  core margins > 0, Type-I = 1.000, at both h —
  MILESTONE, reported immediately, locked language.
- **DYNAMICS MOVES A STANDING NUMBER** (named,
  quantified ≥10× favourably vs the static twin or the
  Phase-83 pulsed rows).
- **DYNAMIC ANATOMY — NO RESCUE**: binding instant,
  quadrant and clause named; comparison vs the static
  twin and vs Phase 83's thickness-changing rows stated.
- **MACHINERY FAILURE** (gate named).
C12: prescribed-geometry pattern-speed audit — NOT a
transport claim.

**Deliverables:** `results/p1084_run_record.md`,
`results/p1084_memo.md`, `results/p1084_results.json`;
scripts + checker in `work/`.

---

## P108-5 (FU-P106-3a, CONDITIONAL) — A GENUINELY MULTIPARTITE PUBLISHED QET HAMILTONIAN

**Condition (exact).** This item runs its evaluation
ONLY if a documented literature search finds a genuinely
multipartite QET protocol whose Hamiltonian and
delivered-energy formulas are published in evaluable
form (printed formulas that can be recomputed, not only
numerical plots). If none is found, the worker records
the search — queries, sources checked, and the exact
gap (what exists vs what evaluable form would require)
— and the item closes as SEARCH NEGATIVE; no evaluation
is improvised from a non-evaluable source.

**Accounting (if triggered).** Phase 106 P106-3's
inherited accounting verbatim (resource counted;
per-sector uncorrelated reference; R_net defined as
there). Reopening bar, inherited verbatim: **any variant
with R_net > 1 resource-counted.** A positive gets a
from-scratch second path before integration and is
milestone-reported immediately.

**Verdicts (only these).** SEARCH NEGATIVE — NO
EVALUABLE MULTIPARTITE FORM FOUND (search + gaps
recorded) / EVALUATED — NET NON-POSITIVE (numbers) /
EVALUATED — REOPENING BAR MET (R_net > 1, second-pathed)
/ NOT POSED (failing clause named). C12: an accounting
item; nothing FTL is claimed by any outcome.

**Deliverables:** `results/p1085_search_record.md`,
`results/p1085_memo.md`, and (if evaluated)
`results/p1085_results.json` + scripts/checker in
`work/`.

---

## Sequencing

P108-1 … P108-5 run as separate workers with separate
result files; P108-1 and P108-2 share Phase 106 machinery
but write disjoint prefixes. The coordinator re-runs
every checker, integrates verdict sections into this
file INCREMENTALLY, and writes the final synthesis:
per-item verdicts; rung verdicts with **FTL (2a) FIRST**,
then traversable wormhole / 2b / technical results; the
integrated follow-up queue. INTERNAL ONLY.

---

## VERDICTS (integrated incrementally by the coordinator)

### P108-3 — VERDICT: STRUCTURAL FEATURE

(Worker report 2026-11-23; checker `work/p1083_checker.py`
127 passed / 0 failed, re-run by the coordinator.
Deliverables: `results/p1083_run_record.md`,
`results/p1083_memo.md`, `results/p1083_results.json`.)

Point 44 is not an accident. The alignment set (both
force terms live, same strict sign, combined force share
S_F ≥ 0.90, |t_kin|/D_can ≤ 1e-6) was computed on all
seven unique corpus configurations, and the census is
identical in all eight sensitivity cells (S_F ∈ {0.80,
0.90, 0.95} × kinetic ceilings {1e-8, 1e-6, 1e-4}) — no
number rides on a threshold. The two μ = 0 configurations
(A76_mu0, B76_mu0) have empty sets by construction
(F_B ≡ 0). Of the five live-channel configurations:
four (runs_A0, runs_A1 = best_A, runs_B1 = best_B the
hinge best, runs_B2) have the set = {44} exactly, and in
each, point 44 is the configuration's maximum-residual
point (S_F = 1.000000, residual = 1.000000). The fifth,
runs_B0 (μ = +0.0245, the opposite sign regime), has a
25-point set {19…43} carrying its maximum at point 22,
with point 44 flipped to opposition (residual 0.624).
All seven stored EoM max/medians were reproduced within
1e-6 first (worst error 8.6×10⁻¹²).

**Mechanism (derived signature, verified).** The
‘wallwide’ profile is flat (φ ≡ pi0, jets ~1e-49–1e-78)
over the inner shells for EVERY corpus profile, so
□φ ≈ 0 and t_pxx ≈ 0 plateau-wide and S_F ≈ 1 there.
The discriminator is the bed: R_bed > 0 at plateau
points 0–43 and R_bed < 0 only at point 44 (outer points
45–55 share the sign but are off-plateau, S_F ≤ 0.84).
By the derived signature sign(t_FA·t_FB) =
sign(F_A·F_B) (P_X² > 0), alignment on the plateau is
exactly the condition μ·H_,φ(pi0)·R_bed < 0 — so
configurations in one sign regime align only at point
44, and runs_B0 (opposite regime) aligns across the
plateau with point 44 flipped. **The front's
obstruction, in alignment-set form:** on this family's
flat-profile plateau the kinetic term vanishes
identically, so the EoM at plateau points is a pure
force balance; the force terms align wherever
μ·H_,φ(pi0)·R_bed < 0, and at every such point the
residual is the full D_can (residual = 1) — the front
cannot be posed on this profile family without an
alignment point carrying its worst residual, because
the plateau always contains both R_bed signs' boundary
and the alignment condition is a sign condition on
quantities the pose does not tune pointwise.
Grounding note: Phase 106's “0.926” was the single-term
share |t_FB|/D_can; the registered combined S_F at
hinge point 44 is 1.000000, on identical reproduced
terms. Two mechanism-suggested escapes are logged for
the queue: a non-flat profile (kill the plateau, revive
□φ), and H_,φ(pi0) = 0 (kill one force channel's
plateau sign). C12: pre-existing walls; no front moved;
no transport claim.

### P108-2 — VERDICT: FLANK TAX IS STRUCTURAL (LEGALITY CONSERVED LOCALLY)

(Worker report 2026-11-23; checker `work/p1082_check.py`
ALL PASS — 63/63, re-run by the coordinator.
Deliverables: `results/p1082_run_record.md`,
`results/p1082_memo.md`, `results/p1082_results.json`.)

Machinery gates G1–G4 all pass for the wider widths
(G1 rel 2.27×10⁻¹⁶; G3 ∇ρ FD-verified at both widths,
max err ≤5.7×10⁻⁹; G4 12/12). The full negative ladder
(8 amplitudes × widths (5.0, 0.80) and (8.0, 1.20)) ran
at h = 0.3; a negative match existed at each width, so
the positive ladder was not run (registered
disposition). Matched rows (target: band worst-direction
q within ±10% of Phase 106's 32.74): (5.0, 0.80) at
A = −0.04 (target read 31.394 at h = 0.3; 31.980 at
h = 0.15) and (8.0, 1.20) at A = −0.16 (34.390; 35.597).
**Both matched gentler rows pay MORE tax than the
narrow bump, not less.** Against the registered bar
(|Δlegality| < 0.0070 at h = 0.3): the (5.0, 0.80) row
pays Δlegality −0.0558 (8.0× the tax; −0.0500 at
h = 0.15) — its h = 0.3 margins/NEC are actually better
than the best row's, so the verdict fires on the
legality clause alone, and its h = 0.15 margin reverses
anyway (−1.99×10⁻³); the (8.0, 1.20) row pays −0.1227
(17.7×; −0.1340 at h = 0.15) and is worse than the best
row on every tax read at both spacings. Band Type-I at
both matched rows collapses to 0.0138 (vs the narrow
bump's 0.1724); global max-q stays +∞ everywhere.
**Anatomy:** widening spreads the deformation over more
volume and the volume pays proportionally more —
legality falls monotonically down each ladder. The
flank tax is the local form of Phase 83's legality
conservation, not a slope effect. **Anti-loop
consequence, as registered: this verdict DENIES a new
mechanism for a third aimed-deformation registration
from the gentler-flank direction.** Reopening
condition: a matched-target read bought with
|Δlegality| < 0.0070 — no gentler row comes within a
factor 8 of it. C12 as P108-1.

### P108-1 — VERDICT: NO FINITE BAND q IN THE TWO-CENTRE FAMILY

(Worker report 2026-11-23; checker `work/p1081_check.py`
102/102 PASS, re-run by the coordinator. Deliverables:
`results/p1081_run_record.md`, `results/p1081_memo.md`,
`results/p1081_results.json`.)

Machinery gates all pass before any deformed number
(G1 rel 2.27×10⁻¹⁶; G3 the analytic two-centre ∇ρ
FD-verified, max abs err ≤5.2×10⁻⁹; G4 max spread
0.0090; G2 the control fails in kind and reproduces
Phase 106's stored control exactly). **The deciding
fact: band q_values = +∞ at (20.0, π/3) in all 14 rows
at both h** — including rows whose corner Gaussian is
centred exactly on the corner, at both signs and three
widths; the wider reporting band B₊ is likewise +∞
everywhere. The inherited reopening condition (a finite
band q_values at both spacings) is not met by any row,
so **the band-local route CLOSES with that as its
reason**. The corner collapse is centre-proof under
radial rescaling: a deformation that only rescales the
radius at the corner cannot reopen a denominator that
has collapsed there. Control: band worst-direction q
110.4 (h = 0.3) / 121.6 (h = 0.15), band Type-I 0.0276,
legality 0.2099, global max-q +∞. Worst-direction gains
exist but do not survive: the best row (+0.12, 0) reads
qwd 30.41 at h = 0.3 but 892.3 at h = 0.15 (not
ladder-stable), priced at legality 0.2048 and NEC min
−3.04×10⁻³; the only ladder-stable gain, (−0.12, 0) at
qwd 40.02/40.47, is priced at band Type-I 0.0276 →
0.0000. **Every joint two-centre row is worse than the
control on qwd at h = 0.3 (122.6–573.6): the centres
interfere destructively, and Phase 106's A_s = −0.12
gain does not survive adding the corner centre.** The
conditional refinement fired and ran (six rows; doubled
candidates skipped at the |A| ≤ 0.16 cap): all +∞ on
q_values at both h, narrow widths collapsing legality
(0.0157, 0.0060). Second path (audit4) on the four
improving rows confirms B₀ max-q +∞ at (20.0, π/3),
band-feasible False in all — discretisation-
independent. Anatomy restated: the band's two binding
structures are not independently treatable by radial
rescaling — the DEC site's gain is single-centre and
fragile, and the corner's collapse is a denominator
zero that radial rescaling at the site does not move.
C12: prescribed-geometry wall legality at β = 1.1 —
not transport; no legal wall claimed or approached.

### P108-5 — VERDICT: EVALUATED — REOPENING BAR MET (R_net > 1, second-pathed)

(Worker report 2026-11-23; checker `work/p1085_check.py`
281/281 PASS, re-run by the coordinator — the memo's
249/249 was written before the second-path results file
landed; with it present the checker runs 281, as the
memo's own note anticipates. Deliverables:
`results/p1085_search_record.md`,
`results/p1085_memo.md`, `results/p1085_results.json`.)

The documented search (8 queries, primary arXiv full
texts) assessed seven candidates; exactly one is a
genuinely multipartite QET protocol in evaluable form:
**Xun & Ren, arXiv:2410.04919** (N-qubit QET via random
bi-partitioning; single N-qubit resource, N-body
interaction V = 2k σ₁ˣ…σ_Nˣ, Hamiltonian Eqs. (1)–(2),
analytic ground state, closed-form E_in and E_out).
Evaluated under P106-3's inherited accounting verbatim
(definitions fixed in `work/p1085_definitions.md`
before the deciding computation; the N = 2 control
reproduces Phase 72's stored E_out, E_prep^(marg) and
τ_pulse EXACTLY at all three r), the receiving sector
goes negative relative to the uncorrelated reference —
the thing that never happened in the pair protocol —
first at (N, m) = (5, 1). **Bar-clearing rows under
BOTH registered τ conventions** (τ₀ = P72-2's literal
first zero-return; τ_marg = return to the reference
level): (6,1,0.5) R = 2.25/3.20; (8,1,0.5) 3.62/4.68;
(8,1,1) 6.52/11.05; (10,1,0.5) 4.24/5.19; (10,1,1)
9.79/14.34. Two convention-split rows ((5,1,0.5),
(6,1,1)) were excluded from deciding. A from-scratch
dense-matrix second path agrees to <10⁻⁶ on every
deciding quantity at (5,1,0.5), (6,1,0.5), (8,1,0.5),
(8,1,1.0); the N = 10 rows are primary-path
corroboration. **Mechanism:** the shared N-body
interaction's total correlation energy dilutes as
4k²/D ≈ 4k²/(Nh) while single-output extraction stays
O(h); the scalings cross at N = 5. This is NOT the
P106-3 V4 artefact: one receiving sector, one resource,
its FULL correlation energy counted — no per-sector
cost is deleted.
**Caveats, part of the verdict:** (1) the PRICE line
does not fire — total counted price per unit delivered
is 5.59–130.19 (injection-dominated; E_in alone is
19–28× E_out at the r = 0.5 deciding rows); what fires
is the registered R_net pulse-ratio bar itself.
(2) Model scope: a finite spin model under the
programme's own P72-2 pulse construction — not a
quantum-field vacuum pulse; no field-theory Ford–Roman
claim is made. (3) FU-P1085-1 is owed before any use
beyond this phase: independent Gate-style replication
of the τ reads plus a ruling on the τ convention.
The QET line's closure (Phases 83/106) is therefore
REOPENED at its own registered condition, in this
accounting scope only: a multipartite sourcing scheme
whose receiving sector delivers net negative energy
relative to its uncorrelated reference, at R_net > 1,
resource counted. It sources nothing yet — the price
line and the field analogue (FU-P1085-2) stand between
this read and any throat. C12: an accounting verdict;
nothing FTL claimed.

### P108-4 — VERDICT: DYNAMIC ANATOMY — NO RESCUE (both β_p = 1.1 rows)

(Worker report 2026-11-23; checker `work/p1084_check.py`
99/99 PASS, re-run by the coordinator. Deliverables:
`results/p1084_run_record.md`, `results/p1084_memo.md`,
`results/p1084_results.json`.)

Gates: T1 PASS (thickness deviation 0.0 / 1.776×10⁻¹⁵
= 1 ulp at 20; the worker's initial bit-exact bar was
amended to ≤1 ulp as a dated post-hoc amendment in the
run record BEFORE any row ran — no verdict bar
touched); T2 PASS exactly (a = 0 core worst
+1.1949248907449214×10⁻⁵, rel. diff. 0.0 vs Phase 16);
T3 the β_p = 1.1 static twin FAILS (DEC −1.000037,
Type-I 0.185, q = ∞) — no stop triggered.
**Rows.** β_p = 1.1, a = 1.0: binding instant
t = 23.33, quadrant Q3 (displacement < 0, moving
inward), clause DEC −1.000037 on non-Type-I points
(Type-I 0.188 at the binding instant, cycle min
0.154), max q = ∞ at r = 9.5, E_- = −1.222. β_p = 1.1,
a = 2.0: same instant and quadrant, DEC −1.000039
(Type-I 0.223, cycle min 0.140), max q = ∞ at r = 9.0,
E_- = −1.103. Every instant of every row fails (48/48
core worsts < 0); h = 0.15 re-reads confirm both worst
instants. Worst-instant NEC −2.833×10⁻³ / −2.850×10⁻³
vs the static twin's −2.823×10⁻³ — bodily translation
is neutral to ~1% WORSE than the twin, and only
7–19% better than Phase 83's thickness-changing rows,
far from the ≥10× DYNAMICS MOVES bar; max q is ∞ on
both sides. Pulse prices at the worst instant:
8.84×10⁷¹ / 8.76×10⁷¹ at τ = Δ/c; 2.26×10⁷⁴ /
2.24×10⁷⁴ at τ = T. **Controls:** both β_p = 0.1 rows
also fail at every instant (Type-I cycle mins 0.244 /
0.231) despite carrying NO negative Eulerian density
anywhere (E_- = 0.0 exactly at all 24 instants) — on
this bed the failure is carried by the non-Type-I /
flux structure alone, not by negative density.
**Anatomy / closure argument (the worker's F2,
adopted):** on this bed, two orthogonal breathing
modes (thickness-changing, Phase 83; thickness-
preserving, here) × amplitudes × pattern speeds all
fail in the same frozen-geometry way (DEC on
non-Type-I points, max q = ∞); the breathing line on
this bed is closable on structural evidence, with
reopening condition: a wall family whose static
β_p = 1.1 twin has FINITE max q. Follow-up F1 (the
frozen-vs-dynamic ∂_t separation at t = 23.33) is
logged but carries no expectation of rescue. C12:
pattern-speed audit — NOT a transport claim.

---

## PHASE 108 — FINAL SYNTHESIS (coordinator, 2026-11-23)

**Plain language first.** The faster-than-light front
was attacked on four sides and characterised on a
fifth, and the headline is a genuine surprise in the
one place nobody was looking for a wall: the energy-
sourcing books. Squeezing the wall at BOTH of its
binding structures at once does not work — the two
squeezes interfere and make things worse, and the
corner where the flux ratio is infinite cannot be
reopened by any bump centred on it, so that route is
closed for good. Making the squeeze gentler does not
help either: at the same target gain, gentler costs
8–18 times MORE legality, not less — the tax is
structural, and the rules now bar a third try from
that direction. The coupling-force wall's single
deciding point turns out to be a law of the family,
not bad luck: wherever this family's field profile is
flat, the equation is a pure force balance, and the
two forces line up at exactly the point where the
residual is total. A wall that slides back and forth
without changing its thickness fails at every instant
of its cycle, just like the wall that breathes by
thickening and thinning — on this bed, motion buys
nothing. And then the surprise: the quantum-energy-
teleportation trick, closed twice because a pair of
particles can never deliver net negative energy once
the entanglement is paid for, DOES deliver it when
the resource is one state shared by many parties —
because the shared entanglement's cost thins out as
1/N while what one receiver can extract does not.
That reopens a sourcing line at its own pre-registered
condition. It is not an energy source yet — the total
price is still 6–130 times what comes out — and it is
a spin-model accounting result, not new physics in a
field. But it is the first sourcing scheme in the
programme whose books show net negative delivery with
everything counted.

### Rung verdicts (FTL first, as tasked)

- **FTL (2a): NO.** No joint (i) legality +
  (ii) solution-grade improvement at any superluminal
  cell in this phase: the band-local route is closed
  (band q_values +∞ in all 14 two-centre rows at both
  spacings — P108-1); the aimed-deformation direction
  is denied a third registration by its own control
  (the flank tax is structural — P108-2); the
  coupling-force front did not move, though its pin
  is now characterised as a structural alignment set
  (P108-3); thickness-preserving breathing fails at
  every instant at β_p = 1.1 (P108-4). Frontier A
  remains 0.000; every superluminal row remains
  EFFECTIVE ONLY or worse. What changed: three of the
  front's escape routes are now closed on structural
  evidence rather than merely unpromising, and the
  sourcing side (below) reopened.
- **Traversable wormhole: NO as an unqualified
  claim, with one sourcing gap materially changed.**
  No throat was posed or improved. But the QET
  sourcing line — closed in both forms at Phases
  83/106 — is REOPENED at its own registered
  condition: a genuinely multipartite published
  protocol (Xun & Ren, arXiv:2410.04919) delivers net
  negative energy to a receiving sector relative to
  its uncorrelated reference at R_net > 1, resource
  counted, second-pathed (P108-5). The conformal
  member's other gaps (two-mouth pose, formation,
  (V-b)) are untouched; the price line (5.6–130× per
  unit) and the field analogue stand between this
  read and any throat.
- **Practical near-c (2b): NO CHANGE.** No subluminal
  configuration was attempted; the standings are
  untouched. (The β_p = 0.1 breathing controls are
  anatomy on the Phase-16 bed, not near-c standings.)
- **Technical results: YES ×5**, recommended for the
  ledger's GATE-QUEUED tier (internal, ungated):
  (1) the band-local route's closure — the
  (20.0, π/3) collapse is centre-proof under radial
  rescaling and the two centres interfere
  destructively (P108-1); (2) the flank tax is
  structural — legality conservation in local form,
  with the anti-loop consequence stated (P108-2);
  (3) the force-alignment set as the coupling-force
  front's obstruction in exact form (the flat-profile
  plateau + the sign condition μ·H_,φ(pi0)·R_bed < 0)
  (P108-3); (4) thickness-preserving breathing's
  failure anatomy, incl. the β_p = 0.1 controls'
  failure with zero negative Eulerian density —
  failure carried by flux structure alone (P108-4);
  (5) the multipartite QET reopening: net negative
  delivery at R_net > 1 resource-counted in the
  Xun–Ren N-qubit protocol, with its 1/N dilution
  mechanism, its price-line caveat, and its
  spin-model scope (P108-5).

### Integrated follow-up queue (ordered)

1. **FU-P1085-1 — Gate-style replication of the
   P108-5 τ reads** (independent worker, deciding
   rows), the N → ∞ asymptotics of τ, and a ruling
   on the τ₀/τ_marg convention for the FR-net ratio
   in the inherited accounting. Owed before any use
   of P108-5 beyond this phase.
2. **FU-P1085-2 — the field/oscillator analogue:**
   does an N-party FIELD QET with a shared
   interaction show the same 1/N dilution of the
   sector correlation energy? The spin-model read
   does not transfer without it. (Sibling of Phase
   83's FU-P833-1, now with a mechanism to aim at.)
3. **FU-P1085-3 — the separable-minimum reference**
   for the Xun–Ren Hamiltonian, completing the
   price-line bookkeeping in P72-2's exact form.
4. **FU-P1083-1 — the non-flat profile escape:**
   P108-3's first named exit — a profile family with
   no flat plateau (□φ alive at the deciding points)
   posed on the coupling-force front; does the
   alignment set empty, and does the front move?
5. **FU-P1083-2 — the H_,φ(pi0) = 0 escape:**
   P108-3's second named exit — kill one force
   channel's plateau sign and re-read the front.
6. **FU-P1084-1 — the breathing line's reopening
   condition, restated as a search criterion:** any
   future breathing registration requires a wall
   family whose static β_p = 1.1 twin has finite
   max q. FU-P1084-F1 (the ∂_t separation at
   t = 23.33) is logged beneath it, unpromoted.
7. **FU-P106-4a — the ℬ-guided search: STILL
   UNPROMISED**, carried verbatim from Phase 106; it
   runs only under its own future registration.

**Anti-loop compliance:** the band-local route closed
on its own inherited reopening condition failing in a
family built to meet it (P108-1); the gentler-flank
control was run precisely to decide the anti-loop
question and its verdict denies the third revisit
(P108-2); the breathing item was Phase 83's own
registered sibling, run once, and its closure argument
is stated with a reopening condition (P108-4); the
QET item ran only because Phase 106's queue registered
the search and a candidate met its evaluability
condition (P108-5). INTERNAL ONLY — nothing uploaded,
nobody contacted.

## Phase status: CLOSED (2026-11-23)

Deliverables: this checkpoint; `results/` (p1081–
p1085 run records, memos, results JSONs) and `work/`
(scripts + checkers: P108-1 102/102, P108-2 63/63,
P108-3 127/127, P108-4 99/99, P108-5 281/281 — all
re-run by the coordinator). No worker number was
altered by the coordinator.
