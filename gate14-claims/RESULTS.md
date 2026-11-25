# Gate-14 claims — RESULTS (release v1.15.0)

One result from Phase 108 (the reopening) and Phase 119
(the replication) — the multipartite quantum-energy-
teleportation (QET) accounting claim — put through
Gate-14 (2026-11-23): the programme's standing two-part
gate — an independent second-path recomputation AND a
documented literature novelty search, under the ruling
"verify everything and tell honestly what you found,"
with the Uniqueness Protocol amendment of 2026-11-22
applied to every wording. Full gate record: `GATE14.md`
in this folder; verifier code and numbers in `code/`
and `results/`; the phase-source records the claim
rests on in `sources/`; file-by-file provenance in
`MANIFEST.md`.

**Count: SURVIVED INTACT 1 · UPLOAD-READY AFTER
RESTATEMENT 0 · DEAD AS OURS 0.** G14-1: correctness
REPRODUCED on fresh machinery built from the published
paper's equations only (no Phase 108 or Phase 119 code
read, imported, or adapted; checker 501/501 PASS).
Novelty: NOVEL (8 verbatim queries/sources logged in
`results/g14_search_log.md`; Semantic Scholar and
INSPIRE-HEP both list zero citations of the source
paper as of 2026-11-23; stated gaps: English only,
abstract-level for subscription literature, no direct
Google Scholar access). The gate's original coordinator
died in a daemon restart mid-run; the recovery
coordinator audited the recovered machinery's
independence before trusting it, and a second restart
was survived by a checkpointing/resumable evaluator
whose resumed values are bit-identical to the earlier
runs' printed lines — the full recovery record is on
the face of `GATE14.md` §1.

The claim below is stated ONLY in Gate-14's upload
wording, quoted verbatim.

---

## G14-1 — SURVIVED INTACT

**Multipartite QET delivers net negative energy against its
uncorrelated reference, with the entanglement resource fully
counted.** In the N-qubit quantum-energy-teleportation model
of Xun & Ren (arXiv:2410.04919) — the model is theirs; what is
claimed here is an accounting result computed on it — read the
receiving sector (the output qubits' local Hamiltonians plus
the interaction V entire) against its uncorrelated reference:
the energy that sector holds in the marginal-product state
(the ground state's own single-qubit marginals, all
correlations deleted) above its ground value,
E_prep^(marg) = 4k²/D, D = √(N²h² + 4k²). The net delivered
energy E_net,B = E_prep^(marg) − E_out is then NEGATIVE at
eight (N, m, k/h) rows — first at (5,1,0.5),
E_net,B = −0.0414 — meaning the protocol extracts more from
the sector than the sector's correlation energy, with that
resource on the books. Measured against the Ford–Roman scale
3/(32π²) with the duration τ_marg (the sector energy's first
return to the uncorrelated-reference level; the convention
ruled in Phase 119-1 from the inherited accounting's text),
the ratio R = |E_net,B|·τ_marg/(3/(32π²)) exceeds 1 at the
five deciding rows: 3.196 (6,1,0.5), 4.681 (8,1,0.5), 11.054
(8,1,1), 5.195 (10,1,0.5), 14.337 (10,1,1). Under the other
registered convention τ₀ (first return to the ground zero)
the same five rows also exceed 1 (2.254, 3.623, 6.518, 4.243,
9.793), and (10,1,2) stands under τ₀ alone at 5.134 with no
τ_marg return for t ≤ 30; the claim is not
convention-dependent at the deciding rows. **Price caveat,
verbatim and inseparable:** against the cheapest uncorrelated
preparation (the separable minimum
E_prep^(sep) = 4k²/(D + N)), the total price is 5.34–28.17
per unit delivered at the deciding rows, classical leg
omitted, so the figure is a lower bound — this is NOT an
energy source: every unit delivered costs between 5.34 and
28.17 units of preparation and injection. **Scope:** a finite
spin model under a pulse construction. This is not a
field-theory claim — no multipartite field/oscillator QET
exists in published form (Phase 119-2), and the 1/N dilution
behind the effect is a property of this model's single shared
interaction. Accounting (C12): a sourcing-accounting result
in a finite model; it implies no device, no transport, and
nothing faster than light.
