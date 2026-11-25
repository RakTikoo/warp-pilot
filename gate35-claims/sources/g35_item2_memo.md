# GATE-35 ITEM 2 MEMO — INDEPENDENT RE-READ OF PHASE 314'S HEADLINE MEMBER

## Path taken

The gate's own assembly (`g35_lib.py`), different in kind from
p312_lib/p314_lib (neither imported, nor p308_lib): the metric is
built in spherical coordinates (t, r, θ, φ) with the polar axis
along the shift direction — γ = M dr² + r²dΩ², g_tt = −N²,
g_tr = −βS cosθ, g_tθ = +rβS sinθ (the pullback of the pose's
shift covector −βS dx) — the Einstein tensor is computed
symbolically with sympy (S, N, M left as undefined functions of
r; analytic ADM inverse supplied and asserted against g
symbolically), T_req = G/(8π) lambdified, transformed to
Cartesian with the pointwise Jacobian as T_cart = J^(−T) T_sph
J^(−1), and put in the Eulerian orthonormal frame via
verify_metric.eulerian_that on the Cartesian metric built from
its definition. Permitted imports only: p258_lib (S_ab, R_NODES,
DIRS162), p274_lib (winner lapse), verify_metric, p2352_run
(SAMPLER-M margins). The Phase 308 split (16πρ = R + Q_K) is
implemented in-lib from CHECKPOINT308's printed formula as the
cross-check. float64 throughout. Driver `g35_item2.py`, run in
this session, wall 186 s; results `g35_item2_results.json`.

## State of the recovered code, and what I changed

The restart-killed worker's `g35_lib.py` / `g35_item2.py` were
structurally complete. I read both in full and checked them
against the charge: permitted imports only; the spherical
sympy path as above (including the J^(−T)…J^(−1) transform and
the covector pullback); M ramp and quintic smoothstep as
registered; the adversary polish (Nelder–Mead of SAMPLER-M NEC
over (r, θ, φ), Type-I-gated objective, seeded from the worst
Type-I SET points) and the Phase 293 site rule matching
p314_common.pick_sites in form. **No changes were needed; the
code ran as recovered.** (The lib header narrates two defects
"caught by C-G2" in a prior incarnation — that history is
unverifiable and I do not rely on it; the verification is the
run below, executed in this session.)

## Internal certificate (tensor ρ vs split ρ)

- 20 random volume points, headline: max rel diff 7.62×10⁻¹⁶
  (max abs 4.34×10⁻¹⁹). M ≡ 1: max rel diff 2.80×10⁻¹² with max
  abs diff 1.09×10⁻¹⁸ (the relative figure is a near-zero-ρ
  denominator artefact; the absolute agreement is at 10⁻¹⁸).
- Four binding sites: max rel diff 1.56×10⁻¹⁵.
- Against Item 1's independent evaluator `g35_rho.py` at the
  four binding sites: max rel diff 1.73×10⁻¹⁵.
All far inside the 1e-9 certificate bar.

## Controls (run before the re-reads)

**C-G2 (M ≡ 1) — PASS, all within 1e-9 relative, Type-I exact:**

| quantity | gate | stored | rel diff |
|---|---|---|---|
| depth | −0.0013869566081224204 | −0.001386956608122417 | 2.50×10⁻¹⁵ |
| SET NEC min | −0.0040797448356678125 | −0.004079744835667814 | 4.25×10⁻¹⁶ |
| Type-I count | 1245 | 1245 | exact |
| polish r | 12.369476376022238 | 12.369476376022238 | 0.0 |
| site ρ S1 | −5.3959951476209144×10⁻⁵ | −5.395995147620893×10⁻⁵ | 4.02×10⁻¹⁵ |
| site ρ S2 | −8.753311322949348×10⁻⁵ | −8.753311322949402×10⁻⁵ | 6.19×10⁻¹⁵ |
| site ρ S3 | −5.050544693136535×10⁻⁵ | −5.050544693136578×10⁻⁵ | 8.59×10⁻¹⁵ |
| site ρ S4 | −9.342707290960466×10⁻⁵ | −9.342707290960482×10⁻⁵ | 1.74×10⁻¹⁵ |

