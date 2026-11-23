# Novelty & Verification Gate 7 — GATE7.md (ground record)

**Status:** COMPLETE (pre-registered 2026-11-22 before any
Gate-7 run; all three workers returned; all three claims
verdicted — verdicts and closing synthesis at the end of this
file). No Gate-7 number existed when the bars below were
written. **Amended 2026-11-22 ~05:13 PT** under the parent
Uniqueness Protocol (see the Amendment section before the
Verdicts): novelty wordings for all three claims brought
into compliance; no correctness verdict changed.
**Work dir:** `~/workspace/warp-pilot/gate7/` — verifier code,
search logs and memos in this dir and `results/`.
**Parent records:** `../gate6/GATE6.md` (method — this gate
follows Gates 5/6 exactly), `../phase50/CHECKPOINT50.md`
(in full), `../phase50/results/p501_memo.md`,
`../phase50/results/p502_memo.md`,
`../phase50/results/p503_memo.md`,
`../phase50/results/p504_closure.md` (sources).
**This gate prepares verdicts only. It uploads NOTHING,
contacts no one, and edits no phase record.** Errata owed are
listed, not executed.

## The ruling this gate implements

Rakshit (2026-11-21 22:21 PT): "Verify everything and tell
honestly what you found." Scope: the three claims below —
Phase 50's two β = 0.10 rows (halved smoothing; spline shift)
and the strengthening of Phase 50's P50-1 audit verdict on
Procaccia's β = 0.1363 claim. Until this gate closes, both
β = 0.10 rows remain **"scan signal under attack"** in the
programme's locked language, and P50-1's verdict remains
CONFIRMED WEAKER.

## Standards (identical to Gates 1–6)

float64 everywhere. Hedges intact. A NOVEL verdict requires
the search to be DOCUMENTED (queries verbatim + sources
checked), never asserted. Verdict categories per axis:
- Novelty: **NOVEL** / **PARTIALLY KNOWN** (exact known part
  cited) / **KNOWN** (cited — claim dies as "ours").
- Correctness: **REPRODUCED** (independent second path, within
  the margins/tolerances registered below) / **REPRODUCED
  WITH RESTATEMENT** (survives only weakened — exact restated
  wording supplied) / **NOT REPRODUCED** (second path
  disagrees — full anatomy required).
GATE VERDICT per claim: **UPLOAD-READY** /
**UPLOAD-READY AFTER RESTATEMENT** (restated form supplied) /
**NOT YET** / **DEAD AS OURS** (KNOWN or NOT REPRODUCED).
For G7-3 the claim under audit is Procaccia's, not ours; the
gate verdict there grades OUR audit product (the independent
confirmation and its exact scope) — see its section.

## Protocol (pre-registered, per claim, BEFORE any gate run)

NOVELTY: systematic arXiv + INSPIRE-HEP + Semantic Scholar +
general web search for the claim's exact statement and near
neighbours; every query logged verbatim with the sources
actually checked and the date; near neighbours cited by arXiv
ID / DOI / stable URL; the novel part (if any) delimited in
one quotable sentence. **Coverage gaps are stated as plainly
as Gate-6's G6-1 gap was** (e.g. if INSPIRE or Semantic
Scholar is reachable only via arXiv-linked indexes or not at
all, the report says so in those words). A search that could
not be run is a gap, not a negative result.

CORRECTNESS: independent second path — reimplement the
deciding computation FROM THE CLAIM STATEMENT (fresh code in
`gate7/`, not a re-run of a phase script; shared *definitions*
— stored profiles, knot vectors, the design vector whose
audit is the claim — may be imported, the deciding machinery
may not). Reproduction = same signs and values within the
tolerances registered per claim below. Where a claim is an
audit of a published paper, the verifier re-derives from the
PAPER's printed formulas, not from the phase's transcription
(G7-3's registered exception: its reconstruction fidelity was
itself a registered, passed check of P50-1 and is re-gated by
hash + spot values below before any number is read).

C12 ACCOUNTING (every claim): every row here is a
prescribed-geometry audit — the audited source is the stress
tensor the metric's Einstein tensor requires; conservation is
automatic (Bianchi). No matter model, formation route, or
stability is claimed for any row. Le (arXiv:2605.25417)'s
stricter source-consistency standard is a standing caveat,
not a bar, and must be cited in any upload wording.

OPTIMISATION DIRECTIVE + RIDER (standing): sweeps/audits run
as unattended scripts; pass/fail computed by checker scripts
over result files; offloading never trades quality, speed or
breadth. No conflict is anticipated: all verification runs as
fresh local scripts at the phases' own resolutions or finer.

## The three claims (exact statements as tasked)

