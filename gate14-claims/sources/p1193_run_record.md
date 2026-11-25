# P119-3 — Run Record: the separable-minimum price reference for the Xun–Ren Hamiltonian

Item: FU-P1085-3 (Phase 119 registration §P119-3). Bookkeeping completion
in P72-2's exact form. C12: this item re-reads no R_net and makes no
claim about the Phase 108 reopening; it completes the price line only.
INTERNAL only.

## 1. The Hamiltonian (from the paper)

Xun & Ren, arXiv:2410.04919, Eqs. (1)–(2), h = 1 throughout, r = k/h:

    H  = Σᵢ Hᵢ + V,
    Hᵢ = h σᵢᶻ + N h²/D,        V = 2k Πᵢ σᵢˣ + 4k²/D,
    D  = √(N²h² + 4k²).

Summing the printed constants: N·(Nh²/D) + 4k²/D = (N²h² + 4k²)/D = D, so

    H = h Σᵢ σᵢᶻ + 2k Πᵢ σᵢˣ + D,

and the printed constants make the ground energy E_ground = 0
(verified on the dense construction in the evaluation: smallest
eigenvalue 0 to ≤1e-12 at the dense-check points; the separable
candidate energies below are all > 0, consistent).

H depends on (N, r) only; m enters only through E_in / E_out.

## 2. Product-state expectation (derived here, not assumed)

For a fully product state ⊗ᵢ|ψᵢ⟩ with single-qubit Bloch vectors
(xᵢ, yᵢ, zᵢ), xᵢ² + yᵢ² + zᵢ² = 1, factorisation of the expectation of
the single N-body term gives, directly from §1:

    ⟨H⟩ = h Σᵢ zᵢ + 2k Πᵢ xᵢ + D.                                    (★)

(This was verified numerically against a dense Kronecker construction
of H: max |formula − dense| over 200 random product states at
(N,k) = (2,0.5), (3,1), (5,0.5) is reported in the results file,
`dense_checks`.)

## 3. Analytic reduction (certificate 1)

Minimise (★) over the product Bloch manifold, h, k > 0.

Step 1 (kill y, fix the z sign). For fixed xᵢ, ⟨H⟩ is linear in zᵢ with
coefficient h > 0, and zᵢ ≥ −√(1−xᵢ²) with equality iff yᵢ = 0 and
zᵢ = −√(1−xᵢ²). So a minimiser has yᵢ = 0, zᵢ = −√(1−xᵢ²) for all i.

Step 2 (fix the product sign). √(1−xᵢ²) is even in xᵢ, so flipping the
sign of any single xᵢ flips the sign of Πxᵢ at no other cost. A
minimiser therefore has Πxᵢ = −Π|xᵢ| ≤ 0. Writing aᵢ = |xᵢ| = sin θᵢ,
θᵢ ∈ [0, π/2]:

    E(θ) = −h Σᵢ cos θᵢ − 2k Πᵢ sin θᵢ + D.                          (†)

Step 3 (structure of the optimum). The domain is compact, so a global
minimum of (†) exists. At any minimiser:
- No θⱼ = π/2: ∂E/∂θⱼ at θⱼ = π/2 (from the left) equals
  h·sin θⱼ − 2k cos θⱼ·Π_{i≠j} sin θᵢ = h > 0, so decreasing θⱼ
  strictly decreases E — contradiction.
- No θⱼ = 0 unless all are 0: if exactly one θⱼ = 0 and the rest lie
  in (0, π/2), then ∂E/∂θⱼ at 0⁺ = −2k Π_{i≠j} sin θᵢ < 0, so
  increasing θⱼ strictly decreases E — contradiction. If ≥ 2 of the
  θ's are 0 and some θᵢ > 0, stationarity in θᵢ reads
  h sin θᵢ = 2k cos θᵢ·Π_{l≠i} sin θ_l = 0 (the product contains a
  zero factor), forcing sin θᵢ = 0 — contradiction.
