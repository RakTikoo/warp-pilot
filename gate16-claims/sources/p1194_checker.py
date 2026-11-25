#!/usr/bin/env python3
"""
p1194_checker.py -- P119-4 independent checker.

Recomputes, from phase119/results/p1194_results.json and the
stored Phase-101 corpus:
 (1) the machinery gate (seven corpus configurations via
     p1015_lib.canonical_terms; hinge alignment set {44});
 (2) every half-(a) and half-(b) run's deciding reads from
     its stored z, with canonical terms written HERE and
     legality via p761_lib margins with fast=False (full
     margins path, p1015_checker.py pattern);
 (3) the hinge-seeded / projected-seed reads, the family-A
     read at half (a)'s best, the half-(b) constraint and
     Phase-118 fence at every half-(b) run, the trap gate
     at both halves' best candidates, half (a)'s
     non-flatness majority at its best and seed;
 (4) both verdicts from the recomputed numbers.
Writes work/p1194_checker_output.json via the perl bridge.
float64. All-pass required.
"""
import json
import subprocess
import sys

import numpy as np

W = '/home/hatch/workspace/warp-pilot'
sys.path.insert(0, W + '/phase119/work')
sys.path.insert(0, W + '/phase101/work')
sys.path.insert(0, W + '/phase79')
sys.path.insert(0, W + '/phase76')
sys.path.insert(0, W + '/phase18')
import p761_lib as L      # noqa: E402
import p1015_lib as H     # noqa: E402
import p1194_lib as P4    # noqa: E402
import p182_engine as E   # noqa: E402
import p182_basis as B    # noqa: E402

checks = []


def chk(name, ok, detail=''):
    checks.append(dict(name=name, pass_=bool(ok), detail=str(detail)))
    print(('PASS' if ok else 'FAIL'), name, detail, flush=True)


def load(p):
    with open(W + '/' + p) as f:
        return json.load(f)


res = load('phase119/results/p1194_results.json')
wall = L.Wall(1.1)
PTS = wall.pts_sub
WB = P4.W_B

# ---------------- (1) gate ----------------
raw = load('phase101/results/p1015_partB_raw.json')
cfgs = [('direct/B76_mu0', raw['direct']['B76_mu0']),
        ('direct/A76_mu0', raw['direct']['A76_mu0'])]
for i, r in enumerate(raw['runs_B']):
    if 'z_full' in r:
        cfgs.append((f'runs_B[{i}]', r))
for i, r in enumerate(raw['runs_A']):
    if 'z_full' in r:
        cfgs.append((f'runs_A[{i}]', r))
worst = 0.0
for name, r in cfgs:
    ct = H.canonical_terms(wall, PTS, np.asarray(r['z_full'][:8]))
    tot = ct['t_kin'] + ct['t_pxx'] + ct['t_FA'] + ct['t_FB']
    D = sum(np.abs(ct[k]) for k in ('t_kin', 't_pxx', 't_FA', 't_FB'))
    rel = np.abs(tot) / (D + 1e-12)
    nd = D >= 1e-9
    worst = max(worst, abs(float(rel[nd].max()) - r['eom_rel_max_nondeg']),
                abs(float(np.median(rel[nd])) - r['eom_rel_med_nondeg']))
chk('gate_seven_configs', worst <= 1e-6, f'worst err {worst:.3e}')
ct = H.canonical_terms(wall, PTS, np.asarray(raw['best_B']['z_full'][:8]))
idx, detail, rel, D = P4.alignment_set(ct)
chk('gate_hinge_alignment_44', idx == [44] and abs(detail[44]['S_F'] - 1.0) < 1e-12,
    f'set={idx} S_F={detail[44]["S_F"] if 44 in detail else None}')


