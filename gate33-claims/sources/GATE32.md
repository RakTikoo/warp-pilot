# GATE-32 — ADVERSARIAL GATE ON PHASE 303: THE SPIN-1 FULL AUDIT

Date: 2026-11-24. Adversarial re-judgement, not a phase.
Scope, fixed in advance (`gate32/work/g32_registration.md`):
whether Phase 303's spin-1 (Einstein-aether vector mode) result —
σ_Æ at rung-2 grade, Corner A's σ-independent death, Corner B's
completed survival, and the flat spot rows HT 2.8044×10⁻⁵ at
c_V = 1, 2, 10 — survives independent attack, and in what wording
the Phase 304 distance-0 re-issue (ledger 757) may be quoted.
Frame of record: Phase 166 pin, venv python (numpy/scipy/sympy).
Method: the gate wrote its own machinery throughout —
`g32_t1_sympy.py` (structural re-derivation), `g32_controls_t4.py`
(controls + Corner A windows), `g32_t3_reimpl.py` (full-space
re-implementation of the spot rows; no import of Phase 303's
solver), `g32_t3b_leg_audit.md` (per-leg c₁ audit),
`g32_rung3_scope.md` (rung-3 executability evidence, extracted
from YBBY's full text), `g32_novelty.md` (novelty search,
primary sources first). The gate does not repair what it breaks;
the one repair is charged as a successor (§6).

## VERDICT

- **The Phase 304 distance-0 re-issue (ledger 757) STANDS
  RESTATED.** Its deciding numbers survive every attack the gate
  could execute: the flat value HT 2.8044×10⁻⁵ at c_V = 2 and 10
  was reproduced by an independent full-space optimiser
  (2.8045×10⁻⁵, rel. diff 2×10⁻⁵) and is forced algebraically
  once the dipole leg binds (§3); Corner A's death is verified
  σ-independent (§4). But the re-issue may be quoted **only** in
  the restated claim set of §5, because two parts of the
  Phase 303 framing failed the gate:
