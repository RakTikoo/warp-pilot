# P21-4 run record — stated BEFORE any scan number was read

Item (fixed, CHECKPOINT21 §P21-4): f(T,B) — the boundary-term
teleparallel sector — on the shared Finalist-A wall bed, β ∈
{0.1, 1.1, 1.5} DIRECT, tetrad of record = good areal
Böhmer–Harko–Lobo tetrad of P10-3/P11-1/P12-1 with the
covariant spin connection (the programme's p111_d path:
Weitzenböck coframe + spin connection restored in the
covariant reading, as in P12-1/P19-3). Bounded by P12-1's
KILL (pure f(T), published tensor) and P19-3's six-function
Lorentz floor (independent-point rel_med 0.298 / 0.330 at
β = 1.1 / 1.5 vs the 0.02 bar). Language: ALIGNMENT /
KILL — TELEPARALLEL CLOSES / INTERMEDIATE exactly as
registered in CHECKPOINT21 §P21-4; nothing here is called
a candidate. Steering (Rakshit, 2026-11-21 21:38 PT):
superluminal points at FULL grid care, no thinning; the
memo carries a separate rung-2a (FTL) paragraph.

Environment: system python3, float64 everywhere (numpy
2.2.6 / scipy 1.14.1). tol = 1.430e-4 (P12-1's value, same
bed, same construction).

## SURVEY ADDENDUM — published f(T,B) equations used

Source: S. Bahamonde, C. G. Böhmer & M. Wright, "Modified
teleparallel theories of gravity", Phys. Rev. D 92 (2015)
104042, arXiv:1508.05120 (fetched and read in-run).
Definitions (their Eqs. 10–17): torsion vector
T_μ = T^λ_{λμ}; torsion scalar T (their S^{abc}T_{abc});
boundary term B = (2/e) ∂_μ(e T^μ) = 2 ∇_μ T^μ; identity
R = −T + B (their Eq. 16). Action (their Eq. 22):
S = ∫ [κ^{-1} f(T,B) + L_m] e d⁴x.
Field equations used — their Eq. (42), the covariant
metric form of their Eq. (29):

  H_μν := −f_T G_μν + g_μν □f_B − ∇_μ∇_ν f_B
          + ½ (B f_B + T f_T − f) g_μν
          + 2 [ (f_BB + f_BT)(∇_λ B)
              + (f_TT + f_BT)(∇_λ T) ] S_ν^{ λμ }
        = 8π Θ_μν ,                                        (42)

with S the published superpotential (their Eqs. 14–15),
□, ∇ the Levi-Civita operators, and all f-partials at
(T,B). Registered limits (their §III A–C, used as gates):
(i) f_B = 0 ⇒ the f(T) equations (their Eq. 31);
(ii) f = F(−T+B) = F(R) ⇒ the standard f(R) equations
(their Eq. 40): F R_μν − ½ F_val g_μν + g_μν □F
− ∇_μ∇_ν F = 8π Θ_μν, F := dF/dR; (iii) Lorentz
invariance holds iff the antisymmetric part vanishes,
which forces (their Eq. 43) f_BB + f_BT = 0 and
f_TT + f_BT = 0 — i.e. only the f(R) sub-class is
Lorentz invariant; every other f(T,B) row carries an
antisymmetric residual, which is exactly the item's
Lorentz-floor read. Conservation ∇^μΘ_μν = 0 holds on
shell via their Eqs. (46)–(52) once the antisymmetric
equations hold. Scalar-tensor representation (Bahamonde
et al., Phys. Rev. D 92 (2015); Bahamonde & Capozziello,
Eur. Phys. J. C 77 (2017) 107): f(T,B) is equivalent to
a two-scalar representation with the B-sector scalar's
kinetic/mass sign controlled by the (T,R)-frame second
derivative g_RR (below) — in the f(R) limit this is the
standard F′(R) Dolgov–Kawasaki sign. Tensor speed
c_T = 1 for f(T,B) (Bahamonde et al., gravitational-wave
sector of f(T,B): the tensor mode is luminal, as in
f(T)); reported as a case-2 pass label, not gated.

### Programme-convention transcription (stated, gated)

