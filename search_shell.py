"""
search_shell.py — Phase 2 shell lens (subluminal primary + SL-2 superluminal).

Stage A: exact 1D screen of base shells (no shift) — headroom fractions.
Stage B: 3D grid audits of shell + interior shift at chosen beta_w.
Stage C: bisection on M for the best Stage-B family at beta_w = 0.02
         (Fuchs value) -> minimum passing mass vs Fuchs 3.334 m baseline.
"""
import json, sys, time
import numpy as np
import verify_metric as vm
import shell as sh

DTYPE = np.float64
G_C2 = 7.426e-28
FUCHS_M_GEOM = G_C2 * 4.49e27     # 3.334 m
R1, R2 = 10.0, 20.0


def exact_headroom(prof):
    """Dimensionless EC headroom of the base shell from exact 1D T:
    min over shell points (rho > 5% peak) of margin/rho for each EC."""
    marg = sh.shell_exact_margins(prof)
    rho = prof['rho_ex']
    sel = (prof['r'] >= R1 - 3) & (prof['r'] <= R2 + 3) & (rho > 0.05 * np.max(rho))
    out = {}
    for k in ('nec', 'wec', 'sec', 'dec'):
        out[k] = float(np.min(marg[k][sel] / rho[sel]))
    out['worst'] = min(out[k] for k in ('nec', 'wec', 'sec', 'dec'))
    out['rho_peak'] = float(np.max(rho))
    return out


def stageA():
    Ms = [0.3, 1.0, 2.0, FUCHS_M_GEOM, 5.0]
    kinds = [('constant', {}),
             ('smoothbox', {'edge': 1.0}), ('smoothbox', {'edge': 2.0}),
             ('smoothbox', {'edge': 3.0}),
             ('gauss', {'Rm': 15.0, 'wd': 2.0}), ('gauss', {'Rm': 15.0, 'wd': 3.5}),
             ('matched', {'Rs': 15.0, 'wd': 1.5, 'floor': 0.05}),
             ('matched', {'Rs': 15.0, 'wd': 2.5, 'floor': 0.05}),
             ('matched', {'Rs': 15.0, 'wd': 4.0, 'floor': 0.2}),
             ('edgepeaked', {'wd': 1.5, 'floor': 0.15}),
             ('edgepeaked', {'wd': 2.5, 'floor': 0.15})]
    smooth = [(0.0, 0.0), (1.0, 0.58), (1.5, 0.87), (2.0, 1.16), (1.0, 1.0), (2.0, 2.0)]
    rows = []
    t0 = time.time()
    for M in Ms:
        for kind, params in kinds:
            for sr, sp in smooth:
                try:
                    prof = sh.build_shell(R1, R2, M, kind=kind, params=params,
                                          s_rho=sr, s_P=sp, Nr=2001)
                    hh = exact_headroom(prof)
                except Exception as e:
                    continue
                rows.append({'M_geom': M, 'kind': kind, 'params': params,
                             's_rho': sr, 's_P': sp, **hh})
    rows.sort(key=lambda d: -d['worst'])
    print(f'stageA: {len(rows)} base shells in {time.time()-t0:.0f}s; top 12:')
    for row in rows[:12]:
        print('  ', {k: (round(v, 4) if isinstance(v, float) else v)
                      for k, v in row.items() if k != 'params'}, row['params'])
    with open('results/stageA.json', 'w') as fh:
        json.dump(rows, fh, indent=1)
    return rows


def stageB_eval(M, kind, params, s_rho, s_P, beta_w, N=41, L=30.0,
                shift_kind='fuchs', Rb=1.0, ws=None, Nr=4001):
    prof = sh.build_shell(R1, R2, M, kind=kind, params=params,
                          s_rho=s_rho, s_P=s_P, Nr=Nr)
    g, h, (X, Y, Z) = sh.shell_grid(prof, N, L, beta_w, shift_kind, Rb, ws)
    r = np.sqrt(X ** 2 + Y ** 2 + Z ** 2)
    mask = (r >= 4.0) & (r <= 27.0)
    mask[:3] = mask[-3:] = False; mask[:, :3] = mask[:, -3:] = False
    mask[:, :, :3] = mask[:, :, -3:] = False
    summ = vm.grid_margins_summary(g, h, mask=mask)
    return {'M_geom': M, 'M_kg': M / G_C2, 'kind': kind, 'params': params,
            's_rho': s_rho, 's_P': s_P, 'beta_w': beta_w, 'N': N,
            'min_nec': summ['min_nec'], 'min_wec': summ['min_wec'],
            'min_sec': summ['min_sec'], 'min_dec': summ['min_dec'],
            'worst': min(summ['min_nec'], summ['min_wec'], summ['min_sec'], summ['min_dec']),
            'typeI_frac': summ['typeI_frac_masked'],
            'rho_peak_euler': float(np.max(summ['That'][..., 0, 0]))}


if __name__ == '__main__':
    if sys.argv[1] == 'stageA':
        stageA()
