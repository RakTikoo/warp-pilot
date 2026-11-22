# P21-3 — Formulation & Coupling Audits (three published-claim checks)

Worker memo, Phase 21 item P21-3. Method (fixed, per CHECKPOINT21 §P21-3):
independent transcription from the fetched paper, background closure at
transcription tolerance on the paper's own solution, full-EC read on BOTH
matter and effective sector on the paper's full domain, conservation read,
verdict VERIFIED / REFUTED / PARTIAL with the exact deciding clause.
Untranscribable printed equations are logged, never fabricated
(Phase-3 Das–Paul precedent). float64 throughout.
Scripts: `p213_a_palatini.py`, `p213_b_hybrid.py`, `p213_c_emsg.py`;
numbers: `results/p213_results.json`.

---

## (a) Palatini f(R) wormholes — Bambi, Cardenas-Avendaño, Olmo & Rubiera-Garcia (2016)

**Paper.** "Wormholes and nonsingular space-times in Palatini f(R)
gravity", Phys. Rev. D 93, 064016 (2016), arXiv:1511.03755 (fetched).
**Model.** Palatini f(R) = R − γR² (γ > 0) coupled to Born–Infeld
electrodynamics, electric ansatz, charge q, scales r_q, l_β,
r_c = (4π)^{1/4}√(r_q l_β), z = r/r_c, α ≡ γ/(2π l_β²); audited at α = 1
(the paper's Fig. 1/2 solid curve; every verdict-relevant conclusion is
α-independent for α > 0).

**Exact claim sentences.** Abstract: the point-like singularity "is
replaced by a finite-size wormhole structure, which provides a
geodesically complete and thus nonsingular space-time, despite the
existence of curvature divergences at the wormhole throat."
Conclusions: "this result follows from a combination of gravitational
and matter actions that satisfy all the energy conditions".

**Transcription discrepancy (logged, Das–Paul style).** The fetched
ar5iv rendering's eqs. (10)/(11)/(13)/(16) are mutually inconsistent:
η as rendered in eq. (13) gives η(z_c) = 32.31 at the rendered
eq. (16) z_c = 0.1708 (α = 1), whereas eq. (18) requires η(z_c) = 1/α;
and the G′(z) of eq. (7) with eqs. (10)/(12) as rendered integrates to
an asymptotic coefficient 3× the one implied by the paper's own
Reissner–Nordström expansion eq. (15) (measured ratio 2.99 at
z = 20–100). No repair was fabricated. η was instead *derived* from
equations that are unambiguous — the Born–Infeld trace
T = (1/2π)(φ − Xφ_X), the flux condition φ_X F^{tr} = q/r², and the
algebraic trace equation of f(R) = R − γR² — giving
η(z) = 2(√(1+z⁻⁴) − 1), f_R = 1 − αη, which reproduces eq. (12)
exactly and puts the f_R zero at z* = [4α²/(4α+1)]^{1/4} = 0.9457
(α = 1), not at the rendered 0.1708.

**Closure.** Trace equation: f_R R − 2f = −R identically (sympy), so
R = −κ²T as the paper states. Radial-null geodesic eq. (29) integrated
on the derived model: Δλ·E from z = 2 to z*+ε grows as ε^{−1/2} with
(Δλ·E)·√ε → 0.512 at ε = 10⁻⁴, against eq. (30)'s predicted asymptote
z*/√c = 0.504 (c = f_R′(z*) = 3.525) — the geodesic equations close at
2%. A(z) at δ₁ = δ₂ = 1: −1.158 (z = 1, inside the horizon region),
0.500 (z = 2), 0.802 (z = 5), 0.950 (z = 20), approaching the RN form.

**Matter ECs (Born–Infeld source, eq. (4)).** With s = 1/z⁴,
X/β² = s/(1+s), φ_X = √(1+s) (derived, above): ρ = −p_r exactly
(NEC1 saturated, ρ + p_r = 0), and on z ∈ [z*, 10³]: ρ ≥ 0,
ρ + p_t ≥ 0, ρ + p_r + 2p_t ≥ 0, ρ − |p_r| = 0, ρ − |p_t| ≥ 0 — all
four ECs hold on the full domain (minima are the infimum 0 at
infinity). At the throat (dimensionless units): ρ = 1.333,
p_r = −1.333, p_t = 0.333. **The "no exotic matter" clause is true
for the matter sector.**

