# GATE-20 — ADJUDICATION OF P178-1 (G20-1)

Gate coordinator: independent adjudication, run adversarially
(the brief was to BREAK the claim). Date: 2026-11-23.
Verification driver (written for this gate, from the
registrations, not copied from Phase 178's stage scripts or
checker): gate20/work/g20_verify.py; output:
gate20/work/g20_verify_out.json. Frame of record: project
venv + Phase 166 pin. Local-short only; nothing launched;
nothing appended to the ledger. INTERNAL only.

## RUNG 2a — FTL: NO (confirmed)

Nothing in G20-1 touches a superluminal configuration, a
bubble, or transport. The item is the T9 flipped pose's
recovery gate read in a diagonal instrument on a β = 1.1 bed
at validity spin λ_val = 0.019992372183091776. Frontier A
remains 0. The finite-λ question (the flip at λ = 0.1452 in
the untruncated pose) is NOT decided by this pass and is
explicitly outside the claim.

## THE CLAIM (G20-1), as made by Phase 178

P178-1 (FU-P1763-1, SPECULATIVE): GATE PASSES — in the
enriched instrument (E-a: {1, P₂, P₄} × 8 knots, 72
coefficients), a single exhibited field satisfies the
flipped pose's gate simultaneously: exact coupled closure
0.6232117059867903 ≤ 0.63, Δq = (−4.992×10⁻⁶, −1.321×10⁻⁴)
within the 5×10⁻⁴ tolerance, Type-I [False, False], subset
count 52, response sizes inside the trust cap (max field
value 0.001318 vs 0.25).

## VERDICT: **SURVIVES INTACT**

Every deciding read was re-derived by this gate and
reproduces the claimed values bit-exactly or to the stored
precision; the cap, the tolerance, and the counting rules
are the registered ones, fixed before the enriched
instrument existed; the enrichment is a strict extension of
the instrument in which the gate twice failed, verified by
re-reading the old failure through the new instrument and
recovering it identically. The claim's own fences
(SPECULATIVE; instrument scope; finite-λ not decided;
P123-3's milestone unchanged) are part of the claim and are
carried verbatim in the quotable form below.

## THE CHECKS

### (a) The witness: single field; closure reproduces; the cap is the registered cap

- The witness is ONE 72-coefficient field: the vector in
  phase178/work/p1781_state.npz (`d_final`) is bit-identical
  to the vector printed in phase178/results/p1781_results.json
  (max diff 0.0), and every exact read below was evaluated by
  this gate on that single field — no per-clause patchwork.
- Exact coupled closure, re-evaluated by this gate through
  the registered path (Ia re-assembled on the posed metric
  per candidate — `pose_E_coupledIa`; residual in the base
  frame, RMS over the 224 scaled components):
  **0.6232117059867903** — bit-identical to the claim, and
  ≤ 0.63 with margin 0.006788.
- The exact path is genuinely the coupled nonlinear
  evaluation, not the linearisation in disguise: the same
  field's linearised closure (this gate's own SVD of the
  saved coupled Jacobian) is 0.6227068127601647, distinct
  from the exact value; its closure under the FROZEN-Ia
  frame is 13.70 — the coupled read is a different and far
  stricter map (in Phase 171 the frozen witness died
  exactly here, coupled closure 5.071).
- The 0.63 cap is NOT a moved bar: it was registered in
  FU-P1234-B's text (quoted in CHECKPOINT171 §P171-1,
  written before Phase 171 computed) as the near-closure
  stall level, with "the verdict is taken at 0.63", and
  Phase 171's witness-verification form already required
  exact closure ≤ 0.63. Phases 176/178 inherited the number
  unchanged, against the same 56-point subset RMS.
- Controls re-run by this gate: reads at d = 0 reproduce
  the stored q [1.0032717740717199, 1.1029635664194024]
  exactly and count 52; exact closure at d = 0 is
  1.0000000000000422 = RMS(res0) from the saved state;
  the coupled LS floor from this gate's own SVD is
  0.6197514399668285 (bit-identical); the P176-3 floor
  witness's exact closure re-reads 0.6196571998307678
  with Δq (+0.0199, +0.0208) — confirming the floor
  witness is a closure witness only, and the P178-1
  witness is a different field that buys the site reads
  at a slightly higher closure, exactly the registered
  trade.

