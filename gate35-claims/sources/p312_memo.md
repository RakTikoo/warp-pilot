# PHASE 312 MEMO — ONE-SIGN M′

## Verdict (FTL goal, leading)

**POSITIVE-DENSITY MEMBER.** Five of the 36 registered members
have depth past the material bar (−0.0034, SAMPLER-M
adversary-polished) AND ρ_req ≥ 0 at ALL four of their binding
sites (Phase 293 site rule):

| member | depth (SAMPLER-M polished) | min ρ_req over binding sites |
|---|---|---|
| ramp broad, m₀ = +0.5 | −1.278702×10⁻³ | +2.146340×10⁻⁵ (S4) |
| ramp broad, m₀ = +1.0 | −1.180275×10⁻³ | +6.498030×10⁻⁵ (S4) |
| ramp early, m₀ = +1.0 | −5.922334×10⁻⁴ | +1.665425×10⁻⁵ (S2) |
| edges E1, m₀ = +1.0 | −6.232242×10⁻⁴ | +1.665425×10⁻⁵ (S2) |
| edges E2, m₀ = +1.0 | −6.232242×10⁻⁴ | +1.665425×10⁻⁵ (S2) |

(E1 and E2 at m₀ = +1.0 are one physical read: the registered
E1/E2 identity audit returned max diff **0.0** over depth, SET
NEC min, Type-I count, and every site's point, ρ_req and both
NEC reads, at every m₀ — see §4.)

Scope fence, stated plainly: the verdict is the registered
one — ρ_req ≥ 0 at the four binding sites per member, the same
site rule Phase 308 was judged by. It is NOT pointwise
positivity over the shell: every winner's SET-244 ρ minimum is
still negative (edges m₀=+1.0: −6.714×10⁻⁵; ramp early +1.0:
−6.714×10⁻⁵; ramp broad +0.5: −4.099×10⁻⁵; ramp broad +1.0:
−7.561×10⁻⁸, i.e. negative only at the 10⁻⁷ level). The winners'
spinor joint match is the parent's charge and was NOT run here.

## 1. Registration summary

Pose, grids, controls, verdict forms and fences were fixed in
`phase312/work/p312_registration.md` before any computation.
Base pose: Gate-30 winner's (S, N) verbatim, spec
{'shape':'plat','a':2,'b':2,'A':0.07439108177516472,'c':15,
'W':5,'e':3.0}, β = 1.1, extended class of Phase 308
(γ_ij = δ_ij + (M−1) n_i n_j). Machinery: p308_lib copied to
p312_lib with ONLY the M-profile layer generalised (Einstein
assembly T_from_SNM verified byte-identical to p308_lib's;
worst_null likewise). Profiles built from the quintic
smoothstep SS(x) = 6x⁵−15x⁴+10x³ and
U(r;a,b) = SS((r−a)/(b−a)):

- **(a) ONE-SIGN RAMP:** M = 1 + m₀[U(r;r1,r2) − U(r;21,24)];
  m₀ ∈ {−0.5,−0.25,+0.1,+0.25,+0.5,+1.0} × windows broad
  (10.5,19.5), centred (12,18), early (10.5,14.5), late
  (15.5,19.5) = 24 members. On [10,20], M′ = m₀·U′ keeps one
  sign.
- **(b) EDGES-OUT:** M = 1 + m₀[U(r;a1,a2) − U(r;a3,a4)], both
  transitions outside [10,20] (E1: rise [8,10], fall [20,22];
  E2: rise [6,9], fall [21,24]); M ≡ 1+m₀, M′ ≡ 0 exactly on
  the band. Same six m₀ × {E1,E2} = 12 members.

