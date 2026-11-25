# P207-1 — MEMO: P-DIR-T2 AND THE MARCH, RE-DECIDED (Phase 207 ITEM 1)

Worker item 1 of Phase 207, warp pilot. Execution of the march
registered in `phase203/work/p2034_registration.md` with the single
corrected prescription **P-DIR-T2** of
`phase207/REGISTRATION207.md` ITEM 1 (POSE (m = 1, κ = 0.3);
c_m^(T2)(θ,t) = [(m − cosθ) − (A_,θ/A)·sinθ]²/(sin²θ·A²), with
A = J['A'] and A_,θ = J['Ah'] at ρ = 0). Frame of record: Phase 166
pin, Gate-19-corrected tensor. Execution form: HOME-SHORT — the
full march (fine 2881/0.0025 + refinement 1441/0.005, 21 sampled
instants, both arms, plus the FD second path) ran locally in
49.2 s, inside the Phase 203 §(d) rule, so no first-window-only
run and no laptop/Kaggle package was needed. Exhibit ≠ construction
language preserved: a march of channel evaluations at posed jets
over sampled instants, at the pose's stated scope; P129-6's
combined-class scope (rotating + general R(ρ,θ,t) + time-dependent
Teo, ZAMO-frame diagonal reads, per-instant (G1)–(G4)) applies to
every claim. INTERNAL only. No ledger append, no launch, no
external contact.

## VERDICT (registered Phase 207 ITEM 1 form): DIRECTOR IS A t = 0 PATCH — PATCH WITH EXTENSION

**The sole failing bar is the refinement gate, and its carrier is
the baseline march itself, not the director.** Every throat bar
the director can touch is met on the whole interval [0, 0.5]: the
full throat EC set is ≥ −10⁻⁹ pointwise at every sampled instant
(worst clause minimum overall **+0.004542169502404825**), momentum
worst 3.608224830031759×10⁻¹⁶ ≤ 10⁻¹⁰, flare > 0 and domain
regularity at every instant, FD second path sign agreement at all
5 registered instants. Against the P169-1(f) baseline (first
NEC_φ failure **t = 0.400**, worst **−0.6297872673028908**), the
director arm's NEC_φ/DEC_φ **never fail**: first failing instant
— none on [0, 0.5]; worst NEC_φ = DEC_φ =
**+0.004542169502404825** at t = 0.5, a shift of the minimum of
+0.6343294368052956 against the control arm at the same instant.
That is an extension past the baseline's first failure and past
the end of the registered interval — hence the sub-form PATCH
WITH EXTENSION. The registered SUSTAINED form is nevertheless not
available, because the registered bar set includes the refinement
gate ≤ 10⁻⁶ and the director arm's gate reads max EC disagreement
**5.8263602620289845×10⁻⁶ at t = 0.5** — numerically the baseline
march's own gate value (P169-1(f): 5.82636026180694×10⁻⁶; the two
agree to 2.2×10⁻¹⁶, and control C1 reproduced the baseline gate
exactly). Per-clause at t = 0.5 the disagreement is carried by
NEC_ρ/DEC_ρ (5.826×10⁻⁶) — clauses whose director shift is
identically zero (ΔNEC_ρ ≡ 0, §2) — while NEC_φ's own disagreement
is 3.899×10⁻⁷, below the bar. The director profile c_m^(T2) is
analytic in (θ,t) and identical on both grids; it contributes
nothing to the gate disagreement. The p1592 gating clause is not
named on a sustained verdict's face because no sustained verdict
is rendered; it remains open exactly as before.

## 1. RUN RECORD — controls before numbers

**Byte identity (asserted before and after the run, md5):**
`phase129/work/p1296_derive_raw.json`, `CHAN_FNS`
(`phase150/work/p1501_families.py`), `lock_solve` / `march` /
`instant_jets` (`phase162/work/p1621_engine.py`),
`phase167/work/p167_engine.py`, `phase169/work/p1692_engine.py`,
`phase202/work/p2022_wound.py` — all byte-identical before/after
(md5 table in `results/p2071_results.json`; independently
re-verified by the checker). The entry route is read-level only:
the new module `work/p2071_engine.py` provides `c_m_dir_T2`,
`channels_with_director_T2` (shifts ONLY the four diagonal
channels: rho8 += (κ/2)c_m, prho8 −= (κ/2)c_m, pth8 −= (κ/2)c_m,
pph8 += (κ/2)c_m; mom_* and S unshifted), and
`instant_read_dir_T2` modelled line-for-line on
`p167_engine.instant_read_comp`.

**C-SYM under T2 (prescription check) — PASS.** The Phase 202 /
P205-1 SymPy machinery re-run with the t-dependent throat
geometry, checked against the CORRECTED profile, both m = 1 and
m = 2, clause by clause:

- ∇_ρ̂n = 0 and ∇_θ̂n = 0 at the throat: **PASS** (identically).
- Averaged stress diagonal, ⟨G_ρρ⟩ = ⟨G_θθ⟩ = 0, all averaged
  off-diagonals zero, no momentum-channel content: **PASS**.
- ⟨G_φφ⟩ = (∇n)²: **PASS**.
- (∇n)² = c_m^(T2)(θ,t): **PASS** as a symbolic identity AND as a
  grid identity — max |(∇n)² − c_m^(T2)| on the audit grid
  ≤ 1.5×10⁻¹¹ over t ∈ {0, 0.125, 0.25, 0.375, 0.5} (float
  residue class; this is the grid check the registration
  required, not a θ*-only or t = 0-only check).
- T2 reduces to Phase 202's c_m at t = 0: **PASS** exactly
  (max |c_T2 − c_T1| at t = 0 is 0.0; A_,θ(·,0) ≡ 0).

**C0 (t = 0 audit) — PASS.** Phase 202's own construction
(`instant_jets` with μ_,tt(θ,0) = ũ_true) read through the T2
channels (at t = 0, J['Ah'] ≡ 0, max abs 0.0, so T2 ≡ T1
verbatim). At (m = 1, κ = 0.3) the seven minima reproduce Phase
202's exact stored values with max abs diff **0.0** (NEC_ρ =
DEC_ρ = +0.431250, NEC_θ = DEC_θ = +0.596875, NEC_φ = DEC_φ =
+0.051181, WEC = +1.062523; S(θ*) = +0.431250; momentum residuals
0.0). At κ = 0 the datum's own minima reproduce with max abs diff
**0.0** and ũ_true(θ*) = 1.1412482021558361 exactly.

**C1 (κ = 0 control arm) — PASS.** The same march code with
κ = 0 reproduces P169-1(f) exactly: per-instant clause minima max
abs diff vs the stored F-rerun **0.0** over all 21 instants;
NEC_φ/DEC_φ first fail at **t = 0.400**; worst NEC_φ
**−0.6297872673028908** at t = 0.5; worst march mom
3.608224830031759×10⁻¹⁶; S(θ*(t)): +0.431250 → +1.058131;
refinement gate max EC disagreement 5.82636026180694×10⁻⁶-class
reproduced (abs diff vs stored ≤ 10⁻⁹; recomputed value in the
results JSON). This licenses pricing every director-arm movement
against the baseline.

**C2 (lock invariance) — PASS.** One march state (MU, U, MTT) was
computed once and consumed by both arms (field md5s in the
results JSON); θ*(t) director vs control max abs diff **0.0**;
momentum channels in the director arm equal the control arm's at
every sampled instant, max abs diff **0.0**. Also verified at
every instant: S(θ*(t)) agrees with the shifted NEC_ρ(θ*(t)) to
≤ 5.6×10⁻¹⁶ (ΔNEC_ρ ≡ 0 makes the two the same read).

## 2. The march (director arm, T2, (m, κ) = (1, 0.3))

