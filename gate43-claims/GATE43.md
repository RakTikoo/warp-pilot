# GATE-43 — Independent re-judgement of the Phase 389 claim set

Charged at ledger entry 990 (2026-11-26). Phase 389 claimed that
381's dwell→harvest fixed point is not a local optimum of the
stationary level surface: a per-profile stationary scaling of the
harvested centre H2, in a direction neither the dwell cycle nor the
harvest ever searched, improves the band stationary joint level
from −1.942246×10⁻⁴ to −1.757074×10⁻⁴. This gate re-judges that
claim set with fresh machinery only, every deciding value
reproduced independently on the VM frame of record.

## Verdict

- **(a) The mixed centre and its level −1.757074×10⁻⁴:
  SURVIVES.** Reproduced at the stored argmin points at roundoff
  (NEC diff +5.4×10⁻²⁰; DEC diff −8.1×10⁻¹⁹); controls reproduced
  (see §2). The raw sampled NEC statistic carries a frame-
  convention band of ±~3×10⁻⁶ at non-Type-I points (§1, C-10);
  the claim's deciding values sit at named points and reproduce
  there exactly.
- **(b) Pointwise-grade survival: SURVIVES RESTATED.** The exact
  worst-null at the NEC argmin reproduces at roundoff
  (−1.7703703917379299×10⁻⁴, diff +8.1×10⁻²⁰), but the margin
  over the bar computed from the phase's own stored numbers is
  **+1.7188×10⁻⁵**, not the +1.721×10⁻⁵ carried in the charge
  and the checkpoint prose. The substance stands; the figure is
  corrected (§2).
- **(c) The end-clamp re-read at the mixed centre: the margin
  SURVIVES clamping** — the opposite of the H2 outcome under
  G41-E. Clamped joint level −1.766963×10⁻⁴ (NEC-carried,
  r = 12.561), clamp cost 1.03×10⁻⁶; margin over L_stat(H2)
  +1.7528×10⁻⁵ survives; margin over the dwelling ceiling
  +3.3242×10⁻⁵ survives. Rider issued as G43-E (§4).
- **(d) The classification claim: SURVIVES.** The gate's own
  125-point cube and quadratic fit reproduce the gradient at
  H2 with the stored signs and magnitudes (gate
  (−1.089, +1.108, +0.830)×10⁻⁴ per unit μ; stored
  (−1.096, +1.115, +0.821)×10⁻⁴; per-component diffs
  ≤ 8.4×10⁻⁷ against a fit residual of 2.1×10⁻⁵), and the
  Hessian is all-negative in both fits. 381's fixed point was
  the iteration's, not the surface's (§3).
- **(e) Side findings: SURVIVE as scoped.** The μ_M
  near-identity reproduces at roundoff (gate bound
  ≤ 5.4×10⁻¹⁹; the stored ≤ 3.4×10⁻¹⁹ differs only in ulp
  count) and the DEC-saturated corner is exactly the stored
  9 triples, pinned at −1.0000003…−1.0000006 (§3).

Every level in this set remains negative. No EC pass, no member,
no drive or transport implication arises from anything in this
gate. Fence in §5.

## §1 Machinery and calibrations

