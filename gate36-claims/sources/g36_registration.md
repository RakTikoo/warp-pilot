# GATE-36 REGISTRATION — written before any gate computation

Gate-36 re-judges Phase 320's spinor mating on the pointwise
member (Phase 314's headline member, ramp m₀ = +4.00, rise
[9, 20.5], on the Gate-30 winner's (S, N) verbatim, β = 1.1) —
the strongest extended-class target in the record, whose
required density Gate-35 certified positive throughout the
closed posed volume at adversary grade (G35-B).

The gate writes its own machinery throughout (own assembly
for the target tensor, own spinor builder, own starts, own
Jacobian). It does not import p312_lib / p320_run / g34_* /
g35_* for any deciding computation; stored artefacts are
read as data (targets, configurations) only. The gate does
not repair what it breaks.

## The claims under attack (from CHECKPOINT320 / p320_memo)

- **C-320-1 (the match).** One six-mode Dirac superposition
  (m = 1, on shell) reproduces the member's full T_req
  jointly at all four binding sites at direct-path residuals
  7.012×10⁻¹⁵ / 7.802×10⁻¹⁴ / 8.231×10⁻¹⁴ / 1.296×10⁻¹⁵
  (max 8.231×10⁻¹⁴ vs the 1×10⁻⁹ bar), one global scale
  |a|² = 0.010204382146024456 with per-site implied s²
  agreeing to ≤ 5.1×10⁻¹⁴ absolute; fit Segre types
  reproduce the targets' (I / IV / I / IV); the ladder
  transition sits at the counting threshold 7N − 1 ≥ 40
  (N = 4 best 7.317×10⁻⁴, N = 5 best 6.215×10⁻⁵, 0 starts
  at bar below N = 6).
- **C-320-2 (density at the match).** The matched
  configuration's density is the target's own, positive at
  all four sites: +6.263182×10⁻⁴ / +6.818808×10⁻⁴ /
  +6.257630×10⁻⁴ / +1.172278×10⁻⁴ (S1/S2/S3/S4).
- **C-320-3 (structural characterisation).** The 40 × 42
  Jacobian at the N = 6 solution has full row rank 40 with
  σ_min = 3.994×10⁻⁴ (σ_max = 3.909×10³); the perturbation
  ladder re-achieves the bar at every rung (ε = 1×10⁻¹²:
  8.3×10⁻¹⁴; 1×10⁻⁹: 1.0×10⁻¹²; 1×10⁻⁶: 2.0×10⁻¹³;
  1×10⁻⁴: 8.1×10⁻¹⁴), densities positive throughout; the
  match is structural, not a knife-edge fit. DISCLOSED in
  the phase: σ_min is ~68× thinner than Gate-34's 0.0272
  on the weaker (Phase 312) winner.

## Controls (all must pass before any re-judgement read
## is quoted)

- **CTRL-T1 (site table).** The gate's own assembly
  reproduces the member's stored site table at the four
  stored site points: ρ_req per site, and the full That
  component-wise against `phase320/work/p320_targets.json`,
  at float64 round-off class (report max diffs; bar:
  ρ diffs ≤ 1×10⁻¹⁵ relative class, components ≤ 1×10⁻¹⁶
  absolute class — the class Gate-34 achieved on the 313
  targets; any excess is reported, not hidden).
- **CTRL-T2 (derived reads).** From the gate's own That:
  exact pointwise NEC minimum (own worst-null) and Type-I
  flags per site vs the stored record (flags S1/S3 True,
  S2/S4 False; exact NEC −1.267419×10⁻³ / −1.266247×10⁻³
  at S1/S3 class).
- **CTRL-S1 (Phase 320's match under the gate builder).**
  Phase 320's persisted winning configuration
  (`p320_joint_bestfit.json`) evaluated by the gate's
  direct path against the stored targets: per-site
  residuals and densities vs the stored direct values
  (7.012×10⁻¹⁵ / 7.802×10⁻¹⁴ / 8.231×10⁻¹⁴ / 1.296×10⁻¹⁵;
  densities to ≤ 3.7×10⁻¹⁵). Report actual diffs.
- **CTRL-S2 (Phase 313's match under the gate builder).**
  Phase 313's persisted winning configuration against
  `p313_targets.json`: max R vs the stored 3.253×10⁻¹³.
- **CTRL-S3 (builder self-consistency).** The gate's
  pairwise fast path vs its direct definitional path on
  the stored configurations and on random mode sets:
  agreement at round-off class before the pairwise path
  is used in any fit.

## Item 1 — the targets, independently

Re-derive the member's full T_req at its four binding
sites with the gate's own assembly (symbolic/jet Einstein
for the posed metric: g_tt = −N(r)², g_tx = −β·S(r),
γ_ij = δ_ij + (M−1) n_i n_j, M the m₀ = +4.00 ramp;
profiles from their definitions: S = 1 − I_u(3,3),
u = (r−10)/10 on [10, 20]; N = 1 + A·B_plat, A =
0.07439108177516472, B_plat the quintic-step plateau
(c = 15, W = 5, e = 3); Eulerian frame by the ADM
convention — unit normal + eigh triad of γ — in the
gate's own code). Compare against Phase 320's targets
component-wise (all 16 components, all four sites);
report ρ_req, exact pointwise NEC, Type-I flags per
site from the gate's tensor.

## Item 2 — the fit, independently

The gate's own builder (Dirac superposition from the
field definition; m = 1; the protocol's packing
θ = [p (3N), Re a (2N), Im a (2N)]; optimiser residual =
10 upper-triangular components per site normalised by
the site's |That|_F; definitional residual = full
Frobenius |T_fit − That|_F by the direct path) and the
gate's own starts (own seeds; warm start from Phase
257's D1 configuration permitted as one start, as in
the protocol):

- Ladder: N = 4, 5 (6 random starts each), N = 6
  (1 warm + 8 random), N = 8 (≥ 4 starts). Bar 1×10⁻⁹
  on the direct-path max residual.
- At the gate's best N = 6 solution: per-site direct
  residuals, density at the match per site, Segre
  types of fit vs target per site, Dirac residuals of
  the modes, D-a per-site amplitude refits (frozen
  momenta/spins) → per-site implied s² vs the global
  |a|².
- Jacobian at the gate solution: central FD,
  h_j = 1×10⁻⁶·max(1, |θ_j|) (the protocol's recipe),
  plus h-refinement (1×10⁻⁵, 1×10⁻⁷) for recipe
  stability; full singular-value tail reported.
- Perturbation ladder at the gate solution (Gate-34
  protocol): ε ∈ {1×10⁻¹², 1×10⁻⁹, 1×10⁻⁶, 1×10⁻⁴},
  componentwise symmetric noise ε·|That_s|_F, 2 draws
  per rung, warm + one fresh start per draw; bar
  re-achievement and matched densities reported.

## Item 3 — the conditioning question

Phase 320's σ_min = 3.994×10⁻⁴ is ~68× thinner than
Gate-34's 0.0272 (same packing, same FD recipe — verified
from the two codebases before registration). Both
Jacobians are of the |That|_F-normalised residual at an
N = 6 solution. Registered experiments, all with the
gate's builder and Jacobian recipe:

- **E1 (census, pointwise target).** σ_min at every
  successful N = 6 solution the gate finds on the
  pointwise target (Item 2's starts; up to 12 extra
  starts if fewer than 6 successes). Distribution
  reported in full.
- **E2 (census, weaker target).** The identical protocol
  (N = 6, 1 warm + 8 random starts, own seeds) against
  the Phase 312 winner's targets (`p313_targets.json`):
  σ_min at every successful solution.
- **E3 (optimiser/recipe variation).** (i) σ_min at
  Phase 320's stored winner under the gate's Jacobian
  (CTRL-S1 extension); (ii) σ_min after re-polishing
  the stored winner with the gate's optimiser at tight
  tolerance; (iii) one refit by a different solver
  route (method variation) from a successful start;
  (iv) σ_min under FD h ∈ {1×10⁻⁵, 1×10⁻⁶, 1×10⁻⁷} at
  one solution of each target.
- **E4 (structure).** At one representative solution of
  each target: the smallest right-singular vector
  (parameter attribution: per-mode, p vs Re a vs Im a
  weight) and the smallest left-singular vector (site /
  component attribution); the singular-value tail shape
  (isolated thin direction vs uniform thinning);
  per-site |That|_F and component dynamic range for
  both targets; σ_min vs solution properties (|a|²,
  max |p|) across the censuses.
- **E5 (scale probe).** The pointwise target scaled ×4
  (all components), fit at N = 6 from a warm start:
  σ_min at the scaled solution vs the unscaled census —
  quantifies how much of σ_min is overall target scale.

**Attribution decision tree (registered):**
- E1 and E2 censuses in the same σ_min class (within
  ~×3 medians) → the thinness is a property of the
  FAMILY/BUILDER as the gate implements it; the
  Gate-34-vs-320 difference is then located in the
  solution/builder instance, and the claim set states
  σ_min only as measured under the gate's recipe.
- E2 median ≥ ×10 above E1 median, with E1 tight →
  property of the TARGET; E4 names the site/component
  structure carrying it.
- E1 spread ≥ ×30 with some solutions ≥ 1×10⁻² →
  property of the SOLUTION FOUND (starts/optimiser);
  the phase's σ_min is then one draw, and the claim
  set quotes the census, not the single value.
- Mixed or ambiguous outcomes are stated as mixed,
  with the numbers; no attribution is forced.

## Claim set forms (verdicts per claim)

For each of C-320-1, C-320-2, C-320-3: SURVIVES /
SURVIVES RESTATED / FAILS, with the gate's numbers.
The quotable set carries the fences verbatim in
substance: binding-site scope only; the member's EC
violations stand exactly as stored (SET-244 SAMPLER-M:
NEC min −1.170007×10⁻³, WEC min −1.044069×10⁻², DEC min
−1.000003; depth −5.327659×10⁻⁴ a negative NEC read);
no extent, no QI (none exists for the extended class),
no legality or front wording. The conditioning is
stated as measured, with its Item 3 attribution.

## Standing rules

Registration before computation (this file). Controls
before any re-judgement read is quoted. DESK: one-line
summary. No ledger append, no launches, no publication,
no user contact. Deliverables: gate36/GATE36.md +
gate36/CHECKPOINT_GATE36.md.