Profile-layer unit checks (pre-run): analytic M′ and M″ agree
with centred finite differences of M and M′; edges profiles
return M = 1+m₀ exactly and M′ = M″ = 0 exactly at in-band
sample radii; a centred ramp's in-band M′ has a single sign.
Read protocol: SET-244 (41 radial nodes × 162 Fibonacci dirs,
SAMPLER-M) + adversary polish; depth := polished in-region
worst NEC, SAMPLER-M; binding sites S1–S4 by Phase 293's rule;
ρ_req := That[0,0]; per site both the SAMPLER-M NEC and the
exact pointwise NEC minimum (worst_null) recorded, each named;
per-site R/(16π) vs Q_K/(16π) split from the C3-audited
formula, R split further into its (1−1/M) piece R1 and its M′
piece R2. The split formula reproduces the tensor assembly's
ρ_req at every one of the 144 recorded binding sites to
≤ 1.52×10⁻¹⁸.

## 2. Controls (all before any verdict read)

- **C1 (M ≡ 1, phase312 protocol): PASS at diff 0.0.** Depth
  −0.001386956608122417 (diff 0.0), SET NEC min
  −0.004079744835667814 (diff 0.0), Type-I count 1245 exact,
  polish site r = 12.369476376022238 (diff 0.0), four site
  ρ_req diffs vs Phase 308's stored full-precision values all
  0.0 (vs the registration's 6-significant-figure roundings,
  ≤ 3.3×10⁻¹², as expected from the rounding).
- **C2 (Phase 308 near-miss via p308_lib as stored): PASS at
  diff 0.0.** m₀ = +0.25 bump member: all four per-site ρ_req
  diffs 0.0, depth diff 0.0 (stored −1.031034×10⁻³), min ρ_req
  diff 0.0 (stored −1.680665×10⁻⁴).
- **C3 (formula audit): PASS.** Split at the m₀ = +0.25
  member's four sites vs phase308/results/p308_anatomy.json:
  max |ΔR/(16π)| and |ΔQ_K/(16π)| = 4.07×10⁻¹⁹ (bar 1e-12). At
  M ≡ 1: R = 0 exactly at all four winner sites, and the split
  total matches Phase 295's factorisation value
  −β²S′²(1−n_x̂²)/(32πα²) to ≤ 5.15×10⁻¹⁹.

Full control records: `phase312/results/p312_controls.json`.

## 3. Full tables — both grids

Depth is SAMPLER-M adversary-polished throughout; bar
−0.0034. min ρ_req is over the member's four binding sites.

### (a) One-sign ramp

| member | depth | min ρ_req | past bar | all sites ρ≥0 |
|---|---|---|---|---|
| broad m₀=−0.50 | −3.411601×10⁻³ | −5.328460×10⁻⁴ | no | no |
| centred m₀=−0.50 | −2.867817×10⁻³ | −3.706260×10⁻⁴ | yes | no |
| early m₀=−0.50 | −2.908943×10⁻³ | −1.857848×10⁻³ | yes | no |
| late m₀=−0.50 | −3.357663×10⁻³ | −1.267043×10⁻³ | yes | no |
| broad m₀=−0.25 | −1.767112×10⁻³ | −2.459997×10⁻⁴ | yes | no |
| centred m₀=−0.25 | −1.852242×10⁻³ | −1.808979×10⁻⁴ | yes | no |
| early m₀=−0.25 | −1.861366×10⁻³ | −6.429656×10⁻⁴ | yes | no |
| late m₀=−0.25 | −2.210175×10⁻³ | −4.573556×10⁻⁴ | yes | no |
| broad m₀=+0.10 | −1.364455×10⁻³ | −5.918381×10⁻⁵ | yes | no |
| centred m₀=+0.10 | −1.384256×10⁻³ | −7.102218×10⁻⁵ | yes | no |
| early m₀=+0.10 | −1.260624×10⁻³ | −7.435902×10⁻⁵ | yes | no |
| late m₀=+0.10 | −1.386957×10⁻³ | −8.753311×10⁻⁵ | yes | no |
| broad m₀=+0.25 | −1.331517×10⁻³ | −2.028230×10⁻⁵ | yes | no |
| centred m₀=+0.25 | −1.380272×10⁻³ | −4.491022×10⁻⁵ | yes | no |
| early m₀=+0.25 | −1.095327×10⁻³ | −5.012687×10⁻⁵ | yes | no |
| late m₀=+0.25 | −1.386957×10⁻³ | −8.753311×10⁻⁵ | yes | no |
| **broad m₀=+0.50** | **−1.278702×10⁻³** | **+2.146340×10⁻⁵** | **yes** | **YES** |
| centred m₀=+0.50 | −1.373808×10⁻³ | −3.008766×10⁻⁵ | yes | no |
| early m₀=+0.50 | −8.696803×10⁻⁴ | −2.050442×10⁻⁵ | yes | no |
| late m₀=+0.50 | −1.386957×10⁻³ | −8.753311×10⁻⁵ | yes | no |
| **broad m₀=+1.00** | **−1.180275×10⁻³** | **+6.498030×10⁻⁵** | **yes** | **YES** |
| centred m₀=+1.00 | −1.361515×10⁻³ | −2.447042×10⁻⁵ | yes | no |
| **early m₀=+1.00** | **−5.922334×10⁻⁴** | **+1.665425×10⁻⁵** | **yes** | **YES** |
| late m₀=+1.00 | −1.386957×10⁻³ | −8.753311×10⁻⁵ | yes | no |

