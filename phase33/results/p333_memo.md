# P33-3 — EiBI TWO-FLUID — Memo

Worker P33-3. Script: `phase33/p333_eibi_twofluid.py`; results:
`phase33/results/p333_results.json`. float64 throughout. Units
8π = G = c = 1 (Shaikh), κ = −1. Conditional observational caveat
|κ| ≲ 10⁸ m² carried in every statement below, as in Phases 3/20/23.

## Baseline

P20-2: the Shaikh et al. (arXiv:1807.07941) anisotropic-fluid EiBI
throat closes as a background and its matter passes all ECs, but its
tangential sound speed c_t² = dp_t/dρ = 1 + 2κρ = **−1 at the throat,
forced for every member**, because the throat condition itself is
κρ(r₀) = −1 (equivalently ω_θ(r₀) = 1 + κρ(r₀) = 0, the theory's own
throat definition; Gate-5 G5-2). Question: is that −1 a property of
any EiBI throat mixture, or only of the one-fluid ansatz?

## Gate (single-fluid limit) — PASSED

Setting the mixture fraction f = 0 in the construction below
reproduces P20-2's background closure exactly:

- Phase-3 normalisation row (C₀ = 2, r₀ = 1): ρ(r₀) = 1, p_t(r₀) = 0,
  NCC(r₀) = −2.0 — bit-level match (≤ 1e-12) against the stored
  `phase3/results/p32_modgrav.json` values.
- P20-2 genuine member (C₀ = 1/2, r₀ = 0.70711, x = r₀²/|κ| = 0.5):
  κρ(r₀) = −1 (the throat condition on the total), c_t²(r₀) = −1
  matching the stored `phase20/results/p202a_eibi.json`, c_t² zero at
  r = (0.75)^{1/4} as in P20-2, conservation (Eq.21) residual ≤ 8.9e-16,
  all ECs pass.

## Construction

Totals only enter the EiBI equations. Fluid 1 is the Shaikh-type
anisotropic fluid with its EoS in its **own** density (the autonomous,
microphysical reading): p_r1 = −ρ₁, p_t1 = ρ₁(1 + κρ₁). Fluid 2 is
isotropic, p₂ = wρ₂, w ∈ [0,1]. The fluids are comoving and separately
conserved:

- Fluid 1's conservation is redshift-free (ρ₁ + p_r1 = 0 kills the Φ′
  term), so it integrates to Shaikh's own family with its own
  constant: ρ₁ = (C₁/r⁴)/(1 − κC₁/(2r⁴)).
- Fluid 2's profile is taken in the same rational family (constant
  C₂); its conservation then **solves** the redshift,
  Φ′ = −wρ₂′/((1+w)ρ₂), finite on the whole domain (Φ′(r₀) ≤ 2.48 on
  the grid; tail Φ′ ~ 4w/((1+w)r), verified numerically). Total
  conservation with this Φ′ holds identically (residual ≤ 1.3e-15) —
  its numerator reduces analytically to wρ₂′ given fluid 1's
  conservation.
- Throat condition imposed on **totals** (registered gate):
  κρ_tot(r₀) = −1, with throat mixture fraction
  f := ρ₂(r₀)/ρ_tot(r₀), so ρ₁(r₀) = (1−f)/|κ|, ρ₂(r₀) = f/|κ|.
  Genuine-wormhole regime throughout: x = r₀²/|κ| = 0.5 < 1, κ < 0.
- Grid: f ∈ {0, 0.25, 0.4, 0.5, 0.6, 0.75, 0.9, 1} × w ∈ {0, 1/3, 1/2, 1},
  domain [r₀, 10³ r₀].

**Closure scope (stated precisely):** closure is certified at the
P20-2 gate standard — profiles, per-fluid and total conservation,
throat algebra on totals, Ω eigenvalues positive for all r > r₀. The
q-Einstein metric reconstruction (b(r), Φ(r) from the field
equations) is **not** performed — exactly as P20-2 did not
reconstruct Shaikh's f(r) — with one asymmetry honestly noted: for
the single fluid, Shaikh's paper supplies existence; for the mixture
no published existence result exists, and the 1/r⁴ tail of a
separately conserved isotropic component forces a logarithmically
growing Φ. The metric reconstruction with an asymptotically flat
tail choice is the follow-up experiment (below). No EC or mode read
below depends on it: all are local in the profiles.

