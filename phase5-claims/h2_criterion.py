#!/usr/bin/env python3
"""
h2_criterion.py -- H2 deciding computations.

CRITERION (stated in CHECKPOINT5.md before these runs): a classical
gravity-sector term can supply a throat's NEC violation while
remaining healthy iff the CROSSING FUNCTIONAL (the combination whose
sign the geometry forces to be negative) is NOT SLAVED to the
perturbation-health functionals -- i.e. the map from the theory's
free functions to (crossing, health) has rank >= 2 at the crossing
point. Rank 1 with health fixing the sign = anti-aligned/forbidden.

Computation 1 (scalar-tensor instance, MRV class, A=B=1):
  gamma = 2 (G4 - 2 X G4X) identically (F4 cancels). Hence:
  - Horndeski (F4 = 0): gamma = H identically -> rank 1 -> the
    crossing gamma < 0 IS the odd-sector ghost H < 0. Forbidden.
  - Beyond-Horndeski: H - gamma = 2 F4 pi'^4, an independent
    function -> rank 2 -> allowed.
  Numerical rank demonstration on the MRV background: rescale
  (f40, f41) -> lam (f40, f41): gamma must be INVARIANT and
  H - gamma must scale by lam.

Computation 2 (f(R) = R + alpha R^2 on the MG-1 generalised warp
background): on a fixed background the required-matter tensor is
EXACTLY affine in alpha (F = 1 + 2 alpha R, f = R + alpha R^2,
nabla F = 2 alpha nabla R). Health (no tachyon f_RR = 2 alpha > 0,
no ghost f_R > 0 on the branch connected to GR) pins alpha > 0.
Deciding number: the slope M1 of the NEC margin contraction
rho + p_i* at the GR-worst sample point along its binding
direction i*. M1 < 0 => the correction's supply is slaved
negative for every healthy alpha => anti-aligned (rank 1).
Also: global min NEC margin vs alpha (MG-1 monotonicity check).

float64 throughout (JAX x64 enabled by mg1_fr's module setup if
present; we set it explicitly).
"""
import json
import sys
import numpy as np

sys.path.insert(0, '/home/hatch/workspace/warp-pilot/phase3')
sys.path.insert(0, '/home/hatch/workspace/warp-pilot/phase5')
sys.path.insert(0, '/home/hatch/workspace/warp-pilot')

import p31_horndeski as p31
import h1_engine as eng

TAU = 10.0
out = {}

# ---------------- Computation 1: scalar-tensor rank ----------------
def mrv_bg(r):
    J = np.sqrt(r**2 + TAU**2)
    return J, r / J, TAU**2 / J**3, TAU * np.arcsinh(r / TAU), TAU / J, -TAU * r / J**3

r = np.linspace(-60, 60, 6001)
base = dict(g40=lambda pi: p31.g40_s(pi / TAU), g41=lambda pi: p31.g41_s(pi / TAU),
            f40=lambda pi: p31.f40_s(pi / TAU), f41=lambda pi: p31.f41_s(pi / TAU),
            f2=lambda pi: p31.f2_s(pi / TAU), f1=lambda pi: p31.f1_s(pi / TAU),
            f0=lambda pi: p31.f0_s(pi / TAU))
res1 = {}
for lam in (0.0, 0.5, 1.0, 2.0):
    th = dict(base)
    th['f40'] = lambda pi, lam=lam: lam * p31.f40_s(pi / TAU)
    th['f41'] = lambda pi, lam=lam: lam * p31.f41_s(pi / TAU)
    d = eng.assemble(r, *mrv_bg(r), th)
    cf = eng.coefficients(d)
    i0 = int(np.argmin(np.abs(r)))
    res1[f'lam={lam}'] = dict(
        gamma_throat=float(cf['gamma'][i0]),
        H_throat=float(cf['calH'][i0]),
        H_minus_gamma_throat=float(cf['calH'][i0] - cf['gamma'][i0]),
        gamma_max_dev_across_domain=float(np.max(np.abs(cf['gamma'] - res1['lam=1.0']['gamma_profile']))) if lam != 1.0 and 'lam=1.0' in res1 else None,
    )
    if lam == 1.0:
        res1['lam=1.0']['gamma_profile'] = cf['gamma']
