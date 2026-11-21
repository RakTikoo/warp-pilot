# How these claims were gated — Gate-2

Before any Phase 8–9 result from this programme may be uploaded
for outside verification, it must pass an internal Novelty &
Verification Gate implementing a standing rule: publish only
what we are sure is (a) **new** — not already in the literature —
and (b) **right** — verified to the programme's full standard.
The gate itself uploads nothing and contacts no one; it prepares
verdicts only. This page summarises, for each of the three claims
in `CLAIMS2.md`, how it was gated and what the gate decided.
(Condensed from the gate's internal record, GATE2.md, 2026-11-21.
Gate-2 follows the same standard and method as this programme's
Gate-1.)

## The gate's method (same for every claim)

**Novelty axis.** A systematic arXiv + web search for the claim's
exact statement and its near neighbours. Every query is logged
verbatim, sources are graded, near neighbours are cited by arXiv
ID/DOI, and the key neighbouring papers are read in full text.
Verdicts: **NOVEL** / **PARTIALLY KNOWN** (with the known part
cited exactly) / **KNOWN** (the claim dies as "ours"). A NOVEL
verdict is always backed by a one-sentence delimitation of
exactly what is new, quotable in an upload.

**Correctness axis.** An independent second path: the deciding
computation is reimplemented *from the claim statement*, as
fresh code that does not import the original machinery (shared
*definitions* — e.g. a stored solution field whose audit is the
claim — may be carried over; the deciding machinery may not), or
derived analytically where feasible. Verdicts: **REPRODUCED**
(same signs and values within the claim's stated margins) /
**NOT YET** (the specific missing piece named) / **FAILS**
(anatomy required).

**Gate verdict per claim.** **UPLOAD-READY** /
**UPLOAD-READY AFTER RESTATEMENT** (the restated form supplied
by the gate and applied in `CLAIMS2.md`) / **NOT YET**. A claim
that is KNOWN or FAILS is dead as ours.

All arithmetic float64, throughout.

## Claim 1 — G2-1, the moving re-solved shell in Schwarzschild

- **Novelty: NOVEL (delimited; two components PARTIALLY KNOWN).**
  20 logged queries, 18 sources graded, full-text reads of
  Garattini–Zatrimaylov arXiv:2408.04495, Schuster–Santiago–
  Visser arXiv:2205.15950, Bolívar–Abellán–Vasilev
  arXiv:2608.15000, Idrissov arXiv:2610.17629, Abellán et al.
  arXiv:2512.16109; citation follow-ups on Bobrick–Martire /
  Fuchs et al. arXiv:2405.02709 (no curved-background, offset, or
  re-solved follow-up found). Per component: (1) the
  offset/two-centre re-solved shells — NOVEL (published shells
  around black holes are concentric and thin: Frauendiener 1990,
  Brady–Louko–Poisson, Idrissov 2026; no two-centre shell
  equilibrium or inflow-value-mismatch mechanism found);
  (2) a moving re-solved shell passing all energy conditions in
  a curved background — NOVEL (areal embedding only;
  curved-background moving results in print are metric-first
  with persisting violations, and all-conditions passes exist
  only in flat background); (3) the dependence of the verdict on
  the construction — PARTIALLY KNOWN as a theme
  (Santiago–Schuster–Visser's Eulerian-vs-all-observer warning,
  arXiv:2105.03079; lapse-family verdict flips), with the
  specific areal-pass/PG-fail pair for one moving re-solved
  offset shell, and its window×inflow anatomy, not found;
  (4) the lapse-inconsistency diagnosis — PARTIALLY KNOWN as a
  phenomenon (Bolívar–Abellán–Vasilev arXiv:2608.15000 publish
  unit-lapse-PG-fails / lapse-released-passes for static hollow
  shells; Abellán–Bolívar–Vasilev, Class. Quantum Grav. 41
  (2024) 105011), with the specific diagnosis (shell-only lapse
  over a superposed total shift; the total lapse flipping the
  stationary core −9.6e-5 → +4.1e-5) not found.
- **A binding wording correction came out of the novelty axis:**
  the dependence must not be described with the bare term
  "slicing-dependence". Pointwise energy conditions for a fixed
  tensor are coordinate-invariant, and the Phase 9 record itself
  establishes that the areal and PG builds are different ansatz
  spacetimes (no exact transform exists). The defensible wording
  is **embedding/ansatz-dependence**, with both embeddings named
  every time the moving pass is stated.
- **Correctness: REPRODUCED.** Independent second path: a fresh
  auditor (no programme audit machinery imported; Einstein
  tensor from direct metric finite differences with its own
  stencils, own Eulerian triad and Hawking–Ellis margins,
  off-lattice sampling; only the shell prescription and metric
  builders shared as definitions). Background-only controls at
  the finite-difference floor (max|T| 1.2×10⁻¹⁴ PG /
  1.6×10⁻¹⁴ areal). (a) Areal moving β = 0.02 rows reproduced:
  d = 50 cavity NEC −2.54×10⁻⁸ (claim −2.75×10⁻⁸, same edge
  site), core +2.82×10⁻⁵ (claim +3.16×10⁻⁵), Type-I 1.000;
  d = 100 cavity −2.8×10⁻⁹ (claim −1.48×10⁻⁸; both in the floor
  class), core +2.93×10⁻⁵ (claim +3.27×10⁻⁵), Type-I 1.000 —
  pass criteria met at both offsets. (b) The total-lapse
  diagnosis reproduced with the tightest match: shell-only-lapse
  PG core −9.80×10⁻⁵ (claim −9.63×10⁻⁵, same site); total-lapse
  PG core +4.13×10⁻⁵ (claim +4.11×10⁻⁵), Type-I 1.000; areal
  re-solved +4.60×10⁻⁵ (claim +4.57×10⁻⁵) — the sign flip
  reproduces essentially exactly. (c) The PG moving read
  reproduced at sign level, as pre-registered for that
  sub-item: d = 50 core −1.54×10⁻⁶ (claim −3.36×10⁻⁶ — negative
  at the same binding site; magnitude ~2.2× smaller, not a 20%
  value reproduction); d = 100 core +1.35×10⁻⁵ (claim
  +1.15×10⁻⁵), Type-I 1.000. The d-dependent PG split
  reproduces. No FAILS, no unchecked items.
- **Gate verdict: UPLOAD-READY** — with wording conditions
  (i)–(v): (i) the novelty delimitation sentence accompanies the
  claim; (ii) embedding/ansatz-dependence language, both
  embeddings named, the PG d = 50 failure stated alongside the
  areal pass; (iii) the lapse-flip phenomenon credited as
  published for static concentric hollow shells
  (Bolívar–Abellán–Vasilev arXiv:2608.15000; Abellán–Bolívar–
  Vasilev CQG 41 (2024) 105011) — the claim is the specific
  diagnosis, not the phenomenon; (iv) the PG moving d = 50 core
  value labelled sign-reproduced (−1.5e-6…−3.4e-6 across the two
  paths), not a precision value; (v) scope β = 0.02, constant
  velocity, M_bg = 1, d ∈ {50, 100}, with the r ≈ 8.9
  edge-artefact separation stated with the cavity numbers. All
  five are applied in `CLAIMS2.md`.

## Claim 2 — G2-2, the Einstein-aether speed-asymmetry

- **Novelty: PARTIALLY KNOWN (components (1)–(2) NOVEL).**
  24 logged queries, ~14 sources graded, full-text reads of
  Golchin et al. arXiv:2511.00825, Oost–Mukohyama–Wang
  arXiv:1802.04303, Jacobson arXiv:0711.3822, Foster–Jacobson
  gr-qc/0509083, Santiago–Schuster–Visser arXiv:2105.03079,
  Lobo–Visser gr-qc/0406083, Rodal arXiv:2507.09724. Per
  component: (1) the aether-on-a-warp-wall computation — NOVEL
  (delimited): no Einstein-aether / khronometric / vector-tensor
  correction tensor on any warp metric found; the theory's only
  exotic-geometry paper is Golchin et al. on static wormhole
  throats (different object, no speed axis, no Eulerian-normal
  supply scan on the c₁₃ = 0 slice). The ingredients (the
  theory, its health functionals, the
  modified-gravity-carries-the-violation idea) are published.
  (2) The speed-asymmetry — NOVEL: no supply reported starved
  subluminal / fed superluminal in any theory; published speed
  results run opposite or flat (Lobo–Visser; Bobrick–Martire;
  Santiago–Schuster–Visser). Caveat carried: a binding-point,
  prescribed-u, off-shell statement at three sampled speeds; the
  GR deficit itself grows ×14–17 superluminally. (3) The
  outer-band sign-flip locus — PARTIALLY KNOWN: wall
  localisation of NEC failure is textbook; a correction supply
  covering the inner wall and failing exclusively in
  r ≈ 18.5–19.75, capped by its own sign flip, not found.
  (4) The PPN exclusion of the scanned supply — PARTIALLY
  KNOWN: the formulas, bounds, GW slice, health functionals and
  the general α₁ = α₂ = 0 tuning are Foster–Jacobson / Jacobson
  / Oost et al.; two precedents cap the novelty — Golchin et al.
  published the identical exclusion *pattern* for æ-theory
  wormholes, and Rodal (2025) published PPN/solar-system
  exclusion of a (scalar-tensor) warp supply. New as stated
  results: the row-by-row 0/327 exclusion with α₂ as the
  binding gate. (The novelty report also listed an on-slice
  tuning corollary as new-as-stated; the correctness axis then
  showed its mechanism to be false — see below — and the
  corrected mechanism takes its place in the claim under the
  same delimitation.)
- **Wording hazards recorded (binding):** never drop "on the
  c₁₃ = 0 slice" from any tuning claim (a healthy α = 0 family
  exists in the full theory); never say the supply "works"
  superluminally (no alignment, PPN-excluded, Čerenkov-failing;
  mode superluminality ≠ bubble β); name the α₂ gate used
  (4×10⁻⁷ is Jacobson's; Oost quotes 10⁻⁷ — the programme's
  gate is the conservative one); the u-ansatz is the
  hypersurface-orthogonal / khronometric sector, prescribed not
  solved; Ellis's "ether" (gr-qc/0411096) is a false friend,
  not a precedent.
