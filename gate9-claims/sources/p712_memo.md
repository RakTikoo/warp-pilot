# P71-2 MEMO — The joining member's formation (growth + nucleation)

Worker item P71-2, Phase 71. Run record: `p712_runrecord.md`
(registration, conventions, re-gate — all fixed before
computing). Scripts: `work/p712_growth.py`, `work/p712_g2.py`,
`work/p712_dynamic.py`, `work/p712_assemble.py`; checker
`work/p712_checker.py` — **27/27 PASS** over the result
files. float64; sympy exact algebra; mpmath 40-digit probes
at deciding points. Language lock: **scan signal under
attack** — the ceiling for everything below. Class-B
honesty label (Phase-30 pattern): the growth audit is a
prescribed-geometry morph read — a legal instant path is
necessary, not sufficient, for a physical growth process.
Scope note carried verbatim from P61-4 (registered in
§P71-2): "the read-off extends the new slice's closed form
inside its own throat, x < 1; the verdict is read-off-scoped
and the intermediate-slice fill is a different registered
read, queue item 3 below" — carried here as: the shell
failure below is a property of the registered Phase-30
Class-B read-off (the new slice's closed form extended
inside its own throat, x < 1), scored exactly as P30-1 /
P61-4 scored their rows; an intermediate-slice shell fill
would be a different registered read (Phase 71 carried
queue item 3), not a correction to this one.

## Verdicts (fixed vocabulary)

- **Growth: GROWABLE-ONLY-EXOTICALLY** — frozen family
  legal at every ladder radius; the growth increment is
  NEC-violating at every step, in two places (price table
  below is part of the verdict). Dynamic clause:
  UNCOMPUTED with the obstruction named (§a-iii) — it
  neither rescues nor is needed for this verdict form.
- **Nucleation: CLOSED (conformally-flat fork clause,
  INHERITED — stated as inherited, with the home-level
  argument in §b).**
- **Ledger standing: UNCHANGED** (tested, §Standing).

**(V-b) UNDECIDED: Pais–Uhlenbeck spin-2 ghost vs Mannheim
PT-symmetric quantisation — opposed literature positions,
B3 NOT COMPUTABLE (Phase 32).** — attached to both
verdicts.

**Plain language:** the joining member's own matter stays
legal at every size, exactly as T-b's did — but growing it
is worse than growing T-b, in a way specific to its
redshift profile. The matter you must add is already
illegal in a thin layer at the new throat's edge. And the
shell that becomes the new throat is not just illegal:
the Φ₂ profile has a pole inside the region the growth
read must extend it into (at r = r₀/e, where the profile's
logarithm hits −1), the extended matter blows up there,
and the exotic price of a growth step is not merely
astronomical like T-b's 10⁷³ × the legal supply — it is
unbounded. Nucleation stays closed, and §b argues, rather
than assumes, that P61-4's closure belongs to the whole
conformal home, this family included. The member stays
what P61-1 made it: pre-existing only, now with its
formation column measured instead of unaudited.

## Gates (all passed before any growth number was read)

- **Engine re-gate:** Phase-38 generic spherical Bach
  engine reproduces the T-b and Ellis closed forms
  EXACTLY (`validate_generic.py` PASS this run); trace
  ≡ 0 symbolically; MK Bach-flat 3.37×10⁻¹⁹ ≤ 1e-12
  (stored Phase-38 re-gate, the one P61-4 used).
- **G1 ledger reproduction:** frozen read at r₀ = 1 m
  reproduces P61-1's joining-member numbers (P61-1 EC
  convention, recorded in the run record): throat
  NEC1 = +0.00364119103852 (stored +0.003641, rel. err.
  5.2×10⁻⁵), DEC_t = +0.00182059551926 (stored +0.001820,
  3.3×10⁻⁴); static radial tidal term 0.1249803 (stored
  0.124980, 2.4×10⁻⁶); gradient at v = 0.1 c =
  1.1233×10¹⁶ s⁻² (stored 1.12×10¹⁶, 2.9×10⁻³);
  r₀* = 4.78544×10⁷ m (stored 4.785×10⁷, 9.2×10⁻⁵).
  EC signs exact. All within the 1% bar.
