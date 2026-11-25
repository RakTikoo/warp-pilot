# FTL Programme — Phase 119 CHECKPOINT (ground record)

**Status:** CLOSED (2026-11-23, coordinator) — all five
items resolved against their pre-registered criteria.
Checkers: P119-1 ALL PASS, P119-2 ALL PASS (127 checks),
P119-5 25/25 — each re-run fresh by the coordinator;
P119-3 ALL PASS and P119-4 245/245 on the workers' runs,
their outputs verified from disk by the coordinator,
whose own fresh re-runs of those two were launched and
still running under severe VM contention at phase close
(logs `work/p1193_coord_rerun.log`,
`work/p1194_coord_rerun.log`; the P119-4 re-run had
already regenerated its output JSON at the identical
byte count). Headline: P119-1 REPLICATED the QET
reopening; the claim is registered for a full Gate
(§P119-1 claim block) and routed to the parent. No
joint (i)+(ii) improvement at any superluminal cell.
Verdict sections and final synthesis at the end of this
file. Workers did not edit this file.

**Mission / sequencing.** Phase 119 executes Phase 108's
integrated follow-up queue in its order:
`../phase108/CHECKPOINT108.md` §"Integrated follow-up
queue", items 1–6 (FU-P106-4a, queue item 7, remains
UNPROMISED under its own future registration and is NOT
run here). Mapping: P119-1 = FU-P1085-1 (Gate-style
replication of the P108-5 τ reads + τ-convention ruling);
P119-2 = FU-P1085-2 (the field/oscillator analogue);
P119-3 = FU-P1085-3 (the separable-minimum price
reference); P119-4 = FU-P1083-1 + FU-P1083-2 (the
alignment set's two named escapes, one item, two halves);
P119-5 = FU-P1084-1 (the breathing reopening criterion as
a search item).

**Parent record.** `../phase108/CHECKPOINT108.md` in
full; `../phase106/CHECKPOINT106.md` §P106-3 (the
inherited accounting, verbatim); `../phase72/results/
p722_run_record.md` §§3–4 + `p722_results.json` (P72-2's
stored reads — the N = 2 control); `../phase108/results/
p1085_results.json` + `p1085_memo.md` +
`../phase108/work/p1085_definitions.md` (the claim under
replication and the definitions fixed before its
computing); `../phase101/work/p1015_lib.py` +
`../phase101/results/p1015_partB_raw.json` (the
coupling-force front machinery and corpus);
`../phase118/CHECKPOINT118.md` §P118-1 (the β_c = 0 slice
registration — Phase 118 owns it; it is IN FLIGHT with no
verdict integrated at this writing);
`../phase85/results/p852_matrix.json` (the coverage
matrix); `~/workspace/compute_allocation.md`.

## Standing orders (binding)

- FAILURE PROTOCOL: anatomy plus at least one
  mechanism-suggested follow-up for every negative;
  closure only on structural evidence with a reopening
  condition.
- ANTI-LOOP RULE: no third revisit of a closed theory
  class without a NEW mechanism. P119-4's two halves ARE
  Phase 108's registered escapes (new mechanisms named by
  P108-3's verdict); P119-5 runs no breathing — it only
  tests the registered reopening criterion on paper.
- float64 everywhere; 40-digit mpmath where a deciding
  read demands it (none is pre-registered as demanding it
  in this phase; a worker who finds one states why on the
  face of its run record). Programme venv
  `~/workspace/warp-pilot/venv/bin/python`.
- Published forms only, never gate-fitted; designer
  candidates enter at the ACTION where a theory is posed.
- Solution-grade reads on the non-degenerate front
  (Phase 79 standard): content set and degenerate count
  stated on every front read; a vacuous point is never a
  passed point.
- Worst-instant auditing for any time-dependent object
  (no such audit is registered in this phase; the τ reads
  of P119-1 are first-return reads of a stored functional,
  defined in P72-2 §4, not cycle averages).
- Full-volume all-directions NEC + full-EC + Type-I bars
  wherever a CONFIGURATION is audited (P119-4's front
  reads are the registered subset form of that bar, as in
  Phases 79/101/106/108/118 — margins + Type-I + the
  canonical EoM read together; margins alone never
  decide).
- Bars pre-registered here; amendments appended, dated,
  marked post-hoc, never silently broadening a pass.
- ADVERSARIAL PROTOCOL: any positive gets an independent
  second path before integration. P119-1 IS a second path
  by construction (fresh machinery, from the paper).
- EVIDENCE RULE + grounding bar, stated on each item's
  face.
- OPTIMIZATION DIRECTIVE + RIDER + FREE-COMPUTE RULE:
  approved pools only per `~/workspace/compute_allocation.md`;
  any run expected over ~2 h continuous is checkpointed
  and routed, not left uncheckpointed on this VM. (No
  item in this phase is expected to approach that bound;
  a worker whose run grows states so and checkpoints.)
- UNIQUENESS PROTOCOL: the QET reopening is claimed
  exactly as Phase 108 scoped it — a sourcing-accounting
  result in a finite spin model, resource counted. No
  "energy source", no field claim, no FTL wording, from
  any item in this phase.
- C12 accounting on every number.
- LANGUAGE: any pass is a "scan signal under attack"
  until a later Gate verifies it.
- INTERNAL ONLY: nothing uploaded, nobody contacted.

---

## P119-1 (FU-P1085-1) — GATE-STYLE REPLICATION OF THE QET REOPENING + τ-CONVENTION RULING

**Grounding.** Phase 108's P108-5 verdict (EVALUATED —
REOPENING BAR MET) carries the caveat on its face:
"FU-P1085-1 is owed before any use beyond this phase:
independent Gate-style replication of the τ reads plus a
ruling on the τ convention." This item is that debt.
The claim under replication, exactly as scoped: in the
Xun & Ren N-qubit QET protocol (arXiv:2410.04919), under
P106-3's inherited accounting (P72-2 run record §§3–4,
verbatim; definitions as fixed in Phase 108's
`work/p1085_definitions.md`), the receiving sector's net
energy relative to its uncorrelated (marginal-product)
reference, E_net,B = E_prep^(marg) − E_out, is NEGATIVE
at eight (N, m, r) rows, and the FR-net ratio
R = |E_net,B| · τ / (3/(32π²)) (ħ = 1 in model units)
exceeds 1 at the deciding rows under the two registered
duration conventions: τ₀ (P72-2's literal τ_pulse — first
t > 0 at which the post-protocol sector energy S(t)
under H-evolution returns to the ground zero) and
τ_marg (first return of S(t) to +E_prep^(marg), the
uncorrelated-reference level).

**Fresh-machinery clause (the item's defining
condition).** The replication is written FROM THE PAPER
(arXiv:2410.04919 full text: Hamiltonian Eqs. (1)–(2),
ground state Eq. (3), E_in Eq. (6), E_out Eqs. (9)–(11)
and the App. A/B sector pattern) and from the inherited
accounting texts above. Phase 108's code
(`p1085_eval.py`, `p1085_secondpath.py`) is NOT read,
imported, or adapted; Phase 108's RESULTS
(`p1085_results.json`, memo tables) are the comparison
target only, opened after the fresh numbers exist.
Acceptable fresh routes (worker's choice, stated in the
run record): dense Kronecker construction of H with
eigendecomposition (2^N ≤ 1024 at N = 10 — feasible) for
the state/energy reads, with the protocol simulated
explicitly (measurement projectors on the m input
qubits, conditional output unitaries), E_out
cross-checked against the paper's printed closed form;
S(t) by exact exponentiation of the constructed H.

