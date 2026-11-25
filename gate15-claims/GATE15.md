# Gate-15 — GATE RECORD (2026-11-23)

Gate: independent re-computation + novelty audit of Phase 122's
two claims. Machinery: the gate's own (W-A/W-B1/W-B2 — no phase
code), deciding reads packaged as Kaggle kernels under the
2026-11-23 standing order, verdicts rendered only after
fresh-process home re-judgement of the harvested outputs.

- **G15-1 (posed two-mouth configuration): SURVIVES IN
  RESTATED WORDING** — §1–§6 below. Joins the publication
  queue in the restated wording of §1.
- **G15-2 (measured shortcut in the constructed metric):
  NO VERDICT — PENDING.** Kernel 2 (`g15-wc`) failed at its
  Stage-0 control gate (a quadrature singularity in the L₁
  integrand); repair is in flight and its numbers have not
  been re-judged. §8. Nothing in this file is a G15-2 verdict.

Home re-judgement provenance: harvested Kernel-1 outputs in
`kaggle/outputs/v2/` (7 files; `PROGRESS.json` stage 5,
"complete — kernel 1 finished"; `wb2_check.json` 38/42 PASS —
the 4 failures are deciding reads, dispositioned in §4–§5, not
machinery faults). The re-judge rebuilt every response matrix
from the settled basis jets (`results/wb1_basis_jets.json`) and
the gate's channel functionals (`work_b2/wb2_functionals.json`)
with its own code and re-solved every registered set (numpy
lstsq and minimum-norm pinv): all deciding amplitudes,
residuals, ranks and singular values reproduce the kernel's
table to every printed digit. The second-path agreement table,
both failed confrontations, and the shell tail arithmetic were
likewise recomputed from the harvested fits (script run in the
home venv, 2026-11-23).

---

## 1. G15-1 verdict — SURVIVES IN RESTATED WORDING

The configuration claim itself is confirmed by the gate's
independent machinery: the complete condition set closes in
the full linearised Bach system at perturbative amplitudes,
and the joining shells are legal at both mouths, the member
control reproducing digit-for-digit. The claim as written
(ledger entry 261) does **not** survive verbatim: its
homogeneous-dimension clause is wrong (settled counts differ
at every ℓ ≥ 1, and at ℓ=1 four of the ten directions are a
verified pure-gauge family, not "all legitimate freedom"); its
[R̃]₂ coefficient is wrong; its uniform amplitude bound is not
reproduced in the settled basis normalisation; and closure
inside the (e)-quotient representatives alone — the deciding
question W-B1's dimension correction left open — holds on
residuals but **fails the amplitude bar at ℓ=1** (§4). The
restated wording, which is the publishable form, is:

> **MILESTONE (scan signal under attack; Gate-15: SURVIVES
> IN RESTATED WORDING): the two-mouth RE-MATCH CLOSES in the
> full linearised Bach system — a posed two-mouth
> configuration exists** (Phase 122, as corrected by
> Gate-15): the complete condition set ([B], [K], [R̃],
> [R̃_,n] + the angular Darmois pair per mode, round Σ,
> modes ℓ ≤ 3, ε ∈ {0.1, 1/30, 0.01, 0.003, 0.001}) is
> satisfied in the full homogeneous solution space —
> settled dimensions ℓ=0: 7, ℓ=1: 10 (four of them a
> verified pure-gauge family; (e) quotient 6), ℓ=2: 8,
> ℓ=3: 8 (all (e); response rank 6, full, at every mode) —
> with residuals ≤ 1.2×10⁻¹⁷ per unit ε^entering (bar
> 10⁻⁵) and amplitudes ≤ 2.2×10⁻² (bar 10²; worst mode
> ℓ=3). Restricted to the (e)-quotient representatives
> alone, the residuals still close (≤ 5.7×10⁻¹³) but at
> ℓ=1 the representative amplitudes reach 6.949×10³,
> above the 10² bar: the small-amplitude closing
> representative uses the full space, gauge directions
> included (physically inert; the quotient basis's
> smallest response singular value is 8.48×10⁻⁷ against
> the full set's 5.04×10⁻⁴). The joining shells are legal
> at BOTH mouths (shell sign minimum Ŝ⁰⁰/α₀ =
> +0.0202914453 at both; +0.0202882 after the corrected
> ℓ≥4 tail bound 2.459×10⁻⁶, ε = 0.1 row). The blindness
> sub-question is decided, not by identity: [R̃]₁ enters
> at ε² with +1.552938×10⁻³, [R̃]₂ at ε³ with
> −2.260117×10⁻⁴ (Gate-15 value, correcting the phase's
> −1.213920×10⁻⁴) — the (t,r)-sector identity does not
> extend to the full system. Scope fences: linearised
> pose (channels above ε⁴ and O(ε²) nonlinear terms
> unposed); formation PRE-EXISTING ONLY; (V-b)
> UNDECIDED: Pais–Uhlenbeck spin-2 ghost vs Mannheim
> PT-symmetric quantisation — opposed literature
> positions, B3 NOT COMPUTABLE (Phase 32).

---

## 2. Deciding numbers (gate reads, home-re-judged)

Response rank is **6 (full) in every set** — the phase's
rank-6 claim is confirmed on the settled bases. Solves of the
6-channel condition set ([B], [K], [R̃], [R̃_,n], [h_θθ],
[K_θθ]) against the gate's own extracted sources; bars:
residual ≤ 10⁻⁵ per unit ε^entering, amplitudes ≤ 10².

| Set | Power | max \|residual\| | max \|amplitude\| | Bars |
|---|---|---|---|---|
| ℓ=1 full (10) | main | 3.7×10⁻¹⁸ | 4.751×10⁻³ | PASS |
| ℓ=1 (e) quotient (6) | main | 5.7×10⁻¹³ | **6.949×10³** | **residual PASS, amplitude FAIL** |
| ℓ=2 (e) (8) | main | 7.2×10⁻¹⁸ | 6.210×10⁻³ | PASS |
| ℓ=2 (e) (8) | tail | 1.2×10⁻¹⁸ | 5.611×10⁻⁴ | PASS |
| ℓ=3 (e) (8) | main | 1.2×10⁻¹⁷ | 2.127×10⁻² | PASS |
| ℓ=3 (e) (8) | tail | 3.0×10⁻¹⁸ | 2.592×10⁻³ | PASS |

(Re-judge's own solves agree with the kernel's to all printed
digits; residuals differ only at the 10⁻¹⁸ round-off level.)

Smallest response singular values: full ℓ=1 set 5.04×10⁻⁴;
ℓ=1 (e) set 8.48×10⁻⁷; ℓ=2 7.43×10⁻⁴; ℓ=3 7.21×10⁻⁴.

**Shell sign (both mouths, corrected interior control).**
The control itself reproduces: fresh [R̃_,n]₀ =
−0.0152185839537 against the phase-stored −0.0152185840, and
Ŝ⁰⁰/α₀ = +0.0202914452716 against +0.0202914453 (the
0.65%-off value +0.0204228620559 in the gate's own W-A — and
inherited in Gate-9's W-B record — was the gate's machinery
error, a spurious 4Φ₁Φ₂A₀ term in a printed A‴ jet for
exp(2Φ₂); the phase-stored control was right throughout).
Shell minima after the gate's ℓ≥4 tail bound
(2×|[R̃_,n]₄| = 2.459×10⁻⁶ at ε = 0.1; the Ŝ⁰⁰ read carries
the [R̃_,n] tail with coefficient exactly 4/3, verified at
all three ε rows):

| ε | min Ŝ⁰⁰/α₀ | after tail bound |
|---|---|---|
| 0.1 | +0.0202914453 | +0.0202881661 |
| 1/30 | +0.0202914453 | +0.0202914129 |
| 0.01 | +0.0202914453 | +0.0202914447 |

Legal (positive) at both mouths at every row. Phase 133's
re-verified post-tail bound (≥ +0.02028927) sits 1.1×10⁻⁶
above the gate's ε = 0.1 read — a spread in how the tail
bound is applied, recorded here; it does not touch the sign
in any reading (the margin is 2.03×10⁻²).

**Member / truncation anchors (Stage 0–1, all PASS).**
Functionals match the home checkpoint at max rel diff
0.000e+00; A2 anchors reproduce (c = 0.0043023736 at all ℓ;
D3 [K]₁ = −4.270452×10⁻⁶, [R̃_,n]₁ = +5.514442×10⁻⁵,
[R̃]₃ = +8.570444×10⁻³ within their bars; S identity
S₀ = −2, S₁ = S₂ = 0, S₃ = −2 exact); κ anchors stand from
W-B1 (κ_full = −2.76430892×10⁻⁵; κ_enlarged = 0 exactly).

---

## 3. The classification settlement (W-B1, confirmed by Kernel 1)

- **ℓ=0: 7** — 3 MK tangents (δβ_MK, δγ, δk) + constant
  rescaling (pure gauge) + 3 (e). Phase's count correct.
- **ℓ=1: 10** — the phase claimed 9, "all (e)". The settled
  space is 10-dimensional and contains a **verified 4-dim
  pure-gauge family**: at ℓ=1 the tracefree angular basis
  E₁ ≡ 0 makes the G-component metrically vacuous, so the
  gauge family with Y = xʲ (j = 0..3), X = −fr²Y′ is a
  genuine perturbation of the (U, V, Θ) ansatz (pointwise
  linearised Bach ≤ 8.4×10⁻²⁴ at Σ; all four ID jets inside
  the settled span). (e) quotient: **6**.
- **ℓ=2: 8** and **ℓ=3: 8** — the phase claimed 7 each.
  The +1 at each of ℓ=2,3 is a **genuine non-gauge
  direction** the phase's system missed (negative control:
  the ℓ=2 gauge triples sit 0.29–0.73 away from the
  nullspace — not solutions in the ansatz; not gauge
  leakage).

