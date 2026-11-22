# P21-1 — BRANEWORLD (Shiromizu–Maeda–Sasaki): the Weyl-relocation test

**Verdict: PARTIAL** — open clause named exactly below (audit (iv),
bulk realisation). Not VERIFIED RELOCATION (no case passes
(i)+(ii)+(iv) together), not REFUTED (one throat case has
EC-legal brane matter passing (i) and (ii) at tolerance, and the
Π-carries clause never triggers anywhere).

Scripts: `../p211_throat.py`, `../p211_wall.py`, `../p211_claim.py`.
Numbers: `p211_results.json` (combined), `p211_throat.json`,
`p211_wall.json`, `p211_claim.json`. Conventions: SMS published
form as registered, Λ₄=0, κ₄²=8π, κ₅⁴=6κ₄²/λ, λ∈{1,100},
r₀=1, float64, SymPy-exact Einstein tensors (generic b(r), Φ(r)
derived once from the metric, then specialised).

## (a) THROAT

Geometry (SymPy): Ellis b=r₀²/r, Φ=0: G^μ_ν throat =
(+1, −1, +1, +1)/r₀², R=−2/r₀⁴. √-shape b=r₀(r/r₀)^{1/2}, Φ=0:
G throat = (−1/2, −1, +1/4, +1/4)/r₀², R=+1/r₀⁴.

Brane matter prescribed BEFORE proceeding, all four ECs verified
on r∈[r₀,10³r₀] per family (min margins in the JSON):
- **dust** (ρ solved from the trace condition, p_r=p_t=0):
  minus branch — Ellis: ρ<0, EC-illegal; √-shape: ρ≥0 everywhere
  (throat ρ=0.0415, tail min ≈1.3e-9), **EC-legal**.
  plus branch — ρ→λ at infinity (throat ρ=1.074 Ellis / 0.959 √),
  EC-legal but non-decaying matter.
- **radiation** p=ρ/3 (trace-solved ρ=√(3·trG/κ₅⁴)): EC-legal on
  Ellis (ρ_throat=0.1995); **no real solution on either √-shape**
  (trG<0 on 100% of the domain).
- **cons-aniso** (ρ=1/(κ₄²r), p_r=ρ/2, p_t from conservation):
  EC-legal for Φ=0 shapes.
- **trace-aniso** (same ρ, p_r; p_t root of the trace equation):
  EC-legal on √-shapes, illegal on Ellis.

Required E (U,P₁,P₂) solved from the three SMS equations; audits:

**(i) Tracelessness.** Vacuum (τ=0): fails at O(1) — relative
trace 2.00 (Ellis Φ=0), 1.00 (√ Φ=0), 3.86 / 1.63 (Φ=−r₀/r).
Trace-solved families: passes to roundoff (4.7e-16 dust-plus,
radiation; 3.6e-8 dust-minus √ — algebraic solve, cancellation
at the tail). Conservation-built family (cons-aniso): fails at
O(1) (0.95–1.46). **Anatomy: (i) and (ii) are competing
constraints on τ — each is easy alone, they are not independent.**

**(ii) Divergence identity** ∇^μE_μν = κ₅⁴∇^μΠ_μν, residual
relative to the |E|/r scale (residual ≡ κ₄²∇^μτ_μν exactly, by
Bianchi; cross-checked in-run). Vacuum: ~1e-5 (Bianchi noise
floor — passes trivially). Dust Φ=0: passes (median 7.8e-6,
max 1.6e-5, √-minus case) because static dust in Φ=0 is
identically conserved. Dust Φ=−r₀/r: 2e-3–4.4e-2 median,
max ~0.5 — the Φ′ρ term. Radiation: **0.63–0.67, O(1) fail**
(isotropic p(r) with p′≠0 is not conserved). Cons-aniso: ~1e-8
by construction. Trace-aniso: 8e-3–5.6e-2 median.

**(iii) E's own effective ECs (report only).** The E-sector
effective tensor (−E/κ₄²) violates NEC1 in every case computed
(e.g. −0.063 √-dust-minus, −0.40 Ellis radiation, −2.3 Ellis
dust-plus, at the throat scale): the NEC violation the throat
needs (total NEC1 at throat = −0.0199 √ / −0.0796 Ellis, in
κ₄²=8π units) sits in the E sector, as the mechanism intends.
Π's own NEC1 at the throat is small and positive in the dust
cases (+2.9e-4 √-minus, +0.19 dust-plus vs total −0.0796):
**Π does not carry the violation** — the REFUTED Π-clause does
not trigger.

