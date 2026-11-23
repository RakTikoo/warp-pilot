# Gate-7 W-A — G7-1: the halved-smoothing row at β = 0.10 / 0.09

## Plain language first

I re-audited Phase 50's halved-smoothing shell with a completely
different kind of machinery — a symbolic calculation, not another
grid finite-difference code — and on the registered 1,404-point
audit set the claim **checks out at both speeds**: at β = 0.10 and
β = 0.09 the shell is Type-I everywhere and every energy-condition
margin is positive, with numbers very close to Phase 50's own
(worst margin +2.16×10⁻⁷ mine vs +1.47×10⁻⁷ theirs, well inside the
registered factor-3 band; core values within ~10 %).

But my denser probe — which the gate registered exactly for this
purpose — found something the fine audit set steps over. The fine
set's radii jump from 9.75 to 10.25 at the inner edge. In between,
immediately inside the shell's inner edge (radii 10 to about 10.2),
there is a thin layer where the dominant energy condition is
negative at β = 0.10 (deepest −1.3×10⁻⁵ at r ≈ 10.01). It is real,
not an artefact of my path: a finite-difference read at that spot
moves toward negative as its grid is refined (+9.5×10⁻⁶ →
+6.3×10⁻⁶ → −1.1×10⁻⁶). At β = 0.09 the same layer exists only as
a shallow dip (worst −7.5×10⁻⁷ at the edge itself, gone by
r = 10.05). So the honest verdict is: the numbers reproduce, and
"fully legal" survives only with its scope stated — legal on the
audited fine set, with a named thin DEC-negative layer just inside
R₁ that the fine set does not resolve.

**Correctness verdict (both β): REPRODUCED WITH RESTATEMENT.**
**Novelty verdict: PARTIALLY KNOWN** (details below).
**Gate verdict suggested: UPLOAD-READY AFTER RESTATEMENT.**

## How I checked (the registered fresh path)

Fresh code in `gate7/`: `wa_symbolic.py` derives the Einstein
tensor of the registered metric form (radial a(r), b(r); shift
β·S(r) along x; spatial δ_ij + (e^{2b}−1) n_i n_j) with SymPy, in
terms of a, b, S, their first/second radial derivatives and the
direction cosines n_i. Spatial derivatives act through the exact
radial chain rule (∂_k r = n_k, ∂_k n_i = (δ_ki − n_k n_i)/r,
∂_k f(r) = f′ n_k); the inverse metric is the closed-form block
(Schur) inverse (numeric spot-check vs the symbolic product:
max error 4.4×10⁻¹⁶); ∂(g⁻¹) is the exact algebra −g⁻¹∂g g⁻¹.
`wa_eval.py` lambdifies those expressions and evaluates them with
**analytic** derivatives of the profile representations — cubic
splines of a, b from the shared definition `shell.py`,
differentiated by the spline itself; the cosine S on [10,30]
differentiated in closed form. No Cartesian FD stencil anywhere
in the deciding path. Hawking–Ellis margins, Type-I
classification and the 162-direction sampled-null NEC are fresh
implementations in `wa_eval.py`. Python: **system python3**
(numpy 2.2.6 / scipy 1.14.1 / sympy 1.12), float64 everywhere.
Numbers: `results/wa_g71_numbers.json` (driver `wa_run_g7.py`),
bars recomputed by `wa_check.py` → `results/wa_check.json`;
anatomy in `results/wa_anatomy.json` (`wa_anatomy.py`) and
`results/wa_tiebreak.json` (`wa_tiebreak.py`).

## Anchors (all pass, before any claim number)

| Anchor | Registered bar | Mine |
|---|---|---|
| (i) Minkowski | symbolic tensor identically zero | max\|G\| = 8.7×10⁻¹⁹ at generic points (a=b=S=0, β=0) |
| (ii) β=0 vs `shell.py` exact spherical T, bulk radii 12–28 | ρ rel err ≲ 3×10⁻³; p abs err ≲ 3×10⁻⁷ | ρ rel err **2.18×10⁻⁵**; p abs err **1.39×10⁻⁹** |
| (iii) Gate-6 champion, β=0.08, full smoothing, fine set | Type-I 1.000, all margins > 0 | Type-I **1.000**, worst **+2.5926×10⁻⁷** (SEC, r = 37) — Gate-6's own h=0.15 read was +2.59×10⁻⁷; core sampled NEC +2.856×10⁻⁶ (Gate-6: +2.86×10⁻⁶) |

