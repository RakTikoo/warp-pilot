#!/usr/bin/env python3
"""
h6_floor_identity.py -- H6 verification (pre-registered in
CHECKPOINT5.md): the W1 exoticity floor is an exact identity.

For zero-tidal Morris-Thorne wormholes (Phi = 0), b(r0) = r0,
0 <= b < r, b'r - b = o(1/r):
  I_V^coord = -r0/2 - (1/2) int_{r0}^inf (b/r) dr        <= -r0/2
  I_V^prop  = -r0   + int_{r0}^inf (sqrt(1-b/r) - 1) dr  <= -r0
Derivation (proper): (rho + p_r) 4 pi r^2 / w = (b'r - b)/(2 r w),
(b'r - b)/r^2 = d(b/r)/dr = -2 w w'/... since b/r = 1 - w^2,
d(b/r) = -2w dw, so the integrand is -r w' and
int_{r0}^R -r w' dr = -R w(R) + int_{r0}^R w dr
  = R(1 - w(R)) - r0 + int_{r0}^R (w-1) dr ;  R(1-w(R)) -> 0 (M=0).
Derivation (coordinate): integrand (b'r - b)/(2r) = (1/2)(b' - b/r);
int = (1/2)(b(R) - r0) - (1/2) int (b/r) dr -> -r0/2 - (1/2) int (b/r)
for b(R) -> 0.

Verification: Phase 2's own integrators (w1_wormhole.IV_side_coord /
IV_side_proper) vs independent quadrature of the identity RHS, on
w1's zero-tidal profiles + one in-run random smooth profile.
float64 throughout.
"""
import json
import sys
import numpy as np
from scipy.integrate import quad

sys.path.insert(0, '/home/hatch/workspace/warp-pilot/phase2')
import w1_wormhole as w1

R0 = 1.0


def identity_rhs_coord(bfun):
    val, err = quad(lambda r: bfun(r, R0) / r, R0, np.inf, epsabs=1e-13, limit=200)
    return -R0 / 2 - 0.5 * val, err


def identity_rhs_proper(bfun):
    val, err = quad(lambda r: np.sqrt(max(0.0, 1 - bfun(r, R0) / r)) - 1,
                    R0, np.inf, epsabs=1e-13, limit=200)
    return -R0 + val, err


def main():
    profiles = {}
    for alpha in (-0.5, -1.0, -2.0):
        bf, bpf = w1.prof_power(alpha)
        profiles[f'power_alpha={alpha}'] = (bf, bpf)
    bf, bpf = w1.prof_exp(1.0)
    profiles['exp_lam=1'] = (bf, bpf)
    bf, bpf = w1.prof_coswin(0.5)
    profiles['coswin_w=0.5'] = (bf, bpf)
    # in-run random smooth profile: b = r0 * exp(-(r-r0)/r0 * s(r)),
    # s a positive smooth random-ish function (fixed seed via poly)
    rng = np.random.default_rng(7)
    cs = rng.uniform(0.5, 1.5, size=4)
    def brand(r, r0):
        s = 0.8 + sum(c / (1 + (r / (r0 * (k + 2)))**2) for k, c in enumerate(cs))
        return r0 * np.exp(-(r - r0) / r0 * s)
    def brandp(r, r0):
        h = 1e-6 * max(r, r0)
        return (brand(r + h, r0) - brand(r - h, r0)) / (2 * h)
    profiles['random_smooth'] = (brand, brandp)

    phi0 = w1.phi_zero
    rows = []
    for name, (bf, bpf) in profiles.items():
        ivc_w1 = w1.IV_side_coord(R0, bf, bpf, phi0)[0]
        ivp_w1 = w1.IV_side_proper(R0, bf, bpf, phi0)[0]
        ivc_id, e1 = identity_rhs_coord(bf)
        ivp_id, e2 = identity_rhs_proper(bf)
        row = dict(profile=name,
                   IV_coord_w1=float(ivc_w1), IV_coord_identity=float(ivc_id),
                   IV_coord_rel_dev=float(abs(ivc_w1 - ivc_id) / max(abs(ivc_id), 1e-30)),
                   IV_proper_w1=float(ivp_w1), IV_proper_identity=float(ivp_id),
                   IV_proper_rel_dev=float(abs(ivp_w1 - ivp_id) / max(abs(ivp_id), 1e-30)),
                   coord_floor_ok=bool(ivc_id <= -R0 / 2 + 1e-12),
                   proper_floor_ok=bool(ivp_id <= -R0 + 1e-12))
        rows.append(row)
        print(row, flush=True)
    out = dict(r0=R0, rows=rows,
               all_coord_match=all(r['IV_coord_rel_dev'] < 1e-6 for r in rows),
               all_proper_match=all(r['IV_proper_rel_dev'] < 1e-6 for r in rows),
               all_floors_ok=all(r['coord_floor_ok'] and r['proper_floor_ok'] for r in rows))
    with open('/home/hatch/workspace/warp-pilot/phase5/results/h6_floor_identity.json', 'w') as fh:
        json.dump(out, fh, indent=2)
    print({k: out[k] for k in ('all_coord_match', 'all_proper_match', 'all_floors_ok')})


if __name__ == '__main__':
    main()
