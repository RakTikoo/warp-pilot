import numpy as np
import verify_metric as vm
import shell as sh
from verify_finalist import dense_points

def dense_audit(M, beta, tag):
    prof = sh.build_shell(10.0, 20.0, M, kind='edgepeaked', params={'wd': 3.0, 'floor': 0.2},
                          s_rho=2.0, s_P=1.16, Nr=4001)
    gf = sh.shell_point_factory(prof, beta, 'cos', 1.0, [10.0, 20.0])
    pts = dense_points()
    G, That, m = vm.einstein_at_points(gf, pts, h=0.15)
    scale = np.max(np.abs(That), axis=(1, 2))
    core = scale > 1e-5
    print(f'== {tag}: core n={core.sum()} typeI={np.mean(m["typeI"][core]):.4f}')
    for k in ('nec', 'wec', 'sec', 'dec'):
        v = m[k][core]
        i = int(np.argmin(v))
        idx = int(np.where(core)[0][i])
        p = pts[idx]
        print(f'  {k}: min={v[i]:+.3e} at r={np.linalg.norm(p):.2f} dir={np.round(p/np.linalg.norm(p),2)}')
    return m, pts, core

dense_audit(2.4, 0.03, 'B M=2.4 b=0.03 (dense h=0.15)')
dense_audit(2.7, 0.03, 'B2 M=2.7 b=0.03 (dense h=0.15)')
dense_audit(2.4, 0.025, 'B3 M=2.4 b=0.025 (dense h=0.15)')
