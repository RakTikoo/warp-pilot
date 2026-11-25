# P245-3 MEMO — THE PULSED DRIVE (Phase 245, Item 3 / C3)

**Verdict form fired: PULSING TRADES EVEN OR WORSE (the per-distance price as a function of δ priced — QI binds the average, so the wall is duty-invariant in this class, stated with the scaling)**

Registration: `phase245/work/p2453_registration.md` (written before
any deciding computation). Driver: `phase245/work/p2453_run.py`.
All verdict-carrying numbers: `phase245/results/p2453_results.json`.
Frame of record: Phase 166 pin, Gate-19-corrected tensor (lineage;
T_req is Phase 235's derived stress, consumed from disk), programme
venv (python 3.12.3 / numpy 2.5.5 / scipy 1.18.1), float64. Bounded
local run (seconds-class). No legality optimisation; nothing tuned.

## The pose (as registered)

The Phase 235 drive (β = 1.1 primary; β = 1.5 secondary check),
gated by a square-wave pulse χ(t) ∈ {0, 1} multiplying the shift,
duty δ ∈ {1, 0.5, 0.25, 0.1}, in the rapid-pulsing regime
P = τ/100 = 0.1 (100 pulses per sampler width — the regime most
favourable to pulsing, since the τ = 10 Fewster–Eveson sampler then
sees the cycle average). Switching is idealised instantaneous and
the payload is assumed retained across off-intervals with zero
slip: every idealisation is pulsing's best case, so the negative
verdict below is conservative. Transition stresses of a real ramp
are not computed and can only add to the price.

## Controls (run first; all PASS, all exact)

| control | read | result |
|---|---|---|
| CT-1 QI price, δ = 1 | ρ_perm,diff(τ=10) = 3/(256π²·10⁴) = 1.1873576208086459×10⁻⁷; R_diff = \|ρ_req,min\|/ρ_perm = **2852.4125063013466**, rel. diff. vs p2352 JSON **0.0** (β = 1.5 companion: 4677.708524046431, rel. diff. 0.0) | PASS |
| CT-2 transport, δ = 1 | arrival integral recomputed from `build_drive(1.1)`: T = 40.71487882848544, **v_eff = 1.4736627426242535**, rel. diff. vs p2351 JSON **0.0** | PASS |

## Read 1 — the pointwise violation map per duty: UNCHANGED at worst instant

At every ON instant, for every δ > 0, the map is Phase 235's map
exactly (SET-A, β = 1.1; min / median / max):

| clause | min | median | max |
|---|---|---|---|
| NEC | −0.0037834 | −0.0015929 | −1.93×10⁻⁶ |
| WEC | −0.0362103 | −0.0154741 | −1.85×10⁻⁵ |
| DEC † | −1.0000517 | −1.0000096 | −0.0013650 |
| SEC (reported) | −0.0374693 | −0.0154673 | −1.86×10⁻⁵ |
| ρ_euler | −3.3868×10⁻⁴ | −4.494×10⁻⁵ | −1.5×10⁻¹⁵ |

Instantaneous E_neg during an on-pulse: −2.590291375073908;
violating share 0.99827 of shell volume, stress share 1.0, at every
pulse. OFF instants: T_req ≡ 0. **Pulsing does not launder the
pointwise map** — the worst-instant audit is duty-invariant by
construction, and no duty in the set (or any δ > 0) removes a
single pointwise violation while the wall is on.

The cycle-averaged TOTAL stress (NO-EXOTIC standard: one tensor,
judged whole; the off-state contributes zero, not a compensating
positive stress — none is invoked anywhere in this item) is
T̄ = δ·T_req,on, so its margins are δ × the table above (degree-1
homogeneity of the Hawking–Ellis margins in T; the DEC row's
scaling is formal, inheriting Phase 235's † normalised-form
caveat, and no deciding quantity uses it). E.g. at δ = 0.1 the
averaged WEC margin is still −0.0036210 (min) / −0.0015474
(median): the averaged tensor violates at every δ > 0 too, only
shallower. Full per-δ averaged tables: results JSON.

## Read 2 — transport per full cycle

Advance accrues only while the wall is on (flat propagation during
off-intervals is not credited to the drive), at the on-state rate
v_eff,on = 1.4736627426242535:

| δ | v_cycle = δ·v_eff,on | T for D = 60 | superluminal cycle? |
|---|---|---|---|
| 1 | 1.4736627 | 40.7149 | yes |
| 0.5 | 0.7368314 | 81.4298 | no — slower than flat (60) |
| 0.25 | 0.3684157 | 162.8595 | no |
| 0.1 | 0.1473663 | 407.1488 | no |

Superluminal cycle transport requires δ > δ_SL = 1/v_eff,on =
**0.6785813**. The Phase 235 slicing fence is inherited verbatim:
v_eff (and hence v_cycle) is a slicing-dependent effective-arrival
read on the t = const slicing, NOT a transport theorem.

## Read 3 — the QI line per unit transported distance

Difference-QEI form (Phase 66 P66-4, Fewster 2000; scope carried:
the bound is on the excursion BELOW the reference state's sampled
density; NO absolute sustained floor; price relative to the
reference at the stated width). At τ = 10, rapid regime, the
sampler sees ρ̄ = δ·ρ_on, so the sampled ratio scales linearly:

  R_sampled(δ) = δ · 2852.4125 → 2852.41 / 1426.21 / 713.10 / 285.24
  for δ = 1 / 0.5 / 0.25 / 0.1 — still ≫ 1 at every registered duty.

Sampled headroom (R_sampled ≤ 1) requires δ ≤ δ_QI = 1/2852.4125 =
**3.5058×10⁻⁴**. But the deciding quantity is the price PER UNIT
TRANSPORTED DISTANCE — the journey-integrated sampled violation
per unit distance, in permitted-density units:

  ℘(δ) ≡ R_sampled(δ) / v_cycle(δ)
        = (δ · R_diff,on) / (δ · v_eff,on)
        = R_diff,on / v_eff,on = **1935.5938 for every δ**

(median-form companion, formed with the SET-A median |ρ|:
℘_med = 256.8232, likewise δ-invariant.) The two windows never
meet: δ_QI = 3.5058×10⁻⁴ and δ_SL = 0.6785813 are disjoint by a
factor 1935.59 — exactly ℘ itself. A duty small enough for the
averaged density to fit the bound transports at v_cycle ≈
5.17×10⁻⁴; a duty large enough to stay superluminal pays the full
2852-class sampled price. The invariance is width-by-width: at the
secondary width τ = 1, ℘ = 0.285241/1.473663 = 0.19355 at every δ
(that width's on-state price was already < 1 continuously — pulsing
is irrelevant there, and equally invariant).

Slow regime (P ≫ τ) is worse, never better: a sampler centred on a
pulse sees ρ_on at full depth (R = 2852.41 at any δ), so
℘_slow(δ) = 1935.5938/δ (3871.19 at δ = 0.5; 19355.94 at δ = 0.1).
The rapid-regime invariant is therefore the floor of the
per-distance price across regimes.

Secondary check, β = 1.5 (disk inputs): R_diff,on = 4677.7085,
v_eff,on = 1.5890184, ℘ = **2943.7724** at every δ; δ_QI =
2.1378×10⁻⁴ vs δ_SL = 0.6293193 — same structure, wider gap.

## Why the other forms do not fire

- PULSING CLEARS QI HEADROOM would require a δ with
  R_sampled(δ) ≤ 1 AND v_cycle(δ) > 1; by the two scalings that is
  δ ≤ 3.5058×10⁻⁴ AND δ > 0.6785813 — empty for the registered set
  and, since both scalings are exact in δ, for every δ > 0.
- PULSED TRANSPORT FAILS (slip) does not fire: under the registered
  best-case retention fence, retained advance is δ·v_eff,on > 0
  for every δ > 0 — transport shrinks with δ but is not lost
  between pulses in this accounting. Switching/slip dynamics are
  outside the factory's stationary solutions and were not computed;
  any real slip only lowers v_cycle and raises ℘, so it cannot
  change this verdict's direction — it would move the result
  further into "or worse".

## Verdict

**PULSING TRADES EVEN OR WORSE** — QI binds the cycle-averaged
density (R_sampled ∝ δ) and honest per-cycle accounting binds the
transport by the same factor (v_cycle ∝ δ); their ratio, the price
per unit transported distance, is duty-invariant at ℘ = 1935.59
(β = 1.1, τ = 10; 2943.77 at β = 1.5), and strictly worse in the
slow-pulsing regime (℘ ∝ 1/δ). The Phase 235 wall was not a duty
assumption: in this drive class, no duty cycle buys QI headroom
per unit distance. The pointwise violation map is separately
unchanged at every on-instant for every δ > 0.

Nothing was appended to NEW_PHYSICS_LEDGER.md; nothing external
was launched; writes are inside phase245/ only.
