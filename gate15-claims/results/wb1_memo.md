# W-B1 (ENGINE + SETTLEMENT) — Gate-15 memo

INTERNAL only. C12 accounting. Formation PRE-EXISTING ONLY. (V-b) UNDECIDED:
Pais–Uhlenbeck spin-2 ghost vs Mannheim PT-symmetric quantisation — opposed
literature positions, B3 NOT COMPUTABLE (Phase 32) — carried, not decided.

All code is W-B1's own, written from scratch in `gate15/work_b/`
(`wb1_engine.py`, `wb1_validate.py`, `wb1_gauge.py`, `wb1_settle.py`,
`wb1_msave.py`, `wb1_basis2.py`, `wb1_basis3.py`, `wb1_kappa.py`,
`wb1_propagate.py`, `wb1_assemble.py`). No phase code was imported, copied or
run; phase records were read only for the registered formulation and stored
control data. float64; 40-digit mpmath for the κ anchor solve.

## Headline result

The anchors all pass (background Bach ≡ 0, ℓ = 0 dimension exactly 7,
κ anchors reproduced), so the machinery is sound. The settled homogeneous
dimensions are

| mode | W-B1 settled | Phase 122 claimed |
|---|---|---|
| ℓ=0 | **7** | 7 ✓ |
| ℓ=1 | **10** (solution space; 4 pure gauge + 6 (e) quotient) | 9, all (e) ✗ |
| ℓ=2 | **8**, all (e) | 7 ✗ |
| ℓ=3 | **8**, all (e) | 7 ✗ |

The +1 discrepancy at every ℓ ≥ 1 is the result, reported at face value with
anatomy below (§3–§4). Phase 91's own first ℓ = 0 count was also cut one low
by extra constraints and corrected on prolongation — the same failure species
is consistent with what is seen here, stated as pattern, not proof.

## 1. Engine (own derivation)

`wb1_engine.py` implements the Bach tensor as an algebraic function of the
metric's partial-derivative jets at a point, via a multivariate Taylor-jet
algebra in (r, θ) to order 4 that I wrote for this Gate. Each jet coefficient
carries a value channel plus one exact-linearisation channel per perturbation
unknown (dual-number style — no finite differencing anywhere in the
settlement chain). Chain, all from the metric definitions:

metric (order 4) → Christoffel (3) → Riemann (2, sign
R^k_{lmn} = ∂_mΓ^k_{ln} − ∂_nΓ^k_{lm} + ΓΓ − ΓΓ) → Ricci R_{ln} = R^k_{lkn},
Schouten, Weyl C = R − (g⊙P) (2) → contracted first Weyl derivative
S_{μνσ} = ∇^ρC_{μρνσ} (1) → its covariant derivative (0) →
**B = 2∇∇C + R·C** in the registered convention (Gate-9 erratum 3).

The engine handles a general static axisymmetric diagonal metric with
g_rθ = 0 and produces all components including B^r_θ. Perturbations enter as
scaled Taylor coefficients U(r) = Σ u_k((r−r_c)/r_c)^k (likewise V, Θ), K = 8;
angular jets come from lambdified dⁿP_ℓ(cos θ)/dθⁿ.

### Validation (wb1_validation.json; all PASS)

- **Background floor.** max |B^μ_ν| on the MK background over 7 (r, θ)
  points = **1.95×10⁻¹⁸** (worst at r = 11; ~6×10⁻²⁴ at Σ). Flat control
  4.84×10⁻¹⁸, Schwarzschild control 2.35×10⁻¹⁸. Since MK is not Ricci-flat,
  this also confirms the R·C sign in the registered convention.
- **MK tangents.** Linearised |B| per unit parameter ≤ 6.8×10⁻¹⁹
  (δβ 6.3×10⁻²⁰, δγ 1.7×10⁻²⁵, δk 6.8×10⁻¹⁹): the (δβ, δγ, δk) tangents
  satisfy the linearised system identically.
