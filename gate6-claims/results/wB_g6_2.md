# GATE-6 — Worker W-B report: Claim G6-2 (P42-1, Φ≠0 inertness theorem)

**Worker:** W-B · **Claim:** G6-2 only · **Date:** 2026-11-22
**Correctness verdict: REPRODUCED**
**Novelty verdict: PARTIALLY KNOWN** (known part cited exactly below; novel part delimited in one sentence)
**Gate verdict: UPLOAD-READY AFTER RESTATEMENT** — the algebra is exact and
reproduced, but the claim as tasked overstates the "unification" of P35-4;
the exact restated wording in §4 must replace it. No other weakening is needed.

Nothing uploaded, no external contact. All computation float64 / exact symbolic.

---

## 1. Correctness — independent THIRD path (done first)

### 1.1 Route (structurally different from both Phase-42 derivations)

Neither `phase42/p421_derivation.py` (full-Christoffel, MT functions b, Φ)
nor `phase42/p421_derivation2.py` (diagonal-metric second path) was re-run
or copied. Fresh code: **`gate6/wb_g62_derivation.py`**.

- General diagonal parametrisation with **independent lapse and radial
  functions**: ds² = −N(r)²dt² + dr²/S(r) + r²dΩ², with N, S, F kept as
  unspecified sympy functions (Φ enters only at the end as Φ′ = N′/N;
  S enters only at the end as S = 1 − b/r).
- Einstein tensor, □F and ∇∇F computed by a generic index-loop tensor
  routine written for this gate.
- The throat limit is taken by a **series in ε = r − r₀** (S = (1−β)ε/r₀ + …,
  N = 1 + Φ′₀ε + …, F = F₀ + F′₀ε + F″₀ε²/2), not by the Phase-42
  substitution map.

### 1.2 Computed facts (not assumptions)

General-(N,S) outputs of the run:

- G^t_t = (rS′ + S − 1)/r² ;  G^r_r = [2rSN′ + N(S − 1)]/(r²N)
  — the Φ′ piece of G^r_r is 2SN′/(rN) = **2AΦ′/r: it carries S (= A)**.
- □F = SF″ + F′S′/2 + SF′N′/N + 2SF′/r.
- ∇^t∇_tF = SF′N′/N = **AΦ′F′** — and □F contains exactly +AΦ′F′ as its
  third term, so in the t–t channel the two **cancel identically, as a
  computed output**: □F − ∇^t∇_tF = SF″ + F′S′/2 + 2SF′/r (no Φ′ term).
- □F − ∇^r∇_rF = SF′(Φ′ + 2/r) — the F″ terms cancel identically at
  general r; **coefficient of F″ in 8πp_r,dem is exactly 0**, and in
  8πρ_dem it is exactly **−S (= −A)**.
- General-r pair, differences against the claimed formulas **exactly 0**:
  - 8πp_r,dem = −Fb/r³ + A[F′Φ′ + 2FΦ′/r + 2F′/r]  — **DIFF = 0**
  - 8πρ_dem = Fb′/r² − AF″ − 2AF′/r − A′F′/2  — **DIFF = 0**
  (translation used: b/r³ = (1−S)/r², b′/r² = (1−S)/r² − S′/r.)
- Throat limits by series, differences against the claim **exactly 0**:
  - 8πρ_dem(r₀) = F₀β/r₀² − (1−β)F′₀/(2r₀), i.e.
    ρ_dem(r₀) = F₀β/(8πr₀²) − (1−β)F′₀/(16πr₀) — **DIFF = 0**
  - 8πp_r,dem(r₀) = −F₀/r₀², i.e. p_r,dem(r₀) = −F₀/(8πr₀²) — **DIFF = 0**
  - R(r₀) = 2β/r₀² − (1−β)Φ′₀/r₀ — **DIFF = 0** (in R, Φ″₀ and Φ′₀² enter
    only S-multiplied; Φ′₀ survives only via the −S′Φ′ cross term).
  - □φ at the throat = (1−β)φ′₀/(2r₀) (all other terms carry S = 0), so
    the scalar EoM at r₀ is exactly the memo's form, with Φ′₀ entering
    only through the R(r₀) term above — an EoM lever on the flux, in the
    combination F_φ0·R(r₀)/(16π). Φ″₀ enters no throat quantity.

