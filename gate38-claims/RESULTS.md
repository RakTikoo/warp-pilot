# Gate-38 claims — RESULTS (release v1.29.0)

The semiclassical identification claim set of
Phases 318 and 323, as published in v1.27.0
(Gate-37's set: G37-A, G37-B, G37-C), re-adjudicated
by Gate-38 on the record through Phase 361, and
finalised by the Gate-38 Addendum against
Phase 363 — which localised the Phase 259 ξ⁰
residual's origin in this programme's own Phase 241
driver. Gate-38 ran no new computation; it
adjudicates on the phase record (Phases 355, 361,
363, 365), and the Addendum finalises the set
against Phase 363's verdict. Full gate record:
`GATE38.md` and `GATE38_ADDENDUM.md` in this folder;
the deciding phase records in `sources/`; the
repaired driver in `code/`; file-by-file
provenance in `MANIFEST.md`.

**Count: G37-A FAILS — withdrawn, no quotable
successor and none pending; G38-B SURVIVES in its
Gate-37 wording; G38-C is restated in FINAL form
below (dependence discharged). The block below —
Gate-38 Addendum §2, quoted verbatim — is the ONLY
quotable form of the identification claims from
this release onward.** The v1.27.0 (Gate-37) set may
no longer be quoted in its Gate-37 form. Where
Gate-38 §5 and the Addendum §2 differ, the Addendum
governs.

What the re-adjudication found, in brief: the
attribution at the heart of G37-A — that the
Phase 259 ξ⁰ throat residual (+16.0 in T^r_r at the
Ellis throat) was carried by exactly one printed
number in Décanini & Folacci (2007), a T^r_r printed
as 80/3 where the derived value is 16 — was never
read off the page; it was solved backwards from the
residual, and direct evaluation refutes it:
verbatim printed Eq. (2.23) IS the derived tensor
(80, 16, 112) at the throat (Phase 355, control R2;
re-confirmed Phase 361, CTL-1), print H(6,3)(3) is
the derived tensor (Phase 361, Arm A), and DF's
(3.14)→(3.15) expansion is faithful (Phase 361,
Arm B). Phase 363 then found the residual's true
origin: the programme's own Phase 241 driver —
its monomial function m39 computed the (3.15)
monomial N40 with an index raised from the wrong
Riemann slot, reading (0, +4, 0) at the throat
against the verbatim (0, −8, 0), worth exactly +16
in the stored ξ⁰ T^r_r total (stored 1075/9, true
931/9), which the Stage-4 back-out faithfully
converted into the stored difference. The derived
assembly's closures, the A-throat evaluation, and
the identification's substance never depended on
that cell: REST cancels identically in every
arbitrated difference. Phase 365 repaired the
driver in a versioned copy and restated the
affected record (the stored driver was never
edited; the one-hunk repair diff is bundled in
`sources/`). The stored print-side coefficient 203
is withdrawn as a comparator — it differs from the
derived 187 by exactly the corrupted +16 and was
never a faithful print value. No other claim set
is affected. No wormhole construction, no
traversability claim, and no FTL claim follows
from this set.

The claims below are stated ONLY in Gate-38
Addendum §2's wording, quoted verbatim (the
addendum's §2 blockquote, character-for-character;
diff-verified against `GATE38_ADDENDUM.md` §2 at
assembly).

---
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
