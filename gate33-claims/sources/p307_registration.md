# PHASE 307 — REGISTRATION: BREAK THE CHANNEL (red team on the spin-1 result)

Written before any arm is run. Charge: ledger entry 761.
Frame of record: Phase 166 pin, venv python. Controls (run by the
coordinator before this registration was finalised): Phase 303's
`p303_pricing.py` re-run reproduces Corner B HT 2.0607×10⁻¹⁸ and the
flat rows HT 2.8044×10⁻⁵ / NS–BH 2.5394×10⁻² exactly
(`phase307/work/p307_controls_pricing.out`); `p303_audit.py` re-run
reproduces the stored fence tables including Corner A's L9 reads
0.15411 / 0.31451 / 0.53153 (`p307_controls_audit.out`).

## The claims under attack (Gate-32 §5 restated wording only)

- **G32-F (the flat value):** maximising the spin-1 channel's dipole
  ratio over the completed fence gives HT 2.8044×10⁻⁵, NS–BH
  bound-class 2.5394×10⁻², at c_V = 1, 2, 10 alike, quoted at the
  floor-binding maximisers (c₋ ≤ 1.59×10⁻³); the maximiser set is a
  ridge. Binding leg at every row: L9, YBBY Eq. (190)'s O(10%)
  tolerance ⟨𝒜⟩_dip ≤ 0.1 for the J1738-class system. Floor-binding
  maximisers (Phase 303 §3.2, central f = 1):
  c_V=1: (c₁,c₂,c₁₄) = (2.6568×10⁻⁶, 2.6676×10⁻⁶, 2.6568×10⁻⁶),
  c₋ = 5.314×10⁻⁶, w₀ = 1.0020, 𝒞 = 7.5127×10⁵;
  c_V=2: (2.5443×10⁻⁵, 6.3620×10⁻⁶, 6.3608×10⁻⁶), c₋ = 5.089×10⁻⁵,
  w₀ = 1.0001, 𝒞 = 1.3098×10⁵;
  c_V=10: (7.9511×10⁻⁴, 7.9621×10⁻⁶, 7.9511×10⁻⁶), c₋ = 1.590×10⁻³,
  w₀ = 1.0007, 𝒞 = 8.3842×10⁴. L8 near-binding at c_V = 1, 10.
- **G32-E (Corner B):** (c₁,c₂,c₁₄) = (0.08293104, 2/21, 7.9×10⁻⁹),
  c₋ = 0.16586208, c_V = 3240; survives the completed fence at the
  central model saturating BBN (margin 0) and L8
  (α̂₂ = −9.9540×10⁻¹⁰, source caveat attached); HT 2.0607×10⁻¹⁸.
- **G32-G (distance-0):** inside the completed fence as modelled at
  rung-2 σ grade, the channel meets the registered bar (HT ≥ 10⁻⁶
  at c_V ≥ 2) at ratio 2.8044×10⁻⁵ — rests entirely on G32-F's
  value and the fence's completeness.
- **G32-C (σ values, rung-2):** σ_Æ = 2.60×10⁻⁶ (c_V=2 maximiser),
  3.24×10⁻⁶ (c_V=10), 2.95×10⁻⁹ (Corner B) at C_* = 0.17, bracket
  f ∈ [0.7, 1.3]; Gupta cross-check (Phase 306) outstanding.

Scopes are never merged: an arm may break the flat VALUE, Corner B,
or the distance-0 statement independently. Verdict per arm:
BREAKS (scope named, breaking numbers stated) / HOLDS (at the arm's
stated strength — strong or weak, worded) / UNRESOLVED (the arm
cannot be executed as registered; the reason stated exactly). An
UNRESOLVED arm blocks the overall HOLDS verdict.

## ARM 1 — THE TOLERANCE ITSELF (scope: the flat value)

