# PHASE 364 MEMO — THE DWELLING POSE

Charged at ledger entry 916 (Phase 349's named
reopening, aimed at its measured anatomy).
Registration: `phase364/work/p364_registration.md`,
filed before any computation of this phase, with
Amendments 1 and 2 (SS6 below).

## SS0. FTL VERDICT (leading)

**MEMBER AT THE WORST INSTANT** — in the charge's
registered sense, stated exactly: four dwelling
members' WORST instants beat Phase 344's stationary
level L_stat on NEC and DEC JOINTLY, at J = 128
confirmation grade, with C1 at every audited
instant, floors at every audited instant, and C2
at the worst instants. The best is
**SNM_a0.30_T160_D0.750_m0.75**: NEC_worst
= -2.169048x10^-4 (beats NEC_stat
= -2.319453x10^-4 by +1.504x10^-5), DEC_worst
= -1.854699x10^-4 (beats DEC_stat
= -2.233693x10^-4 by +3.790x10^-5), joint
worst-instant level **-2.169048x10^-4, which is
1.504x10^-5 (6.5%) above the stationary level**.
This is the first worst-instant improvement over
the best stationary level anywhere on the
time-dependent line (349's best worst instant was
-2.459257x10^-4, BELOW L_stat).

WHAT THIS VERDICT DOES NOT MEAN, on its face: the
levels are still NEGATIVE. Every member still
violates NEC and DEC at every instant; there is
NO EC pass, no member in the energy-condition
sense, and the pressure wall STANDS — moved, for
the first time at the worst instant, from
-2.319453x10^-4 to -2.169048x10^-4. Per the
registration the result is flagged prominently
for GATE REFERRAL; the referral itself is the
parent's act. Sustainment, front/joint and
transport reads remain separate charges,
untouched.

The other three goals: (2) wormhole — untouched
by this phase. (3) subluminal record — untouched;
Procaccia 0.1363 stands, programme verified best
0.10 stands. DESK: NO DATA CONTACT.

## SS1. CONTROLS (registration SS4; stored in
## results/p364_controls.json, ALL PASS, VM =
## frame of record)

- CTL-2 (vectors): A2's K = 33 vectors from
  p344_confirmation.json equal those in
  p344_state_A2.json at max diff 0.0.
- CTL-W (waveform self-check, NEW): the analytic
  (mu, mu_phi, mu_phiphi) of the dwelling shape
  against centred FD of mu itself, all five
  registered (D, m) shapes at a = 0.30 — mu_phi
  FD errors <= 3.7x10^-11 (bars ~1.4-3.9x10^-5);
  mu_phiphi FD errors <= 9.9x10^-3 (bars
  2.4x10^-3 .. 2.3x10^-2, shape-dependent);
  periodicity deviations <= 2.6x10^-15 (Amendment
  2 bar 1.0x10^-12); mu range endpoints match the
  registered [1 + a(2m - 1), 1 + a] on every
  shape. The dwelling waveform is the registered
  shape, with the registered derivatives.
- CTL-T1 (reduction): the time-dependent tensor
  with all time-derivative arrays zero reproduces
  p316_lib.T_from_SNM at diff 0.0.
- CTL-T3 (flat limit): max |T| = 0.0 exactly, at
  phi = 2.6 inside the falling transition (mu,
  mu_dot, mu_ddot all nonzero there).
- CTL-T2 (independent path): the from-scratch 4D
  centred-FD Einstein tensor agrees with the
  analytic tensor at rel 1.093x10^-5 (bar
  1.0x10^-3), abs 0.0 on small components, FD
  self-spread 1.091x10^-5 (bar 2.0x10^-4), at the
  Amendment-carried step h = 0.0125, on the
  dwelling member (SNM a = 0.30 T40 D = 0.75
  m = 0) at phis {2.6, 3.5} — the falling and
  rising transitions. The 349-licensed tensor,
  with 364's modulation layer, is licensed by an
  independent path before any modulated read.
- CTL-0 (stationary anchor, 344 path): A2's SET
  reads and polished depth reproduce the stored
  confirmation at diff 0.0 on every read.
- CTL-1 (zero modulation, new path): the anchor
  member reproduces A2's stored SET reads at
  diff 0.0 at EVERY one of the 32 audited
  instants.
