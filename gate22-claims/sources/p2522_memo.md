# P252-2 (Item 2) — THE RE-POSED MARCH: the composed
# combined-class datum with the κ-analogue trim law at the
# audited amplitude — memo

Worker W252-2, 2026-11-24. Registration (fixed, NOT edited):
`phase252/work/p252_registration.md` §3. Driver:
`phase252/work/p2522_run.py` (machinery via
`phase252/work/p2521_run.py` from Phase 248; nothing outside
`phase252/` edited); checker: `phase252/work/p2522_check.py`
(**ALL PASS, 37/37**, including fresh spot recomputation of
all three brackets' end instants at diff 0.0, pose-refusal
spot reads at diff 0.0, and live protected-file md5
identity); numbers: `phase252/results/p2522_results.json`,
`phase252/results/p2522_verify.json`. Frame of record:
Phase 166 pin, Gate-19-corrected tensor, venv python,
float64. Total stress = G/8π is the read itself. Datum ≠
construction; jet scope. INTERNAL only; no ledger append,
no launches, no user contact. Driver wall 17.6 s, checker
≈ 22 s — no run approached the 900 s rule; no kernel spec
owed.

**Amplitude rule (Item 1's outcome, governing):** Item 1
fired verdict form 3 — CAP PROTECTS NOTHING CURRENT (no
H-condition fails anywhere in a ∈ [0, −2.5] on this datum).
Per registration §3 the re-posed march therefore runs at
**B := 2.5 operational stop**: a(t) = −0.5 − c_trim·t² with
the STORED c_trim = +5.253378 (q₂ = −6.062835, s̄ =
1.154083 — not re-fit), clamped only at |a| = 2.5.

**Interpretation recorded on the face BEFORE the march
(driver header):** the law's peak amplitude over the full
march window [0, 1.0] is the stop itself, |a| = 2.5 (the
unclamped law would reach 5.75 at t = 1; the stop binds at
t_stop = √(2/c_trim) = 0.617015); over the deciding window
(the wound bracket's far end, 0.5625) the unclamped law
reads **−2.162202**, so the stop does not bind the
comparison against the wound pose, exactly as the
registration priced. Pose-refusal was therefore run both
law-adapted at every sampled instant and as a flat member
at the peak amplitude a = −2.5.

## Verdict (registration §3 form 1, verbatim in substance)

**COMBINED-CLASS DATUM TAKES THE LEAD** — the re-posed
first-crossing bracket is **(0.65625, 0.6625]**, carrier
**NEC_φ = DEC_φ**, bracket-end margins **+0.052799 /
−0.073695** — lying entirely past the wound pose's
certified bracket (0.55625, 0.5625], by ≥ 0.09375 in t at
the bracket level. This wording stays a **READ, not
CERTIFIED**: the named successor is a certification
registration in the Phase 243 pattern for this bracket.
At the wound bracket's far end itself (t = 0.5625, law
amplitude −2.162202, stop not yet binding) the re-posed
datum still holds all seven clauses with NEC_φ margin
**+1.126925** (checker-recomputed fresh).

## 1. Controls (run first; all PASS, diff 0.0)

- **CTRL-A (untrimmed, frozen a = −0.5):** refined bracket
  **(0.4875, 0.49375]**, carrier NEC_φ = DEC_φ, margins
  +0.008513 / −0.035909; anchors NEC_φ +0.093089 @ 0.475,
  NEC_ρ +1.295071 @ 0.475, first sampled fail t = 0.5 at
  −0.081831.
- **CTRL-B (trim clamped at 0.8):** refined bracket
  **(0.525, 0.53125]**, carrier NEC_φ = DEC_φ, margins
  +0.042998 / −0.012405; clamp instant **0.238969**;
  stored constants re-pinned (c_trim = +5.253378 from
  q₂ = −6.062835, s̄ = 1.154083).
- **CTRL-C (static pin):** S(θ*) = −4.0625, NEC_ρ min
  = −4.0625, identity deviation ≤ 8.9×10⁻¹⁶ class.

## 2. Pose-refusal (registration §3 / Phase 246 PR-φ,
## adapted to the law) — PASS everywhere; form 3 does not fire

- **Law-adapted, all 41 sampled instants** (a(t) with the
  2.5 stop): PR-φ-1 offset extraction exact at every
  instant; PR-φ-2 mom_φ residual ≤ 1.30×10⁻¹⁵ and
  mom_ρ/mom_θ maxima in the same class (bar 1e-9);
  momentum max over all channels ≤ 1.78×10⁻¹⁵; PR-φ-3
  liveness ≥ 1.5625 at every instant (bar 1e-3);
  non-clause bars pass at every instant (base-pose flare
  min > 0 throughout, domain R_min > 0, exp(2Φ)_min > 0).
- **Flat member at the peak amplitude a = −2.5**, at
  t ∈ {0, 0.25, 0.475, 0.5625} — the march-slice ground
  past t = 0.475 at high amplitude that Item 1's flat
  sweep (t ≤ 0.475) did not price: all checks pass at
  every instant; liveness 6.25 at every spot; mom_φ
  residual ≤ 3.9×10⁻¹⁶. No pose-level condition breaks;
  Item 1's audit is not shown incomplete in any respect
  this item tested.

## 3. The re-posed march

Sampled bracket (0.65, 0.675]; halving ladder (0.6625
fails, 0.65625 holds) → **refined bracket (0.65625,
0.6625]**, width 0.00625. At both ends the law is already
at the stop (a = −2.5; the stop binds from t = 0.617015,
*after* the wound comparison point 0.5625, where a =
−2.162202). Bracket-end margins: at 0.65625 the binding
margin is NEC_φ = DEC_φ = **+0.052799** (next clause
NEC_th/DEC_th +4.188188, NEC_ρ/DEC_ρ +5.146168); at
0.6625 NEC_φ = DEC_φ = **−0.073695**, every other clause
≥ +4.188199. **Carrier at both ends: NEC_φ = DEC_φ** —
the same μ-drift carrier as every prior bracket in this
line.

**Binder / argmin watch (the new-ground checks of task
(b)):** at every sampled instant the worst clause is
NEC_φ, and the NEC_φ argmin sits at index 90 (θ*)
throughout — **no argmin migration, and no clause other
than NEC_φ = DEC_φ ever becomes the binder**, including
in the high-amplitude slices past t = 0.475. (The
composed NEC_ρ argmin sits at index 128 at the bracket
ends, but NEC_ρ's margin there is +5.1 — it is not a
binder and never approaches one.)

**Carrier margin trajectory** (NEC_φ grid min, sampled;
full table in the results JSON): +1.218750 (0) rising
under the growing trim to a peak **+1.464349 at t = 0.4**,
then declining as the headline drift outgrows the trim's
effective sensitivity: +1.407584 (0.475) → +1.187607
(0.55) → +1.126925 (0.5625, checker spot) → +0.888262
(0.6) → +0.618093 (0.625, stop now binding) → +0.174521
(0.65) → **+0.052799 (0.65625)** → **−0.073695 (0.6625)**
→ −0.341991 (0.675), steepening thereafter (−37.77 at
1.0). No sampled instant after the crossing recovers.

**Decomposition at the bracket** (headline + lift =
composed, exact): at 0.65625, headline NEC_φ =
−2.471798, lift +2.524597, composed +0.052799; at
0.6625, headline −2.589541, lift +2.515846, composed
−0.073695. Between the bracket ends the headline drift
falls by 0.117743 while the lift (now flat, the stop
binding) erodes by only 0.008751: **the crossing is
carried by the headline μ-drift against a saturated
lift** — the same anatomy as Phase 248's clamped arm,
one stop-level later.

**a\* comparison (descriptive, Phase 248 B5 method):**
the flat amplitude whose constant lift would repay the
headline deficit at the bracket's hi end (D = 2.589541
over s̄ = 1.154083) is **a_equiv = −2.743808** — beyond
even the 2.5 stop. The law nevertheless crosses at
0.6625 because its lift was banked earlier along the
trajectory (the t² trim held NEC_φ at +1.46 near t = 0.4
while a flat channel spends its lift uniformly); stated
descriptively only, not as a read. Against Phase 248's
priced a* = −1.517513 (the flat price of reaching
0.5625): the law's amplitude at 0.5625 is −2.162202, and
at that instant the datum holds with +1.126925 to spare.

