# Gate 4 — summary of the Novelty & Verification Gate on the Phase 15–16 claims

Gate 4 applied the programme's two-part test to three results
from Phase 15 (screened Einstein-aether) and Phase 16 (dynamic
shells; transient quantum-inequality law): **(a) novelty** —
a documented literature search (queries logged verbatim,
sources graded) for the claim's exact statement and its near
neighbours; **(b) correctness** — an independent second path
(fresh code written from the claim statement, not a re-run of
the phase scripts) reproducing the deciding computations.
Six workers: N1/N2/N3 (novelty), V1/V2/V3 (correctness). All
arithmetic float64. Gate completed 2026-11-21. This summary is
faithful to the gate's ground record; the claims themselves
appear, in gate-approved form only, in `CLAIMS3.md`.

## Verdicts at a glance

| Claim | Novelty | Correctness | Gate verdict |
|---|---|---|---|
| G4-1(a) Breathing shell + motion tax | NOVEL (delimited; robustness-map component PARTIALLY KNOWN) | REPRODUCED, one fragility caveat | **UPLOAD-READY AFTER RESTATEMENT** |
| G4-1(b) Transient QI law | PARTIALLY KNOWN (all three components) | REPRODUCED exactly | **UPLOAD-READY** |
| G4-2 Screening construction + design laws | PARTIALLY KNOWN overall; components (B), (C) NOVEL | REPRODUCED (all spot sub-items) | **UPLOAD-READY AFTER RESTATEMENT** |

No claim was found KNOWN outright, and no correctness axis
FAILED. **No superluminal result is claimed in any of the
three.**

## G4-1(a) — Breathing shell and the motion tax

**Novelty (N1; 29 logged queries, 16 graded sources).** NOVEL
as stated results, per component: (i) the per-instant
full-period energy-condition audit of a genuinely
time-dependent warp shell — the literature instead has
analytic generic theorems over time-dependent classes (Natário
gr-qc/0110086; Santiago–Schuster–Visser arXiv:2105.03079),
time as a plotting axis for other quantities, and
single-instant/constant-velocity audits; (ii) a breathing
configuration legal at every audited instant — the only near
neighbour is White's 2012 oscillation conjecture (NASA NTRS
20110015936 lineage), a conjecture with no metric or audit,
pointing in the opposite direction to the measured result;
(iii) the frozen-vs-dynamic separation, pure ∂_t failures, the
measured ∂_t tax, and "rate, not amplitude, kills" — all four
not found; (iv) the dynamic robustness/island map — PARTIALLY
KNOWN: static parameter scans are published (Le
arXiv:2605.25417, a 600-configuration scan; Warp Factory
sweeps); the dynamic full-period island map was not found.

**Correctness (V1; fresh 2nd-order non-stationary auditor).**
REPRODUCED with one fragility caveat. Stationary control
+1.212e-05 (h = 0.30) → +1.196e-05 (h = 0.075), converging onto
the claimed +1.1949e-05. Breathing δ = 0.5 worst instant
t = 10: SEC +7.22e-06 at h = 0.15 vs claimed +7.20e-06 (~1%).
The δ = 1.0, t = 26.67 frozen-vs-dynamic split's SIGNS confirm
at matched h = 0.30 (frozen +1.548e-05, Type I 1.000; dynamic
−4.59e-05, Type I 0.982 vs claimed −5.46e-05 / 0.970); the
dynamic audit is negative at every h in both paths, its
failure carried by non-Type-I points in both paths.
**Caveat:** the frozen pass is not h-robust in the second
path — at h ≤ 0.15 a handful of core points at r = 11.00 cross
marginally into Type IV (Eulerian flux converging to ~3.1e-05
vs a Type-I threshold of ~2.9e-05; h = 0.3 underestimates it
at ~2.3e-05); frozen sampled margins go slightly negative at
fine h (−1.10e-05 at h = 0.15) while frozen Type-I-only
margins stay positive at all h. The gate therefore required
the isolation to be restated in Type-I-margin form (the
restated text is in `CLAIMS3.md`, verbatim).

**Wording conditions carried into the claim:** N1's
delimitation sentence verbatim; never "first dynamic warp
drive"; White's conjecture flagged and stated as NOT
confirmed; never "stable" — "robust-within-audit", with
evolution-sense dynamical stability explicitly not
established; "legal at every instant" and "rate, not
amplitude, kills" carry their sampling hedges (12 audited
instants for the period audit, 8 in the robustness map,
h = 0.3/0.15; T = 40 vs T = 200 in one family; non-monotone
amplitude response); no refutation or evasion of Natário or
Santiago–Schuster–Visser claimed (scope, not victory); the
∂_t tax quoted only with its parameters; scope GR only, one
shell family, β = 0.02.

## G4-1(b) — The transient quantum-inequality law

