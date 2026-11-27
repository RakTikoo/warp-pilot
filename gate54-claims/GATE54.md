# GATE-54 — INDEPENDENT RE-JUDGEMENT OF THE PHASE 410 CLAIM SET

**Charge:** ledger entry 1095 (2026-11-27). **Frame:** VM frame of
record (`~/workspace/warp-pilot/venv`, numpy 2.5.5 / scipy 1.18.1)
+ Phase 166 pin, float64; deciding reads on the VM. The laptop was
run as an admission control (§1) and is admitted for the deciding
reads of claims (a) and (b). **Machinery:** fresh gate machinery
only — `gate54/work/g54_lib.py`, written for this gate: γ matrices
assembled by Kronecker products; the superposition evaluated as an
explicit field function ψ(X) with analytic mode-by-mode
derivatives; NO pairwise S-matrix in any deciding path (Phase 410's
fits and Jacobians ran on the pairwise path; a separately written
pairwise assembly exists in the gate lib only as the C1
self-consistency cross-check); T_ab from the canonical symmetrised
formula with the Lagrangian density L computed honestly
(|L| ≤ 3.1×10⁻¹⁸ at the sites); own Hawking–Ellis classifier and
eigen-channel decomposition using Phase 410 SS4(ii)'s channel
definitions (the definitions are the claim's content; the code is
the gate's); own FD Jacobians (central h_j = 1×10⁻⁶·max(1,|θ_j|),
plus a forward variant for the Gate-34 leg of claim (d)).
Registration: `gate54/work/g54_registration.md`, written before
computation, ruling bars fixed in advance. Nothing was imported
from phase410/work, phase320/work, phase313/work, gate34/work or
gate36/work for any deciding computation. Targets are the STORED
tensors (the Phase 405 winner's geometry itself is Gate-50's
verified record, not re-judged here).

## Verdict summary

| Claim | Ruling |
|---|---|
| (a) Reproduction: Fit A (6-mode) residuals and joint σ_min 0.3857618146636974, rank 30/30; Fit B (12-mode) stencil track, max residual 2.31×10⁻¹⁴, σ_min 0.015432479500623982, rank 50/50 | **SURVIVES** (§2) |
| (b) Decomposition: supplier's NEC/WEC/DEC and SEC margins agree with T_req's to ≤ 1.3×10⁻¹² at all eight site reads; A2 SEC −2.213557×10⁻⁴ at diff 3.9×10⁻¹³; A3 SEC trace −3.388413×10⁻⁴ at diff 9.0×10⁻¹³ | **SURVIVES** — quoted at the phase checkpoint's own bound ≤ 1.34×10⁻¹² (rider G54-R2; §3) |
| (c) Supplier accounting: density positive at every site; \|a\|² = 0.02927 (Fit A) / 0.02123 (Fit B) | **SURVIVES** (§4) |
| (d) CTRL-313 clarification: the record's σ_min 0.0272 is Gate-34's value at Gate-34's own refit solution; Phase 313's stored solution carries 0.0347527502565207 | **CONFIRMED; quotable form ruled** (G54-D; exactly one standing claim-form must change — §5) |
| Controls C1–C3 | **ALL PASS** (§1) |

The quotable set is §6 (G54-A…G54-D, riders G54-R1…R3). The
standing fences are carried in §0 and bind every quotation.

## §0 Standing fences (verbatim in substance; bind the whole set)

- **Site mating ≠ extent coverage.** These claims are about named
  sites and a five-point radial stencil. No coverage claim of any
  kind attaches: the candidate's extent audit is Phase 409's; the
  coverage line is 346/357/368/362.
- **Sourcing ≠ curing.** The mating sources the Phase 405 winner's
  tensor AS IT STANDS, SEC violation included (at A2 the sourced
  SEC margin is −2.213557×10⁻⁴). **NO no-exotic-matter claim
  attaches to any sourced design.** The composite-supply question
  (W26) — supply T_req PLUS an SEC correction of +2.21×10⁻⁴ at A2
  and the band's SEC profile, keeping the joint channels — is not
  answered by this gate.
- **Novelty NONE for the method** (Martín-Moruno & Visser 2021,
  Gate-25).
- **σ_min is per-solution** (G36-C): every σ_min in this set names
  its solution on the face; no σ_min is a property of a target or
  of the mating.

## §1 Machinery, controls, laptop admission