- **G2 conservation:** the family's conservation
  combination p_r′ + Φ′(ρ + p_r) + 2(p_r − p_t)/r
  simplifies to **0 symbolically exactly** (cleared form
  × r⁶(1 + ln r)⁸ also ≡ 0); trace ≡ 0 exactly.
- **G3 GR control:** CITED, not re-run, per §P71-2 —
  this item's pipeline components are identical to
  P61-4's (same re-gated generic engine, same EC
  combinations, same Class-B read-off, same pricing
  instrument), so P61-4's passed G3 (GR Ellis: ρ(throat)
  = −1, NEC1(throat) = −2, increment phantom-like) is
  the controlling gate. The fact is recorded here and
  in the run record.

## (a) Growth

**Frozen (i).** The family's own Bach read, T = 4α_g·B
(α_g > 0; ECs quoted in the P61-1 B-combination
convention — signs identical). All four ECs hold
**strictly at every ladder radius** r₀ ∈ {1, 10, …,
10⁶, 4.785×10⁷} m on [r₀, 10³r₀]: unit-radius minima
ρ = 6.275136×10⁻¹⁵, NEC1 = 1.229851×10⁻¹⁵, NEC2 =
1.193535×10⁻¹⁴, SEC = 1.255027×10⁻¹⁴, DEC_r =
1.229851×10⁻¹⁵, DEC_t = 6.149256×10⁻¹⁶, all at the far
tail x = 10³, positive, → 0 — matching P61-1's stored
40-digit minima (1.229852×10⁻¹⁵ / 6.149260×10⁻¹⁶) to
five digits, an independent cross-check of the frozen
read. **Scale covariance stated and verified:**
T(r; r₀) = r₀⁻⁴F(r/r₀) componentwise (Φ₂ is a function
of r/r₀); verified by DIRECT (unscaled) evaluation at
r₀ = 10 and r₀ = 10³ m against the scaled read — max
relative deviation 0.0 at both radii (the direct and
scaled evaluations agree to float64 exactly on the
sampled points).

**Increment (ii) — common domain.** ΔT on
[r₀_{j+1}, 10³r₀_{j+1}]: ρ, NEC2, SEC pass at every
step (minima at the far tail, positive). **NEC1, DEC_r,
DEC_t fail at every step, but only in a thin inner-edge
layer:** the minimum sits exactly at x_b = r/r₀_{j+1} =
1, ΔNEC1 = **−0.016680 r₀_{j+1}⁻⁴** (decade steps,
scale-free; −0.002134 r₀_{j+1}⁻⁴ for the final partial
step), and the failure extends only over x_b ∈ [1,
1.00348] (crossing bisected). Mechanism, exact analogue
of P30-1's f(T) edge identity: at the new throat the new
slice's NEC1 is only 0.003641 r₀_{j+1}⁻⁴, while the old
slice's NEC1 at that same radius is larger (scaled value
0.020320 r₀_{j+1}⁻⁴ for a decade step) — growing replaces
stronger-NEC1 matter with weaker at the edge, so the
increment there is NEC-negative. (T-b escaped this
because its throat NEC1, 0.4167 in the same convention,
exceeds its old-slice value at the edge.) The layer's
integrated negative-NEC1 content is finite: **5.83×10⁶⁸
× E_legal per decade step** (scale-free).

