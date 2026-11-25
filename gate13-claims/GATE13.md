# Novelty & Verification Gate 13 — GATE13.md (ground record)

**Status:** COMPLETE (2026-11-23) — **G13-1 SURVIVED
INTACT** (correctness REPRODUCED, novelty NOVEL;
checker 34/34 PASS, re-run by the coordinator).
Verdict, deciding numbers and the proposed ledger
edit are integrated at the end of this file. Nothing
was uploaded; the ledger was NOT edited.
**Work dir:** `~/workspace/warp-pilot/gate13/` — fresh
verifier code, search logs and memos in this dir and
`results/`.
**Parent records:** `../gate11/GATE11.md` (method and
form — this gate follows Gates 5–12 exactly; its fresh
symbolic radial-reduction path is the template),
`../gate12/GATE12.md`, `../phase116/CHECKPOINT116.md`
§P116-1 integrated verdict (the claim as made),
`../phase116/results/p1161_memo.md`,
`../phase116/results/p1161_run_record.md`,
`../phase116/results/p1161_economics.json`,
`../phase116/results/p1161_composed.json`,
`../phase116/results/p1161_alone_state.json`,
`../phase116/results/p1161_verify_e0.10_o0.0725_i0.06.json`,
`../phase116/results/p1161_check.json`,
`../phase88/CHECKPOINT88.md` (the predecessor row),
`../phase96/CHECKPOINT96.md` (the row's second-span
corroboration and queue).
**This gate prepares a verdict only. It uploads
NOTHING, contacts no one, and edits no phase record
and no ledger.** The ledger edit is PROPOSED at the
end of this file, not applied.

## The ruling this gate implements

Rakshit (2026-11-22): "Verify everything and tell
honestly what you found" + the Uniqueness Protocol
(2026-11-22 ~05:13 PT) + the standing publication rule
(gate-passed findings join the publication queue
automatically; ungated results wait). Scope: ONE
claim — Phase 116's P116-1 composed payload row.
Until this gate closes, the row remains
**phase-verified only**.

## Standards (identical to Gates 5–12)

float64 everywhere (40-digit mpmath where the phases
used it). Hedges intact. A NOVEL verdict requires the
search to be DOCUMENTED (queries verbatim + sources
checked), never asserted. Verdict categories per axis:
- Novelty: **NOVEL** / **PARTIALLY KNOWN** (exact known
  part cited) / **KNOWN** (cited — claim dies as "ours").
- Correctness: **REPRODUCED** (independent second path,
  within the margins/tolerances registered below) /
  **REPRODUCED WITH RESTATEMENT** (survives only
  weakened — exact restated wording supplied) /
  **NOT REPRODUCED** (second path disagrees — full
  anatomy required).
GATE VERDICT: **SURVIVED INTACT** / **UPLOAD-READY
AFTER RESTATEMENT** (restated form supplied) /
**DEAD** / **NOT REPRODUCED**.

**Uniqueness Protocol (binding):** no claim may be
worded "unique", "first", "record" or "novel" outright
unless (a) it beats the best verified mark in its
EXACT category, (b) independent second-path
reproduction inside this gate, (c) the novelty search
log is complete with queries verbatim AND coverage
gaps stated, (d) the claim's category and scope are
stated in the wording itself. Otherwise the wording is
"not found in our search (limits: …)" or "scan signal
under attack".

**Category discipline (binding on every wording):**
G13-1's category is **PAYLOAD TRANSPORT ONLY** (held
payload, composed shells). The bare-shell category's
mark (Procaccia 0.1363, Gate-7) is a different
category: no wording in this claim may borrow it,
compare against it, or describe the payload row as
approaching it. The succession inside the payload
category is stated exactly: the standing gate-verified
mark is Gate-11's **0.09556c** (PUBLISHED v1.12.0);
a reproduced G13-1 supersedes 0.09556c as this
category's gate-verified best, and the wording says so
in those terms and no stronger. Phase 80's 0.08745c
row remains phase-verified under Gate-10 (outcome not
cited, as in Gate-11).

## Carried facts (never separated from the claim)