Machinery sanity (labelled, not deciding): on 8 shell points at
β = 0.10 my tensor agrees with the Gate-6 FD auditor's to
max |ΔT̂| = 1.83×10⁻⁷, NEC values to ≲1 % in the shell.

## Deciding set (exact Phase-50 1,404-pt fine set) — my numbers

Gate error floor (registered definition): max(nonsignificant-point
median |NEC| = 5.9×10⁻¹⁰, anchor-(ii) residual scale 1.39×10⁻⁹)
= **1.39×10⁻⁹**.

| Quantity | β = 0.10 mine | claimed | β = 0.09 mine | claimed |
|---|---|---|---|---|
| Type-I fraction (significant) | **1.000** | 1.000 | **1.000** | 1.000 |
| Whole-volume worst margin | **+2.155×10⁻⁷** (DEC, r = 6.0, cavity) | +1.47×10⁻⁷ | **+2.166×10⁻⁷** (DEC, r = 6.0) | +1.474×10⁻⁷ |
| worst NEC / WEC / SEC (all-sig) | +2.157×10⁻⁷ / +2.157×10⁻⁷ / +2.157×10⁻⁷ | — | +2.167×10⁻⁷ (all three) | — |
| Core worst margin | **+3.276×10⁻⁶** (DEC, r = 10.25) | +2.94×10⁻⁶ | **+7.923×10⁻⁶** (DEC, r = 10.25) | +7.70×10⁻⁶ |
| Core sampled-null NEC min | **+1.568×10⁻⁶** | +1.75×10⁻⁶ | **+6.461×10⁻⁶** | +6.64×10⁻⁶ |
| Worst / gate floor | 155× | (36× their FD floor) | 156× | (36×) |

Registered bars (a)–(e), recomputed by `wa_check.py`:
(a) Type-I = 1.000 ✓ both β. (b) worst NEC/WEC/SEC/DEC all > 0 ✓
both. (c) core sampled-null NEC min > 0 ✓ both. (d) worst ≥ 3×
gate floor (155×) and within factor 3 of claimed (ratio 1.47)
✓ both. (e) core worst and core sampled NEC within 50 % of
claimed (ratios 1.11 / 0.90 at 0.10; 1.03 / 0.97 at 0.09) ✓ both.
**On the deciding set, the claim reproduces in full at both β.**

One site note: my whole-volume worst sits in the cavity at
r = 6.0, Phase 50's primary read put its worst in the r = 33 tail
(+1.47×10⁻⁷); Phase 50's own finer reads (h = 0.075) also gave
+2.16×10⁻⁷-class worst values, and my tail read at r = 33 is
+8.68×10⁻⁷ (SEC). The ~10⁻⁷ whole-volume worst is a
representation-detail quantity, as the gate registration itself
says; the factor-3 band covers the difference.

## Robustness set (registered, reported separately) — the layer

Radii 9.75–11.50 step 0.125 and 32–40 step 0.5, × 52 directions
(1,664 pts). Findings, all at the inner edge:

- **β = 0.10:** significant worst **−1.290×10⁻⁵** (DEC) at
  r = 10.0 exactly (inside-limit), 3 non-Type-I points on that
  ring (their sampled NEC stays barely positive, +6.3×10⁻⁸).
  Ring scan (52 dirs): DEC min −1.33×10⁻⁵ at r = 10.01,
  −1.12×10⁻⁵ (10.02), −7.92×10⁻⁶ (10.05), −5.66×10⁻⁶ (10.08),
  −4.38×10⁻⁶ (10.10), −1.59×10⁻⁶ (10.15), **+8.9×10⁻⁷ (10.20)**,
  +3.22×10⁻⁶ (10.25). From the cavity side the limit is clean
  (+6.28×10⁻⁶ at r = 9.99). At r = 10 the value depends on the
  S″ convention because the cosine shift is C¹, not C², at the
  window edge (S″ jumps): outside-limit DEC +6.45×10⁻⁶, mean
  +6.66×10⁻⁶, inside-limit −1.29×10⁻⁵ — but the layer is **not**
  only the edge point: it extends over 10 < r ≲ 10.2 where S″ is
  unambiguous. At β = 0 the same ring reads DEC +6.18×10⁻⁶ under
  every convention, matching `shell.py`'s exact spherical DEC at
  R₁ (+6.1825×10⁻⁶): the layer is a β-driven effect, not a static
  shell defect.
- **FD corroboration (tie-break-style, not deciding):** at the
  symbolic worst point of the r = 10.05 ring, the Gate-6 FD
  auditor's DEC reads +9.46×10⁻⁶ (h = 0.15) → +6.25×10⁻⁶
  (h = 0.075) → **−1.07×10⁻⁶ (h = 0.0375)** — converging toward
  the symbolic sign as the stencil stops averaging over the
  layer. The symbolic path does not stand alone.
- **β = 0.09:** DEC −7.54×10⁻⁷ at r = 10.0 (inside limit),
  −6.7×10⁻⁸ at r = 10.02, positive from r = 10.05 (+9.5×10⁻⁷)
  outward. A sliver of the same layer, ~20× shallower and
  confined to r ≲ 10.02.
- **Tail (32–40):** at r ≥ 34.5 all margins are ≤ 3.1×10⁻⁸ in
  magnitude on points whose tensor scale is ≤ 7×10⁻⁸
  (nonsignificant under the shared convention) — the far tail is
  representation-level noise around the Schwarzschild vacuum, in
  both paths; nothing there is significant.

Per GATE7.md, a robustness violation does not by itself kill the
claim, but it must appear in the restated wording's scope — hence
REPRODUCED WITH RESTATEMENT rather than REPRODUCED for both β:
the unqualified phrase "fully legal at β = 0.10" is a
whole-volume statement, and the whole volume contains this
layer.

## Novelty — the smoothing-width-as-speed-variable finding

Search log (10 queries verbatim, sources, date):
`gate7/wa_search_log.md`. Summary of what the literature says:

- **Known part.** Fuchs et al. 2024 (arXiv:2405.02709; *Class.
  Quantum Grav.* **41** 095013, DOI 10.1088/1361-6382/ad26aa)
  build their shell by smoothing ρ and P with a moving average
  and state that the smoothing coefficients are "found
  iteratively until the solution has no violations" of the four
  ECs, with span ratio s_ρ/s_P ≈ 1.72 found "by trial and
  error", at a fixed design reported at β_warp = 0.02 ("likely
  not an upper limit"). Their §6 outlook proposes replacing
  smoothing by direct 1-D profile optimisation to reduce mass.
  So *smoothing choices decide EC legality at the shell
  boundaries* is Fuchs's own method — that premise is not ours.
- **Near neighbours, none stating the finding.** Procaccia
  (academia.edu, 30 Oct 2026, unrefereed; certificates paper
  read in extract): his density smoothing is a fixed 4× box
  convolution (W = 3.6328174 m); the optimised variable is the
  shift source — no smoothing-width scan or discussion found.
  Le (arXiv:2605.25417): reproduces Fuchs via iterative
  Gaussian-kernel smoothing, finds Type-IV violations in the
  smoothing *tail*, and scans shell compactness and *thickness*
  (600 configurations) for his own source-first classes — no
  smoothing-width-vs-β scan, and his moral is the opposite
  emphasis (the transition region is where admissibility is
  lost). Alcubierre-family wall-sharpness work (Pfenning & Ford,
  gr-qc/9702026; White, NASA TM-2011-217361; the σ-ablations in
  Le's warpax paper, arXiv:2602.18023; Sherrington, Zenodo
  18286172) scans wall thickness/sharpness for metrics that
  violate the ECs, where sharper walls worsen the negative-energy
  budget — a different family and the opposite direction.