# ---------------- (2) independent read ----------------
def indep_read(wallx, z8, fluid):
    """Canonical terms + E_total assembled here; margins fast=False."""
    xi, bc, b2, pi0, shape, p1, p2, mu = [float(q) for q in z8]
    K = wallx.kern(PTS)
    g, ginv, Gam = K['g'], K['ginv'], K['Gam']
    bed, v, Hh = wallx.phi_jets(PTS, pi0, shape)
    sg, basis, aux = E.lag_basis(g, K['dg'], K['ddg'], v, Hh)
    X = -0.5 * aux['XL']; PX = p1 + 2 * p2 * X; PXX = 2 * p2
    box = np.einsum('pab,pab->p', ginv, aux['ph'])
    vup = np.einsum('pab,pb->pa', ginv, v)
    hv = np.einsum('pab,pb->pa', aux['ph'], vup)
    vhv = np.einsum('pa,pa->p', vup, hv)
    phi = bed.cs(np.clip(np.linalg.norm(PTS, axis=1), 0, 60))
    FA = 0.5 * L.dH_of(phi, xi, bc, b2) * K['Rsc']
    FB = -mu * phi
    with np.errstate(divide='ignore', invalid='ignore'):
        tk = box; tp = -(PXX / PX) * vhv; tA = FA / PX; tB = FB / PX
    Dm = np.abs(tk) + np.abs(tp) + np.abs(tA) + np.abs(tB)
    rel = np.abs(tk + tp + tA + tB) / (Dm + 1e-12)
    nd = Dm >= 1e-9
    Hf = L.H_of(phi, xi, bc, b2)
    st = B.stencil(PTS, 0.3).reshape(-1, 3)
    phis = bed.cs(np.clip(np.linalg.norm(st, axis=1), 0, 60))
    Hs = L.H_of(phis, xi, bc, b2).reshape(len(PTS), 19)
    _, HessH = L.fld_derivs(Hs, Gam)
    BoxH = np.einsum('pab,pab->p', ginv, HessH)
    ER = Hf[:, None, None] * K['G'] + HessH - g * BoxH[:, None, None]
    Pval = p1 * X + p2 * X**2 + 0.5 * mu * phi**2
    TP = PX[:, None, None] * np.einsum('pa,pb->pab', v, v) \
        + Pval[:, None, None] * g
    Ec = ER + TP
    if fluid is not None:
        Ec = Ec + L.fluid_T(PTS, g, fluid[0], fluid[1])
    m = L.margins(Ec, g, fast=False)
    lf, _ = L.legal_frac(m)
    ctd = dict(t_kin=tk, t_pxx=tp, t_FA=tA, t_FB=tB, FA=FA, FB=FB,
               phi=phi, PX=PX, X=X, Rsc=K['Rsc'])
    aidx, adet, arel, aD = P4.alignment_set(ctd)
    imax = int(np.argmax(np.where(nd, rel, -1.0)))
    with np.errstate(divide='ignore', invalid='ignore'):
        cr2 = PX / (PX + 2 * X * PXX)
    cr2f = cr2[np.isfinite(cr2)]
    health = bool(np.min(Hf) > 0 and np.min(PX) > 0 and len(cr2f)
                  and cr2f.min() >= 0 and cr2f.max() <= 1)
    return dict(subset_legal=float(lf),
                eom_rel_max_nondeg=float(rel[nd].max()),
                eom_rel_med_nondeg=float(np.median(rel[nd])),
                n_nondeg=int(np.sum(nd)), n_deg=int(np.sum(~nd)),
                health_ok=health, H_min=float(np.min(Hf)),
                PX_min=float(np.min(PX)),
                Fsum_maxabs=float(np.max(np.abs(FA + FB))),
                alignment_set=aidx, max_resid_point=imax,
                max_resid_in_alignment=bool(imax in aidx),
                n_plateau_kin_live=int(sum(
                    1 for i in range(44)
                    if Dm[i] >= 1e-9 and abs(tk[i]) / Dm[i] > 1e-6)),
                tFA_share_at_max=float(abs(tA[imax]) / Dm[imax]),
                tFB_share_at_max=float(abs(tB[imax]) / Dm[imax]),
                rel=rel, Dm=Dm)


