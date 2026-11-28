# CHECKPOINT 479 — THE DEC-CONSTRAINED FIT

Charge: ledger entry 1241 (474 follow-ups
(i) + (ii) charged together). Status:
COMPLETE. Verdict: **A MEMBER AT THE
WIDE POSE** (registration SS6 form 1) —
parent refers to Gate-61 on landing;
this phase made no gate claim and
launched no successor.

## Key objects

- MEMBER (Arm A, rung F0; all six
  arm x rung outputs are members under
  the form, identical across arms):
  BOUGHT-MAXJOINT base + W474B =
  [0, -0.0014031443466063713, 0, 0,
  -0.0013795539861294259, 0, 0,
  -0.002009452499039281, 0], W474A =
  W474C = 0, GN450 unchanged.
  DEFENDED: joint
  +2.820462654076372x10^-9, worst-null
  +1.149158092307544x10^-9, adversary
  +2.333817817820605x10^-13 (all = the
  base's values exactly).
  Six (nodes 8/9/10): SEC
  +2.440444x10^-5 / +2.441198x10^-5 /
  +2.439644x10^-5; DEC +4.894588x10^-5
  / +3.441161x10^-5 / +2.439644x10^-5
  (sampled = Type-I-restricted at all
  three nodes, both channels).
  pen 2.004145258222042x10^-7.
- SET RESIDUE on the member (quoted,
  never targeted): set sec_min
  -6.459908493210403x10^-6 at node 25
  (r = 17.04878048780488, Type-I) — the
  base's pre-existing outer locus,
  bit-identical to 474's F0/F1 objects.
  Set dec_min +2.820462654076372x10^-9
  @ 27.29268292682927.

## Controls

- CTL-479-1 PASS diff 0.0 (base,
  worst-null, adversary).
- CTL-479-2 PASS diff 0.0 (474's F1
  object reproduced; node-10 DEC
  -5.375277493220288x10^-4) +
  NON-VACUITY: the six-constraint set
  excludes that object (SECs >= 0,
  DEC10 < 0), demonstrated before any
  fit was believed.
- CTL-479-3: node-9 FD error
  +9.722155708100704x10^-5 (=
  CTL-474-3 digit-for-digit); halving
  rule fired; error stood at
  +9.722322246477557x10^-5 (sublinear
  at large steps). Fits ran on the
  halved-step Jacobian; the optimum
  (|dx| <= 0.00201) sits in the linear
  regime — LP t vs exact d6 agree to
  ~4.5x10^-11.
- SS4 diagnostic: seven-constraint
  linearised feasibility at the base
  FEASIBLE.

## Files

- work/p479_registration.md (SS0–SS7,
  filed before computation, no
  amendments)
- work/p479_lib.py, p479_controls.py,
  p479_fit.py, p479_confirm.py
- results/p479_controls.json,
  p479_jacobians.json, p479_fit.json,
  p479_confirmations.json (verdict +
  all six confirmations),
  p479_reads.jsonl (62 checkpointed
  exact reads), p479_memo.md,
  p479_fit_log.txt, p479_confirm_log.txt

## Named follow-up (not launched)

474's (iii): the outer locus at node
25 (-6.459908493210403x10^-6) — a lever
address there composed with the basin
cure in ONE joint fit, SEC+DEC carried
as node constraints at basin and outer
locus alike. The parent's to charge.

DESK: NO DATA CONTACT.
