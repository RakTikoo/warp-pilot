# P21-2 — Nonlinear electrodynamics as matter (pure GR): memo

**Worker:** P21-2 worker agent. **Date:** 2026-11-21.
**Scripts:** `../p212_lib.py` (run record + symbolic derivations),
`../p212_derive.py` (identities), `../p212_scan.py` (numerical audits).
**Data:** `p212_identities.json`, `p212_results.json` (this directory).
Units r₀ = 1, float64 throughout. Domain r ∈ [r₀, 10³ r₀] as registered.

## VERDICT: **KILL (structural)**

Per the registered bars: NEC1 ≡ 0 for **every** L(F) **and** for the
G-dependent family F3 — the degeneracy is family-independent, with the
deciding identities written down below (I1, I2). No family gives
b′(r₀) < 1 strict; the forward-solved throat of any of these families is
forced to b′(r₀) = 1 exactly (marginal), and the marginal object is an
extremal throat at infinite proper distance with a log-divergent redshift
(F1 anatomy, §4). A second, independent structural wall (I3) shows the
registered bar "all four ECs legal **and** b′(r₀) < 1 strict" is
unreachable by *any* matter in a Morris–Thorne throat in GR: DEC in the
radial direction at r₀ is exactly equivalent to b′(r₀) ≥ 1.

**Premise correction (recorded plainly):** §P21-2 motivated F3 by the
expectation that G-dependence "breaks T^t_t = T^r_r". It does not — not
for the static spherical (dyonic) ansatz. The identity I1 holds for a
general L(F, G). The kill is therefore stronger than the registered
headwind: it covers the whole Plebanski class L(F, G) in spherical
symmetry, not only L(F).

## 1. Run record — exact forms and citations (recorded before any scan number)

Action as registered: S = ∫√−g [R/16π − L(F,G)/4π], F = F_μνF^μν,
G = F_μν ⋆F^μν, signature (−,+,+,+). Normalisation note: Maxwell limit is
L → F with L_F(0) = 1 in this action; energy densities are 4× the
textbook values at equal charge (q_textbook = 2 q_here). No EC sign,
identity, or verdict depends on this factor. Full record in the header
of `p212_lib.py`.

- **F1** Born–Infeld (F-only): L = 4b²(√(1 + F/(2b²)) − 1).
  Born & Infeld, Proc. Roy. Soc. A 144 (1934) 425; determinant form
  ℒ = (b²/4π)(√−g − √|det(g_μν + F_μν/b)|), with
  det(g + F/b) = −g(1 + F/(2b²) − G²/(16b⁴)).
- **F2** Bronnikov-class L(F): (F2a) L = F e^{−αF}; (F2b) L = F/(1+αF)².
  Bronnikov's regularity conditions (K. A. Bronnikov, gr-qc/0006014,
  PRD 63 (2001) 044005; review arXiv:2211.00743), recorded and tested:
  (R1) Maxwell weak-field limit L ∼ F, L_F → 1 as F → 0;
  (R2) with a Maxwell limit, a regular centre is possible only for
  magnetic charge (Bronnikov's theorem — the item's registered headwind);
  (R3) a globally regular magnetic configuration needs L(F) → finite
  limit as F → ∞; (R4) L > 0 and L_F > 0 for F > 0.
- **F3** Full Born–Infeld: L = 4b²(√Δ − 1),
  Δ = 1 + F/(2b²) − G²/(16b⁴); L_F = 1/√Δ, L_G = −G/(4b²√Δ)
  (both re-derived by SymPy differentiation of L, exact match).
  Maxwell limit L = F − F²/(8b²) + … (series verified). Δ factorises on
  the dyonic ansatz: Δ = (1 + B²/b²)(1 − ℰ²/b²), so Δ > 0 ⟺ ℰ < b
  (the BI field cap), verified symbolically.
- **F4** Control: L = F². No Maxwell limit (L_F(0) = 0).

Phase-3 precedent (§P3-2(2), EiBI/Shaikh): the same NEC1 ≡ 0 saturation
appeared there, but EiBI has a gravity-sector κ-term to relocate the
flare-out into. In pure GR there is no second sector; this item is the
control case showing the saturation is then fatal to strict flare-out.

## 2. The deciding identities (SymPy, from the action by direct variation)

Stress-energy derived from the action with a diagonal metric
(g^tt, g^rr, g^θθ, g^φφ as independent positive symbols), field
components F_tr, F_θφ only; orthonormal fields ℰ (electric), B (magnetic),
F = 2(B² − ℰ²), G = 4ℰB. Result (general L(F,G)):

  ρ  = [ −ℰ(B L_G − ℰ L_F) + L/4 ] / π
  p_r = −ρ  (identically)
  p_t = [ B(B L_F + ℰ L_G) − L/4 ] / π

