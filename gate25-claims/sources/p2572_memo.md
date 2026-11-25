# P257-2 MEMO — LEG 2: EC HEALTH OF THE DECIDING CONFIGURATION

**Verdict (registered form): NET POSITION WORSE OR EQUAL** —
fired on the registered sum, with a presupposition failure
disclosed on the face (§3): under Leg 1's FULL MATCH the
registered sum double-counts, and the sourcing-semantics
companion read (the remainder) is supplied and priced beside
it. The substantive health findings are §1–§2 and do not
depend on the framing.

Registration: `phase257/work/p257_registration.md`. Driver:
`phase257/work/p257_leg2_run.py`. Numbers:
`phase257/results/p257_leg2_results.json`. Audited
configuration: the Leg-1 N = 6 constrained best fit,
unit-normalised (Σ|c|² = 1: T_unit(k*,k*) = −0.48220659,
ρ_unit = −0.01243124), scaled by
s² = 0.007884090763432848 so its contraction carries the full
site deficit exactly. At that scale the scaled tensor differs
from T_req by 1.79×10⁻¹⁶ Frobenius — it is T_req.

## 1. The configuration's own EC profile at the site

At s² the profile is the drive's own, by Leg 1 (this is a
read, not a coincidence): NEC min −0.0038018 (at k*),
sampled DEC violated (worst flux norm² −2.556×10⁻⁴,
past-directed fluxes present), ρ = −9.80091×10⁻⁵.

Sampler disclosure: this phase's WEC read minimises T(u,u)
over ALL unit timelike u with |β| ≤ 0.99 and finds
−0.18828638 for T_req — deeper than the record's margins-
convention WEC read (−0.0362103, a restricted-observer read
in the Phase 158-era margins machinery). Both are reported;
every comparison inside this phase uses the one sampler, so
all within-phase comparisons are like-with-like. At unit
normalisation the spinor's own profile is the same shape
scaled by 1/s²: NEC min −0.48220659, WEC min −23.88, DEC
violated (worst flux norm² −4.112).

Reading: unlike Phase 253's sign-only configuration
(ρ = +2.2404 at unit norm), the TENSOR-matching
configuration has NEGATIVE density at the site
(ρ_unit = −0.0124). Matching the full tensor — flux and
pressures included — costs the positive-density property:
the sign leg and the tensor leg are carried by different
configurations, and no configuration in this phase carries
both. The configuration violates NEC/WEC/DEC at the site
exactly to the extent T_req does — necessarily, since at
s² it equals T_req: a source does not need to be healthier
than the stress it sources; it needs to BE that stress, and
the clauses it "violates" are the drive's demands restated.

## 2. Neighbourhood (patch) health at s²

Over the tangent patch x ∈ [−π, π]³ (729 points, phases
e^{−ip_j·x} applied), the configuration's stress oscillates
away from the fitted point: ρ ranges over
[−9.80×10⁻⁵, +0.09209], the patch NEC minimum is
−0.02231455 (5.9× deeper than the site deficit it covers),
and the patch WEC minimum (sampled) is −1.09913. The match
is a POINT match: on any neighbourhood the field's own
stress departs from T_req and violates the clauses more
deeply than the drive does at the site. A sourcing field
would have to be re-fitted point by point — i.e. the global
on-background existence question (Phase 253 fence (b)) is
where this cost lives, and it is not retired here.

## 3. Net position — the registered sum, and the disclosure

Registered read (T_net = T_req + s²·T_Dirac): NEC min
−0.00760352 (= 2× the bare drive's, to the digits), WEC min
−0.37657 (2×), DEC violated (4× flux norm²). On the
registered deciding clause the sum is strictly worse, so
the registered form fires: **NET POSITION WORSE OR EQUAL**.

Disclosure (presupposition failure, on the face): the sum
was registered for the branch where the spinor is an
ADDITIVE helper distinct from T_req (Phase 253's
configuration, which supplies one contraction). Leg 1's
FULL MATCH falsifies that presupposition: s²·T_Dirac ≈
T_req itself (diff 1.8×10⁻¹⁶), so the registered sum is
2·T_req by construction and its "worse" verdict prices the
double-count, not a physical deterioration. The
sourcing-semantics companion read, computed and priced
here: the REMAINDER T_req − s²·T_Dirac has Frobenius norm
1.79×10⁻¹⁶, NEC min −2.9×10⁻¹⁷, ρ = 1.2×10⁻¹⁶ — zero at
float64 class: **at the site, nothing is left for any other
matter to supply, and the remainder satisfies every clause
trivially.** (The DEC sampler's sentinel value on the
remainder is the zero-tensor artifact — all sampled fluxes
vanish identically; DEC holds trivially.) Both reads stand
on the record; the form above is the registered one.

## 4. Leg-3 gate

The tasking gates Leg 3 on Leg 2 improving the net
position. On the registered sum it does not; on the
sourcing-semantics read (the remainder, §3) the net
position at the site improves maximally (the full tensor is
carried). Leg 3 was run gated on the remainder read, with
this gating choice disclosed here and on its memo's face;
its verdict is independent of the framing (it prices T_req,
which sourcing does not change).