## Total EC audit

For **every** grid row (all f, all w): totals pass NEC/WEC/SEC/DEC on
the full domain [r₀, 10³ r₀], and so does **each fluid by itself**.
Analytically: NEC_r^tot = (1+w)ρ₂ ≥ 0; NEC_t^tot = ρ₁(2+κρ₁) +
(1+w)ρ₂ ≥ 0 (since ρ₁ ≤ 1/|κ| everywhere, ρ₁ being maximal at the
throat); ρ_tot − p_t,tot = ρ₁²·|κ|⁰ + (1−w)ρ₂ ≥ 0 (DEC_t);
SEC^tot = 2ρ₁(1−|κ|ρ₁)·… + ρ₂(1+3w) ≥ 0. No component is EC-illegal
anywhere; there is no exotic matter under a new name in any row.

## Mode analysis — the core question

**Framework (explicit):** comoving two-fluid system, adiabatic
perturbations (each fluid perturbed along its own barotropic EoS),
**matter sector on the closed background**. The EiBI gravitational
coupling through the auxiliary metric q is **not** included, and
cannot be posed at the throat: with general totals
ω_θ = √[(1+κρ_tot)(1−κp_r,tot)], so det Ω(r₀) = 0 for **every**
mixture — it depends only on the total density through the throat
condition 1 + κρ_tot(r₀) = 0 — and off the one-fluid ansatz ω_t
additionally has a pole at the throat (ω_t ≈ 10² at the first grid
point above r₀, diverging as r → r₀⁺). This is P20-2's obstruction,
unchanged; it is a property of the **mixture**, indeed of any EiBI
throat. Two velocity readings are computed, and the bar is applied
across both:

1. **Per-fluid adiabatic speeds** (independent-velocity reading —
   the standard multi-fluid matter sector, fluids coupled only
   gravitationally): fluid 2: c₂² = w ∈ [0,1] in both directions.
   Fluid 1 tangential: **c₁ₜ² = dp_t1/dρ₁ = 1 + 2κρ₁**. Fluid 1
   radial: **no acoustic mode exists** — its radial enthalpy
   ρ₁ + p_r1 vanishes identically, so the formal derivative
   dp_r1/dρ₁ = −1 multiplies zero inertia and is not a propagating
   speed (the same degeneracy that left P20-2's single-fluid radial
   sector with no acoustic read).
2. **Locked-velocity (strictly comoving) reading:** one acoustic
   mode per direction, the enthalpy-weighted average
   c_mix² = Σᵢ cᵢ²(ρᵢ+pᵢ)/Σᵢ(ρᵢ+pᵢ), plus a non-propagating
   composition (entropy) mode with speed² = 0 ∈ [0,1]. Tangential:
   a convex combination of c₁ₜ² and w (weights ρ₁(2+κρ₁) > 0 and
   (1+w)ρ₂ ≥ 0), hence in [0,1] wherever c₁ₜ² is. Radial: fluid 1
   drops out identically (zero radial enthalpy), c_mix,r² = w.

**The deciding formula.** At the throat the throat condition fixes
only the TOTAL: κρ_tot(r₀) = −1. Fluid 1's tangential speed there is

  c₁ₜ²(r₀) = 1 + 2κρ₁(r₀) = **2f − 1**,

which is −1 only at f = 0. Since ρ₁ decreases outward, c₁ₜ²(r) ≥
c₁ₜ²(r₀) everywhere, so all speeds in both readings lie in [0,1] on
the whole domain **iff f ≥ 1/2** — fluid 2 carries at least half the
throat density. Numerics confirm the formula to machine precision on
every row (e.g. f = 0.6: c₁ₜ²(r₀) = +0.20, coupled tangential speed
at the throat 0.103–0.722 across w, domain range inside [0,1];
f = 0.5 is the marginal boundary, c₁ₜ²(r₀) = 0 exactly, positive for
r > r₀). For f < 1/2 the deciding mode is fluid 1's tangential
acoustic mode, c₁ₜ²(r₀) = 2f − 1 < 0, negative out to
r* = (3C₁/2)^{1/4}; note the locked-velocity coupled mode can stay
positive there (f = 0.25, w = 1: +0.022) — the rows fail on the
per-fluid mode, which is a physical mode in the independent-velocity
reading, and the bar counts every computed physical sound speed.

