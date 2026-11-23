# W-B — Gate-7 claim G7-2: the Phase-50 spline-shift row at β = 0.10

**Worker:** W-B · **Date:** 2026-11-22 · **float64 everywhere** ·
nothing uploaded, no external contact, no phase record edited.
**Python:** system python3 (`/usr/bin/python3`, numpy 2.2.6 /
scipy 1.14.1 / sympy 1.12) for every run in this item.
**Code:** `gate7/wb_symbolic.py` (symbolic derivation),
`gate7/wb_auditor.py` (numeric auditor), `gate7/wb_search_log.md`.
**Numbers:** `gate7/results/wb_g72_numbers.json`.
**Derivation independence:** the symbolic derivation is W-B's OWN
(written for this gate, in spherical coordinates). W-A's derivation
was NOT used or read.

## Plain language first

Phase 50 said: take our thick (10,30) warp shell — the one Gate-6
verified at β = 0.08 — keep everything about it the same, but replace
the fixed cosine shape of the shift with a computer-polished spline
shape (five interior knots), and the shell becomes fully legal at
β = 0.10, a speed the cosine version cannot reach. It said this for
two independently polished spline shapes.

I rebuilt the deciding mathematics from scratch in a completely
different way: instead of differencing the metric on a Cartesian grid
(the method every previous verdict used), I derived the Einstein
tensor of this metric form symbolically, once, with the radial
profiles left as abstract functions, and then fed it exact analytic
derivatives of the profiles. No finite-difference stencil exists
anywhere in my deciding path.

**Both spline finalists pass, with numbers very close to Phase 50's.**
On the registered 1,404-point deciding set at β = 0.10, my symbolic
auditor finds both finalists Hawking–Ellis Type-I at every
significant point, every energy-condition margin positive, and the
core sampled-null NEC positive. The headline worst margin — an
exterior-tail SEC value — comes out at +2.593×10⁻⁷, essentially
identical to Phase 50's claimed +2.58×10⁻⁷ (theirs was limited by
their grid spacing; mine has no grid spacing). Core numbers agree
within 2–11 %.

**Correctness verdict, per finalist: REPRODUCED (both).**

One scope note from the separate robustness grid (denser inner-edge
radii and tail radii, 52 directions — reported separately under the
registration, and not a deciding-set failure): at r = 39 in the far
tail both finalists show an SEC margin of −1.53×10⁻⁸ in some
directions, a value at my path's own representation-noise floor
(2.6×10⁻⁸), and the second finalist additionally shows isolated
non-Type-I points (Type-I fraction 0.9985 in the core region) on the
denser inner-edge radii that the deciding set does not sample. The
exact scope sentence that must travel with the claim is given in §4.

On novelty: the general idea "optimise the shift to buy legality" is
**not** ours — Procaccia published an optimised shift (of a different
object, on a different shell) in October 2026, and variational
shift-profile optimisation exists in the Natário class. What the
search found nowhere else is the specific residue: a spline
transition of the shift *profile itself* on the Fuchs-family TOV
thick shell, the finding that of Procaccia's three freedoms only
this one buys speed in that family (+0.02), and the specific legal
β = 0.10 configuration. **Novelty verdict: PARTIALLY KNOWN** (known
part cited exactly in §5; novel residue delimited in one sentence).

**Gate verdict: UPLOAD-READY AFTER RESTATEMENT** — the restated
wording in §4 (deciding-set scope + robustness scope + C12 /
Le caveat) is the form that may be used.

## 1. The fresh path (as registered)

`wb_symbolic.py` derives, with SymPy and a generic index-loop routine
written for this gate, the Einstein tensor of

- g_tt = −e^{2a(r)}; g_t· = −β·S(r) dx (shift along x), i.e.
  g_tr = −βS sinθcosφ, g_tθ = −βS r cosθcosφ, g_tφ = +βS r sinθsinφ;
- γ = diag(e^{2b(r)}, r², r²sin²θ) — the spherical form of
  δ_ij + (e^{2b}−1) n_i n_j —

