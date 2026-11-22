"""wa_run.py — W-A Gate-6 driver: anchors, beta=0.07 audit, beta=0.08 ladder.
Usage: python3 wa_run.py [anchors|main|ladder08|all]"""
import json, sys, time
import numpy as np
sys.path.insert(0, '/home/hatch/workspace/warp-pilot')
sys.path.insert(0, '/home/hatch/workspace/warp-pilot/gate6')
import shell as sh
import wa_auditor as wa

OUT = '/home/hatch/workspace/warp-pilot/gate6/wa_results.json'
res = {}
if len(sys.argv) > 1 and sys.argv[1] != 'anchors':
    try: res = json.load(open(OUT))
    except Exception: res = {}

def save():
    json.dump(res, open(OUT, 'w'), indent=1, default=float)

def fib_dirs(n):
    i = np.arange(n)
    phi = np.arccos(1 - 2*(i+0.5)/n)
    th = np.pi*(1+5**0.5)*i
    return np.stack([np.cos(th)*np.sin(phi), np.sin(th)*np.sin(phi), np.cos(phi)], axis=1)
DIRS = fib_dirs(26)

def fine_pts(R1, R2):
    rad = np.concatenate([np.arange(0.3*R1, R1-0.74, 1.0),
                          np.arange(R1-0.75, R2+0.01, 0.5),
                          np.arange(R2+1.0, 1.35*R2+0.01, 2.0)])
    pts = np.concatenate([DIRS*r for r in rad]).astype(np.float64)
    return pts, np.linalg.norm(pts, axis=1)

def summarise(m, pts, radp, R1, R2):
    That = m['That']
    scale = np.max(np.abs(That), axis=(1, 2))
    rho_peak = float(np.max(That[:, 0, 0]))
    thr = max(1e-9*(10.0/R1)**2, 1e-3*abs(rho_peak))
    out = {'rho_peak': rho_peak, 'n_pts': int(len(pts))}
    for reg, mask0 in (('all_sig', np.ones(len(pts), bool)),
                       ('core', (radp >= R1) & (radp <= R2)),
                       ('cavity', radp < R1), ('exterior', radp > R2)):
        mask = mask0 & (scale > thr)
        d = {}
        for k in ('nec', 'wec', 'sec', 'dec'):
            v = m[k][mask]; i = int(np.nanargmin(v)); idx = int(np.where(mask)[0][i])
            d[k] = float(v[i]); d[k+'_r'] = float(radp[idx]); d[k+'_pt'] = [float(x) for x in pts[idx]]
        d['worst'] = min(d[k] for k in ('nec', 'wec', 'sec', 'dec'))
        d['worst_kind'] = min(('nec', 'wec', 'sec', 'dec'), key=lambda k: d[k])
        d['typeI_frac'] = float(np.mean(m['typeI'][mask]))
        d['n'] = int(mask.sum())
        out[reg] = d
    cmask = (radp >= R1) & (radp <= R2) & (scale > thr)
    out['core_sampled_nec_min'] = float(np.min(m['sampled_nec'][cmask]))
    # FD floor proxy: median |margin| on non-significant points (scale<=thr)
    ns = scale <= thr
    if ns.sum() > 10:
        out['floor_proxy_nonsig_median_abs_nec'] = float(np.nanmedian(np.abs(m['nec'][ns])))
    return out

def anchors():
    t0 = time.time()
    # 1) Minkowski control
    def gmink(pts):
        pts = np.asarray(pts); P = pts.shape[0]
        g = np.zeros((P, 4, 4)); g[:, 0, 0] = -1.0
        for i in range(1, 4): g[:, i, i] = 1.0
        return g
    pts = np.array([[5.0, 1.0, 2.0], [-3.0, 4.0, 0.5], [10.0, -2.0, 3.0]])
    G, g = wa.einstein_at(gmink, pts, 0.3)
    res['anchor_minkowski_maxAbsG'] = float(np.max(np.abs(G)))
    # 2) Static exact anchor: beta=0, best-config profile; eigenvalues vs exact 1D T
    prof = sh.build_shell(10.0, 30.0, 8.0, kind='edgepeaked',
                          params={'wd': 6.0, 'floor': 0.2}, s_rho=4.0, s_P=2.32, Nr=4001)
    from scipy.interpolate import interp1d
    ex = {k: interp1d(prof['r'], prof[k]) for k in ('rho_ex', 'p_r', 'p_t')}
    gf0 = sh.shell_point_factory(prof, 0.0, 'cos', 1.0, [10.0, 30.0])
    rows = []
    for h in (0.3, 0.15):
        for r in (12.0, 15.0, 20.0, 25.0, 28.0):
            p = np.array([[r, 0.37, -0.21]])
            p = p * (r/np.linalg.norm(p))
            m = wa.audit(gf0, p, h)
            ps = np.sort(m['p'][0])
            exact = np.sort([float(ex['p_r'](r)), float(ex['p_t'](r)), float(ex['p_t'](r))])
            rows.append({'h': h, 'r': r, 'rho_mine': float(m['rho'][0]),
                         'rho_exact': float(ex['rho_ex'](r)),
                         'rho_rel_err': float(abs(m['rho'][0]-ex['rho_ex'](r))/max(abs(ex['rho_ex'](r)), 1e-300)),
                         'p_mine_sorted': [float(x) for x in ps],
                         'p_exact_sorted': [float(x) for x in exact],
                         'p_max_abs_err': float(np.max(np.abs(ps-exact))),
                         'typeI': bool(m['typeI'][0])})
    res['anchor_static_rows'] = rows
    res['anchor_static_max_rho_rel_err'] = max(r['rho_rel_err'] for r in rows)
    res['anchor_static_max_p_abs_err'] = max(r['p_max_abs_err'] for r in rows)
    # 3) Finalist A positivity (full fine-style point set, h=0.3)
    profA = sh.build_shell(10.0, 20.0, 2.0, kind='edgepeaked',
                           params={'wd': 3.0, 'floor': 0.2}, s_rho=2.0, s_P=1.16, Nr=4001)
    gfA = sh.shell_point_factory(profA, 0.02, 'cos', 1.0, [10.0, 20.0])
    ptsA, radpA = fine_pts(10.0, 20.0)
    mA = wa.audit(gfA, ptsA, 0.3)
    res['anchor_finalistA_h0.3'] = summarise(mA, ptsA, radpA, 10.0, 20.0)
    res['anchors_elapsed_s'] = time.time()-t0
    save()
    print('ANCHORS DONE', 'mink', res['anchor_minkowski_maxAbsG'],
          'maxrhoerr', res['anchor_static_max_rho_rel_err'],
          'maxperr', res['anchor_static_max_p_abs_err'],
          'A worst', res['anchor_finalistA_h0.3']['all_sig']['worst'], flush=True)

