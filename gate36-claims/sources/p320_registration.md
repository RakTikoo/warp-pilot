# PHASE 320 REGISTRATION — THE SPINOR MATING ON THE POINTWISE MEMBER

Written before any deciding computation. Frame of record:
Phase 166 pin, Gate-19-corrected tensor, venv python
(numpy 2.5.5 / scipy 1.18.1), float64 throughout.

## Question

Phase 313 mated the Phase 312 extended-class winner
(broad ramp m₀ = +1.0) with a six-mode Dirac
superposition: MATCH AT POSITIVE DENSITY at its four
binding sites. Phase 314 then found a stronger member
of the same extended class — the ramp m₀ = +4.00
member — whose required density is positive not only
at the binding sites but at SET-244 pointwise scope,
and Gate-35 upgraded that positivity to a continuum
statement at adversary grade (G35-B: ρ_req > 0
throughout the closed posed volume, continuum minimum
+8.100317×10⁻⁵ at r = 20). This phase asks Phase 313's
question of the pointwise member, by Phase 313's
protocol verbatim: **can a spinor superposition supply
the pointwise member's required stress in full,
jointly at its four binding sites — where the target's
density is positive at every site?**

## The target member (fixed here)

- Base pose: the Gate-30 winner's (S, N) verbatim,
  spec {'shape':'plat','a':2,'b':2,
  'A':0.07439108177516472,'c':15,'W':5,'e':3.0}, β = 1.1.
- Extended-class profile (Phase 314 headline member,
  label 'ramp_m+4.00_r1-9_r2-20.5'):
  {'kind':'ramp','m0':+4.0,'r1':9.0,'r2':20.5} —
  M = 1 + 4.00·[U(r;9,20.5) − U(r;21,24)].
- Stored reads (Phase 314, confirmed by Gate-35's
  independent symbolic-Einstein re-read at round-off):
  depth −5.327658635240826×10⁻⁴ (SAMPLER-M,
  adversary-polished; Phase 314 stored
  −0.0005327658635240826, gate −0.0005327658635240827);
  SET-244 ρ min +8.272455162810697×10⁻⁵ (0/6642
  negative), Type-I count 2615; SET EC minima
  NEC −1.1700067327832923×10⁻³, WEC
  −1.0440691445181194×10⁻², DEC −1.0000031873996493×10⁰
  (SAMPLER-M).
- The target tensor is the EXTENDED CLASS'S OWN
  tensor: That_s = eulerian_that(g, T) with (T, g)
  from `phase312/work/p312_lib.py` `T_at_ext` at the
  site points (p314_lib.py is byte-identical to
  p312_lib.py, md5 504a941734e895ba8919b2630ba99358 —
  the same assembly Phase 314 used). The Eulerian
  frame is verify_metric's ADM frame of the extended
  metric.

## Sites (Phase 293's rule, as applied by Phases 312/314)

Phase 314's stored sites for this member
(`phase314/results/p314_results.json`,
'headline_member' → 'sites'), taken verbatim; Gate-35
re-derived the identical site set (points, radii,
Type-I statuses) with its own assembly:

- S1: adversary-polished worst site, point
  (−1.8498498332103237e-06, 9.138865153681726,
  −8.25246065354556), r = 12.3134870420811, Type-I,
  ρ_req = +6.263182190001702×10⁻⁴,
  SAMPLER-M NEC = −5.327658635240826×10⁻⁴ (= depth),
  exact pointwise NEC = −1.267418999036892×10⁻³.
- S2: SET-244 SAMPLER-M NEC argmin, point
  (−0.31826692722382366, 2.89882042943074,
  −11.464167419451972), r = 11.829268292682926,
  Type IV, ρ_req = +6.818808066077532×10⁻⁴,
  SAMPLER-M NEC = −1.1700067327832923×10⁻³,
  exact pointwise NEC = −1.1836912968446653×10⁻³.
- S3: Type-I-restricted SET argmin, point
  (0.050206190445493494, 10.291664734541234,
  6.766787112315567), r = 12.317073170731705, Type-I,
  ρ_req = +6.257630013907980×10⁻⁴,
  SAMPLER-M NEC = −5.327425174463472×10⁻⁴,
  exact pointwise NEC = −1.266246514576519×10⁻³.
- S4: SET argmin over r ≥ 15, point
  (−1.8017847046548792, −6.7025492921821295,
  16.26392652815417), r = 17.68292682926829, Type IV,
  ρ_req = +1.1722775116980106×10⁻⁴,
  SAMPLER-M NEC = −7.107812464603784×10⁻⁴,
  exact pointwise NEC = −7.120705407266889×10⁻⁴.

