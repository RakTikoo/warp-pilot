"""trackP_ad_audit.py — decisive tiebreak for the Track P beta=0.1
round-4 free-form shape: audit it with the JAX AUTODIFF path (no FD
stencil exists in AD) at the exact final-seed point sets where FD
h=0.3 passed (+6.6e-7) and FD h=0.15 failed (-1.0e-4 / -1.3e-5).

If AD margins are positive, the h=0.15 failure is an FD artefact on
knot-scale features and the candidate proceeds to full finalist
treatment. If AD is negative, the shape is dead.
Run with ./venv/bin/python.
"""
import json
import numpy as np
import jax.numpy as jnp
from scipy.interpolate import CubicSpline, PchipInterpolator

import shell as sh
import trackP as tp
import verify_metric as vm
import redteam as rt

d = json.load(open('results/trackP_b0.1_M10.0_adv_r5.json'))
genes = np.array(d['genes'])
import sys
R1, R2, beta = 10.0, 30.0, 0.1
M = float(sys.argv[1])
tp.set_genes(genes)
prof = sh.build_shell(R1, R2, M, kind='free', params={},
                      s_rho=float(genes[-2]), s_P=float(genes[-1]), Nr=3001)
gfunc_fd = sh.shell_point_factory(prof, beta, 'free', 1.0, None)

xs = jnp.asarray(prof['r'])
ac = jnp.asarray(CubicSpline(prof['r'], prof['a']).c)
bc = jnp.asarray(CubicSpline(prof['r'], prof['b']).c)
kr = np.linspace(R1, R2, 8)
sv = np.concatenate([[1.0], genes[8:14], [0.0]])
pc = PchipInterpolator(kr, sv)
kx = jnp.asarray(kr)
kc = jnp.asarray(pc.c)


def gf(xyz):
    r = jnp.sqrt(jnp.sum(xyz ** 2) + 1e-18)
    rc = jnp.clip(r, xs[0], xs[-1])
    a = rt._spline_eval(rc, xs, ac)
    b = rt._spline_eval(rc, xs, bc)
    sc = jnp.clip(r, kx[0], kx[-1])
    S = rt._spline_eval(sc, kx, kc)
    S = jnp.where(r <= R1, 1.0, jnp.where(r >= R2, 0.0,
                                          jnp.clip(S, 0.0, 1.0)))
    n = xyz / jnp.where(r > 0, r, 1.0)
    g = jnp.zeros((4, 4))
    g = g.at[0, 0].set(-jnp.exp(2 * a))
    g = g.at[0, 1].set(-S * beta).at[1, 0].set(-S * beta)
    eb = jnp.exp(2 * b) - 1.0
    gam = jnp.eye(3) + eb * jnp.outer(n, n)
    g = g.at[1:, 1:].set(gam)
    return g


def ad_margins(pts):
    necs, wecs, secs, decs, tis = [], [], [], [], []
    for pt in pts:
        That = np.array(rt.that_jax(gf, jnp.asarray(pt)))
        m = vm.hawking_ellis_margins(That[None])
        necs.append(float(m['nec'][0])); wecs.append(float(m['wec'][0]))
        secs.append(float(m['sec'][0])); decs.append(float(m['dec'][0]))
        tis.append(bool(m['typeI'][0]))
    return {'nec': min(necs), 'wec': min(wecs), 'sec': min(secs),
            'dec': min(decs), 'typeI_frac': float(np.mean(tis)),
            'worst': min(min(necs), min(wecs), min(secs), min(decs))}


out = {}
for seed in (777001,):
    pts = tp.arbiter_points(R1, R2, seed=seed)
    adm = ad_margins(pts)
    fdm = {}
    for h in (0.3, 0.15):
        ms = tp.audit_full(R1, R2, M, beta, genes, pts, h)
        sig = ms['sig']
        worst = min(float(np.min(ms[k][sig])) for k in
                    ('nec', 'wec', 'sec', 'dec'))
        fdm[h] = {'worst_sig': worst,
                  'typeI_frac_sig': float(np.mean(ms['typeI'][sig]))}
    out[seed] = {'AD': adm, 'FD': {str(k): v for k, v in fdm.items()}}
    print(f'seed {seed}: AD worst {adm["worst"]:+.4e} (NEC {adm["nec"]:+.3e}, '
          f'TypeI {adm["typeI_frac"]:.3f}) | FD stored in json')
    for h, ms in fdm.items():
        print(f'   FD h={h}: {ms}')
json.dump(out, open(f'results/trackP_b01_ad_audit_M{M}.json', 'w'), indent=1,
          default=float)
print('AD AUDIT DONE')
