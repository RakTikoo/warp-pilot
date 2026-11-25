# P122-2 — THE PHASE-90 TRANSIT RE-AUDIT (Phase 122, conditional item)

Worker W-2. Registration: `phase122/CHECKPOINT122.md` §P122-2.
Conditional FIRED: P122-1 verdict **RE-MATCH CLOSES** (checker
57/57 PASS, coordinator-verified). Implementation fixed in
`work/p1222_runrecord.md` before any deciding number.
**(V-b) UNDECIDED: Pais–Uhlenbeck spin-2 ghost vs Mannheim PT-symmetric quantisation — opposed literature positions, B3 NOT COMPUTABLE (Phase 32).**
INTERNAL only. Every transit number below is EFFECTIVE transit
accounting (C12): local light speed is never beaten anywhere, by
any route. Formation PRE-EXISTING ONLY. This is NOT
"a traversable wormhole": the traversal/formation/(V-b) clauses
are not all answered — formation stands PRE-EXISTING ONLY and
(V-b) stands UNDECIDED (verbatim above).

## VERDICT — **MILESTONE EARNED**

Clauses (i)–(iv) complete, artefact tests T1–T4 passed, and the
constructed accounting shows a gain at every registered row:
**a measured shortcut in the constructed two-mouth
configuration** — with the scope sentence attached in the same
breath: perturbative through the entering orders of modes
ℓ ≤ 3; D/r_Σ ∈ {10, 30, 100}; pre-existing configuration;
(V-b) UNDECIDED.

## 1. REPLACEMENT SCOPE (registered, clause by clause)

- **(a) Ambient exterior → constructed exterior.** The handle
  model's "two mouths embedded in one ambient exterior" is
  replaced by P122-1's constructed linearised two-centre Bach
  exterior (about centre A, mirrored to B), valid at
  D/r_Σ ∈ {10, 30, 100} at the re-match's orders (entering
  orders of modes ℓ ≤ 3, full condition set, round Σ).
