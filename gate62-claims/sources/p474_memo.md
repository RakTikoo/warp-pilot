# Phase 474 memo — THE TWO-NODE LEVER (R449-2)

**GOAL 1 (FTL drive):** no drive, and no
member. The two-node idea works on its
own terms: a lever fitted jointly at
basin nodes 8, 9 and 10 cures all three
nodes' SEC at every rung of the freedom
ladder — already at F0, the one-node
family itself refitted jointly. But
every fitted object pays for the cure
in DEC at sister node 10, inside the
fit's own window (-2.10x10^-4 /
-5.38x10^-4 / -2.01x10^-3, growing with
fit freedom), so DEFENDED fails on its
joint clause on all three objects. The
wide pose's last condition is no longer
an intra-basin SEC trade; it is a
DEC-at-the-basin condition, and the
constraint set a successor fit must
carry is named in SS5. **GOAL 2
(wormhole):** no contact. **GOAL 3
(subluminal record):** untouched.

**VERDICT: THE TRADE IS THE CLASS'S
SHAPE (registration SS6, form 3).**
Every jointly-fitted form still bills
some node; the bill is mapped against
fit freedom in SS4. A MEMBER does not
arise (every object fails DEFENDED's
joint clause; F0/F1 also carry set
SEC < 0 at the outer locus, F2 at
node 11). THE JOINT FIT IS INFEASIBLE
does not arise (the SS4 diagnostic is
feasible, and exact three-node-feasible
candidates exist at all rungs).
Sub-form 2b does not arise (no object
carries set SEC >= 0). No gate
referral.

DESK: NO DATA CONTACT.

## 1. Registration, family, controls

Registration `work/p474_registration.md`
(SS0–SS7) filed before any Phase 474
computation; no amendments. The widened
family W474 is exactly three copies of
the lineage's registered centred-window
form (9 knots at centre + (-1.0, ...,
+1.0), window +/-1.0, tapers 0.5/0.5),
centred at node 8 (r = 6.8048780487804885,
W474A), node 9 (R_IN = 7.487804878048781,
W474B — geometrically identical to
W449S) and node 10 (r = 8.170731707317074,
W474C), summed through the lineage's
lever injection on 450's BOUGHT-MAXJOINT
base (SS1 of the registration; GN450,
scalings and mu_S carried unchanged).
Rungs: F0 = {B} (9 parameters),
F1 = {B, C} (18), F2 = {A, B, C} (27);
knot values bounded to [-0.35, +0.35].

Controls (SS3), all before any fit:

- **CTL-474-1 PASS at diff 0.0** —
  BOUGHT-MAXJOINT re-read on this
  phase's path reproduces the stored
  record on all deciding fields, and
  its worst-null (+1.149158092307544
  x10^-9) and adversary Type-I NEC
  depth (+2.333817817820605x10^-13)
  reproduce at diff 0.0. The base's
  basin, sampled node SEC: node 7
  -6.289504497329363x10^-7, node 8
  -6.818999180673762x10^-6, node 9
  -9.112743683512697x10^-6 (the set
  argmin, Type-I), node 10
  -8.419173524140114x10^-6, node 11
  -5.776656862728578x10^-6 (nodes 12,
  13: -1.547988x10^-6, -2.225566x10^-6,
  read on the F0 confirmation where
  they are outside every support and
  hence the base's own values). The
  "basin" is a shallow three-node dip
  (8, 9, 10), with nodes 7 and 11 also
  slightly negative.
- **CTL-474-2 PASS at diff 0.0** — the
  object with W474B = LEVER449 =
  [-0.028, 0, 0, +0.008, 0, 0, 0, 0,
  -0.028] and W474A = W474C = 0
  reproduces 460's composed object on
  all deciding fields, on the node
  SEC minima at nodes 7..11, and on
  the DEFENDED triple. This is the
  registered recovery: the widened
  family's machinery, with its other
  authorities zeroed, recovers the
  one-node lever's node-9 cure
  (+3.3264628436439144x10^-5) exactly.
- **CTL-474-3 (linearity)** — the
  base-point FD Jacobian predicts 460's
  composed node SECs at nodes 8 and 10
  at roundoff (errors -5.506x10^-9 and
  -8.899x10^-9) but at node 9 with
  error +9.722155708100704x10^-5,
  exceeding the node's exact lift
  (+4.237737x10^-5). The registered
  halving rule fired (h: 2.5x10^-3 ->
  1.25x10^-3; Jacobian rebuilt, 27
  further reads) and the node-9 error
  stood at +9.722322246477557x10^-5.
  The discrepancy is therefore NOT FD
  truncation: the site node's response
  is strongly sublinear in the lever
  (the linear model over-predicts
  LEVER449's site lift ~3.3x: predicted
  ~1.396x10^-4 vs exact +4.238x10^-5).
  Per the registration, the fits ran
  on the halved-step Jacobian, with
  sequential re-linearisation as the
  standing correction (in the event,
  no rung needed a second round — SS2).

## 2. The fit (SS4)

The SS4 infeasibility diagnostic at the
base (F2, full box, no trust region) is
**FEASIBLE**: the linearised three-node
constraint set is non-empty, so the
infeasible verdict form was already
disfavoured before the fits ran; the
exact fits settle it (below).

Each rung ran the registered sequential
LP fit from the base (trust region
|dx| <= 0.06 per round, L1-regularised
objective t + 1x10^-3 sum|dx|, joint
carried as a linear constraint) and
stopped after round 1 under the
registered early-stop rule: the LP
returned t <= 0 and the exact read
confirmed d <= 0 with the read
feasible. Exact node SECs (sampled;
the Type-I-restricted minima agree at
these nodes wherever the deciding
values sit, per the confirmation
profiles):

| rung | LP t | node 8 | node 9 | node 10 | d* |
|---|---|---|---|---|---|
| F0 | -1.640231x10^-3 | +5.788568x10^-5 | +3.761259x10^-5 | +1.259838x10^-5 | -1.259838x10^-5 |
| F1 | -2.277206x10^-3 | +6.267279x10^-5 | +2.674869x10^-5 | +2.391783x10^-5 | -2.391783x10^-5 |
| F2 | -5.178328x10^-3 | +4.540784x10^-5 | +7.048559x10^-7 | +1.530712x10^-5 | -7.048559x10^-7 |

Three readings of this table:

1. **THE INTRA-BASIN SEC TRADE IS
   CURABLE, AT EVERY RUNG.** The
   449/460 anatomy — cure node 9, bill
   nodes 10 and 8 — does not survive
   joint fitting. Already F0 (the
   one-node W449S family alone, its 9
   knots refitted against the three
   node constraints instead of against
   site delivery alone) cures all
   three nodes. The cure was in the
   FITTING, not in the widening: the
   extra windows of F1/F2 are not what
   closes the basin's SEC.
2. **The three-node slack is
   NON-MONOTONE in freedom** (d*:
   -1.260x10^-5, -2.392x10^-5,
   -7.049x10^-7). F1 holds the deepest
   slack; F2, with the most authority,
   holds the shallowest — its LP spent
   the trust region hardest (LP t
   -5.178x10^-3, the most optimistic
   promise) against the same saturating
   site response CTL-474-3 measured.
3. **The LP's promises are not the
   reads.** LP t overstates the exact
   slack by ~two orders of magnitude
   at every rung — the quantitative
   shadow of the node-9 sublinearity.
   All verdict weight rests on the
   exact reads, as registered.

The fitted levers are violent compared
to LEVER449: most active knots sit at
the +/-0.06 trust bound with alternating
signs; roughness penalty pen = 1.611x10^-6
(F0), 1.794x10^-6 (F1), 5.654x10^-6 (F2)
against the base's 2.000x10^-7 and 460's
composed 2.195x10^-7; correction
dN'' ranges [-4.012, +5.352] (F0),
[-4.120, +6.894] (F1), [-12.642, +15.577]
(F2). hard_zero_ok holds on every read
(the corrections vanish exactly outside
their supports).

## 3. Confirmations (SS5) — where the
## bill actually lands

Fresh full reads with worst-null and
adversary instruments, per rung output:

| rung | set SEC min (argmin) | joint (argmin) | worst-null | adversary | DEFENDED |
|---|---|---|---|---|---|
| F0 | -6.459908x10^-6 (node 25, r 17.0488, Type-I) | -2.101404x10^-4 (DEC, node 10) | +1.149158092x10^-9 | +2.333818x10^-13 | FALSE |
| F1 | -6.459908x10^-6 (node 25, Type-I) | -5.375277x10^-4 (DEC, node 10) | +1.149158092x10^-9 | +2.333818x10^-13 | FALSE |
| F2 | -4.365759x10^-4 (node 11, r 8.8537, Type-I) | -2.011276x10^-3 (DEC, node 10) | +1.149158092x10^-9 | +2.333818x10^-13 | FALSE |

- **Exactly one DEFENDED clause fails,
  the same one, on every object: the
  sampled joint — and it fails through
  DEC at node 10** (r = 8.170731707317074),
  the sister node inside the fit's own
  window. Worst-null and the adversary
  Type-I NEC depth reproduce the base's
  values EXACTLY on all three objects;
  nec_min and rho_min are the base's.
  The joint was not spent at its home:
  per-node DEC minima at nodes 20–30
  are the base's, unchanged (diagnostic
  read, SS6). The base's DEC at the
  basin was comfortable (+4.8911x10^-5
  / +3.4415x10^-5 / +2.4431x10^-5 at
  nodes 8 / 9 / 10); the F0 fit drives
  node 10's DEC to -2.101404x10^-4 and
  node 9's to -8.7618x10^-5 (diagnostic
  read). The same dN'' swings that
  cure SEC at the basin bill DEC in
  the same window — DEC and SEC weight
  the correction differently, and the
  fit was never asked about DEC.