- FRAME (SS5): the laptop pool ran the controls
  first and was NOT admitted — CTL-2/T1/T3 exact
  and CTL-T2 passed there (rel 1.093x10^-5), but
  CTL-0 differed (NEC min 1.05x10^-6, WEC min
  8.31x10^-6) and CTL-1 differed (max
  8.31x10^-6) — the 344/348/349 pattern a fourth
  time. Execution fell back to this VM, the frame
  of record. Laptop record:
  results/p364_controls_laptop.json.

## SS2. THE SCAN (SS6.3; results/p364_scan.json,
## 37 members x J = 32 = 1184 instant-reads, inside
## the 1600 cap)

C1 HELD AT EVERY AUDITED INSTANT OF EVERY MEMBER
(global min rho +5.9449x10^-5, at
SNM_a0.30_T40_D0.875_m0.00); ZERO floor-infeasible
instants in the whole scan (and none in the
refinement: 2144 instant-reads total, floors
everywhere).

- ARM 1 (pure dwell, symmetric range m = 0; 24
  members): EVERY member has a DEC-SATURATED
  worst instant (L_worst ~ -1.000000), at phases
  in the bottom transit/bottom region
  (phi ~ 2.9-3.5). Dwelling — even at D = 0.875,
  where the cycle spends 7/8 of its period at the
  top — does NOT save the symmetric range: the
  down-swing to mu = 1 - a remains fatal to the
  DEC somewhere in its transit or at its bottom,
  exactly the failure 349's anatomy located, now
  shown to be a property of the RANGE, not of the
  time spent in it. Instantaneous levels at the
  dwell centre reach -2.000913x10^-4 (anatomy,
  SS4), never levels.
- ARM 2 (lifted floor, D = 0.75; 12 members): the
  m = 0.50 members are finite but fail (best:
  SNM_a0.30_T160 m0.50, L_worst -2.710014x10^-4 —
  its bottom is the centre itself, and the
  transit tax puts it below L_stat). The m = 0.75
  members split cleanly by period: at T = 40 all
  four fail (transit tax, x16 in Om^2); at
  T = 160 ALL FOUR BEAT L_stat JOINTLY already at
  J = 32 (SS3 for the J = 128 figures).
- DEC saturation count: 25 of 36 members
  (all of Arm 1, plus M_a0.30_T40_D0.750_m0.50).

## SS3. REFINEMENT AND CONFIRMATION (SS3 + SS6.5;
## results/p364_refine.json, p364_confirm.json)

Refinement list per SS3: (i) best L_worst and
(ii) largest L_best (both SNM m0.75 T160 members),
(iii) the 6.0x10^-6 near-window members — five
members audited at J = 64 and J = 128 (960
reads). ACCEPTANCE PASSED: (i)
|L_worst(128) - L_worst(64)| = 8.94x10^-7
<= 1.0x10^-6 (narrowly — stated); (ii)
|L_best(128) - L_best(64)| = 0.0. The registered
full-scan J = 128 consequence was NOT triggered.
The grids are nested; under refinement every
candidate's L_worst fell slightly (by 6.0x10^-7
to 9.7x10^-7, the NEC coordinate carrying the
movement in each case; every DEC_worst was
unchanged, its instant being the on-grid bottom
point at all densities) and every candidate
still beats both bars by > tol.

THE FOUR MEMBERS (J = 128, confirmation grade):

  member                          NEC_worst (margin)        DEC_worst (margin)        worst phi (NEC / DEC)
  SNM_a0.30_T160_D0.750_m0.75     -2.169048x10^-4 (+1.504x10^-5)  -1.854699x10^-4 (+3.790x10^-5)  2.9943 / 3.1416
  M_a0.30_T160_D0.750_m0.75       -2.224589x10^-4 (+9.486x10^-6)  -1.854699x10^-4 (+3.790x10^-5)  3.2889 / 3.1416
  SNM_a0.15_T160_D0.750_m0.75     -2.256428x10^-4 (+6.303x10^-6)  -2.032703x10^-4 (+2.010x10^-5)  2.9943 / 3.1416
  M_a0.15_T160_D0.750_m0.75       -2.272118x10^-4 (+4.734x10^-6)  -2.032703x10^-4 (+2.010x10^-5)  2.9943 / 3.1416

(All four: min rho over all audited instants
>= +8.7246x10^-5; zero floor-infeasible instants
at J = 32/64/128.)

