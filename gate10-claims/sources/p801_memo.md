# P80-1 — THE LE MULTIPOLE AUDIT — MEMO

**Item:** P80-1, Phase 80. **Date:** 2026-11-22. **Worker:** P80-1 worker.
**Audit target:** An T. Le, "Steering a warp drive without exotic matter,"
**arXiv:2606.22531** (v3 full text + in-paper Supplement §S + published
reproduction code, github.com/anindex/world_tube @ 1e9e3db — identity
verified in Phase 71; arXiv:2605.25417 is a different Le paper, not
audited). **Category (exact):** subluminal ACCELERATING shell,
Bobrick–Martire class. Nothing in this memo is an FTL claim, in any
wording. **Auditor:** programme gate pattern (Phases 50/51/63/71),
generalised to multipoles (`work/p801_lib.py`): FD metric derivatives →
algebraic Γ → FD normal gradient → orthonormal-frame K → Lanczos →
Hawking–Ellis Type-I + Eq.-(35) worst-observer DEC margins + eigenvalue
margins + sampled-observer cross-check + h-ladder. float64. INTERNAL
only; nothing uploaded; no author contact.

## VERDICT (registered form)

**PARTIAL — CONFIRMED AT OUR BARS at the multipole operating points
x ∈ {0.1, 0.2, 0.3}, including BOTH Phase-71 failing pins; the open
clause is the high-compactness pair x ∈ {0.5, 0.7}, whose multipole
closure this run did not independently reproduce (solver-convergence
gap, §5 — the paper's margins there are untested, not impeached).**

**The milestone inside this verdict, stated prominently:** Phase 71
failed Le's dipole-scan pins (0.1, 0.19) and (0.3, 0.19) at the rear
pole (pole limits −2.0×10⁻⁴ / −1.2×10⁻⁴) and explicitly did NOT
impeach the paper's separate multipole (Darmois) solve (FU-P715-1).
That question is now answered at those exact pins: **the multipole
shell passes the full gate audit with the near-pole band included —
worst-observer DEC margins +1.73×10⁻³ at (0.1, 0.19) and +9.10×10⁻³
at (0.3, 0.19), Type-I everywhere on a pole-inclusive grid, against
the paper's published multipole margins of 1.8×10⁻³ and 9.1×10⁻³.**
The dipole failure was a dipole-truncation artefact, exactly as the
paper's relaxation argument said; the published frontier bracket's
lower bound stands as DEC points at x ≤ 0.3. This confirms a
**subluminal accelerating shell** at gate standard at those points —
the category's first gate-verified positive row in this programme —
and nothing stronger.

## 1. Plain-language summary

Le's shell failed our Phase-71 audit only in its simplified
("dipole") form, and only in a thin band near the rear pole that the
paper's own scan never sampled. The paper also contains a fuller
("multipole") version of the shell, which it says repairs exactly
that. This item rebuilt the fuller shell from the published record
and re-audited it on a grid that includes the pole itself. At the
three lower-compactness operating points the fuller shell is legal
everywhere we can measure — including exactly at the rear pole,
where the dipole version failed — and its safety margins match the
paper's published numbers closely. At the two highest-compactness
points our solvers could not finish rebuilding the shell to the
paper's own tightness, so those two points are left open, honestly
named; nothing there is either confirmed or refuted.

## 2. Reconstruction — what the published record does and does not give

- **Paper text (Supplement §S)** specifies the multipole solve
  completely as a *method* (finite-λ least-squares of [h_ab] = 0;
  shape R(ϑ) = R₀(1 + Σ a_l P_l); lapse and tilt modes on both sides;
  residual and margin claims) but publishes **no multipole
  coefficients** — only outcomes: margins {1.8, 9.1, 18, 21}×10⁻³ at
  x = {0.1, 0.3, 0.5, 0.7} at the pins g̲(x), max|[h]| = 1.4×10⁻⁷ at
  x = 0.1 and ~10⁻³ at x = 0.5, 0.7 (L = 6; L = 8–10 tightening).
- **The published code** (cited by the paper's Data Availability
  statement; the Supplement says the configurations and tolerances
  "accompany the implementation") gives the full specification:
  unknowns ρ_l, At_l, w_l, wi_l, Ai_l (l = 1..L), bounded
  least-squares, interior tilt + interior lapse ON, pins
  {0.19, 0.20, 0.19, 0.14, 0.09} at x = {0.1, …, 0.7}. One record
  finding: **the author's own multipole stress grid also stops short
  of the poles** (θ ∈ [0.12, π−0.12]) — the paper's "binding at the
  rear pole" is, in its own numerics, binding at π−0.12. Our audit
  grid (§3) evaluates the pole itself.
- **Reconstruction route used:** the published specification solved
  independently in the programme's FD auditor (damped Gauss–Newton /
  Levenberg–Marquardt, coefficient-space FD Jacobian, start = padded
  Phase-71 dipole, author's dof layout and box bounds), at L = 4 and
  L = 6. The author's own code was also run (deviation D1, run
  record): at x = 0.1 its staged residuals (L = 2: 7.4×10⁻⁴;
  L = 4: 4.4×10⁻⁶) track the same geometric closure as ours
  (L = 4: 5.3×10⁻⁶; L = 6: 1.5×10⁻⁷ vs the paper's printed
  1.4×10⁻⁷ at L = 6) — three-way agreement on the closure scale.

