# P266-1 — MEMO: CERTIFY OR REFUTE THE UNCLAMPED-LAW
# BRACKET (0.675, 0.68125] (Phase 243-pattern
# certificate, NO stop parameter) — INTEGRATED RECORD

Worker of Phase 266 (single item P266-1), warp pilot.
Registration (pre-run, FIXED, not edited):
`phase266/work/p2661_registration.md`. Driver:
`phase266/work/p2661_run.py`; results:
`phase266/results/p2661_results.json`; checker:
`phase266/work/p2661_check.py` →
`phase266/results/p2661_verify.json`. Frame of
record: Phase 166 pin, Gate-19-corrected tensor, venv
python (numpy 2.5.5 / scipy 1.18.1), float64. INTERNAL
only. No ledger append, no launch, no external
contact; nothing outside `phase266/` edited.
Protected files byte-identical before/after (§7).

## VERDICT — FORM 1 FIRES

**BRACKET CERTIFIED.** The run's recorded verdict
note, verbatim from `p2661_results.json`:

> The unclamped-law combined-class first crossing
> (0.675, 0.68125] on NEC_ph = DEC_ph stands as a
> verdict in the certified scope: the datum meets
> every registered throat clause bar at all 28
> sampled instants of [0, 0.675] on the standing grid
> (Phase 265 rows, reproduced by CTRL-1 at diff 0.0),
> and on the registered window [0.61875, 0.75] the
> binding clauses are limit-certified at every window
> instant at the unchanged 1e-6 bar (CERT-1..4 hold),
> the limits and G5 reads straddling zero at the
> bracket with no earlier in-window crossing and
> every non-binding clause positive at G5 at every
> window instant <= 0.68125. The sustainment lead
> extends AT VERDICT GRADE: this bracket, certified
> here, lies entirely past the clamped pose's
> (0.65625, 0.6625] (Phase 256, Gate-26) and the
> wound pose's (0.55625, 0.5625] (Phase 243,
> Gate-23) -- certified-vs-certified. The certified
> object is the trim law UNCLAMPED, a(t) = -0.5 -
> c_trim t^2 with c_trim FITTED (Phase 248 Part A
> provenance; registration sec.B); no stop parameter
> appears in it. Fenced by: (i) the tail limitation
> of sec.5(c) (reads past the window are NOT
> certified; tail pricing with its amplitude caveat
> stands on the face); (ii) pose scope (Phase 169
> A-branch datum, true lock; kappa = 0.3 director +
> C2 rotating headline + CH-PHI-Auu under
> P-PHI-TRIM-248 with the unclamped
> fitted-coefficient law, as posed); (iii) jet scope
> / sector superposition (exhibit != construction);
> (iv) programme-level sustainment wording remains
> gated by p1592 regardless. Named successor: a Gate
> registration on the certified claim set,
> re-examining Gate-26's G26-A fence in light of this
> stop-free certificate.

Named successor (registration §7, form 1): **a Gate
registration on the certified claim set** —
re-examining Gate-26's G26-A fence ("the trim law as
clamped at B := 2.5") in light of this stop-free
certificate. (Amending the gate's claim set is the
parent's act, not this phase's.)

## 1. REGISTRATION SUMMARY, WITH THE ADAPTATIONS