### (b) Δq, count, Type-I: recomputed; criteria are the registered ones

- This gate's exact reads at the witness: q41 =
  1.0032667816897762, q44 = 1.1028314523056981;
  Δq = (−4.992381943624835×10⁻⁶, −1.3211411370428472×10⁻⁴),
  both |Δq| ≤ 5×10⁻⁴ (Δq44 uses 26% of the tolerance);
  Type-I at sites 41/44 = [False, False]; subset count
  (Σ Type-I over the 56-point subset) = 52. All match the
  claim exactly.
- The criteria are verbatim the registered gate
  (CHECKPOINT163 §P163-1, from p1234_run_record.md):
  (a) fixed-path c₂/survival reldiff ≤ 1×10⁻⁶ vs T9
  stored; (b) full-pose direct read at λ_val — Type-I
  [False, False] exact, count 52 exact, q_r within
  5×10⁻⁴ absolute of the same stored values; (c) response
  sizes exhibited with the response active. No tolerance
  or counting rule was redefined by Phase 178: the
  stored q values, the 5×10⁻⁴ tolerance and the count-52
  rule are identical in Phases 123/163/171/176/178.
- Gate (a) replicated by this gate in its own arrangement:
  c₂ = 0.0009028647947471692 (41) / −0.0011544294511897568
  (44), survivals 0.013652955217293665 / 0.14058890317097553,
  reldiff **0.0** vs T9's stored record at both sites
  (tolerance 1×10⁻⁶). Pure-JSON cross-check: the claimed
  values are digit-identical to phase97's t9_results.json.

### (c) Sizes / trust cap: verified — the witness does not pass by being large

Recomputed by this gate from the witness vector:
‖d‖₂ = 0.18087836878121485; max |coeff| =
0.14320434982453112; max field value at the subset points
= 0.0013184603821767068 — 190× inside the solver's
trust-region cap 0.25. Singular content: fraction of
‖d‖² below σ_cut = 0.9971746120746057 (this gate's own
SVD projection), with σ_cut itself recomputed from the
registered formula η_J·(√224 + √72), η_J =
1.00168500225718 → 23.491427444171965 — the Phase 171
formula at the enriched dimensions, not a re-tuned cut.
Five sub-cut directions (σ = 18.44, 14.74, 10.67, 6.16,
0.898), matching Phase 176's spectrum.

### (d) The P₄ enrichment: legitimate extension, same problem

- The closure operator is literally unchanged: the
  enriched instrument imports Phase 171's read path
  (`residual_frame`, `pose_E_coupledIa`, `reads`,
  `STORED_Q`, scales, res0, the same 56 collocation
  points, the same λ_val expansion point, relief OFF,
  profile at coeff0). The only change is the basis:
  angular {1, P₂} → {1, P₂, P₄} — which is precisely the
  reopening condition Phase 171's UNREACHABLE verdict
  registered ("richer angular content than {1, P₂}, with
  the gate re-registered against the enriched
  instrument"), and Phase 176 did re-register it, with
  gate clauses (a), (b), (c) carried verbatim.
- STRICT-EXTENSION TEST (this gate's deciding probe for
  (d)): Phase 171's coupled floor witness (48
  coefficients, exact closure 0.632732 stored, exact
  Δq +7.06×10⁻³ / +1.84×10⁻²) was embedded into the
  enriched basis with all P₄ coefficients zero. The
  posed metrics agree to max diff **0.0**, and the
  enriched path re-reads the embedded field's exact
  closure as 0.6327322436277067 and Δq as (+0.00706,
  +0.01836) — the old failure reproduces identically in
  the new instrument. The enrichment moved no goalposts
  for old fields; it only added directions (the P₄ slot
  carries the new sub-cut directions).
- Selection discipline: the witness was chosen by the
  a-priori registered rule (minimum linearised coupled
  closure subject to the linearised q_r and
  count-preserving constraints, priced against the
  coupled Jacobian). The one rival solve (linearised
  closure 0.622555) was NOT selected because its
  linearised Δq44 = 5.00002×10⁻⁴ violates the
  constraint — the rule applied as written, not tuned
  on the outcome. The selected field then passed its
  exact reads at iteration 1 of 1.

