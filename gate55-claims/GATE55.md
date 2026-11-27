# GATE-55 — INDEPENDENT RE-JUDGEMENT OF THE PHASE 420 CLAIM SET

**Charge:** ledger entry 1103 (2026-11-27). **Frame:** VM frame of
record (`~/workspace/warp-pilot/venv`, numpy 2.5.5 / scipy 1.18.1)
+ Phase 166 pin, float64; deciding reads on the VM. The laptop was
run as an admission control (§2) and is admitted as corroboration
for the deciding reads of claims (a), (b) and (c). **Machinery:**
fresh gate machinery only — `gate55/work/g55_lib.py`, written for
this gate: γ matrices assembled by Kronecker products; the
composite superposition evaluated as an explicit field function
ψ(X) with per-mode masses and analytic mode-by-mode derivatives;
T_ab from the canonical symmetrised bilinear on the total field —
the object Phase 420's registration SS2 defines — with NO pairwise
S-matrix in any deciding path (Phase 420's fits ran on the pairwise
path; a separately written pairwise assembly exists in the gate lib
only as the C1 self-consistency cross-check); own Hawking–Ellis
classifier and eigen-channel decomposition using Phase 410
SS4(ii)'s channel definitions (the definitions are the claim's
content; the code is the gate's); own δ construction from the
stored T_req; own FD Jacobians (central h_j = 1×10⁻⁶·max(1,|θ_j|),
Phase 410's recipe). Registration: `gate55/work/g55_registration.md`,
written before computation, ruling bars fixed in advance. Nothing
was imported from phase420/work, phase410/work, phase320/work,
phase313/work or gate54/work for any deciding computation. Targets
and solutions are the STORED records (Phase 420's stored T_req is
bit-identical to Phase 410's stored That at the A sites — gate
re-checked, max diff 0.0; the Phase 405 winner's geometry itself
is Gate-50's verified record, not re-judged here).

## Verdict summary

| Claim | Ruling |
|---|---|
| (a) δ construction: eigenframe split of Δ = −SEC_trace over the four eigenvalues at A2/A3 (δ ≡ 0 at A1 and the stencil); δ spends no joint surplus (A2 joint 1.385×10⁻⁴ → 2.491×10⁻⁴, channel by channel) | **SURVIVES** (§3) |
| (b) Reproduction: composite primary max residual 3.496×10⁻¹⁰ at the 1×10⁻⁹ bar; σ_min 30.12132520557749 per-solution; stencil tracking 3.565×10⁻¹⁵ | **SURVIVES** (§4) |
| (c) Composite total four-condition-clean at the sites: every channel ≥ 0 at A1/A2/A3; density positive; SEC_trace ≈ 0 at A2/A3; prices \|a\|² 0.029172 / 2.036×10⁻⁶ | **SURVIVES** — with the density-naming rider G55-R2 (§5) |
| (d) C-S context arm: the single m = 1 family also reaches T_corr at the three sites (1.468×10⁻¹¹) | **CONFIRMED** — rider G55-R1 scopes every quotation: "composite" is never quotable as necessary at site scope (§6) |
| Amendments 1–3 (control cap; u_spinor 0/0 guard; completed ladder) | **ALL SOUND** (§7) |
| Controls C1–C3 | **ALL PASS** (§2) |

The quotable set is §1 (G55-A…G55-D, riders G55-R1…R3). The
standing fences are carried in §0 and bind every quotation.

## §0 Standing fences (verbatim in substance; bind the whole set)

- **T_corr is a construction of Phase 420** — never the Phase 405
  winner, and it corresponds to **NO existing geometry**. No
  corrected object exists or is claimed; its extent is unaudited
  because there is nothing to audit (the geometry-side road is
  Phase 419's; the underlying winner's extent is Phase 413's).
- **Site mating ≠ extent coverage.** These claims are about named
  sites and a five-point radial stencil. No coverage claim of any
  kind attaches.
- **Sourcing a corrected target ≠ producing a legal design.** The
  mating sources a site-wise corrected tensor; no geometry
  requires that tensor, and no sourced design is claimed legal.
- **Novelty NONE for the method** (Martín-Moruno & Visser 2021,
  Gate-25).
- **σ_min is per-solution** (G36-C): every σ_min in this set names
  its solution on the face; no σ_min is a property of a target or
  of the mating.

## §1 The quotable set

**G55-A (δ construction).** At Phase 410's sites, the corrected
target T_corr = T_req + δ is reproduced **bit-identically** by the
gate's independent construction (max abs diff 0.0 against the
stored T_corr at all eight sites): δ is built per site in the
eigenframe of η·T_req, splitting Δ = −SEC_trace equally over the
four eigenvalues entering SEC_trace (Δ = 2.2135565049905559×10⁻⁴
at A2, gate 2.213556504990559×10⁻⁴; Δ = 3.3884134221257565×10⁻⁴
at A3), and δ ≡ 0 at A1 and all five stencil sites. SEC_trace of
the corrected target is 1.1×10⁻¹⁹ at A2 and 0.0 at A3. **δ spends
no joint surplus:** at both corrected sites every principal
pressure of T_req is negative (A2: −2.494×10⁻⁴, −1.800×10⁻⁴,
−1.798×10⁻⁴; A3: −2.403×10⁻⁴, −9.790×10⁻⁴, −9.790×10⁻⁴), so the
equal split raises every joint channel — the gate's channel-by-
channel differences (T_corr − T_req) at A2 are all ≥ +2.84×10⁻⁵
(minimum at DEC_flux) and at A3 all ≥ +8.29×10⁻⁵; A2's joint_min
moves 1.384623×10⁻⁴ → 2.491401×10⁻⁴, A3's 8.805×10⁻⁴ →
1.050×10⁻³. *(Fences §0 bind: T_corr is a construction, not a
geometry.)*

**G55-B (reproduction).** The stored composite primary of Phase
420 (two spinor families, m = 1 and m = 0, (6,6), fitted jointly
with cross terms) reproduces the corrected target at {A1, A2,
A3}: gate direct residuals **4.057×10⁻¹² / 7.640×10⁻¹² /
3.496×10⁻¹⁰** — bit-identical to the phase's stored values —
max 3.496×10⁻¹⁰ at the registered 1×10⁻⁹ bar. Joint Jacobian
σ_min at that solution: gate **30.12132520520076** vs stored
30.12132520557749 (rel diff 1.3×10⁻¹¹), rank 30/30 at the
1×10⁻¹⁰ relative tolerance; per-site blocks 309.2806 / 118.5042
/ 50.9392, agreeing with the stored blocks to ~10⁻¹¹ relative.
The stored tracking primary tracks T_req along the five-site
stencil: gate max direct residual **3.565×10⁻¹⁵** (bit-identical
to stored), σ_min 0.01139040693899883 at that solution vs stored
0.011390408308609587 (rel diff 1.2×10⁻⁷), rank 50/50. *(Rider
G55-R3 binds: both σ_min values are per-solution.)*

**G55-C (the composite total's status).** Read from the stored
C-A primary on the gate's machinery, the composite TOTAL tensor
is Type-I and **four-condition-clean at the sites**: every
NEC/WEC/DEC/SEC channel is ≥ 0 at A1, A2 and A3. The smallest
joint channel is A1's **+1.227388×10⁻⁶** (NEC_t/DEC_t; at A1
δ = 0, so this is the winner's pre-existing joint margin,
reproduced). SEC_trace of the supplied tensor is
**+2.7471977600765363×10⁻¹² at A2** and **+2.2765634169474858×10⁻¹⁰
at A3** — the stored values exactly; zero at the level of the
fit residual, positive as read. Densities are positive at every
site under both definitions in the phase's record (rider
G55-R2): Eulerian T[0,0] = +1.238993×10⁻⁴ / +4.571965×10⁻⁴ /
+1.944449×10⁻³ and eigenvalue ρ = +1.238137×10⁻⁴ /
+4.431937×10⁻⁴ / +1.944243×10⁻³ at A1/A2/A3 — every figure
reproduced by the gate (T[0,0] bit-identical to the phase
checker's record; eigenvalue ρ to all printed digits). Prices
|a|² reproduce bit-identically: family 1 (m = 1)
**0.029172052178672605**, family 2 (m = 0)
**2.0362442383995038×10⁻⁶** — against 410's uncorrected-target
price 0.029266406597128584 (gate re-read from 410's stored
primary, bit-identical): the corrected target is supplied at
essentially the uncorrected price. The A2 density anatomy
reproduces: family 1 alone +5.934×10⁻⁴, family 2 alone
+2.761×10⁻⁶, interference −1.389×10⁻⁴ (T[0,0] basis). *(Fences
§0 bind: sites only; no corrected object; sourcing ≠ a legal
design.)*

**G55-D (the C-S context arm — CONFIRMED).** The single m = 1
family also reaches the corrected target at the three sites:
the stored C-S N = 6 warm-A solution reads, on the gate's
machinery, per-site residuals 7.388×10⁻¹⁴ / 1.508×10⁻¹² /
**1.468×10⁻¹¹** (max 1.468495007452498×10⁻¹¹ vs the phase's
stored 1.468495745267423×10⁻¹¹ — agreement to 5×10⁻⁷ relative,
well inside the registered 1×10⁻⁹ bar). *(Rider G55-R1 binds
every quotation of G55-B/G55-C.)*

**G55-R1 (composite-not-necessary — binding rider to G55-B and
G55-C).** The composite is **not necessary at site scope**: the
single m = 1 family reaches the same corrected target at the
same sites (G55-D). "Composite" must never be quoted as
necessary, and no claim in this set is a claim that two families
were required. The quotable content is that **the SEC correction
δ is expressible at essentially zero extra price** — by the
composite (family 2's price share 2.036×10⁻⁶ of a 0.029174
total) and by the single family alike. The supply side is not
the bottleneck at site scope; the bottlenecks remain the
geometry side's SEC (Phase 419) and the extent (Phase 413).

**G55-R2 (two densities — binding rider to G55-C).** The phase's
record quotes the supplier density under one symbol (ρ_sup) in
two senses: its checkpoint §4 table gives the **eigenvalue ρ**
(+1.238137×10⁻⁴ / +4.431937×10⁻⁴ / +1.944243×10⁻³), while its
checker and results record give the **Eulerian T[0,0]**
(+1.238993×10⁻⁴ / +4.571965×10⁻⁴ / +1.944449×10⁻³). The gate
reproduces both, bit-identically where the record is exact.
**Both are positive at every site**, so the density claim
survives unqualified as to sign; every quotation names which
density it quotes. No deciding number in the set changes under
either definition.

**G55-R3 (per-solution σ_min — binding rider to G55-B and to
every σ_min quotation in this lineage).** A σ_min is a property
of a named solution (G36-C), never of a target or of the mating.
Every quotation names its solution. (Context value, quoted only
with this rider: the C-S solution of G55-D carries σ_min
0.3133085549618151 on the gate's Jacobian — a property of that
solution, stated for the record, not a claim leg.)

## §2 Machinery, controls, laptop admission

**C1 · Builder self-consistency — PASS.** Field-function path vs
the lib's separately written pairwise cross-check on a random
mixed-mass superposition (3 modes m = 1, 3 modes m = 0) at five
random points: max relative T diff **2.1×10⁻¹⁶** ≤ the 1×10⁻¹²
bar. Mode health on all stored primaries: Dirac residuals
≤ 5.3×10⁻¹⁷ (410 Fit A 5.1577036902917074×10⁻¹⁷; 410 Fit B
2.7755575615628914×10⁻¹⁷; 420 C-A 5.2845041577819695×10⁻¹⁷;
420 C-B 1.8683543625880677×10⁻¹⁷ — each reproducing the phase's
stored value exactly where one is stored); norm deviations
≤ 6.9×10⁻¹⁸.

**C2 · δ = 0 reduction, Fit A — PASS.** Phase 420's CTRL-420-A
configuration on gate machinery (410's Fit A primary against the
uncorrected A targets): gate residuals
[8.146052146768652×10⁻¹⁵, 2.763444156047428×10⁻¹³,
2.9659839407219894×10⁻¹²] — ratios 0.9986 / 1.00002 / 1.00000
of stored, each ≤ 2× stored, max ≤ 1×10⁻¹¹; gate σ_min
0.38576181687555705 vs stored 0.3857618146636974 (rel diff
5.7×10⁻⁹, bar 1×10⁻²); rank 30.

**C3 · δ = 0 reduction, Fit B — PASS.** Gate residuals at the
five stencil sites match the stored values at ratios
0.99992–1.00019; gate σ_min 0.015432480413708932 vs stored
0.015432479500623982 (rel diff 5.9×10⁻⁸); rank 50.

**Laptop admission — ADMITTED as corroboration for claims (a),
(b), (c).** Gate lib + driver + targets/primaries staged at
`/home/spark/work/g55root` (g55_lib.py md5
781e9385b1187e865eae84000378de52, identical VM↔laptop); laptop
venv numpy 2.5.5 / scipy 1.18.1 (the VM frame). Claim (a)
rebuild: laptop max diff vs stored T_corr 1.2×10⁻¹⁹ (VM 0.0).
C-A residuals VM↔laptop agree ≤ 5.2×10⁻¹⁷ absolute; C-B
≤ 1.4×10⁻¹⁸; claim (c) T[0,0]/ρ/SEC_trace agree ≤ 4.1×10⁻¹⁷,
with all channels positive on the laptop reads as well.
Records: `gate55/results/g55_laptop_results.json`,
`gate55/results/g55_admission.json`. Deciding reads remain the
VM's.

## §3 Claim (a) — δ construction: SURVIVES

The gate's own build (eigendecomposition of η·T_req from the
stored tensors; timelike eigenvalue identified by its
eigenvector's norm; W = diag(+Δ/4, −Δ/4, −Δ/4, −Δ/4) in that
eigenbasis; δThat = η·V·W·V⁻¹) reproduces the phase's stored
T_corr at **max abs diff 0.0 at every one of the eight sites**
(A1, A2, A3 and the five stencil sites, where δ ≡ 0 exactly).
Δ: A2 gate 2.213556504990559×10⁻⁴ vs the stored construction's
2.2135565049905559×10⁻⁴ (agreement ~10⁻¹⁸); A3
3.3884134221257565×10⁻⁴ vs stored 3.388413×10⁻⁴. ‖δ‖_F:
1.231×10⁻⁴ (A2), 1.695×10⁻⁴ (A3) — the stored values.
SEC_trace(T_corr): 1.0842021724855044×10⁻¹⁹ at A2, 0.0 at A3
(the phase checker's independent rebuild recorded the same
A2 figure). **No-joint-surplus-spend, verified channel by
channel:** the joint-channel differences (T_corr − T_req) at
A2 are [+1.107×10⁻⁴, +5.534×10⁻⁵, +1.107×10⁻⁴, +2.842×10⁻⁵,
+1.107×10⁻⁴, +1.107×10⁻⁴, +1.107×10⁻⁴, +1.107×10⁻⁴] over
(NEC_r, NEC_t×2, WEC, DEC_r, DEC_t×2, DEC_flux) — the minimum,
+2.84×10⁻⁵, is DEC_flux, whose rise is smaller only because δ
also moves the flux; no channel decreases. At A3 the minimum
difference is +8.29×10⁻⁵. The mechanism is as registered: at
both sites all three principal pressures of T_req are negative,
so raising each by Δ/4 raises every NEC/DEC combination while
ρ rises by Δ/4. A2 joint_min 1.3846231146900147×10⁻⁴ →
2.491401367185296×10⁻⁴ (the claimed 1.385×10⁻⁴ → 2.491×10⁻⁴);
A3 joint_min 8.80496715176176×10⁻⁴ → 1.049917386282464×10⁻³.

## §4 Claim (b) — reproduction: SURVIVES

Gate direct residuals at the stored C-A primary against the
gate-built T_corr: [4.056832927431698×10⁻¹²,
7.639565560072827×10⁻¹², 3.496009861987862×10⁻¹⁰] —
**bit-identical** to the phase's stored direct reads. The
primary is under the registered 1×10⁻⁹ bar by a factor ~2.9.
Joint Jacobian (gate FD, central, the registered recipe):
σ_min 30.12132520520076 vs stored 30.12132520557749 (rel diff
1.3×10⁻¹¹); σ_max 16516.92; rank 30/30 at the 1×10⁻¹⁰ relative
tolerance; per-site block σ_min 309.2806007036401 /
118.50418717936904 / 50.939192171895606 vs stored 309.2806006954244
/ 118.50418718151461 / 50.93919217155723. Dirac residual of the
primary's modes: 5.2845041577819695×10⁻¹⁷, the stored value.
Tracking (C-B primary, stencil vs T_req): gate residuals
[2.188×10⁻¹⁵, 3.358×10⁻¹⁵, 3.565×10⁻¹⁵, 3.455×10⁻¹⁵,
2.318×10⁻¹⁵], max bit-identical to stored; σ_min
0.01139040693899883 vs stored 0.011390408308609587 (rel diff
1.2×10⁻⁷); rank 50/50. Both σ_min values are properties of the
named stored solutions (G36-C / G55-R3).

## §5 Claim (c) — the composite total's status: SURVIVES

On the gate's own classifier and channel decomposition, the
stored primary's total tensor is Type-I at A1/A2/A3 and every
channel is ≥ 0. Full minima: A1 — joint_min = SEC_min =
+1.2273882707354079×10⁻⁶ (the δ = 0 site; the target's own
margin, carried through the fit); A2 — joint_min
+2.4914013688623446×10⁻⁴, SEC_min = SEC_trace
+2.7471977600765363×10⁻¹²; A3 — joint_min
+1.049917368373495×10⁻³, SEC_min = SEC_trace
+2.2765634169474858×10⁻¹⁰. The two SEC_trace values reproduce
the phase checker's stored record **exactly**; the joint_min
values reproduce the phase's stored per-site reads to all
printed digits. Densities: both definitions positive at every
site, gate values as quoted in G55-C (T[0,0] bit-identical to
the phase checker's rho_sup record; the eigenvalue ρ identical
to the phase driver's diagnostics record) — rider G55-R2
governs their naming. Prices: |a|² from the stored avecs is
pure arithmetic and reproduces bit-identically (0.029172 /
2.036×10⁻⁶; 410 comparison 0.029266406597128584). The A2
family anatomy on the T[0,0] basis — family 1 alone
+5.933751538533417×10⁻⁴, family 2 alone +2.7608764575874975×10⁻⁶,
interference −1.3893955858578413×10⁻⁴ — reproduces the phase's
checkpoint anatomy (+5.934×10⁻⁴ / +2.761×10⁻⁶ / −1.389×10⁻⁴):
δ is carried mostly by re-arrangement of family 1 plus
interference, exactly as the phase stated. On the stencil the
massless family's share is substantial (phase record
|a|²₂ = 0.011729 of 0.043260; the gate's C-B reads confirm the
tracking solution itself, §4).

## §6 Claim (d) — the C-S context arm: CONFIRMED

The stored C-S candidate (N = 6, m = 1 only, warm-A start;
`phase420/work/p420_cands_fitCS_N6.jsonl`) evaluated against
the gate-built T_corr on gate machinery: residuals
[7.387750901420699×10⁻¹⁴, 1.5076160471281149×10⁻¹²,
1.468495007452498×10⁻¹¹], max 1.468495007452498×10⁻¹¹ vs the
phase's stored 1.468495745267423×10⁻¹¹ (rel diff 5.0×10⁻⁷ —
last-digits class, immaterial against the 1×10⁻⁹ bar). The
single family reaches the corrected target at the three sites.
Consequence, carried as rider G55-R1: the quotable claim of
this set is the **expressibility of the SEC correction at
essentially zero extra price**, not the necessity of the
composite. The phase's own checkpoint stated this context
honestly (§5 of CHECKPOINT420); the gate confirms it on
independent machinery.

