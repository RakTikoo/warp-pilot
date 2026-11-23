# W-C — G7-3: The Procaccia Strengthening

**Worker:** W-C · **Date:** 2026-11-22 · **float64 everywhere** ·
nothing uploaded, no external contact, no phase record edited.
**Code (fresh, in `gate7/`):** `wc_recon.py` (shared-definition
reconstruction), `wc_auditor.py` (fresh auditor), `wc_run.py`
(driver), `wc_crosscheck.py` (cross-check anatomy + exact min-null),
`wc_check.py` (checker over the result JSON).
**Numbers:** `results/wc_g73_numbers.json` · **Search log:**
`results/wc_search_log.md`.
**Python:** programme venv `~/workspace/warp-pilot/venv/bin/python`
(numpy 2.5.5 / scipy 1.18.1).
**Verdict path (stated before running):** full audit at β = 0.1363 on
the P50-1 point set at the re-registered h-pair h = 0.0375 AND
h = 0.01875, 2nd-order direct-∂² FD (Gate-6 `wa_auditor.py` pattern,
fresh code). Second path (Bar 4): 4th-order direct-∂² at h = 0.0375.
No Phase-50 or archive code was executed or imported; the
reconstruction re-implements the shared definition (paper §2/§3 as
transcribed by `p501_recon.py`, read as text), and the only archive
material used is the hashed design-vector DATA file.

## Plain language first

Phase 50 rebuilt Procaccia's warp shell from his own posted files and
found it legal at β = 0.1363 everywhere its machinery could see
clearly — but its pre-registered grid spacings (h = 0.3 / 0.15 m) were
far coarser than the design's 0.05 m switch, so the verdict had to be
"confirmed weaker": the bars as literally written failed on stencil
artefacts at the switch. This gate ran exactly the registered fix: a
fresh full audit at spacings that resolve the switch (h = 0.0375 and
0.01875 m), plus a second, different discretisation, plus the
machinery cross-check at his proven-failure point.

**The claim passes.** At both registered spacings the shell is
Hawking–Ellis Type-I at every significant point, all four energy
conditions hold with the worst margin more than 100× above the
measured numerical noise floor, and the independent second
discretisation agrees on every deciding sign. At β = 0.1364 the same
machinery finds his proven violation at his exact point, and — once
the minimum null contraction is computed exactly instead of by
direction sampling — at his exact size: −1.294×10⁻⁷ (2nd-order) and
−1.301×10⁻⁷ (4th-order) against his interval-proven −1.30135×10⁻⁷.
Procaccia's claim is **CONFIRMED AT OUR BARS**. The claim remains
his; what is ours is this independent confirmation and its exact
scope (below).

## Verdict

**CONFIRMED AT OUR BARS** — Phase-50 Bars 1–4 all pass at the
re-registered spacings, and the registered machinery cross-check
passes. Checker: `wc_check.py` over `wc_g73_numbers.json` →
`VERDICT: CONFIRMED AT OUR BARS`.

## Step 0 — Hash gate (before any audit number was read): PASS

SHA-256 of all three design-vector copies in `phase50/procaccia/`:

| Copy | SHA-256 |
|---|---|
| `cont/continuum_cert_code/x_slp2.npy` | a8814dfb6273956da9656379a8dd887218ecc28cbafb03fc87f980c07510d74a |
| `opt/optimal_shift_code/results/x_slp2.npy` | a8814dfb6273956da9656379a8dd887218ecc28cbafb03fc87f980c07510d74a |
| `opt/optimal_shift_code/results/slp2.npy` | a8814dfb6273956da9656379a8dd887218ecc28cbafb03fc87f980c07510d74a |

All equal the registered hash. Design vector: 12 spline coefficients,
q = 1.47837873, r_m = 16.79963062 m (paper rounds q = 1.47838,
r_m = 16.79963 ✓).

## Step 1 — Fidelity spot check (my run): PASS

Reconstruction vs the paper's §2/§3 printed values:

| Quantity | Mine | Paper | Rel. err. | Bar |
|---|---|---|---|---|
| M | 6.1128857378489 | 6.11288573784887775 | 3.6×10⁻¹⁵ | ≤ 1×10⁻⁹ |
| a(R_in) | −0.5847109564396 | −0.58471095644715724 | 1.3×10⁻¹¹ | ≤ 3×10⁻⁸ |
| λ | 0.27839574685 | 0.27839575423 | 2.7×10⁻⁸ | ≤ 3×10⁻⁸ |
| k | 0.0302774971489 | 0.0302774968097 | 1.1×10⁻⁸ | ≤ 3×10⁻⁸ |
| ∫F/r² dr | 33.0278290535 | 33.0278294235 | 1.1×10⁻⁸ | ≤ 3×10⁻⁸ |
| ρ_max | 2.02047546×10⁻⁴ | 2.0204755×10⁻⁴ | 2.0×10⁻⁸ | ≤ 3×10⁻⁸ |

Matches P50-1's achieved tolerances. Fresh-auditor sanity anchor:
Minkowski max|G| = 0.0 exactly.

## Step 2 — Verdict path: my deciding numbers per bar

Point set: the P50-1 set exactly as constructed by `p501_audit.py`'s
`main()` — the (10,20) fine set (858 pts) + support-edge / switch /
fringe clusters (572 pts) = **1,430 point-rows** over 988 significant
points (significance threshold 2.07×10⁻⁷, the shared convention).
Shell region = support [2.734, 27.265] m; all significant points lie
in the shell. (Prose discrepancy, flagged not hidden: GATE7.md and
the P50-1 memo say "1,352 points"; the code construction they name
produces 1,430 rows — 55 radii × 26 directions, with radii 3.0 and
4.0 m appearing in both the fine set and the edge cluster, i.e.
1,378 distinct points. The audited set is the registered code
construction, unchanged; duplicates are exact repeats and cannot
change any minimum or a 1.000 Type-I fraction. Erratum owed to the
prose count — see follow-ups.)

**Bar 1 — Type-I fraction = 1.000 at both spacings: PASS.**
Type-I fraction 1.000, **0 non-Type-I points** among the 988
significant points, at h = 0.0375 and at h = 0.01875 (and on the
second path).

**Bar 2 — worst margins > 0, sign-stable, ≥ 3× FD floor: PASS.**

| Spacing | NEC | WEC | SEC | DEC | Worst | FD floor | Worst / floor |
|---|---|---|---|---|---|---|---|
| h = 0.0375 | +5.008×10⁻⁷ | +5.008×10⁻⁷ | +3.404×10⁻⁷ | +4.290×10⁻⁷ | **+3.404×10⁻⁷ (SEC, r = 5.0)** | 3.11×10⁻⁹ | **109.5×** |
| h = 0.01875 | +4.989×10⁻⁷ | +4.989×10⁻⁷ | +3.398×10⁻⁷ | +4.310×10⁻⁷ | **+3.398×10⁻⁷ (SEC, r = 5.0)** | 2.51×10⁻⁹ | **135.5×** |

Sign-stable across the pair (worst margin changes by 0.2%); NEC/WEC
binding at r = 25.0 m, DEC at r = 25.0 m. Cross-check against P50-1's
own refined reads: their h = 0.0375 worst was +3.404×10⁻⁷ — mine
+3.4042×10⁻⁷, agreement to 4 significant figures.

**Bar 3 — sampled-null NEC min > 0 on the shell: PASS.**
+8.999×10⁻⁸ (h = 0.0375) and +8.945×10⁻⁸ (h = 0.01875), both at
r = 25.0 m, 162 Fibonacci directions. (P50-1 at h = 0.0375:
+9.00×10⁻⁸ ✓.)

