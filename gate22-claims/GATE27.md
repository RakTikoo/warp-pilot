# GATE-27 — FENCE-REVISION GATE: GATE-26'S G26-A FENCE
# ("the trim law as clamped at B := 2.5") RE-EXAMINED
# IN LIGHT OF PHASE 265'S SENSITIVITY READ AND
# PHASE 266'S STOP-FREE CERTIFICATE

Date: 2026-11-24. Adversarial re-judgement, not a phase.
Narrow scope, fixed in advance: this gate decides ONE
question — whether Gate-26's restated G26-A must still
be worded as a claim about the trim law **as clamped at
B := 2.5**, now that a stop-free certificate exists —
and issues the claim set's final wording. It does NOT
re-open Gate-26's other verdicts (G26-B and G26-C stand
as issued, §4), and it does NOT touch the wound pose's
Gate-23 set. Novelty is not in scope (NONE stands, §5).
Frame of record: Phase 166 pin, Gate-19-corrected
tensor, venv python (numpy 2.5.5 / scipy 1.18.1).
Method: Gate-27 re-derived every deciding number from
the stored artefacts of Phases 265/266 with its own
arithmetic (`gate27/work/g27_verify.py` →
`gate27/work/g27_verify_results.json`) — pure JSON
arithmetic on the stored rows; no programme engine was
imported, no phase driver or checker was used as
evidence, and no march was re-run (spot recomputation
at the Gate-23/26 pattern's depth). Independence,
priced on the face: the gate's arithmetic path is
independent of the phases' drivers and checkers at the
arithmetic level (it re-derives from the same stored
rows — the same independence class as Gates 15/19/22/
23/26).

## VERDICT

- **RETIRED WITH A NEW GAP PRICED.** The B := 2.5
  fence is **retired**: Phase 266's certificate
  certifies the same combined-class datum under the
  trim law **unclamped** — no stop parameter anywhere
  in the certified pose — at a later bracket,
  (0.675, 0.68125], and the gate's re-derivation
  confirms the certificate at 0.0 deviation in every
  verdict-carrying field (§2). The claim the fence
  qualified is replaced by **G27-A, which SURVIVES IN
  RESTATED WORDING** (§3): the proposed successor
  wording is correct in substance, and the restatement
  carries the two evidence classes explicitly
  (Gate-23/26 discipline) plus the fences the proposal
  omitted.
- The successor fence, written in the fence's place:
  the certified object's remaining parameter
  dependence is the **fitted coefficient c_trim
  itself**. The bracket's sensitivity to c_trim is
  priced at read grade in §2 (delivery sensitivity
  measured from Phase 265's stored arms; bracket-end
  stability band |δc_trim| ≲ 0.10, ≈ 2% of the
  coefficient; crossing shift ≈ 0.0289 of t per unit
  δc_trim). What is NOT on record — the new priced
  gap — is any estimate of the fit's own parameter
  uncertainty: how far a defensible refit (a different
  fit window or weighting in Phase 248 Part A's
  procedure) would move q₂, hence c_trim. The gap is
  exactly the question whether such a refit could move
  c_trim by ≳ 2%; it is carried in G27-A's wording
  (§3), and it does not impeach the certificate, which
  certifies the pose as posed with the stored
  coefficient.
- **Publication consequence (§4):** G27-A **replaces**
  Gate-26's restated G26-A as the lead sustainment
  entry in the v1.22.0 bundle's claim list. It does
  not supplement it, and it opens no new version.

No deciding number in Phase 265's or Phase 266's
record failed to reproduce: the Phase 266 Richardson
table recomputes at 0.0 deviation at all nine window
instants, the Phase 265 arm brackets and end margins
recompute exactly, the clamp arithmetic is exact, and
the sensitivity pricing of §2 is computed from the
stored fixed-t rows, not quoted from the memos.

---

## §1. Attack line (1) — the unclamped pose is the
## same pose; the evidence classes re-split

**The pose identity holds.** The clamped and unclamped
laws are the same law with the same datum: a(0) = −0.5
under both; the datum (Phase 169 A-branch, true lock),
the κ = 0.3 director and the C2 rotating headline are
Phase 252/256's unchanged (Phase 266 registration A1,
adopting the pose of Phases 252/256 with the law
unclamped). The two applied laws coincide exactly
wherever the unclamped law has not yet reached −2.5:
a(t) = −0.5 − c_trim·t² = −2.5 at t_clamp(2.5) =
√(2/c_trim) — gate-recomputed 0.617014916018226 from
Phase 265's marched record (the analytic root of the
stored coefficient is 0.6170149292514079; the 1.3×10⁻⁸
difference is the recorded rounding of the marched
stop instant, already priced by Gate-26 §1 at the
1×10⁻⁶ bar). That the reads coincide where the applied
amplitudes coincide is not an assumption: Phase 265's
structural cross-check part (i) — equal-amplitude arm
pairs agree at max deviation **0.0** across all 41
sampled + 8 fixed instants — is stored in
`p2651_results.json` and is the empirical warrant
(gate-read from the stored field).

