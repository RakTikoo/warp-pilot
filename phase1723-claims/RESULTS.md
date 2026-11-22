# Phase 17–23 claims — Gate-5 verified results note

**What Gate-5 did.** Gate-5 (Novelty & Verification Gate 5,
closed 2026-11-22) independently recomputed all nine
completed-programme results that had not yet passed a Gate —
the Phase 17 formation paths, the Phase 19 bimetric anatomy,
the Phase 20 wormhole-stability results, the Phase 22 Lentz
and Krasnikov audits, and the Phase 23 thin-shell, GJW and
asymptotic-safety ledgers. For every claim, a verifier wrote
fresh code from the claim statement (never a re-run of the
phase script) and reproduced — or failed to reproduce — the
deciding numbers; novelty was then checked against the
literature with logged queries on arXiv, INSPIRE-HEP,
Semantic Scholar and the web. **Every deciding number in
all nine claims reproduced on the independent second path
(NOT REPRODUCED: 0 of 9).** Every downgrade is on the
novelty/framing axis.

**The honest count (whole-claim level, 9 claims):**
- **0 survived intact** as stated (no whole claim passes
  both axes without a restatement);
- **6 survived after restatement** (Section A);
- **3 fell as discoveries** and are uploadable only as
  independent confirmations or bookkeeping (Section B).

Nothing in this note is stated more strongly than the gate
record (`gate5/GATE5_SUMMARY.md` in this folder; full gate
record and worker reports under `gate5/`). Hedges intact:
formation-path statements are Class B — prescribed
geometry, read-off matter; a legal instant path is
necessary, not sufficient, for formation.

---

## Section A — Gate-verified results

Each claim below is stated **only** in the verbatim
restated wording fixed by Gate-5, followed by the gate's
deciding numbers from the independent second path.

### A1. G5-1 — f(T) wormhole: matter legality is identically a tensor ghost

> "On the T≡0 Böhmer–Harko–Lobo wormhole background the
> quadratic tensor action equals f_T(0) times the TEGR
> tensor action — the proportionality and c_T² = 1 being
> the standard f(T) perturbation result (Cai et al.,
> arXiv:1801.05827) — and since BHL's background equations
> make throat matter legal iff f_T(0) < 0, matter legality
> on this background is identically a tensor ghost
> (kinetic coefficient −1 relative to TEGR)."

Deciding numbers (second path): the symbolic TT expansion
of the torsion scalar gives T = λ²·½(ε̇² − ε′²) with no
linear term, so S₂^tensor = f_T(0)×TEGR exactly (f_TT
enters only via (δ₁T)² = 0 for tensor modes); kinetic
ratio −1.0, c_T² = 1.0; from BHL's printed Eqs.(22)/(23),
ρ and NEC1 at the throat are both ∝ −f_T(0), so legality
⇔ f_T(0) < 0 = the ghost sign; background check
max |T| = 4.668e-16 on (1, 10⁴].

### A2. G5-2 — EiBI throat obstructions, and the BHL Eq.(29) misprint

**(a) Fluid family c_t² = −1 (REPRODUCED × NOVEL, as
stated).** c_t² = 1 + 2κρ = −1.0 at the throat for every
C₀ ∈ {0.5, 1, 2, 5} — the throat definition forces
ρ(r₀) = 1/|κ| — with a negative shell to
r* = (3C₀/2)^{1/4} (C₀ = 2: second path 1.316073 vs
analytic 1.316074; genuine C₀ = 0.5: 0.930601 vs
0.930605). Gate echoes: conservation 8.88e-16,
NCC −4.0/−2.0.

**(b) NLED gradient band — stated only in the gate's
restated wording:**

> "the power-law NLED branch (of which Maxwell is the
> α_e = 1 endpoint) is gradient-unhealthy on the
> EC-legal sub-window −1 ≤ α_e < 0, where
> dp_θ/dρ = α_e < 0."

(The Phase-20 "Maxwell branch" name was wrong: Maxwell
is only the healthy endpoint. Second path: dp_θ/dρ = α_e
exactly, and independently the NLED effective-metric
speed φ_F/(φ_F + 2Fφ_FF) = α_e for one polarisation, so
the sign is a real propagation sign.)

