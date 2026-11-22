# P16-2 — The transient quantum-inequality ledger (memo)

**Plain language first.** Phase 2 showed a warp wall cannot *stay* up:
the quantum rules allow only a speck of negative energy if it has to
last. This run asked the obvious escape hatch — what if the wall only
exists for a very short pulse? Short pulses are allowed to be much
stronger, so we checked exactly how short the pulse would have to be.

The answer: impossibly short for a wall. For every wall size and speed
we tested, the pulse would have to end about **10¹⁶–10¹⁸ times sooner**
than the time light needs just to cross the wall's own thickness. A
thing that disappears before light can cross it cannot be a wall while
it exists — there is no moment at which the whole wall is there. So
the verdict, in the language registered before the run, is
**"OPEN-but-incoherent" for every configuration, and CLOSED at every
duration at or above the thickness crossing time.** The one legal
timescale is the geometric-mean time √(l_P·Δ)/c — roughly 10⁻²⁶ s for
a metre-scale wall — which is a statement about quantum bounds, not
about anything that could hold a shape.

**Binding labelling: a QI-legal pulse is a statement about quantum
bounds, NOT a drive.**

## Method and validation

Constants (SI, float64): ħ = 1.054571817e-34 J·s, c = 299792458 m/s,
G = 6.67430e-11 m³ kg⁻¹ s⁻², l_P = √(ħG/c³) = 1.616255e-35 m.

Required density — Alcubierre Eulerian density, peak value:
ρ_req = β² c⁴/(32πG) · (f′_max)², with the angular factor
(y²+z²)/r² at its maximum of 1, β = v/c, and f the Phase 1 ledger's
tanh profile. **Validation:** integrating this density over space
reproduces the ledger's total energies — anchor R = 100 m, σ = 2/m,
v = 1: numeric −7.48112e29 kg vs ledger −7.48128e29 kg (relative
error 2.2e-5; all nine v = 1 sweep rows within that). Cross-check of
the legal side: the Ford–Roman bound at τ = (1 µm)/c gives
−3.003e-4 J/m³, vs the measured Casimir density −4.3e-4 J/m³ —
same order, as in W6.

Legal density: ρ_min(τ) = −(3/(32π²)) ħ/(c³τ⁴) (Ford–Roman).

Sweep: R ∈ {1, 10, 100} m × the ledger's three σ values per R
(Δ_eff from 0.150 m to 15.56 m) × β ∈ {0.1, 0.5, 1.0} = 27
configurations, each at six pulse durations from τ = Δ/c down
through √(l_P Δ)/c to the Planck time. Full 162-row table:
`p162_ledger.json`.

## (a) Results — the scaling law is exact

The candidate scaling is **confirmed, with its prefactor**:

    ratio (required/legal) = (π k²/3) · β² · (Δ/l_P)² · (cτ/Δ)⁴,
    k = f′_max · Δ_eff ≈ 1.50–1.61 for 26 of 27 configs.

The closed form matches every one of the 162 computed ratios to
machine precision (max deviation 3e-16 in log₁₀). A k-corrected
regression returns exponents exactly 2 (β), 2 (Δ/l_P), 4 (cτ/Δ) with
intercept log₁₀(π/3). (The one outlier config, R = 1 m, σ = 0.2/m,
has σR = 0.2 — a diffuse profile that never forms a proper wall —
and k = 0.069; it changes nothing below.)

Setting the ratio to 1 gives the exact legal duration:

    τ* = [3/(π k² β²)]^{1/4} · √(l_P Δ)/c

i.e. τ* is the geometric-mean time √(l_P Δ)/c times a factor between
0.8 and 12 depending on (k, β). Representative rows (β = 1):

| R (m) | Δ_eff (m) | ρ_req peak (J/m³) | ratio at τ = Δ/c | τ* (s) | τ*/(Δ/c) |
|---|---|---|---|---|---|
| 1 | 0.150 | 1.20e44 | 2.0e68 | 4.2e-27 | 8.4e-18 |
| 1 | 1.556 | 1.29e42 | 2.5e70 | 1.3e-26 | 2.5e-18 |
| 10 | 1.502 | 1.20e42 | 2.0e70 | 1.3e-26 | 2.7e-18 |
| 100 | 1.500 | 1.20e42 | 2.0e70 | 1.3e-26 | 2.7e-18 |
| 100 | 15.016 | 1.20e40 | 2.0e72 | 4.2e-26 | 8.4e-19 |
| 100 | 0.150 | 1.20e44 | 2.0e68 | 4.2e-27 | 8.4e-18 |

Slowing down helps only as β²: even at β = 0.1 the ratio at the
crossing time is still ≥ 4e64. Thinning the wall does not help
either — ρ_req grows as 1/Δ² while the bound at τ = Δ/c falls as
1/Δ⁴, so the ratio at crossing time grows as (Δ/l_P)² regardless.

## (b) Pulsing / pulse trains — no escape through repetition

A wall that exists only as a repeating pulse train with duty cycle D
has time-averaged negative density D·ρ_req. Making even the *average*
legal against the sustained bound at the wall's own scale requires
D ≤ ~4e-73 to 2.5e-65 (per-config values in the JSON) — the wall would
be absent essentially all of the time. And that arithmetic is
generous, because of **quantum interest** (Ford–Roman): a
negative-energy pulse must be followed or preceded by a
positive-energy pulse that *overpays* it, with the required
overpayment growing as the separation between the pulses grows. An
endless train therefore cannot book each pulse against the
short-pulse τ⁻⁴ bound independently — that double-counts the
loophole. The long-time average is governed by W6's sustained law,
E_legal(L) = (3/(32π²)) ħc/L. Pulsing changes *when* the bill is
presented, not its size.

**Gap note:** `phase16/results/p161_*.json` did not exist when this
ran, so P16-1's actual E_-(t) could not be tabulated against the
bound. The one-shot ledger above is complete without it; the P16-1
tabulation can be appended when those results land, and the scaling
law here predicts it will land in the same place (Finalist-A's
densities are far below Alcubierre-family peaks, but its duration
scales are macroscopic, where the bound is ~1e-28 J-scale in total).

## (c) Verdict (pre-registered reading)

- **OPEN** (legal at τ ≥ thickness crossing time): **none**, of 27.
- **OPEN-but-incoherent**: **all 27** — a legal window exists only at
  τ ≤ τ* ≈ √(l_P Δ)/c, which is 17–18 orders of magnitude below the
  thickness crossing time Δ/c. QI-legal as a pulse; unable to be a
  wall while it exists.
- **CLOSED at all τ ≥ Δ/c**: yes, for every (R, Δ, v) — the smallest
  ratio at the crossing time anywhere in the sweep is 4e64.

Mechanism, in one line: the required density is set by (c⁴/G)/Δ² —
a Planck-density suppressed only by (l_P/Δ)² — while the legal pulse
density grows only as τ⁻⁴, so legality is bought only by shrinking τ
down to where √(l_P Δ)/c lives, far below any crossing time.

Files: `phase16/p162_ledger.py`, `phase16/results/p162_ledger.json`.
Internal only.