### (e) Scope: what the pass entitles

The pass certifies exactly this: in the enriched diagonal
instrument, at the gate-(b) configuration fixed for this
gate since Phase 163 (diagonal response field; profile at
coeff0 — its drift is exactly 0.0 on the record; dragging
sector as in the anatomy pose, priced stiff and
first-order-inert by Phase 171), an exhibited field
reproduces the flipped pose's stored full-pose reads
within every registered clause. It is NOT an
untruncated-pose verdict: the finite-λ question (does
the flip survive at λ = 0.1452 in the full pose?) remains
OPEN and undecided, and P123-3's milestone ("LEGAL
FLIPPED POSE — MILESTONE", sector scope, "scan signal
under attack") stands exactly as scoped — this pass
removes its "awaits the full pose" cap at instrument
scope only.

One property noted for the record (not a defect): the
Type-I margins D_r at the witness are small at the two
sites (D_r[44] = −1.040×10⁻⁸, D_r[41] = −2.257×10⁻⁸,
both on the False side) — but this is inherited from
the base pose, not manufactured by the witness (at
d = 0, site 44's margin is already 1.043×10⁻⁸), and the
count is not fragile: exact re-reads under random
coefficient perturbations of norm 1×10⁻⁶ and 1×10⁻⁵
keep count 52, Type-I [False, False] and |Δq| in
tolerance, and flipping point 44 requires a directed
move of norm 0.062 along its own D_r gradient (a third
of the witness's own norm). The clauses are met at the
exhibited field, robustly at any perturbation scale
small compared to the field itself.

## INDEPENDENCE PRICING (stated, per standing orders)

Parts A and C of the verification (vector identity,
norms, σ_cut, SVD floor and singular content, the T9
stored-value comparisons, the strict-extension metric
and closure tests) are this gate's own arithmetic on
stored files. Parts B and D evaluate the exact reads
through the registered gate-path primitives
(p1711_common / p1763_common) — those libraries ARE the
instrument the gate is defined on, shared unchanged by
both failing attempts (Phases 163, 171) and by the
claim; there is no second implementation of the coupled
Ia assembly in the programme, and writing one was
beyond this gate's local-short bound. The gate's
independence therefore rests on: its own driver and
arrangement of every evaluation, the bit-exact
reproduction of both the old failure and the new pass
through one path, and the frozen-vs-coupled contrast
(13.70 vs 0.6232) showing the deciding read is the
registered strict one.

## NOVELTY STATUS (per the claim gate)

No novelty, first, or unique wording is claimed or
granted. G20-1 is a programme-internal numerical
feasibility result: a twice-failed internal recovery
gate passes in a re-registered, strictly enriched
instrument. Its ingredients are all standard or
published (the T9 bed machinery of the programme's
earlier phases; Legendre-polynomial angular enrichment;
least-squares closure with an a-priori constrained
selection rule). No external literature search was run:
the claim makes no assertion about the literature, and
none is quotable. Status: **novelty not claimed — not
found in our search is not applicable; the result is
internal and instrument-scoped by construction.**

## EXACT QUOTABLE FORM (the claim as it survives)

"P178-1 (SPECULATIVE): the flipped pose's recovery gate
PASSES in the enriched diagonal instrument (E-a:
{1, P₂, P₄} × 8 knots). A single exhibited field
(‖d‖₂ = 0.18088, max field value 0.001318 against the
0.25 trust cap, 99.7% of its norm below σ_cut) reads,
exactly and simultaneously: coupled closure
0.6232117059867903 ≤ the registered 0.63 cap; Δq =
(−4.992×10⁻⁶, −1.321×10⁻⁴) against the registered
5×10⁻⁴ tolerance; Type-I [False, False]; subset count
52; gate (a) re-passes at reldiff 0.0. Instrument scope
only — not an untruncated-pose verdict; the finite-λ
question is NOT decided; P123-3's milestone stands
exactly as scoped. Gate-20: SURVIVES INTACT."

## DISPOSITION

- G20-1: SURVIVES INTACT in the quotable form above.
- The finite-λ full-pose read at λ = 0.1452 in the
  enriched instrument (Phase 178's queue item 2) is
  unblocked as a successor registration; it is a new
  item, not a consequence of this verdict.
- No ledger entry appended by this gate.
