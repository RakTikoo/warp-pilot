#!/usr/bin/env python3
"""p1083_main.py -- P108-3 (FU-P106-2a): the force-alignment set.

Registration: phase108/CHECKPOINT108.md S.P108-3; algebraic
signature and definitions stated in results/p1083_run_record.md
BEFORE this computation. Corpus: the seven unique stored
configurations in phase101/results/p1015_partB_raw.json
(direct A76_mu0 + B76_mu0, runs_A[0..1], runs_B[0..2];
best_A/best_B are duplicates, identified and not double-counted).
Per configuration: reproduce stored EoM max/median within 1e-6
first (machinery-failure clause), then the alignment set under
the primary thresholds plus the registered sensitivity grid.
float64; no optimisation."""
import sys, json
import numpy as np
sys.path.insert(0, '/home/hatch/workspace/warp-pilot/phase101/work')
sys.path.insert(0, '/home/hatch/workspace/warp-pilot/phase76')
sys.path.insert(0, '/home/hatch/workspace/warp-pilot/phase18')
sys.path.insert(0, '/home/hatch/workspace/warp-pilot/phase48')
import p1015_lib as H
import p761_lib as L

RAW = '/home/hatch/workspace/warp-pilot/phase101/results/p1015_partB_raw.json'
OUT = '/home/hatch/workspace/warp-pilot/phase108/results/p1083_results.json'
raw = json.load(open(RAW))
wall = L.Wall(1.1)
pts = wall.pts_sub
assert len(pts) == 56

# ---- corpus assembly with duplicate identification ----
corpus = [
    ('A76_mu0', 'direct/A76_mu0', raw['direct']['A76_mu0']),
    ('B76_mu0', 'direct/B76_mu0', raw['direct']['B76_mu0']),
    ('runs_A0', 'runs_A[0]', raw['runs_A'][0]),
    ('runs_A1', 'runs_A[1] (= best_A)', raw['runs_A'][1]),
    ('runs_B0', 'runs_B[0]', raw['runs_B'][0]),
    ('runs_B1', 'runs_B[1] (= best_B, hinge best)', raw['runs_B'][1]),
    ('runs_B2', 'runs_B[2]', raw['runs_B'][2]),
]
dup = dict(
    best_A_equals_runs_A1=bool(raw['best_A']['z'] == raw['runs_A'][1]['z']),
    best_B_equals_runs_B1=bool(raw['best_B']['z'] == raw['runs_B'][1]['z']),
    best_A_equals_runs_A0=bool(raw['best_A']['z'] == raw['runs_A'][0]['z']),
    best_B_equals_runs_B0=bool(raw['best_B']['z'] == raw['runs_B'][0]['z']),
    best_B_equals_runs_B2=bool(raw['best_B']['z'] == raw['runs_B'][2]['z']),
)
assert dup['best_A_equals_runs_A1'] and dup['best_B_equals_runs_B1']
zs = [tuple(c[2]['z']) for c in corpus]
assert len(set(zs)) == 7, 'corpus z vectors are not seven unique'

LIVE = 1e-6           # force-term live floor (fraction of max |term|)
SF_PRIMARY = 0.90
KIN_PRIMARY = 1e-6
SF_GRID = [0.80, 0.95]
KIN_GRID = [1e-8, 1e-4]


def alignment_members(T, D, sf_thr, kin_thr):
    """T: (n,4) terms [t_kin,t_pxx,t_FA,t_FB] at nondeg points.
    Returns boolean mask of alignment-set membership."""
    mx = np.max(np.abs(T), axis=1)
    tFA, tFB = T[:, 2], T[:, 3]
    live = (np.abs(tFA) >= LIVE * mx) & (np.abs(tFB) >= LIVE * mx)
    same = ((tFA > 0) & (tFB > 0)) | ((tFA < 0) & (tFB < 0))
    SF = (np.abs(tFA) + np.abs(tFB)) / D
    kinrel = np.abs(T[:, 0]) / D
    return live & same & (SF >= sf_thr) & (kinrel <= kin_thr), SF, kinrel


