# P108-3 (FU-P106-2a) — The Force-Alignment Set: Run Record

**Registration:** `../CHECKPOINT108.md` §P108-3 (binding; read in
full before this record was written). This record states the
algebraic signature and all definitions **BEFORE** any alignment-set
computation is run. No new optimisation is registered or performed.

**Corpus (fixed, seven unique configurations).** From
`../../phase101/results/p1015_partB_raw.json`, each on the 56-point
β = 1.1 subset, z = (xi, bc, b2, pi0, shape, p1, p2, mu):

| # | label | source |
|---|-------|--------|
| 1 | A76_mu0 | `direct/A76_mu0` (μ = 0) |
| 2 | B76_mu0 | `direct/B76_mu0` (μ = 0) |
| 3 | runs_A0 | `runs_A[0]` (start 4) |
| 4 | runs_A1 | `runs_A[1]` (start 5) — **identical z to `best_A`** |
| 5 | runs_B0 | `runs_B[0]` (start 5) |
| 6 | runs_B1 | `runs_B[1]` (start 6) — **identical z to `best_B`, the P101-5B hinge best** |
| 7 | runs_B2 | `runs_B[2]` (start 7) |

`best_A` and `best_B` are duplicates of runs entries (z equality
verified character-for-character in the main script and asserted
there); they are read once, as registered — the corpus is seven,
not nine. The hinge best whose subset point 44 motivated this item
is configuration 6 (runs_B1 ≡ best_B).

**Machinery.** Canonical terms from
`../../phase101/work/p1015_lib.py:canonical_terms` (the P106-2
decomposition pattern, `../../phase106/work/p1062_main.py`):
t_kin = □φ, t_pxx, t_FA, t_FB; D_can = Σ|terms| over all four
terms; a point is non-degenerate iff D_can ≥ 1e-9; relative
residual = |Σ terms| / (D_can + 1e-12). float64 throughout;
programme venv. **Reproduction gate (machinery-failure clause):**
for each configuration, the recomputed EoM relative-residual
max/median over non-degenerate points must reproduce the stored
`eom_rel_max_nondeg` / `eom_rel_med_nondeg` within 1e-6 before any
alignment read for that configuration is used; a failure is named
and the verdict is MACHINERY FAILURE.

---

## Algebraic signature (derived here, before computing)

Canonical force terms (p1015_lib): t_FA = F_A / P_X and
t_FB = F_B / P_X, with

  F_A = ½ · H_,φ(φ) · R_bed,        F_B = −μ·φ,

where H_,φ is the φ-derivative of the coupling function H at the
local φ, R_bed is the bed's Ricci scalar at the point, μ is the
configuration's mass parameter, and P_X = p1 + 2·p2·X is shared by
both terms at a point.

**(S1) Sign identity.** Wherever P_X ≠ 0,

  t_FA · t_FB = (F_A · F_B) / P_X²,   and   P_X² > 0,

so **sign(t_FA · t_FB) = sign(F_A · F_B)** wherever P_X ≠ 0. The
common divisor P_X can rescale both force terms but can never
flip their relative sign; same-sign alignment of the canonical
force terms is exactly same-sign alignment of the un-divided
forces. (Where P_X = 0 the canonical guard in `canonical_terms`
sets both terms to 0; such a point fails the live floor below and
cannot enter the set.)

**(S2) Alignment in force variables.** Substituting the force
forms,

  F_A · F_B = −½ · μ · φ · H_,φ(φ) · R_bed,

so the two force terms have the same strict sign at a point iff

  **μ · φ · H_,φ(φ) · R_bed < 0**   (and neither force vanishes).

Alignment is therefore a joint sign condition on four local
quantities: the configuration's μ, the local field value φ, the
local coupling slope H_,φ, and the bed curvature R_bed. It does
not involve p1, p2 (the kinetic-function parameters) except
through the magnitude rescaling 1/|P_X| in the shares.

**(S3) What □φ depends on — and what that implies for shared
kinetic-vanishing points.** In `canonical_terms`, t_kin = □φ =
g^{ab}·(ph)_{ab} where the φ jets (v, H) come from
`wall.phi_jets(pts, pi0, shape)`: the radial profile is
`pi_splines('wallwide', pi0, shape)` and nothing else. The metric
(the β = 1.1 bed) and the 56 subset points are identical for every
corpus configuration. Hence **□φ at every subset point is a
function of (pi0, shape) and the fixed bed only** — the remaining
z components (xi, bc, b2, p1, p2, μ) do not enter □φ at all.
Consequences, stated before computing:

