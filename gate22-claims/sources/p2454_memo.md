# P245-4 MEMO — COMPANION-DRIVE FLUX CANCELLATION (Phase 245, Item 4 / C4)

**Verdict form fired: COMPOSITION MAKES IT WORSE** — interference
constructive on the deficits, priced below; the family closes.
(Fired under the registration's between-forms clause: the form's
registered parenthetical expected median q and dist_Re to worsen,
and they do NOT — both improve in band, priced in §3. The form
fires on its headline and its consequence, because every
legality read worsens, the interference is large, and the crack
bar is missed by a factor ≥ 42 at the deciding offset and is
empty at full amplitude. The alternative form, FLUX CANCELS ONLY
WITH TRANSPORT, is factually contradicted by the reads: the
q improvement happens WITH transport rising, and the counter arm
loses transport while its q gets *worse* — §5. No fourth form
was invented.)

Registration: `phase245/work/p2454_registration.md` (written
before any deciding computation; unamended). Driver:
`phase245/work/p2454_run.py`; post-hoc joint-node diagnostic:
`phase245/work/p2454_diag.py` (labelled diagnostic, not a
deciding read). All verdict-carrying numbers:
`phase245/results/p2454_results.json`. Frame of record: Phase
166 pin, Gate-19-corrected tensor (lineage; T_req derived
analytically, no E_total/fluid_T read consumed), programme venv,
float64. Bounded local run (~6.5 min wall, single process).
β = 1.1 only.

## The pair (as registered)

Primary: the D1 drive, shift V⁽¹⁾ = β·S(r₁)·e_x, quintic S on
[10, 20]. Companion: co-directional twin of the same profile
centred at c = (0, d, 0), d = 8 deciding, V⁽²⁾ = a·β·S(r₂)·e_x,
dial a ∈ {0, 0.25, 0.5, 0.75, 1.0}; robustness d ∈ {4, 12} at
a = 1; counter arm: co-centred counter-shift a < 0 (an exact
β-rescaling, diagnostic only). Posed mechanism: the companion's
y-gradients oppose the primary's between the centres while its
on-axis shift adds to transport. T_req by the D2 analytic path
generalised to an arbitrary stationary shift field (exact
Jacobian/Hessian of V; no FD in the primary path). Reads on
SET-P (SET READ: per centre, 21 radial nodes on [10, 20] ×
162-point Fibonacci sphere; pair set = union, 6804 points),
except where labelled. Legality is read on the pair's TOTAL
T_req alone (NO-EXOTIC standard: no posed source, no helper).

## Controls (run first; all PASS)

| control | read | result |
|---|---|---|
| C0a (a → 0 = single-drive map, MANDATORY) | generalised code on D2's SET-A shell subset vs `p2352_results.json` | median q 38.05700115420225 (rel. diff. **0.0**), Type-I fraction 0.0003788835564536499 (abs. diff. 0.0), NEC min −0.00378336198802795 (diff. 0.0), WEC min −0.036210271834070086 (diff. 0.0) — **bit-exact reproduction of D2**; the generalised path IS the D2 path at a = 0 |
| C0b (flat limits) | max \|T_req\| inside both interiors / outside both shells, a = 1 | **0.0 exactly** (22 points) |
| C-OPP (equal-and-opposite = null transport, MANDATORY) | co-centred a = −1, d = 0 | max \|T_req\| = **0.0 exactly** on the sample set; v_eff = **1.0 exactly** at both quadrature tolerances (T = 60) — the expected null-transport limit |
| C-T (translation) | companion alone (a = 1, d = 8) on its own translated set vs primary alone on its own set | median q rel. diff. 8.3×10⁻¹⁶; Type-I abs. diff. 0.00118 (≤ 2×10⁻³ bar; the residual is the joint-node census, §4) |
| C-Q (quadrature) | every arrival read at epsrel 1×10⁻¹¹ / 1×10⁻¹³ | rel. diff. **0.0** on every rung |