in coordinates (t, r, θ, φ), with a, b, S left as unspecified
functions of r. The metric inverse is supplied analytically via the
ADM structure and verified (g·g⁻¹ = I to <10⁻¹² at test points).
The tensor is lambdified over (r, θ, φ, a, a′, a″, b, b′, b″, S, S′,
S″, β). `wb_auditor.py` then evaluates it with **analytic derivatives
only**: a and b from `shell.py`'s `build_shell` (the shared
definition) via their cubic splines differentiated in closed form;
S from the K = 5 clamped cubic spline rebuilt from each finalist's
stored `z_final` through the phase's stick-break convention
(re-implemented here). The spherical tensor is carried to the
Cartesian frame by the exact Jacobian; Eulerian That, Hawking–Ellis
margins, Type-I classification and the 162-direction sampled-null
NEC are fresh code in the auditor. No Cartesian FD stencil, no
Phase-1 nested-Γ judge, no Phase-50 FD path anywhere in the chain.

**Spline reconstruction check (registered):** for both finalists the
knot values rebuilt from `z_final` match the stored `spline_diag`
knot values with max difference **0.0** (bit-exact), and knot radii
match exactly. Primary knot values:
[1, 0.9456828104853556, 0.7729452479662335, 0.5141177574474268,
0.25720817281525676, 0.06890721615129425, 0] at
r = [10, 13.333…, 16.666…, 20, 23.333…, 26.666…, 30]. Second
finalist: [1, 0.9436347227886117, 0.7717214843534514,
0.5132200724643368, 0.25676958541045247, 0.06878890212892275, 0].

## 2. Anchors (all passed BEFORE any claim number was read)

| Anchor | Registered bar | My read |
|---|---|---|
| (i) Minkowski | symbolic tensor identically zero | **0 nonzero entries** after symbolic simplification (wb_symbolic.py main run); numeric max\|G\| = 3.71×10⁻¹⁶ at β = 0.37 |
| (ii) β = 0 vs `shell.py` exact spherical T | ρ rel err ≲ 3×10⁻³; p abs err ≲ 3×10⁻⁷ | ρ rel err max **9.80×10⁻⁶**; p abs err max **1.87×10⁻¹⁰** (radii 12, 15, 20, 25, 28) |
| (iii) Gate-6 champion, β = 0.08, cosine, full smoothing, fine set | Type-I 1.000, all margins > 0 | Type-I **1.000**; whole-volume worst **+2.593×10⁻⁷** (SEC, r = 37.0); core NEC at r = 10.25 = +1.767×10⁻⁵ — digit-identical to Gate-6's recorded continuum inner-edge value |

## 3. Deciding set (exact Phase-50 fine set, 1,404 pts), β = 0.10

Gate path's own error floor (registered definition): larger of the
nonsignificant-point median |NEC| = **2.55×10⁻⁸** and the
anchor-residual scale (~10⁻⁹) → floor = 2.55×10⁻⁸;
3× floor = 7.66×10⁻⁸.

| Quantity | Phase-50 claim | W-B primary (β=0.10-polished) | W-B second (β=0.1363-polished) |
|---|---|---|---|
| Type-I fraction (significant pts) | 1.000 | **1.000** | **1.000** |
| Whole-volume worst margin | +2.58×10⁻⁷ (SEC, tail r = 37) | **+2.593×10⁻⁷** (SEC, r = 37.0) | **+2.593×10⁻⁷** (SEC, r = 37.0) |
| Core worst margin | +1.570×10⁻⁵ (primary, NEC r = 13.25); +1.568×10⁻⁵ (second, DEC r = 10.25) | **+1.544×10⁻⁵** (NEC, r = 13.25) | **+1.603×10⁻⁵** (DEC, r = 10.25) |
| Core sampled-null NEC min | +2.02×10⁻⁶ (primary); +2.66×10⁻⁶ (second) | **+1.80×10⁻⁶** (r = 13.25) | **+2.45×10⁻⁶** (r = 10.25) |
| Worst NEC / WEC / DEC (whole vol) | all > 0 | +4.35×10⁻⁷ / +4.35×10⁻⁷ / +4.35×10⁻⁷ | same |

