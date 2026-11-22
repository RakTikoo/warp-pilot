# P16-1 — Pulsing wall in GR: verdict memo

**Plain language first.** We took the one warp-shell design this
programme has fully verified (Finalist-A: a spherical matter shell,
inner radius 10, outer radius 20, mass 2, drifting at 2% of light
speed) and made it move in three genuinely time-dependent ways:
breathing in and out, surging its drift speed up and down, and
running a density wave back and forth across the wall. Each version
was audited at 12 moments spread over a full cycle with the Phase 7
non-stationary auditor, and a version only counts as legal if it is
legal at *every* moment.

The short answer: **making the wall move never helped, and mostly
hurt.** One gentle version — the wall breathing at half amplitude —
stayed legal at every moment, so a genuinely time-dependent legal
shell does exist. But it bought nothing: the still wall at the same
average settings was already legal, neither version contains any
negative energy, and the breathing wall's safety margin was actually
a bit thinner than the still wall's. Everything stronger broke the
energy conditions at some moments of the cycle:

- Breathing at full amplitude broke at the squeezed part of the
  cycle. Part of that is the squeezed shape itself being illegal
  even frozen still; part is purely the motion — at one moment the
  frozen shape passed and the moving one failed. Slowing the same
  breathing down five-fold (period 200 instead of 40) made it fully
  legal again, so it is the *speed* of the change that kills it, not
  the size of the change alone.
- Surging the drift speed broke whenever the speed rose above about
  0.025 (2.5% of light speed) — but that is mostly not the motion's
  fault: the *still* wall is itself illegal at those speeds. The
  surge spends part of each cycle in a speed range where no still
  wall of this family is legal. The motion adds a small extra tax of
  its own (about 1e-5 in the DEC margin at the moments of fastest
  speed change), which by itself flips two borderline moments from
  pass to fail at the largest amplitude.
- The travelling density wave failed worst of all — but honestly,
  it never had a chance: the smooth Gaussian density profile it was
  built on is itself illegal even standing still (the verified
  design uses a different, edge-peaked profile). The wave motion
  then made a bad situation worse. This verdict is about that
  profile family; a travelling wave on the verified edge-peaked
  profile was not tested.

No version, at any moment, contained any negative Eulerian energy —
the same as the still wall. There is no pulse regime here that the
still wall forbids and the moving wall permits.

**Overall P16-1 verdict: time-dependence does not help.** One
NEUTRAL (breathing, amplitude 0.5), KILL for the other five
configurations, per the pre-registered bars in CHECKPOINT16.md
§P16-1. No variant earns HELPS, and none earns the strict HURTS
label either (that label requires every frozen instant to pass;
every failing variant also had failing frozen twins at its failing
instants — the pure time-derivative failures at individual instants
are documented in the anatomy below).

---

## Validation gate (reported before any dynamic verdict)

The construction (32 precomputed shell slices per period, periodic
cubic interpolation of the metric functions in t, shift window and
β evaluated analytically) was run at amplitude δ=0, where it must
reproduce the stationary Finalist-A audit exactly:

- Interpolated-machinery core worst margin at h=0.3:
  **+1.1949248907449214e-05**; stationary auditor on the same points:
  **+1.1949248907449214e-05**; absolute difference **0.0**. Type I
  fraction 1.0 in both. Same result at a non-grid instant (t=7.3).
- Static baseline h-ladder: core worst +1.1949e-05 at h=0.3 and
  +1.1949e-05 at h=0.15 (DEC 1.19492e-05 / 1.19494e-05) — matches
  the frozen Finalist-A headline (+1.19e-5, Type I 1.0).

Gate: **PASS**.

## Setup (all variants)

M_geom = 2.0 fixed; β0 = 0.02; T = 40 unless stated; 832 audit
points (26 Fibonacci directions × radii 8–22 in 0.5 steps, plus
cavity spot checks at r = 2, 4, 6); h = ht = 0.3 primary, h = 0.15
confirmation at each variant's worst instant; margins on the
verify_finalist "core" mask (max|T̂| > 1e-5), "sig" mask also
tracked. Cavity points carried max|T̂| ≤ ~3e-8 in every dynamic run
(no cavity core points anywhere). float64 throughout; auditor
`phase7/p74_auditor.py` reused unmodified.

