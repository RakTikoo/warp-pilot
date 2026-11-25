# GATE-37 — Adversarial re-judgement of the Phase 318 + Phase 323 semiclassical identification

**Gate:** GATE-37 (adversarial re-judgement; charged at ledger entry
810). **Frame of record:** Phase 166 pin conventions as carried by the
record; exact-rational arithmetic for every deciding read.
**Instrument:** the gate's OWN machinery, built for this gate —
`gate37/work/g37_jets.py` + `g37_engine.py`. No Phase 259, 318 or 323
derivation code was imported or reused for any deciding read: the
variation engine is a from-scratch exact-rational Taylor-jet
implementation in the local frame (t, x = l − l₀, u = θ − π/2, φ),
computing E[scalar] (programme convention: δS = ∫√−g E_ab δg^{ab}) by
dual-jet linearisation with respect to the inverse-metric jet
coefficients, a triangular extraction of the Euler–Lagrange
derivative, and the √−g ratio handled by the exact jet
σ = √(−det g / −det g(0)). Phase 318/323 records were read for
targets and background definitions only (the stored exact R-jets;
the E:1/10 background = A-family R-jet with e^{2Φ} = 1 − 1/R + ε/R²,
ε = 1/10, per the record's construction). Curvature conventions were
locked at every point against the stored Ricci reads — all matched
exactly (Ellis throat (0, −2, 0, 0); Ellis ℓ = 1 (0, −1/2, 0, 0);
A throat (0, −1, 1/2, 1/2); C:1/2 (0, −5, −3/2, −3/2);
E:1/10 (−2, −3, 1/2, 1/2)).

## Verdict

**(i) The printed-number attribution — SURVIVES.**
**(ii) The A-throat evaluation (9/4, 3/4, 21/4) — SURVIVES.**
**(iii) The identification, in its registered form only — SURVIVES.**

The 318+323 claim set joins the publication queue as a future version
after v1.26.0 (packaging is the parent's act).

## §1 Engine calibration (before any deciding read was quoted)

The gate's engine was first run on values it was not built to fit:

- **Ellis ℓ = 1** (a point with g(0) ≠ η): E2 = (47/8, 1/8, 55/8)
  mixed, exact — the stored Phase 323 validation value.
- **Algebraic scalars at the Ellis throat:** E[tr Ric³] =
  (−32, −8, −44), i.e. H(6,3)(3) = (32, 8, 44), and
  E[R_{pq}R_{rs}R^{prqs}] = (−4, −4, −16), i.e. H(6,3)(4) = (4, 4, 16)
  — Phase 318's independent derivations, reproduced exactly. (These
  two values are also the H(3)/H(4) inputs of deciding read (3)
  below, so the REST arithmetic runs on this gate's own numbers, not
  on Phase 318's say-so.)
- **Ellis R = 1.5, float mode:** E2 matches the stored floats at max
  deviation 6.7×10⁻¹⁴ (the stored values' own float-accumulation
  class).
- Every exact evaluation in this gate: **divergence of E exactly
  (0, 0, 0, 0)** at the point and **off-diagonal components exactly
  0** — the diffeomorphism certificate, in exact arithmetic.

## §2 Deciding read (1) — H{2,0}(3) at the Ellis throat

The gate's variation of L = −(∇Ric)² at the Ellis throat, exact:

    E2 (programme mixed) = (−80, −16, −112),   div = 0, offdiag = 0
    derived print H{2,0}(3) = −E2 = (80, 16, 112)

This is a third derivation path, independent of Phase 323's route (a)
(Phase 259's ∇-sector engine on an R-jet-built metric jet) and of
route (b) (the DF Eq. (2.23) transcription). It lands on Phase 259's
Stage 1b byproduct value exactly.

## §3 Deciding read (2) — H{2,0}(3) at the A throat

    E2 (programme mixed) = (−9/4, −3/4, −21/4),   div = 0, offdiag = 0
    derived print H{2,0}(3) = (9/4, 3/4, 21/4)

— exactly Phase 318's registered conditional prediction and Phase
323's route-(a) exact value, reproduced by the gate's independent
machinery in exact rational arithmetic.

## §4 Deciding read (3) — the REST arithmetic and the attribution

Exact Fractions throughout. At the Ellis throat, with the gate's own
H(3) = (32, 8, 44) and H(4) = (4, 4, 16) (§1):

- REST_print = (44/135, 4/27, 100/189) **rebuilds exactly** from the
  implied print tensor and the derived (3),(4) combination.
- Implied print H{2,0}(3) = **(80, 80/3, 112)**.
- Implied − derived = **(0, 32/3, 0)**: T^t_t and T^θ_θ implied =
  derived exactly; the sole difference is T^r_r, 80/3 vs 16.
- Weighted effect: 210·(1/140)·(32/3) = (3/2)·(32/3) = **16,
  exactly** the Phase 259 residual.
- Substitution bracket with the gate's derived tensor:
  Δ = (0, −16, 0); Phase 259 FULL residual (0, +16, 0) → arbitrated
  **(0, 0, 0), exact**.

At the A throat (H(3) = (3, 3/2, 39/8), H(4) = (3/4, 3/4, −3/8) —
the record's joint-consistent set, replicated by Phase 323 and not
separately isolated there, as Phase 318 recorded):

- REST_derived(A) from the gate's H{2,0}(3)(A) =
  **(−23/5040, −13/5040, −31/5040)** — Phase 323's value exactly.
- Δbracket = (0, −2, +7); Phase 259 FULL A residual (0, +2, −7) →
  arbitrated **(0, 0, 0), exact**.
- Recorded for exactness: the A-side implied print tensor is
  (9/4, 25/12, 7/12), differing from the derived in T^r_r and T^θ_θ.
  The "one printed number" statement of claim (i) is an Ellis-throat
  statement (the core at which the attribution was made and at which
  H(3)/H(4) are individually pinned); at A the print aggregate is
  one back-out equation in three tensors, and what the identification
  requires there — the derived tensor closing the core exactly — is
  what deciding read (2) confirms. This is a scope note on the
  record's arithmetic, not a defect in any claim.

### Deciding read (4) — the Ellis gate coefficient 203 → 187

P(ξ) is the assembled throat T^r_r bracket polynomial (harness
`ellis_gate`: P_coefs := throat Tr array; its target array is
confirmed identical to the THA Tr target polynomial
[187, −1806, 5460, −4200] read from the record).

- Stored FULL P₀ = 203.00000000000006 (float assembly residue of the
  exact 203). The REST substitution is ξ⁰-only and moves P₀ by
  exactly the Tr bracket delta of read (3): **203 − 16 = 187,
  exact** — the target coefficient.
- Arbitrated P(ξ) = 187 − 1806ξ + 5460ξ² − 4200ξ³: exactly one root
  in [−1, 2]; exact-rational bisection gives the root
  0.8603576689230… vs the target 0.86035766893 (deviation
  7.0×10⁻¹², the target's own printed rounding).
- NEC consequence, **recomputed by this gate** (Phase 318 had
  labelled it attribution-based): the arbitrated NEC polynomial
  −Tt_target + Tr_arbitrated has roots
  0.1515510908248 / 0.2595996822049 / 1.4221825603037 vs targets
  0.15155109082 / 0.25959968220 / 1.42218256030 — max deviation
  4.9×10⁻¹², again the targets' printed rounding.
- Stage B Δp_r with the arbitrated Tr at ξ = 1/6:
  9.15821986×10⁻⁵ vs target 9.158220×10⁻⁵ (relative deviation
  1.5×10⁻⁸ — the same residue class as the already-passing Δρ and
  Δp_t reads, 2.5×10⁻⁸ and 1.2×10⁻⁸, and inside the target's print
  precision).

### Deciding read (5) — wider-set collapse spot-checks

With the gate's own H{2,0}(3) values and the stored per-point
H(3)/H(4)/REST_print inputs (Phase 323 reassembly record):

- **C:1/2** (the C maximum point): FULL ξ⁰ cells (−3.6×10⁻¹², 250.0,
  117.0) → arbitrated max |cell| **5.5×10⁻¹³** (stored: 5.1×10⁻¹³).
- **E:1/10** (the E maximum point): FULL ξ⁰ cells (85.51, 108.04,
  14.51) → arbitrated max |cell| **2.5×10⁻¹²** (stored: 2.8×10⁻¹²).

Both collapses reproduce at the float-residue floor of the stored
inputs (the small differences from the stored arbitrated values are
the stored inputs' float rounding, not a discrepancy: the gate's
H{2,0}(3) inputs are exact and identical to Phase 323's).

## §5 Claim set — the only quotable form

> **G37-A (the attribution).** The Phase 259 ξ⁰ throat residual
> (+16.0 in T^r_r at the Ellis throat) is carried by exactly one
> printed number: the joint REST arithmetic — REST_print =
> (44/135, 4/27, 100/189), rebuilt exactly in this gate from the
> implied print tensor and independently derived H(6,3)(3) =
> (32, 8, 44) and H(6,3)(4) = (4, 4, 16) — implies print
> H{2,0}(3) = (80, 80/3, 112) at the throat, against the derived
> (80, 16, 112): T^t_t and T^θ_θ agree exactly, T^r_r differs by
> 32/3, whose weighted assembly effect is (3/2)·(32/3) = 16,
> exactly the residual. The derived tensor was reproduced by this
> gate's independent variation machinery (E2 = E[−(∇Ric)²] =
> (−80, −16, −112) at the throat, divergence exactly 0).
>
> **G37-B (the A-throat evaluation).** Derived H{2,0}(3) at the
> A-family throat = **(9/4, 3/4, 21/4)** DF print units, exact —
> Phase 318's registered prediction, confirmed by Phase 323's two
> routes and reproduced by this gate's third, independent route
> (divergence exactly 0; Ricci lock (0, −1, 1/2)). With it, the
> A-throat core ξ⁰ residual (0, +2, −7) is cancelled exactly:
> REST_derived(A) = (−23/5040, −13/5040, −31/5040), Δbracket =
> (0, −2, +7), arbitrated residual (0, 0, 0).
>
> **G37-C (the identification).** Under the fully arbitrated
> assembly of Phases 259/318/323 as re-judged here, T_S is
> identified in the registered form only: against THA's targets on
> the harness cores (Ellis + A) and the Ellis gate, at all powers.
> The gate's own re-derivation covers the ξ⁰ sector end-to-end
> (both cores exact (0, 0, 0); the gate polynomial's ξ⁰ coefficient
> 203 → 187 exactly, its root and the NEC roots on target at the
> targets' printed rounding, Δp_r on target in the passing residue
> class; the wider-set ξ⁰ maxima at C and E collapse under the same
> substitution, spot-checked at their maximum points), and the
> ξ¹/ξ²/ξ³ sectors stand on Phase 259's certificates, unchanged by
> the ξ⁰-only substitution.
>
> **Fences (part of every claim above).** Identification is in the
> registered form only (harness cores Ellis + A and the Ellis gate,
> all powers, fully arbitrated assembly). Phase 259's D1 stands:
> the ξ⁰ residual was not a reading artefact. The D2 generic-θ gap
> remains a gap. The THA Eq. (26) ξ³ defect stands. No wormhole
> construction, no traversability claim, and no FTL claim follows
> from this verdict.

## §6 Incidents

One, in the gate's own machinery: the first Ellis-throat run
returned float-typed values — a series-inverse helper produced a
float constant seed (1/int) that silently floated the σ jet. Caught
by a type audit before any deciding read was quoted; fixed
(type-preserving unit constants); every deciding value in this gate
is from the post-fix runs and is an exact Fraction, with the
divergence and off-diagonal certificates exact. The pre-fix float
values agreed with the post-fix exact values at every quoted digit.

## §7 Provenance and artefacts

Charge: ledger entry 810. Records read: ledger entries 789, 802,
807; `phase318/CHECKPOINT318.md`, `phase318/results/p318_memo.md`;
`phase323/CHECKPOINT323.md`, `phase323/results/p323_memo.md`;
`phase259/CHECKPOINT259.md`, `phase259/results/
p2591_gate_readout.md`, `p2591_assembled.json`;
`phase323/work/p323_exact_jets.json`, `p323_eval_points.json`,
`p323_reassembly.json`, `p323_validate.json`. Gate machinery:
`gate37/work/g37_jets.py`, `g37_engine.py`, `g37_run.py` →
`gate37/work/g37_results.json`; `g37_arithmetic.py` →
`gate37/work/g37_arithmetic.json`. Nothing was written outside
`gate37/`; no ledger append was made by this gate.