**(iv) Bulk consistency.** (α) Tidal profile, derived in-script
from the tidal metric itself (M=0, Q=1): E_tidal^μ_ν·r⁴ =
(−1, −1, +1), trace 2.7e-17 — i.e. (𝒰,P₁,P₂) ∝ (1, −1, +1)/r⁴.
**No throat case matches it** (best constancy deviation 0.0094
for Ellis dust-minus, whose ECs fail; the EC-legal √-dust-minus
E has throat ratios (𝒰,P₁,P₂) = (0.565, 1.022, −0.228), P₁/𝒰 =
+1.8 vs the tidal −1, and an r^{−5/2}-led profile, not r^{−4}).
The only geometry whose E *is* the tidal profile is the tidal
metric itself — same b=r₀²/r shape but Φ=½ln(1−r₀²/r²), which
has f=0 at r=r₀: a horizon, not a traversable throat.
(β) Forced-vs-free, stated exactly: spherical E has 3 component
functions; tracelessness removes 1, the single nontrivial
(radial) divergence equation removes 1 more — **exactly one
free function of bulk data remains (e.g. 𝒰(r)); the other two
components are forced.** Dually, our solve forces all of E from
(b, Φ, τ) and the two constraints land on τ (3 functions, 2
constraints, 1 free) — the same single function seen from the
brane side. The √/Φ=0/dust-minus case is a consistent point of
this underdetermined system; what is missing is any bulk that
projects to it.

**Throat bottom line:** the relocation is *algebraically and
differentially consistent on the brane* in exactly the cases
where τ is built to satisfy both constraints (dust, Φ=0), and
inconsistent at O(1) for generic prescriptions (vacuum,
radiation, Φ≠0 dust). Clause (iv) binds in every surviving
case.

## (b) WALL — β ∈ {0.1, 1.1, 1.5} DIRECT (amended set)

Bed validated in-run: (251 pts, 1.981e-4), (504, 2.825e-3),
(594, 3.387e-3) — all match the registered binding sets.

- **W0 (τ=0, E_req=−G):** supply ratio E_req(k,k)/(κ₄²D) = 1.000
  at every binding point at every β (by construction), (ii)
  holds trivially (div Π=0, Bianchi), but **(i) fails at O(1)**:
  median relative trace 0.96 (β=0.1), 1.86 (β=1.1), 1.76
  (β=1.5); volume-point medians 0.93 / 1.38 / 1.50. A pure-Weyl
  wall is not a Weyl tensor.
- **W1 (trace-fixing dust, per point):** a legal ρ≥0 root exists
  at **100% of binding points and 100% of volume points
  (r²-weighted 1.0) at all three β**; E then traceless to
  roundoff, supply ratio ≥1 at 100% of binding points (min
  1.36 / 1.00 / 1.00; median 1.62 / 1.78 / 1.83) — the shared
  scan bars (full ≥0.90, partial ≥0.50) are met *pointwise* at
  every β. Π(k,k) is never negative and contributes a median
  0.01% / 0.13% / 0.17% of the deficit — Π does not carry it.
  **But (ii) fails by orders of magnitude:** the trace condition
  slaves ρ(x) to trG(x), so ρ varies on the wall scale and
  |κ₄²∇τ| / |κ₅⁴∇Π| ~ λ/(6ρ) = median **1946 (β=0.1), 99
  (β=1.1), 75 (β=1.5)**. The dust that fixes the trace cannot
  be conserved; the identity residual is 2–3 orders above the
  RHS scale. (This is a scaling read of the identity, stated
  as such; the pointwise algebra is exact.)

### Rung-2a (FTL) paragraph

The superluminal rows were run directly, as amended. At
β=1.1 (504 binding pts, max deficit 2.825e-3) and β=1.5
(594 pts, 3.387e-3) the pattern is identical to β=0.1 and, if
anything, cleaner pointwise: trace-fixing legal dust roots at
100% of binding points, E supply ratio ≥1 at 100% (full
coverage under the shared bars), Π negligible and
right-signed. What kills the superluminal rows is the same
clause as at β=0.1, only slightly softened: the divergence
identity residual scale λ/(6ρ) is a median 99× (β=1.1) and
75× (β=1.5) the Π-divergence RHS, because the required ρ is
slaved to the wall's own trG and cannot be a conserved dust
field; and with τ=0 the required E fails tracelessness at
relative 1.86 / 1.76. No bulk closure (tidal or otherwise) is
named by any row. So: at β>1 the braneworld supply problem is
*pointwise solvable and differentially inconsistent* — the
wall's Weyl tensor would have to be bulk data nobody has
exhibited, at exactly the same open clause as the throat.
Nothing here is a scan signal under the shared bars once
audit (ii) is applied, and no stronger language is used.

