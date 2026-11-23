# P50-2 — OUR LADDER, SETTLED AND EXTENDED — worker memo

**HEADLINE (locked language): the halved-smoothing row at β = 0.09 and
β = 0.10 reported below is a "scan signal under attack"** — it has
passed this phase's full bars including the second path (see §4 for
the one coarse-grid disagreement and its resolution), and it stays
in locked language until a future gate verifies it. No verified row
above β = 0.136 exists; nothing here is a discovery.

Run 2026-11-22, per CHECKPOINT50 §P50-2 as registered. Python:
**system python3** (numpy 2.2.6 / scipy 1.14.1), float64 everywhere.
Code: `phase50/p502_lib.py`, `p502_main.py`, `p502_refine.py`,
`p502_diag.py`, `p502_follow.py`, `p502_verify10.py`,
`p502_verify10b.py`, `p502_check.py` (checker over the result
JSONs; every verdict below is recomputed from stored numbers by
`p502_check.py`). Result JSONs: `results/p502_main.json`,
`p502_diag.json`, `p502_refine_b0.11.json`, `p502_follow.json`,
`p502_verify10.json`, `p502_verify10b.json`. Every verdict number
comes from the gate-standard auditor (`gate6/wa_auditor.py`,
2nd-order direct-∂² FD, algebraic ∂Γ); the second path is the
4th-order direct-∂² variant of the `wa_diag.py` pattern (copied
into `p502_lib.py`; `wa_diag.py` itself executes at import and was
not imported). `verify_metric.py` was not used anywhere.

## Plain language first

Three things were settled. **First**, the stored champion shell —
the one Gate-6 cleared at β = 0.07 and 0.08 — really does stop at
0.08. At β = 0.09 it fails, but not the way Phase 26 said and not
at the point Phase 26 blamed: the eigenvalue margins at the inner
edge are actually positive and stay positive as the grid is
refined (continuum value +5.73e-06). What breaks is the *type* of
the stress tensor at the inner edge: at 14 points at radii 10.25
and 10.75 the tensor stops being Hawking–Ellis Type-I, and a
direct null-direction test there finds a genuine NEC violation of
−6.71e-06. That failure is real, grid-stable, and confirmed by the
independent 4th-order discretisation. **Second**, β = 0.10 fails
the same way, only bigger — the bad patch grows from 14 points to
50 and reaches out to r = 12.25. Phase 26's "mid-shell SEC failure
at r = 18.8" does **not** reproduce on this configuration under the
gate-standard auditor (that number belonged to a different mass
row in the Phase-26 search); on the stored configuration the
binding failure is the inner-edge Type-I/NEC breakdown, named from
my own read as registered. **Third**, the family is not dead at
0.08: halving the Gaussian smoothing widths — (s_ρ, s_P) = (2.0,
1.16) instead of (4.0, 2.32), everything else about the champion
unchanged — produces a fully legal row at β = 0.09 **and**
β = 0.10, confirmed by the second path. At β = 0.11 that row fails
again at the inner edge, and a 246-configuration refinement search
over the whole registered envelope finds nothing legal there. So
the family's true ceiling is **β\* = 0.10**, and the wall at 0.11
is the same inner-edge mechanism that killed the stored row at
0.09 — smoothing width buys two rungs, then the same wall returns.

## 1. Anchors (step 1 — all pass; machinery validated before any verdict)

- Minkowski: max|G| = 0.0 exactly.
- Static β = 0 vs `shell.py` exact 1-D T: ρ relative error
  3.07e-03 at h = 0.3, 7.61e-04 at h = 0.15 (clean h² scaling);
  principal-pressure max abs error 9.2e-08. These reproduce
  Gate-6's own recorded anchor values (≤3.1e-03 / ≤7.6e-04 /
  9.2e-08) digit for digit — the auditor setup is Gate-6's.
- Finalist A (M = 2.0, (10,20), β = 0.02, fine set, h = 0.3):
  whole-volume worst **+2.141e-07**, Type-I fraction **1.000**
  (Gate-6: +2.14e-07, 1.000).