- **G7-1 (P50-2)** The halved-smoothing row: the Gate-6
  champion otherwise unchanged — (R₁,R₂) = (10,30), ADM mass
  M = 8.0 geom = 1.0773×10²⁸ kg, compactness M/R₁ = 0.80,
  edge-peaked density (wd = 6.0, floor = 0.2), TOV pressure,
  cosine shift on [10,30] — with Gaussian smoothing halved to
  (s_ρ, s_P) = (2.0, 1.16). Claimed FULLY LEGAL (Phase-50
  common bars) at **β = 0.10** (primary) and **β = 0.09**
  (companion): Type-I fraction 1.000 on the 1,404-point fine
  set at h = 0.3/0.15, whole-volume worst margin
  **+1.47×10⁻⁷ at β = 0.10** (= 36× the measured FD floor
  4.1×10⁻⁹; h = 0.3 read +1.474×10⁻⁷, h = 0.15 read
  +2.175×10⁻⁷), core sampled-null NEC min +1.75×10⁻⁶
  (β = 0.10) / +6.64×10⁻⁶ (β = 0.09), one second path
  (4th-order direct-∂²; its single discordant h = 0.3 point
  anatomised by the phase as a coarse-stencil artefact, both
  discretisations converging to DEC +3.28×10⁻⁶ at the point
  by h = 0.15). Record: `../phase50/CHECKPOINT50.md` §P50-2,
  `../phase50/results/p502_memo.md` §§4–5,
  `../phase50/results/p502_verify10.json`,
  `../phase50/results/p502_verify10b.json`.
- **G7-2 (P50-3)** The spline-shift row: (10,30), M = 8.0,
  compactness 0.80, edge-peaked (wd = 6.0, floor = 0.2),
  Gaussian smoothing (4.0, 2.32) — the champion's FULL
  smoothing — TOV pressure, and a monotone C² cubic-spline
  shift (K = 5 interior knots, clamped end slopes) with knot
  values [1, 0.9457, 0.7729, 0.5141, 0.2572, 0.0689, 0] at
  r = [10, 13.33, 16.67, 20, 23.33, 26.67, 30] (exact values
  in `../phase50/results/p503_pol_B_b0.10_K5.json`,
  `z_final` / `spline_diag`). Claimed FULLY LEGAL at
  **β = 0.10**: Type-I 1.000 at h = 0.3/0.15, whole-volume
  worst **+2.58×10⁻⁷** (SEC, exterior tail r = 37.0; 16.6×
  the FD floor 1.56×10⁻⁸), core worst **+1.570×10⁻⁵**, core
  sampled-null NEC min +2.02×10⁻⁶, second path (4th-order)
  agreeing on every deciding sign. Corroborating sub-claim: a
  second, independent K = 5 finalist (the β = 0.1363-polished
  spline; exact values in
  `../phase50/results/p503_pol_B_b0.1363_K5.json`) is also
  fully legal at β = 0.10. Record:
  `../phase50/CHECKPOINT50.md` §P50-3,
  `../phase50/results/p503_memo.md` §§5–6,
  `../phase50/results/p503_ledger.json`.
- **G7-3 (P50-1 strengthening)** Procaccia's claim: a
  Fuchs-form shell — (R₁,R₂) = (10,20) nominal, M = 6.0
  nominal (continuum mass of the §2 density
  M = 6.1128857), step density box-smoothed (4× box
  convolution, W = 3.6328174 m), ZERO radial pressure,
  spline-modulated shift source (12 cubic B-spline
  coefficients; tanh switch w = 0.05 m at r_m ≈ 16.80 m) —
  satisfies NEC/WEC/SEC/DEC at every β ∈ [0, 0.1363], with a
  proven NEC+DEC violation at β = 0.1364 (his interval value
  at the deciding point (r = 16.635 m, θ = 90°):
  −1.30135×10⁻⁷). P50-1 returned CONFIRMED WEAKER solely
  because the phase's pre-registered spacings (h = 0.3/0.15)
  are coarser than the 0.05 m switch; its registered
  strengthening condition is a verdict-path audit at
  h ≤ 0.0375 (or an analytic-tensor auditor) passing
  Phase-50 Bars 1–4. Record: `../phase50/CHECKPOINT50.md`
  §P50-1, `../phase50/results/p501_memo.md`, archives in
  `../phase50/procaccia/`.

## Registered correctness paths and bars

### G7-1 / G7-2 — the fresh path (both claims)

The Phase-50 verdicts rest on two Cartesian finite-difference
discretisations (2nd-order direct-∂², the Gate-6
`wa_auditor.py` pattern; 4th-order direct-∂², the `wa_diag.py`
pattern), and Phase-26's original verdicts on the Phase-1
nested-Γ judge. **The Gate-7 path must be different in kind
from ALL of these: a symbolic radial-reduction auditor.**
Concretely, the worker:
1. Derives the Einstein tensor of the registered metric form
   (radial functions a(r), b(r); shift β·S(r) along x;
   spatial part δ_ij + (e^{2b}−1) n_i n_j) symbolically
   (e.g. SymPy) in terms of a, b, S and their first/second
   radial derivatives and the direction cosines n_i — fresh
   derivation in `gate7/`, from the metric form, not copied
   from any phase or gate script;
2. Evaluates it on the claim's point set using ANALYTIC
   derivatives of the profile representations (the cubic
   splines of a(r), b(r) built by the shared definition
   `shell.py`; the cosine / cubic-spline S(r) differentiated
   in closed form) — no Cartesian finite-difference stencil
   anywhere in the deciding path;
3. Computes Hawking–Ellis margins, Type-I classification and
   the sampled-null NEC cross-check (≥ 162 Fibonacci
   directions) from the resulting Eulerian tensor with fresh
   code (shared *conventions* — significance threshold
   max(1e-9·(10/R₁)², 1e-3·|ρ_peak|) — may be reused; the
   margin machinery is re-derived or independently
   implemented and anchor-validated).

