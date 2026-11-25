# PHASE 303 — CHECKPOINT: THE SPIN-1 FULL AUDIT

**Registration:** `phase303/work/p303_registration.md`
(ledger entry 750's charge; verdict forms carried verbatim
from entry 750, written before any computation).
**Deliverable:** `phase303/results/p303_memo.md`.
**Work:** `phase303/work/p303_audit.py` + `.out` (symbolic
identities, machinery controls, fence tables at the
corners), `phase303/work/p303_pricing.py` + `.out` (Peters
controls, corner pricing, spot-row maximisation, envelope).
Desk/analysis phase; light VM compute; no launches, no
ledger append.

## What was done

1. **Controls first (all PASS).** C-A: Phase 298's
   `p298_row2.py` re-run reproduces its stored `.out`
   exactly (Corner A c_V = 63.2456, Corner B c_V = 3240
   under the applied fence, diff-0). C-B (sympy): YBBY
   Eqs. (194)–(195) reduce exactly to OMW Eq. (3.24)'s
   slice forms; YBBY Eq. (108) → khronometric c_S² and
   Eq. (100) → c₁/c₁₄ on the slice; the EA extraction
   Eq. (173) ≡ khronometric Eq. (183) in form on the slice.
   Machinery controls reproduce Phase 294's C3
   (7.8606×10⁻¹² vs 7.8608×10⁻¹²) and leg-9 binding value
   (9.99934×10⁻² vs 9.99953×10⁻²) at diff-0-class; Peters
   controls exact (HT 7.7808×10²⁴ W; NS–BH 1.2696×10²⁵ W).
2. **Item 1 — σ_Æ at rung-2 grade.** YBBY retrieved in full
   (EA sector). Structural read decides: the O(v⁰) system
   depends only on c₁₄ (§VI A); the weak-field anchor
   (Eq. 184) runs through (α₁, α₂) only, hence on the slice
   σ_Æ = σ_Æ(c₁₄, c₂; C_*) with s = −(α₁ − (2/3)α₂)(3/5)C_*,
   σ = s/(1−s) — at Corner A σ(0.17) = 1.0200×10⁻⁵, at
   Corner B 2.9546×10⁻⁹ (= Phase 292's σ at the same
   (c₁₄, c₂)). The structural difference from spin-0 is
   derived, not assumed: the α̂ and extraction *forms*
   coincide on the slice, but the integration constant A is
   fixed by a three-field system whose vector asymptotic
   carries [A + 2(c₁₄−1)]/c₋ — σ's c₁-dependence lives
   inside A. Bracket: the EA literature's own stated
   strong-field deviation, 15–30% (Fig. 3), f ∈ [0.7, 1.3]
   (replacing Phase 292's khronometric [0.5, 2] per the
   registration). **Where it opens, named:** σ_Æ at
   c₊ ≈ 0, c₋ ≳ 3×10⁻³ is uncomputed in print (fits stop at
   c₋ = 3×10⁻³, c₊ ≥ 3×10⁻⁴; Fig. 4 at c₊ ∈ {0.1, 1});
   rung 3 (fresh TOV of the published three-field system)
   named, NOT run — rungs 1–2 decide Item 2 (see 3).
   Fits retrieved (Eq. 186/Table I; Appendix C Eq. C1),
   region respected, evaluated nowhere.
3. **Item 2 — the completed fence.** Legs L7 (|α̂₁| ≤ 10⁻⁵),
   L8 (|α̂₂| ≤ 10⁻⁹, isolated-pulsar caveat carried as
   Phase 292 carried it) and L9 (dipole, J1738-class,
   YBBY Eq. 190's O(10%) tolerance, EA 𝒞 of Eq. 114)
   applied with Item 1's σ. **Corner A DIES:** L9 =
   0.15411 / 0.31451 / 0.53153 at f = 0.7 / 1 / 1.3 (limit
   0.1); L7 concurs at f ≲ 1.22 (1.8400×10⁻⁵ central). The
   exclusion is σ-independent: L9 needs σ(0.17) ≤
   5.75×10⁻⁶, L7 needs σ(0.17) ∈ [1.125, 1.375]×10⁻⁵ —
   disjoint windows, so no sensitivity value (rung 3
   included) revives the corner. Mechanism: 𝒞 at A is
   2.666721×10⁴ of which the scalar piece is 2.666700×10⁴
   and the vector piece 0.211 — the corner is killed by its
   scalar companion's dipole (⟨𝒜⟩_dip ∝ c₁₄ along the
   w₀ = 1 edge), not by the vector mode's. **Corner B
   SURVIVES at the central model:** L7 inert
   (7.9632×10⁻⁹), L8 saturating (α̂₂ = −9.9540×10⁻¹⁰),
   L9 inert (7.3481×10⁻¹⁵), BBN saturating at margin 0 —
   Phase 292's shrunk corner's status inherited, with its
   caveats (α̂₂ bracket span [−1.8818×10⁻⁹, −1.0902×10⁻¹⁰];
   σ at c₋ = 0.166 uncomputed in print).
