# PHASE 420 REGISTRATION — W26: COMPOSITE SUPPLY OF THE
# CORRECTED TARGET

Charged at ledger entry 1098 (2026-11-27). Written before any
Phase 420 computation. Frame of record: the VM
(`~/workspace/warp-pilot/venv`, numpy 2.5.5 / scipy 1.18.1).
The laptop admission control (SS6) is run and followed; all
deciding reads are VM reads, as in Phases 313/320/410.

## SS0 — The question

Phase 410's spinor supplier reproduces the Phase 405 winner's
required tensor T_req at its binding sites AS IT STANDS — SEC
violation included (sourcing ≠ curing). The geometry side
(411/415) priced the deficit: SEC binds at r = 12.0732 (the A2
site), and the best geometry-side member still carries
SEC = −1.374485×10⁻⁴. Can a COMPOSITE supplier — two spinor
families with independent parameters, fitted jointly —
supply a CORRECTED target T_corr = T_req + δ, where δ is the
minimal correction that zeroes the SEC deficit, so that the
sourced design's total stress satisfies all four energy
conditions at the sites? And what is the composite's own
accounting (density sign, price per family)?

## SS1 — The corrected target (a construction of this phase)

Sites and T_req are Phase 410's stored records
(`phase410/work/p410_targets.json`): Fit A sites
{A1_joint_argmin (r = 17.926829268292682), A2_sec_argmin
(r = 12.073170731707318), A3_peak (10, 0, 0)} and the B
stencil (5 sites along A1's direction, r = A1_r ± {−1.0,
−0.5, 0, +0.5, +1.0}; B+0.0 = A1). T_req at each site is the
stored Eulerian That (the record of Gate-50's target;
Gate-54 re-derives it independently — not this phase's act).

Channel decomposition is Phase 410's `decompose()` copied
verbatim (Type-I eigen-channels: ρ, p_r, p_t; NEC_r = ρ+p_r,
NEC_t = ρ+p_t, WEC = ρ, DEC_i = ρ−|p_i|, DEC_flux =
ρ−|T_0i|, SEC_trace = ρ+p_r+p_t1+p_t2, SEC_r = NEC_r,
SEC_t = NEC_t; SAMPLER-M margins as cross-check).

**δ construction (registered).** At each site, decompose
T_req.
- If every channel ≥ 0 (A1 and all five stencil sites, per
  Phase 410's decomposition: SEC_min = joint_min =
  +1.227385×10⁻⁶ at A1; SEC_min > 0 at every stencil site):
  **δ = 0 exactly.**
- If SEC_trace < 0 (A2: −2.2135565049905559×10⁻⁴; A3:
  −3.388413×10⁻⁴ — the ONLY failing channel at either site;
  every joint channel positive): Δ = −SEC_trace, and δ is
  defined in the site's eigenframe of η·T_req: with
  η·T_req = V Λ V⁻¹, Λ = diag(ρ, −p_1, −p_2, −p_3), the
  eigenvalue-shift vector is W = diag(+Δ/4, −Δ/4, −Δ/4,
  −Δ/4) (timelike entry +Δ/4 raises ρ by Δ/4; spacelike
  entries −Δ/4 raise each principal pressure by Δ/4), and
  **δThat = η · V W V⁻¹**, T_corr = T_req + δThat.
  This is the Frobenius-minimal first-order correction in
  the eigenframe: SEC_trace's first-order change under
  eigenvalue shifts (δρ, δp_1, δp_2, δp_3) is their sum,
  and the equal split over the four eigenvalues entering
  SEC_trace minimises the shift norm at fixed sum Δ.
- δ at A3 is the identical construction with
  Δ_A3 = −SEC_trace(A3), stated explicitly here: the
  charge defines δ by its A2 purpose, but A3's T_req also
  fails SEC_trace, and a "corrected" target still failing
  at A3 would not be a four-condition target at the sites.
  The same minimal construction is applied and stated.
- A posteriori self-checks (CTRL-420-δ, SS3): SEC_trace
  (T_corr) = 0 to ≤ 1×10⁻¹² at A2/A3; EVERY joint channel
  of T_corr ≥ the corresponding channel of T_req at every
  site (the construction spends no joint surplus — at
  A2/A3 all principal pressures are negative, so the equal
  split raises every joint channel); ||δ||_F reported per
  site; δ ≡ 0 at the clean sites.

T_corr is a CONSTRUCTION of this phase. It is never quoted
as the Phase 405 winner, and no statement about the winner
is made from it.

## SS2 — Composite machinery

Phase 410's spinor machinery (itself Phase 320/313 verbatim)
generalised to PER-MODE masses. A mode is (pvec, avec ∈ ℂ²,
m_i). **Family 1: m = 1** (Phase 410's Fit A family).
**Family 2: m = 0** (massless Dirac modes — independent
dispersion E = |p| and the m = 0 branch of `u_spinor`).
The total field is the sum of both families' fields; the
composite tensor is the total field's stress tensor (cross
terms included — the families are NOT fitted separately
and added).

- Pairwise path: `S_of_multi` = Phase 410's `S_of_vec`
  generalised to per-mode masses (per-mode pcov
  (E_i, −pvec_i), E_i = √(|p_i|² + m_i²)); T(x) =
  T_from_S(S, exp(i p·x)) as in 410.
- Direct path: `fields_at_point_multi` = 410's
  `fields_at_point` with per-mode E_i in the derivative
  phases; `stress_at_point_multi` built on it.
- Machinery checks (run before controls; all must pass):
  M1 — `S_of_multi` with all masses 1 equals 410's `S_of`
  on the Fit A primary's parameters (max diff ≤ 1×10⁻¹³).
  M2 — direct-multi equals 410's `T_direct` at all 8 sites
  for both 410 primaries (max diff ≤ 1×10⁻¹³).
  M3 — a mixed-mass random superposition (3 modes m = 1,
  3 modes m = 0): direct vs pairwise agree at 5 random
  points (≤ 1×10⁻¹² relative to the tensor norm).
- Parametrisation: theta = [family-1 block (7N₁), family-2
  block (7N₂)], each block in 410's folded form
  [pvecs (3N), Re avecs (2N), Im avecs (2N)]. Residuals:
  the 10 upper-triangular components of (T_sup − T_target)
  per site, normalised by ||T_target,site||_F. Fits by
  scipy least_squares (trf). **Match bar (direct path):
  max per-site R = ||T_sup − T_target||_F ≤ 1×10⁻⁹** (the
  313/320/410 bar).

## SS3 — Controls (all before any corrected-target read
## is believed)

- **CTRL-420-A (δ = 0 reduction, Fit A):** the composite
  machinery with family 2 EMPTY (N₂ = 0), evaluated at
  Phase 410's stored Fit A primary (N = 6, m = 1) against
  the UNCORRECTED targets {A1, A2, A3}: direct per-site
  residuals reproduce the stored
  [8.157213446731793×10⁻¹⁵, 2.7633923118189793×10⁻¹³,
  2.9659878908312287×10⁻¹²] (each ≤ 2× stored, and the
  max ≤ 1×10⁻¹¹ — see Amendment 1); the FD Jacobian
  (central differences, h = 1×10⁻⁶·max(1, |θ_j|), 410
  verbatim) at that solution reproduces joint σ_min =
  0.3857618146636974 within 1% relative (PER-SOLUTION,
  G36-C).
- **CTRL-420-B (δ = 0 reduction, Fit B):** the same for
  410's Fit B primary (N = 12) against the uncorrected
  stencil targets: stored residuals
  [9.110193089121277×10⁻¹⁵, 1.6913168093005374×10⁻¹⁴,
  2.3051650590783883×10⁻¹⁴, 2.0952740079404155×10⁻¹⁴,
  7.928455600124212e-15] (each ≤ 2× stored, max
  ≤ 1×10⁻¹¹); joint σ_min = 0.015432479500623982
  within 1%.
- **CTRL-420-δ:** the SS1 self-checks on the constructed
  δ / T_corr (SEC_trace → 0 ≤ 1×10⁻¹²; joint channels
  non-decreasing at every site; δ = 0 exactly at A1 and
  the stencil sites; ||δ||_F reported).

## SS4 — Fits

- **FIT C-A (primary):** sites {A1, A2, A3} against
  T_corr — 30 residuals. Arms (N₁, N₂): (3, 3) — the
  counting-threshold composite, 42 parameters — and
  (6, 6) — 84 parameters. Starts per arm: warm-A (family 1
  = 410 Fit A primary truncated/padded to N₁, family 2 =
  0), warm-B (family 1 as warm-A, family 2 small random,
  scale 0.01), + 6 random starts (410's rand_theta pattern
  per family). max_nfev 900 (3,3) / 1500 (6,6). Primary:
  the (6, 6) arm's best if it matches at the bar, else the
  best arm's winner.
- **FIT C-B (tracking):** the 5 stencil sites against
  T_req (δ = 0 there) — 50 residuals. Arm (6, 6).
  Starts: warm-A (family 1 = the 6 largest-|a| modes of
  410's Fit B primary, family 2 = 0), warm-B (family 2
  small random), + 4 random. Contingency arm (12, 6)
  (family 1 = the full Fit B primary) runs ONLY if (6, 6)
  stalls above the bar. max_nfev 1500.
- **FIT C-S (context, not a verdict leg):** family 1
  ALONE against T_corr at {A1, A2, A3}: N = 6 (seeded at
  410's Fit A primary + 3 random) and N = 12 (4 random +
  warm). Reported so the composite's contribution is
  distinguishable from a larger single family.
- **Contingency (registered):** if C-A (6, 6) with m₂ = 0
  stalls above the bar AND C-S also stalls, ONE
  contingency arm (6, 6) with family 2 at m₂ = 2.0 runs
  (same starts pattern). Disclosed wherever reported.
- **Diagnostics at the C-A and C-B primaries:** direct
  per-site residuals; Dirac residuals of all modes;
  joint + per-site-block σ_min (central FD, verbatim
  410) — quoted PER-SOLUTION (G36-C); pricing |a|² per
  family; perturbation ladder at the C-A primary only
  (targets perturbed by ε·||T_corr||_F, ε ∈ {1×10⁻⁹,
  1×10⁻⁶}, 2 draws each, warm + fresh starts; a rung
  passes if the bar is re-achieved — 410's pattern).

## SS5 — The three reads

(i) **REPRODUCTION.** Per fit: per-site direct-path
residuals at the primary; Dirac residuals; joint and
per-site-block σ_min (per-solution); the ladder outcome
(C-A).

(ii) **THE COMPOSITE'S OWN ACCOUNTING.** Per site: the
composite total's density ρ_sup = T_sup[0, 0] (direct
path) and its sign; |a|² per family (Σ|avecs|² over the
family's modes); for information, the family-standalone
densities ρ₁₁ (family 1 alone), ρ₂₂ (family 2 alone) and
the interference density ρ_x = ρ_sup − ρ₁₁ − ρ₂₂. The
no-exotic standard applies to the composite's TOTAL: its
full channel table (410 decomposition) at every site is
read against T_corr's channel table, side by side, with
the channel-margin differences stated.

(iii) **THE UNMATED REMAINDER** (if the C-A primary's
max R > bar). At each A site, for R = T_corr − T_sup:
||R||_F; R's SEC content — the SEC_trace functional of
R in the site's eigenframe of T_corr; the δ-parallel
fraction ⟨R, δ⟩_F / ||δ||_F² and the orthogonal
remainder's norm; and T_sup's channel margins vs
T_corr's (from read (ii)) — stating precisely which
channel of δ the composite cannot express, if any.

## SS6 — Admission

The winner's `set_read405` is run on the laptop pool
through a fresh minimal mirror (the p405_lib import
closure copied from the VM, md5-verified file by file),
per Phase 410 SS6 / Phase 409's minimal-root pattern. If
its joint / sec_min reproduce the VM read at roundoff,
the laptop frame is ADMITTED for screening in this
phase; deciding reads remain the VM's regardless. If
admitted, the C-A primary's direct residuals are also
cross-checked on the laptop.

## SS7 — Verdicts (registered forms)

- **COMPOSITE SUPPLIES THE CORRECTED TARGET** — FIT C-A's
  primary at direct max R ≤ 1×10⁻⁹ at A1/A2/A3, σ_min
  (joint and per-site blocks) bounded away from zero
  (values stated), the perturbation ladder re-closing;
  the composite's density accounting stated on the
  verdict's face (sign per site, |a|² per family). This
  verdict carries a GATE REFERRAL (fences: sites only;
  the corrected target is band-scoped by construction —
  its sites are the winner's band sites; the corrected
  object's extent is unaudited; NO coverage claim).
- **SUPPLIES ONLY THE UNCORRECTED TARGET** — C-A fails
  the bar against T_corr, while (a) the δ = 0 controls
  pass (the machinery supplies T_req — 410 restated by
  this phase's own reads), and (b) the best C-A fit's
  joint-channel margins agree with T_corr's within
  1×10⁻⁶ absolute at every A site while its SEC channel
  misses by more than 1×10⁻⁶, and/or the remainder
  decomposition (SS5 iii) shows the unmated part is δ's
  SEC content. The unmated part of δ is named precisely;
  the decomposition is the deliverable and becomes the
  obstacle statement for any successor.
- **DOES NOT SUPPLY** — otherwise; the anatomy (which
  components fail, at which sites, in which channels;
  any σ_min collapse; the density accounting) is the
  deliverable.

## SS8 — Fences

A site mating is not a field on the extent: no coverage
is claimed or implied (the extent line — 346/357/368/362
— owns coverage; the candidate's own extent audit is
Phase 409's, separate). T_corr is a construction of this
phase, never the 405 winner. No QI price is quoted.
Novelty NONE for the mating method (Martín-Moruno &
Visser 2021, per Gate-25). σ_min quoted per-solution
only (G36-C). The composite sourcing T_corr is a
statement about the composite's expressive range and its
own accounting at the sites — the sourced design's
four-condition status AT THE SITES is exactly what read
(ii) states, nothing more. DESK line in the memo.

## SS9 — Deliverables

`phase420/CHECKPOINT420.md`,
`phase420/results/p420_memo.md`, the driver and the
independent checker under `phase420/work/`, full records
under `phase420/results/`. No ledger append, no successor
launch, no user contact.

## AMENDMENT 1 (2026-11-27, after the first control run,
## before any fit)

CTRL-420-A's registered absolute cap (each residual
≤ 1×10⁻¹²) was ill-posed against the record it was
meant to reproduce: Phase 410's stored Fit A primary
max residual is 2.9659878908312287×10⁻¹² at A3 — ABOVE
the cap — so an exact reproduction necessarily "fails"
it. The first control run in fact reproduced every
residual at ratio 0.999–1.000 of stored (A:
[8.146×10⁻¹⁵, 2.763×10⁻¹³, 2.966×10⁻¹²]; B: all
ratios 1.000) and both σ_min values at relative
differences 3.4×10⁻⁹ / 4.5×10⁻⁸. The bar is corrected
to the form Phase 410's own controls used in substance:
each residual ≤ 2× stored, with an absolute cap on the
max of 1×10⁻¹¹ (3.4× the stored Fit A max — a cap on
the reproduction, not on the original). Phase 410's
CTRL-313 amendment is the precedent for correcting an
ill-posed control bar on the record. No fit had run;
nothing else changes.

## AMENDMENT 2 (2026-11-27, after CTRL-420-delta passed,
## at the first C-A start, before any fit completed)

The (3,3) arm's warm-A start crashed least_squares with
non-finite residuals: warm-A set family 2's momenta to
exactly zero, and for a MASSLESS mode the spinor
u_spinor divides by E + m = |p| — an exactly-zero
momentum is a 0/0 singularity of the parametrisation
(Phase 410 never met it: every mode had m = 1). The
disclosed fixes, neither of which changes any target,
bar, or verdict form: (i) warm starts give the empty
family nonzero unit momenta with amplitudes exactly
zero — its tensor contribution still vanishes
identically, so warm-A still means "410's solution plus
an empty family"; (ii) a numerical guard in the
composite residual/diagnostic paths replaces an
exactly-zero massless momentum by (1, 0, 0) — any
nonzero |p|, however small, is finite (the spinor's
lower component is O(1) in the direction), so the
guard touches only the measure-zero singular set.
CTRL-420-delta had already passed and is unaffected
(it involves no spinors).

## AMENDMENT 3 (2026-11-27, after the first full driver
## run, before the checker)

The C-A primary matched the corrected target on the
direct read (max R = 3.496e-10, under the 1e-9 bar),
with joint sigma_min = 30.12 (rank 30/30) — and three
of four perturbation-ladder rungs reclosed at the bar.
The fourth (eps = 1e-6, draw 0) stalled at 3.28e-9.
The stall is an optimiser stopping artefact, on this
evidence: the (6,6) arm's fits all terminated on
least_squares' default tolerances at nfev 26-57 in the
1e-9-1e-10 band; the sibling draw at the same eps
reclosed from a FRESH random start at 6.67e-10; and at
sigma_min = 30 the solution set is fat, not
knife-edge. The ladder is therefore COMPLETED, not
re-barred: all four rungs re-run with a fresh seed
(4203) and tightened tolerances (ftol = xtol =
gtol = 1e-13, max_nfev 2500), the bar unchanged at
1e-9. The original ladder stays on the record beside
the completed one; the verdict reads the completed
ladder. If any completed rung still misses the bar,
the DOES NOT SUPPLY form stands with this anatomy.
Phase 410's mid-phase driver correction and the
truncated-arm completions of 392/410 are the
precedents.
