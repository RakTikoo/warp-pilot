# GATE-14 — the multipartite QET accounting claim (P108-5, replicated P119-1)

**Status: CLOSED — verdict SURVIVED INTACT.**
Checker: `g14_check.py` — **501/501 PASS** (run 2026-11-23).
Claim joins the publication queue automatically under the standing
rule, in the upload wording recorded verbatim in §5 below. The gate
itself uploaded nothing; nobody was contacted.

---

## 1. Recovery and independence audit (on the face of the record)

Gate-14's original coordinator died in a daemon restart mid-run,
leaving on disk: `g14_eval.py` (fresh evaluator), `g14_check.py`
(checker), and two partial run logs (`results/g14_run.log`,
`g14_run2.log`; the 21 m=1 rows printed, 4 of 8 separable-price
certificates printed, no results JSON, no gate record). The
recovery coordinator audited the machinery before trusting it:

**(a) Provenance — PASS.** `g14_eval.py` imports only numpy, scipy
and the standard library. It builds the Hamiltonian from the
published paper's Eqs. (1)–(2) constants (H_i = h·Z_i + Nh²/D·1;
V = 2k·X^⊗N + (4k²/D)·1; D = √(N²h² + 4k²)), takes the ground state
both from eigendecomposition and from the paper's Eq. (3) analytic
form (cross-checked per row), applies the Eq. (4) projectors and
the Eq. (7) conditional unitary explicitly at the Eq. (10) optimal
θ, and cross-checks E_in against Eq. (6) and E_out against
Eq. (11) on every row. NO Phase 108 or Phase 119 code is read,
imported, or adapted anywhere in the gate's machinery; Phase 108's
results file is used only as the comparison target, Phase 72's and
Phase 119-3's only as stored anchors in the checker.

**(b) Accounting — PASS (verbatim).** The evaluator implements
exactly the inherited accounting of the P72-2 run record §§3–4 as
fixed for this model in Phase 108's definitions: receiving sector
= the output qubits' H_i plus V entire; E_prep^(marg) = the
sector's energy in the marginal-product (uncorrelated) reference
above its ground value = 4k²/D (computed two ways per row: closed
form and explicit marginal-product density matrix, agreeing to
≤ 1e-9 relative); E_net,B = E_prep^(marg) − E_out;
R = |E_net,B|·τ/(3/(32π²)) for E_net,B < 0, else 0; τ₀ = first
t > 0 with S(t) = 0 (P72-2's τ_pulse); τ_marg = first t > 0 with
S(t) = +E_prep^(marg), searched to t ≤ 30. No accounting change
was made or needed. The N=2 control inside the run reproduces
Phase 72's stored pair-form reads at all three r (energies to
≤ 1e-9 relative, τ₀ to ≤ 1e-6 absolute), and the pair form stays
closed there (E_net,B > 0 at N = 2), as the accounting requires.

**(c) Checker — PASS after one disclosed repair.** `g14_check.py`
re-derives every R from the gate's own E_net,B and τ values,
checks the evaluator's internal cross-checks per row, the N=2
control against Phase 72's stored reads, the full 30-row table
against Phase 108's stored reads, the deciding-row content, and
the price range from the gate's own separable certificates
against Phase 119-3's stored values. REPAIR (schema only): the
original checker read Phase 72's anchor as `P72["rows"][...]["E_net_B"]`;
the stored file's schema is `"points"` with the net read under
`"E_net_B_sector"`. The access was adapted to the stored schema;
no anchor value was altered (the stored values are identical to
the C1 control values printed in CHECKPOINT119 §P119-1).

**Completion repairs to the evaluator (disclosed, numerics
untouched).** (i) The original `main()` covered only the 21 m=1
rows; the registered row set is all 30 rows of
`p1085_results.json`. The configuration list was extended by
(3,2), (4,2), (4,3); `run_row` was already m-general, and every
added row carries the same internal cross-checks. (ii) After a
second daemon/VM restart killed the first full recovery run
(`results/g14_run3.log`: all 30 rows and 3 certificates printed,
JSON never written), `main()` was made checkpointing/resumable —
it writes `results/g14_numbers.json` after every row and every
certificate and skips completed items on restart. Same `run_row`,
same `sep_min`, same SEP seed: the resumed run's values for every
item the earlier runs had printed are bit-identical to those
printed lines (rows in run2/run3; certificates in run2/run3),
which is the on-record evidence that the resilience change altered
no numerics. The completed run is `results/g14_run4.log`.

