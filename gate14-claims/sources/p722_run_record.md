# P72-2 — Run Record (fixed BEFORE any number)

Written before any computation. This record fixes the exact published
QET model, its published formulas, and every accounting definition the
verdict will use. No fitted or reconstructed formula is substituted
anywhere below; every evaluated expression is a printed formula of the
cited source (or an expectation value of the printed Hamiltonian,
labelled as such).

## 1. Model fixed (registered preference: Hotta's standard qubit pair)

**Source:** M. Hotta, "Energy-Entanglement Relation for Quantum Energy
Teleportation", Phys. Lett. A 374, 4165 (2010); arXiv:1002.0200 —
the minimal QET model (two qubits, Ising interaction in a transverse
field). Cross-check values are the h = k point quoted in the QET
review literature (Hotta, arXiv:1008.0188 / 1101.3954): at h = k the
protocol gives E_A ≈ 0.707 and E_B ≈ 0.115 in model units; the
evaluation script must reproduce these before any other number is
trusted (instrument control, §5).

**Hamiltonian** (source Eqs. (1)–(3); h, k > 0, energy dimension):

    H  = H_A + H_B + V
    H_A = h σ_A^z + h²/√(h²+k²)
    H_B = h σ_B^z + h²/√(h²+k²)
    V   = 2k σ_A^x σ_B^x + 2k²/√(h²+k²)

The constants are chosen in the source so that
⟨g|H_A|g⟩ = ⟨g|H_B|g⟩ = ⟨g|V|g⟩ = 0 and the ground eigenvalue of H
is 0 (H ≥ 0).

**Ground state** (source, §2):

    |g⟩ = (1/√2)√(1 − h/√(h²+k²)) |+⟩|+⟩ − (1/√2)√(1 + h/√(h²+k²)) |−⟩|−⟩

with |±⟩ eigenstates of σ^z. Ground-state correlations used below:
cos ς = h/√(h²+k²), sin ς = k/√(h²+k²) (source, after Eq. (8)), and
⟨g|σ_A^x σ_B^x|g⟩ = −k/√(h²+k²) (follows from ⟨g|V|g⟩ = 0 and Eq. (3)).

## 2. Published protocol formulas to be evaluated (only these)

- **Alice's injected energy** (source Eq. (4)):
  E_A = (2h²/√(h²+k²)) Σ_μ l_μ², for POVM operators
  M_A(μ) = m_μ + e^{iα_μ} l_μ σ_A^x. Registered measurement: the
  projective σ_A^x measurement attaining the source's optimum,
  M_A(μ) = (1 + (−1)^μ σ_A^x)/2, i.e. m_μ = 1/2, l_μ = (−1)^μ/2,
  p_A(μ) = 1/2, q_A(μ) = (−1)^μ/2 (so q_A²/p_A² = 1, the case the
  source states attains its bounds). Hence Σ l_μ² = 1/2 and
  E_A = h²/√(h²+k²).

- **Bob's extracted energy, maximum over his local unitary**
  (source Eq. (7)):
  max E_B = ((h²+2k²)/√(h²+k²)) Σ_μ p_A(μ)
           [ √(1 + (h²k²/(h²+2k²)²)(q_A(μ)²/p_A(μ)²)) − 1 ],
  attained by U_max(μ) = cos Ω_μ + i σ_B^y sin Ω_μ with
  cos 2Ω_μ, sin 2Ω_μ as printed after Eq. (7). For the registered
  projective measurement this reduces to the source's global maximum
  (printed after Eq. (7)):
  max E_B = ((h²+2k²)/√(h²+k²)) [ √(1 + h²k²/(h²+2k²)²) − 1 ].
  E_B is the energy by which Tr[ρ(H_B + V)] goes negative:
  E_B = −Tr[ρ(H_B+V)] (source, §2) — i.e. Hotta's own bookkeeping
  assigns the full interaction V to Bob's sector for this read.
  The locally negative energy delivered at Bob's site per copy is
  therefore −E_B in the (H_B + V) sector, relative to the entangled
  ground state's zero.

- **Entanglement of the ground state** (source Eq. (8) at q_A = 0):
  eigenvalues of ρ_B are λ_± = (1 ± cos ς)/2;
  S_ground = −Σ λ_± ln λ_± (nats; ebits = S/ln 2).

- **Entanglement consumed by Alice's measurement** (source Eqs. (8)–(9)):
  ΔS_AB = Σ_μ p_A(μ) f_I(q_A(μ)²/p_A(μ)²) with f_I as printed.
  For the registered projective measurement q_A²/p_A² = 1, where
  λ_±(μ) = (1 ± 1)/2, the post-measurement B states are pure, and
  ΔS_AB = S_ground exactly (all ground-state entanglement consumed).