## (c) Published-claim audit — Lobo (gr-qc/0701133)

Paper: F. S. N. Lobo, "A general class of braneworld
wormholes", PRD 75, 064027 (2007); full text fetched.
**Exact claim sentence (abstract):** "However, it is the
effective total stress energy tensor that violates the latter,
and in this work, the stress energy tensor confined on the
brane, threading the wormhole, is imposed to satisfy the NEC."
**Author's own caveat (exact):** "However, the question of
what 5-dimensional geometry produces this is much more
difficult to answer, and shall not be explored here."

Independent transcription (his Sec. III.A dust, "spatial
Schwarzschild" b=r₀, Φ=0, ρ=λ branch; our SMS conventions):
R=0 exactly (SymPy), E^t_t = **−12πλ**, E^r_r = **4πλ + r₀/r³**,
E^θ_θ = **4πλ − r₀/(2r³)** — the 12πλ / 4πλ magnitudes and the
r₀/r³, r₀/(2r³) coefficients reproduce his printed eqs.
(37)–(38); trace E = 7.1e-15; dust (ρ=λ>0, p=0) obeys all four
ECs and, Φ=0, is identically conserved, so (i) and (ii) hold.
**Full-system verdict on the claim: PARTIAL.** The brane-level
claim is verified — as stated, and note it is *imposed*, not
derived. At the full-system level it is not verified: in this
one exactly auditable case E does **not decay at infinity**
(E^t_t → −12πλ at r=10³r₀), so it cannot be the Weyl
projection of a Schwarzschild–AdS₅ bulk (whose E ∝ Q/r⁴ → 0),
and the paper exhibits no bulk geometry at all (its own
caveat). His asymptotically-flat example (Sec. III.C) could
not be transcribed unambiguously from the fetched text
(eqs. (45)–(50) OCR-garbled; eq. (47) as read contradicts the
stated b′(r₀)=γ²<1) — logged, not fabricated (Phase-3
Das–Paul precedent); as read, its σ_t carries an r^{−3} term,
which is not the tidal r^{−4} profile in any case. Open
clause: an explicit bulk metric whose projection is his E.

## Verdict restated, anatomy, follow-ups

**PARTIAL.** Open clause, exactly: **audit (iv)** — for the
throat case that passes everything else (√-shape, Φ=0,
trace-solved dust-minus, λ=1: EC-legal, (i) 3.6e-8, (ii)
7.8e-6) and for the wall's pointwise-complete supply at all
β∈{0.1,1.1,1.5}, no bulk closure realises the required E: the
tidal (Schwarzschild–AdS₅) profile does not match, and the
system's one free bulk function — 𝒰(r) on the throat,
equivalently the wall's E field off the binding set — is
undetermined by brane data. The deciding bulk datum is
𝒰(r) (throat: 𝒰 = 0.565/r₀² at the throat with the computed
profile in `p211_throat.json`).

What binds, in order: (1) bulk realisation (iv) — everywhere;
(2) the (i)/(ii) competition on τ — generic prescriptions fail
one of them at O(1) (vacuum trace 1.0–3.9; radiation divergence
0.63–0.67; wall dust divergence ratio 75–1946); (3) the
plus-branch/radiation escapes buy consistency with
non-decaying or non-existent matter. What does *not* bind:
brane ECs (satisfiable), Π (never carries the violation),
pointwise supply magnitude on the wall (ratio ≥1 at 100% of
binding points at all β).

**Named follow-ups (Failure Protocol):**
1. **Bulk-lift attempt for the one surviving throat case:**
   take 𝒰(r) from the √/Φ=0/dust-minus solution as boundary
   data and run a Campbell–Magaard / numerical bulk extension
   off the brane; the deciding question is bulk regularity
   (no singularity at finite proper distance off-brane). A
   regular lift upgrades this case to VERIFIED RELOCATION; a
   forced singularity closes (iv) for this family with
   anatomy.
2. **Wall divergence repair scan:** replace dust with an
   anisotropic τ carrying a free radial-pressure function and
   impose trace + conservation as a pointwise linear system
   on the binding set (the throat's F3/F4 trade-off, wall
   version): does any (ρ, p_r, p_t) field satisfy both at
   β=1.1/1.5 with ECs intact? This directly attacks the
   λ/(6ρ) anatomy — if the anisotropic system is solvable,
   (ii) stops binding and (iv) is the sole open clause.
3. **Lobo III.C re-audit** if a clean text (publisher PDF)
   becomes fetchable: transcribe eqs. (45)–(50) exactly and
   run the α-profile test on his σ_t.

*Internal only. Nothing uploaded, no external contact beyond
fetching the paper text above.*
