# CHECKPOINT 482 — THE FLOOR-CLUSTER FIT

Charge: ledger entry 1258 (475's named
successor (i), charged under Intake 3).
Verdict: **A MEMBER ON THE LEVELLED
BASE** (registration SS6, form 1) —
Arm A, rung F2; Arm B's F2 output is
the identical object. The parent
refers the member to the next gate on
landing; this phase makes no gate
claim and no referral.

THREE GOALS: (1) FTL drive — a second
DEFENDED member at the wide pose, on
475's levelled base, with the floor
cluster {7, 10, 11} cured and its set
residue (node 26, invariant) on its
face; (2) functional wormhole — no
contact; (3) subluminal record —
untouched. DESK: NO DATA CONTACT.

## Registration

`work/p482_registration.md` (SS0–SS7),
filed before any Phase 482 computation.
No amendments. The fit: 479's
DEC-constrained joint fit transplanted
to 475's incumbent as base (BOUGHT-
MAXJOINT + GN475 = [+0.02, -0.058, 0,
-0.008, 0, 0, 0, +0.05, -0.05, +0.02, 0,
0, 0, 0, 0]); family W482 = the W474
lineage's centred-window form centred
at nodes 7/10/11; rungs F0 = {B},
F1 = {B, C}, F2 = {A, B, C}; SEC + DEC
as node constraints at {7, 10, 11}
plus the scalar joint as a seventh;
basin nodes {8, 9, 10} (and tracked
5..13) read on every candidate;
judged on DEFENDED and the full
SET-244 SEC minimum throughout.

## Controls (SS3) — all PASS

- CTL-482-1: the incumbent reproduced
  at diff 0.0 on all DECIDING_FIELDS,
  worst-null (+1.3932463241497539
  x10^-9), adversary depth
  (+1.2321965550763508x10^-12) and
  per-node SEC (sampled + Type-I,
  nodes 5..13). Base six fixed by this
  read: SEC -5.368730613015569x10^-6 /
  -6.793448628664004x10^-6 /
  -6.433344854499148x10^-6, DEC
  +6.896066379048901x10^-5 /
  +2.4658984119428845x10^-5 /
  +1.783454002970248x10^-5 (nodes
  7/10/11); d6c(0) =
  +6.793448628664004x10^-6.
- CTL-482-2: the zero-lever degenerate
  case reproduces CTL-482-1 at diff
  0.0 (screen + node values).
- CTL-482-3: probe (+0.01 on W482B's
  centre knot) six-row max prediction
  error 3.2297215798321195x10^-7 <
  1.0x10^-6 — halving rule not fired;
  fits ran on the h = 2.5x10^-3
  Jacobian.
- SS4 diagnostic (F2, full box, seven
  constraints): FEASIBLE.

## Fits (SS4) — summary

F0/F1 (both arms, identical): capped
at d6c = +5.368730613015569x10^-6 —
node 7 lies outside those rungs'
window supports, so SEC7 is invariant
there and the LP levels SEC10/SEC11
exactly up to it, then stalls under
the registered acceptance rule. F2
(both arms, identical): round 1,
LP t = -1.7845395441136043x10^-5,
exact d6c = -1.7845348315432977x10^-5
(agreement 4.7x10^-11), early stop —
CLUSTER-FEASIBLE. Census: 10 exact
candidates, 2 cluster-feasible.

## The member (SS5 confirmation,
## Arm A F2)

Lever: three nonzero knots, one centre
knot per window — W482A[4] =
-0.0006256155864301123, W482B[4] =
-0.0010659530055582157, W482C[4] =
-0.0011990467393266006; pen
1.0558979218253084x10^-6.
Six node values (sampled = Type-I-
restricted; frame-invariant): SEC
+1.7857748749212834x10^-5 /
+1.7860144271433635x10^-5 /
+1.7845348315432977x10^-5; DEC
+6.902108374779023x10^-5 /
+2.4644814128023883x10^-5 /
+1.7845348315432977x10^-5 (7/10/11).
DEFENDED triple (the incumbent's own
values, reproduced exactly): joint
+2.8204691775758897x10^-9, worst-null
+1.3932463241497539x10^-9, adversary
+1.2321965550763508x10^-12.
Set residue, on the face: set SEC
-6.792039324408745x10^-6 at node 26
(r = 19.097560975609756, Type-I; set
Type-I SEC identical) — SS2's
pre-registered invariant ceiling;
improvement over the incumbent's set
level exactly +1.409304255259x10^-9.
Basin read on the member: SEC8
-2.313676x10^-6, SEC9 -4.647783x10^-6
(read, not constrained; both lifted),
DEC at 8/9/10 all positive.

## Disclosures

No amendments. One incident: the
first controls launch was killed by a
service restart before its first
checkpoint write (nothing banked,
nothing altered); controls re-run
detached to completion; fit and
confirmation runs detached, single
pass each. Spend: 94 checkpointed
exact reads + 6 confirmation objects,
all VM, Phase-166 pin, float64,
SET-244 / SAMPLER-M. 479's member and
481's composition untouched (no file
sharing; nothing imported from
phase479/ or phase481/).

## Files

`work/` — p482_registration.md,
p482_lib.py, p482_controls.py,
p482_fit.py, p482_confirm.py.
`results/` — p482_controls.json,
p482_reads.jsonl, p482_jacobians.json,
p482_fit.json, p482_confirmations.json,
p482_memo.md, run logs. No ledger
append, no successor launched, no
user contact — per the charge.
