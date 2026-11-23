"""
wa_probe_exterior.py -- DIAGNOSTIC (non-deciding) tie-break probe for
the deciding row's 21 exterior non-Type-I points on the Gate-11 path.

Questions: (1) at which radii and at what |T| scale do the non-Type-I
points sit (significance-borderline class?); (2) under a dense radial
scan of the exterior band 9.5 < r < 13, is the non-Type-I set an
isolated floor-level spline-tail feature or a convergent region?
Run with ~/workspace/warp-pilot/venv/bin/python.
"""
import sys

import numpy as np
from scipy.interpolate import CubicSpline

sys.path.insert(0, '/home/hatch/workspace/warp-pilot/gate11')
import wa_eval as ev
import wa_profiles as wp

prof_o = wp.outer_profile(); prof_i = wp.inner_profile()
comp = wp.composed_background(prof_o, prof_i)
a_comp = CubicSpline(comp['r'], comp['a']); b_comp = CubicSpline(comp['r'], comp['b'])
xo = wp.outer_vector('e0.10', 'b0.07'); xi = wp.inner_vector('b0.06')
anat = wp.held_w(comp, prof_o, prof_i, 0.07, 0.06)
ch_o = wp.build_chain(prof_o, xo, 0.10); ch_i = wp.build_chain(prof_i, xi, 0.30)
vf = ev.combine_vfunc(anat['beta_o_comp'], wp.chain_sfunc(ch_o),
                      anat['beta_i_comp'], wp.chain_sfunc(ch_i))
pts, rad = wp.registered_points(10.0)
m = ev.audit(pts, a_comp, b_comp, vf)
rr = np.linalg.norm(pts, axis=1)
scale = np.max(np.abs(m['That']), axis=(1, 2))
thr = max(1e-11, 1e-3 * abs(float(np.max(m['That'][:, 0, 0]))))
sig = scale > thr
bad = sig & ~m['typeI']
print(f'thr {thr:.4e}; non-Type-I significant points: {int(np.sum(bad))}')
for idx in np.where(bad)[0]:
    print(f'  r={rr[idx]:.6f} max|That|={scale[idx]:.4e} (x{scale[idx]/thr:.2f} thr) '
          f'sampled_nec={m["sampled_nec"][idx]:+.4e}')
# dense radial scan of the exterior band
dirs = wp.fib_sphere(26, 11)
print('dense scan (26 dirs per radius):')
for r_site in np.arange(9.8, 13.01, 0.2):
    mm = ev.audit(dirs * r_site, a_comp, b_comp, vf)
    sc = np.max(np.abs(mm['That']), axis=(1, 2))
    s2 = sc > thr
    print(f'  r={r_site:.1f} typeI_frac_sig={float(np.mean(mm["typeI"][s2])) if np.any(s2) else None} '
          f'n_sig={int(np.sum(s2))} min_sampled_nec_sig='
          f'{float(np.nanmin(mm["sampled_nec"][s2])) if np.any(s2) else None:+.4e} '
          f'max|That|={float(np.max(sc)):.3e}')