**(I1) NEC1 ≡ 0 for every L(F,G), dyonic spherical ansatz.**
T^t_t − T^r_r = 0 exactly (SymPy: `I1_is_zero = True`, also with L_G = 0).
Mechanism, in one line: F depends on (g^tt, g^rr) only through the
product g^tt·g^rr (electric part) and g^θθ·g^φφ (magnetic part), while
G and √−g depend on the full product g^tt g^rr g^θθ g^φφ — so the
logarithmic derivatives of the action density w.r.t. g^tt and g^rr
coincide, and T^t_t = T^r_r. Equivalently: on the t–r block, both
F^μ_αF^α_ν and F^μ_α⋆F^α_ν are ∝ δ^μ_ν. Einstein's tt/rr equations then
force

  b′(r₀) = 1 + 8πr₀²(ρ + p_r)|_{r₀} = 1   for **every** L(F,G) solution.

The registered shapes demand b′(r₀) = −1 (b = r₀²/r) or 1/2
(b = r₀(r/r₀)^{1/2}) — neither is an Einstein–NLED solution, for any
family, any charges, any parameters. This is the deciding identity for
F1, F2, F3, F4 alike.

**(I2) NEC2 closed form.** ρ + p_t = L_F (ℰ² + B²)/π for general L(F,G)
(the L_G terms cancel); pure magnetic: ρ + p_t = F L_F/(2π). Hence
NEC2 ⟺ L_F ≥ 0 — Bronnikov's condition R4 *is* the NEC2 condition.

**(I4) Null-direction corollary** (linear algebra on the verified
diagonal form + I1 + I2): for any null k at angle χ to the radial
direction, T_μν k^μ k^ν = (ρ+p_r)cos²χ + (ρ+p_t)sin²χ
= [L_F(ℰ²+B²)/π] sin²χ ≥ 0 wherever L_F ≥ 0. In the healthy region
these theories satisfy NEC along **every** null direction, in every
frame — used in the rung-2a paragraphs (§6).

**(I3) Throat DEC identity (matter-independent).** For any Morris–Thorne
throat with regular Φ (Φ′ finite at r₀), the Einstein equations give,
identically,

  8πr₀² ρ(r₀) = b′(r₀),      8πr₀² p_r(r₀) = −1,

so DEC in the radial direction at the throat, ρ(r₀) ≥ |p_r(r₀)|, holds
**iff b′(r₀) ≥ 1**. Strict flare-out (b′(r₀) < 1) and full DEC legality
are mutually exclusive for *any* matter in GR — verified symbolically
for all four registered (Φ, b) combos (`I3_rho_matches_bprime` and
`I3_pr_is_minus_1` both True ×4). NLED saturates this bound exactly
(p_r = −ρ everywhere, DEC_r marginal), which is the same statement as
I1 read at the throat.

**Validation of the derivation:** Maxwell limit (L = F) reproduces
ρ = (ℰ²+B²)/(2π), p_r = −ρ, p_t = +ρ, trace T^μ_μ = 0 (all SymPy-exact);
the constitutive law from ∇_μ(L_F F^μν + L_G ⋆F^μν) = 0,
q_e = r²(L_F ℰ − L_G B), matches the closed BI inversion
𝒟 = ℰ√(1+B²/b²)/√(1−ℰ²/b²) to 4.4e-16 relative error numerically;
the Kretschmann evaluator used in §3 reproduces Schwarzschild
K = 48M²/r⁶ to 2.2e-16 relative error.

## 3. Prescribed-geometry audit (what GR would require)

Required (ρ, p_r, p_t) from the Einstein tensor of the four registered
combos (r₀ = 1; grid r ∈ [1, 10³], 4000 log points):

| combo | b′(r₀) | ρ(r₀) | NEC1_req(r₀) | min DEC_r margin | DEC_r legal out to | K finite (max) |
|---|---|---|---|---|---|---|
| b=r₀²/r, Φ=0 | −1 | −1/(8π) ≈ −0.0398 | −1/(4π) ≈ −0.0796 | −0.0796 | fails on whole domain | yes (12.0) |
| b=r₀²/r, Φ=−r₀/2r | −1 | −0.0398 | −0.0796 | −0.0796 | fails on whole domain | yes (13.0) |
| b=r₀√(r/r₀), Φ=0 | 1/2 | +1/(16π) ≈ +0.0199 | −1/(16π) ≈ −0.0199 | −0.0199 | fails on whole domain | yes (4.5) |
| b=r₀√(r/r₀), Φ=−r₀/2r | 1/2 | +0.0199 | −0.0199 | −0.0199 | fails on whole domain | yes (4.6) |