**Bars, applied exactly as registered:**
(a) Type-I = 1.000 — PASS both. (b) worst NEC/WEC/SEC/DEC all > 0 —
PASS both. (c) core sampled-null NEC > 0 — PASS both.
(d) worst ≥ 3× gate floor: 2.593×10⁻⁷ ≥ 7.66×10⁻⁸ (10.2× floor) —
PASS both; and within factor 3 of the phase's claimed worst
(ratio 1.005) — PASS both. (e) core worst and core sampled NEC
within 50 % of claimed: primary −1.7 % / −11 %; second +2.2 % /
−7.7 % — PASS both.

**Correctness verdict — primary finalist: REPRODUCED.**
**Correctness verdict — second finalist (corroborating sub-claim):
REPRODUCED** (verdicted separately, as tasked).

Note the binding sites reproduce too, not just the values: the
whole-volume worst is the exterior-tail SEC at r = 37 for both
finalists on my path, and the core worst sites (NEC at r = 13.25
primary; DEC at r = 10.25 second) match the phase's sites exactly.

## 4. Robustness set (reported separately, per registration)

Inner-edge radii 9.75–11.50 step 0.125 and tail radii 32–40 step
0.5, × 52 Fibonacci directions (1,612 pts), β = 0.10:

- Both finalists: far-tail SEC = **−1.53×10⁻⁸ at r = 39.0** (some
  directions). Magnitude is at/below my path's representation floor
  (2.55×10⁻⁸ on the deciding set; 5.6×10⁻⁹ nonsignificant median on
  this set) — the tail SEC crosses zero far outside the shell where
  the tensor itself is ~10⁻⁷ and falling; the deciding set's own
  tail points (including r = 39 at its 26 directions) read positive.
- Primary: Type-I 1.000 everywhere on this set; core worst
  +1.95×10⁻⁵; core sampled NEC +7.29×10⁻⁶.
