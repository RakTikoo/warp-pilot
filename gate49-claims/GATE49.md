# GATE-49 — Independent re-judgement of the Phase 403 claim set

Charged at ledger entry 1051 (2026-11-26). Phase 403 claimed
that the pose is a priced, searched lever on the pressure
wall: carrying Phase 395's certified centre C395 by Phase
402's registered transport, the band joint rises
monotonically in width to the registered cap W28 (pose
[1, 29]) without turning, and a per-profile scaling
re-optimisation at that pose finds a new centre at
(μ_S, μ_N, μ_M) = (0.5000090643041506, 1.8999807308424006,
4.892092241322827) with joint −3.676112×10⁻⁶ — carrying, on
its own face, a box-edge disclosure and an SS7 physicality
margin of only 8.0×10⁻⁶ above the half-of-H2 bar, with the
box's μ_S edge placed at the criterion's boundary by
construction. This gate re-judges that claim set with fresh
machinery only, every deciding value reproduced
independently on the VM frame of record, and rules on the
SS7 question as a charged item (claim (e)) on its own
measurements.

## Verdict

- **(a) The Step-1 width curve: SURVIVES.** The gate's
  reads reproduce all eight transported joints at
  |diff| ≤ 6.5×10⁻¹³ and all eight exact worst-nulls at
  |diff| ≤ 6.6×10⁻¹³ (§3); the curve is monotone
  increasing in both statistics on the gate's own reads,
  unturned to the cap; ρ_min reproduces at both ends of
  the spend (9.78 → 4.71 ×10⁻⁵, |diff| ≤ 1.8×10⁻¹²).
- **(b) The new centre: SURVIVES** — with riders G49-E
  and G49-F attached wherever its level is quoted. The
  deciding values reproduce: exact worst-null
  −5.242074×10⁻⁶ (diff +2.5×10⁻¹³, h-refinement spread
  ≤ 3.9×10⁻¹³); adversary Type-I depth re-derived
  independently at −3.928935×10⁻⁷ against the stored
  −3.928911×10⁻⁷ (diff −2.4×10⁻¹², §4); end-clamped joint
  −3.811020×10⁻⁶ (diff +4.7×10⁻¹³). The sampled joint
  −3.676112×10⁻⁶ reproduces at diff +2.5×10⁻¹³ under its
  named frame convention (SAMPLER-M, the eulerian_that
  association); its argmin is non-Type-I on the gate's
  machinery too, so the joint is quoted only under that
  convention, never as a deciding value (C-10).
- **(c) The gain decomposition and the box recount:
  SURVIVE.** The decomposition arithmetic is exact on
  the stored values (diffs 0.0) and reproduces from the
  gate's own reads at 10⁻¹³ (transport +2.042495×10⁻⁵;
  re-optimisation +5.708787×10⁻⁶; total +2.613374×10⁻⁵).
  The stored record recounts exactly: 334 reads, all
  feasible, zero DEC-saturated, worst DEC
  −4.32733270543391×10⁻⁷ (diff 0.0) — and that screen's
  triple is independently re-read on gate machinery at
  diff −3.7×10⁻¹⁴, its DEC argmin Type-I (§5).
- **(d) The box-edge disclosure: SURVIVES — and is
  issued as rider G49-E**, attached on the face of
  G49-A, G49-B and G49-C wherever the centre's level is
  quoted: the centre presses the registered box's μ_S
  lower edge (by 9.064×10⁻⁶) and its μ_N upper edge (by
  1.927×10⁻⁵) — the optimum **of the registered box**
  at pose [1, 29] (§6).
- **(e) The SS7 question: RULED — the centre is NOT an
  artefact candidate, and it is quotable only as AT
  THE CRITERION with the construction disclosed,
  issued as rider G49-F** (part of G49-A, G49-B and
  G49-C wherever their levels are quoted). The peak
  reproduces at diff 0.0 and the criterion as
  pre-registered is met; but the clearance is, by an
  exact identity the gate verifies, nothing but the
  polish's stopping distance above a box edge the
  search itself placed at the criterion's boundary —
  the pass is the fence holding, not the surface
  clearing, and it carries no margin (§7).

## §1 Machinery and calibrations

