# P61-4 MEMO — Formation completion, conformal row (growth + nucleation)

Worker item P61-4, Phase 61. Run record: `p614_runrecord.md`
(registration, sources, re-gate — all fixed before computing).
Scripts: `work/p614_growth.py`, `work/p614_context.py`,
`work/p614_dynamic.py`, `work/p614_dynamic_audit2.py`,
`work/p614_assemble.py`; checker `work/p614_checker.py` —
**22/22 PASS** over the result files. float64; sympy exact
algebra; 40-digit probes at deciding points. Language lock:
**scan signal under attack** — the ceiling for everything
below. Class-B honesty label (Phase-30 pattern): the growth
audit is a prescribed-geometry morph read — a legal instant
path is necessary, not sufficient, for a physical growth
process.

## Verdicts (fixed vocabulary)

- **Growth: GROWABLE-ONLY-EXOTICALLY** — frozen family legal
  at every ladder radius; the growth increment's shell layer
  is NEC-violating at every step (price table below is part
  of the verdict). Dynamic clause reported in full below —
  it neither rescues nor further closes the verdict form.
- **Nucleation: CLOSED** — deciding clause: **the
  conformally-flat fork** (no coherent instanton/scaling
  model exists for this home; the (H-GR) analogue, derivation
  class (B), is indefensible here and was not borrowed).
- **Ledger standing: UNCHANGED** (tested, §Standing).

**(V-b) UNDECIDED: Pais–Uhlenbeck spin-2 ghost vs Mannheim
PT-symmetric quantisation — opposed literature positions,
B3 NOT COMPUTABLE (Phase 32).** — attached to both verdicts.

**Plain language:** the conformal throat's matter stays legal
at every size, and the matter you must add in the open region
when it grows is legal too — but the thin shell that becomes
the new throat is not: there the added matter breaks the
null energy condition at every size, by the same fraction,
forever, and the price of that exotic shell layer is about
10⁷³ times the legal quantum supply at that radius. And
there is no way to create such a throat by quantum tunneling
that this theory itself prices: the only Euclidean wormholes
on record are shapes on which conformal gravity's action is
exactly zero. So the row stays what Phase 38 said it was —
pre-existing only — now with both gaps measured instead of
labelled UNCOMPUTED.

## Gates (all passed before any growth number was read)

- **Engine re-gate:** Phase-38 generic spherical Bach engine
  reproduces the T-b and Ellis closed forms EXACTLY
  (validate_generic PASS this run); trace ≡ 0 symbolically;
  MK Bach-flat max |B| = 3.37×10⁻¹⁹ ≤ 1e-12.
- **G1 ledger reproduction:** frozen T-b read at r₀ = 1 m
  gives tidal gradient 2.2696×10¹⁴ s⁻² (stored 2.27×10¹⁴,
  rel. err. 1.8×10⁻⁴) and r₀* = 6.8023×10⁶ m (stored
  6.802×10⁶, rel. err. 3.9×10⁻⁵); EC signs exact (closed-form
  positivity certificate, Phase 32).
- **G2 conservation:** the T-b conservation combination
  p_r′ + 2(p_r − p_t)/r simplifies to **0 symbolically
  exactly** at general r₀; trace ≡ 0 exactly.
- **G3 GR control:** the same pipeline on GR Ellis returns
  ρ(throat) = −1, NEC1(throat) = −2 (code units), increment
  phantom-like under growth (Δρ, ΔNEC1 < 0 everywhere) — the
  pipeline sees the asymmetry it tests for.

## (a) Growth

**Frozen (i).** T-b matter from the family's own Bach read,
T = 4α_g·B (α_g > 0; α_g = 1 code units, components m⁻⁴):
ρ = (5α_g/6)(3u−1)/(r₀⁴x⁵), p_r = −(5α_g/12)(4u−1)/(r₀⁴x⁵),
p_t = (5α_g/24)(10u−3)/(r₀⁴x⁵), x = r/r₀, u = √x. All four
ECs hold **strictly at every ladder radius** r₀ ∈ {1, 10,
…, 10⁶, 6.802×10⁶} m on [r₀, 10³r₀] (minima at the far tail,
positive, → 0). **Scale covariance stated and verified:**
T(r; r₀) = r₀⁻⁴F(r/r₀) componentwise; verified numerically
at r₀ = 1 and 10³ m under λ = 10 rescaling, max relative
deviation < 1e-12. Context members (p ∈ {0.4, 0.6}, Φ = 0,
Φ₁/Φ₂ at a = −0.1) are likewise frozen-legal at r₀ = 1 m
(generic-engine read; r₀ = 10 m spot check reproduces the
scaled read to ~1e-14) — region context only, as registered.

