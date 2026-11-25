"""
wa_run.py -- Gate-13 W-A run order (registered in GATE13.md):
anchors FIRST, in order (i)-(v) (a failed anchor = machinery failure,
stop, no deciding number read past it), then the deciding row under
bars (a)-(h): economics FIRST, Type-I, region worsts, sampled-null,
the cavity settlement re-derived on this path, the floor-class
statement, the endpoint-residual read (f2), the i0.05 corroboration
row, and the mechanism spot-read (outer alone at beta=0.0725,
e=0.10 vs e=0.075).

DECIDING SET (stated here, before any deciding number is read): the
Phase 46/80/88/116 registered audit pattern -- 26 Fibonacci
directions (seed 11) x 50 radii (linspace(0.4, 14.5, 42) +
{2.1, 2.9, 3.9, 4.5, 5.1, 6.2, 7.8, 9.5}) = 1300 points, full volume
over payload / inner wall / cavity / outer wall / exterior;
significance threshold max(1e-11, 1e-3 |rho_peak|); region worsts
over Type-I significant points; sampled-null over 162 Fibonacci
directions.

CAVITY REFINEMENT ON THIS PATH (stated before running): this path
has no stencil, so its equivalent refinement is (1) exact-site DEC
reads at r = 4.526829 (the phase primary's flagged radius class),
r = 4.53 and r = 4.87 (the phase second-path floor site) over 26
and 162 directions, and (2) a radial density ladder over the cavity
band 4.0 < r < 5.0 at spacings 0.1 / 0.05 / 0.025 / 0.0125 (26 dirs),
recording min DEC in the near-edge shell 4.6 < r < 5 and in the full
cavity.  A convergent negative continuum value = rung minima
converging to a negative value as spacing -> 0.

ENDPOINT-RESIDUAL SENSITIVITY READ (stated before running, bar
(f2)): (i) the rebuilt chain's scalars (lambda, k, S_lo-1, S_hi,
balance) for the beta=0.0725 outer chain at e=0.10 are compared
with Phase 116's stored chain scalars; agreement to ~1e-9 means
the rebuilt profile IS the phase's profile up to spline
representation, so the residuals are a shared property of the
profile, not a discrepancy between paths; (ii) a
residual-corrected variant of the deciding outer S is built by
subtracting the linear ramp delta(r) with delta(lo) = S_lo-1,
delta(hi) = S_hi (constant continuation outside [lo, hi]), which
forces S_corr(lo) = 1 and S_corr(hi) = 0 exactly, and the deciding
audit is re-run with it: if every region worst keeps its sign and
stays within its factor-3 tolerance of the uncorrected read, the
residuals do not reach the deciding audit.

Run: ~/workspace/warp-pilot/venv/bin/python wa_run.py
float64 everywhere.
"""
import json
import sys
import time

import numpy as np
from scipy.interpolate import CubicSpline, interp1d

sys.path.insert(0, '/home/hatch/workspace/warp-pilot/gate13')
import wa_eval as ev
import wa_profiles as wp

F64 = np.float64
OUT = '/home/hatch/workspace/warp-pilot/gate13/results/wa_g131_numbers.json'
t0 = time.time()
res = {'item': 'G13-1 Gate-13 W-A symbolic radial-reduction audit',
       'run_with': '~/workspace/warp-pilot/venv/bin/python',
       'float': 'float64'}


def save():
    res['elapsed_s'] = time.time() - t0
    json.dump(res, open(OUT, 'w'), indent=1)


def log(msg):
    print(msg, flush=True)


# ================= ANCHOR (i): Minkowski identically zero =================
fns, _atoms = ev._load()
pts_m = np.array([[5.0, 1.0, 2.0], [-3.0, 4.0, 0.5],
                  [10.0, -2.0, 3.0], [17.0, 3.0, -6.0]])
r_m = np.linalg.norm(pts_m, axis=1)
n_m = pts_m / r_m[:, None]
z4 = np.zeros(4)
args_m = (r_m, n_m[:, 0], n_m[:, 1], n_m[:, 2], z4, z4, z4, z4, z4, z4, z4, z4, z4)
mx = 0.0
for fn in fns.values():
    mx = max(mx, float(np.max(np.abs(np.asarray(fn(*args_m), dtype=float)))))
