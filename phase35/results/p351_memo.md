# P35-1 Memo — EiBI MIXTURE gravitational sector

Worker P35-1. Script: `phase35/p351_main.py`; results:
`phase35/results/p351_results.json`; full system, prescriptions and
ladder stated before solving in `phase35/results/p351_run_record.md`.
float64. Rows: primary f=0.75, w=1/3; cross-checks f=0.5, w=1/3 and
f=0.6, w=0; κ=−1, r0=0.70711, x=0.5, domain [r0, 1e3 r0].

**Plain language first.** The mixture fixed the *matter* sound-speed
problem in Phase 33, but gravity still cannot be certified at this
throat — and now we know the obstruction is worse for a mixture than
for the single fluid, in a precise way. The auxiliary map Ω that
connects the real metric to the auxiliary one does not just lose two
directions at the throat (the single-fluid behaviour): for a mixture
one of its eigenvalues *blows up* like 1/√ε while the other three
vanish. That blow-up breaks the metric reconstruction itself — the
equations that should determine the wormhole's shape function
contradict each other at the throat by a fixed, sign-opposite amount
that no choice of the shape function can remove — and it makes the
regularised-layer matching of the gravitational sectors fail: the
odd sector's throat data grows without bound and depends on which
regularisation you choose, and the even sector's data is still
moving by 68% per ladder step. Verdict: **OBSTRUCTED** (details and
exact sub-findings below). Step B alone did **not** succeed: the
sub-verdict is NO RECONSTRUCTION, so P33-3 follow-up #1's first half
is answered negatively, with the deciding equation named.

## GATE — PASSED (all three rows)

Recomputed from the P33-3 construction, against
`phase33/results/p333_results.json`:

| row | κρ_tot(r0) | c1t²(r0) (stored) | 2f−1 | cons. residual | all-EC | det Ω(r0) |
|---|---|---|---|---|---|---|
| f=0.75, w=1/3 | −1.0 | 0.5 (0.5) | 0.5 | 8.9e-16 | pass | 0.0 |
| f=0.5, w=1/3 | −1.0 | 0.0 (0.0) | 0.0 | 1.1e-15 | pass | 0.0 |
| f=0.6, w=0 | −1.0 | 0.2 (0.2) | 0.2 | 6.7e-16 | pass | 0.0 |

c1t²(r0) matches 2f−1 to ≤1e-9 (exact in float64); conservation in
the ≤1e-12 class; det Ω(r0)=0 exactly in the rational profile form
(stored primary value 2.3e-16 is the same zero at float64 rounding).

## Ω eigen-structure at the mixture throat (required universality read)

With ε = r−r0, a = 1+κρ_tot, b_om = 1−κp_r,tot, c_om = 1−κp_t,tot,
ω_t = c_om√(b_om/a), ω_r = c_om√(a/b_om), ω_θ = √(a·b_om),
det Ω = c_om²·a·b_om, q-areal radius S = r(a·b_om)^{1/4}.
Log-log fits on ε ∈ [1e-8, 1e-3], all three rows identical in orders:

| quantity | mixture (this item) | one-fluid (P25-2 / recomputed) |
|---|---|---|
| a = 1+κρ_tot | ~ ε¹ (slope 0.9999) | ~ ε¹ (B linear, 2.828ε) |
| b_om | → b0 = f(1+w) **finite** (1.0 / 0.667 / 0.6) | b_om = a → 0 |
| c_om | → c0 finite (1.4375 / 1.4167 / 1.24) | finite (1) |
| ω_t | **~ ε^(−1/2) POLE** (slope −0.500; ω_t(ε=1e-6)=729 primary) | finite (= c0; slope 0.000) |
| ω_r | ~ ε^(+1/2) → 0 | finite (= c0) |
| ω_θ = ω_φ | ~ ε^(+1/2) → 0 (each) | ~ ε¹ → 0 |
| det Ω | ~ ε¹ (slope 0.9999–1.000) | ~ ε² |
| S (q-areal radius) | ~ ε^(1/4) cusp | ~ ε^(1/2) cusp (H ~ √ε) |
| Ω at r0 | one divergent + three vanishing eigenvalues; no finite rank | rank 2/4, eigenvalues (c0, c0, 0, 0) |

