# P253-2 MEMO — THE LOW-SHEAR KINEMATICS SEARCH (Phase 253, Item 2)

**Verdict form fired: SHEAR AND TRANSPORT ARE LOCKED** — no
member of the registered divergence-free family meets the
bar; the trade is priced in §4–§5. The flux cancellation is
NOT the expensive part: the best member keeps the ring,
improves it (Type-I 0.0137 vs Natário's 0.009636, median q
2.87 vs 10.48), and still pays median |ρ| 6.73× Alcubierre's
at equal transport. What is locked is the shear floor
itself: it falls only as the shell widens, and widening is
exactly what the transport band prices.

Registration: `phase253/work/p2532_registration.md` (written
before any deciding computation). Drivers:
`phase253/work/p2532_run.py`, `phase253/work/p2532_analysis.py`.
All verdict-carrying numbers:
`phase253/results/p2532_results.json`. Frame of record:
Phase 166 pin, Gate-19-corrected tensor conventions (lineage;
T_req derived here). Programme venv, float64. Bounded local
run (96 s driver + ~15 s analysis; registered cap ~30 min —
the registered scan completed, so no kernel spec is owed).
SLICING FENCE: v_eff is a t = const effective-arrival read,
NOT a transport theorem.

## The family (registered §1)

Stokes-stream-function shifts ψ = (β/2) r² sin²θ · S_tot(r),
v = β[(S_tot + B)x̂ − B·n_x·n], B = rS_tot′/2 — divergence-free
for ANY S_tot — with S_tot = Σ a_n S_n over five registered
atoms (quintic [10,20] = the Natário control atom; septic
[10,20], the higher-regularity atom; quintic [8,22], wide;
quintic [12,18], narrow; S_{1,1} beta profile [10,20], flat),
dials a on the simplex (Σa = 1, a ≥ 0). Transport band:
|v_eff − v_eff(Alcubierre)|/v_eff ≤ 1% at the same β, the
deviation printed on every member. Primary objective:
median K_ijK^ij over SET-244 at β = 1.1 (see the C1
disclosure below for what K² is and is not); secondary
∫K²dV over the full shell support. Alcubierre enters only
as the transport/price reference control (not a member).

## Controls (run first)

| control | read | result |
|---|---|---|
| C1 Natário member, map reads | E_neg **−22.450425** (rel. diff. vs P250-1 ~10⁻⁷ class, printed 6 dp identical); median q **10.4814** (P250-1: 10.48); Type-I **0.009636** (64 pts, exact); v_eff rel. diff. 0.0 | **PASS** |
| C1 identity sub-check (as registered: ρ = −K²/16π pointwise, bar 10⁻⁶) | max rel. diff. **1.37** | **FAIL — diagnosed, see Disclosure** |
| C1 identity, lapse-corrected (post-analysis) | ρ = −K_ijK^ij/(16π α²), α = √(1+\|v\|²) ∈ [1.000, 1.540] on SET-244: max rel. resid. **1.8×10⁻¹²**, median 1.6×10⁻¹⁵; corrected median K²/16π = 6.3716×10⁻⁴ = median \|ρ\| exactly | **PASS (corrected form)** |
| C2 divergence, every scan member | max \|∇·v\| over all 26 members = **7.3×10⁻¹⁶** (bar 10⁻¹⁰) | **PASS** |
| C3 flat limits, best member | max \|T_req\| interior (r < 8) / exterior (r > 22) = 0.0; β = 0: 0.0 (bar 10⁻¹²) | **PASS** |
| C4 Alcubierre reference | E_neg **−2.590291** (rel. diff. vs −2.5902913736 ~10⁻⁷ class); median q 37.19; v_eff exact | **PASS** |

Control agreement statement: both P250-1 maps are reproduced
on this machinery at the record's precision (budgets and
v_eff identical at printed precision, median q and Type-I
counts exact). The one failure is inside C1's auxiliary
identity, not in any map read; it is disclosed in full below
and it does not touch the verdict, which is read off full
maps, not off the scan objective.

## The scan — 26 members, β = 1.1 (registered budget: ≤ 30)

Objective = median K² on SET-244 (raw symmetrised-gradient
form; see Disclosure). All 26 members are transport-
admissible; v_eff deviation is the price column.