The registration carries the Phase 243 certificate as
adapted by Phase 256, with exactly the six adaptations
stated on its face (§A): (A1) the pose is the
combined-class datum of Phases 252/256 (Phase 169
A-branch datum, true lock; κ = 0.3 director; the C2
rotating headline construction, W = 0.2 sin²θ) +
CH-PHI-Auu under P-PHI-TRIM-248 with the **UNCLAMPED**
law a(t) = −0.5 − c_trim·t², c_trim =
+5.253378225339471 (STORED, from
`phase248/results/p2482_results.json`) — **no stop
parameter enters the pose, the controls' fresh reads,
or the certificate anywhere**; read with Phase 252's
machinery (`base_jets` → `posed_jets` →
`solve_wuu_generic` → `clauses_of` on the fixed audit
grid TH), copied into `phase266/` and unmodified in
substance; binding clauses NEC_φ and DEC_φ. (A2)
grids NOT adapted: G3 (N_θ = 5761, h_t = 0.00125),
G4 (11521, 0.000625), G5 (23041, 0.0003125), every
march to T_END = 1.0. (A3) window fixed by the claim
plus Phase 243's margin pattern, with the top capped
by the audited-delivery coverage: W = {0.61875} ∪
sampled {0.625, 0.65, 0.675, 0.7, 0.725, 0.75} ∪
refined {0.68125, 0.6875}; bracket (0.675, 0.68125].
The pattern's span top 0.76875 would pose
a(0.76875) = −3.6046234051234713, outside Phase 265's
audited delivery range [0, −3.5]; the window's end
0.75 poses a(0.75) = −3.4550252517534528, inside it,
and the law reaches −3.5 only at
t = 0.7556858539654343, past every window instant.
(A4) no t* disposition and no re-opening of any prior
certificate: the wound (0.55625, 0.5625] (Phase 243 /
Gate-23) and clamped (0.65625, 0.6625] (Phase 256 /
Gate-26) brackets stand untouched; the comparison is
certified-vs-certified only because form 1 fired.
(A5) CTRL-1's stored target is Phase 265's B = 3.5
arm — the unclamped-equivalent arm — compared exactly
at the instants where that arm IS this pose (§2).
(A6) tail pricing from this phase's fresh G3/G4 rows,
with the §5(c) amplitude caveat on its face.

