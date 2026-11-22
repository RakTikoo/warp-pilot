# Gate-3 summary — novelty & verification verdicts for the MRV audit claims

Gate-3 applied the programme's two-part standard to the Phase 4
audit of Mironov–Rubakov–Volkova (arXiv:1811.05832 /
arXiv:1812.07022): a claim is upload-ready only if (a) its novelty
is documented against the literature (searches logged, near
neighbours read in full) and (b) its correctness is reproduced by
an independent computation path sharing no deciding machinery with
the original. Six workers: three novelty (N1–N3), three
verification (V1–V3). Full record: `gate3/GATE3.md` (internal).

**Update (2026-11-22).** The gate's two open items have landed.
The G3-1 certification follow-up (branch-independent action-level
congruence reduction) certifies the ghost signs, and the G3-4
dense-profile settlement resolves the ℓ=0 mode question against
the mode. G3-1 and G3-4 are now **UPLOAD-READY**, and the ghost
instance joins G3-5's pattern. This summary reflects both
conversions; the v1.6.x version of this file recorded the earlier
state (G3-1 held, G3-4 restated).

## Verdicts per claim

| Claim | Novelty | Correctness | Gate verdict |
|---|---|---|---|
| G3-1 Even-sector ghost at ℓ≥2 | NOVEL (all components) | REPRODUCED (branch-independent action-level certification, 2026-11-22) | **UPLOAD-READY** |
| G3-2 Printed defects (a₂^BH; e₁ J′² pair) | NOVEL (both defects) | REPRODUCED | **UPLOAD-READY** |
| G3-3 Trajectory incompleteness | PARTIALLY KNOWN | REPRODUCED (on-background half; off-trajectory half is a documented full-text fact) | **UPLOAD-READY** |
| G3-4 Balance (tachyon pass; ℓ=0 health) | ℓ=0 component NOVEL; tachyon pass is a balance item | Odd sector REPRODUCED; ℓ=0 health REPRODUCED; ℓ=0 mode SETTLED by dense profiles (2026-11-22) | **UPLOAD-READY** |
| G3-5 Pattern (printed criteria as hiding place) | PARTIALLY KNOWN (instances in print; general statement and audit-as-object NOVEL) | Inherits its instances' | **UPLOAD-READY AFTER RESTATEMENT** |

The published bundle (`AUDIT.md`, v1.7.0) contains all five
claims: G3-1 (certified), G3-2, G3-3, G3-4 (with the ℓ=0
settlement and the retraction of the +0.00021 value), and G3-5
(restated, now including the ghost instance). In v1.6.x G3-1
appeared only as a single paragraph labelled as the programme's
uncertified result; that placeholder is replaced by the full
claim in §6 of the note.

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

**G3-4, ℓ=0 mode — SETTLED (2026-11-22, dense profiles):** the
missing piece named by the gate (dense corrected (𝒦₀, 𝒢₀, ℳ₀)
profiles from the from-action route; 2,499 radii on [−62, 62],
`gate3/results/g3_ell0_dense_profiles.json`) was produced, and it
settles the question against the mode. The reduced coefficients
are parametrisation-singular at the D = 0 pole r* =
1.772437990426927; the first version's flux-form solve bridged
that pole, and a trial function constant across it has a discrete
𝒦₀-norm diverging like 1/h, driving its Rayleigh quotient
spuriously to ~0 — under refinement and grid offset the bridging
solve's lowest eigenvalue does not converge ((0.01, 0): +0.00020997;
(0.005, h/2): −1.29e-6; (0.0025, 0): +2.7e-7). The +0.00021
throat-localised mode is therefore **retracted** as a
discretisation artefact (pole-bridging). The well-posed problem
(pole excised; the Liouville form has a +2/(ρ−ρ*)² repulsive core
at the pole, above the 3/4 limit-point threshold, so the sides
decouple) has throat-segment ground state ω² = **+0.00445402** by
two routes in agreement (formula route at every δ ∈ [0.01, 0.35],
both h; dense-profile route +0.00445398 / +0.00445406). No route
finds any eigenvalue below the box continuum. Certified
statement: "no ℓ=0 tachyon is found by any route (three
independent eigensolvers agree the lowest ω² is positive); the
ℓ=0 spectrum in the box begins at the positive continuum value
ω² ≈ +0.0045; the D=0 pole at r* = 1.7724 is a parametrisation
singularity of the reduced variable, across which the physical
(Liouville) problem decouples."