**Organisation (used by no earlier deciding read):**
brute-force Cartesian finite-difference differential
geometry. The metric field is assembled pointwise from
the stored profile **values only** — no lineage
derivative (S′, S′′, N′, N′′, M′, M′′) is consumed
anywhere in the gate's machinery. The Einstein tensor
is formed from centred differences of the metric on
Cartesian stencils at two step sizes (h = 0.02,
h/2 = 0.01) with Richardson extrapolation; T = G/(8π).
The Eulerian frame and the Hawking–Ellis margins are
re-implemented from their definitions; the worst-null
is computed by an exact secular-equation solver for
the quadratic on the sphere (the trust-region form),
cross-checked against a dense 8192-point Fibonacci
scan with local polish. Earlier organisations, for
the record: lineage = hand-derived radial formulas;
Gate-43 = Cartesian loops; Gate-45 = Cartesian AD
jets/einsum; Gate-46 = sympy symbolic spherical;
Gate-47 = sympy symbolic Cartesian with cse; Gate-48
= spherical Taylor jets. The shared items are the
claim's own definitions — the metric ansatz
(g_tt = −N², g_tx = −β·S, γ_ij = δ_ij + (M−1)n_i n_j,
β = 1.1), the per-profile scaling, 402's transport,
the SET-244 lattice, the frame association and the
margin definitions — re-stated in the gate's code,
not imported as machinery. VM frame only.

Calibrations (record: `results/g49_calibration.json`):

- **C-0 (trivial limit).** Synthetic flat profiles
  (S ≡ 0, N ≡ 1, M ≡ 1) at 14 scattered points:
  max |G| = 0.0 exactly.
- **C-0b (curved vacuum).** Schwarzschild (m = 0.7)
  in this exact ansatz (N = √(1−2m/r),
  M = (1−2m/r)⁻¹, S = 0): after Richardson,
  max |G| ≈ 10⁻¹² at every radius ≥ 3.5; the single
  near-horizon point (r = 2.0, 2m/r = 0.7, stencil
  reaching toward the horizon) carries 1.2×10⁻⁶.
  The FD algebra forms the Einstein tensor of a
  curved vacuum metric correctly.
- **C-1 (worst-null solver).** Against a tight
  Nelder–Mead polished reference on 30 random
  symmetric matrices: max deviation 5.3×10⁻¹⁵. (The
  first pass compared the solver against a coarse
  2002-point scan minimum and measured the scan's
  own discretisation, 0.019; corrected before any
  deciding read — §9.)
- **C-2 (stored control, h-convergence).** At
  C395's stored NEC argmin point
  (−15.383488301698574, 2.2228398846289754,
  −2.4277326106594397; stored artefact data via
  Gate-46's shellpoints), the gate's worst-null
  against the stored −3.0896210095678075×10⁻⁵:
  h = 0.16 → +5.0×10⁻⁸; h = 0.08 → +2.6×10⁻¹²;
  h = 0.04 → +1.3×10⁻¹³; h = 0.02 → −6.0×10⁻¹⁴;
  h = 0.01 → +4.8×10⁻¹³. Production reads use
  h = 0.02 with Richardson. The per-read Richardson
  error indicator (a worst-component bound over all
  6642 points, including stencils straddling spline
  knots) ranged 7.6×10⁻⁷–1.05×10⁻⁵ across the
  gate's reads; the deciding scalars' observed
  diffs against the record are ≤ 6.6×10⁻¹³
  throughout — the indicator is a bound on the
  worst tensor component, not the error of the
  deciding functionals, whose own convergence is
  C-2's table.

## §2 Controls

All controls are gate-machinery reads (SET-244,
h = 0.02, Richardson). Stored targets from the
md5-verified record.

- **C395 at home [10, 20]:** joint −2.980985033×10⁻⁵
  (diff −5.5×10⁻¹⁴); worst-null at the argmin
  −3.089621016×10⁻⁵ (diff −6.0×10⁻¹⁴); DEC min
  −1.776685×10⁻⁶ (diff −3.0×10⁻¹³); ρ_min
  +9.780857562×10⁻⁵ (diff −1.5×10⁻¹²); NEC argmin
  shell r = 15.7317, non-Type-I, as stored.
- **(1,1,1) at home:** joint −1.942245991678×10⁻⁴
  against L_stat(H2) = −1.9422459891767227×10⁻⁴
  (diff −2.5×10⁻¹³).
- **402's W12 row [9, 21]:** joint diff +1.5×10⁻¹³;
  worst-null diff +1.5×10⁻¹³; DEC diff −2.9×10⁻¹³;
  ρ diff −1.4×10⁻¹².
- **402's W14 row [8, 22]:** joint diff +4.0×10⁻¹³;
  worst-null diff +4.1×10⁻¹³; DEC diff −1.1×10⁻¹³;
  ρ diff −9.2×10⁻¹³.
- **Type-I counts** (not deciding values): the
  gate's counts differ from stored by +5 (C395
  home), +3 (W12), +1 (W14) — FD-noise
  classification flips at borderline points, the
  pattern of Gate-44's calibration note C-1; the
  deciding margins agree at 10⁻¹³ at every one of
  those reads. All Step-1 counts from W18 on, and
  the W28 count, reproduce exactly (§3); the
  winner's count differs by +1 (§4).

