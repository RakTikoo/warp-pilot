# P33-4 — f(T) + a real scalar — memo

Worker P33-4, Phase 33. Script: `phase33/p334_ft_scalar.py`
(sympy symbolic + float64 numerics). Results:
`phase33/results/p334_results.json`. CHECKPOINT33.md not edited.

## Verdict: **AUGMENTED-FAIL**

Deciding term: the throat field equations fix the **totals**
4πρ_tot(r₀) = −f_T(0)/2 and 4π(ρ+p_r)_tot(r₀) = −f_T(0), so
f_T(0) > 0 forces both totals negative, while any sum of
EC-legal minimally coupled components has both ≥ 0 — and the
tensor kinetic coefficient is f_T(0) with **no** matter
contribution at all. The legality sign ≡ ghost sign identity
is **addition-proof for all minimally coupled matter**. The
proof, with its exact scope, is the deliverable (per the
pre-registered FAIL clause).

## Baseline (not re-litigated)

Gate-5 G5-1 / P20-2: on the Böhmer–Harko–Lobo T≡0 Ellis
family (b = r₀²/r, f(0)=0), matter ECs hold iff f_T(0) < 0,
and S⁽²⁾_tensor = f_T(0) × S⁽²⁾_TEGR (δ₁T = 0 for tensor
modes, so f_TT never enters); kinetic ratio −1.0 at the
legal sign; TEGR control f(T)=T gives the GR (illegal)
throat. Phase-3 throat values at |f_T|=1 (paper units):
ρ = 0.500, NEC1 = 0.500 in the phase's normalisation
(= 1.000 in the 4π normalisation used here and in
`gate5/wa_g5_1_ft.py`), NEC2 = 0.125.

## (1) Does the scalar enter S⁽²⁾_tensor's coefficient? No.

Two independent reasons, both checked in the script:

**(a) Structural (the deciding argument).** Minimal coupling
means the matter action is S_m[g(e), ψ]: it depends on the
tetrad only through the metric and contains **no derivatives
of the metric/tetrad**. Expanding in a tensor perturbation h,
every matter term is therefore *algebraic* in h. Matter can
produce h² terms proportional to the background stress-energy
(mass-like terms), but it cannot produce a single (∂h)² term.
The tensor kinetic and gradient coefficients come from the
gravitational sector alone. In the f(T) sector on a T≡0
background, δ₁T = 0 for TT modes (Gate-5's symbolic
expansion: T starts at O(λ²) with no linear term), so
S⁽²⁾_tensor[grav] = f_T(0) × S⁽²⁾_tensor[TEGR] and f_TT(0)
drops out via (δ₁T)² = 0. Total:

  S⁽²⁾_tensor = f_T(0) × S⁽²⁾_tensor,TEGR + (algebraic matter h² terms),
  kinetic ratio vs TEGR = **f_T(0) exactly**, c_T² = 1.

**(b) Explicit symbolic check for the scalar.** With
h_xx = −h_yy = ε(t,z) (TT), background scalar gradient
∂_xφ₀ = v and potential value V₀, sympy expansion of the
canonical scalar density −√(−g)[½ g^μν∂_μφ∂_νφ + V] to
O(h²) gives

  L_φ⁽²⁾ = V₀ ε²/2 + v² ε²/4,

with coefficient of ε̇² = **0** and of ε′² = **0** — purely
algebraic in ε, exactly as (a) requires. Additionally, by
spin decomposition on a spherically symmetric background,
δφ is a scalar-sector perturbation and cannot mix with TT
modes at quadratic order. The scalar shifts the background
the tensor modes live on; it does not touch their kinetic
coefficient. (The same algebraic-in-h check applies verbatim
to Maxwell/Yang–Mills: F_μν is metric-independent and
√(−g) g g F F contains no ∂g.)

Scalar stress-energy (derived in-script from
T_μν = ∂_μφ∂_νφ − g_μν[½(∂φ)² + V], static φ(r),
K ≡ ½ e^{−b}φ′² ≥ 0):

  ρ_φ = K − V,   p_r,φ = K + V,   p_t,φ = V − K,
  NEC1_φ = ρ_φ + p_r,φ = 2K ≥ 0,   NEC2_φ = 0,   SEC_φ = 2V ≥ 0,
  WEC iff K ≥ V. Full DEC (ρ ≥ |p_r|) requires V = 0; the
  spot checks use the V=0 member (ρ=K, p_r=K, p_t=−K: NEC1
  = 2K, NEC2 = 0, SEC = 0, DEC saturated) — itself fully
  EC-legal. Realisability at the throat: K(r₀) > 0 needs
  φ′ ~ √(2K)/s(r), s = √(1−r₀²/r²), and ∫_{r₀}^{2r₀} dr/s
  = **1.7297** (finite), so a finite-φ scalar carrying any
  prescribed throat density exists on the Ellis background.
  The scalar is real, legal, and can genuinely carry the
  load. It just cannot change the sign problem.

## (2) What the throat still forces

The BHL throat equations (Eqs. (22)/(23) at T=0, f(0)=0;
β′(r₀) = −1, flare-out β − rβ′ = 2r₀ > 0) fix the **total**
matter, whatever its composition:

  4πρ_tot(r₀) = β′(r₀)/(2r₀²) · f_T(0) = **−f_T(0)/2**,
  4π(ρ+p_r)_tot(r₀) = −(β − rβ′)/(2r₀³) · f_T(0) = **−f_T(0)**.

