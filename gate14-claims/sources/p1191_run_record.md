# P119-1 — Run record (definitions + machinery route + τ-convention ruling)

Written after the fresh machinery was built and the controls run, and
BEFORE `phase108/results/p1085_results.json` was opened for comparison.
Phase 108's code (`p1085_eval.py`, `p1085_secondpath.py`) was not read,
imported, or adapted at any point. Sources used: Xun & Ren,
arXiv:2410.04919 full text (HTML); P72-2 run record §§3–4 and
`p722_results.json`; `phase108/work/p1085_definitions.md` (inherited
verbatim); CHECKPOINT119 §P119-1.

## Definitions (inherited, fixed)

- Model: Xun & Ren N-qubit QET. h = 1, r = k/h ∈ {0.5, 1, 2},
  D = √(N²h² + 4k²). Hamiltonian Eqs. (1)–(2):
  H = Σᵢ Hᵢ + V, Hᵢ = hσᵢᶻ + Nh²/D, V = 2k Πᵢσᵢˣ + 4k²/D.
  Ground state Eq. (3): |g⟩ = (1/√2)[√(1−Nh/D)|0…0⟩ − √(1+Nh/D)|1…1⟩].
- Protocol: projective measurements Eq. (4), P_j(α_j) = (1+α_jσ_jˣ)/2,
  on the N−m input qubits (qubits 1…N−m); conditional unitary Eq. (7),
  U(α) = cosθ − iα sinθ σ^y_{first output} Π_{rest} σˣ, α = Πⱼα_j, with
  the optimal θ of Eq. (10). Sector (per the inherited definitions,
  paper App. pattern): the output qubits' Hᵢ plus V entire.
- E_in: Eq. (6), E_in = (N−m)Nh²/D. E_out: Eq. (11) closed form.
  E_prep^(marg) = 4k²/D (recomputed three ways, below).
  E_net,B = E_prep^(marg) − E_out. R = |E_net,B|·τ / (3/(32π²)) when
  E_net,B < 0, else R = 0 (ħ = 1 in model units).
