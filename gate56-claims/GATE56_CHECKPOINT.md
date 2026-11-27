# Gate-56 checkpoint — independent verification of the Phase 418 claim set

Subagent session (depth 1) for the FTL — Warp Research
chat, charged at ledger entry 1112. Object: entry 1111
(Phase 418). Deliverables: `gate56/GATE56.md` (quotable
set G56-A…D, riders G56-R1…R5) and this checkpoint.
**No ledger append, no publication, no user contact —
the verdict returns to the parent agent.**

**VERDICT: THE SET SURVIVES AS FENCED.** All four
claims reproduce on fresh machinery; the peak is ruled
definitional (G56-R1); the 2× negative is ruled
search-scoped (G56-R2); both disclosure audits confirm
the phase's record. Admission: ADMITTED.

## 1. Machinery (fresh organisation; registration in work/g56_registration.md)

Phase 418 read through the lineage's hand-coded
Cartesian algebra (p316_lib.T_from_SNM) +
verify_metric.eulerian_that + p2352_run.margins_chunked.
Gate-56 imports none of them in a deciding path (they
appear only as calibration comparators):

- **Splines** — `work/g56_splines.py`: the gate's own
  not-a-knot cubic solver (second-derivative form,
  dense solve, registered constant-extension
  semantics), float64 + mpmath variants. Used at EVERY
  spline layer of the stored assembly (A2 K = 33, H2
  K = 17, base K_B, shape K_S).
- **Profiles** — `work/g56_lib.py`: analytic base
  profiles from their registered formulas (S_{2,2} via
  the regularised incomplete beta; plateau bump;
  M ramp with the built-in fall) and the stored
  assembly arithmetic (A2 base + K = 33 vectors from
  the phase344 confirmation; centre scaling μ = 1.15;
  H2 K = 17 vectors from the phase379 confirmation;
  the 398/414 assembly). Stored vectors are the object
  definition and are taken from the artefacts.
- **Tensor** — `work/g56_build_tensor.py` derives ALL
  first/second metric derivatives SYMBOLICALLY with
  sympy from the metric (g_tt = −N², g_tx = −βS,
  γ_ij = δ_ij + (M−1)n_i n_j) and generates
  `work/g56_tensor.py` (readable CSE source; numpy +
  mpmath evaluators). The Christoffel → Ricci →
  Einstein contraction is the gate's own einsum
  assembly. This replaces exactly the layer where the
  lineage carries hand-derived formulas.
- **Tetrad / margins** — the gate's own ADM Eulerian
  construction; own Hawking–Ellis eigenvalue margins;
  own implementation of the registered sampled
  fallback (162 Fibonacci dirs, velocities
  linspace(0, 0.95, 6)) for non-Type-I points.
- **Worst-null** — the gate's EXACT secular-equation
  solver (min of kᵀThatk over |n| = 1 via
  ||n(μ)|| = 1, μ ≤ λ_min(A), Newton-refined, value at
  the renormalised direction, KKT certificate),
  corroborated by a re-implemented fib(642) scan +
  Nelder–Mead polish.
- **SET read / adversary polish / peak** — SET-244 as
  registered; the registered polish protocol on gate
  machinery; peak on 401 / 20,001 / 200,001 radii.
- **Spot check** — `work/g56_spot.py`: the full chain
  at one point in 50-digit mpmath.

## 2. Build incidents (all resolved; recorded per gate practice)

1. Sympy wraps profile derivatives as
   `Subs(Derivative(N(_xi), _xi), _xi, r)`; direct
   `Derivative(N(r), r)` construction is rejected.
   Fixed with a structural matcher + a no-op-Subs
   collapse pass; the builder asserts no Derivative /
   Subs / applied-function atom survives substitution.
2. `PythonCodePrinter.doprint` returns a plain string;
   an early emitter took `[0]` (first character) and
   produced a syntactically broken tensor module with
   plausible-looking fragments. Caught by an ast.parse
   check before any use; fixed, plus whitespace
   flattening (printer line-wraps) and `math.sqrt` →
   module `sqrt` rewriting.
3. The generated wrappers now broadcast scalar
   (constant-component) entries to the point shape.
4. The secular solver's first form stopped its
   bisection at a 10⁻¹⁵ bracket in μ, leaving
   ‖n‖ off by ~1.4×10⁻⁹ and the value inflated by
   +3.2×10⁻¹³ — caught because the gate's own NM
   polish reproduced the stored worst-null at
   −2.7×10⁻¹⁹ while the "exact" value sat above it
   (impossible for a true minimum). Fixed with Newton
   refinement on the secular function + the deciding
   value taken at the renormalised direction; all
   worst-null diffs then fell to ≤2.2×10⁻¹⁹.