ANCHORS (must pass BEFORE any claim number is read; a failed
anchor stops the item as a machinery failure):
(i) Minkowski: the symbolic tensor is identically zero;
(ii) β = 0: the path's eigenvalues reproduce `shell.py`'s
exact 1-D spherical T (ρ, p_r, p_t) on sample radii in the
bulk with ρ relative error ≲ 3×10⁻³ and principal-pressure
absolute error ≲ 3×10⁻⁷ (the Gate-6 anchor scale);
(iii) the Gate-6 champion at β = 0.08 (full smoothing,
cosine): the path reproduces its legality (Type-I 1.000,
all margins > 0) on the fine set.

DECIDING SET: the Phase-50 fine set exactly (radii from
0.3R₁ step 1.0 to R₁−0.75, step 0.5 through R₂, step 2.0 to
1.35R₂, × 26 Fibonacci directions; 1,404 points for (10,30)).
ROBUSTNESS SET (reported separately; a violation here does
not by itself kill the claim but must appear in the restated
wording's scope): inner-edge radii 9.75–11.50 step 0.125 and
tail radii 32–40 step 0.5, × 52 Fibonacci directions.

REPRODUCTION BARS (registered): the claim is REPRODUCED iff
on the deciding set, at the claimed β:
(a) Type-I fraction = 1.000 over significant points;
(b) worst NEC, WEC, SEC and DEC margins all > 0;
(c) core sampled-null NEC min > 0;
(d) the whole-volume worst margin is ≥ 3× the gate path's
own measured numerical-error floor (floor = the larger of
the nonsignificant-point median |NEC| under the shared
significance convention and the path's anchor-residual
scale), AND agrees with the phase's claimed worst within a
factor 3 (the tail worst is a ~10⁻⁷ quantity set by spline
representation details; factor-3 is the registered band);
(e) core worst margin and core sampled-null NEC min agree
with the phase's claimed values within 50%.
Sign agreement with (b)/(c) but a miss on (d)/(e) =
REPRODUCED WITH RESTATEMENT (the gate's own numbers replace
the phase's in the restated wording). Any failure of
(a)/(b)/(c) = NOT REPRODUCED, with full anatomy (site,
binding condition, whether the phase's two FD paths share
the failure or the symbolic path stands alone, and a
tie-break read — e.g. a point ladder at the binding site on
a fourth discretisation — named and run before the verdict
is final).

### G7-3 — the strengthening path

HASH GATE (before ANY number is read): the design vector
`x_slp2.npy` as extracted in `../phase50/procaccia/` (copies
at `cont/continuum_cert_code/x_slp2.npy`,
`opt/optimal_shift_code/results/x_slp2.npy` and
`opt/optimal_shift_code/results/slp2.npy`) must have SHA-256
**a8814dfb6273956da9656379a8dd887218ecc28cbafb03fc87f980c07510d74a**.
Any mismatch stops the item: verdict NOT YET, gap = the
mismatch, no audit numbers read.
FIDELITY SPOT CHECK (before the audit): the reconstruction
used must reproduce, from the PAPER's §2/§3 printed values,
the continuum mass M = 6.11288573784887775 (to 1×10⁻⁹
relative), a(R_in), λ, k and ρ_max at the tolerances P50-1
achieved (≤ 3×10⁻⁸ relative). The reconstruction code may be
P50-1's (a shared definition whose fidelity is the check
being re-run); the AUDIT machinery may not be P50-1's
verdict path at its registered spacings — see below.
VERDICT PATH (registered, exactly the P50-1 strengthening
condition): a full verdict-path audit of the reconstructed
design at β = 0.1363 whose stencil resolves the switch —
**h-pair h = 0.0375 and h = 0.01875** on the P50-1 point set
(the (10,20) fine set + the support-edge / switch / fringe
clusters of `p501_audit.py`, 1,352 points), using the
Gate-6-standard auditor (`wa_auditor.py` pattern) — OR an
analytic-tensor auditor over the same set, worker's choice,
stated before running. SECOND PATH (Bar 4): a discretisation
different in kind from the verdict path (4th-order direct-∂²
if the verdict path is 2nd-order FD; the symbolic/analytic
tensor if the verdict path is FD) at h ≤ 0.0375-equivalent
resolution, agreeing on the sign of every deciding margin.
BARS (Phase-50 Bars 1–4 as written, for the verdict path's
spacings):
1. Type-I fraction = 1.000 at every significant audited
   point, at both spacings;
2. worst NEC/WEC/SEC/DEC margins > 0 at both spacings,
   sign-stable across the pair, worst ≥ 3× the measured FD
   floor at each spacing;
3. sampled-null NEC agrees in sign with the eigenvalue
   margins on the shell (min > 0);
4. second-path confirmation agrees on the sign of every
   deciding margin.
MACHINERY CROSS-CHECK (registered, from P50-1): at
β = 0.1364, at his exact point (0, 16.635, 0), a site ladder
(h ≤ 0.0375 down to ≤ 0.00234375, or the analytic tensor)
must find the tensor non-Type-I or its minimum null
contraction negative, with magnitude agreeing with his
interval value −1.30135×10⁻⁷ within 25%. If the cross-check
fails, a pass at 0.1363 is NOT credited until the discrepancy
is anatomised.
VERDICT TARGET: **CONFIRMED AT OUR BARS** (all four bars +
cross-check) or the residual gap named exactly (which bar,
at which spacing, at which site, by how much). Novelty axis
for this item = the audit's standing only: his claim is his;
our product is the independent confirmation and its exact
scope. The novelty worker therefore searches only for prior
INDEPENDENT audits / confirmations / refutations of
Procaccia's claim (and any refereed version of it), with the
same documented-query discipline.

## Worker assignments

- W-A: G7-1 (halved-smoothing row; β = 0.10 primary,
  β = 0.09 companion) → `results/wA_g7_1.md`; fresh code
  `gate7/wa_*.py`; numbers `results/wa_g71_numbers.json`.
- W-B: G7-2 (spline-shift row; champion finalist primary,
  second finalist as corroborating sub-claim) →
  `results/wB_g7_2.md`; fresh code `gate7/wb_*.py`;
  numbers `results/wb_g72_numbers.json`.
  (W-A and W-B may share the symbolic-reduction derivation
  ONLY if each independently validates it on the anchors;
  the derivation is machinery, and Gate-5/6 precedent allows
  one derivation to serve two claims when each worker
  re-validates it — but each worker's evaluation, margins
  and verdict must be their own run.)
- W-C: G7-3 (Procaccia strengthening) →
  `results/wC_g7_3.md`; fresh code `gate7/wc_*.py`;
  numbers `results/wc_g73_numbers.json`.

Each worker: correctness FIRST (fresh code in `gate7/`, run
with system python3 or the programme venv
`~/workspace/warp-pilot/venv/bin/python` — state which), then
novelty with logged queries. Each returns per claim:
correctness verdict + deciding numbers from THEIR run;
novelty verdict + citations + coverage gaps; and, wherever
the claim survives only weakened, the EXACT restated wording.
Workers do not edit this file; the coordinator integrates
verdicts from the worker reports + checker-verified result
JSONs.

## Amendment — UNIQUENESS PROTOCOL (parent amendment, dated 2026-11-22 ~05:13 PT, binding)

From Rakshit (2026-11-22 ~05:13 PT, after he pushed back on
inflated novelty wording): no claim in this gate may be
worded "unique", "first", "record" or "novel" outright
unless ALL of the following hold: (a) for speed claims, the
row beats the best VERIFIED mark in its EXACT category
(single-shell speed: Procaccia's 0.1363 is the standing
mark; payload-transport is a different category — no
cross-category "fastest" language); (b) independent
second-path reproduction inside this gate; (c) the novelty
search log is complete with queries verbatim AND coverage
gaps stated (the INSPIRE/Semantic-Scholar bounded gap must
be named, as in Gate-6/8); (d) the claim's category and
scope are stated in the wording itself. Otherwise the
wording is "not found in our search (limits: …)" or "scan
signal under attack".

**Application to this gate (coordinator, 2026-11-22):**
- **G7-1:** condition (a) is NOT met for any single-shell
  speed wording — β = 0.10 does not beat the standing
  verified mark (Procaccia's 0.1363, confirmed at G7-3).
  The claim's wording is therefore family-scoped only (the
  Fuchs-family TOV thick-shell ceiling), and its residue is
  worded "not found in our search" with the limits named in
  its verdict section. The PARTIALLY KNOWN category stands
  (it is not an outright-novelty wording); the phrase
  "novel part" in the verdict below is replaced by the
  protocol wording.
- **G7-2:** same application — the residue (transfer +
  attribution + specific configuration) is worded "not found
  in our search" with limits named; no speed-record wording
  (0.10 < 0.1363, different design in any case). PARTIALLY
  KNOWN stands as a category.
- **G7-3:** the outright NOVEL label on the audit's standing
  is WITHDRAWN under this protocol and replaced by: **not
  found in our search (limits: INSPIRE-HEP and Semantic
  Scholar checked only via general-web queries naming them,
  not their own search interfaces; arXiv checked by
  web-index search, not API listing)** — conditions (b) and
  (d) hold (second-path reproduction inside this gate;
  category and scope stated in the confirmation wording),
  but (c) is met only with the bounded gap named, so the
  protocol's fallback wording governs. The CONFIRMED AT OUR
  BARS correctness verdict is unaffected (it is a bars
  verdict, not a novelty wording), and the exact restated
  confirmation wording contains no "unique / first / record
  / novel" language.
- The two restated claim wordings (G7-1, G7-2 §4) were
  checked against this protocol: neither contains "unique",
  "first", "record" or "novel", both state their category
  and scope, and neither makes a cross-category speed claim.

## Verdicts

### G7-1 — Halved-smoothing row, β = 0.10 / 0.09 (W-A, 2026-11-22)

Full report: `results/wA_g7_1.md`; fresh code `wa_symbolic.py`,
`wa_eval.py`, `wa_run_g7.py`, `wa_anatomy.py`,
`wa_tiebreak.py`, `wa_check.py`; numbers
`results/wa_g71_numbers.json` (+ `wa_anatomy.json`,
`wa_tiebreak.json`, `wa_check.json`); search log
`wa_search_log.md`. System python3, float64. Path: SymPy
symbolic radial reduction (exact radial chain rule, closed-form
block inverse), analytic spline/cosine derivatives — no
Cartesian FD anywhere in the deciding path. All three anchors
passed before any claim number (Minkowski max|G| = 8.7×10⁻¹⁹;
β = 0 vs exact spherical T: ρ rel err 2.18×10⁻⁵, p abs err
1.39×10⁻⁹; Gate-6 champion at β = 0.08 legal, worst
+2.5926×10⁻⁷, matching Gate-6).

- **Correctness: REPRODUCED WITH RESTATEMENT (both β).** On
  the deciding set (1,404 pts) every registered bar (a)–(e)
  passes at both speeds (checker-recomputed): β = 0.10 —
  Type-I 1.000, whole-volume worst **+2.155×10⁻⁷** (DEC,
  r = 6.0 cavity; claimed +1.47×10⁻⁷, ratio 1.47, inside the
  factor-3 band; 155× the gate floor 1.39×10⁻⁹), core worst
  +3.276×10⁻⁶ (claimed +2.94×10⁻⁶), core sampled-null NEC
  +1.568×10⁻⁶ (claimed +1.75×10⁻⁶). β = 0.09 — Type-I 1.000,
  worst **+2.166×10⁻⁷**, core worst +7.923×10⁻⁶ (claimed
  +7.70×10⁻⁶), core sampled NEC +6.461×10⁻⁶ (claimed
  +6.64×10⁻⁶). The restatement is forced by the registered
  ROBUSTNESS set: a genuine thin **DEC-negative layer
  immediately inside R₁** that the fine set's radii (9.75,
  10.25) step over — at β = 0.10, DEC < 0 for
  10 < r ≲ 10.2, minimum **−1.33×10⁻⁵ at r ≈ 10.01**; at
  β = 0.09 only a ≤ 7.5×10⁻⁷ dip confined to r ≲ 10.02. Not
  a symbolic-path artefact: an FD read at the layer converges
  +9.5×10⁻⁶ → +6.3×10⁻⁶ → −1.1×10⁻⁶ as h shrinks, and at
  β = 0 the same ring matches `shell.py`'s exact spherical
  DEC (+6.18×10⁻⁶) — the layer is β-driven. "Fully legal"
  therefore survives as a fine-set statement, not at every
  radius in (10, 10.25).
