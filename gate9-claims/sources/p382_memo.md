# P38-2 MEMO — Classical linearised-stability probe on the conformal-gravity T-b throat (FU-P323-3)

**VERDICT: CLASSICALLY STABLE (computable sectors — named below).**
**(V-b) stands UNDECIDED** (Pais–Uhlenbeck ghost vs Mannheim PT-symmetric
quantisation — opposed literature positions), attached unchanged and
untouched by this item in either direction.
**Language lock: this is a "scan signal under attack" — nothing stronger.**

Computable sectors named: (i) the exact static ℓ=0 sector (R2, sympy,
Phase-32 gated engine); (ii) the dynamic ℓ=0 Galerkin trial space, read on
its physical quotient spectrum (R3/R4 as corrected — see §4); (iii) the
principal-symbol / short-wavelength sector in all ℓ (algebraic, §6/R5).
NOT computable (registered obstructions, unchanged): the ℓ≥1
long-wavelength spectrum (no published Regge–Wheeler-type formalism for the
Bach system on a Morris–Thorne background), non-spherical/nonlinear
stability, and well-posedness of the full nonlinear Bach IVP. The dynamic
read is Galerkin/variational, NOT an exact spectrum — scoped exactly as
registered in the run record.

This memo was completed by the finisher worker from two predecessors'
artifacts (infrastructure deaths, artifacts sound). R1/R2 are consolidated
from `p382_static.json` and were never recomputed. Checker:
`p382_checker.json` — 14/15 registered checks pass; the one failure is the
numeric packet sign check, reported honestly in §5 with its anatomy.

---

## 1. R1 (re-gate) — PASS

Phase-32 engine on the unperturbed T-b metric reproduces the Phase-32
closed-form Bach components to max relative error **1.86e-13** (bar 1e-9).
Sign check 1 (background ρ = −4α_gB^t_t > 0 for α_g > 0) is carried by the
same closed forms.

## 2. R2 (static linearised Bach) — COMPLETE

δB tables for δb and δΦ trial perturbations in `p382_static.json`:
trace of δB ≤ 1.33e-9 (δb) / 1.76e-11 (δΦ) absolute against components of
size ~10⁻²–10⁻¹; finite-difference cross-check disagreement ≤ 2.3e-8
relative. δB is finite at the throat approach (r = 1.001, 1.01 tabulated)
and decays as ~r⁻⁵ at large r. No static zero-mode pathology in the trial
families.

## 3. Gauge instrument checks — CERTIFIED (with the diffeo anatomy)

Registered check (run record, sign check 2): *for a pure-gauge
perturbation the FULL S₂ must vanish identically*, |S₂^gauge| ≤ 1e-6
relative to the physical A-mode scale (0.011145), else the instrument is
indicted and no root may be believed.

**Conformal trial — PASS, direct.** F along the conformal trial is
~1e-10 absolute, max relative 1.85e-8 ≤ 1e-6. (The trial adds the same
profile to all three log-metric components, i.e. it follows the exact
conformal orbit e^{2εP}g, along which √−g C² is pointwise invariant.)

**Diffeo trial — the two reads reconciled.** The DIRECT evaluation
(linearised δg substituted into S₂, i.e. the second derivative of S along
the LINEAR path in field space) gives F = 0.007323 (χ=(r−1)²/r³, rel
0.657) and F = 1.4995 (compact χ, rel 134.5) — an apparent instrument
failure. The gauge-ORBIT evaluation (`p382_gauge_orbit.json`: action
integral along the exact pullback orbit) gives quadratic coefficients
−2.09e-8 and −3.08e-7 at Nr=2000. **The orbit extraction is the literal
implementation of the registered check**, and the algebra says why:

  0 = d²/dε²|₀ S_W[φ_ε* g]  =  S″[δg, δg]  +  S′[δ²g]

Gauge invariance constrains only the sum. The direct evaluation computes
S″[δg,δg] alone; the second term does not vanish because S′ ≠ 0 for the
Weyl action ALONE on this background — the background is held by matter
(4α_gB = T ≠ 0), it is not a stationary point of S_W. δg itself was
constructed correctly (δb = χb′ + χ′, δc = χ/r is the exact linearised
pullback in the (b,c) exponents); the failure is the missing δ²g, whose
exact-orbit coefficients are δ²b = χ²b″/2 − χ′²/2, δ²c = −χ²/(2r²).