| member (a₁ quintic, a₂ septic, a₃ wide, a₄ narrow, a₅ β₁₁) | median K² | v_eff dev |
|---|---|---|
| (0,0,0,0,1) pure flat β₁₁ | 0.03368 | +0.41% |
| (0,.25,0,0,.75) | 0.03850 | +0.25% |
| (0,.5,0,0,.5) | 0.04471 | +0.09% |
| (0,.75,0,0,.25) | 0.04922 | +0.08% |
| (0,1,0,0,0) pure septic | 0.06078 | +0.26% |
| (.25,0,0,0,.75) | 0.03698 | +0.31% |
| (.25,.25,0,0,.5) | 0.04313 | +0.15% |
| (.25,.5,0,0,.25) | 0.04736 | +0.02% |
| (.25,.75,0,0,0) | 0.05686 | +0.19% |
| (.5,0,0,0,.5) | 0.04058 | +0.21% |
| (.5,.25,0,0,.25) | 0.04571 | +0.05% |
| (.5,.5,0,0,0) | 0.05213 | +0.13% |
| (.75,0,0,0,.25) | 0.04356 | +0.11% |
| (.75,.25,0,0,0) | 0.04948 | +0.06% |
| (1,0,0,0,0) Natário control | 0.04772 | 0.00% |
| (0,0,.25,0,.75) | 0.03068 | +0.53% |
| (0,0,.5,0,.5) | 0.02769 | +0.65% |
| (0,0,.75,0,.25) | 0.02436 | +0.76% |
| **(0,0,1,0,0) pure wide [8,22]** | **0.02054** | **+0.88%** |
| (0,0,0,.25,.75) | 0.03942 | +0.14% |
| (0,0,0,.5,.5) | 0.04088 | +0.17% |
| (0,0,0,1,0) pure narrow [12,18] | 0.07387 | +0.86% |
| (.125,0,.875,0,0) polish | 0.02273 | +0.77% |
| (0,.125,.875,0,0) polish | 0.02233 | +0.75% |
| (0,0,.875,.125,0) polish | 0.02151 | +0.70% |
| (0,0,.875,0,.125) polish | 0.02248 | +0.82% |

Reading: same-width shape dials buy at most 1.42× (pure flat
β₁₁, 0.0337 vs Natário 0.0477) — the septic atom, registered
against the outer-joint S″/S‴ swing, is WORSE than the quintic
everywhere on the simplex (its peak gradient is higher; joint
regularity was never the shear driver). The narrow atom is
worst of all, as registered. The only dial that moves the
objective materially is WIDTH, and it moves v_eff with it,
monotonically: the admissible floor sits at the band edge.

## The best member — pure wide atom, S = quintic on [8, 22]

