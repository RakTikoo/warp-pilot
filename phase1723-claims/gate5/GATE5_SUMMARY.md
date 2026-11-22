# Gate-5 — verdict table and restatements

Novelty & Verification Gate 5 (closed 2026-11-22). Scope:
every completed-programme result that had not yet passed
a Gate — Phase 17 (G5-8), Phase 19 (G5-9), Phase 20
(G5-1, G5-2), Phase 22 (G5-6, G5-7), Phase 23 (G5-3,
G5-4, G5-5). Method: independent second-path
recomputation of every deciding number (fresh code from
the claim statement; for paper audits, re-derivation
from the paper's printed formulas), plus documented
novelty searches (arXiv, INSPIRE-HEP, Semantic Scholar,
web; queries logged verbatim in the worker reports under
`results/`).

**Headline: the arithmetic is right everywhere; the
novelty was overstated in three of nine claims.**
NOT REPRODUCED: 0 of 9. NOT YET: 0.

## Verdict table (whole-claim level)

| Claim | Correctness | Novelty | Gate verdict |
|---|---|---|---|
| G5-1 f(T) relocation = ghost identity (P20-2) | REPRODUCED | PARTIALLY KNOWN | UPLOAD-READY AFTER RESTATEMENT |
| G5-2 EiBI obstructions + BHL Eq.(29) misprint (P20-2) | REPRODUCED ((b) WITH RESTATEMENT) | NOVEL (delimited; (b) as restated) | UPLOAD-READY AFTER RESTATEMENT |
| G5-3 Thin-shell σ-identity (P23-1) | REPRODUCED | PARTIALLY KNOWN — deciding statements are Poisson & Visser 1995 | DEAD AS OURS (bookkeeping wording only) |
| G5-4 GJW ledger (P23-2) | REPRODUCED | PARTIALLY KNOWN | UPLOAD-READY AFTER RESTATEMENT |
| G5-5(a) Alencar et al. audit (P23-4) | REPRODUCED WITH RESTATEMENT (R1–R3) | NOVEL | UPLOAD-READY AFTER RESTATEMENT |
| G5-5(b) ASG exact cancellation (P23-4) | REPRODUCED (strengthened: analytic identity) | PARTIALLY KNOWN | UPLOAD-READY AFTER RESTATEMENT |
| G5-6 Lentz refutation (P22-1) | REPRODUCED | PARTIALLY KNOWN — refutation-in-substance is SSV 2021 | DEAD AS OURS (confirmation wording only) |
| G5-7 Krasnikov ledger (P22-2) | REPRODUCED | PARTIALLY KNOWN — all headline components 1997–98 | DEAD AS OURS (ledger wording only) |
| G5-8 Formation paths (P17) | REPRODUCED ((d) WITH RESTATEMENT) | PARTIALLY KNOWN ((a),(c),(d) NOVEL delimited; (b) known) | UPLOAD-READY AFTER RESTATEMENT |
| G5-9 Bimetric anatomy (P19-1) | REPRODUCED | PARTIALLY KNOWN | UPLOAD-READY AFTER RESTATEMENT |

Count: **0 intact** at whole-claim level (closest: G5-2,
three of four sub-items REPRODUCED × NOVEL as stated);
**6 after restatement** (G5-1, G5-2, G5-4, G5-5, G5-8,
G5-9); **3 confirmations/bookkeeping only** (G5-3, G5-6,
G5-7). G5-3, G5-6 and G5-7 must never be presented as
discoveries.

## Restatements (verbatim — the only forms in which these claims may be uploaded)

**G5-1:** "On the T≡0 Böhmer–Harko–Lobo wormhole
background the quadratic tensor action equals f_T(0)
times the TEGR tensor action — the proportionality and
c_T² = 1 being the standard f(T) perturbation result
(Cai et al., arXiv:1801.05827) — and since BHL's
background equations make throat matter legal iff
f_T(0) < 0, matter legality on this background is
identically a tensor ghost (kinetic coefficient −1
relative to TEGR)."

**G5-2(b)** (sub-items (a), (c), (d) upload-ready as
stated): "the power-law NLED branch (of which Maxwell
is the α_e = 1 endpoint) is gradient-unhealthy on the
EC-legal sub-window −1 ≤ α_e < 0, where dp_θ/dρ = α_e
< 0."

