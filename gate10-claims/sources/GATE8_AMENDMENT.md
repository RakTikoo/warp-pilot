# Gate-8 — AMENDMENT (2026-11-22): the G8-1 floor-band figure

**Status:** addendum to `GATE8.md`. Claim **G8-1 only** (the
composed payload at 0.0799c, Phase 46 P46-2). This is a
**wording correction, not a re-audit**: no claim number was
recomputed, no other claim is touched, and the gate's
verdict stands exactly as recorded — **UPLOAD-READY AFTER
RESTATEMENT**; correctness REPRODUCED WITH RESTATEMENT;
novelty NOVEL (carried under the Uniqueness Protocol only
as a new catalogue entry of allowed warp geometries). The
amendment changes **one figure** in the restated wording:
the cavity DEC floor band, `4×10⁻⁵` → `2.3×10⁻⁴`.

## Why

At bundle assembly (release v1.10.0) claim G8-1 was HELD
(`gate8-claims/RESULTS.md` §1, hold note): the gate's
restated wording (`results/wA_g8_1.md` §6) states the
near-edge cavity DEC read is sign-unstable "at
|DEC| ≲ 4×10⁻⁵ under refinement," but the gate's own
stored refinement ladder reads well outside that band at
its finest spacing. Assembly does not repair gate
wordings; this amendment does, on a re-read of the stored
record.

## The original wording (affected sentence, verbatim)

> One floor caveat is part of the claim: in the near-edge cavity shell 4.6 < r < 5 the DEC read is at the discretisation/representation floor — it touches −3.7×10⁻⁶ at h = 0.075 on the focused set, is sign-unstable across spacings, directions and discretisations at |DEC| ≲ 4×10⁻⁵ under refinement, and has no convergent negative continuum value in either of two discretisations different in kind; every stencil-clear cavity read is ≥ +9.98×10⁻⁵ and Type I remains 1.000 — the touch is a floor artefact, and no clean continuum DEC value is asserted for that shell.

(The full restated wording stands in `results/wA_g8_1.md`
§6 and in `gate8-claims/RESULTS.md` §1; only the sentence
above contains the corrected figure.)

## The stored record, re-read

Second path: the raw run JSONs were read directly
(`results/wa_run2.json`, `results/wa_run3.json`,
aggregated in `results/wa_g8_1_numbers.json`); the bundle
copies in `gate8-claims/results/` are byte-identical to
the `gate8/results/` originals (md5 `5067cfe8…` for
`wa_run2.json`, `bf80d248…` for `wa_run3.json`). No memo
summary was relied on.

Fixed caveat site (point (−2.245, −2.387, −3.508),
r = 4.8, in the near-edge cavity shell 4.6 < r < 5);
DEC read by spacing h:

| discretisation | h = 0.15 | h = 0.075 | h = 0.0375 | h = 0.01875 |
|---|---|---|---|---|
| gate path, 4th-order direct-∂² (`richardson_o4.dec_series`) | +6.87×10⁻⁶ | −1.21×10⁻⁵ | −3.95×10⁻⁵ | **−2.06×10⁻⁴** |
| gate path, 2nd-order direct-∂² (`richardson_o2.dec_series`) | −8.89×10⁻⁵ | −3.02×10⁻⁵ | −3.52×10⁻⁵ | −1.71×10⁻⁴ |
| phase judge (comparison path) | +5.80×10⁻⁶ | +1.08×10⁻⁶ | −3.25×10⁻⁵ | −1.90×10⁻⁵ |

Hawking–Ellis Type-I holds at the site at every rung of
every ladder above. Focused-set cavity DEC minima
(4th-order): +2.06×10⁻⁶ (h = 0.15), −1.21×10⁻⁵ (0.075),
−7.47×10⁻⁵ (0.0375), each at r = 4.8; stencil-clear cavity
minima at the same spacings: +9.98×10⁻⁵, +1.18×10⁻⁴,
+1.27×10⁻⁴. Radial profile at h = 0.01875 (4th-order):
r = 4.7 → +1.27×10⁻⁴, r = 4.8 → −2.06×10⁻⁴,
r = 4.9 → +9.93×10⁻⁵, r = 4.95 → **−2.27×10⁻⁴** — the
sign oscillates on a ~0.1 radial wavelength, the
representation-structure behaviour the gate record
describes. The pairwise Richardson extrapolants of the
two gate-path series end at −2.17×10⁻⁴ (4th-order) and
−2.16×10⁻⁴ (2nd-order); neither series supports a
Richardson limit, as the gate found.