- **FAILED — the literature premise of Item 1.** Phase 303's
  framing that σ_Æ in the post-GW corner is "uncomputed in
  print," resting on OMW's 2018 deferral, is **false since
  2021**: Gupta, Herrero-Valea, Blas, Barausse, Cornish, Yagi &
  Yunes, *Class. Quantum Grav.* **38**, 195003 (2021)
  [arXiv:2104.04596] computed neutron-star sensitivities on the
  c₁₃ ≈ 0 slice precisely to fill OMW's deferral, by a
  post-Minkowskian method built because YBBY's direct method is
  numerically unstable in that region. Their σ is a function of
  (α₁, α₂, c_ω ≡ c₋; C_*) — i.e. the c₁-dependence Phase 303
  located "inside A" is, in the literature's working treatment,
  a computed dependence, not an open point. Phase 303's named
  open point ("σ_Æ at c₊ ≈ 0, c₋ ≳ 3×10⁻³ uncomputed in
  print") is **withdrawn**: c₋ is Gupta et al.'s free/scanned
  parameter (worked point c_ω = −0.1 at c_σ = 0); the gate's
  search could not enumerate every printed parameter tuple
  (Gupta §§5.3.2–7 only partially readable — see §5, novelty
  limits), so the withdrawal is stated as "not supported as a
  gap," which is enough to kill the claim as worded.
- **NOT EXECUTED — the rung-3 second path (G32-T2).** A fresh
  TOV integration cannot be executed from YBBY's published
  forms alone, for two material, evidenced reasons (§2): the
  EoSs are named and cited but nowhere specified in print, and
  14 of the 16 asymptotic coefficients in YBBY Eqs. (162)–(164)
  are withheld in print, so their matching conditions
  Eqs. (168)–(171) cannot be evaluated as printed. Per the
  registration this is a **scope limit, not a pass**: every
  claim resting on σ values is fenced to rung-2 grade in §5,
  and the literature's actual second path — Gupta et al.'s PM
  σ evaluated at the deciding points — is charged as the
  successor (§6), not run by this gate.
- **Per-claim verdicts (§5):** G32-A (structural σ) SURVIVES;
  G32-B (the "uncomputed in print" framing) **FAILS**;
  G32-C (σ values at the deciding points) SURVIVES IN RESTATED
  WORDING (rung-2 grade, Gupta cross-check outstanding);
  G32-D (Corner A dies, σ-independent) SURVIVES;
  G32-E (Corner B survives completed, ×3.01 pricing) SURVIVES
  IN RESTATED WORDING; G32-F (flat curve) SURVIVES IN RESTATED
  WORDING (mechanism restated: no leg bounds c₁ *from above*;
  the maximiser is a ridge, quoted at its floor-binding
  representatives); G32-G (distance-0) STANDS RESTATED as the
  claim set's head claim, in that set's wording only.
- **Novelty (exact categories, primary sources first; §5):**
  (a) a computed σ_Æ for the vector sector in the post-GW
  corner — **KNOWN** (Gupta et al. 2021). (b) dipole pricing of
  the spin-1 channel isolated at a completed fence — **NOT
  FOUND IN OUR SEARCH** (limits in §5; total-dipole pricing in
  the same corner is known — Gupta et al. 2021). (c) a
  speed-independent (flat) dipole cap for the vector mode —
  **NOT FOUND IN OUR SEARCH**. No first/unique wording is
  granted for (a) in any form.

## §1. Controls and structural re-derivation (G32-T1)

**Controls — all PASS, run before any attack read.** The gate's
fresh machinery reproduces Phase 303's stored deciding numbers:
X_J1738 = 7.255031×10⁵; Peters HT 7.7808×10²⁴ W, NS–BH
1.2696×10²⁵ W; Corner A 𝒞 = 2.666721×10⁴ (scalar piece
2.666700×10⁴, vector piece 2.108185×10⁻¹), σ(f) and L9/L7 reads
at f = 0.7/1/1.3 identical to the stored table (L9 = 0.15411 /
0.31451 / 0.53153); Corner B σ(0.17) = 2.9546×10⁻⁹,
α̂₂ = −9.9540×10⁻¹⁰ at f = 1.

**Structural derivation — PASS in full, including the part
Phase 303 asserted from the text.** The gate's own sympy script,
starting from OMW Eq. (1.1)'s general PPN forms, verifies
exactly (every difference simplifies to 0): α₁ = −4c₁₄ on the
slice; ∂α₂/∂c₁ = 0 identically; YBBY Eqs. (194)–(195) reduce to
OMW Eq. (3.24)'s slice forms; YBBY Eq. (108) → the khronometric
c_S² and Eq. (100) → c₁/c₁₄ on the slice; the Eq. (173)
extraction is Eq. (183) verbatim in form on the slice (ratio 1),
so σ's c₁-dependence can enter only through the integration
constant A; and the weak-field anchor's ∂s_wf/∂c₁ = 0, so at
anchor order σ_Æ = σ_Æ(c₁₄, c₂; C_*) exactly as Phase 303
derived. Item (e) of the test — the vector asymptotic — is
confirmed against the retrieved full text of YBBY Eq. (164):
w₁^∞ = {[A + 2(c₁₄−1)]/c₋}(M*/r) + O(M*²/r²), verbatim. **No
hole was found in Phase 303's structural derivation; Item 1's
algebra stands.** What failed is not the derivation but its
literature framing (§5, G32-B) and its grade (§2).

## §2. G32-T2 — rung 3: NOT EXECUTABLE from published forms

The extraction (`g32_rung3_scope.md`, from YBBY's full text)
establishes what print supplies. The reduced system is complete
in print: O(v⁰) TOV Eqs. (139)–(141) (only c₁₄ enters —
confirmed), the three-field O(v) system Eqs. (148)–(150) for
(k₁, s₁, w₁), centre data Eqs. (152)–(155) and (159)–(161), the
matching form Eqs. (167)–(171), the A-relation Eq. (172), the
extraction Eq. (173), and the definition Eq. (56) with its
equivalence proof (§III.B.1) — so no O(v²) mass computation
would be needed. Two material gaps stop execution as printed:

- **(G1) The EoS is not in print.** YBBY name four EoSs (APR,
  SLy, Shen, LS220) with citations and, for two of them, a
  thermodynamic slice — no table, parametrisation, variant, or
  interpolation for any of them. A fresh integration must import
  an external implementation whose variant YBBY do not pin
  down, with no printed checksum to validate it against.
- **(G2) The asymptotic matching cannot be evaluated as
  printed.** Of the 16 coefficients in the O(v) asymptotic
  expansions Eqs. (162)–(164), only s_A1 (Eq. 165) and s_c1
  (Eq. 166) are printed; the other 14 are expressly withheld
  ("lengthy and unilluminating"). The four matching conditions
  Eqs. (168)–(171) at finite r_b take those expansions as their
  right-hand sides. A fresh code must re-derive the series
  itself or fit A at leading order — either way it is no longer
  evaluating the published system as printed, which is what
  rung 3 was registered to be.

Secondary gaps (recorded, not deciding): ν″ and M″, needed by
Eq. (149), have no standalone printed formulae (derivable from
Eqs. 139/140); no numerical r_ε, r_b, or RK tolerances are
printed (bounded only by YBBY's <0.1% Fig. 5 check). An
aggravating fact from the novelty search: Gupta et al. (2021)
show YBBY's direct shooting (their Method 1) is **numerically
unstable in precisely the post-GW region** — the cancellation
σ ≈ Ãα₁/4 with Ãα₁ ≈ 0 — which is why the literature's working
computation in this corner is their post-Minkowskian Method 2,
not a TOV shooting. **Disposition: the rung-2 σ values
(σ = 2.5952×10⁻⁶ at the c_V = 2 maximiser, 3.2437×10⁻⁶ at
c_V = 10, 2.9546×10⁻⁹ at Corner B, all at C_* = 0.17, f = 1)
stand WITHOUT a second path from this gate. Every claim that
rests on them is fenced to rung-2 grade in §5, and the Gupta
cross-check is charged as the successor (§6).**

## §3. G32-T3 — the flat curve, re-implemented: value SURVIVES

The gate's optimiser (differential evolution + polish over the
full (c₁, c₂, c₁₄) space, the speed floor as a constraint —
Phase 303's solver fixed c₁ = c*²c₁₄ on a grid; this one does
neither) reproduces the flat value at both registered speeds:
**HT ratio 2.8045×10⁻⁵ at c* = 2 and at c* = 10** (rel. diff
2×10⁻⁵ against 2.8044×10⁻⁵, inside the registered 1%
tolerance), NS–BH 2.5395×10⁻², with L9 binding at 0.10000 at
both rows. The gate additionally exhibits *why* the value is
flat, in a form Phase 303 did not state: once L9 binds and σ is
anchor-linear in C_*, the maximised HT ratio is forced
algebraically — 0.1 × (ΔC_*/0.17)² × (X_HT/X_J1738) × (g/F)
= 2.8044×10⁻⁵ — independent of all couplings and of c*.
Flatness is therefore not a numerical coincidence of
Phase 303's grid; it is the skeleton of the registered fence +
fiducials.

Two mechanism corrections, both recorded in
`g32_t3b_leg_audit.md`:
1. **The maximiser is a ridge, not a point.** Free in c₁, the
   gate's optimiser reached the same ratio at c_V = 12.7
   (c* = 2) and c_V = 59.2 (c* = 10), with c₁₄ re-solving to
   hold σ²𝒞 at the L9 cap. Phase 303's statement "at fixed
   (c₂, c₁₄) the ratio only falls as c₁ grows" is locally true
   but the global maximiser set is the ridge. Phase 303's
   floor-binding maximisers are the ridge's conservative
   representatives — they minimise c₋ (≤ 1.59×10⁻³), while
   ridge points at large c₁ carry c₋ deep into the region
   where σ's strong-field value is least constrained
   (the gate's c* = 10 point: c₋ = 5.6×10⁻²). The quotable
   rows are therefore quoted at Phase 303's floor-binding
   maximisers, as tabulated there.
2. **"No leg prices c₁" is imprecise; the correct statement is
   "no leg bounds c₁ from above."** Per-leg audit: L1 fixes the
   combination c₁+c₃ only; L2, L3, L4 have no c₁-dependence on
   the slice (T1-exact); L5 (Čerenkov w₁² ≥ 1 ⇒ c₁ ≥ c₁₄) and
   L6 (spin-1 energy sign ⇒ c₁ > 0) touch c₁ directly but bound
   it **below**; L9 depends on c₁ through 𝒞's vector piece
   4/(3c₁₄w₁³), monotonically **decreasing** in c₁ (67% of 𝒞 at
   the c* = 1 maximiser, 20% at c* = 2, 0.2% at c* = 10) —
   again a lower-bound direction at fixed (c₂, c₁₄), never a
   cap. L7/L8 are c₁-independent at rung-2 grade (through the
   anchor); their c₁-independence is itself a rung-2 statement,
   since σ's strong-field c₋-dependence (Gupta et al.'s
   computed quantity) could in principle let the α̂ legs price
   c₁ at an order this gate did not evaluate. No leg caps c₁
   above and no leg prices c_V: **the flatness claim's
   substance stands; its wording is restated in §5.**

## §4. G32-T4 — Corner A's death: SURVIVES, σ-independent

Recomputed from the stored numbers (𝒞 = 2.666721×10⁴,
X_J1738 = 7.255031×10⁵, α₁ = −10⁻⁴): the dipole leg passes iff
σ(0.17) ≤ **5.7515×10⁻⁶**; the α̂₁ leg passes iff
σ(0.17) ∈ **[1.125014×10⁻⁵, 1.375017×10⁻⁵]**. The windows are
disjoint (gap factor 1.956), confirming Phase 303's 5.75×10⁻⁶
and [1.125, 1.375]×10⁻⁵. The gate's sweep over the full
bracket × compactness grid (f ∈ {0.7, 1, 1.3} ×
C_* ∈ {0.11, 0.17, 0.28}) finds **no point passing both legs**
— where one leg passes, the other fails — so the exclusion
holds for every σ value the registered fence model can
produce, and, as a statement about the two windows, for every
σ value whatsoever under the fence's registered reading: one
σ at the central compactness feeding both legs, the reading
Phases 292–303 apply throughout (both legs read
comparable-compactness neutron-star sensitivities through the
same anchor-shaped C_*-dependence). That shared-σ reading is
stated on the face of claim G32-D, as registered. **Corner A
is dead, killed by L9 (its scalar companion's dipole: vector
piece 0.211 of 𝒞 = 2.67×10⁴), and no sensitivity computation —
rung 3, Gupta's, or any other — can revive it, because the
exclusion is a property of the windows, not of σ's value.**

## §5. Novelty grades and the quotable claim set

**Novelty (G32-T5; full search record `g32_novelty.md` —
21 queries, primary sources read incl. OMW and Gupta et al. in
full text through §5.3.1):**
- (a) σ_Æ computed for the EA vector sector in the post-GW
  (c₁₃ = 0) corner: **KNOWN** — Gupta et al., CQG 38, 195003
  (2021). (Phase 303's specific presentation — the YBBY
  Eq. (184) anchor in (c₁₄, c₂) form with an assumed
  f ∈ [0.7, 1.3] bracket — is not Gupta et al.'s method; the
  category is nevertheless occupied, and no novelty wording
  attaches to it.)
- (b) Dipole pricing of the spin-1 channel, isolated, at a
  completed fence: **NOT FOUND IN OUR SEARCH** (limits:
  Gupta et al. §§5.3.2–7 only partially readable — mirror
  truncated, IOP paywalled — so printed parameter tuples could
  not be enumerated exhaustively; Vaglio et al. 2026 read in
  part; English-language web-index search, no INSPIRE/Web of
  Science forward-citation sweep). Total-dipole pricing in the
  same corner is KNOWN (Gupta et al. 2021, whose Eq. (35)
  dipole coefficient is explicitly a scalar c_S⁻³ piece plus a
  vector c_V⁻³ piece, priced as a sum; also Lin et al. 2019
  weak-field scaling, Zhang et al. 2020 generic formulas,
  Vaglio et al. 2026 J1738 re-pricing).
- (c) A speed-independent (flat) dipole cap for the vector
  mode: **NOT FOUND IN OUR SEARCH** (same limits). Published
  unconstrained-parameter statements concern c₋ (OMW; Gupta et
  al.), not c₁, and no published fence of the completed fence's
  composition was found at all.
- **Literature tension, recorded not adjudicated:**
  Taherasghari & Will (PRD 108, 102026 (2023); PRD 112,
  024013 (2025)) find the near-zone dipole depends only on the
  vector speed, in stated disagreement with the Foster/YBBY
  far-zone flux Phase 303 prices with. The post-GW literature
  that prices this corner (Gupta et al. 2021; Vaglio et al.
  2026) uses the far-zone coefficient; the gate registers the
  dispute as a rider on G32-F, it does not decide it.
- **Correction absorbed:** Foster (2007) did not compute
  sensitivities (his abstract says the opposite); YBBY (2014)
  were the first computation, pre-GW, on a hypersurface that
  collapses under the GW bound. No Phase 303 number rests on
  Foster; the correction is to the surrounding narrative only.

**The claim set — the only quotable form.** Signalling channel
only, in every claim: nothing here moves matter, forms a
geometry, or carries cargo; ratios are theory-space-corner
values for the stated fiducial systems, not detections and not
detectability claims.

- **G32-A — SURVIVES.** *Structure of σ_Æ on the slice.* On
  c₁₃ = 0, the strong-field PPN forms and the sensitivity
  extraction of Einstein-aether theory reduce exactly to their
  khronometric forms in (α₁, α₂) with α₁ = −4c₁₄ and α₂
  exactly c₁-independent (gate-verified symbolically,
  G32-T1); consequently σ_Æ at weak-field-anchor order is a
  function of (c₁₄, c₂; C_*) alone, and any c₁-dependence of
  σ_Æ enters only through the O(v) integration constant A —
  whose fixing system carries the vector asymptotic
  [A + 2(c₁₄−1)]/c₋ (YBBY Eq. 164, verbatim).
- **G32-B — FAILS.** *The framing "σ_Æ is uncomputed in print
  in the post-GW corner (OMW's deferral), with an open point
  at c₊ ≈ 0, c₋ ≳ 3×10⁻³."* Broken by Gupta et al. (2021),
  who computed σ_Æ on the c₁₃ ≈ 0 slice for both post-GW
  viable regions by a post-Minkowskian method, as a function
  of (α₁, α₂, c₋; C_*), three years before Phase 303. Any
  Phase 303/304 text carrying this framing is superseded by
  this gate; the open-point wording is withdrawn.
- **G32-C — SURVIVES IN RESTATED WORDING.** *σ_Æ values at
  rung-2 grade.* "At the deciding points of the spin-1 audit,
  the weak-field-anchor (YBBY Eq. 184) sensitivity at
  C_* = 0.17 is σ_Æ = 2.60×10⁻⁶ (flat-row maximiser,
  c_V = 2), 3.24×10⁻⁶ (c_V = 10) and 2.95×10⁻⁹ (Corner B),
  with the EA literature's strong-field bracket
  f ∈ [0.7, 1.3] carried on every downstream number. These
  are rung-2 (anchor-grade) values: no TOV second path exists
  from YBBY's printed forms (Gate-32 §2), and they have not
  been cross-checked against Gupta et al.'s (2021)
  post-Minkowskian σ_Æ, which is the literature's computed
  quantity in this corner and the named successor check."
- **G32-D — SURVIVES.** *Corner A is dead.* "Phase 298's
  Corner A (c_V = 63.2456 at c₁₄ = 2.5×10⁻⁵) is excluded by
  the completed fence independently of the sensitivity: the
  binary-pulsar dipole leg (J1738-class, YBBY Eq. 190's
  O(10%) tolerance) passes only for σ(0.17) ≤ 5.75×10⁻⁶ while
  the α̂₁ leg passes only for σ(0.17) ∈ [1.125, 1.375]×10⁻⁵ —
  disjoint windows (gate-recomputed), under the fence's
  registered reading of one central-compactness sensitivity
  feeding both legs. The killing mechanism is the corner's
  scalar companion mode: the vector piece is 0.211 of
  𝒞 = 2.6667×10⁴. Corner A is quotable only as a dead
  corner."
- **G32-E — SURVIVES IN RESTATED WORDING.** *Corner B.*
  "At Corner B (c₁₄ = 7.9×10⁻⁹, c₂ = 2/21, c_V = 3240 by
  construction), the spin-1 channel survives the completed
  fence at the central model, saturating BBN (margin 0) and
  the isolated-pulsar α̂₂ leg (α̂₂ = −9.954×10⁻¹⁰; that
  bound's own literature caveat — its direct mapping is
  declined by its source for want of the timed pulsars'
  masses — attached), and prices at HT ratio 2.0607×10⁻¹⁸ /
  NS–BH bound-class 1.8660×10⁻¹⁵, a factor ×3.01 above the
  spin-0 row at the same (c₁₄, c₂) — the 𝒞-ratio, in which
  the sensitivity cancels. The survival is stated at rung-2
  σ grade (G32-C): across the σ bracket the corner's α̂₂ read
  spans [−1.8818×10⁻⁹, −1.0902×10⁻¹⁰], and σ at its
  c₋ = 0.166 has not been cross-checked against Gupta et al.
  (2021)."
- **G32-F — SURVIVES IN RESTATED WORDING.** *The flat curve.*
  "Maximising the spin-1 channel's dipole ratio over the
  completed fence gives HT 2.8044×10⁻⁵ and NS–BH bound-class
  2.5394×10⁻² at c_V = 1, 2 and 10 alike (gate-reproduced at
  2.8045×10⁻⁵ by an independent optimiser), quoted at the
  floor-binding maximisers (c₋ ≤ 1.59×10⁻³); the maximiser
  set is a ridge of equal values. The binding leg at every
  row is the dipole leg at its limit — YBBY Eq. (190)'s
  O(10%) tolerance, an order-of-magnitude-tolerance bound
  whose character every row inherits. The flatness mechanism,
  restated: no completed leg bounds c₁ from above (the legs
  that touch c₁ — Čerenkov and the energy-sign leg — bound it
  below; the dipole leg's c₁-dependence decreases its flux
  coefficient as c₁ grows), so the vector speed, bought with
  c₁, carries no speed-for-coupling trade-off at rung-2 σ
  grade, while the cap is paid by the scalar sector through
  σ²𝒞. Envelope over the σ bracket: HT ≥ 1.01×10⁻⁵ at
  c_V = 10. Novelty: NOT FOUND IN OUR SEARCH for a published
  flat vector-mode dipole cap (Gate-32 §5, limits stated).
  Rider: the pricing uses the YBBY far-zone flux, whose
  near-zone counterpart is disputed by Taherasghari & Will
  (2023, 2025); the post-GW pricing literature (Gupta et al.
  2021; Vaglio et al. 2026) uses the far-zone coefficient."
- **G32-G — STANDS RESTATED (the distance-0 re-issue, ledger
  757).** "Inside the completed fence as modelled at rung-2
  σ grade, the Einstein-aether spin-1 signalling channel
  meets the programme's registered bar (HT dipole ratio
  ≥ 10⁻⁶ at c_V ≥ 2) at c_V = 2 and c_V = 10, at ratio
  2.8044×10⁻⁵ — distance 0 — by saturating a tolerance-grade
  bound (YBBY Eq. 190's O(10%)), with the σ values carrying
  the f ∈ [0.7, 1.3] bracket and the Gupta et al. (2021)
  cross-check outstanding. This is a signalling channel in a
  surviving theory corner — not a drive, not transport, and
  not a detection claim." The unqualified form of ledger 757
  (which inherits Phase 303's G32-B framing by reference) is
  **not** quotable; this restated form is the only one.

## §6. Successor charged (not run by this gate)

**Phase 305 — the Gupta cross-check.** Evaluate σ_Æ at the
deciding points (the flat rows' floor-binding maximisers at
c_V = 2 and 10; Corner B) from Gupta et al.'s (2021)
post-Minkowskian formulas and printed results (their
Eqs. 52–57, 75–76 and §5, APR4 EoS as tabulated), reading
§§5.3.2–7 in full — which also closes the novelty search's
one open enumeration gap. Compare against G32-C's rung-2
values inside f ∈ [0.7, 1.3]. Outcomes: agreement inside the
bracket promotes G32-C/E/F to second-pathed grade; a deciding
point outside the bracket re-decides Corner B's α̂₂ saturation
and the flat rows' L7/L8 near-bindings at the cross-checked σ,
and the affected claims return to a gate. Until Phase 305
lands, the claim set of §5 is quoted exactly as fenced there.

## §7. Reality Desk

`DESK: NO DATA CONTACT beyond the fences already applied in
Phases 291–303 — Gate-32 re-judged the spin-1 record against
its own stored numbers and the published literature; the one
new literature fact is bibliographic (Gupta et al. 2021
computed the sensitivity Phase 303 treated as uncomputed),
and it fences the claim set's wording, not any datum.`

## §8. What this gate did not do

No TOV integration was run (§2 states why none can be run
from print as printed). No Gupta-formula evaluation was run —
that is the charged successor, not gate work. The
Taherasghari–Will dispute was registered, not adjudicated.
Nothing was published, forwarded, or appended to the ledger;
publication routing of the §5 claim set is the parent's,
after this gate.
