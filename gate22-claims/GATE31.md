# GATE-31 — Verdict on the Axis A member's certified bracket claim

**Gate:** GATE-31 (certification, Gate-23 pattern). **Frame of record:**
Phase 166 pin, Gate-19-corrected tensor, float64, venv python.
**Instrument:** the Gate-23 certificate as registered for this gate in
`gate31/work/g31_registration.md` — grids G3/G4/G5 (Phase 210 doubling
discipline; every march to T_END = 1.0), per-instant Richardson treatment
on the window straddling the bracket, bar 1×10⁻⁶ (unchanged), CERT-1…4,
controls CTRL-1…4, G5 cost-probe rule. **Inputs of record:** Phase 287
(the member: background family 𝒜(θ), J derived through the O(ρ¹) TOV
identity, Phase 285 δP₂ audit passed — cited, not re-run), Phase 288
(the bracket at read grade, full state stored), Phase 289 (§4b standing
for the class). **Execution:** certification run by a delegated worker
under the registration (`gate31/work/g31_run.py`,
`gate31/work/g31_results.json`, memo `gate31/results/g31_memo.md`,
independent checker `gate31/work/g31_check.py` →
`gate31/results/g31_verify.json`, all_pass = true); the gate re-derived
the Richardson table and all four CERT conditions from the stored
per-grid rows with its own arithmetic (`gate31/work/g31_verify.py` →
`gate31/work/g31_verify_results.json`), reproducing the run's table at
max deviation 5.3×10⁻¹⁷ with no case mismatches and full CERT agreement,
and recomputed the span record from Phase 288's stored rows at deviation
0.0. No ledger append (the parent appends); no computation beyond the
certification reads themselves.

## Verdict

**G31-A: SURVIVES IN RESTATED WORDING.** The certificate holds in full —
CTRL-1 at diff 0.0, the probe passed and G5 ran, CERT-1…4 all hold for
both binding clauses under the gate's own re-derivation — so the bracket
**(0.575, 0.58125] on NEC_φ = DEC_φ is a grid-stability-certified bracket
in the Gate-23/26/27 sense**. The draft wording nevertheless fails in
three named places (§2): the background-consistency phrase is quoted
bare, without the audit's order, floor and guard that constitute it; the
sustain sentence carries no evidence-class split and no sampled-instants
fence; and the pose is identified loosely. The quotable form is G31-A
below. The claim does **not** replace the lead: G27-A as reworded by
Gate-28, with the combined-class certified bracket (0.675, 0.68125],
stands longer (§3). Publication consequence: the claim joins v1.22.0's
claim list as a **companion entry** (§4). Novelty: **NONE** — no
first/unique/record wording is granted; the member's distinction is
programme-internal (§3).

## §1 Attack lines — the certification

**Controls (all evaluated before any certificate condition).** CTRL-1
PASS: fresh reads from the stored member state via `read_arm_A` at the
stored march indices reproduce all 44 stored rows (41 sampled + 3
refinement) at max abs diff **0.0** on clause minima and **0.0** on
mom_resid_max. CTRL-2 PASS: a fresh G4 march reproduces the stored
state's MU/U/MTT at [::40] at 0.0 / 0.0 / 0.0. CTRL-3 PASS: at t = 0.5,
|d34| = 1.1544014455466822×10⁻⁷ and |d45| = 1.3112762875522321×10⁻⁸ for
both binding clauses (gate-confirmed from the stored rows). CTRL-4 PASS:
the three protected engines md5-identical before and after.

**Probe.** G5 [0, 0.05] wall 9.77 s, projection ×20 = 195.4 s ≤ 900 s;
the rule did not fire and G5 ran in full (actual march wall 424.7 s under
shared-CPU contention — recorded; the rule is defined on the projection,
and no deciding number depends on wall time).

**The window.** W = {0.5, 0.525, 0.55, 0.56875, 0.575, 0.58125, 0.5875,
0.6, 0.625, 0.65}; NEC_φ and DEC_φ are identical on every stored row of
every grid (identity max abs diff 0.0), so one table serves both binding
clauses:

| t | case | p | L(t) | r |
|---|---|---|---|---|
| 0.5 | monotone | 3.1381 | +0.6751004999421244 | 1.68×10⁻⁹ |
| 0.525 | monotone | 3.1381 | +0.50010842363026486 | 1.88×10⁻⁹ |
| 0.55 | degenerate | — | +0.29780340763424462 | 6.66×10⁻¹⁵ |
| 0.56875 | degenerate | — | +0.12377399490131591 | 4.00×10⁻¹⁵ |
| **0.575** | degenerate | — | **+0.06131127835593286** | 4.44×10⁻¹⁵ |
| **0.58125** | degenerate | — | **−0.0035507384710418144** | 2.22×10⁻¹⁵ |
| 0.5875 | degenerate | — | −0.07092441075744027 | 4.44×10⁻¹⁵ |
| 0.6 | degenerate | — | −0.21368791441602619 | 1.15×10⁻¹⁴ |
| 0.625 | monotone | 2.9542 | −0.53504641511131878 | 2.63×10⁻¹⁶ |
| 0.65 | degenerate | — | −0.91257323096802834 | 2.98×10⁻¹⁴ |

**CERT conditions (gate-evaluated).** CERT-1 PASS: every window instant
limit-certified for both binding clauses. CERT-2 PASS: L(0.575) =
+0.06131127835593286 ≥ 0, L(0.58125) = −0.0035507384710418144 < 0, with
v5 in the same signs at both instants (at both bracket instants the case
is degenerate and L coincides with v5). CERT-3 PASS: L and v5 ≥ 0 at
every window instant ≤ 0.575 for both clauses — no earlier in-window
crossing. CERT-4 PASS: at G5, at every window instant ≤ 0.58125, the
non-binding clauses stay positive (minima over those instants: NEC_ρ
+0.6431958411458871, NEC_θ +1.7244145462938478, WEC +1.7901544548547463,
DEC_ρ = NEC_ρ, DEC_θ = NEC_θ), and the non-clause bars hold at both
bracket instants (momentum worst 3.61×10⁻¹⁶ ≤ 1×10⁻¹⁰; flare_min
+0.083083 / +0.082390 > 0; domain R_min +0.649070 / +0.645771 > 0;
domain exp(2Φ)_min +0.00190145 > 0, with the registered jpose
substitution J_derived + exp(−2Φ₀)·mtt_a).

**Span record (sampled class).** Over the 24 stored sampled instants
t ∈ [0, 0.575] (standing grid G4; cross-checked against CTRL-1 at diff
0.0), the per-clause minima are: NEC_ρ +0.6692566106027371 (at 0.575),
NEC_θ +1.724057978012409 (at 0), NEC_φ +0.0613112783559302 (at 0.575),
WEC +1.7901543713928072 (at 0), DEC_ρ = NEC_ρ, DEC_θ = NEC_θ, DEC_φ =
NEC_φ. All seven clauses positive at every sampled instant of the span;
the binding minimum is NEC_φ = DEC_φ at the span's end.

**The certificate's character — stated exactly.** This is a
**grid-stability certificate**, in the Gate-23/26/27 sense and no
stronger. Priced per component against the 1×10⁻⁶ bar (Gate-23's margin
lesson: no blanket figure): window worst |d34| = 1.2905218671477314×10⁻⁷
(at t = 0.525), a factor 7.7 under the bar; worst |d45| =
1.465893229024573×10⁻⁸, a factor 68 under; worst r = 1.878×10⁻⁹, a factor
532 under. The window's entire measurable grid disagreement sits at its
two head instants (t = 0.5, 0.525, monotone, p = 3.1381); from t = 0.55
onward — including both bracket instants — the three grids agree at the
float64 rounding floor (|d34|, |d45| ≤ 3×10⁻¹⁴), the bracket limits
coincide with the finest-grid reads, and the limit machinery adds no
information there beyond the G5 read itself. No p value and no margin in
this certificate is a convergence assurance, and none may be quoted as
one.

## §2 Wording rulings — why the draft is restated

