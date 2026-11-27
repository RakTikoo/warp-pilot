#!/usr/bin/env python3
"""
p418_search.py -- Phase 418 search driver: THE
CARRYING-AWARE HUNT. Registration:
p418_registration.md (SS5's pattern; SS4's
pricing, box, feasibility; SS6's confirmations
run inside the flow at the registered points).

Resumable: screens append to
results/p418_screens.jsonl; incumbents and
stage marks live in results/p418_state.json.
A stage marked complete is skipped on re-run;
a killed stage resumes from its incumbent of
record (the 398/405/406/414 precedent).
"""
import json
import os
import sys
import time

import numpy as np
from scipy.optimize import minimize

WP = os.environ.get('P418_WP', '/home/hatch/workspace/warp-pilot')
sys.path.insert(0, f'{WP}/phase418/work')

import p418_lib as L  # noqa: E402

RES = f'{WP}/phase418/results'
SCREENS = f'{RES}/p418_screens.jsonl'
STATE = f'{RES}/p418_state.json'
CONF = f'{RES}/p418_confirmation.json'

CAP_TOTAL = 2200
STAGE_CAPS = {'S': 12, 'T': 240, 'A': 800, 'B': 350,
              'G': 250, 'R': 300}
CRIT = L.CRIT
P2 = 2.0 * CRIT


class CapHit(Exception):
    pass


def n_screens():
    if not os.path.exists(SCREENS):
        return 0
    with open(SCREENS) as f:
        return sum(1 for _ in f)


def load_state():
    if os.path.exists(STATE):
        return json.load(open(STATE))
    return {'stages_done': [], 'incumbents': {},
            'crit_incumbent': None, 'crit_best_joint': None,
            'rejects': 0, 'penalised_evals': 0,
            'stage_counts': {}}


ST = load_state()
if os.path.exists(SCREENS):
    cnt = {}
    with open(SCREENS) as f:
        for line in f:
            stg = json.loads(line)['stage']
            cnt[stg] = cnt.get(stg, 0) + 1
    ST['stage_counts'] = cnt


def save_state():
    with open(STATE, 'w') as f:
        json.dump(ST, f, indent=1)


def cfg_of(base, vS_scaled, K_S):
    return {'muN': float(base['muN']), 'muM': float(base['muM']),
            'K_B': int(base['K']),
            'vN': [float(x) for x in base['vN']],
            'vM': [float(x) for x in base['vM']],
            'K_S': int(K_S),
            'vS_scaled': [float(x) for x in vS_scaled]}


def base_of(cfg):
    return L.base_dict(cfg['muN'], cfg['muM'], cfg['K_B'],
                       cfg['vN'], cfg['vM'])