CTRL-MEM (below) verifies the tensors at those points
against BOTH Phase 314's stored per-site reads and
Gate-35's gate values before any fit is run.

## Machinery (used as given, no re-derivation)

- Target side: `phase312/work/p312_lib.py` —
  `T_at_ext`, `set_read_full_ext`, `worst_null`;
  Eulerian frame `verify_metric.eulerian_that`;
  SAMPLER-M margins `p2352_run.margins_chunked`.
- Spinor side: Phase 313's driver machinery, copied
  verbatim in content from `phase313/work/p313_run.py`
  (itself Phase 293 verbatim, itself Phase 261 Item 1
  verbatim): gamma matrices, `u_spinor`,
  `fields_at_point`, `T_bilinear`, `stress_at_point`,
  `pairwise_S`, `T_from_S`, the vectorised `S_of_vec`
  asserted against the verbatim builder before any
  fit, the folded-amplitude parametrisation
  ψ(x) = Σ_j u(p_j, a_j) e^{+i p_j·x}, per-site phase
  evaluation, residual = the 10 upper-triangular
  components per site normalised by the site's
  |That|_F for the optimiser; definitional residuals
  are the DIRECT-path Frobenius norms. Phase 257's
  `segre` classifier verbatim.
- The Pauli-guard and on-shell assertions of Phases
  261/293/313 are carried over verbatim: after any
  loop that binds a local named like a Pauli matrix,
  assert σ₂ intact; assert the winning modes' Dirac
  residuals ≤ 1×10⁻⁹ before any verdict is read.

## Controls (all must pass before any fit is read)

- **K1–K4 — the spinor machinery controls**, Phase
  261's controls on the stored D1 record, verbatim in
  content and bars as run by Phases 293/313 (K1:
  Phase 257's stored match reproduced, R ≤ 1×10⁻¹²
  and |R − stored| ≤ 1×10⁻¹², contraction ≤ 1×10⁻⁹,
  eigenvalues ≤ 1×10⁻⁸; K2: per-site s² table to rel.
  ≤ 1×10⁻⁴; K3: phase machinery vs direct builder
  ≤ 1×10⁻¹⁰ displaced, ≤ 1×10⁻¹² at x = 0; K4: stored
  site contractions ≤ 1×10⁻¹², collinearity as
  stored). The vectorised S builder is asserted
  against the verbatim builder (≤ 1×10⁻¹²) before the
  fit path uses it, as in Phase 313.
- **CTRL-293 — the protocol reproduces Phase 293's
  stored match** (verbatim from Phase 313): Phase
  293's persisted winning configuration evaluated by
  the DIRECT path against Phase 293's persisted
  targets; stored Rs_direct / rhos_direct /
  tkks_direct reproduced to ≤ 1×10⁻¹¹ absolute per
  site and max R ≤ 1×10⁻⁹; stored-U integrity
  ≤ 1×10⁻¹².
- **CTRL-313 — Phase 313's match reproduces under
  this builder.** Phase 313's persisted winning
  configuration (`phase313/work/p313_joint_bestfit.json`,
  N = 6, m = 1) is evaluated by the DIRECT path
  against Phase 313's persisted targets
  (`phase313/work/p313_targets.json`). Required: the
  recomputed per-site residuals reproduce the stored
  Rs_direct (9.816544100325221×10⁻¹⁴ /
  2.846735996293551×10⁻¹³ / 3.253339860306391×10⁻¹³ /
  7.547124382951456×10⁻¹⁴), rhos_direct and
  tkks_direct to ≤ 1×10⁻¹¹ absolute per site, max R
  ≤ 1×10⁻⁹, stored-U integrity ≤ 1×10⁻¹². If
  CTRL-313 fails, the builder cannot be trusted on
  the new target: blocker, reported exactly, no fit
  is run.