## §7 The three amendments — ALL SOUND

**Amendment 1 (the corrected control cap) — SOUND.** From
Phase 410's stored record, its Fit A primary's max direct
residual is 2.9659878908312287×10⁻¹² — **above** the 1×10⁻¹²
absolute cap Phase 420's registration first wrote for
CTRL-420-A, so an exact reproduction of the control
necessarily "failed" the cap as written: the cap was ill-posed
against the record it had to reproduce, exactly as the
amendment states. The corrected form (each residual ≤ 2×
stored, max ≤ 1×10⁻¹¹) is the form Phase 410's own controls
used in substance, and the phase's control reads meet it
(ratios 0.9986–1.00002; the gate's C2/C3 reads meet it too,
§2). The correction was made after the first control run and
before any fit; no target, fit bar, or verdict form moved.

**Amendment 2 (the u_spinor 0/0 guard) — SOUND.** The
singularity is real: in the gate's own independent spinor,
u(p = 0, m = 0) divides by √(E + m) = 0 and returns non-finite
values (verified directly). By code reading, the phase's guard
(`guard_zero_momenta` in `phase420/work/p420_machinery.py`)
triggers only on an exactly-zero momentum in an exactly-zero-
mass mode and replaces it by (1, 0, 0) — the measure-zero
singular set only. Footprint on the deciding reads: **none** —
the gate counted exactly-zero momenta in the stored deciding
solutions (C-A primary, C-B primary, C-S candidates): zero.
The warm-start half of the amendment (unit momenta at exactly
zero amplitude for the empty family) leaves that family's
tensor contribution identically zero, so warm-A still means
"410's solution plus an empty family". No deciding read in
the set passes through the guard.

