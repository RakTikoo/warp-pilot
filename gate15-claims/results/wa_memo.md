# GATE-15 — W-A (CONTROLS) memo

Worker W-A, Gate-15 (independent re-computation). All code written from
scratch in `gate15/work_a/` (`wa_rtilde.py`, `wa_numeric2.py`,
`wa_bach2.py`, diagnostics `wa_bach_diag*.py`); no phase or gate code
was imported, copied, or run. Phase records were read only for the
registered definitions and stored control values. Run with the
programme venv `~/workspace/warp-pilot/venv/bin/python`; mpmath at
50 digits (deciding reads below quoted to 40+ digits), sympy 1.14.
Numbers: `results/wa_results.json`; checks: `results/wa_check.json`;
raw outputs: `results/wa_join_raw.json`, `results/wa_bach_raw.json`.
INTERNAL only. The (V-b) clause is not addressed here (not this
worker's item).

## 1. Definitions (derived, not copied)

Conformal 2-metric on Σ (Phase-61 BDE pattern, as tasked):
γ̃ = diag(−A/r², Bm/r²), built from the metric functions
g_tt = −A, g_rr = Bm. R̃ is the Ricci scalar of γ̃;
R̃_,n = (r/√Bm)·∂_r R̃; J_B = Bm; J_K = A′/(A√Bm);
jumps [X] = X_ext − X_int; shell Ŝ₀⁰ = −(4α₀/3)·[R̃_,n]
(α₀ = α_g/2, BDE eq. (57) mapping, per GATE9.md).

**My derivation.** In `wa_rtilde.py` I computed the Ricci scalar of a
general 2-metric diag(−P(r), Q(r)) from its Christoffel symbols:

  R̃ = (−2PQ·P″ + P·P′Q′ + Q·(P′)²) / (2P²Q²),   P = A/r², Q = Bm/r²

(closed-form residual vs the tensor computation: exactly 0).
Anchor: A = Bm = 1 gives R̃ = −2 exactly. This is the same closed
form Gate-9 W-B reported from its own derivation — obtained here
independently.

**Member.** r₀ = 1, p = 0.1, a = 0.27773424114865775 (full precision,
Gate-9 erratum 2), r_Σ = 1000. Interior (Morris–Thorne):
A_int = e^{2Φ₂}, Bm_int = 1/(1 − b/r), b = r^p,
Φ₂ = a·ln r/(1 + ln r). Exterior (Mannheim–Kazanas):
A_ext = f, Bm_ext = 1/f,
f = 1 − 3βγ − β(2−3βγ)/r + γr − kr², γ = 10⁻²⁸ (r₀ = 1 units).
All radial derivatives analytic (jets to third order; dR̃/dr by
symbolic partials of the jet expression contracted with the analytic
third derivatives — no finite differences).

**Darmois pair.** I solved J_B and J_K continuity at Σ myself
(mpmath findroot): β_MK = 2.1426107198525490, k = −2.2899591247362184×10⁻⁹
(stored: 2.142611, −2.28996×10⁻⁹; relative errors 1.3×10⁻⁷ / 3.8×10⁻⁷,
inside the Gate-9 bars of 1% / 2%; agreement with Gate-9 W-B's pair
to 2.7×10⁻¹⁷ in β). γ is carried as registered; it is numerically
inert here (the γ = 0 variant changes [R̃_,n] only in the 7th
significant digit, via the rounded pair's f-shift, and β_MK by
~10⁻²³ relative per Gate-9's record).

## 2. Join reads at Σ (ℓ = 0), exact Darmois pair

Interior at Σ:
- A_int = 1.6245404453016410432035995561794870374650716667115
- Bm_int = 1.0019992513458373797397666772554397452192998316681
- R̃_int = −1.9742886713617694518376954092792502194638276773929
- R̃_,n|_int = −0.010368518866140533073221935931268206421770277911899
- J_K|_int = 0.0000088739970855749125597340376848927153549195679955219

Exterior at Σ:
- A_ext = 0.99800473768503112039864754460326046444201372568459
- Bm_ext = 1.0019992513458373797397666772554397452192998316681
- R̃_ext = −1.9742886713617694120445324399866771154044570561446
- R̃_,n|_ext = −0.025685665408069936425393173510312329164963079906197

Jumps:
- [J_B] = 0.0 exactly, [J_K] = 0.0 exactly (by the Darmois solve;
  with W-B's pair: 1.5×10⁻⁴² / 1.6×10⁻¹⁹).
- **[R̃] = +3.9793162969292573×10⁻¹⁷** at the stored a — the zero is
  exact; the residual is the stored a's own precision (Gate-9 W-B
  found the identical 3.98×10⁻¹⁷ at this a, and −2.4×10⁻³⁹ at its own
  bisection a_zero). With the rounded stored (β, k) pair,
  [R̃] = +3.36×10⁻⁹, purely from the 6–7-digit rounding of β, k.
- **[R̃_,n]₀ = −0.015317146541929403352171237579044122743192801994298**
- **Ŝ₀⁰/α₀ = −(4/3)[R̃_,n] = +0.020422862055905871136228316772058830324257069325731**
  (sign exactly positive — legal shell). The rounded-pair variant
  gives [R̃_,n] = −0.01531714990439652, Ŝ₀⁰/α₀ = +0.02042286653919535:
  [R̃_,n] is insensitive to the pair's rounding (2×10⁻⁷ relative).

## 3. Comparison with the stored controls (face value)

Stored (Phase 90/91, carried into Phase 122): [R̃_,n]₀ = −0.0152185840,
Ŝ₀⁰ = +0.02029145 α₀ (Gate-9 claim text: +0.020291 α₀); control floor
3.4×10⁻⁹.

- [R̃_,n]: mine − stored = −9.8562541929403352×10⁻⁵; relative
  difference **0.6476%**. Inside Gate-9's registered 2% bar (so the
  G9-2 REPRODUCED verdict stands on my path too), but ~3×10⁴ times
  the control floor — not a digit-level agreement.
- Ŝ₀⁰/α₀: mine − stored (+0.02029145) = +1.314120559×10⁻⁴; relative
  **0.6476%**. Same statement.
- Cross-check between the two independent gate paths: Gate-9 W-B
  obtained [R̃_,n] = −0.01531714654192963717, Ŝ₀⁰/α₀ =
  +0.02042286205590618289. My values agree with W-B's to
  2.3×10⁻¹⁹ ([R̃_,n]) and 3.1×10⁻¹⁶ (Ŝ₀⁰/α₀) absolute. Two fresh
  derivations, built separately, land on the same number; both sit
  0.65% off the phase-stored control. Gate-9 already recorded this
  0.65% offset and passed it inside its 2% bar; nothing in Gate-9's
  verdict changes. What changes is only what may be claimed at
  digit level about the control's exact value (next section).

## 4. THE CONFRONTATION (explicit)

Phase 122's two-mouth shell-sign minimum is Ŝ⁰⁰/α₀ = **+0.0202914453**
at both mouths, stated in CHECKPOINT122.md to be "(the control
value)".

