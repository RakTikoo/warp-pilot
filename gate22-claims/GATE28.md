# GATE-28 — WORDING GATE: G27-A'S FENCE (i) REWORDED
# TO CARRY PHASE 270'S c_trim UNCERTAINTY AS A LIVE
# CAVEAT

Date: 2026-11-24. Adversarial re-judgement, not a phase.
Narrow scope, fixed in advance: this gate issues ONE
piece of text — the reworded fence (i) of G27-A
(Gate-27 §3), replacing its unpriced-gap clause with
Phase 270's measured fit uncertainty as a live caveat.
It does NOT re-open G27-A's certificate statements
(Phase 266's certificate certifies the pose as posed,
with the stored coefficient — untouched), Gate-27's
other verdicts, or any other gate's verdicts. Frame of
record: Phase 166 pin, Gate-19-corrected tensor, venv
python (numpy 2.5.5 / scipy 1.18.1). Method: Gate-28
re-derived every deciding number of Phase 270 by its
own arithmetic on the phase's STORED refit table
(`phase270/results/p270_results.json`) — no refit was
re-run, no engine imported, no march touched
(`gate28/work/g28_verify.py` →
`gate28/work/g28_verify_results.json`). One instrument
of this gate goes beyond re-derivation: §2 applies
Gate-27's measured amplitude response to Phase 266's
stored margin curve to cross-check Gate-27's linearised
crossing range — stored-row arithmetic of the same
class, on the certificate's own rows.

## VERDICT

- **FENCE REWORDED WITH CORRECTIONS.** Phase 270's
  rewording draft (memo §5) is **adopted in substance**:
  its structure, its interval, its two ordering
  statements and its closing sentence are all verified
  (§1) and survive both pricings of the crossing range
  (§2). Three corrections are issued with it, shown in
  §2–§3 and carried in the issued text (§4):
  (1) the draft's gloss "an order of magnitude wider
  than the bracket's priced stability band" is replaced
  by the priced exit amounts — the gloss is exact on
  the lo side (≈ 10.3× the band's lo edge) and overstates
  the hi side (≈ 4.3×); the total interval is 7.4× the
  band's width (§3);
  (2) the locality caveat is made quantitative inside
  the fence and the crossing range is labelled
  indicative, with this gate's curve-based cross-check
  range stated beside the linearised one (§2);
  (3) the draft's intervals are rounded inward at the
  lo ends by ≤ 5×10⁻⁴; the issued text rounds outward
  (priced nil, corrected on the face) (§3).
- The issued fence (i) is a **drop-in replacement** for
  fence (i) inside G27-A's text (§4 gives the complete
  fence (i), retained clauses included). **Publication
  consequence (§6):** the v1.22.0 claim list's lead
  entry (G27-A) has its fence (i) updated in place to
  the issued text; the rest of G27-A — body and fences
  (ii)–(iv) — is unchanged; no new version is opened.
- What survives at full strength after the caveat is
  stated in §5, in one paragraph, as this gate's own
  ruling: the certified bracket for the posed
  coefficient, and the lead over the wound pose robust
  to the full measured fit uncertainty; the
  clamped-vs-unclamped ordering explicitly NOT claimed
  under refit.

No deciding number of Phase 270 failed to reproduce:
the 60-refit distribution, the cross-product total, the
band-membership count and its anatomy, the linearised
crossing range and both ordering checks recompute from
the stored table at float64 precision (§1).

---

## §1. Verification — Phase 270's deciding numbers,
## re-derived from the stored refit table

