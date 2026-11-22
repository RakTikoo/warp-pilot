# Novelty & Verification Gate 6 — GATE6.md (ground record)

**Status:** COMPLETE (launched and closed 2026-11-22; all four
workers returned; all four claims verdicted — closing synthesis
at the end of this file).
**Work dir:** `~/workspace/warp-pilot/gate6/` — verifier code,
search logs and memos in this dir and `results/`.
**Parent records:** `../phase26/CHECKPOINT26.md`,
`../phase42/CHECKPOINT42.md`, `../phase43/CHECKPOINT43.md`
(sources), `../gate5/GATE5.md` (method — this gate follows it),
`../NEW_PHYSICS_LEDGER.md` (all four claims sit in its
GATE-QUEUED tier).

## The ruling this gate implements (Rakshit, 2026-11-21 22:21 PT)

"Verify everything and tell honestly what you found." Scope: the
four Gate-6 claims below — Phase 26's β = 0.07 shell, Phase 42's
Φ ≠ 0 inertness theorem, Phase 43's bulk-shortcut measurement and
its component-blindness proof. This gate prepares verdicts only.
It uploads nothing, contacts no one.

## Standards (identical to Gates 1–5)

float64 everywhere. Hedges intact. A NOVEL verdict requires the
search to be DOCUMENTED (queries verbatim + sources checked),
never asserted. Verdict categories per axis:
- Novelty: **NOVEL** / **PARTIALLY KNOWN** (exact known part
  cited) / **KNOWN** (cited — claim dies as "ours").
- Correctness: **REPRODUCED** (independent second path, within
  stated margins) / **REPRODUCED WITH RESTATEMENT** (survives
  only weakened — exact restated wording supplied) /
  **NOT REPRODUCED** (second path disagrees — anatomy required).
GATE VERDICT per claim: **UPLOAD-READY** /
**UPLOAD-READY AFTER RESTATEMENT** (restated form supplied) /
**NOT YET** / **DEAD AS OURS** (KNOWN or NOT REPRODUCED).

## Protocol (pre-registered, per claim, BEFORE any gate run)

NOVELTY: systematic arXiv + INSPIRE + Semantic Scholar + web
search for the claim's exact statement and near neighbours;
every query logged verbatim with sources checked; near
neighbours cited by arXiv ID/DOI; the novel part (if any)
delimited in one quotable sentence.
CORRECTNESS: independent second path — reimplement the deciding
computation FROM THE CLAIM STATEMENT (fresh code in gate6/, not
a re-run of the phase script; shared *definitions* — stored
solution/basis fields whose audit is the claim — may be
imported, the deciding machinery may not), or derive
analytically where feasible. Reproduction = same signs and
values within the claim's stated margins/tolerances. Where a
claim is an audit of a published paper, the verifier re-derives
from the PAPER's printed formulas, not from the phase's
transcription.

## The four claims (exact statements as tasked)

- **G6-1 (P26-1)** The β = 0.07 subluminal shell: thick GR
  shell (R1,R2) = (10,30), ADM mass M = 8.0 geom =
  1.0773×10²⁸ kg, compactness M/R1 = 0.80, edge-peaked density
  (wd = 6.0, floor = 0.2), Gaussian smoothing (s_rho, s_P) =
  (4.0, 2.32), cosine shift on [10,30]. Fine audit (1,404 pts,
  h = 0.3/0.15): whole-volume worst margin SEC +2.59e-07 at
  both h (exterior tail r = 37.0), core NEC +3.76e-05 / WEC
  +3.28e-05 / DEC +1.97e-05 (binding r = 10.25), Type-I
  fraction 1.000. Record: `../phase26/CHECKPOINT26.md`,
  `../phase26/results/p261_memo.md`,
  `../phase26/results/p261_ledger.json`.
  Deciding sub-question (registered): the β = 0.08 boundary
  row — its failure rests on ONE sign-unstable inner-edge
  point, NEC −5.26e-07 at r = 10.25, h = 0.15 (coarse dense
  audit +9.9e-08 at both h). Settle by an h-ladder with local
  refinement at the inner edge whether 0.08 truly fails in
  the continuum limit or the point is an FD artefact.
