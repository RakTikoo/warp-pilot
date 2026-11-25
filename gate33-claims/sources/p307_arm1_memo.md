# PHASE 307 — ARM 1 MEMO: THE TOLERANCE ITSELF (red team)

Scope (registered, `p307_registration.md`): the flat value
G32-F, HT 2.8044×10⁻⁵, whose binding leg L9 is
⟨𝒜⟩_dip ≤ 0.1 for the J1738-class NS–WD system, the limit
being YBBY Eq. (190)'s O(10%) tolerance.
Sources retrieved 2026-11-24 at primary-source grade:
Freire et al. 2012, MNRAS 423, 3328 (arXiv:1205.1450, ar5iv
full text, incl. Table 1 and §§3.2–3.4, 4); YBBY, PRD 89,
084067 (2014) (arXiv:1311.7144v4, ar5iv + PDF full text,
§§VII A–C, Eqs. 188–195, Fig. 7 caption); Vaglio et al.
2026, PRD 114, 104021 (arXiv:2605.01436, PDF full text) as
the later timing update. All arithmetic below was run with
the programme venv python; the Phase 303 machinery was
re-derived inline from `p303_pricing.py`'s own formulas
(not imported blindly) and the Gate-32 §3 skeleton was
verified against them (§4 below).

## 1. What YBBY Eq. (190) actually bounds

YBBY §VII A, Eqs. (188)–(190) (verbatim structure):

- Eq. (188): the observed decay agrees with GR up to two
  fractional errors,
  (Ṗ_b/P_b)_obs = (Ṗ_b/P_b)_GR (1 ± δ_obs ± δ_inf),
  where δ_obs is the observational uncertainty in Ṗ_b and
  δ_inf is the error induced in the *predicted* Ṗ_b/P_b by
  the uncertainties in the inferred individual masses.
- Eq. (189): the Lorentz-violating prediction is
  (Ṗ_b/P_b)_Æ,kh = (Ṗ_b/P_b)_GR (1 + δṖ_Æ,kh), with
  δṖ_Æ,kh the **total fractional deviation** of the theory's
  orbital decay from GR — i.e. in the language of YBBY
  Eq. (193), δṖ = ⟨𝒜⟩ − 1, the dipole piece **plus** the
  quadrupole deviation, not the dipole piece alone.
- Eq. (190): the "most conservative constraint" is
  |δṖ_Æ,kh| ≤ δ_obs + δ_inf = O(10%).

Three facts about this tolerance that the fence's L9 does
not carry on its face:

1. **It is a generic, cross-system order-of-magnitude
   statement, not a J1738 number.** YBBY give no per-system
   δ_obs or δ_inf anywhere in §VII A; "O(10%)" is asserted
   for the binary-pulsar sample as a whole. For J1738
   specifically the ingredients are larger than 10%:
   δ_obs ≈ 3.2/25.9 = 12.4% on Ṗ_b^Int (18.2% on the raw
   Ṗ_b^obs = −17.0 ± 3.1), and δ_inf ≈ 1.7/27.7 = 6.1%
   from the GR prediction's mass-driven error (§2). The
   linear sum YBBY's Eq. (190) prescribes is ≈ 18–24% for
   this system, not 10%.
2. **YBBY do not apply it to J1738's Ṗ_b at all.** §VII C.1:
   "We do not consider constraints derived from the orbital
   decay rate of PSR J1738+0333 [61] … because they are
   weaker than constraints derived with the systems
   described above." The Ṗ_b bands of Fig. 7 come from
   J1141−6545, J0348+0432 and J0737−3039; J1738 enters
   YBBY only through the conservative α̂₁/α̂₂ mapping
   (Eqs. 194–195). The fence's "J1738-class system with
   Eq. (190)'s 0.1" is the programme's own construction
   (Phase 303 §2, registered there), not a bound YBBY drew
   for this system.
3. **YBBY themselves do not use Eq. (190) as the operative
   constraint.** The sentence after it replaces it with
   Eq. (191) — δṖ evaluated while varying masses, P_b,
   α₁/α₂ within Solar-System ranges and sensitivities over
   EoSs — which is what produces the Fig. 7 bands (Arm 2).
   Eq. (190) is the paper's back-of-envelope summary of
   that procedure, at the confidence of a **linear sum of
   1σ-class errors**: that is the tolerance's implicit
   confidence, and it is *not* the 95% convention of the
   fence's other pulsar legs (L7/L8, Shao–Wex 95%).

## 2. The J1738 data at primary grade (Freire et al. 2012)

All values 1σ, from Freire et al. Table 1 and §§3.2–3.3:

- P_b = 0.3547907398724(13) d = 8.5 h (the fence's
  P_b = 8.5 h, m = 1.6 M☉ class; actual total mass
  M_t = 1.65^{+0.07}_{−0.06} M☉, M_p = 1.46^{+0.06}_{−0.05},
  M_c = 0.181^{+0.008}_{−0.007}).
- Ṗ_b^obs (apparent) = (−17.0 ± 3.1) × 10⁻¹⁵ s s⁻¹.
- Kinematic corrections (§3.2, Eqs. 1–4): Shklovskii
  Ṗ_b^Shk = 8.2^{+0.6}_{−0.5} fs s⁻¹ (text Eq. 4: 8.3);
  Galactic acceleration Ṗ_b^Gal = 0.58^{+0.16}_{−0.14}
  fs s⁻¹. (Note the signs: Ṗ_b^Int = Ṗ_b^obs − Ṗ_b^Acc −
  Ṗ_b^Shk; both corrections are positive, so the intrinsic
  decay is *faster* than the apparent one.)
- **Ṗ_b^Int = (−25.9 ± 3.2) × 10⁻¹⁵ s s⁻¹** (Eq. 5;
  Monte-Carlo uncertainties, §3.4).
- **Ṗ_b^GR = −27.7^{+1.5}_{−1.9} × 10⁻¹⁵ s s⁻¹** (Eq. 6,
  from the optically measured q and m_c).
- Excess: **Ṗ_b^xs = Ṗ_b^Int − Ṗ_b^GR =
  +2.0^{+3.7}_{−3.6} fs s⁻¹** (Eq. 7) — the measured decay
  is *slower* than GR's prediction at central values.
- Ratio: R ≡ Ṗ_b^Int/Ṗ_b^GR = 25.9/27.7 = **0.9350**,
  i.e. R − 1 = **−0.0650**. The published ratio in the
  secondary literature quoting Freire et al. is
  0.94 ± 0.13. The relative uncertainty follows from the
  excess: σ_rel = σ_xs/|Ṗ_b^GR| = 3.65/27.7 = **0.132**
  (quadrature of the Ṗ_b^Int and Ṗ_b^GR errors with the
  symmetrised GR error 1.7 gives 0.138; the three routes
  agree at σ_rel ≈ 0.13–0.14). Corroboration that Freire
  et al. quote their dipole limit at 1σ: their generic
  dipole parameter for this system is
  κ_D = (−0.8 ± 1.6) × 10⁻⁴ (their Eq. 14, 1σ).

**Later update (Vaglio et al. 2026, EPTA DR2 + NANOGrav
9-yr + five-telescope ToAs, Bayesian/Vela):** measured
Ṗ_b = (−1.82 ± 0.25) × 10⁻¹⁴ (Bayesian; linear fit
−1.61 ± 0.14), corrections Ṗ_b^Gal = (−3.0 ± 0.3) ×
10⁻¹⁶ (sign reversed vs Freire et al. under the
MWPotential2014/galpy model, their App. B) and
Ṗ_b^Shk = (9.3 ± 0.6) × 10⁻¹⁵, giving, by their Eq. (64)
subtraction, Ṗ_b^corr ≈ −27.2 ± 2.6 fs s⁻¹ — closer to
GR at central value, with σ_obs improved only from 3.1
to 2.5 fs s⁻¹. Vaglio et al.'s own GR prediction under
their sampled masses is not stated in a form this arm
could extract cleanly from the PDF text layer, so the
update is used only indicatively in §3, not as the
deciding input. Indicatively: with Ṗ_b^GR = −27.7
carried over, R ≈ 0.982, σ_rel ≈ 0.113, and the 1σ cap
of §3 becomes ≈ 0.095 — still below 0.1. The update does
not rescue the 0.1 figure at 1σ; it moves it from
clearly-below to marginally-below.

## 3. The data-grade cap on the dipole piece

Registered formula (registration, Arm 1):
⟨𝒜⟩_dip ≤ (R − 1) + n·σ_rel, applied in the fence's
registered decomposition: Eq. (190)'s tolerance is on the
**total** ⟨𝒜⟩ − 1; the fence applies it to the dipole
piece with the quadrupole deviation bounded separately
at ≤ 2.62×10⁻⁵ at the deciding corner (Phase 303 §2).
That bound is 3–4 orders below every cap in the table, so
the total-vs-piece distinction changes no digit quoted
here: cap_dip = cap_total − (quad deviation) with
|quad deviation| ≤ 2.62×10⁻⁵. The dipole piece is
non-negative by construction (𝒞 > 0, (s₁−s₂)² ≥ 0), so a
negative central R − 1 eats directly into the cap — this
is the term the fence's flat 0.1 silently discards.