- **Linearisation channels** vs finite-amplitude Richardson: relative
  difference ≤ 6.0×10⁻¹¹.
- **Mode decoupling** (pure ℓ=2 profile): cross-mode relative coefficients
  ≤ 2.7×10⁻¹⁴. Correct projected components: B^t_t, B^r_r,
  B^θ_θ+B^φ_φ (all ∝ P_ℓ), B^θ_θ−B^φ_φ (∝ E_ℓ := P_ℓ″ − cotθ·P_ℓ′, the
  tracefree angular harmonic, identically 0 for ℓ < 2), B^r_θ (∝ ∂_θP_ℓ).
  Settlement uses these 5 (ℓ=0: first three; ℓ=1: + rθ).
- **Gauge formulas** (wb1_gauge.py, sympy, ℓ=2, generic X(r), Y(r)): the
  registered Lie action dU = f′X; dV = X(1/f)′ + 2X′/f; dW = r²Y′ + X/f;
  dΘ = 2X/r − ℓ(ℓ+1)Y; dG = 2Y is verified from scratch — all five residuals
  simplify to exactly 0.

Two engine bugs were found and fixed during validation (recorded per the
failure protocol): a Christoffel contraction with the wrong contracted axis
(flat-space Bach ~2×10⁻² before the fix), and a radial-jet scaling error
(Taylor coefficient divided by centre^k instead of centre^i — invisible at
the centre point, corrupting offset stations). Post-fix, a δβ tangent's
Taylor series gives linearised Bach ≤ 6.6×10⁻²¹ at r = 980/1000/1020 vs
3.1×10⁻¹² for a random control.

## 2. Settlement method

Per mode ℓ ∈ {0,1,2,3} and centre r₀ ∈ {11, 1000}: unknowns = scaled Taylor
coefficients k = 0..8 of (U_ℓ, V_ℓ, Θ_ℓ) at r₀ (Θ₀ excluded, areal gauge).
Prolonged rows by two independent routes: Route 1 — linearised Bach at
r₀ + mδ (m = −4..4, δ = 0.01·r₀, 4 thetas), projected per component, Taylor
coefficients in m to order P ∈ {3,4,5}; Route 2 — collocation at 9 radii
r₀(1 + 0.013(m + 0.31)). Rows equilibrated; dimension = rank of the nullspace
projection onto the initial-data (ID) jet space (u₀..u₃, v₀..v₃, w₀..w₃),
fixed relative cut 10⁻⁸, with K ∈ {7,8} subselection reads. ID singular
values (primary reads) are tabulated in `wb1_results.json`; the decisive
gaps are:

- ℓ=0: 7th ID sval ≥ 4.2×10⁻³, 8th ≤ 7.3×10⁻¹⁰ at every read, both radii,
  both routes. **Settled 7** — anchor bar passed.
- ℓ=1: 10th ≥ 4.5×10⁻³ (P4/P5/K7/route-2, both radii), 11th ≤ 7.4×10⁻⁹ in
  all primary reads except one marginal P5-at-Σ read (11th at 1.3×10⁻⁸,
  fit-noise level). **Settled 10.**
- ℓ=2: 8th ≥ 7.4×10⁻⁴ at Σ (P4/P5), 4.0×10⁻² at r = 11 (P4); 9th ≤ 2.3×10⁻⁹
  at P4/P5. The 8th direction weakens in the highest-order r = 11 fits
  (1.9×10⁻⁷ at P5, 1.0×10⁻⁷ at P4/K7) but stays ~4 orders above the next
  singular value. **Settled 8.**
- ℓ=3: 8th ≥ 2.6×10⁻⁴, 9th ≤ 4.8×10⁻¹¹ at P4/P5, both radii.
  **Settled 8.**