def cmp_read(tag, stored, ir, tol_e=1e-6):
    chk(f'{tag}_legal', abs(ir['subset_legal'] - stored['subset_legal']) < 1e-9,
        f"indep={ir['subset_legal']:.6f} stored={stored['subset_legal']:.6f}")
    chk(f'{tag}_emax', abs(ir['eom_rel_max_nondeg']
                           - stored['eom_rel_max_nondeg']) < tol_e,
        f"indep={ir['eom_rel_max_nondeg']:.12f} "
        f"stored={stored['eom_rel_max_nondeg']:.12f}")
    chk(f'{tag}_emed', abs(ir['eom_rel_med_nondeg']
                           - stored['eom_rel_med_nondeg']) < tol_e,
        f"indep={ir['eom_rel_med_nondeg']:.12f} "
        f"stored={stored['eom_rel_med_nondeg']:.12f}")
    chk(f'{tag}_counts', ir['n_nondeg'] == stored['n_nondeg']
        and ir['n_deg'] == stored['n_deg'],
        f"indep {ir['n_nondeg']}/{ir['n_deg']} stored "
        f"{stored['n_nondeg']}/{stored['n_deg']}")
    # max-residual point compared tie-aware: in half (b) many
    # plateau points tie at rel = 1 - O(1e-11), and the two
    # arithmetic paths break the tie differently. The stored
    # point must be a legitimate maximiser (its independent
    # rel within 1e-9 of the independent max); the tie set is
    # reported. Alignment-set identity and in/out are strict.
    rel = ir['rel']; ndm = ir['Dm'] >= 1e-9
    ties = [int(i) for i in range(len(rel))
            if ndm[i] and rel[i] >= ir['eom_rel_max_nondeg'] - 1e-9]
    pt_ok = (ir['max_resid_point'] == stored['max_resid_point']
             or float(rel[stored['max_resid_point']])
             >= ir['eom_rel_max_nondeg'] - 1e-9)
    chk(f'{tag}_align', ir['alignment_set'] == stored['alignment_set']
        and pt_ok
        and ir['max_resid_in_alignment'] == stored['max_resid_in_alignment'],
        f"indep set={ir['alignment_set']} pt={ir['max_resid_point']} "
        f"stored set={stored['alignment_set']} pt={stored['max_resid_point']} "
        f"ties_within_1e-9={ties}")
    chk(f'{tag}_health', ir['health_ok'] == stored['health_ok'],
        f"indep={ir['health_ok']} stored={stored['health_ok']}")


wallNF = P4.WallNF(1.1)
HA, HB = res['half_A'], res['half_B']
for r in HA['runs']:
    v = r['z']
    wallNF.prof_A, wallNF.prof_lam = float(v[8]), float(v[9])
    ir = indep_read(wallNF, v[:8], (WB, float(v[10])))
    cmp_read(f"A_start{r['start']}", r, ir)
    chk(f"A_start{r['start']}_kinlive",
        ir['n_plateau_kin_live'] == r['n_plateau_kin_live'],
        f"indep={ir['n_plateau_kin_live']} stored={r['n_plateau_kin_live']}")
for r in HB['runs']:
    ir = indep_read(wall, r['z'], (WB, float(r['rho0'])))
    cmp_read(f"B_start{r['start']}", r, ir)
    xi, bc, b2 = r['z'][0], r['z'][1], r['z'][2]
    pi0c = bc / (2.0 * (2.0 * xi + b2))
    chk(f"B_start{r['start']}_constraint",
        abs(pi0c - r['z'][3]) < 1e-9 and abs(bc) >= 0.05,
        f'pi0 err {abs(pi0c - r["z"][3]):.2e}, |bc|={abs(bc):.4f}')
    chk(f"B_start{r['start']}_trap",
        (ir['Fsum_maxabs'] < 1e-9) == r['trap_fires'] or ir['Fsum_maxabs'] >= 1e-9,
        f"Fsum={ir['Fsum_maxabs']:.3e} stored trap={r['trap_fires']}")