**G5-4:** "The Gao–Jafferis–Wall mechanism
(arXiv:1608.05687) works as published. Its operating
bounds are also published: the throat is open for a
proper time below the Planck time and the transferable
quanta scale as N ∼ (r_h/ℓ)^{d−1}, so at r_h ∼ ℓ
information cannot be reliably sent (Freivogel et al.,
arXiv:1907.13140). What we add is the evaluated
macroscopic ledger: setting the horizon scale L = 1 m
in the published formulas gives an open proper time of
1.7×10⁻⁷⁹ s (73.8 orders below a 10 μs crossing bar;
the Planck-time cap itself is 38.3 orders below it), a
standard-coupling capacity of 3.5×10⁻⁴⁴ kg (45.3
orders below a 70 kg traveller; the formal S_BH
counting bound does not rescue a coherent traveller,
whose probe shift exceeds |ΔV| by ~72 orders), and a
negative-energy demand/supply ratio of 1.5×10⁷²
against the classical throat demand. Because
Δτ ∝ ℓ_P²/L follows from GJW's ΔV ∼ hG_N/R^{D−2}, a
1 ly throat is worse on every operating number
(Δτ = 1.8×10⁻⁹⁵ s)."

**G5-5(a)** (restatements R1–R3):
R1: "Matter NEC1 holds only to **1.0224 r₀** (exact
root of ρ+p_r=0 at ξ=r₀=1; the figure 1.0227 r₀ in the
checkpoint is the first failing point of the phase's
scan grid, not the root)."
R2: "κ∇_μT^μ_r near the throat has **magnitude 7.70**
(0.63× the equation scale, rising to 1.17×); its sign
flips with the divergence/index convention and carries
no content."
R3: "The printed region decomposition `regionsr` is
**refuted** (counterexample at the paper's own
ξ=r₀=1: ω(1.05r₀)=−2.09, ω(1.20r₀)=+1.68; true phantom
band (1.022, 1.091)). Its lower bound √(2ξ) equals the
paper's ρ+p_r root evaluated at the window edge
r₀²=2ξ; **the provenance of its upper bound
√(2ξ)√(√51−3)=2.878 is not established** (the ρ root
at the edge is 1.511) — delete the claim that both
bounds are edge-evaluated roots."

**G5-5(b)** (restated form): the exact-cancellation
identity and its throat application under k = ξ/r,
with the √200 ℓ_P curvature-identification switch-off,
stated against the known background that
cutoff-identification dependence in RG-improved gravity
is itself published. The identity:
κ(ρ+p_r)(r₀) = (b′−1)[(1+f₀)/r₀² + f′(r₀)/(2r₀)]; for
f ∝ r^(−n) the bracket is [1+f₀(1−n/2)]/r₀² — n=2
(k=ξ/r) is the exact fixed point where prefactor and
X-derivative corrections cancel for any amplitude/shape;
n=4 (curvature) gives the window and the √200
switch-off from the same formula.

**G5-8(d)** (restatement confined to the ceiling;
(a)–(c) as stated, with the worker's delimitation
sentence and credits — Alcubierre gr-qc/9409004;
Natário gr-qc/0110086; Santiago–Schuster–Visser
arXiv:2105.03079; Finazzi et al. arXiv:0904.0141 as the
dynamical-formation neighbour — and the Class B label
on every formation statement): "β* lies in the bracket
(0.025, 0.0275]: β=0.025 is the last fully legal
destination (≈+1.20e-5, Type I 1.0, h-confirmed in a
second-path audit) and β=0.0275 the first
unambiguously illegal one (≈−2.5e-5, SEC, r=10.5, both
auditors, both resolutions); the +6.41e-10 figure is
resolution-dependent and must not be quoted as the
onset value."
Delimitation sentence (worker W-E, required for
upload): "New here are: an instant-by-instant
full-energy-condition audit exhibiting a legal
prescribed formation path (Class B,
necessary-not-sufficient) from flat space to a
positive-energy warp shell, with a measured rate
barrier on the same path; the measured ∂_t tax of
subluminal ramps, exactly linear in β̇; the destination
ceiling of the Finalist-A family, β\* ∈ (0.025,
0.0275]; and, for the shift-first ordering, the
quantitative onset (illegal from β = 0.01) and its
ordering corollary — the qualitative exoticity of a
bare varying shift itself is published (Alcubierre
1994; Natário 2002; Santiago–Schuster–Visser 2022) and
is not claimed."

**G5-9:** "In Hassan–Rosen bimetric gravity, that the
two sectors cannot both be made NEC-clean — the
interaction effective stress-energy tensors' NECs are
strongly anti-correlated and can be simultaneously
fulfilled only when they saturate — is a known general
result (Baccetti, Martin-Moruno & Visser,
arXiv:1206.3814). What is new here is its quantitative
anatomy for a moving superluminal warp shell, measured
end-to-end on the Phase-14 closest-miss configuration:
with a direction-dependent second metric (54
coefficients, 128 collocation points) the pooled
Bianchi constraint closes at β=1.5 for the first time
(0.0189/0.0181 at h=0.3/0.15 against the 0.02 bar)
while its t-component never closes in any row (floor
0.0276–0.0966 at audit points, higher on fresh points),
and the matter Θ_f defined by the full f-sector
equation violates the NEC on 71–100% of the volume at
every coupling m² in every row — the
configuration-level realisation, for a warp shell, of
exoticity relocation into the f-sector."

