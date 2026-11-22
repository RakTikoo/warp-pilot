"""Gate-3 follow-up, l=0 mode settlement -- Route II (dense elim_at
profile) analysis:

 * merge the shard JSONLs; per-point reliability from elim_at's own
   diagnostics (p_ind vs p_f42 = 2 Xi/D deviation; ELA identity
   residual; R01 size);
 * cross-check coefficients against Route I (F4-2 formulas / 2 --
   normalisation) at reliable points;
 * G0/K0 limit toward the pole from reliable flank points
   (Route I / p42 value: 0.6457988469596025);
 * independent throat-segment flux solve from PCHIP interpolants
   of the reliable dense profile (pole excised, Dirichlet at the
   cut), to compare with Route I's segment ground state 0.00445402.

Writes results/g3_ell0_dense_profiles.json (full merged profile
with diagnostics + reliability flags) and
results/g3_ell0_route2.json (analysis).  Safe to run on partial
shard data; rerun at completion for the final record.
"""
import glob
import json
import time

import numpy as np
from scipy.interpolate import PchipInterpolator
from scipy import sparse
from scipy.sparse.linalg import eigsh

import sys
sys.path.insert(0, '/home/hatch/workspace/warp-pilot/phase4')
sys.path.insert(0, '/home/hatch/workspace/warp-pilot/phase3')
sys.path.insert(0, '/home/hatch/workspace/warp-pilot/gate3')
import p43_tachyon as p43            # noqa: E402
from g3_ell0_route1 import profiles_off  # noqa: E402

RSTAR = 1.772437990426927
t0 = time.time()


def log(*a):
    print(f'[{time.time() - t0:7.1f}s]', *a, flush=True)


def flux_solve(r, K0, G0, M0, k=6):
    return p43.ell0_solve(r, K0, G0, M0, k=k)


