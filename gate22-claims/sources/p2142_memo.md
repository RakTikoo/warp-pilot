# P214-2 — TWO-SIDED TRUE MODES (FU-P210-2) — MEMO

Item 2 of Phase 214, executed exactly as registered in
`phase214/REGISTRATION214.md` and the item registration
`phase214/work/p2142_registration.md` (written BEFORE any
deciding computation; no amendments). DIAGNOSTIC scale only
(mr0 = 2, xi = 1/6, h = 0.05, L = 12, omega_max = 30,
ell = 0..32). Production reads remain VOID; no production
cutoff was run; no repair package is created.

## Verdict (registered form 3)

**TWO-SIDED CONSTRUCTION FAILS ITS OWN CONTROL** — the K-3
successor fails at its pre-registered bar (relative agreement
≤ 0.10 on the UNRESCALED tunnelling throat amplitudes): the
even members of the lowest doublets agree at ell = 8
(rel 0.045–0.047) but miss by 0.31–0.32 at ell = 16,
0.70–0.71 at ell = 24 and 0.93–0.94 at ell = 32. Per the
registration, this failure is a verdict, not a tuning
opportunity: the construction was NOT adjusted after seeing
the comparison, and the E-A deciding read did NOT run.
The matching obstruction is priced below, with per-ell
numbers: the disagreement is an exponent deficit
ln(u_disc/u_two) = 0.048 / 0.383 / 1.236 / 2.756 at
ell = 8 / 16 / 24 / 32 (n = 0), and it is quantitatively
explained by the barrier decay rate of the CONTROL'S OWN
REFERENCE — the h = 0.05 tridiagonal discrete eigenvectors
decay through the barrier at the discrete rate kappa_d with
cosh(kappa_d h) = 1 + (kappa h)^2/2, slower than the
continuum kappa, so their throat values are inflated by
e^{+Delta} relative to any continuum mode, with Delta growing
roughly quadratically in ell. The two-sided construction
itself shows the opposite conditioning from Phase 210's
failure (no e^{+S/2} blow-up anywhere; K-3a at 2.06e-10), but
as registered the control compares against the discrete
eigenvectors, and against them it fails. That is the verdict
of record.

## Construction as run (item registration)

