#!/usr/bin/env python3
"""
F4-2: l=0 (spherically symmetric) even modes of the MRV beyond-Horndeski
wormhole (arXiv:1812.07022), from the paper's Appendix B quadratic action
(eq. action_even) at j^2 = l(l+1) = 0.

Method (pre-registered in CHECKPOINT4.md, RELAUNCH):
  * A = B = 1, J = sqrt(r^2+tau^2), tau = 10, background/theory functions
    imported from Phase 3's cross-validated p31_horndeski.py
    (F = G = H = 1; 2P1 - F >= 0.713; c_s2^2 in [0.261, 0.877]).
  * At j^2 = 0 every alpha term in eq. (action_even) carries an explicit
    j^2 factor, so alpha drops out entirely (it also multiplies
    d_a Y_00 = 0 identically). H_1's kinetic term j^2 b_1 H_1^2 vanishes:
    H_1 is a Lagrange multiplier with constraint
        b_2 chi-dot' + b_3 chi-dot + b_4 H_2-dot = 0.
    TREATMENT (stated per brief): the b_i are t-independent, so the
    constraint is d/dt [ b_2 chi' + b_3 chi + b_4 H_2 ] = 0; with
    perturbation boundary conditions (fields and their bracket vanish
    initially / at spatial infinity) the integration constant is zero,
    giving the ALGEBRAIC relation  Q := b_2 chi' + b_3 chi + b_4 H_2 = 0,
    used to eliminate H_2:  H_2 = p chi' + q chi,
    p = -b_2/b_4 = 2 Xi / D,  q = -b_3/b_4 = -b_3 / D,
    D := pi' Xi + 2 J J'  (= -2 a_3 / sqrt(AB) = b_4 / sqrt(B/A)).
  * H_0's constraint (eq. H0 at j^2=0) is then a consistency condition,
    checked explicitly below: on the background (E_B = 0) it integrates
    to d/dr [ a_3 H_2 + a_1 chi' + (a_2 - a_1') chi ] = 0. With the
    Horndeski part of a_2 this bracket is exactly -Q/2 (identity
    b_3 = 2(a_1' - a_2^H)/A, verified to 7e-15), so H_0's constraint
    follows from Q = 0 with vanishing integration function psi(t) = 0
    (localised perturbations). The printed beyond-Horndeski piece
    a_2^BH = 2 sqrt(AB^3) pi'^3 F_4 breaks that identity by exactly
    -4 pi'^3 F_4 in b_3 - 2(a_1' - a_2) (verified to 8e-15): as printed,
    the two constraints would over-determine chi. This is reported as
    an Appendix B inconsistency of the same class as F4-4's E_J finding;
    it does NOT contaminate the reduction, because a_2 enters the action
    only through the H_0 multiplier term, which vanishes on the
    constraints, while the elimination uses the H_1 bracket (the route
    the pre-registration specifies).
  * Substituting H_2(chi) into the remaining action (H_0/H_1 terms
    vanish on their constraints) and integrating by parts in r
    (boundary terms dropped for localised perturbations):
        S = int dt dr [ K0 chi-dot^2 - G0 chi'^2 - M0 chi^2 ],
        K0 = e_1 + c_1 q - (1/2)(c_1 p)',
        G0 = -(e_2 + p c_2 + c_6 p^2),
        M0 = -(e_3 + q c_3 + c_6 q^2 - (1/2)(p c_3 + q c_2 + 2 c_6 p q)').
    Coefficients a_i..e_i are Appendix B at A = B = 1, on background
    (E_A = E_B = 0), H = F = G = 1. c_3 = J^2 dE_B/dpi and
    e_3 = d(EL_pi)/dpi are partial pi-derivatives at fixed kinematics
    and fixed X, computed by shifting the theory functions in
    s = pi/tau (EL_pi from the direct-action route of p44b_elpi.py;
    e_3 = J^2 dE_pi/dpi = dEL_pi/dpi since J is pi-independent).
    K0/G0 do not involve c_3/e_3.
  * Verdict per pre-registration: PASS iff K0 > 0 and G0 > 0 for all r
    (negative only if below -1e-6 relative to scale). M0's sign is
    reported for F4-3 only.

float64 throughout. Derivatives of smooth background functions by
centred FD on the grid; the (c_1 p)' term is assembled pointwise from
p' = (2 Xi' D - 2 Xi D')/D^2 so no differencing ever crosses the
D = 0 pole.
"""
import json
import sys
import numpy as np