## 3. Pole treatment (registered before any number was read)

Audit grid: uniform in μ = cosθ (161 pts) **with both pole endpoints
included exactly** (μ = ±1), plus refined bands θ ∈ [π−0.15, π]
(41 pts — the exact band the dipole scan skipped) and [0, 0.15]
(21 pts); 223 points total. Pole values are *computed at* θ = π
(Cartesian FD machinery is regular there; P_l(−1) = (−1)^l,
S_l(π) = 0 exactly), not extrapolated. Auditor re-gate before any
multipole number: static anchor to ≤2×10⁻⁶; dipole reduction
reproduces Phase 71's stored pole-band margins to all printed
digits, and at θ = π exactly the dipole margins are **−2.0096×10⁻⁴**
(x = 0.1) and **−1.2263×10⁻⁴** (x = 0.3) — Phase 71's pole limits,
now read at the pole itself.

## 4. Audit results at the claimed operating points

Worst-observer DEC margin (Eq. (35) form, R = 1 units), full grid,
h = 0.01; every pin below is Type-I at **every** grid point
(min discriminant > 0), with eigenvalue margins equal to the
worst-observer margin at the binding point and the sampled-observer
cross-check ≥ the exact margin, as registered.

| x | λ = g̲(x) | L | max\|[h]\| (FD) | worst margin | binding θ | pole (θ=π) margin | paper margin |
|---|---|---|---|---|---|---|---|
| 0.1 | 0.19 | 4 | 5.3×10⁻⁶ | **+1.7255×10⁻³** | π (rear pole) | +1.7255×10⁻³ | 1.8×10⁻³ |
| 0.1 | 0.19 | 6 | 1.5×10⁻⁷ | **+1.7283×10⁻³** | π (rear pole) | +1.7283×10⁻³ | 1.8×10⁻³ |
| 0.2 | 0.20 | 4 | 1.1×10⁻⁵ | **+5.1433×10⁻³** | 0 (front pole) | +5.6436×10⁻³ | — (pin only) |
| 0.3 | 0.19 | 4 | 1.4×10⁻⁵ | **+9.1105×10⁻³** | 0 (front pole) | +9.8296×10⁻³ | 9.1×10⁻³ |
| 0.3 | 0.19 | 6 | 2.6×10⁻⁶ | **+9.1021×10⁻³** | 0 (front pole) | +9.8547×10⁻³ | 9.1×10⁻³ |
| 0.5 | 0.14 | — | not closed (§5) | — | — | — | 18×10⁻³ |
| 0.7 | 0.09 | — | not closed (§5) | — | — | — | 21×10⁻³ |

- **h-ladders at the deciding angles** (h = 0.02 / 0.01 / 0.005 +
  4th-order at h = 0.01): x = 0.1 L6 pole margin
  {1.7219, 1.7283, 1.7299, 1.7305}×10⁻³; x = 0.3 L6 front-pole
  {9.0934, 9.1021, 9.1043, 9.1050}×10⁻³ — converged, spread ≤ 1.2×10⁻⁵.
- **Adversarial second path (registered):** the L = 4 and L = 6
  solves are independent reconstructions (separate solves, separate
  coefficient vectors); their pole margins agree to 2.8×10⁻⁶
  (x = 0.1) and 2.5×10⁻⁵ (x = 0.3), and both match the paper's
  published margins (x = 0.1: −4% vs 1.8×10⁻³; x = 0.3: +0.02% vs
  9.1×10⁻³ worst / rear-pole 9.85×10⁻³). The author's staged
  residuals at x = 0.1 (§2) are the third path on closure.
