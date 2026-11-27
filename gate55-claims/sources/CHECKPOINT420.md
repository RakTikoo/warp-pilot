# CHECKPOINT 420 — W26: COMPOSITE SUPPLY OF THE CORRECTED TARGET

**Verdict: COMPOSITE SUPPLIES THE CORRECTED TARGET —
GATE REFERRAL.** A composite of two spinor families
(the m = 1 family of Phase 410's Fit A + a massless
m = 0 family), fitted jointly, supplies the corrected
target T_corr = T_req + δ at Phase 410's sites: direct
max residual 3.496×10⁻¹⁰ at the registered 1×10⁻⁹ bar,
joint σ_min = 30.12 (rank 30/30, PER-SOLUTION per
G36-C), the perturbation ladder reclosed on its
completed form, and the composite's TOTAL tensor is
four-condition-clean at the sites with positive
density throughout. Phase 410 sourced the winner AS
IT STANDS, SEC violation included; this phase's
supplier sources the SEC-corrected tensor instead.
Fences in §7 — sites only, the corrected target is
this phase's construction, its extent unaudited, NO
coverage claim, novelty NONE.

Registration: `phase420/work/p420_registration.md`
(SS0–SS9, written before any computation; Amendments
1–3 appended on the record, §8 below). Driver:
`phase420/work/p420_run.py`; machinery:
`phase420/work/p420_machinery.py` (Phase 410's block
verbatim + the per-mode-mass generalisation).
Checker: `phase420/work/p420_check.py` — ALL PASS.
Admission: laptop ADMITTED (§6). Frame of record:
the programme venv on this VM (numpy 2.5.5 /
scipy 1.18.1, the Phase 166 pin).

## 1. The corrected target (SS1)

δ is built per site in the eigenframe of η·T_req:
where SEC_trace < 0, Δ = −SEC_trace is split equally
over the four eigenvalues entering SEC_trace
(+Δ/4 on ρ, +Δ/4 on each principal pressure); δ = 0
exactly at sites already four-condition-clean. At
both corrected sites every principal pressure of
T_req is negative, so the shift spends no joint
surplus — every joint channel of T_corr is ≥ T_req's,
channel by channel (CTRL-420-δ, PASS):

| site | Δ | ‖δ‖_F | SEC_trace: req → corr | joint_min: req → corr |
|---|---|---|---|---|
| A1 (r = 17.9268) | 0 (δ ≡ 0) | 0 | +2.794×10⁻⁵ | +1.227×10⁻⁶ → same |
| A2 (r = 12.0732) | 2.213557×10⁻⁴ | 1.231×10⁻⁴ | −2.213557×10⁻⁴ → +1.1×10⁻¹⁹ | +1.385×10⁻⁴ → +2.491×10⁻⁴ |
| A3 (r = 10, peak) | 3.388413×10⁻⁴ | 1.695×10⁻⁴ | −3.388413×10⁻⁴ → 0.0 | +8.805×10⁻⁴ → +1.050×10⁻³ |
| B stencil (×5) | 0 (δ ≡ 0) | 0 | ≥ +8.9×10⁻⁶ | unchanged |

T_corr is a CONSTRUCTION of this phase (SS8): a
site-wise corrected tensor, not a geometry, never
the 405 winner.

## 2. Controls (SS3) — all PASS

Machinery checks: M1 S_of_multi ≡ S_of at a single
mass, max diff 6.99×10⁻¹⁸; M2 direct paths identical,
0.0; M3 mixed-mass direct-vs-pairwise, 1.21×10⁻¹⁵
relative. CTRL-420-A (family 2 empty at 410's Fit A
primary, uncorrected targets): residuals reproduce
stored at ratios 0.999–1.000 (max 2.966×10⁻¹²);
σ_min 0.3857618 vs stored 0.3857618146636974 (rel
3.4×10⁻⁹). CTRL-420-B (Fit B primary, stencil):
residuals at ratio 1.000 (max 2.305×10⁻¹⁴); σ_min
0.01543248 vs stored 0.015432479500623982 (rel
4.5×10⁻⁸). The composite machinery reduces to the
single-family mating at δ = 0, as charged. The
checker's independent spot checks agree.