def screen(stage, base, vS_in, K_S, P, tag=''):
    """One stored SET read (SS4/SS5). vS_in is a
    direction (or the scaled vector); it is
    renormalised to peak P per screen. P = 0
    means the static read (vS identically 0)."""
    total = n_screens()
    if total >= CAP_TOTAL:
        raise CapHit('total cap')
    if ST['stage_counts'].get(stage, 0) >= STAGE_CAPS[stage]:
        raise CapHit(f'stage cap {stage}')
    if P == 0.0:
        vS_s = np.zeros(K_S, dtype=L.DTYPE)
    else:
        vS_s, _raw = L.scale_to_peak(
            np.asarray(vS_in, dtype=L.DTYPE), K_S, P)
    t0 = time.time()
    s, _aux = L.set_read(base, vS_s, K_S)
    joint = L.joint_of_read(s)
    feas = bool(s['rho']['min'] > 0.0)
    pen = L.pen418(base['vN'], base['vM'], vS_s)
    score = float(joint - pen) if feas else None
    pk, pkr = (0.0, None) if P == 0.0 else L.peak_radius(vS_s, K_S)
    rec = {
        'id': total, 'stage': stage, 'tag': tag,
        'target_peak': float(P), 'peak': pk,
        'peak_radius': pkr,
        'K_B': int(base['K']), 'K_S': int(K_S),
        'muN': float(base['muN']), 'muM': float(base['muM']),
        'vN': [float(x) for x in base['vN']],
        'vM': [float(x) for x in base['vM']],
        'vS_scaled': [float(x) for x in vS_s],
        'joint': float(joint),
        'binding': ('NEC' if s['nec']['min'] <= s['dec']['min']
                    else 'DEC'),
        'nec_min': s['nec']['min'], 'dec_min': s['dec']['min'],
        'wec_min': s['wec']['min'], 'sec_min': s['sec']['min'],
        'rho_min': s['rho']['min'],
        'nec_argmin_r': s['nec_argmin_r'],
        'dec_argmin_r': s['dec_argmin_r'],
        'typeI_fraction': s['typeI_fraction'],
        'feasible': feas,
        'rejected_reason': (None if feas else 'C1: rho_min <= 0'),
        'pen418': float(pen), 'score': score,
        't_s': time.time() - t0,
    }
    with open(SCREENS, 'a') as f:
        f.write(json.dumps(rec) + '\n')
    ST['stage_counts'][stage] = \
        ST['stage_counts'].get(stage, 0) + 1
    if feas and P > 0.0:
        key = f'{stage}|P{P:.10f}'
        cur = ST['incumbents'].get(key)
        if cur is None or score > cur['score']:
            ST['incumbents'][key] = {
                'screen_id': total, 'score': score,
                'joint': float(joint), 'stage': stage,
                'config': cfg_of(base, vS_s, K_S)}
        if abs(P - CRIT) < 1e-12:
            ci = ST['crit_incumbent']
            if ci is None or score > ci['score']:
                ST['crit_incumbent'] = {
                    'screen_id': total, 'score': score,
                    'joint': float(joint), 'stage': stage,
                    'config': cfg_of(base, vS_s, K_S)}
            bj = ST['crit_best_joint']
            if bj is None or joint > bj['joint']:
                ST['crit_best_joint'] = {
                    'screen_id': total, 'joint': float(joint),
                    'score': score, 'stage': stage,
                    'config': cfg_of(base, vS_s, K_S)}
        save_state()
    return rec


def incumbent(stage, P):
    return ST['incumbents'].get(f'{stage}|P{P:.10f}')


def feasible_base(base):
    """SS4's pre-read feasibility: guards + the
    398 floors. Failing candidates are rejected
    without a read (tallied)."""
    if not L.guards_ok(base['muN'], base['muM'],
                       base['vN'], base['vM']):
        ST['rejects'] += 1
        save_state()
        return False
    if not L.positivity_ok(base['muN'], base['muM'],
                           base['vN'], base['vM'], base['K']):
        ST['rejects'] += 1
        save_state()
        return False
    return True


# ------------------------------------------------ blocks
def cd_shape(stage, base, v0, K_S, P, max_screens=None):
    """412's cd_walks form, base held: greedy
    first-improvement CD on the scaled shape."""
    box = L.box_for_peak(P)
    steps = L.cd_steps(P)
    start_n = n_screens()
    inc = screen(stage, base, v0, K_S, P, tag='seed')
    cur_vec = np.array(inc['vS_scaled'], dtype=L.DTYPE)
    cur_score = inc['score'] if inc['feasible'] else -np.inf
    improved_any = True
    while improved_any:
        improved_any = False
        for step in steps:
            for i in range(K_S):
                for sgn in (1.0, -1.0):
                    if (max_screens is not None
                            and n_screens() - start_n
                            >= max_screens):
                        return incumbent(stage, P)
                    cand = cur_vec.copy()
                    cand[i] = np.clip(cand[i] + sgn * step,
                                      -box, box)
                    if cand[i] == cur_vec[i]:
                        continue
                    try:
                        rec = screen(stage, base, cand, K_S, P,
                                     tag=f'cd{i}'
                                         f'{"+" if sgn > 0 else "-"}')
                    except CapHit:
                        return incumbent(stage, P)
                    if rec['feasible'] and rec['score'] > cur_score:
                        cur_vec = np.array(rec['vS_scaled'],
                                           dtype=L.DTYPE)
                        cur_score = rec['score']
                        improved_any = True
                        break
    return incumbent(stage, P)