**Registered row set.** ALL 30 rows of
`p1085_results.json` (N ∈ {2,3,4,5,6,8,10} × the stored
(N, m) configurations × r ∈ {0.5, 1, 2}, h = 1), each
read for: E_out, E_in, E_prep^(marg) (= 4k²/D,
D = √(N²h² + 4k²) — recomputed, not assumed), E_net,B,
τ₀, τ_marg, R(τ₀), R(τ_marg), price per unit
(E_prep^(marg) + E_in)/E_out. Plus the τ(N) asymptotics
read below.

**Controls (before any deciding row is believed).**
(C1) The N = 2, m = 1 rows reproduce Phase 72's stored
reads from `p722_results.json` at all three r:
E_out = E_B (0.07257277587322132 / 0.11474763394014725 /
0.09818326611803949), E_prep^(marg) (0.4472135954999579 /
1.414213562373095 / 3.5777087639996634), E_net,B
(0.3746408196267366 / 1.2994659284329477 /
3.479525497881624), τ₀ = τ_pulse (0.2327228141003489 /
0.18537475477213097 / 0.11724917203526224) — agreement
≤ 1e-9 relative on energies, ≤ 1e-6 absolute on τ.
(C2) The constructed H's ground energy is 0 to ≤ 1e-12
(the printed constants' property) and the ground state
agrees with the paper's Eq. (3) (overlap ≥ 1 − 1e-10).
(C3) Phase 108's one τ_marg read at a control row,
(N=2, r=0.5) τ_marg = 0.838533050344258, is reproduced
≤ 1e-6 (it is a Phase 108 read, part of the target set).
If any control fails, the item stops and reports
MACHINERY FAILURE (control named) — no deciding row is
read on unvalidated machinery.

**Deciding rows (fixed).** Both-convention bar-clearers
in Phase 108's table: (6,1,0.5) R = 2.2536/3.1959;
(8,1,0.5) 3.6230/4.6807; (8,1,1) 6.5180/11.0540;
(10,1,0.5) 4.2433/5.1947; (10,1,1) 9.7931/14.3367
(R(τ₀)/R(τ_marg)). τ₀-only row: (10,1,2) R(τ₀) = 5.134,
τ_marg no return within t ≤ 30. Convention-split rows:
(5,1,0.5) 0.9871/1.5132; (6,1,1) 0.5228/8.8845. First
negative row: (5,1,0.5), E_net,B = −0.04140061640580686.

**Replication standard.** A row REPLICATES iff the fresh
read agrees with Phase 108's stored read to ≤ 1e-6
relative on E_out, E_prep^(marg), E_net,B and ≤ 1e-4
relative on τ₀, τ_marg, R (τ root-finding tolerances
stated in the run record; a τ read that cannot be
resolved to that tolerance is reported as a discrepancy
with its bracket, not smoothed over). The (10,1,2)
τ_marg non-return is part of the target: the fresh
machinery must also find no return of S(t) to
+E_prep^(marg) for t ≤ 30 there, or exhibit the return
it finds (a return found = a named discrepancy).

**τ asymptotics (registered read, not deciding).**
For m = 1, r ∈ {0.5, 1}: extend N as far as the fresh
machinery honestly reaches beyond 10 (state the largest
N and the route), and report the trend of τ₀(N),
τ_marg(N), E_net,B(N), R(N) — specifically whether τ
grows, saturates, or falls with N, and whether R's
growth with N is carried by |E_net,B| alone. Closed-form
E_out / E_prep^(marg) (printed formulas) may be used for
the energy trend at any N; τ at extended N must come
from the worker's own derived evolution, whose derivation
is stated in the run record.

**The convention ruling (owed, stated once, plainly).**
The worker rules which duration the FR-net ratio of the
inherited accounting uses, arguing from P72-2 §4's text
(the bound is referenced to the uncorrelated vacuum; the
net read's magnitude is |E_net,B| under both of Phase
108's conventions — the ruling is about duration only):
τ₀ (return to the entangled-ground zero — P72-2's
literal τ_pulse, the shorter, conservative read) or
τ_marg (return to the uncorrelated-reference level — the
full duration of the below-reference excursion). The
ruling states: the chosen convention; the argument in
≤ 10 lines; and the claim's status under the OTHER
convention at the deciding rows.

**Verdicts (only these).**
- **REPLICATED**: controls pass; every deciding row
  replicates; the split rows replicate AS split (each
  convention's side of 1 as stored, within tolerance);
  the ruling is stated. The checkpoint then registers
  the reopening claim for a full Gate in the registered
  claim block below (the parent launches gates; nothing
  publishes from this phase).
- **REPLICATION FAILURE**: any deciding row fails to
  replicate — the differing read, its size, and its
  deciding term (which quantity, which convention) are
  named. P108-5 then returns to under-attack status;
  the parent corrects the ledger on this report. An
  IMMEDIATE report is filed on landing, before the
  phase's other items complete.
- **MACHINERY FAILURE** (control named).

**Registered claim block (filled only on REPLICATED).**
Claim, in Phase 108's scoped words: a genuinely
multipartite published QET protocol (Xun & Ren,
arXiv:2410.04919) whose receiving sector delivers net
negative energy relative to its uncorrelated reference
at R_net > 1, resource counted, under the inherited
P72-2/P106-3 accounting — finite spin model scope;
price line 5.59–130.19 per unit delivered stands
against it; no field claim; nothing FTL. The Gate
registration states the ruling's convention and the
deciding rows under it.

**Deliverables:** `results/p1191_run_record.md`
(definitions + machinery route + ruling, written before
deciding numbers are compared), `results/p1191_memo.md`,
`results/p1191_results.json`; fresh scripts + independent
checker in `work/` (the checker recomputes every
verdict-carrying number from the results file and the
stored targets; it does not import the evaluation
script's internals beyond the results file).

---

## P119-2 (FU-P1085-2) — THE FIELD / OSCILLATOR ANALOGUE: DOES THE 1/N DILUTION SURVIVE?

**Grounding.** Phase 108's mechanism, on its face: the
shared N-body interaction's total correlation energy
dilutes as 4k²/D ≈ 4k²/(Nh) while single-output
extraction stays O(h); the scalings cross at N = 5. The
queue's registered question: does an N-party FIELD QET
with a shared interaction show the same 1/N dilution of
the sector correlation energy? The spin-model read does
not transfer without it. (Sibling of Phase 83's
FU-P833-1, now with a mechanism to aim at.)

**Pose discipline (strict).** Published forms only. The
analogue is posable only if the literature supplies, in
evaluable form (printed formulas that can be recomputed,
not only numerical plots): (i) a field or
harmonic-oscillator QET protocol — Hamiltonian and
ground state printed; (ii) its delivered energy at a
receiving sector/region in printed form; AND (iii) a
multipartite / multi-receiver / shared-resource
structure in print in which an N-scaling of the sector
correlation energy vs the per-receiver extraction can
be read. If (i)+(ii) exist but (iii) does not, the
missing ingredient is named exactly and the verdict is
NOT POSABLE in its multipartite clause — with the
single-receiver field reads that DO exist reported as
anatomy (including how the field protocol's own
correlation energy and extraction scale with its
parameters, and what the QEI-priced floor
(3/(32π²))·(1/τ⁴)-form bound does to a field pulse of
the delivered magnitude/duration, in the inherited
accounting's terms).

**Search (documented, before any evaluation).** Logged
queries over primary sources (arXiv full texts and
publisher pages), candidates assessed by name against
(i)–(iii). The search record names every candidate
assessed and the clause it fails, or the candidate that
meets all three. (Coordinator's leads, to be verified
not trusted: field-theory QET in Hotta's line;
QET in conformal field theory; coupled-oscillator QET;
spin-chain QET and its continuum limit; multipartite
field forms citing or generalising Xun–Ren.)

**Accounting (if posed).** The inherited accounting
verbatim (P72-2 §§3–4 via P106-3): per-receiving-sector
uncorrelated reference; E_net,sector = E_prep^(ref) −
E_delivered; R_net = 0 iff E_net ≥ 0, else the FR-net
ratio with the sector pulse's duration read from the
published form's own evolution. Reopening bar inherited
verbatim: **any variant with R_net > 1
resource-counted.** A positive is a scan signal under
attack, second-pathed from scratch before integration,
with the spin-to-field scope stated on its face.

**The deciding question (either way).** Does the
shared-resource cost still dilute ~1/N while
per-receiver extraction holds, in a system with a
continuum of modes and a QEI-priced floor? The answer
is stated as a scaling statement (exponents/forms as
read from the posed form), not only as row numbers.

**Verdicts (only these).**
- **EVALUATED — DILUTION SURVIVES** (the posed form's
  scaling stated; R reads at the posed points; second-
  pathed): the field analogue is registered as a scan
  signal under attack with its scope.
- **EVALUATED — DILUTION DIES** (the deciding term
  named: e.g. the correlation energy's scaling in the
  field form, or the QEI floor's bite at the delivered
  magnitudes — numbers stated).
- **NOT POSABLE FROM PUBLISHED FORMS** (the missing
  ingredient named exactly; the search + the
  single-receiver anatomy reported).
- **SEARCH NEGATIVE** (no field/oscillator QET in
  evaluable form at all — search and gaps recorded).
C12: an accounting item; nothing FTL is claimed by any
outcome.

**Deliverables:** `results/p1192_search_record.md`,
`results/p1192_memo.md`, and (if evaluated)
`results/p1192_results.json` + scripts/checker in
`work/`.

---

## P119-3 (FU-P1085-3) — THE SEPARABLE-MINIMUM PRICE REFERENCE FOR THE XUN–REN HAMILTONIAN

**Grounding.** Phase 108's price caveat: total counted
price per unit delivered is 5.59–130.19
(injection-dominated), read with the resource priced at
E_prep^(marg). P72-2's accounting carries TWO preparation
references — (R-marg) the marginal-product correlation
energy and (R-sep) the separable-minimum gap — and its
deciding total uses the SMALLER. Phase 108 evaluated
only (R-marg) for the Xun–Ren Hamiltonian. The queue:
"the separable-minimum reference for the Xun–Ren
Hamiltonian, completing the price-line bookkeeping in
P72-2's exact form."

**Definitions (fixed here, P72-2 §3 verbatim in form).**
For the Xun–Ren H at (N, r), h = 1 (H does not depend on
m; m enters only through E_out / E_in):
- E_sep = min over fully product states (⊗ᵢ|ψᵢ⟩) of
  ⟨H⟩; E_prep^(sep) = E_sep − E_ground = E_sep
  (E_ground = 0 by the printed constants).
- E_prep^(marg) as stored by Phase 108 (= 4k²/D, the
  full correlation energy: the receiving sector of
  P108-5's definition carries V entire).
- Price per unit delivered, resource at reference X:
  Π_X = (E_prep^(X) + E_in)/E_out (classical leg ≥ 0
  omitted — lower bounds, as inherited).
- Deliverable ratio at each registered row:
  Π_marg / Π_sep, with both Π values stated.

**Registered rows.** The eight E_net,B < 0 rows of
P108-5 — (5,1,0.5), (6,1,0.5), (6,1,1), (8,1,0.5),
(8,1,1), (10,1,0.5), (10,1,1), (10,1,2) — plus the
N = 2 control rows (m = 1, r ∈ {0.5, 1, 2}).

**Control (before any Xun–Ren number).** The same
minimisation machinery at N = 2 reproduces P72-2's
stored E_prep^(sep) EXACTLY (≤ 1e-9):
0.2360679774997898 / 0.3284271247461903 /
0.2221359549995796 at r = 0.5 / 1 / 2. Failure =
MACHINERY FAILURE (control named).

**Minimisation standard.** The product-state expectation
of the printed H is derived in the run record (for this
H it separates into single-qubit terms plus the single
N-body term 2k·Πᵢ⟨σˣ⟩ᵢ + constants — the worker derives
it from the paper's Eqs. (1)–(2), not from this
sentence). The claimed minimum is certified two ways:
an analytic reduction where the structure permits it,
AND a numerical certificate (multi-start local
optimisation over the Bloch-sphere product manifold,
≥ 200 starts, plus a random-sampling sweep of ≥ 10⁵
product states finding none lower by > 1e-9). Both
certificates are reported; a minimum supported by only
one is flagged as such and does not carry the verdict.

**Reads.** Per registered row: E_sep, E_prep^(sep),
Π_sep, Π_marg (recomputed from stored E_in / E_out —
Phase 108's stored values, quoted with their source),
the ratio Π_marg/Π_sep, and the deciding-total price
per unit under P72-2's convention (resource at
min(sep, marg)). Also stated: the N-scaling of
E_prep^(sep) vs E_prep^(marg) (= 4k²/D) at m = 1,
r ∈ {0.5, 1} over the registered N — does the separable
floor dilute like the marginal reference, or not (the
scaling statement is part of the deliverable).

**Verdicts (only these).**
- **REFERENCE COMPLETED — PRICE LINE STANDS** (the
  separable floor is ≥ the marginal reference at the
  deciding rows, or lower but the deciding-total price
  per unit remains > 1 at every deciding row): numbers
  stated; the price caveat of P108-5 is restated in its
  completed form.
- **REFERENCE COMPLETED — PRICE LINE MOVES** (the
  separable floor is enough lower that the
  deciding-total price per unit at some deciding row
  falls to ≤ 1, or the ratio Π_marg/Π_sep ≥ 2 at some
  deciding row): numbers stated; the moved price line
  is the deliverable, flagged for the parent's ledger.
- **MACHINERY FAILURE** (control named).
C12: bookkeeping completion; no claim about the
reopening itself moves — R_net is not re-read here.

**Deliverables:** `results/p1193_run_record.md`,
`results/p1193_memo.md`, `results/p1193_results.json`;
scripts + checker in `work/` (checker re-derives the
minima independently — its own sampling/optimisation —
and recomputes every ratio from the results file and
the stored Phase 108 values).

---

## P119-4 (FU-P1083-1 + FU-P1083-2) — THE ALIGNMENT SET'S TWO NAMED ESCAPES

**Grounding.** Phase 108's P108-3 verdict (STRUCTURAL
FEATURE): on the coupling-force front's flat-profile
plateau the kinetic term vanishes identically, the EoM
at plateau points is a pure force balance, the force
terms align wherever μ·H_,φ(pi0)·R_bed < 0, and at every
such point the residual is the full D_can — the front
cannot be posed on this profile family without an
alignment point carrying its worst residual. Its two
mechanism-suggested escapes, logged for the queue
verbatim: **(1) a non-flat profile (kill the plateau,
revive □φ); (2) H_,φ(pi0) = 0 (kill one force channel's
plateau sign).** This item runs both, as halves (a)
and (b). The front: Phase 48 bed at β = 1.1, the
56-point subset, the hinge theory of P101-5 Part B
(action and canonical EoM exactly as registered there;
machinery `../phase101/work/p1015_lib.py`:
`canonical_terms` — t_kin = □φ, t_pxx, t_FA = F_A/P_X
with F_A = ½·H_,φ(φ)·R_bed, t_FB = F_B/P_X with
F_B = −μφ; D_can = Σ|terms|; non-degenerate iff
D_can ≥ 1e-9; `read` for subset legality / EoM reads /
health / Frontier A).

**The registered front (the comparison, fixed).** The
P101-5B hinge best (family B, start 6): z = (ξ, β_c, β₂,
pi0, shape, p₁, p₂, μ) = (2.756667559450937,
−1.498683175695639, 0.7811507949670238,
0.3385988091052908, 0.870145941019083, 1.222294121969537,
0.0639057960421364, −0.15512773896022752),
ρ₀ = 0.046611949162594764; subset_legal =
0.5892857142857143; EoM rel max (nondeg) =
0.9999999999784565; median = 0.22437629566157347;
n_nondeg = 56, n_deg = 0; health_ok = False;
Frontier A = 0.000. Alignment set at the hinge best
(Phase 108 definition, thresholds verbatim: both force
terms live at ≥ 1e-6 × max|term|, same strict sign,
S_F = (|t_FA| + |t_FB|)/D_can ≥ 0.90,
|t_kin|/D_can ≤ 1e-6): {44}, S_F = 1.000000, point 44
the maximum-residual point.

**Machinery gate (before either half).** Reproduce,
via `p1015_lib.canonical_terms` on
`../phase101/results/p1015_partB_raw.json`: all seven
unique corpus configurations' stored EoM max/medians
within 1e-6 (Phase 108's worst error was 8.6×10⁻¹²),
and the hinge best's alignment set = {44} under the
registered definition. Failure = MACHINERY FAILURE
(gate named); neither half runs on unvalidated
machinery.

**Half (a) — THE NON-FLAT PROFILE (FU-P1083-1).**
Pose: the same theory, the same bed and subset, with
the scalar profile replaced by a NON-FLAT radial
profile — φ varying across the former plateau radii so
that □φ is alive at the deciding points. The profile is
a posed configuration (the theory is fixed by the
action; profiles are what the front reads). Its
analytic form and parameters are fixed in the run
record BEFORE numbers, within this envelope: radial,
φ(r) built from the stored 'wallwide' shape composed
with a stated monotone radial reparametrisation OR a
stated closed-form blend (worker's choice, recorded);
jets by the PhiProfile pattern (analytic d1/d2,
FD-verified at rel agreement < 1e-6 before any read).
Operational non-flatness (registered): at the posed
configurations, |t_kin|/D_can > 1e-6 at a MAJORITY of
the former plateau points (subset indices 0–43) — a
profile failing this at its own best candidate has not
posed the escape, and the half reports exactly that.
Search: joint least-squares on the P101-5 Part B
pattern (residual in `p791_main`'s form) over
(couplings z, profile parameters, family-B fluid ρ₀
∈ [0, 0.05] as in the hinge pose; family A also read at
the best candidate), ≥ 12 starts including the hinge
best re-posed on the non-flat profile; max_nfev and
checkpointing on the P101-5B pattern.

**Half (b) — H_,φ(pi0) = 0 (FU-P1083-2).**
Pose: the stored 'wallwide' profile family, the search
constrained to the codimension-1 set
H_,φ(pi0) = −(2ξ + β₂)·pi0 + β_c/2 = 0, i.e.
pi0 = β_c / (2(2ξ + β₂)), 2ξ + β₂ ≠ 0 — the plateau
value sits at the force derivative's root, so t_FA = 0
at every plateau point exactly. **Boundary with Phase
118 (registered, hard):** Phase 118 owns the β_c = 0
slice (where the same root sits at pi0 = 0). This half
requires |β_c| ≥ 0.05 at any deciding candidate; a
search trajectory whose best candidate presses against
that fence is reported as PRESSING THE PHASE-118
BOUNDARY and the read stops at the fence — the slice
itself is not entered, re-run, or re-judged here. The
trap gate of P101-5B applies verbatim (max over subset
of |F_A + F_B| < 1e-9, or the trap subspace, at the
deciding candidate = KILLED BY THE TRAP, reported
exactly). Search: joint least-squares as half (a), the
constraint imposed by parametrisation (pi0 eliminated),
≥ 12 starts including the hinge best projected onto
the constraint set.

**Reads (both halves, at each half's best candidate and
at the hinge-seeded start).** `p1015_lib.read` in full:
subset_legal, EoM rel max/median on the non-degenerate
set, n_nondeg / n_deg, health_ok, Frontier A; the
alignment set under the registered definition, its
members' terms and shares; whether the
maximum-residual point is in the set; the
three/four-term decomposition at the maximum-residual
point. Every read states its content set (Phase 79
standard).

**Bars (both halves, registered before numbers).**
- **JOINT PASS (the programme's first):** a candidate,
  second-pathed (full-margins recomputation, fast=False,
  on the `p1015_checker.py` pattern), with Frontier A
  > 0 in `p1015_lib.read`'s exact sense (subset_legal
  > 0 AND eom_rel_max_nondeg ≤ 0.02 AND health_ok) AND
  n_nondeg ≥ 28 (the vacuity fence of P118-1, adopted
  verbatim: a majority-vacuous front is not the front
  passing) AND the trap not firing.
- **JOINT IMPROVEMENT (milestone):** a candidate,
  second-pathed, Pareto-dominating the hinge best on
  (subset_legal, eom_rel_max_nondeg): subset_legal ≥
  0.5892857142857143 AND eom_rel_max_nondeg <
  0.9999999999784565, OR subset_legal >
  0.5892857142857143 AND eom_rel_max_nondeg ≤
  0.9999999999784565.
- **ESCAPE WORKS MECHANICALLY, FRONT STANDS:** the
  alignment set at the half's best candidate is empty,
  or the maximum-residual point has exited it, while
  neither bar above is met — the new binding form is
  named (e.g. the residual re-pins on a single channel,
  or legality pays for the kinetic revival), with its
  deciding term.
- **ESCAPE FAILS:** the alignment set still carries
  the maximum-residual point at the half's best
  candidate — the mechanism that re-forms it is named.
Partial movements (median moves, single-clause moves)
are reported as anatomy, not as milestones.
C12: pre-existing walls at β = 1.1; no transport claim;
a moved front is not a legal wall.

**Deliverables:** `results/p1194_run_record.md`,
`results/p1194_memo.md`, `results/p1194_results.json`;
scripts + independent checker in `work/` (checker
recomputes every verdict-carrying number from the
results file; any claimed pass/improvement is
second-pathed by the full-margins recomputation before
the memo calls it).

---

## P119-5 (FU-P1084-1) — THE BREATHING REOPENING CRITERION, AS A SEARCH ITEM

**Grounding.** Phase 108's P108-4 closure argument,
adopted on its face: the breathing line on the
Phase-16/83 bed is closable on structural evidence,
with reopening condition — **a wall family whose static
β_p = 1.1 twin has FINITE max q** (q in the Phase-63
form: the flux ratio read over the family's shell
sample, 162-direction form where that is the stored
read). The queue restates the condition as a search
criterion. This item runs NO breathing and poses NO
new wall: it surveys the record for a family meeting
the criterion ON PAPER.

**Survey scope (fixed).** (i) Every wall family in the
programme's stored record with a static β = 1.1 (or
β_p = 1.1) audit carrying a max-q read — including at
least: the Phase-16/83 bed itself (Finalist-A family);
the (10,30) M = 8.0 family (Phases 63/76/106/108 reads);
the Phase 48 bed / coupling-force front family (its
static β = 1.1 reads, if a max-q read exists in its
form); the Phase 26/50-era shell families; any family
appearing in Phase 85's coverage matrix
(`../phase85/results/p852_matrix.json`) with a stored
static superluminal read. (ii) The coverage matrix's
UNTESTED cells (motion × structure × material): a cell
names a candidate family only if its structure/material
combination corresponds to a wall family whose static
form is posed somewhere in the record — a purely
combinatorial cell with no posed static family does
not meet the criterion "on paper" and is recorded as
such, not promoted.

**Criterion (exact).** A family MEETS the criterion iff
a stored static β = 1.1 read of that family reports a
FINITE max q (a number, not +∞, not absent). A family
whose static 1.1 read reports max q = +∞ fails. A
family with no static 1.1 max-q read in the record is
UNREAD — it does not meet the criterion, and the gap
is stated (what read would have to exist). Scope
discipline: a finite max-q read on a SUBSET or band
(the Phase 106/108 band reads) is reported as such —
subset-finite, whole-family unread or infinite, as the
record states; the criterion is read on the family's
whole-shell static form as stored.

**Deliverable form.** A table: family × source (phase,
file) × static β = 1.1 max-q read (finite value / +∞ /
absent) × criterion disposition. Plus the coverage-
matrix statement: how many untested cells were
examined, how many name a posed static family, and
their dispositions.

**Verdicts (only these).**
- **CRITERION MET BY (family named)**: at least one
  family meets the criterion on a whole-shell static
  read — a breathing registration on that family
  becomes posable, and the registration sketch (bed,
  mode, bars inherited from P108-4's pattern) is
  stated for the queue. (Not a breathing result; no
  run is made.)
- **NOT MET IN OUR SEARCH**: no family meets it —
  limits stated exactly (families surveyed, reads
  found, the unread gap named). The breathing line
  then stands closed under P108-4's condition, with
  this survey as its priced search.
C12: a search/registration item; nothing is claimed
about any wall's legality by either outcome.

**Deliverables:** `results/p1195_memo.md` (survey
table + verdict), `results/p1195_results.json`;
checker in `work/` (recomputes the table from the
cited stored files — every cited max-q value is
re-read from its source file by the checker, not
transcribed from prose).

---

## Dispatch log

- 2026-11-23: Coordinator grounded in Checkpoints 72
  (P72-2 run record + stored reads), 85 (coverage
  matrix), 101 (P101-5 machinery + corpus), 106 (§P106-3
  accounting), 108 (all five verdicts + follow-up queue),
  118 (§P118-1 — in flight, no verdict integrated; the
  β_c = 0 boundary in §P119-4 is live). Registrations
  above written before worker dispatch.
- 2026-11-23: Workers dispatched for P119-2, P119-3,
  P119-4, P119-5. The P119-1 spawn failed three times on
  the transient "sqlx pool timed out" error; its dispatch
  is PENDING and will be retried — no P119-1 number
  exists yet and none is to be inferred.
- 2026-11-23: P119-1 worker dispatched on the fourth
  attempt (pool recovered). P119-5 verdict landed and
  was integrated (below) after a fresh coordinator
  checker re-run (25/25 ALL PASS).

## VERDICTS (integrated incrementally by the coordinator)

### P119-1 — VERDICT: REPLICATED

(Worker report 2026-11-23; checker `work/p1191_checker.py`
ALL PASS, re-run by the coordinator. Deliverables:
`results/p1191_run_record.md` (definitions + machinery
route + ruling, drafted before the comparison),
`results/p1191_memo.md`, `results/p1191_results.json`.)

Fresh machinery written from the paper (arXiv:2410.04919
full text) plus the inherited accounting; Phase 108's
code was never read, imported, or adapted, and its
results file was opened only after all 30 fresh rows
existed. Route: dense Kronecker H, ground state by
eigendecomposition AND Eq. (3), the protocol simulated
explicitly (Eq. (4) projectors, Eq. (7) conditional
unitaries at the Eq. (10) optimum), E_out cross-checked
against Eq. (11), E_in against Eq. (6), S(t) by exact
exponentiation. **All 30 rows replicate:** worst
relative differences vs Phase 108's stored reads —
E_out, E_prep^(marg), E_net,B, E_in, price = 0.0
(bit-exact); τ₀ = 1.0e-9; τ_marg = 1.8e-9; R = 1.0e-9 —
far inside the registered 1e-6 / 1e-4 bars. The five
both-convention deciding rows stand identically
((6,1,0.5) 2.2536/3.1959; (8,1,0.5) 3.6230/4.6807;
(8,1,1) 6.5180/11.0540; (10,1,0.5) 4.2433/5.1947;
(10,1,1) 9.7931/14.3367); (10,1,2) stands at
R(τ₀) = 5.13441 with NO τ_marg return for t ≤ 30 on the
fresh machinery either; the split rows replicate AS
split ((5,1,0.5) 0.98712/1.51323; (6,1,1)
0.52280/8.88452); exactly the registered eight rows are
negative, the first at (5,1,0.5) with E_net,B =
−0.04140061640580686 identical. Controls all pass
before the deciding rows were believed: C1 N = 2
energies bit-exact vs P72-2 at all three r, τ₀ within
1.2e-10; C2 max |E_ground| = 2.7e-15, min Eq. (3)
overlap 1 − 7e-16; C3 τ_marg(2, 0.5) within 3.2e-10 of
0.838533050344258. Price line over the 30 rows
5.5909–130.1920 (Phase 108's 5.59–130.19 stands);
5.7586–28.3253 over the negative rows. **Convention
ruling: τ_marg.** P72-2 §4 references the FR bound to
the uncorrelated vacuum and reads the sector energy
relative to the (R-marg) reference, so the priced pulse
is the excursion below that level, ending at
S(t) = +E_prep^(marg); τ₀ is the FR-raw read's τ_pulse
(entangled-ground reference — a different read). Under
the other convention the claim still stands at the
deciding rows (the five both-convention rows keep
R(τ₀) > 1, plus (10,1,2) at 5.134); only the two split
rows fall below 1. Bar met at 7 rows under τ_marg, 6
under τ₀ — not convention-dependent at the deciding
rows. **τ(N) asymptotics (m = 1; derived pair-block
route validated against the dense route to ≤ 1.2e-10;
honest reach N = 200):** τ FALLS with N for both r and
both conventions (τ₀ at r = 0.5: 0.2265 at N = 5 →
0.1831 at 10 → 0.0466 at 200; τ_marg converges to τ₀ at
large N); |E_net,B| grows and saturates (asymptote
≈ 0.41 at r = 0.5, ≈ 1.20 at r = 1); **R's growth is
NOT carried by |E_net,B| alone** — R peaks (R(τ₀)
≈ 4.67 at N = 16, r = 0.5; ≈ 13.76 at N = 20, r = 1)
then falls as τ's decline dominates (at N = 200:
1.98 at r = 0.5; 6.76 at r = 1, still > 1).
**Disclosed caveat (on the memo's face):** under
severe machine contention the three N = 10 rows were
finished by a lean route (same dense H and explicit
protocol simulation for all energies; Lanczos ground
state; pair-block S(t)), validated against dense-route
τ reads at (10,1,0.5) and (10,1,1) to ≤ 1.2e-10 before
its (10,1,2) read was believed; energies bit-identical.
**The registered claim block of §P119-1 is therefore
FILLED:** the P108-5 reopening claim, in Phase 108's
scoped words (multipartite published QET; receiving
sector net negative vs its uncorrelated reference at
R_net > 1, resource counted; finite spin model;
price line standing against it; no field claim —
P119-2 confirms none is supported; nothing FTL), is
registered for a full Gate under the τ_marg convention,
deciding rows as above, routed to the parent. The
claim does not publish from this phase. P108-5's
status: REPLICATED at Gate-style standard within this
programme — it remains a scan signal under attack
until the Gate the parent launches decides it.



### P119-3 — VERDICT: REFERENCE COMPLETED — PRICE LINE STANDS

(Worker report 2026-11-23; checker `work/p1193_checker.py`
ALL PASS — control, each row, final threshold run;
worker's checker logs on disk verified by the
coordinator, fresh coordinator re-run launched under
heavy VM contention, outcome appended when it lands.
Deliverables: `results/p1193_run_record.md`,
`results/p1193_memo.md`, `results/p1193_results.json`.)

The control passed exactly: the minimisation machinery
at N = 2 reproduces P72-2's stored E_prep^(sep) with
absolute error 0.0 at all three r (0.2360679774997898 /
0.3284271247461903 / 0.2221359549995796). The product
expectation derived from the paper's Eqs. (1)–(2),
⟨H⟩ = h·Σzᵢ + 2k·Πxᵢ + D, was verified against a dense
Kronecker H to 3.6e-15. **The separable minimum is a
closed form:** the analytic reduction proves any
minimiser is either the corner θ = 0 or a symmetric
interior critical point satisfying
h = 2k·sin^{N−2}θ·cosθ, which has NO root at any
registered row, so the minimum is the corner
|1⟩^⊗N and **E_prep^(sep) = D − N = 4k²/(D + N)** —
certified independently by 220-start L-BFGS-B over the
full Bloch manifold (matching to all stored digits) and
110,000 random product states finding none lower. The
separable floor is the SMALLER reference at every
registered row, so P72-2's deciding total does switch
to (R-sep) — but the price is injection-dominated, so
the deciding price per unit moves only to **5.34–28.17
per unit delivered** across the eight negative rows
((10,1,2): 5.340121; (6,1,1): 7.738199; (8,1,1):
9.012193; (10,1,1): 10.452606; (5,1,0.5): 16.930773;
(6,1,0.5): 19.036974; (8,1,0.5): 23.525279; (10,1,0.5):
28.170099), all > 1, and the largest Π_marg/Π_sep is
1.078 — far below the registered ≥ 2 threshold.
Neither PRICE-LINE-MOVES condition is met. **Completed
price caveat for the P108-5 claim: 5.34–28.17 per unit
delivered at the deciding rows, resource at the
separable reference, classical leg omitted — still a
lower bound.** **N-scaling:** E_prep^(sep)/E_prep^(marg)
= D/(D + N) exactly → 1/2 (measured 0.5012–0.5132 over
the registered N): the separable floor DOES dilute like
the marginal reference — both are Θ(1/N), sep ~ 2k²/N
vs marg ~ 4k²/N, the same dilution with exactly half
the leading coefficient, not a non-diluting floor.
C12: bookkeeping completion; R_net was not re-read.

### P119-4 — VERDICT: ESCAPE WORKS MECHANICALLY, FRONT STANDS (both halves)

(Worker report 2026-11-23; checker `work/p1194_checker.py`
245/245 PASS with full-margins (fast=False)
recomputation of every run; output JSON on disk
verified by the coordinator, fresh coordinator re-run
launched under heavy VM contention, outcome appended
when it lands. Deliverables:
`results/p1194_run_record.md`,
`results/p1194_memo.md`, `results/p1194_results.json`.)

Machinery gate PASS: all seven corpus configurations
reproduced (worst error 8.55×10⁻¹² vs the 1e-6 bar);
hinge-best alignment set = {44}, S_F = 1.000000.
Neither half met JOINT PASS or JOINT IMPROVEMENT;
Frontier A = 0 at every start in both halves.
**Half (a) — the non-flat profile:** the registered
non-flatness was posed everywhere (|t_kin|/D_can >
1e-6 at 44/44 former plateau points at the seed and
all 14 candidates), and the alignment set is EMPTY at
every candidate — the escape works mechanically. The
best candidate (start 7) improves legality to 0.6964
(hinge 0.5893) with health_ok TRUE and median 0.0904,
but its EoM max 0.999999999994964 exceeds the hinge
max by 1.65×10⁻¹¹, failing both Pareto clauses.
**New binding form — the all-sign pin:** at the best
candidate's worst point (51; tie set 44/50/52) all
four canonical terms share one strict sign (shares:
kin 0.385 / pxx 0.287 / FA 0.025 / FB 0.303;
S_F = 0.327) — the revived □φ joins the pin instead of
opposing it. Family A at the best candidate reads
legality 0.000: the fluid carried all of the legality
gain. **Half (b) — H_,φ(pi0) = 0:** the constraint was
imposed by parametrisation (14 starts, both β_c
branches; the hinge projected exactly onto the
constraint set, H_,φ(pi0) = 0.0 to the last digit).
The alignment set is empty at the best candidate and
at the projected seed (t_FA ≈ 1e-17 at plateau points
from the first read) — the escape works mechanically.
The best candidate (start 6, negative branch) reaches
subset_legal **0.9107**, the highest read in either
half, but its EoM max 0.9999999999878012 exceeds the
hinge's by 9.3×10⁻¹²; the trap does not fire
(max |F_A + F_B| = 0.1449). **New binding form — the
single-channel pin:** with t_FA dead and □φ ≡ 0 on the
plateau, the EoM there is t_FB alone, so the relative
residual is 1 across the whole plateau (max-residual
tie set = points 14–44 within 1e-9). **The Phase-118
boundary was NOT pressed:** best |β_c| = 0.5505,
closest approach of any run 0.4709 vs the 0.05 fence.
One re-formation is recorded as anatomy (start 8, not
best): an alignment set {19} carrying its max point
via a P_X → 0 blow-up (P_X = 1.7×10⁻⁸, terms ~1e5),
not via H_,φ. **Failure-protocol follow-ups (logged in
the memo):** (1) COMPOSE the two escapes — the
H_,φ(pi0) = 0 constraint on the non-flat profile (the
two binding forms are complementary: half (a)'s pin
needs a channel killed, half (b)'s pin needs □φ
alive); (2) a sign-targeted □φ blend aimed at the
outer-shell pin points; (3) a posed |P_X| floor guard
against alignment-by-blow-up. C12: pre-existing walls
at β = 1.1; no transport claim; the front's pin is
characterised in two further forms, not moved.

### P119-2 — VERDICT: NOT POSABLE FROM PUBLISHED FORMS (missing ingredient: clause (iii))

(Worker report 2026-11-23; checker `work/p1192_checker.py`
ALL PASS — 127 checks + the paper's Eq. (40) cross-check,
re-run by the coordinator. Deliverables:
`results/p1192_search_record.md`,
`results/p1192_memo.md`, `results/p1192_results.json`.)

The missing ingredient, named exactly: a published
field or harmonic-oscillator QET protocol with a
multipartite / multi-receiver / shared-resource
structure — more than one receiving sector drawing on
one shared interaction — in which an N-scaling of
sector correlation energy vs per-receiver extraction
can be read. The documented search (13 logged queries,
primary sources; 11 candidates assessed by name):
clauses (i)+(ii) ARE met in print — cleanly by Nambu &
Hotta's harmonic chain (arXiv:1007.2234: H Eq. 1,
Gaussian ground state Eqs. 2–5, delivered energy
Eq. 26 in closed form), in correlator form by Ikeda's
Thirring QET and Haque's thermal harmonic chain — but
every field/oscillator QET in print is single-receiver,
and the only multi-receiver QET structure in print at
all (Hotta's quantum energy distribution,
arXiv:0803.1512) is a spin-chain protocol with a
generic unspecified chain Hamiltonian and only a total
energy evaluated — wrong system class, not evaluable
per sector (Phase 108's candidate C4, carried
verbatim). No citing/generalising work transplants
Xun–Ren's shared N-body interaction into a
field/oscillator Hamiltonian. **Single-receiver anatomy
(the registered fallback, computed from the printed
forms under the inherited accounting):** in the
harmonic chain the receiving sector's marginal-product
correlation energy is E_prep^(marg,sector) = α·g₁/2 —
an intensive local two-point function of the receiver's
own bonds; it is separation-independent while the
delivered energy falls steeply with distance (at
α = 0.99: 1.885×10⁻² at d = 1 → 1.32×10⁻⁹ at d = 20;
the paper's printed critical fit d^−3.6). Under the
only "many-party" knob in print (a maximal sender
block — sender-side, not receivers sharing a resource),
extraction SATURATES in N (→ 1.717×10⁻³ at α = 0.99;
critical → 2.069×10⁻³, matching the paper's Eq. (40)
constant 0.0020613 within 1%) while the sector price
does not dilute at all (≈ 0.229 at every N).
E_net,sector > 0 at all 34 anatomy rows; R_net = 0
everywhere; no crossing at any N. **Structural reason,
stated as the scaling answer:** the spin model's 1/N
comes from ONE shared N-body term whose total
correlation energy (4k²/D, D ≈ Nh) is charged once;
field/oscillator Hamiltonians in print have local
pairwise couplings, so the receiver's price is not a
shared total divided by anything, and extraction decays
with distance instead of holding. The QEI floor never
bites: there is no below-reference pulse to price
(R_net = 0 identically), and independently the paper
prints no protocol duration (H-evolution neglected), so
no τ can be read from the published form's own
evolution; it also prints no closed-form E_in, so no
price line can be formed. **Follow-up FU-P1192-1
(registered):** a standing search criterion in
P119-5's form — reopening condition = publication of a
field/oscillator QET meeting (i)+(ii)+(iii). C12:
P108-5 keeps its finite-spin-model scope; this verdict
is precisely that the published record does not
support a field claim for it.



### P119-5 — VERDICT: NOT MET IN OUR SEARCH

(Worker report 2026-11-23; checker `work/p1195_check.py`
25/25 ALL PASS, re-run by the coordinator. Deliverables:
`results/p1195_memo.md`, `results/p1195_results.json`.)

No family in the stored record meets P108-4's reopening
criterion (a stored whole-shell static β = 1.1 /
β_p = 1.1 read with FINITE max q, Phase-63 form). The
survey table (every value checker-verified from its
cited JSON source; no prose-only values): the
Phase-16/83 bed itself reads max q = +∞ at its static
twin (Phase 83 G3; Phase 108 T3) — FAILS. The (10,30)
M = 8.0 spherical control / B1 base reads +∞ (Phases
83, 85, 76 anchor) — FAILS. The (10,30) aimed-deformation
/ travelling rows read +∞ whole-sample in every row —
FAILS; their finite reads are subset-only (worst-
direction band q = 32.739, P106-1; radial-band q =
148.420, P85-3) and by the registered scope discipline
do not meet the criterion. The (10,30) flux-first
candidate (P76-3) reads +∞ whole-shell with a finite
160.720 at the single binding point only — point-finite,
does not meet. The Phase 48 bed / coupling-force front
family is UNREAD in the q form (its β = 1.1 reads are
EoM/subset/Frontier-A form; absence checker-verified) —
the gap is named: no whole-shell static β = 1.1 max-q
read of that family exists. The Phase 26/50-era shell
families are UNREAD at 1.1 (q reads only at β ≤ 0.12).
Coverage matrix (recomputed): 1,134 cells, 1,093
never-run examined; 157 name a (material × structure)
combination whose static form is posed somewhere (21
such combinations), 936 are purely combinatorial; of
the 157, only the single-shell GR/Fuchs-(10,30)
combinations carry a β = 1.1 whole-shell max-q read —
+∞, FAIL. **Anatomy:** the criterion fails by
denominator collapse (T₀₀ + T_n̂n̂ ≤ 0 with nonzero
flux) at the inner edge in both read families — the
P63-3/P76-3 flux-overload mechanism — not by a
finite-but-large ratio. **Follow-up (logged, not run):**
reopening still requires first PRODUCING the missing
read — a whole-shell static β = 1.1 q audit of a
never-q-read family, the coupling-force front family
being the named candidate — and finding it finite. The
breathing line stands closed under P108-4's condition,
with this survey as its priced search. C12: a
search/registration verdict; no wall's legality is
claimed or approached.

## Sequencing

P119-1 … P119-5 run as separate workers with separate
result files. P119-1's verdict gates nothing else in
this phase, but a REPLICATION FAILURE is reported
immediately on landing (it changes P108-5's status
programme-wide). The coordinator re-runs every checker,
integrates verdict sections into this file
INCREMENTALLY, and writes the final synthesis:
per-item verdicts; rung verdicts with **FTL (2a)
FIRST**, then traversable wormhole / 2b / technical
results; the integrated follow-up queue (including,
on REPLICATED, the Gate registration for the P108-5
claim, routed to the parent). INTERNAL ONLY.

---

---

## PHASE 119 — FINAL SYNTHESIS (coordinator, 2026-11-23)

**Plain language first.** Phase 108's one surprise — a
many-party quantum-energy-teleportation scheme whose
books show net negative energy delivered to one
receiver, with the entanglement fully paid for — was
put through the three tests it owed, and it passed the
one that mattered most: an independent rebuild from the
published paper, by machinery that never touched the
original code, reproduces every number. Its price is
now fully booked too: even against the cheapest
possible uncorrelated preparation, delivering one unit
costs between 5.3 and 28 units, so it remains a
bookkeeping phenomenon, not an energy source. And the
field version everyone would actually want does not
exist in print: every field or oscillator version of
the trick has exactly one receiver, and in the one
fully worked example the receiver's price is a local
quantity that does not thin out as parties are added,
while what can be extracted fades with distance — the
dilution that powers the spin-model result is a
property of that model's single shared interaction,
not of the trick in general. On the wall front, both
registered escapes from the coupling-force pin work
exactly as designed — the force alignment that carried
the worst point is gone in both — and the wall does not
move anyway: each escape leaves the equation pinned at
full residual in a new, simpler form (all four terms
pointing the same way in one; a single surviving force
term in the other). Legality actually improved a lot
under the second escape (0.59 → 0.91 of the audited
points) while the equation stayed pinned, which is the
cleanest statement yet that on this front legality and
solvability are separate walls. Finally, the breathing
wall's reopening condition was priced as a search: no
wall family in the entire record has ever posted a
finite whole-shell flux ratio at the superluminal
speed, so that line stays closed until someone first
produces the missing measurement on a family that has
never been measured that way.

### Rung verdicts (FTL first, as tasked)

- **FTL (2a): NO.** No joint (i) legality +
  (ii) solution-grade improvement at any superluminal
  cell in this phase: P119-4's both halves read
  Frontier A = 0 at every start, and the phase's
  positive result (P119-1) is a sourcing-accounting
  read in a finite spin model — C12: not transport,
  not a wall, nothing FTL claimed. Every superluminal
  row remains EFFECTIVE ONLY or worse.
- **Traversable wormhole: NO as an unqualified claim,
  with the sourcing gap now replicated and fully
  priced.** The multipartite QET reopening (P108-5) is
  REPLICATED at Gate-style standard (P119-1), ruled to
  the τ_marg convention with the claim standing under
  τ₀ as well, and registered for a full Gate (parent
  launches it). Its price line is completed (P119-3:
  deciding price 5.34–28.17 per unit delivered,
  resource at the separable floor). Its field analogue
  is NOT POSABLE from the published record (P119-2) —
  the spin-model scope is final unless the literature
  changes. No throat was posed or improved; the
  conformal member's other gaps are untouched.
- **Practical near-c (2b): NO CHANGE.** No subluminal
  configuration was attempted.
- **Technical results: YES ×5**, recommended for the
  ledger's GATE-QUEUED tier (internal, ungated):
  (1) the Gate-style replication of the multipartite
  QET reopening — all 30 rows, energies bit-exact, τ
  to ~2e-9 — with the τ_marg convention ruling and the
  τ(N) asymptotics (τ falls with N; R peaks then
  declines, still > 1 at N = 200 for r = 1) (P119-1);
  (2) the field/oscillator analogue's not-posability,
  with the harmonic-chain anatomy showing the sector
  price intensive and non-diluting and extraction
  distance-decaying (R_net = 0 at all 34 rows) (P119-2);
  (3) the separable-minimum reference in closed form,
  E_prep^(sep) = 4k²/(D + N), diluting as Θ(1/N) with
  half the marginal reference's leading coefficient,
  and the completed price line (P119-3); (4) both
  alignment escapes working mechanically (alignment
  set empty in both) while the front stands, with two
  new binding forms named — the all-sign pin and the
  single-channel pin — and legality 0.9107 read under
  the H_,φ(pi0) = 0 constraint (P119-4); (5) the
  breathing reopening criterion's priced search: no
  family in the record meets it, the coupling-force
  front family named as the unread gap (P119-5).

### Integrated follow-up queue (ordered)

1. **THE GATE for the P108-5 claim** — registered in
   §P119-1's claim block (τ_marg convention; deciding
   rows (6,1,0.5), (8,1,0.5), (8,1,1), (10,1,0.5),
   (10,1,1), plus (10,1,2) under τ₀; price line
   5.34–28.17 completed form), routed to the parent.
   The claim joins the push queue only if the Gate
   passes it, under the standing publication rule.
2. **FU-P1194-1 — COMPOSE THE TWO ESCAPES:** the
   H_,φ(pi0) = 0 constraint imposed on the non-flat
   profile family, on the coupling-force front at
   β = 1.1. Grounding: the two halves' binding forms
   are complementary — half (a)'s all-sign pin lacks a
   killed channel, half (b)'s single-channel pin
   lacks a live □φ — and each half emptied the
   alignment set, so the composition is the
   mechanism-suggested next registration (a new
   mechanism in the anti-loop sense: neither half
   re-run). Bars inherited from §P119-4 verbatim,
   including the Phase-118 boundary and the trap gate.
3. **FU-P1194-2 — the sign-targeted □φ blend** aimed
   at the outer-shell pin points (half (a)'s tie set
   44/50/52), and **FU-P1194-3 — a posed |P_X| floor
   guard** against alignment-by-blow-up (half (b)'s
   start-8 anatomy). Both logged from P119-4's memo;
   they run under their own registrations, after or
   alongside FU-P1194-1 as the parent sequences.
4. **FU-P1195-1 — PRODUCE THE MISSING READ:** a
   whole-shell static β = 1.1 max-q audit (Phase-63
   form) of the coupling-force front family — the
   named never-q-read family. If it reads finite, the
   breathing criterion (P108-4) is met by that family
   and a breathing registration becomes posable; if
   +∞, the criterion's search closes on a read, not
   on an absence.
5. **FU-P1192-1 — standing search criterion:** the
   field/oscillator analogue reopens only on
   publication of a field/oscillator QET meeting
   clauses (i)+(ii)+(iii) of §P119-2. No active work;
   the criterion is the deliverable.
6. **FU-P106-4a — the ℬ-guided search: STILL
   UNPROMISED**, carried verbatim from Phase 106
   through Phase 108; it runs only under its own
   future registration.

**Anti-loop compliance:** P119-4's halves were Phase
108's own registered escapes, run once each, under
their stated conditions; their composition is queued
as a new mechanism, not a third run of either. P119-5
ran no breathing — it priced the reopening criterion
as a search, as registered. The QET items ran under
Phase 106's inherited reopening bar and Phase 108's
queue; the line's field extension is closed on the
published record with a stated reopening condition
(publication), not on a failed run. INTERNAL ONLY —
nothing uploaded, nobody contacted.

## Phase status: CLOSED (2026-11-23)

Deliverables: this checkpoint; `results/` (p1191–p1195
run records, memos, results JSONs) and `work/` (scripts
+ checkers: P119-1 ALL PASS, P119-2 ALL PASS, P119-3
ALL PASS, P119-4 245/245, P119-5 25/25 — coordinator
re-runs: P119-1/2/5 fresh ALL PASS; P119-3/4 workers'
outputs verified from disk, coordinator re-runs
launched under contention, logs in `work/`). No worker
number was altered by the coordinator.

**Coordinator addendum (2026-11-23, later):** both
outstanding coordinator checker re-runs have now
landed — `work/p1193_coord_rerun.log` ends CHECKER
RESULT: ALL PASS, and the P119-4 re-run regenerated
`work/p1194_checker_output.json` at 245 checks /
245 pass. All five items' checkers are therefore
coordinator-re-run-verified ALL PASS; the contention
caveat in the status header and synthesis is retired.
