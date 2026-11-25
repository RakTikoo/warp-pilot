# Gate-15 claims — RESULTS (release v1.19.0)

One claim from Phase 122 — the posed two-mouth
configuration (G15-1) — put through Gate-15
(2026-11-23): the programme's standing two-part
gate — an independent second-path recomputation AND a
documented literature novelty search, under the ruling
"verify everything and tell honestly what you found,"
with the Uniqueness Protocol amendment of 2026-11-22
applied to every wording. Full gate record: `GATE15.md`
in this folder; verifier code and numbers in `code/`
and `results/`; the phase-source records the claim
rests on in `sources/`; file-by-file provenance in
`MANIFEST.md`. Phase 122's second claim (G15-2, the
measured shortcut in the constructed metric) received
NO VERDICT at this gate — its deciding kernel failed
at its Stage-0 control gate, and its repair and
relaunch are pending — so this bundle states no G15-2
result; see the pending note at the end.

**Count: SURVIVED INTACT 0 · SURVIVED IN RESTATED
WORDING 1 · DEAD AS OURS 0 · NO VERDICT 1.** G15-1:
the configuration itself is confirmed on the gate's
own machinery (W-A/W-B1/W-B2 — no phase code; the
deciding reads packaged as a Kaggle kernel under the
2026-11-23 standing order and re-judged fresh at home
from the harvested outputs; kernel checker 38/42 PASS,
the 4 failures being deciding reads dispositioned on
the record in `GATE15.md` §§4–5, not machinery faults).
The claim as written (ledger entry 261) does NOT
survive verbatim: its homogeneous-dimension clause is
wrong (settled counts ℓ=0: 7, ℓ=1: 10 — four of them a
verified pure-gauge family, (e) quotient 6 — ℓ=2: 8,
ℓ=3: 8); its [R̃]₂ coefficient is wrong (corrected
−1.213920×10⁻⁴ → −2.260117×10⁻⁴) and its [B]₂ tail
coefficient is wrong (corrected −1.268835×10⁻⁵ →
−5.210158×10⁻⁴); and its uniform amplitude bound is
not reproduced in the settled basis normalisation.
One genuine qualification rides on the restated
wording's face: restricted to the (e)-quotient
representatives alone, closure holds on residuals but
FAILS the amplitude bar at ℓ=1 (representative
amplitudes reach 6.949×10³ against the 10² bar) — the
small-amplitude closing representative uses the full
solution space, gauge directions included (verified
pure gauge; physically inert; the failure is priced
exactly as a basis-conditioning property in
`GATE15.md` §4). Novelty: PARTIALLY KNOWN for the
claim (W-D audit; the exact pose was not found in the
search, and every ingredient is published — limits
stated below).

The claim below is stated ONLY in Gate-15's restated
wording (§1 of `GATE15.md`), quoted verbatim.

**REVISION (2026-11-24, pre-publication).** After this
bundle was packaged, Phase 230's exoticity audit
(item (a) of `phase230/results/p2301_memo.md` in the
programme tree; checker 13/13 PASS) restated the
framing of the claim's shell-legality sentence: the
shell read Gate-15 carries is the surface density
Ŝ⁰⁰ only — the BDE junction formalism for pure Weyl
gravity fixes Ŝ⁰⁰ only, and the shells' tangential
energy conditions are undetermined by the posed
theory. The verbatim Gate-15 quote below is
unchanged; the Phase 230 restatement block printed
immediately after the claim, and the shell-legality
fence bullet in the fences list, govern how the
sentence "The joining shells are legal at BOTH
mouths" may be read. Full revision record:
`REVISION_2026-11-24.md` in this bundle. Nothing in
this release was ever uploaded in its earlier form.

---

## G15-1 — SURVIVES IN RESTATED WORDING

