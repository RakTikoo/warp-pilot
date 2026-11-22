# Gate-5 — Worker W-E report: Claim G5-8 (Phase 17 formation paths)

**Claim source:** `phase17/CHECKPOINT17.md` §P17-2/§P17-3; memos
`phase17/results/p172_memo.md`, `p173_memo.md`.
**Scope (as tasked):** the Phase-17 MORPH/RAMP claims only. Phase 16's
dynamics claims are NOT re-gated here (Gate-4 already did them).
**Hedges intact throughout:** every result below is **Class B —
prescribed geometry, read-off matter; a legal instant path is
NECESSARY, NOT SUFFICIENT, for formation.** Nothing was uploaded;
no external contact was made.
**Code:** `gate5/we_g5_8.py` (fresh), run with
`~/workspace/warp-pilot/venv/bin/python`; outputs
`gate5/results/we_control.json`, `we_m1_T200.json`, `we_m1_T40.json`,
`we_shiftonly.json`, `we_ramps.json`, `we_ceiling.json`.
float64 everywhere.

---

## 1. Method — the independent second path

Fresh code written from the claim statement. **No phase deciding
machinery was imported or re-run** (`p74_auditor.py`,
`p161_dynamic.py`, `p172_morph.py`, `p173_ramp.py` were read for the
registered definitions only; their stored JSONs were opened only in
the final comparison, never by the audit code). Deliberate
differences from the original machinery:

- **Finite differences: 2nd-order central stencils** (offsets ±1) for
  ∂g and ∂Γ, in time and space. The original auditor is 4th-order.
  Accuracy is therefore established by my own h-scan, not inherited.
- **Morph λ-interpolation: local 4-point Lagrange in λ** over the 17
  slice nodes. The original used a global cubic spline in λ.
- **Einstein tensor, Eulerian tetrad, Hawking–Ellis margins:** my own
  vectorised implementation (Gate-4 V1 pattern, re-derived here),
  including my own sampled-observer fallback at non-Type-I points.
- **Imported as shared DEFINITIONS only** (Gate-4 precedent):
  `shell.py` — the frozen Finalist-A prescription (`build_shell`
  profiles: R1=10, R2=20, M=2.0, edgepeaked wd=3.0/floor=0.2,
  s_rho=2.0, s_P=1.16, Nr=4001) and the cos shift window S(r) on
  [10,20]. Sampling: 26 Fibonacci directions × radii 8–22 (step 0.5)
  + cavity 2,4,6 = 832 points; core = max|T̂| > 1e-5 — the claim's
  own sampling definition.

**Grid and convergence (read this before the numbers).** My
2nd-order scheme's stationary control converges onto the claimed
Finalist-A headline from above:

| h | my static β=0.02 core worst | Type I |
|---|---|---|
| 0.30 | +1.21161e-5 | 1.0 |
| 0.15 | +1.19908e-5 | 1.0 |
| 0.075 | +1.19598e-5 | 1.0 |
| claimed (4th-order, h=0.3) | +1.19492e-5 | 1.0 |

So my h=0.3 margins sit ~1.4% above the original's, shrinking to
~0.1% at h=0.075. Signs, sites, Type-I fractions and the
frozen-vs-dynamic splits — the deciding content — are unaffected.
Minkowski smoke test: max|T̂| = 0.0 exactly. β=0 static wall control:
mine +1.21214e-5 (h=0.3) / +1.19959e-5 (h=0.15), converging toward
the claimed +1.19544e-5 / +1.19546e-5 — legal in both paths, so the
ramp question is well-posed in mine too.

**Mindful of Gate-4's erratum history:** Gate-4 found the Phase-16
frozen figure +1.53e-05 to be an h=0.3-only read that changes at
finer h. The same failure mode appears once in this claim — at the
β=0.025 ceiling point, §2(d) below — and it is reported there in
full, with h = 0.30/0.15/0.075 reads from my auditor.

---

## 2. Correctness — my deciding numbers, per sub-claim

### (a) Legal morph path — M1 (grow wall and shift together)