- Second finalist: Type-I **0.9994** overall (0.9985 in the core
  region) — isolated non-Type-I points at inner-edge radii the
  deciding set does not sample (the 0.125-step grid reaches radii
  between the deciding set's 0.5-step radii); core worst
  +6.94×10⁻⁶, core sampled NEC +4.78×10⁻⁷, both still positive.

Per the registration these findings do not by themselves kill the
claim, but they must appear in its scope. **Exact restated wording
(the only form in which the claim should be carried forward):**

> "On the registered 1,404-point fine set, an independent symbolic
> radial-reduction auditor (analytic derivatives, no finite-difference
> stencil) confirms that the (10,30), M = 8.0, compactness-0.80,
> edge-peaked (wd = 6.0, floor = 0.2), Gaussian-smoothed (4.0, 2.32),
> TOV-pressure shell with a monotone C² cubic-spline shift profile
> (K = 5; knot values [1, 0.9457, 0.7729, 0.5141, 0.2572, 0.0689, 0])
> is fully legal at β = 0.10 — Type-I fraction 1.000, whole-volume
> worst margin +2.59×10⁻⁷ (SEC, exterior tail r = 37), core worst
> +1.54×10⁻⁵, core sampled-null NEC min +1.80×10⁻⁶ — and that a
> second, independently polished K = 5 spline finalist is likewise
> fully legal at β = 0.10 on the same set (core worst +1.60×10⁻⁵,
> core sampled-null NEC min +2.45×10⁻⁶). On a denser robustness grid
> beyond the deciding set, the far tail (r = 39) shows an SEC margin
> of −1.5×10⁻⁸, at the auditor's representation-noise floor, for
> both finalists, and the second finalist shows isolated non-Type-I
> points at inner-edge radii the deciding set does not sample;
> legality is therefore claimed on the registered fine set, not on
> every off-set radius and direction. This is a prescribed-geometry
> audit: the audited source is the stress tensor the metric's
> Einstein tensor requires, conservation is automatic (Bianchi),
> and no matter model, formation route, or stability is claimed.
> Le (arXiv:2605.25417)'s stricter source-consistency standard is a
> standing caveat, not a bar met here."

## 5. Novelty

Systematic documented search: 9 queries logged verbatim with
sources and date in `gate7/wb_search_log.md` (2026-11-22). Sources
actually checked: arXiv, IOPscience, academia.edu, Springer,
Zenodo, general web. **Coverage gaps, stated plainly:** the
INSPIRE-HEP and Semantic Scholar database interfaces were not
reached directly — queries naming them returned arXiv/IOP mirrors
through the general web index instead — so those two databases
were searched only indirectly; an unrun direct search is a gap,
not a negative result. The companion Procaccia optimisation paper's
full text was likewise not separately retrieved (its construction
is described inside the certificates paper and in the Phase-50
record).

Near neighbours, cited:
- Fuchs et al. 2024, arXiv:2405.02709, Class. Quantum Grav. 41
  095013, DOI 10.1088/1361-6382/ad26aa — the base family; shift in
  FIXED forms only (no shift optimisation).
- Procaccia, "Continuum Energy-Condition Certificates for an
  Optimized Positive-Energy Warp Shell" + companion "Numerical
  Optimization of Shift Profiles for Positive-Energy Warp Shells",
  academia.edu, posted Oct 30 2026, unrefereed,
  https://www.academia.edu/180109147/Continuum_Energy_Condition_Certificates_for_an_Optimized_Positive_Energy_Warp_Shell
  — optimised shift, but of a shift SOURCE (12 B-spline coefficients
  of a source function, tanh switch), on a (10,20) zero-radial-
  pressure shell, reaching β = 0.1363. **This is the known part of
  the general idea: "an optimised shift buys legality/speed in a
  positive-energy warp shell" is his, published before this gate.**
- Bolívar & Vasilev, "Zero expansion is not free…", arXiv HTML
  2609.36211 (Gen. Rel. Grav.) — the exact variational minimiser
  over shift profiles of the integrated Eulerian negative energy in
  the Natário zero-expansion class (unit lapse, flat slices, no
  matter shell): shift-profile optimisation as a method also exists
  there, for a different class and objective.
- Le, arXiv:2605.25417 and arXiv:2602.18023 — source-first shells
  (shift derived from the momentum constraint, not optimised) and
  observer-robust verification; no TOV thick-shell shift-profile
  optimisation, and no attribution across Procaccia's freedoms.
- Sherrington, Zenodo 10.5281/zenodo.18286172 — parameter (σ, v)
  optimisation of a Rodal-style irrotational family; not a shell
  shift profile.

Nothing found — in any source actually checked — optimises a spline
transition of the shift profile S(r) itself on the Fuchs TOV
thick-shell family, nor attributes Procaccia's three freedoms
against each other in that family, nor exhibits a legal β = 0.10
configuration of the (10,30) M = 8.0 TOV shell.

**Novel residue, one quotable sentence:** "Ours is the transfer of
shift-profile optimisation to the Fuchs TOV thick-shell family —
specifically the finding, by controlled one-freedom-at-a-time
attribution, that a spline reshaping of the shift profile itself is
the only one of Procaccia's three freedoms that buys speed there
(+0.02, β = 0.08 → 0.10), together with the specific legal β = 0.10
configuration that embodies it."

**Novelty verdict: PARTIALLY KNOWN** — the general move (optimise
the shift) is Procaccia's (Oct 2026, unrefereed) and variational
profile optimisation exists in the Natário class; the residue
delimited above — options (i) transfer, (ii) attribution, and
(iii) the specific configuration, jointly — was found nowhere else.
Not (iv): the residue is not nothing, because Procaccia's object
(spline-modulated shift source on a zero-pressure (10,20) shell)
and ours (spline transition of S(r) itself on a TOV (10,30) shell)
are different constructions on different shells, and the
attribution result has no counterpart in his papers.

## 6. Gate verdict

- Correctness: **REPRODUCED** (primary finalist); **REPRODUCED**
  (second finalist, corroborating sub-claim).
- Novelty: **PARTIALLY KNOWN** (known part = shift optimisation as
  a legality-buying move, Procaccia Oct 2026; residue as delimited).
- **GATE VERDICT: UPLOAD-READY AFTER RESTATEMENT**, in the exact
  wording of §4 only (which carries the deciding-set scope, the
  robustness scope, the C12 prescribed-geometry accounting, and
  the Le arXiv:2605.25417 caveat). No upload was made by this gate.
