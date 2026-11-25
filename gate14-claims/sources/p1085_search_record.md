# P108-5 — Search Record (FU-P106-3a, conditional multipartite QET)

Registration (CHECKPOINT108 §P108-5): the evaluation runs ONLY if a
documented literature search finds a genuinely multipartite QET
protocol whose Hamiltonian AND delivered-energy formulas are
published in evaluable form (printed formulas that can be
recomputed, not only numerical plots or simulation descriptions).
Accounting, if triggered: Phase 106 P106-3's inherited accounting
verbatim (resource counted; per-sector uncorrelated reference;
R_net as defined in P72-2 §4 / P106-3). Reopening bar: any variant
with R_net > 1 resource-counted. This record is the search; the
evaluation it triggered is in `p1085_memo.md` /
`p1085_results.json` / `work/p1085_eval.py` +
`work/p1085_secondpath.py` + `work/p1085_check.py`.

## Queries run (web search, 2026-11-23)

1. `multipartite quantum energy teleportation`
2. `multi-party QET Hamiltonian quantum energy teleportation`
3. `three-qubit QET ground state energy extraction formula`
4. `multipartite QET protocol analytical energy`
5. `"quantum energy teleportation" N-qubit Hamiltonian E_out formula`
6. `Ikeda long-range quantum energy teleportation distribution multipartite Hamiltonian`
7. `"quantum energy teleportation" spin chain many-body analytical extracted energy Hotta`
8. `"quantum energy teleportation" three parties OR multipartite OR multi-party review Hotta spin chain`

Primary sources (arXiv full texts) were fetched and read for every
candidate below; secondary summaries (news/blogs, a review) were
used only as pointers.

## Candidates and evaluability assessments

### C1 — Xun & Ren, "Quantum Energy Teleportation via Random Bi-Partitioning in N-Qubit Systems", arXiv:2410.04919 — **PASSES (evaluated)**

- Genuinely multipartite: a single N-qubit resource state; the
  interaction is the N-body term V = 2k σ₁ˣ…σ_Nˣ + const — not a
  composition of pair protocols. (N−m) parties measure (inputs),
  m parties extract jointly (outputs); the paper calls the model
  "genuinely correlated N-body".
- Hamiltonian printed in evaluable form: Eqs. (1)–(2)
  (H_i = hσ_i^z + Nh²/D, V as above, D = √(N²h²+4k²)); analytic
  ground state Eq. (3); explicit 3-qubit (App. A, Eqs. 18–42) and
  4-qubit (App. B, Eqs. 43–67) instances.
- Delivered-energy formulas printed in evaluable form: E_in
  Eq. (6); E_out Eqs. (9)–(11) in closed form in (N, m, h, k);
  optimal unitary Eq. (7) with optimal θ Eq. (10); efficiency
  Eq. (12); m = 1 specialisation Eqs. (13)–(14). The paper itself
  plots the general formula at N = 10 and N = 100 (Figs. 2–3).
