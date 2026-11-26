# CHECKPOINT 364 — THE DWELLING POSE

**STATUS: COMPLETE.**
**VERDICT: MEMBER AT THE WORST INSTANT** — in the
charge's registered sense: four dwelling members'
worst instants beat Phase 344's stationary level
on NEC and DEC jointly at J = 128 confirmation
grade (C1 and floors at every audited instant,
C2 at the worst instants). Best:
SNM_a0.30_T160_D0.750_m0.75 — NEC_worst
-2.169048x10^-4 (bar -2.319453x10^-4, margin
+1.504x10^-5), DEC_worst -1.854699x10^-4 (bar
-2.233693x10^-4, margin +3.790x10^-5), joint
worst-instant level -2.169048x10^-4. The other
three: M_a0.30 (NEC margin +9.486x10^-6),
SNM_a0.15 (+6.303x10^-6), M_a0.15 (+4.734x10^-6),
all T = 160, D = 0.75, m = 0.75. ALL LEVELS
REMAIN NEGATIVE — no EC pass; the pressure wall
is MOVED at the worst instant (-2.319453x10^-4
-> -2.169048x10^-4), not broken. Flagged for
gate referral (the parent's act).

Full memo: `results/p364_memo.md`.
Registration: `work/p364_registration.md` (filed
before computing; Amendment 1 = CTL-W FD step
2.0x10^-4 -> 5.0x10^-5; Amendment 2 = CTL-W
periodicity bar 0.0 -> 1.0x10^-12, grounds from
the laptop admission run; both disclosed in
memo SS6).

## Controls — ALL PASS (VM, frame of record)

`results/p364_controls.json`: CTL-2 vectors diff
0.0; CTL-W waveform self-check PASS on all five
registered shapes (FD errors <= 3.7x10^-11 /
<= 9.9x10^-3 vs bars; periodicity <= 2.6x10^-15
under the Amendment-2 bar); CTL-T1 reduction
diff 0.0; CTL-T3 flat limit exactly 0.0 (at a
transition phase, derivatives nonzero); CTL-T2
independent FD path PASS (rel 1.093x10^-5,
self-spread 1.091x10^-5); CTL-0 stationary
anchor diff 0.0 incl. depth; CTL-1 zero
modulation diff 0.0 at all 32 instants. Frame
admission (SS5): the laptop pool was NOT
admitted (CTL-0 SET statistics differed, max
8.31x10^-6 — the 344/348/349 pattern a fourth
time); execution fell back to the VM. Laptop
record: `results/p364_controls_laptop.json`.

## Scan + refinement + confirmation

Scan: 37 members x J = 32 = 1184 instant-reads
(inside the 1600 cap), flushed per member to
`results/p364_scan.json`; completed in a single
run, no re-reads. C1 held at every audited
instant (global min rho +5.9449x10^-5); zero
floor-infeasible instants in scan + refinement
(2144 reads). Arm 1 (m = 0, 24 members): every
worst instant DEC-saturated — dwelling does not
save the symmetric range. Arm 2: m = 0.50 fails;
m = 0.75 at T = 40 fails (transit tax); m = 0.75
at T = 160 — all four members beat L_stat
jointly. Refinement: 5 members at J = 64/128
(`results/p364_refine.json`); acceptance PASSED
((i) 8.94x10^-7 <= 1.0x10^-6, narrowly; (ii)
0.0); the full-scan J = 128 consequence was not
triggered. (SS3's (i) followed 349's executed
reading — best worst-instant member — disclosed
in memo SS6.) Confirmation
(`results/p364_confirm.json`): adversary polish
at all four candidates' NEC- and DEC-worst
instants — C2 PASSES at all eight (depths
-1.496774x10^-4 .. -1.935726x10^-4 vs the
-0.0034 bar); worst-null at each SET NEC argmin
reproduces the SET NEC min exactly. Anatomy:
the DEC-worst instant of every candidate is the
bottom point phi = pi (mu = 1 + a/2, derivatives
zero); NEC-worst instants sit in the adjacent
transits; the lift (never leaving up-displaced
configurations) is the mechanism, the dwell is
not.

## Fences / accounting

SET-244 SAMPLER-M set reads, worst-instant
quoting only; verdict binds the registered
dwelling family at the A2 centre with spline
corrections fixed (no re-search under
modulation); M'' never targeted. MEMBER here is
the charge's term (worst-instant improvement
over L_stat, jointly, under C1/floors/C2) — not
an EC pass. Three goals: FTL — worst-instant
level moved for the first time on the
time-dependent line; wall stands; wormhole —
untouched; subluminal — untouched (0.1363 /
0.10 stand).
**DESK: NO DATA CONTACT.**

Artefacts: work/p364_registration.md,
work/p364_lib.py, work/p364_controls.py,
work/p364_scan.py, work/p364_refine.py,
work/p364_confirm.py; results/p364_controls
.json, results/p364_controls_laptop.json,
results/p364_scan.json, results/p364_refine
.json, results/p364_confirm.json,
results/p364_memo.md, run logs (controls_vm.log,
controls_laptop.log, scan_vm.log, refine_vm.log,
confirm_vm.log). No ledger append, no launches,
no external contact.