- **(b) Unit-lapse ambient accounting → constructed-metric
  accounting.** The exterior route is scored IN THE
  CONSTRUCTED METRIC: its own lapse/redshift along the route
  (the constructed A_ax(r) on the inter-centre axis), its own
  proper length L_ext, computed at the construction's order
  (linearised in B's field amplitude; cross-terms
  (B amplitude)×(A's deviation from flatness) bounded ≤ 5×10⁻³
  relative per P122-1). **The O(ε²) remainder is named
  uncomputed wherever a number depends on it** — every route
  number in §3 carries that label.
- **(c) D and the route.** D is the construction's
  centre-separation parameter (D ∈ {10000, 30000, 100000} r₀).
  The route is the inter-centre axis path in the constructed
  exterior from Σ_A to Σ_B (registered default); its proper
  length is COMPUTED in the constructed metric, not set equal
  to D (L_ext/D = 0.775 / 0.755 / 0.463 at the three rows —
  the constructed metric's MK −kr² growth shortens the far
  route's proper length well below the coordinate span).
- **Unsupported, NOT reported:** the handle-model grid beyond
  the perturbative domain (D/r₀ to 10¹²) and the kpc anchors
  are named unsupported and left unquoted. Handle-model
  numbers are restated alongside ONLY at comparable rows
  (§3), the difference named.

Constructed axis metric (run record §1): A_ax(r;D) =
f_MK(r) − C/(D−r) − 3βγ, Bm_ax(r;D) = 1/f_MK(r) + C/(D−r),
C = 4.285222, on 1000 ≤ r ≤ D−1000. Route functions:
L_ext = ∫√Bm_ax dr; E_ext = ∫√(Bm_ax/A_ax) dr (null coordinate
time; S2 coordinate-time kernel).

## 2. Clauses (i), (ii), (iv)

**(i) BOTH SHELLS LEGAL — cited from P122-1, not re-derived.**
P122-1's shell-sign read on the solved configuration:
Ŝ⁰⁰/α₀ minimum **+0.0202914453 at BOTH mouths** at every
ε ∈ {0.1, 1/30, 0.01}; minus the ℓ ≥ 4 tail bound the minimum
is +0.02028870 > 0. That read is this audit's clause (i).

**(ii) INTERIOR LEGALITY INHERITED.** Gate-9 stands; the
interiors are the same solutions. Stated, not re-run.

**(iv) SECOND PATH — complete before any gain was quoted.**
L₁, T₁ re-verified in-item: float64 primary L₁ =
1005.3728512079 r₀, T₁ = 794.1997332925 r₀ (at the
full-precision a = 0.27773424114865775); 40-digit mpmath
second path agrees to 3.4×10⁻¹⁶ (L₁) and 0.0 (T₁) relative —
bar ≤ 10⁻⁹ met. Against the P86-1 stored controls
(1005.3728512079 / 794.1998958168, computed at the rounded
a = 0.277734): L₁ identical; T₁ differs by 2.05×10⁻⁷
relative, exactly P86-1's registered a-sensitivity — no
deciding read moves. Route integrals: 40-digit mpmath
quadrature vs the primary integrator agrees to ≤ 2×10⁻¹⁶
relative on L_ext and E_ext at every row (bar 5%). Σ join
data: P122-1's second path (collocation-route residuals
≤ 5.6×10⁻¹⁰; GL source within 5% on all deciding
coefficients) — cited per the registration.

## 3. Clause (iii) — the through-trip re-read as a configuration

Through-leg (interior, exactly P86-1): S1 t_thru = 2T₁ =
1588.399 r₀; S2 τ_thru = 2L₁/(γβ_tr), t_thru = 2T₁/β_tr,
β_tr ∈ {0.1, 0.5, 0.9} (gains are β-independent, as in P86-1).
Exterior leg per replacement scope (b). All route numbers at
the construction's linearised order; O(ε²) remainder
uncomputed.

| D/r_Σ | D (r₀) | L_ext (r₀) | E_ext (r₀) | G_τ = L_ext/2L₁ | G_t = E_ext/2T₁ | u_eff (S1) |
|---|---|---|---|---|---|---|
| 10 | 10000 | 7752.485 | 7516.411 | **3.856** | **4.732** | 6.296 |
| 30 | 30000 | 22647.977 | 18797.506 | **11.263** | **11.834** | 18.887 |
| 100 | 100000 | 46264.037 | 27499.777 | **23.008** | **17.313** | 62.956 |

u_eff > 1, where found, is a statement about the
configuration's geometry, never about local motion.

**Thresholds RE-DERIVED in both accountings** (root-finding,
brentq, on the constructed route functions; residuals
< 10⁻⁶ r₀): **D*_τ = 4016.023 r₀** (proper accounting,
L_ext(D) = 2L₁) and **D*_t = 3592.719 r₀** (coordinate
accounting, E_ext(D) = 2T₁). **Domain validity (registered
subtlety, stated):** both roots lie BELOW the construction
domain D ≥ 10⁴ r₀; they are the constructed accounting's own
formal break-even statement computed from its route
functions, NOT construction-domain reads. The gain table
above is quoted at the registered rows {10, 30, 100} only,
where the gains are decided. **Handle-model numbers restated
at the comparable rows, difference named:** the handle model
set L_ext = E_ext = D identically (proper length D at unit
lapse), giving D*_τ = 2010.746 r₀, D*_t = 1588.400 r₀ and
gains G_τ = D/2L₁, G_t = D/2T₁ (at D = 10000: 4.973 / 6.296).
The constructed accounting's route functions differ — its
own lapse (dominated far out by the MK −kr² term in A_ax)
and its own proper length (L_ext < D − 2000 at every row) —
moving both break-evens UP (4016.023 / 3592.719 r₀) and
reducing the gains at every comparable row (at D = 10000:
3.856 / 4.732 vs the handle model's 4.973 / 6.296). The
accounting-dependent band persists in the constructed
accounting, now 3592.72 < D/r₀ < 4016.02 (formal
break-evens); it is not counted as a shortcut — the verdict
rests on the registered rows, where both accountings gain.

**Artefact tests (constructed setting):**
- **T1 like-for-like — PASS.** Gains exist proper-to-proper
  (G_τ > 1) AND coordinate-to-coordinate (G_t > 1) at every
  registered row, in the constructed metric.
- **T2 redshift honesty — PASS, difference stated.** The
  exterior's own lapse is included in E_ext. The flat-lapse
  variant (A_ax → 1) gives E_flat = L_ext identically:
  +3.14% (D = 10⁴), +20.48% (3×10⁴), +68.23% (10⁵) above the
  honest E_ext — the flat-lapse variant OVERSTATES the
  exterior coordinate time (and hence the gain); the honest
  constructed accounting's gain is the smaller one and it
  still exceeds 1 at every row. The shortcut is not a
  flat-lapse artefact. (Through-leg: P86-1's T2 stands —
  the honest e^{−Φ} weight, not the flat variant, is used.)
- **T3 endpoint identification — STATUS CHANGED, supplied
  by the construction.** In P86-1 the endpoints were the two
  mouth surfaces of one throat identified under the handle
  embedding (an assumption). Here the endpoints are Σ_A and
  Σ_B of the POSED two-mouth configuration itself; the
  identification is supplied by P122-1's construction, not
  assumed.
- **T4 local causality — PASS.** A_ax > 0 (min 0.99753 /
  0.99786 / 0.99796 at the three rows) and Bm_ax > 0 along
  the whole route; every profile is everywhere timelike/null
  and locally subluminal in BOTH the interior (P86-1) and the
  constructed exterior (S1 null; S2 local β_tr ∈
  {0.1, 0.5, 0.9} < 1 by construction). u_eff > 1, where
  found, is a statement about the configuration's geometry,
  never about local motion.

**Folded read — TRAVELLER'S EC READS.** Interior: P86-2's
audit stands (cited, not re-run): no EC refusal point on the
interior trajectory, per-profile tidal envelope as stored.
Exterior legs (new, at the construction's order): the
constructed exterior is Bach-flat vacuum at that order
(traveller-frame EC content T = 4α_g·B = 0 at the
construction's order; the O(ε²) remainder is named
uncomputed). Tidal components along the exterior route in
the constructed metric (sympy-derived orthonormal Riemann
of the axis metric), read against the Phase-23 bar
(4.905 s⁻² across 2 m) at r₀ = r₀* = 4.785×10⁷ m: maxima
over each route — |K_r| ≤ 1.13×10⁻⁸ r₀⁻² (≤ 4.5×10⁻⁷ s⁻²);
boosted transverse |K_⊥| at β_tr = 0.9 ≤ 5.35×10⁻⁸ r₀⁻²
(≤ 2.1×10⁻⁶ s⁻²) — **at least six orders of magnitude below
the bar at every registered row and profile. NO REFUSAL
POINT on the exterior legs.**

**Folded read — SHELL CROSSING.** P90-2's datum-labelled
verdict stands, re-stated with its datum label: under the
Phase-88 Poisson–Visser datum family on u ∈ [−1/2, 1]
(traceless point u = −1/2 at the interval's boundary), the
crossing is clean on every profile and the distributional
tidal kick is identically zero — a statement about the
datum-carrying shell, NOT about the P61-1 configuration as
registered in BDE. What the construction itself fixes, at
its size: the crossing surface is the round Σ of the posed
configuration, and on the solved configuration the
[R̃_,n] mode residuals are ≤ 10⁻¹² per unit ε^entering with
the angular Darmois pair closed on the round Σ (P122-1) —
the posed configuration carries no additional crossing
datum beyond P90-2's labelled read at that size.

**Folded read — MOVING-MOUTH COMPOSITION.** P86-3 Part A
stands (cited): the local join survives a boost identically;
the global pose failure it named is exactly what P122-1 has
now supplied at the registered orders. For Part B: the
conditional time-shift (t_arr,S = γ_m·Δ_id + γ_m²·v·D,
Δ_id = 2T₁/β_tr; approaching-orientation precedence iff
γ_mβ_mD > 2T₁/β_tr, thresholds 3056.88 r₀ to 158043.78 r₀
over the P86-3 grid on the verified 2T₁) is now a property
of a **POSED configuration at the registered orders**, not
of an identification the configuration does not supply.
Any time-shift number here is a MEASURED TIME-SHIFT with
chronology protection OPEN. The chronology-protection
question is **RE-REGISTERED as the head follow-up** of this
phase's queue (Phase 90 queue item 3's trigger, now fired);
it is NOT decided here, NOT computed as a CTC, and NOT
claimed.

## 4. Scope

Every number carries the construction's domain and order:
perturbative through the entering orders of modes ℓ ≤ 3;
D/r_Σ ∈ {10, 30, 100}; linearised in B's amplitude with the
O(ε²) remainder named uncomputed; nothing extrapolated to
D ≈ 2r_Σ or to the handle-model grid. The configuration is
pre-existing (formation PRE-EXISTING ONLY). **(V-b) UNDECIDED: Pais–Uhlenbeck spin-2 ghost vs Mannheim PT-symmetric quantisation — opposed literature positions, B3 NOT COMPUTABLE (Phase 32).**

## 5. Files

`results/p1222_results.json` (deciding record incl. tidal
table), `results/p1222_checker.json` (39/39 PASS) from
`work/p1222_checker.py`; engines `work/p1222_main.py`,
`work/p1222_tidal.py`; implementation `work/p1222_runrecord.md`.
