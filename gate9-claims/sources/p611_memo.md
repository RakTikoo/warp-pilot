# P61-1 MEMO — THE COEFFICIENT-4 SWEEP (FU-P383-1/2)

Worker item P61-1, Phase 61. Run record (junction conditions, the
α₀ ↔ α_g mapping and the Ŝ₀⁰ sign convention derived and numerically
sign-checked, and what the BDE formalism fixes — all BEFORE any sweep
number): `p611_runrecord.md`. Scripts: `work/p611_signcheck.py`,
`work/p611_junction.py`, `work/p611_follow.py`, `work/p611_freed2.py`,
`work/p611_freed3.py`, `work/p611_ecaudit.py`, `work/p611_locus_ledger.py`,
`work/p611_extra.py`, `work/p611_consolidate.py`, `work/p611_checker.py`.
Checker: **27/27 PASS** over `p611_results.json`. float64; 40-digit
probes at every deciding point.

## Verdict (fixed vocabulary)

**JOINS WITH LEGAL SHELL** — scoped exactly, and no wider:

- **At the primary registered radii r_Σ = 10 r₀ and 10² r₀: DOES NOT
  JOIN.** For every one of the 81 swept interiors (9 shapes × 9
  (Φ, a) profiles), at the registered γ = 10⁻²⁸ m⁻¹ per r₀ with the
  Darmois pair (B, K) matched, the deciding datum **[R̃] is strictly
  positive** (smallest values: +0.061107 at 10 r₀; +0.006982 at
  10² r₀). No sign change anywhere on the primary grid or on a fine
  41-point a-scan; no shell can absorb a [R̃] jump (double-layer
  datum, BDE §III.B).
- **At the labelled extension radius r_Σ = 10³ r₀, registered γ: a
  join lands.** The Φ₂ zero locus a_zero(p) crosses the legal region
  in one sliver: **p ∈ [0.1, 0.10120), a = a_zero(p)** (segment
  endpoint bisected: a_zero(p) = a*(p) at p = 0.101196). Audited
  point: **p = 0.1, Φ₂, a = 0.277734** — [R̃] = 0 (bisection
  residual 4×10⁻¹⁶; 40-digit second path 0.0), [R̃_,n] = −0.015219,
  shell Ŝ₀⁰ = (4α₀/3)(0.015219) = **+0.020291 α₀ ≥ 0 — passes the
  registered shell bar** (the BDE formalism fixes Ŝ₀⁰ only; no
  tangential datum exists to score — run record §4). Full EC
  re-audit of that exact interior at 40 digits on [r₀, 10³ r₀]:
  **LEGAL** (all six combinations > 0; throat NEC1 = +0.003641,
  DEC_t = +0.001820; tail minima > 0 at their own scale).
- **Secondary branch (separate, unregistered exterior): JOINS ONLY
  AT FREED γ also holds** — with γ freed, (β, γ, k) fit (B, K, R̃)
  for all 81 interiors at both primary radii (162/162 converged);
  108 of them are EC-legal interiors whose shell passes
  (Ŝ₀⁰ ≥ 0). Every fitted γ is **negative**, |γ| ∈ [7.7×10⁻⁵,
  3.1×10⁻²] per r₀ — 23–26 orders of magnitude from the registered
  galactic γ = 10⁻²⁸ m⁻¹ and of the opposite sign. This branch is
  a different exterior claim and is never merged with the primary
  verdict.

**(V-b) UNDECIDED: Pais–Uhlenbeck spin-2 ghost vs Mannheim PT-symmetric quantisation — opposed literature positions, B3 NOT COMPUTABLE (Phase 32).**
Language lock: the conformal result is a **"scan signal under attack"** — nothing stronger.

## The Φ = 0 slice — closed form (analytic sub-item)

Derived symbolically in-item (γ = 0 form; registered-γ corrections
≤ 10⁻²⁶, far below every read), verified against the numeric sweep
at 15 (p, Σ) points to < 10⁻⁹ and against P38-3 at p = ½ exactly:

- R̃_int(r) = **(3 − p)·r^{p−1} − 2**; R(r) = 2p·r^{p−3} (r₀ = 1).
- At the Darmois match (β_MK = Σ^p/3, k = Σ^{p−2}/3 in r₀ units):
  R̃_ext(Σ) = **4·Σ^{p−1} − 2** — the exterior's coefficient is
  exactly **4 for every p**.
- **[R̃](r_Σ) = (1 + p)·(r_Σ/r₀)^{p−1} > 0** for all p ∈ (0, 1) and
  all finite r_Σ. At p = ½: (3/2)√(r₀/r_Σ) — P38-3's value.

So on the Φ = 0 slice the coefficient relation is exact and
structural: interior coefficient (3 − p) ∈ [2.1, 2.9] on the swept
box, exterior coefficient 4; equality would need p = −1, outside
the family. The gap function is (1 + p)(r₀/r_Σ)^{1−p}; it closes
only as r_Σ → ∞.

## The sweep at registered γ (primary + extension)

81 interiors × 3 radii = 243 Darmois-matched rows
(`p611_results.json`). [R̃] > 0 in 242; the single negative grid
value is Φ₂, a = +0.5, p = 0.1 at Σ = 10³ (−0.001700). Registered
refinement (bisection, bracket ≪ 0.01) located the Σ = 10³ Φ₂ zero
locus: a_zero(0.1) = 0.277734, a_zero(0.11) = 0.300861, …,
a_zero(0.17) = 0.487163; the locus leaves the registered a-box
above p ≈ 0.18 and leaves the legal region at p = 0.101196, where
it crosses the P38-1 throat-NEC1 boundary a*(p) = [11 − p −
√(p² − 14p + 97)]/4. The rest of the locus is EC-illegal: audited
at p = 0.173220, a = 0.5 (NEC1 fails at the throat itself,
−0.237722) and probed at p = 0.11, a = 0.300861 (throat NEC1 =
−0.027108 at 40 digits, matching the exact P38-1 throat formula
−0.027108195). **Coefficient-4 locus vs legal region, stated
exactly:** at the primary radii the [R̃] = 0 locus is *empty* in
the swept box (disjoint, gap named above on Φ = 0 and measured
minima +0.0611 / +0.00698 over all profiles); at the extension
radius the locus *intersects* the legal region in exactly the
segment p ∈ [0.1, 0.10120) of the Φ₂ family — and intersects the
illegal set for 0.10120 ≤ p ≲ 0.18 (deciding EC: throat NEC1).
Whether the locus continues legally below p = 0.1 is outside the
registered box (follow-up FU-P611-2).

## Adversarial protocol at the landed join (all required reads)

- **Second path:** 40-digit mpmath junction data (independent
  differentiation) at the audited point: [R̃] = 0.0, [R̃_,n] =
  −0.0152186 — agrees with the symbolic path to < 10⁻⁹. T-b
  controls reproduced to < 10⁻⁹ at both primary radii; the
  freed-γ T-b fit at 10 r₀ independently reproduces P38-3's
  robustness values (γ·r₀ = −0.030572, [R̃_,n] = −0.440238).
