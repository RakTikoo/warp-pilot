# P318 memo — FU-P237-1a: the augmented-basis re-solve

**VERDICT: SECTOR-BY-SECTOR** — all four arbitration sectors completed
with verdicts; the fully arbitrated assembly passes the Ellis gate and
the whole Ellis core at all powers; the final read is blocked at
exactly one core background (A throat) on one named datum. **No
identification is claimed** (the IDENTIFICATION form requires the core
complete; see §5).

Registration: `phase318/work/p318_registration.md`, filed before any
Phase 318 computation. Frame: Phase 259's engines and conventions
throughout (programme E; bridge print H = −E; prefactor ratio 210;
Eq. (3.14) weights as printed). Inherited as fixed: Phase 259's D1
conclusiveness (the residual is not a reading artefact under R0–R6 —
not re-litigated) and the D2 generic-θ completion gap (inherited as a
gap, §6).

## 1. Control — PASS

Phase 259's assembled record was reproduced from the stored artefacts
by re-running the stored stage-4 machinery (control worker;
`work/control/`): every reproduced value deviates from
`p2591_assembled.json` by **exactly 0.0** — throat ξ⁰ T^r_r =
16.000000000000057 (the stored float residue of the exact +16; the
exact-rational attribution −608/9 + 672/9 + 24/9 + 56/9 = 16 stands),
T^t_t = T^θ_θ = 0 at residue class, decay 16 / 0.2914043092852623 /
0.052978515625 / 0.0028962020126912513 over Ellis R = 1/1.5/2/3, core
ξ¹/ξ²/ξ³ maxima 3.41×10⁻¹³ / 6.82×10⁻¹³ / 2.84×10⁻¹³, P(ξ) =
[203, −1806, 5460, −4200]. One wording correction to the inheritance:
the stored route-(ii) per-power S_T values are
[−8.1×10⁻¹⁶, +2.0×10⁻¹⁵, −6.5×10⁻¹⁵, 0.0] — max 6.5×10⁻¹⁵, passing
Phase 259's 1×10⁻¹² bar; a literal "all powers ≤ 2×10⁻¹⁵" bound is
not met by the stored values themselves and is not repeated here.

## 2. Sector (iii) — the ξ⁰ assembly weights: CORRECT, move exactly 0

Every Eq. (3.14) weight was re-expanded independently (exact
Fractions) and cross-checked against the printed forms, the Phase 241
checker, and the Phase 259 harness `WEIGHTS` Stage 4 uses — agreement
as full polynomials, all ten tensors. ξ⁰ constants: H{2,0}(1) 1/56,
H{2,0}(3) 1/140, H(6,3)(1) +1/216, H(6,3)(2) −1/180, H(6,3)(3) −8/945,
H(6,3)(4) 2/315, H(6,3)(5) +1/180, H(6,3)(6) 1/1260, H(6,3)(7)
17/7560, H(6,3)(8) −1/270; prefactor 210 exact. **The +16 is not a
weights-bookkeeping artefact; this inheritance item is discharged.**
(`work/weights263/`)

## 3. Sector (iv) — the 263-group scalar: it is H(6,3)(4); it was never missing