### (b) Edges-out (E1 and E2 reads identical — §4)

| member | depth | min ρ_req | past bar | all sites ρ≥0 |
|---|---|---|---|---|
| E1/E2 m₀=−0.50 | −2.914070×10⁻³ | −4.182513×10⁻⁴ | yes | no |
| E1/E2 m₀=−0.25 | −1.896010×10⁻³ | −1.976521×10⁻⁴ | yes | no |
| E1/E2 m₀=+0.10 | −1.248117×10⁻³ | −7.435902×10⁻⁵ | yes | no |
| E1/E2 m₀=+0.25 | −1.081503×10⁻³ | −4.937434×10⁻⁵ | yes | no |
| E1/E2 m₀=+0.50 | −8.778467×10⁻⁴ | −2.050442×10⁻⁵ | yes | no |
| **E1/E2 m₀=+1.00** | **−6.232242×10⁻⁴** | **+1.665425×10⁻⁵** | **yes** | **YES** |

Trade curve: the table pairs (depth, min ρ_req) over all 36
members ARE the depth-vs-min-ρ_req trade curve (also in
machine form in p312_results.json). Its shape: depth improves
monotonically with m₀ in both families; min ρ_req crosses zero
only for m₀ > 0, and only where the rise actually covers the
binding sites (broad at m₀ ≥ +0.5; early and edges at
m₀ = +1.0). The late window never moves min ρ_req off the
winner's own −8.753311×10⁻⁵ at any positive m₀ (see §5).

### Winners in full (per-site reads; NEC-M = SAMPLER-M NEC,
NEC-X = exact pointwise NEC minimum; split pieces /(16π))

**ramp broad m₀=+0.5** — depth −1.278702×10⁻³, Type-I count 1271
| site | r | Type-I | NEC-M | NEC-X | ρ_req | R1 | R2 | Q_K |
|---|---|---|---|---|---|---|---|---|
| S1 | 12.346 | yes | −1.278702×10⁻³ | −3.907007×10⁻³ | +9.136388×10⁻⁵ | +7.843×10⁻⁶ | +1.344×10⁻⁴ | −5.085×10⁻⁵ |
| S2 | 12.805 | no | −3.424400×10⁻³ | −3.424943×10⁻³ | +1.000049×10⁻⁴ | +1.266×10⁻⁵ | +1.689×10⁻⁴ | −8.152×10⁻⁵ |
| S3 | 12.317 | yes | −1.276271×10⁻³ | −3.900064×10⁻³ | +9.035907×10⁻⁵ | +7.563×10⁻⁶ | +1.318×10⁻⁴ | −4.905×10⁻⁵ |
| S4 | 17.683 | no | −2.433336×10⁻³ | −2.449071×10⁻³ | +2.146340×10⁻⁵ | +4.070×10⁻⁵ | +4.504×10⁻⁵ | −6.428×10⁻⁵ |