**Increment (ii) — grown shell.** The new slice's matter
on [r₀_j, r₀_{j+1}] (Class-B read-off) violates **all**
ECs at every step, on roughly half the scaled shell
domain, in two anatomically distinct ways:
(1) *Regular failure near the throat:* NEC1 < 0
immediately inside the throat — 40-digit probe at
x_b = 0.99: NEC1 = −0.0500024683181 (B-convention,
r₀_{j+1}⁻⁴ units); ρ < 0 by x_b = 0.9 (probe NEC1 =
−1.41540940753, ρ = −1.00227306856 at x_b = 0.9).
(2) *The Φ₂ pole inside the extension:* Φ₂ =
a·L/(1 + L), L = ln x_b, has a pole at **x_b = e⁻¹ =
0.367879** (L = −1: Φ → −∞ from above, +∞ from below) —
inside every shell interval (decade shells span x_b ∈
[0.1, 1]; the final partial shell [0.0209, 1]). The
extended slice is not a regular geometry there, and
every EC combination diverges: 40-digit probes give
NEC1 = −6.58154461639×10²¹ at x_b = e⁻¹(1 − 10⁻³) and
−6.64506547545×10⁴² at e⁻¹(1 − 10⁻⁶) — a pole of order
≈ 7 in |1 + ln x_b|, **non-integrable**. Grid minima
(pole neighbourhood |1 + ln x_b| ≤ 0.01 excluded) sit
at the pole-adjacent grid point x_b = 0.3641 for every
EC at every step, scale-free in scaled units (e.g.
shell NEC1 grid min = −5.383×10¹⁰ r₀_{j+1}⁻⁴-scaled at
the 1→10 m step, ∝ r₀_{j+1}⁻⁴ thereafter). This pole is
a property of the Φ₂ profile itself, not of the
numerics: it is the same slow-tail logarithm that made
Φ₂ the joining profile, read inside its own throat.

**Dynamic (iii).** The time-extended spherical Bach
derivation was **attempted** in the P61-4 pattern
(Phase-32 `bach_engine.bach_mixed` on b(r,t) =
r₀(t)(r/r₀(t))^0.1, Φ(r,t) = Φ₂(r/r₀(t)), r₀(t)
log-smoothstep 1→10 m, T_s = 10⁴; script
`work/p712_dynamic.py`, progress record
`p712_dynamic_progress.json`). **It did not close:**
the derivation's Ricci/scalar simplification stage did
not return within the item's compute window (~600
CPU-seconds in the first attempt, terminated by the
runtime; a bounded 480 s retry likewise did not
return), whereas P61-4's Φ = 0 derivation closed on
the same engine. Obstruction, named: expression swell
in the time-extended Bach system when Φ depends on t
through ln(r/r₀(t)) — every mixed component carries
Φ_t, Φ_tr terms in (1 + ln(r/r₀(t))) denominators that
have no Φ = 0 analogue; P61-4's saved dynamic
expressions are Φ = 0-specific and do not transfer.
The dynamic clause is therefore reported **UNCOMPUTED**
exactly as registered. It does not affect the verdict
form: the increment already violates the NEC, which is
what GROWABLE-ONLY-EXOTICALLY scores. Follow-up
registered below (FU-P712-1).

**Pricing (iv).** The shell's integrated
negative-NEC1 content per step (T = 4α_g·B convention,
P61-4 pattern) against E_legal(L) = (3/(32π²))ħc/L at
L = r₀_{j+1}. Because of the pole, the un-excluded
integral **diverges**; the table gives LOWER BOUNDS at
pole-exclusion ε in |1 + ln x_b|, identical at every
decade step (scale-free):

| Step | ratio ≥ (ε = 10⁻²) | ratio ≥ (ε = 10⁻³) | ratio ≥ (ε = 10⁻⁴) |
|---|---|---|---|
| each decade step 1→10 … 10⁵→10⁶ m | 6.925×10⁸⁴ | 7.327×10⁹⁰ | 1.711×10⁹⁶ |
| final partial 10⁶→4.785×10⁷ m | 6.984×10⁸⁴ | 5.458×10⁹⁰ | 5.411×10⁹⁵ |

The bound grows ≈ ε⁻⁶ as ε → 0 (the NEC1 pole order
≈ 7, integrated against r²dr) — the shell's exotic
content per decade step exceeds **any** finite multiple
of E_legal; even at the loosest exclusion it is ~84
orders above the legal supply, against T-b's finite
2.216×10⁷³. The common-domain edge layer adds a finite
5.83×10⁶⁸ × E_legal per decade step, negligible beside
the shell bound. The frozen family's own exotic
content is 0 by legality (stated, not priced as a
demand).

**Accretion law: NAMED ABSENCE** (as P61-4). No
conformal-gravity accretion law exists in the sourced
literature; the González-Díaz/Debnath law is
GR-specific and was not borrowed; the in-family
increment read stands alone.

## (b) Nucleation — inheritance audit

