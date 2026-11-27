# Warp Pilot v1.45.0 — Gate-54: Phase 410's spinor-supply claim set survives independent re-judgement as fenced — the Phase 405 warp-grade candidate's required stress is reproduced in full at its binding sites by a single Dirac superposition with positive density throughout, the supplier missing no energy-condition channel (agreement ≤ 1.34×10⁻¹²), and one attribution ruling (G54-D) on the face — sites only; sourcing ≠ curing; no no-exotic-matter claim

This release publishes Phase 410's claim set as
re-judged by Gate-54 (ledger entry 1099). Phase
410 (SOURCE THE CANDIDATE) put the Phase 405
winner's required tensor T_req — the programme's
gate-verified warp-grade candidate (Gate-50,
v1.42.0), whose NEC/WEC/DEC joint is positive in
the band [10, 20] at the full SS7 criterion peak
with SEC failing on its face — to the spinor
mating machinery (the 313/320 pattern), at the
sites where the requirement binds: A1 the joint
argmin (r = 17.926829268292682), A2 the SEC
argmin (r = 12.073170731707318), A3 the peak
(10, 0, 0), and a five-point radial stencil
along A1's direction. Its verdict: a single
m = 1 six-mode Dirac superposition reproduces
T_req in full at every named site at the
registered bar, with positive supplier density
throughout, a single 12-mode superposition
tracks it along the whole stencil, and the
supplier misses no energy-condition channel —
SEC included. SUPPLIES AT THE SITES, with a
gate referral.

Gate-54 re-judged the set with fresh machinery
built for the gate alone: gamma matrices
assembled by Kronecker products; the
superposition evaluated as an explicit field
function ψ(X) with analytic mode-by-mode
derivatives; NO pairwise S-matrix in any
deciding path (Phase 410's fits and Jacobians
ran on the pairwise path; a separately written
pairwise assembly exists in the gate lib only
as the C1 self-consistency cross-check); T_ab
from the canonical symmetrised formula with
the Lagrangian density L computed honestly
(|L| ≤ 3.1×10⁻¹⁸ at the sites); the gate's own
Hawking–Ellis classifier and eigen-channel
decomposition; its own FD Jacobians. Nothing
was imported from phase410/work, phase320/work,
phase313/work, gate34/work or gate36/work for
any deciding computation; targets are the
STORED tensors (the Phase 405 winner's geometry
is Gate-50's verified record, not re-judged
here). Controls C1–C3 ALL PASS before any claim
read. The laptop was run as an admission
control and is ADMITTED for the deciding reads
of claims (a) and (b) (residuals VM↔laptop
≤ 2.7×10⁻¹⁸ absolute; σ_min ≤ 1.6×10⁻⁸
relative); deciding reads remain the VM's.
Disclosed on the gate's face: two gate-side
bugs found and fixed during the work (a
complex-casting error in a cross-check
accumulator, fixed before any read; a
double-lowered index in a diagnostic-only
health check — no deciding read used it) and a
SIGPIPE incident (an early driver run piped
through head truncated the results JSON;
re-run untruncated, the full record regenerated
with identical values). Verdicts: (a) SURVIVES;
(b) SURVIVES; (c) SURVIVES; (d) CONFIRMED, with
the quotable form ruled (G54-D). The quotable
set (GATE54.md §6: G54-A…G54-D, riders
G54-R1…R3) is embedded verbatim as a blockquote
at the end of these notes.

## Attribution ruling — G54-D: one standing claim-form changes; no published claim's deciding number changes

This ruling is part of the claim set, not a
footnote to it. Phase 410's CTRL-313 control
found that the record's "σ_min = 0.0272" is
Gate-34's Jacobian σ_min at Gate-34's own
refit solution on the Phase 312 winner's
target. Gate-54 confirms the clarification on
its own machinery and rules the quotable form:

- "σ_min = 0.0272" (full precision
  0.027165249637030254, gate34/results/
  g34_item3c.json) is quotable ONLY as Gate-34's
  Jacobian σ_min at Gate-34's own refit
  solution on the Phase 312 winner's target —
  never as Phase 313's solution's σ_min,
  never as a property of the target or of the
  mating (G36-C; rider G54-R1).
- Phase 313's stored solution carries σ_min
  0.0347527502565207 (Gate-54 reads
  0.03475275259383748; Gate-36's CTRL-S2 read
  0.034753 — three independent builds agree).
