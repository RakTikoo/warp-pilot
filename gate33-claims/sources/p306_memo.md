# PHASE 306 — THE GUPTA CROSS-CHECK: MEMO

**Registration:** `phase306/work/p306_registration.md`
(ledger entry 760's charge; verdict forms fixed before any
Gupta evaluation was run). Gate-32 §6 charged this as its
successor under the number 305; the parent renumbered it
306 (Phase 305 is the instrument phase). The charge's
substance is unchanged.
**Computation:** `phase306/work/p306_eval.py` + `.out`
(controls, transcription cross-check, main evaluation,
supplementary sweep), `phase306/work/p306_cornerB.py` +
`.out` (Corner B's α̂₂ read under σ_Gupta and the shrunk
corner). mpmath at 60 digits; inputs exact decimals.
**Source text:** Gupta, Herrero-Valea, Blas, Barausse,
Cornish, Yagi & Yunes, CQG **38**, 195003 (2021),
arXiv:2104.04596 **v2** — retrieved in full 2026-11-24 as
the arXiv PDF **and** the arXiv e-print LaTeX source; all
formulae below are transcribed from the LaTeX source
(`phase306/work/p306_gupta_eq80_source.txt` preserves the
deciding equation verbatim).

**VERDICT: AGREEMENT** (registered form 1 of ledger 760).
At every deciding point, Gupta et al.'s post-Minkowskian
σ_Æ falls inside the registered bracket f ∈ [0.7, 1.3]
around the rung-2 values:

| Deciding point | σ (rung-2, G32-C) | σ (Gupta 2021) | ratio |
|---|---|---|---|
| Flat-row maximiser, c_V = 2 | 2.5952×10⁻⁶ | 2.4539×10⁻⁶ | **0.9456** |
| Flat-row maximiser, c_V = 10 | 3.2437×10⁻⁶ | 2.8713×10⁻⁶ | **0.8852** |
| Corner B | 2.9546×10⁻⁹ | 2.7200×10⁻⁹ | **0.9206** |

**Promotion (as registered): G32-C, G32-E and G32-F are
promoted to second-pathed grade by independent method** —
the YBBY Eq. (184) weak-field-anchor values of Gate-32's
claim set now stand cross-checked against the literature's
own computed quantity in this corner, Gupta et al.'s
post-Minkowskian σ_Æ, by a method that shares no step with
the anchor beyond the leading-order limit both records
contain (the overlap control, §2). One quantified
consequence rides on G32-E's promotion, stated in §5: at
σ_Gupta, Corner B's literal coordinates sit 23% over the
α̂₂ bound and the surviving corner is the slightly shrunk
one (c₁₄* = 6.4227×10⁻⁹) — exactly the shrink G32-E's own
bracket span already discloses, now measured rather than
bracketed. No novelty wording attaches to the σ
computation in any form: it is KNOWN (Gupta et al. 2021),
per Gate-32.

---

## 1. Item 1 — Gupta et al. retrieved in full; their σ results

The full text was obtained (arXiv v2 PDF + LaTeX source),
closing the readability gap Gate-32 recorded (its mirror
truncated at §5.3.1; IOP paywalled). Equation numbers
below are the published v2 numbering; Gate-32's charge
cited Eqs. 52–57/75–76 from a partial mirror — in v2 the
extraction is Eq. (58) and the Ã series is Eq. (76).

**Their σ apparatus, as printed:**
- The O(v⁰) background is the modified TOV system in
  (α₁, α₂, c_σ, c_ω) (their Eqs. 46–48); the O(v) system
  is Eqs. (53)–(55). The sensitivity is extracted from the
  asymptotic integration constant à la YBBY:
  **σ = 2Ãα₁/(α₁ + 8)** (their Eq. 58), Ã the 1/r
  coefficient of W₁^ext.