**G3-3, on-background half (worker V3):** ℱ, 𝒢 recomputed fresh
from the designer functions on log grids to |r| = 10⁴, both signs:
max |c_T − 1| = 2.2×10⁻¹⁶ per side, max |𝒢 − 1| = 4.4×10⁻¹⁶ —
the same roundoff-floor class as the audit's own 7.8×10⁻¹⁶.

**G3-1 — CERTIFIED (2026-11-22, certification follow-up;
`gate3/v_g3_1_cert.py`, `gate3/results/v_g3_1_cert.json`):**
worker V1's third route had reproduced the claimed signs on its
distinguished regular elimination branch but proved
equation-of-motion row elimination is branch-dependent in sign in
general, leaving the branch-independent action-level
certification as the named missing piece. The follow-up lands it
by the stronger of the named routes: the auxiliary field b is
eliminated by a block Schur complement of the action/EOM symbol
(exact rational arithmetic), and the physical kinetic matrix is
the symmetric part of the (iω)² coefficient restricted to the
Hamiltonian-constraint surface — a congruence, performing no EOM
row operation at any step. Result (this route's normalisation;
signs are the content): det 𝒦_phys = +137.96 (r = −20), −67.26
(r = −5), −17.20 (r = +5), +127.28 (r = +20) — signs
(+, −, −, +), the claim. Branch-independence is demonstrated:
all three solved-field parametrisations of the constraint surface
give the same sign at every radius (decisively at r = −20, where
the EOM elim-c branch had flipped to −338.26, the action-level
c-parametrisation gives +185.01); 18/18 random congruences leave
every sign invariant; the bordered-determinant identity holds to
≤ 1.5e-15; FD-step variation leaves every sign invariant. The
GR + canonical-scalar control is positive definite at r = ±5
(det +7661.64; eigenvalues +69.99, +109.46) on the same substrate
where V1's row elimination gave +6717.02 / −6817.65 by branch.
The certification also resolves the Phase 4 routes' r = −20
disagreement in favour of the jet extraction's positive sign, by
a route sharing no deciding formulas with either. Scope:
branch-independence is demonstrated within the Regge–Wheeler-gauge
presentation all routes used; the reduction performs no EOM row
operation, which is exactly the gap V1 named.

## Wording conditions (binding on the publication)

1. **Mandatory credit, in substance, leading the note:** the
   construction's background is a genuine solution of the stated
   theory (all four background equations close), the odd sector
   is healthy and complete, and the beyond-Horndeski γ-crossing
   formalism is untouched by every finding. Register throughout:
   a methods/audit note, non-polemical — "inconsistent with the
   action as printed", never characterisations of the authors.
2. **G3-1** is stated under its pre-registered conditions:
   signs only (magnitudes are presentation-dependent and are
   never compared across routes); r = 0 stated as degenerate,
   carrying no sign in any presentation; the band "bracketed by
   settled points at |r| = 5 (negative) and |r| = 20 (positive)",
   not a mapped interval; the mandatory credit sentence (item 1)
   included; non-polemical register throughout.
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
5. **G3-4** carries the settled ℓ=0 statement verbatim in
   substance: "no ℓ=0 tachyon is found by any route (three
   independent eigensolvers agree the lowest ω² is positive);
   the ℓ=0 spectrum in the box begins at the positive continuum
   value ω² ≈ +0.0045; the D=0 pole at r* = 1.7724 is a
   parametrisation singularity of the reduced variable, across
   which the physical (Liouville) problem decouples." The
   v1.6.x soft-mode sentence is deleted, and the retracted
   +0.00021 value is identified in the note as a discretisation
   artefact (pole-bridging at r* = 1.772437990426927), with the
   settled throat-segment ground state +0.00445402 stated.
6. **G3-5** is stated over the gate-certified instances
   (a₂^BH; the e₁ J′² pair; the programme's own Eᵢ error; and,
   since the 2026-11-22 certification, the det 𝒦 factorisation /
   ghost instance), with the general form presented as the
   programme's stated lesson / hypothesis from this audit.

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
