# GATE-38 — Re-adjudication of the Phase 318 + Phase 323 claim set (the Gate-37 set) on the record through Phase 361

**Gate:** GATE-38 (re-adjudication; charged at ledger entry 917).
**Set under adjudication:** the Gate-37 claim set — G37-A, G37-B,
G37-C as quoted in `gate37/GATE37.md` §5 — published as release
v1.27.0 of the warp-pilot repo.
**Frame of record:** Phase 166 pin conventions as carried by the
record; exact-rational arithmetic for every deciding read in the
underlying phases.
**Instrument:** this gate ran no new computation. It adjudicates on
the phase record, and it trusts no summary: every deciding link
below was verified in the cited phase records themselves
(`phase355/CHECKPOINT355.md` + `phase355/results/p355_memo.md`;
`phase361/CHECKPOINT361.md` + `phase361/results/p361_memo.md`;
`gate37/GATE37.md`). Where a later phase reproduced an earlier
result as a registered control, that reproduction is the link the
gate relies on.

## Verdict

**(i) G37-A (the attribution — the residual "is carried by exactly
one printed number" in H{2,0}(3)) — FAILS.**
**(ii) G37-B (the A-throat evaluation (9/4, 3/4, 21/4)) — SURVIVES.**
**(iii) G37-C (the identification, registered form only) — SURVIVES
RESTATED** (exact new quotable wording in §5).

The set as published in v1.27.0 may no longer be quoted in its
Gate-37 form: G37-A's quotable wording is withdrawn, and G37-C is
quotable only in the restated form of §5 below. A draft correction
note for the published release is at §6. This gate publishes
nothing and alters no release; the published wording's handling is
Rakshit's decision.

## §1 What changed since Gate-37

Gate-37's deciding read (3) was a **back-out**: it rebuilt
REST_print = (44/135, 4/27, 100/189) exactly from an *implied* print
tensor and the derived H(6,3)(3), H(6,3)(4), and inferred that the
sole difference between print and derived sat in one component of
H{2,0}(3) (T^r_r: 80/3 vs 16, weighted effect exactly the Phase 259
residual +16). Gate-37 §4 recorded, and Phase 318's record had
stated before it, the load-bearing assumption: H(6,3)(3) entered
that arithmetic as a *joint-consistent* set member — it had never
been individually isolated against print, and print H{2,0}(3)
itself was taken from the back-out, not evaluated from the page.

Two phases have since replaced the back-out with direct evaluation:

- **Phase 355** (charged for a different question — the misprint's
  black-hole blast radius) extracted DF Eq. (2.23) verbatim from the
  published paper (two independent transcriptions, term-by-term
  agreement) and evaluated it. Its registered control — ΔH at the
  Ellis throat must equal (0, 32/3, 0), the difference Gate-37's
  back-out implied — **FAILED: ΔH = (0, 0, 0)**. Print H{2,0}(3) ≡
  derived in every point evaluation performed: both arms read
  (80, 16, 112) at the Ellis throat and Gate-37's derived values at
  Ellis ℓ = 1; the generic-jet fit returns all 14 non-g_ab
  coefficients identical to print (residual exactly 0); direct Δ
  evaluations are exactly zero on nine jets (generic ×2, Ellis
  throat, Ellis ℓ = 1, Schwarzschild, RN ×2, Schwarzschild–AdS ×2).
  (Recorded precision caveat, carried from the 355 memo: the g_ab
  sector's coefficients are not separately fit-determined — a
  6-dimensional nullspace confined to that sector — but the
  sector's observable combination vanishes on every jet evaluated.)
- **Phase 361** (the localisation) tested the two remaining
  DF-side candidates, with all controls passing before any new
  evaluation was quoted — including CTL-1 (355's machinery re-run:
  print H{2,0}(3) = derived = (80, 16, 112), Δ = 0) and CTL-2
  (REST_print − REST_derived = (0, 8/105, 0) reproduced exactly;
  bracket (0, 16, 0); 203 − 16 = 187; A-throat REST_derived
  reproduced exactly). Its verdict was **NEITHER**: Arm A — direct
  evaluation of print Eq. (2.26) gives H(6,3)(3) = **(32, 8, 44)**
  at the throat, identical to derived; the sharp single-carrier
  prediction (32, −1, 44) is refuted; ΔH(6,3)(3) vanishes
  identically on six generic jets. Arm B — DF's (3.14)→(3.15)
  expansion, recomputed from (3.14) over the resolved print forms
  of all ten §2 tensors in exact rational arithmetic, reproduces
  printed (3.15) **exactly, term by term** (59 monomials,
  ξ⁰..ξ³); the programme's own stored (3.15) transcription also
  matches fresh print on all 58 entries. Carried amounts:
  a = (0, 0, 0), b = 0.

Cumulative exclusion list (Phase 361 checkpoint §5, verified):
H{2,0}(3) print = derived (355; re-confirmed 361); H(6,3)(3)
print = derived, throat and generic jets (361); H(6,3)(4)
print = derived at the throat (Phase 318, direct evaluation of
printed (2.27)); DF's (3.14)→(3.15) expansion faithful (361); the
programme's (3.15) transcription identical to fresh print (361).
**Every DF-side location candidate for the +16 discrepancy is
excluded, and the single-carrier substance — that the discrepancy
is one printed number somewhere in DF's §2 tensors or their
expansion — is unsupported by the record.**

What has NOT moved: the Phase 259 ξ⁰ residual itself (D1 stands —
it was not a reading artefact); the all-derived assembly (with the
derived tensors substituted, both harness cores close exactly,
(0, 0, 0)); the Ellis gate coefficient move 203 → 187, which is
arithmetic on the programme's own assembly; and the difference
REST_print − REST_derived = (0, 8/105, 0), reproduced as a control
in both 355 and 361. Where REST_print — the print-side aggregate
produced by Phase 259 Stage-4's back-out — actually came from is
now the open question, and it is a question about the programme's
own bookkeeping, not about DF's page: Phase 363 (charged at ledger
entry 915, still running) re-examines R1 (the Stage-4 back-out
algebra and its known-sector subtractions), R2 (the harness's
throat *evaluation* of (3.15) — its transcription is cleared, its
evaluation is a separate artefact), and R3 (the THA target side of
the original differencing).

## §2 Adjudication of G37-A — FAILS

**The claim (Gate-37 §5):** the Phase 259 ξ⁰ throat residual
(+16.0 in T^r_r at the Ellis throat) "is carried by exactly one
printed number": the joint REST arithmetic implies print
H{2,0}(3) = (80, 80/3, 112) against derived (80, 16, 112), the
sole difference T^r_r = 80/3 vs 16, weighted effect exactly 16.

**Evidence chain against it:**
1. Phase 355, Step 3 read R2 (registered control): verbatim print
   Eq. (2.23), double-transcribed, evaluated directly — ΔH(throat)
   = (0, 0, 0), not (0, 32/3, 0). Print H{2,0}(3) at the throat is
   (80, 16, 112): the T^r_r component the claim quotes as printed
   80/3 evaluates from the page as **16**, the derived value.
2. Phase 355 memo §2: the fit and the nine-jet direct evaluations
   (above, §1) — the identity is tensor-level in the fit-determined
   sector, not a throat accident.
3. Phase 361, CTL-1: the identity re-confirmed on a re-run of
   355's machinery before 361 quoted anything of its own.
4. Phase 361, Arms A + B: the fallback positions the claim's
   method would retreat to — the discrepancy carried instead by
   H(6,3)(3), or by DF's expansion into (3.15) — are each excluded
   by direct exact computation (a = (0, 0, 0); b = 0). The claim's
   substance was never only its named component: it was that a
   single printed number in DF carries the residual. No tested
   DF-side carrier exists.

**Why FAILS and not SURVIVES RESTATED:** every clause of G37-A's
quotable form asserts the location or the single-carrier fact.
Both are refuted or unsupported. The residue that survives — the
back-out difference REST_print − REST_derived = (0, 8/105, 0)
exists as programme bookkeeping, reproduced exactly in 355/361
controls — asserts nothing about DF's page, and its origin is
precisely what Phase 363 is re-examining. Dressing that residue in
claim form now would repeat Gate-37's error (quoting a back-out as
a location) one level down. **G37-A therefore has no quotable
successor in this gate.** The negative result itself — every
DF-side candidate excluded by direct evaluation — is quotable
from the Phase 355 and Phase 361 records, which are its proper
home.