Fresh gate machinery (`gate43/work/g43_lib.py`), written for
this gate: forward-mode second-order AD jets of the metric in
Cartesian coordinates — structurally distinct from both the
lineage's hand-derived radial formulas and Gate-41's radial
jets. Own profile assembly (A2 base + K = 33 corrections from
Phase 344's stored vectors; H2 = centre(1.15) + K = 17
corrections from Phase 379's stored vectors), own Eulerian
frame, own SAMPLER-M margins, own worst-null and adversary
polish. No phase or gate code is reused for any deciding read.
All deciding reads ran on the VM (the frame of record); the
laptop is not a gate instrument (C-7 below).

Calibrations (`gate43/results/g43_calibration.json`,
`g43_calibration_fd.json`):

- **C-0** Stored vectors: the gate's A2 and H2 correction
  vectors agree with both stored artefacts each (confirmation
  JSON and state file) at max diff 0.0.
- **C-1** Trivial limit (S = 0, N = 1, M = 1): max |T| = 0.0
  exactly.
- **C-5** centre(1.0) ≡ A2 totals on r ∈ [9, 21]: max diff 0.0.
- **C-4** A2 anchor SET-244 read: NEC min
  −2.3194531327529964×10⁻⁴ (diff −2.7×10⁻²⁰ vs stored), DEC
  min diff +1.4×10⁻¹⁹, ρ diff +1.2×10⁻¹⁹, Type-I count 3535
  exact, argmin radii exact.
- **C-3** Density-split identity: the gate's Eulerian ρ against
  the closed-form (R + Q_K)/(16π) at all 6642 A2 SET points:
  max diff 1.41×10⁻¹⁸.
- **C-2** Independent cross-path: centred finite differences of
  the metric (h = 0.1 … 0.0125) converge to the gate's AD
  tensor at both test points at the mixed centre (residuals
  1.1×10⁻⁶ → 2.2×10⁻¹² and 3.8×10⁻⁷ → 3.0×10⁻¹³).
- **C-9** Clamp construction at (1,1,1) against Gate-41 §4:
  clamped DEC diff +3.8×10⁻¹⁹, ρ diff −1.6×10⁻¹⁹, clamped
  joint −2.087299309761313×10⁻⁴ vs Gate-41's
  −2.087299309761317×10⁻⁴. The clamped NEC minimum differs
  (gate −1.952837×10⁻⁴, Gate-41 −1.956241×10⁻⁴): see C-10.
- **C-7** Frame admission: not run — by the charge, the laptop
  is not a gate instrument; every deciding read is a VM read.
- **C-10 (the sampled-margin convention band; Gate-41's C-8
  phenomenon, mechanised).** The SET NEC/WEC/SEC minima of
  this lineage are sampled margins at non-Type-I points. The
  Eulerian triad inside γ's exactly degenerate tangential
  eigenspace (γ eigenvalues {M, 1, 1}) is determined by
  rounding-level details, so two honest implementations —
  indeed two evaluation paths inside this gate's own library
  (profiles evaluated at the exact node radius vs at point
  norms, a ≤1.2×10⁻¹⁴ profile difference) — return That
  components differing by up to 2.09×10⁻⁴ at individual
  non-Type-I points, while the coordinate-basis tensor agrees
  to 3.4×10⁻¹⁸ and the mixed tensor's eigenvalues agree to
  8.5×10⁻¹⁹ at every point of the test shell
  (`gate43/results/g43_frame_check.json`). The sampled
  statistics inherit a convention band: at (1,1,1) the gate's
  two paths read NEC minima −1.942242×10⁻⁴ and
  −1.949532×10⁻⁴ around the stored −1.942246×10⁻⁴, above the
  exact worst-null floor −1.951198×10⁻⁴. Consequences, applied
  uniformly in §2–§4: deciding values are taken at named
  points (where the gate reproduces the stored sampled values
  at roundoff, §2) or from frame-invariant statistics
  (Type-I eigenvalue margins, ρ, adversary-polish depth,
  exact worst-nulls) — never from a raw cross-implementation
  sampled minimum. This is the same discipline Gates 39–41
  applied; Gate-43 adds the mechanism and its size.

## §2 Claims (a) and (b) — the mixed centre

Gate deciding reads (`gate43/results/g43_numbers.json`,
`g43_diag.json`):

**(a) The centre.** (μ_S, μ_N, μ_M) = (0.9323593026620368,
1.1444417317708335, 1.1445068359375) applied to H2's totals
(S → μ_S·S, N → μ_N·N, M → 1 + μ_M·(M − 1)).

- At the stored NEC argmin point (−1.9470056065537118,
  −10.702464686683815, 6.28048780487805), r = 12.560975609756097:
  gate NEC = −1.7570735537945236×10⁻⁴, diff +5.4×10⁻²⁰ vs
  stored −1.7570735537945242×10⁻⁴.
- DEC min (Type-I at its argmin, r = 19.634146341463413):
  gate −1.5670690855768764×10⁻⁴, diff −8.1×10⁻¹⁹.
- WEC min diff −1.7×10⁻¹⁸; SEC min diff +2.2×10⁻¹⁸; ρ min
  +8.936712674433238×10⁻⁵, diff +1.4×10⁻¹⁹; Type-I count 3359
  exact (fraction 0.5057211683227943).
- Adversary-polish depth: gate −9.660225437141889×10⁻⁵, diff
  +6.5×10⁻¹⁹ vs stored −9.660225437141954×10⁻⁵ — the polished
  point remains Type-I, so the depth is pointwise-grade.
- The joint level is min(NEC, DEC) = **−1.757074×10⁻⁴**,
  NEC-carried. The gate's raw batch NEC minimum reads
  −1.756688×10⁻⁴ at another direction of the same shell —
  inside the C-10 band (±3.9×10⁻⁸ from the stored minimum
  here); the level is confirmed at its argmin point, above.
- Controls. (1,1,1): at the stored argmin point, gate NEC
  diff −8.1×10⁻²⁰; DEC diff −2.2×10⁻¹⁹; ρ diff −2.7×10⁻²⁰;
  Type-I count 3262 exact; adversary depth diff +5.4×10⁻¹⁹;
  exact worst-null at the stored argmin diff +2.7×10⁻¹⁹ —
  L_stat(H2) = −1.942246×10⁻⁴ reproduced. (1.225, 1.30, 1.30)
  (Phase 383's mixed point): DEC min diff −1.1×10⁻¹⁹
  (−1.287489042939161×10⁻⁴); NEC minimum sampled-carried, gate
  −1.997153×10⁻⁴ vs stored −1.995404×10⁻⁴, inside the C-10
  band; the control's deciding content (the point is
  stationarily worse than H2's centre and worse than the
  mixed centre) is unchanged under every statistic the gate
  read.

**Ruling (a): SURVIVES** as G43-A.

**(b) Worst-null.** At the mixed centre's NEC argmin point,
the gate's exact worst-null (fib-642 scan + Nelder–Mead
polish, independently coded) is −1.7703703917379299×10⁻⁴ vs
stored −1.7703703917379307×10⁻⁴, diff +8.1×10⁻²⁰; the
multistart confirmation agrees. The improvement therefore
survives at pointwise grade. The margin over the bar,
however, is L_stat(H2) − worst-null = 1.9422459891767227×10⁻⁴
− 1.7703703917379307×10⁻⁴ = **+1.7188×10⁻⁵**, not +1.721×10⁻⁵
as carried in the charge and in Phase 389's checkpoint prose
(the stored numbers never supported the larger figure; this
is a prose-figure correction of the Gate-40 §SS4.2 kind, not
a substance failure).

