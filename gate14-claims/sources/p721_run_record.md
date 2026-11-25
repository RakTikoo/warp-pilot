# P72-1 RUN RECORD — written BEFORE any number is computed

Worker: P72-1 (spinor-supported throats, Einstein–Dirac).
Registration: `phase72/CHECKPOINT72.md` §P72-1. This record fixes
(a) the exact published solutions audited in part (i), (b) the exact
spinor ansatz and throat system of part (ii), (c) the bars, verbatim
where they come from a parent record. No number in this item was
computed before this file was written.

## 0. Scope facts carried in (not re-litigated)

- P31-3's sum-of-squares identity is proved for 2-form field
  strengths and canonical scalars ONLY. A Dirac spinor is neither;
  the identity neither supplies nor forbids this channel.
- P39-1 closed CLASSICAL spin only: the Weyssenhoff spin fluid in
  GR carries Δ_spin(ρ+p_r) = 0 exactly at a static throat. That is
  a classical fluid model; Einstein–Dirac is a different sector and
  P39-1 does not bind it.
- Clause set C (Phases 44/48 form):
  C = {t–t, r–r, θθ, EoM(s), cone, solution-grade, health,
  throat-EC}. For pure Einstein–Dirac in GR there is no scalar
  cone condition; the "cone" slot is taken by the throat
  junction/regularity condition of the spinor ansatz (the
  ε_r-flip consistency at the throat — the clause Danielson et
  al. showed the symmetric BSKR construction fails). This
  substitution is stated here, before numbers, not after.

## 1. Phase-23 traversability bars (confirmed from
##    `phase23/CHECKPOINT23.md`, "Shared human-traversability
##    bars", BEFORE reading any number against them)

- Tidal gradient ≤ 4.905 s⁻² (≤ 1 g across a 2 m traveller) in
  the traveller's frame at the registered crossing speed
  v = 0.1 c relative to static observers (v→c worst also
  reported).
- Crossing between stations at ±10 throat radii: traveller
  proper time ≤ 1 day AND external time ≤ 1 day.
- ADM mass finite and reported in kg / Jupiter masses.

Conversion used: a geometric tidal gradient K [m⁻²] reads
K·c² [s⁻²] against the 4.905 bar (c = 299792458 m/s).

Throat-EC interpretation (registered here, following P39-2's
record): in GR, at any Morris–Thorne throat with b′(r₀) = β < 1,
ρ + p_r at the throat equals (β−1)/(8πr₀²) < 0 by the Einstein
equations themselves — the radial NEC violation AT the throat
is the flare-out identity, required of every throat source, and
is reported as such. The throat-EC clause is therefore read on
the remaining combinations (ρ ≥ 0, ρ + p_t ≥ 0, SEC and DEC
combinations not identical to the flare-out combination). The
full EC set is READ and TABULATED everywhere regardless; this
interpretation governs only what counts as a clause failure.

## 2. Part (i) — published solutions audited

### S-A (AUDITED, exact): the BSKR exact massless solution
- Authors: J. L. Blázquez-Salcedo, C. Knoll, E. Radu,
  "Traversable wormholes in Einstein-Dirac-Maxwell theory",
  Phys. Rev. Lett. 126, 101102 (2021), arXiv:2010.07317; exact
  solution in its footnote, given in full in the companion
  paper "Einstein–Dirac–Maxwell wormholes: ansatz, construction
  and properties of symmetric solutions", Eur. Phys. J. C 82,
  533 (2022), Appendix D, eqs. (D.1)–(D.4).
- Ansatz: metric (EPJC eq. 3.1) ds² = −F₀(r)²dt² + F₁(r)²dr² +
  F₂(r)²dΩ² with F₂(r) = √(r²+r₀²), r ∈ (−∞,∞) (r here is a
  proper-radial-type coordinate; the areal radius is F₂, throat
  at r = 0 with areal radius r₀); two-spinor singlet ansatz
  (EPJC eq. 3.7) with z = P + iQ; ungauged massless fermions:
  q = w = μ = 0; V(r) as in (D.2) (odd extension, V(0) = 0).
