# CHECKPOINT 430 — SUPPLIER PERSISTENCE (instrument B-2 built)

Charged at ledger entry 1133 (Phase 428's §2 separable item,
entry 1132). Registration written before computation:
`phase430/work/p430_registration.md` (SS0–SS6, Amendments
1–3 appended on the record — §5 below). Frame of record:
VM, programme venv (numpy 2.5.5 / scipy 1.18.1) + Phase 166
pin. Driver `phase430/work/p430_run.py`; independent checker
`phase430/work/p430_check.py` (opposite path) → ALL PASS,
14/14; coordinator's restatement read
`phase430/work/p430_frobenius_addendum.py` → `results/
p430_frobenius_addendum.json`. Admission:
`results/p430_admission.json` — laptop ADMITTED (diff
4.18×10⁻¹⁸ ≤ 1×10⁻¹³ bar); deciding reads are the VM's.

## VERDICT: BOTH SUPPLIES DRIFT

**Instrument B-2 (the T_sup(t) read) is BUILT** — the stored
superpositions' time-dependent stress is now readable, by two
independent paths that agree at roundoff. Read under it, at
test-field scope, **neither stored supply persists**: Phase
410's Fit A and Phase 420's composite C-A are both classified
**DRIFTING**. The mating residual R(t) (the record's R: max
per-site Frobenius norm, 428's functional) crosses the 1×10⁻⁹
bar at

- Fit A: **t\* = 7.261×10⁻⁹ code units = 2.422×10⁻¹⁷ s**
- C-A: **t\* = 7.267×10⁻⁹ code units = 2.424×10⁻¹⁷ s**

— at ~2×10⁻²⁵ of Phase 425's window (W = 3.6518×10¹⁶ code
units). The B-2 supply certificate that 428's Route A
requires is therefore **not issuable for either stored fit**.
This is a verdict on these two superpositions under free-Dirac
evolution, not on supply in general (§6).

## The instrument (SS1)

Each stored mode is a positive-energy free-Dirac plane wave
with on-shell E_k = sqrt(|p_k|² + m_k²) — the machinery's own
dispersion (stored Dirac residuals ~1e-17). B-2 evolves the
mode phase exp(i p·x) → exp(i p·x − i E_k t) and reads
T_sup(t) at the mating sites two ways: PAIRWISE
(T_from_S with time-phased coefficients; S_of / S_of_multi)
and DIRECT (stress_at_point / _multi with time-phased modes).
The background enters only through the sites/targets, as in
every supply read in the record (Gates 54/55 scope).

## Controls (SS3 — all PASS, all before any t > 0 read)

- CTL-430-0 (t = 0 reproduction): Fit A maxR diff 3.48×10⁻¹⁸
  (pairwise) / 0.0 (direct); σ_min 0.38576181596969916 vs
  stored 0.3857618146636974 (rel 3.39×10⁻⁹, per-solution
  G36-C); per-site σ rel diffs ≤ 9.17×10⁻¹¹. C-A: maxR diffs
  0.0 / 0.0 (against T_corr — the reproduction is the proof
  the corrected targets are the right ones); σ_min
  30.12132520557749 at rel diff 0.0; per-site at 0.0.
- CTL-430-1 (single mode, closed form): T(t) = T(0) to
  3.74×10⁻¹⁶ over 17 instants; evolved Dirac residual
  6.94×10⁻¹⁸.
- CTL-430-2 (two-mode beat, closed form): return at
  2π/ΔE to 1.22×10⁻¹⁵; anti-phase tensor to 2.04×10⁻¹⁶.
- CTL-430-3 (direct vs pairwise in t, 40 draws/object):
  max component diffs 9.99×10⁻¹⁶ (Fit A) / 5.41×10⁻¹⁶
  (C-A), ≤ 8.9×10⁻¹⁵ of scale.
- CTL-430-4 (admission): ADMITTED, above.

## The read (SS4, deciding normalisation per Amendment 3)

**Fit A** — T_char = 24.773803197248984 (slowest material
pair modes 2↔6, ΔE = 0.2536221530926388; fastest period
1.887223263528613); grid [0, T_char] × 2048.
R(0) = 2.965984413711632×10⁻¹². Max R over the grid
**0.5279163900361216** at t = 6.8137035662194325 (site
A2_sec_argmin). R(T_char/4) = 0.339247978638945,
R(T_char/2) = 0.23049949373528442, R(T_char) =
0.32632911020835537 — no return within bar: DRIFTING.
Crossing t\* = 7.261×10⁻⁹ code units [bracket 7.258×10⁻⁹,
7.264×10⁻⁹] = 2.422008204×10⁻¹⁷ s, verified on the DIRECT
path (9.989459337007198×10⁻¹⁰ < 1×10⁻⁹ ≤
1.0009458421139267×10⁻⁹).

**C-A** — T_char = 651.3114481849092 (slowest material pair
modes 6↔7, family-1 mode 6 vs family 2, ΔE =
9.64697507573331×10⁻³; fastest period 1.881676524765556);
grid [0, T_char] × 32768. R(0) =
3.49600985773513×10⁻¹⁰. Max R over the grid
**0.5843616404573604** at t = 290.9603252824702 (site
A1_joint_argmin). R(T_char/4) = 0.43624118625007147,
R(T_char/2) = 0.24105816370895464, R(T_char) =
0.1730122438191481 — no return within bar: DRIFTING.
Crossing t\* = 7.267×10⁻⁹ code units [7.264×10⁻⁹,
7.270×10⁻⁹] = 2.424009588×10⁻¹⁷ s, DIRECT-verified
(9.99404752492033×10⁻¹⁰ < 1×10⁻⁹ ≤
1.0014055131094656×10⁻⁹).

