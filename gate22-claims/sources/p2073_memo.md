# P207-3 — MODE-SUM C1b FAILURE ANATOMY — MEMO

Item 3 of Phase 207, per `phase207/REGISTRATION207.md` item 3.
Sources: `phase200/kaggle/p2003_results.json`,
`phase200/kaggle/p2003_laptop_run.log`,
`phase200/kaggle/p2003_modesum_kernel.py` (line numbers below are
that file as written), `phase200/results/p2003_memo.md`.
Fence honoured: the production run was NOT rerun; the production
reads are VOID until C1b passes and none is quoted here as a supply
read. All new computation is bounded diagnostics (selected ℓ,
selected channels, one h) in `phase207/work/p2073_diag.py`;
arithmetic claims are recomputed by `phase207/work/p2073_check.py`
(all 19 checks pass; `phase207/results/p2073_verify.json`).

## Verdict (registered form 2)

**ANATOMY NAMED, NO REPAIR YET** — the failure is (c) kernel
defects, in both subtractions, with (a) and (b) excluded as primary
causes by the numbers below. No repair is packaged: the two
deciding defects (D-A, D-B) are defects of the subtraction *scheme
as coded*, and no line-level correction follows from their
mechanism — the coded counterterms must be replaced by objects the
source does not contain (true WKB mode functions for A; a
locally matched reference plus an explicit finite local term for
B). Two subsidiary defects (D-App, D-kmax) do have mechanical
corrections, but fixing them alone cannot pass C1b — proved below
by the App cancellation in NEC_φ — so packaging them as "the
repair" would misstate the anatomy. The deciding experiment is
specified exactly at the end.

## The failure, priced (checker-recomputed from the harvested JSON)

THA targets: NEC_ρ = 3.3505682421407874e-5, NEC_φ =
1.440744344120542e-4, both positive; tol 0.25 relative + sign.

| sub | channel | h=0.05 | h=0.025 | h-ratio | \|h=0.025\|/target |
|---|---|---|---|---|---|
| A | NEC_ρ | −17483858.83 | −53838734.86 | ×3.079 | 1.61e12 |
| A | NEC_φ | −135396362.01 | −134668740.17 | ×0.995 | 9.35e11 |
| B | NEC_ρ | −1718.25 | −1645.83 | ×0.958 | 4.91e7 |
| B | NEC_φ | −1562.70 | −1365.75 | ×0.874 | 9.48e6 |

Every read is negative (sign agreement fails everywhere) and
5e6–1e12 times the target in magnitude. C1a/C2 pass (harvested
JSON; C2 is, per kernel lines 349–370, an algebraic identity
between two identical sums, so its pass carries no information
about the mode-sum machinery).

## (b) h-resolution failure — EXCLUDED as primary

B moves only 4.2% (NEC_ρ) and 12.6% (NEC_φ) under h halving while
sitting 4.9e7× / 9.5e6× off target; A NEC_φ moves 0.54% while
9.3e11× off target. A resolution failure shrinks with h; these do
not. The one genuinely h-sensitive read, A NEC_ρ (×3.08), is
explained by defect D-App below, whose error scales as h⁻² —
finer h makes it *worse*, the opposite of a resolution failure.

## (a) tail-fit non-convergence — NOT primary; the sequence itself is defective

The harvested JSON logs only the extrapolated values (no per-ℓ
sequence, no fit residuals), so (a) cannot be decided from the
harvest alone. The diagnostic per-ℓ increments (mr₀=2, ξ=1/6,
h=0.05, L=12, ω_max=30; full table in `p2073_results.json`) decide
it: for subtraction A the renormalised per-ℓ increments *grow*
with ℓ instead of decaying — D-channel increment magnitudes
0.0013, 0.226, 9.43, 467, 1.89e4, 1.27e5, 4.26e5, 1.99e6, 5.44e6
at ℓ = 1, 2, 4, 8, 16, 24, 32, 48, 64 (checker-verified monotone
growth ℓ≥8). A fit of S∞ + a₁/ℓ + a₂/ℓ² (kernel lines 325–335)
to cumulative sums of growing increments is not "unconverged at
ℓ≤64"; the underlying sequence is divergent by construction
(D-A). For B the renormalised B-channel increments likewise grow
through ℓ=24 (below, D-B), then the kernel's own truncation
zeroes ℓ≥32 — the fit converges, to a wrong value set by the
scheme. Fit form is not the deciding failure in either case.