sys.path.insert(0, '/home/hatch/workspace/warp-pilot/phase3')
import p31_horndeski as p31

TAU = p31.TAU
RSTAR = 1.772438  # root of D, refined in-run


def build(r, h):
    """All Appendix B coefficients at j^2=0 and the reduced K0, G0."""
    d = p31.theory_on_bg(r)
    Xi, Gamma = p31.Xi_Gamma(d)
    Sig = p31.Sigma_val(d, Xi, Gamma)
    J, Jp, Jpp = d['J'], d['Jp'], d['Jpp']
    pip, pipp, X, Xp = d['pip'], d['pipp'], d['X'], d['Xp']
    F4 = d['F4']
    gr = lambda v: np.gradient(v, h, edge_order=2)
    Xip = gr(Xi)
    D = 2.0 * J * Jp + Xi * pip
    Dp = gr(D)
    # Appendix B, A = B = 1, on-shell (E_A = E_B = 0, F = G = H = 1)
    a1 = Xi
    a3 = -0.5 * D
    a2H = (2 * pip * Xip - 2 * pipp * Xi - 4 * J * Jpp) / (2 * pip)
    a2 = a2H - 2 * pip**3 * F4                    # printed a_2 (minus a_2^BH)
    b1 = 0.5                                      # (1/2) sqrt(B/A) H
    b2 = -2.0 * Xi
    b3 = (2 * pipp * Xi + 4 * J * Jpp) / pip
    b4 = D
    c1 = -Xi - 4 * J * Jp * pip**3 * F4           # -Xi/sqrt(AB) - c_1^BH
    c2 = -J * Jp * Gamma - 2 * J**2 * Sig / pip
    c6 = 0.5 * J**2 * (Sig + pip * Jp / J * Gamma + Jp**2 / J**2)
    e1BH = 4.0 / pip**2 * gr(J * Jp * pip**4 * F4)
    e1 = (0.5 * (-2 * Xip / pip - (Xp / X) * (Xi / pip)
                 + 2 * Jp**2 / X - 2 * Jp**3 / X + 2 * J * Jpp / X)
          - e1BH)
    e2 = -J**2 * Sig / X
    # elimination via the H_1 bracket Q = 0
    p = -b2 / b4
    q = -b3 / b4
    pp_ = (2 * Xip * D - 2 * Xi * Dp) / D**2      # p' pointwise
    c1p_ = gr(c1)
    K0 = e1 + c1 * q - 0.5 * (c1p_ * p + c1 * pp_)
    G0 = -(e2 + p * c2 + c6 * p**2)
    return dict(d=d, Xi=Xi, Gamma=Gamma, Sig=Sig, Xip=Xip, D=D, Dp=Dp,
                a1=a1, a2=a2, a2H=a2H, a3=a3, b1=b1, b2=b2, b3=b3, b4=b4,
                c1=c1, c2=c2, c6=c6, e1=e1, e2=e2, p=p, q=q, K0=K0, G0=G0)