The programme's torsion scalar of record (p111_d) is
t := T_prog = −T_BBW (p111_d flips S and T against its
raw contraction; with this sign f = t is TEGR, matching
P12-1). The checkpoint's B is defined by R = −t + b,
i.e. b := R + t. BBW variables in programme data:
u := T_BBW = −t, v := B_BBW = R − t = b − 2t
(R from the programme Einstein tensor, R = −tr_g G,
orthonormal trace −G_00+G_11+G_22+G_33).
Families are functions φ(t,b); the BBW function is
F(u,v) = φ(−u, v−2u). All partials to third order are
carried through the linear map (dt,db)_u = (−1,−2),
(dt,db)_v = (0,1) exactly. Eq. (42) is then assembled
covariantly from: G (verify_metric), the superpotential
contraction Z_X,μν := S_ν^{λμ}∇_λX built with the
p111_d S construction (the same contraction that gives
P12-1's published W for X = t — identity-checked in the
gate), gradients/Hessians of t and R by central FD
stencils on the scalar fields (t from the torsion path;
R = t + B_b with B_b = 2∇·T_vec from the torsion vector
— its sign/normalisation fixed numerically against
R = −tr G in the gate), and the chain rule for
∇∇f_B (third partials included — the equations are
fourth order in the B sector, as BBW state).
Θ_req := H/8π; correction C := H − G; supply ratio and
ratio-free cross-check exactly as P12-1 (the scalar
∝ g_μν term drops out of every null contraction, so
binding/volume NEC reads are insensitive to it; it does
enter WEC/SEC/DEC and conservation, where the BBW
Eq. (42) sign is used — one documented deviation from
P12-1's ∝g sign, which cannot affect any P12-1 verdict
because every P12-1 verdict read is a null contraction
or the antisymmetric part).

## Families (exact normalisations fixed here; L_w = 10)

(B1a) f = t + γ L_w² b².   γ dimensionless (the
      checkpoint's "γ(B²/L_w²)" read in the bed's
      (κ, L_w) convention as the PL2-analogous
      γ L_w² B²: units L⁻² ✓).
(B1b) f = t + γ |b|^{1/2} / L_w
      [= γ L_w^{-2} (|b| L_w²)^{1/2}]. Partials singular
      at b = 0 (f_b ~ |b|^{-1/2}, f_bb ~ |b|^{-3/2}):
      any binding point with a non-finite partial fails
      health by the convention below — stated in advance.
(B2)  f = t + α L_w² t² + γ L_w² b²  (P12-1's PL n=2
      with α = κ_PL2, PLUS the B1a B-sector; γ = 0 rows
      are the in-run PL2 regression against P12-1).
(B3)  CONTROL: f = F(−t+b) = F(R), F(R) = R·exp(κ L_w² R)
      — the P12-1 (E) exponential form with argument R.
      Gate (below) must pass BEFORE scan numbers.
GR control: φ = t (H ≡ G exactly, algebraic).

## Gates stated before running

(G1) B3 CONTROL GATE (p214_gate.py, runs first): at
  β ∈ {1.1, 1.5}, 12 binding points, κ ∈ {−5, 1, 20}:
  H_cov from this machinery vs the textbook f(R) LHS
  (Eq. 40) computed independently from (G, R, ∇R, ∇∇R):
  PASS iff median relative Frobenius difference
  ≤ 0.05 at both β (FD-tolerance scale of the bed).
  Also: GR control max|H−G| = 0 (algebraic); Z_t vs
  p111_d's W identity (rel. diff ≤ 0.02 at h = 0.1);
  B_b-from-torsion-vector vs R − t (rel. diff ≤ 0.05).
  A gate failure is reported as such BEFORE scan
  numbers and the scan proceeds only against a passing
  transcription.
(G2) PL2 regression (in scan): B2 γ=0 rows at
  α ∈ {5, 20} must reproduce P12-1's stored PL2 binding
  reads (β=1.1: partial/full 0.000/0.000, ratio_med
  −14.4; β=1.5: 0.000/0.000, −23.3) within ±0.01 /
  Δlog10 ≤ 0.3 — null contractions, so the documented
  ∝g sign deviation cannot enter.

## Health gates (registered)

Per row, on the binding set: (H1) effective-G sign:
G_eff := −F_u = φ_t + 2φ_b > 0 at every binding point
and finite (this is the coefficient of G_μν in
Eq. (42) — the f(T,B) generalisation of P12-1's
f_T > 0); φ_t min also reported. (H2) all partials of
f to third order finite at every binding point.
(H3) B-sector scalar ghost proxy (published
scalar-tensor representation, above): g_RR := φ_bb
(the (T,R)-frame R-sector second derivative; = F′(R)
for B3) — reported per row (min, fraction > 0);
scalar_pass := g_RR > 0 at every binding point for
B-active rows. health_pass := H1 ∧ H2 ∧ (H3 if the
row is B-active). c_T = 1 label carried (case 2).

## Scan grid (per β ∈ {0.1, 1.1, 1.5} DIRECT, full care
at superluminal β — no thinning)