**Novelty (N2; 20 logged queries, 11 graded sources).**
PARTIALLY KNOWN on all three components. **Decisive prior
art: Pfenning & Ford 1997 (arXiv:gr-qc/9702026), eq. (17)** —
with its bracket neglected as the authors themselves do, it is
the claim's ratio set to unity for their piecewise-linear
profile (effectively k = 1), with sampling time in place of a
free pulse duration; solving it for the sampling time gives
the same √(l_PΔ) form, constant and β-dependence as τ* at
k = 1. Pfenning & Ford never state τ*: they eliminate the
sampling time via the curvature radius and report a thickness.
Not found anywhere: the ratio as a closed form in the free
variable (cτ/Δ)⁴; the tanh prefactor k = f′_max·Δ_eff ≈
1.50–1.61; the 162-row confirmation; τ* stated and evaluated
as a pulse lifetime; the duration-form incoherence
quantification; the duty-cycle bound; any application of
quantum interest (Ford & Roman 1999, arXiv:gr-qc/9901074) to a
warp pulse train.

**Correctness (V2; fresh symbolic + numeric path).**
REPRODUCED exactly. A sympy derivation from the defining
densities returns the claimed form divided by the derived form
= exactly 1 (prefactor πk²/3 and all exponents confirmed);
ratio(τ*) = 1 to ≤ 8.9e-16 across all 27 configurations; the
k range 1.50000016–1.61162355 over the 26 proper-wall
configurations matches the claimed 1.50–1.61 (the diffuse
outlier's k = 0.0690196 also matches, its true |f′| maximum
sitting at r ≈ 3.37 m — a trap V2 initially missed by 1.1% on
a narrow scan, recorded rather than hidden); six from-scratch
rows match to ≤ 4.3e-16 (closed form) and ≤ 3.1e-10 (ledger);
the duty cycle at R = 100 m, σ = 2/m, β = 1 reproduces
bit-identically (D_max = 4.9272835297184655e-71, identically
1/ratio at crossing).

**Numeric reconciliation (binding):** the exact sweep minimum
at crossing is **3.939904e64** (precisely
3.939904393564e+64, at R = 1 m, Δ_eff = 0.454 m, β = 0.1). The
Phase 16 memo's "≥ 4e64" and the "3.9e64" shorthand both round
this value; the claim quotes the exact row value.

**Wording conditions carried into the claim:** explicit credit
to Pfenning & Ford 1997 eq. (17) for the τ⁻⁴ scaling, the π/3,
the Δ²/(v_b²t₀⁴) structure and the τ* functional form; only
the delimited residue claimed (N2's delimitation sentence,
verbatim in `CLAIMS3.md`); τ identified as a wall lifetime,
not Pfenning–Ford's sampling time, with the 16–18 orders
measured against the light-crossing time Δ/c; the prefactor
tied to the Ford–Roman form of the bound (no universality —
the Fewster/Eveson prefactor is sampling-function dependent);
the binding label unsoftened (a QI-legal pulse is a statement
about quantum bounds, NOT a drive; the registered reading
OPEN-but-incoherent, CLOSED at every τ ≥ Δ/c, stated as
registered); quantum interest credited to Ford & Roman 1999;
scope limited to the one-shot Alcubierre tanh family at peak
density.

## G4-2 — The screening construction and its design laws

**Novelty (N3; 30 logged queries, 16 graded sources).**
PARTIALLY KNOWN overall, with two NOVEL components:
**(B)** couplings slaved to a ∇u-activity invariant Q with a
symmetron switch — NOVEL (delimited); **(C)** the verified
package on the warp bed — NOVEL (delimited, application
level). The known surroundings, all credited in the claim:
screened vector-tensor gravity (Beltrán Jiménez–Delvas
Fróes–Mota arXiv:1212.1923 — conformal vector, field vanishing
at high *density*); generalised-Proca Vainshtein screening;
GEA F(K) (Zlosnik–Ferreira–Starkman arXiv:astro-ph/0607411 —
a ∇u-invariant response with no switch); the c_i(φ) line
(Kanno–Soda via Donnelly–Jacobson arXiv:1007.2594;
Paliathanasis–Leon arXiv:2107.12546); K-mouflage
(arXiv:0905.2943 — trigger is the scalar's own X, closing
where the trigger is large: the opposite assignment); the
symmetron mechanism itself (Hinterbichler–Khoury
arXiv:1001.4525). Law (iv)'s formula V ~ Q²/(4μ) is published
symmetron algebra (in print since 2010) and is **not
claimed**; law (v)'s warning is published in temporal form
(Llinares–Mota; Noller et al.), with a published temporal
success as counterweight (arXiv:1802.04001) — the claim keeps
law (v) in its spatial, wall-scale form only.

**Correctness (V3; fresh machinery).** REPRODUCED on all three
spot sub-items. Minkowski with Eulerian u: Q absmax = 0.0
exactly. Exterior maximum Q = 7.953734828265921e-10 vs stored
7.953734828265919e-10 (relative difference 2.6e-16);
Q_crit = 2.3861204484797762e-08; S = 0.0 exactly on the
exterior at all three β. Screen open: S ≥ 0.5 at 1.000 of
binding points at all three β (n = 251/504/594; minimum
binding Q ~ 4000× above Q_crit — not marginal). The β = 1.1
row's screened partial coverage 0.8988095238 (453/504) is
bit-identical to the stored value and to the unscreened
(S ≡ 1) computation, both rounding to the Phase 10 value
0.899; screened full coverage also reproduces exactly
(0.291667). V3's honesty note stands: the near-machine-
precision agreement partly reflects shared finite-difference
conventions (step sizes and stencil order as shared
definitions).

