# P33-5 — WALLS + Λ AND MAGNETIC FIELD

Worker P33-5, Phase 33. Bars and verdict language per
CHECKPOINT33.md (pre-registered, unedited). float64 throughout;
scripts `p335_rerun.py`, `p335_pricing.py`; numbers in
`p335_results.json` (+ `p335_rerun.json`).

## Baseline

Finalist family (Phase 1 / REPORT.md): β=0.02 passes
(2.69×10²⁷ kg), β=0.05 passes at compactness M/R₁ = 0.383,
**β=0.1 row EMPTY**. All EC margins/deficits are in the
programme's geometric audit units, T in 1/m² (verify_metric.py:
T = G/8π, G = c = 1, lengths in metres). SI conversion used for
every pricing statement: ρ_SI [J/m³] = T_geom × c⁴/G,
c⁴/G = 1.210×10⁴⁴ J/m³ per 1/m².

**The β=0.1 deficit, three labelled sources** (pricing uses the
smallest — the most augmentation-friendly — so both FAILs are
lower bounds on the true price):

- **D1 = 2.06×10⁻⁷ m⁻²** (recorded, REPORT §1.2): closest
  β=0.1 near-miss of the named families (autodiff tiebreak
  +1.3×10⁻⁹, uncertifiable).
- **D2 = 1.8×10⁻⁶ m⁻²** (recorded, REPORT §1.3, N3 run 2):
  conditions-first tail DEC deficit, resolution-independent —
  a ρ≈0, p_r≈+1.8×10⁻⁶ tail.
- **D3 (re-run this item, `p335_rerun.py`)**: the Finalist
  machinery DOES re-run. Unoptimised profiles at β=0.1 fail
  outright: Finalist-A profile (10,20), M=2.0 → worst margin
  −1.0 (DEC, r=11 m); a frontier-like (5,10), M=1.915
  (M/R₁=0.383) profile → worst SEC −3.70×10⁻³, DEC
  −2.17×10⁻⁶ at r=6 m. The re-run's DEC scale corroborates D2;
  nothing in the re-run contradicts the recorded wall (P8:
  NEC/SEC pin ~1e-9 vs mass in optimised families).

## (a) Cosmological constant — measured Λ only

Λ = 1.09×10⁻⁵² m⁻² (no dialling). As a stress-energy,
T_Λ = −(Λ/8π) g_ab, i.e. ρ_Λ = Λ/(8π), p_Λ = −ρ_Λ:

- ρ_Λ = **4.34×10⁻⁵⁴ m⁻²** geometric
  = **5.25×10⁻¹⁰ J/m³** SI (the known dark-energy density —
  conversion cross-check passed).
- Dimensionless effect at shell scale: ΛR² at R = 20 m is
  4.4×10⁻⁵⁰, against compactness ~0.383.

**Identity-level anatomy (before magnitude):** Λ has
ρ + p = 0 exactly, so its NEC shift is **zero**; ρ − |p| = 0,
so its DEC shift is **zero**; its only nonzero EC shift is
SEC, ρ + Σp = −2ρ_Λ < 0 — the **wrong sign**. Λ cannot cover
an NEC or DEC deficit at any magnitude, and at an SEC-binding
site it makes the margin worse. Priced on magnitude anyway,
as tasked:

- vs D1: ρ_Λ/D1 = 2.1×10⁻⁴⁷ → **46.7 orders of magnitude short**
- vs D2: ρ_Λ/D2 = 2.4×10⁻⁴⁸ → **47.6 orders of magnitude short**

**Verdict (a): AUGMENTED-FAIL** — deciding terms: NEC/DEC
neutrality of Λ by identity (ρ+p ≡ 0) and SEC anti-alignment;
magnitude price **≈47 orders short** (46.7 vs the smallest
recorded deficit).

## (b) Uniform magnetic field

EM stress-energy (B along ẑ): ρ_EM = B²/(2μ₀) > 0,
p_⊥ = +ρ_EM, p_∥ = −ρ_EM (tension along B). EM alone is
EC-legal: NEC = 2ρ_EM (⊥) / 0 (∥), WEC = ρ_EM, SEC ≥ 0,
DEC = ρ_EM − |p| = 0 (saturated everywhere). No clause of
the EM tensor itself is illegal — it is real stuff, not
exotic matter under a new name.

