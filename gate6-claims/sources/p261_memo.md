# P26-1 — THE BEST SUBLUMINAL DRIVE — worker memo

Run 2026-11-21/22, per CHECKPOINT26 §P26-1 as registered. float64
everywhere, system python3 (numpy 2.2.6 / scipy 1.14.1). Scripts:
`p261_ha.py`, `p261_ha2.py`, `p261_fine.py`, `p261_fine2.py`,
`p261_hc.py`, `p261_hd.py`, `p261_build_ledger.py`. Raw data:
`p261_*_raw.json`; assembled ledger: `p261_ledger.json`.
No bar was moved; no post-hoc amendment was needed or made.

## Plain language first

The best fully legal moving shell this programme has ever verified
is faster than the old frontier. The old record was β=0.05. A thick
shell (inner radius 10, outer radius 30, mass 8.0 geometric units =
1.08×10²⁸ kg, compactness 0.80) in the same Finalist family passes
the full audit at **β=0.07** — every energy condition, everywhere
audited, at two resolutions, with the fine-grained audit that killed
the fake Finalist B. At β=0.08 the same family's best shell develops
a tiny negative pocket at the inner edge of the wall that only shows
up at the finer resolution, so 0.07 is the ceiling and 0.08 is
honestly closed. The other homes do not beat it: the curved-background
home still cannot move at all (no engine exists to solve it), the
areal-embedding home's pass ends between β=0.02 and 0.03, and the
breathing home's ceiling is β=0.02 with dynamics buying nothing.
The β=0.07 configuration is a **Gate candidate** — nothing stronger
is claimed.

## Anchors (step 1 — all reproduce; machinery validated)