## §3 Claim (a) — the width curve

Gate reads of C395 transported (stored → gate,
diffs in units of 10⁻¹³):

| W | pose | joint stored | Δjoint | worst-null stored | Δwn | ρ_min stored |
|---|---|---|---|---|---|---|
| 10 | [10, 20] | −2.980985×10⁻⁵ | −0.55 | −3.089621×10⁻⁵ | −0.60 | +9.780858×10⁻⁵ |
| 12 | [9, 21] | −2.472805×10⁻⁵ | +1.49 | −2.660769×10⁻⁵ | +1.55 | +8.886992×10⁻⁵ |
| 14 | [8, 22] | −2.050977×10⁻⁵ | +4.03 | −2.268065×10⁻⁵ | +4.05 | +8.110300×10⁻⁵ |
| 16 | [7, 23] | −1.792647×10⁻⁵ | +6.55 | −1.970635×10⁻⁵ | +6.58 | +7.431160×10⁻⁵ |
| 18 | [6, 24] | −1.571427×10⁻⁵ | +4.71 | −1.702465×10⁻⁵ | +4.68 | +6.833890×10⁻⁵ |
| 20 | [5, 25] | −1.393772×10⁻⁵ | −2.54 | −1.522698×10⁻⁵ | −2.69 | +6.305841×10⁻⁵ |
| 24 | [3, 27] | −1.128452×10⁻⁵ | −2.82 | −1.253404×10⁻⁵ | −2.68 | +5.418057×10⁻⁵ |
| 28 | [1, 29] | −9.384899×10⁻⁶ | −2.56 | −1.054503×10⁻⁵ | −2.42 | +4.705368×10⁻⁵ |

On the gate's own reads the joint and the
worst-null both increase strictly at every step —
monotone, unturned to the registered cap, with no
disagreement flag anywhere (the worst-null improves
in step with the joint, as stored). The NEC argmin
shells reproduce exactly (15.7317 → 16.3659 across
the curve). DEC recedes along the curve (gate W28
DEC min −3.878662×10⁻⁷, diff −5.3×10⁻¹⁴); ρ_min
falls 9.780858×10⁻⁵ → 4.705368×10⁻⁵ (gate diffs
−1.5×10⁻¹² / +1.4×10⁻¹²): widening spends density
margin to buy pressure level, as claimed. Type-I
counts: stored/gate 4067/4072, 4093/4096,
4097/4098, 4098/4099, 4100/4100, 4103/4103,
4104/4104, 4109/4109 — exact from W18 on; the
early diffs are the §2 classification flips.
**Ruling (a): SURVIVES.**

## §4 Claim (b) — the centre at [1, 29]

Triple taken exactly from Phase 403's stored
files: (0.5000090643041506, 1.8999807308424006,
4.892092241322827), pose [1, 29].

- **Sampled joint** −3.676112×10⁻⁶: gate
  −3.676111275×10⁻⁶, diff +2.5×10⁻¹³ — under the
  named frame convention (SAMPLER-M, the
  eulerian_that association, Gate-43 C-10). The
  binding point (r = 17.0488) is non-Type-I on the
  gate's machinery as on the phase's, so per C-10
  the joint is **not** a deciding value.
