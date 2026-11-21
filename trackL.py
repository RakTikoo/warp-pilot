"""
trackL.py — Track L: mass-velocity frontier of the positive-energy shell
family. For a given beta rung, search (geometry x density profile x shift
profile) designs and M values with the established point auditor
(whole volume, Type I + eigenvalue margins, significance relative to
rho_peak). Winners get h/2 confirmation + dense audit.

Usage: python3 trackL.py 0.05   ->  results/trackL_b0.05.json (incremental)
"""
import json, sys, time
import numpy as np
import verify_metric as vm
import shell as sh

G_C2 = 7.426e-28           # m per kg
KG_PER_M = 1.0 / G_C2
MJUP_KG = 1.898e27


def sample_points(R1, R2, ndir=14, dense=True):
    rng = np.random.default_rng(42)
    i = np.arange(ndir)
    phi = np.arccos(1 - 2 * (i + 0.5) / ndir)
    th = np.pi * (1 + 5 ** 0.5) * i
    dirs = np.stack([np.cos(th) * np.sin(phi), np.sin(th) * np.sin(phi),
                     np.cos(phi)], axis=1)
    W = R2 - R1
    rad = list(np.linspace(0.3 * R1, 1.3 * R2, 26))
    if dense:
        rad += [R1 - 0.1 * W, R1 + 0.05 * W, R1 + 0.1 * W, R1 + 0.25 * W,
                R2 - 0.25 * W, R2 - 0.1 * W, R2 + 0.1 * W]
    rad = sorted(set(round(float(r), 6) for r in rad if r > 0.5))
    return np.concatenate([dirs * r for r in rad]), dirs


def eval_shell(R1, R2, M, kind, params, sr, sp, beta, shift_kind='cos',
               ws=None, h=None, pts=None):
    if pts is None:
        pts, _ = sample_points(R1, R2)
    if h is None:
        h = 0.03 * R1
    try:
        prof = sh.build_shell(R1, R2, M, kind=kind, params=params,
                              s_rho=sr, s_P=sp, Nr=3001)
    except Exception:
        prof = None
    if prof is None or not (np.all(np.isfinite(prof['a']))
                            and np.all(np.isfinite(prof['b']))):
        return {'R1': R1, 'R2': R2, 'M_geom': M, 'M_kg': M * KG_PER_M,
                'M_Mjup': M * KG_PER_M / MJUP_KG, 'kind': kind,
                'params': params, 's_rho': sr, 's_P': sp, 'beta': beta,
                'shift_kind': shift_kind, 'ws': ws, 'h': h, 'worst': -1e30,
                'worst_kind': 'build_fail_nonfinite', 'worst_radius': -1.0,
                'nec': -1e30, 'wec': -1e30, 'sec': -1e30, 'dec': -1e30,
                'typeI_frac_sig': 0.0, 'n_sig': 0, 'rho_peak': 0.0}
    gfunc = sh.shell_point_factory(prof, beta, shift_kind, 1.0, ws)
    G, That, m = vm.einstein_at_points(gfunc, pts, h=h)
    scale = np.max(np.abs(That), axis=(1, 2))
    rho_peak = float(np.max(That[:, 0, 0]))
    thr = max(1e-9 * (10.0 / R1) ** 2, 1e-3 * abs(rho_peak))
    sig = scale > thr
    worst = {k: float(np.min(m[k][sig])) for k in ('nec', 'wec', 'sec', 'dec')}
    w = min(worst.values()); wk = min(worst, key=worst.get)
    wi = int(np.where(sig)[0][int(np.argmin(m[wk][sig]))])
    return {'R1': R1, 'R2': R2, 'M_geom': M, 'M_kg': M * KG_PER_M,
            'M_Mjup': M * KG_PER_M / MJUP_KG, 'kind': kind, 'params': params,
            's_rho': sr, 's_P': sp, 'beta': beta, 'shift_kind': shift_kind,
            'ws': ws, 'h': h, 'worst': w, 'worst_kind': wk,
            'worst_radius': float(np.linalg.norm(pts[wi])), **worst,
            'typeI_frac_sig': float(np.mean(m['typeI'][sig])),
            'n_sig': int(np.sum(sig)), 'rho_peak': rho_peak}


def designs(R1, R2):
    W = R2 - R1
    profs = [
        ('edgepeaked', {'wd': 0.30 * W, 'floor': 0.20}),
        ('edgepeaked', {'wd': 0.20 * W, 'floor': 0.10}),
        ('matched', {'Rs': R1 + 0.15 * W, 'wd': 0.25 * W, 'floor': 0.10}),
        ('smoothbox', {'edge': 0.30 * W}),
    ]
    shifts = [
        ('cos', [R1, R2]),
        ('cos', [R1 - 0.25 * W, R2 + 0.25 * W]),
        ('cos', [R1, R2 + 0.50 * W]),
        ('quintic', [R1 - 0.25 * W, R2 + 0.25 * W]),
    ]
    out = []
    for kind, params in profs:
        for sk, ws in shifts:
            out.append(dict(kind=kind, params=params, shift_kind=sk, ws=ws,
                            sr=0.20 * W, sp=0.116 * W))
    return out


GEOS = [(10.0, 20.0), (10.0, 15.0), (10.0, 30.0),
        (20.0, 40.0), (5.0, 10.0), (30.0, 60.0)]