**The re-split, exactly.** Phase 252's span evidence
(the evidence under Gate-26's restated G26-A) was 27
sampled instants of [0, 0.65] on the 0.025 lattice
plus the refined instant t = 0.65625. Against
t_clamp(2.5) = 0.617015:

- the 25 sampled instants t ∈ {0, 0.025, …, 0.6} are
  rows of **both** poses identically (the applied laws
  agree at every step up to those instants);
- the sampled instants t = 0.625, 0.65 and the refined
  instant t = 0.65625 are rows of the **clamped pose
  only** — the clamp binds from 0.617015, inside
  Phase 252's span.

G27-A rests on **neither** class past the coincidence
point. Its evidence is Phase 266's own, in the two
classes Phase 266's registration §C fixed in advance:

- **Span class:** the 28 sampled instants of
  [0, 0.675] on the standing grid (N_θ = 2881) are
  Phase 265's stored rows for the arms that ARE this
  pose over the whole span — the B = 3.0 arm is
  unclamped until t_clamp(3.0) = 0.6898436476740386
  and the B = 3.5 arm until t_clamp(3.5) =
  0.7556858539654343 (both gate-recomputed from the
  stored coefficient, exact against the stored
  values), so over [0, 0.68125] both arms' applied
  amplitude is the unclamped law itself. Phase 266's
  CTRL-1 reproduced those rows with a **fresh
  unclamped march** at max abs diff **0.0** on every
  compared row (31 sampled instants t ≤ 0.75, both
  bracket ends, 8 fixed-t rows; the stored CTRL-1
  record's pass flag and all four verdict-carrying
  diffs re-read by this gate: 0.0, pass = true). All
  seven clauses hold at all 28 span instants in both
  arms (gate-read from the stored rows); the span's
  binding minimum is NEC_φ = DEC_φ
  **+0.051321249458261775 at t = 0.675**, and the
  non-binding span minima (NEC_ρ = DEC_ρ +1.68125;
  NEC_θ = DEC_θ +1.6875750349885346; WEC
  +2.306493031032269) sit at t = 0 and coincide with
  Gate-26's span minima for the clamped pose — as
  they must, the poses being one pose there.
- **Window class:** the window [0.61875, 0.75] is
  certified by Phase 266's own G3/G4/G5 ladder (§2) —
  no clamped-pose row enters it.

So the new claim's evidence is complete without any
clamped-pose row past t = 0.617015, and the instants
it shares with the old claim's span are the same
pose's rows, not borrowed ones. One sceptical point
priced and dismissed: Phase 266's window top is 0.75,
not the pattern's 0.76875, because a(0.76875) =
−3.6046234051234713 lies outside Phase 265's audited
delivery range [0, −3.5] while a(0.75) =
−3.4550252517534528 lies inside it (gate-recomputed).
That is a **window choice, not a pose parameter**: the
pose is unclamped at every t (its law reaches −3.5
only at t = 0.7556858539654343, past every window
instant), the certified bracket closes at 0.68125
where the applied amplitude is −2.9381010427835257 —
deep inside the audited range — and nothing in the
claim is read past the bracket except the tail
pricing, which carries its own amplitude caveat (§3).
The coverage cap limits how far past the bracket the
window extends; it binds no read the claim makes.

## §2. Attack line (2) — the stop-free certificate
## re-derived; the residual sensitivity lives in
## c_trim, and it is priced

**The certificate reproduces.** Gate-27 recomputed the
per-instant Richardson treatment from the stored
G3/G4/G5 window rows in `p2661_results.json` (NEC_φ
and DEC_φ verified pointwise identical on all three
grids, max abs diff 0.0, so one row serves both, as
the record states). All nine window instants: eight
monotone (p ∈ [3.60, 4.38]), the bottom instant
t = 0.61875 degenerate at the rounding floor under the
registered degenerate case; CERT-1, CERT-2, CERT-3,
CERT-4 all TRUE under the gate's own evaluation. The
straddle is real and exact: **L(0.675) =
+0.05132124946169617 ≥ 0, L(0.68125) =
−0.048044525888048084 < 0** — deviation **0.0** from
the stored limits at float64 precision, and 0.0 at
every other window instant (the gate's maximum L
deviation over the window is 0.0). CERT-4's stored
non-clause bars at the bracket instants re-read:
t = 0.675 — momentum worst 5.551×10⁻¹⁶, flare min
0.11832390561033951, domain R min 0.5920075151570856,
exp(2Φ) min 0.005811244758454283; t = 0.68125 —
4.718×10⁻¹⁶, 0.1171397537959998, 0.5881379704716508,
0.00581124471577311 — all pass; the worst non-binding
G5 minimum over window instants ≤ t_hi is NEC_θ =
DEC_θ +4.202201045205472. And the certified object
demonstrably contains no clamp: the stored G5 window
rows' `a_applied` equals the unclamped law
−0.5 − c_trim·t² at deviation **0.0** at every window
instant (gate-checked), and the results record's law
field reads "a(t) = −0.5 − c_trim*t^2, UNCLAMPED (no
stop parameter)" with no B field present (Phase 266's
checker's no-stop-parameter record check, re-read).

