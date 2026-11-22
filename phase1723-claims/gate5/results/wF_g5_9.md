# Gate-5 — W-F report: G5-9 (P19-1) Bimetric two-ground kill anatomy

Worker W-F, Gate 5. Date 2026-11-21/22 PT. Standards: float64
everywhere; hedges intact; nothing uploaded, no external contact.
Source record: `phase19/CHECKPOINT19.md` §P19-1, memo
`phase19/results/p191_memo.md`, data `p191_solve.json`,
`p191_audit.json`, `p191_gate.json`, `p191_summary.json`,
`p191_coeffs.npz`; Phase-14 origin `phase14/CHECKPOINT14.md` §P14-3.

## Verdicts (summary)

- **Correctness: REPRODUCED.** Every deciding number of
  sub-claims (a)–(d) and of the registered machinery gate was
  re-derived with fresh, independent code and lands on the
  phase's values within finite-difference-order noise (my
  discretisation is 2nd-order where the phase's is 4th-order).
  Two low-end range endpoints differ slightly under my stricter
  non-Type-I counting (T_req DEC floor 0.828 vs the stated 0.85;
  Θ_f = 0 distance floor 0.997 vs the stated 0.999); neither
  touches any bar, sign, or verdict clause. Details and the
  exact per-cell numbers are below.
- **Novelty: PARTIALLY KNOWN.** The qualitative heart of the
  claim — in Hassan–Rosen bimetric gravity the exoticity cannot
  be removed, only moved between the two sectors — is already
  published as a general theorem about the *interaction*
  effective stress-energy tensors: Baccetti, Martin-Moruno &
  Visser, arXiv:1206.3814 (JHEP 1208 (2012) 148). What is new as
  a stated result is the warp-shell anatomy itself: no
  Hassan–Rosen warp-drive computation exists in the searched
  literature at all, and no published work states the pooled
  closure / t-component floor / Θ_f-as-defined-matter audit for
  a moving superluminal shell. Exact restated wording in §4.
- **Gate verdict: UPLOAD-READY AFTER RESTATEMENT** (restated
  novelty framing supplied in §4; the correctness content needs
  no restatement).

## 1. Method — the independent second path

Fresh code, written from the claim statement and the run-record
definitions only:

- `gate5/wf_g59_lib.py` — my machinery. Differences from the
  phase's machinery, by construction: the principal square root
  S = √(g⁻¹f) is taken per point with `scipy.linalg.sqrtm`
  (phase: batched eigendecomposition); Christoffel symbols from
  2nd-order central finite differences of the metric (phase's
  `verify_metric`: 4th-order stencils); the Einstein tensor from
  2nd-order central differences of Γ (phase: nested 4th-order);
  the Bianchi divergence assembled directly from
  ∇^aC_ab = ∂_aC^a_b + Γ^a_{ad}C^d_b − Γ^d_{ab}C^a_d with the
  claim's relative scale (max of the three-term cancelling scale
  and the per-axis partial scale); the Eulerian tetrad rebuilt
  from the ADM split; energy-condition margins from my own
  mixed-tensor eigenvalue code, with NEC at non-Type-I points
  by my own 1024-direction Fibonacci null sampling and
  non-Type-I points counted as WEC/SEC/DEC violations
  (Hawking–Ellis classification — stricter than the phase's
  sampled-margin fill where they differ).
- `gate5/wf_g59_audit.py` — the deciding run; outputs
  `gate5/wf_g59_numbers.json`. Run with
  `~/workspace/warp-pilot/venv/bin/python`.
- Shared DEFINITIONS only (as authorised): the stored
  coefficient vectors in `p191_coeffs.npz` (the configurations
  being audited); the bed's g-metric factory (Finalist-A shell,
  `shell.py` via the p103 bed parameters — the definition of
  the g configuration); the volume point set (phase14 cache
  `pts_v`/`r_v`, 1270 pts); the per-β tolerances
  (1.813e-6 / 5.163e-5 / 6.569e-5); the registered collocation
  seed (191191, 128 pts) and the phase's fresh-point seed
  (191777, 64 pts). Stored result JSONs were read only to
  compare at the end. The phase's own solver was not re-run;
  no phase audit code was imported.
