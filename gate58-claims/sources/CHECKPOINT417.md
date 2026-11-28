# CHECKPOINT — PHASE 417: THE DENSE READ

**Charge:** ledger entry 1090 (2026-11-27). Gate-53's rider
G53-R2 found, on a denser radial sampling, that A-6 (graded best
β = 0.193359375) dips to SEC −1.257×10⁻⁶ at r ≈ 5.42 *between*
the registered shells — legal on the registered radial set, not
in the radial continuum — and that E2-1 also dips while RW-5 and
y_his stay positive. This phase is the charged measurement of
that finding across the whole graded lineage: a READ, not a
search. It restates each standing ceiling's SCOPE. It does not
re-open any ceiling's registered-set verdict (those stand as
gate-verified under their registered instruments).

**Holders** (each at its standing ceiling β, vector hash-verified
before any read): y_his at 0.1363 (the category's reference
member, c = 0); S1 at 0.18671875 (Phase 386's holder, Gate-42);
E2-1 at 0.191796875 (Phase 391, Gate-44); RW-5 at 0.192578125
(Phase 392, Gate-51); B-2 at 0.192578125 (Phase 408 Arm B seed of
record — "RW-5 embedded, box-clipped at c13" per G53-R3 — as the
embedding control); A-6 at 0.193359375 (Phase 408, Gate-53).

## §1 Machinery

Phase 417's own machinery, `phase417/work/p417_lib.py` — imports
nothing from phase386/391/392/408/work or gate53/work; tensor
instruments are the registered pair (gate6/wa_auditor.py,
phase50/p503_lib.audit4). The construction is the shared class
definition (CHECKPOINT386 §2: ρ = ρ0·Box4_W[φ·1_[R1,R2]],
φ = exp(ΣcⱼBⱼ); GenProcaccia background/source chain;
y = (c[n_c], a[12], q, r_m)). The numerical organisation is a
third one, distinct from both predecessors:

- **Stages 2–4** ("panel-Lagrange"): uniform construction grid
  (dr = 2.5×10⁻⁵, no knot insertions); each stage's antiderivative
  is the cumulative sum of panel-exact integrals of the cubic
  Lagrange interpolant through the four nearest grid values;
  shifted-point evaluation by 6-point Lagrange interpolation of
  the antiderivative's grid values.
- **Stage 1**: φ·1_[R1,R2] is discontinuous at R1/R2 and no
  stencil may straddle the jumps; its antiderivative is built on
  the inside grid [R1, R2] alone by per-panel 8-point
  Gauss–Legendre quadrature of the exact φ (B-spline basis at the
  GL nodes), with F1 clipping its argument to [R1, R2].
- Downstream (builder grid, m, a, source chain, metric factory):
  the GenProcaccia conventions, as the shared class definition.

Deciding reads on the VM (frame of record). The laptop was run
as an admission control (§5) and is ADMITTED as corroboration.
float64 everywhere.

## §2 Calibration and the stage-1 incident (disclosed)

Chain reads (M, ρ_max, λ, k) for all six holders against the
stored gate values (Gate-53's chain reads; Gate-42/Phase 386 for
S1): **max relative diff 8.9×10⁻¹¹** (λ of y_his; all others
≤ 8.2×10⁻¹¹, M at ≤ 2.4×10⁻¹⁴) — the lineage's inter-scheme
class (Gate-53's two schemes agreed at ~10⁻¹¹). Record:
`results/p417_calibration.json`.

INCIDENT, on the record: the first draft of this machinery
applied the panel scheme to φ·1_[R1,R2] on the uniform grid;
stencil panels straddling the R1/R2 jumps produced an O(h)
error — chain reads off by up to 7.4×10⁻⁶ relative in λ
(`results/p417_calibration_draft1_superseded.json`). The
calibration caught it before any audit was run; stage 1 was
rebuilt as in §1 and the calibration re-run clean. No audit
read was ever taken on the draft machinery.

## §3 Control — registered-set reads reproduced

Full registered-set audits (wa + audit4, both registered
spacings, pts_1020_control) on Phase 417 machinery, against each
holder's gate-stored deciding values: **every deciding margin
reproduces at abs diff ≤ 1.8×10⁻¹³** (worst-margin abs diffs:
y_his 1.7×10⁻¹⁴, S1 1.5×10⁻¹⁴, E2-1 2.1×10⁻¹⁴, RW-5 2.3×10⁻¹⁴,
B-2 6.6×10⁻¹⁴, A-6 6.3×10⁻¹⁴ at h = 0.0375; ≤ 1.8×10⁻¹³ at
h = 0.01875), and all six holders read legal_full = True on this
machinery — the registered-set verdicts stand reproduced, as
charged. Record: `results/p417_controls.json`. No dense figure
was believed before this control passed.

## §4 The dense read — method

Identical geometry to Gate-53's densification, for comparability:
radii 2.6–10.6 step 0.05 × the registered 26 directions, wa at
h = 0.009375. All dense minima are over SIGNIFICANT points (the
registered definition: max|That| > thr, thr = max(1e-9·(10/R1)²,
1e-3·ρ_peak)) — the same filtered minima Gate-53's R2 reported.
Then, per holder: radial refinement at step 0.01 over ±0.12
around the significant SEC argmin radius (same directions, same
h, same thr), and a binding-shell ladder at the refined worst
point (wa at h ∈ {0.0375, 0.01875, 0.009375, 0.0046875}, audit4
at both registered spacings, Richardson pairs on SEC).

INCIDENT, on the record: the first dense run's classification
took RAW unfiltered minima; for the three positive holders the
raw argmin is a cavity-fringe point at r = 2.75 with SEC ≈
−10⁻¹³ (FD noise where the stress itself is ~10⁻¹³, a
non-significant point). The run's own significance-filtered
blocks (summarise all_sig) matched Gate-53's dense values
exactly, exposing the flaw; the run is preserved as
`results/p417_dense_run1_unfiltered.json` and the read was
re-run with significance filtering throughout (v2, the record
of record, `results/p417_dense.json`). No classification in
this checkpoint comes from the v1 run.

Cross-check against Gate-53's dense reads (step 0.05,
significant): y_his SEC +5.4489344×10⁻⁸ vs Gate-53 +5.4489101×10⁻⁸
(Δ 2.4×10⁻¹⁴); E2-1 −1.1619581×10⁻⁶ vs −1.1619568×10⁻⁶
(Δ 1.3×10⁻¹²); RW-5 +2.9750367×10⁻⁷ vs +2.9750321×10⁻⁷
(Δ 4.6×10⁻¹⁴); B-2 −8.6109134×10⁻⁷ vs −8.6108950×10⁻⁷
(Δ 1.8×10⁻¹²); A-6 −1.2528729×10⁻⁶ vs Gate-53's radial profile
−1.2528729×10⁻⁶ at h = 0.009375. Floor proxies agree to 3–4
digits throughout. S1 has no Gate-53 dense read — this phase is
its first.

## §5 Laptop admission

The laptop pool ran Phase 417's builder + the wa instrument
(job: chain reads for all six holders; registered-set wa audits
at h = 0.0375 for A-6 and E2-1; point reads at all six VM dense
worst points at h = 0.009375 and 0.0375). Comparison
(`results/p417_laptop_out.json`, `results/p417_laptop_compare.json`):
chain reads bit-identical (diffs 0.0; one 3.5×10⁻¹⁸); worst-point
reads agree to ≤ 5.4×10⁻¹⁵; registered audits agree in the same
class. **Max deciding abs diff 5.4×10⁻¹⁵, far inside the 1×10⁻⁹
admission bar: the laptop is ADMITTED as corroboration for the
deciding reads.** All deciding reads remain the VM's. (Staging
note: p503_lib's `shell` dependency is the warp-pilot root
shell.py; it was added to the staged set after the first launch
failed on the import — disclosed, no read affected.)

