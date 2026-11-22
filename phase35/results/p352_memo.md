# P35-2 — THE |κ| WINDOW FOR THE MIXTURE ROW — Memo

Worker P35-2. Script: `phase35/p352_kappa_window.py`; results:
`phase35/results/p352_results.json`; run record:
`phase35/results/p352_run_record.md`. float64 throughout.
**Level of every mixture number below: q-curvature / PROFILE
level.** P35-1's Step B reconstruction had NOT landed at run time
(`phase35/results/` contained no P35-1 output), so no reconstructed
metric is used; the coefficient is built from the P33-3 profile
construction plus Shaikh's throat flare relation, exactly as the
item's fallback registers. Reconstruction-level status is a
follow-up (below), not silently assumed.

## GATE — PASSED (≤1.5×10⁻⁷, bar ≤1%)

**Tidal-bar definition (Phase 23, restated from
`phase23/p233_ledger.py`):** traveller-frame tidal gradient
≤ **4.905 s⁻²** (1 g across a 2 m traveller) at **v = 0.1 c**,
gradient = c²·Cmax/|κ|, where Cmax is the max |tidal coefficient|
(radial vs γ²v²-boosted transverse) at the throat, in units of
1/|κ|; the scaling family keeps **x = r₀²/|κ| = 0.5**, so
|κ|\* = c²·Cmax/4.905 and r₀\* = √(0.5·|κ|\*).

Recomputed from the Phase-23 fluid coefficient Cmax = +1
(radial R_tltl = +1 per |κ|): **|κ|\* = 1.8323×10¹⁶ m²**
(stored 1.832324×10¹⁶; rel. err 1.5×10⁻⁷), **r₀\* = 9.5716×10⁷ m**
(stored 9.571636×10⁷; rel. err 7.3×10⁻⁸), gradient at 1 m
4.49378×10¹⁶ s⁻² (stored 4.493775×10¹⁶). Sign check (P13-3):
C_rad = −(f′(r₀)/2)·Φ_r(r₀) with f′(r₀) = 2(1−x)/r₀ = 1.41421 and
Phase 23's Φ_r(r₀) = −√2 gives **+1.000** — the fluid value. ✓

## COMPUTATION 1 — mixture tidal coefficient (profile level)

For a Morris–Thorne metric at the throat (F = 1−b/r = 0):
radial coefficient **C_rad = −(F′(r₀)/2)·Φ′(r₀)**,
transverse boosted coefficient = −γ²v²·F′(r₀)/(2r₀) = **−0.010101**
per |κ| (same for every row, since F′(r₀) = 2(1−x)/r₀ is
throat-algebra in x only). The mixture's Φ′(r₀) is the P33-3
profile redshift, solved there from fluid-2 conservation:
Φ′(r₀) = [w/(1+w)]·2(2−f)/r₀ — verified in-run against all 28
stored P33-3 rows (max abs err 4.4×10⁻¹⁶). Hence, closed form
(|κ| = 1 units):

**C_rad(f, w) = −2w(2−f)/(1+w)**,  Cmax = max(|C_rad|, 0.010101).

