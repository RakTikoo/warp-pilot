# P35-3 — COUNTER-ROTATING SHELL CURRENTS: **FAIL**

**Plain:** the one shell channel rotation left open is closed, and it
closes twice over. Two counter-rotating dust streams are perfectly
legal matter — but a wormhole shell demands a *negative* surface
density and a *positive* pressure, i.e. 𝒫/σ < 0, while any pair of
dust streams has σ ≥ 0 and 𝒫/σ = v² ≥ 0. The streams would need an
imaginary speed. No tuning of v or charge touches either sign,
because v enters the stream tensor only through γ² > 0 and v² ≥ 0.

## Run record (stated before solving)

- Baseline: sum-glued thin-shell throat only (wormhole topology;
  difference gluing is P24-1's scope, not this item). Per side,
  f_i = 1 − 2M_i/r + Q_i²/r², s_i = √f_i(a), t_i = s_i(1+A_i) =
  (1−M_i/a)/s_i (Minkowski side: t_i = 1). Lanczos:
  σ_L = −(s₊+s₋)/(4πa), 𝒫_L = (t₊+t₋)/(8πa), isotropic
  (𝒫_θ = 𝒫_φ = 𝒫_L). Admissible domain a > r₊ on both sides.
- M1 (streams along φ̂): σ_s = σ₀γ², 𝒫_∥ = 𝒫_φ = σ_s v², 𝒫_⊥ =
  𝒫_θ = 0. M2 (isotropised pairs): 𝒫_θ = 𝒫_φ = σ_s v². σ₀ = total
  rest surface density of both streams; net S^t_φ = 0. Matching =
  σ-equation AND 𝒫-equation (M1: φ̂φ̂; its θ̂θ̂ mismatch reported)
  satisfied by ONE (σ₀ > 0, v ≤ 0.5) pair.
- **β₀² prescription (fixed before solving):** Poisson–Visser with
  the stream EoS along the stream family at FIXED v. On that family
  𝒫 = v²σ_s exactly (linear), so β₀² = d𝒫/dσ_s = v² ∈ [0, 0.25];
  the registered general form v² + σ_s·d(v²)/dσ_s reduces to v²
  under this prescription.
- Gates: sympy Q→0 limit reproduces P23-1's σ, 𝒫 exactly; v→0
  stream limit gives (σ₀, 0); v = 0 control reproduces the static
  σ-identity failure with max abs err **0.0** (2,000 points);
  stability V″ machinery gated against P23-1's closed form at
  Q = 0 to **1.8×10⁻¹⁵**.

## Deciding combination (as computed, both models)

Both Lanczos equations fail **independently**, on every one of
786,150 grid points (symmetric Schwarzschild 783; symmetric RN
314,669; asym RN–Schw 156,600; RN–Mink 157,330; RN–RN(½Q) 156,768):

1. **σ-equation:** σ_L = −(√f₊+√f₋)/(4πa) < 0 on 100% of points,
   demanding σ_s < 0; streams give σ_s = σ₀γ² ≥ 0. Required
   σ₀ = σ_L(1−v²) < 0 for every v ∈ [0, 0.5].
2. **Ratio equation:** streams require 𝒫/σ_s = v² ∈ [0, 0.25];
   the throat pair has 𝒫_L > 0 on 100% of points, hence
   𝒫_L/σ_L < 0 everywhere — grid range **[−25461, −0.505]**
   (→ −1/2 at large a, → −∞ at the horizon). v²_required is
   negative: no real v exists *even if the σ sign were waived*.
   This refutes-or-proves the registered candidate as stated:
   **proven, and strengthened** — the failure is a double sign
   mismatch, not a single one.

M1 carries a third, independent failure: its θ̂θ̂ equation demands
𝒫_θ = 0 while Lanczos gives 𝒫_θ = 𝒫_L > 0 (𝒫_L·M range
[0.0016, 6.73] on the symmetric RN grid — never 0). M2 removes
that clause and still fails on (1) and (2).

## Reference rows (a = 1 m, x = a/2M = 2, symmetric)

| row | σ_L (kg/m²) | 𝒫_L/σ_L = v²_req | σ₀ required at v=0.5 |
|---|---|---|---|
| Q = 0 | −1.515×10²⁶ | −0.750 | −1.137×10²⁶ kg/m² |
| Q/M = 0.9 | −1.590×10²⁶ | −0.681 | −1.193×10²⁶ kg/m² |

Scale-free: σ_L·M, 𝒫_L·M and their ratio depend only on (a/M, Q/M);
the sign failure is not a scale effect.

## ECs and stability

- **Stream tensor itself: fully EC-legal.** For σ₀ > 0, all four
  ECs (NEC/WEC/SEC/DEC) pass for both M1 and M2 at every
  v ∈ [0, 0.5] (𝒫_i/σ_s = v² ≤ 0.25 or 0). Nothing exotic was
  smuggled — the streams simply cannot *be* the shell the geometry
  demands. The Lanczos-required tensor (σ_L, 𝒫_L) fails NEC/WEC/
  DEC on every point (σ_L < 0).
- **Stability: moot, and independently empty.** There is no
  solution sequence to stabilise; and evaluating the PV potential
  anyway at the stream β₀² = v² ∈ [0, 0.25] gives V″(a₀) > 0 on
  **0 of 120 a₀-rows** for each of Q/M ∈ {0, 0.5, 0.9, 0.99}
  (consistent with P23-1/P33-1: the window never intersects even
  [0,1]).

## Verdict

**FAIL** — deciding term: the double sign mismatch
σ_L < 0 vs σ_s = σ₀γ² ≥ 0 **and** 𝒫_L/σ_L < 0 vs 𝒫/σ_s = v² ≥ 0,
in both M1 and M2, on all 786,150 grid points including all
charged controls. The counter-rotating-stream channel — the one
channel P33-2a left untied to (σ₀, 𝒫₀) — is not eigenvalue-tied,
and it fails anyway: counter-rotation changes the shell tensor's
*eigenvalue ratio* to v² ≥ 0, but the throat's Lanczos pair lives
at ratio < 0 with σ < 0, a quadrant no dust-stream sum can reach.
With this, every rotation channel for the sum-glued shell throat
is closed (O(Ω) theorem, O(Ω²) rescaling λ ≥ 1, eigenvalue
invariance, and now stream currents).

## Follow-ups (Failure Protocol)

- **F1 — Heat-flow / radially-moving stream shell:** the stream
  quadrant argument covers purely *tangential* dust sums. A shell
  layer with a radial energy flux (S^t_r ≠ 0, e.g. two
  counter-streaming radial flows or a Vaidya-type through-flow)
  changes the Lanczos system itself (non-static shell, flux term
  in the junction conditions) — the only stream variant whose
  σ-equation is not the static sum-of-roots. Needs its own
  pre-registration as a non-static shell item; prediction: the
  flux buys a transient, not an equilibrium, throat.
- **F2 — Charged streams:** streams carrying opposite charges with
  a shell self-field add Maxwell stress ∝ (tension along the
  field) to the shell tensor, whose 𝒫/σ can be negative
  (ρ_EM > 0, p_∥ = −ρ_EM). That is no longer a pure dust-stream
  item — it is P33-1's charge channel relocated *into* the shell
  tensor rather than the bulks, and is the one registered route
  by which a stream-family tensor could reach the 𝒫/σ < 0
  quadrant; worth one pre-registered row before the stream class
  is declared structurally closed.

Record: `phase35/p353_shell_streams.py`,
`phase35/results/p353_results.json`, this memo. Internal only.
