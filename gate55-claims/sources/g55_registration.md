# GATE-55 REGISTRATION — INDEPENDENT RE-JUDGEMENT OF THE PHASE 420 SET

Charged at ledger entry 1103 (2026-11-27). Written before any
Gate-55 computation. Frame of record: the VM
(`~/workspace/warp-pilot/venv`, numpy 2.5.5 / scipy 1.18.1) +
Phase 166 pin, float64; deciding reads on the VM. The laptop is
run as an admission control and reported; it decides nothing.

## Machinery (fresh, this gate's own)

`gate55/work/g55_lib.py`, written for this gate: gamma matrices
by Kronecker products (Dirac representation); the composite
superposition evaluated as an EXPLICIT FIELD FUNCTION psi(X)
with per-mode masses and analytic mode-by-mode derivatives;
T_ab from the canonical symmetrised bilinear on the total field
— the object Phase 420's registration SS2 defines — with NO
pairwise S-matrix in any deciding path (a separately written
pairwise assembly exists only as the C1 self-consistency
cross-check). Own Hawking–Ellis classifier and eigen-channel
decomposition using Phase 410 SS4(ii)'s channel definitions
(the definitions are the claim's content; the code is the
gate's). Own FD Jacobians (central, h_j = 1e-6 * max(1, |th_j|),
Phase 410's recipe — the recipe is part of the sigma_min
claim's content per G36-C practice). Own delta construction
from the STORED T_req (Phase 420's stored T_req is bit-identical
to Phase 410's stored That at the A sites — verified by the
parent record; the gate re-checks the identity itself).
Nothing is imported from phase420/work, phase410/work,
phase320/work, phase313/work or gate54/work for any deciding
computation. Stored solutions and stored targets are data.

## Controls (all before any claim read is believed)

- C1 · Builder self-consistency: field-function path vs the
  lib's separately written pairwise cross-check on a random
  mixed-mass superposition (3 modes m = 1, 3 modes m = 0) at
  5 random points: max relative T diff <= 1e-12. Mode health:
  Dirac residual of every stored mode at the primaries
  <= 1e-12; norm deviation |u^dag u - 2E|chi|^2| <= 1e-12.
- C2 · Phase 420's CTRL-420-A configuration on gate machinery
  (410's Fit A primary, family 2 empty, UNCORRECTED A targets):
  per-site direct residuals each <= 2x the stored
  [8.157213446731793e-15, 2.7633923118189793e-13,
  2.9659878908312287e-12] and max <= 1e-11; joint sigma_min
  within 1% relative of 0.3857618146636974 (per-solution).
- C3 · Phase 420's CTRL-420-B configuration on gate machinery
  (410's Fit B primary, UNCORRECTED stencil targets): per-site
  residuals each <= 2x stored, max <= 1e-11; joint sigma_min
  within 1% relative of 0.015432479500623982 (per-solution).

## Claims and bars

(a) DELTA CONSTRUCTION. From stored T_req at the 8 sites:
  gate delta per the registered construction (eigenframe of
  eta*T_req; Delta = -SEC_trace split +Delta/4 on rho,
  +Delta/4 on each principal pressure, i.e. W = diag(+D/4,
  -D/4, -D/4, -D/4) on the eigenvalues of eta*T; delta = 0
  where SEC_trace >= 0). Bars: Delta at A2/A3 within 1e-9
  relative of 2.213557e-4 / 3.388413e-4 (full stored precision
  2.2135565049905559e-4 at A2); gate T_corr vs stored T_corr
  max abs diff <= 1e-12; SEC_trace(gate T_corr) <= 1e-12 in
  abs at A2/A3; delta exactly 0 at A1 and the stencil;
  NO-JOINT-SURPLUS-SPEND: every joint channel (NEC_r, NEC_t,
  WEC, DEC_r, DEC_t, DEC_flux) of T_corr >= the same channel
  of T_req at A2 and A3, tolerance -1e-15; the A2 joint_min
  move +1.385e-4 -> +2.491e-4 reproduced within 1e-9 relative.
(b) REPRODUCTION. Stored C-A primary ((6,6), m2 = 0) against
  gate T_corr at {A1, A2, A3}: per-site direct residuals each
  <= 1e-9 (the registered match bar); max reported against
  stored 3.496009861987862e-10. Joint sigma_min within 1%
  relative of 30.12132520557749 (per-solution, G36-C); rank
  30 at the 1e-10 relative tolerance; per-site blocks
  reported against stored 309.28 / 118.50 / 50.94 (1% rel).
  Stored C-B primary against T_req at the 5 stencil sites:
  max direct residual <= 1e-9 (report against stored
  3.564601757239122e-15); sigma_min within 1% of
  0.011390408308609587; rank 50.
(c) COMPOSITE TOTAL'S STATUS. From the stored C-A primary on
  gate machinery: T_sup at A1/A2/A3; channel table of T_sup;
  bars: every channel >= -1e-9 at all three sites (report
  actual minima); SEC_trace(T_sup) at A2/A3 <= 1e-9 in abs
  (report against stored 2.7471977600765363e-12 /
  2.2765634169474858e-10); densities reported BOTH ways —
  T_sup[0,0] (Eulerian, site frame) and the eigenvalue rho —
  each compared to its stored record (checker T[0,0]:
  1.238992716060313e-4 / 4.5719647172514505e-4 /
  1.9444494781581017e-3; diagnostics eigenvalue rho:
  1.238137e-4 / 4.431937059565106e-4 / 1.9442432352044024e-3)
  at 1e-6 relative; both must be positive at every site for
  the density claim to survive unqualified. Prices |a|^2 per
  family from the stored avecs: within 1e-12 relative of
  0.029172052178672605 / 2.0362442383995038e-06; and the
  comparison price 410's 0.029266406597128584 re-read from
  410's stored Fit A primary avecs the same way.
(d) C-S CONTEXT ARM. The stored C-S N = 6 warmA solution
  (phase420/work/p420_cands_fitCS_N6.jsonl) against gate
  T_corr at {A1, A2, A3} on gate machinery: max direct
  residual reported against stored 1.468495745267423e-11;
  C-S STANDS iff max residual <= 1e-9 (the registered bar).

## Amendment audits (from the stored record + code reading)

- A1 (control cap): verify from Phase 410's stored record
  that its Fit A primary max residual is
  2.9659878908312287e-12 > the registered 1e-12 cap (so the
  cap was ill-posed as charged), and that the corrected bar
  (each <= 2x stored, max <= 1e-11) is met by the phase's
  control reads (ratios 0.999-1.000 on the record).
- A2 (u_spinor 0/0): verify the singularity exists in the
  unguarded spinor (m = 0, p = 0 divides by sqrt(E) = 0);
  verify from the stored primaries that NO mode sits at
  exactly-zero momentum (guard inert on every deciding
  read); verify the guard's trigger condition by code
  reading (exactly-zero massless momenta only).
- A3 (ladder): confirm from p420_ladder_completed.json
  that all four completed rungs reclose <= 1e-9 (recorded
  max 1.2781931870247612e-14) and from p420_results.json
  that the original ladder's eps = 1e-6 draw 0 stalled at
  3.2820674985370054e-09 with the sibling draw reclosing;
  the bar (1e-9) is the same in both records.

## Fences (bind every quotation)

T_corr is a construction of Phase 420 — never the 405
winner, and it corresponds to NO existing geometry; site
mating != extent coverage; sourcing a corrected target !=
producing a legal design; novelty NONE for the method
(Gate-25); sigma_min per-solution only (G36-C).

DESK: NO DATA CONTACT.
