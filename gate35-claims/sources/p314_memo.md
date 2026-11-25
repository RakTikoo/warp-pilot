# PHASE 314 MEMO — THE POINTWISE PUSH

## Verdict (FTL goal, leading)

**POINTWISE MEMBER.** The extended (three-function) class
produces members whose required density is non-negative
EVERYWHERE on the posed volume (SET-244: 41 radial nodes ×
162 directions, SAMPLER-M), with both hard bars held:
depth (SAMPLER-M adversary-polished) past −0.0034 AND
ρ_req ≥ 0 at all four binding sites (Phase 293 site rule).
Five members are confirmed at full protocol (headline
first):

| member (profile) | SET-244 ρ min | depth (SAMPLER-M polished) | min site ρ_req |
|---|---|---|---|
| **ramp m₀=+4.00, rise [9, 20.5]** | **+8.272455×10⁻⁵** | −5.327659×10⁻⁴ | +1.172278×10⁻⁴ |
| ramp m₀=+4.25, rise [9, 20] | +8.161643×10⁻⁵ | −4.725941×10⁻⁴ | +1.118222×10⁻⁴ |
| ramp m₀=+4.00, rise [9, 20] | +8.066120×10⁻⁵ | −4.952192×10⁻⁴ | +1.106733×10⁻⁴ |
| ramp m₀=+4.00, rise [9, 19.5] | +8.055642×10⁻⁵ | −4.554515×10⁻⁴ | +1.044445×10⁻⁴ |
| edges m₀=+3.00 (plateau M ≡ 4) | +4.613988×10⁻⁵ | −2.407065×10⁻⁴ | +7.196712×10⁻⁵ |

(The edges member was confirmed under the E3 extent
label — rise [9,10], fall [20,21]; the E1 and E2 extents
at m₀=+3.00 give the identical in-band read at screen
grade, +4.613988×10⁻⁵, as they must: all three have
M ≡ 4, M′ ≡ 0 on the band.)

FENCE, stated before anything else: this is a DENSITY
statement about the target — ρ_req ≥ 0 at every SET-244
point of the posed shell. It is NOT an energy-condition
pass. The headline member's SET reads (SAMPLER-M) are:
NEC min −1.170007×10⁻³ (median −1.687×10⁻⁴), WEC min
−1.044069×10⁻², DEC min −1.000003, SEC min −1.200683×10⁻²;
its polished depth is −5.327659×10⁻⁴. The NEC/WEC/DEC are
still violated on the volume; what has closed is the
DENSITY leg only. No spinor match was run (the parent's
charge on a pointwise member).

## 1. Registration summary

Registration (`phase314/work/p314_registration.md`)
written before computation. Machinery: Phase 312's
p312_lib copied byte-identical (md5
504a941734e895ba8919b2630ba99358). Objective: maximise
the SET-244 ρ minimum. Hard constraints H1 (depth past
−0.0034) and H2 (binding-site ρ_req ≥ 0), never traded.
Bases: broad-ramp winner (primary), edges E1 (second
family), early-ramp winner (fallback, only on a broad
stall per the registered stall rule — the broad base did
NOT stall, round gain +8.28×10⁻⁵ ≫ the 10⁻⁸ threshold,
so the fallback was correctly never run). Coordinate
passes over the registered knobs (ramp height, placement,
width, refinement; edges height, extent), SET-screened,
with full-protocol confirmation of any screen-feasible
candidate beating the best confirmed objective and of
each family's final best screened point. Every evaluated
member is stored (`p314_screens.json`,
`p314_confirmed.json`).

## 2. Controls (all before any optimisation read)

- **K1 — PASS, exact.** Phase 312's five winners re-read
  under this phase's machinery at full protocol: SET-244
  ρ min, depth, and min binding-site ρ_req all reproduce
  the stored p312 values at **diff 0.0** (bar 1e-9), all
  five members.
- **K2 — the starting pockets, anatomised.**
  *Broad +1.0:* ρ min −7.561242×10⁻⁸ at r = 10.3659,
  direction n_x̂ = +0.0041 (near-transverse), where
  M = 1.0000 and M′ = 0 exactly — the point sits INSIDE
  the ramp's start (r1 = 10.5), so R1 = R2 = 0 and the
  pocket is carried entirely by Q_K (−7.561×10⁻⁸): the
  Phase 295 negated square at a radius where S′ is small
  but nonzero. 324 of 6642 SET points negative.
  *Edges E1 +1.0:* ρ min −6.713620×10⁻⁵ at r = 15.4878,
  n_x̂ = +0.0041, M = 2, M′ = 0: R1/(16π) = +8.294×10⁻⁵
  against Q_K/(16π) = −1.501×10⁻⁴ — on the plateau the
  negated-square remnant (at M = 2) still beats the
  (1−1/M) term at mid radii in transverse directions.
  1000 negative points.

## 3. How the pockets closed (the optimisation's anatomy)

