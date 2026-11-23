# P50-1 — Audit of Procaccia's β = 0.1363 claim

**Worker:** P50-1 · **Date:** 2026-11-22 · **float64 everywhere** · nothing uploaded, no external contact.
**Code:** `../p501_recon.py` (reconstruction), `../p501_audit.py`, `../p501_audit2.py`, `../p501_site2.py`, `../p501_site3.py`.
**Data:** `p501_fidelity.json`, `p501_audit.json`, `p501_audit2.json`, `p501_site2.json`, `p501_site3.json`; logs `p501_*.log`.
**Auditor:** Gate-6 gate-standard auditor (`gate6/wa_auditor.py`, direct-∂² FD, ∂Γ algebraic), validated on the Gate-6 anchor set before use (below). `verify_metric.py` was not used anywhere. Python: programme venv (numpy 2.5.5 / scipy 1.18.1).

## Plain language first

Procaccia's claim is that one specific warp shell — a (10, 20) m shell with a smoothed step density, no radial pressure, and a computer-optimised shift profile — obeys all four classical energy conditions at every speed from 0 up to β = 0.1363, and first breaks them at β = 0.1364.

We rebuilt his shell from what he actually posted (his papers plus his published code and design file — the design file's fingerprint matches the one printed in his papers exactly), and checked it with our own independent auditor. **The design is real and the claim's substance holds up:** wherever our machinery can resolve the design's very sharp features, the shell is legal at β = 0.1363, and at β = 0.1364 our auditor finds his proven failure at his exact point, at almost exactly his proven size (−1.25×10⁻⁷ vs his −1.30×10⁻⁷). That last check matters: it proves our machinery can see the effect his claim turns on.

**Why the verdict is nevertheless "weaker":** our pre-registered bars require the full-volume audit to pass at two fixed grid spacings, h = 0.3 and h = 0.15. His design has a switch only 0.05 m wide — much narrower than either spacing — so at those spacings our auditor's stencil smears the switch and reports artefacts: a negative DEC margin of −3.88×10⁻⁶ at h = 0.3 and 3 non-Type-I points (all at the switch) at h = 0.15. Refining the grid makes every one of these artefacts disappear (at h = 0.075 and 0.0375 the full audit is clean: Type-I fraction 1.0000, worst margin +3.4×10⁻⁷, stable), and point-by-point ladders down to h = 0.0023 converge to positive margins at β = 0.1363 and to his negative value at β = 0.1364. So the claim is confirmed in substance, but it does **not** pass our bars as literally registered — the failing bars and margins are named in the verdict. Nothing here is a discovery; this is an audit of a posted, unrefereed claim, in the programme's locked language: a scan signal that survived independent attack, at weaker-than-registered strength.

## Verdict

**CONFIRMED WEAKER** — the failing bars are Bar 1 and Bar 2 of the Common verdict bars (CHECKPOINT50):

- **Bar 1 (Type-I fraction = 1.000 at every significant audited point): FAILS at the registered spacings.** Shell Type-I fraction 0.9939 at h = 0.3 and 0.9970 at h = 0.15 (β = 0.1363, full fine set). Anatomy: at h = 0.15 exactly **3 significant non-Type-I points, all at r = 16.6 m** — the switch cluster. At h = 0.075 and h = 0.0375 the fraction is **1.0000**.
- **Bar 2 (worst NEC/WEC/SEC/DEC margins > 0 at h = 0.3 AND h = 0.15, sign-stable): FAILS at h = 0.3.** Worst margin at β = 0.1363, h = 0.3 is **DEC −3.882×10⁻⁶ at r = 17.0 m** (negative). At h = 0.15 the worst is +3.528×10⁻⁷ (SEC, r = 5.0), i.e. 65× the measured FD floor (5.4×10⁻⁹) — but the h-pair is not sign-stable, because h = 0.3 does not resolve the 0.05 m switch.
- Bars 3 and 4 pass where the machinery resolves the design: sampled-null NEC agrees in sign with the eigenvalue margins at h = 0.15 (+9.70×10⁻⁸) and at all refined spacings; the second paths (4th-order direct-∂² variant; his own posted tensor pipeline as a discretisation different in kind) agree on the sign of every deciding margin, and on the switch value to ~1.4%.

## Fidelity evidence (registered checks (a)–(c)) — ALL PASS

**(a) Design-vector hash.** The file `x_slp2.npy` was obtained from both figshare archives (DOI 10.6084/m9.figshare.34866243.v1 and 10.6084/m9.figshare.34895667.v1; three copies in the archives: `x_slp2.npy`, `slp2.npy`). SHA-256 of every copy = `a8814dfb6273956da9656379a8dd887218ecc28cbafb03fc87f980c07510d74a` — **exact match** to the published hash. The vector is 14 float64 numbers: 12 spline coefficients aᵢ, then q = 1.47837873 and r_m = 16.79963062 (paper rounds: q = 1.47838, r_m = 16.79963 ✓).

**(b) Quantitative values stated in the papers, reproduced by the reconstruction** (continuum §2 closed form only; targets are the certificates paper's §3 Arb enclosures):

| Quantity | Paper (§3 enclosure) | Reconstruction | Δ |
|---|---|---|---|
| Total mass M | 6.11288573784887775 m | 6.1128857378489 m | 2×10⁻¹⁴ |
| Lapse a(R_in) | −0.58471095644715724 | −0.5847109564396 | 8×10⁻¹² |
| Balance factor λ | 0.27839575423 | 0.27839574685 | 7×10⁻⁹ (rel 3×10⁻⁸) |
| Shift constant k | 0.0302774968097 m⁻² | 0.0302774971489 m⁻² | rel 1×10⁻⁸ |
| ∫F/r² dr | 33.0278294235 m | 33.0278290535 m | rel 1×10⁻⁸ |
| ρ_max (§2) | 2.0204755×10⁻⁴ m⁻² | 2.02047546×10⁻⁴ m⁻² | rel 2×10⁻⁸ |

Independent cross-check against his posted discrete code's own tables: max |ΔS| = 1.11×10⁻⁸, max |ΔS′| = 1.63×10⁻⁸ over r ∈ [3, 27] (his §2 agreement claim for the tables is 1.0×10⁻⁸ for S — consistent). Note: the checkpoint's "M = 6.0 geom" is the nominal design mass; the continuum density of §2 integrates to M = 6.1128857 m, which is what the certificates actually cover. Also noted: the figshare archive as served today (article v3) has SHA-256 a04771e2… for `continuum_cert_code.zip`, differing from the zip hash printed in the paper (62070096…) — a version difference; figshare's own supplied MD5 matches our download, and the load-bearing design-vector hash inside matches exactly.

**(c) β = 0 exact spherical read.** At β = 0 the auditor's eigenvalues were compared with the exact spherical read of the reconstruction's own profiles, (ρ, p_r, p_t) = (ρ(r), 0, rρa′/2) (§4.2 of the paper), at 10 radii × 2 point orientations: in the bulk (ρ > 5×10⁻⁵) ρ relative error ≤ 6.9×10⁻³ at h = 0.3 and ≤ 1.7×10⁻³ at h = 0.15 with clean h² scaling; principal-pressure absolute error ≤ 2.30×10⁻⁷ (h = 0.3), ≤ 5.78×10⁻⁸ (h = 0.15); Type-I at every anchor point. In the fringe (ρ → 0 at the support edges) relative ρ errors grow (up to 26% at r = 26.18 where ρ = 6.8×10⁻⁸) while absolute errors stay ≤ ~3×10⁻⁷ — this is the FD floor of a C³ piecewise-quartic design, and it is the same floor that drives the Bar 1/2 failures below. Fidelity is established: the reconstruction is his geometry, and the auditor reads it correctly where it is resolved.

**Auditor anchors (Gate-6 set, run first):** Minkowski max|G| = 0.0 exactly; static exact anchor ρ rel. err. 3.07×10⁻³ at h = 0.3 (Gate-6: ≤ 3.1×10⁻³); Finalist A whole-volume worst **+2.141×10⁻⁷**, Type-I **1.000** (Gate-6: +2.14×10⁻⁷, 1.000). Pass.

**Reconstruction scope / gaps:** none material. Every §2 quantity is determined by the posted material: density (exact Δr, R₁, R₂, W, ρ₀ from §2/§3), zero-radial-pressure background (a′ = m/(r(r−2m)), B = (1−2m/r)⁻¹), source (q, r_m, w = 0.05 from §2; the 12 aᵢ from the hashed design vector; the cubic B-spline knot construction — knots [3,3,3, linspace(3,27,10), 27,27,27], constant extension — from the posted code `opt_surrogate.Design`, matching §3's stated knots 3, 5.667, …, 27), balance λ and shift constant k by the §2 integrals. The one textual wrinkle: §2's printed tanh argument is garbled in the academia.edu text extraction ("tanh(r_m r/w)"); the posted code (`opt_core.matched_source`, `opt_surrogate.Design` docstring) gives tanh((r_m − r)/w), which is also the only reading consistent with the §3 λ enclosure — used, and it reproduces λ to 3×10⁻⁸.

## Audit ledger (gate-standard auditor; full fine set for (10,20) + edge/switch clusters, 1,352 pts)

Shell region = support [R_in, R_out] = [2.734, 27.265] m. Worst = min over NEC/WEC/SEC/DEC.

| β | h | Worst margin (shell) | Binding | Type-I (shell) | Sampled-null NEC min |
|---|---|---|---|---|---|
| 0.10 | 0.3 | −2.397×10⁻⁷ | DEC @ r = 26.0 | 1.000 | −5.69×10⁻⁸ |
| 0.10 | 0.15 | **+6.567×10⁻⁷** | DEC @ r = 25.0 | 1.000 | +4.97×10⁻⁷ |
| 0.1363 | 0.3 | −3.882×10⁻⁶ | DEC @ r = 17.0 | 0.9939 | −1.48×10⁻⁶ |
| 0.1363 | 0.15 | **+3.528×10⁻⁷** | SEC @ r = 5.0 | 0.9970 | +9.70×10⁻⁸ |
| 0.1363 | 0.075 | **+3.429×10⁻⁷** | SEC @ r = 5.0 | **1.0000** | +9.21×10⁻⁸ |
| 0.1363 | 0.0375 | **+3.404×10⁻⁷** | SEC @ r = 5.0 | **1.0000** | +9.00×10⁻⁸ |
| 0.1364 | 0.3 | −4.558×10⁻⁶ | DEC @ r = 17.0 | 0.992 | −1.62×10⁻⁶ |
| 0.1364 | 0.15 | +3.511×10⁻⁷ | SEC @ r = 5.0 | 0.9970 | +9.59×10⁻⁸ |
| 0.1364 | 0.075 / 0.0375 | +3.41×10⁻⁷ / +3.39×10⁻⁷ | SEC @ r = 5.0 | 1.0000 | +9.1×10⁻⁸ / +8.9×10⁻⁸ |

The β = 0.1364 fine-set rows pass because the 26-direction fine set does not land on the exact failure point; the failure is a point event at (r = 16.635 m, θ = 90°), read site-specifically below — exactly as registered.

**Deciding site (r = 16.635 m, θ = 90°, point (0, 16.635, 0)) — h-ladder, 2nd-order auditor:**

| β | h = 0.3 | 0.15 | 0.075 | 0.0375 | 0.01875 | 0.009375 | 0.0046875 | 0.00234375 | continuum read |
|---|---|---|---|---|---|---|---|---|---|
| 0.1363 NEC | +1.534×10⁻⁴ | +6.034×10⁻⁵ | +2.066×10⁻⁵ | +1.007×10⁻⁵ | +6.297×10⁻⁶ | +5.026×10⁻⁶ | +4.660×10⁻⁶ | +4.565×10⁻⁶ | ≈ **+4.5×10⁻⁶** (positive) |
| 0.1364 NEC | +1.533×10⁻⁴ | +5.979×10⁻⁵ | +1.885×10⁻⁵ | +5.435×10⁻⁶ | non-Type-I | non-Type-I | non-Type-I | non-Type-I | **violated** |

**Registered machinery cross-check at β = 0.1364 — PASS.** At the finest spacings the tensor at his point is non-Type-I (complex eigenvalue pair), i.e. NEC/DEC violated, in both our auditor and his own posted tensor pipeline. The frame-invariant minimum null contraction there is **−1.245×10⁻⁷** (h = 0.0046875) / −1.267×10⁻⁷ (branch ladder), against his interval-proven **−1.30135×10⁻⁷** — agreement to ~4%. We see his failure, at his point, at his magnitude. A pass at 0.1363 is therefore creditable on machinery grounds; its weakness is only against the registered h-pair bars above.

**Second paths.** (i) His posted tensor pipeline (`fringe_exact.radial` + `tensor_fast.F`, analytic-formula tensor on his discrete tables — a discretisation different in kind from our FD-on-continuum) at the switch point, β = 0.1363: NEC **+4.534×10⁻⁶**, vs our FD continuum limit ≈ +4.5×10⁻⁶ (agreement ~1.4%); at β = 0.1364 it is likewise non-Type-I. (ii) 4th-order direct-∂² variant (`wa_diag` pattern) on the full fine set at h = 0.3, β = 0.1363: worst **+3.389×10⁻⁷** (SEC @ r = 5.0), agreeing in sign with the refined 2nd-order reads (its Type-I fraction 0.9757 at h = 0.3 is its wider stencil meeting the same switch). (iii) Equator scan (θ = 90°, r step 0.05, h = 0.009375): β = 0.1363 — no non-Type-I points, no significant negative margins; β = 0.1364 — 21 non-Type-I points. Branch ladders at his five active branches (8.64, 12.63, 16.635, 21.98, 26.18 m, equator, finest h): all Type-I and NEC-positive at β = 0.1363 (NEC +1.26×10⁻⁵, +2.78×10⁻⁵, +4.57×10⁻⁶, +1.06×10⁻⁶, +2.0×10⁻⁹ respectively — the fringe branch at 26.18 m is positive but tiny, as expected where T → 0); at β = 0.1364 the switch, 21.98 m and 26.18 m branches are non-Type-I (min-null −1.27×10⁻⁷, −2.15×10⁻⁸, −3.4×10⁻¹¹).

**Anatomy of the Bar 1/2 failures (failure protocol).** Binding feature: the tanh switch of width w = 0.05 m at r_m = 16.80 m and the C³ density breakpoints. An FD stencil of width h ≫ w averages S″ across the switch, producing spurious DEC/NEC dips of size ~10⁻⁶–10⁻⁵ at h = 0.3 that shrink monotonically (switch-site NEC error: 1.5×10⁻⁴ → 4.6×10⁻⁶ over h = 0.3 → 0.0023) and vanish by h = 0.075 on the full set. This is a machinery-resolution failure, not a design failure: the same auditor at the same spacings passes our smoother Gate-6 shell, whose features are ~100× wider. **Follow-up (mechanism-suggested, partially executed in-item):** the ladders, Richardson reads and second paths above are the executed follow-up; what remains to lift this verdict to CONFIRMED AT OUR BARS is a full fine-set audit whose stencil resolves the switch — either re-registering the h-pair for this design at h ≤ 0.0375 (where this audit already reads Type-I 1.0000 and worst +3.40×10⁻⁷, stable between 0.075 and 0.0375), or an analytic-tensor auditor built on the continuum profiles over the full fine set. Reopening/strengthening condition: either of those, run as a verdict path, passing Bars 1–4 as written for its spacings. The β = 0.10 row shows the same artefact class (h = 0.3 DEC −2.40×10⁻⁷ at the r = 26 fringe; fully legal at h = 0.15, Type-I 1.000, worst +6.57×10⁻⁷), so the weakness is not specific to the top amplitude.

## C12 accounting

This row is a **prescribed-geometry audit**: the stress tensor audited is the one the metric implies through the Einstein equations, and conservation is automatic (Bianchi) — the same standard as Fuchs / Phase 26 / Gate-6, and the same scope Procaccia states in his own paper ("They say nothing about a matter model that could source it, about stability, or about acceleration"). **No matter model, formation route, or stability is claimed, by him or by us.** Le (arXiv:2605.25417)'s stricter source-consistency standard is carried as a standing caveat, not a bar. Language: hedges intact; the β = 0.1363 row is a scan signal that survived independent attack at weaker-than-registered strength — not a discovery, and not a programme result: it is Procaccia's design, audited.

## Source log (all retrieved 2026-11-22)

1. F. Procaccia, "Continuum Energy-Condition Certificates for an Optimized Positive-Energy Warp Shell" (posted Oct 30, 2026, academia.edu, unrefereed) — full text read via the academia.edu page https://www.academia.edu/180109147/Continuum_Energy_Condition_Certificates_for_an_Optimized_Positive_Energy_Warp_Shell (§§1–8, incl. §2 geometry, §3 enclosures, §6 violation values, code-availability hashes).
2. Scivora mirror abstracts: "Code and cell logs for Continuum Energy-Condition Certificates…" (DOI 10.6084/m9.figshare.34895667.v1; design hash stated) and "Supplementary code for Numerical Optimization of Shift Profiles for Positive-Energy Warp Shells" (DOI 10.6084/m9.figshare.34866243.v1; archive contents stated) — via scivora.io article pages returned by search.
3. Figshare article records (API) for 34866243 and 34895667: file lists, download URLs, supplied MD5s.
4. Downloaded archives (in `../procaccia/`): `optimal_shift_code.zip` (514,062 B; MD5 fd920f0911b0687b736260fef7201c82 = figshare supplied MD5 ✓) and `continuum_cert_code.zip` (7,998,253 B; MD5 f18b7190b047526603f902edef5b74ca = figshare supplied MD5 ✓). Design vectors, posted code (`opt_core.py`, `opt_surrogate.py`, `tensor_fast`/`fringe_exact`, `violation.json`, `radial_vs_reference.json`) read from these archives.
5. The companion optimisation paper itself ("Numerical Optimization of Shift Profiles for Positive-Energy Warp Shells") was **not** retrieved as a full text — only its scivora abstract and its posted code archive (which states it reproduces every number in that paper). Named gap, non-material: the certificates paper §2/§3 + the hashed design vector + the posted code determine the geometry completely, and fidelity (a)–(c) all pass without it.
