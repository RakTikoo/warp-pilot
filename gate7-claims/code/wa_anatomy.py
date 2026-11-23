"""
wa_anatomy.py — Gate-7 W-A anatomy of the robustness-set findings.
All robustness violations sit at exactly r = R1 = 10.0. This script asks:
  * what happens at r=10 under the three S'' conventions at the edge
    (inside limit, outside limit = 0, mean), since the cosine shift has
    S'' discontinuous at R1/R2 (S in C^1, not C^2, at the window edges);
  * one-sided radial limits r -> 10 +/- ;
  * the beta=0 exact spherical DEC at r=R1 (is the edge DEC deficit a
    property of the static shell representation itself?);
  * which robustness points are non-Type-I at beta=0.10;
  * the tail radii 34-36 margins vs their significance scale.
Symbolic path only (wa_eval). System python3, float64.
Output: results/wa_anatomy.json
"""
import json, sys
import numpy as np
sys.path.insert(0, '/home/hatch/workspace/warp-pilot')
sys.path.insert(0, '/home/hatch/workspace/warp-pilot/gate7')
import shell as sh
import wa_eval as ev
from scipy.interpolate import CubicSpline, interp1d

out = {}
prof = sh.build_shell(10.0, 30.0, 8.0, kind='edgepeaked', params={'wd': 6.0, 'floor': 0.2},
                      s_rho=2.0, s_P=1.16, Nr=4001)
a_s = CubicSpline(prof['r'], prof['a']); b_s = CubicSpline(prof['r'], prof['b'])
DIRS = ev.fib_dirs(52)


def sfunc_factory(spp_mode):
    base = ev.cosine_sfunc(10.0, 30.0)
    k2 = 0.5 * (np.pi / 20.0) ** 2  # |S''(R1+)| = 0.5*k^2 * cos(0)

    def sf(r):
        S, Sp, Spp = base(r)
        r = np.asarray(r, dtype=float)
        at = np.isclose(r, 10.0) | np.isclose(r, 30.0)
        if spp_mode == 'outside':
            Spp = np.where(at, 0.0, Spp)
        elif spp_mode == 'mean':
            Spp = np.where(at, -0.25 * (np.pi / 20.0) ** 2 * np.where(np.isclose(r, 10.0), 1.0, -1.0), Spp)
        return S, Sp, Spp
    return sf


def audit_with_sfunc(pts, beta, sf):
    spl = (a_s, b_s, sf)
    G = ev.einstein_symbolic(pts, spl, beta)
    g = ev.metric_numeric(pts, spl, beta)
    That = ev.eulerian_that(g, G / ev.EIGHT_PI)
    m = ev.margins_from_that(That)
    m['That'] = That; m['sampled_nec'] = ev.sampled_nec_min(That)
    return m


# --- r = 10 ring under S'' conventions, beta = 0.10 and 0.09 and 0 ---
ring = DIRS * 10.0
for beta in (0.10, 0.09, 0.0):
    for mode in ('inside', 'outside', 'mean'):
        m = audit_with_sfunc(ring, beta, sfunc_factory(mode))
        out[f'r10_b{beta}_Spp-{mode}'] = {
            'dec_min': float(np.nanmin(m['dec'])), 'nec_min': float(np.nanmin(m['nec'])),
            'typeI_frac': float(np.mean(m['typeI'])),
            'sampled_nec_min': float(np.min(m['sampled_nec'])),
            'rho_range': [float(np.nanmin(m['rho'])), float(np.nanmax(m['rho']))]}
        print(f"r=10 b={beta} Spp={mode}: DECmin {out[f'r10_b{beta}_Spp-{mode}']['dec_min']:+.4e} "
              f"typeI {out[f'r10_b{beta}_Spp-{mode}']['typeI_frac']:.3f} "
              f"sampNEC {out[f'r10_b{beta}_Spp-{mode}']['sampled_nec_min']:+.4e}", flush=True)

# --- one-sided limits (standard inside convention everywhere) ---
for beta in (0.10, 0.09):
    for dr in (-0.125, -0.05, -0.01, 0.01, 0.05, 0.125):
        m = audit_with_sfunc(DIRS * (10.0 + dr), beta, sfunc_factory('inside'))
        out[f'r10{dr:+.3f}_b{beta}'] = {'dec_min': float(np.nanmin(m['dec'])),
                                        'typeI_frac': float(np.mean(m['typeI'])),
                                        'sampled_nec_min': float(np.min(m['sampled_nec']))}
        print(f"r=10{dr:+.3f} b={beta}: DECmin {out[f'r10{dr:+.3f}_b{beta}']['dec_min']:+.4e} "
              f"typeI {out[f'r10{dr:+.3f}_b{beta}']['typeI_frac']:.3f}", flush=True)

# --- non-Type-I robustness points at beta=0.10 (standard convention) ---
pts_r, radp_r, _ = ev.robustness_pts(10.0, 30.0)
m = ev.audit_symbolic(pts_r, prof, 0.10)
bad = np.where(~m['typeI'])[0]
out['robust_b0.10_non_typeI_points'] = [
    {'pt': [float(x) for x in pts_r[i]], 'r': float(radp_r[i]),
     'sampled_nec': float(m['sampled_nec'][i]),
     'scale_max_abs_That': float(np.max(np.abs(m['That'][i])))} for i in bad]
print('non-TypeI robustness pts b=0.10:', out['robust_b0.10_non_typeI_points'], flush=True)

# --- beta=0 exact spherical read at r=R1 (shell.py exact T) ---
ex = {k: interp1d(prof['r'], prof[k]) for k in ('rho_ex', 'p_r', 'p_t')}
for rr in (9.9, 10.0, 10.1):
    rho, pr, pt = float(ex['rho_ex'](rr)), float(ex['p_r'](rr)), float(ex['p_t'](rr))
    out[f'exact_spherical_r{rr}'] = {'rho': rho, 'p_r': pr, 'p_t': pt,
                                     'dec': rho - max(abs(pr), abs(pt)), 'nec_min': rho + min(pr, pt)}
    print(f'exact spherical r={rr}: rho {rho:.4e} pr {pr:.4e} pt {pt:.4e} DEC {rho-max(abs(pr),abs(pt)):+.4e}', flush=True)

# --- tail radii: margins and significance scale ---
for rr in (33.0, 34.0, 34.5, 35.0, 35.5, 36.0, 37.0):
    mm = ev.audit_symbolic(DIRS * rr, prof, 0.10)
    scale = np.max(np.abs(mm['That']), axis=(1, 2))
    out[f'tail_r{rr}'] = {'scale_max': float(np.max(scale)), 'sec_min': float(np.nanmin(mm['sec'])),
                          'nec_min': float(np.nanmin(mm['nec'])), 'dec_min': float(np.nanmin(mm['dec'])),
                          'typeI_frac': float(np.mean(mm['typeI']))}
    print(f"tail r={rr}: scale {out[f'tail_r{rr}']['scale_max']:.3e} SECmin {out[f'tail_r{rr}']['sec_min']:+.3e} "
          f"NECmin {out[f'tail_r{rr}']['nec_min']:+.3e} DECmin {out[f'tail_r{rr}']['dec_min']:+.3e}", flush=True)

json.dump(out, open('/home/hatch/workspace/warp-pilot/gate7/results/wa_anatomy.json', 'w'), indent=1, default=float)
print('ANATOMY DONE', flush=True)