**Character, carried as Phase 266 fixed it in
advance:** this is a **grid-stability** certificate in
Gate-26 §2's sense — worst |d34| =
3.3217872896784684×10⁻¹³ (t = 0.75), worst |d45| =
2.3092638912203256×10⁻¹⁴ (t = 0.725), worst residual
2.109×10⁻¹⁵ (gate-recomputed d34/d45 maxima; residual
as recorded) — the disagreements sit at the float64
rounding floor, the limit coincides with the
finest-grid read, and the p values carry **no
convergence information**. No wording may quote them
as convergence assurance; G27-A's wording (§3)
carries the distinction, as Gate-26's restated G26-A
did for its certificate. The bar was not relaxed and
no CERT condition was waived.

**The B-sensitivity is closed, at verdict grade as
at read grade.** From Phase 265's stored arms
(gate-recomputed): refined brackets B = 1.5 →
(0.59375, 0.6]; B = 2.0 → (0.63125, 0.6375]; B = 2.5 →
(0.65625, 0.6625] with end margins
+0.05279917238250764 / −0.07369468042669158 (the
certified clamped bracket, reproduced); B = 3.0 and
B = 3.5 → (0.675, 0.68125] with identical end margins
+0.051321249458261775 / −0.04804452588981167 and hi
carriers exactly {NEC_φ, DEC_φ} at every arm.
Midpoints recompute to 0.596875, 0.634375, 0.659375,
0.678125, 0.678125 — the certified arm sits exactly
**0.01875** of midpoint from the stop-free bracket,
and the sensitivity saturates (interval rate 0.0 from
B = 3.0). The stop-free bracket Phase 265 read is the
bracket Phase 266 certified: same ends, same
carriers, and the standing-grid end margins agree
with the certificate's limits to the rounding floor
(L − standing read ≤ 3.5×10⁻¹²). Gate-26's priced gap
— "no sensitivity of the bracket to the stop's value
is on record" — is closed: the sensitivity is tabled
in full by Phase 265 and the endpoint of the table is
now certified.