- **Exact worst-null at the argmin (deciding):**
  gate −5.242074216×10⁻⁶ against stored
  −5.24207446894373×10⁻⁶, diff +2.5×10⁻¹³;
  h-refinement at the point (h = 0.04 / 0.02 /
  0.01) gives diffs +7.1×10⁻¹⁴ / +2.5×10⁻¹³ /
  −3.9×10⁻¹³ — converged.
- **Adversary Type-I depth (deciding), re-derived:**
  the gate's own polish (Nelder–Mead over
  (r, θ, φ) in the pose band, Type-I-restricted,
  started from the gate SET's five shallowest
  Type-I points, the phase's stored polished
  point, and five probe starts on the DEC shell)
  converges from every Type-I start to one basin
  at r ≈ 25.70; the tight pass gives depth
  **−3.928935×10⁻⁷** against the stored
  −3.928911×10⁻⁷ (diff −2.4×10⁻¹² — the gate's
  polish lands a hair deeper, inside polish
  tolerance; the stored depth is confirmed as the
  basin's depth). No deeper Type-I basin was
  found; the deeper raw minima the probes touched
  (to −3.80×10⁻⁶) are at non-Type-I points and are
  excluded by the statistic's definition. Over
  Type-I points the configuration is within
  3.93×10⁻⁷ of legal, as claimed.
- **End-clamped joint:** gate −3.811019229×10⁻⁶
  against stored −3.8110196987227636×10⁻⁶ (diff
  +4.7×10⁻¹³); clamp cost 1.349×10⁻⁷ reproduced.
  The clamped level remains above C395's home
  level by +2.599883×10⁻⁵.
- DEC min −3.809243×10⁻⁷ (gate diff −2.5×10⁻¹³,
  at r = 25.9268); ρ_min +4.705527×10⁻⁵ (gate diff
  −1.5×10⁻¹⁴); Type-I count 4604 against stored
  4603 (+1 classification flip, §2 pattern).
- Anatomy spot-check: the gate's binding-site
  radius and the DEC shell agree with the stored
  anatomy; the joint is NEC-bound at the
  transported image of C395's home argmin, as
  claimed.

**Ruling (b): SURVIVES**, with riders G49-E and
G49-F attached.

## §5 Claim (c) — decomposition and recount

- **Decomposition:** on the stored values the
  arithmetic is exact (transport
  +2.0424951526593445×10⁻⁵, re-optimisation
  +5.708787224231813×10⁻⁶, total
  +2.613373875082526×10⁻⁵; gate recomputation of
  the stored figures returns diffs 0.0). From the
  gate's own reads: transport +2.042495×10⁻⁵,
  re-optimisation +5.708788×10⁻⁶, total
  +2.613374×10⁻⁵ — the re-optimisation increment
  exceeds the C-10 band (±3×10⁻⁶) on both records:
  the scaling genuinely pays at the new pose; the
  gain is not pose-only.
- **Recount of `p403_screens.jsonl`** (stored
  bytes): 334 rows; 334 feasible; 334 floors-ok;
  **zero DEC-saturated** (dec_min < −0.9999 census
  rule); worst DEC −4.32733270543391×10⁻⁷ (diff
  0.0 against the claim), a G2 screen at
  (0.601180962300002, 1.5934531363763935,
  4.387238651223381); 334 rows beat C395's home
  level; 329 beat the transported seed; exactly
  one row carries the winner's triple, and it is
  the record's best row (joint
  −3.676111526923747×10⁻⁶, stage G4).
- **Independent re-read of the worst-DEC screen:**
  gate SET read of its triple at [1, 29] gives
  DEC min −4.327333071×10⁻⁷ (diff −3.7×10⁻¹⁴),
  its DEC argmin Type-I on gate machinery, joint
  diff +8.0×10⁻¹³.

**Ruling (c): SURVIVES.**

## §6 Claim (d) — the box edges

Gate arithmetic on the stored triple against the
registered box μ_S ∈ [0.50, 1.10], μ_N ∈
[0.95, 1.90], μ_M ∈ [1.60, 6.50]: μ_S sits
9.06430415059667×10⁻⁶ above the lower edge; μ_N
sits 1.9269157599310915×10⁻⁵ below the upper edge;
μ_M is interior (3.292 above the lower edge,
1.608 below the upper). Both figures reproduce
the stored disclosure exactly. **Ruling (d):
SURVIVES — issued as rider G49-E.**

## §7 Claim (e) — the SS7 question, ruled

