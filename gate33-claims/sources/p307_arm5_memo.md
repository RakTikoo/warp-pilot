# PHASE 307 — ARM 5: STABILITY AT THE POINTS (scope: each tested point)

**Worker:** red team, Phase 307. **Charge:** registration
`phase307/work/p307_registration.md`, ARM 5. **Points:** the three
flat maximisers M1 (c_V=1), M2 (c_V=2), M10 (c_V=10), Corner B,
and Corner A (for the record), all on the c₁₃=0 slice
(c₊=0, c₋=2c₁, c₃=−c₁, c₄=c₁₄−c₁). **Method:** published
conditions taken from the primary source and evaluated
numerically (programme venv python) at every point. No ledger
append, no launches.

---

## 1. The published conditions (primary source, with equation numbers)

**Source:** Oost, Mukohyama & Wang (OMW), PRD 97, 124023 (2018)
[arXiv:1802.04303], §III and Appendix A (linear perturbations
about Minkowski; the quadratic actions are derived there, not
quoted from secondary literature).

**Ghost-freedom (kinetic-sign).** OMW Eq. (3.1): the time-kinetic
coefficients of all three sectors must be positive,

    q_{S,V,T} > 0 ,

with OMW Eq. (3.2):

    q_S = (1−c₁₃)(2+c₁₃+3c₂)/c₁₂₃ ,
    q_V = c₁₄ ,
    q_T = 1−c₁₃ ,

where c₁₂₃ ≡ c₁+c₂+c₃. Appendix derivation: scalar quadratic
action Eq. (A.9) → ghost condition Eq. (A.10),
q_S ≡ (1−c₁₃)(2+c₁₃+3c₂)/c₁₂₃ > 0; vector action Eq. (A.12) →
Eq. (A.13), q_V ≡ c₁₄ > 0; tensor action Eq. (A.15) →
Eq. (A.16), q_T ≡ 1−c₁₃ > 0. OMW's fn. 2 (at Eq. (3.1)):
in the decoupling limit c_i→0, q_V = c₁₄ vanishes "but the limit
must be taken from the positive side of q_{S,V,T} and
c²_{S,V,T}" — i.e. strict positivity at every finite point.

**Gradient stability (speed-squared positivity).** OMW
Eq. (3.3): c²_{S,V,T} ≥ 0 (evaluated below as strict > 0, the
stronger read), with OMW Eq. (3.4):

    c_S² = c₁₂₃(2−c₁₄) / [ c₁₄(1−c₁₃)(2+c₁₃+3c₂) ] ,
    c_V² = [2c₁ − c₁₃(2c₁ − c₁₃)] / [2c₁₄(1−c₁₃)] ,
    c_T² = 1/(1−c₁₃) .

Appendix: scalar Eq. (A.11), vector Eq. (A.14), tensor
Eq. (A.17) — identical forms. (The charge's expected slice forms
were verified against these equations, not trusted: tensor
c_T² = 1/(1−c₁₃) ✓; vector c_V² → c₁/c₁₄ on the slice ✓;
scalar c_S² with c₁₂₃ = c₂ on the slice = w₀² ✓ — see §2.)

