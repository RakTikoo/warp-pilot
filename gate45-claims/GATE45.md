# GATE-45 — Independent re-judgement of the Phase 394 claim set

Charged at ledger entry 1011 (2026-11-26). Phase 394 claimed that
Phase 393's ray point was not a ridge: a 389-pattern scaling search
seeded there climbed diagonally to a new stationary centre at
(μ_S, μ_N, μ_M) = (0.8015689430763502, 1.3179449338854314,
3.574968377899082) on H2's total profiles, with band level
−6.812653×10⁻⁵ — +5.601066×10⁻⁵ over the seed, +1.075808×10⁻⁴ over
389's mixed centre, +1.260980×10⁻⁴ over L_stat(H2). This gate
re-judges that claim set with fresh machinery only, every deciding
value reproduced independently on the VM frame of record.

## Verdict

- **(a) The new centre and its level −6.812653×10⁻⁵: SURVIVES.**
  The gate's batch SET-244 read reproduces the stored joint at
  −6.812652656191745×10⁻⁵ (diff −8.1×10⁻²⁰), the DEC minimum at
  diff +3.7×10⁻¹⁹, ρ_min at diff −8.8×10⁻¹⁹, and the Type-I count
  exactly (3311). All three controls reproduce (§2).
- **(b) Pointwise survival: SURVIVES.** The exact worst-null at
  the centre's SET NEC argmin point reproduces at
  −7.17315328450248×10⁻⁵ (diff −4.1×10⁻²⁰ vs stored).
- **(c) The end-clamp rider: SURVIVES.** The clamped level
  reproduces at diff +1.4×10⁻¹⁹ (−6.968822658140869×10⁻⁵); clamp
  cost 1.561700×10⁻⁶ (gate, = stored to the digits shown); the
  clamped level remains above the seed's unclamped level by
  +5.4449×10⁻⁵ and above L_stat(H2) by +1.2454×10⁻⁴ — both
  clamped margins survive. Rider issued as part of G45-C (§5).
- **(d) The box claims: SURVIVE.** The stored record recounts
  exactly (349 reads; 318 beating the seed; worst DEC
  −5.3917400712468285×10⁻⁵; zero DEC-saturated reads under
  either saturation threshold); the worst-DEC read is
  independently re-read on gate machinery at diff −2.6×10⁻¹⁸;
  the pure μ_M ray is independently re-read at all eight
  registered radii and rises monotonically on the gate's reads
  with no turn (six joints at roundoff, two inside the C-10
  band) (§3).
- **(e) The box-edge disclosure: SURVIVES — and is issued as
  rider G45-E**, attached on the face of G45-A, G45-B and G45-C
  wherever the centre's level is quoted: the centre presses
  the registered μ_S lower edge (0.8015689430763502 vs 0.80),
  and whether the level keeps rising for μ_S < 0.80 is
  UNMEASURED. The centre is quotable only as the optimum of
  the registered box (§4).

Every level in this set remains negative. No EC pass, no member,
no drive or transport implication arises from anything in this
gate. Fence in §5.

## §1 Machinery and calibrations

