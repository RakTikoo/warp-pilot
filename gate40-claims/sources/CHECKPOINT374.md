# CHECKPOINT 374 — THE LONG DWELL

Status: COMPLETE. Charged at ledger entry 943.
Full record: results/p374_memo.md. Registration:
work/p374_registration.md (filed before any
computation; Phase 364 Amendments 1-2 adopted at
filing; no new amendments).

## Verdict

WORST-INSTANT LEVEL IMPROVES AGAIN (registration
SS7 sense; flagged for GATE REFERRAL — the
referral is the parent's act).

Best member: SNM_a0.15_T640_D0.750_m0.88, J = 128:
- joint L_worst = NEC_worst
  = -2.099385079591706e-4 at phi = pi
- margin over L_364 (-2.169047936502377e-4):
  +6.966286e-6 (>= tol 1.0e-6)
- margin over L_stat (-2.319453132752996e-4):
  +2.200681e-5 (wall moved 9.49% from stationary;
  364 had moved it 6.5%)
- DEC_worst = -1.9410812223900952e-4 at phi = pi:
  REGRESSES vs DEC_364 (-1.8546990569430298e-4)
  by -8.638217e-6; beats DEC_stat
  (-2.2336932044559818e-4) by +2.926120e-5.
  Stated on the memo's face.
- Best both-coordinates improver:
  SNM_a0.30_T640_D0.750_m0.88 (L +2.516e-6,
  DEC +1.583e-5 vs champion bars).
- 12 of 16 members are joint-level candidates;
  the 4 non-candidates are the a = 0.15 / m = 0.75
  members (all still above L_stat).
- ALL LEVELS REMAIN NEGATIVE. NO EC pass. The
  wall stands, moved to -2.099385x10^-4
  (worst-instant, dwelling pose, band-posed
  r in [10, 20] on the A2 lineage; Phase 356
  full-extent caveats travel).

## Integrity

- Controls ALL PASS on the VM (frame of record):
  CTL-2/CTL-T1/CTL-0/CTL-1 diffs 0.0; CTL-T3
  max |T| exactly 0.0; CTL-T2 rel 2.505e-6;
  CTL-W PASS on both new shapes. Laptop pool ran
  controls first, NOT admitted (CTL-0 NEC
  1.05e-6 / WEC 8.31e-6; CTL-1 max 8.31e-6) —
  the 344/348/349/364 pattern a fifth time.
- C1 at every audited instant (global min rho
  +8.638078e-5); zero floor-infeasible instants
  in scan, refinement, anchor audit, everywhere.
- C2 PASS at all 24 candidate worst instants;
  worst-null reproduces the SET NEC min exactly
  (23) or to +1.1e-19 (1).
- Acceptance: side (i) PASS (0.0); side (ii)
  FAIL (1.753e-6 > 1.0e-6). Registered
  consequence executed: anchor J = 128 audit
  added to the 16 refinement J = 128 audits —
  the entire scan stands re-audited at J = 128.
  Anchor J = 128 reproduces L_stat/DEC_stat
  exactly.

## Anatomy (one line each)

- Champion saturates the quasi-stationary bound:
  worst instant phi = pi is a bottom-dwell
  instant (mu = 1.1125, mu_dot = mu_ddot = 0);
  L_worst = L_stat(1.1125). Transit tax at the
  verdict instant: zero.
- Period lever nearly exhausted (T160 -> T320
  bought +3.160e-5; T320 -> T640 bought
  +1.753e-6 on the a = 0.30 line; champion's
  T320 -> T640 gain +7.906e-6 = its residual
  transit tax, fully recovered).
- Lift lever paid through the stationary
  profile: m 0.75 -> 0.875 at a = 0.15 worth
  +7.278e-5 (bottom mu 1.075 -> 1.1125); at
  a = 0.30 worth ~0 on the joint level (top
  binds), +1.583e-5 on DEC.
- DEC_worst = DEC_stat(bottom mu) for every
  member at every density; co-modulation nearly
  free (SNM-M twin gap 3.03e-7 at the champion).

## Process

- Four runtime restarts killed detached workers
  (scan once after 3/17 members; refinement
  three times, last two after 23 and 31 of 32
  audits); all resumed from checkpoint files,
  zero re-reads, nothing lost or duplicated.
- VM shared with other pilots (load ~5/4 cores);
  wall times only affected.
- No ledger append, no successor launch, no
  user contact (per charge).

## Files

- work/p374_registration.md
- work/p374_lib.py, p374_controls.py,
  p374_scan.py, p374_refine.py, p374_confirm.py,
  p374_anchor128.py
- results/p374_controls.json,
  p374_controls_laptop.json, p374_scan.json,
  p374_refine.json, p374_anchor128.json,
  p374_confirm.json (+ run logs)
- results/p374_memo.md (this phase's memo)
