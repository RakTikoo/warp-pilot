# P72-1 MEMO — Spinor-supported throats (Einstein–Dirac)

## Plain-language summary

Spinors really are different from every field this programme
has killed before: a Dirac field's stress tensor is not a sum
of squares, so the Phase-31 identity does not touch it, and at
a wormhole throat a Dirac field genuinely supplies the
negative radial pressure combination a throat needs. That
part of the literature's claim is true, and this run verified
it from the published formulas.

It still does not produce a wormhole that passes this
programme's bars, for two separate reasons. First, the one
published solution that can be reconstructed exactly (the
massless Blázquez-Salcedo–Knoll–Radu solution) violates the
null and dominant energy conditions at its throat by a large,
exact margin — the "no exotic matter" headline means "no
phantom field was put in by hand", not "the energy conditions
hold" — and its spinor never switches off at infinity, so it
is not a localised particle-like state at all. The massive
numerical solutions in the same papers cannot be rebuilt
from what was published (and the symmetric ones were
independently shown not to solve the equations at the
throat). Second, when we posed the programme's own
throat system with a Dirac source on the standard throat
shapes, the throat equations close only if the fermion is
massive — and every closing solution then falls apart
immediately outside the throat: the field equations stop
being satisfied within a ten-thousandth of a throat radius,
and the spinor itself blows up a few to a few dozen throat
radii out. The throat can be closed; the neighbourhood
behind it cannot, on these backgrounds.

**VERDICT (registered form): KILL.** Both registered kill
clauses are met: (i) every audited published solution fails
at least one full bar by a converged margin; (ii) the throat
system admits no closing datum at the massless registered
points, and at the massive points closes only with a named
domain obstruction (solution-grade breach at
R/r₀ = 1.000026–1.000113 and spinor blow-up at
R/r₀ = 5.9–69.7, both before 10³r₀). Checker: 40/40 PASS
(`work/p721_check.py` over `results/p721_results.json` +
`results/p721_second_path.json`).

## Machinery gates (passed before verdict numbers)

- G1: FD Riemann formulas reproduce the P23-3 Ellis
  traveller tidal 0.010101/r₀² at v = 0.1c (got 0.01010100).