**Corrected band.** The largest |DEC| at which sign
instability under refinement is actually observed in
this record is **2.27×10⁻⁴** (−2.2704519008012248×10⁻⁴
at **r = 4.95**, 4th-order direct-∂² discretisation,
h = 0.01875; the fixed-site excursion at the same
spacing and discretisation is −2.0585277158458493×10⁻⁴
at r = 4.8). Reads of both signs occur across spacings,
directions and discretisations throughout the range up
to that figure. The band is therefore restated as
**|DEC| ≲ 2.3×10⁻⁴** — the observed maximum rounded up
to one significant figure, the same rounding the
original figure applied to its (incomplete) ladder
(4×10⁻⁵ was the h = 0.0375 rung, −3.95×10⁻⁵, rounded
up; the wording understated the ladder's two finest
rungs, which the worker's own §3 prints in full).

**One stored rung is excluded from the band, on the
record.** `wa_run3.json` (`mine_caveat_site_fine`)
extends the 4th-order site series one spacing finer, to
h = 0.009375, where DEC reads −8.54×10⁻⁴. At that rung
the same evaluator's density and NEC reads at the site
are also negative (ρ = −1.65×10⁻⁴, NEC = −1.20×10⁻⁴,
against ρ = +1.93×10⁻⁴…+3.15×10⁻⁴ and NEC > 0 at every
ladder rung): the point evaluation itself, not the DEC
combination, has broken down. That rung is a single
discretisation only, carries no stored Type-I read, and
sits below twice the stored metric's tabulation step
(dr = 0.005); both registered ladders and the judge
comparison terminate at h = 0.01875. It is therefore
not a DEC sign-instability read of the cavity shell and
does not set the band. So the exclusion is not silent:
if that rung were counted as a DEC-floor read, the band
would have to read ≲ 8.6×10⁻⁴.

**The substantive settlement is untouched** and is
supported by the same record: no convergent negative
continuum value in either discretisation; every
stencil-clear cavity read ≥ +9.98×10⁻⁵; Type-I 1.000
throughout the ladder.

## The amended restated wording for G8-1 (full text)

> Nested GR shells with the inner shell solved in the composed lapse (coordinate β_i turned down by exactly the lapse factor ×0.6451; orthonormal shift W held at the verified alone value 0.06638) carry a payload at 0.0799c at full bars on the registered audit pattern (full-volume all-directions NEC/WEC/SEC/DEC at h = 0.3/0.15, Hawking–Ellis Type-I fraction 1.000, conservation clean; h = 0.15 worst margins by region: inner wall +9.79×10⁻⁴, outer wall +4.05×10⁻⁵, payload region +1.09×10⁻⁴; independently reproduced by a direct-∂² evaluator: +9.74×10⁻⁴ / +2.86×10⁻⁵ / +1.14×10⁻⁴). One floor caveat is part of the claim: in the near-edge cavity shell 4.6 < r < 5 the DEC read is at the discretisation/representation floor — it touches −3.7×10⁻⁶ at h = 0.075 on the focused set, is sign-unstable across spacings, directions and discretisations at |DEC| ≲ 2.3×10⁻⁴ under refinement, and has no convergent negative continuum value in either of two discretisations different in kind; every stencil-clear cavity read is ≥ +9.98×10⁻⁵ and Type I remains 1.000 — the touch is a floor artefact, and no clean continuum DEC value is asserted for that shell. Follow-up rows (not verdict rows): dual re-equilibration passes at 0.0729; β_o capped at its verified 0.05 gives a passing 0.0821 (independently confirmed). At 0.0998 the inner wall passes (+9.86×10⁻⁴; the P41-3 inner kill is gone) but the outer wall fails: its worst point is Hawking–Ellis non-Type-I in two independent discretisations (sampled NEC ≈ −3.4×10⁻⁵; the Phase-1 judge's sampled SEC quantification is −2.73×10⁻⁴), so the P22-3 trigger does not fire. C12: subluminal pre-arranged configuration; construction-inclusive arrival ≥ D/c; no transport claim beyond the payload's own speed.

## Byte check

Whitespace-normalised comparison of the full wording
above against `results/wA_g8_1.md` §6: 266 word tokens
on both sides, exactly **one** differing token —
`4×10⁻⁵` → `2.3×10⁻⁴` in the floor-caveat sentence.
Every other word of the gated wording is unchanged.

## Effect

The bundle-assembly hold on G8-1 is **lifted**.
G8-1 is upload-ready after restatement **as amended
here**, and is released in v1.10.0 (release body:
`RELEASE_NOTES_v1100.md`); its ledger entry moves to the
PUBLISHED tier in the amended wording with that
release. GATE8.md itself is not edited — this addendum
is the correction of record, in the programme's erratum
pattern.
