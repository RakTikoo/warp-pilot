# W-A REPORT — GATE-9, claim G9-1 (LEGALITY of the conformal joining member)

Worker W-A, Gate 9. Run with `~/workspace/warp-pilot/venv/bin/python`
(float64 grid; mpmath/SymPy probes at 50-digit working precision,
reported to 40 digits). Fresh code in `gate9/`: `wa_engine.py`
(engine), `wa_anchors.py`, `wa_tb.py` + `wa_tb_last.py`, `wa_phi0.py`,
`wa_member.py` (grid stage), `wa_probes.py` (probe stage),
`wa_checker.py` (pass/fail recomputed from the result files).
Numbers: `results/wa_g91_numbers.json` (+ `wa_member_grid.json`,
`wa_member_probes.json`, `wa_tb.json`, `wa_phi0.json`).
Search log: `results/wa_search_log.md`.
Nothing outside `gate9/` was edited; nothing was uploaded.

## Verdicts

- **Correctness: REPRODUCED.** Both registered bars pass on a fully
  independent second path (fresh symbolic Bach derivation built from
  the metric for this gate; no phase script imported or re-run).
- **Novelty: PARTIALLY KNOWN** (known part cited exactly below).
- **Gate verdict proposed: UPLOAD-READY AFTER RESTATEMENT** — the
  correctness bars pass as registered, but the Uniqueness Protocol
  forbids outright novelty wording; the exact restated wording is at
  the end of this report.

## The fresh engine and the convention identification

`wa_engine.py` derives the Bach tensor from the metric
ds² = −e^{2Φ(r)}dt² + (1 − b(r)/r)⁻¹dr² + r²dΩ² from first principles
(Christoffel → Riemann → Ricci → Weyl → double covariant divergence),
sparsely, computing ∇C for **all** index patterns (an early version
that formed ∇C only where C ≠ 0 failed the Schwarzschild anchor —
∇C is nonzero on zero Weyl components through connection mixing;
that machinery bug was found by the anchor, fixed, and the anchor
then passed exactly).

The raw bracket ∇^a∇^b C_{manb} + ½R^{ab}C_{manb} reproduced the
Phase-32 T-b closed forms with ratio **exactly 0.5** at every point
and component: the registered Bach tensor is
B = 2∇∇C + R·C (Mannheim's B; Varieschi–Ault's W, their eq. (4)).
The factor 2 was identified by the anchor, applied in the engine,
and the anchor then passed exactly. Bach-flatness anchors are
insensitive to the overall factor; the T-b anchor fixes it.

## Anchors (all run BEFORE any claim number)

- **(i) Bach-flatness.** Schwarzschild (b = 2, Φ = ½ln(1−2/r)):
  B^t_t = B^r_r = B^θ_θ = **0 symbolically** (full simplify).
  MK ansatz at Phase 32's registered point (β = 1/2, γ = 1/100,
  k = 1/1000): max |B| over r ∈ {3, 10, 30} = **1.3×10⁻¹⁶⁹** ≤ 10⁻¹²
  (the unsimplified rational expressions evaluate to ~0 at 30-digit
  precision). **PASS.**
- **(ii) T-b closed forms** (p323_memo: B^t_t = −5(3u−1)/(24r⁵),
  B^r_r = −5(4u−1)/(48r⁵), B^θ_θ = 5(10u−3)/(96r⁵), u = √r):
  B^t_t symbolic point differences **exactly 0** at r = 3/2, 2, 5, 10;
  all three components' 50-digit point differences **exactly 0.0**
  at all four points. **PASS.**
- **(iii) Φ = 0 slice** (b = r^p, p ∈ {1/10, 3/10, 1/2, 7/10, 9/10},
  r ∈ {1.5, 2, 5, 10, 100}):
  - NEC1 factorisation **reproduced**: NEC1 equals the Phase-38
    closed form (p−3)(p−1)(1 − 3p + 2p·r^{1−p})/(6r^{6−2p}) — i.e.
    NEC1 ∝ (1 − 3p + 2pq), q = r^{1−p} — with max relative error
    1.8×10⁻¹³ (float64 lambdify noise floor). **PASS.**
  - DEC_r = NEC1: **exact** (difference 0.0 at all 25 points;
    p_r < 0 on the whole slice, so ρ − |p_r| = ρ + p_r). **PASS.**
  - SEC = 2ρ: holds to ≤ 3.9×10⁻¹⁶ (trace identically zero). **PASS.**
  - **DEC_t = NEC2: FALSE as stated** — in the gate text and in
    p381_memo. Measured: DEC_t − NEC2 = −2p_t ≠ 0 at all 25 points
    (p_t > 0 on the slice). It also contradicts Phase 32's own T-b
    closed forms (DEC_t = 5(2u−1)/(24r⁵) vs NEC2 = 5(22u−7)/(24r⁵)
    at p = 1/2). The correct slice identity is DEC_t = ρ − |p_t|
    (= ρ − p_t on the slice). This is a **prose error in the
    registered anchor text, not a machinery failure** — the machinery
    is proven exact by anchors (i), (ii) and the factorisation — and
    the identity is not used anywhere in the G9-1 bars (which score
    the six combinations directly). Flagged here for the coordinator;
    it does not touch the claim's numbers, whose stored DEC_t is the
    ρ − |p_t| value throughout.

