# P71-5 — LE STEERING-DRIVE GATE AUDIT — RUN RECORD

**Item:** P71-5 (fringe registration R3), Phase 71. **Worker:** P71-5 worker.
**Date:** 2026-11-22. **float64 everywhere.** INTERNAL only; nothing uploaded.
**Registration:** `phase71/CHECKPOINT71.md` §P71-5 (binding; not edited).
**Fringe source:** `fringe_sweep_2026-11-22.md` §U3 / R3.

---

## 1. PAPER IDENTITY — verified FIRST, before any number

Verified against the live arXiv records on 2026-11-22 (arXiv abstract pages
fetched and read in full):

- **arXiv:2606.22531** = An T. Le, **"Steering a warp drive without exotic
  matter"** (gr-qc; v1 submitted 21 Jun 2026; latest v4, 13 Sep 2026).
  Abstract confirms the registered content verbatim in substance: prescribed
  passenger worldtube, exact Kinnersley photon-rocket exterior, matching
  timelike shell, steering law −ṁ ≥ 3m|a| paid in Bondi mass, shell surface
  DEC for 2m/R < 24/25, Buchdahl-type frontier a_max·R bracketed between a
  numerical lower bound ~0.2 and the closed-form ceiling ½(1 − 2m/R).
  **This is the audit target.**
- **arXiv:2605.25417** = An T. Le, **"On the boundary cost of
  source-consistent warp shells"** (gr-qc; v1 25 May 2026; v3 17 Sep 2026) —
  a DIFFERENT paper (Fuchs-shell source-consistency critique; Type-IV tail
  violations; 600-configuration source-first scan). It matches the stored
  programme record (`gate6/results/wA_g6_1.md`, `gate6/GATE6.md`) and its
  citation in v1.9.0. It is context only (its stricter source-consistency
  standard is noted in the memo), **not** the audit target.

The Phase-71 tasking text's citation of 2605.25417 for this item is the
mis-citation the checkpoint's registered correction identifies; the audit
proceeds on 2606.22531 as R3 specifies. Paper version audited: **v3 full
text** (25 pp. + appendices + in-paper Supplement §S), cross-checked against
the v1 abstract record; the published reproduction code (Data Availability:
github.com/anindex/world_tube, public, MIT, commit 1e9e3db) was read as
published supplementary material for the data gate (its `worldtube/geometry.py`,
`worldtube/energy.py` definitions), but **no author code was run or imported**
by the auditor — the audit is an independent reimplementation.

## 2. AUDITOR RE-GATE — before any Le number

Control row (programme gate auditor, Phases 50/51/63 pattern — gate6
`wa_auditor.py` / `wa_run.py` anchors, the Phase-50/51 auditor lineage):

- **Control row named:** Finalist A positivity anchor — M = 2.0, (10,20),
  β = 0.02, full fine-style point set, h = 0.3 — plus the Minkowski and
  static-spherical exact anchors of the same anchor suite.
- **Stored verdict** (`phase50/results/p501_audit.json`, same auditor):
  Minkowski max |G| = 0.0; static-anchor max ρ rel. err (h = 0.3) =
  0.0030717699532123565; max principal-pressure abs. err = 9.215029876625953e-08;
  Finalist A whole-volume worst margin (SEC) = **+2.141179301461828e-07**
  (positive), Type-I fraction 1.000 — stored verdict: **PASS / positive anchor**.
- **Reproduction (this run, 2026-11-22, gate6 `wa_run.anchors()` re-run):**
  `ANCHORS DONE mink 0.0 maxrhoerr 0.0030717699532123565 maxperr
  9.215029876625953e-08 A worst 2.141179301461828e-07` — **all four stored
  values reproduced exactly** (bit-identical at float64 print precision).
  Re-gate: **PASS**. Only after this were Le numbers computed.

