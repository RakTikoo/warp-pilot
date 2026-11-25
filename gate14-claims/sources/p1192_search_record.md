# P119-2 — Search Record (FU-P1085-2, the field/oscillator analogue)

Registration (CHECKPOINT119 §P119-2): the analogue is posable ONLY if
the literature supplies, in evaluable form (printed formulas that can
be recomputed, not only numerical plots): (i) a field or
harmonic-oscillator QET protocol — Hamiltonian and ground state
printed; (ii) its delivered energy at a receiving sector/region in
printed form; AND (iii) a multipartite / multi-receiver /
shared-resource structure in print in which an N-scaling of the
sector correlation energy vs the per-receiver extraction can be
read. If (i)+(ii) exist but (iii) does not: NOT POSABLE in its
multipartite clause, missing ingredient named, single-receiver
anatomy reported. Accounting, had it posed: P72-2 §§3–4 via P106-3,
verbatim. This record is the search; the anatomy it leaves is in
`p1192_memo.md` / `p1192_results.json` / `work/p1192_anatomy.py` +
`work/p1192_checker.py`.

## Queries run (web search, 2026-11-23)

1. `quantum energy teleportation quantum field theory Hotta Hamiltonian ground state extracted energy formula`
2. `quantum energy teleportation conformal field theory arXiv`
3. `quantum energy teleportation harmonic oscillator coupled oscillators arXiv`
4. `multipartite quantum energy teleportation field theory multi-receiver shared interaction`
5. `"2410.04919" OR "Xun" "Ren" citing multipartite quantum energy teleportation field oscillator generalization`
6. `Hotta quantum energy teleportation massless Klein-Gordon field 1+1 extracted energy formula arXiv 0803`
7. `quantum energy teleportation spin chain continuum limit field theory extracted energy analytical formula`
8. `"quantum energy teleportation" multiple receivers OR "energy distribution" consumers formula Hotta chain`
9. `"quantum energy teleportation" "N-qubit" OR "N-party" OR multipartite oscillator chain receivers extracted energy scaling`
10. `Mann Villasenor quantum energy teleportation quantum field theory protocol detectors arXiv`
11. `"quantum energy teleportation" review 2025 field theory harmonic chain multipartite Xun Ren`
12. `"quantum energy distribution" field theory multiple consumers extract energy vacuum regions`
13. `quantum energy teleportation several receivers one measurement field vacuum extraction regions protocol`

Primary sources (arXiv full texts / publisher pages) were fetched and
read for every candidate below; reviews and secondary summaries were
used only as pointers. Full texts read end-to-end: C1 (all 23 pp.),
C2 §3 energetics, C3 §§2–2.4 (continuum protocol).

## Candidates and clause assessments

### C1 — Nambu & Hotta, "Quantum Energy Teleportation with a Linear Harmonic Chain", arXiv:1007.2234 — **(i) YES, (ii) YES, (iii) NO — the closest field/oscillator form**

- (i) YES: Hamiltonian printed, Eq. (1),
  H = ½ Σ_j (p_j² + q_j² − α q_j q_{j−1}), periodic chain of N sites;
  ground state printed as the Gaussian fixed by the mode expansion
  Eqs. (2)–(3) and the two-point functions Eqs. (4)–(5)
  (g_r = (1/N)Σ_k cos(rθ_k)/(2ω_k), h_r = (1/N)Σ_k ω_k cos(rθ_k)/2,
  ω_k² = 1 − α cos θ_k), wavefunction Eq. (8). Fully recomputable.
- (ii) YES: the receiving sector is a single site B with printed
  local energy H_B, Eq. (19) (with ε fixed by Eq. (20),
  ⟨g|H_B|g⟩ = 0), and the optimized delivered energy is printed in
  closed form, Eq. (26):
  ⟨H_B⟩_opt = −½ J_pᵀT_p⁻¹J_p − ½ J_qᵀT_q⁻¹J_q < 0,
  with T_p, T_q, J_p, J_q defined in Eq. (24) and the line following
  it, entirely from the printed correlators. Recomputed in
  `work/p1192_anatomy.py`; the paper's own printed critical fit
  Eq. (40) is reproduced (checker, 1% clause).
