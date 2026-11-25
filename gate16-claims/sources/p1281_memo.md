# P128-1 memo — FU-P1194-1: compose the two escapes

Registration: `../CHECKPOINT128.md` §P128-1. Pose, seeds and
bars fixed before numbers in `p1281_run_record.md`. Numbers:
`p1281_results.json`; scripts in `../work/` (`p1281_gate.py`,
`p1281_search.py`, `p1281_assemble.py`, `p1281_checker.py`).

## RECOVERY DISCLOSURE (on the face)

The original worker session for this item ended without a
final report. This memo was completed by a **recovery
finisher** from the checkpointed disk state, not from the
original worker's account. What the disk state showed, and
what the recovery did:

- The machinery gate had run and passed (log preserved).
- **First pass** (`p1281_search.log`): starts 0–4 logged;
  start 0's optimisation **errored with a shape broadcast
  error — "could not broadcast input array from shape
  (284,) into shape (285,)"** — the half-(b) variable-length
  penalty residual changed length when the trajectory
  crossed a guard boundary. **Fix in the second pass:** the
  residual was rewritten with fixed-shape penalty slots
  (0.0 when the guard is satisfied), as commented in
  `p1281_search.py`.
- **Second pass** (`p1281_search2.log`): starts 0–7
  completed and checkpointed to `p1281_ckpt.jsonl`
  (8 records); start 8 had a SEED line and no RUN — the
  pass was **incomplete** when the session ended.
- **Recovery:** verified the gate from the preserved log,
  then ran `p1281_search.py 8 16` to completion
  (`p1281_search3.log`), checkpoint-appending starts 8–15
  in the same format. No start was dropped or re-run:
  the final record is **16 starts (0–15)**, the 8 named
  seeded starts (0–8 per the run record's list, including
  registered (i), (ii) with both named (A, λ) seedings,
  and (iii)) plus the 7 registered random seeds 9–15.
  The recovery then ran `p1281_assemble.py` and
  `p1281_checker.py`, which had been written but never run.

## VERDICT: JOINT (i)+(ii) IMPROVEMENT (milestone)

