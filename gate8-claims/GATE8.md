# Novelty & Verification Gate 8 — GATE8.md (ground record)

**Status:** COMPLETE (launched and closed 2026-11-22; both
workers returned; both claims verdicted — verdicts and
closing synthesis at the end of this file).
**Work dir:** `~/workspace/warp-pilot/gate8/` — verifier code,
search logs and memos in this dir and `results/`.
**Parent records:** `../phase46/CHECKPOINT46.md` (sources:
P46-2, P46-3), `../phase43/CHECKPOINT43.md` (P43-1),
`../gate6/GATE6.md` (method + G6-3 verdict),
`../gate6/results/wC_g6_3.md` (G6-3 restated wording, §6),
`../NEW_PHYSICS_LEDGER.md` (the two claims sit in its
GATE-QUEUED tier as entries 31 and 33).

## Scope and the baseline this gate does NOT re-open

The bulk-shortcut claim was ALREADY published in v1.9.0 in
its Gate-6 restated form: gain 0.480 at z_a = 1 (0.436 at
z_a = 0.5, 0.289 at z_a = 2), cap-labelled, **infimum NOT
attained**, **EFFECTIVE ONLY** under C12, graviton-only
carrier. Phase 46's P46-3 does NOT contradict that
publication — its hedges said exactly what P46-3 confirmed
(the 0.480 is unattained; the singularity is load-bearing
for its size). This gate's job is ONLY the NEW statements
Phase 46 added (G8-1, G8-2 below). It uploads nothing,
contacts no one.

## Standards (identical to Gates 5–7)

float64 everywhere. Hedges intact. A NOVEL verdict requires
the search to be DOCUMENTED (queries verbatim + sources
checked), never asserted. Verdict categories per axis:
- Novelty: **NOVEL** / **PARTIALLY KNOWN** (exact known part
  cited) / **KNOWN** (cited — claim dies as "ours").
- Correctness: **REPRODUCED** (independent second path,
  within stated margins) / **REPRODUCED WITH RESTATEMENT**
  (survives only weakened — exact restated wording
  supplied) / **NOT REPRODUCED** (second path disagrees —
  full anatomy required).
GATE VERDICT per claim: **UPLOAD-READY** /
**UPLOAD-READY AFTER RESTATEMENT** (restated form supplied)
/ **NOT YET** / **DEAD AS OURS** (KNOWN or NOT REPRODUCED).

## Protocol (pre-registered, per claim, BEFORE any gate run)

NOVELTY: systematic arXiv + INSPIRE + Semantic Scholar +
web search for the claim's exact statement and near
neighbours; every query logged verbatim with sources
checked; near neighbours cited by arXiv ID/DOI; the novel
part (if any) delimited in one quotable sentence; coverage
gaps (any index not natively reachable) stated plainly.
CORRECTNESS: independent second path — reimplement the
deciding computation FROM THE CLAIM STATEMENT (fresh code
in gate8/, not a re-run of the phase script; shared
*definitions* — stored solution/basis fields whose audit is
the claim — may be imported, the deciding machinery may
not), or derive analytically where feasible. Reproduction
= same signs and values within the claim's stated
margins/tolerances.

## The two claims (exact statements as tasked)

- **G8-1 (P46-2)** The composed configuration: nested GR
  shells with the inner shell solved IN the composed lapse
  (coordinate β_i turned down by exactly the lapse factor
  ×0.6451, e^a ratio; orthonormal shift W held at the
  verified alone value 0.06638), carrying a PAYLOAD at
  **0.0799c** at full bars — full-volume all-directions
  NEC/WEC/SEC/DEC, Hawking–Ellis Type-I fraction 1.000,
  conservation clean (h = 0.15 worst margins by region:
  inner wall +9.79×10⁻⁴, outer wall +4.05×10⁻⁵, payload
  region +1.09×10⁻⁴). Follow-up rows (NOT verdict rows):
  dual re-equilibration passes at payload 0.0729; β_o
  capped at its verified 0.05 gives a passing payload
  0.0821. At payload 0.0998 the inner kill of P41-3 is
  gone but the outer wall fails SEC −2.73×10⁻⁴
  (h-converged) — the P22-3 trigger does not fire.
  **CARRIED CAVEAT (deciding sub-question, registered):**
  the verdict row's focused payload-region DEC touches
  **−3.7×10⁻⁶ at h = 0.075** (one point; Type I still
  1.000). The gate must settle head-on whether this is an
  FD artefact (h-ladder + a second discretisation at that
  site) or a genuine marginal failure; the claim's final
  wording must reflect the settlement exactly.
  Record: `../phase46/CHECKPOINT46.md` (P46-2),
  `../phase46/results/p462_memo.md`,
  `../phase46/results/p462_results.json`,
  `../phase46/results/p462_follow.json`.