Exact identification (Phase 259 engine, jets 11/23/37 + fresh 71/101):
the (2,4)-trace of a Riemann factor is Ric exactly, and the flagged
scalar is identically S₂₆₃ = R_{pq}R_{rs}R^{prqs} — DF §2.1's 4th
R⁰_{6,3} basis element, §2.3 Eq. (2.9) action term, whose variation
§2.4 Eq. (2.27) defines as **H(6,3)(4)**, entering the ξ⁰ assembly at
weight 2/315 (bracket coefficient 4/3) inside the kept-print REST
aggregate. It cannot explain the +16 as an omitted term. Checkpoint
259's inheritance item 3 is reworded accordingly: "outside
span{tr Ric³, R·Ric²}" is true, but the scalar is inside the a₃ basis;
only its print tensor's correctness was unarbitrated — which is sector
(ii). (The tasking's "−263 on jet 37" does not match the record: the
group's values are 263 / 1263/2 / **−275/4** on jets 11/23/37.)

## 4. Sectors (i) and (ii) — derivations, certificates, arbitration

**H(6,3)(3) = −E[tr Ric³]** (43 patterns) and **H(6,3)(4) =
−E[R_{pq}R_{rs}R^{prqs}]** (84 patterns) were derived with Phase 259's
Part A machinery (`work/h34/`): analytic-P vs engine diff 0, two-route
E agreement diff 0, pattern lists vs E diff 0 (jets 11/23/37),
conservation ∇^aE_ab **exactly (0,0,0,0)** on generic rational jets
11/23/37 for both, harness SSS S ≤ 8.9×10⁻¹⁶ at Ellis ℓ = 0/1/2,
tr E_alg = L at D = 4 exact. Throat values (DF print units, Tt/Tr/Tθ):
H(3) = (32, 8, 44); H(4) = (4, 4, 16).

**H{2,0}(3)**: the Stage 1b byproduct E2 = E[−(∇Ric)²] was arbitrated
(`work/h203/`). On the print contents preserved in the record it
**AGREES**: of the three coefficients Phase 241's Control 0 preserved,
□□Ric_ab (print −1 vs derived programme +1 under the bridge) and
∇_a∇_b□R (print +1 vs derived −1) are uniquely forced by a
principal-sector probe (rank 4/5, residual 2.7×10⁻¹², zero nullspace
component), and the trace coefficient (print −1/2) agrees at the level
of its unique principal invariant (the split between the two
g-monomials is an exact null direction, not arbitrable). E2 is
conservation-exact on generic jets 101/202 (Phase 259) and on both
Ellis jets computed here; print H{2,0}(3) is one of Phase 241's seven
conserved tensors, so conservation cannot discriminate. E2's throat
values (programme mixed) are (−80, −16, −112); print candidate −E2 =
**(80, 16, 112)**.

**The isolation problem, and its resolution.** In Phase 259's assembly
the three tensors enter only through the ξ⁰ aggregate
REST = (1/140)H{2,0}(3) − (8/945)H(3) + (2/315)H(4), backed out
exactly — one equation, three unknown tensors, so no individual print
tensor is isolated by the record. The joint arithmetic at the throat
(exact rationals) is:

- REST_print = (44/135, 4/27, 100/189) (DF-sum).
- Derived weighted (3),(4) combination: (−232/945, −8/189, −256/945).
- Implied print H{2,0}(3) **if** print (3),(4) = derived:
  **(80, 80/3, 112)**.
- Direct evaluation of printed Eq. (2.27) on the Phase 241 driver
  machinery (Task D; H(6,3)(2) control exact) gives print H(4) at the
  throat = **(4, 4, 16) = derived, exactly** — H(4) individually
  agrees at the throat.
- The implied print H{2,0}(3) agrees with the derived tensor in Tt
  (80 = 80) and Tθ (112 = 112) **exactly** — neither equality is
  forced by the construction — and differs only in T^r_r:
  **implied print 80/3 vs derived 16**, a difference of 32/3 in H
  units, whose weighted assembly effect is (3/2)·(32/3) = **16 —
  exactly the residual**.

A competing single-carrier attribution was considered and discharged:
the Phase 241 driver's REST cross-check is off by −8/105 (DF-sum) in
Tr, which would be explained if print H(4)'s throat Tr were 16 rather
than 4 (an m10 trio-term reading). Task D's direct Eq. (2.27)
evaluation — the print form itself, control-validated — gives Tr = 4,
so the −8/105 sits in the driver's trio transcription (the same
residue family as Phase 259's §2 residues), not in the print tensor
and not in Phase 259's assembly, which never used trio evaluations.

**Sector verdicts.** (i) H{2,0}(3): **DIFFERS** — in exactly one
number the record can reach: its throat T^r_r. All preserved pattern
coefficients agree and Tt/Tθ implied values agree exactly; the
difference lives in the part of DF Eq. (2.23) that Phase 241's
Control 0 did not preserve. (ii) H(6,3)(3): **joint-consistent**
(weighted combination matches print's exactly at the throat under the
implied split; conserved as printed per Phase 241); individual
isolation impossible from the record. H(6,3)(4): **AGREES** at the
throat by direct print-form evaluation, and joint-consistent.

## 5. Stepwise re-assembly and the final read

Substitution delta (bracket units):
Δ_c = 210·[(1/140)H{2,0}(3)_c − (8/945)H(3)_c + (2/315)H(4)_c −
REST_print_c], all H in print units. (Sign convention verified against
Phase 259's only5 move: 210·(1/180)·(+64) = +74.667.)

Throat ξ⁰ residuals (Tt, Tr, Tθ), stepwise as registered:

| step | residual |
|---|---|
| Phase 259 FULL (print REST) | (0, **+16**, 0) |
| after (iii) weights audit | (0, +16, 0) — move exactly 0 |
| after (iv) 263 scalar | (0, +16, 0) — no omission; it is H(4), inside (ii) |
| after (ii) derived (3),(4), conditional on implied print H{2,0}(3) | (0, +16, 0) — move 0 in all components |
| after (i) derived H{2,0}(3) substituted | **(0, 0, 0) — exact** |

Sectors (i) and (ii) are not separately substitutable from the record
(REST is one back-out equation); the (ii)-conditional row uses the
implied print H{2,0}(3), and the joint substitution — the only one the
record licenses — is the last row combined with it.

Final read of the fully arbitrated assembly (derived (5),(6),(8-B)
from Phase 259; derived H{2,0}(3), H(3), H(4) here; weights audited):

- **Core ξ⁰** (coordinator's off-throat E2 evaluation, float route
  validated against the exact throat and ℓ=1 records to ≤10⁻¹³,
  div E2 ≤ 2.7×10⁻¹⁵; `work/p318_ellis_e2_offthroat.py/.json`):
  Ellis R=1: **0 exactly**, all components. R=1.5: max 5.1×10⁻¹⁴
  (Tt −5.1×10⁻¹⁴, Tr −4.1×10⁻¹⁵, Tθ +1.1×10⁻¹⁶). R=2: max 2.5×10⁻¹⁵.
  R=3: max 1.2×10⁻¹⁵. The Phase 259 decay profile
  16 / 0.291 / 0.053 / 0.0029 collapses to the ξ¹–ξ³ residue class.
- **Core ξ¹/ξ²/ξ³**: unchanged (the REST sector is ξ⁰-only), maxima
  3.4×10⁻¹³ / 6.8×10⁻¹³ / 2.8×10⁻¹³ — PASS at the registered bars.
- **Ellis gate**: P(ξ) ξ⁰ coefficient 203 → **187 exactly**; P(ξ) is
  now exactly the target polynomial, so the P root is the target
  0.86035766893. Forced deficit, Δρ, Δp_t unchanged (already passing;
  their throat ξ⁰ Tt/Tθ deltas are 0). Δp_r: Phase 259's readout
  attributes its entire excess to the throat Tr ξ⁰ error read at
  ξ = 1/6 (16/(20160π²) = 8.04×10⁻⁵, exact); that error is now
  exactly 0 and ξ¹ is unchanged, so Δp_r lands on target at the
  passing reads' residue class. NEC roots likewise return to targets
  within the ξ¹–ξ³ residue class by the readout's single-defect
  attribution (labelled: attribution-based, not an independent gate
  re-run). Family-D ξ³ keeps the 1680-unit THA charge (unchanged
  sector).
- **Conservation per power**: every tensor in the arbitrated assembly
  is individually certified (S exactly 0 on generic rational jets;
  ≤ 8.9×10⁻¹⁶ on SSS harness reads for the tensors derived here;
  Phase 259 certificates for the rest), and each power's assembly is a
  constant-coefficient linear combination — the arbitrated assembly
  is conserved per power at the certificate class; Phase 259's
  assembled route-(ii) values (max 6.5×10⁻¹⁵) stand as the float read
  for the unsubstituted remainder.
- **A throat — NOT RE-READ.** Phase 259's ξ⁰ values stand there
  (Tt 0.0, Tr +2.0, Tθ −7.0). Blocker, named exactly: no derived
  H{2,0}(3) evaluation exists on the A-family background — the
  ∇-sector engine's jet evaluations cover generic and Ellis jets, and
  the A background enters the harness through a Riemann-jet solve
  (`solve_Rjet_throat`), not a closed-form metric jet an E2 evaluation
  can consume. The isolating datum is an E2 evaluation on the
  A-throat jet, or a full DF Eq. (2.23) transcription evaluated on the
  A backgrounds. Conditional prediction for that datum: if the
  A-throat residual is likewise carried wholly by H{2,0}(3) (with
  print (3),(4) = derived there; implied print = (9/4, 25/12, 7/12)),
  the derived H{2,0}(3) at A throat must read **(9/4, 3/4, 21/4)** in
  print units. The wider set's ξ⁰ maxima (C 250, E 108, D 7.997) are
  likewise not re-read; they were reported, not deciding, checks in
  Phase 259.

## 6. Fences and inheritance

No identification wording: the IDENTIFICATION form requires core +
gate at all powers, and the core's A-throat point is unre-read — the
identification is established at the throat, the full Ellis core, and
the gate, and is one named evaluation short of the registered form.
Phase 259's D1 stands untouched. The D2 generic-θ completion gap is
inherited as a gap, unchanged. The THA Eq. (26) ξ³ defect stands as
recorded. Checkpoint 259's inheritance item 3 (the 263 scalar) is
superseded by §3 above. The published-data route's remaining open
item is now a single evaluation (E2 on the A-throat jet) plus, for
full-tensor arbitration of H{2,0}(3), a faithful DF §2 Eq. (2.23)
text — the same journal-text absence Phase 255 recorded.

DESK: NO DATA CONTACT — every read is stored-record versus
first-principles derivation; no external data was consulted.
