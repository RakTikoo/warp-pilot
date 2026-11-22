"""Gate-3 follow-up, l=0 mode settlement -- Route I (F4-2/F4-3
formula coefficients) stress tests:

 1. full-line flux solves at h = 0.01, 0.005, 0.0025 with grid
    offsets 0 and h/2 (grid-placement sensitivity at the D=0 pole);
    offset-0 values must replicate F4-3's stored sequence.
 2. segment solves with the pole excised: throat segment
    [-60, r*-delta] and far segment [r*+delta, 60], Dirichlet at
    the cut, delta -> 0 study.  (Theory: at r*, K0,G0 ~ +1/D^2;
    the Liouville potential acquires a +2/(rho-rho*)^2 core, the
    normalisable branch has chi(r*) = 0, so the segment problem
    with Dirichlet at the cut is the physical one.)
 3. Liouville potential from the finest profile: fit of
    V*(rho-rho*)^2 near rho* (expect -> 2), V minimum on the
    throat side, and a Schroedinger-form segment solve in rho.

float64; nothing uploaded.  Results -> results/g3_ell0_route1.json
"""
import json
import time

import numpy as np

import sys
sys.path.insert(0, '/home/hatch/workspace/warp-pilot/phase4')
sys.path.insert(0, '/home/hatch/workspace/warp-pilot/phase3')
import p31_horndeski as p31          # noqa: E402
import p42_ell0 as F42               # noqa: E402
import p43_tachyon as p43            # noqa: E402

RSTAR = 1.772437990426927
t0 = time.time()


def log(*a):
    print(f'[{time.time() - t0:7.1f}s]', *a, flush=True)


def profiles_off(h, offset):
    """p43.ell0_profiles with a shifted grid (same formulas)."""
    r = np.arange(-60.0 + offset, 60.0 + 0.5 * h, h)
    B = F42.build(r, h)
    d = B['d']
    J = d['J']
    corr = (d['Jp']**2 - d['Jp']**3) / d['X']
    K0 = B['K0'] - corr
    G0 = B['G0']
    ds_ = 2e-3
    dpi_ = p31.TAU * ds_
    EBp, _ = F42.shifted_EB_EA(r, d, +ds_)
    EBm, _ = F42.shifted_EB_EA(r, d, -ds_)
    c3 = J**2 * (EBp - EBm) / (2 * dpi_)
    hc = 0.01
    rc = np.arange(-60.0, 60.0 + 0.5 * hc, hc)
    dc = p31.theory_on_bg(rc)
    ELp = F42.el_pi_shifted(rc, dc, +ds_)
    ELm = F42.el_pi_shifted(rc, dc, -ds_)
    e3 = np.interp(r, rc, (ELp - ELm) / (2 * dpi_))
    gr = lambda v: np.gradient(v, h, edge_order=2)
    Bm = B['p'] * c3 + B['q'] * B['c2'] + 2 * B['c6'] * B['p'] * B['q']
    M0 = -(e3 + B['q'] * c3 + B['c6'] * B['q']**2 - 0.5 * gr(Bm))
    return r, K0, G0, M0


def seg(r, K0, G0, M0, lo, hi, k=4):
    m = (r >= lo) & (r <= hi)
    vals, _ = p43.ell0_solve(r[m], K0[m], G0[m], M0[m], k=k)
    return vals


def main():
    res = {'task': 'l=0 mode settlement: Route I stress tests',
           'full_line': {}, 'segments': {}, 'liouville': {}}
    profs = {}
    for h in (0.01, 0.005, 0.0025):
        for off in (0.0, h / 2):
            r, K0, G0, M0 = profiles_off(h, off)
            vals, _ = p43.ell0_solve(r, K0, G0, M0, k=6)
            key = f'h{h}_off{off}'
            res['full_line'][key] = dict(
                lowest=[float(v) for v in vals[:4]],
                K0_min=float(np.min(K0)),
                K0_at_nearest_rstar=float(
                    K0[np.argmin(np.abs(r - RSTAR))]),
                r_nearest_rstar=float(r[np.argmin(np.abs(r - RSTAR))]))
            log(key, 'lowest om2:', np.round(vals[:4], 8),
                'K0min', f"{np.min(K0):.4g}")
            if off == 0.0:
                profs[h] = (r, K0, G0, M0)
    # ---- segment solves (delta -> 0) on the two finest profiles
    for h in (0.005, 0.0025):
        r, K0, G0, M0 = profs[h]
        rows = {}
        for delta in (0.35, 0.2, 0.1, 0.05, 0.02, 0.01):
            th = seg(r, K0, G0, M0, -60.0, RSTAR - delta, k=4)
            fa = seg(r, K0, G0, M0, RSTAR + delta, 60.0, k=4)
            rows[str(delta)] = dict(
                throat_lowest=[float(v) for v in th[:3]],
                far_lowest=[float(v) for v in fa[:3]])
            log(f'h={h} delta={delta}: throat {np.round(th[:3], 8)} '
                f'far {np.round(fa[:3], 8)}')
        res['segments'][f'h{h}'] = rows
    # ---- mode shape on the throat segment (delta = 0.02, h=0.0025)
    r, K0, G0, M0 = profs[0.0025]
    m = (r >= -60.0) & (r <= RSTAR - 0.02)
    vals, vecs = p43.ell0_solve(r[m], K0[m], G0[m], M0[m], k=4)
    chi = vecs[:, 0]
    w = chi**2 * K0[m][1:-1]
    w = w / w.sum()
    rr = r[m][1:-1]
    res['mode_shape'] = dict(
        om2=float(vals[0]),
        frac_r_gt_0=float(w[rr > 0].sum()),
        frac_r_in_0_1=float(w[(rr > 0) & (rr < 1.0)].sum()),
        frac_r_lt_minus5=float(w[rr < -5].sum()),
        peak_r=float(rr[np.argmax(w)]))
    log('mode shape:', res['mode_shape'])
    # ---- Liouville analysis on h=0.0025
    rho, V = p43.liouville_V(r, K0, G0, M0)
    i0 = int(np.argmin(np.abs(r - RSTAR)))
    rho_star = float(rho[i0])
    s = rho - rho_star
    fit = {}
    for side, msk in (('left', (s < -0.002) & (s > -0.06)),
                      ('right', (s > 0.002) & (s < 0.06))):
        if np.sum(msk) > 3:
            fit[side] = dict(
                mean_V_times_s2=float(np.mean(V[msk] * s[msk]**2)),
                min_V_times_s2=float(np.min(V[msk] * s[msk]**2)),
                max_V_times_s2=float(np.max(V[msk] * s[msk]**2)))
    res['liouville'] = dict(
        rho_star=rho_star, fit_Vs2=fit,
        V_min_throat_side=float(np.min(V[(r > -60) & (r < RSTAR - 0.05)])),
        V_at_throat=float(V[np.argmin(np.abs(r))]),
        rho_range=[float(rho[0]), float(rho[-1])])
    log('liouville:', res['liouville'])
    with open('results/g3_ell0_route1.json', 'w') as fh:
        json.dump(res, fh, indent=2)
    log('DONE')


if __name__ == '__main__':
    main()