res['anchor_i_minkowski_maxAbsG'] = mx
log(f'[A i] Minkowski max|G| = {mx:.3e} (bar < 1e-12)')
assert mx < 1e-12, 'ANCHOR (i) FAILED -- machinery failure, stop'
save()

# ================= profiles / composed background =================
prof_o = wp.outer_profile()
prof_i = wp.inner_profile()
comp = wp.composed_background(prof_o, prof_i)
a_comp = CubicSpline(comp['r'], comp['a'])
b_comp = CubicSpline(comp['r'], comp['b'])
a_alone_o = CubicSpline(prof_o['r'], prof_o['a'])
b_alone_o = CubicSpline(prof_o['r'], prof_o['b'])

# ================= ANCHOR (ii): beta=0 spherical T =================
ex = {k: interp1d(prof_o['r'], prof_o[k]) for k in ('rho_ex', 'p_r', 'p_t')}
rows = []
for rr in (6.0, 7.0, 7.5, 8.0, 9.0):
    p = np.array([[rr, 0.37, -0.21]])
    p = p * (rr / np.linalg.norm(p))
    m = ev.audit(p, a_alone_o, b_alone_o, ev.zero_vfunc)
    ps = np.sort(m['p'][0])
    exact = np.sort([float(ex['p_r'](rr)), float(ex['p_t'](rr)), float(ex['p_t'](rr))])
    rows.append({'r': rr, 'rho_mine': float(m['rho'][0]),
                 'rho_exact': float(ex['rho_ex'](rr)),
                 'rho_rel_err': float(abs(m['rho'][0] - ex['rho_ex'](rr))
                                      / max(abs(ex['rho_ex'](rr)), 1e-300)),
                 'p_max_abs_err': float(np.max(np.abs(ps - exact))),
                 'typeI': bool(m['typeI'][0])})
res['anchor_ii_static_rows'] = rows
res['anchor_ii_max_rho_rel_err'] = max(x['rho_rel_err'] for x in rows)
res['anchor_ii_max_p_abs_err'] = max(x['p_max_abs_err'] for x in rows)
log(f"[A ii] max rho rel err {res['anchor_ii_max_rho_rel_err']:.3e} (bar 3e-3); "
    f"max p abs err {res['anchor_ii_max_p_abs_err']:.3e} (bar 3e-7)")
assert res['anchor_ii_max_rho_rel_err'] <= 3e-3, 'ANCHOR (ii) rho FAILED'
assert res['anchor_ii_max_p_abs_err'] <= 3e-7, 'ANCHOR (ii) p FAILED'
save()

# ================= deciding set =================
pts, rad = wp.registered_points(10.0)
res['deciding_set'] = {'n_pts': int(len(pts)), 'n_radii': int(len(rad)),
                       'pattern': '26 Fibonacci dirs (seed 11) x 50 radii, '
                                  'Phase 46/80/88/116 registered pattern'}


def cavity_ladder(a_s, b_s, vfunc, spacings=(0.1, 0.05, 0.025, 0.0125)):
    dirs = wp.fib_sphere(26, 11)
    out = {}
    for h in spacings:
        radii = np.arange(4.0 + h, 5.0, h)
        pp = np.concatenate([dirs * rr for rr in radii])
        mm = ev.audit(pp, a_s, b_s, vfunc)
        rr_all = np.linalg.norm(pp, axis=1)
        dec, ti = mm['dec'], mm['typeI']

        def worst(mask):
            v = dec[mask & ti]
            v = v[~np.isnan(v)]
            return float(np.min(v)) if v.size else None
        out[str(h)] = {'n_pts': int(len(pp)),
                       'min_dec_near_edge_shell_4.6_5': worst((rr_all > 4.6) & (rr_all < 5.0)),
                       'min_dec_full_cavity': worst(np.ones(len(pp), bool)),
                       'typeI_frac': float(np.mean(ti)),
                       'min_sampled_nec': float(np.nanmin(mm['sampled_nec']))}
    return out