**C1 · Builder self-consistency — PASS.** Field-function path vs
the lib's separately written pairwise cross-check path: max
relative T component diff **1.0238289108497418×10⁻¹³** ≤ the
1×10⁻¹² bar. Mode health on both stored primaries: norm deviation
≤ 6.9×10⁻¹⁸ (u†u = 2E|χ|² — the stored χ carry the fit amplitudes
and are not unit spinors); Dirac residuals reproduce the phase's
stored values EXACTLY (Fit A 5.1577036902917074×10⁻¹⁷, Fit B
2.7755575615628914×10⁻¹⁷).

**C2 · Stored 320 winner — PASS.** Gate direct residuals
[7.0105917748102985×10⁻¹⁵, 7.801736139349803×10⁻¹⁴,
8.230855248120619×10⁻¹⁴, 1.2959002164511548×10⁻¹⁵], maxR
8.230855248120619×10⁻¹⁴; gate σ_min 0.000399430073426119 vs stored
3.994300907411277×10⁻⁴ (rel diff 4.33×10⁻⁸); rank 40.

**C3 · Stored 313 winner — PASS (residual leg).** Gate maxR
3.253291635019471×10⁻¹³ vs stored 3.253339860306391×10⁻¹³ (abs
diff 4.82×10⁻¹⁸). The σ_min leg of the 313 control is claim (d),
§5 — Phase 313's own record contains no Jacobian and no σ_min.

**Laptop admission — ADMITTED for claims (a) and (b).** Gate lib +
driver + targets/primaries staged at `/home/spark/work/g54root`;
laptop venv numpy 2.5.5 / scipy 1.18.1 (the VM frame). Residuals
VM↔laptop agree ≤ 2.7×10⁻¹⁸ absolute; σ_min ≤ 1.6×10⁻⁸ relative
(Fit A laptop 0.3857618165948743; Fit B 0.015432480700342604);
densities ≤ 2.8×10⁻¹⁸; Fit A max channel diff laptop
1.3366523599761537×10⁻¹² vs VM 1.3366521431357192×10⁻¹². Records:
`gate54/results/g54_laptop_results.json`,
`gate54/results/g54_admission.json`. Deciding reads remain the
VM's.

**Gate-side incidents (disclosed; full record in the
checkpoint).** (1) A complex-casting error in the C1 pairwise
cross-check accumulator — fixed before any read. (2) The
mode-health Dirac slash initially paired covariant momenta with
covariant γ matrices (double-lowering), giving spurious ~0.4
Dirac residuals in a DIAGNOSTIC ONLY — fixed to γ^a p_a; no
deciding read used it (T, residuals, Jacobians unaffected); after
the fix the Dirac residuals reproduce the phase's stored values
exactly. (3) An early piping of the driver through `head -4`
SIGPIPE-killed it and truncated the results JSON to controls
only — the driver was re-run untruncated and the full record
regenerated with identical values; the on-disk JSON is complete.

## §2 Claim (a) — reproduction: SURVIVES

**Fit A (N = 6, the stored primary solution).** Gate direct
residuals R = ||T_sup − T_req||_F at the three A sites:
**8.144×10⁻¹⁵** (A1, joint argmin r = 17.926829268292682) /
**2.763×10⁻¹³** (A2, SEC argmin r = 12.073170731707318) /
**2.966×10⁻¹²** (A3, peak (10, 0, 0)) — stored
[8.146×10⁻¹⁵, 2.763×10⁻¹³, 2.966×10⁻¹²]; gate maxR
2.965982516552786×10⁻¹² vs stored 2.9659839407219894×10⁻¹², ~340×
inside the registered 1×10⁻⁹ bar. Joint Jacobian σ_min: gate
**0.3857618160623069** vs stored 0.3857618146636974 (rel diff
3.6×10⁻⁹, bar 1×10⁻²); σ_max 14944.163562989306; rank 30/30.
Per-site block σ_min agree to all printed digits (A1 202.7882 /
A2 80.6668 / A3 35.2925). h-stability: σ_min 0.3857618344922747
(h×10) / 0.385761815433645 (h÷10) — stable at 5×10⁻⁸ relative over
two decades of h.

**Fit B (N = 12, the stored primary solution).** Gate residuals
at the five stencil sites (r ± {−1.0, −0.5, 0, +0.5, +1.0} along
A1's direction): [9.110×10⁻¹⁵, 1.692×10⁻¹⁴, 2.305×10⁻¹⁴,
2.095×10⁻¹⁴, 7.928×10⁻¹⁵]; gate maxR 2.305490336342112×10⁻¹⁴ vs
stored 2.3054719412020823×10⁻¹⁴. Joint σ_min: gate
**0.015432480949901446** vs stored 0.015432479500623982 (rel diff
9.4×10⁻⁸); rank 50/50; per-site blocks match (198.9305 / 209.3959
/ 232.0209 / 258.7224 / 292.2305).

