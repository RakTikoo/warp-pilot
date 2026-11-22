#!/usr/bin/env python
"""Gate-5 W-B, claim G5-4: INDEPENDENT verification of the GJW ledger.

Fresh code from the PUBLISHED formulas as stated in the claim:
  GJW (arXiv:1608.05687) eq. for the ANE integral along the horizon,
    int_{U0}^inf dU T_UU = -h Gamma(2D+1)^2 / [2^{4D} (2D+1) Gamma(D)^2
    Gamma(D+1)^2 l] * 2F1(1/2+D, 1/2-D; 3/2+D; 1/(1+U0^2))
    / (1+U0^2)^{D+1/2},   U0 = 1, l = L_AdS = 1 here;
  horizon shift (GJW Sec.5 scaling) dV ~ h G_N / R^{D-2};
  BDS (arXiv:1907.13140) dV = 4 pi G_N * ANE, open proper time
    dtau ~= 2 l dV (symmetric frame), capped by t_Planck;
  throughput N = O(h) at r_h ~ l; thermal quantum E ~ hbar c / L.
Macroscopic numbers recomputed in SI with scipy.constants.
Phase-2 / Phase-23 stored numbers are read ONLY at the end, to compare.
float64 everywhere.
"""
import json
import numpy as np
from scipy.special import gamma, hyp2f1
from scipy.constants import c, hbar, G, physical_constants

lp = physical_constants['Planck length'][0]
tp = physical_constants['Planck time'][0]
OUT = {}

# ---------------------------------------------------------------- ANE --
def ane_integral(Delta, h=0.1, U0=1.0, ell=1.0):
    D = Delta
    pref = (gamma(2 * D + 1) ** 2 /
            (2 ** (4 * D) * (2 * D + 1) * gamma(D) ** 2 * gamma(D + 1) ** 2 * ell))
    hyp = hyp2f1(0.5 + D, 0.5 - D, 1.5 + D, 1.0 / (1.0 + U0 ** 2))
    return -h * pref * hyp / (1.0 + U0 ** 2) ** (D + 0.5)

Ds = [0.1, 0.25, 0.5, 0.75, 0.9]
ane = {str(d): ane_integral(d) for d in Ds}
fine = np.linspace(0.01, 0.99, 99)
ane_fine = [ane_integral(float(d)) for d in fine]
OUT['ANE_mine_h0.1'] = ane
OUT['ANE_all_negative_0<D<1'] = bool(np.all(np.array(ane_fine) < 0))
OUT['ANE_peak_Delta'] = float(fine[int(np.argmin(ane_fine))])
OUT['ANE_linear_in_h_check'] = bool(
    abs(ane_integral(0.5, h=0.3) / ane_integral(0.5, h=0.1) - 3.0) < 1e-12)
# Phase-2 gate row (comparison only, read now)
p2 = json.load(open('/home/hatch/workspace/warp-pilot/phase2/results/w2_quantum_wh.json'))
p2ane = p2['GJW']['ANE_integral_int_dU_TUU_per_h_over_L']
OUT['phase2_gate_comparison'] = {
    str(d): {'mine': ane[str(d)], 'phase2': p2ane[str(d)],
             'rel_diff': abs(ane[str(d)] - p2ane[str(d)]) / abs(p2ane[str(d)])}
    for d in Ds}
OUT['phase2_DeltaV_order'] = p2['GJW']['DeltaV_horizon_shift_Kruskal']
OUT['send_window_mine'] = float(np.log(1.0 / (0.1 * 0.01)))   # ln(R/(h lp,eff)), R=1
OUT['send_window_phase2'] = p2['GJW']['send_in_window_Dt_Lc (R ln(R/(h lp)))']

# ------------------------------------------------------- macro ledger --
def ledger(L):
    h = 0.1
    dV_order = h * lp**2 / L**2                    # GJW scaling, D=4
    # BDS coefficient: dV_BDS = 4 pi G_N * ANE_int; transplanted to 4D the
    # ratio dV_BDS/dV_order = 4 pi * |ANE_int(h=0.1)| / h * h ... the stored
    # run's ratio is 0.3183 = 4 pi * 0.02533 with 0.02533 = |ANE_int| at
    # h=0.1 in BTZ units -- an O(1) factor < 1 either way; the deciding
    # object is dV_order and dtau derived from it, computed below.
    dtau = 2 * L * dV_order / c                    # BDS dtau ~ 2 l dV, SI
    E_q = hbar * c / L                             # thermal quantum scale
    N_std = h                                      # N = O(h) at r_h ~ l
    cap_kg = N_std * E_q / c**2
    S_nats = np.pi * L**2 / lp**2                  # A/(4 lP^2), A = 4 pi L^2
    A_dimless = abs(ane_integral(0.5, h=0.1)) / 0.1  # per-unit-h coefficient 0.2533? check
    # phase supply: E_neg = Acoef_stored * h * hbar c / L with
    # Acoef_stored = 0.02533 = |ANE_int| at h=0.1 itself. Their supply is
    # therefore |ANE_int(h=0.1)| * h * hbar c/L. Reproduce that bookkeeping
    # AND the per-unit-h variant; both are one-loop O(hbar c/L) scales.
    E_sup_phase_book = abs(ane_integral(0.5, h=0.1)) * h * hbar * c / L
    E_sup_perh = A_dimless * h * hbar * c / L
    E_dem = L * c**4 / G                           # exotic scale r0 c^4/G
    return {
        'L_m': L, 'DeltaV_order': dV_order,
        'open_proper_time_s': dtau,
        'open_over_planck': dtau / tp,
        'gap_open_orders_vs_10us': float(np.log10(1e-5 / dtau)),
        'gap_planckcap_orders_vs_10us': float(np.log10(1e-5 / tp)),
        'E_thermal_quantum_J': E_q,
        'capacity_kg_N_O(h)': cap_kg,
        'gap_capacity_orders_vs_70kg': float(np.log10(70.0 / cap_kg)),
        'S_BH_nats': S_nats,
        'E_neg_supplied_J_phase_bookkeeping': E_sup_phase_book,
        'E_neg_supplied_J_per_unit_h_coeff': E_sup_perh,
        'E_demand_J': E_dem,
        'demand_over_supply_phase_book': float(E_dem / E_sup_phase_book),
        'demand_over_supply_orders_phase_book': float(np.log10(E_dem / E_sup_phase_book)),
        'W1W6_ratio_(4pi/3)(L/lP)^2': float((4 * np.pi / 3) * (L / lp) ** 2),
    }

OUT['macro_1m'] = ledger(1.0)
OUT['macro_1ly'] = ledger(9460730472580800.0)
OUT['antiscaling_ratio_dtau_1m_over_1ly'] = (
    OUT['macro_1m']['open_proper_time_s'] / OUT['macro_1ly']['open_proper_time_s'])
OUT['antiscaling_expected_L_ratio'] = 9460730472580800.0

print(json.dumps(OUT, indent=1))
with open('/home/hatch/workspace/warp-pilot/gate5/wb_g54_out.json', 'w') as f:
    json.dump(OUT, f, indent=1)
