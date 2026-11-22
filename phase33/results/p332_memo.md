# P33-2 — ROTATION (Phase 33, worker P33-2)

Script: `../p332_rotation.py` · Results: `p332_results.json` ·
float64, venv python (numpy/scipy). Bars and limits from
CHECKPOINT33.md P33-2 (Ωa ≤ 0.5 c; Kerr a* ≤ 0.9), unedited.

**Verdicts: (a) AUGMENTED-FAIL · (b) AUGMENTED-FAIL**
(one sub-computation labelled NOT COMPUTABLE inside each part —
the full Hartle O(Ω²) junction in (a), the genuine axisymmetric
Kerr re-solve in (b) — with the obstruction named; in both parts
the computable sanctioned models were run and decide the verdict.)

---

## (a) Rotating shell throat — AUGMENTED-FAIL

**Baselines.** P23-1 identity re-verified in-run on the registered
grid (q: 100 pts on [0, 0.99], A: 241 pts on [−2, 10], a = 1):
σ₀ = −√(1−q)/(2πa), 𝒫₀ = √(1−q)(1+A)/(4πa); all 24,100 rows fail
the surface ECs statically (σ₀ < 0 for every q < 1).

**O(Ω) — registered expectation TESTED, CONFIRMED (theorem).**
σ and 𝒫 come from the diagonal Lanczos jumps. Under Ω → −Ω
(rotation reversal = time reversal of the stationary
axisymmetric configuration) every diagonal metric component is
even and g_tφ is odd; σ, 𝒫 are rest-frame scalars of the shell
matter, hence even functions of Ω — no O(Ω) term exists. In
Hartle's expansion this is the standard structure: first order
is the frame-dragging potential ω(r) in g_tφ only; diagonal
perturbations enter at second order. The only O(Ω) Lanczos
component is S^t_φ (surface angular-momentum density). At O(Ω),
σ and 𝒫 are unchanged — frame dragging only, as registered.

**O(Ω²), matter side — Model F (surface fluid, exact).** Shell
matter = perfect surface fluid with the statically required
rest-frame (σ₀, 𝒫₀), rigidly rotating at v = Ωa ≤ 0.5. Static
frame: ρ_stat = σ₀ + (γ²−1)(σ₀+𝒫₀), 𝒫_φ = 𝒫₀ + γ²v²(σ₀+𝒫₀),
𝒫_θ = 𝒫₀, plus a t–φ energy flux. Two audits:
- *Eigenvalue audit (the physical one):* the full mixed tensor
  S^a_b (flux included) was diagonalised for sample rows at
  v = 0.3–0.5: eigenvalues are (−σ₀, 0, 𝒫₀, 𝒫₀) to ≤ 7e-17 —
  **exactly the static eigenvalues at every v**. ECs are
  frame-invariant, so a rotating perfect-fluid shell has the
  static EC verdict: DEC/WEC need σ₀ ≥ 0, impossible. 0 pass
  rows on the full (q, A, v) scan.
- *Naive static-frame audit* (treat (ρ_stat, 𝒫_θ, 𝒫_φ) as a
  diagonal tensor — the most favourable misreading): ρ_stat ≥ 0
  does occur (15,200 scan rows; analytically iff A ≥ 7 at
  v = 0.5, since (γ²−1) = 1/3 there), but 𝒫_φ grows faster than
  ρ_stat and DEC fails everywhere: 0 full-EC pass rows; the
  best row of the whole scan is a static one (worst margin
  −1.59e-2).

**O(Ω²), geometry side — Model G (equatorial Kerr-jump
reduction).** Symmetric wormhole, both exteriors Kerr (M, α),
equatorial Lanczos: at the equator g_tt is the Schwarzschild
function (Φ, A unchanged) while √g^rr = √Δ/a, Δ/a² = 1−q+α²/a².
Both diagonal jumps carry √u, so (σ, 𝒫) → λ(σ₀, 𝒫₀) with
λ = √(1 + α²/(a²(1−q))) ≥ 1 (α ≤ 0.45qa at a* = 0.9; λ_max =
1.001 / 1.049 / 1.625 / 4.566 at q = 0.1 / 0.5 / 0.9 / 0.99).
Every margin keeps its sign; |σ| grows. Spin makes the
*required* σ more negative. (Stated limits: O(α²) spin terms in
g_θθ neglected against the √Δ factor; sign and scaling are the
content.)