Full Phase 235-format map (SET-244 reads; continuum
quadrature over its full shell support [8, 22] for budgets —
the controls' budgets are over [10, 20], their own support).
DEC carries the D2 † caveat (sampled normalised ≈−1 form at
non-Type-I points, not a stress-unit deficit).

### β = 1.1 (primary)

| quantity | Alcubierre (control) | Natário (control) | Best member (wide) |
|---|---|---|---|
| Type-I fraction | 0.000000 (0) | 0.009636 (64) | **0.013701 (91)** |
| median q (defined) | 37.19 | 10.48 | **2.87** |
| max q (defined) | 2.94×10⁶ | 2.77×10³ | 1.96×10⁴ |
| q > 1 share (defined) | 1.0000 | 0.9426 | **0.8205** |
| denominator ≤ 0 share | 0.6640 | 0.8294 | 0.9220 |
| ρ_euler min / median / max | −3.387×10⁻⁴ / −4.463×10⁻⁵ / −1.1×10⁻¹¹ | −2.556×10⁻³ / −6.372×10⁻⁴ / −8.2×10⁻⁸ | −7.349×10⁻⁴ / **−3.003×10⁻⁴** / −9.7×10⁻⁸ |
| NEC min / median | −0.003783 / −0.001588 | −0.023092 / −0.009573 | −0.007236 / −0.003944 |
| WEC min / median | −0.036201 / −0.015516 | −0.225112 / −0.092444 | −0.069423 / −0.038024 |
| DEC min / median † | −1.000052 / −1.000009 | −1.001389 / −1.000324 | −1.000231 / −1.000049 |
| SEC min / median | −0.037467 / −0.015399 | −0.224828 / −0.093449 | −0.071292 / −0.038418 |
| violating point share NEC / WEC / DEC | 1.0 / 1.0 / 1.0 | 0.9904 / 1.0 / 1.0 | 0.9858 / 1.0 / 1.0 |
| clause vol. share (quad.) NEC / WEC / DEC | 0.9931 / 0.9931 / 0.9931 | 0.9856 / 0.9931 / 0.9931 | 0.9850 / 0.9929 / 0.9929 |
| **E_neg budget** | **−2.590291** | **−22.450425** | **−11.368744** |
| QI price R_diff (τ = 10) | 2852.3 | 21522.7 | 6189.3 |
| QI price R_diff (τ = 1) | 0.2852 | 2.1523 | 0.6189 |
| ∫K²dV (secondary, raw form) | — | 1510.7 | 696.9 |
| v_eff | 1.4736627426242535 | 1.4736627426242535 | 1.4865634044441078 (**+0.875%**, in band) |
| deepest sites | r ≈ 12.80, inner-mid, ⊥ X | r = 19.878, outer edge | r = 10.37, inner shell (SET-244's inner nodes, where the wide profile's gradient is already up) |

### β = 1.5 (transfer check, same dials)

| quantity | Alcubierre (P250-1 record) | Natário (P250-1 record) | Best member (wide) |
|---|---|---|---|
| Type-I fraction | 0.002108 | 0.011292 | **0.020325 (135)** |
| median q | 32.25 | 16.29 | **3.00** |
| q > 1 share | 1.0000 | 0.9300 | **0.7275** |
| denominator ≤ 0 share | 0.6777 | 0.8366 | 0.9249 |
| ρ_euler median | −6.794×10⁻⁵ | −9.093×10⁻⁴ | −4.601×10⁻⁴ |
| **E_neg** | −4.216329 | −35.453719 | −18.689962 |
| QI R_diff (τ = 10) | 4677.0 | 39762.0 | 11382.8 |
| v_eff | 1.5890183845769814 | 1.5890183845769814 | 1.6116244601634486 (**+1.42% — OUTSIDE the 1% band at β = 1.5**; the dials were selected at β = 1.1, disclosed as a transfer limit) |

Quadrature twins (best member): E_neg twin rel. diffs
3.3×10⁻⁵ (β = 1.1), 3.7×10⁻⁵ (β = 1.5), bar 2×10⁻³.

## Ring analysis — the cancellation survives, widened

Best member, β = 1.1: all 93 q ≤ 1 points and 91 of 91
Type-I points sit on TWO adjacent radial nodes,
r = 13.293 (45) and r = 13.537 (48 q ≤ 1 / 46 Type-I) —
the registered ring test (≥ 80% on ≤ 2 adjacent nodes)
passes, and the ring is broader than Natário's single node
(65 q ≤ 1, all at 13.293). On the equatorial ⊥ X ray the
|flux| dip sits at r = 13.25 with |flux| = 1.77×10⁻⁴ —
an order deeper than Natário's ray dip (1.39×10⁻³ at
r = 13.0, P250-1). Ring-concentrated Type-I share of the
shell: the full Type-I population (0.013701 of SET-244) is
on the ring. **The cancellation structure is retained and
strengthened by the very member that minimises shear** —
cancellation and shear are separable in that direction.
What does not separate is the shear floor from transport.

## Verdict evaluation (registered §6, β = 1.1)

| bar component | read | fires? |
|---|---|---|
| median \|ρ\| within 2× of Alcubierre's | best 3.003×10⁻⁴ vs Alcubierre 4.463×10⁻⁵ = **6.73×** (bar: ≤ 8.93×10⁻⁵) | **NO** |
| ring retained, Type-I ≥ 0.009636 class, ring-concentrated | Type-I 0.013701, ring test pass | YES |
| v_eff in band | +0.875% | YES |

Two of three components pass and the shear component fails
by 3.4× against its own bar — so SHEAR IS A DIAL does not
fire. All 26 scanned members are transport-admissible, so
FAMILY CANNOT HOLD TRANSPORT does not fire. Exactly the
remaining form fires: **SHEAR AND TRANSPORT ARE LOCKED**.

## The price of the lock (registered deliverable of this form)

**Shear floor as a function of v_eff across the scanned
family** (median K² on SET-244; full-map anchors marked):

| v_eff deviation | floor member | median K² | full-map median \|ρ\| |
|---|---|---|---|
| 0.00% (exact) | Natário (1,0,0,0,0) | 0.04772 | 6.372×10⁻⁴ (14.3× Alc.) |
| +0.41% | pure flat β₁₁ | 0.03368 | — (scan only) |
| +0.65% | (0,0,.5,0,.5) | 0.02769 | — |
| +0.88% (band edge) | pure wide [8,22] | 0.02054 | 3.003×10⁻⁴ (6.73× Alc.) |

The floor falls ~2.3× across the band and is still 6.73×
Alcubierre's median |ρ| AT the band edge; the bar (2×)
would need roughly another 3.4× of shear reduction, which
on the observed width-scaling (K² ∝ 1/width² at fixed shape)
means a shell ~1.8× wider again — a v_eff deviation far
outside the registered band. Inside the family, there is no
admissible point near the bar.

**Mechanism — which components of K carry both.** Mean
shares of K² over SET-244 (post-analysis decomposition):