**Increment (ii).** On the common domain [r₀_{j+1}, 10³r₀_{j+1}]
ΔT passes **all four ECs at every ladder step** (each EC
combination of a slice is ∝ (au−b)/(r₀⁴x⁵) with a/2 ≥ b for
every combination — NEC1/DEC saturate the bound a/2 = b —
so every slice's matter grows monotonically in r₀ at fixed
r; minima sit at the far tail, positive). **The grown shell
fails:** the new slice's matter on [r₀_j, r₀_{j+1}] (Phase-30
Class-B read-off) has NEC1 ∝ (2u−1), DECt ∝ (2u−1),
ρ, SEC ∝ (3u−1) in the shell's scaled coordinate — negative
for r < r₀_{j+1}/4 (NEC1, DECt) and r < r₀_{j+1}/9 (ρ, SEC),
at **every step, scale-free** (the same u-interval each
time; no refined ladder can move it). Worst point: the
shell's inner edge, NEC1 = −1.5314352831930172… m⁻⁴ (40-digit
probe, step 1→10 m; ∝ r₀_{j+1}⁻⁴ thereafter). Mechanism: the
closed form's numerators (au−b) are positive only for
u ≥ 1, i.e. on the slice's own domain; the shell read-off
extends the new slice's matter inside its own throat, where
those numerators change sign. This is the exact analogue of
P30-1's f(T) increment anatomy (a scale-free shell-layer
failure), with NEC in place of DEC_r.

**Dynamic (iii).** The time-extended spherical Bach
derivation **closed**: b(r,t) = √(r·r₀(t)), Φ = 0, r₀(t)
log-smoothstep over the decade 1→10 m at quasistatic
schedule T_s = 10⁴ (by verified scale covariance, one decade
is every decade in scaled units). The saved expressions
validate: trace = 0 to ≤ 2.1×10⁻¹² relative at all sampled
points, B^r_θ ≡ 0, and at x = r/r₀(t) ≥ 3 the dynamic matter
agrees with the static closed forms at the instantaneous
r₀(t) to ≤ 3×10⁻³ (the quasistatic tax). Sampled read
(u = t/T_s ∈ {0.25, 0.5, 0.75}; x ∈ {1.001, 3, 30, 1000}):
**all ECs pass at x = 3 and x = 30 at all three times**;
**the read fails at x = 1.001 at all three times**
(ρ = −1.63×10², −5.95×10¹, −6.87 m⁻⁴; NEC radial likewise
negative) — a thin layer at the moving throat where the
(1 − b/r)⁻ⁿ factors amplify the schedule-derivative terms.
The x = 1000 samples sit at ~1e-16 absolute, below the
evalf instrument floor, and are excluded. Whether the
near-throat failure is rate-independent is **UNRESOLVED**:
one schedule was computed; the layer's terms scale as
T_s⁻² amplified by (1−b/r)⁻ⁿ, which predicts shrinkage at
slower rate without establishing it. Follow-up registered
below. (Instrument note: float64 lambdify of the saved
expressions overflows on intermediate exp(+359) factors
that cancel exactly; the audit used sympy evalf, which
handles the cancellation — recorded in the raw file.)

**Pricing (iv).** The common-domain increment contributes
zero negative energy. The shell's integrated NEC1-violating
content per step, against E_legal(L) = (3/(32π²))ħc/L at
L = r₀_{j+1} (code-unit integral converted at c⁴/G):

| Step | E_legal (J) | Shell negative-NEC1 content (J) | Ratio |
|---|---|---|---|
| 1→10 m | 3.003×10⁻²⁹ | 6.656×10⁴⁴ | 2.216×10⁷³ |
| 10→10² m | 3.003×10⁻³⁰ | 6.656×10⁴³ | 2.216×10⁷³ |
| 10²→10³ m | 3.003×10⁻³¹ | 6.656×10⁴² | 2.216×10⁷³ |
| 10³→10⁴ m | 3.003×10⁻³² | 6.656×10⁴¹ | 2.216×10⁷³ |
| 10⁴→10⁵ m | 3.003×10⁻³³ | 6.656×10⁴⁰ | 2.216×10⁷³ |
| 10⁵→10⁶ m | 3.003×10⁻³⁴ | 6.656×10³⁹ | 2.216×10⁷³ |
| 10⁶→6.802×10⁶ m | 4.415×10⁻³⁵ | 2.000×10³⁸ | 4.530×10⁷² |