**Question registered:** is P61-4's conformally-flat
fork a property of the conformal HOME or of the T-b
FAMILY? **Argument:** the fork's three components each
quantify over the home or over geometry as such, never
over a throat family: (1) the Strominger–Horowitz–Perry
instantons are extrema of the conformal ACTION —
vacuum-tunneling saddles with topological action, no
throat, no S_E(r₀) — a statement about the action's
Euclidean sector; (2) the Giddings–Strominger class is
conformally flat because ALL Robertson–Walker metrics
have C_μνρσ = 0 (sourced in P61-4; verified in-item
there: the Bach engine on a general RW metric returns
B ≡ 0) — a statement about a geometry class; (3) the
(H-GR) analogue was rejected because it prices an
Einstein–Hilbert bounce on that class, where this
home's action vanishes identically and the geometry is
not a Bach solution with its axion matter (B = 0 would
force T = 0) — a statement about the home's field
equation. No premise mentions b = √(r r₀), Φ = 0, or
any (p, Φ, a). The joining member lives in the same
home — same action, same Bach equation T = 4α_g·B,
same scored gauge Ω = 1 (this item's G1/G2 ran on the
same re-gated engine) — so a family-specific escape
would need a sourced instanton class with C ≠ 0 that
creates a throat, solves the Bach system with its
matter, and is specific to the Φ₂ family. None exists
on record: P61-4's sourced search contains no
family-specific Euclidean throat bounce for ANY family
of this home, and this item's re-examination for
family-specificity found none (the Lorentzian
Weyl-gravity wormholes of Varieschi–Ault /
Heydari-Fard et al. are classical solutions of other
families of the same home, not nucleation saddles for
any family). **The fork is therefore a property of
the HOME, and it covers the Φ₂ family.** No P28-2
pricing run is triggered (no family-specific
instanton class sourced); the analogue is not forced.

**NUCLEATION CLOSED** — deciding clause: the
conformally-flat fork, **INHERITED** from P61-4 (stated
as inherited, argument above). Derivation class
attached: the only candidate price on record is the
(H-GR) area law, derivation class **(B)**, and it is
rejected for this home, not quoted as this family's
rate.

## Formation-column output (verbatim-ready replacement clause)

> **PRE-EXISTING ONLY.** The topology must be in the
> initial data or the Planck foam; creation is
> classical topology change, priced by P28-1's E4.
> Growth: GROWABLE-ONLY-EXOTICALLY (Phase 71 P71-2) —
> the frozen joining-member family (p = 0.1, Φ₂,
> a = 0.277734) is EC-legal at every radius from 1 m
> to its tidal-bar radius r₀* = 4.785×10⁷ m, but the
> growth increment is NEC-violating at every step:
> the common-domain increment fails NEC1/DEC at the
> new throat's edge in a thin layer (x_b ∈
> [1, 1.00348], ΔNEC1 = −0.016680 r₀_{j+1}⁻⁴,
> scale-free), and the grown shell at each step
> carries matter violating all four ECs, singular at
> the Φ₂ profile's own pole x_b = e⁻¹ inside the
> Class-B read-off extension, so the shell's
> integrated negative-NEC1 content per decade step
> is unbounded (lower bounds: ≥ 6.93×10⁸⁴ × E_legal
> at pole-exclusion 10⁻², growing ≈ ε⁻⁶ — price
> table in P71-2 memo), so growth from a seed is
> possible only by accreting exotic matter in the
> shell layer; the dynamic clause is UNCOMPUTED
> (time-extended Bach derivation for Φ₂(r,t) did not
> close; obstruction named in P71-2 memo).
> Nucleation: CLOSED for this home (Phase 71 P71-2,
> inherited from Phase 61 P61-4 with the home-level
> argument stated) — no conformal-gravity instanton
> creating a throat exists on record for any family
> of this home, and the Giddings–Strominger
> Euclidean wormhole class is conformally flat, so
> its Weyl action vanishes identically and it is not
> a solution of the Bach system; the (H-GR) area-law
> analogue (derivation class (B)) is therefore not
> borrowed. (V-b) UNDECIDED: Pais–Uhlenbeck spin-2
> ghost vs Mannheim PT-symmetric quantisation —
> opposed literature positions, B3 NOT COMPUTABLE
> (Phase 32).

## Standing