def main():
    recs = {}
    for path in glob.glob('work_cert/ell0_shard*.jsonl'):
        with open(path) as fh:
            for line in fh:
                d = json.loads(line)
                if 'error' not in d:
                    recs[d['r']] = d
    rs = np.array(sorted(recs))
    log(f'merged {len(rs)} points, r in [{rs[0]}, {rs[-1]}]')
    K0 = np.array([recs[r]['K0'] for r in rs])
    G0 = np.array([recs[r]['G0'] for r in rs])
    M0 = np.array([recs[r]['M0'] for r in rs])
    D = np.array([recs[r]['D'] for r in rs])
    pind = np.array([recs[r]['p_ind'] for r in rs])
    pf42 = np.array([recs[r]['p_f42'] for r in rs])
    ela = np.array([recs[r]['ELA_resid_max'] for r in rs])
    r01 = np.array([recs[r]['R01'] for r in rs])
    # reliability (calibrated on the healthy outer region):
    # p_ind / p_f42 is a CONSTANT convention factor (rel dev exactly
    # 0.5 at every healthy point -- a factor 2 or 2/3 convention);
    # scatter of the ratio away from its median flags FD breakdown
    # of the elimination.  ELA identity residual is ~1e-4 healthy;
    # threshold 2e-3.  (R01/(K0+G0+M0) ~ 0.04-0.08 uniformly -- a
    # property of the route, not a failure signal; recorded only.)
    with np.errstate(divide='ignore', invalid='ignore'):
        ratio = pind / pf42
    med_ratio = float(np.nanmedian(ratio))
    rel_p = np.abs(ratio - med_ratio) / max(abs(med_ratio), 1e-12)
    # NOTE: the p-ratio / ELA diagnostics probe the M-level algebra
    # only; they stay clean (~1e-5) even on points whose final
    # coefficients are FD garbage, because the corruption enters
    # through the r-derivative stencils (half-width 0.28) straddling
    # the D=0 pole.  The operative reliability cut is therefore the
    # programme's own pre-registered exclusion, used identically
    # by F4-1, F4-2b's delta fit and F4-3: |r - r*| >= 0.35, on top
    # of the diagnostics (which do flag the three points nearest
    # the pole, where even the M-level algebra breaks).
    in_band = np.abs(rs - RSTAR) < 0.35
    reliable = (rel_p < 0.02) & (ela < 2e-3) & ~in_band
    reliable &= np.isfinite(K0) & np.isfinite(G0) & np.isfinite(M0)
    res_extra = dict(p_ratio_median=med_ratio)
    bad = rs[~reliable]
    res = {'task': 'l=0 dense Route II profile analysis',
           'n_points': int(len(rs)),
           'n_reliable': int(reliable.sum()),
           'unreliable_r': [float(x) for x in bad],
           'p_ratio_median': med_ratio,
           'unreliable_bands': None}
    if len(bad):
        bands = []
        start = prev = bad[0]
        for x in bad[1:]:
            if x - prev > 0.11:
                bands.append([float(start), float(prev)])
                start = x
            prev = x
        bands.append([float(start), float(prev)])
        res['unreliable_bands'] = bands
    log('unreliable bands:', res['unreliable_bands'])

    # ---- cross-check vs Route I (coefficients / 2)
    rI, K0I, G0I, M0I = profiles_off(0.005, 0.0)
    K0I, G0I, M0I = K0I / 2, G0I / 2, M0I / 2
    sel = reliable & (np.abs(rs - RSTAR) > 0.35) & (np.abs(rs) > 0.2)
    devs = {}
    for name, mine, ref in (('K0', K0, K0I), ('G0', G0, G0I),
                            ('M0', M0, M0I)):
        interp = np.interp(rs[sel], rI, ref)
        denom = np.maximum(np.abs(interp), 1e-12)
        dev = np.abs(mine[sel] - interp) / denom
        devs[name] = dict(max=float(np.max(dev)),
                          median=float(np.median(dev)),
                          frac_within_1pct=float(np.mean(dev < 0.01)))
    res['routeI_crosscheck'] = devs
    log('Route I cross-check (rel dev):', devs)

    # ---- G0/K0 pole limit: Route II band-edge values bracket the
    # analytic limit; Route I (formula route, regular at the pole)
    # evaluates the ratio at its nodes nearest r*.
    flank = reliable & (np.abs(rs - RSTAR) < 0.6)
    if np.sum(flank) > 4:
        order = np.argsort(np.abs(rs[flank] - RSTAR))
        near = [(float(rs[flank][i]), float((G0 / K0)[flank][i]))
                for i in order[:8]]
        res['G0_over_K0_band_edges_routeII'] = near
        log('G0/K0 band edges (Route II):', near)
    with np.errstate(divide='ignore', invalid='ignore'):
        ratioI = G0I / K0I   # normalisation cancels in the ratio
    nearI = np.abs(rI - RSTAR) < 0.05
    res['G0_over_K0_routeI_near_pole'] = dict(
        min=float(np.nanmin(ratioI[nearI])),
        max=float(np.nanmax(ratioI[nearI])),
        analytic_limit=0.6457988469596025)
    log('G0/K0 near pole (Route I):', res['G0_over_K0_routeI_near_pole'])

    # ---- throat-segment solve from the reliable dense profile
    segres = {}
    for delta in (0.35,):
        cut = RSTAR - delta
        m = reliable & (rs <= cut) & (rs >= -60.0)
        if np.sum(m) < 250:
            segres[str(delta)] = 'insufficient reliable coverage'
            continue
        ik = PchipInterpolator(rs[m], K0[m])
        ig = PchipInterpolator(rs[m], G0[m])
        im = PchipInterpolator(rs[m], M0[m])
        for h in (0.01, 0.005):
            rr = np.arange(-60.0, cut + 0.5 * h, h)
            vals, _ = flux_solve(rr, ik(rr), ig(rr), im(rr), k=4)
            segres[f'delta{delta}_h{h}'] = [float(v) for v in vals[:3]]
            log(f'Route II segment delta={delta} h={h}: '
                f'{np.round(vals[:3], 8)}')
    res['routeII_segment'] = segres

    # ---- full merged profile output
    prof = {f'{r:.6f}': dict(
        K0=float(recs[r]['K0']), G0=float(recs[r]['G0']),
        M0=float(recs[r]['M0']), D=float(recs[r]['D']),
        reliable=bool(reliable[i]),
        rel_p_dev=float(rel_p[i]) if np.isfinite(rel_p[i]) else None,
        ELA_resid_max=float(ela[i]))
        for i, r in enumerate(rs)}
    with open('results/g3_ell0_dense_profiles.json', 'w') as fh:
        json.dump({'task': 'dense corrected l=0 profiles (F4-2b '
                           'action route, elim_at), with per-point '
                           'reliability diagnostics',
                   'normalisation': 'covariant (F4-2 App-B = 2x)',
                   'n_points': int(len(rs)),
                   'profile': prof}, fh, indent=1)
    with open('results/g3_ell0_route2.json', 'w') as fh:
        json.dump(res, fh, indent=2)
    log('DONE')


if __name__ == '__main__':
    main()
