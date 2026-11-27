#!/usr/bin/env python3
"""
p412_search.py -- Phase 412 ladder search
(registration SS5). One process climbs the
whole ladder with resume semantics: append-only
screens (results/p412_screens.jsonl), state in
results/p412_state.json (per-rung records +
incumbents), rung summaries in
results/p412_rungs.json. Incumbent semantics:
best score (joint - PEN400) among C1-feasible
screens at the rung; the pure joint recorded
for every screen. Rerunning skips rungs the
state marks complete.
"""
import json
import os
import sys
import time

import numpy as np
from scipy.optimize import minimize

WP = '/home/hatch/workspace/warp-pilot'
sys.path.insert(0, f'{WP}/phase412/work')
import p412_lib as L  # noqa: E402

RES = f'{WP}/phase412/results'
SCREENS = f'{RES}/p412_screens.jsonl'
STATE = f'{RES}/p412_state.json'
RUNGS_OUT = f'{RES}/p412_rungs.json'
CAP_TOTAL = 2400
CAP_RUNG_K9 = 280
CAP_ARM_K17 = 200


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
    return {'rungs': {}, 'incumbents': {}}


def save_state(st):
    with open(STATE, 'w') as f:
        json.dump(st, f, indent=1)


STATE_OBJ = load_state()
STAGE_COUNT = {}
if os.path.exists(SCREENS):
    with open(SCREENS) as f:
        for line in f:
            stg = json.loads(line)['stage']
            STAGE_COUNT[stg] = STAGE_COUNT.get(stg, 0) + 1


def stage_cap(stage):
    return CAP_ARM_K17 if stage.endswith('K17') else CAP_RUNG_K9


def screen(stage, K, vS_in, target_peak, tag=''):
    total = n_screens()
    if total >= CAP_TOTAL:
        raise CapHit('total cap')
    if STAGE_COUNT.get(stage, 0) >= stage_cap(stage):
        raise CapHit(f'stage cap {stage}')
    vS_s, _raw = L.scale_to_peak(
        np.asarray(vS_in, dtype=L.DTYPE), K, target_peak)
    t0 = time.time()
    s, _aux = L.set_read(vS_s, K)
    phys = L.phys_row(vS_s, K, s['nec_argmin_r'])
    joint = L.joint_of_read(s)
    feas = bool(s['rho']['min'] > 0.0)
    pen = L.pen400(vS_s)
    score = float(joint - pen) if feas else None
    rec = {
        'id': total, 'stage': stage, 'K': K, 'tag': tag,
        'target_peak': float(target_peak),
        'peak': phys['peak_abs_beta_S'],
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
        'pen400': float(pen), 'score': score,
        'local_at_nec_argmin': phys['local_at_nec_argmin'],
        't_s': time.time() - t0,
    }
    with open(SCREENS, 'a') as f:
        f.write(json.dumps(rec) + '\n')
    STAGE_COUNT[stage] = STAGE_COUNT.get(stage, 0) + 1
    if feas:
        key = f'{stage}|K{K}|{target_peak:.10f}'
        cur = STATE_OBJ['incumbents'].get(key)
        if cur is None or score > cur['score']:
            STATE_OBJ['incumbents'][key] = {
                'screen_id': total, 'score': score,
                'joint': float(joint),
                'vS_scaled': rec['vS_scaled'], 'K': K,
                'target_peak': float(target_peak),
                'stage': stage}
            save_state(STATE_OBJ)
    return rec


def incumbent(stage, K, target):
    return STATE_OBJ['incumbents'].get(
        f'{stage}|K{K}|{target:.10f}')


def best_joint_screen(stage, K, target):
    """Max pure joint among the stage's feasible
    stored screens (SS5's alongside record)."""
    best = None
    if os.path.exists(SCREENS):
        with open(SCREENS) as f:
            for line in f:
                r = json.loads(line)
                if (r['stage'] == stage and r['K'] == K
                        and abs(r['target_peak'] - target) < 1e-9
                        and r['feasible']):
                    if best is None or r['joint'] > best['joint']:
                        best = r
    return best


def cd_walks(stage, K, target, v0):
    box = L.box_for_peak(target)
    steps = L.cd_steps(target)
    inc = screen(stage, K, v0, target, tag='seed')
    cur_vec = np.array(inc['vS_scaled'], dtype=L.DTYPE)
    cur_score = inc['score'] if inc['feasible'] else -np.inf
    improved_any = True
    while improved_any:
        improved_any = False
        for step in steps:
            for i in range(K):
                for sgn in (1.0, -1.0):
                    cand = cur_vec.copy()
                    cand[i] = np.clip(cand[i] + sgn * step,
                                      -box, box)
                    if cand[i] == cur_vec[i]:
                        continue
                    try:
                        rec = screen(stage, K, cand, target,
                                     tag=f'cd{i}'
                                         f'{"+" if sgn > 0 else "-"}')
                    except CapHit:
                        return incumbent(stage, K, target)
                    if rec['feasible'] and rec['score'] > cur_score:
                        cur_vec = np.array(rec['vS_scaled'],
                                           dtype=L.DTYPE)
                        cur_score = rec['score']
                        improved_any = True
                        break
    return incumbent(stage, K, target)