## Confirmation / bookkeeping wordings (never as discoveries)

**G5-3:** "For two identical Morris–Thorne exteriors
glued at r = a, the Lanczos surface density is
σ = −√(1−b(a)/a)/(2πa) — the Morris–Thorne
specialisation of the surface density printed by
Poisson & Visser (arXiv:gr-qc/9506083, eqs. (8), (11),
(18)) — which is negative for every shell and
independent of the redshift function, so no choice of
Φ can make any surface energy condition containing
σ ≥ 0 hold. The Schwarzschild member's linearised
stability window is likewise Poisson & Visser's:
stability requires β₀² ≥ 3/2+√3 ≈ 3.232 or β₀² ≤ −1/2
(their eqs. (35)–(36)), hence never meets physical
sound speeds β₀² ∈ [0,1], as they state in their
conclusion. Our additions are bookkeeping only: a
zero-pass full-EC scan over the general (q, A) plane,
and the observation that at a = 1 m the tidal bar is
first met at x = a₀/(2M) ≥ 1.83×10¹⁶, exactly where
|σ| is largest in the family — weakening the gravity
does not weaken the shell's exoticity."

**G5-6:** "An independent numerical confirmation, on a
registered representative of Lentz's printed
gradient-shift class (Φ = v_s·z·f(r), v_s = 2, R = 1),
of the Santiago–Schuster–Visser result
(arXiv:2105.03079) that this class violates the energy
conditions: Eulerian ρ_Eul reaches −0.577, the
all-observer NEC margin is −3.398 at h = 0.02, realised
by transverse null directions in the rear wall where
ρ_Eul = +2.27 and principal tensions reach ≈ −5.5, and
SSV's identity ∫ρ_Eul = 0 for a localised gradient
soliton is confirmed numerically (∫ρ_Eul = −0.0058
against ∫|ρ_Eul| = 4.108). Lentz's unprinted figure
soliton is not addressed."

**G5-7:** "A single-computation verification ledger for
the Everett–Roman four-dimensional Krasnikov tube
(arXiv:gr-qc/9702049), confirming their 1997
conclusions with exact numbers at a = 1 m, ε = 0.1 m,
δ = 0.01: all-observer NEC worst margin −1.237 (inner
wall), QI required/legal ratios 1.06×10⁷²–1.06×10⁷³
(D = 1 m) and 1.00×10⁸⁸–1.00×10⁸⁹ (D = 1 ly),
construction-inclusive earliest arrival at B ≥ D/c,
and the single-tube no-CTC property. The hyperfast
property, the no-CTC result, the one-way bound and the
QI prohibition are Krasnikov's (1998) and Everett &
Roman's (1997), not new. Bibliographic note: Everett &
Roman is arXiv:gr-qc/9702049; gr-qc/9701051 is Brody &
Hughston, 'Statistical Geometry in Quantum
Mechanics'."

## Errata and residual checks flowing from this gate

- **Phase 17 (and Phase 16, inherited):** the +6.41e-10
  frozen core-worst figure at β=0.025 is an h=0.3
  single-auditor read and is resolution-fragile; the
  ceiling stands as the bracket (0.025, 0.0275].
  Erratum logged in `phase17/CHECKPOINT17.md`
  ("ERRATA (Gate-5, 2026-11-22)").
- **G5-2(d) residual check (Semantic Scholar) —
  COMPLETED 2026-11-22, negative:** the citing-list
  pull Gate-5 flagged was performed. Semantic Scholar
  record for Böhmer–Harko–Lobo (arXiv:1110.5756, DOI
  10.1103/PhysRevD.85.044033; S2 paperId
  2bc5c44d4d4195977a94f12a7d9429067b593e89) lists 229
  citations; the full citing list (229/229 returned)
  was scanned — **zero** citing titles match
  erratum / corrigendum / comment / reply / critique /
  reconsider patterns, and there are no joint
  Böhmer+Harko self-citations that could carry a
  correction. Combined with Gate-5's arXiv (no version
  past v2, 2012), INSPIRE-HEP and APS/DOI searches:
  **no published erratum, corrigendum or comment on
  the paper exists in any source checked.** The
  Eq.(29) misprint stands as previously unflagged in
  print; the G5-2(d) wording needs no adjustment.
- **G5-4 nit:** the phase's S_BH figure is in nats,
  labelled "bits" (1.73×10⁷⁰ in bits) — immaterial;
  rescues nothing either way.
- **G5-9 endpoint notes:** second-path T_req DEC
  violation 0.828–1.000 vs the phase's 0.85–1.000
  (lowest cell 0.023 below, under stricter non-Type-I
  DEC counting); best NEC violation 0.109 vs 0.110.
  Convention/FD-order effects; no bar, sign or verdict
  clause affected.