- **G6-2 (P42-1)** The Φ ≠ 0 inertness theorem: for an
  F(·)R scalar-tensor Morris–Thorne throat, the demanded
  pair at r₀ is exactly the canonical Φ = 0 pair for any
  regular Φ: ρ_dem(r₀) = F₀β/(8πr₀²) − (1−β)F′₀/(16πr₀),
  p_r,dem(r₀) = −F₀/(8πr₀²) — every radial-derivative term
  carries the throat A-factor (1 − b/r), and the one
  Φ′-coupled survivor in ρ_dem cancels identically between
  □F and ∇^t∇_tF; Φ′ survives only as an EoM lever on the
  flux magnitude (unique off-grid root a* per (ξ, shape)).
  This unifies P35-4's teleparallel p_r lock and Phase 40's
  Φ = 0 result. Record: `../phase42/CHECKPOINT42.md` (P42-1),
  `../phase42/results/p421_memo.md`.
- **G6-3 (P43-1)** The bulk-shortcut measurement: in the
  P29-3 constructed bulk lift of the exhibited √-shape
  braneworld throat, a cross-throat bulk null geodesic beats
  brane-confined light by fractional gain 0.480 at z_a = 1
  (brane 6.2784 r₀/c → bulk 3.2618 r₀/c; u_eff = 1.92c),
  throat-specific (same-sheet control gain ≈ 0.00025),
  EFFECTIVE ONLY under C12 (formation of throat+bulk has no
  classical route — setup leg unavailable, not merely
  losing), infimum not attained (gain grows monotonically
  with the depth cap; lives at the singular bulk boundary).
  Record: `../phase43/CHECKPOINT43.md` (P43-1),
  `../phase43/results/p431_results.json`,
  `../phase43/results/p431_bulk_fields.npz`.
- **G6-4 (P43-3c)** The component-blindness proof: a
  Krasnikov tube's QI sampling bound on a fixed total is
  decomposition-independent, B_tot = (Σᵢcᵢ)·Φ[f] — a function
  of field content, sampler and background only; the only
  mixture analogue is the species factor (N free fields buy
  at most N × the single-field bound; tube escape needs
  N ≥ 1.06×10⁷²). Scope: free fields; interacting-4D QEI is
  the named reopening. Record:
  `../phase43/CHECKPOINT43.md` (P43-3c),
  `../phase43/results/p433_memo.md`.

## Worker assignments

- W-A: G6-1 (β = 0.07 shell + β = 0.08 boundary) →
  `results/wA_g6_1.md`
- W-B: G6-2 (Φ ≠ 0 inertness theorem) → `results/wB_g6_2.md`
- W-C: G6-3 (bulk-shortcut measurement) → `results/wC_g6_3.md`
- W-D: G6-4 (component-blindness proof) → `results/wD_g6_4.md`

Each worker: correctness FIRST (fresh code in gate6/, run with
system python3 or the phase venv at
`~/workspace/warp-pilot/venv/bin/python`), then novelty with
logged queries. Each returns per-claim: correctness verdict +
deciding numbers from THEIR run; novelty verdict + citations;
and, wherever the claim survives only weakened, the EXACT
restated wording.

## Verdicts

### G6-1 — β = 0.07 shell + β = 0.08 boundary (W-A, 2026-11-22)

Full report: `results/wA_g6_1.md`; fresh code `wa_auditor.py`,
`wa_run.py`, `wa_diag.py`; data `wa_results.json`.
`verify_metric.py` never used; only `shell.py` imported as the
shared metric definition. Auditor discretisation differs in
kind: 2nd-order central FD for first AND second metric
derivatives directly, ∂Γ computed algebraically from ∂g, ∂²g —
no nested Γ stencil. Anchors passed before any claim number:
Minkowski max|G| = 0 exactly; static β = 0 eigenvalues vs the
exact 1-D spherical T (ρ ≤ 0.31% rel. err., clean h² scaling);
Finalist A positive (+2.14e-07, Type-I 1.000).

- **Correctness (a) — the β = 0.07 configuration: REPRODUCED.**
  Worker's numbers (1,404 pts, 26 dirs): whole-volume worst
  SEC **+2.580e-07 (h = 0.3) / +2.590e-07 (h = 0.15)** at
  r = 37.0 (claim: +2.591e-07 / +2.593e-07); core NEC
  +3.730e-05 / +3.729e-05, core WEC +3.513e-05, core DEC
  +1.943e-05 / +1.965e-05 (all binding r = 10.25); Type-I
  fraction 1.000; sampled-null core NEC +1.223e-05; FD floor
  ~2e-08. The configuration and its margin ledger stand.