## 2. β = 0.09 settled (step 2) — stored configuration FAILS, new anatomy

Full fine audit (1,404 pts), stored configuration
((10,30), M = 8.0, edge-peaked wd=6.0/floor=0.2, (4.0, 2.32), cos):

| | h = 0.3 | h = 0.15 |
|---|---|---|
| Whole-volume worst (eigenvalue, Type-I subset) | +2.580e-07 (SEC, r = 37 tail) | +2.590e-07 |
| Core worst (eigenvalue) | +5.841e-06 (NEC, r = 10.75) | +5.758e-06 |
| **Type-I fraction** | **0.990** | **0.990** |
| **Core sampled-null NEC min** | **−6.710e-06** | **−6.708e-06** |
| FD floor | 1.6e-08 | 2.3e-08 |

Inner-edge h-ladder (radii 9.75–11.50, 26 dirs): eigenvalue NEC
minimum +5.841e-06 / +5.758e-06 / +5.738e-06 / +5.732e-06 at
h = 0.3/0.15/0.075/0.0375, Richardson continuum **+5.730e-06** at
r = 10.75 — the Phase-26 failure value (−1.10e-06 at r = 10.25)
does **not** exist in the eigenvalue read; that part of the
Phase-26 verdict was indeed the impeached artefact. But the
sampled-null NEC over the same ladder region is **−6.71e-06 at
every h**, and the point diagnosis (`p502_diag.json`) shows why:
exactly **14 significant points, at r = 10.25 and r = 10.75, are
non-Type-I, and the same 14 points are exactly the
sampled-NEC-negative points** (overlap 14/14 at both h). A sampled
null contraction T_ab k^a k^b < 0 is a direct NEC violation for
any Hawking–Ellis type, so this is a genuine failure, not a
labelling artefact. Second path (4th-order, fine set): Type-I
0.988/0.990 at h = 0.3/0.15 — agrees. **Verdict: β = 0.09 FAILS
bars 1 and 3 on the stored configuration. Binding site: inner
edge, r = 10.25–10.75. Binding condition: NEC (via Type-I
breakdown).** The Gate-6 follow-up is discharged: 0.09 is settled,
against the stored row.

## 3. β = 0.10 re-confirmed (step 3) — fails; binding read is mine

Same configuration, fine audit: Type-I **0.964** (both h), core
sampled-null NEC min **−1.648e-05** at r = 10.25 (both h),
eigenvalue core worst still positive (+1.05e-05). Diagnosis: 50
non-Type-I significant points spanning r = 10.25–12.25, 49 of them
sampled-negative. Second path: Type-I 0.962/0.963 — agrees.
**Binding site/EC from my read: inner edge (r = 10.25, patch
extending to 12.25), NEC/Type-I — NOT the mid-shell SEC site
Phase 26 reported** (its −2.99e-05 @ r = 18.8 was the M = 9.5
search row's dense read, not this configuration's). The failure
itself is h-stable and real; only its address changes.

## 4. The climb (step 4) — stored rows, refinement, and the 0.10 row

Stored configuration at 0.11–0.14 (step i, fine audits): all fail
the same way — Type-I 0.927 / 0.890 / 0.845 / 0.777, core sampled
NEC −2.64e-05 / −3.66e-05 / −4.68e-05 / −5.73e-05, worst point
always r = 10.25.