**(c) det Ω = 0 posing obstruction (REPRODUCED × NOVEL,
as stated).** From Shaikh's Eq.(7): ω_t = ω_r = 1 − κp_θ,
ω_θ = 1 + κρ, so det Ω = (1−κp_θ)²(1+κρ)² = 0 at r₀
identically and H(r₀) = 0 — the gravitational
perturbation problem cannot be posed at the throat;
eigenvalues are all > 0 for r > r₀ (det min 7.63e-08
Maxwell / 4.77e-09 fluid on the second-path grid).

**(d) BHL printed Eq.(29) misprint (REPRODUCED ×
NOVEL).** Böhmer–Harko–Lobo (arXiv:1110.5756, Phys.
Rev. D 85 (2012) 044033), transcribed from print by the
second path: the printed Eq.(29) gives p_r(throat) = 0
and NEC1 = 0.500, while the printed Eq.(14) simplifies
symbolically to p_r = (1−s)/(2r²), NEC1 = 1.000,
matching the paper's own Eq.(31) to 8.9e-16 — Eq.(29)
contradicts it. Conservation: the Eq.(29) branch's max
residual is 77.87336046345915 (1676.8 at r = 1+10⁻⁷;
4.747e-03 for r > 2); the Eq.(14) branch closes
(second-path closed-form representation 1.2e-11).
Eq.(14)-vs-Eq.(29) grid max difference 0.49040404877061383,
throat-limit difference exactly 0.5. No erratum,
corrigendum or comment found on arXiv (no version past
v2, 2012), INSPIRE-HEP, APS/DOI searches, the authors'
later work, or a Semantic Scholar citing-list pull
(2026-11-22; see `gate5/GATE5_SUMMARY.md`).

### A3. G5-4 — Gao–Jafferis–Wall traversability ledger

> "The Gao–Jafferis–Wall mechanism (arXiv:1608.05687)
> works as published. Its operating bounds are also
> published: the throat is open for a proper time below
> the Planck time and the transferable quanta scale as
> N ∼ (r_h/ℓ)^{d−1}, so at r_h ∼ ℓ information cannot be
> reliably sent (Freivogel et al., arXiv:1907.13140).
> What we add is the evaluated macroscopic ledger:
> setting the horizon scale L = 1 m in the published
> formulas gives an open proper time of 1.7×10⁻⁷⁹ s
> (73.8 orders below a 10 μs crossing bar; the
> Planck-time cap itself is 38.3 orders below it), a
> standard-coupling capacity of 3.5×10⁻⁴⁴ kg (45.3
> orders below a 70 kg traveller; the formal S_BH
> counting bound does not rescue a coherent traveller,
> whose probe shift exceeds |ΔV| by ~72 orders), and a
> negative-energy demand/supply ratio of 1.5×10⁷²
> against the classical throat demand. Because
> Δτ ∝ ℓ_P²/L follows from GJW's ΔV ∼ hG_N/R^{D−2}, a
> 1 ly throat is worse on every operating number
> (Δτ = 1.8×10⁻⁹⁵ s)."

Deciding numbers (second path, recomputed from the
published ANE formula): Δτ = 1.7427×10⁻⁷⁹ s at 1 m
(73.759 orders short of the 10 μs bar), Planck-cap gap
38.268 orders, capacity 3.5177×10⁻⁴⁴ kg (45.299 orders
short of 70 kg), demand/supply = 1.5113×10⁷²; at 1 ly,
Δτ = 1.8421×10⁻⁹⁵ s (89.735 orders short); anti-scaling
Δτ ∝ ℓ_P²/L confirmed exactly (ratio = length ratio to
15 digits); the Phase-2 gate row reproduced with ANE
relative differences ≤ 1.2×10⁻¹⁶.

### A4. G5-5 — Asymptotic safety: Alencar et al. audit, and the exact cancellation

