# Gate-21 claims — RESULTS (release v1.21.0)

Two claims from Phase 186 — the flipped pose's
enriched-instrument gate read at finite λ — put
through Gate-21: the programme's standing two-part
gate — an independent second-path recomputation AND a
documented literature novelty search, under the ruling
"verify everything and tell honestly what you found,"
with the Uniqueness Protocol amendment of 2026-11-22
applied to every wording. Full gate record: `GATE21.md`
in this folder; verifier code and numbers in `code/`
and `results/`; the phase-source records the claims
rest on in `sources/`; file-by-file provenance in
`MANIFEST.md`.

**Count: SURVIVED INTACT 1 · SURVIVED IN RESTATED
WORDING 1 · DEAD AS OURS 0.** G21-1: the λ = 0.10 gate
read HOLDS, restated with its fence as part of the
claim — the witness is coefficient-large and
near-null-carried (‖d‖₂ = 4.407427, 99.976% of ‖d‖²
below σ_cut), reached by the registered fallback start
plus two exact-read correction iterations after the
linearised min-closure SLSQP failed to converge; the
pass is an exact-reads pass, as the registration
provides. G21-2: at λ = 0.1452 the read FAILS under
the registered count-preserving discipline, intact;
the gate's own probe tightens the onset bracket to
(0.10, 0.11]. Two narration corrections to Phase 186
are recorded in the gate record (the flip mechanism is
a complex→real eigenvalue-pair transition at site 44,
not a D_r zero-crossing; the linearised feasible set
at cap 0.63 was not empty — the SLSQP failed to
converge, a different fact). Both claims are
SPECULATIVE and instrument-scoped. Novelty: not
claimed for either.

The claims below are stated ONLY in Gate-21's exact
quotable forms, quoted verbatim.

---

## G21-1 — SURVIVES IN RESTATED WORDING

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

---

## G21-2 — SURVIVES INTACT

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
