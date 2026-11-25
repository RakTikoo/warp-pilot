# P108-3 (FU-P106-2a) — The Force-Alignment Set: Memo

**Verdict: STRUCTURAL FEATURE.**

The alignment set is nonempty for **every** corpus configuration
in which both force channels are live (5 of 5), and in every such
configuration a set member carries the configuration's maximum
residual — in four of the five, the maximum-residual point is the
*sole* member, and it is the same subset point, **44**. Point 44's
pattern is not an isolated accident of the hinge optimisation; it
recurs across independently optimised configurations, and the
mechanism below shows why it must. No machinery failure: all seven
stored configurations' EoM max/median reproduced within 1e-6
(largest error 8.6×10⁻¹², most exactly 0). Independent checker:
**127 passed, 0 failed** (`work/p1083_checker.py`, recomputing all
sets, residuals and sensitivity cells from the raw corpus with its
own implementation).

## Per-configuration census (primary thresholds)

S_F ≥ 0.90, |t_kin|/D_can ≤ 1e-6, live floor 1e-6, same strict sign.

| config | μ | channels live | set size | members | max-residual pt | max pt in set |
|---|---|---|---|---|---|---|
| A76_mu0 | 0 | no (F_B ≡ 0) | 0 | — | 3 | — (empty by construction) |
| B76_mu0 | 0 | no (F_B ≡ 0) | 0 | — | 14 | — (empty by construction) |
| runs_A0 | −1.500 | yes | 1 | {44} | 44 | **yes — sole member** |
| runs_A1 (= best_A) | −1.079 | yes | 1 | {44} | 44 | **yes — sole member** |
| runs_B0 | +0.0245 | yes | 25 | {19…43} | 22 | **yes** |
| runs_B1 (= best_B, hinge best) | −0.155 | yes | 1 | {44} | 44 | **yes — sole member** |
| runs_B2 | −0.146 | yes | 1 | {44} | 44 | **yes — sole member** |

Duplicates identified, not double-counted: best_A ≡ runs_A[1],
best_B ≡ runs_B[1] (z identical). Corpus = 7 unique of 9 stored.

**Sensitivity:** every set above is *identical* in all eight
sensitivity cells (S_F ∈ {0.80, 0.95} × |t_kin|/D_can ∈ {1e-8,
1e-4}, plus the primary-threshold cross cells). No census number
rides on a threshold: members sit at S_F = 1.000000 and
|t_kin|/D_can ≤ 9×10⁻⁹, far inside every cell boundary.

**Member detail (primary set).** Every member has S_F = 1.000000
and residual_rel = 1.000000 (to float64 print precision). Hinge
best, point 44: t_FA = +0.0034441, t_FB = +0.0429733,
t_kin = +2.0×10⁻⁵⁸, D_can = 0.0464174 — the P106-2 terms
reproduced exactly. (Note on the grounding figure: P106-2's
0.9258 was the *single-term* share |t_FB|/D_can; the registered
combined share S_F = (|t_FA|+|t_FB|)/D_can at point 44 is
1.000000, because t_kin and t_pxx are both negligible there.)
runs_A0 pt 44: t_FA = +0.002350, t_FB = +0.576002. runs_A1 pt 44:
t_FA = +0.001310, t_FB = +0.738901. runs_B2 pt 44: t_FA =
+0.001316, t_FB = +0.016566. runs_B0 members 19–43: both force
terms negative throughout (e.g. pt 22: t_FA = −0.03989,
t_FB = −0.01033), each with residual 1.000000.

## Anatomy — why the set is structural (mechanism, not numerology)

Three facts, all verified in the run, compose the pattern:

1. **The plateau.** The 'wallwide' φ profile is flat — φ ≡ pi0
   with jets at the 1e-49–1e-78 level — over the inner subset
   shells (r ≲ 14.75) for *every* corpus profile. There t_kin =
   □φ ≈ 0 and t_pxx ≈ 0 identically, so D_can ≈ |t_FA| + |t_FB|
   and S_F ≈ 1.000 on the whole plateau. Kinetic vanishing is a
   property of the family's profile form, not of one optimum.
2. **The sign split is in the bed, not the optimiser.** On the
   plateau φ = pi0 > 0 (all corpus configs), so sign(F_B) =
   −sign(μ) is one fixed sign per configuration, and
   sign(F_A) = sign(H_,φ(pi0))·sign(R_bed). R_bed > 0 at plateau
   points 0–43 and **R_bed < 0 at point 44** — point 44 is the
   plateau's only negative-curvature point (the next points,
   45–55, also have R_bed < 0 but lie off the plateau: φ varies,
   t_kin/t_pxx are live, S_F ≤ 0.84, so they never enter the set).
   By the run record's signature (S2), alignment on the plateau
   is exactly μ·H_,φ(pi0)·R_bed < 0.
3. **The two sign regimes both occur in the corpus, and both pin
   the worst residual.** Where H_,φ(pi0) and −μ have opposite
   signs (runs_A0, A1, B1, B2: H_,φ < 0, μ < 0), the plateau's
   aligned point is uniquely point 44, and because aligned terms
   cannot cancel, its residual is exactly ~1 — the maximum.
   Where the signs agree (runs_B0: H_,φ < 0, μ > 0), the forces
   align at *every* plateau point with S_F = 1 (points 19–43;
   points 14–18 fall short on S_F through a not-yet-negligible
   t_pxx), all carrying residual ~1, and point 44 flips to
   opposition (residual 0.624). The μ = 0 direct rows have no
   F_B channel at all — their empty sets are the degenerate case
   of the same algebra (signature S4), outside the verdict's
   quantifier as registered.

**The front's obstruction, in alignment-set form:** on this
family's flat-profile plateau the EoM numerator reduces to
F_A + F_B with nothing else available to cancel it; the bed's
curvature sign pattern guarantees an aligned region (a single
point or the whole plateau, depending on the sign of
μ·H_,φ(pi0)), and at aligned points the relative residual is
pinned at ~1 regardless of parameter magnitudes, because
rescaling (p1, p2, μ, coupling) changes |F_A|, |F_B| but — by
signature (S1) — never their relative sign, which is fixed by
sign(μ·H_,φ(pi0)·R_bed). An optimiser in this family can choose
*which* plateau points are aligned (by choosing the sign regime)
but cannot pose the front with the alignment set empty while
both force channels are live.

**Failure-protocol follow-up (mechanism-suggested, for the
coordinator's queue; not run here):** the only registered-form
escapes the anatomy leaves open are (a) a profile that is *not*
flat on the inner shells, so t_kin/t_pxx are live on the plateau
and can cancel the aligned force sum, or (b) a configuration
with H_,φ(pi0) = 0 exactly, killing the F_A channel on the
plateau. Either would be a new registration, not a re-run of
this item.

C12: pre-existing walls; no transport claim; this item moves no
front — it characterises the obstruction. INTERNAL ONLY.

**Files:** `results/p1083_run_record.md` (signature stated before
computing; one post-hoc anatomy note appended and marked),
`results/p1083_results.json`, `work/p1083_main.py`,
`work/p1083_checker.py` (127/127).
