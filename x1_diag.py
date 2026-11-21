"""x1_diag.py — where does the prescribed-profile torus fail?"""
import numpy as np
from scipy.interpolate import CubicSpline
import x1_torus as x1
import verify_metric as vm

# Control A: flat profiles, beta=0 -> exact Minkowski
_r = np.linspace(0.0, 60.0, 121); _z = np.zeros_like(_r)
tp0 = {'a_s': CubicSpline(_r, _z), 'b_s': CubicSpline(_r, _z),
       'smax': 60.0, 'M': 0.0, 'delta': 5.0, 'a_in': 0.0, 'prof': None}
gf = x1.torus_gfunc(tp0, 45.0, 0.0)
pts = x1.torus_points(45.0, 7)
_, That, _ = vm.einstein_at_points(gf, pts, h=0.3)
print('Control A (flat, beta=0): max|That| =', float(np.max(np.abs(That))))

for (M, Rmaj) in [(2.0, 45.0), (0.5, 45.0), (2.0, 90.0)]:
    tp = x1.torus_profiles(M)
    gf = x1.torus_gfunc(tp, Rmaj, 0.0)
    # structured points: s x phi grid at azimuth 0
    rows = []
    for s in [8, 10.5, 12, 15, 17.5, 19.5, 21, 22.5, 24, 26]:
        for phi in [0.0, np.pi / 2, np.pi, 3 * np.pi / 2]:
            Rc = Rmaj + s * np.cos(phi)
            rows.append([Rc, 0.0, s * np.sin(phi), s, phi])
    arr = np.array(rows)
    _, That, m = vm.einstein_at_points(gf, arr[:, :3], h=0.3)
    worst = np.minimum(np.minimum(m['nec'], m['wec']),
                       np.minimum(m['sec'], m['dec']))
    print(f'--- M={M} Rmaj={Rmaj}: rho range '
          f'[{That[:,0,0].min():+.2e},{That[:,0,0].max():+.2e}]')
    for i in np.argsort(worst)[:6]:
        print(f'  worst {worst[i]:+.3e} at s={arr[i,3]:.1f} phi={arr[i,4]:.2f} '
              f'rho={That[i,0,0]:+.2e} typeI={bool(m["typeI"][i])}')
    # best point too
    i = int(np.argmax(worst))
    print(f'  best  {worst[i]:+.3e} at s={arr[i,3]:.1f} phi={arr[i,4]:.2f}')
