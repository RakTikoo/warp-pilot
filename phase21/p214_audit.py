#!/usr/bin/env python3
"""
p214_audit.py -- P21-4 Lorentz-floor read + conservation audit.
Selection (from p214_scan.json): best row per beta (largest
binding partial among health-passing rows; if none, largest
partial overall, labelled), the B3 control's best row per
beta, plus every health-passing row with partial >= 0.50
(conservation only).
FLOOR: antisymmetric residual of the full H (BBW Eq. 42) on
independent Sobol points in the wall volume (r in [9,21],
never in the binding/volume sets), h in {0.3, 0.15};
rel per point = max|H_[ab]| / max|H_(ab)| (coordinate
components); report rel_med.  P19-3 floor: 0.298 / 0.330 at
beta = 1.1 / 1.5; floor-move bar: >= 25% relative
improvement (<= 0.2235 / <= 0.2475) at solution-grade
health.
CONSERVATION: div_b = nabla_a Theta^a_b of Theta := H/8pi,
sample = every 21st binding point, FD step 0.15 (fields at
h=0.15), p121_audit scale pattern; bar rel_med <= 0.02.
float64, system python3.
"""
import json
import sys
import time

import numpy as np
from scipy.stats import qmc

sys.path.insert(0, '/home/hatch/workspace/warp-pilot/phase21')
sys.path.insert(0, '/home/hatch/workspace/warp-pilot')
import verify_metric as vm    # noqa: E402
import p214_lib as L          # noqa: E402

HERE = '/home/hatch/workspace/warp-pilot/phase21/results/'
gate = json.load(open(HERE + 'p214_gate.json'))
B_SIGN = gate['B_sign']
PASS_BAR = 0.02
FLOOR = {1.1: 0.298, 1.5: 0.330}


def par_of(row):
    if row['family'] == 'B2':
        return tuple(row['par'])
    return row['par']


def sobol_points(n=96, seed=20261121):
    eng = qmc.Sobol(d=3, scramble=True, seed=seed)
    u = eng.random_base2(m=int(np.log2(n)))
    # map to shell 9<=r<=21: radius via volume, direction uniform
    r = (9.0**3 + u[:, 0] * (21.0**3 - 9.0**3)) ** (1 / 3)
    z = 2 * u[:, 1] - 1
    ph = 2 * np.pi * u[:, 2]
    s = np.sqrt(1 - z**2)
    return np.stack([r * s * np.cos(ph), r * s * np.sin(ph), r * z],
                    axis=1)


def antisym(beta, pts, fam, par, h):
    gf = L.gf_of(beta)
    F = L.fields_for_set(gf, pts, h, B_sign=B_SIGN)
    H, _ = L.H_cov(F, fam, par)
    Ha = 0.5 * (H - np.swapaxes(H, -1, -2))
    Hs = 0.5 * (H + np.swapaxes(H, -1, -2))
    num = np.max(np.abs(Ha), axis=(1, 2))
    den = np.maximum(np.max(np.abs(Hs), axis=(1, 2)), 1e-300)
    rel = num / den
    return dict(h=h, rel_med=float(np.median(rel)),
                rel_max=float(np.max(rel)),
                rel_p90=float(np.percentile(rel, 90)))


def theta_cov(beta, pts, fam, par, hfield=0.15):
    gf = L.gf_of(beta)
    F = L.fields_for_set(gf, pts, hfield, B_sign=B_SIGN)
    H, _ = L.H_cov(F, fam, par)
    return H / L.EIGHT_PI, gf


