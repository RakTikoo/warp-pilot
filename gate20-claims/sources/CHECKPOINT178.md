# PHASE 178 — CHECKPOINT (coordinator)

Phase 178 executes two items from Phase 176's integrated
follow-up queue: FU-P1763-1 (the third gate attempt,
witness-first, SPECULATIVE) and FU-P1764-1 (the O(ω⁴)
closure in the p_t,tot-adjusted pose). Both
registrations below were written BEFORE any Phase 178
computation ran.

STANDING ORDERS (binding, parent-issued 2026-11-23):
NO heavy compute on this VM — local-short only (staged,
checkpointed, per the Phase 171/176 precedent); heavy
work packaged as Kaggle kernels (controls first), NOT
launched. Frame of record: the project venv
(~/workspace/warp-pilot/venv/bin/python; numpy 2.5.5 /
scipy 1.18.1) + the Phase 166 pin. Corrected
instruments only (fluid_T fixed at Gate-19, divF fixed
at SOURCE FIX 2, true forms). Append-only dated
corrections, prefix-verified. INTERNAL only; nothing
uploaded; nobody contacted; nothing appended to the
ledger by this phase. float64 everywhere.

Queue source: phase176/CHECKPOINT176.md (integrated
follow-up queue items 1 and 4), phase176/results/
p1763_memo.md (the third gate attempt's registered
form), phase176/results/p1764_memo.md §3 (the named
further posed quantity), phase171/CHECKPOINT171.md
(the pose the gate lives in), phase123/CHECKPOINT123.md
(P123-3's milestone the gate serves; P123-1's segment).

---

## REGISTRATIONS (written before computation)

### P178-1 (FU-P1763-1) — THE THIRD GATE ATTEMPT, witness-first (SPECULATIVE)

DESIGNATED SPECULATIVE — the label attaches to this
item, every number in it, and every verdict line,
never softened (T9 line; P176-3's successor
registration, carried verbatim in substance).

STATE. P176-3 enriched the flipped pose's diagonal
instrument to E-a ({1, P₂, P₄} × 8 knots, 72
coefficients) and moved the COUPLED-Ia LS closure
floor to 0.6197514399668285 < the registered cap 0.63
(P171-1's unenriched coupled floor: 0.632948, above
cap; the near-closure set was empty). Its floor
witness is a CLOSURE witness only: exact coupled
closure 0.6196571998307678, Type-I [F, F] ✓, count
52 ✓, but Δq = (+0.019929, +0.020785) — ~40× outside
the gate's 5×10⁻⁴ tolerance. NO gate attempt has
been run in the enriched instrument.

REGISTERED FORM (from p1763_memo.md, verbatim in
substance):
- INSTRUMENT: the enriched E-a instrument as built by
  P176-3 — 3 fields (u, a, b) × 8 spline knots (p641
  grid 8…22) × angular {1, P₂(μ), P₄(μ)} = 72
  coefficients; expansion point d = 0 at λ_val =
  0.019992372183091776, relief OFF, profile at coeff0;
  collocation the same 56-point subset; closure read
  RMS(res) in the solver's scaled frame. The coupled
  E-a Jacobian is on disk (phase176/work/
  p1763_state.npz, p1763_J_coupled_Ea.npz) and is
  reused, not rebuilt.
