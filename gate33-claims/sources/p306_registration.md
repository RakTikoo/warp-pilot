# PHASE 306 — REGISTRATION (written before any Gupta evaluation)

**Charge:** ledger entry 760 (parent). Gate-32 §6's charged
successor, renumbered 306 (Phase 305 is the instrument phase).
**Task:** the independent-method second path for the spin-1
sensitivity values Gate-32 could not second-path from YBBY's
printed forms: evaluate Gupta et al.'s (2021)
post-Minkowskian σ_Æ at Phase 303's deciding points and
compare against the rung-2 (YBBY Eq. 184 anchor) values
inside the registered bracket f ∈ [0.7, 1.3].

## The values under test (G32-C, C_* = 0.17, f = 1)

From gate32/GATE32.md §2/§5 and phase303/results/
p303_memo.md §3.2 (floor-binding maximisers) and §2.2
(Corner B):

| Point | (c₁, c₂, c₁₄) | c₋ | rung-2 σ_Æ |
|---|---|---|---|
| Flat-row maximiser, c_V = 2 | (2.5443×10⁻⁵, 6.3620×10⁻⁶, 6.3608×10⁻⁶) | 5.089×10⁻⁵ | 2.5952×10⁻⁶ |
| Flat-row maximiser, c_V = 10 | (7.9511×10⁻⁴, 7.9621×10⁻⁶, 7.9511×10⁻⁶) | 1.590×10⁻³ | 3.2437×10⁻⁶ |
| Corner B | (0.08293104, 2/21, 7.9×10⁻⁹) | 0.16586208 | 2.9546×10⁻⁹ |

## Parameterisation conversion (Gupta et al.'s own
## definitions, §2, as verified in gate32/work/g32_novelty.md)

Gupta et al. use (c_θ, c_σ, c_ω, c_a) with
c₁ = (c_ω + c_σ)/2, c₃ = (c_σ − c_ω)/2, c₂ = (c_θ − c_σ)/3,
c₄ = c_a − (c_σ + c_ω)/2. Hence on the slice c_σ = c₁₃ = 0:

    c_a = c₁₄,   c_ω = c₋ = 2c₁ (slice),   c_θ = 3c₂,
    α₁ = −4c₁₄,
    α₂ = c₁₄(c₁₄ + 2c₂c₁₄ − c₂)/[c₂(2 − c₁₄)]   (OMW Eq. 3.21)

Gupta's σ is a function of (α₁, α₂, c_ω; C_*); their
extraction is σ = 2Ãα₁/(α₁ + 8) (their Eq. 57), Method 2
(post-Minkowskian) Ã from their Eq. 75, weak-field limit
their Eq. 76: s_wf = (α₁ − (2/3)α₂)·Ω/M_*.

Converted deciding points (computed in the evaluation
script, printed there, not by hand):

| Point | α₁ | α₂ | c_ω | c_θ | c_a |
|---|---|---|---|---|---|
| c_V = 2 max | −4c₁₄ = −2.54432×10⁻⁵ | from Eq. 3.21 | 5.089×10⁻⁵ | 3c₂ = 1.90860×10⁻⁵ | 6.3608×10⁻⁶ |
| c_V = 10 max | −3.18044×10⁻⁵ | from Eq. 3.21 | 1.590×10⁻³ | 2.38863×10⁻⁵ | 7.9511×10⁻⁶ |
| Corner B | −3.16×10⁻⁸ | −3.95×10⁻⁹ (Phase 298) | 0.16586208 | 2/7 = 0.285714 | 7.9×10⁻⁹ |

## Overlap control (runs before any comparison is quoted)

Gupta's Eq. (76) weak-field limit IS the YBBY Eq. (184)
anchor in (α₁, α₂) form (gate32 novelty file: the anchor is
Gupta's O(C¹) term). Control: Eq. (76) evaluated at Corner
B's (α₁, α₂) with the programme's Ω/M_* = −(3/5)C_*
convention (C_* = 0.17) must reproduce the shared
khronometric value σ = 2.9546×10⁻⁹. If it does not, the
discrepancy is reported BEFORE any Gupta-vs-rung-2
comparison is quoted, and the comparison proceeds only with
the discrepancy's cause identified (convention, EoS
Ω/M_*, or formula difference). The realistic-EoS (APR4)
Ω/M_* vs uniform-density −(3/5)C_* difference is a known
convention gap, carried explicitly: it is part of what the
f-bracket was absorbing, and it is reported, not hidden.

## Evaluation scope discipline

Gupta's numbers are used only inside their stated method
scope: Method 2 is a post-Minkowskian expansion in
compactness (background not expanded), truncated at the
order they fixed by matching Method 1 where Method 1 is
stable; APR4 EoS. Where a deciding point sits outside the
regime their printed results cover (their two viable
regions; their printed tuples), that is reported as a
coverage fact, and the formula evaluation is labelled as
such — a formula evaluated is not a printed tuple.

## Verdict forms (registered, ledger 760 — verbatim)

- **AGREEMENT** — all deciding points inside the bracket
  f ∈ [0.7, 1.3] (σ_Gupta/σ_rung2 ∈ [0.7, 1.3] at every
  deciding point): the memo states the promotion — G32-C/E/F
  to second-pathed grade by independent method — and quotes
  the compared values.
- **MISS** — any deciding point outside the bracket:
  re-decide with Gupta's σ — Corner B's α̂₂ saturation first
  (does Corner B still survive?), then the flat rows' L7
  cuts (does the flat value 2.8044×10⁻⁵ stand, move, or
  fall?); the distance-0 wording of GATE32 §5 is re-issued
  or withdrawn accordingly, in the memo's own restated text.
- **GUPTA'S RESULTS DO NOT COVER THE DECIDING POINTS** —
  the coverage gap stated exactly (which parameter region
  is missing); the claims then stand single-pathed at
  rung-2 grade with that fence stated.

## Also charged

Close Gate-32's novelty-enumeration gap: read Gupta
§§5.3.2–7 in full and state which printed (α₁, α₂, c_ω)
tuples exist (σ curves / figures / tables), so the novelty
record can say what was actually enumerated.

## Standing rules

No novelty wording for the σ computation in any form
(KNOWN, Gupta 2021, per Gate-32). DESK: one-line summary.
No ledger append, no launches, no user contact.
Deliverable: phase306/CHECKPOINT306.md +
phase306/results/p306_memo.md.
