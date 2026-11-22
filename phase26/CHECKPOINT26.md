# FTL Programme — Phase 26 CHECKPOINT (ground record)

**Status:** CLOSED (2026-11-21, coordinator — all four queue items
resolved against their pre-registered criteria; verdict sections
and closure summary at the end of this file).
**Work dir:** `~/workspace/warp-pilot/phase26/` — results in `results/`.
**Parent records read before registration:** `../CHECKPOINT.md` and
`../REPORT.md` (Phase 1: Finalists A/B2 and the compactness frontier),
`../phase5/CHECKPOINT5.md` (H2 rank criterion; H4 curved-background
shells; H6 floor identities), `../phase6/CHECKPOINT6.md` (P6-1:
rank ≥ 2 is necessary, not sufficient, on walls; the binding-null-
direction field is the geometric obstruction; corrected coverage
ceiling 0.096–0.319 after the 8π erratum), `../phase14/CHECKPOINT14.md`
(simultaneity pattern: coverage, solution grade, full ECs and data /
health gates bind together), `../phase16/CHECKPOINT16.md` (breathing
shell legal at every instant at β=0.02; dynamics buys nothing; the
static family breaks at β≈0.025–0.03).

## Mission (Rakshit, 2026-11-21 22:09 PT — steering for this phase)

Test new theories. A very good SUBLUMINAL result counts: find and
develop the BEST one. Keep creating our OWN theories. Expand the
scope if needed. Hunt hidden physics and variables nobody has
scanned. The programme goal remains traversable wormholes and FTL
somehow; this phase's headline deliverable is the best fully legal
subluminal configuration, with new-theory and origination work in
parallel.

## Standing rules (binding)

- float64 everywhere. No float32/16 in any verdict path.
- FAILURE PROTOCOL: no item closes on "it failed" — anatomy (site,
  binding condition/term, scaling), ≥1 mechanism-suggested follow-up
  run or explicitly logged with its requirements, and closure only
  on structural evidence with a reopening condition.
- PRE-REGISTRATION: every bar below is fixed before its run. A bar
  may not be edited after the run it governs; amendments are
  appended, dated, marked post-hoc, and never silently broaden a
  pass.
