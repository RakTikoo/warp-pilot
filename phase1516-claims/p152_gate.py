#!/usr/bin/env python3
"""
p152_gate.py -- Phase 15 SA-2 gates (CHECKPOINT15.md SA-2 block +
continuation C1-C7):
  G-T  pointwise-weighted tensor vs direct evaluation, frozen-chi
       control row (SA-2 code path), binding + volume subsets.
  Q    sanity: Q >= 0 (FD tol), Q = 0 on Minkowski.
  G-W  Q_crit from the beta=1.1 exterior (C3 union); screen
       closed outside at every beta (S_ext = 0 <= 1e-4), open
       fraction at binding points per beta (bar 0.90).
  G-H  chi = 0 is the exact GR limit (couplings vanish).

float64.  System python3.
"""
import json
import sys
import time

import numpy as np

sys.path.insert(0, '/home/hatch/workspace/warp-pilot/phase15')
import p152_lib as L   # noqa: E402
import p93_tensor as tn  # noqa: E402
import verify_metric as vm  # noqa: E402

RES = '/home/hatch/workspace/warp-pilot/phase15/results'


def main():
    t0 = time.time()
    out = dict(item='P15 SA-2 gates', gates={})

    # ---------- Q_crit (C3) ----------
    qc, qc_info = L.q_crit()
    out['Q_crit_info'] = qc_info
    print(f"Q_crit = {qc:.6e} (p151 set max "
          f"{qc_info['max_Q_p151_set']:.3e}, fib set max "
          f"{qc_info['max_Q_fib_set']:.3e})", flush=True)

    # ---------- Q sanity: Minkowski ----------
    rng = np.random.default_rng(152)
    dirs = rng.normal(size=(40, 3))
    dirs /= np.linalg.norm(dirs, axis=1)[:, None]
    pts_m = dirs * rng.uniform(9.0, 21.0, 40)[:, None]
    Qm, Q1m, Q2m = L.Q_at(L.mink_gf, pts_m)
    out['Q_minkowski'] = dict(Q_absmax=float(np.max(np.abs(Qm))),
                              Q1_absmax=float(np.max(np.abs(Q1m))),
                              Q2_absmax=float(np.max(np.abs(Q2m))))
    print(f"Q Minkowski absmax {np.max(np.abs(Qm)):.3e}", flush=True)

    # ---------- beds, Q/S fields, G-W ----------
    beds = {}
    open_frac = {}
    for beta in (0.1, 1.1, 1.5):
        bd = L.bed(beta)
        beds[beta] = bd
        Qb, Q1b, Q2b = L.Q_at(bd['gf'], bd['pts_b'])
        Qv, _, _ = L.Q_at(bd['gf'], bd['pts_v'])
        chib, Sb = L.chi_S(Qb, qc)
        chiv, Sv = L.chi_S(Qv, qc)
        bd.update(Q_b=Qb, Q1_b=Q1b, Q2_b=Q2b, chi_b=chib, S_b=Sb,
                  Q_v=Qv, chi_v=chiv, S_v=Sv)
        open_frac[beta] = dict(
            binding_S_ge_0p5=float(np.mean(Sb >= 0.5)),
            binding_S_pos=float(np.mean(Sb > 0)),
            volume_S_ge_0p5=float(np.mean(Sv >= 0.5)),
            Q_b_min=float(np.min(Qb)), Q_b_med=float(np.median(Qb)),
            Q_b_max=float(np.max(Qb)),
            Q_min_overall=float(min(np.min(Qb), np.min(Qv))),
            S_b_max=float(np.max(Sb)))
        print(f'beta={beta}: binding {bd["n_bind"]}, open frac '
              f'{open_frac[beta]["binding_S_ge_0p5"]:.3f}, Q_b med '
              f'{open_frac[beta]["Q_b_med"]:.3e} max '
              f'{open_frac[beta]["Q_b_max"]:.3e} '
              f'({time.time()-t0:.0f}s)', flush=True)
    out['open_fraction'] = {str(k): v for k, v in open_frac.items()}

    # exterior closed at every beta (same exterior point sets)
    pa, pb = L.exterior_points()
    ext = {}
    for beta in (0.1, 1.1, 1.5):
        gf = L.bed_gf(beta)
        Qa, _, _ = L.Q_at(gf, pa)
        Qb2, _, _ = L.Q_at(gf, pb)
        _, Sa = L.chi_S(Qa, qc)
        _, Sb2 = L.chi_S(Qb2, qc)
        ext[str(beta)] = dict(
            Q_ext_max=float(max(np.max(Qa), np.max(Qb2))),
            ratio_to_Qcrit=float(max(np.max(Qa), np.max(Qb2)) / qc),
            S_ext_max=float(max(np.max(Sa), np.max(Sb2))))
        print(f'beta={beta}: exterior Q max '
              f'{ext[str(beta)]["Q_ext_max"]:.3e} '
              f'(Qcrit ratio {ext[str(beta)]["ratio_to_Qcrit"]:.3f}), '
              f'S_ext max {ext[str(beta)]["S_ext_max"]:.1e}',
              flush=True)
    out['exterior'] = ext
    out['G-W'] = dict(
        S_ext_max_all_beta=max(v['S_ext_max'] for v in ext.values()),
        bar_S_ext=1e-4,
        closed_outside=bool(max(v['S_ext_max']
                                for v in ext.values()) <= 1e-4),
        open_bar=0.90,
        open_superluminal=bool(
            open_frac[1.1]['binding_S_ge_0p5'] >= 0.90
            or open_frac[1.5]['binding_S_ge_0p5'] >= 0.90),
        note='chi=0 outside => c_i^eff = 0 => alpha1 = alpha2 = 0, '
             'c_T^2 = 1/(1-c13^eff) = 1 exactly on the exterior / '
             'GW path (weak-field window).')

    # ---------- G-T: frozen-chi control via the SA-2 path ------
    bd = beds[1.1]
    sub = bd['pts_b'][::37]
    gsub = bd['gf'](sub)
    row = (0.2, 1.0, 1.0)
    s0 = 0.7
    cs_dir = tuple(s0 * c for c in L.cs_of(*row))
    C_direct = tn.C_aether(bd['gf'], sub, 0.3, L.U_TILT, cs_dir,
                           lam_sign=-1.0, h_fd=0.15)
    C_combo = np.zeros_like(C_direct)
    for i in range(4):
        csi = tuple(1.0 if j == i else 0.0 for j in range(4))
        Bi = tn.C_aether(bd['gf'], sub, 0.3, L.U_TILT, csi,
                         lam_sign=-1.0, h_fd=0.15)
        C_combo += (s0 * L.cs_of(*row)[i]) * Bi
    rel = float(np.max(np.abs(C_direct - C_combo))
                / max(np.max(np.abs(C_direct)), 1e-300))
    out['gates']['G-T'] = dict(max_rel_diff=rel,
                               pass_=bool(rel <= 1e-6), s0=s0,
                               row=row)
    print(f'G-T frozen-chi: max rel diff {rel:.3e}', flush=True)

    # basis linearity spot check on volume points (subset)
    subv = bd['pts_v'][::211]
    C_direct_v = tn.C_aether(bd['gf'], subv, 0.3, L.U_TILT, cs_dir,
                             lam_sign=-1.0, h_fd=0.15)
    C_combo_v = np.zeros_like(C_direct_v)
    for i in range(4):
        csi = tuple(1.0 if j == i else 0.0 for j in range(4))
        Bi = tn.C_aether(bd['gf'], subv, 0.3, L.U_TILT, csi,
                         lam_sign=-1.0, h_fd=0.15)
        C_combo_v += (s0 * L.cs_of(*row)[i]) * Bi
    rel_v = float(np.max(np.abs(C_direct_v - C_combo_v))
                  / max(np.max(np.abs(C_direct_v)), 1e-300))
    out['gates']['G-T_volume_spot'] = dict(max_rel_diff=rel_v,
                                           pass_=bool(rel_v <= 1e-6))
    print(f'G-T volume spot: max rel diff {rel_v:.3e}', flush=True)

    out['gates']['G-H_chi0'] = ('exact GR limit: S(0)=0 => all '
                                'c_i(0)=0; health_ae at zero '
                                'couplings is GR')
    out['gates']['Q_nonneg'] = bool(
        out['Q_minkowski']['Q_absmax'] <= 1e-12
        and all(open_frac[b]['Q_min_overall'] >= -1e-12
                for b in open_frac))
    out['verdict'] = dict(
        G_T=bool(rel <= 1e-6 and rel_v <= 1e-6),
        G_W_closed=out['G-W']['closed_outside'],
        G_W_open_superluminal=out['G-W']['open_superluminal'],
        gate_pass=bool(rel <= 1e-6 and rel_v <= 1e-6
                       and out['G-W']['closed_outside']
                       and out['G-W']['open_superluminal']))
    out['runtime_s'] = time.time() - t0
    with open(f'{RES}/p152_gate.json', 'w') as fh:
        json.dump(out, fh, indent=1)
    print(f"WROTE results/p152_gate.json verdict={out['verdict']}",
          flush=True)


if __name__ == '__main__':
    main()