- **Correctness (b) — the β = 0.08 boundary: Phase 26's
  failure NOT REPRODUCED; 0.08 passes, the 0.07 ceiling is
  wrong.** The Phase-26 failure rested on ONE point —
  (−1.2926, 9.9753, −1.9712), r = 10.25, read non-Type-I
  with sampled-fallback NEC −5.26e-07 at h = 0.15. On the
  gate path: inner-edge h-ladder (radii 9.75–11.50, h = 0.3 →
  0.0375) gives min NEC +1.7723e-05, +1.7697e-05, +1.7675e-05,
  +1.7670e-05 → **Richardson continuum +1.767e-05 ± 1e-07,
  POSITIVE** (~34× larger in magnitude than, and opposite in
  sign to, the phase's −5.26e-07); at the exact suspect point
  both the worker's 2nd-order auditor and an independent
  4th-order variant converge to NEC ≈ +1.94e-05, Type-I, at
  every h. The Phase-26 point is a machinery artefact of the
  Phase-1 nested-Γ-stencil judge at that single point. The
  worker's full β = 0.08 audit also passes (worst SEC
  +2.58e-07/+2.59e-07, core DEC +1.28e-05, Type-I 1.000).
  **The H-a ceiling is ≥ 0.08, not 0.07.** Follow-up owed
  (outside this gate's scope, flagged in the report):
  Phase 26's β = 0.09 fine row failed at the SAME suspect
  point (−1.10e-06, h = 0.15) and is UNSETTLED until
  re-audited; β = 0.10's failure was mid-shell and h-stable
  and is NOT impeached. An erratum to the Phase-26 record's
  ceiling claim is owed.
- **Novelty: PARTIALLY KNOWN.** The class is Fuchs et al.
  2024 (arXiv:2405.02709 — all-EC shell, exhibited at
  v ≈ 0.02–0.04); framework Bobrick & Martire
  (arXiv:2102.06824); toolkit Warp Factory
  (arXiv:2404.03095). Decisively, Procaccia (publicly posted
  Oct 30, 2026, academia.edu, unrefereed) certifies an
  all-EC Fuchs-form shell — (10,20), M = 6, zero radial
  pressure, optimised spline shift — at every β up to
  **0.1363**, anticipating any "past 0.05 / past 0.07"
  framing. Lentz (arXiv:2006.07125) and Fell & Heisenberg
  (arXiv:2104.06488) claim only Eulerian positive energy;
  Santiago–Schuster–Visser (arXiv:2105.03079) is a no-go for
  the Natário class this family sits outside. Caveat carried
  for any upload: Le (arXiv:2605.25417) finds Type-IV tail
  violations in the Fuchs shell under a stricter
  source-consistency standard. Coverage limit recorded:
  INSPIRE-HEP / Semantic Scholar reached only via
  arXiv-linked indexes, no native sessions. Novel part, one
  sentence: only the specific TOV thick-shell configuration
  — (10,30), M = 8.0 at compactness 0.80, edge-peaked
  density, cosine shift — and its margin ledger; EC-legal
  shells as a class, and legality above β = 0.05, are
  already in the literature.
- **GATE VERDICT: UPLOAD-READY AFTER RESTATEMENT** — overall
  correctness REPRODUCED WITH RESTATEMENT (configuration
  reproduced; ceiling sub-claim NOT REPRODUCED and dropped;
  ledger now includes β = 0.08). Exact restated wording
  (required for any upload): "Within the Fuchs et al.
  (2024) TOV-shell family, the thick-shell configuration
  (R₁,R₂) = (10,30), ADM mass M = 8.0 geometric units =
  1.0773×10²⁸ kg (compactness M/R₁ = 0.80), edge-peaked
  density (wd = 6.0, floor = 0.2), Gaussian smoothing
  (s_rho, s_P) = (4.0, 2.32), cosine shift on [10,30],
  satisfies NEC, WEC, SEC and DEC at every audited point
  (1,404 points, Hawking–Ellis Type-I fraction 1.000,
  whole-volume worst margin SEC +2.59e-07 in the exterior
  tail at r = 37.0, core margins NEC +3.73e-05 / DEC
  +1.94e-05 at r = 10.25) at β = 0.07 — and, on independent
  re-audit with an h-ladder to h = 0.0375 (continuum
  inner-edge NEC +1.767e-05), also at β = 0.08, so β = 0.07
  is not the family ceiling. Fully EC-legal subluminal
  shells are known (Fuchs et al. 2024, arXiv:2405.02709),
  and a certified all-EC shell reaching β = 0.1363 in a
  different (zero-radial-pressure, shift-optimised (10,20))
  design was publicly posted by Procaccia (Oct 2026); the
  novel content of this result is the specific TOV
  thick-shell configuration and its margin ledger, not the
  existence of EC-legal shells above β = 0.05."

### G6-3 — Bulk-shortcut measurement (W-C, 2026-11-22)

Full report: `results/wC_g6_3.md`; fresh code
`wc_g63_solver.py`, `wc_g63_rest.py`, `wc_g63_scans.py`;
numbers `results/wc_g63_numbers_{main,rest,scans}.json`.
Phase 43's variational minimiser NOT re-run. Fresh path:
Euler–Lagrange ODE for the optical metric
diag((D/A)², (1/A)²), solved by shooting/root-finding
(DOP853) on the stored bulk fields (shared definition),
headline paths re-evaluated under both spline and linear
field representations.

- **Correctness: REPRODUCED WITH RESTATEMENT.** Structural
  finding: no smooth symmetric crossing geodesic exists for
  any z_a (throat-launched geodesics return within
  Δz ≤ 0.26); the optimum is a geodesic-arc + cap-ride path,
  matching Phase 43's stored path shape (cap entry
  z₁ = 0.697 vs their 0.73). Deciding numbers (cap
  y ≤ 0.455): **flat-bulk gate EXACT** (gain 0.0, rel. err
  0.0 vs the ≤ 1e-10 bar, same code path). **z_a = 1: gain
  0.4800, T = 3.2646, u_eff = 1.923c — the headline 0.480 is
  CONFIRMED** (two internal tolerances agree to 4×10⁻¹²;
  linear-field evaluation 0.4804; error ±0.002); the stored
  nseg-24 value 0.5065 is the coarse artefact, as Phase 43's
  own subdivision suggested. **z_a = 0.5: 0.436, not 0.422**
  — Phase 43's subdivided figure was an upper bound on T
  from subdividing a fixed path, not a re-minimisation.
  **z_a = 2: 0.289, not 0.177** — Phase 43's subdivided path
  was tangled/suboptimal (its stored nodes jump
  non-monotonically); the gate's clean optimum (T = 10.883
  spline / 10.880 linear) sits between the phase's two
  erroneous reads. Depth caps at z_a = 1 reproduce and
  extend: **0.067 / 0.166 / 0.348 / 0.480 at caps
  0.20 / 0.30 / 0.40 / 0.455** (phase coarse reads
  0.068 / 0.171 / 0.371 / 0.509), plus 0.492 at the slab
  edge 0.46 — monotone, optimum always at the cap,
  **infimum not attained** ✔. Same-sheet control ≈ 0.00019
  (stored 0.00025) — throat-specificity confirmed. The
  stored forced-depth rows are cornered discrete paths, not
  geodesic times (no geodesic arc from (1,0) reaches the
  throat plane aloft in the slab); the claim's hedge rests
  on the cap sequence, which reproduces.