- Pre-checks of my machinery (validation, not deciding
  numbers): my C tensor vs the phase's `C_fast` on sample
  points agrees to 1.1e-13 (g-side) / 1.6e-12 (f-side); my
  Einstein tensor vs `verify_metric.einstein_at_points` agrees
  to 5.1e-6 (g) / 3.5e-4 (f) absolute at h=0.15 — consistent
  with the 2nd- vs 4th-order stencil difference; Minkowski
  gives G ≡ 0 exactly.

## 2. Machinery gate — the C_f density identity, independently

Claim: √(−g)Σₙbₙeₙ(S) = √(−f)Σₘb₄₋ₘeₘ(S⁻¹), verified by the
phase to 2.98e-13, with C_f = C_fast(f, g, ℳ², b_rev).

My test: 6 generic (g, f) pairs × 8 bed points (g from the
β=1.5 bed, f from the stored PRIMARY D1 field, trials 1–5 with
additional random symmetric perturbations of f so f is not the
solved field), random b ∈ [−2, 3]⁵, my own eₙ code and my own
scipy-sqrtm S.

- **Density identity worst relative error: 3.8e-15** — the
  identity holds, better than the claimed 2.98e-13 (different
  sample; same conclusion).
- Orientation control: with b NOT reversed the same identity
  fails at worst relative error **0.707** — the reversal is
  load-bearing, as claimed.
- My own action-FD gate for C_f (central FD of √(−f)·L_int^f
  w.r.t. f^μν, ε=1e-6, symmetric-E convention
  ∂dens/∂f^μν = √(−f)·C_f,μν): **max relative error 8.2e-8**
  over 4 points (phase: 7.74e-8 main / 1.17e-7 alt; bar < 2%).
  PASS, independently.

## 3. Correctness — my deciding numbers, per sub-claim

### (a) Pooled Bianchi closure + D0 controls

My constraint audits (collocation points, pooled / t-component
rel_med, h=0.3 / 0.15), phase values in brackets:

| row | pooled (mine) | pooled (phase) | t (mine) | t (phase) |
|---|---|---|---|---|
| PRIMARY (3,0) β=1.5 | **0.0189 / 0.0181** | 0.0189 / 0.0181 | 0.0319 / 0.0276 | 0.0318 / 0.0276 |
| (3,0) β=1.1 | 0.0262 / 0.0255 | 0.0261 / 0.0257 | 0.0381 / 0.0342 | 0.0382 / 0.0348 |
| (1,0) β=1.5 | **0.0176 / 0.0179** | 0.0173 / 0.0179 | 0.0762 / 0.0677 | 0.0763 / 0.0730 |
| (0,0) β=1.5 | 0.0290 / 0.0287 | 0.0287 / 0.0286 | 0.0711 / 0.0654 | 0.0694 / 0.0679 |
| (3,0) β=0.1 control | **0.0184 / 0.0170** | 0.0185 / 0.0170 | 0.0964 / 0.0515 | 0.0966 / 0.0515 |

The pooled clause closes (≤ 0.02 at both h) in exactly the
three claimed rows — PRIMARY at β=1.5, (1,0) at β=1.5, and the
β=0.1 control — and in no other row. **Sub-claim (a) pooled
part: reproduced.**

D0 controls, my machinery on the stored radial coefficients
(48 Phase-14 collocation points, seed 143143): pooled
**0.0235 / 0.0222** (claimed 0.0235 / 0.0229; the h=0.15 cell
differs by 0.0007, FD-order noise), t 0.0377 / 0.0383 (phase
0.0377 / 0.0405); held-out at binding points [::10]:
**0.0188 / 0.0192** (claimed 0.0197); supply sign fraction
**0.8080808…** (claimed 0.808 — exact). **D0 controls:
reproduced.**

### (b) The t-component floor — real, not a grid artefact

