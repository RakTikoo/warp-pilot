# PHASE 306 — CHECKPOINT: THE GUPTA CROSS-CHECK

**Registration:** `phase306/work/p306_registration.md`
(ledger entry 760's charge; verdict forms fixed before
any Gupta evaluation). Gate-32 §6 charged this work as
its successor under the number 305; renumbered 306 by
the parent (Phase 305 is the instrument phase).
**Deliverable:** `phase306/results/p306_memo.md`.
**Work:** `phase306/work/p306_eval.py` + `.out`
(controls, C↔Ω transcription cross-check, main
evaluation, compactness sweep), `phase306/work/
p306_cornerB.py` + `.out` (Corner B α̂₂ under σ_Gupta;
shrunk corner), `phase306/work/
p306_gupta_eq80_source.txt` (the deciding equation
verbatim from the arXiv LaTeX source). Desk/retrieval
phase; light VM compute; no launches, no ledger append.

## What was done

1. **Retrieval (Item 1).** Gupta, Herrero-Valea, Blas,
   Barausse, Cornish, Yagi & Yunes, CQG 38, 195003
   (2021) [arXiv:2104.04596 **v2**] retrieved IN FULL —
   arXiv PDF and e-print LaTeX source — closing the
   readability gap Gate-32 recorded. Their σ apparatus:
   extraction σ = 2Ãα₁/(α₁ + 8) (Eq. 58); Method 2
   (post-Minkowskian) Ã series with Ã₁ = 0 identically
   (Eq. 76); weak-field limit Eq. (77) = the YBBY
   Eq. (184) anchor as its O(𝒞¹) term; the closed-form
   Tolman VII sensitivity s(𝒞) through O(𝒞³),
   Eq. (80), adopted by the authors for all their
   constraint work. **Enumeration closed:** exactly
   three printed σ tuples exist — Fig. 1
   (10⁻⁴, 4×10⁻⁷, c_ω = −0.1; field plot, no σ curve),
   Fig. 2 APR4 (10⁻⁴, 4×10⁻⁷, c_ω = 10⁻⁴, c_σ = 0;
   σ(𝒞) at PM orders 1–3 vs Method 1), Fig. 3 Tolman
   VII + 6 EoSs (−10⁻⁴, −4×10⁻⁷, c_ω = 10⁻³;
   universality < 3%). §§6–7 print no further tuples —
   §6 evaluates the same analytic σ continuously over
   its prior box (α₂ ∈ [−4×10⁻⁷, 4×10⁻⁷],
   c_ω ∈ [−10⁵, 10⁵]).
2. **Conversion + controls (Item 2a) — all PASS.**
   Deciding points converted via Gupta's §2 map
   (c_a = c₁₄, c_ω = 2c₁, c_θ = 3c₂, α₁ = −4c₁₄,
   α₂ per OMW Eq. 3.21). The anchor evaluated from the
   converted (α₁, α₂) reproduces G32-C's values at
   ≤ 9.6×10⁻⁶ relative. **Overlap control:** Gupta's
   Eq. (77) at Corner B with the programme's
   Ω/M_* = −(3/5)C_* gives σ = 2.9546×10⁻⁹ — exactly
   the khronometric value both records share. Corner
   B's converted α₂ = −3.9500×10⁻⁹ reproduces
   Phase 298's printed value.
