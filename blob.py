"""
blob.py — TRACK B: free-form 3D blob (no imposed symmetry).

Metric-side fields on a Gaussian-RBF control lattice over a box
[-L, L]^3, L = 40: lapse field A(x), conformal field B(x)
(gamma_ij = exp(2B) delta_ij), shift components Vx, Vy, Vz
(g_ti = -V_i). RBF kernels => fields are Cinf (the auditor needs
two metric derivatives; a trilinear lattice would inject
stencil-scale artefacts — the Track P third artefact class).
Genes = control values; boundary control planes pinned to 0
(Minkowski). Fields are multiplied by a C2 taper reaching EXACT
zero at |x_i| = L-2 per axis, so the metric is exactly flat in a
boundary shell and outside the box. NO spherical or axial symmetry
anywhere; the only fixed structure is the travel axis (x) in the
seeding and the taper.

DE (Track P protocol): objective = worst all-observer margin on a
dense space-filling RANDOM 3D screen (no radial/angular grids);
arbiters re-randomised at h and h/2 for finals; ADM mass of any
winner measured post-hoc by grid integration of the Eulerian
density (reported, not targeted — the beta=0.1 comparison reads
margin-vs-measured-mass against the spherical M=10 boundary).
Seeding: one row samples the spherical (10,30) M=10 forward config
(the located beta=0.1 wall) onto the lattice — blurred by the
lattice resolution, a known handicap, reported as such.

Usage: python3 blob.py BETA [NL] [maxiter]
float64 everywhere.
"""
import json, sys, time
import numpy as np
from scipy.interpolate import BSpline
from scipy.optimize import differential_evolution

import shell as sh
import verify_metric as vm

DTYPE = np.float64
BETA = float(sys.argv[1]) if len(sys.argv) > 1 else 0.1
NL = int(sys.argv[2]) if len(sys.argv) > 2 else 5
MAXITER = int(sys.argv[3]) if len(sys.argv) > 3 else 20
L = 40.0
NFIELD = 5
N_GENES = NFIELD * NL ** 3

# Control lattice centres and Gaussian RBF kernel (Cinf fields;
# feature scale = node spacing, stated honestly as the lattice
# resolution). The taper enforces exact asymptotic flatness.
_ctrl = np.linspace(-L, L, NL)
_CENTRES = np.stack(np.meshgrid(_ctrl, _ctrl, _ctrl,
                                indexing='ij'), axis=-1).reshape(-1, 3)
_SIGMA = (2.0 * L / (NL - 1)) * 0.9 if NL > 1 else L


def _kernel(pts):
    a2 = np.sum(pts ** 2, axis=1)[:, None]
    c2 = np.sum(_CENTRES ** 2, axis=1)[None, :]
    d2 = np.maximum(a2 + c2 - 2.0 * pts @ _CENTRES.T, 0.0)
    return np.exp(-d2 / (2.0 * _SIGMA ** 2))


def _rbf_eval(ctrl_vals, kern):
    # normalised RBF (partition of unity): constant fields exact,
    # coefficients read as approximate field values at the nodes
    return (kern @ ctrl_vals.reshape(-1)) / kern.sum(axis=1)


def _taper(pts):
    t = np.ones(len(pts))
    for i in range(3):
        u = np.clip((np.abs(pts[:, i]) - (L - 8.0)) / 6.0, 0.0, 1.0)
        t *= 1.0 - sh.smootherstep(u)
    return t


def genes_to_fields(genes):
    f = genes.reshape(NFIELD, NL, NL, NL).copy()
    for k in range(NFIELD):
        f[k][0, :, :] = f[k][-1, :, :] = 0.0
        f[k][:, 0, :] = f[k][:, -1, :] = 0.0
        f[k][:, :, 0] = f[k][:, :, -1] = 0.0
    return f


def make_gfunc(fields):
    def gfunc(pts):
        pts = np.asarray(pts, dtype=DTYPE)
        P = len(pts)
        tap = _taper(pts)
        kern = _kernel(pts)
        A = _rbf_eval(fields[0], kern) * tap
        B = _rbf_eval(fields[1], kern) * tap
        Vx = _rbf_eval(fields[2], kern) * tap
        Vy = _rbf_eval(fields[3], kern) * tap
        Vz = _rbf_eval(fields[4], kern) * tap
        g = np.zeros((P, 4, 4), dtype=DTYPE)
        g[:, 0, 0] = -np.exp(2 * A)
        g[:, 0, 1] = g[:, 1, 0] = -Vx
        g[:, 0, 2] = g[:, 2, 0] = -Vy
        g[:, 0, 3] = g[:, 3, 0] = -Vz
        eb = np.exp(2 * B)
        for i in range(3):
            g[:, 1 + i, 1 + i] = eb
        return g

    return gfunc