## 2. The claim under audit (as registered, CHECKPOINT119 §P119-1)

In the multipartite quantum-energy-teleportation model of Xun &
Ren (arXiv:2410.04919), under the programme's inherited resource
accounting (§1(b)), the receiving sector delivers net negative
energy relative to its uncorrelated reference — E_net,B < 0 first
at (N,m) = (5,1) — with the Ford–Roman ratio R > 1 at the
deciding rows under the τ_marg convention (Phase 119-1's ruling):
(6,1,0.5), (8,1,0.5), (8,1,1), (10,1,0.5), (10,1,1); plus
(10,1,2) under τ₀. Completed price caveat (Phase 119-3): total
price 5.34–28.17 per unit delivered against the separable minimum
E_prep^(sep) = 4k²/(D+N), classical leg omitted. Scope: a finite
spin model under the programme's pulse construction — NOT a
field-theory claim, NOT an energy source.

## 3. Deciding reads (gate's own machinery, `results/g14_numbers.json`)

Internal machinery quality, all 30 rows: worst |E_out(sim) −
E_out(Eq. 11)| relative difference 1.3×10⁻¹⁴; Eq. (3) ground-state
overlap ≥ 1 − 6.7×10⁻¹⁶; max |E_ground(eig)| = 2.24×10⁻¹⁵;
S(0) = −E_out to ≤ 1e-9 on every row.

Negative rows — exactly the registered eight, no others:
(5,1,0.5), (6,1,0.5), (6,1,1.0), (8,1,0.5), (8,1,1.0),
(10,1,0.5), (10,1,1.0), (10,1,2.0). First negative:
(5,1,0.5), E_net,B = −0.041400616405806862.

| row (N,m,r) | E_net,B | R(τ₀) | R(τ_marg) |
|---|---|---|---|
| (6,1,0.5) deciding | −0.09902166393023670 | 2.253576 | **3.195883** |
| (8,1,0.5) deciding | −0.17386621648101050 | 3.622990 | **4.680715** |
| (8,1,1.0) deciding | −0.29578297720912627 | 6.518023 | **11.053974** |
| (10,1,0.5) deciding | −0.22016893412110833 | 4.243281 | **5.194680** |
| (10,1,1.0) deciding | −0.47102276125613374 | 9.793104 | **14.336682** |
| (10,1,2.0) τ₀ row | −0.22350352389957173 | **5.134410** | no return, t ≤ 30 |
| (5,1,0.5) split | −0.04140061640580686 | 0.987117 | 1.513231 |
| (6,1,1.0) split | −0.02247361538192427 | 0.522802 | 8.884516 |

All five τ_marg deciding rows clear R > 1; all five also clear
R(τ₀) > 1; (10,1,2) clears under τ₀ with NO τ_marg return for
t ≤ 30 on the gate's machinery either (the registered non-return
is reproduced, not assumed); the two split rows split exactly as
registered. C3 control: τ_marg(2, 0.5) = 0.8385330500198817 vs
the registered 0.838533050344258 (Δ = 3.2×10⁻¹⁰).

Price, from the gate's OWN separable certificates (240-start
L-BFGS-B over the Bloch parametrisation plus the analytic corner;
the corner D − N attains the minimum at every negative row):
Π_sep = 16.930773 (5,1,0.5); 19.036974 (6,1,0.5); 7.738199
(6,1,1); 23.525279 (8,1,0.5); 9.012193 (8,1,1); 28.170099
(10,1,0.5); 10.452606 (10,1,1); 5.340121 (10,1,2) — completed
range **[5.34, 28.17] per unit delivered**, reproducing Phase
119-3's completed caveat from fresh certificates.

Full-table agreement with Phase 108's stored reads: inside the
registered tolerances at all 30 rows (checker §full-table:
energies ≤ 1e-6 relative; τ and R ≤ 1e-4 relative), most rows far
inside them.