- **Why the fit could not see it: the
  scalar joint's FD row at the base is
  IDENTICALLY 0.0 in all 27 columns.**
  At the base the joint is DEC-bound at
  r = 27.2927, far outside the supports,
  so the linearised joint constraint of
  SS4 was vacuous (0 >= -2.82x10^-9
  along every direction the LP could
  take). A scalar-joint linearisation
  is structurally blind to an argmin
  RELOCATION: the DEC argmin moved from
  node 41's neighbourhood into the
  basin, a move no first-order model of
  the scalar joint at the base can
  represent. The registered fit is
  judged exactly as run — this is its
  anatomy, not an excuse: the joint
  constraint must be carried as NODE
  constraints (DEC at the basin nodes)
  in any successor fit, because the
  scalar carries no signal.
- **The set-SEC residue splits by
  rung.** F0 and F1 leave the set SEC
  at -6.459908493210403x10^-6 at node
  25 (the OUTER locus, r = 17.0488,
  Type-I) — a pre-existing feature of
  the bought base (its second-deepest
  SEC node), outside every W474 support
  and bit-identical on both objects;
  with the basin cured it becomes the
  set argmin, at 0.71x the base's own
  set depth. F2 instead bills node 11's
  SEC to -4.365759013621926x10^-4
  (Type-I, the set argmin): the widest
  fit's right-edge authority (node 11
  sits in W474C's right taper) rings
  the window edge — 460's node-8
  pattern, one node further out.
  Node 7's SEC: unchanged at
  -6.289504x10^-7 on F0/F1; cured
  incidentally on F2 (+2.942617x10^-5).
  Node 11 on F1: -6.496095x10^-8,
  nearly cured incidentally.

## 4. The bill map against fit freedom
## (SS6, form 3's required statement)

- On the fit's own constraint set
  (SEC at nodes 8, 9, 10): the bill
  goes from the base's +9.113x10^-6
  deficit to CURED at all three rungs
  (d* = -1.260x10^-5 / -2.392x10^-5 /
  -7.049x10^-7; non-monotone, SS2).
  The 449/460 intra-basin SEC bill is
  NOT a constant bill and NOT a
  shrinking one — it is removable
  outright by joint fitting.