| Confidence | n | Cap on ⟨𝒜⟩_dip | Data-grade flat HT | NS–BH |
|---|---|---|---|---|
| Implicit (Eq. 190: linear sum of 1σ errors) | 1 | **0.067** (0.070 from published 0.94 ± 0.13) | **1.87×10⁻⁵** (1.96×10⁻⁵) | 1.70×10⁻² |
| 95% CL, one-sided | 1.645 | 0.152 | 4.26×10⁻⁵ | 3.85×10⁻² |
| 95% CL, two-sided | 1.96 | 0.193 | 5.42×10⁻⁵ | 4.91×10⁻² |

Equivalently: the fence's 0.1 sits at
n = (0.1 + 0.065)/0.132 = **1.25σ** above the measured
central ratio — roughly a 79% one-sided confidence level.
It is neither the tolerance's own implicit (≈1σ) level
nor the 95% level of legs L7/L8. It is an unattributed
intermediate number.

## 4. Recomputation of the flat value

Scaling verified, not assumed. Gate-32 §3's skeleton,
recomputed from `p303_pricing.py`'s own formulas
(Xfac, Peters g/F, HT compactnesses at R = 12 km):
maximised HT ratio = cap × (ΔC_*/0.17)² × (X_HT/X_J1738)
× (g/F), with X_J1738 = 7.255031×10⁵ (recomputed
7.25503×10⁵), X_HT = 4.66427×10⁵, ΔC_* = 0.006153,
g/F = 0.33300. At cap = 0.1 this gives 2.80438×10⁻⁵ vs
the stored 2.8044×10⁻⁵ (rel. diff 2×10⁻⁵, the stored
value's rounding) — the skeleton and the script agree,
and the maximised ratio is exactly linear in the cap
once L9 binds. Independent check at the data-grade cap:
a coarse re-maximisation over the full completed fence
(all legs L1–L9 as in `p303_pricing.py`, cap = 0.0668,
c₁ = c*²c₁₄) reaches HT 1.83×10⁻⁵ (c* = 2) and
1.86×10⁻⁵ (c* = 10) on a coarse grid, approaching the
algebraic 1.873×10⁻⁵ from below with L9 binding
(⟨𝒜⟩_dip = 0.0653 / 0.0664 at the grid maximisers) and
L7/L8 passing — so the lower value is attainable inside
the unchanged fence, not an artefact of the skeleton.

**Data-grade flat value (implicit confidence):
HT 1.87×10⁻⁵, NS–BH 1.70×10⁻²** — a factor 0.67 of the
claimed 2.8044×10⁻⁵ / 2.5394×10⁻².

## 5. Verdict — ARM 1: BREAKS (scope: the flat value)

At the confidence level YBBY Eq. (190)'s tolerance
implicitly uses — a linear sum of 1σ-class observational
and inferred-mass errors, with no central-offset term —
the J1738 data support a dipole cap of **0.067**, not
0.1, because the system's measured decay is 6.5% *slower*
than GR at central values (R = 0.935, excess
+2.0 ± 3.65 fs s⁻¹) and the fence's 0.1 spends that
offset as if it were headroom. Replacing L9 by the
data-grade cap, all other legs unchanged, the flat value
falls to **HT 1.87×10⁻⁵ < 2.8044×10⁻⁵**. G32-F's number,
as stated, does not survive its own leg's data at its
own leg's confidence.

Stated on the face of the break, because the parent must
weigh it: at a uniform 95% CL — the convention of the
fence's L7/L8 — the data-grade cap is 0.19 and the flat
value would *rise* to 5.4×10⁻⁵, i.e. 2.8044×10⁻⁵ would
be conservative. The break is therefore precisely a
**confidence-level break**: 0.1 is defensible at no
single stated confidence for this system (1σ ⇒ 0.067;
95% ⇒ 0.19; 0.1 itself ⇒ ≈1.25σ), and YBBY's text
supplies two further qualifications the fence dropped —
Eq. (190) bounds the total deviation, is generic across
systems rather than a J1738 figure, and was never
applied by its authors to J1738's Ṗ_b, which they
recorded as the weaker constraint and set aside. The
distance-0 statement (G32-G, bar 10⁻⁶) is *not* broken
by this arm: 1.87×10⁻⁵ still clears it by ×18.7.

Retrieval limits: Freire et al. and YBBY retrieved in
full text (ar5iv/PDF) — primary grade, no gap. Vaglio
et al. 2026 retrieved in full text via the publisher/
author PDF; their Ṗ_b^GR under their own mass posterior
could not be extracted cleanly from the PDF text layer,
so the update enters indicatively only (§2). No other
post-2012 J1738 timing update stating an intrinsic
Ṗ_b/GR ratio was found in this arm's search.
