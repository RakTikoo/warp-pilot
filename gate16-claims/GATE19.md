# GATE-19 — the fluid_T transposition defect: fix, corpus re-audit, and re-judgement of every gate-judged claim that consumed it

**Ordered:** by the parent, on Phase 166's stop-rule flag
(phase166/CHECKPOINT166.md §P166-4). **Execution form:** all reads
are SHORT local re-derivations on this VM in the frame of record
(venv: python 3.12.3 / numpy 2.5.5 / scipy 1.18.1) with the
Phase 166 pin live. Nothing heavy was needed; no Kaggle package
was required. **Basis files:** `gate19/work/g19_repro.py` (this
gate's independent reproduction, pre/post), `gate19/work/g16c/`
(Gate-16's own auditor + driver, copied, output redirected to
`gate19/results/g19_g16_results.json`), `gate19/work/g18c/`
(Gate-18's own evaluator, copied, output redirected to
`gate19/results/g19_g18_results.json`), `gate19/work/g19_audit.py`
(iteration-0 + Gate-17B legality re-reads). The ledger was NOT
edited — the parent records these verdicts.

## VERDICTS AT A GLANCE

| claim / record | verdict under the corrected tensor |
|---|---|
| **G16-1** (Gate-16) | **SURVIVES IN RESTATED WORDING** — legality 0.75 → 0.8928571428571429 (hinge → P128-1 best, both margin forms); still Pareto-dominates on both registered clauses |
| **G16-2** (Gate-16) | **FAILS** as a joint improvement — legality coordinate reverses against the corrected hinge (0.6071428571428571 < 0.75); EoM coordinates + coverage law stand as anatomy |
| **G13-1** (Gate-13, payload row) | **UNAFFECTED** — deciding reads never consumed fluid_T (evidence §5) |
| **Gate-12 reads** (G12-1/G12-2) | **UNAFFECTED** — same evidence |
| **Gate-17B verdict** (P124-1 FAILS) | **STANDS** — deciding path consumes no fluid_T; its legality table is restated (worse) |
| **Gate-17C verdict** (FAILS) | **STANDS** — companion clause outcome unchanged under corrected reads; legality direction unchanged |
| **Gate-18 ruling** (companion does not join) | **SURVIVES IN RESTATED WORDING** — operative §4(a)/§4(b) unchanged; its quoted numbers restated (§6) |
| Phase 158's Gate-16 confirmation | EoM side stands; legality standing is this gate's (G16-2 falls) |

## 1. The defect, independently reproduced (before any fix)

`phase76/p761_lib.py:fluid_T` built the Eulerian tetrad matrix
`Em`, inverted it (`A = Einv`), and formed
`Tcov = einsum('pma,pab,pnb', Einv, That, Einv)` = **A·That·Aᵀ**.
The tetrad identity is That = Eᵀ·Tcov·E (E^mu_a columns), so
Tcov = **Aᵀ·That·A**. This gate's own reproduction
(`g19_repro.py`, mode `pre`; results
`gate19/results/g19_repro_pre.json`):

- **Synthetic ADM metric** (rotated γ = R·diag(2, 1, 0.5)·Rᵀ,
  β ≠ 0, w = 0.37): coded output misses the basis-free tensor
  (ρ+p)·n⊗n + p·g by **0.7369**; the Aᵀ·That·A form matches it
  to **3.3×10⁻¹⁶**; the coded output equals the explicit
  A·That·Aᵀ form to 1.1×10⁻¹⁶ (the coded line is exactly the
  transposed congruence, nothing else).
- **Degenerate-plane rotation** (γ with an exactly degenerate
  eigenvalue pair; eigenvector basis rotated 0.9 rad inside the
  degenerate plane): the coded form's output moves by
  **0.1398** — it is not a well-defined function of the geometry;
  the Aᵀ·That·A form moves by **1.1×10⁻¹⁶**.
- **Stored P128-2 bed** (subset points, fluid (1.0, ρ₀)): coded
  vs basis-free max diff **0.1144** (Phase 166: 0.114 — concur).

Phase 166's three proofs are confirmed in full, with independent
code and a different synthetic metric.

## 2. The fix at source

`fluid_T` now forms `einsum('pam,pab,pbn->pmn', Einv, That, Einv)`
= Aᵀ·That·A, with a dated Gate-19 note in the source recording
the defect, the proofs, and this gate as the re-audit of record.
Post-fix regression (`g19_repro.py`, mode `post`): synthetic
max diff vs basis-free **3.3×10⁻¹⁶**; P128-2 bed **5.6×10⁻¹⁷**.
The fix changes no other function; `Wall.E_total`'s non-fluid
components are untouched.

**Which stored reads are bit-unchanged by the fix** (verified
explicitly, both forms computed side by side):

- Any read with **fluid = None**, and any point where the fluid
  term vanishes (**ρ₀ = 0**, or ρ(r) = 0 — the window_w support
  is r ∈ [10, 20], so all points outside it): both forms return
  exactly 0. Bit-identical (verified: ρ₀ = 0 case, array-equal).
- **Zero shift with γ diagonal whose eigenvalues stand in
  eigh's ascending order along the coordinates** (V a signed
  identity, A diagonal): bit-identical (verified, max diff 0.0).