**ramp broad m₀=+1.0** — depth −1.180275×10⁻³, Type-I count 1336
| site | r | Type-I | NEC-M | NEC-X | ρ_req | R1 | R2 | Q_K |
|---|---|---|---|---|---|---|---|---|
| S1 | 12.324 | yes | −1.180275×10⁻³ | −3.516338×10⁻³ | +2.168496×10⁻⁴ | +1.482×10⁻⁵ | +2.501×10⁻⁴ | −4.806×10⁻⁵ |
| S2 | 11.829 | no | −3.126870×10⁻³ | −3.150424×10⁻³ | +1.521832×10⁻⁴ | +7.071×10⁻⁶ | +1.689×10⁻⁴ | −2.383×10⁻⁵ |
| S3 | 12.317 | yes | −1.180145×10⁻³ | −3.517020×10⁻³ | +2.161432×10⁻⁴ | +1.470×10⁻⁵ | +2.491×10⁻⁴ | −4.767×10⁻⁵ |
| S4 | 17.683 | no | −1.827601×10⁻³ | −1.830999×10⁻³ | +6.498030×10⁻⁵ | +6.168×10⁻⁵ | +5.171×10⁻⁵ | −4.841×10⁻⁵ |

**ramp early m₀=+1.0** — depth −5.922334×10⁻⁴, Type-I count 1400
| site | r | Type-I | NEC-M | NEC-X | ρ_req | R1 | R2 | Q_K |
|---|---|---|---|---|---|---|---|---|
| S1 | 12.308 | yes | −5.922334×10⁻⁴ | −1.282559×10⁻³ | +7.885957×10⁻⁴ | +7.646×10⁻⁵ | +7.475×10⁻⁴ | −3.540×10⁻⁵ |
| S2 | 17.683 | no | −1.758593×10⁻³ | −1.764499×10⁻³ | +1.665425×10⁻⁵ | +6.362×10⁻⁵ | 0 | −4.697×10⁻⁵ |
| S3 | 12.317 | yes | −5.921128×10⁻⁴ | −1.281350×10⁻³ | +7.851480×10⁻⁴ | +7.688×10⁻⁵ | +7.440×10⁻⁴ | −3.570×10⁻⁵ |
| S4 | 17.683 | no | −1.757077×10⁻³ | −1.757561×10⁻³ | +1.769701×10⁻⁵ | +6.362×10⁻⁵ | 0 | −4.593×10⁻⁵ |

**edges E1 m₀=+1.0** (= E2, identical) — depth −6.232242×10⁻⁴,
Type-I count 1556; M ≡ 2, M′ ≡ 0 at every site, so R2 = 0 and
R is the pure (1−1/M) piece R1.
| site | r | Type-I | NEC-M | NEC-X | ρ_req | R1 | R2 | Q_K |
|---|---|---|---|---|---|---|---|---|
| S1 | 12.371 | yes | −6.232242×10⁻⁴ | −1.810600×10⁻³ | +1.029634×10⁻⁴ | +1.300×10⁻⁴ | 0 | −2.703×10⁻⁵ |
| S2 | 17.683 | no | −1.758593×10⁻³ | −1.764499×10⁻³ | +1.665425×10⁻⁵ | +6.362×10⁻⁵ | 0 | −4.697×10⁻⁵ |
| S3 | 12.317 | yes | −6.188672×10⁻⁴ | −1.788275×10⁻³ | +1.058829×10⁻⁴ | +1.311×10⁻⁴ | 0 | −2.525×10⁻⁵ |
| S4 | 17.683 | no | −1.757077×10⁻³ | −1.757561×10⁻³ | +1.769701×10⁻⁵ | +6.362×10⁻⁵ | 0 | −4.593×10⁻⁵ |

In every winner, at every binding site, R (positive) exceeds
|Q_K| (negative): the density is R-carried, exactly the
mechanism Phase 308's near-miss showed at S1/S3 but could not
hold at S4.

## 4. E1/E2 identity audit (registered prediction)