- G2: the exact solution S-A satisfies the paper's Einstein
  (G = 2T, T derived here from EPJC (2.5) by SymPy), Dirac
  (3.11) and Maxwell (3.12) equations with max residuals
  ~1e-14 on ℓ ∈ [0.05, 100], for Q_e ∈ {0.25, 0.5} and
  c₀ ∈ {0.5, 1, 2} — the transcription and the derived
  Dirac stress tensor (T^t_t = −4w(P²+Q²)/F₀,
  T^ℓ_ℓ = 4(P′Q−PQ′)/F₁, T^θ_θ = 2κ(Q²−P²)/F₂) are
  validated by the solution itself. (One transcription
  defect was caught and fixed by this gate: the ℓℓ
  Einstein component's +ℓ²F₀ term.)
- G3: GR gate — spinor off, Ellis shape: ρ_dem(r₀) =
  −1/(8πr₀²), (ρ+p_r)_dem(r₀) = −1/(4πr₀²), exact.
- Conservation (reported, not assumed): for S-A the Dirac
  and Maxwell residuals above are ≤ ~1e-13, and the
  Einstein residuals ≤ ~1e-14; ∇^μT_μν = 0 follows from
  those equations by the Bianchi identity, so the
  conservation read inherits the ~1e-13 level. In part
  (ii)'s extension the r–r Einstein equation is carried
  as the independent residual (it is the breach quoted
  below).

## Part (i) — audit of the published solutions

Audited set (fixed in `results/p721_run_record.md` before
numbers): S-A = BSKR exact massless ungauged solution
(arXiv:2010.07317; EPJC 82, 533 (2022) App. D), Q_e/r₀ ∈
{0.25, 0.50, 0.75, 0.90}, κ = +1, c₀ = 1 (residuals are
c₀-independent — the equations hold for the whole c₀
family). Its throat shape slope is β = (Q_e/r₀)². S-B =
BSKR numerical symmetric massive solutions: **NOT
AUDITABLE** (no profiles or tabulated data published —
figures only), and on the published record they are not
solutions at the throat at all (Danielson, Satishchandran,
Wald & Weinbaum, arXiv:2108.13361: metric not C³ at the
throat, a spurious Dirac source and an extra charged
shell implied by the matching). S-C = Konoplya–Zhidenko
asymmetric solutions (arXiv:2106.05034): **NOT AUDITABLE**,
gap named in the run record (throat series coefficients
unpublished; six-digit throat data cannot start an
integration off the singular throat point to audit grade).

### S-A audit table (r₀ = 1 units; EC margins in 1/(8π) scale
### as tabulated, full domain R ∈ [r₀, 10³r₀], fine grid;
### coarse grid agrees)

| Q_e/r₀ | NEC1 min (ρ+p_r) | NEC2 min (ρ+p_t) | WEC min (ρ) | SEC min (ρ+p_r+2p_t) | DEC_r min | DEC_t min | worst at |
|---|---|---|---|---|---|---|---|
| 0.25 | **−0.03730** | +1.7e-11 (sat.) | +2.5e-15 (sat.) | −1.1e-12 (sat.) | **−0.03730** | **−0.01865** | throat |
| 0.50 | **−0.02984** | +8.9e-12 (sat.) | +1.0e-14 (sat.) | −2.7e-13 (sat.) | **−0.02984** | **−0.01492** | throat |
| 0.75 | **−0.01741** | +2.5e-12 (sat.) | +2.2e-14 (sat.) | −1.2e-13 (sat.) | **−0.01741** | **−0.00870** | throat |
| 0.90 | **−0.00756** | +4.0e-13 (sat.) | +3.2e-14 (sat.) | −8.8e-14 (sat.) | **−0.00756** | **−0.00378** | throat |

- The NEC1/DEC_r failure is exact, not numerical: at the
  throat ρ + p_r = ((Q_e/r₀)² − 1)/(8πr₀²), reproduced by
  the grid to 1e-9 (checker). This is the flare-out
  combination — a GR throat must violate it — but the
  registered audit bar is the full EC set read, and the
  authors' "without exotic matter" framing does not
  survive it: the total (Dirac + Maxwell) stress tensor
  violates NEC and DEC at the throat at every audited
  parameter value. DEC_t also fails at the throat
  (p_t > ρ there). NEC2, WEC and SEC saturate (minima
  ~1e-11–1e-15, at infinity / roundoff level — reported
  as saturation, not failure).
- Health/scope: the spinor does not decay —
  P(∞) = −1/(8c₀(1+(Q_e/r₀)²)), Q(∞) = +same (analytic;
  numeric matches to 1e-6): the wave function is not
  normalizable and the one-particle condition cannot be
  imposed (the authors state this themselves). The
  configuration is not a localised state at any scale.
- Traversability (Phase-23 bars, confirmed in the run
  record): radial tidal at the throat = (Q_e/r₀)²/r₀²
  exactly (0.0625 / 0.25 / 0.5625 / 0.81 per r₀²), so the
  1 g bar needs r₀* = 3.38e7 / 6.77e7 / 1.02e8 / 1.22e8 m.
  At r₀* the crossing bars PASS easily (proper
  25.7 / 53.1 / 85.5 / 112 s; external 26.8 / 62.6 / 129 /
  251 s, vs 1 day) — but the ADM mass there is
  2.8e6 / 1.9e7 / 5.2e7 / 7.7e7 Jupiter masses, and the
  non-normalizable spinor problem is scale-free. At
  r₀ = 1 m the tidal gradient exceeds the bar by ~16
  orders (crossing ~1e-6 s passes; mass 0.08–0.63 M_J).
  Traversability is not the deciding failure — the EC
  set and normalizability are — but the price of the
  tidal bar is stated, not hidden.

## Part (ii) — θθ-complete throat system with a Dirac source

System as registered (run record §4): pure Einstein–Dirac,
two-spinor singlet ansatz (EPJC (3.7)), Φ = 0, shapes
Ellis (β = −1) and √ (β = +1/2), μr₀ ∈ {0, 0.2, 1.0},
unknowns (P₀, Q₀, w) at the throat; clauses {t–t, r–r,
θθ, EoM(s) (Dirac equations slaving P′(0), Q′(0)), cone
(= ε_r-flip junction consistency — verified consistent
for the mirror extension), solution-grade, health
(Noether density ∝ P₀²+Q₀² ≥ 0 ✓), throat-EC}.

Throat algebra (derived, then solved two ways): with
S = P₀²+Q₀² and D = P₀²−Q₀², the clauses reduce to
  t–t: wS = β/(8r₀²);
  θθ: −D = (1−β)/(8r₀)  (κ = +1);
  r–r: 4[D + wS] + 8μP₀Q₀/r₀ = −1/(2r₀²),
which collapse to the single deciding relation
**μ P₀Q₀ = −β/(8r₀)**.

| point | closing datum (P₀, Q₀, w r₀) | throat residuals | domain |
|---|---|---|---|
| Ellis, μ=0 | none — r–r residual floor 2\|β\| = 2.0 (G−2T units), parametrised scan | — | — |
| √, μ=0 | none — floor 2\|β\| = 1.0 | — | — |
| Ellis, μ=0.2 | (0.715805, 0.873142, −0.098058) | ≤ 8.9e-16 | breach R = 1.000050r₀; blow-up R = 69.7r₀ |
| Ellis, μ=1.0 | (0.227545, 0.549342, −0.353553) | ≤ 2.2e-16 | breach R = 1.000026r₀; blow-up R = 11.5r₀ |
| √, μ=0.2 | (0.531798, −0.587630, +0.099504) | ≤ 2.2e-16 | breach R = 1.000051r₀; blow-up R = 35.0r₀ |
| √, μ=1.0 | (0.196538, −0.318005, +0.447214) | ≤ 2.2e-16 | breach R = 1.000111r₀; blow-up R = 5.9r₀ |

- Independent second path (fsolve on the raw G−2T
  residuals from perturbed starts): data agree with the
  analytic solve to ≤ 2.8e-11 (bar 1e-8); RK4 extension
  reproduces every breach radius to < 1e-3 relative.
- Throat-EC at the closing data (geometric values, any
  source on these backgrounds): Ellis — ρ = −1/(8πr₀²)
  (WEC fails at the throat, a property of the Ellis
  shape), ρ+p_t = 0 (saturates); √ — ρ = +1/(16πr₀²),
  ρ+p_t = 3/(32πr₀²), DEC_t margin +1/(32πr₀²); radial
  NEC is the flare-out identity on both, per the run
  record's registered interpretation.
- Domain obstruction (named, per branch — the same for
  all four closing rows): on the frozen Φ = 0
  backgrounds the Dirac field's growing mode is excited;
  the carried r–r (solution-grade) residual crosses the
  0.02 bar at R/r₀ = 1.000026–1.000111 — a Phase-48-type
  near-throat domain death, sharper than P42-3's 1.0033 —
  and |P|,|Q| grow without bound, passing 1e6× their
  throat norm at R/r₀ = 5.9–69.7 and overflowing before
  10³r₀. No closing row extends to 10³r₀.

## Verdict

**KILL** (registered form). Clause (i): the only audited
published solution family (S-A, four parameter values)
fails the NEC and DEC bars by exact, converged margins
(min NEC1 = −(1−(Q_e/r₀)²)/(8π), up to −0.0373 at
Q_e/r₀ = 0.25); S-B and S-C resolve NOT AUDITABLE with
gaps named (S-B additionally refuted on the published
record). Clause (ii): at μ = 0 there is no closing datum
at either registered shape (residual floor 2|β|); at
μ ∈ {0.2, 1.0} the throat closes at ≤ 1e-16 (second path
≤ 2.8e-11) but only with the named domain obstruction
above. No SCAN SIGNAL: no datum both closes C and
extends to 10³r₀.

## Anatomy

1. Why the spinor escapes Phase 31/39 and still fails:
   T^ℓ_ℓ at a throat is 4(P′Q−PQ′)/F₁ — a Wronskian, not
   a sum of squares — so the radial NEC can and does go
   negative. What binds instead is (a) the EC set as a
   whole (DEC fails wherever NEC1 does, and the exact
   solution's tangential pressure exceeds its density at
   the throat), and (b) the domain: the same Wronskian
   structure that closes the throat is carried by a
   growing mode off it.
2. The mass term is the throat's only lever: after the
   Dirac equations slave P′(0), Q′(0), every throat
   clause collapses to μP₀Q₀ = −β/(8r₀). A massless
   Dirac field cannot close ANY of the registered shapes
   (it would need β = 0 — no flare-out). This is a
   structural statement about the Φ = 0 frozen-shape
   system, scope stated.
3. The exact solution evades (2) by not living on these
   backgrounds: it carries Φ ≠ 0, a source-free Maxwell
   field supplying p_r at the throat, and β = (Q_e/r₀)²
   ∈ (0,1) — and pays with a non-normalizable spinor.
   The frozen-background death in (ii) is therefore
   partly a background-rigidity statement; see F2.

## Follow-ups (Failure Protocol)

- F1 (reopening for S-C): reconstruct the
  Konoplya–Zhidenko throat series coefficients from
  their eqs. (31) + (36)–(37) (a SymPy series solve in
  the four throat parameters), then integrate and audit
  their Table I rows at programme bars. This is the one
  published family that could still change clause (i).
- F2 (reopening for (ii)): coupled extension — free
  Φ(r) and b(r) with the Dirac source (the FU-P484-B2
  pattern): does the near-throat breach survive freeing
  the shape, or was it a frozen-background artefact?
  The exact solution's existence at β ∈ (0,1), Φ ≠ 0
  says the coupled system has somewhere to go; its EC
  and normalizability prices would then be the audit.
- F3: β-scan of the throat algebra: the closing
  relation μP₀Q₀ = −β/(8r₀) plus S ≥ |D| bounds which
  (β, μ) admit throat data at all on Φ = 0 backgrounds
  — a one-page analytic map, no scan budget needed.

## C12 accounting

All configurations are pre-existing static throats; no
formation mechanism was computed and no transport claim
is made or implied. The only construction-inclusive
numbers are the scale/mass prices stated in the audit
table (r₀* ~ 1e8 m, M ~ 1e7 M_J for the tidal bar) —
there is no formation step in this item to book.

Files: `results/p721_run_record.md` (forms fixed before
numbers), `results/p721_results.json`,
`results/p721_second_path.json`; scripts
`work/p721_lib.py`, `work/p721_derive_G.py`,
`work/p721_T.py`, `work/p721_validate.py`,
`work/p721_main.py`, `work/p721_second.py`,
`work/p721_check.py` (40/40 PASS). Internal only;
nothing uploaded.
