#!/usr/bin/env python3
"""
g41_calibrate.py -- Gate-41 calibrations. ALL must pass
before any deciding read is quoted.

C-0 vectors: A2's K = 33 vectors in p344_confirmation.json
     vs p344_state_A2.json final incumbent.
C-1 trivial limits: zero profiles -> T == 0 exactly.
C-2 FD path: the gate's analytic tensor vs a 4-D centred-FD
     Einstein tensor built from the metric function alone,
     at sample points of the A2 anchor and both centres.
C-3 density-split identity: Eulerian rho from the gate's
     tensor vs the recorded closed form (R + Q_K)/(16 pi)
     at every SET point of the A2 anchor.
C-4 stationary anchor: the gate's SET-244 read of A2
     (centre path at mu = 1, zero added corrections)
     reproduces the stored A2 confirmation record.
C-5 mu == 1 reduction: centre_profiles(1.0) == A2 totals.
C-6 anchor depth: the gate's adversary polish at A2
     reproduces the stored polished depth.
"""
import json
import sys

import numpy as np

sys.path.insert(0, '/home/hatch/workspace/warp-pilot/gate41/work')
import g41_lib as G  # noqa: E402

OUT = {}


def rec(name, **kw):
    OUT[name] = kw
    print(name, json.dumps(kw, default=str)[:600], flush=True)


# ---------------- C-0: vectors
a, b = G.load_a2_vectors(), G.load_a2_vectors_state()
rec('C-0_vectors', max_diff=float(max(
    np.max(np.abs(x - y)) for x, y in zip(a, b))))

# ---------------- C-1: trivial limits
rng = np.random.default_rng(41)
dirs = rng.normal(size=(8, 3)); dirs /= np.linalg.norm(
    dirs, axis=1)[:, None]
pts = dirs * np.array([10.5, 13.0, 16.0, 19.5, 12.0, 18.0, 11.0,
                       15.0])[:, None]
P = len(pts)
zero = np.zeros(P); one = np.ones(P)
T_flat, _ = G.einstein_from_profiles(
    pts, (zero, zero, zero, one, zero, zero, one, zero, zero))
rec('C-1_flat', max_abs_T=float(np.max(np.abs(T_flat))))

# ---------------- C-2: FD cross-check
def metric_fn_factory(mu, vS, vN, vM, K):
    def fn(x4):
        p = np.asarray(x4[1:], dtype=G.DTYPE)[None, :]
        r = np.linalg.norm(p, axis=1)
        pr = G.profiles_radial(mu, vS, vN, vM, K, r)
        return G.metric_from_profiles(p, pr)[0]
    return fn


sample_pts = np.array([
    [-9.892460780527792, -12.645514806819484, 2.3027702499247202],
    [0.07903746812706403, 16.20172963160452, 10.652664859981932],
    [3.0, 11.0, 6.5], [-14.0, 5.0, 8.0], [12.330081871976182,
    -2.9640809161871493, -10.112165010538996],
    [-0.3943763993356135, 14.770073859618968, -9.714694369165914],
])
cases = [('A2', 1.0, None, None, None, 33),
         ('H1c', G.MU_H1, None, None, None, 17),
         ('H2c', G.MU_H2, None, None, None, 17)]
fd_rows = []
for tag, mu, vS, vN, vM, K in cases:
    fn = metric_fn_factory(mu, vS, vN, vM, K)
    Ta, _ = G.T_at(mu, vS, vN, vM, K, sample_pts)
    for h in (0.05, 0.025):
        Tf = G.einstein_fd(sample_pts, fn, h=h)
        d = np.abs(Ta - Tf)
        scale = np.maximum(np.abs(Ta), 1e-12)
        big = np.abs(Ta) > 1e-6
        fd_rows.append({'case': tag, 'h': h,
                        'max_abs_diff': float(np.max(d)),
                        'max_rel_diff_big': float(
                            np.max(d[big] / scale[big]))})
rec('C-2_fd', rows=fd_rows)

# ---------------- C-3: density split identity (A2 anchor, all SET pts)
worst = 0.0
for rr in G.R_NODES:
    p = G.DIRS162 * rr
    r = np.linalg.norm(p, axis=1)
    pr = G.profiles_radial(1.0, None, None, None, 33, r)
    T, g = G.einstein_from_profiles(p, pr)
    That = G.eulerian_that(g, T)
    rho_t = That[:, 0, 0]
    rho_s = G.rho_split_closed(p, pr)
    worst = max(worst, float(np.max(np.abs(rho_t - rho_s))))
rec('C-3_rho_split', max_abs_diff=worst)

# ---------------- C-5: mu == 1 reduction (before the anchor read)
rr = np.linspace(9.0, 21.0, 241)
pc = G.centre_profiles(1.0, rr)
pa = G.a2_total_profiles(rr)
rec('C-5_mu1_reduction', max_profile_diff=float(max(
    np.max(np.abs(x - y)) for x, y in zip(pc, pa))))

# ---------------- C-4: the A2 anchor SET read
s, aux = G.set_read(1.0, None, None, None, 33)
tgt = {'nec': -0.0002319453132752996, 'dec': -0.00022336932044559818,
       'wec': -0.0021092144017509297, 'sec': -0.002379031965576834,
       'rho': 8.638077678074035e-05}
diffs = {k: float(s[k]['min'] - tgt[k]) for k in tgt}
rec('C-4_anchor', diffs=diffs,
    typeI_count=s['typeI_count'], typeI_target=3535,
    nec_argmin_r=s['nec_argmin_r'], dec_argmin_r=s['dec_argmin_r'],
    nec_argmin_r_target=16.21951219512195,
    dec_argmin_r_target=19.390243902439025)

# ---------------- C-6: anchor depth (adversary polish)
pol = G.adversary_polish(1.0, None, None, None, 33, aux)
rec('C-6_anchor_depth',
    depth=pol['in_region_worst_nec_SAMPLER-M'],
    target=-0.00022644422911711972,
    diff=float(pol['in_region_worst_nec_SAMPLER-M']
               - (-0.00022644422911711972)),
    source=pol['source'], point=pol['point'])

with open('/home/hatch/workspace/warp-pilot/gate41/results/'
          'g41_calibration.json', 'w') as fh:
    json.dump(OUT, fh, indent=1)
print('calibration written')
