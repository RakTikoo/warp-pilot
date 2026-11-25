#!/usr/bin/env python
"""GATE-31 independent checker. Recomputes, from the
stored per-grid window rows in gate31/work/
g31_results.json only (plus the spot recomputation
below):
  - the per-instant per-binding-clause Richardson table
    (registration sec.1, verbatim cases) and CERT-1..4;
  - CTRL-3 at t=0.5 from the same rows;
  - verdict-form consistency under sec.4's decision
    order, from the recorded controls / probe / CERT;
  - protected-engine md5 identity (current vs recorded
    before/after).
Spot recomputation: the bracket instants' G4 reads
(t=0.575 -> m=920, t=0.58125 -> m=930 on the stored G4
member state, phase288/work/p288_member_state.npz) via
phase288's read_arm_A with the member profiles; must
match the results' fresh G4 window rows at max abs diff
0.0 (clause minima and mom_resid_max).
Writes gate31/results/g31_verify.json. Nothing else
written."""
import hashlib, json, math, sys
import numpy as np

WP = '/home/hatch/workspace/warp-pilot/'
sys.path.insert(0, WP + 'phase288/work')
import p288_lib as L              # noqa: E402

RES = json.load(open(WP + 'gate31/work/g31_results.json'))
PROTECTED = [WP + 'phase169/work/p1692_engine.py',
             WP + 'phase167/work/p167_engine.py',
             WP + 'phase162/work/p1621_engine.py']
WINDOW = RES['window']
T_LO, T_HI = RES['bracket']
BINDING = RES['binding_clauses']
CK = ['NEC_rho', 'NEC_th', 'NEC_ph', 'WEC', 'DEC_rho',
      'DEC_th', 'DEC_ph']
BAR = 1e-6
out = {'checker': 'g31_check.py (independent)'}


def row(gname, t):
    return [r for r in RES['per_grid_window_rows'][gname]
            if abs(r['t'] - t) < 1e-12][0]


def rich(v3, v4, v5):
    d34, d45 = v3 - v4, v4 - v5
    if d34 * d45 > 0.0:
        p = math.log2(d34 / d45)
        if 0.5 <= p <= 6.0:
            Lv = v5 - d45 / (2.0 ** p - 1.0)
            return d34, d45, 'monotone', p, Lv, abs(Lv - v5)
        return d34, d45, 'degenerate_inadmissible_p', p, v5, \
            max(abs(d34), abs(d45))
    return d34, d45, 'degenerate', None, v5, \
        max(abs(d34), abs(d45))


# ---- Richardson + CERT recomputation ----
table = []
max_tab_diff = 0.0
stored_tab = {e['t']: e for e in RES['richardson_table']}
for t in WINDOW:
    entry = {}
    for kk in BINDING:
        v3 = row('g3', t)['clause_minima'][kk]
        v4 = row('g4', t)['clause_minima'][kk]
        v5 = row('g5', t)['clause_minima'][kk]
        d34, d45, case, p, Lv, r = rich(v3, v4, v5)
        cert = bool(r <= BAR and abs(d34) <= BAR
                    and abs(d45) <= BAR)
        entry[kk] = {'L': Lv, 'v5': v5, 'cert': cert}
        s = stored_tab[t][kk]
        for a, b in ((Lv, s['L']), (r, s['r']),
                     (d34, s['d34']), (d45, s['d45']),
                     (v5, s['v5'])):
            max_tab_diff = max(max_tab_diff, abs(a - b))
        assert case == s['case'] and cert == \
            s['limit_certified'], (t, kk, case, s['case'])
    table.append((t, entry))
by_t = dict(table)
cert = {}
cert['CERT-1'] = all(e[kk]['cert'] for _, e in table
                     for kk in BINDING)
cert['CERT-2'] = all(
    by_t[T_LO][kk]['L'] >= 0.0 and by_t[T_HI][kk]['L'] < 0.0
    and by_t[T_LO][kk]['v5'] >= 0.0
    and by_t[T_HI][kk]['v5'] < 0.0 for kk in BINDING)
cert['CERT-3'] = all(
    e[kk]['L'] >= 0.0 and e[kk]['v5'] >= 0.0
    for t, e in table if t <= T_LO + 1e-12 for kk in BINDING)
