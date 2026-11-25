# GATE-36 — WORKER C MEMO: ITEM 3, THE CONDITIONING QUESTION

Question: Phase 320's Jacobian σ_min = 3.994×10⁻⁴ at its N = 6 solution
is ~68× thinner than Gate-34's 0.0272 on the weaker Phase 312 winner.
Is the thinness a property of the TARGET, the FAMILY/BUILDER, or the
SOLUTION FOUND? All computation with Worker B's builder
(`g36_spinor.py`) and the gate FD recipe (central FD on the
40-component |That|_F-normalised residual, h_j = 10⁻⁶·max(1,|θ_j|)).
Driver `g36_item3.py`; full numbers `g36_item3_results.json`; new θ's
`g36_item3_solutions.json`. Wall time 3575 s, checkpointed per
experiment. Seeds: E1 extra starts base 3603, E2 base 3604, E5 random
base 3605 (same seed construction as B: base·1000 + 100N + k).

## E1 — CENSUS, POINTWISE TARGET (p320 targets, N = 6)

B's three persisted solutions plus 12 extra random starts (2 more
successes; census closed at 5 successes when the 12 starts were spent,
per the registered "≥6 or 12 spent" rule). Successful solutions
(direct max R ≤ 10⁻⁹), σ_min in full in the results file:

| solution | σ_min | max R (direct) | \|a\|² | max \|p\| |
|---|---|---|---|---|
| warm0 (B, 257 lineage) | 3.994302×10⁻⁴ | 1.128×10⁻¹³ | 0.010204 | 6.017 |
| extra7 (new) | 3.813789×10⁻³ | 3.591×10⁻¹⁴ | 0.008090 | 5.732 |
| rand2 (B) | 6.878744×10⁻³ | 2.654×10⁻¹³ | 0.011312 | 6.555 |
| extra6 (new) | 4.617597×10⁻² | 1.622×10⁻¹² | 0.033565 | 5.243 |
| rand0 (B) | 4.940592×10⁻² | 2.117×10⁻¹² | 0.008230 | 5.597 |

**Median 6.879×10⁻³; spread ×123.7** (min 3.994×10⁻⁴ → max
4.941×10⁻²). The other 10 extra starts stalled at max R between
4.8×10⁻⁶ and 2.0×10⁻³. On this one target, σ_min at successful
solutions spans more than two decades — and the thinnest value in
the census is exactly the warm-lineage one Phase 320 reported.

## E2 — CENSUS, WEAKER TARGET (p313 targets, N = 6)

1 warm (257 lineage) + 8 random starts; 7/9 successful, no extra
starts needed:

| solution | σ_min | max R (direct) | \|a\|² | max \|p\| |
|---|---|---|---|---|
| rand1 | 1.431816×10⁻³ | 6.068×10⁻¹² | 0.007182 | 5.194 |
| rand5 | 5.292055×10⁻³ | 1.006×10⁻¹² | 0.015212 | 5.990 |
| rand6 | 7.233890×10⁻³ | 4.972×10⁻¹³ | 0.258307 | 6.196 |
| rand4 | 1.258714×10⁻² | 1.465×10⁻¹² | 0.497820 | 5.039 |
| rand3 | 1.696000×10⁻² | 2.132×10⁻¹² | 0.034810 | 5.317 |
| warm0 | 1.895872×10⁻² | 1.567×10⁻¹² | 0.032756 | 4.813 |
| rand0 | 2.846123×10⁻² | 1.871×10⁻¹³ | 0.261565 | 4.015 |

**Median 1.259×10⁻²; spread ×19.9.** The weaker target's census sits
in the same σ_min class as the pointwise census: its median is only
×1.83 above E1's median, and the two censuses overlap over most of
their range (E1's thickest solutions exceed E2's median).

## E3 — OPTIMISER / RECIPE VARIATION

