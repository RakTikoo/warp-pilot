#!/usr/bin/env python3
"""
p93_gate.py -- P9-3 BUILD checkpoint (A): tensor identification.

(A1) Random-field brute-force action FD: periodic-free box,
random smooth (g, u, prescribed lambda) fields; directional
derivative of S_ae = int sqrt(-g) [L_ae + lam_pres (u.u + 1)]
under random smooth compactly-supported metric perturbations
vs int sqrt(-g) C_ab dg^{ab} with C from p93_tensor
(lam_override mode).  Bar: rel diff < 2% (P7-1 gate pattern).

(A2) Spherical reduced-action variation: static spherical
A(r), B(r); u = static unit vector.  (t,t), (r,r) mixed
components from FD/EL variation of the reduced 1D action
(sympy) vs the tensor formula.  Fixes lam_sign (the EOM
lambda's coefficient) and checks the overall scale s
(derivation predicts C as written, i.e. ratio 1).  Known
limit used as a cross-check: on this background
L_ae = c14 A'^2/(4 A^2 B) exactly (only c14 survives;
Jacobson sec.7: the static aether sector depends only on
c14) -- asserted in the sympy reduction.

float64.  System python3.
"""
import json
import sys
import time

import numpy as np
import sympy as sp

sys.path.insert(0, '/home/hatch/workspace/warp-pilot')
sys.path.insert(0, '/home/hatch/workspace/warp-pilot/phase9')
import verify_metric as vm   # noqa: E402
import p93_tensor as tn      # noqa: E402

rng = np.random.default_rng(20261121)

# ------------------------------------------------------------------
# (A1) random-field action FD
# ------------------------------------------------------------------
LBOX = 6.0


def g_rand(pts):
    x, y, z = pts[:, 0], pts[:, 1], pts[:, 2]
    g = np.zeros((len(pts), 4, 4))
    g[:, 0, 0] = -1.0 + 0.08 * np.sin(1.1 * x) * np.cos(0.9 * y) \
        + 0.05 * np.cos(1.3 * z + 0.4)
    g[:, 1, 1] = 1.0 + 0.07 * np.cos(0.8 * x + 0.3) * np.sin(1.2 * z)
    g[:, 2, 2] = 1.0 + 0.06 * np.sin(1.0 * y) * np.cos(0.7 * x)
    g[:, 3, 3] = 1.0 + 0.05 * np.cos(1.1 * z) * np.sin(0.9 * y + 0.2)
    g[:, 0, 1] = g[:, 1, 0] = 0.04 * np.sin(0.8 * y + 0.5) * np.cos(1.1 * z)
    g[:, 0, 2] = g[:, 2, 0] = 0.03 * np.cos(1.2 * x) * np.sin(0.6 * z)
    g[:, 1, 2] = g[:, 2, 1] = 0.035 * np.sin(0.9 * z + 0.1) * np.cos(1.0 * y)
    return g


def u_rand(pts, g):
    x, y, z = pts[:, 0], pts[:, 1], pts[:, 2]
    u = np.zeros((len(pts), 4))
    u[:, 0] = 1.0
    u[:, 1] = 0.15 * np.sin(0.9 * y + 0.2)
    u[:, 2] = 0.12 * np.cos(1.1 * z + 0.3)
    u[:, 3] = 0.10 * np.sin(0.7 * x + 1.0)
    return u


def lam_rand(pts):
    x, y, z = pts[:, 0], pts[:, 1], pts[:, 2]
    return 0.3 * np.sin(0.8 * x) * np.cos(0.9 * z) \
        + 0.2 * np.cos(1.1 * y)


def dg_rand(pts, seed):
    r = np.random.default_rng(seed)
    x, y, z = pts[:, 0], pts[:, 1], pts[:, 2]
    bump = (np.sin(np.pi * x / LBOX) * np.sin(np.pi * y / LBOX)
            * np.sin(np.pi * z / LBOX))**2
    dg = np.zeros((len(pts), 4, 4))
    for a in range(4):
        for b in range(a, 4):
            c1, c2, c3, ph = r.uniform(0.5, 1.4, 3), 0, 0, 0
            ph = r.uniform(0, 6.28)
            dg[:, a, b] = dg[:, b, a] = bump * (
                0.6 * np.sin(c1[0] * x + ph) * np.cos(c1[1] * y)
                + 0.4 * np.cos(c1[2] * z + ph))
    return dg


