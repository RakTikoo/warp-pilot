# CHECKPOINT 410 — SOURCE THE CANDIDATE: the spinor supplier at the Phase 405 winner's sites

Charged at ledger entry 1070. Registration written before computation:
`phase410/work/p410_registration.md` (SS0–SS9, plus Amendments 1–4 —
the CTRL-313 clarification and three recovery amendments, all
disclosed there). Frame of record: VM, programme venv (numpy 2.5.5 /
scipy 1.18.1) + Phase 166 pin. Driver `phase410/work/p410_run.py`
(spinor machinery verbatim from `phase320/work/p320_run.py` lines
48–201 in content). Results `phase410/results/p410_results.json`;
independent checker `phase410/work/p410_check.py` →
`phase410/results/p410_check_results.json` (ALL PASS). Admission:
`phase410/results/p410_admission.json`.

## Verdict

**SUPPLIES AT THE SITES** (gate referral). Fit A primary (N = 6)
direct max residual 2.9659839407219894×10⁻¹² ≤ 1×10⁻⁹ bar; Fit B
primary (N = 12) direct max residual 2.3054719412020823×10⁻¹⁴.
Supplier density positive at all eight site reads. Channel
decomposition: T_sup carries every EC channel of T_req at every
site, SEC included, to ≤ 1.3×10⁻¹².

## Sites and target (Item 1)

Winner vS (K = 9, Phase 405 Stage-C lineage, D-curve screen at
criterion) loaded exactly as `p405_confirm.py` loads it; asserted
equal to Gate-50's stored knots at diff 0.0:
[0.40243113547885484, 0.23237610808870765, 0.10110504581235646,
0.030274386301308052, 0.021559512630984955, 0.01297222477301449,
0.007865452045132022, 0.0035285750792539276, −0.00043513901545560714].

- A1 (joint argmin): (−17.827002016737087, 0.1739363226225222,
  1.8812104787714563), r = 17.926829268292682 (Gate-50's stored
  argmin point).
- A2 (SEC argmin): from the winner's own `set_read405` aux arrays
  (argmin of `aux['R']['sec']` over the 41×162 grid):
  (−12.005940133720896, 0.11714078870496394, 1.2669376693766954),
  r = 12.073170731707318, sec −2.2135565049905559×10⁻⁴.
- A3 (peak): (10.0, 0, 0), r = 10.
- B stencil: A1's direction at r = 16.926829268292682,
  17.426829268292682, 17.926829268292682, 18.426829268292682,
  18.926829268292682.

CTRL-TGT-410: joint +1.2273852081052888×10⁻⁶ (diff 0.0 vs stored),
sec_min −2.2135565049905559×10⁻⁴ (diff 3.0×10⁻¹⁹), NEC at A1
+1.2273852081052888×10⁻⁶ (diff 0.0), worst-null at A1
+7.282191364112375×10⁻⁷ (diff 0.0), A1 Type-I true.

## Controls

- CTRL-320: maxR 8.230813708013984×10⁻¹⁴ (stored identical);
  σ_min 0.0003994300112181778 vs stored 3.994300907411277×10⁻⁴,
  rel. diff 1.99×10⁻⁷ (bar 1%). PASS.
- CTRL-313: maxR 3.253339860306391×10⁻¹³ = stored (diff 0.0).
  σ_min leg per registration Amendment 1: the record's 0.0272 is
  Gate-34's value at Gate-34's refit solution (Phase 313's driver
  computed no Jacobian). Forward-difference FD at Gate-34's stored
  theta (`gate34/results/g34_item3a.json` N6_winner): σ_min
  0.027165249667980257 vs stored 0.027165249637030254 (rel.
  ~1.1×10⁻⁹); σ_max 3966.2716384200294 vs stored
  3966.2716384255486. Central-difference at the same theta:
  0.027173817517817934. At 313's stored solution: σ_min
  0.0347527502565207 (per-solution, G36-C). PASS.
