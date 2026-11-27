# GATE-46 — Independent re-judgement of the Phase 395 claim set

Charged at ledger entry 1017 (2026-11-26). Phase 395 claimed
that widening Phase 394's scaling box moved the stationary
centre again: in the extended box μ_S ∈ [0.60, 1.10],
μ_N ∈ [0.95, 1.60], μ_M ∈ [1.60, 5.00], a 389-pattern search
seeded at 394's centre found a new centre at
(μ_S, μ_N, μ_M) = (0.601180962300002, 1.5934531363763935,
4.887238651223381) on H2's total profiles, with band level
−2.980985×10⁻⁵ — +3.831668×10⁻⁵ over the anchor (394's
centre), +1.458975×10⁻⁴ over 389's mixed centre,
+1.644147×10⁻⁴ over L_stat(H2); the standing level is 15.3%
of its H2 magnitude. This gate re-judges that claim set with
fresh machinery only, every deciding value reproduced
independently on the VM frame of record.

## Verdict

- **(a) The new centre and its level −2.980985×10⁻⁵:
  SURVIVES.** The gate's batch SET-244 read reproduces the
  stored joint at −2.9809850277749195×10⁻⁵ (diff
  −1.9×10⁻¹⁹), the DEC minimum at diff −6.8×10⁻²⁰, ρ_min at
  diff −6.9×10⁻¹⁸, and the Type-I count exactly (4067). All
  four controls reproduce (§2).
- **(b) Pointwise survival: SURVIVES.** The exact worst-null
  at the centre's SET NEC argmin point reproduces at
  −3.089621009567827×10⁻⁵ (diff −2.0×10⁻¹⁹ vs stored).
- **(c) The end-clamp rider: SURVIVES.** The clamped level
  reproduces at diff −5.4×10⁻²⁰ (−3.0189206094012074×10⁻⁵
  stored); clamp cost 3.793558×10⁻⁷ (gate magnitude agrees
  with stored at 1.4×10⁻¹⁹); the clamped level remains
  above the anchor's unclamped level by +3.793732×10⁻⁵ and
  above L_stat(H2) by +1.640354×10⁻⁴ — both clamped margins
  survive. Rider issued as part of G46-C (§5).
- **(d) The box claims: SURVIVE.** The stored record
  recounts exactly (220 reads, all feasible; 212 beating
  the anchor; worst DEC −6.5529696405777245×10⁻⁶; zero
  DEC-saturated reads under either threshold); the
  worst-DEC read is independently re-read on gate machinery
  at diff +1.6×10⁻¹⁹; the registered diagonal is re-read at
  all five points at roundoff and rises at every step with
  undiminished increments and no turn; the pure μ_M ray is
  re-read at all seven registered radii and dips then rises
  monotonically to the 5.00 edge with no turn (six joints at
  roundoff, one inside the C-10 band) (§3).
- **(e) The box-edge disclosure: SURVIVES — and is issued
  as rider G46-E**, attached on the face of G46-A, G46-B
  and G46-C wherever the centre's level is quoted: the
  centre presses the extended box's μ_S lower edge
  (0.601180962300002 vs 0.60, by 0.00118) and nears its
  μ_N upper edge (1.5934531363763935 vs 1.60, by 0.00655),
  and whether the level keeps rising for μ_S < 0.60 or
  μ_N > 1.60 is UNMEASURED. The centre is quotable only as
  the optimum of the registered extended box (§4).

Every level in this set remains negative. No EC pass, no
member, no drive or transport implication arises from
anything in this gate. Fence in §5.

## §1 Machinery and calibrations