All figures below are this gate's arithmetic on
`p270_results.json` (the phase's checker PASS 39/39 is
of record but is not this gate's evidence).

**The distribution.** The 60 stored refit rows
recompute exactly: c_trim min **4.116961394770839**,
max **5.654858048437557**, median **4.799039298128982**
— identical to the stored distribution summary; every
stored row satisfies c_trim = −c₂/s̄_registered at max
deviation **0.0**. The Leg-2 δ range recomputes to
**[−1.1364168305686322, +0.40147982309808583]** — it
exits Gate-27's band [−0.11264, +0.10352] on both sides
by itself, as the memo states.

**The total.** From the two stored marginals by the
registered combination rule: |q₂| ∈
[4.751315536043338, 6.526176061254181] (the Leg-2 c₂
range, sign removed) crossed with the Tier-1 divisor
range s̄ ∈ [1.1461834865666987, 1.1602797411747192]
(the three stored Tier-1 summaries: median / mean /
trapezoid) gives c_trim ∈
**[4.094974140661021, 5.693831867010073]**, δc_trim ∈
**[−1.15840408467845, +0.44045364167060175]** —
identical to the stored total. Exits past the band:
lo by **1.04576408467845**, hi by
**0.33693364167060175**. As fractions of the stored
coefficient: **−22.05% / +8.38%**. The Tier-1 divisor
leg alone, δ ∈ [−0.028056459825500646,
+0.036206781513066666], sits inside the band alone —
the exiting leg is the window/weighting spread, as
priced.

**Band membership.** Exactly **5 of 60** refits land
inside the band [5.140738225339471, 5.356898225339471]:
three at window end 0.475 (starts 0.0 OLS — the
registered baseline itself, c_trim =
5.253378225339471, confirmed present as a stored row —
0.0 Huber, and 0.025 Huber) and two at end 0.45 with
the start dropped to 0.05 (OLS and Huber). The memo's
anatomy — "all in the maximal-window corner (end
0.475, or end 0.45 with the start dropped)" — is exact
against the stored rows.

**The end marginals.** At the registered start /
subsetting / weighting, the window end prices as:
0.475 → 5.253378225339471 (baseline); 0.45 →
4.962714725519467 (**−5.53%**); 0.425 →
4.70572147663847 (−10.42%); 0.40 → 4.478378142477985
(−14.75%); 0.375 → 4.2772507316387225 (−18.58%) — the
memo's table, recomputed row by row. The window end
is the driver; even a one-instant end-trim exits the
band.

**Leg 1.** SE(q₂) = **0.22489878172866737** (3.71% of
|q₂|), SE(c_trim) = 0.1948722611841016; the ±1 SE band
[5.05850596415537, 5.448250486523572] exits the
stability band on both sides, so the verdict never
hinged on Leg 1's exclusion — verified. The residual
diagnostics recompute as stored: 4 sign runs,
Durbin–Watson **0.3481079183855556**, declaration
SYSTEMATIC, `enters_total = false`. Ruling on the
draft's silence about Leg 1: **correct, not an
omission.** The SE is a misfit-scale diagnostic of a
deterministic trajectory (Phase 270 §2, repriced
there); carrying it in the claim fence would misstate
it as an error bar. The fence prices the refit spread,
which is the measured quantity.

**The crossing range (linearised instrument).**
Applying Gate-27's slope 0.0289 of t per unit δc_trim
about t* = 0.6782280511877113 to the verified total:
[0.6782280511877113 − 0.033477878047207206,
0.6782280511877113 + 0.01272911024428039] =
**[0.6447501731405041, 0.6909571614319917]** —
identical to the stored range. Ordering checks
recompute: the min crossing clears the wound hi end
0.5625 by **0.08225017314050409** (lead over the wound
pose survives the full range); the range straddles the
clamped bracket — begins **0.01149982685949591** below
its lo end 0.65625, ends **0.02845716143199173** above
its hi end 0.6625 (ordering past the clamped
certificate does not survive). §2 prices the
instrument itself.

## §2. Attack line (1) — the linearisation, priced:
## the fence carries the range as indicative, with
## the curve-based cross-check beside it

Gate-27's 0.0289 slope is a two-leg linearisation:
(i) the margin at fixed t responds to the applied
amplitude at ≈ 1.0 per unit (measured from Phase 265's
arms at three instants: 1.009839 / 1.006338 /
0.999345), and a coefficient shift δ moves the
amplitude at the crossing by −δ·t² ≈ −0.460δ; (ii) the
margin falls through the crossing at the tangent slope
−15.8985 per unit t, read off the certificate's two
bracket limits. Phase 270 applied the product over
δ ∈ [−1.158404, +0.440454] — an amplitude excursion at
the crossing of **0.5328581053863496** (lo) /
0.20260571946814468 (hi), against bracket-end margins
of +0.05132124946169617 / −0.048044525888048084: the
lo excursion is ≈ **10.4× the margin it displaces**.
The question is whether a fence may quote the
resulting range as its quantitative content.

