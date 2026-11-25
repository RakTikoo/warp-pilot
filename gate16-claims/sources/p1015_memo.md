# P101-5 — FU-T2-1 + FU-T2-2 — MEMO (Phase 101, carried capacity item)

Registration: `phase101/CHECKPOINT101.md` §P101-5 (binding), under
Phase 94 §T2's registrations and verdict forms. float64 everywhere.
Canonical EoM form only (force ÷ P_X) wherever an EoM is read in
Part B. Margins alone never decide. INTERNAL only.

This memo's §1 and §2 are the NEW REGISTRATIONS for both parts,
written and timestamped (2026-11-23T06:34Z, file creation) BEFORE
any scoring (Part A) or computing (Part B) for this item. Results
are appended in §3/§4 only after the runs; no registration text is
altered after scoring.

---

## §1 — PART A (FU-T2-1) REGISTRATION: THE MAGNITUDE-BALANCE RESTATEMENT

**Restated principle (exact).** For a corpus row, let the deciding
quantity be the one its own phase record names (the T2 corpus rule,
unchanged), read at its deciding point, with T2's live-term floor
(a term below 10⁻⁶ of the largest deciding term counts as absent).
Partition the live deciding contributions into two groups by the
direction in which they push the deciding quantity relative to its
registered pass condition:

- **A** = total magnitude of the pass-pushing contributions,
- **B** = total magnitude of the fail-pushing contributions,

with the group definitions per deciding-quantity form, fixed here:

| form | rows | A (pass-pushing) | B (fail-pushing) |
|---|---|---|---|
| q-criterion (sampled-null NEC / Type-I) | 1, 3, 4, 5 | D = T₀₀ + Tₙ̂ₙ̂ in the minimising direction | 2\|T₀ₙ̂\| in that direction |
| DEC margin ρ − max\|pᵢ\| | 2 | ρ | deciding max\|pᵢ\| |
| NEC1 / traveller ρ + p_r | 10, 11 | ρ | \|p_r\| |
| throat closure F_r = supply − demand (EQUALITY) | 8 | supply 2πℓ_tot² | demand |
| prefactor K_tot = K_single − ξ₂ψ² > 0 | 9 | K_single | ξ₂ψ² |
| scalar-EoM relative residual | 6, 7 | live terms of one sign at the median point | live terms of the opposite sign |

**Balance functional (exact):** ℬ := A / B (with B = 0 read as
ℬ = +∞ and A = 0 read as ℬ = 0).

**The restated principle has two clauses:**
1. **Opposition is necessary, not sufficient:** a pass requires
   BOTH groups live and nonzero (A > 0 and B > 0 in the table's
   sense; for the q/DEC/NEC1/prefactor forms this is exactly
   opposite signs among the live deciding terms in the record's
   written form; for the EoM form, live terms of both signs).
