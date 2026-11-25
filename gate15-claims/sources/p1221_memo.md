# P122-1 — THE RE-MATCH (Phase 122, head item)

Worker W-1b (finisher; W-1 died mid-run on an infrastructure
timeout after fixing the implementation in
`work/p1221_runrecord.md` and validating the machinery — this
memo completes the item from that stored state, following the
run record exactly; two finisher repairs are recorded in §9
and in the run-record addendum).
Registration: `phase122/CHECKPOINT122.md` §P122-1.
**(V-b) UNDECIDED: Pais–Uhlenbeck spin-2 ghost vs Mannheim PT-symmetric quantisation — opposed literature positions, B3 NOT COMPUTABLE (Phase 32).**
INTERNAL only. No transport/FTL language (C12 accounting
throughout). Formation PRE-EXISTING ONLY.

## VERDICT — **RE-MATCH CLOSES**

Every channel of modes ℓ = 1, 2, 3 entering within the
registered span closes in the full linearised Bach system on
the round Σ, and the shell sign holds pointwise on both
mouths at every registered ε row. In the LANGUAGE LOCK
wording: **a two-mouth configuration is POSED through the
entering orders of modes ℓ ≤ 3 in the full linearised Bach
system** (scope: full condition set per mouth — [B]_ℓ,
[K]_ℓ, [R̃]_ℓ, [R̃_,n]_ℓ and the angular Darmois pair
[h_θθ]_ℓ, [K_θθ]_ℓ — at their confirmed entering orders,
§5; shell sign on the solved configuration at both mouths,
§7; perturbative domain ε ∈ {0.1, 1/30, 0.01} for the sign
and ε ∈ {0.1, 1/30, 0.01, 0.003, 0.001} for the extraction,
D/r_Σ ∈ {10, 30, 100}; linearised in B's amplitude). No mode
is priced: the largest solving amplitude anywhere is
4.4×10⁻³ per unit ε^entering (bar 10²), the largest
post-exhaustion residual is 3.2×10⁻¹³ per unit ε^entering
on the primary route and 5.6×10⁻¹⁰ on the independent
collocation route (bar 10⁻⁵). This verdict is a MILESTONE
under the registration: P122-2's conditional is triggered.

## 1. Method (as fixed in the run record, before evaluation)

System: full linearised Bach system about the single-centre
MK background, Phase 91's formulation (B = 2∇∇C + R·C),
Regge–Wheeler gauge (W_ℓ = G_ℓ = 0) for ℓ ≥ 1 — complete:
no residual gauge freedom at ℓ ≥ 1. Source: centre B's
localised MK far field as a FULL metric, exact
displaced-centre transformation, linearised in B's
amplitude, projected on Legendre modes and gauge-transformed
to RW gauge (run record §2 formulas). Channels: the six
registered functionals of the mode jets at Σ (LR, LK, LRn
recomputed in-item at 50 digits; the angular pair by its
registered operational definitions). Homogeneous freedom:
prolonged-system settlement by the Phase 91 W-1b method —
the Bach-at-a-point Jacobian J(r) of the generic engine
(`work/p1221_bachgen.py`, validated by W-1) on a 5-point
stencil, prolonged rows = channel Taylor coefficients with
COMPLETE Leibniz rows (J's own r-derivatives included),
dimension = rank of the nullspace's projection onto the
initial-data (ID) jet space. Floors: 3.4×10⁻⁹ per channel
per unit ε^entering (the Phase-90/91 control floor; the
A2 reproduction errors and engine noise are below it for
every deciding channel), so 10³ × floor = 3.4×10⁻⁶ < 10⁻⁵
and every channel is decidable on machinery. Cross-term
bound (registered): ≤ 5×10⁻³ relative on jump coefficients
at the κ_trunc scale — see the tail discussion in §5.

## 2. Anchors (all before any deciding number)

- **(A1) ℓ = 0 control — PASS.** (i) The in-item prolonged
  system at ℓ = 0 settles at dimension **7** at both radii
  (Σ spectrum: six ID singular values at 1.0, a seventh at
  3.5×10⁻⁵, then 1.5×10⁻¹⁷ — the seventh direction is
  weakly ID-represented and separates only at P = 3, Phase
  91's delayed determination). (ii) From Phase 91's stored
  jumps and response matrix, the in-item solve reproduces
  κ_full = −2.7643063154×10⁻⁵/ε (stored −2.7643063154×10⁻⁵,
  rel. diff 2×10⁻¹⁵) with |δβ| = 6.93×10⁻³/ε (stored size
  class; sign is the solve-convention sign), and the
  enlarged solve (δβ_MK, δk + the 7-direction ID basis)
  gives κ_enlarged = 0 with residual norm 8.6×10⁻²¹. The
  in-item tangent responses reproduce the stored response
  matrix exactly (β column [2.008005×10⁻³, 2.010890×10⁻⁶,
  1.200000×10⁻²]; k column [1.0040025×10⁶, −1997.552,
  ~0]).
- **(A2) Truncation control per mode — PASS.** Restricted
  to Phase 90's truncation the in-item functionals give
  [B]_ℓ = c·ε^{ℓ+1} with c = 4.302374×10⁻³ at every
  ℓ = 0…3 (Phase 90's own stored stage tables:
  4.302373597×10⁻³; the D3 prose value 4.302743×10⁻³
  differs in the 4th digit — a transposition in that prose
  value; agreement is within the registered 5% either way);
  the D3 dipole triple per ε²: (+4.302374×10⁻³,
  −4.270452×10⁻⁶, +5.514442×10⁻⁵) vs stored (+4.302743×10⁻³,
  −4.270543×10⁻⁶, +5.514561×10⁻⁵), all within 2×10⁻⁴
  relative; [R̃]₃ coefficient +8.570444×10⁻³ per ε⁴ exact;
  response identity S₀ = −2, S₁ = 0, S₂ = −4.7×10⁻¹⁶
  (within 1%).
- **(A3) Background + tangents — PASS.** Generic engine:
  max |B| on the MK background 7.9×10⁻¹⁹ (at r = 11; ≤
  3.7×10⁻²⁴ at Σ); cross-check vs the Phase-91 reference
  engine exact (0 difference) at the tested points;
  linearised tangents at the finite-difference floor
  (β: 5.5×10⁻²¹; γ: 4.1×10⁻¹¹; k: 5.1×10⁻⁹ — the γ/k
  residuals scale with the square of those profiles'
  amplitudes, i.e. FD quadratic contamination, consistent
  with exact linearised satisfaction).
- **(A4) Projected-problem inputs at scope — STATED.**
  Phase 92's pair-match (through O(ε²) in the blind
  channel) and Phase 103's verdicts (the blind channel is
  feedable only by an illegal source in the registered
  classes; the obstruction reappears at O(ε³)) are
  statements about the PROJECTED / truncated problem.
  Neither substitutes for this item, which is the
  unprojected full system: §6 shows the full-system
  [R̃]₁, [R̃]₂ are not blind, so the projected problem's
  premise does not carry over. The (t, r)-sector response
  identity is an input at its scope only (A2).

## 3. Homogeneous freedom: dimensions and classification

Settled dimensions (ID-jet projection rank; Σ spectra at
K = 7, P = 3, row tolerance 10⁻³, stable for K ∈ {6, 7},
P ∈ {2, 3} and row tolerances 10⁻⁴…10⁻²):

| mode | dimension | ID spectrum (Σ) after the unit block |
|---|---|---|
| ℓ = 0 (control) | 7 | 3.5×10⁻⁵, then 1.5×10⁻¹⁷ |
| ℓ = 1 | **9** | 2.3×10⁻⁹ |
| ℓ = 2 | **7** | 5.5×10⁻¹⁵ |
| ℓ = 3 | **7** | 1.0×10⁻¹⁵ |

Classification (registered scheme): (a) pure gauge —
EMPTY at ℓ ≥ 1 (gauge completeness, run record §1);
(b) MK tangents — ℓ = 0 only, none at ℓ ≥ 1 (stated);
(c) singular — none (jets finite at Σ; propagation spot
check §8); (d) source-inconsistent — no local diagnosis
applies at Σ under the registered scheme (stated
limitation); (e) LEGITIMATE — every settled direction at
ℓ = 1, 2, 3. (β_MK, k) are consumed at ℓ = 0 and are not
in the ℓ ≥ 1 sets; the γ-freed branch was not examined
(it is an ℓ = 0 freedom). The response of the (e) sets on
the six channels has **rank 6 — full — at every mode**
(smallest response singular values: ℓ = 1: 0.70; ℓ = 2:
3.9×10⁻³; ℓ = 3: 1.2×10⁻³, in the unit-max-Taylor
normalisation). Mode decoupling was verified structurally
in-item (W-1's engine validation + the per-mode Jacobian
construction: a pure-mode profile produces Bach components
only in that mode's angular span).

Second-radius note (anatomy, not a verdict input): the
r = 11 route corroborates ℓ = 0 (7), ℓ = 1 (9) and ℓ = 3
(7) on its clean (P = 2) reads. For ℓ = 2 the Richardson
r = 11 read brackets 7–8: an eighth direction appears at
ID strength 1.1×10⁻⁵ at row tolerance 10⁻³ (7 at 10⁻⁴).
At Σ that direction has no ID content above 5.5×10⁻¹⁵ in
the settled window, and the verdict is insensitive to it:
the response rank is already full with the settled 7, and
all residuals close at ≤ 10⁻¹². It is recorded here as the
one place the two-radius settlement is not equally clean
at both radii.

## 4. Source coefficients (full system, per unit ε^power)

Extracted over ε ∈ {0.1, 1/30, 0.01, 0.003, 0.001} at 40
digits; every channel's ε-dependence fits a two-power form
with fit residuals ≤ 10⁻¹⁴ relative (the middle power's
coefficient is ≤ 10⁻¹⁷ in every fit — identically zero
within the extraction). Deciding values:

**ℓ = 1 (all at ε²):** [B] +6.014537×10⁻³; [K]
−4.254506×10⁻⁶; [R̃] +1.552938×10⁻³; [R̃_,n]
+1.622818×10⁻³; [h_θθ] +5.992471×10⁻³; [K_θθ]
+1.015272×10⁻⁸ (below the decided threshold — not a
decided entry, answered anyway).

**ℓ = 2:** at ε³ (main): [B] +4.296098×10⁻³; [K]
−8.532279×10⁻⁶; [R̃] −1.213920×10⁻⁴; [R̃_,n]
−3.532492×10⁻⁴; [h_θθ] +4.280336×10⁻³; [K_θθ]
+2.145284×10⁻⁶ (below threshold). At ε¹ (tail, §5): [B]
−1.268835×10⁻⁵; [h_θθ] +5.700094×10⁻⁶; [R̃]
+3.367788×10⁻⁷, [R̃_,n] +2.073658×10⁻⁷, [K] −6.9×10⁻⁹,
[K_θθ] −6.3×10⁻⁹ (all four below the decided threshold
3.4×10⁻⁶, answered anyway).

**ℓ = 3:** at ε⁴ (main): [B] +4.295796×10⁻³; [K]
−1.281201×10⁻⁵; [R̃] +8.413535×10⁻³; [R̃_,n]
+2.495529×10⁻²; [h_θθ] +4.280472×10⁻³; [K_θθ]
+4.283369×10⁻⁶. At ε² (tail, §5): [B] −1.141952×10⁻⁵;
[R̃] +1.291242×10⁻⁵; [R̃_,n] +7.125451×10⁻⁵; [h_θθ]
+5.130084×10⁻⁶; [K] −1.8×10⁻⁸, [K_θθ] −3.1×10⁻⁹ (below
threshold).

## 5. Entering-order deviation (anatomy, as registered)

The registered expectation ([B]_ℓ, [K]_ℓ, [R̃_,n]_ℓ,
angular pair at ε^{ℓ+1}) is CONFIRMED for ℓ = 1 and for
the main terms at ℓ = 2, 3, but at ℓ = 2 and ℓ = 3 the
full-system source ALSO carries a tail exactly one power
lower (ε^{ℓ−1}… in absolute terms ε¹ at ℓ = 2, ε² at
ℓ = 3), with the intervening power identically zero. The
tail is structural, not numerical: in the raw projection
the flat-space pieces cancel between V^raw_ℓ and the
gauge term 2X′_ℓ/f exactly at leading order, and the
cancellation is broken at relative order f′(Σ)·r_Σ/3 =
2.96×10⁻³ by the background's radial variation (the
−f′Q term in X′ and the X·(1/f)′ term combine to
−(f′/f)(r_Σ/3) in v-units; for [B]₂ this predicts the
tail coefficient −C·f′·r_Σ/(3000·f) = −1.268×10⁻⁵ per
ε¹, matching the extracted −1.268835×10⁻⁵). The tail
coefficients are ~3×10⁻³ relative to their modes' main
coefficients — at the registered cross-term bound scale
(5×10⁻³), so their precise values carry that uncertainty;
they are decided nonzero against the machinery floor
([B]₂ tail: 3730× floor) and are answered by the same
(e) solve, so no deciding read hinges on their exact
values. Both powers were solved (§7 table in the results
file). Channels entering above ε⁴ remain the unposed
remainder, with the O(ε²) nonlinear terms (FU-P911-2).

## 6. The [R̃]₁ / [R̃]₂ blindness sub-question — DECIDED

The (t, r)-sector identity δR̃_ℓ = −(ℓ−1)(ℓ−2)·u_ℓ(Σ)
does **not** extend to the full system. The full metric's
RW-gauge source jets are not the slaved (t, r) jets, and
the computed full-system coefficients are decided nonzero:
**[R̃]₁ enters at ε² with +1.552938×10⁻³** (4.6×10⁵ ×
floor) and **[R̃]₂ enters at ε³ with −1.213920×10⁻⁴**
(3.6×10⁴ × floor; its ε¹ tail +3.37×10⁻⁷ is below the
decided threshold). No identity proof exists in the full
system — the sub-question is decided by computation, and
both channels are answered by the (e) solve (residuals
≤ 10⁻¹⁴). This is also why the Phase-92/103 projected
results (A4) do not transfer: their blind channel is not
blind here.

## 7. Mode solves and shell sign

Per mode, per entering power, the (e) solve
R_ℓ·a = −(source vector) closes every channel:

| mode / power | max |residual| (primary) | max |residual| (collocation route) | max amplitude |
|---|---|---|---|---|
| ℓ=1, ε² | 3.2×10⁻¹³ | 5.6×10⁻¹⁰ | 4.09×10⁻³ |
| ℓ=2, ε¹ (tail) | 6.3×10⁻¹⁵ | 1.1×10⁻¹³ | 7.8×10⁻⁶ |
| ℓ=2, ε³ | 1.4×10⁻¹² | 6.8×10⁻¹¹ | 3.96×10⁻³ |
| ℓ=3, ε² (tail) | 5.5×10⁻¹⁶ | 4.9×10⁻¹³ | 8.0×10⁻⁶ |
| ℓ=3, ε⁴ | 8.9×10⁻¹³ | 5.1×10⁻¹⁰ | 4.42×10⁻³ |

(Full per-channel vectors in `results/p1221_results.json`.)
Note the contrast with the truncated scheme, where the
ℓ = 2 deformed Darmois pair was inconsistent (s₂ ratio
1.995743): in the full system [B]₂ and [K]₂ close
simultaneously on the ROUND Σ — no surface lean is needed
at any mode (the combined deformed-Σ question is P122-3's
Q3, which on this verdict records its round-Σ premise).

**Shell sign.** On the solved configuration the mode
residuals in [R̃_,n] are ≤ 10⁻¹², so [R̃_,n](θ) equals
the ℓ = 0 control −0.0152185840 up to ≤ 10⁻⁹ pointwise
variation, and Ŝ⁰⁰(θ)/α₀ = −(4/3)[R̃_,n](θ) has minimum
**+0.0202914453** — the control value Ŝ₀⁰ = +0.02029145 α₀
— at BOTH mouths (Σ_B evaluated explicitly; the A↔B
symmetry makes the two minima identical) at each of
ε ∈ {0.1, 1/30, 0.01}. The ℓ ≥ 4 tail bound (run record
§6: 2×|[R̃_,n]₄(ε)| ≤ 2.06×10⁻⁶ at ε = 0.1, falling as
ε⁵) leaves the minimum at +0.02028870 > 0. **The shell
sign holds pointwise everywhere with the full control
margin.**

## 8. Second path (adversarial protocol)

- *Source side:* all deciding coefficients recomputed by
  an independent 200-point Gauss–Legendre quadrature
  (float64) with FD/Richardson derivatives and an
  independently coded gauge transform: agreement within
  5% on every deciding coefficient (worst in that set:
  1.4×10⁻³, [R̃]₂ at ε³; most ≤ 10⁻⁵).
- *[R̃_,n] side:* a direct profile route (R̃(r) from its
  definition at Σ±1, Σ±2, outer FD) agrees for ℓ = 1
  (4.8% at ε²) and ℓ = 3 (0.2% at both powers). For
  ℓ = 2 it disagreed (15% at ε³) — arbitrated by a third
  route (FD of the reliable jets U″, V′ + the LRn
  functional), which reproduces the primary **exactly**
  (U‴, V″ and [R̃_,n]₂ agree to ≤ 10⁻⁹ relative at
  ε ∈ {0.1, 0.01, 0.001}). The profile route's ℓ = 2
  off-Σ R̃ values carry the artefact (its R̃(Σ) values
  agree to 10⁻⁵); the primary stands.
- *Homogeneous side:* the collocation route (Bach = 0
  imposed at the stencil radii directly, different row
  construction) repeats every solve: all deciding
  residuals ≤ 5.6×10⁻¹⁰, same verdict.
- *Propagation spot check:* one (e) basis element per
  mode, realised as a polynomial profile about Σ, has
  linearised Bach 1.8×10⁻⁹…1.1×10⁻⁶ at Σ±20 r₀, vs
  2.7×10⁻²…6.4×10⁻² per unit for random control jets.
- *Shell-sign second path:* [R̃_,n](θ) re-evaluated from
  the collocation route's solved profiles — residuals
  ≤ 10⁻¹⁰ there too, same minima.

## 9. Finisher repairs (recorded, minimal)

(i) The first finisher source extraction had a sign error
in the W_ℓ projection (missing minus in
W_ℓ = −⟨H, P′_ℓ⟩/⟨P′_ℓ, P′_ℓ⟩, run record §2); it was
caught by the ℓ = 2 entering-order anomaly before any
deciding read, the extraction was re-run, and the
corrected values are second-pathed in §8. (ii) The
homogeneous settlement's first attempt (single-θ
collocation on truncated polynomials) was unstable across
routes — the Phase-91 truncation trap — and was replaced
by the registered prolonged-system method in its
Jacobian/Leibniz form (§3); no design change. (iii) At
ℓ = 1 the tracefree angular basis vanishes identically
(E_θθ = E_φφ = 0), so the (X, Y) projection degenerates;
the ℓ = 1 channel set is (Bt, Br, BX-trace, Brt) — a
machinery fact, stated here and in the run-record
addendum. Nothing in the registration or the run record's
fixed setup was changed.

