#!/usr/bin/env python
"""GATE-31 staged driver. Registration:
gate31/work/g31_registration.md (read in full before this
run; it governs). Stages, one process each:
  controls   CTRL-1 (stored-state reproduction, diff 0.0),
             CTRL-2 (fresh G4 march vs stored, diff 0.0),
             CTRL-4 md5 before/after this stage,
             G5 cost probe (sec.3(e))
  g3|g4|g5   one grid's march to T_END=1.0 + window reads
             (g5 also the sec.1 CERT-4 non-clause bars at
             the bracket instants)
  evaluation CTRL-3 (from the three grids' t=0.5 rows),
             span record (sec.3(d)), Richardson table,
             CERT-1..4, verdict form under sec.4; assembles
             gate31/work/g31_results.json
Frame: Phase 166 pin, Gate-19-corrected tensor, venv
python, float64. Writes ONLY under gate31/work/.
Nothing is tuned against any read."""
import hashlib, json, sys, time
import numpy as np

WP = '/home/hatch/workspace/warp-pilot/'
G31 = WP + 'gate31/work/'
sys.path.insert(0, WP + 'phase288/work')
import p288_lib as L              # noqa: E402  (sets sys.path)
import p1621_engine as B          # noqa: E402

PROTECTED = [WP + 'phase169/work/p1692_engine.py',
             WP + 'phase167/work/p167_engine.py',
             WP + 'phase162/work/p1621_engine.py']
P287_NPZ = WP + 'phase287/work/p287_built_profiles_amended.npz'
MEM_NPZ = WP + 'phase288/work/p288_member_state.npz'
P288_RES = WP + 'phase288/results/p288_results.json'
CK = list(B.CLAUSE_KEYS)
TH = B.AUDIT_TH
WINDOW = [0.5, 0.525, 0.55, 0.56875, 0.575, 0.58125,
          0.5875, 0.6, 0.625, 0.65]
T_LO, T_HI = 0.575, 0.58125
BINDING = ['NEC_ph', 'DEC_ph']
GRIDS = {'g3': (5761, 0.00125), 'g4': (11521, 0.000625),
         'g5': (23041, 0.0003125)}
BAR = 1e-6


def md5s():
    return {p: hashlib.md5(open(p, 'rb').read()).hexdigest()
            for p in PROTECTED}


def profiles():
    z = np.load(P287_NPZ)
    auu = np.array(z['Auu_new'], dtype=np.float64)
    jder = np.array(z['J_derived'], dtype=np.float64)
    z.close()
    return auu, jder


def slim(row):
    return {'t': row['t'], 'march_index': row['march_index'],
            'clause_minima': row['clause_minima'],
            'mom_resid_max': row['mom_resid_max']}


def stage_controls():
    t0 = time.time()
    out = {'stage': 'controls', 'md5_before': md5s()}
    auu, jder = profiles()
    stored_res = json.load(open(P288_RES))
    # ---- CTRL-1: stored-state reproduction ----
    z = np.load(MEM_NPZ)
    state = (np.array(z['MU']), np.array(z['U']),
             np.array(z['MTT']), np.array(z['th_f']),
             np.array(z['times']))
    z.close()
    rows_ref = (stored_res['member_instants']
                + stored_res['member_refinement_instants'])
    recomputed = []
    max_d_cl = 0.0
    max_d_mom = 0.0
    for ref in rows_ref:
        r = L.read_arm_A(int(ref['march_index']), state,
                         auu, jder)
        recomputed.append(slim(r))
        for kk in CK:
            d = abs(r['clause_minima'][kk]
                    - ref['clause_minima'][kk])
            max_d_cl = max(max_d_cl, d)
        for kk in ('mom_rho', 'mom_th', 'mom_ph'):
            d = abs(r['mom_resid_max'][kk]
                    - ref['mom_resid_max'][kk])
            max_d_mom = max(max_d_mom, d)
    out['ctrl1'] = {
        'n_rows': len(rows_ref),
        'max_abs_diff_clause_minima': float(max_d_cl),
        'max_abs_diff_mom_resid_max': float(max_d_mom),
        'pass': bool(max_d_cl == 0.0 and max_d_mom == 0.0)}
    out['ctrl1_recomputed_rows'] = recomputed
    del state
    print('CTRL-1 clause diff', max_d_cl, 'mom diff',
          max_d_mom, flush=True)
    # ---- CTRL-2: fresh G4 march vs stored [::40] ----
    st = L.march_incumbent(11521, 0.000625, 1.0, 0.25)
    z = np.load(MEM_NPZ)
    d = {}
    for name, arr in (('MU', st[0]), ('U', st[1]),
                      ('MTT', st[2])):
        d[name] = float(np.max(np.abs(arr[::40]
                                      - np.array(z[name])[::40])))
    z.close()
    del st
    out['ctrl2'] = {'max_abs_diff_sub40': d,
                    'pass': bool(all(v == 0.0
                                     for v in d.values()))}
    print('CTRL-2', d, flush=True)
    # ---- G5 cost probe (sec.3(e)): [0, 0.05], 160 steps ----
    tp = time.time()
    stp = L.march_incumbent(23041, 0.0003125, 0.05, 0.25)
    probe_wall = time.time() - tp
    probe_shape = list(stp[0].shape)
    del stp
    proj = 20.0 * probe_wall
    out['probe'] = {'t_end': 0.05, 'steps': 160,
                    'state_shape': probe_shape,
                    'wall_s': probe_wall,
                    'projected_full_wall_s': proj,
                    'threshold_s': 900.0,
                    'fires': bool(proj > 900.0)}
    print('PROBE wall %.2fs projected %.2fs fires %s'
          % (probe_wall, proj, proj > 900.0), flush=True)
    out['md5_after'] = md5s()
    out['ctrl4_pass_this_stage'] = bool(
        out['md5_after'] == out['md5_before'])
    out['wall_s'] = time.time() - t0
    json.dump(out, open(G31 + 'g31_stage_controls.json', 'w'),
              indent=1)
    print('WROTE stage_controls, wall %.1fs' % out['wall_s'],
          flush=True)