- **NOT unchanged:** a diagonal γ whose eigenvalue order is
  permuted against the coordinates — eigh sorts ascending, so
  the tetrad axes are permuted, and the old form assigns each
  coordinate direction the *wrong* eigenvalue's pressure
  (verified: γ = diag(1.2, 0.9, 2.0), old spatial diag
  p·(0.9, 1.2, 2.0) vs correct p·(1.2, 0.9, 2.0); max diff
  0.015 at ρ = 0.05). The tasking's phrase "axis-aligned
  eigenbasis" is therefore narrowed on the record: alignment
  alone does not protect a read; the eigenvalue *ordering*
  must also match.
- **All canonical/grouped/split EoM reads are bit-unchanged**
  as a class: `canonical_terms` (p1015_lib and every copy) never
  calls fluid_T. Verified in the Gate-16 re-run below (every
  EoM number bit-identical, machinery-gate worst error
  8.549×10⁻¹² as stored). Health clauses (H, P_X, cr2), the
  trap, and alignment/targeting reads likewise never consume
  fluid_T.

## 3. Corpus map — what consumes fluid_T

Every E_total assembly in the live tree adds fluid_T when a
fluid is posed: `p761_lib.Wall.E_total`, `p1015_lib.hinge_E_total`
and its descendants/copies (p1125, p1194, p1241/p1242 E_total_ext,
p1251, p126, p128 libs, p1351, p1401 via hinge, p1461, p1504,
p1541, p1611/p1612, p1641–p1643, gate copies in gate16/work_a,
gate17/work, gate17c/work, gate18/work). The reads that consume
it are exactly: **legality fractions from margins(E_total)**,
**R_E** (the E_tot − H·G residual norm), and **the conservation
companion** (divergence of T_required = E_total/8π). Frozen
copies inside publication bundles and Kaggle bundles
(gate17-claims/, phase157/kaggle/bundle/, phase165/kaggle/bundle/,
phase142/kaggle/libs/) carry the defective line but are records,
not machinery; they are not edited.

## 4. Deciding re-reads (old → corrected, clause outcomes)

### 4.1 Gate-16's deciding set (Gate-16's own machinery, copied)

Machinery gate: PASS, worst corpus error 8.54938342342848e-12
(as stored); hinge alignment set {44} as stored.

| read | hinge best | P128-1 best | P128-2 best | P128-2 targeted |
|---|---|---|---|---|
| subset_legal fast, stored | 0.5892857142857143 | 0.9285714285714286 | 0.7857142857142857 | 0.5357142857142857 |
| subset_legal full, stored | 0.5892857142857143 | 0.9464285714285714 | 0.7857142857142857 | 0.5357142857142857 |
| **subset_legal corrected (fast = full)** | **0.75** | **0.8928571428571429** | **0.6071428571428571** | **0.42857142857142855** |
| EoM max / median, health, worst point | bit-identical | bit-identical | bit-identical | bit-identical |

(Full corrected record: `gate19/results/g19_g16_results.json`.)