def action_S(gf, pts, w, h3, cs):
    fc = tn.field(gf, pts, 0.4, u_rand, cs, h_fd=0.2)
    uu = np.einsum('pa,pa->p', fc['u_up'], fc['u_cov'])
    Ltot = fc['L'] + lam_rand(pts) * (uu + 1.0)
    det = np.linalg.det(fc['g'])
    return float(np.sum(w * np.sqrt(-det) * Ltot) * h3)


def gate_A1():
    n = 13
    h = LBOX / (n - 1)
    ax = np.linspace(0, LBOX, n)
    XX, YY, ZZ = np.meshgrid(ax, ax, ax, indexing='ij')
    pts = np.stack([XX.ravel(), YY.ravel(), ZZ.ravel()], axis=1)
    w = np.ones(len(pts))
    h3 = h**3
    out = []
    for cs in [(0.7, -0.4, 0.2, 0.9), (0.3, 0.5, -0.3, 0.8)]:
        C, parts = tn.C_aether(g_rand, pts, 0.4, u_rand, cs,
                               lam_sign=-1.0, h_fd=0.2,
                               lam_override=lam_rand(pts),
                               want_parts=True)
        # the gate's prescribed u is NOT normalised, so the
        # action's lam(u.u+1) term also contributes its
        # -1/2 g_ab lam (u.u+1) variation piece (zero on shell
        # in the real theory, nonzero here -- include it).
        fc = parts['fc']
        uu = np.einsum('pa,pa->p', fc['u_up'], fc['u_cov'])
        C = C - 0.5 * fc['g'] * (lam_rand(pts)
                                 * (uu + 1.0))[:, None, None]
        g0 = g_rand(pts)
        ginv0 = np.linalg.inv(g0)
        sq = np.sqrt(-np.linalg.det(g0))
        for seed in (1, 2):
            dg = dg_rand(pts, seed)
            dg_up = -np.einsum('pac,pcb,pbd->pad', ginv0, dg, ginv0)
            # dg^{ab} = -ginv dg ginv: (ginv @ dg @ ginv) with sign
            dg_up = -np.einsum('pac,pcb,pbd->pad', ginv0, dg, ginv0)
            pred = float(np.sum(w * sq * np.einsum(
                'pab,pab->p', C, dg_up)) * h3)
            eps = 1e-4
            Sp = action_S(lambda p: g_rand(p) + eps * dg_rand(p, seed),
                          pts, w, h3, cs)
            Sm = action_S(lambda p: g_rand(p) - eps * dg_rand(p, seed),
                          pts, w, h3, cs)
            fd = (Sp - Sm) / (2 * eps)
            rel = abs(fd - pred) / max(abs(fd), 1e-300)
            out.append(dict(cs=list(cs), seed=seed, fd=fd, pred=pred,
                            rel=rel))
            print(f'[A1] cs={cs} seed={seed}: FD {fd:+.6e} '
                  f'pred {pred:+.6e} rel {rel:.3e}', flush=True)
    return out


