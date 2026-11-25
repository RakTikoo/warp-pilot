# PHASE 307 — ARM 3 MEMO: FULL-THEORY COSMOLOGY (red team)

Registration: `phase307/work/p307_registration.md`, Arm 3.
Charge: retrieve cosmological perturbation constraints for FULL
Einstein-aether (general c_i, not the khronometric ξ = 1 corner
Phase 302 used), translate each onto the c₁₃ = 0 slice in the EA
dictionary, and apply to the three flat maximisers and Corner B.
A khronometric result imported as if it were a full-EA one does
not discharge this arm and does not break a point.
All sources retrieved 2026-11-24. Computation: sympy/numeric
evaluation in the Phase 166 venv (script run this arm; identities
below verified symbolically, differences simplify to 0).

## VERDICT: HOLDS (weak)

Wording, exactly as registered: **no applicable full-EA
cosmological constraint exists in retrievable primary form that
excludes any of the four tested points.** This is an absence
statement, not a pass. Every full-EA cosmological MCMC retrieved
scans a PPN-reduced subspace that none of the four points lies
on (shown algebraically in §3), and the one tighter
G_cos bound in print (Frusciante & Benetti 2021, 1.9×10⁻³) is a
khronometric/Hořava result whose stated scope does not cover a
non-hypersurface-orthogonal EA point. The nearest threats are
recorded with their numbers in §4 — Corner B would fall to two
of them if a transfer existed; no retrieved source licenses the
transfer. The flat maximisers are not merely unexcluded: their
cosmological deviations are 10⁻⁵-class (§2), two to three orders
below every cosmological cap discussed anywhere in this memo,
under any dictionary.

## 1. The full-EA dictionary (derived from EA sources, not imported)

Sources: Jacobson, arXiv:0711.3822 (status report / CPT07
review), §2 (Newtonian limit) and §3 (homogeneous cosmology);
Zuntz, Ferreira & Zlosnik, arXiv:0808.1824, §I–II; Audren, Blas,
Ivanov, Lesgourgues & Sibiryakov, JCAP 03 (2015) 016
[arXiv:1410.6514], §§II–III (Eqs. 4, 10, 13, 20, 24–25).

EA combinations: c₊ = c₁+c₃, c₋ = c₁−c₃, c₁₄ = c₁+c₄,
c₁₂₃ = c₁+c₂+c₃, and Zuntz et al.'s background combination

    α ≡ c₁ + 3c₂ + c₃.

Jacobson's §3 (his Eq. (8)): the Friedmann equation's constant is

    G_cos = G / [ 1 + (c₁₃ + 3c₂)/2 ],

and his §2: G_N = G / [1 − c₁₄/2]. Sympy verification (this arm):
α − (c₁₃ + 3c₂) simplifies to 0 identically — i.e. **the EA
combination in G_cos is α = c₁+3c₂+c₃ = c₁₃+3c₂**, so

    G_cos/G_N = (1 − c₁₄/2) / (1 + α/2) = (2 − c₁₄)/(2 + c₁₃ + 3c₂),
    G_N/G_cos − 1 = (c₁₄ + c₁₃ + 3c₂)/(2 − c₁₄).

This is the full-EA form, derived here from the EA source. It is
NOT taken from Phase 302: Phase 302's applied number was
Frusciante & Benetti's Hořava bound, whose dictionary
(η = c₁₄, λ_H − 1 = c₂ at ξ = 1, verified there by α₁/α₂/G_c
identities for the *khronometric* nominee) is a statement about
the hypersurface-orthogonal theory. That the EA G_cos bridge has
the same functional shape is a derived fact (above), not a
licence to import the khronometric MCMC's bound — the EA
perturbation sector contains the spin-1 modes and the
c₁₂₃-carrying scalar system that the ξ = 1 analysis does not
contain. (Convention note: Zuntz et al.'s c_i carry the opposite
overall sign to Jacobson's — their footnote 15 — so their
Friedmann factor (2+c₁₄)/(2−α) is the same statement in their
signs; the programme's conventions are Jacobson/OMW/YBBY's, and
the formula above is in those conventions, matching the fence's
existing BBN leg, Phase 303 `p303_audit.py`:
|(1−c₁₄/2)/(1+3c₂/2) − 1| on the slice.)