**Dependence note:** if Phase 363 localises the origin of
REST_print (in the back-out algebra, the harness's (3.15)
evaluation, or the target side), a future gate may state a new
attribution claim on that record. Until then, no attribution of
the +16 residual to any printed number, tensor, or expansion in
Décanini & Folacci (2007) may be quoted from this programme.

## §3 Adjudication of G37-B — SURVIVES

**The claim (Gate-37 §5):** derived H{2,0}(3) at the A-family
throat = **(9/4, 3/4, 21/4)** DF print units, exact — Phase 318's
registered prediction, confirmed by Phase 323's two routes and
reproduced by Gate-37's third, independent route (divergence
exactly 0); with it, the A-throat core ξ⁰ residual (0, +2, −7) is
cancelled exactly (REST_derived(A) = (−23/5040, −13/5040,
−31/5040); Δbracket = (0, −2, +7); arbitrated residual (0, 0, 0)).

**Evidence chain for it, on the current record:**
1. The claim is entirely about the **derived** tensor and the
   **derived** assembly. Nothing in Phase 355 or Phase 361 touches
   the derived side: both phases' controls *presuppose and
   reproduce* it (355 R2's both-arms reads match Gate-37's derived
   values at the throat and at Ellis ℓ = 1; 361 VAL-1's pipeline
   recovers an independent print tensor end-to-end, and 361's
   derived side is triangulated against Phase 318's pattern form,
   exact on fresh jets).