## 4. The (e)-quotient amplitude failure — anatomy

The deciding question left by the dimension correction was
whether closure holds inside the correctly classified (e)
sets. It holds on residuals everywhere (worst 5.7×10⁻¹³,
seven orders below the bar). On amplitudes it holds at
ℓ=2,3 and **fails at ℓ=1**: the unique solve in the six
settled quotient representatives needs a component of
amplitude 6.949×10³ (bar 10²).

The failure is a conditioning property of the representative
basis, and the re-judgement prices it exactly: the (e) set's
response singular values are (8.42, 2.87, 0.941, 1.03×10⁻³,
3.23×10⁻⁴, **8.48×10⁻⁷**), and the ℓ=1 source's component
along the weakest left-singular direction is 5.992×10⁻³ —
the largest of its six components — so that direction alone
demands amplitude ≈ 5.992×10⁻³ / 8.48×10⁻⁷ ≈ 7.1×10³. The
full 10-element set's weakest direction is 5.04×10⁻⁴
(594× stronger), and the same source closes there with max
amplitude 4.751×10⁻³. The closing solution's physical
content is one equivalence class; its small-amplitude
representative uses the full space including the four
verified pure-gauge directions, whose admixture changes the
metric representative, not the geometry. The gate therefore
records the quotient-basis amplitude failure on the claim's
face (it is in the restated wording) but does not let a
basis-conditioning artefact kill a configuration whose
closure, rank, and shell legality are independently
confirmed. The phase's own amplitude figure (≤ 4.4×10⁻³)
was a full-space number of exactly this scale; in the
gate's settled normalisation (basis elements rescaled to
unit max |Taylor coefficient|) the per-mode full-space
maxima read 4.751×10⁻³ (ℓ=1), 6.210×10⁻³ (ℓ=2),
2.127×10⁻² (ℓ=3) — the claim's uniform 4.4×10⁻³ bound is
not reproduced mode-by-mode, and the restated wording
carries the gate's numbers against the 10² bar instead.

## 5. Source corrections and the second path

Two Phase-122 stored coefficients are **wrong** and are
corrected on the record; in both cases the gate's primary
(40-digit mpmath) extraction and its independent second path
(200-point Gauss–Legendre, float64) agree with each other
and disagree with the phase:

- **[R̃]₂ main coefficient:** phase −1.213920×10⁻⁴ →
  gate **−2.260117×10⁻⁴** (second path −2.259596×10⁻⁴;
  mutual agreement 2.3×10⁻⁴). The claim's qualitative
  decision — [R̃]₂ is decided nonzero (gate blindness
  check: |coeff| 2.26×10⁻⁴ vs the 3.4×10⁻⁶ decision
  floor), so the (t,r)-sector identity does not extend —
  **stands**; only the value is corrected.
- **[B]₂ tail coefficient:** phase-extracted −1.268835×10⁻⁵
  → gate **−5.210158×10⁻⁴** (ratio 41.1×; second path
  agrees to 1.7×10⁻⁹). The ℓ=2 tail solve closes on the
  corrected source within all bars (§2), so no verdict
  turns on the phase's value.

All other confronted literals reproduce (ℓ=1: [B]₁
+6.0145368205×10⁻³, [K]₁ −4.2545060×10⁻⁶, [R̃]₁
+1.5529383458×10⁻³, [R̃_,n]₁ +1.6228184576×10⁻³ — rel
diffs ≤ 2.9×10⁻⁷ against the phase).