- **Correctness: REPRODUCED on every deciding number — one
  stated mechanism FAILS, restatement required.** Independent
  second path: the correction tensor derived by hand and
  verified against pointwise finite differences to 2.8×10⁻¹⁰;
  own divergences at own step sizes; the overall sign fitted by
  its own spherical gate; the full 109×3 grid evaluated via
  coupling linearity; no re-run of the Phase 9 scan and no
  import of its tensor code in the deciding path. Tensor:
  spherical-gate ratio 1.0000 (max deviation 2×10⁻⁴, two
  coupling sets). Coverage: the bed re-derived from the second
  path's own Einstein code (251 / 504 / 594 binding points; max
  GR deficits matching Phase 9 to the digits shown); β = 0.1
  best partial 0.000 over the full grid (all 109 fractions
  identical to the recorded ones); β = 1.1 named row partial
  0.8135 (exact), full 0.2163 (recorded 0.2183); best
  health-passing full 0.2202; β = 1.5 best health-passing
  partial 0.7912, best full 0.4495 — every deciding fraction
  within ±0.01, ratio-free cross-checks never fired; the
  outer-band locus reproduced; no spikes (worst ratio
  −0.295 / −0.614 against the claimed −0.30 / −0.61). Health
  and data: flags identical to the recorded ones on all 327
  rows (α values to <10⁻⁹ relative); 32/109 health-passing per
  speed; α₁ = −4·c₁₄ on the slice (symbolically exact); best
  rows α₂ = +2.0; probe rows at c₁₄ = 10⁻⁵ fail α₂ at
  −5.0×10⁻⁶ against the 4×10⁻⁷ gate; total data-passing
  **0 of 327 — exact**. **The failure:** the sub-claim "α₂ = 0
  tuning forces c₂ < 0 → s₀² < 0" does **not** reproduce.
  Symbolically, α₂ = 0 on the slice is equivalent to
  c₂ = c₁₄/(1−2c₁₄) — *positive* for c₁₄ < 1/2 — and s₀² ≡ 1
  exactly on the whole α₂ = 0 curve. The second path's own
  probe rows settle the correct mechanism: the tuned
  c₁₄ = 10⁻⁵ row (c₂ = +1.00002×10⁻⁵) is health- *and*
  data-passing but has coverage 0.000 at every speed (the
  supply collapses); the tuned c₁₄ = 1 row (c₂ = −1) is
  health-passing with partial coverage 0.708 / 0.741 but is
  excluded by α₁ = −4. **Correct mechanism: exclusion of the
  supplying rows is driven by α₁ = −4c₁₄ jointly with α₂; the
  data-compatible corner carries ~zero supply.** The Phase 9
  anatomy's one-line explanation was wrong; its headline
  (0/327) is exact.