The frozen family's own exotic content is 0 by legality
(stated, not priced as a demand).

**Accretion law: NAMED ABSENCE.** No conformal-gravity
accretion law exists in the sourced literature (searches
recorded in the run record). The González-Díaz/Debnath law
is GR-specific and was not borrowed; the in-family
increment read stands alone. (Its GR pattern — phantom
accretion grows, legal accretion shrinks — is neither
confirmed nor contradicted here: the common-domain
increment is legal *and* growing, and the exoticity sits
in the shell layer, an object the GR law does not describe.)

## (b) Nucleation

**Sourced search.** Conformal-gravity instantons exist:
Strominger–Horowitz–Perry (Nucl. Phys. B238 (1984) 653)
found asymptotically Euclidean extrema of the conformally
invariant action, of arbitrary Euler number and Hirzebruch
signature, describing tunneling between zero-curvature
vacua and between flat space and topologically non-trivial
zero-energy initial data. They are **not** throat-creating
bounces: no Morris–Thorne handle is created, and their
action is fixed by topological invariants, not by a throat
radius — there is no S_E(r₀) to fit, so the class-(A)
computation has no object. Lorentzian wormholes in Weyl
gravity (Varieschi–Ault; Heydari-Fard et al.) are classical
solutions, not nucleation bounces.

**The registered fork — deciding.** The
Giddings–Strominger Euclidean wormhole is O(4)-symmetric
of Robertson–Walker form dτ² + a(τ)²dΩ₃². All RW metrics
have C_μνρσ = 0 (sourced: J. Math. Phys. 48 (2007) 122501 —
"the Weyl tensor for all Robertson–Walker cosmological
metrics vanishes"; **verified in-item**: the Phase-32 Bach
engine on a general RW metric a(t) returns B^μ_ν ≡ 0
componentwise). Therefore, for this home: (1) the Weyl
action of the candidate bounce vanishes **identically**;
(2) the geometry is not even a solution of the home's
equations with its axion matter — B = 0 forces T = 0 under
T = 4α_g·B, and the axion's T ≠ 0. What prices the GS
bounce in the literature is the Einstein–Hilbert + axion
matter action (with boundary terms) — **a different
theory's action**. No source prices a throat bounce inside
conformal gravity; that is a named absence, not a gap this
item may fill by borrowing.

**Analogue — rejected, not forced.** Borrowing P28-2's
(H-GR) area law S_E/ħ = C(r₀/l_P)² with C = π, p = 2
(derivation class **(B)**, stored in
`phase28/results/p282_results.json`) would give, with the
class attached to every number: S_E/ħ = 3.14 at l_P,
1.20×10⁵⁸ at 1 μm, 1.20×10⁶⁴ at 1 mm, 1.20×10⁷⁰ at 1 m,
5.56×10⁸³ at r₀* (all derivation class (B)); log₁₀Γ =
−5.22×10⁶⁹ at 1 m and −2.42×10⁸³ at r₀* (derivation class
(B)); S_E/ħ ≤ 10² only within 5.64 l_P of l_P (derivation
class (B)). But every one of those numbers prices an
Einstein–Hilbert bounce on a geometry class where this
home's action is identically zero and which is not a Bach
solution — the analogue is **indefensible for this home**,
so per the registration it is not used and the verdict is:

**NUCLEATION CLOSED** — deciding clause: the
conformally-flat fork; no coherent instanton/scaling model
exists for the home (P28-2 CLOSED vocabulary). Derivation
class attached: the only candidate price on record is
class (B) (H-GR), and it is rejected, not quoted as this
home's rate.

## Formation-column output (verbatim-ready replacement clause)

