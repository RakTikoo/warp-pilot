"""P33-5 pricing: measured Lambda and uniform B against the Finalist beta=0.1 deficit.
float64, SI pricing statements. Deficits are EC margins in geometric units (1/m^2),
the programme's audit units (verify_metric.py: T = G/8pi, G=c=1).
Conversion: rho_SI [J/m^3] = T_geom [1/m^2] * c^4/G.
"""
import json, math
import numpy as np

c = np.float64(2.99792458e8); G = np.float64(6.674e-11)
mu0 = np.float64(4e-7 * np.pi)
LAM = np.float64(1.09e-52)          # m^-2, measured, CHECKPOINT33 (no dialling)
C4_G = c**4 / G                     # J/m^3 per (1/m^2)

# ---- deficits (geometric 1/m^2), all labelled by source ----------------------
deficits = {
    'D1_record_closest_nearmiss': 2.06e-7,   # REPORT 1.2: named families, beta=0.1 closest near-miss -2.06e-7
    'D2_record_tail_DEC':         1.8e-6,    # REPORT 1.3/N3 run2: tail DEC -1.8e-6, resolution-independent
    'D3_rerun_frontierlike_DEC':  2.173907043259432e-06,  # p335_rerun.json, unoptimised (5,10) profile
}
rerun = json.load(open('/home/hatch/workspace/warp-pilot/phase33/results/p335_rerun.json'))

# ---- (a) Lambda ---------------------------------------------------------------
# T_Lambda_ab = -(Lambda/8pi) g_ab  =>  rho_L = Lambda/(8pi) (geom), p_L = -rho_L.
rho_L_geom = LAM / (8 * np.pi)
rho_L_SI = rho_L_geom * C4_G                       # J/m^3 (~5.3e-10, dark-energy density)
lam = {'Lambda_m-2': float(LAM), 'rho_Lambda_geom_m-2': float(rho_L_geom),
       'rho_Lambda_SI_J_m-3': float(rho_L_SI),
       'EC_of_Lambda_alone': {'NEC_rho+p': 0.0, 'WEC_rho': float(rho_L_geom),
                              'SEC_rho+sum_p': float(-2 * rho_L_geom), 'DEC_rho-|p|': 0.0},
       'note': 'Lambda is NEC-neutral and DEC-saturating exactly (rho+p=0, rho-|p|=0); '
               'its only nonzero EC shift is SEC-negative (-2 rho_L). It cannot cover an '
               'NEC/DEC deficit at any magnitude; priced below on magnitude anyway.',
       'Lambda_R2_at_R20m': float(LAM * 20.0**2),
       'per_deficit': {}}
for k, D in deficits.items():
    lam['per_deficit'][k] = {'deficit_geom': D, 'ratio_rhoL_over_deficit': float(rho_L_geom / D),
                             'orders_short': float(-np.log10(rho_L_geom / D))}

# ---- (b) Magnetic field -------------------------------------------------------
# EM (B along z): rho_EM>0, p_perp=+rho_EM (x,y), p_par=-rho_EM (z, tension).
# EC contributions of EM alone: NEC_perp=2rho, NEC_par=0, WEC=rho,
# SEC_worst_dir=0 (par), SEC_rho+sum_p=2rho, DEC=rho-|p|=0 (saturates, never negative).
# Optimal cover of a binding deficit D (geom): need rho_EM_geom >= D
# (binding combination gains between rho_EM and 2*rho_EM depending on clause/orientation;
#  pricing uses rho_EM = D, the most augmentation-friendly choice).
# B from rho_EM_SI = B^2/(2 mu0).
def B_for(D):
    rho_SI = D * C4_G
    return float(np.sqrt(2 * mu0 * rho_SI)), float(rho_SI)

mag = {'benchmarks_T': {'sustained': 45.0, 'pulsed': 1e3, 'Schwinger_Bc': 4.4e9},
       'EM_EC_alone': 'NEC: 2rho_EM (perp) / 0 (along B); WEC: rho_EM; SEC: >=0; DEC: 0 (saturated). '
                      'EM alone is EC-legal, but its DEC margin contribution is exactly 0 in its own '
                      'eigenframe and its NEC contribution along B is exactly 0.',
       'per_deficit': {}}
