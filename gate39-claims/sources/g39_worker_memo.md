# GATE-39 WORKER MEMO — INDEPENDENT RE-JUDGEMENT OF PHASE 364

Worker: Gate-39 (independent deciding machinery, written fresh in
`gate39/work/g39_lib.py`, `g39_members.py`; drivers `g39_calibrate.py`,
`g39_scan.py`, `g39_refine.py`, `g39_confirm.py`).

**HARD INDEPENDENCE:** no deciding read imports or calls p349_lib,
p364_lib, p316_lib, p341_lib, p338_lib, p258_lib, p274_lib, p2352_run or
verify_metric. The centre assembly, dwelling waveform, time-dependent
Einstein tensor (assembled from the metric's derivative tensors through
the Christoffel→Ricci algebra, vectorised), Eulerian frame,
Hawking–Ellis margins (with the sampled non-Type-I fallback, n_dir=162,
n_vel=6), SET-244 read, floor check, adversary polish and worst-null
were all re-implemented in `g39_lib.py` from the definition sources
named in the brief. An additional sympy check of the generic
Christoffel/Ricci algebra against a generic (non-metric-form)
polynomial metric agrees to max abs diff 3.47e-18.

**HEADLINE RESULT:** Phase 364's claim set **REPRODUCES** under fully
independent machinery. Every deciding number of the scan, refinement
and confirmation agrees with Phase 364's stored values at roundoff
scale (all summary-field diffs ≤ 6.5e-19 in absolute terms; per-instant
diffs ≤ 8.8e-17, on DEC-saturated values of order 1). The four claimed
members beat the stationary bars jointly at their worst instants at
J = 128, with the claimed margins, phases, C1 and floors — see SS3.
**One stored confirmation number does NOT reproduce:** Phase 364's
stored `worst_null_at_set_nec_argmin` (claimed equal to the SET NEC min
at all 8 confirmation instants) — the true pointwise worst null is
below it by 2.8e-9 … 4.2e-7 at all 8 instants (SS4). This does not
touch any MEMBER verdict input.

**Deviation from the brief, stated on its face:** the M-ramp question
in the brief is arbitrated by the anchor — r2 = 20.0 (the 364
registration) reproduces the stationary anchor to ~1e-18, while
r2 = 19.5 (the p317/p338 lineage value) fails it by ~1e-5 (NEC diff
+1.068e-5). All deciding reads use **r2 = 20.0**. (So the profile the
364 *registration* specifies is the one that reproduces 344's A2
record; the older lineage default does not.)

---

## SS1. CALIBRATIONS (all pass; `results/g39_calibration.json`)

- **C-1 Vectors:** A2's (vS, vN, vM) from `p344_confirmation.json`
  (entry A2, index 1) vs `p344_state_A2.json` final_incumbent:
  max diff **0.0**. PASS.
- **C-2 Waveform:** my μ, μ_φ, μ_φφ vs 5-point centred FD of μ
  (h = 5.0e-5, Amendment 1) on a 4096-point grid, five registered
  (D, m) shapes at a = 0.30:
  - D0.50_m0.00: FD err μ_φ 2.82e-11 (bar 1.72e-5), μ_φφ 1.03e-4
    (bar 2.40e-3), periodicity 2.22e-15, range err 0.0.
  - D0.75_m0.00: 2.77e-11 (bar 2.43e-5), 8.26e-4 (bar 6.62e-3),
    periodicity 1.78e-15, range err 0.0.
  - D0.875_m0.00: 3.66e-11 (bar 3.86e-5), 6.61e-3 (bar 2.35e-2),
    periodicity 2.66e-15, range err 0.0.
  - D0.75_m0.50: 1.39e-11 (bar 1.72e-5), 4.13e-4 (bar 3.81e-3),
    periodicity 8.88e-16, range err 0.0.
  - D0.75_m0.75: 8.79e-12 (bar 1.36e-5), 2.06e-4 (bar 2.40e-3),
    periodicity 4.44e-16, range err 0.0.
  All periodicity ≤ 1e-12 (Amendment 2 bar); μ range endpoints match
  [1 + a(2m − 1), 1 + a] exactly on the grid. PASS.
- **C-3 Stationary anchor** (my stationary SET read of A2, r2 = 20.0):
  NEC min −2.319453132752996e-4 (diff −1.08e-19, argmin r 16.2195);
  DEC min −2.2336932044559818e-4 (diff +5.42e-20, argmin r 19.3902);
  WEC min diff −4.34e-19; SEC min diff +8.67e-19;
  ρ min diff +1.22e-19. All ≤ 1e-9. Adversary polish reproduces the
  polished depth −2.2644422911711972e-4 at r = 12.2330 with diff
  +4.34e-19 (bar 1e-7). PASS. (Alternative r2 = 19.5 diffs: NEC
  +1.068e-5, DEC −1.984e-6, WEC +6.557e-5, SEC +1.115e-4, ρ −7.02e-8 —
  fails; recorded in the calibration JSON.)
