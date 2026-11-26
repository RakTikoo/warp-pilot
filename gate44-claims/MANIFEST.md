# Gate-44 claims bundle - MANIFEST (release v1.35.0)

Every file in this folder, its size in bytes, and where it came from.
Copies are byte-for-byte copies of the named source (md5-verified at
assembly; every copy also cmp-verified against its source at assembly).
This manifest lists every file in the bundle except itself.

| file | bytes | source / traceability |
|---|---|---|
| GATE44.md | 14828 | gate44/GATE44.md (gate record, verbatim copy) md5 0cd170430adabb276566cbf01eb14f19 |
| RESULTS.md | 11065 | written for this bundle (the claim set: the GATE44.md §5 block verbatim — the only quotable form of the Phase 391 claim set; the §5 block in RESULTS.md was diff-verified character-for-character against GATE44.md §5 at assembly) |
| RELEASE_v1.35.0.md | 9662 | written for this bundle (release draft; the GATE44.md §5 claim set embedded verbatim, diff-verified against GATE44.md §5 at assembly; the disclosure paragraph in gate38-claims/RELEASE_v1.29.0.md's exact form; version DOI TBD — minted at release) |
| README_WHATSNEW_v1350.md | 3817 | written for this bundle (prepared README update; applied at upload) |
| code/g44_lib.py | 22242 | gate44/work/g44_lib.py (Gate-44's library — the gate builder generalised to grading bases of n_c ∈ {8, 12} modes, own summary/legality/q/exact-min-null code, verbatim copy) md5 8971de000636b5d6e5b98c435476a9b6 |
| code/g44_audits.py | 2379 | gate44/work/g44_audits.py (Gate-44's audit driver — the registered-bar audits of the seven subjects, verbatim copy) md5 832c01b9a822f536b815158ab8bdabd0 |
| code/g44_screen.py | 4460 | gate44/work/g44_screen.py (Gate-44's screening driver — the two-mask β_crit recalibration of y_his and the convicted artefact, verbatim copy) md5 cb2af6596e75e33b57345b06537e8814 |
| sources/CHECKPOINT391.md | 18691 | phase391/CHECKPOINT391.md (Phase 391's phase record — registration, enrichment registrations, verdict, anatomy, verbatim copy) md5 bc21b0a283f13dafbf9df2bdb8b9af6f |
| sources/p391_memo.md | 9773 | phase391/results/p391_memo.md (Phase 391's worker memo — the claim set as filed, verbatim copy) md5 0ca4ba421cf425d0d93f4b0b63b89701 |
| sources/g44_summary.json | 7183 | gate44/results/g44_summary.json (Gate-44's registered-bar verdict table — chain reads and per-rung audits for all seven subjects, verbatim copy) md5 089885158e97a30c6519bb3598e40270 |
| sources/g44_hashes.json | 690 | gate44/results/g44_hashes.json (Gate-44's hash-gate record — sha256 of every audited vector against its stored record, verbatim copy) md5 079024431fe2d0230604925d820b9fb4 |
| sources/g44_screen.json | 1380 | gate44/results/g44_screen.json (Gate-44's screening record — β_crit of y_his and the convicted artefact under both masks, verbatim copy) md5 0f39cbd6b7eb648f373491cfa60251c1 |
| sources/g44_audits_E2-1.json | 17983 | gate44/results/g44_audits_E2-1.json (Gate-44's full audit record for E2-1 — chain reads incl. the grading vector and both rungs at both spacings, verbatim copy) md5 d207956495cd74b813b0adf6b2651d4c |
| sources/g44_audits_E1-4.json | 18203 | gate44/results/g44_audits_E1-4.json (Gate-44's full audit record for E1-4, verbatim copy) md5 c24186b45dbab22d14381b64861e5090 |
| sources/g44_audits_H3.json | 18025 | gate44/results/g44_audits_H3.json (Gate-44's full audit record for H3 — incl. the fine-spacing q read q_max 1.000246396923074 at the r = 16.3 flux site, verbatim copy) md5 19ba8f28b246429ebdaa0fc3c050d7fa |
| sources/g44_audits_H4.json | 9425 | gate44/results/g44_audits_H4.json (Gate-44's full audit record for H4, verbatim copy) md5 6f203e870e968431a72458a725fa60a3 |
| sources/g44_audits_H5.json | 9287 | gate44/results/g44_audits_H5.json (Gate-44's full audit record for H5, verbatim copy) md5 832090dbb0b9bbc72cf41e1f6c856829 |
| sources/g44_audits_H6.json | 9466 | gate44/results/g44_audits_H6.json (Gate-44's full audit record for H6, verbatim copy) md5 b13e9a16f92d791e5911995969f7547c |
| sources/g44_audits_y_his.json | 9208 | gate44/results/g44_audits_y_his.json (Gate-44's full audit record for the c = 0 control, verbatim copy) md5 535557aa52cd0802cc383536698866c8 |

## Numbers check (every deciding number in the final set, transcribed from the bundled records)

Sources of truth for this section: the bundled gate record
`GATE44.md` (§§1–6), the bundled Phase 391 records in
`sources/` (`CHECKPOINT391.md`, `p391_memo.md`), and Gate-44's
bundled result records in `sources/` (`g44_summary.json`,
`g44_hashes.json`, `g44_screen.json`, `g44_audits_<subject>.json`).
Values below were transcribed from those files during packaging —
packaging copies, hashes, and transcribes only; no bundled code was
executed and nothing was unpickled. Spot-checks performed against
the bundled JSON records at assembly: 65 checks covering every
deciding value below — the raised best's legal and failing rungs,
the E1 rung pair, the three tie holders, H3's ceiling and restated
failure, the control, the two-mask screen, all six subject hashes,
and E2-1's chain reads and bound-sitters — 0 unmatched.

- **Hash gate (C-0)** — every audited vector re-hashed (sha256 of
  the float64 tobytes) against its stored record, all
  `hash_match = true`: E2-1
  **6167938325934832baac896f7e177be6e0bed594fe43865c9bafcfe8a2573066**,
  E1-4 2732e3be…, H3 29aa162b…, H4 08773ac6…, H5 2c64fb21…, H6
  0d965624… (full values in `sources/g44_hashes.json`). The five
  holders of the Gate-42 best are five distinct vectors (S1
  84c9043e…, Rank-1 d1efd424…, H4, H5, H6 — all hashes distinct) —
  `GATE44.md` §1; `sources/g44_hashes.json`.
- **Builder reproduction (C-0b)** — at n_c = 8 the gate builder's
  construction grid count is **1,200,671** — Gate-42's count
  exactly; at n_c = 12 it reproduces Phase 391's stored E2-1 chain
  reads at near-roundoff: ρ_max gate
  **3.2585104937459165×10⁻⁴** vs stored 3.2585104937459127×10⁻⁴,
  λ **0.8931410086746383** vs 0.8931410086746355, k
  **0.024530591100784323** vs 0.024530591100784312, M equal to the
  target at 1.5×10⁻¹⁵ relative. E2-1's grading vector sits on the
  registered E2 box at exactly the two stored bound-sitters
  (c₁ = **+2.25**, c₉ = **−2.25**) and nowhere else —
  `GATE44.md` §1; `sources/g44_audits_E2-1.json` (`chain_reads`).
- **The raised class best (G44-B)** — E2-1 at β = 0.191796875:
  LEGAL under the registered bars — wa worst margin SEC
  **7.075488047566495×10⁻⁸** at r = 6.0, **13.364×** the FD floor,
  Type-I 1.000 at both spacings, fine-spacing worst
  5.824604103877142×10⁻⁸, audit4 worst
  **5.407155495297896×10⁻⁸**, q_max 0.9947333580434966 at
  r = 19.75 (a direction-sampled diagnostic; the phase's stored
  read is 0.9933 at the same site). At β = 0.1921875: FAILS — wa
  worst SEC **−7.281065524914095×10⁻⁷** at r = 9.75, audit4
  −7.372241145243595×10⁻⁷, Type-I 1.000 — `GATE44.md` §2;
  `sources/g44_summary.json` (`E2-1`).
- **The Step-0 tie (G44-B)** — at β = 0.18671875, all LEGAL under
  the registered bars: H4 wa worst SEC
  **4.335645797463759×10⁻⁷** at r = 3.75 (audit4
  4.331310364585308×10⁻⁷); H5 **4.495082158967855×10⁻⁷** at
  r = 5.0 (audit4 4.419619236909114×10⁻⁷); H6
  **2.782550894983649×10⁻⁷** at r = 3.75 (audit4
  2.776849973108382×10⁻⁷); wa Type-I 1.000 at both spacings for
  all three — `GATE44.md` §3; `sources/g44_summary.json`
  (`H4`, `H5`, `H6`).
- **H3's ceiling and restated failure (G44-C)** — LEGAL at
  β = 0.1859375: wa worst SEC **4.7008123559798945×10⁻⁷** at
  r = 3.75, audit4 4.696668931640235×10⁻⁷. At β = 0.18671875:
  FAILS on the Type-I clause at the fine spacing alone — wa
  Type-I (coarse) 1.000, wa fine Type-I
  **0.9971857410881801** (the quoted 0.99719), every EC margin
  positive at both spacings (fine worst
  4.690155620753531×10⁻⁷), fine-spacing shell sampled-NEC
  **−3.550122019299614×10⁻⁸** (the quoted −3.6×10⁻⁸), and the
  fine-spacing q read at the r = 16.3 flux site
  **q_max 1.000246396923074** (the quoted 1.00025) —
  `GATE44.md` §3; `sources/g44_summary.json` (`H3`),
  `sources/g44_audits_H3.json`
  (`audits.0.18671875.by_h.h0.01875.q.q_max`).
- **Calibration note C-1** — for H4 and H5 the second path
  classifies a handful of significant points as non-Type-I
  (audit4 Type-I **0.9962476547842402** for H4,
  **0.99812382739212** for H5 — the phase's own stored record
  shows the identical fractions, 0.99625 / 0.99812 / 0.99906)
  while every audit4 deciding margin and its sampled-NEC minimum
  over the significant set stay positive (H4 audit4 sampled-NEC
  min +2.698629411903559×10⁻⁷; H5 +2.865913544139822×10⁻⁷). The
  registered bar — audit4 agreement on the sign of every deciding
  (eigenvalue) margin — is met; no ruling turns on a sampled
  diagnostic at a non-Type-I point — `GATE44.md` §1 (C-1), §3;
  `sources/g44_summary.json`.
- **The enrichment ladder (G44-D)** — E1-4 LEGAL at
  β = 0.18984375: wa worst DEC **1.1509578036978188×10⁻⁷** at
  r = 16.6 (digit-identical to the stored +1.150958×10⁻⁷),
  audit4 1.1741415062746063×10⁻⁷, Type-I 1.000; FAILS at
  0.19046875 (DEC −9.320040549623364×10⁻⁷ at r = 16.6) — E1
  bought **+0.003125**; E2-1's rung (above) bought a further
  **+0.001953125**; ladder total **+0.005078125** over the
  Gate-42 best — `GATE44.md` §4; `sources/g44_summary.json`
  (`E1-4`).
- **Controls and recalibration (G44-A, claim d)** — y_his
  (c = 0) LEGAL at β = 0.1363: wa worst SEC
  **3.404177926256379×10⁻⁷** at r = 5.0, **109.508×** the FD
  floor, Type-I 1.000 at both spacings, audit4
  3.3957704573015516×10⁻⁷ — ratio **1.000** to Gate-42's /
  Gate-7's stored read. On the gate's own FD screen:
  β_crit(y_his) = **0.136328125** (bracket [0.1359375,
  0.13671875]) under BOTH masks; the convicted Phase-386
  artefact reads **0.174609375** under the old core mask
  (bracket [0.17421875, 0.175]) and **0.120703125** under the
  extended mask (bracket [0.1203125, 0.12109375]), its extended
  score at 0.1363 **−7.0428305387819725×10⁻⁶** (SEC at
  r = 7.0) — `GATE44.md` §4; `sources/g44_summary.json`
  (`y_his`), `sources/g44_screen.json`.

Checked: every deciding number in the final set — 0 unmatched.

## Assembly notes

- **Selection, stated:** the gate record entire (`GATE44.md` —
  its §5 is the only quotable form of the set). From gate44/, the
  gate's machinery entire (three files in `code/` — Gate-44 ran
  its own computation, so this bundle carries the gate's code)
  and its deciding result records (in `sources/`: the summary,
  hash and screen JSONs and the seven per-subject audit JSONs).
  From phase391/, the checkpoint and the worker memo — the
  phase's verdict records, carrying the claim set as filed.
  **Not bundled:** Phase 391's own machinery and its
  control/search/screen/verdict JSONs and logs (the gate judged
  Phase 391's records; its deciding values are carried in the
  bundled gate records and the bundled phase checkpoint/memo);
  Gate-44's run logs (g44_audits.log, g44_screen.log — console
  transcripts of the bundled drivers); the `__pycache__`
  .pyc files under the gate work directory (compiled artefacts);
  the stored design vectors and harvest/state files the gate's
  code reads (identified on the bundled code's face and in
  GATE44.md §6, with their hashes in the bundled
  `g44_hashes.json`).
- The verbatim block embedded in the written files was
  diff-verified character-for-character at assembly: the
  GATE44.md §5 claim set in RESULTS.md and in
  RELEASE_v1.35.0.md — both checks exact. The disclosure
  paragraph in RELEASE_v1.35.0.md is in
  gate38-claims/RELEASE_v1.29.0.md's exact form.
- No source file was edited; no bundled .py was executed and
  nothing was unpickled at any point in packaging.