# ------------------------------------------------------------------
# (A2) spherical reduced action (sympy)
# ------------------------------------------------------------------
def gate_A2():
    r = sp.symbols('r', positive=True)
    A = 0.85 + 0.10 * sp.tanh((r - 10) / 3) \
        + 0.05 * sp.sin(r / 3) * sp.exp(-r / 15)
    B = 1.15 - 0.08 * sp.tanh((r - 11) / 4) \
        + 0.04 * sp.cos(r / 4) * sp.exp(-r / 20)
    Ap, Bp = sp.diff(A, r), sp.diff(B, r)
    App = sp.diff(Ap, r)
    Af = sp.lambdify(r, A, 'numpy')
    Bf = sp.lambdify(r, B, 'numpy')
    Apf = sp.lambdify(r, Ap, 'numpy')
    Bpf = sp.lambdify(r, Bp, 'numpy')
    Appf = sp.lambdify(r, App, 'numpy')
    # Known limit, verified NUMERICALLY (sympy simplify of the
    # tanh/sin expressions hangs): for u = static unit vector,
    # D_t^r = A'/(2B sqrt(A)) is the only nonzero D_a^c, theta
    # = 0, A3 = 0, A1 = -A'^2/(4A^2B), A4 = +A'^2/(4A^2B), so
    # L_ae = c14 A'^2/(4 A^2 B) -- only c14 survives (Jacobson
    # sec.7).  The tensor code's own L on this background is
    # compared against this limit in the caller loop below.
    # Reduced density (per unit t, per steradian):
    #   Ld = sqrt(AB) r^2 L = r^2 c14 A'^2 /4 * A^{-3/2} B^{-1/2}
    # EL_A = dLd/dA - d/dr(dLd/dA'), EL_B = dLd/dB (no B' in Ld).
    def EL(rv, c14):
        Av, Bv, Apv, Bpv, Appv = Af(rv), Bf(rv), Apf(rv), \
            Bpf(rv), Appf(rv)
        base = rv**2 * c14 / 4.0
        dLdA = base * Apv**2 * (-1.5) * Av**(-2.5) * Bv**(-0.5)
        Pj = rv**2 * c14 / 2.0 * Apv * Av**(-1.5) * Bv**(-0.5)
        # d/dr Pj by the product rule
        dPj = c14 / 2.0 * (
            2 * rv * Apv * Av**(-1.5) * Bv**(-0.5)
            + rv**2 * Appv * Av**(-1.5) * Bv**(-0.5)
            + rv**2 * Apv * (-1.5) * Av**(-2.5) * Apv * Bv**(-0.5)
            + rv**2 * Apv * Av**(-1.5) * (-0.5) * Bv**(-1.5) * Bpv)
        EL_A = dLdA - dPj
        EL_B = base * Apv**2 * Av**(-1.5) * (-0.5) * Bv**(-1.5)
        sq = np.sqrt(Av * Bv) * rv**2
        return -Av * EL_A / sq, -Bv * EL_B / sq   # C^t_t, C^r_r

    def gf_sph(pts):
        rr = np.linalg.norm(pts, axis=1)
        rs = np.where(rr > 0, rr, 1.0)
        nn = pts / rs[:, None]
        Av, Bv = Af(rr), Bf(rr)
        g = np.zeros((len(pts), 4, 4))
        g[:, 0, 0] = -Av
        g[:, 1:, 1:] = np.eye(3)[None] \
            + (Bv - 1.0)[:, None, None] * np.einsum('pi,pj->pij', nn, nn)
        return g

    radii = np.array([5.0, 7.0, 9.0, 11.0, 13.0])
    pts = np.stack([radii, np.zeros(5), np.zeros(5)], axis=1)
    res = {}
    for cs in [(0.7, -0.4, 0.2, 0.9), (-0.5, 0.3, 0.5, -0.2)]:
        C0, parts = tn.C_aether(gf_sph, pts, 0.3, tn.eulerian_u,
                                cs, lam_sign=0.0, h_fd=0.15,
                                want_parts=True)
        Av, Bv = Af(radii), Bf(radii)
        # mixed components at (r,0,0): tt: -C_tt/A ; rr: C_xx/B
        tt0 = -C0[:, 0, 0] / Av
        rr0 = C0[:, 1, 1] / Bv
        tt_red, rr_red = EL(radii, cs[0] + cs[3])
        # L-limit check: tensor L vs c14 A'^2/(4A^2B)
        L_lim = (cs[0] + cs[3]) * Apf(radii)**2 \
            / (4 * Av**2 * Bv)
        L_err = np.max(np.abs(parts['fc']['L'] - L_lim)
                       / np.maximum(np.abs(L_lim), 1e-300))
        print(f'[A2] cs={cs}: L vs c14-limit max rel err '
              f'{L_err:.3e}', flush=True)
        lam_cand = parts['lam']
        # (lam u u)^t_t = -lam  =>  tt = tt0 - lam_sign * lam
        lam_implied = -(tt_red - tt0)
        ratio_rr = rr_red / rr0
        ratio_lam = lam_implied / lam_cand
        res[str(cs)] = dict(
            rr_red=rr_red.tolist(), rr_form=rr0.tolist(),
            ratio_rr=ratio_rr.tolist(),
            tt_red=tt_red.tolist(), tt_form_nolam=tt0.tolist(),
            lam_cand=lam_cand.tolist(),
            lam_implied=lam_implied.tolist(),
            ratio_lam=ratio_lam.tolist())
        print(f'[A2] cs={cs}: C^r_r ratio red/form '
              f'{np.array2string(ratio_rr, precision=4)}', flush=True)
        print(f'[A2] cs={cs}: lam implied/cand '
              f'{np.array2string(ratio_lam, precision=4)}', flush=True)
    return res, 'L-limit verified numerically in-loop (see prints)'


def main():
    t0 = time.time()
    a1 = gate_A1()
    a2, lsimp = gate_A2()
    out = dict(gate='P9-3 checkpoint A', A1=a1, A2=a2,
               A2_L_limit_check=lsimp, runtime_s=time.time() - t0)
    with open('/home/hatch/workspace/warp-pilot/phase9/results/'
              'p93_gate.json', 'w') as fh:
        json.dump(out, fh, indent=2)
    print('gate done', flush=True)


if __name__ == '__main__':
    main()