**Stated reduction:** at the binding site, optimally oriented,
the binding EC combination gains between ρ_EM and 2ρ_EM;
pricing sets ρ_EM = D (most augmentation-friendly). Worked
example (D2 tail site, ρ≈0, p_r = +1.8×10⁻⁶, tension axis
along r, ρ_EM = D2): after summation ρ = 1.8×10⁻⁶, p_r = 0,
p_t = +1.8×10⁻⁶ → DEC_r = +1.8×10⁻⁶, NEC_r = +1.8×10⁻⁶,
NEC_t = +3.6×10⁻⁶ — but **DEC_t = 0 exactly** (saturated,
uncertifiable, the same status as the record's +1.3×10⁻⁹
tiebreak). So even at the required B, the augmented tail sits
on the DEC boundary in the transverse direction, not above it.

**Clause-breakage check:** the tension direction is the risk,
as tasked. Along B, EM adds NEC exactly 0 — it never breaks
NEC — and DEC exactly 0 in its own frame. But orientation is
not free: **a single uniform B cannot be radial everywhere on
a spherical shell** (a radial B is a monopole, ∇·B ≠ 0).
Uniform B is radial only at the poles; at the equator it is
tangential, where its +ρ_EM pressure *adds* to the radial
pressure and **worsens radial DEC there**. The priced B below
is therefore a lower bound for one uniform field over the
whole shell.

**Required B** (ρ_EM = D; B = √(2μ₀·D·c⁴/G)):

| Deficit | ρ_EM needed (J/m³) | B required | vs 10³ T pulsed | vs B_c = 4.4×10⁹ T |
|---|---|---|---|---|
| D1 = 2.06×10⁻⁷ m⁻² | 2.49×10³⁷ | **7.9×10¹⁵ T** | 12.9 orders above | 6.3 orders above (1.8×10⁶×) |
| D2 = 1.8×10⁻⁶ m⁻² | 2.18×10³⁸ | **2.3×10¹⁶ T** | 13.4 orders above | 6.7 orders above |
| D3 (re-run DEC) | 2.63×10³⁸ | 2.6×10¹⁶ T | 13.4 orders above | 6.8 orders above |

Against 45 T sustained the D1 price is 14.2 orders above.
The required field exceeds even the Schwinger critical field
by ~6–7 orders of magnitude — long before any engineering
limit, the vacuum itself would be in the pair-production
regime the classical EM audit assumes away.

**Melvin cost (part of the verdict, per checkpoint):** a
uniform B is not asymptotically flat — the exterior is a
Melvin magnetic universe, not Schwarzschild. Its
curvature/flux-tube scale at the required field,
~1/B_geom with ρ_EM = B_geom²/8π, is **≈440 m (D1) /
≈150 m (D2)** — only ~10–20× the shell radii (5–30 m). The
"wall in flat space" problem has been replaced by a wall in a
self-gravitating magnetic universe whose field energy is
unbounded at large radius. That is a different, harder
problem, not a repaired Finalist.

**Verdict (b): AUGMENTED-FAIL** — deciding term: required
field **B ≈ 7.9×10¹⁵ T** against the smallest recorded
deficit (2.3×10¹⁶ T against D2), i.e. **12.9 orders above the
10³ T pulsed bar** and ~6.3 orders above B_c; compounded by
Melvin (non-asymptotically-flat) asymptotics and the
uniform-B/monopole orientation obstruction.

## Follow-up experiment (failure protocol)

Both failures are priced, and one is identity-level (Λ), so
the follow-up targets the only lever the EM analysis exposed:
**anisotropy with a free axis field** — replace the uniform B
by a *toroidal* field configuration (B_φ, divergence-free,
axis following the shell's tangential direction everywhere),
re-run the p335_rerun audit with the EM tensor summed in, and
read whether the DEC_t saturation and the equatorial DEC
worsening both disappear at ρ_EM = D2, or whether the
saturation is structural for any |p| = ρ component (a
Maxwell field saturates DEC identically, so the prediction
registered here is: toroidal geometry fixes the orientation
obstruction but NOT the DEC saturation — the augmented margin
would pin at exactly 0, uncertifiable, at any B). Reopening
condition for (a): none at measured Λ — the neutrality is an
identity, not a magnitude gap. Reopening condition for (b):
a legal component with |p| < ρ strictly (DEC margin > 0 of
its own) at ρ ~ 10⁻⁶ m⁻² geometric — that is an ordinary
fluid/gas question, belonging to the fluid items, not to EM.