**Ruling (b): SURVIVES RESTATED** as G43-B with the margin
+1.7188×10⁻⁵.

## §3 Claim (d) and side findings (e) — the scaling-space surface

The gate built its own G1 cube: 125 SET-244 reads at
μ ∈ {0.90, 0.95, 1.00, 1.05, 1.10}³ on the gate's machinery
(`gate43/results/g43_cube.jsonl`), then its own full-quadratic
least-squares fit over its non-saturated points
(`g43_fit.json`).

**(d) The gradient at H2.** Excluding the points the gate's
own reads show as DEC-saturated (dec_min < −0.5; exactly the
stored 9, below) leaves **116 points — the stored fit's count
exactly**. Gate fit: gradient at the centre
**(−1.0888, +1.1075, +0.8295)×10⁻⁴ per unit μ**, vs stored
(−1.0955, +1.1147, +0.8211)×10⁻⁴ — signs identical,
per-component diffs (+6.7, −7.2, +8.4)×10⁻⁷, against a max
fit residual of 2.0956×10⁻⁵ (stored 2.0927×10⁻⁵). Hessian
eigenvalues: gate (−3.280, −0.834, −0.054)×10⁻³, stored
(−3.330, −0.838, −0.061)×10⁻³ — all negative in both fits:
a concave cap, and the centre is not at its top. Independent
cross-check, axis finite differences at h = 0.05 from the
gate's own cube rows: μ_S −1.4938242913410102×10⁻⁴ (stored
−1.493824291340853×10⁻⁴, diff 1.6×10⁻¹⁷), μ_N
+1.5377712656999804×10⁻⁴ (stored +1.5377712657000672×10⁻⁴),
μ_M −3.598×10⁻⁵ (stored −3.491×10⁻⁵; the shallow, sign-
agreeing axis — the stored anatomy itself records the μ_M
axis dipping both ways, the M gain being cooperative).
The deciding content is the gradient's existence and
direction: at H2 the level improves toward smaller μ_S and
larger μ_N, μ_M — the mixed direction of claim (a), which is
neither the dwell cycle's direction nor the harvest's.
381's −1.942246×10⁻⁴ was the fixed point of that iteration,
not a local optimum of this surface.

**Ruling (d): SURVIVES** as G43-C.

**(e)(i) The μ_M near-identity.** From the gate's own cube
rows, J(1,1,μ) vs J(μ,μ,μ): joint diffs 3.5×10⁻¹⁹ (μ = 0.95),
5.4×10⁻¹⁹ (1.05), 4.3×10⁻¹⁹ (1.10), with NEC/DEC diffs of the
same order and identical argmin radii for both members of
each pair. The identity holds at roundoff in the gate's
machinery; the gate's bound (≤ 5.4×10⁻¹⁹) differs from the
stored (≤ 3.4×10⁻¹⁹) only in ulp count, which is not a
physical quantity.

