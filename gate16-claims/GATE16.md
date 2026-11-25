# GATE-16 — the two Phase 128 superluminal-front improvements

Claims under audit: G16-1 (P128-1, the composed escapes) and G16-2
(P128-2, the sign-targeted □φ blend + the coverage law), both at
β = 1.1 on the coupling-force front registered in §P119-4 /
CHECKPOINT128 ("The registered front").

**Verdicts: G16-1 SURVIVED INTACT. G16-2 SURVIVED INTACT.**
Both claims join the publication queue automatically under
Rakshit's standing rule, in the wordings of §7 verbatim. The gate
uploaded nothing.

**Plain language first.** Phase 128 said the superluminal wall's
front moved twice: once by combining two known escapes, once by
aiming a curvature term's sign at the bad points — and that the
worst point migrates to whichever bad point the aim doesn't cover.
I rebuilt both configurations from their stored data on machinery
written fresh for this gate, re-derived the old champion (the
hinge best) on the same machinery, and every deciding number came
back: the legality jumps (0.589 → 0.929 and → 0.786), the
worst-point equation errors (down by 1.9×10⁻⁵ and by 1.94×10⁻³),
the medians (one worse, one better — both as registered), and the
migration read exactly (opposition posed at points 50/51/52, the
worst point lands on 44, the one point left uncovered). Neither
claim is a pass — the pass mark (Frontier A) is 0 everywhere, and
both wordings say so. A later phase (130) found the health clause
that fails in G16-2 is curable in closed form in a neighbouring
pose; that is recorded in §5 as a separate fact — it does not
change G16-2 as registered, whose configuration still fails it.

## 1. Recovery and independence audit (on the face of the record)

The first Gate-16 coordinator died in a daemon restart
(2026-11-23 ~08:39 PT) after writing its auditor
(`gate16/work_a/g16_audit.py`, `g16_run.py`) and completing its
run (`gate16/results/wa_results.json`). The recovery coordinator
audited the recovered machinery before relying on it:

- **Independence.** `g16_audit.py` implements the hinge E_total
  assembly, the canonical EoM terms (t_kin = □φ, t_pxx,
  t_FA = F_A/P_X, t_FB = F_B/P_X), the relative-residual
  statistics, the alignment set, the targeting read, the
  health / Frontier A / trap reads, and both profile blends
  (single-sine; K = 3 sine sum) in-file, from the registered
  formulas. It imports NO Phase 101/119/128 work code. Its only
  programme imports are datum machinery that predates the claims
  and defines the bed itself: `phase76/p761_lib` (the Wall, H(φ),
  fluid stress-energy, margins) and `phase18/p182_engine` +
  `p182_basis` (Lagrangian basis, profile splines, stencil) —
  the same datum layer every gate since Gate-11 has shared; all
  deciding machinery is the gate's own.
- **Inputs.** The run reads only stored DATA: the hinge z and ρ₀
  (verbatim from the registered front), Phase 101's stored corpus
  (machinery gate), and Phase 128's stored best/targeted
  configurations (z, blend parameters, ρ₀). The recovery
  coordinator verified byte-identity of every z/blend used
  against `phase128/results/p128{1,2}_results.json` (checker
  assertions `g161_z_matches_stored`, `g162_z_matches_stored`,
  `g162t_z_matches_stored`).
- **Completeness.** `wa_results.json` contains the full
  registered read set for all four configurations (hinge,
  P128-1 best, P128-2 best, P128-2 targeted): both legality
  forms, EoM max AND median on the non-degenerate set, health
  clauses, alignment sets, targeting reads, term decompositions
  at the worst point, and both Pareto comparisons. No deciding
  read was missing; nothing had to be re-run. The one component
  the dead coordinator had NOT produced — an independent checker
  — was written by the recovery coordinator (`gate16/g16_check.py`,
  §6). The novelty audit (§6 below, search log at
  `results/g16_search_log.md`) is likewise the recovery
  coordinator's.

## 2. The claims as registered (CHECKPOINT128, verdicts §P128-1/§P128-2)

Front: Phase 48 bed at β = 1.1, 56-point subset, hinge theory of
P101-5 Part B. Hinge best (family B, start 6): subset_legal
0.5892857142857143; EoM rel max (nondeg) 0.9999999999784565;
median 0.22437629566157347; n_nondeg/n_deg 56/0; health False;
Frontier A 0.000; alignment set {44}. Bars: JOINT IMPROVEMENT =
Pareto-dominating the hinge best on (subset_legal, EoM rel max)
under either clause; JOINT PASS = Frontier A > 0 with n_nondeg
≥ 28 and the trap not firing.

