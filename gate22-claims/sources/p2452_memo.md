# P245-2 (Item 2, C2) — THE COMBINED-CLASS SOS THROAT: memo

Worker W245-2, 2026-11-24. Registration (written BEFORE any deciding
computation): `phase245/work/p2452_registration.md`. Driver:
`phase245/work/p2452_run.py`; checker: `phase245/work/p2452_check.py`
(**ALL PASS, 24/24**); numbers: `phase245/results/p2452_results.json`.
This item RUNS the packaged spec P230-2/FU of
`phase230/results/p2302_memo.md`: the P129-6 combined class
(ω₀ ≢ 0, general R(ρ,θ,t), t-jets on) on the A-branch base pattern
with the Phase 167/169 compensator, R_,tt(θ*) < 0 through the lock,
seven clauses + SOS control on the total stress at jet scope,
sustained over t ∈ [0, 0.5] under the true lock (P169-1 engine),
judged at the WORST instant. Total stress = G/8π (GR; no
gravity-sector term exists to exclude) — the NO-EXOTIC
total-stress standard is the read itself. Datum ≠ construction.
INTERNAL only; no ledger append, no launches, nobody contacted.

## Verdict (registered form, verbatim)

**THE BREAK IS REAL AT DATUM LEVEL**

— on the headline datum (ω_a = 0.2, W₁ = 0) the pin clause NEC_ρ
passes at every sampled instant of [0, 0.5] including the worst,
carried by the R_,tt t-term at θ*(t); sustainment — of the
NEC_φ/DEC_φ drift clause, which fails at the worst instant in
every arm (face facts §4) — becomes the named successor. The
fences in §4 are part of the verdict, not footnotes to it.

## 1. The datum

P167 compensated pose on the fixed (true-lock) P162-1 engine:
Φ₀ = −0.2 + 0.3 sin²θ; R = 0.8 + 0.1ρ² + (t²/2)Att(θ),
Att = −0.9129985617247269 sin⁴θ (R_,tt(θ*) = −0.9130 < 0, the
P129-6 Exhibit-A sign); μ₀ lock-marched under the true lock
(gauge u(0,t) = 0, h_t = 0.0025, fine grid 2881); compensator
J_pose = j_prof + e^{−2Φ₀}μ_,tt, Fuu = e^{2μ₀}J_pose. Rotation
added exactly as in P230-2: ω₀ = ω_a sin²θ (time-independent),
W₁ posed, Wuu solved pointwise per instant from mom_φ = 0
(residual ≤ 9.3×10⁻¹⁶ in every arm). 21 sampled instants,
t = 0, 0.025, …, 0.5; 181-point audit grid; momentum maxima
≤ 9.3×10⁻¹⁶ at every instant of every arm (true lock clean with
rotation on). Arms: headline ω_a = 0.2, W₁ = 0; ω_a ∈ {0.1, 0.4},
W₁ = 0; ω_a = 0.2, W₁ = 0.3 sin²θ (priced); ω_a = 0 (baseline).

## 2. Controls (run first; all PASS)

- **CA — time-independent limit reproduces P230 X2's pin.**
  Static rotating pose (areal R, μ₀ ≡ 0, t-jets zero, ω_a = 0.2,
  W₁ = 0): NEC_ρ min = **−4.0625** at θ* = π/2; channel S vs the
  analytic identity ≤ 8.9×10⁻¹⁶ on the grid; mom_φ solve residual
  1.8×10⁻¹⁶.
- **CB — non-rotating limit reproduces Phase 77's pin.** Same
  pose, ω_a = 0: S(θ*) = **−4.0625** exactly (angular −0.9375,
  flare −3.125), grid deviation ≤ 8.9×10⁻¹⁶.