**MILESTONE (scan signal under attack; Gate-15: SURVIVES IN RESTATED WORDING): the two-mouth RE-MATCH CLOSES in the full linearised Bach system — a posed two-mouth configuration exists** (Phase 122, as corrected by Gate-15): the complete condition set ([B], [K], [R̃], [R̃_,n] + the angular Darmois pair per mode, round Σ, modes ℓ ≤ 3, ε ∈ {0.1, 1/30, 0.01, 0.003, 0.001}) is satisfied in the full homogeneous solution space — settled dimensions ℓ=0: 7, ℓ=1: 10 (four of them a verified pure-gauge family; (e) quotient 6), ℓ=2: 8, ℓ=3: 8 (all (e); response rank 6, full, at every mode) — with residuals ≤ 1.2×10⁻¹⁷ per unit ε^entering (bar 10⁻⁵) and amplitudes ≤ 2.2×10⁻² (bar 10²; worst mode ℓ=3). Restricted to the (e)-quotient representatives alone, the residuals still close (≤ 5.7×10⁻¹³) but at ℓ=1 the representative amplitudes reach 6.949×10³, above the 10² bar: the small-amplitude closing representative uses the full space, gauge directions included (physically inert; the quotient basis's smallest response singular value is 8.48×10⁻⁷ against the full set's 5.04×10⁻⁴). The joining shells are legal at BOTH mouths (shell sign minimum Ŝ⁰⁰/α₀ = +0.0202914453 at both; +0.0202882 after the corrected ℓ≥4 tail bound 2.459×10⁻⁶, ε = 0.1 row). The blindness sub-question is decided, not by identity: [R̃]₁ enters at ε² with +1.552938×10⁻³, [R̃]₂ at ε³ with −2.260117×10⁻⁴ (Gate-15 value, correcting the phase's −1.213920×10⁻⁴) — the (t,r)-sector identity does not extend to the full system. Scope fences: linearised pose (channels above ε⁴ and O(ε²) nonlinear terms unposed); formation PRE-EXISTING ONLY; (V-b) UNDECIDED: Pais–Uhlenbeck spin-2 ghost vs Mannheim PT-symmetric quantisation — opposed literature positions, B3 NOT COMPUTABLE (Phase 32).

### Phase 230 restatement of the shell-legality sentence (2026-11-24)

Phase 230's exoticity audit (item (a)) found the
claim's shell legality **WAS LEGAL ONLY BY
ACCOUNTING**: Gate-15's shell read is the single
number min Ŝ⁰⁰/α₀ = +0.0202914453 (post-tail
+0.0202881661 at ε = 0.1). Ŝ⁰⁰ = −(4α₀/3)[R̃_,n] is a
conformal-junction quantity; the BDE junction
formalism for pure Weyl gravity fixes Ŝ⁰⁰ **only**.
The shell's tangential surface stress Ŝ₂² is not
determined by the theory, by the junction
conditions, or by anything in the posed
configuration — the programme's own record says so
three times (Phase 86: "NOT SCORED (BDE fixes Ŝ⁰⁰
only)"; Phase 88: Ŝ₂² supplied only as an explicitly
labelled, UNFITTED datum family; Phase 90: the full
surface EC set scored only as a function of that
family). With u := Ŝ₂²/Ŝ⁰⁰, in α₀ units at either
mouth: NEC_t/α₀ = (1 + u)(0.0202914453),
DEC_t/α₀ = (1 − |u|)(0.0202914453). As posed, u is
unconstrained, so both tangential clauses are
**unbounded below** — an unposed component, not a
stored negative number. On the only tangential
datum family on record (Phase 88/90, Poisson–Visser
barotropic, unfitted), the full surface EC set
holds exactly for u ∈ [−1/2, 1]. The bulk check is
clean: the interior read already counts the full
gravity sector (in conformal gravity the Bach tensor
is the whole gravity operator) and the exterior is
Bach-flat.

**Restatement (Phase 230, verbatim):** The two-mouth
configuration restates as: posed closure in the
linearised Bach system (Gate-15, unchanged) with
joining shells of legal surface density
Ŝ⁰⁰/α₀ ≥ +0.0202881661 (post-tail, ε = 0.1) at both
mouths, whose tangential energy conditions are
**undetermined by the posed theory** — closable only
by adjoining a shell matter datum (on record: the
Phase 88/90 family, window u ∈ [−1/2, 1]). "Shells
legal" without that qualification does not survive
the strict audit.

