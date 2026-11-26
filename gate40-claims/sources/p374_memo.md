# PHASE 374 MEMO — THE LONG DWELL

Charged at ledger entry 943 (Phase 364's named
reopening territory, first arm: longer periods and
higher floor lifts on 364's winning corner).
Registration: `phase374/work/p374_registration.md`,
filed before any computation of this phase; Phase
364's Amendments 1 and 2 adopted at filing (SS6).

## SS0. FTL VERDICT (leading)

**WORST-INSTANT LEVEL IMPROVES AGAIN** — in the
registration's SS7 sense, stated exactly: twelve
of the sixteen registered members have a joint
worst-instant level at J = 128 at or above
L_364 + tol (tol = 1.0x10^-6), with C1 at every
audited instant, floors at every audited instant,
and C2 at the worst instants (SS3). The best is
**SNM_a0.15_T640_D0.750_m0.88**: joint
worst-instant level **-2.099385x10^-4**, which is
**+6.966x10^-6 above 364's best level
-2.169048x10^-4** and **+2.201x10^-5 (9.5%) above
the stationary level L_stat = -2.319453x10^-4**.
Its NEC_worst = -2.099385x10^-4 (margin
+6.966x10^-6 over NEC_364; +2.201x10^-5 over
NEC_stat). Its DEC_worst = -1.941081x10^-4:
**this REGRESSES against 364's DEC coordinate by
-8.638x10^-6** (DEC_364 = -1.854699x10^-4), while
still beating the stationary DEC by +2.926x10^-5.
The registration's verdict is on the JOINT level
and anticipated this mixed case; both margins
stand on the face of the verdict here. The best
member that improves BOTH champion coordinates is
SNM_a0.30_T640_D0.750_m0.88 (joint level
-2.143888x10^-4, +2.516x10^-6; DEC_worst
-1.696387x10^-4, +1.583x10^-5 over DEC_364).

WHAT THIS VERDICT DOES NOT MEAN, on its face:
**EVERY LEVEL IN THIS PHASE REMAINS NEGATIVE.**
Every member still violates NEC and DEC at its
worst instant; there is NO EC pass, no member in
the energy-condition sense, and the pressure
wall STANDS — moved at the worst instant from
-2.319453x10^-4 (stationary) through
-2.169048x10^-4 (Phase 364) to -2.099385x10^-4
here. Per the registration the result is flagged
prominently for GATE REFERRAL; the referral
itself is the parent's act. Sustainment,
front/joint and transport reads remain separate
charges, untouched.

The other three goals: (2) wormhole — untouched
by this phase. (3) subluminal record — untouched;
Procaccia 0.1363 stands, programme verified best
0.10 stands. DESK: NO DATA CONTACT.

## SS1. CONTROLS (registration SS4; stored in
## results/p374_controls.json, ALL PASS, VM =
## frame of record)

- CTL-2 (vectors): A2's K = 33 vectors from
  p344_confirmation.json equal those in
  p344_state_A2.json at max diff 0.0.
- CTL-W (waveform self-check): the analytic
  (mu, mu_phi, mu_phiphi) of the dwelling shape
  against centred FD of mu itself, on the two
  NEW registered shapes (D = 0.75, m in {0.75,
  0.875}) at a = 0.30, with 364's Amendments 1-2
  adopted at filing — mu_phi FD errors
  6.40x10^-12 / 3.84x10^-12 (bars 1.358x10^-5 /
  1.179x10^-5); mu_phiphi FD errors 3.096x10^-4 /
  1.548x10^-4 (bars 2.404x10^-3 / 1.702x10^-3);
  periodicity deviations <= 4.44x10^-16
  (Amendment 2 bar 1.0x10^-12); mu range
  endpoints match the registered
  [1 + a(2m - 1), 1 + a] on both shapes.
- CTL-T1 (reduction): the time-dependent tensor
  with all time-derivative arrays zero reproduces
  p316_lib.T_from_SNM at diff 0.0.
- CTL-T3 (flat limit): max |T| = 0.0 exactly, at
  phi = 2.6 inside the falling transition of the
  CTL-T2/T3 member {SNM, a = 0.30, T = 320,
  D = 0.75, m = 0.75} (mu, mu_dot, mu_ddot all
  nonzero there).
- CTL-T2 (independent path): the from-scratch 4D
  centred-FD Einstein tensor agrees with the
  analytic tensor at rel 2.505x10^-6 (bar
  1.0x10^-3), abs 0.0 on small components, FD
  self-spread 2.503x10^-6 (bar 2.0x10^-4), at
  h = 0.0125, on the same member at phis
  {2.6, 3.5}. The 349-licensed tensor, with
  364's dwelling layer, is RE-LICENSED by an
  independent path before any modulated read.
- CTL-0 (stationary anchor, 344 path): A2's SET
  reads and polished depth reproduce the stored
  confirmation at diff 0.0 on every read.
- CTL-1 (zero modulation, new path): the anchor
  member reproduces A2's stored SET reads at
  diff 0.0 at EVERY one of the 32 audited
  instants.
- FRAME (SS5): the laptop pool ran the controls
  first and was NOT admitted — CTL-2/W/T1/T3
  exact or passing and CTL-T2 passed there
  (rel 2.50x10^-6), but CTL-0 differed (NEC min
  1.05x10^-6, WEC min 8.31x10^-6) and CTL-1
  differed (max 8.31x10^-6) — the 344/348/349/
  364 pattern a fifth time. Execution fell back
  to this VM, the frame of record. Laptop
  record: results/p374_controls_laptop.json.

## SS2. THE SCAN (SS6.3; results/p374_scan.json,
## 17 members x J = 32 = 544 instant-reads,
## inside the 1600 cap)

The registered family: the anchor plus subsets
{M} and {S,N,M} x a in {0.15, 0.30} x
T in {320, 640} m x m in {0.75, 0.875}, all at
D = 0.75. C1 held at every instant of every
member (global min rho = +8.638078x10^-5, the
anchor's; every modulated member's min rho
>= +8.725x10^-5). ZERO floor-infeasible instants
anywhere. The anchor reproduced L_stat exactly
(NEC -2.319453x10^-4, DEC -2.233693x10^-4). At
J = 32 every one of the sixteen members already
sat above L_stat, and the whole corner sat
within ~2x10^-6 of the champion level — the
registered 6.0x10^-6 near-window therefore
captured all sixteen members for refinement
(SS3). J = 32 levels are superseded by the
J = 128 audits below wherever they differ.

## SS3. REFINEMENT, ACCEPTANCE, AND
## CONFIRMATION (SS3 + SS6.5; results/
## p374_refine.json, p374_anchor128.json,
## p374_confirm.json)

Refinement list per SS3: (i) best L_worst
(SNM_a0.15_T640_D0.750_m0.88), (ii) largest
L_best (SNM_a0.30_T640_D0.750_m0.75), (iii) the
6.0x10^-6 near-window members — which proved to
be ALL SIXTEEN non-anchor members, each audited
at J = 64 and J = 128 (4096 reads).

ACCEPTANCE: side (i) PASSED at 0.0
(|L_worst(128) - L_worst(64)| = 0.0 for the (i)
member). Side (ii) FAILED:
|L_best(128) - L_best(64)| = 1.753x10^-6
> 1.0x10^-6 for the (ii) member (L_best moved
from -2.021046x10^-4 at J = 64 to -2.003513x10^-4
at J = 128 — the finer grid finds a better
transit instant, as in 349). The registered
consequence — the entire scan re-audited at
J = 128 — was therefore executed: the refinement
list had already re-audited all sixteen
non-anchor members at J = 128, and the remaining
member, the anchor, was audited at J = 128 with
the identical machinery (results/
p374_anchor128.json: L_worst = NEC_worst
= -2.319453133x10^-4 = L_stat exactly, DEC_worst
= -2.233693204x10^-4 = DEC_stat exactly, min rho
+8.638078x10^-5, zero floor-infeasible instants).
The entire 17-member scan thus stands re-audited
at J = 128 in substance. This is the registered
consequence executed, not a deviation. Every
J = 128 audit: zero floor-infeasible instants,
min rho >= +8.638x10^-5.

THE TWELVE CANDIDATES (J = 128; margins against
the Phase 364 champion bars NEC_364 = L_364
= -2.169048x10^-4, DEC_364 = -1.854699x10^-4):

  member                       L_worst (margin)          DEC_worst (margin)        worst phi (NEC / DEC)
  SNM_a0.15_T640_D0.750_m0.88  -2.099385x10^-4 (+6.966x10^-6)  -1.941081x10^-4 (-8.638x10^-6)  3.1416 / 3.1416
  M_a0.15_T640_D0.750_m0.88    -2.099688x10^-4 (+6.936x10^-6)  -1.941081x10^-4 (-8.638x10^-6)  2.9943 / 3.1416
  SNM_a0.15_T320_D0.750_m0.88  -2.107291x10^-4 (+6.176x10^-6)  -1.941081x10^-4 (-8.638x10^-6)  2.9943 / 3.1416
  M_a0.15_T320_D0.750_m0.88    -2.109895x10^-4 (+5.915x10^-6)  -1.941081x10^-4 (-8.638x10^-6)  2.9943 / 3.1416
  M_a0.30_T640_D0.750_m0.75    -2.132906x10^-4 (+3.614x10^-6)  -1.854699x10^-4 (0.000)        2.5525 / 3.1416
  M_a0.30_T320_D0.750_m0.75    -2.135484x10^-4 (+3.356x10^-6)  -1.854699x10^-4 (0.000)        3.5834 / 3.1416
  SNM_a0.30_T640_D0.750_m0.75  -2.135692x10^-4 (+3.336x10^-6)  -1.854699x10^-4 (0.000)        2.5525 / 3.1416
  SNM_a0.30_T320_D0.750_m0.75  -2.137445x10^-4 (+3.160x10^-6)  -1.854699x10^-4 (0.000)        3.5834 / 3.1416
  SNM_a0.30_T640_D0.750_m0.88  -2.143888x10^-4 (+2.516x10^-6)  -1.696387x10^-4 (+1.583x10^-5)  2.8471 / 3.1416
  M_a0.30_T320_D0.750_m0.88    -2.144095x10^-4 (+2.495x10^-6)  -1.696387x10^-4 (+1.583x10^-5)  2.8471 / 3.1416
  M_a0.30_T640_D0.750_m0.88    -2.145011x10^-4 (+2.404x10^-6)  -1.696387x10^-4 (+1.583x10^-5)  2.8471 / 3.1416
  SNM_a0.30_T320_D0.750_m0.88  -2.149139x10^-4 (+1.991x10^-6)  -1.696387x10^-4 (+1.583x10^-5)  2.8471 / 3.1416

(NEC_worst = L_worst for every candidate — the
joint level is NEC-carried throughout this
corner. The four a = 0.15 / m = 0.75 members fell
below L_364 + tol at J = 128 — L_worst
-2.172167x10^-4 .. -2.192407x10^-4 — while still
beating L_stat by +1.27x10^-5 .. +1.47x10^-5.)

CONFIRMATION (SS6.5): adversary polish at each
candidate's NEC-worst and DEC-worst instants —
C2 PASSES at all twenty-four (polished depths
-1.693611x10^-4 .. -7.580368x10^-5, all past the
-0.0034 bar by more than an order of magnitude;
the polished Type-I depths are BETTER than the
SET worst reads, i.e. the polish does not
undercut the SET-grade condition). Exact
pointwise worst-null at each worst instant's SET
NEC argmin reproduces the SET NEC min exactly at
twenty-three instants and to +1.1x10^-19 (one
float64 ulp at this scale) at the remaining one
(e.g. -2.099385x10^-4 for the best member, whose
NEC-worst and DEC-worst instants coincide at
phi = pi). The DEC-worst instant of every member
is exactly the bottom point phi = pi, grid-stable
at J = 32/64/128.

## SS4. ANATOMY

1. THE LONG DWELL SATURATES ITS QUASI-STATIONARY
   BOUND. The best member's worst instant is
   phi = pi, which for this waveform is a
   BOTTOM-DWELL instant: mu = 1.1125 with
   mu_dot = mu_ddot = 0 exactly (verified from
   the waveform itself). Its read there IS the
   stationary read at mu = 1.1125:
   NEC_stat(1.1125) = -2.099385x10^-4 binding
   over DEC_stat(1.1125) = -1.941081x10^-4. The
   top of its range (mu = 1.15, also a dwell
   read) has L = -2.031811x10^-4. So the
   champion's L_worst equals min over its
   visited mu-range of L_stat(mu), attained at
   a stationary instant: at T = 640 NO transit
   instant undercuts the bottom dwell. The
   transit tax at the verdict instant is zero;
   what binds is the stationary level's own
   mu-profile across the visited range.
2. THE PERIOD LEVER IS NEARLY EXHAUSTED. The
   T = 320 twin of the champion still has its
   worst instant in transit (phi = 2.9943) at
   -2.107291x10^-4 — a residual transit tax of
   7.906x10^-6 below the bottom level — and the
   T 320 -> 640 step buys exactly that back
   (+7.906x10^-6) and no more. On the a = 0.30
   line the saturation is plainer: SNM m0.75
   reads T = 160 (364) -2.169048x10^-4 ->
   T = 320 -2.137445x10^-4 (+3.160x10^-5) ->
   T = 640 -2.135692x10^-4 (+1.753x10^-6). Each
   doubling buys ~20x less than the last; the
   a = 0.30 members' J = 128 levels still sit
   0.5x10^-6 .. 1.7x10^-5 below their range top
   L_stat(1.30) = -2.132388x10^-4 (residual
   transit tax at phi ~ 2.55-3.58), shrinking
   with T but not yet zero — their worst
   instants have not yet reached the dwell.
3. THE LIFT IS WHAT PAID HERE, AND IT PAYS
   THROUGH THE STATIONARY PROFILE. At a = 0.15,
   raising m from 0.75 to 0.875 lifts the
   binding bottom from mu = 1.075 to
   mu = 1.1125, worth +7.278x10^-5 (SNM, T = 640)
   — the largest single gain in the phase. At
   a = 0.30 the same lift is worth ~0 on the
   joint level (-0.8x10^-6 .. -1.2x10^-6: the
   top, not the bottom, binds there) but
   +1.583x10^-5 on DEC, whose worst instant is
   always the bottom. The lift and period taxes
   are thereby separated: period buys down the
   transit tax toward the quasi-stationary
   bound; lift moves the bound itself, along
   L_stat(mu).
4. DEC IS BOTTOM-CARRIED EVERYWHERE.
   DEC_worst = DEC_stat(bottom mu) exactly for
   all sixteen members at every density:
   -2.032703x10^-4 (mu = 1.075), -1.941081x10^-4
   (mu = 1.1125), -1.854699x10^-4 (mu = 1.15),
   -1.696387x10^-4 (mu = 1.225). The champion's
   DEC regression against DEC_364 is the price
   of its shallower range bottom (1.1125 < 1.15)
   — the same stationary DEC(mu) profile that
   364's champion rode at mu = 1.15.
5. CO-MODULATION REMAINS NEARLY FREE. SNM vs M
   twins at the champion corner differ by
   3.03x10^-7 in L_worst (SNM better); DEC_worst
   is shared exactly within each (a, m) pair —
   the bottom point is M-carried, as in 349
   and 364.
6. THE LARGEST INSTANTANEOUS LEVEL (anatomy,
   not a level): the (ii) member
   SNM_a0.30_T640_D0.750_m0.75 reaches
   L_best = -2.003513x10^-4 at J = 128, on the
   transit approach to the bottom (its J = 128
   curve sits at the top-dwell read
   -2.132388x10^-4 across both dwell plateaus
   and dips only in transit). The level of a
   member is its worst instant, SS3.

## SS5. THE CLASSIFICATION STATEMENT

At the SS1 pose, across the registered long-
dwell family (16 members: subsets {M}, {S,N,M};
a in {0.15, 0.30}; D = 0.75; m in {0.75, 0.875};
T in {320, 640} m), the dwelling pose's
worst-instant level is bounded by the
quasi-stationary bound min over the visited
mu-range of L_stat(mu), and the bound is
ATTAINED inside the family: the best member's
worst instant is a stationary dwell instant and
its level is the stationary level at its range
bottom. Both of 364's taxes are now measured to
their floors at this corner: the transit (period)
tax falls to zero at the champion's worst
instant by T = 640 and to <= 3.3x10^-6 on the
top-bound a = 0.30 line; the lift (range) tax is
the stationary profile's variation across the
visited range, and it — not any time-dependent
term — sets the level. Extending the period
further inside this family buys nothing once the
worst instant is a dwell instant; the pose has
fully cashed out, and the wall it meets is the
STATIONARY wall read at the best visited mu.
The wall stands at -2.099385x10^-4
(worst-instant, dwelling pose) against
-2.319453x10^-4 (stationary) and -2.169048x10^-4
(Phase 364's dwelling corner). No EC pass.
Reopening territory (named, not charged here):
a pose that changes the stationary profile
itself at the visited mu — a different centre or
shape class — since no dwelling range placement
at THIS centre can beat min over its range of
this centre's L_stat(mu) by more than the
profile's own variation.

## SS6. COVERAGE AND PROCESS (deviations and
## amendments disclosed)

- Registered protocol executed in full: SS4
  controls (SS1), SS6.3 scan (544 of the
  1600-read cap), SS3 refinement (16 members at
  J = 64/128 — the near-window captured the
  whole corner), the SS3 acceptance (side (i)
  passed, side (ii) FAILED at 1.753x10^-6) and
  its registered consequence (anchor audited at
  J = 128; entire scan re-audited at J = 128 in
  substance), SS6.5 confirmation (triggered —
  twelve candidates — and executed: polish +
  worst-null + C1/C2 at the worst instants;
  instantaneous anatomy on the largest-L_best
  member).
- NO NEW AMENDMENTS. Phase 364's Amendments 1
  (CTL-W FD step 5.0x10^-5) and 2 (CTL-W
  periodicity bar 1.0x10^-12) were adopted at
  filing in this phase's registration and
  applied unchanged. Refinement (i) was
  executed as BEST L_worst, adopted at filing
  (349/364 precedent), not as a mid-phase
  reading.
- FRAME: laptop not admitted (SS1); all
  production reads are VM reads. The laptop
  copy holds the synced tree plus its
  non-admitted control record, copied back to
  results/p374_controls_laptop.json the same
  session.
- INTERRUPTIONS (disclosed): four runtime
  restarts during the compute window killed
  detached workers — the scan once (after 3 of
  17 members) and the refinement three times
  (once early, then after 23 and after 31 of
  32 audits). Every run resumed from its
  per-member / per-audit checkpoint file with
  zero re-reads; no read was lost or duplicated,
  and every checkpointed value stands as
  written. Further restarts interrupted only
  coordinator monitoring sleeps.
- LOAD: the VM was shared with other pilots'
  jobs throughout (load average ~5 on 4 cores);
  per-read wall times ran ~4.7-11 s against
  364's ~5.9 s. Wall times only; no read is
  affected.

## SS7. FENCES

The verdict binds ONLY the registered family
(SS2: subsets {M}, {S,N,M}; common (a, Om, D, m)
per member; smoothstep dwelling waveform; spline
corrections FIXED at the A2 centre — no re-search
under modulation) at the SS1 pose (beta = 1.1,
the A2 lineage). Every level quoted is a
BAND-POSED read over r in [10, 20] on that
lineage, quoted as such: the A2 object's
full-extent caveats travel with it (Phase 356:
over the full stored extent [10, 60] the
stationary object's levels restate to
~ -1.44x10^-3, the tail carrying the
unaccompanied M-fall identity); nothing here is
a full-extent read. Levels only: NO EC pass is
claimed by the verdict name or anywhere in this
memo, and every level reported remains negative.
No sustainment, front/joint, or transport
wording is used or implied. DESK: NO DATA
CONTACT.