- **(i)+(ii) Tight re-polish of Phase 320's stored winner** (trf,
  xtol=gtol=ftol=10⁻¹⁵, max_nfev 2000): σ_min 3.994300×10⁻⁴ →
  3.994300×10⁻⁴ (3.99429997×10⁻⁴ after); θ displacement 1.13×10⁻⁷;
  max R after 3.6×10⁻¹⁷. The thinness is not a convergence artefact —
  the stored winner is already at the bottom of its basin.
- **(iii) Solver-route variation** (dogbox refit from B's rand2):
  success (max R 8.67×10⁻¹⁵, nfev 2 — rand2 was already converged),
  σ_min = 6.878745×10⁻³, identical to the trf value at rand2. The
  σ_min belongs to the solution, not the solver route.
- **(iv) h-stability at the best E2 solution** (rand0, σ_min
  2.846123×10⁻² at h = 10⁻⁶): 2.846118×10⁻² (h = 10⁻⁵),
  2.846123×10⁻² (10⁻⁶), 2.846126×10⁻² (10⁻⁷) — stable to ~3×10⁻⁶
  relative. (Pointwise h-stability was B's: ~5×10⁻⁷ relative.)

## E4 — STRUCTURE

**SV tails (last 6).** Pointwise warm0: 0.42680, 0.21990, 0.042944,
0.011693, 0.0083539, **0.00039943** — σ_min isolated, ×20.9 below the
next value. Weaker best (rand0): 0.89221, 0.34853, 0.22839, 0.18604,
0.077330, **0.028461** — a smooth tail, σ_min only ×2.7 below the
next. **The isolated-thin-direction shape is a per-solution feature,
not a target feature:** across the censuses it appears at pointwise
warm0 (×20.9), extra7 (×5.5), rand2 (×9.9) but not rand0 (×1.3) or
extra6 (×2.8); and at weaker rand1 (×22.5) but not at the other six
weaker solutions. Verdict on tail shape: **both censuses contain
isolated-thin solutions and non-isolated ones — neither target owns
the shape.**

**Smallest right singular vector** (parameter attribution, weights =
squared components). Pointwise warm0: per mode [0.028, **0.842**,
0.001, 0.091, 0.036, 0.002] — one mode (mode 1) carries 84% of the
thin direction; per class: p 0.0005, Re a 0.777, Im a 0.223 — the
thin direction is almost purely an **amplitude** direction of a
single mode, with essentially no momentum content. Weaker rand0:
per mode [0.357, 0.048, 0.216, 0.063, 0.265, 0.051] — spread over
modes 0/2/4; per class: p 0.679, Re a 0.147, Im a 0.173 — mostly a
**momentum** direction. The two thinnest-direction anatomies are
different in kind; there is no common carrying structure.

**Smallest left singular vector** (site/component attribution).
Pointwise warm0: per-site weights [0.003, 0.485, 0.511, 0.000] —
sites S2/S3 carry it; largest components: S3 (1,1) w 0.161, S2 (1,3)
w 0.160, S2 (1,1) w 0.125. Weaker rand0: per-site [0.037, 0.368,
0.592, 0.002] — again S2/S3-dominated; largest: S3 (3,3) w 0.169,
S3 (1,3) w 0.119, S2 (1,3) w 0.095. (Both targets' S4 carries
~nothing in the thin direction.)

**Target scales.** Per-site |That|_F — pointwise: 1.998×10⁻³,
1.905×10⁻³, 1.996×10⁻³, 5.916×10⁻⁴; weaker: 3.046×10⁻³, 2.524×10⁻³,
3.046×10⁻³, 1.321×10⁻³. The weaker target is if anything *larger*
in norm, so a raw scale difference does not explain a ×68 gap in a
normalised-residual Jacobian. Component dynamic range (max|comp| /
min nonzero |comp| over all sites): pointwise 2.82×10¹⁷, weaker
6.85×10²² (both driven by ~10⁻²¹–10⁻²⁶ near-zero off-block
components; neither is the thinner-conditioned target by this read).
Per-site ρ spread (max/min): pointwise ×5.82, weaker ×3.34.

**Cross-census scatter.** σ_min vs |a|² and vs max|p|: **no monotone
pattern in either census.** Pointwise: |a|² = 0.0081 → σ 3.8×10⁻³
and 4.9×10⁻² at nearly the same |a|²; |a|² = 0.0336 → 4.6×10⁻².
Weaker: |a|² spans 0.0072–0.498 with σ interleaved 1.4×10⁻³–
2.8×10⁻² (the largest-|a|² solution, 0.498, sits mid-range at
1.26×10⁻²). max|p| spans 5.2–6.6 (pointwise) and 4.0–6.2 (weaker)
with σ_min uncorrelated. σ_min is not priced by solution size or
momentum extent.

## E5 — SCALE PROBE (pointwise targets ×4)

The exactly-scaled warm start (B's warm0 θ, amplitudes ×2, i.e.
a → √4·a) begins **at** a solution of the scaled target: max R
4.512×10⁻¹³ before any refit, |a|² = 0.040818 (= 4 × 0.010204).
σ_min at that scaled solution: **3.994063×10⁻⁴** — the unscaled
warm0 value (3.994302×10⁻⁴) to 6×10⁻⁴ relative. One random start
also succeeded on the scaled target (rand1, max R 3.5×10⁻¹²) with
σ_min = 5.808×10⁻² — again thick, again a different solution. The
×4 target scaling moves σ_min by ≲0.1% at the corresponding
solution: **overall target scale contributes essentially nothing**
(the residual is |That|_F-normalised and the scaled solution is the
same point of the family in scaled coordinates).

## ATTRIBUTION — VERDICT IN THE REGISTERED TREE'S TERMS

Deciding numbers: E1 median 6.879×10⁻³, E1 spread ×123.7; E2 median
1.259×10⁻², E2 spread ×19.9; median ratio ×1.83.

- **TARGET branch — does NOT fire.** It requires E2 median ≥ ×10
  above E1 median *with E1 tight*. The ratio is ×1.83 and E1 is the
  opposite of tight (spread ×123.7). E5 independently excludes the
  scale route (×4 target → σ_min unchanged at the corresponding
  solution), and E4 finds no common carrying structure (the two
  representative thin directions differ in kind: single-mode
  amplitude vs spread momentum).
- **SOLUTION-FOUND branch — fires exactly.** E1 spread ×123.7 ≥ ×30,
  with two solutions ≥ 10⁻² (4.62×10⁻², 4.94×10⁻²) on the *same*
  pointwise target whose reported solution sits at 3.994×10⁻⁴.
  Every non-warm-lineage solution found on the pointwise target —
  by trf, by dogbox, and on the ×4-scaled target — is ≥ ×9.5
  thicker than the reported value. E3 shows the reported value is
  not an optimiser artefact: it is a genuine property of that one
  solution (the 257 warm lineage: Phase 320's stored winner, B's
  warm0 and the E5 scaled warm start all sit at 3.994×10⁻⁴).
- **FAMILY/BUILDER branch — its median condition also holds**
  (medians within ×1.83, i.e. within ~×3): as a population, the
  builder's N = 6 solutions on both targets live in the same
  σ_min class (~10⁻³–10⁻² medians, spreads of ×20–×124), so there
  is no target-level separation for the family baseline either.

**Verdict: MIXED in the tree's terms, with the deciding branch
SOLUTION-FOUND.** The headline thinness — σ_min = 3.994×10⁻⁴, the
~68× gap to Gate-34's 0.0272 — is a property of **the solution
found** (the Phase 257 warm-start lineage), not of the pointwise
target and not of target scale. The phase's σ_min is one draw from
a census spanning 3.99×10⁻⁴ to 4.94×10⁻² on its own target; the
claim set should quote the census, not the single value. The
isolated-thin-direction tail shape likewise attaches to individual
solutions in **both** censuses, not to either target.

## FILES

Driver `g36_item3.py` (+ `g36_item3_run.log`); results
`g36_item3_results.json` (E1–E5 in full, all SV lists);
`g36_item3_solutions.json` (2 new E1 θ's, 7 E2 θ's, 1 E5 θ).
No ledger append, no launches, no publication, no user contact.
