# Gate-5 Verification — G5-5: Asymptotic-safety throats (P23-4)

**Worker:** Gate-5 verification worker wC (fresh code: `~/workspace/warp-pilot/gate5/wc_g55.py`, run with `~/workspace/warp-pilot/venv/bin/python`, float64 throughout).
**Claim record audited:** `phase23/CHECKPOINT23.md` §P23-4; memo `phase23/results/p234_memo.md`; data `phase23/results/p234_asg.json`.
**Method (Gate-4 standard):** the phase's own script was NOT re-run. For (a) I downloaded the LaTeX source of Alencar, Bezerra, Muniz & Vieira, arXiv:2106.02476 (published version: *Universe* **7** (2021) 238, DOI 10.3390/universe7070238) from `export.arxiv.org/e-print/2106.02476` and transcribed the equations **myself** from `WormAssympSafe01-07.tex`. For (b) I re-derived the throat NEC from the general improved Morris–Thorne equations (Φ = 0) and evaluated it on a fresh 400-point log grid, r₀ ∈ [1 ℓ_P, 1 m]. Stored JSON read only for final comparison. Nothing uploaded; no external contact beyond literature search.

---

## (a) CLAIM AUDIT — Alencar et al.

### My transcription (from the paper's source, verbatim structure)

General improved equations (Φ = 0 form used below), κ = 8πG₀, G = G₀/(1+f):

- κρ = (1+f)b′/r² − (1−b/r)(f″+2f′/r) + (b′r−b)f′/(2r²)
- κp_r = −(1+f)b/r³ + (1−b/r)(2/r)f′
- κp_l = −(1+f)[(b′r−b)/(2r²)](1/r) + (1−b/r)(f′/r+f″) − (b′r−b)f′/(2r²)