Measured anatomy (finisher, `p382_gauge_anatomy.json`): adding δ²g to the
path gives q2 = −2.06e-8 / −3.12e-7, agreeing with the independent orbit
extraction (−2.09e-8 / −3.08e-7) to ~2%; and S′[δ²g] = corrected − linear
= −0.00732307 / −1.49951940, cancelling the direct values digit for digit.
Grid refinement: the orbit q2 falls as 1/Nr² (×4 per doubling:
−2.09e-8 → −5.3e-9; −3.08e-7 → −7.7e-8), Richardson continuum value
~1e-10 absolute ≈ 1e-8 relative to the A-mode scale — under the 1e-6 bar.
(The orbit integral's small LINEAR drift in ε is a first-variation /
boundary-flux effect — χ(30) ≠ 0 for the original χ — and is not part of
S₂.) **The gauge check is therefore certified and the instrument is NOT
indicted; roots from the scans may be believed, subject to §4.**

## 4. R3/R4 (dynamic scans) — no tachyon; the registered det read is structurally void, its quotient form decides

**Snapshot/average anatomy (affects every fit).** The instrument's
F(ω=0) is a t=0 *snapshot*; F(ω>0) is a period *average*. For cos(ωt)
modes the ω⁰ (cos²) part averages to exactly half its snapshot value:
F(0)_snap / F_avg(0+) = **2.0000000** for every mode measured. The
registered 3-point fit through the snapshot point therefore distorts A₀
and manufactures roots (mode A's "complex pair" [2.5, 1.323] follows
algebraically from F(1)=F(2)=F(0)_snap/2 alone). All scans below were
computed under BOTH extraction conventions (snapshot fit through
F(0),F(1),F(2) — as registered — and averaged-branch fit through
F(1),F(2),F(3), validated at held-out ω=0.5,1.5 to ≤3.6e-9 relative);
no conclusion differs between them.

**Structural finding: det M ≡ 0 identically.** With a common radial
profile in the three components (a,b,c), conformal invariance forces the
exact identities F_AB = F_C, F_AC = F_B, F_BC = F_A (the quadratic form
depends only on pairwise differences of the components). Hence the
Galerkin matrix M(ω²) has the EXACT null vector (1,1,1) — the conformal
gauge direction — for every ω². Measured: max |det M|/‖M‖³ = 2.4e-9,
row-sum residuals ≤ 1.5e-8 relative, null-eigenvector alignment
1 − 1e-15, across all blocks. **Every raw-det sign and bracket is grid
noise around an identically-zero determinant.** Direct evidence: the
predecessor's primary det (Nr=2000) was negative at all 200 points; the
Nr=1000 recompute is positive at all 200. The R4 read as literally
registered (scan det M for a sign change) cannot decide anything; its
correct implementation on the same data is the spectrum of M on the
quotient by the gauge direction, which is what decides below. This is a
structural statement about the trial space, not a numerical judgement.

**The alt-profile bracket is an artefact — deciding evidence.** The
predecessor's alt scan (profile (r−1)²/r⁵, R=30, Nr=2000) showed one
sign-change bracket at ω² ∈ [−1.525, −1.5], det_min_abs 3.35e-17. At that
location the eigenvalues of M are **[≈6e-11, 0.0157, 0.0696]**: the
bracket is the noise of the identically-zero GAUGE eigenvalue wobbling
through zero; the physical eigenvalues are O(10⁻²), nowhere near zero.
The bracket does not reproduce at Nr=1000 at R ∈ {10, 20, 30} under
either extraction (200-, 2000- and 400-point scans), and a different
spurious bracket ([−0.475, −0.45], one fit at R=10) appears and vanishes
at fine resolution — the signature of noise, not of a mode.

**Deciding quotient read — clean everywhere.** The two physical
eigenvalues of M(ω²) were scanned on ω² ∈ [−5, 0) (2001 points) for
profiles P1=(r−1)²/r⁴ and P2=(r−1)²/r⁵, R ∈ {10, 20, 30}, both
extractions (`p382_finish_eig.json`): **no zero crossing anywhere; the
smallest physical eigenvalue is ≥ 0.00265 (P1) and ≥ 0.000877 (P2),
attained at ω²=0, and is R-independent to 4 digits** (P2: 0.00087671 /
0.00087687 / 0.00087688 at R = 10/20/30). No tachyon in the trial space.

