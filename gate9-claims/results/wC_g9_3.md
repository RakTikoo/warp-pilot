# W-C — GATE-9, claim G9-3 (STABILITY of the conformal joining member's interior background)

Worker W-C, Gate 9. Run with the programme venv
`~/workspace/warp-pilot/venv/bin/python` (stated per protocol).
All code fresh in `gate9/` (`wc_*.py`); no phase script was imported
or re-run. Shared *definitions* only were taken as text: the profile
forms P1 = (r−1)²/r⁴, P2 = (r−1)²/r⁵, the static trial families
δb ~ (r−1)²/r², δΦ ~ (r−1)²/r⁴, the Galerkin quotient method
description (P38-2/P71-1 memos), and the Bach definition in its
Ricci form (arXiv:2505.17171 eq.6 — the form the phase record uses).

**Correctness verdict: REPRODUCED.**
**Novelty verdict: PARTIALLY KNOWN** (exact known part cited in §5).
Checker: `wc_checker.py` over `results/wc_g93_numbers.json` —
**20/20 PASS**.

---

## 1. Machinery re-gate on T-b (BEFORE any member number) — PASS

Fresh quotient-spectrum machinery: my own symbolic derivation of
the Weyl² density Q = √−g C² for the log-metric
ds² = −e^{2a}dt² + e^{2b}dr² + e^{2c}r²dΩ² (`wc_symq.py`; the
simplified C² has 130 terms), lambdified and driven by my own
Galerkin code (`wc_dyn.py`: 5-point ε-FD of the time-averaged
integrated density, Nr = 1000, nt = 8, averaged fit through
ω = 1,2,3 and snapshot fit through ω = 0,1,2, quotient scan on
ω² ∈ [−5, 0] at 2001 points, gauge eigenvalue identified by
eigenvector alignment with (1,1,1)/√3 — a bare determinant was
never read as a result anywhere).

T-b (b = r₀(r/r₀)^{1/2}, Φ = 0), averaged fit, smallest physical
eigenvalues from MY run:

| block | mine | stored (P71-1 re-run) |
|---|---|---|
| P1, R=10 | **0.0026528417913793652** | 0.00265284 |
| P1, R=20 | 0.0026671074229840685 | 0.00266711 |
| P1, R=30 | 0.0026678090638160602 | 0.00266781 |
| P2, R=10 | **0.000876709357515032** | 0.00087671 |
| P2, R=20 | 0.000876873300458329 | 0.00087687 |
| P2, R=30 | 0.0008768767323317112 | 0.00087688 |

Bar: within 5% at R = 10 — met at ~1e-7 relative (the values agree
with the stored re-run values to every digit the phase printed).
No zero crossing and no negative physical eigenvalue in any T-b
block (0 crossings, 0 negative scan points, both extractions).
Gauge anatomy verified structurally on T-b: max |det M| over scans
3.14e-9 (identically-zero determinant at instrument precision),
null row-sum residuals ≤ 1.04e-8, null-eigenvector alignment
≥ 0.99999999999993 — det M ≡ 0 with null vector (1,1,1), as
registered. The re-gate passed, so member numbers were read.

## 2. (a) Static sector — REPRODUCED

Fresh Bach tensor in jet space (derivatives of A = Φ and
B = −½ln(1 − b/r) as symbols, radial derivative as the jet
operator) in the Ricci form (`wc_bach5.py`):
B_mn = □R_mn − ⅓∇_m∇_nR − ⅙g_mn□R + 2R^{rs}R_{m r n s}
− ½g_mn R^{rs}R_rs − ⅔R R_mn + ⅙g_mnR².
Anchors, all passed BEFORE the member traces were read:
T-b closed forms reproduced with closed/mine ratio
1.0000000000000000 at every radius and component (control max rel
err 9.9e-15); Schwarzschild Bach-flat to ≤ 1.9e-17; trace of the
derived tensor zero numerically on random jets to 2.0e-15.

Member (p = 0.1, Φ₂, a = 0.277734), from MY run (`wc_static.py`):
background B reproduces the stored spot values to 2.7e-14 relative.
Linearised-Bach traces:
- float64 (centred FD, ε = 1e-4 with halving check): max |trace|
  1.39e-11 (δb family), 2.41e-11 (δΦ family) — same instrument-noise
  class as the stored ≤ 2.9e-12 (mine is the noisier FD evaluation;
  the deciding precision is the 40-digit read below).