Ellis b = r₀²/r; identifications (paper eq. `fKretsch`): f₁ = −ξR = 2ξr₀²/r⁴, f₂ = ξ(R_μνR^μν)^½ = 2ξr₀²/r⁴, f₃ = ξ(K)^½ = √12 ξr₀²/r⁴, hence f₁ = f₂ = f₃/√3 (paper's own line).

### My deciding numbers (fresh code)

| Quantity | Mine | Phase | Match |
|---|---|---|---|
| General eqs vs printed κρ, κp_r (f₁), max diff on r∈[1,50] | 2.9×10⁻¹⁵ / 8.9×10⁻¹⁶ | sympy diff = 0 | ✓ (float64 roundoff) |
| Throat κρ, κp_r, κp_l (ξ=r₀=1) | +5.0, −3.0, −5.0 | +5.0, −3.0, −5.0 | ✓ exact |
| κ(ρ+p_r)(r₀) | +2.0 = 2(2ξ−r₀²)/r₀⁴ | same | ✓ |
| Window edge f₁/f₂ | √2 ℓ_P = 1.41421 ℓ_P (r₀²<2ξ) | 1.41421 | ✓ |
| Window edge f₃ (correct √3) | 1.86121 ℓ_P (r₀²<2√3 ξ) | 1.86121 | ✓ |
| **SEC at throat** κ(ρ+p_r+2p_l)(r₀) | **−8.0 = −8ξ/r₀⁴** (analytic: [(6ξ−r₀²)+(−r₀²−2ξ)+2(r₀²−6ξ)]/r₀⁴) | −8.0 | ✓ exact |
| κ(ρ+p_l)(r₀) | 0.0 exactly (saturated) | 0.0 | ✓ |
| **NEC1 root** (ρ+p_r=0), ξ=r₀=1 | **r = 1.022429 r₀** (Brent) | 1.02243 (region check); 1.0227 (grid first-fail) | ✓ (see restatement R1) |
| ρ = 0 root | r = 1.091286 r₀ | 1.09129 / 1.092 | ✓ |
| Effective sector κ(ρ+p_r)_eff = −2r₀²/r⁴ | −2.0 at throat, < 0 ∀r | −2.0, entire domain | ✓ |
| Conservation: \|∇_μT^μ_r\| at r=1.00433r₀ | 7.695, ratio **0.633** × equation scale | 7.70, 0.633 | ✓ magnitude (sign is convention, R2) |
| Conservation max ratio, r∈[r₀,3r₀] | **1.169** | 1.170 | ✓ |

The headline reproduces: radial NEC/WEC/DEC at the throat hold iff r₀² < 2ξ, a window ≤ 1.86 ℓ_P wide (f₃). Every programme clause the phase added fails exactly as recorded: SEC = −8ξ/r₀⁴ at the throat, effective-sector NEC negative on the entire domain, matter NEC surviving only to ≈1.022 r₀, and an O(1) energy exchange with the running coupling (divergence 0.63×–1.17× the equation scale — the "source" is not a standalone conserved fluid).

### Per-error verdicts (the sharpest part — each decided individually against the printed source)

**Error 1 — printed p_l equation (eq. `IEQ-ll-s`): REAL ERROR IN THE PAPER. CONFIRMED.**
The printed simplified equation reads κp_l = (1+f)(r₀²/r⁴)**f′** + (1−r₀²/r²)(f′/r+f″) + (r₀²/r³)f′. The paper's own general p_l equation, specialised to Φ=0, b=r₀²/r, gives the first term as (1+f)r₀²/r⁴ with **no f′**. The printed term is dimensionally wrong (f′ carries 1/L, making the term 1/L³ against the required 1/L²). My numbers: printed form gives κp_l(r₀) = **−32.0**; the general equations give **−5.0**, matching the corrected closed form κp_l = r₀²(r⁴+32ξr²−38ξr₀²)/r⁸ to 3.2×10⁻¹⁵ over the domain, and printed-minus-general at r=2 is −0.0879 ≠ 0. Not an artefact of the phase's reading — the extra f′ is in the published LaTeX. The paper never uses p_l, so its radial headline survives its own typo. Phase verdict upheld in full.

**Error 2 — Kretschmann rescaling "ξ → √4 ξ": REAL ERROR IN THE PAPER. CONFIRMED.**
The published text (final paragraph of §II) states the f₃ results follow by "ξ → √4 ξ". The paper's own `fKretsch` line gives f₃/f₁ = √12/2 = √3, and its own text states f₁ = f₂ = f₃/√3. The correct rescaling is ξ → √3 ξ; the f₃ window edge is √(2√3) = **1.8612 ℓ_P**, not the √4 value 2.0 ℓ_P. Internal inconsistency in print, not a reading artefact. Phase verdict upheld in full.

**Error 3 — region decomposition (eq. `regionsr`): REFUTATION UPHELD — the printed decomposition is false — BUT the phase's provenance explanation is only half right (restatement R3 required).**
Printed `regionsr` (for r₀²<2ξ) claims: quintessence for r₀<r<√(2ξ); phantom for √(2ξ)<r<√(2ξ)√(√51−3) = (1.414, 2.878) at ξ=1; ω>1 beyond. Decisive counterexample at the paper's own figure parameters ξ=1, r₀=1 (which satisfies r₀²<2ξ), computed from the paper's printed ρ and p_r: **ω(1.05 r₀) = −2.089 (phantom)** — inside the band the paper labels quintessence; **ω(1.20 r₀) = +1.675 (ω>1)** — inside the band the paper labels phantom. The true bands at ξ=r₀=1 are quintessence on (1, 1.0224), phantom on (1.0224, 1.0913), ω>1 beyond — i.e. the phantom band is (1.022, 1.091), not (1.414, 2.878). So `regionsr` as printed is a genuine error in the paper (its bounds are r₀-independent, while the actual roots — the paper's own `rootrho`/`rootpl` — depend on r₀).
*Where the phase overreached:* the memo/JSON explain the printed bounds as "the roots evaluated at the window edge r₀²=2ξ". I checked: `rootpl` at r₀²=2ξ gives exactly √(2ξ) = 1.414 ✓ (the lower bound), but `rootrho` at r₀²=2ξ gives **1.5109**, not 2.878. The upper bound √(2ξ)√(√51−3) does not equal any of the paper's printed roots evaluated at the edge; its provenance is not established. The refutation stands; the explanation of how the authors produced the upper bound does not.

### Correctness verdict (a): **REPRODUCED WITH RESTATEMENT**

The Phase-23 PARTIAL verdict on the claim audit is correct in every deciding number. Exact restated wording to replace the corresponding memo/JSON lines:

- **R1:** "Matter NEC1 holds only to **1.0224 r₀** (exact root of ρ+p_r=0 at ξ=r₀=1; the figure 1.0227 r₀ in the checkpoint is the first failing point of the phase's scan grid, not the root)."
- **R2:** "κ∇_μT^μ_r near the throat has **magnitude 7.70** (0.63× the equation scale, rising to 1.17×); its sign flips with the divergence/index convention and carries no content."
- **R3:** "The printed region decomposition `regionsr` is **refuted** (counterexample at the paper's own ξ=r₀=1: ω(1.05r₀)=−2.09, ω(1.20r₀)=+1.68; true phantom band (1.022, 1.091)). Its lower bound √(2ξ) equals the paper's ρ+p_r root evaluated at the window edge r₀²=2ξ; **the provenance of its upper bound √(2ξ)√(√51−3)=2.878 is not established** (the ρ root at the edge is 1.511) — delete the claim that both bounds are edge-evaluated roots."

---

## (b) ORIGINATION KILL — exact cancellation under k = ξ/r

### Analytic demonstration (worth more than the scan — it works)

From the general improved equations at Φ=0, the throat factor (1−b/r₀)=0 kills every f″ term and every (1−b/r)f′ term in p_r, for **any** shape with b(r₀)=r₀:

κρ(r₀) = (1+f₀)b′(r₀)/r₀² + (b′(r₀)−1)f′(r₀)/(2r₀),   κp_r(r₀) = −(1+f₀)/r₀²

⇒ **κ(ρ+p_r)(r₀) = (b′(r₀)−1) · [ (1+f₀)/r₀² + f′(r₀)/(2r₀) ].**

For a power profile f = C r^(−n): f′(r₀)/(2r₀) = −(n/2) f₀/r₀², so the bracket is [1 + f₀(1 − n/2)]/r₀². **n = 2 is the exact fixed point**: the bracket is 1/r₀² for *any* amplitude C, any ω, any ξ_cut — the running-coupling prefactor correction (+f₀) and the X-sector derivative correction (−f₀) are the same number with opposite signs because d ln f/d ln r = −2 at the throat. The Bonanno–Reuter identification k = ξ_cut/r gives f = ωξ_cut²(ℓ_P/r)² — precisely n=2. Hence throat NEC = GR value identically, at every scale, for every shape. More generally the cancellation holds iff r₀f′(r₀) = −2f₀, i.e. iff f has local log-slope −2 at the throat. For curvature identifications f ∝ r⁻⁴ (n=4) the bracket is (1−f₀)/r₀²: the correction is real, equals f₀ = 2ξ/r₀² relative to the deficit, exceeds the deficit iff r₀²<2ξ (the paper's window), and falls to 1% at f₀=0.01 ⇒ **r_switch = √200 ℓ_P = 14.142 ℓ_P**. The phase's two results are one theorem: the throat NEC correction is controlled by (1 − n/2)f₀.

### My deciding numbers (fresh grid, r₀: 1 ℓ_P → 1 m, ω_BR = 1.185973)

| Case | κ(ρ+p_r)(r₀=1ℓ_P) | GR value | Pieces (prefactor / X) at ξ_cut=10 | Max \|correction\| on grid |
|---|---|---|---|---|
| Ellis, ξ_cut=1 | −2.0000000000000004 | −2.0 | −2.37195 / +2.37195 | 4.4×10⁻¹⁶ |
| Ellis, ξ_cut=10 | −2.0 | −2.0 | **−237.1946 / +237.1946** | 2.5×10⁻¹⁴ (roundoff; phase: 4.2×10⁻¹⁵ on its grid) |
| √-shape, ξ_cut=1 | −0.5000000000000001 | −0.5 | −0.59299 / +0.59299 | 1.1×10⁻¹⁶ |
| √-shape, ξ_cut=10 | −0.5 | −0.5 | −59.2987 / +59.2987 | 6.2×10⁻¹⁵ |

Curvature identification: analytic r_switch = √200 = **14.14214 ℓ_P**; my grid value 14.1416 ℓ_P (phase grid: 14.209). Window edge √2 ℓ_P ✓. The checkpoint's "−237.19/+237.19 κ-units at 1 ℓ_P" is confirmed digit-for-digit. r_switch for k=ξ/r: none exists — the correction is identically zero, already below 1% at the grid floor; "switches off at √200 ℓ_P ≈ 14 ℓ_P" for the curvature identification is confirmed. Effective sector = GR tensor by construction, throat NEC identical negative value.

### Correctness verdict (b): **REPRODUCED** — and strengthened: the cancellation is now an analytic identity (log-slope −2 fixed point), not only a numeric scan result. No restatement needed.

**Overall correctness: (a) REPRODUCED WITH RESTATEMENT (R1–R3 above); (b) REPRODUCED. The Phase-23 verdicts — claim PARTIAL, origination KILL (macroscopic) — stand.**

---

## Novelty

### Verbatim query log (browser_search; sources checked: arXiv, INSPIRE-HEP, Semantic Scholar via arXiv citation links, MDPI/Universe, Springer/EPJC, ScienceDirect, general web)

1. `Alencar Bezerra Muniz Vieira traversability Ellis wormholes asymptotically safe gravity critique comment`
2. `arXiv 2106.02476 citations comment erratum asymptotic safety wormhole`
3. `RG improved wormhole cutoff identification dependence k xi/r throat null energy condition cancellation`
4. `Bonanno Reuter RG improvement cutoff identification ambiguity criticism asymptotic safety black hole`
5. `"2106.02476" OR "Ellis-Bronnikov wormholes asymptotically safe" cited by follow-up energy conditions`
6. `Koch Saueressig scale identification RG improved black holes proper distance Kretschmann cutoff dependence`
7. `"RG improvement" wormhole "energy conditions" throat asymptotic safety Moti Panella cutoff function`

### (a) Critique of Alencar et al. — **NOVEL**

No published comment, erratum, or critique of arXiv:2106.02476 / DOI 10.3390/universe7070238 was found in any source checked (17 citations recorded on the OUCI index; the citing works found are extensions, not critiques). The follow-up literature *extends* the claim without running the phase's clauses: Nilton, Furtado, Alencar & Landim, "Generalized Ellis–Bronnikov wormholes in asymptotically safe gravity", arXiv:2203.08860, *Annals of Physics* **448** (2023) 169195 — same curvature identifications, radial conditions only, no SEC/effective-sector/conservation read, none of the three errors flagged; "Schwarzschild-like Wormholes in Asymptotically Safe Gravity", arXiv:2108.07912 — same pattern. None of the three printed errors (p_l f′, √4, `regionsr`), the SEC value −8ξ/r₀⁴, the effective-sector NEC failure, or the O(1) non-conservation appears in anything found. The audit package — including all three error corrections — is, on this search, previously unpublished.

### (b) Exact cancellation — **PARTIALLY KNOWN** (delimitation below)

*Known part (cite exactly):* that RG-improvement outcomes depend on the cutoff identification and on the level of implementation is a long-standing, explicitly published sore point — e.g. Bonanno & Reuter's proper-distance identification vs Kretschmann identification for improved Schwarzschild (reviewed in Saueressig et al., "Black holes in Asymptotically Safe Gravity", PoS FFP14 (2014) 174); Borissova & Carballo-Rubio, "Effective geometrodynamics for renormalization-group improved black-hole spacetimes in spherical symmetry", arXiv:2601.17115, which "establish[es] explicitly the discrepancies in the outcomes of RG-improvement when implemented at the level of the action, in the field equations, or in the Schwarzschild solution"; Konoplya & Zhidenko, arXiv:2206.14714, on identification-parameter arbitrariness. Recent k = ξ/r wormhole papers (Dekel–Zhao halo wormholes, *Eur. Phys. J. C* **86** (2026) 407, DOI 10.1140/epjc/s10052-026-15676-2; Burkert-profile wormholes, *Phys. Lett. B* **876** (2026) 140381, DOI 10.1016/j.physletb.2026.140381) use k=ξ/r at solution/action level and report throat NEC still violated — qualitatively consistent with "k=ξ/r does not rescue a throat", but they do not compute the improved-*equations* throat NEC and state no cancellation.
*Not found anywhere, and therefore the new part:* (i) the identity itself — κ(ρ+p_r)(r₀) = (b′−1)[1+f₀(1−n/2)]/r₀² and the exact cancellation at log-slope n=2 for arbitrary amplitude/shape; (ii) its application to wormhole throats under k=ξ/r in the truncated-X improved-equations formalism; (iii) the curvature-identification switch-off number √200 ℓ_P ≈ 14.14 ℓ_P. No source states "ASG does nothing to a throat under k=ξ/r", in those words or in equivalent formula form.

**Novelty verdicts: (a) NOVEL. (b) PARTIALLY KNOWN — the identification-dependence framing is known (cited above); the cancellation identity, its throat application, and the √200 ℓ_P switch-off are new on this search.**

---

## Bottom line

Phase-23 P23-4 survives independent verification. Headline window r₀²<2ξ (≤1.86 ℓ_P), SEC −8ξ/r₀⁴, effective-sector NEC failure everywhere, O(1) non-conservation, the −237.19/+237.19 exact cancellation at every scale 1 ℓ_P–1 m, and the √200 ℓ_P curvature switch-off are all reproduced from the paper's own printed formulas and a fresh derivation — the cancellation now with an analytic proof. Two of the three alleged paper errors are exactly as charged; the third (`regionsr`) is genuinely refuted but the phase's story of how its upper bound arose is wrong and must be restated (R3), alongside the 1.0224-vs-1.0227 precision fix (R1) and the conservation-sign note (R2). Downgrade applied: none to any verdict; one explanatory clause (R3 provenance) is downgraded from "established" to "not established".
