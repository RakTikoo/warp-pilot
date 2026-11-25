# P133-2 — GENUINELY SECOND-ORDER ℓ = 0 (FU-P911-2)

**Worker:** W-2 (stages 1–2, stage-3 draft), completed by
**finisher W-2b** from W-2's stored state after W-2's session was
killed by a daemon restart mid stage 3 (Phase-122 W-1/W-1b recovery
pattern). Implementation fixed in `work/p1332_runrecord.md`,
including its dated finisher entry (machinery fix only; no bar,
quantity, or verdict form changed). Checker: 26/26 PASS
(`results/p1332_checker.json`, script `work/p1332_checker.py`).

## VERDICT: SECOND-ORDER CLOSES AT A PRICE

The second-order [R̃]₀ residual is zero after the full second-order
parameter set is exhausted — the areal-cancellation pattern is NOT
an O(ε) accident at the κ coefficient. But the closure is bought at
a price, stated in full below: the representative solving amplitude
δβ⁽²⁾ = −2714.48 per unit ε² exceeds the 10² priced-modes bar, and
the second-order shell datum Ŝ⁰⁰⁽²⁾ = −162.648 per unit ε² flips
the shell sign at ε = 0.1 and ε = 1/30 (it survives only at
ε = 0.01). The plain CLOSES form's shell conjunct therefore does
not hold at the two larger registered rows; the price is the
verdict's content, not a footnote.

Phase 122's milestones are cited here only as scan signals under
attack (Gate-15 pending), at their registered scope (perturbative
through the entering orders of modes ℓ ≤ 3; D/r_Σ ∈ {10, 30, 100};
pre-existing configuration). Nothing here is a transport or FTL
claim. **(V-b) UNDECIDED: Pais–Uhlenbeck spin-2 ghost vs Mannheim PT-symmetric quantisation — opposed literature positions, B3 NOT COMPUTABLE (Phase 32).**

## Anchors (all PASS, confirmed from the stored JSONs before any
deciding number was read)

- **A1** — V₀ two steps reproduced: full-metric +1.428407×10⁻³ →
  areal +3.501114×10⁻⁶ per unit ε (targets +1.428407×10⁻³ /
  +3.501114×10⁻⁶); κ_full = −2.76430632×10⁻⁵/ε vs stored
  −2.764306×10⁻⁵ (rel diff 1.1×10⁻⁷, bar 5%); enlarged 3×3 solve
  residual 4.2×10⁻²² (bar ≤ 10⁻¹²); amplitudes of the stored size
  (δβ = −3.113×10⁻³, δk = 8.89×10⁻¹², a_e = 7.56×10⁻⁵ per unit ε).
- **A2** — exact-family control: β tangent residual
  9.0×10⁻²⁷; k tangent residual 1.67×10⁻¹², both ≤ the 10⁻⁹ floor
  in Bach units. Note: the stored unit-amplitude k-tangent absolute
  values are cancellation-dominated (tangent jets ~10⁶); W-2's
  scaled redo (tangent ×10⁻⁹ and ×3×10⁻¹⁰, bachgen) gives
  residual/B2 scale 1.07×10⁻⁹ / 8.0×10⁻⁹ at B2/unit ≈ 9.801 — the
  exact-family identity holds to ~10⁻⁹ relative on the scaled
  route.
- **A3** — polarisation identity: max abs diff 2.3×10⁻²³ on a B2
  scale of 6.7×10⁻¹⁸.

## The stage-3 crash and its fix (machinery, not science)

Stage 3 crashed at `float(expr.subs(subs))` on the Q_J evaluation.
Diagnosis (verified in-item, recorded in the run record BEFORE
re-running): stage 1's `quad_coeff` extracted the λ² coefficient
with `sp.expand(expr).coeff(lam, 2)` on the RATIONAL functions Rt
and Rtn; `coeff()` on a non-polynomial is not a series extraction,
so the stored form strings still contained the symbol `lam` in
denominators after the u/v substitution, and the K channel had
degenerated to the literal "0" by the same defect. Fix: stage 3
rebuilds the exact jet functionals verbatim from the stage-1
construction, substitutes the stored h₁ jet, and extracts the λ²
coefficient as ½F″(0). Cross-check by Richardson FD in λ agrees:
Q_J[h₁,h₁] per unit ε² = ([B] 0, [K] −4.4×10⁻²⁶,
[R̃] +1.51638173×10⁻⁷ sympy vs +1.51638280×10⁻⁷ FD,
[R̃_,n] −2.45347580×10⁻⁷ vs −2.45347579×10⁻⁷).