The best candidate (start 2: half (b)'s best re-posed on
the blend at half (a)'s best (A, λ)) Pareto-dominates the
P101-5B hinge best on the registered pair
(subset_legal, eom_rel_max_nondeg), under **both**
registered clauses:

- subset_legal = **0.9285714285714286** ≥ 0.5892857142857143
  (hinge) AND eom_rel_max_nondeg = **0.999981215379503** <
  0.9999999999784565 (hinge) — clause 1 met;
- subset_legal > hinge AND eom_rel_max_nondeg ≤ hinge —
  clause 2 also met.

**Second path (as registered, before this memo calls
it):** the independent checker recomputed every run from
its stored (z, A, λ, ρ₀) with canonical terms written in
the checker and legality via full margins (`fast=False`,
the `p1015_checker.py` pattern). It reproduced the best
candidate's EoM max within 1e-6 and read its subset_legal
**higher** — **0.9464285714285714** (53/56) — than the
search's fast-margins read (52/56). The improvement holds
under the second path with margin to spare on the
legality coordinate. Per the programme's language rule
this is a scan signal under attack until a later Gate
verifies it; it is the programme's first joint
improvement *on this front*, stated exactly so.

**It is NOT a JOINT PASS:** Frontier A = 0.0 at the best
candidate (health_ok = False, and the EoM max ≈ 0.99998
is far above the 0.02 pass clause). The trap does not
fire (Fsum_maxabs = 0.13215611237163147 ≫ 1e-9).

## Machinery gate

PASS, before any deciding read. All seven unique corpus
configurations' stored EoM max/medians reproduced via
`p1015_lib.canonical_terms`, worst error
8.54938342342848×10⁻¹² (tolerance 1e-6); hinge best's
alignment set = {44}, S_F = 1.0; blend jets FD-verified
(d1 rel 7.24×10⁻¹⁰, d2 rel 4.74×10⁻⁷, both < 1e-6).

## Best candidate — full standing read

Start 2, family B. z = (0.6317779811527673,
−0.549270312351474, −1.661656318450654, 0.6898641308314336,
0.877562831720773, 1.7687341210494216, 0.017415750183995916,
−0.17939843167030622); A = −0.04538543038954925,
λ = 4.635264154193024, ρ₀ = 0.04999986064110258.
Content set: the 56-point subset, all 56 non-degenerate.

- subset_legal = 0.9285714285714286 (search read) /
  0.9464285714285714 (full-margins second path)
- EoM rel max (nondeg) = 0.999981215379503
- EoM rel median (nondeg) = 0.47963896879690177 — **worse
  than the hinge best's median 0.22437629566157347**;
  reported as anatomy (scope honesty): the registered
  improvement bar is the (legal, max) Pareto pair, and
  the median moved the other way.
- n_nondeg / n_deg = 56 / 0; health_ok = False;
  Frontier A = 0.0; alignment set = {} (empty);
  max-residual point 44, not in any alignment set.
- Guards at the candidate: |2ξ+β₂| = 0.3981003561451195
  ≥ 0.2, pi0 = 0.6898641308314336 ∈ [0.02, 2.9],
  |β_c| = 0.549270312351474 — all strict.
- Non-flatness test: **passed** — |t_kin|/D_can > 1e-6 at
  44/44 former plateau points (majority required: > 22).
  Every one of the 16 runs also reads 44/44.
- Phase-118 fence: |β_c| closest approach over all runs
  = **0.053131893737917754** (start 8's candidate), i.e.
  0.00313 above the 0.05 fence; the boundary was not
  pressed under the registered test and the β_c = 0 slice
  was never entered.

## The composition's deciding anatomy (at the best candidate)

Maximum-residual point **44** (tie set within 1e-9: {44}
alone). Signed term decomposition, D_can =
0.07853704458077647, rel residual = 0.999981215379503:

- t_kin = □φ = **+0.009273557882887383** (share 0.118079)
- t_pxx = −7.376437887112905×10⁻⁷ (share 9.39×10⁻⁶)
- t_FA = **+2.3124581666039688×10⁻⁶** (share 2.94×10⁻⁵)
- t_FB = **+0.06926043659593377** (share 0.881882)

The memo question, answered explicitly:

- **t_kin does NOT oppose t_FB at the worst point.** Both
  are strictly positive; the live □φ (11.8% share — the
  composition did keep it alive there) *joins* t_FB
  instead of opposing it.
- **t_FA is at its posed zero in the registered sense:**
  H_,φ(pi0) = 0.0 exactly by the parametrisation
  (pi0 = β_c/(2(2ξ+β₂)) is an identity at the candidate),
  and t_FA at point 44 is 2.31×10⁻⁶ (share 2.9×10⁻⁵);
  max |t_FA| over the former plateau points is
  7.329917974100926×10⁻⁴.

**Binding form (named): the single-channel FB pin at the
migrated worst point.** With t_FA posed to zero and
t_pxx negligible, the EoM residual at point 44 is t_FB
alone in effect (88.2% of D_can), and the one live
opposing-capable channel the composition added — □φ —
carries the pin's own sign there. This is half (b)'s
single-channel pin re-formed at the first outer point
rather than on the plateau: the composition works
mechanically (both escapes posed simultaneously, the
alignment set empty everywhere), the front moved on
legality, and the EoM max remains pinned at ≈ 1 by
t_FB at point 44.

## All 16 starts (optimised candidates, family B)

Every run: Frontier A = 0.0, alignment set empty,
kin_live 44/44, guards_ok true, n_nondeg 56.

| start | legal | EoM max | EoM median | health | \|β_c\| |
|---|---|---|---|---|---|
| 0 | 0.5179 | 0.999999999996 | 0.1898 | True | 0.1173 |
| 1 | 0.6250 | 0.999988627687 | 0.2126 | False | 0.6391 |
| **2** | **0.9286** | **0.999981215380** | 0.4796 | False | 0.5493 |
| 3 | 0.5179 | 0.999999999998 | 0.3037 | True | 0.2387 |
| 4 | 0.6607 | 0.999981929546 | 0.9649 | False | 0.8302 |
| 5 | 0.1964 | 0.999997624418 | 0.9190 | False | 2.4513 |
| 6 | 0.1964 | 0.999999999986 | 0.9792 | False | 2.4513 |
| 7 | 0.3929 | 0.999988277039 | 0.9770 | False | 1.4683 |
| 8 | 0.5000 | 0.999999999999 | 0.2765 | True | 0.0531 |
| 9 | 0.5714 | 0.999997719059 | 0.5746 | False | 1.0534 |
| 10 | 0.0000 | 0.999999999999 | 0.8633 | False | 2.7605 |
| 11 | 0.3571 | 0.999999999999 | 0.9983 | True | 1.3797 |
| 12 | 0.1071 | 0.999758107098 | 0.9417 | False | 0.6957 |
| 13 | 0.0000 | 0.999999419474 | 0.9945 | False | 2.1061 |
| 14 | 0.4643 | 0.999999999998 | 0.8792 | True | 1.7654 |
| 15 | 0.5179 | 0.999996227727 | 0.2962 | False | 0.5025 |

Seeded-start (initial configuration) reads are stored in
full in `p1281_results.json` (`seed_starts`). Note from
the run record, restated: start 0's *seed* sits inside
the guard penalty zone (|2ξ+β₂| = 0.1457 < 0.2, the
registered projection of half (a)'s best); its optimised
candidate satisfies the guards strictly, as every
deciding candidate must.

Starts 1, 2 and 4 also individually Pareto-dominate the
hinge best on the registered pair; start 2 is the best
by the registered selection key. No run anywhere met
the JOINT PASS bar (Frontier A = 0.0 in all 16).

## Family A at the best candidate

Same z and (A, λ), no fluid: subset_legal = 0.0, EoM rel
max = 0.999981215379503, median = 0.47963896879690177,
n_nondeg/n_deg = 56/0, health_ok = False, Frontier A =
0.0, alignment set empty, max-residual point 44 with the
identical term decomposition (the EoM terms are
fluid-independent). The improvement is a family-B
(fluid-carrying) result; family A at the same couplings
is legal nowhere on the subset.

## Checker — 273/275, and the two non-passes resolved

`p1281_checker.py` (independent canonical terms,
full-margins `fast=False` legality) ran to completion:
**273/275 PASS**, including `verdict_form` (stored
verdict recomputed = JOINT (i)+(ii) IMPROVEMENT),
`verdict_flags`, the gate, the constraint/guard/fence
checks at every run, the best-candidate decomposition,
the kin-opposition flag and the posed-zero check.

The two non-passes are the same one-point discrepancy
twice — `run2_legal` (indep 0.946429 vs stored 0.928571)
and `seed2_legal` (indep 0.928571 vs stored 0.910714) —
and they are resolved, not waved: at **subset point 51**,
in both configurations, the search path's fast margins
(`hawking_ellis_margins` with fallback off) return NaN,
recorded as −1.0 (illegal) on all four EC margins, while
the full-margins computation returns all four margins
positive but tiny (run 2: NEC 3.40×10⁻⁵, WEC 2.55×10⁻³,
SEC 3.19×10⁻⁴, DEC 5.69×10⁻⁶; seed 2: NEC 3.96×10⁻⁵,
WEC 2.72×10⁻³, SEC 1.41×10⁻⁴, DEC 6.90×10⁻⁶). The
registered second path is the full-margins one, so the
deciding legality read for the claimed improvement is
0.9464285714285714; the stored search reads are left as
computed (fast margins) and the difference is exactly
1/56 in the conservative direction for the search read.
No verdict-carrying number fails under the second path:
the EoM max, the counts, health, the trap, the anatomy
and the verdict form all reproduce.

## Failure protocol (for the part that did not move)

Anatomy: the EoM max did not move materially anywhere
(best 0.999981215379503; all 16 runs ≥ 0.9997581070983811)
because at the worst point the residual is t_FB with an
88% share while the only other live channel, □φ, takes
t_FB's sign. The composition removed both registered
pins as posed (alignment empty; plateau no longer
single-channel — □φ is live at 44/44 plateau points) and
the pin re-formed one point out, at 44, in single-channel
FB form. Mechanism-suggested follow-up, already in this
phase's queue: **P128-2 (FU-P1194-2)** poses the □φ sign
at the pin points as a target — the direct attack on
the deciding fact above (t_kin same-sign as t_FB at the
worst point). A second, narrower observation for the
queue: at the best candidate the median worsened while
the max and legality improved, so a future pose that
also prices the median would test whether the trade is
structural. Closure is not claimed for the EoM clause:
the obstruction is exhibited at a point, not shown to
be structural.

C12: pre-existing walls at β = 1.1; no transport claim;
a moved front is not a legal wall. float64 throughout.
INTERNAL only; nothing uploaded, nobody contacted.
