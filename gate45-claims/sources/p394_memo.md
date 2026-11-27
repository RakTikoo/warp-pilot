# PHASE 394 MEMO — SCALING SEARCH SEEDED AT THE RAY POINT

VERDICT: STATIONARY LEVEL IMPROVES AGAIN —
GATE REFERRAL.

Phase 393's ray point was not a ridge. A 389-pattern
scaling search seeded there (349 stored SET-244
reads, every one feasible, none DEC-saturated)
climbed across the ray to a new centre at
(μ_S, μ_N, μ_M) = (0.8015689430763502,
1.3179449338854314, 3.574968377899082) on H2's
total profiles, with a confirmed stationary joint
level of −6.812653×10⁻⁵ (SET-244, band [10, 20]) —
+5.601066×10⁻⁵ over the seed, +1.075808×10⁻⁴ over
389's mixed centre, +1.260980×10⁻⁴ over L_stat(H2).
The level remains negative: no EC pass, no member.

Charge: ledger entry 1009. Registration:
work/p394_registration.md (SS0–SS7), filed before
any computation. Frame: VM (laptop not admitted,
fourteenth occurrence; §Controls).

## The new centre (confirmed)

Full re-read reproduces the stored screen minima
at diff 0.0. Joint = NEC −6.812653×10⁻⁵ @
r = 15.488; DEC −4.611098×10⁻⁶ @ r = 18.171
(NEC-bound by a wide margin — DEC is nearly
closed here); ρ_min +9.678145×10⁻⁵ (C1 holds).
Exact worst-null at the SET NEC argmin
−7.173153×10⁻⁵, beating the seed's
−1.247728×10⁻⁴ by +5.304123×10⁻⁵ — the
improvement survives at pointwise grade.
Polished depth −4.730182×10⁻⁶.

END-CLAMP RIDER, MEASURED INSIDE THE CHARGE
(Gate-41/43 construction; validated by
CTL-394-CLAMP at diff 0.0 on the H2 leg and
2.17×10⁻¹⁹ against Gate-43 at the mixed centre):
the new centre end-clamped reads −6.968823×10⁻⁵,
a clamp cost of only 1.562×10⁻⁶ — the gain is
carried by the scaling direction, not the
correction vectors' end knots. The clamped level
still beats the seed's unclamped level by
+5.445×10⁻⁵. The seed's own clamped level is
−1.247663×10⁻⁴ (cost 6.291×10⁻⁷).

## How the gain was found

THE RAY ALONE IS NOT THE STORY: along the pure
μ_M ray from the seed the level rises
monotonically to the registered edge
(−1.039017×10⁻⁴ at μ_M = 3.6) with decaying
increments — no turn inside the box — but that
accounts for only +2.02×10⁻⁵ of the +5.60×10⁻⁵.
At the seed the pure-axis slopes are small and
sign-mixed; the ascent is DIAGONAL (μ_S down,
μ_N up, μ_M up jointly), the same cooperative
texture 389 measured at H2. G1's corner
(0.85, 1.25, 3.5) read −8.136279×10⁻⁵; the
polish from the ray's edge point walked it to
the centre. A second, fresh polish from the
incumbent (150 evaluations) returned exactly its
start point — a local optimum of the searched
box at polish resolution.

BOX-EDGE DISCLOSURE: the centre presses the
registered μ_S lower edge (0.80157 vs the 0.80
edge, in a tight flat cluster). Whether the
level keeps rising below μ_S = 0.80 is
unmeasured; μ_N (1.318 / 1.35) and μ_M
(3.575 / 3.60) sit inside their edges. A box
extension is a named follow-up, not part of
this verdict.

RECONCILIATION: 389's concavity at H2 was a
local fit over μ ∈ [0.90, 1.10]³ and stands as
scoped. This centre is a different neighbourhood
of the same surface, past 393's dip along the
ray; the surface has at least two ascent regions
and the second is higher. Neither reading
revises the other.

## Controls

VM, all diff 0.0: (1, 1, 1) → L_stat(H2) (five
minima + depth); the mixed centre → 393's anchor
(five minima + depth); the seed → 393's stored
ray read (five minima) with its worst-null
reproduced exactly (−1.2477276305772507×10⁻⁴);
the clamp construction → 379's stored end-clamp
read, and 2.17×10⁻¹⁹ against Gate-43's clamped
mixed centre. Laptop admission attempted at the
seed on the pool mirror: SET minima differ at
2.7×10⁻⁷ (NEC) / 1.6×10⁻⁵ (WEC) / 4.2×10⁻⁶
(SEC), DEC and ρ at roundoff — NOT ADMITTED
(fourteenth occurrence); all numbers are VM
numbers.

INCIDENTS (disclosed in the checkpoint): the
first G4 polish invocation no-opped on a dropped
load_done() in this phase's driver — caught from
its own log line, fixed, rerun in full, no read
lost; consequently the two polishes executed in
swapped order (ray-start first, incumbent-start
second), the registered pattern intact in
substance.

## Fences

Band-posed [10, 20] SET-244 / SAMPLER-M levels,
356's full-extent caveats travelling (lineage
full-extent ≈ −1.44×10⁻³ over [10, 60] stands;
no full-extent read of the new centre is claimed
here). No EC pass, no member, no sustainment,
front or transport content. Sampled minima name
their frame convention (C-10); deciding values
are diff-0.0 reproductions and frame-invariant
worst-nulls. Three-goal accounting: Goal 1 — the
stationary pressure level improves again
(progression −1.942246×10⁻⁴ → −1.757074×10⁻⁴ →
−1.241372×10⁻⁴ → −6.812653×10⁻⁵); the wall moved,
it did not break. Goals 2 and 3 untouched.

DESK: NO DATA CONTACT — the programme's own
stored configurations re-read and re-scaled on
its own instruments; no external data of any
kind.

Files: work/p394_registration.md, work/p394_lib.py,
work/p394_controls.py, work/p394_admission.py,
work/p394_search.py, work/p394_confirm.py,
work/p394_clamp.py; results/p394_controls.json,
results/p394_controls_laptop.json,
results/p394_screens.jsonl (+ parts/),
results/p394_search_summary.json,
results/p394_anatomy.json,
results/p394_confirmation.json,
results/p394_clamp.json. Spend: ≈ 21 min VM wall.