- **Not found anywhere searched:** any statement that reducing
  a Fuchs-family shell's profile smoothing width raises its
  EC-legal β ceiling, and any smoothing-width scan at all in the
  Fuchs-family / positive-energy-shell literature.

**Novel part, delimited in one quotable sentence:** "In the
Fuchs-family TOV warp shell, the Gaussian smoothing width of the
density/pressure profiles is a speed variable: halving it
(s_ρ, s_P) = (4.0, 2.32) → (2.0, 1.16) raises the
energy-condition-legal shift ceiling from β = 0.08 to β = 0.10,
because narrower smoothing sharpens the inner-edge support
against the shift gradient that otherwise opens a non-Type-I
pocket there."

**Novelty verdict: PARTIALLY KNOWN** — the premise (smoothing
must be tuned for EC legality) is Fuchs et al.'s published
method; the direction, the ceiling shift, and the mechanism
attribution above were not found in the searched literature.

**Coverage gaps (plainly):** INSPIRE-HEP was not queried through
its own search interface in this session — it was reached only
via general web search and via the index links on arXiv abstract
pages; a record indexed only in INSPIRE could have been missed.
Semantic Scholar was likewise not queried through its own search
interface — same route only; a record indexed only there could
have been missed. Procaccia's companion optimisation paper was
not retrieved in full text (the certificates paper was read via
the academia.edu extract; Phase 50 had the companion's abstract
and code archives), so a smoothing-width discussion appearing
only in that full text would be missed. These are gaps, not
negative results.

## Exact restated wording (required scope)

> On the 1,404-point fine audit set (radii 3–9 step 1.0,
> 9.25–30 step 0.5, 31–39 step 2.0, × 26 Fibonacci directions),
> the (R₁,R₂) = (10,30) shell — ADM mass M = 8.0 geom
> (1.0773×10²⁸ kg), compactness M/R₁ = 0.80, edge-peaked density
> (wd = 6.0, floor = 0.2), TOV pressure, cosine shift on
> [10,30] — with Gaussian smoothing halved to (s_ρ, s_P) =
> (2.0, 1.16) satisfies NEC, WEC, SEC and DEC at every
> significant point with Hawking–Ellis Type-I fraction 1.000 at
> β = 0.10 (whole-set worst margin +2.16×10⁻⁷) and at β = 0.09
> (+2.17×10⁻⁷), verified by an independent symbolic
> radial-reduction auditor. This is a prescribed-geometry
> audit: the audited source is the stress tensor the metric's
> Einstein tensor requires, conservation is automatic
> (Bianchi), and no matter model, formation route or stability
> is claimed; Le's (arXiv:2605.25417) stricter
> source-consistency standard is a standing caveat, not a bar
> met here. Scope limit: a denser radial probe finds a
> DEC-negative layer immediately inside the inner edge at
> β = 0.10 (10 < r ≲ 10.2, minimum −1.3×10⁻⁵ at r ≈ 10.01),
> which the fine set's radii 9.75 and 10.25 step over; at
> β = 0.09 the same layer appears only as a dip of at most
> 7.5×10⁻⁷ confined to r ≲ 10.02. "Fully legal" is therefore
> claimed on the audited fine set, not at every radius in
> (10, 10.25).

## Files

- Code: `gate7/wa_symbolic.py` (derivation; log
  `wa_symbolic.log`, `wa_derivation.json`, expressions
  `wa_g_expr.pkl`), `gate7/wa_eval.py`, `gate7/wa_run_g7.py`,
  `gate7/wa_anatomy.py`, `gate7/wa_tiebreak.py`,
  `gate7/wa_check.py`.
- Numbers: `gate7/results/wa_g71_numbers.json`,
  `results/wa_anatomy.json`, `results/wa_tiebreak.json`,
  `results/wa_check.json`.
- Novelty: `gate7/wa_search_log.md`.
- Nothing uploaded, no one contacted, no phase record edited.