- Otherwise all θⱼ ∈ (0, π/2), and stationarity in θⱼ gives
  h sin θⱼ = 2k cos θⱼ Π_{i≠j} sin θᵢ, i.e.

      sin²θⱼ / cos θⱼ = 2k Πᵢ sin θᵢ / h   — the same for every j.

  φ(θ) = sin²θ/cos θ is strictly increasing on (0, π/2)
  (φ′(θ) = sin θ (2cos²θ + sin²θ)/cos²θ > 0), so all θⱼ are equal:
  any interior minimiser is symmetric, θⱼ = θ, with

      h = 2k sin^{N−2}θ · cos θ        (N ≥ 3;  h = 2k cos θ for N = 2).   (‡)

Conclusion: the global minimum of (†) — hence E_sep — is the smaller
of (a) the corner value at θ = 0, E = D − Nh (the product state
|1⟩^{⊗N}: every zᵢ = −1, every xᵢ = 0), and (b) the values of the
symmetric function g(θ) = −Nh cos θ − 2k sin^N θ + D at its interior
critical points (‡). The evaluation enumerates the roots of (‡) on a
50001-point grid with Brent refinement and compares all candidates.
(For N = 2 this reproduces the closed form min at cos θ = h/(2k) when
2k ≥ h, giving E_sep = D − 2k − h²/(2k), and the corner when 2k = h.)

## 4. Numerical certificate (certificate 2)

Independent of the reduction: multi-start local optimisation
(L-BFGS-B, analytic gradient) over the full product Bloch manifold
((θⱼ, φⱼ) per qubit, 220 starts per row, ≥ 200 as registered), plus a
random sweep of 110000 (≥ 10⁵) uniformly random product states per
row. The certificate passes for a row iff neither finds a value lower
than the analytic E_sep by > 1e-9. Per-row numbers are in
`p1193_results.json` (`numeric`).

## 5. Control (run before any registered row was believed)

The same machinery at N = 2 must reproduce P72-2's stored
E_prep^(sep) (`phase72/results/p722_results.json`) to ≤ 1e-9:
0.2360679774997898 / 0.3284271247461903 / 0.2221359549995796 at
r = 0.5 / 1 / 2. Result: see §7 of the memo / results file `control`.
(At r = 0.5 the corner and the critical point coincide, cos θ = h/2k
= 1; at r = 1, 2 the symmetric interior critical point carries the
minimum — the machinery exercises both branches of §3 at the control.)

## 6. Price definitions (P72-2 §3 verbatim in form)

E_prep^(sep) = E_sep − E_ground = E_sep. E_prep^(marg) = 4k²/D as
stored by Phase 108. Price per unit delivered at reference X:
Π_X = (E_prep^(X) + E_in)/E_out, with E_in, E_out Phase 108's STORED
values from `phase108/results/p1085_results.json` (quoted per row in
the results file; not recomputed). Classical leg ≥ 0 omitted — all
prices are lower bounds, as inherited. Deciding total (P72-2): the
resource at min(sep, marg).

Registered rows: (N,m,r) = (5,1,0.5), (6,1,0.5), (6,1,1), (8,1,0.5),
(8,1,1), (10,1,0.5), (10,1,1), (10,1,2) — the E_net,B < 0 rows of
P108-5 — plus the N = 2 control.

Verdict thresholds (registered): PRICE LINE MOVES iff the
deciding-total price per unit at some deciding row falls to ≤ 1, or
Π_marg/Π_sep ≥ 2 at some deciding row; otherwise PRICE LINE STANDS.
A minimum supported by only one certificate is flagged and does not
carry the verdict.

## 7. Numbers

See `p1193_results.json` and the memo. float64 throughout;
programme venv `~/workspace/warp-pilot/venv/bin/python`.
Scripts: `work/p1193_eval.py`; independent checker
`work/p1193_checker.py` (dense-H tensor expectations, its own
sampling/optimisation, ratio recomputation).