def nm_shape(stage, base, v0, K_S, P, maxfev=120):
    box = L.box_for_peak(P)
    x0 = np.asarray(v0, dtype=L.DTYPE)

    def neg_score(x):
        x = np.clip(np.asarray(x, dtype=L.DTYPE), -box, box)
        rec = screen(stage, base, x, K_S, P, tag='nm')
        return -(rec['score'] if rec['feasible'] else -1.0)

    try:
        minimize(neg_score, x0, method='Nelder-Mead',
                 options={'maxfev': maxfev,
                          'xatol': 1e-3 * L.step_scale(P),
                          'fatol': 1e-9})
    except CapHit:
        pass
    return incumbent(stage, P)


def shape_block(stage, base, v0, K_S, P):
    """405's stage pattern: CD, NM polish, CD
    again (from the incumbent each time)."""
    cd_shape(stage, base, v0, K_S, P)
    inc = incumbent(stage, P)
    if inc is not None:
        nm_shape(stage, base, inc['config']['vS_scaled'],
                 K_S, P)
        inc = incumbent(stage, P)
        if inc is not None:
            cd_shape(stage, base, inc['config']['vS_scaled'],
                     K_S, P)
    return incumbent(stage, P)


def cd_base(stage, base0, vS_scaled, K_S, P,
            mu_levels=(0.04, 0.016, 0.006),
            corr_levels=(0.03, 0.012, 0.005),
            max_screens=None):
    """SS5's BASE block: CD on (muN, muM)
    (multiplicative) then on (vN, vM) (additive),
    the shape held. Greedy first-improvement,
    412's CD form. Candidates failing guards/
    floors are skipped without a read."""
    cur = L.base_dict(base0['muN'], base0['muM'], base0['K'],
                      base0['vN'], base0['vM'])
    start_n = n_screens()
    inc = screen(stage, cur, vS_scaled, K_S, P, tag='base-seed')
    cur_score = inc['score'] if inc['feasible'] else -np.inf

    def trial(cand_base, tag):
        nonlocal cur, cur_score
        if (max_screens is not None
                and n_screens() - start_n >= max_screens):
            raise CapHit('block budget')
        if not feasible_base(cand_base):
            return False
        try:
            rec = screen(stage, cand_base, vS_scaled, K_S, P,
                         tag=tag)
        except CapHit:
            raise
        if rec['feasible'] and rec['score'] > cur_score:
            cur = cand_base
            cur_score = rec['score']
            return True
        return False

    improved_any = True
    while improved_any:
        improved_any = False
        for d in mu_levels:
            for which in ('muN', 'muM'):
                for sgn in (1.0, -1.0):
                    cand = L.base_dict(cur['muN'], cur['muM'],
                                       cur['K'], cur['vN'],
                                       cur['vM'])
                    cand[which] = cur[which] * (1.0 + sgn * d)
                    try:
                        if trial(cand, f'mu{which}'
                                       f'{"+" if sgn > 0 else "-"}'):
                            improved_any = True
                            break
                    except CapHit:
                        return incumbent(stage, P)
        for step in corr_levels:
            for sect in ('vN', 'vM'):
                for i in range(cur['K']):
                    for sgn in (1.0, -1.0):
                        cand = L.base_dict(cur['muN'], cur['muM'],
                                           cur['K'], cur['vN'],
                                           cur['vM'])
                        cand[sect] = cand[sect].copy()
                        cand[sect][i] += sgn * step
                        try:
                            if trial(cand,
                                     f'{sect}{i}'
                                     f'{"+" if sgn > 0 else "-"}'):
                                improved_any = True
                                break
                        except CapHit:
                            return incumbent(stage, P)
    return incumbent(stage, P)


