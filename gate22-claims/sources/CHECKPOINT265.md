# CHECKPOINT 265 — P265-1: THE B-SENSITIVITY READ:
# THE CERTIFIED BRACKET'S DEPENDENCE ON THE STOP
# B := 2.5, PRICED END TO END — THE STOP RETIRES
# (READ GRADE)

Phase 265 (single item), warp pilot. Integrated record:
`phase265/results/p2651_memo.md`. Registration
(pre-run): `phase265/work/p265_registration.md`.
Driver: `phase265/work/p2651_run.py`; results:
`phase265/results/p2651_results.json`; checker:
`phase265/work/p2651_check.py` →
`phase265/results/p2651_verify.json` (8/8 PASS). Frame
of record: Phase 166 pin, Gate-19-corrected tensor,
venv python, float64. INTERNAL only. No ledger append,
no launches, no external contact; protected files
byte-identical before/after (15 files; memo §7/C8).

## VERDICT

**FORM 1 — THE STOP RETIRES.** Marched under the
generalised clamp a_B(t) = max(−0.5 − c_trim·t², −B)
(c_trim = +5.253378225339471, stored, not re-fit), the
combined-class datum's first-crossing bracket moves
monotonically with B and **saturates**: B = 1.5 →
(0.59375, 0.6]; B = 2.0 → (0.63125, 0.6375]; B = 2.5 →
(0.65625, 0.6625] (control, diff 0.0 vs Phase 252);
**B = 3.0 and B = 3.5 coincide exactly at
(0.675, 0.68125]** with hi carriers exactly
{NEC_φ, DEC_φ} at both, all §4 admissibility gates
passing at both arms — and t_clamp(3.0) =
0.6898436476740386 ≥ 0.68125, so at B = 3.0 the clamp
never binds before the crossing: the coincident
bracket is the **unclamped trim law's own crossing**,
the stop-free bracket at read grade. Gate-26's priced
gap — "no sensitivity of the bracket to the stop's
value is on record" — is closed at read grade: the
sensitivity is tabled in full (bracket midpoints
0.596875 → 0.634375 → 0.659375 → 0.678125 → 0.678125;
interval rates 0.075, 0.050, 0.0375, 0.0 per unit B),
and it vanishes exactly where form 1 requires.

## FTL VERDICT (leading): NO

No grouped joint pass anywhere; Frontier A unchanged;
drive step 1 remains unachieved. The phase's yield is
on the wormhole goal, and it is a record-completion
yield: the programme's longest-lived throat datum's
certified bracket is now known not to be an artefact
of the operational stop at which it was posed. The
unclamped law's own first crossing reads
(0.675, 0.68125] — 0.01875 past the certified bracket
in bracket position — as a READ; the certified
(0.65625, 0.6625] stands as the verdict-grade
statement, about the pose as clamped at B := 2.5,
exactly as Gate-26 restated it.

## WHAT RAN (decision order)

- **Controls first, all PASS** (memo §2): CTRL-1 =
  Phase 252's CTRL-A/B/C verbatim; CTRL-2 = the
  B = 2.5 arm reproduces Phase 252's stored re-posed
  record at max abs diff 0.0 on the 41 sampled
  instants' clause minima, end margins exact, stop
  instant within 1.40×10⁻⁸ of record.
- **One pair of march states** (main N_θ = 2881,
  h_t = 0.0025, 24.3 s; aux h_t = 0.00125, 33.8 s;
  both T_END = 1.0); all five arms read off them.
- **Per-B arms** (memo §§3–6): t_clamp(B) tabled
  (0.436295 / 0.534351 / 0.617015 / 0.689844 /
  0.755686); sampled scans; halving-ladder brackets
  with all-clause end margins and carriers; margins
  at the certified instants (at B = 3.0 both
  certified instants are back inside the living span:
  +0.317823 / +0.233984); the fixed-t sensitivity
  table (the margin's B-slope is the delivery
  sensitivity ≈ 1.0 per unit B where the clamp binds,
  exactly 0 where neither arm clamps, partial in the
  transition rows); the structural cross-check at
  diff 0.0 / 5.30×10⁻¹⁰.
- **§4 gates pass at every arm** (memo §6): delivery
  affine-exact at peak amplitude to a = −3.5 (max
  deviation 6.37×10⁻¹⁰ vs the 1×10⁻⁶ bar); PR-φ
  clean at peak amplitude and law-adapted at bracket
  ends. No arm refused.
- **Checker 8/8 PASS** (memo §7): every deciding
  number re-derived from fresh marches at diff 0.0
  where 0.0 was required, including the t = 0.7
  B = 3.0/B = 3.5 separation (0.07307305580435397)
  that proves the coincident arms are not trivially
  identical, and a mechanical re-application of the
  verdict forms from the stored results alone.
  Driver wall 111.3 s; checker 64.1 s; nothing
  packaged.

## NAMED SUCCESSOR

A certification registration in the Phase 243 pattern
for the **unclamped-law bracket (0.675, 0.68125]** —
per-instant Richardson limits on NEC_φ/DEC_φ over the
crossing neighbourhood, matched T_END = 1.0 — whose
registration carries no stop parameter (the pose is
the law a(t) = −0.5 − c_trim·t² itself, clamped
nowhere before its crossing), followed by a gate on
the amended claim set (the Gate-26 fence on G26-A —
"the trim law as clamped at B := 2.5" — is the
wording such a gate would re-examine). This phase
does not register it; the parent's act.

## FENCES

Form 1's fences stand: (i) READ grade — no bracket in
this phase is certified; Phase 256's certificate and
Gate-26's verdicts (G26-A restated, G26-B, G26-C)
stand untouched for the pose as posed at B := 2.5;
(ii) pose scope (Phase 169 A-branch datum, true lock;
κ = 0.3 director + C2 rotating headline + CH-PHI-Auu
under P-PHI-TRIM-248 with its fitted coefficient —
Gate-26 §4(3b) provenance carried); (iii) jet scope /
sector superposition (exhibit ≠ construction);
(iv) programme-level sustainment wording remains
gated by p1592 regardless. The stop's retirement is
a read-grade statement that the bracket is not an
artefact of the stop's choice; no B is promoted to a
physical boundary, and Phase 252's "no finite
boundary in [0, −2.5]" is neither extended as a claim
nor contradicted (§4 gate passes are this read's
admissibility evidence at the swept amplitudes).
Phase 243/248/252/256 verdicts stand for their own
poses and scopes.
