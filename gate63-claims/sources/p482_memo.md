# Phase 482 memo — THE FLOOR-CLUSTER FIT
# (475's named successor (i))

**GOAL 1 (FTL drive):** A MEMBER ON THE
LEVELLED BASE under the charge's
registered form. 479's DEC-constrained
fit, transplanted to 475's incumbent,
cures the levelled bowl's floor cluster
{7, 10, 11} outright: the member object
passes DEFENDED (joint
+2.8204691775758897x10^-9, worst-null
+1.3932463241497539x10^-9, adversary
Type-I NEC depth +1.2321965550763508
x10^-12 — all three reproducing the
incumbent's values exactly) with SEC
and DEC both non-negative at cluster
nodes 7, 10, 11 (worst node value
+1.7845348315432977x10^-5). The member's
lever is three nonzero knots — one
centre knot per window, each at its own
cluster node's address, |x| <= 0.00120.
ON THE FACE, per the registration: the
object's set SEC minimum is
-6.792039324408745x10^-6 at node 26
(r = 19.097560975609756, Type-I) — the
invariant outer node SS2 pre-registered
as this family's ceiling, improved past
the incumbent's level
(-6.793448628664004x10^-6) by exactly
+1.409304255259x10^-9, the full headroom
SS2 computed before any fit ran. It is
quoted here as the set residue it is;
it was not this phase's target. The
parent refers the member to the next
gate on landing, with the residue in
plain view; this phase makes no gate
claim. **GOAL 2 (wormhole):** no
contact. **GOAL 3 (subluminal record):**
untouched.

**VERDICT: A MEMBER ON THE LEVELLED BASE
(registration SS6, form 1)** — Arm A,
rung F2 (the first member in the
registered application order; Arm B's
F2 output is the identical object —
SS3). No gate referral is made by this
phase.

DESK: NO DATA CONTACT.

## 1. Registration, controls, the
## probe

Registration `work/p482_registration.md`
(SS0–SS7) filed before any Phase 482
computation; no amendments. The family
is the W474 lineage's centred-window
form (9 knots, window +/-1.0, tapers
0.5/0.5) in three copies centred at
nodes 7 (W482A), 10 (W482B) and 11
(W482C) on 475's incumbent (BOUGHT-
MAXJOINT + GN475); rungs F0 = {B},
F1 = {B, C}, F2 = {A, B, C}; knot box
[-0.35, +0.35]. The constraint set is
479's discipline moved to the cluster:
SEC and DEC as node constraints at
7/10/11 (six constraints) plus the
scalar joint retained as a seventh.

Controls (SS3), all before any fit:

- **CTL-482-1 PASS at diff 0.0** — the
  incumbent re-read on this phase's
  path through 475's own lever builder
  reproduces the stored record on all
  DECIDING_FIELDS, its worst-null
  (+1.3932463241497539x10^-9) and its
  adversary depth (+1.2321965550763508
  x10^-12) reproduce at diff 0.0, and
  the per-node SEC minima (sampled and
  Type-I-restricted) at nodes 5..13
  reproduce at diff 0.0. The read fixes
  the base's six, the phase's first
  record of the incumbent's DEC nodes:
  SEC -5.368730613015569x10^-6 /
  -6.793448628664004x10^-6 /
  -6.433344854499148x10^-6; DEC
  +6.896066379048901x10^-5 /
  +2.4658984119428845x10^-5 /
  +1.783454002970248x10^-5 (nodes
  7/10/11) — d6c(0) =
  +6.793448628664004x10^-6, SEC at node
  10 binding, as SS2 anticipated.
- **CTL-482-2 PASS at diff 0.0** — the
  zero-lever degenerate case through
  this phase's widened machinery
  reproduces CTL-482-1's read exactly
  (screen and node values): the fit's
  base point IS the incumbent.
- **CTL-482-3 (linearity)** — the
  registered probe (+0.01 on W482B's
  centre knot) is predicted by the
  base-point Jacobian with six-row max
  error 3.2297215798321195x10^-7, inside
  the registered 1.0x10^-6 tolerance:
  the halving rule did not fire and all
  fits ran on the h = 2.5x10^-3
  Jacobian. SS3 shows the probe's
  accuracy was earned: the F2 LP's
  promise and its exact read agree to
  ~4.7x10^-11.

The SS4 infeasibility diagnostic at
the base (F2, full box, seven
constraints) is **FEASIBLE**, so form 2
(INFEASIBLE AT THE CLUSTER) was already
disfavoured before the fits ran; the
exact fits settle it (SS2).

## 2. The fits (SS4) — the ladder caps
## at the rung that cannot reach node 7,
## and the full ladder cures

