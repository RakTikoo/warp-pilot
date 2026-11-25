# GATE-21 — ADJUDICATION OF PHASE 186 (G21-1, G21-2)

Gate coordinator: independent adjudication, run adversarially
(the brief was to BREAK the claims, and to price the
λ = 0.10 witness's near-null character honestly). Date:
2026-11-23. Verification drivers (written for this gate,
from the registrations, not copied from Phase 186's stage
scripts or checker): gate21/work/g21_verify.py and
gate21/work/g21_verify2.py; outputs:
gate21/work/g21_verify_out.json,
gate21/work/g21_verify2_out.json. Frame of record: project
venv + Phase 166 pin. Local-short only (two driver runs,
≈45 s and ≈95 s); nothing launched; nothing appended to
the ledger. INTERNAL only.

## RUNG 2a — FTL: NO (confirmed)

Nothing in either claim touches a superluminal
configuration, a bubble, or transport. Both claims are the
T9 flipped pose's instrument reads on a β = 1.1 bed at
finite spin λ. Frontier A remains 0.

## THE CLAIMS, as made by Phase 186

G21-1: at finite λ = 0.10, the enriched instrument's
flipped-pose gate read HOLDS: a single exhibited field
passes exactly (coupled closure 0.6233418793559693 ≤ 0.63,
Δq within tolerance, Type-I [False, False], count 52,
max field 0.0425 ≤ 0.25). SPECULATIVE, instrument scope.

G21-2: at λ = 0.1452 the read FAILS STRUCTURALLY (the
unresponded pose flips site 44's Type-I and the count to
53 at d = 0 level, so no count-preserving witness can be
selected), onset bracketed in (0.10, 0.12].

## VERDICTS

- **G21-1: SURVIVES IN RESTATED WORDING.** Every exact
  read reproduces bit-identically (check (a)); clause (v)
  as registered is met. The restatement is a fence, not a
  repair: the witness's near-null character and its
  fallback provenance are material facts about what kind
  of pass this is, they were flagged by Phase 186 itself
  for this gate to price, and the quotable form below
  carries them verbatim. The fence is in §THE CENTRAL
  QUESTION; the deciding analysis is there.
- **G21-2: SURVIVES INTACT.** The deciding d = 0 reads
  reproduce exactly and the discipline argument is sound
  (check (b)). Two refinements/corrections to Phase 186's
  narration are recorded in §CHECKS (b) — the gate's own
  probes tighten the onset bracket to (0.10, 0.11], and
  the phase's "D_r crosses zero" mechanism gloss is
  wrong on its own numbers (the flip is a complex→real
  eigenvalue-pair transition). Neither touches the
  claim's deciding content: the bracket as claimed,
  (0.10, 0.12], is true, and no mechanism was asserted
  in the claim itself.

## THE CHECKS

### (a) The λ = 0.10 exact reads reproduce independently

Path control first: Phase 178's λ_val witness, evaluated
through this gate's path (p186_common res0/scales recipe +
exact_closure), returns coupled closure
**0.6232117059867903 — bit-identical to Gate-20's
adjudicated value.** The gate's path is the registered
path, tied to Gate-20 at 0.0 difference.

On the stored witness (phase186/work/
p186_opt_lam010_state.npz `d_final`; the iteration-2
partial state is bit-identical to it, max diff 0.0), this
gate's own arrangement of the exact reads gives:
coupled closure **0.6233418793559693** (bit-identical to
the claim; margin to the 0.63 cap 0.006658, the same
margin class as Gate-20's 0.006788); q = (0.9923674977779767,
0.9225404112782403) against this gate's recomputed
q(0; 0.10) = (0.9923385740704013, 0.9223100532072909),
so Δq = (**+2.8923707575456703×10⁻⁵,
+2.3035807094939909×10⁻⁴**), both inside 5×10⁻⁴ (Δq44 at
46% of tolerance); Type-I at sites 41/44 = **[False,
False]**; subset count = **52**. One field, every clause,
exact reads — as claimed.

### (b) The λ = 0.1452 failure and the onset bracket

This gate's own d = 0 probes through the λ-parameterised
path (reads at the unresponded pose):

