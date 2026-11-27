# GATE-52 CHECKPOINT — verification of the Phase 412 claim set

Charge: ledger entry 1077 (parent agent). Claims: entry 1076
(Phase 412 verdict). Precedents read: Gate-50 verdict + riders
(entry 1066, `gate50/GATE50.md`, esp. G50-R5 at-the-criterion
discipline), Gate-43 C-10 calibration.
**Verdict: the claim set SURVIVES as fenced in `GATE52.md` §1
(G52-A/B/C/D with riders G52-R1…R4).** No ledger append, no
publication, no user contact — the verdict returns to the
parent agent.

## 1. Files

Deliverables: `gate52/GATE52.md`, this checkpoint.
Machinery (`gate52/work/`):
- `g52_extract.py` — stored inputs from the primary artefacts
  (md5s recorded in the output).
- `g52_lib.py` — the gate machinery: Cartan structure equations
  in an orthonormal tetrad + forward-mode Taylor jets; own
  not-a-knot spline; certified worst-null (Fibonacci scan +
  pattern search + chart-Newton polish + KKT/PSD certificate).
  numpy + json only; no phase/gate imports.
- `g52_calibrate.py`, `g52_run.py`, `g52_polish.py`,
  `g52_arith.py`, `g52_mp.py`, `g52_admit.py`.
Results (`gate52/results/`): `g52_stored_inputs.json`,
`g52_calibration.json` (ALL_PASS), `g52_numbers.json`,
`g52_polish.json`, `g52_arith.json`, `g52_mp.json`,
`g52_admission_laptop.json`. md5s at the end of this file.

## 2. Evidence summary (VM deciding reads)

Controls: BASE at diff 0.0 (joint/nec/dec/wec/worst-null;
sec +5.4×10⁻²⁰); CRIT joint +1.6×10⁻¹⁹, worst-null +1.1×10⁻¹⁹,
peak 0.0. Calibration CAL-1…CAL-10 ALL PASS (worst items:
spline vs scipy 1.3×10⁻¹⁵; Schwarzschild 2.1×10⁻¹⁸; ρ closed
form 2.7×10⁻¹⁸; rotation orthogonality 2.2×10⁻¹⁴; Type-I
margin invariance 1.8×10⁻¹⁸).

(a) m2 winner SET read: joint +6.699288757137218×10⁻⁷ at
r = 18.170731707317074 (stored diff −3.9×10⁻¹⁹), Type-I
fraction 1.0; certified worst-null +1.6577507677226363×10⁻⁷
(diff −5.4×10⁻²⁰, KKT residual 4.2×10⁻²¹, PSD +6.35×10⁻⁷);
polish +6.489725143843286×10⁻⁷ at the stored radius (diff
+2.6×10⁻¹⁹). Peak: achieved = target = H2 peak =
0.8853484980534808 exactly, at r = 10, on FINE_R and a
20 001-point dense scan; SS7 halving/doubling float-exact →
**construction (G52-R1)**. Winner's first knot = H2's S(10)
float exactly.

(b) m5 winners: gate joints −6.528451×10⁻⁵ (K9) /
−6.526398×10⁻⁵ (K17), sampled minima at non-Type-I points,
within the C-10 band of the stored pair; frame-invariant
companions at roundoff (Type-I NEC min diff −6.4×10⁻¹⁹; DEC
min −6.4×10⁻¹⁹; Type-I fractions exact); certified worst-nulls
−6.557749×10⁻⁵ (r = 15.0 node) / −6.602178×10⁻⁵ (r = 15.2439
node) for K17, −7.660353×10⁻⁶ at the Type-I argmin point;
polish −1.7758241945718385×10⁻⁵ at the stored radius (diff
+1.4×10⁻¹⁹). Screens audit: 760 screens (280/280/200), zero
rejected, no m5 screen ≥ 0; stored K9/K17 agreement
1.5259×10⁻⁸; gate pair agreement 2.1×10⁻⁷ (C-10 band).

(c) Spends recompute at diff 0.0; local exponents 2.0952 /
4.9268; Gate-50 law from its own spends: exponents
2.0964/2.0945, coefficient 8.692277×10⁻⁷; refit A, p, crossing
(0.8650138528482604) at diff 0.0; crossing below the legal
rung → fit failure on the face, measured bracket governs.