- Phase 313's own record contains NO σ_min
  (its driver computed no Jacobian) — nothing
  in Phase 313's documents needs correction.
- Exactly ONE standing claim-form must change:
  G34-C's parenthetical "(σ_min = 0.0272)"
  must carry the per-solution attribution when
  quoted. GATE34.md §4's body text, ledger
  entry 794 and Gate-36's attributions already
  attribute correctly and need no change.
- The historical GATE34.md is NOT edited. The
  correction rides in this release, following
  the honesty precedent of the v1.29.0
  correction release.
- NO published claim's deciding number
  changes: at BOTH solutions the Jacobian has
  full row rank with σ_min bounded away
  from zero (0.0272 at Gate-34's refit
  solution; 0.0348 at Phase 313's stored
  solution), so G34-C's structural content
  holds at either attribution.
- Recipe note (rider G54-R3): the stored
  figure 0.027165249637030254 is the
  forward-FD-class value (Gate-54's forward
  read 0.027165249779697535, rel. diff
  5.25×10⁻⁹); the central-FD value at the same
  θ is 0.027173817559233707. The
  forward–central spread (3.2×10⁻⁴ relative)
  is a recipe note, not a discrepancy.

## The claims in brief

(a) G54-A — REPRODUCTION SURVIVES. Fit A (the
stored m = 1 six-mode primary solution): gate
direct residuals 8.144×10⁻¹⁵ / 2.763×10⁻¹³ /
2.966×10⁻¹² at A1/A2/A3 (~340× inside the
1×10⁻⁹ bar); joint Jacobian σ_min at that
solution 0.3857618160623069 (stored
0.3857618146636974; rank 30/30). Fit B (the
stored 12-mode primary solution) tracks the
five-site stencil: gate max direct residual
2.305×10⁻¹⁴; joint σ_min at that solution
0.015432480949901446 (rank 50/50). Both
σ_min values are per-solution (G54-R1).

(b) G54-B — DECOMPOSITION SURVIVES. On the
gate's independent channel decomposition, the
supplier's NEC/WEC/DEC and SEC margins agree
with T_req's to ≤ 1.34×10⁻¹² at all eight site
reads (gate max |channel diff|
1.3366521431357192×10⁻¹², at A3 in a tangential
channel); at A2 the SEC value −2.213557×10⁻⁴
is reproduced at diff +3.9×10⁻¹³; at A3 the
SEC trace combination −3.388413×10⁻⁴ at diff
−9.0×10⁻¹³. The supplier sources the winner's
tensor as it stands, SEC violation included.
(Rider G54-R2 binds: the bound is quoted as
≤ 1.34×10⁻¹² — the Phase 410 checkpoint's own
bound, gate-confirmed at 1.337×10⁻¹².)

(c) G54-C — ACCOUNTING SURVIVES. The
supplier's density is POSITIVE at all eight
reads (Fit A +1.238993×10⁻⁴ / +3.956517×10⁻⁴ /
+1.859720×10⁻³; stencil +1.405987×10⁻⁴ …
+1.101573×10⁻⁴) — not a Phase 257
negative-density match. Prices |a|² reproduce
at rel. diff 0.0: 0.029266406597128584
(Fit A) / 0.021228149358339266 (Fit B).

(d) G54-D — the attribution ruling of the
section above: CONFIRMED, quotable form ruled.

## Fences (GATE54.md §0 — bind every quotation)

- **Site mating ≠ extent coverage.** These
  claims are about named sites and a five-point
  radial stencil. No coverage claim of any kind
  attaches: the candidate's extent audit is
  Phase 409's; the coverage line is
  346/357/368/362.
- **Sourcing ≠ curing.** The mating sources
  the Phase 405 winner's tensor AS IT STANDS,
  SEC violation included (at A2 the sourced SEC
  margin is −2.213557×10⁻⁴). **NO
  no-exotic-matter claim attaches to any
  sourced design.** The composite-supply
  question (W26) — supply T_req PLUS an SEC
  correction of +2.21×10⁻⁴ at A2 and the band's
  SEC profile, keeping the joint channels — is
  not answered by this gate.
- **Novelty NONE for the method**
  (Martín-Moruno & Visser 2021, Gate-25).
- **σ_min is per-solution** (G36-C; rider
  G54-R1): every σ_min in this set names
  its solution on the face.