**Wording conditions carried into the claim:** law (iv) only
in the gate's restated form (budgeting requirement +
trigger–budget pathology + decoupled repair window; the
formula credited to the symmetron literature); N3's
delimitation sentence verbatim; "screening solves the aether's
data problem" never unqualified — the evasion is scoped to
this bed's supply scan, with χ adiabatic, u prescribed
(conservation relative median 0.35–0.88), and the screen's own
stress not in the scan tensor; the PPN exclusion the
construction builds on is cited in Gate-2's restated form
(supply collapses toward the data-compatible corner;
α1 = −4c14 on the c13 = 0 slice); "symmetron-type transition
on Q" only; "exactly GR" / c_T = 1 carry their domain (the
sampled bed exterior); and the family closure at abstract
level, on the face of the claim: the screened-aether family
is CLOSED as a superluminal supply route (coverage ceiling
full 0.29 / 0.54 vs the 0.90 bar, screening-independent).

## Corrections the gate owed the internal records (errata)

The gate recorded three corrections to the Phase 15/16
records, logged as dated errata in those records on
2026-11-21 (appended, not silently absorbed):

1. `phase16/CHECKPOINT16.md` — "ERRATA (Gate-4, 2026-11-21)":
   P16-1's frozen control at δ = 1.0, t = 26.67 was an
   h = 0.3-only read; the frozen sampled margin +1.53e-05 must
   not be quoted without its resolution (at h ≤ 0.15 a second
   path finds marginal Type-IV points at r ≈ 11); the
   isolation survives in Type-I-margin form.
2. Same errata section: the QI sweep minimum at crossing is
   the exact row value 3.939904e64 (R = 1 m, Δ_eff = 0.454 m,
   β = 0.1), superseding both memo roundings.
3. `phase15/CHECKPOINT15.md` — "ERRATUM (Gate-4, 2026-11-21)":
   law (iv)'s formula V ~ Q²/(4μ) is published symmetron
   algebra (in print since 2010); the claimable content is the
   budgeting requirement, the trigger–budget pathology, and
   the decoupled repair window.

## Write-up-time novelty re-checks (required by the gate; run 2026-11-21)

The gate left two residual novelty items to close at write-up
time. Both were run as documented web searches before this
bundle was finalised. **Neither found anticipating prior art
for any claim.**

**Re-check 1 — N2's residual gaps for G4-1(b).**
(a) *Line-by-line check of Pfenning's dissertation, Chapter 5*
(arXiv:gr-qc/9805037, "A Dynamic Spacetime: The Warp Drive",
§§5.1–5.5, read in full): Chapter 5 reproduces the 1997
derivation — its eq. (5.17) is the paper's eq. (17); the
sampling time is then eliminated against the local curvature
radius (eqs. 5.19–5.20) to give the wall-thickness bound
(Δ ≲ 10²·v_b·l_P, eqs. 5.22–5.23), and §5.4 computes the total
energy; the §5.5 summary is stated entirely in thickness and
total-energy form. Chapter 5 contains **no** free-duration
ratio, **no** tanh-profile prefactor, **no** τ* stated as a
pulse lifetime, and **no** duty-cycle bound. Gap closed; no
anticipation.
(b) *Citing literature of arXiv:gr-qc/9702026:* targeted
searches over the citing literature (multiple query
formulations) surfaced only standard retellings of
Pfenning–Ford in thickness / total-energy form. No citing work
stating the closed-form duration ratio, the tanh prefactor k,
τ* as a lifetime, or a pulse-train duty-cycle bound was found.
Stated limitation: this was a documented web-index search, not
a direct INSPIRE-HEP API census of the citing list; the
residue's delimitation in `CLAIMS3.md` is worded "in the
sources searched" accordingly.

**Re-check 2 — N3's screened-khronometric / c_i(χ) watch for
G4-2.** Searches for a screened khronometric mechanism and for
environmentally triggered, scalar-switched aether couplings
c_i(χ) (including 2025–2026-targeted formulations) found **no**
screened-khronometric mechanism and **no** environmentally
triggered c_i(χ) preprint. The nearest khronometric hit
(Franchini–Herrero-Valea–Barausse, arXiv:2103.00929) concerns
GR-equivalence by exact coupling vanishing — a parameter
constraint, not an environmental screening mechanism; the
remaining hits were generic scalar-tensor screening reviews
(chameleon / symmetron / Vainshtein / K-mouflage). No
anticipation. Per N3's caveat this remains a bounded search:
a fresh re-check at any future write-up is still recommended,
and the claim's novelty is worded "not found in the
literature" on the documented searches, gate and re-check
combined.

## What the gate did not do

The gate prepared verdicts only. It uploaded nothing and
contacted no one. Publication of this bundle is a separate
step, taken under the programme's upload rule (gate first,
then upload), with code-generated diagrams for each claim
prepared from gate-cleared data only.