4. **Item 3 — pricing.** Corner B (c_V = 3240): HT ratio
   2.0607×10⁻¹⁸ (P_dip 1.6034×10⁷ W), NS–BH 1.8660×10⁻¹⁵
   (2.3690×10¹⁰ W), central; envelope ∝ f². That is ×3.01
   the spin-0 row's price at the same (c₁₄, c₂) — the
   vector piece of 𝒞 (4.9622×10⁻³) added to the shared
   scalar piece (2.4632×10⁻³). Spot rows (maximise ratio
   s.t. c_V ≥ c*, completed fence): **flat** — HT
   2.8044×10⁻⁵, NS–BH 2.5394×10⁻² at c* = 1, 2, 10 alike
   (L9 binding at each; maximisers on the w₀ ≈ 1 edge at
   c₁₄ = 2.6568 / 6.3608 / 7.9511×10⁻⁶, c₋ ≤ 1.590×10⁻³).
   Envelope: f = 1.3 reproduces the flat values; f = 0.7
   cuts the c* = 2, 10 rows via L7 to 1.2598×10⁻⁵ /
   1.0099×10⁻⁵ — HT ≥ 1.01×10⁻⁵ at c_V = 10 across the
   bracket, vs the spin-0 row's 2.374368×10⁻¹¹ there.

## Verdicts

- **Item 1:** σ_Æ computed at rung-2 grade; open point
  named (c₊ ≈ 0, c₋ ≳ 3×10⁻³); rung 3 named, not run.
- **Item 2:** Corner A — **DIES AT COMPLETION** (killing
  leg L9, dipole; mechanism on the memo's face). Corner B
  — **SURVIVES COMPLETED** (central model; BBN + L8
  saturating; caveats attached).
- **Item 3:** **CHANNEL PRICED** (Corner B + flat spot
  rows; §3 of the memo).
- **Row: SURVIVES COMPLETED** (ledger 750's form), with
  Corner A's death as the completion's cost. Phase 298's
  OUTRUNS witness (Corner A) is withdrawn; the row's
  outrunning now rests on the flat spot-row curve
  (×1.18×10⁶ the spin-0 price at speed 10) and Corner B's
  ×3.01 — quote those, never Corner A.
- **DESK:** `DESK: Einstein-aether spin-1 (vector) signal channel — SURVIVES the completed fence (sigma_AE = YBBY Eq. (184) anchor, EA bracket f in [0.7,1.3]; strong-field sigma at c+~0, c- > 3e-3 uncomputed in print, rung-3 TOV named not run): Corner A (c_V = 63.2456 at c14 = 2.5e-5) DIES AT COMPLETION by the binary-pulsar dipole leg (x1.54-5.32 over across the bracket; no sigma value passes both the dipole and alpha-hat-1 windows), killed by its scalar companion's dipole (vector piece 0.21 of C = 2.67e4); Corner B SURVIVES COMPLETED at the central model (c_V = 3240; BBN + isolated-pulsar alpha-hat-2 saturating, that bound's caveat attached), priced HT 2.0607e-18 / NS-BH 1.8660e-15 (x3.01 the spin-0 price at the same point); spot rows FLAT at HT 2.8044e-5 / NS-BH 2.5394e-2 for c_V = 1, 2, 10 (envelope HT >= 1.01e-5 at c_V = 10) — the speed lives in c1, which no completed leg prices.`

## Standing

- The W-i census's last unpriced row is now priced. Of the
  extra modes of the surviving Lorentz-violating gravity
  theories, the spin-1 row is the only one whose completed
  fence does not tax speed: its trade curve is flat at the
  dipole cap's height (HT 2.8044×10⁻⁵) across the
  registered rows, because the cap is paid by the scalar
  sector's c₁₄ while the speed is bought with c₁. Its top
  speed corner (B, c_V = 3240) stands exactly where the
  spin-0 row's fastest corner stands — saturating the same
  two fences in the same (c₁₄, c₂) plane — at ×3.01 the
  price.
- Remaining softness, named (memo §4): σ_Æ's strong-field
  value at c₊ ≈ 0, c₋ ≳ 3×10⁻³ is the one input no
  publication supplies; a rung-3 TOV integration of YBBY's
  published system would re-decide Corner B's saturation
  margin and the spot rows' L7/L8 near-bindings at better
  than bracket grade, but cannot revive Corner A (its
  exclusion is σ-independent) and cannot move the flat
  curve's height by more than the bracket's factor ~2.8
  (the f = 0.7 L7 cut). Corner A joins Phase 298's record
  as a dead corner: quote it only as one.
- No claim from this phase joins any publication queue: it
  completes a census row's fence and prices its channel,
  in the Phase 292 pattern. Quote Corner B only with its
  saturating legs and the α̂₂ caveat attached; quote the
  spot rows only with L9 and its O(10%)-tolerance character
  attached (and L8's caveat at c* = 1, 10, where it is
  near-binding).