def nm_polish(stage, K, target, v0, maxfev=120):
    box = L.box_for_peak(target)
    x0 = np.asarray(v0, dtype=L.DTYPE)

    def neg_score(x):
        x = np.clip(np.asarray(x, dtype=L.DTYPE), -box, box)
        rec = screen(stage, K, x, target, tag='nm')
        return -(rec['score'] if rec['feasible'] else -1.0)

    try:
        minimize(neg_score, x0, method='Nelder-Mead',
                 options={'maxfev': maxfev,
                          'xatol': 1e-3 * L.step_scale(target),
                          'fatol': 1e-9})
    except CapHit:
        pass
    return incumbent(stage, K, target)


def search_at(stage, K, target, seeds):
    """405's stage pattern: seed screens, CD from
    the best seed, NM polish, CD again."""
    try:
        for sd in seeds:
            screen(stage, K, sd, target, tag='seed')
        inc = incumbent(stage, K, target)
        if inc is None:
            return None
        cd_walks(stage, K, target, inc['vS_scaled'])
        inc = incumbent(stage, K, target)
        if inc is not None:
            nm_polish(stage, K, target, inc['vS_scaled'])
            inc = incumbent(stage, K, target)
            if inc is not None:
                cd_walks(stage, K, target, inc['vS_scaled'])
    except CapHit:
        pass
    return incumbent(stage, K, target)


def confirm(stage, K, inc, do_polish):
    """SS5 confirmation of a rung winner at its
    frozen scaled vector."""
    vS = np.array(inc['vS_scaled'], dtype=L.DTYPE)
    s, aux = L.set_read(vS, K)
    joint = L.joint_of_read(s)
    pk, pk_r = L.peak_radius(vS, K)
    pt = np.array(s['nec_argmin_point'], dtype=L.DTYPE)
    wn, wn_fib = L.worst_null_at(vS, K, pt)
    phys = L.phys_row(vS, K, s['nec_argmin_r'])
    out = {
        'screen_id': inc['screen_id'],
        'joint': float(joint),
        'joint_diff_vs_screen': float(joint - inc['joint']),
        'nec_min': s['nec']['min'], 'dec_min': s['dec']['min'],
        'wec_min': s['wec']['min'], 'sec_min': s['sec']['min'],
        'rho_min': s['rho']['min'],
        'nec_argmin_r': s['nec_argmin_r'],
        'dec_argmin_r': s['dec_argmin_r'],
        'typeI_fraction': s['typeI_fraction'],
        'typeI_nec_min': s['typeI_nec_min'],
        'worst_null_at_nec_argmin': wn,
        'worst_null_fib': wn_fib,
        'peak': pk, 'peak_radius': pk_r,
        'local_at_nec_argmin': phys['local_at_nec_argmin'],
        'S_range': phys['S_range'],
        'adversary_polish': None,
    }
    if do_polish:
        pol = L.adversary_polish(vS, K, aux)
        if pol is not None:
            out['adversary_polish'] = {
                'source': pol['source'], 'r': pol['r'],
                'in_region_worst_nec_SAMPLER-M':
                    pol['in_region_worst_nec_SAMPLER-M'],
                'typeI': pol['typeI']}
    return out