def nm_joint(stage, base0, v0, K_S, P, maxfev=200):
    """Joint NM polish on the full vector
    (SS5). Infeasible-region evals return a
    penalised score without a read (tallied)."""
    KB = int(base0['K'])
    box = L.box_for_peak(P)
    x0 = np.concatenate([
        [base0['muN'], base0['muM']],
        np.asarray(base0['vN'], dtype=L.DTYPE),
        np.asarray(base0['vM'], dtype=L.DTYPE),
        np.asarray(v0, dtype=L.DTYPE)])

    def unpack(x):
        muN = float(np.clip(x[0], *L.MU_BOUNDS[:2]))
        muM = float(np.clip(x[1], *L.MU_BOUNDS[2:]))
        vN = np.clip(np.asarray(x[2:2 + KB], dtype=L.DTYPE),
                     -L.VN_BOUND, L.VN_BOUND)
        vM = np.clip(np.asarray(x[2 + KB:2 + 2 * KB],
                                dtype=L.DTYPE),
                     -L.VM_BOUND, L.VM_BOUND)
        vS = np.clip(np.asarray(x[2 + 2 * KB:], dtype=L.DTYPE),
                     -box, box)
        return L.base_dict(muN, muM, KB, vN, vM), vS

    def neg_score(x):
        base, vS = unpack(np.asarray(x, dtype=L.DTYPE))
        if not feasible_base(base):
            ST['penalised_evals'] += 1
            save_state()
            return 1.0
        rec = screen(stage, base, vS, K_S, P, tag='nmj')
        return -(rec['score'] if rec['feasible'] else -1.0)

    try:
        minimize(neg_score, x0, method='Nelder-Mead',
                 options={'maxfev': maxfev, 'xatol': 1e-3,
                          'fatol': 1e-9})
    except CapHit:
        pass
    return incumbent(stage, P)


# ------------------------------------------------ confirmation (SS6)
def confirm_point(cfg, label, do_polish=True):
    """SS6's confirmation of a stored carried
    point. Not a screen (not in the jsonl, not
    counted in the caps, as in 412/414)."""
    base = base_of(cfg)
    vS = np.array(cfg['vS_scaled'], dtype=L.DTYPE)
    K_S = int(cfg['K_S'])
    s, aux = L.set_read(base, vS, K_S)
    joint = L.joint_of_read(s)
    wn, wnf = L.worst_null_at(base, vS, K_S,
                              np.array(s['nec_argmin_point']))
    phys = L.phys_row(base, vS, K_S, s['nec_argmin_r'])
    pol = None
    if do_polish:
        pol = L.adversary_polish(base, vS, K_S, aux)
    s0, _ = L.set_read(base, None, K_S)
    static_joint = L.joint_of_read(s0)
    out = {'label': label, 'config': cfg,
           'joint': float(joint),
           'nec_min': s['nec']['min'],
           'dec_min': s['dec']['min'],
           'wec_min': s['wec']['min'],
           'sec_min': s['sec']['min'],
           'rho_min': s['rho']['min'],
           'nec_argmin_r': s['nec_argmin_r'],
           'dec_argmin_r': s['dec_argmin_r'],
           'typeI_fraction': s['typeI_fraction'],
           'typeI_nec_min': s['typeI_nec_min'],
           'worst_null_at_nec_argmin': wn,
           'worst_null_fib': wnf,
           'peak': phys['peak_abs_beta_S'],
           'peak_radius': L.peak_radius(vS, K_S)[1],
           'local_at_nec_argmin': phys['local_at_nec_argmin'],
           'S_range': phys['S_range'],
           'adversary_polish': (
               None if pol is None else {
                   'source': pol['source'], 'r': pol['r'],
                   'in_region_worst_nec_SAMPLER-M':
                       pol['in_region_worst_nec_SAMPLER-M'],
                   'typeI': pol['typeI']}),
           'base_static_joint': float(static_joint),
           'base_static_sec_min': s0['sec']['min'],
           'spend_vs_own_base': float(static_joint - joint)}
    confs = {}
    if os.path.exists(CONF):
        confs = json.load(open(CONF))
    confs[label] = out
    with open(CONF, 'w') as f:
        json.dump(confs, f, indent=1)
    return out


# ------------------------------------------------ stages
def stage_S():
    if 'S' in ST['stages_done']:
        return
    try:
        screen('S', L.BASE400, L.G50_KNOTS, 9, CRIT, tag='S-A')
        screen('S', L.BASEB1, L.B1T1_KNOTS, 17, CRIT,
               tag='S-B')
        screen('S', L.BASEB1, L.G50_KNOTS, 9, CRIT, tag='S-C')
        screen('S', L.BASE400, L.B1T1_KNOTS, 17, CRIT,
               tag='S-D')
        screen('S', L.BASE400_K9, L.G50_KNOTS, 9, CRIT,
               tag='S-E')
    except CapHit:
        pass
    ST['stages_done'].append('S')
    save_state()