**Amendment 3 (the completed ladder) — SOUND.** From the
stored records: the original ladder's ε = 10⁻⁶ draw 0 stalled
at **3.2820674985370054×10⁻⁹** (above the 1×10⁻⁹ bar) while
its sibling draw at the same ε reclosed from a fresh start at
6.667373216443225×10⁻¹⁰, and both ε = 10⁻⁹ rungs reclosed
(3.497×10⁻¹⁰, 3.487×10⁻¹⁰) — the stall pattern of an optimiser
stopping artefact at a fat solution set (σ_min = 30.12), as
the amendment states. The completed ladder
(`p420_ladder_completed.json`: fresh seed 4203, tolerances
ftol = xtol = gtol = 1×10⁻¹³, max_nfev 2500, **bar unchanged
at 1×10⁻⁹**) recloses at all four rungs:
[1.2104360712580401×10⁻¹⁴, 7.478104010061205×10⁻¹⁵;
1.2781931870247612×10⁻¹⁴, 2.297751081392394×10⁻¹⁶] — maximum
1.278×10⁻¹⁴, five orders inside the bar. The phase's checker
independently records the completed ladder as all-reclose,
and the as-first-computed verdict string ("DOES NOT SUPPLY",
from the stalled ladder state) is preserved in the results
record beside the completed one. The gate reads the completed
ladder's reclosure values as confirming the registered SS7
verdict leg (ladder re-closing at the unchanged bar).

*Gate-55 records: `gate55/results/` (g55_results.json,
g55_laptop_results.json, g55_admission.json); machinery
`gate55/work/` (g55_registration.md, g55_lib.py, g55_run.py,
g55_laptop.py). Working record: `gate55/GATE55_CHECKPOINT.md`.*

DESK: NO DATA CONTACT.