- **G8-2 (P46-3)** The attained completion: closing the
  P29-3 constructed bulk lift of the exhibited √-shape
  throat at y_c = 0.30 r₀ with a Z₂ mirror brane makes the
  Phase-43 shortcut an ATTAINED geodesic of an
  everywhere-regular bulk: **gain 0.167** (bulk 5.2304 vs
  brane 6.2784 r₀/c; u_eff = 1.200c; Kretschmann finite
  along the path, ≤ 2.21×10³/r₀⁴), priced at one
  pre-existing tension-like mirror brane (σ ∈ [1.001,
  1.47] over |z| ≤ 3, p ≈ −λ; NEC/WEC/DEC saturated-pass;
  SEC −2.00 = the model's own RS-brane value). Deeper
  mirrors attain more: 0.247 @ y_c = 0.35, 0.349 @ 0.40.
  The two alternative completions (regular core, floored-D)
  attain 0.195 / 0.135 only with NEC-violating bulk matter
  (~10⁶× the audit floor) — relocation, not credited.
  C12: EFFECTIVE ONLY (formation leg unavailable,
  Phase 28); carrier graviton-only. The v1.9.0 statement
  (0.480, unattained) stands untouched; the novel residue,
  if any, is the attained-regular-completion statement for
  an exhibited throat lift.
  Record: `../phase46/CHECKPOINT46.md` (P46-3),
  `../phase46/results/p463_memo.md`,
  `../phase46/results/p463_results.json`,
  `../phase43/CHECKPOINT43.md` (P43-1 + Gate-6 erratum).

## Worker assignments

- W-A: G8-1 (composed configuration + the DEC caveat
  settlement) → `results/wA_g8_1.md`
- W-B: G8-2 (attained completion: gain curve + regularity
  + mirror-brane price) → `results/wB_g8_2.md`

Each worker: correctness FIRST (fresh code in gate8/, run
with system python3 or the venv at
`~/workspace/warp-pilot/venv/bin/python`), then novelty
with logged queries. Each returns per-claim: correctness
verdict + deciding numbers from THEIR run; novelty verdict
+ citations; and, wherever the claim survives only
weakened, the EXACT restated wording.

## Verdicts

### G8-1 — Composed configuration (W-A, 2026-11-22)

Full report: `results/wA_g8_1.md`; fresh code `wa_lib.py`,
`wa_run1–4.py` (4th-order direct-∂² FD, ∂Γ algebraic — the
Phase-1 judge never used as deciding machinery; the judge
was run only as a comparison path); data
`results/wa_g8_1_numbers.json`; search log
`results/wa_search_log.md`.

- **Correctness: REPRODUCED WITH RESTATEMENT.** Anchors
  passed before any claim number: Minkowski max|T| = 0.0
  exactly; Finalist-A calibration worst +5.30×10⁻⁷ (record
  +5.50×10⁻⁷), Type I 1.000. Anatomy exact on the gate
  path: composed lapse at inner mid-wall −0.72178 vs
  −0.28339 alone, e^a ratio 0.64507, W held at 0.066381.
  Verdict row (payload 0.0799, h = 0.15): inner wall
  +9.74×10⁻⁴, outer wall +2.86×10⁻⁵, payload +1.14×10⁻⁴,
  Type-I fraction 1.000, conservation clean (rel. median
  7.8×10⁻³) — the phase's margins reproduced. The phase's
  two other instrument claims both CONFIRMED: the h = 0.3
  payload-region negative flips to +1.14×10⁻⁴ at h = 0.15
  (under-resolution artefact), and the cavity DEC dip is
  a stencil artefact (stencil-clear reads positive).
- **THE CAVEAT — SETTLED: ARTEFACT (representation
  floor), with the floor carried in the wording.** First,
  a correction to the record's framing (found by the
  worker, ratified here): the −3.7×10⁻⁶ focused touch
  sits in the **cavity near-edge shell (4.6 < r < 5)**,
  not the payload region — the payload region reads
  +1.21×10⁻⁵ at that spacing. At the cavity site, fixed-
  site h-ladders are NON-MONOTONE in both machineries
  (phase judge: +5.8×10⁻⁶ → −3.25×10⁻⁵ → −1.90×10⁻⁵;
  gate path: +6.9×10⁻⁶ → −3.95×10⁻⁵ → −2.06×10⁻⁴, with
  radial sign oscillation at fine h — representation
  structure of the spline-of-linear-interpolants metric),
  so NO convergent negative continuum value exists in
  either discretisation and no Richardson limit can be
  quoted; every stencil-clear cavity read is
  +9.98×10⁻⁵ / +1.18×10⁻⁴ / +1.27×10⁻⁴ under refinement,
  Type I 1.000 throughout. The touch is therefore an
  artefact — but refinement does not produce a clean
  continuum DEC value for that thin shell either, so the
  claim's wording (below) names the floor exactly rather
  than asserting a clean value.