def divergence(beta, pts, fam, par, hdiv=0.15):
    Theta0, gf = theta_cov(beta, pts, fam, par, 0.15)
    g0 = gf(pts)
    ginv0 = np.linalg.inv(g0)
    Theta_mix = np.einsum('pma,pab->pmb', ginv0, Theta0)
    Gamma, _, _ = vm._gamma_at(gf, pts, 0.15)
    dTheta = np.zeros_like(Theta_mix)
    for a in range(3):
        acc = np.zeros_like(Theta_mix)
        for kk, wk in ((1, 1.0), (-1, -1.0)):
            off = np.zeros(3)
            off[a] = kk * hdiv
            Th, _ = theta_cov(beta, pts + off, fam, par, 0.15)
            gi = np.linalg.inv(gf(pts + off))
            acc += wk * np.einsum('pma,pab->pmb', gi, Th)
        dTheta[:, a + 1, :] = acc[:, a + 1, :] / (2.0 * hdiv)
    term1 = dTheta.sum(axis=1)
    term2 = np.einsum('paac,pcb->pb', Gamma, Theta_mix)
    term3 = -np.einsum('pcab,pac->pb', Gamma, Theta_mix)
    div = term1 + term2 + term3
    scale = np.abs(term1) + np.abs(term2) + np.abs(term3)
    partial_scale = np.stack([sum(np.abs(dTheta[p, a, :])
                                  for a in range(4))
                              for p in range(len(pts))])
    scale = np.maximum(scale, partial_scale)
    rel = np.abs(div) / np.maximum(scale, 1e-300)
    return dict(hdiv=hdiv, rel_med=float(np.median(rel)),
                rel_max=float(np.max(rel)),
                rel_p90=float(np.percentile(rel, 90)))


def main():
    t0 = time.time()
    scan = json.load(open(HERE + 'p214_scan.json'))
    pts_s = sobol_points()
    out = dict(item='P21-4 Lorentz floor + conservation audit',
               pass_bar=PASS_BAR, floor_P19_3=FLOOR, rows=[])
    sel = {}   # (beta, family, par-key) -> dict(kind=..., row=...)
    cons = {}
    for bs, blk in scan['betas'].items():
        beta = float(bs)
        rows = [r for r in blk['rows'] if r['family'] != 'GR']
        hp = [r for r in rows if r['health_pass']]
        pool = hp if hp else rows
        best = max(pool, key=lambda r: (r['partial'], r['full']))
        sel[(beta, best['family'], str(best['par']))] = dict(
            kind='best' + (' (health-passing pool)' if hp
                           else ' (NO health-passing row; overall)'),
            row=best)
        b3 = [r for r in rows if r['family'] == 'B3']
        b3best = max(b3, key=lambda r: (r['partial'], r['full']))
        sel.setdefault((beta, 'B3', str(b3best['par'])),
                       dict(kind='B3 control best', row=b3best))
        for r in rows:
            if r['health_pass'] and r['partial'] >= 0.50:
                cons[(beta, r['family'], str(r['par']))] = r
    for (beta, fam, pk), ent in sorted(sel.items()):
        r = ent['row']
        par = par_of(r)
        rec = dict(beta=beta, family=fam, par=r['par'], kind=ent['kind'],
                   scan_partial=r['partial'], scan_full=r['full'],
                   scan_health=r['health_pass'], antisym={})
        for h in (0.3, 0.15):
            rec['antisym'][str(h)] = antisym(beta, pts_s, fam, par, h)
            print(f"floor beta={beta} {fam} par={par} h={h}: rel_med="
                  f"{rec['antisym'][str(h)]['rel_med']:.4f}", flush=True)
        if beta in FLOOR:
            base = FLOOR[beta]
            best_rel = min(rec['antisym'][str(h)]['rel_med']
                           for h in (0.3, 0.15))
            rec['floor_P19_3'] = base
            rec['floor_improvement_rel'] = float(1 - best_rel / base)
            rec['floor_move_25pct'] = bool(best_rel <= 0.75 * base)
            rec['antisym_le_002'] = bool(best_rel <= PASS_BAR)
        out['rows'].append(rec)
    out['conservation'] = []
    for (beta, fam, pk), r in sorted(cons.items()):
        par = par_of(r)
        import p103_lib as lib
        bd = lib.bed(beta)
        pts = bd['pts_b'][::21]
        dv = divergence(beta, pts, fam, par)
        rec = dict(beta=beta, family=fam, par=r['par'],
                   scan_partial=r['partial'], divergence=dv,
                   cons_pass=bool(dv['rel_med'] <= PASS_BAR))
        out['conservation'].append(rec)
        print(f"cons beta={beta} {fam} par={par}: rel_med="
              f"{dv['rel_med']:.4f}", flush=True)
    out['runtime_s'] = time.time() - t0
    with open(HERE + 'p214_audit.json', 'w') as fh:
        json.dump(out, fh, indent=2,
                  default=lambda o: bool(o) if isinstance(
                      o, (np.bool_,)) else float(o))
    print('audit done', flush=True)


if __name__ == '__main__':
    main()