**Single-mode reads (reported, not deciding).** A-component: F is
*exactly* ω-independent (A₄, A₂ = 0 to instrument precision) for P1, P2
and all packets — a non-dynamical direction carrying no dispersion.
B/C components: quartic fits are excellent (held-out residuals ≤3.6e-9),
but their single-entry roots are complex pairs (e.g. B: 0.049+0.107i
averaged vs 0.057+0.156i snapshot) that move 40–100% across extraction
convention, R and profile. A diagonal entry's roots are not eigenvalues
of the coupled system; the coupled physical eigenvalues are real (M is
real symmetric) and never cross zero. The complex pairs are therefore
anatomised as single-entry artefacts of a coupled system, and the R3
"complex root" clause is answered by the coupled read: no complex or
negative frequency exists in the trial space's physical spectrum.

**ω-parity — PASS (anatomised).** The predecessor's raw quartic-in-ω fit
showed odd coefficients at rel 0.57/0.71. That fit included the
discontinuous snapshot point F(0) (see above); on the averaged branch,
quadratic-in-ω² fits predict held-out points to ≤3.6e-9 relative in every
block — F is even in ω, as registered. The raw fit's failure mode is the
instrument's ω=0 convention, not a parity violation.

## 5. Packet / principal-symbol sign check — numeric check FAILED (instrument indicted for this read only); symbol read stands algebraically

Registered expectation: packet roots approach the light cone
(ω²/k² → 1); if not, the instrument is indicted first. Outcome: the
numeric packet read does NOT produce light-cone roots in any component.
A-component packets (k=5,10,20): F exactly ω-independent (residuals
0–2e-16) — no dispersion exists to extract. Follow-up experiment (B/C
components, same packets): B gives A₂/A₄ ≈ −0.170 independent of k; C
gives A₂/A₄/(−2k²) ≈ 0.44 at all k, with complex single-entry roots —
no (ω²−k²)² factorisation in either. Anatomy: a localised
single-component packet is not a polarisation eigenstate of the
fourth-order system, so the zeros of its action are not the PDE
dispersion; the Galerkin packet instrument cannot read the symbol.
Per the registration's own rule, the instrument is indicted for this
read — the theory is not. The short-wavelength read itself is the exact
algebraic principal symbol (background-independent): the (□)² symbol,
whose characteristic cone is the light cone with multiplicity two — no
superluminal characteristics, no short-wavelength tachyon or gradient
sign in any sector (see R5). What would decide the numeric version: a
WKB/plane-wave trial with a full polarisation basis on a locally flat
patch — a formalism build, queued as a follow-up, not a probe fix.

## 6. R5 — Well-posedness of the linearised radial sector (analytic, scoped exactly as registered)

**Operator order and initial-data count.** The linearised Bach equations
are fourth order in time. Each independent dynamical radial field
requires FOUR initial-data sets (h, ∂t h, ∂t²h, ∂t³h) — twice GR's two.
Raw radial count: 3 metric functions × 4 = 12 data functions of r,
reduced by the linearised constraints (the tt/tr components, the
fourth-order analogues of the Hamiltonian/momentum constraints) and by
gauge (radial diffeomorphisms ξ^t, ξ^r; conformal σ). A complete
constraint/gauge reduction count for the Bach system on a Morris–Thorne
background is not in the published literature available to this
programme and is not claimed.

**Characteristics.** The principal symbol of the linearised Bach
operator is background-independent in form: the (□)²-type symbol of the
Weyl action. The characteristic cone is exactly the background LIGHT
CONE with multiplicity two (double root). No superluminal or spacelike
characteristics; the system is not strictly hyperbolic (repeated
characteristic), so standard second-order strong-hyperbolicity theorems
do not apply directly and energy estimates lose derivatives unless the
system is first reduced (e.g. auxiliary linearised-Ricci variables,
converting (□)² into a coupled second-order system).

