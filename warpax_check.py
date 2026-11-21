"""
warpax_check.py — Independent second code path (warpax, JAX autodiff +
frame-free certification) on:
  1. NatarioMetric (SSV class — MUST be reported violating)
  2. WarpShellPhysical (warpax's own Fuchs et al. implementation at the
     paper's parameters v_s=0.02, R1=10, R2=20 — paper claims PASS)
Prints full CertifyResult summaries. Results -> results/warpax_check.log
"""
import sys
import numpy as np
import warpax
from warpax.metrics.natario import NatarioMetric
from warpax.metrics.warpshell import WarpShellPhysical


def show(name, res):
    print(f'==== {name} ====')
    print(type(res))
    for attr in ('passed', 'certified', 'is_physical', 'verdict', 'summary',
                 'min_nec', 'min_wec', 'min_sec', 'min_dec',
                 'nec_min', 'wec_min', 'sec_min', 'dec_min'):
        if hasattr(res, attr):
            print(f'  {attr} = {getattr(res, attr)}')
    print('  full:', repr(res)[:3000])
    sys.stdout.flush()


try:
    m = NatarioMetric(v_s=0.5, R=1.0, sigma=8.0)
    res = warpax.certify(m, v_s=0.5, shape=(28, 28, 28))
    show('Natario v=0.5 (control, must FAIL)', res)
except Exception as e:
    print('Natario certify error:', repr(e))
    sys.stdout.flush()

try:
    m2 = WarpShellPhysical()
    res2 = warpax.certify(m2, v_s=0.02, bounds=(-32.0, 32.0), shape=(28, 28, 28))
    show('WarpShellPhysical Fuchs params (paper claims PASS)', res2)
except Exception as e:
    print('WarpShell certify error:', repr(e))
    sys.stdout.flush()
print('WARPAX CHECK DONE')
