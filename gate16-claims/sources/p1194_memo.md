# P119-4 memo — the alignment set's two named escapes (FU-P1083-1 + FU-P1083-2)

No milestone: neither half produced a joint pass or a joint
improvement. Both escapes work mechanically; the front stands
in both. Details below; all numbers second-pathed by the
independent checker (`work/p1194_checker.py`, 245/245 PASS,
full-margins `fast=False` recomputation of every run from its
stored z).

## Verdicts

- **Half (a) — non-flat profile (FU-P1083-1):
  ESCAPE WORKS MECHANICALLY, FRONT STANDS.**
- **Half (b) — H_,φ(pi0) = 0 (FU-P1083-2):
  ESCAPE WORKS MECHANICALLY, FRONT STANDS.**

## Machinery gate (passed before either half ran)

All seven unique corpus configurations of
`phase101/results/p1015_partB_raw.json` reproduced via
`p1015_lib.canonical_terms` — worst error 8.55×10⁻¹²
(tolerance 1e-6) — and the hinge best's alignment set is
{44} with S_F = 1.000000 under the registered definition.

## Half (a) — the non-flat profile

**Pose** (run record §2, fixed before numbers):
φ(r) = wallwide(pi0, shape) + A·W(r)·sin(2π(r−10)/λ),
W the smootherstep window on [10, 20]; A ∈ [−0.35, 0.35],
λ ∈ [2, 6]; jets by the PhiProfile pattern (CubicSpline on
the 4001-point grid). FD verification (h = 10⁻⁶): d1 rel
7.24×10⁻¹⁰, d2 rel 4.74×10⁻⁷ — both < 1e-6. (At h = 10⁻⁴
the d2 FD read is 4.74×10⁻⁵; the error scales linearly in
h and is worst at r = 11.25, the window's smootherstep
join — an FD truncation artefact at the kink, not a jet
error; the spline derivatives are exact for the posed
profile, as in the PhiProfile pattern itself.)

**Non-flatness (registered test): posed at every
candidate.** |t_kin|/D_can > 1e-6 at 44/44 former plateau
points (indices 0–43) at the hinge-seeded start and at all
14 optimised candidates. The plateau is dead everywhere in
this half.

**Search:** 14 starts (≥ 12 registered), joint
least-squares on the P101-5B pattern over (z, A, λ,
ρ₀ ∈ [0, 0.05]), family B; family A read at the best
candidate. Every read: content set = the 56 subset points,
n_nondeg = 56, n_deg = 0 throughout.

**Best candidate (start 7, selection key of the run
record):** z = (1.09396088842477, −0.5286786253298396,
−1.4719328625445878, 0.43502659549969874,
0.8501116945716124, 0.08238464503952589,
−2.1859449891197795, −0.026844566778504827),
A = −0.033678153095735734, λ = 4.640050126789908,
ρ₀ = 0.04996138256328585.
subset_legal = 0.6964285714285714 (hinge: 0.5892857142857143);
EoM rel max (nondeg) = 0.999999999994964 (hinge:
0.9999999999784565); median = 0.09039800971262574 (hinge:
0.22437629566157347); health_ok = **True** (hinge: False);
Frontier A = 0.000; trap not firing (Fsum_maxabs =
0.01348). Alignment set: **empty**. Max-residual point 51
(tied within 1e-9 with 44, 50, 52), decomposition there:
t_kin = +0.07653, t_pxx = +0.05709, t_FA = +0.00488,
t_FB = +0.06008, D_can = 0.19857 — shares kin 0.385 /
pxx 0.287 / FA 0.025 / FB 0.303, S_F = 0.327.

**Hinge-seeded start (hinge z on the non-flat profile,
A = 0.15, λ = 3.0):** subset_legal = 0.000; EoM max/median
0.99886/0.80063; alignment set empty; max-residual point
46 with kinetic share 0.948 — the blend alone, at the
hinge couplings, already empties the alignment set and
moves the worst point off the plateau, at the price of
all legality.

