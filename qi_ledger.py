"""
qi_ledger.py — Phase 1: uniform (R, Delta, v) negative-energy accounting.

All energies computed from the analytic Alcubierre density via the exact
angular reduction (Pfenning & Ford Eq. 26):
    E = -(v^2/12) * int_0^inf r^2 (f'(r))^2 dr      [geometric units: metres]
converted with M_kg = E_m / (G/c^2), G/c^2 = 7.426e-28 m/kg.
Anchors (PF 1997 primary): ~0.25-0.6 M_sun at R=100 m, Delta=1 m, v~1;
~-3e20 galaxy masses at the QI wall Delta_QI = 100 * v * L_P (PF Eq. 23);
scaling |E| ~ v^2 R^2 / Delta.
Van den Broeck: v5 abstract "few solar masses" total negative, comparable
positive; his region-IV uses the same integral at femtometre radius
(VdB Eq. 8-9), region II quoted from his Eqs. (15)-(16).
"""
import json
import numpy as np

DTYPE = np.float64
G_C2 = 7.426e-28          # G/c^2, m per kg
M_SUN = 1.98847e30        # kg
M_GAL_PF = 2.0e42         # kg, PF's galaxy mass (2e45 g)
L_P = 1.616255e-35        # m
C4_G = 1.0 / (8.262e-45)  # c^4/G, J/m^3 per geometric 1/m^2


def tanh_integral(R, sigma):
    """int r^2 (f')^2 dr for Alcubierre tanh f (numeric, fine radial grid)."""
    rmax = R + 30.0 / sigma
    r = np.linspace(0.0, rmax, 200001, dtype=DTYPE)
    fp = (sigma * (1 / np.cosh(sigma * (r + R)) ** 2
                   - 1 / np.cosh(sigma * (r - R)) ** 2)
          / (2 * np.tanh(sigma * R)))
    return float(np.trapz(r ** 2 * fp ** 2, r))


def E_tanh(R, sigma, v):
    I = tanh_integral(R, sigma)
    E_m = -(v ** 2 / 12.0) * I
    return E_m, E_m / G_C2


def E_piecewise(R, Delta, v):
    I = R ** 2 / Delta + Delta / 12.0
    E_m = -(v ** 2 / 12.0) * I
    return E_m, E_m / G_C2


def delta_eff(R, sigma):
    """Effective piecewise wall thickness matching the tanh integral:
    solve R^2/D + D/12 = I  (thin-wall root)."""
    I = tanh_integral(R, sigma)
    # D^2 - 12 I D + 12 R^2 = 0 -> smaller root is the wall thickness branch
    disc = (12 * I) ** 2 - 48 * R ** 2
    D = (12 * I - np.sqrt(max(disc, 0.0))) / 2.0
    return float(D)


def integrated_negative_energy(g, That, h):
    """int min(rho_Euler,0) sqrt(det gamma) d^3x from an audit grid.
    Returns geometric metres (mass-equivalent)."""
    gamma = g[..., 1:, 1:]
    det = np.linalg.det(gamma)
    rho = That[..., 0, 0]
    neg = np.minimum(rho, 0.0)
    return float(np.sum(neg * np.sqrt(np.maximum(det, 0.0))) * h ** 3)