CONFIRMATION (SS6.5): adversary polish at each
candidate's NEC-worst and DEC-worst instants —
C2 PASSES at all eight (polished depths
-1.496774x10^-4 .. -1.935726x10^-4, all past the
-0.0034 bar by more than an order of magnitude;
the polished Type-I depths are BETTER than the
SET worst reads, i.e. the polish does not
undercut the SET-grade condition). Exact
pointwise worst-null at each worst instant's SET
NEC argmin reproduces the SET NEC min exactly
(worst-null = set_nec_min at all eight, e.g.
-2.169048x10^-4 for the best member). The
DEC-worst instant of every candidate is exactly
the bottom point phi = pi, grid-stable at
J = 32/64/128.

## SS4. ANATOMY

1. THE LIFT IS THE MECHANISM; THE DWELL IS NOT.
   Arm 1 isolates the dwell: same range as 349's
   sinusoid, 7/8 of the cycle at the top — and
   the DEC still saturates in the down-swing
   transit. What Arm 2's m = 0.75 changes is the
   RANGE: mu in [1 + a/2, 1 + a] — the cycle
   NEVER visits a weakened (mu < 1) or even a
   centred configuration. 349's split said the
   help is up-displacement; the dwelling pose
   that works is the one that never comes down.
2. THE WORST INSTANTS ARE THE CYCLE'S QUIETEST
   PLACES. Every candidate's DEC-worst instant
   is the bottom point phi = pi exactly, where
   mu = 1 + a/2 and mu_dot = mu_ddot = 0: the
   quasi-stationary up-displaced configuration,
   whose stationary DEC (-1.854699x10^-4 at
   a = 0.30) is itself better than A2's. The
   NEC-worst instants sit in the transits
   ADJACENT to the bottom (phi = 2.9943 or
   3.2889), where mu ~ 1.08-1.16, |mu_dot|
   ~ 2.6-5.2x10^-3 and mu_ddot ~ +1.1-2.1x10^-3:
   the transit tax is real but, at T = 160, an
   order below the displacement gain.
3. THE PERIOD IS THE TAX RATE. At T = 40 the
   identical shapes fail by 2-4x10^-4: the
   transit terms scale with Om^2 (x16 from
   T = 160 to T = 40) while the displacement
   gain does not. The pose wants to be SLOW:
   dwell long, transit gently, never come down.
4. THE SPLIT, RE-MEASURED ON THE WINNING SHAPE
   (SS6.5 anatomy, SNM_a0.15_T160_D0.750_m0.75,
   J = 128 curve; special phases read directly):
   L(phi = 0, dwell centre, mu = 1.15)
   = -2.031811x10^-4; L(phi = pi, bottom,
   mu = 1.075) = -2.169504x10^-4; L(mid-transit,
   max |mu_phi|, mu = 1.1125, mu_dot
   = +7.031x10^-3) = -2.120749x10^-4. The whole
   cycle lives above L_stat; the largest
   instantaneous level in the family is this
   member's L_best = -1.981970x10^-4 (J = 128).
   These are anatomy, not levels — the level is
   the worst instant, SS3.
5. CO-MODULATION IS NEARLY FREE AT THE WORST
   INSTANT. The SNM and M candidates at the same
   (a, m) share their DEC_worst EXACTLY
   (-1.854699x10^-4 / -2.032703x10^-4 — the
   bottom point is M-carried, as in 349 SS3.3),
   and SNM's NEC_worst is slightly BETTER than
   M's at a = 0.30 (+5.6x10^-6): co-modulating
   S and N costs nothing at the worst instant in
   this pose, unlike the sinusoidal family where
   it saturated the DEC at a >= 0.15.

## SS5. THE CLASSIFICATION STATEMENT

At the SS1 pose, across the registered dwelling
family (36 members: subsets {M}, {S,N,M};
a in {0.15, 0.30}; D in {0.50, 0.75, 0.875};
m in {0, 0.50, 0.75}; T in {160, 40} m), the
pressure wall's worst-instant level MOVES for
the lifted-floor, slow members and only for
them: the symmetric dwelling range fails exactly
where the sinusoid failed (DEC saturation in the
down-swing), the centre-floored members fail on
the transit tax, and the four members whose
cycles never leave up-displaced configurations
(m = 0.75, T = 160) beat the stationary level at
the worst instant on both coordinates, best
-2.169048x10^-4. Combined with 348 (no slack in
any stationary base) and 349 (the sinusoid's
worst instant below L_stat), the plateau is
intrinsic to the STATIONARY and SYMMETRIC-
RANGE-periodic poses at this centre; it is NOT
intrinsic to periodic posing as such — a
sufficiently slow cycle confined to up-displaced
configurations holds a better level at every
instant. The wall stands at -2.169048x10^-4
(worst-instant, dwelling pose) against
-2.319453x10^-4 (stationary). No EC pass.