- **G16-1.** Composing the two escapes (non-flat profile blend
  AND H_,φ(π₀) = 0): subset_legal 0.9285714285714286 (search
  read) / 0.9464285714285714 (full-margins second path, 53/56);
  EoM rel max 0.999981215379503 (a 1.9×10⁻⁵ move); median
  0.47963896879690177 (WORSENED vs 0.22437629566157347);
  alignment set empty; worst point 44 carried by t_FB
  (share 0.881882) with the live □φ same-sign (t_kin share
  0.118079) and t_FA = +2.31×10⁻⁶ (the posed zero holds);
  health False; Frontier A 0.0.
- **G16-2.** The □φ-sign-targeted K = 3 blend (best, start 12):
  subset_legal 0.7857142857142857; EoM rel max 0.9980625645582593
  (a 1.94×10⁻³ move); median 0.14496119199937418 (improved) —
  all three coordinates improved; health False on the cr2 clause
  (H_min 0.469, PX_min 2.784 pass); Frontier A 0; alignment
  empty; the best candidate is itself NOT targeted (named 1/4),
  its worst point 52 a kinetic pin (t_kin share 0.843, t_FB
  0.156, same sign). The best TARGETED candidate (start 5:
  legal 0.5357142857142857, EoM max 0.9996997984797714) achieved
  opposition at 50/51/52 exactly as posed, and its worst point
  migrated to 44, the one unopposed named point, as an
  FB-dominated pin (t_FB share 0.854, t_kin share 0.064).
  Coverage law as registered: the pin migrates to whichever
  named point the opposition does not cover; opposition at a
  point works, coverage is the binding constraint.

## 3. Machinery gate (the gate's own machinery, before any deciding read)

The gate's `canonical_terms` reproduced all seven unique corpus
configurations' stored EoM max/medians from
`phase101/results/p1015_partB_raw.json`: worst error
8.54938342342848e-12 (bar 1e-6; the same precision Phase 119's
machinery recorded). Hinge alignment set on the gate's machinery:
{44}, S_F = 1.000000. MACHINERY GATE PASS.

## 4. Deciding reads (gate's own machinery; both sides of each comparison)

| read | hinge best | P128-1 best | P128-2 best | P128-2 targeted |
|---|---|---|---|---|
| subset_legal (fast) | 0.5892857142857143 | 0.9285714285714286 | 0.7857142857142857 | 0.5357142857142857 |
| subset_legal (full margins) | 0.5892857142857143 | 0.9464285714285714 | 0.7857142857142857 | 0.5357142857142857 |
| EoM rel max (nondeg) | 0.9999999999784565 | 0.999981215379503 | 0.9980625645571286 | 0.9996997984797714 |
| EoM rel median (nondeg) | 0.22437629566157347 | 0.47963896879690177 | 0.14496119326202822 | 0.17132470134865474 |
| n_nondeg / n_deg | 56 / 0 | 56 / 0 | 56 / 0 | 56 / 0 |
| health_ok | False | False | False | False |
| cr2 range | [1.0, 1.0008488] | [1.00000007, 1.0009867] | [1.00000002, 1.0027938] | [1.0000014, 1.0083984] |
| H_min / PX_min | 0.3854 / 1.2218 | 0.9053 / 1.7679 | 0.4691 / 2.7835 | 0.6388 / 0.1327 |
| alignment set | {44} | ∅ | ∅ | ∅ |
| worst point | 44 | 44 | 52 | 44 |
| Frontier A | 0.0 | 0.0 | 0.0 | 0.0 |

Comparisons on the gate's reads. G16-1 vs hinge: Δlegal
+0.3392857 (subset) / +0.3571429 (full); ΔEoM max
−1.87846×10⁻⁵ (strictly below); Δmedian +0.2552627 (worse).
Both registered Pareto clauses TRUE. G16-2 vs hinge: Δlegal
+0.1964286; ΔEoM max −1.93744×10⁻³; Δmedian −0.0794151 — all
three coordinates improved; both Pareto clauses TRUE. Agreement
with the phase's stored reads: exact on every legality fraction
and on G16-1's EoM max; G16-2's EoM max agrees to 1.1×10⁻¹² and
its median to 1.3×10⁻⁹ (independent-machinery precision, far
inside the 1e-6 registered tolerance).

Anatomy re-derived. G16-1 at point 44: t_FB +0.06926043659593377
(share 0.881882), t_kin +0.009273557882887383 (share 0.118079,
same sign — the live □φ joins the pin), t_FA
+2.3124581666039688×10⁻⁶, H_,φ(π₀) = 0.0 exactly; alignment set
empty (both escapes work mechanically as posed). G16-2 best at
point 52: t_kin +0.08721156438193656 (share 0.843), t_FB
+0.016132799905004675 (share 0.156), same sign — a kinetic pin;
its targeting read opposes exactly one named point (44), so it
is not itself targeted (named 1/4), as registered.