Fresh gate machinery (`gate46/work/g46_lib.py`,
`g46_profiles.py`), written for this gate: the Einstein
tensor is derived **symbolically with sympy in spherical
coordinates** (t, r, θ, φ) from the prescribed metric
ansatz (g46_derive.py → g46_exprs.py), lambdified, and
transformed to Cartesian components point by point — an
organisation used by no earlier read in this lineage (the
lineage used hand-derived radial formulas; Gate-43 loop
contractions in Cartesian; Gate-45 forward-mode AD jets
with whole-array einsum in Cartesian). The inverse metric
inside the derivation is built analytically by the block
Schur complement (the spatial block is diagonal in these
coordinates). Own profile assembly (A2 base + K = 33
corrections from Phase 344's stored vectors; H2 =
centre(1.15) + K = 17 corrections from Phase 379's stored
vectors), own Eulerian frame, own SAMPLER-M margins, own
worst-null and recount. No phase or earlier gate code is
imported or reused for any deciding read. All deciding
reads ran on the VM; the laptop is not a gate instrument.

Calibrations (`gate46/results/g46_numbers.json`,
`g46_ray_box.json`, `g46_summary.json`):

- **C-0** Stored vectors: the gate's A2 and H2 correction
  vectors agree between the two stored artefacts each
  (confirmation JSON and state file) at max diff 0.0.
- **C-1** Trivial limit (S = 0, N = 1, M = 1): max |T| =
  2.5×10⁻¹⁸ — roundoff (the raw symbolic form leaves a
  10⁻¹⁸ residue where Gate-45's AD path returned exact 0;
  no deciding value is within ten orders of magnitude of
  this floor).
- **C-2** Independent cross-path: centred finite
  differences of the metric (h = 0.1 … 0.025) converge to
  the gate's symbolic tensor at the centre's NEC argmin
  point — max |ΔT| 1.26×10⁻⁶ → 8.11×10⁻⁸ → 2.17×10⁻¹².
- **C-3** Clamp construction cross-checks: at the mixed
  centre the gate's clamped joint is
  −1.7669632754376664×10⁻⁴ against Gate-43's independent
  value at diff −2.7×10⁻¹⁹; at (1,1,1) the gate's clamped
  joint is −2.0872993097613136×10⁻⁴ against Gate-41/43/45's
  value at diff +2.7×10⁻¹⁹; at the anchor the gate's
  clamped joint reproduces Phase 395's stored
  −6.968822658140883×10⁻⁵ at diff −1.2×10⁻¹⁹. The clamp
  construction the gate applies in §2(c) is therefore the
  registered one.
- **C-10 (frame-convention band, applied as in
  Gate-43/45).** Raw sampled NEC minima at non-Type-I
  points carry the ±~3×10⁻⁶ convention band. In this gate
  the mechanism was measured directly at the seed's batch
  argmin point (`g46_diag2.py` record in the run logs):
  the profiles, the Cartesian tensor and the metric from a
  batch (162-point) and a single-point evaluation agree to
  ≤ 3.6×10⁻¹⁵, while the Eulerian-frame component
  That[0,1] differs by 1.43×10⁻⁴ (+1.024×10⁻⁴ batch vs
  −4.070×10⁻⁵ single) — the triad inside γ's exactly
  degenerate tangential eigenspace is rounding-determined,
  and the sampled margins at non-Type-I points inherit it.
  The band appears exactly where Gate-43/45 mechanised it:
  the gate's batch minimum at (1,1,1) sits on the sibling
  shell r = 17.683 (−1.9495321561300275×10⁻⁴, Gate-45's
  batch value), while at the stored argmin shell
  r = 16.21951219512195 the gate's shell NEC minimum
  reproduces the stored NEC minimum at diff −5.1×10⁻¹⁹;
  the seed's and mixed centre's shell sampled minima
  differ from stored by +7.68×10⁻⁸ and +3.85×10⁻⁸ (inside
  the band; Gate-45 saw the same +7.7×10⁻⁸ at the seed),
  while at their named points the frame-invariant
  statistics reproduce at roundoff (§2). The batch WEC/SEC
  minima at (1,1,1) differ from stored by −7.10×10⁻⁶ /
  −4.09×10⁻⁶ — differences of two extreme order statistics
  over ~2.6×10³ non-Type-I points; no claim in this set
  rests on a WEC or SEC value. Deciding values throughout
  are taken at named points or from frame-invariant
  statistics (eigenvalue margins, ρ, Type-I counts, exact
  worst-nulls), never from a raw cross-implementation
  sampled minimum alone.