## (c) Kernel defects

### D-A (DECIDING, subtraction A): the adiabatic counterterm is a spectral mean applied pointwise, with its 1/ω² expansion used in the forbidden region — lines 300–309

The bare sums use the pointwise throat value R²(j₀) with weight
w = (2ℓ+1)/(4π)/(2ω) (line 293). The counterterm (lines 303–304)
instead uses amp = w/(2L r₀²), i.e. the *box-averaged* mode
density 1/(2L) at the throat, times
corr = 1 − V_t/(2ω²) + 3V_t²/(8ω⁴) (line 305), summed over every
box mode. Two separable failures, both measured:

1. **Pointwise vs mean.** At ℓ=0 the coded pointwise factors
   U_n(j₀)²·2L for the first ten modes are [0.304, ~1e-26, 1.117,
   ~1e-25, 1.905, ~1e-26, 2.274, ~1e-27, 2.347, ~1e-27]: alternate
   modes have a node at the throat (bare throat contribution
   exactly ~0) while the counterterm subtracts the full mean from
   every mode. Per-mode cancellation therefore does not occur;
   only an imperfect pairwise cancellation of large terms remains.
2. **Forbidden region.** corr is an expansion in V_t/ω², valid
   only for ω² ≫ V_t. The fraction of modes with ω² < V_t is
   0.26 at ℓ=8, 0.52 at ℓ=16, 0.80 at ℓ=24 and 1.00 at ℓ≥32;
   corr_max grows 77 (ℓ=8), 5.3e2 (16), 1.3e3 (24), 2.0e3 (32),
   3.2e3 (48), 4.0e3 (64). Simultaneously the bare throat
   contributions collapse by tunnelling suppression (B-channel
   bare: 0.0057 at ℓ=32, 1.8e-26 at ℓ=48, 1.6e-50 at ℓ=64) while
   the counterterm *grows* (B-channel CT: 1.11e4, 4.21e4, 1.04e5;
   D-channel CT: 4.26e5, 1.99e6, 5.44e6 at the same ℓ). The
   renormalised per-ℓ increments are thus ≈ −CT for ℓ≥32,
   negative and growing — summing them over ℓ reproduces the
   harvested A scale (−1e7…−1e8) and sign. This is "the scheme
   as coded cannot reproduce THA at any cutoff": raising ℓ_max
   or ω_max adds more forbidden-region counterterm, not less
   error. Already at low ℓ the C channel is mis-subtracted
   (renA C increments −1.26, −3.63, −5.61, −7.96 at ℓ=0,1,2,4
   against bare C of 4.07, 12.12, 19.89, 34.12), because the
   C counterterm kr²·amp·corr (line 308) is not the derivative
   of the A counterterm's mode function.

### D-App (subtraction A only): A″(0) is differenced after pointwise-only subtraction — lines 306–311

The A counterterm is subtracted only at the single grid point
j₀ (lines 306–309 modify A[j0], B[j0], C[j0], D[j0] only);
A[j₀±1] remain bare. Line 311 then forms
App = (A[j₀+1] − 2A[j₀] + A[j₀−1])/h², injecting a spurious
+2·CT_A/h² spike. Measured at ℓ_max=4 (diagnostic): CT_A total
= 1.5538, App as coded = 1242.68, App of the bare arrays =
−0.340, difference = 1243.02 = 2·CT_A/h² exactly (ratio
1.0000000000000002, checker-verified). This term enters ρ with
coefficient −ξ (line 315) and hence NEC_ρ, scaling as h⁻² —
the mechanism behind A NEC_ρ's ×3.08 worsening when h halved.
Separability proof: in NEC_φ = ρ + p_θ the App terms cancel
identically (−ξ·App at line 315, +ξ·App at line 319), so D-App
contributes *nothing* to A NEC_φ = −1.35e8; that read's failure
is entirely D-A. Hence no repair of D-App alone can pass C1b.

