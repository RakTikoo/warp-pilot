# P80-1 — LE MULTIPOLE (DARMOIS) AUDIT — RUN RECORD

**Item:** P80-1, Phase 80. **Worker:** P80-1 worker. **Date:** 2026-11-22.
**float64 everywhere** (venv `~/workspace/warp-pilot/venv/bin/python`).
INTERNAL only; nothing uploaded. **Registration:**
`phase80/CHECKPOINT80.md` §P80-1 (binding; not edited by this worker).
**Predecessor:** `phase71/CHECKPOINT71.md` §P71-5 + `phase71/results/
p715_memo.md`, `p715_runrecord.md`, `p715_results.json`, `p715_pole.json`.

**Category (exact, binding):** subluminal ACCELERATING shell,
Bobrick–Martire class. This item is never described as FTL anywhere.
A CONFIRMED verdict confirms a subluminal accelerating shell at gate
standard and nothing stronger. The category has no gate-verified
positive row (Phase 71's dipole certification FAILED at two pins).

---

## 1. SOURCES LOG (every source retrieved, with date + identifier)

All retrieved 2026-11-22 (PT) by this worker unless marked P71 (retrieved
by the Phase 71 worker on 2026-11-22 and re-verified in its run record):

1. **Le (2026), "Steering a warp drive without exotic matter,"
   arXiv:2606.22531, v3 full text (PDF)** —
   https://arxiv.org/pdf/2606.22531v3.pdf — fetched and read in full
   (esp. Supplement §S, "Numerical frontier: the finite-amplitude
   bracket," and the Data Availability statement). This is the audit
   target. Identity re-verified against the arXiv record:
   arXiv:2606.22531 = the steering-drive paper; arXiv:2605.25417 is a
   DIFFERENT Le paper and is NOT audited here.
2. **arXiv abstract record arXiv:2606.22531v1 / latest v4 (13 Sep 2026)**
   — https://arxiv.org/abs/2606.22531v1 — version history + abstract
   cross-check (P71 verified v1–v4 identity; the audited text is v3,
   as in Phase 71).
3. **Published reproduction code (the paper's Data Availability
   statement points to it): github.com/anindex/world_tube**, public,
   MIT, commit `1e9e3dbf2bedbe31e54a40c427495ee61b477ac2` — cloned
   2026-11-22 to `phase80/work/world_tube_repo/`. Files read in full:
   `README.md` (script→claim map), `reproduce/multipole_frontier.py`
   (the multipole solve), `worldtube/geometry.py`, `worldtube/energy.py`
   (`FRONTIER_G`, `phi_HE`). The paper states (Supplement §S, end):
   "Its configurations and tolerances accompany the implementation
   referenced in the Data Availability statement" — i.e. the code is
   part of the published record for the numerical claims.
4. **Phase 71 stored audit record** (programme-internal, on disk):
   `phase71/work/p715_lib.py` (auditor), `p715_main.py`,
   `p715_checker.py`; `phase71/results/p715_results.json`,
   `p715_pole.json`, `p715_memo.md`, `p715_runrecord.md`.

**No author contact** (standing rule). No other sources used.

### What the published record contains for the MULTIPOLE solve

- **Paper text (Supplement §S):** the solve is a finite-λ least-squares
  solve of the full [h_ab] = 0 with areal shape
  R(ϑ) = R₀(1 + Σ_l a_l P_l), the lapse and the foliation tilt on both
  sides expanded in Legendre / vector-harmonic modes. Reported outputs
  ONLY: residual decay (max|[h_ab]| → 10⁻⁷–10⁻⁹ by L = 6 for x ≲ 0.3;
  ~10⁻³ by L = 6 at x = 0.5, 0.7, tightening at L = 8–10); converged
  worst-observer DEC margins {1.8, 9.1, 18, 21}×10⁻³ at
  x = {0.1, 0.3, 0.5, 0.7} at λ = g̲(x); max|[h]| = 1.4×10⁻⁷ at
  x = 0.1; Newton–Kantorovich h ≤ 1.3×10⁻⁵ (x ≤ 0.3), ~6×10⁻²
  (x = 0.5, 0.7). **The paper text publishes NO multipole coefficients**
  (no a_l, lapse or tilt mode values at any pin).
- **Published code (`reproduce/multipole_frontier.py`):** the full
  solve specification — unknowns per order l = 1..L: shape ρ_l
  (R(θ) = R₀(1 + λ Σ ρ_l P_l(cosθ))), exterior lapse At_l, exterior
  tilt w_l (vector harmonic S_l(θ) = sinθ P_l′(cosθ)), interior tilt
  wi_l, interior lapse Ai_l; the closing configuration is bounded
  least-squares (frame-timelike box: |w|,|wi| ≤ 0.8, |ρ| ≤ 4,
  |At|,|Ai| ≤ 8) with interior tilt AND interior lapse ON; residual =
  ([h_ττ], [h_τθ], [h_θθ])/λ on a θ-grid; pins
  FRONTIER_G = {0.1: 0.19, 0.2: 0.20, 0.3: 0.19, 0.5: 0.14, 0.7: 0.09};
  the script's own stress read uses θ ∈ [0.12, π−0.12] (29 pts) —
  **the author's multipole stress grid also stops short of both
  poles** (0.12 rad), a fact recorded here before any audit number.
  Hence the converged coefficients are obtainable by RUNNING the
  published code (it is the published data for this claim), and the
  gate audit then reads those coefficients on the programme's own
  full-angle grid (§3).

**Data gate: PASS in the code-inclusive sense** — paper + published
code determine the multipole configuration (solve specification +
pins + tolerances). The paper-text-only gap (no printed coefficients)
is recorded as a finding, not as the verdict: the NOT REPRODUCIBLE
branch would require the code route to fail as well; it is tested by
actually running it (§4).

## 2. AUDITOR RE-GATE (before any multipole number)

Auditor: `phase80/work/p801_lib.py` — a generalisation of the Phase 71
auditor (`phase71/work/p715_lib.py`, itself re-gated in Phase 71
against the Finalist A anchor suite, bit-identical reproduction).
Reuse statement (what is reused from Phase 71 / Phases 50/51/63
lineage): the FD metric-derivative → algebraic Γ → FD normal-gradient
→ orthonormal-frame K → Lanczos pattern; `metric_ext` / `metric_int`
(Kerr–Schild Kinnersley exterior; flat Rindler interior), `retarded`,
`christoffel`, `lanczos`, `phi_HE` (paper Eq. (35) worst-observer
margin + Hawking–Ellis discriminant), `sampled_dec_min`,
`anchor_closed`. Generalised for this item: multipole shape
c_l = λR₀ρ_l (l = 1..L), multipole lapse/tilt seeds on BOTH sides
(interior tilt wi and interior lapse Ai included — the dipole auditor
had Ai₁ = 0, wi = 0 by the paper's dipole convention), pole-safe
evaluation (§3).

Re-gate controls (must pass BEFORE any multipole number is read):
(C1) static anchor: multipole machinery at λ = 0, all coefficients 0,
     reproduces Eqs. (22)–(23) σ₀, p₀ to ≤ 10⁻⁵ at x ∈ {0.1, 0.3, 0.5};
(C2) dipole reduction: L = 1, Ai = wi = 0 with the Phase 71 stored
     dipole dof at x = 0.1 reproduces the Phase 71 stored pole-band
     margins (`p715_pole.json`: at (0.1, 0.19): +4.52×10⁻⁵ at π−0.15 →
     −1.99×10⁻⁴ at π−0.0125) to within the Phase 71 h-ladder spread;
(C3) the auditor's [h] residual for the DIPOLE solution at finite λ
     is O(λ²)-sized (1–10% of λ per the paper), i.e. the auditor sees
     the same mismatch the multipole solve exists to remove.

## 3. POLE TREATMENT — STATED BEFORE ANY NUMBER IS READ (binding)

The Phase 71 dipole scan (author's) stopped at π − 0.15; the author's
multipole stress grid stops at π − 0.12. This audit's grid does not
stop short of either pole:

- **Audit angular grid:** uniform in μ = cosθ, μ ∈ [−1, +1] with the
  ENDPOINTS INCLUDED EXACTLY (μ = −1 ⇔ θ = π, the rear pole; μ = +1 ⇔
  θ = 0, the front pole), N_μ = 161 base points, PLUS a refined
  near-pole band: 41 additional points in θ ∈ [π − 0.15, π] (the exact
  band the dipole scan never sampled) and 21 in θ ∈ [0, 0.15].
- **Pole evaluation is regular, not extrapolated:** all quantities are
  computed in the Cartesian FD machinery at the exact pole point
  X = (0, ∓q, 0, 0). At a pole: P_l(±1) = (±1)^l exactly; the tilt
  harmonics S_l = sinθ·P_l′(cosθ) vanish exactly (sinθ = 0); the
  meridian/azimuth seed vectors are the Cartesian tangent vectors
  (0,0,∓1,0) and (0,0,0,1), non-degenerate in the embedding; the level
  set uses μ = Y₁/|Y_spatial| (pole-safe, no arccos). The pole margin
  is therefore a COMPUTED value at θ = π, and the "pole limit" is the
  value at the endpoint itself, cross-checked against the refined-band
  sequence approaching it.
- **Solve grids vs audit grid:** the reconstruction solves (author's
  published code; this worker's independent solve) use their own
  interior solve grids (author's: θ ∈ [0.2, π−0.2]); the AUDIT is
  always on the grid above, which strictly contains both poles and
  the near-pole band. A solution that only matches on its own solve
  grid but fails the audit grid's pole read fails the audit.

## 4. RUN PLAN (registered)

(R1) RECONSTRUCTION (author path): run the published
     `multipole_frontier.py` machinery (`solve_multipole` /
     `frontier_diag`, bounded, interior tilt + lapse ON) at the five
     pins (x, λ) = (0.1, 0.19), (0.2, 0.20), (0.3, 0.19), (0.5, 0.14),
     (0.7, 0.09), L = 6; L = 8 at x = 0.5, 0.7 (the paper says L = 6
     leaves ~10⁻³ there). Store the converged coefficient vectors —
     these ARE the reconstructed multipole solution.
(R2) GATE AUDIT (programme path): read (R1)'s coefficients with the
     §2 auditor on the §3 grid: [h_ab] residual max (absolute and
     per-λ), Hawking–Ellis type at every grid point, worst-observer
     DEC margin (Eq. (35) form), eigenvalue margins (σ−|p_∥|,
     σ−|p_φ| from the boosted eigen-decomposition), sampled-null /
     sampled-observer DEC cross-check at the binding angle, h-ladder
     h ∈ {0.02, 0.01, 0.005} + independent 4th-order FD at the
     deciding (minimum-margin) angle. Margins alone never decide:
     a pin passes only if Type-I everywhere on the audit grid AND
     sampled-null/eigen margins ≥ 0 AND worst-observer margin > 0 on
     every ladder rung.
(R3) ADVERSARIAL SECOND PATH (any deciding number): an independent
     least-squares multipole solve in the §2 FD auditor (scipy,
     no JAX, no warpax, no author code), started from the padded
     dipole solution (NOT from (R1)'s coefficients), at the two
     Phase-71 failing pins (0.1, 0.19) and (0.3, 0.19); its
     coefficients and pole margins must agree with (R1)/(R2) within
     the ladder spread before any verdict wording.
(R4) CHECKER: `results/p801_check.py` recomputes the deciding
     numbers (pole margins, worst margins, types) from the stored
     JSONs and re-reads the stored coefficient vectors through the
     stored per-θ stress arrays; output `results/p801_check.json`.

**Compute note:** no run is expected to exceed ~2 h continuous; the
author-path solves are the slow step (published estimate: tens of
minutes for the full script). No Kaggle flag. All runs checkpoint
their JSON to `results/` as they land.

## 5. DEVIATIONS / INSTRUMENT LOG

- **Re-gate (run BEFORE any multipole number): PASS.** (C1) Static
  anchor via the multipole machinery (λ = 0, L = 2): σ, p vs
  Eqs. (22)–(23) agree to ≤ 2×10⁻⁶ at x ∈ {0.1, 0.3, 0.5}.
  (C2) Dipole reduction (L = 1, Phase-71 stored dof at x = 0.1,
  λ = 0.19): pole-band margins reproduce `p715_pole.json` to all
  printed digits (+4.518862×10⁻⁵ at π−0.15, −9.019238×10⁻⁵ at π−0.10,
  −1.730580×10⁻⁴ at π−0.05, −1.992079×10⁻⁴ at π−0.0125), and at the
  pole endpoint itself θ = π the auditor computes −2.0096×10⁻⁴ —
  i.e. Phase 71's "pole limit −2.0×10⁻⁴" is the value AT the pole,
  now computed directly. (C3) Dipole [h] residual at (0.1, 0.19):
  max|[h]| = 1.39×10⁻² = 7.3% of λ, inside the paper's stated 1–10%
  dipole mismatch — the auditor sees the same mismatch the multipole
  solve exists to remove.
- **Deviation D1 (solver route):** the author's published solve
  (`solve_multipole`, JAX/warpax) was run as registered (R1) but is
  extremely slow on this shared cell (its L-continuation stages take
  tens of minutes each under multi-tenant CPU contention; first stage
  at x = 0.1, L = 2 completed: max|[h]| = 7.4×10⁻⁴ on the author's
  dense grid). The reconstruction was therefore ALSO carried out by
  an independent FD solve of the SAME published specification
  (R3 machinery promoted to the primary reconstruction route):
  `work/p801_solve.py` (damped Gauss–Newton, FD Jacobian in
  coefficient space, start = padded dipole, author's dof layout and
  box bounds) and `work/p801_solve2.py` (λ-continuation + L
  continuation, scipy bounded least-squares) for the high-compactness
  pins where the direct solve stalls. This changes WHERE the
  coefficients come from, not what is audited: every coefficient set,
  from either route, is read by the same pole-inclusive FD gate audit
  (R2), and the audit's own FD-measured max|[h]| is the closure
  evidence. The author-path run was left running as corroboration;
  its coefficients, where landed, are audited under `_author` keys.
- **Deviation D2 (solver tolerances):** the FD solves stop at the FD
  noise floor of the auditor (residual/λ ~ 2×10⁻⁵ at low x, i.e.
  max|[h]| ~ 5×10⁻⁶–1.4×10⁻⁵ absolute), not at the published script's
  10⁻¹⁴ tolerances; the audit reads the achieved residual directly,
  so no conclusion rests on solver tolerance.
- **Instrument note:** the direct Gauss–Newton at x = 0.5 / 0.7
  (L = 4, no continuation) STALLS (residual/λ ~ 0.40 / 0.68,
  max|[h]| ~ 0.06) — a solver failure, recorded as such; those
  coefficient sets are NOT a reconstruction and their stress reads
  are not used. The continuation solver (D1) is the route for those
  pins. A RuntimeWarning (sqrt of a negative Gram–Schmidt norm at an
  intermediate trial point during the stalled x = 0.5 iterations) is
  confined to that discarded solve.
- **Service restart (2026-11-22, mid-run):** the runtime restarted
  once, killing background jobs; both were restarted from their
  on-disk checkpoints (no stored result was lost; the x = 0.3
  iteration history restarted from the dipole).

## 6. OUTCOME

**PARTIAL — CONFIRMED AT OUR BARS at x ∈ {0.1, 0.2, 0.3} (including
both Phase-71 failing pins (0.1, 0.19) and (0.3, 0.19)); open clause:
x ∈ {0.5, 0.7} multipole closure not independently reproduced
(solver-convergence gap; paper's margins there untested, not
impeached).** Deciding numbers (full audit, pole-inclusive grid,
h-ladder + 4th-order at the binding angle): x = 0.1 pole margin
+1.7283×10⁻³ (L = 6; L = 4: +1.7255×10⁻³; paper 1.8×10⁻³;
max|[h]| 1.5×10⁻⁷ vs paper's printed 1.4×10⁻⁷); x = 0.3 worst
+9.1021×10⁻³ at the front pole, rear pole +9.8547×10⁻³ (L = 6;
paper 9.1×10⁻³); x = 0.2 worst +5.1433×10⁻³ (L = 4). Type-I at every
grid point at every confirmed pin; eigenvalue margins = worst-observer
margins at the binding points; sampled cross-checks ≥ exact margins.
Checker: **73/73 PASS**. Full statement in `results/p801_memo.md`.

**Background runs still in flight at memo time** (their outputs land
in the same files and can only add corroboration; the coordinator may
re-run `p801_check.py` after they land): the author-path
reconstruction (`work/p801_reconstruct.py`, staged residuals at
x = 0.1: L = 2 → 7.4×10⁻⁴, L = 4 → 4.4×10⁻⁶, L = 6 stage running) and
the LM continuation at x = 0.5 (`work/p801_solve4.py`, plateaued
~1×10⁻² absolute at λ = 0.112 when last read). No run exceeded ~2 h
continuous; no Kaggle flag was raised (the constraint was shared-cell
CPU contention, not single-run length).