Even/odd parity sectors integrated OUTWARD from the throat
(the potential being even; REGISTRATION214's "OR" branch):
even u(0) = 1, u'(0) = 0; odd u(0) = 0, u'(0) = 1; Numerov,
substep S = 8, h_f = 0.00625, on the half-box [0, L], mirrored
to the full box. In each barrier crossing the integrated
branch is the one decaying toward the throat (the physical
branch grows in the direction of integration, so admixture
decays relatively). Parity per eigenvalue: symmetry score of
the discrete eigenvector for singlets; one even + one odd per
near-degenerate doublet (Phase 210 grouping tolerance).
Normalisation: the matched mode's box norm rescaled to the
C_n phase-averaged target norm N_tgt (phase-averaged norm of
the Phase 209/210 C_n convention, evanescent points zero, as
registered) — the registered normalisation Phase 210's named
next object prescribes.

## Controls

- **K-1 PASS.** By-value counts exactly 258 (ell = 0) and
  251 (ell = 16); headroom asserted at every ell.
- **K-2 PASS.** V0 D-channel renormalised increments
  reproduce the full-precision stored values
  -467.09590320096555, -18847.939076552324,
  -126566.65035008395, -426296.6708632074 at
  ell = 8/16/24/32 with relative error **0.0** at all four
  (bar was ~1e-15 relative), monotonically growing in
  magnitude over ell = 8..32.
- **K-3a PASS.** Parity integrator vs exact sinusoids on
  constant V_ref (ell = 0, m = 1..12; ell = 16, m = 1..8;
  tolerances L2 rel < 1e-3, throat abs < 1e-3, right-BC
  residual < 1e-3): max L2 relative error **2.06e-10**
  (Phase 210's one-sided integrator measured 4.10e-10; same
  class). The integrator is not the obstruction.
- **K-3 SUCCESSOR FAIL — the deciding control.** Unrescaled
  throat amplitudes under the registered normalisation,
  lowest doublets n = 0..3, degenerate members by eigenspace
  projection, bar ≤ 0.10 for every compared doublet:

| ell | n | parity | u_two(0) | u_disc(0) | ratio | rel | pass |
|---|---|---|---|---|---|---|---|
| 8  | 0 | even | +1.303e-10 | +1.367e-10 | 0.953 | 0.047 | yes |
| 8  | 1 | odd  | 0 | +8.9e-24 | — | ~1e-23 (vs peak) | yes |
| 8  | 2 | even | +1.323e-09 | +1.385e-09 | 0.955 | 0.045 | yes |
| 8  | 3 | odd  | 0 | +4.4e-23 | — | ~9e-23 (vs peak) | yes |
| 16 | 0 | even | +2.995e-20 | +4.391e-20 | 0.682 | 0.318 | **NO** |
| 16 | 1 | odd  | 0 | +1.6e-33 | — | ~3e-33 (vs peak) | yes |
| 16 | 2 | even | +6.912e-19 | +1.005e-18 | 0.688 | 0.312 | **NO** |
| 16 | 3 | odd  | 0 | +6.8e-33 | — | ~1e-32 (vs peak) | yes |
| 24 | 0 | even | +5.614e-30 | +1.932e-29 | 0.290 | 0.710 | **NO** |
| 24 | 1 | odd  | 0 | -3.2e-43 | — | ~7e-43 (vs peak) | yes |
| 24 | 2 | even | +2.311e-28 | +7.803e-28 | 0.296 | 0.704 | **NO** |
| 24 | 3 | odd  | 0 | +1.1e-42 | — | ~2e-42 (vs peak) | yes |
| 32 | 0 | even | +9.952e-40 | +1.567e-38 | 0.064 | 0.936 | **NO** |
| 32 | 1 | odd  | 0 | -2.3e-49 | — | ~5e-49 (vs peak) | yes |
| 32 | 2 | even | +6.372e-38 | +9.703e-37 | 0.066 | 0.934 | **NO** |
| 32 | 3 | odd  | 0 | +1.2e-47 | — | ~3e-47 (vs peak) | yes |

(Odd members: throat value identically zero on both sides by
parity, judged on the registered 0/0 completion against the
projected peak; they pass trivially and carry no deciding
weight. The even members carry the e^{-S/2} amplitudes and
fail from ell = 16 on.)

## Deciding read

**Not run.** The registered stop rule fires on a K-3-successor
failure. There is therefore no per-ell E-A increment table
for this item: reporting one would require either adjusting
the construction to pass its control (forbidden by the
registration) or running the diagnostic on a basis that
failed validation (forbidden by the controls-first rule).
Cumulative NEC_rho / NEC_phi in THA units at ell_max = 32:
not produced. Subtraction B's Phase 209 plateau
(+2.95e5 x THA cumulative) remains the separate open term it
was; this item neither touches nor discharges it.

## Mechanism / obstruction pricing

The failure is one-sided and systematic: u_two(0) is always
SMALLER than u_disc(0), by a factor e^{-Delta} with
Delta = ln(u_disc/u_two) growing from 0.048 (ell = 8) to
2.756 (ell = 32) at n = 0 (n = 2 tracks it: 0.046 / 0.374 /
1.219 / 2.724). Three candidate obstructions were priced:

1. **Integrator conditioning (Phase 210's disease): ABSENT.**
   The outward parity integration has the stable branch
   selection by construction, and K-3a passes at 2.06e-10.
   Nothing in the two-sided modes blows up: their throat
   values are e^{-S/2}-suppressed exactly as physics requires
   (S/2 = 21.06 / 43.21 / 65.65 / 88.24 at ell = 8/16/24/32
   for n = 0, recomputed by the checker).
2. **Normalisation transfer: EXONERATED.** The registered
   N_tgt factor is applied to both sides of the comparison
   and cancels in the ratio; the deficit is in the ratio
   itself, not in any scale factor.
3. **The reference's own barrier dispersion: THE OBSTRUCTION,
   priced.** The discrete box eigenvectors solve the
   h = 0.05 tridiagonal problem, whose constant-kappa barrier
   recurrence u_{j+1} = (2 + kappa^2 h^2) u_j - u_{j-1} has
   decay rate kappa_d defined by
   cosh(kappa_d h) = 1 + (kappa h)^2/2, i.e. kappa_d < kappa
   (at the throat at ell = 32, kappa h ≈ 1.63 and
   kappa_d/kappa ≈ 0.91). A mode normalised in the edge wells
   therefore reaches the throat larger, by
   e^{int (kappa - kappa_d) dl} over the barrier, than the
   continuum mode at the same eigenvalue. Integrating that
   rate difference over the barrier (checker-recomputed)
   predicts the deficit:

   | ell | S/2 | Delta_obs (n=0) | Delta_pred (dispersion) | pred/obs |
   |---|---|---|---|---|
   | 8  | 21.06 | 0.048 | 0.061 | 1.27 |
   | 16 | 43.21 | 0.383 | 0.432 | 1.13 |
   | 24 | 65.65 | 1.236 | 1.347 | 1.09 |
   | 32 | 88.24 | 2.756 | 2.951 | 1.07 |

   The prediction tracks the observation at every ell
   (within 7–27%, tightening with ell, the residual being
   the constant-kappa form of the rate formula applied to a
   varying kappa(l)). Delta grows ~quadratically in ell
   because both kappa ~ ell and the barrier action S/2 ~ ell.
   So the "matching obstruction" is not the two-sided
   matching at all: it is that at h = 0.05 the discrete
   reference's tunnelling throat amplitudes — the very
   quantity K-3's successor was written to validate against,
   because Phase 210's rescaling was blind to it — are
   themselves continuum-wrong by e^{Delta}, Delta > 0.10
   from ell ~ 12 on. A continuum-true basis and the discrete
   spectrum it must cancel against differ at the throat by
   exactly this dispersion factor; that mismatch, not
   branch selection, is what any successor registration has
   to price (e.g. a reference built at a finer h, or a
   control against continuum eigenvalues). No such change
   was made here: the bar was pre-registered and the failure
   stands as the verdict.

## Fences

Diagnostic scale only; stand-in scope — nothing here is a
statement about production cutoffs or the production field.
Production reads remain VOID. No repair is packaged (verdict
form 3). No ledger append, no launches, no edits outside
`phase214/`.

## Files

- Item registration (pre-run):
  `phase214/work/p2142_registration.md`
- Driver: `phase214/work/p2142_run.py`; checker:
  `phase214/work/p2142_check.py`
- Results (controls in full; per_ell empty by the stop rule):
  `phase214/results/p2142_results.json`
- Checker output: `phase214/results/p2142_verify.json`
  (**13/13 pass** — the checker verifies the failure: counts,
  K-2 at 0.0, K-3a, the K-3-successor failure pattern at the
  0.10 bar, verdict form 3, diagnostic not run, and the
  dispersion pricing)
- This memo: `phase214/results/p2142_memo.md`
- Repair package: NONE (verdict form 3)
