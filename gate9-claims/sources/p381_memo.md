# P38-1 MEMO — Shape/Φ sweep around the conformal T-b throat (FU-P323-1)

Worker P38-1, Phase 38. Run record (forms, gate tolerances, sign
checks, all fixed before scan numbers): `p381_runrecord.md`.
Bars: `../CHECKPOINT38.md` §P38-1. Parent signal: Phase 32 §P32-3.

## VERDICT: REGION

**The legal throat is a REGION, not an island.** Legality holds on
an open set around (p = 1/2, Φ = 0) — measured extent below — and
on the entire Φ = 0 shape interval p ∈ (0, 1) in exact closed form.
54 of 90 registered rows are legal (checker `p381_checker.json`
over `p381_sweep_raw.json`).

**(V-b) attached, unchanged: the HEALTH/QUANTUM clause stands
UNDECIDED (Pais–Uhlenbeck ghost vs Mannheim PT-symmetric
quantisation — opposed literature positions; Phase 32 B3 = NOT
COMPUTABLE). This verdict is classical only; the ghost clause is
not imported into it, and it does not retroactively change it.**
Strongest language: **"scan signal under attack"** — nothing
stronger.

## Instrument (re-gated before any sweep number)

- Phase-32 engine (`phase32/work/bach_engine.py`) RE-GATED:
  Schwarzschild member B^μ_ν ≡ 0 symbolically exact; MK at
  (β,γ,k) = (0.5, 0.01, 0.001): max |B^μ_ν| = 3.4e-19 at r = 3,
  ≤ 1.8e-20 at r = 10, 30 — **PASS** vs the registered 1e-12
  tolerance, matching Phase 32's stored values (`p381_gate.json`).
- Sweep instrument: generic-b(r), Φ(r) Bach components derived
  once symbolically from the same published Ricci form
  (arXiv:2505.17171 eq. (6)); trace ≡ 0 *symbolically exactly*.
  Gated against Phase 32's exact closed forms: T-b and Ellis
  B^t_t, B^r_r, B^θ_θ reproduced **exactly** (`p381_validation.json`).
- Conservation: the combination p_r′ + (2/r)(p_r − p_t) +
  Φ′(ρ + p_r) vanishes at 40-digit probes (|C| ≲ 1e-42) on the
  Φ = 0 family, the Ellis control, and Φ ≠ 0 rows
  (`p381_sweep_raw.json: conservation_probes`).
- Sign checks: all passed before registration closed
  (`p381_signchecks.txt`).

## The Φ = 0 slice is legal for EVERY p ∈ (0, 1) — exact proof

With q ≡ r^{1−p} ≥ 1 on [1, 1000], the symbolic-p closed forms
(`p381_phi0_symbolic_p.json`) factorise as (all over r^{6−2p} > 0):

- ρ = (p−3)[(−6p²+11p−3) + (4p²−8p) q] / (12 r^{6−2p}); the
  bracket is linear in q, negative at q = 1 (−2p²+3p−3, disc. < 0)
  and decreasing (slope 4p(p−2) < 0), and (p−3) < 0
  ⇒ ρ > 0 ∀p ∈ (0,1), ∀r.
- NEC1 = (p−3)(p−1)(1 − 3p + 2p q) / (6 r^{6−2p}) > 0, since
  1 − 3p + 2pq ≥ 1 − p > 0.
- B^r_r < 0 and B^θ_θ > 0 on the whole domain ∀p ∈ (0,1)
  (bracket signs as in the run analysis), hence DEC_r = NEC1 and
  DEC_t = NEC2 exactly on this slice.
- NEC2's bracket is likewise linear in q, negative at q = 1
  (−3p²+4p−5, disc. < 0) and decreasing ⇒ NEC2 > 0.
- SEC = 2ρ identically (tracelessness), > 0.

So along Φ = 0 there is **no p-boundary inside (0, 1)**; the
Phase-32 positivity certificate at p = 1/2 is one point of a
family-wide certificate. (p → 0, p → 1 read from the trend, per
registration: all margins shrink like (1−p) or p factors but no
sign flips occur inside the open interval.)