- Published tensor/action forms only for existing theories. For
  originated theories, the action or constitutive law is written in
  this checkpoint (or in the item's run record, before solving)
  BEFORE any scan number is read.
- FULL-EC + CONSERVATION inside every scan: NEC, WEC, SEC, DEC,
  Hawking–Ellis type, all directions, full volume — not NEC alone.
  A configuration is solution-grade only if its own field equations
  (or, for prescribed-geometry audits, the Einstein equations with
  the computed required source) and conservation close at the bars
  below. Designer-sustained rows are labelled as such and cannot be
  called legal configurations.
- SUPERLUMINAL AMENDMENT: β ∈ {1.1, 1.5} are scanned DIRECTLY
  wherever a wall supply is tested. Born-superluminal framing only:
  constant-velocity configurations; crossing c is never modelled
  and no claim may rely on it.
- ANTI-LOOP RULE: no class gets a third revisit without a NEW
  mechanism. Variations of a twice-killed construction are not
  queued; if an item below turns out to be a variation, the worker
  says so and closes it with that finding.
- UNITS DISCIPLINE (Phase 7 / Phase 14): every coverage or supply
  ratio in consistent units, and no verdict rests on a ratio until
  a ratio-free cross-check (absolute margins) agrees.
- LANGUAGE: nothing passing a scan is a discovery. A full-bar pass
  is a GATE CANDIDATE ("candidate under attack"), reported for a
  novelty + independent-verification gate. Scan reads are "scan
  signals" at most.
- INTERNAL ONLY: nothing leaves this machine; no publication, no
  external contact.
- OPTIMISATION DIRECTIVE (Rakshit, 2026-11-21 22:31 PT — process
  only, science standard unchanged; applies from the next item
  launched after its receipt): (1) CODE-FIRST GRINDING — every
  sweep, grid evaluation, EC audit and scan runs as an unattended
  script/background process, launched once and left to run; no
  agent turns spent babysitting iterations. (2) VERIFY BY SCRIPT —
  pass/fail against the pre-registered bars is computed by a
  checker over result files; agents read only the summary output
  and the survivors/finalists. (3) State lives in checkpoint/result
  files; resume from diffs and summaries, not full histories.
  (4) Report at milestones only (item verdicts). (5) For heavy
  batches, prefer GitHub Actions runners on a PRIVATE compute repo
  (workflow_dispatch, chunked jobs, results back as artifacts,
  smoke-test on a known value first) over local supervised runs
  where practical. Machines grind, agents judge. Items already
  running at receipt (P26-1, P26-2a, P26-2c, P26-2d) are not
  disturbed; P26-4 is the first item launched under this directive.
  RIDER (Rakshit, 2026-11-21 22:32 PT): offloading changes WHERE
  compute happens, never HOW MUCH science gets done. Quality,
  execution speed and exploration breadth are explicitly
  protected: same number of candidates and lenses, same grid
  resolutions, same bars, same adversarial protocol, same pace.
  If an offloaded run would ever be slower, coarser or narrower
  than the agent-supervised way, do it the better way instead and
  note the conflict in the milestone report — never silently trade
  quality for token savings.

## Common verdict bars (registered 2026-11-21, before all runs)

A configuration is **FULLY LEGAL** for this phase iff, on the
audited volume (wall/throat support plus cavity and exterior
control regions):
1. Hawking–Ellis Type I at every audited point (Type-I fraction
   = 1.000 beyond the registered FD-floor treatment);
2. worst NEC, WEC, SEC and DEC margins > 0 at two resolutions
   (h and h/2; h = 0.3/0.15 in programme units unless an item
   registers its own ladder), with the sign stable and not
   shrinking toward zero at the FD rate — i.e. the margin exceeds
   the item's measured FD floor by ≥ 3×, the floor being measured
   on the item's own vacuum/GR controls;
3. field-equation / realisation residual at the item's registered
   solution-grade bar (default: relative median ≤ 0.02 against the
   equations' own scale, the programme's standing tol pattern), and
   conservation residual likewise ≤ 0.02 relative median where the
   theory carries a conservation/Bianchi constraint;
4. every class health gate passes (no ghost: kinetic coefficients
   positive; no gradient instability: sound speeds real; no
   superluminal *signal* speed where the class forbids it — see
   P26-2c's two-cone rule; strong-coupling loci named, not hidden);
5. data gates where they bind (Phase 1 D1–D5: GW170817 c_T window,
   PPN/fifth-force, Fermi dispersion), each labelled by the
   three-case rule.
**BEST** (P26-1, pre-registered): highest β at full legality;
ties broken by lower ADM mass in kg; further ties by larger worst
margin. A β=0 static equilibrium is not a drive and cannot win.

---

## P26-1 — THE BEST SUBLUMINAL DRIVE (rung 2b, optimisation)

**Question.** Across every home that has ever produced a legal
MOVING configuration, what is the highest β attainable under the
full bar set above, and what is the complete ledger of the best
configuration?

**Homes in scope (fixed):**
- (H-a) GR flat named shell family (Finalist A/B2 lineage:
  edge-peaked density, cosine shift on the matter support,
  Gaussian smoothing; Track L frontier: β=0.05 passes at
  compactness M/R1 = 0.383 at every scale; β=0.1 empty for named
  families and free-form, boundary at compactness ≈ 1.0).
- (H-b) GR shells re-solved in curved backgrounds (Phase 5 H4 /
  Phase 6 P6-2: static Schwarzschild passes M_bg = 1, 2; DEC
  crossing at M_bg ≈ 2.5; the β=0.02 areal uniform-shift moving
  case fails in the CAVITY, not the core; AdS passes only on the
  shell-difference tensor — the total tensor carries the
  background's own WEC violation, so AdS rows are eligible only
  under an explicitly stated difference-tensor convention and are
  flagged as such in the ledger, never silently pooled with
  total-tensor passes).
- (H-c) The areal-embedding moving shell (Phase 9 P9-1: PASS in
  areal slicing at β=0.02 at both distances; PG read fails at
  d=50 — slicing-dependence must be carried in the ledger, and the
  β-scaling of the areal pass is this item's registered test).
- (H-d) The breathing shell (Phase 16: δ=0.5, T=40 legal at every
  instant at mean β=0.02; static family breaks at β≈0.025;
  quasi-static T=200 control passes at δ=1.0 where T=40 fails —
  rate, not amplitude, binds).

**Registered optimisation plan.**
1. Reproduce the stored anchors first (Finalist A, B2, frontier
   β=0.05 (5,10) M=1.91): margins within the Phase 1 record's own
   agreement scales. A failed anchor stops the item as a machinery
   failure, not a physics result.
2. H-a β-ladder: β ∈ {0.05, 0.06, 0.07, 0.08, 0.09, 0.10} ×
   compactness M/R1 ∈ [0.30, 1.05] × geometries (R1,R2) ∈
   {(5,10), (10,20), (10,30), (20,40)} with the family's profile
   freedoms (smoothing pair, edge-peak parameters, shift window
   inside the matter support — Pattern P3). Screening may use the
   family's fast path; every apparent pass and every rung's best
   row gets the full dense audit (whole volume, h and h/2,
   Type-I + all-EC eigenvalue margins + sampled-null cross-check).
3. H-c β-scaling: the P9-1 areal construction at β ∈ {0.02, 0.03,
   0.04, 0.05} (its own machinery, `../phase9/p92_*`,
   `../phase8/p82_*`); report where the areal pass ends and
   whether the PG failure mode changes with β.
4. H-d dynamic ceiling: breathing δ=0.5 at mean β ∈ {0.02, 0.025,
   0.03}, T ∈ {40, 200}, full-period per-instant audits; the
   frozen-instant margins reported beside the dynamic ones (the
   Phase 16 separation), so a pass is credited to dynamics only if
   the frozen twins fail.
5. H-b: no new moving solve is registered (the PG-sliced moving
   solve is a named unbuilt engine — Phase 6 formulation); this
   item records H-b's ceiling honestly as: static passes only,
   moving = open-by-missing-engine, with the H4 cavity numbers as
   the obstruction of record. (Registering this limitation in
   advance, not discovering it after.)

**Deliverable.** ONE best configuration with its complete ledger
(β, ADM mass geom + kg, geometry, wall profile parameters, worst
margins per EC with sites, Type-I fraction, resolutions, home,
slicing/convention flags), plus a β-ceiling per home with the
binding constraint named for each. If the β=0.05 frontier row
remains best, the deliverable says so and the intermediate-rung
search volume is the rung-1 product.

**Kill / closure.** A home's ceiling is closed only when its best
row at the next β rung fails the full audit with h-converged
margins and the binding EC/site is named. The item itself cannot
be killed (it is an optimisation over verified homes); it closes
when every home's ceiling is measured or its obstruction is named.

STATUS: OPEN — pre-registered, not yet run.

---

## P26-2 — NEW THEORIES, NEXT TRANCHE

Four classes the programme has never touched. Each: action stated
below BEFORE any scan; identification/validation gate before any
wall number; wall scan at β=0.1 plus DIRECT β ∈ {1.1, 1.5} and/or
a throat, on the programme's shared wall bed (Finalist-A family
shell, edge-peaked, M=2.0, R 10–20, s_rho=2.0, s_P=1.16, cosine
shift on [10,20]; stored GR deficits: max NEC deficit 1.981e-4 at
β=0.1, 2.825e-3 at β=1.1, 3.387e-3 at β=1.5) unless the class's own
structure forces a different bed — any substitution is stated in
the run record before solving, with the GR control on the same bed.
Full bars = the common bars above, plus the class health gates
named per item. Verdicts per class: ALIGNMENT (full-bar legal
supply at some β — Gate candidate), PARTIAL (coverage or legality
in a proper subset, named), KILL (no row reaches partial ≥ 0.50
coverage at β=0.1 with health passing, or the class's supply is
shown structurally incapable — anatomy required), or
IDENTIFICATION FAILURE (the published equations cannot be
implemented faithfully with this machinery — the obstruction is
the deliverable, and no wall numbers are read off an ungated
tensor).

### P26-2a — Nonlocal infinite-derivative gravity (IDG)

ACTION (registered): the ghost-free entire-function class
(Biswas–Mazumdar–Siegel / Biswas–Geronimo–Koivisto):
  S = ∫ d⁴x √−g [ (M_P²/2) R + (1/2) R ℱ₁(□/M_s²) R
      + (1/2) R_μν ℱ₂(□/M_s²) R^μν
      + (1/2) R_μνρσ ℱ₃(□/M_s²) R^μνρσ + ℒ_m ],
with the ghost-freedom constraint
  2ℱ₁ + ℱ₂ + 2ℱ₃ = 0 and the propagator form factor
  a(□) = exp(−□/M_s²) (entire, no new poles). The NEW VARIABLE is
the propagator itself: the scan variable is M_s (equivalently the
nonlocal length ℓ = 1/M_s) against the wall's curvature scale.
GATE: ℱ_i → 0 reproduces GR exactly on the bed (stored deficits);
the linearised propagator has no pole beyond the massless
graviton (checked algebraically); c_T = c.
SCAN: the class's field equations in the strongest faithful
reduction the machinery supports — the reduction (e.g. linearised
around the bed geometry, or the spherical/static sector equations
as published) is stated in the run record BEFORE solving, and its
scope limits every claim. Supply read = the nonlocal correction's
contribution to the required-matter tensor on the bed, full-EC +
conservation in-scan. Health: ghost-freedom is by construction of
a(□) — the gate verifies the construction, it is not assumed from
the label.
KNOWN RISK (registered): the full nonlinear IDG equations are
integro-differential; if only a linearised reduction is faithful,
the verdict is scoped to it and says so.

### P26-2b — Mimetic gravity

ACTION (registered): Chamseddine–Mukhanov mimetic gravity with a
potential and the Lagrange-multiplier constraint:
  S = ∫ d⁴x √−g [ R/(2κ²) − λ( g^μν ∂_μ φ ∂_ν φ + 1 )
      − V(φ) + ℒ_m ],
φ the mimetic field (the hidden variable: a constrained scalar
whose gradient is unit-timelike by construction, contributing a
pressureless-dust-like sector whose density is an integration
function, not a matter input). The multiplier λ is solved from
the theory's own equations, never prescribed freely: a row in
which λ is chosen to fit the wall is designer-sustained and
labelled.
GATE: λ = 0, V = 0 reproduces GR on the bed; the constraint
g^μν∂_μφ∂_νφ = −1 holds to solver tolerance on every row.
SCAN: wall rows at β ∈ {0.1, 1.1, 1.5} and a static throat row
(Morris–Thorne ansatz, mimetic sector as the supply), V in a
registered family {0, quadratic, exponential} with coefficients
scanned over a stated grid. Health: the mimetic sector's known
caustic / gradient issues are audited where the reduction allows
(sound speed of the φ perturbations = 0 in the minimal model —
named, not hidden; any extension used to give it a sound speed is
a different action and must be registered as an amendment BEFORE
its numbers are read).

### P26-2c — Disformal scalar-tensor gravity

ACTION (registered): Bekenstein disformal coupling:
  S = ∫ d⁴x √−g [ R/(2κ²) − (1/2)(∂φ)² − V(φ) ] + S_m[ ψ, g̃_μν ],
  g̃_μν = C(φ,X) g_μν + D(φ,X) ∂_μφ ∂_νφ,
matter sees g̃, gravity sees g. C > 0 and g̃ Lorentzian on every
row (gate).
THE HONESTY RULE (registered, this item's core): there are TWO
light cones. Any "effective FTL" appearance is audited by the
FRONT-VELOCITY test in BOTH cones: the physical signal speed for
matter is set by g̃'s cone; the gravitational cone is g's. A
configuration counts as transport-relevant only if a signal can
outrun the GRAVITATIONAL cone's exterior light front — apparent
superluminality that is only a cone mismatch (matter cone wider
than gravity cone, or vice versa) is recorded as exactly that,
never as FTL. (Programme precedent: Phase 2/3 front-velocity
kills — Scharnhorst, Drummond–Hathrell.)
SCAN: φ profiles in the wall-window class, (C, D) in registered
families (C = e^{2αφ}, D = D₀/M⁴ constant and D ∝ X variants),
wall rows at β ∈ {0.1, 1.1, 1.5}; required-matter ECs read in the
MATTER frame (g̃) and the gravitational required tensor in g;
conservation in the frame where the matter action is defined.
Health: no ghost in the scalar sector (kinetic coefficient > 0),
disformal factor non-singular, c_T for tensor modes in g read
against D2.

### P26-2d — Einstein–Gauss–Bonnet–dilaton (EGBd)

ACTION (registered): the string-sector coupling in the
Kanti–Mavromatos–Wiltshire form:
  S = ∫ d⁴x √−g [ R/(2κ²) − (1/2)(∂φ)²
      + α e^{−γφ} ( R² − 4 R_μν R^μν + R_μνρσ R^μνρσ ) + ℒ_m ],
α ≥ 0 the GB coupling (length²), γ the dilaton coupling
(γ = 1 the string value; scanned γ ∈ {0.5, 1, 2}).
TWO PARTS: (i) CLAIM AUDIT — one named published EGBd wormhole
claim (Kanti-class dilaton-GB throat) transcribed independently
and audited at the full bars (background closure from the
published equations, full ECs on matter AND on the effective
sector separately, health: the class's known tensor-speed and
hyperbolicity caveats at the solution's own couplings, stated);
(ii) ORIGINATION SCAN — wall rows at β ∈ {0.1, 1.1, 1.5} and/or
throat rows over α (in units of the bed's curvature scale) on a
stated grid, with the published EGBd field equations (variation
of the action above — derived or transcribed and gated against
the α → 0 GR limit and against the audit part's equations).
Health gates: α small enough that the solution stays in the
class's hyperbolic regime where that is checkable; rows outside
are flagged, not silently read.

STATUS (all of P26-2): OPEN — actions registered, not yet run.

---

## P26-3 — ORIGINATION: MATTER WITH A DIRECTION

Provenance: Phase 6's wall anatomy. A wall binds a continuum of
null contractions whose worst direction k*(x) varies across the
wall; scalar-gradient supply F_X (k*·∇π)² cancels directionally
(the flow-aligned component induced by the shift cancels the
spatial contraction), and Hessian supply spikes. Rank is
necessary, not sufficient — the obstruction is a SUSTAINED
DIRECTION FIELD. Both items below are our own constructions aimed
at exactly that: matter whose stress carries an intrinsic,
sustainable direction. Actions/constitutive laws registered here,
before any scan.

### P26-3a — Relativistic elastic media ("solids") in GR

CONSTITUTIVE FRAMEWORK (registered): the Carter–Quintana /
EFT-of-solids formulation. Matter = three scalar fields φ^I
(I = 1,2,3, the comoving material coordinates) with internal
volume-preserving diffeomorphism invariance; define
  B^IJ = g^μν ∂_μ φ^I ∂_ν φ^J,   b = √det B,
  I₁ = tr B / b^{2/3},  I₂ = tr B² / b^{4/3},  I₃ = det B = b².
ACTION: S_m = ∫ d⁴x √−g F(I₁, I₂, I₃) with F ≤ 0 the stored-
energy density in the material frame; the stress tensor is the
metric variation of S_m (derived in the run record and gated:
F depending only on b reproduces a perfect fluid with
p = −F + b F_b; the unstressed configuration F = −ρ₀ at I₁ = I₂
= 3, I₃ = 1 reproduces dust-free equilibrium with zero stress
anisotropy).
REGISTERED FAMILIES: (i) neo-Hookean-type
F = −ρ₀ [ 1 + (μ₁/2)(I₁ − 3) + (μ₂/2)(I₂ − 3)
      + (K/2)(ln b)² ], μ₁, μ₂ ≥ 0 the shear moduli, K ≥ 0 the
bulk modulus; (ii) a strain-stiffening variant with (I₁ − 3)²
term, coefficient ≥ 0. A solid sustains anisotropic stress BY
CONSTITUTION (p_∥ ≠ p_⊥ under strain) — that is the mechanism
under test.
STABILITY BARS (the solid's own, registered): longitudinal and
transverse sound speeds real and ≤ c everywhere on the audited
configuration (computed from F's derivatives in the material
frame); strong-ellipticity / moduli positivity (μ₁, μ₂, K ≥ 0
and the acoustic tensor positive); ECs are CHECKED anyway (the
brief's "by construction" is not accepted — the full-EC read runs
on the solved configuration like any other).
CONFIGURATIONS: (a) a strained-solid WALL: material strained
across the Finalist-bed wall window, strain profile in a stated
family, the Einstein equations solved/required-tensor-audited on
the bed at β ∈ {0.1, 1.1, 1.5}; (b) a strained-solid THROAT:
spherically symmetric strained ball/throat ansatz, throat rows
over (μ₁, μ₂, K, strain amplitude). The strain must be
sustainable: φ^I maps must remain regular (det ∂φ ≠ 0, no
material caustic) on the whole volume — a torn or folded material
map is a failed row, named as such.

### P26-3b — Kalb–Ramond 2-form backgrounds

ACTION (registered): Einstein gravity + a 2-form B with
field strength H = dB and a potential on its invariant:
  S = ∫ d⁴x √−g [ R/(2κ²) − (1/12) H_μνρ H^μνρ − V(𝒝) ],
  𝒝 = (1/2) B_μν B^μν,  V ∈ {0, (m²/2)𝒝, λ𝒝²/4} registered
families. Stress tensor (derived in the run record, gated against
the V = 0 Maxwell-like limit and the B → 0 GR limit):
  T_μν = (1/2) H_μ^ρσ H_νρσ + 2 V'(𝒝) B_μ^ρ B_νρ
         − g_μν [ (1/12) H² + V(𝒝) ]   (conventions stated
         in the run record; the gate, not this line, is arbiter).
The 2-form's stress has an intrinsic direction structure (the
plane of B, the kernel of H) — the mechanism under test.
CONFIGURATIONS: sustained "electric" (B_{0i}) and "magnetic"
(B_{ij}) ansätze with the field equations for B solved on the
configuration (a prescribed B that does not satisfy its own
equation d(⋆H) + V' terms = 0 is designer-sustained and labelled):
(a) wall rows on the bed at β ∈ {0.1, 1.1, 1.5}; (b) throat rows
(spherical ansatz, magnetic B on the 2-sphere directions is the
natural sustained case). Full-EC + B-equation residual +
conservation in-scan. Health: H kinetic term sign fixed positive
by the action; tachyon read from V''(𝒝) ≥ 0 on the row's range
where applicable.

**Verdicts (both items).** ALIGNMENT / legal configuration at
full bars → Gate candidate. KILL requires the killing term named:
if the direction still cannot be sustained, the deliverable is
WHICH term kills it (directional cancellation reappearing in a
new guise, sound-speed/ellipticity failure, material-map
singularity, B-equation residual that will not close) and how it
scales. Intermediate outcomes named exactly.

STATUS: OPEN — laws registered, not yet run.

---

## P26-4 — HIDDEN-VARIABLE LEDGER (synthesis; runs LAST)

**Task.** From ALL programme results to date (Phases 1–25
checkpoints, including the running phases' records as they stand
at run time), tabulate every degree of freedom / sector / variable
that has ever CHANGED A VERDICT — candidates named in advance from
the steering: screen fields (Phase 15/17 symmetron χ), Weyl shadows
(Phase 21 braneworld E_μν), second metrics (bimetric f, Phases
14/19/25), running couplings (Phase 23/24 asymptotic safety),
disformal factors (P26-2c), plus whatever the records actually
contain (γ-crossing functions, Lorentz fields Λ, shift windows,
background curvature, boundary terms, species number, strain,
2-form planes…). For each: where it changed a verdict, which way,
and its current status (live / killed / dormant).
**Combinations matrix.** Mark which pairs/triples of LIVE-or-
dormant variables have never been tried together — e.g. screening
× a surviving home; a disformal factor on P26-1's best
configuration; a boundary term on a ledger-ranked throat.
**Deliverable.** A ranked shortlist of untested combinations, each
with: the mechanism it would exploit (one paragraph), why it is a
NEW mechanism and not a variation (anti-loop test, applied in
writing), the cheapest decisive test, and its pre-registered kill
bar in draft. This shortlist is the Phase 27 queue head.
STATUS: OPEN — runs after P26-1/2/3 land.

**AMENDMENT (2026-11-21, appended BEFORE the P26-4 run — the
Phase 27 interface):** a Phase 27 ("working backward", target-first
inverse solves) is being launched in parallel and consumes this
shortlist as its main input. Every shortlist entry must therefore
additionally name the concrete TARGET it would serve, in one of
the registered target forms: (i) a THROAT SPEC (throat radius /
flare profile class / traversability quantity it would move);
(ii) a WALL β (the β rung and bed it would attack, e.g. first
full-bar legality at β=0.1, or a superluminal row); or (iii) a
BEST-SUBLUMINAL IMPROVEMENT (the P26-1 quantity it would beat —
higher β at full legality, or equal β at lower ADM mass, with the
current best value quoted from the landed P26-1 ledger). An entry
whose target cannot be stated in one of these forms is not
Phase-27-consumable and is demoted to the unranked annex, with the
reason stated. No other change to the P26-4 task.

---

## Sequencing

P26-1, P26-2, P26-3 run in parallel (separate workers, separate
result files: `results/p261_*`, `results/p262*_*`, `results/p263*_*`).
P26-4 runs last, from the landed records. The coordinator
integrates verdict sections into this file from worker memos +
result JSONs; workers do not edit this file. Final synthesis at
queue end: per-item verdicts, THE BEST SUBLUMINAL CONFIGURATION
as its own headline section, rung verdicts (1 / 2a / 2b), and the
Phase 27 queue head.

## Environment

Python 3.12. Phase 1 venv at `~/workspace/warp-pilot/venv`
(numpy 1.26.4 stack); system python3 numpy 2.2.6 / scipy 1.14.1 /
sympy 1.12 — every script states which it used. Programme
machinery: Phase 1 judge `../verify_metric.py`, shell factory
`../shell.py`; Phase 5 H4 solver `../phase5/h4_resolved_shell.py`;
Phase 9 areal machinery `../phase9/p92_*`, `../phase8/p82_*`;
Phase 16 dynamics `../phase16/p161_dynamic.py`; Phase 7
non-stationary auditor `../phase7/p74_auditor.py`.

---

## P26-1 — VERDICT: BEST SUBLUMINAL CONFIGURATION IMPROVED — β = 0.07 (Gate candidate)

Run 2026-11-21: `p261_*.py`; results `results/p261_memo.md`,
`results/p261_ledger.json` (+ raw JSONs). Float64. No bar moved;
no post-hoc amendment needed.
PLAIN LANGUAGE: the programme's best verified drive got faster.
The Phase-1 frontier stopped at β=0.05; a systematic ladder over
the intermediate rungs found full legality at β=0.06 (three rows)
and at β=0.07 (one row). The speed was bought with thickness and
compactness, not lightness.
ANCHORS: all reproduce. Finalist A/B2 positive, Type-I 1.000,
h-stable. The frontier anchor initially failed on a worker error
(wrong profile: the stored winner is wd=1.0, floor=0.1, M=1.9125);
with the stored profile the reproduction is exact (worst +5.930e-07
vs stored +5.9299e-07 at h=0.075) — caught against the record and
documented in the memo.
THE BEST CONFIGURATION (H-a, complete ledger): thick shell
(R1,R2) = (10,30); ADM mass 8.0 geom = 1.0773e28 kg; compactness
M/R1 = 0.80; edge-peaked density (wd=6.0, floor=0.2); Gaussian
smoothing (4.0, 2.32); cosine shift on [10,30]. Fine audit (1,404
pts, h=0.3/0.15): whole-volume worst margin SEC +2.59e-07 at both
h (binding point in the exterior Gaussian tail, r=37.0 — the
family's usual tail-limited worst); core NEC +3.76e-05, WEC
+3.28e-05, SEC positive, DEC +1.97e-05/+1.78e-05 (binding at
r=10.25); Type-I fraction 1.000; sampled-null cross-check positive
(core NEC +1.24e-05/+9.3e-06); worst margin ≈10× the measured FD
floor (2.6e-08). LANGUAGE: Gate candidate only — it goes to a
novelty + independent-verification gate before any stronger word.
CEILINGS PER HOME (binding constraint named):
- H-a — ceiling β=0.07, CLOSED. One site binds the whole ladder:
  the inner edge r ≈ R1+0.25. β=0.08's best row passes the coarse
  dense audit but the fine audit finds NEC −5.26e-07 @ r=10.25 at
  h=0.15 (sign-unstable — fails the sign-stability bar); β=0.09:
  NEC −1.10e-06 @10.25; β=0.10: mid-shell SEC −2.99e-05 @ r=18.8,
  h-stable (the Phase-1 wall, re-measured from inside the family).
  Search volume: 144 + 588 screening/refinement evals, 64 dense,
  18 fine audits. Mass honesty: the β=0.07 row is 5.7× the mass of
  the lightest β=0.05 row (2.58e27 kg at (5,10)) — "best" is by
  the pre-registered rule (highest β, then mass), and the
  lightest-at-β=0.05 record stands separately.
- H-b — static only, as registered. Moving = open-by-missing-
  engine (PG-sliced solve formulated in Phase 6, unbuilt).
  Obstruction of record: H4 cavity NEC −1.95e-04 at β=0.02,
  M_bg=1 (uniform shift × background curvature; core passing).
  Static DEC crossing M_bg ≈ 2.5 stands.
- H-c — ceiling β=0.02, CLOSED, slicing flag carried. β=0.02
  reproduces P9-1 exactly (core +2.934e-05 @ h=0.2, d=50). β=0.03
  fails in the CORE (worst −1.27e-04 @ h=0.1, Type-I 0.935,
  cavity still at floor); Type-I degrades monotonically to 0.542
  at β=0.05. The PG read fails at every β.
- H-d — ceiling mean β=0.02, CLOSED; dynamics buys nothing.
  β=0.02 passes at T=40 (worst instant +7.203e-06, reproducing
  Phase 16 exactly) and T=200. β=0.025 and 0.03 fail at both T
  WITH FROZEN TWINS ALSO FAILING — the binding cause is the frozen
  family's β≈0.025 break at the breathing extremes; dynamics adds
  a secondary tax at T=40 but is never the binding cause. No pass
  anywhere is credited to dynamics.

## P26-2a — VERDICT: KILL at all β (scoped to the linearised BGK reduction)

Run 2026-11-21: `p262a_gate.py`, `p262a_scan.py`,
`p262a_anatomy.py`; results `results/p262a_memo.md`,
`p262a_scan.json`, `p262a_run_record.md`, `p262a_gate.json`,
`p262a_anatomy.json`. Float64.
GATE PASS: ℱ_i→0 reproduces the stored GR deficits exactly
(binding counts 251/504/594; deficits 1.981e-4 / 2.825e-3 /
3.387e-3). Pole check algebraic: a(z)=e^{−z} entire and zero-free,
a(0)=1 — only the massless graviton pole. c_T = c. Health passes;
the kill is on supply.
REDUCTION (stated before solving): the full nonlinear IDG
equations are integro-differential and were NOT solved. The
implemented reduction is the published linearised BGK system
(Boos–Pinedo Soto–Frolov arXiv:2004.07420): a(□)G⁽¹⁾ = 8πT as a
prescribed-geometry audit T_req = a(Δ)G_bed/8π, ℓ = 1/M_s the
only scan variable. All claims are scoped to this reduction.
RESULT: every readable row at every β has partial-coverage
fraction 0.000 and negative median coverage ratio; the anti-supply
grows ∝ ℓ² and with β (leading-term median ratio per ℓ²: −0.122 /
−0.148 / −0.174 at β = 0.1/1.1/1.5). Mechanism: the inverse form
factor's spectral multiplier exp(+ℓ²k²) ≥ 1 preserves every mode's
sign and amplifies the wall-gradient band where the deficit
lives — smoothing the source sharpens the demand. ℓ ≥ 1 rows are
operator-unresolved (series unconverged; resolutions disagree in
sign) and were not counted. REOPENING CONDITION: a source-first
item (legal matter → the geometry IDG produces → audit it) is a
different, solution-side question needing its own registration;
the nonlinear theory remains untested.

## P26-2b — VERDICT: KILL (structural)

Run 2026-11-21: `p262b_scan.py`, `p262b_throat.py`; results
`results/p262b_memo.md`, `p262b_scan.json`, `p262b_throat.json`,
`p262b_run_record.md`. Float64.
GATE PASS at all β (binding counts exact; deficits to ≤1.1e-4
relative; conservation closes analytically + numerically 4.4e-16).
T^(mim) derived before solving: on-constraint the sector is
pressureless dust of density 2λ, plus a V g_μν term that is
NEC-neutral.
DECIDING THEOREM (congruence-independent): T^(mim)(k,k) =
2λ(u·k)² along any null k — the sign is fixed by λ. With λ ≥ 0
(legal sector) the mimetic sector can NEVER carry an NEC
violation; measured coverage is exactly 0.000 for every positive
flux at every β, and the required matter degrades monotonically
in the flux. The one covering row (negative flux, β=0.1) is
negative-energy dust — sector WEC margin −1.26e-3 — and collapses
superluminally anyway. V ≠ 0 families are excluded by a
stationarity lemma (φ = t + ψ(x) forces V' = 0 on a stationary
wall). THROAT: killed by inequality — ρ_mim + p_r^mim =
2λ(2e^{−2Φ} − 1) ≥ 0 for all Φ ≤ 0, λ ≥ 0, any b(r): flare-out
supply impossible with a legal sector. The solved λ(r) also
diverges ∝ C/r² at the cavity centre (the class's c_s = 0 caustic
disease, realised concretely). REOPENING CONDITION: a modified
action whose on-constraint stress tensor is not sign-fixed dust
(new registration, not a variation).

## P26-2c — VERDICT: KILL

Run 2026-11-21: `p262c_scan.py`; results `results/p262c_memo.md`,
`p262c_scan.json`, `p262c_run_record.md`. Float64.
GATE PASS after one genuine catch: the naive front-velocity
formula assumed ∂φ purely spatial in the Eulerian frame; the warp
shift tilts the frame (d₀ = −(β·∇φ)/α ≠ 0). The corrected
two-cone law (Amendment 1, logged before any scan number) makes
even the transverse cone move, u_⊥ = √((C−D d₀²)/C); frame
identity then holds to 2.2e-16. Disformal-off limit reproduces
GR within 0.7%; GR volume Type-I matches Phase 12's stored row
digit-for-digit.
RESULT (76 rows/β, 65 health-passing): β=0.1 — partial coverage
exactly 0.000 on EVERY health row. β=1.1 — best partial 0.111,
full 0.000. β=1.5 — best partial 0.204, full 0.000. Zero fully
legal rows anywhere. Health otherwise clean (no ghost; c_T = 1
in g, GW170817 case-1 pass). Matter-frame conservation also fails
independently on best rows (0.39/0.34 vs the 0.02 bar).
TWO-CONE ANATOMY: matter-frame NEC ∝ T_req(k̃,k̃) − (k̃·∂φ)² —
the same gradient that reshapes the cone bills the wall, and the
bill (s = |∇φ|² ≈ 0.079 at the registered profile) exceeds the
discount (B ≲ 3e-3, the wall's ordinary stresses) by s/B ≈
25–400 everywhere scanned. The one wider-cone row (D<0, near the
singular edge) does deliver a signal before the g-cone front —
with required matter wildly illegal in its own frame (binding
NEC −2.95, volume WEC −54.8): recorded as CONE MISMATCH ONLY,
not FTL, not transport-relevant, per the registered honesty rule.
REOPENING (named by the kill's own scaling law): the weak-
gradient corner Φ ≲ 0.05–0.2 with |D| ~ C/s ~ 10²–10³ L², where
B > s becomes arithmetically possible — carried to P26-4 as a
dormant variable, not a continuation of this scan.

## P26-2d — VERDICT: claim audit PARTIAL; wall scan KILL

Run 2026-11-21: `p262d_*.py`; results `results/p262d_memo.md`,
`p262d_scan.json`, `p262d_run_record.md`, `p262d_gate.json`,
`p262d_audit.json` (+ supporting gates). Float64.
GATE: PASS in part, PARTIAL overall (hedge intact). α→0
reproduces GR on the bed (ratios 0.89/0.99/0.99); GB scalar on
Schwarzschild matches 48M²/r⁶ to 3e-5; the CKZ H-tensor vanishes
to 4.2e-9; the scalar equation is exactly CKZ's spherical ODE (3);
the throat NEC identity reproduces −2/(f₀r₀²) = −1.8182. NOT
closed: full reduction to CKZ ODEs (1)–(2) and an Eq. (4)
P-term calibration — the scan uses the field equations
transcribed verbatim from Cuyubamba–Konoplya–Zhidenko
(arXiv:1804.11170, Eq. 2); two failed calibration routes are
documented in the run record, not hidden.
CLAIM AUDIT (Kanti–Kleihaus–Kunz, arXiv:1108.3003; representative
γ=1, α/r₀²=0.02, f₀=1.1): PARTIAL. Existence + no exotic matter:
VERIFIED — the throat's radial NEC total −0.07234 splits as
dilaton +0.04538 (canonical, NEC-legal), GB sector −0.11772 (the
entire violation), matter identically zero. Stability of a
subset: REFUTED by CKZ 2018 for ALL parameters (KKK's ansatz
fixed the throat radius, removing the unstable mode); the class
also carries no-strong-hyperbolicity caveats (Papallo
1710.10155; Ripley–Pretorius 2005.05417).
WALL SCAN: KILL (135 rows). Best coverage −2.47 at β=0.1 (the
deficit GROWS), −0.079 at 1.1, +0.015 at 1.5; all rows
designer-sustained (prescribed dilaton, scalar-equation residual
at full scale). ANATOMY: the GB term's NEC sign is fixed by the
local flare geometry — NEC-negative at an areal-radius minimum
(a throat), NEC-positive across this shift-driven wall. The
sector's supply is throat-shaped, not wall-shaped. REOPENING
CONDITION: a wall geometry whose binding region contains an
areal-radius minimum (throat–wall hybrid), or a coupled
metric+dilaton wall solve (new engine) — carried to P26-4.

## P26-3a — VERDICT: KILL (the direction mechanism works; the solid cannot sustain it)

Run 2026-11-21: `p263a_solid.py`; results
`results/p263a_memo.md`, `results/p263a_run_record.md`,
`results/p263a_scan.json`. Float64.
GATES (derivation before scan): Gate 1 fluid limit PASS
(isotropy exact; p = b·dρ/db − ρ to <1e-10). FLAGGED
DISCREPANCY, recorded not absorbed: this checkpoint's §P26-3a
parenthetical "p = −F + bF_b" is the negative of the derived /
thermodynamic relation; the gate-as-arbiter rule was applied.
Gate 2 unstressed PASS (F = −ρ₀, anisotropy exactly 0; reference
pressure p = −ρ₀, NEC-marginal). Gate 3 sound-speed formulas
PASS (isotropic c_s² = (1−ln b)/(ln b), numeric-verified; in
[0,1] only for b ∈ [1.65, 2.72]).
THE POSITIVE RESULT: constitutional anisotropy genuinely
supplies the wall/throat NEC direction and magnitude — NO
directional cancellation (Phase 6's obstruction is answered on
its own terms). Regular wall profiles supply 4.6×–76× the β=0.1
deficit in magnitude; throat flare supply on 33–44% of states,
best 2.8e-2.
THE KILL: supply ∩ phonon-healthy = 0 across all 405 scanned
states. The registered families' volume-normalised invariants
make the phonon kinetic term vanish exactly at the unstressed
state: sound speeds diverge ∝ 1/strain near reference and go
imaginary/ghost-like on the expanded side — exactly where the
supply lives. The only healthy pocket (strong compression,
(μ₁,μ₂,K)=(1,0,1), 9/81 states) is exactly where the NEC identity
forces ρ+pᵢ ≥ 0, i.e. no supply. Wall rows additionally fail
conservation at 0.76×–1.0× the supply itself (~50× the bar;
designer-sustained); A=3.0 profiles fold (det ∂φ < 0) — failed
rows, discarded as folding artefacts. KILLING TERMS: (1) phonon
kinetic degeneracy of the det-normalised invariants, exact form
(1−ln b)/ln b; (2) conservation failure at the supply scale;
(3) material-map singularity at large amplitude. REOPENING
CONDITION (new pre-registration): a family with H_t(𝟙) > 0 —
un-normalised invariants or F_b(1) ≠ 0 — carried to P26-4 as the
top-ranked dormant combination.

## P26-3b — VERDICT: KILL

Run 2026-11-21: `p263b_run.py`; results `results/p263b_memo.md`,
`results/p263b_run_record.md`, `results/p263b_scan.json`.
Float64.
GATES: derivation reproduces the checkpoint's displayed T_μν
coefficient-by-coefficient (FD metric variation of the action:
max rel. error 4.1e-10 — no draft-formula disagreement). B
equation ∇_μH^μνρ − 2V′(ℬ)B^νρ = 0 fixed before scanning. B→0
gate PASS (deficits 1.95e-4/2.83e-3/3.35e-3 vs stored). Constant-B
controls as expected; constant B is sustained only for V=0.
RESULT: the only sustained ansatz on the spherical wall
(hedgehog B_θφ = f(r)sinθ, B-equation solved as an ODE on the bed
metric, residual ≤ 2.1e-6) has on-shell NEC_KR = s² radially,
s² + 2V′u² tangentially — ≥ 0 for every family/branch/amplitude.
The sustained sector is NEC-legal radiation-like matter: it makes
the residual ordinary matter MORE exotic, monotonically (β=0.1:
−1.95e-4 → −4.91e-4 at C=0.02; anti-supply ∝ C²). THROAT: at the
amplitude matching the deficit's magnitude, the residual radial
NEC is −(deficit + s²) to four digits — the sign is exactly
wrong. KILLING TERMS: (1) on-shell NEC sign (algebraic in the
ansatz); (2) B-equation directional non-closure — the plane
electric/magnetic ansätze (the ones with the wall's wanted
direction structure) fail their own equation on a spherical wall,
the residual splitting into parts that cannot vanish together
unless trivial: Phase 6's direction-field obstruction reappearing
one level down, inside the matter equation; (3) branch structure
(V=0 forces a global constant with exotic residual forced in the
vacuum regions; mass/λ branches blow up or arrive with ~1e-7 of
the needed supply). Health passes (no tachyon/ghost) — health
does not save the class. REOPENING CONDITION: a V′<0 potential
family plus a genuinely new ansatz, or a time-dependent /
non-spherical sustained solution of the full B PDE (new
registration).

## P26-4 — VERDICT: LEDGER DELIVERED (checker PASS)

Run 2026-11-21 (first item under the optimisation directive —
script-first extraction, checker-verified): `p264_extract.py`,
`p264_build.py`, `p264_check.py`; results
`results/p264_ledger.json`, `results/p264_memo.md`,
`results/p264_check.json`, `results/p264_candidates.json`.
64 programme files scanned mechanically. VARIABLE TABLE: 33
variables that ever changed a verdict — 4 live, 14 dormant, 15
killed — each with source phase, verdict changed, direction,
status. COMBINATIONS MATRIX over live/dormant variables: 153
pairs (15 tried, 138 untested), 816 triples. RANKED SHORTLIST:
6 entries, each with mechanism, anti-loop justification,
cheapest decisive test, draft kill bar, and a TARGET in a
registered form (throat spec / wall β / best-subluminal
improvement vs the landed β=0.07, 1.0773e28 kg best). ANNEX: 8
demoted entries with reasons (screening × surviving home —
twice-killed, anti-loop bars it; IDG source-first — not a
combination; KR V′<0 — needs a new ansatz first; GJW/species ×
throat — 28-orders open-time gap, no credible target; background
curvature × supply — blocked by the unbuilt PG engine; imperfect
mimetic — unregistered theory; bimetric/dRGT × anything — killed
three times incl. inverse construction; EiBI × hybrid — sector
not computable, no decisive test exists). CHECKER: PASS, 0
errors. Judgement call flagged by the worker and accepted:
disformal factors and elastic strain are DORMANT, not killed —
each killing memo names a specific untested reopening corner,
and shortlist ranks 1 and 3 are built on those corners.

---

## PHASE 26 — CLOSURE SUMMARY (2026-11-21, coordinator)

All four queue items resolved against their pre-registered
criteria. Process note: P26-4 was the first item run under
Rakshit's optimisation directive (code-first grinding, verify by
script, milestone reporting) WITH its rider — no grid, candidate
count, bar or adversarial step was reduced anywhere in the phase;
no offload conflict arose that required the supervised route
instead.

### THE BEST SUBLUMINAL CONFIGURATION (headline, rung 2b)

**β = 0.07** — the programme's fastest fully legal moving
configuration to date, up from the Phase-1 β=0.05 frontier.
Thick GR shell (R1,R2) = (10,30), ADM mass 8.0 geom =
1.0773×10²⁸ kg, compactness 0.80, edge-peaked density
(wd=6.0, floor=0.2), Gaussian smoothing (4.0, 2.32), cosine
shift on the matter support. Fine audit: whole-volume worst
margin SEC +2.59e-07 at h=0.3 AND h=0.15 (≈10× the measured FD
floor), core margins NEC +3.76e-05 / WEC +3.28e-05 / DEC
+1.97e-05, Type-I fraction 1.000, sampled-null cross-check
positive. Status: GATE CANDIDATE — novelty + independent-
verification gate next, no stronger language earned or used.
The lightest-at-speed record is unchanged and separate: β=0.05
at 2.58×10²⁷ kg ((5,10), compactness 0.383). Per-home ceilings:
H-a 0.07 (inner edge binds), H-c areal 0.02 (core binds; PG read
fails at every β — slicing flag permanent), H-d breathing 0.02
(frozen-family break binds; dynamics never helps), H-b static
only (moving open by missing PG engine).

### Rung verdicts

- **Rung 2a (FTL): NOTHING.** No superluminal row in any new
  theory or construction reached even partial legality with
  health passing: IDG anti-supply ∝ ℓ² at 1.1/1.5; mimetic
  sign-fixed dust; disformal best partial 0.204 at β=1.5 with
  full 0.000 and its one wider-cone row recorded as cone
  mismatch only; EGBd wall coverage ≤ +0.015; elastic supply
  unhealthy at every state; KR on-shell NEC ≥ 0. The born-
  superluminal direct-scan discipline held throughout.
- **Rung 2b (practical near-c): ACHIEVED, improved** — the
  β=0.07 Gate candidate above, with per-home ceilings measured
  and the β=0.08 rung's failure localised to a single
  sign-unstable inner-edge point.
- **Rung 1 (new physics): ACHIEVED, several.** (1) The β=0.06/
  0.07 legal rungs inside the "empty" 0.05–0.1 interval — the
  Phase-1 wall was partly a compactness/profile frontier, now
  mapped rung by rung. (2) The elastic-solid result: matter with
  a constitution CAN supply a wall's direction-varying NEC
  demand (Phase 6's obstruction answered) — and the precise
  reason this family cannot sustain it (phonon kinetic
  degeneracy of det-normalised invariants, exact sound-speed
  law (1−ln b)/ln b). (3) The EGBd sector split: a published
  throat's no-exotic-matter claim VERIFIED sector-by-sector
  while its stability claim stands refuted — and the GB supply's
  flare-geometry sign law (throat-shaped, not wall-shaped).
  (4) The mimetic sign theorem (on-constraint stress is
  sign-fixed dust; throat inequality for all Φ ≤ 0). (5) The
  disformal two-cone frame-tilt correction (d₀ = −(β·∇φ)/α)
  and the tax-vs-discount scaling law (s/B ≈ 25–400). (6) The
  IDG anti-supply law in the linearised reduction (∝ ℓ², growing
  with β). (7) The hidden-variable ledger itself: 33 verdict-
  changing variables, their statuses, and the untested-
  combinations matrix.

### Phase 27 queue head (from P26-4's ranked shortlist — each entry is a new mechanism with a stated target)

1. **Elastic solids with H_t(𝟙) > 0 families × the H-a home** —
   remove the phonon degeneracy that alone killed a working
   directional supply. TARGET: first full-bar legality at
   β=0.1 on the Finalist-A wall bed.
2. **EGBd Gauss–Bonnet sector × throat–wall hybrid geometry** —
   embed an areal-radius minimum in the wall window so the
   throat-shaped supply points the right way. TARGET: first
   full-bar legality at β=0.1 on the hybrid bed.
3. **Disformal weak-gradient corner × the P26-1 best
   configuration** — the B > s regime (Φ ≲ 0.05–0.2,
   |D| ~ 10²–10³ L²) spent against a positive margin ledger.
   TARGET: beat β=0.07 / 1.0773e28 kg — legality at β=0.08, or
   β=0.07 at lower ADM mass.
4. **Braneworld Weyl shadow × sign-flip gluing × √-shape
   throat** — the single-clause throat failure (bulk
   realisation) meets the one tool that changes junction
   matching. TARGET: throat spec r₀=1, √-shape, Φ=0 — close
   audit clause (iv).
5. **Tilted Proca × toroidal W2 carrier** — two INTERMEDIATE
   superluminal supplies with complementary caps. TARGET:
   β=1.1 toroidal row above partial 0.60.
6. **DHOST Ia × braneworld Weyl shadow** — the violation as a
   bulk datum, not a 4D matter failure (with "hiding violations
   in E" pre-registered as a kill). TARGET: r₀=1 √-shape throat,
   DHOST brane matter keeping audits (i)/(ii) ≤ 1e-5 and passing
   clause (iv).

Files: CHECKPOINT26.md (this record); scripts p261_*.py,
p262{a,b,c,d}_*.py, p263{a,b}_*.py, p264_*.py; memos, run
records and result JSONs in results/. INTERNAL ONLY — nothing
left this machine. The β=0.07 configuration and any future
full-bar pass go to a Gate (novelty + independent verification)
before any language beyond "Gate candidate" is used.

---

## ERRATUM (appended 2026-11-22 by the Phase 49 coordinator; full text: phase49/results/p491_errata.md)

P49-1 re-anchored the GB tensor and re-read P26-2d. (E1) The
two gate items this phase left open — full reduction to CKZ
ODEs (1)–(3) and the Eq. (4) throat calibration — are now
CLOSED for the anchored tensor (`Q_tensor` 'dd', K=−4; full
system ≤ 1.3e-10; pinned-φ₁ residual ∝ ε). The tensor the
scan used (`CKZ_Q`, CKZ Eq. (2) verbatim) FAILS both tests
(pinned 0.1965 → 0.2074, no ε scaling; spherical tt residual
0.2077/0.0185): the verbatim transcription does not satisfy
CKZ's own spherical system in this implementation. (E2) The
135-row scan re-read on the anchored tensor: best coverage
−2.450 at β=0.1 (stored −2.467, same best row), −0.0076 at
β=1.1 (stored −0.079), +0.0399 at β=1.5 (stored +0.0147);
all rows still designer-sustained. **No verdict wording in
this checkpoint changes** — the P26-2d KILL, its sign law,
and the claim-audit PARTIAL stand verbatim.

---

## ERRATUM (appended 2026-11-22, Gate-6; full record: gate6/GATE6.md §G6-1)

Gate-6 re-audited P26-1 with a fresh auditor (2nd-order direct-∂²
FD, ∂Γ algebraic; the Phase-1 nested-Γ-stencil judge was NOT
used). (E1) The β = 0.07 configuration REPRODUCED (whole-volume
worst SEC +2.580e-07 at h = 0.3 / +2.590e-07 at h = 0.15, vs
+2.591e-07 / +2.593e-07 recorded here; core NEC +3.73e-05, DEC
+1.94e-05/+1.97e-05, Type-I 1.000). (E2) **The H-a ceiling
"β = 0.07" recorded in this checkpoint is WRONG.** The β = 0.08
row's failure rested on ONE point (r = 10.25, non-Type-I
sampled-fallback NEC −5.26e-07 at h = 0.15) which is an artefact
of the nested-Γ-stencil judge: on the gate path the inner-edge
h-ladder (h = 0.3 → 0.0375) gives min NEC +1.7723e-05 →
+1.7670e-05, Richardson continuum **+1.767e-05 ± 1e-07,
POSITIVE**, and the full β = 0.08 audit passes (worst SEC
+2.58e-07/+2.59e-07, Type-I 1.000). **The programme's rung-2b
best is now the β = 0.08 row of the same (10,30), M = 8.0
configuration.** (E3) The β = 0.09 fine row failed at the SAME
impeached point (−1.10e-06, h = 0.15) and is **UNSETTLED**
pending re-audit — Phase 50 owns it; no ceiling above 0.08 may
be quoted either way until it lands. (E4) β = 0.10's failure
was mid-shell and h-stable and is NOT impeached. Novelty note:
Procaccia (posted Oct 30, 2026, academia.edu, unrefereed)
certifies an all-EC Fuchs-form shell to β = 0.1363 in a
different design — any "first/past 0.05" framing for this
family is dead; the claim survives only in Gate-6's restated
wording (gate6/GATE6.md §G6-1), published as v1.9.0.
