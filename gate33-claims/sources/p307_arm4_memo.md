# PHASE 307 — ARM 4: THE DISPUTE ADJUDICATED (scope: the flat value's pricing framework)

**Worker:** red team, Phase 307. **Charge:** registration
`phase307/work/p307_registration.md`, ARM 4. **Target claim:**
G32-F (Gate-32 §5) — the flat HT ratio 2.8044×10⁻⁵ at c_V = 1, 2, 10,
priced with the YBBY far-zone dipole coefficient 𝒞 (YBBY Eq. 114),
bound by L9 (⟨𝒜⟩_dip ≤ 0.1, J1738-class). **Method:** full-text
retrieval of both Taherasghari–Will (TW) papers, of the post-TW
pricing literature's engagement (Vaglio et al. 2026), and a
quantitative re-evaluation at the registered maximisers with the
programme venv python. No ledger append, no launches.

**Bibliographic correction, on the record:** Paper I is
PRD **108, 124026** (2023) [arXiv:2308.13243], not 102026 as
written in Gate-32 and in this arm's charge. Paper II is
PRD 112, 024013 (2025) [arXiv:2506.03843]. No number below
depends on the article number.

---

## 1. What TW actually compute

**Paper I (2023)** computes no dipole and no equations of motion.
It adapts DIRE (direct integration of the relaxed equations) to
Einstein-aether: by a redefinition of the perturbative metric and
aether variables via superpotentials it obtains flat-spacetime wave
equations for each new field, and solves them **in the near zone**
through 2.5PN order. Its own stated plan (abstract/introduction):
future papers will obtain the equations of motion, the far-zone
fields, and finally the energy flux and waveform. Paper I is the
foundation, not the dispute.

**Paper II (2025)** derives the compact-binary **equations of
motion** through 2.5PN order from Paper I's near-zone potentials,
via the modified geodesic equation for bodies whose masses depend
on γ = −K_ae·u (sensitivities, their Eq. (15)-series definitions),
and computes the **rate of change of the near-zone orbital energy**
dE/dt by contracting those equations of motion — i.e. a
**radiation-reaction (near-zone) energy loss**, not a far-zone
flux integral. Headline results:

- Dipole (−1PN) energy loss, TW Eq. (42):

      Ė_{−1PN} = −(G³m₁²m₂²/3r⁴) · [(s₁−s₂)/((1−s₁)(1−s₂))]²
                 · [ 1 + 3(2−c₁₄)/(c₁v_T) ]

  with v_T² = c₁/c₁₄ (their Eq. (5)) — the **transverse (spin-1)
  aether speed only**. The longitudinal/spin-0 speed
  v_L² = (2−c₁₄)c₂/[(2+3c₂)c₁₄] (≡ w₀² on the record's slice)
  **does not appear**. TW trace this structurally to their
  relaxed equations (Paper II Eq. (3)): in the redefined
  variables the metric potentials obey wave equations at speed 1
  and the aether potential at v_T; "**There is no wave equation
  involving the speed v_L**" (§V.1).
- The 0PN (quadrupole-analogue) loss, TW Eq. (49), likewise
  "bear[s] no resemblance to published results, even in the
  limit s₁→0, s₂→0" (§V.2) — the disagreement is not dipole-only.

**The far-zone result TW dispute**, in TW's own translation
(§V.1, their Eq. (53)): Foster's/YBBY's expression has the *same
form* as Eq. (42) with the bracket replaced by

      [ 2/(c₁₄v_L³) + 2(2−c₁₄)/(c₁v_T) ] ,

cited to Foster's Eqs. (79)/(89) and to Eq. (116) of ref. [14]
(YBBY). TW: "Apart from a numerical factor of 3 vs. 2 in the
second term, the biggest difference is that Foster et al.'s
coefficient depends on the longitudinal speed v_L, whereas ours
does not. … **We have been unable to find a simple resolution of
this disagreement.**"

## 2. What L9 prices, and what TW claim about it — scope quoted precisely

L9 bounds Ṗ_b of a J1738-class binary via ⟨𝒜⟩. In the standard
treatment (GR and EA alike, at the orders involved) Ṗ_b is
obtained from the orbital energy loss by the **balance relation**
Ṗ_b/P_b = −(3/2)Ė_b/E_b with Ė_b = −ℱ_far-zone. TW do **not**
compute a far-zone flux and do **not** claim the Foster/YBBY flux
integral is arithmetically wrong on its own terms. What they
claim, verbatim in scope (§V.2, final paragraphs):

- "our work and the previous calculations are **conceptually very
  different. We have calculated the near-zone gravitational
  radiation reaction effects, while previous work has calculated
  the far-zone energy flux** using the 'Noether current' as a
  device…"
- "It seems eminently reasonable that they should be equal to
  each other, but in fact **there is limited concrete evidence
  for this 'energy balance' even in GR**." (They cite Ehlers et
  al. 1976's criticism and note the one explicit GR check,
  Pati–Will at 3.5PN, giving balance to 1PN beyond quadrupole.)
