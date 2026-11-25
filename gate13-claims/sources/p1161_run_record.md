# P116-1 — RUN RECORD (FU-P962-1, the β = 0.0725 bisection)

**Item:** P116-1, Phase 116. **Category: PAYLOAD TRANSPORT only.**
Standing verified mark in this category: **0.0799c** (Phase 46,
Gate-8 restated scope). Phase-verified rows: 0.08745c (Phase 80)
and 0.09556c (Phase 88, corroborated at a second span in
Phase 96; NOT gated — Gate-11 is the parent's line, not awaited).
The bare-shell mark (Procaccia 0.1363, Gate-7) is a different
category and is not compared against anywhere in this item.
**Python:** ~/workspace/warp-pilot/venv/bin/python, float64
everywhere. INTERNAL only; nothing uploaded; nobody contacted.
CHECKPOINT116.md not edited. phase96/, phase88/, phase80/
read-only throughout; machinery lineage COPIED into
phase116/work/ with prefix p1161_ (p1161_lib.py, p1161_common.py,
p1161_control.py, p1161_alone.py, p1161_compose.py,
p1161_verify.py — sed-renamed copies of the p962 lineage, with
result paths repointed to phase116/results/).

## 1. REGISTRATION RESTATED (from CHECKPOINT116.md §P116-1, fixed)

- **Construction (fixed, inherited):** Phase 80's
  source-modulated composition with the Phase 88/96 span
  variable; 14-number design vectors, chain, TOV backgrounds,
  lapse re-equilibration with held orthonormal shifts,
  economics-before-legality discipline — unchanged.
- **Control (fixed, before any Phase-116 number):** reproduce
  on this phase's machinery, from stored design vectors, the
  Phase-96 alone cells β = 0.07 (PASS) and β = 0.075 (FAIL:
  Type-I 0.772, sampled NEC −9.91×10⁻⁵) at ±0.10W, and the
  0.09556 composed row's stored audit pattern (regional
  margins +3.84×10⁻⁶ / +1.190×10⁻³ / +3.35×10⁻⁵ / +1.11×10⁻⁶
  class; cavity decided by the Gate-8 settlement ladder as
  re-derived in Phase 96's control; reference
  phase96/results/p962_control.json). A control failure voids
  the item's numbers until repaired.
- **Registered cells (fixed):** the outer shell ALONE at
  β = 0.0725 × spans {±0.10W, ±0.075W}: full gate-standard
  audit (Type-I + sampled-null + margins, full volume) at
  every cell, fringe anatomy read separately (wall vs
  transition/fringe radii), exactly as Phase 96, PLUS the
  q-read (see §2, stated before computing).
  Alone design vectors for the new β are produced by the
  Phase-88/96 polish unchanged (clone-algebra core objective,
  explicit FD Jacobian step 2×10⁻³, L-BFGS-B maxiter 100 /
  maxfun 3000, Phase-96 bounds), by continuation in β from
  the stored β = 0.07 vector of the same span (Phase 96's
  own continuation pattern for non-stored cells).
- **Economics before legality (fixed):** IF β = 0.0725 is
  alone-legal at either span, the held-W payload sum of the
  composed (inner 0.06, outer 0.0725) row at that span is
  computed and frozen to a results file BEFORE any composed
  legality read; the composed row is then audited under the
  full gate-standard audit over both shells AND the cavity
  (cavity under the Gate-8 settlement standard as re-derived
  in the control), with an independent second path (two
  discretisations different in kind) if it passes. If
  β = 0.0725 is alone-legal at NEITHER span, no composed row
  is run and the reason is stated.
- **Verdict forms (fixed):** CEILING TIGHTENED TO
  (0.07, 0.0725) / CEILING TIGHTENED TO (0.0725, 0.075) /
  PARTIAL forms with the open cell named — exactly as
  registered in CHECKPOINT116.md §P116-1.
- **Bars:** margins alone never decide — the gate standard is
  Type-I + sampled-null + margins, with alone legality under
  the standing Phase-88 criterion as translated verbatim in
  p1161_common.alone_legal (copied from p962_common). No bar
  is loosened; any amendment would be appended here, dated,
  marked post-hoc.

## 2. THE q-READ — STATED BEFORE COMPUTING ANY NEW CELL

The checkpoint registers "the flux q diagnostic as carried by
the Phase 88/96 audit lineage — its definition quoted verbatim
from the lineage in the run record BEFORE computing; if the
lineage audit carries no q channel, that fact and the named
substitute read are stated in the run record before computing".