def site_read(a_s, b_s, vfunc, r_site, ndir):
    dirs = wp.fib_sphere(ndir, 11) if ndir == 26 else wp.fib_sphere_det(ndir)
    pp = dirs * r_site
    mm = ev.audit(pp, a_s, b_s, vfunc)
    dec, ti = mm['dec'], mm['typeI']
    v = dec[ti]
    v = v[~np.isnan(v)]
    return {'r': r_site, 'n_dir': ndir, 'typeI_frac': float(np.mean(ti)),
            'min_dec': float(np.min(v)) if v.size else None,
            'min_sampled_nec': float(np.nanmin(mm['sampled_nec']))}


# ================= ANCHOR (iii): control-span row e0.30_o0.06_i0.06 ======
xo_ctl = wp.outer_vector_88('e0.30', 'b0.06')
xi_ctl = wp.inner_vector('b0.06')
ch_o_ctl = wp.build_chain(prof_o, xo_ctl, 0.30)
ch_i_ctl = wp.build_chain(prof_i, xi_ctl, 0.30)
anat_ctl = wp.held_w(comp, prof_o, prof_i, 0.06, 0.06)
vf_ctl80 = ev.combine_vfunc(anat_ctl['beta_o_comp'], wp.chain_sfunc(ch_o_ctl),
                            anat_ctl['beta_i_comp'], wp.chain_sfunc(ch_i_ctl))
m_ctl80 = ev.audit(pts, a_comp, b_comp, vf_ctl80)
s_ctl80 = ev.summarise(m_ctl80, pts, wp.region_name)
cons_ctl80 = ev.conservation_read(pts, a_comp, b_comp, vf_ctl80)
res['anchor_iii_control_span'] = {
    'chains': {'outer': ch_o_ctl['info'], 'inner': ch_i_ctl['info'],
               'outer_stored': wp.stored_chain_info('outer88', 'e0.30', 'b0.06'),
               'inner_stored': wp.stored_chain_info('inner', beta_key='b0.06')},
    'economics': anat_ctl, 'audit': s_ctl80, 'conservation': cons_ctl80,
    'phase80_stored': {'cavity_raw': -1.107e-4, 'outer_wall': 3.2016e-5,
                       'conservation_rel_med': 0.0115},
    'factors': {
        'outer_wall_vs_stored': float(s_ctl80['regions']['outer_wall']['worst'] / 3.2016e-5),
        'conservation_vs_stored': float(cons_ctl80['rel_med'] / 0.0115),
        'cavity_site_abs_vs_raw_abs': None}}
site_ctl = site_read(a_comp, b_comp, vf_ctl80, 4.53, 26)
res['anchor_iii_control_span']['cavity_site_4.53_26dir'] = site_ctl
res['anchor_iii_control_span']['factors']['cavity_site_abs_vs_raw_abs'] = \
    float(abs(site_ctl['min_dec']) / 1.107e-4)
log(f"[A iii] control-span Type-I {s_ctl80['typeI_frac_sig']}; outer wall "
    f"{s_ctl80['regions']['outer_wall']['worst']:+.4e} (stored +3.2016e-5, factor "
    f"{res['anchor_iii_control_span']['factors']['outer_wall_vs_stored']:.2f}); "
    f"conservation rel_med {cons_ctl80['rel_med']:.4f} (stored 0.0115, factor "
    f"{res['anchor_iii_control_span']['factors']['conservation_vs_stored']:.2f}); "
    f"cavity site r=4.53 DEC {site_ctl['min_dec']:+.4e} (phase FD raw -1.107e-4)")
assert s_ctl80['typeI_frac_sig'] == 1.0, 'ANCHOR (iii) Type-I FAILED'
assert s_ctl80['regions']['outer_wall']['worst'] > 0
assert 1 / 3 <= res['anchor_iii_control_span']['factors']['outer_wall_vs_stored'] <= 3, \
    'ANCHOR (iii) outer-wall factor FAILED -- machinery failure, stop'
assert 1 / 3 <= res['anchor_iii_control_span']['factors']['conservation_vs_stored'] <= 3, \
    'ANCHOR (iii) conservation factor FAILED -- machinery failure, stop'
save()