3. **Evaluation (Item 2b).** Eq. (80) transcribed from
   the LaTeX source and cross-checked against the
   independently transcribed Ω-form Eq. (82) via
   Eq. (81): agreement 1.9×10⁻⁸ (Corner B), 2.1×10⁻³
   (c_V = 10), 5.0×10⁻² (c_V = 2 — the two series'
   truncation scales; both forms inside the bracket
   everywhere). Two source typos found and resolved on
   the record (the Ω-form's (3α₁ + 2α₂) leading sign;
   a dropped "+" in the 𝒞-form's final summand) —
   neither moves any verdict. At 𝒞 = 0.17:
   **σ_Gupta = 2.4539×10⁻⁶ (c_V = 2 maximiser),
   2.8713×10⁻⁶ (c_V = 10 maximiser),
   2.7200×10⁻⁹ (Corner B)** — ratios to rung-2
   **0.9456 / 0.8852 / 0.9206**, all inside
   f ∈ [0.7, 1.3]. Term structure: 𝒞¹ = anchor × 25/21
   (Tolman VII Ω/M_* vs uniform-density), 𝒞² removes
   ≈ 32% of leading, 𝒞³ returns 6–11%. Supplementary:
   ratios stay in [0.76, 1.01] over 𝒞 ∈ [0.11, 0.28].
4. **Coverage.** The closed form covers all deciding
   points: Corner B inside Gupta's region (ii)
   (c_a ≲ 10⁻⁷, c_θ = 2/7 ≲ 0.3); the maximisers on
   the region-(i) ray c_θ ≈ 3c_a at c_a ~ 10⁻⁵,
   between the named regions, inside the (α₂, c_ω)
   domain §6 exercised. Formula evaluations, labelled
   as such — no printed curve sits at the maximiser
   tuples. Method scope stated in the memo §4
   (O(𝒞⁴) truncation; singular limits avoided at the
   deciding points, evidenced by the cross-form
   agreements; Tolman VII representativeness is the
   source's own < 3% universality claim).

## Verdict

- **AGREEMENT** (ledger 760, form 1). **G32-C, G32-E
  and G32-F are promoted to second-pathed grade by
  independent method** (Gupta et al.'s post-Minkowskian
  σ vs the YBBY-anchor rung-2 values), in Gate-32 §5's
  restated wording; G32-G inherits through G32-F.
- **Consequence on G32-E, quantified:** at σ_Gupta,
  Corner B's literal α̂₂ read is −1.2300×10⁻⁹ (23%
  over the bound) — a bracket-interior σ (f_eff =
  0.9206), inside the span G32-E already discloses.
  The shrunk corner, solved exactly with σ from
  Eq. (80): **c₁₄* = 6.4227×10⁻⁹** (×0.8130), where
  α̂₂ = −10⁻⁹, σ_Gupta = 2.2113×10⁻⁹ and c_V = 3593.4
  at fixed c₁. Corner B's survival is unchanged; its
  saturating coordinate is now second-pathed.
- **Not touched:** G32-A (structure), G32-B (failed
  framing — stays failed), G32-D (Corner A's
  σ-independent death). The flat rows' full fence
  re-run under σ_Gupta as a function is named in the
  memo as the remaining non-deciding refinement, not
  run (not charged by the AGREEMENT branch).
- **DESK:** `DESK: NO DATA CONTACT beyond the fences
  already applied in Phases 291–303 — Phase 306
  cross-checked the spin-1 record's sensitivity values
  against Gupta et al. (2021)'s published
  post-Minkowskian computation (ratios 0.9456 / 0.8852
  / 0.9206 at the three deciding points, all inside
  the registered bracket); the contact is
  bibliographic and methodological, not a new datum.`

## Standing

- The spin-1 claim set's last outstanding item from
  Gate-32 §6 is discharged: the σ values at the
  deciding points are no longer single-pathed. The
  claim set of GATE32 §5 is quotable in its restated
  wording, now at second-pathed σ grade, with
  Corner B's saturating coordinate read as
  c₁₄* = 6.4227×10⁻⁹ under the cross-checked σ (the
  literal 7.9×10⁻⁹ point's α̂₂ status under σ_Gupta is
  stated in the memo §5, not smoothed over).
- No novelty wording attaches to the σ computation in
  any form (KNOWN, Gupta et al. 2021, per Gate-32).
  Nothing was published, forwarded, or appended to the
  ledger; publication routing remains the parent's.
