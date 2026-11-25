# PHASE 303 — THE SPIN-1 FULL AUDIT: MEMO

**Registration:** `phase303/work/p303_registration.md` (ledger
entry 750's charge, written before any computation).
**Computation:** `phase303/work/p303_audit.py` + `.out`
(symbolic identities, machinery controls, fence tables at the
corners), `phase303/work/p303_pricing.py` + `.out` (Peters
controls, corner pricing, spot-row maximisation, envelope).
Desk/analysis phase; light VM compute; no sweeps beyond the
registered maximisation grids, no launches, no ledger append.
All sources retrieved 2026-11-24.

**The row's overall standing, in one sentence:** the
Einstein-aether spin-1 channel **SURVIVES COMPLETED** — its
strong-coupling witness, Phase 298's Corner A, **dies at
completion** under the binary-pulsar dipole leg, but the
channel stands priced at Corner B and along spot rows
c_V ∈ {1, 2, 10} whose dipole ratio is flat at the spin-0
row's loudest level, because the vector mode's speed lives in
a coupling (c₁) that no completed fence leg prices.

**Plain statement, up front:** Phase 298 left one mode
unpriced: the Einstein-aether spin-1 (vector) mode, whose
speed numerator c₁ was touched by no applied fence, with the
pulsar legs recorded-not-applied because the neutron-star
sensitivity σ_æ was uncomputed in the post-GW corner. This
phase computes σ_æ at the grade the published literature
supports (Item 1), applies the deferred legs (Item 2), and
prices the channel (Item 3). The headline witness does not
survive: Corner A (c_V = 63.2456 at c₁₄ = 2.5×10⁻⁵) is
excluded by the dipole radiation its own scalar companion
mode would emit — the vector mode is an innocent bystander
in its own corner's death. What survives is quieter at the
top speed and louder everywhere else: at c_V = 3240 the
channel prices at 2.06×10⁻¹⁸ (Hulse–Taylor ratio), three
times the spin-0 row's price at the same point, and at
c_V = 2 and c_V = 10 it prices at 2.80×10⁻⁵ — the level the
spin-0 row reaches only at c_S = 1, and 10⁶ times louder
than the spin-0 row at the same speed. These are signalling
channels only; nothing here moves matter or carries cargo.

---

## 1. Item 1 — σ_æ for the spin-1 sector

### 1.1 Sources (rung 1, retrieval)

Retrieved in full text 2026-11-24: **Yagi, Blas, Barausse &
Yunes (YBBY), PRD 89, 084067 (2014) [arXiv:1311.7144v4]**
(ar5iv HTML, complete — the same text Phase 292 retrieved;
this phase reads its Einstein-aether sector, §§IV–VII and
Appendix C). **Oost, Mukohyama & Wang (OMW), PRD 97, 124023
(2018) [arXiv:1802.04303]** as retrieved in Phases 292/298
(Eq. 1.1 PPN forms; Eq. 3.8 Shao–Wex bounds
|α̂₁| ≤ 10⁻⁵, |α̂₂| ≤ 10⁻⁹ at 95%; Eqs. 3.9/3.24 α̂ forms).
**Jacobson, arXiv:0711.3822** §6 (sensitivities scale as the
couplings c_i for small c_i), as retrieved in Phase 298.

The published Einstein-aether sensitivity apparatus, with
equation numbers as used below:

- **Definitions:** σ_A ≡ −[d ln m̃_A(γ_A)/d ln γ_A]_{γ=1}
  (their Eqs. 30–34), equivalently σ = −∂²ln M_tot/∂v²|_{v=0}
  (Eq. 56); s_A ≡ σ_A/(1+σ_A).
- **Extraction (EA):** σ_Æ = 2c₁(2A − 4 − α₁^Æ)/[c₋(8 + α₁^Æ)]
  (Eq. 173), where A is the O(v) asymptotic integration
  constant of the three-field (k₁, s₁, w₁) stellar system
  (Eqs. 145–171; the vector potential's asymptotic carries
  [A + 2(c₁₄−1)]/c₋ at leading order).
- **Extraction (khronometric):** σ^kh = (2A − 4 − α₁^kh)/
  (8 + α₁^kh) (Eq. 183), from the two-field (k₁, s₁) system.
- **Weak-field anchor (EA):** s_Æ^wf = (α₁^Æ − (2/3)α₂^Æ)·
  Ω/M_obs + O(Ω²/M²) (Eq. 184), Ω the Newtonian self-energy
  (Eq. 185), Ω < 0; stated for EA with EA's α₁, α₂
  (Eqs. 42–43).
- **O(v⁰) structure:** the static stellar solutions "depend
  only on the c₁₄ combination" (§VI A, citing Eq. 45) — the
  mass–radius sector of the full theory is the khronometric
  one under the Eq. (15) map.
- **Strong-field deviation (EA):** the numerical sensitivity
  departs from Eq. (184) by **15–30% at realistic
  compactnesses 0.1 ≲ C_* ≲ 0.3** (§VI A, Fig. 3), computed
  at c₊ = 10⁻⁴ = c₋ with PPN saturated. (The khronometric
  figure Phase 292 bracketed was 50–100%; the EA literature's
  own stated deviation is the tighter one, and per the
  registration it replaces Phase 292's f ∈ [0.5, 2] here:
  **f ∈ [0.7, 1.3]**.)
- **c₋-dependence:** "the sensitivity increases monotonically
  with c₋ and c₊" (§VI A, Fig. 4) — computed at c₊ = 1 and
  c₊ = 0.1, PPN saturated.
- **Fitting formulas:** s_Æ = Σ_{ℓ,m,n≤2} c_{ℓmn} c₊^ℓ c₋^m
  C_*^n (Eq. 186, Table I, r² = 0.959) and the 120-term
  version (Appendix C, Eq. C1, r² = 0.999), both fit over
  **c₊ ∈ 3×(10⁻⁴, 10⁻¹), c₋ ∈ 3×(10⁻⁵, 10⁻³),
  C_* ∈ (0.11, 0.28)**, at **fixed** α₁^Æ = 10⁻⁴,
  α₂^Æ = 4×10⁻⁷ (Solar-System-saturating). The fits are
  retrieved and their region respected: **no fit is evaluated
  at any point of this phase** — every corner and maximiser
  below sits at c₊ = 0 (below the fits' c₊ edge) and Corners
  A/B sit at c₋ = 0.2 / 0.166 (two orders above the fits'
  c₋ edge). Evaluating them there would be exactly the
  extrapolation Phase 298 recorded-not-applied.

### 1.2 The structural read (rung 2 — decides)

Three derived facts, all verified symbolically in
`p303_audit.py` Part A1 (control C-B, §4):

1. **The α̂ forms coincide on the slice; σ does not.** On
   c₁₃ = 0 (c₊ = 0, c₋ = 2c₁), YBBY Eqs. (194)–(195) reduce
   *exactly* to OMW Eq. (3.24)'s forms,
   α̂₁ = α₁ + (8+α₁)σ and α̂₂ = (α₂/α₁)(α₁ + (8+α₁)σ), with
   the slice's α₁ = −4c₁₄ and α₂(c₂, c₁₄) — the same
   reduction Phase 292 verified for the khronometric
   reading, here re-verified as an identity in (c₁, c₂, c₁₄).
   Likewise the extraction formulas coincide in form:
   Eq. (173) at c₋ = 2c₁ is Eq. (183) verbatim. **But the
   input A is a different number**: in the full theory A is
   fixed by a three-field system in which the vector
   potential w₁ is dynamical and its asymptotic is tied to A
   through 1/c₋; in khronometric theory the system is
   two-field and A knows nothing of any c₁. The c₁-dependence
   of σ_Æ lives entirely inside A.
2. **At the orders published, σ_Æ on the slice is a function
   of (c₁₄, c₂; C_*) only.** The O(v⁰) system depends only
   on c₁₄; the weak-field anchor (Eq. 184) depends on the
   couplings only through (α₁^Æ, α₂^Æ), which on the slice
   are functions of (c₁₄, c₂) — α₂ is exactly c₁-independent
   (Phase 298, sympy-verified). So the anchor gives, exactly
   as in Phase 292,

       s_Æ(C_*) = −(α₁ − (2/3)α₂)·(3/5)·C_*,
       σ_Æ = s/(1−s),

   with Ω/M = −(3/5)C_* the uniform-density form Phase 292
   used (realistic-EoS O(1) factors absorbed in f). At
   Corner A (α₂ = 0): σ_Æ(0.17) = 1.0200×10⁻⁵ (κ ≡ σ/c₁₄ =
   0.408). At Corner B: σ_Æ(0.17) = 2.9546×10⁻⁹ — numerically
   Phase 292's σ at the same (c₁₄, c₂), as it must be: same
   α's, same anchor.
3. **Where the computation opens — stated exactly.** No
   published computation gives A (hence σ_Æ) at c₊ ≈ 0 with
   c₋ ≳ 3×10⁻³: the fits stop at c₋ = 3×10⁻³ and c₊ ≥
   3×10⁻⁴; Fig. 4's monotonicity is at c₊ ∈ {0.1, 1}; Fig. 3's
   15–30% deviation is at c₊ = c₋ = 10⁻⁴. OMW's deferral
   ("not known at present in the new ranges of the
   parameters") is, after this phase's retrieval, located
   precisely: **σ_Æ(c₊ ≈ 0, c₋ ≳ 3×10⁻³) is the open
   point**, and Corners A (c₋ = 0.2) and B (c₋ = 0.166) both
   sit in it. The named route to close it is rung 3 — a fresh
   integration of YBBY's published three-field O(v) system
   (Eqs. 145–171) with the Eq. (172)–(173) extraction. Per
   the registration, rung 3 runs only if rungs 1–2 do not
   decide Item 2; §2 shows they do — Corner A's exclusion
   holds for *every* value of σ_Æ (not merely across the
   bracket), and Corner B's status is the inherited
   saturation statement whose σ-dependence is fully displayed
   — so rung 3 is **not run**, and every downstream number
   that touches σ at large c₋ is stated as conditional on the
   anchor + bracket. The spot rows of §3 are in a different
   position: their c₋ ≤ 1.6×10⁻³ lies *inside* the fits'
   c₋ range (their c₊ = 0 remains at the fits' edge; the
   anchor is exact there regardless, since it runs through
   α₁, α₂ only).

**Item 1 verdict:** σ_Æ is computed at the grade Phase 292's
σ_æ was computed — weak-field anchor (exact leading
behaviour) + the theory's own published strong-field
deviation as bracket, f ∈ [0.7, 1.3] — as a function
σ_Æ(c₁₄, c₂; C_*) on the slice, with the structural
difference from the spin-0 sector derived (item 1 above) and
the open point named (item 3 above). No λ-analogue arises:
on the slice there is no third coupling for σ to hide in,
and at α₁ = 0 the slice collapses to the decoupling
boundary c₁₄ = 0, so no (α₁, α₂)-independent piece of σ_Æ
exists on it.

## 2. Item 2 — the completed fence

Completed fence = Phase 298's applied legs V1–V6 (GW slice;
solar α₁ ⇒ c₁₄ ≤ 2.5×10⁻⁵; solar α₂; BBN; Čerenkov;
stability) **plus** the deferred legs, now applied:
**L7** |α̂₁| ≤ 10⁻⁵ and **L8** |α̂₂| ≤ 10⁻⁹ (OMW Eq. 3.8,
Shao–Wex 95%, via the exact slice forms of §1.2 with Item
1's σ_Æ at the central compactness C_* = 0.17, brackets
reported; the isolated-pulsar α̂₂ bound carries YBBY's own
caveat — its direct mapping is declined for want of the
timed pulsars' masses, §VII B — exactly as Phase 292
carried it), and **L9** the binary-pulsar dipole map in the
programme's registered form: ⟨𝒜⟩_dip ≤ 0.1 for the
J1738-class NS–WD system (P_b = 8.5 h, m = 1.6 M☉, s_WD = 0;
X ≡ (P_b/(2πG_N m))^{2/3} = 7.255031×10⁵ computed from SI
constants), the limit being YBBY Eq. (190)'s O(10%)
tolerance — an order-of-magnitude-tolerance bound, whose
character every number it binds inherits (Phase 294's
registered rider). The dipole coefficient is the EA one
(YBBY Eq. 114): 𝒞 = 4/[3w₀³c₁₄(2−c₁₄)] + 4/[3c₁₄w₁³], with
w₀² = (2−c₁₄)c₂/[(2+3c₂)c₁₄] (Eq. 108 on the slice — the
khronometric c_S² form, sympy-verified) and w₁² = c₁/c₁₄
(Eq. 100 on the slice). The quadrupole part of ⟨𝒜⟩ is
bounded, not dropped: |⟨𝒜⟩_quad − 1| ≤ |𝒜₁−1| + 𝒮|𝒜₂| +
𝒮²|𝒜₃| + c₁₄/2 + (2/3)(s₁+s₂) with 𝒮 ≤ σ — at Corner A
this bound is 2.62×10⁻⁵, five orders below the dipole term
that decides there, so no fence conclusion rests on it.

### 2.1 Corner A — DIES AT COMPLETION

Corner A: (c₁, c₂, c₁₄) = (0.1, 2.500125×10⁻⁵, 2.5×10⁻⁵),
c₋ = 0.2, w₀ = 1.000000, c_V = 63.2456, Z = 4/3.
𝒞 = 2.666721×10⁴ — of which the **scalar piece is
2.666700×10⁴ and the vector piece 2.108×10⁻¹**: at this
corner the dipole is emitted by the spin-0 companion, not
by the mode the corner was built to witness.

| Leg | f = 0.7 | f = 1 (central) | f = 1.3 | Bound |
|---|---|---|---|---|
| L7 \|α̂₁\| | 4.2880×10⁻⁵ ✗ | 1.8400×10⁻⁵ ✗ | 6.0801×10⁻⁶ ✓ | 10⁻⁵ |
| L8 \|α̂₂\| | 0 ✓ | 0 ✓ | 0 ✓ | 10⁻⁹ |
| L9 ⟨𝒜⟩_dip | 0.15411 ✗ | 0.31451 ✗ | 0.53153 ✗ | 0.1 |

**Killing leg: L9, the binary-pulsar dipole leg** — over
its limit by ×1.54 / ×3.15 / ×5.32 across the bracket.
L7 concurs at f ≲ 1.22 and is the *only* leg that ever
passes, in the bracket's top sliver, where L9's margin is
largest. The exclusion is in fact **σ-independent**, and
this is the form in which it should be quoted: L9 passes
iff σ_Æ(0.17) ≤ 5.75×10⁻⁶, while L7 passes iff
σ_Æ(0.17) ∈ [1.125, 1.375]×10⁻⁵ (the α̂₁ window about the
tuned value c₁₄/2, Phase 292 §4's arithmetic at this
corner's α₁ = −10⁻⁴). The windows are disjoint by a factor
of two, so **no value of the sensitivity — computed,
bracketed, or yet-to-be-computed by rung 3 — lets Corner A
satisfy both legs at once** (both legs read the sensitivity
of comparable-compactness neutron stars through the same
anchor-shaped C_*-dependence; the C_* sweep at f = 1 moves
α̂₁ through its window only near C_* ≈ 0.20–0.24, where σ
is larger and L9 is worse). Rung 3 therefore cannot revive
Corner A; it could only re-decide *which* leg is quoted
first. **Mechanism:** Corner A shelters the spin-0 mode on
its Čerenkov edge (w₀ = 1) at the largest c₁₄ the solar
fence allows; there 𝒞_scalar ∝ 1/(c₁₄w₀³) while σ ∝ c₁₄,
so ⟨𝒜⟩_dip ∝ σ²𝒞 ∝ c₁₄ — the dipole grows linearly with
the coupling along the edge, and at c₁₄ = 2.5×10⁻⁵ it
overshoots the O(10%) orbital-decay tolerance by ×3.15
(central). The corner is killed by its scalar sector, at
the coupling its own solar-α₁ saturation chose.

### 2.2 Corner B — SURVIVES COMPLETED (central model)

Corner B: (c₁, c₂, c₁₄) = (0.08293104, 2/21, 7.9×10⁻⁹),
c₋ = 0.16586208, c_V = 3240 exactly (by construction of c₁;
the spin-0 speed's formula value at the literal corner is
w₀ = 3247.8 — the 3240 rider of Phases 292/298 applies to
that number, not to c_V). 𝒞 = 7.425396×10⁻³ (scalar
2.463169×10⁻³ + vector 4.962227×10⁻³ — here the vector
piece is the larger one). All applied legs V1–V6 pass, BBN
saturating at margin 0 (the literal-l = 2/21 evaluation sits
on the bound within the programme's stated saturation
tolerance — Phase 294 memo note (i); the true BBN edge is
l = 2(1−4a)/21). The completed legs, central model
(f = 1, C_* = 0.17): L7 |α̂₁| = 7.9632×10⁻⁹ (inert);
**L8 α̂₂ = −9.9540×10⁻¹⁰, saturating** (99.5% of the 10⁻⁹
bound); L9 ⟨𝒜⟩_dip = 7.3481×10⁻¹⁵ (inert by 13 orders).
Corner B is, in its (c₁₄, c₂) coordinates, Phase 292's
shrunk corner — it inherits that corner's status exactly:
a fence-saturating reference point of the completed fence,
not a maximum. Its caveats, on its face: (i) the L8
saturation rests on the isolated-pulsar α̂₂ bound whose
direct mapping YBBY decline (under YBBY's own *binary*
α̂₂ bound, 1.8×10⁻⁴, the leg would be inert by five
orders); (ii) across the EA bracket, α̂₂(f) spans
[−1.8818×10⁻⁹ (f = 0.7), −1.0902×10⁻¹⁰ (f = 1.3)] — at the
bracket's low end the corner would shrink slightly along
Phase 292's a*(f) pattern; (iii) σ_Æ's strong-field value
at c₋ = 0.166 is uncomputed in print (§1.2, item 3): the
survival is a statement at the anchor + bracket grade, and
rung 3 is the named route to better.

## 3. Item 3 — the channel priced

Conventions: Phase 294/296 verbatim. Fiducials: HT
(1.44 + 1.39 M☉, P_b = 7.75 h, e_orb = 0.617, R = 12 km
both stars — C₁ = 0.1772, C₂ = 0.1710, ΔC_* = 0.00615;
Peters quadrupole computed, 7.7808×10²⁴ W, control-exact);
NS–BH bound class (1.4 + 10 M☉, P_b = 7.75 h, e_orb = 0,
Δσ = σ_Æ(C_* = 0.17), the labelled maximal-asymmetry bound
class; Peters circular quadrupole computed, 1.2696×10²⁵ W,
control-exact). Ratios are the circular ⟨𝒜⟩_dip of
YBBY Eq. (193) with the EA 𝒞 of Eq. (114), times
g(e)/F(e) = 0.3330 for HT (Phase 292's eccentric treatment);
equal compactness ⇒ dipole exactly 0, as registered. The
single strong-field factor f multiplies the anchor
everywhere (fence and fiducial consistently); envelope =
full re-runs at f ∈ {0.7, 1.3}, the EA literature's own
15–30% deviation — where Phase 294 carried a khronometric
κ-bracket and a separate f_fid, the mapping is: this
phase's f is that phase's two factors identified, at the
EA-published width.

### 3.1 Corner B (c_V = 3240), priced

| Model | HT ratio | HT P_dip | NS–BH ratio | NS–BH P_dip |
|---|---|---|---|---|
| f = 0.7 | 1.0097×10⁻¹⁸ | 7.8566×10⁶ W | 9.1433×10⁻¹⁶ | 1.1608×10¹⁰ W |
| **f = 1** | **2.0607×10⁻¹⁸** | **1.6034×10⁷ W** | **1.8660×10⁻¹⁵** | **2.3690×10¹⁰ W** |
| f = 1.3 | 3.4826×10⁻¹⁸ | 2.7097×10⁷ W | 3.1535×10⁻¹⁵ | 4.0036×10¹⁰ W |

At the same (c₁₄, c₂) the spin-0 row prices at HT
6.8296×10⁻¹⁹ (Phases 292/294): **the spin-1 channel at
Corner B is ×3.01 louder** — exactly the ratio of the 𝒞's
(7.4254×10⁻³ vs 2.4632×10⁻³), i.e. the vector piece
(4.9622×10⁻³) added to the scalar piece the two rows share.
Same speed class, same coupling c₁₄, three times the
dipole: the parity corner of the census is not a parity
price.

### 3.2 Spot rows — the flat curve

Maximising the HT ratio subject to c_V ≥ c* over the
completed fence (central model; c₁ = c*²c₁₄ at the optimum
— verified global in c₁: at fixed (c₂, c₁₄) the ratio only
falls as c₁ grows, since 𝒞's vector piece dilutes; the
floor-binding maximiser also minimises c₋, hence the
uncomputed-σ exposure):

| c* | Maximiser (c₁, c₂, c₁₄) | c₋ | w₀ | 𝒞 | Binding legs | HT ratio | NS–BH ratio |
|---|---|---|---|---|---|---|---|
| 1 | (2.6568×10⁻⁶, 2.6676×10⁻⁶, 2.6568×10⁻⁶) | 5.314×10⁻⁶ | 1.0020 | 7.5127×10⁵ | L9 (= 0.10000); L8 near (−9.8853×10⁻¹⁰) | **2.8044×10⁻⁵** | **2.5394×10⁻²** |
| 2 | (2.5443×10⁻⁵, 6.3620×10⁻⁶, 6.3608×10⁻⁶) | 5.089×10⁻⁵ | 1.0001 | 1.3098×10⁵ | L9 (= 0.10000) | **2.8044×10⁻⁵** | **2.5394×10⁻²** |
| 10 | (7.9511×10⁻⁴, 7.9621×10⁻⁶, 7.9511×10⁻⁶) | 1.590×10⁻³ | 1.0007 | 8.3842×10⁴ | L9 (= 0.10000); L8 near (−9.9797×10⁻¹⁰) | **2.8044×10⁻⁵** | **2.5394×10⁻²** |

(P_dip at every row: HT 2.1820×10²⁰ W; NS–BH 3.2240×10²³ W.
L9's limit is the O(10%) tolerance of YBBY Eq. (190); every
row inherits its order-of-magnitude character. L8's caveat
attaches to the c* = 1 and c* = 10 rows, where it is
near-binding.)

**The curve is flat.** The maximised ratio is the same at
c_V = 1, 2 and 10 to all quoted digits, because the binding
constraint (L9) caps the product σ²𝒞, and along the
w₀ ≈ 1 edge that product is a function of (c₁₄, c₂) alone:
raising the speed floor only re-sits c₁ = c*²c₁₄ (and with
it 𝒞's small vector piece), while c₁₄* re-solves to keep
σ²𝒞 at the cap. Contrast Row 1 (Phase 296, central model):
HT 3.917708×10⁻⁹ at c_S = 2 and 2.374368×10⁻¹¹ at c_S = 10 —
the spin-0 row pays ×7,151 then ×165 for speed, because its
speed and its price are the same coupling. The spin-1 row
at c_V = 10 is **×1.18×10⁶ louder than the spin-0 row at
c_S = 10**, and at c_V = 2 ×7.2×10³ louder, at the price of
being no louder than the spin-0 row's own loudest point
(2.8017×10⁻⁵ at c_S = 1): the flat curve's height is the
dipole cap's height in both rows, because both rows' caps
are set by the same scalar-sector product σ²𝒞_scalar at
w₀ ≈ 1. What the vector mode buys is not height but
*reach*: the cap-level ratio, available at speed.

**Envelope (f re-runs):** at f = 1.3 every row reproduces
the flat central values (L9 binding throughout). At
f = 0.7 the c* = 1 row still reaches 2.8044×10⁻⁵ (L9
binding), but the c* = 2 and c* = 10 rows are cut by L7
(α̂₁ = −1.0000×10⁻⁵ binding, maximisers on the α₂ = 0 edge
at c₁₄ = 5.8302×10⁻⁶) to HT 1.2598×10⁻⁵ and 1.0099×10⁻⁵
(NS–BH 1.1408×10⁻², 9.1445×10⁻³). Envelope statement: HT
ratio ∈ [1.01×10⁻⁵, 2.80×10⁻⁵] at c_V = 10 across the
bracket — the flatness is a central-model statement, the
floor of the envelope is an L7-cut statement, and at no
point of the envelope does any spot row fall within five
orders of magnitude of the spin-0 row's price at the same
speed.

## 4. Controls and verdicts

**Controls (all PASS, run before any corner was decided):**
C-A — Phase 298's `p298_row2.py` re-run reproduces its
stored `.out` exactly (blank-line-normalised diff empty):
Corner A c_V = 63.2456 and Corner B c_V = 3240 under the
applied fence, diff-0. C-B — symbolic (Part A1): YBBY
(194)–(195) reduce to the OMW (3.24) slice forms exactly
(differences simplify to 0); Eq. (108) → the khronometric
c_S² form and Eq. (100) → c₁/c₁₄ on the slice; Eq. (173) ≡
Eq. (183) in form on the slice (ratio 1). Machinery
controls: X_J1738 and the programme's KH-𝒞 dipole form
reproduce Phase 294's C3 (7.8606×10⁻¹² vs 7.8608×10⁻¹²) and
leg-9 binding value (9.99934×10⁻² vs 9.99953×10⁻²) at
diff-0-class (≤ 3×10⁻⁵ relative, the stored values' own
rounding); Peters controls exact (7.7808×10²⁴ W;
1.2696×10²⁵ W with μ = 1.2281 M☉, a_orb = 3.1014×10⁹ m);
HT compactnesses exact (0.1772 / 0.1710 / 0.00615).

**Verdicts (registered forms, ledger 750):**
- Item 1 — σ_Æ COMPUTED at rung-2 grade (anchor + EA
  bracket); the computation's open point named exactly
  (σ_Æ at c₊ ≈ 0, c₋ ≳ 3×10⁻³), rung 3 named and not run,
  for the registered reason (§2.1: Corner A's exclusion is
  σ-independent, so rung 3 cannot change any verdict).
- Item 2 — Corner A: **DIES AT COMPLETION** (killing leg
  L9, binary-pulsar dipole; mechanism §2.1; L7 concurring
  except in the bracket's top sliver). Corner B: **SURVIVES
  COMPLETED** at the central model, as a fence-saturating
  corner (BBN + L8), caveats on its face (§2.2).
- Item 3 — **CHANNEL PRICED**: Corner B (HT 2.0607×10⁻¹⁸,
  NS–BH 1.8660×10⁻¹⁵ at c_V = 3240) and spot rows c_V ∈
  {1, 2, 10} flat at HT 2.8044×10⁻⁵ / NS–BH 2.5394×10⁻²
  (central), envelope §3.2.
- **Row verdict: SURVIVES COMPLETED** — with Corner A's
  death recorded as the completion's cost. Phase 298's
  OUTRUNS verdict rested on Corner A as its witness; that
  witness is withdrawn, and the outrunning now rests on
  §3.2's flat curve and §3.1's ×3.01 — quote those, never
  Corner A, for the row's strength. **What remains
  recorded-not-applied, enumerated:** (i) σ_Æ's strong-field
  value at c₊ ≈ 0, c₋ ≳ 3×10⁻³ (Corners A/B's regime) —
  uncomputed in print; every number touching it is stated
  at anchor + bracket grade, and Corner A's verdict alone
  is independent of it; (ii) YBBY's Fig. 7 allowed bands as
  drawn — applied here through their mechanism
  (Eqs. 190–195) rather than read off the figure, since the
  bands were computed inside the fits' region and reading
  them at c₋ = 0.2 would be the extrapolation Phase 298
  forbade; their combined region (an almost-box of c₋-width
  O(10⁻³), §VII C.1) is consistent with, but is not, this
  phase's fence; (iii) the fits of Eq. (186)/Appendix C —
  retrieved, region respected, evaluated nowhere. Nothing
  else in the row's fence set remains unapplied: GW, solar
  α₁, solar α₂, BBN, Čerenkov, stability, α̂₁, α̂₂ and the
  dipole maps have all now been applied to the spin-1
  sector at primary-source grade.

## 5. Reality Desk checklist (Phase 236 protocol)

- **Step 0 — Claims as posed.** The spin-1 mode's surviving
  corner under the completed fence, and its channel price
  at that corner and at registered spot speeds. Free
  parameters (c₁, c₂, c₁₄) on the GW slice; background
  Minkowski + preferred frame; c = 1 units in the fence
  algebra, SI in the pricing.
- **Step 1 — Limits/dimensions.** c_V² → c₁/c₁₄ and
  w₀² → the khronometric c_S² on the slice (symbolic);
  σ_Æ → 0 as (α₁, α₂) → 0 (anchor); 𝒞's scalar piece →
  the khronometric 𝒞 when the vector piece is removed;
  GR recovered as c_i → 0 (Eq. 193 → ⟨𝒜⟩ = 1); all ratios
  dimensionless, powers in watts from SI constants.
- **Step 2 — Data-contact search.** GW170817 speed (slice);
  solar PPN α₁/α₂; BBN G-rescaling; UHECR vacuum Čerenkov;
  Shao–Wex strong-field α̂₁/α̂₂ (isolated + binary
  pulsars); binary-pulsar orbital decay (YBBY systems
  J1141−6545, J0348+0432, J0737−3039, J1738+0333 — applied
  through the J1738-class dipole term, the strongest of the
  three Ṗ_b systems at fixed mass by the (P_b/m)^{2/3}
  scaling, with the quadrupole deviation bounded at
  ≤ 2.62×10⁻⁵ at the deciding corner).
- **Step 3 — Applicability.** Each leg applied in its
  published form at the slice; the two legs whose mapping
  the literature itself qualifies carry their qualifications
  on their faces (L8's isolated-pulsar caveat; L9's O(10%)
  tolerance character). The fits' region is respected by
  non-evaluation. σ_Æ's open point is named rather than
  filled.
- **Step 4 — Verdicts.** As §4: row SURVIVES COMPLETED;
  Corner A DIES AT COMPLETION (L9); Corner B SURVIVES
  COMPLETED (central, saturating); channel PRICED (Corner B
  + flat spot rows).
- **Step 5 — Recording.** This memo is the record. One line:
  `DESK: Einstein-aether spin-1 (vector) signal channel — SURVIVES the completed fence (sigma_AE = YBBY Eq. (184) anchor, EA bracket f in [0.7,1.3]; strong-field sigma at c+~0, c- > 3e-3 uncomputed in print, rung-3 TOV named not run): Corner A (c_V = 63.2456 at c14 = 2.5e-5) DIES AT COMPLETION by the binary-pulsar dipole leg (x1.54-5.32 over across the bracket; no sigma value passes both the dipole and alpha-hat-1 windows), killed by its scalar companion's dipole (vector piece 0.21 of C = 2.67e4); Corner B SURVIVES COMPLETED at the central model (c_V = 3240; BBN + isolated-pulsar alpha-hat-2 saturating, that bound's caveat attached), priced HT 2.0607e-18 / NS-BH 1.8660e-15 (x3.01 the spin-0 price at the same point); spot rows FLAT at HT 2.8044e-5 / NS-BH 2.5394e-2 for c_V = 1, 2, 10 (envelope HT >= 1.01e-5 at c_V = 10) — the speed lives in c1, which no completed leg prices.`

**Retrieval limits (on the face of the memo).** Retrieved
in full 2026-11-24: YBBY arXiv:1311.7144v4 (ar5iv HTML,
complete, including Appendix C). OMW and Jacobson as
retrieved in full in Phases 292/298; no bound in the set
was found to have moved since. Foster PRD 76, 084033
(2007) = arXiv:0706.0704: used only as republished and
corrected by YBBY (who state explicitly that they found
and fixed errors in Foster's flux calculation — the
𝒱_ij term of Eq. (102) is YBBY's correction); no number
rests on Foster alone. Shao–Wex bound values via OMW
Eq. (3.8) and YBBY §VII B, not from the Shao–Wex papers
directly. No TOV integration was run (rung 2 decided, per
the registered ladder).

## 6. What this is not

A statement about a signalling channel in principle, in a
hypothetical Lorentz-violating gravity theory. Nothing here
moves matter faster than light, forms or holds a geometry,
or carries cargo; no transport, vehicle, formation, or
drive content is claimed or implied. The ratios are values
at theory-space corners for the stated fiducial systems —
the NS–BH figure a bound-class asymmetry for a system class
with no timed exemplar — not detections and not
detectability claims. Corner values are maxima of nothing
but their named objectives; Corner A is a dead corner and
is quoted only as one.
