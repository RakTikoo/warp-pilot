# FTL / Warp Pilot — Final Internal Report

**Status:** ledger fully closed 2026-11-21 (continuation session 3).
**Work dir:** `~/workspace/warp-pilot/` — ground record `CHECKPOINT.md`,
results in `results/`, frozen configs in `results/frozen/`.
**Sequencing lock (in force):** nothing leaves this machine; no external
contact, no publication; outside experts only on Rakshit's separate
explicit go, after exhaustion is declared.

## Plain-language summary

**The short version: no faster-than-light warp drive was found, and the
search that failed to find one is now thorough enough to say where the
wall is, how thick it is, and what would have to change to get past it.
The programme did find real, verified subluminal warp shells that are
lighter than anything in the literature at their speed — the fastest
verified one moves at 5% of light speed, and a conditions-first
construction showed the 10%-of-light-speed wall is partly a quirk of
the shape families we started with — but it could not get a fully
legal design past 10%, from any direction tried.**

**By mission rung** (Rakshit's hierarchy: 1 = genuinely new physics;
2a = faster-than-light; 2b = practical near-light-speed):

- **Rung 2a (FTL): NO.** Every superluminal test failed, in every
  geometry and every theory lens tried — spherical shells, donuts,
  free-form machine shapes, a fully 3D blob, shells sitting on curved
  backgrounds, shells in an expanding universe, and five modified-
  gravity / exotic-source lenses. The failures are not close calls:
  at superluminal speeds the audits hit the bottom of the scale
  (the matter tensor stops being classifiable at all — "Type IV"
  pockets), with deficits thousands of times larger than the margins
  the subluminal shells live on. Section 4 maps each geometry
  separately so no single claim is over-read.
- **Rung 2b (practical near-c): YES, up to a hard ceiling.** Two
  verified subluminal shells beat the published Fuchs baseline:
  **Finalist A** — 2.69×10²⁷ kg at β=0.02 (40% lighter than Fuchs at
  the same radius and speed); **Finalist B2** — 3.64×10²⁷ kg at
  β=0.03 (19% lighter and 50% faster). The lightest verified shell
  at β=0.05 is 2.58×10²⁷ kg. **β=0.1 is the ceiling**: the forward
  search located the wall there to within ~1e-9 of zero, and a
  completely independent conditions-first construction (prescribe
  legal matter, integrate back to a metric) confirmed the same wall
  from the other side — it can make the *interior* legal at β=0.1,
  but the full configuration saturates at the boundary. Nothing
  legal exists at β=0.1 in anything this programme can build, and
  the failure site migrated to the support tail — the last place
  left to look in this family.
- **Rung 1 (new physics): the failures taught things.** Three
  structural findings: (1) *every* perturbative modification tried
  (quadratic gravity, non-minimal scalar, extra-dimension gradients,
  background curvature, expansion) pushes the binding margin the
  wrong way — the deficit is robust to modifications *around* the
  shell; (2) the Einstein–Cartan spin term is the one classical
  term with the right sign, but it would need matter at 10³⁹ kg/m³
  (21 orders above nuclear density) — the coupling is fixed by
  nature, not tunable; (3) a proof-grade negative: no mixture of
  ordinary components can ever sum to a violating total (energy
  conditions are linear), so "combine two legal sources" is closed
  by arithmetic, not by search. The one genuinely new instrument
  built — the conditions-first inverter — works exactly where the
  answer is known (reproduces the verified shell's metric to
  ~3×10⁻⁷) and is the programme's most reusable asset.

**What it would take to reopen this:** a construction that solves
the shell *in* its background instead of superposing onto it; a
genuinely toroidal equilibrium construction (not profiles bent from
spheres); a prescription basis with an explicit boundary-layer
family at the support edge (the β=0.1 tail); or a modified-gravity
theory whose extra terms are not perturbative around the shell.
Each is named precisely in the ledger with what it would need.
Nothing in this report is a claim about nature — it is a map of
what was searched, how hard, and where it stopped.

---

## 1. Technical record

### 1.1 The judge (Phase 0, calibration)

