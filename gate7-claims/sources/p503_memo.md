# P50-3 — His design freedoms, our audit (mechanism attribution)

**Worker:** P50-3 · **Date:** 2026-11-22 · **float64 everywhere** ·
nothing uploaded, no external contact.
**Python:** programme venv `~/workspace/warp-pilot/venv/bin/python`
(numpy 2.5.5 / scipy 1.18.1) for every script in this item.
**Code:** `phase50/p503_lib.py`, `p503_anchors.py`, `p503_audit.py`,
`p503_secondpath.py`, `p503_polish.py`, `p503_opt.py`, `p503_check.py`.
**Data:** `results/p503_anchors.json`, `p503_audits_nonspline.json`,
`p503_audits_spline.json`, `p503_pol_*.json`,
`p503_anatomy_nontypeI.json`, `p503_B_b010_badpoint.json`.

## Plain language first

We took our best warp shell — the thick (10,30) shell that Gate-6
verified at β = 0.07 and 0.08 — and tried, one at a time and in
combination, the three design freedoms that distinguish Procaccia's
certified 0.1363 design from ours: (a) zero radial pressure,
(b) a computer-optimised (spline) shift profile instead of our fixed
cosine, and (c) his thinner (10,20) geometry at lower mass. Every
variant was tested at β = 0.10, 0.12 and 0.1363 under our own bars
(gate-standard auditor, full fine point set, all four energy
conditions, Type-I fraction, sampled-null cross-check, second path
for anything that passes).

**The headline:** exactly one freedom buys speed in our formalism,
and it is the optimised shift. With a spline shift (K = 5 knots,
polished from the cosine profile), our unchanged TOV (10,30) shell
becomes **fully legal at β = 0.10** — verified on the second,
4th-order path as well — where the cosine version fails. Nothing
else reached 0.10: zero radial pressure made every row it touched
*worse*, the (10,20) geometry made every row it touched *worse*,
and the full Procaccia combination (zero pressure + spline +
(10,20), in both smoothing variants) failed at all three speeds.
No variant reached 0.12 or 0.1363 as run. The β = 0.10 spline row
is a **scan signal under attack** (locked language): a legal row
above β = 0.08, verified under this phase's bars, not a discovery.

Why the cosine rows fail above 0.08 is itself a clean result: the
margins at most points stay positive, but a growing patch of the
inner shell (radii ≈ 10.25–16.25) stops being Hawking–Ellis
Type-I — the stress tensor there acquires a flux-dominated,
non-Type-I character as the shift grows — and the sampled-null
NEC over the core goes negative. The spline's small reshaping of
the shift (its knot values differ from the cosine's by only
~0.01–0.02) removes exactly that patch at β = 0.10.

**Attribution caveat (important):** the spline optimisation as run
was the registered L-BFGS-B polish stage, started from the
cosine-equivalent spline (plus warm starts across β). The full
registered differential-evolution stage (seed 50, popsize 15,
maxiter 200) was started and abandoned under multi-worker VM
contention (load average ≈ 19; a detached DE process measured
≈ 8 % of one core) and is logged as a follow-up with its
requirements (§7). Every verdict below rests only on full fine
audits of specific finalist configurations, never on optimiser
objective values, so the reach numbers are hard; what the bounded
optimisation cannot support is any claim that a variant *cannot*
reach a β — only that the finalists produced did not. Where that
distinction matters, it is stated per row.

## 1. Machinery and anchors (all passed before any verdict)

- Generic builder (`p503_lib.build_profile`) reproduces
  `shell.py`'s `build_shell` **bit-exactly** (max abs diff 0.0 on
  ρ, P, m, a, b, ρ_ex, p_r, p_t) for the TOV + Gaussian control.