Both σ_min values are properties of the named stored solutions
(G36-C), quoted as such in G54-A.

## §3 Claim (b) — decomposition: SURVIVES

On the gate's own Hawking–Ellis classifier and eigen-channel
decomposition (Phase 410 SS4(ii) definitions), over ALL channels
× all eight site reads, the gate's max |channel diff| between
T_sup and T_req is **1.3366521431357192×10⁻¹²**, at A3, in a
tangential channel (NEC_t/DEC_t/SEC_t second component; the
joint_min diff there is −1.3×10⁻¹²). Per-site maxima: A1
2.57×10⁻¹⁵ · A2 3.85×10⁻¹³ · A3 1.34×10⁻¹² · B−1.0 1.07×10⁻¹⁴ ·
B−0.5 1.13×10⁻¹⁴ · B+0.0 3.71×10⁻¹⁴ · B+0.5 2.09×10⁻¹⁴ · B+1.0
1.40×10⁻¹⁴. The two named specifics reproduce exactly: at A2 the
SEC_min diff is **+3.9×10⁻¹³** (SEC value −2.213557×10⁻⁴); at A3
the SEC trace diff is **−9.0×10⁻¹³** (value −3.388413×10⁻⁴). Both
tensors are Type-I at all eight reads on the gate's own
classifier. The supplier misses no channel.

**Precision (rider G54-R2).** The bound is quoted as
**≤ 1.34×10⁻¹²** — the Phase 410 checkpoint's own recorded bound,
gate-confirmed at 1.337×10⁻¹². The ledger's "≤ 1.3×10⁻¹²" is that
figure rounded; quotations use the checkpoint's bound.

## §4 Claim (c) — supplier accounting: SURVIVES

Densities (T_sup[0,0]) positive at all eight reads, matching the
phase's to all printed digits: Fit A +1.238993×10⁻⁴ (A1) /
+3.956517×10⁻⁴ (A2) / +1.859720×10⁻³ (A3); stencil
+1.405987×10⁻⁴ / +1.319327×10⁻⁴ / +1.238993×10⁻⁴ /
+1.166924×10⁻⁴ / +1.101573×10⁻⁴. This is not a Phase 257
negative-density match. Prices |a|² reproduce at rel diff **0.0**:
**0.029266406597128584** (Fit A) / **0.021228149358339266**
(Fit B). Per-site implied s² agrees with |a|² to ≤ ~1×10⁻⁹
relative at every site (gate s² matches stored to 9 digits).

## §5 Claim (d) — the CTRL-313 clarification: CONFIRMED; quotable form ruled

**At Gate-34's stored θ** (`gate34/results/g34_item3a.json`,
N6_winner): the gate's forward-FD σ_min is
**0.027165249779697535** vs stored 0.027165249637030254 (rel diff
**5.25×10⁻⁹**; σ_max forward 3966.2716384216906 vs stored
3966.2716384255486, rel 9.7×10⁻¹³). The gate's central-FD read at
the same θ is 0.027173817559233707 — matching Phase 410's central
read 0.027173817517817934 at 1.5×10⁻⁹ relative. The stored figure
is the forward-FD-class value; the forward–central spread at this
θ is 3.2×10⁻⁴ relative — a recipe note, not a discrepancy
(rider G54-R3).

**At Phase 313's stored θ:** gate σ_min
**0.03475275259383748** vs Phase 410's 0.0347527502565207 (rel
diff 6.7×10⁻⁸) and Gate-36 CTRL-S2's 0.034753 — three independent
builds agree; rank 40; σ_max 6389.649857481197.

**RULING.** "σ_min = 0.0272" is quotable ONLY as Gate-34's
Jacobian σ_min at Gate-34's own refit solution on the Phase 312
winner's target (full precision 0.027165249637030254,
`gate34/results/g34_item3c.json`); never as Phase 313's solution's
σ_min (that solution carries 0.0347527502565207), never as a
property of the target or the mating (G36-C). Phase 313's own
record contains NO σ_min (its driver computed no Jacobian) —
nothing in Phase 313's documents needs correction.

