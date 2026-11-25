#!/usr/bin/env python3
"""
p1281_checker.py -- P128-1 independent checker.

Recomputes, from phase128/results/p1281_results.json and the
stored Phase-101 corpus:
 (1) the machinery gate (seven corpus configurations via
     p1015_lib.canonical_terms; hinge alignment set {44});
 (2) every run's, every seed's, and the family-A read's deciding
     numbers from their stored (z, A, lam, rho0), with canonical
     terms written HERE and legality via p761_lib margins with
     fast=False (full margins, p1015_checker.py pattern);
 (3) the constraint H_,phi(pi0) = 0, the guards, the Phase-118
     fence, the non-flatness majority, the trap gate, and the
     composition anatomy (t_kin vs t_FB sign at the max-residual
     point; t_FA at its posed zero) at the best candidate;
 (4) the verdict from the recomputed numbers.
Writes work/p1281_checker_output.json. float64. All-pass
required.
"""
import json
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


res = load('phase128/results/p1281_results.json')
wallP = L.Wall(1.1)
PTS = wallP.pts_sub
WB = P4.W_B
HINGE_LEGAL = 0.5892857142857143
HINGE_EMAX = 0.9999999999784565

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
    ct = H.canonical_terms(wallP, PTS, np.asarray(r['z_full'][:8]))
    tot = ct['t_kin'] + ct['t_pxx'] + ct['t_FA'] + ct['t_FB']
    D = sum(np.abs(ct[k]) for k in ('t_kin', 't_pxx', 't_FA', 't_FB'))
    rel = np.abs(tot) / (D + 1e-12)
    nd = D >= 1e-9
    worst = max(worst, abs(float(rel[nd].max()) - r['eom_rel_max_nondeg']),
                abs(float(np.median(rel[nd])) - r['eom_rel_med_nondeg']))
chk('gate_seven_configs', worst <= 1e-6, f'worst err {worst:.3e}')
ct = H.canonical_terms(wallP, PTS, np.asarray(raw['best_B']['z_full'][:8]))
idx, detail, rel, D = P4.alignment_set(ct)
chk('gate_hinge_alignment_44', idx == [44] and abs(detail[44]['S_F'] - 1.0) < 1e-12,
    f'set={idx}')
chk('gate_record_matches', res['gate']['pass_'] is True
    and abs(res['gate']['worst_err'] - worst) < 1e-15,
    f"stored worst {res['gate']['worst_err']:.3e}")


# ---------------- (2) independent read ----------------
def indep_read(wallx, z8, fluid):
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
                health_ok=health,
                frontier_A=float(lf) if (rel[nd].max() <= 0.02
                                         and health) else 0.0,
                Fsum_maxabs=float(np.max(np.abs(FA + FB))),
                trap_fires=bool(float(np.max(np.abs(FA + FB))) < 1e-9
                                or (abs(bc) < 1e-12
                                    and abs(2 * xi + b2) < 1e-12
                                    and abs(mu) < 1e-12)),
                alignment_set=aidx, max_resid_point=imax,
                max_resid_in_alignment=bool(imax in aidx),
                n_plateau_kin_live=int(sum(
                    1 for i in range(44)
                    if Dm[i] >= 1e-9 and abs(tk[i]) / Dm[i] > 1e-6)),
                dec=dict(t_kin=float(tk[imax]), t_pxx=float(tp[imax]),
                         t_FA=float(tA[imax]), t_FB=float(tB[imax]),
                         D_can=float(Dm[imax])),
                tFA_absmax_plateau=float(np.max(np.abs(tA[:44]))),
                rel=rel, Dm=Dm)


def cmp_read(tag, stored, ir):
    chk(f'{tag}_legal', abs(ir['subset_legal'] - stored['subset_legal']) < 1e-9,
        f"indep={ir['subset_legal']:.6f} stored={stored['subset_legal']:.6f}")
    chk(f'{tag}_emax', abs(ir['eom_rel_max_nondeg']
                           - stored['eom_rel_max_nondeg']) < 1e-6,
        f"indep={ir['eom_rel_max_nondeg']:.12f} "
        f"stored={stored['eom_rel_max_nondeg']:.12f}")
    chk(f'{tag}_emed', abs(ir['eom_rel_med_nondeg']
                           - stored['eom_rel_med_nondeg']) < 1e-6,
        f"indep={ir['eom_rel_med_nondeg']:.12f} "
        f"stored={stored['eom_rel_med_nondeg']:.12f}")
    chk(f'{tag}_counts', ir['n_nondeg'] == stored['n_nondeg']
        and ir['n_deg'] == stored['n_deg'],
        f"indep {ir['n_nondeg']}/{ir['n_deg']} stored "
        f"{stored['n_nondeg']}/{stored['n_deg']}")
    rel = ir['rel']
    pt_ok = (ir['max_resid_point'] == stored['max_resid_point']
             or float(rel[stored['max_resid_point']])
             >= ir['eom_rel_max_nondeg'] - 1e-9)
    chk(f'{tag}_align', ir['alignment_set'] == stored['alignment_set']
        and pt_ok
        and ir['max_resid_in_alignment'] == stored['max_resid_in_alignment'],
        f"indep set={ir['alignment_set']} pt={ir['max_resid_point']} "
        f"stored set={stored['alignment_set']} pt={stored['max_resid_point']}")
    chk(f'{tag}_health_frontier',
        ir['health_ok'] == stored['health_ok']
        and abs(ir['frontier_A'] - stored['frontier_A']) < 1e-12
        and ir['trap_fires'] == stored['trap_fires'],
        f"health {ir['health_ok']}/{stored['health_ok']} "
        f"frontier {ir['frontier_A']}/{stored['frontier_A']} "
        f"trap {ir['trap_fires']}/{stored['trap_fires']}")
    chk(f'{tag}_kinlive',
        ir['n_plateau_kin_live'] == stored['n_plateau_kin_live'],
        f"indep={ir['n_plateau_kin_live']} stored={stored['n_plateau_kin_live']}")