- **Gate verdict: UPLOAD-READY AFTER RESTATEMENT.** The
  restatement is the exclusion mechanism only: the false
  sentence is deleted and replaced by the gate's corrected
  mechanism text (quoted verbatim in `CLAIMS2.md`). Upload
  wording must additionally carry: (i) the novelty delimitation
  sentence, with the PPN machinery credited to
  Foster–Jacobson / Jacobson / Oost and the precedents (Golchin
  et al. arXiv:2511.00825; Rodal arXiv:2507.09724) cited;
  (ii) "on the c₁₃ = 0 slice" on every tuning statement, and
  never "the supply works superluminally"; (iii) the α₂ gate
  named as |α₂| ≤ 4×10⁻⁷ (Jacobson's value; Oost quotes
  10⁻⁷); (iv) the labelling: binding-point, prescribed-u
  (khronometric sector, u not solved from its equation of
  motion), off-shell supply statement at three sampled speeds —
  not a drive claim, not an alignment claim. All applied in
  `CLAIMS2.md`, which also flags, in an editorial note, the one
  clause of the quoted delimitation sentence that the
  restatement replaced.

## Claim 3 — G2-3, the realised toroidal metric

- **Novelty: PARTIALLY KNOWN (NOVEL delimited core).**
  22 logged queries, ~18 sources graded, full-text reads of
  Fuchs et al. arXiv:2405.02709, Dzhunushaliev et al.
  arXiv:1901.07545, Lynden-Bell & Katz arXiv:1205.1616, White
  NTRS 20110015936, Santos-Pereira et al. EPJC 2022, and the
  Meyler MFHD manuscript. Per component: (a) toroidal geometry
  in warp physics — KNOWN (Alcubierre 1994's read-off source is
  a negative-energy torus; White's thick toroidal analysis
  2011–12; González-Díaz's ringhole, Phys. Rev. D 54 (1996)
  6122); (b) the conditions-first / source-first method —
  PARTIALLY KNOWN (the classical direction of GR; Fuchs et al.
  is a genuine partial precedent — prescribed density → TOV →
  metric — but spherical / one-dimensional with the shift added
  afterwards; Einstein–Vlasov tori, arXiv:1603.05404, prescribe
  and solve in astrophysics); (c) the realised toroidal shell
  (γ(s,φ) in g_ψψ, boundary conditions built into the basis,
  full meridional solve to residual RMS 1.89×10⁻⁴) — NOVEL
  (delimited): every neighbour misses a load-bearing element
  (Dzhunushaliev et al.'s thin-shell T² wormholes explicitly
  leave the thick PDE problem open; Lynden-Bell & Katz and
  Krisch & Glass, gr-qc/0303110, are exact fitted toroidal
  solutions with matter read off). The γ-count-restoring move
  and boundary-conditions-in-basis are themselves PARTIALLY
  KNOWN standard techniques — the novelty is the realised
  object and its residual, not the techniques; (d) the Gelfand
  branch boundary at ρ_c·s_t² ∈ (0.6–0.7)× — NOVEL (delimited);
  the fold / extremal-parameter phenomenon itself is textbook
  (Joseph–Lundgren), and the boundary is a numerical bracket,
  not an analytic extremal value; (e) toroidal shells and
  Einstein solutions audited against energy conditions outside
  warp physics — KNOWN (Lynden-Bell & Katz 2012; toroidal black
  holes, Class. Quantum Grav. 42 (2025) 155015); (f) the
  β = 0.02 inner-equator NEC negative on the realised metric —
  NOVEL as a specific measurement, low weight (moving-warp NEC
  failure in general is known, Santiago–Schuster–Visser
  arXiv:2105.03079; no realised-toroidal-metric audit found).
