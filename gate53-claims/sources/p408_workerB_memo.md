# Phase 408 — Worker B memo (pool search: Arms A + B)

Scope executed on the laptop pool (screening machinery only), per
CHECKPOINT408.md **including Amendment A-408-1 (binding)** and the
Worker B brief. Code: `work/p408_pool_*.py` (VM copies; pool copies in
the pool tree's `phase408/work/`, state in pool `~/work/p408/state`).
Record: `results/p408_search.json` + `results/p408_pool_*.json`
(pool records copied back verbatim) + `results/p408_ram_log.txt` +
`results/p408_pool_log_*.log`. CHECKPOINT408.md and
p408_controls.json not edited; no ledger append; no home verdict
audits (Worker C scope); no external contact.

**ALL numbers in this memo and in `p408_search.json` are SCREENING
numbers** (hybrid GPU evaluator / CPU clone algebra on screening
point sets under the EXTENDED mask [2.234381, 27.265413]).
Screening is never a verdict; every harvested candidate is
provisional until Worker C re-judges it at home.

DESK: NO DATA CONTACT (this worker's objects are prescribed
configurations from the programme's own record).

## Machinery

392's pool drivers copied to `p408_pool_` copies with paths adapted
(state dir → `/home/spark/work/p408/state`; work path → the pool's
`phase408/work`; the specs' lib string `"p392_16"` maps to
`p408_pool_p408_lib16.py`, a copy of
`phase392/work/p392_pool_p392_lib16.py` — round-trip diff-verified:
undoing the path/name substitutions reproduces the 392 files
byte-for-byte for de / screen16 / powell / harvest / lib16).
Validate and recalib drivers were adapted to the 408 arms (see
below). The full `phase408/work/` tree was staged to the pool and
all 15 files' md5s verified pool-side against home before any
launch; the one later patch (recalib, below) was re-staged and
md5-re-verified.

## Validation gates C-408-6 — BOTH PASS

- **(a) Arm A spot re-validation** (5 shared candidates incl. the
  staged population's `best_y`): GPU vs pool-CPU clone worst margins
  agree to max |Δ| = **1.16×10⁻¹⁴** (bar ≤ 1×10⁻⁷); β_crit brackets
  agree for all 5 — the staged `best_y` reads **0.191015625** on
  both paths. (`p408_pool_p408_validate_a.json`)
- **(b) Arm B full re-validation at the widened box** (20 shared
  candidates incl. Arm B's y_his-equivalent and the clipped RW-5
  embedding): max |Δ| = **2.29×10⁻¹⁴**; brackets agree. The clipped
  embedding reads 0.192578125-class on both paths (see C-408-5).
  (`p408_pool_p408_validate_b.json`)
- No CPU-clone fallback was needed for either arm.

## Recalibration C-408-4 — PASS on both arms (pre-search gate)

On each arm's 16-mode recalib instrument (extended mask, union set
n_pts = 3,640 on both arms):

- **Step design (c = 0 with y_his's own a/q/r_m, sha `6db0afbf…` —
  the y_his-equivalent of every prior phase's recalib):**
  **0.136328125**, bracket [0.1359375, 0.13671875] (contains 0.1363,
  width 0.00078), GPU union = CPU extended, **both arms**.
- **Convicted Stage-1 artefact** (16-mode LS embedding, sha
  `8501b200…`): **0.120703125 ∈ [0.115, 0.127]**, both arms.

**Naming collision disclosed on the face (not an instrument
failure).** The arm DE specs name a different vector
"y_his_equivalent": Arm A's seed 0 (c = 0 with the **E2-1
embedding's** a/q/r_m, sha `be13909e…`) and Arm B's seed 0 (c = 0
with **RW-5's** a/q/r_m, sha `c8cb0ed4…`). Both were ALSO read on
the recalib instrument, as tasked, and both read
**at_or_below_lo (≤ 0.10)** on GPU union and CPU extended alike.
Anatomy: a foreign a-block was tuned jointly with its grading;
setting c = 0 while keeping it produces a different, worse design —
it is not Procaccia's step design, whose a/q/r_m are y_his's own.
That the instrument is the registered one is proven by the
simultaneous exact reproduction of the step design
(0.136328125-class), the artefact (0.120703125), the staged
population's stored fitnesses (validate A: pop members read
0.191015625 / 0.175390625 / 0.178515625, matching the staged
state's stored values digit-for-digit), and the RW-5 embeddings
(0.192578125-class). The recalib driver was patched to read all of
these on the face (patch re-staged, md5 re-verified; no bar was
adjusted — the C-408-4 bar was applied to the step design, exactly
as in 386/391/392).

## C-408-5 POOL GATE — PASSED (clipped seed screens lossless)

The seed of record — **"RW-5 embedded, box-clipped at c13"**
(sha256 `d228c82e…d69f`) — reads on the recalib instrument:
GPU union **0.192578125**, CPU extended **0.192578125** (bracket
[0.1921875, 0.19296875] on both). The stored float is
0.19257812500000002 — the bisection centre 0.5·(lo+hi), 1 ulp above
the literal, the identical value the Arm B DE driver itself
produced for this vector (gen-0 best and y_ref read). At screening
resolution this **is** exactly 0.192578125; the gate is recorded
PASSED and seed continuity holds. Anatomy record: the **unclipped**
embedding (sha `a0201be1…`) reads identically (0.192578125-class on
both paths) — the c13 clip costs nothing at screening resolution.

## Arm A — RESUME (R-16's DE, finished) — COMPLETE, yield +0.00234

**Resumption cross-check PASSED.** The driver printed
**n_pts = 3,640** (the staged state's count) and gen-0 best
**0.191015625 exactly**. The driver's gen-0 state file was
overwritten by gen 1 (~57 s/gen) before the first rsync, so the
full 64-member agreement was completed by an independent re-read
of all 64 staged members on the identical union instrument
(`p408_pool_p408_gen0check_a.json`): **64/64 exact (max abs
deviation 0.0), 64/64 brackets equal**, best exactly 0.191015625.

- **DE: 107 generations, 6,912 β_crit evals, 7,207 s — ran to the
  full +120 min cap** (state done=True). Trajectory: best flat at
  the seed 0.191015625 through gen ~20, rose to **0.191796875** by
  gen 24, then to **0.193359375** by gen 74 and flat to the cap;
  population mean 0.17787 (staged, gen 106 of 392) → 0.18586
  (gen 11) → 0.18990 (gen 27) → 0.19120 (gen 50) → 0.19277
  (gen 107). **The finished finer basis DID pay at screening:
  +0.00234375 over its own seed, +0.00078125 over the standing
  best RW-5 (0.192578125)** — the 392 truncation was hiding a real
  lift (contrast 392 Arm T, where more time at 12-mode bought
  nothing).
- **Powell** top 3 distinct (hashes `59abd692…`, `244992ca…`,
  `c598034e…`, all starts at 0.193359375): 507 / 502 / 507
  objective evals — **no improvement**, all incumbents at
  0.193359375.
- **Harvest: 6 distinct candidates, ALL at CPU screening
  0.193359375** — `59abd692…`, `244992ca…`, `c598034e…`,
  `8d92bee8…`, `d7ec16e8…`, `6461827f…`. Control member: the
  staged `best_y` (`e28f083f…`) was appended as a harvest
  candidate and re-read at 0.191015625; it is in the harvest
  record's `all_candidates` (not in the top-6 distinct), marked
  as control in `p408_search.json`.
- Screening anatomy of the DE best (`59abd692…`): sits on the
  original box edges c idx 0 = +2.25 and c idx 10 = −2.25.

## Arm B — COMBINED (16-mode × widened box) — COMPLETE, DE flat, Powell +1 rung

- **DE: 140 generations, 9,024 β_crit evals, 7,232 s — ran to the
  full 120-min cap** (done=True). Gen-0 best = the clipped seed
  itself at 0.192578125, and **the DE best never passed its seed
  in 140 generations** (final population argmax is still the
  clipped seed, hash `d228c82e…`). The population mean was still
  rising at the cap: 0.10203 (gen 22) → 0.10782 (gen 58) →
  0.15458 (gen 89) → 0.18236 (gen 113) → 0.19034 (gen 140) —
  with only 2 seeds in 30 dims the population converged far more
  slowly than Arm A's resumed 64 (the 392 R-16 pattern); the
  honest statement is that the DE bought nothing within its cap
  while still converging, not that the combination is empty.
- **Powell** top 3 distinct (idx 1 = the clipped seed `d228c82e…`
  at 0.192578125; idx 62 `fd5ca3c9…` at 0.192578125; idx 3
  `2c83e43c…` at 0.191796875): de0 (from the clipped seed)
  **improved to 0.193359375** (498 evals, incumbent tracking);
  de1 / de2 no improvement (529 / 510 evals).
- **Harvest: 6 distinct candidates** — `b2527d10…` at
  **0.193359375** (the Powell de0 product), the clipped embedding
  `d228c82e…` at 0.192578125 (**control member, naturally in the
  top-6 distinct**, marked in `p408_search.json`), `fd5ca3c9…`
  and `174f7775…` at 0.192578125, `dbc7214f…` and `a86767e8…`
  at 0.191796875.
- Screening anatomy of the Arm B winner (`b2527d10…`): it is the
  clipped seed polished — c idx 0 moved 2.4882 → **2.5477**
  (inside the widened ±3.375, beyond the old ±2.25); c idx 11
  unchanged at the seed's −2.1134 (the widened switch-region
  coordinate was not used further); c idx 13 remains on its
  −2.25 clip bound. The combination's screening yield over RW-5
  (+0.00078125) came through Powell on the seed, not through the
  DE population.

## Pool priority rule — honoured, no yield events

- Every launch at ≥ 6 GiB available (validation/recalib launches
  ~11.8 GiB; DE A ~11.7 GiB; DE B 11,774 MiB). Footprint within
  the proven envelope (pop 64, chunk 8). DE checkpoints every
  generation; states rsynced home at least every ~25 min.
  Phase 362 was never disturbed — its driver stayed live
  throughout under its own supervisor.
- Watchdog (`p408_ram_log.txt`, 132 samples): **no
  POOL-PRIORITY YIELD fired.** Four isolated samples below
  2.5 GiB (76 / 176 / 981 / 2,366 MiB), never 3 consecutive,
  each recovered by the next sample — the same transient
  phenomenon 392 recorded. No job was killed, no OOM.
- Total pool search wall: DE 14,439 s (4.01 h) + Powell
  ~616 s (A) / ~600 s (B) parallel triples + harvests < 30 s +
  validations/recalibs/gen0-check ~10 min — inside the
  registered 4.5 h pool budget across both arms.

## Incidents (all disclosed, no work lost)

1. **SSH broken pipes** on several launch/monitor connections
   (the WSL proxy dropped the session after the pool-side
   `nohup` launch had already succeeded). Verified each time by
   a fresh connection: every launched process was running.
2. **Pool SSH host key changed 3×** (WSL restarts), each time
   restored with the standing fix (`ssh-keygen -R
   100.71.86.14` + `StrictHostKeyChecking=accept-new`).
3. **Watchdog died/exited 3×** in VM runtime restarts and
   host-key episodes (starts logged 06:45Z, 08:50Z, 10:37Z;
   the 08:49Z "no p408 processes; watchdog exit" was the
   watchdog's own SSH failing during a host-key change and
   misreading the empty result as no processes — the Arm B DE
   was alive pool-side throughout). Relaunched each time;
   gaps covered by direct `free -m` checks at every launch.
   The RAM log's per-sample label reads `p392_procs` (cosmetic
   leftover of the adapted 392 script); the pgrep pattern is
   `p408_pool`.
4. **Gen-0 state overwrite** (Arm A cross-check): the driver's
   gen-0 checkpoint was replaced by gen 1 before the first
   rsync; the 64-member agreement was instead proven by an
   independent re-read on the identical instrument (64/64
   exact) — see Arm A.
5. **First gen0-check run failed** with a NameError (the
   extracted recalib head lacked `batched_beta_crit`, which is
   defined below the cut point in the recalib driver); fixed by
   including the function verbatim, re-run clean.
6. **First Powell-B launch attempt was interrupted** by a
   service restart before the per-start specs landed pool-side;
   verified absent, re-synced (md5-verified), relaunched clean.
7. A harmless `RuntimeWarning: invalid value encountered in
   log` from the lib16 builder (r → 0 guard) appears in every
   pool log, exactly as in 392's runs; it affects no read.

## Bottom line (SCREENING ONLY)

- C-408-6 validation: Arm A PASS (1.16×10⁻¹⁴), Arm B PASS
  (2.29×10⁻¹⁴). C-408-4 recalibration: PASS both arms
  (step design 0.136328125-class; artefact 0.120703125).
  C-408-5 pool gate: **PASSED** — the clipped seed
  ("RW-5 embedded, box-clipped at c13") screens at exactly
  0.192578125; the unclipped embedding reads identically.
- **Arm A (resume): best screening 0.193359375** — the finished
  16-mode DE passed its seed at gen ~24 and RW-5's level by
  gen 74; 6 harvest candidates at 0.193359375.
- **Arm B (combined): DE flat at its seed for 140 gens (mean
  still rising at cap); Powell on the seed recovered one rung
  to 0.193359375**; 6 harvest candidates, top at 0.193359375,
  control (clipped embedding) at 0.192578125 in the top-6.
- All 12 harvested candidates (6 per arm) are staged in
  `results/p408_search.json` for Worker C's home re-judgement.
  Nothing here is a verdict; the standing home-verified best
  remains β = 0.192578125 until C rules.