5. The laptop venv lacks mpmath; the generated tensor
   module now imports it optionally (float path never
   touches it) — regenerated and re-verified (FD +
   mp checks identical) before restaging the mirror.
6. CTL-H2 was initially mis-targeted (the (1,1)
   member of the 398 assembly is a different object
   from the H2 centre's own read, which carries its
   S sector); replaced by CTL-H2CENTRE (the full
   centre read from the gate's totals).

## 3. Calibrations (registration §3; results/g56_controls.json)

| calibration | result |
|---|---|
| CAL-1 spline vs scipy not-a-knot (value/d1/d2, 3 vectors) | ≤ 4.8×10⁻¹⁶ |
| CAL-2 gate profiles vs lineage profiles_at414 (23 scattered pts, 9 sectors) | ≤ 8.9×10⁻¹⁶ |
| CAL-3a gate T vs lineage T_from_SNM | ≤ 2.7×10⁻¹⁵ (g: 1.4×10⁻¹⁴) |
| CAL-3b gate T vs FD judge einstein_at_points | 9.9×10⁻⁴ @ h = 0.2 → 1.0×10⁻⁴ @ h = 0.1 (converging) |
| CAL-4 gate That vs verify_metric.eulerian_that (same g, T) | 0.0 |
| CAL-5 gate margins vs margins_chunked (Type-I) | 0.0, Type-I flags agree |
| CAL-5b margins at non-Type-I points (same That) | 0.0 |

The sympy-derived derivative tensors were additionally
verified against finite differences of the metric
itself (dg: 1.0×10⁻⁹ at h = 2×10⁻⁴; mpmath evaluators
agree with float64 at ≤1.1×10⁻¹⁶).

## 4. Controls (gate machinery, VM)

| control | joint diff | worst-null diff | other |
|---|---|---|---|
| CTL-405WIN | −1.6×10⁻¹⁹ | −1.3×10⁻¹⁹ | SEC −7.0×10⁻¹⁹; argmin r exact; polish +2.7×10⁻²⁰ |
| CTL-PSTAR | +3.4×10⁻¹⁹ | +2.2×10⁻¹⁹ | SEC −5.4×10⁻²⁰; peak identical |
| CTL-400STAT | +1.1×10⁻¹⁹ | — | |
| CTL-B1STAT | +5.4×10⁻²⁰ | — | SEC −7.6×10⁻¹⁹ |
| CTL-B1T1 | −7.1×10⁻⁸ (global sampled; C-10) | −1.5×10⁻¹⁸ at the phase's argmin point | sampled NEC at that point −1.8×10⁻¹⁸ |
| CTL-H2CENTRE | −7.2×10⁻⁷ (sampled; C-10) | anchor consistent (see below) | ρ −5.4×10⁻²⁰; Type-I fraction 0.4911 identical |

The B1T1 / H2-centre pattern is the C-10 mechanism,
diagnosed explicitly: at non-Type-I points the sampled
margins are taken in the Eulerian frame, whose
transverse triad is rounding-determined inside γ's
exactly degenerate transverse eigenspace; the two
pipelines' That at the B1T1 point differ by 6.1×10⁻⁶
while their T and g agree at 10⁻¹⁵. Wherever it
matters, the gate therefore anchors on (i) the stored
read reproduced AT THE PHASE'S OWN ARGMIN POINT
(identified across frames by the frame-invariant
worst-null) and (ii) the exact worst-null there. Both
reproduce at roundoff in every case (B1T1: sampled
−1.8×10⁻¹⁸, worst-null −1.5×10⁻¹⁸; H2 centre: gate
exact worst-null −1.9436×10⁻⁴ at its argmin point vs
stored −1.9433×10⁻⁴ at the phase's, shell minimum
−1.9443×10⁻⁴).

## 5. Claim reads (results/g56_reads.json)

(a) Both criterion winners reproduce at roundoff in
every deciding figure (table in GATE56.md §2(a));
locals at the binding point ≤1.1×10⁻¹³; peaks bit-
identical to the criterion float at r = 10 on all
three scans. **Peak ruled definitional (G56-R1).**
(b) Statics at diff 0.0 (B418) / roundoff (controls);
spend comparison and ordering as claimed (G56-B);
the B1 leg's two forms recorded (G56-R3).
(c) Both 2× winners confirmed at the phase's argmin
point (dir 2, r = 12.073170731707318): sampled NEC
diff +5.4×10⁻²⁰, exact worst-null diff +1.2×10⁻¹⁹.
Gate global sampled joints −3.1105×10⁻⁵ (both
winners; C-10). Gate global SEC −5.627828×10⁻⁴ vs
stored −5.578679×10⁻⁴ (sampled, non-deciding).
(d) Transect: 12/12 configurations re-derived
(statics ≤2.7×10⁻¹⁹; interior carried ≤5.4×10⁻²⁰;
B1-end carried +1.4×10⁻⁶ / +4.1×10⁻⁷, inside the
C-10 band, Type-I fractions 0.819 / 0.565 there vs
1.0 in the interior — the pattern is exactly the
non-Type-I exposure). Binning recount exact:
1,378 / 859 / 760 and every bin maximum.

## 6. Disclosure audits

(i) Seed attribution — CONFIRMED (bit-identical
vectors; §4 of GATE56.md). The gate's re-reads of the
two seed configurations: joints −1.990577×10⁻⁴ /
−5.495390×10⁻⁵ (C-10 band of the stored values),
exact worst-nulls at the gate's argmin points
−1.996845×10⁻⁴ / −5.539232×10⁻⁵.
(ii) Pattern execution — CONFIRMED (§4 of GATE56.md),
including the `total_screens` = 1,684 record note
(main driver only; the jsonl and stage_counts carry
the full 1,884).

## 7. Admission (results/g56_admission_{vm,laptop}.json)

Minimal mirror (g56_lib + g56_splines + g56_tensor +
g56_admission + the three confirmation artefacts)
staged at ~/work/gate56 on the laptop pool
(RTGaming WSL, ~/g39venv: numpy 2.5.5 / scipy 1.18.1 —
same versions as the VM venv). Endpoint read =
screen-1347 SET read. Diffs (laptop − VM): joint
−2.7×10⁻²⁰; SEC +1.7×10⁻¹⁸; ρ 0.0; worst-null
+1.4×10⁻²⁰; argmin radius and peak identical.
**ADMITTED.** Deciding reads are the VM's.

## 8. Spot check (results/g56_spot.json)

Screen-1347 NEC argmin point
(−18.06954626186276, 0.17630280320242048,
1.906805179162905), r = 18.1707317073170724…, in
50-digit mpmath end-to-end: NEC =
3.65262073438416657445881987921×10⁻⁶ (float64 gate:
3.6526207343842476×10⁻⁶; stored:
3.6526207343841256×10⁻⁶); worst-null =
3.51279675561151067283409249635×10⁻⁶ (stored
3.5127967556114907×10⁻⁶); all mixed-tensor
eigenvalues exactly real (max |Im| = 0.0 at 50
digits); ρ = 1.2011355787230574×10⁻⁴; mp-vs-float
profile diffs ≤7.4×10⁻¹⁴ (M sector, values ≈ 38.45).

## 9. File inventory

- gate56/GATE56.md — the quotable set (§1) + rulings.
- gate56/GATE56_CHECKPOINT.md — this file.
- gate56/work/g56_registration.md — charges, bars,
  machinery, verdict bars (written before computing).
- gate56/work/g56_splines.py, g56_lib.py,
  g56_build_tensor.py, g56_tensor.py (generated),
  g56_controls.py, g56_reads.py, g56_reads2.py,
  g56_spot.py, g56_admission.py.
- gate56/results/g56_controls.json, g56_reads.json,
  g56_spot.json, g56_admission_vm.json,
  g56_admission_laptop.json.
- gate56/mirror/ — the admission mirror as staged
  (VM copy; the laptop copy is at ~/work/gate56).

## 10. Notes for the parent

- Publication inputs, if the desk proceeds: the
  quotable set is GATE56.md §1 verbatim (G56-A…D +
  R1–R5 + §0 fences). Suggested ledger facts: B418
  criterion joint +3.6526207343841256×10⁻⁶ ≈ 2.98×
  the 405 winner's +1.227385×10⁻⁶ on the same
  criterion; spend floor 1.254×10⁻⁹ (≈136× below
  400's base, ≈8,660× below B1); B418 carries
  nothing at 2× (search-scoped) — 412's P\* remains
  the 2× carrier; SEC −5.294469×10⁻⁴ on the carried
  point's face.
- The one record imperfection found anywhere is
  cosmetic: p418_state.json's `total_screens` field
  (1,684) counts the main driver only. The jsonl,
  stage_counts, memo and checkpoint all carry the
  correct 1,884. No claim is affected.
- No follow-up gate work is owed on this set. The
  C-10 behaviour at non-Type-I argmins is now
  characterised with point-identified reproductions
  at three independent sites (B1T1, the 2× winners,
  the H2 centre) — future phases quoting sampled
  joints at non-Type-I argmins should expect
  cross-frame spread at the 10⁻⁷–10⁻⁶ level and
  quote the exact worst-null as the deciding anchor,
  as this gate has ruled in G56-R3.
