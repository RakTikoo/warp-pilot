"""
p462_audit.py — P46-2: lapse-re-equilibrated nested shells.

Construction (P41-3 composed pattern, ONE changed ingredient):
  m_comp = m_i + m_o; b_comp from m_comp; P_comp = P_i (standalone,
  unchanged enclosed mass) + P_o* (outer TOV re-integrated against
  m_comp); a_comp integrated from composed pressure [joint re-solve
  retained, exactly as P41-3].
  RE-EQUILIBRATION: the composed lapse a_comp is computed FIRST
  (it is shift-independent), then the inner coordinate beta_i is
  chosen so the inner shell's characteristic orthonormal shift
    W_i = beta_i * exp(-a_comp(r_mid,i)),  r_mid,i = (R1i+R2i)/2
  equals the verified ALONE value W_i^alone = beta_i^alone *
  exp(-a_i^alone(r_mid,i))  (P41-3 follow-up E4 definition:
  frontier 0.05*exp(0.28339) = 0.066381; Finalist-A analogous).
  Hence beta_i^new = beta_i^alone * exp(a_comp(r_mid) - a_i^alone(r_mid)).
  beta_o carries the remainder of the payload:
    beta_o = payload_coord - beta_i^new.
  Shift staircase V(r) = beta_o*S_o(r) + beta_i^new*S_i(r), as P41-3.
Audit: Phase-1 judge, full-volume all-directions NEC/WEC/SEC/DEC +
Type at h in {0.3, 0.15}, conservation read, flat FD-floor control.
float64. Incremental JSON checkpointing.
"""
import json, sys, time, os
import numpy as np

sys.path.insert(0, '/home/hatch/workspace/warp-pilot')
sys.path.insert(0, '/home/hatch/workspace/warp-pilot/phase41')
import shell as sh
import verify_metric as vm
from p413_audit import (build_composed, composed_gfunc, audit_points,
                        region_of, summarise, divergence_read, flat_gfunc)

DTYPE = np.float64
OUT = '/home/hatch/workspace/warp-pilot/phase46/results/p462_results.json'
os.makedirs(os.path.dirname(OUT), exist_ok=True)

CLASSES = {
    'frontier': dict(
        prof_o=lambda: sh.build_shell(5.0, 10.0, 1.9125, kind='edgepeaked',
                                      params={'wd': 1.0, 'floor': 0.1},
                                      s_rho=1.0, s_P=0.58, Nr=4001),
        prof_i=lambda: sh.build_shell(2.0, 4.0, 0.765, kind='edgepeaked',
                                      params={'wd': 0.4, 'floor': 0.1},
                                      s_rho=0.4, s_P=0.232, Nr=4001),
        beta_i_alone=0.05, beta_o_verified=0.05),
    'finalistA': dict(
        prof_o=lambda: sh.build_shell(10.0, 20.0, 2.0, kind='edgepeaked',
                                      params={'wd': 3.0, 'floor': 0.2},
                                      s_rho=2.0, s_P=1.16, Nr=4001),
        prof_i=lambda: sh.build_shell(4.0, 8.0, 0.8, kind='edgepeaked',
                                      params={'wd': 1.2, 'floor': 0.2},
                                      s_rho=0.8, s_P=0.464, Nr=4001),
        beta_i_alone=0.02, beta_o_verified=0.02),
}

# (row name, class, payload_coord) — calibration FIRST
ROWS = [
    ('A_cal_payload0.04', 'finalistA', 0.04),
    ('F_payload0.06', 'frontier', 0.06),
    ('F_payload0.08', 'frontier', 0.08),
    ('F_payload0.0998', 'frontier', 0.10),   # coord 0.10 -> relat 0.0998
]


def anatomy(comp, prof_i, beta_i_alone, beta_i_new, beta_o):
    r_mid_i = 0.5 * (comp['R1i'] + comp['R2i'])
    r_mid_o = 0.5 * (comp['R1o'] + comp['R2o'])
    a_comp_mid_i = float(np.interp(r_mid_i, comp['r'], comp['a']))
    a_alone_mid_i = float(np.interp(r_mid_i, prof_i['r'], prof_i['a']))
    a_comp_mid_o = float(np.interp(r_mid_o, comp['r'], comp['a']))
    a_comp_pay = float(np.interp(0.5 * comp['R1i'], comp['r'], comp['a']))
    S_mid = 0.5  # cos window at its midpoint
    V_mid_i = beta_o + beta_i_new * S_mid
    return {
        'r_mid_inner': r_mid_i,
        'a_composed_inner_midwall': a_comp_mid_i,
        'a_inner_alone_midwall': a_alone_mid_i,
        'exp_a_ratio': float(np.exp(a_comp_mid_i - a_alone_mid_i)),
        'W_target_alone': float(beta_i_alone * np.exp(-a_alone_mid_i)),
        'W_reeq_characteristic': float(beta_i_new * np.exp(-a_comp_mid_i)),
        'beta_i_alone': beta_i_alone, 'beta_i_reeq': float(beta_i_new),
        'beta_o': float(beta_o),
        'V_local_inner_midwall': float(V_mid_i),
        'W_local_total_inner_midwall': float(V_mid_i * np.exp(-a_comp_mid_i)),
        'W_local_inner_own_inner_midwall': float(beta_i_new * S_mid * np.exp(-a_comp_mid_i)),
        'W_local_inner_own_alone_midwall': float(beta_i_alone * S_mid * np.exp(-a_alone_mid_i)),
        'a_composed_outer_midwall': a_comp_mid_o,
        'a_composed_payload': a_comp_pay,
        'W_payload_total': float((beta_o + beta_i_new) * np.exp(-a_comp_pay)),
        'W_outer_characteristic': float(beta_o * np.exp(-a_comp_mid_o)),
    }


