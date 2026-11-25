# GATE-34 REGISTRATION — ADVERSARIAL RE-JUDGEMENT OF THE
# POSITIVE-DENSITY PAIR (PHASES 312 + 313)

Written before any gate computation. Frame of record:
Phase 166 pin, venv python (numpy 2.5.5 / scipy 1.18.1),
float64 throughout. The gate writes its own machinery
throughout and does not repair what it breaks.

## The pair under re-judgement

- **Phase 312** (CHECKPOINT312.md, p312_memo.md): in the
  Phase 308 extended class (γ_ij = δ_ij + (M−1) n_i n_j)
  at the Gate-30 winner's base pose (spec {'shape':'plat',
  'a':2,'b':2,'A':0.07439108177516472,'c':15,'W':5,'e':3.0},
  β = 1.1), the broad-ramp member {'kind':'ramp','m0':+1.0,
  'r1':10.5,'r2':19.5} — M = 1 + [U(r;10.5,19.5) −
  U(r;21,24)] — is stored with depth −1.180275×10⁻³
  (SAMPLER-M, adversary-polished), four binding sites by
  Phase 293's rule, per-site ρ_req
  +2.168496×10⁻⁴ / +1.521832×10⁻⁴ / +2.161432×10⁻⁴ /
  +6.498030×10⁻⁵ (S1/S2/S3/S4), all R-carried
  (R/(16π) > |Q_K/(16π)| at every site).
- **Phase 313** (CHECKPOINT313.md, p313_memo.md): one
  six-mode Dirac superposition (m = 1) reproduces that
  member's T_req in full, jointly at the four sites, at
  direct-path residuals ≤ 3.253×10⁻¹³ (bar 1×10⁻⁹), with
  density at the match +2.168496×10⁻⁴ / +1.521832×10⁻⁴ /
  +2.161432×10⁻⁴ / +6.498030×10⁻⁵ — positive at all four
  sites. Verdict: MATCH AT POSITIVE DENSITY.

## Gate machinery (all written fresh in gate34/work/)

- `g34_lib.py` — profiles re-implemented from their
  definitions (S via the incomplete-beta form; N via the
  plateau H-product; M via the quintic-smoothstep ramp);
  an Einstein-tensor assembly organised as tensor
  calculus over derivative operators (NOT p312_lib's
  index-loop assembly); the ADM Eulerian frame
  re-implemented from its definition (normal observer +
  γ-eigendecomposition triad, as in verify_metric's
  definition); an exact pointwise worst-null read
  (Fibonacci scan + Nelder–Mead, fresh code); the
  Phase 308 R/Q_K split formula re-implemented.
- `g34_fd.py` — a finite-difference assembly (metric
  values only; 5-point stencils, two step sizes,
  Richardson) used ONLY as an independent guard on the
  analytic assembly, never as a deciding read.
- The SAMPLER-M margin functional is the protocol's
  definition (verify_metric.hawking_ellis_margins with
  the sampled fallback, via p2352_run.margins_chunked) —
  programme machinery predating both phases, applied
  identically to the gate's own tensors. The sampler is
  part of the protocol being re-judged, not of either
  phase's machinery.
- `g34_spinor.py` — the Dirac stress builder written
  from the field definitions (Dirac representation,
  u_spinor, symmetrised bilinear stress, folded
  amplitudes, per-site phases); the joint-fit optimiser
  is the gate's own (own packing, own starts, own seed).

## Controls (all before any re-judgement read is quoted)

- **G34-C1 (two-function limit):** the gate assembly at
  M ≡ 1 reproduces Phase 295's factorisation value
  −β²S′²(1−n_x̂²)/(32πα²) for ρ at the Gate-30 winner's
  four Phase 293 sites to ≤ 1×10⁻¹².
- **G34-C2 (FD guard):** the gate's analytic That at the
  four stored site points and at 12 off-site sample
  points agrees with the FD assembly's That within the
  FD error class (reported; expected ≤ 1×10⁻⁷ absolute
  on components of size ≤ 3×10⁻³).
- **G34-C3 (split audit):** the gate's R/Q_K split at
  the four sites reproduces Phase 312's stored per-site
  R/(16π), R1, R2, Q_K values to ≤ 1×10⁻¹², and
  R + Q_K reproduces 16π × (gate ρ) to ≤ 1×10⁻¹⁵.
- **G34-C4 (spinor builder):** the gate builder,
  evaluated on Phase 313's stored winning modes
  (`p313_joint_bestfit.json`), reproduces the stored
  per-site direct residuals (9.816544100325221×10⁻¹⁴ /
  2.847×10⁻¹³ / 3.253×10⁻¹³ / 7.547×10⁻¹⁴ class) and
  rhos_direct to ≤ 1×10⁻¹¹ absolute per site
  (stored-precision class, mirroring Phase 313's
  CTRL-293 bar); winning modes' Dirac residuals
  ≤ 1×10⁻⁹.
- Record reproduction (reported, not a control bar):
  the gate's That at the four site points vs
  `p313_targets.json`'s stored That, componentwise.