**(a) "Background consistent by construction" is not quotable bare.**
The phrase's entire substance is one audit with a stated scope: J was
derived through the O(ρ¹) TOV identity, and the Phase 285 δP₂ audit then
checked that identity's residual against the audit's own per-θ
ladder-error floor, with the Amendment-A1 smoothness guard as part of
the gate. Phase 287's own fence limits the verdict to "the background's
O(ρ¹) TOV-consistency at throat scope, nothing more." A bare
"consistent by construction" would claim more than the audit performed.
The restated wording carries the order, the floor, the numbers and the
guard with the phrase. (The draft's 1.047×10⁻⁶ is the stored
1.047228×10⁻⁶ at its printed precision; the quotable form uses the
stored value.)

**(b) The sampled-instants fence applies, with the evidence classes
split.** The draft's "sustains all seven throat clauses on the sampled
march to a first crossing" reads as a continuum statement and merges two
evidence classes of different strength — the defect class Gate-23's
restated fence exists to prevent. In G31-A the span is stated as what it
is (a sampled standing-grid read at 24 named instants), the bracket as
what it is (limit-certified at the window instants), the non-binding
clauses' window standing is carried by CERT-4 at G5, and the fence
sentence closes the claim verbatim in the Gate-23 form.

**(c) The pose identification is made exact.** The draft's "on the Phase
264 joint pose's background class" blurs what the member is: the joint
pose's sectors are carried unchanged (κ = 0.3 wound director, δμ ≡ +0.25
profile replacement, incumbent att) while its background is *replaced* —
the 𝒜(θ) deformation with J derived. G31-A says so.

**G31-A (quotable, with its fences):**

> *The Axis A member — the Phase 264 joint pose (κ = 0.3 wound director
> + δμ ≡ +0.25 profile replacement, incumbent att) with its background
> deformation replaced by 𝒜(θ) = 0.2 + (−0.5 + 0.15·cos 2θ) and its
> centring term J derived through the O(ρ¹) TOV identity, a background
> TOV-consistent at the audit order by construction (the Phase 285 δP₂
> audit passed at all 181 sampled θ: max |δP₂| = 1.047228×10⁻⁶ against
> the audit's per-θ ladder-error floor, zero of 181 angles above the
> floor, and the smoothness guard satisfied) — sustains all seven throat
> clauses at the sampled instants of its march on [0, 0.575] (worst
> clause minimum +0.0613112783559302, NEC_φ = DEC_φ at t = 0.575), and
> its binding clauses NEC_φ = DEC_φ carry Richardson-extrapolated
> limits L(0.575) = +0.06131127835593286 ≥ 0 and L(0.58125) =
> −0.0035507384710418144 < 0: a grid-stability-certified first crossing
> in (0.575, 0.58125] on NEC_φ = DEC_φ (window worst |d34| =
> 1.2905218671477314×10⁻⁷, |d45| = 1.465893229024573×10⁻⁸, r =
> 1.878×10⁻⁹ against the 1×10⁻⁶ bar; the bracket instants themselves sit
> at the float64 rounding floor). The interval is [0, 0.575] at the
> sampled and window instants named; no continuum claim between
> instants is made or certified.*
>
> *Fences: (i) Stage D form 2 stands for this pose as for the class —
> Phase 289 §4b FAILS UNMOVED (median 0.169177, max 808,773.48, six-row
> table closed) — and the director's on-shell drift along the march
> stands as Phase 288 recorded it (onset 0.050; window maxima 0.027612
> at 0.5, 0.042164 at 0.55, 1.245852 at 1.0; identical to J1's, the
> drift proven background-blind): this certificate certifies the clause
> bracket only and grants no construction wording. (ii) Pose scope:
> this claim concerns the member's seven-clause bracket only; the pose
> remains a jet-scope exhibit of sector superposition on the Phase 264
> joint pose's construction, not a construction. (iii) Director
> statements inherit the director's standing domain fence: the director
> law is degenerate at the south pole (θ = π); all director statements
> concern θ ∈ [0, π). (iv) Programme-level sustainment wording remains
> gated by p1592 regardless of this certificate. (v) The Phase 287
> datum-slice pose read (binding NEC_φ = +1.015422) and this claim's
> march-slice reads are different slices of one pose and are never
> joined.*

## §3 The claim's standing