Exoticity measures: Eulerian negative-energy content of the shell
sample, E_- = Σ min(ρ_Euler, 0)·ΔV, and the volume-integrated
negative NEC part over the shell sample. **E_- = 0.0 at every
instant of every variant, and in the static twin** — no sampled
point anywhere has negative Eulerian density. All NEC failures
below are pressure / Hawking–Ellis-type failures, not negative
density.

## (i) Breathing — R1(t) = 10 − δ·sin(2πt/T), R2(t) = 20 + δ·sin(2πt/T)

Shift window [R1(t), R2(t)] follows the wall; edgepeaked wd=3.0 /
floor=0.2, s_rho=2.0, s_P=1.16 (the Finalist-A profile family).

**δ = 0.5, T = 40 — NEUTRAL.** Legal at all 12 instants. Worst-instant
core margins: NEC +9.52e-06, WEC +9.52e-06, SEC +7.20e-06,
DEC +9.52e-06; Type I fraction 1.0 at every instant; h=0.15 at the
worst instant (t=10) confirms +7.19e-06. No margin drift across the
period (mirrored phases agree). Why not HELPS: the static twin at
the same mean parameters is the verified Finalist-A, which also
passes — the dynamics unlocks no new legal configuration; the
time-averaged exoticity is identical to static (E_- = 0,
NEC-negative integral = 0 in both); and the worst margin is
thinner than static (+7.2e-06 vs +1.19e-05). A genuinely
time-dependent legal shell exists; it costs margin and buys
nothing.

**δ = 1.0, T = 40 — KILL.** Worst-instant core margins: NEC
−1.04e-05, WEC −6.95e-05, SEC −1.00e-04, DEC −5.8e-09; Type I
fraction < 1 at three instants (min 0.967); h=0.15 at the worst
instant (t=30) confirms SEC −6.70e-05, Type I 0.978 — KILL bar met
on both clauses. Anatomy, mixed:
- t=30 is peak compression (R1=11, R2=19): the *frozen* compressed
  geometry is itself illegal (frozen core worst −3.88e-05, Type I
  0.985), and the dynamic audit is worse (−1.00e-04).
- t=26.67: the frozen geometry passes (+1.53e-05, Type I 1.0) while
  the dynamic audit fails (−5.46e-05, Type I 0.970) — a pure
  time-derivative failure at that instant.
- Time-averaged NEC-negative integral −5.6e-04 (static: 0).

**δ = 1.0, T = 200 (quasi-static control) — NEUTRAL, legal.** All 6
audited instants pass; worst-instant core worst +1.19e-05, Type I
1.0 everywhere. Same amplitudes as the killed T=40 run, five times
slower: the controlling variable is the *rate* of breathing, not
the amplitude alone.

## (ii) Oscillating shift — β(t) = 0.02·(1 + A·sin(2πt/40)), static profile

**A = 0.5 — KILL. A = 1.0 — KILL.** Worst-instant core margins:
A=0.5: SEC −1.16e-04, NEC −1.22e-05, Type I min 0.970; h=0.15
confirms −8.27e-05. A=1.0: SEC −3.61e-04, NEC −3.73e-05, Type I
min 0.832; h=0.15 confirms −3.16e-04. KILL bar met on both clauses
for both amplitudes.