(d) Peak orders above P\*: 6.0529. Fit law: spend(10⁶) =
1.021×10¹⁷, 22.86 orders short. Local-exponent law: 29.54
orders. Naive Gate-50 quadratic: 12.39 orders (understates).

mpmath (50-digit, §5 of GATE52.md): margins agree ≤ 9.3×10⁻¹⁹
at the two Type-I named points; worst-null polishes agree at
+1.0×10⁻¹⁹ (m2 point) and +2.1×10⁻¹⁹ (m5 sampled point);
block eigenvalues ≤ 1.9×10⁻¹⁹.

Laptop admission: ADMITTED at roundoff (all diffs
≤ 6.5×10⁻¹⁹; KKT residuals ≤ 2.3×10⁻²⁰; argmin radii and
Type-I fractions identical).

## 3. Incidents

1. Frame-rotation einsum orientation bug in the first build —
   caught by the BASE control (ρ exact, margins off by
   ≈ −9.5×10⁻³ uniformly; That_nat was correct, isolating the
   rotation). Fixed, CAL-10 added, calibration re-run ALL PASS,
   deciding reads re-taken. No claim read from the broken build
   was used anywhere.
2. First mpmath comparison used raw components across
   differing tangential eigh bases (γ's tangential eigenspace
   is exactly degenerate) — spurious diffs up to 7.9×10⁻⁵ in
   flux components. Resolved by basis-invariant comparisons
   (block eigenvalues, eigenvalue margins, transferred-direction
   worst-nulls): agreement ≤ 9.3×10⁻¹⁹ throughout.
3. `g52_admit.py` needed two key-name fixes against the final
   `set_read` summary schema (no data impact; the laptop run
   was re-executed clean).

## 4. Standing fences carried onto the set

Band [10, 20]; SEC −2.917201×10⁻⁴ printed wherever the
candidate is quoted; NO member, NO EC pass; C-10 naming
throughout; G52-B search-scoped (never a non-existence proof);
G52-D fit-based (the measurements are G52-A and G52-B only);
G52-R4 lineage wording. Next gate number remains 53,
serialised by the parent in landing order (408/410/411/413
referrals outstanding).

## 5. Artefact md5s

```
f94607e41f6089e176d2506941091154  results/g52_admission_laptop.json
31b2db669649d5bdd57882c2cce77cb8  results/g52_arith.json
9def71bc5673eddfbc518e06a3c13ab5  results/g52_calibration.json
162c52d91390e2b4e8c112cae9f70768  results/g52_mp.json
6990e0152dd4547f35533dad173ba001  results/g52_numbers.json
6ff2af990a1b357e37e6f56b79d3efd4  results/g52_polish.json
61186777dd0c1675a39534062c332e51  results/g52_stored_inputs.json
d413d24350a947f0ec98c7266a21da93  work/g52_admit.py
0c2e20a2a37f3ede86ddd7252707952c  work/g52_arith.py
be19e635fe8a0b6b9bbd46bfa98c5f36  work/g52_calibrate.py
cd9035cab27104a3d9629a6633536abc  work/g52_extract.py
f600e2d7695f075626f849a93d9b636e  work/g52_lib.py
cbe5d3c0e537940e1be90c9da5db849e  work/g52_mp.py
c891072be056c0bae0ef7dda4615b00f  work/g52_polish.py
ecf75918aa89132d53cb73ffb5d093f7  work/g52_run.py
```
Stored-input source md5s (in `g52_stored_inputs.json`):
p344_confirmation bca93c039daf9c8baf68f4e567abe873 ·
p379_confirmation 1bcb8b3900026cc78e6aacb33654ad72 ·
p400_confirmation 7a7792e3941380d23d38e959f0cd0b6f ·
p405_confirmation 9b6a30cf3e17343288e69a7103a7f66d ·
p412_rungs d57b7c02e13413f56f6a09845c59073b ·
p412_fit ab6971c10f94f2cc5ba0c7c2edb57b55 ·
p412_controls f63f9aebd1f588c4ea9d9a073737ef0a ·
p412_screens b544a1a17b53f42d0833f98e6c02396d.