**The migration read, re-derived.** Gate targeting reads on the
named set {44, 50, 51, 52} (live = both t_kin and t_FB above the
registered 1e-6 liveness floor; opposed = live with
t_kin·t_FB < 0):
- Hinge best: 50, 51, 52 live and opposed; 44 NOT live
  (t_kin = 2.0×10⁻⁵⁸ — the □φ channel is dead on the plateau)
  and 44 is the alignment pin and worst point. The uncovered
  point carries the front.
- P128-2 targeted candidate: opposed exactly {50, 51, 52};
  44 live but not opposed; worst point = 44, an FB-dominated
  pin (t_FB share 0.854, t_kin share 0.064, same sign).
- P128-2 best: opposed {44} only; worst point 52, where the
  opposition does not reach (same-sign kinetic pin).
In each configuration the worst point sits at a named point the
opposition does not cover, and where opposition is posed
(50/51/52 in the targeted candidate) the pin leaves those
points. The coverage law reproduces as registered.

## 5. The health clause, and the Phase 130 confrontation

On the gate's machinery, health fails at the hinge best and at
both improvement candidates on the cr2 clause ALONE: H_min > 0
and PX_min > 0 everywhere; cr2_max > 1 everywhere (hinge
1.0008488; P128-1 1.0009867; P128-2 1.0027938). G16-2's
registered attribution (health fails on cr2) is confirmed, and
the same attribution holds for G16-1, whose phase record stated
health False without naming the clause.