- **Wording hazards recorded (binding):** a self-published
  manuscript (Meyler, PhilArchive, March 2025 — not
  arXiv-indexed, not peer-reviewed) publicly claims a toroidal
  positive-energy warp metric with "first complete derivation"
  language; a full-text read shows it is ansatz-first
  (one-variable functions, stress-energy read off, energy
  conditions asserted) — it does not anticipate the delimited
  claim, but it kills any unqualified "first toroidal warp
  metric" wording on sight. Also banned: "first toroidal shell
  satisfying energy conditions", "first toroidal Einstein
  solution", "solved" without the residual, and any conflation
  with T²-throat topology. All applied in `CLAIMS2.md`: the
  word "first" appears only inside the delimited
  conditions-first construction.
- **Correctness: REPRODUCED (one precision caveat).**
  Independent second path: a generic tensor-calculus Einstein
  evaluator in toroidal coordinates (explicit index sums;
  4th-order stencils; a new 97×40 grid against the original
  81×32; the stored solution fields — the claim's definition —
  carried over by interpolation; no Phase 8 script re-run).
  (1) Realisation residual reproduced: solved fields RMS
  1.978×10⁻⁴ (claim 1.894×10⁻⁴, +4.4%); γ = 0 base on the same
  grid 3.015×10⁻³ (claim 2.99×10⁻³); reduction 15.24× (claim
  15.8×); the no-uniform-floor structure confirmed with the same
  component ordering and spread; boundary-condition facts on
  the stored fields exact. (2) Branch boundary reproduced to
  the digits: fresh high-order shooting gives max β(15) =
  −0.18528 at λ = 1 (claim −0.18528), +0.16130 at λ = 1/2,
  +0.491 at 1/4, +0.767 at 1/10; refinement −0.00694 at
  λ = 0.7, +0.07014 at λ = 0.6 — boundary in (0.6, 0.7)×,
  exactly as claimed. (3) Motion audit reproduced in sign and
  converged magnitude, with a caveat: a fresh Cartesian point
  judge (different stencils, 642 sampled null directions, two
  orientations) finds the inner-equator NEC negative at every
  grid spacing and both orientations; Type-I fraction 0.784
  (claim 0.789); static control Type-I 1.000. The caveat's
  anatomy: the headline coarse-grid values do **not** reproduce
  within 25% — the worst point sits at s = 14.5, φ = π, one
  stencil-reach from the s = 15 taper, and is
  stencil/orientation-unstable in *both* judges. But the
  fine-grid (h = 0.075) converged values agree almost exactly
  across both paths: moving −1.51×10⁻⁴ in both judges; static
  −3.37×10⁻⁵ against the claimed −3.40×10⁻⁵. The negative is
  real and converged; the specific coarse-grid figure is an
  inflated, stencil-unstable number and must not be quoted as
  converged.
