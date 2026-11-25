# P72-2 — Quantum Energy Teleportation, Priced — Memo

## Plain-language summary

Quantum energy teleportation does produce a small patch of negative
energy at Bob's end — that part is real, and the numbers below confirm
it from the inventor's own published formulas. But it is not free, and
it is not a shortcut around the programme's negative-energy budget.
Alice's measurement alone injects about six times more energy than
Bob ever gets out (at the standard point: 0.707 in, 0.115 out). Before
that, the shared entangled state itself has to be prepared, and the
correlations it stores are worth more energy than Bob extracts: read
against an ordinary uncorrelated reference — the reference the
Ford–Roman bound uses — Bob's end never actually goes negative at
all. It stays positive by +1.30 energy units while delivering its
−0.115 relative to the entangled state's own zero. In other words,
the negative energy is bought and paid for inside the resource; the
protocol moves the cost into the pre-shared entanglement and into
Alice's measurement, it does not evade the price. Total counted cost
is at least 9 times the negative energy delivered (18 times under
the second reference accounting). **Filed as relocation.** Separately,
and as Phase 2 already recorded: the message that makes it work is an
ordinary classical signal, so nothing arrives faster than light —
this filing is about price, not transport.

## Model and controls

Hotta's minimal two-qubit QET model (Phys. Lett. A 374, 4165 (2010);
arXiv:1002.0200), fixed in `p722_run_record.md` before any number:
H = H_A + H_B + V with H_A = H_B = hσ^z + h²/√(h²+k²),
V = 2kσ_A^xσ_B^x + 2k²/√(h²+k²); projective σ_A^x measurement at
Alice; Bob's optimal unitary (source Eq. (7) optimum). Only the
source's printed formulas were evaluated, at h = 1, r = k/h ∈
{0.5, 1, 2} (named evaluation points, not a scan).

Controls (all pass): at h = k, E_A = 0.70711 and E_B = 0.11475,
matching the review-quoted 0.707 / 0.115; direct evolution of the
post-operation state under the printed H gives
⟨H_B + V⟩(0) = −E_B to 1e-9 at every point; E_B ≤ E_A everywhere
(the source's own bound); the projective measurement consumes
exactly the ground state's entanglement, ΔS_AB = S_ground, by
direct evaluation of Eq. (9).

## Full bookkeeping table (energies in units of h, per consumed copy)

| Quantity | r = 0.5 | r = 1 (h = k) | r = 2 |
|---|---|---|---|
| E_A — Alice's measurement injection, Eq. (4) | 0.89443 | 0.70711 | 0.44721 |
| E_B — negative energy delivered at Bob (−E_B in H_B+V sector) | 0.07257 | 0.11475 | 0.09818 |
| E_B / E_A | 0.0811 | 0.1623 | 0.2195 |
| Ground entanglement S_ground (ebits) | 0.29812 | 0.60088 | 0.85049 |
| Entanglement consumed ΔS (ebits/copy) | 0.29812 | 0.60088 | 0.85049 |
| (a) E_B per ebit consumed | 0.24344 | 0.19097 | 0.11544 |
| (b) Prep price, separable-minimum gap E_prep^(sep) | 0.23607 | 0.32843 | 0.22214 |
| (b′) Prep price, marginal-product reference E_prep^(marg) | 0.44721 | 1.41421 | 3.57771 |
| Classical leg energy | ≥ 0 (not a printed formula; latency ≥ D/c, leg ≤ c) | ≥ 0 | ≥ 0 |
| (c) Total counted (deciding: E_prep^(sep) + E_A) | 1.13050 | 1.03553 | 0.66935 |
| (c) Total per unit delivered, deciding | **15.58** | **9.02** | **6.82** |
| (c′) Total per unit delivered, marg reference | 18.49 | 18.49 | 40.99 |
| τ_pulse (ħ/h; first zero-return of ⟨H_B+V⟩(t)) | 0.23272 | 0.18537 | 0.11725 |
| E_legal(τ_pulse) = (3/32π²)ħ/τ_pulse | 0.04082 | 0.05124 | 0.08101 |
| FR-raw ratio R_raw = E_B τ_pulse / [(3/32π²)ħ] | 1.778 | 2.239 | 1.212 |
| Net Bob-sector energy vs uncorrelated ref: E_prep^(marg) − E_B | +0.37464 | +1.29947 | +3.47953 |
| FR-net ratio R_net (resource on the books) | **0** | **0** | **0** |

## The deciding comparison

Two deciding lines, both fixed in the run record (§7) before
computing:

1. **Price line.** The total bookkeeping per unit of negative energy
   delivered is 9.02 at h = k (6.82–15.58 across the evaluated
   points) under the conservative separable-minimum preparation
   price, and 18.49 at h = k under the marginal-product reference.
   Both are ≥ 1 by a wide margin — indeed Alice's injection alone
   (E_A/E_B = 6.16 at h = k) already overpays the delivery. The
   delivered negative energy is priced at well above the W6 pulse
   price for its magnitude: nothing is obtained below cost.

2. **Pulse line, resource on the books.** Read relative to Hotta's
   entangled-ground zero, the local pulse's |ρ|τ⁴ product exceeds
   the free-field Ford–Roman coefficient by a factor R_raw =
   1.21–2.24. That raw read is reported, not hidden — and it is not
   the deciding read, for a stated reason: the Ford–Roman bound is
   referenced to the uncorrelated vacuum, while Hotta's zero is the
   *entangled ground state*, a state whose Bob-sector correlations
   store E_prep^(marg) = 2k²/√(h²+k²) of energy above the
   uncorrelated reference (marginal-product state). With the
   resource on the books, Bob's sector after extraction sits at
   E_prep^(marg) − E_B = +1.29947 (h = k), +0.37464 (r = 0.5),
   +3.47953 (r = 2) relative to that reference — positive at every
   evaluated point. No negative pulse relative to the uncorrelated
   reference exists: R_net = 0 ≤ 1. The apparent raw excess is
   exactly the correlation energy of the resource being spent,
   i.e. the cost was relocated into the pre-shared state, not
   evaded. (This is the same reference distinction the programme
   met in the A5 discussion: a bound system's state energy is not
   a free-field pulse, and pricing it against the wrong zero
   manufactures a factor-of-two-scale excess.)

**Does any step evade the pulse-pricing assumptions?** No. Every
step's cost is on the books above: preparation (two references,
deciding line uses the smaller), measurement injection (Eq. (4)),
and the classical leg (energy ≥ 0, latency ≥ D/c, speed ≤ c by the
protocol's own construction — stated per Phase 2 §W7(i), not
relitigated). The negative excursion at Bob is an internal
redistribution inside a system whose total energy stays ≥ 0
(H ≥ 0 in the source; post-protocol total = E_A − E_B > 0). The
mechanism that makes the local read look cheap — measuring the
pulse from the entangled ground's zero instead of the uncorrelated
vacuum's — is precisely the relocation the filing names.