**G16-1 re-judged.** Against the corrected hinge (0.75):
Δlegal = +0.1428571428571429, ΔEoM max = −1.87846×10⁻⁵
(strictly below; unchanged). Both registered Pareto clauses —
stated against the hinge best — hold against the hinge best as
it actually is. **SURVIVES IN RESTATED WORDING:** "subset
legality 0.75 → 0.8928571428571429 (both margin forms), worst-
point EoM residual 0.9999999999784565 → 0.999981215379503,
median worsened 0.22437629566157347 → 0.47963896879690177,
health fails on cr2, alignment set empty, Frontier A = 0" —
Gate-16 §7's wording with exactly those numbers replaced; all
fences unchanged.

**G16-2 re-judged.** Against the corrected hinge (0.75):
Δlegal = **−0.1428571428571429** (a worsening), ΔEoM max =
−1.93744×10⁻³, Δmedian = −0.0794151 (both unchanged). The
registered claim is Pareto dominance on (subset_legal,
eom_rel_max) under either clause; with the legality coordinate
reversed, neither clause is met against the true hinge best.
The registration itself classifies single-coordinate movements
as "anatomy, not milestones". **FAILS** as a joint improvement.
What stands, as anatomy (canonical path, bit-identical): the
EoM max and median moves, the targeted candidate's opposition
at 50/51/52, the worst point's migration to 44, and the
coverage law. A note on the literal thresholds: Phase 128's
clauses were registered against the defective hinge constant
0.5892857142857143, against which the corrected P128-2 legal
(0.6071) would nominally pass clause (i). This gate judges the
claim's substance — dominance over the hinge best — per the
Gate-17B definitional standard: a threshold manufactured by
the same defective instrument that produced the candidate's
number is not a bar. The hinge's corrected value is the bar.

**Phase 158's confirmation** of Gate-16 was an EoM-side audit;
it stands for G16-1 (restated) and falls with G16-2. A pointer
note is appended to CHECKPOINT158.

### 4.2 Gate-17B's legality table (its own read path)

Read path verified first: with the old form reinstated the
path reproduces Gate-17B's stored table exactly (subset
0.5535714285714286, 31/56). Corrected (full margins):

| set | stored | corrected |
|---|---|---|
| subset (56) | 0.5535714285714286 | **0.05357142857142857** (3/56) |
| binding (504) | 0.4523809523809524 | **0.021825396825396824** (11/504) |
| volume (300) | 0.3567 | **0.25** (75/300) |

At this z the fluid term carries most of the stored legality
(fluid = None reads subset 0.0). Gate-17B's **verdict stands**:
its deciding term is the grouped EoM (canonical, unaffected),
and the corrected legality is strictly worse. Gate-17C's
**verdict stands**: its companion clause re-reads (via Gate-18's
evaluator, §4.4) at median 0.0770 / max 0.1901 vs the 0.02 bar —
still failing; its re-discretisation legality direction is
unchanged (the corrected subset is already 0.0536).

### 4.3 P161-2 iteration-0 record + the P164-3 C1 targets

(p1612_proto's full_eval path, unchanged, under the fixed lib.)

| set | legal stored → corrected | R_E stored → corrected |
|---|---|---|
| subset | 0.7857142857142857 → **0.6071428571428571** | 7.064234364523864 → **6.539621079037025** |
| binding | 0.7678571428571429 → **0.5714285714285714** | 7.146033331363234 → **6.653647141308457** |
| volume | 0.42333333333333334 → **0.32666666666666666** | 9.13873039750334 → **8.914461395352056** |

(Consistency: the corrected subset legality equals §4.1's
P128-2 best read, 0.6071428571428571, as it must — same z, same
set.) P161-2's verdict (NO UPDATE RULE EXISTS) is unaffected.
**C1 disposition:** C1's targets are re-based to the corrected
R_E values above. C1's rebuild side (Phase 166's re-run:
subset 7.0468 / binding 7.2439 / volume 9.1834) was computed
with the defective tensor and is **not** re-judged here; the
named follow-up is an unchanged re-run of
`phase164/work/p1643_solver.py` under the fixed library,
after which C1's clauses (grouped within 1e-6 relative —
canonical, unaffected; R_E within 1% — against the re-based
targets) can be re-judged. Phase 166's attribution (residual
C1 failure = rebuild-path fidelity) was measured against
defective-tensor R_E on both sides and must be re-measured,
not carried.