Test: retrieve, at primary-source grade, the measured Ṗ_b of the
J1738-class system YBBY's map uses (PSR J1738+0333: P_b, Ṗ_b^obs,
Ṗ_b^int after Galactic/Shklovskii corrections, and its published
uncertainty — Freire et al. 2012 and any later timing update), and
the exact theory-comparison quantity YBBY Eq. (190) bounds
(⟨𝒜⟩ ≡ Ṗ_b^theory/Ṗ_b^GR or its registered equivalent in the
programme's fence). Compute the cap on ⟨𝒜⟩_dip the DATA support:
⟨𝒜⟩_dip ≤ (Ṗ_b^int/Ṗ_b^GR − 1) + n·σ_rel at the confidence level
YBBY's tolerance implicitly uses, stated explicitly; also the
cap at 95% CL for direct comparison with the other legs' 95%
conventions. Recompute the flat value with L9 replaced by the
data-grade cap (all other legs unchanged, Phase 303 machinery):
BREAKS if the data-grade flat value < 2.8044×10⁻⁵ (state it);
HOLDS if the data at their published precision support a cap
≥ 0.1 on the dipole piece alone, with the arithmetic shown.
Pre-registered subtlety: Eq. (190)'s tolerance applies to the
TOTAL ⟨𝒜⟩; the fence's registered form applies 0.1 to the dipole
piece with the quadrupole deviation bounded separately
(≤ 2.62×10⁻⁵ at the deciding corner) — the arm must state whether
the data-grade cap is on the total or the piece, and apply it in
the fence's registered decomposition, noting any difference.

## ARM 2 — THE BANDS AS DRAWN (scope: each tested point)

Test: obtain YBBY Fig. 7 (PRD 89, 084067) at the best available
resolution; digitise the allowed bands (state the digitisation
method and its error in the plane's coordinates). Identify what
the bands' axes and parameter slices are (which couplings are
held fixed, at what values) BEFORE testing any point — a point
can only be tested against a band whose slice contains it or
whose slice-dependence is shown immaterial. Test: the three
floor-binding maximisers, Corner B. BREAKS at a point's scope if
the point lies outside its applicable drawn band by more than
the digitisation error; HOLDS (weak form, worded as such — the
bands were computed inside the fits' region) if every applicable
point lies inside; UNRESOLVED if the figure or its slice
definitions cannot be obtained well enough to test.

## ARM 3 — FULL-THEORY COSMOLOGY (scope: each tested point)

Test: retrieve cosmological perturbation constraints for FULL
Einstein-aether (general c_i, not the khronometric ξ = 1 /
c₄-combination corner Phase 302 used) from primary sources —
candidates named in advance: Zuntz et al. (the generalised-EA
line Phase 302 scope-excluded), Jacobson/Matarrese-class EA
cosmology bounds, Planck-era EA analyses with c₁, c₂, c₃, c₄
free or in EA combinations (e.g. bounds on the EA effective
Newton constant / growth sector). Translate each retrieved
constraint onto the c₁₃ = 0 slice and apply to: the three flat
maximisers, Corner B. BREAKS at a point's scope if a retrieved
constraint, applied at its own stated scope and confidence,
excludes the point; HOLDS (strong) if retrieved applicable
constraints pass every point with margins stated; HOLDS (weak)
if no applicable full-EA constraint exists in retrievable form,
worded exactly as that. Note in advance: khronometric legs from
Phase 302 do NOT discharge this arm — the slice here is the
full theory's c₁₃ = 0 plane, and the dictionary must be the EA
one (c₊, c₋, c₁₄, c₂), shown explicitly.

## ARM 4 — THE DISPUTE ADJUDICATED (scope: the flat value's pricing framework)

Test: retrieve Taherasghari & Will, PRD 108, 102026 (2023) and
PRD 112, 024013 (2025) in full; retrieve any published response
or adoption (Gupta et al. 2021 and Vaglio et al. 2026 use the
far-zone coefficient — establish whether either engages the
objection). Decide, at the scope the objection actually covers:
(1) what quantity TW compute (near-zone dipole in the equations
of motion vs far-zone flux); (2) whether the orbital-decay
observable ⟨𝒜⟩ that L9 bounds is fixed by energy balance
(far-zone flux) or by the near-zone dynamics, in the regime of
the J1738-class system (weak-field, slow-motion binary —
state the PN orders involved); (3) whether TW's differing
dipole, if correct, changes 𝒞 at the flat rows' points — TW's
dipole "depends only on the vector speed": evaluate what L9
would become under TW's coefficient at the c_V = 2 and 10
maximisers. BREAKS if TW's framework, at its own stated scope,
invalidates the far-zone pricing at these points (state the
replacement cap or the collapse); FENCED if the objection
leaves a stated regime standing (the fence wording given);
HOLDS if the objection does not reach the quantity L9 prices,
with the reason derived, not asserted.

## ARM 5 — STABILITY AT THE POINTS (scope: each tested point)

Test: take the published EA mode-stability conditions (ghost
freedom + gradient stability, all three sectors simultaneously;
primary source — OMW §II / Jacobson status-report conditions,
stated in the memo with equation numbers) and evaluate every
condition at: the three flat maximisers, Corner B, and (for the
record) Corner A. The conditions to evaluate, in the slice's
variables, at minimum: tensor sector (1 − c₁₃ > 0 and c_T² > 0);
vector sector (c_V² = c₁/c₁₄ > 0 and the vector kinetic-sign
condition in its published form); scalar sector (w₀² > 0 and
the scalar kinetic-sign condition in its published form, which
involves (2 − c₁₄), (1 − c₁₃), (2 + c₁₃ + 3c₂) and c₁₂₃);
plus any published no-tachyon / subluminality-adjacent
condition the source states as a stability requirement (as
distinct from the fence's Čerenkov leg, which is separate).
BREAKS at a point if any published stability condition fails
there; HOLDS if all pass at all points, values stated.

## ARM 6 — THE EDGE (scope: the flat value)

Test: (1) Identify the w₀ ≈ 1 edge physically from the
published forms: w₀² = (2−c₁₄)c₂/[(2+3c₂)c₁₄] is the spin-0
mode speed squared on the slice (YBBY Eq. 108); the edge
w₀ = 1 is therefore the scalar mode's light-speed surface,
and the fence side w₀ > 1 is imposed by the vacuum-Čerenkov
leg (a subluminal scalar mode would be Čerenkov-radiated by
high-energy cosmic rays). The arm confirms or corrects this
identification from primary sources. (2) Re-run the
c_V ∈ {2, 10} maximisations (Phase 303 machinery, completed
fence, central model) with the added constraint
w₀² ≥ 1 + δ, δ = 10⁻³ (relative margin on w₀²), and also
report δ = 10⁻² and δ = 10⁻⁴ for sensitivity. BREAKS
(restated as an edge value) if the interior flat value falls
below the envelope floor 1.01×10⁻⁵ or collapses toward the
spin-0 row's prices; HOLDS if the flat value is reproduced
(to within the bracket's variation) at δ = 10⁻³ with the
sensitivity table shown.

## ARM 7 — POLARISATION CONTENT (scope: the distance-0 statement's fence completeness)

Test: applicability first. Retrieve what GW polarisation-content
tests actually bound (detector-network Bayesian analyses —
GW170814/GW170817-era and later catalog analyses favouring pure
tensor over pure vector/scalar alternatives): the observable
(extra-polarisation amplitude relative to tensor, for compact
binaries in the LIGO/Virgo band), the source class, and the
model assumptions (the tests compare GR-tensor against
pure-alternative hypotheses for the SAME signal; mixed-content
bounds are weaker and differently stated). Decide: do these
tests bound the spin-1 mode's emission from the fiducial
binaries (orbital frequencies ~10⁻⁵ Hz — state the band
mismatch explicitly), or the mode's coupling constants
themselves? Application only if applicable: if a retrieved
bound does translate to a cap on c₁ or the mode's amplitude
at a relevant frequency, apply it to the flat maximisers.
NOT APPLICABLE with reasons = weak HOLD, worded as such; an
applicable excluding bound = BREAKS at the stated scope.

## OVERALL VERDICT (registered)

CHANNEL BROKEN — any arm BREAKS: name the arm, scope, breaking
numbers. / CHANNEL HOLDS AT RED-TEAM GRADE — every arm HOLDS
(weak holds worded as weak) or closes with stated reasons. /
CHANNEL HOLDS WITH ARM N UNRESOLVED — any arm UNRESOLVED and
none BREAKS. DESK line: name any arm that contacted data beyond
the fences already applied (expected: Arm 1 — J1738 timing
precision; Arm 3 — cosmological datasets, if applicable
constraints are found; Arm 7 — GW catalog data, if applicable).