Refinement at β = 0.11 (step ii; the first rung is tested first,
per the registered stop rule): **246 screened rows** (4 geometries
× 6 compactnesses {0.30…1.05} × the Phase-26 ha2 design set —
edge-peaked ×2, matched, smoothbox × cos/cos-extended/quintic
windows — plus smoothing scales {0.5, 1.5} on the canonical
design; 42 build failures, all compactness/geometry combinations
`build_shell` rejects or non-finite profiles, logged in the JSON),
reduced point set, h = 0.3, ranked by min(eigenvalue worst,
sampled-null min) so non-Type-I rows cannot hide. **No legal
row.** Best row: the canonical (10,30) M = 8.0 design with
**smoothing halved** (scale 0.5: (2.0, 1.16)), screen score
−3.36e-06. Its full fine audit: DEC **−2.53e-06** (h = 0.3) /
**−5.76e-06** (h = 0.15) at r = 10.25, Type-I 0.990, sampled
−3.19e-06/−3.32e-06; second path agrees (worst −5.5e-07/−7.5e-06,
Type-I 0.986/0.990); inner-edge ladder sampled NEC → **−2.95e-06**
continuum. β = 0.11 is closed, so the climb stops; rungs
0.12–0.14 received their step-(i) stored reads (above) and no
refinement, per the stop rule.

**Failure-protocol follow-up (run, not just logged):** the best
row's one changed freedom — halved smoothing — was fine-audited
at β = 0.09 and 0.10, where the stored row had failed. Result:

| Halved-smoothing row (10,30) M = 8.0, (2.0, 1.16) | β = 0.09 | β = 0.10 |
|---|---|---|
| Fine worst, h = 0.3 / 0.15 (primary) | +1.474e-07 / +2.186e-07 | +1.474e-07 / +2.175e-07 |
| Type-I fraction | 1.000 / 1.000 | 1.000 / 1.000 |
| Core worst | +7.70e-06 / +7.98e-06 | +2.94e-06 / +3.33e-06 |
| Core sampled-null NEC min | +6.64e-06 / +6.51e-06 | +1.75e-06 / +1.61e-06 |
| FD floor (h = 0.3) | 4.1e-09 (worst = 36× floor) | 4.1e-09 (36×) |
| Second path (4th-order) worst, h = 0.3 / 0.15 | +2.148e-07 / +2.164e-07 | −2.99e-07 / +2.154e-07 |
| Primary h = 0.075 worst | +2.174e-07 | +2.163e-07 |
| Second path h = 0.075 worst | — | +2.155e-07 |

β = 0.09 passes every common bar on both discretisations at both
resolutions. At β = 0.10 the single discordant number is the
4th-order h = 0.3 DEC at one point (r = 10.25): −2.99e-07. The
point ladder at that exact point (`p502_verify10b.json`) shows
both discretisations converging to DEC ≈ **+3.28e-06** by
h = 0.15 and identical at h = 0.075/0.0375 (+3.276e-06 both
methods) — the h = 0.3 4th-order value is the same coarse-stencil
artefact pattern Gate-6 documented for this variant at the
Phase-26 suspect point (4th-order deviates at h = 0.3, converges
by h = 0.15). Read at converged resolutions, the second path
agrees on the sign of every deciding margin. **Verdict: β = 0.10
is a fully legal row under the common bars (scan signal under
attack, per the headline).** Its whole-volume worst margin
(+1.47e-07, DEC in the r = 33 tail region on the primary read) is
the family's usual tail-limited worst; the core margins are
+1.6e-06 and up.

## 5. Per-rung margin ledger

| β | Row | Type-I | Core sampled NEC | Binding read | Verdict |
|---|---|---|---|---|---|
| 0.08 | stored (Gate-6) | 1.000 | +2.86e-06 | — | LEGAL (Gate-6) |
| 0.09 | stored | 0.990 | −6.71e-06 | NEC/Type-I, r = 10.25–10.75 (14 pts) | FAIL |
| 0.09 | halved smoothing | 1.000 | +6.64e-06 | tail +1.47e-07 | **LEGAL** (2 paths) |
| 0.10 | stored | 0.964 | −1.65e-05 | NEC/Type-I, r = 10.25 (patch → 12.25, 50 pts) | FAIL |
| 0.10 | halved smoothing | 1.000 | +1.75e-06 | tail +1.47e-07 | **LEGAL** (2 paths, §4 note) |
| 0.11 | stored | 0.927 | −2.64e-05 | NEC/Type-I, r = 10.25 | FAIL |
| 0.11 | best of 246 (halved) | 0.990 | −3.19e-06 | DEC −2.5e-06/−5.8e-06, r = 10.25 | FAIL (2 paths + ladder) |
| 0.12–0.14 | stored | 0.890/0.845/0.777 | −3.7e-05/−4.7e-05/−5.7e-05 | NEC/Type-I, r = 10.25 | FAIL (no refinement — stop rule) |