So the "flare-out deficit" is not a component that some
sector can supply separately: the field equations read the
sum. If f_T(0) > 0 (no ghost), the required total is
ρ_tot < 0 and NEC_tot < 0 — i.e. the geometry demands
exotic total matter, and every legal component added makes
the remainder *more* negative, not less. If f_T(0) < 0, the
required total is positive and legal splits exist at every
scalar fraction (below) — at the price of kinetic ratio
f_T(0) < 0, the tensor ghost. The sign of f_T is forced by
the throat read itself; no decomposition freedom exists.

## (3) Can total matter be EC-legal with f_T(0) > 0? No — proof

Assume f_T(0) > 0. Then by (2), ρ_tot(r₀) = −f_T(0)/(8π)
< 0 (equivalently −f_T(0)/2 in 4π units). But each
minimally coupled EC-legal component has ρ_i ≥ 0 and
(ρ+p_r)_i ≥ 0, so any sum has ρ_tot ≥ 0 and NEC1_tot ≥ 0.
Contradiction. ∎ The argument never uses the scalar's
detailed profile — only additivity of stress-energy and the
throat totals — which is why it covers every minimally
coupled addition at once. This is a failure of the
augmentation, not of any component: no component was found
EC-illegal; the scalar is legal throughout. (Checkpoint's
"exotic matter under a new name" clause does not trigger:
nothing exotic was smuggled in — the point is that legal
matter *cannot* do the job.)

## Numerical spot-check family (float64, 4π units, |f_T| = 1)

Required totals on the legal branch (f_T = −1): ρ_req =
0.500, NEC1_req = 1.000, NEC2_req = 0.125. V=0 scalar
carrying fraction s of ρ_req (NEC1_φ = 2ρ_φ carries the
same fraction s of NEC1_req; NEC2_φ = 0):

| s | ρ_φ | remainder required (ρ, NEC1, NEC2), f_T=−1 | kinetic ratio | remainder required (ρ, NEC1), f_T=+1 |
|---|------|------|------|------|
| 0.00 | 0.000 | (0.500, 1.000, 0.125) — all ≥ 0 | −1.0 (ghost) | (−0.500, −1.000) — illegal |
| 0.25 | 0.125 | (0.375, 0.750, 0.125) — all ≥ 0 | −1.0 (ghost) | (−0.625, −1.250) — illegal |
| 0.50 | 0.250 | (0.250, 0.500, 0.125) — all ≥ 0 | −1.0 (ghost) | (−0.750, −1.500) — illegal |
| 0.75 | 0.375 | (0.125, 0.250, 0.125) — all ≥ 0 | −1.0 (ghost) | (−0.875, −1.750) — illegal |

Reading: on the f_T < 0 branch a fully legal split exists
at every fraction — the scalar genuinely carries its share
— and the tensor kinetic ratio stays −1.0 in every row,
fraction-independent. On the f_T > 0 branch the totals
themselves are negative before any split is attempted, and
keeping the scalar legal only deepens the (illegal)
remainder. There is no row with total matter EC-legal and
f_T > 0. **AUGMENTED-PASS is unreachable within scope.**

## (4) Scope statement (verbatim-ready)

> On any T≡0-class f(T) wormhole background of the
> Böhmer–Harko–Lobo type (f(0)=0, flare-out β − rβ′ > 0 at
> the throat), for ANY matter sector coupled minimally —
> i.e. any matter action depending on the tetrad only
> through the metric, containing no derivatives of the
> metric/tetrad and no direct coupling to the torsion
> scalar, the torsion tensor, or curvature — including a
> canonical scalar field, Maxwell and Yang–Mills fields,
> perfect and anisotropic fluids, and a cosmological
> constant: (i) the tensor quadratic action's kinetic and
> gradient coefficients equal f_T(0) times their TEGR
> values, with matter contributing at most algebraic
> (non-kinetic) h² terms; and (ii) the throat field
> equations fix the TOTAL matter density and NEC
> combination to −f_T(0) times a positive flare-out factor.
> Hence total matter is EC-legal at the throat iff
> f_T(0) < 0 iff the tensor sector is a ghost. No minimally
> coupled addition, in any proportion, can separate the
> two signs.

**Reopening condition.** An addition that is NOT minimally
coupled in the above sense: one whose action contains
derivatives of the tetrad/metric or a direct coupling to
torsion/curvature — e.g. a scalar–torsion coupling φT or
an f(T,φ) sector, a φ𝔗 coupling (𝔗 = trace of the
stress-energy tensor; f(T,𝔗)-type theories), a non-minimal
ξφ²R or ξφ²T coupling, or derivative torsion couplings
(∂φ contracted with the torsion tensor). Such terms change
the *theory*, not the matter content: they can enter
S⁽²⁾_tensor's coefficient and shift the throat relations,
and are the named route by which this identity could break.
Also outside scope: backgrounds outside the T≡0 class
(there δ₁T ≠ 0 for tensor modes in general, and both
f_T(T_bg) and f_TT enter), and scalar/Lorentz-sector health
for a *specified* f, which needs f_TT(0) (the standing
P20-2 (F-b) follow-up, unchanged by this item).

## Follow-up experiment (per failure protocol)

The anatomy is structural (two sign-fixing totals + an
algebraic-in-h kinetic argument), so the one experiment
aimed at the mechanism is the reopening-condition test:
take the simplest non-minimal addition, f(T,φ) with a
φT coupling of strength ξ, on the same Ellis background,
and compute (i) whether S⁽²⁾_tensor's coefficient becomes
f_T(0) + (ξ-dependent term) and (ii) whether the throat
totals acquire a ξ-term that can flip their sign at
f_T > 0 — with the explicit label that this is a *different
theory*, so a pass there would not rescue P33-4, it would
price exactly what leaving minimal coupling costs.
