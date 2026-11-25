"""P72-1 checker: recomputes every verdict-carrying number from
results/p721_results.json + results/p721_second_path.json and
asserts the registered bars. Prints the verdict logic."""
import json, numpy as np

R = json.load(open('results/p721_results.json'))
S = json.load(open('results/p721_second_path.json'))
ok = []
def chk(name, cond):
    ok.append((name, bool(cond))); print(('PASS' if cond else 'FAIL'), name)

chk('G1 Ellis traveller tidal matches P23-3 value', R['gates']['G1_pass'])
chk('G3 GR gate (Ellis demands)', R['gates']['G3_pass'])

# (i) every audited S-A row fails NEC and DEC by a converged margin
for qe in ['0.25', '0.5', '0.75', '0.9']:
    e = R['part_i'][f'Qe_{qe}']
    chk(f'S-A Qe={qe} NEC1 fails by converged margin (<-1e-3, grid-stable)',
        e['NEC1_min_fine'] < -1e-3 and abs(e['NEC1_min_fine'] - e['NEC1_min_coarse']) < 0.01 * abs(e['NEC1_min_fine']) + 1e-9)
    chk(f'S-A Qe={qe} DEC_r fails', e['DEC_r_min_fine'] < -1e-3)
    c = S['part_i_cross'][f'Qe_{qe}']
    chk(f'S-A Qe={qe} NEC1 min = analytic throat value (1-Qe^2)/(8pi)',
        abs(c['NEC1_throat_analytic'] - c['NEC1_min_numeric']) < 1e-9)
    chk(f'S-A Qe={qe} spinor non-normalizable (nonzero at infinity, analytic match)',
        abs(c['spinor_inf_analytic'] - c['spinor_inf_numeric_Q']) < 1e-6 and c['spinor_inf_analytic'] > 0.05)
    chk(f'S-A Qe={qe} crossing at r0star passes 1-day bar', e['crossing']['r0star']['proper_s'] < 86400 and e['crossing']['r0star']['external_s'] < 86400)

# (ii) mu=0: no closing datum, floor = 2|beta| in G-2T units
for shape, beta in [('ellis', -1.0), ('sqrt', 0.5)]:
    chk(f'(ii) {shape} mu=0 no closing datum (floor 2|beta|)',
        abs(S['mu0_floor'][shape]['min_max_resid_over_A_C_family'] - 2 * abs(beta)) < 1e-6
        and not R['part_ii'][f'{shape}_mu0.0']['closing'])
# (ii) mu>0: closes at throat <=1e-10, second path agrees <=1e-8 on datum,
#      but domain obstruction: breach + blow-up before 1e3 r0, both paths
for shape in ['ellis', 'sqrt']:
    for mu in ['0.2', '1.0']:
        e = R['part_ii'][f'{shape}_mu{mu}']
        chk(f'(ii) {shape} mu={mu} throat closes <=1e-10',
            e['closing'] and max(abs(v) for v in e['throat_residuals'].values()) <= 1e-10)
        chk(f'(ii) {shape} mu={mu} second-path datum agrees <=1e-8',
            S['throat_fsolve'][f'{shape}_mu{mu}']['diff_vs_main'] <= 1e-8)
        b2 = S['extension_rk4'][f'{shape}_mu{mu}']
        chk(f'(ii) {shape} mu={mu} domain obstruction: breach in (1,1e3), paths agree',
            1 < e['domain_breach_R_over_r0'] < 1000 and abs(b2['breach_R'] - e['domain_breach_R_over_r0']) / e['domain_breach_R_over_r0'] < 1e-3)
        chk(f'(ii) {shape} mu={mu} spinor blow-up before 1e3 r0',
            e['spinor_blowup_R_over_r0'] is not None and e['spinor_blowup_R_over_r0'] < 1000)

kill_i = all(R['part_i'][f'Qe_{q}']['NEC1_min_fine'] < -1e-3 for q in ['0.25', '0.5', '0.75', '0.9'])
kill_ii = True  # established by the (ii) checks above: mu=0 no datum; mu>0 only with obstruction
allpass = all(c for _, c in ok)
print(f'\n{sum(c for _, c in ok)}/{len(ok)} checks pass')
print('KILL clause (i):', kill_i, ' KILL clause (ii):', kill_ii)
print('VERDICT:', 'KILL' if (allpass and kill_i and kill_ii) else 'SEE MEMO — checker did not fully pass')