- S(t) = post-protocol sector energy ⟨S_op⟩(t) under H-evolution.
  τ₀ = first t > 0 with S(t) = 0 (P72-2's literal τ_pulse);
  τ_marg = first t > 0 with S(t) = +E_prep^(marg). Non-return is
  reported for t ≤ 30. Price per unit = (E_prep^(marg) + E_in)/E_out,
  classical leg ≥ 0 omitted (lower bound, as inherited).
- Rows: all 30 — (N,m) ∈ {(2,1),(3,1),(3,2),(4,1),(4,2),(4,3),(5,1),
  (6,1),(8,1),(10,1)} × r ∈ {0.5,1,2}. float64 everywhere.

## Machinery route (fresh, from the paper)

- `work/p1191_eval.py`: dense Kronecker construction of H, Hᵢ, V and
  the sector operator (real symmetric — only σᶻ and Πσˣ appear — built
  in float64). Ground state by full eigendecomposition AND by Eq. (3).
  Protocol simulated explicitly: every outcome α ∈ {±1}^{N−m}, the
  Eq. (4) projectors and the Eq. (7) conditional unitary applied to
  |g⟩ as operators (dense matrices in the first implementation;
  the identical operators applied axis-wise on the state tensor in
  the final one — the two agree digit-for-digit on re-run rows).
  E_out(sim) = −⟨S_op⟩ of the post-protocol mixture, cross-checked
  against Eq. (11); E_in(sim) = total ⟨H⟩ of the post-measurement
  mixture, cross-checked against Eq. (6); E_prep^(marg) computed
  (i) as 4k²/D, (ii) as Tr[ρ_marg S_op] with ρ_marg the dense product
  of |g⟩'s single-qubit marginals. S(t) by exact exponentiation:
  components rotated into H's eigenbasis, S(t) assembled as a
  frequency-grouped trigonometric sum (eigenvalue differences
  rounded to 1e-8 for grouping), roots by sign-change scan at
  Δt = 0.002 plus Brent refinement (xtol/rtol 1e-13). Observed
  root accuracy vs the independent derived path: ≤ 3.3e-10.
- `work/p1191_lean10.py` (N = 10 rows only, used because the full-eigh
  route repeatedly exceeded the runtime window under machine
  contention — load average ≈ 38 on 1.5 CPUs): same dense H and same
  explicit protocol simulation for every energy read; ground state
  by sparse Lanczos eigendecomposition of the constructed H; S(t)
  by the derived pair-block exponentiation below. Its (10,1,0.5) and
  (10,1,1) τ reads were checked against the full dense-eigh reads
  obtained for those rows (agreement ≤ 1.2e-10) before its (10,1,2)
  read was believed.
- `work/p1191_asymptotics.py`: derived evolution for m = 1, any N.
  H couples only complementary basis pairs {s, s̄}: in each pair
  H = D·I + [[d, 2k],[2k, −d]], d = h(N−2|s|), Ω = √(d²+4k²), and the
  sector operator has the same pair-block form, so each pair's
  contribution to S(t) is q₀ + q_c cos(2Ωt) + q_s sin(2Ωt) exactly.
  Applying Eq. (4) to Eq. (3) gives pre-unitary amplitudes
  A₀(x) = a′χ_x, A₁(x) = −b′χ_{¬x} (x = input-bit config,
  χ_x(α) = Π_{j∈x}α_j, a′ = a·2^{−(N−1)}, b′ = b·2^{−(N−1)}), and the
  Eq. (7) unitary (α_tot = χ_full) collapses them to
  B₀(x) = uχ_x, B₁(x) = vχ_{¬x} with u = a′cosθ + b′sinθ,
  v = a′sinθ − b′cosθ, independent of x. Summing S(t) over all α
  kills the χ_xχ_{¬x} cross terms (Σ_α χ_full = 0) and leaves an
  O(N) binomial-weighted sum over w = |x|. Validation against the
  dense machinery: |S(0) + E_out| ≤ 3.4e-16 at N ∈ {3,5,8,10};
  τ₀/τ_marg agree with the dense reads to ≤ 1.2e-10 at every
  compared row, and at (2,1,0.5) the derived τ₀ = 0.23272281410034895
  reproduces P72-2's stored τ_pulse to 5e-17.

## Controls (registered; all must pass before deciding rows believed)

- C1 (N=2 vs P72-2 stored): E_out, E_prep^(marg), E_net,B agree with
  `p722_results.json` at all three r with relative difference 0.0
  (bit-exact at printed precision); τ₀ agrees to ≤ 1.2e-10 absolute
  (bar: ≤ 1e-9 rel energies, ≤ 1e-6 abs τ). PASS.
- C2: ground eigenvalue of the constructed H: max |E_ground| =
  2.7e-15 over all 30 rows (bar ≤ 1e-12); overlap of the eigenvector
  with Eq. (3): min = 1 − 7e-16 (bar ≥ 1 − 1e-10). PASS.
- C3: τ_marg at (2,1,0.5) = 0.8385330500198818 (dense) vs the
  registered 0.838533050344258: difference 3.2e-10 (bar ≤ 1e-6).
  PASS. (Derived path: 0.8385330503442567, difference 1.3e-15.)
- Internal cross-checks (all rows): max |E_out − E_out(sim)| =
  6.7e-16; max |E_in − E_in(sim)| = 3.6e-15; max |4k²/D −
  Tr[ρ_marg S_op]| = 1.3e-15; outcome probabilities sum to 1.

## τ-convention ruling

**Ruling: τ_marg.** Argument (from P72-2 §4's text):
1. §4's FR-net read is "the same read WITH the resource on the books":
   the Ford–Roman bound "is referenced to the uncorrelated vacuum, so
   Bob-sector energy is read relative to the uncorrelated reference
   (R-marg), not relative to the entangled ground."
2. The pulse whose magnitude the ratio prices is therefore the
   excursion below the uncorrelated-reference level: it begins at
   S(0) = −E_out and ends when S(t) returns to that level,
   +E_prep^(marg) — that duration is τ_marg by definition.
3. τ₀ (return to the entangled-ground zero) is §4's τ_pulse, defined
   inside the FR-raw read, whose reference is the entangled ground —
   a different read with a different zero; importing its duration
   into FR-net mixes the two reads' references.
4. τ_marg ≥ τ₀ wherever both exist, so the ruling is also the
   longer, less conservative duration; it is adopted because the
   text fixes the reference, not because it is longer.
Status under the OTHER convention (τ₀): the claim stands at the
deciding rows — all five both-convention bar-clearers keep
R(τ₀) > 1 (2.2536, 3.6230, 6.5180, 4.2433, 9.7931) and the τ₀-only
row (10,1,2) keeps R(τ₀) = 5.134 with no τ_marg return within
t ≤ 30. Only the two convention-split rows change side under τ₀:
(5,1,0.5) R = 0.9871 < 1 and (6,1,1) R = 0.5228 < 1, versus
1.5132 and 8.8845 under τ_marg. So under τ₀ the reopening bar is
still met (five rows, plus (10,1,2) on τ₀ alone); under τ_marg it
is met at seven rows. The claim is not convention-dependent at its
deciding rows; the split rows are.

## C12 accounting note

This is a sourcing-accounting result in a finite spin model: the
negative E_net,B is relative to the uncorrelated marginal-product
reference, with the preparation resource and the injected E_in on
the books (price per unit in the results file). No "energy source",
no field claim, no FTL wording attaches to any number here.
INTERNAL only.
