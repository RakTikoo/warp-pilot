# FTL Programme — Phase 128 CHECKPOINT (ground record)

**Status:** CLOSED (2026-11-23, coordinator) — all five
items resolved against their pre-registered criteria:
**two JOINT (i)+(ii) IMPROVEMENTS (P128-1, P128-2 — the
programme's first joint improvements on the
coupling-force front, milestones, scan signals under
attack)**, the floor guard posed with its basin
excluded (P128-3), the missing q read produced at +∞
(P128-4), the standing criterion registered (P128-5).
No JOINT PASS anywhere (Frontier A = 0 at every
candidate). Checkers: P128-1 273/275 (two non-passes
resolved on the memo's face), P128-2 230/230, P128-3
183/183, P128-4 12/12 — all re-run fresh by the
coordinator. Verdict sections and final synthesis at
the end of this file. Workers did not edit this file
(P128-1 was recovery-completed by a finisher after its
worker session ended without a report; disclosed on
its memo's face). The Gate for the P108-5/P119-1 QET
claim is Gate-14, the PARENT's line, running
separately — it was NOT duplicated here and nothing in
this phase publishes.

**Mission / sequencing.** Phase 128 executes Phase 119's
integrated follow-up queue, items 2–5 (queue item 1, the
Gate, is the parent's):
`../phase119/CHECKPOINT119.md` §"Integrated follow-up
queue". Mapping: P128-1 = FU-P1194-1 (compose the two
escapes); P128-2 = FU-P1194-2 (the sign-targeted □φ
blend); P128-3 = FU-P1194-3 (the posed |P_X| floor
guard); P128-4 = FU-P1195-1 (produce the missing
whole-shell q read); P128-5 = FU-P1192-1 (the standing
search criterion, registered only). **FU-P106-4a (the
ℬ-guided search) remains UNPROMISED, carried verbatim
from Phase 106 through Phases 108/119, and is NOT run
in this phase** — it runs only under its own future
registration. That statement stands on this phase's
face, as tasked.

**Parent record.** `../phase119/CHECKPOINT119.md` in
full (verdicts + queue); `../phase119/results/
p1194_memo.md` + `p1194_run_record.md` +
`p1194_results.json` (the two halves' poses, best
candidates, pin anatomies, and the failure-protocol
follow-ups this phase executes); `../phase119/results/
p1195_memo.md` + `p1195_results.json` (the criterion
search and the named unread gap); `../phase119/results/
p1192_memo.md` + `p1192_search_record.md` (clauses
(i)–(iii) and FU-P1192-1's registration);
`../phase101/work/p1015_lib.py` + `../phase101/results/
p1015_partB_raw.json` (the front machinery and corpus);
`../phase119/work/p1194_lib.py` + the p1194 drivers and
checker (the halves' machinery, reused not rewritten);
`../phase85/work/p853_lib.py` (`q_values` — the
Phase-63/76 q form, verbatim source for P128-4);
`../phase118/CHECKPOINT118.md` §P118-1 (the β_c = 0
slice — Phase 118 owns it; the boundary discipline
below is live); `~/workspace/compute_allocation.md`.

## Standing orders (binding)

- FAILURE PROTOCOL: anatomy plus at least one
  mechanism-suggested follow-up for every negative;
  closure only on structural evidence with a reopening
  condition.
- ANTI-LOOP RULE: no third revisit of a closed theory
  class without a NEW mechanism. P128-1 is Phase 119's
  registered composition (a new pose — neither half
  re-run); P128-2 and P128-3 are Phase 119's own logged
  follow-ups under their own registrations.
- float64 everywhere; 40-digit mpmath where a deciding
  read demands it (none is pre-registered as demanding
  it in this phase; a worker who finds one states why
  on the face of its run record). Programme venv
  `~/workspace/warp-pilot/venv/bin/python`.
- Published forms only, never gate-fitted; designer
  candidates enter at the ACTION where a theory is
  posed. (The front items pose profiles/constraints on
  a theory already fixed by the P101-5B action, exactly
  as Phase 119 did.)
- Solution-grade reads on the non-degenerate front
  (Phase 79 standard): content set and degenerate
  count stated on every front read; a vacuous point is
  never a passed point.
- Full-volume all-directions NEC + full-EC + Type-I
  bars wherever a CONFIGURATION is audited (the front
  reads are the registered subset form of that bar, as
  in Phases 79/101/106/108/118/119 — margins + Type-I +
  the canonical EoM read together; margins alone never
  decide).
- **Legality/health bars exactly as Phases 108/119
  registered them. No bar moves.**
- **BOTH median and max forms reported on every front
  read** (Phase 89's scope honesty, carried verbatim).
- **Phase-118 boundary discipline:** the β_c = 0 slice
  is Phase 118's. Any constrained search in this phase
  keeps |β_c| ≥ 0.05 at any deciding candidate; a
  trajectory pressing the fence is reported as
  PRESSING THE PHASE-118 BOUNDARY and the read stops
  at the fence — the slice is not entered, re-run, or
  re-judged here (Phase 119's halves stopped at
  |β_c| = 0.4709 closest approach; the fence is 0.05).
- Bars pre-registered here; amendments appended,
  dated, marked post-hoc, never silently broadening a
  pass.
- ADVERSARIAL PROTOCOL: any positive gets an
  independent second path before integration (the
  full-margins `fast=False` recomputation on the
  `p1015_checker.py` pattern for front positives).
- EVIDENCE RULE + grounding bar, stated on each item's
  face.
- OPTIMIZATION DIRECTIVE + RIDER + FREE-COMPUTE RULE:
  approved pools only per
  `~/workspace/compute_allocation.md`; any run expected
  over ~2 h continuous is checkpointed and routed, not
  left uncheckpointed on this VM. (No item in this
  phase is expected to approach that bound; a worker
  whose run grows states so and checkpoints. The
  P119-4 searches are the timing pattern.)
- UNIQUENESS PROTOCOL: no claim in this phase is
  called unique/first/record beyond the registered
  verdict language; a joint pass is the programme's
  first *on this front*, stated exactly so, and is a
  scan signal under attack until a later Gate.
- C12 accounting on every number.
- LANGUAGE: any pass is a "scan signal under attack"
  until a later Gate verifies it.
- INTERNAL ONLY: nothing uploaded, nobody contacted.

---

## The registered front (the comparison, fixed — inherited verbatim from §P119-4)

The front: Phase 48 bed at β = 1.1, the 56-point
subset, the hinge theory of P101-5 Part B (action and
canonical EoM exactly as registered there; machinery
`../phase101/work/p1015_lib.py`: `canonical_terms` —
t_kin = □φ, t_pxx, t_FA = F_A/P_X with
F_A = ½·H_,φ(φ)·R_bed, t_FB = F_B/P_X with
F_B = −μφ; D_can = Σ|terms|; non-degenerate iff
D_can ≥ 1e-9; `read` for subset legality / EoM reads /
health / Frontier A). H(φ) = 1 − ξφ² + β_cφ/2 −
β₂φ²/2, H_,φ(φ) = −(2ξ+β₂)φ + β_c/2. z = (ξ, β_c, β₂,
pi0, shape, p₁, p₂, μ).

The P101-5B hinge best (family B, start 6): z =
(2.756667559450937, −1.498683175695639,
0.7811507949670238, 0.3385988091052908,
0.870145941019083, 1.222294121969537,
0.0639057960421364, −0.15512773896022752),
ρ₀ = 0.046611949162594764; subset_legal =
0.5892857142857143; EoM rel max (nondeg) =
0.9999999999784565; median = 0.22437629566157347;
n_nondeg = 56, n_deg = 0; health_ok = False;
Frontier A = 0.000. Alignment set at the hinge best
(Phase 108 definition, thresholds verbatim: both force
terms live at ≥ 1e-6 × max|term|, same strict sign,
S_F = (|t_FA| + |t_FB|)/D_can ≥ 0.90,
|t_kin|/D_can ≤ 1e-6): {44}, S_F = 1.000000, point 44
the maximum-residual point.

**Machinery gate (before any front item's deciding
read; each front worker runs it or cites a same-phase
run of it).** Reproduce, via `p1015_lib.canonical_terms`
on `../phase101/results/p1015_partB_raw.json`: all
seven unique corpus configurations' stored EoM
max/medians within 1e-6 (Phase 119's worst error was
8.55×10⁻¹²), and the hinge best's alignment set = {44}
under the registered definition. Failure = MACHINERY
FAILURE (gate named); no deciding read is taken on
unvalidated machinery.

**Bars (all front items, inherited verbatim from
§P119-4).**
- **JOINT PASS (the programme's first on this front):**
  a candidate, second-pathed (full-margins
  recomputation, fast=False, on the `p1015_checker.py`
  pattern), with Frontier A > 0 in `p1015_lib.read`'s
  exact sense (subset_legal > 0 AND
  eom_rel_max_nondeg ≤ 0.02 AND health_ok) AND
  n_nondeg ≥ 28 (the vacuity fence of P118-1, adopted
  verbatim) AND the trap not firing (trap gate
  verbatim: max over subset of |F_A + F_B| < 1e-9, or
  the trap subspace, at the deciding candidate =
  KILLED BY THE TRAP).
- **JOINT IMPROVEMENT (milestone):** a candidate,
  second-pathed, Pareto-dominating the hinge best on
  (subset_legal, eom_rel_max_nondeg):
  subset_legal ≥ 0.5892857142857143 AND
  eom_rel_max_nondeg < 0.9999999999784565, OR
  subset_legal > 0.5892857142857143 AND
  eom_rel_max_nondeg ≤ 0.9999999999784565.
- Partial movements (median moves, single-clause moves)
  are reported as anatomy, not as milestones.
C12: pre-existing walls at β = 1.1; no transport
claim; a moved front is not a legal wall.

**Reads (every front item, at its best candidate and
at its seeded starts).** `p1015_lib.read` in full:
subset_legal, EoM rel max/median on the non-degenerate
set, n_nondeg / n_deg, health_ok, Frontier A; the
alignment set under the registered definition, its
members' terms and shares; whether the
maximum-residual point is in the set; the
term decomposition at the maximum-residual point.
Every read states its content set (Phase 79 standard).

---

## P128-1 (FU-P1194-1) — COMPOSE THE TWO ESCAPES

**Grounding.** Phase 119's two halves have
complementary binding forms (CHECKPOINT119 §P119-4
verdict; `p1194_memo.md` failure protocol, follow-up
1, quoted in substance): half (a)'s non-flat profile
emptied the alignment set but re-pinned as the
**all-sign pin** — at its best candidate's worst point
(51; tie set 44/50/52) all four canonical terms share
one strict sign, the revived □φ joining the pin
instead of opposing it; half (b)'s H_,φ(pi0) = 0
constraint emptied the alignment set but re-pinned as
the **single-channel pin** — with t_FA dead and
□φ ≡ 0 on the plateau, the EoM there is t_FB alone,
rel = 1 across the whole plateau. The memo's stated
mechanism: "Half (b) shows t_FB needs an opposing live
channel at plateau points; half (a) shows □φ can be
that channel but joined the pin at the searched
candidates. The composed pose is the direct test of
whether a live □φ of the *opposing* sign is attainable
at the pin points." This item is that test. It is a
new pose (the composition), not a re-run of either
half — anti-loop compliance on its face.

**Pose (fixed here, before numbers).** The same
theory, bed, and 56-point subset. The scalar profile
is half (a)'s registered blend, verbatim in form:

  φ(r) = φ_ww(r; pi0, shape)
         + A · W(r) · sin(2π (r − 10)/λ),

φ_ww the stored 'wallwide' profile
(`p182_engine.pi_splines`), W the smootherstep window
of `p1194_lib.py` / the Phase-79 counterweight pattern
(W = 0 below r = 10, 1 on [11.25, 18.75], 0 above
r = 20); A ∈ [−0.35, 0.35], λ ∈ [2.0, 6.0]; jets by the
PhiProfile pattern (CubicSpline on the 4001-point grid,
FD-verified at rel agreement < 1e-6 before any read),
exactly as in `p1194_halfA.py`. AND half (b)'s
constraint imposed by parametrisation, verbatim:
H_,φ(pi0) = −(2ξ+β₂)·pi0 + β_c/2 = 0, i.e. pi0
eliminated, pi0 = β_c / (2(2ξ+β₂)), 2ξ + β₂ ≠ 0 —
the plateau value sits at the force derivative's
root, so t_FA = 0 at every plateau point exactly,
while the blend keeps □φ alive there. Guards verbatim
from `p1194_run_record.md` §3: a large penalty residual
fires if |2ξ+β₂| < 0.2 or if the eliminated pi0 leaves
[0.02, 2.9]; deciding candidates must satisfy both
strictly. Two β_c branches, β_c ∈ [−4, −0.05] and
[0.05, 4] (the Phase-118 fence |β_c| ≥ 0.05 is a hard
boundary of this pose, per the standing orders).

**Registered operational non-flatness (inherited):**
at the posed configurations, |t_kin|/D_can > 1e-6 at a
MAJORITY of the former plateau points (subset indices
0–43). A candidate failing this has not posed the
composition and the item reports exactly that.

**Search.** Joint least-squares on the P101-5 Part B
pattern (residual in `p791_main`'s form, as coded in
`p1015_partB.residuals` and reused by the p1194
drivers) over (free z with pi0 eliminated, A, λ,
family-B fluid ρ₀ ∈ [0, 0.05]); bounds for z are the
P101-5B LO8/HI8 with pi0's slot removed; max_nfev = 150
per start (P101-5B pattern), checkpointed. ≥ 12 starts,
including at minimum: (i) half (a)'s best candidate
re-posed under the constraint (its z projected onto
the constraint set by the §3 projection pattern, its
(A, λ) carried); (ii) half (b)'s best candidate
re-posed on the blend at several (A, λ) seedings
including (0.15, 3.0) and half (a)'s best
(−0.033678153095735734, 4.640050126789908);
(iii) the hinge best projected onto the constraint set
and blended. Family A also read at the best candidate
(same z, no fluid), as in both halves.

**Reads.** The standing front reads (above) at the
best candidate and at each seeded start, PLUS the
composition's deciding anatomy: at the best
candidate's maximum-residual point, the signed term
decomposition with shares, stating explicitly whether
t_kin opposes t_FB there (the memo's question) and
whether t_FA is at its posed zero.

**Verdicts (only these).**
- **JOINT PASS** (the programme's first on this
  front): the inherited JOINT PASS bar met,
  second-pathed. IMMEDIATE milestone report on
  landing.
- **JOINT (i)+(ii) IMPROVEMENT** (milestone): the
  inherited JOINT IMPROVEMENT bar met, second-pathed.
  IMMEDIATE milestone report on landing.
- **COMPOSITION WORKS MECHANICALLY, FRONT STANDS:**
  the composed pose is posed as registered
  (non-flatness test passed; t_FA at its posed zero at
  plateau points) and neither bar is met — the
  composition's own binding form is NAMED (a third pin
  form is a result, stated with its deciding term and
  the max-residual point's full decomposition).
- **ESCAPE FAILS (composition form):** the composed
  pose cannot be posed as registered, or an alignment
  set in the registered sense re-forms carrying the
  maximum-residual point — the re-forming mechanism
  named (including any P_X → 0 blow-up re-formation,
  cross-referenced to P128-3).

**Deliverables:** `results/p1281_run_record.md`
(pose + seeds fixed before numbers),
`results/p1281_memo.md`, `results/p1281_results.json`;
scripts + independent checker in `work/` (checker
recomputes every verdict-carrying number from the
results file; any claimed pass/improvement is
second-pathed by the full-margins recomputation
before the memo calls it).

---

## P128-2 (FU-P1194-2) — THE SIGN-TARGETED □φ BLEND

**Grounding.** `p1194_memo.md` failure protocol,
follow-up 2, verbatim in substance: "a blend whose □φ
changes sign across the inner shell (more zero
crossings than the single-sine family searched), posed
so the kinetic term opposes −μφ at the radii where the
pin migrates (outer shell, points 44–55, in half (a))."
Half (a)'s pin migrated to the outer shell: worst
point 51, tie set {44, 50, 52} within 1e-9, all four
terms one strict sign (t_kin = +0.07653, t_FB =
+0.06008 at point 51). The kinetic term opposed
nothing because the single-sine blend's □φ sign at
those radii was the pin's sign. This item registers
the blend's □φ sign at the pin points as a POSED
TARGET, fixed before running.

**Pose (fixed here, before numbers).** Same theory,
bed, subset; NO H_,φ constraint (this is the blend
item on the plain front; pi0 is a free variable of z
as in half (a)). The profile is a multi-component
blend on the same window W:

  φ(r) = φ_ww(r; pi0, shape)
         + W(r) · Σ_{k=1..K} A_k · sin(2π (r − 10)/λ_k + φ_k),

with K ≥ 2 components (the registered difference from
half (a): more zero crossings of □φ across the shell
than the single sine affords), A_k ∈ [−0.35, 0.35],
λ_k ∈ [2.0, 6.0], φ_k ∈ [0, 2π). The worker's run
record fixes K and any further restriction of the
envelope BEFORE numbers; jets by the PhiProfile
pattern, FD-verified as in P128-1. A stated closed-form
alternative with ≥ 2 □φ zero crossings across the
shell may replace the sum-of-sines ONLY if the run
record registers it before numbers and states why it
meets the memo's description at least as directly.

**The sign target (registered, checked as a posed
property — not assumed).** At the named pin points —
subset indices 44–55 (the outer-shell band of half
(a)'s migrated pin), with the tie set {44, 50, 51, 52}
named — the posed candidate's kinetic term must
OPPOSE the FB force term: sign(t_kin) = −sign(t_FB)
at a MAJORITY of the named pin points where both
terms are live (|t| ≥ 1e-6 × max|term| at the point).
The targeting read is reported at the best candidate
and at the seeded starts whether or not it is met:
a candidate meeting the target is TARGETED; the
search below is run over the full envelope regardless
(the target is a read, and additionally the worker
runs ≥ 4 starts SEEDED from targeted constructions —
initial (A_k, λ_k, φ_k) chosen so the seed itself is
targeted at the hinge couplings, the construction
stated in the run record).

**Search.** Joint least-squares on the P101-5B
pattern over (z, blend parameters, ρ₀ ∈ [0, 0.05]),
family B; ≥ 12 starts including the hinge best
re-posed on the blend and the ≥ 4 targeted seeds;
max_nfev = 150 per start, checkpointed. Family A read
at the best candidate. The trap gate applies verbatim
at any deciding candidate.

**Reads.** The standing front reads, PLUS the
targeting read (above) and the term decomposition at
the maximum-residual point with the t_kin vs t_FB
sign relation stated.

**Verdicts (only these).**
- **JOINT PASS** / **JOINT (i)+(ii) IMPROVEMENT**: the
  inherited bars, second-pathed. IMMEDIATE milestone
  report on landing.
- **TARGET MET, FRONT STANDS:** a targeted candidate
  exists (the sign target met at its pin points) and
  neither bar is met — the binding form at the
  targeted candidate's worst point is named (whether
  the pin re-forms elsewhere, the legality↔EoM trade
  binds, or another named form).
- **TARGET UNATTAINABLE IN THE ENVELOPE:** no searched
  candidate meets the sign target at its pin points —
  the obstruction to targeting is named (which term's
  sign the blend cannot control at those radii, and
  why — a structural statement about the blend family
  and the bed, not a search-size complaint).
- **ESCAPE FAILS:** the alignment set (registered
  definition) re-forms carrying the maximum-residual
  point at the best candidate — mechanism named.

**Deliverables:** `results/p1282_run_record.md`
(blend form, K, targeting construction fixed before
numbers), `results/p1282_memo.md`,
`results/p1282_results.json`; scripts + independent
checker in `work/`.

---

## P128-3 (FU-P1194-3) — THE POSED |P_X| FLOOR GUARD

**Grounding.** `p1194_memo.md` failure protocol,
follow-up 3, verbatim: "**P_X floor as a posed guard**:
exclude the P_X → 0 basin (start 8, half (b))
explicitly in future searches on this front (|P_X| ≥
a stated floor at all subset points), so
alignment-by-blow-up cannot re-enter through the
denominator." The anatomy it guards against (half (b),
start 8, not its best candidate): an alignment set
{19} carrying its max-residual point (rel = 1.0
exactly) formed NOT via H_,φ but via P_X at point 19
= 1.73×10⁻⁸, blowing both force terms up by the 1/P_X
division (t_FB = −1.82×10⁵, t_FA = −1.99×10², same
sign, S_F = 0.99972); the configuration is a
P_X-crossing one (PX_min = −1.15×10⁻⁵,
health_ok = False).

**The guard (registered here, before numbers).** The
floor is **|P_X| ≥ 1.0×10⁻⁴ at every one of the 56
subset points**, evaluated on the posed configuration
through the same P_X the canonical EoM divides by
(`p1015_lib`'s P_X at each subset point). The floor's
size is fixed by the anatomy, not tuned: it sits
~4 orders above the exhibited blow-up value
(1.73×10⁻⁸) and above the exhibited crossing minimum
(|−1.15×10⁻⁵|), so the exhibited basin is excluded
with margin, while no stored corpus or half-(a)/(b)
best candidate comes near it (the worker verifies
this last clause on the stored configurations as part
of the deliverable — if any stored best candidate
violates the floor, that is reported as a finding
about the floor, and the floor does NOT move in this
phase; the item reports and the queue re-registers).

**Pose.** The guard is posed on half (b)'s constrained
pose — the pose where the blow-up anatomy was
exhibited: stored 'wallwide' family, H_,φ(pi0) = 0
imposed by parametrisation (pi0 eliminated; guards
|2ξ+β₂| ≥ 0.2, pi0 ∈ [0.02, 2.9]; two β_c branches
with the |β_c| ≥ 0.05 Phase-118 fence), PLUS the
floor as a hard feasibility condition of the search:
the implementation (penalty residual, barrier, or
candidate rejection) is stated in the run record
BEFORE numbers, and any DECIDING candidate is
verified to satisfy |P_X| ≥ 1.0×10⁻⁴ at all 56 points
by direct evaluation in its read — a candidate whose
read does not include the floor verification carries
no verdict. Search: joint least-squares on the
P101-5B pattern, ≥ 12 starts including half (b)'s
best candidate and half (b)'s start 8 itself (the
exhibited blow-up configuration, re-posed as a seed:
the guard's exclusion of its basin is demonstrated,
not asserted). max_nfev = 150 per start, checkpointed.
Family A read at the best guarded candidate.

**Reads.** The standing front reads at the best
guarded candidate and the seeded starts, PLUS, at
every read: min over subset of |P_X| and its argmin;
the start-8 seed's disposition under the guard (its
floor violation stated numerically); and whether any
alignment set in the registered sense carries the
maximum-residual point at the best guarded candidate,
by ANY mechanism.

**Verdicts (only these).**
- **JOINT PASS** / **JOINT (i)+(ii) IMPROVEMENT**
  under the guard: the inherited bars, second-pathed,
  floor verified. IMMEDIATE milestone report.
- **GUARD POSED — BLOW-UP BASIN EXCLUDED, FRONT
  STANDS:** the guard is posed as registered (start-8
  basin numerically outside the guarded feasible set),
  the guarded search completes, neither bar is met —
  the guarded best candidate's binding form named
  (expected candidate: the single-channel pin of half
  (b), restated only if the read shows it).
- **GUARD BINDS:** the floor excludes configurations
  the unguarded search preferred (named: which stored
  or searched candidates violate it, and the guarded
  optimum's cost on (subset_legal, eom_rel_max_nondeg)
  against half (b)'s best) — the guard's price is the
  deliverable, with the front's verdict under it
  stated.
- **MACHINERY FAILURE** (gate named).

**Deliverables:** `results/p1283_run_record.md`
(guard implementation fixed before numbers),
`results/p1283_memo.md`, `results/p1283_results.json`;
scripts + independent checker in `work/` (the checker
re-evaluates the floor at every reported candidate
from its stored z, independently of the search code).

---

## P128-4 (FU-P1195-1) — PRODUCE THE MISSING WHOLE-SHELL q READ

**Grounding.** Phase 119's P119-5 verdict (NOT MET IN
OUR SEARCH): no family in the stored record meets
P108-4's breathing reopening criterion — a stored
whole-shell static β = 1.1 / β_p = 1.1 read with
FINITE max q, q in the Phase-63 form. The Phase 48 bed
/ coupling-force front family is the named UNREAD gap:
"its β = 1.1 reads are EoM/subset/Frontier-A form;
absence checker-verified" — no whole-shell static
β = 1.1 max-q read of that family exists. P119-5's
follow-up, verbatim in substance: "reopening still
requires first PRODUCING the missing read — a
whole-shell static β = 1.1 q audit of a never-q-read
family, the coupling-force front family being the
named candidate — and finding it finite." This item
produces the read. It runs NO breathing and poses NO
new wall.

**The q form (fixed, verbatim source).** Per-point
q = max over 162 directions n̂ of
2|T_0n̂| / (T_00 + T_n̂n̂), in the orthonormal frame;
q = +∞ at a point where the denominator ≤ 0 with
nonzero flux; q = 0 where denominator ≤ 0 and
|flux| < 1e-300. Source: `phase76/p763_lib.py` as
carried verbatim in `../phase85/work/p853_lib.py`
(`q_values`, `_dirs162`). The family's max q is the
maximum over the whole-shell sample.

**Control (before the family's read is believed).**
The worker's q machinery reproduces a stored control
read in the same form: the (10,30) family's static
β = 1.1 whole-sample max q = +∞ as stored (Phase 83 G3
/ `phase85/results/p853_results.json` static row), OR
another stored whole-shell q read the worker names in
the run record, reproduced to its stored value (a
finite control value to ≤ 1e-6 relative; a +∞ control
by exhibiting the denominator-collapse point). Failure
= MACHINERY FAILURE (control named); the family's read
is not taken on unvalidated machinery.

**The family's static form (fixed here).** The
coupling-force front family's stored static β = 1.1
configurations are the seven unique corpus
configurations of `../phase101/results/
p1015_partB_raw.json` (each: a z, its profile, its
family fluid) on the Phase 48 bed — the family's
complete stored static set at β = 1.1. The read is
taken on EVERY one of the seven (the criterion speaks
of the family's read; a single-configuration read
would leave the family unread in exactly the way
P119-5 priced). The hinge best is among them and is
reported individually as well.

**The whole-shell sample (fixed here).** The bed's
full shell volume in the same form as the stored
(10,30) reads: the radial × angular sample of
`p853_lib`'s verdict-point construction adapted to
the bed's shell radii (the radii and point count
stated in the run record, derived from the bed
machinery — `p1015_lib` / the Phase-48 bed definition
— not invented); the 56-point subset is NOT the
sample (it is a subset read, and P119-5's scope
discipline excludes subset reads from the criterion).
The stress tensor at each sample point is the posed
configuration's full stress (scalar sector + coupling
+ family fluid, as the front's own machinery assembles
it — the worker states the assembly and validates it
against the front's stored subset reads: the
configuration's EoM/subset behaviour reproduced from
the assembled stress where the two overlap, or the
difference stated exactly).

**Reads.** Per configuration: whole-shell max q (a
finite number or +∞), the argmax point and, for a +∞
read, the deciding denominator-collapse point(s)
(r, direction, T_00 + T_n̂n̂, flux) in P119-5's anatomy
form; the family's disposition stated per
configuration and jointly.

**Verdicts (only these).**
- **FINITE — CRITERION'S LETTER MET:** at least one
  stored static configuration of the family reads a
  FINITE whole-shell max q at β = 1.1. The read itself
  is the deliverable; the verdict states exactly what
  follows and what does not: P108-4's reopening
  criterion is met BY THAT FAMILY on its letter, so
  the breathing line's search reopens on its own
  terms (a breathing registration on that family
  becomes posable for the queue) — and nothing more:
  no breathing is run, no wall's legality is claimed,
  the finite q is a flux-ratio read, not a legality
  pass. IMMEDIATE report on landing (it changes a
  closed line's status).
- **+∞ — CLOSURE EVIDENCE EXTENDED:** every stored
  static configuration reads max q = +∞, with the
  deciding anatomy stated (denominator collapse, its
  location) — the criterion's search now closes on a
  read, not on an absence, for this family.
- **MACHINERY FAILURE** (control or assembly named).

**Deliverables:** `results/p1284_run_record.md`
(sample construction + stress assembly + control,
fixed before the family's numbers),
`results/p1284_memo.md`, `results/p1284_results.json`;
scripts + independent checker in `work/` (checker
recomputes the max-q reads from the stored
configurations and the run record's sample definition,
independently of the evaluation script).

---

## P128-5 (FU-P1192-1) — THE STANDING SEARCH CRITERION, REGISTERED ONLY

**Registration-only item. No search is run in this
phase.** The criterion is recorded here verbatim, as
tasked; recording it IS the deliverable.

The criterion (Phase 119, §P119-2, clauses (i)–(iii),
verbatim):

> (i) a field or harmonic-oscillator QET protocol —
> Hamiltonian and ground state printed; (ii) its
> delivered energy at a receiving sector/region in
> printed form; AND (iii) a multipartite /
> multi-receiver / shared-resource structure in print
> in which an N-scaling of the sector correlation
> energy vs the per-receiver extraction can be read.

The reopening condition (Phase 119, integrated
follow-up queue, item 5, verbatim):

> **FU-P1192-1 — standing search criterion:** the
> field/oscillator analogue reopens only on
> publication of a field/oscillator QET meeting
> clauses (i)+(ii)+(iii) of §P119-2. No active work;
> the criterion is the deliverable.

And in the form Phase 119's synthesis states it: a
future publication of a multipartite field/oscillator
QET meeting clauses (i)+(ii)+(iii) reopens P119-2's
line. Phase 119's verdict stands behind it: clauses
(i)+(ii) ARE met in print (cleanly by Nambu & Hotta's
harmonic chain, arXiv:1007.2234); clause (iii) is met
nowhere in the published record assessed there (11
candidates, 13 logged queries); the missing
ingredient is named exactly in §P119-2's verdict. Any
future reopening under this criterion runs under the
inherited accounting verbatim (P72-2 §§3–4 via
P106-3) with the inherited reopening bar: **any
variant with R_net > 1 resource-counted** — and any
positive is a scan signal under attack with the
spin-to-field scope stated on its face.

**P128-5 VERDICT: REGISTERED** (complete on
registration, 2026-11-23, coordinator). No search was
run; no literature state is claimed beyond Phase
119's documented search.

---

## Sequencing

P128-1 … P128-4 run as separate workers with separate
result files, in parallel where their machinery is
independent (all four reuse stored machinery but write
disjoint files; P128-3's pose is independent of
P128-1's outcome by its registration). A JOINT PASS or
JOINT IMPROVEMENT in P128-1/-2/-3, or a FINITE verdict
in P128-4, is reported IMMEDIATELY on landing, before
the phase's other items complete. The coordinator
re-runs every checker, integrates verdict sections
into this file INCREMENTALLY, and writes the final
synthesis: per-item verdicts; rung verdicts with
**FTL (2a) FIRST**, then traversable wormhole / 2b /
technical results; the integrated follow-up queue.
INTERNAL ONLY.

## Dispatch log

- 2026-11-23: Coordinator grounded in Checkpoints 101
  (front machinery + corpus), 108 (P108-3 alignment
  law, P108-4 closure + criterion, P108-5), 118
  (§P118-1 boundary), 119 (all five verdicts +
  integrated queue), the P119-4 memo/run record/results
  (poses, best candidates, both pin anatomies, the
  start-8 blow-up anatomy, the three failure-protocol
  follow-ups), the P119-5 memo (survey + named gap),
  and the Phase-63/76 q form as carried in
  `phase85/work/p853_lib.py`. Registrations above
  written before worker dispatch. P128-5 completed on
  registration (above).
- 2026-11-23: Workers dispatched for P128-1, P128-2,
  P128-3, P128-4 (parallel; disjoint result files;
  each brief carries its registration, the machinery
  gate, the verbatim bars, and the immediate-report
  duty on a milestone / FINITE q verdict). No number
  exists yet for any of the four and none is to be
  inferred.

---

## VERDICTS (integrated incrementally by the coordinator)

### P128-1 — VERDICT: JOINT (i)+(ii) IMPROVEMENT (MILESTONE)

(Recovery-completed: the original worker session ended
without a final report; the item was finished by a
recovery finisher from the checkpointed disk state —
16 starts (0–15), none dropped — with the recovery,
the first pass's start-0 broadcast error and its
fixed-shape-penalty fix disclosed on the memo's face.
Checker `work/p1281_checker.py` 273/275 PASS, re-run
fresh by the coordinator, including `verdict_form`
recomputed = JOINT (i)+(ii) IMPROVEMENT; the two
non-passes are one resolved discrepancy, below.
Deliverables: `results/p1281_run_record.md`,
`results/p1281_memo.md`, `results/p1281_results.json`.)

**The composed pose produces the programme's first
joint (i)+(ii) improvement on this front** — stated
exactly so, and a scan signal under attack until a
later Gate. The best candidate (start 2: half (b)'s
best re-posed on the blend at half (a)'s best
(A, λ) = (−0.04538543038954925, 4.635264154193024);
z and ρ₀ in the memo) Pareto-dominates the hinge best
on the registered pair under BOTH clauses:
subset_legal = **0.9285714285714286** (search read) /
**0.9464285714285714** (full-margins second path,
53/56) vs hinge 0.5892857142857143, AND EoM rel max
(nondeg) = **0.999981215379503** < hinge
0.9999999999784565. Starts 1 and 4 also individually
Pareto-dominate. Machinery gate PASS (worst corpus
error 8.549×10⁻¹²; hinge alignment set = {44}).

**Sizes, stated honestly.** The legality coordinate
moved hugely (0.589 → 0.929/0.946). The EoM-max
coordinate moved strictly but thinly
(0.9999999999784565 → 0.999981215379503, a 1.9×10⁻⁵
move; all 16 runs ≥ 0.9997581070983811) — the residual
at the worst point is still ≈ the full D_can. **It is
NOT a JOINT PASS:** Frontier A = 0.0 at the best
candidate and in all 16 runs (health_ok = False at the
best; the EoM max is far above the 0.02 pass clause).
The **median worsened** (0.47963896879690177 vs hinge
0.22437629566157347) — reported as anatomy; the
registered bar is the (legal, max) Pareto pair.
Content set 56 points, n_nondeg/n_deg = 56/0 at the
best candidate; alignment set EMPTY; trap does not
fire (Fsum_maxabs = 0.1322); non-flatness posed
everywhere (44/44 former plateau points at every run);
Phase-118 fence not pressed (closest |β_c| =
0.053131893737917754, start 8; the slice never
entered). Family A at the best candidate: legal 0.0 —
the improvement is a family-B (fluid-carrying) result.

**Deciding anatomy (the memo's question, answered).**
At the best candidate's maximum-residual point 44
(tie set {44} alone; D_can = 0.07853704458077647):
t_FB = +0.06926043659593377 (share 0.881882),
t_kin = □φ = +0.009273557882887383 (share 0.118079),
t_FA = +2.31×10⁻⁶ (H_,φ(pi0) = 0.0 exactly by the
parametrisation — the posed zero holds), t_pxx
negligible. **t_kin does NOT oppose t_FB there** —
both strictly positive; the live □φ joins the pin.
**Binding form (named): the single-channel FB pin at
the migrated worst point** — half (b)'s pin re-formed
one point out, at 44, with the composition's added
channel carrying the pin's own sign. The composition
works mechanically (both escapes posed simultaneously;
both registered pins removed as posed) and the front
moved on the improvement bar, but the EoM clause's
obstruction is exhibited at a point, not shown
structural — closure is NOT claimed. The direct
attack on the deciding fact (t_kin same-sign as t_FB
at the worst point) is this phase's own P128-2, which
poses the □φ sign at the pin points as a target.

**Checker resolution (on the memo's face).** The two
non-passes (`run2_legal`, `seed2_legal`) are the same
one-point discrepancy: at subset point 51 the search
path's fast margins return NaN (recorded −1.0, illegal)
while the full-margins computation returns all four
margins positive but tiny (run 2: DEC 5.69×10⁻⁶;
seed 2: DEC 6.90×10⁻⁶). The registered second path is
the full-margins one; the difference is exactly 1/56
in the conservative direction for the stored search
reads, which are left as computed. No verdict-carrying
number fails under the second path.

### P128-2 — VERDICT: JOINT (i)+(ii) IMPROVEMENT (MILESTONE)

(Worker report 2026-11-23; checker `work/p1282_checker.py`
230/230 PASS, re-run fresh by the coordinator —
`verdict_form` recomputed = JOINT IMPROVEMENT, the
best candidate second-pathed by full-margins
recomputation. Deliverables:
`results/p1282_run_record.md`, `results/p1282_memo.md`,
`results/p1282_results.json`. Process on the memo's
face: the seed construction was OOM-killed once and
two search ranges were killed by a service restart;
all resumed via checkpointing — 15 starts completed as
registered, none dropped.)

**The sign-targeted blend produces the phase's second
joint improvement on this front, with a materially
larger EoM move than P128-1's** — a scan signal under
attack until a later Gate. Best candidate (start 12,
a random start; K = 3 blend; z, blend parameters and
ρ₀ = 0.04987930769917497 in the memo):
subset_legal = **0.7857142857142857** (independent
read identical) vs hinge 0.5892857142857143, AND EoM
rel max (nondeg) = **0.9980625645582593** vs hinge
0.9999999999784565 — a 1.94×10⁻³ move, ~100× P128-1's
1.9×10⁻⁵ — AND the median also improved
(0.14496 vs hinge 0.22437629566157347), unlike
P128-1. Both Pareto clauses met. **NOT a JOINT PASS:**
Frontier A = 0 (health_ok = False — the cr2 clause;
H_min = 0.469, PX_min = 2.784), trap not firing
(Fsum_maxabs = 0.1511), alignment set empty, content
set 56 points, n_nondeg/n_deg = 56/0. Family A at the
best candidate: legal 0.000 — again a family-B
(fluid-carrying) result.

**The sign target: MET, and generic.** At the hinge
couplings, 2288/6027 construction-pool vectors were
target-eligible; all 4 targeted seeds read named 4/4
and band 12/12 opposed at their search initial reads;
9/15 optimised candidates are targeted. The blend's
□φ part has 9 zero crossings at the best profile vs 7
for half (a)'s single-sine reference. **But the best
candidate is NOT itself targeted** (named 1/4): its
worst point is 52, a named pin point, where the pin
re-formed as a **kinetic pin** — t_kin = +0.08721
(share 0.843) dominating and same-sign as t_FB =
+0.01613 (share 0.156). And the best TARGETED
candidate (start 5: legal 0.5357, EoM max 0.99970)
achieved opposition at 50/51/52 exactly as posed —
and its worst point migrated to **44, the one
unopposed named point**, as an FB-dominated pin
(t_FB share 0.854, t_kin share 0.064, same sign
there). The pattern across both: **the pin migrates
to whichever named point the opposition does not
cover** — opposition at a point works; coverage is
the binding constraint. Secondary anatomy: start 11
re-formed an inner-shell alignment set
{17, 18, 19, 21, 28–36} not carrying its max point.

**Failure-protocol follow-ups (logged in the memo):**
target r = 14.75 (point 44's radius) directly, so the
opposition covers the migration target; iterate the
target onto the migrated pin; a posed cr2 guard for
the health clause (both of this phase's improvements
fail health on it). Closure is not claimed: the EoM
max at the best candidate is still 0.998 of full, and
Frontier A remains 0 everywhere.

### P128-3 — VERDICT: GUARD POSED — BLOW-UP BASIN EXCLUDED, FRONT STANDS

(Worker report 2026-11-23; checker `work/p1283_checker.py`
183/183 PASS, re-run fresh by the coordinator — floor
re-evaluated at every reported candidate from its
stored z, `verdict_form` recomputed to the same
verdict with the guard's cost read directly.
Deliverables: `results/p1283_run_record.md`,
`results/p1283_memo.md`, `results/p1283_results.json`.
Process on the memo's face: the checkpointed search
was silently killed three times mid-run and resumed
from checkpoint each time; all 16 starts completed
under registered settings.)

Machinery gate PASS (worst corpus error 8.55×10⁻¹²;
hinge alignment set = {44}). **Floor premise
verified, floor unmoved:** min |P_X| over the subset
for the stored configurations — corpus 2.30×10⁻² … 2.79
(closest 230× the floor), half (a) best 8.24×10⁻²,
half (b) best 1.767116. The only stored violator is
the blow-up itself (half (b) start 8: min |P_X| =
1.732128×10⁻⁸ at point 19). The guard (penalty
residual 10⁶·max(0, 10⁻⁴ − |P_X,i|) per subset point
+ candidate rejection + direct floor verification in
every deciding read) was posed on half (b)'s
constrained pose.

**The blow-up basin's exclusion, demonstrated three
ways.** (i) The start-8 seed itself: min |P_X| =
1.732×10⁻⁸ at point 19, 26/56 points below floor,
alignment set {19} reproduced — infeasible by a
factor 5.8×10³. (ii) The guarded run from that seed
(start 15) was driven to the floor's edge and ended
2.19×10⁻⁹ BELOW it at one point → rejected — the
search's only infeasible final (15/16 feasible),
excluded from selection; the memo records this as the
edge limit of penalty-only enforcement, caught by the
candidate-rejection layer. (iii) The guarded run from
the original start-8 seed (start 8) lands feasible,
parked exactly on the floor (min |P_X| =
1.000003699×10⁻⁴ at point 21), legality 0.6071,
health_ok = True (unguarded: False), alignment set
EMPTY (unguarded: {19}); its worst point 24 is t_FB
alone (share 1.0) — the basin is closed and the
configuration that lived in it now reads as an
ordinary single-channel-pin point.

**Best guarded candidate** (start 14, half (b)'s best
basin re-found): subset_legal = 0.9107142857142857,
EoM max = median = 0.9999999999878011, n_nondeg/n_deg
= 56/0, health_ok = False, Frontier A = 0.000, trap
not firing, alignment set empty, max-residual point
14 (plateau tie set 14–44), t_FA = 0.0 exactly, t_FB
share ≈ 1; **floor verified: min |P_X| = 1.767116 at
point 2.** Cost against half (b)'s best: Δlegal =
0.0, Δemax = −1.1×10⁻¹⁶ — **the guard is free at the
optimum**, so the verdict is not GUARD BINDS. Family
A at the best: legality 0.000, floor verified.
Phase-118 fence not pressed (closest |β_c| = 0.4709).
All 16 guarded finals have empty alignment sets.
Neither bar is met, exactly as in half (b): legality
0.9107 > hinge but the EoM max exceeds the hinge's by
9.3×10⁻¹². **Binding form (restated from the read):
the single-channel pin of half (b).** Failure-protocol
follow-ups in the memo: the floor as a standing
cost-free guard for future front searches; the pin
attack unchanged (it is P128-1/P128-2's line, now with
improvements on record).

### P128-4 — VERDICT: +∞ — CLOSURE EVIDENCE EXTENDED

(Worker report 2026-11-23; checker `work/p1284_checker.py`
12/12 PASS, re-run fresh by the coordinator — its
independent inline q implementation recomputed all seven
reads and anatomies. Deliverables:
`results/p1284_run_record.md`, `results/p1284_memo.md`,
`results/p1284_results.json`.)

The missing whole-shell q read for the coupling-force
front family now EXISTS, and every one of the family's
seven stored static β = 1.1 configurations reads
**max q = +∞**. Both validation gates passed before
the read was believed: the control reproduced the
(10,30) family's stored static β = 1.1 whole-sample
max q = +∞ exactly (collapse at the stored point
(2.8153708227909306, 0.0, 9.855769230769232), r = 10.25,
T₀₀ + T_n̂n̂ = −2.952×10⁻⁴, flux = −1.778×10⁻⁴; 895/1764
points +∞), and the stress assembly reproduced all
seven configurations' stored subset reads on the
56-point subset (errors 0.0 for six, 8.549×10⁻¹² for
one; independently assembled That identical to the
margins path, max diff exactly 0.0; hinge alignment
set = {44}). The sample (fixed in the run record
before the family's numbers): `p503_lib.fine_pts(10, 20)`
— the fine component of `p853_lib.verdict_pts()` at
the Phase 48 bed's radii R1 = 10, R2 = 20 (from
`p152_lib.bed_gf`) — 26 Fibonacci directions × 33 radii
= 858 points, 520 in shell; stress via
`p1015_lib.hinge_E_total` (scalar + coupling + fluid),
That via `eulerian_that`, q via `p853_lib.q_values`
verbatim.

Per-configuration reads (whole-shell max q; +∞ points
of 858; max finite q; deciding collapse = minimum
denominator): direct/B76_mu0 — +∞, 172, 6.275, r = 9.00,
den −1.683×10⁻², flux −8.257×10⁻³; direct/A76_mu0 —
+∞, 274, 27.752, r = 9.00, den −1.931×10⁻², flux
−9.267×10⁻³; runs_B[0] — +∞, 131, 23.838, r = 9.25,
den −5.285×10⁻³, flux −2.829×10⁻³; **runs_B[1] = the
hinge best — +∞, 131, 9.015, r = 9.00, den −7.682×10⁻³,
flux −3.816×10⁻³**; runs_B[2] — +∞, 88, 14.800,
r = 8.00, den −1.087×10⁻³, flux −5.257×10⁻⁴;
runs_A[0] — +∞, 274, 27.752 (identical to
direct/A76_mu0); runs_A[1] — +∞, 352, 44.355,
r = 10.25, den −1.612×10⁻², flux −1.189×10⁻³. The
thresholded "sig" variant is also +∞ for all seven.

**Anatomy:** denominator collapse (T₀₀ + T_n̂n̂ ≤ 0
with nonzero flux) at the inner edge in EVERY
configuration — deciding radii r = 8.00–10.25, first
collapse at r ≤ 9.75 — the same flux-overload
mechanism as the (10,30) and Finalist-A families
(P119-5's anatomy). The breathing reopening criterion
(P108-4) is therefore NOT met by this family either,
and the criterion's search now closes for it on a
READ, not on an absence: the named unread gap of
P119-5 is filled. No breathing registration becomes
posable from this phase. C12: a flux-ratio read; no
wall's legality is claimed or approached by it.

---

## PHASE 128 — FINAL SYNTHESIS (coordinator, 2026-11-23)

**Plain language first.** Phase 119 ended with the
superluminal wall's equation pinned at its worst point
in two different ways and a list of three attacks.
This phase ran all three, and the wall moved — twice,
independently. Composing the two escapes (kill one
force channel *and* keep the field's curvature term
alive in the same configuration) produced the first
configuration in the programme that is better than the
standing best on legality and on the equation's worst
error *at the same time*; aiming the curvature term's
sign at the pin points produced a second, stronger
one. Neither is a pass — the equation's worst error is
still 99.8% of full at best, and the overall pass mark
(Frontier A) is still zero everywhere — but "the front
cannot move" is no longer true, and the reason it
still doesn't pass is now a named, narrower thing:
wherever the curvature term is made to oppose the
force at the pin points, the worst point migrates to
the one named point left unopposed. Coverage, not
opposition, is the binding constraint. The third
attack priced a safety guard for the wall's searches
and found it free — it excludes a known blow-up basin
completely and costs nothing at the optimum. And the
one measurement the breathing-wall line was owed came
back negative on all seven configurations, so that
line's closure now rests on a measurement rather than
on a missing one.

### Per-item verdicts

- **P128-1 (FU-P1194-1) — JOINT (i)+(ii) IMPROVEMENT
  (milestone).** The composition Pareto-dominates the
  hinge best under both clauses: legality 0.589 →
  0.929 (0.946 second path), EoM max strictly below
  the hinge's (by 1.9×10⁻⁵); median worsened (anatomy);
  Frontier A = 0 — not a pass. Binding form: the
  single-channel FB pin at the migrated worst point
  (44), with the live □φ carrying the pin's sign.
  Recovery-completed after the original worker session
  ended without a report; disclosed on the memo's face.
- **P128-2 (FU-P1194-2) — JOINT (i)+(ii) IMPROVEMENT
  (milestone).** The sign-targeted blend: legality
  0.589 → 0.786, EoM max 0.99999999998 → 0.99806,
  median 0.224 → 0.145 (all three coordinates
  improved); Frontier A = 0 — not a pass. The sign
  target is met generically, and the pin migrates to
  the unopposed named point — coverage is the binding
  constraint.
- **P128-3 (FU-P1194-3) — GUARD POSED — BLOW-UP BASIN
  EXCLUDED, FRONT STANDS.** The |P_X| ≥ 10⁻⁴ floor,
  posed on half (b)'s constrained pose, excludes the
  start-8 blow-up basin demonstrably (three ways) and
  is free at the optimum (Δlegal = 0.0,
  Δemax = −1.1×10⁻¹⁶). The guarded best re-finds half
  (b)'s best and its single-channel pin.
- **P128-4 (FU-P1195-1) — +∞ — CLOSURE EVIDENCE
  EXTENDED.** The coupling-force front family's
  whole-shell static β = 1.1 max q is +∞ on all seven
  stored configurations (inner-edge denominator
  collapse, r = 8.00–10.25). P108-4's breathing
  reopening criterion is not met by this family; the
  criterion's search closes for it on a read.
- **P128-5 (FU-P1192-1) — REGISTERED.** The standing
  search criterion recorded verbatim; no search run.

### Rung verdicts (FTL first, as tasked)

- **FTL (2a): NO — with the front's standing changed
  in kind.** No joint (i) legality + (ii) solution-grade
  PASS exists anywhere in this phase: Frontier A = 0
  at every candidate of all three front items, and
  the best EoM max on record is still 0.998 of full.
  What changed: the coupling-force front at β = 1.1
  now has two independent, second-pathed,
  checker-verified joint IMPROVEMENTS over its
  standing best (P128-1, P128-2) — the first movement
  of this front in the programme's history — each a
  scan signal under attack until a Gate. C12: these
  are reads on pre-existing walls at β = 1.1; a moved
  front is not a legal wall, not transport, nothing
  superluminal produced or claimed. Every superluminal
  row remains EFFECTIVE ONLY or worse.
- **Traversable wormhole: NO as an unqualified claim,
  unchanged.** No throat was posed or improved in this
  phase. The QET sourcing claim's Gate is Gate-14, the
  parent's line (not duplicated here). P128-4's read
  closes the breathing line's last unread family on a
  measurement: no breathing registration becomes
  posable from this phase, and the line stands closed
  under P108-4's condition with its criterion now
  priced on every family in the record.
- **Practical near-c (2b): NO CHANGE.** No subluminal
  configuration was attempted.
- **Technical results: YES ×5**, recommended for the
  ledger's GATE-QUEUED tier (internal, ungated):
  (1) the composition improvement — the programme's
  first joint (i)+(ii) improvement on the
  coupling-force front, with its migrated single-channel
  FB pin anatomy (P128-1); (2) the sign-targeted blend
  improvement and the coverage law — opposition works
  pointwise, the pin migrates to the unopposed named
  point (P128-2); (3) the |P_X| floor guard posed,
  basin excluded, priced free at the optimum (P128-3);
  (4) the front family's whole-shell q read: +∞ on all
  seven stored configurations, inner-edge denominator
  collapse (P128-4); (5) the standing field-QET search
  criterion, registered verbatim (P128-5).

### Integrated follow-up queue (ordered)

1. **A GATE for the two improvement claims** —
   P128-1's and P128-2's joint (i)+(ii) improvements
   on the coupling-force front at β = 1.1, in the
   registered Pareto form over the P101-5B hinge best,
   routed to the parent (gates are the parent's line,
   as Gate-14 is for the QET claim). The claims join
   any push queue only if a Gate passes them, under
   the standing publication rule. Nothing publishes
   from this phase.
2. **COVERAGE-COMPLETE SIGN TARGETING** (from
   P128-2's memo, the head science item): pose the □φ
   sign target over the FULL named pin set
   {44, 50, 51, 52} and the band 44–55 simultaneously —
   including a direct target at r = 14.75 (point 44,
   the migration target both improvements exhibited) —
   and iterate the target onto any point the pin
   migrates to, so no named point is left unopposed.
   Grounding: P128-2's coverage law (opposition works
   pointwise; the pin migrates to the unopposed point)
   and P128-1's anatomy (t_kin same-sign as t_FB at
   point 44 under the composition). Bars inherited
   from §P119-4/§P128-1 verbatim; the |P_X| floor
   (item 3) and the cr2 guard (item 4) posed as
   standing guards of the search.
3. **THE |P_X| FLOOR AS A STANDING GUARD** (from
   P128-3): |P_X| ≥ 1.0×10⁻⁴ at all subset points,
   adopted as a standing feasibility condition for
   future searches on this front — priced free at the
   optimum in P128-3; penalty enforcement backed by
   candidate rejection (P128-3's edge lesson).
4. **A POSED cr2 GUARD FOR THE HEALTH CLAUSE** (from
   P128-2's memo): both of this phase's improvements
   fail health_ok on the cr2 clause, and health is a
   JOINT PASS clause — a future pass attempt must pose
   health as a search condition, not discover it in
   the read.
5. **THE MEDIAN-PRICING POSE** (from P128-1's memo):
   P128-1's improvement worsened the median while
   improving (legal, max); P128-2's improved all
   three. A pose pricing the median alongside the
   registered pair tests whether P128-1's trade is
   structural to the composition or an artefact of
   its search.
6. **FU-P1192-1 — standing search criterion:** carried
   (registered in §P128-5; reopens only on publication
   of a field/oscillator QET meeting clauses
   (i)+(ii)+(iii)). No active work.
7. **FU-P106-4a — the ℬ-guided search: STILL
   UNPROMISED**, carried verbatim from Phase 106
   through Phases 108/119/128; it runs only under its
   own future registration.

**Anti-loop compliance:** P128-1 was Phase 119's
registered composition (a new pose, neither half
re-run); P128-2 and P128-3 were Phase 119's own logged
follow-ups under their own registrations, run once
each; P128-4 ran no breathing and posed no wall — it
produced the registered measurement; P128-5 registered
a criterion and ran no search. The two improvements
are claimed exactly in their registered Pareto form
over the hinge best, as scan signals under attack,
with their anatomies (migrated pins, worsened median
in P128-1, health failures) on their faces. INTERNAL
ONLY — nothing uploaded, nobody contacted.

## Phase status: CLOSED (2026-11-23)

Deliverables: this checkpoint; `results/` (p1281–p1284
run records, memos, results JSONs; P128-5 is
registration-only, its deliverable is §P128-5 above)
and `work/` (scripts + checkers: P128-1 273/275 with
the two non-passes resolved on the memo's face,
P128-2 230/230, P128-3 183/183, P128-4 12/12 — all
re-run fresh by the coordinator). No worker number
was altered by the coordinator.

---

**GATE-19 CORRECTION (2026-11-23, append-only; gate19/GATE19.md):**
the legality coordinates of P128-1/P128-2 were read through
p761_lib.fluid_T, proven defective by Gate-19 (A*That*A^T for
A^T*That*A; fixed at source). Corrected deciding reads (Gate-16
machinery, venv + pin): hinge best subset legality
0.5892857142857143 -> 0.75; P128-1 best 0.9285714285714286 /
0.9464285714285714 -> 0.8928571428571429; P128-2 best
0.7857142857142857 -> 0.6071428571428571; P128-2 targeted
0.5357142857142857 -> 0.42857142857142855. All EoM reads stand
bit-identical. P128-1's JOINT IMPROVEMENT stands in restated
numbers (Gate-19: G16-1 SURVIVES IN RESTATED WORDING). P128-2's
JOINT IMPROVEMENT FALLS (Gate-19: G16-2 FAILS): against the
corrected hinge its legality coordinate worsens by 0.1428571;
its EoM max/median moves and the coverage law stand as anatomy,
which the registration classifies as partial movement, not a
milestone. The Pareto thresholds registered in this checkpoint
were themselves computed with the defective tensor (hinge
0.5892857142857143); Gate-19 judges dominance against the
corrected hinge, per the Gate-17B definitional standard.