The P71-5 auditor itself (`work/p715_lib.py`) is a fresh implementation in
the same pattern (FD metric derivatives → algebraic Γ → FD normal gradient →
orthonormal-frame K → Lanczos → Hawking–Ellis Type-I classification +
Eq.-(35) margins + sampled-observer NEC/DEC cross-check + h-ladder), and it
was validated on the paper's static anchor before the frontier scan:
FD junction σ₀, p₀ vs the paper's closed-form Eqs. (22)–(23) agree to
~2×10⁻⁷ (σ) at h = 0.01, and the independently solved Darmois tilt matches
the paper's closed form w₁ = x/(2√(1−x)) to 3×10⁻⁷ at x = 0.3 (see results).

## 3. TIMELIKE-SHELL ADAPTATION — registered BEFORE computing the audit

Registered here (and fixed in `work/p715_lib.py`'s header before the frontier
run) as the §P71-5-required adaptation of the volume gate auditor to a
matching (timelike, distributional) shell:

1. **Object audited:** the surface stress-energy S_ab of the timelike shell Σ
   (not a volume T_ab), obtained by the Lanczos equation
   S^a_b = −(1/8π)([K^a_b] − δ^a_b [K]) from the extrinsic-curvature jump
   across Σ between the two published metrics (Kinnersley–Kerr–Schild
   exterior; flat Rindler interior), in a shared geometric orthonormal
   frame (timelike seed At·∂_t + w·meridian, meridian, azimuth; projected
   ⊥ n, Gram–Schmidt per side).
2. **Junction re-derivation BEFORE the DEC read:** the first junction
   condition [h_ab] = 0 is solved independently at O(λ) for the shell/frame
   dipoles (ρ₁, At₁, w₁) (interior lapse dipole Ai₁ = 0, the paper's
   convention), as a 3×3 linear system on the (const, cos) parts of
   [h_ττ] and the sin part of [h_τθ]; the solution is checked against the
   paper's closed-form tilt w₁(x) = x/(2√(1−x)) (App. C) and the static
   limit against Eqs. (22)–(23) BEFORE any accelerating DEC number is read.
   Agreement/discrepancy recorded in the results file.
3. **DEC read:** on S_ab across the claimed range 2m/R < 24/25 (static
   anchor, closed form + FD junction) and at the **registered frontier
   points**: the paper Supplement's (S1) dipole-scan pins
   (x, g̲(x)) = (0.1, 0.19), (0.2, 0.20), (0.3, 0.19), (0.5, 0.14),
   (0.7, 0.09), with the bracket's other endpoint the closed-form ceiling
   ½(1−x) (Prop. 5). At each pin: Hawking–Ellis type of the (τ̂,θ̂) block
   (discriminant Δ_s = (σ+p_θ̂)² − 4q²; Δ_s < 0 ⇒ Type IV), worst-observer
   DEC margin in the paper's Eq. (35) form, sampled-observer DEC
   cross-check at the binding angle, θ-grid over [0.05, π−0.05] (25 pts,
   binding angle tracked), **h-ladder** h ∈ {0.02, 0.01, 0.005} (2nd-order
   FD) plus an independent **4th-order FD discretisation** at h = 0.01
   (adversarial second path within the auditor; the auditor as a whole is
   the independent second path against the author's warpax/JAX pipeline).
   Margins alone never decide: a pin passes only if Type-I AND margin > 0
   on every ladder rung AND the sampled check is non-negative.
4. **Frontier reproduction:** the first margin zero λ*(x) is located by
   scan (Δλ = 0.02) + bisection (24 iterations) on the same auditor; the
   bracket is reproduced iff pin ≤ λ*(x) ≤ ½(1−x) (scan tolerance 0.021
   on the lower side) at every x.
5. **Volume read (where a volume representation exists):** (a) the paper's
   Kerr–Schild radial-tension thickening, Eq. (50) — fully published closed
   form — DEC read across the wall on a δ-ladder (the paper claims it
   FAILS; the audit checks the failure and its 1/δ² edge law, Cor. 7);
   (b) the tangential-pressure wall's Type-I discriminant (54),
   Δ = ρ(ρ+4μ), and its margin factor 1 − m/(2(r−2m)), whose positivity
   window is the published 2m(r)/r < 4/5. The full numerical thick-wall
   profile itself is constructed only inside the author's code (constraint
   solve), not published as data in the paper; that is recorded as a scope
   note, not the deciding gap — the deciding object (the thin shell) IS
   determined (see §4).