**Mode-energy signs (second published form of the kinetic
conditions).** Jacobson, "Einstein-aether gravity: a status
report," arXiv:0801.1547, §4 (as carried in Phase 298 Row 2's
fence V5, from the full-text retrieval there): the spin-1 mode
energy is positive iff (2c₁ − c₁² + c₃²)/(1−c₁₃) > 0 and the
spin-0 mode energy carries the sign of c₁₄(2−c₁₄) (with the
tensor sector's sign that of (1−c₁₃)). These are evaluated as
an independent cross-form in §3. Note they are *not* identical
in content to q_V > 0 off the slice; on the slice
2c₁ − c₁² + c₃² = 2c₁ (since c₃ = −c₁), so the spin-1 energy
condition is c₁ > 0.

**Explicitly NOT scored as stability conditions:**

- OMW Eq. (3.5), c²_{S,V,T} ≳ 1: this is the **vacuum
  gravi-Čerenkov** requirement, an observational leg of the
  fence (Phase 303's Čerenkov leg), not a ghost/gradient
  condition. It is reported in §3 for completeness but no
  verdict rests on it. In particular Corner B's w₀ = 3247.8
  (c_S² ≈ 1.05×10⁷) is **superluminality, which is not an
  instability** and is not scored as one.
- No tachyon condition beyond c² ≥ 0 exists in the source at
  this (two-derivative, Minkowski-background) level: a negative
  speed squared *is* the tachyonic/gradient instability, and it
  is already Eq. (3.3). No separate subluminality or
  no-superluminality stability requirement is stated by OMW or
  Jacobson.

## 2. Slice reduction (c₁₃ = 0)

With c₃ = −c₁: c₁₂₃ = c₁+c₂+c₃ = **c₂**. The conditions become:

| Condition | Slice form | Content |
|---|---|---|
| q_T > 0 | 1 > 0 | automatic |
| q_V > 0 | c₁₄ > 0 | every point has c₁₄ > 0 |
| q_S > 0 | (2+3c₂)/c₂ > 0 (OMW Eq. (3.11)) | holds iff c₂ > 0 (given c₂ > −2/3); **the scalar kinetic sign is ∝ 1/c₁₂₃ = 1/c₂** |
| c_T² > 0 | 1 | automatic |
| c_V² > 0 | c₁/c₁₄ > 0 | holds iff c₁ > 0 (given c₁₄ > 0) |
| c_S² > 0 | c₂(2−c₁₄)/[c₁₄(2+3c₂)] = w₀² > 0 | holds iff c₁₄ ∈ (0,2), c₂ > 0 |
| spin-1 energy > 0 | 2c₁ > 0 | c₁ > 0 |
| spin-0 energy sign | c₁₄(2−c₁₄) > 0 | c₁₄ ∈ (0,2) |

The danger points the charge flagged are real in form: q_S and
c_S² both turn on **c₂ > 0** (through c₁₂₃ = c₂), and c₂ at the
maximisers is tiny (2.67×10⁻⁶ … 7.96×10⁻⁶) — but tiny *positive*
is positive: the kinetic coefficient q_S = (2+3c₂)/c₂ is then
huge positive, not marginal. Likewise every point sits at
c₁₄ ∈ (0,2) strictly, so (2−c₁₄) > 0 everywhere.

## 3. Numerical evaluation — every condition, every point

Computed with the venv python from the registered point
coordinates. Speeds: c_V and w₀ ≡ c_S recomputed from the
coordinates (they reproduce the registered values: M1 w₀=1.0020,
M2 w₀=1.0001, M10 w₀=1.0007, Corner B w₀=3247.85, Corner A
w₀=1.000000).

| Quantity (condition) | M1 | M2 | M10 | Corner B | Corner A |
|---|---|---|---|---|---|
| (c₁, c₂, c₁₄) | (2.6568e-6, 2.6676e-6, 2.6568e-6) | (2.5443e-5, 6.3620e-6, 6.3608e-6) | (7.9511e-4, 7.9621e-6, 7.9511e-6) | (0.08293104, 2/21, 7.9e-9) | (0.1, 2.500125e-5, 2.5e-5) |
| q_T = 1−c₁₃ > 0 | 1 ✓ | 1 ✓ | 1 ✓ | 1 ✓ | 1 ✓ |
| q_V = c₁₄ > 0 | 2.6568×10⁻⁶ ✓ | 6.3608×10⁻⁶ ✓ | 7.9511×10⁻⁶ ✓ | 7.9×10⁻⁹ ✓ | 2.5×10⁻⁵ ✓ |
| q_S = (2+3c₂)/c₂ > 0 | 7.4974×10⁵ ✓ | 3.1437×10⁵ ✓ | 2.5119×10⁵ ✓ | 24.000 ✓ | 7.9999×10⁴ ✓ |
| c_T² = 1 > 0 | 1 ✓ | 1 ✓ | 1 ✓ | 1 ✓ | 1 ✓ |
| c_V² = c₁/c₁₄ > 0 | 1 ✓ | 4.0000 ✓ | 100.00 ✓ | 1.04976×10⁷ ✓ | 4000.0 ✓ |
| c_S² = w₀² > 0 | 1.00406 ✓ | 1.00018 ✓ | 1.00137 ✓ | 1.05485×10⁷ ✓ | 1.00000 ✓ |
| spin-1 energy num. 2c₁ > 0 | 5.3136×10⁻⁶ ✓ | 5.0886×10⁻⁵ ✓ | 1.5902×10⁻³ ✓ | 0.16586 ✓ | 0.20000 ✓ |
| spin-0 energy factor c₁₄(2−c₁₄) > 0 | 5.3136×10⁻⁶ ✓ | 1.2722×10⁻⁵ ✓ | 1.5902×10⁻⁵ ✓ | 1.5800×10⁻⁸ ✓ | 4.9999×10⁻⁵ ✓ |
| (2−c₁₄) | 1.9999973 | 1.9999936 | 1.9999920 | 1.99999999 | 1.9999750 |
| (2+c₁₃+3c₂) = 2+3c₂ | 2.0000080 | 2.0000191 | 2.0000239 | 2.2857143 | 2.0000750 |
| c₁₂₃ = c₂ | 2.6676×10⁻⁶ | 6.3620×10⁻⁶ | 7.9621×10⁻⁶ | 0.0952381 | 2.500125×10⁻⁵ |
| *(not scored)* c² ≳ 1 Čerenkov read | c_S²=1.004, c_V²=1 | c_S²=1.0002, c_V²=4 | c_S²=1.0014, c_V²=100 | c_S²≈1.05×10⁷, c_V²≈1.05×10⁷ | c_S²=1, c_V²=4000 |

**No condition fails at any point.** The closest approaches to
a boundary, stated honestly:

- q_V = c₁₄ at Corner B is 7.9×10⁻⁹ — strictly positive, as
  OMW's fn. 2 requires (the limit c₁₄→0 is the decoupling limit,
  taken from the positive side; Corner B is a finite point on
  the positive side, not the limit).
- c₂ at the maximisers is ~10⁻⁶–10⁻⁵, strictly positive, so
  q_S is not near zero but ~10⁵–10⁶ (q_S ∝ 1/c₂). The scalar
  ghost condition would fail only at c₂ ≤ 0 or c₂ ≤ −2/3, both
  far from every tested point in sign, not merely in magnitude.
- c_S² at Corner A is exactly 1.00000 (the Čerenkov edge by
  construction) — positive; gradient stability needs only > 0.

## 4. Verdict — ARM 5: HOLDS (all points, all published conditions)

Every published Einstein-aether stability condition —
ghost-freedom q_{S,V,T} > 0 (OMW Eqs. (3.1)–(3.2); App. Eqs.
(A.10), (A.13), (A.16)), gradient stability c²_{S,V,T} > 0
(OMW Eq. (3.3)–(3.4); App. Eqs. (A.11), (A.14), (A.17)), and the
Jacobson §4 mode-energy signs — **passes at M1, M2, M10,
Corner B and Corner A**, with the values tabulated in §3. No
point is excluded on stability grounds; Corner B's
superluminal scalar speed (w₀ = 3247.8) is not an instability
and was not scored as one, and the Čerenkov leg (OMW Eq. (3.5))
is a separate fence leg, reported but not scored here.

**Retrieval limits (on the face of this memo).** OMW
arXiv:1802.04303 retrieved in full text 2026-11-24 (ar5iv HTML,
complete: §III Eqs. (3.1)–(3.5), (3.11)–(3.20) and Appendix A
Eqs. (A.9)–(A.17) read directly). Jacobson arXiv:0801.1547:
the mode-energy sign forms are as carried from Phase 298's
full-text retrieval of that source (its §4), cross-checked for
consistency with OMW's q-coefficients on the slice (both reduce
to c₁ > 0 / c₁₄(2−c₁₄) > 0 / (2+3c₂)/c₂ > 0 here); no verdict
rests on Jacobson alone — OMW's conditions, read directly in
this arm, already cover all three sectors and all pass. The
conditions evaluated are the two-derivative Minkowski-background
conditions the sources publish; nonlinear/background-dependent
instability (e.g. on curved or cosmological backgrounds) is
outside both sources' stated scope for these conditions and
outside this arm's charge.