- **C-4 Flat limit:** S0 = 0, N0 = 1, M0 = 1, member
  {SNM, a = 0.30, T = 40, D = 0.75, m = 0} at φ = 2.6:
  max |T| = **0.0 exactly**. PASS.
- **C-5 Reduction:** anchor member (a = 0) through my time-dependent
  tensor at all 32 J = 32 instants: max diff vs the C-3 SET reads
  **8.67e-19** (bar 1e-9). PASS.
- **C-6 FD cross-check:** my analytic tensor vs my from-scratch 4D
  centred-FD Einstein tensor at the 6 CTL-T2 pairs (member
  {SNM, a = 0.30, T = 40, D = 0.75, m = 0}, φ ∈ {2.6, 3.5}, radii
  {12.3, 16.2, 19.4} on the stored A2 NEC-argmin direction):
  relative agreement (h = 0.00625) **1.21e-7** (bar 1e-3); absolute on
  small components **0.0** (bar 1e-8); FD self-spread (h vs h/2)
  **1.09e-5** (bar 2e-4). PASS.
- **C-7 Sinusoidal cross-check:** with μ = 1 + a·cos(Ωt):
  (M, a = 0.05, T = 160) worst-instant level mine
  −2.459256513879051e-4 vs stored −2.4592565138790523e-4, diff
  +1.08e-19; SNM a = 0.30 T = 40 L(φ = 0) diff −2.71e-20;
  L(φ = π/2) mine −2.6241785645616557e-4 vs stored
  −2.624178564561655e-4, diff −5.42e-20. All ≤ 2e-6. PASS.
- **C-8 Frame admission:** the laptop pool was **reachable**
  (spark@100.71.86.14, RTGaming WSL, via the proxy script; it had no
  scipy, so a venv `~/g39venv` with numpy 2.5.5 / scipy 1.18.1 was
  created there and the identical `g39_lib.py` + A2 vectors were run).
  The laptop does **NOT** reproduce the anchor at diff 0.0: NEC diff
  −1.055e-6, DEC diff +2.7e-19, WEC diff −8.313e-6, SEC diff
  −5.736e-7, ρ diff +1.2e-19 (max 8.31e-6 — the same pattern as
  344/348/349/364). **Laptop NOT admitted; all deciding reads were
  executed on this VM, the frame of record.**

Benchmark: one instant SET read ≈ 2 s wall on this VM under shared
load; projected scan total (1184 reads) ≈ 40 min. Actual: the scan +
refinement (2144 reads) completed in two runs — a runtime restart
killed the first set of workers after 22/37 scan members and 7/10
refinement audits were checkpointed; the workers resumed from the
per-member checkpoint files with zero re-reads of completed members.

---

## SS2. A-1 SCAN (J = 32; `results/g39_scan.json`)

Member name set verified equal to `p364_scan.json`'s 37 keys before
running. All 37 members × 32 instants read with my machinery.

- **C1 holds:** global min ρ over the scan = **+5.94490273097585e-5**
  at **SNM_a0.30_T40_D0.875_m0.00** (stored: +5.9449e-5 at the same
  member; signed diff −1.5e-19).
- **Floors:** zero floor-infeasible instants in the scan (and zero in
  the refinement; 2144 instant-reads total, matching the stored
  count).
- Every member's summary (L_worst, NEC_worst + phase, DEC_worst +
  phase, L_best, min ρ, floor count) reproduces the stored summary:
  the only nonzero diffs among all 37 × 9 summary fields are 126
  values, every one ≤ 6.5e-19 in magnitude (float64 roundoff in a
  different operation order); all phases, argmin radii and counts are
  identical. Per-instant diffs over all 1184 instants × 6 fields:
  max abs diff 8.85e-17 (on DEC-saturated values of order 1).

## SS3. A-2 REFINEMENT + A-3 CONFIRMATION (`g39_refine.json`, `g39_confirm.json`)

Refinement: the 5 stored audit_list members at J = 64 and J = 128.
Acceptance: |L_worst(128) − L_worst(64)| for the best member
(SNM_a0.30_T160_D0.750_m0.75) = **8.943221597361255e-7** ≤ 1e-6
(stored 8.943221597359087e-7); |L_best(128) − L_best(64)| for the
largest-L_best member (SNM_a0.15_T160_D0.750_m0.75) = **0.0**. PASS —
the full-scan J = 128 consequence is not triggered, as stored.