- Laptop admission (SS6): mirror `/home/spark/work/p390root`,
  `p405_lib.set_read405` on the winner's knots: joint
  1.22738520810537×10⁻⁶ (diff 8.1×10⁻¹⁷), sec_min
  −2.2135565049905622×10⁻⁴ (diff 6×10⁻¹⁹), rho_min identical,
  argmin radii identical, Type-I fraction 1.0. ADMITTED for
  screening; deciding reads VM.

## Fit A (sites A1/A2/A3, 30 residuals, m = 1)

| N | matched | best maxR | best start |
|---|---------|-----------|------------|
| 4 | 0/6 | 9.995×10⁻⁴ | rand0 |
| 5 | 4/6 | 2.651×10⁻¹³ | rand5 |
| 6 | 8/9 | 2.966×10⁻¹² | rand4 |
| 8 | 8/9 | 6.682×10⁻¹¹ | rand1 |
| 12 | 3/9 | 1.029×10⁻¹⁰ | rand6 |

Primary: N = 6 arm's best (rand4). Direct residuals
[8.146×10⁻¹⁵, 2.763×10⁻¹³, 2.966×10⁻¹²] (checker-recomputed,
dmaxR 4.0×10⁻¹⁸). Joint Jacobian (central FD, h = 1×10⁻⁶·max(1,|θ|),
320 verbatim): σ_min 0.3857618146636974, σ_max/rank: rank 30 at
10⁻¹⁰ relative. Per-site block σ_min: A1 202.78818227797214,
A2 80.6667621143565, A3 35.29252647881794. D-a: per-site R equal to
the direct residuals, all ≤ 1×10⁻⁹. Dirac residual 5.1577036902917074×10⁻¹⁷.
Perturbation ladder (best of warm/fresh per draw): ε=10⁻¹² →
2.968×10⁻¹², 2.967×10⁻¹²; ε=10⁻⁹ → 3.604×10⁻¹³, 5.013×10⁻¹²;
ε=10⁻⁶ → 5.494×10⁻¹⁴, 5.191×10⁻¹²; ε=10⁻⁴ → 3.389×10⁻¹¹,
6.877×10⁻¹². All rungs reclose. Pricing: |a|² 0.029266406597128584;
per-site implied s²: A1 0.029266406591731877, A2
0.02926640651632981, A3 0.02926640668911892. Supplier densities:
[+1.238993×10⁻⁴, +3.956517×10⁻⁴, +1.859720×10⁻³] — all positive.
m = 0 secondary: not triggered (m = 1 arms matched).

## Fit B (stencil, 50 residuals, m = 1)

| N | matched | best maxR | note |
|---|---------|-----------|------|
| 6 | 0/2 | 4.542×10⁻⁶ | arm truncated at 2/6 (Amendment 2) |
| 8 | 0/2 | 7.667×10⁻⁷ | arm truncated at 2/9 (Amendment 3) |
| 12 | 9/9 | 2.305×10⁻¹⁴ | warm |

Primary: N = 12 warm. Direct residuals [9.110×10⁻¹⁵, 1.692×10⁻¹⁴,
2.305×10⁻¹⁴, 2.095×10⁻¹⁴, 7.928×10⁻¹⁵] (checker dmaxR 3.1×10⁻¹⁸).
Joint σ_min 0.015432479500623982, rank 50/50. Per-site block σ_min:
198.93050908330537, 209.39586421757318, 232.0208745230703,
258.72244944890787, 292.2304971308097. D-a all ≤ 1×10⁻⁹. Dirac
residual 2.7755575615628914×10⁻¹⁷. Ladder: ε=10⁻⁹ → 5.350×10⁻¹⁴,
3.570×10⁻¹⁴; ε=10⁻⁶ → 5.801×10⁻¹⁴, 5.365×10⁻¹⁵. All reclose.
Pricing: |a|² 0.021228149358339266; per-site s² 0.0212281491…–
0.0212281499…. Supplier densities: [+1.405987×10⁻⁴, +1.319327×10⁻⁴,
+1.238993×10⁻⁴, +1.166924×10⁻⁴, +1.101573×10⁻⁴] — all positive.

