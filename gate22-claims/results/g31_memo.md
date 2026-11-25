# GATE-31 — RUN MEMO (worker)

Registration: `gate31/work/g31_registration.md` (read in
full before any computation; it governed throughout).
Frame: Phase 166 pin, Gate-19-corrected tensor, venv
python (numpy 2.5.5 / scipy 1.18.1), float64. Writes only
under `gate31/`. No ledger append, no launches, no
external contact. Nothing was tuned against any read.

## Verdict form that fires (registration §4)

**SURVIVES** — decision-order step (iv): CERT-1…4 all
hold for both binding clauses (NEC_φ, DEC_φ). Whether the
claim stands INTACT or IN RESTATED WORDING is reserved to
the gate under §5 (the worker issues no GATE31.md and no
wording ruling). No failing condition / instant / clause
exists to name.

Per the §1 character fence: this is a **grid-stability**
certificate. Worst over the window (both binding clauses,
identical values): |d34| = 1.291×10⁻⁷, |d45| = 1.466×10⁻⁸,
r = 1.878×10⁻⁹, all against the 1×10⁻⁶ bar. No p value is
worded as a measured convergence rate or assurance.

## Decision order as executed (§4)

1. **Controls first, before any certificate evaluation.**
   - CTRL-1 (stored-read reproduction): PASS — 44 stored
     rows (41 sampled + 3 refinement) recomputed from
     `phase288/work/p288_member_state.npz` via
     `read_arm_A`; max abs diff 0.0 on clause minima AND
     0.0 on mom_resid_max.
   - CTRL-2 (fresh G4 march reproduction): PASS —
     MU/U/MTT [::40] vs stored member state, max abs
     diff 0.0 / 0.0 / 0.0.
   - CTRL-4 (protected md5): PASS — identical before /
     after (p1692 1781b544…, p167 9db35c0b…, p1621
     1f12ec29…).
   - CTRL-3 (G5 admission, evaluated once all three
     grids' t = 0.5 rows existed): PASS — NEC_φ and DEC_φ
     both |d34| = 1.154×10⁻⁷ ≤ 1e-6, |d45| = 1.311×10⁻⁸
     ≤ 1e-6.
2. **G5 cost probe (§3(e)), before the G5 march:** G5
   over [0, 0.05] (160 steps) wall 9.77 s → projection
   ×20 = 195.4 s ≤ 900 s. Rule did NOT fire; G5 ran.
3. **Window reads:** G3 (5761, 0.00125), G4 (11521,
   0.000625), G5 (23041, 0.0003125), every march to
   T_END = 1.0; all seven clause minima + mom_resid_max
   at all 10 window instants, reads at march index
   round(t/h_t).
4. **CERT evaluation (§1/§3(c)):** CERT-1 PASS,
   CERT-2 PASS, CERT-3 PASS, CERT-4 PASS (see below).

## Bracket numbers (both binding clauses identical)

| t | v5 | L | case | d34 | d45 | r |
|---|---|---|---|---|---|---|
| 0.575 | +0.06131127835593286 | +0.06131127835593286 | degenerate | +4.44×10⁻¹⁵ | −2.66×10⁻¹⁵ | 4.44×10⁻¹⁵ |
| 0.58125 | −0.00355073847104181 | −0.00355073847104181 | degenerate | +2.22×10⁻¹⁵ | 0.0 | 2.22×10⁻¹⁵ |

(Degenerate case per §1 verbatim: d34·d45 ≤ 0, so
L := v5, r := max(|d34|, |d45|). The three grids agree
at these instants to ~1e-15.)

## Non-clause bars at G5, bracket instants (§1 CERT-4)

| t | mom_worst (bar ≤1e-10) | flare_min (>0) | domain_R_min (>0) | domain_exp2Phi_min (>0) |
|---|---|---|---|---|
| 0.575 | 3.61×10⁻¹⁶ | 0.083083 | 0.649070 | 0.00190145 |
| 0.58125 | 3.61×10⁻¹⁶ | 0.082390 | 0.645771 | 0.00190145 |

All pass. CERT-4's clause side also holds: every
non-binding clause's G5 minimum > 0 at every window
instant t ≤ 0.58125. The domain_exp2Phi bar used the
registered jpose substitution
J_derived + exp(−2Φ₀)·mtt_a.

## Span record (§3(d), record only)

24 stored sampled instants, t ∈ [0, 0.575]; per-clause
minima cross-checked against CTRL-1's recomputation at
max abs diff 0.0 (pass). Minima: NEC_rho 0.669257 @
0.575; NEC_th 1.724058 @ 0.0; NEC_ph 0.061311 @ 0.575;
WEC 1.790154 @ 0.0; DEC_rho 0.669257 @ 0.575; DEC_th
1.724058 @ 0.0; DEC_ph 0.061311 @ 0.575.

## Walls (s)

Controls stage 83.7 (incl. CTRL-2's G4 march and the
probe); G3 march 20.0; G4 march 76.1; G5 march 424.7
(stage 425.4); evaluation 0.17; checker ≈ 41.

## Incidents (on the face of the memo)

1. **Driver defects caught before any number existed:**
   the first controls launch failed on a syntax error
   (`pass` used as a dict keyword) and, after that fix,
   on an import-order error (p1621_engine imported before
   p288_lib set sys.path). Both were fixed in
   `g31_run.py` before any stage produced output; no read
   was affected.
2. **First G5 stage attempt lost to a service restart:**
   launched ~17:26 PT in the foreground; the exec service
   restarted mid-march, killing the process. It produced
   no stage file and no numbers (log empty). This was
   not an OOM-kill (no OOM record; the process died with
   the service). The stage was re-run **unchanged**
   (identical settings and code path), detached, and
   completed: march 424.7 s.
3. **G5 actual wall exceeded the probe projection:**
   projected 195.4 s, actual march 424.7 s, under heavy
   shared-CPU contention from other work on the VM. The
   §3(e) rule is defined on the projection (195.4 ≤ 900),
   so the G5 run stood as authorised; the discrepancy is
   recorded here, not hidden.

## Independent checker

`gate31/work/g31_check.py` → `gate31/results/
g31_verify.json`: **ALL PASS** — Richardson table
recomputed from the stored per-grid rows at max abs diff
0.0 vs the results file; CERT booleans and CTRL-3 match;
bracket instants' G4 reads spot-recomputed from the
stored member npz at max abs diff 0.0 (m = 920, 930);
verdict-form consistency under §4 confirmed; protected
md5 identity confirmed.

## Deliverables

- `gate31/work/g31_run.py` (staged driver)
- `gate31/work/g31_results.json` (controls, probe,
  per-grid window rows, non-clause bars, span record,
  Richardson table, CERT booleans, walls)
- `gate31/work/g31_check.py` → `gate31/results/g31_verify.json`
- This memo: `gate31/results/g31_memo.md`
- Stage fragments + logs under `gate31/work/`
  (`g31_stage_*.json`, `g31_*.log`)