## §6 Results — the scope table

Registered margin = the gate-stored worst margin at h = 0.0375.
Dense figures are significant-point minima; "refined" is the
step-0.01 binding-shell read; the Richardson column is the
h → 0 limit of the SEC read at the refined worst point (wa
ladder), with audit4 concurring at every point (agreement
≤ 7.5×10⁻¹²; see the memo). SEC is the binding channel for
every holder; NEC/WEC/DEC dense minima are positive for all
six (full per-EC record in `results/p417_dense.json`).

| holder | β | registered margin | dense SEC (refined) | Richardson SEC | class |
|---|---|---|---|---|---|
| y_his | 0.1363 | +3.404×10⁻⁷ @ 5.0 | **+5.449×10⁻⁸** @ 4.0 | +5.448×10⁻⁸ | CONTINUUM-LEGAL |
| S1 | 0.18671875 | +3.971×10⁻⁷ @ 3.75 | **+2.529×10⁻⁷** @ 3.62 | +2.529×10⁻⁷ | CONTINUUM-LEGAL |
| E2-1 | 0.191796875 | +7.075×10⁻⁸ @ 6.0 | **−1.174×10⁻⁶** @ 9.96 | −1.175×10⁻⁶ | REGISTERED-SET — **FRAGILE** (dip 16.6× margin) |
| RW-5 | 0.192578125 | +6.056×10⁻⁷ @ 3.75 | **+2.856×10⁻⁷** @ 3.54 | +2.855×10⁻⁷ | CONTINUUM-LEGAL |
| B-2 | 0.192578125 | +6.042×10⁻⁷ @ 3.75 | **−8.611×10⁻⁷** @ 9.95 | −8.615×10⁻⁷ | REGISTERED-SET — THIN-BUT-SCOPED (dip 1.43× margin) |
| A-6 | 0.193359375 | +3.613×10⁻⁸ @ 5.0 | **−1.257×10⁻⁶** @ 5.42 | −1.259×10⁻⁶ | REGISTERED-SET — **FRAGILE** (dip 34.8× margin) |

