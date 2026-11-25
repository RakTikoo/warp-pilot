"""
p462_cavity.py — deciding check on the cavity DEC dip (r~4.87, just
inside the outer wall's inner edge R1o=5): audit cavity points whose
FD stencil does NOT cross the wall edge (r <= 4.6 at h=0.075/0.15)
vs the near-edge radius itself, for the 0.08 and 0.0998 rows.
If interior cavity points are clean at both h while only the
stencil-crossing radius dips at floor level, the dip is a stencil
artefact (P41-3 precedent), not a cavity violation.
"""
import json, sys
import numpy as np
sys.path.insert(0, '/home/hatch/workspace/warp-pilot')
sys.path.insert(0, '/home/hatch/workspace/warp-pilot/phase41')
import shell as sh
import verify_metric as vm
from p413_audit import build_composed, composed_gfunc, fib_dirs

OUT = '/home/hatch/workspace/warp-pilot/phase46/results/p462_cavity.json'
prof_o = sh.build_shell(5.0, 10.0, 1.9125, kind='edgepeaked',
                        params={'wd': 1.0, 'floor': 0.1}, s_rho=1.0, s_P=0.58, Nr=4001)
prof_i = sh.build_shell(2.0, 4.0, 0.765, kind='edgepeaked',
                        params={'wd': 0.4, 'floor': 0.1}, s_rho=0.4, s_P=0.232, Nr=4001)
comp0 = build_composed(prof_o, prof_i, 0.0, 0.0)
beta_i_reeq = float(0.05 * np.exp(float(np.interp(3.0, comp0['r'], comp0['a']))
                                  - float(np.interp(3.0, prof_i['r'], prof_i['a']))))
dirs = fib_dirs(26, 23)
res = {'beta_i_reeq': beta_i_reeq}
for tag, payload in (('F_payload0.08', 0.08), ('F_payload0.0998', 0.10)):
    comp = build_composed(prof_o, prof_i, payload - beta_i_reeq, beta_i_reeq)
    gf = composed_gfunc(comp)
    res[tag] = {}
    for label, radii in (('interior_r_le_4.6', [4.2, 4.4, 4.6]),
                         ('near_edge_r_4.87', [4.87])):
        pts = np.concatenate([dirs * rr for rr in radii])
        res[tag][label] = {}
        for h in (0.15, 0.075):
            G, That, m = vm.einstein_at_points(gf, pts, h=h)
            scale = np.max(np.abs(That), axis=(1, 2))
            rho_peak = float(np.max(That[:, 0, 0]))
            thr = max(1e-11, 1e-3 * abs(rho_peak))
            sig = scale > thr
            entry = {'n_sig': int(np.sum(sig)), 'thr': float(thr)}
            for k in ('nec', 'wec', 'sec', 'dec'):
                v = m[k][sig]
                entry['min_' + k] = float(np.min(v)) if v.size else None
            entry['worst'] = float(min(entry['min_' + k] for k in ('nec', 'wec', 'sec', 'dec')))
            entry['typeI_frac'] = float(np.mean(m['typeI'][sig])) if np.any(sig) else None
            res[tag][label][str(h)] = entry
            print(f'{tag} {label} h={h}: worst={entry["worst"]:+.4e} dec={entry["min_dec"]:+.4e} '
                  f'typeI={entry["typeI_frac"]}', flush=True)
json.dump(res, open(OUT, 'w'), indent=1)
print('DONE ->', OUT, flush=True)