- Point auditor: finite-difference Einstein tensor (float64, JAX x64
  confirmed) + Hawking–Ellis classification with all-observer
  NEC/WEC/SEC/DEC margins. PASS requires Type I + all margins above
  numerical error, confirmed at two resolutions AND an independent
  second path. Judge passes 5/5 unit tests; Alcubierre FD-vs-analytic
  converges 28.5% → 0.90% under refinement; the exact Alcubierre
  tensor is Type IV at generic wall points (a real calibration
  finding, not a bug); Fuchs smoothed shell passes, unsmoothed fails
  DEC exactly as Fuchs stated; Van den Broeck violations reproduced.
- **Four audit artefact classes** (each caught live this programme):
  (i) radial sampling hole; (ii) angular pocket; (iii) stencil-scale
  exploitation; (iv) **threshold poisoning** (session 3, X2: one
  out-of-domain point with |T| ~ 1e297 inflated the significance
  threshold and silently emptied a verdict set). Defences:
  re-randomised screens between screening and finals, arbiters at h
  and h/2, domain-restricted thresholds + overflow guards, and a
  sampled-null cross-check whenever a tensor's type is not already
  established (the eigenvalue NEC silently restricts to Type-I
  points — at β=1.5 it read +2.8e-7 while the sampled all-observer
  NEC was −3.36e-3).
- Quantum inequality ledger (Phase 1): Pfenning–Ford anchors within
  ~2×/16%; exponents v^2.000, R^1.97, Δ^−0.96; Casimir gap ~46
  orders of magnitude.

### 1.2 Verified subluminal finalists (rung 2b)

| Finalist | Geometry | Mass | β | vs Fuchs |
|---|---|---|---|---|
| A | (10,20) edge-peaked, cosine shift | 2.0 geom = 2.69×10²⁷ kg | 0.02 | 40% lighter |
| B2 | (10,20) | 2.7 geom = 3.64×10²⁷ kg | 0.03 | 19% lighter, 50% faster |
| Frontier β=0.05 | (5,10) lightest | 1.91 geom = 2.58×10²⁷ kg | 0.05 | min compactness M/R₁ = 0.383 |

- A, B2 and the β=0.05 frontier each survived R1 (adversarial
  point-hunt, 192 restarts × 500 steps — worst NEC found still
  positive), R2 (SymPy symbolic third path — min NEC agrees with
  FD to ~1%), and R3 (observer-sampling sign agreement 1.000).
  One tanh-shift "pass" was retracted after extended sampling
  found interior violations — the protocol works.
- Track L frontier: β=0.05 passes at compactness ≥ 0.383 at every
  scale; β=0.1 EMPTY for named families (closest near-miss
  −2.06e-7, autodiff tiebreak +1.3e-9, uncertifiable; M=11/12 fail
  DEC — the wall, Pattern P8); β=0.2–0.9 empty by wide margins.
- Track P: β=0.05 below-floor (M=3.5) closed negative — the 0.383
  floor stands against 11,264 free-form evals; β=0.1 free-form
  closed as the boundary measurement.

### 1.3 Session-3 closures (continuation coordinator #3)

**X1 toroidal φ-extension — CLOSED, bounded exclusion.**
φ-dependent corrections (28 extra genes, cos φ / cos 2φ on the
s-only winner) improved the static inner-equator deficit only
−1.78e-5 → −1.59e-5 (stage-1 −1.39e-5, stage-2 adversarial
saturation −1.59e-5; finals −1.60e-5/−1.92e-5, 15,030 DE evals).
Velocity ladder: v=0 reproduces the finals; v=0.02 already
collapses to the −1.0 floor (Type I 0.748 — the φ-optimised base
is more brittle than the s-only base); v ∈ {1.1, 1.5, 2.0} floor,
Type I ~0.46. P9 stands, strengthened. Reopening: a genuinely
toroidal equilibrium construction (N3 method ported to toroidal
topology).

**X2 backgrounds — CLOSED, bounded exclusion (superposition
class).** 59-row scan + definitive Schwarzschild rerun: background
curvature never assists; it degrades the shell monotonically with
background strength at every velocity. The static shell (β=0)
already fails on Schwarzschild (−9.9e-5 at M_bg=1 vs exactly 0 in
flat space). At β=0.02: −1.37e-4 (M_bg=1), −1.23e-3 (M_bg=2),
−4.13e-4 (M_bg=4) vs flat +1.85e-7. Superluminal rows fail worst
near β≈1 (NEC −2.0e-2, ~8× worse than flat). AdS: shell's own
difference tensor passes at β=0.02 — AdS is neutral for the shell
itself. Mechanism (F1): most degradation is already present at
β=0 — it is the matter-in-background interaction of the ad-hoc
superposition (multiplicative lapse × additive shift is not
solution-generating), not shift×inflow coupling. Reopening: a
construction that re-equilibrates the shell profiles in the
background lapse (background-TOV solver — new engine).

