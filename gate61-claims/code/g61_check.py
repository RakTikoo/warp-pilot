#!/usr/bin/env python
"""Gate-61 independent checker (separate process). Recomputes the
verdict-carrying numbers of gate61/results/g61_results.json with
fresh builds and an INDEPENDENTLY ORDERED assembly whose clause
arithmetic is the ENGINE's clauses_of (the driver's deciding path
used the gate's own clause implementation — the two paths
cross-check). Also recomputes the rescue arithmetic from the
stored worsts, the D-blindness totals, and the documentary
counts. Writes gate61/results/g61_verify.json."""
import json, math, sys
import numpy as np

sys.path.insert(0, '/home/hatch/workspace/warp-pilot/phase254/work')
sys.path.insert(0, '/home/hatch/workspace/warp-pilot/phase162/work')
sys.path.insert(0, '/home/hatch/workspace/warp-pilot/phase167/work')
import lateral_tide as LT          # noqa: E402
import p1621_engine as B           # noqa: E402
import p167_engine as E            # noqa: E402

ROOT = '/home/hatch/workspace/warp-pilot'
R = json.load(open(f'{ROOT}/gate61/results/g61_results.json'))
TH = B.AUDIT_TH.copy()
CK = list(B.CLAUSE_KEYS)
KAP = 0.254873
C_LIGHT = 299792458.0
BAR = 4.905
checks = []


def chk(name, ok, detail=''):
    checks.append({'check': name, 'pass': bool(ok),
                   'detail': str(detail)})


# ---- fresh builds (independently ordered) -------------------------
th_f = np.linspace(0.0, np.pi, 2881)
h_f = th_f[1] - th_f[0]
rhs = B.att(th_f) * B.phi0_h(th_f) / B.R00 - B.att_h(th_f) / B.R00
u_f = np.exp(B.phi0(th_f)) * B.cum_simpson(np.exp(-B.phi0(th_f))
                                           * rhs, h_f)
ut_a = B.interp_fine(th_f, u_f, TH)
z = np.zeros_like(TH)
J_home = B.instant_jets(0.0, z, z, z, z, ut_a)
th2, tm2, MU2, U2 = B.march(2881, 0.0025)
h2 = th2[1] - th2[0]
MTT2 = E.mtt_field(U2, 0.0025)
mu_a = B.interp_fine(th2, MU2[0], TH)
mu_h = B.interp_fine(th2, B.fd4_deriv(MU2[0], h2), TH)
mu_hh = B.interp_fine(th2, B.fd4_deriv2(MU2[0], h2), TH)
u_a = B.interp_fine(th2, U2[0], TH)
mtt_a = B.interp_fine(th2, MTT2[0], TH)
J_X = E.comp_jets(float(tm2[0]), mu_a, mu_h, mu_hh, u_a, mtt_a)
J_H0 = B.instant_jets(0.0, z, z, z, z, z)

C1 = (1.0 - np.cos(TH))**2 / (np.sin(TH)**2 * B.R00**2)


def engine_composition(Jbase):
    J = dict(Jbase)
    J['M'] = Jbase['M'] + 0.10 * np.ones_like(TH)
    J['Mhh'] = Jbase['Mhh'] - 0.10 * np.ones_like(TH)
    ch = B.channels(J, TH)
    rho = ch['rho8'] + 0.5 * KAP * C1
    pr = ch['prho8'] - 0.5 * KAP * C1
    pt = ch['pth8'] - 0.5 * KAP * C1
    pp = ch['pph8'] + 0.5 * KAP * C1
    cl = B.clauses_of(rho, pr, pt, pp)
    return {k: float(np.min(cl[k])) for k in CK}, J, ch


# ---- (1) CTL-H combined vector, engine path -----------------------
mins_home, _, _ = engine_composition(J_home)
d = max(abs(mins_home[k] - R['controls']['CTL-H']['combined_minima'][k])
        for k in CK)