| λ | Type-I 41/44 | count | D_r(44) | q44(0) |
|---|---|---|---|---|
| 0.10 | F/F | 52 | +9.370142207746235×10⁻⁹ | 0.9223100532072909 |
| 0.11 | F/**T** | **53** | +1.3925008485107015×10⁻⁸ | 0.8885926768958734 |
| 0.12 | F/**T** | **53** | +1.900555600555393×10⁻⁸ | 0.8536450237548929 |
| 0.1452 | F/**T** | **53** | +3.431302664974539×10⁻⁸ | 0.762381677464587 |

The full 56-point Type-I arrays at λ = 0.10 and
λ = 0.1452 differ at **exactly one point: index 44** —
the count change 52 → 53 is that point's flip, as
claimed. Site 44 is the ladder's min-|D_r| point at
every probed rung (argmin 44 throughout). The claimed
onset bracket (0.10, 0.12] is confirmed; **this gate's
λ = 0.11 probe tightens it to (0.10, 0.11]** — recorded
as a refinement, not a correction.

The discipline argument is sound: the registered
selection and the correction loop both constrain
sign(D_r) to the d = 0 pattern at the same λ (the
sign constraints are verbatim in both
p1781_stage3_opt.py and its Phase 186 mirror), so at
λ = 0.1452 any selectable witness inherits count 53 and
site-44 Type-I True at linearised level, and the exact
reads are decided against exhibited fields only. A
count-52 witness would require a count-changing
selection, which is not registered. "Fails structurally
under the registered count-preserving discipline" is
the correct verdict form, and the quotable form keeps
that fence.

MECHANISM CORRECTION (narration, not claim): Phase
186's checkpoint glosses the flip as "D_r(44) crosses
zero between λ = 0.10 and λ = 0.12". Its own printed
values contradict this — D_r(44) is positive at every
rung and *grows* (+9.37×10⁻⁹ → +3.43×10⁻⁸). This gate
exhibits the actual mechanism from the flux reads:
Type-I is decided by the mixed tensor's eigenvalue
structure, not by sign(D_r). At site 44, λ = 0.10, the
(t,r) eigenvalue pair is **complex** (eigenvalues
−0.006275 ± 2.891×10⁻⁵ i, with two real eigenvalues
0.005849, 0.006523), so the real-eigenvalue condition
fails and Type-I reads False; at λ = 0.11 and 0.1452
the pair has resolved to **two distinct real negative
eigenvalues** (−0.006291, −0.006260 at 0.11), and
Type-I reads True. The flip is a complex→real
eigenvalue-pair transition at the pose's marginal
point (site 44 sits within 2.9×10⁻⁵ of the exceptional
point at λ = 0.10). D_r — the (t,r) discriminant
(T00+Trr)² − 4T0r² — stays positive throughout because
q44(0) < 1 throughout; it tracks the point's
marginality (min |D_r| on the ladder) but its sign is
not the flip.

### (c) The witness's singular content, recomputed

This gate's own SVD of the stored coupled Jacobian at
λ = 0.10 (224×72): σ_max = 7360.755977842796,
σ_min = 0.035875776548625275, LS closure floor =
**0.6200617243030125** (claim: …124, agreement to
3×10⁻¹⁶), and **16 singular values below σ_cut** =
23.491427444171965 (the registered formula
η_J·(√224 + √72), η_J inherited — not re-tuned),
vs 5 at λ_val. Witness exhibits, recomputed from the
vector: ‖d‖₂ = **4.407427402148757**; max |coeff| =
3.547358374106746; max field value =
**0.042537246320521915** (5.9× inside the 0.25 cap);
fraction of ‖d‖² below σ_cut =
**0.9997605765139753**. All as claimed.

### (d) The fallback path: legitimate, with one narration corrected

- The fallback is the registered procedure, verbatim:
  the line `d_cur = feas[best]['d'] if best_name else
  mint['0.63']['d']` and the exact-read correction loop
  (secant form, ≤ 13 iterations, each iterate exact-read
  and logged) appear identically in Phase 178's
  p1781_stage3_opt.py (line 116) — the script Gate-20
  adjudicated — and in Phase 186's mirror. The Phase 186
  witness is iteration 2 of that loop from the
  min_t@0.63 start (iteration records reproduce: iter 0
  misses (i)/(ii), iter 1 misses (ii), iter 2 passes
  all). No unregistered step was taken.
- The "~4×10⁻⁹" figure is exact: the best min-closure
  SLSQP iterate (from_ls) stopped at linearised
  Δq44 = +5.000039214448932×10⁻⁴, i.e. **3.92×10⁻⁹**
  over the 5×10⁻⁴ tolerance (and 2.9×10⁻⁹ over the
  script's own TOL+10⁻⁹ feasibility filter). All three
  SLSQP starts report non-convergence ("positive
  directional derivative for linesearch").
- CORRECTION to Phase 186's narration: the checkpoint
  says "the linearised min-closure selection's feasible
  set was EMPTY at λ = 0.10". That overstates a solver
  failure as a feasibility fact. This gate recomputed
  the stored min_t@0.63 field's linearised reads from
  the stored Jacobian/gradients: linearised closure
  0.6300000000004269 (at the cap), linearised Δq =
  (+1.3×10⁻¹⁴, −1.7×10⁻¹⁵), linearised count-preserving
  satisfied (min margin +8.85×10⁻⁹). **The linearised
  feasible set at cap 0.63 is non-empty** — the min_t
  cross-check field itself sits in it. What is true:
  the min-closure SLSQP did not converge to a feasible
  optimum from any start, so no linearised *selection*
  was available and the registered fallback start was
  used. The distinction matters because the fallback
  was justified in the phase's text by the stronger,
  false statement; the procedure actually followed
  needed no such justification — it is the registered
  one. This correction does not touch the witness's
  status, which rests on exact reads alone.

### (e) Scope fences: intact

Phase 186's verdict carries its fences verbatim and
this gate confirms them: instrument scope only (the
enriched diagonal instrument rebuilt at each λ, coupled
closure the deciding read, dragging sector as in the
anatomy pose); NOT P123-4's untruncated full
axisymmetric pose; the pose's own full-EC legality at
finite λ NOT read; SPECULATIVE throughout; P123-3's
milestone stands exactly as scoped. The restated
quotable form below adds the character fence; it
removes nothing.

## THE CENTRAL QUESTION — is the λ = 0.10 witness the instrument reading its own slack?

Priced honestly, the answer is: **no — but it is a
different kind of pass from Gate-20's, and the
difference belongs on the claim's face.**

What does NOT distinguish it from Gate-20's witness:

- Near-null carriage in *fraction* is common to both:
  99.976% of ‖d‖² below σ_cut here, 99.7% at λ_val —
  Gate-20 exhibited that fraction and survived the
  claim intact. The sub-cut directions are directions
  of the *coupled* Jacobian: the coupled map prices
  them weakly at linear order, but the deciding read
  is the exact coupled evaluation, and it is not
  fooled. The historical slack witness (Phase 171's
  frozen-map field) died precisely here — linearised
  closure ≈ 0.63-class, exact coupled closure 5.071.
  The λ = 0.10 witness's exact closure (0.62334) sits
  *below* its d=0-linearised closure (0.62524): the
  exact map confirms the pass, it does not expose one.
- Robustness, measured fairly (this gate ran both
  witnesses through the same path at the same scales):
  under random coefficient perturbations of norm 10⁻⁵,
  BOTH witnesses keep every clause (λ = 0.10: Δq44 ≤
  3.1×10⁻⁴; λ_val: Δq44 ≤ 1.8×10⁻⁴). At norm 10⁻⁴,
  BOTH leave the Δq tolerance (λ = 0.10: up to
  9.1×10⁻⁴; λ_val: up to 2.0×10⁻³, with closure also
  failing at 0.669/0.692). The absolute perturbation
  scale the gate's Δq clauses tolerate (~10⁻⁵) is a
  property of the gate's gradients, identical for both
  witnesses. The λ = 0.10 witness is not more fragile
  in the instrument's own units.

What DOES distinguish it:

- Scale: ‖d‖₂ = 4.407 is 24× Gate-20's witness
  (0.181); max field value 0.0425 is 32× (0.00132),
  though still 5.9× inside the registered cap. The
  perturbation tolerance above is ~4×10⁻⁶ of this
  witness's own norm, vs ~10⁻⁴ of the λ_val witness's
  — relative to its own size, this witness sits in a
  proportionally far thinner shell of the coefficient
  space. That is the honest content of "near-null
  carried": the field is large in exactly the
  directions the instrument prices weakly, and its
  physical values stay small only because those
  directions nearly cancel at the subset points.
- Provenance: it is not the a-priori linearised
  selection (which failed to converge — §(d)); it is
  the registered fallback start corrected twice
  against exact reads, and its d=0-linearised reads
  *violate* the selection constraints (linearised
  Δq44 = 2.75×10⁻³, 5.5× the tolerance; linearised
  count margin −8.8×10⁻⁸). The registration provides
  for exactly this ("linearised predictions alone
  decide nothing — the witness is decided by its
  EXACT reads"), so the pass is legitimate under the
  registered rules. But a quotable form that says
  only "the read holds at λ = 0.10" would let a
  reader assume a λ_val-style pass. Hence the
  restatement.

Judgment: a witness carried by near-null directions
is a legitimate pass in this programme *when the
deciding read is the exact coupled evaluation* — that
has been the discipline since Phase 171, and it is
what separates this witness from the slack witness
that discipline killed. The λ = 0.10 pass stands.
Its character — coefficient-large, near-null-carried,
fallback-reached, exact-reads-only — is fenced into
the quotable form.

## INDEPENDENCE PRICING (stated, per standing orders)

This gate's own work: both drivers and the arrangement
of every evaluation; the SVD, floor, singular content,
norms and field values (pure arithmetic on stored
files); the min_t field's linearised constraint status;
the d = 0 λ-probes including the new λ = 0.11 rung; the
eigenvalue-mechanism exhibit; the two-witness robustness
comparison; the script-provenance diff against
p1781_stage3_opt.py. The exact reads themselves
(closure, q, Type-I, count) run through the registered
gate-path primitives (p186_common on p1763_common /
p1711_common, over the p762 flux reads) — those
libraries ARE the instrument the gate is defined on,
shared unchanged by the failing attempts (Phases 163,
171), by Gate-20's claim, and by this one; no second
implementation of the coupled Ia assembly exists in
the programme, and writing one was beyond this gate's
local-short bound. The gate's independence rests on:
its own drivers, the bit-exact reproduction of
Gate-20's λ_val value through its path (0.0
difference), the bit-exact reproduction of every
deciding number in both claims, and two exhibits no
phase produced (the λ = 0.11 probe and the eigenvalue
mechanism).

## NOVELTY STATUS (per the claim gate)

No novelty, first, or unique wording is claimed or
granted. Both claims are programme-internal numerical
feasibility results in a re-registered instrument —
a finite-λ extension and a priced frontier of the
Gate-20 result. Ingredients all standard or published.
No external literature search was run; neither claim
asserts anything about the literature. Status:
**novelty not claimed.**

## EXACT QUOTABLE FORMS

G21-1 (restated — the fence is part of the claim):

"P186-1 (SPECULATIVE): the flipped pose's
enriched-instrument gate read HOLDS at finite
λ = 0.10. A single exhibited field reads, exactly and
simultaneously: coupled closure 0.6233418793559693 ≤
the registered 0.63 cap; Δq = (+2.892×10⁻⁵,
+2.304×10⁻⁴) against q(0; λ = 0.10) inside the
registered 5×10⁻⁴ tolerance; Type-I [False, False];
subset count 52; max field value 0.042537 ≤ the 0.25
trust cap. FENCE (part of the claim): the witness is
coefficient-large and near-null-carried — ‖d‖₂ =
4.407427 (24× the λ_val witness), 99.976% of ‖d‖²
below σ_cut, in an instrument whose coupled Jacobian
has 16 sub-σ_cut directions (5 at λ_val); it was
reached by the registered fallback start (the
min_t@0.63 cross-check field) plus two exact-read
correction iterations, after the linearised
min-closure SLSQP failed to converge (best iterate
3.9×10⁻⁹ over the Δq44 tolerance), and its
d=0-linearised reads do not satisfy the selection
constraints (linearised Δq44 = 2.75×10⁻³) — the pass
is an exact-reads pass, as the registration provides.
It keeps every clause under random coefficient
perturbations of norm 10⁻⁵, the same absolute scale
as Gate-20's λ_val witness (both leave the Δq
tolerance at 10⁻⁴). Instrument scope only; P123-3's
milestone stands exactly as scoped. Gate-21:
SURVIVES IN RESTATED WORDING."

G21-2 (as claimed):

"P186-2 (SPECULATIVE): at λ = 0.1452 the flipped
pose's enriched-instrument read FAILS under the
registered count-preserving discipline: the
unresponded pose itself reads Type-I [False, True]
(site 44) and subset count 53 ≠ 52 at d = 0, so no
witness the registered selection may select can
satisfy clauses (iii)/(iv); onset bracket
(0.10, 0.12] (the gate's own probes tighten it to
(0.10, 0.11]). Instrument scope only. Gate-21:
SURVIVES INTACT."

## DISPOSITION

- G21-1: SURVIVES IN RESTATED WORDING (quotable form
  above; the fence is not optional).
- G21-2: SURVIVES INTACT (quotable form above).
- Two narration corrections to Phase 186's checkpoint
  are recorded in §CHECKS (b) and (d): the flip
  mechanism is a complex→real eigenvalue-pair
  transition at site 44, not a D_r zero-crossing; and
  the linearised feasible set at cap 0.63 was not
  empty — the min-closure SLSQP failed to converge,
  which is a different fact. Neither correction alters
  a verdict.
- Phase 186's remaining queue items (frontier
  refinement inside the bracket — now (0.10, 0.11] on
  this gate's probe; interior full reads; P123-4's
  untruncated question) are unaffected and stand as
  registered.
- No ledger entry appended by this gate.
