# Warp Pilot v1.29.0 — Gate-38: correction to the v1.27.0 semiclassical identification set — the misprint attribution is withdrawn; the discrepancy was this programme's own driver defect

This release corrects v1.27.0 (Gate-37's
semiclassical identification set), on the record of
Phases 355, 361, 363 and 365 as re-adjudicated by
Gate-38 and finalised by its Addendum. **G37-A
FAILS and is withdrawn**: the attribution of the
Phase 259 ξ⁰ residual to exactly one printed number
in Décanini & Folacci (2007) is refuted by direct
evaluation — verbatim printed Eq. (2.23) is the
derived tensor — and Phase 363 established the
residual's true origin in this programme's own
Phase 241 driver (monomial function m39, an index
raised from the wrong Riemann slot, worth exactly
+16). **G38-B survives** in its Gate-37 wording,
and **G38-C, in the final form below, is the only
quotable form of the identification claim**: the
derived assembly closes both harness cores exactly
and the Ellis gate coefficient is 187 exactly; the
stored print-side coefficient 203 is withdrawn as a
comparator. The v1.27.0 set may no longer be quoted
in its Gate-37 form. No other claim set is
affected. The bundle is in `gate38-claims/`
(RESULTS.md, MANIFEST.md, GATE38.md,
GATE38_ADDENDUM.md, code/, sources/ — the deciding
records of Phases 355, 361, 363 and 365).

**Correction note (Gate-38 Addendum §3, verbatim):**

**Correction to the semiclassical identification claim set
(v1.27.0)**

We are correcting one claim in this release, and narrowing the
framing of another. The underlying computations stand; what was
wrong is a statement about *where* a discrepancy sits in a 2007
paper by Décanini & Folacci, and we are withdrawing that
statement. The discrepancy turned out to be ours.

**What we published.** The release stated that a leftover
discrepancy (+16, in one component) in a wormhole throat
calculation could be traced to exactly one misprinted number in
that paper: a coefficient that we said was printed as 80/3 where
the correct value is 16. That location was not read off the page.
It was solved for backwards, from the size of the discrepancy,
on the assumption that the neighbouring formulas in the paper
were printed correctly.

**What we have since done.** We extracted the printed formulas
exactly as published (transcribed twice, independently, and
checked term by term) and evaluated them directly, with exact
arithmetic. The formula we named is printed correctly: it gives
16, the correct value, not 80/3. We then tested the two
remaining places the error could have been — the neighbouring
formula, and the paper's own expansion step that combines these
formulas. Both are also correct, and the expansion is faithful
to the last coefficient. Every location in that paper that we
proposed has now been excluded by direct evaluation.

**Where the discrepancy actually came from.** Our own code. The
bookkeeping that assembled the "printed" side of our original
comparison was driven by a table of totals computed by an
earlier programme driver, and one cell of that table was wrong:
a single term in the driver's evaluation of the paper's
combined formula contracted a tensor index from the wrong slot.
At the throat that one cell reads +4 where the term as printed
gives −8, and weighted into the total it is worth exactly +16 —
the entire discrepancy. Our backwards solve then faithfully
converted that corrupted total into the "misprint" we published.
The error was in our evaluation machinery, not in the paper,
and not in our reading of it: every printed value in the chain
has since been re-verified by direct exact evaluation, and the
paper is clean everywhere in the part of it we used. One
separate finding about that paper does stand and is unaffected:
three other formulas in it, tested separately for a different
property, are not conserved as printed. That result concerns
different formulas, was reached by a different test, and has
nothing to do with the discrepancy corrected here.

**What did not change.** The corrected set of formulas still
closes the throat equations exactly, the second throat's
evaluation still holds exactly, and the headline coefficient
still lands on its target value, 187 — none of those results
ever depended on the corrupted cell, which cancels out of every
one of those comparisons identically. (The 203 we originally
quoted on the other side of that comparison was produced
through the same defective cell, so it was never a faithful
value for the published formulas either; we withdraw it as a
comparator.) The residual bookkeeping is now fully explained:
there is no unexplained remainder left over. No black hole
result is affected: we checked, and no widely quoted black hole
datum was ever computed from that paper's formulas (the famous
values all predate it), the tensor in question is in any case
exactly zero around ordinary black holes, and the two later
papers that genuinely build on the paper's expansion use a step
we have now verified is faithful — their numbers do not move.
Separately, a small set of secondary residual figures elsewhere
in our earlier record was computed through the same defective
cell; those figures are being restated as bookkeeping, and none
of them is a claim in this release or affects any claim in it.

**The corrected claim.** The identification claim in this
release should be read in the corrected form issued with this
note: it rests on the corrected assembly's exact closures and
target matches, and makes no claim that a misprint in
Décanini & Folacci (2007) carried the original discrepancy. It
did not. We did.

This correction concerns only the identification claim set in
this release. No other claim set is affected.

**The final claim set (Gate-38 Addendum §2, verbatim):**