On the slice c₁₃ = 0 (c₃ = −c₁, c₊ = 0, c₋ = 2c₁), sympy:
c₁₂₃ reduces to c₂ exactly, α reduces to 3c₂, and

    G_cos/G_N = (2 − c₁₄)/(2 + 3c₂),   G_cos/G_N − 1 = −(c₁₄ + 3c₂)/(2 + 3c₂).

The scalar (spin-0) cosmological sound speed in Audren et al.'s
parametrisation, c_χ², is Jacobson's spin-0 speed squared,
c₁₂₃(2−c₁₄)/[c₁₄(1−c₁₃)(2+c₁₃+3c₂)], which on the slice is
(2−c₁₄)c₂/[(2+3c₂)c₁₄] — identically the fence's w₀² (YBBY
Eq. (108) on the slice). So c_χ² = w₀² at every tested point.

## 2. The four points in cosmological combinations

| Point | α = 3c₂ | G_cos/G_N − 1 | c_χ² = w₀² |
|---|---|---|---|
| flat c_V=1 (2.6568e-6, 2.6676e-6, 2.6568e-6) | 8.0028×10⁻⁶ | −5.3298×10⁻⁶ | 1.004060 |
| flat c_V=2 (2.5443e-5, 6.3620e-6, 6.3608e-6) | 1.9086×10⁻⁵ | −1.2723×10⁻⁵ | 1.000176 |
| flat c_V=10 (7.9511e-4, 7.9621e-6, 7.9511e-6) | 2.3886×10⁻⁵ | −1.5919×10⁻⁵ | 1.001368 |
| Corner B (0.08293104, 2/21, 7.9e-9) | 0.285714 | **−0.125000** | **1.054852×10⁷** |

Corner B's G_cos deviation is exactly its BBN saturation
(−1/8), as it must be: same bridge, same point. The flat rows'
deviations are ≤ 1.6×10⁻⁵ — factors 357 / 149 / 119 below even
the (inapplicable, khronometric) 1.9×10⁻³ cap of §4, and factors
126–376 below Audren's EA surface parameter limit (§3).

## 3. The retrieved full-EA constraints — and their scopes

### 3.1 Zuntz, Ferreira & Zlosnik (2008), arXiv:0808.1824 — EA, WMAP3 + Boomerang + ACBAR/VSA + SDSS + 2dF + SNe Ia

The only pre-Planck EA-native cosmology MCMC retrieved. Its
scope is stated on its face and is decisive: the analysis runs
on two subspaces only.

- **Class 𝒞:** the PPN-exact subspace — α₁ = α₂ = 0 imposed by
  expressing c₂ and c₄ through (c₁, c₃):
  c₂ = (−2c₁² − c₁c₃ + c₃²)/(3c₁), c₄ = −c₃²/c₁ — with the
  binary-pulsar relation between c₊ and c₋ further imposed in
  the "weak pulsar" variant. Its outputs are constraints in the
  (c₊, c₋) plane (their Fig. 4; Table I means are O(0.1)-class
  values on that surface).