## Sweep map (power shapes; L = legal, ✗ = first failing EC)

| p | Φ=0 | Φ₁ a=−0.5 | Φ₁ a=−0.1 | Φ₁ a=+0.1 | Φ₁ a=+0.5 | Φ₂ a=−0.5 | Φ₂ a=−0.1 | Φ₂ a=+0.1 | Φ₂ a=+0.5 |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.1 | L | ✗ DEC_r @1.443 | L | L | ✗ NEC1 @throat | ✗ DEC_r @5.368 | ✗ DEC_r @53.30 | L | ✗ NEC1 @throat |
| 0.2 | L | ✗ DEC_r @1.777 | L | L | ✗ NEC1 @throat | ✗ DEC_r @16.56 | ✗ DEC_r @331.1 | L | ✗ NEC1 @throat |
| 0.3 | L | ✗ NEC1 @2.368 | L | L | ✗ NEC1 @throat | ✗ DEC_r @67.63 | L | L | ✗ NEC1 @throat |
| 0.4 | L | L | L | L | ✗ NEC1 @throat | ✗ DEC_r @440.0 | L | L | ✗ NEC1 @throat |
| 0.5 | L | L | L | L | ✗ NEC1 @throat | L | L | L | ✗ NEC1 @throat |
| 0.6 | L | L | L | L | ✗ NEC1 @throat | L | L | L | ✗ NEC1 @throat |
| 0.7 | L | L | L | L | ✗ NEC1 @throat | L | L | L | ✗ NEC1 @throat |
| 0.8 | L | L | L | L | ✗ NEC1 @throat | L | L | L | ✗ NEC1 @throat |
| 0.9 | L | L | L | L | ✗ NEC1 @throat | L | L | L | ✗ NEC1 @throat |

(Authoritative source: `p381_results.json` / `p381_checker.json`.
Crossings are the first-failure radii from 40-digit bisection.)

**Open neighbourhood of (1/2, 0), measured:** every row with
p ∈ [0.4, 0.9] and a ∈ [−0.5, +0.1] (both profiles) is legal, as
is a = +0.1 at every sampled p and a ∈ {−0.1, 0} at every sampled
p (Φ₂ a = −0.1 excepted at p = 0.1, 0.2 — tail DEC_r, below).
(1/2, 0) is strictly interior to the legal set in both the p and
a directions. That is the REGION verdict's measured core.

## Boundaries and deciding terms

- **Positive-a boundary (all p, both profiles): the throat NEC1
  numerator.** Exact throat limits:
  NEC1(r₀) = (p−1)²(2a² + (p−8)a + (3−p))/6 (Φ₁);
  NEC1(r₀) = (p−1)²(2a² + (p−11)a + (3−p))/6 (Φ₂).
  The legal-side root: a*_Φ₁(p) = [8−p − √(p²−8p+40)]/4
  (≈ 0.370 at p = 1/2); a*_Φ₂(p) = [11−p − √(p²−14p+97)]/4
  (**= 1/4 exactly at p = 1/2**). At a = +0.5 every power row
  fails NEC1 *at the throat itself* (registered grid's first
  point; 40-digit throat probes agree). Deciding term: the
  2a² + (p−8)a (resp. (p−11)a) quadratic in the throat NEC1
  numerator — the Φ′(r₀) = a terms of the □R sector.
- **Negative-a boundary (small p): mid-domain / tail DEC_r.**
  Φ₁ a = −0.5 fails at p = 0.1 (DEC_r zero at r = 1.443; SEC
  goes deepest, −1.9e-2 at r ≈ 1.78), p = 0.2 (DEC_r @ 1.777),
  p = 0.3 (NEC1 @ 2.368); legal from p = 0.4 up. Φ₂ a = −0.5
  fails by tail DEC_r at p = 0.1–0.4 (crossings 5.37, 16.6,
  67.6, 440 — retreating outward as p grows) and is legal from
  p = 0.5 up. Deciding term: the DEC_r combination
  ρ − |p_r| (with p_r > 0 in the failing zone, so DEC_r =
  ρ − p_r there) — its numerator's zero crossing is the
  boundary; the crossing radius diverges as p → 0.5⁻, which is
  the boundary's mechanism.