**T=200 — PATH LEGAL, reproduced.** All 13 instants audited
dynamically at h=0.3: instants k=0,1,2 are core-less (young shell
below the 1e-5 scale, as in the original); every cored instant has
core worst > 0 and Type I = 1.0.

- Worst instant: **t=50, λ=0.15625** — the same instant as claimed.
  My dynamic core worst **+7.503e-6** (SEC) at h=0.3,
  **+7.525e-6** at h=0.15. Claimed: +7.532e-6 at both.
  Agreement within 0.4%.
- Frozen twin at that instant: mine +8.297e-6 (h=0.3), +8.325e-6
  (h=0.15); claimed +8.334e-6. Frozen spot checks at k=4, 6, 12 all
  legal; frozen minimum over my spots +8.297e-6 (claimed path
  minimum +8.334e-6).
- Endpoint (λ=1) dynamic: mine +1.21127e-5 vs frozen +1.21161e-5 —
  the endpoint is quiet at T=200 in my run too.

**T=40 — RATE BARRIER, reproduced.** Frozen slices pass; the
dynamic audit fails on the morph's own ∂_t terms.

- **First failing instant: k=1, t=3.333, λ\* = 0.0197** (β=3.94e-4) —
  identical λ\* to the claim. My dynamic core: **NEC −1.2528e-5**
  (claimed −1.252e-5), WEC −1.1699e-4 (claimed −1.169e-4),
  SEC −1.2860e-4 (claimed −1.286e-4), **DEC −1.0000000014,
  Type I fraction 0.0, worst site r=21.5** — every figure matches
  the claim's, the DEC value and the site to all quoted digits.
  h=0.15 confirmation: DEC −1.0000000014, Type I 0.0.
- **Frozen twin at λ\* is core-less in my run too** — the dynamic
  terms alone create the core and immediately make it illegal.
  This is the frozen-vs-dynamic split that makes the barrier a
  *rate* barrier, and it reproduces exactly.
- Worst instant k=6 (t=20, λ=0.5): mine DEC −1.0000000021,
  Type I 0.732 — claimed −1.0000000021, Type I 0.732. Frozen there:
  mine +1.01496e-5 (claimed +1.005e-5).
- Endpoint k=12 passes dynamically: mine +2.990e-6 (claimed
  +2.912e-6), Type I 1.0 — the failure is mid-morph, not an
  endpoint effect, in both paths.
- One honest discrepancy, non-deciding: at k=2 (t=6.67) my core
  mask is empty (dynamic scale sits just under 1e-5 at the sampled
  points) while my all-points margins there are already negative
  (worst −1.0000000014, Type I 0.29 over all 832 points). The
  original counted 10 of 13 instants failing on the core mask; the
  count at this one threshold-marginal instant is
  discretisation-sensitive. The barrier verdict does not rest on
  it: the first failure, the worst instant, and the endpoint all
  reproduce.

**Verdict (a): REPRODUCED.**

### (b) Shift-first impossibility — pure varying shift on flat space

Frozen β-scan of the shift-only geometry (a ≡ b ≡ 0, cos window,
my auditor):

| β | core | NEC min | DEC min | Type I | worst site |
|---|---|---|---|---|---|
| 0.005 | none (scale ≤ 1e-5) | — | — | — | — |
| 0.0074 | none | — | — | — | — |
| **0.01** | **6 points** | **−2.046e-5** | **−1.0000000011** | **0.0** | **r=11.0** |
| 0.015 | 137 points | −3.083e-5 | −1.0000000024 | 0.0 | r=11.0 |
| 0.02 | 227 points | −4.130e-5 | −1.0000000043 | 0.0 | r=11.0 |

Claimed at β=0.01: NEC −2.126e-5, DEC −1.0000000012, Type I 0.0,
site r≈10.5–11, core appearing between β=0.0074 and 0.01. **Every
element reproduces**, including the core-less interval below 0.01
and the inner-window-edge site. h=0.15 at β=0.01 confirms
(NEC −2.050e-5, DEC −1.0000000011, Type I 0.0). The *dynamic* M3
stage-1 audit at its β=0.01 instant (t=T/4) is essentially the
frozen read, as claimed: T=200 dyn DEC −1.0000000011,
NEC −2.045e-5; T=40 dyn DEC −1.0000000014 — dynamic ≈ frozen to
~1e-7/5e-8, so this is a configuration-space barrier, not a rate
effect. Since the frozen slices are illegal from β=0.01 and the
shift-only stress scale grows ~β², no shift-only path exists at
any rate: slowing down cannot help a path whose *slices* fail.