- Finalist A (M=2.0, (10,20), β=0.02): positive at h=0.3/0.15,
  Type-I 1.000; whole-volume worst +1.11e-07 (exterior tail,
  r=24.2) — the stored core margins (+1.20e-05) are larger, as
  recorded in Phase 1 (tail-limited worst is this family's norm).
- Finalist B2 (M=2.7, β=0.03): same pattern, worst +1.28e-07 tail.
- Frontier β=0.05 (5,10) M=1.91: my first attempt used the wrong
  profile (canonical wd=1.5/floor=0.2) and failed — a worker error,
  caught against the stored record. The stored winner's actual
  profile (wd=1.0, floor=0.1, M=1.9125) reproduces the stored worst
  **exactly**: +5.930e-07 (SEC @ r=12.1) at h=0.075 vs stored
  +5.9299e-07; +4.17e-07 at h=0.3, +5.83e-07 at h=0.15, Type-I 1.000.

## H-a — GR flat Finalist family: ceiling β = 0.07

Search volume: 144 canonical screening evals (β-ladder × 4
geometries × compactness 0.30–1.00) + 588 refinement evals (10
designs: edge-peaked ×2, matched, smoothbox × shift windows cos
[R1,R2] / cos extended / quintic, Gaussian smoothing pair scaled
0.20W/0.116W) + 64 coarse-dense audits + 18 fine audits (radii step
0.5 across the shell, inner-edge cluster at R1+0.25, 26 directions,
h=0.3/0.15, eigenvalue margins + sampled-null cross-check).

Per-rung outcome (fine audit is the arbiter):
- β=0.05: passes (frontier family; min compactness 0.383 at (5,10)).
- β=0.06: passes — (10,30) M=6.5 edge-peaked (fine worst +3.03e-07,
  core +1.87e-05 at h=0.15), (10,30) M=8.0 smoothbox, and (5,10)
  M=2.5 edge-peaked wd=1.0/floor=0.1 (fine worst +1.88e-05 — the
  healthiest β=0.06 row, but β loses to 0.07 in the BEST ordering).
- β=0.07: passes ONLY at (10,30) M=8.0 edge-peaked canonical
  (below). M=6.5 at the same geometry fails the fine audit
  (SEC −1.45e-05 @ r=10.25, h=0.15); smoothbox M=8.0 fails at both
  h (DEC −2.12e-06 / WEC −1.09e-05 @ r=10.25).
- β=0.08: best row (10,30) M=8.0 edge-peaked passes the coarse
  dense audit (+9.9e-08, both h) but the FINE audit finds NEC
  −5.26e-07 @ r=10.25 at h=0.15 (core +1.84e-05 NEC at h=0.3) —
  sign-unstable at the inner edge; fails bar 2 (sign stability).
- β=0.09: NEC −1.10e-06 @ r=10.25 (h=0.15, M=9.5), Type-I 0.998.
- β=0.10: mid-shell failure, SEC −2.99e-05 @ r=18.8, h-stable
  (matches Phase 1's β=0.1 anatomy at a different mass).

**Ceiling anatomy (H-a):** one site binds the whole ladder — the
inner edge of the wall, r ≈ R1 + 0.25, the same site class as
Phase 1's r≈10.5 failures. Below the ceiling the core margins
there are ~+2e-05; the pocket deepens monotonically with β once
it opens (0 at 0.07 for M=8 → −5.3e-07 at 0.08 → −1.1e-06 at
0.09). Thick shells (W=2R1) and compactness ~0.8 are what buy the
extra speed over the Phase-1 frontier (which used W=R1,
compactness 0.383): the frontier's "terminates between 0.05 and
0.1" is refined — it terminates between 0.07 and 0.08, and only
in the thick-shell corner. Compactness 1.00–1.05 rows mostly fail
to build (min(1−2m/r) ≤ 0.02 in build_shell) at W=R1 geometries.

## THE BEST CONFIGURATION (complete ledger)

- Home: H-a, GR flat named shell family (Finalist lineage).
- β = 0.07. Geometry (R1, R2) = (10, 30). ADM mass M = 8.0 geom
  = **1.0773×10²⁸ kg** (5.68 M_jup). Compactness M/R1 = 0.80.
- Profile: edge-peaked density wd=6.0, floor=0.2; Gaussian
  smoothing s_rho=4.0, s_P=2.32; cosine shift on window [10,30]
  (exactly the matter support). ρ_peak = 7.137e-05.
- Fine audit (1,404 pts, radii step 0.5, 26 dirs):
  - h=0.3: NEC +4.349e-07, WEC +4.349e-07, SEC +2.591e-07,
    DEC +4.349e-07 (all whole-volume; binding point is the
    exterior tail at r=37.0, point (36.11, 7.94, −1.42) — the
    family's dust-like Gaussian tail, margin →0⁺ as in Phase 1).
    Core (10≤r≤30): NEC/WEC/SEC +3.756e-05, DEC +1.974e-05,
    all binding at r=10.25. Cavity worst +7.26e-07.
  - h=0.15: NEC +4.350e-07, WEC +4.350e-07, SEC +2.593e-07,
    DEC +4.350e-07; core DEC +1.779e-05 @ r=10.25.
  - Type-I fraction 1.000 (significant set, both h).
  - Sampled-null cross-check (core): NEC min +1.238e-05 (h=0.3),
    +9.306e-06 (h=0.15) — agrees in sign with eigenvalue margins.
  - FD floor: non-significant-point margin scale 2.6e-08 on the
    dense audit → worst margin ≈ 10× floor (bar: ≥3×); h-pair
    variation of the worst margin is 2e-10. Ratio-free check:
    absolute margins above are the verdict; no ratio is load-bearing.
- Slicing/convention flags: stationary ADM slicing of the
  programme's shell construction, Eulerian-tetrad judge.
  Solution status is the programme-standard prescribed-geometry
  status shared with Finalists A/B2 and the β=0.05 frontier
  (TOV-constructed shell; required source = its Einstein tensor;
  static sector conserves by construction). No difference-tensor
  convention is used. Data gates: case 3 (pure mathematics;
  "mathematically established; experimentally untested regime").

## H-b — curved backgrounds: ceiling β = 0 (static only), as registered

No new moving solve (registered in advance). Static Schwarzschild
passes at M_bg=1, 2 (H4), DEC zero-crossing at M_bg ≈ 2.5 (P6-2,
mechanism validated by its falsifiable M_bg=3 prediction).
Moving = open-by-missing-engine: the PG-sliced moving solve is
formulated (Phase 6) but unbuilt. Obstruction of record: H4's
β=0.02 cavity failure, NEC −1.95e-04 at M_bg=1, carried by
T_0i ~ −1e-4 — a uniform shift on a curved background is not a
gauge transformation and sources shift×curvature stress in the
cavity, while the shell core itself still passed (+3.9e-05).
AdS rows pass only on the shell-difference tensor (background's
own WEC violation in the total tensor) — flagged, never pooled.

## H-c — areal embedding: ceiling β = 0.02 (slicing-dependent)

P9-1 machinery (h4 flat re-solved shell, s=0.8846 reproduced;
M_bg=1, areal two-centre, TD auditor at t=0, h=0.2/0.1):
- β=0.02 reproduces P9-1 exactly: core worst +2.934e-05 (h=0.2,
  d=50; P9-1: +2.93e-05), cavity NEC −3.22e-07 → −2.75e-08
  (floor), Type-I 1.000, both d. PASS stands, areal slicing only.
- β=0.03: FAILS at both d — core worst −1.27e-04 (h=0.1, d=50),
  core NEC −1.33e-05, Type-I 0.935; cavity still at floor
  (−3.8e-08). β=0.04: core −3.64e-04, Type-I 0.727. β=0.05: core
  worst at the −1.0 floor, Type-I 0.542.
- PG-consistent read (d=50): fails at every β tested (core worst
  −4.23e-05 at 0.02 — raw all-EC read; P9-1's NEC-only read was
  −3.36e-06 — degrading to −6.47e-04 at 0.05); cavity raw worst
  −1.25e-04 is the edge point P9-1 separated as an FD artefact.
- Anatomy: the areal pass ends in the CORE, not the cavity — the
  failure mode does not change character with β, it grows:
  Type-I fraction 1.000 → 0.935 → 0.727 → 0.542 as β goes
  0.02 → 0.05, i.e. the moving shell's own wall tensor goes
  non-Type-I, while the cavity (the H4 failure site) never
  re-opens in areal slicing. The slicing-dependence flag is
  carried in full: this home's only pass exists in areal slicing;
  the PG read of the same configuration fails at β=0.02 already.
- Note: my H4 region split reads exterior raw worst = −1.0 at
  isolated far points at ALL β including the reproduced β=0.02
  anchor row; P9-1's verdicts rest on cavity+core (as do mine)
  and its own exterior reads were reported separately. The
  β-scaling verdict above is core-driven and unaffected.

## H-d — breathing shell: ceiling mean β = 0.02; dynamics buys nothing

δ=0.5 breathing, Finalist-A family (M=2.0, (10,20) mean), 8
instants/period, h=0.3 with worst instant confirmed at h=0.15,
frozen twins beside dynamic margins (Phase-16 separation):
- Mean β=0.02: PASSES at T=40 (worst instant +7.203e-06 @ t=10 —
  reproduces Phase 16 exactly; frozen twin +1.128e-05) and at
  T=200 (+9.816e-06; frozen +9.853e-06). Legal at every instant,
  but the frozen/static family passes too — no credit to dynamics.
- Mean β=0.025: FAILS at T=40 (dynamic −1.120e-04 @ t=30,
  h=0.15-confirmed −7.80e-05) and T=200 (−8.861e-05 @ t=150).
  Frozen twin at the worst instant ALSO fails (−8.772e-05):
  the binding geometry is a frozen-illegal breathing extreme
  (wall compressed/thinned past the static family's β≈0.025
  break); dynamics adds a further tax at T=40 (−1.12e-04 vs
  frozen −8.77e-05) but is not the binding cause.
- Mean β=0.03: FAILS at both T (−2.604e-04 / −2.370e-04);
  frozen twins fail too (−2.361e-04 at the worst instant;
  −2.97e-05 even at the T/4 instant).
- Verdict: H-d ceiling = 0.02 at both periods. No configuration
  is legal dynamically while its frozen twins fail, so per the
  registered credit rule nothing is credited to dynamics.

## Verdicts per home

- H-a: ceiling β=0.07, closed (next rung's best row fails the
  fine audit with h-resolved margins; binding EC/site named:
  NEC, inner edge r=R1+0.25). Best configuration above —
  **Gate candidate**.
- H-b: static passes only; moving open-by-missing-engine,
  obstruction named (H4 cavity numbers). No β>0 row exists.
- H-c: ceiling β=0.02, closed (β=0.03 core failure h-converged
  at two d, binding site = core/Type-I collapse; slicing flag
  carried). The β=0.02 areal pass remains a Gate-candidate-class
  result of Phase 9, not beaten here.
- H-d: ceiling β=0.02, closed (β=0.025 fails at both T with
  frozen twins failing; binding = frozen-family break, dynamics
  tax secondary).

**Overall BEST (pre-registered ordering — highest β, then lower
mass, then larger worst margin): the H-a β=0.07 (10,30) M=8.0
configuration in the ledger above.** It supersedes the Phase-1
β=0.05 frontier as the programme's best verified subluminal
configuration, at 5.7× the frontier (5,10) row's mass — the
speed was bought with thickness and compactness, not lightness.
Language: Gate candidate only; novelty + independent-verification
gate still owed before any stronger word.
