#!/usr/bin/env python
"""g59_b2.py -- Gate-59 B-2 persistence reads on Phase 431's
matings, with the gate's own implementation (g59_lib).

Arm A: registered-E grid [0, 2e5] x 2048 (pair form); window
spots {W/4, W/2, W} in the pair (Acoef) form AND in a factored
direct field form (gate's own); verbatim grid + spots; for
A_t2 the verbatim first crossing of the 1e-9 bar (scan +
bisection, pair form) and its seconds conversion.
Arm B: period grid [0, T_c] x 2048 (pair form, verbatim) --
worst instant; ladder returns n = 1..1024 (powers of 2) in
three forms (verbatim pair, registered pair, direct field);
cycles in window; per-cycle bar (1e-6) comparison.
Writes gate59/results/g59_b2.json.
"""
import json
import sys

import numpy as np

WP = '/home/hatch/workspace/warp-pilot'
sys.path.insert(0, f'{WP}/gate59/work')
import g59_lib as G  # noqa: E402

RES = f'{WP}/gate59/results'
BAR = 1e-9
W_UNITS = 3.6518e16
SEC_PER_UNIT = 1.218123e8 / W_UNITS   # 425 window: W = 3.860 yr


def avecs(rows):
    return np.array([[complex(*z) for z in row] for row in rows])


def load_targets(which):
    tg = json.load(open(
        f'{WP}/phase410/work/p410_targets.json' if which == 't1'
        else f'{WP}/phase420/work/p420_targets.json'))
    key = 'That' if which == 't1' else 'T_corr'
    return ([np.array(s['point']) for s in tg['sitesA']],
            [np.array(s[key]) for s in tg['sitesA']])


def load_best(tag):
    bj = json.load(open(f'{WP}/phase431/work/p431_best_{tag}.json'))
    return (np.array(bj['pvecs']), avecs(bj['avecs']),
            np.array(bj['masses']), float(bj['info_Ebase']))


out = {'gate': 59, 'W_units': W_UNITS,
       'sec_per_unit': SEC_PER_UNIT}

# ---------------- Arm A ----------------
for tag, tgt in (('A_t1_N12', 't1'), ('A_t2_6_6', 't2')):
    pv, av, mm, Ebase = load_best(tag)
    XS, TG = load_targets(tgt)
    S = G.pair_kernel(pv, av, mm)
    Ereg = np.full(len(pv), Ebase)
    R0 = float(G.RF_grid_pair(S, pv, XS, TG, np.array([0.0]), mm=mm)[0])
    rec = {'R_F_0_gate_pair': R0, 'E_registered': Ebase}
    ts = np.linspace(0.0, 2e5, 2048)
    RF_reg = G.RF_grid_pair(S, pv, XS, TG, ts, E=Ereg, mm=mm)
    rec['registered_grid_max_abs_dev'] = float(
        np.max(np.abs(RF_reg - R0)))
    spots = np.array([W_UNITS / 4, W_UNITS / 2, W_UNITS])
    RF_sp = G.RF_grid_pair(S, pv, XS, TG, spots, E=Ereg, mm=mm)
    rec['acoef_spots'] = {f'W_over_{d}': float(RF_sp[i])
                          for i, d in enumerate((4, 2, 1))}
    fd = {}
    for d in (4, 2, 1):
        t = W_UNITS / d
        fd[f'W_over_{d}'] = max(
            float(np.linalg.norm(
                G.T_field(pv, av, mm, XS[si], t=t,
                          factored_E=Ebase) - TG[si]))
            for si in range(len(XS)))
    rec['factored_direct_spots'] = fd
    rec['factored_direct_max_dev'] = float(
        max(abs(v - R0) for v in fd.values()))
    # verbatim
    RF_v = G.RF_grid_pair(S, pv, XS, TG, ts, mm=mm)
    rec['verbatim_grid_max_RF'] = float(RF_v.max())
    rec['verbatim_grid_RF_at_2e5'] = float(RF_v[-1])
    vspots = {}
    for t in (2e5, 2e6, 2e7, 2e8):
        vspots[f't={t:.0e}'] = float(
            G.RF_grid_pair(S, pv, XS, TG, np.array([t]), mm=mm)[0])
    rec['verbatim_spots'] = vspots
    rec['spectrum_scatter'] = float(
        G.energies(pv, mm).max() - G.energies(pv, mm).min())
    out[tag] = rec
    print(tag, 'R0 =', R0, ' reg grid dev =',
          rec['registered_grid_max_abs_dev'], ' verbatim max =',
          rec['verbatim_grid_max_RF'], flush=True)