def analyse(label, source, rec):
    z = np.asarray(rec['z'], dtype=np.float64)
    ct = H.canonical_terms(wall, pts, z)
    T = np.column_stack([ct['t_kin'], ct['t_pxx'], ct['t_FA'], ct['t_FB']])
    D = np.sum(np.abs(T), axis=1)
    tot = np.sum(T, axis=1)
    rel = np.abs(tot) / (D + 1e-12)
    nd = D >= 1e-9
    idx_nd = np.where(nd)[0]
    Tn, Dn, reln = T[nd], D[nd], rel[nd]
    eom_max = float(reln.max()); eom_med = float(np.median(reln))
    err_max = abs(eom_max - float(rec['eom_rel_max_nondeg']))
    err_med = abs(eom_med - float(rec['eom_rel_med_nondeg']))
    repro_ok = bool(err_max <= 1e-6 and err_med <= 1e-6
                    and int(nd.sum()) == int(rec['n_nondeg']))
    mu = float(z[7])
    # H-force identically zero? F_A == 0 at every nondeg point
    FA_nd = ct['FA'][nd]
    hforce_ident_zero = bool(np.all(FA_nd == 0.0))
    both_live = bool(mu != 0.0 and not hforce_ident_zero)
    imax = int(np.argmax(reln))          # position within nondeg list
    max_idx = int(idx_nd[imax])          # subset index of max-residual pt

    def member_rows(mask):
        rows = []
        SF = (np.abs(Tn[:, 2]) + np.abs(Tn[:, 3])) / Dn
        for i in np.where(mask)[0]:
            rows.append(dict(
                idx=int(idx_nd[i]),
                t_kin=float(Tn[i, 0]), t_pxx=float(Tn[i, 1]),
                t_FA=float(Tn[i, 2]), t_FB=float(Tn[i, 3]),
                D_can=float(Dn[i]),
                S_F=float(SF[i]),
                kin_rel=float(abs(Tn[i, 0]) / Dn[i]),
                box_phi_abs=float(Tn[i, 0]),
                residual_rel=float(reln[i]),
                is_max_residual_point=bool(int(idx_nd[i]) == max_idx)))
        return rows

    mask_p, _, _ = alignment_members(Tn, Dn, SF_PRIMARY, KIN_PRIMARY)
    members = member_rows(mask_p)
    sens = {}
    for sf in SF_GRID:
        for kin in KIN_GRID:
            m, _, _ = alignment_members(Tn, Dn, sf, kin)
            sens[f'SF={sf}_kin={kin:g}'] = dict(
                size=int(m.sum()),
                members=[int(idx_nd[i]) for i in np.where(m)[0]],
                max_residual_in_set=bool(m[imax]))
    # also primary-threshold cross cells for completeness of the grid read
    for sf, kin, key in [(SF_PRIMARY, 1e-8, 'SF=0.9_kin=1e-08'),
                         (SF_PRIMARY, 1e-4, 'SF=0.9_kin=0.0001'),
                         (0.80, KIN_PRIMARY, 'SF=0.8_kin=1e-06'),
                         (0.95, KIN_PRIMARY, 'SF=0.95_kin=1e-06')]:
        m, _, _ = alignment_members(Tn, Dn, sf, kin)
        sens[key] = dict(size=int(m.sum()),
                         members=[int(idx_nd[i]) for i in np.where(m)[0]],
                         max_residual_in_set=bool(m[imax]))
    # sign-identity spot data: sign(tFA*tFB) vs sign(FA*FB) where PX!=0
    PX = ct['PX']
    prod_t = ct['t_FA'] * ct['t_FB']
    prod_F = ct['FA'] * ct['FB']
    ok = PX != 0
    sign_agree = bool(np.all(np.sign(prod_t[ok]) == np.sign(prod_F[ok])))
    return dict(
        label=label, source=source, z=[float(x) for x in z],
        mu=mu, pi0=float(z[3]), shape=float(z[4]),
        stored_eom_max=float(rec['eom_rel_max_nondeg']),
        stored_eom_med=float(rec['eom_rel_med_nondeg']),
        stored_n_nondeg=int(rec['n_nondeg']),
        eom_max_recomputed=eom_max, eom_med_recomputed=eom_med,
        eom_max_repro_err=err_max, eom_med_repro_err=err_med,
        n_nondeg=int(nd.sum()), n_deg=int((~nd).sum()),
        reproduction_ok=repro_ok,
        both_force_channels_live=both_live,
        H_force_identically_zero=hforce_ident_zero,
        PX_min_abs=float(np.min(np.abs(PX))),
        sign_identity_holds_all_points=sign_agree,
        max_residual_point=dict(
            idx=max_idx, residual_rel=float(reln[imax]),
            t_kin=float(Tn[imax, 0]), t_pxx=float(Tn[imax, 1]),
            t_FA=float(Tn[imax, 2]), t_FB=float(Tn[imax, 3]),
            D_can=float(Dn[imax]),
            S_F=float((abs(Tn[imax, 2]) + abs(Tn[imax, 3])) / Dn[imax]),
            kin_rel=float(abs(Tn[imax, 0]) / Dn[imax]),
            in_alignment_set_primary=bool(mask_p[imax])),
        alignment_primary=dict(size=int(mask_p.sum()), members=members),
        sensitivity=sens)


configs = [analyse(*c) for c in corpus]
machinery_failure = [c['label'] for c in configs if not c['reproduction_ok']]

live_configs = [c for c in configs if c['both_force_channels_live']]
hinge = next(c for c in configs if c['label'] == 'runs_B1')
if machinery_failure:
    verdict = 'MACHINERY FAILURE'
elif all(c['alignment_primary']['size'] > 0 for c in live_configs) and \
        all(c['max_residual_point']['in_alignment_set_primary']
            for c in live_configs):
    verdict = 'STRUCTURAL FEATURE'
elif all(c['alignment_primary']['size'] == 0 for c in configs
         if c['label'] != 'runs_B1') and hinge['alignment_primary']['size'] > 0:
    verdict = 'ISOLATED ACCIDENT'
elif all(c['alignment_primary']['size'] == 0 for c in configs):
    verdict = 'ISOLATED ACCIDENT'
else:
    verdict = 'MIXED / SET EXISTS BUT DOES NOT CARRY THE PIN'

out = dict(item='P108-3', beta=1.1, n_subset=56,
           duplicates_identified=dup,
           primary_thresholds=dict(live_floor=LIVE, S_F=SF_PRIMARY,
                                   kin_rel=KIN_PRIMARY, D_can_floor=1e-9),
           configs=configs,
           machinery_failure_configs=machinery_failure,
           verdict=verdict)
json.dump(out, open(OUT, 'w'), indent=1)
for c in configs:
    print(c['label'], 'mu=%.4g' % c['mu'], 'live', c['both_force_channels_live'],
          'repro_err', '%.3g/%.3g' % (c['eom_max_repro_err'], c['eom_med_repro_err']),
          'set', c['alignment_primary']['size'],
          [m['idx'] for m in c['alignment_primary']['members']],
          'maxpt', c['max_residual_point']['idx'],
          'in_set', c['max_residual_point']['in_alignment_set_primary'],
          'sens', {k: v['size'] for k, v in c['sensitivity'].items()})
print('VERDICT:', verdict)