**Finding (verified by inspection of the lineage before any
Phase-116 number was computed): the Phase 88/96 audit lineage
carries NO q channel.** The gate-standard auditor
(wa_auditor.audit, used unchanged by p962_lib.summarise_gs and
hence by every Phase 88/96 audit) returns exactly: the
Hawking–Ellis eigenvalue margins (nec/wec/sec/dec), the Type-I
classification, and `sampled_nec`. The stored Phase-88 and
Phase-96 audit blocks contain no other channel (key inventory
checked on p882_alone.json and p962_alone.json). The letter
"q" appears in the lineage only as (i) the design-vector
exponent in the chain source, quoted verbatim from
p962_lib.py's chain():

    g0 = (rhohat ** q) * tanh((r_m-r)/0.05) * exp(sum_i a_i B_i(r))

— a construction parameter (x[12] of the 14-number vector),
not an audit read — and (ii) in the polish bounds ("q within
[x0−0.5, x0+0.5] ∩ (0.5, 3.0)"). There is no flux-q audit
diagnostic to quote.

**Named substitute read (never silent):** the q-read for every
new cell in this item is the lineage's only null-flux read —
the **sampled-null NEC**, defined verbatim in wa_auditor.py as
"Min over Fibonacci null directions of That_ab k^a k^b,
k=(1,n)" (sampled_nec_min, n_dir=162) — reported per cell as
`min_sampled_nec_all_sig` over all significant points and per
fringe region as `min_sampled_nec_all`, i.e. exactly the
sampled-null leg of the gate standard, broken out per region
as the q-read. In addition, as flux anatomy of the chain
itself, each cell's chain block (λ, k, S_lo−1, S_hi, balance,
monotonicity) is reported — the chain is the lineage's
source→flux→shift object (p962_lib chain docstring:
"Source->flux->shift chain for one shell profile"). The
design-vector exponent q (x[12]) of each polished 0.0725
vector is also stated in the memo for completeness. No other
quantity is called a q-read in this item.

## 3. PER-STAGE RECORD

### 3.2 ALONE CELLS β = 0.0725 (p1161_alone.py, 1808 s total)

Polish: continuation in β from the stored Phase-96 β = 0.07
vector of the same span; clone-algebra core objective,
Phase-96 settings unchanged. Polish scores: +1.555×10⁻⁴
(±0.10W, nfev 56, 931 s) and +1.559×10⁻⁴ (±0.075W, nfev 63,
862 s) — the β = 0.07 class (+1.56×10⁻⁴).

**±0.10W — ALONE-LEGAL (standing criterion, p1161_common).**
h = 0.15: Type-I 1.000, sampled NEC (q-read substitute, all
significant points) −2.17×10⁻⁷ — the fixed exterior floor
read, identical to the β = 0.07/0.075 cells (Phase-96 memo ‡:
−5.01×10⁻⁷ worst DEC in the exterior, flipping positive at
h = 0.075: here worst +5.31×10⁻⁷, sampled NEC +6.01×10⁻⁷ at
h = 0.075). Fringe anatomy at h = 0.15 (Type-I / worst /
q-read per region): interior 1.000 / +7.64×10⁻⁷ / +6.50×10⁻⁷;
fringe_lo 1.000 / +1.55×10⁻⁴ / +1.06×10⁻⁴; wall 1.000 /
+1.40×10⁻⁴ / +3.24×10⁻⁵; fringe_hi 1.000 / +1.68×10⁻⁵ /
+2.04×10⁻⁶; exterior 1.000 / −5.01×10⁻⁷ / −2.17×10⁻⁷ (floor
class only). At h = 0.3 the fringe_hi/exterior read
Type-I 0.981/0.886 with worst −1.52×10⁻⁵ — the criterion's
h-convergence clause carries the cell (h = 0.075 combined
fringe_hi+exterior worst > 0), exactly the β = 0.07 pattern.
Chain: λ 0.95902, k 0.17709, S_lo−1 −4.335×10⁻³,
S_hi +9.433×10⁻³, balance 2.1×10⁻¹⁶, monotonicity exact.
Design vector exponent q (x[12]) = 1.12729, r_m = 8.93917.

**±0.075W — ALONE-ILLEGAL.** The failure is confined to
fringe_hi: at h = 0.15 fringe_hi Type-I 0.904, q-read
(sampled NEC) −8.86×10⁻⁶, eigenvalue worst +9.11×10⁻⁶
(positive — the failure is the non-Type-I patch, not a
margin); at h = 0.075 fringe_hi Type-I 0.865, q-read
−1.02×10⁻⁵ — the patch does NOT converge away with h, so
the criterion's convergence clause fails. Every other
region is clean at every h (interior 1.000 / +7.72×10⁻⁷;
fringe_lo 1.000 / +2.35×10⁻⁴; wall 1.000 / +1.40×10⁻⁴;
exterior floor class only). Overall h = 0.15: Type-I
0.99445, sampled NEC −8.86×10⁻⁶. Chain: λ 0.91676,
k 0.17946, S_lo−1 −6.132×10⁻³, S_hi +1.321×10⁻², balance
5.5×10⁻¹⁷, monotonicity exact. q (x[12]) = 1.13427,
r_m = 8.93437.

