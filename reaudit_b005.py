"""Re-audit named-family beta=0.05 near/passing configs on RE-RANDOMISED
dense point sets (Track P anti-artefact rule i) at h=0.3 and h=0.15."""
import numpy as np
import trackL as tl

rng = np.random.default_rng(777)

def rand_points(R1, R2, ndir=26, seed=777):
    r2 = np.random.default_rng(seed)
    i = np.arange(ndir)
    phi = np.arccos(1 - 2 * (i + 0.5) / ndir)
    th = np.pi * (1 + 5 ** 0.5) * i + r2.uniform(0, 0.3)
    dirs = np.stack([np.cos(th) * np.sin(phi), np.sin(th) * np.sin(phi), np.cos(phi)], axis=1)
    W = R2 - R1
    rad = np.linspace(0.25 * R1, 1.35 * R2, 30) + r2.uniform(-0.15, 0.15, 30)
    rad = np.sort(np.concatenate([rad, [R1 + f * W for f in (0.02, 0.05, 0.1, 0.2, 0.35, 0.5, 0.65, 0.8, 0.9, 0.97)]]))
    return np.concatenate([dirs * r for r in rad if r > 0.5])

cases = [
    dict(M=4.0, kind='edgepeaked', params={'wd': 2.0, 'floor': 0.10}, sr=2.0, sp=1.16, ws=[10.0, 20.0]),
    dict(M=6.0, kind='edgepeaked', params={'wd': 3.0, 'floor': 0.20}, sr=2.0, sp=1.16, ws=[10.0, 20.0]),
    dict(M=2.0, kind='edgepeaked', params={'wd': 3.0, 'floor': 0.20}, sr=2.0, sp=1.16, ws=[10.0, 20.0]),  # finalist A at beta .05 for reference
]
for c in cases:
    for seed in (777, 1234):
        pts = rand_points(10.0, 20.0, seed=seed)
        for h in (0.3, 0.15):
            r = tl.eval_shell(10.0, 20.0, c['M'], c['kind'], c['params'], c['sr'], c['sp'],
                              0.05, 'cos', c['ws'], h=h, pts=pts)
            print(f"M={c['M']} wd={c['params']['wd']} seed={seed} h={h}: worst={r['worst']:+.4e} "
                  f"({r['worst_kind']} @r={r['worst_radius']:.2f}) nec={r['nec']:+.3e} tI={r['typeI_frac_sig']:.3f} nsig={r['n_sig']}", flush=True)