**The fitted coefficient (§B, carried in every
quotation):** c_trim is a FITTED pose parameter —
formula c_trim = −q₂/s̄ registered in Phase 248 (B1)
before any fit; value fitted in Phase 248 Part A
(q₂ = −6.062834985645177, the full quadratic fit's c₂
over [0, 0.475]; s̄ = 1.1540830919809508) and frozen
before every subsequent march; never re-fit here
(CTRL-2 pins it via Phase 265's stored constants).
The bracket certified here lies OUTSIDE the fit
window [0, 0.475] — the law is extrapolated there, on
the record (Gate-26 §4(3b)).

**Evidential character (§C, carried in advance):**
the evidence is two classes — (i) the sampled
standing-grid span [0, 0.675] (Phase 265's rows,
CTRL-1-reproduced at diff 0.0; NOT limit-certified),
and (ii) the window limit-certification of §4. The
interval is [0, 0.675] at the sampled, refined and
window instants named; **no continuum claim between
instants is made or certified.** The certificate's
character is grid-stability in Gate-26 §2's sense
(§4 below): the disagreements sit at the float64
rounding floor, the limit coincides with the
finest-grid read, and the p values carry no
convergence information — recorded plainly, not as a
relaxation: no CERT condition was waived and the
1×10⁻⁶ bar is nowhere changed.

Execution order (Phase 243/256 driver order, followed
here): CTRL-2 and CTRL-1 ran first; the §5(d) probe
ran before the G5 march because the probe gates that
march; CTRL-3 — which by construction reads off the
G5 state — was evaluated immediately after the G5
march and BEFORE any certificate evaluation. No
certificate quantity was computed before all three
controls had passed, so the §6 decision order is
preserved in substance. No driver bug was found or
fixed during the run; the driver completed in one
honest attempt (wall 929.6 s total).

## 2. CONTROLS

**CTRL-2 — PASS, exact** (stored rows of
`phase265/results/p2651_results.json` only): (a) both
arms' (B = 3.0, B = 3.5) sampled brackets recompute
to (0.675, 0.7] with first-fail carriers exactly
{NEC_φ, DEC_φ}; (b) the two arms' refined brackets
coincide at (0.675, 0.68125] with end NEC_φ margins
exactly +0.051321249458261775 /
−0.04804452588981167 in both arms; (c) the clamp
arithmetic from the stored c_trim:
t_clamp(3.0) = √((3.0 − 0.5)/c_trim) =
0.6898436476740386 (recomputed = stored, diff 0.0)
≥ t_hi = 0.68125, and t_clamp(3.5) =
√((3.5 − 0.5)/c_trim) = 0.7556858539654343
(recomputed = stored) — so over the whole deciding
span [0, 0.68125] the B = 3.0 arm's applied amplitude
IS the unclamped law and the coincident bracket is
the unclamped law's own; (d) every stored ladder
`a_applied` of both arms and the fixed-t t = 0.675
rows equal −0.5 − c_trim·t² exactly, with `clamped`
= False at t = 0.675.

**CTRL-1 — PASS, all diffs 0.0** (matched march
length T_END = 1.0; standing discretisation
N_θ = 2881, main h_t = 0.0025 / aux h_t = 0.00125;
Phase 265's read discipline — main-lattice instants
from the main march, all others from the aux march):

| comparison | max abs diff |
|---|---|
| fresh unclamped rows, sampled instants si 0..30 (t ≤ 0.75), clause minima vs Phase 265 stored B = 3.5-arm `sampled` | 0.0 |
| stored `a_applied` == unclamped law at every compared instant (exact), compared set exactly t ≤ 0.75, sampled[31].t > 0.75 | exact / true |
| bracket lo end t = 0.675 (main march, index 270), clause minima vs stored `refined_bracket` lo margins | 0.0 |
| bracket hi end t = 0.68125 (aux march, index 545), clause minima vs stored hi margins | 0.0 |
| fixed-t rows t ∈ {0.5625, 0.6, 0.65, 0.65625, 0.6625, 0.66875, 0.675, 0.7}, NEC_φ/DEC_φ minima vs stored `fixed_t_NEC_ph` | 0.0 |

Per §A5, the comparison covers exactly the instants
where the stored arm is this pose; past
t = 0.7556858539654343 that arm is a different
(clamped) pose and its rows are not compared. Phase
265's stored arm record carries clause minima, not
profiles; the minima are the verdict-carrying
comparison (Phase 265's own checker verified those
rows fresh at diff 0.0).

**CTRL-3 — PASS** (G5 admitted): fresh G5
director-only reads (wound machinery copied from
`p2431_run.py`, unmodified in substance) vs Phase
210's stored G4 director rows — t = 0.25:
1.4235054024425153×10⁻⁸; t = 0.5:
5.694021876223587×10⁻⁸, both ≤ 1×10⁻⁶. (Numerically
identical to Phases 243/256's CTRL-3 values, as they
must be: same grid, same machinery, same stored
rows.)

## 3. G5 COST PROBE (§5(d))

Probe march G5 over [0, 0.05] (160 steps): **25.3 s**.
Projection for the registered [0, 1.0] march (3200
steps): 20 × probe = **505.7 s ≤ 900 s** — the rule
does NOT fire; G5 was run. (Actual G5 march wall:
636.0 s.) State-array size on the face: 590,033,928 B
per field; MU + U + MTT = 1.770 GB; G3/G4 states were
freed before the G5 march. The §5(d) kernel-spec
packaging obligation attaches only to form 3, which
did not fire; no spec was written. March walls:
standing main 13.6 s / aux 25.9 s; G3 39.4 s;
G4 170.8 s; G5 636.0 s.

## 4. THE CERTIFICATE — UNCLAMPED-LAW BRACKET

Per-instant Richardson on NEC_φ = DEC_φ (the two
clauses are pointwise identical in this machinery —
the checker verified the two rows equal at every
instant on all three grids, max diff 0.0; one row
serves both — the results file carries both,
identical). v3/v4/v5 are the G3/G4/G5 clause minima;
L the Richardson limit; r = |L − v5| the residual.
Bar 1×10⁻⁶ throughout.

| t | case | p | v3 | v4 | v5 | d34 | d45 | L | r | cert |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.61875 | degenerate | — | 0.730765354895377 | 0.7307653548955173 | 0.7307653548955164 | −1.403×10⁻¹³ | +8.882×10⁻¹⁶ | 0.7307653548955164 | 1.403×10⁻¹³ | ✓ |
| 0.625 | monotone | 4.28540 | 0.6716188498447728 | 0.6716188498449114 | 0.6716188498449185 | −1.386×10⁻¹³ | −7.105×10⁻¹⁵ | 0.6716188498449188 | 3.331×10⁻¹⁶ | ✓ |
| 0.65 | monotone | 4.24793 | 0.39700195971843577 | 0.3970019597186045 | 0.3970019597186134 | −1.688×10⁻¹³ | −8.882×10⁻¹⁵ | 0.3970019597186139 | 4.996×10⁻¹⁶ | ✓ |
| **0.675** (t_lo) | monotone | 4.13876 | 0.051321249461480534 | 0.05132124946168393 | 0.05132124946169547 | −2.034×10⁻¹³ | −1.155×10⁻¹⁴ | **0.05132124946169617** | 6.939×10⁻¹⁶ | ✓ |
| **0.68125** (t_hi) | monotone | 3.66496 | −0.048044525888280454 | −0.0480445258880664 | −0.04804452588804953 | −2.141×10⁻¹³ | −1.688×10⁻¹⁴ | **−0.048044525888048084** | 1.443×10⁻¹⁵ | ✓ |
| 0.6875 | monotone | 3.91886 | −0.15315575670859705 | −0.1531557567083821 | −0.1531557567083679 | −2.149×10⁻¹³ | −1.421×10⁻¹⁴ | −0.1531557567083669 | 9.992×10⁻¹⁶ | ✓ |
| 0.7 | monotone | 3.65753 | −0.38189231723441885 | −0.3818923172341835 | −0.38189231723416484 | −2.354×10⁻¹³ | −1.865×10⁻¹⁴ | −0.3818923172341632 | 1.610×10⁻¹⁵ | ✓ |
| 0.725 | monotone | 3.60334 | −0.9235558359313192 | −0.9235558359310385 | −0.9235558359310154 | −2.807×10⁻¹³ | −2.309×10⁻¹⁴ | −0.9235558359310133 | 2.109×10⁻¹⁵ | ✓ |
| 0.75 | monotone | 4.37697 | −1.600501661149428 | −1.6005016611490959 | −1.6005016611490799 | −3.322×10⁻¹³ | −1.599×10⁻¹⁴ | −1.600501661149079 | 8.882×10⁻¹⁶ | ✓ |

Eight window instants are monotone with p in
[3.60, 4.38]; the window's bottom instant
(t = 0.61875) is **degenerate** — d34 and d45 carry
opposite signs (−1.403×10⁻¹³ vs +8.882×10⁻¹⁶) at the
rounding floor, so the registered degenerate case
applies (L := v5, r := max(|d34|, |d45|) =
1.403×10⁻¹³ ≤ 1×10⁻⁶) and the instant is
limit-certified. Stated plainly, the anatomy is the
one Gate-26 §2 priced for Phase 256: the
combined-class clause minima are a read-level sector
off the marched state, interpolated onto the fixed
audit grid, and at these instants they are
grid-stable to ~10⁻¹³ — worst in-window |d34| =
3.322×10⁻¹³ (t = 0.75), worst |d45| = 2.309×10⁻¹⁴
(t = 0.725), worst residual r = 2.109×10⁻¹⁵ — so the
Richardson limit sits on top of the finest-grid
value and the p values are ratios of noise-floor
differences carrying no convergence information.
This is a **grid-stability certificate**, in the
sense registration §C fixed in advance; the bar is
met as registered and no CERT condition was waived —
CERT-2/CERT-3 still required the LIMIT to straddle
zero at the bracket with no earlier in-window
crossing, and it does, with the bracket-end limits
carrying essentially the standing-grid margins
(+0.051321249458261775 / −0.04804452588981167 at the
standing read; L = +0.05132124946169617 /
−0.048044525888048084).

**CERT booleans: CERT-1 TRUE** (no failures),
**CERT-2 TRUE** (L(0.675) = +0.0513212495 ≥ 0,
L(0.68125) = −0.0480445259 < 0; v5 likewise
+0.0513212495 / −0.0480445259), **CERT-3 TRUE** (no
earlier in-window crossing at L or v5 — all window
instants ≤ t_lo are positive at both), **CERT-4
TRUE** (no non-binding clause crosses first at G5
anywhere in the window up to t_hi — the worst
non-binding G5 minimum over window instants
≤ t_hi is NEC_θ = DEC_θ +4.202201045205472, and at
the hi end the next clause is +4.735863108240077;
non-clause bars at the bracket instants: momentum
worst 5.551×10⁻¹⁶ (0.675) / 4.718×10⁻¹⁶ (0.68125),
flare_min 0.11832 / 0.11714 > 0, domain_R_min
0.59201 / 0.58814 > 0, domain_exp2Phi_min 0.0058112
> 0 — all ok).

## 5. TAIL PRICING (§5(c) — ON THE FACE, AS
## REGISTERED, WITH ITS AMPLITUDE CAVEAT)

From THIS phase's fresh G3 and G4 rows (the §5(c)
adaptation: no stored multi-grid rows exist for this
pose): per-instant max G3–G4 disagreement over all
seven clauses at the sampled instants on
(0.75, 1.0] — 1.674898×10⁻⁶ (0.775),
2.080761×10⁻⁶ (0.8), 2.547347×10⁻⁶ (0.825),
3.207686×10⁻⁶ (0.85), 4.038276×10⁻⁶ (0.875),
5.230809×10⁻⁶ (0.9), 6.832713×10⁻⁶ (0.925),
8.975729×10⁻⁶ (0.95), 1.201325×10⁻⁵ (0.975),
1.632692×10⁻⁵ (1.0). First exceedance of the
1×10⁻⁶ bar on (0.75, 1.0] at the first tail instant,
**t = 0.775**; stage max =
**1.6326921098652747×10⁻⁵ at t = 1.0**, carrier
**WEC**, relative disagreement |d|/|v4| =
7.363195956559376×10⁻⁶. **Amplitude caveat (§5(c),
on the face):** past t = 0.7556858539654343 the tail
reads pose amplitudes beyond Phase 265's audited
delivery range [0, −3.5], reaching a(1.0) =
−5.753378225339471 at t = 1.0; this pricing is a
grid-disagreement record for reads in that
unaudited-amplitude regime — it prices the tail
reads' uncertainty, certifies nothing, and no tail
read is quoted as a clause verdict on the pose.
(Recorded without interpretation beyond the numbers:
the stage max is numerically close to Phase 256's
clamped-pose tail max, but the carrier differs —
WEC here, DEC_θ there — and the relative
disagreement differs (7.363×10⁻⁶ vs 1.893×10⁻⁶),
because the clause values at t = 1.0 are read under
different amplitudes (a = −5.753378225339471
unclamped vs −2.5 clamped). The tail price attaches
to the tail reads, exactly as the scope argument of
§1 provides.) This stands on the face of the form-1
verdict as fence (i): reads past the window are NOT
certified.