def main_audit():
    prof = sh.build_shell(10.0, 30.0, 8.0, kind='edgepeaked',
                          params={'wd': 6.0, 'floor': 0.2}, s_rho=4.0, s_P=2.32, Nr=4001)
    pts, radp = fine_pts(10.0, 30.0)
    for beta in (0.07, 0.08):
        gf = sh.shell_point_factory(prof, beta, 'cos', 1.0, [10.0, 30.0])
        for h in (0.3, 0.15):
            t0 = time.time()
            m = wa.audit(gf, pts, h)
            key = f'main_b{beta}_h{h}'
            res[key] = summarise(m, pts, radp, 10.0, 30.0)
            res[key]['elapsed_s'] = time.time()-t0
            save()
            print(f"MAIN b={beta} h={h} allWorst={res[key]['all_sig']['worst']:+.4e} "
                  f"({res[key]['all_sig']['worst_kind']}@r={res[key]['all_sig'][res[key]['all_sig']['worst_kind']+'_r']:.2f}) "
                  f"coreNEC={res[key]['core']['nec']:+.4e} coreDEC={res[key]['core']['dec']:+.4e} "
                  f"tI={res[key]['all_sig']['typeI_frac']:.3f} sampNEC={res[key]['core_sampled_nec_min']:+.4e} "
                  f"({res[key]['elapsed_s']:.0f}s)", flush=True)
    print('MAIN DONE', flush=True)

def ladder08():
    """Inner-edge h-ladder for beta=0.08 AND beta=0.07 (control):
    radii 9.75..11.5 step 0.25, 26 dirs; min NEC (eigenvalue) per h;
    also track the specific worst direction family: report per-radius minima."""
    prof = sh.build_shell(10.0, 30.0, 8.0, kind='edgepeaked',
                          params={'wd': 6.0, 'floor': 0.2}, s_rho=4.0, s_P=2.32, Nr=4001)
    rad = np.arange(9.75, 11.51, 0.25)
    pts = np.concatenate([DIRS*r for r in rad]).astype(np.float64)
    radp = np.linalg.norm(pts, axis=1)
    for beta in (0.08, 0.07):
        gf = sh.shell_point_factory(prof, beta, 'cos', 1.0, [10.0, 30.0])
        for h in (0.3, 0.15, 0.075, 0.0375):
            t0 = time.time()
            m = wa.audit(gf, pts, h)
            nec = m['nec']
            i = int(np.nanargmin(nec))
            per_r = {}
            for r in rad:
                sel = np.abs(radp-r) < 1e-9
                per_r[f'{r:.2f}'] = float(np.nanmin(nec[sel]))
            key = f'ladder_b{beta}_h{h}'
            res[key] = {'min_nec': float(nec[i]), 'min_nec_r': float(radp[i]),
                        'min_nec_pt': [float(x) for x in pts[i]],
                        'per_radius_min_nec': per_r,
                        'typeI_frac': float(np.mean(m['typeI'])),
                        'sampled_nec_min': float(np.min(m['sampled_nec'])),
                        'elapsed_s': time.time()-t0}
            save()
            print(f"LADDER b={beta} h={h} minNEC={res[key]['min_nec']:+.4e} @r={res[key]['min_nec_r']:.2f} "
                  f"sampNEC={res[key]['sampled_nec_min']:+.4e} ({res[key]['elapsed_s']:.0f}s)", flush=True)
    print('LADDER DONE', flush=True)

if __name__ == '__main__':
    mode = sys.argv[1] if len(sys.argv) > 1 else 'all'
    if mode in ('anchors', 'all'): anchors()
    if mode in ('main', 'all'): main_audit()
    if mode in ('ladder08', 'all'): ladder08()
