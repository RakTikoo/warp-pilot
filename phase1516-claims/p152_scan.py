#!/usr/bin/env python3
"""
p152_scan.py -- Phase 15 SA-2 wall-bed scan, beta in {0.1, 1.1,
1.5} DIRECT (registration: CHECKPOINT15.md SA-2 + C1-C7).

Per beta: unit-coupling basis tensors (tilted u, wwall) at the
binding set and the volume set; chi/S fields from p152_lib
(row-independent).  Per c0 row: Chat = sum_i S(x) c0_i B_i
(pointwise weights), T_req = T_GR + Chat/8pi.
  - coverage at binding points, ratio + ratio-free cross-checks
    asserted per row (bands all / outer r>=17 / inner r<17);
  - Hawking-Ellis margins of T_req at binding points;
  - local health (G-H): health_ae at c_i(x) = S(x) c0_i for
    every binding/volume point with S > 0.01;
  - full-volume NEC violation fraction (C7: margins with
    sampled fallback) + volume min margins, Type-I fraction.
Signal bar clauses (i)-(iv) evaluated here; clause (v) (chi
residual, C6) and the C5 completeness rule are finalised by
p152_verdict.py from p152_eom.json.

Basis tensors are cached to results/p152_bases_beta*.npz for
the EOM/conservation script.  float64.  System python3.
"""
import json
import sys
import time

import numpy as np

sys.path.insert(0, '/home/hatch/workspace/warp-pilot/phase15')
import p152_lib as L          # noqa: E402
import p61_scan as p61        # noqa: E402
import p93_tensor as tn       # noqa: E402
import verify_metric as vm    # noqa: E402
from p93_scan import health_ae  # noqa: E402

RES = '/home/hatch/workspace/warp-pilot/phase15/results'
BETAS = (0.1, 1.1, 1.5)


def bases_at(bd, pts, g_pts):
    basis = []
    for i in range(4):
        cs = tuple(1.0 if j == i else 0.0 for j in range(4))
        C = tn.C_aether(bd['gf'], pts, 0.3, L.U_TILT, cs,
                        lam_sign=-1.0, h_fd=0.15)
        basis.append(vm.eulerian_that(g_pts, C))
    return basis


def coverage(That_req, Chat, n_b, D, Gkk_raw, r_b):
    Ckk = p61.null_contract(Chat, n_b)
    ratio = (Ckk / L.EIGHT_PI) / D
    Tkk_req = p61.null_contract(That_req, n_b)
    out = {}
    for name, m in (('all', np.ones(len(r_b), bool)),
                    ('outer', r_b >= 17.0), ('inner', r_b < 17.0)):
        if m.sum() == 0:
            out[name] = None
            continue
        ff = float(np.mean(ratio[m] >= 1))
        fp = float(np.mean(ratio[m] >= 0.5))
        xf_f = float(np.mean(Tkk_req[m] >= 0))
        xf_p = float(np.mean(Ckk[m] >= 0.5 * (-Gkk_raw[m])))
        assert ff == xf_f, f'full xf mismatch {name}'
        assert fp == xf_p, f'partial xf mismatch {name}'
        out[name] = dict(
            n=int(m.sum()), frac_full=ff, frac_partial=fp,
            frac_sign=float(np.mean(ratio[m] > 0)),
            ratio_med=float(np.median(ratio[m])),
            ratio_min=float(np.min(ratio[m])),
            ratio_max=float(np.max(ratio[m])))
    return out


def local_health(S_b, S_v, c0):
    """G-H: health_ae at local couplings, all points S > 0.01."""
    cs0 = L.cs_of(*c0)
    worst = {}
    nfail = 0
    npts = 0
    for S in (S_b, S_v):
        for s in S[S > 0.01]:
            hp = health_ae(*(s * np.array(cs0)))
            npts += 1
            if not hp['health_pass']:
                nfail += 1
            for k in ('s1sq', 's0sq', 'e1', 'e0'):
                if k not in worst or hp[k] < worst[k]:
                    worst[k] = float(hp[k])
    return dict(n_points=int(npts), n_fail=int(nfail),
                pass_=bool(nfail == 0 and npts > 0), worst=worst)


