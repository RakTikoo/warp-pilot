# P46-3 — Bulk completion past y*: memo

**Verdict (registered fixed form): COMPLETION EXISTS** — gain line
and C12 line stated separately in §6, as registered. This is not a
transport claim.

## 1. Posing

P43-1's cross-throat bulk gain (0.480 at z_a = 1) is a
cap-labelled infimum of the P29-3 Gaussian-normal lift of the
exhibited √-shape throat: the gain grows monotonically toward the
bulk curvature singularity at y* ≈ 0.4675 r₀ (D(0,y): 2.83 →
0.037; Kretschmann at the throat 713 → 1.09×10⁷ by y = 0.45) and
the infimum is **not attained** in that bulk. This item asked:
does a REGULAR completion of the bulk — past the pinch or around
it — attain a maximising geodesic, and at what price? Registered
routes R1 (mirror/Z₂ brane at y_c < y*), R2 (regular-core bulk
extension), R3 (different slicing/ansatz). Bars: gate first;
Kretschmann finite on the whole traversed domain; maximiser an
actual geodesic of the completed bulk with computed arrival
time; no added brane matter on the endpoint brane; EC-violating
bulk matter named as the completion's price (relocation);
C12 full and mandatory.

## 2. Gate (before any completion number) — PASS

Same code path as P43-1 (`phase43/p431_geodesic.minimise_time`)
on the P43-1 stored bulk fields (`p463_gate.py`,
`results/p463_gate.json`):

- Flat RS2: free minimisation returns the W3 zero **exactly**
  (rel. err 0.0); forced detours reproduce W3's analytic times
  to ≤ 1.4×10⁻¹⁴ (bar 1×10⁻¹⁰).
- Throat, z_a = 1, y ≤ 0.455: nseg-48 refine gain **0.4806**
  (record 0.480); ×10 subdivision of the refined path **0.4802**
  (record checker 0.4798). Gate passed; only then were
  completion numbers read.

## 3. Route R1 — mirror/Z₂ brane at y_c: COMPLETION EXISTS

**Construction.** Close the bulk at y_c < y* with a Z₂ mirror
brane (the standard RS move). The completed bulk is
y ∈ [0, y_c]; its bulk matter is unchanged (Λ₅ only — the
evolved P29-3 fields on the slab); nothing is added to the
endpoint brane. The domain is compact in y, so the optical
minimiser is attained, not an infimum.

**Attained gains** (nseg-48 minimisation, ×10-subdivided checker
times; brane time 6.2784 r₀/c at z_a = 1):

| y_c /r₀ | T_attained (subdiv.) | gain | u_eff | K bound along path | D(0,y_c) |
|---|---|---|---|---|---|
| 0.20 | 5.8581 | 0.067 | 1.072c | ≤ 9.64×10² | 1.738 |
| 0.25 | 5.5996 | 0.108 | 1.121c | ≤ 1.30×10³ | 1.473 |
| 0.30 | 5.2304 | **0.167** | 1.200c | ≤ 2.21×10³ | 1.197 |
| 0.35 | 4.7270 | 0.247 | 1.328c | ≤ 5.91×10³ | 0.901 |
| 0.40 | 4.0842 | 0.349 | 1.537c | ≤ 4.59×10⁴ | 0.580 |

(K bound: on the P43-1 track the slice-maximum of Kretschmann is
the throat value at every snapshot, so any path with y ≤ y_c has
K ≤ K_throat(y_c) — finite at every y_c < y*, vs the divergence
713 → 1.09×10⁷ → ∞ of the uncompleted bulk.)

**Is the minimiser a geodesic of the completed bulk?** The
minimiser rises to y_c and rides the mirror interface over
|z| ≲ 0.64 (it does not merely touch). This was attacked
directly (`p463_r1b_double.py`): free minimisation in the
**Z₂ double** (unfolded space, fields mirrored about y_c,
metric continuous and Lipschitz at the interface), in both
endpoint classes (crossing to the mirror copy of the brane;
return). The crossing class converges to the *same* time
(gain 0.16699 vs 0.16693 at y_c = 0.30; 0.34944 vs 0.34949 at
0.40 — agreement ≤ 6.5×10⁻⁵). The reason is geometric: in the
double, the optical scale D/A has a transverse **minimum** at
the interface from both sides (D decreases toward y_c in each
copy) — the interface is a valley of the optical metric, and
the minimiser is the valley-floor curve: a minimising geodesic
of the completed space in the metric-geometry sense, smooth on
each side of the interface. It is *not* a smooth transversal
crossing, and the memo does not call it one; the reopening
condition in the results JSON names exactly the proof that
would downgrade this clause.