## 6. FILES

- `phase266/work/p2661_registration.md` — the
  registration (pre-run, fixed).
- `phase266/work/p2661_run.py` — driver (controls,
  probe, ladder marches, window reads, Richardson +
  CERT-1..4, tail pricing, verdict; 929.6 s).
- `phase266/results/p2661_results.json` — full
  record (controls, probe, window rows G3/G4/G5,
  tail rows, per-instant Richardson table, CERT
  booleans, tail pricing, verdict).
- `phase266/work/p2661_check.py` — independent
  checker (§8 below).
- `phase266/results/p2661_verify.json` — checker
  record.
- `phase266/results/p2661_memo.md` — this memo.
- No G5 kernel spec: the §5(d) obligation attaches
  only to form 3, which did not fire.

## 7. PROTECTED FILES — BYTE IDENTITY HOLDS

md5-identical before and after the run (29 files;
driver-recorded; checker re-verified live). Full
table in `p2661_results.json`
(`md5_protected_before/after`); the load-bearing
entries:

| file | md5 |
|---|---|
| phase129/work/p1296_derive_raw.json | d89f6a8646e4a96d7733c0b1827b5fcd |
| phase150/work/p1501_families.py | 9738b6267ec51a10f62db9f495b06b40 |
| phase162/work/p1621_engine.py | 1f12ec29c2693ca00a19da365abeccf4 |
| phase265/results/p2651_results.json | 6e2a20a062cf37a1d26add7ced05ca5b |
| phase266/work/p2661_registration.md | (in results table) |