## 3. Read (i) — reproduction against T_corr

FIT C-A (primary arm (6,6), warm-A start; stored
`phase420/work/p420_fitCA_primary.json`): direct
residuals per site [4.057×10⁻¹², 7.640×10⁻¹²,
3.496×10⁻¹⁰], max 3.496×10⁻¹⁰ ≤ bar 1×10⁻⁹. Joint
Jacobian σ_min = 30.12132520557749 (per-solution,
G36-C), rank 30/30 at the 1×10⁻¹⁰ relative
tolerance; per-site blocks 309.28 / 118.50 / 50.94;
Dirac residual 5.28×10⁻¹⁷. The (3,3) counting arm
matched deeper (best 9.573×10⁻¹³; all eight starts
≤ 2.77×10⁻¹¹). The registered contingency (family 2
at m₂ = 2.0) never triggered.

Perturbation ladder: the original run reclosed at
ε = 10⁻⁹ (3.497×10⁻¹⁰, 3.487×10⁻¹⁰) and at
ε = 10⁻⁶ draw 1 (6.667×10⁻¹⁰), but draw 0 stalled at
3.282×10⁻⁹ — an optimiser stopping artefact
(Amendment 3: the arm's fits all terminated on
default tolerances in the 1×10⁻⁹–1×10⁻¹⁰ band, and
the sibling draw reclosed from a fresh start). The
completed ladder (fresh seed, tolerances 1×10⁻¹³,
bar unchanged) recloses everywhere at
[1.210×10⁻¹⁴, 7.478×10⁻¹⁵; 1.278×10⁻¹⁴,
2.298×10⁻¹⁶] (`p420_ladder_completed.json`). The
match is not a knife-edge: at σ_min = 30 the
solution set is fat.

FIT C-B (tracking, δ = 0 stencil): primary (6,6)
direct max R = 3.565×10⁻¹⁵, σ_min = 0.011390
(per-solution), rank 50/50 — the composite tracks
T_req along the whole radial stencil, as 410's
single family did, now with both families active.

## 4. Read (ii) — the composite's own accounting

Pricing |a|² (410's convention): family 1 (m = 1)
0.029172052178672605; family 2 (m = 0)
2.036×10⁻⁶; total 0.029174 — against 410 Fit A's
0.029266 for the UNCORRECTED target: the corrected
target is supplied at essentially the same price.
Supplier density ρ_sup (the composite TOTAL, direct
path) is POSITIVE at every site, and the total's
four-condition status at the sites is:

| site | ρ_sup | joint_min | SEC_trace | SEC_min |
|---|---|---|---|---|
| A1 | +1.238137×10⁻⁴ | +1.227×10⁻⁶ | +2.794×10⁻⁵ | +1.227×10⁻⁶ |
| A2 | +4.431937×10⁻⁴ | +2.491×10⁻⁴ | +2.7×10⁻¹² | +2.7×10⁻¹² |
| A3 | +1.944243×10⁻³ | +1.050×10⁻³ | +2.3×10⁻¹⁰ | +2.3×10⁻¹⁰ |

Every channel of the supplied tensor is ≥ 0 at all
three sites: the sourced corrected object is
four-condition-clean AT THE SITES, its binding
margin A1's pre-existing joint +1.227×10⁻⁶ (where
δ = 0). Density split (information): at A2,
family 1 alone +5.934×10⁻⁴, family 2 alone
+2.761×10⁻⁶, interference −1.389×10⁻⁴ — δ is
carried mostly by re-arrangement of family 1 and
the interference term; the massless family's direct
share is small at the A sites. On the stencil
(C-B) its share is substantial (|a|²₂ = 0.011729
of 0.043260 total) and densities are positive at
all five sites (+1.406×10⁻⁴ … +1.102×10⁻⁴).

## 5. Read (iii) — the unmated remainder