The question: the centre's peak |β·S| =
0.44268227409480604 against the half-of-H2 bar
0.4426742490267404 — a clearance of 8.025×10⁻⁶ —
with the box's μ_S lower edge placed at the
criterion's boundary by construction. Is the
centre quotable as CLEARING the criterion, only
as AT the criterion with the construction
disclosed, or as an artefact candidate?

**The gate's measurements.**

1. The peak reproduces at **diff 0.0**: the gate's
   grid maximum over the pose band (endpoints
   included) returns 0.44268227409480604 exactly.
   H2's peak likewise reproduces at diff 0.0
   (0.8853484980534808), and the bar is exactly
   half of it. The peak of |β·S| over the band is
   attained at the band's inner edge (home
   r = 10.0) for every object on this line — the
   criterion measures that edge value; that is its
   registered definition and nothing in the ruling
   turns on it.
2. **The identity is exact:** peak ratio =
   μ_S (gate: 0.44268227409480604 /
   0.8853484980534808 = 0.5000090643041506, the
   winner's μ_S to all shown digits — Gate-47's
   measurement, re-verified). It follows that the
   clearance is *identically*
   (μ_S − 0.50) × H2's peak
   = 9.0643041506×10⁻⁶ × 0.8853484980534808
   = 8.025×10⁻⁶: **the clearance is the polish's
   stopping distance above the box's μ_S edge,
   rescaled. It contains no information beyond
   that distance.**
3. **The construction is in the stored record:**
   Phase 403's registration (SS5) placed the box's
   μ_S lower edge at 0.50 expressly because
   "μ_S < 0.5 puts the peak |β·S| below the
   half-of-H2 bar by construction — artefact
   territory per 396/397, excluded from the search
   rather than searched and flagged". Twelve
   stored screens sit exactly at μ_S = 0.50, every
   one with stored peak exactly the bar
   (0.4426742490267404); the G3 stage walked the
   diagonal to the corner (0.50, 1.90) at joint
   −3.787147×10⁻⁶; the G4 polish settled
   9.064×10⁻⁶ inside it. The surface's improving
   direction at the winner points out of the box
   through the μ_S edge (the diagonal's increments
   grow toward the corner): the region below the
   edge — the artefact territory — is where the
   surface was still heading, and it is unmeasured
   in this claim set **by design**.

**The ruling.** The criterion (396 SS7, carried
verbatim by 403 SS6) is a pre-registered threshold
on the peak: at or above the bar, a centre is not
an artefact candidate; below it, it is. Gate-47
enforced exactly that binary against Phase 396's
centre (peak ratio 0.400, below the bar → G47-F).
This gate does not move a pre-registered bar after
the fact — the discipline G47-F itself rests on —
and on the gate's own measurement the winner's
peak is at-or-above the bar. **The centre is
therefore NOT an artefact candidate.**

But "clears the criterion" is quotable only in
the threshold sense, and any quotation implying
margin or evidential weight would misstate the
record: a search fenced to the non-degenerate
region by construction could not have returned a
sub-bar centre, so the pass certifies that the
fence held, not that the surface cleared anything.
The centre sits **at** the criterion — its peak
is the bar plus the polish's hair — and the
construction is part of the claim. **Ruling (e):
the centre is quotable only as AT THE CRITERION
with the construction disclosed — rider G49-F,
in the G47-F manner, attached to G49-A, G49-B
and G49-C wherever their levels are quoted.** For
contrast, stated in the rider: the last centre on
this line clearing the bar with a genuine margin
is Phase 395's (peak ratio 0.6012, clearance
8.958×10⁻² — four orders of magnitude above this
centre's 8.0×10⁻⁶). The phase's own comparison
also stands, with the rider: the winner's level
(−3.676112×10⁻⁶) is above Phase 396's flagged
level (−7.431892×10⁻⁶) while sitting at the bar
that centre failed.

## §8 The quotable set (G49-*), with the fence

**FENCE (verbatim, travels with every quotation):**
every level in this set is a band read at its
stated pose under transport (the centre's pose is
[1, 29]); Phase 356's full-extent caveats travel
with every level; every level is negative; no EC
pass, no member, no drive implication.

