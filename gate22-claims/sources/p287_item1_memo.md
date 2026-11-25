# P287 ITEM 1 MEMO — THE FAMILY AND ITS FIRST NEW MEMBER

**Phase 287, Item 1** (Axis A of the Phase 283 geometry-level
redesign spec). Registration `phase287/work/p287_registration.md`
(binding, written before any deciding number; Amendment A1
appended mid-phase under the conditions stated there). Frame of
record: Phase 166 pin, Gate-19-corrected tensor, float64. All
controls passed; the member was built through the TOV identity
and passed the Phase 285 audit as a gate. **Verdict: MEMBER
BUILT AND AUDIT-CLEAN** (Item 2 therefore ran; its memo is
`p287_item2_memo.md`).

## 1. The family

Deformation family (registration §1): the areal radius
R(ρ,θ) = R₀ + (𝒜(θ)/2)·ρ² with

    𝒜(θ; Δ) = 0.2 + δ(θ; Δ),   δ(θ; Δ) = −0.5 + Δ·cos(2θ).

It departs from the incumbent R_a = R_base + (a/2)ρ² by
**θ-dependence only**: the deformation becomes an angular
profile. (ρ-nonlinearity, the spec's other branch, is invisible
at throat-jet scope — no `Auuuu` jet exists in the machinery, so
a ρ⁴ term changes no jet and no channel: a derived fact of this
phase.) The throat jets of a θ-dependent 𝒜 are admissible
exactly: A = R₀, Ah = 0, Au = 0, Auh = 𝒜′(θ)·ρ|₀ = 0, Ahh = 0 —
every non-Auu A-jet keeps its incumbent throat value, and the
channels consume 𝒜 only through the 'Auu' entry. **Incumbent
member: Δ = 0** (𝒜 ≡ −0.3, the Phase 264 joint-pose background,
bitwise). **New member: Δ = +0.15**, chosen by the registered
principle of **fixed-mean redistribution** — cos(2θ) is the
lowest nonconstant axisymmetric harmonic with zero mean over
[0, π], so the member carries the incumbent's mean deformation
and differs only in angular placement: 𝒜 ∈ [−0.45, −0.15],
deepest (−0.45) at the clause-binding locus θ*, shallowest
(−0.15) at the poles. Δ = |𝒜_inc|/2 keeps the flare sign at
every θ and the depth within [0.5×, 1.5×] of incumbent
pointwise. The principle was registered before the pose test;
no clause value entered it.

## 2. Controls (all before any new-member read)

- **C-MD5**: protected engines identical before/after both
  drivers (p1692 `1781b544…`, p167 `9db35c0b…`, p1621
  `1f12ec29…`).
- **C-273** (floor calibration): PASS — Phase 273's original
  profile FAILS (c₃ min −1.721725×10⁻⁸ at r = 39.375) and its
  RB-2 repair PASSES (+1.733412×10⁻¹¹, P′−P_TOV ≡ 0.0),
  reproduced with Phase 285's own drivers.
