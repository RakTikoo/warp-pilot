# P257-1 MEMO — LEG 1: FULL TENSOR MATCH AT THE WORST SITE

**Verdict (registered form): FULL MATCH AT THE SITE.**

Registration: `phase257/work/p257_registration.md` (written
before any deciding computation). Driver:
`phase257/work/p257_leg1_run.py`. Independent checker:
`phase257/work/p257_check.py` (rebuilds the fitted tensor via
Phase 253's bilinear builder — a different code path from the
pairwise formula used in the fit): **all checks PASS**,
R = 1.767689307869179×10⁻¹⁶ via the checker path. Numbers:
`phase257/results/p257_leg1_results.json`,
`phase257/results/p257_check.json`; the winning configuration
is persisted at `phase257/work/p257_bestfit.json`. Frame of
record: Phase 166 pin, Gate-19-corrected tensor lineage,
programme venv, float64. Nothing appended to the ledger;
nothing outside phase257/ edited.

## Controls (run first; ALL PASS)

- C1: Phase 253's deciding configuration reproduced:
  T(k*,k*) = −10.878491901602604 (exact to the stored digits),
  ρ = +2.2403520362312377, Dirac residuals ≤ 3.5×10⁻¹⁵.
- C2: stored Phase 235 rows exact; That contracted with k*
  reproduces −0.0038017605291582623.
- C3: real-spectrum floor recomputed from That·η:
  |Im λ|max = 8.201278128046272×10⁻⁴ (= 34.2% of
  |T_req|_F = 2.3978336134611576×10⁻³). T_req's mixed
  eigenvalues: {0.000676 ± 0.000820 i, 0.000113, 0.001042} —
  Type IV at the site, as registered.
- C4 (full-tensor second path): the pairwise mode-tensor
  formula reproduces the bilinear builder's T_ab at the
  deciding configuration to 5.3×10⁻¹⁵ Frobenius.

## The type derivation — where the wall actually was

(a) On shell, L = 0 pointwise for any superposition, so T_ab
is exactly the symmetrised derivative bilinear, with the
pairwise form T_ab = Σ_ij c_i* c_j · ¼[(p_i+p_j)_a (ū_iγ_b u_j)
+ (p_i+p_j)_b (ū_iγ_a u_j)] (verified by C4).

(b) SINGLE MODE: T_ab = p_(a j_b), p future timelike, j future
causal (Fierz) — Type-I. Verified by direct Segre
classification of Phase 253's three registered probe modes:
all Type-I, max |Im λ| = 0.

(c) SUPERPOSITIONS: the cross terms carry transition currents
J_ij = ū_iγu_j, which are complex and not causally
constrained — (b)'s argument does not extend, and the run
decides the question empirically: **of 300 random
superpositions (N = 2–5, m = 1), 40 (13.3%) have a complex
mixed-eigenvalue pair — Dirac superpositions are NOT confined
to real spectrum.** The C3 floor, which bounds every
real-spectrum tensor, therefore does not bind this family.
This is the tensor-level analogue of Phase 253's sign result:
the same interference that makes N = A∘C indefinite for the
contraction makes the full tensor's spectrum complex.

## The fits (m = 1; residual R = |T_Dirac − T_req|_F)

| mode set | R_free | R_constr (contraction held) | R_constr / floor |
|---|---|---|---|
| N=3 (Phase 253 deciding modes) | 1.437×10⁻³ | 2.564×10⁻³ | 3.13 |
| N=4 (best of 8 restarts) | 1.466×10⁻³ | 1.511×10⁻³ | 1.84 |
| **N=6 (best of 8 restarts)** | **3.876×10⁻⁹** | **1.767×10⁻¹⁶** | **2.2×10⁻¹³** |
| N=8 | 8.890×10⁻⁹ | 4.213×10⁻¹² | 5.1×10⁻⁹ |
| N=12 | 6.167×10⁻⁹ | 6.055×10⁻¹¹ | 7.4×10⁻⁸ |

The threshold is sharp in mode count: N ≤ 4 cannot beat
~1.8× the real-spectrum floor even though their fitted
tensors are already Type IV (having a complex spectrum is
necessary, not sufficient — the component-by-component fit
needs the interference dimension); at N = 6 the constrained
fit closes to machine precision with the contraction held to
6×10⁻¹⁴ relative. The m = 0 secondary was not triggered
(the m = 1 fit did not stall above 2× floor; it closed).

**The winning configuration** (N = 6, m = 1, positive
frequency, on shell; full spinors in p257_bestfit.json):
momenta (−0.237, −0.565, −0.563), (−0.089, 0.050, 0.010),
(−3.500, −3.804, −0.148), (0.186, −0.679, 1.426),
(1.130, 1.284, 1.456), (−0.890, 2.669, −0.552);
Σ|c|² = 0.007884 at the fitted scale. Its mixed eigenvalues
reproduce T_req's to the digits shown in the results JSON
(0.0006755 ± 0.0008201 i, 0.0001130, 0.0010419): the Dirac
field at this site IS a non-Type-I tensor, eigenstructure
included.

## Verdict and fences

**FULL MATCH AT THE SITE** — the registered bar
(R_constr ≤ 1e-9) is met at 1.8×10⁻¹⁶, checker-confirmed on
an independent code path. Phase 244's closing sentence named
what could change the drive picture: "a healthy sector
producing non-Type-I stress — none is in the registered
libraries." That premise is now false at the pointwise,
tangent-frame level: the spinor sector was in the library,
and its superpositions produce exactly the drive's
non-Type-I stress at the drive's worst site. Leg 2 therefore
runs (gate: FULL MATCH).

Fences: the match is POINTWISE (one site, tangent frame,
x = 0 of the superposition) and a TEST-FIELD statement: no
global on-background Dirac field, no normalisability, no
backreaction is claimed (Phase 253 fences (b), (d) stand;
Leg 2 prices the neighbourhood, Leg 3 the budget sketch).
The type-scan statement (c) is family-scope (300 draws,
registered distribution), not a theorem about all Dirac
configurations; the derivation (a)–(b) is exact.