**Verdict (b): REPRODUCED.**

### (c) Ramps 0 → 0.02 legal at all rates; ∂_t tax linear in β̇, tiny

Segment-1 midpoints (max-|β̇| instants, β=0.01) audited dynamically
at all three rates, plus extra T=40 instants (t=10, 30) and the
hold instant:

- Dynamic core worst at midpoints: T=400 +1.21143e-5,
  T=200 +1.21085e-5, T=40 +1.20620e-5 — all legal, Type I 1.0.
  Extra T=40 instants legal (+1.20777e-5, +1.20742e-5). Hold
  instant (β̇=0): dynamic = static = +1.21161e-5 exactly, as it
  must. **Segment 1 legal at all tested rates — reproduced**
  (the claim's own worst-instant values, +1.19464e-5 / +1.19413e-5
  / +1.18959e-5, are the same statement read with the 4th-order
  auditor; cf. my convergence table, §1).
- **Segment-1 DEC tax** (frozen − dynamic, core worst per EC):

| T | β̇_max | claimed tax_DEC | my tax_DEC |
|---|---|---|---|
| 400 | 7.50e-5 | 5.72e-9 | 5.802e-9 |
| 200 | 1.50e-4 | 1.14e-8 | 1.160e-8 |
| 40 | 7.50e-4 | 5.72e-8 | 5.802e-8 |

  My regression: **slope 7.735e-5, intercept 7.2e-13 (≈0),
  R² = 0.99999999993** — claimed slope 7.63e-5, R² = 1.000.
  Taxes agree within 1.5%; slope within 1.4%. **Segment-1 NEC tax
  identically 0.0 at all three rates in my run too**, exactly as
  claimed.
- Segment-2 midpoints (β=0.035, inside the frozen-illegal zone):
  dynamic ≈ frozen at every rate (core worst ≈ −1.986e-4 both) —
  segment 2 fails *frozen*, not dynamically, in my run too.
  Segment-2 taxes are exactly linear in my run (R² = 1.000 to the
  same precision), and tiny (largest: SEC tax 1.849e-6 at T=40).
  **One quantitative caveat, stated plainly:** my segment-2 tax
  *magnitudes* run ~1.7–2.2× the claim's (NEC tax at T=40: mine
  1.911e-7 vs claimed 8.72e-8; NEC slope mine 1.698e-4 vs claimed
  7.75e-5; SEC tax at T=40: mine 1.849e-6 vs claimed 1.06e-6). At
  β=0.035 the core-minimum points sit on near-zero frozen margins,
  so the tax — a difference of two nearly equal numbers at a
  marginal site — is the most discretisation-sensitive number in
  the item. The claim as stated ("exactly linear in β̇ and tiny")
  reproduces; the segment-2 slope's second digit does not.

**Verdict (c): REPRODUCED** (with the segment-2 slope caveat above
recorded; it does not touch the stated claim, whose deciding
segment is segment 1).

### (d) Destination ceiling β\* ≈ 0.025 — my own static scan

Frozen Finalist-A audits, my auditor, β bracketing:

| β | my core worst h=0.3 | my core worst h=0.15 | Type I | worst site/EC |
|---|---|---|---|---|
| 0.0200 | +1.21161e-5 | — | 1.0 | r=8.5, DEC |
| 0.0225 | +1.21148e-5 | — | 1.0 | r=8.5, DEC |
| **0.0250** | **+1.21132e-5** | **+1.19879e-5** (h=0.075: +1.19569e-5) | **1.0** | r=8.5, DEC |
| **0.0275** | **−2.5458e-5** | **−2.5296e-5** | 0.987 | **r=10.5, SEC** |
| 0.0300 | −8.2843e-5 | — | 0.973 | r=10.5, SEC |
| 0.0500 | −5.5312e-4 (SEC) | — | 0.678 | r=10.5, SEC |