- Exact functions (D.1)–(D.3):
  F₀(r) = 1 − [2Q_e²r₀/(Q_e²+r₀²)]·(1/F₂(r));
  F₁(r) = √(1 + r₀/F₂) / √(1 − Q_e²/(r₀F₂));
  P = U₁ − U₂, Q = U₁ + U₂, with U₁, U₂ as in (D.3)
  (κ = +1 fixed; c₀ the spinor amplitude parameter);
  mass M = 2Q_e²r₀/(Q_e²+r₀²) (D.4); domain r₀ > Q_e.
- Parameter values audited: r₀ = 1 (geometric units; the
  solution is scale-free in r₀ because μ = 0 — r₀ is re-priced
  in §4 below), Q_e/r₀ ∈ {0.25, 0.50, 0.75, 0.90}, c₀ = 1
  primary, with a c₀ ∈ {0.5, 2} sensitivity read on the
  field-equation residuals (if the residuals depend on c₀,
  that dependence is itself reported).
- Reconstruction: the closed formulas above, evaluated in
  float64; the Einstein tensor is computed from the metric
  functions by an independent symbolic (SymPy) derivation
  cross-checked against finite differences of the profiles.
  Field equations of the paper: EPJC eqs. (3.10) (Einstein),
  (3.11) (Dirac), (3.12) (Maxwell) — residuals of the exact
  functions in these equations are the solution-grade read.
  Paper's normalisation: G_μν = 2T_μν (EPJC eq. 2.2). EC signs
  are invariant under the positive rescaling to the
  programme's G_μν = 8πT_μν, so EC reads are taken on
  T := G_μν/(8π) directly from the geometry.
- Known scope facts stated by the authors themselves (EPJC
  App. D): the spinor functions do NOT vanish as r → ±∞; the
  wave function is not normalizable and the one-particle
  condition Q_N = 1 cannot be imposed. Recorded as a scope
  fact, priced in the memo, not hidden.

### S-B (NOT AUDITABLE + published refutation on record):
### BSKR numerical symmetric massive EDM solutions
- Same papers as S-A (PRL 126, 101102; EPJC 82, 533 §4):
  two massive (μ > 0) gauged fermions in a singlet state,
  Z₂-symmetric numerical solutions, Q_e/M > 1, connected to
  extremal Reissner–Nordström.
- Gap: neither paper publishes the solution profiles or
  tabulated function data — only figures and asymptotic
  parameters. The functions cannot be reconstructed to audit
  grade from the published record. Resolves NOT AUDITABLE,
  gap named here.
- Published-record fact (not our number): Danielson,
  Satishchandran, Wald & Weinbaum, arXiv:2108.13361
  (Phys. Rev. D 104, 124055 (2021)) prove the BSKR symmetric
  wormholes are NOT solutions of the EDM equations: the
  metric fails to be C³ at the throat, the Maxwell matching
  implies an extra charged shell at the throat, and the
  Dirac matching implies a spurious source term for the
  Dirac field at the throat. This is a solution-grade
  failure on the published record, cited as such.

### S-C (NOT AUDITABLE, gap named): Konoplya–Zhidenko
### asymmetric numerical solutions
- Authors: R. A. Konoplya, A. Zhidenko, "Traversable
  wormholes in General Relativity", Phys. Rev. Lett. 128,
  091104 (2022), arXiv:2106.05034. Smooth asymmetric EDM
  solutions; ODE system (their eqs. 31a–e) and throat data
  (their Table I: qr₀ = 0.03, μr₀ = 0.2, b_i ∈ {0.03,…,0.08},
  g_i, f_i, n_i/σ₊, σ₋/σ₊, Q_±/r₀, M_±/r₀, ωr₀/σ₊ to six
  digits) ARE published.