- **Class ℰ:** the exotic subspace c₁ = c₃ = 0, where cosmology
  is "potentially the only way of constraining" the couplings;
  there, with c₁=c₂=c₃=0, −0.05 < c₄ < 0 (their signs), and with
  c₂ freed, c₂ and c₄ ∈ [−0.01, 0] (their signs; = [0, 0.01] in
  the programme's Jacobson signs).

**Application test (this arm, algebraic):** on the c₁₃=0 slice
the class-𝒞 relations demand c₂ = 0 and c₄ = −c₁ (hence
c₁₄ = 0). All four tested points have c₂ > 0 and c₁₄ > 0:
flat rows c₂ = 2.67/6.36/7.96×10⁻⁶, c₁₄ = 2.66/6.36/7.95×10⁻⁶;
Corner B c₂ = 0.095238, c₁₄ = 7.9×10⁻⁹. (Corner B happens to sit
on the c₄ = −c₁ relation to its quoted digits — c₄ = −0.08293103
vs required −0.08293104 — but fails the c₂ = 0 relation by the
whole of c₂ = 2/21.) No tested point is in class 𝒞; none is in
class ℰ (all have c₁ ≠ 0; Corner B's c₂ = 0.095 also exceeds the
class-ℰ interval by ×9.5, in a subspace it is not in).
**Disposition: retrieved, scope-excluded — its numbers have no
projection onto the tested points, exactly the status Phase 302
recorded for the generalised-EA line, now verified for the
letter itself rather than inherited.**

### 3.2 Zuntz et al. (2010), PRD 81, 104015 [arXiv:1002.0849], and Battye, Bolliet, Pace & Trinh (2018) [arXiv:1811.07805] — generalised EA F(K)

The generalised-EA line Phase 302 scope-excluded, re-checked
here at abstract/full-text-skim grade: Zuntz et al. 2010
constrain designer F(K) models (a dark-matter candidate, which
"does not fit the data", and a dark-energy candidate, fitted in
its kinetic index n_ae and density parameters); Battye et al.
run a designer EoS approach against Planck CMB + lensing and
bound w_de (−1.04 class at 68% CL), not the c_i. Neither paper's
parameters include the two-derivative linear corner
(c₁, c₂, c₁₄); the linear EA theory is the F(K) ∝ K tangent
case, which these designer scans do not isolate.
**Disposition: scope-excluded, no projection exists in
published form — confirmed, not merely inherited from
Phase 302.**

### 3.3 Audren et al. (2015) — the EA case, Planck 2013 + WiggleZ

Audren et al. run BOTH theories. Their EA case is a genuine
full-EA cosmological perturbation analysis (CLASS, scalar
sector; they note the EA vector sector's possible CMB
polarisation effects and leave them for future work). But its
scope condition is the same in kind as Zuntz's: **vanishing
PN parameters are imposed as exact priors** — their Eqs. (10a)
and (10b) for EA — reducing the EA scan to the two parameters
(log α, log c_χ²) on that surface, with (β, λ)-combinations
slaved by the PN relations. Their Table I, EA with
Lorentz-invariant DM (Y ≡ 0), 95% CL upper limits: the scanned
coupling parameter < 1.0×10⁻³ and **c_χ² < 427** (with Y ≠ 0:
< 5.0×10⁻³ and < 240). Mechanism (their §§IV–V): on the PN
surface the enhanced-gravity (G_N vs G_cos) effects vanish to
leading order in EA (their Eq. (25) is exactly the vanishing of
the α-combination), and the remaining scalar-sector effects are
the shear (∝ β = c₁₃) and the c_χ²-carrying aether perturbation
dynamics.

**Application test:** the tested points are not on Audren's
surface — α₁ = −4c₁₄ ≠ 0 at every point (−1.06×10⁻⁵,
−2.54×10⁻⁵, −3.18×10⁻⁵, −3.16×10⁻⁸) and α₂ ≠ 0 likewise; they
satisfy the *bounded* PPN fences, not exact vanishing. Under
the discipline Phase 302 itself applied to this same paper's
khronometric row (1-D limits "recorded with surface scope, not
applied off-surface"), the EA 1-D limits are recorded, not
applied. For the record, their face values against the points:
the coupling-parameter limit passes all four points with
margins ×376 / ×157 / ×126 / ×1.27×10⁵; the c_χ² < 427 limit
passes the flat rows by a factor ~425 (c_χ² ≈ 1.000–1.004) and
**Corner B exceeds it by a factor 2.47×10⁴**
(c_χ² = w₀² = 1.0549×10⁷ vs 427). That exceedance is stated
here in full, not buried: it is the single largest
cosmology-side number against any tested point. It does not
break Corner B under the registered verdict form — the limit
is a marginalised projection of a scan on a surface Corner B
is not on, where the other scan parameter is slaved to it by
relations Corner B violates; off that surface the scalar
sector acquires the G_cos deviation (−0.125 at Corner B) and
nonzero α₁, α₂, which the scan's likelihood never evaluated.
Phase 302 faced the identical structure for the khronometric
rows at c_S = 100 (c_χ² = 10⁴ vs the kh limit 91) and recorded
it as "not addressed in that form"; consistency of method
requires the same disposition here, and the red team flags
that this is a *method* protection, not a physical one: an
off-surface EA MCMC is the named instrument that could
convert this record into a verdict either way, and none was
retrieved.

### 3.4 Growth / fσ8 and CMB c_i bounds — search outcome

Directed searches were run for: EA growth-of-structure / fσ8
bounds on the c_i; Planck-era EA analyses with c₁…c₄ free or in
EA combinations beyond §§3.1–3.3; CMB bounds from the aether
perturbation sector. Outcome: no additional primary analysis
exists in retrievable form. What exists is (i) the G_cos
combination as the growth-relevant quantity (Audren et al.'s
identification: sub-horizon growth δ ∝ a^(−1+√(1+24G_N/G_cos))/4
in matter domination — a statement about the same α
combination evaluated in §2, bounded by data only inside the
scans of §3); (ii) Carroll & Lim (2004), qualitative
(order-unity couplings disturb the CMB), superseded; (iii) Lim
(2005) / Kanno & Soda (2006) perturbation treatments, whose
own conclusion is that the late-time CMB/matter effects are
small and degenerate with neutrino masses and galaxy bias —
no bound on the c_i is stated. No fσ8-specific EA bound on
(c₁, c₂, c₁₄) was found.

## 4. The khronometric bound, faced squarely (not applied)

Frusciante & Benetti (2021): |G_cos/G_N − 1| ≤ 1.9×10⁻³
(95% CL, Planck 2018 BKP + lensing + DES + Pantheon, ξ = 1
Hořava/khronometric MCMC). Applied *as if* it transferred, the
flat rows pass (factors 357 / 149 / 119 of headroom) and
**Corner B is excluded by a factor 65.8** (0.125 vs 1.9×10⁻³) —
the same factor by which it killed Phase 302's khronometric
corner, because the G_cos bridge coincides. The transfer is
not licensed: FB2021's theory is the hypersurface-orthogonal
one (their action is Hořava's at ξ = 1; there is no spin-1
sector, no c₁ as an independent coupling, and their sampled
parameters are (λ_H, η)); the tested points are points of the
full theory at which the vector sector exists and
c₋ = 0.166 (Corner B) is deep in the region where the EA
scalar system's input differs from the kh one through A
(Phase 303 §1.2). Per the arm's standing rule — never import a
khronometric result as if it were a full-EA one — this is
recorded as the arm's principal *conditional* threat, not a
break. If a future EA-native MCMC bounds the α combination at
anywhere near 10⁻³, Corner B falls by ~two orders of magnitude
and the flat rows stand by ~two orders of magnitude; that
asymmetry is the honest summary of Arm 3's cosmology exposure.

## 5. Per-point disposition

- Flat c_V = 1, 2, 10 maximisers: **not excluded by any
  retrieved constraint, applicable or not.** Every number
  computed for them in this arm (G_cos deviation ≤ 1.6×10⁻⁵,
  c_χ² ≈ 1.00, α ≤ 2.4×10⁻⁵) passes every cap discussed,
  including the inapplicable ones, with margins ≥ ×119.
- Corner B: **not excluded by any applicable retrieved
  constraint.** It carries two recorded conditional threats,
  both stated with factors: FB2021-transfer (×65.8, scope not
  licensed) and Audren-EA c_χ² surface limit (×2.47×10⁴,
  surface not containing the point). Its applicable
  cosmological bound remains the one already in the fence:
  BBN, saturated at margin 0.

## 6. Retrieval limits (on the face of this memo)

Retrieved in full text: Jacobson arXiv:0711.3822 (archive.org
full text, §§2–3 read verbatim); Zuntz et al. arXiv:0808.1824
(full, incl. Table I and footnotes 15, 20); Audren et al.
arXiv:1410.6514 (full, incl. Table I and §§IV–V). Abstract/
record grade: Zuntz et al. arXiv:1002.0849; Battye et al.
arXiv:1811.07805 (abstract + introduction skim). Frusciante &
Benetti 2021 as retrieved in full by Phase 302 (its numbers
and scope are quoted from that record, not re-retrieved).
No INSPIRE/Web-of-Science forward-citation sweep was run;
the search was English-language web-index plus arXiv, the
same limits as Gate-32's novelty search. The verdict's weak
form is conditioned on exactly these limits.

DESK (Arm 3): full-EA cosmology contacted (Zuntz 2008 EA MCMC —
surface-scoped, no point on its surfaces; Audren 2015 EA case —
PN-surface-scoped; FB2021 kh bound faced, transfer not
licensed). No applicable full-EA cosmological constraint
excludes any tested point: **HOLDS (weak)** — an absence
statement. Corner B's conditional exposure (×65.8 under an
unlicensed kh transfer; c_χ² ×2.47×10⁴ over a surface limit it
is not on) is on the record.