The **bracket reproduces**: β=0.025 legal, β=0.0275 unambiguously
illegal at both resolutions, failure at the inner wall edge
r=10.5 driven by SEC — the claimed site and EC. My β=0.0275
magnitude (−2.53e-5 at h=0.15) matches the claim's h=0.15 read
(−2.516e-5); my β=0.03 (−8.284e-5) matches the claim's h=0.15 read
(−8.273e-5); segment 2's first failure on the ramp grid and its
frozen character are consistent with this bracket.

**But the claim's marginal-point anatomy at β=0.025 does NOT
reproduce.** The original reports β=0.025 core worst = +6.41e-10
at h=0.3 (DEC at r=10.5, Type I 0.999) — a point sitting exactly
on zero. In my auditor β=0.025 is **comfortably legal at every
grid spacing** (+1.211e-5 / +1.199e-5 / +1.196e-5 at
h = 0.30/0.15/0.075, Type I 1.0, worst at r=8.5): there is no
near-zero point anywhere on my core at β=0.025. Conversely the
original's h=0.3 magnitudes just above the ceiling (−5.54e-5 at
0.0275, −1.158e-4 at 0.03) are ~2× more negative than both my
reads and the original's own h=0.15 reads. This is the Gate-4
erratum pattern exactly: **the r=10.5 inner-edge margins in the
original's h=0.3 stencil are resolution-fragile**; the robust
content, confirmed by two auditors at two resolutions, is the
bracket and the failure anatomy above the ceiling, not a
zero-crossing at 0.025 itself. The ceiling statement therefore
survives only in bracket form.

**Verdict (d): REPRODUCED WITH RESTATEMENT.** Exact restated
wording:

> "For the Finalist-A family at fixed M = 2.0, the legal
> destination ceiling β\* lies in the bracket (0.025, 0.0275]:
> β = 0.025 is the last fully legal destination (core worst
> ≈ +1.20e-5, Type I 1.0, confirmed at h = 0.30/0.15/0.075 in an
> independent second-path audit), and β = 0.0275 is the first
> unambiguously illegal destination (core worst ≈ −2.5e-5, SEC,
> at the inner wall edge r = 10.5, at both h = 0.3 and h = 0.15
> in both auditors). The Phase-17 figure +6.41e-10 for the frozen
> core worst at β = 0.025 is an h = 0.3 read of the original
> auditor only and is resolution-dependent; it must not be quoted
> as the onset value. Destinations above the bracket are
> statically illegal, so no path question arises for them."

### Overall correctness verdict

- (a) REPRODUCED · (b) REPRODUCED · (c) REPRODUCED ·
  (d) REPRODUCED WITH RESTATEMENT (above).
- **G5-8 overall: REPRODUCED WITH RESTATEMENT** — the restatement
  is confined to sub-claim (d)'s marginal-point figure. The
  deciding items — the T=200 all-legal morph, the T=40 rate
  barrier at λ\*=0.0197 with its frozen/dynamic split, the
  β=0.01 shift-only illegality, the linear tiny ∂_t tax, and the
  ceiling bracket — all reproduce in a fully independent
  second path, several of them to all quoted digits.

---

## 3. Novelty

### 3.1 Verbatim query log (all run 2026-11-21, this worker)

Sources checked per query: arXiv, INSPIRE-HEP-indexed records and
Semantic Scholar-indexed records as surfaced by web search, plus
general web. Full texts/abstracts read for the decisive neighbours
(Natário; Finazzi–Liberati–Barceló; Santiago–Schuster–Visser;
Fuchs et al.; Everett–Roman; Clough–Dietrich–Khan).

1. `Alcubierre warp drive formation how to create bubble turn-on dynamics`
2. `warp drive bubble formation problem cannot be created Alcubierre`
3. `"warp drive" formation initial data constraints build from flat space numerical relativity`
4. `Finazzi Liberati Barcelo dynamical warp drives semiclassical instability formation`
5. `Alcubierre metric energy density shift vector gradient negative energy formula Eulerian density`
6. `"warp drive" accelerating bubble ramp velocity time dependent energy conditions audit instants`
7. `Santiago Schuster Visser generic warp drive energy conditions Natario class theorem 2105.03079`
8. `Fuchs warp drive shell positive energy maximum velocity subluminal limit 2405.02709`