Member baselines on SET-P (own-centre sets, for comparison):
primary alone — median q 34.267 (max 4.22×10⁴, a denominator→0⁺
artefact as in D2), denominator ≤ 0 on 70.4% of points, q ≤ 1 at
**0%** of defined points, NEC min/median −0.003771 / −0.001541,
WEC min/median −0.03611 / −0.014947, violating share 91.24%.
(The SET-P median q, 34.267, differs from D2 SET-A's 38.057
because the point set differs; C0a ties the two sets' codes
bit-exactly.)

## 1. Transport — the companion ADDs, as posed (fenced read)

Arrival read as in D1 (co-propagating null ray on the X axis,
D = 60, t = const slicing — a slicing-dependent
effective-arrival read, NOT a transport theorem):

| a (d = 8) | v_eff | vs single |
|---|---|---|
| 0.0 | 1.473663 | — (D1 read reproduced exactly) |
| 0.25 | 1.536307 | +4.25% |
| 0.5 | 1.588773 | +7.81% |
| 0.75 | 1.633270 | +10.83% |
| 1.0 | **1.671497** | **+13.42%** |

Every rung is in band (registered floor: ≥ 0.99 × single).
Robustness at a = 1: d = 4 → v_eff 1.720081 (+16.72%);
d = 12 → 1.602444 (+8.74%). Transport is never the price in
this family — the companion's on-axis shift is ≥ 0 everywhere.

## 2. The q-map — the flux RATIO halves, in band

Pair on SET-P (union set):

| a | median q | max q | denom ≤ 0 share | q ≤ 1 share (of defined) |
|---|---|---|---|---|
| 0.0 | 33.513 | 3.79×10⁷ † | 0.730 | 0.0 |
| 0.25 | 17.652 | 8.17×10⁶ † | 0.660 | 0.00043 |
| 0.5 | 15.941 | 8.17×10⁶ † | 0.684 | 0.00419 |
| 0.75 | 15.097 | 8.17×10⁶ † | 0.711 | 0.02189 |
| 1.0 | 15.844 | 8.17×10⁶ † | 0.726 | 0.02466 |

