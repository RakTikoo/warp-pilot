"""
wa_run_g7.py — Gate-7 W-A driver (G7-1, halved-smoothing row).
Order is registered: ANCHORS first; claim numbers only if anchors pass.
Path: wa_symbolic.py expressions + wa_eval.py analytic evaluation.
System python3, float64. Deciding machinery: symbolic only.
(The wa_auditor FD import below is used ONLY for a labelled machinery
sanity cross-check on 8 points, never for any deciding number.)
"""
import json, sys, time
import numpy as np
sys.path.insert(0, '/home/hatch/workspace/warp-pilot')
sys.path.insert(0, '/home/hatch/workspace/warp-pilot/gate7')
sys.path.insert(0, '/home/hatch/workspace/warp-pilot/gate6')
import shell as sh
import wa_eval as ev
from scipy.interpolate import interp1d

OUT = '/home/hatch/workspace/warp-pilot/gate7/results/wa_g71_numbers.json'
res = {'claim': 'G7-1 halved-smoothing row (10,30) M=8.0 edgepeaked wd=6.0 floor=0.2 '
                'TOV cosine [10,30] smoothing (2.0,1.16)',
       'python': sys.version, 'path': 'symbolic radial-reduction (wa_symbolic.py + wa_eval.py)'}
t_start = time.time()


def save():
    json.dump(res, open(OUT, 'w'), indent=1, default=float)


def build(s_rho, s_P):
    return sh.build_shell(10.0, 30.0, 8.0, kind='edgepeaked',
                          params={'wd': 6.0, 'floor': 0.2}, s_rho=s_rho, s_P=s_P, Nr=4001)


# ---------------- ANCHOR (i): Minkowski ----------------
fns = ev.g_functions()
pts_m = np.array([[5.0, 1.0, 2.0], [-3.0, 4.0, 0.5], [10.0, -2.0, 3.0], [17.0, 3.0, -6.0]])
r_m = np.linalg.norm(pts_m, axis=1); n_m = pts_m / r_m[:, None]
z4 = np.zeros(4)
args_m = (r_m, n_m[:, 0], n_m[:, 1], n_m[:, 2], z4, z4, z4, z4, z4, z4, z4, z4, z4, z4)
mx = 0.0
for fn in fns.values():
    mx = max(mx, float(np.max(np.abs(np.asarray(fn(*args_m), dtype=float)))))
res['anchor_i_minkowski_maxAbsG'] = mx
print(f'[A i] Minkowski max|G| = {mx:.3e}', flush=True)
assert mx < 1e-12, 'ANCHOR (i) FAILED'
save()

# ---------------- ANCHOR (ii): beta=0 vs shell.py exact spherical T ----------------
prof_h = build(2.0, 1.16)
ex = {k: interp1d(prof_h['r'], prof_h[k]) for k in ('rho_ex', 'p_r', 'p_t')}
rows = []
for rr in (12.0, 15.0, 20.0, 25.0, 28.0):
    p = np.array([[rr, 0.37, -0.21]]); p = p * (rr / np.linalg.norm(p))
    m = ev.audit_symbolic(p, prof_h, 0.0)
    ps = np.sort(m['p'][0])
    exact = np.sort([float(ex['p_r'](rr)), float(ex['p_t'](rr)), float(ex['p_t'](rr))])
    rows.append({'r': rr, 'rho_mine': float(m['rho'][0]), 'rho_exact': float(ex['rho_ex'](rr)),
                 'rho_rel_err': float(abs(m['rho'][0] - ex['rho_ex'](rr)) / max(abs(ex['rho_ex'](rr)), 1e-300)),
                 'p_max_abs_err': float(np.max(np.abs(ps - exact))),
                 'typeI': bool(m['typeI'][0])})
res['anchor_ii_static_rows'] = rows
res['anchor_ii_max_rho_rel_err'] = max(x['rho_rel_err'] for x in rows)
res['anchor_ii_max_p_abs_err'] = max(x['p_max_abs_err'] for x in rows)
print(f"[A ii] max rho rel err {res['anchor_ii_max_rho_rel_err']:.3e} (bar 3e-3); "
      f"max p abs err {res['anchor_ii_max_p_abs_err']:.3e} (bar 3e-7)", flush=True)
assert res['anchor_ii_max_rho_rel_err'] <= 3e-3, 'ANCHOR (ii) rho FAILED'
assert res['anchor_ii_max_p_abs_err'] <= 3e-7, 'ANCHOR (ii) p FAILED'
save()

# ---------------- ANCHOR (iii): Gate-6 champion beta=0.08 legal on fine set ----------------
prof_full = build(4.0, 2.32)
pts, radp, rad = ev.fine_pts(10.0, 30.0)
assert len(pts) == 1404, len(pts)
m08 = ev.audit_symbolic(pts, prof_full, 0.08)
s08 = ev.summarise(m08, pts, radp, 10.0, 30.0)
res['anchor_iii_champion_b0.08'] = s08
print(f"[A iii] champion b=0.08: typeI {s08['all_sig']['typeI_frac']:.3f} "
      f"worst {s08['all_sig']['worst']:+.4e} ({s08['all_sig']['worst_kind']} @ r={s08['all_sig'][s08['all_sig']['worst_kind']+'_r']:.2f}) "
      f"core sampled NEC {s08['core_sampled_nec_min']:+.4e}", flush=True)