- **EC re-audit:** engine re-gated first (MK Bach-flat
  3.4×10⁻¹⁹ ≤ 10⁻¹², matching P38-1's stored gate); the audited
  interior is legal at 40 digits on the full domain (above).
- **Shell read:** Ŝ₀⁰/α₀ = +0.020291 ≥ 0 — LEGAL SHELL. [R] at the
  join: −2.12×10⁻⁸ r₀⁻² (reported, not a registered condition).
  Joined exterior: β_MK = 2.142611 r₀, γ = 10⁻²⁸ m⁻¹ per r₀
  (registered), k = −2.28996×10⁻⁹ r₀⁻².
- **Ledger reads (Phase-23 bars), joined configuration:**
  tidal at the throat is decided by the *static radial* term
  |R_t̂l̂t̂l̂| = Φ₂′(r₀)(1 − p)/2 = a(1 − p)/2 = 0.124980 r₀⁻²
  (Φ′(r₀) ≠ 0 here, unlike the Φ = 0 rows; orthonormal Riemann
  check converges to 0.124979 / −0.450000 for R_tltl / R_lθlθ).
  At v = 0.1 c, r₀ = 1 m: gradient **1.12×10¹⁶ s⁻² =
  2.29×10¹⁵ × the 1 g bar**; **tidal-bar radius
  r₀\* = 4.785×10⁷ m**. (The transverse boost term is only
  0.004545 c²/r₀² at 0.1 c but diverges as γ² as v → c, as in
  every ledger family.) **Crossing** (stations at proper distance
  ±10 r₀; station areal radius 8.498 r₀): at c, 5.81×10⁻⁸ s at
  r₀ = 1 m and 2.78 s at r₀\*; traveller proper at 0.1 c
  6.64×10⁻⁷ s / 31.8 s; external (P38 convention, redshift-weighted)
  5.81×10⁻⁷ s / 27.8 s — passes the 1-day bar by ~11 orders at
  1 m, ~3.4 orders at r₀\*. **Mass:** no ADM mass exists in MK
  asymptotics; the joined (β_MK, γ, k) above are the mass-read
  replacement.

## Drafted replacement ledger window-column text (verbatim-ready)

> **Junction: JOINS WITH LEGAL SHELL at the extension radius
> only.** No MK exterior joins at r_Σ = 10 r₀ or 10² r₀ for any
> member of the P38-1 legal region (deciding datum [R̃] > 0
> everywhere; Φ = 0 slice exact: [R̃] = (1 + p)(r₀/r_Σ)^{1−p}).
> At r_Σ = 10³ r₀, the Φ₂ member (p = 0.1, a = 0.277734; legal
> locus segment p ∈ [0.1, 0.10120)) joins the registered-γ MK
> exterior (β_MK = 2.143 r₀, γ = 10⁻²⁸ m⁻¹, k = −2.29×10⁻⁹ r₀⁻²)
> with [R̃] = 0 and a shell Ŝ₀⁰ = +0.0203 α₀ ≥ 0 (BDE
> arXiv:1710.10438 §III.B; the formalism fixes Ŝ₀⁰ only).
> Interior EC-legal at 40 digits on [r₀, 10³ r₀]. With γ freed,
> joins exist at both primary radii but only at γ < 0, 23–26
> orders from the galactic fit — a different exterior claim.
> **Tidal:** static-radial-decided gradient at r₀ = 1 m
> (v = 0.1 c) 1.12×10¹⁶ s⁻² = 2.29×10¹⁵ × the 1 g bar;
> tidal-bar radius r₀\* = 4.79×10⁷ m; v→c transverse diverges
> as γ². **Crossing** (stations ±10 r₀ proper): at c
> 5.81×10⁻⁸ s (1 m) / 2.78 s (r₀\*); traveller proper at
> 0.1 c 6.64×10⁻⁷ s / 31.8 s — passes the 1-day bar.
> **Mass:** no GR-style ADM mass in MK asymptotics; joined
> (β_MK, γ, k) reported instead.

## Non-MK branch — closed as registered

MK-exhaustion in the scored gauge, sourced (run record §5):
Berezin–Dokuchaev–Eroshenko (JCAP 02 (2016) 019) find the
*complete* pure-vacuum set = a constant-R̃ class (Robertson–Walker
/ "gravitational bubbles") plus a varying-R̃ class conformally
covered by the three-parameter MK solution; Dzhunushaliev–Schmidt
(arXiv:gr-qc/9908049) report every spherically symmetric Bach
solution is almost everywhere conformally an Einstein space. In
the scored gauge Ω = 1 (conformal rescalings are not new rows),
the varying class IS MK; the constant class's static spherical
Einstein members (Schwarzschild–(A)dS) are already MK's γ = 0
sub-family. No distinct published static spherical Bach-flat
family exists to audit. Named absences: non-static / non-spherical
exteriors (out of registered scope); a double-layer matter
interpretation (excluded per BDE/Senovilla — no conventional EMT
counterpart).

## Failure Protocol — anatomy and follow-ups

- **Anatomy of the primary-radius non-join:** the Darmois-matched
  MK exterior's R̃ coefficient is pinned at 4 (exact on Φ = 0;
  measured across all profiles), while legal interiors carry
  smaller effective coefficients at finite Σ; the jump decays
  like a power of r₀/r_Σ but reaches zero at a *registered* radius
  only at Σ = 10³ r₀, and there only for the slow-tail Φ₂ profile
  at small p — because Φ₂'s redshift keeps modifying R̃_int out
  to large r (the same 1/ln r tail that made Φ₂'s P38-1 boundary
  profile-sensitive). The legal segment is a sliver
  (Δp ≈ 0.0012 inside the box) because a_zero(p) rises steeply
  while the throat-NEC1 boundary a*(p) is nearly flat.