**Leg (i) is well supported.** The amplitude response's
affinity is not a local hope: Phase 265's structural
cross-check verified the affine prediction over its
clamp arms at max deviation 5.30×10⁻¹⁰ (Gate-27 §2,
carried), and those arms differ in applied amplitude
by up to ≈ 1.39 at the crossing's instants — more than
twice the 0.533 excursion the lo end requires. The
measured sensitivities bracket 1.0 within 1%.

**Leg (ii) is the weak leg, and it is priced here.**
Phase 266's stored per-instant limits give the true
margin curve L(t) across the window; its local slopes
(gate-computed) steepen monotonically: −9.463 at
[0.61875, 0.625], −10.985, −13.827, **−15.898524**
across the certified bracket itself — Gate-27's
tangent, re-derived exactly — then −16.818, −18.299,
−21.667, −27.078 at [0.725, 0.75]. The tangent is the
bracket interval's own slope; the curve is shallower
before the bracket and steeper after it, so the
linearised range is biased inward on both ends.
Removing the tangent assumption while keeping leg (i)
— solving L(t) + t²·δ = 0 on the stored limits
(piecewise-linear, sensitivity 1.0) — gives the
curve-based range:

  **[0.6425954500568838, 0.6906103111037827]**

against the linearised [0.6447501731405041,
0.6909571614319917]: the lo end moves earlier by
0.0021547230836203024, the hi end earlier by
0.00034685032820902517. Both ordering conclusions
survive the correction, and the lo-side conclusion is
strengthened: wound clearance **0.08009545005688379**
(curve) vs 0.08225017314050409 (linearised); straddle
of the clamped bracket: below its lo end by
**0.013654549943116212** (curve) vs 0.01149982685949591,
above its hi end by **0.028110311103782704** vs
0.02845716143199173. A consistency check closes the
loop: Gate-27's endpoint band re-derives from the same
instrument at 0.0-class deviation — the lo end flips at
δ = −L(0.675)/0.675² = **−0.11263923064295453** (band:
−0.11264) and the hi end at **+0.1035215775384253**
(band: +0.10352) — the band is a fixed-t statement and
never carried the tangent assumption.

**Ruling.** The fence may carry the crossing range as
quantitative content **only as an indicative,
linearised price with the caveat inside the quotable
text** — which is the form Phase 270's draft already
chose ("(linearised price, locality caveat)") — with
two strengthenings, issued as correction (2): the
caveat is quantified (the lo end extrapolates the
local slope over a margin excursion ≈ 10× the
bracket-end margins), and the curve-based cross-check
range [0.6426, 0.6906] is stated beside the linearised
[0.6448, 0.6910], so no quotation can present either
as a re-computed bracket. Neither range is one: a
bracket under a refit coefficient requires re-marching
under that coefficient, which neither Phase 270 nor
this gate performed. What the fence asserts at full
strength is the two ordering statements, which hold
under both pricings with the clearances above; the
endpoints are the record's pricing instrument applied
to the measured uncertainty, indicative to ≈ ±0.0022
(the curve-vs-tangent spread).

## §3. Attack line (2) — "the single most aggressive
## window choice": fair with its gloss, and the gloss
## is mandatory