- DECIDING READ: the COUPLED closure — Ia
  re-assembled on the posed metric per candidate
  (P171-1's coupled form). The frozen linearisation
  is a screen only, never a deciding read.
- WITNESS-FIRST DISCIPLINE (binding): before any gate
  language, EXHIBIT a single enriched field whose
  EXACT coupled reads satisfy ALL of: exact coupled
  closure ≤ 0.63 (direct evaluation, not the LS
  prediction); |Δq_r| ≤ 5×10⁻⁴ at BOTH sites 41 and
  44 vs stored [1.0032717740717199,
  1.1029635664194024], read by the exact gate path
  (p1711_common.reads); Type-I [False, False] at the
  sites; subset count 52 exact. Registered route: the
  linearised count-preserving / q_r-constrained
  optimum over the enriched near-closure set
  (gradients of q41, q44 and of D_r at all 56 points
  wrt the 72 enriched coefficients, central FD in
  P171-1 Stage-B form; count-preserving = linearised
  sign(D_r) preserved at every subset point);
  linearised predictions alone decide nothing — the
  witness is decided by its EXACT reads. If the
  linearised optimum's exact reads miss a clause,
  iterate (re-linearise / correct against exact
  reads) and report the iteration count; a witness
  that cannot be exact-verified is not a witness.
- THE GATE (only with the witness exhibited and
  exact-read): clauses (a), (b), (c) UNMODIFIED,
  verbatim from CHECKPOINT163 §P163-1:
  (a) FIXED-PATH part (identical instrument to
      P104-2's gate): counter-path c₂ at sites 41/44,
      survival fractions 0.013652955217293665 /
      0.14058890317097553, reldiff ≤ 1e-6 vs T9
      stored (the p1631_solver.py gate-stage form;
      P163-1/P171-1/P176-1-era runs reproduced it at
      reldiff 0.0 — re-run, not inherited);
  (b) FULL-POSE DIRECT READ at λ_val (dragging +
      diagonal + profile solves run at λ_val, relief
      NOT active): Type-I [False, False] exact,
      subset count 52 exact, q_r within 5×10⁻⁴
      absolute of stored — read at THE WITNESS (the
      diagonal response exhibited by this item; the
      profile sector at coeff0 and the dragging
      sector as in the anatomy's pose, drift 0.0 on
      the record since P163-1);
  (c) the full-pose response sizes at λ_val
      exhibited: the witness's ‖d‖₂, max |coeff|,
      max field value at the subset points (the
      solver's trust-region quantity, cap 0.25), and
      its singular content (fraction of ‖d‖² below
      σ_cut = 23.4914 at η_J = 1.00168500225718).
  SELECTION RULE, STATED A PRIORI (this registration):
  the witness is the minimum-closure field subject to
  the linearised q_r and count-preserving constraints
  above, with any anchor priced against the COUPLED
  Jacobian (σ_cut = 23.4914) — no selection rule tuned
  on the frozen map (the P171-1 lesson).
  If the gate fails: STOP, report the discrepancy, no
  finite-λ verdict is read off this instrument. No
  tolerance moved, no criterion waived.

VERDICT FORMS (exactly one, checker-verified;
SPECULATIVE throughout):
- GATE PASSES — all clauses (a), (b), (c) hold with
  numbers stated. Milestone-adjacent for the P123-3
  line; flagged plainly — it goes to a Gate. (P123-3's
  milestone stands exactly as scoped regardless; a
  pass here removes its "awaits the full pose" cap at
  instrument scope, nothing more.)
- WITNESS EXISTS, GATE FAILS — the failing clause
  named with its numbers.
- NO GATE WITNESS IN THE ENRICHED POSE — the deciding
  obstruction exhibited (which clause's linearised
  optimum cannot be exact-verified, and the exact
  reads at the best candidate); the line closes
  again, at the enriched level, with the reopening
  condition named.

EXECUTION FORM: local-short staged computation with
checkpointing (the FD gradient sweep is the long
stage, checkpointed per batch, Phase 171 precedent).
If a stage threatens the routing bound it is packaged
as a Kaggle kernel (controls first, NOT launched) and
the item reports the packaged clause as its open part.

### P178-2 (FU-P1764-1) — THE O(ω⁴) CLOSURE IN THE p_t,tot-ADJUSTED POSE

STATE. P176-4 derived the O(ω⁴) diagonal sources of
P123-1's spherical segment and solved the response in
the pose with total tangential stress HELD POSED.
Verdict: FLOOR IS GENUINE (posed-quantity exhaustion)
— the deciding term exhibited: S4's rr l=0 component
(source max 4.96×10⁻⁵) cancels alone (→ 1.01×10⁻¹⁰)
and jointly with tt (→ 6.07×10⁻¹⁰), but once the
θθ/φφ equations enter — equations that exist ONLY
because p_t,tot is held posed — the rr residual
returns to 5.03×10⁻⁵ (88% of source), invariant at
K = 32/48, in both solve forms, and in exact closure.
Floor after closure (exact): tt 5.15×10⁻⁵, rr
6.22×10⁻⁵, θθ 5.41×10⁻⁵, φφ 5.42×10⁻⁵, rθ
2.77×10⁻⁵. Bars at that closure: (iv) STANDS inside
the floor; (v) STANDS digit-identical at
+0.1818181870416408. The further posed quantity was
NAMED by P176-4 §3: an O(ω⁴) adjustment of p_t,tot —
θθ/φφ then become its defining equations.

POSE (this registration — the adjustment, fixed
before numbers):
- The segment, the O(ω⁴) sources S4, the response
  ansatz (modes l = 0, 2, 4; A, B, C per mode; C0 = 0
  gauge; Chebyshev K = 32; P176-4's BCs) and the exact
  closure machinery are P176-4's, reused (phase176/
  work/p1764_*.py). resp1 is P163-2's, ω₃ P171-4's,
  both as stored.
- THE ADJUSTMENT: δp_t(r, θ), an O(ω⁴) correction to
  the total tangential stress, carried in modes
  l = 0, 2, 4 on the same Chebyshev radial basis
  (K = 32), entering the stress side of BOTH
  tangential equations as the SAME adjustment (the
  total tangential stress is one quantity: p_θ,tot
  and p_φ,tot both derive from p_t,tot as in P123-1's
  construction — p_θg = p_t,tot, p_φg = p_t,tot − Φ²
  on the guide side; the worker states the exact
  entry of δp_t into each tangential channel from
  P163-2/P176-4's operator forms BEFORE numbers).
  θθ/φφ are then DEFINING equations for δp_t: at each
  mode, the tangential residuals determine δp_t's
  symmetric part; the θθ−φφ DIFFERENCE equation
  remains a genuine equation for the response fields
  (it carries no δp_t) and is solved, not defined
  away. If the worker's operator anatomy shows the
  adjustment enters the two channels DIFFERENTLY,
  that anatomy is stated and the registration's
  one-quantity discipline applied to the actual
  entry — no silent second adjustment.
- DETERMINACY, STATED BEFORE NUMBERS: per mode, the
  system is tt + rr + rθ (response-determining, as in
  P176-4's probe anatomy) + (θθ−φφ) for the response,
  with δp_t absorbing the tangential mean — the
  worker exhibits the adjusted system's rank /
  σ_min per mode against P176-4's (264/264,
  σ_min 3.44×10⁻² for the held-posed LS system).
- CONSERVATION: the radial conservation law at
  O(ω⁴) involves p_t,tot; δp_t's entry into it is
  stated, and the closure's conservation residual is
  exhibited (Bianchi: if every Einstein equation
  holds to the new floor, the residual must sit at
  that floor — shown, not asserted).

DECIDING READS: (1) the rr l=0 residual in the
adjusted pose (standing at 5.03×10⁻⁵ under the held
pose — THE deciding read); (2) the full per-component
floor after exact closure, P176-4's table form
(max + RMS, before/after); (3) δp_t exhibited: its
size per mode against p_t,tot and against the floor
scale (an adjustment that dwarfs the quantity it
repairs is a re-pose, not a closure — stated if so);
(4) bars (iv) and (v) re-read at the adjusted closure
(P176-4 §6 forms; bar (v)'s guide stress is built
from p_t,tot, so δp_t moves it — margins re-read,
not inherited); (5) restated (i) J, (ii) β_phys,
(vi) QI price if they move.

VERDICT FORMS (exactly one, checker-verified):
- CLOSED AT O(ω⁴) — the adjusted response + δp_t
  exhibited; the new floor stated per component at
  O(ω⁶)-sized remainders (the residual accounting
  then stands complete to that order in the adjusted
  pose); bars (iv)/(v) re-read at the closure.
- FLOOR RELOCATES — the new deciding term exhibited
  (e.g. the θθ−φφ difference equation, or a mode
  whose tangential mean cannot be absorbed), with
  its size and reason.
- NOT POSABLE — the gap named (e.g. the adjustment's
  actual entry into the channels contradicts the
  one-quantity discipline, or determinacy fails),
  with the anatomy.

EXECUTION FORM: local-short (P176-4's longest single
run was ~85 s; the adjusted solve is the same class).
If the full solve exceeds local-short, package the
remainder as a Kaggle kernel (controls first, NOT
launched) and report the packaged clause as the
item's open part.

---

## VERDICTS (integrate incrementally, checker-verified only)

_(coordinator integrates each item's verdict here as its
checker passes; worker memos, results JSONs and checkers
live in phase178/results/, scripts in phase178/work/)_

### P178-2 (FU-P1764-1) — VERDICT: **FLOOR RELOCATES** (checker 20/20 PASS, re-run by the coordinator)

The adjusted pose frees the held pose's deciding term
and the wall moves one channel over, exactly along the
anatomy the registration priced as the risk. Operator
anatomy (stated before numbers, confirmed): δp_t
enters BOTH tangential channels identically as
−8π·δp_t — the tangential MEAN defines δp_t, the
θθ−φφ DIFFERENCE carries none; its conservation entry
is −2(W′+1/r)δp_t. One structural fact: the difference
operator on l=0 response fields is identically zero
(checker: exactly 0.0) — l=0 difference content is
reachable only through the l=2,4 fields' projections.
Controls passed before any adjusted number was
trusted (probe rr0 alone 1.010×10⁻¹⁰, tt+rr
6.072×10⁻¹⁰, held full-posed rr0 5.034×10⁻⁵; held LS
σ_min 3.4440×10⁻², residuals digit-matching P176-4).
Determinacy never fails (adjusted joint 363/363,
σ_min 3.42×10⁻² pointwise / 1.00×10⁻² projected).
- DECIDING READ (rr l=0): FREED — 5.03×10⁻⁵ (held) →
  6.07×10⁻¹⁰ (adjusted probe), 2.26×10⁻⁸ (projected
  joint), 8.77×10⁻⁶ (exact-closure projection).
- NEW DECIDING TERM: the θθ−φφ difference source
  (l=0 max 3.36×10⁻⁵, l=2 max 3.19×10⁻⁵). Cancellable
  alone (→ 1.10×10⁻⁶, all modes), but with tt+rr
  cancelled to ≤ 1.25×10⁻⁶ it stands at diff0
  5.026×10⁻⁵ / diff2 4.865×10⁻⁵ in the projected
  form — the same joint compromise as the held pose
  (5.034×10⁻⁵), one channel over. Exact adjusted
  floor (form A; form B same class): tt 3.46×10⁻⁵,
  rr 2.04×10⁻⁵, θθ 2.85×10⁻⁵, φφ 3.19×10⁻⁵, rθ
  2.42×10⁻⁵ — a factor ~2–3 bought per component,
  NOT O(ω⁶) remainders. Bianchi conservation
  residual 9.69×10⁻⁵ (~3× the floor; no independent
  obstruction).
- δp_t DWARFS WHAT IT REPAIRS (on the verdict's
  face, per the registration's test): field max
  8.47×10⁻⁵ = 6.6× p_t,tot's own max (1.28×10⁻⁵);
  δp_{t,2}(30) = +1.07×10⁻⁴ where the posed stress
  is 0. The adjustment is a re-pose, not a closure.
- BAR (v) FAILS at the adjusted closure: guide
  rebuilt from p_t,tot + δp_t — NEC relative min
  −32115 (form A) / −10293 (form B); absolute NEC
  min −7.13×10⁻⁵ (checker full-grid: rel min
  −69687, abs min −8.47×10⁻⁵), while the checker's
  held-pose control on the same grid reproduces
  +0.1818181870416408 digit-exact. Mechanism: δp_t
  is O(10⁻⁴) in the outer shell where ρ_g → 0 and
  the posed stress vanishes — tangential pressures
  with no density to support them. The held pose's
  bar (v) standing is NOT inherited and NOT re-earned.
- BAR (iv) STANDS inside the relocated floor
  (momentum read 0.0 outright; tt dip 0.40× floor,
  φ dip 0.89× floor). Restated: (i) J = 63.115;
  (ii) β_phys peak 0.45736 at r = 23.93; (vi) QI
  price 0.
- Coordinator's checker re-run: 20/20 PASS (the
  edge-sensitive tt/θθ closure components re-derive
  inside the checker's stated band; rr/φφ/rθ to
  ≤ 0.3%; all deciding reads exact).
Reopening (worker's, on the record): a new
registration posing δp_t WITH the boundary behaviour
of the stress it adjusts (δp_t → 0 where p_t,tot → 0)
and a size discipline — neither was in this
registration and neither was applied retroactively.
Record: phase178/results/p1782_memo.md,
p1782_results.json, p1782_run_record.md,
p1782_checker.py (20/20); scripts + stage files
phase178/work/p1782_*.

### P178-1 (FU-P1763-1) — VERDICT: **GATE PASSES (SPECULATIVE)** (checker 15/15 PASS, re-run by the coordinator)

DESIGNATED SPECULATIVE — the label attaches to this
verdict and every number in it, never softened.
Executed exactly as registered (witness-first). The
third gate attempt PASSES: a gate witness is exhibited
and exact-verified in the enriched (P₄-carrying)
instrument, and the unmodified gate clauses (a), (b),
(c) all hold. Milestone-adjacent for the P123-3 line —
flagged plainly: IT GOES TO A GATE. P123-3's milestone
stands exactly as scoped regardless; this pass removes
its "awaits the full axisymmetric pose" cap at
INSTRUMENT scope only (the enriched diagonal
instrument with the coupled closure as deciding read)
— it is not an untruncated-pose verdict and no
finite-λ verdict beyond the gate is read off it.

- CONTROLS (all exact, diffs 0.0): the saved coupled
  E-a Jacobian reused, not rebuilt — LS floor
  0.6197514399668285; floor witness exact closure
  0.6196571998307678 with Δq (+0.019929, +0.020785),
  Type-I [F, F], count 52; d = 0 reads reproduce the
  stored q and count 52.
- GRADIENTS: central FD h = 1×10⁻³ wrt the 72
  enriched coefficients (1728.6 s, checkpointed):
  ‖g41‖ = 63.657, ‖g44‖ = 178.763 (b-field
  dominated). Structural note: min |D_r| at d = 0 is
  1.043×10⁻⁸ at subset point 44 itself — site 44
  sits essentially on the Type-I boundary, so
  count-preservation is binding there by
  construction; the exact count nevertheless holds.
- THE WITNESS (a-priori rule: minimum linearised
  coupled closure s.t. |Δq| ≤ 5×10⁻⁴ at both sites +
  linearised count-preserving signs; SLSQP from an
  equality-LS start): linearised closure 0.622707,
  linearised Δq ≈ 0. EXACT READS, iteration 1 of 1
  (no correction needed): exact coupled closure
  **0.6232117059867903 ≤ 0.63** (margin 0.006788);
  Δq = (**−4.992×10⁻⁶, −1.321×10⁻⁴**), both inside
  5×10⁻⁴; Type-I [False, False]; subset count 52 —
  ALL CLAUSES SIMULTANEOUSLY. (Honesty notes on the
  memo's face: an LS-start SLSQP reached linearised
  closure 0.622555 but stopped unconverged with
  linearised Δq44 = 5.00002×10⁻⁴ and was NOT
  selected; min-max-|Δq| cross-checks at caps
  0.63/0.625 return t ≈ 0 as corroboration only.)
- GATE: (a) FIXED-PATH — PASS, c₂ and survival
  reldiffs **0.0** at both sites (survivals
  0.013652955217293665 / 0.14058890317097553 vs the
  1×10⁻⁶ tolerance), re-run in p1631_solver.py's
  gate-stage form (pipeline not executed);
  (b) FULL-POSE DIRECT READ — PASS, the witness's
  exact reads above (profile at coeff0, dragging
  sector as in the anatomy pose, relief off);
  (c) RESPONSE SIZES — exhibited: ‖d‖₂ = 0.18088,
  max |coeff| = 0.14320, max field value 0.001318
  (trust-region cap 0.25), 0.99717 of ‖d‖² below
  σ_cut = 23.4914.
- Coordinator's checker re-run: 15/15 PASS — floor,
  controls, linearised stats, the witness's exact
  closure and gate reads, gate (a), and the
  clause-(c) sizes all re-derived from saved state.
Record: phase178/results/p1781_memo.md,
p1781_results.json, p1781_run_record.md,
p1781_checker.py (15/15); scripts + state
phase178/work/p1781_* (witness field in
p1781_state.npz).

---

# PHASE 178 — FINAL SYNTHESIS (coordinator, 2026-11-23)

## The phase question

Phase 176 left two priced debts: a twice-failed
recovery gate whose closure floor had just been
brought under its cap by angular enrichment — with no
field yet shown to hold closure and the gate's site
reads together — and a segment floor whose genuineness
had been traced to a single posed quantity, p_t,tot,
with the adjusted pose named but untried. Phase 178
paid both. One debt clears; the other relocates and,
in relocating, prices its own escape as unusable.

## The answer

1. **The flipped pose's gate passes in the enriched
   instrument** (P178-1, SPECULATIVE). The witness
   exists and is exhibited: one enriched field whose
   exact coupled closure (0.623212) sits under the
   0.63 cap while its exact site reads hold q_r to
   (−5.0×10⁻⁶, −1.32×10⁻⁴), Type-I [F, F], count 52.
   The obstruction that closed this gate twice
   (P163-1, P171-1) was angular starvation, and with
   P₄ content the near-closure set contains a point
   that satisfies every clause at once. The gate
   clauses themselves were never modified; (a)
   re-passes at reldiff 0.0. This is the P123-3
   line's missing full-pose read AT INSTRUMENT
   SCOPE — it goes to a Gate for adjudication, and
   P123-3's milestone stands exactly as scoped in
   the meantime.
2. **The adjusted pose frees the rr term and the
   wall moves to the difference equation** (P178-2).
   δp_t absorbs the tangential mean by definition;
   the θθ−φφ difference, which no scalar adjustment
   can touch, carries the same joint compromise at
   the same size (5.03×10⁻⁵). Worse, the adjustment
   the solve demands is 6.6× the posed stress itself
   and it destroys bar (v) at the segment's edge.
   The O(ω⁴) accounting therefore does NOT close in
   either pose: held pose — floor genuine by
   posed-quantity exhaustion (P176-4); adjusted
   pose — floor relocated, escape priced unusable.
   What would reopen it is named (boundary-faithful,
   size-disciplined δp_t), and it is a new pose, not
   a patch.

## Rung verdicts

**RUNG 2a — FTL: NO (unchanged).** No superluminal
configuration, no bubble, no transport; no joint pass
anywhere; Frontier A remains 0 in every cell.
P178-1's gate pass is wormhole-adjacent INSTRUMENT
scope under a SPECULATIVE label — the flipped pose is
a β = 1.1 bed read at validity-legal spin λ_val, and
the gate certifies that the bed's full-pose reads can
be reproduced by an exhibited response field; it is
not an FTL result of any kind, and the finite-λ
question (the flip at λ = 0.1452 in the untruncated
pose) is NOT decided by it — the gate was the
precondition for reading any finite-λ verdict off
this instrument, and that verdict is a successor
item (queue item 1), not this phase's.

**TRAVERSABLE WORMHOLE: advanced at instrument
scope.** The two-mouth configuration's standing
verdict (Gate-15 G15-1, restated wording; G15-2
pending its kernel) is unchanged. On the T9 line:
P123-3's legal flipped pose (sector scope) now has
its recovery gate PASSED in the enriched instrument
(P178-1, SPECULATIVE) — the pose's full-pose
reproduction is no longer blocked by the closure
obstruction. The directed segment (P123-1) stands
with bars (iv)/(v) intact in the HELD pose; the
adjusted pose is not a segment improvement — it
fails bar (v) and is not adopted.

**RUNG 2b — practical near-c: no change.** Nothing
here reads on the shell or payload marks (programme
best 0.10c / payload 0.09758c standing; Procaccia
0.1363 stands).

**RUNG 1 — new technical results (the phase's
yield):**
- P178-1 (SPECULATIVE): the third gate attempt
  passes — witness exhibited and exact-verified
  (closure 0.623212 ≤ 0.63; Δq −4.992×10⁻⁶ /
  −1.321×10⁻⁴; Type-I [F, F]; count 52), gate (a)
  at reldiff 0.0, response sizes exhibited with
  99.7% of the witness's norm below σ_cut. The
  flipped pose's closure obstruction is closed at
  the enriched level; referred to a Gate.
- P178-2: the relocation anatomy of the O(ω⁴)
  floor — the difference operator's l=0 blindness
  (identically zero), the mean/difference split of
  the tangential pair under a scalar adjustment,
  the joint compromise invariant across both poses
  at 5.03×10⁻⁵, and the pricing of the δp_t escape
  (6.6× the posed stress; bar (v) destroyed at the
  edge). The segment's residual accounting is now
  decided in both registered poses.

## Integrated follow-up queue (for the successor phase)

1. **A GATE for P178-1** (parent calls gates): the
   third gate attempt's PASS (SPECULATIVE) is
   referred for independent gate adjudication —
   the witness, its exact reads, and the enriched
   instrument's provenance (P176-3) are the gate's
   record. No claim from P178-1 is quotable beyond
   "gate-passed at phase level, SPECULATIVE, gate
   adjudication owed" until the Gate rules.
2. **The finite-λ read in the enriched instrument**
   (SPECULATIVE; successor to P178-1, gated on item
   1's disposition or explicitly registered as
   instrument-scope): with the recovery gate passed,
   the full-pose deciding reads at λ = 0.1452 (the
   P123-4 question — does the flip survive a legal
   full pose?) may now be registered against the
   enriched instrument, coupled closure the deciding
   read from the start. P123-3's milestone stands
   exactly as scoped until it lands.
3. **FU-P1712-2** — the source-level replica
   correction, sequenced WITH the p1635_reread
   harvest (parent launches; P163-5's open clause —
   P48-1, P75-4, P82-2, P127-4, P157-3 certified
   neither way until it lands). Carried unchanged
   from Phase 176's queue.
4. **The boundary-faithful δp_t registration**
   (P178-2's reopening): δp_t posed with the
   boundary behaviour of the stress it adjusts
   (δp_t → 0 where p_t,tot → 0) AND a size
   discipline (a registered cap on |δp_t| against
   p_t,tot's scale), re-attempting the adjusted
   closure with bar (v) as a deciding read from the
   start. Lower priority: the difference-equation
   compromise (5.03×10⁻⁵) stands in front of it —
   even a boundary-faithful δp_t does not touch the
   difference source, so the expected yield is a
   bar-(v)-legal adjusted pose at the relocated
   floor, not a closure.
5. **The l=5 dragging refinement** (pose (A) defect
   RMS 0.15532 → priced 0.10816) — rides with any
   future re-derivation of the segment's dragging
   sector; not a standalone item. Carried unchanged.
6. **Guide tail: CLOSED at the P123-2 pose**
   (P176-2). No queue item. Carried unchanged.
7. **Phase 123 items 7–10 carried unchanged**
   (Df_Σ reopenings; the denominator bound by
   certificate; the ensemble-stability registration
   prerequisite; FU-T8-b PARKED).

PHASE 178 STATUS: COMPLETE — both items resolved in
their registered verdict forms (P178-1 GATE PASSES,
SPECULATIVE; P178-2 FLOOR RELOCATES), every checker
re-run by the coordinator (15/15, 20/20). Nothing
appended to the ledger. INTERNAL only; nothing
uploaded; nobody contacted; no Kaggle kernel
launched or needed.
