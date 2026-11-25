# PHASE 307 — ARM 6: THE EDGE (red team on the flat rows' w₀ ≈ 1 edge)

**Registration:** `phase307/work/p307_registration.md`, ARM 6
(scope: the flat value G32-F). **Computation:**
`phase307/work/p307_arm6_run.py` + `.out` (Phase 303 machinery
adapted, one added constraint; venv python, central model f = 1).
No ledger append, no launches.

## VERDICT: **HOLDS** (at the registered δ = 10⁻³ strength)

The flat value is **edge-hugging but robust**, not an edge
artefact. At the registered margin δ = 10⁻³ the interior
maximisation reproduces HT **2.8044×10⁻⁵ at both c_V = 2 and
c_V = 10, to all quoted digits** (2.804394×10⁻⁵ / 2.804397×10⁻⁵),
with L9 still the binding leg. The value only breaks at ten
times the registered margin (δ = 10⁻²: HT 4.76×10⁻⁶ / 3.78×10⁻⁶,
below the envelope floor 1.01×10⁻⁵ — but still 10³–10⁵× above
the spin-0 row's prices at the same speeds, so even there it is
a degradation, not a collapse toward the spin-0 row). Full
sensitivity table in §2.

---

## 1. Item 1 — the edge identified (registration CONFIRMED, one correction of form)

**The identification is correct.** w₀² = (2−c₁₄)c₂/[(2+3c₂)c₁₄]
is YBBY Eq. (108) on the c₁₃ = 0 slice — the general form is
w₀² = (2−c₁₄)c₁₂₃/[(2+3c₂+c₊)(1−c₊)c₁₄] (YBBY, PRD 89, 084067,
arXiv:1311.7144), and it is the **spin-0 (scalar companion)
mode's squared propagation speed**: it coincides with the
spin-0 speed in Jacobson's status review (arXiv:0711.3822,
Eq. 11: c₁₂₃(2−c₁₄)/[c₁₄(1−c₁₃)(2+c₁₃+3c₂)], which reduces to
the slice form at c₁₃ = 0, c₁₂₃ = c₂). The w₀ = 1 surface is
therefore exactly the surface where the scalar mode propagates
at the (matter) light speed.

**Why the fence keeps only the w₀ > 1 side.** A subluminal
gravitational mode is vacuum-Čerenkov-radiated by
ultra-high-energy cosmic-ray particles, which would lose their
energy to gravi-Čerenkov emission en route. YBBY state this in
their introduction: the surviving parameter region is bounded
by "requiring the speeds of the gravitational modes be larger
than the speed of light, so that photons and high-energy
particles do not lose energy in a Cherenkov-like process."
Jacobson's review states it identically: the squared speeds
"must moreover be greater than unity (super-luminal), to avoid
the existence of vacuum Čerenkov radiation by matter. (The
strongest constraints arise from the existence of ultra high
energy cosmic rays.)" The underlying bound is Moore & Nelson,
JHEP 09 (2001) 023 (c − c_g < 2×10⁻¹⁵ c for galactic-origin
cosmic rays, ~2×10⁻¹⁹ c extragalactic), applied to the
Einstein-aether modes by Elliott, Moore & Stoica, JHEP 08
(2005) 066; in the form quoted in the later EA literature the
physical bound is **c_{S,V,T}² > 1 − 10⁻¹⁵** — i.e. the true
Čerenkov leg tolerates subluminality of order 10⁻¹⁵ in w².

**Which leg enforces it here, and in what form.** In Phase
303's completed fence this is **leg L5** (Čerenkov: w₀² ≥ 1 and
w₁² ≥ 1). As *registered and coded* (`p303_pricing.py`
`feasible()`: `if w02 < 1.0: return False`) it is a **hard
exclusion with zero tolerance** — strictly stronger than the
physical bound by ~10⁻¹⁵ in w₀². That discrepancy is real but
immaterial to this arm: every margin tested below is
δ ≥ 10⁻⁴, eleven orders above the physical tolerance, so no
conclusion here turns on the fence's zero-tolerance form.

