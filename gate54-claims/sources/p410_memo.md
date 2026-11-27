# Phase 410 memo — SOURCE THE CANDIDATE: the spinor supplier at the Phase 405 winner's sites

**FTL VERDICT: SUPPLIES AT THE SITES — gate referral.** A 6-mode Dirac
superposition (m = 1) reproduces the Phase 405 winner's required stress
tensor T_req, in full, at every named site, at the registered bar
(direct-path max residual 2.97×10⁻¹² against a 1×10⁻⁹ bar), with the
supplier's own field density POSITIVE at every site. A single 12-mode
superposition also tracks T_req along the whole radial stencil around
the joint site (max residual 2.31×10⁻¹⁴ at five radii). The supplier
expresses every energy-condition channel of T_req — including the SEC
channel, whose demand it carries faithfully (it sources the winner's
tensor as it stands; it does not cure the winner's SEC deficit).

## What was put to the machinery

The winner (Phase 405, Gate-50 verified; joint +1.227385×10⁻⁶, K = 9
free shift shape on the 400 base) at four site groups:

- **A1** — the joint argmin: point (−17.827002016737087,
  0.1739363226225222, 1.8812104787714563), r = 17.926829268292682.
- **A2** — the SEC argmin site, identified from the winner's own SET
  read: point (−12.005940133720896, 0.11714078870496394,
  1.2669376693766954), r = 12.073170731707318, SEC margin
  −2.2135565049905559×10⁻⁴.
- **A3** — the peak site (10.0, 0, 0), r = 10.
- **B** — the radial stencil along A1's direction at
  r = 17.926829268292682 + {−1.0, −0.5, 0, +0.5, +1.0}.

## Read (i) — reproduction

Fit A (one superposition, jointly at A1/A2/A3, 30 residuals). Primary
at N = 6 (8/9 starts matched; the counting threshold N = 5 already
matched 4/6, best 2.65×10⁻¹³; below-threshold N = 4 matched 0/6, best
1.0×10⁻³, the residual concentrated at the peak site):

- direct-path residuals per site: A1 8.15×10⁻¹⁵, A2 2.76×10⁻¹³,
  A3 2.97×10⁻¹² (max 2.97×10⁻¹² ≤ 1×10⁻⁹ bar).
- σ_min of the joint FD Jacobian at the primary solution:
  **0.3857618146636974** (rank 30/30) — quoted per-solution per G36-C;
  this mating is far better conditioned than the 314 member's
  (3.99×10⁻⁴). Per-site block σ_min: A1 202.79, A2 80.67, A3 35.29.
- Perturbation ladder: perturbed targets reclose at the bar at every
  rung (ε = 10⁻¹²: 2.97×10⁻¹²; 10⁻⁹: ≤5.01×10⁻¹²; 10⁻⁶: ≤5.19×10⁻¹²;
  10⁻⁴: ≤3.39×10⁻¹¹) — the match is an isolated solution, not a
  knife-edge.
- The modes are genuine Dirac modes: equation residual 5.16×10⁻¹⁷.

Fit B (one superposition at all five stencil sites, 50 residuals).
N = 8 plateaus at 7.67×10⁻⁷ (arm truncated at 2/9 starts — see
disclosures); N = 12 matched 9/9 starts. Primary (warm): direct max
residual **2.31×10⁻¹⁴**, per site 9.11×10⁻¹⁵ … 2.31×10⁻¹⁴; joint
σ_min **0.015432479500623982** (rank 50/50), per-solution; ladder
recloses at ε = 10⁻⁹ (≤5.35×10⁻¹⁴) and 10⁻⁶ (≤5.80×10⁻¹⁴); Dirac
residual 2.78×10⁻¹⁷. One field tracks the winner's tensor across the
stencil — the site mating is not a point accident.

## Read (ii) — channel decomposition (the centre)

Type-I eigen-channels of T_req vs the supplier's tensor T_sup, at
every site (full tables in CHECKPOINT410.md). The supplier misses
nothing: every channel margin of T_sup agrees with T_req's to
≤ 1.3×10⁻¹². On the SEC question Phase 407 left open — the winner's
residual deficit is entirely SEC-carried, so can a supplier even
express the SEC channel's demand here? — the answer at these sites
is yes, exactly:

- at A2, where the winner's own SET read binds on SEC
  (−2.2136×10⁻⁴), T_sup reproduces T_req's SEC channel value at a
  difference of 3.9×10⁻¹³;
- at A3 (peak), T_req's SEC trace combination is −3.388413×10⁻⁴ and
  T_sup reproduces it at 9.0×10⁻¹³;
- the joint (NEC/WEC/DEC) channel at A1 (+1.227385×10⁻⁶, the winner's
  joint margin) is reproduced at 8.3×10⁻¹⁶.

So the spinor supplier's tensor spans the SEC demand at these sites.
What it supplies is the winner's tensor as it stands — SEC violation
included. Sourcing is not curing: the composite-supply question
(whether anything can carry the joint channels while NOT carrying
the SEC deficit) is not this phase's verdict form, and this mating
does not answer it.

## Read (iii) — the supplier's own accounting

The Phase 257 lesson (a match at negative field density is a
different claim) does not bite here: the supplier's density is
positive at every site read.

- Fit A solution densities: A1 +1.238993×10⁻⁴, A2 +3.956517×10⁻⁴,
  A3 +1.859720×10⁻³.
- Fit B solution densities along the stencil: +1.405987×10⁻⁴,
  +1.319327×10⁻⁴, +1.238993×10⁻⁴, +1.166924×10⁻⁴, +1.101573×10⁻⁴.
- Amplitude price: |a|² = 0.029266406597128584 (Fit A) /
  0.021228149358339266 (Fit B); the per-site implied scale s² agrees
  across sites to ~10⁻⁹ relative in both fits — one field, one price,
  no site-by-site rescaling.

## Controls

- CTRL-320 (the 314 member's mating, on this build): direct maxR
  8.230813708013984×10⁻¹⁴ = stored exactly; σ_min
  3.994300112181778×10⁻⁴ vs the record's 3.994300×10⁻⁴ (rel.
  2.0×10⁻⁷). PASS.
- CTRL-313 (the 312 winner's mating): residual leg exact
  (3.253339860306391×10⁻¹³ = stored, diff 0.0). The record's σ_min
  0.0272 is Gate-34's number, computed at Gate-34's own refit
  solution with forward differences; evaluated exactly there, this
  build reads 0.027165249667980257 vs Gate-34's stored
  0.027165249637030254 (rel. ~1.1×10⁻⁹). At 313's stored solution
  this build reads σ_min = 0.0347527502565207 — a different solution
  of the same target, per G36-C. PASS (clarification disclosed in
  the registration amendment written before any candidate read).
- CTRL-TGT-410 (the target itself): the winner's joint, SEC min,
  and A1 NEC/worst-null values reproduce Gate-50's stored record at
  diff 0.0 (SEC at 3.0×10⁻¹⁹); the loaded knots equal Gate-50's
  stored knots exactly.
- Laptop admission (SS6): the winner is 100% Type-I, so its deciding
  values are frame-invariant; the laptop pool mirror reproduced the
  joint at diff 8.1×10⁻¹⁷ and the SEC min at 6×10⁻¹⁹. ADMITTED for
  screening; all deciding reads are the VM's.

## Disclosures (execution)

The phase executed under repeated interruption (one silent driver
death, two service restarts) on a contended shared VM. Per-start
JSONL persistence (Phase 320 recovery pattern) banked every
completed start; re-executions reproduced the crashed runs' values
identically. Two arms were truncated under disclosed registration
amendments (Phase 392 truncated-run precedent): Fit B's
below-threshold N = 6 arm at 2/6 starts (stalls 4.54×10⁻⁶,
1.50×10⁻⁴ — the arm cannot match by counting) and Fit B's N = 8 arm
at 2/9 starts (both starts plateau at the cap at 7.67×10⁻⁷ /
1.06×10⁻⁶, warm start included). One driver bug was found and fixed
mid-phase (a missing np.array wrap in the residual closure, exposed
only by the perturbation ladder's list-typed norms; numerics
unchanged, amendment 4). Reopening condition for the truncations:
the un-run starts can be executed at any time from the persisted
machinery if a gate requires the full arms. An independent checker
re-derived the targets (exact), the primaries' direct residuals
(≤ 4×10⁻¹⁸), the decomposition (diff 0.0), and the verdict:
ALL PASS.

## Fences

- A site mating is not a field on the extent. This phase says the
  supplier reproduces T_req at the named sites and along one radial
  stencil; coverage of the winner's full extent belongs to the
  extent line (346/357/368/362) and the candidate's extent audit is
  Phase 409, running separately. No coverage is claimed.
- The mating reproduces the winner's tensor including its SEC
  violation; it does not establish the no-exotic-matter standard
  (NEC+WEC+DEC pointwise on total stress) for any sourced design.
- σ_min values are properties of the named solutions (G36-C), never
  of the target.
- Novelty: NONE for the mating method (Martín-Moruno & Visser 2021,
  per Gate-25).

## Three-goals accounting

- Goal 1 (FTL drive): the 405 winner's required tensor at its
  binding sites is sourceable by an explicit Dirac superposition
  with positive field density and a well-conditioned σ_min — the
  supply question at the sites is answered YES. This verdict
  carries a gate referral.
- Goal 2 (wormhole): no wormhole object was mated in this phase;
  nothing claimed.
- Goal 3 (subluminal record): untouched; β standings unchanged.

DESK: NO DATA CONTACT — no publication action arises from this
phase; the gate referral is for the parent to log.