G31-A does not replace the lead and does not compete with it. The lead
of the sustainment line remains **G27-A as reworded by Gate-28** — the
combined-class certified bracket (0.675, 0.68125], standing longer, its
c_trim caveat carried as Gate-28 ruled. G31-A certifies a different
pose on a different line of the programme (the Axis A background
redesign of the joint pose), with a shorter bracket; replacement logic
(Gate-27 §4) applies within a claim line, not across poses. The
member's distinction is real but **programme-internal**: within the
programme's own record, this is the first bracket certified at verdict
grade on a background that is TOV-consistent at the audit order by
construction rather than numerically consistent at the datum. Stated
that way — as a fact about the programme's record, not about the
literature — it is exact; any shorter form ("first certified bracket on
a consistent background") is not quotable. Novelty against the
literature: **NONE** (Gate-22 §6 discipline). Certification changes
nothing else on the record: Stage D form 2 stands (§2 fence (i)), the
§4b six-row table stays closed, p1592 still gates programme-level
sustainment wording, and the member's Stage D position is otherwise
Phase 289's (admission CLOSED; §4a form 2; Gap 1 as the class's outer
debt).

## §4 Publication consequence

**G31-A joins the v1.22.0 family's claim queue as a companion entry** —
appended to the release's claim list in the restated wording above,
fences included — and is not record-only. Reasons, by the pattern of
Gates 26–28: (1) Gate-23 §5's precedent is that a newly certified claim
set joins the same bundle's claim list as appended entries alongside the
existing set; v1.22.0 is the sustainment bundle and this claim is a
sustainment claim of the same programme, certified by the same
instrument. (2) It is not the lead and opens no new version: Gate-27 §4
replaced a lead only with the same line's stronger form, and Gate-28
kept the lead under a fence rather than demoting it; a shorter bracket
on a different pose neither displaces G27-A nor warrants a bundle of
its own. (3) Record-only is the disposition for claims that fail
certification or survive only as internal measurements; G31-A survived
certification in full, and its substance — a verdict-grade bracket on
an audit-clean background — is exactly the kind of incremental,
correctly-fenced result the claim list exists to carry. Packaging
(tagging, notes, upload) is the parent's act, as with Gates 26–28.

## §5 Incidents, and the gate's rulings on them

Three incidents are recorded on the run memo's face; none touches a
deciding number. (1) Two driver defects (a syntax error, an import-order
error) were caught and fixed before any stage produced numbers; CTRL-1's
diff-0.0 reproduction post-dates them and validates the read path
end-to-end. (2) The first G5 attempt was killed mid-march by an
execution-service restart (SIGTERM; no stage file, no numbers, not an
OOM) and the stage was re-run **unchanged**. Gate ruling: no breach of
the registration — its no-retry rule governs altering settings after a
result; here no result existed to evade, the re-run used the registered
settings in full, and Phase 275 set the identical-relaunch precedent for
infrastructure loss. (3) The probe's projection (195.4 s) understated
the actual G5 wall (424.7 s) under shared-CPU contention; the admission
rule is defined on the projection by the Phase 243 pattern, the actual
wall is recorded above, and the certificate does not depend on either.

## §6 Provenance and artefacts

Registration: `gate31/work/g31_registration.md` (window, controls,
CERT conditions, decision order and verdict forms fixed before any
number existed). Run: `gate31/work/g31_run.py`,
`gate31/work/g31_results.json` (controls, probe, per-grid window rows,
non-clause bars, span record, Richardson table, CERT booleans, walls),
`gate31/results/g31_memo.md`. Independent checker:
`gate31/work/g31_check.py` → `gate31/results/g31_verify.json`
(all_pass = true; Richardson/CERT recomputed at diff 0.0; bracket-instant
G4 spot reads recomputed from the stored member state at diff 0.0).
Gate's own re-derivation: `gate31/work/g31_verify.py` →
`gate31/work/g31_verify_results.json`. Walls: controls 83.7 s, G3 march
20.0 s, G4 march 76.1 s, G5 march 424.7 s, evaluation 0.17 s. Protected
engines md5-identical before/after (CTRL-4). Nothing was written outside
`gate31/`; no ledger append was made by this gate.