**(e)(ii) The DEC-saturated corner.** The gate's saturation
criterion (dec_min < −0.5) selects **exactly the stored 9
triples** — (1.0, 0.9, 0.9), (1.05, 0.9, 0.9),
(1.05, 0.9, 0.95), (1.05, 0.95, 0.9), (1.1, 0.9, 0.9),
(1.1, 0.9, 0.95), (1.1, 0.9, 1.0), (1.1, 0.95, 0.9),
(1.1, 0.95, 0.95) — with dec_min pinned in
[−1.0000006, −1.0000003], the stored ≈ −1.0000005. Within
the pinned plateau the argmin radius is not sharp: the gate
reads r = 17.683 for six of the nine and r = 17.195 for
three (the plateau spans both shells; the pinned values
differ by ≤ 2.7×10⁻⁷, inside the C-10 band).

**Ruling (e): SURVIVES as scoped** as G43-D.

## §4 Claim (c) — the end-clamp re-read at the mixed centre

Construction exactly as Gate-41's: H2's three K = 17
correction vectors with first/last knots zeroed, totals
rebuilt, the mixed scaling applied to the clamped totals,
SET-244 read on the gate's machinery
(`g43_numbers.json`, record `mixed_clamped`):

- Clamped joint level **−1.766963×10⁻⁴**, NEC-carried at
  r = 12.560975609756097 (the unclamped argmin shell);
  clamped DEC min −1.660823×10⁻⁴ (Type-I, r = 19.634);
  clamped ρ min +8.938935×10⁻⁵; Type-I count 3442;
  adversary-polish depth −9.659258×10⁻⁵ (vs unclamped
  −9.660225×10⁻⁵).
- Clamp cost at the mixed centre: **1.03×10⁻⁶** (gate's
  consistent statistic: unclamped joint −1.756688×10⁻⁴ →
  clamped −1.766963×10⁻⁴) — an order of magnitude below the
  1.450533×10⁻⁵ the same clamping cost at H2 (Gate-41 §4).
  Against the stored unclamped level the cost is 9.9×10⁻⁷;
  either way it is ~5% of the gain, not ~78% of it as at H2.
- Margins after clamping: over L_stat(H2) =
  −1.942246×10⁻⁴: **+1.7528×10⁻⁵ — SURVIVES** (unclamped
  +1.8517×10⁻⁵). Over the dwelling ceiling
  −2.099385×10⁻⁴: **+3.3242×10⁻⁵ — SURVIVES** (unclamped
  +3.4231×10⁻⁵). Both margins exceed the C-10 convention
  band (±~3×10⁻⁶) by an order of magnitude, and every other
  clamped statistic (DEC, depth) also sits above L_stat(H2):
  the survival is overdetermined, not statistic-dependent.
- Why the outcome differs from H2's: at H2 the gain's
  band-edge component was chiefly the S correction's r = 20
  knot (G41-E); at the mixed centre the improvement is
  carried by the scaling direction itself (μ_S < 1 with
  μ_N, μ_M > 1 acting on the whole profiles), not by the
  correction vectors' end knots — zeroing those knots costs
  only 1.03×10⁻⁶.

**Ruling (c): the margin over L_stat(H2) survives clamping at
the mixed centre, and the margin over the dwelling ceiling
survives with it.** The rider is issued as G43-E in §5, in
G41-E's form, and attaches to G43-A wherever its margin is
quoted.

## §5 The quotable set (G43-*), with the fence

**FENCE (verbatim, travels with every quotation):** band pose
[10, 20] only; Phase 356's full-extent caveats travel with
every level in this set; every level is negative; no EC pass,
no member, no drive or transport implication.

- **G43-A (the mixed centre).** At the per-profile stationary
  scaling (μ_S, μ_N, μ_M) = (0.9323593026620368,
  1.1444417317708335, 1.1445068359375) of the harvested centre
  H2's total profiles, the stationary joint level (SET-244,
  SAMPLER-M, band [10, 20]) is **−1.757074×10⁻⁴** (NEC min
  −1.7570735537945242×10⁻⁴ at r = 12.560975609756097; DEC min
  −1.5670690855768682×10⁻⁴, Type-I, at
  r = 19.634146341463413; ρ min +8.936712674433238×10⁻⁵;
  adversary-polish depth −9.660225437141954×10⁻⁵), above
  L_stat(H2) = −1.942246×10⁻⁴ by +1.851724×10⁻⁵. G43-E is
  part of this claim wherever its margin is quoted.
