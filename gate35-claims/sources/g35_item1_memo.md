# GATE-35 ITEM 1 MEMO — SET READ → CONTINUUM ADVERSARY SEARCH

Member: M(r) = 1 + 4.00·[U(r; 9, 20.5) − U(r; 21, 24)] (quintic
smoothstep U), Gate-30 winner (S, N) verbatim (plat, a=2, b=2,
A=0.07439108177516472, c=15, W=5, e=3.0), β=1.1, closed shell
r ∈ [10, 20], all directions. float64.

## Route for (S, N)

Clean separation was possible, no PCHIP extraction needed:
S, S′ from `p258_lib.S_ab(r, 2, 2)`; N = 1 + A·`shape_B_plat`
from `p274_lib` (c=15, W=5, e=3.0). These are profile FUNCTIONS
only; the ρ evaluator (`g35_rho.py`) is implemented fresh from
the Phase 308 split and imports nothing from p312/p314/p308.
M, M′, M′′ are analytic from the smoothstep (validated against
the stored site M, M′ values, e.g. S1: M=1.5909376185915285,
M′=0.4389959408070712 reproduced).

## Control C-G1 — PASS

- S1–S4 splits (R1, R2, Q_K, ρ_req at stored r, n_x̂): max
  relative diff **1.79×10⁻¹⁵** (bar 1×10⁻⁹). Per-site ρ rel
  diffs: S1 3.5×10⁻¹⁶, S2 1.6×10⁻¹⁶, S3 1.7×10⁻¹⁶, S4 6.9×10⁻¹⁶.
- Stored SET-244 ρ minimum +8.272455×10⁻⁵ at the memo §3 locus
  (r = 19.878049 = outermost midpoint node, n_x̂ = +0.0041):
  evaluator gives 8.272455163×10⁻⁵ at that locus (rel diff
  1.1×10⁻¹², consistent with the memo's 4-digit n_x̂), and
  ρ*(node) = 8.272455162×10⁻⁵ (rel diff 9.3×10⁻¹¹).

## Structural reduction (b) — VERIFIED

ρ depends on direction only through u = n_x̂²: R1, R2 are
functions of (r, M, M′) only; the Q_K numerator carries (1−u)
in term 1 and u in terms 2–4 and nothing else directional;
α² is affine in u and nothing else directional. Numerically at
50 random (r, direction) samples: the Q_K numerator and α² are
affine in u to max relative deviation 2.5×10⁻¹⁶, and ρ(u) was
monotonic in u in 50/50 samples — as it must be, since ρ(u) at
fixed r is a ratio of affine functions of u. Hence
ρ*(r) = min_u ρ(r, u) is the EXACT angular minimum (attained at
a u endpoint), and the continuum problem is the 1-D radial one.
The search nevertheless ran the registered 2001-point u-scan
at every radius, with golden polish inside ρ*.

## Search (c) — NO NEGATIVE LOCUS

Mesh Δr = 0.01 (1001 radii) + rim mesh Δr = 0.001 on
[19.5, 20] (501 radii); every mesh local minimum polished
with bounded `minimize_scalar` (there were NO interior mesh
local minima — ρ* decreases monotonically from r=10 to r=20);
registered seeds polished/evaluated directly: r=10 and r=20
exactly, S′ extremum r=15.0 (at u=0: ρ=2.013728×10⁻⁴), M′′
sign-change r=14.75 (ρ*=2.252896×10⁻⁴), rim window [19.99, 20].

**Global minimum: ρ* = +8.100317×10⁻⁵ at r = 20.000000 (closed
outer boundary), u = 0** (at r=20, S=S′=0 exactly, so ρ is
direction-independent there). Split there:
R1/(16π) = +7.9565×10⁻⁵, R2/(16π) = +1.4379×10⁻⁶,
Q_K/(16π) = 0. The continuum minimum sits BELOW the SET-244
minimum (+8.272455×10⁻⁵ at r=19.878) and is R1-carried against
a vanished Q_K — the memo §3 rim mechanism, pushed to the
boundary itself. No polished or mesh point has ρ < 0.

## Margin floors (d) — as computed

Per region: |dρ/dr| at the minimising u by central FD
(h=1e-5) on the mesh, regional max, safety factor 2;
floor₁ = 2·max|dρ*/dr|·(Δr/2), Δr/2 = 0.005. Second-order
floor₂ = 2·max|d²ρ*/dr²|_mesh·(Δr/2)²/2 reported alongside;
no regional minimum is an interior polished stationary point
(all three sit on region boundaries), so floor₁ is the
certifying floor in every region.

| region | found min | at r | max\|dρ/dr\| | floor₁ | certified bound₁ | floor₂ | bound₂ |
|---|---|---|---|---|---|---|---|
| inner [10, 12.5] | +2.590271×10⁻⁴ | 10.000 | 4.257×10⁻⁴ | 4.257×10⁻⁶ | **+2.547705×10⁻⁴** | 9.674×10⁻⁹ | +2.590175×10⁻⁴ |
| mid [12.5, 17.5] | +1.187206×10⁻⁴ | 17.500 | 1.944×10⁻⁴ | 1.944×10⁻⁶ | **+1.167761×10⁻⁴** | 2.112×10⁻⁹ | +1.187184×10⁻⁴ |
| rim [17.5, 20] | +8.100317×10⁻⁵ | 20.000 | 1.839×10⁻⁵ | 1.839×10⁻⁷ | **+8.081922×10⁻⁵** | 2.743×10⁻¹⁰ | +8.100289×10⁻⁵ |

The floors (≤ 4.3×10⁻⁶) are at or below the depth class of
the Phase 312 sibling pockets (10⁻⁷–10⁻⁵): a dip of that
class deeper than the regional floor could not have hidden
between mesh nodes, and every regional found minimum exceeds
its floor by a factor of 60 (inner), 61 (mid) and 440 (rim).

## Verdict input (coordinator assigns the registered verdict)

- No negative locus anywhere in the posed volume: **no
  POCKET FOUND input**.
- Certified continuum lower bound > 0 in all three regions
  (smallest: rim, +8.081922×10⁻⁵) — the facts match the
  CONTINUUM-CLEAN AT ADVERSARY GRADE form, with floors as
  tabled above.

Artefacts: `g35_rho.py` (evaluator), `g35_item1.py` (driver),
`g35_item1_results.json` (control diffs, polished list,
floors, global minimum + split). No ledger append, no
launches, no external contact.
