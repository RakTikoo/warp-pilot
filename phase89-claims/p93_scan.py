#!/usr/bin/env python3
"""
p93_scan.py -- P9-3 checkpoint (B): Einstein-aether scan on the
Finalist-A warp wall, beta in {0.1, 1.1, 1.5} (superluminal
rows run DIRECTLY per the 2026-11-21 amendment; binding set
re-derived at each beta).  Grid (109 rows per beta, stated in
CHECKPOINT9.md before running): slice c13 = 0 (c3 = -c1,
GW170817 data gate), c1 x c2 x c14 main grid + PPN-probe rows
+ c1 = 0 rows + GR control row.

C is linear in (c1,c2,c3,c4) exactly (L, Q, R, divergences
and the EOM lambda are all linear), so 4 unit-coupling basis
tensors at the binding points give every row.  Tensor
identification: p93_gate.py (A1 action FD 0.19-0.52%, A2
spherical reduced action: C^r_r ratio 1.0000, lambda ratio
-1.000, c14-limit 2-4e-4).

Units (Phase-8 Addition 1): ratio = (C_raw(k*,k*)/8pi)/D_That;
ratio-free cross-checks asserted for EVERY row.  Health gate
and data flags as pre-registered in the survey (Jacobson
0711.3822 mode speeds / energy signs; PPN alpha1, alpha2 as
data flags).  Frame gate: N/A in this class (recorded).

float64.  System python3.
"""
import json
import sys
import time

import numpy as np

sys.path.insert(0, '/home/hatch/workspace/warp-pilot')
sys.path.insert(0, '/home/hatch/workspace/warp-pilot/phase6')
sys.path.insert(0, '/home/hatch/workspace/warp-pilot/phase9')
import shell as sh           # noqa: E402
import verify_metric as vm   # noqa: E402
from verify_finalist import dense_points  # noqa: E402
import p61_scan as p61       # noqa: E402
import p93_tensor as tn      # noqa: E402

EIGHT_PI = 8.0 * np.pi
R1, R2 = 10.0, 20.0


def health_ae(c1, c2, c3, c4):
    c13 = c1 + c3
    c14 = c1 + c4
    c123 = c1 + c2 + c3
    s2sq = 1.0 / (1.0 - c13) if c13 != 1.0 else np.inf
    s1sq = (c1 - 0.5 * c1**2 + 0.5 * c3**2) / (c14 * (1.0 - c13)) \
        if c14 != 0 else np.nan
    den = c14 * (1.0 - c13) * (2.0 + c13 + 3.0 * c2)
    s0sq = c123 * (2.0 - c14) / den if den != 0 else np.nan
    e1 = (2 * c1 - c1**2 + c3**2) / (1.0 - c13) if c13 != 1 else np.nan
    e0 = c14 * (2.0 - c14)
    health = bool(0.0 < c14 < 2.0 and np.isfinite(s1sq)
                  and np.isfinite(s0sq) and s1sq > 0 and s0sq > 0
                  and s2sq > 0 and e1 > 0 and e0 > 0)
    # PPN (data flags; formulas Jacobson 0711.3822 eqs.(4,5))
    den1 = 2 * c1 - c1**2 + c3**2
    a1 = -8.0 * (c3**2 + c1 * c4) / den1 if den1 != 0 else None
    if a1 is not None and c123 != 0 and c14 != 2.0:
        a2 = a1 / 2.0 - (c1 + 2 * c3 - c4) * (2 * c1 + 3 * c2 + c3 + c4) \
            / (c123 * (2.0 - c14))
    else:
        a2 = None
    data = bool(a1 is not None and a2 is not None
                and abs(a1) <= 1e-4 and abs(a2) <= 4e-7
                and abs(c13) <= 1e-15)
    cher = bool(np.isfinite(s1sq) and np.isfinite(s0sq)
                and s1sq >= 1.0 and s0sq >= 1.0)
    return dict(c13=c13, c14=c14, c123=c123, s2sq=s2sq,
                s1sq=float(s1sq), s0sq=float(s0sq),
                e1=float(e1), e0=float(e0), health_pass=health,
                alpha1=a1, alpha2=a2, data_pass=data,
                cherenkov_ok=cher)


def grid_rows():
    rows = []
    for c1 in (-0.8, -0.5, -0.2, 0.2, 0.5, 0.8):
        for c2 in (-0.3, 0.0, 0.3, 1.0):
            for c14 in (0.05, 0.2, 0.5, 1.0):
                rows.append((c1, c2, c14))
    for c14 in (1e-5, 1e-3):
        for c1 in (0.2, 0.5):
            for c2 in (0.3, 1.0):
                rows.append((c1, c2, c14))
    for c2 in (0.3, 1.0):
        for c14 in (0.2, 1.0):
            rows.append((0.0, c2, c14))
    rows.append((0.0, 0.0, 0.0))   # GR control
    return rows