**The residual sensitivity: c_trim, priced at read
grade.** Retiring the stop does not retire parameter
sensitivity in full; it relocates it to the one
parameter the unclamped pose still carries. The law
is extrapolated: c_trim was fitted over [0, 0.475]
(Phase 248 Part A; Gate-26 §4(3b) chain of custody,
carried) and the certified bracket (0.675, 0.68125]
lies outside that window. The gate prices what a
perturbation δc_trim would do, from stored rows only:

- *Delivery sensitivity, measured:* at fixed t, the
  NEC_φ margin's response per unit applied amplitude,
  from Phase 265 arms that differ at that t **only**
  in the applied amplitude (B = 2.5 arm clamped at
  a = −2.5; B = 3.0 arm applying the unclamped law):
  **1.009839** at t = 0.65625, **1.006338** at
  t = 0.6625, **0.999345** at t = 0.675 (gate-computed
  from the stored fixed-t rows and the stored law) —
  the margin responds to amplitude at ≈ 1.0 per unit,
  the s̄-class slope of Phase 265 §5, and the response
  is affine (Phase 265's structural cross-check part
  (ii): both-clamped affine prediction max deviation
  5.30×10⁻¹⁰, stored).
- *Crossing slope:* from the certificate's limits,
  (L(0.68125) − L(0.675))/0.00625 = **−15.8985** per
  unit t; the linearised crossing sits at
  t* = 0.6782280511877113.
- *Perturbation response:* δc_trim shifts the applied
  amplitude by −δc_trim·t²; at the crossing
  (t² ≈ 0.460) with sensitivity ≈ 1.0, the margin at
  fixed t shifts by ≈ 0.460·δc_trim and the crossing
  by ≈ **0.0289·δc_trim** in t. Tabled: δc_trim of
  ±1% (±0.052533782253394716) moves the crossing
  ∓/± **0.00152** — a quarter of the bracket width;
  ±2% → ±0.00304; ±5% → ±0.00760; ±10%
  (±0.5253378225339471) → ±0.01520.
- *Endpoint stability band:* the certified bracket's
  lo end (margin +0.05132124946169617) flips only at
  δc_trim = **−0.11264** and its hi end (margin
  −0.048044525888048084) only at δc_trim =
  **+0.10352** — the bracket **as an interval** is
  stable at read grade to |δc_trim| ≲ 0.10, i.e.
  ≈ **2%** of c_trim = +5.253378225339471 (gate-
  computed: −2.14% / +1.97%). The crossing itself,
  and with it the lead-change ordering of §3,
  persists far outside the band: at δc_trim = −10%
  the crossing still sits at t ≈ 0.663, past the
  wound bracket's 0.5625 by a wide margin and at the
  clamped bracket's own position.

**The new priced gap.** Nothing in the record prices
the other side of that band: Phase 248 Part A's fit
(q₂ = −6.062834985645177, the full quadratic fit's c₂
over [0, 0.475], divided by s̄ = 1.1540830919809508)
is stored as a point value. No residual-based standard
error for q₂, and no spread of q₂ under a different
fit window or weighting, is on record anywhere in
Phases 248/252/256/265/266. The gap is therefore
exactly this: **whether a defensible refit of the
Phase 248 procedure could move c_trim by ≳ 2% is
unanswered on the record.** It is a gap about the
fit's robustness, not about the certificate: Phase
266 certifies the pose with the stored coefficient,
which was fixed in advance of every march it governed
and never adjusted against any bracket (Gate-26
§4(3b), carried). The successor fence in §3 states
the priced sensitivity and names the gap, so no
quotation of G27-A can shed either.