- **C2 — SOS verified on the fields** (P230-2's method): 25
  configurations × 4000 null directions per sector, direct
  contraction: scalar min T(k,k) = +2.8×10⁻⁹, Maxwell min
  T(k,k) = +2.1×10⁻⁶ (both ≥ 0), closed forms reproduced to
  ≤ 8.5×10⁻¹⁶ relative. SOS-only matter satisfies NEC along
  every null direction identically — the geometry's positive
  NEC_ρ below is therefore a statement about the combined-class
  geometry's required stress being SOS-admissible in sign, at
  jet scope, exactly as the spec poses it.
- **C3 — machinery consistency.** The ω_a = 0 arm reproduces
  P169-1 exactly: t = 0 clause minima = the P159-3b compensated
  datum set to 1.3×10⁻¹⁵; NEC_φ first failing instant 0.400;
  NEC_φ worst −0.6297872673028908 at t = 0.5 (≤ 1e-6).

## 3. The deciding read — the identity's own terms at θ*(t)

Channel S vs the independently computed P129-6 identity RHS
agree to ≤ 8.9×10⁻¹⁶ on the whole grid at every instant — the
decomposition below is the mechanism, not a fit. Headline arm,
at θ*(t) = π/2 (h-maximum at every instant; rho8 units):

| t | angular+grad | flare | rotation | cross-term | R_,tt term | **t-terms total** | static+rot | **S(θ*)** |
|---|---|---|---|---|---|---|---|---|
| 0.0 | −0.9375 | −0.5000 | 0 | 0.0000 | +1.8688 | **+1.8688** | −1.4375 | **+0.4313** |
| 0.1 | −0.9122 | −0.4972 | 0 | −0.0214 | +1.8795 | **+1.8580** | −1.4094 | **+0.4486** |
| 0.2 | −0.8326 | −0.4889 | 0 | −0.0872 | +1.9124 | **+1.8252** | −1.3215 | **+0.5037** |
| 0.3 | −0.6859 | −0.4757 | 0 | −0.2021 | +1.9699 | **+1.7678** | −1.1615 | **+0.6063** |
| 0.4 | −0.4450 | −0.4585 | 0 | −0.3757 | +2.0565 | **+1.6808** | −0.9035 | **+0.7773** |
| 0.5 | −0.0573 | −0.4384 | 0 | −0.6259 | +2.1797 | **+1.5538** | −0.4957 | **+1.0581** |

Answers to the registered questions, plainly:

- **Does the t-term contribution lift NEC_ρ at θ*? Yes — at
  every instant.** The t-terms total +1.8688 at t = 0, easing to
  +1.5538 at t = 0.5, against a static+rotation part that is
  negative at every instant (−1.4375 → −0.4957). S(θ*) is
  positive throughout, smallest at t = 0 (+0.4313) and growing
  to +1.0581 at t = 0.5. No sampled instant re-imposes the pin
  at θ*.
- **Versus the −4.0625 rotation-alone read:** on the control
  datum (CA/CB — the identical geometry P230-2 audited) the
  t-terms are zero by construction and the pin reads −4.0625.
  On the combined datum the geometry differs (flare −0.5000, not
  −3.125: R_,ρρ = 0.2, not 1.25), so the honest comparison is
  term-by-term, as tabled: the lift the t-terms must supply
  against this datum's own static+rotation part is 1.4375 at
  t = 0 (0.4957 at t = 0.5); they supply 1.8688 (1.5538) — the
  break clears its own bar at every instant, with margin
  +0.4313 rising to +1.0581 at θ*.
- **Which t-term carries it: the R_,tt term alone.** It grows
  +1.8688 → +2.1797 (R₀(θ*,t) shrinks 0.800 → 0.686 as the
  throat breathes in). The cross-term
  +2e^{−2Φ₀}(R_,t/R₀)(Φ_,t + μ_,t) is **negative on this datum
  at every t > 0** (0 → −0.6259): Φ_,t ≡ 0 in the A-branch pose,
  R_,t(θ*) = t·Att(θ*) < 0 and the lock's μ_,t(θ*) > 0, so the
  cross-term taxes the break instead of helping it — the
  opposite sign choice from P129-6's Exhibit B, whose factors
  were posed favourable. The break here is Exhibit A's
  mechanism (R_,tt < 0 through the lock/compensator pose),
  priced against a hostile cross-term.
- **Rotation's part:** exactly 0 at θ* at every instant (as in
  P230-2), and ≤ 0 off θ*: at ω_a = 0.2 it costs the NEC_ρ grid
  minimum 0.0114 of margin at t = 0.5 (baseline +0.0248 →
  headline +0.0134). Rotation neither helps nor, at this
  strength, breaks the pin clause.

## 4. Worst-instant clause table (headline arm) — and the fences

Per-clause worst over t ∈ [0, 0.5] (min / median / max are over
the θ-grid at the worst instant):