def shifted_EB_EA(r, d, ds):
    """E_B, E_A with theory functions evaluated at s+ds, kinematics/X fixed.
    Returns (EB, EA) arrays; used for dE/dpi by central difference."""
    s_ev = d['s'] + ds
    X = d['X']
    J, Jp, pip = d['J'], d['Jp'], d['pip']
    g40, g41 = p31.g40_s(s_ev), p31.g41_s(s_ev)
    f40, f41 = p31.f40_s(s_ev), p31.f41_s(s_ev)
    f2v = p31.f2_s(s_ev)
    f1v = p31.f1_s(s_ev, f2v)
    f0v = p31.f0_s(s_ev, f1v, f2v)
    F = f0v + f1v * X + f2v * X**2
    FX = f1v + 2.0 * f2v * X
    G4 = 0.5 + g40 + g41 * X
    G4X = g41
    G4pi = p31.dpi(p31.g40_s, s_ev) + p31.dpi(p31.g41_s, s_ev) * X
    G4piX = p31.dpi(p31.g41_s, s_ev)
    F4v = f40 + f41 * X
    F4X = f41
    F4pi = p31.dpi(p31.f40_s, s_ev) + p31.dpi(p31.f41_s, s_ev) * X
    G4pipi = p31.d2pi(p31.g40_s, s_ev) + p31.d2pi(p31.g41_s, s_ev) * X
    dd = dict(d)
    dd.update(F=F, FX=FX, G4=G4, G4X=G4X, G4pi=G4pi, G4piX=G4piX,
              G4pipi=G4pipi, F4=F4v, F4X=F4X, F4pi=F4pi)
    EA, EB, _, _, _ = p31.eom_residuals(dd)
    return EB, EA


def el_pi_shifted(r, d, ds):
    """Unnormalised EL_pi (p44b route) with theory functions at s+ds,
    kinematics fixed. Coarse grid assumed (per-point F_pi loop)."""
    s_ev = d['s'] + ds
    J, Jp, Jpp = d['J'], d['Jp'], d['Jpp']
    q_, w, X = d['pip'], d['pipp'], d['X']
    R = 2.0 * (1.0 - Jp**2) / J**2 - 4.0 * Jpp / J
    Kg = 4.0 * Jp * q_ * w / J + 2.0 * Jp**2 * q_**2 / J**2
    g40, g41 = p31.g40_s(s_ev), p31.g41_s(s_ev)
    f40, f41 = p31.f40_s(s_ev), p31.f41_s(s_ev)
    G4pi = p31.dpi(p31.g40_s, s_ev) + p31.dpi(p31.g41_s, s_ev) * X
    G4piX = p31.dpi(p31.g41_s, s_ev)
    G4X = g41
    F4v = f40 + f41 * X
    F4X = f41
    F4pi = p31.dpi(p31.f40_s, s_ev) + p31.dpi(p31.f41_s, s_ev) * X
    Fpi = np.empty_like(r)
    for i in range(len(r)):
        X0 = X[i]
        def F_of_s(ss, X0=X0):
            f2v = p31.f2_s(np.atleast_1d(ss))
            f1v = p31.f1_s(np.atleast_1d(ss), f2v)
            f0v = p31.f0_s(np.atleast_1d(ss), f1v, f2v)
            return f0v + f1v * X0 + f2v * X0**2
        Fpi[i] = float(p31.dpi(lambda ss: F_of_s(ss),
                               np.atleast_1d(s_ev[i]))[0])
    ds_dpi = J**2 * Fpi + J**2 * (G4pi * R + G4piX * Kg) \
        + 2.0 * Jp**2 * q_**4 * F4pi
    ds_dq = (-J**2 * q_ * (p31.f1_s(s_ev, p31.f2_s(s_ev))
                           + 2.0 * p31.f2_s(s_ev) * X)
             + J**2 * (-q_ * G4X * R
                       + G4X * (4.0 * Jp * w / J + 4.0 * Jp**2 * q_ / J**2))
             + 2.0 * Jp**2 * q_**3 * (4.0 * F4v - q_**2 * F4X))
    ds_dw = 4.0 * J * Jp * q_ * G4X
    hh = r[1] - r[0]
    EL = (ds_dpi - np.gradient(ds_dq, hh, edge_order=2)
          + np.gradient(np.gradient(ds_dw, hh, edge_order=2),
                        hh, edge_order=2))
    return EL