- **Novelty: PARTIALLY KNOWN.** Known part: Fuchs et al.
  2024 (arXiv:2405.02709; CQG 41 095013, DOI
  10.1088/1361-6382/ad26aa) already tune smoothing
  coefficients iteratively until EC violations vanish, at a
  fixed design (β_warp = 0.02) — the premise that smoothing
  decides legality is theirs. Not found anywhere searched:
  any statement that *reducing* smoothing width *raises* the
  legal-β ceiling, or any smoothing-width scan in the
  Fuchs-family literature (Procaccia's box width is fixed;
  Le arXiv:2605.25417 scans thickness, not smoothing width).
  Part not found in our search, one sentence (worker's
  delimitation; limits in the coverage gaps below): "In the
  Fuchs-family TOV warp shell, the Gaussian smoothing width
  of the density/pressure profiles is a speed variable:
  halving it (s_ρ, s_P) = (4.0, 2.32) → (2.0, 1.16) raises
  the energy-condition-legal shift ceiling from β = 0.08 to
  β = 0.10, because narrower smoothing sharpens the
  inner-edge support against the shift gradient that
  otherwise opens a non-Type-I pocket there." Coverage gaps
  (stated plainly by the worker): INSPIRE-HEP and Semantic
  Scholar were reached only via general web search and
  arXiv-page index links, not their own search interfaces —
  records indexed only there could have been missed;
  Procaccia's companion optimisation paper was not retrieved
  in full text.