### 3.2 Near neighbours (cited)

- **Natário, arXiv:gr-qc/0110086** (Class. Quantum Grav. 19 (2002)
  1157): the general warp class with an arbitrary *time-dependent*
  shift vector field on flat slices; proves such spacetimes always
  violate some energy condition, with the Eulerian density a
  (negative-semidefinite) shear/vorticity functional of the shift.
- **Santiago, Schuster & Visser, arXiv:2105.03079** (Phys. Rev. D
  105 (2022) 064038): generic Natário-class drives (unit lapse,
  flat slices) violate WEC/SEC/DEC, and NEC under subsidiary
  conditions, at any speed.
- **Finazzi, Liberati & Barceló, arXiv:0904.0141** (Phys. Rev. D
  79 (2009) 124017) + Barceló, Finazzi & Liberati,
  arXiv:1001.4960: the one true *formation* analysis in print — a
  warp drive "created out of an initially flat spacetime" and
  accelerated to *superluminal* speed — but the object computed is
  the semiclassical RSET backreaction (exponential growth at the
  front wall), not a classical per-instant EC audit of the
  formation path; subluminal creation is explicitly untouched by
  the instability.
- **Everett & Roman, arXiv:gr-qc/9702049**: the causal-separation
  observation — an occupant can neither create nor control a
  superluminal bubble on demand (horizon argument; superluminal
  scope only).
- **Clough, Dietrich & Khan, arXiv:2406.02466**: numerical-relativity
  *evolution* of an already-formed Alcubierre bubble (collapse /
  containment failure, gravitational-wave signatures) — dynamics of
  a finished bubble, not a formation path from flat space.
- **Fuchs et al., arXiv:2405.02709** (Class. Quantum Grav. 41
  (2024) 095013): the constant-velocity positive-energy shell this
  family descends from; static, single β=0.02 anchor, no formation,
  ramp, ordering or ceiling analysis.
- **Alcubierre, arXiv:gr-qc/9409004**: the original metric; the
  Eulerian density of a pure shift geometry,
  ρ ∝ −v²(f′)²-type terms, is negative wherever the shaping
  function varies — the seed of sub-claim (b) is already visible
  here in formula form.
- Self-published/non-refereed "warp bubble formation" frameworks
  (e.g. Zenodo simulation specifications) were found and graded
  non-evidence in both directions, following Gate-4 practice.

### 3.3 Per-sub-claim novelty

- **(a) Existence of a legal morph path (Class B): NOVEL
  (delimited).** No published work audits a prescribed formation
  path — flat space → finished shell — instant by instant for
  full all-observer EC legality, for any shell family. The
  formation literature is Finazzi et al.'s semiclassical
  superluminal analysis and NR evolution of pre-formed bubbles;
  neither asks whether the intermediate *classical* configurations
  of a growing conditions-first shell are legal, and neither finds
  a legal path. The rate-barrier half of (a) (same path legal
  slowly, illegal at 5× rate, purely dynamically, with the
  frozen/dynamic split as the instrument) likewise has no
  published counterpart found.
- **(b) Shift-first impossibility: PARTIALLY KNOWN.** The
  qualitative core — a spatially varying shift on flat slices,
  with no wall matter, carries exotic read-off stress-energy — is
  a direct corollary of published results: it is the Alcubierre
  geometry itself, whose Eulerian density formula has been in
  print since 1994, inside Natário's class (gr-qc/0110086), for
  which generic EC violation is theorem (arXiv:2105.03079). What
  is NOT in print and is this programme's: the quantitative onset
  for this window and sampling (core appears between β=0.0074 and
  0.01; NEC −2.1e-5, Type I 0.0 at β=0.01), and the *ordering*
  conclusion drawn from it for a conditions-first shell — that in
  a formation sequence the wall's matter must be present before /
  as the shift is installed, because the shift's curvature is
  exactly what the wall pays for. Any upload must credit the
  Natário/SSV theorems and claim only the onset number and the
  ordering corollary for this family.