**What dp_t/dρ does and does not mean for a mixture.** The single
background derivative dp_t,tot/dρ_tot along a solution profile is
[p_t1′ + wρ₂′]/[ρ₁′ + ρ₂′] — the per-fluid EoS derivatives weighted
by the **background slopes** ρᵢ′(r). It is a sound speed only if
perturbations are constrained to slide along the background family
(δρ₂/δρ₁ = ρ₂′/ρ₁′ fixed), which physical perturbations are not:
δρ₁ and δρ₂ are independent, and the true mode weights are the
**enthalpies** ρᵢ + pᵢ, not the slopes. In the one-fluid case the
two notions coincide trivially — which is why P20-2's read was a
genuine sound speed there, and why exporting it to a mixture would
be a category error. The numbers show the difference is real, not
pedantic: at f = 0.4, w = 1/3 the background derivative at the
throat is **+0.031** (looks healthy) while fluid 1's actual
tangential mode is at **−0.20** (gradient-unstable); at f = 0.25,
w = 1 it is −0.023 while the locked coupled mode is +0.022. Neither
sign read from the background derivative is a mode of the system.

(Alternative EoS reading noted and set aside: defining fluid 1's EoS
through the total density, p_t1 = ρ₁(1 + κρ_tot), makes δp_t1
respond to δρ₂ — an interacting, non-autonomous "fluid" for which a
per-fluid sound speed is not defined. The own-density reading above
is the microphysically clean one and is what was computed.)

## Verdict (fixed language)

**AUGMENTED-PASS** — for the 16 rows with throat mixture fraction
**f ≥ 1/2** (all w ∈ {0, 1/3, 1/2, 1}): background closes at the
P20-2 gate standard with the throat condition on totals
κρ_tot(r₀) = −1, total ECs pass on the full domain [r₀, 10³ r₀],
each component is EC-legal by itself on the whole domain, and every
computed physical sound speed — per-fluid and coupled, tangential
and radial, both velocity readings — at and near the throat and on
the whole domain lies in [0,1], in the genuine-wormhole regime
κ < 0, x = r₀²/|κ| = 0.5 (conditional caveat |κ| ≲ 10⁸ m²).

**AUGMENTED-FAIL** for the 12 rows with f < 1/2 (including the
f = 0 single-fluid baseline rows, which reproduce P20-2's failure):
deciding mode = **fluid 1's tangential acoustic mode**,
c₁ₜ²(r₀) = 2f − 1 < 0 (at f = 0: exactly −1, the P20-2 result).
The f = 1 rows are the degenerate boundary (fluid 1 absent) and are
not counted as an augmentation.

**Answer to the core question:** the forced c_t² = −1 is a property
of the **one-fluid ansatz**, not of the mixture. The throat
condition constrains only the total density; a second ordinary,
itself-EC-legal fluid carrying at least half the throat density
moves fluid 1's tangential mode to 2f − 1 ∈ [0,1] and every other
computed mode follows. What **is** a mixture property is the
auxiliary degeneracy det Ω(r₀) = 0 (with an ω_t pole off-ansatz):
the full EiBI gravitational perturbation problem through q remains
NOT COMPUTABLE at the throat, exactly as in P20-2 — the PASS is a
matter-sector verdict, at the scope the item registered.

**Deciding term:** c₁ₜ²(r₀) = 1 + 2κρ₁(r₀) = 2f − 1.

## Follow-up experiment (Failure Protocol)

1. **Metric reconstruction:** solve the q-Einstein system for the
   mixture (b(r), Φ(r)) with an asymptotically flat fluid-2 tail
   (the separately conserved 1/r⁴ tail forces Φ ~ [4w/(1+w)] ln r);
   verify flare-out b′(r₀) < 1 and no horizons off the profile
   level. This promotes closure from the P20-2 gate standard to a
   full solution.
2. **q-frame perturbation door (P20-2 F-a, unchanged):** a
   formulation that poses throat boundary conditions without
   dividing by det Ω is still required before any gravitational
   sector of any EiBI throat — one-fluid or mixture — can be
   certified; the mixture does not move this obstruction.