def run_rung(mult, target, prev_winner_vec, prev_winner_K):
    key = f'm{mult}'
    if STATE_OBJ['rungs'].get(key, {}).get('complete'):
        return STATE_OBJ['rungs'][key]
    stage9 = f'R{mult}'
    seeds9 = []
    if prev_winner_vec is not None:
        if prev_winner_K == 9:
            seeds9.append(np.array(prev_winner_vec, dtype=L.DTYPE))
        else:
            seeds9.append(L.shape_at_knots(prev_winner_vec,
                                           prev_winner_K, 9))
    seeds9.append(L.G50_KNOTS.copy())
    seeds9.append(L.h2_seed(9))
    inc9 = search_at(stage9, 9, target, seeds9)
    rec = {'mult': mult, 'target_peak': float(target),
           'K9': None, 'K17': None, 'legal': False,
           'winner_K': None, 'winner': None,
           'confirmation': None}
    if inc9 is not None:
        bj = best_joint_screen(stage9, 9, target)
        rec['K9'] = {'incumbent_joint': inc9['joint'],
                     'incumbent_score': inc9['score'],
                     'incumbent_screen': inc9['screen_id'],
                     'best_joint_screen': (bj['joint'] if bj
                                           else None),
                     'best_joint_screen_id': (bj['id'] if bj
                                              else None),
                     'screens': STAGE_COUNT.get(stage9, 0)}
    winner, winnerK, winner_stage = None, None, None
    legal = False
    if inc9 is not None and inc9['joint'] >= 0.0:
        winner, winnerK, winner_stage = inc9, 9, stage9
        legal = True
    else:
        # SS5's K=17 gate at this rung
        stage17 = f'R{mult}K17'
        seeds17 = []
        if inc9 is not None:
            seeds17.append(L.shape_at_knots(inc9['vS_scaled'],
                                            9, 17))
        if prev_winner_vec is not None:
            seeds17.append(L.shape_at_knots(prev_winner_vec,
                                            prev_winner_K, 17))
        seeds17.append(L.shape_at_knots(L.G50_KNOTS, 9, 17))
        inc17 = search_at(stage17, 17, target, seeds17)
        if inc17 is not None:
            bj = best_joint_screen(stage17, 17, target)
            rec['K17'] = {'incumbent_joint': inc17['joint'],
                          'incumbent_score': inc17['score'],
                          'incumbent_screen': inc17['screen_id'],
                          'best_joint_screen': (bj['joint'] if bj
                                                else None),
                          'best_joint_screen_id': (bj['id']
                                                   if bj else None),
                          'screens': STAGE_COUNT.get(stage17, 0)}
            if inc17['joint'] >= 0.0:
                winner, winnerK, winner_stage = inc17, 17, stage17
                legal = True
            elif inc9 is None or inc17['joint'] > inc9['joint']:
                # illegal rung: its confirmation is of the
                # better incumbent
                winner, winnerK, winner_stage = inc17, 17, stage17
        if winner is None and inc9 is not None:
            winner, winnerK, winner_stage = inc9, 9, stage9
    rec['legal'] = bool(legal)
    if winner is not None:
        rec['winner_K'] = winnerK
        rec['winner'] = {'joint': winner['joint'],
                         'score': winner['score'],
                         'screen_id': winner['screen_id'],
                         'vS_scaled': winner['vS_scaled'],
                         'stage': winner_stage}
        # SS5: the polish runs for every legal rung winner
        # and for the first illegal rung's incumbent -- the
        # ladder stops at the first illegal rung, so every
        # rung winner is polished.
        rec['confirmation'] = confirm(winner_stage, winnerK,
                                      winner, True)
    rec['complete'] = True
    STATE_OBJ['rungs'][key] = rec
    save_state(STATE_OBJ)
    with open(RUNGS_OUT, 'w') as f:
        json.dump(STATE_OBJ['rungs'], f, indent=1)
    return rec


def main():
    targets = L.rung_targets()
    prev_vec, prev_K = L.G50_KNOTS.copy(), 9
    last_legal = {'mult': 1, 'target_peak': float(L.CRIT),
                  'joint': L.G50_JOINT}
    bracket = None
    for mult, target in targets:
        if n_screens() >= CAP_TOTAL:
            bracket = ('cost_bounded', last_legal)
            break
        rec = run_rung(mult, target, prev_vec, prev_K)
        print(f"rung m={mult} peak={target:.6g} "
              f"K9={None if rec['K9'] is None else round(rec['K9']['incumbent_joint'], 12)} "
              f"K17={None if rec['K17'] is None else round(rec['K17']['incumbent_joint'], 12)} "
              f"legal={rec['legal']} screens={n_screens()}",
              flush=True)
        if rec['winner'] is not None:
            prev_vec = rec['winner']['vS_scaled']
            prev_K = rec['winner_K']
        if rec['legal']:
            last_legal = {'mult': mult,
                          'target_peak': float(target),
                          'joint': rec['winner']['joint']}
        else:
            bracket = ('bracketed', last_legal,
                       {'mult': mult, 'target_peak': float(target),
                        'joint': (rec['winner']['joint']
                                  if rec['winner'] else None)})
            break
    else:
        bracket = ('ceiling', last_legal)
    STATE_OBJ['ladder_outcome'] = {'kind': bracket[0],
                                   'last_legal': last_legal,
                                   'first_illegal': (bracket[2]
                                                     if len(bracket) > 2
                                                     else None),
                                   'total_screens': n_screens()}
    save_state(STATE_OBJ)
    print('ladder outcome:', json.dumps(STATE_OBJ['ladder_outcome']))


if __name__ == '__main__':
    main()