**Anatomy vs β = 0.075 (Failure Protocol read):** at
β = 0.075 the failure lived in interior-classified points
(Type-I 0.43) AND fringe_hi/exterior (0.54/0.41) with
sampled NEC −9.91×10⁻⁵ (±0.10W). At β = 0.0725 the interior
component is GONE at both spans (interior Type-I 1.000,
worst +7.6×10⁻⁷ class) and the sampled-NEC depth has
shrunk by an order of magnitude (−8.9×10⁻⁶ at ±0.075W,
floor-only at ±0.10W). The split is NOT saturated at the
0.075 pattern: the interior failure switches off between
0.075 and 0.0725, and what remains at the tighter span is
a fringe_hi non-Type-I patch only. At ±0.10W nothing
remains beyond the settled exterior floor.

**Consequence (registered):** β = 0.0725 IS alone-legal at
±0.10W, so the composed (inner 0.06, outer 0.0725) row at
±0.10W is run: economics frozen BEFORE any composed
legality read (§3.3), then the full composed audit.

### 3.3 ECONOMICS FREEZE (before any composed legality read)

Frozen by p1161_compose.py to p1161_economics.json:
e0.10_o0.0725_i0.06 held-W payload **0.09758c** (exact value
in the frozen file), e0.10_o0.0725_i0.05 = 0.09118c; the
±0.075W rows carry the same payloads with
alone_legal_outer = False and are never audited as composed
rows. NOTE (environment incident, recorded plainly): the
first two compose launches were killed by an environment
write failure (Errno 1, Operation not permitted, on file
writes from interpreter processes, beginning ~10:07 UTC —
see §4 D2); the first launch died DURING the economics
dump, leaving a 0-byte file, and NO composed legality read
had occurred at that point (the script performs no legality
read above the freeze, and the audit stage had not been
reached — the successful foreground re-run re-froze the
economics from scratch before auditing, and the freeze
timestamp in the final composed file is that re-freeze).
The economics-before-legality order is therefore intact:
every composed legality read in this item postdates a
completed freeze of the same numbers.

### 3.4 COMPOSED ROWS + SECOND PATH (machine-written files)

The final stored economics and composed files were produced
by the original p1161_compose.py run end-to-end (58 s) once
the environment write window reopened (§4 D2): economics
frozen_at_unix = 1795432892.0549617, carried identically
into p1161_composed.json; design vectors in the economics
file are BIT-EXACT against p1161_alone.json (outer) and the
Phase-80 economics file (inner) — checker-verified.

Composed rows audited (descending held payload; both shells
alone-legal only — the ±0.075W rows were frozen with
alone_legal_outer = False and never audited):

- **e0.10_o0.0725_i0.06 — payload 0.0975831574914493c —
  LEGAL.** h = 0.15: Type-I 1.000, sampled NEC (all
  significant points) +1.126×10⁻⁶; regional worsts: payload
  +3.836×10⁻⁶, inner wall +1.191×10⁻³, outer wall
  +3.394×10⁻⁵, exterior +1.107×10⁻⁶; cavity raw worst
  −1.131×10⁻⁴ (DEC, r ≈ 4.527) decided by the Gate-8
  settlement ladder (stencil-clear −1.541×10⁻⁴ →
  +9.484×10⁻⁵ → +1.631×10⁻⁴; focused −1.856×10⁻⁴ →
  +1.239×10⁻⁶ → +1.437×10⁻⁵; Type-I 1.000 on every rung);
  conservation rel. median 0.0117. row_legal (standing
  criterion, checker-recomputed) = True.
- **e0.10_o0.0725_i0.05 — payload 0.09118184734247374c —
  LEGAL** (same pattern; conservation rel. median 0.0146).

**Independent second path on the deciding row**
(p1161_verify.py, source econ96 — the Phase-88/96 pattern:
two discretisations different in kind, same point set,
h = 0.15): wa_diag 4th-order worst −2.588×10⁻⁶, Type-I
1.000; Phase-1 judge worst −3.242×10⁻⁶, Type-I 1.000 — the
settled cavity floor class, the same site class as the
0.09556 row's own second path (−2.20×10⁻⁶ / −2.84×10⁻⁶ in
Phase 96; −2.10×10⁻⁶ / −2.75×10⁻⁶ for the ±0.075W
corroborating row). Every other region positive on both
paths (stored in p1161_verify_e0.10_o0.0725_i0.06.json).