- **CTRL-MEM — the pointwise member's stored reads
  reproduce (the charge's control (i)).** (a) Sites:
  at the four stored site points, That via
  `T_at_ext` + `eulerian_that` must reproduce, against
  BOTH Phase 314's stored reads and Gate-35's gate
  values: ρ_req to ≤ 1×10⁻¹² absolute; SAMPLER-M NEC
  (margins_chunked) to ≤ 1×10⁻¹²; exact pointwise NEC
  minimum (worst_null: fib(642) + Nelder–Mead) to
  ≤ 1×10⁻⁹; Hawking–Ellis Type-I flags equal to the
  stored flags (S1/S3 True, S2/S4 False). S1's
  SAMPLER-M NEC must equal the member's stored depth
  −0.0005327658635240826 to ≤ 1×10⁻¹². (b) SET-244:
  `set_read_full_ext` must reproduce Phase 314's
  stored set summary — n_points 6642 and Type-I count
  2615 exact; nec/wec/dec/sec/rho min, median and max
  to ≤ 1×10⁻¹¹ absolute (stored-precision class;
  Phase 314's own controls reproduced stored set
  reads at diff 0.0). If CTRL-MEM fails, the target
  cannot be re-read: blocker, reported exactly, no
  fit is run.

## Item 1 — target extraction

Per site, extracted and persisted
(`work/p320_targets.json`): point x_s; That_s (4×4,
Eulerian frame of the extended metric); ρ_s =
That_s[0,0]; |That_s|_F; k*_s = (1, n̂*_s) with n̂*_s
the exact worst null direction (worst_null) and the
pointwise NEC minimum That_s(k*_s, k*_s); SAMPLER-M
margins (nec/wec/dec/sec) at the site; Hawking–Ellis
type at the site; Segre type of That_s. Both NEC
reads are reported, named, wherever either is quoted
(Gate-25 sampler-naming rule).

## Item 2 — the joint match (Phase 313 protocol,
## with the counting-threshold ladder)

m = 1 primary. The residual vector has 40 components
(10 per site × 4); the folded-amplitude
parametrisation carries 7N real parameters minus one
overall-phase gauge, so the counting threshold
(Gate-34 Item 3) is 7N − 1 ≥ 40, first met at N = 6.

- **Below-threshold arms N ∈ {4, 5}** (7N − 1 = 27,
  34): 6 random starts each (`rand_theta`, rng seed
  3201), least_squares (trf, protocol tolerances),
  max_nfev 900. These arms map the below-threshold
  stall, as in Gate-34's sweep; they are not expected
  to close and a stall there is not evidence against
  the match.
- **Threshold-and-above arms N ∈ {6, 8, 12}** —
  Phase 313's protocol verbatim: all three run; per
  N, 9 starts — 1 warm (Phase 257's stored winner
  modes, augmented with drawn modes for N > 6,
  exactly as Phase 313's `warm_theta`; a start, not
  evidence) + 8 random (`rand_theta`, rng seed 3201);
  least_squares (trf), max_nfev 900 / 1300 / 2000 for
  N = 6 / 8 / 12.
- Definitional numbers are the DIRECT-path residuals
  of the best fit (`T_direct` — the verbatim bilinear
  builder with explicit phases), as in Phases
  261/293/313.

**Match bar (Phase 261/293/313 JOINT MATCH bar):**
max over sites of the direct-path Frobenius residual
R_s = ‖T_fit(x_s) − That_s‖_F ≤ 1×10⁻⁹.

**m = 0 secondary:** only if every m = 1 arm stalls
with best maxR > 1×10⁻⁶ (Phase 313's registered
trigger): one arm at the best m = 1 N, 5 random
starts, max_nfev 1300.

**Density read:** ρ_fit,s = T_fit(x_s)[0,0] from the
direct path, per site, reported beside ρ_s. (For a
match at the bar, ρ_fit,s = ρ_s to ≤ ~1×10⁻⁹, so the
density at the match is the target's own positive
ρ_req; the per-site difference is reported — verified,
not assumed.)

**Pricing (on a match):** the global amplitude scale
|a|² of the winning configuration and the per-site
implied s²_s = |That_s(k*_s,k*_s)| /
|T_unit,s(k*_s,k*_s)| with T_unit the
unit-normalised configuration's tensor at site s
(Phase 257 Leg-3 form; for an exact joint match
s²_s = |a|² at every site — a consistency check,
reported). **QI:** no QI read for any extended-class
member exists in the record (Phases 312/314 computed
none; Gate-35 computed none) and none is invented;
the matched configuration's QI price is therefore
NOT quoted.

**Diagnostics:** D-a (per-site amplitude refits at
frozen momenta/spins, Phase 313 form) on the winning
configuration — always run on a match. D-b (per-site
full refits alone from the joint solution) — run
only if the joint fit stalls above the match bar, to
distinguish "individually fittable, not jointly"
(joint-sharing obstruction) from "not fittable at
all" (a site's tensor resisting the sector). The
per-component stall anatomy of the best fit is
always recorded. Segre types of the fitted tensors
are compared against the targets' per site.

**Structural diagnostics (Gate-34 Item 3 standard)**
— on a match, at the N = 6 solution if N = 6 matched
(the Gate-34-comparable configuration), else at the
winning configuration:
(a) *Jacobian:* the 40 × 7N Jacobian of the
|That|_F-normalised residual vector at the solution,
by central finite differences; full singular-value
list, rank, and σ_min reported.
(b) *Perturbation ladder:* each target perturbed
componentwise by symmetric noise of relative size
ε × |That_s|_F (symmetric 4×4 noise, entries iid
uniform(−1, 1), rng seed 3202) and re-fit (warm from
the winning configuration + one fresh random start,
2 draws per rung, max_nfev 900) at
ε ∈ {1×10⁻¹², 1×10⁻⁹, 1×10⁻⁶, 1×10⁻⁴}; per rung,
the best max R (direct-path verified) and the
matched densities are reported.

## Verdict forms (registered, ledger 795; binding)

1. **MATCH AT POSITIVE DENSITY** — match at the bar,
   jointly at all four sites, with the density at
   the match positive at all four sites (= the
   target's own positive ρ_req, to the reported
   per-site differences). Report: the superposition
   (persisted in full), the residuals per site, the
   density at the match per site, the pricing, the
   structural diagnostics, and the extent/coverage
   successors the result opens (named in the memo's
   fence item).
2. **NO MATCH AT REGISTERED SCOPE** — no arm reaches
   the bar. The anatomy is owed: which components at
   which sites resist (per-component stall pattern
   of the best fit, against the Phase 31 sign-pattern
   class), the best residual set against the counting
   threshold (the below-threshold arms' bests and the
   at/above-threshold arms' bests stated separately),
   the D-b discrimination, and whether the
   obstruction is algebraic (the superposition's
   reachable set / joint sharing / rank — with the
   Jacobian read at the best fit where it informs)
   or numerical (start-dependence at fixed reachable
   set). A stall in (1×10⁻⁹, 1×10⁻⁶] is a near-match,
   NOT a match: reported under this form with its
   stall anatomy. Any proper nonempty subset of the
   four sites reaching the bar is named exactly
   inside this form, with per-site residuals.

## Item 3 — fences (owed whatever the verdict)

- **Binding-site scope:** the match's scope is the
  four binding sites under the site rule — a
  pointwise supply at four sites. (For this member,
  unlike Phase 313's, the target's positivity is
  independently a continuum statement at adversary
  grade (Gate-35 G35-B); that is the TARGET's claim,
  at Gate-35's scope — the MATCH's scope remains the
  four sites. No extent statement is made or
  implied: extent on this background is not this
  phase's question.)
- **No energy-condition or front pass is implied by
  a match:** the member's SET EC reads remain
  violated (NEC min −1.170007×10⁻³, WEC min
  −1.044069×10⁻², DEC min −1.000003, SAMPLER-M) and
  its depth is a negative NEC read (−5.327659×10⁻⁴
  SAMPLER-M polished; exact pointwise reads at the
  sites are more negative and are quoted named).
  Those violations are Phase 317's question and are
  untouched by this verdict either way. A match is
  not a front pass, not a configuration on the
  background, not sustainment, not transport
  (Gate-25 restated-wording discipline: pointwise
  existence of a supplying superposition; no global
  on-background existence, normalisability, or
  sourcing of a drive is claimed).
- **Sampler naming:** SAMPLER-M vs exact pointwise
  named wherever a T_req or NEC value is quoted.
- **DESK:** the winner is a configuration, not a
  datum — NO DATA CONTACT unless a genuine data
  contact is found (none is expected; none is to be
  manufactured).

## Independent checker

`work/p320_check.py`, mirroring Phase 313's checker:
loads the persisted targets and the persisted joint
best fit; recomputes every deciding number via the
DIRECT bilinear path only (no pairwise/S machinery);
re-derives ALL FOUR targets from p312_lib (T_at_ext
+ eulerian_that) to guard the targets file; compares
against the driver's stored results and re-derives
the verdict from the registered forms above.

## Standing fences

Registration and verdict forms before computation
(this file). Controls first. Margins alone never
decide: the verdict is a tensor-residual + density
read. SET reads are set reads; the polished site is
an adversary-polished local worst under the
registered protocol, not a certified global minimum.
No ledger append, no launches, no external contact.
Writes inside phase320/ only.
