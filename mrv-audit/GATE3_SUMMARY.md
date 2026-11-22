# Gate-3 summary — novelty & verification verdicts for the MRV audit claims

Gate-3 applied the programme's two-part standard to the Phase 4
audit of Mironov–Rubakov–Volkova (arXiv:1811.05832 /
arXiv:1812.07022): a claim is upload-ready only if (a) its novelty
is documented against the literature (searches logged, near
neighbours read in full) and (b) its correctness is reproduced by
an independent computation path sharing no deciding machinery with
the original. Six workers: three novelty (N1–N3), three
verification (V1–V3). Full record: `gate3/GATE3.md` (internal).

## Verdicts per claim

| Claim | Novelty | Correctness | Gate verdict |
|---|---|---|---|
| G3-1 Even-sector ghost at ℓ≥2 | NOVEL (all components) | NOT YET | **NOT YET — held** |
| G3-2 Printed defects (a₂^BH; e₁ J′² pair) | NOVEL (both defects) | REPRODUCED | **UPLOAD-READY** |
| G3-3 Trajectory incompleteness | PARTIALLY KNOWN | REPRODUCED (on-background half; off-trajectory half is a documented full-text fact) | **UPLOAD-READY** |
| G3-4 Balance (tachyon pass; ℓ=0 health) | ℓ=0 component NOVEL; tachyon pass is a balance item | Odd sector REPRODUCED; ℓ=0 health REPRODUCED; ℓ=0 mode value NOT YET | **UPLOAD-READY AFTER RESTATEMENT** |
| G3-5 Pattern (printed criteria as hiding place) | PARTIALLY KNOWN (instances in print; general statement and audit-as-object NOVEL) | Inherits its instances' | **UPLOAD-READY AFTER RESTATEMENT** |

The published bundle (`AUDIT.md`) contains G3-2, G3-3, G3-4
(restated) and G3-5 (restated). G3-1 is held: it appears only as a
single paragraph labelled as the programme's uncertified result.

## Reproduction numbers (deciding values)

**G3-2 (worker V2, independent route — exponential lapse/shift
areal ansatz, own jet-Hessian machinery; `gate3/v_g3_2.py`):**
- J′² pair: sympy applied to the printed e₁ gives the pair's
  on-background sum = (J′² − J′³)/X, exactly 0 at J′ = 1. Removing
  the pair restores 𝒦₀ > 0 on the whole [−60, 60] grid (printed
  𝒦₀ is negative on the negative side, e.g. −34.91 at r = −40);
  𝒦₀(corrected)/J² at |r| = 100/200/400 = 0.019406 / 0.019850 /
  0.019963 at both signs → +2/τ² (Appendix B normalisation).
- a₂^BH: at r = 5 the identity b₃ = 2(a₁′ − a₂^H) holds to
  ≤ 3.6×10⁻¹⁵ (a₂^H = −3.18040, matching the from-action value)
  and fails with the printed a₂ = −4.38759 by exactly −4π′³F₄
  (residual −2.4143829503861225 vs −4π′³F₄ = −2.4143829503861225,
  all printed digits).

**G3-4, ℓ=0 health (worker V2):** 𝒦₀ > 0 at every sampled radius;
spot values match the Phase 4 from-action derivation (F4-2b) to
≤ 0.5% (r = −60: 34.16 vs 34.00; −40: 14.10 vs 14.07; −20: 3.093
vs 3.09; −15: 2.500 vs 2.50; −12.5: 2.673 vs 2.67); 𝒦₀/J² at
|r| = 100/200/400 = 0.009745 / 0.009966 / 0.010023, identical at
both signs → +1/τ² at both infinities (covariant normalisation).

**G3-4, odd sector / tachyon pass (worker V3; `gate3/v_g3_3.py`):**
effective potential rebuilt independently (closed-form check
against −4τ²/J⁴: max deviation 1.4×10⁻¹⁷); V_eff > 0 for
ℓ = 2, 3, 5, 10; ℓ=2 minimum 0.0015924 (Phase 3/4 value 0.00159);
own eigensolver's ℓ=2 lowest ω² = +0.0082544 on both grids (the
box-continuum value +0.008254).

**G3-4, ℓ=0 mode value — NOT YET:** the gate's FEM eigensolver
finds no negative eigenvalue under any interpolation of the
coefficient data (PCHIP, cubic spline, Akima), so the tachyon
pass's deciding content stands with three eigensolvers in
agreement; but the claimed +0.00021 throat-localised mode does not
appear in the gate's solve (its lowest mode is the +0.00447
box-continuum mode, coincident with Phase 4's second eigenvalue
+0.00445). The claimed mode's binding energy (~5×10⁻⁵ below the
continuum threshold ℳ₀/𝒦₀ → 2.61×10⁻⁴) is below the interpolation
uncertainty of the 31-radius coefficient data. Missing piece:
dense corrected (𝒦₀, 𝒢₀, ℳ₀) profiles from the from-action route.

**G3-3, on-background half (worker V3):** ℱ, 𝒢 recomputed fresh
from the designer functions on log grids to |r| = 10⁴, both signs:
max |c_T − 1| = 2.2×10⁻¹⁶ per side, max |𝒢 − 1| = 4.4×10⁻¹⁶ —
the same roundoff-floor class as the audit's own 7.8×10⁻¹⁶.