- **G49-A (the width curve).** Carried by Phase
  402's registered transport, Phase 395's centre
  C395 (0.601180962300002, 1.5934531363763935,
  4.887238651223381) reads joint levels (SET-244,
  SAMPLER-M, band at each pose) of −2.980985×10⁻⁵
  (W10, [10, 20]), −2.472805×10⁻⁵ (W12),
  −2.050977×10⁻⁵ (W14), −1.792647×10⁻⁵ (W16),
  −1.571427×10⁻⁵ (W18), −1.393772×10⁻⁵ (W20),
  −1.128452×10⁻⁵ (W24) and −9.384899×10⁻⁶ (W28,
  [1, 29]) — monotone increasing, unturned at the
  registered cap, with the exact worst-null
  improving in step at every width
  (−3.089621×10⁻⁵ → −1.054503×10⁻⁵) and ρ_min
  falling from +9.780858×10⁻⁵ to +4.705368×10⁻⁵:
  widening spends density margin to buy pressure
  level. Whether the trend turns past W28 is
  unmeasured in this claim set (the cap is
  geometric: centre-15 widenings end at a′ = 1).
- **G49-B (the new centre).** At pose [1, 29], the
  per-profile scaling (μ_S, μ_N, μ_M) =
  (0.5000090643041506, 1.8999807308424006,
  4.892092241322827) of H2's total profiles reads
  joint level **−3.676112×10⁻⁶** (SET-244,
  SAMPLER-M frame convention; NEC-bound at
  r = 17.0488, a non-Type-I point), exact
  worst-null at the argmin **−5.242074×10⁻⁶**,
  adversary Type-I depth **−3.928911×10⁻⁷** (the
  Type-I sector within 3.93×10⁻⁷ of legal), DEC
  min −3.809243×10⁻⁷ at r = 25.9268, ρ_min
  +4.705527×10⁻⁵ — above C395's home level by
  +2.613374×10⁻⁵ and above L_stat(H2) =
  −1.942246×10⁻⁴ by +1.905485×10⁻⁴. **G49-E and
  G49-F are part of this claim wherever its level
  is quoted.**
- **G49-C (the end-clamp rider — part of G49-B
  wherever its margin is quoted).** End-clamping
  H2's correction splines and applying the G49-B
  scaling at pose [1, 29] reads a joint level of
  −3.811020×10⁻⁶, a clamp cost of 1.349×10⁻⁷: the
  clamped level remains above C395's home level
  by +2.599883×10⁻⁵ — the margin over the anchor
  survives clamping. **G49-E and G49-F are part
  of this claim wherever its level is quoted.**
- **G49-D (the decomposition and the registered
  box).** Of the centre's +2.613374×10⁻⁵ total
  gain over C395's home level, transport alone
  contributes +2.042495×10⁻⁵ and the
  re-optimisation at the pose a further
  +5.708787×10⁻⁶ (beyond the C-10 band — the
  scaling pays at the new pose too). In Phase
  403's registered box (μ_S ∈ [0.50, 1.10],
  μ_N ∈ [0.95, 1.90], μ_M ∈ [1.60, 6.50]) at pose
  [1, 29], all 334 stored reads are feasible and
  none is DEC-saturated (worst DEC
  −4.327×10⁻⁷, a Type-I read); 334 beat C395's
  home level and 329 beat the transported seed.