2. Phase 361 CTL-2 reproduces the claim's A-throat arithmetic
   exactly: REST_derived(A) = (−23/5040, −13/5040, −31/5040).
3. The three independent derivation routes of the value
   (9/4, 3/4, 21/4) (318 prediction; 323 routes (a) and (b);
   Gate-37's from-scratch jet engine, divergence exactly 0, Ricci
   lock (0, −1, 1/2, 1/2)) stand unchallenged by any later record.

**Scope note (recorded, not a defect):** the residual figure the
claim quotes, (0, +2, −7), is Phase 259's A-throat residual; Phase
363's R3 re-derives the target side of the original differencing
from its stored sources. If R3 were to move that figure, the
cancellation clause would be re-stated against the moved figure —
the derived evaluation (9/4, 3/4, 21/4), which is the claim's
deciding content, does not depend on it. The verdict is SURVIVES
in Gate-37's exact wording (§5).

## §4 Adjudication of G37-C — SURVIVES RESTATED

**The claim (Gate-37 §5):** under the fully arbitrated assembly of
Phases 259/318/323, T_S is identified in the registered form only
— against THA's targets on the harness cores (Ellis + A) and the
Ellis gate, at all powers — supported by the gate's ξ⁰
re-derivation (both cores exact (0, 0, 0); gate coefficient
203 → 187 exactly; root and NEC roots on target at the targets'
printed rounding; wider-set ξ⁰ maxima at C and E collapsing under
the same substitution) and by Phase 259's certificates for the
ξ¹/ξ²/ξ³ sectors.

**What the current record does to it:**
1. The identification's deciding content is **derived-side**:
   substitute the derived tensors and both cores close exactly;
   the gate polynomial's ξ⁰ coefficient lands on the target value
   187; its root and the NEC roots land on target. Every one of
   those reads is arithmetic on the programme's own assembly and
   targets, and all of them stand — re-confirmed where the later
   record touches them (361 CTL-2: the REST difference and the
   203 → 187 move reproduced exactly; 355 memo §2: "the
   all-derived assembly closes the Ellis and A cores exactly
   (0,0,0) and moves the gate coefficient 203 → 187 (G37-C's
   assembly identification is arithmetic on the programme's own
   assembly and does not depend on where print errs)").
2. What the record removes is the claim's **framing**: "fully
   arbitrated assembly" was understood, in the published set, as
   *print assembly arbitrated against derived assembly, the
   difference located in print*. The location half of that
   arbitration has collapsed (§2). The differencing statement —
   REST_print differs from REST_derived by (0, 8/105, 0) — still
   stands as bookkeeping, but what REST_print faithfully
   represents is under re-examination (Phase 363, R1–R3). A claim
   whose final strength depends on that outcome must be worded at
   the strength the current record supports, with the dependence
   on its face (the charge's fence). The current record supports:
   the derived assembly closes the cores and meets the targets;
   it does not yet support any statement about what the print-side
   comparator is.
3. The ξ¹/ξ²/ξ³ sectors stand on Phase 259's certificates,
   unchanged — nothing in 355/361 touches them (both phases worked
   in the ξ⁰ sector and its bookkeeping).

**Verdict:** SURVIVES RESTATED, in the wording of §5. The
identification itself — T_S identified in the registered form
only, on the harness cores and the Ellis gate, at all powers —
is retained at full strength; the restatement strips the
arbitration framing back to what the record now shows and states
the Phase 363 dependence on the claim's face.

## §5 Claim set as re-judged — the only quotable form

> **G37-A — FAILS. No quotable successor.** The attribution of
> the Phase 259 ξ⁰ residual to exactly one printed number in
> Décanini & Folacci's H{2,0}(3) (print T^r_r = 80/3 vs derived
> 16) is refuted by direct evaluation: verbatim printed
> Eq. (2.23) is the derived tensor (Phase 355, control R2;
> re-confirmed Phase 361, CTL-1). The single-carrier substance is
> likewise unsupported: print H(6,3)(3) is the derived tensor
> (Phase 361, Arm A) and DF's (3.14)→(3.15) expansion is faithful
> (Phase 361, Arm B). No attribution of the residual to any
> printed number in DF (2007) may be quoted.
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
> reproduced exactly as a control in Phase 361 (CTL-2).
>
> **G38-C (the identification, restated).** T_S is identified in
> the registered form only: against THA's targets on the harness
> cores (Ellis + A) and the Ellis gate, at all powers, **under
> the derived assembly** — with the derived H tensors substituted,
> both cores close exactly (0, 0, 0); the Ellis gate
> polynomial's ξ⁰ coefficient is 187 exactly (the target value;
> the stored print-side assembly's coefficient is 203, a
> difference of exactly the ξ⁰ bracket (0, 16, 0)); the root and
> the NEC roots land on target at the targets' printed rounding;
> the wider-set ξ⁰ maxima at C and E collapse under the same
> substitution; and the ξ¹/ξ²/ξ³ sectors stand on Phase 259's
> certificates. **Dependence, stated on the claim's face:** the
> print-side comparator REST_print — the aggregate produced by
> Phase 259 Stage-4's back-out, which differs from the derived
> aggregate by (0, 8/105, 0) — is under re-examination
> (Phase 363: the back-out algebra, the harness's (3.15) throat
> evaluation, and the target side of the original differencing).
> Every printed tensor and expansion step on the DF side that
> could have carried that difference has been excluded by direct
> evaluation (Phases 355, 361). If Phase 363 moves REST_print,
> the differencing statement above — not the derived closures,
> the coefficient 187, or the target matches — is what would be
> re-stated.
>
> **Fences (part of every claim above).** Identification is in
> the registered form only (harness cores Ellis + A and the
> Ellis gate, all powers, derived assembly). Phase 259's D1
> stands: the ξ⁰ residual was not a reading artefact. The D2
> generic-θ gap remains a gap. The THA Eq. (26) ξ³ defect
> stands. No wormhole construction, no traversability claim, and
> no FTL claim follows from this verdict. **Defect separation:**
> Phase 241's indictment of DF's H(6,3)(5), (6), (8) as not
> conserved as printed is a separate result about separate
> tensors, reached by a separate test; it is not part of this
> claim set, is untouched by this gate, and must never be merged
> with the ξ⁰ identification above. (Phase 363's R1 re-derives
> one known-sector subtraction in which a Phase 241-sector value
> appears as bookkeeping; per its charge that re-derivation does
> not re-open, use, or disturb the indictment.)

