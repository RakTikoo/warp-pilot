# P106-3 — Run Record (definitions + variant constructions fixed BEFORE any Phase-106 number)

**Item:** P106-3 (FU-P833-2) — MULTI-PARTY QET NET READS, Phase 106.
**Registration:** `../CHECKPOINT106.md` §P106-3 — bars, variants and
verdict forms are fixed there; nothing in this record moves any
definition. This record restates the inherited accounting and the
exact variant constructions so the evaluation, the second path and
the checker all read the same objects.
**Nature:** an accounting item only. No new Hamiltonian is posed, no
scan, no simulation. Compositions of the published two-qubit Hotta
protocol ONLY. Every number is recomputed from
`../../phase72/results/p722_results.json`'s stored point values,
never quoted from prose. float64 throughout; programme venv
`~/workspace/warp-pilot/venv/bin/python`.
**C12:** an accounting verdict on a sourcing scheme; no throat, no
transport, nothing FTL is claimed by any outcome of this item.

## 1. Inherited accounting (verbatim from P72-2's run record; no definition moves)

Evaluated points: r = k/h ∈ {0.5, 1, 2} with h = 1 (energies in gap
units, i.e. units of h). Per consumed Hotta copy, from the Phase-72
JSON's stored point fields (`EA`, `EB`, `E_prep_sep`,
`E_prep_marg`, `E_net_B_sector`, `tau_pulse`, `R_net`):

- Delivered at Bob's sector, relative to the entangled ground's
  zero: `E_B` (JSON field `EB`).
- Alice's injection: `E_A = h²/√(h²+k²)` (JSON field `EA`).
- Resource stored energy at the receiving sector (marginal-product
  / uncorrelated reference, R-marg):
  `E_prep^(marg) = 2k²/√(h²+k²)` (JSON field `E_prep_marg`).
- Separable-minimum preparation reference (R-sep):
  `E_prep^(sep)` (JSON field `E_prep_sep`). The deciding total
  price uses the smaller reference; both references are reported
  wherever a price is reported.
- Net Bob-sector energy vs the uncorrelated (marginal-product)
  reference: `E_net,B = E_prep^(marg) − E_B` (cross-checked against
  the stored `E_net_B_sector` field at every point).
  Net delivered per receiving sector: `E_B − E_prep^(marg) = −E_net,B`.
- `R_net` (P72-2 §4, FR-net, the deciding read):
  `R_net = 0` iff `E_net,B ≥ 0` at the receiving sector; else
  `R_net = |E_net,B| · τ_pulse / (3/(32π²))` with `τ_pulse` and the
  coefficient `3/(32π²)` taken from the Phase-72 JSON (this is the
  exact form in `phase72/work/p722_eval.py`). `R_raw` is reported
  nowhere as deciding.
- Total price per copy (classical leg energy ≥ 0, omitted — every
  price ratio is a lower bound):
  `price^(sep) = E_prep^(sep) + E_A`,
  `price^(marg) = E_prep^(marg) + E_A`;
  total price per unit delivered (raw `E_B` delivery):
  `price^(ref)/E_B` — the P72-2 deciding lines
  `total_per_EB` (sep) and `total_per_EB_marg` (marg), cross-checked
  against the stored fields.
- **Reopening bar (inherited verbatim): any variant (V1–V3) with
  `R_net > 1` resource-counted.** A positive verdict additionally
  requires the independent from-scratch second path.

## 2. Registered variants (constructions fixed here, before numbers)

### V1 — Parallel parties
M independent Alice–Bob pairs, M ∈ {1, 2, 4, 8, 16, 64, 1024};
each pair is a full Hotta copy with its own resource, injection
and receiving sector, all at the same evaluated point.
Reads per (point, M):
- per-sector `E_net,B` and `R_net` (identical in form to §1);
- aggregate raw delivered `M·E_B`;
- aggregate net delivered `Σ_sectors (E_B − E_prep^(marg)) = M·(E_B − E_prep^(marg))`;
- aggregate total price at each reference `M·price^(ref)`;
- total price per unit delivered at each reference
  `M·price^(ref) / (M·E_B) = price^(ref)/E_B` (M-invariant by
  construction; the equality is computed, not asserted).