## §2 Claims (a), (b), (c) — the centre, its worst-null, its clamp

Gate deciding reads (`gate46/results/g46_numbers.json`,
`g46_shellpoints.json`):

**(a) The centre.** (μ_S, μ_N, μ_M) = (0.601180962300002,
1.5934531363763935, 4.887238651223381) applied to H2's
totals (S → μ_S·S, N → μ_N·N, M → 1 + μ_M·(M − 1)).

- Batch SET-244 read on gate machinery: joint (NEC) min
  −2.9809850277749195×10⁻⁵ at r = 15.73170731707317 (stored
  −2.9809850277749006×10⁻⁵, diff −1.9×10⁻¹⁹); DEC min
  −1.7766846142506707×10⁻⁶ at r = 18.65853658536585, Type-I
  (diff −6.8×10⁻²⁰); ρ min +9.780857711542179×10⁻⁵ (diff
  −6.9×10⁻¹⁸); Type-I count 4067 (stored fraction
  0.6123155676001204 × 6642 = 4067, exact). The
  shell-restricted read at the stored argmin shell
  reproduces the same minimum at diff −1.9×10⁻¹⁹.
- Controls. (1,1,1): DEC diff −5.7×10⁻¹⁹, ρ diff
  +5.4×10⁻²⁰, Type-I count 3262 exact; at the stored NEC
  argmin shell the shell NEC minimum reproduces
  L_stat(H2) at diff −5.1×10⁻¹⁹ (the batch minimum's
  sibling-shell excursion is C-10, §1). The mixed centre
  (0.9323593026620368, 1.1444417317708335,
  1.1445068359375): DEC diff +1.0×10⁻¹⁸, ρ diff
  +1.4×10⁻¹⁹, Type-I count 3359 exact, argmin shell exact;
  at Gate-43's stored argmin point
  (−1.9470056065537118, −10.702464686683815,
  6.28048780487805) the gate's sampled NEC margin is
  −1.7570735537945242×10⁻⁴ — the stored minimum, exact —
  and its exact worst-null is
  −1.770370391737933×10⁻⁴ (diff −2.4×10⁻¹⁹ vs Gate-43's
  stored value). The seed (0.9323593026620368,
  1.1444417317708335, 2.289013671875): DEC diff
  −1.1×10⁻¹⁹, ρ diff −9.5×10⁻¹⁹, Type-I count 3148 exact;
  at the gate's named argmin point the sampled NEC
  reproduces the stored minimum exactly (diff 0.0) and the
  exact worst-null at diff −2.7×10⁻²⁰. The anchor (394's
  centre): joint diff −2.7×10⁻²⁰, DEC diff +5.3×10⁻¹⁹,
  ρ diff +3.0×10⁻¹⁹, Type-I count 3311 exact, worst-null
  diff +1.4×10⁻²⁰. All four controls are reproduced at
  roundoff on frame-invariant fields, as charged.

**Ruling (a): SURVIVES** as G46-A.

**(b) Worst-null.** At the centre's SET NEC argmin point
(the gate's batch and shell argmin at
r = 15.73170731707317), the gate's exact worst-null
(fib-642 scan + Nelder–Mead polish, independently coded)
is −3.089621009567827×10⁻⁵ vs stored
−3.0896210095678075×10⁻⁵, diff −2.0×10⁻¹⁹. The improvement
over the anchor survives at pointwise grade (stored
margin +4.083532×10⁻⁵; the gate's centre and anchor
worst-nulls reproduce individually at roundoff).

**Ruling (b): SURVIVES** as G46-B.