**P33-3's ω_t pole is CONFIRMED, with order −1/2** (it is the
eigenvalue ω_t = c_om√(b_om/a): b_om stays finite because off the
one-fluid ansatz p_r,tot(r0) = −1+f(1+w) ≠ −ρ_tot(r0), while
a ~ ε). **The deciding degeneracy is MIXTURE-DEPENDENT.** What is
universal is only the trigger: a vanishes linearly (the throat
condition κρ_tot(r0) = −1) and det Ω(r0) = 0. Everything downstream
of that differs: because b_om(r0) = f(1+w) ≠ 0 for any genuine
mixture row (f>0), the angular eigenvalue vanishes only as √ε
instead of ε, det Ω vanishes one order more slowly (ε¹ vs ε²), ω_r
newly vanishes as √ε, ω_t acquires its ε^(−1/2) pole, the q-areal
cusp sharpens from ε^(1/2) to ε^(1/4), and Ω has no finite rank at
r0 at all (one-fluid: rank 2/4). The mixture does not merely inherit
P20-2/P25-2's obstruction; it changes its anatomy.

## STEP B — metric reconstruction: **NO RECONSTRUCTION**

System (stated in full in the run record before solving): g-areal
frame (the frame the throat and the profiles live in); unknowns
u(r) = 1 − b_g(r)/r, with Φ input from fluid-2 conservation,
Φ = −(w/(1+w)) ln(ρ2/ρ2(r0)); equations the EiBI defining relation
q_{μν} = g_{μν} + κR_{μν}(q), three components (t, r, θ) for the one
unknown u. One-fluid limit of the Ω map checked (b_om = a,
ω_t = ω_r = c_om, ω_θ = a — P20-2's eigenvalues, gate values above).

Throat balance, exact in ε (all three rows, identical coefficients):
writing u ~ Uε^q, the t-component's bracket K_t has
ε²K_t → (2−q)/8 (measured: q=1: +0.125; q=1.5: +0.0625; q=2: 0.0;
q=2.5: −0.0625), so the t equation forces **q = 2**. With q = 2:

- **r-component (deciding):** ε²R_rr(q) → **−1/8** (measured
  −0.12500 at ε=1e-6, all rows), while the r-component of
  q = g + κR(q) requires ε²R_rr → **+1/U**. For every U > 0 (the
  no-horizon sign) the two are sign-opposite; the mismatch is
  −(1/8 + 1/U), i.e. −9/8 at U=1. Puiseux corrections to u enter
  R_rr only at O(ε^(−3/2)) and cannot move the ε^(−2) coefficient.
- **θ-component (independent second failure):** R_θθ(q) → **1.000**
  as ε→0, while the θ equation requires R_θθ → r0²(1−ω_θ) →
  **0.500**. Mismatch a factor 2, likewise at an order corrections
  to u cannot reach.
- Secondary: the forced balance u ~ Uε² gives b_g'(r0) = 1, so the
  flare bar b'(r0) < 1 also fails in the limit (equality).

The mechanism is the mixture's S ~ ε^(1/4) cusp: in the one-fluid
case (S ~ ε^(1/2), u ~ ε¹) the two dangerous ε^(−2) terms of R_rr
cancel exactly (−2S″/S against B′S′/S); with the mixture's
exponents (S ~ ε^(1/4), u ~ ε²) the same combination leaves the
residue (1−q)/8 ε^(−2) = −ε^(−2)/8. No ODE integration is owed once
the series balance fails: there is no u(r) — smooth or Puiseux —
satisfying the system at the throat, so the ≤1e-8 residual bar,
b(r0)=r0 with b'(r0)<1, and the no-horizon read cannot be met.
Asymptotics, read exactly at the level reached: Φ is finite at the
throat (Φ'(r0) = 0.884 primary; 1.061 and 0.0 cross-rows) and its
profile-level tail is Φ ~ c_Φ ln r with **c_Φ = 4w/(1+w) = 1.0**
for w=1/3 (0 for w=0) — the P33-3 prediction is confirmed as a
profile identity, but since no metric exists completing it, the
reconstruction neither removes nor inherits it as a solution tail;
the sub-verdict is NO RECONSTRUCTION, not RECONSTRUCTED-NONFLAT.

## STEP C — regularised-layer matching: **OBSTRUCTED**

Posed at the registered level (run record): principal-symbol +
Frobenius/radial-operator level (l=2 radial operator on q,
D[Ψ] = Ψ″ + 2(S_reg'/S_reg)Ψ′ − 6/S_reg² Ψ = 0), NOT a full
quadratic action; both sectors share the radial operator at this
level and differ in regular throat data (even: Ψ=1, Ψ'=0; odd:
Ψ=0, Ψ'=1). Ladder: all 9 (δ/r0, η) pairs, δ/r0 ∈ {1e-1,1e-2,1e-3},
η ∈ {1e-2,1e-4,1e-6}, both prescriptions, primary row; diagonal for
both cross-rows (same behaviour). Both prescriptions are EC-legal
in the layer (mid-layer EC minimum ≥ +0.49 in every rung, both
prescriptions). Boundary data L = Ψ'/Ψ at r = r0+δ, diagonal
sequence (δ/r0 = √η):

| sector | prescription | L: δ/r0=1e-1 | 1e-2 | 1e-3 | last-step change | cross-prescription diff (finest) |
|---|---|---|---|---|---|---|
| even | hard floor | 1.340 | 0.503 | 0.162 | **67.9%** | 2.9e-5 (rel) |
| even | smooth interp | 1.362 | 0.504 | 0.162 | **67.9%** | — |
| odd | hard floor | 5.18 | 27.4 | 166 | **507%** | **160%** |
| odd | smooth interp | 7.30 | 53.9 | 431 | **701%** | — |

Partial scope, stated exactly:
- **Odd sector: DIVERGED and PRESCRIPTION-DEPENDENT.** L_odd grows
  ~δ^(−0.8) (hard) / faster (smooth) along the diagonal, varies by
  over an order of magnitude across η at fixed δ=1e-3 r0
  (2211 at η=1e-2 vs 166 at η=1e-6, hard floor), and the two
  prescriptions disagree by 160% at the finest rung. No boundary
  datum exists to certify.
- **Even sector: NOT CONVERGED (by the registered bar).** The two
  prescriptions agree closely (3e-5 relative at the finest rung),
  but L_even is still falling steeply at the ladder's end (last-step
  change 67.9%, ≫ the 1% bar); no converged value is certified.
- **Health signs: HEALTHY where read, off-layer only.** On
  [r0+δ, 10 r0] (original background): kinetic sign
  sign(√det Ω) = + (min √det Ω = 0.075–0.66 across δ), radial cone
  ratio² b_om/a > 0 and angular cone ratio² ω_t/ω_θ > 0 everywhere
  read. These are the P25-2 off-throat diagnostics, unchanged; they
  do not extend through the layer, and healthy signs without
  convergent boundary data do not certify a sector.

## STEP D — Hamiltonian momentum-map scoping (one paragraph)

No momentum-map variable of the kind P25-2 named is available for
the mixture system with the machinery on hand: everything computed
here (and in P20-2/P25-2/P33-3) lives in the metric Ω-map
formulation, where the would-be independent angular variable is
algebraically slaved to the totals through ω_θ = √(a·b_om) — and
for the mixture that slaving is itself singular (ω_t pole,
ω_r ~ √ε). Posing it would require a genuine canonical
reformulation of EiBI (connection/q variables with their constraint
algebra, in the spirit of the Palatini Hamiltonian treatments in
the literature) *plus* a two-fluid matter Hamiltonian with separate
conservation imposed as constraints, and a check that the angular
momentum-map component stays independent at a ~ ε with b_om finite;
none of that machinery exists in this programme's codebase, and
building it is a phase-level item, not a follow-up computation.
Scoping verdict: door named, not opened; no computation owed or
claimed.

## VERDICT (fixed language)

**OBSTRUCTED** — deciding degeneracy: the mixture Ω eigenvalue
**ω_t ~ ε^(−1/2) pole** (with ω_r ~ ε^(+1/2), ω_θ ~ ε^(+1/2),
det Ω ~ ε¹), arising because b_om(r0) = f(1+w) ≠ 0 off the
one-fluid ansatz. It acts in both steps: in Step B it sharpens the
q-areal cusp to S ~ ε^(1/4), whose uncancelled ε^(−2) residue
(−1/8 computed vs +1/U required in the r-component of
q = g + κR(q); θ-component 1.000 vs 0.500 required) makes the
reconstruction inconsistent at the throat — **Step B alone did NOT
succeed (NO RECONSTRUCTION)**; in Step C it makes the odd sector's
layer boundary data diverge prescription-dependently and leaves
the even sector unconverged at the ladder's end, with health signs
healthy only off-layer. The degeneracy is **MIXTURE-DEPENDENT**
(orders, pole structure, det order and rank all differ from
P25-2's one-fluid anatomy: det ~ ε², rank 2/4, ω_t finite).
Consequence, stated exactly: the EiBI-fluid ledger row's
gravitational criterion stays "NOT COMPUTABLE (uncertified)" for
the mixture row as well; the row still carries the |κ| window
(P35-2) and remains a static pre-existing throat, NOT CROSSABLE as
transport on this phase's evidence alone, not FTL. The P33-3
matter-sector AUGMENTED-PASS is untouched — it never depended on
the gravitational sector.

## Follow-ups (Failure Protocol)

1. **Proper-distance layer matching (mechanism-suggested by the
   ε^(1/4) cusp):** the areal-δ ladder compresses the layer's
   proper width ∝ ∫√Q_r dr, which the ω_r ~ √ε vanishing distorts
   differently per prescription. Re-run Step C with the layer
   defined in q proper radial distance ℓ (δ_ℓ ladder, S(ℓ)
   regularised directly); the odd sector's ~δ^(−0.8) growth law
   makes a falsifiable prediction for how L_odd(δ_ℓ) must rescale
   if the divergence is a coordinate-width artefact rather than a
   property of the throat — if it survives in ℓ, the obstruction
   is coordinate-invariant at this level.
2. **Frobenius-rescaled master variable:** the radial operator's
   singular terms (S'/S ~ 1/(4ε), 6/S² ~ ε^(−1/2)) suggest posing
   the sectors for Ψ̃ = Ψ/S^(3/4) (the mixture analogue of the
   one-fluid S^(1/2) rescaling), whose indicial structure differs
   from the one-fluid case precisely by the mixture exponents
   above; whether the rescaled odd datum converges is a sharp,
   cheap test of whether the divergence lives in the variable or
   in the sector.
3. **Reconstruction in the q-areal coordinate:** Step B's mismatch
   was derived in the g-areal frame (registered choice). The
   ε^(−2) residue is a tensor-component statement, but a
   coordinate-level cross-check — re-expressing the profiles as
   functions of S and re-running the balance — would close the
   last reparametrisation loophole before this NO RECONSTRUCTION
   is treated as frame-independent.

Files: `../p351_main.py`; `p351_results.json`, `p351_run_record.md`,
this memo. CHECKPOINT35.md untouched.