**(a) Claim audit — Alencar et al. (arXiv:2106.02476)
PARTIAL verdict stands (REPRODUCED WITH RESTATEMENT).**
Second-path deciding numbers (paper transcribed from
its LaTeX source): throat κρ/κp_r/κp_l = +5.0/−3.0/−5.0
at ξ = r₀ = 1; radial NEC window r₀² < 2ξ, edge
√2 ℓ_P = 1.414, f₃ edge 1.861 ℓ_P; SEC = −8ξ/r₀⁴
exactly at the throat; effective sector
κ(ρ+p_r) = −2r₀²/r⁴ < 0 on the entire domain; the
source exchanges energy with the running coupling at
O(1) (|∇T| = 7.70 = 0.633× the equation scale, max
1.169×). Two printed errors confirmed: the p_l equation
carries an extra f′ term (printed form gives
κp_l(r₀) = −32 vs the correct −5; dimensionally
inconsistent in print), and the Kretschmann rescaling
is ξ → √3 ξ, not the printed ξ → √4 ξ (correct f₃ edge
1.861 ℓ_P, not 2.0). The gate's restatements, verbatim:

> "Matter NEC1 holds only to **1.0224 r₀** (exact root
> of ρ+p_r=0 at ξ=r₀=1; the figure 1.0227 r₀ in the
> checkpoint is the first failing point of the phase's
> scan grid, not the root)."

> "κ∇_μT^μ_r near the throat has **magnitude 7.70**
> (0.63× the equation scale, rising to 1.17×); its sign
> flips with the divergence/index convention and
> carries no content."

> "The printed region decomposition `regionsr` is
> **refuted** (counterexample at the paper's own
> ξ=r₀=1: ω(1.05r₀)=−2.09, ω(1.20r₀)=+1.68; true
> phantom band (1.022, 1.091)). Its lower bound √(2ξ)
> equals the paper's ρ+p_r root evaluated at the window
> edge r₀²=2ξ; **the provenance of its upper bound
> √(2ξ)√(√51−3)=2.878 is not established** (the ρ root
> at the edge is 1.511) — delete the claim that both
> bounds are edge-evaluated roots."

**(b) Origination kill — exact cancellation
(REPRODUCED, and strengthened to an analytic identity;
stated against the known background that
cutoff-identification dependence in RG-improved gravity
is itself published).** The identity, verbatim from the
gate record: κ(ρ+p_r)(r₀) =
(b′−1)[(1+f₀)/r₀² + f′(r₀)/(2r₀)]; for f ∝ r^(−n) the
bracket is [1+f₀(1−n/2)]/r₀² — n=2 (k=ξ/r) is the exact
fixed point where prefactor and X-derivative corrections
cancel for any amplitude/shape; n=4 (curvature) gives
the window and the √200 switch-off from the same
formula. Deciding numbers: the two corrections are
−237.1946/+237.1946 κ-units at 1 ℓ_P (ξ_cut = 10) and
cancel identically; throat NEC equals the GR value
(−2.0 Ellis, −0.5 √-shape) at every scale from 1 ℓ_P to
1 m; curvature-identification switch-off √200 =
14.142 ℓ_P (second-path grid 14.1416).

### A5. G5-8 — Formation paths for the Finalist-A shell family

Sub-claims (a)–(c) reproduced as stated; sub-claim (d)
only in the gate's restated wording.

**(a) A legal morph path exists (Class B,
necessary-not-sufficient).** Growing wall and shift
together at T=200: all 13 instants legal/dynamic, worst
at t=50, λ=0.15625 — second path +7.503e-6 (h=0.3) /
+7.525e-6 (h=0.15) vs claimed +7.532e-6; frozen twin
+8.297e-6 vs +8.334e-6. At T=40 the same path hits a
rate barrier: first failure at λ* = 0.0197 with
NEC −1.2528e-5 (claimed −1.252e-5), DEC −1.0000000014,
Type I 0.0, site r=21.5, while its frozen twin is
core-less — a pure rate failure.

**(b) Shift-first is impossible for this family.** A
pure varying shift on flat space is core-less at
β=0.005/0.0074 and illegal from β=0.01: second path
NEC −2.046e-5 (claimed −2.126e-5), DEC −1.0000000011,
Type I 0.0, site r=11.0, h=0.15-confirmed; dynamic read
≈ frozen — a configuration-space fact, not a rate
effect. (The qualitative exoticity of a bare varying
shift is published — Alcubierre 1994; Natário 2002;
Santiago–Schuster–Visser 2022 — and is not claimed;
the measured onset and the ordering corollary for this
family are the new part.)