- **Gate verdict: UPLOAD-READY AFTER RESTATEMENT.** The
  restatement is only in the motion-audit numbers (the
  realisation and branch parts of the claim stand as stated):
  the motion negative is restated with the converged fine-grid
  value −1.51×10⁻⁴ at h = 0.075 (identical in both judges;
  static control −3.4×10⁻⁵), with coarse-grid values near the
  surface ring declared stencil-sensitive and not quoted as
  converged (the gate's restated text is quoted verbatim in
  `CLAIMS2.md`). Upload wording must additionally carry:
  (i) the novelty delimitation — "first" only in the delimited
  conditions-first sense, with the banned wordings above not
  used; (ii) credit: toroidal warp geometry (Alcubierre 1994;
  White 2011–12; González-Díaz ringhole 1996), the
  conditions-first precedent (Fuchs et al. arXiv:2405.02709,
  spherical), the γ-technique and the fold phenomenon as
  standard tools; (iii) scope: one prescription (R = 45,
  s_t = 15, ρ_c = 2.708×10⁻⁴), the residual is a numerical
  solve not an exact solution, the branch boundary is a
  numerical bracket (0.6–0.7)× not an analytic extremal value.
  All applied in `CLAIMS2.md`.

## Errata owed to the internal records

The gate logged three corrections to be appended to the
programme's Phase 8 / Phase 9 records as dated errata (done at
bundle assembly, 2026-11-21):