**Tested, not assumed: UNCHANGED.** The member's
standing rests on P61-1's junction verdict (JOINS WITH
LEGAL SHELL at r_Σ = 10³ r₀ only), its tidal bar
(r₀* = 4.785×10⁷ m) and (V-b) UNDECIDED — none of
which the growth or nucleation reads touch. Growth is
exotic-only with an unbounded shell price and
nucleation is closed, so neither supplies a route
that could change the standing; formation completes
the member's column without rescuing it (the Phase-28
pattern, confirmed for this member).

## Failure Protocol — anatomies and follow-ups

- **Dynamic non-closure (anatomy):** the time-extended
  Bach derivation for Φ₂(r,t) stalls in the Phase-32
  engine's simplification stage on Φ_t-bearing terms
  with (1 + ln(r/r₀(t))) denominators; the Φ = 0 case
  (P61-4) closed on the same engine, so the
  obstruction is the profile's t-coupled logarithm,
  not the engine. **FU-P712-1:** re-attempt the dynamic
  derivation with a sparse/no-simplify Bach assembly
  (the phase38 derive_generic sparse pattern extended
  to (r,t)), or with the schedule frozen in scaled
  coordinates x = r/r₀(t) before differentiation; if
  it closes, audit at u ∈ {0.25, 0.5, 0.75},
  x ∈ {1.001, 3, 30} as in P61-4, plus a second
  schedule T_s = 10⁵ for rate-independence (joining
  FU-P614-1). Reopening condition for the dynamic
  clause: that run.
- **Shell pole (anatomy, not an instrument failure):**
  the Class-B read-off extends the new slice inside
  its own throat, x_b < 1, where Φ₂'s logarithm hits
  its pole at x_b = e⁻¹; the divergence is in the
  profile's closed form (40-digit probes on both
  sides), not in any grid. **FU-P712-2:** the
  intermediate-slice shell fill (Phase 71 carried
  queue item 3) is the registered alternative read;
  note it must still cross x_b = e⁻¹ in scaled
  coordinates for every slice with r₀ < r < e·r₀ —
  whether ANY in-family fill avoids the pole layer
  is a question that read should state at
  registration. The verdict here rests on the
  registered read, exactly as P61-4's did.
- **Common-domain edge layer (anatomy):** a thin,
  finite, scale-free NEC failure at the new throat's
  edge (mechanism in §a) — it alone would already
  force the EXOTICALLY verdict form; the shell pole
  sets the price. No follow-up needed beyond
  FU-P712-2 (a fill read would re-score the edge
  layer too).
- **Nucleation (reopening condition, inherited):** a
  published conformal-gravity Euclidean
  bounce/instanton whose geometry has C_μνρσ ≠ 0 and
  which creates a throat, with an action computable
  as a function of throat radius — the class-(A)
  computation registered in CHECKPOINT61 §P61-4(b)
  would run unchanged, for this family as for T-b.

## C12 accounting

Computed: engine re-gate; G1 (40-digit throat probes +
tidal/gradient/r₀* reads); G2 (symbolic conservation
≡ 0, trace ≡ 0); frozen ECs at 8 ladder radii with
scale covariance verified by direct evaluation at two
radii (deviation 0.0); increment ECs on common domains
and Class-B shells at 7 steps, with the edge-layer
crossing bisected and its integrated content priced;
shell pricing as pole-exclusion lower bounds at three
exclusions × 7 steps; 40-digit probes at the throat,
three shell points, both sides of the pole (two
offsets), and the tail; dynamic derivation attempted
twice (did not close — UNCOMPUTED, obstruction named).
Cited, not re-run: G3 GR control (P61-4's, pipeline
identical — recorded). Argued, not assumed: nucleation
inheritance (home-level argument; no family-specific
instanton sourced, so no pricing run). Claimed:
exactly the two verdicts above, at Class-B morph
honesty for growth, with the dynamic clause and the
shell-read scope declared as open clauses. Nothing
uploaded. INTERNAL only.

Files: results/p712_runrecord.md, p712_memo.md,
p712_results.json, p712_checker.json,
p712_growth_raw.json, p712_g2.json,
p712_dynamic_progress.json; scripts in work/
(p712_growth.py, p712_g2.py, p712_dynamic.py,
p712_assemble.py, p712_checker.py).