**NOT COMPUTABLE (scoped).** The full second-order Hartle
junction (h₀/m₀/h₂/m₂ with a shell source, incl. cross terms):
no Hartle solver exists anywhere in the programme record;
every engine on hand is static-spherical (H4 pattern) or an FD
judge that needs an explicit metric only a Hartle solve could
supply. Models F and G bound the two channels such a solve
would mix — matter content and geometry demand — and each
fails independently, so the verdict does not rest on the
missing computation. Reopening: a validated Hartle shell
solver whose O(Ω²) cross terms overcome *both* the eigenvalue
invariance (impossible for a perfect surface fluid — the cross
terms would have to change the required rest-frame σ itself)
and the λ ≥ 1 equatorial rescaling.

**Deciding terms:** rest-frame eigenvalue σ₀ = −√(1−q)/(2πa)
(rotation-invariant); λ ≥ 1 in Model G.

**Follow-up experiment (≥1, per Failure Protocol):** build the
Hartle second-order shell solve for the one channel neither
model covers — a shell whose rotation is carried by a
*non-perfect-fluid* surface current (e.g. counter-rotating
streams, whose S has independent t–φ structure and whose
eigenvalues are NOT tied to (σ₀, 𝒫₀)); audit whether its
required σ at O(Ω²) can reach ≥ 0 at Ωa ≤ 0.5 c. Prediction
from Model G: the geometry demand still rescales by λ ≥ 1, so
the streams must supply the difference — a sharp, checkable
target.

---

## (b) Finalist family in a Kerr background — AUGMENTED-FAIL

**GATE — Schwarzschild control REPRODUCED.** The H4 solver
itself (`h4.solve_in_background`, exact 1D core margins, β=0):

| M_bg | s (run) | s (record) | DEC core (run) | DEC (record) |
|---|---|---|---|---|
| 0 | 0.885 | 0.885 | +3.760e-5 | +3.76e-5 |
| 1 | 2.475 | 2.475 | +2.771e-5 | +2.77e-5 |
| 2 | 4.827 | 4.827 | +1.307e-5 | +1.31e-5 |
| 3 | 8.666 | 8.666 | −1.083e-5 | −1.08e-5 |
| 4 | 16.096 | 16.096 | −5.708e-5 | −5.71e-5 |

All rows within gate tolerance (s rel. err < 1%, DEC abs. err
< 2e-6); interpolated DEC crossing M_bg = **2.547** (record
≈ 2.5). Instrument gated; Kerr read taken.

**Kerr step — stated formalism.** The H4 machinery is
spherical, so Kerr enters by spherical reduction (the O(a²)
diagonal channel of part (a), Model G): *equatorial* —
m_bg(r) = M − α²/(2r) (from u = Δ/r²), Φ_bg = ½ln(1−2M/r)
(exact at the equator); *averaged* — Σ̄ = r² + α²/3
(⟨cos²θ⟩ = 1/3), u = Δ/Σ̄, Φ_bg = ½ln(1 − 2Mr/Σ̄). The reduced
background is not vacuum: it carries effective fields
(ρ_bg, p_r,bg, p_t,bg) from its own Einstein tensor, and the
shell is re-solved in the total reduced geometry by the exact
H4 pattern (prescription on top of the background fields,
conservation solve, shooting on s; clean secant solves,
residuals ≤ 1e-14). Frame dragging does not enter a static
spherical reduction — stated scope limit. Grid: M_bg ∈
{1, 2, 2.5, 3, 3.5, 4} × a* ∈ {0.3, 0.6, 0.9} × both variants.