**What else lives at w₀ = 1: nothing singular.** w₀ = 1 is a
regular point of the theory, not a degeneracy:

- The spin-0 mode's energy sign is ∝ c₁₄(2−c₁₄) (Eling, via
  Jacobson's review) — independent of w₀; the ghost/gradient
  (L6 stability) conditions are w₀² > 0 and that sign, neither
  of which degenerates or changes character at w₀ = 1.
- The dipole coefficient 𝒞 = 4/[3w₀³c₁₄(2−c₁₄)] +
  4/[3c₁₄w₁³] and the other flux coefficients (A₂ ∝ w₀⁻³,
  A₃ ∝ w₀⁻⁵) are finite and smooth at w₀ = 1; the singular
  points of the scalar sector are w₀ → 0 and c₁₄ → 0 / 2,
  not w₀ = 1.
- Physically, w₀ = 1 is only the light-cone crossing of the
  scalar mode: below it the Čerenkov channel kinematically
  opens, above it it closes. The edge in the fence is imposed
  entirely by the observational L5 leg; the theory itself
  places no wall there. (Phase 298's Corner A sat exactly on
  it, w₀ = 1.000000 — a regular point that died by L9, not by
  any pathology at the edge.)

So the registration's identification stands, with the single
correction that the *physical* Čerenkov bound carries a
~10⁻¹⁵ tolerance below 1 which the fence's L5 implements as a
hard cut.

## 2. Item 2 — the interior re-run

Machinery: `p303_pricing.py`'s functions copied verbatim
(α₂ form, 𝒞, anchor σ, α̂'s, Peters fiducials, the
grid + Nelder–Mead maximiser over (c₂, c₁₄) with
c₁ = c*²c₁₄), completed fence as registered there (L2
c₁₄ ≤ 2.5×10⁻⁵; L3 |α₂| ≤ 10⁻⁷; L4 BBN ≤ 0.125 with the
programme's 10⁻⁹-relative saturation tolerance; L5; L7
|α̂₁| ≤ 10⁻⁵; L8 |α̂₂| ≤ 10⁻⁹; L9 ⟨𝒜⟩_dip ≤ 0.1; f = 1),
plus the single added constraint **w₀² ≥ 1 + δ**.

### Controls (δ = 0) — PASS, run before any δ > 0 read

| c* | HT ratio (re-run) | vs 2.8044×10⁻⁵ | NS–BH | Maximiser (c₁, c₂, c₁₄) | w₀ |
|---|---|---|---|---|---|
| 2 | 2.804394×10⁻⁵ | rel. diff 2.3×10⁻⁶ | 2.539405×10⁻² | (2.544311×10⁻⁵, 6.362042×10⁻⁶, 6.360776×10⁻⁶) | 1.000093 |
| 10 | 2.804397×10⁻⁵ | rel. diff 9.5×10⁻⁷ | 2.539405×10⁻² | (7.951095×10⁻⁴, 7.962078×10⁻⁶, 7.951095×10⁻⁶) | 1.000682 |

Peters controls exact (7.7808×10²⁴ W / 1.2696×10²⁵ W);
maximisers match Phase 303 §3.2's stored rows. Control
condition met; the δ > 0 reads below are quotable.

### Sensitivity table (central model, f = 1)

