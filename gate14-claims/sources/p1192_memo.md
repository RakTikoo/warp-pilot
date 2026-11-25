# P119-2 — Memo (FU-P1085-2): does the 1/N dilution survive in a field / oscillator analogue?

**VERDICT: NOT POSABLE FROM PUBLISHED FORMS** — the multipartite
clause (iii) is absent from the published field/oscillator record.
Missing ingredient, named exactly: **a published field or
harmonic-oscillator QET protocol with a multipartite /
multi-receiver / shared-resource structure — more than one
receiving sector drawing on one shared interaction — in which an
N-scaling of the sector correlation energy against the
per-receiver extraction can be read.** Every field/oscillator QET
in print is a single-receiver protocol (one Alice region/apparatus,
one Bob region/apparatus). The only multi-receiver QET structure
in print at all (Hotta's quantum energy distribution,
arXiv:0803.1512) is a spin-chain protocol with a generic,
unspecified chain Hamiltonian and only a total, infinitely-many-
consumers energy evaluated — wrong system class for this item and
not evaluable per sector (P108-5's candidate C4, carried verbatim).
Full search: `p1192_search_record.md` (13 logged queries, 11
candidates assessed by name against (i)–(iii)).

So the deciding question — does the shared-resource cost still
dilute ~1/N while per-receiver extraction holds, against a
continuum of modes and a QEI-priced floor? — **cannot be posed on
any published field/oscillator form.** What follows is the
registered fallback: the single-receiver field anatomy that DOES
exist, from the one form meeting (i)+(ii) cleanly.

## The single-receiver anatomy that exists (Nambu & Hotta, arXiv:1007.2234)

The harmonic-chain QET prints everything the pair-level accounting
needs: H (Eq. 1), the Gaussian ground state via Eqs. (2)–(5), the
receiving sector's local energy H_B (Eq. 19, zeroed on the ground
state by Eq. 20), and the optimized delivered energy in closed
form (Eq. 26). I evaluated it under the inherited accounting
verbatim (P72-2 §3 (R-marg) construction on the printed H): the
receiving sector is the paper's own site-B sector (which carries
B's coupling halves exactly as printed in Eq. 19); its uncorrelated
reference is the product of the ground state's own single-site
marginals, in which ⟨q_n q_{n±1}⟩ = 0, giving the sector
correlation energy

  E_prep^(marg, sector) = α·g₁/2,   g₁ = (1/N)Σ_k cos θ_k/(2ω_k),

