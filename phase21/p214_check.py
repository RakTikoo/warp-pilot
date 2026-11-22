#!/usr/bin/env python3
"""
p214_check.py -- P21-4 verdict checker: computes pass/fail
against the registered bars (CHECKPOINT21 S P21-4 + run
record) mechanically from p214_scan.json + p214_audit.json
+ p214_gate.json, plus the PL2 regression vs P12-1's stored
reads.  Writes results/p214_results.json (the item's
results file: verdict + all summary tables the memo rests
on).  No new field computations.  float64 values as stored.
"""
import json
import math
import sys

HERE = '/home/hatch/workspace/warp-pilot/phase21/results/'
P12 = '/home/hatch/workspace/warp-pilot/phase12/results/p121_scan.json'


def vol_clean(row):
    return all(row['volume'][h]['nec_viol_frac_vol'] == 0.0
               and row['volume'][h]['typeI_frac'] == 1.0
               for h in ('0.3', '0.15'))


def main():
    scan = json.load(open(HERE + 'p214_scan.json'))
    gate = json.load(open(HERE + 'p214_gate.json'))
    audit = json.load(open(HERE + 'p214_audit.json'))
    p12 = json.load(open(P12))
    out = dict(item='P21-4 f(T,B) -- checker summary',
               gate_passed=gate['gate_passed'],
               gate_B3_rel_med_max=max(
                   v['rel_med'] for v in gate['checks']['B3_gate']
                   ['rows'].values()))

    # ---- PL2 regression (B2 gamma=0 vs P12-1 PL2 stored)
    reg = []
    for beta in ('1.1', '1.5'):
        p12rows = {r['kappa']: r for r in p12['betas'][beta]['rows']
                   if r['family'] == 'PL2'}
        for r in scan['betas'][beta]['rows']:
            if r['family'] == 'B2' and r['par'][1] == 0.0 \
                    and r['par'][0] in (5.0, 20.0):
                st = p12rows[r['par'][0]]
                dl = abs(math.log10(abs(r['ratio_med']))
                         - math.log10(abs(st['ratio_med']))) \
                    if r['ratio_med'] and st['ratio_med'] else None
                reg.append(dict(beta=float(beta), alpha=r['par'][0],
                                partial=r['partial'], stored_partial=st['partial'],
                                full=r['full'], stored_full=st['full'],
                                ratio_med=r['ratio_med'],
                                stored_ratio_med=st['ratio_med'],
                                dlog10=dl,
                                passed=bool(abs(r['partial'] - st['partial']) <= 0.01
                                            and abs(r['full'] - st['full']) <= 0.01
                                            and dl is not None and dl <= 0.3)))
    out['PL2_regression'] = reg
    out['PL2_regression_passed'] = all(x['passed'] for x in reg)

    # ---- per-beta / per-family summaries
    summ = {}
    kill1_rows = []
    clean_rows = []
    hp_rows = []
    for bs, blk in scan['betas'].items():
        beta = float(bs)
        summ[bs] = {}
        for fam in ('B1a', 'B1b', 'B2', 'B3', 'GR'):
            fr = [r for r in blk['rows'] if r['family'] == fam]
            if not fr:
                continue
            best = max(fr, key=lambda r: (r['partial'], r['full']))
            hp = [r for r in fr if r['health_pass']]
            besthp = max(hp, key=lambda r: (r['partial'], r['full'])) \
                if hp else None
            summ[bs][fam] = dict(
                best=dict(par=best['par'], partial=best['partial'],
                          full=best['full'], health=best['health_pass'],
                          volviol_015=best['volume']['0.15']['nec_viol_frac_vol'],
                          typeI_015=best['volume']['0.15']['typeI_frac']),
                best_health_passing=None if besthp is None else dict(
                    par=besthp['par'], partial=besthp['partial'],
                    full=besthp['full'],
                    volviol_015=besthp['volume']['0.15']['nec_viol_frac_vol'],
                    typeI_015=besthp['volume']['0.15']['typeI_frac'],
                    ratio_med=besthp['ratio_med']),
                n_health_passing=len(hp))
            for r in fr:
                if vol_clean(r):
                    clean_rows.append((beta, fam, r['par']))
                if r['health_pass']:
                    hp_rows.append((beta, fam, r['par'], r['partial']))
                if r['health_pass'] and vol_clean(r) \
                        and r['partial'] >= 0.50:
                    kill1_rows.append((beta, fam, r['par']))
    out['summary'] = summ
    out['volume_clean_rows_any_health'] = clean_rows
    out['health_passing_rows'] = hp_rows
    out['kill_clause1_holds'] = bool(len(kill1_rows) == 0)
    out['rows_simultaneously_health_clean_partial50'] = kill1_rows

    # ---- floor reads from audit
    floor_rows = {}
    for rec in audit['rows']:
        if rec['beta'] in (1.1, 1.5):
            floor_rows.setdefault(str(rec['beta']), []).append(rec)
    out['floor_rows'] = floor_rows
    # floor-move on non-control best rows (health-passing)
    move = {}
    for bs, recs in floor_rows.items():
        mv = False
        for rec in recs:
            if rec['family'] != 'B3' and rec.get('floor_move_25pct') \
                    and rec['scan_health']:
                mv = True
        move[bs] = mv
    out['floor_move_by_beta'] = move
    out['floor_move_any_superluminal'] = any(move.values())
    out['kill_clause2_floor_fails_both'] = bool(
        not move.get('1.1', False) and not move.get('1.5', False))

    # ---- conservation summary
    out['conservation'] = audit.get('conservation', [])

    # ---- ALIGNMENT test
    align = []
    for rec in audit['rows']:
        if rec['beta'] in (1.1, 1.5) and rec.get('antisym_le_002'):
            bs = str(rec['beta'])
            for r in scan['betas'][bs]['rows']:
                if r['family'] == rec['family'] \
                        and str(r['par']) == str(rec['par']) \
                        and r['full'] >= 0.90 and r['health_pass'] \
                        and vol_clean(r):
                    align.append(rec)
    out['alignment_rows'] = align

    # ---- verdict (registered bars, CHECKPOINT21 S P21-4)
    if align:
        verdict = 'ALIGNMENT'
    elif out['kill_clause1_holds'] or out['kill_clause2_floor_fails_both']:
        verdict = 'KILL — TELEPARALLEL CLOSES'
    else:
        verdict = 'INTERMEDIATE'
    out['verdict'] = verdict
    with open(HERE + 'p214_results.json', 'w') as fh:
        json.dump(out, fh, indent=2)
    print(json.dumps(dict(verdict=verdict,
                          PL2_regression_passed=out['PL2_regression_passed'],
                          kill_clause1=out['kill_clause1_holds'],
                          floor_move=move,
                          n_health_passing=len(hp_rows),
                          volume_clean_rows=clean_rows), indent=2))


if __name__ == '__main__':
    main()
