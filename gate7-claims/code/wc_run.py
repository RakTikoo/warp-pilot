"""
wc_run.py — W-C driver for G7-3 (Procaccia strengthening).
Order of operations is the registered one:
  STEP 0 hash gate (STOP on mismatch, no audit numbers read);
  STEP 1 fidelity spot check (paper §2/§3 printed values);
  STEP 2 verdict path: 2nd-order FD audit at beta=0.1363, h=0.0375 AND
         h=0.01875, on the P50-1 point set (fine set + support-edge /
         switch / fringe clusters as built by p501_audit.py's main());
         second path: 4th-order direct-d2 at h=0.0375, same set;
  STEP 3 machinery cross-check: beta=0.1364 site ladder at (0,16.635,0),
         h = 0.0375 .. 0.00234375, plus beta=0.1363 at the same point.
Point set and summary conventions replicate p501_audit.py (read as text).
float64. Python: programme venv (numpy 2.5.5 / scipy 1.18.1).
"""
import json, sys, time
import numpy as np
sys.path.insert(0, '/home/hatch/workspace/warp-pilot/gate7')
import wc_recon as rc
import wc_auditor as au

OUT = '/home/hatch/workspace/warp-pilot/gate7/results/wc_g73_numbers.json'
res = {'python': sys.executable, 'item': 'G7-3 Procaccia strengthening (W-C)'}
try:
    res.update(json.load(open(OUT)))
except Exception:
    pass


def save():
    json.dump(res, open(OUT, 'w'), indent=1, default=float)


# ---------- STEP 0: HASH GATE ----------
hashes = rc.hash_gate()
res['step0_hash_gate'] = {
    'expected': rc.PUBLISHED_SHA256,
    'copies': hashes,
    'all_match': all(v == rc.PUBLISHED_SHA256 for v in hashes.values()),
}
save()
print('HASH GATE all_match =', res['step0_hash_gate']['all_match'], flush=True)
if not res['step0_hash_gate']['all_match']:
    res['verdict'] = 'NOT YET — hash mismatch (named gap; no audit numbers read)'
    save()
    sys.exit(0)

x = rc.load_design_vector(rc.DESIGN_PATHS[1])
shell = rc.ProcacciaShellWC(x)
res['design_vector'] = {'q': float(shell.q), 'r_m': float(shell.r_m),
                        'a_i': [float(v) for v in shell.a_i]}

# ---------- STEP 1: FIDELITY SPOT CHECK ----------
fid = shell.fidelity()
res['step1_fidelity'] = fid
core = {k: fid[k]['rel_err'] for k in ('M', 'a_Rin', 'lambda', 'k', 'rho_max')}
res['step1_fidelity']['max_rel_err_core'] = max(core.values())
res['step1_fidelity']['pass'] = bool(fid['M']['rel_err'] <= 1e-9 and
                                     all(core[k] <= 3e-8 for k in ('a_Rin', 'lambda', 'k', 'rho_max')))
save()
print('FIDELITY', json.dumps(core), 'pass =', res['step1_fidelity']['pass'], flush=True)

# Minkowski anchor for the fresh auditor (sanity, not a registered bar)
def gmink(pts):
    pts = np.asarray(pts, dtype=np.float64)
    g = np.zeros((pts.shape[0], 4, 4))
    g[:, 0, 0] = -1.0
    for i in range(1, 4):
        g[:, i, i] = 1.0
    return g
G, _ = au.einstein2(gmink, np.array([[5.0, 1.0, 2.0], [-3.0, 4.0, 0.5]]), 0.0375)
res['anchor_minkowski_maxAbsG'] = float(np.max(np.abs(G)))
save()
print('MINKOWSKI max|G| =', res['anchor_minkowski_maxAbsG'], flush=True)

# ---------- point set (p501_audit.py main() construction) ----------
DIRS = au.fib_dirs(26)


def fine_pts(R1n, R2n):
    rad = np.concatenate([np.arange(0.3 * R1n, R1n - 0.74, 1.0),
                          np.arange(R1n - 0.75, R2n + 0.01, 0.5),
                          np.arange(R2n + 1.0, 1.35 * R2n + 0.01, 2.0)])
    pts = np.concatenate([DIRS * r for r in rad]).astype(np.float64)
    return pts


pts_fine = fine_pts(10.0, 20.0)
extra_rad = np.concatenate([np.arange(2.5, 4.01, 0.25), np.arange(16.3, 17.01, 0.1),
                            np.arange(26.0, 27.51, 0.25)])
epts = np.concatenate([DIRS * r for r in extra_rad]).astype(np.float64)
ALLPTS = np.concatenate([pts_fine, epts])
ALLRAD = np.linalg.norm(ALLPTS, axis=1)
res['point_set'] = {'n_fine': int(len(pts_fine)), 'n_extra': int(len(epts)),
                    'n_total': int(len(ALLPTS)),
                    'extra_radii': [float(v) for v in extra_rad]}
save()
print('POINT SET n =', len(ALLPTS), flush=True)

R_IN = float(rc.R_IN)
R_OUT = float(rc.R_OUT)