Cross-centre genuineness test: the Σ basis re-expanded about r = 900 lies in
the r = 900 system's ID span (d = 10/8/8 there too) with ID distances ≤ 10⁻⁶
(ℓ=1), ≤ 7×10⁻³ (ℓ=2), ≤ 1.1×10⁻² (ℓ=3); pending artefacts would show
O(0.1–1). The weakest directions are the last ones at ℓ=2,3 — reported
honestly; they are nonetheless inside the span at both centres.

Cut anatomy: the least-squares Taylor-fit rows carry fit noise ~10⁻⁸ in
row-equilibrated singular values, so a fixed 10⁻⁸ cut on the full system is
fragile; the ID-projection rank is the robust read and is stable across
P ∈ {3,4,5}, K ∈ {7,8}, both radii and both routes at the settled values
above (full cut-sensitivity table in `wb1_results.json`).

## 3. The ℓ=2, r=11 confrontation (explicit)

Phase 122 recorded a Richardson bracket 7–8 at r = 11, the 8th direction at
ID strength 1.1×10⁻⁵, absent at Σ above 5.5×10⁻¹⁵, and settled 7.

W-B1 reproduces the *phenomenon* — a weak extra direction visible only in
low-order r = 11 reads and absent at Σ — but one level up. In my system the
low-order reads (P3, route 2) show a **ninth** direction at ID strength
2.6×10⁻⁶ (P3, r = 11), 3.8×10⁻⁶ (P3, Σ), 3.8×10⁻⁸ (route 2, r = 11),
1.0×10⁻⁸ (route 2, Σ), which dies under prolongation (P4: ≤ 2.3×10⁻⁹ at
r = 11, ≤ 1.7×10⁻¹⁰ at Σ). The **eighth** direction, by contrast, survives
every prolongation at both radii (≥ 7.4×10⁻⁴ at Σ; §2). My bracket is
therefore 8–9 where Phase 122's was 7–8, and my settled ℓ=2 dimension is
**8**, one above their 7. The same weak-ninth species appears at ℓ=3
(2.0×10⁻⁶ at P3/r = 11, dying at P4). I did not inspect Phase 122's code
(per Gate rules); the statement is about the spectra, not their machinery.

## 4. Classification

**ℓ=0 (settled 7).** Named vectors identified inside the settled span by
ID-space distance: δβ 7.0×10⁻¹², δk 1.4×10⁻¹⁵, constant rescaling
4.4×10⁻¹⁴, δγ 2.4×10⁻³ (weakest identification; δγ's jet has the largest
dynamic range — fit-level, flagged). All four also satisfy M·v ≈ 0 directly
(|Mv|∞/|v|∞ ≤ 9×10⁻¹⁴). Classification: 3 MK tangents (b) + constant
rescaling (a, pure gauge, verified by metric form) + **3 (e)**.

**ℓ=1 (settled 10) — the gauge-completeness argument has a hole at ℓ=1.**
The registered argument (preserving W = G = 0 forces X = Y = 0) treats
dG = 2Y as a metric condition. But G multiplies the tracefree angular
harmonic E_ℓ = P_ℓ″ − cotθ·P_ℓ′ + P_ℓ·(angular factor), and **E₁ ≡ 0**:
at ℓ=1 the G-component is metrically vacuous. The gauge family with
Y = xʲ (j = 0..3), X = −fr²Y′ (killing W) is therefore a genuine
perturbation of the (U, V, Θ) ansatz. Verified directly: pointwise
linearised Bach ≤ 8.4×10⁻²⁴ at Σ, ≤ 6.1×10⁻¹⁸ at r = 980 (random control
2.7×10⁻¹⁰), and all four gauge ID jets lie in the settled 10-dim span
(distances ≤ 2.3×10⁻⁹). So the ℓ=1 solution space contains a **4-dim
pure-gauge subspace (class (a))**, leaving an **(e) quotient of 6**.
Phase 122's "9, all (e)" matches neither the space (10) nor the quotient
(6). The basis file splits the ℓ=1 basis accordingly (4 gauge elements
labelled class (a); 6 quotient elements labelled (e)).