- **Novelty: PARTIALLY KNOWN.** The concept and quantitative
  measurements in cosmological / domain-wall / AdS-BH bulks
  are published: Chung–Freese (see the ID correction
  below), Caldwell–Langlois (arXiv:gr-qc/0103070), Abdalla
  et al. (arXiv:hep-th/0109024; hep-th/0205203;
  hep-th/0209101; hep-th/0501076), Leach–Lesame
  (arXiv:gr-qc/0502109), Dai–Stojkovic
  (arXiv:2306.04069). Not found anywhere (11 queries logged
  verbatim): a measured gain inside an exhibited
  wormhole-throat bulk lift, with the same-sheet control
  and the unattained-infimum-at-the-singularity structure.
  The novel part is the measurement in this constructed
  bulk, not the shortcut concept. **Bibliographic
  correction (worker's catch): Chung–Freese is
  arXiv:hep-ph/9910235, not hep-ph/9912346** — every citing
  source gives 9910235; the wrong ID appeared in this
  gate's own worker brief and must not propagate.
- **GATE VERDICT: UPLOAD-READY AFTER RESTATEMENT** — exact
  restated wording in `results/wC_g6_3.md` §6: gains
  0.480 (z_a = 1, unchanged), **0.436 at z_a = 0.5**
  (was 0.422), **0.289 at z_a = 2** (was 0.177); cap
  sequence 0.067 / 0.166 / 0.348 / 0.480 / 0.492; control
  ≈ 0.0002; all hedges intact (cap-labelled, infimum not
  attained, EFFECTIVE ONLY under C12, graviton-only
  carrier).

### G6-4 — Component-blindness proof (W-D, 2026-11-22)

Full report: `results/wD_g6_4.md`; check code `wd_arith.py`
(mpmath, 30-digit).

- **Correctness: REPRODUCED WITH RESTATEMENT.** Steps 2–4 of
  the proof (linearity; summing valid inequalities; the bound
  never sees the attribution) are correct; per-field QEIs
  quantify over ALL Hadamard states, so cross-component
  entanglement also buys nothing (a route the memo did not
  need). All three counterexample routes independently
  attacked and confirmed closed: (a) a below-floor component
  is by construction not a free-field expectation value;
  (b) Φ is pinned by sampler/worldline/fixed metric — a
  bookkeeping split has no lever; (c) adding fields is
  exactly the priced species case. Main technical finding:
  the factored form B_tot = (Σᵢcᵢ)·Φ[f] with a single common
  Φ is exact only for identical fields / flat-space massless
  species — in general each field's functional Φᵢ depends on
  its own mass/spin (e.g. Fewster–Eveson's Q₃(u/m)), so the
  theorem-grade form is **B_tot = Σᵢ Φᵢ[f]**;
  decomposition-independence survives intact. Scope clauses
  the memo left implicit, now mandatory: components must be
  mutually non-interacting free quantum fields admitting
  *state-independent* QEIs (the non-minimally coupled scalar
  admits only a state-dependent QEI — a real hole in the
  memo's quantifier); classical components are outside the
  proof; in curved backgrounds the statement is a
  difference-QEI (excursion below the summed reference
  value). None of these narrows the tube application.
- **Arithmetic: one number WRONG.** N ≥ 1.06×10⁷² ✔;
  1.06×10⁷³ at L = a ✔; caps 3.83×10⁶⁹ (ℓ = 1 m) and
  3.83×10⁶⁷ (ℓ = 0.1 m) ✔; shortfalls 2.45 / 4.45 orders ✔.
  But **Λ ~ M_P/√N at N = 10⁷² is 1.22×10⁻⁸ eV, not
  ~10⁻¹⁷ eV** — a GeV↔eV slip (10⁻¹⁷ is the value in GeV).
  The qualitative claim survives: Λ ≈ 1.2×10⁻⁸ eV ↔ cutoff
  length ħc/Λ ≈ 16 m, larger than the 1 m tube, so the
  semiclassical frame still dissolves.
- **Novelty: PARTIALLY KNOWN.** QEIs are standardly stated
  per field (Ford–Roman arXiv:gr-qc/9607003; Fewster–Eveson
  arXiv:gr-qc/9805024; Fewster–Teo PRD 59, 104007 (1999)),
  and the summed form is effectively in print in 2D CFT,
  where Fewster's bound runs through the central charge
  c = Σᵢcᵢ (Rev. Math. Phys. 17 (2005) 577). Not found
  anywhere searched (11 queries logged verbatim): the
  anti-loophole corollary stated for a fixed metric-pinned
  total, nor the tube species pricing. Novel part, one
  sentence: the component-blindness statement isolated as
  the closure of the splitting loophole for exotic-matter
  engineering, with the Krasnikov species escape priced at
  N ≥ 1.06×10⁷².
- **GATE VERDICT: UPLOAD-READY AFTER RESTATEMENT** — exact
  restated wording in `results/wD_g6_4.md` §4 (summed-
  functional form B_tot = Σᵢ Φᵢ[f] with the factored form as
  its identical-fields/flat-massless special case; explicit
  scope clauses; corrected Λ ≈ 1.2×10⁻⁸ eV; difference-QEI
  clause; reopening condition unchanged).

### G6-2 — Φ ≠ 0 inertness theorem (W-B, 2026-11-22)

Full report: `results/wB_g6_2.md`; fresh code
`wb_g62_derivation.py`, `wb_g62_numeric.py` (+ `.json`) —
neither Phase-42 derivation script re-run or copied.

- **Correctness: REPRODUCED.** Third, structurally different
  path: general diagonal parametrisation with independent
  lapse N(r) and radial function S(r), F/N/S unspecified
  functions, throat limit by series in ε = r − r₀. Computed
  outputs exhibit the mechanism rather than assuming it:
  G^r_r's Φ′ piece is 2AΦ′/r; □F = AF″ + F′A′/2 + AΦ′F′ +
  2AF′/r and ∇^t∇_tF = AΦ′F′, so the cancellation is a
  computed fact; the coefficient of F″ is exactly 0 in p_r
  and exactly −A in ρ. General-r pair diffs vs the claimed
  formulas: exactly 0 (both channels); throat limits ρ, p_r
  and R(r₀) = 2β/r₀² − (1−β)Φ′₀/r₀ all DIFF = 0. Numeric
  spot check: controlled triples C1–C3 with identical
  F₀ = 2.215, β = +1/2 but F′₀ ∈ {+1.08, −2.97, +5.40},
  F″₀ ∈ {+2.10, −0.69, +19.56}, Φ′₀ ∈ {+0.5, −1.7, +2.3}
  extrapolate to a p_r spread of only 1.4e-04 around
  −F₀/(8π); ρ matches canonical in all cases; Ellis case
  passes (all errors ≤ 3.6e-04). One evaluator bug (G^t_t)
  was caught and fixed mid-run and is recorded in the
  report. Unification check: Phase 40's Φ = 0 pair + cone
  F′₀ = −2F₀/r₀ verified as the Φ′₀ = 0 special case;
  P35-4 is NOT the same theorem (in teleparallel the r–r
  equation has no derivative term at any r; here terms exist
  off-throat and die via A/cancellation) — the ledger's
  "same pattern, mechanism differing" is the correct
  reading, and the claim's "unifies" wording must be
  downgraded to pattern level.
- **Novelty: PARTIALLY KNOWN.** Known: the general-r
  equations and the Φ = 0 throat evaluation are the
  literature's standard apparatus (arXiv:0909.5539;
  arXiv:1007.3040; arXiv:1709.06431 — the literature
  standardly sets Φ′ = 0, e.g. arXiv:1012.2443 "simplifies
  the calculations"); Bronnikov et al. (arXiv:gr-qc/0612032;
  arXiv:1005.3262; arXiv:1802.00098) prove Einstein-frame
  no-go theorems and Barceló–Visser (arXiv:gr-qc/0003025)
  give specific solutions — neither states this result.
  Not found (8 queries logged verbatim): the Φ ≠ 0
  inertness statement itself. Novel part, one sentence: for
  regular Φ the Φ ≠ 0 extension changes nothing at the
  throat — every radial-derivative term carries A, the
  AΦ′F′ piece cancels identically, p_r,dem(r₀) is
  independent of F′₀/F″₀/Φ′₀, and Φ′ acts only through
  R(r₀) in the scalar EoM.
- **GATE VERDICT: UPLOAD-READY AFTER RESTATEMENT** — the
  only change is the unification clause, downgraded to
  pattern level. Exact restated wording (required for any
  upload): "In F(φ)R scalar-tensor gravity (canonical
  scalar, potential V(φ)) on a Morris–Thorne throat with
  regular Φ (Φ, Φ′, Φ″ finite at r₀), the demanded matter
  pair at the throat is exactly the canonical Φ = 0 pair
  for any such Φ: ρ_dem(r₀) = F₀β/(8πr₀²) −
  (1−β)F′₀/(16πr₀) and p_r,dem(r₀) = −F₀/(8πr₀²), because
  every radial-derivative term in the t–t and r–r field
  equations carries the factor A = 1 − b/r — including
  AΦ′₀F′₀ and 2AF₀Φ′₀/r₀ — the AΦ′F′ piece of □F cancels
  identically against ∇^t∇_tF = AΦ′F′, F″₀ enters neither
  channel, and Φ′ survives only in the scalar equation of
  motion via R(r₀) = 2β/r₀² − (1−β)Φ′₀/r₀, moving the EoM
  flux's magnitude but not its sign on the families tested.
  Phase 40's Φ = 0 result is the Φ′₀ = 0 special case of
  this theorem. Phase 35's teleparallel p_r lock (P35-4) is
  the same *pattern* by a *different mechanism* — there the
  r–r equation contains no derivative term at any r — not
  the same theorem."

## Closing synthesis (coordinator, 2026-11-22)

**The honest headline: the flagship got better and its
ceiling died; the theorem is exact; two sets of phase numbers
needed correction; and all four claims were overstated in
framing, none in substance.** Every claim's core survived an
independent second path — but no claim passes both axes
without a restatement, and the gate's most consequential
finding is a Phase-26 error it caught: the β = 0.07 "ceiling"
rested on a single machinery-artefact point, and β = 0.08 is
legal.

**Count (claim level, 4 claims):**
- **Survived intact (UPLOAD-READY as stated): 0.**
- **Survived weakened (UPLOAD-READY AFTER RESTATEMENT): 4**
  — G6-1 (configuration reproduced and extended to β = 0.08;
  "ceiling 0.07" and "first past 0.05" framings both dead),
  G6-2 (theorem reproduced exactly; unification downgraded
  to pattern level), G6-3 (headline gain 0.480 confirmed;
  z_a = 0.5 / z_a = 2 rows restated to 0.436 / 0.289),
  G6-4 (proof stands; headline formula restated as
  B_tot = Σᵢ Φᵢ[f], scope clauses explicit, one number
  corrected).
- **Fell (DEAD AS OURS): 0** as whole claims — but two
  sub-claims died: G6-1's ceiling (NOT REPRODUCED — the
  deciding point is a Phase-1-judge artefact) and G6-3's
  z_a = 2 figure (NOT REPRODUCED as stated — the phase's
  subdivided path was tangled; converged gain is 0.289,
  not 0.177).

