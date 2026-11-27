# Phase 431 — THE DEGENERATE MATING: memo

**Charge:** ledger entry 1137, the logical attack on the
supply-drift roadblock (entry 1135's verdict; intake entry
1136). **Question:** can the two standing supply targets be
mated under a spectrum constraint, so the supplied tensor
persists by construction — all modes at one energy
(Arm A: stationary supply), or mode energies on an exact
integer ladder (Arm B: exactly periodic supply)? **Targets:**
T_req, the 405 winner's required tensor at 410's sites
A1/A2/A3; T_corr, Phase 420's SEC-corrected tensor at the
same sites. **Bar:** R = max per-site Frobenius residual
≤ 1×10⁻⁹. **Machinery:** the record's mating machinery
(Phases 313/320/410/420) verbatim, spectrum constraint
added; instrument B-2 (Phase 430) for the time reads.
Registration `work/p431_registration.md` (SS0–SS8,
Amendments A1–A2, two incident notes), written before
computation.

## Verdicts

| arm | T_req (405 winner) | T_corr (420) |
|---|---|---|
| A — single energy | **DOES NOT ADMIT** | **ADMITS** |
| B — commensurate ladder | **ADMITS** | **ADMITS** |

**Arm A / T_req — DOES NOT ADMIT (at the registered
scope).** Best residual over N = 6, 8, 12 modes and 30
starts: **1.2732×10⁻³** (N = 8), flat in N (N = 6:
1.3236×10⁻³; N = 12: 1.2754×10⁻³, the confirmed mating),
six orders above the bar, at |a|² = **5.998 — 205× the
unconstrained Fit A's 0.029266** — and the found mating IS
stationary (B-2 registered-E deviation 8.67×10⁻¹⁸ over the
grid; window spots at W/4, W/2, W equal R_F(0) in two
independent evaluable forms, supplement): persistence is
not what fails. Anatomy (SS7; constrained-Jacobian σ_min
5.41×10⁻⁴, full rank — a genuine shallow local minimum,
not a singularity): the residual is carried almost
entirely by the three spatial diagonal components, nearly
isotropically — at the peak site A3, T11/T22/T33 =
7.40/7.34/7.36×10⁻⁴; at A2, ≈ 2.0×10⁻⁴ each; at A1,
≈ 3.2×10⁻⁵ each — while the density T00 is matched to
≤ 4.1×10⁻⁶ and every off-diagonal to ≤ 3.1×10⁻⁷. **The
single-energy supply reproduces T_req's density and fluxes
but not its principal pressures: at one shell energy the
supplied pressure content at a site is locked to the
density through the shell, and T_req's pressure content
sits off that lock, worst at the peak.** Amplitude cannot
buy the missing components — 205× the price changes
nothing.

**Arm B / T_req — ADMITS.** Residual **1.3730×10⁻¹⁶**
(pairwise; direct 1.3388×10⁻¹⁶), seven orders under the
bar, at the FIRST registered size (N = 6, ladder counts
(2,2,2)): base E₀ = 1.019134, rungs exactly (1,1,2,2,3,3)
(ratio deviation 0.0). Price |a|² = **0.013963 — 0.48× the
unconstrained Fit A**: the persistent mating is CHEAPER
than the drifting one. Route-B (Form P) terms: common
period T_c = 6.165222 code units (2.06×10⁻⁸ s);
5.923×10¹⁵ cycles in the 425 window; return error at T_c
+2.55×10⁻¹⁸; cycle-ladder returns 1…1024 ≤ **4.71×10⁻¹⁴**
(verbatim = registered to the printed digits) against
Form P's per-cycle bar 1×10⁻⁶. Printed plainly: the
worst instant over the period departs from the fixed
target by R_F = 0.20791 (at t = 2.1565) — the supply
oscillates through a wide tensor family between exact
returns; that number is the input a geometry-side
worst-instant legality read would consume, not a
supply-certificate term. **The B-2 supply certificate in
Form P terms is issuable in principle for T_req.**

**Arm A / T_corr — ADMITS.** Residual **9.9696×10⁻¹⁵**
(direct 9.9271×10⁻¹⁵) at the first registered size
(composite (6,6)): registered energy E = 2.189896 (spectrum
scatter 4.44×10⁻¹⁶, representation level). Prices per
family: fam1 **0.010003**, fam2 **0.014068**, total
**0.024071 — 0.82× the unconstrained composite's
0.029174** (the split differs from C-A's: family 2 carries
real weight here, 0.014068 vs 2.04×10⁻⁶ in C-A). B-2:
registered-E grid deviation 1.57×10⁻¹⁷ over [0, 2×10⁵];
window spots at W/4, W/2, W equal R_F(0) in both evaluable
forms (supplement) — the mating is stationary across the
full 3.860 yr window by construction. Representation
bound: the verbatim stored momenta (scatter 4.44×10⁻¹⁶)
drift off the construction, crossing the bar at
t* = 3.573×10⁷ code units = **0.119 s** — against the
unconstrained fits' 2.42×10⁻¹⁷ s, a 24-order improvement,
and a representation bound, not the construction's.
**The B-2 supply certificate (428 Route A supply leg) is
issuable in principle for T_corr.**