| arm/rung | LP t (r1) | dx_max | exact d6c | outcome |
|---|---|---|---|---|
| A F0 | +5.368731x10^-6 | 0.000074 | +5.368731x10^-6 | capped |
| A F1 | +5.368731x10^-6 | 0.000062 | +5.368731x10^-6 | capped |
| A F2 | -1.784540x10^-5 | 0.001199 | -1.784535x10^-5 | CURED, early stop |
| B F0 | +5.368731x10^-6 | 0.000074 | +5.368731x10^-6 | capped (identical) |
| B F1 | +5.368731x10^-6 | 0.000062 | +5.368731x10^-6 | capped (identical) |
| B F2 | -1.784540x10^-5 | 0.001199 | -1.784535x10^-5 | CURED, early stop (identical) |

Three readings of this table:

1. **F0 AND F1 CAP AT NODE 7's LEVEL,
   BY GEOMETRY, NOT BY PRICE.** Node 7
   (r = 6.121951219512195) lies outside
   both rungs' window supports (F0:
   [7.170732, 9.170732]; F1 adds
   [7.853659, 9.853659]), so SEC7 is
   invariant in those rungs and d6c
   cannot fall below its incumbent
   value. The LP sees this exactly: it
   levels SEC10 and SEC11 up to SEC7's
   -5.368730613015569x10^-6 with whisper
   steps (|dx| <= 7.5x10^-5), promises
   t = +5.368731x10^-6 — the cap itself,
   stated honestly by the linear model
   — and round 2 returns dx ~ 0 /
   non-improving candidates that the
   registered acceptance rule refuses.
   The rung outputs are DEFENDED (SS3)
   and already carry the set SEC at
   node 26's level, but they are not
   cluster-feasible: SEC7 stands. The
   ladder transplanted from 474/479
   discriminates here because the
   cluster is wider than one window:
   in 479, F0's single window covered
   all three constraint nodes; here
   only F2's does.
2. **AT F2 THE CLUSTER CURES IN ONE
   ROUND, IN BOTH ARMS, AT A WHISPER.**
   With W482A in play the LP promises
   t = -1.7845395441136043x10^-5 and the
   exact read delivers d6c =
   -1.7845348315432977x10^-5 — agreement
   to 4.7x10^-11, 479's linear-regime
   signature. The early-stop rule fired
   (LP t <= 0, exact d6c <= 0). Census:
   10 exact candidates, 2
   cluster-feasible (the two arms' F2
   round-1 reads of the same object).
3. **THE TWO ARMS PRODUCE IDENTICAL
   OBJECTS AT EVERY RUNG.** The
   DEC-constrained optimum sits at
   |dx| <= 0.00120, far inside both
   trust regions (0.06 and 0.03), and
   Arm B's roughness price is inert at
   that step — 479's identity result
   reproduces on the levelled base:
   at the DEC-constrained optimum there
   is no violence to gentle, on either
   base this fit has been transplanted
   to.

**Why the cluster was curable here:**
carrying DEC at the nodes caps the
LP's achievable slack at DEC11's level
(~+1.78x10^-5 — and on the member
SEC11 and DEC11 coincide digit-for-
digit, the same binding point pricing
both channels at node 11), the
cheapest achieving step is one centre
knot per window at |x| ~ 0.001, and at
that step the linear model is exact
and DEC is never billed. The wall was
the constraint set, not the class —
479's mechanism, confirmed on a second
base and a second node set.

## 3. Confirmations (SS5) — the member

Fresh full reads with worst-null and
adversary instruments, per arm/rung
output. All six outputs are DEFENDED;
the two F2 outputs are identical in
every deciding field.

**THE MEMBER (SS6 form 1, first in the
registered order — Arm A, rung F2; the
full W482 family refitted under the
six constraints):**