def run_beta(beta, qc):
    t0 = time.time()
    bd = L.bed(beta)
    Qb, _, _ = L.Q_at(bd['gf'], bd['pts_b'])
    Qv, _, _ = L.Q_at(bd['gf'], bd['pts_v'])
    chib, Sb = L.chi_S(Qb, qc)
    chiv, Sv = L.chi_S(Qv, qc)
    print(f'beta={beta}: binding {bd["n_bind"]} vol {bd["n_vol"]}, '
          f'open frac binding {np.mean(Sb >= 0.5):.3f} '
          f'({time.time()-t0:.0f}s)', flush=True)
    basis_b = bases_at(bd, bd['pts_b'], bd['g_b'])
    print(f'  binding bases done ({time.time()-t0:.0f}s)',
          flush=True)
    basis_v = bases_at(bd, bd['pts_v'], bd['g_v'])
    print(f'  volume bases done ({time.time()-t0:.0f}s)', flush=True)
    np.savez(f'{RES}/p152_bases_beta{beta}.npz',
             basis_b=np.array(basis_b), basis_v=np.array(basis_v),
             S_b=Sb, S_v=Sv, Q_b=Qb, Q_v=Qv, chi_b=chib, chi_v=chiv)
    out = dict(beta=beta, n_binding=bd['n_bind'],
               n_volume=bd['n_vol'], maxdef=bd['maxdef'],
               open_frac_binding=float(np.mean(Sb >= 0.5)),
               open_frac_volume=float(np.mean(Sv >= 0.5)),
               rows=[], gr_control=None)
    for c0 in list(L.ROWS) + [(0.0, 0.0, 0.0)]:
        cs0 = np.array(L.cs_of(*c0))
        Chat_b = sum((Sb * cs0[i])[:, None, None] * basis_b[i]
                     for i in range(4))
        Chat_v = sum((Sv * cs0[i])[:, None, None] * basis_v[i]
                     for i in range(4))
        Treq_b = bd['That_GR_b'] + Chat_b / L.EIGHT_PI
        Treq_v = bd['That_GR_v'] + Chat_v / L.EIGHT_PI
        cov = coverage(Treq_b, Chat_b, bd['n_b'], bd['D_that'],
                       bd['Gkk_raw'], bd['r_b'])
        mb = vm.hawking_ellis_margins(Treq_b)
        mv = vm.hawking_ellis_margins(Treq_v)
        nec_v = mv['nec']
        lh = local_health(Sb, Sv, c0) if c0 != (0.0, 0.0, 0.0) \
            else dict(n_points=0, n_fail=0, pass_=True, worst={})
        row = dict(
            c0=list(c0), cs0=list(cs0), bands=cov,
            bind_margins=dict(
                nec_min=float(np.nanmin(mb['nec'])),
                wec_min=float(np.nanmin(mb['wec'])),
                sec_min=float(np.nanmin(mb['sec'])),
                dec_min=float(np.nanmin(mb['dec'])),
                typeI_frac=float(np.mean(mb['typeI']))),
            volume=dict(
                nec_viol_frac=float(np.mean(nec_v < 0)),
                nec_min=float(np.nanmin(nec_v)),
                wec_min=float(np.nanmin(mv['wec'])),
                sec_min=float(np.nanmin(mv['sec'])),
                dec_min=float(np.nanmin(mv['dec'])),
                typeI_frac=float(np.mean(mv['typeI']))),
            local_health=lh)
        # signal clauses (i)-(iv); (v) in p152_verdict.py
        if beta in (1.1, 1.5) and c0 != (0.0, 0.0, 0.0):
            row['signal_i_iv'] = bool(
                cov['all']['frac_full'] >= 0.90
                and cov['all']['frac_partial'] >= 0.90
                and lh['pass_']
                and row['volume']['nec_viol_frac'] == 0.0
                and row['bind_margins']['wec_min'] >= -1e-5
                and row['bind_margins']['dec_min'] >= -1e-5)
        if c0 == (0.0, 0.0, 0.0):
            out['gr_control'] = row
        else:
            out['rows'].append(row)
        print(f'  row {c0}: full {cov["all"]["frac_full"]:.3f} '
              f'partial {cov["all"]["frac_partial"]:.3f} '
              f'volNECviol {row["volume"]["nec_viol_frac"]:.4f} '
              f'health {lh["pass_"]} ({time.time()-t0:.0f}s)',
              flush=True)
    out['runtime_s'] = time.time() - t0
    return out


def main():
    qc, qc_info = L.q_crit()
    out = dict(item='P15 SA-2 wall-bed scan', Q_crit=qc,
               Q_crit_info=qc_info,
               units='ratio=(C_raw(k,k)/8pi)/D_That; ratio-free '
                     'cross-checks asserted per row per band',
               label='u-EOM residual open (all rows); chi solved '
                     'adiabatically, residual in p152_eom.json',
               betas=[])
    for beta in BETAS:
        out['betas'].append(run_beta(beta, qc))
    with open(f'{RES}/p152_scan.json', 'w') as fh:
        json.dump(out, fh, indent=1)
    print('WROTE results/p152_scan.json', flush=True)


if __name__ == '__main__':
    main()