## The quotable set (GATE54.md §6, verbatim)

> **G54-A (reproduction).** At the Phase 405 winner's binding sites
> (A1 joint argmin r = 17.926829268292682; A2 SEC argmin
> r = 12.073170731707318; A3 peak (10, 0, 0)), the stored m = 1
> six-mode Dirac superposition of Phase 410 (Fit A primary)
> reproduces T_req in full: gate direct residuals 8.144×10⁻¹⁵ /
> 2.763×10⁻¹³ / 2.966×10⁻¹² against the 1×10⁻⁹ bar; joint Jacobian
> σ_min 0.3857618160623069 at that solution (rank 30/30). A single
> stored 12-mode superposition (Fit B primary) tracks the five-site
> radial stencil along A1's direction: gate max direct residual
> 2.305×10⁻¹⁴; joint σ_min 0.015432480949901446 at that solution
> (rank 50/50). *(Rider G54-R1 binds: both σ_min values are
> per-solution.)*
>
> **G54-B (decomposition).** The supplier misses no channel: on an
> independent channel decomposition, T_sup's NEC/WEC/DEC and SEC
> margins agree with T_req's to **≤ 1.34×10⁻¹²** at all eight site
> reads; at A2 the SEC value −2.213557×10⁻⁴ is reproduced at diff
> +3.9×10⁻¹³; at A3 the SEC trace combination −3.388413×10⁻⁴ at
> diff −9.0×10⁻¹³. The supplier sources the winner's tensor as it
> stands, SEC violation included. *(Fences §0 bind: sourcing ≠
> curing; no no-exotic claim.)*
>
> **G54-C (accounting).** The supplier's density is POSITIVE at
> every site read (Fit A +1.239×10⁻⁴ / +3.957×10⁻⁴ / +1.860×10⁻³;
> stencil +1.406×10⁻⁴ … +1.102×10⁻⁴); prices |a|² =
> 0.029266406597128584 (Fit A) / 0.021228149358339266 (Fit B),
> reproduced at rel diff 0.0.
>
> **G54-D (the 313 σ_min ruling).** "σ_min = 0.0272" (full
> precision 0.027165249637030254) is Gate-34's Jacobian σ_min at
> Gate-34's own refit solution on the Phase 312 winner's target,
> and is quotable only with that attribution on the face. Phase
> 313's stored solution carries σ_min 0.0347527502565207 (gate
> 0.03475275259383748). Phase 313's own record contains no σ_min
> and needs no correction; the one standing claim-form that must
> change is G34-C's parenthetical, which must carry the
> per-solution attribution when quoted.
>
> **G54-R1 (per-solution σ_min — binding rider to G54-A and to
> every σ_min quotation in this lineage).** A σ_min is a property
> of a named solution (G36-C), never of a target or of the mating.
> Every quotation names its solution.
>
> **G54-R2 (bound precision — binding rider to G54-B).** The
> decomposition bound is quoted as ≤ 1.34×10⁻¹² (the phase
> checkpoint's bound, gate-confirmed at 1.337×10⁻¹²), not as the
> ledger's rounded ≤ 1.3×10⁻¹².
>
> **G54-R3 (FD recipe note — binding rider to G54-D).** At
> Gate-34's θ the stored 0.027165249637030254 is the forward-FD
> value (gate forward 0.027165249779697535, rel 5.25×10⁻⁹); the
> central-FD value at the same θ is 0.027173817559233707. The
> forward–central spread (3.2×10⁻⁴ relative) is a recipe note, not
> a discrepancy; quotations of the stored figure are quotations of
> the forward-FD-class value.
>
> *Gate-54 records: `gate54/results/` (g54_results.json,
> g54_laptop_results.json, g54_admission.json); machinery
> `gate54/work/` (g54_registration.md, g54_lib.py, g54_run.py,
> g54_laptop.py, g54_run.log). Working record:
> `gate54/GATE54_CHECKPOINT.md`.*
>
> DESK: NO DATA CONTACT.

**Links.** Concept DOI: 10.5281/zenodo.24425078.
Version DOI: TBD — Zenodo mints it at release.

Disclosure: this is AI-driven analysis — the
computation was produced by an AI research system
working under my direction, and I am posting it
precisely to have its legitimacy checked by humans:
is the argument sound, and is it already known?
Corrections and references are exactly what I am
asking for.