**Second path (registered bar: 5% on deciding
coefficients).** Recomputed from the harvested fits: 17 of
18 deciding coefficients agree within the bar (worst
passing: [R̃_,n]₃ at 1.61×10⁻²). One breaches:
**[R̃_,n]₂ main, 8.76×10⁻²** (primary −4.176670×10⁻⁴ vs
GL-200 −4.542733×10⁻⁴). The breach is recorded, not
waived. Its materiality is nil and is demonstrated, not
asserted: re-solving the ℓ=2 main system with the
second-path source vector in place of the primary shifts
every amplitude by ≤ 4.1×10⁻⁶ and leaves max amplitude at
6.209×10⁻³ with residuals at 4.3×10⁻¹⁸ — the closure
verdict is insensitive to this coefficient at the observed
discrepancy. (The [R̃_,n] channel is the same channel whose
ℓ=0 control sits at the stored-β_MK evaluation floor,
3.4×10⁻⁹; see STATUS.md's Kernel-1 repair addendum.)

## 6. Phase 133 and Phase 141 flags — dispositioned

**Phase 133 flags** (full record: `results/gate15_p133_flags.md`):
1. *Corrected tail bound* — ADOPTED. Phase 122's 2.06×10⁻⁶
   is superseded by 2.459×10⁻⁶; the gate's own ℓ=4
   extraction concurs independently (2×|[R̃_,n]₄| at
   ε = 0.1 = 2.4594×10⁻⁶). The shell verdict is read
   against the corrected bound in §2.
2. *Second-order ℓ=0 pricing* — RECORDED, does not move
   the linearised verdict. κ⁽²⁾ = 0 is achievable only
   via amplitudes ~2714 per unit ε², far above the 10²
   bar, and the shell sign at second order survives only
   at D/r_Σ = 100 (ε = 0.01). The G15-1 claim is a
   linearised claim and is not priced at second order;
   the price rides with the claim wherever it is stated
   beyond linearised scope.
3. *Chronology (P133-1)* — RECORDED. Protection is
   POSTURE ONLY; no deciding term exists inside the
   configuration. Consistent with the gate's C12
   accounting: no wording implies formation, superluminal
   travel, or a decided chronology statement.

**Phase 141 flags** (CHECKPOINT141; ledger 352–355):
1. *The second-order price is irreducible in the
   registered basis* (P141-1) — RECORDED. The SVD anatomy
   shows the load L_J[p2] is carried entirely by one
   component (amplitude +82.806); removing it breaks the
   registered 10⁻²⁰ row-residual bar. κ⁽²⁾ itself never
   moved (≤ 4.4×10⁻¹⁶). The named decider for the
   residual doubt (a 40-digit reassembly of the prolonged
   matrix — the two engines read the smallest singular
   value 5.3× apart, below their mutual assembly
   difference) remains an open follow-up, not a gate
   blocker: it prices the second-order extension, not
   the linearised claim.
2. *The pose stands at second order at D/r_Σ = 100*
   (P141-3) — RECORDED as the claim's Gate-carryable
   second-order form: `phase141/results/p1413_memo.md`
   §5, quoted in the gate's files. At ε = 0.01 the
   second-order shell sign at both mouths is
   Ŝ⁰⁰/α₀ = +0.00402664 > 0 (first-order margin
   +0.0202914453, second-order excursion −0.0162648021,
   measured ℓ≥4 tail 3.07×10⁻¹⁰), with the
   perturbativity bar met in its excursion form
   (|δβ⁽²⁾|ε² = 0.271448 = 0.127×β_MK; |a_e⁽²⁾|ε² =
   0.0274). This statement is ℓ=0's. The ℓ≥1
   second-order components computed by P141-4 are each
   ≤ ~9×10⁻³ per unit λ² before ε-suppression, so
   nothing computed threatens the +0.00402664 read; the
   ℓ≥1 deciding term itself rides the p1414 kernel,
   unharvested — the second-order standing beyond ℓ=0
   is therefore **not before this gate** and no wording
   may present it as gate-judged.
3. *Machinery items* (P141-2's radial-ODE premise —
   structurally rank-deficient, a Bianchi-type identity;
   P141-5's moving-mouth refusals at two priced points,
   missing datum = the fixed-ω homogeneous response at Σ)
   — RECORDED as open follow-ups. Neither is a verdict
   on G15-1, which is a static-pose claim.

## 7. Novelty (W-D audit, complete)

Both claims grade **PARTIALLY KNOWN** (`results/wd_novelty.md`;
queries logged in `results/wd_search_log.md`). Delimitation:

- **G15-1:** the exact pose — two MK-exterior mouths joined
  in one linearised two-centre Bach exterior with the full
  conformal join set closing at ℓ ≤ 3 and positive shell
  density at both mouths — **was not found in the search**;
  every ingredient is published (single-mouth conformal
  wormholes: Lobo 2008; Varieschi & Ault 2016; Oliva, Tempo
  & Troncoso 2009; Hohmann et al. 2018; Cadoni et al. 2025;
  the MK thin-shell two-copy construction: Bochicchio &
  Laserra 2013 — one shell joining two copies, not two
  mouths in one exterior; the BDE junction formalism
  itself: Berezin, Dokuchaev & Eroshenko, arXiv:1710.10438;
  the two-mouths-in-a-common-exterior pose in GR: Schein,
  Aichelburg & Israel, gr-qc/9602053, and the MMP line).
- **G15-2:** the effective-shortcut concept and two-mouth
  transit-time computations are published (Morris–Thorne;
  Visser; Fu, Grado-White & Marolf arXiv:1908.03273;
  Maldacena & Milekhin PRD 103 (2021) 066007 — whose
  accounting's verdict is *no* shortcut); a shortcut
  accounting whose exterior leg is evaluated **inside a
  constructed two-mouth metric** was not found in the
  search, in any theory reached.

Coverage gaps (stated in the audit, carried here): web-index
search only — INSPIRE-HEP and Semantic Scholar reached via
web indexes, not direct sessions; no exhaustive arXiv
listing-API sweep; forward citations of BDE and of
Bochicchio–Laserra not systematically enumerated (a later
paper applying BDE to a two-centre problem is the most
plausible miss); English-language only; searches run
2026-11-23. Per the claim gate, no wording may call either
claim unique/first/record: the publishable form is "not
found in our search (limits: as above)".

## 8. G15-2 — NO VERDICT (pending)

Kernel 2 (`g15-wc`, the transit numbers: thresholds
D*_τ = 4016.023 r₀, D*_t = 3592.719 r₀; gains G_τ/G_t at
D/r_Σ = 10/30/100; tides) launched and **failed at its
Stage-0 control gate**: the L₁ integrand divides by
√(1 − r^(−0.9)), which vanishes at a quadrature node
(mpmath ZeroDivisionError at the first integral, ~10 s
in). No Stage-1+ number exists from the kernel, and the
phase's stored literals (L₁ = 1005.3728512079 r₀,
T₁ = 794.1997332925 r₀) were not re-verified by it.
Repair is in flight (parent's line); G15-2's verdict
renders only on harvest + home re-judgement of the
repaired kernel. Two fences stand in the meantime:

- The Kernel-2 fence (its README): clauses (i)/(ii) are
  inherited from G15-1. G15-1 has now SURVIVED IN RESTATED
  WORDING, so the conditional is satisfiable — but it is
  satisfied by the restated claim, and any G15-2 wording
  must inherit the restated form, not ledger 262's
  original.
- Phase 141's §5 statement quotes effective transit gains
  with O(ε²) remainders (G_τ = 23.00840 [23.00838,
  23.00844]; G_t = 17.31288 [17.31288, 17.31290]). Those
  are Phase 141's second-order ℓ=0-sector numbers, carried
  in §6 as part of the G15-1 flag disposition. They are
  **not** a G15-2 verdict and must not be cited as one.

## 9. Publication consequence

- **G15-1 joins the publication queue** in the restated
  wording of §1 (standing rule: gate-passed findings push
  without asking; ungated or failed results wait). The
  bundle must carry: the classification settlement (§3),
  the quotient-amplitude anatomy (§4), the two source
  corrections (§5), the second-order price and its
  D/r_Σ = 100 scope (§6), the PARTIALLY KNOWN novelty
  grade with its citations and stated search limits (§7),
  and the standing fences (linearised pose; formation
  PRE-EXISTING ONLY; (V-b) UNDECIDED verbatim; chronology
  POSTURE ONLY). Ledger entry 261 is to be replaced by
  the gate's restated text at publication time (parent's
  edit, per the standing gate-replacement pattern).
- **G15-2 does not join the queue.** Ledger entry 262
  stays GATE-QUEUED / under attack until the repaired
  Kernel 2 is harvested and re-judged.
- The Gate-9 record flag stands (STATUS.md): Gate-9's W-B
  recorded the same erroneous shell value +0.0204228620559
  inside its 2% bar; the number must not be reused as an
  anchor. Gate-9's verdict is not re-litigated — the
  offset did not move it.

INTERNAL only. Nothing uploaded, nobody contacted.
