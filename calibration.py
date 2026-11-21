"""
calibration.py — Phase 0 calibration tests. All must pass before any search.
Writes results/calibration.json and prints a summary.
"""
import json, time
import numpy as np
import verify_metric as vm
import metrics as mx
import shell as sh

DTYPE = np.float64
out = {}

# ---------------------------------------------------------------- unit tests
def unit_tests():
    res = {}
    # (a) perfect fluid rho=2, p=0.5: must PASS all
    That = np.diag([2.0, 0.5, 0.5, 0.5]).astype(DTYPE)[None]
    m = vm.hawking_ellis_margins(That)
    res['perfect_fluid_pass'] = bool(m['nec'][0] > 0 and m['wec'][0] > 0
                                    and m['sec'][0] > 0 and m['dec'][0] > 0)
    # (b) Eulerian-positive (rho_E=1) but p_x=-2: must FAIL NEC (all-observer)
    That = np.diag([1.0, -2.0, 0.0, 0.0]).astype(DTYPE)[None]
    m = vm.hawking_ellis_margins(That)
    res['eulerian_positive_nec_fail'] = bool(m['rho_euler'][0] > 0 and m['nec'][0] < 0)
    # (c) big momentum flux T_0x=1.5, rho=1, p=0: complex eigenvalues (Type IV),
    #     must NOT be Type I and sampled NEC must be negative
    That = np.zeros((1, 4, 4), dtype=DTYPE); That[0, 0, 0] = 1.0
    That[0, 0, 1] = That[0, 1, 0] = 1.5
    m = vm.hawking_ellis_margins(That)
    s = vm.sampled_margins(That)
    res['flux_typeIV_flagged'] = bool((not m['typeI'][0]) and s['nec_s'][0] < 0)
    # (d) dust rho=1,p=0 passes; negative density fails WEC
    That = np.diag([1.0, 0.0, 0.0, 0.0]).astype(DTYPE)[None]
    m = vm.hawking_ellis_margins(That)
    res['dust_pass'] = bool(m['wec'][0] >= 0 and m['dec'][0] >= 0)
    That = np.diag([-1.0, 0.0, 0.0, 0.0]).astype(DTYPE)[None]
    m = vm.hawking_ellis_margins(That)
    res['neg_density_wec_fail'] = bool(m['wec'][0] < 0)
    return res

out['unit_tests'] = unit_tests()
print('unit tests:', out['unit_tests'], flush=True)

# ------------------------------------------------- Alcubierre numeric vs analytic
def alcubierre_test(N, v=0.7, R=1.5, sigma=2.0, L=6.0):
    g, h, (X, Y, Z) = mx.alcubierre_grid(N, L, v, R, sigma)
    r = mx.radii(X, Y, Z)
    fprime = mx.alcubierre_fprime(r, R, sigma)
    rho_analytic = -(v ** 2 / (32 * np.pi)) * ((Y ** 2 + Z ** 2) / np.maximum(r, 1e-12) ** 2) * fprime ** 2
    # interior mask: away from boundary and origin, significant density
    mask = np.zeros_like(r, dtype=bool)
    mask[3:-3, 3:-3, 3:-3] = True
    mask &= (r > 0.4) & (r < 4.5) & (np.abs(rho_analytic) > 0.05 * np.max(np.abs(rho_analytic)))
    t0 = time.time()
    if N <= 49:
        res = vm.audit_metric(g, h)
        dt = time.time() - t0
        rho_num = res['That'][..., 0, 0]
        wall = np.abs(fprime) > 0.25 * np.max(np.abs(fprime))
        nec = res['nec']
        viol = (nec < -1e-6) & mask
        frac_in_wall = float(np.sum(viol & wall) / max(np.sum(viol), 1))
        return {'N': N, 'h': h, 'time_s': dt, 'method': 'full audit',
                'max_abs_err_rho': float(np.max(np.abs(rho_num - rho_analytic)[mask])),
                'median_rel_err_rho': float(np.median(
                    np.abs(rho_num - rho_analytic)[mask]
                    / np.maximum(np.abs(rho_analytic)[mask], 1e-300))),
                'min_nec': float(np.nanmin(nec)), 'min_wec': float(np.nanmin(res['wec'])),
                'min_sec': float(np.nanmin(res['sec'])), 'min_dec': float(np.nanmin(res['dec'])),
                'frac_nec_viol_in_wall': frac_in_wall,
                'typeI_frac': float(np.mean(res['typeI']))}
    summ = vm.grid_margins_summary(g, h, mask=mask)
    dt = time.time() - t0
    rho_num = summ['That'][..., 0, 0]
    return {'N': N, 'h': h, 'time_s': dt, 'method': 'screening summary',
            'max_abs_err_rho': float(np.max(np.abs(rho_num - rho_analytic)[mask])),
            'median_rel_err_rho': float(np.median(
                np.abs(rho_num - rho_analytic)[mask]
                / np.maximum(np.abs(rho_analytic)[mask], 1e-300))),
            'min_nec': summ['min_nec'], 'min_wec': summ['min_wec'],
            'min_sec': summ['min_sec'], 'min_dec': summ['min_dec'],
            'typeI_frac': summ['typeI_frac_masked']}

