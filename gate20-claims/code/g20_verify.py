#!/usr/bin/env python3
"""GATE-20 independent verification driver (adversarial).
Written by the Gate-20 coordinator from the registrations, NOT copied
from phase178's stage scripts or checker. Parts B/D use the registered
gate-path primitives (p1711_common / p1763_common) -- that machinery IS
the instrument the gate is defined on; priced in GATE20.md.
Part A and the T9 comparisons are pure arithmetic on stored files.
"""
import json, sys
import numpy as np

WP = '/home/hatch/workspace/warp-pilot'
sys.path.insert(0, WP + '/phase176/work')
sys.path.insert(0, WP + '/phase171/work')

out = {}
def rep(k, v):
    out[k] = v
    print(k, '=', v, flush=True)

R = json.load(open(WP + '/phase178/results/p1781_results.json'))
ST178 = np.load(WP + '/phase178/work/p1781_state.npz')
S176 = np.load(WP + '/phase176/work/p1763_state.npz')
G178 = np.load(WP + '/phase178/work/p1781_grad.npz')

# ---------- PART A: pure arithmetic ----------
d_npz = ST178['d_final']
d_json = np.array(R['witness']['d'])
rep('A1 d npz-vs-json maxdiff', float(np.max(np.abs(d_npz - d_json))))
d = d_npz
rep('A2 norm_d', float(np.linalg.norm(d)))
rep('A2 max_coeff', float(np.max(np.abs(d))))
rep('A2 norm_expected', R['gate']['c_response_sizes']['norm'])
ETA_J = 1.00168500225718
sig_cut = ETA_J * (np.sqrt(224) + np.sqrt(72))
rep('A3 sigma_cut recomputed', float(sig_cut))
rep('A3 sigma_cut claimed', R['gate']['c_response_sizes']['sigma_cut'])
res0, scales, J = S176['res0'], S176['scales'], S176['J_coupled_Ea']
U, sv, Vt = np.linalg.svd(J, full_matrices=False)
floor = float(np.sqrt(max(float(np.sum(res0**2) - np.sum((U.T @ res0)**2)), 0.0) / 224.0))
rep('A4 coupled LS floor (own SVD)', floor)
lin_cl = float(np.sqrt(np.mean((res0 + J @ d)**2)))
rep('A5 witness linearised closure (own)', lin_cl)
y = Vt @ d
frac = float(np.sum(y[sv < sig_cut]**2) / np.sum(y**2))
rep('A6 frac ||d||^2 below sigma_cut (own SVD)', frac)
rep('A6 frac claimed', R['gate']['c_response_sizes']['frac_below_sigcut'])
rep('A7 n singular values below cut', int(np.sum(sv < sig_cut)))
rep('A7 sub-cut sigmas', [float(s) for s in sv[sv < sig_cut]])
# stored-q arithmetic
q41, q44 = R['witness']['exact']['q41'], R['witness']['exact']['q44']
rep('A8 dq41 from stored q', q41 - 1.0032717740717199)
rep('A8 dq44 from stored q', q44 - 1.1029635664194024)
# T9 stored gate-(a) targets vs claim (pure JSON)
T9 = json.load(open(WP + '/phase97/results/t9_results.json'))
for i, nm in ((41, '41'), (44, '44')):
    rep(f'A9 T9 c2[{nm}] stored', T9['two_layer']['counter_rigid']['Fr_c2'][i])
    rep(f'A9 claim c2[{nm}]', R['gate']['a_fixed_path']['reads'][nm]['c2_reproduced'])
    rep(f'A9 T9 survival[{nm}] stored', T9['survival'][nm]['survival_rigid'])
    rep(f'A9 claim survival[{nm}]', R['gate']['a_fixed_path']['reads'][nm]['survival_reproduced'])

# ---------- PART B: registered-path exact reads ----------
import p1763_common as X
import p1711_common as C
import p762_lib as L