**Exactly ONE standing claim-form must change:** G34-C's
parenthetical "(σ_min = 0.0272)" must carry the per-solution
attribution when quoted. GATE34.md §4's body text already
attributes correctly ("at the gate's N = 6 solution") and needs
no change; ledger entry 794 attributes correctly ("at the gate
solution"); Gate-36's attributions are correct; entry 798's
"~68× thinner than Gate-34's 0.0272" is a Gate-34 attribution and
stands. Ledger entry 1070's compressed control line ("313's …
(σ_min = 0.0272)") is superseded on this point by Phase 410's
Amendment 1 + entry 1094 + this gate; historical charge text is
not rewritten. No published claim's deciding number changes: at
BOTH solutions the Jacobian has full row rank with σ_min bounded
away from zero (0.0272 / 0.0348), so G34-C's structural content is
true at either attribution.

## §6 The quotable set

**G54-A (reproduction).** At the Phase 405 winner's binding sites
(A1 joint argmin r = 17.926829268292682; A2 SEC argmin
r = 12.073170731707318; A3 peak (10, 0, 0)), the stored m = 1
six-mode Dirac superposition of Phase 410 (Fit A primary)
reproduces T_req in full: gate direct residuals 8.144×10⁻¹⁵ /
2.763×10⁻¹³ / 2.966×10⁻¹² against the 1×10⁻⁹ bar; joint Jacobian
σ_min 0.3857618160623069 at that solution (rank 30/30). A single
stored 12-mode superposition (Fit B primary) tracks the five-site
radial stencil along A1's direction: gate max direct residual
2.305×10⁻¹⁴; joint σ_min 0.015432480949901446 at that solution
(rank 50/50). *(Rider G54-R1 binds: both σ_min values are
per-solution.)*

**G54-B (decomposition).** The supplier misses no channel: on an
independent channel decomposition, T_sup's NEC/WEC/DEC and SEC
margins agree with T_req's to **≤ 1.34×10⁻¹²** at all eight site
reads; at A2 the SEC value −2.213557×10⁻⁴ is reproduced at diff
+3.9×10⁻¹³; at A3 the SEC trace combination −3.388413×10⁻⁴ at
diff −9.0×10⁻¹³. The supplier sources the winner's tensor as it
stands, SEC violation included. *(Fences §0 bind: sourcing ≠
curing; no no-exotic claim.)*

**G54-C (accounting).** The supplier's density is POSITIVE at
every site read (Fit A +1.239×10⁻⁴ / +3.957×10⁻⁴ / +1.860×10⁻³;
stencil +1.406×10⁻⁴ … +1.102×10⁻⁴); prices |a|² =
0.029266406597128584 (Fit A) / 0.021228149358339266 (Fit B),
reproduced at rel diff 0.0.

**G54-D (the 313 σ_min ruling).** "σ_min = 0.0272" (full
precision 0.027165249637030254) is Gate-34's Jacobian σ_min at
Gate-34's own refit solution on the Phase 312 winner's target,
and is quotable only with that attribution on the face. Phase
313's stored solution carries σ_min 0.0347527502565207 (gate
0.03475275259383748). Phase 313's own record contains no σ_min
and needs no correction; the one standing claim-form that must
change is G34-C's parenthetical, which must carry the
per-solution attribution when quoted.

**G54-R1 (per-solution σ_min — binding rider to G54-A and to
every σ_min quotation in this lineage).** A σ_min is a property
of a named solution (G36-C), never of a target or of the mating.
Every quotation names its solution.

**G54-R2 (bound precision — binding rider to G54-B).** The
decomposition bound is quoted as ≤ 1.34×10⁻¹² (the phase
checkpoint's bound, gate-confirmed at 1.337×10⁻¹²), not as the
ledger's rounded ≤ 1.3×10⁻¹².

**G54-R3 (FD recipe note — binding rider to G54-D).** At
Gate-34's θ the stored 0.027165249637030254 is the forward-FD
value (gate forward 0.027165249779697535, rel 5.25×10⁻⁹); the
central-FD value at the same θ is 0.027173817559233707. The
forward–central spread (3.2×10⁻⁴ relative) is a recipe note, not
a discrepancy; quotations of the stored figure are quotations of
the forward-FD-class value.

*Gate-54 records: `gate54/results/` (g54_results.json,
g54_laptop_results.json, g54_admission.json); machinery
`gate54/work/` (g54_registration.md, g54_lib.py, g54_run.py,
g54_laptop.py, g54_run.log). Working record:
`gate54/GATE54_CHECKPOINT.md`.*

DESK: NO DATA CONTACT.