- **Boundaries:** the 0.0998 outer-wall failure is
  CONFIRMED in kind and location, with a quantification
  correction: the failing point is Hawking–Ellis
  non-Type-I in BOTH discretisations (sampled NEC
  ≈ −3.4×10⁻⁵; Type-I fraction 0.983 gate / 0.985
  judge); the headline SEC −2.73×10⁻⁴ is the Phase-1
  judge's sampled quantification at a non-Type-I point,
  not a machinery-independent number. Inner wall passes
  (+9.81×10⁻⁴) — the P41-3 inner kill is gone, as
  claimed. The β_o-capped follow-up row (payload 0.0821)
  PASSES on the gate path (inner +9.75×10⁻⁴, outer
  +2.62×10⁻⁵, Type I 1.000); the dual-re-equilibration
  row (0.0729) was not re-run (the capped row was the
  registered spot-check).
- **Novelty: NOVEL.** 11 queries logged verbatim. All
  near neighbours are single-shell (Bobrick–Martire
  arXiv:2102.06824; Fuchs et al. arXiv:2405.02709; Warp
  Factory arXiv:2404.03095; Lentz arXiv:2006.07125;
  Fell–Heisenberg arXiv:2104.06488; Procaccia Oct 2026;
  Le arXiv:2605.25417 et al.). Concentric-shell GR
  exists only as collapse/dynamics theory — no transport
  configuration composing EC-legal shells, and no source
  holding an inner shell's orthonormal shift fixed
  against an outer shell's deepened lapse. Novel part,
  one sentence (worker's §5): "Nesting two individually
  energy-condition-legal warp shells defeats legality
  only through lapse-deepening amplification of the inner
  shell's orthonormal shift, and re-solving the inner
  shell in the composed lapse — coordinate β_i reduced by
  exactly the lapse factor (×0.6451) so the orthonormal
  shift stays at its verified alone value (0.06638) —
  restores full legality at a composed payload of
  0.0799c, above the 0.05c single-shell frontier."
  Coverage gap stated plainly: INSPIRE / Semantic
  Scholar reached only via arXiv-linked indexes, no
  native sessions.
- **GATE VERDICT: UPLOAD-READY AFTER RESTATEMENT** —
  exact restated wording in `results/wA_g8_1.md` §6
  (the floor caveat is part of the claim; follow-up rows
  labelled as such; the 0.0998 failure stated in its
  machinery-independent form; C12 line attached).

### G8-2 — Attained completion (W-B, 2026-11-22)

Full report: `results/wB_g8_2.md`; fresh code
`wb_g82_solver.py`, `wb_g82_israel.py`,
`wb_g82_spotcheck2.py` (Euler–Lagrange geodesic-ODE
shooting, the Gate-6 W-C pattern — the phase's
variational minimiser NOT re-run); data
`results/wb_g82_numbers.json`,
`results/wb_g82_israel.json`,
`results/wb_g82_spotcheck2.json` (a v1 spot check kept
and marked non-deciding); search log
`results/wb_g82_search_log.md`.

- **Correctness: REPRODUCED.** Gates first: flat-RS2
  zero EXACT (rel. err 0.0 vs the ≤ 1e-10 bar); the
  uncompleted record reproduced on the gate path (gain
  0.4799 at cap 0.455 vs the published 0.480). Gain
  curve (gate path): 0.0669 @ y_c = 0.20, 0.1081 @ 0.25,
  **0.1669 @ 0.30 (T = 5.2305 r₀/c, u_eff = 1.200c)**,
  0.2471 @ 0.35, 0.3494 @ 0.40 — every row within
  5×10⁻⁴ of the claim. Regularity: Kretschmann
  ≤ 2.21×10³/r₀⁴ along the attained path at y_c = 0.30,
  finite; the y* ≈ 0.4675 r₀ singularity is cut off by
  the completion, as claimed. **Geodesic honesty
  settled:** D/A has its transverse minimum exactly at
  the mirror interface in the Z₂ double (valley
  confirmed); NO smooth transversal crossing geodesic
  exists (31-slope scan); the gate's folded-space
  optimum agrees with the phase's double-space
  minimisation to 9×10⁻⁵ — so the attainment holds in
  exactly the sense claimed, "valley-floor minimising
  geodesic of the completed space, in the metric-
  geometry sense (smooth arcs joined by the interface
  segment)", and no stronger sense. **Price:** the
  worker's own spline-derivative Israel computation
  (validated at y = 0 to 0.13–0.20%, beating the
  phase's 0.8% validation) gives σ ∈ [1.001, 1.40] with
  the throat peak discretisation-bracketed [1.40, 1.47]
  across methods (the phase's 1.47 is the bracket's top,
  not a discrepancy); NEC +0.00072 saturated-pass,
  WEC/DEC pass, SEC −1.998 — the model's own RS value,
  as claimed. **Alternative-completion spot check
  (deciding):** on the worker's own dense re-evolved
  lift (evolution gate exact to 10⁻¹⁵), the floored-D
  completion's slab NEC_min ≈ −0.40 against the gate
  path's own audit floor −0.0085 (~47×; ~10⁶× the
  phase's finer floor, as reported) — NEC-violating
  bulk matter confirmed NOT phase-specific; the
  relocation verdict stands.
- **Novelty: PARTIALLY KNOWN.** 9 queries logged
  verbatim. Known: the shortcut concept + measurements
  (Chung–Freese arXiv:hep-ph/9910235; Caldwell–Langlois
  arXiv:gr-qc/0103070; Abdalla et al.; Leach–Lesame
  arXiv:gr-qc/0502109; Dai–Stojkovic arXiv:2306.04069 —
  Gate-6's map, re-verified); the Z₂/Israel machinery
  (standard RS; e.g. Mukohyama arXiv:hep-th/0006146);
  regular braneworld completions in print for black
  holes (Crispim et al. arXiv:2405.08048; Estrada et al.
  arXiv:2410.06189) and with bulk fluids (review
  arXiv:2110.15079); two-brane RS wormhole SOLUTIONS
  (McFadden–Turok arXiv:hep-th/0412109; Kar–Lahiri–
  SenGupta arXiv:1505.06831) pose no bulk-geodesic
  timing problem. Not found: a regular completion of a
  constructed wormhole-throat bulk lift in which the
  cross-throat shortcut becomes an ATTAINED minimiser
  with a measured gain, priced by the completing
  brane's Israel data. Novel residue, one sentence
  (worker's §6): "What is new here is not the bulk
  shortcut, nor the mirror brane, but their composition
  for an exhibited throat: closing the P29-3
  constructed bulk lift of the √-shape braneworld
  throat with a Z₂ mirror brane at y_c = 0.30 r₀
  converts the published unattained 0.480 infimum into
  an attained, everywhere-regular minimising geodesic
  of gain 0.167, priced by one pre-existing
  tension-like mirror brane — the first
  attained-regular-completion statement for a
  braneworld wormhole-throat bulk lift." Coverage gap
  stated plainly: INSPIRE-HEP / Semantic Scholar via
  the web index only, no native sessions; non-English
  literature not searched.
- **GATE VERDICT: UPLOAD-READY AFTER RESTATEMENT** —
  exact restated wording in `results/wB_g8_2.md` §7
  (v1.9.0 baseline verbatim-intact; the attained form
  stated as the new content; the mirror peak carried as
  the bracket [1.40, 1.47]; C12 EFFECTIVE ONLY and
  graviton-only carrier hedges attached).

## Closing synthesis (coordinator, 2026-11-22)

**The honest headline: both of Phase 46's new claims
survive independent re-computation — one exactly, one
with its floor named — and the published v1.9.0 statement
is untouched, exactly as its hedges promised.** No claim
needed a NOT REPRODUCED anatomy; the gate's catches are
quantification-level, and both are recorded below rather
than smoothed over.

**Count (claim level, 2 claims):**
- **Survived intact (UPLOAD-READY as stated): 0.**
- **Survived weakened (UPLOAD-READY AFTER
  RESTATEMENT): 2** — G8-1 (configuration reproduced;
  the carried caveat settled as a representation-floor
  artefact, with the floor itself written into the
  claim and the 0.0998 failure restated in
  machinery-independent form), G8-2 (correctness
  REPRODUCED outright; restatement needed only to fix
  the claim's form — the attained statement alongside
  the intact v1.9.0 baseline, the mirror peak as a
  bracket, the attainment in its metric-geometry
  sense).
- **Fell (DEAD AS OURS): 0.**

**Correctness sub-count:** REPRODUCED: G8-2 (every
headline number within 5×10⁻⁴ on a different method;
price validated tighter than the phase's own
validation). REPRODUCED WITH RESTATEMENT: G8-1 (all
verdict-row margins reproduced; the caveat has no
clean continuum value in either machinery — artefact
by sign-instability and stencil-clear reads, floor
named, not hidden).

**Novelty sub-count:** NOVEL ×1 (G8-1 — no composed
EC-legal shell configuration in print; ingredients
known, composition not), PARTIALLY KNOWN ×1 (G8-2 —
ingredients all published; the attained-regular-
completion statement for an exhibited throat lift not
found), KNOWN ×0.

**Errata and follow-ups owed (recorded, not executed
by this gate):**
1. Phase-46 record: the P46-2 caveat's location is the
   **cavity near-edge shell (4.6 < r < 5)**, not the
   payload region as the checkpoint's status log
   phrases it; the payload region reads +1.21×10⁻⁵ at
   h = 0.075. An erratum note belongs in
   `../phase46/CHECKPOINT46.md`.
2. Phase-46 record: the 0.0998 outer-wall figure
   "SEC −2.73×10⁻⁴" is the Phase-1 judge's sampled
   quantification at a non-Type-I point; the
   machinery-independent statement is: worst point
   non-Type-I in two discretisations, sampled NEC
   ≈ −3.4×10⁻⁵, Type-I fraction 0.983–0.985.
3. P46-3's mirror-brane peak σ = 1.47 should be
   carried as the discretisation bracket [1.40, 1.47]
   (gate path: 1.40; phase path: 1.47). No other price
   number changes (SEC −1.998 vs −2.00 is rounding).
4. Ledger entries 31 (P46-2) and 33 (P46-3) can now
   move GATE-QUEUED → gated, in the restated wordings
   only (`results/wA_g8_1.md` §6; `results/wB_g8_2.md`
   §7). Entry 31's carried caveat is settled per
   erratum 1 and the §6 floor clause.
5. Coverage limits (both claims): INSPIRE-HEP /
   Semantic Scholar reached only via arXiv-linked
   indexes / the web index, no native sessions — the
   same bounded gap as Gate-6's G6-1 flag, to be
   closed at write-up time if either claim is
   uploaded.
6. Follow-up (science, not owed by this gate): the
   dual-re-equilibration row (0.0729) was not
   independently re-run; if it is ever promoted from
   follow-up to verdict status it needs its own gate
   read. The cavity shell 4.6 < r < 5 has no clean
   continuum DEC value in the current metric
   representation — a representation with a smooth
   (non-spline-of-linear) cavity profile would settle
   it outright.

**Upload-ready list (standing two-part rule):** G8-1,
G8-2 — each ONLY in its restated wording as recorded
verbatim in the worker reports cited above. Nothing
was uploaded by this gate.

**Status: COMPLETE** (both workers returned; both
claims verdicted; record closed 2026-11-22).

## Status log

- 2026-11-22: gate opened by coordinator; ground records
  read (GATE6.md protocol + G6-3 verdict; CHECKPOINT46 in
  full; CHECKPOINT43 P43-1 + Gate-6 erratum; ledger
  entries 31/33). Protocol pre-registered above BEFORE any
  Gate-8 number was computed. Workers dispatched in
  parallel: W-A = G8-1, W-B = G8-2.
- 2026-11-22: both workers returned; coordinator
  integrated verdicts, closing synthesis, errata and
  follow-ups above. Gate CLOSED. Nothing uploaded.
