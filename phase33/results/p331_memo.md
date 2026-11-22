# P33-1 — CHARGED THIN SHELLS — memo

**Baseline (one line):** the uncharged thin-shell wormhole has
σ = −√(1−q)/(2πa) < 0 for every shell (P23-1 identity, STRUCTURAL
KILL); this item adds electric charge (RN bulks, real Maxwell field)
and asks whether charge can flip σ, fix the shell ECs, or open the
Poisson–Visser stability window.

**VERDICT: AUGMENTED-FAIL.**
**Deciding term:** σ = −(√f₊(a) + √f₋(a))/(4πa) — a *sum of two
strictly positive roots*. Charge enters only inside the roots and
cannot flip the sign (proof in §4). Stability window ∩ [0,1] = ∅
at every charged row as well, so the item fails on two independent
clauses; σ is the deciding one (it kills every row before stability
is even consulted).

## 1. Derivation (sympy, script p331_charged.py)

Per side: ds² = −fᵢ dt² + dr²/fᵢ + r²dΩ²,
fᵢ(r) = 1 − 2Mᵢ/r + Qᵢ²/r², Φᵢ = ½ ln fᵢ, sᵢ = √fᵢ(a),
Aᵢ = aΦᵢ′(a). Wormhole gluing (two exteriors, normals pointing
into the two asymptotic regions — the P23-1/P24-1 sum form):

  σ = −(s₊ + s₋)/(4πa),
  𝒫 = [s₊(1+A₊) + s₋(1+A₋)]/(8πa).

Key simplification (sympy-verified, difference = 0):
sᵢ(1+Aᵢ) = (2fᵢ + afᵢ′)/(2√fᵢ) = (1 − Mᵢ/a)/√fᵢ, because for RN
2f + af′ = 2(1 − M/a) — **the Q² terms cancel exactly in 𝒫's
numerator**. Hence, symmetric RN:

  σ = −√(1 − 2M/a + Q²/a²)/(2πa),
  𝒫 = (1 − M/a) / (4πa √(1 − 2M/a + Q²/a²)).

Sign checks: Q→0 reproduces P23-1 exactly (σ = −s/(2πa),
𝒫 = (1−M/a)/(4πa√(1−2M/a)), the standard PV pressure) ✓.
Flipping one side's orientation reproduces P24-1's difference
form σ = −(s_out − s_in)/(4πa) and its smooth limit σ=𝒫=0 ✓.
Shell's own charge: the Maxwell junction puts the charge
difference Q₊−Q₋ on the shell (symmetric case: equal |Q|, field
threading the throat); consistently, Q enters the Lanczos
S^μ_ν *only* through the fᵢ — there is no extra term. The EM
bulk is EC-legal everywhere: u = Q²/(8πr⁴) ≥ 0, p_r = −u,
p_t = +u (NEC saturated radially, DEC saturated, traceless),
and ρ+p_r = 0 makes the flux-free shell conservation law
σ′ = −2(σ+𝒫)/a exact for RN sides (the P24-1 F-S1 caveat does
not arise here).

## 2. (Q1) Symmetric RN — σ ≥ 0 at sub-extremal Q/M < 1?

**No.** f_RN(a) = f_Schw(a) + Q²/a² > f_Schw(a): at fixed (M, a)
charge makes the root *larger*, so σ is **more** negative than
the uncharged shell, for every a > r₊. Grid (M = 1, Q/M ∈
[0, 0.999] × 400, a/M ∈ (r₊/M, 50] × 800, both sides filtered
a > r₊ strictly): **314,669 points, σ ≥ 0 on 0, all-four-EC
legal on 0** (SEC alone holds on 6,145 — never rescues the set,
since NEC/WEC/DEC each require σ ≥ 0). Most negative row:
σ·M = −0.03974 at Q/M = 0.999, a/M ≈ 1.98. Reference row
a = 1 m, a = 2M, Q/M = 0.9: σ = −9.64×10²⁵ kg/m², shell mass
−1.21×10²⁷ kg (vs −1.90×10²⁷ kg uncharged at x = 2 in P23-1's
different normalisation a/(2M) — same sign, same order).

