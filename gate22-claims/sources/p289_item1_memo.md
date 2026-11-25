# P289 ITEM 1 MEMO — THE DECIDING READ: §4b ON THE AXIS A
# MEMBER (A BACKGROUND CONSISTENT BY CONSTRUCTION)

Registration: `work/p289_registration.md` (verdict forms
and the materiality threshold fixed before computation).
Controls: `results/p289_controls.json`. Deciding read:
`results/p289_item1.json`, per-point records
`work/p289_item1_records.json`. Independent checker:
`work/p289_check.py`, 14/14 PASS,
`results/p289_verify.json`.

## §1 CONTROLS (all PASS, before the deciding read)

- **C-S4B-J1** (instrument): the verbatim p278 lib on the
  stored J1 full state reproduces Phase 268's deciding
  read at diff **0.0** — median 0.16762395022464124, max
  715629.9865333225.
- **C-S4B-M0** (parametrisation): the member lib at Δ = 0
  with posed J reproduces that read at **per-point diff
  0.0** over all 1991 records. The two registered sites
  (𝒜 family in A_vec; J_bg in profiles_vec) are the only
  differences from the verbatim lib (diff exhibited in
  the run record); at the incumbent member they are
  bitwise inert.
- **C-PROF-M**: 𝒜(θ; +0.15) vs Phase 287's saved Auu_new —
  max abs diff 5.6×10⁻¹⁷ (the analytic family formula is
  the saved profile); Δ = 0 gives 𝒜 ≡ −0.3 exactly and
  matches Auu_inc at 0.0; J_derived finite on all 181
  points, range [−0.889383, −0.530265]; the PCHIP
  interpolant reproduces J_derived at its nodes at 0.0.
- **C-STATE-M**: member state shapes (1601, 11521) ×3,
  times [0, 1.0]. **C-MD5**: protected engines identical
  throughout.

## §2 THE DECIDING READ

Member lib (Δ = +0.15, J = PCHIP(J_derived)) on
`phase288/work/p288_member_state.npz`; 1991 points,
hs = (0.025, 0.05, H_AUD):

**median 0.16917676136946494, max 808773.4788442705**
(bar 0.02 / 0.02). 30/1991 points ≤ 0.02; **no instant
passes** (per-instant medians U-shaped: 0.1426 at t = 0,
minimum 0.1273 at t = 0.4, 0.2002 at t = 0.8, 0.1888 at
t = 1.0; every per-instant max ≥ 807,610). Companion
(halved stencils, t ∈ {0, 0.5, 1}): 0.1530062103196459 /
76.58760054403888. Interior (1969 pts): median
0.1676070101062429, max 17.656918970165584 — the headline
max is the pole-adjacent θ = 0.02 statistic (worst five
points all at θ = 0.02, t ∈ [0.6, 1.0]), as in every
prior row. Checker spot-recompute at t ∈ {0.0, 1.0}
reproduces the stored records at diff 0.0 in a fresh
process, worst point included.

## §3 THE SIX-ROW TABLE (bar 0.02 / 0.02)

| subject | throat | median | max |
|---|---|---|---|
| prescribed J1 (incumbent bg) | YES | 0.167624 | 715,629.99 |
| att-solved | **NO** | 0.091008 | 714,294.11 |
| projected θ-flat (incumbent bg) | YES | 0.203356 | 658,563.27 |
| successor att₁ (incumbent bg) | YES | 0.196485 | 750,246.02 |
| projected successor (incumbent bg) | YES | 0.242321 | 633,905.82 |
| **Axis A member (consistent bg)** | **YES** | **0.169177** | **808,773.48** |

The member's median sits inside the throat band
[0.167624, 0.242321], 0.93% above its lowest row (J1);
its max is the table's largest (+13.0% over J1's) — the
pole-adjacent single-point statistic in every row. The
five prior rows all sat on the background Phase 285
proved O(1) TOV-inconsistent; the sixth row's background
is audit-clean by construction (Phase 287: max|δP₂| =
1.047×10⁻⁶, zero of 181 θ above the floor).

## §4 THE ANATOMY — EVERY GROUP FELL; THE STATISTIC DID NOT