**Family A at the best candidate:** subset_legal = 0.000
(the family-B fluid carries all of the best candidate's
legality), EoM reads unchanged, health_ok = True,
alignment set empty.

**Why neither bar is met.** JOINT PASS: Frontier A = 0 at
every candidate (the EoM max never approaches 0.02; the
smallest max over all starts is 0.866, start 12, at
legality 0.036). JOINT IMPROVEMENT: start 7 beats the
hinge on legality (0.696 > 0.589) and on health and
median, but its EoM max exceeds the hinge's by
1.65×10⁻¹¹, failing both Pareto clauses (clause 1 needs
max < hinge max; clause 2 needs max ≤ hinge max). No
other candidate is close on both axes at once.

**New binding form (named, per the verdict).** With the
plateau dead, the worst point is no longer a force
alignment: at the best candidate it is an **all-sign pin**
— every live canonical term at point 51 has the same
strict sign, so the numerator is the full D_can up to
O(10⁻¹¹) with no cancellation available from any channel,
the revived □φ included (it joins the pin instead of
opposing it). The escape removed the *force* alignment
and the front re-pinned on *total sign-coherence*. The
secondary binding form is the legality↔EoM trade: the
only candidates with EoM max materially below 1
(start 12: 0.866; start 11: 0.993) pay with legality
0.036 / 0.125.

## Half (b) — H_,φ(pi0) = 0

**Pose:** stored 'wallwide' family; constraint imposed by
parametrisation, pi0 = β_c/(2(2ξ+β₂)), in two β_c branches
([−4, −0.05] and [0.05, 4]). 14 starts (≥ 12 registered),
including the hinge best projected onto the constraint
set: z_proj = (2.756667559450937, 2.4512053601027106,
−1.8937043136728997, 0.3385988091052908, 0.870145941019083,
1.222294121969537, 0.0639057960421364,
−0.15512773896022752), with H_,φ(pi0) = 0.0 exactly and
pi0 reproduced to the last digit.

**Projected seed read:** subset_legal = 0.5714285714285714;
EoM max = median = 0.9999999999767298; health_ok = False;
alignment set **empty**; at the max-residual point (14;
tied 14–44) t_FA = 9.7×10⁻¹⁸ and the t_FB share is
0.99999999987 — the F_A channel is dead at the plateau
exactly as posed, from the first read onward.

**Best candidate (start 6, negative branch):**
z = (0.6364774799490114, −0.550546095484792,
−1.6603977857177497, 0.7104868883815072, 0.87329906344317,
1.7677186914997867, 0.016255180150389955,
−0.20395940295879322), ρ₀ = 0.04999986064344583.
subset_legal = 0.9107142857142857 (hinge: 0.5892857142857143
— the highest legality seen in either half);
EoM rel max = 0.9999999999878012 (hinge: 0.9999999999784565);
median = 0.9999999999840075; health_ok = False;
Frontier A = 0.000; trap **not firing** (Fsum_maxabs =
0.1449 ≫ 1e-9; trap subspace not met). Alignment set:
**empty**. Max-residual point 44 in the primary path,
tied within 1e-9 with **every plateau point 14–44**;
decomposition at 44: t_FA = 9.4×10⁻¹⁵, t_FB = 0.08198,
D_can = 0.08198, t_FB share 0.99999999999988.
(Start 7 ties start 6 on legality, 0.9107, with a better
median 0.99972 but a worse max; the registered key
selects start 6.)

**Phase-118 boundary: NOT pressed.** |β_c| at the best
candidate is 0.5505; the closest approach of any run is
|β_c| = 0.4709 (start 3). The search never came near the
0.05 fence; the β_c = 0 slice was not entered.

