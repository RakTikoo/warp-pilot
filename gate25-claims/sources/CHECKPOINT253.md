# CHECKPOINT 253 — TWO NAMED FOLLOW-UPS OF PHASE 250

Phase 250 named two residuals: the spinor gap in Phase 31's sign
identity (the library's last untested sector against a drive's
T_req), and the low-shear kinematics question left by Natário's
ring cancellation. This phase ran both, registrations and verdict
forms before computation, controls first. Item memos:
results/p2531_memo.md, results/p2532_memo.md; registrations,
drivers, checkers, results under work/ and results/.

## FTL VERDICT (leading): NO — with one obstruction REMOVED

No grouped joint pass anywhere; Frontier A unchanged; drive
step 1 remains unachieved. But the drive's sourcing obstruction
is no longer complete over the library: Item 1 breaks the sign
identity on spinors (below). The sign leg of the drive's
sourcing problem REOPENS on exactly one sector. Every other leg
— full tensor match against a non-Type-I T_req, EC health of a
sourcing configuration, budget/QI pricing — remains open and
unpriced for that sector. This is an obstruction removed, not a
drive sourced.

## ITEM 1 (P253-1) — SPINOR SOURCING TEST: SPINORS BREAK THE IDENTITY

Verdict form fired: **SPINORS BREAK THE IDENTITY** (the second
registered form). Controls PASS, diff-0.0 class: stored Phase 235
rows exact; stored That contracted with k* reproduces the stored
NEC worst values to ≤5×10⁻¹⁸ at all four deciding sites.
Independent checker (Weyl representation, separately coded):
28/28 PASS, deciding value reproduced.

**The algebra.** The g_ab·L term drops out of the null
contraction with no field equations needed (as with radiation).
The sign conclusion, however, DOES need them — off shell
T(k,k) is linear in the jet k·Dψ and no identity exists. On
shell, for a Dirac superposition, T(k,k) is the Hermitian form
c†Nc with N = A∘C: A is a Gram matrix (PSD — B = γ⁰(γ·k) has
eigenvalues {0,0,2,2}), but C_ij = ½(f_i + f_j), f = k·p, is
INDEFINITE whenever modes project differently onto k (deciding
pair det C = −28.0). N is therefore indefinite. The negativity
is a pure multi-mode interference effect: a single mode always
has T(k,k) ≥ 0; superpositions need not. This is structurally
different from every covered sector — 2-forms, canonical
scalars (Phase 31) and null dust/radiation (Phase 250 L2) are
sum-of-squares; the Dirac form is a Gram matrix Hadamard-mixed
with an indefinite frequency form.

**The deciding configuration.** m = 1, three positive-frequency
on-shell plane waves (Σ|c|² = 1, u†u = 2E; f = k*·p spanning
0.815 / 11.401 / 3.647): **T(k*,k*) = −10.8785** at the β = 1.1
worst site (r = 12.84), Dirac residuals ≤3.5×10⁻¹⁵, with
POSITIVE local density ρ_spinor = +2.2404 — the negative null
contraction is not bought with negative density. The massless
case also breaks (−8.9847). Random corroboration: 0.4% of 2000
random two-mode draws are negative.

**Pricing.** The unit-normalised configuration carries 2861×
the worst site's full NEC deficit (−0.0038018); scaled by
amplitude² s² = 3.49×10⁻⁴ it carries the deficit exactly, at
ψ†ψ = 7.7×10⁻⁴ and ρ_spinor = +7.8×10⁻⁴. Same class at the
other sites: s² = 3.45×10⁻⁴ (r = 12.5), 1.51×10⁻⁴ (r = 15.0),
4.49×10⁻⁴ (β = 1.5 worst site).