def summarise(m, pts, radp):
    That = m['That']
    scale = np.max(np.abs(That), axis=(1, 2))
    rho_peak = float(np.max(That[:, 0, 0]))
    thr = max(1e-9 * (10.0 / 10.0) ** 2, 1e-3 * abs(rho_peak))
    out = {'rho_peak': rho_peak, 'n_pts': int(len(pts)), 'thr': thr}
    for reg, mask0 in (('all_sig', np.ones(len(pts), bool)),
                       ('shell', (radp >= R_IN) & (radp <= R_OUT)),
                       ('nominal_core', (radp >= 10.0) & (radp <= 20.0)),
                       ('cavity', radp < R_IN), ('exterior', radp > R_OUT)):
        mask = mask0 & (scale > thr)
        d = {'n': int(mask.sum())}
        if mask.sum():
            for k in ('nec', 'wec', 'sec', 'dec'):
                v = m[k][mask]
                i = int(np.nanargmin(v))
                idx = int(np.where(mask)[0][i])
                d[k] = float(v[i]); d[k + '_r'] = float(radp[idx])
                d[k + '_pt'] = [float(xx) for xx in pts[idx]]
            d['worst'] = min(d[k] for k in ('nec', 'wec', 'sec', 'dec'))
            d['worst_kind'] = min(('nec', 'wec', 'sec', 'dec'), key=lambda k: d[k])
            d['typeI_frac'] = float(np.mean(m['typeI'][mask]))
            d['n_non_typeI'] = int((~m['typeI'][mask]).sum())
            d['sampled_nec_min'] = float(np.min(m['sampled_nec'][mask]))
            d['sampled_nec_min_r'] = float(radp[int(np.where(mask)[0][int(np.argmin(m['sampled_nec'][mask]))])])
        out[reg] = d
    ns = scale <= thr
    if ns.sum() > 10:
        out['fd_floor_median_abs_nec_nonsig'] = float(np.nanmedian(np.abs(m['nec'][ns])))
        out['n_nonsig'] = int(ns.sum())
    return out


# ---------- STEP 2: VERDICT PATH (2nd-order, h pair) + SECOND PATH (4th-order) ----------
gf = shell.metric_factory(0.1363)
for tag, order, h in (('verdict_h0.0375', 2, 0.0375),
                      ('verdict_h0.01875', 2, 0.01875),
                      ('secondpath_order4_h0.0375', 4, 0.0375)):
    if tag in res:
        print('SKIP (already in JSON)', tag, flush=True)
        continue
    t0 = time.time()
    m = au.audit(gf, ALLPTS, h, order=order)
    s = summarise(m, ALLPTS, ALLRAD)
    s['elapsed_s'] = time.time() - t0
    s['order'] = order
    s['h'] = h
    res[tag] = s
    save()
    sh_ = s['shell']
    print(f"{tag}: shell worst={sh_['worst']:+.4e} ({sh_['worst_kind']}@r={sh_[sh_['worst_kind']+'_r']:.2f}) "
          f"typeI={sh_['typeI_frac']:.4f} sampNEC={sh_['sampled_nec_min']:+.4e} "
          f"floor={s.get('fd_floor_median_abs_nec_nonsig')} ({s['elapsed_s']:.0f}s)", flush=True)

# ---------- STEP 3: MACHINERY CROSS-CHECK ----------
pt = np.array([[0.0, 16.635, 0.0]])
dirs_dense = au.fib_dirs(5002)
lad = {}
for beta in (0.1363, 0.1364):
    gfb = shell.metric_factory(beta)
    for h in (0.0375, 0.01875, 0.009375, 0.0046875, 0.00234375):
        G, g = au.einstein2(gfb, pt, h)
        That = au.eulerian_that(g, G / au.EIGHT_PI)
        m = au.margins_from_that(That)
        key = f'b{beta}_h{h}'
        lad[key] = {'nec': float(m['nec'][0]), 'wec': float(m['wec'][0]),
                    'sec': float(m['sec'][0]), 'dec': float(m['dec'][0]),
                    'typeI': bool(m['typeI'][0]), 'rho': float(m['rho'][0]),
                    'min_null_dense5002': float(au.null_min(That, dirs_dense)[0]),
                    'sampled_nec162': float(au.null_min(That, au.fib_dirs(162))[0])}
        print(f"SITE {key} typeI={lad[key]['typeI']} NEC={lad[key]['nec']} "
              f"minNull={lad[key]['min_null_dense5002']:+.4e}", flush=True)
    # analytic-resolution read: 4th-order at the finest spacing as well
    G4, g4 = au.einstein4(gfb, pt, 0.00234375)
    That4 = au.eulerian_that(g4, G4 / au.EIGHT_PI)
    m4 = au.margins_from_that(That4)
    lad[f'b{beta}_order4_h0.00234375'] = {
        'nec': float(m4['nec'][0]), 'typeI': bool(m4['typeI'][0]),
        'min_null_dense5002': float(au.null_min(That4, dirs_dense)[0])}
res['step3_crosscheck_site_ladder'] = lad
res['step3_crosscheck'] = {'his_interval_value': -1.30135e-07, 'point': [0.0, 16.635, 0.0]}
save()
print('ALL DONE', flush=True)