## 10. Scope and follow-ups

Perturbative domain only (registered ε rows; D/r_Σ ∈
{10, 30, 100}); nothing about D ≈ 2r_Σ. The construction
is linearised in B's amplitude; second-order terms are
the carried FU-P911-2 question. A closed re-match poses
a configuration at the registered orders; it does not
form one (formation PRE-EXISTING ONLY) and decides
nothing about (V-b). **(V-b) UNDECIDED: Pais–Uhlenbeck spin-2 ghost vs Mannheim PT-symmetric quantisation — opposed literature positions, B3 NOT COMPUTABLE (Phase 32).**
Follow-ups: (1) P122-2's conditional is TRIGGERED by this
verdict. (2) P122-3 takes this item's stored mode data as
input (below). (3) The r = 11 ℓ = 2 eighth-direction
sighting (§3) is available as a machinery follow-up; it
cannot change this verdict (response rank already full).

## 11. Files P122-3 should read

- `work/p1221_mode_data.json` — per mode: `source_fits`
  (per-channel ε-power fits of the full-system source,
  both powers), `response_matrix` and
  `id_basis_jets_normalised` (the (e) basis at Σ, unit
  max Taylor coefficient), `solves` (per-power source
  vectors, amplitudes, residuals). Schema note is in the
  file's `note` field.
- `work/p1221_source.json` — the per-ε source jets
  (U, V, Θ jets at Σ for every extraction row) behind the
  fits.
- `results/p1221_results.json` — the full deciding
  record (anchors, classification, fits, solves, shell
  sign, second path, verdict). Checker:
  `results/p1221_checker.json` (57/57 PASS) from
  `work/p1221_checker.py`.