## Item 1 — the member, independently

Re-read the broad-ramp m₀ = +1.0 member from its stored
profile with the gate assembly: SET-244 read (41 radial
midpoint nodes × 162 Fibonacci dirs, SAMPLER-M margins on
the gate's tensors); adversary polish (gate's own,
Type-I-restricted, Phase 263/267 form) → depth; the four
binding sites re-derived under Phase 293's rule from the
gate's SET read (S1 polished worst; S2 SET SAMPLER-M NEC
argmin; S3 Type-I SET argmin; S4 SET argmin over r ≥ 15)
and ALSO read at Phase 312's stored site points; per-site
ρ_req, both NEC reads (SAMPLER-M named; exact pointwise
named), Type-I flags, and the R/Q_K split at those sites.
Any deciding number that moves is reported at both values
(gate's and the phase's).

## Item 2 — the site rule on the new background

Adversary read over the member's volume with the gate
assembly, hunting loci where ρ_req < 0 that are
binding-grade candidates the rule never selects:
- Dense scan: 201 radial nodes × 642 Fibonacci dirs on
  [10, 20]; per point ρ_req, Type-I flag, exact
  pointwise NEC (eigenvalue form where Type-I; fib-642
  contraction min as the general read).
- Continuum polish: Nelder–Mead minimisation of the
  exact pointwise NEC and of ρ_req from the scan's
  extreme loci (gate's own worst-null at each locus).
- Binding-grade thresholds, fixed here: a ρ < 0 locus is
  binding-grade if (a) its SAMPLER-M NEC ≤ S2's stored
  SAMPLER-M NEC (−3.126870×10⁻³) — more binding than the
  rule's own global argmin; or (b) its exact pointwise
  NEC ≤ the most binding exact read among the four
  sites (−3.517021×10⁻³, S3); or (c) its SAMPLER-M NEC
  ≤ the member's depth (−1.180275×10⁻³) AND it is
  Type-I (an S1-class locus the polish could have
  selected). Report every binding-grade ρ < 0 locus
  found, or the scan's closest approaches.
- Output: the exact scope the binding-site verdict can
  certify after this read — the gate either certifies
  the rule's selection on this background (no
  binding-grade ρ < 0 locus exists outside the
  selected sites, at the thresholds above) or fences
  the claim to the rule's literal scope.

## Item 3 — the match, independently

- Reproduce the joint four-site fit from the stored
  targets (`p313_targets.json`) with the gate builder +
  gate optimiser (m = 1, N = 6; own starts, seed 3401):
  report per-site direct residuals and densities at the
  match, beside Phase 313's.
- Mode-count sweep (gate's own): N ∈ {4, 5, 6, 7, 8},
  ≥ 4 starts per arm, best max-residual per arm.
  Parameter counting stated (7N real parameters vs 40
  residual components; overall phase gauge −1).
- Structural read: singular values of the 40 × 42
  Jacobian at the gate's N = 6 solution.
- Perturbation read: each target perturbed componentwise
  by random symmetric noise of relative size ε ×
  |That_s|_F, ε ∈ {1×10⁻¹² (stored-precision class),
  1×10⁻⁹, 1×10⁻⁶, 1×10⁻⁴}; re-fit warm-started from the
  gate's unperturbed winner plus fresh starts; report
  per ε whether the 1×10⁻⁹ bar is re-achieved and the
  density at the perturbed match.

## Item 4 — the claim set

Per-claim verdicts (SURVIVES / SURVIVES RESTATED /
FAILS):
- **G34-A** the member's existence and values (profile,
  depth, the four sites, per-site ρ_req, R-carriage).
- **G34-B** binding-site positivity (at the scope
  Item 2 certifies).
- **G34-C** the match and its residuals (one six-mode
  superposition, joint, residuals ≤ 3.253×10⁻¹³ class).
- **G34-D** density-at-match positivity.
The quotable set carries verbatim: the full-volume
fence (this member's SET-244 ρ minimum is
−7.561×10⁻⁸ — negative, at the 10⁻⁷ level; positivity
is NOT pointwise over the shell); the NEC fence (the
member's depth is a negative NEC read,
−1.180275×10⁻³ SAMPLER-M adversary-polished, and the
exact pointwise reads at the sites are more negative,
−3.516×10⁻³ / −3.150×10⁻³ / −3.517×10⁻³ / −1.831×10⁻³
at S1/S2/S3/S4 — no energy-condition pass is implied);
the absent QI read (no QI read for any extended-class
member exists in the record and none is quoted). No
claim is quoted beyond binding-site scope unless
Item 2's read certifies more.

## Standing fences

Controls first; deciding numbers that move are reported
at both values; margins alone never decide; SET reads
are set reads; the polished site is an adversary-polished
local worst under the protocol, not a certified global
minimum. **DESK: NO DATA CONTACT** (configurations, not
data). No ledger append, no launches, no publication,
no user contact. Writes inside gate34/ only.