def nonclause_bars(m, state, jder):
    MU, U, MTT, th_f, times = state
    t = float(times[m])
    mu_a = B.interp_fine(th_f, MU[m], TH)
    mtt_a = B.interp_fine(th_f, MTT[m], TH)
    rho_g = np.linspace(0.0, 2.0, 41)
    Rdom = (B.R00 + 0.1 * rho_g[None, :] ** 2
            + 0.5 * t * t * B.att(TH)[:, None])
    jpose_a = jder + np.exp(-2.0 * B.phi0(TH)) * mtt_a
    phi2_a = 0.5 * np.exp(2.0 * mu_a) * jpose_a
    Phidom = (B.phi0(TH)[:, None]
              + rho_g[None, :] ** 2 * phi2_a[:, None])
    return {'t': t, 'march_index': int(m),
            'flare_min': float(np.min(np.exp(-2.0 * mu_a)
                                      * B.AUU)),
            'domain_R_min': float(np.min(Rdom)),
            'domain_exp2Phi_min': float(np.min(
                np.exp(2.0 * Phidom)))}


def stage_grid(name):
    t0 = time.time()
    n_th, h_t = GRIDS[name]
    auu, jder = profiles()
    st = L.march_incumbent(n_th, h_t, 1.0, 0.25)
    march_wall = time.time() - t0
    rows = []
    for t in WINDOW:
        m = int(round(t / h_t))
        rows.append(slim(L.read_arm_A(m, st, auu, jder)))
    out = {'stage': name, 'n_th': n_th, 'h_t': h_t,
           'march_wall_s': march_wall, 'window_rows': rows}
    if name == 'g5':
        bars = {}
        for t in (T_LO, T_HI):
            m = int(round(t / h_t))
            b = nonclause_bars(m, st, jder)
            # momentum worst from the window row at same m
            row = [r for r in rows
                   if r['march_index'] == m][0]
            b['mom_worst'] = float(max(
                row['mom_resid_max'].values()))
            b['mom_resid_max'] = row['mom_resid_max']
            bars[str(t)] = b
        out['nonclause_bars'] = bars
    del st
    out['wall_s'] = time.time() - t0
    json.dump(out, open(G31 + 'g31_stage_%s.json' % name, 'w'),
              indent=1)
    print('WROTE stage_%s march %.1fs total %.1fs'
          % (name, march_wall, out['wall_s']), flush=True)


def richardson(v3, v4, v5):
    d34 = v3 - v4
    d45 = v4 - v5
    if d34 * d45 > 0.0:
        import math
        p = math.log2(d34 / d45)
        if 0.5 <= p <= 6.0:
            Lval = v5 - d45 / (2.0 ** p - 1.0)
            r = abs(Lval - v5)
            case = 'monotone'
        else:
            p_out, Lval, r = p, v5, max(abs(d34), abs(d45))
            case = 'degenerate_inadmissible_p'
            return {'v3': v3, 'v4': v4, 'v5': v5,
                    'd34': d34, 'd45': d45, 'case': case,
                    'p': p_out, 'L': Lval, 'r': r,
                    'limit_certified': bool(
                        r <= BAR and abs(d34) <= BAR
                        and abs(d45) <= BAR)}
    else:
        p, Lval, r = None, v5, max(abs(d34), abs(d45))
        case = 'degenerate'
    return {'v3': v3, 'v4': v4, 'v5': v5, 'd34': d34,
            'd45': d45, 'case': case, 'p': p, 'L': Lval,
            'r': r, 'limit_certified': bool(
                r <= BAR and abs(d34) <= BAR
                and abs(d45) <= BAR)}