- **Binding-angle anatomy:** at x = 0.1 the multipole shell binds
  exactly at the rear pole (the paper's claim), where the dipole
  margin was −2.0×10⁻⁴ — the multipoles add ≈ +1.93×10⁻³ of margin
  at the pole. At x = 0.2 / 0.3 the binding point on the full grid
  is the *front* pole (θ = 0, also inside the author's unsampled
  band), with the rear pole close behind; both poles pass.
- **Bulk / volume:** the exterior bulk read is unchanged from
  Phase 71 (null dust, n² ≥ 0 ⟺ −ṁ ≥ 3m|a|, exact); the interior is
  the exactly flat cavity (vacuum). The shell is distributional
  (timelike matching shell); there is no additional volume
  representation of the multipole shell in the published record —
  the thick-wall volume reads were Phase 71's and are unchanged.

## 5. The open clause: x = 0.5 and x = 0.7

Named exactly: at (0.5, 0.14) and (0.7, 0.09) this run did **not**
produce a multipole coefficient set closed to the paper's own level
(max|[h]| ~ 10⁻³ at L = 6, theirs) in the programme auditor.
Attempts, all logged in the run record: direct Gauss–Newton from the
dipole (stalls at max|[h]| ≈ 0.06); bounded least-squares with
λ-continuation (under-iterates, plateaus ~2×10⁻³ absolute at the
first stage); Gauss–Newton + λ-continuation (linear crawl);
Levenberg–Marquardt + λ-continuation (best route: stage residuals
0.131 → 0.061 → 0.059 absolute-per-λ at λ = 0.042, plateauing
~9×10⁻²/λ ≈ 1×10⁻² absolute by λ = 0.112 — still an order above the
paper's closure). The author's own solver (autodiff Jacobians) was
still working through its low-x stages on this shared cell when
this memo closed. **This is a solver-convergence gap on our side,
not evidence about the shell:** the paper's margins at these pins
(18, 21×10⁻³) are neither confirmed nor impeached, and the dipole
reads at these pins from Phase 71 (which passed) are untouched.
Reopening condition: a closed (max|[h]| ≲ 10⁻³) coefficient set at
either pin, from the author's code completing or an AD-Jacobian
FD-free solve, read on this memo's audit grid — the audit script
(`work/p801_audit2.py`) takes any stored coefficient set.

## 6. C12 accounting

What was computed: a reconstruction of a *published* configuration
from its published specification, and a gate audit of that
reconstruction. The configuration is **pre-existing** (the paper's),
not a programme construction; no formation claim is made or audited.
Category-exact language: this is a subluminal accelerating shell of
the Bobrick–Martire class, paying Bondi mass by photon-rocket recoil
(−ṁ ≥ 3m|a|); it is not FTL, not a payload-transport row, and not a
programme shell. The confirmation at x ≤ 0.3 is a statement about
the paper's DEC certification of its multipole shell at those
operating points, at this programme's bars. The thin shell's matter
model remains a constitutive hypothesis (the paper's §7.2 radiating
layer), exactly as in Phase 71; the stricter source-consistency
standard of the author's companion paper (arXiv:2605.25417) is a
different bar, not applied here, as registered.

## 7. Failure Protocol — follow-ups (≥1, mechanism-suggested)

- **FU-P801-1 (the open clause):** close x = 0.5 / 0.7 with an
  autodiff-Jacobian solve (the author's published code run to
  completion on an uncontended machine, or a JAX re-implementation
  of the FD auditor's residual), then read the coefficients on
  this item's pole-inclusive audit grid via `p801_audit2.py`.
  Mechanism: every FD-Jacobian solver here degraded exactly where
  the Jacobian's conditioning worsens with x (the author's AD
  route does not), so the deciding instrument difference is the
  Jacobian, not the physics.
- **FU-P801-2:** pole-limit frontier curve for the MULTIPOLE shell:
  with the multipole solve trusted at x ≤ 0.3, scan λ upward at
  x = 0.1 / 0.3 on the pole-inclusive grid to locate the multipole
  margin zero λ*_mp(x) ≥ g̲(x) — the paper asserts the true frontier
  lies at or above the pins; the size of the gap measures how much
  frontier the dipole scan's truncation was hiding.
- **FU-P715-3 (carried, now cheaper):** the worked burn (Thm. 3,
  x⋆ = 0.3, λ_max = 0.12) per-cut pole read — λ_max = 0.12 is well
  below the confirmed multipole margin zero at x = 0.3, and the
  machinery of this item reads it directly.

## 8. Deliverables and checker

- `results/p801_memo.md` (this memo); `results/p801_run_record.md`
  (sources log with dates/URLs, pole treatment registered before
  numbers, deviations D1–D2, instrument log).
- `results/p801_solve.json` — reconstructed coefficient vectors +
  solve histories (L = 4 / 6 at the confirmed pins; the stalled
  high-x attempts stored and marked by their residuals).
- `results/p801_audit.json` — full per-θ audit rows (stress, margin,
  type, eigenvalue margins, discriminant) + ladders for every
  audited pin.
- `results/p801_recon.json` — author-path outputs (staged residuals
  in the run record; the file lands when the author's x = 0.1 job
  completes — it was still running at memo time).
- `results/p801_check.py` → `results/p801_check.json`: recomputes
  every deciding number from the stored JSONs — **73/73 PASS** at
  memo time (bars per pin, row-level margin recomputation, ladder
  spreads, L4-vs-L6 pole-margin agreement, paper-margin comparison).
- Scripts: `work/p801_lib.py` (auditor), `work/p801_solve.py`,
  `work/p801_solve3.py`, `work/p801_solve4.py` (solvers),
  `work/p801_audit2.py` (audit driver), `work/p801_reconstruct.py`
  (author path). float64 throughout.