## Deciding numbers (my run)

Member: b = r^{0.1}, Φ₂ = a·ln r/(1 + ln r),
a = 0.27773424114865775 (the audited point of the claim's record;
the claim statement rounds to a = 0.277734 — the difference moves
the throat values by 9×10⁻⁵ relative, see below).
B-combinations: ρ = −B^t_t, p_r = B^r_r, p_t = B^θ_θ;
DEC_i = ρ − |p_i| (the phase convention that reproduces every stored
DEC value; the gate-bar forms ρ − p_i were also evaluated and are
also positive everywhere — on this member p_r < 0 and p_t > 0 on the
whole grid, so DEC_t is identical in both conventions and
DEC_r(gate form) ≥ DEC_r).

**Float64 grid** (2500 log-spaced points on [1, 1000]; minima):

| combination | my minimum | at r | stored (p611_ecaudit) |
|---|---|---|---|
| ρ | 6.275140592394116×10⁻¹⁵ | 1000 | 6.275140592×10⁻¹⁵ |
| NEC1 | 1.2298520389625545×10⁻¹⁵ | 1000 | 1.229852039×10⁻¹⁵ |
| NEC2 | 1.1935355165306837×10⁻¹⁴ | 1000 | 1.193535517×10⁻¹⁴ |
| DEC_r | 1.2298520389625545×10⁻¹⁵ | 1000 | 1.229852039×10⁻¹⁵ |
| DEC_t | 6.149260194813948×10⁻¹⁶ | 1000 | 6.149260195×10⁻¹⁶ |
| SEC | 1.2550281184787997×10⁻¹⁴ | 1000 | 1.255028118×10⁻¹⁴ |

All six > 0 at every grid point. Exactly one NaN per combination,
at the single point r = r₀, where the raw unsimplified expression is
0/0 (1 − b/r = 0); the throat is decided by the probes below.
Trace check on grid: |−ρ + p_r + 2p_t| ≤ 9.1×10⁻¹³ near the throat,
~10⁻²⁵ at the tail (float64 noise on O(0.3) quantities).

**50-digit probes:**
- Tail (r = 1000, the stored tail-minimum radius): NEC1 =
  1.22985203896229205×10⁻¹⁵, DEC_t = 6.14926019481146027×10⁻¹⁶,
  ρ = 6.275140592×10⁻¹⁵-class — all > 0, matching stored to ~9
  digits.
- Throat probe at the phase record's own point r = 1 + 10⁻⁹:
  NEC1 = 0.00364087235488633 (stored probe 0.0036408724),
  DEC_t = 0.00182043617744317 (stored probe 0.0018204362).
- Throat limit (quadratic extrapolation in δ from δ = 10⁻⁶, 10⁻⁸,
  10⁻¹⁰): **NEC1 = 0.00364086750048373**, **DEC_t =
  0.00182043375024187**, ρ = 0.30176162255120. The extrapolated NEC1
  agrees to all printed digits with the Phase-38 throat formula
  (p−1)²(2a² + (p−11)a + (3−p))/6 evaluated at the full-precision a —
  an independent arithmetic cross-check of the limit.

**Bars (checker-recomputed, `wa_checker.py`):**
- (a) all six combinations > 0 at every grid point and probe: **PASS**.
- (b) throat NEC1 vs stored +0.00364119103852: relative difference
  **8.9×10⁻⁵** (0.0089%); DEC_t vs stored +0.00182059551926: **8.9×10⁻⁵**.
  Both ≪ the 2% bar: **PASS**. (The residual is an a-rounding
  sensitivity inside the phase record: at the rounded a = 0.277734
  the throat formula gives 0.00364118618412, between my full-a value
  and the stored digits; immaterial against the bar, noted for the
  record.)

**Correctness verdict: REPRODUCED.**

## Novelty

**Verdict: PARTIALLY KNOWN.** Full log: `results/wa_search_log.md`
(11 queries verbatim, sources checked, dated 2026-11-22).

Known part, cited exactly: that wormhole matter in conformal (Weyl)
gravity can satisfy the energy conditions **at/near the throat** is
published —
- F. S. N. Lobo, arXiv:0801.4401, Class. Quantum Grav. 25 (2008)
  175006, DOI 10.1088/0264-9381/25/17/175006: a class "satisfies all
  of the energy conditions, **in the vicinity of the throat**".