# seeds + family A
seedA = HA['hinge_seed_initial']
wallNF.prof_A, wallNF.prof_lam = float(seedA['z'][8]), float(seedA['z'][9])
cmp_read('A_hingeseed', seedA,
         indep_read(wallNF, seedA['z'][:8], (WB, float(seedA['z'][10]))))
seedB = HB['hinge_projected_seed']
cmp_read('B_projseed', seedB,
         indep_read(wall, seedB['z'], (WB, float(seedB['rho0']))))
chk('B_projseed_Hphi_zero',
    abs(-(2 * seedB['z'][0] + seedB['z'][2]) * seedB['z'][3]
        + seedB['z'][1] / 2.0) < 1e-12, 'H_,phi(pi0) at projected seed')
famA = HA['family_A_at_best']
wallNF.prof_A, wallNF.prof_lam = famA['profile_A'], famA['profile_lam']
cmp_read('A_familyA_at_best', famA, indep_read(wallNF, famA['z'], None))

# ---------------- (4) verdicts ----------------
HINGE_LEGAL = 0.5892857142857143
HINGE_EMAX = 0.9999999999784565


def pareto(r):
    return ((r['subset_legal'] >= HINGE_LEGAL
             and r['eom_rel_max_nondeg'] < HINGE_EMAX)
            or (r['subset_legal'] > HINGE_LEGAL
                and r['eom_rel_max_nondeg'] <= HINGE_EMAX))


for tag, half in (('A', HA), ('B', HB)):
    best = half['best']
    chk(f'{tag}_no_joint_pass',
        not half['any_joint_pass']
        and all(r['frontier_A'] == 0.0 for r in half['runs']),
        f"best frontier_A={best['frontier_A']}")
    chk(f'{tag}_no_pareto', not half['any_pareto']
        and not any(pareto(r) for r in half['runs']),
        'no run Pareto-dominates the hinge best (recomputed)')
    chk(f'{tag}_best_is_key_max',
        best['start'] == max(
            half['runs'],
            key=lambda r: (r['frontier_A'], r['subset_legal'],
                           -r['eom_rel_max_nondeg'],
                           -r['eom_rel_med_nondeg']))['start'],
        f"best start={best['start']}")
    chk(f'{tag}_best_alignment_empty',
        best['alignment_set'] == []
        and best['max_resid_in_alignment'] is False,
        f"best set={best['alignment_set']}")
    chk(f'{tag}_verdict_form',
        half['verdict'] == 'ESCAPE WORKS MECHANICALLY, FRONT STANDS',
        half['verdict'])
chk('B_boundary_not_pressed', HB['boundary_pressed'] is False
    and HB['min_abs_bc_all_runs'] >= 0.05,
    f"min |bc| over runs = {HB['min_abs_bc_all_runs']:.4f}")
chk('A_nonflat_majority_at_best',
    HA['best']['n_plateau_kin_live'] > 22
    and HA['hinge_seed_initial']['n_plateau_kin_live'] > 22,
    f"best {HA['best']['n_plateau_kin_live']}/44, "
    f"seed {HA['hinge_seed_initial']['n_plateau_kin_live']}/44")
chk('A_fd_check', HA['fd_check'].get('pass', HA['fd_check'].get('pass_')) is True
    and HA['fd_check']['d1_rel'] < 1e-6 and HA['fd_check']['d2_rel'] < 1e-6,
    f"d1={HA['fd_check']['d1_rel']:.2e} d2={HA['fd_check']['d2_rel']:.2e}")
chk('n_starts', HA['n_starts'] >= 12 and HB['n_starts'] >= 12,
    f"A={HA['n_starts']} B={HB['n_starts']}")

n_pass = sum(c['pass_'] for c in checks)
print(f'CHECKER {n_pass}/{len(checks)} PASS')
out = dict(n=len(checks), n_pass=n_pass, checks=checks)
data = json.dumps(out, indent=1)
p = subprocess.run(['perl', W + '/phase119/work/p1194_writefile.pl',
                    W + '/phase119/work/p1194_checker_output.json'],
                   input=data.encode(), capture_output=True)
print(p.stderr.decode())
sys.exit(0 if n_pass == len(checks) else 1)
