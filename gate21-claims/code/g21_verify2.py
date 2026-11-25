#!/usr/bin/env python3
"""GATE-21 follow-up probes: (i) the actual Type-I flip mechanism at
site 44 (eigenvalue structure at d=0 across the bracket); (ii) a fair
robustness comparison -- both witnesses (lambda=0.10 and Gate-20's
lambda_val) under the same random-perturbation scales, through the
same path. SPECULATIVE. Frame of record: venv + Phase 166 pin.
"""
import json, sys
import numpy as np

WP = '/home/hatch/workspace/warp-pilot'
sys.path.insert(0, WP + '/phase186/work')
sys.path.insert(0, WP + '/phase176/work')
sys.path.insert(0, WP + '/phase171/work')
import p186_common as P186
import p1763_common as X
import p1711_common as C

LAM_VAL = 0.019992372183091776
basis = X.BASES['Ea']
out = {}

# ---- (i) flip mechanism at d=0: eigenvalue diagnostics at site 44 ----
mech = {}
for lam in (0.10, 0.11, 0.1452):
    gf = X.make_gf_enriched(np.zeros(72), basis)
    Ea = C.Ea_on(gf)
    E1, g = C.species_E(gf, C.coeff0, +lam)
    E2, _ = C.species_E(gf, C.coeff0, -lam)
    That = P186.L.that_in_frame(g, (Ea + E1 + E2) / C.EIGHT_PI, C.pts)
    fr = P186.L.flux_reads(That)
    M = That[44].copy(); M[0, :] *= -1.0
    ev = np.linalg.eigvals(M)
    mech[str(lam)] = dict(typeI44=bool(fr['typeI'][44]),
                          ev_imag_max44=float(fr['ev_imag_max'][44]),
                          eigvals44=[complex(x) for x in ev],
                          D44=float(fr['D_r'][44]), q44=float(fr['q_r'][44]))
out['flip_mechanism'] = mech

# ---- (ii) robustness, both witnesses, same scales ----------------------
_, scalesv = P186.res0_scales_at(LAM_VAL)
STORED_Q = [1.0032717740717199, 1.1029635664194024]
d178 = np.load(WP + '/phase178/work/p1781_state.npz')['d_final']
S = np.load(WP + '/phase186/work/p186_J_coupled_lam010.npz')
scales010 = S['scales']
d010 = np.load(WP + '/phase186/work/p186_opt_lam010_state.npz')['d_final']
QREF010 = [0.9923385740704013, 0.9223100532072909]

def probe(d, lam, sc, qref, scale, rng):
    p = rng.standard_normal(72); p *= scale / np.linalg.norm(p)
    dd = d + p
    cl = P186.exact_closure(dd, lam, sc)
    fr = P186.reads_lam(X.make_gf_enriched(dd, basis), lam)
    return dict(closure=cl, dq41=float(fr['q_r'][41] - qref[0]),
                dq44=float(fr['q_r'][44] - qref[1]),
                typeI_sites=[bool(fr['typeI'][41]), bool(fr['typeI'][44])],
                count=int(np.sum(fr['typeI'])))

rng = np.random.default_rng(20261123)
rob = {}
for scale in (1e-5, 1e-4):
    for trial in range(2):
        rob[f'lam010_{scale}_{trial}'] = probe(d010, 0.10, scales010,
                                              QREF010, scale, rng)
        rob[f'lamval_{scale}_{trial}'] = probe(d178, LAM_VAL, scalesv,
                                               STORED_Q, scale, rng)
out['robustness_fair'] = rob
json.dump(out, open(WP + '/gate21/work/g21_verify2_out.json', 'w'),
          indent=1, default=str)
print(json.dumps(out, indent=1, default=str))
print('G21 VERIFY2 DONE')