- The binding bill — DEC at node 10,
  which is what refuses every object —
  GROWS monotonically with fit freedom:
  -2.101x10^-4 (F0, 9 par) ->
  -5.375x10^-4 (F1, 18 par) ->
  -2.011x10^-3 (F2, 27 par), factors
  ~2.6x and ~3.7x per rung, tracking
  the dN'' violence the LP spends
  (pen 1.61 / 1.79 / 5.65 x10^-6;
  corr_dNpp extremes growing to
  +/-15.6 at F2).
- The set-SEC bill: -6.460x10^-6 at a
  pre-existing outer locus (F0, F1 —
  shallower than the base's own set
  bill) vs -4.366x10^-4 at node 11
  (F2 — 48x the base's set depth).

**Statement of the distinction, with
numbers:** this is not a priced
approach — a priced approach's bill
shrinks toward zero as freedom widens,
and the binding bill here grows ~3x
per rung. Nor is it 460's shape (a
constant intra-basin SEC bill): that
bill is cured. The class's shape, as
now measured, is a RELOCATION WITH A
GROWING PRICE: within this lever class,
jointly curing the basin's SEC is
always available, and the charge is
levied by DEC at the sister node in
proportion to the correction's violence
— i.e. to the authority the fit spends.
A shape theorem in embryo would be the
statement that the DEC charge at the
basin is bounded below by a positive
function of the SEC cure demanded
there; this phase prices three points
of that function (cure slacks
+1.26x10^-5 / +2.39x10^-5 / +7.05x10^-7
bought at DEC bills -2.10x10^-4 /
-5.38x10^-4 / -2.01x10^-3) but does not
prove the bound — the three points come
from one registered fit's LP solutions,
which saturate their trust region, and
a gentler fit might pay less (SS5,
follow-up (ii)).

## 5. Follow-ups named (none launched
## by this phase)

- (i) THE DEC-CONSTRAINED FIT: the
  successor this anatomy names — the
  same joint fit with DEC at nodes
  8, 9, 10 carried as fit constraints
  alongside SEC (six node constraints),
  the scalar joint dropped or kept as
  a seventh. The constraint set is
  decidable by the same machinery.
- (ii) A GENTLER FIT: roughness-priced
  objective or a smaller trust region.
  The DEC bill scales with the spent
  dN'' violence across this phase's
  three points; whether a low-roughness
  jointly-fitted lever pays materially
  less DEC for the same SEC cure is an
  open, decidable question — and the
  honest caveat on SS4's embryo.
- (iii) THE OUTER LOCUS: on the two
  narrower objects the set's SEC argmin
  is now node 25 (-6.460x10^-6), outside
  every W474 support. Closing the set
  needs a lever address there (460's
  GN450 family lives at those radii)
  composed with a basin cure — a joint
  basin+outer fit is a different
  registration.

## 6. Discipline, spend, disclosures

Registration filed before computation;
**no amendments**. Exactly the SS4 fit
was judged; no near-miss was
re-optimised; no lever outside SS2 was
tried. Spend: 59 checkpointed exact
SET-244 reads (2 controls, 54 FD
columns across the two registered FD
steps, 3 fit candidates) in
results/p474_reads.jsonl, plus 3
confirmation objects (each: full read +
worst-null + adversary polish) in
results/p474_confirmations.json.
Disclosed: two post-verdict diagnostic
reads (the base and the F0 output,
node DEC profiles) were run to localise
the DEC bill per node for SS3's
anatomy; they judged nothing and no
verdict input comes from them. No
incidents: the controls, fit and
confirmation runs each completed in a
single pass; CTL-474-3's step-halving
was a registered rule firing, not an
incident. All reads VM, Phase-166 pin,
float64, SET-244 / SAMPLER-M
(eulerian_that association, 449-lib
forms). Deciding SEC values at nodes
8, 9, 10 and both set argmins sit at
Type-I points and are quoted as
frame-invariant statistics. No pool,
no Kaggle, no ledger append, no
successor launch, no user contact.