basis = X.BASES['Ea']
gf0 = X.make_gf_enriched(np.zeros(72), basis)
fr0 = C.reads(gf0)
rep('B1 d=0 q', [float(fr0['q_r'][i]) for i in (41, 44)])
rep('B1 d=0 count', int(np.sum(fr0['typeI'])))
Et0, _ = C.pose_E_coupledIa(gf0)
dR0, _, _ = C.residual_frame(gf0, Et0)
cl0 = float(np.sqrt(np.mean(X.resvec(dR0, scales)**2)))
rep('B2 exact closure at d=0', cl0)
rep('B2 RMS(res0) from state', float(np.sqrt(np.mean(res0**2))))

gfw = X.make_gf_enriched(d, basis)
Etw, _ = C.pose_E_coupledIa(gfw)
dRw, _, _ = C.residual_frame(gfw, Etw)
clw = float(np.sqrt(np.mean(X.resvec(dRw, scales)**2)))
rep('B3 witness EXACT coupled closure', clw)
rep('B3 claimed', R['witness']['exact']['closure_rms_coupledIa'])
Etf, _ = C.pose_E_frozenIa(gfw)
dRf, _, _ = C.residual_frame(gfw, Etf)
clf = float(np.sqrt(np.mean(X.resvec(dRf, scales)**2)))
rep('B4 witness closure under FROZEN Ia (contrast)', clf)
frw = C.reads(gfw)
rep('B5 witness q41', float(frw['q_r'][41]))
rep('B5 witness q44', float(frw['q_r'][44]))
rep('B5 witness dq41', float(frw['q_r'][41]) - X.STORED_Q[0])
rep('B5 witness dq44', float(frw['q_r'][44]) - X.STORED_Q[1])
rep('B5 witness TypeI sites', [bool(frw['typeI'][i]) for i in (41, 44)])
rep('B5 witness count', int(np.sum(frw['typeI'])))
Dr = np.array(frw['D_r'])
rep('B6 witness D_r[44]', float(Dr[44]))
rep('B6 witness D_r[41]', float(Dr[41]))
rep('B6 min |D_r| over subset', float(np.min(np.abs(Dr))))
rep('B6 argmin |D_r|', int(np.argmin(np.abs(Dr))))
rep('B6 five smallest |D_r|', sorted([float(v) for v in np.abs(Dr)])[:5])
# floor-witness control (P176-3)
fw = S176['witness_coupled_Ea']
gff = X.make_gf_enriched(fw, basis)
Etf2, _ = C.pose_E_coupledIa(gff)
dRf2, _, _ = C.residual_frame(gff, Etf2)
rep('B7 P176-3 floor witness exact closure', float(np.sqrt(np.mean(X.resvec(dRf2, scales)**2))))
rep('B7 claimed', R['controls']['floor_witness_exact_closure'])
frf = C.reads(gff)
rep('B7 floor witness dq', [float(frf['q_r'][41]) - X.STORED_Q[0], float(frf['q_r'][44]) - X.STORED_Q[1]])
rep('B7 floor witness count', int(np.sum(frf['typeI'])))
# clause (c) max field value
Cu, Ca, Cb = X.field_value_contribs(basis)
mf = float(max(np.abs(Cu @ d).max(), np.abs(Ca @ d).max(), np.abs(Cb @ d).max()))
rep('B8 max field value at subset points', mf)
rep('B8 claimed', R['gate']['c_response_sizes']['max_field_value'])

# fragility probes: small perturbations of the witness, exact reads
rng = np.random.default_rng(20261123)
for scale in (1e-6, 1e-5):
    for t in range(2):
        delta = rng.standard_normal(72); delta *= scale / np.linalg.norm(delta)
        frp = C.reads(X.make_gf_enriched(d + delta, basis))
        rep(f'B9 perturb {scale} #{t} count', int(np.sum(frp['typeI'])))
        rep(f'B9 perturb {scale} #{t} TypeI sites', [bool(frp['typeI'][i]) for i in (41, 44)])
        rep(f'B9 perturb {scale} #{t} dq', [float(frp['q_r'][41]) - X.STORED_Q[0], float(frp['q_r'][44]) - X.STORED_Q[1]])