**Scope and fences (on the memo's face).** The classical/quantum
dependence is confined to negative-frequency modes (excluded by
registration) and Grassmann point-values (no sign until a state
is chosen) — neither is used by the deciding configuration, so
the CANNOT-BE-POSED form does not fire. Phase 72 scope
correction (stated in the memo; its files untouched): Phase 72
closed spinor THROATS on EC/domain grounds, and its own audit
exhibits on-shell Dirac NEC violation; any reading of Phase 72
as closing spinor sourcing generally overstates its scope.
Fences: this decides the SIGN LEG ONLY. Still open for a spinor
sourcing attempt: the full tensor match against the drive's
non-Type-I T_req, global on-background existence and
normalisability of the configuration, full EC health of the
posed field, and budget/QI pricing.

## ITEM 2 (P253-2) — LOW-SHEAR KINEMATICS: SHEAR AND TRANSPORT ARE LOCKED

Verdict form fired: **SHEAR AND TRANSPORT ARE LOCKED** (the
second registered form). Family as registered: Stokes-stream-
function shifts, S_tot = ΣaₙSₙ over 5 atoms (quintic [10,20]
Natário control, septic [10,20], wide quintic [8,22], narrow
quintic [12,18], flat S₁,₁), dials on the simplex, ±1% v_eff
band, primary objective median K² on SET-244. Bounded scan:
26 members, 96 s — no kernel spec owed.

**Controls.** C1/C4 reproduce P250-1 at record precision
(Natário E_neg −22.450425, median q 10.4814, Type-I 0.009636,
v_eff exact; Alcubierre E_neg −2.590291). C2 divergence
≤7.3×10⁻¹⁶ across all 26 members; C3 flat limits exact. ONE
DISCLOSED SUB-CHECK FAILURE: the registered auxiliary identity
ρ = −K²/16π (raw symmetrised gradient) is wrong for this metric
form — the ADM lapse is α = √(1+|v|²) ≠ 1. The lapse-corrected
identity ρ = −K_ijK^ij/(16πα²) verifies to 1.8×10⁻¹². The
verdict is read off full maps, not the proxy; the JSON's
controls_pass=False is solely this sub-check, explained on the
memo's face.

**Best member: the pure wide atom (quintic on [8, 22])**,
v_eff +0.875% (in band). β = 1.1 headlines vs Alcubierre /
Natário:

| quantity | Alcubierre | Natário | best member |
|---|---|---|---|
| median \|ρ\| | 4.463×10⁻⁵ | 6.372×10⁻⁴ | **3.003×10⁻⁴** |
| E_neg | −2.590291 | −22.450425 | **−11.368744** |
| median q | 37.19 | 10.48 | **2.87** |
| Type-I fraction | 0.0 | 0.009636 | **0.013701** |
| R_diff (τ=10) | 2852 | 21523 | **6189** |

Median |ρ| is 6.73× Alcubierre's — the registered 2× bar FAILS
— though 2.1× better than Natário, and Natário's budget is
halved. Caveats on the face: denominator ≤0 share worsens
(0.922); at β = 1.5 the same dials drift to +1.42% v_eff
(outside band — transfer read only).

**The ring survived — strengthened.** All 93 q ≤ 1 points and
91 Type-I points sit on two adjacent nodes r = 13.293/13.537
(Natário: one node); ray flux dip 1.77×10⁻⁴ at r = 13.25 (vs
Natário's 1.39×10⁻³). Cancellation and shear ARE separable.
What is locked is shear↔transport: the shear floor falls only
along the width dial (median K² 0.0477 → 0.0205 as v_eff
deviation runs 0 → +0.88%), because ~76% of K² is transverse
components forced by ∇·v = 0 from B = rS′/2 — the same S′ whose
on-axis profile carries the transport. Shape dials buy ≤1.42×;
the septic (higher-regularity) atom is worse than the quintic
everywhere — the outer-joint swing was not the shear's home.

## SYNTHESIS

- The sourcing map is redrawn. Phase 31's identity, after
  Phase 250, covered every library sector except spinors; it
  now has a priced counterexample sector. The drive's sign leg
  — for 220 phases the cleanest single obstruction — is open
  again, on spinors only, at the sign level only. Everything
  downstream of the sign leg (type match, health, budget) is
  untouched and still hostile: T_req is non-Type-I with a
  complex spectrum, and Item 1 prices nothing there.
- The kinematics axis is priced to its floor in this family:
  flux cancellation is a dial (ring retained and strengthened
  in the best member), shear is not — it is the transport's own
  gradient, transverse-forced by the divergence-free condition.
  Within divergence-free axisymmetric stream-function shifts,
  the cheapest drive still pays 6.7× Alcubierre's median |ρ|
  and 4.4× its budget. Leaving the family (non-axisymmetric,
  or expansion traded against shear) is outside this item's
  scope and is the only direction the lock does not cover.
- Net for the drive line: one door reopened (spinor sign),
  one corridor surveyed to its end (divergence-free
  kinematics). Neither moves drive step 1: an honest front
  pass is still owed, and no item here is one.

## NAMED FOLLOW-UPS (none launched)

(i) The spinor sourcing attempt proper: full tensor match of a
Dirac configuration against T_req at the deciding sites, EC
health of the posed field, and budget/QI pricing — the four
fences Item 1 left open, in that order.
(ii) Gate-grade re-judgement of the spinor break, if the parent
wants the reopened sign leg at gate scope before (i) is built
on it.
(iii) Family extension along the only dial that paid: shells
wider than [8, 22], priced against the v_eff band drift seen
at β = 1.5.
(iv) Out-of-family kinematics: non-axisymmetric stream
functions, or expansion-permitted shifts trading ∂·v against
transverse shear — the lock's stated exterior.

Nothing was appended to NEW_PHYSICS_LEDGER.md; nothing external
was launched; writes are inside phase253/ only.