- **FU-P611-1:** extend the junction audit to Σ ∈ (10², 10³) r₀
  as a *primary* scan under new registration — the gap function
  suggests locus crossings for other (profile, p) pairs may enter
  the legal region at intermediate radii; this item's data neither
  confirm nor exclude them.
- **FU-P611-2:** the p < 0.1 continuation of the Φ₂ locus
  (outside the registered box): does the legal segment widen
  below the box edge?
- **Instrument failures (anatomy + follow-up, both resolved
  in-item):** (i) the first γ-freed solver never moved (ier = 5)
  — unscaled unknowns (γ ~ 10⁻²⁸ beside β ~ 1); fixed by scaled
  unknowns (β, γΣ, kΣ²), then by least-squares multi-start
  (162/162 converged, fit residuals ≤ 10⁻¹²-class). No freed-γ
  number from the failed versions is used. (ii) the first
  finite-difference second path gave a corrupt [R̃_,n] (−82 vs
  −0.719) — nested float64 FD amplifies noise through two
  differentiations; replaced by the 40-digit mpmath path, which
  reproduces every symbolic jump to < 10⁻⁹. No number from the
  failed FD path is used.

## C12 accounting

Computed: 243 primary+extension Darmois-matched junction rows
(float64, symbolic-formula instrument, gated); the Φ = 0 slice in
exact closed form; registered bisection refinement of both
sign-change brackets; the full Σ = 10³ Φ₂ locus a_zero(p) at 11
p-values plus its legal-segment endpoint; 40-digit EC re-audits
(float grid + mpmath probes at argmins, throat, tail) of both
audited locus points and 40-digit throat probes at a third;
162 γ-freed fits (multi-start least squares, residuals audited);
40-digit mpmath second-path junction data at 6 deciding rows;
ledger reads for the one joined configuration with an orthonormal
Riemann convergence check. Claimed: exactly the verdict scoped
above — a legal-shell join at the extension radius on the named
locus segment (one audited point in full, the segment bounded by
the exact throat-NEC1 boundary and two full audits), non-join at
both primary radii over the swept box, the freed-γ branch as a
separate unregistered-exterior result, and MK-exhaustion from
cited literature (not independently re-derived). Derivation
classes: junction data and EC audits are direct computations on
the registered families (Class A pattern); the α₀ = α_g/2 mapping
is an exact algebraic identification of two published
normalisations; the non-MK closure is a literature result carried
with its sources. (V-b) is not computed by anything here and is
attached unchanged.

Files: results/p611_runrecord.md, p611_memo.md, p611_results.json,
p611_checker.json, p611_junction_raw.json, p611_follow_raw.json,
p611_freed_raw.json, p611_freed3.json, p611_ecaudit.json,
p611_locus_ledger.json, p611_extra.json, p611_signcheck.json;
scripts in work/. Internal only; nothing uploaded.