**Well-posedness.** For the linear constant-coefficient model problem
(□)²u = 0 the Cauchy problem IS well-posed with the four data sets
(solutions by applying □ twice; resonant forcing gives at most
polynomial-in-t growth). On the curved T-b background, no published
well-posedness theorem for the linearised Bach IVP exists. Reported
scoped: symbol-level hyperbolicity on the (double) light cone, data
count doubled vs GR, curved-background well-posedness UNPROVEN — the
obstruction is named; deciding it requires an auxiliary-field or
first-order reduction of the linearised Bach system on this background
plus an energy estimate (a formalism build, not a probe).

**Positive conserved energy.** None exists. The quadratic action S₂ has
Pais–Uhlenbeck structure: its Ostrogradsky Hamiltonian is linear in one
canonical momentum and unbounded below; a conserved energy exists but is
INDEFINITE. Per this item's HARD SCOPE RULE, that indefinite partner is
precisely the (V-b) object, which stands UNDECIDED and is not used as a
deciding classical read in either direction; R5 records the
non-existence of a positive conserved energy as the registered
well-posedness fact. In-scope classical consequence: energy arguments
cannot prove radial stability — the stability read above rests entirely
on the mode/quotient-spectrum scans.

## 7. Failure-protocol ledger

| Failure | Anatomy | Follow-up run | Status / reopening condition |
|---|---|---|---|
| Diffeo gauge direct evaluation: rel 0.657 / 134.5 | Linear path omits S′[δ²g]; S′≠0 for S_W on the matter-held background (§3) | Corrected-path extraction + orbit refinement (Nr 2000→4000) | CLOSED structurally: two independent extractions agree; continuum q2 ~1e-10. Reopen if a future instrument evaluates S₂ along a non-orbit path and claims a gauge failure without the δ²g term. |
| Raw det scans: contradictory signs, brackets at [−1.525,−1.5] and [−0.475,−0.45] | det M ≡ 0 identically (conformal null direction in the common-profile trial space) | Quotient (physical-eigenvalue) scans: 2 profiles × 3 R × 2 extractions × 2001 points | CLOSED structurally: no physical crossing anywhere. Reopen if a trial space WITHOUT a common-profile conformal direction (independent profiles per component, or gauge-fixed) is built — its det would be a genuine read. |
| ω-parity raw fit: odd coeffs rel 0.57/0.71 | Snapshot F(0) vs averaged F(ω>0) convention discontinuity (exact factor 2) | Averaged-branch fits with held-out points | CLOSED: parity holds to ≤3.6e-9 on the averaged branch. |
| Packet light-cone sign check: no light-cone root in A, B or C components | Single-component localised packets are not symbol polarisation eigenstates; A component is exactly ω-independent | B/C packet follow-up (this memo §5) — also failed to factorise, confirming the instrument-level cause | OPEN as a numeric read; the symbol statement rests on exact algebra. Reopening/deciding step: WKB plane-wave trials with full polarisation basis on a locally flat patch (formalism build). |
| Single-mode B/C complex ω² pairs | Diagonal-entry roots of a coupled system; not eigenvalues; values not robust (40–100% drift) | Coupled quotient spectrum (§4) | CLOSED as deciding evidence: physical eigenvalues real, bounded away from zero. Reopen if an exact (non-Galerkin) radial spectrum is ever computed and shows a complex frequency. |

## 8. Verdict restated

**CLASSICALLY STABLE** in the computable sectors named in the header:
exact static ℓ=0; dynamic ℓ=0 Galerkin trial space (physical quotient
spectrum tachyon-free on ω²∈[−5,0) across profiles, radii and extraction
conventions); principal-symbol sector in all ℓ (algebraic). Caveats that
travel with the verdict: Galerkin ≠ exact spectrum; no positive
conserved energy exists (R5), so no energy-based proof is possible;
linearised curved-background IVP well-posedness unproven; ℓ≥1
long-wavelength modes untested. **(V-b) UNDECIDED, attached unchanged.**
The conformal throat remains a **scan signal under attack** — nothing
stronger.

Files: `p382_static.json` (R1/R2), `p382_gauge_orbit.json`,
`p382_gauge_anatomy.json`, `p382_finish_dyn.json`, `p382_finish_eig.json`,
`p382_finish_packets_bc.json`, `p382_checker.json`, `p382_results.json`;
scripts and logs in `work/p382_finish_*.py/.log`, R5 draft in
`work/p382_r5_draft.md`.