- **C-INC-ROW** (the Axis A kill's second form): **PASS at max
  diff 0.0** — the family's incumbent member, run through the
  parametrised machinery, reproduces the Phase 264 joint row
  exactly (NEC_ρ 1.386147994784475, NEC_θ 1.3559004940354429,
  NEC_φ 0.8141638620472562, WEC 2.0174214338470633, full seven
  clauses). The kill does not fire.
- **C-DERIV**: the O(ρ¹) conservation identity re-derived with
  𝒜 a symbolic FUNCTION of θ (PATH-S, sympy exact): the
  coefficient is P₂ + J(θ)·(ρ_m + p_ρ) + (𝒜(θ)/R₀)·(2p_ρ −
  p_θ − p_φ) — **no 𝒜′(θ) term appears**; the Phase 285 audit
  generalises verbatim. PATH-F confirms the coefficients at FD
  scale at five sampled θ with the member's 𝒜(θ) inserted.
- **C-INC-AUDIT**: the generalised audit machinery at the
  incumbent member reproduces Phase 285's stored joint-arm δP₂
  profile at max abs diff **2.4×10⁻¹³** (181/181 above floor,
  max|δP₂| = 1.984988) — the generalised transport (Phase 285's
  transport plus the 𝒜′(θ) term in the Fh slot, §4 of the
  registration) IS Phase 285's transport at 𝒜′ ≡ 0.

## 3. The registered build, its pathology, and Amendment A1

The registered secant build ran first and terminated **MEMBER
AUDIT-DEAD** after its 6 registered evaluations (trace:
1.164789 → 1.258383 → **4694.13** → 3115.30 → 1014.14 →
361.59). Two build-procedure diagnostics (`p287_diag.py`,
`p287_diag2.py` — diagnostics, not deciding reads) established
that this outcome is a **solver pathology, not a member
property**:

- The diagonal response s(θ) = ∂δP₂/∂J(θ) has median |s| =
  1.626 but falls to **+0.014417 at idx 136 (θ = 2.363426) and
  idx 44 (θ = 0.778167)**. The secant step there was **47.19**;
  a localised J scan over ±2 at idx 136 moves δP₂ only +0.652 →
  +0.709 — there is no algebraic root (the linear root sits at
  ≈ −47, where the transported channels explode through
  Φ ⊃ (J/2)ρ²: the 4694 figure).
- But δP₂(θ) also depends on **J′(θ)** through the transport's
  Fh slot, and there the response is dominant: an odd ramp of
  amplitude ±0.5 centred at idx 136 (J(θ_w) itself unchanged)
  swings δP₂(θ_w) by **∓28.7** (response ≈ −57 per unit).

The identity, as an equation for the profile J(θ), is a
**first-order ODE in θ**, not 181 independent algebraic
equations; a diagonal secant cannot pose it. Amendment A1
(appended to the registration after the diagnostics and before
the amended build — the deciding read it governs; gate, floor,
member, verdict forms and the second-member policy unchanged)
replaced the solver with a Newton iteration on the audit
oracle's full δP₂ profile and added a narrowing smoothness
guard (A1.2: the gate counts only if max err(built) ≤ 10× max
err(incumbent audit) = 12.677). The original build's outcome
stays on the record (`p287_results.json`), superseded as a
member verdict by the amendment's reasoning, not deleted.

## 4. The amended build and the gate

Newton on F(J) = δP₂(J), Jacobian estimated once by per-point
FD (δJ = 0.01, 181 audits, 4.3 s, condition number 1.29×10⁴):

| iter | max|δP₂| | θ above floor |
|---|---|---|
| 0 (posed J) | 1.164789 | 181 |
| 1 | 3.025×10⁻³ | 4 |
| 2 | **1.047×10⁻⁶** | **0** |

**Gate (fresh audit of the built background, Phase 285 floor
verbatim): PASSES at all 181 θ.** max|δP₂| = 1.047228×10⁻⁶
(argmax θ = 3.121593, at the grid's south edge); CTRL-T passes
at diff 0.0; m(0,θ) = 0.4 exactly (deviation 0.0); **guard:
max err(built) = 0.318005 ≤ 12.677** (2.5% of the limit; the
built background's ladder error is also 4× smaller than the
incumbent audit's max err 1.268). J_derived profile: range
[−0.889383, −0.530265] against the posed j_prof range
[−1.187050, −0.715625] — the identity asks for a uniformly
shallower J; max |J_derived − j_prof| = 0.543618. Built
profiles saved at `phase287/work/p287_built_profiles_amended.npz`.

Two facts worth the record. (i) Even before derivation, the
new member's background with the POSED J sits at max|δP₂| =
1.164789 against the incumbent's 1.984988 — the fixed-mean
redistribution starts 41% closer to TOV consistency. (ii) The
response anatomy is a new structural fact about the identity
in this class: the diagonal J-response has zeros (between idx
135 and 136 the uniform-shift slope changes sign), and at
those θ the identity is carried entirely by the J′ coupling —
any future build through this identity must be posed as the
ODE it is.

## 5. Verdict

**MEMBER BUILT AND AUDIT-CLEAN.** The Δ = +0.15 member's
background is built through the TOV identity (J derived, never
posed) and passes the Phase 285 audit as a gate at every θ,
with the A1.2 smoothness guard satisfied. Item 2 (the pose
test) therefore ran; see `p287_item2_memo.md`. Independent
checker: `phase287/results/p287_verify.json` — ALL PASS (gate
re-run from the saved profiles matches the driver's gate to
the digit; pose row reproduced at diff 0.0).

Fences: this verdict is about the background's O(ρ¹)
TOV-consistency at throat scope, nothing more. It does not
touch p1592, Gate-23's verdicts for their own pose, or any
incumbent record.