**Throat regularity in both metrics (registered addition).**
f_R(z*) = 0 exactly, with f_R > 0 for z > z*.
- Physical metric g: Kretschmann scalar computed numerically from the
  full transcribed functions A(z), f_R(z), x(z) (finite-difference
  Riemann at θ = π/2): K_g = 4.84×10² at ε = z − z* = 0.01, rising to
  7.51×10⁴ at ε = 10⁻³ — divergent at the throat, consistent with the
  paper's own eq. (20), K ∼ (z − z_c)⁻² (the FD log-log slope over
  ε ∈ [3×10⁻³, 5×10⁻²] is −0.81, not a clean −2; the divergence
  itself is unambiguous, the exponent is FD-limited).
- Auxiliary metric q = f_R·g (the paper's h): K_q = 1.36×10⁵ at
  ε = 0.01, 1.29×10⁹ at ε = 10⁻³ (FD slope −2.72) — also divergent. And since
  f_R(z*) = 0, q *degenerates* at the throat surface (det q → 0):
  the auxiliary metric is not a regular metric there at all.

**Do g-geodesics see a traversable throat? No.** Radial null
geodesics reach the throat only at *infinite* affine parameter
(Δλ·E = 51.2 already at ε = 10⁻⁴ and growing ∝ ε^{−1/2}); timelike
and non-radial null geodesics turn back before the throat (paper
Sec. IV, eq. (28)). The paper itself concludes the two sides are
"causally disconnected from each other, and therefore cannot
exchange information" — the wormhole lies on the future/past causal
boundary. Corroborated independently by Olmo, Rubiera-Garcia &
Sanchez-Puente, arXiv:1710.08712: for the f(R) family "the wormhole
structure lies on the future (or past) causal boundary and cannot be
reached in finite affine time by null geodesics".

**Conservation.** ∇^g T = 0 identically for the sourceless
Born–Infeld field (paper Sec. IV) — as Palatini f(R) requires.

**Effective sector.** By construction G(g) = κ²T_eff with T_eff the
GR-prism source; it necessarily carries the flare-out NEC violation
at the throat (this is the relocation the paper intends; reported,
not held against the claim, whose wording is about the matter and
the action).

### Verdict (a): PARTIAL
Deciding clauses: the matter clause is VERIFIED (Born–Infeld source
satisfies all four ECs on the full domain, NEC1 saturated) and the
topology clause is VERIFIED (finite-area throat, area
4π r_c² z*² = 0.894 × 4π r_c² at α = 1, charge-without-charge flux).
But the claim's plain wording — a nonsingular wormhole spacetime —
fails two registered additions: (i) **regularity**: curvature
invariants of the physical metric diverge at the throat and the
auxiliary metric q degenerates there (f_R = 0); "nonsingular"
survives only under the paper's chosen definition (geodesic
completeness), not as regularity; (ii) **traversability**:
g-geodesics do not cross — radial null geodesics need infinite
affine parameter to reach the throat and the two sides are causally
disconnected, so the throat living in g is not a traversable throat.
Failure anatomy: both failures trace to the same mechanism, f_R → 0
at the throat — the conformal factor that creates the bounce also
degenerates q, blows up A's 1/f_R terms in g, and stretches the
affine distance to the throat to infinity. Follow-up (Failure
Protocol): the EiBI/Palatini family where the conformal factor stays
finite at the throat (Olmo–Rubiera-Garcia Ricci-squared models) is
the known comparison case where observers *can* cross; it is a
different theory, not a repair of this one.

---

## (b) Hybrid metric-Palatini f(R, ℛ) wormholes — Capozziello, Harko, Koivisto, Lobo & Olmo (2012)

**Paper.** "Wormholes supported by hybrid metric-Palatini gravity",
Phys. Rev. D 86, 127504 (2012), arXiv:1209.5862 (fetched).
**Model.** Action eq. (1): S = (1/2κ²)∫√−g [R + f(ℛ)] + S_m, ℛ the
Palatini scalar; scalar-tensor form (paper): (1+φ)R +
(3/2φ)(∂φ)² − V(φ). **Solution II** (Sec. IV.B, the asymptotically
flat example): Φ = Φ₀ const, b(r) = r₀, φ = φ₀(r₀/r)³, V(φ) eq. (32);
audited at φ₀ = 3 and φ₀ = 5 (units κ² = r₀ = 1).

**Exact claim.** "assuming φ₀ > 0, the energy density is positive
throughout the spacetime… The NEC at the throat takes the form
ρ(r₀) + p_r(r₀) = (φ₀ − 2)/(2κ²r₀²), which is positive, by imposing
φ₀ > 2; it is an easy matter to verify that this specific example
satisfies Eq. (14)" — i.e. matter NEC at the throat with
NEC-satisfying standard matter, the effective sector carrying the
flare-out.

