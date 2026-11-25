# P71-5 — LE STEERING-DRIVE GATE AUDIT — MEMO

**Item:** P71-5 (fringe registration R3), Phase 71. **Date:** 2026-11-22.
**Audit target:** An T. Le, "Steering a warp drive without exotic matter,"
**arXiv:2606.22531** (v3 full text + in-paper Supplement §S audited;
identity verified against the arXiv records as the run's first step —
arXiv:2605.25417 is the different Le paper, "On the boundary cost of
source-consistent warp shells," already cited in v1.9.0; context only).
**Auditor:** fresh independent implementation, programme gate pattern
(Phases 50/51/63): FD metric derivatives → algebraic Γ → FD normal
gradient → orthonormal-frame extrinsic curvature → Lanczos surface stress
→ Hawking–Ellis Type-I classification + worst-observer DEC margins
(Eq. (35) form) + sampled-observer cross-check + h-ladder. No author code
run or imported; no warpax/JAX. float64. INTERNAL only; nothing uploaded.

## VERDICT (fixed form)

**FAILS AT NAMED POINTS** — the published dipole-scan frontier pins
(x, a_max·R) = **(0.1, 0.19)** and **(0.3, 0.19)** fail the surface DEC at
the rear pole on the full-angle read: worst-observer DEC margins
**−2.0×10⁻⁴** and **−1.2×10⁻⁴** (pole limits, R = 1 units; h-converged on
h ∈ {0.02, 0.01, 0.005} and on an independent 4th-order discretisation;
deciding condition: surface DEC, σ − p̃ < 0 at θ → π; Hawking–Ellis
Type-I at both points — the failure is a margin failure, not a type
failure). The remaining pins (0.2, 0.20), (0.5, 0.14), (0.7, 0.09) pass,
the static-anchor DEC window 2m/R < 24/25 reproduces **exactly**, and the
frontier bracket itself reproduces (see §3): the corrected full-angle
dipole frontier is λ*(x) ≈ {0.186, 0.203, 0.189, 0.141, 0.091} against the
paper's {0.19, 0.20, 0.19, 0.14, 0.09} — the two failing pins are high by
0.004 and 0.001 in λ because the paper's published angular scan stops
0.15 rad short of the binding rear pole.

## 1. Re-gate (before any Le number)

Control row: Finalist A anchor suite of the programme gate auditor
(gate6 `wa_auditor`/`wa_run`, Phase-50/51 lineage). Stored verdict
(`phase50/results/p501_audit.json`): Minkowski max |G| = 0.0; static ρ
rel. err 0.0030717699532123565; pressure abs. err 9.215029876625953e-08;
Finalist A worst margin +2.141179301461828e-07, Type-I fraction 1.000,
PASS. **Reproduction this run: all four values bit-identical.** The
P71-5 auditor was additionally validated on the paper's static anchor
(FD junction vs closed-form Eqs. (22)–(23): margins agree to ≤5×10⁻⁷)
and on the junction re-derivation (independently solved Darmois tilt
w₁ vs the paper's closed form w₁ = x/(2√(1−x)): agreement ≤1.6×10⁻⁶ at
every audited x) before the frontier scan.

## 2. What reproduces exactly

- **Static anchor and the 24/25 window.** σ₀, p₀ (Eqs. (22)–(23))
  reproduced by an independent Israel/Lanczos junction from the metric
  pair (Schwarzschild ↔ Minkowski) at x ∈ {0.1, 0.3, 0.7} to ≤0.02% on
  the h-ladder. DEC margin σ₀ − p₀ > 0 for every grid x < 24/25
  (x = 0.05…0.95), < 0 at x = 0.97, 0.99, and = 0 at x = 0.96 to 4×10⁻¹⁷
  — the window edge is exactly 24/25, as claimed (factor (5s−1)(s−1)).
- **Junction conditions.** The O(λ) Darmois system [h_ab] = 0 was
  re-solved independently at each x (unknowns ρ₁, At₁, w₁; Ai₁ = 0):
  residuals ≤ 3.5×10⁻⁴ at x ≤ 0.3 (≤1.1×10⁻² at x = 0.7), and w₁ matches
  the paper's closed form (App. C) to ≤1.6×10⁻⁶ everywhere. The shell
  tensor the audit reads is therefore the paper's shell tensor, arrived
  at independently — no discrepancy in the junction re-derivation.
- **Bulk + steering law.** The exterior bulk ECs reduce to n² ≥ 0
  (Prop. 3), and 4πn²(ϑ) = −ṁ − 3ma cos ϑ ≥ 0 ∀ϑ ⟺ −ṁ ≥ 3m|a|
  (Eq. (14)) verified by direct sampling at saturation and at
  ±0.001 around it: the law is exact, not perturbative.
- **Frozen-shape axial threshold.** λ_DEC(x) from Eq. (42) lies strictly
  below the ceiling ½(1−x) at every audited x; ratio to ceiling at
  x = 0.63 is 0.9900 (paper: 0.9931 — agreement within root-finding and
  equation-parse tolerance; the ordering and near-ceiling approach
  reproduce).
- **Ceiling.** ½(1−x) (Prop. 5) is an exterior-regularity identity
  (g^rr = f + 2ar cos ϑ, rear-pole minimum exact); nothing in the audit
  reaches it: all reproduced frontier values sit strictly inside.

## 3. The frontier: bracket reproduced, two pins fail at the pole

Full-angle dipole-scan read (θ ∈ [0.05, π−0.05], binding tracked; pole
band refined to π−0.0125 at the deciding points). At every x the binding
angle is the rear pole (θ → π), as the paper states. Margins at the pins
(h = 0.01; ladder spread ≤ 8×10⁻⁶; 4th-order agrees to ≤9×10⁻⁶):

| x | pin g̲(x) | margin at pin | λ* (full-angle) | verdict at pin |
|---|---|---|---|---|
| 0.1 | 0.19 | **−1.73×10⁻⁴** (pole limit −2.0×10⁻⁴) | 0.186 | **FAIL (DEC)** |
| 0.2 | 0.20 | +3.45×10⁻⁴ | 0.203 | pass |
| 0.3 | 0.19 | **−3.7×10⁻⁵** (pole limit −1.2×10⁻⁴) | 0.189 | **FAIL (DEC)** |
| 0.5 | 0.14 | +2.18×10⁻⁴ | 0.141 | pass |
| 0.7 | 0.09 | +4.58×10⁻⁴ | 0.091 | pass |

Anatomy of the failure (structural, not numerical): the margin decreases
monotonically toward the rear pole and converges to its pole limit
(x = 0.1, λ = 0.19: +4.5×10⁻⁵ at π−0.15, −9.0×10⁻⁵ at π−0.10,
−1.73×10⁻⁴ at π−0.05, −1.99×10⁻⁴ at π−0.0125). The author's published
scan samples θ ∈ [0.15, π−0.15] (their `stress_over_theta`), so at their
nearest sampled angle the margin at both failing pins is still positive
(+4.5×10⁻⁵, +6.5×10⁻⁴) — the failure lives in the unsampled near-pole
band θ ∈ (π−0.10, π), exactly the Phase-50/51 pattern of a failure
between a first-pass audit's registered sample points. At λ = pin − 0.01
the pole-limit margins are positive (+3.3×10⁻⁴, +1.4×10⁻³), so the
corrected full-angle dipole frontier (λ* ≈ 0.186 at x = 0.1, ≈ 0.189 at
x = 0.3) sits 0.001–0.004 below the published pins — inside the paper's
own stated ~5% scan resolution for the pins, but the pins as published
DEC points do not pass at our bars, which read the full angle range.
Type: Hawking–Ellis **Type-I at every pin on every rung** (minimum
discriminant +3.9×10⁻⁶ > 0); no Type-IV anywhere in the scan. The
sampled-observer cross-check at the x = 0.1 pin returned +9.6×10⁻⁵
(it undersamples the worst observer); the exact Eq.-(35) form decides,
as registered.

**Scope of the failure, stated exactly:** this impeaches the published
*dipole-scan pins* as full-angle DEC points. It does **not** directly
impeach the paper's separate nonlinear multipole solve, whose relaxed
configuration is reported to carry strictly positive margins
{1.8, 9.1, 18, 21}×10⁻³ at the same pins — a different (junction-relaxed)
shell whose near-pole margin this audit did not compute (registered
scope limit, run record §3.6). If the multipole shell's pole margin is
indeed positive at those amplitudes, the frontier bracket stands as
published and only the dipole-scan pins' status changes (from "DEC
points" to "scan-resolution locators"). That is follow-up FU-P715-1.

## 4. Volume reads (where a volume representation exists)

- **Radial-tension Kerr–Schild thickening (Eq. (50), closed form):**
  the paper claims it FAILS the DEC — **confirmed, with its law**: for a
  smoothstep wall the worst margin sits at the inner edge and equals
  −|S″(0)|m/(8πr₋δ²) to all printed digits at δ = 0.2, 0.1, 0.05
  (−0.895, −3.581, −14.32), scaling ×4 per halving — the 1/δ² boundary
  cost (Cor. 7) reproduces exactly.
- **Tangential-pressure wall:** the radiative split's discriminant
  Δ = ρ(ρ+4μ) > 0 (Type-I, Eq. (54)) verified on sampled (ρ, μ); the
  margin factor 1 − m/(2(r−2m)) is positive ⟺ local 2m(r)/r < 4/5
  (window edge at exactly 0.8 in the read: passes 0.79, fails 0.81) —
  the published 4/5 window reproduces. (The full numerical thick-wall
  profile is constructed only inside the author's code, not published
  as paper data; the closed-form relations above are the published
  volume content and are what was read.)

## 5. C12 accounting

An accelerating shell paying Bondi mass by photon-rocket recoil is
**subluminal transport bookkeeping (2b-adjacent)**: the drive is causal
and subluminal by construction, its acceleration is ordinary recoil
against outgoing null radiation (−ṁ ≥ 3m|a|; ~51% of rest mass radiated
for Δrapidity 0.24 in the paper's worked burn), and **no FTL content is
claimed by the paper or audited here**. Steering is the gap
Bobrick–Martire named for the constant-velocity positive-energy family
(Fuchs et al.; the programme's own (10,30) rows are constant-velocity).
This audit's verdict speaks **only** to the paper's DEC certification
and frontier bracket, in Gate language: the anchor certification and
the bracket survive; two of five published frontier pins do not pass a
full-angle DEC read at the dipole level. Nothing here is a programme
configuration, a programme claim, or transport by any programme shell.
Context note (not part of the verdict): the stricter source-consistency
standard of the author's own companion paper (arXiv:2605.25417 —
explicit matter model + constraint satisfaction) is a different, higher
bar than the prescribed-geometry/junction standard both the paper and
this audit apply; the thin shell's matter model is a constitutive
hypothesis (the radiating layer of §7.2 of the paper), and that caveat
stands alongside this verdict exactly as it does for Fuchs-class shells.

## 6. Failure Protocol

**Anatomy (the verdict failure).** Deciding term: worst-observer
surface DEC margin σ − p̃ at the rear pole. Mechanism: the matched
shell's margin is pole-dominated and still decreasing at the edge of
the author's sampled band; the published pins were located on a grid
that stops at π−0.15, so the located zeros sit one scan-step high at
x = 0.1 and x = 0.3. Size of the error: ≤0.004 in λ (≤2%), margins
−1.2×10⁻⁴…−2.0×10⁻⁴ — small, named, h-converged, and *not* a refutation
of the construction: the anchor, the junction, the bulk law, the
ceiling, and the bracket all reproduce, and DEC holds at every audited
point with λ ≤ λ*(x).

**Anatomy (auditor instrument failure, caught and quarantined).** The
first full run of this audit returned grossly negative margins
everywhere (anchor σ wrong-signed). Cause: a transposed-index error in
my vectorised Christoffel computation (transpose axes (2,0,1) for the
−∂_s g term; correct: (1,2,0)), introduced when optimising the auditor
after its (correct) loop-form smoke test. It was caught by the anchor
control (FD σ₀ vs Eqs. (22)–(23)), localised by a loop-vs-vectorised Γ
comparison (max diff 0.166 → 3×10⁻¹⁷ after the fix), and **all numbers
from that run were discarded**; every number in this memo is from the
post-fix run, whose anchor, Γ, and w₁ controls all pass. A second,
cosmetic defect (an inverted ratio expectation in the checker's 1/δ²
scaling check) was likewise a checker bug, fixed and documented; it
never touched a result. Isolated RuntimeWarnings (sqrt of a negative
FD-stencil value at isolated off-shell stencil points during the
Darmois probes) did not enter any deciding read: every deciding margin
is smooth and h-stable across three ladder rungs plus the 4th-order
discretisation.

**Follow-ups (≥1 per failure, registered):**
- **FU-P715-1:** independently run the nonlinear multipole Darmois
  solve at the two failing pins with angular sampling to the pole
  (θ → π−0.005) and read its rear-pole margin: decides whether the
  paper's strictly-positive multipole margins at (0.1, 0.19) and
  (0.3, 0.19) survive a full-angle read, i.e. whether the published
  bracket's lower bound stands as DEC points or only as locators.
- **FU-P715-2:** pole-limit frontier map: recompute λ*(x) on the
  pole-refined angular grid over x ∈ [0.05, 0.9] (the corrected
  full-angle dipole frontier as a curve, not five points), and check
  the heuristic envelope (24/25 − x)/2 against it.
- **FU-P715-3:** audit the worked finite-duration burn (Thm. 3,
  x⋆ = 0.3, λ_max = 0.12) per-cut at the pole band: λ_max = 0.12 is
  below λ*(0.3) ≈ 0.189, so the burn is expected to pass; the read
  would close the time-assembly's DEC content at our bars.

## 7. Deliverables and checker

- `results/p715_runrecord.md` — identity verification, data gate,
  adaptation registration, run log.
- `results/p715_results.json` — all audit numbers; `results/p715_pole.json`
  — near-pole refinement at the deciding pins.
- `work/p715_lib.py` (auditor), `work/p715_main.py` (run),
  `work/p715_checker.py` (bars) → `results/p715_checker.json`:
  **48/56 checks passed**; the 8 failures are exactly the pin-DEC rungs
  (4 ladder/discretisation rungs × the 2 failing pins) that constitute
  this verdict. float64 throughout.
