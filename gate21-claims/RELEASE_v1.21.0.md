# Warp Pilot v1.21.0 — Gate-21: the flipped pose's instrument gate holds at λ = 0.10 (fenced) and fails by λ = 0.1452

Two results from Phase 186, put through Gate-21 (the
programme's standing two-part gate: independent
second-path reproduction plus a documented literature
novelty search, under the ruling "verify everything and
tell honestly what you found"). **G21-1 SURVIVES IN
RESTATED WORDING** — the enriched-instrument gate read
holds at finite λ = 0.10, with the fence carried as
part of the claim: the witness is coefficient-large
and near-null-carried, and the pass is an exact-reads
pass reached by the registered fallback route.
**G21-2 SURVIVES INTACT** — at λ = 0.1452 the read
fails under the registered count-preserving
discipline; the onset bracket is (0.10, 0.12], and the
gate's own probes tighten it to (0.10, 0.11]. Both
claims are SPECULATIVE and instrument-scoped; neither
is a pose verdict or an FTL result. The bundle is in
`gate21-claims/` (RESULTS.md, MANIFEST.md, GATE21.md,
code/, results/, sources/).

**G21-1, the claim, in Gate-21's exact quotable form
(verbatim):**

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

**G21-2, the claim, in Gate-21's exact quotable form
(verbatim):**

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

**Gate record.** Deciding reads: closure
0.6233418793559693, Δq = (+2.892×10⁻⁵, +2.304×10⁻⁴),
Type-I [False, False], count 52, max field 0.042537.
The gate also corrects two of Phase 186's narration
points on the record (the flip mechanism; the SLSQP
non-convergence). Full record: `gate21-claims/GATE21.md`.

**Links.** Concept DOI: 10.5281/zenodo.24425078.
Version DOI: TBD — Zenodo mints it at release.

Disclosure: this is AI-driven analysis — the
computation was produced by an AI research system
working under my direction, and I am posting it
precisely to have its legitimacy checked by humans:
is the argument sound, and is it already known?
Corrections and references are exactly what I am
asking for.