**The four members at J = 128 (mine; margins vs the stationary bars;
every value's diff vs stored is ≤ 8.1e-20 — see SS5):**

| member | NEC_worst (margin) | φ_NEC | DEC_worst (margin) | φ_DEC |
|---|---|---|---|---|
| SNM_a0.30_T160_D0.750_m0.75 | −2.169048e-4 (**+1.504e-5**) | 2.9943 | −1.854699e-4 (**+3.790e-5**) | π |
| M_a0.30_T160_D0.750_m0.75 | −2.224589e-4 (**+9.486e-6**) | 3.2889 | −1.854699e-4 (**+3.790e-5**) | π |
| SNM_a0.15_T160_D0.750_m0.75 | −2.256428e-4 (**+6.303e-6**) | 2.9943 | −2.032703e-4 (**+2.010e-5**) | π |
| M_a0.15_T160_D0.750_m0.75 | −2.272118e-4 (**+4.734e-6**) | 2.9943 | −2.032703e-4 (**+2.010e-5**) | π |

All four: min ρ over audited instants ≥ +8.7246e-5; zero
floor-infeasible instants at J = 32/64/128. **MEMBER AT THE WORST
INSTANT reproduces** in the registered sense (NEC and DEC jointly
past their bars by > tol = 1e-6 at J = 128, C1 and floors at every
audited instant, C2 below). All levels remain negative — no EC pass,
exactly as Phase 364 stated.

Confirmation polish (8 polishes, at the J = 128 NEC-worst and
DEC-worst instants): polished depths mine vs stored C2_depth agree
to ≤ 1.2e-18 at all 8 (range −1.496774e-4 … −1.935726e-4); **C2
passes at all 8** against the −0.0034 bar. Worst-null: see SS4.

## SS4. THE ONE NON-REPRODUCTION: stored worst-null values

Phase 364's memo states the exact pointwise worst-null at each worst
instant's SET NEC argmin "reproduces the SET NEC min exactly", and
its stored `p364_confirm.json` records
`worst_null_at_set_nec_argmin` equal to the SET NEC min at all 8
instants, while also recording `argmin_typeI = False` at all 8.

That cannot hold for a genuine worst-null, and under the brief's
protocol (fib-642 scan + Nelder–Mead polish of kᵀ·That·k) it does
not: at a non-Type-I point the SET NEC margin is the sampled
162-direction value, an upper bound on the true worst null. My
values (mine − stored): SNM_a0.30 NEC −9.63e-8, DEC −2.82e-9;
M_a0.30 NEC −3.78e-7, DEC −2.82e-9; SNM_a0.15 NEC −3.83e-7,
DEC −4.10e-8; M_a0.15 NEC −4.15e-7, DEC −4.10e-8. Spot-verified at
the best member's NEC-worst instant: SET NEC min
−2.169047936502378e-4; fib-642 scan alone −2.169596634241091e-4
(already below the SET value); NM-polished worst null
−2.1700111452323573e-4; an independent dense random scan of
400,000 directions gives min −2.170007094577368e-4, corroborating
the polished value to 4e-10. So the stored worst-null numbers are
the sampled SET values restated, not pointwise worst-nulls.

**Verdict relevance: none.** NEC_worst/DEC_worst are SET-244 reads
and reproduce; C2 reproduces and passes. Even read pointwise, the
best member's true worst null at its NEC-worst instant
(−2.170011e-4) still beats NEC_stat (−2.319453e-4) by 1.494e-5 >
tol. The MEMBER verdict stands; the worst-null line of the 364
confirmation record should be corrected to the values in
`g39_confirm.json`.

## SS5. A-5 DIFFS TABLE (mine − stored, signed)

- Stationary anchor (C-3): NEC −1.08e-19, DEC +5.42e-20,
  WEC −4.34e-19, SEC +8.67e-19, ρ +1.22e-19, polished depth
  +4.34e-19.
- Scan summaries (37 members × 9 fields): all diffs 0.0 except 126
  roundoff diffs ≤ 6.5e-19. Headline fields: ANCHOR L_worst
  −1.08e-19; global min ρ −1.5e-19; floor-infeasible counts 0
  everywhere (diff 0).
- Refinement summaries (10 audits × 9 fields): all diffs 0.0 except
  41 roundoff diffs ≤ 7.6e-19. The four members' J = 128 deciding
  values: SNM_a0.30 NEC_worst −1.08e-19, DEC_worst +5.42e-20;
  M_a0.30 NEC_worst +2.7e-19 (from −2.2245893410012844e-4),
  DEC_worst +5.4e-20; SNM_a0.15 NEC_worst −8.13e-20,
  DEC_worst 0.0 (DEC_worst −2.0327034045733113e-4 both);
  M_a0.15 NEC_worst 0.0, DEC_worst 0.0. Margins recomputed from my
  values: +1.5040519625061802e-5, +9.48637917517117e-6,
  +6.3025568619104195e-6, +4.733562656283121e-6 (NEC);
  +3.789941475129525e-5 (a = 0.30 DEC), +2.0098979988267046e-5
  (a = 0.15 DEC) — the claimed margins to their stated precision.
- Refinement acceptance |ΔL_worst|: mine 8.943221597361255e-7,
  stored 8.943221597359087e-7, diff +2.2e-19. |ΔL_best| 0.0 both.
- Confirmation: set_nec_min / set_dec_min / set_rho_min diffs at the
  8 instants ≤ 6.6e-19; C2 polished-depth diffs ≤ 1.2e-18;
  **worst-null diffs −2.82e-9 … −4.15e-7 (SS4 — the only
  non-roundoff diffs in the gate).**
- Phase 349 cross-checks (C-7): +1.08e-19, −2.71e-20, −5.42e-20.
- Bottom-point targets (A-4 iv): my DEC minima at constant
  μ = 1.15 / 1.075 are −1.8546990569430293e-4 (SNM) /
  −1.8546990569430304e-4 (M) and −2.0327034045733113e-4 (SNM) /
  −2.0327034045733103e-4 (M), vs the full-precision stored
  winners' DEC_worst −1.8546990569430298e-4 / −2.0327034045733113e-4:
  diffs ≤ 1e-19. (Against the brief's rounded targets
  −1.854699e-4 / −2.032703e-4 the diffs are −5.69e-12 / −4.05e-11,
  i.e. the targets' own rounding.)

## SS6. A-4 ANATOMY

- (i) **Arm 1 (m = 0, 24 members):** every member's L_worst is
  carried by DEC (L_worst = DEC_worst) and every DEC_worst is
  saturated (≤ −0.99; values −1.000001 … −1.000214). Full table in
  `g39_confirm.json` (`anatomy.arm1_m0_table`). Matches the claim.
- (ii) **Winners' DEC-worst phase at J = 128: φ = π for all four**
  (the quasi-stationary bottom). Matches.
- (iii) **T = 40, m = 0.75 members (J = 32):** L_worst vs L_stat
  shortfalls: M_a0.30 −3.875e-4 (L_worst −6.194893e-4),
  SNM_a0.30 −2.646e-4 (−4.965538e-4), M_a0.15 −1.924e-4
  (−4.243595e-4), SNM_a0.15 −1.678e-4 (−3.997740e-4). The brief's
  "fail by 2–4e-4" is the right scale; the exact range is
  1.68e-4 … 3.88e-4 (the SNM_a0.15 member falls just below 2e-4).
- (iv) **Bottom-point check:** the winners' DEC-worst equals the
  stationary DEC minimum of the centre scaled by the constant
  bottom μ (1.15 for a = 0.30, 1.075 for a = 0.15), for both the SNM
  and M subsets, to ≤ 1e-19 (SS5). The claim holds exactly.

## SS7. PROCESS / DEVIATIONS

- All calibrations C-1…C-7 passed before any audit read; C-8
  recorded (laptop not admitted; VM is the frame of record and ran
  every deciding read).
- One runtime restart interrupted the audit workers; per-member
  checkpoints (in `g39_scan_part*.json` / `g39_refine_part*.json`,
  retained) made the resume exact with no completed member re-read.
- Deviations from the brief, on the face: (1) the M-ramp r2
  arbitration came out for the registration's r2 = 20.0 (SS1/C-3) —
  as the brief instructed to report; (2) the brief's T = 40 anatomy
  range "2–4e-4" is 1.68–3.88e-4 exactly (SS6 iii); (3) the stored
  worst-null confirmation numbers do not reproduce (SS4) — this is
  a finding about Phase 364's record, not a deviation in my
  protocol, which followed the brief's worst-null specification.
- No GATE39.md written, no ledger append, no external contact.
  Writes are inside `gate39/` only (plus a venv and the anchor-run
  copy under `~/g39/` on the laptop for C-8, and /tmp scratch).

**Bottom line for the gate:** Phase 364's MEMBER AT THE WORST
INSTANT claim — four dwelling members beating L_stat on NEC and DEC
jointly at J = 128, best SNM_a0.30_T160_D0.750_m0.75 at
NEC_worst −2.169048e-4 / DEC_worst −1.854699e-4, with C1, floors
and C2 — is **confirmed by fully independent machinery at roundoff
precision**, with the single correction that its stored worst-null
confirmation values are sampled SET values restated, the true
pointwise worst-nulls lying 2.8e-9 … 4.2e-7 below them (immaterial
to the verdict, as shown in SS4).