- **Method 1** (YBBY's direct shooting) is shown
  numerically unstable in the post-GW region (the
  σ ≈ Ãα₁/4 cancellation) — their Fig. 1.
- **Method 2** (the results method) is post-Minkowskian:
  the O(v) system is expanded in compactness 𝒞 and solved
  order by order (background unexpanded — a partial
  resummation). Ã = (1/M_*) Σ_{j≥2} Ã_j ε^j with
  **Ã₁ = 0 identically** (their Eq. 76 and §5.2: the O(𝒞)
  W₁₁ solution matches only with Ã₁ = D̃₁ = 0), so the
  leading contribution is O(𝒞²) in Ã, i.e. O(𝒞) in σ.
  For the tabulated APR4 EoS the coefficients Ã_j are
  numerical; the truncation order (n = 3) is fixed by
  convergence onto Method 1 where Method 1 is stable
  (their Fig. 2).
- **Weak-field limit** (their Eq. 77):
  s_wf = (α₁ − (2/3)α₂)·Ω/M_* — the YBBY Eq. (184) anchor,
  present inside their computation as its O(𝒞¹) term.
- **The closed form** (their §5.3.2, Eq. (80),
  `tolman_sens_C` in the source): for the Tolman VII EoS
  the whole Method-2 computation is analytic, giving
  s(𝒞) as an explicit series through O(𝒞³) in
  (α₁, α₂, c_ω) — reproduced verbatim in the work file
  cited above. Its 𝒞¹ term is (5/21)𝒞(−3α₁ + 2α₂)
  [= (α₁ − (2/3)α₂)·Ω/M_* with Tolman VII's
  Ω/M_* = −(5/7)𝒞 + O(𝒞³), their Eq. (81)]; its 𝒞² and
  𝒞³ terms carry the strong-field and c_ω-dependent
  content the anchor lacks. A companion form s(Ω/M_*)
  through O((Ω/M_*)³) is their Eq. (82). They adopt the
  Tolman VII analytic sensitivities **for all subsequent
  calculations** (§5.3.2, final paragraph), on the
  strength of Fig. 3's EoS universality (< 3% across
  seven EoSs at the Fig. 3 tuple).

