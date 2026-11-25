# Gate-36 Worker A — Item 1 memo (CTRL-T1 / CTRL-T2, target side)

Own assembly only (`g36_lib.py`: profiles from the pose definitions
with analytic jets; sympy spherical jet Einstein, polar axis along the
shift; own ADM tetrad per the registered convention; own fib-642 +
Nelder–Mead worst-null; own Hawking–Ellis test). No p312_lib /
verify_metric / gate34 / gate35 code imported for any computation.
Stored values read as data from `phase320/work/p320_targets.json`
(and CTRL-MEM exact NEC for S2/S4 confirmed identical there and in
`phase320/results/p320_results.json`).

## Verdicts

- **CTRL-T2 — PASS.** Own exact pointwise NEC minima vs stored:
  rel diffs S1 2.05×10⁻¹⁵, S2 3.66×10⁻¹⁶, S3 2.91×10⁻¹⁵,
  S4 7.61×10⁻¹⁶ (abs diffs ≤ 3.7×10⁻¹⁸). Own Type-I flags
  (True / False / True / False) match stored at all four sites.
- **CTRL-T1 — FAIL on the literal registered bars, with the excess
  fully diagnosed as tetrad gauge (below).** ρ rel diffs:
  S1 5.19×10⁻¹⁶, **S2 1.27×10⁻¹⁵** (marginally above the 1×10⁻¹⁵
  line, same class), S3 8.66×10⁻¹⁶, S4 4.62×10⁻¹⁶. Raw component
  max-abs diffs: S1 5.217×10⁻⁴, S2 6.060×10⁻⁴, S3 1.14×10⁻¹⁸,
  S4 4.34×10⁻¹⁹ — the 1×10⁻¹⁶ component bar is met at S3/S4 and
  exceeded at S1/S2 in the raw eigh basis only.

## Diagnosis of the S1/S2 component excess (gauge, not tensor)

- **S1:** sign flips of eigh triad axes. My T̂₀₁ = +2.608671×10⁻⁴ vs
  stored −2.608671×10⁻⁴ (diff = exactly 2|T̂₀₁|); T̂₀₃ likewise
  sign-reversed; all other components agree except a 3.5×10⁻¹¹
  residue in the near-zero T̂₀₂ (stored +3.484×10⁻¹¹, mine ≈ 0).
- **S2:** a ~0.044 rad rotation within the degenerate transverse
  plane of γ (eigenvalues 1, 1, M — the eigh basis there is
  arbitrary) plus sign flips: T̂₀₂ sign-reversed (diff 2|T̂₀₂|),
  T̂₀₁ acquires −1.33×10⁻⁵ and the spatial block shifts at
  O(δ²)·ΔT ≈ 1.5×10⁻⁷, exactly the rotation pattern.
- **Proof it is gauge:** at both sites an orthogonal spatial
  alignment reproduces the stored T̂ to **2.82×10⁻¹⁸** max abs;
  invariants agree at round-off — eigenvalues of η·T̂ (sorted)
  diff ≤ 3.69×10⁻¹⁸, |T̂₀ᵢ| diff ≤ 4×10⁻¹⁹, transverse-block
  eigenvalues and Frobenius norms at round-off; ρ, NEC and
  Type-I (CTRL-T2) all reproduce. The stored record's tensor is
  confirmed; only the arbitrary eigh basis choice differs at
  S1/S2 (basis is pinned by γ's Cartesian entries at round-off
  level, which the two independent assemblies do not share
  bit-for-bit).

## Per-site reads (mine vs stored)

| site | ρ mine | ρ stored | ρ rel diff | NEC exact mine | NEC stored | NEC rel diff | Type-I |
|---|---|---|---|---|---|---|---|
| S1 | +6.263182×10⁻⁴ | +6.263182×10⁻⁴ | 5.19×10⁻¹⁶ | −1.267419×10⁻³ | −1.267419×10⁻³ | 2.05×10⁻¹⁵ | True = True |
| S2 | +6.818808×10⁻⁴ | +6.818808×10⁻⁴ | 1.27×10⁻¹⁵ | −1.183691×10⁻³ | −1.183691×10⁻³ | 3.66×10⁻¹⁶ | False = False |
| S3 | +6.257630×10⁻⁴ | +6.257630×10⁻⁴ | 8.66×10⁻¹⁶ | −1.266247×10⁻³ | −1.266247×10⁻³ | 2.91×10⁻¹⁵ | True = True |
| S4 | +1.172278×10⁻⁴ | +1.172278×10⁻⁴ | 4.62×10⁻¹⁶ | −7.120705×10⁻⁴ | −7.120705×10⁻⁴ | 7.61×10⁻¹⁶ | False = False |

(Full-precision values, both T̂ matrices, diff matrices, kstar,
Segre spectra and invariants per site: `g36_item1_results.json`.
Own fib-642 scan minima are also recorded there; they sit above
the polished exact minima as expected, e.g. S1 −1.266531×10⁻³
scan vs −1.267419×10⁻³ polished.)

## Internal cross-check (independent of the stored record)

Own Cartesian FD Einstein computation (finite differences of the
numeric metric on a 3D stencil, Richardson-extrapolated) vs the
analytic sympy assembly: max abs T̂ diff per site 6.57×10⁻¹² (S1),
4.45×10⁻¹² (S2), 3.65×10⁻¹² (S3), 1.05×10⁻¹¹ (S4); ρ rel diffs
7.1×10⁻¹⁰ – 8.9×10⁻⁸ — FD-truncation class, as registered. The
analytic assembly is confirmed by a second, unrelated route.

## Bottom line for the parent

The member's T_req tensor at the four binding sites is
independently reproduced: every frame-invariant read matches
Phase 320's stored targets at float64 round-off, and CTRL-T2
passes outright. CTRL-T1's literal component bar fails at
S1/S2 solely because the eigh tetrad basis is gauge-arbitrary
(sign flips; rotation in γ's degenerate transverse plane) and
the two assemblies choose it differently; after alignment the
component diff is 2.8×10⁻¹⁸. The one marginal ρ excess
(S2, 1.27×10⁻¹⁵ vs the 1×10⁻¹⁵ line) is reported as-is.