def run_rung(beta, tag):
    path = f'results/trackL_b{tag}.json'
    state = {'beta': beta, 'rows': [], 'winner': None}
    t0 = time.time()

    def save():
        json.dump(state, open(path, 'w'), indent=1)

    def ev(R1, R2, M, d, h=None, pts=None):
        r = eval_shell(R1, R2, M, d['kind'], d['params'], d['sr'], d['sp'],
                       beta, d['shift_kind'], d['ws'], h=h, pts=pts)
        r['phase'] = state.get('phase', '')
        state['rows'].append(r)
        print(f"  [{state.get('phase','')}] R=({R1},{R2}) M={M:.2f} "
              f"{d['kind'][:4]}/{d['shift_kind']} ws={d['ws']} "
              f"worst={r['worst']:+.3e} ({r['worst_kind']} @r={r['worst_radius']:.1f}) "
              f"tI={r['typeI_frac_sig']:.2f} [{time.time()-t0:.0f}s]", flush=True)
        save()
        return r

    # Phase A: base geometry, all designs, M ladder
    state['phase'] = 'A'
    R1, R2 = 10.0, 20.0
    ptsA, _ = sample_points(R1, R2)
    ladderA = [2.7, 4.0, 6.0, 9.0]
    resultsA = []
    for d in designs(R1, R2):
        best = None
        for M in ladderA:
            r = ev(R1, R2, M, d, pts=ptsA)
            if best is None or r['worst'] > best['worst']:
                best = r
            if r['worst'] > 0 and r['typeI_frac_sig'] == 1.0:
                break
        resultsA.append((best, d))
    resultsA.sort(key=lambda t: -t[0]['worst'])

    # Phase B: top-3 designs on other geometries, scaled M ladder
    state['phase'] = 'B'
    top = resultsA[:3]
    for R1b, R2b in GEOS[1:]:
        ptsB, _ = sample_points(R1b, R2b)
        W = R2b - R1b
        for _, d0 in top:
            d = designs(R1b, R2b)[0]  # placeholder replaced below
            # rebuild the same design at this geometry's scale
            idx = designs(10.0, 20.0).index(d0) if d0 in designs(10.0, 20.0) else 0
            d = designs(R1b, R2b)[idx]
            for Mrel in (0.27, 0.45, 0.7, 1.0):
                M = Mrel * R1b
                r = ev(R1b, R2b, M, d, pts=ptsB)
                if r['worst'] > 0 and r['typeI_frac_sig'] == 1.0:
                    break

    # Phase C: bisect min M for every (design, geo) that passed somewhere
    state['phase'] = 'C'
    passed = {}
    for r in state['rows']:
        if r['worst'] > 0 and r['typeI_frac_sig'] == 1.0:
            key = (r['R1'], r['R2'], r['kind'], json.dumps(r['params']),
                   r['shift_kind'], json.dumps(r['ws']))
            if key not in passed or r['M_geom'] < passed[key]['M_geom']:
                passed[key] = r
    winners = []
    for key, r0 in passed.items():
        R1c, R2c = r0['R1'], r0['R2']
        ptsC, _ = sample_points(R1c, R2c)
        d = dict(kind=r0['kind'], params=r0['params'], shift_kind=r0['shift_kind'],
                 ws=r0['ws'], sr=r0['s_rho'], sp=r0['s_P'])
        lo = None  # largest known fail below
        hi = r0['M_geom']
        cand = [x for x in state['rows']
                if x['R1'] == R1c and x['R2'] == R2c and x['kind'] == d['kind']
                and x['shift_kind'] == d['shift_kind'] and x['ws'] == d['ws']
                and x['M_geom'] < hi and not (x['worst'] > 0 and x['typeI_frac_sig'] == 1.0)]
        if cand:
            lo = max(x['M_geom'] for x in cand)
        for _ in range(3):
            if lo is None:
                Mtry = hi * 0.75
            else:
                if hi - lo < 0.15:
                    break
                Mtry = 0.5 * (lo + hi)
            r = ev(R1c, R2c, Mtry, d, pts=ptsC)
            if r['worst'] > 0 and r['typeI_frac_sig'] == 1.0:
                hi = Mtry
            else:
                lo = Mtry
        # confirm winner at h/2 on dense points
        ptsD, _ = sample_points(R1c, R2c, ndir=26)
        rc = ev(R1c, R2c, hi, d, h=0.015 * R1c, pts=ptsD)
        rc['confirmed'] = bool(rc['worst'] > 0 and rc['typeI_frac_sig'] == 1.0)
        winners.append(rc)
        print(f"  WINNER-CANDIDATE beta={beta}: M={hi:.3f} geom "
              f"({rc['M_kg']:.3e} kg) confirmed={rc['confirmed']} "
              f"worst={rc['worst']:+.3e}", flush=True)
    if winners:
        ok = [w for w in winners if w['confirmed']]
        if ok:
            state['winner'] = min(ok, key=lambda w: w['M_geom'])
    state['n_evals'] = len(state['rows'])
    state['elapsed_s'] = time.time() - t0
    save()
    print(f"RUNG beta={beta} DONE: {len(state['rows'])} evals, "
          f"winner={state['winner'] is not None}", flush=True)


if __name__ == '__main__':
    beta = float(sys.argv[1])
    run_rung(beta, sys.argv[2] if len(sys.argv) > 2 else f"{beta}")