**Lens E expansion — CLOSED.** H from H₀-scaled to inflation
scale: today's expansion does nothing at shell scale (H₀ anchor
identical to flat). Shell-difference NEC deficit grows ≈ −ρ_bg/3,
crossover H* ≈ 1.3e-2/m. At H where recession across the shell
reaches 1.0c, the local audit is at its WORST — E2 made
numerical: recession is not transport; expansion violates SEC
not NEC and never supplies NEC. Superluminal rows fail within
10–30% of flat. Reopening: comoving re-solved shell (same as X2).

**X4 non-minimal scalar — CLOSED, negative in BOTH frames.**
22 configs (ξ ∈ {1/6, 1/4}, φ₀ ∈ {0.1, 0.3}, β ∈ {0.05, 1.1, 1.5}):
Jordan-frame T^(min) NEC negative in every row, worsening as
ξφ₀² (bump profile overshoots: F″ changes sign across the wall);
the mechanism-suggested follow-up (monotone tail profile,
one-signed F″) improved the Jordan NEC 40× at β=0.05 but still
failed everywhere, and the Einstein frame failed in all 22 rows
— no frame rescue, consistent with Fliss et al.'s effective-ANEC
restoration. Reopening: a coupled scalar-tensor solve, or an
interacting-field construction (no QEI theorem exists there).

**X5 Casimir threading — CLOSED, magnitude exclusion.** To cover
superluminal deficits (D_max 2.8–4.2e-3, ~57% of significant
points in deficit) a Casimir NEC supply would need cycle size
L ≤ 2.0 m (N_eff=1), 3.7 m (10), 6.6 m (100) — a bubble-sized
"compact" cycle — with negative-energy budget ~10× the shell's
mass and QI pulse ratio 65–585× over the Ford–Roman scale. No
superluminal shortcut shown. Reopening: a cycle geometry whose
mode sum beats the plate coefficient by orders (none known).

**N1 Kaluza–Klein lift — CLOSED, bounded exclusion.** Exact
warped-product reduction (σ=0 controls validate it: 5D NEC
+6.9e-7 at β=0.02, −3.36e-3 at β=1.5 — exactly the 4D source).
With σ₀ ∈ {0.1, 0.3} the 5D source's all-observer NEC is negative
in every row (β=0.02: −1.7e-3/−5.3e-3 — the lift of the VERIFIED
shell already needs an NEC-violating 5D source, worsening with
σ₀; β=1.5: −4.4e-3/−1.4e-2); Einstein frame at the −1.0 floor.
By the proposal's own rule: disguised exotic matter = FAIL.
Reopening: a stabilisation sector audited ordinary that cancels
the σ-gradient terms, or a warped (RS-type) lift carrying the
2.3 TeV floor.

**N2 Einstein–Cartan torsion — CLOSED, bounded exclusion by
magnitude.** The spin contact term is the one classical term with
the helping sign (NEC supply 2δ along the spin axis). Supplying
the β=1.5 deficit needs a spin-polarised fluid at 1.5×10³⁹ kg/m³
— 21.2 orders above nuclear density, with the coupling fixed by
GR constants (no free parameter). Reopening: non-minimal
torsion–matter coupling ≫ EC standard (different theory, gated
by spin-precession bounds).

**N4 two-component ordinary sources — CLOSED BY PROOF.** NEC is
linear in T, so NEC(T₁+T₂) = NEC(T₁)+NEC(T₂) ≥ 0 whenever every
component obeys NEC — a violating total cannot be assembled from
non-violating parts in any frame, with any interaction. Numeric
confirmation: 0/40 worst points admit an ordinary split at both
the β=0.05 below-floor point and the β=1.1 point (LP feasibility,
most favourable treatment; controls behave). The only exit is a
component that itself violates NEC — a ghost, i.e. exotic matter
under the E3 label. Strongest closure in the ledger.