**(c) End-clamp.** Construction exactly as Gate-41/43/45
(the gate's construction is cross-validated in C-3). The
centre end-clamped on gate machinery: joint
−3.0189206094012074×10⁻⁵ (stored; gate diff −5.4×10⁻²⁰),
NEC-carried at r = 15.73170731707317; DEC min
−1.7417010050539813×10⁻⁶ (stored); ρ min
+9.780939577475905×10⁻⁵ (stored). Clamp cost: gate
3.793558162629325×10⁻⁷ against stored
3.7935581626306804×10⁻⁷ (agreement 1.4×10⁻¹⁹). Clamped
margins: over the anchor's unclamped level
−6.812653×10⁻⁵: **+3.793732×10⁻⁵ — SURVIVES** (gate
+3.793732046790524×10⁻⁵). Over L_stat(H2) =
−1.942246×10⁻⁴: **+1.640354×10⁻⁴ — SURVIVES** (gate
+1.6403539282366014×10⁻⁴). Both margins exceed the C-10
band by more than an order of magnitude; the survival is
not statistic-dependent. As at the mixed centre (G43-E)
and the anchor (G45-C), the gain is carried by the scaling
direction, not the correction vectors' end knots.

**Ruling (c): SURVIVES** as G46-C, with the clamped level
and both margins stated on its face.

## §3 Claim (d) — the registered extended box

The box (Phase 395 registration): μ_S ∈ [0.60, 1.10],
μ_N ∈ [0.95, 1.60], μ_M ∈ [1.60, 5.00]; 220 stored SET-244
reads (RAY2 7, DIAG 4, G1 24, G2 12, G3 17, G4 29, G5 127).

- **Recount of the stored record** (`p395_screens.jsonl`,
  md5-verified inputs; `g46_recount.json`): 220 reads, all
  feasible; **212** with joint above the anchor's
  −6.812652656191736×10⁻⁵; worst DEC over all reads
  **−6.5529696405777245×10⁻⁶** (the G2 read at
  (0.8015689430763502, 1.3179449338854314,
  3.074968377899082)); **zero** reads with DEC below −0.5
  and zero below −0.9999 — no DEC-saturated read under
  either threshold in the lineage's use.
- **Independent re-read of the worst-DEC subject** on gate
  machinery: DEC min −6.5529696405777245×10⁻⁶ (gate diff
  +1.6×10⁻¹⁹ vs stored), its DEC argmin Type-I at
  r = 18.170731707317074. The box's least-DEC read is an
  ordinary Type-I read, nowhere near the past-branch
  pinning of Phase 387's saturated regime.
- **The registered diagonal, independently re-read** from
  the anchor along (−0.025, +0.025, +0.25) steps
  (`g46_ray_box.json`): gate joints −6.812653×10⁻⁵ →
  −6.304991×10⁻⁵ → −5.754609×10⁻⁵ → −5.289900×10⁻⁵ →
  −4.818018×10⁻⁵, every joint at roundoff vs stored
  (diffs ≤ 2.2×10⁻¹⁹); step increments (gate)
  +5.076619×10⁻⁶, +5.503820×10⁻⁶, +4.647083×10⁻⁶,
  +4.718826×10⁻⁶ against stored +5.076619×10⁻⁶,
  +5.503820×10⁻⁶, +4.647083×10⁻⁶, +4.718826×10⁻⁶ —
  **undiminished, no turn inside the box**.
- **The pure μ_M ray, independently re-read** at
  (A_S, A_N) = (0.8015689430763502, 1.3179449338854314)
  for μ_M ∈ {3.574968377899082, 3.75, 4.0, 4.25, 4.5,
  4.75, 5.0}: gate joints −6.812653×10⁻⁵ →
  −6.912171×10⁻⁵ → −6.730269×10⁻⁵ → −6.626716×10⁻⁵ →
  −6.572789×10⁻⁵ → −6.477082×10⁻⁵ → −6.323066×10⁻⁵ —
  **dips first (at μ_M = 3.75), then rises monotonically
  to the box edge with no turn**. Six of the seven joints
  reproduce the stored ray at roundoff (diffs ≤
  3.8×10⁻¹⁹); the μ_M = 5.0 joint differs by +1.07×10⁻⁷,
  inside the C-10 band, at a point whose deciding content
  (the rise to the edge) is unaffected.

**Ruling (d): SURVIVES** as G46-D.

## §4 Claim (e) — the box-edge disclosure

The centre's μ_S = 0.601180962300002 sits 0.00118 above
the extended box's lower edge μ_S = 0.60 — the same margin
by which 394's centre pressed its box — in the tight flat
cluster the phase disclosed (five stored reads within
1.7×10⁻⁷ of its joint). It also nears the μ_N upper edge
(1.5934531363763935, 0.00655 below 1.60); μ_M =
4.887238651223381 sits inside its edge (0.113 below 5.00).
The phase's G5 polish walked to this point from the
diagonal's end; the corner incumbent's G4 polish returned
exactly its start point, so the centre is a local optimum
**of the searched box at polish resolution** — and nothing
in the record measures the surface for μ_S < 0.60 or
μ_N > 1.60. Both traces (§3) were still rising at their
edges, which is a second, independent reason the box does
not close the surface.

The disclosure is therefore not a caveat on the phase's
honesty — the phase carried it on its own face — but a
standing rider on the claim set, in the G41-E/G43-E/G45-E
manner: **any quotation of the centre's level (G46-A),
its worst-null (G46-B), or its clamped level (G46-C) must
carry G46-E with it.** A centre found in a further-widened
box (Phase 396's charge) will supersede or confirm this
one under its own gate; until then the level is quotable
only as the optimum of the registered extended box.

**Ruling (e): SURVIVES** as rider G46-E, attached to
G46-A, G46-B and G46-C.

## §5 The quotable set (G46-*), with the fence

**FENCE (verbatim, travels with every quotation):** band pose
[10, 20] only; Phase 356's full-extent caveats travel with
every level in this set; every level is negative; no EC pass,
no member, no drive or transport implication.

- **G46-A (the widened-box centre).** At the per-profile
  stationary scaling (μ_S, μ_N, μ_M) =
  (0.601180962300002, 1.5934531363763935,
  4.887238651223381) of the harvested centre H2's total
  profiles, the stationary joint level (SET-244, SAMPLER-M,
  band [10, 20]) is **−2.980985×10⁻⁵** (NEC min
  −2.9809850277749006×10⁻⁵ at r = 15.73170731707317; DEC min
  −1.7766846142506707×10⁻⁶, Type-I, at
  r = 18.65853658536585; ρ min +9.780857711542179×10⁻⁵),
  above Phase 394's centre (−6.812653×10⁻⁵) by
  +3.831668×10⁻⁵, above Phase 393's ray point
  (−1.241372×10⁻⁴) by +9.432734×10⁻⁵, above Phase 389's
  mixed centre (−1.757074×10⁻⁴) by +1.458975×10⁻⁴, and
  above L_stat(H2) = −1.942246×10⁻⁴ by +1.644147×10⁻⁴.
  **G46-E is part of this claim wherever its level is
  quoted.**
- **G46-B (pointwise grade).** The exact worst-null at
  G46-A's NEC argmin is −3.0896210095678075×10⁻⁵, above
  the anchor's worst-null (−7.173153284502476×10⁻⁵) by
  +4.083532×10⁻⁵: the improvement survives at pointwise
  grade. **G46-E is part of this claim wherever its level
  is quoted.**
- **G46-C (the end-clamp rider — part of G46-A wherever
  its margin is quoted).** End-clamping H2's correction
  splines (all first/last knots zeroed) and applying the
  G46-A scaling to the clamped totals reads a joint level
  of −3.018921×10⁻⁵ (NEC-carried), a clamp cost of
  3.794×10⁻⁷: the clamped level remains above the anchor's
  unclamped level by +3.793732×10⁻⁵ — the margin over the
  anchor survives clamping — and remains above L_stat(H2)
  by +1.640354×10⁻⁴ — the margin over the centre bar
  survives clamping with it. **G46-E is part of this claim
  wherever its level is quoted.**
- **G46-D (the registered extended box).** In Phase 395's
  registered extended box (μ_S ∈ [0.60, 1.10],
  μ_N ∈ [0.95, 1.60], μ_M ∈ [1.60, 5.00]), all 220 stored
  reads are feasible and none is DEC-saturated (worst DEC
  −6.5529696405777245×10⁻⁶, an ordinary Type-I read at
  (0.8015689430763502, 1.3179449338854314,
  3.074968377899082)); 212 of the 220 reads beat the
  anchor's level; the registered diagonal (μ_S down,
  μ_N up, μ_M up) rises at every step with undiminished
  increments (+5.08, +5.50, +4.65, +4.72 ×10⁻⁶) and no
  turn inside the box; and the pure μ_M ray from the
  anchor dips (−6.912171×10⁻⁵ at μ_M = 3.75) then rises
  monotonically to the box edge (−6.333735×10⁻⁵ at
  μ_M = 5.0, stored) with no turn inside the box.
- **G46-E (the box-edge rider — part of G46-A, G46-B and
  G46-C wherever their levels are quoted).** The G46-A
  centre presses the registered extended box's μ_S lower
  edge (μ_S = 0.601180962300002 against the edge 0.60) and
  nears its μ_N upper edge (μ_N = 1.5934531363763935
  against the edge 1.60): the centre is the optimum **of
  the registered extended box**, and whether the level
  keeps rising outside the box — below μ_S = 0.60, or
  above μ_N = 1.60 — is unmeasured in this claim set.

## §6 Provenance and artefacts

- Stored bytes verified (md5): p395_confirmation.json
  6d3e2c209ffbcd36ff2f59bdee09a0bb · p395_clamp.json
  2eb334e7a12e55753fc894d1793f8df6 · p395_anatomy.json
  1632c1d11b6242ff4593e64d6cd94691 · p395_controls.json
  c351a47304f5186a1884e8db2dcbdc7c ·
  p395_search_summary.json 62993b28d0ea5f6dbb000fef530053ff
  · p395_screens.jsonl 918d28be3c00c7d978ce318ed1580bd0 ·
  CHECKPOINT395.md 0c30b160559366962ff3c6cd3d454713 ·
  p395_memo.md 15af837dcac189fec01751ad2ee66979 ·
  p394_confirmation.json 611424f0c0ac49ead895e2ed2b3a9172 ·
  p393_ray.json 090d0fb234179b631a53e99fc010934e ·
  p389_confirmation.json f2139b1fac8f8ae2bad7a490e8be80ed
  · p379_confirmation.json
  1bcb8b3900026cc78e6aacb33654ad72 ·
  p344_confirmation.json bca93c039daf9c8baf68f4e567abe873 ·
  GATE45.md aebe3da522659159e87150e6be9e41d0 · GATE43.md
  1fc62511f4b33d47de96771164ff3739. The gate's profile
  assembly consumes the stored vectors from the
  confirmation artefacts; the state files agree at 0.0
  (C-0).
- Gate artefacts: `gate46/work/g46_derive.py` (the sympy
  derivation; its docstring records why the shipped form
  uses an analytic Schur inverse and time-boxed
  simplify/factor — the first, fully-simplifying attempt
  did not finish and was terminated), `g46_exprs.py` (the
  derived tensor), `g46_profiles.py`, `g46_lib.py`
  (machinery), `g46_run.py`, `g46_recount.py`,
  `g46_shellpoints.py`; `gate46/results/g46_numbers.json`
  (the §2 deciding reads), `g46_clamp_margins.json`,
  `g46_ray_box.json` (the §3 trace re-reads, the worst-DEC
  re-read, the FD cross-check), `g46_recount.json`,
  `g46_shellpoints.json`, `g46_summary.json`. The main
  run's first launch was lost to a service restart before
  any output was written and was relaunched in full; no
  read was repeated or lost.
- Three-goal accounting: Goal 1 (FTL drive) — the pressure
  wall's best band stationary level improves to
  −2.980985×10⁻⁵ and the improvement is now gate-verified
  with its end-clamp rider and its box-edge rider; the
  level remains negative, so no front pass, no member, no
  transport. Goal 2 (wormhole) — no throat claim is
  touched by this gate. Goal 3 (subluminal record) —
  untouched; Procaccia's 0.1363 stands.
- DESK: NO DATA CONTACT.