Every mechanism element in the claim — A-factor on every radial-derivative
term (AΦ′₀F′₀, 2AF₀Φ′₀/r₀ explicitly), the □F vs ∇^t∇_tF cancellation,
F″₀ entering neither channel, Φ′ surviving only in the EoM via R(r₀) —
is exhibited by this third path as a computed fact.

### 1.3 Numeric spot check (independent of the symbolic route)

Fresh code: **`gate6/wb_g62_numeric.py`** (+ `wb_g62_numeric.json`).
A float64 numeric tensor evaluator (concrete analytic profiles and their
derivatives; field equations evaluated at r = r₀+δ for
δ = 0.04, 0.02, 0.01, 0.005, 0.0025, r₀ = 1, linearly extrapolated δ→0).
One evaluator bug was caught and fixed during the run (G^t_t initially
coded −b/r³, corrected to −b′/r² per §1.2; p_r was unaffected and already
matched, ρ then matched too — recorded here as run honesty).

Controlled set C1–C3: **same** √-shape (β = +1/2), **same** φ₀ = 0.9,
ξ = 1.5 ⇒ **same F₀ = 2.215**, but Φ′₀, F′₀, F″₀ all varied:

| case | Φ′₀ | F′₀ | F″₀ | ρ extrap. | ρ canonical | err | p_r extrap. | p_r canonical | err |
|---|---|---|---|---|---|---|---|---|---|
| C1 | +0.50 | +1.080 | +2.100 | +0.033292 | +0.033323 | 3.1e-05 | −0.088029 | −0.088132 | 1.0e-04 |
| C2 | −1.70 | −2.970 | −0.690 | +0.073665 | +0.073609 | 5.6e-05 | −0.088129 | −0.088132 | 3.5e-06 |
| C3 | +2.30 | +5.400 | +19.560 | −0.009388 | −0.009649 | 2.6e-04 | −0.088173 | −0.088132 | 4.1e-05 |
| E1 (Ellis, β=−1, ξ=2, F₀=1.72) | −2.00 | +1.680 | +4.360 | −0.135114 | −0.135282 | 1.7e-04 | −0.068799 | −0.068437 | 3.6e-04 |

Deciding numbers: across C1–C3, F′₀ spans −2.97…+5.40, F″₀ spans
−0.69…+19.56, Φ′₀ spans −1.7…+2.3, yet the extrapolated p_r,dem(r₀)
spread is **1.4e-04** around the single canonical value −F₀/(8π) =
−0.088132 — no dependence on F′₀/F″₀/Φ′₀, as claimed. ρ matches the
canonical F′₀-dependent formula in every case. All errors ≤ 3.6e-04,
consistent with linear extrapolation over the δ-ladder.

### 1.4 Unification clause — judged at statement level

- **Phase 40 (Φ = 0): TRUE special case.** Setting N′ = 0 (Φ′₀ = 0) in
  §1.2 leaves the general-r pair and both throat formulas unchanged in
  form, and the throat pair is exactly Phase 40's canonical pair,
  including the cone: supply at the throat is ρ_φ = V₀, p_r,φ = −V₀
  (kinetic term A(φ′)² = 0), so p_r,dem(r₀) = −F₀/(8πr₀²) forces
  V₀ = F₀/(8πr₀²), and ρ_dem(r₀) = V₀ then gives F′₀ = −2F₀/r₀ exactly.
  Phase 40's result is the Φ′₀ = 0 slice of this theorem. ✔