Fresh gate machinery (`gate45/work/g45_lib.py`), written for
this gate: forward-mode second-order AD jets of the metric in
Cartesian spatial coordinates, with the Christoffel and Ricci
contractions carried out by whole-array einsum algebra — a
different contraction organisation from both the lineage's
hand-derived radial formulas and Gate-43's loop contractions.
Own profile assembly (A2 base + K = 33 corrections from Phase
344's stored vectors; H2 = centre(1.15) + K = 17 corrections
from Phase 379's stored vectors), own Eulerian frame, own
SAMPLER-M margins, own worst-null and polish. No phase or
earlier gate code is imported or reused for any deciding read.
All deciding reads ran on the VM; the laptop is not a gate
instrument.

Calibrations (`gate45/results/g45_numbers.json`,
`g45_ray_box.json`, `g45_summary.json`):

- **C-0** Stored vectors: the gate's A2 and H2 correction
  vectors agree between the two stored artefacts each
  (confirmation JSON and state file) at max diff 0.0.
- **C-1** Trivial limit (S = 0, N = 1, M = 1): max |T| = 0.0
  exactly.
- **C-2** Independent cross-path: centred finite differences
  of the metric (h = 0.1 … 0.0125) converge to the gate's AD
  tensor at the centre's NEC argmin point — max |ΔT|
  1.32×10⁻⁷ → 8.42×10⁻⁹ → 2.10×10⁻¹¹ → 2.97×10⁻¹².
- **C-3** Clamp construction cross-checks: at the mixed
  centre the gate's clamped joint is
  −1.7669632754376664×10⁻⁴, identical to Gate-43's
  independent value (diff 0.0 at the stored digits); at
  (1,1,1) the gate's clamped joint is
  −2.0872993097613136×10⁻⁴ vs Gate-41/Gate-43's
  −2.087299309761313×10⁻⁴ (diff −5.4×10⁻²⁰). The clamp
  construction the gate applies in §2(c) is therefore the
  registered one.
- **C-10 (frame-convention band, applied as in Gate-43).**
  Raw sampled NEC minima at non-Type-I points carry the
  ±~3×10⁻⁶ convention band. It appears in this gate exactly
  where Gate-43 mechanised it: the gate's batch minimum at
  (1,1,1) sits on the sibling shell r = 17.683
  (−1.949532×10⁻⁴, Gate-43's second-path value), while at
  the stored argmin shell r = 16.2195 the gate reproduces
  the stored NEC minimum at diff +2.7×10⁻²⁰; the seed's
  batch sampled minimum differs from stored by 7.7×10⁻⁸
  while at the seed's named argmin point the sampled NEC
  reproduces at diff +3.8×10⁻¹⁹ and the frame-invariant
  worst-null at diff +3.5×10⁻¹⁹. Deciding values throughout
  are taken at named points or from frame-invariant
  statistics (eigenvalue margins, ρ, Type-I counts, exact
  worst-nulls), never from a raw cross-implementation
  sampled minimum alone.

## §2 Claims (a), (b), (c) — the centre, its worst-null, its clamp

Gate deciding reads (`gate45/results/g45_numbers.json`):

**(a) The centre.** (μ_S, μ_N, μ_M) = (0.8015689430763502,
1.3179449338854314, 3.574968377899082) applied to H2's totals
(S → μ_S·S, N → μ_N·N, M → 1 + μ_M·(M − 1)).

- Batch SET-244 read on gate machinery: joint (NEC) min
  −6.812652656191745×10⁻⁵ at r = 15.487804878048781 (stored
  −6.812652656191736×10⁻⁵, diff −8.1×10⁻²⁰); DEC min
  −4.611098054059921×10⁻⁶ at r = 18.170731707317074, Type-I
  (stored −4.611098054060287×10⁻⁶, diff +3.7×10⁻¹⁹); ρ min
  +9.678145350055485×10⁻⁵ (stored +9.678145350055573×10⁻⁵,
  diff −8.8×10⁻¹⁹); Type-I count 3311 (stored fraction
  0.49849442938873834 × 6642 = 3311, exact).
- Controls. (1,1,1): at the stored NEC argmin shell
  r = 16.21951219512195 the gate's shell NEC is
  −1.9422459891767224×10⁻⁴ (stored L_stat(H2)
  −1.9422459891767227×10⁻⁴, diff +2.7×10⁻²⁰); DEC diff
  +5.4×10⁻²⁰; ρ diff −2.7×10⁻²⁰; Type-I count 3262 exact.
  The mixed centre (0.9323593026620368, 1.1444417317708335,
  1.1445068359375): DEC diff −6.2×10⁻¹⁹, ρ diff +8.1×10⁻²⁰,
  Type-I count 3359 exact; at the stored argmin point
  (−1.9470056065537118, −10.702464686683815, 6.28048780487805)
  the gate's NEC is −1.757073553794523×10⁻⁴ (diff ~+1×10⁻¹⁹)
  and its exact worst-null is −1.7703703917379307×10⁻⁴
  (diff 0.0 vs Gate-43's stored value). The seed
  (0.9323593026620368, 1.1444417317708335, 2.289013671875):
  DEC diff +5.0×10⁻¹⁹, ρ diff +4.1×10⁻²⁰, Type-I fraction
  0.47395362842517313 exact; at its named argmin point the
  sampled NEC reproduces at diff +3.8×10⁻¹⁹ and the exact
  worst-null at diff +3.5×10⁻¹⁹. All three controls are
  reproduced at roundoff on frame-invariant fields, as
  charged.

**Ruling (a): SURVIVES** as G45-A.

**(b) Worst-null.** At the centre's SET NEC argmin point
(the gate's shell argmin at r = 15.487804878048781), the
gate's exact worst-null (fib-642 scan + Nelder–Mead polish,
independently coded) is −7.17315328450248×10⁻⁵ vs stored
−7.173153284502476×10⁻⁵, diff −4.1×10⁻²⁰. The improvement
over the seed survives at pointwise grade (stored margins:
+5.304123×10⁻⁵; the gate's centre and seed worst-nulls
reproduce individually at roundoff).

**Ruling (b): SURVIVES** as G45-B.

**(c) End-clamp.** Construction exactly as Gate-41/43 (the
gate's construction is cross-validated in C-3). The centre
end-clamped on gate machinery: joint −6.968822658140869×10⁻⁵
(stored −6.968822658140883×10⁻⁵, diff +1.4×10⁻¹⁹),
NEC-carried at r = 15.487804878048781; DEC min
−4.827335644720391×10⁻⁶ (diff −4.7×10⁻¹⁹); ρ min
+9.678542130126975×10⁻⁵ (diff +1.2×10⁻¹⁸). Clamp cost:
1.561700×10⁻⁶ (gate −6.968822658140869×10⁻⁵ −
−6.812652656191745×10⁻⁵; stored 1.5617000194914637×10⁻⁶).
Clamped margins: over the seed's unclamped level
−1.241372×10⁻⁴: **+5.4449×10⁻⁵ — SURVIVES** (stored prose
+5.445×10⁻⁵). Over L_stat(H2) = −1.942246×10⁻⁴:
**+1.2454×10⁻⁴ — SURVIVES**. Both margins exceed the C-10
band by more than an order of magnitude; the survival is
not statistic-dependent. As at the mixed centre (G43-E),
the gain is carried by the scaling direction, not the
correction vectors' end knots.

**Ruling (c): SURVIVES** as G45-C, with the clamped level
and both margins stated on its face.

## §3 Claim (d) — the registered box

The box (Phase 394 registration SS4): μ_S ∈ [0.80, 1.10],
μ_N ∈ [0.95, 1.35], μ_M ∈ [1.60, 3.60]; 349 stored SET-244
reads (RAY 8, G1 41, G2 9, G3 26, G5 127, G4 138).

- **Recount of the stored record** (`p394_screens.jsonl`,
  md5-verified inputs): 349 reads, all feasible; **318**
  with joint above the seed's −1.241372×10⁻⁴; worst DEC
  over all reads **−5.3917400712468285×10⁻⁵** (the G2 read
  at (0.9323593026620368, 1.1444417317708335,
  1.9890136718749998)); **zero** reads with DEC below
  −0.5 and zero below −0.9999 — no DEC-saturated read
  under either threshold in the lineage's use.
- **Independent re-read of the worst-DEC subject** on gate
  machinery: DEC min −5.3917400712470874×10⁻⁵ at
  r = 19.634146341463413, Type-I (diff −2.6×10⁻¹⁸ vs
  stored). The box's least-DEC read is an ordinary
  Type-I read, nowhere near the past-branch pinning of
  Phase 387's saturated regime.
- **The pure μ_M ray, independently re-read** at
  (μ_S⁰, μ_N⁰) = (0.9323593026620368, 1.1444417317708335)
  for μ_M ∈ {2.0, 2.289013671875, 2.5, 2.75, 3.0, 3.25,
  3.5, 3.6} (`g45_ray_box.json`): gate joints
  −1.449554×10⁻⁴ → −1.240604×10⁻⁴ → −1.154605×10⁻⁴ →
  −1.117751×10⁻⁴ → −1.096222×10⁻⁴ → −1.069928×10⁻⁴ →
  −1.040741×10⁻⁴ → −1.039017×10⁻⁴ — **strictly increasing,
  no turn inside the box**, increments decaying (last step
  +2.31×10⁻⁷ over 0.1 in μ_M). Six of the eight joints
  reproduce the stored ray at roundoff (diffs ≤ 5.4×10⁻¹⁹);
  the seed point and μ_M = 3.5 differ by 7.7×10⁻⁸ and
  5.9×10⁻⁸, inside the C-10 band, at points whose
  frame-invariant statistics reproduce exactly (seed, §2).

**Ruling (d): SURVIVES** as G45-D.

## §4 Claim (e) — the box-edge disclosure

The centre's μ_S = 0.8015689430763502 sits 0.00157 above
the registered box's lower edge μ_S = 0.80, in the tight
flat cluster the phase disclosed (four further stored
reads within 3.1×10⁻⁷ of its joint, at μ_S ≤ 0.81). The
phase's own G4 polish (a fresh Nelder–Mead from the
incumbent, 150 evaluations) returned exactly its start
point, so the centre is a local optimum **of the searched
box at polish resolution** — and nothing in the record
measures the surface for μ_S < 0.80. μ_N = 1.3179 (edge
1.35) and μ_M = 3.5750 (edge 3.60) sit inside their edges;
the ray (§3) was still rising, slowly, at the μ_M edge,
which is a second, independent reason the box does not
close the surface.

The disclosure is therefore not a caveat on the phase's
honesty — the phase carried it on its own face — but a
standing rider on the claim set, in the G41-E/G43-E
manner: **any quotation of the centre's level (G45-A),
its worst-null (G45-B), or its clamped level (G45-C)
must carry G45-E with it.** A centre found in an extended
box (Phase 395's charge) will supersede or confirm this
one under its own gate; until then the level is quotable
only as the optimum of the registered box.

**Ruling (e): SURVIVES** as rider G45-E, attached to
G45-A, G45-B and G45-C.

## §5 The quotable set (G45-*), with the fence

**FENCE (verbatim, travels with every quotation):** band pose
[10, 20] only; Phase 356's full-extent caveats travel with
every level in this set; every level is negative; no EC pass,
no member, no drive or transport implication.

- **G45-A (the ray-seeded centre).** At the per-profile
  stationary scaling (μ_S, μ_N, μ_M) =
  (0.8015689430763502, 1.3179449338854314,
  3.574968377899082) of the harvested centre H2's total
  profiles, the stationary joint level (SET-244, SAMPLER-M,
  band [10, 20]) is **−6.812653×10⁻⁵** (NEC min
  −6.812652656191736×10⁻⁵ at r = 15.487804878048781; DEC min
  −4.611098054060287×10⁻⁶, Type-I, at
  r = 18.170731707317074; ρ min +9.678145350055573×10⁻⁵),
  above the Phase 393 seed (−1.241372×10⁻⁴) by
  +5.601066×10⁻⁵, above Phase 389's mixed centre
  (−1.757074×10⁻⁴) by +1.075808×10⁻⁴, and above L_stat(H2)
  = −1.942246×10⁻⁴ by +1.260980×10⁻⁴. **G45-E is part of
  this claim wherever its level is quoted.**
- **G45-B (pointwise grade).** The exact worst-null at
  G45-A's NEC argmin is −7.173153284502476×10⁻⁵, above the
  seed's worst-null (−1.2477276305772507×10⁻⁴) by
  +5.304123×10⁻⁵: the improvement survives at pointwise
  grade. **G45-E is part of this claim wherever its level
  is quoted.**
- **G45-C (the end-clamp rider — part of G45-A wherever
  its margin is quoted).** End-clamping H2's correction
  splines (all first/last knots zeroed) and applying the
  G45-A scaling to the clamped totals reads a joint level
  of −6.968823×10⁻⁵ (NEC-carried), a clamp cost of
  1.562×10⁻⁶: the clamped level remains above the seed's
  unclamped level by +5.4449×10⁻⁵ — the margin over the
  seed survives clamping — and remains above L_stat(H2)
  by +1.2454×10⁻⁴ — the margin over the centre bar
  survives clamping with it. **G45-E is part of this
  claim wherever its level is quoted.**
- **G45-D (the registered box).** In Phase 394's
  registered box (μ_S ∈ [0.80, 1.10], μ_N ∈ [0.95, 1.35],
  μ_M ∈ [1.60, 3.60]), all 349 stored reads are feasible
  and none is DEC-saturated (worst DEC
  −5.3917400712468285×10⁻⁵, an ordinary Type-I read at
  r = 19.634146341463413); 318 of the 349 reads beat the
  seed's level; and the pure μ_M ray from the seed rises
  monotonically to the box edge (−1.039017×10⁻⁴ at
  μ_M = 3.6) with no turn inside the box.
- **G45-E (the box-edge rider — part of G45-A, G45-B and
  G45-C wherever their levels are quoted).** The G45-A
  centre presses the registered box's μ_S lower edge
  (μ_S = 0.8015689430763502 against the edge 0.80), and
  the pure μ_M ray was still rising at the box's μ_M
  edge: the centre is the optimum **of the registered
  box**, and whether the level keeps rising outside the
  box — below μ_S = 0.80, or beyond μ_M = 3.60 — is
  unmeasured in this claim set.

## §6 Provenance and artefacts

- Stored bytes verified (md5): p394_confirmation.json
  611424f0c0ac49ead895e2ed2b3a9172 · p394_clamp.json
  7e04481ec112da6ad34cdaaa59c52e6f · p394_anatomy.json
  81312726c1206879f3a236559e04b434 · p394_controls.json
  8549ffaed25f5a102a91cbccbfae40d2 ·
  p394_search_summary.json b4a9017d092b74a9ea450b7b785071be
  · CHECKPOINT394.md 815bdbf1a498ee6abfad8970047c93ea ·
  p394_memo.md 7b9da9e7e1cff62f062020ba8f660065 ·
  p393_ray.json 090d0fb234179b631a53e99fc010934e ·
  p389_confirmation.json f2139b1fac8f8ae2bad7a490e8be80ed
  · p379_confirmation.json
  1bcb8b3900026cc78e6aacb33654ad72 ·
  p344_confirmation.json bca93c039daf9c8baf68f4e567abe873.
  The gate's profile assembly consumes the stored vectors
  from the confirmation artefacts; the state files agree
  at 0.0 (C-0).
- Gate artefacts: `gate45/work/g45_lib.py` (machinery);
  `gate45/results/g45_numbers.json` (the §2 deciding
  reads), `g45_ray_box.json` (the §3 ray re-reads, the
  worst-DEC re-read, the mixed-centre stored-point read,
  the FD cross-check), `g45_clamp_margins.json`,
  `g45_summary.json`.
- Three-goal accounting: Goal 1 (FTL drive) — the pressure
  wall's best band stationary level improves to
  −6.812653×10⁻⁵ and the improvement is now gate-verified
  with its end-clamp rider and its box-edge rider; the
  level remains negative, so no front pass, no member, no
  transport. Goal 2 (wormhole) — no throat claim is
  touched by this gate. Goal 3 (subluminal record) —
  untouched; Procaccia's 0.1363 stands.
- DESK: NO DATA CONTACT.
