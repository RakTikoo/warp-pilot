"""
blob_attack.py — candidate-under-attack protocol for the Track B
blob winner (beta=0.1, NL=5). NOT a verification: an attempt to
BREAK it.
 1. Field anatomy: Vx (shift) plateau along the travel axis —
    does the configuration actually move at ~beta, or did the DE
    quietly remove the motion? ADM shift beta^x = Vx e^{-2B}.
 2. Dense fresh audits: 6000 pts x 3 seeds at h=0.35 / 0.175.
 3. R1-style adversarial point hunt: DE + local polish minimising
    the worst margin and the NEC separately, 60 restarts.
Usage: python3 blob_attack.py results/blob_b0.1_NL5.json
"""
import json, sys, time
import numpy as np
from scipy.optimize import differential_evolution, minimize

_SRC = sys.argv[1]
sys.argv = ['blob', '0.1', '5', '8']  # blob parses argv at import
import blob
import verify_metric as vm

DTYPE = np.float64


def main():
    d = json.load(open(_SRC))
    genes = np.array(d['genes'])
    fields = blob.genes_to_fields(genes)
    gf = blob.make_gfunc(fields)
    out = {'source': _SRC}
    # 1. anatomy along the x axis (y=z=0)
    xs = np.linspace(-38, 38, 39)
    pts = np.stack([xs, np.zeros(39), np.zeros(39)], axis=1)
    kern = blob._kernel(pts); tap = blob._taper(pts)
    A = blob._rbf_eval(fields[0], kern) * tap
    B = blob._rbf_eval(fields[1], kern) * tap
    Vx = blob._rbf_eval(fields[2], kern) * tap
    Vy = blob._rbf_eval(fields[3], kern) * tap
    Vz = blob._rbf_eval(fields[4], kern) * tap
    beta_adm = Vx * np.exp(-2 * B)
    out['axis'] = {'x': xs.tolist(), 'A': A.tolist(), 'B': B.tolist(),
                   'Vx': Vx.tolist(), 'Vy': Vy.tolist(),
                   'Vz': Vz.tolist(), 'beta_adm_x': beta_adm.tolist()}
    core = (np.abs(xs) <= 10)
    out['interior_beta_adm_mean'] = float(np.mean(beta_adm[core]))
    out['interior_Vx_mean'] = float(np.mean(Vx[core]))
    print(f'anatomy: interior (|x|<=10) Vx mean '
          f'{out["interior_Vx_mean"]:+.4f}, ADM shift mean '
          f'{out["interior_beta_adm_mean"]:+.4f}, A range '
          f'[{A.min():+.3f},{A.max():+.3f}], B range '
          f'[{B.min():+.3f},{B.max():+.3f}]', flush=True)
    # 2. dense fresh audits
    for seed in (111, 222, 333):
        pts = blob.screen_points(seed, n=6000)
        for h in (0.35, 0.175):
            w, tI = blob.audit_worst(fields, pts, h=h)
            out[f'dense_seed{seed}_h{h}'] = {'worst': w, 'typeI': tI}
            print(f'dense seed={seed} h={h}: worst {w:+.4e} '
                  f'TypeI {tI:.4f}', flush=True)
    # 3. adversarial hunt: minimise worst margin pointwise
    def worst_at(p):
        _, _, m = vm.einstein_at_points(gf, np.array([p]), h=0.3)
        return float(np.min(np.minimum(
            np.minimum(m['nec'], m['wec']),
            np.minimum(m['sec'], m['dec']))))
    def nec_at(p):
        _, _, m = vm.einstein_at_points(gf, np.array([p]), h=0.3)
        return float(m['nec'][0])
    best = {'worst': 1e9, 'nec': 1e9}
    rng = np.random.default_rng(7)
    t0 = time.time()
    for trial in range(60):
        p0 = rng.uniform(-30, 30, 3)
        for name, fn in (('worst', worst_at), ('nec', nec_at)):
            r = minimize(fn, p0, method='Nelder-Mead',
                         options={'maxiter': 300, 'xatol': 0.05,
                                  'fatol': 1e-9})
            if r.fun < best[name]:
                best[name] = float(r.fun)
                best[name + '_at'] = r.x.tolist()
    out['adversarial'] = best
    out['adv_elapsed_s'] = time.time() - t0
    print(f"adversarial: worst margin found {best['worst']:+.4e} at "
          f"{best.get('worst_at')}; NEC {best['nec']:+.4e} at "
          f"{best.get('nec_at')}", flush=True)
    json.dump(out, open('results/blob_attack.json', 'w'), indent=1,
              default=float)
    print('BLOB ATTACK DONE', flush=True)


if __name__ == '__main__':
    main()