- **The cavity settlement rides with the claim.**
  Phase 116 decided the deciding row's cavity by the
  Gate-8 settlement ladder as re-derived in its
  control (stencil-clear read **+9.48×10⁻⁵ at
  h = 0.075**); its two second paths read Type-I 1.000
  with worst −2.59×10⁻⁶ (4th-order diagnostic) and
  −3.24×10⁻⁶ (Phase-1 judge) — the settled cavity
  floor class, the same class as the 0.09556c row's
  own second path. This gate does NOT inherit that
  settlement: it re-derives it (registered path below).
- **The alone-β anatomy rides with the claim.**
  β = 0.0725 alone is legal at span ±0.10W and illegal
  at ±0.075W (a single fringe_hi non-Type-I patch:
  Type-I 0.904 at h = 0.15, sampled NEC −8.86×10⁻⁶,
  worsening under refinement — no convergence rescue).
  The interior failure that dominates at β = 0.075 is
  absent at 0.0725 at both spans (Phase 116 P116-3:
  that interior failure is GENUINE where it lives,
  and it lives above 0.0725).
- **C12 accounting:** prescribed-geometry audit.
  Subluminal pre-arranged configuration;
  construction-inclusive arrival ≥ D/c; no transport
  claim beyond the payload's own speed; no matter
  model, formation route or stability claimed. The
  source-consistency standard of Le
  (arXiv:2605.25417) stands as a caveat in the
  wording, as in Gate-11.

## Protocol (pre-registered, BEFORE any gate run)

NOVELTY: systematic arXiv + INSPIRE-HEP + Semantic
Scholar + general web search for the claim's exact
statement and near neighbours — here: nested/composed
warp shells carrying a held payload at or above
0.09758c at full legality, source-modulated
(Procaccia-form) shells as composition elements, and
the alone-ceiling-via-outer-β mechanism (raising a
composition's payload by raising the outer shell's
alone β inside its span-narrowed legal window);
every query logged verbatim with the sources actually
checked and the date; near neighbours cited by arXiv
ID / DOI / stable URL; the novel part (if any)
delimited in one quotable sentence. **Coverage gaps
stated plainly.** A search that could not be run is a
gap, not a negative result.

CORRECTNESS: independent second path — reimplement
the deciding computation FROM THE CLAIM STATEMENT
(fresh code in `gate13/`, not a re-run of a phase
script and not an import of Phase 116's `p1161_lib.py`,
Phase 88's machinery, or any gate's auditor as the
deciding machinery; shared *definitions* — the
composition specification, the per-shell design
vectors, the span parameterisation — may be imported
as data/text, the deciding machinery may not).
Reproduction = same signs and values within the
tolerances registered below. Anchors must pass BEFORE
any claim number is read; a failed anchor stops the
item as a machinery failure, not a claim failure.

OPTIMISATION DIRECTIVE + RIDER (standing): verification
runs as unattended scripts; pass/fail computed by
checker scripts over result files; offloading never
trades quality, speed or breadth.

## The claim (exact statement as tasked)

- **G13-1 (P116-1) — the β = 0.0725 composed row.**
  Phase 80's source-modulated nested composition
  (inner shell + payload cavity + outer shell, lapse
  re-equilibrated, both shells' orthonormal shifts
  held at their alone values per the Phase-46
  protocol; per-shell 14-number design vectors in
  `../phase116/results/p1161_economics.json` and
  `../phase116/results/p1161_alone_state.json` for the
  outer shell at β = 0.0725 and the Phase-80/88 lineage
  for the inner), with the Phase-88 span assignment
  (outer source-spline span **±0.10W**, transition
  [4.5, 10.5] around the shell [5, 10]; inner keeps
  **±0.30W**) and ONE registered change from the
  Gate-11 row: the outer shell alone at **β = 0.0725**
  (legal at ±0.10W; the alone ceiling is now bracketed
  to (0.0725, 0.075)). The deciding row — outer alone
  β = 0.0725, inner alone β = 0.06 — carries a **held
  payload of 0.09758c** (held-W payload sum
  0.17590965427919802, recorded in
  `p1161_economics.json` BEFORE any composed legality
  read; held shifts β_o^comp = 0.05910208146649168,
  β_i^comp = 0.03870429794369106; W relative errors
  ≤ 1.8×10⁻¹⁶). Claimed at full legality under the
  gate-standard audit (Type-I + sampled-null +
  margins, full volume over both shells AND the
  cavity): Type-I **1.000**; sampled NEC min
  **+1.13×10⁻⁶** (162 directions); region worst
  margins payload **+3.84×10⁻⁶**, inner wall
  **+1.191×10⁻³**, outer wall **+3.394×10⁻⁵**,
  exterior **+1.107×10⁻⁶**; conservation relative
  median 0.0117; cavity clean by the settlement ladder
  (+9.48×10⁻⁵ stencil-clear at h = 0.075).
  Corroborating row: the i0.05 companion
  (e0.10_o0.0725_i0.05) at **0.09118c** is also legal.
  Records: `../phase116/CHECKPOINT116.md` §P116-1 +
  final synthesis, `../phase116/results/p1161_memo.md`,
  `p1161_run_record.md`, `p1161_economics.json`,
  `p1161_composed.json`, `p1161_verify_e0.10_o0.0725_i0.06.json`,
  `p1161_check.json` (phase checker 22/22).

