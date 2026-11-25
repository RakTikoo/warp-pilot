"""Diagnostic probe (NOT deciding machinery): per-radius payload-region
margins on the Gate-10 symbolic path for the 0.0799 control row, to
anatomise the payload-region read."""
import sys
import numpy as np
from scipy.interpolate import CubicSpline
sys.path.insert(0, '/home/hatch/workspace/warp-pilot/gate10')
import wa_eval as ev
import wa_profiles as wp

prof_o = wp.frontier_outer(); prof_i = wp.frontier_inner()
comp = wp.build_composed(prof_o, prof_i)
a_s = CubicSpline(comp['r'], comp['a']); b_s = CubicSpline(comp['r'], comp['b'])
vf = ev.composed_vfunc(0.04774641838025745, wp.cosine_sfunc(5.0, 10.0),
                       0.03225358161974255, wp.cosine_sfunc(2.0, 4.0))
pts, rad = wp.audit_points(10.0, seed=11)
m = ev.audit(pts, a_s, b_s, vf)
rr = np.linalg.norm(pts, axis=1)
scale = np.max(np.abs(m['That']), axis=(1, 2))
print('rho_peak', float(np.max(m['That'][:, 0, 0])), 'thr', max(1e-11, 1e-3 * abs(float(np.max(m['That'][:, 0, 0])))))
for r0 in sorted(set(np.round(rad, 6))):
    if r0 >= 2.0:
        continue
    sel = np.isclose(rr, r0)
    print(f"r={r0:.4f} n={sel.sum()} max|That|={scale[sel].max():.3e} "
          f"sec_min={np.nanmin(m['sec'][sel]):+.3e} nec_min={np.nanmin(m['nec'][sel]):+.3e} "
          f"rho range [{m['rho'][sel].min():+.3e},{m['rho'][sel].max():+.3e}]")
# the worst payload point in detail
sel = rr < 2.0
sec = np.where(sel, np.where(np.isnan(m['sec']), np.inf, m['sec']), np.inf)
i = int(np.argmin(sec))
print('worst payload point', pts[i], 'r=', rr[i], 'That=\n', m['That'][i])
print('a,b,V at that r: a=', float(a_s(rr[i])), 'b=', float(b_s(rr[i])))