- **40-digit mpmath probes at 6 radii** {1.05, 1.5, 2, 10, 100,
  1000}: traces δb / δΦ = −3.13e-34 / +3.00e-34 (r = 1.05),
  −1.00e-35 / +4.30e-36 (1.5), −9.87e-37 / −1.88e-36 (2),
  −4.18e-39 / −2.17e-39 (10), +7.28e-44 / −1.20e-44 (100),
  +1.34e-47 / +4.69e-48 (1000). **Max |trace| = 3.13e-34**, against
  the bar |trace| < 1e-25 (stored read ≤ 5.7e-31). PASS by ~9
  orders of magnitude.

## 3. (b) Dynamic sector — REPRODUCED

Registered grid exactly (no equivalent needed): 2001 scan points
× profiles P1/P2 × R ∈ {10, 20, 30} × both extraction conventions,
from MY machinery (§1). **No zero crossing anywhere; zero scan
points with a negative physical eigenvalue in all 12 blocks.**
Smallest physical eigenvalues (averaged fit, mine):

| block | R=10 | R=20 | R=30 |
|---|---|---|---|
| P1 | **0.004245411313722145** | 0.004264737164045491 | 0.00426556018760345 |
| P2 | **0.0012174053847267233** | 0.0012175805464631508 | 0.0012175837238155118 |

Bars: P2-averaged within a factor 2 of 0.00121741 — met at ratio
1.0000 (value agrees with the stored 0.00121741 to all printed
digits); P1 within a factor 2 of 0.00424541 — met at ratio 1.0000.
Snapshot-convention minima are the expected factor-2 partners
(P2 R=10: 0.002434811990295628). Gauge anatomy on the member:
max |det M| 3.97e-9, null row-sum residuals ≤ 2.13e-8 — the same
structural det M ≡ 0 anatomy, anatomised as such; no raw
determinant sign or bracket was read anywhere. R-independence in
the P38-2 sense holds (P2 spread ≤ 1.5e-4 relative).

## 4. (c) Principal symbol — REPRODUCED (flat quotient spectrum independently re-derived)

Both registered routes were in effect run: (i) P71-1's transfer
argument premises checked on the member — the symbol is a
pointwise-algebraic object of the operator; the member background
is smooth and non-degenerate on the interior (1 − r^{−0.9} ∈ (0,1)
for r > r₀, e^{2Φ₂} finite and nonzero, Φ₂ ∈ [0, 0.2426), all
background derivatives finite for r > r₀, Φ₂′(r₀) = a finite);
(ii) the controlling computation, P61-3's flat quotient spectrum,
re-derived independently and exactly (`wc_symbol.py`): linearised
Bach symbol on Minkowski, plane wave along z, full 10-component
polarisation space, sympy-exact. MY results:
- gauge nullspace exact: all 4 diffeomorphism directions and the
  1 conformal direction are exact null directions of the symbol
  matrix for all (ω, k) (symbolic zero, not numeric);
- rank M = 5 off the cone (at (ω,k) = (2,1) and (3,1));
- every physical eigenvalue equals **−Q²/4** (×5) in my
  normalisation, Q := ω² − k² (at (2,1): −9/4 ×5 with Q² = 9; at
  (3,1): −16 ×5 with Q² = 64) — hence the quotient determinant is
  −Q¹⁰/1024 in my normalisation, i.e. the same Q¹⁰ factorisation
  with the same sign as P61-3's −Q¹⁰/24; the constant differs by
  symbol normalisation/basis conventions (P61-3 itself records a
  factor 2 between its Ricci-form and Weyl-form symbols, and its
  sector coefficients −Q²/2, −Q²/2, −2Q²/3 are inner-product
  quotient eigenvalues, whereas mine are the map eigenvalues in the
  coefficient basis — the deciding content, the Q² factorisation
  per polarisation and the absence of any other branch, is
  identical);
- TT polarisations are exact eigenvectors with eigenvalue
  −(w² − k²)²/4; the scalar sector's physical eigenvalue is the
  same −Q²/4 with the remaining scalar directions gauge;
- on the cone (ω = k) all eigenvalues vanish and the matrix keeps
  rank 1 — the nonzero nilpotent on-cone remnant P61-3 recorded
  for the scalar block;
- single-component vector trial e_xz is NOT an eigenvector (it
  mixes with e_tz) — the P38-2 single-component anatomy again; the
  coupled spectrum above is the deciding read.
