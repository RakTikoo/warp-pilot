"""
x2_fix.py — X2 follow-ups under the Failure Protocol.
(1) Rerun all Schwarzschild rows with the audit domain restricted to
    points where the superposed metric's t=const slices are spacelike
    (alpha^2 > 0) AND r >= max(5, 2*Mbg + 1); report excluded counts.
    The original scan's NaN/overflow rows (schw2 beta 0.9-1.5, schw4
    beta 0.9-2.0) came from alpha^2 < 0 points at r = 3-4.5, inside
    the horizon, where no Eulerian tetrad exists.
(2) Decomposition follow-up (F2): schw Mbg in {1, 4} with the shell
    present but its shift set to zero (beta=0) vs full beta=0.02 —
    separates matter-in-tidal-field degradation from shift x inflow
    coupling.
"""
import json, time
import numpy as np

import verify_metric as vm
import x2_bg

PTS = x2_bg.sample_points()
RAD = np.linalg.norm(PTS, axis=1)


def alpha2_mask(g):
    gam = g[:, 1:, 1:]; gti = g[:, 0, 1:]; gtt = g[:, 0, 0]
    ginv = np.linalg.inv(gam)
    a2 = np.einsum('pi,pij,pj->p', gti, ginv, gti) - gtt
    return a2 > 0.0, float(np.min(a2))


def margins_masked(That, mask):
    m = vm.hawking_ellis_margins(That)
    scale = np.max(np.abs(That), axis=(1, 2))
    rho_peak = float(np.max(That[:, 0, 0]))
    thr = max(1e-9, 1e-3 * abs(rho_peak))
    sig = (scale > thr) & mask
    out = {'rho_peak': rho_peak, 'n_sig': int(sig.sum())}
    if sig.sum():
        for k in ('nec', 'wec', 'sec', 'dec'):
            out[k] = float(np.min(m[k][sig]))
        out['worst'] = min(out[k] for k in ('nec', 'wec', 'sec', 'dec'))
        out['typeI_frac_sig'] = float(np.mean(m['typeI'][sig]))
    return out


def audit_fix(bg, beta_w):
    gf_t = x2_bg.make_gfunc(bg, beta_w, shell_on=True)
    g = gf_t(PTS)
    ok, a2min = alpha2_mask(g)
    rmin = max(5.0, 2.0 * bg[1] + 1.0) if bg[0] == 'schw' else 5.0
    mask = ok & (RAD >= rmin)
    G_t, That_t, _ = vm.einstein_at_points(gf_t, PTS, h=0.3)
    gf_b = x2_bg.make_gfunc(bg, 0.0, shell_on=False)
    G_b, That_b, _ = vm.einstein_at_points(gf_b, PTS, h=0.3)
    That_d = vm.eulerian_that(g, (G_t - G_b) / vm.EIGHT_PI)
    return {'total': margins_masked(That_t, mask),
            'diff': margins_masked(That_d, mask),
            'n_excluded_alpha': int((~ok).sum()),
            'n_excluded_total': int((~mask).sum()),
            'alpha2_min': a2min, 'rmin': rmin}


def main():
    t0 = time.time()
    out = {'rows': []}
    for Mbg in (1.0, 2.0, 4.0):
        for beta in (0.0, 0.02, 0.5, 0.9, 1.0, 1.1, 1.5, 2.0, 3.0):
            r = audit_fix(('schw', Mbg), beta)
            t, d = r['total'], r['diff']
            print(f"schw{Mbg:g} beta={beta:4.2f}: total worst "
                  f"{t.get('worst', float('nan')):+.4e} (NEC "
                  f"{t.get('nec', float('nan')):+.3e}) TypeI "
                  f"{t.get('typeI_frac_sig', float('nan')):.3f} | diff NEC "
                  f"{d.get('nec', float('nan')):+.3e} | excl "
                  f"{r['n_excluded_total']} (alpha<0: {r['n_excluded_alpha']})",
                  flush=True)
            out['rows'].append({'bg': f'schw{Mbg:g}', 'beta': beta, **r})
    out['elapsed_s'] = time.time() - t0
    json.dump(out, open('results/x2_schw_fix.json', 'w'), indent=1,
              default=float)
    print(f'X2 FIX DONE in {out["elapsed_s"]:.0f}s', flush=True)


if __name__ == '__main__':
    main()