## Deciding quantities (per unit ε²)

Second-order jump vector before homogeneous completion,
J₂ = Q_J[h₁,h₁] + L_J[s2] + L_J[p2], channels ([B], [K], [R̃],
[R̃_,n]):

| channel | Q_J (jump-quadratic) | L_J[s2] (source 2nd order) | L_J[p2] (field-quadratic) | total |
|---|---|---|---|---|
| [B] | 0 | +4.253×10⁻⁹ | −43.135816 | −43.135816 |
| [K] | −4.4×10⁻²⁶ | −6.503×10⁻¹² | +0.0190721 | +0.0190721 |
| [R̃] | +1.516×10⁻⁷ | +7.132×10⁻⁹ | −33.237455 | −33.237455 |
| [R̃_,n] | −2.453×10⁻⁷ | −8.039×10⁻⁹ | +77.109537 | +77.109537 |

- **κ⁽²⁾ = 0.** Restricted (δβ⁽²⁾, δk⁽²⁾) closure of ([B], [K])
  leaves κ⁽²⁾_restricted = +100.130 per unit ε²; the full
  second-order parameter set (representative (e) direction in the
  registered 3×3 procedure) zeroes [R̃]₀⁽²⁾ exactly (residual
  0.0; full-space lstsq over β, k and all 8 nullspace directions:
  residual 2.13×10⁻¹⁴). Closure bar |κ⁽²⁾| ≤ 10⁻⁵ met;
  floor_J2 = 3.241 per unit ε² (dominated by the A2 k-tangent
  residual mapped through the p2 machinery; all other floor
  components ≤ 7.3×10⁻⁸), so κ⁽²⁾ is at/below floor and is NOT
  decided nonzero (which would require ≥ 10³ × floor).
- **Amplitudes (the price, part 1):** representative solve
  (δβ⁽²⁾, δk⁽²⁾, a_e⁽²⁾) = (−2714.48, +2.61×10⁻⁵, −274.00) per
  unit ε² — max amplitude 2714.48 > the 10² bar. The full-space
  min-norm lstsq closes the same channels with max basis amplitude
  50.13 (basis-dependent normalisation); the registered
  representative procedure's coefficient is the priced one.
  κ⁽²⁾ is invariant under p2 nullspace shifts (diff exactly 0.0;
  amplitudes shift to (−2772.83, +2.67×10⁻⁵, −279.89) under a unit
  nullspace shift of p2).
- **Ŝ⁰⁰⁽²⁾ (the price, part 2):** −162.648 per unit ε² (primary
  solve; −43.477 under the full-space lstsq completion — the
  magnitude is completion-dependent, the sign and the row verdicts
  are not; both are ≥ 13× floor_J2). Shell pricing
  Ŝ⁰⁰/α₀ = +0.0202914453 + Ŝ⁰⁰⁽²⁾ε² − 2.7×10⁻⁶ (ℓ ≥ 4 tail
  carried): **ε = 0.1 → −1.60619 (sign FAILS);
  ε = 1/30 → −0.16043 (sign FAILS); ε = 0.01 → +0.00402
  (survives)**.

## Pattern read (per unit ε²)

The areal-cancellation pattern PERSISTS for the source monopole at
second order, by the same mechanism (the areal shift's action on
the background functionals): step 0 (slaved reference, bookkeeping
only) V₀⁽²⁾ = +1.85281×10⁻⁵ → step 1 (full-metric dyadic source,
U₀⁽²⁾,raw = 0) V₀⁽²⁾,raw = +6.12104×10⁻⁶ → step 2 (areal gauge)
V₀⁽²⁾,areal = +4.25323×10⁻⁹ — a cancellation factor of 1439
(first order: 408). The second-order problem is not in the source
monopole.