## §3. G27-A — the final wording (quotable form)

The proposed successor wording survives in restated
form: its substance — the unclamped pose, the span,
the certified bracket, the ordering past both prior
certified brackets, the absence of any operational
stop — is verified (§§1–2). The restatement makes the
evidence classes explicit (the Gate-23 defect class,
priced at Gate-26 §3 for the predecessor claim) and
attaches the fences the proposal omitted: the fitted
coefficient's provenance and extrapolation, the §2
sensitivity fence, the tail fence of the Phase 266
certificate, and the standing scope fences.

**G27-A (final wording):** *On the Phase 169 A-branch
throat datum with the true lock, the combined-class
pose (κ = 0.3 wound director + the Phase 245 C2
rotating headline construction, W = 0.2 sin²θ +
CH-PHI-Auu under P-PHI-TRIM-248 — the open-loop trim
law a(t) = −0.5 − c_trim·t² with c_trim =
+5.253378225339471 fitted in Phase 248 Part A to the
composed datum's measured drift and frozen before
every subsequent march, **unclamped: no stop parameter
exists in the pose**) meets every registered throat
clause bar at all 28 sampled instants of [0, 0.675] on
the standing grid (N_θ = 2881; worst clause minima
over the span: NEC_φ = DEC_φ +0.051321249458261775 at
t = 0.675, the span's binding minimum; NEC_ρ = DEC_ρ
+1.68125; NEC_θ = DEC_θ +1.6875750349885346; WEC
+2.306493031032269 — the non-binding minima at t = 0;
rows are Phase 265's stored reads for the arms that
are this pose over the whole span, reproduced by
Phase 266 CTRL-1 at max abs diff 0.0 — a sampled
standing-grid read, not a limit-certified one), and
on the registered window [0.61875, 0.75] its binding
clauses NEC_φ = DEC_φ are limit-certified at every
window instant under per-instant Richardson limits on
G3/G4/G5 at the unchanged 1×10⁻⁶ bar — the three
grids agreeing to worst |d34| =
3.3217872896784684×10⁻¹³, worst |d45| =
2.3092638912203256×10⁻¹⁴, worst residual
2.109×10⁻¹⁵, the limit coinciding with the
finest-grid read (a grid-stability certificate for a
read-level sector, not a measured convergence rate) —
the limits and the G5 reads straddling zero at the
bracket (L(0.675) = +0.05132124946169617,
L(0.68125) = −0.048044525888048084) with no earlier
in-window crossing and every non-binding clause
positive at G5 at every window instant ≤ 0.68125 —
so the pose's first crossing sits at
t ∈ (0.675, 0.68125] on NEC_φ = DEC_φ. The bracket
lies entirely past both prior certified brackets —
the wound pose's (0.55625, 0.5625] (Phase 243 /
Gate-23) and this pose's own clamped certificate
(0.65625, 0.6625] (Phase 256 / Gate-26) — and the
combined-class datum is the programme's longest-lived
throat datum at verdict grade. The interval is
[0, 0.675] at the sampled and window instants named;
no continuum claim between instants is made or
certified. Fences: (i) the coefficient is a fitted
pose parameter with the provenance stated, and the
certified bracket lies outside its fit window
[0, 0.475] — the law is extrapolated there; the
bracket's sensitivity to the coefficient is priced at
read grade (Gate-27 §2: the certified bracket as an
interval is stable to |δc_trim| ≲ 0.10, ≈ 2% of the
coefficient, and the crossing moves ≈ 0.0289 of t per
unit δc_trim), while the fit's own parameter
uncertainty under window/weighting variation is not
on record and no wording may imply the bracket is
robust to a refit beyond the priced band; (ii) tail
reads past the window are not certified — the tail
pricing stands on the face (first exceedance of
1×10⁻⁶ at t = 0.775; stage max
1.6326921098652747×10⁻⁵ at t = 1.0, carrier WEC,
relative 7.363195956559376×10⁻⁶), with its amplitude
caveat: past t = 0.7556858539654343 the tail reads
pose amplitudes beyond Phase 265's audited delivery
range [0, −3.5]; (iii) pose scope and jet scope as
registered — a jet-scope sector superposition,
exhibit ≠ construction; (iv) programme-level
sustainment wording remains gated by the p1592
deciding scan regardless.*