def stage_T():
    if 'T' in ST['stages_done']:
        return
    rows = {}
    for t in (0.0, 0.2, 0.4, 0.6, 0.8, 1.0):
        bt = L.base_dict(
            (1 - t) * L.BASE400_K9['muN'] + t * L.BASEB1['muN'],
            (1 - t) * L.BASE400_K9['muM'] + t * L.BASEB1['muM'],
            9,
            (1 - t) * L.BASE400_K9['vN'] + t * L.BASEB1['vN'],
            (1 - t) * L.BASE400_K9['vM'] + t * L.BASEB1['vM'])
        try:
            st_rec = screen('T', bt, np.zeros(9), 9, 0.0,
                            tag=f't{t}-static')
            before = n_screens()
            cd_shape('T', bt, L.G50_KNOTS, 9, CRIT,
                     max_screens=37)
            used = n_screens() - before
            tb = best_screen_where(
                lambda r, bt=bt: r['stage'] == 'T'
                and r['target_peak'] > 0
                and abs(r['muN'] - bt['muN']) < 1e-12
                and abs(r['muM'] - bt['muM']) < 1e-12)
            rows[str(t)] = {
                'base': {'muN': bt['muN'], 'muM': bt['muM']},
                'static_joint': st_rec['joint'],
                'static_sec_min': st_rec['sec_min'],
                'carried_screens': used,
                'carried_best_joint': (
                    None if tb is None else tb['joint']),
                'carried_best_score': (
                    None if tb is None else tb['score']),
                'carried_best_screen': (
                    None if tb is None else tb['id']),
                'spend': (None if tb is None else
                          st_rec['joint'] - tb['joint'])}
        except CapHit:
            rows[str(t)] = {'cap_hit': True}
            break
    ST['transect'] = rows
    ST['stages_done'].append('T')
    save_state()


def best_screen_where(pred):
    best = None
    if os.path.exists(SCREENS):
        with open(SCREENS) as f:
            for line in f:
                r = json.loads(line)
                if pred(r) and r['feasible']:
                    if best is None or r['score'] > best['score']:
                        best = r
    return best


def cfg_from_screen(r):
    return {'muN': r['muN'], 'muM': r['muM'], 'K_B': r['K_B'],
            'vN': r['vN'], 'vM': r['vM'], 'K_S': r['K_S'],
            'vS_scaled': r['vS_scaled']}


def stage_A():
    if 'A' in ST['stages_done']:
        return
    # candidate starts (SS5): S-E, the best transect
    # incumbent, the B1-side best of S-B/S-C
    cand = []
    r = best_screen_where(lambda r: r['tag'] == 'S-E')
    if r is not None:
        cand.append(('S-E', r))
    r = best_screen_where(lambda r: r['stage'] == 'T'
                          and r['target_peak'] > 0)
    if r is not None:
        cand.append(('T-best', r))
    r = best_screen_where(lambda r: r['tag'] in ('S-B', 'S-C'))
    if r is not None:
        cand.append(('B1-side', r))
    cand.sort(key=lambda kv: -kv[1]['score'])
    starts = cand[:2]
    ST['A_starts'] = [{'name': n, 'screen_id': r['id'],
                       'score': r['score'], 'joint': r['joint']}
                      for n, r in starts]
    save_state()
    nm1_moved = None
    for si, (name, r) in enumerate(starts):
        cfg = cfg_from_screen(r)
        base = base_of(cfg)
        vS = np.array(cfg['vS_scaled'], dtype=L.DTYPE)
        K_S = 9
        if cfg['K_S'] != 9:
            vS = L.shape_at_knots(vS, cfg['K_S'], 9)
        prev_score = None
        for rnd in range(4):
            try:
                shape_block('A', base, vS, K_S, CRIT)
                inc = incumbent('A', CRIT)
                if inc is not None:
                    base = base_of(inc['config'])
                    vS = np.array(inc['config']['vS_scaled'],
                                  dtype=L.DTYPE)
                cd_base('A', base, vS, K_S, CRIT)
                inc = incumbent('A', CRIT)
                if inc is not None:
                    base = base_of(inc['config'])
                    vS = np.array(inc['config']['vS_scaled'],
                                  dtype=L.DTYPE)
            except CapHit:
                break
            inc = incumbent('A', CRIT)
            sc = inc['score'] if inc is not None else None
            if (prev_score is not None and sc is not None
                    and sc - prev_score < 1e-9):
                prev_score = sc
                break
            prev_score = sc
            if si == 0 and rnd == 0:
                before = (inc['screen_id'] if inc else None)
                try:
                    nm_joint('A', base, vS, K_S, CRIT)
                except CapHit:
                    pass
                inc2 = incumbent('A', CRIT)
                nm1_moved = bool(
                    inc2 is not None
                    and inc2['screen_id'] != before)
                inc = inc2
                if inc is not None:
                    base = base_of(inc['config'])
                    vS = np.array(inc['config']['vS_scaled'],
                                  dtype=L.DTYPE)
    # second joint NM from the overall incumbent if
    # the first moved it (SS5)
    inc = incumbent('A', CRIT)
    if nm1_moved and inc is not None:
        try:
            nm_joint('A', base_of(inc['config']),
                     np.array(inc['config']['vS_scaled'],
                              dtype=L.DTYPE), 9, CRIT)
        except CapHit:
            pass
    ST['A_nm1_moved'] = nm1_moved
    ST['stages_done'].append('A')
    save_state()