- **GATE VERDICT: UPLOAD-READY AFTER RESTATEMENT** — exact
  restated wording (required for any upload): "On the
  1,404-point fine audit set (radii 3–9 step 1.0, 9.25–30
  step 0.5, 31–39 step 2.0, × 26 Fibonacci directions), the
  (R₁,R₂) = (10,30) shell — ADM mass M = 8.0 geom
  (1.0773×10²⁸ kg), compactness M/R₁ = 0.80, edge-peaked
  density (wd = 6.0, floor = 0.2), TOV pressure, cosine shift
  on [10,30] — with Gaussian smoothing halved to (s_ρ, s_P) =
  (2.0, 1.16) satisfies NEC, WEC, SEC and DEC at every
  significant point with Hawking–Ellis Type-I fraction 1.000
  at β = 0.10 (whole-set worst margin +2.16×10⁻⁷) and at
  β = 0.09 (+2.17×10⁻⁷), verified by an independent symbolic
  radial-reduction auditor. This is a prescribed-geometry
  audit: the audited source is the stress tensor the metric's
  Einstein tensor requires, conservation is automatic
  (Bianchi), and no matter model, formation route or stability
  is claimed; Le's (arXiv:2605.25417) stricter
  source-consistency standard is a standing caveat, not a bar
  met here. Scope limit: a denser radial probe finds a
  DEC-negative layer immediately inside the inner edge at
  β = 0.10 (10 < r ≲ 10.2, minimum −1.3×10⁻⁵ at r ≈ 10.01),
  which the fine set's radii 9.75 and 10.25 step over; at
  β = 0.09 the same layer appears only as a dip of at most
  7.5×10⁻⁷ confined to r ≲ 10.02. "Fully legal" is therefore
  claimed on the audited fine set, not at every radius in
  (10, 10.25)."

