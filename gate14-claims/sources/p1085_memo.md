# P108-5 — Memo (FU-P106-3a: genuinely multipartite published QET)

## Verdict (registered form)

**EVALUATED — REOPENING BAR MET (R_net > 1, second-pathed)**

The search (record: `p1085_search_record.md`) found exactly one
genuinely multipartite QET protocol published in evaluable form:
**Xun & Ren, "Quantum Energy Teleportation via Random
Bi-Partitioning in N-Qubit Systems", arXiv:2410.04919** — a single
N-qubit resource state with an N-body interaction
V = 2k σ₁ˣ…σ_Nˣ + const, Hamiltonian Eqs. (1)–(2), analytic ground
state Eq. (3), delivered energy E_out in closed form Eqs. (9)–(11),
injection E_in Eq. (6). Evaluated under Phase 106 P106-3's
inherited accounting verbatim (definitions fixed in
`work/p1085_definitions.md` before the deciding computation), it
meets the inherited reopening bar — **any variant with
R_net > 1 resource-counted** — at multiple of its own
configurations, confirmed by a from-scratch second path. This is
flagged as a milestone read, in the exact scope stated in
§Scope and caveats below. C12: an accounting item; nothing FTL
is claimed.

## The accounting applied (inherited verbatim)

Per P72-2's run record §§3–4 as inherited by P106-3: delivered
E_B := the paper's E_out at the receiving sector (the output
qubits' H_i plus V — the paper's own sector definition,
Eqs. 28/39 pattern); resource counted via the per-sector
uncorrelated reference, E_prep^(marg) = the receiving sector's
energy in the marginal-product state (product of the ground
state's own single-qubit marginals) above its ground value;
E_net,B = E_prep^(marg) − E_out; R_net = 0 iff E_net,B ≥ 0, else
the FR-net ratio of P72-2 §4 (net pulse magnitude × its duration
/ (3/32π²), ħ = 1 in model units). Evaluated points inherited:
h = 1, r = k/h ∈ {0.5, 1, 2}. Configurations: the paper's own —
(N, m) = (3,1), (3,2), (4,1), (4,2), (4,3) (its appendix
instances), (5,1), (6,1), (8,1), (10,1) (its general formula;
the paper plots N = 10, 100), plus the N = 2, m = 1 control.
Classical-leg energy ≥ 0 omitted throughout (all price ratios
are lower bounds), as inherited.

For this Hamiltonian the marginal-product reference is exact in
closed form: every marginal is diagonal, so ⟨H_i⟩ is unchanged
and ⟨∏σˣ⟩_marg = 0, giving **E_prep^(marg) = 4k²/D**,
D = √(N²h² + 4k²) — and at N = 2 it reduces to P72-2's
2k²/√(h²+k²), as it must.

**Controls (all pass).** The N = 2, m = 1 instance reproduces
Phase 72's stored reads exactly: E_out = 0.07257 / 0.11475 /
0.09818, E_prep^(marg) = 0.44721 / 1.41421 / 3.57771, τ₀ =
0.23272 / 0.18537 / 0.11725 (= P72-2's τ_pulse) at r = 0.5/1/2
(checker-verified against `phase72/results/p722_results.json`).
The dense second path's eigendecomposition returns ground
energy 0 to ≤1.3×10⁻¹⁵ (the printed constants' property), and
its simulated E_out agrees with the printed closed form to
<10⁻⁹ at every second-pathed row.

## Deciding reads

E_net,B < 0 — the receiving sector goes negative **relative to
the uncorrelated reference**, the thing that never happened in
the pair protocol — first at (N, m) = (5, 1), and at every
m = 1 configuration with N ≥ 6 at r = 0.5, growing with N:

| (N, m, r) | E_out | E_prep^(marg) | E_net,B | τ₀ | R (τ₀) | τ_marg | R (τ_marg) |
|---|---|---|---|---|---|---|---|
| 6, 1, 0.5 | 0.26342 | 0.16440 | −0.09902 | 0.21618 | **2.254** | 0.30657 | **3.196** |
| 8, 1, 0.5 | 0.29790 | 0.12403 | −0.17387 | 0.19794 | **3.623** | 0.25572 | **4.681** |
| 8, 1, 1.0 | 0.78085 | 0.48507 | −0.29578 | 0.20932 | **6.518** | 0.35499 | **11.054** |
| 10, 1, 0.5 | 0.31967 | 0.09950 | −0.22017 | 0.18307 | **4.243** | 0.22412 | **5.195** |
| 10, 1, 1.0 | 0.86326 | 0.39223 | −0.47102 | 0.19749 | **9.793** | 0.28912 | **14.337** |
| 10, 1, 2.0 | 1.70907 | 1.48556 | −0.22350 | 0.21821 | **5.134** | >30 (no return in window) | — |

τ₀ is P72-2's literal τ_pulse (first return of the sector energy
S(t) to the ground zero under the printed H); τ_marg is the
same read shifted to the uncorrelated reference (first return
of S(t) to +E_prep^(marg)) — the primary FR-net duration under
the definitions fixed before computing. **The bar is met under
both duration conventions at the first five rows** (the sixth
meets it under τ₀, and under τ_marg its pulse has not returned
within the t ≤ 30 window at all). Two further rows are
convention-SPLIT and are **not** used as deciding rows:
(5, 1, 0.5): R = 0.987 (τ₀) vs 1.513 (τ_marg);
(6, 1, 1.0): R = 0.523 (τ₀) vs 8.885 (τ_marg).
All other 22 evaluated rows have E_net,B ≥ 0 and R_net = 0 —
including every m ≥ 2 configuration and every N ≤ 4
configuration (closest: (4, 1, 0.5), E_net,B = +0.04100).
Full table: `p1085_results.json` (30 rows).

**Second path.** `work/p1085_secondpath.py` — from-scratch
dense Kronecker construction, ground state by
eigendecomposition, protocol simulated with explicit projector /
unitary matrices, marginals by partial trace, S(t) by full
spectral evolution — agrees with the primary path to <10⁻⁶ on
every deciding quantity at (5,1,0.5), (6,1,0.5), (8,1,0.5),
(8,1,1.0) (E_out, E_prep^(marg), E_in, τ₀, τ_marg, both R's).
The bar therefore rests on second-pathed rows; the (10, 1, ·)
rows in the table are primary-path reads, reported as
corroborating trend, not as deciding rows.
Checker `work/p1085_check.py`: **249/249 PASS** (closed-form
recomputation of all 30 rows, P72-2 control, bar assertions;
second-path cross-checks included when
`work/p1085_secondpath_results.json` is present).

## Anatomy — why the multipartite form changes the read

In the pair protocol the correlation energy stored at Bob's
sector, 2k²/√(h²+k²), grows with the coupling and always exceeds
E_B — the relocation filing's binding term. Here the resource
is ONE N-body interaction shared by all N parties. Its total
correlation energy above the marginal-product reference is
4k²/D ≈ 4k²/(Nh) — it is diluted as 1/N, because the
uncorrelated reference kills the single N-body correlator
⟨∏σˣ⟩ while the constant that normalises it is spread over the
whole system. The single-output (m = 1) extraction, by contrast,
stays O(h) (E_out → h(√(1+4r²) − 1) as N → ∞ at fixed r).
The two scalings cross at N = 5 (r = 0.5). This is **not** the
P106-3 V4 artefact: V4 granted M delivering sectors one shared
preparation. Here there is ONE receiving sector, ONE resource
state, and its FULL correlation energy — total, not a per-sector
fraction — is on the books (the other sectors' marginal-product
energies equal their ground values, so the sector read and the
total read of the resource coincide). No per-sector cost is
deleted; the resource genuinely costs 4k²/D in total.

## Scope and caveats (part of the verdict, not footnotes)

1. **The price line does NOT fire.** Total counted price per
   unit delivered, (E_prep^(marg) + E_in)/E_out, is 5.59–130.19
   across all rows (deciding rows: 19.35, 23.73, 9.32, 28.33,
   10.68, 5.76) — the (N−1) measurements inject far more than
   the one output extracts (E_in alone is 19–28× E_out at the
   r = 0.5 deciding rows). What fires is the registered bar
   itself: the FR-net **pulse ratio** R_net > 1 with the
   resource counted. P72-2's relocation filing required both
   lines; P106-3/P108-5's reopening bar is R_net, and it is met.
2. **Model scope.** This is a finite spin model with an N-body
   interaction, read with the programme's own P72-2 pulse
   construction (model units, τ from the model's intrinsic
   evolution). It is not a quantum-field vacuum pulse, and no
   Ford–Roman claim about field theory is made or implied.
3. **τ convention.** Handled by deciding only on rows that
   clear the bar under both registered readings of the pulse
   duration (see table); the two split rows are reported as
   split and carry no verdict weight.
4. Supplementary closed-form only (no τ computed, no R
   claimed): at N = 100, m = 1, E_net,B = −0.394 / −1.156 /
   −2.804 at r = 0.5 / 1 / 2 — the net negativity grows with N;
   the R reads above rest on N ≤ 10, where S(t) was computed.
5. The separable-minimum preparation reference (P72-2's
   deciding *price* reference) was not evaluated for this
   Hamiltonian; the marg reference is the R_net reference and
   is the one the bar is defined on. The price line is reported
   on the marg reference only, labelled as such.

## Failure Protocol — follow-ups

- **FU-P1085-1 (coordinator's call):** independent replication
  of the τ reads at the deciding rows by a second worker /
  Gate-style audit before any use beyond this phase, including
  the N → ∞ asymptotics of τ and an explicit ruling on the
  τ₀/τ_marg convention for the FR-net ratio in the inherited
  accounting (two evaluated rows split on it).
- **FU-P1085-2:** the field/oscillator analogue — whether an
  N-party field QET with a shared interaction shows the same
  1/N dilution of the sector correlation energy; the spin-model
  read does not transfer without it.
- **FU-P1085-3:** pose the separable-minimum reference for this
  Hamiltonian (product-state minimisation of the printed H) to
  complete the price-line bookkeeping in P72-2's exact form.

## C12 line

C12: an accounting verdict on a sourcing scheme — no throat,
no transport, nothing FTL is claimed by this outcome. The QET
classical leg is ≤ c by the protocol's own construction.
INTERNAL ONLY — nothing uploaded, nobody contacted (web reading
was the item's registered search method).