2. **Magnitude balance decides, in ratio form:** for a
   STRICT-INEQUALITY deciding quantity, a pass requires
   **ℬ > 1** (strictly); for an EQUALITY deciding quantity
   (row 8's closure only), a pass requires **|ℬ − 1| ≤ 10⁻⁸**
   (tolerance stated here: the row's own record carries closure
   residuals ≤ 2.2×10⁻¹⁶ absolute on terms ~10⁻⁶, i.e. relative
   ~2×10⁻¹⁰; 10⁻⁸ sits above that and below every other row's
   deciding distance). Row 9 is a strict-inequality row: at its
   deciding point (the crossing, K_tot = 0) ℬ = 1 exactly, which
   FAILS the strict clause — equality is balance without the
   strict excess a prefactor needs.

**Prediction rule:** a row is predicted PASS iff clause 1 holds
AND clause 2's applicable inequality holds; predicted FAIL
otherwise (opposition absent, or balance on/over the wrong side).

**Honesty clause (registered with the principle, not added
later):** for a pure signed-sum deciding quantity, ℬ > 1 is
algebraically equivalent to the signed sum lying on the pass
side; the restatement's empirical content is therefore exactly
(i) the NECESSITY of opposition across all families in the
corpus (including the EoM rows, where it is not algebraic) and
(ii) the single ratio form ℬ covering the q, DEC, NEC1,
prefactor and closure quantities uniformly. The verdict strength
is capped accordingly: a corpus-supported heuristic at exactly
that strength, nothing more.

**PASS bar (Phase 94's form):** all 11 rows of
`phase94/results/t2_results.json` score clean — predicted outcome
= stored outcome on every row, no counterexample.
**KILL:** one counterexample row, stated exactly (predicted ≠
actual, with its ℬ and clause readings).

Corpus rows (numbering = t2_memo.md's table): 1 GR S-A β=0.10
pass; 2 GR D1 β=0.1025 pass; 3 GR S-B β=0.10 fail; 4 GR S-A
β=0.105 fail; 5 flux-first β=1.1 fail; 6 coupling front B β=1.1
joint best fail; 7 P79-1 arm-(b) counterweight fail; 8 P68-3
throat closure pass; 9 P87-1 K_tot crossing fail; 10 conformal
member pass; 11 braneworld traveller fail.

---

## §2 — PART B (FU-T2-2) REGISTRATION: THE SLAVED-PAIR / SINGLE-EoM SIGNED-SUM HINGE

**The defect being aimed at (T2(b) anatomy):** the doublet's
opposition sat BETWEEN two fields' equations and cancelled
nothing. The hinge puts a signed sum of two coupling
contributions inside ONE field's ONE equation.

**Action (posed here, before computing; published blocks only):**

  S = ∫ e [ −(1 − ξφ²)T/2 + (βc/2) V·∂φ + (β₂/2) φ² div V
            + P(X, φ) ] d⁴x,
  P(X, φ) = p₁X + p₂X² + (μ/2) φ²,   X = −½ g^μν ∂_μφ ∂_νφ.

Blocks: the −(ξφ²)T/2 nonminimal block and the V-coupling blocks
are the published P47-2/P52-2/P76-1 coupling-force blocks,
unchanged in form. P(X, φ) with P_φ ≠ 0 is P52-2's published
general datum space (its throat path carries P_φ explicitly);
`p761_lib` restricted to the P_φ = 0 slice — this pose restores
the μφ term, μ a free coupling. ONE scalar field φ, ONE profile
(the P76-1 wallwide family), on the Phase 79 bed at β = 1.1.
Metric form as in p761_lib: H(φ) = 1 − ξφ² + βc φ/2 − β₂ φ²/2;
total stress E_tot = H G_bed + (Hess H − g □H) + T_P [+ family-B
fluid], with T_P built from the FULL P above (P now includes
(μ/2)φ² in its value; P_X = p₁ + 2p₂X unchanged in form).

**The single EoM and its two coupling contributions.** The
canonical EoM (P59-3 form: coupling force DIVIDED by P_X) is

  □φ − (P_XX/P_X)(v^μ ∇_μ∇_ν φ v^ν) + [ F_A + F_B ] / P_X = 0,

  F_A(φ) = ½ H_,φ(φ) · R_bed,   H_,φ = −2ξφ + βc/2 − β₂φ
           (the H-sector coupling force: nonminimal + V blocks),
  F_B(φ) = −P_φ(φ) = −μ φ
           (the P-sector coupling force).

The signed sum F_A + F_B sits inside the one equation; that is
the hinge. (Sign of F_B from P52-2's own throat EoM,
D_eom·W = P_φ − coeff·n₀ − P_X L/2, i.e. the numerator carries
−P_φ alongside the H-force.)

**The Phase-79 null-locus trap — the named gate, with proof the
sum is NOT identically zero.** F_sum(φ, R) = ½(−2ξφ + βc/2 −
β₂φ)·R − μφ. On the front, R_bed and φ are independent pointwise
data (P79-1 (b3) record: subset points sharing one φ value carry
different R). F_sum ≡ 0 on any open set of (φ, R) data forces
the R-coefficient AND the R-free term to vanish separately:
βc/2 = 0, 2ξ + β₂ = 0, μ = 0 — a measure-zero coupling subspace
(the trap subspace). GATE, applied at every candidate read and
at the deciding candidate: compute max over the 56 subset points
of |F_A + F_B|; **the trap FIRES iff that max < 10⁻⁹** (the
record's absolute degeneracy floor) or the candidate's couplings
lie on the trap subspace (|βc|, |2ξ + β₂|, |μ| all < 10⁻¹²).
If the trap fires at the deciding candidate, the item is
reported KILLED BY THE TRAP, exactly, whatever the front reads.

**Front (Phase 79's non-degenerate front definition, β = 1.1):**
the 56 subset points of Wall(1.1). Canonical EoM terms per point:
t_kin^c = □φ, t_pxx^c = −(P_XX/P_X)·vhv, t_FA^c = F_A/P_X,
t_FB^c = F_B/P_X. Canonical denominator D_can = |t_kin^c| +
|t_pxx^c| + |t_FA^c| + |t_FB^c|. A point is NON-DEGENERATE iff
D_can ≥ 10⁻⁹; degenerate count stated for every read. Relative
residual = |t_kin^c + t_pxx^c + t_FA^c + t_FB^c| / (D_can +
10⁻¹²). Legality = subset legal fraction from margins on
T_required of the hinge E_tot (p761_lib paths), plus health
(H > 0, P_X > 0, 0 ≤ c_r² ≤ 1) as in p791_main's read.

**Parameter space:** z = (ξ, βc, β₂, pi0, shape, p₁, p₂, μ)
with the first seven in p791_main's LO7/HI7 bounds and
μ ∈ [−3, 3]; family A: no fluid (z as above); family B: the
P76-1 family-B fluid (w from the stored B β=1.1 joint best) with
ρ₀ ∈ [0, 0.05] as a ninth parameter. Optimisation: least-squares
in p791_main's joint residual form (canonical EoM residuals with
degenerate points zeroed, EC hinges ×50 against the GR-control
scales, health hinges ×50), starts seeded from the stored P76-1
A and B joint bests at μ ∈ {0, ±0.5, ±1.5}, the P79-1 arm-(b) B
joint best at μ ∈ {0, −1}, and random starts (seed stated in the
run script).

**Phase 79's reads at the same cells (the comparison, fixed):**
family B β=1.1: subset legal joint best 0.518, Frontier B
legality 0.679, Frontier A 0.000, non-degenerate EoM max =
median = 1.000 (P79-1 second path); arm-(b) joint best: subset
legal 0.643, EoM median 0.987. Family A β=1.1: Frontier A 0.000.

**PASS bar (registered):** any candidate, second-pathed, with
(i) legality: subset_legal ≥ 0.518 AND health_ok, AND
(ii) solution-grade improvement: canonical EoM MAX over
non-degenerate points ≤ 0.02 (the Frontier-A form — Phase 79's
is 0.000, so any such candidate is a strict improvement), with
the trap gate NOT firing at that candidate.
**KILL:** the trap fires at the deciding candidate, OR no
candidate meets the PASS bar (the front does not improve on
Phase 79's reads at the same cells in the registered sense);
partial movements (e.g. a median move at stated legality) are
reported as anatomy, not as a pass.

**Failure protocol (both parts):** any kill gets an anatomy and
at least one follow-up aimed at the mechanism, in §3/§4.

---

---

## §3 — PART A RESULTS (FU-T2-1)

Scored by `work/p1015_partA.py` (deciding terms re-read from the
stored source records; `results/p1015_partA.json`); independently
recomputed by `results/p1015_checker.py`.

| # | row | form | A | B | ℬ = A/B | predicted | actual |
|---|---|---|---|---|---|---|---|
| 1 | GR S-A β=0.10 | q | 4.579×10⁻⁵ | 4.425×10⁻⁵ | **1.034841** | pass | pass |
| 2 | GR D1 β=0.1025 | DEC | 2.732×10⁻⁵ | 2.660×10⁻⁵ | **1.026978** | pass | pass |
| 3 | GR S-B β=0.10 | q | 4.558×10⁻⁵ | 4.612×10⁻⁵ | **0.988089** | fail | fail |
| 4 | GR S-A β=0.105 | q | 4.547×10⁻⁵ | 4.644×10⁻⁵ | **0.979238** | fail | fail |
| 5 | flux-first β=1.1 | q | 1.831×10⁻⁶ | 2.942×10⁻⁴ | **0.006222** | fail | fail |
| 6 | coupling front B β=1.1 | EoM | — | — | — (clause 1 fails: only the force term is live, kinetic share 1.9×10⁻¹¹) | fail | fail |
| 7 | P79-1 arm-(b) | EoM | — | — | — (clause 1 fails: kinetic/force same sign at the median point) | fail | fail |
| 8 | P68-3 closure | equality | 1.195174×10⁻⁶ | 1.195174×10⁻⁶ | **0.99999999989** (\|ℬ−1\| = 1.06×10⁻¹⁰ ≤ 10⁻⁸) | pass | pass |
| 9 | P87-1 K_tot crossing | prefactor | = B at the crossing | = A | **1.0 exactly** (fails the strict clause) | fail | fail |
| 10 | conformal member | NEC1 | 0.301762 | 0.298121 | **1.012213** | pass | pass |
| 11 | braneworld traveller | NEC1 | 0.0198944 | 0.0397887 | **0.500000** | fail | fail |

**11/11 predicted = actual. No counterexample.**

### Verdict A (registered form)

**PASS — the corpus scores clean under the restated principle
(no counterexample in the registered set): a corpus-supported
heuristic at exactly that strength.** The strength is capped by
§1's registered honesty clause: opposition is necessary on all
11 rows (0 passes without it; the two failures without it fail
clause 1), and the single ratio ℬ separates every
failure-with-opposition row from every pass — rows 3/4 by 1–2%
on the wrong side, row 5 by the denominator collapse
(ℬ = 0.0062), row 9 by equality-without-excess (ℬ = 1 exactly,
strict clause), row 11 by a factor 2 (ℬ = 0.5). For pure
signed-sum quantities ℬ > 1 is the pass side restated as a
ratio; the heuristic's non-algebraic content is the necessity
clause and the uniformity of the ratio form across the q, DEC,
NEC1, prefactor and closure families.

**Follow-up (for the queue):** FU-T2-1a — score the restated
principle on any NEW deciding rows the programme produces
(out-of-corpus test; the corpus fit is now exact, so only new
rows can strengthen or kill it).

---

## §4 — PART B RESULTS (FU-T2-2)

Runs: `work/p1015_partB.py` (first launch, max_nfev=150,
completed family B starts 0–7 before the 1700 s wrapper ended
it), `work/p1015_partB2.py` (max_nfev=60 launch; completed B
0–7 and A 0–3 before external termination — checkpointing
retained A 0–3 in full), `work/p1015_partB_finish.py` (re-ran
B starts 5–7 and A starts 4–5 with full stored reads; B starts
0–4 and A starts 0–3 carried as log-recovered summaries,
provenance flagged in `p1015_partB_raw.json`). The two
launches' deciding reads concur exactly on every shared start
(Frontier A 0.000, EoM max 1.0000, trap never fired). One
assembly defect was found and repaired on the record (the
finish run's checkpoint overwrite briefly mislabelled family-B
reads as family A in `runs_A`; repaired in the raw file with a
`repair_note` — no A run in any launch exceeded subset legality
0.0, so no deciding read was affected). Independent second
path: `p1015_checker.py` recomputes the deciding candidates
from raw jets with the FULL margins path (fast=False) —
legality and EoM max agree to <10⁻⁶ on both bests.

**Front reads (β = 1.1, 56 subset points; non-degenerate /
degenerate = 56 / 0 in EVERY read — the canonical denominator
never falls below the 10⁻⁹ floor, so no median is carried by
empty points):**

| read | subset legal | EoM (nondeg) max / median | Frontier A | trap gate: max\|F_A+F_B\| |
|---|---|---|---|---|
| direct: P76-1 B best, μ=0 | 0.518 | 1.0000 / 1.0000 | 0.000 | 3.31×10⁻² |
| direct: P76-1 A best, μ=0 | 0.000 | 1.0000 / 1.0000 | 0.000 | — |
| B starts 0–4 (log-recovered) | 0.518 / 0 / 0 / 0 / 0 | max 1.0000 all; median 0.9455–1.0000 | 0.000 | 3.19×10⁻² – 1.78 |
| **B best (arm-(b) seed, μ: −1 → −0.155)** | **0.589** | **1.0000 / 0.2244** | **0.000** | 5.67×10⁻² |
| B random start | 0.571 | 1.0000 / 0.1939 | 0.000 | 2.23×10⁻² |
| A starts (all) | 0.000 | max 1.0000 all; median 0.6690–1.0000 | 0.000 | 1.38×10⁻¹ – 1.73 |

**Trap gate:** never fires. At every candidate the signed sum
is genuinely present (max|F_A + F_B| ≥ 1.5×10⁻³ everywhere,
5.67×10⁻² at the best) and no candidate lands on the trap
subspace. At the B best the two contributions really do oppose
inside the one equation: median shares F_A 0.382 / F_B 0.489 of
the canonical denominator, sign(F_A) ≠ sign(F_B) at 84% of
points, median |F_A| = 4.27×10⁻², |F_B| = 5.25×10⁻².

### Verdict B (registered form)

**KILLED — the front does not improve on Phase 79's reads at
the same cells (the trap does not fire).** No candidate meets
the registered PASS bar: Frontier A = 0.000 in every read
(Phase 79's: 0.000); the non-degenerate EoM MAX is 1.0000 in
every read (Phase 79's: 1.000); no candidate is jointly legal
(≥ 0.518) + healthy + EoM-max ≤ 0.02 — in fact NO run in either
family is health_ok (the B best fails health on a single
clause, c_r² max = 1.00085 > 1, with H_min = 0.385 > 0 and
P_X min = +1.222 > 0; most other runs fail on P_X < 0).

**Anatomy.** The hinge works as posed — opposition now sits
inside one equation, with both force contributions live and
oppositely signed at most points — and it moves the MEDIAN
hard (1.000 → 0.224 at legality 0.589, above the P76-1
joint-best 0.518 and approaching Frontier B's 0.679; the
random start reaches median 0.194 at legality 0.571). What it
does not move is the MAX: at the B best only 2 of 56 points
reach EoM ≤ 0.02 and at least one non-degenerate point in
every configuration sits at relative residual 1.0000 — a
point where the canonical sum is carried by a single term
with nothing cancelling it. The wall is no longer "the terms
add instead of opposing" (arm (b)) or "the opposition is in
the wrong equation" (the doublet): with opposition inside the
equation and magnitudes comparable (shares 0.38/0.49), the
residual still pins at isolated points where the profile's
kinetic term vanishes AND the two force contributions happen
to align or one vanishes — a pointwise, not median,
obstruction. Median-based fronts overstate this pose exactly
as they did Phase 79's locus; on the non-degenerate MAX read
the pin is intact.

**Follow-up (Failure Protocol, aimed at the mechanism):**
FU-T2-2a — a pointwise hinge: seed the optimiser with a
residual form that prices the MAX (or a high quantile) of the
canonical EoM over non-degenerate points rather than the
least-squares sum, at the B-best configuration found here
(legal 0.589, median 0.224, μ = −0.155), and read whether the
residual-1.0000 points are a finite identifiable set (their
(φ, R) values stated) whose obstruction is a stated algebraic
condition on (F_A + F_B, □φ) — if the max-pin points share one
algebraic signature, that signature is the next registration's
target; if they do not, the pin is a covering property of the
front and the signed-sum family closes on that evidence.

## C12 accounting

All configurations are pre-existing walls on stored beds — no
formation mechanism is computed and NO transport claim is made
or implied by either verdict.

## Deliverables

- `results/p1015_memo.md` (this file; §1/§2 registrations
  written before scoring/computing), `results/p1015_results.json`,
  `results/p1015_partA.json`, `results/p1015_partB_raw.json`,
  `results/p1015_partB_anatomy.json`,
  `results/p1015_checker.py` → **33/33 PASS**
  (`p1015_checker_output.json`).
- `work/p1015_partA.py`, `work/p1015_lib.py`,
  `work/p1015_partB.py`, `work/p1015_partB2.py`,
  `work/p1015_partB_finish.py`, `work/p1015_partB2.log`.