- **G43-B (pointwise grade).** The exact worst-null at
  G43-A's NEC argmin is −1.7703703917379307×10⁻⁴, above
  L_stat(H2) by **+1.7188×10⁻⁵** (restated figure; the
  +1.721×10⁻⁵ in the Phase 389 prose does not reproduce from
  its stored numbers).
- **G43-C (the classification).** Phase 381's fixed point at
  −1.942246×10⁻⁴ is the fixed point of the dwell→harvest
  iteration, not a local optimum of the stationary level
  surface: the surface's gradient at H2 in per-profile
  scaling space is nonzero — (−1.089, +1.108, +0.830)×10⁻⁴
  per unit μ (gate fit over the gate's own 116-point
  non-saturated cube; Phase 389's fit:
  (−1.096, +1.115, +0.821)×10⁻⁴) — with all-negative Hessian
  eigenvalues in both fits (gate (−3.280, −0.834,
  −0.054)×10⁻³). The improving direction at H2 — μ_S down,
  μ_N and μ_M up — is the mixed direction of G43-A, searched
  by neither the dwell cycle nor the harvest.
- **G43-D (side findings, as scoped).** (i) The μ_M
  near-identity: J(1,1,μ) = J(μ,μ,μ) to roundoff at
  μ ∈ {0.95, 1.05, 1.10} (gate bound ≤ 5.4×10⁻¹⁹; stored
  ≤ 3.4×10⁻¹⁹). (ii) The DEC-saturated corner of the G1
  cube is exactly 9 grid points — (1.0, 0.9, 0.9),
  (1.05, 0.9, 0.9), (1.05, 0.9, 0.95), (1.05, 0.95, 0.9),
  (1.1, 0.9, 0.9), (1.1, 0.9, 0.95), (1.1, 0.9, 1.0),
  (1.1, 0.95, 0.9), (1.1, 0.95, 0.95) — with DEC minima
  pinned at −1.0000003…−1.0000006.
- **G43-E (the end-clamp rider — part of G43-A wherever its
  margin is quoted).** End-clamping H2's correction splines
  (all first/last knots zeroed) and applying the G43-A
  scaling to the clamped totals reads a joint level of
  −1.766963×10⁻⁴ (NEC-carried), a cost of 1.03×10⁻⁶: the
  clamped level remains above L_stat(H2) by +1.7528×10⁻⁵ —
  the margin over the centre bar survives clamping — and
  remains above the dwelling ceiling by +3.3242×10⁻⁵ — the
  margin over the dwelling ceiling survives clamping with
  it. (Contrast G41-E, where the centre-bar margin did not
  survive.)

## §6 Provenance and artefacts

- Stored bytes verified (md5): p379_confirmation.json
  1bcb8b3900026cc78e6aacb33654ad72 · p379_state_H2.json
  66adf3797e6e105c71f89ca8fe5be4fe · p344_confirmation.json
  bca93c039daf9c8baf68f4e567abe873 · p344_state_A2.json
  eec813ee4d1c94de6ac21829304d5ebd · p389_confirmation.json
  f2139b1fac8f8ae2bad7a490e8be80ed · p389_anatomy.json
  d43fd81d809a593036dac1dc8f997010. The gate's profile
  assembly consumes the stored vectors from the confirmation
  artefacts; the state files agree at 0.0 (C-0).
- Gate artefacts: `gate43/work/g43_lib.py` (machinery),
  `g43_calibrate.py`, `g43_audit.py`, `g43_diag.py`,
  `g43_cube.py` (drivers); `gate43/results/
  g43_calibration.json`, `g43_calibration_fd.json`,
  `g43_numbers.json`, `g43_diag.json`, `g43_frame_check.json`,
  `g43_cube.jsonl`, `g43_fit.json`.
- The lineage comparison in `g43_diag.json`
  (`lineage_cmp_111_argmin`) is a diagnostic only — it
  establishes that the gate's tensor equals the lineage's at
  the test point (max diff 2.7×10⁻¹⁹); no deciding read uses
  lineage code.
- Three-goal accounting: Goal 1 (FTL drive) — the pressure
  wall's best band stationary level improves to
  −1.757074×10⁻⁴ and the improvement is now gate-verified
  with its end-clamp rider; the level remains negative, so
  no front pass, no member, no transport. Goal 2 (wormhole)
  — no throat claim is touched by this gate. Goal 3
  (subluminal record) — untouched; Procaccia's 0.1363 stands.
- DESK: NO DATA CONTACT.