- **(c) Ramp legality + linear ∂_t tax: NOVEL (delimited).** No
  published per-instant EC audit of a subluminal β(t) ramp of a
  positive-energy shell, and no published measurement of a dynamic
  tax linear in β̇, was found. (Finazzi et al. accelerate a bubble,
  but to superluminal speeds and for RSET purposes.) The novel
  content is family- and regime-specific: segment 0→0.02 legal at
  T ∈ {40, 200, 400}, tax slope ≈ 7.6–7.7e-5 per unit β̇
  (segment-1 DEC), NEC tax identically zero on segment 1.
- **(d) Destination ceiling β\* ≈ 0.025: NOVEL (delimited,
  family-specific).** Fuchs et al. publish the shell at β=0.02
  only; no published velocity ceiling for the Fuchs/Finalist-A
  family was found. The number is a property of this one family at
  fixed M=2.0 and must be quoted only as such (and only in the
  restated bracket form of §2(d)).

### 3.4 Novelty verdict (overall)

**PARTIALLY KNOWN** — sub-claim (b)'s qualitative statement is
published theorem (Natário gr-qc/0110086; Santiago–Schuster–Visser
arXiv:2105.03079; the pure-shift density formula is Alcubierre
1994); sub-claims (a), (c) and (d) are **NOVEL** in the delimited
senses above. The one quotable delimitation sentence:

> "New here are: an instant-by-instant full-energy-condition audit
> exhibiting a legal prescribed formation path (Class B,
> necessary-not-sufficient) from flat space to a positive-energy
> warp shell, with a measured rate barrier on the same path; the
> measured ∂_t tax of subluminal ramps, exactly linear in β̇; the
> destination ceiling of the Finalist-A family, β\* ∈ (0.025,
> 0.0275]; and, for the shift-first ordering, the quantitative
> onset (illegal from β = 0.01) and its ordering corollary — the
> qualitative exoticity of a bare varying shift itself is
> published (Alcubierre 1994; Natário 2002; Santiago–Schuster–
> Visser 2022) and is not claimed."

Wording hazards (binding for any upload): never "first dynamic
warp drive" (Finazzi et al. own dynamical creation, semiclassically);
never present (b) as a new impossibility theorem — it is a measured
onset inside a class already known to be exotic; the Class B label
(necessary, not sufficient) rides on every formation statement;
β\* is quoted only as the bracket, only for this family at M=2.0.

---

## 4. Gate verdict for G5-8

**UPLOAD-READY AFTER RESTATEMENT** — correctness REPRODUCED on
(a), (b), (c) and REPRODUCED WITH RESTATEMENT on (d) (restated
wording in §2(d)); novelty PARTIALLY KNOWN overall with (a), (c),
(d) NOVEL as delimited and (b) PARTIALLY KNOWN. The upload must
carry: the §2(d) restated ceiling wording; the §3.4 delimitation
sentence with its credits (Alcubierre gr-qc/9409004; Natário
gr-qc/0110086; Santiago–Schuster–Visser arXiv:2105.03079; Finazzi
et al. arXiv:0904.0141 as the dynamical-formation neighbour); the
Class B headline on every formation statement; and the segment-2
tax-slope caveat of §2(c) if segment-2 slopes are quoted.

**Erratum owed to the Phase 17 record (for the coordinator to log,
not silently absorb):** the P17-3 onset line "β=0.025 core worst
+6.41e-10 at h=0.3 (identical value to Phase 16's β-scan)" is an
h=0.3-resolution read of one auditor at the r=10.5 site class; an
independent auditor at h = 0.30/0.15/0.075 finds β=0.025
comfortably legal (+1.196e-5 converged). The ceiling conclusion
(β\* ≈ 0.025–0.0275, first unambiguous failure at 0.0275) stands;
the marginal-point figure does not, and Phase 16's β-scan value at
0.025 inherits the same fragility note Gate-4 already attached to
its frozen reads at this site class.