B1a: γ ∈ {−20, −5, −1, −0.2, 0.2, 1, 5, 20} (8)
B1b: γ ∈ {−5, −1, −0.2, 0.2, 1, 5} (6)
B2:  α ∈ {−5, 5, 20} × γ ∈ {−5, −1, 0, 1, 5} (15)
B3:  κ ∈ {−20, −5, −1, 1, 5, 20} (6)
GR control (1). Total 36 rows/β, 108 rows.
Every row: binding partial/full/sign/ratio_med +
ratio-free cross-check; health (above); full-volume
all-directions NEC read at h ∈ {0.3, 0.15} (1274 pts,
9 ≤ r ≤ 21, r²-weighted violation fraction beyond
tol = 1.430e-4, worst NEC, Type-I fraction — P12-1
pattern). Every row with partial ≥ 0.50 additionally:
full-volume ALL-FOUR-EC read (Hawking–Ellis margins,
fallback-sampled NEC at non-Type-I points) and a
conservation residual (p121_audit pattern, sample =
every 21st binding point, step 0.15).

## Lorentz-floor read (registered)

For the best row per β (best := largest binding partial
among health-passing rows; if none health-passing, the
largest-partial row, labelled as such) AND the B3
control's best row per β: antisymmetric residual of
the full H on independent Sobol points in the wall
volume (never used in any fit — there is no fit; the
points are independent of the binding/volume sets),
h ∈ {0.3, 0.15}, rel_med of max|H_[ab]| / max|H_(ab)|
(coordinate components, P12-1 audit pattern — the
orthonormal transform symmetrises, so the read is
covariant). Floor: P19-3's 0.298 (β=1.1) / 0.330
(β=1.5). "B moves the floor" (registered): rel_med
improves ≥ 25% relative (≤ 0.2235 / ≤ 0.2475) at
either superluminal β at solution-grade health
(health-passing row). B3's read is reported as the
control (its antisymmetric part vanishes analytically
by Eq. (43) — a machinery check, not a floor move).

## Verdict bars (fixed, CHECKPOINT21 §P21-4)

ALIGNMENT iff some row at β=1.1 or 1.5 meets the
shared scan bars (full ≥ 0.90, health pass,
volume-clean) AND its antisymmetric residual ≤ 0.02.
KILL — TELEPARALLEL CLOSES iff no row at any β is
simultaneously health-passing, volume-clean and
partial ≥ 0.50, OR the B sector fails the registered
floor-move test at both superluminal β. INTERMEDIATE
otherwise, named clause. Anatomy per family either
way: what B can and cannot change, from the runs.

## POST-HOC NOTES (dated 2026-11-21, during the scan runs —
numerical conventions only, no bar/grid/tolerance changed)

(1) The ratio-free cross-check was first coded as P12-1's
count agreement (<= 1 binding point). It fired twice, both
times on rounding-boundary points only: first from a mixed
GR baseline (fixed by using the bed's stored That_GR_b for
the binding read throughout, as P12-1 does), then on the
B3 kappa=-20 row at beta=1.1, where 112 binding points have
H(k*,k*) ~= 0 and therefore sit at ratio = 1 +- 1e-16
automatically (any point with vanishing LHS null
contraction has ratio exactly 1, since That_GR(k*,k*) =
-D). The check now passes iff every disagreeing point lies
within 1e-9 of the boundary in ratio; disagreement counts
are stored per row. No verdict bar was changed.
(2) Health: a row's B sector counts as ACTIVE iff phi_b or
phi_bb is nonzero somewhere on the binding set (the first
coding marked B2 gamma=0 rows B-active, failing them on
the scalar proxy phi_bb > 0 although their B sector is
identically zero). B2 gamma=0 rows are the PL2 regression
rows and are gated as pure f(T) rows.
(3) Superpotential-term sign (found by the PL2 regression
gate, 2026-11-21): as first transcribed, the B2 gamma=0
rows reproduced P12-1's PL2 partial/full/sign EXACTLY but
ratio_med was off by a systematic factor 4.79 (beta=1.1) /
5.04 (beta=1.5) at both alpha in {5, 20} -- the W term's
sign against the programme's published-W tensor (BBW's S,
their Eq. 14, carries the opposite sign to p111_d's
flipped S once T_prog = -T_BBW). The sign is flipped in
p214_lib.H_cov; the B3 gate is blind to it (Z = 0 for
f(R)) and still passes at 1e-16, and the regression is
re-checked by p214_check.py on the re-run. The first
scan/audit run (wrong-sign Z) is superseded in full; no
number from it is used.