Dispersion, every physical polarisation: ω² = k², a double root
(the (□)² double light cone). No tachyon branch, no branch with
ω²/k² → c² ≠ 1, no superluminal characteristics.

## 5. Novelty — PARTIALLY KNOWN

Search log: `results/wc_search_log.md` (8 queries verbatim,
arXiv + INSPIRE-HEP + Semantic Scholar + general web, 2026-11-22).

Known part (exact): the bare headline "wormholes in conformal
gravity that are stable at the linear perturbation level" is
already in the literature — **Cadoni, Modesto, Pitzalis & Sanna,
arXiv:2503.14214 [gr-qc], JCAP 06 (2025) 016,
DOI 10.1088/1475-7516/2025/06/016** — for wormholes built by Weyl
rescaling of Minkowski space, analysed in a conformally invariant
scalar–tensor theory with a Morris–Thorne shape function. That is
a different theory sector (scalar–tensor, conformally flat
backgrounds), a different background (not a matter-held
pure-Weyl/Bach member with T = 4α_gB joined to a
Mannheim–Kazanas exterior), and a different method (no linearised-
Bach Galerkin quotient spectrum, no static linearised-Bach trace
audit). Neighbouring construction-only works: Hohmann et al.,
arXiv:1802.02184, JCAP 10 (2018) 003; Lobo, arXiv:0801.4401;
vacuum wormhole arXiv:0907.1128 — none computes a stability
spectrum. Bronnikov & Grinyok, arXiv:gr-qc/0411063, prove
scalar–tensor conformal-continuation wormholes UNSTABLE under
spherical perturbations — different theory, opposite verdict, not
a Bach-operator analysis.

Not found in our search: any linearised-Bach stability analysis
(static traces or dynamic quotient spectrum) of a matter-supported
Morris–Thorne background in pure conformal (Weyl) gravity, and
anything treating this joining member. The specific claim and its
numbers are therefore not found in our search (limits: §6), but
the claim may not be worded as a "first/novel stable conformal-
gravity wormhole" — Cadoni et al. hold that headline for their
class. Hence PARTIALLY KNOWN, not NOVEL.

## 6. Coverage gaps (plainly)

INSPIRE-HEP was reached only through web-indexed records, not a
direct INSPIRE API/literature session; Semantic Scholar only via
general-web queries aimed at its index, not its API or site
search; arXiv through the search index and returned arXiv
pages/full texts, not an exhaustive listing-API sweep of
gr-qc/hep-th; non-English and paywalled-only literature not
systematically covered. A search that could not be run as a
native database session is a gap, not a negative result.

## 7. Failure-protocol ledger (my own instrument failures, all anatomised)