def stage_B():
    if 'B' in ST['stages_done']:
        return
    rA = best_screen_where(lambda r: r['tag'] == 'S-A')
    incA = ST['crit_incumbent']
    start_cfg = None
    # score the Stage-A incumbent resampled to K_B=17
    # as a candidate start (a representation move,
    # recorded as a Stage-B screen)
    try:
        if incA is not None:
            cfgA = incA['config']
            b17 = L.base_at_K(base_of(cfgA), 17)
            rec = screen('B', b17, cfgA['vS_scaled'],
                         cfgA['K_S'], CRIT, tag='A-inc-at-17')
            if (rA is None or (rec['feasible']
                               and rec['score'] > rA['score'])):
                start_cfg = cfg_from_screen(rec)
        if start_cfg is None and rA is not None:
            start_cfg = cfg_from_screen(rA)
    except CapHit:
        start_cfg = None
    if start_cfg is not None:
        base = base_of(start_cfg)
        vS = np.array(start_cfg['vS_scaled'], dtype=L.DTYPE)
        K_S = int(start_cfg['K_S'])
        if K_S != 9:
            vS = L.shape_at_knots(vS, K_S, 9)
            K_S = 9
        ST['B_start'] = {'screen_score': start_cfg.get('score'),
                         'K_B': 17}
        try:
            cd_base('B', base, vS, K_S, CRIT,
                    corr_levels=(0.012, 0.005))
            inc = incumbent('B', CRIT)
            if inc is not None:
                base = base_of(inc['config'])
                vS = np.array(inc['config']['vS_scaled'],
                              dtype=L.DTYPE)
            cd_shape('B', base, vS, K_S, CRIT)
            inc = incumbent('B', CRIT)
            if inc is not None:
                base = base_of(inc['config'])
                vS = np.array(inc['config']['vS_scaled'],
                              dtype=L.DTYPE)
            nm_joint('B', base, vS, K_S, CRIT)
        except CapHit:
            pass
    ST['stages_done'].append('B')
    save_state()


def stage_G(confirmed_joint):
    if 'G' in ST['stages_done']:
        return
    triggered = bool(confirmed_joint <= L.J1_400)
    ST['G_triggered'] = triggered
    ST['G_trigger_joint'] = confirmed_joint
    save_state()
    if not triggered:
        ST['stages_done'].append('G')
        save_state()
        return
    inc = ST['crit_incumbent']
    if inc is None:
        ST['stages_done'].append('G')
        save_state()
        return
    cfg = inc['config']
    base = base_of(cfg)
    vS17a = L.shape_at_knots(cfg['vS_scaled'], cfg['K_S'], 17)
    vS17b = L.shape_at_knots(L.G50_KNOTS, 9, 17)
    try:
        screen('G', base, vS17a, 17, CRIT, tag='warm-inc')
        screen('G', base, vS17b, 17, CRIT, tag='warm-g50')
        incG = incumbent('G', CRIT)
        v0 = (incG['config']['vS_scaled'] if incG is not None
              else vS17a)
        cd_shape('G', base, v0, 17, CRIT)
        incG = incumbent('G', CRIT)
        if incG is not None:
            nm_shape('G', base, incG['config']['vS_scaled'],
                     17, CRIT)
            incG = incumbent('G', CRIT)
            if incG is not None:
                # short BASE block at K_S = 17 (<= 60
                # screens by the stage pattern's
                # remaining budget discipline)
                cd_base('G', base_of(incG['config']),
                        np.array(incG['config']['vS_scaled'],
                                 dtype=L.DTYPE), 17, CRIT,
                        corr_levels=(0.005,), max_screens=60)
    except CapHit:
        pass
    ST['stages_done'].append('G')
    save_state()