- Gap: the system is singular at the throat (r′(0) = 0,
  B(0) = 0 in their coordinate x); integration must start
  from a throat power series whose coefficients are NOT
  published (the paper states they "can be calculated" from
  the four throat parameters and gives only the two
  regularity relations (36)–(37)). Reconstructing the
  series and shooting two asymptotic conditions from
  six-digit throat data does not reach this programme's
  audit grade (checker tolerances ≪ 10⁻⁶) within this run.
  Resolves NOT AUDITABLE with this gap named; the series
  reconstruction is registered as a follow-up in the memo.

## 3. Part (i) audit protocol (registered)

For S-A, at each Q_e/r₀ value:
- Full-domain EC read: orthonormal-frame (ρ, p_r, p_t) from
  G_μν on the whole domain (areal radius R from r₀ to
  10³r₀, both sides by symmetry), dense grid, h-refined
  (two grids; a margin counts as converged only if its sign
  and magnitude are stable under refinement). NEC
  all-directions: the tensor is Type I diagonal, so the
  all-directions NEC minimum is min(ρ+p_r, ρ+p_t) exactly;
  WEC/SEC/DEC read in full, not sampled.
- Solution grade: residuals of EPJC (3.10)–(3.12) for the
  exact functions, and the Dirac-equation identity for
  conservation: ∇^μT_μν = 0 must follow from the Dirac +
  Maxwell equations; the residual of that identity is
  REPORTED, not assumed.
- Traversability: the solution's own r₀ is a free scale
  (μ = 0). Reads are made at r₀ = 1 m (priced) and at the
  tidal-bar radius r₀* implied by the throat tidal
  coefficient (computed, not assumed); tidal at v = 0.1c
  and v→c worst; crossing proper/external times between
  stations at ±10r₀ (areal); ADM mass M from (D.4) in kg
  and Jupiter masses at each r₀. A microscopic or
  astronomically large required r₀ is a scope fact, stated.

## 4. Part (ii) — throat system with a Dirac source

Background/form: Morris–Thorne form in the BSKR ℓ-gauge:
ds² = −F₀(ℓ)²dt² + F₁(ℓ)²dℓ² + F₂(ℓ)²dΩ²,
F₂(ℓ) = √(ℓ²+r₀²), ℓ ∈ (−∞,∞), throat at ℓ = 0.
Matter: PURE Einstein–Dirac (q = 0, no Maxwell sector):
two spinors in the singlet ansatz EPJC (3.7),
Ψ^[1], Ψ^[2] with z(ℓ) = P(ℓ) + iQ(ℓ), frequency w,
mass μ, κ = +1, ε_t = +1, ε_r = sign(ℓ).
Field equations: EPJC (3.10) (three Einstein equations)
and (3.11) (two Dirac equations), with V ≡ 0, q = 0.

Registered scan points (fixed here, before numbers):
shapes at the throat β := b′(r₀) ∈ {−1 (Ellis), +1/2
(√-shape)} — equivalently F₁(0) = √(2/(1−β)) ∈ {1, 2} —
with Φ(0) = 0 gauge (F₀(0) = 1), Φ′(0) = 0 (symmetric
extension), and μr₀ ∈ {0, 0.2, 1.0}. r₀ = 1.

Throat system (clause set C, mapped to this system):
- Unknowns at the throat: (P₀, Q₀, w) := (P(0), Q(0), w r₀).
  Slaved at the throat: F₀″(0) by the θθ equation,
  F₁′(0) by the t–t equation.
- t–t clause: the (3.10) second equation at ℓ = 0,
  evaluated with the symmetry condition F₁′(0) = 0 imposed
  — i.e. the equation's prediction for F₁′(0) must vanish.
- r–r clause: the (3.10) third equation at ℓ = 0 (the
  constraint; contains F₀′/F₀ = 0 by symmetry).
- θθ clause: the (3.10) first equation at ℓ = 0 must hold
  with a FINITE F₀″(0) AND the value it slaves must be
  consistent with the extension's F₀″ read (checked in the
  extension, solution-grade clause).