| Failure | Anatomy | Disposition |
|---|---|---|
| First Weyl-form Bach assembly (`wc_bach_derive.py`, full-tensor route) | Final symbolic simplify intractable in-item (killed after ~12 min wall in that stage); no number used from it | Superseded by jet routes; retained as an artefact |
| Jet Weyl-form Bach (`wc_bach2.py`, then `wc_bach3.py` v1) | Components wrong on non-Ricci-flat backgrounds (Schwarzschild leftover B^t_t = −2B^θ_θ ≠ 0): my covariant-derivative loops SKIPPED components whose value is zero — but a zero Weyl component can have a nonzero covariant derivative via Γ^r_{θθ} mixing (e.g. ∇_θ C^t_{tθt} = −Γ^r_{θθ} C^t_{trt} ≠ 0). The two P38-2-style instrument scares in my path were exactly this class: never read raw | Skip removed (`wc_bach3.py` v2): Schwarzschild then Bach-flat to 1e-18 |
| Jet Weyl-form Bach, no-skip (`wc_bach3.py` v2 / parts in `wc_bach4.py`) | Schwarzschild AND de Sitter Bach-flat, Ricci and Weyl separately verified (Weyl traces exactly 0; T-b Ricci satisfies Bianchi exactly), yet NO combination DD ± ½RC in either divergence placement reproduced the T-b closed forms (best ratio spread 2.28). The ∇∇C assembly error was not isolated to a sign or placement in the time available | DISCARDED as an instrument. The deciding static read uses the Ricci form (the phase's own definition form), implemented fresh (`wc_bach5.py`) and anchor-validated to ratio 1.0000000000000000 on T-b closed forms AND on the member's stored background values, Schwarzschild-flat to 1.9e-17. The Weyl-form/Ricci-form disagreement is my assembly's, recorded here; it does not touch the claim, whose static content (traces) is form-independent |
| Flat-symbol first run (`wc_symbol.py` v1) | Ricci contraction omitted the η^{aa} sign (eigenvalues not ∝ Q², conformal direction not null) | Fixed; v2 gives the exact results of §4 |
| Concrete-function Bach variant test (`wc_bach_concrete.py`) | Too slow under shared-CPU contention; killed in its DD2 stage after Weyl/DC stages; no number used from it | Superseded by the jet Ricci-form route |
| Static float64 traces noisier than the phase's (≤ 2.4e-11 vs stored ≤ 2.9e-12) | FD evaluation-order noise on O(1) components; the registered deciding precision is the 40-digit read | Reported as-is; 40-digit traces (≤ 3.1e-34) decide |

No zero crossing and no negative physical eigenvalue appeared on
any deciding path. (Had one appeared, the verdict would have been
NOT REPRODUCED with its full anatomy, per the gate bars.)

## 8. EXACT restated wording (the form in which G9-3 survives)

> The conformal (Weyl) gravity joining member — a throat OBJECT
> with b = r₀(r/r₀)^0.1, Φ₂ = a·ln(r/r₀)/(1 + ln(r/r₀)),
> a = 0.277734, Ω = 1, 4α_g·B = T, joined at 10³ r₀ to the
> Mannheim–Kazanas exterior — is CLASSICALLY STABLE in the
> computable interior sectors, as reproduced by an independent
> second path in Gate 9: exact static ℓ=0 linearised-Bach traces
> ≤ 3.1×10⁻³⁴ at 40-digit probes at 6 radii; dynamic ℓ=0 Galerkin
> quotient spectrum with no zero crossing in ω² ∈ [−5, 0) on the
> registered grid (2001 points × profiles P1/P2 × R ∈ {10, 20, 30}
> × both extraction conventions), smallest physical eigenvalue
> 0.00121741 (P2 averaged; P1 0.00424541); principal symbol in all
> ℓ = the (□)² double light cone, with the flat quotient spectrum
> independently re-derived (exact gauge nullspace, rank 5 off the
> cone, every physical eigenvalue proportional to (ω² − k²)²).
> Registered scope, part of the claim: interior sectors only; the
> shell/exterior perturbation problem is OPEN (not computed);
> ℓ ≥ 1 long-wavelength and nonlinear stability are not
> computable; the dynamic read is a Galerkin/variational quotient
> read, NOT an exact spectrum; the packet numeric sign check
> remains OPEN; no positive conserved energy exists for the
> radial sector and curved-background linearised-Bach IVP
> well-posedness is unproven — recorded facts, not deciding
> reads. The member's tidal-bar radius is r₀* = 4.785×10⁷ m, and
> its formation standing is PRE-EXISTING ONLY. This is a throat
> OBJECT claim: no transport is claimed and no traversability is
> claimed. (V-b) UNDECIDED: Pais–Uhlenbeck spin-2 ghost vs Mannheim PT-symmetric quantisation — opposed literature positions, B3 NOT COMPUTABLE (Phase 32). Linear-perturbation stability of conformal-gravity wormholes of a different class (Weyl-rescaled-Minkowski / conformal scalar–tensor) is already published (Cadoni et al., arXiv:2503.14214, JCAP 06 (2025) 016); the stability computation for THIS member, in these sectors, was not found in our search (limits: INSPIRE-HEP and Semantic Scholar reached only via web indexes, no exhaustive arXiv listing-API sweep, non-English and paywalled-only literature not systematically covered). The member remains a scan signal under attack — nothing stronger.

## 9. Files

Code (all fresh, `gate9/`): `wc_symq.py` (+ `wc_symq_expr.json`),
`wc_dyn.py`, `wc_bach5.py` (+ `wc_bach_expr.json`),
`wc_static.py`, `wc_symbol.py`, `wc_checker.py`; discarded-route
artefacts `wc_bach_derive.py`, `wc_bach2.py`, `wc_bach3.py`,
`wc_bach4.py` (+ `wc_bach_parts.json`,
`wc_bach_expr_v2_wrongslots.json`), `wc_bach_concrete.py`.
Numbers: `results/wc_g93_numbers.json` (checker-verified),
`results/wc_dyn_tb.json`, `results/wc_dyn_jm.json`,
`results/wc_static.json`, `results/wc_symbol.json`.
Search log: `results/wc_search_log.md`.
Nothing uploaded; nothing outside `gate9/` edited.