## Decomposition (Type-I eigen-channels, req vs sup)

Channel margin differences (sup − req) are ≤ 1.34×10⁻¹² at every
site (checker recomputation: max diff 0.0 against the stored
tables). Deciding values:

| site | req ρ | req p_r | req SEC_min | req joint_min | worst margin diff |
|------|-------|---------|-------------|---------------|-------------------|
| A1 | 1.238137×10⁻⁴ | 1.335803×10⁻⁵ | +1.227385×10⁻⁶ | +1.227385×10⁻⁶ | 2.6×10⁻¹⁵ |
| A2 | 3.878548×10⁻⁴ | −1.798439×10⁻⁴ | −2.213557×10⁻⁴ | +1.384623×10⁻⁴ | 3.9×10⁻¹³ |
| A3 | 1.859533×10⁻³ | −9.790362×10⁻⁴ | −3.388413×10⁻⁴ | +8.804967×10⁻⁴ | 1.3×10⁻¹² |
| B−1.0 | 1.405470×10⁻⁴ | 3.434213×10⁻⁶ | +2.042875×10⁻⁶ | +2.042875×10⁻⁶ | 1.1×10⁻¹⁴ |
| B−0.5 | 1.318839×10⁻⁴ | 7.434170×10⁻⁶ | +1.540743×10⁻⁶ | +1.540743×10⁻⁶ | 1.1×10⁻¹⁴ |
| B+0.0 | = A1 | = A1 | = A1 | = A1 | 3.7×10⁻¹⁴ |
| B+0.5 | 1.166026×10⁻⁴ | 1.453181×10⁻⁵ | +1.325351×10⁻⁶ | +1.325351×10⁻⁶ | 2.1×10⁻¹⁴ |
| B+1.0 | 1.100729×10⁻⁴ | 9.875967×10⁻⁶ | +1.262697×10⁻⁶ | +1.262697×10⁻⁶ | 1.4×10⁻¹⁴ |

Both tensors Type-I at every site. The supplier expresses the SEC
channel's demand exactly at the sites where it binds (A2: the
winner's SET SEC argmin; A3: SEC trace combination −3.388413×10⁻⁴).
It sources T_req as it stands — SEC violation included; sourcing ≠
curing (see memo).

## Execution record

Six driver executions: (1) aborted at the CTRL-313 σ_min leg as
designed (Amendment 1 followed); (2) died silently during Fit A
N = 6 rand0 (shared-VM contention, no traceback) after controls,
Item 1, arms N = 4/5 and N = 6 warm; (3) recovery with per-start
JSONL persistence — reproduced every banked value identically,
died to a service restart during Fit B N = 8 rand0; (4) recovery,
Fit B N = 6 arm truncated (Amendment 2); (5) recovery, Fit B N = 8
arm truncated (Amendment 3), completed all fits and primaries,
crashed in the Fit A perturbation ladder on the residual-closure
TypeError (Amendment 4, one-line np.array fix); (6) final recovery:
52 candidates resumed, diagnostics and decomposition completed,
verdict emitted. Final execution wall 4119 s. All candidates
persist in `phase410/work/p410_cands_*.jsonl` (52 starts);
primaries in `phase410/work/p410_fitA_primary.json` /
`p410_fitB_primary.json`; targets in `phase410/work/p410_targets.json`.

## Fences (on the face)

Site mating ≠ field on the extent (coverage: extent line
346/357/368/362; candidate extent audit: Phase 409, separate). The
mating sources the winner's tensor including its SEC violation —
no no-exotic-matter claim for any sourced design. σ_min quoted
per-solution only (G36-C). Novelty NONE for the mating method
(Martín-Moruno & Visser 2021, Gate-25). No ledger append, no
successor launched, no user contact by this coordinator; the gate
referral goes to the parent with this checkpoint.

DESK: NO DATA CONTACT.
