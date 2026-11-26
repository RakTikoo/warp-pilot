# CHECKPOINT 361 — THE LOCALISATION: WHERE THE WRONG NUMBER LIVES

**Charged:** ledger entry 910. **Subject:** Décanini & Folacci, CQG 24 (2007)
4777–4799, arXiv:0706.0691v3 (DF). **Work:** `phase361/work/`.
**Machine-readable results:** `phase361/results/p361_results.json`.

## Verdict: NEITHER

The +16 bracket throat residual is carried neither by print H(6,3)(3)
(Arm A: carried amount a = (0, 0, 0)) nor by DF's (3.14)→(3.15) expansion
(Arm B: carried amount b = 0). The single-carrier assumption behind the
charge falls. The residual itself and the all-derived assembly stand
untouched (Gate-37's core closures, coefficient 203 → 187); what falls is
only the search for the wrong number inside DF's printed §2 tensors and
DF's expansion of them. Where it can still live is scoped in §6 — not run.

## 1. Controls (all passed before any new evaluation was quoted)

- **CTL-1.** Phase 355's own machinery re-run (`phase355/work/step3/
  test_ellis.py`): print H{2,0}(3) = derived = (80, 16, 112) at the Ellis
  throat, Δ = (0,0,0,0). ✓
- **CTL-2.** REST arithmetic reproduced exactly: REST_print − REST_derived
  = (0, 8/105, 0) (bracket (0, 16, 0)); 203 − 16 = 187; A-throat
  REST_derived = (−23/5040, −13/5040, −31/5040); engine E[tr Ric³]
  divergence exactly 0 at the throat. ✓
- **VAL-0** (ruler certification for the new monomial library). The
  library (`work/p361_eval.py`, all 42 non-g + 17 g monomials of DF's
  (2.1)/(2.2) basis as exact-Fraction einsums) reproduces Phase 355's
  validated print evaluator **exactly** on generic jet seed 404 (every
  component) and at the Ellis throat (80, 16, 112, 112). One defect was
  found and fixed en route: per-monomial diagnosis showed 22 of 23 shared
  monomials matching raw; N23 (R^{pq}_{;r}R_{pq b}{}^{;r}{}_{a}-slot)
  matched 355's T11 only after its (a,b)-symmetrisation — the
  symmetrised reading was adopted, per the registered rule that shared
  monomials take 355's fit-validated operationalisation. ✓
- **VAL-1** (pipeline QA). Exact fit of −E[R³] on Part A generic jets
  11/23/37 (+ fresh jet 47) recovers printed Eq. (2.24)'s coefficients
  exactly (N3 +6, N16 +6, N27 −3), unique solution, residual exactly 0 —
  the derived-side pipeline (engine + extended-pack fields + library +
  exact fit) reproduces an independent print tensor end-to-end. ✓

## 2. Transcription (registered protocol, filed before computation)

DF Eqs. (2.22), (2.24)–(2.31) and (3.15) independently double-transcribed:
A from the arXiv LaTeX source; B from the ar5iv HTML, corroborated against
the arXiv PDF text layer for every equation (B never used the LaTeX
source). **Term-by-term agreement on all 197 terms** (reconciliation:
0 diffs on all ten equations). Resolved transcription:
`work/df_resolved_transcription.json` (A/B files and reconciliation in
`work/transA/`, `work/transB/`, `work/reconciliation.json`).

Observation (both renderings, and reproduced by Arm B's recomputation):
printed (3.15) contains **no N20 term** — a genuine feature of the printed
equation, not a legibility gap.

## 3. Arm A — print H(6,3)(3) vs derived

**Registered prediction:** at the Ellis throat, print reads (32, −1, 44)
where derived reads (32, 8, 44).

**Throat read (direct evaluation, VAL-0-certified library, 355's SSS
machinery):** print (2.26) = **(32, 8, 44)**. Δ = (0, 0, 0).
**The prediction is refuted.** (Per-term record: `work/armA_throat_out.json`.)

**Tensor level (generic jets):** ΔH(6,3)(3) = print − derived vanishes
identically on six generic jets (11, 23, 37, 47, 71, 101): a joint exact
fit of Δ onto {N27..N33} + {S2..S17} returns the zero solution
consistently over 60 equations, and direct componentwise confrontation
on jet 101 gives Δ = 0 in all 16 components. The derived side is doubly
anchored: Phase 318's independent pattern form of H(6,3)(3) equals the
engine's −E_at0('TR3') exactly on fresh jets 101/202.

**Disclosed fit artefact (methodology note).** A first coefficient fit
with per-jet g-sector nuisance scalars appeared to load a cubic-sector
combination with coefficient 6132/473. Direct evaluation shows that
combination, C = −N27 + (5/2)N28 + (3/2)N29 − 3N30 + N31 − N32 + 2N33,
is **identically a pure g-sector tensor in four dimensions** (C = φ·g;
φ = −130 on jet 11, 291/8 on jet 101, 0 at the Ellis throat) — a basis
identity of the (6,3) algebraic sector. The fit had a 1-parameter
blindness along C (C trading against the per-jet g-scalars); direct Δ
evaluation is the arbiter and gives zero. Fits of this sector with
per-jet g-nuisances should not be quoted without a direct-evaluation
check.

**Arm A carried amount: a = (0, 0, 0)** — at the throat, and Δ = 0 as a
tensor, so at every point.

## 4. Arm B — the (3.14)→(3.15) expansion audit

Every (3.15) coefficient was recomputed from (3.14)'s weights applied to
the resolved print §2 forms of all ten tensors ((2.23) from Phase 355's
resolved record), in exact rational ξ-polynomial arithmetic, all 59 basis
monomials, ξ⁰..ξ³. **Result: printed (3.15) is reproduced exactly —
0 coefficient differences. The expansion is faithful.**

Control: the programme's stored MONO/TMONO transcription of (3.15)
(Phase 241 driver; the source of Phase 259's printed totals) agrees with
the fresh resolved print (3.15) on all 58 entries, coefficient by
coefficient. No programme-side transcription error.

**Arm B carried amount: b = 0** (Δ(3.15) ≡ 0).

**Propagation:** not triggered — no defect localised in (3.15), so the
Belokogne & Folacci 2014 / Taylor & Breen 2021 propagation does not
arise. Consumer statement, for the record: BF's published values do not
move on account of anything in the tested chain — (3.15) is a faithful
expansion and the §2 tensors it expands agree with the derived tensors
at every point tested. The Taylor & Breen posability question does not
arise.

## 5. What is now excluded (cumulative)

- H{2,0}(3) print = derived (Phase 355; re-confirmed here, CTL-1/VAL-0).
- H(6,3)(3) print = derived — throat and generic jets (this phase).
- H(6,3)(4) print = derived at the throat (Phase 318, direct evaluation
  of printed (2.27)).
- DF's (3.14)→(3.15) expansion: faithful, term by term (this phase).
- The programme's (3.15) transcription: identical to fresh print
  (this phase).

## 6. Scoped re-examination (NOT run, per the charge)

With every DF-side candidate excluded by direct exact computation, the
+16 can only live in the assembly record between DF's printed tensors
and the residual's statement. Three bounded reads, in order:

- **R1 — the Stage-4 back-out algebra (Phase 259) that produced
  REST_print.** Re-derive the ξ⁰ aggregate A0 and the netting of the
  print H(6,3)(6), (7), (8) throat evaluations (now available from the
  resolved transcriptions of (2.29), (2.30), (2.31)) out of it, auditing
  every "known-sector" subtraction — H{2,0}(1) at ξ⁰ weight 1/56,
  H(6,3)(1) at +1/216, H(6,3)(2) at −1/180, H(6,3)(5) at +1/180 — and
  which side's values (print or derived) each subtraction used. The
  H(6,3)(5) ξ⁰ subtraction is the one place the Phase 241 sector touches
  REST's bookkeeping; re-deriving the back-out's arithmetic does not
  disturb Phase 241's indictment, which concerns the full assembly's
  core arbitration and stays distinct.
- **R2 — the harness's throat evaluation of (3.15)** (eval_df on the SSS
  jet; the programme-side monomial functions of the Phase 241 driver).
  Transcription is cleared by this phase; evaluation is a separate
  artefact and is not cleared.
- **R3 — the target side of the original differencing:** the THA target
  values of the Phase 237/241 lineage against which the +16 residual
  was measured.

## 7. Fences

Nothing posted anywhere. The published v1.27.0 wording is not altered by
this phase (Gate-38 follows separately, on this verdict). Phase 241's
H(6,3)(5),(6),(8) indictment kept distinct and unused — the printed
forms of (2.28)–(2.31) were transcribed as data for the expansion audit
only. No ledger append; no successor launched.

**DESK:** literature and exact computation only; no observational data;
nothing for the Publishing Desk.