## 3. Preparation price — definitions fixed here

Two uncorrelated references, both computed from the printed H.
The DECIDING total uses the smaller (conservative: it understates
the resource price, i.e. it is the choice most favourable to a
loophole filing).

 (R-sep) **Separable-minimum gap.** E_sep = min over product states
 of ⟨H⟩ (an expectation value of the printed H, minimised over
 product Bloch vectors — evaluation of H, not a new formula);
 E_prep^(sep) = E_sep − E_ground = E_sep (E_ground = 0 by the
 source's constants). This is the least energy, above the entangled
 ground state, of any state with no A–B correlations at all.

 (R-marg) **Marginal-product correlation energy.** Reference =
 ρ_A ⊗ ρ_B built from |g⟩'s own marginals (same local states, all
 correlations deleted). E_prep^(marg) = ⟨H⟩_{ρ_A⊗ρ_B} − ⟨H⟩_g.
 Since the marginals fix ⟨H_A⟩ = ⟨H_B⟩ = 0, this is exactly the
 correlation part of V: E_prep^(marg) = −2k⟨σ_A^xσ_B^x⟩_g
 = 2k²/√(h²+k²). Sector form (deciding for §4's local read):
 the (H_B + V) sector's energy in the marginal-product reference
 above its ground value is the same 2k²/√(h²+k²), because
 ⟨H_B⟩ is identical in the two states.

## 4. Ford–Roman comparison — definitions fixed here

W6 law (Phase 2 §W6): ρ_min(τ) = −(3/(32π²)) ħ/(c³τ⁴);
E_legal(L) = (3/(32π²)) ħc/L for a pulse in volume L³ sustained
τ ~ L/c. Two reads, both reported:

 (FR-raw) The local pulse as Hotta states it, relative to the
 entangled-ground zero: magnitude E_B, duration τ_pulse := the
 first time t > 0 after Bob's optimal operation at which
 ⟨H_B + V⟩(t) under the printed H returns to zero (direct
 evaluation of the printed H and the printed U_max; the model's
 only intrinsic duration for the negative excursion). Volume by
 the W6 identification V = (c τ_pulse)³, ρ = −E_B/V, and the
 ratio R_raw = |ρ|τ_pulse⁴ / [(3/(32π²))ħ/c³]
             = E_B τ_pulse / [(3/(32π²)) ħ].

 (FR-net) The same read WITH the resource on the books, which is
 the registered deciding read: the Ford–Roman bound is referenced
 to the uncorrelated vacuum, so Bob-sector energy is read relative
 to the uncorrelated reference (R-marg), not relative to the
 entangled ground. Net Bob-sector energy after extraction,
 relative to (R-marg): E_net,B = E_prep^(marg) − E_B. If
 E_net,B ≥ 0, no negative pulse relative to the uncorrelated
 reference exists at all: R_net = 0.

## 5. Registered evaluation points and controls

Dimensionless ratios r = k/h ∈ {0.5, 1, 2} plus the headline point
h = k = 1 (energies in units of h; ħ = 1 in model units for
τ_pulse, restored explicitly in the FR ratios). These are
evaluations of the printed formulas at named points, not a scan.
Controls: (i) h = k values reproduce the review-quoted
E_A ≈ 0.707, E_B ≈ 0.115; (ii) E_B ≤ E_A at every point (the
source's stated bound: output is upper-bounded by input);
(iii) ΔS_AB(projective) = S_ground by direct Eq. (9) evaluation.

## 6. Classical leg and C12 accounting (stated, not relitigated)

QET's classical leg (Alice's 1-bit result μ for the registered
measurement) travels at ≤ c by the protocol's own construction
(Phase 2 §W7(i)); Bob can act only after it arrives, latency ≥ D/c
for separation D. Its energy cost is not a printed formula of the
model; it is ≥ 0, so omitting it understates the total price —
every price ratio below is a lower bound. Construction-inclusive
(C12) total per copy = E_prep + E_A + E_classical(≥ 0); the verdict
is a filing about bookkeeping, never a transport claim.

## 7. Filing criterion (registered, CHECKPOINT72 §P72-2(c))

FILED AS RELOCATION iff the total bookkeeping prices the delivered
negative energy at ≥ the W6 pulse price for the same magnitude and
duration — deciding lines: total price per unit delivered,
(E_prep + E_A)/E_B ≥ 1, AND the resource-on-books pulse read
R_net ≤ 1. FILED AS LOOPHOLE iff a step's local negative energy,
with ALL resource costs counted, exceeds the pulse bound for its
duration (R_net > 1 with surviving margin). No third filing.