**Result — spin does not move the shell's DEC crossing.**
On the shell's own (difference) tensor — the H4/AdS-convention
judge whenever the background carries a tensor of its own —
core DEC at M_bg = 4 is **−5.4e-5 … −6.8e-5 at every a* in
both variants** (Schwarzschild: −5.71e-5; spin slightly
*worsens* the equatorial rows), and the DEC crossing stays at
M_bg = **2.54–2.60** (control 2.55). The s(M_bg) amplification
mechanism is untouched by spin at this order: s(4) = 15.6–17.9
across variants/spins vs 16.10 Schwarzschild.

**The one apparent exception, and why it is not a pass.**
Core *total* tensor at (averaged, a* = 0.6, M_bg = 4): DEC
+8.98e-6, all core ECs > 0, Type-I 1.0; total-tensor crossings
rise to 2.86–3.81 across the grid. But: (i) the margin is a
core-local cancellation against the reduction's effective
background fields, which are **themselves EC-illegal at the
inner edge** (background-only core NEC = −6.7e-5 for that row;
−4.1e-4 equatorial a* = 0.9) — the reduction loads Kerr-shaped
metric functions with a large negative p_t,bg that has no
counterpart in true Kerr, which is vacuum; (ii) the same row
fails on the full band (band total NEC −3.1e-4), where the
shell tapers off and the background illegality stands alone.
Crediting that row would be crediting a reduction artefact —
reported in full in the JSON (`core_total`, `bg_core`,
`band_total` per row), not counted.

**NOT COMPUTABLE (scoped).** A genuine axisymmetric Kerr
re-solve (shell equilibrium in Boyer–Lindquist geometry):
no axisymmetric shell solver exists in the programme; the FD
judge audits metrics but cannot construct the re-equilibrated
shell in one. This is the reopening condition. The verdict
rests on the sanctioned reduction, which was computable.

**β\* ceiling — labelled SCALING ARGUMENT (not a computation).**
Phase 17 record: SEC deficit at β = 0.0275 is −2.5e-5 (h = 0.15,
two auditors) at r = 10.5, where the Finalist-A wall density is
ρ = 5.38e-5 (computed in-run from the windowed profile). The
maximal rotational energy density at the registered speed cap,
u_rot = ½ρv² at v = 0.5, is 6.72e-6 — **0.27× the deficit**
(short ~4× at the first illegal point, ~30× short of the
β = 0.1 deficit scale ~2e-4). And by part (a), rotating the
wall's matter changes none of its Hawking–Ellis eigenvalues,
so u_rot is not even an available SEC supply channel; frame-
dragging corrections to the required tensor are O((Ωa)²) ≤ 0.25
of the local stress scale with geometry-fixed sign. Rotation
does not lift β\* out of (0.025, 0.0275].

**Deciding terms:** difference-tensor DEC at M_bg = 4
(−5.4e-5…−6.8e-5, all spins/variants); u_rot/deficit = 0.27
for the ceiling.

**Follow-up experiment:** an axisymmetric re-solve — prescribe
the Finalist shell on Kerr Boyer–Lindquist slices and solve
the (t, r, θ) conservation system with the FD judge as
auditor — targeted at the one thing the reduction cannot see:
whether frame dragging (absent here by construction) couples
to the shell's tangential pressure at O(a*) strongly enough
to dent s(M_bg). The reduction predicts it cannot (s is set
by the diagonal geometry, where spin enters only at O(a*²)
through Δ, measured above to move DEC by ≲ 20%).

---

## Files
- Script: `phase33/p332_rotation.py`
- Results: `phase33/results/p332_results.json` (all rows:
  control table + gate, Kerr rows with s / core-total /
  core-diff / band-total / background-core margins, part (a)
  scans, eigenvalue checks, Model-G λ table, β\* pricing)
- This memo: `phase33/results/p332_memo.md`
- CHECKPOINT33.md not edited.