- Zero-pressure construction: P profile identically 0; the exact
  spherical p_r of the (10,30) zero-P profile is ≤ 8.6e-21 in
  absolute value everywhere (r > 1) — p_r ≡ 0 by construction, as
  registered (a′ = (m/r²)/(1−2m/r)). For the box-4 (10,20) zero-P
  profile, max |p_r| in the shell region is 1.7e-20.
- Gate-6 anchor set on the gate-standard auditor
  (`gate6/wa_auditor.py`): Minkowski max|G| = 0 exactly; static
  anchor ρ relative error 3.07e-03 at h = 0.3 (Gate-6 recorded
  ≤ 3.1e-03), principal-pressure abs error ≤ 9.2e-08; Finalist A
  whole-volume worst +2.14e-07, Type-I fraction 1.000 — all
  matching the Gate-6 record.
- The vectorised clone of the auditor used **only** for optimiser
  screening agrees with `wa_auditor` to ≤ 3.7e-19 on all margins
  over 200-point samples of two configurations, and the batched
  objective path agrees with single evaluations exactly (0.0).
  No verdict number in this memo comes from the clone.
- FD floors (non-significant-point median |NEC|, wa_run
  convention) per configuration are in the audit JSONs; the
  control's floor is 1.56e-08, the zero-P (10,30) floor 5.73e-08,
  the (10,20) floors 1.85e-08 (TOV) / 1.18e-08 (zero-P).

## 2. The test matrix as run

Base control: (10,30), M = 8.0, edge-peaked wd = 6.0 / floor = 0.2,
Gaussian smoothing (4.0, 2.32), cosine shift on [10,30], TOV
pressure (the P50-2 best configuration). Scaled variants use the
registered (0.20W, 0.116W) smoothing pair and wd = 0.3W, so the
(10,20) rows carry (2.0, 1.16) and wd = 3.0 at M = 6.0
(compactness 0.60). Spline rows: monotone-knot C² cubic spline
(clamped end slopes), K ∈ {3, 5, 8} interior knots, knot values in
[0,1] non-increasing, S(R₁) = 1, S(R₂) = 0; objective = worst
all-EC margin over significant points of the reduced set
restricted to r ∈ [R₁−0.75, R₂] (the region the shift acts on;
exterior-tail margins are shift-independent and are reported in
the full audits), with non-Type-I points entering through their
sampled-null NEC (the all-EC margin is undefined there; a constant
penalty makes the objective piecewise-flat and unoptimisable —
this is a screening device only). All finalist splines audited
came out monotone with zero overshoot.

(a)-rows carry the density profile but **not** the TOV pressure:
their pressure is identically zero by construction, stated per
row below and never pooled with TOV rows.

## 3. Reach table (full fine audits, gate-standard auditor)

A variant "reaches" a β iff a fully legal row exists there
(common bars: Type-I fraction 1.000, worst NEC/WEC/SEC/DEC > 0 at
h = 0.3 and 0.15, worst ≥ 3× FD floor, sampled-null core NEC > 0,
second path for passing rows).

| Variant | (a) | (b) | (c) | β = 0.10 | β = 0.12 | β = 0.1363 | Reach |
|---|---|---|---|---|---|---|---|
| control | – | – | – | FAIL | FAIL | FAIL | ≤ 0.08 (Gate-6) |
| (a) zero-P | ✓ | – | – | FAIL | FAIL | FAIL | < 0.10 |
| (b) spline K5 | – | ✓ | – | **LEGAL ✓ verified** | FAIL | FAIL | **0.10** |
| (c) (10,20) | – | – | ✓ | FAIL | FAIL | FAIL | < 0.10 |
| (a)+(b) | ✓ | ✓ | – | FAIL | FAIL | FAIL | < 0.10 |
| (a)+(c) | ✓ | – | ✓ | FAIL | FAIL | FAIL | < 0.10 |
| (b)+(c) | – | ✓ | ✓ | FAIL* | FAIL | FAIL | < 0.10 |
| (a)+(b)+(c) Gauss | ✓ | ✓ | ✓ | FAIL | FAIL | FAIL | < 0.10 |
| (a)+(b)+(c) box-4 | ✓ | ✓ | ✓ | FAIL* | FAIL | FAIL | < 0.10 |