1. **Phase 9, P9-3 anatomy (α₂ mechanism).** The sentence
   claiming that α₂ = 0 tuning on the c₁₃ = 0 slice forces
   c₂ < 0, flipping s₀² < 0 (health-incompatible), is **wrong**.
   The correct mechanism (verified by the gate's independent
   path, including probe rows): on the slice α₁ = −4c₁₄
   exactly; α₂ = 0 gives c₂ = c₁₄/(1−2c₁₄), positive for
   c₁₄ < 1/2, with s₀² ≡ 1 on the whole curve — the tuning is
   health-compatible; the scanned supply is excluded because
   supplying rows carry c₁₄ large enough that α₁ (jointly with
   α₂) violates the PPN bounds by orders of magnitude, while
   the data-compatible corner has partial coverage 0.000 at
   every speed. The 0/327 exclusion itself is exact and stands.
2. **Phase 8, P8-3 motion value.** The coarse-grid (h = 0.3)
   inner-equator NEC figure quoted in the Phase 8 record is
   stencil-unstable; the converged value is −1.51×10⁻⁴ at
   h = 0.075 — a value Phase 8's own grid ladder already
   contained — identical in the gate's independent judge
   (static control −3.4×10⁻⁵). The coarse figure must not be
   quoted as converged.
3. **Phase 9, P9-1 wording.** "Slicing-dependence" in the P9-1
   reporting should read **embedding/ansatz-dependence**: the
   areal and PG builds are different ansatz spacetimes and no
   exact transform between them exists (the Phase 9 record
   itself establishes this); pointwise energy conditions for a
   fixed tensor are coordinate-invariant.

## Summary

| Claim | Novelty | Correctness | Gate verdict |
|---|---|---|---|
| G2-1 moving re-solved shell | NOVEL (delimited; two components PARTIALLY KNOWN) | REPRODUCED (all three sub-items; PG d = 50 moving value sign-reproduced) | UPLOAD-READY (wording conditions (i)–(v), incl. embedding/ansatz-dependence language) |
| G2-2 aether speed-asymmetry | PARTIALLY KNOWN (computation + asymmetry NOVEL) | REPRODUCED on every deciding number; one stated mechanism FAILS | UPLOAD-READY AFTER RESTATEMENT (corrected exclusion mechanism, applied in `CLAIMS2.md`) |
| G2-3 realised toroidal metric | PARTIALLY KNOWN (realised object + branch location NOVEL, delimited) | REPRODUCED (one precision caveat) | UPLOAD-READY AFTER RESTATEMENT (converged motion value, applied in `CLAIMS2.md`) |

Nothing in this bundle was uploaded by the gate. The gate
prepared verdicts only.