| clause | worst min | at t | median | max |
|---|---|---|---|---|
| NEC_ρ | **+0.0134** | 0.5 | +0.5707 | +1.3727 |
| NEC_θ | +1.0626 | 0.0 | +1.2313 | +1.5312 |
| NEC_φ | **−0.6298** | 0.5 | +1.2379 | +1.7301 |
| WEC | +1.0565 | 0.0 | +1.0603 | +1.0625 |
| DEC_ρ | **+0.0134** | 0.5 | +0.5707 | +1.0613 |
| DEC_θ | +0.5911 | 0.5 | +0.7967 | +1.0621 |
| DEC_φ | **−0.6298** | 0.5 | +0.7233 | +1.2864 |

Face facts (stated on the verdict, per registration §6):

1. **The full seven-clause set does NOT pass at the worst
   instant.** NEC_φ = DEC_φ fail from t = 0.400, worst
   −0.6297872673028908 at t = 0.5 — bit-identical to the
   ω_a = 0 baseline: this is the A branch's known μ-drift
   carrier (P169-1), binding at an angle where sin²θ ≈ 0, so
   rotation is exactly neutral to it, and the t-terms that
   break the pin do not repair it. Sustainment of this clause
   is the named successor (below).
2. **The headline NEC_ρ worst-instant margin is thin:**
   +0.0134 at t = 0.5, and its argmin has moved off θ*
   (θ ≈ 0.813) — at θ* itself the margin is +1.0581. The
   erosion is the same spatial drift that carries NEC_φ,
   read on the radial clause.
3. **ω_a = 0.4 fence:** at the strongest rotation arm the
   worst instant DOES re-impose an NEC_ρ failure —
   grid min −0.020876 at t = 0.5 (off-θ*, θ ≈ 0.813 region;
   S(θ*) itself remains +1.0581, rotation being zero there).
   The break at datum level is therefore stated for the
   headline datum (ω_a = 0.2, the P129-6 exhibit scale, and
   ω_a = 0.1, whose worst NEC_ρ min is +0.0220); at ω_a = 0.4
   rotation's off-θ* subtraction (−½ sin²θ e^{−2Φ₀}(∂_θω₀)²,
   ≤ 0 everywhere) exhausts the thin drift-eroded margin.
   Form 2's mechanism is real at that arm and is priced here
   rather than allowed to swallow the headline datum's
   registered read.
4. **W₁ only hurts, again:** the priced W₁ = 0.3 sin²θ arm
   leaves NEC_ρ untouched (+0.0134) and worsens NEC_φ/DEC_φ
   to −0.655842 at t = 0.5.

## 5. Named successor

**Sustainment of the combined-class datum**: a successor
registration that carries the combined pose (rotation +
time-dependent shape + compensator) AND a drift control for
the NEC_φ/DEC_φ carrier — e.g. P169-2's t-controlled
spatial-jet pose crossed with rotation, or an S-aware /
NEC_φ-aware posed degree of freedom — read at the worst
instant on the same seven clauses. Until that runs, the
standing statement is exactly this memo's: the Phase 77 pin
is broken at datum level in the combined class by the R_,tt
t-term (worst-instant NEC_ρ +0.0134 grid / +1.0581 at θ* on
the headline datum), and the combined datum as posed is NOT
sustained — NEC_φ/DEC_φ fail from t = 0.400.

## 6. Scope fences

Jet scope, per-instant diagonal ZAMO reads, 21 sampled
instants of one lock march; datum ≠ construction (no global
solution, no EOM claim beyond C2's configuration-level SOS
identity). The −4.0625 comparison is term-by-term across two
different geometries, stated as such in §3. No heavy compute
was used (one local march, seconds-scale reads). No ledger
append, no launches, nobody contacted.

## Files

- `phase245/work/p2452_registration.md` — registration +
  verdict forms + decision rules, written before computation.
- `phase245/work/p2452_run.py` — driver (controls CA/CB/C2/C3,
  then the main read).
- `phase245/work/p2452_check.py` — checker, ALL PASS (24/24).
- `phase245/results/p2452_results.json` — full reads (per-arm,
  per-instant clause min/median/max, identity decompositions
  at θ*, momentum maxima).
- `phase245/results/p2452_memo.md` — this memo.