**ℓ=2, ℓ=3 (settled 8 each, all (e)).** Here E_ℓ ≠ 0 and the completeness
argument holds: symbolically (§1) and by numeric negative control — the
ℓ=2 gauge triples (without their G part) sit 0.29–0.73 away from the
nullspace, i.e. they are not solutions in the ansatz. The +1 over Phase 122
at ℓ=2,3 is therefore a genuine non-gauge solution direction their system
missed, not gauge leakage.

**Class (c) vs (e) — propagation spot check** (registered test): one basis
element per mode realised as a polynomial profile about Σ has projected
linearised-Bach residual at Σ−20/Σ/Σ+20 of 7.8×10⁻²⁴/… (ℓ=1),
1.8×10⁻²² (ℓ=2), 9.4×10⁻²² (ℓ=3), 3.7×10⁻²¹ (ℓ=0 (e)) vs random controls
8.8×10⁻¹⁰, 1.9×10⁻⁹, 2.3×10⁻⁹, 4.0×10⁻¹² — 8 to 13 orders below control.
No basis element is singular at Σ or fails to propagate: all are class (e)
(subject to the ℓ=1 gauge split above). **Class (d) has no local diagnosis
under the registered scheme** — stated limitation, as in Phase 91/122.

## 5. κ anchor (own solve from stored data, 40-digit mpmath)

Using Phase 91's stored jumps and stored response data (read as data only):

- κ_full recomputed = **−2.76430892×10⁻⁵** vs stored −2.76430632×10⁻⁵:
  relative difference **9.4×10⁻⁷** (bar: 5%) ✓. Restricted amplitudes
  δβ = −6.93053×10⁻³/ε (stored −6.93053×10⁻³), δk = 1.037×10⁻¹¹.
- Enlarged solve with my own three ℓ=0 (e) basis responses under the stored
  channel functionals: response rank **3**; exact 3×3 solve (β, k, e₀)
  residual [−8.5×10⁻²², 0, 0], so **κ_enlarged = 0** ✓, with amplitudes
  δβ = −3.395×10⁻³/ε (stored class −3.9×10⁻³/ε), δk = 1.291×10⁻¹¹,
  e₀ = 2.24×10⁻⁵. Each of the three (e) directions individually completes
  the solve with residual ≤ 1.3×10⁻²¹ and δβ in the −3.1…−6.0×10⁻³/ε range.

## 6. Deliverables and the W-B2 hand-off

- `wb1_basis_jets.json`: per mode, the settled basis elements' Taylor
  coefficients (k = 0..8 about Σ) and jets (U, U′, U″, U‴, V, V′, V″, Θ, Θ′)
  at r = 1000. Normalisation (stated in the file): nullspace from the
  route-1 prolonged system at Σ (P = 4, K = 8); basis rotated so ID-space
  projections are orthonormal, at the settled dimensions; ℓ=0 (e) elements
  ID-orthogonal to the named span; ℓ=1 split into 4 class-(a) gauge + 6 (e)
  quotient elements; each element finally rescaled to unit max |Taylor
  coefficient| (scale recorded).
- **Response ranks on the 6-channel condition set ([B], [K], [R̃],
  [R̃_,n], [h_θθ], [K_θθ]) are W-B2's job** — the channel functionals were
  not W-B1's to apply. W-B1 delivers the dimensions and the basis jets
  above; the ℓ=0 response rank on ([B], [K], [R̃]) from stored functionals
  is 3 (§5). Phase 122's claimed rank 6 at ℓ = 1,2,3 is therefore neither
  confirmed nor refuted here; it must be recomputed by W-B2 on the settled
  bases (10/8/8 solution spaces; 6/8/8 (e) after the ℓ=1 gauge split).
- `wb1_results.json`: full settlement tables, spectra, classification and
  κ data. `wb1_check.json`: 18/21 checks PASS; the three FAILs are exactly
  the ℓ = 1,2,3 claim comparisons (settled 10/8/8 vs claimed 9/7/7) — the
  discrepancy is the result.