- **Φ₂ a = −0.1 tail sliver (p = 0.1, 0.2):** DEC_r crosses zero
  at r = 53.3 (p = 0.1) and r = 331 (p = 0.2). These are NOT
  roundoff: at 40 digits the minima are −5.5e-11 and −1.9e-14,
  and at the p = 0.2 argmin DEC_r = −7.6 × ρ_local — an
  order-unity relative violation at the tail's own scale.
  Φ₁ at the same (p, a) is legal: the boundary is
  profile-sensitive in the tail because Φ₂ approaches its
  asymptote like 1/ln r, far slower than Φ₁'s 1/r.
- **p direction:** no boundary inside (0, 1) at Φ = 0 (exact,
  above) or at a = ±0.1 for Φ₁; the only p-side failures are
  the Φ₂ negative-a tail sliver at small p.

## Ellis-like family (b = r₀²/r, Φ ≠ 0): NO legal row

All 8 rows fail. First failure is DEC_r in every row but one,
with zero crossings at r = 1.089–1.317 (a = −0.5, −0.1, +0.1)
and r = 2.428 (Φ₁ a = +0.5); Φ₂ a = +0.5 fails ρ at the throat
itself. The Φ = 0 control reproduces the Phase-32 KILL (first
DEC_r crossing at r = √1.5 ≈ 1.2247, ρ tail zero at √(5/3)).
**Anatomy:** the Ellis shape's B^t_t numerator zero at
r = √(5/3) r₀ (Phase 32) sits inside the domain for Φ = 0, and
no registered Φ profile removes the near-throat DEC_r/SEC
deficit — Φ moves the crossing by ≲ 0.3 in r but never out of
the domain, because at the throat the Ellis DEC_r is already
marginal (p_r(r₀) structure) and the Φ terms enter at the same
order. **Follow-up FU-P381-1:** a Φ profile with Φ′(r₀) tuned
per-shape (not the registered two families) could be tested
under a new registration; within the registered families the
Ellis branch is closed. Reopening condition: a published or
pre-registered Φ family whose throat derivatives differ in
kind (e.g. Φ′(r₀) = 0 with Φ″(r₀) ≠ 0), not a re-tune of a.

## Failure Protocol items

- **Sweep v1 (instrument failure, not physics):** full-grid
  40-digit mpmath ran ~1.5 min/row (> 2 h projected). Anatomy:
  expression evaluation cost × 2009 grid points × 90 rows.
  Follow-up (run): v2 = float64 grid (Phase-32's own standard)
  + 40-digit probes at every deciding point (argmins, crossings
  by 90-step bisection, throat, tail) + symbolic throat limits
  and the symbolic-p exact proof. No bar was lowered: every
  legal row's minima, throat and tail values were re-confirmed
  at 40 digits (checker + probe audit: no legal row fails any
  40-digit probe), and every marginal failure was confirmed at
  40 digits with relative scale stated.
- **a = +0.5 throat failures:** anatomy = the throat NEC1
  quadratic above; follow-up (done): exact a*(p) boundary
  curves for both profiles, quoted above.
- **Φ₂ tail sliver:** anatomy = slow (1/ln r) approach of Φ₂
  to its asymptote keeping a DEC_r deficit alive to large r at
  small p; follow-up (done): 40-digit relative-scale check
  (DEC_r = −7.6 ρ_local). Open refinement: the exact
  (p, a) curve of the tail boundary for Φ₂ at a ∈ (−0.5, 0) —
  registered as FU-P381-2 for any future pass; it does not
  affect the REGION verdict, whose core box is unaffected.

## Files

results/p381_runrecord.md (pre-registered), p381_gate.json,
p381_validation.json, p381_phi0_symbolic_p.json,
p381_sweep_raw.json (90 rows + probes + conservation),
p381_checker.json, p381_results.json, p381_signchecks.txt;
scripts in work/ (derive_generic.py, validate_generic.py,
sweep.py, checker.py, regate.py, sign_checks.py;
generic expressions in work/generic_bach.json).
Internal only; nothing uploaded.