CONFIRMED EXACTLY. For all six m₀, E1 vs E2: depth diff 0.0,
SET NEC min diff 0.0, Type-I count diff 0, and per-site point,
ρ_req, SAMPLER-M NEC and exact pointwise NEC diffs all 0.0.
Max audit diff = **0.0**. No machinery defect. (The reads live
only on [10,20], where both extents give M ≡ 1+m₀, M′ ≡ 0.)

## 5. Site-migration anatomy

**Class (a), negative m₀ — one sign, wrong sign.** With
m₀ < 0, M′ < 0 at every selectable radius, so the whole band
is a falling edge. The binding sites migrate OUT: at
m₀ = −0.5 all four sites sit at r ≈ 17.7–18.2 in every window
(the winner's inner cluster at r ≈ 12.3–12.8 disappears from
the site list), and the worst site is decided by the M′ piece
R2 in 5 of the 8 negative-m₀ ramp members (e.g. early −0.5:
S2 at r = 13.29 — inside the steep early fall, M′ = −0.167 —
R2/(16π) = −1.468×10⁻³, ρ_req = −1.858×10⁻³; late −0.5: S4 at
r = 18.17, R2 = −1.107×10⁻³). Q_K decides the other three.
One-signed M′ with the negative sign is uniformly worse than
either Phase 308 edge: it makes the poisoning global.

**Class (a), positive m₀ — the falling edge is fixed; Q_K is
what replaces it.** At S4 (r = 17.68), Phase 308's m₀ = +0.25
bump had R/(16π) = −9.12×10⁻⁵ (M′ < 0 there) and
ρ_req = −1.68×10⁻⁴. Under the broad ramp at the same m₀,
S4's R pieces are both positive (R1 = +2.42×10⁻⁵,
R2 = +3.19×10⁻⁵) and ρ_req improves to −2.03×10⁻⁵ — the
falling-edge poisoning is gone. What remains, at EVERY
surviving positive-ramp failure, is Q_K as the most negative
term at the worst site (the negated-square remnant, reduced
but not removed by its M-dependent terms): broad +0.25 S4
Q_K = −7.64×10⁻⁵ vs R = +5.61×10⁻⁵; centred +0.5 worst site
S3 (r = 12.32) sits where the centred rise has barely begun
(M = 1.001, M′ = +0.006), so R ≈ +2.04×10⁻⁵ cannot cover
Q_K = −5.05×10⁻⁵; centred +1.0's worst site migrates to
r = 11.83, BEFORE the rise starts (M = 1 exactly), where
ρ_req = −2.45×10⁻⁵ is the untouched Phase 295 negated square.
The broad window wins because its rise covers all binding
radii: at S4, R grows from +5.61×10⁻⁵ (m₀=+0.25) through
+8.57×10⁻⁵ (+0.5) to +1.13×10⁻⁴ (+1.0) while |Q_K| shrinks
(7.64 → 6.43 → 4.84 ×10⁻⁵), crossing between +0.25 and +0.5.
The early window wins at +1.0 by a different route: its steep
rise (M′ up to +0.46 at the inner sites) makes R2 enormous
there (+7.48×10⁻⁴ at S1), and its sites beyond r = 14.5 sit
on the finished plateau (M = 2, M′ = 0) and read exactly like
edges-out. The late window NEVER engages: at every positive
m₀ its S1/S2/S3 sit at r ≤ 12.8 where M ≡ 1, so its depth and
min ρ_req are the winner's own values verbatim
(−1.386957×10⁻³, −8.753311×10⁻⁵, decided by Q_K at S2 with
R = 0) — a ramp that starts after the binding sites cannot
rescue them.