*β-specific polish finalists at 0.10 were also run for (b)+(c)
(warm from its 0.1363 finalist) and (a)+(b)+(c)-box4 (fresh
cosine start), and warm β-specific finalists for (a)+(b) at 0.10
and for (b) at 0.12: all failed their full audits (§5). For (b),
K = 3 and K = 8 finalists (optimised at 0.1363) were also audited
at all three β: both fail, closest at 0.10 (Type-I 0.992 for
K = 3, 0.980 for K = 8, core margins positive) — as run, K = 5 is
the best knot count, with no monotone trend in K (screening
objectives at 0.1363: K3 −3.55e-05, K5 −2.63e-05, K8 −3.62e-05;
local-polish caveat of §7.2 applies).

## 4. Attribution

- **(b) spline shift: Δreach = +0.02 or more** (0.08 → 0.10 on the
  control shell; the control's own ceiling inside this matrix is
  < 0.10 and Gate-6 verified it at 0.08). It is the only freedom
  that buys anything. Mechanism: it repairs the Type-I /
  sampled-NEC failure patch in the inner shell (radii
  10.25–16.25) that ends every cosine row above 0.08. Cost: none
  in mass or compactness (same M = 8.0, compactness 0.80); the
  worst margin of the legal row is the same exterior-tail SEC
  +2.58e-07 as the control's; its core worst margin at 0.10 is
  DEC +1.57e-05 at r = 10.25 (vs the cosine control's core margins
  being moot under Type-I failure, sampled core NEC −1.65e-05).
- **(a) zero radial pressure: Δreach ≤ 0 — it costs, everywhere.**
  Alone on (10,30) it turns the control's Type-I-only failure at
  0.10 into an outright SEC margin failure (−4.79e-06 at
  r = 12.25) with a worse Type-I fraction (0.887 core vs 0.952).
  Combined with the spline (AB vs B) the screening objective at
  0.1363 is worse (−5.21e-05 vs −2.63e-05) and the audits fail at
  all three β with inner-edge SEC failures. Combined with (c)
  (AC vs C) it is likewise worse or equal at every β. In our
  builder, removing the TOV pressure removes the lapse gradient
  support (a′ loses its 4πrP term) that the inner shell's SEC
  margin was standing on. (a)-rows carry the edge-peaked density
  profile but not the TOV pressure, per the registration.
- **(c) geometry (10,20) at M = 6.0: Δreach ≤ 0 — it costs too.**
  Alone (C vs control) it fails at 0.10 on an inner-edge DEC
  margin (−7.32e-06 at r = 10.25) where the control fails only on
  type; its Type-I fractions are worse than the control's at
  every β (core 0.835 / 0.710 / 0.600 vs 0.952 / 0.855 / 0.741).
  The thinner shell concentrates the same shift drop into half
  the radial width, doubling the shift-gradient load per unit
  radius at the inner edge. It does buy a lower ADM mass
  (6.0 vs 8.0 geometric units; 0.60 vs 0.80 compactness) — that
  is its entire ledger entry: cheaper, and slower.