6. **Scope limits registered:** the audit covers the paper's **dipole-scan**
   frontier (the published pins (S1)) and the static anchor and frozen-shape
   axial threshold λ_DEC (Eq. 42) — the objects the paper publishes as
   numbers. The author's separate nonlinear multipole solve (residuals
   ~10⁻³ at x = 0.5, 0.7) reports margins at the same pins that are ≥ the
   dipole-scan margins by construction of its relaxation argument; auditing
   it independently would require re-running a nonlinear Darmois solve at
   the paper's stated tolerances, which is registered here as a follow-up,
   not silently included. The finite-duration burn (Thm. 3) is audited only
   through its per-cut shell (the same pins/anchor machinery); its
   time-assembly is a theorem of the paper, not a DEC number.

## 4. DATA GATE — extraction from the published paper (+ published supplement)

Extracted (v3 full text + in-paper Supplement §S + published code cited in
the paper's Data Availability statement):

- **Interior / passenger worldtube:** exactly flat cavity M⁻ (Minkowski;
  under acceleration the born-rigid Rindler frame, lapse N = 1 + a·x),
  central worldline Γ with prescribed covariant proper acceleration a;
  cavity vacuum (T⁻ = 0). ✔ determined.
- **Exterior:** exact Kinnersley–Robinson–Trautman photon rocket,
  Eqs. (4)–(6): retarded coordinates, Bondi mass m(u), conformal factor
  P(u, ζ, ζ̄) = A + Bζ + B̄ζ̄ + Cζζ̄ with AC − B B̄ = 1 (unit-curvature
  sphere); stress-energy pure outgoing null dust, Eq. (7), amplitude
  4πn² = −ṁ + 3m(ln P),u, Eq. (8); axisymmetric dipole form
  4πn²(ϑ) = −ṁ − 3ma cos ϑ, Eq. (13). Kerr–Schild form used by the
  published code: g = η + (2M/r_a) l l on the hyperbolic worldline. ✔
  determined.
- **Shell:** timelike Σ: r = R(u, Ω); first junction [h_ab] = 0 fixes the
  shape; Lanczos Eq. (10) returns S_ab; flux-source balance laws
  Eqs. (27)–(28). Static anchor in closed form: σ₀, p₀ Eqs. (22)–(23),
  DEC margin Eq. (24) with factor (5s−1)(s−1), s = √(1−x), hence the
  window x = 2m/R < 24/25, Eq. (25). Accelerating shell: dipole response
  (σ₁, p₁, q₁) from the linearised Darmois system (App. C/D; tilt closed
  form w₁ = x/(2s)); finite-λ Lanczos stress evaluated numerically
  (Supplement). ✔ determined **as a construction** (metric pair + junction
  prescription + dipole solve), which is what a gate audit re-runs.
- **Claimed DEC range:** surface DEC strict for **2m/R < 24/25** at the
  static anchor (Lemma 3); accelerating admissible shells exist for small
  λ = aR, μ (Thm. 2, openness at the anchor — no explicit radius published,
  and none claimed as a number).
- **Frontier bracket:** g(x) (largest admissible λ = a_max·R) satisfies
  c(x) ≤ g(x) ≤ ½(1−x) rigorously (Lemma 6 / Prop. 5), with the numerical
  lower-bound pins **g̲(x) ≃ {0.19, 0.20, 0.19, 0.14, 0.09}** at
  x = {0.1, 0.2, 0.3, 0.5, 0.7} (Supplement (S1), ~5% scan resolution),
  converged-multipole margins at those pins {1.8, 9.1, 18, 21}×10⁻³ at
  x = {0.1, 0.3, 0.5, 0.7}; heuristic envelope (24/25 − x)/2 (Eq. 39,
  explicitly non-rigorous); frozen-shape axial threshold λ_DEC(x) exact
  from Eq. (42), estimate Eq. (43), ratio to ceiling 0.9931 at x ≈ 0.63.
- **Steering law:** −ṁ ≥ 3m|a| (Eq. 14), Tsiolkovsky form Eq. (15).

**Data-gate verdict: PASS.** The published data (paper + in-paper
supplement + the published code the paper's Data Availability statement
points to, read for definitions) determines the configuration: metric pair,
junction prescription, dipole solve, anchor, pins, ceiling. The
NOT REPRODUCIBLE branch is therefore not taken. Two published-data limits
are recorded, neither of which blocks the registered audit: (a) Thm. 2's
existence neighbourhood (ε_a, ε_ṁ) is proved open but not numerically
sized in the paper — the audit therefore tests the paper's *published
numbers* (anchor window, pins, bracket, λ_DEC), not the un-sized
neighbourhood; (b) the multipole-solve's per-pin margins are quoted to
2 significant figures with residuals ~10⁻³ at high x (see §3.6 scope).

## 5. RUN LOG

- Re-gate (§2): PASS, exact reproduction. [2026-11-22]
- Auditor validation: anchor FD vs Eqs. (22)–(23); w₁ vs closed form. PASS.
- Main run: `work/p715_main.py` → `results/p715_results.json`
  (anchor grid + FD ladder; λ_DEC roots; bulk law sampling; Darmois solves
  at x ∈ {0.1, 0.2, 0.3, 0.5, 0.7}; frontier scans + bisection; pin
  h-ladders + 4th-order + sampled cross-checks; volume reads).
- Checker: `work/p715_checker.py` → `results/p715_checker.json`:
  **48/56 passed**; the 8 failures are the pin-DEC rungs at
  (0.1, 0.19) and (0.3, 0.19) — the verdict's deciding failures.
- Numbers: see `results/p715_results.json`, `results/p715_pole.json`
  (near-pole refinement at the deciding pins), and the memo.

## 6. INSTRUMENT-ERROR LOG (Failure Protocol, auditor side)

- **Run 1 (discarded in full):** a first background launch was killed
  with its process group before writing results (no numbers read).
- **Run 2 (discarded in full):** returned wrong-signed anchor σ.
  Anatomy: an index error in the vectorised Christoffel in
  `p715_lib.py` (transpose axes (2,0,1) used for the −∂_s g_{μν} term;
  correct axes (1,2,0)), introduced in a speed optimisation after the
  loop-form auditor had passed its smoke test (anchor σ to 2×10⁻⁷,
  w₁ to 3×10⁻⁷). Caught by the anchor control; localised by direct
  loop-vs-vectorised Γ comparison (max diff 0.166 → 3×10⁻¹⁷ post-fix).
  Every number in the memo is from the post-fix run, whose controls
  (anchor FD vs closed form ≤5×10⁻⁷; Γ vs loop reference 3×10⁻¹⁷;
  w₁ vs closed form ≤1.6×10⁻⁶) all pass.
- **Checker defect (fixed, documented):** the 1/δ² scaling check
  initially expected successive-margin ratio ~4; the correct ratio for
  δ-halving under a 1/δ² law is 0.25 (margins: −0.895, −3.581, −14.32).
  Checker fixed; no result was affected.
- Isolated RuntimeWarnings (sqrt of negative FD-stencil values at
  off-shell stencil points during Darmois probes) did not enter any
  deciding read: all deciding margins are smooth across the h-ladder
  and the 4th-order discretisation.

## 7. OUTCOME

Data gate: **PASS** (configuration determined; §4). Verdict:
**FAILS AT NAMED POINTS** — (0.1, 0.19) and (0.3, 0.19), deciding term
the rear-pole worst-observer surface DEC margin (pole limits
−2.0×10⁻⁴, −1.2×10⁻⁴), Type-I throughout; bracket, anchor window,
junction, bulk law and ceiling all reproduced. Full statement in
`results/p715_memo.md`.