**Track B free-form 3D blob — CLOSED NEGATIVE.** NL=5 lattice
(625 genes, Gaussian-RBF fields, no symmetry): DE screen
+8.86e-6 and 500-pt finals +2.78e-6/+3.58e-6 looked like a pass
at β=0.1 — the attack protocol broke it: dense audits (6,000 pts
× 3 seeds × 2 resolutions) found −1.87e-5/−1.21e-5/−1.64e-5
(a 3D sampling hole; the dense scale matches the seed's
−1.88e-5). Angular freedom at this lattice resolution bought
nothing against the wall. Also logged: the DE diluted the seed's
0.1 motion (interior ADM shift mean 0.036 — velocity was seeded,
not pinned) and the blob's mass was 47 geom units, not 10.
Refinement not triggered (did not end within 10× of the
spherical boundary). Reopening: a lattice whose seed reproduces
the spherical wall at ~1e-7 or better, with velocity pinned in
the objective.

**S6 free-form superluminal ladder — CLOSED.** (10,30) free-form
at β ∈ {1.1, 1.5, 2.0}: all at the −1.0 floor, Type I 0.31–0.38
(2,496 + 1,248 + 1,248 evals). No near-miss structure anywhere
the adversarial trainer looks. Reopening: none within free-form
spherical splines.

**N3 conditions-first (headline track) — CLOSED, wall confirmed
construction-independent.** Inverter (prescribe ρ*, p_t* = τρ*
freely; p_r from conservation integrated outward with secant
shooting; gauge = pilot ADM ansatz; ADM mass from the recovered
metric) validated on the forward construction (metric recovered
to max|da| = 3.3e-7). Four DE runs at β=0.1, M=10, (10,30):

- Run 1 (realisability-penalised objective): winner −2.1e-6.
  Diagnosis: the penalty exiled the best seed (objective-design
  artefact) → run 2.
- Run 2 (penalty removed): screen +2.44e-7, fresh finals
  +6.3e-7 sustained, Type I 1.000 — an apparent pass. Attack:
  dense audits confirmed the interior (min DEC +2.56e-7 over
  3,000 pts × 3 seeds × 2 resolutions; cavity +1.79e-7). The
  first tail failure (−1e-3) then decomposed into (layer 1) an
  audit artefact — the gfunc clamped the metric at its domain
  edge r=44, a kink with FD tensor ~1e-3 ∝ 1/h — fixed with an
  exact Schwarzschild continuation (far-field tensor ~1e-12,
  h²-clean; run 3, which chased the artefact, is void); and
  (layer 2) the real disease: beyond the prescription window
  (ρ* = 0 past r=38) the conservation law leaves a p_r tail
  ~ +1.8e-6, and a ρ=0, p_r≠0 tail violates DEC by |p_r|
  (DEC −1.8e-6 on [39, 52], resolution-independent). Run 2 is
  therefore NOT a verified pass: legal interior, illegal tail.
  The interior measurement stands: independent p_t freedom
  moves the β=0.1 interior margin from the forward wall
  (+1e-9) to +6.4e-7 — the wall was partly a family artefact
  (p_t slaving).
- Run 4 (soft exponential tail, decay length a gene; domain
  60, screens to 58): SPLIT verdict = negative — screen +2.85e-9,
  finals seed 555001 +2.12e-9, finals seed 777001 −1.24e-5
  (smooth pocket, Type I 1.000). With the tail honestly priced,
  conditions-first saturates at the same ~1e-9 wall.
- Below-floor run (β=0.05, M=3.5, (10,20)): DE converged to
  −7.83e-9 (both seeds/resolutions) — boundary contact from a
  second construction; the 0.383 floor is real, not beaten
  (tail unaudited in that run — the named follow-up).
- Formation snapshots (run-1 prescription): static β=0 at
  −2.87e-8; morph β 0→0.05 in 6 steps: worst ~ −3.1e-8 at every
  step — a quasi-static instant path exists at boundary-hugging
  margin (necessary, not sufficient, for formation — labelled).
  β=1.1 snapshot: floor, Type I 0.43.
- Axisymmetric step: closed by argument — a diffeomorphism
  pullback preserves every pointwise EC verdict exactly, so a
  deformed conditions-first metric is vacuous; the non-vacuous
  version is a coupled meridional PDE solve (not computable in
  this engine set; logged with its requirements).