**Anatomy.** The drift is not a slow leak; it is the
cancellation failing. At the sites, the supplied tensor is
a residue of pair cross-terms up to **~4.1×10² × the
target's own Frobenius norm** (largest pair weights 406.1 /
405.8 / 336.7 for Fit A; 408.5 / 405.4 / 336.9 for C-A).
Per-site ‖dT/dt‖_F at t = 0 is 0.1377 / 0.0634 / 0.1024
(Fit A) and 0.1377 / 0.0621 / 0.1018 (C-A) per code unit —
the residual, starting near-orthogonal to its derivative,
grows on the ‖ṙ‖·t law and reaches O(0.5) absolute within a
fraction of the fastest beat period. The supplementary
component-normalised read (registration SS1's definition;
Amendment 3) agrees in kind: Fit A R_comp(0) =
6.688×10⁻¹⁰, max 2110.31 at t = 14.208326797054376 carried
by T00 at A1, crossing at 3.0155748816865357×10⁻¹² code
units (checker DIRECT bisection 3.0163665978789995×10⁻¹²,
rel diff 2.6×10⁻⁴); fastest-growing component T33 at A1,
|d resid/dt| = 336.44 per code unit (C-A: 337.67).

## Amendments (on the face)

- **A1 (SS2, filed before the read):** the strict t = 0
  weight rule also flags C-A's 15 family-2-internal pairs
  (weights 5.8×10⁻⁴…9.8×10⁻³ ≥ 1×10⁻⁶), whose slowest
  ΔE = 3.616×10⁻⁸ would set T_char = 1.7376729689029083×10⁸.
  Per the registration's own SS2 text these are
  stored-rounding residue on near-degenerate modes
  (pairwise ΔE ≤ 5.19×10⁻⁷; rotation over the registered
  grid ≤ 3.379×10⁻⁴ rad); the registered T_char was used.
- **A2 (SS4, driver's, filed before its grid read):** under
  SS1's component normalisation, C-A's R(0) =
  5.639×10⁻⁸ is already above the bar at t = 0. Recorded;
  superseded as the deciding read by A3.
- **A3 (coordinator's, after the run):** SS1's R
  normalisation (max component / FROB_site) deviates from
  the record's R. Phase 428's functional and the stored
  maxR of 410/420 are the max per-site Frobenius norm
  (428 §2: "residuals ≤ 3.496×10⁻¹⁰ vs the 1×10⁻⁹ bar" is
  C-A's stored Frobenius maxR). The deciding read is
  restated in the record's normalisation
  (`p430_frobenius_addendum.py`); its t = 0 values
  reproduce the stored maxR at diffs 3.48×10⁻¹⁸ / 0.0
  (Fit A) and 0.0 / 0.0 (C-A). Classifications unchanged:
  DRIFTING under both normalisations, for both objects.
- One driver bug was caught and fixed during the run (grid
  argmax bookkeeping for the drift-carrying site/component;
  corrected record independently spot-verified). No
  headline R, t\*, or classification value changed.

## What this does to 428's functional

Route A's supply leg requires a B-2 certificate (T_sup(t)
stationary within the bar, or Form P's periodic form).
Neither stored superposition can carry one: both leave the
bar ~10⁻¹⁷ s into a 3.860 yr window. GAP-2's status is
unchanged (its gate remains GAP-3's four-condition
geometry), but the supply half of any future sustainment
registration against these fits is now known to fail at its
first clause, on measurement rather than on absence of
measurement. **Named follow-up (not charged):** a
degenerate-spectrum mating — all modes at a single energy,
stationary under B-2 by construction (CTL-430-1/2 are its
limiting cases) — would pass the supply leg by design;
whether the sites' targets admit such a fit is unposed.

## Fences

Test-field scope on every quotation (no backreaction, no
self-consistency). Persistence of the SUPPLY is not
persistence of the GEOMETRY and not sustainment — 428's
functional governs any such claim. The 405 background's
SEC failure (−2.213557×10⁻⁴) is printed here and is
untouched; both fits mate a background that itself fails
SEC, and nothing in this phase changes that.

## THREE GOALS

(1) FTL drive/mechanism: NO — no sustainment content;
B-2 built, and the two standing supplies measured
non-persistent; Frontier A unchanged. (2) Functional
wormhole: untouched. (3) Best subluminal record:
untouched (Procaccia β = 0.1363 stands in its category).
DESK: NO DATA CONTACT.

## FILES

- `work/p430_registration.md` — registration (SS0–SS6).
- `work/p430_run.py` — driver (component-normalised read).
- `work/p430_frobenius_addendum.py` — Amendment 3 read
  (deciding normalisation).
- `work/p430_check.py` — independent checker (opposite
  path).
- `work/p430_admission.py` — admission helper.
- `results/p430_results.json` — driver results +
  Amendments 1–2.
- `results/p430_frobenius_addendum.json` — deciding
  R_F read.
- `results/p430_check_results.json` — checker, ALL PASS.
- `results/p430_admission.json` — admission record.
- `results/p430_memo.md` — the full memo.