- **Interactions:** the pairs are not additive — they are
  dominated by the costs. (a)+(b) < (b); (b)+(c) < (b);
  (a)+(c) is the worst (10,20) cosine row at 0.12 (SEC
  −9.23e-06 at r = 12.75). The all-three rows inherit both costs:
  the Gaussian all-three finalist fails at 0.10 on SEC
  −4.12e-06 (r = 10.75); the box-4 all-three finalist fails at
  0.10 on Type-I (0.778) with an outer-edge core NEC of only
  +5.68e-06 (r = 19.75). Box-4 vs Gaussian smoothing inside the
  all-three row: box-4 is modestly better at 0.10 (Type-I 0.778
  vs 0.791 — comparable; core margins positive vs an SEC
  failure), i.e. his smoothing is not the active ingredient
  either. **In our formalism, Procaccia's 0.1363 reach is not
  explained by (a) or (c); if it is explained by any of the three
  registered freedoms, it is (b) — and our bounded (b) reaches
  0.10, not 0.1363.** The remaining gap is consistent with his
  optimisation being far heavier (full DE-class search over a
  spline-modulated shift *source*, per the Gate-6 record) and/or
  with construction details outside the registered freedoms
  (P50-1's scope); it is not evidence against his claim, and this
  item does not audit his claim.

## 5. Per-variant cost ledger

At β = 0.10, h = 0.3, gate auditor (the full 38-row ledger,
all β, both h, is `results/p503_ledger.json`, produced by
`p503_check.py` over the audit JSONs). "Worst" is the
whole-volume worst margin with its binding site; "core worst"
the shell-region (R₁ ≤ r ≤ R₂) worst; sampled = core
sampled-null NEC minimum.

| Row | M (geom) | compact. | Worst (site) | Core worst (site) | Type-I | Sampled |
|---|---|---|---|---|---|---|
| control | 8.0 | 0.80 | +2.58e-07 (SEC, r=37.0) | +1.05e-05 (NEC, 12.25) | 0.964 | −1.65e-05 |
| (a) zero-P | 8.0 | 0.80 | −4.79e-06 (SEC, 12.25) | −4.79e-06 (SEC, 12.25) | 0.914 | −3.36e-05 |
| **(b) spline K5 (β-opt)** | 8.0 | 0.80 | **+2.58e-07 (SEC, 37.0)** | **+1.57e-05 (NEC, 13.25)** | **1.000** | **+2.02e-06** |
| (b) spline K5 (0.1363-opt) | 8.0 | 0.80 | +2.58e-07 (SEC, 37.0) | +1.57e-05 (DEC, 10.25) | 1.000 | +2.66e-06 |
| (b) spline K3 | 8.0 | 0.80 | +2.58e-07 (SEC, 37.0) | +3.59e-06 (NEC, 10.25) | 0.992 | −3.80e-06 |
| (b) spline K8 | 8.0 | 0.80 | +2.58e-07 (SEC, 37.0) | +1.51e-06 (NEC, 13.25) | 0.980 | −4.33e-06 |
| (c) (10,20) TOV | 6.0 | 0.60 | −7.32e-06 (DEC, 10.25) | −7.32e-06 (DEC, 10.25) | 0.882 | −1.30e-04 |
| (a)+(b) | 8.0 | 0.80 | −2.21e-06 (SEC, 10.25) | −2.21e-06 (SEC, 10.25) | 0.901 | −2.23e-05 |
| (a)+(b), β-opt | 8.0 | 0.80 | −2.68e-06 (SEC, 13.75) | −2.68e-06 (SEC, 13.75) | 0.896 | −1.86e-05 |
| (a)+(c) | 6.0 | 0.60 | −7.49e-07 (DEC, 23.0) | +1.62e-05 (SEC, 10.25) | 0.846 | −2.12e-04 |
| (b)+(c) | 6.0 | 0.60 | +6.29e-07 (SEC, 6.0) | +3.52e-06 (DEC, 10.25) | 0.915 | −3.32e-05 |
| (b)+(c), β-opt | 6.0 | 0.60 | −6.77e-06 (DEC, 10.25) | −6.77e-06 (DEC, 10.25) | 0.927 | −2.63e-05 |
| (a)+(b)+(c) Gauss | 6.0 | 0.60 | −4.12e-06 (SEC, 10.75) | −4.12e-06 (SEC, 10.75) | 0.791 | −1.21e-04 |
| (a)+(b)+(c) box-4 | 6.0 | 0.60 | +1.48e-07 (SEC, 4.0) | +5.68e-06 (NEC, 19.75) | 0.778 | −1.35e-04 |
| (a)+(b)+(c) box-4, β-opt | 6.0 | 0.60 | −9.84e-06 (SEC, 10.25) | −9.84e-06 (SEC, 10.25) | 0.700 | −5.19e-05 |

FD floors per configuration: (10,30) TOV rows 1.56e-08;
(10,30) zero-P rows 5.73e-08; (10,20) TOV rows 1.85e-08;
(10,20) zero-P rows 1.18e-08 (Gauss) / 1.46e-08 (box-4). The two
legal (b) rows' worst margins are 16.6× their floor.

At β = 0.12 the best (b) row (warm-polished at 0.12) still fails:
Type-I 0.849, core sampled NEC −1.30e-05, core margins positive
(+3.60e-06 NEC at r = 29.75 — the binding site has moved to the
outer edge). At β = 0.1363 the best (b) row fails with Type-I
0.750 and core sampled NEC −2.73e-05. Full per-β numbers for
every row are in the ledger JSON.

## 6. The best verified row this item produces

Two distinct spline finalists are fully legal at β = 0.10; by
the BEST ordering (same β, same mass; larger worst margin —
whole-volume worsts are identical, so the core worst decides)
the best verified row is the β-specific one:

**Configuration:** (R₁,R₂) = (10,30), M = 8.0 geometric units
(= 1.0773×10²⁸ kg per the Gate-6 record), compactness 0.80,
edge-peaked density (wd = 6.0, floor = 0.2), Gaussian smoothing
(4.0, 2.32), TOV pressure, **spline shift K = 5** with knot values
[1, 0.9457, 0.7729, 0.5141, 0.2572, 0.0689, 0] at
r = [10, 13.33, 16.67, 20, 23.33, 26.67, 30] (stick-break
z = [0.0543, 0.1827, 0.3349, 0.4997, 0.7321, 0.5]), β = 0.10.
**Scan signal under attack.**

- Gate auditor, full fine set (1,404 pts): Type-I fraction 1.000
  at h = 0.3 and 0.15; whole-volume worst +2.58e-07 (SEC, exterior
  tail r = 37.0, shift-independent) = 16.6× the FD floor
  (1.56e-08); core worst +1.570e-05 (NEC, r = 13.25); core
  sampled-null NEC min +2.02e-06.
- Second path (4th-order direct-∂², wa_diag pattern): Type-I
  1.000 at both h; worst +2.592e-07 / +2.593e-07; core
  +1.541e-05 / +1.531e-05; sampled core NEC +1.95e-06 /
  +1.93e-06 — every deciding margin agrees in sign, no caveats.
- h-ladder at the core binding site (NEC, radii 12.25–14.25):
  +1.507e-05 / +1.517e-05 / +1.521e-05 / +1.522e-05 at
  h = 0.3 / 0.15 / 0.075 / 0.0375 — converged.

**Corroborating second legal row** (the 0.1363-optimised K = 5
spline, knot values [1, 0.9436, 0.7717, 0.5132, 0.2568, 0.0688,
0], audited at β = 0.10): gate Type-I 1.000 at both h, core worst
+1.568e-05 (DEC, r = 10.25), ladder at that site converged
(+1.568e-05 → +1.603e-05, Richardson ≈ +1.604e-05); second path
agrees on every deciding margin sign (worst +2.592e-07, sampled
core NEC +2.08e-07 at h = 0.3). One documented artefact on this
row only: at 4th-order h = 0.3 exactly one significant point
(r = 10.25) reads non-Type-I (fraction 0.999); the point-level
ladder (`p503_B_b010_badpoint.json`) shows the 4th-order auditor
itself reads Type-I there at h ≤ 0.15 with NEC +1.664e-05,
matching the gate auditor at every h (NEC +1.665e-05, sampled
+2.66e-06). Coarse-stencil artefact, recorded, not hidden. Two
independent finalists landing legal at the same β is the
robustness statement for the (b) mechanism.

## 7. Failure protocol — anatomies and follow-ups

1. **Cosine-family ceiling mechanism (anatomy).** Above β = 0.08
   the cosine rows fail by Hawking–Ellis type, not by margin
   sign: non-Type-I significant points appear in the inner shell
   (control at 0.1363: 269 points, radii 10.25–16.25 plus a small
   outer-edge group; per-radius counts in
   `p503_anatomy_nontypeI.json`), and the core sampled-null NEC
   goes negative (−1.65e-05 at 0.10 → −5.34e-05 at 0.1363 for the
   control; worse for every (a)/(c) variant). Scaling is monotone
   in β and in shift-gradient concentration. Follow-up suggested
   by the mechanism (run in part here): reshape S(r) to spread
   the shift drop — exactly what (b) does; the residual failure
   of the B finalist at 0.12 sits at the *outer* edge
   (NEC +1.42e-07 at r = 29.75, Type-I 0.850), i.e. the binding
   site moved outward once the inner patch was repaired.
2. **Registered DE not completed (machinery/process failure, not
   a physics result).** The full differential_evolution stage
   (seed 50, popsize 15, maxiter 200, then polish) was launched
   for (b) at 0.1363 and abandoned: on this VM, shared with the
   parallel Phase-50 workers (load ≈ 19), a detached DE process
   received ≈ 8 % of one core; projected completion was many
   hours per (variant, K, β). What ran instead: the registered
   L-BFGS-B polish stage from the cosine-equivalent spline, warm
   starts across β, K ∈ {3, 5, 8} for the lead variant — code
   `p503_polish.py`; the DE driver remains at `p503_opt.py`,
   validated (batched objective = single objective exactly).
   **Reopening condition / requirements:** re-run `p503_opt.py`
   per (variant, β, K) on an uncontended machine (or offloaded
   runner); ≈ 18,000 objective evaluations ≈ 25 CPU-minutes per
   run at the measured uncontended rate. Any variant whose reach
   is quoted as "< 0.10" in §3 is quoted for the finalists
   produced, and this follow-up is the named route to strengthen
   those bounds.
3. **(a)+(c) at 0.10 — nearest extra anatomy.** The AC row's
   whole-volume worst at 0.10 is an exterior DEC point
   (−7.49e-07 at r = 23.0, in the (10,20) smoothing tail beyond
   R₂) while its core is positive (+1.62e-05): the tail is a
   separate, milder failure layered on the core Type-I failure
   (0.785). Noted for the Le-caveat file: tail behaviour is
   exactly where Le's stricter standard also presses.
4. No row is closed as "impossible": the structural statement
   supported here is narrower — within the finalists produced,
   (a) and (c) each move every measured quantity the wrong way,
   and (b) is the only freedom with a positive Δ. A heavier
   optimisation (follow-up 2) is the named experiment that could
   move the (b)-family numbers; nothing in this item's data
   suggests it would rehabilitate (a) or (c), whose failures are
   margin-sign failures at the *cosine* level already, before
   optimisation enters.

## 8. C12 accounting

Every row in this item is a prescribed-geometry audit: the
required source is the Einstein tensor of the stated metric, and
the verdict is that this source satisfies NEC/WEC/SEC/DEC under
the programme's shell standard on the audited volume.
Conservation is automatic (Bianchi), as in Phase 26 / Gate-6.
No matter model, formation route, or stability is claimed for
any row — including the zero-pressure rows, whose "pressure" is
a property of the construction (p_r ≡ 0 in the exact spherical
read), not a matter model. Le (arXiv:2605.25417)'s stricter
source-consistency standard is carried as a standing caveat, not
a bar. The β = 0.10 spline row is a **scan signal under attack**
in the phase's locked language; nothing here is a discovery, and
nothing was uploaded or published.