for lam in ('0.0', '0.5', '2.0'):
    d = eng.assemble(r, *mrv_bg(r), {**base,
                                     'f40': lambda pi, lam=float(lam): lam * p31.f40_s(pi / TAU),
                                     'f41': lambda pi, lam=float(lam): lam * p31.f41_s(pi / TAU)})
    cf = eng.coefficients(d)
    res1[f'lam={lam}']['gamma_max_dev_vs_lam1'] = float(
        np.max(np.abs(cf['gamma'] - res1['lam=1.0']['gamma_profile'])))
del res1['lam=1.0']['gamma_profile']
out['scalar_tensor_rank'] = res1

# ---------------- Computation 2: f(R) affine slope ----------------
try:
    import jax
    jax.config.update('jax_enable_x64', True)
    import mg1_fr as mg
    import verify_metric as vm

    # MG-1 stage-1 baseline family: R=1, Delta=0.25, eta=0
    R_, Delta = 1.0, 0.25
    pts = mg.sample_points(R_, Delta)
    # choose the config with the best (least negative) GR worst margin
    # among a small set, mirroring mg1_scan's AMPS/VS
    cands = [(0.0, 0.0, 1.0), (0.3, 0.3, 1.0), (0.0, 0.0, 2.0), (0.3, 0.0, 1.5)]
    best = None
    for (aA, aC, v) in cands:
        b = mg.audit_config_fast(v, R_, Delta, aA, aC, 0.0, 0.0, pts)
        if best is None or b['worst_m'] > best[0]['worst_m']:
            best = (b, (aA, aC, v))
    base_row, (aA, aC, v) = best
    Rstar = base_row['R_absmax']
    gf = mg.make_metric(v, R_, Delta, aA, aC, 0.0)

    def that_m_at(alpha):
        Tm, Teff, Rsc, F = mg.tensors_at_points(gf, pts, alpha)
        Tm = np.asarray(Tm)
        g = np.stack([np.asarray(gf(p)) for p in pts])
        return np.stack([vm.eulerian_that(g[i], Tm[i]) for i in range(len(pts))]), np.asarray(Rsc)

    That0, _ = that_m_at(0.0)
    # NEC margins per point at alpha=0 via the programme's judge;
    # find the worst point, then track THAT point's NEC margin
    # (a min of affine functions of alpha) across alpha.
    mm = [vm.hawking_ellis_margins(That0[i]) for i in range(len(pts))]
    nec = np.array([m['nec'] for m in mm])
    iw = int(np.argmin(nec))
    res2 = dict(config=dict(aA=aA, aC=aC, v_s=v, R_star=Rstar,
                            GR_worst_m=float(base_row['worst_m'])),
                worst_point=pts[iw].tolist(),
                margin_at_alpha={})
    for ah in (0.0, 0.01, 0.1, 1.0):
        alpha = ah / Rstar if Rstar > 0 else 0.0
        That, _ = that_m_at(alpha)
        margin = float(vm.hawking_ellis_margins(That[iw])['nec'])
        mm_a = [vm.hawking_ellis_margins(That[i]) for i in range(len(pts))]
        res2['margin_at_alpha'][f'ahat={ah}'] = dict(
            fixed_point_dir_margin=margin,
            global_min_nec=float(np.min([m['nec'] for m in mm_a])),
            alpha=float(alpha))
    m0 = res2['margin_at_alpha']['ahat=0.0']['fixed_point_dir_margin']
    m1 = res2['margin_at_alpha']['ahat=0.01']['fixed_point_dir_margin']
    m2 = res2['margin_at_alpha']['ahat=0.1']['fixed_point_dir_margin']
    res2['slope_M1_from_0_to_0.01'] = float((m1 - m0) / (0.01 / Rstar))
    res2['slope_M1_from_0_to_0.1'] = float((m2 - m0) / (0.1 / Rstar))
    res2['affine_consistency'] = float(
        abs((m2 - m0) / (0.1 / Rstar) - (m1 - m0) / (0.01 / Rstar)))
    out['fR_affine_slope'] = res2
except Exception as e:
    out['fR_affine_slope'] = dict(error=repr(e))

with open('/home/hatch/workspace/warp-pilot/phase5/results/h2_criterion.json', 'w') as fh:
    json.dump(out, fh, indent=2)
print(json.dumps(out, indent=2)[:3500])