**(c) Ramps and the ∂_t tax.** Segment 0→0.02 is legal
at all tested rates (T=400/200/40 midpoints
+1.21143e-5 / +1.21085e-5 / +1.20620e-5, Type I 1.0).
The DEC tax is exactly linear in β̇ and tiny: second
path 5.802e-9/1.160e-8/5.802e-8 vs claimed
5.72e-9/1.14e-8/5.72e-8; regression slope 7.735e-5,
R² = 0.99999999993 (claimed 7.63e-5, R² = 1.000); the
NEC tax is identically 0.0, as claimed.

**(d) Destination ceiling — stated only in the gate's
restated wording:**

> "β* lies in the bracket (0.025, 0.0275]: β=0.025 is
> the last fully legal destination (≈+1.20e-5, Type I
> 1.0, h-confirmed in a second-path audit) and β=0.0275
> the first unambiguously illegal one (≈−2.5e-5, SEC,
> r=10.5, both auditors, both resolutions); the
> +6.41e-10 figure is resolution-dependent and must not
> be quoted as the onset value."

(See the Phase-17 erratum, logged 2026-11-22: the
+6.41e-10 marginal figure does not reproduce; the
ceiling stands as the bracket.)

### A6. G5-9 — Bimetric anatomy: exoticity relocation into the f-sector

> "In Hassan–Rosen bimetric gravity, that the two
> sectors cannot both be made NEC-clean — the
> interaction effective stress-energy tensors' NECs are
> strongly anti-correlated and can be simultaneously
> fulfilled only when they saturate — is a known
> general result (Baccetti, Martin-Moruno & Visser,
> arXiv:1206.3814). What is new here is its quantitative
> anatomy for a moving superluminal warp shell,
> measured end-to-end on the Phase-14 closest-miss
> configuration: with a direction-dependent second
> metric (54 coefficients, 128 collocation points) the
> pooled Bianchi constraint closes at β=1.5 for the
> first time (0.0189/0.0181 at h=0.3/0.15 against the
> 0.02 bar) while its t-component never closes in any
> row (floor 0.0276–0.0966 at audit points, higher on
> fresh points), and the matter Θ_f defined by the full
> f-sector equation violates the NEC on 71–100% of the
> volume at every coupling m² in every row — the
> configuration-level realisation, for a warp shell, of
> exoticity relocation into the f-sector."

Deciding numbers (second path; machinery gate passed
stronger than claimed — the density identity
√(−g)Σbₙeₙ(S) = √(−f)Σb₄₋ₘeₘ(S⁻¹) verified to 3.8e-15,
and the non-reversed b fails at 0.707, so the reversal
is load-bearing): pooled closure rows (3,0) β=1.5
0.0189/0.0181, (1,0) β=1.5 0.0176/0.0179, β=0.1 control
0.0184/0.0170 — exactly the claimed three rows;
t-component audit-point medians 0.0276–0.0964, never
closing, and worse on two independent unseen point sets
(0.098–0.218; 0.057–0.161); Θ_f NEC violation
0.703–1.000 across all rows/m²/h in both readings (all
four ECs fail in every row); Θ_f=0 distance 0.997–1.000;
supply sign 0.8080808… (exact).

---

## Section B — Independent confirmations (not discoveries)

The three results below were **reproduced exactly** by
Gate-5's second paths, but their substance was already
in the published literature. They are recorded here as
independent confirmations and bookkeeping only, in the
gate's exact wording, and must never be presented as
discoveries of this programme.

### B1. G5-3 — Thin-shell wormholes (bookkeeping)

> "For two identical Morris–Thorne exteriors glued at
> r = a, the Lanczos surface density is
> σ = −√(1−b(a)/a)/(2πa) — the Morris–Thorne
> specialisation of the surface density printed by
> Poisson & Visser (arXiv:gr-qc/9506083, eqs. (8),
> (11), (18)) — which is negative for every shell and
> independent of the redshift function, so no choice of
> Φ can make any surface energy condition containing
> σ ≥ 0 hold. The Schwarzschild member's linearised
> stability window is likewise Poisson & Visser's:
> stability requires β₀² ≥ 3/2+√3 ≈ 3.232 or
> β₀² ≤ −1/2 (their eqs. (35)–(36)), hence never meets
> physical sound speeds β₀² ∈ [0,1], as they state in
> their conclusion. Our additions are bookkeeping only:
> a zero-pass full-EC scan over the general (q, A)
> plane, and the observation that at a = 1 m the tidal
> bar is first met at x = a₀/(2M) ≥ 1.83×10¹⁶, exactly
> where |σ| is largest in the family — weakening the
> gravity does not weaken the shell's exoticity."