Per-instant minima (full table in `results/p2071_results.json`):
NEC_φ = DEC_φ declines monotonically from +0.906710 at t = 0
(the march's compensated t = 0 slice; distinct from C0's
lock-carrying datum audit +0.051181, exactly the named Phase 169
distinction) to its worst **+0.004542169502404825 at t = 0.5** —
positive at every sampled instant. The other clauses' worst
minima over [0, 0.5]: NEC_ρ = DEC_ρ = +0.024846076305979237
(t = 0.5; the S-drift carrier — the director supplies it no
support, ΔNEC_ρ ≡ 0, and it holds on the uncontrolled march's S
trajectory exactly as FU-1's registered note anticipates),
NEC_θ = +1.0625750349885348 (t = 0), DEC_θ =
+0.9053756499513512 (t = 0.5), WEC = +1.0625218927247293
(t = 0.5). Pointwise shift structure verified per instant:
ΔNEC_ρ = ΔNEC_θ ≡ 0 (shift of minima exactly 0.0 at t = 0.5),
ΔNEC_φ = +κ·c_m^(T2) ≥ 0 before DEC saturation, ΔWEC =
+(κ/2)·c_m^(T2). Δτ(θ*) = 0.5525854590378236, identical to the
control arm (same θ*(t), C2). FD second path (einstein_fd,
metric alone, with the same additive T2 terms applied to its
four diagonal outputs before clauses): sign agreement on
S(θ*(t)) and every EC minimum at all 5 instants (0, 0.125, 0.25,
0.375, 0.5). Prototype off-diagonal worst 1.4048432902906356 —
the baseline march's own stored value, unchanged by the
read-level sector (a prototype read, not a registered bar).

**The one failing bar, priced.** Refinement gate (director fine
2881/0.0025 vs coarse 1441/0.005): max EC disagreement
5.8263602620289845×10⁻⁶ at t = 0.5 vs the registered bar 10⁻⁶.
Carrier, by per-clause decomposition at t = 0.5: NEC_ρ and DEC_ρ
carry the maximum (5.826×10⁻⁶ each) and the director's shift on
those clauses is identically zero; NEC_θ 1.043×10⁻⁶, DEC_θ
2.762×10⁻⁶, NEC_φ/DEC_φ 3.899×10⁻⁷, WEC 5.480×10⁻⁸. The κ = 0
control arm's gate on the same pair of grids is the same number
(C1), and P169-1(f)'s stored gate is the same number: the
disagreement is the march's own μ_,tt grid/FD disagreement at
t = 0.5, inherited unchanged by the director arm. Under the
registered bar set as written, that is a failed bar, and the
registered verdict forms leave exactly one form for a failed
bar — hence the verdict above, with this anatomy on its face:
**the EC sustainment the item was registered to decide held on
the full interval; what failed is a grid-agreement bar the
uncompensated baseline itself does not meet.**

## 3. What stands, and the follow-up the failure names

Standing: the corrected prescription is the posed director's
actual stress (C-SYM T2, grid identity); the t = 0 closure is
unchanged (C0, bitwise); the baseline is reproduced exactly
(C1); the lock is untouched (C2). The director at (1, 0.3) under
T2 removes the baseline's NEC_φ/DEC_φ failure outright on
[0, 0.5] — worst +0.004542 at the final instant, i.e. the margin
is thin and still declining at the interval's end (control-arm
drift −0.072 → −0.630 over [0.4, 0.5] against a director shift
that grows only through A(θ,t)'s shrinkage); nothing here reads
past t = 0.5.

**Follow-up experiment (Failure Protocol — aimed at the
mechanism):** the failing bar's mechanism is the march's
μ_,tt discretisation disagreement at t = 0.5 (5.83×10⁻⁶, carried
by NEC_ρ/DEC_ρ), present identically with κ = 0. The deciding
experiment is a grid study of the BASE march alone: a third grid
(5761, h_t = 0.00125) read of the κ = 0 arm at t = 0.5 — if the
fine-vs-third-grid NEC_ρ disagreement falls toward ≤ 10⁻⁶ with
the expected order, the gate failure is ordinary FD convergence
and a future registration can set the gate at the demonstrated
order (or require the third grid); if it does not fall, the
t = 0.5 μ_,tt field carries a non-convergent feature that must
be anatomised before any sustained form is claimed at any pose.
No such run is made here (outside this item's registration).

**Fences on this verdict's face:** sector superposition at the
channel-read level (the programme's W1/W7/W9 pattern) — a
director coupled back into the geometry is a different,
unregistered problem; P-DIR-T2 inherits P-DIR-T1's flagged gap
(i) (no ṅ terms, no director dynamics); the defect-core
divergence of the profile persists per-instant (c_m^(T2) range
at t = 0.5 reaches 1.5624×10⁴ at the grid's south end) and no
deciding read sat at a grid end (the binding clauses' argmins
are interior throughout — NEC_φ's argmin sits adjacent to θ*,
θ = 1.5536 at t = 0.5; only the non-binding NEC_θ/WEC minima,
at +1.06, sit at the north grid end, exactly as in the baseline
march's own reads). FU-1 and FU-2 are untouched: this pose prescribes no
spatial jet and consumes neither. The p1592 deciding scan
remains in the parent's launch queue; no programme-level
milestone form is claimed by this item at any scope.

## Files

- `work/p2071_engine.py` — the T2 read-level extension
  (`c_m_dir_T2`, `channels_with_director_T2`,
  `instant_read_dir_T2`).
- `work/p2071_run.py` — driver (C-SYM T2 → C0 → marches → C1 →
  C2 → FD second path → bars/verdict; byte identity asserted
  before/after).
- `work/p2071_check.py` — checker: recomputes every
  verdict-carrying number from the results files (C-SYM T2 grid
  identity re-derived from the stored symbolic expressions, C0
  vs Phase 202, C1 vs P169-1(f) stored march, C2 from stored
  channel arrays, director bars and refinement gate from stored
  per-instant reads, verdict consistency, protected-file byte
  identity). **ALL PASS, 45/45, TOTAL FAILURES 0** (re-run at
  delivery).
- `results/p2071_results.json` — C-SYM T2 per-m symbolic
  expressions, check flags and grid-identity table; C0/C1/C2
  full blocks; per-instant director/control fine and director
  coarse reads; FD second path; bar summary and the failing
  bar's anatomy; md5 before/after table.
- Full march executed home-short; no Kaggle/laptop package was
  required. No ledger append, no launch, no other file edited.