- "**could it be possible that energy balance is not valid
  already at the lowest dipole-radiation order**, and if not,
  would that invalidate the theory? **Conversely could there be
  a fundamental flaw either in our approach** to applying the
  'relaxed field equations' methodology to the theory, **or in
  the Noether current approach** to determining the energy flux?
  **This will be the subject of further research.**"

So TW's stated scope is: *an unresolved discrepancy between two
conceptually distinct calculations, with three live alternatives
(balance fails in EA / TW's relaxed-equation method is flawed /
the Noether-current flux is flawed), expressly undecided by its
authors.* TW nowhere assert that their Eq. (42) is the correct
replacement pricing for Ṗ_b, and nowhere withdraw the far-zone
coefficient. Any red-team verdict that simply substitutes Eq. (42)
for 𝒞 and declares the flat value broken would be applying TW
**outside TW's own stated scope** — the opposite red-team failure
this arm was charged to avoid.

Two further scope facts:

- **PN-correction rider (TW §V.2):** TW also note that prior
  authors' use of Ṗ/P = −(3/2)Ė/E "is only valid at the lowest
  Newtonian order" when Ė carries PN corrections. This touches
  0PN-and-above corrections, not the leading −1PN dipole term
  L9 prices; Vaglio et al. (2026) Eq. (45) confirm the relation
  holds at the 1PN-corrected level they use. It does not reach
  the dipole cap.
- **Post-TW adoption, with engagement:** Gupta et al. (2021)
  *predate* TW and cannot engage them; they use the far-zone
  coefficient (their Eq. (35): scalar c_S⁻³ + vector c_V⁻³
  pieces, priced as a sum — Gate-32 §5). **Vaglio et al. (2026),
  PRD 114, 104021 [arXiv:2605.01436], engage TW directly**
  (§III.3, their Eqs. (44)–(49)): they state the balance relation
  Ė_b = −ℱ explicitly, reproduce *both* prefactors — balance:
  Ė_b ∝ (2/(c_a v_L³) + 4(2−c_a)/(c_ω v_T)); direct-PN (TW):
  Ė_b ∝ (1 + 6(2−c_a)/(c_ω v_T)) — and **deliberately follow the
  pre-TW energy-balance expression**, giving reasons: the spin-0
  mode "carries energy away from the system and is expected to
  remain physical at all PN orders," so its speed should appear;
  and the balance prefactor vanishes as v_T, v_L → ∞ (fields
  non-dynamical ⇒ GR limit, no dipole flux) while TW's does not
  (their fn. 11 answers the sensitivities→0 rebuttal). They
  "defer a thorough investigation of this discrepancy to a
  future study." Independently, Albertini, Vaglio & Barausse
  (2026, arXiv:2611.21034) show by fully nonlinear collapse that
  the spin-0 mode *is* a dynamical, positive-energy-carrying wave
  at its linear-theory speed — removing the "spin-0 is not a
  wave" reading of TW — while stating explicitly that spherical
  collapse "cannot decide whether the near-zone
  radiation-reaction force or the energy flux correctly describes
  the energy loss of a two-body system."

## 3. Quantitative test — TW's coefficient at the flat maximisers

**Mapping (stated, with limits).** TW's §V.1 statement that the
far-zone result is Eq. (42)'s form with the bracket replaced lets
the ratio be taken bracket-to-bracket, with every common factor
(sensitivities, masses, r, X) cancelling. Cross-checks performed
in the venv:

1. The far-zone bracket equals **3𝒞 exactly** (to ≤1.3×10⁻⁵,
   the stored 𝒞's rounding) at every test point, where 𝒞 is the
   record's YBBY Eq. (114) coefficient: 3𝒞 = 4/[c₁₄(2−c₁₄)v_L³]
   + 4/[c₁₄v_T³], and with c_ω ≡ c₋ = 2c₁ on the slice,
   4/[c₁₄v_T³] = 4(2−c₁₄)/(c_ωv_T)·(2/(2−c₁₄))·… — evaluated
   numerically, Vaglio's balance bracket and 3𝒞 agree to
   1.000000–1.000013 at M1, M2, M10, Corner B, Corner A.
2. TW's bracket in Vaglio's variables, 1 + 6(2−c_a)/(c_ωv_T)
   with c_ω = 2c₁, is identically TW's 1 + 3(2−c₁₄)/(c₁v_T).
3. Sensitivities: TW's s_A ≡ (d ln m_A(γ)/d ln γ)_{γ=1}; the
   record's σ is YBBY's sensitivity and s_YBBY = σ/(1+σ). At the
   test points σ ≤ 3.24×10⁻⁶ and the WD sensitivity is 0, so
   [(s₁−s₂)/((1−s₁)(1−s₂))]² = (Δσ)² to relative accuracy
   ≲10⁻⁵ under either identification (sign conventions square
   away). **Limit of the mapping:** this identifies the
   *coefficient* ratio only; it does not re-derive TW's σ from
   their γ-expansion at strong field, which nobody has published
   — the same rung-2 σ is carried on both sides, so it cancels.

Hence ⟨𝒜⟩_dip^TW(point) = ⟨𝒜⟩_dip^YBBY(point) × R(point),
R = [1 + 3(2−c₁₄)/(c₁c_V)] / (3𝒞), and the HT ratio priced with
TW's coefficient at the same point scales by the same R.

| Point | c_V | 𝒞 (YBBY) | TW bracket | 3𝒞 (far bracket) | R = TW/far | ⟨𝒜⟩_dip^TW at J1738 (YBBY read = 0.10000) | HT ratio under TW at this point |
|---|---|---|---|---|---|---|---|
| M1 (2.6568e-6, 2.6676e-6, 2.6568e-6) | 1 | 7.5127×10⁵ | 2.2584×10⁶ | 2.2538×10⁶ | **1.0020** | 0.10020 | 2.8100×10⁻⁵ |
| M2 (2.5443e-5, 6.3620e-6, 6.3608e-6), σ=2.60×10⁻⁶ | 2 | 1.3098×10⁵ | 1.1791×10⁵ | 3.9295×10⁵ | **0.30007** | **0.03001** | **8.415×10⁻⁶** |
| M10 (7.9511e-4, 7.9621e-6, 7.9511e-6), σ=3.24×10⁻⁶ | 10 | 8.3842×10⁴ | 7.5561×10² | 2.5153×10⁵ | **0.003004** | **3.00×10⁻⁴** | **8.42×10⁻⁸** |

(Deciding arithmetic reproduced from the stored inputs:
⟨𝒜⟩_dip^YBBY recomputed at M2/M10 from σ, 𝒞, X_J1738 = 7.255031×10⁵
is 0.10037 / 0.09977 — the maximisers' saturation of the 0.1 cap,
rounding as stored.)

**Reading of the numbers.**

- **Under TW, L9 does not bind at M2 or M10.** The J1738 dipole
  reads fall to 0.030 (M2) and 3.0×10⁻⁴ (M10). The mechanism is
  exactly the disputed one: at the maximisers w₀ ≈ 1, so 𝒞 is
  dominated by its scalar piece (80% at M2, 99.8% at M10), and
  TW's bracket contains no v_L/w₀ term at all — what remains is
  ∝ (2−c₁₄)/(c₁c_V) = (2−c₁₄)/(c₁₄c_V³), i.e. the TW dipole
  falls as **c_V⁻³** where the far-zone scalar piece is
  speed-independent. Flatness is therefore *not* a property of
  TW's coefficient: R runs 1.0020 → 0.30007 → 0.003004 across
  c_V = 1, 2, 10.
- **Under TW, the flat value at its registered points collapses
  as stated:** HT 8.415×10⁻⁶ at c_V = 2 (below the quoted
  2.8044×10⁻⁵ by ×3.33) and HT 8.42×10⁻⁸ at c_V = 10 — **below
  the programme's 10⁻⁶ distance-0 bar by ×11.9**. Via the
  Gate-32 skeleton (HT = cap × (ΔC_*/0.17)² × (X_HT/X_J1738) ×
  (g/F), HT/cap = 2.8044×10⁻⁴), the *effective* cap TW's
  coefficient imposes at the M10 point corresponds to a
  TW-priced HT of 8.42×10⁻⁸; there is no single replacement cap,
  because R is point-(speed-)dependent — that is the collapse of
  the flat form, not a rescaling of it.
- At c_V = 1 the two coefficients coincide to 0.2% (R = 1.0020):
  the c_V = 1 row is insensitive to the dispute.
- For the record (outside this arm's scope): at Corner B,
  R = 45.89 — TW's bracket is *larger* there — but Corner B's
  YBBY dipole read is 7.3481×10⁻¹⁵, so its TW read
  (≈3.4×10⁻¹³) remains inert by 11 orders; at Corner A,
  R = 2.436×10⁻⁵, which would move its L9 read from 0.31451 to
  ≈7.7×10⁻⁶ — noted only as a record entry; Corner A's death
  (G32-D) is *not* re-decided by this arm, whose scope is the
  flat value, and G32-D's σ-independence argument was built on
  the far-zone leg.
- A full re-maximisation of the fence under TW's coefficient
  was **not** run: it is not the registered test (the test is at
  M2/M10), and under TW the binding-leg structure changes
  (L9-TW inert at the old maximisers; L7/L8 would bind first),
  so no "TW flat value" exists to quote from this arm. What is
  established is point-wise and structural (the c_V⁻³ fall),
  which suffices for the verdict form below.

## 4. Verdict — ARM 4: FENCED

Not BREAKS: TW, at their own stated scope, do not invalidate
the far-zone pricing — they exhibit a discrepancy between two
conceptually distinct calculations, name three live resolutions
including a flaw in their own method, and expressly leave the
question to further research (§2 quotes). Substituting their
bracket as the correct Ṗ_b pricing would exceed their scope.
The post-TW pricing literature that engages them (Vaglio et al.
2026) deliberately retains the balance-law coefficient, with
stated physical reasons; the spin-0 mode's dynamical,
energy-carrying reality has since been confirmed nonlinearly
(Albertini–Vaglio–Barausse 2026), though that work itself
declines to decide the binary question.

Not HOLDS: the quantitative test shows the flat value is
*entirely* carried by the disputed term. Remove the far-zone
scalar piece — the precise content of TW's objection — and at
the registered maximisers L9 stops binding (0.030 / 3.0×10⁻⁴),
the c_V = 10 row falls below the 10⁻⁶ bar (8.42×10⁻⁸), and
flatness itself disappears (R: 1.0020 / 0.30007 / 0.003004).
A claim whose deciding numbers change by ×3.3 and ×333 under a
published, unresolved, on-scope objection is not "unreached" by
that objection.

**Exact fence wording (to be attached to G32-F wherever quoted):**

> "The flat value HT 2.8044×10⁻⁵ at c_V = 1, 2, 10 is priced
> with the Foster/YBBY **far-zone (energy-balance) dipole
> coefficient** 𝒞 (YBBY Eq. 114), whose scalar piece
> ∝ 1/(c₁₄(2−c₁₄)w₀³) supplies 80% (c_V = 2) to 99.8%
> (c_V = 10) of 𝒞 at the maximisers and whose use for Ṗ_b
> rests on the energy-balance relation Ė_b = −ℱ. Taherasghari
> & Will's near-zone radiation-reaction calculation (PRD 108,
> 124026 (2023); PRD 112, 024013 (2025), Eq. (42)) contains no
> w₀ term — its dipole depends only on c_V, falling as c_V⁻³ —
> and its authors leave open whether energy balance fails in
> Einstein-aether or either calculation is flawed. Under TW's
> coefficient, at the same maximisers, the J1738 dipole reads
> are 0.030 (c_V = 2) and 3.0×10⁻⁴ (c_V = 10) instead of the
> binding 0.100, and the TW-priced HT ratios are 8.4×10⁻⁶
> (c_V = 2) and 8.4×10⁻⁸ (c_V = 10, below the 10⁻⁶ bar); the
> c_V = 1 row is dispute-insensitive (coefficients agree to
> 0.2%). The far-zone coefficient is the one the post-GW
> pricing literature uses — Gupta et al. (2021), and Vaglio et
> al. (2026), who engage TW explicitly and adopt the
> balance-law expression with stated reasons, deferring the
> discrepancy's resolution. **The flat value stands exactly
> and only in the regime where the energy-balance / far-zone
> dipole pricing is the correct Ṗ_b pricing; it is not a
> coefficient-independent result.**"

**Retrieval limits (on the face of this memo).** Retrieved in
full text 2026-11-24: TW Paper II, arXiv:2506.03843v1 HTML
(complete, §§I–V + appendices incl. Eq. (42), Eq. (53) passage);
Vaglio et al. 2026, arXiv:2605.01436v1 HTML (§§I–III.4 read in
full incl. Eqs. (44)–(49) and fn. 11; results sections not
needed for this arm). Paper I: abstract + introduction +
programme statements in full (arXiv:2308.13243), plus its
near-zone results as carried and used in Paper II §II.1 — Paper
I contains no dipole/EOM result, so nothing in §§1–3 rests on
its un-read middle sections. Gupta et al. 2021: Gate-32's
full-text record (§5) plus abstract; their engagement with TW
is impossible (2021 < 2023) and is stated as such, not inferred.
Albertini–Vaglio–Barausse 2026: abstract + indexed full-text
passages stating their scope limit verbatim. No response by TW
to Vaglio et al. was found in search as of this run.