# directed probe: push D_r(44) through zero along its own gradient
GD = G178['GD']
g44row = GD[44]
delta = -np.sign(Dr[44]) * g44row / np.dot(g44row, g44row) * (abs(float(Dr[44])) + 1e-6)
frd = C.reads(X.make_gf_enriched(d + delta, basis))
rep('B10 directed D_r44-flip probe: ||delta||', float(np.linalg.norm(delta)))
rep('B10 directed probe count', int(np.sum(frd['typeI'])))
rep('B10 directed probe TypeI[44]', bool(frd['typeI'][44]))

# ---------- PART C: strict extension of the P171-1 instrument ----------
S171 = np.load(WP + '/phase171/work/p1711_state.npz')
w48 = S171['witness']
w72 = np.zeros(72)
for fi in range(3):
    for k in range(8):
        for l in range(2):
            w72[fi * 24 + k * 3 + l] = w48[fi * 16 + k * 2 + l]
dc_old = C.diag_pack(w48)
g_old = C.make_gf(diag_c=dc_old)
g_new = X.make_gf_enriched(w72, basis)
pts = C.pts
rep('C1 metric maxdiff old-vs-enriched (P4=0 embedding)', float(np.max(np.abs(g_old(pts) - g_new(pts)))))
Etc, _ = C.pose_E_coupledIa(g_new)
dRc, _, _ = C.residual_frame(g_new, Etc)
rep('C2 embedded P171-1 witness exact closure via enriched path', float(np.sqrt(np.mean(X.resvec(dRc, scales)**2))))
rep('C2 P171-1 stored exact closure of its coupled witness', 0.632732)
frc = C.reads(g_new)
rep('C3 embedded witness dq via enriched path', [float(frc['q_r'][41]) - X.STORED_Q[0], float(frc['q_r'][44]) - X.STORED_Q[1]])
rep('C3 P171-1 stored exact dq of floor field', [7.06e-3, 1.84e-2])

# ---------- PART D: gate (a) fixed-path replication (own arrangement) ----------
EIGHT_PI = 8.0 * np.pi
bed, coeff0, Ea0 = C.bed, C.coeff0, C.Ea0
def That_cf(lam):
    E1, g = C.species_E(bed.gf, coeff0, +lam)
    E2, _ = C.species_E(bed.gf, coeff0, -lam)
    return L.that_in_frame(g, (Ea0 + E1 + E2) / EIGHT_PI, pts)
That0 = L.that_in_frame(C.g_b, C.E_base / EIGHT_PI, pts)
vals = {0.0: That0}
for hh in (0.02, 0.01):
    for s in (+1, -1):
        vals[s * hh] = That_cf(s * hh)
def rich2(v, h=0.02):
    c = lambda hh: (v[hh] - 2 * v[0.0] + v[-hh]) / hh**2
    return (4 * c(h / 2) - c(h)) / 3
c2 = rich2({k: v[:, 0, 1] for k, v in vals.items()})
for i, nm in ((41, '41'), (44, '44')):
    sc = T9['two_layer']['counter_rigid']['Fr_c2'][i]
    sb = T9['single_layer']['both_lin']['Fr_c2'][i]
    surv = float(c2[i] / sb)
    ss = T9['survival'][nm]['survival_rigid']
    rep(f'D gate(a) site {nm} c2 own', float(c2[i]))
    rep(f'D gate(a) site {nm} c2 reldiff vs T9', abs(float(c2[i]) - sc) / abs(sc))
    rep(f'D gate(a) site {nm} survival own', surv)
    rep(f'D gate(a) site {nm} survival reldiff vs T9', abs(surv - ss) / ss)

json.dump(out, open(WP + '/gate20/work/g20_verify_out.json', 'w'), indent=1, default=str)
print('DONE')