**Correctness sub-count:** REPRODUCED outright: G6-2, and
G6-1(a) (the β = 0.07 configuration, margins matching to
~0.4% on a discretisation different in kind). REPRODUCED
WITH RESTATEMENT: G6-1 as a whole (ceiling sub-claim dead),
G6-3 (two of three gain rows corrected; headline, caps,
control, infimum structure all confirmed), G6-4 (proof
sound; formula generality and one arithmetic value
corrected). NOT REPRODUCED: G6-1(b) (the β = 0.08 failure —
continuum inner-edge NEC +1.767e-05 ± 1e-07, positive, on an
h-ladder with two discretisations) and G6-3's z_a = 2 row
as stated.

**Novelty sub-count:** PARTIALLY KNOWN ×4, NOVEL ×0,
KNOWN ×0. Every claim's machinery or concept had published
roots (Fuchs 2024; the Φ = 0 throat apparatus; Chung–Freese
and the braneworld-geodesic literature; per-field QEIs with
the summed form in print in 2D CFT); every claim also has a
delimited novel residue, stated in one quotable sentence in
each verdict section.

**Errata and follow-ups owed (recorded, not executed by
this gate):**
1. Phase-26 record: the H-a ceiling "β = 0.07" is wrong —
   β = 0.08 passes the gate audit; an erratum belongs in
   `../phase26/CHECKPOINT26.md`, and the programme's
   rung-2b "best" is now the β = 0.08 row of the same
   configuration pending the phase's own ledger update.