## 8. CHECKER — 25/25 PASS

`phase266/work/p2661_check.py` →
`phase266/results/p2661_verify.json`: **25 passed, 0
failed** (checker wall 671.8 s, including its own
fresh G4 and G5 marches). The checks: protected byte
identity (live vs results before/after, two checks);
CTRL-2 recomputed independently from Phase 265's
stored rows (per-arm sampled brackets, refined
brackets and margins, cross-arm identity of the
refined brackets, clamp arithmetic, ladder/fixed-t
unclamped exactness — seven checks) and
recorded-pass consistency; CTRL-1 recorded outcome
consistent with its recorded diffs (all four
verdict-carrying diffs 0.0, sub-check flags true);
Phase 210 stored director t = 0.5 NEC_φ anchor
(+0.0045418770853060675); CTRL-3 recorded outcome
consistent; probe projection arithmetic (fires
False); **fresh G4 spot recomputation of both
bracket-end instants at diff 0.0**; **fresh G5 spot
recomputation of both bracket-end instants at diff
0.0**; fresh G5 director read at t = 0.5 reproducing
the recorded CTRL-3 diff exactly
(5.694021876223587×10⁻⁸); Richardson arithmetic
reproduced from the stored per-instant values;
per-instant v3/v4/v5 equal to the stored window
rows; CERT booleans reproduced (all true);
NEC_φ/DEC_φ pointwise identity in the stored window
rows (max diff 0.0 on G3, G4, G5); tail pricing
recomputed from the stored G3/G4 tail rows (first
exceedance 0.775, stage max
1.6326921098652747×10⁻⁵, carrier WEC, relative
7.363195956559376×10⁻⁶ — all exact); the
no-stop-parameter record check ('B_stop' absent from
the results; law recorded as UNCLAMPED); verdict
form consistent with §6's decision order (form 1).