- Reopening: (i) run-4-design rerun at the below-floor point;
  (ii) a prescription basis with an explicit boundary-layer
  family at the support edge; (iii) the meridional PDE
  inversion.

### 1.4 Patterns (fitted across the programme)

- **P1** Scale covariance: the frontier is a compactness–β curve.
- **P2** Failure-site migration: inner edge (β≤0.05) → mid-shell
  (0.1) → support tail (conditions-first) as designs improve.
- **P3** Shift transitions must live inside the matter support.
- **P4** Worst-margin vs M is non-monotone.
- **P5/P7** Modified-gravity anti-alignment: f(R), f(Q) quadratic
  corrections degrade the wall's NEC deficit monotonically once
  strong enough to matter.
- **P6** Free-form margin floor ~−2e-4 at compactness 0.35.
- **P8** The β=0.1 boundary wall: NEC/SEC pin ~1e-9 vs mass; tail
  DEC degrades with mass.
- **P9** Toroidal inner-equator deficit: tube-vs-sphere divergence
  mismatch ~−2e-5, aspect-independent for aspect ≥ 3.
- **P10** Modification robustness (session 3): every perturbative
  modification around the shell degrades or leaves unchanged the
  binding margin; the only levers that ever moved margins were
  compactness (P1) and in-shell profile freedom — and those
  saturate at P8. Plus the fourth artefact class (threshold
  poisoning) and the eigenvalue-only NEC trap.

### 1.5 Data-rule dispositions

- Case 1 (contradicted by data — dies): linear Lorentz-violating
  dispersion (Fermi GRB 090510, E_QG > 1.2 E_Planck); nothing in
  the finalist set is case-1 touched.
- Case 2 (covered — measured numbers rule): D1 Planck H₀, w₀
  (phantom variants only inside w ∈ [−1.06, −1.00], E3 label);
  D2 GW170817 c_T window for all modified-gravity claims
  (MG-1/MG-2/EC all have c_T = c); D3 Eöt-Wash (N1's L_y < 30 µm
  gate satisfiable by choice; unstabilised modulus excluded);
  D4 Cassini/MICROSCOPE/ATLAS as recorded per row.