**Height alone does nothing at the broad base.** At
(r1, r2) = (10.5, 19.5), raising m₀ through
{1.25, 1.5, 2, 3, 4} leaves the SET ρ minimum at exactly
−7.561242×10⁻⁸, argmin unmoved at r = 10.3659: the
pocket lives where M ≡ 1 by construction, upstream of
the rise, and no height reaches it. (All five height
screens are the same member on the pocket.)

**Placement is the deciding knob.** Moving the rise's
start to r1 = 9.0 — before the shell's inner edge — at
m₀ = +4.00 puts M > 1 over the whole posed volume. The
inner pocket closes (R1 > 0 and Q_K's square rescaled by
1/M at every inner point) and the minimum MIGRATES to
the outer rim: at r1 = 9.0 the SET ρ min is
+8.055642×10⁻⁵ with argmin at the outermost node
r = 19.878. At r1 = 9.5 the same value (the rim, not the
inner edge, binds); at r1 = 10.0 the inner edge reopens
partly (+8.003509×10⁻⁶, argmin back at r = 10.122, zero
negative points but a thinner margin).

**At the rim, the minimum is R1-carried against a
vanished Q_K.** The headline member's argmin
(r = 19.878049, n_x̂ = +0.0041, M = 4.994, M′ = +0.0273):
R1/(16π) = +8.053×10⁻⁵, R2/(16π) = +2.19×10⁻⁶,
Q_K/(16π) = −4.57×10⁻¹⁰ (split reproduces the tensor
ρ to 1.2×10⁻¹⁹). At the outer rim S and S′ have died, so
the negated-square remnant is ~10⁻¹⁰; the floor is set
by the (1−1/M) term at its 1/r² weakest radius. That is
why the margin improves only slowly from there: width
(r2 = 19.5 → 20 → 20.5, keeping M′ > 0 at the rim, adds
R2) gives +8.056 → +8.066 → +8.272 ×10⁻⁵; height
(m₀ = 4.25 at r2 = 20) gives +8.162×10⁻⁵ via R1's
(1−1/M) saturation curve. All confirmed members sit on
this rim floor.

**The edges family closes by height alone.** With
M′ ≡ 0 on the band, the pocket is the mid-radius
transverse contest R1 vs Q_K(M) (argmin r ≈ 15.73–15.98,
n_x̂ ≈ 0.004 throughout). Raising the plateau:
m₀ = +1.25 → −4.180×10⁻⁵ (648 negative points);
+1.50 → −2.154×10⁻⁵ (343); **+2.00 → +8.842×10⁻⁶ (0)**;
+3.00 → +4.614×10⁻⁵ (0; confirmed). The crossing is
between m₀ = +1.5 and +2.0. At the confirmed member's
argmin (r = 15.9756, M = 4): R1/(16π) = +1.169×10⁻⁴ vs
Q_K/(16π) = −7.078×10⁻⁵. Extent (E1/E2/E3) is exactly
inert, as registered.

## 4. The headline member in full

Profile: ramp, M(r) = 1 + 4.00·[U(r; 9, 20.5) −
U(r; 21, 24)], base (S, N) = Gate-30 winner verbatim,
β = 1.1. (On the posed volume M rises from 1 at r = 9 to
M ≈ 4.994 at the outer node; M ≥ 1.36 at every SET
radius ≥ 10.122.)

- Depth (SAMPLER-M, adversary-polished): **−5.327659×10⁻⁴**
  — past the −0.0034 bar by ×6.4. Polish site r = 12.3135,
  Type-I, ρ_t = +6.263×10⁻⁴.
- Full-volume density (SET-244, SAMPLER-M set):
  **ρ min +8.272455×10⁻⁵** (locus §3), median
  +2.722×10⁻⁴, max +8.831×10⁻⁴. Negative points: 0/6642.
- Binding sites (Phase 293 rule; NEC-M = SAMPLER-M NEC,
  NEC-X = exact pointwise NEC minimum; split /(16π)):

| site | r | Type-I | NEC-M | NEC-X | ρ_req | R1 | R2 | Q_K |
|---|---|---|---|---|---|---|---|---|
| S1 | 12.313 | yes | −5.327659×10⁻⁴ | −1.267419×10⁻³ | +6.263182×10⁻⁴ | +9.75×10⁻⁵ | +5.60×10⁻⁴ | −3.16×10⁻⁵ |
| S2 | 11.829 | no | −1.170007×10⁻³ | −1.183691×10⁻³ | +6.818808×10⁻⁴ | +8.09×10⁻⁵ | +6.18×10⁻⁴ | −1.74×10⁻⁵ |
| S3 | 12.317 | yes | −5.327425×10⁻⁴ | −1.266247×10⁻³ | +6.257630×10⁻⁴ | +9.76×10⁻⁵ | +5.60×10⁻⁴ | −3.17×10⁻⁵ |
| S4 | 17.683 | no | −7.107812×10⁻⁴ | −7.120705×10⁻⁴ | +1.172278×10⁻⁴ | +9.96×10⁻⁵ | +3.79×10⁻⁵ | −2.02×10⁻⁵ |