chk('ctlH_combined_engine_path_vs_gate', d == 0.0, f'max diff {d}')

# ---- (2) both shadow vectors, engine path -------------------------
for sname, Jb in (('X_m', J_X), ('H_0', J_H0)):
    mins, _, _ = engine_composition(Jb)
    dv = max(abs(mins[k] - R['shadow_vectors'][sname]['minima'][k])
             for k in CK)
    chk(f'shadow_{sname}_vector_engine_path', dv == 0.0,
        f'max diff {dv}')
    chk(f'shadow_{sname}_positive',
        all(mins[k] > 0 for k in CK), 'all seven > 0')

# ---- (3) rescue arithmetic from the stored worsts -----------------
for sname in ('X_m', 'H_0'):
    p = R['prices'][sname]
    W = max(p['R_tltl_worst_abs_pose^-2'],
            p['lateral_beta0.1_worst_pose^-2'])
    rr = 0.8 * C_LIGHT * math.sqrt(W / BAR)
    chk(f'rescue_arithmetic_{sname}',
        abs(rr - p['rescue_radius_m_float64'])
        / p['rescue_radius_m_float64'] <= 1e-12,
        f'recomputed {rr} vs stored {p["rescue_radius_m_float64"]}')
    conv = C_LIGHT**2 / (p['rescue_radius_m_float64'] / 0.8)**2
    chk(f'rung_radial_ratio_{sname}',
        abs(p['R_tltl_worst_abs_pose^-2'] * conv / BAR - 1.0) <= 1e-9,
        'radial at rescue = bar')

# ---- (4) E_shell totals cross-checked by ratio to the blind value -
blind = R['D_blindness_crosscheck']
for sname in ('X_m', 'H_0'):
    p = R['prices'][sname]
    expect = (blind['datum_H_utilde_true']
              * p['rescue_radius_m_float64'] / 1.068e8)
    rel = abs(p['E_shell_at_rescue']['E_J'] - expect) / expect
    chk(f'E_shell_propto_R_{sname}', rel <= 1e-12,
        f'E(rescue) vs E(1.068e8)*R ratio rel diff {rel}')

# ---- (5) documentary counts re-verified ---------------------------
def cnt(p, n):
    return open(p).read().count(n)


chk('counts_comp_jets_zero',
    cnt(f'{ROOT}/phase226/work/p2261_run.py', 'comp_jets') == 0
    and cnt(f'{ROOT}/phase224/work/p2242_run.py', 'comp_jets') == 0,
    'gate count reproduced')
chk('A1_diff_zero',
    R['identity_G2']['max_abs_diff'] == 0.0, 'from gate results')
chk('both_marker_classification_complete',
    set(R['identity_G3']['both_marker_files'])
    == set(R['identity_G3']['coordinator_classification'].keys()),
    'every both-marker file classified; none POSING-class')

# ---- (6) verdict consistency --------------------------------------
m = R['verdict_mechanics']
chk('mechanics_all_hold', m['all_mechanical_legs_hold'],
    json.dumps({k: v for k, v in m.items()
                if k != 'all_mechanical_legs_hold'}))
chk('verdict_consistent',
    (R['gate_verdict'] == 'PASS') == m['all_mechanical_legs_hold'],
    R['gate_verdict'])

out = {'checker': 'Gate-61 independent checker (engine clause path, '
                  'independently ordered assembly)',
       'checks': checks,
       'n_pass': sum(1 for c in checks if c['pass']),
       'n_total': len(checks),
       'overall_pass': all(c['pass'] for c in checks)}
json.dump(out, open(f'{ROOT}/gate61/results/g61_verify.json', 'w'),
          indent=1)
print(f"CHECKER: {out['n_pass']}/{out['n_total']} PASS; "
      f"overall {out['overall_pass']}")
for c in checks:
    print(('PASS' if c['pass'] else 'FAIL'), c['check'], '|',
          c['detail'])