| c* | δ | Maximiser (c₁, c₂, c₁₄) | c₋ | w₀ (w₀²) | 𝒞 | σ_Æ | Binding legs | HT ratio | NS–BH ratio |
|---|---|---|---|---|---|---|---|---|---|
| 2 | 0 | (2.5443×10⁻⁵, 6.3620×10⁻⁶, 6.3608×10⁻⁶) | 5.089×10⁻⁵ | 1.000093 (1.000186) | 1.3098×10⁵ | 2.5952×10⁻⁶ | L9 = 0.10000 | 2.804394×10⁻⁵ | 2.539405×10⁻² |
| 2 | 10⁻⁴ | (2.5449×10⁻⁵, 6.3644×10⁻⁶, 6.3621×10⁻⁶) | 5.090×10⁻⁵ | 1.000171 (1.000342) | 1.3093×10⁵ | 2.5957×10⁻⁶ | L9 = 0.10000 | 2.804394×10⁻⁵ | 2.539405×10⁻² |
| 2 | **10⁻³** | (2.5483×10⁻⁵, 6.3793×10⁻⁶, 6.3707×10⁻⁶) | 5.097×10⁻⁵ | 1.000665 (1.001331) | 1.3060×10⁵ | 2.5990×10⁻⁶ | L9 = 0.10000; L8 at 0.78 of bound | **2.804394×10⁻⁵** | **2.539405×10⁻²** |
| 2 | 10⁻² | (4.3753×10⁻⁶, 1.1048×10⁻⁶, 1.0938×10⁻⁶) | 8.751×10⁻⁶ | 1.004988 (1.010000) | 7.5282×10⁵ | 4.4591×10⁻⁷ | **L8 = −1.0000×10⁻⁹ (saturates)**; added w₀-margin leg saturates; L9 falls to 0.01697 | 4.758697×10⁻⁶ | 4.309064×10⁻³ |
| 10 | 0 | (7.9511×10⁻⁴, 7.9621×10⁻⁶, 7.9511×10⁻⁶) | 1.590×10⁻³ | 1.000682 (1.001365) | 8.3842×10⁴ | 3.2437×10⁻⁶ | L9 = 0.10000; L8 at 0.998 of bound | 2.804397×10⁻⁵ | 2.539405×10⁻² |
| 10 | 10⁻⁴ | (7.9455×10⁻⁴, 7.9531×10⁻⁶, 7.9455×10⁻⁶) | 1.589×10⁻³ | 1.000470 (1.000940) | 8.3955×10⁴ | 3.2415×10⁻⁶ | L9 = 0.10000 | 2.804397×10⁻⁵ | 2.539405×10⁻² |
| 10 | **10⁻³** | (7.9479×10⁻⁴, 7.9569×10⁻⁶, 7.9479×10⁻⁶) | 1.590×10⁻³ | 1.000561 (1.001122) | 8.3907×10⁴ | 3.2424×10⁻⁶ | L9 = 0.10000; L8 at 0.82 of bound | **2.804397×10⁻⁵** | **2.539405×10⁻²** |
| 10 | 10⁻² | (1.0873×10⁻⁴, 1.0983×10⁻⁶, 1.0873×10⁻⁶) | 2.175×10⁻⁴ | 1.005017 (1.010060) | 6.0520×10⁵ | 4.4327×10⁻⁷ | **L8 = −1.0000×10⁻⁹ (saturates)**; L9 falls to 0.01348 | 3.780351×10⁻⁶ | 3.423159×10⁻³ |

### How the maximiser moves

- **δ = 10⁻⁴ and δ = 10⁻³: the maximiser barely moves and
  nothing re-solves.** At c* = 2, c₁₄ shifts +0.02% (δ=10⁻⁴)
  and +0.16% (δ=10⁻³), c₂ +0.04% / +0.27%; the point simply
  steps a little further up the c₂ direction to clear
  w₀² ≥ 1+δ (its achieved w₀² overshoots the imposed floor:
  1.001331 vs 1.001 required). At c* = 10 the δ = 0 maximiser
  already satisfies δ = 10⁻³ (w₀² = 1.001365 > 1.001), and the
  re-run lands on a neighbouring ridge point (c₁₄ −0.04%).
  In all four rows **L9 remains the binding leg at exactly
  0.10000** and the ratio is unchanged to all quoted digits —
  as Gate-32 §3 showed it must be: once L9 binds, the
  maximised HT ratio is forced algebraically
  (0.1 × (ΔC_*/0.17)² × (X_HT/X_J1738) × g/F), independent of
  the couplings, so a small displacement of the maximiser
  inside the fence cannot move the value. L8 creeps closer at
  c* = 2 (0.11 → 0.20 → 0.78 of its bound across
  δ = 0, 10⁻⁴, 10⁻³) but does not bind.