assert s08['all_sig']['typeI_frac'] == 1.0 and s08['all_sig']['worst'] > 0, 'ANCHOR (iii) FAILED'
save()

# machinery sanity cross-check (NOT deciding): symbolic vs Gate-6 FD on 8 pts
import wa_auditor as wa
gf = sh.shell_point_factory(prof_h, 0.10, 'cos', 1.0, [10.0, 30.0])
rng = np.random.default_rng(3)
dirs = rng.normal(size=(8, 3)); dirs /= np.linalg.norm(dirs, axis=1)[:, None]
radii = np.array([10.25, 12.0, 15.0, 18.8, 20.0, 25.0, 29.0, 33.0])
pts2 = dirs * radii[:, None]
ms = ev.audit_symbolic(pts2, prof_h, 0.10)
mf = wa.audit(gf, pts2, 0.15)
res['sanity_crosscheck_vs_FD_h0.15'] = {
    'radii': [float(x) for x in radii],
    'nec_symbolic': [float(x) for x in ms['nec']],
    'nec_FD': [float(x) for x in mf['nec']],
    'typeI_symbolic': [bool(x) for x in ms['typeI']],
    'typeI_FD': [bool(x) for x in mf['typeI']],
    'max_abs_diff_That': float(np.max(np.abs(ms['That'] - mf['That'])))}
print(f"[sanity] max|That_sym - That_FD| = {res['sanity_crosscheck_vs_FD_h0.15']['max_abs_diff_That']:.3e}", flush=True)
save()

# ---------------- DECIDING SET: halved smoothing, beta = 0.10 / 0.09 ----------------
anchor_resid = res['anchor_ii_max_p_abs_err']
for beta in (0.10, 0.09):
    t0 = time.time()
    m = ev.audit_symbolic(pts, prof_h, beta)
    s = ev.summarise(m, pts, radp, 10.0, 30.0)
    floor = max(s.get('floor_proxy_nonsig_median_abs_nec', 0.0), anchor_resid)
    s['gate_floor'] = float(floor)
    s['floor_components'] = {'nonsig_median_abs_nec': s.get('floor_proxy_nonsig_median_abs_nec'),
                             'anchor_ii_residual_scale': anchor_resid}
    s['worst_over_floor'] = float(s['all_sig']['worst'] / floor)
    s['elapsed_s'] = time.time() - t0
    res[f'deciding_b{beta}'] = s
    print(f"[DEC b={beta}] typeI {s['all_sig']['typeI_frac']:.3f} worst {s['all_sig']['worst']:+.4e} "
          f"({s['all_sig']['worst_kind']} @ r={s['all_sig'][s['all_sig']['worst_kind']+'_r']:.2f}) "
          f"core worst {s['core']['worst']:+.4e} core sampled NEC {s['core_sampled_nec_min']:+.4e} "
          f"floor {floor:.3e} worst/floor {s['worst_over_floor']:.1f}", flush=True)
    save()

# ---------------- ROBUSTNESS SET (reported separately) ----------------
pts_r, radp_r, rad_r = ev.robustness_pts(10.0, 30.0)
res['robustness_n_pts'] = int(len(pts_r))
for beta in (0.10, 0.09):
    m = ev.audit_symbolic(pts_r, prof_h, beta)
    s = ev.summarise(m, pts_r, radp_r, 10.0, 30.0)
    # also raw (all points, no significance mask) minima for the robustness radii
    raw = {}
    for k in ('nec', 'wec', 'sec', 'dec'):
        i = int(np.nanargmin(m[k])) if np.any(~np.isnan(m[k])) else -1
        raw[k] = float(m[k][i]) if i >= 0 else None
        raw[k + '_r'] = float(radp_r[i]) if i >= 0 else None
    raw['typeI_frac_all'] = float(np.mean(m['typeI']))
    raw['sampled_nec_min_all'] = float(np.min(m['sampled_nec']))
    i = int(np.argmin(m['sampled_nec'])); raw['sampled_nec_min_r'] = float(radp_r[i])
    s['raw_all_points'] = raw
    res[f'robustness_b{beta}'] = s
    print(f"[ROB b={beta}] sig typeI {s['all_sig']['typeI_frac']:.3f} worst {s['all_sig']['worst']:+.4e} "
          f"raw typeI {raw['typeI_frac_all']:.3f} raw sampled NEC {raw['sampled_nec_min_all']:+.4e} @ r={raw['sampled_nec_min_r']:.2f}",
          flush=True)
    save()

res['total_elapsed_s'] = time.time() - t_start
save()
print('WA RUN DONE', flush=True)