- **Phase 35 (P35-4, teleparallel): NOT the same theorem — same pattern,
  different mechanism** (the ledger's own wording is the correct one).
  In P35-4 the p_r lock is *structural absence*: BHL Eq. (14) contains
  no ∂F term at any r. Here the derivative terms **exist at every
  r > r₀** and are removed only at r₀, by the A-factor and the
  □F/∇∇F cancellations. The mechanisms are genuinely different, and
  the parallel even extends to the failure mode: P35-4's ρ channel
  *did* break, via a finite s·φ′ flux limit (φ′ ~ L/s) — the torsion
  analogue of this theorem's stated scope exit (singular Φ′ with
  AΦ′ ↛ 0). My derivation supports pattern-level unification only;
  the GATE6 claim sentence "This unifies P35-4's teleparallel p_r lock"
  is acceptable only under the ledger's "same pattern, mechanism
  differing per theory" reading — hence the restatement in §4.
- Scope note: the "unique off-grid root a*" parenthetical in the gate
  statement is a Phase-42 scan result (F′₀ affine in a via the R₀ lever);
  §1.2 verifies the lever (R(r₀) formula and EoM form) from which it
  follows, but W-B did not independently re-run the 192-row scan.

**Correctness: REPRODUCED** (third symbolic path, all diffs exactly 0;
numeric spot check, all errors ≤ 3.6e-04).

---

## 2. Novelty

### 2.1 Search log (every query verbatim; sources checked: arXiv, INSPIRE-HEP, Semantic Scholar, web)

1. `scalar-tensor nonminimal coupling wormhole throat flare-out condition F(phi) R Morris Thorne`
2. `Bronnikov scalar-tensor wormholes nonminimal coupling throat`
3. `"wormhole" throat radial pressure independent of derivative nonminimal coupling scalar tensor`
4. `arXiv nonminimally coupled scalar wormhole xi phi squared R throat conditions`
5. `INSPIRE-HEP scalar tensor wormhole throat nonminimal coupling flare out`
6. `Semantic Scholar Morris Thorne wormhole scalar tensor theory zero redshift radial pressure throat equation`
7. `"f(R)" wormhole throat equations redshift function derivative terms vanish at throat shape function`
8. `Barcelo Visser scalar fields energy conditions traversable wormholes nonminimal coupling throat stress energy`

### 2.2 What the literature actually contains (near neighbours)

- **The general-r field equations are standard and printed.**
  Lobo & Oliveira, arXiv:0909.5539 (f(R) MT wormholes, field eq. with
  (∇_μ∇_ν − g_μν□)F terms); Garcia & Lobo, arXiv:1007.3040
  [Phys. Rev. D 82, 104018 (2010)] (nonminimal curvature–matter coupling;
  throat NEC restrictions from the same structure); "Some Aspects of
  Morris-Thorne Wormhole in Scalar Tensor Theory", arXiv:1709.06431
  (Brans–Dicke-type MT equations derived "by direct calculation",
  pressures worked out — **in the zero-redshift case**). Anyone
  evaluating these printed equations at b(r₀) = r₀ can read off the
  A-suppression; it is implicit in the standard algebra.
- **The Φ ≠ 0 case is usually avoided, not analysed.** Garcia & Lobo,
  arXiv:1012.2443, states the common move verbatim in substance:
  "we consider Φ′ = 0, which simplifies the calculations considerably."
  The scalar-tensor paper above likewise restricts to Φ = 0. No source
  found asks what Φ′ ≠ 0 does to the throat pair.
- **Bronnikov et al. prove different theorems.** Bronnikov &
  Starobinsky, arXiv:gr-qc/0612032; Bronnikov, Skvortsova &
  Starobinsky, arXiv:1005.3262 [Grav. Cosmol. 16, 216 (2010)];
  Bronnikov, arXiv:1802.00098 — Einstein-frame no-go results (no
  wormholes with f > 0 and no ghosts). They do not state throat
  demanded-pair formulas or any derivative-independence at r₀.