# ================= ANCHOR (iv): THE 0.0799 CONTROL =================
sf_o_cos = wp.cosine_sfunc(5.0, 10.0)
sf_i_cos = wp.cosine_sfunc(2.0, 4.0)
BO_CTL, BI_CTL = 0.04774641838025745, 0.03225358161974255
vf_g8 = ev.combine_vfunc(BO_CTL, sf_o_cos, BI_CTL, sf_i_cos)
m_g8 = ev.audit(pts, a_comp, b_comp, vf_g8)
s_g8 = ev.summarise(m_g8, pts, wp.region_name)
res['anchor_iv_control_audit'] = s_g8
log(f"[A iv] 0.0799 control Type-I {s_g8['typeI_frac_sig']}")
for reg in ('payload', 'inner_wall', 'outer_wall', 'exterior'):
    log(f"   {reg}: worst {s_g8['regions'][reg]['worst']:+.4e}")
assert s_g8['typeI_frac_sig'] == 1.0, 'ANCHOR (iv) Type-I FAILED'
G8 = {'inner_wall': 9.79e-4, 'outer_wall': 4.05e-5, 'payload': 1.09e-4}
fac = {}
for reg, g8v in G8.items():
    w = s_g8['regions'][reg]['worst']
    assert w > 0, f'ANCHOR (iv) sign FAILED in {reg}'
    fac[reg] = float(w / g8v)
for reg in ('inner_wall', 'outer_wall'):
    assert 1 / 3 <= fac[reg] <= 3, f'ANCHOR (iv) factor-3 FAILED in {reg}: {fac[reg]}'
res['anchor_iv_control_factor_vs_gate8'] = fac
log(f'[A iv] control region factors vs Gate-8: {fac}')
ctl_rr = np.linalg.norm(pts, axis=1)
sel143 = np.isclose(ctl_rr, 1.431707)
sec143 = float(np.nanmin(m_g8['sec'][sel143])) if np.any(sel143) else None
res['anchor_iv_payload_site_read'] = {
    'gate8_judge_payload_worst': 1.09e-4, 'gate8_site_r': 1.431707,
    'this_path_sec_at_gate8_site': sec143,
    'factor_at_gate8_site': float(sec143 / 1.09e-4) if sec143 else None,
    'this_path_payload_region_worst': s_g8['regions']['payload']['worst']}
ctl_ladder = cavity_ladder(a_comp, b_comp, vf_g8)
res['anchor_iv_control_cavity_ladder'] = ctl_ladder
for h, e in ctl_ladder.items():
    log(f"   control cavity ladder h={h}: shell DEC {e['min_dec_near_edge_shell_4.6_5']:+.4e}, "
        f"full cavity {e['min_dec_full_cavity']:+.4e}, Type-I {e['typeI_frac']}")
# Gate-8 settlement consistency: no convergent negative continuum value
# = ladder near-edge minima do not converge to a negative value.
save()

# ================= ANCHOR (v): THE 0.09556 GATE-11 ROW =================
xo11 = wp.outer_vector_88('e0.10', 'b0.07')
xi11 = wp.inner_vector('b0.06')
anat11 = wp.held_w(comp, prof_o, prof_i, 0.07, 0.06)
ch_o11 = wp.build_chain(prof_o, xo11, 0.10)
ch_i11 = wp.build_chain(prof_i, xi11, 0.30)
vf11 = ev.combine_vfunc(anat11['beta_o_comp'], wp.chain_sfunc(ch_o11),
                        anat11['beta_i_comp'], wp.chain_sfunc(ch_i11))
m11 = ev.audit(pts, a_comp, b_comp, vf11)
s11 = ev.summarise(m11, pts, wp.region_name)
site11_26 = site_read(a_comp, b_comp, vf11, 4.53, 26)
site11_162 = site_read(a_comp, b_comp, vf11, 4.53, 162)
G11 = {'payload': 3.274e-6, 'inner_wall': 9.783e-4,
       'outer_wall': 4.852e-5, 'exterior': 2.087e-6}
fac11 = {}
for reg, gv in G11.items():
    w = s11['regions'][reg]['worst']
    assert w > 0, f'ANCHOR (v) sign FAILED in {reg}'
    fac11[reg] = float(w / gv)
    assert 1 / 3 <= fac11[reg] <= 3, f'ANCHOR (v) factor-3 FAILED in {reg}: {fac11[reg]}'