| component group | Alcubierre | Natário | Best (wide) |
|---|---|---|---|
| K_xx (longitudinal) | (only non-zero row: K_xx, K_xy, K_xz all ∝ S′) | 0.235 | 0.241 |
| K_xy, K_xz (transverse shear) | — | 0.553 | 0.561 |
| K_yy, K_zz, K_yz (transverse block) | — | 0.213 | 0.198 |

For a divergence-free shift the transverse components are
not a choice: the stream function ties them to B(r) =
rS′/2, i.e. transverse gradients of order S′/2 exist
wherever S′ ≠ 0, and ∇·v = 0 forces ∂_y v_y + ∂_z v_z =
−∂_x v_x pointwise. ~76% of the family's K² is transverse
(shear + transverse block) in both the Natário member and
the best member — widening dilutes all components together
and does not change the mix. Meanwhile the on-axis
transport is carried by the SAME S′: v_eff is a functional
of the on-axis profile S_tot whose total drop (1 → 0 across
the shell) and shape set both the arrival-time read and,
through B = rS′/2, the transverse shear norm. The only
in-family dilution of |S′| is shell width, and width is
precisely what v_eff measures. That is the lock, stated at
the component level: **transport fixes the profile whose
derivative IS the shear; the divergence-free condition
spreads that derivative into transverse components carrying
~3/4 of K², and no radial dial removes them.**

## Disclosure

- **C1 identity failure (on the face).** The registration
  asserted ρ = −K_ijK^ij/(16π) with K the raw symmetrised
  gradient. That is wrong for this metric form: g_tt = −1
  with g_ti = −v_i gives ADM lapse α = √(1 + |v|²) ≠ 1, and
  the correct identity is ρ = −K_ijK^ij/(16πα²) — verified
  post-hoc to 1.8×10⁻¹² (max rel. resid. on SET-244).
  Consequences: (i) the scan objective is the RAW K², a
  shear proxy that overstates |ρ| by the α² factor (median
  9.49×10⁻⁴ proxy vs 6.37×10⁻⁴ true for Natário); (ii) the
  JSON's `controls_pass` is False for this sub-check alone —
  every map read in C1/C4 passes at record precision;
  (iii) the verdict does not rest on the proxy: it is read
  off the best member's FULL map (median |ρ| 3.003×10⁻⁴),
  and the proxy's ranking (wide < flat < quintic < septic <
  narrow) is corroborated by the two full maps computed
  (Natário vs wide). No bar, verdict form, or family member
  changed after registration.
- SET-244 samples r ∈ [10, 20]; the wide member's shell is
  [8, 22]. Its SET reads (incl. the verdict's median |ρ|)
  are on the registered set, as registered; its budgets are
  integrated over the full [8, 22] support and are therefore
  not shell-identical to the controls' [10, 20] budgets —
  the comparison direction is conservative for E_neg (a
  wider integration domain can only add negative mass, and
  the member still halves Natário's budget).
- β = 1.5 transfer: the best dials leave the 1% v_eff band
  at β = 1.5 (+1.42%). The β = 1.5 map is a transfer read,
  not an admissible member at that β; the verdict is
  registered at β = 1.1 and does not use it.
- Denominator ≤ 0 share moves the WRONG way for the wide
  member (0.9220 vs Natário 0.8294): widening spreads the
  NEC-negative region over more of the SET-244 shell even
  as it shallows every margin. Reported, not hidden: the
  lock is on the shear/transport pair, and this share is
  one more quantity the width dial does not buy.
- Grouped EoM (Phase 158): NOT APPLICABLE to a derived
  stress, per the D2 disposition; no number forced.

## Verdict

**SHEAR AND TRANSPORT ARE LOCKED** — across the registered
26-member divergence-free family, the best transport-
admissible member (pure quintic shell widened to [8, 22],
v_eff +0.875% in band) retains and strengthens Natário's
flux-cancellation ring (Type-I 0.013701 vs 0.009636, median
q 2.87 vs 10.48, ring broadened to r = 13.293–13.537, flux
dip 1.77×10⁻⁴) and halves the budget (E_neg −11.368744 vs
−22.450425), yet its median |ρ| is 3.003×10⁻⁴ — 6.73×
Alcubierre's 4.463×10⁻⁵, against a 2× bar. The shear floor
falls only along the width dial (median K² 0.0477 → 0.0205
as v_eff deviation runs 0.00% → +0.88%), because the
transverse components that carry ~76% of K² are forced by
the divergence-free condition from the same S′ whose
on-axis profile carries the transport. Cancellation is a
dial; shear, at fixed transport, is not — within this
family, this factory, this slicing.

Nothing was appended to NEW_PHYSICS_LEDGER.md; nothing
external was launched; writes are inside phase253/ only,
p2532 files only.