**Bar 4 — second path agrees on every deciding sign: PASS.**
4th-order direct-∂² at h = 0.0375, same set: Type-I 1.000 (0
non-Type-I), NEC +4.982×10⁻⁷, WEC +4.982×10⁻⁷, SEC +3.396×10⁻⁷,
DEC +4.317×10⁻⁷, worst +3.396×10⁻⁷ (SEC, r = 5.0), sampled-null NEC
min +8.927×10⁻⁸. Every deciding sign agrees with the verdict path.

## Step 3 — Machinery cross-check at β = 0.1364, point (0, 16.635, 0): PASS (after anatomy)

Requirement: site ladder h ≤ 0.0375 down to ≤ 0.00234375 must find
non-Type-I or negative min null contraction, magnitude within 25% of
his −1.30135×10⁻⁷.

- **Type:** the tensor at his point is Type-I at h = 0.0375 and
  **non-Type-I at every h ≤ 0.01875** — the violation is found, at
  his point. (At β = 0.1363 the same point is Type-I at all spacings,
  eigenvalue NEC converging +1.007×10⁻⁵ → +4.565×10⁻⁶, matching
  P50-1's ladder digit-for-digit.)
- **Magnitude — the anatomy that had to be resolved first.** The
  minimum null contraction is min over unit n of
  T₀₀ + 2s·n + nᵀPn in the Eulerian frame; the minimiser is
  n ≈ (1,0,0) (the shift axis) and the form varies on the scale of
  |T| ~ 10⁻⁴ while its minimum is ~10⁻⁷, so *direction sampling
  under-resolves it*: a 5,002-direction Fibonacci sample reads only
  −3.4×10⁻⁸ at h = 0.0046875, and P50-1's 20,000-direction sample
  read −1.245×10⁻⁷. (My 20,000-direction sample reproduces P50-1's
  −1.2452×10⁻⁷ exactly, confirming the tensors are identical; the
  gap was never in the tensor.) Computing the minimum **exactly**
  (dense sample + constrained optimisation on the sphere,
  cross-validated by an independent Lagrange-multiplier secular
  solve — the two agree to ~10⁻¹³):

| h | β = 0.1364 exact min null | β = 0.1363 exact min null |
|---|---|---|
| 0.0375 | +7.46×10⁻⁸ (Type-I) | +2.565×10⁻⁷ |
| 0.01875 | −8.18×10⁻⁸ | +1.002×10⁻⁷ |
| 0.009375 | −1.182×10⁻⁷ | +6.38×10⁻⁸ |
| 0.0046875 | −1.272×10⁻⁷ | +5.49×10⁻⁸ |
| 0.00234375 | **−1.2938×10⁻⁷** | +5.27×10⁻⁸ |
| 0.00234375, 4th-order | **−1.30122×10⁻⁷** | +5.19×10⁻⁸ |

  The 2nd-order finest value deviates from his −1.30135×10⁻⁷ by
  **0.58%**; the 4th-order value by **0.010%** — far inside the
  registered 25% band. At β = 0.1363 the exact min null at his point
  stays positive (+5.3×10⁻⁸). **Cross-check PASS.** (Note for the
  record: P50-1's quoted −1.245×10⁻⁷ was itself a 20,000-direction
  sample of this same quantity; the exact value is −1.294×10⁻⁷ at
  that discretisation's finest spacing. No bar was affected — the
  25% band covers both — but the exact computation is the better
  number and is what this gate reports.)

## Novelty axis (audit standing only)

**Verdict: NOVEL** — as an independent confirmation, this audit
(Phase 50's P50-1 plus this strengthening) has no prior instance
found. Documented search (2026-11-22; full log with verbatim queries
in `results/wc_search_log.md`): arXiv + INSPIRE-HEP + Semantic
Scholar + general web. No prior independent audit, confirmation, or
refutation of Procaccia's claim was found; no refereed or arXiv
version of either Procaccia paper was found — the only sources for
the claim are his own academia.edu posting ("Continuum
Energy-Condition Certificates for an Optimized Positive-Energy Warp
Shell", posted Oct 30, 2026, https://www.academia.edu/180109147/Continuum_Energy_Condition_Certificates_for_an_Optimized_Positive_Energy_Warp_Shell)
and his figshare datasets (DOI 10.6084/m9.figshare.34866243.v1 and
10.6084/m9.figshare.34895667.v1). The "independent audit" language
inside his paper refers to his own internal re-audit of his cell
cover — self-audit, not independent confirmation. Neighbouring warp
energy-condition literature found (Le, arXiv:2602.18023; Le,
arXiv:2605.25417; Barzegar et al., arXiv:2602.16495) does not audit
Procaccia's design.

**Coverage gaps (stated plainly):** INSPIRE-HEP and Semantic Scholar
were checked only through general-web queries naming them; their own
search interfaces were not queried directly, so a record indexed
only inside those databases could have been missed — those two
checks are partial, not negatives. The arXiv check was by
author/title/keyword over the general web index, not an arXiv API
listing search.

## C12 accounting

This is a **prescribed-geometry audit**: the stress tensor audited is
the one the metric implies through the Einstein equations, and
conservation is automatic (Bianchi) — the same standard as Fuchs /
Phase 26 / Gate-6, and the scope Procaccia states in his own paper.
**No matter model, formation route, or stability is claimed, by him
or by us.** Le (arXiv:2605.25417)'s stricter source-consistency
standard is a standing caveat, not a bar.

## EXACT restated wording for the confirmation, as it may be uploaded

> Independent confirmation (2026-11-22): We have independently
> audited the warp-shell design of F. Procaccia, "Continuum
> Energy-Condition Certificates for an Optimized Positive-Energy
> Warp Shell" (posted 30 October 2026 on academia.edu; unrefereed;
> no arXiv version), reconstructing its continuum geometry from the
> paper's §2/§3 formulas and its published design vector (SHA-256
> a8814dfb6273956da9656379a8dd887218ecc28cbafb03fc87f980c07510d74a,
> verified against all three published copies). With an independent
> finite-difference Einstein-tensor auditor whose stencil resolves
> the design's 0.05 m switch (grid spacings h = 0.0375 m and
> h = 0.01875 m; confirmed by a second, fourth-order discretisation
> agreeing on every deciding sign), the design satisfies the null,
> weak, strong and dominant energy conditions at β = 0.1363 at every
> significant audited point of the full audit set (Hawking–Ellis
> Type-I fraction 1.000; worst margin +3.40×10⁻⁷, more than 100×
> the measured numerical floor), and at β = 0.1364 the same
> machinery finds the violation Procaccia proved, at his exact
> point (r = 16.635 m, θ = 90°), with minimum null contraction
> −1.29×10⁻⁷ (second-order) / −1.30×10⁻⁷ (fourth-order) against his
> interval value −1.30135×10⁻⁷. Scope: this is a
> prescribed-geometry audit — the stress tensor checked is the one
> the metric implies through the Einstein equations — and it claims
> no matter model, formation route, or stability for the design.
> Under the stricter source-consistency standard of Le
> (arXiv:2605.25417) the design is not certified; that standard is
> carried as a standing caveat, not as a bar of this audit. The
> claim and the design are Procaccia's; ours is only the
> independent confirmation and its stated scope.

## Follow-ups / errata owed (recorded, not executed)

1. Prose point-count erratum: GATE7.md §G7-3 and the P50-1 memo say
   the audit set has 1,352 points; the `p501_audit.py` construction
   both name produces 1,430 point-rows (1,378 distinct). The set
   itself was never in doubt; the count in prose should be corrected
   at integration.
2. P50-1's cross-check magnitude (−1.245×10⁻⁷) was a
   20,000-direction sample of the min null contraction; the exact
   value at the finest ladder spacing is −1.294×10⁻⁷ (2nd-order) /
   −1.301×10⁻⁷ (4th-order). Worth a note wherever the sampled number
   is quoted, since direction sampling under-reads this quantity by
   up to ~4× at coarse sample counts.
