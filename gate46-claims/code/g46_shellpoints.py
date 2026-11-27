#!/usr/bin/env python3
"""Gate-46 supplementary deciding reads: shell-restricted
NEC minima at the STORED argmin shells (the Gate-45 deciding
construction for the controls whose batch minima wander
inside the C-10 band), and the worst-null at Gate-43's
stored MIX argmin point."""
import json

import numpy as np

import g46_lib as L
import g46_profiles as P

RES = '/home/hatch/workspace/warp-pilot/gate46/results'
CASES = {
    'H2S': ((1.0, 1.0, 1.0), 16.21951219512195,
            -1.9422459891767227e-04),
    'MIX': ((0.9323593026620368, 1.1444417317708335,
             1.1445068359375), 12.560975609756097,
            -1.7570735537945242e-04),
    'SEED': ((0.9323593026620368, 1.1444417317708335,
              2.289013671875), 12.317073170731707,
             -1.2413718983790085e-04),
    'ANCHOR': ((0.8015689430763502, 1.3179449338854314,
                3.574968377899082), 15.487804878048781,
               -6.812652656191736e-05),
    'CENTRE': ((0.601180962300002, 1.5934531363763935,
                4.887238651223381), 15.73170731707317,
               -2.9809850277749006e-05),
}
out = {}
for name, (tr, rr, stored_nec) in CASES.items():
    pts = L.DIRS162 * rr
    pr = P.scaled_profiles(*tr, np.full(len(pts), rr))
    T = L.T_cart(pts, pr)
    g = L.metric_cart(pts, pr)
    That = L.eulerian_that(g, T)
    m = L.margins(That)
    j = int(np.argmin(m['nec']))
    _, wn, _ = L.worst_null(That[j])
    out[name] = {
        'shell_r': rr,
        'shell_nec_min': float(m['nec'][j]),
        'stored_nec_min': stored_nec,
        'diff': float(m['nec'][j]) - stored_nec,
        'argmin_point': pts[j].tolist(),
        'argmin_typeI': bool(m['typeI'][j]),
        'worst_null_at_shell_argmin': wn,
    }
    print(name, out[name]['shell_nec_min'], 'diff',
          out[name]['diff'], 'typeI', out[name]['argmin_typeI'],
          flush=True)

# MIX worst-null at Gate-43's stored argmin point
pt43 = np.array([-1.9470056065537118, -10.702464686683815,
                 6.28048780487805])
That = L.that_at(*CASES['MIX'][0], pt43)
m = L.margins(That[None, :, :])
_, wn, _ = L.worst_null(That)
out['MIX_at_gate43_point'] = {
    'point': pt43.tolist(),
    'nec_margin': float(m['nec'][0]),
    'typeI': bool(m['typeI'][0]),
    'worst_null': wn,
    'worst_null_stored_gate43': -1.7703703917379307e-04,
    'worst_null_diff': wn - (-1.7703703917379307e-04),
}
print('MIX@G43pt wn', wn, 'diff',
      out['MIX_at_gate43_point']['worst_null_diff'], flush=True)

with open(f'{RES}/g46_shellpoints.json', 'w') as fh:
    json.dump(out, fh, indent=1)
print('written g46_shellpoints.json', flush=True)