**Arm B / T_corr — ADMITS.** Residual **1.2311×10⁻¹⁵**
(direct 1.2117×10⁻¹⁵) at (6,6), ladder L = 3 per family:
E₀ = 1.178657, T_c = 5.330801 code units (1.78×10⁻⁸ s);
6.850×10¹⁵ cycles in the window. Prices: fam1 **0.009963**,
fam2 **0.007210**, total **0.017173 — 0.59× the
unconstrained composite**. Cycle-ladder returns ≤
**1.00×10⁻¹³** verbatim (≤ 2.75×10⁻¹⁴ registered) at
2¹⁰ cycles; worst instant over the period R_F = 0.65688
(at t = 2.9974), printed with the same meaning as above.
**Certificate issuable in principle in Form P terms.**

## What this does to the roadblock

Phase 430 measured that both stored supplies drift off
their targets in ~2.42×10⁻¹⁷ s. This phase's answer: the
drift was a property of the unconstrained fits, not of the
targets. Three of the four (constraint, target) pairs admit
a mating at or below machine precision at prices BELOW
the drifting fits — the ladder expresses T_req at
1.4×10⁻¹⁶ for half Fit A's price; the corrected target
admits even the rigid single-energy form. The one refusal
is specific and anatomical: a SINGLE energy cannot express
T_req's principal pressures. Intake disposition (entry
1136): wild attack 1, THE ACTIVE SUPPLY, does not need to
charge on the supply side's account — its premise (no
persistent mating exists) is now false for both standing
targets; it remains the named road only for a future
target that defeats both arms.

**Whether 428's functional can be met:** its supply leg
can — for T_req via Route B / Form P, for T_corr via
Route A or Form P — at the prices above. The functional
as a whole still has no object: its geometry leg requires
a four-condition geometry, which is GAP-3, untouched
here. **Fences:** test-field scope throughout; a
persistent SUPPLY is not a sustained GEOMETRY (428's
functional governs); the targets' own status stands on
the face of every verdict — the 405 winner's geometry
fails SEC (stored SEC_min −2.213557×10⁻⁴, Gate-50 record)
and T_corr is a construction (a corrected target tensor),
not a geometry.

## The rotation-sweep ponder (entry 1136, wild attack 2) — LABELLED SPECULATIVE

*Speculative note; nothing below is a finding.* The
registered by-product (SS6) read the two drifting
supplies' sweeps against the other target: Fit A's sweep
vs T_corr and C-A's sweep vs T_req both minimise at
t = 0, at exactly the inter-target distance
1.6946×10⁻⁴, and move away (excursions to 0.528 /
0.584). Within their characteristic periods, neither
sweep passes near the other stored target — the
two-target form of the ponder is answered negatively by
measurement. The stronger form — whether a drifting
supply's wide sweep (excursions ~250× the targets' norms)
passes through some four-condition-legal tensor a
co-rotating geometry could use — was not read and is not
claimed either way. The ponder stands as a ponder; its
motivation is weaker now that persistence by construction
exists for both targets.

## Controls

- CTL-431-0: Fit A reproduced — diffs 3.48×10⁻¹⁸
  (pairwise) / 0.0 (direct); |a|² = 0.029266406597128584.
- CTL-431-1: C-A reproduced — diffs 0.0 / 0.0; |a|² fam1
  0.029172052178672605 + fam2 2.0362442383995038×10⁻⁶.
- CTL-431-2: laptop ADMITTED (admission object: Fit A
  t = 0 pairwise read; maxR diff 4.18×10⁻¹⁸ ≤ the 1×10⁻¹³
  bar; mirror md5-verified). Fits ran on the VM (shared
  1.5-CPU cell; per-start walls to ~3.5 min under
  contention); the pool carries the priority run.
- CTL-431-3: B-2 self-checks reproduce 430's stored
  control values (stationarity 3.737×10⁻¹⁶; beat return
  1.221×10⁻¹⁵, anti-phase 2.036×10⁻¹⁶; direct/pairwise
  ratios 3.935×10⁻¹⁵ / 1.172×10⁻¹⁴).
- Independent checker (`work/p431_check.py`, opposite-path
  direct residuals, exact spectrum verification, B-2
  headlines): **ALL PASS** on all four matings of record.
- Amendments on the face: A1 (search at the record's
  default-tolerance precedent; best candidate polished at
  1×10⁻¹³, polished point is the candidate of record);
  A2 (search evaluation cap 4000 → 1200 on the record's
  convergence evidence; banked pre-A2 starts stand);
  two incidents (a warm-start padding crash, fixed with
  410's pattern; a silent mid-run death under shared-VM
  memory pressure, resumed from banked JSONL state);
  the window-spot supersession (supplement, above).

## Three goals

- **Goal 1 (FTL drive):** the supply side of sustainment
  is no longer the blocker Phase 430 measured: persistent
  matings exist for both standing targets, at or below the
  drifting fits' prices. Frontier A unchanged — the
  geometry gates (SEC, extent) are untouched by this
  phase, and sustainment's functional (428) still awaits
  a four-condition geometry.
- **Goal 2 (wormhole):** untouched by this phase.
- **Goal 3 (subluminal record):** untouched; Procaccia's
  0.1363 stands in its category.

DESK: NO DATA CONTACT.