## SS6. COVERAGE AND PROCESS (deviations and
## amendments disclosed)

- Registered protocol executed in full: SS4
  controls (SS1), SS6.3 scan (1184 of the
  1600-read cap), SS3 refinement (5 members at
  J = 64/128; acceptance passed; the full-scan
  consequence not triggered), SS6.5 confirmation
  (triggered — four candidates — and executed:
  polish + worst-null + C1/C2 at the worst
  instants; instantaneous anatomy on the
  largest-L_best member).
- AMENDMENT 1 (filed before the formal control
  run): CTL-W's FD step 2.0x10^-4 -> 5.0x10^-5
  (bring-up smoke: FD truncation 3.96x10^-2
  against the D = 0.875 transit's fourth
  derivative; bars unchanged, comparison made
  stricter).
- AMENDMENT 2 (filed before the frame-of-record
  control run; grounds measured on the SS5
  laptop admission run): CTL-W's periodicity
  sub-check bar 0.0 -> 1.0x10^-12 (float64 wrap
  roundoff: measured 4.4x10^-16 .. 2.6x10^-15;
  bit-exact periodicity under a +2pi shift is
  unachievable for any wrapped-phase evaluation).
  The laptop run's CTL-W is recorded as failing
  the as-filed bar and passing the amended bar;
  the VM run passes under the amended bar.
- REFINEMENT (i) READING (disclosed): SS3's
  wording ("the member with the smallest
  L_worst") is inherited verbatim from 349 SS2,
  whose own execution took (i) as the BEST
  worst-instant member — the verdict-bearing
  one. A literal min() would select a
  DEC-saturated member whose saturated L_worst
  is not a verdict input and whose J-movement
  (~1x10^-4 in the saturation depth) would
  spuriously fail the acceptance and trigger a
  full-scan J = 128 re-audit of no verdict
  content. This phase followed 349's executed
  reading; the near-window rule (iii) in any
  case captured every member near a bar.
- FRAME: laptop not admitted (SS1); all
  production reads are VM reads. The laptop copy
  (~/work/p364root) holds the synced tree plus
  its non-admitted control record, copied back
  to results/p364_controls_laptop.json the same
  session.
- No interruptions to the scan or refinement
  (both completed in single runs; a runtime
  restart during the window interrupted only a
  monitoring sleep of the coordinator, and the
  scan's per-member checkpoint file verified
  complete at 37 members before refinement was
  launched).

## SS7. FENCES

The verdict binds ONLY the registered family
(SS2: subsets {M}, {S,N,M}; common (a, Om, D, m)
per member; smoothstep dwelling waveform; spline
corrections FIXED at the A2 centre — no re-search
under modulation) at the SS1 pose (beta = 1.1,
posed shell [10, 20]). Worst-instant quoting
only: no favourable-instant number in this memo
is a level. MEMBER AT THE WORST INSTANT is the
charge's verdict term and means exactly SS0's
statement — worst-instant improvement over
L_stat on NEC and DEC jointly under C1/floors/
C2; it is NOT an EC pass and NOT a member in the
energy-condition sense (all levels remain
negative). No claim about the sinusoidal family
beyond 349's verdict; no claim about the
stationary family beyond 348's. The Phase 344
incumbent remains the best STATIONARY level and
is untouched as such. The spherical member's
Gate-35 claims are untouched. No spinor match;
no sustainment, front/joint, transport or drive
claim. M'' was never targeted (measured dead,
four times); the M modulation enters through
M_dot / M_dot' / M_ddot, a different channel.
REOPENING territory (named in SS8 of the
registration, not run): per-profile amplitudes
and phase offsets, a spline re-search under
modulation, modulating beta, T = 10 m at
dwelling shapes, other dwell shapes, and —
named here from SS4's anatomy — longer periods
(T > 160 m) and higher floor lifts (m > 0.75) on
this winning corner, which the registered family
brackets but does not explore. DESK: NO DATA
CONTACT.