**The completion's price — the mirror brane's own stress.**
Israel Z₂ jump at y_c from the stored fields' extrinsic
curvature k_a = ∂_y ln(scale_a) (method validated at y = 0
against the exhibited brane's analytic Israel data: rel. err
≤ 0.8%). The mirror brane is **tension-like**: over |z| ≤ 3,
σ ∈ [1.001, σ_peak] (σ_peak = 1.47 at y_c = 0.30, 3.34 at 0.40,
concentrated at the throat), p_z, p_θ ≈ −1 (the RS tension
λ = 1) with throat corrections. All four ECs, |z| ≤ 3, every
y_c row: **NEC passes** (min +0.0004…+0.0014 — saturated, i.e.
zero within the k-method's validation error; no violation
seen), **WEC passes** (σ ≥ 1.0005), **DEC passes** (min
+0.0004…+0.0014, saturated), **SEC fails at ≈ −2.00** — which
is exactly the positive-tension value
(σ + p_z + 2p_θ ≈ −2λ): the mirror brane has the same SEC
status as the RS brane tension that the whole construction
already stands on, and no NEC/WEC/DEC exoticity anywhere.
No bulk matter is added; no endpoint-brane matter is added.

**Headline row: y_c = 0.30** — gain **0.167** attained
(T = 5.2304 r₀/c vs brane 6.2784 r₀/c, u_eff = 1.200c),
K ≤ 2.21×10³ /r₀⁴ along the path, mirror price mildest.
Deeper mirrors (0.35, 0.40) attain more at higher K and higher
mirror σ_peak; they are reported, not headlined.