### D-B (DECIDING, subtraction B): reference not locally matched, spectra truncated against each other, promised finite local term never added — lines 202–205, 227–232, 250–265, 282–285

1. **Reference mismatch.** The reference potential (line 205)
   is V_ref = ℓ(ℓ+1)/r₀² + m²: it omits the (1−2ξ)r₀²/a² term
   of the bare potential (line 208) and freezes a = r₀², so the
   reference geometry (R = +2/r₀², per the radial_modes
   docstring at lines 197–198) is not the throat-local geometry
   (R = −2r₀²/a²). Mode-by-mode subtraction by eigenvalue order
   then leaves per-ℓ residuals that *grow* with ℓ: renormalised
   B-channel increments +0.0087, −0.0226, −0.197, −0.518,
   −3.195, −13.68, −40.14 at ℓ = 0,1,2,4,8,16,24
   (checker-verified monotone growth in magnitude). The
   cumulative wrong scale (~−1e3 after tail fit) matches the
   harvested B reads; the h-stability (4–13%) matches a
   scheme-level, not numerical, residual.
2. **Mutual truncation.** Lines 227–232 truncate the bare
   spectrum to min(len(ω), len(ω_ref)). Reference mode counts
   fall 230, 230, 229, 228, 221, 192, 133 at ℓ = 0…24 and to
   **0 at ℓ≥32** (V_ref ≥ 1064 > ω_max², while bare edge-localised
   modes persist), so for ℓ≥32 subtraction B silently discards
   the entire bare contribution, and at ℓ=24 it discards 42% of
   the bare spectrum — preferentially the high-ω modes whose
   subtraction matters most. (In the diagnostic table the ℓ≥32
   renB rows are bare-minus-empty-reference before this
   truncation; their magnitudes are ≤0.006 and immaterial.)
3. **Missing finite local counterterm.** The header (lines
   43–49) and the comment at lines 261–265 promise "the analytic
   finite local counterterm difference … added at throat level
   in throat_channels()". It is added nowhere: the word "local"
   occurs only at lines 43, 49 (header), 261, 264 (the comment
   itself) and 352 (C2 docstring), and the B branch of
   throat_channels (lines 282–285) adds only the channel arrays.
   For the production field the comment's vanishing argument
   ((1/6−ξ)R + m² = 0) holds, but for the C1b control m² = 4 ≠ 0,
   so the term is nonzero for exactly the control that judges B.
   Its absence is a real defect but is *not* size-deciding: no
   local term of THA scale (~1e-4) can account for a −1.7e3
   residual; D-B.1/D-B.2 are the deciding parts.

### D-kmax (both subtractions): the ω_max selection silently truncates at ω≈27.4–28.0 — lines 211–215

kmax is estimated from the *continuum* dispersion
(πn/(2L))² + min(V) ≤ ω_max² (lines 211–212), but the discrete
Laplacian's eigenvalues lie below the continuum values at large
n, so the estimate undercounts. Measured at h=0.05: the formula
keeps 230 modes with headroom 0 and max ω kept 27.418 (ℓ=0) /
28.031 (ℓ=16), while a direct lowest-320 eigensolve finds 258
(ℓ=0) and 251 (ℓ=16) eigenvalues ≤ ω_max² = 900
(checker-re-derived). Modes with 27.4 < ω ≤ 30 are never
computed, for either spectrum. This is a genuine defect with a
mechanical correction (select by value, or assert headroom > 0),
but it is not size-deciding: it removes ~10% of modes near the
top of the spectrum from bare and counterterm alike, and cannot
produce sign-flipped residuals 7–12 orders above target.

