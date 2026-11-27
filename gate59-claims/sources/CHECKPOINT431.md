# CHECKPOINT 431 — THE DEGENERATE MATING

Charge: ledger entry 1137 (roadblock intake 1136; Phase
430's drift verdict, entry 1135). Registration:
`work/p431_registration.md` (SS0–SS8 + Amendments A1, A2 +
two incident notes + supplement note). Memo:
`results/p431_memo.md`. Full numbers:
`results/p431_results.json`, `results/p431_check_results.json`,
`results/p431_admission.json`, `results/p431_supplement.json`.
Matings of record: `work/p431_best_{A_t1_N12, B_t1_N6_L3,
A_t2_6_6, B_t2_6_6_L3}.json`. Per-start bank:
`work/p431_cands_<tag>.jsonl`. Code: `work/p431_b2.py`
(B-2 copy + registered-energy override), `work/p431_run.py`,
`work/p431_check.py`, `work/p431_supplement.py`.

## VERDICTS (bar R ≤ 1×10⁻⁹, R = max per-site Frobenius)

- **Arm A / T_req: DOES NOT ADMIT** (registered scope
  N ∈ {6, 8, 12}, 30 starts). Best 1.2732×10⁻³ (N = 8);
  confirmed mating = N = 12 representative of the same
  attractor: maxR 1.2754×10⁻³ (pairwise = direct),
  |a|² = 5.998223 (205× Fit A's 0.029266), E = 1.005853,
  spectrum scatter exactly 0.0. The mating IS stationary
  (B-2 exact across the window, two forms, supplement) —
  the failure is expressibility. Anatomy: constrained-
  Jacobian σ_min 5.41×10⁻⁴ (rank 30/30, shallow genuine
  minimum); residual ≈ isotropic in the spatial diagonals
  (A3: T11/T22/T33 = 7.40/7.34/7.36×10⁻⁴; A2 ≈ 2.0×10⁻⁴;
  A1 ≈ 3.2×10⁻⁵), T00 ≤ 4.1×10⁻⁶, off-diagonals
  ≤ 3.1×10⁻⁷. Named: **the single-energy supply cannot
  express T_req's principal pressures** (pressure locked
  to density through the one shell).
- **Arm B / T_req: ADMITS.** N = 6, counts (2,2,2),
  warm_scan: maxR 1.3730×10⁻¹⁶ pw / 1.3388×10⁻¹⁶ dir;
  |a|² = 0.013963 (0.48× Fit A); E₀ = 1.019134, rungs
  (1,1,2,2,3,3) exact; T_c = 6.165222 units; return at
  T_c +2.55×10⁻¹⁸; ladder 1…1024 ≤ 4.71×10⁻¹⁴ (Form P
  bar 1×10⁻⁶); cycles in window 5.923×10¹⁵; worst
  instant R_F = 0.20791 @ t = 2.1565 (geometry-side
  input, not a certificate term). σ_min (unconstr-form
  Jac) 0.6139.
- **Arm A / T_corr: ADMITS.** Composite (6,6), rand2:
  maxR 9.9696×10⁻¹⁵ pw / 9.9271×10⁻¹⁵ dir; |a|² fam1
  0.010003 + fam2 0.014068 = 0.024071 (0.82× C-A's
  0.029174); E = 2.189896, scatter 4.44×10⁻¹⁶; B-2
  registered-E grid dev 1.57×10⁻¹⁷, window spots = R_F(0)
  (supplement, two forms); verbatim representation
  crossing t* = 3.573×10⁷ units = 0.119 s (vs 2.42×10⁻¹⁷ s
  unconstrained). σ_min 21.61.
- **Arm B / T_corr: ADMITS.** (6,6) L3 per family, rand0:
  maxR 1.2311×10⁻¹⁵ pw / 1.2117×10⁻¹⁵ dir; |a|² fam1
  0.009963 + fam2 0.007210 = 0.017173 (0.59× C-A);
  E₀ = 1.178657; T_c = 5.330801; ladder ≤ 1.00×10⁻¹³
  verbatim / ≤ 2.75×10⁻¹⁴ registered at 2¹⁰; cycles
  6.850×10¹⁵; worst instant 0.65688 @ t = 2.9974.
  σ_min 19.09.

## Sweep by-product (SS6)

Fit A sweep vs T_corr: min 1.6945974196533054×10⁻⁴ at
t = 0. C-A sweep vs T_req: min 1.6945985678760018×10⁻⁴
at t = 0. Both = the inter-target distance; the sweeps
move away. Ponder (1136 wild attack 2) carried in the
memo as LABELLED SPECULATIVE with this negative
two-target evidence; the legal-set form unmeasured.

## Controls — ALL PASS

CTL-431-0 Fit A diffs 3.48×10⁻¹⁸ / 0.0. CTL-431-1 C-A
diffs 0.0 / 0.0. CTL-431-2 laptop ADMITTED (diff
4.181655516197936e-18 ≤ 1×10⁻¹³; mirror
/home/spark/work/p431root md5-verified; fits on VM).
CTL-431-3 B-2 self-checks = 430's stored values.
Checker ALL PASS (4/4 matings: direct residuals, exact
spectra, B-2 headlines).

## Process record (on the face)

Amendment A1: searches at least_squares defaults (1e-8)
per the 410/420 primary-fit precedent; best candidate per
size polished at 1×10⁻¹³ / max_nfev 4000; polished point
is the candidate of record (superseding JSONL record).
Amendment A2: search max_nfev 4000 → 1200 (record's fits
converged in 26–750 evals; banked pre-A2 starts stand).
Incident 1: driver crash at Arm A N = 8 warm-start (warm
projection didn't pad the primary's 6 modes to escalated
sizes) — fixed with `_pad_block` (410's warm_theta
pattern). Incident 2: silent death mid-N = 12 under
shared-VM memory pressure (free RAM 154 MB observed);
relaunched, JSONL resume verified; final run completed
all arms + sweep. Supplement: the driver's Arm A window
spots used the per-mode-phase read (unevaluable at
t ~ W); superseded by `p431_supplement.py`'s Acoef +
factored-direct reads (agreement ≤ 4.4×10⁻¹⁷); the
checker uses the Acoef form for its W spot. Kill-pattern
note: `pkill -f p431_run.py` self-matches the caller's
shell — use `pgrep -f "p431[_]run.py"`.

## Standing consequences

- 430's drift verdict now reads: a property of the
  UNCONSTRAINED fits. Persistent matings exist for both
  standing targets (T_req: ladder only; T_corr: both
  arms), at prices ≤ the drifting fits.
- 428's supply leg is satisfiable in principle for both
  targets (Route B/Form P for T_req; Route A or Form P
  for T_corr). The functional's geometry leg (GAP-3)
  still gates any sustainment claim. Test-field scope;
  a persistent supply is not a sustained geometry.
- Entry 1136 wild attack 1 (THE ACTIVE SUPPLY): premise
  falsified for both standing targets; charges only for
  a future target defeating both arms.
- Targets' status unchanged: 405 winner SEC
  −2.213557×10⁻⁴ (Gate-50); T_corr is a construction.

DESK: NO DATA CONTACT.