**Closure.** Printed ρ, p_r, p_t (after eq. (32)) against the paper's
field equations:
- eq. (15) (ρ): residual ≤ 2×10⁻¹⁶ at r/r₀ = 1, 1.5, 2, 5. Closes.
- eq. (16) (p_r): residual ≤ 3×10⁻¹⁸. Closes.
- eq. (17) (p_t): closes at the throat (3×10⁻¹⁶) but **fails at O(1)
  for every r > r₀**: residual +1.778 at r = 1.5r₀ (printed
  p_t = 0.240), +0.633 at r = 2r₀ (printed 0.100), +0.0104 at
  r = 5r₀ (printed 0.00467). Anatomy is exact: the residual equals
  2(1 − b/r)·3φ′²/(4φ) at every radius checked, i.e. eq. (17) as
  printed under-weights the 3φ′²/(4φ) sub-term by a factor 3; with
  that single factor the equation closes. Logged as a misprint
  suspect in the printed equation — as printed, Solution II is not
  a solution of the full system away from the throat.
- Klein–Gordon eq. (11): closes to ≤ 3×10⁻¹⁶ at r = 1.5, 2, 5 r₀
  (using T from the printed profiles and V_φ from eq. (32)).
- Two further printed-equation discrepancies, logged not repaired:
  eq. (30) as printed does not integrate to eq. (31) (lhs = 19683 at
  r = 3r₀; with sign flip and (r₀/r)⁶ for (r/r₀)⁶ it closes to
  7×10⁻¹⁸, so eq. (31) itself is sound), and the paper's stated
  trace formula T = [4V + 9φ₀u³(1−2u)]/(2κ²r²) disagrees with the
  trace of its own printed profiles (−0.0211 vs −0.0844 at
  r = 2r₀; opposite sign at r = 5r₀). V eq. (31) ≡ V eq. (32) under
  φ(r): identical (−0.0421875 at r = 2r₀).

**Matter ECs.** At the throat the claim verifies *exactly*:
ρ + p_r = (φ₀−2)/2 = +0.5 (φ₀ = 3), and all six EC combinations are
positive at the throat for φ₀ = 3 and 5. On the **full domain**
r ∈ [r₀, ∞), however: ρ + p_r crosses zero at r = 1.63 r₀ (φ₀ = 3;
2.31 r₀ for φ₀ = 5) and reaches −0.0331 (φ₀ = 3); ρ − |p_t| crosses
at 2.44 r₀ and reaches −0.00593. Asymptotically p_r ∼ −u³ dominates
ρ ∼ u⁵, so matter NEC1 and DEC_t fail on the whole exterior beyond
a throat neighbourhood. The paper's claim is scoped to the throat,
and at the throat it is right; "NEC-satisfying matter" does not
extend over the solution's domain.

**Effective sector (registered addition, scalar DoF included).**
T_eff = G/κ² for b = r₀, Φ const: ρ_eff ≡ 0, ρ_eff + p_r,eff =
−u³ < 0 everywhere — the effective sector (which here *is* the
scalar sector's stress-energy, via eq. (10)) carries the entire
flare-out, as the paper intends. At the throat ρ_matter = 1.8 while
ρ_eff = 0: the scalar/curvature sector supplies the cancelling
share in the tt equation.

**Scalar ghost health (registered addition, entered at the action).**
Jordan action (1+φ)R + (3/2φ)(∂φ)² − V. With Φ = 1+φ the
nonminimal-coupling field, the kinetic term is −Z(∂Φ)² with
Z = −3/(2(Φ−1)); the Einstein-frame (∂Φ)² coefficient is
−Z/Φ − 3/(2Φ²) = **3/(2φ(1+φ)²)**, equivalently 2ω_eff + 3 = −3/φ.
For φ > 0 this coefficient is *positive* — with −+++ signature a
negative time-kinetic term, i.e. a **ghost**. The ghost-free window
is −1 < φ < 0 (with 1+φ > 0), which is disjoint from the throat-NEC
branch: Solution II needs φ₀ > 2, hence φ > 0 everywhere, hence the
NEC-satisfying example lives entirely in the ghost branch of the
scalar sector. (K_EF = +0.0313 at the throat for φ₀ = 3, +2.116 at
r = 2r₀.)

**Conservation.** ∇^μT_μν for the printed profiles: residual
≤ 2.7×10⁻¹⁰ (finite-difference tolerance) at r = 1.5–20 r₀ —
matter is conserved, as minimal coupling in this theory requires.

### Verdict (b): PARTIAL
Deciding clauses: the paper's literal claim — matter NEC at the
throat for φ₀ > 2 — is VERIFIED exactly (formula and throat EC
table). The claim does not survive as a full-domain statement:
(i) **closure clause fails as printed** — eq. (17) is violated at
O(1) for all r > r₀ by the paper's own printed p_t (exact factor-3
anatomy above); (ii) **full-domain EC clause fails** — matter
ρ + p_r < 0 for r > 1.63 r₀ (φ₀ = 3); (iii) **health clause
fails** — the φ₀ > 2 branch is the ghost branch of the scalar
sector (Einstein-frame kinetic coefficient 3/(2φ(1+φ)²) > 0 for
φ > 0; the healthy window −1 < φ < 0 cannot reach φ₀ > 2).
Failure anatomy: the throat NEC is bought by φ₀ > 2, and the same
sign of φ that buys it is the ghost sign; the exterior NEC failure
is structural too (p_r ∼ −u³ vs ρ ∼ u⁵ at large r, for any φ₀).
Follow-up: a φ₀ < 0 (healthy-window) analogue would need
1 + φ > 0 and a different throat-NEC mechanism — the paper's
condition (14) cannot be met there with this ansatz, so no repair
exists within Solution II's family.