## Anatomy

The second-order join load is carried almost entirely by the
FIELD-QUADRATIC channel through the particular jet p2
(L_J[p2] up to 77.11 per unit ε²), not by the source: Q_J ≤
2.5×10⁻⁷ and L_J[s2] ≤ 8.0×10⁻⁹ per unit ε². B⁽²⁾[h₁,h₁] itself
is ~1.25×10⁻²⁰ / 3.14×10⁻²⁰ / −2.20×10⁻²⁰ (Bt, Br, Bθ) at Σ —
the two engines (bachgen primary, bachfloat second path) agree to
≤ 1.6×10⁻²⁷, Richardson spread 4.5×10⁻²⁵ — but its Taylor jet,
fed through the ill-conditioned prolonged jet system (rank 8 of
12 rows at P = 3; p2 row residual 6.4×10⁻²¹), produces a
particular jet with large join functionals. Whether that
amplification is a property of the field or of the jet algebra's
conditioning is exactly what follow-up experiment 2 below is
aimed at; the registered procedure's reads are stated above at
their floors either way.

## Second path (§8) and cross-check (§9)

- §8(i) B2 at Σ by the independent engine: agreement ≤ 1.6×10⁻²⁷
  absolute (above).
- §8(ii) source jump data by Richardson FD in amplitude on the
  exact displaced-centre source (nonlinear functionals, areal
  transform by implicit solve): after correcting a first FD fit
  that omitted the background constant (stage 4, superseded) and
  small-h mp.diff noise on the O(1) [R̃] background (stages
  4b/4c), the deciding read is the two-point Richardson in h²
  from q(0.3), q(0.4) (stage 4d): agreement with the primary
  Q_J[source] + L_J[s2] vector within **0.248%** max over the
  four channels (bar 5%).
- §8(iii) κ⁽²⁾ from second-path inputs: **0.0**, amplitudes
  (−2714.48276, +2.61×10⁻⁵, −274.00411), Ŝ⁰⁰⁽²⁾ =
  −162.6480174 vs primary −162.6480215 (rel diff 2.5×10⁻⁸) —
  agreement far inside 5% before the verdict form is used.
- §9 cross-check with P133-3 at the axis endpoint r = Σ,
  ε = 0.1: my dyadic λ² coefficient per unit ε²
  2.2670527888×10⁻⁵ vs P133-3's dBm_src_per_unit_eps2
  2.2681327279×10⁻⁵ — rel diff 4.76×10⁻⁴ (0.048%), within 5%:
  AGREEMENT. dg_tt⁽²⁾ = 0 on both sides.

## Follow-up experiments (failure protocol; aimed at the mechanism)

1. P = 4 prolonged-system and SVD-truncation sweep of the p2
   solve: if L_J[p2] (hence Ŝ⁰⁰⁽²⁾ and the solving amplitudes)
   moves by more than floor_J2 under regularisation changes while
   the prolonged row residuals stay ≤ 10⁻²⁰, the price
   coefficients must be re-read at the swept values.
2. Radial-ODE construction of h₂ — integrate
   L[h₂] = −B⁽²⁾[h₁,h₁] from the throat with the first-order
   boundary data, independently of the Σ jet algebra — and read
   its join data and shell datum directly: decides whether the
   large p2 join load is a property of the field or of the jet
   algebra's conditioning.
3. Re-price the pose restricted to ε ≤ 0.01 rows (D/r_Σ ≥ 100) at
   second order, where the shell sign survives, as a
   scope-narrowed restatement.

## Scope

ℓ = 0 only; second order in amplitude only (third order is a
named remainder); modes ℓ ≥ 1 at second order are NOT this item.
Formation standing: PRE-EXISTING ONLY. INTERNAL only; nothing
uploaded; nobody contacted.
**(V-b) UNDECIDED: Pais–Uhlenbeck spin-2 ghost vs Mannheim PT-symmetric quantisation — opposed literature positions, B3 NOT COMPUTABLE (Phase 32).**