## Registered correctness path and bars

### G13-1 — the fresh path

The Phase-116 verdict rests on the Phase-80/88 FD
chain lineage plus two FD second paths. **The Gate-13
path must be different in kind: a symbolic
radial-reduction auditor** (the Gate-11 pattern).
Concretely, the worker:
1. Derives the Einstein tensor of the registered
   composed metric form (radial functions a(r), b(r);
   the composed shift profile along x; spatial part of
   the Fuchs form) symbolically (e.g. SymPy) in terms
   of the radial profiles and their first/second
   derivatives and the direction cosines — fresh
   derivation in `gate13/`, from the metric form, not
   copied from any phase or gate script;
2. Rebuilds the profiles from the shared design data —
   the per-shell design vectors, the chain construction
   and the Phase-46 composition specification imported
   as data/text (the specification text lives in
   `../phase80/` P80-3's library and memo and in the
   Phase-88/116 run records; the span parameterisation
   [R₁−eW, R₂+eW] with e = 0.10 outer / 0.30 inner is
   part of the shared definition) — with the chain,
   source spline and shift integration re-implemented
   fresh in `gate13/`;
3. Evaluates the tensor on the claim's point set using
   ANALYTIC derivatives of the profile representations
   — no Cartesian finite-difference stencil anywhere in
   the deciding path;
4. Computes Hawking–Ellis margins, Type-I
   classification and the sampled-null NEC cross-check
   (≥ 162 Fibonacci directions) with fresh code (shared
   *conventions* — the significance threshold — may be
   reused; the margin machinery is re-derived or
   independently implemented and anchor-validated).

ANCHORS (must pass BEFORE any deciding number is read;
a failed anchor stops the item as a machinery failure):
(i) Minkowski: the symbolic tensor is identically zero;
(ii) β = 0: the path's eigenvalues reproduce the exact
1-D spherical T of the shell profiles on sample radii
at the Gate-6 anchor scale (ρ relative error
≲ 3×10⁻³, principal-pressure absolute error
≲ 3×10⁻⁷);
(iii) CONTROL-SPAN ROW: the fresh path rebuilds the
e = 0.30 composed row (o0.06_i0.06) and reproduces
Phase 80's stored reads (cavity raw −1.107×10⁻⁴,
outer wall +3.2016×10⁻⁵, conservation relative median
0.0115; signs exact, magnitudes within a factor 3);
(iv) THE 0.0799 CONTROL (deciding anchor): the fresh
path audits the Phase-46 composed row itself — the
G8-1 configuration in its Gate-8 restated form — and
must reproduce its Gate-8 settlement: Type-I 1.000 on
the registered pattern with the Gate-8 sign pattern of
region worsts (inner wall +9.79×10⁻⁴, outer wall
+4.05×10⁻⁵, payload region +1.09×10⁻⁴ at h = 0.15;
signs and order of magnitude are the bar, magnitudes
within a factor 3), AND the cavity settlement
consistent with Gate-8 (floor artefact: sign-unstable
at |DEC| ≲ 2.3×10⁻⁴, no convergent negative continuum
value; every stencil-clear read ≥ +9.98×10⁻⁵ on the
Gate-8 ladder; an analytic path reading the control's
cavity cleanly is recorded as the stronger settlement,
as in Gate-11);
(v) THE 0.09556 GATE-11 ROW (deciding anchor): the
fresh path audits the Gate-11 row e0.10_o0.07_i0.06
and reproduces Gate-11's fresh-path reads (held
payload 0.0955573263c; Type-I 1.000; region worsts
payload +3.274×10⁻⁶, inner wall +9.783×10⁻⁴, outer
wall +4.852×10⁻⁵, exterior +2.087×10⁻⁶; sampled-null
min +2.27×10⁻⁶; cavity flagged site r ≈ 4.53 read
cleanly positive, +2.00×10⁻⁴ class) — signs exact,
magnitudes within a factor 3. This anchor exercises
the fresh chain at the deciding span e = 0.10 with the
narrowed chain's endpoint residuals in play.