The characterisation (Phase 270 checkpoint and memo:
the stored coefficient is "the product of the single
most aggressive window choice in the defensible set")
is attacked from both directions.

**Not misconduct.** The window — the full holding
interval [0, 0.475] with the posed t = 0 point
included — was registered in Phase 248 Part A's
procedure before the fit was run (Gate-26 §4(3b)
chain of custody, carried by Gate-27 §2), and Phase
248 predates the first bracket this coefficient ever
governed by the whole sustainment line: the choice
cannot have been tuned to a target that did not yet
exist, and the coefficient was never adjusted against
any bracket. Phase 270 prices the counterfactual
spread of a fixed, pre-registered procedure (§6 of
its memo); nothing in the stored record contradicts
that, and this gate found nothing either.

**Not innocuous.** Within the defensible set the
stored window is the extreme of the axis that drives
the uncertainty: it takes the latest end the holding
interval allows (end 0.5 is the first FAILED instant,
outside the procedure — Phase 270 §3), and every
end-trim moves the coefficient materially (§1: one
instant, −5.53%, already outside the band). The
stored coefficient ranks **49th of 60** ascending in
the defensible distribution — 48 refits give a
smaller coefficient — and all five in-band refits sit
in its corner (§1). A reader who met the stored
coefficient without this anatomy would reasonably
assume it central; it is in the distribution's top
quintile, on the side that favours a late crossing.

**One precision, priced.** "Most aggressive" is exact
only on the end axis. The stored coefficient is not
the set's maximum: the 11 refits above it **all drop
the start point** (gate-verified: every refit with
c_trim > 5.253378225339471 has window_start > 0; the
set maximum 5.654858048437557 sits at [0.05, 0.475]).
"Aggressive" therefore means, and may only be quoted
as meaning: **maximal window on the driving axis —
the full holding interval, latest end, posed t = 0
point included**. Phase 270's memo carries that gloss
in its verdict section ("the full holding interval
with the posed t = 0 point included"); its checkpoint
headline does not. Ruling: the characterisation
stands, quotable only with the gloss attached.

**Correction (1), the draft's gloss.** "An order of
magnitude wider than the bracket's priced stability
band" is not exact as a bare phrase: the total
interval's width (1.5988577263490527) is **7.40×** the
band's width (0.21616); the excursions past the band
edges are 10.28× (lo: 1.15840408467845 /
0.11264) and 4.25× (hi: 0.44045364167060175 /
0.10352) the respective half-widths. The issued fence
replaces the gloss with the exit amounts themselves
(§4). (Phase 270's own checkpoint headline — "an
order of magnitude past the ±~2% band" — is the
phase's summary of its verdict form, not claim text;
this ruling governs the fence and any quotation of
the characterisation in claim wording.)

**Correction (3), rounding.** The draft's intervals
round inward at the lo ends: δ [−1.158, +0.440] for
[−1.15840408467845, +0.44045364167060175]; c_trim
[4.095, 5.694] for [4.094974140661021,
5.693831867010073] (lo end narrowed by 2.6×10⁻⁵, hi
widened by 1.7×10⁻⁴); crossing [0.6448, 0.6910] for
[0.6447501731405041, 0.6909571614319917] (lo end
narrowed by 5.0×10⁻⁵). Priced nil — three orders
below every deciding margin — and corrected anyway:
the issued text rounds outward (δ [−1.159, +0.441];
c_trim [4.094, 5.694]; linearised crossing [0.6447,
0.6910]; curve-based [0.6425, 0.6907]).

## §4. The issued fence (i) — drop-in replacement
## for fence (i) of G27-A

The text below replaces fence (i) inside G27-A
(Gate-27 §3) in full. Its first sentences are G27-A's
own, retained; the clause Gate-27 left open — "the
fit's own parameter uncertainty under window/weighting
variation is not on record and no wording may imply
the bracket is robust to a refit beyond the priced
band" — is superseded by the live caveat. Fences
(ii)–(iv) of G27-A are untouched by this gate.

**Fence (i) (as reworded by Gate-28):** *(i) the
coefficient is a fitted pose parameter with the
provenance stated, and the certified bracket lies
outside its fit window [0, 0.475] — the law is
extrapolated there; the bracket's sensitivity to the
coefficient is priced at read grade (Gate-27 §2: the
certified bracket as an interval is stable to
|δc_trim| ≲ 0.10, ≈ 2% of the coefficient, and the
crossing moves ≈ 0.0289 of t per unit δc_trim). The
fit's own parameter uncertainty is now measured
(Phase 270, over the registered set of defensible
refits of Phase 248's procedure — window, subsetting
and weighting variations, crossed with the divisor's
Tier-1 summary range): δc_trim ∈ [−1.159, +0.441]
(c_trim ∈ [4.094, 5.694]; −22% / +8.4% of the stored
coefficient), exiting the priced stability band
[−0.11264, +0.10352] on both sides — by 1.046 on the
lo side and 0.337 on the hi side. The stored
coefficient's window — the full holding interval,
latest end, posed t = 0 point included — was
registered in Phase 248 in advance and was never
adjusted against any bracket; it is also the
maximal-window corner of the defensible set (48 of
the 60 defensible refits give a smaller coefficient,
and all 5 refits inside the stability band sit in
that corner). Under the measured uncertainty the
crossing ranges over [0.6447, 0.6910] by the
linearised price (Gate-27's slope applied to the
measured range; indicative, not a re-computed
bracket — the lo end extrapolates the local slope
over a margin excursion ≈ 10× the bracket-end
margins; Gate-28's curve-based cross-check on the
certificate's stored margin curve gives [0.6425,
0.6907]). Under both pricings the lead change over
the wound pose's certified bracket (0.55625, 0.5625]
survives the full range (the lowest crossing clears
its hi end by ≥ 0.080), and the ordering past this
pose's own clamped certificate (0.65625, 0.6625]
does not — the crossing range straddles it, so that
ordering is a property of the stored coefficient and
is not claimed under refit. The certified bracket
(0.675, 0.68125] remains a statement about the pose
with the stored coefficient.*

## §5. Attack line (3) — what survives at full
## strength: the strongest honest form of the lead
## claim as it now stands

After the caveat, the sustainment lead claim stands
at full strength in exactly this form: *Phase 266's
certificate certifies the combined-class pose as
posed — with the stored coefficient c_trim =
+5.253378225339471, fitted in Phase 248 and frozen in
advance of every march it governed — to meet every
registered throat clause bar at the 28 sampled
instants of [0, 0.675] and to cross first at
(0.675, 0.68125] on NEC_φ = DEC_φ, a grid-stability
certificate at the unchanged 1×10⁻⁶ bar; that
certified bracket lies entirely past the wound pose's
Gate-23-certified bracket (0.55625, 0.5625], and the
lead over the wound pose is robust to the fit's
entire measured defensible uncertainty — under every
defensible refit Phase 270 priced, the crossing stays
at or past ≈ 0.6426, clearing the wound bracket's hi
end by at least ≈ 0.080 — while the certified
bracket's exact position, and any ordering between
the stop-free certificate and this pose's own clamped
certificate (0.65625, 0.6625], are statements about
the stored coefficient, not robust to refit, and are
not claimed as such.*

## §6. Publication consequence

**The v1.22.0 claim list's lead entry (G27-A) is
updated in place: its fence (i) is replaced by the
§4 text.** The remainder of G27-A — the claim body
and fences (ii) (tail), (iii) (pose and jet scope),
(iv) (p1592) — stands exactly as Gate-27 issued it,
and Gate-27's replacement ruling (G27-A replaces
Gate-26's restated G26-A as the lead sustainment
entry) is unaffected. No new version is opened: this
is a fence revision within the same claim, of the
same claim line Gate-27 §4 assigned to v1.22.0.
Phase 270's named successor — "a Gate registration
rewording G27-A's fence (i)" — is discharged by this
gate. (Packaging remains the parent's act, not this
gate's.)

**What this gate does not touch.** Phase 266's
certificate and every statement in G27-A about it;
Gate-27's verdicts (the fence retirement, the
evidence re-split, the B-sensitivity closure);
Gate-26's and Gate-23's sets; Phase 248's verdict and
Phase 270's verdict form (THE GAP BITES stands as the
phase issued it — this gate verifies its numbers,
adopts its rewording in substance with the §2–§3
corrections, and rules on its characterisation; it
does not re-try the phase). Novelty is not in scope:
NONE stands (Gate-27 §5, carried).

## Files

- `gate28/work/g28_verify.py` +
  `g28_verify_results.json` — Gate-28's independent
  verification: the 60-refit distribution, row
  identities, band membership and its window anatomy,
  the end marginals, the Leg-1 band and diagnostics,
  the Tier-1 divisor range, the cross-product total
  and exits, the linearised crossing range and both
  ordering checks — all recomputed from Phase 270's
  stored table — plus the stored coefficient's rank
  in the defensible set, the start-drop anatomy of
  the refits above it, and the §2 curve-based
  cross-check (Phase 266's stored per-instant limits,
  local slopes, curve crossings, the re-derived
  endpoint band).
- No ledger append, no launches, no external contact.
  Nothing outside `gate28/` was edited.
