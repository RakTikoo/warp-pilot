# Warp Pilot — an open, verified search for positive-energy warp metrics

An independent computational search for warp-drive spacetimes whose matter
satisfies the classical energy conditions (NEC, WEC, SEC, DEC) for **all
observers**, audited with a purpose-built verifier, adversarial red-teaming,
and three independent computation paths. Everything here is reproducible
from the code and frozen configurations in this repository.

**We are publishing this to ask for independent verification.** If you can
re-run an audit, break a result, or extend a search, please see the
[help-wanted issues](../../issues) — several are scoped as good first
issues (run a script, compare numbers, report).

## Headline results (all numbers in `REPORT.md` and `CHECKPOINT.md`)

- **Two novel subluminal warp shells, verified.** Shell geometries outside
  the Natário class (non-unit lapse, non-flat spatial slices) that pass all
  energy conditions for all observers, confirmed by a finite-difference
  auditor, an independent autodiff code (warpax), and a symbolic SymPy
  derivation, plus an adversarial optimiser that tried and failed to find
  a violating point:
  - *Finalist A* — β = 0.02c, ADM mass 2.69×10²⁷ kg, **40% below** the
    Fuchs et al. (2024) baseline mass at the same radius and velocity.
  - *Finalist B2* — β = 0.03c, 3.64×10²⁷ kg, **19% below** that baseline
    at 50% higher velocity.
  - A β = 0.05c frontier design at compactness M/R₁ = 0.383 (lightest:
    2.58×10²⁷ kg), with a fitted scale-covariance law for the frontier.
- **The positive-energy frontier terminates between β = 0.05 and β = 0.1.**
  At β = 0.1, three independent constructions (named families, free-form
  machine search, and a conditions-first reverse construction) all land
  within ~10⁻⁸ of zero worst-margin and none certifies a pass. The
  boundary is a wall: different energy conditions bind on its two sides.
- **No superluminal candidate anywhere.** A per-geometry exclusion map
  (16 rows in `REPORT.md`) covers spherical shells, toroidal shells
  (symmetric and asymmetric), free-form and fully-3D shapes, shells on
  Schwarzschild/(A)dS backgrounds, shells in expanding (FLRW/de Sitter)
  backgrounds, and modified-gravity / exotic-source lenses — f(R), f(Q),
  Kaluza–Klein lifts, Einstein–Cartan torsion, non-minimal scalars,
  Casimir threading, and multi-component sources (the last closed by a
  linearity proof, not by search).

## The shape of Finalist A

![Finalist A cross-section and profiles](finalist_A_shape.png)

*Finalist A, computed from the frozen configuration in `results/frozen/finalist_A.json` with the repository's own `shell.py` (plot script: `plot_finalist_A.py`). Left: matter density in a cross-section through the centre — an empty cavity (r < 10) inside a spherical wall (10–20) whose density peaks at its two edges; the whole configuration moves at β = 0.02. Right: the density profile and the shift (velocity) profile — the interior rides at the full β and the shift falls to zero across the wall, so the transition lives entirely inside the matter. This is a constant-velocity configuration; formation and stability are not claimed (see Limits).*

## Limits — read these before citing anything

- The verified shells are **constant-velocity** configurations. Formation,
  acceleration, and stability are **not** solved; a quasi-static snapshot
  sequence is included and labelled necessary-not-sufficient.
- Margins are numerical (~10⁻⁵–10⁻⁷), established by finite sampling of
  points and observers — strong evidence, **not a proof**.
- Matter is characterised only through the energy conditions; no specific
  physical matter model is proposed.
- No outside expert has re-run these results yet. That is the point of
  this repository.

## Repository layout

- `REPORT.md` — the final internal report: plain-language summary,
  technical record, verification appendix, superluminal exclusion map.
- `CHECKPOINT.md` — the full ground record: every run, failure anatomy,
  fitted pattern, data binding (Planck, GW170817, Eöt-Wash, ATLAS values
  used as gates), and the exhaustion ledger.
- `verify_metric.py`, `metrics.py`, `shell.py` — the auditor (Einstein
  tensor by finite differences, Hawking–Ellis classification, all-observer
  margins).
- `results/frozen/` — the three verified configurations (A, B2, β=0.05
  frontier winner) exactly as audited.
- `results/` — JSON/log output of every run cited in the report.
- Track scripts: `trackL.py` (frontier), `trackP*.py` (free-form search),
  `mg1_*.py` / `mg2_*.py` (modified gravity), `x1_*.py`–`x5_*.py`
  (geometry/source lenses), `n1_*.py`–`n4_*.py` (new-physics tracks),
  `redteam*.py` (adversarial verification), `qi_ledger.py` (quantum
  inequality ledger).

## Re-running the headline check

Python 3.12, NumPy/SciPy/SymPy (float64 throughout). The finalist audits
are driven by `verify_finalist.py` / `run_finalistB2.py` against the
frozen configurations in `results/frozen/`; the cross-check path uses
`warpax_check.py` / `warpax_crosscheck.py` (optional, requires warpax).
Expected agreement: NEC minima +2.121×10⁻⁵ (A) and +2.864×10⁻⁵ (B2) on
both paths, Hawking–Ellis Type I everywhere.

## Licence

MIT. The physics, favourable or not, belongs to whoever checks it.