### 4.4 Gate-18's deciding companion reads (its own evaluator, copied)

All 12 recorded reads disagree with their stored values
(AGREE 0/12 — expected: the evaluator's agreement flags test
the defective-tensor numbers). Corrected deciding values:

| read | median stored → corrected | max stored → corrected |
|---|---|---|
| P128 G16-2 deciding | 0.2666388711339408 → **0.0796322760631874** | 0.8627845254790542 → **0.3045242444648436** |
| P128 G16-2 control | 0.2608249793749235 → **0.0953627952627903** | 1.339819227527566 → **0.2582058362169998** |
| P140 moved 1 deciding | 0.3357550427384781 → **0.0867976142729086** | 1.4529605418741998 → **0.1900186069208907** |
| P140 moved 2 deciding | 0.3382603850300888 → **0.0834382745893021** | 1.446767443114848 → **0.1880696653488728** |
| P89 arm (a) deciding | 0.3493287018563901 → **0.0813573859597069** | 1.4313646012468235 → **0.2716104244801319** |
| P89 V2 deciding | 0.5325325283058377 → **0.0544779828459139** | 1.26134252326992 → **0.1972772343022574** |
| T1 (P124-1) deciding | 0.359824646064951 → **0.0770043862997114** | 1.3791062082656986 → **0.1901133475279939** |
| T1 control (a = 0) | 0.3598252198297751 → **0.0770041027115605** | 1.3791006786722664 → **0.1901134972105708** |

Every corrected read still fails the 0.02 bar on **median and
max** (closest: V2 median, 2.7× the bar; T1 h-scan at h = 0.6:
0.1107 — the failure is not a stencil artefact in either
direction). The defective tensor was *inflating* the companion
~4×: most of what Gate-18 measured as the prescribed bed's
inconsistency was the instrument's own spurious term.

**Gate-18 re-judged.** Its ruling's deciding ground was
definitional (on a prescribed bed the companion measures the
construction, and a candidate moves it by ≲0.018 while it sits
0.34 from its bar) plus empirical (the ~0.35 band; the extremes
invert). Under the corrected tensor: the band is 0.054–0.095;
controls land within 0.0002–0.016 of their deciding reads; no
candidate meets or approaches the bar on either form; the
extremes-invert observation does **not** survive (the corrected
lowest median in the β = 1.1 hinge line is T1's 0.0770, and the
set no longer ranks the worst-EoM configuration first — that
sentence of Gate-18's evidence is withdrawn). The operative
ruling — §4(a) the companion does not join the front joint
conditions; §4(b) the step-2 conservation condition on solved
metrics — rests on the definitional ground, which the
corrected numbers do not touch (the corrected floor, ~0.08, is
the bed's genuine prescription inconsistency, exactly as the
ruling described the quantity). **SURVIVES IN RESTATED
WORDING:** Gate-18's ruling stands verbatim in §4; its §2/§3
quoted medians, the ~0.35 band, and the inversion sentence are
superseded by the table above.

### 4.5 Phase-level deciding reads re-read

- **Phase 140's moved pair:** subset legality (fast = full)
  0.5892857142857143 → **0.6428571428571429**, both candidates.
  Clause outcome unchanged (≥ 0.518 bar); the phase's deciding
  claim (grouped worst point 0.6813357021143944 / 0.6815) is
  canonical and stands. Subset illegal-point count for the
  pair: 23 → **20**.
- **Phase 76 family-B joint best (β = 1.1):** subset_legal
  0.5178571428571429 → **0.42857142857142855** (single-config
  re-read on its own Wall.E_total path).
- **Phase 146 / Phase 150 (P150-4):** both consumed the Phase
  140 pair's margins through hinge_E_total. Their subset-level
  content is corrected by §4.5's count (23 → 20 illegal). Their
  set-level deciding anatomies (Phase 146's DEC bands on
  binding/volume sets; P150-4's full-margins tail reads at the
  named sentinel points) were **not** re-read in this gate —
  named follow-up: re-run `phase146/work/p1461_search.py`'s
  read path and `phase150/work/p1504_read.py` under the fixed
  library and restate their margin anatomies; neither phase's
  headline verdict is a gate claim, and P150-4's question
  (sentinel vs genuine tail) must be re-answered, not assumed
  in either direction.

## 5. Gate-judged claims that did NOT consume fluid_T (evidence)

- **Gate-13 (G13-1, the 0.09758c payload row):** its verifier
  (`gate13/wa_*.py`) is the fresh symbolic radial-reduction /
  shell path over Phase 116's composed profiles (build_shell
  machinery, verify_metric margins). A grep of gate13's code
  for `p761`, `fluid_T`, `hinge_E_total` returns no hits; the
  deciding reads are shell-sector margins of a prescribed
  composed profile, a different instrument entirely. Phase
  116's own code is likewise free of the defective path.
  **UNAFFECTED.**