- G. U. Varieschi & K. L. Ault, arXiv:1510.05054 (read in full):
  ECs not violated "at or near the wormhole throat" for two-power
  (b₀/r) shape/redshift families; displayed solutions are legal only
  for 1 ≤ r ≲ 1.03 (Φ = 0) and 1 ≤ r ≲ 1.10 (Φ ≠ 0), with exotic
  matter needed at their attempted junctions beyond, and ANEC
  violated for their Φ = 0 class.
Further neighbours (different constructions, no whole-domain matter
legality): Hohmann et al., arXiv:1802.02184, DOI
10.1088/1475-7516/2018/10/003 (vacuum wormholes); Dotti, Oliva &
Troncoso, arXiv:0907.1128, DOI 10.1142/S0217751X09044930 (vacuum);
Cadoni et al., arXiv:2503.14214, DOI 10.1088/1475-7516/2025/06/016
(Weyl-rescaling, scalar-tensor); Heydari-Fard et al.,
arXiv:2312.07588 (time-dependent, exotic matter required);
Godani & Samanta, arXiv:1809.00341 (same power-law shape in f(R),
ECs violated — different theory).

Not found in our search: strict legality of **all** EC combinations
for T = 4α_g·B (α_g > 0) over a whole domain extending to 10³ r₀;
the Φ = 0 power-law family b = r₀(r/r₀)^p, p ∈ (0,1), legal on the
whole domain or its NEC1 ∝ (1 − 3p + 2pq) factorisation; the Φ₂
profile a·ln(r/r₀)/(1 + ln(r/r₀)) used for any conformal-gravity
wormhole; any 40-digit Bach-tensor throat-legality audit.

**Coverage gaps (plainly):** arXiv was checked natively (full texts
surfaced and two read). **INSPIRE-HEP and Semantic Scholar were
checked only via the general web index, not via their native
interfaces** — dedicated queries naming them were run and returned
the same records through the index; a source reachable only via
indexes is a gap, not a negative. General web was checked.

## Exact restated wording (proposed upload wording)

> In conformal (Weyl) gravity, in the scored gauge Ω = 1 with the
> Bach normalisation 4α_g·B_μν = T_μν, α_g > 0, the static spherical
> throat b(r) = r₀(r/r₀)^0.1 with redshift profile
> Φ₂ = a·ln(r/r₀)/(1 + ln(r/r₀)), a = 0.277734, is EC-legal on the
> whole interior domain [r₀, 10³ r₀] (r₀ = 1): all six
> B-combinations (ρ, ρ + p_r, ρ + p_t, ρ − |p_r|, ρ − |p_t|,
> ρ + p_r + 2p_t) are strictly positive on the full domain —
> throat NEC1 = +0.003641 and DEC_t = +0.001821 in B-combination
> form, tail minima > 0 at 40 digits — independently reproduced in
> Gate 9 (W-A) by a fresh symbolic Bach-tensor derivation. That
> conformal-gravity wormhole matter can satisfy the energy
> conditions near a throat is PARTIALLY KNOWN (Lobo,
> arXiv:0801.4401; Varieschi & Ault, arXiv:1510.05054 — throat
> vicinity only, r ≲ 1.1 r₀); whole-domain legality to 10³ r₀ for
> this family and member was not found in our search (limits:
> arXiv checked natively; INSPIRE-HEP and Semantic Scholar checked
> only via the general web index, not their native interfaces;
> general web checked; full log in Gate 9 W-A search log). This is
> a throat OBJECT claim: no transport is claimed and no
> traversability is claimed (the word "traversable" appears only
> in negations of this kind). The member's tidal-bar radius is
> r₀* = 4.785×10⁷ m, and its formation standing is PRE-EXISTING
> ONLY. (V-b) UNDECIDED: Pais–Uhlenbeck spin-2 ghost vs Mannheim PT-symmetric quantisation — opposed literature positions, B3 NOT COMPUTABLE (Phase 32).

## Notes for the coordinator

1. Anchor (iii)'s "DEC_t = NEC2" identity (GATE9.md and p381_memo)
   is false as stated; correct form DEC_t = ρ − |p_t|. No claim
   number depends on it. Recommend a gate-record erratum line.
2. Stored throat digits (NEC1 = +0.00364119103852) carry a ~9×10⁻⁵
   relative sensitivity to the rounding of a (0.277734 vs
   0.27773424114865775); my full-a limit is 0.00364086750048,
   matching the Phase-38 throat formula at full a to all digits.
   Inside the 2% bar by a factor ~225; no restatement needed.
3. `wa_member.py` stage 2 (SymPy `N()` probes) was superseded by
   `wa_probes.py` (mpmath-lambdified probes) after the raw-expression
   `N()` path proved too slow; the grid stage of `wa_member.py` is
   the one whose output the checker consumed.