- Case 3 (no coverage — labelled "mathematically established;
  experimentally untested regime"): all core EC audits, including
  every finalist and every closure above. No result in this
  report claims experimental contact.

---

## 2. R4 verification appendix

| # | Check | Method | Result | Remaining limitation |
|---|---|---|---|---|
| 1 | Judge correctness | Unit tests; Alcubierre analytic convergence; Fuchs/VdB reproduction | 5/5; 28.5%→0.90%; reproduced | FD truncation is modelled, not eliminated |
| 2 | Finalist A, B2, frontier | Two independent paths (FD point auditor + warpax autodiff), ~5 sig-fig agreement | VERIFIED (NEC +2.121e-5 both paths for A) | **Finite spatial sampling** — audits cover dense finite point sets, not the continuum |
| 3 | R1 adversarial hunt | 192 restarts × 500 steps minimising NEC/WEC | Failed to break A/B2/frontier | **R1 hunts NEC/WEC only** — SEC/DEC pockets are covered by dense audits, not by the hunter |
| 4 | R2 symbolic third path | SymPy axisymmetric derivation | Agrees with FD at every sampled point (all 3 finalists) | Axisymmetric path only; sampled points, not a proof |
| 5 | R3 observer completeness | Random observer sampling | Sign agreement 1.000 | Finite observer sample |
| 6 | Artefact sweep | Re-randomised screens/finals; h and h/2 arbiters; AD tiebreaks | Caught: sampling hole (Track P, Track B, N3 screens), angular pocket (Finalist B — replaced by B2), stencil exploitation (Track P), threshold poisoning (X2), domain-edge clamp kink (N3) | New artefact classes may exist that no instrument here imagines |
| 7 | Margin scale honesty | Margins reported with their FD noise context | **Numerical margins ~1e-5 (and the β=0.1 wall at ~1e-9) are not a proof** — they are measurements at stated resolution | A margin of +6e-7 is a strong numerical result, not a theorem |
| 8 | Velocity regime | All audits at constant velocity | Finalists verified at fixed β only | **Constant-velocity only** — acceleration, formation dynamics (except N3's labelled quasi-static snapshots) and stability are unmodelled |
| 9 | Matter model | Matter characterised only through the ECs | Finalists' T_ab is Type I with all margins positive | **Matter characterised only through the ECs** — no microphysical model, no equation-of-state realisation, no QI ledger entry makes the matter buildable |
| 10 | External replication | None | — | **No outside-expert re-run yet** — by the sequencing lock, that happens only on Rakshit's separate go |

---

## 3. Per-geometry superluminal exclusion map

Every entry: local β > 1 audited directly (recession never counted
as transport). "Bounded" = the stated volume was searched to
saturation; it is not a theorem about the class.

| Geometry / lens | Superluminal points | Result | Scale of failure |
|---|---|---|---|
| Spherical shell (named families) | β 0.5–3.0 (SL-1/SL-2) | All fail; family ceiling β≈0.03–0.04 | NEC to −5.4e-3 |
| Spherical free-form (Track P / S6) | β ∈ {1.1, 1.5, 2.0} | All fail (4,992 adversarial evals) | −1.0 floor, Type I 0.31–0.38 |
| Toroidal, s-only (X1/S1) | v 0.5–3.0, 30 ladder rows | All fail | NEC −2.4e-3…−4.6e-3, Type I ~0.47 |
| Toroidal, φ-dependent (X1 ext) | v ∈ {1.1, 1.5, 2.0} | All fail; base collapses already at v=0.02 | −1.0 floor, Type I ~0.46 |
| Background-assisted (X2/S2) | β 0.5–3.0 on Schwarzschild/(A)dS | All fail; background makes it worse (~8× at β≈1) | NEC −2.0e-2 |
| Expansion-assisted (Lens E/S3) | β 0.5–3.0, H to 5e-2 | All fail, within 10–30% of flat | as flat; recession ≠ transport |
| Free-form 3D blob (Track B) | not reached (β=0.1 target failed first on dense audit) | Excluded by premise collapse at β=0.1 | dense −1.2e-5…−1.9e-5 at β=0.1 |
| Conditions-first (N3/S7) | β ∈ {1.1, 1.5, 2.0} sweeps + 1.1 snapshot | All fail | −1.0 floor, Type I 0.43–0.72 |
| f(R) = R + αR² (MG-1) | 176 superluminal evals | Zero passes | best −4.69; monotone anti-alignment |
| f(Q) = Q + βQ² (MG-2) | superluminal rows in 60 evals | Zero passes | P7 signature |
| Non-minimal scalar (X4/S4) | β ∈ {1.1, 1.5} | Fail in BOTH frames | Jordan NEC −2.7e-3…−1.4e-2 |
| Einstein–Cartan (N2/S7) | β = 1.5 | Excluded by magnitude | needs 1.5×10³⁹ kg/m³ (21 orders > nuclear) |
| Kaluza–Klein (N1/S7) | β = 1.5 lift | 5D source violates own NEC | sampled NEC −4.4e-3…−1.4e-2 |
| Casimir threading (X5/S5) | β ∈ {1.1, 1.5, 2.0} deficits | Excluded by magnitude | needs L ≤ 2–6.6 m cycle; QI 65–585× |
| Ordinary mixtures (N4/S7) | β = 1.1 audit point | Excluded BY PROOF (NEC linearity) | 0/40 splits feasible |

---

## 4. What remains open (named, not hidden)

1. Background-TOV / comoving re-solved shells (X2 + Lens E
   reopening) — needs a new solver.
2. Toroidal conditions-first construction (X1 reopening).
3. N3 below-floor tail-honest rerun; boundary-layer prescription
   basis; meridional PDE inversion (N3 reopenings).
4. Coupled scalar-tensor solve (X4 reopening); KK stabilisation
   sector / RS lift (N1 reopening); non-minimal torsion coupling
   (N2 reopening).
5. Track B at a resolution whose seed reproduces the spherical
   wall, with velocity pinned (Track B reopening).
6. Outside-expert re-run of the finalists — only on Rakshit's
   separate explicit go (sequencing lock).

*End of report. Ground record: CHECKPOINT.md (this report is a
summary of it; where they differ, CHECKPOINT.md governs).*