- (iii) NO — the deciding gap. The protocol is bipartite in every
  printed setting: a measured group A vs ONE receiving site B
  (Sec. III B: "group B … composed of a single site in our numerical
  setting", n_B = N/2 + ℓ + 1). Setting 1 varies the A–B separation
  d; Setting 2 varies the number 2ℓ+1 of MEASURED (sender-side)
  sites. There is no multi-receiver structure, no shared-resource
  division among receivers, and no N that counts receivers: N is
  the chain length. The only N-scalings in print run the wrong way
  or saturate (paper Eq. (40); anatomy in the memo): at maximal
  measurement the single receiver's extraction DECREASES with N
  toward a constant, and the receiving sector's correlation energy
  (α g_1/2 in the inherited R-marg construction) does not dilute —
  it is a fixed local two-point function of B's own bonds.
- Also absent, for the record: no printed E_in (measurement energy
  infusion is discussed qualitatively, never given a closed form),
  and no printed protocol duration — the paper explicitly neglects
  H-evolution during the protocol and takes the classical
  communication speed infinite (Secs. I, III), so the FR-net ratio's
  τ cannot be read from the published form's own evolution either.

### C2 — Guo & Lin, "Quantum Energy Teleportation in Two-dimensional Conformal Field Theories", arXiv:1708.09544 — **(i) NO (as registered), (ii) scaling only, (iii) NO**

- (i) NO in the registration's sense: no Hamiltonian of a specified
  model is printed; the theory is a generic 2D CFT (unspecified
  primaries, OPE coefficients, central charge) and the "ground
  state" is the abstract CFT vacuum. The measurement operators are
  OPE blocks holding only in the weak (ground-state) sense.
- (ii) The delivered energy appears only as a large-T asymptotic
  series whose coefficients are unspecified CFT data: leading order
  is negative-definite (no extraction as T → ∞, their no-go), and
  the toy-model read, Eq. (69),
  E_B⁽¹⁾ = −C T^{−(4n+1)} β₁ [1 + (64/π²)c]⁻¹ (Γ(2n−1)/(Γ(n)Γ(n+1)))²,
  still carries free parameters (n, c, β₁, C) — a sign/scaling
  demonstration, not a recomputable delivered energy for a specified
  Hamiltonian.
- (iii) NO: one Alice interval, one Bob.

### C3 — Ikeda, "Quantum Energy Teleportation Across Lattice and Continuum", arXiv:2604.09973 (Phys. Rev. D 114, 045016 (2026)) — **(i) PARTIAL, (ii) YES in correlator form, (iii) NO**

- (i) PARTIAL: continuum Hamiltonian density printed in canonical
  form (sine-Gordon, Eq. (2) of the paper, constant chosen so the
  ground-state energy density vanishes), but the ground state
  itself is available only through form-factor/spectral
  representations, not a printed evaluable state.
- (ii) YES in form: Bob's optimized extracted energy printed,
  E_B^max = η²/(2ξ) (Eq. (20)), η a ground-state correlator
  ⟨D̂_A Ô_B(T)⟩_g with exact bulk form-factor evaluation; extracted
  energy quadratic in the measurement strength. One Bob region,
  windowed by w_B(x).
- (iii) NO: one Alice region A, one Bob region B, on both the
  continuum and the lattice side (the lattice protocol is
  single-site at each end). No receiver multiplicity, no
  shared-resource N-scaling anywhere in the paper.

### C4 — Hotta, "Quantum Measurement Information as a Key to Energy Extraction from Local Vacuums", arXiv:0803.2272 (Phys. Rev. D 78, 045006) — **(i) YES in kind, (ii) YES for its example, (iii) NO**

The original field QET: free massless scalar field in 1+1
dimensions, a general POVM measurement at Alice's point and an
explicit worked example (§5) in which part of the excitation energy
is extracted at Bob's distant apparatus, with negative-energy
wavepackets at Bob. Single sender point, single receiving
apparatus; no multipartite structure of any kind. (Pointer text
read via the arXiv full text archived copy; §§1–5 structure and
the §5 example verified.)

### C5 — Hotta, "Quantum Energy Teleportation with an Electromagnetic Field: Discrete versus Continuous Variables", J. Phys. A 43, 105305 (2010) — **(iii) NO**

Field QET where Alice's probe is either a qubit or ONE harmonic
oscillator coupled to the EM vacuum fluctuation, and Bob extracts
with the matching single apparatus (teleported energy exponentially
damped in input for the spin probe, power-damped for the oscillator
probe). The oscillator here is a measuring probe, not a receiving
sector of a multipartite resource; one sender apparatus, one
receiver apparatus. Fails (iii).

### C6 — Funai & Martín-Martínez, "Engineering Negative Stress-Energy Densities with Quantum Energy Teleportation", arXiv:1701.03805 — **(iii) NO**

Detector-based field QET: two Unruh–DeWitt detectors (one Alice,
one Bob) coupled to a scalar field; the protocol's negative
stress-energy densities are printed and shown to saturate the
quantum interest conjecture. Directly relevant to the QEI floor
(the field pulse is QI-priced in print, and saturates it), but the
structure is a single detector pair: no multi-receiver or
shared-resource scaling. Fails (iii).

### C7 — Verdon-Akzam, Martín-Martínez & Kempf, "Asymptotically Limitless Quantum Energy Teleportation via Qudit Probes", Phys. Rev. A 93, 022308 (2016) — **(iii) NO**

Two qudit probes coupled to a field; "limitless" is in probe
dimension at a single receiving probe, not in receiver count.
Fails (iii). (Pointer via the 2025 review, C11, and the Waterloo
thesis record.)

### C8 — Haque, "Thermal Screening and Critical Scaling of Quantum Energy Teleportation in a Harmonic Chain", Phys. Rev. A (2026) — **(i) YES in kind, (ii) YES, (iii) NO**

Finite-temperature Gaussian formulation on the same harmonic chain
as C1; the protocol is explicitly the SINGLE-SITE protocol, its
extracted energy governed by a single correlator, with the exact
zero-temperature critical law E_ext ∼ d^{−4} derived. The resource
state is a Gibbs state (ground state only as the T → 0 limit).
One receiver site; no multipartite structure. Fails (iii). Its
d^{−4} law is consistent anatomy for C1's extraction fall-off
(C1's numerical fit: d^{−3.6}).

### C9 — Hotta, "A Protocol for Quantum Energy Distribution", arXiv:0803.1512 (Phys. Lett. A 372, 5671 (2008)) — **(iii) EXISTS but wrong system class and not evaluable per sector — the closest miss on (iii), already C4 of P108-5's search**

The ONLY multi-receiver QET structure in print found by either
search: M consumers simultaneously extract from one chain, per-
consumer formula E_m = ½[√(ξ_m² + η_m²) − ξ_m]. But (a) it is a
SPIN chain protocol, not a field/oscillator one — outside this
item's registered scope; (b) ξ_m, η_m are correlators of a GENERIC
chain (H = Σ_n T_n with T_n an unspecified local form), and the one
concrete model (critical transverse Ising) evaluates only the
TOTAL distributed energy for infinitely many consumers
(E_C ≈ 6.2×10⁻⁵ h), not a per-receiver delivered energy against a
finite per-sector reference; (c) no N-scaling of a sector
correlation energy vs per-receiver extraction is printed — the
consumers are symmetric sites of one chain, each carrying its own
local correlator, and no shared interaction term is divided among
them. Fails the field/oscillator scope and (i)/(ii) in finite
per-sector form. Carried verbatim from P108-5's assessment; not
re-derived here.

### C10 — Xun & Ren, arXiv:2410.04919, and its citing/generalising literature — **no field/oscillator generalisation found**

Queries 5, 9, 11 targeted papers citing or generalising Xun–Ren
toward fields, oscillators, or chains. Nothing surfaced: the
citing trail returns the paper itself, the harmonic-chain paper
(C1, which predates it by 14 years), and the circuit W-state work
already failed on evaluability by P108-5 (its C3: no interacting
Hamiltonian, no delivered-energy formula). No published work
transplants the N-body shared interaction V = 2k Πσˣ — the object
whose total correlation energy 4k²/D is what dilutes — into a
field or oscillator Hamiltonian.

### C11 — Pointers checked, not candidates

Ragula & Martín-Martínez review, arXiv:2505.04689 (every field/
oscillator pointer in it reduces to C1–C8 above; its multipartite
pointers reduce to P108-5's C1–C4); Hotta's spin-chain QET,
arXiv:0803.0348, and ground-state-entanglement bound, Phys. Rev. A
87, 032313 (2013) (spin chains, correlator-generic — wrong system
class, same gap as C9); Haque, arXiv:2601.18718 (an upper BOUND
|E_A − E_B| ≤ C e^{−μd} for gapped LATTICE systems — a bound, not a
protocol form, and lattice not field); Ikeda's QFT-criticality QET,
Phys. Rev. D 107, L071502 (2023) (single receiver, correlator
form); QET in quantum Hall edge channels and trapped ions (cited
as [17–20] in C3 — single-receiver protocols); the QUINT /
Q-UNIVERSE preprints (viXra 2508.0175, 2509.0069 — a network of
independent Alice–Bob pairs with hypothesised per-cycle formulas;
not a shared-resource multipartite form, not a primary
arXiv/publisher source, and no evaluable Hamiltonian + delivered
energy pair).

## Search outcome

**No candidate meets (i)+(ii)+(iii).** Clauses (i) and (ii) ARE met
by published field/oscillator forms — cleanly by C1 (Nambu–Hotta
harmonic chain), in correlator form by C3 and C8. Clause (iii) is
met NOWHERE in the field/oscillator literature found: every
field/oscillator QET in print is a single-receiver protocol. The
missing ingredient is named exactly in the memo. Verdict:
**NOT POSABLE FROM PUBLISHED FORMS** (multipartite clause), with
C1's single-receiver anatomy reported as registered.

Search limits (stated per language lock): web search over the 13
queries above plus full-text reads of every candidate they
surfaced, 2026-11-23; a field/oscillator multipartite QET paper
not indexed under these terms would not have been found. INTERNAL
ONLY.