## 6. Anatomy at the first failing rung (step 5)

- **Binding site:** the inner edge, r ≈ R₁ + 0.25 = 10.25, at
  every β and in every row. It never moves to mid-shell or tail
  as the *binding* (most negative) site; what changes with β is
  the patch's size and reach: 14 points at r ≤ 10.75 (β = 0.09,
  stored) → 50 points reaching r = 12.25 (0.10) → ~100 points
  reaching r = 13.75 (0.11).
- **Binding condition:** NEC, expressed as Hawking–Ellis Type-I
  breakdown — the Eulerian tensor's eigenvalue problem stops
  admitting a timelike eigenvector at the inner-edge points, and
  the sampled-null contraction is negative at exactly those
  points. Eigenvalue margins on the surviving Type-I points stay
  positive throughout (continuum +5.73e-06 at β = 0.09): a
  margins-only audit would have called 0.09–0.14 legal. The
  Type-I + sampled-null bars are what bind.
- **Scaling:** stored-row core sampled NEC vs β is nearly linear:
  +2.86e-06 (0.08, Gate-6) → −6.71e-06 (0.09) → −1.65e-05 (0.10) →
  −2.64e-05 (0.11) → −3.66e-05 (0.12) → −4.68e-05 (0.13) →
  −5.73e-05 (0.14); slope ≈ −1.0e-05 per 0.01 of β, zero crossing
  at β ≈ 0.083 for the stored smoothing. Halving the smoothing
  shifts the whole curve up by ≈ +2.3e-05 at β = 0.11 (from
  −2.64e-05 to −3.2e-06 sampled; DEC eigenvalue becomes the
  binding margin there) — enough to clear 0.09 and 0.10, not
  0.11. Mechanism, stated plainly: the shift gradient at the
  inner edge drives a growing non-Type-I pocket; narrower
  smoothing sharpens the density/pressure support against that
  gradient and delays the pocket's opening by two rungs.
- **Follow-ups:** (run) the halved-smoothing audits at 0.09/0.10
  and the 0.11 ladder above. (logged, not run) a β = 0.105
  bisection of the halved row and a smoothing-scale scan
  {0.35, 0.4, 0.65} at β = 0.11 — both outside the registered
  ±50% envelope/grid as run; either reopens the 0.11 rung if a
  future phase registers it. Closure here is on the registered
  envelope only, stated as such.

## 7. Ceiling verdict

- Stored configuration: ceiling **β = 0.08** (Gate-6), confirmed
  from above — 0.09 fails on a genuine, second-path-confirmed
  inner-edge NEC/Type-I violation, not on the impeached point.
- Family (registered Phase-26 freedoms, gate-standard auditor):
  **β\* = 0.10**, held by the (10,30) M = 8.0 edge-peaked
  wd=6.0/floor=0.2 configuration with halved Gaussian smoothing
  (s_ρ, s_P) = (2.0, 1.16), cosine shift on [10,30] — ADM mass
  8.0 geom = 1.0773×10²⁸ kg, compactness 0.80, unchanged from the
  champion except the smoothing widths. β = 0.11 is closed after
  the full 246-row refinement, its best row failing on both
  discretisations with an h-converged ladder.

## C12 accounting

Every row above is a prescribed-geometry audit: the configuration
is a Fuchs-form TOV-constructed shell metric, and the audited
source is the stress tensor that metric's Einstein tensor
requires; conservation is automatic (Bianchi), as in Phase 26 /
Gate-6. No matter model, formation route, or stability is
claimed for any row, including the β = 0.10 row. Le
(arXiv:2605.25417)'s stricter source-consistency standard is
carried as a standing caveat, not a bar, per the checkpoint.
Nothing was uploaded; no external contact was made.