- **G49-E (the box-edge rider — part of G49-A,
  G49-B and G49-C wherever their levels are
  quoted).** The G49-B centre presses the
  registered box's μ_S lower edge
  (0.5000090643041506 against 0.50) and its μ_N
  upper edge (1.8999807308424006 against 1.90):
  the centre is the optimum **of the registered
  box** at pose [1, 29], and whether the level
  keeps rising outside the box — below μ_S = 0.50
  or above μ_N = 1.90 — is unmeasured in this
  claim set (for μ_S, unmeasured by the
  registration's design: see G49-F).
- **G49-F (the SS7 at-the-criterion rider — part
  of G49-A, G49-B and G49-C wherever their levels
  are quoted; the gate's ruling on the SS7
  question).** The G49-B centre is quotable as
  **at** the SS7 physicality criterion, not as
  clearing it with margin, and not as an artefact
  candidate: its band peak |β·S| is
  0.44268227409480604, which is the pre-registered
  half-of-H2 bar (0.4426742490267404, half of
  H2's peak 0.8853484980534808) plus
  8.025×10⁻⁶. The peak ratio to H2's equals μ_S
  exactly, so the clearance is identically the
  centre's distance above the box's μ_S edge
  (9.064×10⁻⁶) rescaled by H2's peak — and that
  edge was placed at the criterion's boundary by
  the search's own registration (Phase 403 SS5),
  which excluded the sub-bar region from the
  search rather than searching and flagging it;
  twelve stored screens sit exactly on the edge
  with peak exactly the bar. The criterion as
  registered is met, so the centre is not an
  artefact candidate (contrast Phase 396's
  centre, peak ratio 0.400, below the bar, rider
  G47-F); but the pass certifies the fence, not a
  margin — the last centre on this line clearing
  the bar with a genuine margin is Phase 395's
  (peak ratio 0.6012, clearance 8.958×10⁻²).
  Criterion, restated for this line: a centre is
  quotable as a design improvement only while its
  peak |β·S| is at least half of H2's peak, and a
  centre whose peak sits within the polish's hair
  of the bar, on a box edge placed at the bar,
  carries this rider.

## §9 Provenance and artefacts

Machinery: `gate49/work/g49_lib.py` (FD Einstein
tensor, frame, margins, worst-null, SET read),
`gate49/work/g49_calibrate.py` (C-0/C-0b/C-1/C-2),
`gate49/work/g49_run.py` (controls, width curve,
winner, clamp, SS7 peaks), `gate49/work/g49_polish.py`
(adversary depth re-derivation, h-refinement),
`gate49/work/g49_recount.py` (screens recount,
decomposition, box edges, worst-DEC re-read).
Records: `gate49/results/g49_calibration.json`,
`gate49/results/g49_numbers.json`,
`gate49/results/g49_polish.json`,
`gate49/results/g49_recount.json`,
`gate49/results/g49_winner_set.npz`.

Stored bytes consumed, md5-verified before use:
phase403/CHECKPOINT403.md
a776f5e9915ed8ed33757a3804ddb5e4 · phase403/results/
p403_memo.md 839a084f7ea4e967af443eea0892b37d ·
p403_step1.json f08f1c8a3de468960c17d672d9c38d83 ·
p403_confirmation.json c39a358bfa6e8ad4ac3881ddbaf04ad6 ·
p403_anatomy.json a04e1ff6eac7ba35828328045966d746 ·
p403_clamp.json 51b3b04a5fdf52b58e570f06c19d1673 ·
p403_search_summary.json d20c40c375c031f6af2c92a30ec415b2 ·
p403_screens.jsonl 40767ad5b159240a0e77d0a90c70d68b ·
p403_controls.json 9b82f0b6307fbf2a4a1d30b4243edfb ·
p403_controls_laptop.json f900802320f68a5b1f8fdf60bca785d5 ·
phase403/work/p403_registration.md
40c55ac0ace8ff655770c297cdcef7e9 ·
phase402/results/p402_map.json
2cc03c7caa04a7a47bfbe84617575212 ·
phase402/work/p402_registration.md
14b25fcaf40619998b8231ab047c2fca ·
gate46/results/g46_shellpoints.json
38b0912999c6d9d957425fca48565f5f ·
phase395/results/p395_confirmation.json
6d3e2c209ffbcd36ff2f59bdee09a0bb. The gate's
profile assembly consumes the stored profile
vectors through the lineage's value evaluation
only (components S, N, M of the stored totals);
no stored derivative is read by any gate
computation.

Process incidents, disclosed: (i) the gate's
first SS7 peak computation used a golden-section
refinement that walked off the band endpoint and
understated H2's peak by 2.65×10⁻⁶; the peak is
attained at the endpoint (r = 10.0), the grid
maximum with endpoints included reproduces the
stored peak at diff 0.0, and no deciding read
used the faulty value (the winner's and C395's
peaks came from the pose grid and were exact at
first pass). (ii) Calibration C-1's first pass
compared the exact worst-null solver against a
coarse scan minimum and reported the scan's
discretisation (0.019) as a solver deviation;
re-run against a polished reference before any
deciding read (max deviation 5.3×10⁻¹⁵). No read
was lost, repeated silently, or reused from
either incident. The laptop was not used: all
deciding reads are VM reads, per the charge.

DESK: NO DATA CONTACT.