def stage_R(best_cfg):
    if 'R' in ST['stages_done']:
        return
    base = base_of(best_cfg)
    try:
        for sd, tg in ((best_cfg['vS_scaled'], 'inc-shape'),
                       (L.G50_KNOTS, 'g50'),
                       (L.h2_seed(9), 'h2')):
            screen('R', base, np.array(sd, dtype=L.DTYPE), 9,
                   P2, tag=tg)
        inc = incumbent('R', P2)
        if inc is not None:
            cd_shape('R', base, inc['config']['vS_scaled'],
                     9, P2)
            inc = incumbent('R', P2)
            if inc is not None:
                nm_shape('R', base,
                         inc['config']['vS_scaled'], 9, P2)
                inc = incumbent('R', P2)
                if inc is not None:
                    cd_shape('R', base,
                             inc['config']['vS_scaled'], 9, P2)
        inc = incumbent('R', P2)
        if inc is not None and inc['joint'] < 0.0:
            # the K_S = 17 gate at 2x (412's form)
            v17a = L.shape_at_knots(inc['config']['vS_scaled'],
                                    9, 17)
            v17b = L.shape_at_knots(L.G50_KNOTS, 9, 17)
            screen('R', base, v17a, 17, P2, tag='k17-warm-inc')
            screen('R', base, v17b, 17, P2, tag='k17-warm-g50')
            cd_shape('R', base, v17a, 17, P2)
            inc17 = incumbent('R', P2)
            if inc17 is not None:
                nm_shape('R', base,
                         inc17['config']['vS_scaled'], 17, P2)
    except CapHit:
        pass
    ST['stages_done'].append('R')
    save_state()


def main():
    t00 = time.time()
    stage_S()
    print('S done', n_screens(), flush=True)
    stage_T()
    print('T done', n_screens(), flush=True)
    stage_A()
    print('A done', n_screens(), flush=True)
    stage_B()
    print('B done', n_screens(), flush=True)
    # SS6 confirmation #1: the criterion score-incumbent
    inc = ST['crit_incumbent']
    conf1 = None
    confirmed_id = None
    if inc is not None:
        conf1 = confirm_point(inc['config'], 'criterion_best',
                              do_polish=True)
        confirmed_id = inc['screen_id']
        print('CONF1 joint', conf1['joint'], flush=True)
        stage_G(conf1['joint'])
    else:
        ST['G_triggered'] = False
        ST['stages_done'].append('G')
        save_state()
    print('G done', n_screens(), flush=True)
    # if Stage G produced a better criterion incumbent,
    # confirm the new best before Stage R (SS6)
    inc = ST['crit_incumbent']
    best_cfg = inc['config'] if inc is not None else None
    best_joint = conf1['joint'] if conf1 is not None else None
    if inc is not None and inc['screen_id'] != confirmed_id:
        conf2 = confirm_point(inc['config'], 'criterion_best',
                              do_polish=True)
        best_joint = conf2['joint']
        print('CONF2 joint', best_joint, flush=True)
    if best_cfg is not None:
        stage_R(best_cfg)
    print('R done', n_screens(), flush=True)
    incR = incumbent('R', P2)
    if incR is not None:
        confR = confirm_point(
            incR['config'], 'twice_best',
            do_polish=bool(incR['joint'] >= 0.0))
        print('CONFR joint', confR['joint'], flush=True)
    ST['total_screens'] = n_screens()
    ST['wall_s'] = time.time() - t00
    ST['cost_bounded'] = bool(n_screens() >= CAP_TOTAL)
    save_state()
    print('ALL DONE', n_screens(), 'screens', flush=True)


if __name__ == '__main__':
    main()