wallNF = P4.WallNF(1.1)
indep = {}
for r in res['runs']:
    wallNF.prof_A, wallNF.prof_lam = float(r['A']), float(r['lam'])
    ir = indep_read(wallNF, r['z'], (WB, float(r['rho0'])))
    indep[r['start']] = ir
    cmp_read(f"run{r['start']}", r, ir)
    xi, bc, b2, pi0 = r['z'][0], r['z'][1], r['z'][2], r['z'][3]
    pi0c = bc / (2.0 * (2.0 * xi + b2))
    chk(f"run{r['start']}_constraint",
        abs(pi0c - pi0) < 1e-9 and abs(-(2 * xi + b2) * pi0 + bc / 2) < 1e-9,
        f'pi0 err {abs(pi0c - pi0):.2e}')
    chk(f"run{r['start']}_guards_fence",
        r['guards_ok'] == bool(abs(2 * xi + b2) >= 0.2
                               and 0.02 <= pi0 <= 2.9 and abs(bc) >= 0.05)
        and abs(bc) >= 0.05,
        f"|2xi+b2|={abs(2 * xi + b2):.4f} pi0={pi0:.4f} |bc|={abs(bc):.4f} "
        f"guards_ok={r['guards_ok']}")
for s in res['seed_starts']:
    wallNF.prof_A, wallNF.prof_lam = float(s['A']), float(s['lam'])
    ir = indep_read(wallNF, s['z'], (WB, float(s['rho0'])))
    cmp_read(f"seed{s['start']}", s, ir)

famA = res['family_A_at_best']
wallNF.prof_A, wallNF.prof_lam = famA['profile_A'], famA['profile_lam']
cmp_read('familyA_at_best', famA, indep_read(wallNF, famA['z'], None))

# ---------------- (3)+(4) best anatomy + verdict ----------------
best = res['best']
bir = indep[best['start']]
dec = bir['dec']
chk('best_is_key_max',
    best['start'] == max(res['runs'], key=lambda r: (
        r['frontier_A'], r['subset_legal'], -r['eom_rel_max_nondeg'],
        -r['eom_rel_med_nondeg']))['start'],
    f"best start={best['start']}")
chk('best_decomp_matches_indep',
    all(abs(dec[k] - best['max_resid_decomp'][k]) < 1e-6
        for k in ('t_kin', 't_pxx', 't_FA', 't_FB', 'D_can')),
    f"indep dec={ {k: round(v, 6) for k, v in dec.items()} }")
chk('best_kin_opposition_flag',
    best['kin_opposes_FB_at_max'] == bool(dec['t_kin'] * dec['t_FB'] < 0),
    f"t_kin={dec['t_kin']:.6g} t_FB={dec['t_FB']:.6g} "
    f"opposes={best['kin_opposes_FB_at_max']}")
chk('best_tFA_posed_zero',
    abs(best['Hphi_at_pi0']) < 1e-9 and best['tFA_abs_at_pi0_exact_zero'],
    f"H_,phi(pi0)={best['Hphi_at_pi0']:.3e}, "
    f"max|t_FA| plateau (indep)={bir['tFA_absmax_plateau']:.3e}")
chk('nonflat_majority_at_best',
    res['nonflat_majority_at_best'] == (best['n_plateau_kin_live'] > 22),
    f"kin live {best['n_plateau_kin_live']}/44")


def pareto(r):
    return ((r['subset_legal'] >= HINGE_LEGAL
             and r['eom_rel_max_nondeg'] < HINGE_EMAX)
            or (r['subset_legal'] > HINGE_LEGAL
                and r['eom_rel_max_nondeg'] <= HINGE_EMAX))


def jpass(r):
    return (r['frontier_A'] > 0 and r['n_nondeg'] >= 28
            and not r['trap_fires'])


any_pass = any(jpass(r) for r in res['runs'])
any_par = any(pareto(r) for r in res['runs'])
chk('verdict_flags', res['any_joint_pass'] == any_pass
    and res['any_pareto'] == any_par,
    f'pass={any_pass} pareto={any_par}')
posed = best['n_plateau_kin_live'] > 22
carries = bool(best['alignment_set'] and best['max_resid_in_alignment'])
if any_pass:
    expect = 'JOINT PASS'
elif any_par:
    expect = 'JOINT (i)+(ii) IMPROVEMENT'
elif carries or not posed:
    expect = 'ESCAPE FAILS (composition form)'
else:
    expect = 'COMPOSITION WORKS MECHANICALLY, FRONT STANDS'
chk('verdict_form', res['verdict'] == expect,
    f"stored={res['verdict']} recomputed={expect}")
chk('boundary', res['boundary_pressed'] == bool(
    min(r['abs_bc'] for r in res['runs']) <= 0.05 + 1e-9)
    and min(r['abs_bc'] for r in res['runs']) >= 0.05,
    f"min |bc| = {min(r['abs_bc'] for r in res['runs']):.4f}")
chk('n_starts', res['n_starts'] >= 12, f"n={res['n_starts']}")

n_pass = sum(c['pass_'] for c in checks)
print(f'CHECKER {n_pass}/{len(checks)} PASS')
out = dict(n=len(checks), n_pass=n_pass, checks=checks)
with open(W + '/phase128/work/p1281_checker_output.json', 'w') as f:
    json.dump(out, f, indent=1)
sys.exit(0 if n_pass == len(checks) else 1)