for k, D in deficits.items():
    B, rho_SI = B_for(D)
    # Melvin scale: geometrised B (Gaussian geom, rho=B_g^2/8pi) -> curvature/flux-tube length 1/B_g
    Bg = np.sqrt(8 * np.pi * D)
    mag['per_deficit'][k] = {
        'deficit_geom_m-2': D, 'rho_EM_needed_SI_J_m-3': rho_SI, 'B_required_T': B,
        'orders_above_pulsed_1e3T': float(np.log10(B / 1e3)),
        'orders_above_sustained_45T': float(np.log10(B / 45.0)),
        'ratio_over_Schwinger_Bc': float(B / 4.4e9),
        'orders_above_Schwinger_Bc': float(np.log10(B / 4.4e9)),
        'Melvin_length_scale_m_est': float(1.0 / Bg),
        'note_Melvin': 'uniform B => Melvin asymptotics, not asymptotically flat; flux-tube/'
                       'curvature scale ~1/B_geom as listed, i.e. only ~10-20x the shell radii.'}
# Tail-DEC worked example (N3 tail: rho~0, p_r~+1.8e-6, B oriented with tension along r):
D = deficits['D2_record_tail_DEC']
mag['tail_worked_example'] = {
    'site': 'conditions-first tail, rho~0, p_r=+1.8e-6 geom, p_t~0',
    'orientation': 'B tension axis along r (locally optimal)',
    'rho_EM_geom': D, 'after': {'rho': D, 'p_r': 0.0, 'p_t': D,
    'DEC_r': D, 'DEC_t': 0.0, 'NEC_r': D, 'NEC_t': 2 * D},
    'caveat': 'DEC_t saturates at exactly 0 (uncertifiable, same status as the record\'s +1.3e-9 '
              'tiebreak); and a single UNIFORM B cannot be radial everywhere on a spherical shell '
              '(radial B = monopole, div B != 0): uniform B is radial only at the poles, tangential '
              'at the equator, where its +rho_EM pressure ADDS to the radial pressure and worsens '
              'radial DEC there. The priced B is therefore a lower bound for one uniform field.'}

res = {'item': 'P33-5 WALLS + LAMBDA AND MAGNETIC FIELD', 'beta': 0.1,
       'units': 'margins/deficits in geometric 1/m^2 (programme audit units); c^4/G = %.6e J/m^3 per 1/m^2' % C4_G,
       'deficit_sources': {
           'D1': 'REPORT.md 1.2 (recorded): closest beta=0.1 near-miss -2.06e-7, named families',
           'D2': 'REPORT.md 1.3/N3 run 2 (recorded): tail DEC -1.8e-6, resolution-independent',
           'D3': 'p335_rerun.py this item: unoptimised profiles at beta=0.1 fail (A-profile worst -1.0; '
                 'frontier-like (5,10) M=1.915 worst SEC -3.70e-3, DEC -2.17e-6) — corroborates D2 scale; '
                 'pricing uses D1/D2, the smallest (most augmentation-friendly) deficits'},
       'rerun_summary': {k: v for k, v in rerun.items() if k != 'wall_time_s'},
       'lambda': lam, 'magnetic': mag,
       'verdicts': {
           'a_lambda': 'AUGMENTED-FAIL — measured Lambda is NEC/DEC-neutral by identity (rho+p=0) and '
                       'SEC-negative; on magnitude alone it is %.1f orders short of the smallest recorded '
                       'deficit (D1) and %.1f orders short of D2.' % (
                           lam['per_deficit']['D1_record_closest_nearmiss']['orders_short'],
                           lam['per_deficit']['D2_record_tail_DEC']['orders_short']),
           'b_magnetic': 'AUGMENTED-FAIL — covering even the smallest recorded deficit (D1) needs '
                         'B = %.2e T (%.1f orders above the 1e3 T pulsed bar, %.1f orders above Schwinger '
                         'Bc); D2 needs %.2e T. Plus Melvin (non-asymptotically-flat) asymptotics and the '
                         'uniform-B/monopole orientation obstruction.' % (
                             mag['per_deficit']['D1_record_closest_nearmiss']['B_required_T'],
                             mag['per_deficit']['D1_record_closest_nearmiss']['orders_above_pulsed_1e3T'],
                             mag['per_deficit']['D1_record_closest_nearmiss']['orders_above_Schwinger_Bc'],
                             mag['per_deficit']['D2_record_tail_DEC']['B_required_T'])}}
with open('/home/hatch/workspace/warp-pilot/phase33/results/p335_results.json', 'w') as fh:
    json.dump(res, fh, indent=1)
print(json.dumps(res['verdicts'], indent=1))
print('Lambda orders short: D1 %.2f  D2 %.2f' % (lam['per_deficit']['D1_record_closest_nearmiss']['orders_short'],
                                                 lam['per_deficit']['D2_record_tail_DEC']['orders_short']))
for k, v in mag['per_deficit'].items():
    print(k, 'B = %.3e T, %.2f orders above pulsed, %.2f above Bc, Melvin L ~ %.0f m' % (
        v['B_required_T'], v['orders_above_pulsed_1e3T'], v['orders_above_Schwinger_Bc'], v['Melvin_length_scale_m_est']))