# A_t2 verbatim first crossing of the bar (scan + bisection)
pv, av, mm, Ebase = load_best('A_t2_6_6')
XS, TG = load_targets('t2')
S = G.pair_kernel(pv, av, mm)


def RF1(t):
    return float(G.RF_grid_pair(S, pv, XS, TG, np.array([t]), mm=mm)[0])


scan = np.concatenate([[0.0], np.logspace(3, 8.3, 400)])
vals = np.array([RF1(t) for t in scan])
ix = int(np.argmax(vals > BAR))
lo, hi = scan[ix - 1], scan[ix]
for _ in range(200):
    mid = 0.5 * (lo + hi)
    if RF1(mid) > BAR:
        hi = mid
    else:
        lo = mid
    if hi - lo < 1e-3:
        break
tstar = 0.5 * (lo + hi)
out['A_t2_6_6']['verbatim_first_crossing_units'] = float(tstar)
out['A_t2_6_6']['verbatim_first_crossing_s'] = float(
    tstar * SEC_PER_UNIT)
out['A_t2_6_6']['stored_first_crossing_units'] = 35727055.84393014
out['A_t2_6_6']['crossing_rel_diff'] = float(
    abs(tstar - 35727055.84393014) / 35727055.84393014)
out['A_t2_6_6']['orders_vs_unconstrained'] = float(
    np.log10((tstar * SEC_PER_UNIT) / 2.422008204e-17))
print('A_t2 crossing:', tstar, 'units =',
      tstar * SEC_PER_UNIT, 's; orders vs unconstrained:',
      out['A_t2_6_6']['orders_vs_unconstrained'], flush=True)

# ---------------- Arm B ----------------
for tag, tgt, counts in (
        ('B_t1_N6_L3', 't1', [(2, 2, 2)]),
        ('B_t2_6_6_L3', 't2', [(2, 2, 2), (2, 2, 2)])):
    pv, av, mm, E0 = load_best(tag)
    XS, TG = load_targets(tgt)
    S = G.pair_kernel(pv, av, mm)
    Tc = 2 * np.pi / E0
    rungs = []
    for c in counts:
        rungs += [n + 1 for n, cc in enumerate(c) for _ in range(cc)]
    Ereg = np.array(rungs, dtype=float) * E0
    R0 = float(G.RF_grid_pair(S, pv, XS, TG, np.array([0.0]), mm=mm)[0])
    ts = np.linspace(0.0, Tc, 2048)
    RFg = G.RF_grid_pair(S, pv, XS, TG, ts, mm=mm)
    iw = int(np.argmax(RFg))
    rec = {'R_F_0_gate_pair': R0, 'E0': E0, 'T_c': float(Tc),
           'T_c_seconds': float(Tc * SEC_PER_UNIT),
           'cycles_in_window': float(W_UNITS / Tc),
           'worst_instant_RF': float(RFg.max()),
           'worst_instant_t': float(ts[iw])}
    # direct-field worst instant cross-check (coarse grid)
    RFd = []
    for t in np.linspace(0.0, Tc, 129):
        RFd.append(max(
            float(np.linalg.norm(
                G.T_field(pv, av, mm, XS[si], t=float(t)) - TG[si]))
            for si in range(len(XS))))
    rec['worst_instant_RF_direct_coarse'] = float(np.max(RFd))
    lad_v, lad_r, lad_d = {}, {}, {}
    for k in range(11):
        n = 2 ** k
        lad_v[str(n)] = float(G.RF_grid_pair(
            S, pv, XS, TG, np.array([n * Tc]), mm=mm)[0]) - R0
        lad_r[str(n)] = float(G.RF_grid_pair(
            S, pv, XS, TG, np.array([n * Tc]), E=Ereg, mm=mm)[0]) - R0
        lad_d[str(n)] = max(
            float(np.linalg.norm(
                G.T_field(pv, av, mm, XS[si], t=n * Tc) - TG[si]))
            for si in range(len(XS))) - R0
    rec['ladder_returns_verbatim_pair'] = lad_v
    rec['ladder_returns_registered_pair'] = lad_r
    rec['ladder_returns_direct_field'] = lad_d
    rec['ladder_max_abs_verbatim'] = float(
        max(abs(v) for v in lad_v.values()))
    rec['per_cycle_bar'] = 1e-6
    out[tag] = rec
    print(tag, 'Tc =', Tc, ' worst =', rec['worst_instant_RF'],
          ' ladder max verbatim =', rec['ladder_max_abs_verbatim'],
          flush=True)

json.dump(out, open(f'{RES}/g59_b2.json', 'w'), indent=1,
          default=str)
print('written g59_b2.json')