> **G37-A — FAILS. No quotable successor, and none is pending.**
> The attribution of the Phase 259 ξ⁰ residual to exactly one
> printed number in Décanini & Folacci's H{2,0}(3) (print
> T^r_r = 80/3 vs derived 16) is refuted by direct evaluation:
> verbatim printed Eq. (2.23) is the derived tensor (Phase 355,
> control R2; re-confirmed Phase 361, CTL-1). The single-carrier
> substance is likewise excluded: print H(6,3)(3) is the derived
> tensor (Phase 361, Arm A) and DF's (3.14)→(3.15) expansion is
> faithful (Phase 361, Arm B). **The residual's origin is
> established and is the programme's own:** the Phase 241
> driver's monomial function m39 computed the (3.15) monomial
> N40 with an index raised from the wrong Riemann slot (slot 0
> instead of slot 2), reading (0, +4, 0) at the Ellis throat
> against the verbatim (0, −8, 0) — worth exactly +16 in the
> stored ξ⁰ T^r_r total (stored 1075/9, true 931/9), which the
> Stage-4 back-out faithfully converted into the stored
> difference REST_print − REST_derived = (0, 8/105, 0)
> (Phase 363: R2 origin; R1 back-out algebra and R3 target side
> cleared in full). No misprint in Décanini & Folacci (2007)
> stands behind the residual, and no attribution of it to any
> printed number in that paper may be quoted.
>
> **G38-B (= G37-B, SURVIVES in its Gate-37 wording).** Derived
> H{2,0}(3) at the A-family throat = **(9/4, 3/4, 21/4)** DF
> print units, exact — Phase 318's registered prediction,
> confirmed by Phase 323's two routes and reproduced by
> Gate-37's third, independent route (divergence exactly 0;
> Ricci lock (0, −1, 1/2)). With it, the A-throat core ξ⁰
> residual (0, +2, −7) is cancelled exactly: REST_derived(A) =
> (−23/5040, −13/5040, −31/5040), Δbracket = (0, −2, +7),
> arbitrated residual (0, 0, 0) — the A-throat arithmetic
> reproduced exactly as a control in Phase 361 (CTL-2), and the
> target side of the original differencing verified in full in
> Phase 363 (R3).
>
> **G38-C FINAL (the identification, restated; dependence
> discharged).** T_S is identified in the registered form only:
> against THA's targets on the harness cores (Ellis + A) and the
> Ellis gate, at all powers, **under the derived assembly** —
> with the derived H tensors substituted, both cores close
> exactly (0, 0, 0); the Ellis gate polynomial's ξ⁰ coefficient
> is 187 exactly, the target value; the root and the NEC roots
> land on target at the targets' printed rounding; the wider-set
> ξ⁰ maxima at C and E collapse under the same substitution; and
> the ξ¹/ξ²/ξ³ sectors stand on Phase 259's certificates. The
> stored print-side comparator is withdrawn: the stored
> difference (0, 8/105, 0) and the stored print-side coefficient
> 203 are both wholly accounted for by the programme's own
> m39 evaluation defect (Phase 363) — the stored ξ⁰ T^r_r total
> exceeded faithful evaluation of printed Eq. (3.15) by exactly
> 16 — and no print-side comparator is asserted. The arbitrated
> closures never depended on that comparator: REST cancels
> identically in every 318/323/Gate-37 arbitrated difference.
>
> **Fences (part of every claim above).** Identification is in
> the registered form only (harness cores Ellis + A and the
> Ellis gate, all powers, derived assembly). Phase 259's D1
> stands in its precise form: the ξ⁰ residual was not a
> transcription or reading artefact — every printed value in
> the chain has been verified by direct exact evaluation
> (Phases 355, 361, 363 R1) — it was an evaluation artefact of
> the programme's own driver, localised to one monomial
> function (Phase 363, R2). The D2 generic-θ gap remains a gap.
> The THA Eq. (26) ξ³ defect stands. No wormhole construction,
> no traversability claim, and no FTL claim follows from this
> verdict. **Defect separation:** Phase 241's indictment of
> DF's H(6,3)(5), (6), (8) as not conserved as printed is a
> separate result about separate tensors, reached by a separate
> test; it is not part of this claim set, is untouched by
> Phases 355–363 and by this gate, and must never be merged
> with the ξ⁰ identification above or with the m39 mechanism,
> which is a defect in this programme's code and in nothing of
> Décanini & Folacci's.

**Figures note.** The figures gallery's Gate-37
figure (`figures/`, drawn from the Phase 318/323
records) depicts the SUPERSEDED claim set and is
retained as part of the record.

**Links.** Concept DOI: 10.5281/zenodo.24425078.
Version DOI: TBD — Zenodo mints it at release.

Disclosure: this is AI-driven analysis — the
computation was produced by an AI research system
working under my direction, and I am posting it
precisely to have its legitimacy checked by humans:
is the argument sound, and is it already known?
Corrections and references are exactly what I am
asking for.