At every binding site the
density is R-carried (R2, the M′ piece, dominant at the
inner sites where the rise is steep; R1 dominant at S4),
with |Q_K| an order below R.
- Energy-condition reads, reported as they are (SET-244,
  SAMPLER-M): NEC min −1.170007×10⁻³ / median
  −1.687×10⁻⁴ / max +6.541×10⁻⁴; WEC min −1.044069×10⁻²;
  DEC min −1.000003; SEC min −1.200683×10⁻². Type-I
  count 2615/6642. **The member violates NEC, WEC and
  DEC on the volume** — pointwise ρ ≥ 0 is the density
  leg only, exactly as fenced in the registration.

## 5. The landscape (all evaluated members)

25 screened points (3 seeded from the K1 controls, 22
fresh screens) + 10 full-protocol confirmations (5 K1
seeds + 5 new). Screened SET ρ minima, by family:

- Ramp at (10.5, 19.5), m₀ ∈ {1.0…4.0}: −7.561×10⁻⁸
  (×6, identical — inner pocket, §3).
- Ramp (4.00, 10, 19.5): +8.004×10⁻⁶ (screen grade,
  0 negative points).
- Ramp (4.00, 9, ·): +8.056×10⁻⁵ (r2 = 18, 19, 19.5 —
  identical; the rim binds, width inert until the rise
  reaches it), (4.00, 9.5, 19.5): +8.056×10⁻⁵;
  (3.75, 9, 20): +7.961×10⁻⁵; (4.00, 8.5, 20):
  +8.065×10⁻⁵; (4.00, 9, 20): +8.066×10⁻⁵ confirmed;
  (4.00, 9.5, 20): +8.068×10⁻⁵; (4.25, 9, 20):
  +8.162×10⁻⁵ confirmed; (4.00, 9, 20.5):
  +8.272×10⁻⁵ confirmed (best).
- Edges E1: +1.00 → −6.714×10⁻⁵; +1.25 → −4.180×10⁻⁵;
  +1.50 → −2.154×10⁻⁵; +2.00 → +8.842×10⁻⁶ (screen);
  +3.00 → +4.614×10⁻⁵ (E1/E2 screen, E3 confirmed).
- Seeds: early +1.0 → −6.714×10⁻⁵; broad +0.5 (K1) →
  SET ρ min −4.099×10⁻⁵ (confirmed, from Phase 312).

Every screen-feasible candidate that beat the confirmed
incumbent was confirmed in-run; each family's best
screened point was confirmed at the end, per the
registration. Screen-grade pointwise reads (0 negative
SET points, H2-screen feasible) not promoted to
confirmation — (4.00, 10, 19.5), (3.75, 9, 20),
(4.00, 8.5, 20), (4.00, 9.5, 20), edges +2.00 — are
reported as screens, not members.

## 6. Fences

Verdicts bind ONLY the registered profile families,
bases and knob grids at the winner's base pose
(β = 1.1, (S,N) verbatim, posed shell [10,20]).
"Everywhere / full volume" = the SET-244 grid (6642
points) — a set read, quoted as a set read; no continuum
claim is made (between-node and off-grid behaviour is
unread; the rim floor's carrier, R1 at the outermost
node against Q_K ≈ 0, is a grid statement). POINTWISE
MEMBER is a density statement about the target, not an
energy-condition pass (§0, §4), not a spinor-matched
construction (not run — the parent's charge), and not a
joint pass or a drive. Depth is SAMPLER-M
adversary-polished on every quotation; site NEC is
quoted under SAMPLER-M and the exact pointwise read,
each named. The early-base fallback was not run (no
stall); no statement is made about it beyond its K1
seed.

## 7. Three-goals accounting

- **FTL drive:** POINTWISE MEMBER at registered scope —
  the extended class's density leg is now closed at
  SET-244 pointwise scope (was: binding-site scope,
  Phase 312; before that: an identity of the
  two-function class, Phase 295). The target these
  members pose demands ρ ≥ 0 everywhere on the shell
  while holding depth past the bar. Still NOT a drive:
  NEC/WEC/DEC fail on the volume, no spinor match run,
  no joint pass claimed.
- **Wormhole:** no read touches the wormhole standings.
  Untouched.
- **Subluminal record:** no read touches it; Procaccia
  0.1363 / verified 0.10 stand. Untouched.

**DESK: NO DATA CONTACT** — an algebra and
configuration-space phase; no real-world dataset bears
on it and none was manufactured.

## 8. Artefacts

- Registration: `phase314/work/p314_registration.md`
- Machinery: `phase314/work/p314_lib.py` (byte-identical
  copy of p312_lib), `phase314/work/p314_common.py`
- Scripts + logs: `phase314/work/p314_controls.py`,
  `phase314/work/p314_opt.py`, `*.log`
- Controls: `phase314/results/p314_controls.json`
- Screens / confirmations / log:
  `phase314/results/p314_screens.json`,
  `phase314/results/p314_confirmed.json`,
  `phase314/results/p314_opt_log.json`
- Assembled results: `phase314/results/p314_results.json`
- Checkpoint: `phase314/CHECKPOINT314.md`

No ledger append, no launches, no external contact.