Anatomy (frozen-vs-dynamic separation, computed at 4 instants for
A=0.5 and all 12 for A=1.0): **the dominant cause is not the time
derivatives.** Frozen slices at the same instants fail nearly
identically to the dynamic audit (e.g. A=1.0, t=10, β=0.04: dynamic
−3.606e-04, frozen −3.606e-04), because the static Finalist-A family
itself breaks above β ≈ 0.025: static β scan gives core worst
+6.4e-10 with Type I 0.9986 at β=0.025, −1.16e-04 at β=0.03,
−3.61e-04 at β=0.04. The oscillation spends part of each period in
a statically illegal speed regime. A genuine time-derivative
penalty also exists, isolated at the max-|β′| instants where
β = 0.02 and the frozen slice passes (+1.19e-05): for A=1.0 the
dynamic DEC margin falls to −1.09e-07 at t=0 and −2.34e-06 at t=20
(NEC unchanged at +1.28e-05) — a ~1.2e-05 DEC tax from ∂_t terms
alone, enough to flip those two marginal instants. Because the
frozen instants do *not* all pass, the strict pre-registered HURTS
label does not apply; the verdict is KILL with the anatomy above.

## (iii) Travelling density wave — 'gauss' wd=3.0, Rm(t) = 15 + Λ·sin(2πt/40)

**Λ = 2 — KILL. Λ = 4 — KILL.** Worst-instant core margins: Λ=2:
NEC −4.11e-05, WEC −4.01e-04, SEC −3.98e-04, Type I min 0.678.
Λ=4: NEC −8.28e-05, WEC −7.27e-04, SEC −8.71e-04, Type I min
0.112. Both confirmed at h=0.15. (The "worst"/DEC figure of −1.0
is the sampled-fallback normalised DEC saturating at non-Type-I
points; read it as "DEC fails, magnitude saturated" — NEC/WEC/SEC
carry the quantitative depth.) Time-averaged NEC-negative
integrals −8.2e-02 (Λ=2) and −4.2e-01 (Λ=4), vs 0 static.

Anatomy: **the base profile is statically illegal before any
motion.** The static gauss twin (Rm=15, wd=3.0, β=0.02, same
smoothing) has core NEC −1.98e-05, WEC −1.84e-04, Type I 0.844 at
h=0.3 and the same at h=0.15; frozen travelling slices fail
similarly (Type I 0.75–0.82). The motion then worsens the Type I
fraction substantially (Λ=4 dynamic min 0.112 vs 0.747 for the
frozen slice at the matched phase). Hedge, stated plainly: this
variant tests the gauss profile family more than it tests
travelling motion — the verified Finalist-A uses the edgepeaked
profile, and a travelling wave on *that* profile was not run.

## Handoff note for P16-2

Every configuration here has E_- = 0 (no Eulerian negative energy
at any instant), so the transient QI ledger for the P16-1 family
has no negative-energy pulse to budget; the failures are
pressure/type failures. Any QI-relevant pulse regime would have to
come from a different family (P16-2's one-shot Alcubierre ledger is
exactly that separate question).

## Caveats

- Kinematic audit of prescribed metrics (programme-wide R4 limit):
  legality here means the energy conditions hold for the prescribed
  geometry; no stability or matter-model claim (that is P16-3's
  registered scope, with its own honesty constraint).
- 12 instants per period (6 for the T=200 control) and 832 points
  per instant: a violation narrower than ~T/12 in time or finer
  than the 0.5 radial / 26-direction sampling could in principle
  hide between samples. The failures found are broad in both time
  and space, and the legal variants' margins are smooth across
  instants, so this cuts against hidden *passes* more than hidden
  failures.
- "No amplitude growth" for the legal variants: the configurations
  are prescribed-periodic, so growth could only appear as margin
  drift across the period; none was observed (mirrored-phase
  margins agree to ~1e-9 relative). This is not a stability result.

## Files

- Script: `phase16/p161_dynamic.py` (gate / static / breathing /
  shift / travelling pieces), `phase16/p161_controls.py` (frozen
  and static attribution controls).
- Results: `phase16/results/p161_gate.json`, `p161_static.json`,
  `p161_breathing_d0.5_T40.json`, `p161_breathing_d1.0_T40.json`,
  `p161_breathing_d1.0_T200.json`, `p161_shift_A0.5_T40.json`,
  `p161_shift_A1.0_T40.json`, `p161_travelling_L2_T40.json`,
  `p161_travelling_L4_T40.json`, `p161_controls.json` — each with
  per-instant margins, aggregates, exoticity measures,
  frozen-vs-dynamic tables (shift), and h=0.15 confirmations.