### V2 — Star / fan-out
One Alice party holding M pairs (one per Bob), M in the same set
as V1; Alice's classical result is broadcast to all Bobs. Each
pair is still separately prepared and separately measured — the
published protocol has one measurement per pair; a shared single
measurement across pairs is NOT the published protocol and is NOT
granted. Reads exactly as V1, plus Alice's aggregate injection
`M·E_A` stated explicitly per (point, M). No preparation,
measurement or injection saving is granted to the star topology.

### V3 — Relay chain
L ∈ {2, 4, 8} Hotta hops in series at the same evaluated point;
only the final Bob's sector is the receiving sector.
Reads per (point, L):
- final-sector `E_net,B` and `R_net`, from the final hop's own
  pair accounting exactly as in §1 (a single copy);
- delivered at the final sector: `E_B` (the final hop's delivery
  only; upstream deliveries are internal to the chain and are not
  counted as delivered at the final sector);
- total price per unit delivered at the final sector with ALL
  upstream preparation + injection costs counted: total cost over
  all L hops at each reference is `L·price^(ref)` (each hop is a
  full copy: its own preparation at the stated reference plus its
  own injection `E_A`), so the price per unit delivered at the
  final sector is `L·price^(ref)/E_B`. Upstream costs are positive
  costs on the books; they cannot subtract from the final sector's
  reference energy, and the final sector's `E_net,B` is therefore
  not reduced by any upstream term.

### V4 — Adversarial accounting bound (LABELLED: a bound, not a protocol)
Grant, most favourably to a loophole, that M receiving sectors
share ONE pair's preparation and ONE injection: cost paid once,
delivery `M·E_B`. Two granted reads are exhibited, both labelled
artefacts, at both preparation references:
- (V4-sector) granted aggregate sector net
  `M·E_B − E_prep^(ref)` — the §1 net form with the per-sector
  preparation deleted down to a single payment;
- (V4-total) granted aggregate net after all granted costs
  `M·E_B − (E_prep^(ref) + E_A)` — preparation and injection each
  paid once (the form named in the tasking).
For each read and each reference, the crossing is the smallest
integer M ≥ 1 with granted aggregate net > 0, i.e.
`M_cross = floor(cost/E_B) + 1` with cost `E_prep^(ref)` (sector
read) or `E_prep^(ref) + E_A` (total read); the granted net is
also tabulated at the registered M set of V1.
**Registered caveat (stated wherever V4 is reported):** the
uncorrelated reference against which `R_net` is defined is PER
RECEIVING SECTOR — each sector's marginal-product correlation
energy is its own — so V4's crossing, if any, is an artefact of
deleting per-sector resources from the books, not an `R_net`
read; **V4 cannot fire the reopening bar.** Its purpose is to show
exactly which bookkeeping deletion a claimed multi-party gain
would require. No `R_net` is assigned to V4.

## 3. Verdict forms (only these, CHECKPOINT106 §P106-3)

- **MULTI-PARTY NET POSITIVE — REOPENING BAR MET**: some
  registered variant (V1–V3) at some registered scale has
  `R_net > 1` resource-counted, second-pathed.
- **NET NON-POSITIVE IN ALL REGISTERED MULTI-PARTY FORMS**:
  per-sector and aggregate net ≤ 0 in V1–V3 at every registered
  scale and evaluated point, `R_net = 0` throughout, V4's artefact
  crossing (if any) exhibited with its caveat; the closure count
  (forms × scales × points read) stated; scope stated exactly
  (compositions of the published two-qubit protocol; a genuinely
  multipartite published Hamiltonian with evaluable formulas
  would be a new item under the same reopening bar).
- **NOT POSED**: a variant cannot be stated under the inherited
  accounting (the failing clause named).

## 4. Scripts

- `../work/p1063_eval.py` — the evaluation above; writes
  `p1063_results.json`.
- `../work/p1063_secondpath.py` — independent from-scratch second
  path: recomputes the deciding lines directly from the Phase-72
  JSON's raw point fields with its own arithmetic (no import of,
  and no shared functions with, the evaluation script); writes
  `p1063_secondpath.json` alongside its stdout verdict.
- `../work/p1063_check.py` — checker: recomputes every
  verdict-carrying number in `p1063_results.json` from the
  Phase-72 JSON + the definitions above, and every deciding line
  against the second path's output; prints PASS/FAIL counts.

INTERNAL ONLY — nothing uploaded, nobody contacted.