---

## (c) Energy-momentum-squared gravity f(R, T²) wormholes — Ganiyeva, Rosa & Lobo (2023)

**Paper.** "Wormhole geometries in f(R,T²) gravity satisfying the
energy conditions", Eur. Phys. J. C 83 (2023) 1040; proceedings
version arXiv:2502.19323 (fetched).
**Model.** f(R,T²) = R + γT², γ = −1; ansatz eq. (10):
ζ = ζ₀(r₀/r)^α, b = r₀(r₀/r)^β with α = β = 1, r₀ = 3M (M = 1),
ζ₀ = −6/5 (the paper's matched example, eqs. (39)–(42)).
Interior domain r ∈ [r₀, r_Σ], r_Σ = 9M/2; exterior Schwarzschild.

**Exact claim sentences.** Abstract: "we demonstrate the existence
of a wide range of wormhole solutions that satisfy all of the
energy conditions without requiring fine-tuning of the model
parameters" and, after matching, "yielding localized, static, and
spherically symmetric wormholes that satisfy all the energy
conditions throughout the entire spacetime."

**The L_m question (registered addition) — the paper never states
L_m.** Θ_ab is not printed either; only its consequences, the
γ-brackets of eqs. (12)–(14). Taking Θ_ab in the standard
Board–Barrow / Katirci–Kavuk form
Θ_ab = −2L_m(T_ab − ½g_abT) − TT_ab + 2T_a^cT_cb, sympy shows all
three printed γ-brackets are reproduced **identically, in all three
components, iff L_m = (p_r + 2p_t)/3** (the mean pressure). L_m = −ρ
and L_m = p_r both fail in all three components (differences stored
in the JSON). So the construction silently uses L_m = p̄; the claim
is meaningless until that choice is supplied, and the paper does
not supply it.

**Closure / root census.** Eqs. (12)–(14) are a quadratic algebraic
system at each r. At the throat, Gröbner lex elimination gives a
degree-8 univariate polynomial in p_t; its four real roots seed
exact polishes — the census is complete: exactly **4 real roots**
at the throat, exactly **one** EC-satisfying:
(ρ, p_r, p_t) = (12.562, 4.185, 4.194). Continuation of that branch
over the interior: all six EC combinations stay positive with wide
margins (minima: ρ = 12.562, ρ+p_r = 16.747, ρ+p_t = 16.755,
SEC = 25.133, ρ−|p_r| = 8.376, ρ−|p_t| = 8.368). The branch is a
near-constant **radiation-like fixed point**: ρ → 4π = 12.566,
p_r, p_t → 4π/3 = 4.189 as r → 30 (tracless limit, where
18p² = 24πp fixes p = 4π/3). Two consequences the paper does not
flag: the density is ρ·r₀² ≈ **113× the geometric scale** 1/r₀²,
and it does not decay at all — the interior is a ball of
near-constant density ~4π cut off at r_Σ, which is why the matching
is mandatory. Exterior vacuum satisfies the ECs trivially, so on
this branch "all ECs throughout the entire spacetime" is literally
true. Effective sector: ρ_eff = b′/(8πr²) < 0 on the whole interior
(−0.00442 at the throat, −0.000873 at r_Σ) — effective WEC violated,
flare-out carried by the γ sector, as intended. Matching:
eqs. (39), (40), (41) are mutually consistent and reproduce the
paper's stated r_Σ = 9M/2, ζ₀ = −6/5, C = (5/9)e^{4/5} = 1.2364
exactly; eq. (42) as rendered gives C = 0.159 instead — logged as a
rendered-equation discrepancy, not repaired (the matching itself
closes through (39)–(41)).

**Conservation (registered addition).** On the EC branch,
∇_μT^μ_r = p_r′ + ζ′(ρ+p_r)/2 + 2(p_r−p_t)/r = **+3.351 at the
throat** (units 1/r₀³), with max relative size **0.9996** of the
sum of its three constituent terms — non-conservation at O(1), not
a small correction, dominated by the essentially uncancelled
ζ′(ρ+p_r)/2 term. This is exactly what the theory requires
(paper eq. (8): 8π∇T = γ∇(Θ − ½gT²)). **No silent conservation
assumption was found**: the paper states ∇T ≠ 0 explicitly
(eqs. (5), (8)), and neither the algebraic construction (12)–(14)
nor the junction derivation uses a hydrostatic/conservation
equation anywhere. This clause passes.

**The other L_m (registered addition).** Rebuilding the full
system with L_m = −ρ (same ansatz, same γ, ζ₀, r₀; geometric parts
transcribed from eqs. (12)–(14), Θ recomputed): a wide fsolve
census (600 starts in [−45,45]³ plus fixed-point seeds) finds 4
real throat roots — **none satisfies the ECs** (all have ρ < 0:
ρ = −0.0044, −4.187, −12.570, −37.696). The radiation fixed point
that carries the claim under L_m = p̄ has no EC analogue under
L_m = −ρ. **The claim does not survive the other standard L_m
choice.**

### Verdict (c): PARTIAL
Deciding clause: the **L_m clause**. On the paper's implicit,
unstated L_m = p̄ = (p_r+2p_t)/3 — reverse-engineered here, not
read off the paper — the audited example verifies: complete root
census with exactly one EC branch, all ECs holding on the interior
with wide margins, smooth matching closing through eqs. (39)–(41),
effective sector reported (ρ_eff < 0 throughout), and conservation
behaving exactly as the theory requires (∇T = O(1), explicitly
acknowledged by the paper, never silently assumed away). But the
claim as plainly worded — EMSG wormholes satisfying all the energy
conditions — is a claim about a theory whose field equations are
not defined until L_m is chosen, and for the other standard choice
L_m = −ρ the same construction has **no EC-satisfying root at the
throat at all**. A claim that flips with an unstated Lagrangian
choice is not verified as stated. Secondary notes: the EC branch
is a single selected root at density ρ·r₀² ≈ 113, near-constant to
the matching radius — "wide range… without fine-tuning" was
audited only at the paper's one worked parameter set, where the
branch is a fixed point rather than a family.

---

## Synthesis (P21-3)

Three formulation/coupling audits, three PARTIAL verdicts, three
different deciding mechanisms — and in each case the NEC-satisfying
matter at the throat, the part of the claim that is usually
headlined, is the part that *checks out*:

- (a) Palatini f(R): matter ECs genuinely hold (BI source, NEC1
  saturated); what fails is regularity and traversability — f_R = 0
  at the throat degenerates the auxiliary metric, diverges K in g,
  and puts the throat at infinite affine distance (causally
  disconnected sides, by the paper's own conclusion).
- (b) Hybrid metric-Palatini: throat NEC formula verifies exactly;
  what fails is everything around it — eq. (17) as printed at O(1)
  on the whole exterior, matter NEC beyond 1.63 r₀, and the
  φ₀ > 2 branch is the scalar's ghost branch (healthy window
  −1 < φ < 0 is disjoint from it).
- (c) EMSG: on its implicit L_m the example verifies completely,
  including O(1) non-conservation honestly stated; what fails is
  that the claim is L_m-relative in a paper that never states
  L_m — under L_m = −ρ no EC root exists at the throat.

Pattern (Phase-3 inheritance): exoticity relocation works only
when structural. Here the relocations are real but each carries a
formulation-level price the headline omits — a degenerate
conformal factor, a ghost sign tied to the NEC sign, an unstated
matter Lagrangian. None of the three is a traversable,
EC-clean wormhole as plainly claimed; none is a fabrication
either. All three verdicts are PARTIAL with the deciding clause
named, per the registered verdict scheme.
