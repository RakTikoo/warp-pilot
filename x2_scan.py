"""
x2_scan.py — X2 scan (background curvature) + Lens E (expansion),
on the validated x2_bg engine. Finalist A shell superposed on:
  schw  Mbg in {1,2,4} (horizon inside the cavity, verdict region r>=5)
  ds    H in {7.3e-27 (H0), 1e-3, 3e-3, 1e-2, 2e-2, 5e-2}  [Lens E]
  ads   L in {30, 60}
  flat  control on the same beta grid
beta grid: design 0.02 + S2/S3 grid {0.5,0.9,1.0,1.1,1.5,2.0,3.0}.

Per config: TOTAL margins (physical tensor), DIFF margins (shell's own
contribution, T_tot - T_bg in the total Eulerian frame), bg max|T|,
all significance-masked; schw rows additionally radius-masked r>=5
(interior reported separately as noise-dominated, per engine validation).
E2 framing binding: de Sitter background violates SEC by itself
(rho+3p = -2rho < 0) and saturates NEC; the shell question is the NEC /
WEC / DEC response and the DIFF tensor. Recession v_rec = H*r is
reported as background expansion, never as local transport.
Lens E snapshot limitation (logged in x2_bg): frozen-H river form;
Hdot terms are outside this audit.
float64 everywhere.
"""
import json, time
import numpy as np

import verify_metric as vm
import x2_bg

DTYPE = np.float64
BETA_GRID = [0.02, 0.5, 0.9, 1.0, 1.1, 1.5, 2.0, 3.0]
PTS = x2_bg.sample_points()
RAD = np.linalg.norm(PTS, axis=1)


def margins_masked(That, mask_extra=None):
    m = vm.hawking_ellis_margins(That)
    scale = np.max(np.abs(That), axis=(1, 2))
    rho_peak = float(np.max(That[:, 0, 0]))
    thr = max(1e-9, 1e-3 * abs(rho_peak))
    sig = scale > thr
    if mask_extra is not None:
        sig = sig & mask_extra
    out = {'rho_peak': rho_peak, 'n_sig': int(sig.sum())}
    if sig.sum():
        for k in ('nec', 'wec', 'sec', 'dec'):
            out[k] = float(np.min(m[k][sig]))
        out['worst'] = min(out[k] for k in ('nec', 'wec', 'sec', 'dec'))
        out['typeI_frac_sig'] = float(np.mean(m['typeI'][sig]))
    return out


def audit2(bg, beta_w, rmin=None):
    gf_t = x2_bg.make_gfunc(bg, beta_w, shell_on=True)
    G_t, That_t, _ = vm.einstein_at_points(gf_t, PTS, h=0.3)
    gf_b = x2_bg.make_gfunc(bg, 0.0, shell_on=False)
    G_b, That_b, _ = vm.einstein_at_points(gf_b, PTS, h=0.3)
    T_diff = (G_t - G_b) / vm.EIGHT_PI
    That_d = vm.eulerian_that(gf_t(PTS), T_diff)
    mask = None if rmin is None else (RAD >= rmin)
    return {'total': margins_masked(That_t, mask),
            'diff': margins_masked(That_d, mask),
            'bg_only': margins_masked(That_b, mask),
            'bg_max_abs_T': float(np.max(np.abs(That_b)))}


def row(bg_label, bg, beta, rmin=None):
    r = audit2(bg, beta, rmin=rmin)
    t, d = r['total'], r['diff']
    print(f"{bg_label:12s} beta={beta:5.2f}: total worst "
          f"{t.get('worst', float('nan')):+.4e} (NEC {t.get('nec', float('nan')):+.3e}) "
          f"TypeI {t.get('typeI_frac_sig', float('nan')):.3f} | diff worst "
          f"{d.get('worst', float('nan')):+.4e} (NEC {d.get('nec', float('nan')):+.3e}) "
          f"| bg max|T| {r['bg_max_abs_T']:.2e}", flush=True)
    return {'bg': bg_label, 'beta': beta, **r}


def main():
    t0 = time.time()
    out = {'rows': []}
    # flat controls on the full grid
    for beta in BETA_GRID:
        out['rows'].append(row('flat', ('flat',), beta))
    # Schwarzschild (S2): full beta grid at each Mbg, verdict r>=5
    for Mbg in (1.0, 2.0, 4.0):
        for beta in BETA_GRID:
            out['rows'].append(row(f'schw{Mbg:g}', ('schw', Mbg), beta,
                                   rmin=5.0))
    # AdS: subset
    for L in (30.0, 60.0):
        for beta in (0.02, 1.1, 2.0):
            out['rows'].append(row(f'ads{L:g}', ('ads', L), beta))
    # de Sitter / Lens E: H scan at design beta, beta grids at two H,
    # H0 anchor rows
    for H in (1e-3, 3e-3, 1e-2, 2e-2, 5e-2):
        out['rows'].append(row(f'ds{H:g}', ('ds', H), 0.02))
    for H in (1e-2, 5e-2):
        for beta in (0.5, 0.9, 1.0, 1.1, 1.5, 2.0, 3.0):
            out['rows'].append(row(f'ds{H:g}', ('ds', H), beta))
    for beta in (0.02, 1.5):
        out['rows'].append(row('dsH0', ('ds', 7.3e-27), beta))
    out['elapsed_s'] = time.time() - t0
    json.dump(out, open('results/x2_scan.json', 'w'), indent=1, default=float)
    print(f'X2 SCAN DONE in {out["elapsed_s"]:.0f}s', flush=True)


if __name__ == '__main__':
    main()