Anatomy: the b = r₀²/r shapes require ρ < 0 everywhere near the throat
(WEC-dead geometry for *any* matter, not just NLED). The √(r/r₀) shapes
have ρ > 0 but require NEC1 < 0 on the whole domain and violate DEC_r
on the whole domain (for Φ = 0 exactly: |p_r| = 2ρ at every r). The
geometries themselves are regular (Kretschmann finite everywhere) — the
obstruction is purely the matter matching, and by I1/I3 it is exact,
not numerical.

## 4. Per-family anatomy

**F1 — Born–Infeld (F-only), magnetic.** As *matter* it is impeccable:
12/12 parameter sets (b ∈ {0.5,1,2,5}, q_m ∈ {0.5,1,2}) have all four
ECs legal on the full trajectory F(r) = 2q_m²/r⁴ (margins ≥ 0; the
minima ~1e-13 are the r → 10³r₀ tails → 0⁺). L_F = 1/√(1+F/2b²) ∈
[0.243, 1] — finite, positive (R4 ✓); R1 ✓; F(r) strictly decreasing ⇒
L single-valued along r ✓ (no branch switching). R3 fails
(L ∼ √(2b²F) → ∞ as F → ∞) — but R3 is Bronnikov's regular-*centre*
condition; on the throat domain F is bounded and this does not bind.
The family dies *only* on I1: b′(r₀) = 1 forced. Forward anatomy of
that forced marginal throat (b_BI = 1, q_m = √(17/64) ≈ 0.5154 chosen
so 2r₀²L(F(r₀)) = 1 exactly): r − b(r) ≈ C(r−r₀)² with C = 0.871 > 0,
so the proper distance to the throat diverges logarithmically —
partial integrals grow 2.42 per decade of approach vs the predicted
ln10/√C = 2.467 — and the redshift diverges too: N′(r₀) = 1.78 ≠ 0
gives Φ′ ≈ N′(r₀)/(2C(r−r₀)) (Φ′(r₀+0.01) ≈ 99 measured), i.e. Φ is
log-divergent at the throat. The unique NLED "throat" is an extremal,
null, infinitely distant, infinitely redshifted surface — the
wormhole analogue of an extremal horizon — not a traversable throat.

**F2a — L = F e^{−αF}.** R1 ✓, R3 ✓ (L → 0). EC-legal as matter iff the
trajectory stays at αF ≲ 1/2: SEC binds first (SEC combo
= (2FL_F − L)/2π ∝ (1 − 2αF)); NEC2 and DEC_t bind at αF = 1, exactly
where L_F = e^{−αF}(1−αF) changes sign (R4). At αF(r₀) = 0.4
(α=0.2, q_m=1): fully legal. At αF(r₀) = 8 (α=1, q_m=2): L_F,min =
−0.135, NEC2_min = −0.0492, SEC_min = −0.132, DEC_t fails — every
failure sits inside the L_F < 0 corner, as I2 says it must. 6/9 sets
legal. Throat: killed by I1 regardless of parameters.

**F2b — L = F/(1+αF)².** R1 ✓, R3 ✓ (L → 0). SEC binds earliest of all
families: legal iff αF ≤ 1/3 on the trajectory; already at αF(r₀) = 0.4
(α=0.2, q_m=1) SEC_min = −0.0232 with p_t(r₀) < 0. L_F sign change at
αF = 1 as in F2a. 3/9 sets legal. Throat: killed by I1.

**F3 — Full Born–Infeld, dyonic.** The registered hope — G-dependence
breaking the degeneracy — is refuted by I1: NEC1 ≡ 0 symbolically for
the BI partials as for general L(F,G). As matter, dyonic BI is again
fully legal: 12/12 sets (q_m ∈ {0.5,1,2}, q_e ∈ {0.5,1}, b ∈ {1,2})
pass all four ECs on the trajectory (constitutive inversion
ℰ² = 𝒟²/(1 + B²/b² + 𝒟²/b²), 𝒟 = q_e/r²); L_F = 1/√Δ ∈ [0.49, 1],
Δ ≥ 1 on the domain, ℰ/b ≤ 0.408 (cap respected), F and G finite,
L(F,G) a fixed single-valued function (no reconstruction, no branch).
Reconstruction against the best prescribed geometry (b = r₀√(r/r₀),
Φ = −r₀/2r) quantifies the overdetermination: at the throat no ℰ
solves even the ρ equation for the sampled charges (min over ℰ of
ρ_BI(r₀) = 0.150 vs required 0.0199 at q_m=1, b=2; 0.0376 vs 0.0199 at
q_m=0.5, b=1 — parameter-dependent anatomy, not the deciding clause);
on the 80–93% of radii where a ρ-match exists, the p_r residual is
exactly |NEC1_req| in structure (p_r^BI = −ρ identically vs required
ρ + p_r < 0), and the would-be conserved charge q_e(r) = r²(L_Fℰ −
L_GB) drifts by factors of 1667× and 4348× across the domain — the
Maxwell/constitutive equation cannot hold along the trajectory. The
deciding clause remains I1: required NEC1(r₀) = −1/(16π) vs supplied
0, identically, for all (q_e, q_m, b).