- **δ = 10⁻²: the regime changes.** Clearing w₀² ≥ 1.01 at the
  old c₁₄ would require a c₂/c₁₄ ratio whose α̂₂ read breaks
  L8; instead c₁₄ **re-solves downward by a factor ~5.8
  (c* = 2) / ~7.3 (c* = 10)** to ≈ 1.09×10⁻⁶, σ falls by the
  same factor, 𝒞 rises ~×5.7 / ×7.2, the **binding leg
  switches from L9 to L8** (α̂₂ = −1.0000×10⁻⁹ exactly, with
  the added w₀-margin leg also saturating at c* = 2), and L9
  goes slack (0.017 / 0.013). The price falls to
  HT 4.758697×10⁻⁶ (c* = 2) and 3.780351×10⁻⁶ (c* = 10) —
  below the envelope floor 1.01×10⁻⁵, by factors 2.1 / 2.7.
  Even there, however, the values sit ×1.2×10³ (c* = 2) and
  ×1.6×10⁵ (c* = 10) **above** the spin-0 row's prices
  (HT 3.917708×10⁻⁹ at c_S = 2; 2.374368×10⁻¹¹ at c_S = 10):
  degradation, not collapse.

### Verdict against the registered criteria

- BREAKS requires, at δ = 10⁻³, an interior value below
  1.01×10⁻⁵ or a collapse toward the spin-0 prices. Observed
  at δ = 10⁻³: **2.804394×10⁻⁵ (c* = 2) and 2.804397×10⁻⁵
  (c* = 10)** — neither. **BREAKS fails.**
- HOLDS requires the flat value reproduced at δ = 10⁻³ within
  the bracket's variation, with the sensitivity table shown.
  Observed: reproduced **exactly** (rel. change < 10⁻⁵, far
  inside the f-bracket envelope [1.01×10⁻⁵, 2.80×10⁻⁵]).
  **HOLDS, at full (not weak) strength for the registered
  margin.**

**The true description, per the registered subtlety:** the
maximisers do hug the edge (w₀ − 1 ~ 10⁻⁴–10⁻³ at δ = 0, the
same order as δ itself), but the *value* is not an edge
artefact at any margin up to ten times smaller than the
distance at which it finally degrades: it survives δ = 10⁻³
unchanged because its binding constraint is L9, not L5, and
L9's cap is coupling-independent once it binds. The honest
caveat the flat rows should carry is the δ = 10⁻² row of the
table: push the scalar mode a full percent (in w₀²) into the
interior and the fence's binding leg changes to L8 and the
price drops to ~4×10⁻⁶ — still a distance-0-class value
against the 10⁻⁶ bar, and still orders above the spin-0 row
at the same speed, but no longer the flat 2.8044×10⁻⁵.

## 3. Scope and limits

- The re-run uses Phase 303's machinery as registered,
  including its floor-binding representative choice
  c₁ = c*²c₁₄ (Gate-32 established the maximiser set is a
  ridge; the interior constraint w₀² ≥ 1+δ acts on (c₂, c₁₄)
  only, so the ridge structure in c₁ is untouched by this
  arm's test).
- All numbers are central-model (f = 1) as registered for
  this arm; the f-bracket envelope is Phase 303 §3.2's /
  Gate-32's, not re-run here.
- Sources for §1: YBBY PRD 89, 084067 (arXiv:1311.7144,
  Eq. 108 and introduction); Jacobson arXiv:0711.3822 (spin-0
  speed Eq. 11, energy signs, Čerenkov statement); Moore &
  Nelson JHEP 09 (2001) 023; Elliott, Moore & Stoica JHEP 08
  (2005) 066; the c_{S,V,T}² > 1 − 10⁻¹⁵ form as quoted in
  the subsequent EA literature. OMW arXiv:1802.04303 is the
  fence's L7/L8 source and states no separate w₀ tolerance.