Second-path numbers: the worker's own 96,641-point scan
gives NEC/WEC/DEC/ALL = 0 passes; β₀²_crit minimum
3.23207 at x = 1.1835; tides 15.26–16.26 orders over the
1 g bar at 1 m; tidal bar first met at
x = 1.8323245234185884×10¹⁶, where |σ| = 2.1432×10²⁶
kg/m² is the family maximum (ADM 3.6745×10¹⁰ kg).

### B2. G5-6 — Lentz positive-energy soliton (confirmation)

> "An independent numerical confirmation, on a
> registered representative of Lentz's printed
> gradient-shift class (Φ = v_s·z·f(r), v_s = 2,
> R = 1), of the Santiago–Schuster–Visser result
> (arXiv:2105.03079) that this class violates the
> energy conditions: Eulerian ρ_Eul reaches −0.577, the
> all-observer NEC margin is −3.398 at h = 0.02,
> realised by transverse null directions in the rear
> wall where ρ_Eul = +2.27 and principal tensions
> reach ≈ −5.5, and SSV's identity ∫ρ_Eul = 0 for a
> localised gradient soliton is confirmed numerically
> (∫ρ_Eul = −0.0058 against ∫|ρ_Eul| = 4.108). Lentz's
> unprinted figure soliton is not addressed."

Second-path numbers: ρ_Eul at the claimed argmin site
−0.57648 (formula branch −0.57641); judge-vs-Lentz-formula
max diff 0.0024 at h=0.02; all-observer NEC −3.3984 at
h=0.02 at the rear-wall site (0.082, −0.029, −0.839),
realising direction (0.941, −0.331, 0.075); adversarial
hunt at h=0.01: −3.448; divergence identity
∫ρ_Eul = −0.0001 vs ∫|ρ_Eul| = 4.016 on the second path.

### B3. G5-7 — Krasnikov tube (verification ledger)

> "A single-computation verification ledger for the
> Everett–Roman four-dimensional Krasnikov tube
> (arXiv:gr-qc/9702049), confirming their 1997
> conclusions with exact numbers at a = 1 m,
> ε = 0.1 m, δ = 0.01: all-observer NEC worst margin
> −1.237 (inner wall), QI required/legal ratios
> 1.06×10⁷²–1.06×10⁷³ (D = 1 m) and
> 1.00×10⁸⁸–1.00×10⁸⁹ (D = 1 ly), construction-inclusive
> earliest arrival at B ≥ D/c, and the single-tube
> no-CTC property. The hyperfast property, the no-CTC
> result, the one-way bound and the QI prohibition are
> Krasnikov's (1998) and Everett & Roman's (1997), not
> new. Bibliographic note: Everett & Roman is
> arXiv:gr-qc/9702049; gr-qc/9701051 is Brody &
> Hughston, 'Statistical Geometry in Quantum
> Mechanics'."

Second-path numbers: NEC worst −1.2521 (h=0.025) /
−1.2515 (h=0.05) at the exact claimed site ρ = 8.875
(inner wall); judge-vs-Everett–Roman Eq. (T) cross-check
0.200%; QI ratios reproduced exactly (1.057×10⁷² /
1.057×10⁷³ at 1 m; 1.000×10⁸⁸ / 1.000×10⁸⁹ at 1 ly);
return-photon ODE Δt_r = −96.79, t_E = 3.21 (phase:
−97.00/3.00); construction support at B first exceeds
threshold at t = 100.4 ≥ D = 100.

---

## Evidence

Gate-5's verification artefacts — the fresh second-path
scripts (`wa_*`, `wb_*`, `wc_*`, `wd_*`, `we_*`, `wf_*`),
their result files, run logs and the six worker reports
— are in `gate5/` and `gate5/results/` in this folder.
The original phase computations live in the repository's
phase folders (`phase17/`, `phase19/`, `phase20/`,
`phase22/`, `phase23/`), which remain the full-data
record for each claim. Verdict table and restatements:
`gate5/GATE5_SUMMARY.md`.