## Conclusion of the anatomy

(c), combinations separated: **D-A decides subtraction A's
failure** (with D-App a separable h⁻² contaminant of A NEC_ρ
only), **D-B.1+D-B.2 decide subtraction B's failure** (D-B.3 a
real but non-deciding omission), **D-kmax is a real but
non-deciding truncation** shared by both. (a) is excluded as
primary because the per-ℓ sequences are divergent/mis-set by
construction before any fit; (b) is excluded as primary because
the residuals are h-stable at 1e7–1e12× target, and the single
h-sensitive read is fully accounted for by D-App's h⁻² spike.
The subtraction scheme *as coded* cannot reproduce THA at any
cutoff — this is not an unconverged-but-right scheme.

## Deciding experiment (exactly specified; NOT run here)

Precondition (both variants): fix D-kmax by selecting eigenvalues
by value (eigh_tridiagonal select="v", range (0, ω_max²)) and
assert kept-count headroom; verify counts 258 (ℓ=0) and 251
(ℓ=16) at h=0.05, L=12, ω_max=30, mr₀=2. Log, per ℓ, the bare,
counterterm/reference and renormalised A, B, C, D throat
increments and the cumulative NEC_ρ/NEC_φ — the fields whose
absence from the harvested JSON forced this diagnostic route.

- **E-A (separates D-A.1 from D-A.2):** diagnostic (non-production)
  run at mr₀=2, ξ=1/6, h=0.05, L=12, ω_max=30, ℓ_max ∈ {8,16,24,32},
  three A-counterterm variants: V0 = as coded; V1 = as coded but
  corr summed only over modes with ω² > V_t, with the counterterm
  applied as a grid array (local V_t(l)) before differencing
  (also fixes D-App); V2 = pointwise WKB mode-function
  counterterm (amplitude from the local (ω²−V_t(l))^(−1/4) WKB
  mode, formula to be written into the next registration before
  the run). Separating outcome: if V1's per-ℓ renormalised
  increments decay with ℓ and its cumulative NECs land within a
  factor of a few of THA, D-A.2 (forbidden region) was deciding
  and V1 is the repair basis; if V1 still leaves O(1–10)
  non-decaying low-ℓ increments (the D-A.1 signature already
  visible in the C channel at ℓ≤4), only V2-class subtraction
  can repair A, and V2's increments are then the gate.
- **E-B (tests D-B):** same grid/cutoffs, ℓ_max ∈ {8,16,24,32},
  reference variant with locally matched potential
  V_ref = ℓ(ℓ+1)/r₀² + m² + (1−2ξ)/r₀², both spectra taken to
  ω_max by value with no min-length truncation (pairing by box
  quantum number), plus the finite local counterterm difference
  written explicitly into the next registration (formula and
  coefficients stated in advance — the current header promises
  it without giving it). Separating outcome: if the per-ℓ
  renormalised increments now decay with ℓ, D-B.1/D-B.2 were
  deciding; any remaining ℓ-independent offset at THA scale is
  then attributable to the finite local term and priced against
  it. If increments still grow, subtraction B's reference class
  itself is wrong and must be replaced, not patched.

Gate for any subsequent repair packaging: per-ℓ renormalised
increments decaying in both subtractions AND cumulative NECs
within a factor of a few of THA at ℓ_max=32 in E-A/E-B, before
any production-cutoff C1b rerun is proposed. Production remains
VOID until C1b passes.

## Files

- This memo: `phase207/results/p2073_memo.md`
- Diagnostic numbers: `phase207/results/p2073_results.json`
- Checker output: `phase207/results/p2073_verify.json` (19/19 pass)
- Diagnostic script: `phase207/work/p2073_diag.py`
- Checker script: `phase207/work/p2073_check.py`
- Repaired kernel: NONE (verdict form 2 — no repair packaged,
  for the reasons stated in the verdict paragraph)