- Lever (W482A / W482B / W482C knots;
  three nonzero entries, each its
  window's CENTRE knot — one tap at
  each cluster node's own address):
  A = [0, 0, 0, 0, -0.0006256155864301123,
  0, 0, 0, 0]; B = [0, 0, 0, 0,
  -0.0010659530055582157, 0, 0, 0, 0];
  C = [0, 0, 0, 0, -0.0011990467393266006,
  0, 0, 0, 0]. pen
  1.0558979218253084x10^-6 (the
  incumbent's own pen is 1.05572x10^-6;
  474's fitted objects carried
  1.61–5.65x10^-6 on their base).
- Six node values (sampled; the
  Type-I-restricted minima AGREE at
  all three nodes for both channels —
  the deciding values sit at Type-I
  points and are frame-invariant
  statistics): SEC +1.7857748749212834
  x10^-5 / +1.7860144271433635x10^-5 /
  +1.7845348315432977x10^-5; DEC
  +6.902108374779023x10^-5 /
  +2.4644814128023883x10^-5 /
  +1.7845348315432977x10^-5 (nodes
  7/10/11). DEC7 actually rose slightly
  (+6.896066x10^-5 -> +6.902108x10^-5);
  the cure's whole DEC cost is DEC10's
  -1.4x10^-8 and DEC11's +1.1x10^-9 of
  movement — the slack was spent
  nowhere.
- DEFENDED triple: joint
  +2.8204691775758897x10^-9 (the
  incumbent's own value; dec_min
  identical), worst-null
  +1.3932463241497539x10^-9, adversary
  Type-I NEC depth +1.2321965550763508
  x10^-12. All three reproduce the
  incumbent's values exactly, as does
  nec_min (+4.68795873140689x10^-9).
- Basin read, as charged (nodes 8, 9,
  10 on the member): SEC -2.313676
  x10^-6 / -4.647783x10^-6 /
  +1.786014x10^-5; DEC +4.844569x10^-5
  / +3.446010x10^-5 / +2.464481x10^-5 —
  every basin DEC positive; nodes 8
  and 9 lifted slightly, not cured
  (they were read, not constrained, in
  this phase). Node 6 (inside W482A's
  left taper): SEC -5.927807x10^-6,
  the member's worst tracked node, also
  lifted. Node 12: -2.899449x10^-6.
  Node 13 (outside every support):
  -4.049726x10^-6, invariant.
- **SET RESIDUE, QUOTED ON THE FACE
  (SS5): set sec_min =
  -6.792039324408745x10^-6 at node 26
  (r = 19.097560975609756, Type-I; the
  set Type-I SEC is identical)** — the
  invariant outer node SS2 named
  before any fit ran, bit-identical on
  the incumbent, on all six rung
  outputs, and on this object; with
  the cluster cured it is the set
  argmin, at the family's pre-computed
  ceiling. The improvement over the
  incumbent's set level is exactly
  SS2's headroom, +1.409304255259
  x10^-9. The phase's fence holds:
  node 26 was quoted, never targeted.
  This phase makes no gate claim; the
  Gate referral, if the parent makes
  it, is made with this residue in
  plain view.

## 4. The two members, side by side
## (the record's position, stated
## plainly)

479's member (on BOUGHT-MAXJOINT)
cures {8, 9, 10} and carries its
residue at node index 23
(-6.459908493210403x10^-6, Gate-62's
rider numbering). This phase's member
(on the levelled base) cures
{7, 10, 11} and carries its residue at
node 26 (-6.792039324408745x10^-6).
The cured sets are complementary:
on this member, nodes 8 and 9 remain
slightly negative (-2.313676x10^-6,
-4.647783x10^-6); on 479's member the
cluster nodes 7 and 11 were never
constrained. Neither object is a
four-condition pass, and neither
phase claims one: each is a DEFENDED
member of its base with one named
node set cured and its set residue on
its face. What the pair establishes
together: the DEC-constrained fit
cures every node set it has been
aimed at, on both bases, at whisper
steps, with the LP exact — the
remaining distance at the wide pose
is now a list of named nodes and two
named invariant residues, not a
mechanism in doubt.

## 5. Follow-ups named (none launched
## by this phase)

- THE UNION FIT: one DEC-constrained
  fit carrying SEC + DEC node
  constraints at the union set
  {7, 8, 9, 10, 11} on the levelled
  base (node 6 read; it is the
  member's worst tracked node at
  -5.927807x10^-6 and sits inside
  W482A's taper) — the composition of
  479's and this phase's cures in a
  single object, posed as one joint
  fit on this phase's evidence, not a
  sequential composition.
- The two residues (node 23 on 479's
  base, node 26 here) are both outer,
  both invariant under the inner
  families, and both already named in
  their phases' records (481's charge
  addresses the node-23 locus on 479's
  base); nothing in this phase touches
  either.

## 6. Discipline, spend, disclosures

Registration filed before computation;
**no amendments**. Exactly the SS4
fits were judged; no near-miss was
re-optimised; no lever outside SS1
was tried; GN475, GN450, the scalings
and mu_S were carried unchanged in
every object. 479's member and 481's
composition were untouched — this
phase's computation read only 475's
stored confirmation and the lineage
libraries, and imported nothing from
phase479/ or phase481/. Spend: 94
checkpointed exact SET-244 reads
(2 controls, 27 base FD columns, 1
probe, 54 re-linearisation FD columns,
10 candidates) in
results/p482_reads.jsonl, plus 6
confirmation objects (each: full read
+ worst-null + adversary polish) in
results/p482_confirmations.json.
Disclosed incident: the first launch
of the controls script was killed by
a service restart before its first
checkpoint write — no read was banked
and no state was altered; the controls
were re-run detached and completed in
a single pass (all control values in
SS1 are from the completed run), and
the fit and confirmation runs were
likewise detached and each completed
in a single pass. The two arms'
identity of output is a measured
result (SS2), not a code path shared
in error — the arms ran separate LPs
with separate objectives and trust
bounds, and their candidate x vectors
agree because the optimum is interior
to both. All reads VM, Phase-166 pin,
float64, SET-244 / SAMPLER-M
(eulerian_that association, 449-lib
forms). Deciding SEC and DEC values
at nodes 7, 10, 11 sit at Type-I
points (sampled = Type-I-restricted
on the member) and are quoted as
frame-invariant statistics. No pool,
no Kaggle, no ledger append, no
successor launch, no user contact.