- Evaluability verdict: Hamiltonian AND delivered energy are
  recomputable closed formulas. The P72-2/P106-3 accounting
  applies directly: the receiving sector is the paper's own
  extraction sector (output H_i's + V, Eqs. 28/39 pattern), and
  its marginal-product (uncorrelated) reference energy is an
  expectation value of the printed H, exactly as in P72-2 §3
  (R-marg). **Condition met; evaluation triggered (see memo).**

### C2 — Hassan, Shubha & Mahdy, "Enhanced Quantum Energy Teleportation using a 3-Qubit System", arXiv:2408.07997 — **FAILS evaluability**

- Genuinely 3-qubit in intent (MISO: two senders → one receiver;
  SIMO: one sender → two receivers), but the paper does NOT print
  a 3-qubit Hamiltonian in evaluable form: its printed Hamiltonian
  (Eqs. 7–9) is the 2-qubit minimal model; the 3-qubit extension
  is specified by circuits (Figs. 4–5), a spin-chain diagram
  (Fig. 11), and hardware tables. The delivered energies appear
  only as tabulated "analytical values" for specific (h, k) points
  (Table I: ⟨V_b⟩, ⟨V_c⟩, E_a, E_c) with no printed closed-form
  E_out(h, k) for the 3-qubit Hamiltonian from which they were
  computed, and the interaction terms V_{0,2}, V_{1,2} are never
  given as formulas of a stated 3-qubit H.
- Gap: no recomputable Hamiltonian + delivered-energy formula
  pair. Evaluating it would require reconstructing the model from
  circuits/tables — exactly the improvisation the registration
  forbids. (Its reported efficiencies, ~32–58% observing only V,
  are in any case E_out/E_in reads, not net-of-resource reads.)

### C3 — Khan, Anjum & Chowdhury, "Quantum Energy Teleportation across Multi-Qubit Systems using W-State Entanglement", arXiv:2505.01863 — **FAILS evaluability**

- Multi-qubit circuits (3, 4, 5 qubits) built on a W state, but
  there is no interacting ground-state Hamiltonian of QET type:
  the "total Hamiltonian" is Eq. (3) H_total = ΣH_i + V with V
  never specified as an operator; the local terms are projectors
  H_n = |1⟩⟨1|_n (Eq. 10); the resource state (Eq. 7) is an
  ansatz superposition of |0…0⟩ and |W_N⟩, not shown to be the
  ground state of the stated H (Eq. (9) asserts H_total = E_0);
  the receivers' operation is a phase correction (I or Z), not an
  energy-extracting unitary with a printed optimum.
- Delivered energy: no delivered-energy formula at all — only
  simulator/hardware measurement tables (Tables 1–3) of positive
  subsystem Hamiltonian readings that decrementshare the injected
  E_0. Nothing negative is delivered at any sector, and no formula
  exists to recompute.
- Gap: neither a specified interacting Hamiltonian nor a
  delivered-energy formula. A circuit/simulation description —
  the registration's excluded case.

### C4 — Hotta, "A Protocol for Quantum Energy Distribution", arXiv:0803.1512 — **FAILS evaluability for this accounting (borderline, gap named)**

- Genuinely multi-party: M consumers simultaneously extract from
  one spin chain, per-consumer formula E_m = ½[√(ξ_m²+η_m²) − ξ_m]
  (Eq. 9) — but ξ_m, η_m are ground-state correlators of a GENERIC
  spin chain (H = ΣT_n with T_n an unspecified local form,
  §2–3). The one concrete model (critical transverse Ising,
  §5) evaluates only the TOTAL distributed energy for infinitely
  many consumers, E_C ≈ 6.2×10⁻⁵ h (Eq. 24), via the correlator
  Δ(n) given through special-function products/asymptotics.
- Gap: the resource is an infinite chain — there is no finite
  per-copy resource state whose per-sector marginal-product
  reference (the inherited accounting's deciding object) is
  printed or finite; no finite Hamiltonian instance with a
  closed delivered-energy formula per receiving sector is given.
  Posing the inherited accounting on it would require inventing
  the finite resource and its reference — not evaluable as
  registered. (Noted as the closest miss after C1.)

### C5 — QKD by QET / N-party information sharing, arXiv:2506.02054 — **FAILS (not multipartite QET)**

The N-party construction is a key-distribution protocol built by
composing the two-party QET primitive; no multipartite
Hamiltonian or multipartite delivered-energy formula is printed.
Compositions of the pair protocol are P106-3's closed scope.

### C6 — Xie, Sajjan & Kais, "Strong Local Passivity … Amplified Quantum Energy Teleportation", arXiv:2502.05288 — **FAILS (not multipartite)**

A two-party (Alice–Bob) protocol on the printed two-qubit
H_AB (Eq. 2), with an auxiliary register in the amplified
variant; extracted energy is a total-system ΔE (Eq. 7), not a
multipartite sector delivery. Two-party scope, already the
P72-2/P106-3 closed class in kind.

### C7 — Pointers checked, not candidates

Frey–Gerlach–Hotta Gibbs-state QET (arXiv:1305.5853, two sites);
Ikeda long-range QET/distribution on hyperbolic networks
(QST+QET hybrid, no multipartite Hamiltonian with delivered
formula); Ikeda–Lowe QIP using QET (complexity construction, no
Hamiltonian/energy formula); the QET review arXiv:2505.04689
(secondary; its multipartite pointers reduce to C1–C4 above);
Hotta's spin-chain QET (arXiv:0803.0348) and the repeater
architecture arXiv:2601.18327 (many-body chains, delivered
energy only as correlator expressions / scaling claims — same
gap as C4).

## Search outcome

ONE candidate passes the registered evaluability condition:
**C1, Xun & Ren arXiv:2410.04919**. The evaluation therefore ran,
under the inherited accounting verbatim, with definitions fixed
in `work/p1085_definitions.md` before the deciding (τ) computation
and a from-scratch dense-matrix second path. Result and verdict:
`p1085_memo.md`. Headline: the search is NOT negative, and the
evaluation's deciding reads are stated there — including that
**the reopening bar is met** at several of the paper's own
configurations (flagged in the memo, §Deciding reads).

Search limits (stated per language lock): web search over the
queries above plus full-text reads of every candidate they
surfaced, 2026-11-23; a multipartite QET paper not indexed under
these terms would not have been found. INTERNAL ONLY.