## 3. (Q2) Asymmetric wormhole gluings

Same answer, by the same term — σ is a sum of the two sides'
roots whatever the sides are (a must exceed *both* outer
horizons). Grids (a > max(r₊₊, r₊₋) enforced):
RN–Schwarzschild 156,600 pts, RN–Minkowski-exterior 157,330 pts,
RN–RN with Q₋ = Q₊/2 156,768 pts — **σ ≥ 0 on 0 and all-EC
legal on 0 in every family**. The Minkowski side is the worst
partner: its root is exactly 1, the largest possible, so
σ ≤ −1/(4πa) − √f_RN/(4πa) there.

## 4. (Q4) The general statement, and the one evasion

**Claim.** Let two static, spherically symmetric exterior
regions with metric functions f±(r) be glued at r = a in the
wormhole topology (two asymptotic regions, shell normals
pointing away from the shell into each region). If the shell
lies in the static region of both sides, f±(a) > 0, then the
angular extrinsic-curvature jump is [K^θ_θ] ∝ √f₊ + √f₋ and

  σ = −(√f₊(a) + √f₋(a))/(4πa) < 0, strictly.

Charge — indeed *any* bulk content — enters σ only through the
values f±(a). For RN, f(a) = 1 − 2M/a + Q²/a²; sub-extremality
(Q/M < 1) plus a > r₊ is exactly the condition f(a) > 0, i.e.
exactly the condition that the root is real and positive. The
sum can vanish only if both roots vanish, i.e. a sits on both
horizons — excluded by the bar (a > r₊ strictly) and worthless
where approached: in the a→r₊ limits (follow-up F2) σ→0⁻ only
as 𝒫·M → +∞ like ε^(−1/2) (ε = 10⁻²…10⁻⁶, fixed-Q and
extremal-diagonal sequences in the JSON), the P23-1 singular
limit with charge added. **No sub-extremal charge, on either
or both sides, symmetric or not, flips σ. The augmentation is
refuted by an identity, not by a scan** (the scans are the
cross-check: 785k+ wormhole rows, zero exceptions).

**The evasion, and why it is not a throat.** Flip one normal:
glue an *interior* ball to one exterior (difference gluing,
P24-1). Then σ = −(s_out − s_in)/(4πa), a difference of roots,
and σ > 0 is generic. Follow-up F3 computed it (RN exterior /
Minkowski interior): **15/15 sampled rows pass all four shell
ECs** (e.g. a/M = 3, Q/M = 0: σ·M = +0.0112, 𝒫·M = +0.00205).
Labelled, as registered: **NOT A THROAT.** The object has one
asymptotic region and one mouth; the interior is a capped ball,
there is no second side to cross *to*, and no through-path
exists. It is a charged star / gravastar-pattern shell. P24-1
already showed the complementary fact: difference-gluing onto
a segment that *does* contain a genuine throat re-presents the
flare-out NEC violation in that bulk segment (−2/r₀²,
Φ-independent). The sum-of-roots sign is the price of having
two outsides; removing an outside removes the wormhole.

## 5. (Q3) Poisson–Visser stability with charge