**F4 — Control L = F².** Behaves as registered-expected, validating
the audit: NEC2, SEC pass, but DEC_t fails on the whole domain
(min margin −2/π ≈ −0.6366 at q_m=1, since p_t = 3ρ), and L_F(0) = 0
— no Maxwell limit (R1 ✗). 0/3 sets legal. Throat: killed by I1 as
well, independently of its DEC failure.

## 5. Why the registered LEGAL THROAT bar is unreachable (summary)

Two independent identities, either sufficient:
(i) I1 forces b′(r₀) = 1 for every L(F,G) in spherical symmetry —
strict flare-out would need a stress-energy no member of the class
possesses; (ii) I3 forces DEC_r at r₀ to fail for *any* matter
whenever b′(r₀) < 1. The bar set (strict flare-out ∧ all four ECs ∧
regularity) is empty in pure GR for this matter class — and clause
(ii) of the bar is empty for all matter whatsoever.

## 6. Rung-2a (FTL) paragraph per family — wall supply at β = 0.1, 1.1, 1.5

Registered secondary triggers only for a throat survivor; there is
none, so no wall scan was run. Per the steering amendment, the
structural reason is recorded per family, and it is stronger than
"not triggered": the shared bed's binding sets are NEC-*deficit* sets
(β=0.1: 251 pts, max deficit 1.981e-4; β=1.1: 504 pts, 2.825e-3;
β=1.5: 594 pts, 3.387e-3), and by I4 these families' supply against
any NEC deficit is **identically zero at every β**, because
T_μνk^μk^ν ≥ 0 for every null k wherever the matter is healthy.

- **F1:** T(k,k) = [F L_F/(2π)] sin²χ ≥ 0 with L_F ∈ (0,1] on every
  trajectory. Supply = 0 vs deficits up to 3.387e-3 at β=1.5. No
  moving-wall configuration of this family can cover a single binding
  point; the obstruction is the same identity as at the throat.
- **F2a/F2b:** Identical where L_F > 0. The only NEC-violating region
  is L_F < 0 (αF > 1) — exactly Bronnikov's R4-violating corner, where
  the static-frame NEC2, SEC and DEC_t already fail (measured in §4):
  ghost-corner matter, not a legal supply at any β.
- **F3:** I4 with NEC2 = L_F(ℰ²+B²)/π, L_F = 1/√Δ ∈ (0,1]: T(k,k) ≥ 0
  for all null k on all 12 audited dyonic trajectories. A
  boost-stationary, non-spherical field ansatz on the wall bed is not
  defined by the published spherical families, and I1's mechanism
  (t–r block degeneracy of a radial 2-form) is a statement about the
  field's algebraic structure, not about β. No superluminal supply.
- **F4:** Control; NEC-saturating (I1) and DEC-illegal as matter.
  Nothing to supply.

## 7. Failure Protocol — anatomy and follow-ups

Anatomy in one line: spherical NLED matter has a boost-degenerate
t–r stress block (p_r = −ρ identically), so it can at best saturate
flare-out; and GR's throat identities make saturation the exact
boundary of DEC legality. The failure is structural (two exact
identities), not parametric: no (α, b, q_e, q_m) scan can move it,
because I1/I2/I3 contain no family parameters.

Named follow-ups (mechanism-suggested, for the coordinator to
register or not):
- **FU-P212-1 (break the block, stay electromagnetic):** I1 rests on
  F having only (tr, θφ) components. A field configuration with
  components outside the radial blocks — e.g. a Melvin-type flux tube
  or a non-spherical stationary field — is outside I1's proof. Test:
  does any stationary non-spherical NLED configuration give
  T^t_t ≠ T^r_r in its rest frame while keeping L_F > 0? This is the
  only in-class door the identity leaves open.
- **FU-P212-2 (leave the class):** non-Abelian (Yang–Mills) or
  multi-field matter, whose stress block is not a single 2-form's —
  the natural next matter class if the programme wants a
  T^t_t ≠ T^r_r source with healthy ECs elsewhere.
- **Reopening condition for P21-2 itself:** a published L(F,G)-class
  (Plebanski) model with a *spherical* ansatz and T^t_t ≠ T^r_r would
  contradict I1's derivation and would reopen this item immediately;
  short of that, the item is closed on structural evidence.

**Deliverables:** `../p212_lib.py`, `../p212_derive.py`,
`../p212_scan.py`, `p212_identities.json`, `p212_results.json`,
this memo. Internal only; nothing uploaded; no external contact
beyond the two literature searches used for the run record.