def stage_evaluation():
    t0 = time.time()
    ctrl = json.load(open(G31 + 'g31_stage_controls.json'))
    res = {'gate': 'GATE-31',
           'registration': 'gate31/work/g31_registration.md',
           'frame': 'Phase 166 pin, Gate-19-corrected tensor, '
                    'float64',
           'window': WINDOW, 'bracket': [T_LO, T_HI],
           'binding_clauses': BINDING,
           'md5_protected_before': ctrl['md5_before'],
           'controls': {
               'CTRL-1': ctrl['ctrl1'],
               'CTRL-2': ctrl['ctrl2'],
               'CTRL-4_md5_controls_stage': bool(
                   ctrl['ctrl4_pass_this_stage'])},
           'probe': ctrl['probe'],
           'walls_s': {'controls_stage': ctrl['wall_s']}}
    grids = {}
    for name in ('g3', 'g4', 'g5'):
        try:
            g = json.load(open(G31 + 'g31_stage_%s.json'
                               % name))
            grids[name] = g
            res['walls_s'][name + '_stage'] = g['wall_s']
            res['walls_s'][name + '_march'] = g['march_wall_s']
        except FileNotFoundError:
            grids[name] = None
    res['per_grid_window_rows'] = {
        name: (grids[name]['window_rows'] if grids[name]
               else None) for name in grids}
    if grids['g5']:
        res['nonclause_bars_g5'] = grids['g5']['nonclause_bars']
    # ---- span record (sec.3(d)) ----
    stored_res = json.load(open(P288_RES))
    span_rows = [r for r in stored_res['member_instants']
                 if r['t'] <= 0.575 + 1e-12]
    recomp = {r['march_index']: r
              for r in ctrl['ctrl1_recomputed_rows']}
    span = {}
    span_ok = True
    for kk in CK:
        vals = [(r['t'], r['clause_minima'][kk])
                for r in span_rows]
        tmin, vmin = min(vals, key=lambda x: x[1])
        # cross-check vs CTRL-1 recomputation at those rows
        xd = 0.0
        for r in span_rows:
            rc = recomp[r['march_index']]
            xd = max(xd, abs(rc['clause_minima'][kk]
                             - r['clause_minima'][kk]))
        span_ok = span_ok and xd == 0.0
        span[kk] = {'min': vmin, 't_at_min': tmin,
                    'crosscheck_max_abs_diff_vs_ctrl1': xd}
    res['span_record'] = {
        'n_instants': len(span_rows),
        't_range': [span_rows[0]['t'], span_rows[-1]['t']],
        'per_clause_minima': span,
        'crosscheck_pass': bool(span_ok)}
    # ---- decision order (sec.4) ----
    verdict = None
    failing = None
    if not ctrl['ctrl1']['pass']:
        verdict, failing = 'FAILS-(b)', 'CTRL-1'
    elif not ctrl['ctrl2']['pass']:
        verdict, failing = 'FAILS-(a)', 'CTRL-2'
    elif ctrl['probe']['fires']:
        verdict, failing = ('FAILS-(c)',
                            'G5 cost probe sec.3(e)')
        res['controls']['CTRL-3'] = 'not evaluated: G5 not run'
    if verdict is None and grids['g5'] is None:
        verdict, failing = ('INCOMPLETE',
                            'G5 stage missing without probe '
                            'firing')
    if verdict is None:
        # ---- CTRL-3 from t=0.5 rows ----
        def row_at(gname, t):
            return [r for r in grids[gname]['window_rows']
                    if abs(r['t'] - t) < 1e-12][0]
        c3 = {}
        c3pass = True
        for kk in BINDING:
            v3 = row_at('g3', 0.5)['clause_minima'][kk]
            v4 = row_at('g4', 0.5)['clause_minima'][kk]
            v5 = row_at('g5', 0.5)['clause_minima'][kk]
            d34, d45 = abs(v3 - v4), abs(v4 - v5)
            ok = d34 <= BAR and d45 <= BAR
            c3pass = c3pass and ok
            c3[kk] = {'v3': v3, 'v4': v4, 'v5': v5,
                      'abs_d34': d34, 'abs_d45': d45,
                      'pass': bool(ok)}
        res['controls']['CTRL-3'] = {'per_clause': c3,
                                     'pass': bool(c3pass)}
        if not c3pass:
            verdict, failing = 'FAILS-(a)', 'CTRL-3'
    if verdict is None:
        # ---- Richardson + CERT ----
        table = []
        for t in WINDOW:
            entry = {'t': t}
            for kk in BINDING:
                vs = {}
                for gname, key in (('g3', 'v3'), ('g4', 'v4'),
                                   ('g5', 'v5')):
                    vs[key] = [r for r in
                               grids[gname]['window_rows']
                               if abs(r['t'] - t) < 1e-12
                               ][0]['clause_minima'][kk]
                entry[kk] = richardson(vs['v3'], vs['v4'],
                                       vs['v5'])
            table.append(entry)
        res['richardson_table'] = table
        by_t = {e['t']: e for e in table}
        cert = {}
        f1 = None
        for e in table:
            for kk in BINDING:
                if not e[kk]['limit_certified'] and f1 is None:
                    f1 = {'t': e['t'], 'clause': kk}
        cert['CERT-1'] = {'pass': f1 is None,
                          'failing': f1}
        f2 = None
        for kk in BINDING:
            lo, hi = by_t[T_LO][kk], by_t[T_HI][kk]
            if not (lo['L'] >= 0.0 and hi['L'] < 0.0
                    and lo['v5'] >= 0.0 and hi['v5'] < 0.0):
                f2 = {'clause': kk, 'L_t_lo': lo['L'],
                      'L_t_hi': hi['L'], 'v5_t_lo': lo['v5'],
                      'v5_t_hi': hi['v5']}
                break
        cert['CERT-2'] = {'pass': f2 is None, 'failing': f2}
        f3 = None
        for e in table:
            if e['t'] <= T_LO + 1e-12:
                for kk in BINDING:
                    if e[kk]['L'] < 0.0 or e[kk]['v5'] < 0.0:
                        f3 = {'t': e['t'], 'clause': kk,
                              'L': e[kk]['L'], 'v5': e[kk]['v5']}
                        break
            if f3:
                break
        cert['CERT-3'] = {'pass': f3 is None, 'failing': f3}
        # CERT-4: non-binding G5 minima > 0 at t <= t_hi,
        # plus non-clause bars at bracket instants
        nonbinding = [kk for kk in CK if kk not in BINDING]
        f4 = None
        for r in grids['g5']['window_rows']:
            if r['t'] <= T_HI + 1e-12:
                for kk in nonbinding:
                    if not r['clause_minima'][kk] > 0.0:
                        f4 = {'t': r['t'], 'clause': kk,
                              'g5_min': r['clause_minima'][kk]}
                        break
            if f4:
                break
        bars_ok = True
        bars_detail = {}
        for tstr, b in grids['g5']['nonclause_bars'].items():
            ok = bool(b['mom_worst'] <= 1e-10
                      and b['flare_min'] > 0.0
                      and b['domain_R_min'] > 0.0
                      and b['domain_exp2Phi_min'] > 0.0)
            bd = dict(b)
            bd['pass'] = ok
            bars_detail[tstr] = bd
            bars_ok = bars_ok and ok
        res['nonclause_bars_g5'] = bars_detail
        if f4 is None and not bars_ok:
            bad = [s for s, b in bars_detail.items()
                   if not b['pass']]
            f4 = {'nonclause_bar_failure_at_t': bad}
        cert['CERT-4'] = {'pass': bool(f4 is None and bars_ok),
                          'failing': f4,
                          'bars_pass': bool(bars_ok)}
        res['cert'] = cert
        # window worsts
        res['window_worsts'] = {
            kk: {'max_abs_d34': max(abs(e[kk]['d34'])
                                    for e in table),
                 'max_abs_d45': max(abs(e[kk]['d45'])
                                    for e in table),
                 'max_r': max(e[kk]['r'] for e in table)}
            for kk in BINDING}
        bad_cert = [k for k, v in cert.items()
                    if not v['pass']]
        if bad_cert:
            verdict = 'FAILS-(a)'
            failing = bad_cert[0] + ': ' + json.dumps(
                cert[bad_cert[0]]['failing'])
        else:
            verdict = ('SURVIVES (INTACT vs IN RESTATED '
                       'WORDING reserved to the gate, sec.5)')
            failing = None
    res['md5_protected_after'] = md5s()
    res['controls']['CTRL-4'] = bool(
        res['md5_protected_after']
        == res['md5_protected_before'])
    if not res['controls']['CTRL-4'] and verdict is not None \
            and not verdict.startswith('FAILS'):
        verdict, failing = 'FAILS-(a)', 'CTRL-4'
    res['verdict_form'] = verdict
    res['failing_condition'] = failing
    res['walls_s']['evaluation_stage'] = time.time() - t0
    json.dump(res, open(G31 + 'g31_results.json', 'w'),
              indent=1)
    print('VERDICT', verdict, '| failing:', failing,
          flush=True)
    print('WROTE g31_results.json', flush=True)


if __name__ == '__main__':
    stage = sys.argv[1]
    if stage == 'controls':
        stage_controls()
    elif stage in GRIDS:
        stage_grid(stage)
    elif stage == 'evaluation':
        stage_evaluation()
    else:
        raise SystemExit('unknown stage ' + stage)