Reading of the table:

1. **Densification costs every holder margin.** The continuum
   margin is 16% (y_his), 64% (S1), 47% (RW-5) of the registered
   margin for the holders that stay legal. The registered set
   systematically flatters the lineage's margins, not only its
   two thinnest holders.
2. **The sign flips exactly where R2 pointed, plus the
   embedding twin.** E2-1 and A-6 (the two thinnest registered
   margins) dip at 16.6× and 34.8× their registered margins —
   FRAGILE. B-2 dips at 1.43× — THIN-BUT-SCOPED.
3. **B-2 vs RW-5 is the sharpest single fact in the table:**
   the same registered ceiling (0.192578125), the same
   registered bracket, registered margins within 0.22% — and
   opposite continuum classes. The least-squares embedding +
   c13 clip is lossless ON THE REGISTERED SET (Gate-53 §3) and
   is NOT lossless in the continuum: the entire difference
   between the two vectors lives between the shells at
   r ≈ 9.95. Any future use of the embedding control inherits
   this scope.
4. **Dip anatomy.** All three dips are SEC-only: at each dip
   point NEC = WEC = DEC are strongly positive (A-6:
   +6.25×10⁻⁶; E2-1 and B-2: +8.5×10⁻⁵ at their sites), the
   points are Type-I, and the sites sit genuinely between
   registered shells (5.42 in the 5.0–6.0 gap; 9.95/9.96
   between 9.75 and 10.25). The positive holders' dense minima
   sit in the inner ramp (r = 3.54–4.0).
5. **The category's continuum ceiling, as restated:** the
   highest standing β whose holder is CONTINUUM-LEGAL is
   RW-5's 0.192578125 (dense margin +2.86×10⁻⁷). A-6's
   0.193359375 remains the registered-set best (Gate-53's set,
   rider G53-R2). The two statements are both true, each in
   its stated sense; neither may be quoted in the other's.

## §7 Verdict

**THE LINEAGE RESTATED.** Per-holder scope: y_his, S1 and RW-5
are CONTINUUM-LEGAL at their standing ceilings (dense margins
+5.45×10⁻⁸, +2.53×10⁻⁷, +2.86×10⁻⁷); E2-1, B-2 and A-6 are
REGISTERED-SET at theirs (dips −1.174×10⁻⁶ @ 9.96,
−8.611×10⁻⁷ @ 9.95, −1.257×10⁻⁶ @ 5.42), with E2-1 and A-6
flagged FRAGILE and B-2 THIN-BUT-SCOPED. Phase 416's in-flight
searches screen on the registered set; its eventual gate
referral inherits this scope table — a 416 raise will be a
registered-set statement until its own dense read is taken.

**Fences.** Graded-category wording only: nothing here contests
the step-profile category (Procaccia's 0.1363 stands there; the
programme's verified best there remains 0.10). This phase
restates scope; it does not re-open any registered-set verdict.
The FRAGILE flag is a scope statement about the registered
instrument's resolution, not a claim that the holders' designs
fail any bar they were ever judged under.

DESK: NO DATA CONTACT.

**Records:** `phase417/results/` — p417_calibration.json
(+ draft1 superseded), p417_controls.json, p417_dense.json
(+ run1 unfiltered, superseded), p417_laptop_out.json,
p417_laptop_compare.json; machinery `phase417/work/`
(p417_lib.py, p417_calib.py, p417_controls.py, p417_dense.py,
p417_laptop.py, p417_laptop_job.json). Memo:
`phase417/results/p417_memo.md`.