assert s11['typeI_frac_sig'] == 1.0, 'ANCHOR (v) Type-I FAILED'
assert s11['min_sampled_nec_all_sig'] > 0, 'ANCHOR (v) sampled-null FAILED'
assert abs(anat11['payload_relat'] - 0.0955573263) / 0.0955573263 <= 1e-4, \
    'ANCHOR (v) held payload FAILED'
assert site11_162['min_dec'] > 0, 'ANCHOR (v) cavity site FAILED'
res['anchor_v_gate11_row'] = {
    'economics': anat11, 'chains': {'outer': ch_o11['info'], 'inner': ch_i11['info']},
    'audit': s11, 'factors_vs_gate11_fresh': fac11,
    'gate11_fresh_reads': {'held_payload': 0.0955573263, 'typeI': 1.0,
                           'worsts': G11, 'sampled_null_min': 2.27e-6,
                           'cavity_site_r4.53_dec_class': 2.00e-4},
    'cavity_site_4.53_26dir': site11_26, 'cavity_site_4.53_162dir': site11_162,
    'sampled_factor_vs_gate11': float(s11['min_sampled_nec_all_sig'] / 2.27e-6),
    'cavity_site_factor_vs_gate11_class': float(site11_162['min_dec'] / 2.00e-4)}
log(f"[A v] Gate-11 row: payload {anat11['payload_relat']:.10f} (Gate-11 0.0955573263); "
    f"Type-I {s11['typeI_frac_sig']}; sampled {s11['min_sampled_nec_all_sig']:+.4e} "
    f"(Gate-11 +2.27e-6); site r=4.53 DEC {site11_162['min_dec']:+.4e} (Gate-11 +2.00e-4 class)")
for reg in G11:
    log(f"   {reg}: worst {s11['regions'][reg]['worst']:+.4e} (factor {fac11[reg]:.2f} vs Gate-11)")
save()

# ================= DECIDING ROW: economics FIRST (bar a) =================
xo = wp.outer_vector_116('e0.10', 'b0.0725')
xi = wp.inner_vector('b0.06')
anat = wp.held_w(comp, prof_o, prof_i, 0.0725, 0.06)
res['deciding_economics'] = anat
CLAIM_PAYLOAD = 0.0975831574914493
CLAIM_WSUM = 0.17590965427919802
rel_p = abs(anat['payload_relat'] - CLAIM_PAYLOAD) / CLAIM_PAYLOAD
rel_w = abs(anat['W_payload_sum'] - CLAIM_WSUM) / CLAIM_WSUM
res['deciding_economics_rel_err'] = {
    'payload_vs_claim': float(rel_p), 'Wsum_vs_claim': float(rel_w),
    'W_held_max_rel_err': float(max(anat['W_i_rel_err'], anat['W_o_rel_err']))}
log(f"[E] deciding held payload {anat['payload_relat']:.13f} (rel err vs claim: "
    f"{rel_p:.2e}, bar 1e-4); W sum {anat['W_payload_sum']:.14f} (rel err {rel_w:.2e}); "
    f"held-W err {max(anat['W_i_rel_err'], anat['W_o_rel_err']):.2e}; beta_o_comp "
    f"{anat['beta_o_comp']:.14f}, beta_i_comp {anat['beta_i_comp']:.14f}")
assert rel_p <= 1e-4, 'BAR (a) FAILED'
save()

# ================= chains + stored comparison (bar f2, part i) ============
ch_o = wp.build_chain(prof_o, xo, 0.10)
ch_i = wp.build_chain(prof_i, xi, 0.30)
res['deciding_chains'] = {
    'outer': ch_o['info'], 'inner': ch_i['info'],
    'outer_stored': wp.stored_chain_info('outer116', 'e0.10', 'b0.0725'),
    'inner_stored': wp.stored_chain_info('inner', beta_key='b0.06')}