### G7-2 — Spline-shift row, β = 0.10, both finalists (W-B, 2026-11-22)

Full report: `results/wB_g7_2.md`; fresh code `wb_symbolic.py`,
`wb_auditor.py`; numbers `results/wb_g72_numbers.json`;
search log `wb_search_log.md`. System python3, float64.
Path: W-B's OWN symbolic derivation (spherical coordinates,
ADM-form inverse verified g·g⁻¹ = I; W-A's derivation was not
used or read), analytic derivatives only. Spline
reconstruction from stored `z_final` is bit-exact against the
phase's `spline_diag` for both finalists (max diff 0.0). All
three anchors passed before any claim number (Minkowski: 0
nonzero symbolic entries; β = 0: ρ rel err 9.8×10⁻⁶, p abs
err 1.9×10⁻¹⁰; Gate-6 champion at β = 0.08 legal, worst
+2.593×10⁻⁷, core NEC at r = 10.25 = +1.767×10⁻⁵,
digit-identical to Gate-6's continuum value).

- **Correctness: REPRODUCED (primary finalist); REPRODUCED
  (second finalist, corroborating sub-claim).** Deciding set
  (1,404 pts), β = 0.10, bars (a)–(e) all pass for both:
  primary — Type-I 1.000, whole-volume worst **+2.593×10⁻⁷**
  (SEC, r = 37; claim +2.58×10⁻⁷, ratio 1.005; 10.2× the
  gate floor 2.55×10⁻⁸), core worst **+1.544×10⁻⁵** (claim
  +1.570×10⁻⁵), core sampled NEC **+1.80×10⁻⁶** (claim
  +2.02×10⁻⁶). Second finalist — Type-I 1.000, worst
  +2.593×10⁻⁷, core worst **+1.603×10⁻⁵** (claim
  +1.568×10⁻⁵), core sampled NEC **+2.45×10⁻⁶** (claim
  +2.66×10⁻⁶). Binding sites reproduce exactly (tail SEC at
  r = 37; core NEC r = 13.25 primary, DEC r = 10.25 second).
  Robustness set (reported separately, per registration):
  both finalists show far-tail SEC −1.53×10⁻⁸ at r = 39, at
  the path's representation-noise floor; the second finalist
  also shows isolated non-Type-I points on the denser
  inner-edge radii (core Type-I 0.9985 there). These scope
  facts are carried in the restated wording.
- **Novelty: PARTIALLY KNOWN.** Known part: "optimise the
  shift to buy legality" is Procaccia's (academia.edu, Oct
  30 2026, unrefereed — his object is a spline-modulated
  shift *source* on a (10,20) zero-radial-pressure shell),
  and variational shift-profile optimisation exists in the
  Natário class (Bolívar & Vasilev). Residue not found in
  our search, one sentence (worker's delimitation; limits
  in the coverage gaps below): "Ours is the transfer of
  shift-profile optimisation to the Fuchs TOV thick-shell
  family — specifically the finding, by controlled
  one-freedom-at-a-time attribution, that a spline reshaping
  of the shift profile itself is the only one of Procaccia's
  three freedoms that buys speed there (+0.02, β = 0.08 →
  0.10), together with the specific legal β = 0.10
  configuration that embodies it." Coverage gaps (stated
  plainly): the INSPIRE-HEP and Semantic Scholar interfaces
  were not reached directly (general web index only);
  Procaccia's companion optimisation paper full text not
  separately retrieved.
- **GATE VERDICT: UPLOAD-READY AFTER RESTATEMENT** — the
  claim is carried forward ONLY in the worker's exact
  wording (`results/wB_g7_2.md` §4), which states the
  configuration and both finalists' gate numbers (worst
  +2.59×10⁻⁷; core +1.54×10⁻⁵ / sampled +1.80×10⁻⁶ primary;
  core +1.60×10⁻⁵ / sampled +2.45×10⁻⁶ second), the
  robustness scope (far-tail SEC −1.5×10⁻⁸ at the noise
  floor at r = 39 for both finalists; second finalist's
  isolated off-set inner-edge non-Type-I points; legality
  claimed on the registered fine set), the C12
  prescribed-geometry accounting, and the Le
  (arXiv:2605.25417) caveat.

### G7-3 — Procaccia strengthening (W-C, 2026-11-22)

Full report: `results/wC_g7_3.md`; fresh code `wc_recon.py`,
`wc_auditor.py`, `wc_run.py`, `wc_crosscheck.py`,
`wc_check.py`; numbers `results/wc_g73_numbers.json`;
search log `results/wc_search_log.md`. Programme venv,
float64. Verdict path (stated before running): 2nd-order
direct-∂² FD at h = 0.0375 / 0.01875 on the P50-1 point set;
second path 4th-order direct-∂² at h = 0.0375. No Phase-50
or archive code was executed or imported; the reconstruction
re-implements the shared definition from text, using only
the hashed design-vector data file.

