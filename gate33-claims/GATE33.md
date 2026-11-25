# GATE-33 — ADVERSARIAL RE-JUDGEMENT OF THE SPIN-1 CLAIMS
# PHASE 307 BROKE (G32-E, G32-F, G32-G)

Date: 2026-11-24. Adversarial re-judgement, not a phase.
Scope, fixed in advance (`gate33/work/g33_registration.md`):
G32-E (Corner B survives completed), G32-F (the flat
curve) and G32-G (distance-0), as broken or fenced by the
Phase 307 red team — Arm 1 (the dipole leg's tolerance is
a confidence-level artefact; data-grade cap 0.067 at its
own implicit confidence, 0.193 at 95%), Arm 2 (YBBY
Fig. 7's bands as drawn exclude Corner B's projection;
the c_V = 10 maximiser unresolved at text grade), Arm 4
(the flat value's pricing framework fenced to far-zone /
energy-balance pricing) — and as promoted by Phase 306
(Gupta cross-check: AGREEMENT; σ second-pathed).
Frame of record: Phase 166 pin, venv python
(numpy/scipy/sympy). Method: the gate wrote its own
machinery (`g33_controls.py`, `g33_diagnosis.py`);
controls reproduced the stored Phase 303/306/307 numbers
before any re-judgement read was quoted (§1); the YBBY
construction was reconstructed from the paper's own
LaTeX source (`g33_ybby_reconstruction.md`, from
`gate33/work/ybby_src/paper.tex`, arXiv:1311.7144
e-print) and the drawn regions were extracted from the
published figure files themselves
(`g33_fig7_extraction.md`). The gate does not repair
what it breaks beyond the registered re-issues of §5.

## VERDICT

- **Item 1 — FENCE GOVERNS.** The bands-vs-fence
  discrepancy is driven by a modelling choice the
  reconstruction exhibits (registered candidate (c)):
  **YBBY's (c₊, c₋) plane is the leading-order small-α
  reduced family** defined by Eqs. (Aecons)/(Aecons2)
  (paper.tex L669–L677) — not the full theory — and at
  c₊ = 0 that family degenerates identically
  (c₂ = c₁₄ = 0 at every c₋; §2, Part A). The drawn
  combined region is that family's allowed set (the
  per-system pulsar bands' intersection ∩ the family's
  Cherenkov wedge); its exclusion of the plane point
  (0, 0.16586208) is a statement about the family's
  degenerate member there. Corner B is not that member:
  it is an off-family GW-slice point departing from the
  family at (α₁, α₂) = (−3.16×10⁻⁸, −3.95×10⁻⁹), inside
  the Solar-System ranges the bands themselves vary
  over, and **at Corner B's own parameters every
  constraint YBBY state is satisfied with margins of
  four to five orders** (§2, Part B). Candidate (a) is
  the presentation mechanism (a reduced plane vs the
  fence's point-true fixed-fiducial reads); candidate
  (b) is excluded as the driver (Part C: the σ toggle
  moves any Ṗ_b read at B by ≤ ×1.69 against margins
  ≥ 10⁴). **G32-E SURVIVES RESTATED** (§5), re-issued
  with the projection read carried on its face. The
  verdict covers both points at the projection: the
  Phase 303 corner (c₁₄ = 7.9×10⁻⁹) and Phase 306's
  second-pathed coordinate (c₁₄* = 6.4227×10⁻⁹,
  c_V = 3593.4), which share (c₊, c₋) = (0, 0.16586208)
  and the same off-family status.
- **Item 3 — DECIDED: the c_V = 10 maximiser is INSIDE
  the combined drawn region** under the registered
  Arm-2 box semantics, at deciding grade (margin
  +4.52×10⁻⁴ in c₋ = 23σ, extraction σ = ±2×10⁻⁵;
  inside all four Fig. 7 panels as drawn at that c₋).
  Arm 2's UNRESOLVED is superseded. The wedge caveat is
  carried on the face of the claim set (§3, §5).
- **Item 2 — G32-F and G32-G SURVIVE RESTATED** at the
  data-grade dipole cap. The quotable confidence
  convention is **the tolerance's own implicit
  confidence** (cap 0.067; flat value HT 1.87×10⁻⁵ /
  NS–BH 1.70×10⁻²); the fence's 95% convention
  (cap 0.193; HT 5.42×10⁻⁵) is carried as the stated
  alternative face (§4 gives the reason). The restated
  claims carry Arm 4's far-zone fence and the TW
  re-pricing, and Phase 306's promotion (§5).
- **Per-claim verdicts:** G32-E **SURVIVES RESTATED**;
  G32-F **SURVIVES RESTATED**; G32-G **SURVIVES
  RESTATED**. Nothing falls at this gate. What fell at
  Phase 307 stays fallen: the number 2.8044×10⁻⁵ as
  G32-F's value, and Phase 303 §4(ii)'s "consistent
  with" recording (its stated reason is also corrected,
  §6).