Note what is *not* claimed: the 0.480 of P43-1 is **not**
attained by any row here. It remains the infimum of the
uncompleted bulk at its singular boundary. The completion
buys attainment and regularity at the price of most of the
gain — the honest exchange the registration anticipated
("D no longer collapses to 0.037, so the gain must be
re-measured, not assumed").

## 4. Route R2 — regular-core extension: attained, but the
## exoticity is relocated into the bulk (named, per the bars)

**Construction** (`p463_bulk_r2r3.py`; dense re-evolution of
the lift, gate: D_throat(y=0) = 2.8284271247461903, exact;
fields at y_c = 0.30 match the P43-1 track to all digits).
Past y_c, ln A, ln D, ln C are blended in y by the cubic
Hermite matching value and k_a at y_c and reaching k_a = 0 at
y_c + L (L = 0.15), returning each field to its y_c value;
beyond, fields are y-constant (a regular core) to a Z₂ mirror
at y_m = 0.60. C¹ in y — no distributional shell. Bulk
stress-energy read from the 5D Einstein tensor (P29-3 sympy
jet machinery): κ₅²T^a_b = G^a_b + Λ₅. **Audit floor:** the
same read on the un-extended slab returns T ≈ 0
(NEC_min = −1.5×10⁻⁵; ρ ∈ [−3.5×10⁻¹², 1.8×10⁻³]) — vacuum +
Λ₅ only, as it must.

**Result.** Attained gain **0.195** (subdivided; path ymax
0.350, riding the blend's A-dip), Kretschmann finite
everywhere (max 8.64×10⁴ on the domain; ≤ 4.29×10⁴ along the
path). **But the bulk matter is the price, and it is
exotic:** in the transition layer, ρ_min = **−19.57**,
NEC_min = **−20.09**, SEC_min = −20.09, DEC_min = −34.67 —
NEC violated at 1.37×10⁶ × the audit floor; even the constant
core carries ρ ≈ +2.05…+2.12 with NEC_min = −0.250 and
SEC_min = −6.37. Per the registered bar, this completion
**relocates the exoticity into the bulk** and is verdicted as
such; it is not the headline. *Failure anatomy + follow-up
(Failure Protocol):* the violation is concentrated where the
blend forces dk_a/dy ~ k_a/L — the transition must absorb the
full y-variation of k (k_z ≈ −4.9 at y_c) over L; the follow-up
experiment is named: minimise the transition NEC over blend
profiles and L (the k-variation is fixed by matching, so an
integral lower bound on the violation is the expected
structural result — if proven, R2-class completions are
exoticity-relocating by identity, not by ansatz choice).

## 5. Route R3 — different ansatz: slicing impossible (proof
## clause); floored-D ansatz attempted, same relocation

*Slicing clause (proof-grade):* a different Gaussian-normal
slicing of the **same** bulk cannot regularise the pinch —
Kretschmann is a scalar invariant, slicing-independent, and it
diverges at the throat as y → y* on the grid-converged P29-3
record. Any R3 must change the bulk, not its slicing.
*Ansatz attempted:* D floored by construction,
D_R3 = √(D² + 0.60²), on the slab + the R2 core skeleton.
Attained gain **0.135**, K finite (≤ 3.49×10⁴ along the path),
but its bulk matter violates NEC already on the slab
(−0.278) and in the transition (−17.61; 1.20×10⁶ × floor),
core as R2. Same verdict as R2: a regular completion that
relocates exoticity into the bulk — named, not used.

**Route summary:** ≥ 2 routes attempted in full (R1, R2),
R3 attempted as an ansatz plus a proof that its slicing form
is impossible. The singularity is therefore **not**
load-bearing for attainment itself — R1 attains a regular
maximiser without it — but it *is* load-bearing for the
*size* of the P43-1 number: every regular completion caps
the attained gain at ≤ 0.349 (deepest mirror run), strictly
below the 0.480 singular-boundary infimum, and the cap is
monotone in the distance kept from y*.

## 6. Verdict lines (carried separately, as registered)

**Gain line — COMPLETION EXISTS (R1).** A regular completion
(Z₂ mirror brane at y_c = 0.30 r₀) attains the maximising
cross-throat geodesic with gain **0.167** (T = 5.2304 r₀/c vs
brane 6.2784 r₀/c; u_eff = 1.200c; subdivided and Z₂-double
checkers agree to 6×10⁻⁵), Kretschmann ≤ 2.21×10³ /r₀⁴ along
the whole path, no bulk matter, no added endpoint-brane
matter. Price: one pre-existing tension-like mirror brane
(NEC/WEC/DEC saturated-pass; SEC fails at the tension value
−2λ, as the RS tension itself does). Deeper mirrors attain
0.247 (y_c = 0.35) and 0.349 (y_c = 0.40). R2/R3 attain
0.195/0.135 only with strongly NEC-violating bulk matter —
relocation, named.

**C12 line — EFFECTIVE ONLY.** Formation leg stated, not
waived: Phase 28 — no classical route to a created handle
exists below the quantum level (Geroch's obstruction is
field-equation-free and binds this home); quantum nucleation
is Planck-scale only (area-law suppression, exponent
~1.2×10⁷⁰ already at r₀ = 1 m); growth UNCOMPUTED. The
throat, its bulk and the mirror brane are **pre-existing
structure in the initial data** — that assumption prices
every number above. At the exhibited row's
r₀ = 6.802266×10⁶ m: brane light time 0.14246 s vs attained
bulk arrival 0.11866 s — a local win of 0.0238 s that exists
only under pre-arrangement by ≤ c signals; the
decision-inclusive arrival is ≥ 0.14246 s. **No transport
claim.**

**Tolman clause.** A CTC would need v > 2u/(1+u²) **and** a
second independently moving home: at the headline
u_eff = 1.200c, v_crit = 0.9835c (at y_c = 0.40's 1.537c,
0.9143c). The completion is static in the home's frame and
creates no second moving home; no CTC is created or used —
reported as a finding of absence, per registration.

## 7. Files

Scripts: `p463_gate.py`, `p463_r1_mirror.py`,
`p463_r1b_double.py`, `p463_bulk_r2r3.py`, `p463_assemble.py`,
`p463_check.py`. Results: `p463_gate.json`, `p463_r1.json`,
`p463_r1b.json`, `p463_r2r3.json` (+ log), `p463_results.json`,
`p463_check.json` (**CHECK PASS**, all clauses, including
independent recomputation of every gain and the R1↔R1b
agreement). float64 throughout; all runs unattended scripts.