## §4. Publication consequence — G27-A replaces
## G26-A (restated) in the v1.22.0 claim list

**G27-A replaces Gate-26's restated G26-A as the lead
sustainment entry in the v1.22.0 bundle's claim list;
it does not supplement it, and no new version is
opened.** Reasons: (1) it is the same claim line
Gate-26 §5 assigned to v1.22.0 — the wound-throat
sustainment line of Gate-22/Gate-23/Gate-26 — and the
Gate-23/Gate-26 precedent of keeping one coherent
sustainment release stands; (2) the lead entry must
state the line's current verdict-grade position, and
that position is now the stop-free certificate: the
clamped pose's certificate is strictly superseded as
the lead statement (same datum, same instrument, a
later bracket, and the concern its fence named —
robustness to the stop — is the very concern this
gate retires); quoting both as co-leads would present
two certified brackets for one datum with the weaker
fenced by a retired qualification; (3) replacement is
not erasure — the clamped certificate remains of
record in Phase 256 and Gate-26, and G27-A's wording
cites it as a prior certified bracket in the ordering
sentence, exactly as it cites the wound pose's.
(Packaging remains the parent's act, not this gate's.)

**What this gate does not touch.** G26-B stands as
issued: its comparison (the clamped combined-class
bracket lies entirely past the wound pose's
Gate-23-certified bracket; the lead changes hands at
verdict grade) is exact as stated and is not
re-examined here; the ordering sentence inside G27-A
is this gate's own statement, decided on the §1–§2
recomputation, and adds the second comparison
(unclamped past clamped) without amending G26-B.
G26-C stands as issued; one of its clauses described
the then-certified object ("the trim law as clamped
at B := 2.5, … the bracket's sensitivity to the stop's
value unpriced on the record") — as a description of
the lead claim that clause is **superseded** by
G27-A and its fences (the B-sensitivity is priced by
Phase 265 and closed in §2; the residual sensitivity
is the c_trim fence), while G26-C's remaining fences
(tail reads not certified; pose and jet scope;
p1592) carry over unchanged and are restated inside
G27-A's fence text so that no quotation of the lead
claim can shed them. Gate-22's restated
G22-1/G22-2/G22-3 and Gate-23's appended set stand as
recorded there. Phase 243/252/256/265 verdicts stand
for their own poses and scopes.

## §5. Novelty position

Not in scope for this gate, per its brief. Gate-26 §6
and Gate-22 §6 stand unchanged: novelty NONE granted;
no "first", "unique" or "record" wording is granted
or implied for G27-A. ("Longest-lived throat datum at
verdict grade" in G27-A's wording is the programme-
internal comparison of Gate-26's G26-B class —
certified brackets within this record — not a
literature claim.)

## Files

- `gate27/work/g27_verify.py` +
  `g27_verify_results.json` — Gate-27's independent
  re-derivation: the trim-law and clamp arithmetic;
  the Phase 266 Richardson table recomputed from the
  stored G3/G4/G5 window rows (limits, cases, CERT
  booleans, the a_applied = unclamped-law check, the
  NEC_φ/DEC_φ identity); the Phase 265 arm brackets,
  midpoints and fixed-t rows recomputed from the
  stored results; the delivery-sensitivity, crossing-
  slope and c_trim-perturbation pricing of §2.
- No ledger append, no launches, no external contact.
  Nothing outside `gate27/` was edited.