and E_net,sector = E_prep^(marg, sector) − E_delivered,
R_net = 0 iff E_net ≥ 0 (P72-2 §4). Numbers:
`p1192_results.json`, computed by `work/p1192_anatomy.py`,
independently recomputed by `work/p1192_checker.py` (complex-
exponential correlator route; ALL PASS, incl. a 1% cross-check
against the paper's own printed Eq. (40) fit). POVM parameter
ω = 1 (the site frequency of Eq. (1); the paper leaves ω as the
POVM's own parameter — the sign of every read is insensitive to
it, since E_prep does not contain ω and E_delivered only shrinks
as ω moves away from the correlators' scale).

**Reads (Setting 1: one measured site, N = 100).**
E_prep^(marg, sector) is independent of the A–B separation d:
0.09975 (α = 0.90), 0.13837 (0.95), 0.22892 (0.99), 8.21303
(α = 1−10⁻⁷, IR/zero-mode dominated at finite N — a regulator
artefact of the paper's own α₄, stated as such). E_delivered
falls steeply with d — at α = 0.99: 1.885×10⁻² (d = 1),
6.76×10⁻⁴ (2), 1.08×10⁻⁴ (3), 9.68×10⁻⁶ (5), 2.18×10⁻⁷ (10),
1.32×10⁻⁹ (20); the paper's printed critical fit is
|⟨H_B⟩| ∼ 2×10⁻³ d^{−3.6} (its Eq. 37), and the thermal-chain
successor (search C8) derives E_ext ∼ d^{−4} exactly at criticality.
**E_net,sector > 0 at all 24 Setting-1 rows and all 10 Setting-2
rows; R_net = 0 everywhere.** Even at the best point (d = 1) the
delivered energy is only 8–15% of the sector's own correlation
energy (1.5% at criticality).

**Reads (Setting 2: maximal measured block, 2ℓ+1 = N−3 senders,
one receiver).** This is the only "many-party" knob in print, and
it is on the SENDER side. E_delivered saturates in N
(α = 0.99: 1.736×10⁻³ at N = 20 → 1.717×10⁻³ at N = 100;
critical: → 2.069×10⁻³ at N = 100, against the paper's printed
fit constant 0.0020613, Eq. (40)), while E_prep^(marg, sector)
does not dilute at all — at α = 0.99 it sits at ≈ 0.229 for every
N. There is no crossing, at any N, in either setting.

**Scaling statement (the deciding anatomy).** In Xun–Ren the
dilution is a property of ONE shared N-body interaction:
V = 2k Πᵢσᵢˣ is a single term, its total correlation energy is
4k²/D with D = √(N²h² + 4k²) ≈ Nh, and that one total is what the
single output sector is charged — hence 1/N. In every
field/oscillator form in print the couplings are LOCAL and
PAIRWISE (nearest-neighbour q_j q_{j−1} in C1; a local field
density in C3/C4), so a receiving sector's correlation energy is
an INTENSIVE, local quantity — here α g₁/2, a two-point function
of the receiver's own bonds — which is not a shared total divided
by anything. Adding parties adds senders or sites; it does not
divide the receiver's price. The extraction, meanwhile, is
controlled by the A–B correlator at the receiver's separation and
DECAYS with distance (d^{−3.6}…d^{−4} at criticality, exponential
off it). The two scalings that cross at N = 5 in the spin model
therefore have no field counterparts in print: the price does not
fall with party number, and the extraction does not hold with
distance. This is a statement about the published forms, not a
theorem about fields: a field Hamiltonian with a genuinely shared
multi-receiver interaction term is simply not in the literature
found.

**The QEI-priced floor, in the inherited accounting's terms.**
It never gets to bite, for two independent reasons. (1) There is
no below-reference pulse to price: E_net,sector ≥ 0 at every
anatomy point, so R_net = 0 identically — the floor
(3/(32π²))·τ⁻⁴ (density form) prices a negative excursion that
this protocol, resource counted, does not produce. For scale
only: even if the ENTIRE delivered energy at the best point
(α = 0.99, d = 1, E = 1.885×10⁻²) were (counterfactually) a
below-reference pulse, the FR ratio would reach 1 only at
τ ≈ (3/(32π²))/E ≈ 0.50 in model units — the accounting gives
the field pulse no headroom to hide in. (2) The duration input
itself is not in print: the harmonic-chain paper explicitly
neglects H-evolution during the protocol and takes classical
communication at infinite speed, so no τ can be read from the
published form's own evolution — the FR-net ratio is not merely
zero here, it is not posable as a duration read on this form at
all. (The detector-based field form, search C6, confirms the
floor's role from the other side: its printed negative
stress-energy densities SATURATE the quantum interest bound —
in a genuine field the QEI pricing is tight, not loose.)

**Also missing for any price line:** the harmonic-chain paper
prints no closed-form E_in (measurement infusion energy), so even
the pair-level price per unit delivered cannot be formed from its
pages — a second, independent evaluability gap below (iii).

## Failure protocol

- **Anatomy:** the dilution mechanism is carried, in the spin
  model, by a single shared N-body interaction term whose total
  correlation energy is charged once to one output sector.
  Field/oscillator Hamiltonians in print have local pairwise
  couplings; a receiving sector's correlation price is intensive
  (α g₁/2 here) and party-number-independent, while extraction
  decays with separation. The mechanism's load-bearing object —
  the shared interaction — is exactly what no published
  field/oscillator QET contains.
- **Mechanism-suggested follow-up (search/registration only; no
  protocol is improvised):** FU-P1192-1 — a standing search
  criterion, sibling of P119-5's form: the field analogue becomes
  posable the day a published form supplies (iii) — e.g. a
  multi-receiver extension of the harmonic-chain or detector QET,
  or a field version of Hotta's distribution protocol, with a
  printed per-receiver delivered energy and a shared-resource
  Hamiltonian. Until then the spin-model reopening (P108-5) keeps
  its stated scope: finite spin model, no field claim.
- **Reopening condition for this item:** publication of a
  field/oscillator QET meeting (i)+(ii)+(iii) in evaluable form.

## C12

An accounting/search item. Nothing FTL is claimed by any outcome;
no field claim is made for the P108-5 reopening — this verdict is
precisely that the published record does not currently support
one. INTERNAL ONLY: nothing uploaded, nobody contacted.

**Deliverables:** `results/p1192_search_record.md`,
`results/p1192_memo.md`, `results/p1192_results.json` (anatomy
reads — supplied although the verdict is NOT POSABLE, because the
registration requires the single-receiver anatomy in numbers);
scripts in `work/`: `p1192_anatomy.py`, `p1192_checker.py`
(ALL PASS on re-run).
