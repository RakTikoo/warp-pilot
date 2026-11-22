# P16-3 — Stability / growth read on the breathing wall: verdict memo

**Plain language first.** P16-1 found exactly one moving shell that
stays legal at every moment: the wall breathing gently (amplitude
0.5, period 40), with a worst-moment safety margin of +7.2e-06 —
already thinner than the still wall's +1.19e-05. This task asked how
much you can push that configuration's settings before it breaks:
the thickness of its legal island in each direction.

Short answer: **the island is thin but real — it has finite
thickness in most directions, and it is NOT knife-edge in every
direction, so this is not a kill.** In most directions you can move
the settings by the full tested amount and the breathing wall stays
legal at every moment. But three places are genuinely tight:

- **Pushing the inner edge outward (R1 up) breaks it immediately** —
  even the smallest step tested (+0.25) flips the margin negative,
  confirmed at both grid resolutions. That direction is knife-edge.
- **Breathing harder breaks it at amplitude 0.6** (from 0.5) — but
  strangely, amplitude 0.75 passes again at every sampled moment.
  The boundary in that direction is pocketed, not a clean wall.
- **Taking 5% of the mass away leaves the margin at essentially
  zero** at one moment of the cycle — the coarse grid says a hair
  positive with a Type-I dip, the fine grid says clean. That point
  sits on the boundary, inside the audit's own resolution.

And one honest non-result: nothing here says whether the wall would
*hold together on its own*. Our auditor checks a prescribed,
scripted motion — it does not evolve anything. The wall repeats
identically for three cycles because we scripted it to, not because
physics keeps it there. **Dynamical stability in the evolution
sense is NOT established by anything here** (see §(b) — this is the
registered honesty constraint of §P16-3, stated in its own terms).

**Verdict (per §P16-3(c)): ROBUST-WITHIN-AUDIT** — finite thickness
in most directions (table below), knife-edge only in R1-up and in
the first amplitude pocket (2 of 13 directions, well under the
"half the directions" kill bar), with the evolution caveat attached.

---

## Method