nonbinding = [k for k in CK if k not in BINDING]
c4_rows = all(row('g5', t)['clause_minima'][kk] > 0.0
              for t in WINDOW if t <= T_HI + 1e-12
              for kk in nonbinding)
bars_ok = True
for tstr, b in RES['nonclause_bars_g5'].items():
    ok = bool(b['mom_worst'] <= 1e-10 and b['flare_min'] > 0.0
              and b['domain_R_min'] > 0.0
              and b['domain_exp2Phi_min'] > 0.0)
    bars_ok = bars_ok and ok and b['pass']
cert['CERT-4'] = bool(c4_rows and bars_ok)
out['richardson_recomputed_max_abs_diff_vs_stored'] = \
    float(max_tab_diff)
out['cert_recomputed'] = cert
out['cert_match_stored'] = bool(all(
    cert[k] == RES['cert'][k]['pass'] for k in cert))

# ---- CTRL-3 recomputation at t = 0.5 ----
c3 = True
for kk in BINDING:
    v3 = row('g3', 0.5)['clause_minima'][kk]
    v4 = row('g4', 0.5)['clause_minima'][kk]
    v5 = row('g5', 0.5)['clause_minima'][kk]
    c3 = c3 and abs(v3 - v4) <= BAR and abs(v4 - v5) <= BAR
out['ctrl3_recomputed_pass'] = bool(c3)
out['ctrl3_match_stored'] = bool(
    c3 == RES['controls']['CTRL-3']['pass'])

# ---- spot recomputation: bracket G4 reads, diff 0.0 ----
z287 = np.load(WP + 'phase287/work/'
               'p287_built_profiles_amended.npz')
auu = np.array(z287['Auu_new'], dtype=np.float64)
jder = np.array(z287['J_derived'], dtype=np.float64)
z = np.load(WP + 'phase288/work/p288_member_state.npz')
state = (np.array(z['MU']), np.array(z['U']),
         np.array(z['MTT']), np.array(z['th_f']),
         np.array(z['times']))
spot = {}
spot_max = 0.0
for t, m in ((0.575, 920), (0.58125, 930)):
    r = L.read_arm_A(m, state, auu, jder)
    ref = row('g4', t)
    d = 0.0
    for kk in CK:
        d = max(d, abs(r['clause_minima'][kk]
                       - ref['clause_minima'][kk]))
    for kk in ('mom_rho', 'mom_th', 'mom_ph'):
        d = max(d, abs(r['mom_resid_max'][kk]
                       - ref['mom_resid_max'][kk]))
    spot[str(t)] = {'march_index': m, 'max_abs_diff': float(d)}
    spot_max = max(spot_max, d)
out['spot_recompute_bracket_g4'] = spot
out['spot_recompute_max_abs_diff'] = float(spot_max)
out['spot_recompute_pass_diff0'] = bool(spot_max == 0.0)

# ---- verdict-form consistency under sec.4 ----
c = RES['controls']
if not c['CTRL-1']['pass']:
    expected = 'FAILS-(b)'
elif not c['CTRL-2']['pass']:
    expected = 'FAILS-(a)'
elif RES['probe']['fires']:
    expected = 'FAILS-(c)'
elif not c['CTRL-3']['pass']:
    expected = 'FAILS-(a)'
elif not all(cert.values()):
    expected = 'FAILS-(a)'
else:
    expected = 'SURVIVES'
out['verdict_expected_form'] = expected
out['verdict_recorded'] = RES['verdict_form']
out['verdict_consistent'] = bool(
    RES['verdict_form'].startswith(expected))

# ---- protected md5 identity ----
cur = {p: hashlib.md5(open(p, 'rb').read()).hexdigest()
       for p in PROTECTED}
out['md5_current'] = cur
out['md5_identity_pass'] = bool(
    cur == RES['md5_protected_before']
    and cur == RES['md5_protected_after']
    and c['CTRL-4'])

out['all_pass'] = bool(
    out['richardson_recomputed_max_abs_diff_vs_stored'] == 0.0
    and out['cert_match_stored'] and out['ctrl3_match_stored']
    and out['spot_recompute_pass_diff0']
    and out['verdict_consistent'] and out['md5_identity_pass'])
json.dump(out, open(WP + 'gate31/results/g31_verify.json',
                    'w'), indent=1)
print(json.dumps(out, indent=1))
print('CHECKER ALL PASS:', out['all_pass'])
