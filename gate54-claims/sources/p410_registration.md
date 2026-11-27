# PHASE 410 REGISTRATION — SOURCE THE CANDIDATE: THE SPINOR
# SUPPLIER AT THE PHASE 405 WINNER'S SITES

Charged at ledger entry 1070 (2026-11-26). Written before any
Phase 410 computation. Frame of record: the VM
(`~/workspace/warp-pilot/venv`). The laptop admission control
(SS6) is run and followed; all deciding reads are VM reads, as
in Phases 313/320.

## SS0 — The question

Phase 405's winner — Phase 400's static base (N/M verbatim)
plus the free K = 9 spline shift shape at the SS7 criterion
peak, joint +1.227385×10⁻⁶ in the band [10, 20], Gate-50
verified — is a prescribed geometry. Can the programme's
spinor supplier (the Phase 313/320 mating machinery: a 6-mode
Dirac superposition solved against the FULL required stress
tensor at named sites) supply that geometry's required
stress T_req at its deciding sites — and, channel by
channel, what does the supplier carry and what does it miss?

## SS1 — Machinery

The spinor side is Phase 320's driver machinery copied
verbatim in content (itself Phase 313 verbatim, itself Phase
293/261): gamma matrices, `u_spinor`, `fields_at_point`,
`T_bilinear`, `stress_at_point`, pairwise-S / `T_from_S`,
vectorised `S_of` asserted against the verbatim builder,
`T_pairwise`, `T_direct`, Phase 257's `segre`. Parametrisation
(folded amplitudes): theta = [pvecs (3N), Re avecs (2N),
Im avecs (2N)], 7N parameters; residuals = the 10
upper-triangular components of (T_sup − T_req) per site,
normalised by the site's ||T_req||_F. Fits by
`scipy.optimize.least_squares` (trf), m = 1 primary; the
m = 0 secondary runs only if every m = 1 arm stalls above
max R = 1×10⁻⁶ (Phase 320's registered rule). Match bar
(direct path): max per-site R = ||T_sup − T_req||_F ≤ 1×10⁻⁹
(the 313/320 bar).

The target side is Phase 405's own assembly
(`p405_lib.T_at405` / `set_read405`, the frame of record for
the winner), with That = `verify_metric.eulerian_that(g, T)`
at each site point. The winner's knot vector is loaded from
Phase 405's stored state exactly as `p405_confirm.py` loads
it (Stage-C lineage, D-curve screen at the criterion) and is
asserted equal to Gate-50's stored knots
(`gate50/results/g50_stored_inputs.json`, conf405).

## SS2 — Sites

- **A1 — the joint argmin.** Gate-50's stored argmin point
  (−17.827002016737087, 0.1739363226225222,
  1.8812104787714563), r = 17.926829268292682. Direction
  n̂1 = point / r.
- **A2 — the SEC argmin.** The argmin point of the winner's
  own `set_read405` SET-244 read (identified in Item 1,
  before any fit; its radius and point are recorded there).
  Cross-check: the read's sec_min must reproduce the stored
  −2.2135565049905559×10⁻⁴ (Phase 405 confirmation) at
  ≤ 1×10⁻¹².
- **A3 — the peak site.** (10.0, 0, 0), r = 10 — the x-axis
  phys-row point where the FINE_R peak |β·S| =
  0.4426742490267404 is attained (Gate-50 claim (b)).
- **B — the radial stencil** (the tracking read): points
  n̂1 · r for r ∈ {16.926829268292682, 17.426829268292682,
  17.926829268292682 (= A1), 18.426829268292682,
  18.926829268292682} — offsets δ ∈ {−1.0, −0.5, 0, +0.5,
  +1.0} about the joint site, along its own direction.

## SS3 — Fits

- **FIT A (primary):** one superposition jointly at
  {A1, A2, A3} — 30 residuals. Ladder N ∈ {4, 5, 6, 8, 12}
  (the counting rule 7N − 1 ≥ 30 is first met at N = 5;
  N = 4 runs below threshold for the record, as in 320).
  Starts per arm: 1 warm (the Phase 257 best-fit folded
  start, the lineage warm start) + 8 random at/above
  threshold; 6 random below threshold.
- **FIT B (stencil tracking):** one superposition jointly
  at the 5 stencil sites — 50 residuals. Ladder
  N ∈ {6, 8, 12} (counting first met at N = 8). Starts as
  in Fit A.
- **Primary solutions:** Fit A at N = 6 if N = 6 matches at
  the bar (Gate-34 diagnostic standard), else the best
  arm's winner; Fit B at N = 8 if it matches, else its best.

## SS4 — The three reads

(i) **REPRODUCTION.** Per fit: per-site direct-path
residuals at the primary solution; Dirac residuals of the
modes; D-a per-site amplitude refits (Phase 320 pattern —
one field, one global scale |a|², per-site implied alphas).
Structural diagnostics (Gate-34 Item 3 standard): the
finite-difference Jacobian of the normalised residual
vector at the primary solution (central differences,
h = 1×10⁻⁶·max(1, |θ_j|), verbatim 320) — joint σ_min AND
per-site block σ_min (the smallest singular value of each
site's own 10-row block of J). σ_min is quoted
PER-SOLUTION (G36-C): a property of the found solution,
never of the target. Perturbation ladder (the operative
structural test): targets perturbed by ε·||T_req||_F with
ε ∈ {1×10⁻¹², 1×10⁻⁹, 1×10⁻⁶, 1×10⁻⁴} (Fit A) and
ε ∈ {1×10⁻⁹, 1×10⁻⁶} (Fit B), 2 draws each, warm + fresh
starts; a rung passes if the bar is re-achieved.

(ii) **CHANNEL DECOMPOSITION** (the phase's centre). At
every site of both fits, for T_req and for T_sup at the
primary solution (direct path): the Hawking–Ellis type
(Phase 257's `segre`); if Type-I, the eigen-decomposition
of η·T giving ρ and the three principal pressures, p_r
identified as the eigenvalue whose eigenvector has the
largest |component along n̂|; the channels —
NEC_r = ρ + p_r, NEC_t = ρ + p_t (each tangential),
WEC = ρ, DEC_i = ρ − |p_i|, DEC_flux = ρ − |T_0i| (the
Eulerian-frame flux norm), SEC_trace = ρ + p_1 + p_2 + p_3,
SEC_i = ρ + p_i — for both tensors side by side; the
SAMPLER-M sampled margins (`margins_chunked`, named) of
both tensors as cross-check; and the full 10-component
table (T_req vs T_sup vs difference). The decomposition
must state, per site: which channels of T_req are negative
(the demand's failing channels — Phase 407's map says the
winner's integrated deficit is entirely SEC-carried; the
per-site statement is this phase's to make), and whether
T_sup carries those same channel values or misses them,
and by how much. If a tensor at a site is not Type-I, the
decomposition falls back to the sampled margins + the
component table, and says so.

(iii) **THE SUPPLIER'S OWN ACCOUNTING.** Per site: the
supplier's density ρ_sup = T_sup[0, 0] (direct path) and
its sign (Phase 257's lesson: a match delivered at
negative field density is a different claim than at
positive); the global |a|²; per-site implied s² from the
worst-null contraction (Phase 320 pricing pattern, with
k* from the exact worst null of T_req at the site).

## SS5 — Controls (all before any candidate read is believed)

- **CTRL-320:** Phase 320's stored joint best fit
  (`p320_joint_bestfit.json`) against its stored targets
  (`p320_targets.json`), rebuilt on this phase's machinery
  copy: direct-path per-site residuals (stored max
  8.231×10⁻¹⁴) and the FD Jacobian σ_min at the stored
  solution (stored 3.994300907411277×10⁻⁴). PASS: max R
  ≤ 2× stored and ≤ 1×10⁻¹²; σ_min within 1% relative.
- **CTRL-313:** the same for Phase 313 (stored max R
  3.253×10⁻¹³; σ_min = 0.0272 in the record — Phase 313's
  own 0.027075700215882452, Gate-34's re-derivation
  0.027165249637030254). PASS: max R ≤ 2× stored and
  ≤ 1×10⁻¹²; σ_min within 2% of 0.0272.
- **CTRL-TGT-410:** the winner's target extraction:
  (a) `set_read405` of the winner reproduces the stored
  joint +1.2273852081052888×10⁻⁶ and sec_min
  −2.2135565049905559×10⁻⁴ (diff ≤ 1×10⁻¹²);
  (b) at A1, `nec_at405` and the exact worst null
  reproduce Gate-50's stored +1.2273852081052888×10⁻⁶ /
  +7.282191364112375×10⁻⁷ (diff ≤ 1×10⁻⁹; A1 is Type-I, so
  these are frame-invariant deciding values);
  (c) the winner's knot vector equals Gate-50's stored
  knots exactly.

## SS6 — Admission

The winner's `set_read405` is also run on the laptop pool
through the identical p405_lib; if its joint / sec_min /
argmin radii reproduce the VM read at roundoff (the
Phase 405 admission pattern), the laptop frame is ADMITTED
for screening in this phase. Deciding reads remain the
VM's regardless (Phases 313/320 precedent).

## SS7 — Verdicts (registered forms)

- **SUPPLIES AT THE SITES** — Fit A's primary solution at
  direct max R ≤ 1×10⁻⁹ at A1/A2/A3, σ_min (joint and
  per-site blocks) bounded away from zero (values stated),
  the perturbation ladder re-closing; Fit B's tracking
  outcome reported with it (holds at the bar / degrades,
  radii stated). This verdict carries a GATE REFERRAL.
- **SUPPLIES THE JOINT CHANNELS BUT NOT SEC** — the
  full-tensor match fails the bar, but at the best fit the
  NEC/WEC/DEC channel margins of T_sup agree with
  T_req's within 1×10⁻⁶ absolute at every Fit A site
  while the SEC channel disagrees by more than 1×10⁻⁶
  (or the residual concentrates in the SEC-carrying
  components, named). The decomposition is the
  deliverable; it becomes W26 composite supply's price
  list.
- **DOES NOT SUPPLY** — otherwise; the anatomy (which
  tensor components fail, at which sites, by how much)
  is the deliverable.

## SS8 — Fences

A site mating is not a field on the extent: no coverage
is claimed or implied (the extent line — 346/357/368/362 —
owns coverage; the candidate's own extent audit is
Phase 409, separate). No QI price is quoted (no QI read
for this configuration exists and none is invented).
Novelty NONE for the mating method (Martín-Moruno &
Visser 2021, per Gate-25). The supplier reproducing an
SEC-violating T_req is a statement about the supplier's
expressive range, not an energy-condition pass for
anything. DESK line in the memo.

## SS9 — Deliverables

`phase410/CHECKPOINT410.md`,
`phase410/results/p410_memo.md`, the driver and checker
under `phase410/work/`, full records under
`phase410/results/`. No ledger append, no successor
launch, no user contact.

## AMENDMENT (2026-11-26, before any candidate computation)

CTRL-313's σ_min leg as first written compared this build's
σ_min at Phase 313's STORED solution against the record's
0.0272. That comparison is ill-posed, and the record itself
shows why: Phase 313's driver computed no Jacobian; the
0.0272 figure is GATE-34's, evaluated at GATE-34's OWN refit
N = 6 solution (g34_item3a.json, N6_winner.theta) with
Gate-34's forward-difference FD. Per G36-C, σ_min is a
property of a solution, not of a target: at 313's stored
solution this build reads σ_min = 0.0347527502565207, at
Gate-34's refit solution 0.0272 — both legitimate, at
different solutions of the same target (whose direct
residuals this build reproduces at diff 0.0). CTRL-313's
σ_min leg is therefore evaluated as Gate-34 computed it:
forward-difference FD Jacobian at Gate-34's stored refit
theta, bar 2% of Gate-34's stored smallest singular value
0.027165249637030254 (g34_item3c). The at-stored-solution
value is recorded alongside. CTRL-320 is unaffected (Phase
320's σ_min WAS computed at its stored solution, in its own
driver, and reproduces at 2.0×10⁻⁷ relative).

## RECOVERY AMENDMENT 2 (2026-11-26, coordinator, disclosed)

The first execution died silently during Fit A N=6 rand0 (no
traceback; shared-VM contention) after completing all controls,
Item 1, and Fit A arms N=4/N=5/N=6-warm. The driver was rebuilt
with per-start JSONL persistence and deterministic re-execution;
the re-run reproduced every completed start of the crashed run
at identical values (recovery gate passed). During the re-run,
Fit B's below-threshold N=6 arm (35 dof vs 50 residuals -- the
arm cannot match by counting) burned its full 1300-evaluation
cap on each of its first two starts under CPU contention
(756 s and 787 s wall; stalls at 4.54e-06 and 1.50e-04). The
arm's outcome class is established -- below-threshold arms
never matched in 313, 320, or this phase's Fit A N=4 arm --
so the arm is TRUNCATED at 2 of 6 starts (Phase 392 truncated-
run precedent: the truncation is stated wherever the arm is
reported). No deciding read is affected: Fit B's primary
selection (N=8), diagnostics, decomposition and verdict all
proceed as registered. The remaining N=6 Fit B starts are the
only registered computation not executed.

## RECOVERY AMENDMENT 3 (2026-11-26, coordinator, disclosed)

A service restart killed the recovery-2 execution during Fit B
N=8 rand0; per-start persistence banked everything completed
(42 candidates). Fit B's N=8 arm has now run two starts -- the
warm start (seeded from Fit A's converged primary, the most
favourable start available) and rand0 -- and BOTH plateau at
the full 1300-evaluation cap at the same level: 7.667e-07 and
1.061e-06 max residual across the five stencil sites, three
orders short of the 1e-9 bar, with the residual spread evenly
over the sites. The plateau reads as a property of the arm,
not of the starts. The N=8 arm is therefore TRUNCATED at 2 of
9 starts (same truncated-run precedent as Amendment 2), and
the phase proceeds to Fit B's N=12 arm as registered -- the
arm that can still change the tracking answer (83 dof vs 50
residuals). Wherever the N=8 arm is reported, the truncation
and the two plateau values are stated. Reopening condition:
the seven un-run N=8 starts can be executed at any time from
the persisted machinery if a gate requires the full arm.

## RECOVERY AMENDMENT 4 (2026-11-26, coordinator, disclosed)

The recovery-5 execution completed all fits and both primary
selections (fitA N=6, maxR 2.966e-12; fitB N=12, maxR
2.305e-14) and Fit A's Jacobian (sigma_min 0.38576, rank 30),
then crashed in the perturbation ladder on a TypeError in the
driver's own residual closure: the comprehension was divided
by FROBS[si] without an np.array wrap, which works when FROBS
is a numpy array (all fit/control paths) but raises when the
ladder passes a plain list of Python floats. One-line fix
(np.array wrap; elementwise division, numerics unchanged).
All fit candidates persist in the per-start JSONL files, so
the re-run resumes every fit and recomputes diagnostics from
the persisted primaries.