**Registered expectation — TESTED, REFUTED in its strict form.**
The coefficient is *not* a function of the throat-algebra quantity
|κ|p_t,tot(r₀) = f(1−f+w) alone (signed κp_t,tot = −f(1−f+w);
the checkpoint's unsigned form is |κ|p_t,tot). Counterexample pair
at identical |κ|p_t,tot = 0.9375: (f, w) = (0.75, 1) gives
C_rad = −1.250, while (0.9, 0.9417) gives C_rad = −1.067. The
coefficient is throat-*local* but needs (f, w) separately, through
Φ′(r₀) — i.e. through fluid 2's conservation, not through the
totals' algebra alone. (The f = 0 gate column is discontinuous:
at f = 0 fluid 2 is absent, P33's Φ is undefined, and the column
reverts to Phase 23's own Φ_r = −√2, C = +1 for every w.)

Grid (PASS rows f ≥ 1/2; full table in the JSON):

| f | w | C_rad | Cmax | \|κ\|\* (m²) | r₀\* (m) | \|κ\|\*/10⁸ | orders |
|---|---|---|---|---|---|---|---|
| 0.5 | 0 | 0 | 0.0101 (transv.) | 1.85×10¹⁴ | 9.62×10⁶ | 1.85×10⁶ | 6.27 |
| 0.5 | 1/3 | −0.750 | 0.750 | 1.37×10¹⁶ | 8.29×10⁷ | 1.37×10⁸ | 8.14 |
| 0.5 | 1/2 | −1.000 | 1.000 | 1.83×10¹⁶ | 9.57×10⁷ | 1.83×10⁸ | 8.26 |
| 0.5 | 1 | −1.500 | 1.500 | 2.75×10¹⁶ | 1.17×10⁸ | 2.75×10⁸ | 8.44 |
| 0.6 | 1/3 | −0.700 | 0.700 | 1.28×10¹⁶ | 8.01×10⁷ | 1.28×10⁸ | 8.11 |
| 0.6 | 1 | −1.400 | 1.400 | 2.57×10¹⁶ | 1.13×10⁸ | 2.57×10⁸ | 8.41 |
| 0.75 | 1/3 | −0.625 | 0.625 | 1.15×10¹⁶ | 7.57×10⁷ | 1.15×10⁸ | 8.06 |
| 0.75 | 1 | −1.250 | 1.250 | 2.29×10¹⁶ | 1.07×10⁸ | 2.29×10⁸ | 8.36 |
| 0.9 | 1/3 | −0.550 | 0.550 | 1.01×10¹⁶ | 7.10×10⁷ | 1.01×10⁸ | 8.00 |
| 0.9 | 1 | −1.100 | 1.100 | 2.02×10¹⁶ | 1.00×10⁸ | 2.02×10⁸ | 8.30 |

(w = 1/2 rows lie between the 1/3 and 1 rows; w = 0 rows are all
the transverse-floor row, |κ|\* = 1.85×10¹⁴ m².) **x check:
x = r₀\*²/|κ|\* = 0.5 < 1 for every row** — the genuine regime is
preserved along the whole scaling family, as in Phase 23.
**Every PASS row has |κ|\*/10⁸ ≥ 1.85×10⁶ ≥ 10⁶.**

## COMPUTATION 2 — bound audit (primary sources fetched in-run)

Phase 3's source for |κ| ≲ 10⁸ m² is the Buchdahl-in-EiBI paper,
Feng, Geng & Luo, arXiv:1810.06753 (its abstract is quoted in
`phase3/results/p32_modgrav.json`). Read in full in-run:

- **(i) Sign branch — the 10⁸ figure does NOT constrain κ < 0 as
  published.** The paper states (Sec. IIA, on its modified TOV
  equation): "both κ > 0 and κ < 0 are allowed… However, for
  κ < 0, when some generic first-order phase transitions are
  present… ρ cannot be monotonically non-increasing… **we will
  only focus on the case of κ > 0 in this study**." Its theorem
  additionally assumes the κ-energy condition ab ≥ 1. The wormhole
  branch is κ < 0, so the carried bound is a κ > 0 result carried
  over a branch it explicitly excluded.
- **(ii) Assumptions / conditionality.** Static, spherically
  symmetric, *isotropic perfect-fluid* stars; ρ̃ and ρ_eff finite
  and monotonically non-increasing (extra assumptions beyond GR's
  Buchdahl proof, EoS-restricting); observable = mass/radius of
  the most compact star via r_s/2ℳ ≥ 9/8 + (3π/8)κ(ρ̄−p̄). The
  number itself is **future-conditional**: typical NS values give
  κ ≲ 10⁹ m² in the paper's own conclusions; 10⁸ requires a
  ~3 M⊙ NS "observed in the future" (abstract). No such star is
  an observed datum in the paper. **Mixture interaction — the
  registered expectation is CONFIRMED as a finding:** κ is a
  constant of the theory, shared by stars and throats; the
  mixture's (f, w) signature lives inside one throat's matter
  profile and cannot change what a star measures. No assumption
  of the bound interacts with (f, w).
- **Sign-blind alternative in the same literature:** Avelino's
  existence-of-neutron-stars / fundamental-length argument
  (l_f = √|κ|, PRD 85 (2012) 104053; quoted by Sham et al. as
  |8πκρ₀| ≲ 0.1) bounds **|κ|** — both signs — at the same
  10⁸ m² order. So a κ < 0 bound of this order exists in the
  literature, but it is *not* the Feng/Buchdahl figure Phase 3
  carried.
- **(iii) Decomposition of the fluid's 8.26 orders:**
  (a) row coefficient — κ\* ∝ Cmax exactly; the mixture moves it
  by log₁₀Cmax ∈ [−2.00, +0.18] orders (at most ~2 orders down,
  on the w = 0 transverse-floor rows; it *adds* up to 0.18 on
  w = 1 rows). (b) bound branch/conditional status — **0 orders
  of magnitude, all of the applicability**: the carried figure is
  wrong-branch and future-conditional; the sign-blind replacement
  is the same order. (c) the rest — **the r₀\* ∝ √|κ\*| scaling
  itself** (gradient ~ c²/|κ| at fixed x): ~6.3–8.4 orders of
  every row's gap live here and no audited factor touches them.

## VERDICT — **GAP MOVES** (bound-branch clause; the ratio does not move)

Per the fixed verdict language, GAP MOVES triggers because the
bound audit shows the 10⁸ m² figure **does not apply to the
κ < 0 branch as carried**: Feng–Geng–Luo's Buchdahl bound is a
κ > 0-only, future-3 M⊙-conditional result, so against *that*
figure the mixture's gap is not 8.3 orders — it is **undefined**
(no published constraint from that source on this branch).
The factor that moved is **(b), the bound's branch/conditional
status**; factors (a) and (c) did not move the ratio below the
bar: against the sign-blind |κ| ≲ 10⁸ m² order bound that does
apply (Avelino-type), every PASS row's ratio remains
**1.85×10⁶ to 2.75×10⁸ (6.27–8.44 orders)** — i.e. the numeric
gap stands at ≥6 orders on every f ≥ 1/2 row, smallest on the
w = 0 rows where the radial coefficient vanishes and the boosted
transverse term (0.0101 per |κ|) sets |κ|\* = 1.85×10¹⁴ m².

**One-line window (mixture row):** survivable radius
r₀\* = 9.6×10⁶–1.17×10⁸ m (row-dependent; 7.1×10⁷–1.17×10⁸ m for
w > 0), required |κ|\* = 1.85×10¹⁴–2.75×10¹⁶ m², applicable bound
|κ| ≲ 10⁸ m² (sign-blind Avelino-type; the carried Feng/Buchdahl
10⁸ is κ > 0-only and future-conditional), **gap 6.27–8.44
orders on every PASS row**.

## Follow-ups (Failure Protocol)

1. **Reconstruction-level recheck (owed to P35-1 Step B):** the
   mixture's Ω structure differs from the one-fluid case —
   ω_θ = √[(1+κρ_tot)(1−κp_r,tot)] vanishes as ε^{1/2} with
   1−κp_r,tot(r₀) = f(1+w) finite, so the q-areal radius scales as
   H ~ ε^{1/4}, not the one-fluid √ε. Whether the profile-level
   F′(r₀) = 2(1−x)/r₀ and Φ′(r₀) used here survive the Step B
   reconstruction must be checked against its output when it
   lands; if F′(r₀) differs, C_rad rescales by F′(r₀)/1.41421 and
   the w = 0 rows' transverse floor moves with it.
2. **A κ < 0-native stellar bound:** the phase-transition
   literature Feng et al. cite for excluding κ < 0 (Sham et al.:
   with first-order phase transitions, κ < 0 equilibrium stars
   "cannot be constructed") suggests the true κ < 0 constraint
   may be a *construction failure*, not a number — deriving the
   sharpest published κ < 0 statement (bound or no-go) is a
   bounded literature+TOV item that would replace the Avelino
   order-of-magnitude stand-in used here.
