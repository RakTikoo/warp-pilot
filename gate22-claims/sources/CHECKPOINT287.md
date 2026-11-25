# CHECKPOINT 287 — AXIS A: A DIFFERENT DEFORMATION FAMILY, BUILT THROUGH THE TOV IDENTITY, AUDIT-GATED, POSE-TESTED

Phase 287 executes Axis A of the Phase 283 geometry-level
redesign spec (the last of the three axes; B died at counting
cost in Phase 284, C at audit cost in Phase 285). Registration
`phase287/work/p287_registration.md` — family, incumbent
member, controls, build, gate, verdict forms and the
second-member policy all fixed before computation; Amendment
A1 (build solver only) appended mid-phase under the conditions
recorded there and in the Item 1 memo. Frame of record: Phase
166 pin, Gate-19-corrected tensor, float64. No §4b value was
computed or used. No ledger append, no launches (per tasking).

## VERDICTS

- **Item 1: MEMBER BUILT AND AUDIT-CLEAN.** The new member's
  background is built through the TOV identity (J derived,
  never posed) and passes the Phase 285 audit as a gate at all
  181 θ (max|δP₂| = 1.047×10⁻⁶), with the A1.2 smoothness
  guard satisfied (max err 0.318 vs limit 12.677).
- **Item 2: POSE HOLDS AT t = 0.** All seven clauses positive
  under full joint accounting; binding clause **NEC_φ =
  +1.015422**, 24.7% above the incumbent's +0.814164; on-shell
  groups in their registered forms (G1 symbolic exactly 0.0,
  G2 analytic exactly 0.0, G3 exactly 0.0). **The Axis A kill
  does not fire — Axis A is the first of the three redesign
  axes to survive.** The member earns a march registration
  (not launched here).

## THE FAMILY AND THE MEMBER

Family: R(ρ,θ) = R₀ + (𝒜(θ)/2)ρ², 𝒜(θ; Δ) = 0.2 + (−0.5 +
Δ·cos(2θ)) — θ-dependence only (ρ-nonlinearity is invisible at
throat-jet scope: no `Auuuu` jet exists; derived fact).
Incumbent member Δ = 0 (𝒜 ≡ −0.3, bitwise the Phase 264
background). New member Δ = +0.15 by the registered principle
of fixed-mean redistribution (cos(2θ): zero mean, deepest
−0.45 at θ*, shallowest −0.15 at the poles; flare sign kept
everywhere). Controls: C-273 PASS; **C-INC-ROW PASS at max
diff 0.0** (the kill's second form does not fire); C-DERIV —
the O(ρ¹) identity re-derived with 𝒜(θ) symbolic: same form,
**no 𝒜′(θ) term**; C-INC-AUDIT reproduces Phase 285's joint
δP₂ at 2.4×10⁻¹³ through the generalised transport.

## THE BUILD — INCLUDING THE FAILURE THAT TAUGHT THE METHOD

The registered diagonal-secant build terminated MEMBER
AUDIT-DEAD in 6 evaluations (1.165 → 1.258 → 4694 → 3115 →
1014 → 362). Diagnostics proved it a solver pathology: the
diagonal response ∂δP₂/∂J(θ) collapses to +0.014417 at idx
44/136 (median 1.626; no algebraic root — linear root at step
≈ 47, where the channels explode), while the **J′(θ) response
there is ≈ −57 per unit** — the identity is a first-order ODE
in θ for J. Amendment A1 replaced the solver with Newton on
the audit oracle (Jacobian by per-point FD, cond 1.29×10⁴)
and added the narrowing smoothness guard; the original outcome
stays on record in `p287_results.json`. Amended build: **two
Newton iterations** (1.164789 → 3.025×10⁻³ → 1.047×10⁻⁶;
181 → 4 → 0 above floor). J_derived range [−0.889, −0.530] vs
posed [−1.187, −0.716] (max departure 0.544): the identity
asks for a uniformly shallower J. Side facts: the member with
the POSED J already sits at max|δP₂| = 1.165 vs the
incumbent's 1.985 (the redistribution starts 41% closer to
consistency), and the built background's max ladder error
(0.318) is 4× smaller than the incumbent audit's (1.268).

## THE POSE

Row (member vs incumbent): NEC_ρ +1.613597 (+0.227449),
NEC_θ +1.562131 (+0.206231), **NEC_φ +1.015422 binding
(+0.201258)**, WEC +1.790154 (−0.227267, argmin to the pole),
DEC_ρ +1.478577 (+0.092429), DEC_θ +1.506306 (+0.150406),
DEC_φ +1.015422 (+0.201258). Attribution (swap diagnostic):
the deformation profile alone carries +0.107369 of the
binding gain (posed-J row NEC_φ +0.921533); the J-derivation
adds +0.093889 more — building through the identity is worth
margin in its own right. Factorial: the R×Φ cross-term on
NEC_ρ/WEC equals the Phase 262 closed form **exactly** under
the θ-dependent profile with derived J (checker 6.7×10⁻¹⁶);
the tangential "half" heuristic deviates (max 0.2139) and its
true profile is on record; director pairings ≤ 1.9×10⁻¹².

## WHAT THIS MEANS FOR THE PROGRAMME

The geometry-level redesign programme (Phase 283) is **not
closed**: Axes B and C are dead, but Axis A produced a new
throat pose on the first background in the programme that is
TOV-consistent at the audit order by construction — removing,
for this pose, the Phase 285 candidate contributor to the
§4b line's invariance (the O(1)-inconsistent shared
background). The decisive test of that explanation is now
well-posed and is the earned successor: **a march registration
for the Axis A member, whose §4b read decides whether the
five-row invariance was background-borne.** If §4b still fails
unmoved on a consistent background, the invariance is in the
configuration's evolved geometry itself (Phase 283's reading)
with the background explanation excluded; if it moves, Phase
285's anatomy was the carrier. Bracket certification for the
new member rides the same march. Axis B's extension count is
unchanged (this phase consumed the throat-order identity for
the background, not the extension); p1592 still gates
programme-level sustainment wording; Gate-23 stands for its
own pose; the incumbent record is untouched.

## FILES

- Registration (+ Amendment A1): `phase287/work/p287_registration.md`
- Library: `phase287/work/p287_lib.py`
- Registered build driver + results: `phase287/work/p287_run.py`, `phase287/results/p287_results.json` (original outcome on record)
- Diagnostics: `phase287/work/p287_diag.py`, `p287_diag2.py` (+ `.json` outputs)
- Amended build driver + results: `phase287/work/p287_build2.py`, `phase287/results/p287_amended_results.json`
- Built profiles: `phase287/work/p287_built_profiles_amended.npz` (original build's: `p287_built_profiles.npz`)
- Independent checker: `phase287/work/p287_check.py`, `phase287/results/p287_verify.json` — **ALL PASS**
- Memos: `phase287/results/p287_item1_memo.md`, `phase287/results/p287_item2_memo.md`

Checker detail: md5s identical; incumbent row ≤ 5×10⁻⁷; saved
𝒜 matches the family formula exactly; gate re-run from saved
profiles identical (n_above 0, max|δP₂| 1.047228×10⁻⁶); pose
row diff 0.0; G2 analytic zero; G3 = 0.0; factorial identity
6.7×10⁻¹⁶; swap row diff 0.0.