(Site radii also reproduce exactly.)

**C-G3 (headline SET reproduction) — PASS:** ρ min gate
8.272455162810711×10⁻⁵ vs stored full-precision
8.272455162810697×10⁻⁵ (rel 1.80×10⁻¹⁵; vs the registration's
rounded 8.272455×10⁻⁵, rel 1.97×10⁻⁸), argmin r = 19.87804878,
n_x̂ = +0.0040761 (transverse) — same SET point (index 6516) as
stored. NEC min rel 1.48×10⁻¹⁵, WEC min rel 1.66×10⁻¹⁵,
DEC min rel 0.0 (full-precision comparisons), Type-I count
2615 exact.

## Re-reads (headline member, gate assembly) vs stored

**Depth:** gate −5.327658635240827×10⁻⁴ vs stored
−5.327659×10⁻⁴ (full precision −0.0005327658635240826);
diff −1.08×10⁻¹⁹. Polish point identical to stored
(r = 12.3134870420811, same Cartesian point), Type-I,
ρ_t = +6.263182190001702×10⁻⁴ (stored +6.263182×10⁻⁴).

**Binding sites** (ρ tensor / split agree per the certificate;
NEC-X = my own exact pointwise minimum, 642-point Fibonacci
scan + Nelder–Mead polish):

| site | r | Type-I | ρ_req gate | ρ_req stored | diff | NEC-M gate / stored | NEC-X gate / stored |
|---|---|---|---|---|---|---|---|
| S1 | 12.313487 | yes | +6.263182190001702×10⁻⁴ | +6.263182×10⁻⁴ | 0.0 | −5.327659×10⁻⁴ / −5.327659×10⁻⁴ | −1.267419×10⁻³ / −1.267419×10⁻³ |
| S2 | 11.829268 | no | +6.818808066077541×10⁻⁴ | +6.818808×10⁻⁴ | +8.7×10⁻¹⁹ | −1.170007×10⁻³ / −1.170007×10⁻³ | −1.183691×10⁻³ / −1.183691×10⁻³ |
| S3 | 12.317073 | yes | +6.257630013907989×10⁻⁴ | +6.257630×10⁻⁴ | +9.8×10⁻¹⁹ | −5.327425×10⁻⁴ / −5.327425×10⁻⁴ | −1.266247×10⁻³ / −1.266247×10⁻³ |
| S4 | 17.682927 | no | +1.172278×10⁻⁴ | +1.172278×10⁻⁴ | 0.0 | −7.107812×10⁻⁴ / −7.107812×10⁻⁴ | −7.120705×10⁻⁴ / −7.120705×10⁻⁴ |

All site radii identical to stored (diff 0.0); all NEC diffs
≤ 4.6×10⁻¹⁸ absolute.

**SET-244 EC summary (gate vs stored):** NEC min/median/max
−1.1700067327832906×10⁻³ / −1.6869212992366483×10⁻⁴ /
+6.541263184102982×10⁻⁴ (stored −1.1700067327832923×10⁻³ /
−1.6869212992366763×10⁻⁴ / +6.541263184103002×10⁻⁴);
WEC min −1.0440691445181177×10⁻² (stored −1.0440691445181194×10⁻²);
DEC min −1.0000031873996493 (stored identical);
SEC min −1.2006829673724798×10⁻² (stored −1.2006829673724816×10⁻²);
ρ min/median/max +8.272455162810711×10⁻⁵ / +2.722318715886096×10⁻⁴ /
+8.830803571811661×10⁻⁴ (stored +8.272455162810697×10⁻⁵ /
+2.722318715886096×10⁻⁴ / +8.830803571811661×10⁻⁴);
Type-I count 2615 (stored 2615). Every diff ≤ ~2×10⁻¹⁵ relative.

## Discrepancies

None. The independent symbolic assembly reproduces every
stored headline value — depth, all four binding sites
(point, ρ, both NEC reads, Type-I status), and the full
SET-244 summary — at float64 round-off level (≤ ~10⁻¹⁵
relative, several exactly). Phase 314's headline record is
confirmed by a computation that shares no tensor machinery
with it.

DESK: NO DATA CONTACT. No ledger append, no launches.