**Class (b) — how close the pure (1−1/M) term comes.** It
comes all the way at the top of the grid. With M′ ≡ 0, R is
R1 alone, sign(m₀), radius-dependent only through 1/r². At the
persistent worst site (r = 17.68, S4 for m₀ ≤ +0.5, S2 at
+1.0): R1/(16π) = +1.16×10⁻⁵ (m₀=+0.1), +2.55×10⁻⁵ (+0.25),
+4.24×10⁻⁵ (+0.5), +6.36×10⁻⁵ (+1.0), against
Q_K/(16π) = −8.59, −7.48, −6.29, −4.70 ×10⁻⁵ — the gap closes
monotonically from both sides (R1 grows, |Q_K| shrinks as
M grows) and crosses between m₀ = +0.5 (net −2.05×10⁻⁵) and
m₀ = +1.0 (net +1.67×10⁻⁵ at the worst site; +1.03×10⁻⁴ and
+1.06×10⁻⁴ at the inner sites S1/S3, where 1/r² is larger).
At negative m₀ the same term turns against the member:
m₀ = −0.5's worst site (S2, r = 12.80) is decided by R1
(−2.43×10⁻⁴) ahead of Q_K (−1.76×10⁻⁴), ρ_req = −4.18×10⁻⁴.
Edges-out site radii do not migrate at all with m₀
(S1 12.37, S2 12.80, S3 12.32, S4 17.68 throughout, except S2
and S4 swapping the worst-site label at m₀ = +1.0): with no
in-band M′ structure there is nothing to migrate toward —
only the plateau height moves.

**Decider census (worst binding site, 36 members):** Q_K is
the most negative term at 29 worst sites (including every
positive-m₀ failure and every winner's tightest site), R2
(the M′ piece) at 5 (all negative-m₀ ramps), R1 (the (1−1/M)
piece) at 2 (edges-out at m₀ = −0.5, E1 and E2). Phase 308's decider — a sign-flipped M′
piece on a falling edge inside the band — decides NOTHING at
positive m₀ in either class: there is no falling edge in the
band.

## 6. Fences

Verdicts bind ONLY the two registered profile classes at the
winner's base pose (β = 1.1, (S,N) verbatim), 36 members, no
other dial moved. The positive verdict is a binding-site
verdict under Phase 293's site rule — the registered form —
not a claim of pointwise ρ ≥ 0 over the shell (SET ρ minima
remain negative for all winners; §0) and not a joint
spinor-matched construction (the parent's charge). SET reads
are set reads; polished sites are adversary-polished local
worsts, not certified global minima. Depth is SAMPLER-M
adversary-polished on every quotation; site NEC is quoted
under both SAMPLER-M and the exact pointwise read, each
named. No statement is made about other M profiles, other
base poses, angular/time dependence, or further extensions.

## 7. Three-goals accounting

- **FTL drive:** POSITIVE-DENSITY MEMBER at registered scope —
  five members (four distinct reads; E1/E2 coincide) past the
  depth bar with ρ_req ≥ 0 at all binding sites, R-carried.
  This answers Phase 308's open mechanism question in the
  affirmative: the edge-sign failure was a property of the
  bump profile, not of the extended class. The members are
  NOT a drive: depth (NEC) remains negative at the polished
  site, no spinor match was run, and no joint pass is claimed.
- **Wormhole:** no read touches the wormhole-throat standings;
  nothing in this phase re-judges them. Standings untouched.
- **Subluminal shell record:** no read touches it; Procaccia's
  0.1363 and the pilot's verified 0.10 stand as before.
  Standings untouched.

**DESK: NO DATA CONTACT** — an algebra and configuration-space
phase; no real-world dataset bears on it and none was
manufactured.

## 8. Artefacts

- Registration: `phase312/work/p312_registration.md`
- Library: `phase312/work/p312_lib.py` (p308_lib copy, profile
  layer generalised, split function appended)
- Run script + log: `phase312/work/p312_run.py`,
  `phase312/work/p312_run.log` (one VM restart interrupted the
  first launch during C2; the resumed run's controls and
  members are checkpointed in the results files and the final
  run completed all 36 members, total wall 1508 s)
- Controls: `phase312/results/p312_controls.json`
- All member records + splits + audit:
  `phase312/results/p312_results.json`
- Checkpoint: `phase312/CHECKPOINT312.md`

No ledger append, no launches, no external contact.