- **Gate-12 (G12-1 Le pin; G12-2 endowed-shell spectrum):**
  `gate12/g12_*.py` — Le multipole reads and a surface-action
  spectrum; no p761_lib import, no fluid_T, no hinge machinery
  (the word "fluid" in GATE12.md is the Brown–Gladush *surface*
  perfect-fluid action of the endowed shell, a different
  object). **UNAFFECTED.**
- **Gate-17 (P124-1, SURVIVES INTACT at the time):** its EoM
  deciding path was canonical (unaffected); its legality
  coordinate is restated by §4.2. The claim was already
  superseded by Gate-17B's FAILS, which stands.

## 6. Affected-but-not-re-read (enumerated, superseded as a class)

Every other stored legality / R_E / companion number computed
from E_total **with a fluid posed** encodes the defective
tensor and is superseded as a class, including: Phase 76's
search-level reads (both β), Phase 79's and Phase 89's stored
legality reads, Phase 101 Part B legality, Phase 103, 105,
109 (assembled model's 0.4286), 112, 118, 119, 120, 124's
search reads, 125, 126B, 130, 132 (auditxi 0.506 cell), 135,
137, 142's reads, 154's ridge reads, 161's D3 inputs (re-read
at gate level in §4.4), 164's unintegrated diagnostics, and
the Kaggle-bundle copies of the same. Search-level re-runs are
not local-short; each line's numbers re-enter only through a
re-run under the fixed library when that line next moves, and
no verdict in this gate relies on them. Phase-level verdicts
whose deciding coordinate was one of these numbers (notably
Phase 109's and Phase 132's legality-side statements) carry
the same supersession; their EoM-side statements are
unaffected.

## 7. Restatements executed (append-only, prefix-verified)

Dated Gate-19 notes appended — stored numbers never rewritten
— to: `gate16/GATE16.md`, `phase128/CHECKPOINT128.md`,
`gate17b/GATE17B.md`, `gate18/GATE18.md`,
`phase161/CHECKPOINT161.md`, `phase140/CHECKPOINT140.md`,
`phase124/CHECKPOINT124.md`, `phase76/CHECKPOINT76.md`, and a
pointer note on `phase158/CHECKPOINT158.md`. Each append was
verified byte-prefix-exact against the pre-append content
(md5s in this gate's run record). The library fix itself
carries a dated note at `phase76/p761_lib.py:fluid_T`.

## 8. Standing consequences

1. The corrected hinge best for the β = 1.1 front is subset
   legality **0.75**; every future Pareto threshold on this
   front registers against corrected baselines.
2. In-kernel Kaggle controls that compare against stored
   fluid-consuming reads (Phase 166's caution) now compare
   against Gate-19's corrected values where §4 supplies them;
   all other stored fluid-consuming values are void as control
   targets.
3. The P164-3 C1 follow-up (§4.3) is sequenced with the
   fluid_T disposition as Phase 166 directed — the disposition
   is this gate; the solver re-run is the remaining act.
4. No FTL-relevant standing improves: Frontier A = 0
   everywhere in the re-audit; G16-2's fall removes one of the
   front's two gate-verified improvements, and P124-1's
   corrected legality (0.0536) deepens its fall. G16-1 remains
   a gate-verified improvement, in restated numbers.

**Uniqueness protocol:** nothing in this gate is worded
first/unique/record; the corrected numbers are stated as
re-reads of named configurations on named machinery.