def run_beta(beta, pts):
    prof = sh.build_shell(R1, R2, 2.0, kind='edgepeaked',
                          params={'wd': 3.0, 'floor': 0.2},
                          s_rho=2.0, s_P=1.16, Nr=4001)
    gf = sh.shell_point_factory(prof, beta, 'cos', 1.0, [R1, R2])
    sec = p61.Sector(gf, pts, 0.3, 1.0)
    nec_s, n_hat = p61.binding_directions(sec.That_GR)
    r_pts = np.linalg.norm(pts, axis=1)
    deficit = -nec_s
    band = (r_pts >= 9.0) & (r_pts <= 21.0) & (deficit > 0)
    maxdef = np.max(deficit[band])
    bind = band & (deficit >= 0.5 * maxdef)
    pts_b = pts[bind]
    n_b = n_hat[bind]
    D_that = deficit[bind]
    Gkk_raw = p61.null_contract(sec.That_GR, n_hat)[bind] * EIGHT_PI
    print(f'beta={beta}: max deficit {maxdef:.6e}, binding '
          f'{int(bind.sum())}', flush=True)
    # unit-coupling basis tensors at binding points
    basis = []
    for i in range(4):
        cs = tuple(1.0 if j == i else 0.0 for j in range(4))
        C = tn.C_aether(gf, pts_b, 0.3, tn.eulerian_u, cs,
                        lam_sign=-1.0, h_fd=0.15)
        basis.append(vm.eulerian_that(sec.g[bind], C))
        print(f'  basis c{i+1} done', flush=True)
    basis_kk = [p61.null_contract(b, n_b) for b in basis]
    out = dict(beta=beta, max_GR_deficit=float(maxdef),
               n_binding=int(bind.sum()),
               r_at_max=float(r_pts[band][np.argmax(deficit[band])]),
               basis_stats=[], rows=[])
    for i in range(4):
        rk = (basis_kk[i] / EIGHT_PI) / D_that
        out['basis_stats'].append(dict(
            basis=f'c{i+1}', frac_sign=float(np.mean(rk > 0)),
            ratio_med=float(np.median(rk)),
            ratio_min=float(np.min(rk)), ratio_max=float(np.max(rk))))
    for (c1, c2, c14) in grid_rows():
        c3 = -c1
        c4 = c14 - c1
        cs = (c1, c2, c3, c4)
        Chat = sum(cs[i] * basis[i] for i in range(4))
        Ckk = p61.null_contract(Chat, n_b)
        ratio = (Ckk / EIGHT_PI) / D_that
        That_req = sec.That_GR[bind] + Chat / EIGHT_PI
        Tkk_req = p61.null_contract(That_req, n_b)
        w_req, _ = p61.judge_worst(That_req)
        m_req = vm.hawking_ellis_margins(That_req)
        xf_full = float(np.mean(Tkk_req >= 0))
        xf_part = float(np.mean(Ckk >= 0.5 * (-Gkk_raw)))
        assert xf_full == float(np.mean(ratio >= 1)), \
            'full cross-check mismatch'
        assert xf_part == float(np.mean(ratio >= 0.5)), \
            'partial cross-check mismatch'
        hp = health_ae(c1, c2, c3, c4)
        out['rows'].append(dict(
            c1=c1, c2=c2, c3=c3, c4=c4, cs=list(cs),
            ratio_min=float(np.min(ratio)),
            ratio_med=float(np.median(ratio)),
            frac_full=float(np.mean(ratio >= 1)),
            frac_partial=float(np.mean(ratio >= 0.5)),
            frac_sign=float(np.mean(ratio > 0)),
            frac_full_crosscheck=xf_full,
            frac_partial_crosscheck=xf_part,
            req_worst_at_bind=float(np.nanmin(w_req)),
            req_nec_at_bind=float(np.nanmin(m_req['nec'])),
            health=hp))
    return out


def main():
    t0 = time.time()
    pts = dense_points()
    out = dict(item='P9-3 Einstein-aether on warp walls (Phase 9)',
               identification='p93_gate.json: A1 rel 0.19-0.52%; '
                              'A2 rr ratio 1.0000, lambda -1.000',
               units='ratio = (C_raw(k,k)/8pi)/D_That; ratio-free '
                     'cross-checks asserted per row',
               frame_gate='N/A in this class (recorded in survey)',
               betas=[])
    for beta in (0.1, 1.1, 1.5):
        out['betas'].append(run_beta(beta, pts))
        b = out['betas'][-1]
        hp_rows = [r for r in b['rows'] if r['health']['health_pass']]
        best = max(b['rows'], key=lambda r: r['frac_partial'])
        best_hp = max(hp_rows, key=lambda r: r['frac_partial']) \
            if hp_rows else None
        print(f'beta={beta}: rows {len(b["rows"])}, health-pass '
              f'{len(hp_rows)}, best partial (any) '
              f'{best["frac_partial"]:.3f}, best partial (health) '
              f'{best_hp["frac_partial"] if best_hp else None}',
              flush=True)
    out['runtime_s'] = time.time() - t0
    with open('/home/hatch/workspace/warp-pilot/phase9/results/'
              'p93_scan.json', 'w') as fh:
        json.dump(out, fh, indent=2)
    print('P9-3 scan done', flush=True)


if __name__ == '__main__':
    main()