## §1. Controls (run before any re-judgement read)

The gate's own re-implementation (`g33_controls.py`)
reproduces the stored record exactly at stored
precision:
- **C1 (Phase 303, Corner B):** σ(0.17) = 2.9546×10⁻⁹;
  L7 α̂₁ = −7.9632×10⁻⁹; L8 α̂₂ = −9.9540×10⁻¹⁰;
  L9 = 7.3481×10⁻¹⁵; 𝒞 = 2.4632×10⁻³ (scalar) +
  4.9622×10⁻³ (vector); BBN read 0.125000 (saturating);
  c₋ = 0.16586208. Flat maximisers bind L9 at 0.10000
  at c_V = 1, 2, 10, with c₋ = 5.3136×10⁻⁶ /
  5.0886×10⁻⁵ / 1.5902×10⁻³ (Arm 2's table).
- **C2 (Phase 306):** σ_Gupta ratios 0.9456 / 0.8852 /
  0.9206; α̂₂ at Corner B under σ_Gupta =
  −1.2300×10⁻⁹ (stored −1.2300144×10⁻⁹);
  c_V(c₁₄*) = 3593.3548 (stored 3593.3549); the shrunk
  corner's c₋ is unchanged, 0.16586208.
- **C3 (Phase 307 Arm 1):** R = 0.9350, σ_rel = 0.132;
  cap 0.067 at n = 1, 0.1937 at n = 1.96; the fence's
  0.1 sits at n = 1.25σ; flat values by cap-linearity
  1.87×10⁻⁵ / 5.42×10⁻⁵ (Arm 1's stored digits).

## §2. Item 1 — the Corner B diagnosis

**The evidence base.** (i) Reconstruction from YBBY's
LaTeX source (`g33_ybby_reconstruction.md`): the
(c₊, c₋) presentation rests on §II's reduction — "we
can expand the theory in these quantities and shrink
the parameter space to just two parameters… to leading
order in α₁ and α₂. The only free parameters in
Einstein-Æther theory are then c±" (L669–L677, Eqs.
Aecons/Aecons2: c₂ = (−2c₁² − c₁c₃ + c₃²)/(3c₁),
c₄ = −c₃²/c₁); the stability bounds drawn with the
bands, 0 ≤ c₋ ≤ c₊/[3(1−c₊)], are likewise "to leading
order in α₁ and α₂" (L682–L690). The bands' shading
rule is existential in wording over masses, P_b,
(α₁, α₂) within Solar-System ranges
(|α₁| ≲ 10⁻⁴, |α₂| ≲ 10⁻⁷, L653) and EoS
sensitivities (L3022, L3116, L3124); the tex nowhere
states how σ is evaluated inside Eq. (191). (ii)
Extraction from the published figure files
(`g33_fig7_extraction.md`): Fig. 1's combined
binary-pulsar region is a wedge-blob from the origin
whose left boundary is the family's Cherenkov line
(drawn edge c₊ = 0.004671 at c₋ = 1.590×10⁻³ vs the
line's 0.004751 — coincident within a line width);
its c₋ extent is 2.0416×10⁻³ at its left edge and
3.1704×10⁻³ ± 2×10⁻⁵ globally; a literal slice at
c₊ = 0 meets it only at the origin. Corner B's
projection exceeds the drawn maximum by 0.16269
(8135σ) — Arm 2's break is confirmed as a statement
about the drawing. (iii) The gate's deciding
computation (`g33_diagnosis.py`):

**Part A — the family at the disputed point.**
Solving Aecons at (c₊, c₋) = (0, 0.16586208):
c₁ = 0.08293104, c₃ = −0.08293104, and
**c₂ = 0, c₄ = −0.08293104, c₁₄ = 0, identically**;
the α₁ and α₂ numerators (c₃² + c₁c₄) and
(c₁ + 2c₃ − c₄) both vanish exactly — the family
member is the α₁ = α₂ = 0 point with (c₂, c₁₄) =
(0, 0), where the mode speeds are singular
(w₀² ∝ c₂/c₁₄). The same holds along the entire
c₊ = 0 line: the family's c₊ = 0 slice is degenerate
at every c₋. Corner B departs from the family at
(c₂, c₁₄) = (2/21, 7.9×10⁻⁹),
(α₁, α₂) = (−3.16×10⁻⁸, −3.9500×10⁻⁹) — inside both
Solar-System ranges the bands vary over — and Phase
306's coordinate departs at (2/21, 6.4227×10⁻⁹),
(α₁*, α₂*) = (−2.5691×10⁻⁸, −3.2113×10⁻⁹), at the
same projection.

**Part B — YBBY's stated constraints at Corner B's
own parameters.** Eq. (191) for J1141−6545,
J0348+0432, J0737−3039, evaluated as a bound (dipole
term with X_sys ≤ 0.68·X_J1738 from the tex's stated
periods and a mass floor; (s₁−s₂)² bounded by
σ(C_* = 0.30, f = 1.3)² = (6.7782×10⁻⁹)²; quadrupole
deviation from the fence audit's Eq. (193) bound at
the point): the dipole term is ≤ 2.63×10⁻¹⁴ and the
quadrupole deviation ≤ 6.51×10⁻⁹, so
**|δṖ| ≤ 6.51×10⁻⁹ for all three systems** — a margin
of ≥ 1.54×10⁵ against δ_obs = 10⁻³, and ≥ 1.54×10⁴
even against a hypothetical δ_obs = 10⁻⁴ (below every
value in YBBY's sample; Eq. (190) characterises
δ_obs + δ_inf = O(10%)). Eqs. (194)–(195) against
YBBY's §VII B bounds (α̂₁ ≲ 10⁻⁵, α̂₂ < 1.8×10⁻⁴)
pass by ≥ 3.2 and ≥ 5.3 orders; against the tighter
§II bounds the fence adopts as L7/L8 (10⁻⁵, 10⁻⁹),
α̂₁ passes ×1.3×10³ and α̂₂ saturates — the fence's
own leg, not a band leg. Stability at the point in
the full theory passes (Phase 307 Arm 5: q_S = 24.0,
q_V = c₁₄ > 0, all speeds² > 0); the family's
Cherenkov edge, which closes the drawn wedge at
c₊ = 0, is a leading-order-in-α family bound, not
the full theory's condition at an off-family point.

**Part C — candidate (b) excluded.** At Corner B's
(α₁, α₂), the two σ evaluations on record (anchor
2.9546×10⁻⁹; Gupta PM 2.7200×10⁻⁹, ratio 0.9206)
differ by ≤ ×1.18 in any Ṗ_b read (≤ ×1.69 at the
bracket top f = 1.3) — four orders short of the
margins in Part B. The bands' σ is a family object
(§VI: sensitivities computed on the family, growing
with c₋ at Solar-System-saturating α's); it is not
evaluated at Corner B's α's anywhere in YBBY's
construction, and no σ evaluation at those α's can
manufacture the exclusion.

**Verdict: FENCE GOVERNS.** The drawn region's
exclusion of (0, 0.16586208) is the reduced family's
statement about its own degenerate member at that
plane point. Correctly understood — as an allowed set
of the small-α reduced family, in a plane that exists
only through that reduction — the projection does not
exclude Corner B (nor Phase 306's coordinate at the
same projection), because Corner B is not a member of
the family the region describes, and at its own
parameters every constraint YBBY state is satisfied.
Phase 303 §4(ii)'s bottom line (the bands are not this
fence, and are not to be read off at the corner) is
vindicated; its stated reason is not (§6).

## §3. Item 3 — the c_V = 10 maximiser's drawn read

Extraction at deciding grade from the published
figure files (vector data of Fig. 1's combined panel;
600-dpi raster of the four Fig. 7 panels; σ(c₋) =
±2×10⁻⁵, confirmed by two independent routes):
- **c₋ = 1.590×10⁻³ (c_V = 10 maximiser): INSIDE**
  the combined drawn region under the registered
  Arm-2 box semantics — the region spans
  c₊ ∈ [0.004671, 0.025653] at that c₋; margin
  +4.52×10⁻⁴ against the region's left-edge c₋ extent
  (2.0416×10⁻³) = 23σ (79σ against the global max).
  Inside all four Fig. 7 panels as drawn at that c₋
  (the binding right edge is J0737−3039's, 0.0252
  raster vs 0.025653 vector).
- c₋ = 5.089×10⁻⁵ (c_V = 2 maximiser): INSIDE the
  combined region (spans c₊ ∈ [1.328×10⁻⁴, 0.021588]
  at that c₋); the Fig. 7 panels' frames end at
  c₋ ≈ 7.5×10⁻⁴ and neither contain nor exclude it —
  the combined panel is the deciding drawn source.
- c₋ = 0.16586208 (Corner B): OUTSIDE, by 8135σ
  (the Item 1 subject; calibration cross-check PASS).
- **Wedge caveat, on the face:** the drawn region is
  a wedge whose left boundary is the reduced family's
  Cherenkov line; at exactly c₊ = 0 it contains only
  the origin, so no c₊ = 0 point — maximiser or
  corner — is a literal drawn member. Per §2, that
  literal reading is the family's degenerate-line
  artefact and applies to every GW-slice point
  equally; the registered semantics (c₋ against the
  region's c₋ extent, with the c₊ window stated) is
  the read the claim set carries.

## §4. Item 2 — the confidence convention

Arm 1 established that L9's cap is a confidence-level
statement: 0.067 at Eq. (190)'s own implicit
confidence (a linear sum of 1σ-class errors, with the
measured central offset R − 1 = −0.065 included);
0.193 at the fence's 95% convention (the convention of
L7/L8); the Gate-32 figure 0.1 sits at 1.25σ,
defensible at neither. **The gate fixes the quotable
form at the tolerance's own implicit confidence**
(cap 0.067; HT 1.87×10⁻⁵, NS–BH 1.70×10⁻²), for three
reasons: (i) a leg is quoted at the confidence its
own source attaches to it — Eq. (190) is a 1σ-class
tolerance, and restating it at 95% would change the
leg, not merely its reading; (ii) a re-issue must not
repair a broken value upward — the 95% face
(5.42×10⁻⁵) exceeds even the broken Gate-32 value,
and adopting it would raise the claim by convention
choice after the break; (iii) conservatism costs the
distance-0 claim nothing it needs — 1.87×10⁻⁵ clears
the registered bar ×18.7 at c_V = 2. The 95% face is
carried in G33-F as the stated alternative, not
suppressed: at a uniform 95% fence the cap would be
0.193 and the flat value HT 5.42×10⁻⁵ / NS–BH
4.91×10⁻².

## §5. The quotable claim set (the only quotable form)

Signalling channel only, in every claim: nothing here
moves matter, forms a geometry, or carries cargo;
ratios are theory-space-corner values for the stated
fiducial systems, not detections and not detectability
claims. G32-A, G32-D are untouched by Phase 307 and
this gate and stand as issued in Gate-32 §5; G32-B
stays failed; G32-C stands as promoted by Phase 306
(second-pathed σ). G32-E/F/G are superseded by:

- **G33-E — G32-E SURVIVES RESTATED.** *Corner B.*
  "At Corner B (c₁₄ = 7.9×10⁻⁹, c₂ = 2/21, c_V = 3240
  by construction), the spin-1 channel survives the
  completed fence at the central model, saturating
  BBN (margin 0) and the isolated-pulsar α̂₂ leg
  (α̂₂ = −9.954×10⁻¹⁰; that bound's own literature
  caveat — its direct mapping is declined by its
  source for want of the timed pulsars' masses —
  attached), and prices at HT ratio 2.0607×10⁻¹⁸ /
  NS–BH bound-class 1.8660×10⁻¹⁵, a factor ×3.01
  above the spin-0 row at the same (c₁₄, c₂) — the
  𝒞-ratio, in which the sensitivity cancels. The
  sensitivity is now second-pathed (Phase 306: Gupta
  et al.'s post-Minkowskian σ agrees with the rung-2
  anchor at ratio 0.9206 at this point). At the
  cross-checked σ the literal point's α̂₂ read is
  −1.2300×10⁻⁹ — inside the bracket span
  [−1.8818×10⁻⁹, −1.0902×10⁻¹⁰] Gate-32 disclosed —
  and the corner's second-pathed saturating
  coordinate is c₁₄* = 6.4227×10⁻⁹ (c_V = 3593.4 at
  fixed c₁), where α̂₂ = −10⁻⁹ exactly under
  σ_Gupta; the corner's survival is stated at that
  coordinate under the cross-checked σ. Projection
  read, carried on the face: YBBY's drawn combined
  region excludes this point's (c₊, c₋) projection
  (0, 0.16586208) — outside by 0.16269 at extraction
  grade (Gate-33 §3). Gate-33's diagnosis (§2) finds
  that region is the allowed set of YBBY's
  leading-order small-α reduced family, which
  degenerates at c₊ = 0 (its member at this
  projection is (c₂, c₁₄) = (0, 0)); Corner B is an
  off-family point, and at its own parameters every
  constraint YBBY state — Eq. (191) for
  J1141−6545/J0348+0432/J0737−3039
  (|δṖ| ≤ 6.51×10⁻⁹, margins ≥ 10⁴), Eqs.
  (194)–(195) against YBBY's stated α̂ bounds
  (margins ≥ 3 orders) — is satisfied. The projection
  read is therefore recorded as a reduced-family
  statement, not an exclusion of this point; it is
  carried here, not suppressed."
- **G33-F — G32-F SURVIVES RESTATED.** *The flat
  curve, at the data-grade cap.* "Maximising the
  spin-1 channel's dipole ratio over the completed
  fence gives **HT 1.87×10⁻⁵ and NS–BH bound-class
  1.70×10⁻² at c_V = 1, 2 and 10 alike**, quoted at
  the floor-binding maximisers (c₋ ≤ 1.59×10⁻³); the
  maximiser set is a ridge of equal values. The
  binding leg at every row is the dipole leg at its
  **data-grade cap 0.067** — YBBY Eq. (190)'s
  tolerance taken at its own implicit confidence (a
  linear sum of 1σ-class errors) with the measured
  J1738 central offset (Ṗ_b^Int/Ṗ_b^GR = 0.9350,
  Freire et al. 2012) included, per Phase 307 Arm 1;
  the maximised ratio is exactly linear in the cap,
  so flatness (speed-independence) is untouched by
  the re-pricing, and the value is unchanged with
  the scalar-Čerenkov edge held interior at
  δ = 10⁻³ (Arm 6, by the same linearity).
  Alternative face, stated not quoted: at the fence's
  95% convention the cap is 0.193 and the value
  would be HT 5.42×10⁻⁵ / NS–BH 4.91×10⁻²; Gate-32's
  2.8044×10⁻⁵ (cap 0.1, at 1.25σ) is superseded and
  is not quotable. The σ values at the maximisers
  are second-pathed (Phase 306: ratios 0.9456 at
  c_V = 2, 0.8852 at c_V = 10, inside
  f ∈ [0.7, 1.3]); at fixed cap the maximised value
  is invariant under σ's overall scale on the ridge
  (Gate-32 §3 skeleton), so the promotion raises the
  claim's grade, not its number, and the bracket
  envelope floor (HT ≥ 1.01×10⁻⁵ at c_V = 10) stands
  a fortiori with f_eff now measured in
  [0.885, 0.946]. The flatness mechanism stands as
  restated at Gate-32: no completed leg bounds c₁
  from above, so the vector speed, bought with c₁,
  carries no speed-for-coupling trade-off, while the
  cap is paid by the scalar sector through σ²𝒞.
  Drawn-band read (Gate-33 §3, deciding grade): the
  c_V = 10 maximiser's c₋ = 1.590×10⁻³ lies inside
  YBBY's combined drawn region under the registered
  box semantics (margin 23σ; inside all four Fig. 7
  panels at that c₋), superseding Phase 307 Arm 2's
  text-grade UNRESOLVED; at exactly c₊ = 0 the drawn
  wedge contains only the origin — the reduced
  family's degenerate-line artefact of Gate-33 §2,
  applying to every GW-slice point equally. Novelty:
  NOT FOUND IN OUR SEARCH for a published flat
  vector-mode dipole cap (Gate-32 §5, limits
  stated). **Fence (Arm 4, verbatim in substance):
  this value stands exactly and only where
  energy-balance/far-zone pricing is the correct
  Ṗ_b pricing.** Under Taherasghari & Will's
  near-zone coefficient (PRD 108, 124026 (2023);
  PRD 112, 024013 (2025)) — whose authors leave the
  discrepancy open, and which the post-GW pricing
  literature (Gupta et al. 2021; Vaglio et al. 2026,
  engaging TW explicitly) does not adopt — the rows
  re-price to HT 8.415×10⁻⁶ at c_V = 2 and
  8.42×10⁻⁸ at c_V = 10, and flatness itself
  disappears (the TW dipole falls as c_V⁻³); the
  c_V = 1 row is dispute-insensitive (coefficients
  agree to 0.2%)."
- **G33-G — G32-G SURVIVES RESTATED.** *Distance-0,
  with the speed asymmetry explicit.* "Inside the
  completed fence, with σ second-pathed (Phase 306)
  and the dipole leg at its data-grade cap (Phase
  307 Arm 1; Gate-33 §4), the Einstein-aether spin-1
  signalling channel meets the programme's registered
  bar (HT dipole ratio ≥ 10⁻⁶ at c_V ≥ 2) **at
  c_V = 2 under every pricing on record** — far-zone
  at the data-grade cap: 1.87×10⁻⁵ (×18.7 over the
  bar); far-zone at the 95% cap: 5.42×10⁻⁵;
  Taherasghari–Will near-zone pricing: 8.415×10⁻⁶
  (×8.4) — distance 0 at c_V = 2 unconditionally on
  pricing. **At c_V = 10 the bar is met under
  far-zone pricing only** (1.87×10⁻⁵ at the
  data-grade cap; 5.42×10⁻⁵ at 95%); under TW
  near-zone pricing the c_V = 10 row falls to
  8.42×10⁻⁸, below the bar — distance 0 at c_V = 10
  is conditional on energy-balance/far-zone pricing
  being the correct Ṗ_b pricing. This is a signalling
  channel in a surviving theory corner — not a
  drive, not transport, and not a detection claim."
  The Gate-32 §5 form of G32-G (quoting 2.8044×10⁻⁵
  at both speeds without the pricing asymmetry) is
  **not** quotable; this restated form is the only
  one.

## §6. Corrections to the record

- **Phase 303 §4(ii)** recorded the Fig. 7 bands as
  "consistent with, but is not, this phase's fence,"
  on the stated ground that "the bands were computed
  inside the fits' region." Both parts are corrected:
  the consistency recording falls for Corner B (the
  drawn region excludes its projection, §3), and the
  stated ground is not supported by YBBY's text — no
  sentence in §VII ties the bands to the Eq. (186)
  fits or their region; the fit region was chosen
  *because* it "will still be allowed after imposing
  binary pulsar constraints" (tex L2723–L2729), i.e.
  justified by the allowed region, not the other way
  round (reconstruction §6). The correct ground for
  not reading the bands off at the fence's points is
  Gate-33 §2's: the drawn regions are reduced-family
  objects.
- **Phase 307 Arm 2's break** is confirmed in its
  drawn statement (Corner B's projection is outside
  the combined drawn region, now at 8135σ extraction
  grade) and **not sustained** in its claim scope:
  at projection scope the exclusion binds the reduced
  family's member at the plane point, not Corner B
  (§2). Arm 2's named successor diagnosis is the one
  this gate executed; its other named items (pixel-
  grade digitisation — executed as Item 3; the
  off-surface EA cosmology MCMC) are unaffected.
- **Gate-32 §5's TW citation** (PRD 108, 102026) was
  already corrected by Phase 307 Arm 4 to **124026**;
  the restated claim set uses the corrected citation.

## §7. Reality Desk

`DESK: NO NEW DATA CONTACT — Gate-33 re-judged the
spin-1 record against its stored numbers, YBBY's
published LaTeX source and figure files
(arXiv:1311.7144 e-print), and the J1738+0333 Ṗ_b
datum already contacted by Phase 307 Arm 1 (Freire et
al. 2012). The one new fact is presentational and
deciding: YBBY's (c₊, c₋) plane is the leading-order
small-α reduced family, degenerate at c₊ = 0, which
resolves the bands-vs-fence discrepancy in the
fence's favour.`

## §8. What this gate did not do

No fresh TOV or post-Minkowskian σ computation was
run (Phase 306's cross-check is the σ second path and
stands). YBBY's numerical band computation was not
re-executed — the diagnosis rests on the construction
as stated in their text, the drawn geometry as
extracted from their figure files, and the gate's
evaluation of their stated constraints at the
disputed point; the existential scan over (α₁, α₂,
EoS) was not re-run, because Part B shows the point
itself satisfies every stated constraint, which is
the property the verdict turns on. The
Taherasghari–Will dispute was fenced, not adjudicated
(Arm 4's disposition stands). The off-surface EA
cosmology MCMC named by Phase 307 Arm 3 remains
unrun and is not decided here; Arm 3's two conditional
threats against Corner B remain recorded as
scope-shielded, neither activated nor discharged by
this gate. Nothing was published, forwarded, or
appended to the ledger; publication routing of the §5
claim set is the parent's, after this gate.