- **Hash gate: PASS** — all three copies of `x_slp2.npy`
  SHA-256 = a8814dfb…10d74a exactly, verified before any
  audit number was read.
- **Fidelity spot check: PASS** — M rel err 3.6×10⁻¹⁵
  (bar 1×10⁻⁹); a(R_in) 1.3×10⁻¹¹; λ 2.7×10⁻⁸; k 1.1×10⁻⁸;
  ∫F/r² 1.1×10⁻⁸; ρ_max 2.0×10⁻⁸ (all ≤ 3×10⁻⁸). Minkowski
  anchor exactly 0.
- **Verdict: CONFIRMED AT OUR BARS.** Bar 1 — Type-I
  fraction **1.000**, 0 non-Type-I among 988 significant
  points, at both spacings (and on the second path). Bar 2 —
  worst margin **+3.404×10⁻⁷** (SEC, r = 5.0) at h = 0.0375
  = **109.5×** the floor (3.11×10⁻⁹); **+3.398×10⁻⁷** at
  h = 0.01875 = **135.5×** the floor; sign-stable (0.2%
  change); matches P50-1's refined read (+3.404×10⁻⁷) to 4
  figures. Bar 3 — sampled-null NEC min **+8.999×10⁻⁸ /
  +8.945×10⁻⁸** > 0. Bar 4 — 4th-order path: Type-I 1.000,
  worst +3.396×10⁻⁷, every deciding sign agrees.
- **Machinery cross-check: PASS, after a required anatomy.**
  At (0, 16.635, 0), β = 0.1364, the tensor is non-Type-I
  at every h ≤ 0.01875. The first magnitude read
  (−3.4×10⁻⁸, 5,002-direction sample) failed the 25% band;
  anatomy showed the min-null contraction (minimiser
  n ≈ (1,0,0); the form varies on the |T| ~ 10⁻⁴ scale
  against a ~10⁻⁷ minimum) is under-resolved by ANY
  direction sampling — P50-1's −1.245×10⁻⁷ was itself a
  20,000-direction sample (W-C's identical sample reproduced
  it digit-for-digit, proving the tensors identical). Exact
  minimisation (sphere optimisation cross-validated by an
  independent Lagrange secular solve, agreeing to ~10⁻¹³):
  **−1.2938×10⁻⁷** at the finest h (0.58% from his
  −1.30135×10⁻⁷) and **−1.30122×10⁻⁷** on the 4th-order path
  (0.010%). At β = 0.1363 the exact min null at his point
  stays positive (+5.3×10⁻⁸).
- **Novelty (audit standing only): NOT FOUND IN OUR SEARCH
  (limits: INSPIRE-HEP and Semantic Scholar checked only via
  general-web queries naming them, not their own search
  interfaces; arXiv checked by web-index search, not API
  listing)** — the outright NOVEL wording is withdrawn
  under the Uniqueness Protocol amendment above. Documented
  search (arXiv + INSPIRE-HEP + Semantic Scholar + general
  web, queries logged verbatim) found no prior independent
  audit / confirmation / refutation of Procaccia's claim and
  no refereed or arXiv version of it — only his academia.edu
  posting and figshare DOIs 10.6084/m9.figshare.34866243.v1
  / 34895667.v1. Coverage gaps (stated plainly): INSPIRE-HEP
  and Semantic Scholar were checked only via general-web
  queries naming them, not their own search interfaces
  (partial checks, not negatives); arXiv was checked by
  web-index search, not API listing.
- **GATE VERDICT: UPLOAD-READY AFTER RESTATEMENT** — the
  confirmation may be uploaded ONLY in the worker's exact
  wording (`results/wC_g7_3.md`, final section), which
  credits Procaccia, states the unrefereed status and the
  verified design-vector hash, gives the gate's numbers
  (Type-I 1.000; worst +3.40×10⁻⁷, > 100× floor; cross-check
  −1.29×10⁻⁷ / −1.30×10⁻⁷ vs his −1.30135×10⁻⁷), and
  carries the prescribed-geometry C12 scope (no matter
  model, formation route, or stability) and the Le
  (arXiv:2605.25417) caveat. The claim and the design are
  Procaccia's; ours is only the independent confirmation
  and its stated scope.

## Closing synthesis (coordinator, 2026-11-22)

**The honest headline: both β = 0.10 rows are real, and one
of them is thinner than it looked; and Procaccia's 0.1363
claim is now confirmed at our bars, not just in substance.**
All three items survived a genuinely independent path — for
G7-1/G7-2 a symbolic auditor with no finite-difference
stencil anywhere in it, whose anchors reproduce Gate-6's own
numbers digit-for-digit where they overlap. The programme's
best GATE-verified subluminal configuration OF ITS OWN is
now β = 0.10, held by two different configurations (Gate-6's
best was 0.08) — category stated per the Uniqueness
Protocol: the standing verified single-shell speed mark
overall remains Procaccia's 0.1363 (G7-3), which is not a
programme configuration. But the gate also did the other half of its job: the
halved-smoothing row's "fully legal" is a fine-set statement
— a denser probe found a real, thin DEC-negative layer just
inside its inner edge that the standard audit set steps
over — and the spline row's second finalist has isolated
off-set non-Type-I points. Neither row may be quoted without
its scope. And the strengthening removes Phase 50's last
"weaker": Procaccia's design passes Bars 1–4 at spacings
that resolve his switch, with his proven failure reproduced
at his point to 0.010% on the second path — the 0.1363 mark
the programme is climbing toward is a confirmed mark, and it
is his.

