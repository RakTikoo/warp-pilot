# P253-1 MEMO — THE SPINOR SOURCING TEST

**Verdict (verbatim, registered form): SPINORS BREAK THE IDENTITY**

Registration: `phase253/work/p2531_registration.md` (written
before any deciding computation). Driver:
`phase253/work/p2531_run.py`. Independent checker:
`phase253/work/p2531_check.py` (**28/28 PASS**, Weyl gamma
representation, independently coded stress tensor). All
verdict-carrying numbers: `phase253/results/p2531_results.json`
and `phase253/results/p2531_check.json`. Frame of record:
Phase 166 pin, Gate-19-corrected tensor lineage (T_req imported
from Phase 235 via P250-2's stored control-exact site rows),
programme venv, float64. Bounded local run. Nothing appended
to the ledger; nothing outside phase253/ edited.

## Controls (run first; PASS, diff-0.0 class)

Stored Phase 235 rows read back exactly (E_neg = −2.590291375073908
at β = 1.1, −4.216328950794798 at β = 1.5; NEC min
−0.00378336198802795; WEC min −0.036210271834070086). The stored
Eulerian That at every deciding site, contracted with the site's
stored worst direction k* = (1, n̂), reproduces the stored NEC
worst value to ≤ 5×10⁻¹⁸ (worst site: −0.003801760529158262 vs
stored −0.0038017605291582623; r = 12.5: −0.003755770589968388;
r = 15.0: −0.0016384261964676222; β = 1.5: −0.004881620592011806).
Machinery cross-checks inside the item: the direct T_ab
contraction and the independent N-matrix path agree on every
spinor read to ≤ 1e-12 (single modes: 19.975791617137634 vs
19.97579161713763; deciding configuration: −10.878491901602604
vs eigenvalue −10.878491901602544); the Weyl-representation
checker reproduces the deciding value as −10.8784919016026.
(One index-position defect in the first driver draft's
full-tensor builder was caught by exactly this cross-check,
fixed, and the fixed paths agree; the checker is the second,
independent implementation.)

## 1. The algebra — why spinors are not a sum of squares

Conventions and health as registered: η = diag(+1,−1,−1,−1),
L = ψ̄(iγ·D − m)ψ with the correct-sign kinetic term (ghost =
overall sign flip, excluded, used only as a control — T_ab is
linear in that sign, so the ghost sector trivially flips every
read below and buys nothing healthy),
T_ab = (i/4)[ψ̄γ_(a D_b)ψ − (D_(aψ̄)γ_b)ψ] − g_ab·L.

**Null contraction (exact, no field equations):** for null k,
g(k,k) = 0 kills the −g_ab·L term identically — the same
field-equation-free first step as P250-2's radiation identity —
leaving the current/derivative bilinear
  T(k,k) = (i/2)[ ψ̄(γ·k)(γ·k contracted derivative) ] =
  (i/2)[ ψ̄(γ·k)(k·D ψ) − ((k·D)ψ̄)(γ·k)ψ ].
Unlike the 2-form/scalar/radiation cases, what remains is NOT
a square: it is a bilinear in two independent objects, ψ and
k·Dψ. Structurally: (γ·k)² = (k·k)I = 0 (SymPy-verified
identically), so γ·k is nilpotent of rank 2, and
B := γ⁰(γ·k) is Hermitian with eigenvalues {0, 0, 2, 2}
((α·n̂)² = I, trace 0) — positive semidefinite, with a
two-dimensional kernel: the half of spinor space that γ·k
annihilates.

**Tier A (off shell — sign structure only, not deciding):**
at fixed ψ, T(k,k) is LINEAR in the jet ξ = (k·D)ψ, hence
indefinite: the registered instance gives T(k,k) = −2.866×10⁻³
for ξ₀ and +2.866×10⁻³ for −ξ₀. No off-shell sum-of-squares
identity exists for spinors — in sharp contrast to Phase 31's
sectors, whose identity holds off shell. The field equations
ARE therefore needed for any sign conclusion, and Tier B
imposes them.

**Tier B (on shell — deciding).** Registered family: finite
superpositions of positive-frequency plane waves,
(slashed p − m)u = 0, u†u = 2E, p⁰ = +√(|p|²+m²) only
(negative-frequency modes excluded by registration, so the
result cannot be bought with the classical negative-energy
modes). For one mode,
  T(k,k) = (k·p)·ū(γ·k)u = (k·p)(k·j),  j^a = ψ̄γ^aψ,
with (k·p) > 0 (future timelike p, future null k) and
ū(γ·k)u = u†Bu ≥ 0 (B PSD) — a single mode obeys the identity:
verified numerically (T(k,k) = +19.976, +0.826, +131.969 for
the three registered probe modes; Dirac residuals ≤ 2.5×10⁻¹⁵).
For a superposition the contraction is the Hermitian form
  T(k,k) = Σ_ij c_i* N_ij c_j,   N = A ∘ C,
  A_ij = u_i† B u_j  (a Gram matrix — PSD),
  C_ij = ½(f_i + f_j),  f_j = k·p_j.
**The deciding fact: C is not positive semidefinite when the
modes have different f = k·p** (for the deciding pair below,
det C = −28.0 < 0), so the Schur product theorem does not
apply, N need not be PSD — and it is not. The negativity is
an INTERFERENCE effect: modes whose momenta project very
differently onto k (f spanning 0.81 to 11.40 in the deciding
configuration) beat against each other through the
rank-2 operator B, and the cross terms — weighted by the
arithmetic mean ½(f_i+f_j) rather than the geometric structure
a Gram form would need — overwhelm the (individually
non-negative) diagonal. Massive and massless cases do not
differ in kind: both break (below).

This is the same structural object Phase 72 met at throats —
T^ℓ_ℓ = 4(P′Q − PQ′)/F₁, a Wronskian — seen here in momentum
space: a derivative bilinear whose sign is carried by
interference, not by any square.

## 2. The deciding configuration and the site prices

Best configuration found in the registered family (randomised
search over mode pairs/triples, subordinate to the algebra
above; eigenvector of N for its mode set), m = 1, at the
β = 1.1 worst site (r = 12.84), Σ|c_j|² = 1, u†u = 2E:

| mode | p (Eulerian frame) | E | f = k*·p | c |
|---|---|---|---|---|
| 1 | (1.742, 0.261, 1.564) | 2.559 | 0.815 | 0.5466 |
| 2 | (−5.320, −2.581, −0.945) | 6.071 | 11.401 | 0.1041 − 0.3265i |
| 3 | (−1.404, 0.741, −1.232) | 2.245 | 3.647 | 0.5321 − 0.5483i |

(full spinors in the results JSON). Reads at unit normalisation:
- **T_spinor(k*,k*) = −10.8785 < 0** — Dirac residuals
  ≤ 3.5×10⁻¹⁵ per mode (driver), < 1e-10 in the Weyl checker;
  each mode individually has T(k*,k*) ≥ 0 (checker), so the
  negative sign is purely the interference term.
- **ρ_spinor = T(e_t,e_t) = +2.2404 > 0** and ψ†ψ = +2.1936 at
  the site point: the configuration's local Eulerian energy
  density is POSITIVE while its null contraction along k* is
  negative. The sign leg is not bought with negative density
  at the point.
- Massless case: best m = 0 configuration gives
  T(k*,k*) = −8.9847 per unit Σ|c|², ρ = +8.8378 — same verdict.
- Randomised corroboration (P250-2 style, subordinate):
  2000 random two-mode draws at m = 1: 0.4% have T(k*,k*) < 0,
  min −1.116, median +18.70 — negativity is generic but not
  typical; it lives where the f-spread and B-overlap align.

**Site pricing** (same configuration, each site's own k*;
T_spinor(k*,k*) per unit Σ|c|² ≈ −10.88 at all four sites —
the k* directions are near-parallel across the band):

| site | T_req(k*,k*) | T_spinor (unit) | amplitude² s² for FULL deficit | ρ_spinor at s² | ψ†ψ at s² |
|---|---|---|---|---|---|
| β=1.1, r=12.84 | −0.0038018 | −10.8785 | 3.495×10⁻⁴ | +7.83×10⁻⁴ | 7.67×10⁻⁴ |
| β=1.1, r=12.5 | −0.0037558 | −10.8793 | 3.452×10⁻⁴ | +7.73×10⁻⁴ | 7.57×10⁻⁴ |
| β=1.1, r=15.0 | −0.0016384 | −10.8604 | 1.509×10⁻⁴ | +3.38×10⁻⁴ | 3.31×10⁻⁴ |
| β=1.5, r=13.23 | −0.0048816 | −10.8775 | 4.488×10⁻⁴ | +1.005×10⁻³ | 9.84×10⁻⁴ |

Reading: at unit normalisation the configuration carries
**2861× the worst site's entire NEC deficit** along k*; scaled
down by s² = 3.49×10⁻⁴ (amplitude s = 0.0187) it carries the
full deficit exactly, at a local spinor density ψ†ψ =
7.7×10⁻⁴ and a POSITIVE local energy density +7.8×10⁻⁴
(≈ 8× |ρ_req| at the site, of the healthy sign). On the sign
leg, spinors are not amplitude-starved: the deficit is small
change against the interference term's natural size. What
fraction of the deficit it can carry is therefore: **all of
it, along the deciding direction, at small amplitude** —
subject to the fences in §4, which are substantial.

## 3. Scope — where the classical/quantum line enters

The pose is classical throughout, in the same sense as
Phase 31's and P250-2's tests: spinor components are commuting
c-number fields, T_ab is the classical symmetrised tensor, and
the verdict is a statement about that tensor. The
Grassmann/quantum dependence enters at exactly two named
steps, neither of which is used by the deciding configuration:
(i) NEGATIVE-FREQUENCY modes — a commuting classical Dirac
field's negative-frequency modes carry negative energy, which
is the textbook reason the field is quantised with
anticommutators; this item EXCLUDED them from the deciding
family by registration, and the exhibited configuration uses
positive-frequency modes only, with positive local density at
the site point. (ii) The VALUE of a Grassmann bilinear at a
point is an even Grassmann element, to which "sign" does not
apply until a state/expectation is chosen — so a
Grassmann-classical restatement of the question is not
well-posed without quantisation; in the quantised theory
⟨T(k,k)⟩ < 0 locally for fermions is unremarkable (fermionic
Casimir/squeezed-state NEC violations) but is fenced by
quantum-inequality bounds this item does not price. Because
the programme's identity question (Phase 31, P250-2) is posed
and answered in the classical theory, and the classical pose
here is clean and explicit, the third verdict form does NOT
fire: the ambiguity is confined to steps the verdict does not
take. Any future quantum restatement is a different item.

## 4. Verdict, Phase 72 scope correction, and fences

**SPINORS BREAK THE IDENTITY** — the registered deciding
clause fires: a healthy (correct-sign kinetic term, m² ≥ 0,
on-shell, positive-frequency) classical Dirac configuration
with T(k*,k*) = −10.8785 per unit Σ|c|² < 0 exists at every
deciding site of the Phase 235 drive, exhibited above with an
independent-representation checker at 28/28. The Phase 31
sign obstruction is therefore NOT complete over the library:
2-forms, canonical scalars and radiation are closed; spinors
are open. The drive's sourcing question REOPENS on this
sector — on the sign leg only, per the fences below.

**Phase 72 scope correction (stated here; Phase 72's files
not edited):** Phase 72's KILL was a THROAT closure, on two
grounds — (i) the published Einstein–Dirac solutions fail the
full EC set / normalizability bars, (ii) the programme's
frozen-shape throat system dies by a domain obstruction off
the throat. Neither ground is a sign identity, and Phase 72's
own audit in fact exhibits on-shell Dirac NEC violation
(BSKR S-A: NEC1 = ((Q_e/r₀)²−1)/(8πr₀²) < 0 at the throat).
Any reading of the record — including any ledger phrasing —
that treats Phase 72 as closing SPINOR SOURCING in general
overstates its scope: it closes spinor-supported THROATS at
its registered bars. The correct scope line is: spinors were
closed for throats in Phase 72 (EC/domain grounds), and are
now shown OPEN on the sign leg for drive sourcing by this
item. The configurations do not overlap in kind: Phase 72's
are self-gravitating throat solutions; this item's is a local
test-field configuration in the drive site's tangent frame —
so no Phase 72 number is contradicted; only the scope
reading needs the correction.

**Fences (on the face):** this verdict reopens the sourcing
QUESTION on the spinor sector; it does not source the drive.
Not claimed, still open: (a) the full tensor match — T_req is
non-Type-I and flux-carried (Phase 235's type obstruction,
≥ 34% of norm from every real-spectrum tensor), and a Dirac
field's full T_ab at the site was not fitted to T_req, only
its deciding null contraction was matched; (b) global
existence — the exhibited configuration is a tangent-frame
plane-wave superposition at the site; extending it to an
on-shell Dirac field on the whole Alcubierre background
(spin connection, mode mixing, normalizability — the very
point Phase 72's S-A failed) is untested; (c) standalone EC
health beyond the sign leg and the positive pointwise density
reported (DEC/SEC of the spinor field, and its behaviour away
from the site point, unread); (d) backreaction, budget and
QI pricing of any full sourcing attempt (the s² densities in
§2 are local pointwise reads, not a shell integral);
(e) the quantum restatement (§3).

Reopening condition (standing pattern, inverted for a BREAK
verdict): this item's verdict would be overturned by a proof
that on-shell, positive-frequency classical Dirac
superpositions have T(k,k) ≥ 0 for all null k — such a proof
would have to defeat the N = A∘C indefiniteness above and the
exhibited configuration — or by a health condition, stated
independently of this drive, that excludes multi-mode
interference configurations of the registered family while
admitting single modes. None is known to this programme.

Files: `work/p2531_registration.md`, `work/p2531_run.py`,
`work/p2531_check.py`, `results/p2531_results.json`,
`results/p2531_check.json`, this memo. Internal only.
