# Gate-37 claims bundle - MANIFEST (release v1.27.0)

Every file in this folder, its size in bytes, and where it came from.
Copies are byte-for-byte copies of the named source (md5-verified at
assembly; every copy also cmp-verified against its source at assembly).
This manifest lists every file in the bundle except itself.

| file | bytes | source / traceability |
|---|---|---|
| GATE37.md | 11299 | gate37/GATE37.md (gate record, verbatim copy) md5 2bf574e767f07f6c8e78317be6d44455 |
| RESULTS.md | 4928 | written for this bundle (G37-A/B/C, in Gate-37 §5's wording, verbatim — the only quotable form of the identification claims; the §5 block in RESULTS.md was diff-verified character-for-character against GATE37.md §5 at assembly) |
| RELEASE_v1.27.0.md | 5520 | written for this bundle (release draft; version DOI TBD — minted at release) |
| README_WHATSNEW_v1270.md | 2246 | written for this bundle (prepared README update; applied at upload) |
| code/g37_arithmetic.py | 7468 | gate37/work/g37_arithmetic.py (gate REST/gate-coefficient arithmetic code, verbatim copy) md5 d227781aee9c7699d8973b6c2fbcfc32 |
| code/g37_engine.py | 9102 | gate37/work/g37_engine.py (gate variation engine, verbatim copy) md5 912ba995fa7217450c62f8b3cca0ae35 |
| code/g37_jets.py | 14702 | gate37/work/g37_jets.py (gate Taylor-jet machinery, verbatim copy) md5 c01aa0bd290b396c4304544060bf1f0d |
| code/g37_run.py | 3984 | gate37/work/g37_run.py (gate run script (calibration + deciding reads), verbatim copy) md5 35dc4db1b8cc97153086b2ce10efb559 |
| results/g37_arithmetic.json | 3492 | gate37/work/g37_arithmetic.json (the gate's REST arithmetic, gate coefficient and collapse spot-checks (deciding record), verbatim copy) md5 03fffc9ab8a27153d488e3cf58407552 |
| results/g37_results.json | 4081 | gate37/work/g37_results.json (the gate's calibration + deciding tensor evaluations (deciding record), verbatim copy) md5 86fa57d25eaadab7bac4843891e29377 |
| sources/CHECKPOINT259.md | 7853 | phase259/CHECKPOINT259.md (phase record (the derivation and the ξ⁰ residual), verbatim copy) md5 cabbe903679d2d4107f4c9bbe445a1e4 |
| sources/CHECKPOINT318.md | 6423 | phase318/CHECKPOINT318.md (phase record (the attribution), verbatim copy) md5 48e6e9647ea63121695b78822415a7e6 |
| sources/CHECKPOINT323.md | 4333 | phase323/CHECKPOINT323.md (phase record (the A-throat evaluation), verbatim copy) md5 b17fd160eec4855dc0d3e611ae308598 |
| sources/check_h4_out.json | 4045 | phase318/work/weights263/check_h4_out.json (Phase 318's stored H(6,3)(4) check file — the file Phase 323's route (b) reproduces bit-for-bit, verbatim copy) md5 7a6de927ca3aa22d5930c6c365475193 |
| sources/h203_results.json | 8245 | phase318/work/h203/h203_results.json (Phase 318's Ellis gate-coefficient (203) fit results, verbatim copy) md5 be54028a190d7329612675b041d780d6 |
| sources/p2591_assembled.json | 92328 | phase259/results/p2591_assembled.json (Phase 259's assembled totals on all 24 backgrounds — the record the arbitration and Phase 323's reassembly read, verbatim copy) md5 bc576a3d758e16b690c9bc9a690ccd72 |
| sources/p2591_gate_readout.md | 7289 | phase259/results/p2591_gate_readout.md (Phase 259's gate readout (the stored FULL polynomial, P₀ = 203), verbatim copy) md5 cacb43cdf2fd4feb67be2536da92bd2d |
| sources/p318_derived_H633.json | 84897 | phase318/work/h34/p318_derived_H633.json (Phase 318's derived H(6,3)(3) record, verbatim copy) md5 d939e285da4a0b4e41c243c1d4d163b0 |
| sources/p318_derived_H634.json | 163691 | phase318/work/h34/p318_derived_H634.json (Phase 318's derived H(6,3)(4) record, verbatim copy) md5 54ec7bad09bf53aaca128d612af77b10 |
| sources/p318_final_read.json | 2892 | phase318/results/p318_final_read.json (Phase 318's final read (the joint REST arithmetic), verbatim copy) md5 8714e9755775e0198a4cdec744e47af8 |
| sources/p318_h34_results.json | 13130 | phase318/work/h34/h34_results.json (Phase 318's H(6,3)(3)/(4) derivation results, verbatim copy) md5 ae4b42ad4cae3e9fa87b777c69811618 |
| sources/p318_memo.md | 12223 | phase318/results/p318_memo.md (phase worker memo (the carrier found), verbatim copy) md5 34b182f7de95a64eba67ae58c1c0daa4 |
| sources/p318_registration.md | 3942 | phase318/work/p318_registration.md (phase registration, verbatim copy) md5 8aac0102a6ba69f84e93a133b2011cda |
| sources/p323_control_i.json | 421 | phase323/work/p323_control_i.json (Phase 323's control (i) record (Phase 318's throat read reproduced; gate coefficient 203 → 187), verbatim copy) md5 17435a8e7406b05cbfa58b86b9266746 |
| sources/p323_eval_points.json | 9193 | phase323/work/p323_eval_points.json (Phase 323's exact H{2,0}(3) evaluations at all harness points, verbatim copy) md5 aee29c9a098d450c004dadf9bf75459c |
| sources/p323_exact_jets.json | 2852 | phase323/work/p323_exact_jets.json (the stored exact R-jets the gate's A-throat read consumes, verbatim copy) md5 a3c09c73e8846ec12cb09780715b8abf |
| sources/p323_memo.md | 10111 | phase323/results/p323_memo.md (phase worker memo (the identification), verbatim copy) md5 fe3f4b411e6ed0e71af6947298752ee6 |
| sources/p323_reassembly.json | 21141 | phase323/work/p323_reassembly.json (Phase 323's reassembly record (the wider-set arbitrated maxima), verbatim copy) md5 8feb40c4990cdc9f68dfb0b5e0c14fa8 |
| sources/p323_registration.md | 3188 | phase323/work/p323_registration.md (phase registration (the registered prediction), verbatim copy) md5 6f8ec9856933c0f8405f7764622afbd1 |
| sources/p323_route_b_out.json | 4045 | phase323/work/p323_route_b_out.json (Phase 323's route-(b) output (the independent DF Eq. (2.23) transcription) — byte-identical to sources/check_h4_out.json, as the record states, verbatim copy) md5 7a6de927ca3aa22d5930c6c365475193 |
| sources/p323_validate.json | 1497 | phase323/work/p323_validate.json (Phase 323's validation record (Ellis throat and ℓ = 1 exact values), verbatim copy) md5 41919245210cf9d8c95f2a2a3436ff4a |
| sources/weights263_results.json | 9594 | phase318/work/weights263/weights263_results.json (Phase 318's Eq. (3.14) weights / 263-group results, verbatim copy) md5 4662062cc7f8aea1834d7b871638ca4c |

## Numbers check (every deciding number in Gate-37 §5's claim set, re-derived from the bundled records)

Sources of truth for this section: `results/g37_results.json` and
`results/g37_arithmetic.json` (the gate's own deciding records),
cross-read against the bundled phase records in `sources/`
(`p318_final_read.json`, `p323_reassembly.json`,
`p323_exact_jets.json`). Values below were transcribed from those
files during packaging — packaging copies, hashes, and transcribes
only; no bundled code was executed and nothing was unpickled.

- **Ellis-throat derived tensor E2 = (−80, −16, −112), div exactly
  0** — `results/g37_results.json` (`dec_ellis_throat_L2`:
  E_mixed_diag [−80, −16, −112, −112], diag_match true, div all
  "0"); derived print H{2,0}(3) = (80, 16, 112).
- **A-throat derived tensor (9/4, 3/4, 21/4)** —
  `results/g37_results.json` (`dec_A_throat_L2`: E_mixed_diag
  [−9/4, −3/4, −21/4, −21/4], Ricci lock (0, −1, 1/2), diag_match
  true); the same fractions are carried in
  `sources/p323_exact_jets.json`.
- **Calibration values** — Ellis ℓ = 1 E2 = (47/8, 1/8, 55/8);
  H(6,3)(3) = (32, 8, 44) (E[tr Ric³] = (−32, −8, −44));
  H(6,3)(4) = (4, 4, 16) (E[R_{pq}R_{rs}R^{prqs}] = (−4, −4, −16))
  — all in `results/g37_results.json` with diag_match true, and
  H(3)/H(4) again in `results/g37_arithmetic.json` (`rest_ellis`:
  H3_mine, H4_mine).
- **REST arithmetic** — REST_print = (44/135, 4/27, 100/189)
  rebuilds exactly from the implied print tensor
  (rest_rebuild_matches true); implied print H{2,0}(3) =
  (80, 80/3, 112); implied − derived = (0, 32/3, 0); weighted
  effect "16"; Δbracket (0, −16, 0) against the FULL residual
  (0, +16, 0) → arbitrated (0, 0, 0) — all in
  `results/g37_arithmetic.json` (`rest_ellis`); the REST fractions
  and "80/3" are also carried in `sources/p318_final_read.json`.
- **A-throat REST** — REST_derived(A) = (−23/5040, −13/5040,
  −31/5040); Δbracket (0, −2, +7); arbitrated residual (0, 0, 0);
  implied print at A = (9/4, 25/12, 7/12) (the §4 scope note) —
  `results/g37_arithmetic.json` (`rest_A`).
- **Ellis gate** — P₀ 203 → 187 exactly (P_full_stored
  203.00000000000006; delta_P0_from_read3 "−16"; P0_arbitrated
  "187"); root 0.8603576689230… (stored 0.8603576689230115,
  deviation 6.99×10⁻¹² vs the target's printed 0.86035766893 —
  the claim prints 7.0×10⁻¹²); NEC roots 0.1515510908248 /
  0.2595996822049 / 1.4221825603037, max deviation 4.9×10⁻¹²
  (stored 4.85×10⁻¹²); Δp_r 9.15821986×10⁻⁵, relative deviation
  1.5×10⁻⁸ (stored 1.508×10⁻⁸) — `results/g37_arithmetic.json`
  (`gate`).
- **Wider-set collapse spot-checks** — C:1/2 arbitrated max
  |cell| 5.5×10⁻¹³ (stored new_max_abs_mine 5.542×10⁻¹³) against
  the stored arbitrated 5.1×10⁻¹³ (5.116×10⁻¹³, also in
  `sources/p323_reassembly.json`); E:1/10 arbitrated max |cell|
  2.5×10⁻¹² (stored 2.458×10⁻¹²) against the stored 2.8×10⁻¹²
  (2.800×10⁻¹², also in `sources/p323_reassembly.json`); the old
  FULL cells (C Tr 250.0; E (85.51, 108.04, 14.51)) match the
  stored record — `results/g37_arithmetic.json` (`collapse_C12`,
  `collapse_E110`, `family_maxima_stored`).

Checked: every deciding number in the §5 set — 0 unmatched.

## Assembly notes

- **Selection, stated:** from gate37/, the gate record and the
  gate's own machinery entire (both engines, the run script, the
  arithmetic script, and both results JSONs). Gate-37 has no
  separate checkpoint or registration file (charged at ledger
  entry 810; the charge and verdict forms are on GATE37.md's
  face), so none is bundled. From phase318/, the checkpoint, the
  memo, the registration, the final read, and the deciding
  artefacts of its three sub-lines (h34: the derived H(6,3)(3)/(4)
  records and results; weights263: the Eq. (3.14)-weights results
  and the stored check_h4_out.json; h203: the gate-coefficient fit
  results). From phase323/, the checkpoint, the memo, the
  registration (carrying the registered prediction), and its
  deciding JSONs (exact jets, exact evaluations, reassembly,
  validation, control (i), route-(b) output). From phase259/, the
  three records Gate-37 §7 lists as read for the arbitrated
  assembly (checkpoint, gate readout, assembled totals on all 24
  backgrounds). **Not bundled:** the phases' engine/run code and
  run logs (the gate judged the phases' records and results; the
  deciding re-derivation machinery is the gate's own, bundled in
  `code/`); Phase 259's large derived-tensor candidate files
  (the assembly's stored totals are the deciding record and are
  bundled); the `__pycache__` .pyc files under gate37/work/,
  phase318/work/ and phase323/work/ (compiled artefacts; their
  sources are bundled or are the phases' unbundled engines).
- No source file was edited; no bundled .py was executed and
  nothing was unpickled at any point in packaging.