At the audit/collocation points my t-medians span
**0.0276–0.0964** across the five rows and both h (claimed
floor range 0.0276–0.0966) — every row above the 0.02 bar, by
1.4–4.8×. On points no solver saw:

- phase's fresh set (seed 191777, 64 pts): my t-medians
  0.098 / 0.099 / 0.188–0.191 / 0.218 / 0.164–0.168 across rows
  (phase's own reads: 0.070–0.22);
- **my own fresh set (new seed 590590, 128 pts, chosen by
  me)**: t-medians **0.057–0.161** across rows (PRIMARY
  0.057–0.059; (0,0) 0.121–0.132; β=0.1 control 0.153–0.161),
  pooled 0.019–0.041.

Two independent fresh point sets, drawn independently of every
audit grid and of each other, both read the t-component
*worse* than the collocation floor and never below 0.057.
The floor is a property of the continuum configuration in
this ansatz class, not of the audit grid. **Sub-claim (b):
reproduced, including its "higher on fresh points" clause.**

### (c) Θ_f — NEC violation, all-EC failure, distance, readings

My full-volume audits (1270 pts, r²-weighted, per m² ∈
{0.1, 0.3, 1, 3, 10, 30}, both h; ranges over all 5 rows × 6
m² × 2 h):

- Θ_f NEC violation fraction, f-reading: **0.703–1.000**
  (claimed 0.71–1.00; my minimum cell is (0,0) β=1.5, m²=30:
  0.703–0.705 vs the phase's 0.705). No row, no m², no h is
  NEC-clean; the best cell still violates on ~70% of the
  volume.
- Θ_f NEC violation, g-reading: **0.706–1.000** — the two
  readings agree on illegality in every cell, as claimed; no
  reading-disagreement naming arises.
- All four conditions fail for Θ_f in every row: my WEC
  violation 0.703–1.000, SEC 0.810–1.000, DEC 0.703–1.000
  (f-reading, all rows/m²/h). (My WEC/SEC/DEC fractions at
  non-Type-I points use the Hawking–Ellis classification
  count, the phase's sampled-margin fill; the two conventions
  agree on the conclusion in every cell.)
- Θ_f = 0 distance (componentwise |G_f + C_f| / (|G_f| +
  |C_f|), median over scale-masked entries): mine
  **0.997–1.000** (claimed 0.999–1.000; three cells at
  0.997–0.998 under my 2nd-order G_f). The solved f is no
  closer to an empty f-sector than Phase 14's was.
  **Sub-claim (c): reproduced.**

### (d) Behind both: T_req volume DEC / NEC

My T_req = (G_g + C_g)/8π volume audits (my own G_g at
h=0.15; EC reads at both audit h for Θ_f, T_req tensor
h-independent given G_g):

- DEC violation fraction across all rows/m²: **0.828–1.000**
  (claimed 0.85–1.000). My single lowest cell — (1,0) β=1.5,
  m²=0.1: 0.828 — sits 0.023 below the phase's 0.854 for that
  cell, entirely attributable to my stricter non-Type-I DEC
  counting plus FD order; every strong row at m² ≥ 0.3 reads
  ≥ 0.966 in my audit, and the PRIMARY row reads
  0.971–1.000. The substance — DEC fails on essentially the
  whole volume in every strong row — is intact.
- No volume-NEC-clean row: my T_req NEC violation range
  0.109–0.852, best **0.109** at the β=0.1 control (claimed
  best 0.110). **Sub-claim (d): reproduced** (with the DEC
  low-end convention note above).

### Correctness verdict

**REPRODUCED.** All four sub-claims and the machinery gate
re-derive from fresh code with the same signs, the same
bar-crossings, and values matching to ≤ 0.005 on constraint
medians, ≤ 0.01 on Θ_f NEC fractions, and exactly on the D0
supply sign. No restatement of the correctness content is
needed; the two range-endpoint notes (DEC floor, Θ_f-distance
floor) are convention/FD-order effects documented above, not
disagreements.

## 4. Novelty

### 4.1 Verbatim query log (all run 2026-11-21/22, via
browser_search / browser_open; sources checked: arXiv,
INSPIRE-HEP-indexed records, Semantic Scholar-indexed
records, APS/DOI records, general web)

1. `Hassan-Rosen bimetric gravity warp drive Alcubierre`
2. `bimetric gravity warp drive exotic matter energy conditions second metric`
3. `arXiv bimetric gravity wormhole energy conditions effective stress-energy tensor`
4. `Hassan Rosen bimetric Bianchi constraint interaction stress energy conservation`
5. `"massive gravity" OR "dRGT" warp drive Alcubierre bubble energy conditions`
6. `Hassan-Rosen bimetric gravity wormholes traversable solutions`
7. `INSPIRE-HEP bimetric gravity effective stress energy tensor violates null energy condition interaction term`
8. `Semantic Scholar bimetric gravity second metric matter sector energy conditions phantom effective fluid`
9. `"giant wormholes" ghost-free bigravity Sushkov Volkov`
10. `arxiv listing bimetric gravity Alcubierre warp bubble superluminal shell numerical solution Bianchi`
Plus browser_open on the arXiv record of the key neighbour
(arXiv:1206.3814) to read its abstract verbatim.

### 4.2 What the search found

**No Hassan–Rosen warp-drive paper exists in the searched
literature.** Queries 1, 2, 5 and 10 return no refereed or
preprint computation of an Alcubierre-type shell in bimetric
gravity — only GR warp work, and two unrefereed speculative
items (a NASAspaceflight-forum/ResearchGate "adelic gravity"
preprint and a Zenodo toy model, Pronenko 2026) that invoke
bimetric gravity as inspiration for an ansatz without solving
the bimetric equations for a warp shell. Bimetric
exotic-geometry work is confined to wormholes and cosmology:

- **Baccetti, Martin-Moruno & Visser, "Null Energy Condition
  violations in bimetric gravity", arXiv:1206.3814 [gr-qc],
  JHEP 1208 (2012) 148.** The decisive near neighbour. They
  consider the *effective* stress-energy tensors (the
  interaction tensors) of the foreground and background
  sectors in ghost-free bimetric gravity and prove from the
  theory's symmetries that the two sectors' NECs are
  **strongly anti-correlated**: "the NECs can only be
  simultaneously fulfilled when they saturate, corresponding
  to foreground and background cosmological constants. In all
  other situations, either the foreground or the background
  is subject to a NEC-violating contribution to the total
  stress-energy." I.e. the principle "clean one sector and
  the other sector pays" — exoticity relocation between the
  two grounds — is a published, general result about the
  interaction tensors, from 2012.
- **Sushkov & Volkov, "Giant wormholes in ghost-free
  bigravity theory", arXiv:1502.03712 [hep-th], JCAP 06
  (2015) 017, DOI 10.1088/1475-7516/2015/06/017.** Bigravity
  wormholes exist precisely because "the graviton
  energy-momentum tensors do not a priori fulfill any energy
  conditions" — the f/g interaction sectors carrying
  NEC violation is the working mechanism, stated as known.
- **Rahman, Sen & Bohra, "Traversable wormholes in bimetric
  gravity", arXiv:2305.13013 [gr-qc], Phys. Rev. D 108,
  104008 (2023), DOI 10.1103/PhysRevD.108.104008.** Exact
  static bimetric wormhole; the (effective) weak energy
  condition is violated near the throat — again the
  interaction sector supplying the exoticity.
- Hohmann, "Traversable wormholes without exotic matter in
  multimetric repulsive gravity", arXiv:1312.5290 — a
  different (multimetric, non-Hassan–Rosen) theory; cited
  only to delimit: sector-relocation of EC burden is a
  familiar multimetric theme, not specific to this claim.
- The Bianchi constraint itself, and its coupling of the
  interaction terms to both sectors' stress-energy tensors,
  is standard Hassan–Rosen structure (e.g. the doubly-coupled
  analysis, arXiv:1306.0004, §2.2 "Bianchi constraints").
  Bimetric cosmology likewise routinely finds the effective
  bimetric fluid phantom/NEC-violating (e.g. arXiv:1503.07436;
  arXiv:1701.00811) — the f-sector effective content being
  exotic is, at the qualitative level, understood.

**What no source states:** (i) any warp/Alcubierre shell —
moving, superluminal, or otherwise — solved or audited in
Hassan–Rosen bimetric gravity; (ii) a Bianchi-constraint
solve for such a shell in which the *pooled* constraint
closes under a direction-dependent f while its *t-component*
retains a floor (0.0276–0.0966 at audit points, higher on
fresh points); (iii) Θ_f defined as *matter* by the full
f-sector equation G_f + C_f = 8πΘ_f for a solved
configuration and then EC-audited as matter, per m², on the
full volume (the literature audits the interaction tensors
as effective fluids, or assumes f-sector matter, rather than
reading the defined matter off a solved warp shell);
(iv) the quantitative two-ground anatomy as one result —
pooled closure + component floor + Θ_f relocation +
T_req DEC failure — for the Phase-14 closest-miss
configuration.

One delimitation the claim must carry honestly: Baccetti et
al.'s anti-correlation is a statement about the interaction
effective tensors in the two sectors, not about a matter
tensor Θ_f defined by the f-equation; P19-1's Θ_f result is
a distinct, configuration-level measurement, and it is
*consistent with and foreshadowed by* the 2012 theorem, not
identical to it. Conversely, the theorem does not cover the
t-component constraint floor at all — that part of the
anatomy has no published counterpart found.

### 4.3 Novelty verdict

**PARTIALLY KNOWN.** Known part, exactly: the qualitative
relocation principle — in ghost-free bimetric gravity the
two sectors' effective NECs are strongly anti-correlated and
can both hold only at saturation, so exoticity removed from
one sector reappears in the other — is Baccetti,
Martin-Moruno & Visser, arXiv:1206.3814 (JHEP 1208 (2012)
148); the f/g interaction tensors' freedom from any energy
condition is likewise the stated working mechanism of
Sushkov & Volkov, arXiv:1502.03712. New part, exactly: the
quantitative two-ground anatomy of a moving superluminal
warp shell in Hassan–Rosen gravity — pooled Bianchi closure
at β=1.5 under direction-dependent f, the persistent
t-component floor, and the per-m² full-volume EC audit of
the matter Θ_f that the full f-equation defines — which no
searched source states.

### 4.4 Exact restated wording (required for upload)

> "In Hassan–Rosen bimetric gravity, that the two sectors
> cannot both be made NEC-clean — the interaction
> effective stress-energy tensors' NECs are strongly
> anti-correlated and can be simultaneously fulfilled only
> when they saturate — is a known general result
> (Baccetti, Martin-Moruno & Visser, arXiv:1206.3814). What
> is new here is its quantitative anatomy for a moving
> superluminal warp shell, measured end-to-end on the
> Phase-14 closest-miss configuration: with a
> direction-dependent second metric (54 coefficients, 128
> collocation points) the pooled Bianchi constraint closes
> at β=1.5 for the first time (0.0189/0.0181 at h=0.3/0.15
> against the 0.02 bar) while its t-component never closes
> in any row (floor 0.0276–0.0966 at audit points, higher on
> fresh points), and the matter Θ_f defined by the full
> f-sector equation violates the NEC on 71–100% of the
> volume at every coupling m² in every row — the
> configuration-level realisation, for a warp shell, of
> exoticity relocation into the f-sector."

## 5. Files

- Code: `gate5/wf_g59_lib.py`, `gate5/wf_g59_audit.py`
  (fresh; run with `~/workspace/warp-pilot/venv/bin/python`).
- Numbers: `gate5/wf_g59_numbers.json`; run log
  `gate5/wf_g59_audit.log`.
- This report: `gate5/results/wF_g5_9.md`.
- Nothing uploaded; no external contact beyond the logged
  literature searches.
