"""
n3_attack.py — candidate-under-attack audits for the N3 run-2
winner (conditions-first, beta=0.1, M=10, (10,30), finals
+6.3e-7). Dense fresh audits with per-margin breakdown, a
dedicated support-tail audit (r in [30, 44] — the prescription
support ends at RMAX=44), and an R1-style adversarial point hunt.
The warpax AD cross-check and R2 symbolic path run separately.
Usage: python3 n3_attack.py results/n3_b0.1_M10.0_10-30_run2.json
"""
import json, sys, time
import numpy as np
from scipy.optimize import minimize

_SRC = sys.argv[1]
sys.argv = ['n3_de', '0.1', '10', '10', '30']  # n3_de parses argv
import n3_de
import n3_invert as n3
import verify_metric as vm

DTYPE = np.float64


def margins_at(gf, pts, h):
    _, _, m = vm.einstein_at_points(gf, pts, h=h)
    return {k: float(np.min(m[k])) for k in
            ('nec', 'wec', 'sec', 'dec')}, float(np.mean(m['typeI']))


def main():
    d = json.load(open(_SRC))
    genes = np.array(d['genes'])
    rho_s, pt_s = n3_de.prescription(genes)
    prof = n3.solve_shell(rho_s, pt_s, R1=10.0, R2=30.0, Nr=4001,
                          rmax=44.0, rout=44.0)
    gf = n3.prof_gfunc(prof, 0.1, 10.0, 30.0)
    out = {'source': _SRC, 'shoot_F': prof['shoot_F'],
           'M_recovered': prof['M'], 'umin': prof['umin'],
           'realisation': n3.realisation_residual(prof)}
    print(f"rebuilt: M {prof['M']:.5f} umin {prof['umin']:.3f} "
          f"shoot_F {prof['shoot_F']:.2e}", flush=True)
    # dense fresh audits, per-margin
    for seed in (555001, 777001, 999331):
        pts = n3_de.screen_points(seed, n=3000)
        for h in (0.3, 0.15):
            mm, tI = margins_at(gf, pts, h)
            out[f'dense_seed{seed}_h{h}'] = {**mm, 'typeI': tI}
            print(f'dense seed={seed} h={h}: NEC {mm["nec"]:+.4e} '
                  f'WEC {mm["wec"]:+.4e} SEC {mm["sec"]:+.4e} '
                  f'DEC {mm["dec"]:+.4e} TypeI {tI:.4f}', flush=True)
    # tail audit: support boundary region
    rng = np.random.default_rng(424242)
    dirs = rng.normal(size=(900, 3))
    dirs /= np.linalg.norm(dirs, axis=1)[:, None]
    pts = rng.uniform(29.0, 44.5, 900)[:, None] * dirs
    for h in (0.3, 0.15):
        mm, tI = margins_at(gf, pts.astype(DTYPE), h)
        out[f'tail_h{h}'] = {**mm, 'typeI': tI}
        print(f'tail h={h}: NEC {mm["nec"]:+.4e} WEC {mm["wec"]:+.4e} '
              f'SEC {mm["sec"]:+.4e} DEC {mm["dec"]:+.4e} '
              f'TypeI {tI:.4f}', flush=True)
    # cavity audit r in [0.5, 10]
    dirs = rng.normal(size=(600, 3))
    dirs /= np.linalg.norm(dirs, axis=1)[:, None]
    pts = rng.uniform(0.5, 10.0, 600)[:, None] * dirs
    mm, tI = margins_at(gf, pts.astype(DTYPE), 0.3)
    out['cavity_h0.3'] = {**mm, 'typeI': tI}
    print(f'cavity: NEC {mm["nec"]:+.4e} WEC {mm["wec"]:+.4e} '
          f'SEC {mm["sec"]:+.4e} DEC {mm["dec"]:+.4e}', flush=True)
    # R1-style adversarial hunt (all-margin + NEC), 96 restarts
    def worst_at(p):
        _, _, m = vm.einstein_at_points(gf, np.array([p]), h=0.3)
        return float(np.min(np.minimum(
            np.minimum(m['nec'], m['wec']),
            np.minimum(m['sec'], m['dec']))))
    def nec_at(p):
        _, _, m = vm.einstein_at_points(gf, np.array([p]), h=0.3)
        return float(m['nec'][0])
    best = {'worst': 1e9, 'nec': 1e9}
    rng = np.random.default_rng(11)
    t0 = time.time()
    for _ in range(96):
        p0 = rng.uniform(2.0, 42.0) * \
            (lambda v: v / np.linalg.norm(v))(rng.normal(size=3))
        for name, fn in (('worst', worst_at), ('nec', nec_at)):
            r = minimize(fn, p0, method='Nelder-Mead',
                         options={'maxiter': 250, 'xatol': 0.05,
                                  'fatol': 1e-10})
            if r.fun < best[name]:
                best[name] = float(r.fun)
                best[name + '_at'] = r.x.tolist()
    out['adversarial'] = best
    out['adv_elapsed_s'] = time.time() - t0
    print(f"adversarial: worst {best['worst']:+.4e} at "
          f"{best.get('worst_at')}; NEC {best['nec']:+.4e} at "
          f"{best.get('nec_at')}", flush=True)
    json.dump(out, open('results/n3_attack.json', 'w'), indent=1,
              default=float)
    print('N3 ATTACK DONE', flush=True)


if __name__ == '__main__':
    main()
