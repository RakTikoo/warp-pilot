# CHECKPOINT 243 — P243-1: CERTIFICATION OF THE (0.55625,
# 0.5625] BRACKET (FU-P234-1, SECOND REGISTRATION) —
# BRACKET CERTIFIED (FORM 1, DISPOSITION T-A)

Phase 243 (single item), warp pilot. Integrated record:
`phase243/results/p2431_memo.md`. Registration (pre-run,
Phase 240's design unchanged in substance + the §R repair):
`phase243/work/p2431_registration.md`. Driver:
`phase243/work/p2431_run.py`; results:
`phase243/results/p2431_results.json`; checker:
`phase243/work/p2431_check.py` →
`phase243/results/p2431_verify.json`. Frame of record:
Phase 166 pin, Gate-19-corrected tensor, venv python,
float64. INTERNAL only. No ledger append, no launches, no
external contact; protected files byte-identical
before/after (memo §7).

## VERDICT

**FORM 1 — BRACKET CERTIFIED, disposition T-A.** The
three-channel first crossing (0.55625, 0.5625] on
NEC_φ = DEC_φ stands as a verdict in the certified scope:
CERT-1…4 hold for the new bracket, and Phase 214's t*
bracket (0.5, 0.50625], re-read under the SAME certificate
on the director-only pose, certifies as posed — the
comparison is in one frame and the sustainment interval's
extension is a finding in the certified scope, fenced by
the tail limitation, pose scope, jet scope, and the p1592
gate on programme-level wording. **Named successor: a Gate
registration on the certified claim set** (the parent
amends Gate-22's claim set; this phase does not).

## THE REPAIR (registration §R — the only deviations from
## Phase 240)

Phase 240 stopped at CTRL-1 because its T_END = 0.65
marches met Phase 234's T_END = 1.0 stored rows at the one
instant (t = 0.65) where the pinned `mtt_field` stencil is
march-length-dependent (centred interior vs one-sided
final index; Phase 240 memo §8 anatomy). Repair: (a)
CTRL-1 restated at matched march length (T_END = 1.0);
(b) ALL window-read marches fixed at T_END = 1.0 for every
grid, so every window instant is an interior
(centred-stencil) read in every grid; (c) the §5(e) probe
arithmetic only — project the [0, 1.0] march (3200 steps)
as 20 × probe wall, 900 s threshold unchanged.

## WHAT RAN (decision order; run wall 772.5 s)

- **CTRL-2 PASS, bit-exact:** Stage A
  3.4339573895536546×10⁻⁷, Stage B
  3.4498744435396134×10⁻⁵, recomputed from Phase 234's
  stored rows = stored.
- **Tail pricing (stored rows) on the face:** first
  1×10⁻⁶ exceedance in Stage B at t = 0.775; max on
  (0.65, 1.0] = 3.4498744435396134×10⁻⁵ at t = 1.0, carrier
  DEC_θ, relative 3.3942464143610627×10⁻⁶; per-instant
  disagreement on (0.5, 0.65] ≤ 6.25625901307103×10⁻⁷.
  Fence (i) of the verdict: tail reads past the window are
  NOT certified; the stage-max gate still fails there.
- **CTRL-1 PASS, all diffs 0.0:** fresh G4/G3 three-channel
  sampled (≤ 0.65), G4 refined, G4 director sampled and
  refined (t = 0.50625) all reproduce the Phase 234 /
  Phase 214 stored rows exactly at T_END = 1.0.
- **G5 probe:** [0, 0.05] (160 steps) 21.2278 s → projected
  [0, 1.0] march 424.556 s ≤ 900 s; rule does not fire, G5
  run (actual march wall 466.65 s; state 590,033,928 B per
  field, ≈1.770 GB for MU + U + MTT). No kernel spec
  written (that obligation attaches to form 3 only).
- **CTRL-3 PASS:** G5 director vs Phase 210 stored G4 —
  1.4235054024425153×10⁻⁸ (t = 0.25),
  5.694021876223587×10⁻⁸ (t = 0.5), both ≤ 1×10⁻⁶.

## THE CERTIFICATE

**New bracket (three-channel), NEC_φ = DEC_φ:** CERT-1
TRUE (every window instant limit-certified; monotone
instants at p ≈ 2.0000, worst |d34| = 3.482×10⁻⁷ at
t = 0.65, worst residual r = 2.901×10⁻⁸); CERT-2 TRUE
(L(0.55625) = +0.0044681427164857323 ≥ 0,
L(0.5625) = −0.054339801013359036 < 0; v5 likewise);
CERT-3 TRUE; CERT-4 TRUE (non-clause bars at bracket
instants: momentum ≤ 4.441×10⁻¹⁶, flare ≥ 0.13926,
domain_R ≥ 0.65556).

**t* (director-only):** CERT-1…4 all TRUE
(L(0.5) = +0.0045418645951645232 ≥ 0,
L(0.50625) = −0.035378628675540646 < 0; bracket residuals
1.419×10⁻⁹ / 1.461×10⁻⁹). **Disposition T-A: t* certifies
as posed (0.5, 0.50625]**; the §5(c) restated-bracket
search was not needed.

**Checker: 17/17 PASS** — including fresh G4 and G5 spot
recomputation of the deciding instants for both poses at
diff 0.0 (marches at T_END = 1.0), Richardson arithmetic
and CERT booleans recomputed for both brackets, verdict
form consistent with §6, and live protected-file byte
identity. (The Phase 243 checker's CTRL-1 assertion checks
the recorded outcome's consistency with its recorded
diffs, per the registered decision order, instead of
Phase 240's assert-pass form that structurally failed a
legitimate control-failure file; memo §8.)

## FENCES

Form 1's four fences stand: (i) the tail limitation above;
(ii) pose scope (Phase 169 A-branch datum, true lock;
κ = 0.3 director P-DIR-T2 + CH-COMB flat +0.10
P-PROF-FROZEN + CH-PHI-Auu flat −0.5 P-PHI-FROZEN);
(iii) jet scope / sector superposition (exhibit ≠
construction); (iv) programme-level sustainment wording
remains gated by p1592 regardless. Phase
210/214/226/229/233 verdicts stand for their own poses and
scopes; Phase 240's control-stopped record stands as
written. One cosmetic note (memo, verdict section): the
driver's recorded verdict note retains Phase 240's prose
phrase "under the p2401 registration"; the registration of
record is `phase243/work/p2431_registration.md`, as the
results file's `registration` field states. No number is
affected.