**Why neither bar is met.** JOINT PASS: Frontier A = 0
everywhere (EoM max ≈ 1 − 10⁻¹¹ at all 14 candidates).
JOINT IMPROVEMENT: starts 6 and 7 beat the hinge on
legality by a wide margin (0.911 vs 0.589) but their EoM
maxima exceed the hinge's by 9.3×10⁻¹² and 1.1×10⁻¹¹
respectively, failing both Pareto clauses.

**New binding form (named, per the verdict).** The
**single-channel pin**: on the flat plateau □φ ≡ 0 and
t_pxx ≈ 0, and the constraint kills t_FA at pi0 exactly,
so at plateau points the canonical EoM *is* t_FB alone —
rel = |t_FB|/D_can = 1 wherever no other channel is live,
which is the whole plateau (tie set 14–44 at the best
candidate). Killing one force channel did not free the
balance; it removed the only term that could oppose the
other. The median tells the same story: ≈ 1.000 at every
positive-branch candidate and at the seed.

**Anatomy — the one re-formation (start 8, not the best
candidate).** Its alignment set is {19} and does carry
its max-residual point (rel = 1.0 exactly) — but the
mechanism is not H_,φ: P_X at point 19 is 1.73×10⁻⁸, so
both force terms are blown up by the 1/P_X division
(t_FB = −1.82×10⁵, t_FA = −1.99×10², same sign,
S_F = 0.99972). Alignment can re-form through a P_X → 0
denominator blow-up even with H_,φ(pi0) = 0; that basin
is a P_X-crossing configuration (PX_min = −1.15×10⁻⁵,
health_ok = False), not a plateau-force effect.

## Failure protocol — anatomy and follow-ups

Both negatives have the same anatomy at one remove: the
front's worst point is a point of *zero available
cancellation* — on the flat profile because only aligned
forces are live (P108-3), off it because either all live
terms share a sign (half (a)) or only one term is live
(half (b)). Mechanism-suggested follow-ups, for the
queue:

1. **Compose the two escapes**: the H_,φ(pi0) = 0
   constraint *on* the non-flat profile. Half (b) shows
   t_FB needs an opposing live channel at plateau points;
   half (a) shows □φ can be that channel but joined the
   pin at the searched candidates. The composed pose is
   the direct test of whether a live □φ of the *opposing*
   sign is attainable at the pin points.
2. **Sign-targeted profile**: a blend whose □φ changes
   sign across the inner shell (more zero crossings than
   the single-sine family searched), posed so the kinetic
   term opposes −μφ at the radii where the pin migrates
   (outer shell, points 44–55, in half (a)).
3. **P_X floor as a posed guard**: exclude the
   P_X → 0 basin (start 8, half (b)) explicitly in future
   searches on this front (|P_X| ≥ a stated floor at all
   subset points), so alignment-by-blow-up cannot
   re-enter through the denominator.

Closure is not claimed for the coupling-force front: the
two registered escapes are spent and both re-pin, but
follow-up 1 is a genuinely new pose (the composition),
not a revisit of either half alone.

## C12 and scope

Pre-existing walls at β = 1.1; no transport claim; a moved
front is not a legal wall. All reads are the registered
56-point subset form (content set stated on every read:
56 points, n_nondeg = 56, n_deg = 0 at every candidate in
both halves). float64. INTERNAL only; nothing uploaded,
nobody contacted. CHECKPOINT119.md was not edited.

## Files

- `results/p1194_run_record.md` — poses fixed before numbers.
- `results/p1194_results.json` — gate, both halves' runs,
  seeds, best candidates, family-A read, verdicts.
- `work/p1194_lib.py`, `work/p1194_gate.py`,
  `work/p1194_halfA.py`, `work/p1194_halfB.py`,
  `work/p1194_assemble.py`, `work/p1194_patch_ties.py` —
  machinery and drivers.
- `work/p1194_checker.py` + `work/p1194_checker_output.json`
  — independent checker, 245/245 PASS.
- `work/p1194_gate.json`, `work/p1194_halfA_ckpt.json`,
  `work/p1194_halfB_ckpt.json` — gate record and search
  checkpoints.