## 4. Three-bracket table

| datum | first-crossing bracket | carrier |
|---|---|---|
| Untrimmed composed (CTRL-A) | (0.4875, 0.49375] | NEC_φ = DEC_φ |
| Trimmed, clamped at 0.8 (CTRL-B) | (0.525, 0.53125] | NEC_φ = DEC_φ |
| Wound pose, certified (Phase 243) | (0.55625, 0.5625] | NEC_φ = DEC_φ |
| **Re-posed, B = 2.5 stop (this item)** | **(0.65625, 0.6625]** | NEC_φ = DEC_φ |

## 5. Scope fences

Jet scope; sampled/refined-instant reads; datum ≠
construction; sector superposition (Phase 234 §6). No
certificate is claimed for this bracket — Phase
243/Gate-23 cover the wound pose only; form 1's named
successor is a Phase 243-pattern certification
registration for the (0.65625, 0.6625] bracket. The trim
law is open-loop and fixed in advance — ≠ the closed-loop
stabilisability proof (Phase 208) and ≠ Phase 217 V2.
Retiring the 0.8 cap here is Item 1's finding about THIS
datum's lifetime question; the cap's standing in the
wound line's registrations (Phases 234/243) is untouched.
Amplitudes beyond |a| = 2.5 remain unaudited (Item 1 §6):
the stop is an operational limit of this march, not a
priced boundary.

## Files

- `phase252/work/p2522_run.py` — driver (controls,
  pose-refusal, re-posed march, ladder, decomposition,
  verdict; 17.6 s).
- `phase252/work/p2522_check.py` — independent checker,
  ALL PASS (37/37): fresh marches, all three brackets'
  end margins at diff 0.0, pose-refusal spot reads at
  diff 0.0, law arithmetic, verdict consistency,
  protected md5 live.
- `phase252/results/p2522_results.json` — full reads
  (controls, pose-refusal records, 41 sampled instants
  with full clause profiles, ladder, decomposition,
  carrier trajectory, a* comparison).
- `phase252/results/p2522_verify.json` — checker record.
- `phase252/results/p2522_memo.md` — this memo.
