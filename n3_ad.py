"""
n3_ad.py — warpax/JAX autodiff cross-check of an N3 winner
(second, stencil-free computation path; the R5 finalist gate).
Rebuilds the recovered metric from the genes, audits fresh
points with rt.that_jax, and compares against the FD judge at
the same points. Run with ./venv/bin/python.
Usage: python3 n3_ad.py GENES_JSON BETA R1 R2
"""
import json, sys
import numpy as np
import jax.numpy as jnp
from scipy.interpolate import CubicSpline

_SRC = sys.argv[1]; _BETA = float(sys.argv[2])
_R1 = float(sys.argv[3]); _R2 = float(sys.argv[4])
sys.argv = ['n3_de', str(_BETA), '10', str(int(_R1)), str(int(_R2))]
import n3_de
import n3_invert as n3
import shell as sh
import verify_metric as vm
import redteam as rt


def main():
    d = json.load(open(_SRC))
    genes = np.array(d['genes'])
    rho_s, pt_s = n3_de.prescription(genes)
    prof = n3.solve_shell(rho_s, pt_s, R1=_R1, R2=_R2, Nr=4001,
                          rmax=n3_de.RMAX, rout=n3_de.RMAX)
    xs = jnp.asarray(prof['r'])
    ac = jnp.asarray(CubicSpline(prof['r'], prof['a']).c)
    bc = jnp.asarray(CubicSpline(prof['r'], prof['b']).c)
    Sv = sh.shift_S(prof['r'], _R1, _R2, 'cos', 1.0, [_R1, _R2])
    sc = jnp.asarray(CubicSpline(prof['r'], Sv).c)
    beta = _BETA

    def gf(xyz):
        r = jnp.sqrt(jnp.sum(xyz ** 2) + 1e-18)
        rc = jnp.clip(r, xs[0], xs[-1])
        a = rt._spline_eval(rc, xs, ac)
        b = rt._spline_eval(rc, xs, bc)
        S = rt._spline_eval(rc, xs, sc)
        n = xyz / jnp.where(r > 0, r, 1.0)
        g = jnp.zeros((4, 4))
        g = g.at[0, 0].set(-jnp.exp(2 * a))
        g = g.at[0, 1].set(-S * beta).at[1, 0].set(-S * beta)
        eb = jnp.exp(2 * b) - 1.0
        gam = jnp.eye(3) + eb * jnp.outer(n, n)
        g = g.at[1:, 1:].set(gam)
        return g

    out = {'source': _SRC, 'beta': beta}
    gf_fd = n3.prof_gfunc(prof, beta, _R1, _R2)
    for seed in (555001, 777001, 999331):
        pts = n3_de.screen_points(seed, n=700)
        necs, wecs, secs, decs, tis = [], [], [], [], []
        for pt in pts:
            That = np.array(rt.that_jax(gf, jnp.asarray(pt)))
            m = vm.hawking_ellis_margins(That[None])
            necs.append(float(m['nec'][0])); wecs.append(float(m['wec'][0]))
            secs.append(float(m['sec'][0])); decs.append(float(m['dec'][0]))
            tis.append(bool(m['typeI'][0]))
        ad = {'nec': min(necs), 'wec': min(wecs), 'sec': min(secs),
              'dec': min(decs), 'typeI': float(np.mean(tis)),
              'worst': min(min(necs), min(wecs), min(secs), min(decs))}
        _, _, mfd = vm.einstein_at_points(gf_fd, pts, h=0.3)
        fd = {'nec': float(np.min(mfd['nec'])),
              'wec': float(np.min(mfd['wec'])),
              'sec': float(np.min(mfd['sec'])),
              'dec': float(np.min(mfd['dec'])),
              'typeI': float(np.mean(mfd['typeI'])),
              'worst': float(np.min(np.minimum(
                  np.minimum(mfd['nec'], mfd['wec']),
                  np.minimum(mfd['sec'], mfd['dec']))))}
        out[f'seed{seed}'] = {'AD': ad, 'FD': fd}
        print(f'seed {seed}: AD worst {ad["worst"]:+.4e} '
              f'(NEC {ad["nec"]:+.3e} DEC {ad["dec"]:+.3e} '
              f'TypeI {ad["typeI"]:.3f}) | FD worst '
              f'{fd["worst"]:+.4e}', flush=True)
    json.dump(out, open('results/n3_ad.json', 'w'), indent=1,
              default=float)
    print('N3 AD DONE', flush=True)


if __name__ == '__main__':
    main()