V(a) = f(a) − (2πaσ(a))², ȧ² + V(a) = 0, σ(a) extended by the
(exact, §1) conservation law; V″(a₀) derived symbolically —
linear in β₀² ≡ d𝒫/dσ|₀, as in PV. **Gates:** Q→0 reproduces
P23-1's a₀²V″ = [−4(2x−3)(x−1)β₀² − (4x²−6x+3)]/(2x(x−1)) to
1.8×10⁻¹⁵; finite-difference validation of the charged V″ at
four (a₀, Q) rows: rel. err ≤ 1.2×10⁻⁸.
Result over Q/M ∈ {0, 0.3, 0.5, 0.7, 0.9, 0.99, 0.999} × 60
a₀ values each (420 rows): **window ∩ [0,1] = ∅ on every row**,
with P23-1's structure intact — near the horizon stability
needs β₀² > β_crit ≈ +243…+251 (superluminal sound), at larger
a₀ it needs β₀² below a negative threshold ≈ −0.58…−0.71.
Charge moves the thresholds only slightly *toward* [0,1]
(near-horizon β_crit 251.0 → 243.2 from Q = 0 → 0.999;
a₀ ≈ 8M threshold −0.712 → −0.682) and never across. At
a₀ = 3M, where the uncharged β₀² coefficient vanishes (x = 3/2,
no β₀² works), charge restores a finite slope but with
β_crit = −8.08 (Q/M = 0.5) → −1.54 (0.99): still negative,
still no physical window.

## 6. What charge DOES buy — priced

- **|σ|: nothing; it costs.** At fixed (M, a): |σ| grows by
  ×1.041 (Q/M = 0.5), ×1.127 (0.9), ×1.152 (0.99) at a = 3M;
  ×1.008–1.032 at a = 5M; ×1.002–1.006 at a = 10M. (Follow-up
  F1, fixed a/r₊ instead: the apparent relief at high Q is a
  parametrisation artefact — r₊ shrinks with Q, so a/r₊ fixed
  means a smaller shell around a smaller horizon; at fixed
  a/r₊ = 5, σ·M actually worsens −0.0142 → −0.0246 from
  Q/M = 0 → 0.999 because M is held fixed while a shrinks.
  No parametrisation gives σ ≥ 0 or even a monotone relief.)
- **𝒫: a real reduction.** 𝒫's numerator is Q-independent
  (§1) while its denominator √f grows: 𝒫/|σ| = (1−M/a)/(2f)
  falls, e.g. at a = 3M from 1.000 (Q = 0) to 0.754 (Q/M =
  0.99); 𝒫·M falls 0.0306 → 0.0266. σ+𝒫 moves *toward* zero
  at a = 3M (−0.0087 at Q/M = 0.99 vs 0 at Q = 0 — actually
  worse there) — mixed, small, and irrelevant while σ < 0
  alone fails NEC/WEC/DEC.
- **Stability thresholds: a small move toward [0,1]** (§5:
  ~3% on the near-horizon β_crit, ~0.03 on the large-a₀
  threshold), never an intersection in 420 rows.
- **Horizon structure:** r₊ shrinks (2M → M at extremality),
  so charged shells may sit at smaller a/M — but F2 shows
  that limit is the same singular 𝒫→∞ shell as P23-1's.

Net: charge buys a cheaper pressure and marginally closer
stability thresholds; it charges *more* surface exoticity
(|σ| up) for them, and the sign of σ — the bar's first clause
— is untouched by construction.

## 7. Failure protocol — follow-ups run in-item

- **F1 (parametrisation artefact check):** fixed-a/r₊ scan —
  no relief (§6). The fixed-(M,a) worsening is the honest read.
- **F2 (limit anatomy):** a→r₊ at fixed Q and the extremal
  diagonal: σ→0⁻ only with 𝒫→∞ — limits, never passes, per
  the registered physical-range limits.
- **F3 (evasion priced):** one-mouth difference gluing is
  shell-legal (15/15) and is NOT A THROAT (§4) — the evasion
  costs exactly the wormhole topology.
- **Reopening condition:** a wormhole-topology gluing whose
  angular jump is not a sum of two positive roots — i.e. a
  non-static or non-spherical shell, or f(a) < 0 on a side
  (shell inside a horizon: not a static shell in a static
  region, a different construction needing its own
  pre-registration). Within static spherical two-exterior
  gluings the result is an identity and the item is closed
  structurally.

Files: `p331_charged.py`, `results/p331_results.json`,
`results/p331_memo.md`. CHECKPOINT33.md not edited.