Digit by digit against the member's own shell density as
independently computed here:

    member (Gate-15 W-A):   0.020422862055905871…
    member (Gate-9 W-B):    0.020422862055906183…
    Phase-122 minimum:      0.0202914453
    stored control Ŝ₀⁰:     0.020291445333…   (= −(4/3)·(−0.0152185840))

- Phase-122's minimum and the member's own value share only the
  prefix **0.020**; they differ at the **4th decimal place**
  (0.0204… vs 0.0202…). Absolute difference:
  **+1.3141675590587×10⁻⁴** (member higher); relative **0.6476%**.
- Phase-122's minimum equals the **stored Phase-90/91 control
  number** to 3.3×10⁻¹¹ — i.e. to every digit Phase 122 prints, it
  is the control's rounding.
- **Conclusion: the two-mouth minimum does NOT equal the member's
  own shell density.** It equals the inherited stored control value.
  If the solved perturbation's [R̃_,n] mode sum vanishes at its
  minimum point (so the minimum is the unperturbed member's shell),
  that minimum should sit at **+0.0204228620559**, not at
  +0.0202914453. The 0.65% gap is exactly the Gate-9-recorded offset
  between the phase-stored control and the member as independently
  recomputed, propagated into Phase 122's "control value" language.
  This is a statement about which number the minimum equals; the
  shell's sign and legality (Ŝ₀⁰ > 0) hold on every path, and no
  Gate-9 bar is breached.

## 5. Bach-flatness control (Task 4)

Registered convention (Gate-9 erratum 3): B = 2∇∇C + R·C, i.e.
B_μν = 2∇^α∇^β C_{αμβν} + R^{αβ}C_{αμβν} — twice the
∇∇C + ½R·C bracket. My `wa_bach2.py` builds the full tensor route
(Christoffel → Riemann → Ricci → Weyl → double covariant divergence)
in sympy for diag(−F, 1/F, r², r²sin²θ) with F an undefined function
(derivatives kept atomic), then substitutes the MK jet
(β = 2.142611, γ = 10⁻²⁸, k = −2.28996×10⁻⁹ as exact rationals) per
radius. Max |B_diag| over components, at θ = 0.7 and 1.1:

- r = 2: 2.07×10⁻²⁵
- r = 10: 6.57×10⁻²⁵
- r = 100: 3.28×10⁻²⁵
- r = 1000 (= Σ): 3.28×10⁻²⁵

**B_μν = 0 on the MK exterior** at the 25-digit evaluation floor of
exact rational expressions. Machinery anatomy (recorded, Gate-7/8
style): my first assembly skipped ∇C components whose Weyl component
vanishes identically — the covariant derivative of a vanishing
component is not zero (connection terms), and the engine duly failed
its Schwarzschild diagnostic (Y_rtt = 3/6250 ≠ 0 pinpointed the
missing θ/φ connection terms). The skip was removed everywhere
(∇C and ∇Y); the fixed engine gives the residuals above. (Gate-9
W-A's record notes the same machinery lesson independently.)

Interior join-data consistency: GATE9.md records no separate numeric
[B]/[K] jump values at Σ = 1000 — it records the Darmois pair
(β_MK, k) that defines them to vanish. Against that definition my
interior data are consistent: [J_B] = [J_K] = 0.0 exactly with my
solved pair (§2), and my pair reproduces the stored pair inside the
Gate-9 bars (C2 in `wa_check.json`).

## 6. Check summary

`wa_check.json`: C1 (R̃ derivation + flat anchor) PASS; C2 (Darmois
pair vs stored, Gate-9 bars) PASS; C3 ([R̃] zero, a-precision caveat
stated) PASS; C4/C5 ([R̃_,n], Ŝ₀⁰ vs control at the Gate-9 2% bar)
PASS; **C6 (digit-equality with the stored control) FAIL**;
**C7 (confrontation: Phase-122 minimum vs member's own density)
FAIL — the minimum is the stored control number, not the member's
density**; C8 (Bach-flatness) PASS; C9 (interior join consistency)
PASS. Tolerances and their justification are stated in
`wa_check.json`.