## 4. Novelty audit

Grade: **NOVEL** (search log: `results/g14_search_log.md`,
queries verbatim, gaps stated there). What is graded is only the
accounting result of §2. The source paper itself frames its
results as transfer efficiency η = E_out/E_in and its correlation
with entanglement — no uncorrelated-reference netting, no
Ford–Roman ratio. Citation indexes checked 2026-11-23: Semantic
Scholar lists ZERO citations of arXiv:2410.04919; INSPIRE-HEP
records citation_count 0 — no citing work carries the result
either. Near neighbours, none of which carries it: Hotta's QET
foundations (negative density against the entangled-ground zero;
no uncorrelated-reference netting); Funai & Martín-Martínez,
PRD 96, 025014 (2017) (field/detector QET saturating quantum
interest — a different model class and accounting); Ragula &
Martín-Martínez, arXiv:2505.04689 (review; no such result for
this model); Ikeda, PRD 114, 045016 (2026) (lattice/continuum
correspondence — a different question). The model is Xun & Ren's
and is cited as theirs in the upload wording; no priority over
the model is claimed or implied.

## 5. Verdict and upload wording

**G14-1: SURVIVED INTACT.** The registered claim — convention,
deciding rows, split rows, non-return, and completed price
caveat — is reproduced in full by the gate's independent
machinery. No restatement is required: the registered wording
already carries the τ_marg convention, the claim's status under
τ₀, the price caveat, and the finite-spin-model scope. The claim
may be carried only in this wording:

> **Multipartite QET delivers net negative energy against its
> uncorrelated reference, with the entanglement resource fully
> counted.** In the N-qubit quantum-energy-teleportation model
> of Xun & Ren (arXiv:2410.04919) — the model is theirs; what is
> claimed here is an accounting result computed on it — read the
> receiving sector (the output qubits' local Hamiltonians plus
> the interaction V entire) against its uncorrelated reference:
> the energy that sector holds in the marginal-product state
> (the ground state's own single-qubit marginals, all
> correlations deleted) above its ground value,
> E_prep^(marg) = 4k²/D, D = √(N²h² + 4k²). The net delivered
> energy E_net,B = E_prep^(marg) − E_out is then NEGATIVE at
> eight (N, m, k/h) rows — first at (5,1,0.5),
> E_net,B = −0.0414 — meaning the protocol extracts more from
> the sector than the sector's correlation energy, with that
> resource on the books. Measured against the Ford–Roman scale
> 3/(32π²) with the duration τ_marg (the sector energy's first
> return to the uncorrelated-reference level; the convention
> ruled in Phase 119-1 from the inherited accounting's text),
> the ratio R = |E_net,B|·τ_marg/(3/(32π²)) exceeds 1 at the
> five deciding rows: 3.196 (6,1,0.5), 4.681 (8,1,0.5), 11.054
> (8,1,1), 5.195 (10,1,0.5), 14.337 (10,1,1). Under the other
> registered convention τ₀ (first return to the ground zero)
> the same five rows also exceed 1 (2.254, 3.623, 6.518, 4.243,
> 9.793), and (10,1,2) stands under τ₀ alone at 5.134 with no
> τ_marg return for t ≤ 30; the claim is not
> convention-dependent at the deciding rows. **Price caveat,
> verbatim and inseparable:** against the cheapest uncorrelated
> preparation (the separable minimum
> E_prep^(sep) = 4k²/(D + N)), the total price is 5.34–28.17
> per unit delivered at the deciding rows, classical leg
> omitted, so the figure is a lower bound — this is NOT an
> energy source: every unit delivered costs between 5.34 and
> 28.17 units of preparation and injection. **Scope:** a finite
> spin model under a pulse construction. This is not a
> field-theory claim — no multipartite field/oscillator QET
> exists in published form (Phase 119-2), and the 1/N dilution
> behind the effect is a property of this model's single shared
> interaction. Accounting (C12): a sourcing-accounting result
> in a finite model; it implies no device, no transport, and
> nothing faster than light.

**Status: COMPLETE** (evaluation run4 complete; checker 501/501
re-run by the recovery coordinator from disk; novelty audit
complete; record closed 2026-11-23).