so = res['deciding_chains']['outer_stored']
log(f"[F2] rebuilt outer chain e=0.10 beta=0.0725: lam {ch_o['info']['lam']:.12f} "
    f"(stored {so['lam']:.12f}), k {ch_o['info']['k']:.12f} (stored {so['k']:.12f}), "
    f"S_lo-1 {ch_o['info']['S_lo_minus1']:+.4e} (stored {so['S_lo_minus1']:+.4e}), "
    f"S_hi {ch_o['info']['S_hi']:+.4e} (stored {so['S_hi']:+.4e}), "
    f"balance {ch_o['info']['balance_rel']:.2e} (stored {so['balance_rel']:.2e})")
save()

# ================= DECIDING ROW: legality (bars b, c, d) =================
sf_o = wp.chain_sfunc(ch_o)
sf_i = wp.chain_sfunc(ch_i)
vf_dec = ev.combine_vfunc(anat['beta_o_comp'], sf_o, anat['beta_i_comp'], sf_i)
m_dec = ev.audit(pts, a_comp, b_comp, vf_dec)
s_dec = ev.summarise(m_dec, pts, wp.region_name)
cons_dec = ev.conservation_read(pts, a_comp, b_comp, vf_dec)
res['deciding_audit'] = s_dec
res['deciding_conservation'] = cons_dec
PHASE_WORSTS = {'payload': 3.84e-6, 'inner_wall': 1.191e-3,
                'outer_wall': 3.394e-5, 'exterior': 1.107e-6}
res['deciding_factors_vs_phase'] = {
    reg: float(s_dec['regions'][reg]['worst'] / v) for reg, v in PHASE_WORSTS.items()}
log(f"[D] deciding Type-I {s_dec['typeI_frac_sig']}, sampled-null min "
    f"{s_dec['min_sampled_nec_all_sig']:+.4e} (phase +1.13e-6), conservation rel_med "
    f"{cons_dec['rel_med']:.4f} (phase 0.0117)")
for reg, e in s_dec['regions'].items():
    log(f"   {reg}: worst {e['worst']:+.4e} ({e['worst_kind']}) at r={e.get('worst_r')}")
save()

# ================= CAVITY SETTLEMENT (bar e) + FLOOR CLASS (bar f) ========
cav = {}
for r_site in (4.526829, 4.53, 4.87):
    cav[f'site_{r_site}_26dir'] = site_read(a_comp, b_comp, vf_dec, r_site, 26)
    cav[f'site_{r_site}_162dir'] = site_read(a_comp, b_comp, vf_dec, r_site, 162)
dec_ladder = cavity_ladder(a_comp, b_comp, vf_dec)
cav['radial_density_ladder'] = dec_ladder
cav['deciding_set_cavity_region'] = s_dec['regions'].get('cavity')
res['deciding_cavity_settlement'] = cav
for k, e in cav.items():
    if isinstance(e, dict) and 'min_dec' in e and 'min_sampled_nec' in e:
        log(f"   cavity {k}: DEC {e['min_dec']:+.4e}, Type-I {e['typeI_frac']}, "
            f"sampled {e['min_sampled_nec']:+.4e}")
for h, e in dec_ladder.items():
    log(f"   deciding cavity ladder h={h}: shell DEC {e['min_dec_near_edge_shell_4.6_5']:+.4e}, "
        f"full cavity {e['min_dec_full_cavity']:+.4e}, Type-I {e['typeI_frac']}")
save()

# ================= RESIDUAL SENSITIVITY (bar f2, part ii) =================
info_o = ch_o['info']
lo_e, hi_e = info_o['lo'], info_o['hi']
d_lo, d_hi = info_o['S_lo_minus1'], info_o['S_hi']
S_grid = ch_o['S']
rr_grid = ch_o['r']
ramp = np.where(rr_grid < lo_e, d_lo,
                np.where(rr_grid > hi_e, d_hi,
                         d_lo + (d_hi - d_lo) * (rr_grid - lo_e) / (hi_e - lo_e)))
S_corr = CubicSpline(rr_grid, S_grid - ramp)


