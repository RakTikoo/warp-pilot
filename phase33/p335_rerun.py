"""P33-5 bounded re-run attempt: Finalist-A profile at beta=0.1, point audit.
float64, geometric units (T in 1/m^2). Records worst EC margins."""
import json, sys, time
import numpy as np
sys.path.insert(0, '/home/hatch/workspace/warp-pilot')
import shell as sh
import verify_metric as vm

def fib_dirs(n):
    i = np.arange(n)
    phi = np.arccos(1 - 2 * (i + 0.5) / n)
    th = np.pi * (1 + 5 ** 0.5) * i
    return np.stack([np.cos(th) * np.sin(phi), np.sin(th) * np.sin(phi), np.cos(phi)], axis=1)

out = {}
t0 = time.time()
for tag, (R1, R2, M, kind, params, sr, sp, ws) in {
    'A_profile_M2.0': (10.0, 20.0, 2.0, 'edgepeaked', {'wd': 3.0, 'floor': 0.2}, 2.0, 1.16, [10.0, 20.0]),
    'frontierlike_5-10_M1.915': (5.0, 10.0, 1.915, 'edgepeaked', {'wd': 1.5, 'floor': 0.2}, 1.0, 0.58, [5.0, 10.0]),
}.items():
    try:
        prof = sh.build_shell(R1, R2, M, kind=kind, params=params, s_rho=sr, s_P=sp, Nr=4001)
        gf = sh.shell_point_factory(prof, 0.1, 'cos', 1.0, ws)
        dirs = fib_dirs(26)
        rad = np.linspace(3.0, 24.0, 22)
        pts = np.concatenate([dirs * r for r in rad])
        G, That, m = vm.einstein_at_points(gf, pts, h=0.3)
        scale = np.max(np.abs(That), axis=(1, 2))
        thr = max(1e-7, 1e-3 * float(np.max(That[:, 0, 0])))
        sig = scale > thr
        rec = {'n_pts': int(len(pts)), 'n_sig': int(sig.sum()), 'thr': float(thr),
               'rho_peak_geom': float(np.max(That[:, 0, 0]))}
        if sig.any():
            for k in ('nec', 'wec', 'sec', 'dec'):
                rec['min_' + k] = float(np.min(m[k][sig]))
            rec['worst'] = float(min(rec['min_' + k] for k in ('nec', 'wec', 'sec', 'dec')))
            wi = int(np.where(sig)[0][np.argmin(m['dec'][sig])])
            rec['worst_dec_radius_m'] = float(np.linalg.norm(pts[wi]))
        out[tag] = rec
        print(tag, json.dumps(rec), flush=True)
    except Exception as e:
        out[tag] = {'error': repr(e)}
        print(tag, 'ERROR', repr(e), flush=True)
out['wall_time_s'] = time.time() - t0
with open('/home/hatch/workspace/warp-pilot/phase33/results/p335_rerun.json', 'w') as fh:
    json.dump(out, fh, indent=1)
print('done', out['wall_time_s'])