One execution disclosure, on the face: the checker's
first launch was terminated by the runtime (SIGTERM
at 659 s) inside its G5 march, after its first 16
checks had passed (including the fresh G4 bracket-end
recomputation at diff 0.0) — an infrastructure kill,
no checker error and no mismatch. The identical,
unmodified checker was re-run detached and completed
25/25; every checker number above is from that
completed run.

## 9. FENCES (unchanged from the registration)

(i) Tail limitation (§5 above): reads past the
window [0.61875, 0.75] are NOT certified; the tail
pricing, with its amplitude caveat, stands on the
face as the tail reads' priced uncertainty.
(ii) Pose scope: Phase 169 A-branch datum, true lock;
κ = 0.3 director + C2 rotating headline construction
+ CH-PHI-Auu under P-PHI-TRIM-248 with the UNCLAMPED
law a(t) = −0.5 − c_trim·t², c_trim FITTED (§1) — as
posed. No stop parameter exists in this pose.
(iii) Jet scope / sector superposition: posed jet
entries, no coupled solve — no claim a physical
sector realises the channels jointly; exhibit ≠
construction. (iv) Programme-level sustainment
wording remains gated by p1592 regardless —
untouched by this verdict. The trim law is open-loop
and fixed in advance — ≠ the closed-loop
stabilisability proof (Phase 208) and ≠ Phase 217
V2; its coefficient is fitted and the certified
bracket lies outside the fit window — extrapolation,
on the record. Phase
210/214/226/229/233/243/252/256/265 verdicts stand
for their own poses and scopes; Gate-23's and
Gate-26's claim sets stand untouched. This
certificate is this phase's registered instrument,
adopted in advance — not a retroactive amendment of
Phase 265's registration, whose checkpoint named
exactly this successor.