**Checker:** p1161_check.py recomputes every deciding
number from the stored JSONs: **22/22 PASS**
(p1161_check.json).

## 4. DEVIATIONS

- D1 (machinery adaptation, pre-registered in §1): the
  copied p1161_alone.py runs only β = 0.0725, seeded by
  continuation in β from the stored Phase-96 β = 0.07
  vector of the same span (Phase 96's own continuation
  pattern); the copied p1161_control.py gains a part (c)
  reproducing the two alone control cells from Phase-96
  stored vectors, as the checkpoint's control requires.
  No machinery numerics were changed.
- D2 (ENVIRONMENT INCIDENT, 2026-11-23 ~10:07–11:21 UTC):
  file writes from interpreter processes (Python, Perl;
  also Node as a Python descendant) began failing with
  Errno 1 (Operation not permitted), leaving 0-byte files;
  shell/coreutils writes and the tool-side write path were
  unaffected, and other Phase-116 items show the same
  signature (e.g. a 0-byte p1165_solve.json at 10:46). Two
  compose launches died this way — the first DURING the
  economics dump (0-byte file), before any composed
  legality read existed; no number was produced by those
  launches. Interim stdout-capture drivers
  (p1161_econ_stdout.py, p1161_compose_stdout.py,
  p1161_verify_stdout.py) were built to keep working, and
  the economics values were captured from stdout; HOWEVER
  the hand-transcribed economics/composed files produced
  from those captures were found by an exactness check to
  drift in last-ulp digits of the design vectors and were
  DISCARDED, not used. Once writes recovered, the original
  p1161_compose.py was re-run end-to-end and produced the
  final stored p1161_economics.json / p1161_composed.json
  (vectors bit-exact vs the alone and Phase-80 files,
  checker-verified). The economics-before-legality order
  holds for the final record: the freeze timestamp in the
  composed file is the completed freeze of the same run,
  and the script performs no legality read above the
  freeze. The interim §3.3 note above describes the first
  (stdout) freeze; the final freeze superseded it before
  any composed legality read was stored.
- D3: no stage approached the ~2 h continuous-run flag
  (longest: the alone ladder, 1808 s total). Nothing was
  shortened; nothing needs the Kaggle queue from this item.
- No other deviations. Bars, spans, β, and verdict forms
  are exactly those registered in CHECKPOINT116.md
  §P116-1; no post-hoc amendments were needed.

## 3.1 CONTROL — PASS (landed before any new cell; p1161_control.py)

- (a) 0.0799 cosine cavity, Gate-8 settlement standard:
  wa_diag 4th-order stencil-clear cavity DEC
  +1.623×10⁻⁴ / +2.010×10⁻⁴ / +1.977×10⁻⁴
  (h = 0.15 / 0.075 / 0.0375), Type-I 1.000 at every rung —
  the ≥ +9.98×10⁻⁵ settlement class reproduced exactly;
  Minkowski max|G| = 0.0.
- (b) Phase-88 0.09556 row from stored vectors: payload
  0.0955573262914437c exactly; regional worsts at h = 0.15:
  payload +3.840×10⁻⁶, inner wall +1.190×10⁻³, outer wall
  +3.351×10⁻⁵, exterior +1.107×10⁻⁶ (registered classes);
  Type-I 1.000; cavity by the settlement ladder
  (stencil-clear −1.527×10⁻⁴ → +9.50×10⁻⁵ → +1.631×10⁻⁴;
  focused −1.843×10⁻⁴ → +1.45×10⁻⁶ → +1.38×10⁻⁵).
- (c) Alone cells at ±0.10W from Phase-96 stored vectors
  (p1161_control part_c, added to the copied control script):
  β = 0.07 alone-legal TRUE (Type-I 1.000, sampled NEC
  −2.17×10⁻⁷ — the fixed exterior floor read, cf. Phase-96
  memo ‡); β = 0.075 alone-legal FALSE with Type-I 0.772 and
  sampled NEC −9.91×10⁻⁵ at h = 0.15 — the registered FAIL
  reproduced. Fringe anatomy at β = 0.075 matches the stored
  Phase-96 pattern (interior Type-I 0.43, fringe_hi 0.54,
  wall and fringe_lo clean).

**Control verdict: PASS on all clauses. The new cells below
stand on this control.**