- EoM clauses: evenness of the spinor across the throat
  (P, Q even in ℓ, as the ansatz's reflection symmetry
  requires) forces P′(0) = Q′(0) = 0; the Dirac equations
  (3.11) at ℓ = 0 predict P′(0), Q′(0) from the throat
  data — both predictions must vanish.
- Cone clause (junction/regularity, per §0): the ε_r-flip
  consistency of (3.11) at ℓ = 0 — the same conditions as
  the EoM clauses read from the ℓ < 0 side; a datum that
  satisfies them only on one side carries a spurious
  throat source (the Danielson clause) and fails.
- Health: the Dirac sector is the published canonical one
  (no ghost by construction — kinetic sign fixed by the
  action); the checkable health read is the Noether charge
  density sign, j⁰ ∝ (P₀²+Q₀²)/F₀(0) ≥ 0, and F₀, F₁ > 0.
- Throat-EC: per §1's registered interpretation, full set
  tabulated.
- Closing: the system {t–t, r–r, EoM(P′), EoM(Q′)} is four
  equations in three unknowns (P₀, Q₀, w) at each
  registered (β, μr₀) point — overdetermined by one, a
  genuine closing problem. Solved by least-squares/root
  finding from a multi-start grid; a closing datum is a
  root with all residuals ≤ 1e-10 (SCAN SIGNAL bar of the
  registration), confirmed by an independent second path
  (separate implementation) agreeing ≤ 1e-8.

Extension: from any closing datum (and, for the anatomy,
from the least-squares best datum at each point where no
root exists), integrate (3.10)–(3.11) outward on
ℓ ∈ [0, ℓ_max], R(ℓ_max) = 10³r₀, with (F₀, F₀′, F₁, P, Q)
as state, F₀″ from the θθ equation, F₁′ from the t–t
equation, P′, Q′ from (3.11); the r–r equation is carried
as the solution-grade residual (bar: ≤ 0.02 relative, the
programme's domain standard; the SCAN SIGNAL form
additionally requires the throat residuals ≤ 1e-10 above).
Blow-up, F₀ or F₁ hitting 0, or loss of the solution
before R = 10³r₀ is a Phase-48-type domain obstruction,
named per branch. Independent second path: a second
integrator (different method/step) plus finite-difference
recomputation of the carried residuals from the stored
profiles.

## 5. Verdict forms (from the registration, verbatim intent)

KILL iff (i) every AUDITED published solution fails ≥ 1
full bar by a converged margin (a failure at the numerical
floor is UNDECIDED, named — not a kill) AND (ii) the
throat system admits no closing datum at the registered
points, or closes only with a named domain obstruction.
SCAN SIGNAL iff a datum closes C at residuals ≤ 1e-10
(second path ≤ 1e-8), extends to 10³r₀ without blow-up,
and passes the throat ECs (per §1 interpretation).
INTERMEDIATE otherwise, named clause.

## 6. C12 accounting (registered)

All configurations here are pre-existing static throats.
No formation mechanism is computed; no transport claim is
made or implied by any verdict. Construction-inclusive
accounting is therefore limited to stating, per solution,
its scale and mass price — there is no formation step in
this item whose cost could be booked.

## 7. Machinery gates (must pass before verdict numbers)

G1: SymPy Einstein tensor of the (F₀,F₁,F₂) metric vs
finite-difference evaluation on a test profile: agreement
at FD tolerance.
G2: The exact solution S-A must satisfy (3.10)–(3.12) to
near roundoff if the transcription is right; a failure
here is a transcription defect to fix, NOT a finding
about the paper — unless it survives an independent
re-derivation, in which case it is reported as such.
G3: GR gate for part (ii): with the spinor switched off
(P = Q = 0) and β = −1, the throat demands reproduce the
Ellis values ρ_dem(r₀) = −1/(8πr₀²),
(ρ+p_r)_dem(r₀) = −1/(4πr₀²).