def sf_corr(rr):
    rr = np.asarray(rr, dtype=F64)
    rc = np.clip(rr, 0.0, float(rr_grid[-1]))
    S, S1, S2 = S_corr(rc), S_corr(rc, 1), S_corr(rc, 2)
    out = rr > float(rr_grid[-1])
    if np.any(out):
        S = np.where(out, 0.0, S); S1 = np.where(out, 0.0, S1); S2 = np.where(out, 0.0, S2)
    return S, S1, S2


vf_corr = ev.combine_vfunc(anat['beta_o_comp'], sf_corr, anat['beta_i_comp'], sf_i)
m_corr = ev.audit(pts, a_comp, b_comp, vf_corr)
s_corr = ev.summarise(m_corr, pts, wp.region_name)
res['residual_sensitivity_corrected_audit'] = s_corr
res['residual_sensitivity_factors'] = {
    reg: float(s_corr['regions'][reg]['worst'] / s_dec['regions'][reg]['worst'])
    for reg in PHASE_WORSTS}
log(f"[F2] residual-corrected audit: Type-I {s_corr['typeI_frac_sig']}")
for reg, e in s_corr['regions'].items():
    log(f"   {reg}: worst {e['worst']:+.4e} (uncorrected {s_dec['regions'][reg]['worst']:+.4e})")
save()

# ================= CORROBORATION (bar g): the i0.05 row ===================
xi2 = wp.inner_vector('b0.05')
anat2 = wp.held_w(comp, prof_o, prof_i, 0.0725, 0.05)
ch_i2 = wp.build_chain(prof_i, xi2, 0.30)
sf_i2 = wp.chain_sfunc(ch_i2)
vf2 = ev.combine_vfunc(anat2['beta_o_comp'], sf_o, anat2['beta_i_comp'], sf_i2)
m2 = ev.audit(pts, a_comp, b_comp, vf2)
s2 = ev.summarise(m2, pts, wp.region_name)
cav2 = {'site_4.53_26dir': site_read(a_comp, b_comp, vf2, 4.53, 26),
        'site_4.53_162dir': site_read(a_comp, b_comp, vf2, 4.53, 162),
        'site_4.87_162dir': site_read(a_comp, b_comp, vf2, 4.87, 162),
        'radial_density_ladder': cavity_ladder(a_comp, b_comp, vf2)}
res['corroboration_row'] = {'economics': anat2, 'audit': s2,
                            'inner_chain': ch_i2['info'], 'cavity': cav2}
log(f"[G] corroboration payload {anat2['payload_relat']:.11f} (claim 0.09118184734247374), "
    f"Type-I {s2['typeI_frac_sig']}, sampled {s2['min_sampled_nec_all_sig']:+.4e}")
for reg, e in s2['regions'].items():
    log(f"   {reg}: worst {e['worst']:+.4e}")
save()

# ================= MECHANISM SPOT-READ (bar h) ============================
mech = {}
for ext_key, ext in (('e0.10', 0.10), ('e0.075', 0.075)):
    xv = wp.outer_vector_116(ext_key, 'b0.0725')
    chv = wp.build_chain(prof_o, xv, ext)
    lo_v, hi_v = chv['info']['lo'], chv['info']['hi']
    vfv = ev.single_vfunc(0.0725, wp.chain_sfunc(chv))
    mv = ev.audit(pts, a_alone_o, b_alone_o, vfv)
    sv = ev.summarise(mv, pts, lambda rr, lo=lo_v, hi=hi_v:
                      wp.alone_region_name(rr, lo, hi), regions=ev.ALONE_REGIONS)
    mech[ext_key] = {'chain': chv['info'],
                     'chain_stored': wp.stored_chain_info('outer116', ext_key, 'b0.0725'),
                     'audit': sv}
    log(f"[H] outer alone beta=0.0725 {ext_key}: Type-I {sv['typeI_frac_sig']:.4f}, "
        f"worst {sv['worst']:+.4e}, sampled-null min {sv['min_sampled_nec_all_sig']:+.4e}")
    for reg, e in sv['regions'].items():
        log(f"   {reg}: worst {e['worst']:+.4e}, Type-I {e['typeI_frac']}, "
            f"sampled {e['min_sampled_nec_all']:+.4e}")
res['mechanism_alone'] = mech
save()
log(f'[run] DONE in {time.time()-t0:.0f}s')