**Fences and standing qualifications, inseparable
from the claim** (Gate-15 §§6–9; the first three are
also carried inside the wording itself):

- Shell legality is a Ŝ⁰⁰ statement only (Phase 230,
  2026-11-24): the joining shells' surface density
  Ŝ⁰⁰/α₀ ≥ +0.0202881661 (post-tail, ε = 0.1) at both
  mouths is legal; their tangential energy conditions
  (NEC_t, DEC_t) are undetermined by the posed theory
  — the BDE formalism fixes Ŝ⁰⁰ only — and close only
  under an adjoined shell matter datum (on record:
  the Phase 88/90 family, window u ∈ [−1/2, 1]).
  "Shells legal" without that qualification does not
  survive the strict audit.
- Linearised pose only: channels above ε⁴ and
  O(ε²) nonlinear terms are unposed. The claim is a
  linearised claim and is not priced at second order.
- Formation PRE-EXISTING ONLY.
- (V-b) UNDECIDED, verbatim: "Pais–Uhlenbeck spin-2
  ghost vs Mannheim PT-symmetric quantisation —
  opposed literature positions, B3 NOT COMPUTABLE
  (Phase 32)."
- Chronology protection is POSTURE ONLY: no deciding
  term exists inside the configuration, and no
  wording implies formation, superluminal travel, or
  a decided chronology statement.
- Second order: the second-order price (κ⁽²⁾ = 0
  only via amplitudes ~2714 per unit ε², far above
  the 10² bar; shell sign at second order surviving
  only at D/r_Σ = 100) rides with the claim wherever
  it is stated beyond linearised scope. The one
  second-order form this gate carries is the ℓ=0
  statement of Phase 141 (`sources/p1413_memo.md`
  §5): at ε = 0.01 the second-order shell sign at
  both mouths is Ŝ⁰⁰/α₀ = +0.00402664 > 0, with the
  perturbativity bar met in its excursion form. The
  second-order standing beyond ℓ=0 is NOT
  gate-judged — its deciding term rides the
  unharvested p1414 kernel — and no wording may
  present it as gate-judged.
- Novelty PARTIALLY KNOWN, with its search limits:
  web-index search only — INSPIRE-HEP and Semantic
  Scholar reached via web indexes, not direct
  sessions; no exhaustive arXiv listing-API sweep;
  forward citations of BDE and of Bochicchio–Laserra
  not systematically enumerated (a later paper
  applying BDE to a two-centre problem is the most
  plausible miss); English-language only; searches
  run 2026-11-23. No wording may call the claim
  unique/first/record; the publishable form is "not
  found in our search (limits: as above)."
- Gate-9 anchor flag: the shell value
  +0.0204228620559 recorded by this gate's own W-A —
  and inherited in Gate-9's W-B record — was the
  gate's machinery error (a spurious 4Φ₁Φ₂A₀ term in
  a printed A‴ jet for exp(2Φ₂)); it must not be
  reused as an anchor. The corrected control is
  Ŝ⁰⁰/α₀ = +0.0202914453, reproducing the
  phase-stored value digit-for-digit. Gate-9's
  verdict is not re-litigated — the offset did not
  move it.

---

## G15-2 — NO VERDICT (pending; not a claim of this release)

Phase 122's measured-shortcut claim (ledger entry
262) stays GATE-QUEUED / under attack. Its deciding
kernel (`g15-wc`) failed at its Stage-0 control gate
(a quadrature singularity in the L₁ integrand;
diagnosis and repair record in
`results/wc_kernel_repair_2026-11-23.md` and in
`STATUS.md`); no transit number was re-verified, and
no G15-2 verdict exists. Two fences stand in the
meantime (`GATE15.md` §8): any future G15-2 wording
must inherit G15-1's RESTATED form, not ledger 262's
original; and Phase 141's §5 effective transit gains
(G_τ = 23.00840 [23.00838, 23.00844]; G_t = 17.31288
[17.31288, 17.31290]) are Phase 141's second-order
ℓ=0-sector numbers — they are NOT a G15-2 verdict
and must not be cited as one.