**Enumeration — the printed σ tuples, complete
(§§5.3.2–7 read in full; the gate's gap is closed).**
Exactly three discrete parameter tuples carry printed
σ results in the paper:
1. (§5.1, Fig. 1) (α₁, α₂, c_ω) = (10⁻⁴, 4×10⁻⁷, −0.1):
   the S₁ field plot illustrating Method 1's instability
   — no σ curve.
2. (§5.3.1, Fig. 2; tabulated APR4) (α₁, α₂, c_ω, c_σ) =
   (10⁻⁴, 4×10⁻⁷, 10⁻⁴, 0): σ(𝒞) curves at PM truncation
   orders n = 1, 2, 3, against Method 1 and the
   weak-field curve (which coincides with n = 1).
3. (§5.3.2, Fig. 3; Tolman VII + six further EoSs)
   (α₁, α₂, c_ω) = (−10⁻⁴, −4×10⁻⁷, 10⁻³): s(Ω/M_*)
   curves; EoS universality better than 3%.
§§6–7 print **no further σ tuples**: §6's Bayesian
analysis evaluates the Tolman VII analytic σ
*continuously* over its prior box (uniform α₂ ∈
[−4×10⁻⁷, 4×10⁻⁷], uniform c_ω ∈ [−10⁵, 10⁵], Gaussian
α₁ about the lunar-laser-ranging value) for the
constraint figures (J1738 alone; the four-pulsar joint;
two J0348 projections; the joint-plus-triple analysis,
whose α₁ bound improves to −2.4×10⁻⁵ at 95%). §7
(conclusions) states the α₁ constraint at O(10⁻⁵) and
prints no σ values. **That is the whole enumeration.**

## 2. Item 2a — Conversion and the overlap control

Conversion (Gupta et al.'s §2 definitions, as verified in
gate32/work/g32_novelty.md): on the slice c_σ = 0,
c_a = c₁₄, c_ω = c₋ = 2c₁, c_θ = 3c₂, α₁ = −4c₁₄,
α₂ = c₁₄(c₁₄ + 2c₂c₁₄ − c₂)/[c₂(2 − c₁₄)] (OMW Eq. 3.21).
The deciding points convert to:

| Point | α₁ | α₂ | c_ω | c_θ |
|---|---|---|---|---|
| c_V = 2 maximiser | −2.54432×10⁻⁵ | −5.5943×10⁻¹⁰ | 5.0886×10⁻⁵ | 1.90860×10⁻⁵ |
| c_V = 10 maximiser | −3.18044×10⁻⁵ | −5.4292×10⁻⁹ | 1.59022×10⁻³ | 2.38863×10⁻⁵ |
| Corner B | −3.16×10⁻⁸ | −3.9500×10⁻⁹ | 0.16586208 | 2/7 |

**Controls — all PASS, run before any comparison was
quoted:**
- *Anchor reproduction:* the rung-2 anchor evaluated from
  the converted (α₁, α₂) reproduces G32-C's three values
  at relative differences 9.6×10⁻⁶, 3.0×10⁻⁶, 1.2×10⁻⁸ —
  the conversion lands on the values under test.
- *Overlap control (registered):* Gupta's Eq. (77) at
  Corner B's (α₁, α₂), with the programme's
  Ω/M_* = −(3/5)C_* convention, gives σ = 2.9546×10⁻⁹ —
  **exactly the khronometric value both records share**
  (Phase 292's σ at the same (c₁₄, c₂), Phase 303's
  Corner B anchor). The two records' leading orders are
  the same formula; the comparison below is therefore a
  comparison of the strong-field content, which is what
  a second path is for.
- *α₂ check:* the conversion's α₂ at Corner B,
  −3.9500×10⁻⁹, reproduces Phase 298's printed
  −3.95×10⁻⁹.

## 3. Item 2b — Evaluation at the deciding points

**Transcription integrity.** Eq. (80) was transcribed
from the LaTeX source and cross-checked against the
independently transcribed Ω-form, Eq. (82), through
their Eq. (81) 𝒞(Ω) relation: the two printed forms
agree at Corner B to 1.9×10⁻⁸ relative and at the
c_V = 10 maximiser to 2.1×10⁻³. At the c_V = 2 maximiser
they differ by 5.0×10⁻² relative — the two series'
truncation scales (O(𝒞⁴) vs O((Ω/M_*)⁴) plus the
conversion's own truncation) at 𝒞 = 0.17; both forms'
values at all three points lie inside the registered
bracket (the Ω-form's c_V = 2 ratio is 0.898), so the
verdict does not depend on which of Gupta's forms is
read as primary. The 𝒞-form is used for the verdict: it
is the form in the fence's own variable. Two source
defects were found and resolved on the record: (i) the
Ω-form's printed leading term (3α₁ + 2α₂)/3 is a sign
typo — only the (3α₁ − 2α₂)/3 reading matches Eq. (77)
identically and reproduces the 𝒞-form at Corner B
(the literal reading misses by 23.5% there); (ii) the
𝒞-form's source drops a "+" before its final
16α₁²α₂(…) summand — the summand reading is forced by
the Ω-form's parallel structure and by the Corner B
cross-form agreement (1.9×10⁻⁸, which the summand
reading achieves); numerically the ambiguity is in any
case bracket-immaterial (dropping the term moves
Corner B's ratio from 0.9206 to 0.9961, the maximisers
by ≤ 1.1×10⁻⁴ relative).

**Main evaluation** (Eq. (80) at 𝒞 = C_* = 0.17;
σ = s/(1 − s); terms in s):

| Point | 𝒞¹ term | 𝒞² term | 𝒞³ term | σ_Gupta | ratio |
|---|---|---|---|---|---|
| c_V = 2 max | 3.0895×10⁻⁶ | −9.8621×10⁻⁷ | +3.5064×10⁻⁷ | 2.4539×10⁻⁶ | 0.9456 |
| c_V = 10 max | 3.8615×10⁻⁶ | −1.2323×10⁻⁶ | +2.4203×10⁻⁷ | 2.8713×10⁻⁶ | 0.8852 |
| Corner B | 3.5174×10⁻⁹ | −8.4722×10⁻¹⁰ | +4.9829×10⁻¹¹ | 2.7200×10⁻⁹ | 0.9206 |

The structure is legible: Gupta's 𝒞¹ term is the anchor
times 25/21 (Tolman VII's Ω/M_* = −(5/7)𝒞 against the
programme's uniform-density −(3/5)𝒞 — the EoS convention
Phase 303 explicitly absorbed into f); the 𝒞² term then
removes ≈ 32% of the leading term and the 𝒞³ term
returns ≈ 6–11%. The near-cancellation of the EoS factor
by the strong-field terms is why the anchor + bracket
landed within 5–12% of the PM result at all three
points. Sanity: at Gupta's own Fig. 3 tuple the formula
gives s(0.17) = 9.1167×10⁻⁶ with the same term pattern.

**Supplementary (non-deciding):** across the fence's
compactness range, σ_Gupta/σ_anchor stays inside
[0.76, 1.01] at 𝒞 ∈ {0.11, 0.28} for all three points —
the agreement is not a C_* = 0.17 accident.

## 4. Coverage and method scope

**Coverage.** Gupta's results DO cover the deciding
points, through the closed form: Eq. (80) is a general
function on the slice, adopted by its authors for all
their constraint work, and every deciding point's
(α₂, c_ω) lies inside the domain their §6 analysis
actually exercised the same formula over. By region:
Corner B sits **inside their region (ii)**
(c_a = 7.9×10⁻⁹ ≲ 10⁻⁷; c_θ = 2/7 = 0.2857 ≲ 0.3;
c_ω free). The flat-row maximisers sit on the
region-(i) ray c_θ ≈ 3c_a (ratios 3.0006 and 3.0047)
but at c_a ≈ 6–8×10⁻⁶ — an order below region (i)'s
O(10⁻⁴) PPN saturation and above region (ii)'s 10⁻⁷
cap, i.e. between the two named regions, in the general
slice where the formula is defined; no printed σ curve
sits at their tuples (§1's enumeration), so their
evaluation is a formula evaluation, labelled as such —
not a read-off of a printed curve. The third verdict
form (DO NOT COVER) therefore does not fire.

**Method scope, stated where it binds.** Method 2 is a
post-Minkowskian expansion in 𝒞, here carried
analytically to O(𝒞³) for an analytic EoS; its
uncomputed remainder is O(𝒞⁴), and the two printed
forms' mutual spread at the deciding points (≤ 5%) is a
fair internal measure of that truncation — immaterial
against the ±30% bracket. The formula is not regular as
α₁ → 0 at fixed α₂ or c_ω → 0 at fixed (α₁, α₂) (the
authors' own note); no deciding point is at those
limits (Corner B, the extreme case, has α₂/α₁ = 0.125
and its two-form agreement is 1.9×10⁻⁸ — direct evidence
the evaluation is not in the singular regime there).
The APR4 Method-2 results (Fig. 2) are numerical and
print no evaluable formula; the Tolman VII form is the
only printed evaluable σ, and its authors' own
universality evidence (< 3% across seven EoSs) is the
stated basis for using it as the cross-check — an
EoS-representativeness assumption inherited from the
source, recorded here, not re-derived.

## 5. Verdict and its consequences

**AGREEMENT** — all deciding points inside
f ∈ [0.7, 1.3] (ratios 0.9456, 0.8852, 0.9206), robust
to which of Gupta's two printed forms is evaluated and
to the source's two typographical defects. **G32-C,
G32-E and G32-F are promoted to second-pathed grade by
independent method**, in Gate-32 §5's restated wording,
with this memo as the second path's record. G32-G's
distance-0 statement inherits the promotion through
G32-F, in its restated wording only.

Consequences, on the face:
- **Corner B (G32-E).** At σ_Gupta the literal corner's
  α̂₂ read is **−1.2300×10⁻⁹ — 23% over the 10⁻⁹
  bound** (rung-2 central read: −9.9540×10⁻¹⁰). This is
  not a MISS-branch re-decision: σ_Gupta is a
  bracket-interior value (f_eff = 0.9206), and G32-E as
  gated already states the corner's survival at the
  central model with the bracket span
  [−1.8818×10⁻⁹, −1.0902×10⁻¹⁰] on its face. What the
  second path adds is the measurement of the shrink the
  span implied: solving α̂₂(c₁₄) = −10⁻⁹ along
  c₂ = 2/21 at Corner B's c₁ with σ from Eq. (80) gives
  **c₁₄* = 6.4227×10⁻⁹** (factor 0.8130 of the literal
  corner), where σ_Gupta = 2.2113×10⁻⁹ and
  c_V = 3593.4 (c₁ fixed — the speed rises as the
  coupling shrinks). Corner B survives completed as a
  fence-saturating corner; its saturating coordinate is
  now second-pathed at 6.4227×10⁻⁹ rather than
  7.9×10⁻⁹. (The BBN saturation is a (c₁₄, c₂)-plane
  statement inherited from Phases 292/303 and is not
  re-decided here.)
- **The flat rows (G32-F).** The flat value's forcing is
  algebraic once the dipole leg binds (Gate-32 §3) and
  does not run through σ's value; σ_Gupta's effective
  factors at the maximisers (0.9456, 0.8852) sit far
  inside the bracket and far from the f = 0.7 regime
  where Phase 303's envelope shows the α̂₁ leg cutting
  the rows (to ≥ 1.01×10⁻⁵). A full fence re-run with
  σ_Gupta as a function of (c₁₄, c₂, c_ω) is not charged
  by the AGREEMENT branch and was not run; it is named
  here as the remaining refinement, non-deciding at the
  bracket's width.
- **What is not promoted:** nothing in this phase
  touches G32-A (structure — already gate-verified),
  G32-B (the failed framing — stays failed; Gupta et
  al. remain the reason), or G32-D (Corner A's
  σ-independent death — independent of any σ path by
  construction).

## 6. Reality Desk

`DESK: NO DATA CONTACT beyond the fences already applied
in Phases 291–303 — Phase 306 cross-checked the spin-1
record's sensitivity values against Gupta et al. (2021)'s
published post-Minkowskian computation; the contact is
bibliographic and methodological, not a new datum.`

## 7. What this is not

A cross-check of three sensitivity values by an
independent published method, at the points where those
values decide claims. It is not a re-run of the spin-1
fence, not a re-pricing of the channel, and not a
detectability statement of any kind. The claims it
promotes remain, in Gate-32 §5's wording, statements
about a signalling channel in a surviving theory corner
— not a drive, not transport, not a detection.