† max q is a denominator→0⁺ artefact and carries no weight
(D2's standing note); median is the distributional read.
Robustness at a = 1: d = 4 → median q 15.855; d = 12 → 10.973.
So the posed gradient opposition is real in the ratio: median q
falls by ~2.2× against the member baseline (34.267) while
transport rises. **This is the family's one genuine effect —
and it does not convert into type** (§3, §4).

## 3. Type structure — the wall stands; the two improvements never meet

Distance to real spectrum, dist_Re/|T_req|_F (the D3 measure;
per point, max |Im λ| of the mixed tensor over |T|_F):

| a | dist_Re median | dist_Re max | real-spectrum share (≤ 1×10⁻⁶) |
|---|---|---|---|
| member alone | 0.405 | 0.7071 | (see §4) |
| 0.25 | 0.408 | 0.7071 | 0.0403 |
| 0.5 | 0.352 | 0.7071 | 0.0417 |
| 0.75 | 0.307 | 0.7071 | 0.0437 |
| 1.0 | 0.281 | 0.7071 | 0.0412 |

The median distance improves modestly (0.405 → 0.281 at a = 1);
the MAX never moves (0.7071 = 1/√2, the maximally non-real
value, at every rung) — the worst of the shell is untouched.

**The crack conjunction is empty where it matters.** The
registered crack requires points simultaneously Type-I AND
real-spectrum AND q ≤ 1 with denominator > 0, at ≥ 5% of SET-P.
Read: a = 0.25 → 0 points; a = 0.5 → 5 points (0.0735%);
a = 0.75 → 0; **a = 1.0 → 0 points (0.000%)**; secondary
d = 12, a = 1 → 0.118%; d = 4, a = 1 → 0. Best deciding-offset
read is **68× below the 5% bar**. The diagnostic (§4) shows
why: at a = 1 the real-spectrum points and the q ≤ 1 points are
**disjoint sets** — every real-spectrum point has flux
denominator ≤ 0 (q undefined; NEC failing through
T_00 + T_n̂n̂ < 0), and none of the 46 q ≤ 1 points is Type-I or
real-spectrum. The 5 stray conjunction points at a = 0.5 sit at
r₁ ≈ 10.5 (the inner joint's edge) and still violate NEC there
(median NEC margin at those points −1.33×10⁻⁴): even the
" cracked" points are not legal.

## 4. Joint-node anatomy (post-hoc diagnostic, not deciding)

SET-P's radial nodes include r = 10 and r = 20 exactly, where a
single bubble's S′ = S″ = 0 and its T_req vanishes identically —
trivially Type-I, q undefined. The diagnostic
(`p2454_diag.py`) removes this census artefact:

- Primary alone, nontrivial points (|T|_F ≥ 1×10⁻⁸, n = 3078):
  Type-I fraction **0.00000**, real-spectrum fraction 0.00000 —
  on this set the single drive has NO nontrivial Type-I points
  at all (consistent with D2's SET-A fraction 3.8×10⁻⁴).
  Mid-shell points only (own r ∈ {12.5, 15, 17.5}): Type-I 0.
- Pair a = 1, nontrivial points (n = 6514): Type-I / real
  fraction 0.00200 (13 points) — a real but tiny creation —
  with crack conjunction still **0**; mid-shell points only:
  Type-I **0.00000**, median q 9.729, q ≤ 1 share 2.68% (none
  of them Type-I).
- The pair's q ≤ 1 points (46 at a = 1) sit at the companion's
  inner shell edge (median min(r₁, r₂) = 11.0) — the weak-field
  fringe where |S′| is small, not the cancellation midplane
  band the family posed.

## 5. Legality on the total stress — worse on every read

Pair on SET-P, NO-EXOTIC standard (pair's T_req alone):

| a | NEC min / median | WEC min / median | NEC=WEC=DEC violating share |
|---|---|---|---|
| member alone | −0.003771 / −0.001541 | −0.03611 / −0.014947 | 0.9124 |
| 0.25 | −0.004470 / −0.001168 | −0.04277 / −0.011429 | 0.9608 |
| 0.5 | −0.005063 / −0.001228 | −0.04841 / −0.011871 | 0.9608 |
| 0.75 | −0.005604 / −0.001415 | −0.05367 / −0.013757 | 0.9608 |
| 1.0 | **−0.006098 / −0.001595** | **−0.05838 / −0.015477** | **0.9608** |

(Margin maxima are 0.0 at every rung — the shell-edge nodes;
medians AND maxima reported per the standing rule.) The deepest
deficits DEEPEN monotonically with a (WEC min −62% deeper at
a = 1 than the member's), and the violating share rises from
91.2% to 96.1% (the pair's shell is the union of two shells —
more of the sampled volume is inside a wall).

Negative-energy budget (CONTINUUM: spherical quadrature about
the origin, ball r ≤ 30 containing both shells; twin-checked,
twin rel. diff. ≤ 1.6×10⁻⁵; the a = 0 rung reproduces D2's
−2.590291375073908 to rel. diff. 1.4×10⁻⁷):

- a = 0.0: E_neg = −2.590291
- a = 0.5: E_neg = −3.425305
- a = 1.0: E_neg = **−4.919969** — 90% more negative budget than
  the single drive. Against the additive two-bubble price
  (2 × −2.590291 = −5.180582) interference SAVES 0.260613
  (5.0%): the budget is sub-additive, but the pair still costs
  nearly two drives' worth of negative energy for one drive's
  (plus 13%) transport.

## 6. Interference, priced exactly (Phase 226 discipline)

Cross tensor T_× = T_pair − T_primary − T_companion (covariant
components, common coordinate frame; each member computed by
the same path at the same SET-P points). It is NOT small:

| a | \|T_×\|_F median | \|T_×\|_F max | \|T_×\|_F/\|T_pair\|_F median | max |
|---|---|---|---|---|
| 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| 0.25 | 2.56×10⁻⁴ | 1.08×10⁻³ | 0.240 | 5.12 † |
| 0.5 | 4.78×10⁻⁴ | 1.84×10⁻³ | 0.420 | 18.6 † |
| 0.75 | 6.52×10⁻⁴ | 2.35×10⁻³ | 0.540 | 9.39 † |
| 1.0 | 8.05×10⁻⁴ | 2.75×10⁻³ | **0.588** | 16.4 † |

† relative maxima sit at near-zero |T_pair| points (fringe
nodes) and carry no weight; the MEDIAN is the read: at a = 1
the cross-term is typically ~59% of the pair tensor's own norm.
Unlike Phase 226's director (interference numerically zero),
this composition is strongly non-additive — superposition of
two shift fields is not superposition of their stresses, and
the cross-term's net sign is set by where it lands: mildly
favourable on the integrated budget (§5, −5.0% vs additive),
unfavourable on every pointwise deficit (deepest NEC/WEC
deepen, §5). Zero-interference composition does not exist in
this family.

## 7. The counter arm — the exchange that isn't (diagnostic)

Co-centred counter-shift (= the single drive at β(1+a)):

| a | effective β | v_eff | in band? | median q | NEC min |
|---|---|---|---|---|---|
| −0.25 | 0.825 | 1.377154 | NO (−6.5%) | 45.56 | −0.002893 |
| −0.5 | 0.55 | 1.264519 | NO (−14.2%) | 65.34 | −0.001890 |
| −0.75 | 0.275 | 1.136696 | NO (−22.9%) | 117.33 | −0.000857 |

Counter-shifting buys smaller margins (∝ β², as it must) at
direct transport cost — AND its median q RISES (34.3 → 117.3):
q is a ratio, and as β falls the linear-in-β second-derivative
terms hold the denominator down faster than the flux numerator
falls. There is no point in this family, on either arm, where
flux cancellation is bought with transport: on the co-directional
arm q improves free of transport cost but never reaches type;
on the counter arm transport is paid AND q worsens. The type
wall is not an amplitude effect in either direction.

## Verdict

**COMPOSITION MAKES IT WORSE — the family closes.** Priced
summary: the transversely-offset co-directional twin does
exactly half of what was posed — its on-axis shift adds
(v_eff 1.473663 → 1.671497 at a = 1, +13.4%, in band at every
rung and every offset read) and its gradient opposition halves
the flux ratio (median q 34.3 → 15.8) — but the two halves do
not meet: the q ≤ 1 population it creates (46 points, 2.47% of
defined) and the real-spectrum population it creates (13
nontrivial points, 0.20%) are **disjoint**, the crack
conjunction is 0 at a = 1 and at best 0.0735% (68× below the
registered 5% bar, at a = 0.5, on still-NEC-violating
joint-edge points), dist_Re's max never leaves 0.7071, and the
composition's interference (median |T_×|_F = 59% of |T_pair|_F
at a = 1) lands constructively on the deficits: WEC min
−0.03611 → −0.05838, NEC min −0.003771 → −0.006098, violating
share 91.2% → 96.1%, E_neg −2.590 → −4.920. A companion drive
in this family is a second wall, not a canceller: flux is
carried per-bubble by the same transverse gradients that make
each bubble's wall, the overlap region where the gradients
oppose is not where the type failure is decided, and the
fringe where q ≤ 1 appears is not where the spectrum is real.

Scope fences: this family only (co-directional twin, transverse
offset, same quintic profile, β = 1.1, this factory, this
slicing). Nothing here touches a counter-propagating or
profile-mismatched companion, which would be a different
registration. Nothing was appended to NEW_PHYSICS_LEDGER.md;
nothing external was launched; writes are inside phase245/ only.