## §6 Draft correction note for release v1.27.0

*Draft only — prepared by Gate-38 for Rakshit's approval. Nothing
in this section is published by this gate.*

---

**Correction to the semiclassical identification claim set
(v1.27.0)**

We are correcting one claim in this release, and narrowing the
framing of another. The underlying computations stand; what was
wrong is a statement about *where* a discrepancy sits in a 2007
paper by Décanini & Folacci, and we are withdrawing that
statement.

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

**What did not change.** The discrepancy itself is real — it was
never a reading error on our side. The corrected set of formulas
still closes the throat equations exactly, the headline
coefficient still moves from 203 to 187 onto its target value,
and the evaluation at the second throat still holds exactly.
No black hole result is affected: we checked, and no widely
quoted black hole datum was ever computed from that paper's
formulas (the famous values all predate it), the tensor in
question is in any case exactly zero around ordinary black
holes, and the two later papers that genuinely build on the
paper's expansion use a step we have now verified is faithful —
their numbers do not move.

**What is still open.** If the paper's formulas are correct, the
discrepancy must have entered on our side of the ledger — in the
bookkeeping that assembled the "printed" side of our original
comparison, in our evaluation machinery, or in the target values
we compared against. A re-examination of those three places is
under way. Until it reports, we withdraw the claim that the
discrepancy is carried by a misprint in Décanini & Folacci
(2007), and the identification claim in this release should be
read in the corrected form issued with this note: it rests on
the corrected assembly's exact closures and target matches, and
makes no claim about where the original discrepancy entered.

This correction concerns only the identification claim set in
this release. No other claim set is affected.

---

## §7 Provenance and artefacts

Charge: ledger entry 917. Records read and verified:
`gate37/GATE37.md` (the set under adjudication; §5 the quotable
form); `phase355/CHECKPOINT355.md`,
`phase355/results/p355_memo.md` (headline verdict NO FAMOUS
CONSUMER FOUND; Step 3 control R2 failure and its stated
consequence); `phase361/CHECKPOINT361.md`,
`phase361/results/p361_memo.md` (verdict NEITHER; Arms A and B;
controls CTL-1/CTL-2, validations VAL-0/VAL-1; the cumulative
exclusion list; the scoped R1–R3 re-examination); ledger entries
914 (Phase 361 verdict), 915 (Phase 363 charge — still running at
the time of this gate), 917 (this gate's charge). Phase 318/323
records were relied on through Gate-37's adjudication of them and
through the reproductions of their values in the 355/361
controls; no link in any evidence chain above rests on a phase
summary alone. Nothing was written outside `gate38/`; no ledger
append was made by this gate; no release, file, or wording
outside `gate38/` was altered.