def screen_points(seed, n=300):
    rng = np.random.default_rng(seed)
    pts = rng.uniform(-30.0, 30.0, (n, 3))
    d = rng.normal(size=(n // 2, 3))
    d /= np.linalg.norm(d, axis=1)[:, None]
    pts[:n // 2] = (rng.uniform(6.0, 30.0, n // 2)[:, None] * d)
    return pts.astype(DTYPE)


def audit_worst(fields, pts, h=0.35):
    gf = make_gfunc(fields)
    _, That, m = vm.einstein_at_points(gf, pts, h=h)
    worst = np.minimum(np.minimum(m['nec'], m['wec']),
                       np.minimum(m['sec'], m['dec']))
    return float(np.min(worst)), float(np.mean(m['typeI']))


def grid_mass(fields, N=61, Lbox=36.0):
    """ADM-ish mass: volume integral of Eulerian rho on a grid."""
    gf = make_gfunc(fields)
    ax = np.linspace(-Lbox, Lbox, N)
    h = ax[1] - ax[0]
    X, Y, Z = np.meshgrid(ax, ax, ax, indexing='ij')
    pts = np.stack([X.ravel(), Y.ravel(), Z.ravel()], axis=1)
    g = gf(pts)
    G = vm.einstein_from_grid(g.reshape(N, N, N, 4, 4), h)
    That = vm.eulerian_that(g.reshape(N, N, N, 4, 4),
                            G / vm.EIGHT_PI)
    rho = That[..., 0, 0]
    return float(np.sum(rho) * h ** 3)


_PTS = screen_points(4242)
_G = {'evals': 0}


def _obj(genes):
    _G['evals'] += 1
    fields = genes_to_fields(genes)
    w, _ = audit_worst(fields, _PTS, h=0.35)
    return -w


def seed_genes():
    base = sh.build_shell(10.0, 30.0, 10.0, kind='edgepeaked',
                          params={'wd': 3.0, 'floor': 0.2},
                          s_rho=2.0, s_P=1.16, Nr=4001)
    from scipy.interpolate import CubicSpline
    a_s = CubicSpline(base['r'], base['a'])
    b_s = CubicSpline(base['r'], base['b'])
    f = np.zeros((NFIELD, NL, NL, NL))
    for i, x in enumerate(_ctrl):
        for j, y in enumerate(_ctrl):
            for k, z in enumerate(_ctrl):
                r = np.sqrt(x * x + y * y + z * z)
                rc = min(r, base['r'][-1])
                f[0, i, j, k] = a_s(rc)
                f[1, i, j, k] = b_s(rc)
                f[2, i, j, k] = sh.shift_S(np.array([r]), 10.0, 30.0,
                                           'cos', 1.0, [10.0, 30.0])[0] * BETA
    return f.reshape(-1)


BOUNDS = ([(-0.45, 0.15)] * NL ** 3 + [(-0.05, 0.45)] * NL ** 3
          + [(-1.6, 1.6)] * NL ** 3 + [(-0.4, 0.4)] * NL ** 3
          + [(-0.4, 0.4)] * NL ** 3)


def main():
    t0 = time.time()
    print(f'TRACK B blob: beta={BETA} lattice {NL}^3 x {NFIELD} fields '
          f'= {N_GENES} genes, screen {len(_PTS)} pts', flush=True)
    g_seed = seed_genes()
    fields0 = genes_to_fields(g_seed)
    w0, tI0 = audit_worst(fields0, _PTS, h=0.35)
    print(f'seed (spherical wall blurred on lattice): worst {w0:+.4e} '
          f'TypeI {tI0:.3f}', flush=True)
    rng = np.random.default_rng(13)
    pop = 1 * N_GENES
    init = np.tile(g_seed, (pop, 1)).astype(DTYPE)
    init += rng.normal(0, 0.02, init.shape)
    init[:, 2 * NL ** 3:3 * NL ** 3] += rng.normal(0, 0.05, (pop, NL ** 3))
    lo = np.array([b[0] for b in BOUNDS]); hi = np.array([b[1] for b in BOUNDS])
    init = np.clip(init, lo, hi)
    init[0] = g_seed
    res = differential_evolution(_obj, BOUNDS, maxiter=MAXITER, popsize=1,
                                 mutation=(0.3, 1.2), recombination=0.8,
                                 init=init, polish=False, seed=20261124,
                                 workers=3, updating='deferred')
    genes = res.x
    fields = genes_to_fields(genes)
    out = {'beta': BETA, 'NL': NL, 'screen_worst': float(-res.fun),
           'seed_worst': w0, 'n_evals': int(res.nfev),
           'elapsed_s': time.time() - t0, 'genes': genes.tolist()}
    print(f'DE done: screen worst {-res.fun:+.4e} evals {_G["evals"]} '
          f'{out["elapsed_s"]:.0f}s', flush=True)
    for seed in (555001, 777001):
        pts = screen_points(seed, n=500)
        for h in (0.35, 0.175):
            w, tI = audit_worst(fields, pts, h=h)
            out[f'final_seed{seed}_h{h}'] = {'worst': w, 'typeI': tI}
            print(f'  final seed={seed} h={h}: worst {w:+.4e} '
                  f'TypeI {tI:.3f}', flush=True)
    out['grid_mass'] = grid_mass(fields)
    out['grid_mass_seed'] = grid_mass(fields0)
    print(f'grid mass: winner {out["grid_mass"]:.2f} (seed '
          f'{out["grid_mass_seed"]:.2f}, spherical target 10)', flush=True)
    tag = f'blob_b{BETA}_NL{NL}'
    json.dump(out, open(f'results/{tag}.json', 'w'), indent=1, default=float)
    print('TRACK B DONE', flush=True)


if __name__ == '__main__':
    main()