Nominal configuration (P16-1's legal breathing wall): M_geom = 2.0,
R1(t) = 10 − δ·sin(2πt/T), R2(t) = 20 + δ·sin(2πt/T), δ = 0.5,
T = 40, edgepeaked wd = 3.0 / floor = 0.2, s_rho = 2.0, s_P = 1.16,
β = 0.02, shift window following the wall. Machinery reused
unmodified from P16-1 (`p161_dynamic.py`: 32-slice periodic
interpolation + the Phase 7 non-stationary auditor), generalised to
variable M, R centres, wd, δ, T and phase. Each perturbed
configuration was audited at 8 instants over a full period
(h = ht = 0.3, 832 points/instant, core mask as in P16-1). Any
configuration failing at h = 0.3 was re-audited at its worst instant
at h = 0.15. Nominal re-run at 8 instants reproduces P16-1's
12-instant worst exactly: **+7.203e-06 at t = 10, Type I 1.0**.

Classification (stated once, used throughout): a **confirmed flip**
fails (margin < 0 or Type I < 1) at h = 0.3 *and* at h = 0.15 at the
worst instant. A **graze** fails at h = 0.3 but passes at h = 0.15
at that instant — the boundary passes within the audit's resolution
there, and we do not call it either way.

## (a) Margin-robustness map — worst-instant core margins

| Perturbation | Worst margin (h=0.3) | Type I min | h=0.15 at worst instant | Reading |
|---|---|---|---|---|
| nominal δ=0.5, T=40 | **+7.20e-06** | 1.000 | (P16-1: +7.19e-06) | legal |
| M +1% (2.02) | +7.25e-06 | 1.000 | — | legal |
| M −1% (1.98) | +7.15e-06 | 1.000 | — | legal |
| M +5% (2.10) | +7.45e-06 | 1.000 | — | legal |
| M −5% (1.90) | +7.8e-10 | 0.998 | +1.08e-05, Type I 1.000 | **graze** — margin ≈ 0 at t=30 only |
| R1 +0.25 | −2.28e-05 | 0.994 | −4.98e-05, 0.985 | **confirmed flip** |
| R1 +0.5 | −3.65e-05 | 0.984 | −1.24e-05, 0.992 | **confirmed flip** |
| R1 −0.25 | +7.20e-06 | 1.000 | — | legal |
| R1 −0.5 | +7.33e-06 | 1.000 | — | legal |
| R2 +0.25 | +8.21e-06 | 1.000 | — | legal |
| R2 +0.5 | +9.55e-06 | 1.000 | — | legal (margin improves) |
| R2 −0.25 | +8.86e-06 | 1.000 | — | legal |
| R2 −0.5 | −2.78e-05 | 0.981 | −1.11e-04, 0.963 | **confirmed flip** |
| wd 2.5 | +7.73e-06 | 1.000 | — | legal |
| wd 3.5 | +6.82e-06 | 1.000 | — | legal |
| phase +π/4 | +7.20e-06 | 1.000 | — | identical (see below) |
| phase +π/2 | +7.20e-06 | 1.000 | — | identical |
| δ 0.4 | +7.46e-06 | 1.000 | — | legal |
| δ 0.6 | −1.84e-05 | 0.989 | −1.16e-05, 0.989 | **confirmed flip** (t=25, 35 only) |
| δ 0.75 | +5.62e-06 | 1.000 | — | legal at all 8 instants (!) |
| T 30 | +2.21e-06 | 1.000 | — | legal, margin thins ~3× |
| T 60 | +9.44e-06 | 1.000 | — | legal |

Two at a time:

| Pair | Worst margin (h=0.3) | Type I min | h=0.15 | Reading |
|---|---|---|---|---|
| M+5%, δ 0.6 | +4.29e-06 | 1.000 | — | legal — extra mass *rescues* δ=0.6 |
| M−5%, δ 0.6 | −4.38e-05 | 0.985 | −3.24e-05, 0.972 | **confirmed flip** |
| M+5%, wd 2.5 | +7.99e-06 | 1.000 | — | legal |
| M−5%, T 30 | −1.33e-05 | 0.989 | +8.90e-06, 1.000 | **graze** (flip not confirmed) |
| δ 0.6, T 30 | −9.27e-05 | 0.969 | −8.39e-05, 0.940 | **confirmed flip** — deepest failure |
| δ 0.6, wd 2.5 | −9.9e-07 | 1.000 | +6.08e-06, 1.000 | **graze** (single shallow dip at t=35) |
| R1+0.5, R2−0.5 (wall thins by 1) | −6.95e-05 | 0.982 | −3.65e-05, 0.983 | **confirmed flip** |
| R1−0.5, R2+0.5 (wall thickens by 1) | +1.05e-05 | 1.000 | — | legal, margin *better* than nominal |

### Thickness of the legal island, by direction

Distance from nominal to the nearest confirmed sign flip:

- **M up:** > 5% (no flip; margin barely moves).
- **M down:** no confirmed flip out to −5%, but the margin
  collapses to ~0 at −5% at the single peak-expansion instant
  (t = 30; every other instant stays ≥ +6.9e-06) and the two grid
  resolutions disagree there — the boundary is at ≈ 5% down,
  unresolved at the endpoint. Treat as thin in practice.
- **R1 up:** **< 0.25** — flips at the smallest step tested.
  Knife-edge.
- **R1 down:** > 0.5.
- **R2 up:** > 0.5 (margin improves — the island extends outward).
- **R2 down:** between 0.25 and 0.5 (clean at −0.25, confirmed
  flip at −0.5).
- **wd either way:** > 0.5 (both 2.5 and 3.5 clean; margin moves
  by < 1e-06).
- **Amplitude down:** > 0.1 tested (δ = 0.4 clean; the δ → 0 limit
  is the legal static shell).
- **Amplitude up:** < 0.1 to the first failing pocket — δ = 0.6
  fails at t = 25 and t = 35 only (both at sin(2πt/T) = −0.707,
  wall partly re-expanded) while passing at peak expansion
  (t = 30, +9.8e-06). **But δ = 0.75 passes at all 8 sampled
  instants**, and P16-1 showed δ = 1.0 fails. So this direction's
  boundary is pocketed and non-monotone at the sampled resolution,
  not a clean wall: there is a failing pocket at 0.6, a re-entrant
  pass at 0.75, and failure again by 1.0. (Caveat: 8 instants —
  a pocket narrower than T/8 in time could hide in the δ = 0.75
  run; the δ = 0.6 pockets are T/8-wide at least.)
- **Period down:** > 10 (T = 30 legal; margin thins to +2.21e-06 —
  faster breathing taxes the margin, consistent with P16-1's
  rate-kills finding, but T = 30 is not yet a flip).
- **Period up:** > 20 (T = 60 legal, +9.44e-06).
- **Oscillation phase:** no thickness to measure — phase offsets
  of π/4 and π/2 reproduce the nominal worst margin *exactly*
  (+7.203e-06, at the correspondingly shifted instant). A phase
  shift of a periodic prescription is a relabelling of the time
  origin, not a physical direction; included for completeness, as
  briefed.

**Diagonal anatomy.** The two thin single directions (R1 up,
R2 down) are exactly the two halves of *thinning the wall*, and
the wall-thinning pair (R1+0.5, R2−0.5) flips hard (−6.95e-05,
confirmed), while the wall-thickening pair is legal with a better
margin than nominal (+1.05e-05). Mass and amplitude trade against
each other: +5% mass rescues δ = 0.6; −5% mass with δ = 0.6 is a
confirmed flip; δ = 0.6 with the faster T = 30 is the deepest
failure in the map (−9.27e-05, confirmed −8.39e-05). The island is
thinnest along the wall-thinning diagonal and along
lower-mass / larger-amplitude / faster-breathing combinations.

## (b) Linear growth estimate — none defensible; what the boundedness check does and does not establish

**No defensible linear growth-rate estimate exists from this
machinery, and we do not report one.** Two things were checked:

1. **Margin response to the imposed oscillation amplitude** (the
   breathing mode treated as its own perturbation): worst-instant
   margin vs δ is +1.195e-05 (δ = 0, static, P16-1), +7.46e-06
   (0.4), +7.20e-06 (0.5), −1.84e-05 (0.6, pockets only),
   +5.62e-06 (0.75), −1.00e-04 (1.0, P16-1). This is **not
   monotone and not linear** — no growth rate or linear-response
   coefficient can honestly be fitted to it. The response is
   bounded (margins stay O(1e-05)) across the legal part of the
   range; that is all that can be said.
2. **Three consecutive periods at the nominal configuration:**
   worst-instant margins per period are +7.203001107399109e-06,
   +7.2030011073992255e-06, +7.203001107399109e-06 — identical,
   maximum per-instant deviation 1.6e-18. There is no drift.

**What this does and does not establish, explicitly.** The
three-period identity is true *by construction*: the metric is
prescribed to be exactly periodic (the slice interpolation wraps
t mod T and the shift/β are analytic periodic functions), so the
auditor re-audits the same prescribed geometry three times. It
establishes that the *prescription* is bounded and non-drifting —
nothing more. The auditor is **kinematic (prescribed metric, no
matter model, no Einstein evolution)**, so **dynamical stability
in the evolution sense is NOT established by anything here**: no
perturbation is ever allowed to evolve, feed back on the geometry,
or grow or decay under its own dynamics. Whether a real shell
sitting at these parameters would hold together, ring down, or
fly apart is a question this programme's machinery cannot pose,
let alone answer (§P16-3's registered honesty constraint).

## (c) Verdict

Per the registered bar in §P16-3(c): a practical KILL requires the
legal set to be knife-edge in *every* direction (operationalised
in the brief as a sign flip within the smallest perturbation step
in ≥ half the directions). Measured: confirmed flips within the
smallest step in **2 of 13 directions** (R1 up; amplitude up, to
its first pocket). Finite thickness in the other eleven, plus one
graze at the largest M-down step. The kill bar is not met.

**VERDICT: ROBUST-WITHIN-AUDIT** — the breathing δ = 0.5, T = 40
configuration's legal island has the thicknesses tabulated above:
thick (> tested range) in M-up, R1-down, R2-up, wd both ways,
period both ways, and amplitude-down; thin in R1-up (< 0.25),
pocketed in amplitude-up (first pocket at +0.1, re-entrant pass
at 0.75, failure by 1.0), 0.25–0.5 in R2-down, and grazing zero at
M −5%. The island is thinnest along the wall-thinning diagonal.
The dynamic island remains thinner than the static one in absolute
margin (+7.20e-06 vs +1.19e-05), as P16-1 found. **The evolution
caveat of §(b) is attached to this verdict in full: robustness
here means robustness of the audited margins under prescribed
parameter changes — it is not a stability result.**

## Caveats

- 8 instants per period (brief permitted ≥ 8) vs P16-1's 12: a
  violation narrower than ~T/8 in time could hide between sampled
  instants in any "legal" row. The confirmed flips are broad or
  resolution-confirmed; the δ = 0.75 re-entrant pass is the row
  most exposed to this caveat.
- Three rows (M −5%; M−5%+T30; δ0.6+wd2.5) sit within the audit's
  own h-resolution at their worst instant and are recorded as
  grazes, not flips — the island boundary passes through them.
- All margins are O(1e-05) — the same order as the static
  Finalist-A margin. "Thick" here means thick *relative to the
  tested steps*, in a configuration whose absolute margin was
  always hair-thin.
- Kinematic audit throughout (programme-wide R4 limit): legality
  = energy conditions hold for the prescribed geometry at the
  audited instants. No matter model, no evolution, no stability
  claim — see §(b).

## Files

- Script: `phase16/p163_robust.py` (checkpointed per configuration
  under `results/p163_parts/`).
- Results: `phase16/results/p163_robust.json` — all 29
  configurations with per-instant margins, Type-I fractions,
  h = 0.15 confirmations, the 3-period drift block, and a summary
  block with the thickness table and verdict.
- This memo: `phase16/results/p163_memo.md`.
