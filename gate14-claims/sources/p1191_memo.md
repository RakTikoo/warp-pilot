# P119-1 memo — Gate-style replication of the P108-5 QET verdict

**Verdict: REPLICATED.**

Fresh machinery, written from Xun & Ren (arXiv:2410.04919) and the
inherited P72-2/P106-3 accounting — Phase 108's code was not read,
imported, or adapted, and Phase 108's results were opened only after
the fresh numbers existed — reproduces every one of the 30 stored
rows of `p1085_results.json` inside the registered replication
standard, with all three controls passing before any deciding row
was believed. The τ-convention ruling is stated below and in the
run record. Checker: `work/p1191_checker.py` — ALL PASS.

## Deciding numbers (fresh vs Phase 108 stored)

Worst relative differences over all 30 rows: E_out, E_prep^(marg),
E_net,B, E_in, price per unit — **0.0** (bit-exact at float64 print
precision); τ₀ — 1.0e-9; τ_marg — 1.8e-9; R — 1.0e-9. Registered
bars were 1e-6 (energies) and 1e-4 (τ, R): the replication lands
three to five orders of magnitude inside them.

Both-convention bar-clearers (R(τ₀)/R(τ_marg), fresh = stored to
the digits shown): (6,1,0.5) 2.2536/3.1959; (8,1,0.5) 3.6230/4.6807;
(8,1,1) 6.5180/11.0540; (10,1,0.5) 4.2433/5.1947; (10,1,1)
9.7931/14.3367. τ₀-only row (10,1,2): R(τ₀) = 5.13441, and the fresh
machinery also finds **no return of S(t) to +E_prep^(marg) for
t ≤ 30** there, as stored. Convention-split rows replicate AS split:
(5,1,0.5) 0.98712/1.51323 and (6,1,1) 0.52280/8.88452 — below 1 on
τ₀, above 1 on τ_marg, on both sides of the comparison. First
negative row (5,1,0.5): E_net,B = −0.04140061640580686, identical.
Exactly the registered eight rows have E_net,B < 0. Price per unit
over the 30 rows: 5.5909–130.1920 (the registered 5.59–130.19 line
stands); over the eight negative rows: 5.7586–28.3253.

## Controls

- **C1** (N=2 vs P72-2 stored, all three r): E_out, E_prep^(marg),
  E_net,B bit-exact; τ₀ within 1.2e-10 (bar 1e-6). PASS.
- **C2**: constructed H's ground eigenvalue ≤ 2.7e-15 in magnitude
  over all rows (bar 1e-12); Eq. (3) overlap ≥ 1 − 7e-16
  (bar ≥ 1 − 1e-10). PASS.
- **C3**: τ_marg at (2,1,0.5): fresh 0.83853305002 (dense route) vs
  registered 0.838533050344258 — 3.2e-10 (bar 1e-6); the derived
  pair-block path gives 0.8385330503442567 (1.3e-15). PASS.
- Internal cross-checks on every row: simulated E_out vs Eq. (11)
  ≤ 6.7e-16; simulated E_in vs Eq. (6) ≤ 3.6e-15; E_prep^(marg) as
  4k²/D vs as Tr[ρ_marg S_op] ≤ 1.3e-15.

## Machinery note (on the face of the result)

Dense Kronecker route (`p1191_eval.py`, full eigendecomposition)
produced 27 of the 30 rows. Under severe machine contention (load
average ≈ 38 on 1.5 CPUs; several launches killed by the runtime),
the three N=10 rows were completed by `p1191_lean10.py`: identical
dense H and identical explicit protocol simulation for every energy
read, ground state by sparse Lanczos eigendecomposition, and S(t)
by the derived pair-block exact exponentiation. The lean route's
(10,1,0.5) and (10,1,1) τ reads were verified against the dense
route's reads for those rows (agreement ≤ 1.2e-10) before its
(10,1,2) read was believed; its energies are bit-identical to the
dense route's. One encoding difference, not a discrepancy: for
(10,1,2) the fresh file stores R(τ_marg) = 0.0 (no-return encoding)
where Phase 108 stores null; τ_marg itself is null on both sides.

## τ-convention ruling

**τ_marg is the duration of the inherited FR-net ratio.** P72-2 §4
references the Ford–Roman bound to the uncorrelated vacuum and
reads Bob-sector energy relative to the uncorrelated (R-marg)
reference, not the entangled ground; the priced pulse is therefore
the excursion below that reference level, which ends when S(t)
returns to +E_prep^(marg). τ₀ is §4's τ_pulse of the FR-raw read —
a different read, referenced to the entangled-ground zero.
Under the other convention (τ₀) the claim still stands at the
deciding rows: the five both-convention rows keep R(τ₀) > 1 and
(10,1,2) keeps R(τ₀) = 5.134; only the two split rows fall below 1.
Bar met at seven rows under τ_marg, six under τ₀ — the reopening
is not convention-dependent at its deciding rows.

## τ(N) asymptotics (m = 1; derived evolution, validated vs dense)

Route: exact pair-block exponentiation derived from Eqs. (1)–(3),
(7), (10) (derivation in the run record; the conditional-unitary
amplitudes collapse to B₀(x) = uχ_x, B₁(x) = vχ_{¬x}), giving S(t)
as an O(N) binomial-weighted trig sum — honest reach N = 200,
validated against the dense machinery at N ∈ {3,5,8,10} (τ to
≤ 1.2e-10) and against P72-2 at N = 2 (τ₀ to 5e-17). Energies at
extended N from the printed closed forms.

Read: **τ falls with N** for both r and both conventions, after the
small-N plateau (τ₀ ≈ 0.23): r = 0.5, τ₀ = 0.2265 (N=5), 0.1831
(N=10), 0.1385 (N=20), 0.0466 (N=200); τ_marg tracks τ₀ closely and
the two converge at large N. **|E_net,B| grows and saturates**
(r = 0.5: 0.0414 → 0.2202 → 0.4042, asymptote ≈ 0.41; r = 1:
asymptote ≈ 1.20). **R's growth is therefore not carried by
|E_net,B| alone**: R rises only while |E_net,B|'s growth outruns
the falling τ — peak R(τ₀) ≈ 4.67 at N = 16 (r = 0.5) and ≈ 13.76
at N = 20 (r = 1) — then falls as τ's decline dominates (r = 0.5:
R(τ₀) = 1.98 at N = 200; r = 1: 6.76 at N = 200, still > 1).

## Scope (C12)

A sourcing-accounting result in a finite spin model, resource
counted (price line above stands against it). No "energy source",
no field claim, nothing FTL. INTERNAL only; nothing uploaded,
nobody contacted. On this REPLICATED verdict the checkpoint's
registered claim block may be filled and the claim routed to the
parent for a full Gate, under the ruling's convention (τ_marg).