- Two configurations share their entire □φ field (and therefore
  exactly the same kinetic-vanishing points) **iff they have
  identical (pi0, shape)**. Configurations with different
  (pi0, shape) have different □φ fields; a near-zero of □φ in one
  is generically not a near-zero in another.
- In this corpus the (pi0, shape) pairs are: A76_mu0
  (1.0699239865289338, 0.8673536330756604); runs_A0
  (1.0699239834387124, 0.8673536327455258) — the same profile to
  ~3×10⁻⁹, i.e. A76's profile carried into the μ ≠ 0 run, so
  these two share their □φ field to that accuracy but not
  exactly; all other pairs are plainly distinct. The hinge best
  runs_B1 has (pi0, shape) = (0.3385988091052908,
  0.870145941019083), shared with **no** other corpus
  configuration. Point 44's □φ ≈ 0 (t_kin ≈ 2×10⁻⁵⁸ in P106-2)
  is therefore, by construction, a property of that one
  profile; it cannot be inherited by any other corpus
  configuration, and any recurrence of the alignment pattern
  elsewhere would have to arise from an independent near-zero of
  a different □φ field coinciding with force alignment there.

**(S4) Channel-liveness precondition.** If μ = 0 then F_B ≡ 0
everywhere, t_FB ≡ 0, and condition (i) below can never hold: the
alignment set is empty by construction, not by accident. The two
direct rows (A76_mu0, B76_mu0) are exactly this case. The
STRUCTURAL FEATURE verdict's quantifier is therefore read as
registered: over configurations in which both force channels are
live (μ ≠ 0 with the H-force not identically zero, i.e. F_A not
identically zero on the non-degenerate points).

---

## Alignment set (registered definition, primary thresholds)

At a non-degenerate point of a configuration, the point is in the
ALIGNMENT SET iff **all** of:

- (i) both force terms live: |t_FA|, |t_FB| ≥ 1e-6 × max_k|term_k|
  (max over the four canonical terms; the P106 live floor);
- (ii) t_FA and t_FB have the same strict sign (both > 0 or
  both < 0; a zero term fails (i) anyway);
- (iii) combined force share S_F = (|t_FA| + |t_FB|)/D_can ≥ 0.90;
- (iv) kinetic term vanishing in relative form:
  |t_kin|/D_can ≤ 1e-6 (absolute □φ also reported per member).

**Sensitivity grid (registered):** the set is also read at
S_F ∈ {0.80, 0.95} × |t_kin|/D_can ∈ {1e-8, 1e-4} (the live floor
and same-sign conditions held fixed), so the verdict does not ride
on one threshold.

**Per configuration, reported:** set members (subset indices) with
each member's four terms, S_F, |t_kin|/D_can, absolute □φ, and
relative residual; whether the configuration's maximum-residual
(non-degenerate) point is in the set; the set size under the
primary thresholds and under each sensitivity cell; μ; whether
both force channels are live; the (pi0, shape) pair.

**Post-computation anatomy note (appended after the run, marked
post-hoc; the pre-computation text above is unchanged).** The
computation refined (S3)'s expectation in one respect: although
the exact □φ field differs between distinct (pi0, shape) pairs,
the 'wallwide' profile is *flat* — φ ≡ pi0, with spline jets at
the 1e-49–1e-78 level — throughout the inner subset shells
(r ≲ 14.75), for every corpus profile. Kinetic vanishing is
therefore a plateau property shared by all configurations (each
over its own plateau point range), not a point-44 coincidence of
one profile; and t_pxx vanishes on the plateau for the same
reason (it is built from the same φ jets). What discriminates
point 44 within the plateau is the sign condition (S2): R_bed > 0
at plateau points 0–43 and R_bed < 0 at point 44 (and at the
outer points 45–55, where φ varies, t_kin/t_pxx are live and
S_F < 0.90, so they never enter the set). Full anatomy in the
memo.

**Verdicts (only these, per registration):** STRUCTURAL FEATURE /
ISOLATED ACCIDENT / MIXED — SET EXISTS BUT DOES NOT CARRY THE PIN
/ MACHINERY FAILURE, as worded in CHECKPOINT108 §P108-3. C12:
pre-existing walls; no transport claim; this item moves no front
— it characterises the obstruction. INTERNAL ONLY.