alc = []
for N in (33, 49, 65, 97):
    a = alcubierre_test(N)
    alc.append(a)
    print('alcubierre', a, flush=True)
out['alcubierre'] = alc

# eigenvalue vs sampled cross-check, done with the POINT auditor (grid FD
# noise flips Hawking-Ellis type at isolated points; the point auditor at
# h=0.05 reproduces the exact classification). On Type-I points with a clear
# eigenvalue NEC margin, dense sampled NEC must agree in sign; sampled NEC
# (an upper bound of the true min over the sampled set) must also satisfy
# sampled >= eigenvalue - tolerance on Type-I points.
rng = np.random.default_rng(7)
dirs = rng.normal(size=(400, 3)); dirs /= np.linalg.norm(dirs, axis=1)[:, None]
pts = dirs * rng.uniform(0.8, 2.4, size=(400, 1))
G, That, m = vm.einstein_at_points(lambda p: mx.alcubierre_point(p, 0.7, 1.5, 2.0),
                                   pts, h=0.05, do_fallback=False)
s = vm.sampled_margins(That)
clear = m['typeI'] & (np.abs(m['nec']) > 1e-3)
sign_agree = float(np.mean((s['nec_s'][clear] < 0) == (m['nec'][clear] < 0))) if np.any(clear) else float('nan')
bound_ok = float(np.mean(s['nec_s'][clear] >= m['nec'][clear] - 2e-3)) if np.any(clear) else float('nan')
out['eigen_vs_sampled_nec_agreement_typeI'] = sign_agree
out['eigen_vs_sampled_nec_clear_points'] = int(np.sum(clear))
out['sampled_ge_eigen_bound_frac'] = bound_ok
print('eigen vs sampled NEC: sign agreement', sign_agree,
      'n_clear =', int(np.sum(clear)), 'bound frac', bound_ok, flush=True)

# ------------------------------------------- point-auditor convergence (exact)
# Exact values from the SymPy path (debug_typeI.py): equator point is Type I
# with NEC = -0.00964 and That00 = -0.00492; generic point is Type IV.
pts = np.array([[0.0, 1.5, 0.0], [1.0, 1.0, 0.5], [0.0, 0.0, 1.5]])
pa = []
for hh in (0.2, 0.1, 0.05):
    G, That, m = vm.einstein_at_points(lambda p: mx.alcubierre_point(p, 0.7, 1.5, 2.0), pts, h=hh)
    pa.append({'h': hh, 'That00': [float(x) for x in That[:, 0, 0]],
               'nec': [float(x) for x in m['nec']],
               'typeI': [bool(x) for x in m['typeI']]})
    print('point audit h=', hh, pa[-1], flush=True)
out['point_auditor'] = {'points': pts.tolist(),
                        'exact_That00': [-0.00492, -0.00273, -0.00492],
                        'exact_nec_equator': -0.00964, 'runs': pa}

# ------------------------------------------------------------- Van den Broeck
def vdb_test(N=49, v=0.7):
    g, h, (X, Y, Z) = mx.vandenbroeck_grid(N, 6.0, v)
    res = vm.audit_metric(g, h)
    r = mx.radii(X, Y, Z)
    wall = (r > 0.4) & (r < 3.0)
    return {'min_nec': float(np.nanmin(res['nec'])),
            'min_wec': float(np.nanmin(res['wec'])),
            'min_dec': float(np.nanmin(res['dec'])),
            'min_nec_in_wall': float(np.nanmin(np.where(wall, res['nec'], np.inf))),
            'typeI_frac': float(np.mean(res['typeI']))}

out['vandenbroeck'] = vdb_test()
print('vandenbroeck:', out['vandenbroeck'], flush=True)

# ------------------------------------------------- Fuchs base shell (exact 1D)
M_geom = 7.426e-28 * 4.49e27   # G/c^2 * M_kg, in metres
prof = sh.build_shell(10.0, 20.0, M_geom, kind='constant', s_rho=1.5, s_P=1.5 / 1.72)
marg = sh.shell_exact_margins(prof)
shellmask = (prof['r'] >= 8.0) & (prof['r'] <= 22.0)
out['fuchs_base_shell_exact'] = {
    'M_geom_m': float(M_geom),
    'min_nec_shell': float(np.nanmin(marg['nec'][shellmask])),
    'min_wec_shell': float(np.nanmin(marg['wec'][shellmask])),
    'min_sec_shell': float(np.nanmin(marg['sec'][shellmask])),
    'min_dec_shell': float(np.nanmin(marg['dec'][shellmask])),
    'rho_peak_geom': float(np.max(prof['rho_ex'])),
    'p_t_peak_over_rho': float(np.max(np.abs(prof['p_t'][shellmask]) / np.maximum(prof['rho_ex'][shellmask], 1e-300))),
}
print('fuchs base shell exact:', out['fuchs_base_shell_exact'], flush=True)

with open('results/calibration.json', 'w') as fh:
    json.dump(out, fh, indent=1)
print('CALIBRATION DONE')