Term decomposition (median |div| at argmax), member vs
J1: gamma_trace 0.015325 vs 0.040351 (**×0.380**);
deriv_th 0.026423 vs 0.035209 (×0.750); gamma_second
0.035799 vs 0.046999 (×0.762); deriv_u 0.027196 vs
0.034921 (×0.779); deriv_t 8.46×10⁻⁷ vs 8.46×10⁻⁷ and
deriv_phi_director 0.000320 vs 0.000320 — the two
smallest groups bit-identical (each median attained at
a single t = 0.3 record; see §5). The director group is
innocent in the sixth row as in all five before it.

So the background repair demonstrably carried
term-level residue — most sharply in gamma_trace — and
the deciding statistic did not follow: rel_c is a
per-point max-norm of the SUMMED divergence vector, and
the groups' reductions do not compose into the sum's
norm, which re-forms at 0.169. This is the same
non-composition the successor row showed in the other
direction (Phase 282: the targeted group fell ×5.9, the
median rose), now confirmed from the background side.

## §5 TWO FACTS OF RECORD ABOUT THE COMPARISON

(i) **The evolved state is the same state.** The member
march's MU/U/MTT are bit-identical to the J1 march's
(verified array-by-array in this phase): the evolution
is deformation-blind (Phase 269 C1; Phase 288's design —
the background change is confined to the read layer).
The six-row comparison's last two rows are therefore a
pure background swap on one evolved geometry: posed,
O(1)-inconsistent background vs derived, audit-clean
background — and **zero of the 1991 rel_c values are
identical between the two reads**. The background swap
moves every point's residue and moves the verdict not
at all.

(ii) **The verdict is interpolant-independent.** The
member's J enters through a PCHIP interpolant (the
machinery's own class; the one new instrument element
vs the five prior rows). Recomputed with a natural
cubic spline and with piecewise-linear interpolation,
the median is 0.16917676136946494 under all three
(maxima 808773.4788 / 808773.4721 / 808773.4765; n ≤
0.02: 30 / 29 / 29) and the verdict form is the same
under all three. The bit-identical group medians of §4
are an order-statistic property of the shared state,
not a loading artefact: the checker reproduced the
member records from the member state and lib in a
fresh process at diff 0.0, and fact (i) holds
array-by-array.

## §6 VERDICT (registration §6, decided in order)

PASSES does not fire (no instant passes). FALLS
MATERIALLY does not fire (median 0.169177 ≥ the
registered threshold 0.167624). **§4b FAILS UNMOVED.**

**The background-borne explanation dies.** Phase 285's
candidate contributor to the five-row invariance — the
shared background's O(1) TOV inconsistency — is removed
for this subject, on the same evolved state, and the
failure stands at the table's level. The priced
residue: the inconsistent background did carry
term-level residue (gamma_trace ×0.38 under repair),
but it was not the failure's carrier. The carrier is
the configuration class itself: §4b's failure is now
invariant under pose, evolution law, att shape,
projection, **and background consistency** — six rows,
no blank cells, every throat row failing on the bulk
statistic by ~an order of magnitude over the bar.

**Standing restated.** Stage D form 2 stands for the
Axis A family as it stood for the incumbent and
successor families. The member's genuine gains are
untouched by this verdict and stand at read grade:
audit-clean background by construction, t = 0 binding
margin +24.7% over the incumbent (Phase 287), bracket
(0.575, 0.58125] — longer than J1's (Phase 288). What
remains open, in order: (1) Gate-23-pattern
certification of the member's bracket — a completeness
item, insufficient alone for construction wording
while §4b fails for every read subject in the class;
(2) p1592 — unchanged, gates programme-level
sustainment wording regardless; (3) the outer debt —
Gap 1's extension (Phase 260), whose registered front
door (Axis B, a constitutive closure) died at counting
cost in Phase 284 and whose deficit stands at one
scalar relation per radial order. The Phase 283
redesign programme has now spent all three axes: B
dead at counting, C dead at audit, A run its full
course (pose, march, §4b) — it produced the class's
best pose and did not move §4b. Any further §4b
progress requires leaving this configuration class,
not another variation within it.

## §7 FENCES

Read grade only; the read judged only (no tuning of
the member, background, march, interpolant, point set,
or stencils against the read; the §5 sensitivity arms
are diagnostics, not verdict inputs). No certification
claimed; the member's Gate-23-pattern debt rides in
full. No traversability, construction, or
programme-level wording.