> **PRE-EXISTING ONLY.** The topology must be in the initial
> data or the Planck foam; creation is classical topology
> change, priced by P28-1's E4. Growth: GROWABLE-ONLY-
> EXOTICALLY (Phase 61 P61-4) — the frozen T-b family is
> EC-legal at every radius from 1 m to the tidal-bar radius
> r₀* = 6.802×10⁶ m and the common-domain growth increment
> is EC-legal at every step, but the grown shell at each
> step carries NEC-violating matter (NEC1 fails for
> r < r₀_{j+1}/4, scale-free; integrated negative-NEC1
> content per decade step = 2.22×10⁷³ × E_legal at that
> radius — price table in P61-4 memo), so growth from a
> seed is possible only by accreting exotic matter in the
> shell layer; the dynamic read at quasistatic rate passes
> outside the throat layer and fails inside it,
> rate-independence unresolved. Nucleation: CLOSED for
> this home (Phase 61 P61-4) — no conformal-gravity
> instanton creating a throat exists on record, and the
> Giddings–Strominger Euclidean wormhole class is
> conformally flat, so its Weyl action vanishes identically
> and it is not a solution of the Bach system; the (H-GR)
> area-law analogue (derivation class (B)) is therefore
> not borrowed. (V-b) UNDECIDED: Pais–Uhlenbeck spin-2
> ghost vs Mannheim PT-symmetric quantisation — opposed
> literature positions, B3 NOT COMPUTABLE (Phase 32).

## Standing

**Tested, not assumed: UNCHANGED.** The row's standing
rests on the junction verdict (DOES NOT JOIN, P38-3), the
tidal bar (r₀* = 6.802×10⁶ m) and (V-b) UNDECIDED — none of
which the growth or nucleation reads touch. Growth is
exotic-only and nucleation is closed, so neither supplies
a route that could change the standing; formation completes
the column without rescuing the row (the Phase-28 pattern,
confirmed for this row).

## Failure Protocol — anatomies and follow-ups

- **Dynamic near-throat layer (anatomy):** the failure is
  localised to x ≲ 3 at the sampled schedule, in the layer
  where (1 − b/r)⁻ⁿ amplifies ṙ₀/r̈₀ terms; outside it the
  dynamic read is the frozen read plus a ≤ 3×10⁻³ tax.
  **FU-P614-1:** second schedule T_s = 10⁵ with the same
  sampled audit — if the layer's NEC deficit scales as
  T_s⁻² it is a rate tax (and the dynamic clause softens to
  "passes at sufficiently slow rate, layer width ∝ rate");
  if it does not move, the failure is rate-independent and
  the growth verdict must be re-scored against NOT
  GROWABLE. Reopening condition for the dynamic clause:
  that run.
- **Shell extension (declared scope):** the shell failure
  is a property of the Phase-30 Class-B read-off (the new
  slice's closed form extended inside its own throat,
  x < 1), exactly as P30-1 scored its rows (its GR control's
  shell row fails the same way; its f(T) shell happened to
  pass). A morph parametrisation that fills the shell with
  intermediate-slice throat matter instead would be a
  different registered read, not a correction to this one;
  it is named here so the coordinator can register it if
  wanted. The verdict rests on the registered read.
- **Nucleation (reopening condition):** a published
  conformal-gravity Euclidean bounce/instanton whose
  geometry has C_μνρσ ≠ 0 and which creates a throat, with
  an action computable as a function of throat radius —
  the class-(A) computation is registered in CHECKPOINT61
  §P61-4(b) and would run unchanged.

## C12 accounting

Computed: frozen ECs + conservation at 8 ladder radii and
6 context members; increment ECs on common domains and
shells at 7 steps; pricing at 7 steps; dynamic Bach
derivation (closed) + sampled audited read (12 points, 3
times × 4 radii, x = 1000 row excluded as below floor);
nucleation literature search + fork verification (in-item
RW Bach-flat check). Claimed: exactly the two verdicts
above, at Class-B morph honesty for growth, with the
dynamic rate-independence and the shell-read scope
declared as open clauses. Nothing uploaded. INTERNAL only.

Files: results/p614_runrecord.md, p614_memo.md,
p614_results.json, p614_checker.json, p614_growth_raw.json,
p614_context_raw.json, p614_dynamic_raw.json,
p614_dynamic_bach.json, p614_dynamic_progress.json;
scripts in work/ (p614_growth.py, p614_context.py,
p614_dynamic.py, p614_dynamic_audit.py [superseded by
p614_dynamic_audit2.py — lambdify overflow, see memo],
p614_dynamic_audit2.py, p614_assemble.py, p614_checker.py).