## Verdict (registered form)

**FILED AS RELOCATION** — the total bookkeeping prices the delivered
negative energy at ≥ the W6 pulse price for the same magnitude and
duration. Deciding lines in numbers (h = k): total price per unit
delivered = 9.02 (conservative preparation price; 18.49 under the
marginal-product reference), and the resource-on-books pulse ratio
R_net = 0 against the bound 1, with Bob's sector net-positive by
+1.29947 energy units relative to the uncorrelated reference.
Checker: `work/p722_checker.py` recomputes every verdict-carrying
number from `results/p722_results.json` — 44/44 assertions PASS.

This is a filing under C12 construction-inclusive accounting, not a
transport claim. QET's classical leg is ≤ c by the protocol's own
construction; earliest Bob-side action after Alice's decision is
≥ D/c, the Krasnikov/GJW pattern of Phase 22 / Phase 2 §W2.

## Failure Protocol — anatomy and follow-ups

No formula failed to pose: the item did not resolve NOT POSED.
The one near-miss, anatomised: the raw pulse read R_raw > 1
(1.21–2.24) would, if the entangled-ground zero were mistaken for
the vacuum zero, misfile this item as a loophole. Anatomy: the
excess factor is bounded by, and accounted for by, the correlation
energy E_prep^(marg)/E_B ≥ 6.2 stored in the resource's Bob sector;
subtracting the resource (FR-net) removes the excess entirely at
every point, with margin +0.37 to +3.48 energy units.

Follow-ups:
- **F1 (field version).** Price Hotta's harmonic-oscillator / field
  QET the same way if its published E_B density and correlation
  energy can be fixed in evaluable form: the deciding question is
  whether the field version's net-of-resource local density also
  stays non-negative against the vacuum reference at its own
  correlation length and time. (Not run here: this item's
  registration priced the qubit model; the field formulas were not
  fixed in the run record.)
- **F2 (species/copy scaling).** N copies deliver N·E_B at N times
  the total price — the price ratio is copy-invariant by linearity
  of the printed formulas, so no multi-copy arrangement changes
  this filing; a future item could verify the same for the
  three-qubit QET variants reported in the literature, whose
  higher E_B/E_A efficiency (~0.675 of the interaction scale in
  review reports) still keeps E_A > E_B and the same reference
  structure.
- **Reopening condition.** This filing reopens only if a published
  QET variant exhibits, in evaluable printed form, a Bob-sector
  energy that is negative relative to the *uncorrelated* reference
  after its own preparation and injection costs are counted —
  i.e. R_net > 1 with the resource on the books.
