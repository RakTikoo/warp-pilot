#!/usr/bin/env python3
"""p83_branch_refine.py - supplementary refinement of the P8-3 Gelfand
branch boundary on the primary path (rho_c scaled, s_t=15):
lam in {0.9, 0.8, 0.7, 0.6, 0.55}. Same shooting test as
p83_control_scan.py. float64, system python3 numpy 2.2.6/scipy 1.14.1."""
import json
import sys
import time
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from p83_control_scan import shoot_beta15, S_T  # noqa: E402
from scipy.interpolate import CubicSpline  # noqa: E402
sys.path.insert(0, str(HERE.parent / 'phase7'))
sys.path.insert(0, str(HERE.parent / 'phase6'))
sys.path.insert(0, str(HERE.parent))
from p75_solve import build_prescription  # noqa: E402


def main():
    t0 = time.time()
    pres = build_prescription()
    rho_s = CubicSpline(pres['r'], pres['rho'])
    rho_c = pres['rho_c']
    b0_grid = np.linspace(0.0, 1.0, 101)
    rows = []
    for lam in (0.9, 0.8, 0.7, 0.6, 0.55):
        rf = lambda s, lam=lam: lam * float(rho_s(np.clip(s, 0, S_T)))
        b15 = shoot_beta15(rf, S_T, b0_grid)
        i = int(np.nanargmax(b15))
        lo = b0_grid[max(i - 1, 0)]; hi = b0_grid[min(i + 1, len(b0_grid) - 1)]
        fine = np.linspace(lo, hi, 41)
        b15f = shoot_beta15(rf, S_T, fine)
        j = int(np.nanargmax(b15f))
        rows.append({'lam_rho_c_s_t2': lam,
                     'gelfand_param_rho_c_times_st2': lam * rho_c * S_T ** 2,
                     'max_beta15': float(b15f[j]), 'b0_at_max': float(fine[j])})
        print('lam=%.3g max beta(15)=%.5f at b0=%.3f' % (lam, b15f[j], fine[j]), flush=True)
    out = {'item': 'P8-3 branch boundary refinement (primary path)',
           'environment': 'system python3, numpy 2.2.6, scipy 1.14.1; float64',
           'rows': rows, 'runtime_s': time.time() - t0}
    (HERE / 'results' / 'p83_branch_refine.json').write_text(json.dumps(out, indent=1))
    print('wrote results/p83_branch_refine.json')


if __name__ == '__main__':
    main()