None. C-A matched at the bar, so there is no
unmated remainder to decompose: δ is FULLY
expressed at the sites. The largest leftover is
the fit residual itself, 3.496×10⁻¹⁰ at A3 —
seven orders below δ's smallest content
(Δ/4 = 5.53×10⁻⁵ at A2).

Context (FIT C-S, registered as context, not a
verdict leg): the SINGLE m = 1 family also reaches
T_corr at the sites (N = 6 warm-A: 1.468×10⁻¹¹;
N = 12 warm-A: 3.288×10⁻¹⁰). The composite is
therefore not necessary at three-site scope; what
it adds on this record is a second, independent
family in the supply, the counting arm's depth,
and the primary's conditioning (σ_min 30.12 for
this solution vs 0.386 for 410's Fit A solution —
per-solution values against different targets,
stated as such, not a ranking theorem). The
supply side is not the bottleneck at site scope;
the bottlenecks remain the geometry side's SEC
(Phase 419) and the extent (Phase 413).

## 6. Admission (SS6)

Fresh minimal mirror `/home/spark/work/p420root`
(236 files, md5-verified file by file after
transfer). set_read405 on the laptop: joint diff
8.1×10⁻¹⁷, sec_min diff 3.6×10⁻¹⁹, rho_min diff
0.0, argmin radii diff 0.0 — laptop ADMITTED for
screening; deciding reads are the VM's. The C-A
primary's direct residuals cross-checked on the
laptop: per-site agreement ≤ 5.2×10⁻¹⁷
(`phase420/results/p420_admission.json`).

## 7. Verdict and fences

**COMPOSITE SUPPLIES THE CORRECTED TARGET — GATE
REFERRAL** (a four-condition SITE-MATED candidate).
Fences, all standing: site mating ≠ extent
coverage; the target is band-scoped (it inherits
the 405 winner's band [10, 20] scope, and Phase
409's full-extent failure of the underlying winner
is untouched — the corrected object's extent is
unaudited and no corrected OBJECT exists yet whose
extent could be audited); T_corr is a construction
of this phase, quoted as such, never as the 405
winner; σ_min per-solution per G36-C; novelty
NONE for the method (Gate-25, Martín-Moruno &
Visser 2021). No no-exotic claim beyond the sites:
the no-exotic standard is met by the composite's
total AT THE SITES, which is exactly what a site
mating can say.

Named follow-ups (for the parent's queue; nothing
launched from here): the gate verification of this
set; a geometry-side corrected object (Phase 419's
road) whose extent an audit could then read;
Phase 413's exterior re-closure, unchanged.

## 8. Amendments and incidents (on the record)

- **Amendment 1** (registration): CTRL-420-A's
  absolute cap ≤ 1×10⁻¹² was ill-posed against the
  stored value it had to reproduce (410's Fit A max
  residual is 2.97×10⁻¹²); corrected to ≤ 2× stored
  with max ≤ 1×10⁻¹¹ before any fit ran. The first
  control run had in fact reproduced every residual
  at ratio 0.999–1.000.
- **Amendment 2** (registration): the massless
  family's exactly-zero warm-start momenta are a
  0/0 singularity of u_spinor (E + m = |p|); warm
  starts now give the empty family unit momenta at
  zero amplitude (its tensor contribution still
  vanishes identically), plus a disclosed guard on
  the measure-zero singular set.
- **Amendment 3** (registration): the perturbation
  ladder completed at tightened tolerances after
  one rung stalled on default tolerances (§3); the
  bar never moved, both ladders are on the record,
  and the as-first-computed verdict string is
  preserved in `p420_results.json`
  (`verdict_as_first_computed`).
- The driver's first launch aborted at the
  Amendment-1 control bar (no fit had run); the
  second at the Amendment-2 singularity (no fit had
  completed). Per-start JSONL persistence is in
  `phase420/work/p420_cands_*.jsonl`.

Records: `phase420/results/p420_results.json`,
`p420_ladder_completed.json`, `p420_admission.json`,
`p420_check_results.json` (ALL PASS; its independent
δ rebuild agrees with the driver's stored targets
at max diff 0.0, and its verdict re-derivation
agrees). DESK: NO DATA CONTACT.
