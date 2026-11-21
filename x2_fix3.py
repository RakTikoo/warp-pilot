"""
x2_fix3.py — definitive Schwarzschild rerun with robust masking.
Fix: significance threshold computed on the verdict domain only;
overflow guard |That| < 1e50; alpha^2>0 domain + 0.8 stencil guard;
radius mask r >= max(5, 2 Mbg + 1). Supersedes the schw rows of
x2_scan.json / x2_schw_fix.json.
"""
import json, time
import numpy as np

import verify_metric as vm
import x2_bg
from x2_fix import alpha2_mask, PTS, RAD


def robust_margins(That, mask):
    m = vm.hawking_ellis_margins(That)
    scale = np.max(np.abs(That), axis=(1, 2))
    dom = mask & np.isfinite(scale) & (scale < 1e50)
    out = {'n_domain': int(dom.sum())}
    if dom.sum() == 0:
        return out
    rho_peak = float(np.max(That[dom][:, 0, 0]))
    thr = max(1e-9, 1e-3 * abs(rho_peak))
    sig = dom & (scale > thr)
    out.update({'rho_peak': rho_peak, 'n_sig': int(sig.sum())})
    if sig.sum():
        for k in ('nec', 'wec', 'sec', 'dec'):
            out[k] = float(np.min(m[k][sig]))
        out['worst'] = min(out[k] for k in ('nec', 'wec', 'sec', 'dec'))
        out['typeI_frac_sig'] = float(np.mean(m['typeI'][sig]))
    return out


def audit3(bg, beta_w):
    gf_t = x2_bg.make_gfunc(bg, beta_w, shell_on=True)
    g = gf_t(PTS)
    ok, a2min = alpha2_mask(g)
    bad = PTS[~ok]
    if len(bad):
        d2 = np.min(np.sum((PTS[:, None, :] - bad[None, :, :]) ** 2, axis=2),
                    axis=1)
        near = d2 < 0.8 ** 2
    else:
        near = np.zeros(len(PTS), bool)
    rmin = max(5.0, 2.0 * bg[1] + 1.0)
    mask = ok & ~near & (RAD >= rmin)
    G_t, That_t, _ = vm.einstein_at_points(gf_t, PTS, h=0.3)
    gf_b = x2_bg.make_gfunc(bg, 0.0, shell_on=False)
    G_b, That_b, _ = vm.einstein_at_points(gf_b, PTS, h=0.3)
    That_d = vm.eulerian_that(g, (G_t - G_b) / vm.EIGHT_PI)
    return {'total': robust_margins(That_t, mask),
            'diff': robust_margins(That_d, mask),
            'n_excluded_total': int((~mask).sum()), 'rmin': rmin}


def main():
    t0 = time.time()
    out = {'rows': []}
    for Mbg in (1.0, 2.0, 4.0):
        for beta in (0.0, 0.02, 0.5, 0.9, 1.0, 1.1, 1.5, 2.0, 3.0):
            r = audit3(('schw', Mbg), beta)
            t, d = r['total'], r['diff']
            print(f"schw{Mbg:g} beta={beta:4.2f}: total worst "
                  f"{t.get('worst', float('nan')):+.4e} (NEC "
                  f"{t.get('nec', float('nan')):+.3e}) TypeI "
                  f"{t.get('typeI_frac_sig', float('nan')):.3f} | diff NEC "
                  f"{d.get('nec', float('nan')):+.3e} | nsig {t.get('n_sig')}",
                  flush=True)
            out['rows'].append({'bg': f'schw{Mbg:g}', 'beta': beta, **r})
    out['elapsed_s'] = time.time() - t0
    json.dump(out, open('results/x2_schw_fix3.json', 'w'), indent=1,
              default=float)
    print(f'X2 FIX3 DONE in {out["elapsed_s"]:.0f}s', flush=True)


if __name__ == '__main__':
    main()