2. Phase-26's β = 0.09 fine row failed at the same
   impeached point and is UNSETTLED — re-audit owed before
   any ceiling above 0.08 is quoted either way. (β = 0.10's
   mid-shell h-stable failure is not impeached.)
3. Phase-43 record: P43-1's z_a = 0.5 / z_a = 2 gains
   should carry the gate's converged values (0.436 /
   0.289); the stored p431 path nodes for z_a = 2 are
   tangled.
4. Phase-43's p433 memo: the species-scale value
   "Λ ~ 10⁻¹⁷ eV" is a GeV↔eV slip — correct value
   ≈ 1.2×10⁻⁸ eV (conclusion unchanged in kind).
5. Bibliographic: Chung–Freese is arXiv:hep-ph/9910235
   (not 9912346, which appeared in this gate's own brief).
6. Any G6-1 upload must cite Le (arXiv:2605.25417)'s
   tail/source-consistency caveat alongside the claim.
7. Coverage limit: G6-1's search reached INSPIRE-HEP /
   Semantic Scholar only via arXiv-linked indexes (no
   native sessions) — a bounded gap of the same kind as
   Gate-5's G5-2 flag, to be closed at write-up time if
   G6-1 is uploaded.

**Upload-ready list (standing two-part rule):** G6-1, G6-2,
G6-3, G6-4 — each ONLY in its restated wording as recorded
verbatim in its verdict section above. Nothing was uploaded
by this gate.

**Status: COMPLETE** (all four workers returned; all four
claims verdicted; record closed 2026-11-22).