def main():
    out = {'anchors': {}, 'sweep': [], 'scaling': {}}

    # --- Anchor 1: PF piecewise, R=100 m, Delta=1 m, v=1 --------------------
    E_m, E_kg = E_piecewise(100.0, 1.0, 1.0)
    out['anchors']['pf_R100_D1_v1'] = {'E_kg': E_kg, 'E_Msun': E_kg / M_SUN,
                                      'pf_claim': 'order of a quarter solar mass'}
    # tanh with sigma=2 (Delta ~ 2/sigma = 1 m)
    E_m2, E_kg2 = E_tanh(100.0, 2.0, 1.0)
    out['anchors']['tanh_R100_sigma2_v1'] = {'E_kg': E_kg2, 'E_Msun': E_kg2 / M_SUN,
                                             'Delta_eff_m': delta_eff(100.0, 2.0)}
    # --- Anchor 2: QI wall ---------------------------------------------------
    DQ = 100.0 * 1.0 * L_P
    E_m, E_kg = E_piecewise(100.0, DQ, 1.0)
    out['anchors']['pf_R100_QIwall_v1'] = {'Delta_QI_m': DQ, 'E_kg': E_kg,
                                           'E_galaxies': E_kg / M_GAL_PF,
                                           'pf_claim': '~-3e20 galaxy masses (Eq. 31)'}
    # --- Anchor 3: Van den Broeck region IV (femtometre bubble) -------------
    # VdB v5 Eq. (7)-(9): outer radius ~3e-15 m scale; he quotes
    # E_IV ~ -6.3e29 v_s kg, E_II,- = -1.4e30 kg, E_II,+ = +4.9e30 kg.
    out['anchors']['vdb'] = {'paper_total_negative': 'few x 1e30 kg (few M_sun)',
                             'E_IV_kg_quoted': -6.3e29, 'E_II_neg_kg_quoted': -1.4e30,
                             'E_II_pos_kg_quoted': 4.9e30,
                             'note': 'v5 corrected version; v4 abstract erroneously said grams'}

    # --- Sweep: Alcubierre tanh family ---------------------------------------
    for R in (1.0, 10.0, 100.0):
        for v in (0.1, 0.5, 1.0, 2.0):
            for sigma in (0.2, 2.0, 20.0):
                E_m, E_kg = E_tanh(R, sigma, v)
                out['sweep'].append({'family': 'alcubierre_tanh', 'R': R, 'v': v,
                                     'sigma': sigma, 'Delta_eff': delta_eff(R, sigma),
                                     'E_kg': E_kg, 'E_Msun': E_kg / M_SUN})
    # --- Scaling exponents from the sweep (fixed sigma=2: Delta_eff ~ 1 m) ---
    vs = np.array([0.1, 0.5, 1.0, 2.0])
    Es = np.array([abs(E_tanh(10.0, 2.0, v)[1]) for v in vs])
    out['scaling']['v_exponent'] = float(np.polyfit(np.log(vs), np.log(Es), 1)[0])
    Rs = np.array([1.0, 10.0, 100.0])
    Es = np.array([abs(E_tanh(R, 2.0, 1.0)[1]) for R in Rs])
    out['scaling']['R_exponent'] = float(np.polyfit(np.log(Rs), np.log(Es), 1)[0])
    sgs = np.array([0.2, 2.0, 20.0])
    Ds = np.array([delta_eff(10.0, s) for s in sgs])
    Es = np.array([abs(E_tanh(10.0, s, 1.0)[1]) for s in sgs])
    out['scaling']['Delta_exponent'] = float(np.polyfit(np.log(Ds), np.log(Es), 1)[0])

    # --- Casimir scale --------------------------------------------------------
    hbar_c = 3.1615e-26  # J m
    a = 1e-6
    rho_cas = -np.pi ** 2 * hbar_c / (720 * a ** 4)
    # warp density scale for a 1 m structure: (c^4/8 pi G) * (1/R^2), R = 1 m
    rho_warp = C4_G / (8 * np.pi)
    out['casimir'] = {'rho_J_m3_at_1um': float(rho_cas),
                      'warp_need_J_m3_at_R1m': float(rho_warp),
                      'gap_orders': float(np.log10(rho_warp / abs(rho_cas))),
                      'note': 'research report said ~1e35 J/m3 / ~38 orders; '
                              'direct evaluation of (c^4/8piG)(1/R^2) at R=1 m '
                              'gives 4.8e42 J/m3 and a ~46-order gap. Even the '
                              'report smaller figure leaves >=38 orders.'}

    with open('results/qi_ledger.json', 'w') as fh:
        json.dump(out, fh, indent=1)
    print(json.dumps(out['anchors'], indent=1))
    print('scaling:', out['scaling'])
    print('casimir:', out['casimir'])
    print('LEDGER DONE')


if __name__ == '__main__':
    main()