**G3-1 — why NOT YET (worker V1):** a third route (Regge–Wheeler
gauge, exact sympy ε-series, equation-of-motion elimination;
shares no formulas with either Phase 4 route) reproduces the
claimed signs at all four settled points on its distinguished
regular elimination branch, and independently re-finds Phase 4's
antisymmetric Wronskian remnant. However, V1 proved that
equation-of-motion row elimination is branch-dependent in sign in
general (an exact identity relates the branches, and a
GR + canonical-scalar control flips sign between them), and the
branch-independent, action-level congruence certification was not
completed — the Wronskian sector's skew odd-dimensional block
makes the naive Schur complement structurally singular. Named
missing piece: an extended canonicalisation handling jets to
(2,2) after the auxiliary-field substitution, or a gauge in which
the auxiliary fields are algebraic from the start. This is
explicitly not a FAILS: no branch-independent computation
disagrees with the claim, and the gate record notes the caveat
does not by itself impeach Phase 4's two routes (one an
action-level canonical reduction, variationally tested; the other
tracking its auxiliary determinant explicitly).

## Wording conditions (binding on the publication)

1. **Mandatory credit, in substance, leading the note:** the
   construction's background is a genuine solution of the stated
   theory (all four background equations close), the odd sector
   is healthy and complete, and the beyond-Horndeski γ-crossing
   formalism is untouched by every finding. Register throughout:
   a methods/audit note, non-polemical — "inconsistent with the
   action as printed", never characterisations of the authors.
2. **G3-1** appears only as: the programme's two independent
   computations find the even sector ghostly at ℓ≥2 near the
   throat, a third branch-independent certification in progress —
   labelled uncertified. (Pre-registered for an eventual certified
   upload: signs only, magnitudes being presentation-dependent;
   r = 0 stated as degenerate, carrying no sign; the band
   "bracketed by settled points at |r| = 5 (negative) and
   |r| = 20 (positive)", not a mapped interval.)
3. **G3-2** carries: the on-background caveat (the derivation
   fixes the pair's on-background value, zero; a correct general
   form could differ by factors vanishing on this background);
   the disclosure, wherever the defect list appears, that the one
   background-equation error found was the programme's own (the
   E_J 1/J transcription) and the paper's printed E_J is correct;
   the sequel-republication fact (arXiv:2212.05969, eq. (98) and
   eq. (121)) as a neutral bibliographic statement only.
4. **G3-3** is scoped "from the published construction" (not "the
   theory cannot predict"); the authors' own asymptotic caveats
   are credited in the same paragraph; on-background GR-ness is
   stated with its numbers so the claim cannot be read as an
   observational exclusion. Label: (ii) NOT EXCLUDED BUT
   INCOMPLETE.
5. **G3-4** carries the restated ℓ=0-mode sentence verbatim in
   substance: "no ℓ=0 tachyon is found by any route (three
   independent eigensolvers agree the lowest ω² is positive); the
   programme's dense flux-form solve finds in addition a soft
   throat-localised near-zero mode at ω² ≈ +2×10⁻⁴, whose precise
   value is at the resolution limit of the available coefficient
   data and is reported as the programme's own result, not as
   gate-reproduced."
6. **G3-5** is stated only over the gate-certified instances
   (a₂^BH; the e₁ J′² pair; the programme's own E_J error), with
   the general form presented as the programme's stated lesson /
   hypothesis from this audit. The ghost/factorisation instance
   joins the pattern only when G3-1 certifies.

## Citing-list check (the gate's named strengthening, run 2026-11-21)

Gate-3's novelty workers could not pull the full citing lists
directly; this check closes that caveat before publication.

**Method.** INSPIRE-HEP API: record lookup for arXiv:1812.07022
(citation_count 36; CQG 36 (2019) 135008) and arXiv:1811.05832
(citation_count 12), then the full citing lists via the INSPIRE
`refersto recid` literature query (36 records returned for
1812.07022). Semantic Scholar Graph API: full citation lists for
both papers (32 citing papers for 1812.07022; 10 for 1811.05832).
Titles and, for every stability-adjacent entry, abstracts were
scanned for: a stability re-analysis of the 2019 example, an
erratum or comment, any evaluation of the even-parity sector or
of det 𝒦 for this example, and any documentation of the
Appendix B coefficients.

**Outcome: no anticipating source found for any certified claim.**
No citing paper re-analyses the stability of the 2019 example, no
erratum or comment on either version exists in either list, and
none evaluates the even sector or Appendix B of the example. The
stability-related citing works are all general-formalism or
different-system papers, consistent with the gate's searches:
the authors' own sequels (arXiv:2212.05969, which builds a new
example and republishes the coefficients unchanged;
arXiv:2404.06297, general stability conditions for arbitrary
static spherically symmetric backgrounds, which does not evaluate
the 2019 example); Franciolini et al. (arXiv:1811.05481,
model-independent framing); general criteria papers
(arXiv:2306.17791; arXiv:2408.01480; arXiv:2411.05416;
arXiv:2610.28592); and wormhole constructions in other theories.
The future-dated ID flagged by worker N3 re-verifies: arXiv:
2610.28592 (Kiselev et al., "Monopole stability of time-dependent,
spherically symmetric backgrounds in Horndeski theory") exists in
both databases; it is Horndeski-only, concerns time-dependent
backgrounds, and does not evaluate the MRV example — it does not
anticipate any certified claim.

**Effect.** No claim was stopped. The novelty verdicts in the
table above now rest on the full citing lists, not only on
topical-query sampling.