**Count (claim level, 3 claims):**
- **Survived intact (UPLOAD-READY as stated): 0.**
- **Survived weakened (UPLOAD-READY AFTER RESTATEMENT): 3**
  — G7-1 (numbers reproduced at both β; scope restated for
  the inner-edge DEC layer), G7-2 (both finalists reproduced
  outright on the deciding set; carried forward only with
  its deciding-set + robustness scope wording), G7-3
  (CONFIRMED AT OUR BARS; the confirmation uploadable only
  in its credited, scoped wording).
- **Fell (DEAD AS OURS): 0.** **NOT YET: 0.**
- **NOT REPRODUCED: 0** — no claim's deciding-set numbers
  failed on the fresh path.

**Correctness sub-count:** REPRODUCED: G7-2 (both
finalists). REPRODUCED WITH RESTATEMENT: G7-1 (both β —
restating for scope, not for deciding-set values).
CONFIRMED AT OUR BARS: G7-3 (the registered strengthening
condition discharged in full).

**Novelty sub-count (as amended by the Uniqueness Protocol,
2026-11-22 ~05:13 PT):** PARTIALLY KNOWN ×2 (G7-1: the
smoothing-tunes-legality premise is Fuchs et al.'s; the
direction, ceiling shift and mechanism are the residue, not
found in our search within the limits named. G7-2: shift
optimisation as a legality-buying move is Procaccia's, with
a Natário-class variational precedent; the transfer +
attribution + specific configuration are the residue, not
found in our search within the limits named). NOT FOUND IN
OUR SEARCH ×1 (G7-3 — the independent confirmation itself,
limits named in its verdict section; the underlying claim
is Procaccia's, and the standing verified single-shell
speed mark remains his 0.1363). Outright "novel" ×0.
KNOWN ×0.

**Rung verdicts:** rung 2b's gate-verified best of the
programme's own configurations is now
β = 0.10 (two configurations, each in its restated scope) —
the locked language "scan signal under attack" is lifted
for these two rows in their restated wordings only. Rung 2a
(FTL): nothing — every speed here is subluminal, and the
confirmed 0.1363 is Procaccia's design, not a programme
configuration. Traversable wormhole: nothing this gate.

## Errata / follow-ups owed (recorded, not executed by this gate)

1. **Prose point-count erratum (this gate's own record
   included):** §G7-3 above and the P50-1 memo say the
   Procaccia audit set has 1,352 points; the `p501_audit.py`
   construction both name produces **1,430 point-rows
   (1,378 distinct)** — radii 3.0/4.0 m are duplicated
   between the fine set and the edge cluster. The audited
   set is exactly the registered code construction;
   duplicates cannot affect any minimum or a 1.000 Type-I
   fraction. The prose count should be corrected wherever it
   appears (GATE7.md pre-registration §G7-3, CHECKPOINT50
   §P50-1, p501_memo.md).
2. **P50-1 cross-check magnitude:** the quoted
   −1.245×10⁻⁷ was a 20,000-direction sample of the min null
   contraction, which direction sampling under-reads by up
   to ~4× at coarse sample counts. The exact values are
   −1.294×10⁻⁷ (2nd-order, finest h) / −1.301×10⁻⁷
   (4th-order). A note is owed wherever the sampled number
   is quoted (p501_memo.md, CHECKPOINT50 §P50-1).
3. **Halved-smoothing row — inner-edge layer:** future
   audits of this family should add radii inside (10, 10.25)
   to the deciding set; Phase 50's family-ceiling statement
   (β* = 0.10) inherits the fine-set scope of G7-1's
   restated wording. Whether the layer also bounds the
   spline × halved-smoothing combination (Phase 50 follow-up
   queue item 4) is untested.
4. **Spline row — robustness scope:** the second finalist's
   isolated non-Type-I points sit at inner-edge radii
   between the deciding set's 0.5-step radii; a deciding set
   refined at the inner edge would either absorb or sharpen
   this scope note. The far-tail SEC −1.5×10⁻⁸ at r = 39 is
   at both paths' representation-noise floor and is recorded
   as a scope fact, not a violation claim.
5. **Coverage gap (all three novelty searches):** no worker
   reached the INSPIRE-HEP or Semantic Scholar search
   interfaces directly; both were covered via general-web /
   index routes only — the same bounded gap as Gate-5's G5-2
   flag and Gate-6's G6-1 flag, to be closed at write-up
   time if any of these claims is uploaded.
6. **Ledger:** the two β = 0.10 rows and the Procaccia
   confirmation can move to the gated tier of
   NEW_PHYSICS_LEDGER.md in their restated wordings only
   (a ledger edit, not executed by this gate).

**Upload-ready list (standing two-part rule):** G7-1, G7-2,
G7-3 — each ONLY in its restated wording as recorded
verbatim in its verdict section above (G7-2/G7-3 wordings in
their worker reports, §4 / final section respectively).
Nothing was uploaded by this gate.

**Status: COMPLETE** (all three workers returned; all three
claims verdicted; record closed 2026-11-22).