- **Barceló & Visser**, arXiv:gr-qc/0003025 [Class. Quantum Grav. 17,
  3843 (2000)] — exact ξ-coupled scalar *solutions* (a wormhole branch
  for every ξ > 0), not a throat-algebra inertness statement for
  general F(φ), general Φ.
- **Derivative/kinetic-coupling neighbours are different theories:**
  Sushkov, Class. Quantum Grav. 29, 085008 (2012) and Korolev &
  Sushkov, arXiv:1408.1235 — G_μν∂φ∂φ couplings; flare-out analysed
  per-solution, no F(φ)R throat-pair theorem.
- No hit in any of the eight queries states: that the demanded radial
  pressure at an F(φ)R throat is independent of F′₀, F″₀ **and** Φ′₀;
  the A-factor as the mechanism; the □F/∇^t∇_tF cancellation; or Φ′
  surviving only through R(r₀) in the scalar EoM.

### 2.3 Novelty verdict: PARTIALLY KNOWN

Known part (exact): the general-r F(φ)R / f(R) Morris–Thorne field
equations and their Φ = 0 throat evaluation — the canonical pair itself
is a throat evaluation of algebra printed since arXiv:0909.5539 /
1007.3040 / 1709.06431, in a literature that standardly sets Φ′ = 0.

**Novel part, delimited in one quotable sentence:** "For a regular
redshift function the Φ ≠ 0 extension changes nothing at the throat —
every radial-derivative term in the t–t and r–r equations of F(φ)R
gravity carries the factor A = 1 − b/r (with the AΦ′F′ piece of □F
cancelling identically against ∇^t∇_tF), so p_r,dem(r₀) = −F₀/(8πr₀²)
is independent of F′₀, F″₀ and Φ′₀, and Φ′ acts on the throat system
only through R(r₀) in the scalar equation of motion — a statement and
mechanism not found in the scalar-tensor wormhole literature, which
treats Φ′ = 0 as a simplifying assumption rather than an irrelevance."

---

## 3. Gate verdict

**UPLOAD-READY AFTER RESTATEMENT** — correctness REPRODUCED by an
independent third path + numeric spot check; novelty PARTIALLY KNOWN
with the novel content exactly delimited above. The single required
change is the unification sentence (pattern, not same theorem, for
P35-4). The Phase-40 unification stands as stated.

## 4. Exact restated wording (replaces the claim's unification sentence)

> "In F(φ)R scalar-tensor gravity (canonical scalar, potential V(φ)) on
> a Morris–Thorne throat with regular Φ (Φ, Φ′, Φ″ finite at r₀), the
> demanded matter pair at the throat is exactly the canonical Φ = 0
> pair for any such Φ: ρ_dem(r₀) = F₀β/(8πr₀²) − (1−β)F′₀/(16πr₀) and
> p_r,dem(r₀) = −F₀/(8πr₀²), because every radial-derivative term in
> the t–t and r–r field equations carries the factor A = 1 − b/r —
> including AΦ′₀F′₀ and 2AF₀Φ′₀/r₀ — the AΦ′F′ piece of □F cancels
> identically against ∇^t∇_tF = AΦ′F′, F″₀ enters neither channel, and
> Φ′ survives only in the scalar equation of motion via
> R(r₀) = 2β/r₀² − (1−β)Φ′₀/r₀, moving the EoM flux's magnitude but
> not its sign on the families tested. Phase 40's Φ = 0 result is the
> Φ′₀ = 0 special case of this theorem. Phase 35's teleparallel p_r
> lock (P35-4) is the same *pattern* by a *different mechanism* —
> there the r–r equation contains no derivative term at any r —
> not the same theorem."

## 5. Files

- `gate6/wb_g62_derivation.py` — third-path symbolic derivation (all diffs 0).
- `gate6/wb_g62_numeric.py`, `gate6/wb_g62_numeric.json` — numeric spot check.
- This report: `gate6/results/wB_g6_2.md`.