**Post-claim development, recorded as a separate fact (Phase
130, P130-4, INDEPENDENTLY CURABLE, its checker 25/25):** the
cr2 clause has the closed form cr2 − 1 = −4p₂X/(p₁ + 6p₂X) for
this P(X) family; on the β_c = 0 slice front, X < 0 at all 56
points at the deciding z, so p₂ > 0 forces cr2 > 1 and setting
p₂ = 0 at that z attains health True at exactly the slice best's
legality (0.625) and EoM max. The gate notes the consistency:
G16-2's best carries p₂ = +0.06174935270709549 > 0 and its cr2
excess is of the same sign structure. **Ruling:** G16-2 is
audited AS REGISTERED — its configuration has p₂ > 0 and fails
health on cr2; the Phase 130 cure was demonstrated at a
different configuration on a different (slice) front, and no
p₂ ≤ 0 re-pose of the G16-2 blend has been run by any phase.
The cure neither amends nor weakens the claim; it is the
already-logged follow-up (P128-2's posed cr2 guard) now known to
have a closed-form target. The claim's fence stands verbatim in
its wording: health failed on the cr2 clause in the registered
configuration.

## 6. Checker and novelty audit

**Checker:** `gate16/g16_check.py`, written by the recovery
coordinator, re-deriving every deciding number from the gate's
own `wa_results.json` against the registered claim values and
the registered bars (it does not read the phase's checkers):
**70/70 PASS** (output at `results/g16_check_output.json`).

**Novelty audit:** documented search (4 verbatim queries,
2026-11-23; log at `results/g16_search_log.md`). Scoped to the
claims' exact category — joint (legality + solution-grade)
improvements on a superluminal warp front by profile composition
/ sign-targeted coupling terms — **grade: NOVEL (delimited)**
for both claims. No published work found poses or moves this
front, and neither mechanism (composing the non-flat profile
with the exact H_,φ(π₀) = 0 constraint; the □φ-sign-targeted
blend) nor the coverage/migration law has a published
counterpart in the searched literature. Near neighbours, named:
Warp Factory (arXiv:2404.03095 / 2404.10855 — numerical
optimisation of GR warp metrics; metric-first, no matter-action
front); Bobrick & Martire (arXiv:2102.06824 — GR shell
classification); Lentz's positive-energy solitons
(arXiv:2201.00652); Santiago–Schuster–Visser (arXiv:2105.03079
— the all-observer fence on GR claims); Le's warpax
(arXiv:2602.18023 — verification tooling); Jusufi & Lobo
(arXiv:2609.05554); Rodal (arXiv:2507.09724); Lobo & Visser
(gr-qc/0412065). The programme's own earlier front moves
(Phases 89/103/108/112/118/119) are the internal lineage, cited
as such. Gaps, stated: English-language web + arXiv abstract
level only; no Google Scholar / INSPIRE full-text search;
subscription literature at abstract level; non-English
literature not searched. The claims are internal-front
statements inside the programme's own designer theory — the
grade covers exactly that category, nothing wider.

## 7. Verdicts and upload wordings (verbatim)

**G16-1: SURVIVED INTACT.** The registered claim — both legality
forms, the strict EoM-max move, the worsened median, the empty
alignment set, the point-44 anatomy — is reproduced in full by
the gate's independent machinery. No restatement is required.
The claim may be carried only in this wording:

> **First joint legality + solution-grade improvement on the
> programme's superluminal front, by composing the two escapes.**
> On the registered front (Phase 48 bed at β = 1.1, 56-point
> subset, hinge theory), composing Phase 119's two escapes — a
> non-flat profile blend AND the exact constraint
> H_,φ(π₀) = 0 — Pareto-dominates the hinge best: subset
> legality 0.5892857142857143 → 0.9285714285714286 (search read)
> / 0.9464285714285714 (full-margins second path), with the
> worst-point relative EoM residual strictly below the hinge
> best's, 0.9999999999784565 → 0.999981215379503 (a 1.9×10⁻⁵
> move). **Fences, inseparable:** Frontier A = 0 — an
> improvement, not a pass; no legal superluminal configuration
> is claimed. The median EoM residual WORSENED
> (0.22437629566157347 → 0.47963896879690177). Health fails
> (on the cr2 clause). The alignment set is empty — both
> escapes work as posed — and the pin re-forms one point out,
> at point 44, carried by t_FB (share 0.882) with the live □φ
> same-sign. Accounting (C12): a pre-existing wall at β = 1.1
> inside one designer scalar+fluid theory; a moved front is
> not a legal wall, and nothing here implies transport or
> anything faster than light in the world.

**G16-2: SURVIVED INTACT.** The registered claim — all three
coordinates improved, health failing on cr2, the best candidate
not itself targeted, and the coverage law on the targeted
candidate — is reproduced in full. No restatement is required.
The claim may be carried only in this wording:

> **Second joint improvement on the same front, by sign-targeted
> opposition — and the coverage law.** A profile blend whose □φ
> sign is targeted at the named pin points improves all three
> coordinates against the hinge best at once: subset legality
> 0.5892857142857143 → 0.7857142857142857, worst-point relative
> EoM residual 0.9999999999784565 → 0.9980625645582593
> (a 1.94×10⁻³ move, ~100× G16-1's), median
> 0.22437629566157347 → 0.14496119199937418. **Fences,
> inseparable:** Frontier A = 0 — an improvement, not a pass;
> no legal superluminal configuration is claimed. Health fails
> on the cr2 clause in the registered configuration
> (cr2 max 1.0028; H and P_X clauses pass). The best candidate
> is not itself targeted (named 1/4; its worst point 52 is a
> same-sign kinetic pin). The coverage law, on the best
> targeted candidate: opposition posed at points 50/51/52 works
> there, and the worst point migrates to point 44, the one
> named point left unopposed — opposition at a point works;
> coverage is the binding constraint. (Separate later fact,
> not part of this claim: Phase 130 showed the cr2 clause is
> curable in closed form — p₂ = 0 — at a slice-front
> configuration; no such re-pose of this blend has been run.)
> Accounting (C12): a pre-existing wall at β = 1.1 inside one
> designer scalar+fluid theory; a moved front is not a legal
> wall, and nothing here implies transport or anything faster
> than light in the world.

**Status: COMPLETE** (recovered run audited and complete;
checker 70/70 by the recovery coordinator; novelty audit
complete; record closed 2026-11-23). Both claims join the
publication queue in the wordings above; the gate uploaded
nothing and contacted nobody.

---

**GATE-19 CORRECTION (2026-11-23, append-only; gate19/GATE19.md):**
this gate's deciding legality reads consumed p761_lib.fluid_T,
which Gate-19 proves computed A*That*A^T where the tetrad identity
requires A^T*That*A (defect proven in phase166/CHECKPOINT166.md
P166-4; independently reproduced and fixed at source by Gate-19).
Re-read on Gate-16's own machinery (copied, output redirected)
under the corrected tensor, venv frame + Phase 166 pin: hinge
subset legality 0.5892857142857143 -> 0.75 (both margin forms);
P128-1 best 0.9285714285714286 / 0.9464285714285714 ->
0.8928571428571429 (both forms); P128-2 best 0.7857142857142857
-> 0.6071428571428571; P128-2 targeted 0.5357142857142857 ->
0.42857142857142855. Every EoM number, health clause, alignment
set and worst point above is bit-identical (the canonical path
does not consume fluid_T). GATE-19 VERDICTS: G16-1 SURVIVES IN
RESTATED WORDING (legality 0.75 -> 0.8928571428571429, still
Pareto-dominating the corrected hinge on both clauses); G16-2
FAILS as a joint improvement (its legality coordinate reverses
against the corrected hinge, 0.6071428571428571 < 0.75; its EoM
coordinates and the coverage law stand as anatomy). The wordings
in S7 above are superseded accordingly; do not quote the stored
legality numbers without this note.