def main():
    t0 = time.time()
    res = {'item': 'P46-2', 'float': 'float64', 'rows': {}}
    if os.path.exists(OUT):
        try:
            res = json.load(open(OUT))
            res.setdefault('rows', {})
        except Exception:
            pass

    # FD floor control
    if 'flat_control' not in res:
        rng = np.random.default_rng(7)
        fpts = rng.normal(size=(120, 3)) * 6.0
        res['flat_control'] = {}
        for h in (0.3, 0.15):
            G, That, m = vm.einstein_at_points(flat_gfunc, fpts, h=h)
            res['flat_control'][str(h)] = {'max_abs_T': float(np.max(np.abs(G)) / (8 * np.pi))}
        json.dump(res, open(OUT, 'w'), indent=1)
        print('flat control done', flush=True)

    cache = {}
    for row_name, cls, payload_coord in ROWS:
        if row_name in res['rows'] and 'composed' in res['rows'][row_name]:
            print(f'skip done row {row_name}', flush=True)
            continue
        if cls not in cache:
            prof_o = CLASSES[cls]['prof_o']()
            prof_i = CLASSES[cls]['prof_i']()
            cache[cls] = (prof_o, prof_i)
        prof_o, prof_i = cache[cls]
        bi_alone = CLASSES[cls]['beta_i_alone']
        # provisional composed build (beta values do not affect a_comp)
        comp0 = build_composed(prof_o, prof_i, 0.0, 0.0)
        r_mid_i = 0.5 * (prof_i['R1'] + prof_i['R2'])
        a_comp_mid = float(np.interp(r_mid_i, comp0['r'], comp0['a']))
        a_alone_mid = float(np.interp(r_mid_i, prof_i['r'], prof_i['a']))
        beta_i_new = float(bi_alone * np.exp(a_comp_mid - a_alone_mid))
        beta_o = float(payload_coord - beta_i_new)
        comp = build_composed(prof_o, prof_i, beta_o, beta_i_new)
        gf = composed_gfunc(comp)
        pts, _ = audit_points(prof_o['R2'], seed=11)
        row = {
            'class': cls, 'payload_coord': payload_coord,
            'payload_relat': (beta_o + beta_i_new) / (1 + beta_o * beta_i_new),
            'beta_o': beta_o, 'beta_i_reeq': beta_i_new,
            'beta_i_alone': bi_alone,
            'outer': {'R1': prof_o['R1'], 'R2': prof_o['R2'], 'M': prof_o['M']},
            'inner': {'R1': prof_i['R1'], 'R2': prof_i['R2'], 'M': prof_i['M']},
            'anatomy': anatomy(comp, prof_i, bi_alone, beta_i_new, beta_o),
            'composed': {},
        }
        for h in (0.3, 0.15):
            row['composed'][str(h)] = summarise(
                gf, pts, h, region_fn=lambda r: region_of(r, comp))
            print(f'{row_name} h={h}: worst={row["composed"][str(h)]["worst"]:+.4e} '
                  f'({row["composed"][str(h)]["worst_kind"]}) '
                  f'beta_o={beta_o:.4f} beta_i={beta_i_new:.4f}', flush=True)
            res['rows'][row_name] = row
            json.dump(res, open(OUT, 'w'), indent=1)
        rr = np.sqrt(np.sum(pts ** 2, axis=1))
        wsel = np.array([region_of(x, comp) in ('inner_wall', 'outer_wall') for x in rr])
        wpts = pts[wsel][::max(1, int(np.sum(wsel)) // 28)][:28]
        row['conservation'] = divergence_read(gf, wpts)
        print(f'{row_name} conservation rel_med={row["conservation"]["rel_med"]:.4f}', flush=True)
        res['rows'][row_name] = row
        json.dump(res, open(OUT, 'w'), indent=1)
    res['elapsed_s'] = time.time() - t0
    json.dump(res, open(OUT, 'w'), indent=1)
    print(f'DONE {res["elapsed_s"]:.0f}s -> {OUT}', flush=True)


if __name__ == '__main__':
    main()