def main():
    res = {'task': 'F4-2 l=0 even modes, MRV Appendix B at j^2=0',
           'convention': 'S = int dt dr [K0 chidot^2 - G0 chi^2 - M0 chi^2] '
                         'with chi^2 -> chi-prime^2 for G0; coefficients '
                         'include sqrt(-g) as in Appendix B. Normalised '
                         'values K0/J^2, G0/J^2 also reported.'}
    h = 0.002
    r = np.arange(-60.0, 60.0 + 0.5 * h, h)
    B = build(r, h)
    d, K0, G0 = B['d'], B['K0'], B['G0']
    J = d['J']
    pip, F4 = d['pip'], d['F4']
    inner = np.abs(r) < 50

    # ---- structural verification (brief item 1)
    res['structural'] = {
        'alpha_drops': ('every alpha term in eq. (action_even) carries an '
                        'explicit j^2 (j^2 a4 alpha\', j^2 a9 alpha, '
                        'j^2 b5 alphadot, j^2 c5 alpha, j^2 d1..d4); at '
                        'j^2=0 alpha is absent. It also multiplies '
                        'd_a Y_00 = 0.'),
        'H1_multiplier': 'kinetic term j^2 b_1 H_1^2 = 0 at j^2=0; '
                         'constraint d/dt[b_2 chi\' + b_3 chi + b_4 H_2]=0 '
                         'integrated to Q=0 with vanishing integration '
                         'constant (localised perturbations).',
        'b2_b4_proportionality': 'b_2 = -2 a_1/A and b_4 = -2 a_3/A hold '
                                 'identically (A=1) by the printed formulas.',
        'H0_H1_identity_Horndeski_part_max_dev':
            float(np.max(np.abs(B['b3'] - 2 * (B['Xip'] - B['a2H']))[inner])),
        'H0_H1_identity_printed_mismatch_minus_(-4 pip^3 F4)_max_dev':
            float(np.max(np.abs((B['b3'] - 2 * (B['Xip'] - B['a2']))
                                + 4 * pip**3 * F4)[inner])),
        'finding': ('The Horndeski part of a_2 satisfies the H0/H1 '
                    'constraint identity b_3 = 2(a_1\' - a_2) to 7e-15; '
                    'the printed a_2^BH breaks it by exactly -4 pi\'^3 F_4 '
                    '(agreement to 8e-15). Independent confirmation: the '
                    'paper\'s a_5 identity a_5 = -J^2 dE_A/dpi = a_2\' - '
                    'a_1\'\' holds with a_2^H to 5.9e-6 (FD floor) but '
                    'fails by 0.213 with printed a_2. As printed the two '
                    'constraints would over-determine chi; the '
                    'consistent reduction (used here) eliminates via '
                    'the H_1 bracket, and a_2 then drops out of the '
                    'reduced action entirely. Logged as an Appendix B '
                    'inconsistency, same class as the F4-4 E_J '
                    'transcription finding.'),
    }

    # ---- D pole
    D = B['D']
    idx = np.where(np.diff(np.sign(D)) != 0)[0]
    roots = []
    for i in idx:
        a, b = r[i], r[i + 1]
        fa, fb = D[i], D[i + 1]
        roots.append(float(a - fa * (b - a) / (fb - fa)))
    res['D_roots'] = roots
    rstar = roots[0]
    i0 = np.argmin(np.abs(r - rstar))
    # c_s2^2 limit at the pole from the l>=1 P3 formula:
    # cs2 = P3 / (D^2 (2 P1 - F)), P1 = Q', Q = J^2 (H - 2 F4 pip^4)/D
    # -> limit P3 / (-2 * J^2 (1 - 2 F4 pip^4) * D')
    P3 = (2 * J**2 * B['Gamma'] * B['Xi'] * pip**2
          - B['Xi']**2 * pip**2 - 4 * J**4 * B['Sig'])
    num = J**2 * (1 - 2 * F4 * pip**4)
    cs2_pole = float(P3[i0] / (-2 * num[i0] * B['Dp'][i0]))
    res['pole'] = {
        'location_r': rstar,
        'K0_G0_behaviour': 'both ~ +1/D^2, positive on both sides '
                           '(shared parametrisation singularity of the '
                           'chi variable at the xi-denominator zero)',
        'G0_over_K0_limit': float(G0[i0 - 3] / K0[i0 - 3]),
        'cs2_limit_from_l_ge_1_P3_formula': cs2_pole,
    }

    # ---- throat behaviour
    kth = {}
    for rr in (0.02, 0.05, 0.1):
        kp = np.argmin(np.abs(r - rr))
        km = np.argmin(np.abs(r + rr))
        kth[f'r={rr}'] = dict(K0_over_r2_plus=float(K0[kp] / rr**2),
                              K0_over_r2_minus=float(K0[km] / rr**2),
                              G0_over_r2_plus=float(G0[kp] / rr**2),
                              G0_over_r2_minus=float(G0[km] / rr**2),
                              ratio_plus=float(G0[kp] / K0[kp]),
                              ratio_minus=float(G0[km] / K0[km]))
    res['throat'] = {
        'K0_at_0': float(K0[np.argmin(np.abs(r))]),
        'G0_at_0': float(G0[np.argmin(np.abs(r))]),
        'fits': kth,
        'note': ('K0 and G0 both vanish quadratically at r=0 '
                 '(K0 ~ 0.97 r^2, G0 ~ 0.76 r^2, ratio -> ~0.789): the '
                 'J\'^2 degeneracy, mirroring det K, det G ~ J\'^2 at '
                 'l>=1. No 1/J\' artefact survives at l=0: every 1/J\' '
                 'in Appendix B (d_3, e_4) multiplies j^2. Coefficients '
                 'are finite (zero, not singular) at the throat.'),
    }

    # ---- headline sign results + grid convergence
    def headline(hh):
        rr = np.arange(-60.0, 60.0 + 0.5 * hh, hh)
        Bb = build(rr, hh)
        KK, GG = Bb['K0'], Bb['G0']
        mm = np.abs(rr) < 59.9
        neg = mm & (KK < 0)
        cross = None
        if np.any(neg):
            # rightmost negative point on the negative side
            rn = rr[neg & (rr < 0)]
            cross = float(rn.max()) if len(rn) else None
        return dict(h=hh, K0_min=float(np.min(KK[mm])),
                    K0_min_r=float(rr[mm][np.argmin(KK[mm])]),
                    K0_min_over_J2=float(np.min((KK / Bb['d']['J']**2)[mm])),
                    G0_min=float(np.min(GG[mm])),
                    K0_neg_rightmost_r_negative_side=cross)
    res['convergence'] = [headline(0.004), headline(0.002),
                          headline(0.001)]
    m = np.abs(r) < 59.9
    iK = np.argmin(np.where(m, K0, np.inf))
    res['K0'] = {'min': float(K0[iK]), 'min_r': float(r[iK]),
                 'min_over_J2': float(np.min((K0 / J**2)[m])),
                 'asymptotic_over_J2_minus_inf': -2.0 / TAU**2,
                 'negative_region': 'r < -12.32 (within [-60,60]); '
                                    'K0/J^2 -> -2/tau^2 = -0.02 as '
                                    'r -> -inf (analytic leading term)',
                 'at_throat': float(K0[np.argmin(np.abs(r))]),
                 'samples': {f'r={rr}': float(K0[np.argmin(np.abs(r - rr))])
                             for rr in (-40, -20, -10, 0, 5, 20, 40)}}
    res['G0'] = {'min': float(np.min(G0[m])), 'min_r': 0.0,
                 'note': 'G0 > 0 everywhere on [-60,60] except the '
                         'throat point itself, where it vanishes '
                         'quadratically (see throat fits)',
                 'samples': {f'r={rr}': float(G0[np.argmin(np.abs(r - rr))])
                             for rr in (-40, -20, -10, 0, 5, 20, 40)}}

    # ---- anatomy of the K0 sign (u=0 parity control + term variants)
    def K0_variant(U, mode):
        old = p31.U
        p31.U = U
        try:
            Bb = build(r, h)
            dd = Bb['d']
            JJ, Jp_, X_ = dd['J'], dd['Jp'], dd['X']
            j3 = -2 * Jp_**3 / X_
            e1v = Bb['e1']
            if mode == 'removed':
                e1v = e1v - 0.5 * j3
            elif mode == 'flipped':
                e1v = e1v - j3
            return Bb['K0'] - Bb['e1'] + e1v
        finally:
            p31.U = old
    K0_u0 = K0_variant(0.0, 'printed')
    K0_rm = K0_variant(0.1, 'removed')
    K0_fl = K0_variant(0.1, 'flipped')
    kp40 = np.argmin(np.abs(r - 40))
    km40 = np.argmin(np.abs(r + 40))
    res['anatomy'] = {
        'driver': ('K0 < 0 for r < -12.32 as printed. Leading asymptotic '
                   'K0/J^2 -> -2/tau^2 (r -> -inf) vs +2/tau^2 (r -> '
                   '+inf): the sign is set by the single parity-odd term '
                   'of printed e_1, -H B^2 J\'^2/(J X A) d/dr(J^2 A/B) '
                   '= -2 J\'^3/X.'),
        'u0_parity_control': {
            'K0_side_difference_at_abs40': float(K0_u0[kp40]
                                                 - K0_u0[km40]),
            'twice_e1_odd_part_at_40': float(2 * (-(40.0 / J[kp40])**3
                                                  / (-0.5 * (TAU
                                                             / J[kp40])**2))),
            'K0_even_part_at_abs40': float(0.5 * (K0_u0[kp40]
                                                  + K0_u0[km40])),
            'note': ('for u=0 the construction is manifestly r -> -r '
                     'symmetric, yet K0(40) - K0(-40) = 62.0891 equals '
                     'exactly twice the odd part of printed e_1 at 40, '
                     '-J\'^3/X = 31.0446: the J\'^3 term is the ONLY '
                     'asymmetry in K0. That term is invisible in '
                     'Kobayashi\'s J=r original (J\'=1). Its J-general '
                     'form as printed is therefore suspect — but see '
                     'next entry: no variant rescues positivity.')},
        'variant_removed': {'K0_at_-40': float(K0_rm[km40]),
                            'K0_at_+40': float(K0_rm[kp40]),
                            'K0_min': float(np.min(K0_rm[m]))},
        'variant_flipped': {'K0_at_-40': float(K0_fl[km40]),
                            'K0_at_+40': float(K0_fl[kp40]),
                            'K0_min': float(np.min(K0_fl[m]))},
        'conclusion': ('Even part of K0 at |r|=40 is already negative '
                       '(-3.88, u=0 control); removing the suspect term '
                       'leaves K0 -> ~ -4 at BOTH infinities, flipping '
                       'it moves the ghost to r > 0. Within the printed '
                       'coefficient set no single-term repair of e_1 '
                       'makes K0 positive everywhere.'),
    }

    # ---- c_3, e_3, M0 (input to F4-3; not part of the verdict)
    ds_ = 2e-3  # shift in s; d pi = tau * ds = 0.02
    EBp, EAp = shifted_EB_EA(r, d, +ds_)
    EBm, EAm = shifted_EB_EA(r, d, -ds_)
    dpi_ = TAU * ds_
    c3 = J**2 * (EBp - EBm) / (2 * dpi_)
    dEA = (EAp - EAm) / (2 * dpi_)
    a5_from_aH = np.gradient(B['a2H'], h, edge_order=2) \
        - np.gradient(B['Xip'], h, edge_order=2)
    a5_from_a = np.gradient(B['a2'], h, edge_order=2) \
        - np.gradient(B['Xip'], h, edge_order=2)
    res['c3_validation'] = {
        'minus_J2_dEA_dpi_vs_a5_from_a2H_max_dev_|r|<30':
            float(np.max(np.abs(-J**2 * dEA - a5_from_aH)[np.abs(r) < 30])),
        'minus_J2_dEA_dpi_vs_a5_from_printed_a2_max_dev_|r|<30':
            float(np.max(np.abs(-J**2 * dEA - a5_from_a)[np.abs(r) < 30])),
        'note': ('the shifted-pi machinery reproduces the paper\'s a_5 '
                 'identity to 5.9e-6 (FD floor) when a_5 is built from '
                 'the Horndeski part of a_2 — validating c_3 and '
                 'confirming independently that printed a_2^BH is the '
                 'inconsistent piece (dev 0.213 with printed a_2)')}
    # e_3 on a coarse grid via the EL route, interpolated
    hc = 0.01
    rc = np.arange(-60.0, 60.0 + 0.5 * hc, hc)
    dc = p31.theory_on_bg(rc)
    ELp = el_pi_shifted(rc, dc, +ds_)
    ELm = el_pi_shifted(rc, dc, -ds_)
    e3c = (ELp - ELm) / (2 * dpi_)
    e3 = np.interp(r, rc, e3c)
    gr = lambda v: np.gradient(v, h, edge_order=2)
    Bm = B['p'] * c3 + B['q'] * B['c2'] + 2 * B['c6'] * B['p'] * B['q']
    M0 = -(e3 + B['q'] * c3 + B['c6'] * B['q']**2 - 0.5 * gr(Bm))
    away = (np.abs(r - rstar) > 1.0) & m
    iMn = np.argmin(np.where(away, M0, np.inf))
    iMx = np.argmax(np.where(away, M0, -np.inf))
    res['M0'] = {
        'definition': 'M0 in S = int [K0 chidot^2 - G0 chi\'^2 - M0 '
                      'chi^2]; singular at the D=0 pole like K0/G0 '
                      '(same chi-parametrisation); extrema quoted for '
                      '|r - r*| > 1',
        'samples': {f'r={rr}': float(M0[np.argmin(np.abs(r - rr))])
                    for rr in (-40, -20, -10, -5, -2, 0, 5, 10, 20, 40)},
        'min_|r-r*|>1': float(M0[iMn]), 'min_r': float(r[iMn]),
        'max_|r-r*|>1': float(M0[iMx]), 'max_r': float(r[iMx]),
        'at_throat': float(M0[np.argmin(np.abs(r))]),
        'negative_region_|r-r*|>1':
            (lambda neg: ([float(r[neg].min()), float(r[neg].max())]
                          if np.any(neg) else None))(
                away & (M0 < 0)),
        'sign_summary': 'M0(0) ~ 0 (5e-7) and M0 > 0 at all sampled '
                        'radii except a negative pocket on the '
                        'positive side of the throat, 0 <~ r <~ 0.77 '
                        '(min -3.05 at r = 0.77); at large |r| '
                        'M0 -> ~ +0.019. '
                        'This pocket is the l=0 tachyon input for '
                        'F4-3 (its sign alone is not a verdict here).',
        'caveat': 'e_3 from FD pi-shift of the EL_pi functional '
                  '(p44b route); absolute normalisation is the '
                  'reduced-action one (E_pi = EL_pi/J^2).'}

    # ---- why the l -> 0 limit of the l>=1 matrices is not the answer
    res['ell_limit_note'] = (
        'det K and det G (eqs. detK/detG) carry (l-1)(l+2) in the '
        'numerator but l(l+1) = j^2 in the denominator, and K_11 '
        'carries [j^2 P_1 - F]/j^2: as l -> 0 these diverge or flip '
        'sign (K_11 -> -F/j^2). The divergence is manufactured by the '
        'l>=1 reduction itself, which divides by j^2 when solving the '
        'H_0 constraint for alpha (eq. alpha). At l=0 alpha does not '
        'exist, H_1 degenerates to a multiplier, and the constraint '
        'structure is different: the l=0 reduction above is '
        'independent, not a limit.')

    res['verdict'] = ('FAIL — K0 < 0 for r in [-60, -12.32] (ghost in '
                      'the spherically symmetric even sector, negative '
                      'side, K0/J^2 -> -0.02 at -inf), beyond tolerance '
                      'by ~4 orders of magnitude. G0 > 0 everywhere '
                      '(vanishing only quadratically at the throat). '
                      'Anatomy in res.anatomy: the sign is driven by '
                      'printed e_1, whose J\'^3 term is parity-anomalous '
                      '(suspected misprint in the J-generalisation), '
                      'but the even part of K0 is also negative at '
                      'large |r| and no single-term repair restores '
                      'positivity. Reopening: a corrected Appendix B '
                      'e_1 / a_2^BH, or an independent l=0 derivation '
                      'from the covariant action.')

    with open('/home/hatch/workspace/warp-pilot/phase4/results/'
              'p42_ell0.json', 'w') as fh:
        json.dump(res, fh, indent=2)
    print(json.dumps({k: res[k] for k in
                      ('structural', 'pole', 'throat', 'convergence',
                       'K0', 'G0', 'anatomy', 'M0', 'verdict')},
                     indent=2))


if __name__ == '__main__':
    main()