DECIDING SET: the Phase-46/80/88/116 registered audit
pattern for the composed configuration (full volume
over both shells, the cavity, the payload region and
the exterior; the worker states the exact set from the
phase record in their run record BEFORE reading any
deciding number).

REPRODUCTION BARS (registered): the claim is
REPRODUCED iff, on the fresh path:
(a) ECONOMICS FIRST: the held-W payload of the
deciding row is reproduced from the design data
BEFORE any legality read: 0.0975831574914493c within
10⁻⁴ relative (held-W sum 0.17590965427919802;
held-W relative errors of order 10⁻¹⁶);
(b) Type-I fraction = 1.000 over significant points on
the deciding set;
(c) worst NEC/WEC/SEC/DEC margins > 0 in every region
(payload, inner wall, outer wall, exterior), signs
agreeing with the phase's reads and region worsts
within a factor 3 of the phase's (payload +3.84×10⁻⁶,
inner wall +1.191×10⁻³, outer wall +3.394×10⁻⁵,
exterior +1.107×10⁻⁶);
(d) sampled-null NEC min > 0 over ≥ 162 directions
(phase: +1.13×10⁻⁶);
(e) **CAVITY SETTLEMENT RE-DERIVED:** the fresh path's
reads on the deciding row's cavity settle it at the
Gate-8 standard on THIS path — either (i) the analytic
path reads the cavity sites ≥ 0, or at floor level
with no convergent negative value under its own
refinement ladder, or (ii) if the fresh path produces
a negative coarse read in the cavity, its ladder flips
it positive with stencil-clear reads > 0, mirroring
the controls' behaviour on the same machinery
(anchors (iv)/(v)). A convergent negative continuum
value in the cavity on the fresh path = NOT
REPRODUCED, with full anatomy, regardless of bars
(a)–(d);
(f) **FLOOR-CLASS STATEMENT:** the fresh path's cavity
reads on the deciding row (its own worst cavity value
and its site) are reported against BOTH bounds
(Phase 80's 2×10⁻⁶ and Phase 88's 4×10⁻⁶) and against
the Gate-8 settlement's own carried touch
(−3.7×10⁻⁶), and against Phase 116's second-path
floor reads (−2.59×10⁻⁶ / −3.24×10⁻⁶). The verdict
must state whether the row's legality, on the fresh
path, depends on any floor-class bound at all;
(f2) **ENDPOINT RESIDUALS ON THEIR MERITS:** the fresh
chain rebuild states its endpoint residuals for the
β = 0.0725 outer chain at e = 0.10 (S_lo−1, S_hi) and
reads their profile-level effect on the deciding
margins (Gate-11's (g) pattern: residuals that leave
the deciding reads inside tolerance are bookkeeping,
with the numbers; residuals that move a deciding read
across a bar = that bar's failure, anatomised);
(g) CORROBORATION: the i0.05 companion row (0.09118c)
passes the same audit pattern on the fresh path
(Type-I 1.000, all region worsts > 0, cavity settled
under (e)) — a failure here does not kill the deciding
row but must be restated in the wording's scope;
(h) MECHANISM SPOT-READ: the alone ladder's deciding
step — the outer shell alone at β = 0.0725, spans
e = 0.10 vs e = 0.075 — is re-read on the fresh path
(at e = 0.10: Type-I 1.000 with positive margins, or
the phase's demonstrated settled-floor signature
confined to the exterior; at e = 0.075: failing, with
the fringe_hi patch anatomy in kind — Type-I in the
0.904 class, sampled NEC negative). The mechanism
sentence in the wording stands only if this read
agrees in kind.
Sign agreement with (b)/(d) but a miss on (c)
magnitudes = REPRODUCED WITH RESTATEMENT (the gate's
own numbers replace the phase's in the restated
wording). Any failure of (a)/(b)/(d)/(e)/(f)/(g) =
NOT REPRODUCED, with full anatomy (site, binding
condition, whether the phase's paths share the failure
or the fresh path stands alone, and a tie-break read
named and run before the verdict is final).

## Worker assignment

- W-A: G13-1 correctness (fresh symbolic
  radial-reduction path; anchors (i)–(v); bars
  (a)–(h)) → `results/wA_g13_1.md`; fresh code
  `gate13/wa_*.py`; numbers
  `results/wa_g131_numbers.json`.
- W-B: G13-1 novelty (documented search, queries
  verbatim, coverage gaps stated) →
  `results/wB_novelty.md`; search log
  `results/wb_search_log.md`.

The workers do not edit this file; the coordinator
integrates the verdict from the worker reports +
checker-verified result JSONs, and writes the gate's
own checker over the gate's own result files.

## Status log

- 2026-11-23: gate opened by coordinator; ground
  records read (GATE11.md and GATE12.md in full;
  CHECKPOINT116.md in full incl. the P116-1 integrated
  verdict and final synthesis; the P116-1 datum files
  inspected). Protocol pre-registered above BEFORE any
  Gate-13 number was computed. Workers dispatched:
  W-A = correctness, W-B = novelty.
- 2026-11-23: W-B returned — novelty NOVEL (11 verbatim
  queries; search log `results/wb_search_log.md`;
  report `results/wB_novelty.md`).
- 2026-11-23: W-A returned — correctness REPRODUCED,
  checker 34/34 PASS over the worker's result files
  (`results/wa_check.json`); the coordinator re-ran
  `wa_check.py` from disk: 34/34 PASS. Coordinator
  integrated the verdict, closing synthesis and
  proposed ledger edit below. Gate CLOSED. Nothing
  uploaded; the ledger was NOT edited.

## Verdict (coordinator integration)

**G13-1: SURVIVED INTACT.**
- Correctness: **REPRODUCED** on a fresh symbolic
  radial-reduction path (fresh SymPy derivation from
  the metric form; span-parameterised chain/source-
  spline/shift integration rebuilt fresh in `gate13/`;
  analytic derivatives only; no Cartesian FD in any
  deciding quantity; no phase or gate machinery
  imported as deciding machinery). Worker report:
  `results/wA_g13_1.md`; numbers
  `results/wa_g131_numbers.json`; checker
  `results/wa_check.json` 34/34 PASS (coordinator
  re-run).
- Novelty: **NOVEL** — "not found in our search
  (limits: INSPIRE-HEP and Semantic Scholar reached
  only via indexes, no native sessions; non-English
  literature not searched; the non-peer-reviewed
  layered-bubble web document and the academia.edu-
  hosted Procaccia certificate read at
  abstract/introduction level; no live-browser or
  paywalled-full-text checks)": any composed/nested
  multi-shell warp configuration carrying a held
  payload at or above 0.09758c at full legality, any
  published use of optimised-source (Procaccia-form)
  shells as elements of a payload-carrying composition
  above 0.09556c, and any published raising of a
  composition's payload by raising a constituent
  shell's alone β inside a span-narrowed legal window.
  Search log: `results/wb_search_log.md` (11 verbatim
  queries; near neighbours Fuchs et al.
  arXiv:2405.02709, Bobrick–Martire arXiv:2102.06824,
  Van den Broeck arXiv:gr-qc/9905084, Le
  arXiv:2605.25417, arXiv:2602.18023, arXiv:2606.22531,
  Santiago–Schuster–Visser SSRN 4164341, Barzegar–
  Buchert–Vigneron arXiv:2602.16495 — all single-shell,
  all-violating, negative-energy-retaining, or
  payload-unmodelled; a threshold-specific query found
  0.09556/0.09758/0.0799 only in this programme's own
  records).

**Anchors (all passed BEFORE deciding numbers):**
(i) Minkowski max|G| = 3.47×10⁻¹⁸. (ii) β=0: ρ rel err
2.36×10⁻⁵, p abs err 2.02×10⁻⁹ (bars 3×10⁻³ / 3×10⁻⁷).
(iii) Control-span row e0.30_o0.06_i0.06: Type-I 1.000;
outer wall +4.831×10⁻⁵ vs stored +3.2016×10⁻⁵ (factor
1.51); conservation 0.0133 vs 0.0115 (factor 1.16);
cavity site read +2.022×10⁻⁴ where the FD paths read
−1.107×10⁻⁴ raw — the stronger settlement. (iv) 0.0799
control: Type-I 1.000; inner wall +9.678×10⁻⁴ (factor
0.99 vs Gate-8), outer wall +3.751×10⁻⁵ (factor 0.93);
cavity ladder floor −1.33×10⁻⁶…−2.04×10⁻⁶,
sign-unstable, no convergent negative — the Gate-8
settlement reproduced. Recorded exception, of the
same kind Gates 10/11 recorded: the payload-region
worst on this path (+3.308×10⁻⁶) sits on the
significance-borderline shell at r = 1.0878; at
Gate-8's own deciding site this path reads +1.172×10⁻⁴
(factor 1.08 vs the judge's +1.09×10⁻⁴). The anchor
passes on signs, Type-I and the settlement; the
exception is carried into the record, not hidden.
(v) The Gate-11 row reproduced at factor 1.00 on every
region: held payload 0.0955573263c, Type-I 1.000,
worsts +3.274×10⁻⁶ / +9.783×10⁻⁴ / +4.852×10⁻⁵ /
+2.087×10⁻⁶, sampled-null +2.27×10⁻⁶, cavity flagged
site +1.994×10⁻⁴.

**Deciding numbers (fresh path):** (a) economics
first: held payload **0.0975831574914493c** (rel err
4.3×10⁻¹⁶ vs the claim; bar 10⁻⁴), held-W sum
0.17590965427919802 exact, held-W rel errs
≤ 1.74×10⁻¹⁶, β_o^comp 0.05910208146649168 /
β_i^comp 0.03870429794369106. (b) Type-I **1.000**
(1040 significant points of 1300). (c) region worsts:
payload **+3.269×10⁻⁶** (×0.85), inner wall
**+9.786×10⁻⁴** (×0.82), outer wall **+4.863×10⁻⁵**
(×1.43), exterior **+2.087×10⁻⁶** (×1.89) — all signs
agree, all within factor 3. (d) sampled-null NEC min
**+2.25×10⁻⁶** (162 directions; phase +1.13×10⁻⁶).
(e) **cavity settlement re-derived in the stronger
form:** the flagged site r ≈ 4.53 reads **+2.03×10⁻⁴**
cleanly positive on the analytic path (the phase's raw
FD flag −1.131×10⁻⁴ does not reproduce at all);
residual negatives only near r ≈ 4.87 at floor level
(deciding-set worst −2.195×10⁻⁶; ladder minima
|DEC| ≤ 2.22×10⁻⁶ across spacings 0.1 → 0.0125,
wandering rather than converging; Type-I 1.000 at
every rung; sampled-null at the floor site +2.52×10⁻⁴)
— no convergent negative continuum value. (g)
corroborating row reproduced: **0.09118184734c**,
Type-I 1.000, all regions positive, cavity site
+1.987×10⁻⁴. (h) mechanism spot-read agrees in kind:
outer shell alone at β = 0.0725 reads Type-I **1.0000**
at e = 0.10 (worst +5.334×10⁻⁷, sampled +5.843×10⁻⁷ —
cleaner than the phase's settled-floor signature) and
fails at e = 0.075 on the fringe_hi patch only
(fringe_hi Type-I 0.846, sampled NEC −1.147×10⁻⁵,
eigenvalue worst positive; interior clean at both
spans).

**Disclosure (f) — the floor class, decided on its
merits:** the deciding set's cavity worst
(−2.195×10⁻⁶) sits marginally **outside** Phase 80's
narrower 2×10⁻⁶ bound (Gate-11's row sat inside it),
inside Phase 88's widened 4×10⁻⁶ bound and inside the
Gate-8 settlement's own carried touch class
(−3.7×10⁻⁶), and smaller in magnitude than Phase
116's own second-path floor reads on this row
(−2.59×10⁻⁶ / −3.24×10⁻⁶). **The row's legality on
the fresh path does not depend on any floor-class
bound** — the settlement is re-derived from the
analytic path's reads, not resting on either bound.
The upload wording carries this gate's own floor
figure (|DEC| ≲ 3.0×10⁻⁶ near r ≈ 4.87) in place of
Gate-11's ≲ 2.5×10⁻⁶.

**Disclosure (f2) — endpoint residuals, decided on
their merits:** the worker's rebuilt β = 0.0725 outer
chain at e = 0.10 reproduces Phase 116's stored chain
scalars to all printed digits (λ 0.959019336985,
k 0.177089668981, S_lo−1 = −4.3353×10⁻³,
S_hi = +9.4326×10⁻³, balance 2.14×10⁻¹⁶, monotonicity
exact). The residual-corrected variant (endpoints
forced exact) moves every deciding margin by < 0.3%
with no sign change: **the residuals are endpoint
bookkeeping and do not reach the audit.** Caveat
recorded on the worker's record (as in Gate-11): the
C⁰ correction ramp's own kinks give the corrected
variant Type-I 0.975 at floor level; the margins —
the registered question — do not move.

**Machinery event on the gate's own path (anatomised
in the worker report, recorded here):** the first
full run crashed in a cavity *logging* line (a KeyError
in the worker's print loop) after anchors, economics,
the deciding audit and the cavity site reads were
printed; no computation was wrong. The guard was
fixed and the run repeated end-to-end (EXIT=0,
434 s); every reported number is from the completed
re-run, which reproduces the crashed run's printed
values digit-for-digit where they overlap.

## Upload wording (verbatim, the only form in which
this claim may be carried)

> **Payload transport.** A nested (composed) warp
> configuration — an inner shell and an outer shell, each
> shell's shift derived by integration from an optimised
> Procaccia-form source, composed under the Phase-46 protocol
> with both shells' orthonormal shifts held at their alone
> values by lapse re-equilibration — with the outer shell's
> source-spline span at ±0.10W (transition [4.5, 10.5] around
> the shell [5, 10]; the inner shell keeps the ±0.30W span)
> and the outer shell alone at β = 0.0725 carries a held
> payload of **0.09758c** at full legality (Hawking–Ellis
> Type-I at every significant point of the full-volume audit
> over both shells, the cavity, the payload region and the
> exterior; worst margins: payload +3.84×10⁻⁶, inner wall
> +1.191×10⁻³, outer wall +3.394×10⁻⁵, exterior +1.107×10⁻⁶;
> sampled-null NEC positive everywhere). The mechanism: the
> outer shell alone at β = 0.0725 is legal at span ±0.10W
> and fails at ±0.075W on a single fringe_hi non-Type-I
> patch — its alone ceiling, inside its span-narrowed legal
> window, is bracketed to (0.0725, 0.075), and raising the
> outer shell's alone β from 0.07 to 0.0725 inside that
> window raises the composition's held payload from
> 0.09556c to 0.09758c. This row **supersedes Gate-11's
> 0.09556c as the payload transport category's
> gate-verified best** (Phase 80's 0.08745c row remains
> phase-verified under Gate-10; its outcome is not cited);
> no comparison with any bare-shell result is made or
> implied. A second composed row at 0.09118c passes the
> same audit pattern and corroborates the first. **Cavity
> caveat, in its settled form:** the primary
> finite-difference auditor's raw cavity DEC read on this
> row is −1.131×10⁻⁴ at r ≈ 4.53; an independent symbolic
> radial-reduction audit with analytic derivatives
> (Gate-13) reads that site cleanly positive (DEC
> +2.03×10⁻⁴ at r = 4.53), reads the 0.0799 control row's
> cavity and the Gate-11 row's cavity at floor level with
> no convergent negative continuum value, and finds the
> only residual negative reads on this row at floor level
> (|DEC| ≲ 3.0×10⁻⁶ near r ≈ 4.87), sign-unstable under
> refinement — the flagged read is a finite-difference
> representation artefact, settled on different-in-kind
> machineries. **Disclosure — floor-class bound:** the
> phase checkers' second-path cavity bounds are 2×10⁻⁶
> (Phase 80) and 4×10⁻⁶ (Phase 88); on the Gate-13 path the
> deciding set's cavity worst (−2.19×10⁻⁶) sits outside the
> narrower bound and inside the widened bound and inside
> the Gate-8 settlement's own carried touch class
> (−3.7×10⁻⁶), and the row's legality on this path rests on
> the re-derived settlement, not on either bound.
> **Disclosure — chain endpoint residuals:** at span
> ±0.10W the β = 0.0725 outer chain's endpoint residuals
> are S_lo−1 = −4.34×10⁻³ and S_hi = +9.43×10⁻³ (vs
> −3.92×10⁻³ / +8.43×10⁻³ for the β = 0.07 chain of the
> Gate-11 row) with balance (2.1×10⁻¹⁶) and monotonicity
> exact; Gate-13's rebuilt chain reproduces those residuals
> to all printed digits, and forcing the endpoints exact
> moves every deciding margin by less than 0.3% — the
> residuals are endpoint bookkeeping and do not reach the
> audit. **Accounting (C12):** this is a prescribed-geometry
> audit of a subluminal, pre-arranged configuration;
> construction-inclusive arrival is ≥ D/c; no transport
> claim beyond the payload's own speed is made; no matter
> model, formation route or stability is claimed. The
> source-consistency standard of Le (arXiv:2605.25417)
> stands as a caveat on this result: the audit certifies
> the geometry's required source against the classical
> energy conditions and does not supply a source-first
> matter model.

## Proposed ledger edit (PROPOSED, not applied)

Move GATE-QUEUED entry 236 to the PUBLISHED-pending
form the ledger editor applies on publication (per
the Gate-9/11 placement precedent, the entry stays in
its tier until a release moves it; the gate proposes
the replacement text and the tier marker):

**Replace entry 236's text with:**

> 236. **Payload transport, GATE-VERIFIED NEW BEST:
> 0.09758c at full legality** (Phase 116, Gate-13 —
> SURVIVED INTACT: correctness REPRODUCED on a fresh
> symbolic radial-reduction path, novelty NOVEL with
> search limits stated): raising the outer shell's
> alone β to 0.0725 inside its span-narrowed legal
> window (alone ceiling bracketed (0.0725, 0.075) at
> ±0.10W; fails at ±0.075W on a fringe_hi patch) raised
> the composed row e0.10_o0.0725_i0.06's held payload
> to 0.09758c (Gate-13 fresh-path reads: Type-I 1.000;
> payload +3.269×10⁻⁶, inner wall +9.786×10⁻⁴, outer
> wall +4.863×10⁻⁵, exterior +2.087×10⁻⁶;
> sampled-null min +2.25×10⁻⁶), corroborated by a
> second row at 0.09118c. The cavity is settled in
> the stronger form: the analytic path reads the
> flagged site (r ≈ 4.53) cleanly positive
> (+2.03×10⁻⁴); residual negatives are floor-level
> only (|DEC| ≲ 3.0×10⁻⁶ near r ≈ 4.87,
> sign-unstable, no convergent negative). Both
> disclosures are closed on their merits: the row's
> legality does not depend on any floor-class bound
> (deciding-set cavity worst −2.195×10⁻⁶ sits outside
> Phase 80's narrower 2×10⁻⁶ bound, inside Phase 88's
> 4×10⁻⁶ bound and the Gate-8 touch class, and the
> settlement is re-derived, not bound-based), and
> the β = 0.0725 chain's endpoint residuals
> (S_lo−1 = −4.34×10⁻³, S_hi = +9.43×10⁻³) are
> endpoint bookkeeping (forcing the endpoints exact
> moves every deciding margin <0.3%). Supersedes
> Gate-11's 0.09556c as the payload category's
> gate-verified best; Phase 80's 0.08745c row remains
> phase-verified under Gate-10, outcome not cited.
> The claim may be carried only in Gate-13's upload
> wording (gate13/GATE13.md). Basis: P116-1 (checker
> 22/22); Gate-13 (checker 34/34).

**Upload-ready list:** G13-1 — ONLY in the upload
wording recorded verbatim above. Nothing was uploaded
by this gate; publication follows the parent's
standing rule (the claim set joins the publication
queue automatically).

**Status: COMPLETE** (both workers returned; verdict
integrated; record closed 2026-11-23).
